# SNMP MIB module (JNX-OPT-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JNX-OPT-IF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:12:42 2024
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

(jnxoptIfMibRoot,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxoptIfMibRoot")

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

jnxoptIfMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1)
)
jnxoptIfMibModule.setRevisions(
        ("2003-08-13 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JnxoptIfAcTI(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )



class JnxoptIfBitRateK(Integer32, TextualConvention):
    status = "current"


class JnxoptIfDEGM(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )



class JnxoptIfDEGThr(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )



class JnxoptIfDirectionality(Integer32, TextualConvention):
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



class JnxoptIfSinkOrSource(Integer32, TextualConvention):
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



class JnxoptIfExDAPI(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )



class JnxoptIfExSAPI(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )



class JnxoptIfIntervalNumber(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )



class JnxoptIfTIMDetMode(Integer32, TextualConvention):
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



class JnxoptIfTxTI(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )



# MIB Managed Objects in the order of their OIDs

_JnxoptIfObjects_ObjectIdentity = ObjectIdentity
jnxoptIfObjects = _JnxoptIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1)
)
_JnxoptIfOTMn_ObjectIdentity = ObjectIdentity
jnxoptIfOTMn = _JnxoptIfOTMn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 1)
)
_JnxoptIfOTMnTable_Object = MibTable
jnxoptIfOTMnTable = _JnxoptIfOTMnTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxoptIfOTMnTable.setStatus("current")
_JnxoptIfOTMnEntry_Object = MibTableRow
jnxoptIfOTMnEntry = _JnxoptIfOTMnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 1, 1, 1)
)
jnxoptIfOTMnEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxoptIfOTMnEntry.setStatus("current")


class _JnxoptIfOTMnOrder_Type(Unsigned32):
    """Custom type jnxoptIfOTMnOrder based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_JnxoptIfOTMnOrder_Type.__name__ = "Unsigned32"
_JnxoptIfOTMnOrder_Object = MibTableColumn
jnxoptIfOTMnOrder = _JnxoptIfOTMnOrder_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 1, 1, 1, 1),
    _JnxoptIfOTMnOrder_Type()
)
jnxoptIfOTMnOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTMnOrder.setStatus("current")
_JnxoptIfOTMnReduced_Type = TruthValue
_JnxoptIfOTMnReduced_Object = MibTableColumn
jnxoptIfOTMnReduced = _JnxoptIfOTMnReduced_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 1, 1, 1, 2),
    _JnxoptIfOTMnReduced_Type()
)
jnxoptIfOTMnReduced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTMnReduced.setStatus("current")


class _JnxoptIfOTMnBitRates_Type(Bits):
    """Custom type jnxoptIfOTMnBitRates based on Bits"""
    namedValues = NamedValues(
        *(("bitRateK1", 0),
          ("bitRateK2", 1),
          ("bitRateK3", 2))
    )

_JnxoptIfOTMnBitRates_Type.__name__ = "Bits"
_JnxoptIfOTMnBitRates_Object = MibTableColumn
jnxoptIfOTMnBitRates = _JnxoptIfOTMnBitRates_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 1, 1, 1, 3),
    _JnxoptIfOTMnBitRates_Type()
)
jnxoptIfOTMnBitRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTMnBitRates.setStatus("current")
_JnxoptIfOTMnInterfaceType_Type = SnmpAdminString
_JnxoptIfOTMnInterfaceType_Object = MibTableColumn
jnxoptIfOTMnInterfaceType = _JnxoptIfOTMnInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 1, 1, 1, 4),
    _JnxoptIfOTMnInterfaceType_Type()
)
jnxoptIfOTMnInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTMnInterfaceType.setStatus("current")
_JnxoptIfOTMnTcmMax_Type = Unsigned32
_JnxoptIfOTMnTcmMax_Object = MibTableColumn
jnxoptIfOTMnTcmMax = _JnxoptIfOTMnTcmMax_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 1, 1, 1, 5),
    _JnxoptIfOTMnTcmMax_Type()
)
jnxoptIfOTMnTcmMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOTMnTcmMax.setStatus("current")


class _JnxoptIfOTMnOpticalReach_Type(Integer32):
    """Custom type jnxoptIfOTMnOpticalReach based on Integer32"""
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


_JnxoptIfOTMnOpticalReach_Type.__name__ = "Integer32"
_JnxoptIfOTMnOpticalReach_Object = MibTableColumn
jnxoptIfOTMnOpticalReach = _JnxoptIfOTMnOpticalReach_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 1, 1, 1, 6),
    _JnxoptIfOTMnOpticalReach_Type()
)
jnxoptIfOTMnOpticalReach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTMnOpticalReach.setStatus("current")
_JnxoptIfPerfMon_ObjectIdentity = ObjectIdentity
jnxoptIfPerfMon = _JnxoptIfPerfMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 2)
)
_JnxoptIfPerfMonIntervalTable_Object = MibTable
jnxoptIfPerfMonIntervalTable = _JnxoptIfPerfMonIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    jnxoptIfPerfMonIntervalTable.setStatus("current")
_JnxoptIfPerfMonIntervalEntry_Object = MibTableRow
jnxoptIfPerfMonIntervalEntry = _JnxoptIfPerfMonIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 2, 1, 1)
)
jnxoptIfPerfMonIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxoptIfPerfMonIntervalEntry.setStatus("current")


class _JnxoptIfPerfMonCurrentTimeElapsed_Type(Gauge32):
    """Custom type jnxoptIfPerfMonCurrentTimeElapsed based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_JnxoptIfPerfMonCurrentTimeElapsed_Type.__name__ = "Gauge32"
_JnxoptIfPerfMonCurrentTimeElapsed_Object = MibTableColumn
jnxoptIfPerfMonCurrentTimeElapsed = _JnxoptIfPerfMonCurrentTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 2, 1, 1, 1),
    _JnxoptIfPerfMonCurrentTimeElapsed_Type()
)
jnxoptIfPerfMonCurrentTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfPerfMonCurrentTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfPerfMonCurrentTimeElapsed.setUnits("seconds")


class _JnxoptIfPerfMonCurDayTimeElapsed_Type(Gauge32):
    """Custom type jnxoptIfPerfMonCurDayTimeElapsed based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_JnxoptIfPerfMonCurDayTimeElapsed_Type.__name__ = "Gauge32"
_JnxoptIfPerfMonCurDayTimeElapsed_Object = MibTableColumn
jnxoptIfPerfMonCurDayTimeElapsed = _JnxoptIfPerfMonCurDayTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 2, 1, 1, 2),
    _JnxoptIfPerfMonCurDayTimeElapsed_Type()
)
jnxoptIfPerfMonCurDayTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfPerfMonCurDayTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfPerfMonCurDayTimeElapsed.setUnits("seconds")


class _JnxoptIfPerfMonIntervalNumIntervals_Type(Unsigned32):
    """Custom type jnxoptIfPerfMonIntervalNumIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_JnxoptIfPerfMonIntervalNumIntervals_Type.__name__ = "Unsigned32"
_JnxoptIfPerfMonIntervalNumIntervals_Object = MibTableColumn
jnxoptIfPerfMonIntervalNumIntervals = _JnxoptIfPerfMonIntervalNumIntervals_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 2, 1, 1, 3),
    _JnxoptIfPerfMonIntervalNumIntervals_Type()
)
jnxoptIfPerfMonIntervalNumIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfPerfMonIntervalNumIntervals.setStatus("current")


class _JnxoptIfPerfMonIntervalNumInvalidIntervals_Type(Unsigned32):
    """Custom type jnxoptIfPerfMonIntervalNumInvalidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_JnxoptIfPerfMonIntervalNumInvalidIntervals_Type.__name__ = "Unsigned32"
_JnxoptIfPerfMonIntervalNumInvalidIntervals_Object = MibTableColumn
jnxoptIfPerfMonIntervalNumInvalidIntervals = _JnxoptIfPerfMonIntervalNumInvalidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 2, 1, 1, 4),
    _JnxoptIfPerfMonIntervalNumInvalidIntervals_Type()
)
jnxoptIfPerfMonIntervalNumInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfPerfMonIntervalNumInvalidIntervals.setStatus("current")
_JnxoptIfOTSn_ObjectIdentity = ObjectIdentity
jnxoptIfOTSn = _JnxoptIfOTSn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3)
)
_JnxoptIfOTSnConfigTable_Object = MibTable
jnxoptIfOTSnConfigTable = _JnxoptIfOTSnConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    jnxoptIfOTSnConfigTable.setStatus("current")
_JnxoptIfOTSnConfigEntry_Object = MibTableRow
jnxoptIfOTSnConfigEntry = _JnxoptIfOTSnConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 1, 1)
)
jnxoptIfOTSnConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxoptIfOTSnConfigEntry.setStatus("current")
_JnxoptIfOTSnDirectionality_Type = JnxoptIfDirectionality
_JnxoptIfOTSnDirectionality_Object = MibTableColumn
jnxoptIfOTSnDirectionality = _JnxoptIfOTSnDirectionality_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 1, 1, 1),
    _JnxoptIfOTSnDirectionality_Type()
)
jnxoptIfOTSnDirectionality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnDirectionality.setStatus("current")
_JnxoptIfOTSnAprStatus_Type = SnmpAdminString
_JnxoptIfOTSnAprStatus_Object = MibTableColumn
jnxoptIfOTSnAprStatus = _JnxoptIfOTSnAprStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 1, 1, 2),
    _JnxoptIfOTSnAprStatus_Type()
)
jnxoptIfOTSnAprStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnAprStatus.setStatus("current")
_JnxoptIfOTSnAprControl_Type = SnmpAdminString
_JnxoptIfOTSnAprControl_Object = MibTableColumn
jnxoptIfOTSnAprControl = _JnxoptIfOTSnAprControl_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 1, 1, 3),
    _JnxoptIfOTSnAprControl_Type()
)
jnxoptIfOTSnAprControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOTSnAprControl.setStatus("current")
_JnxoptIfOTSnTraceIdentifierTransmitted_Type = JnxoptIfTxTI
_JnxoptIfOTSnTraceIdentifierTransmitted_Object = MibTableColumn
jnxoptIfOTSnTraceIdentifierTransmitted = _JnxoptIfOTSnTraceIdentifierTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 1, 1, 4),
    _JnxoptIfOTSnTraceIdentifierTransmitted_Type()
)
jnxoptIfOTSnTraceIdentifierTransmitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOTSnTraceIdentifierTransmitted.setStatus("current")
_JnxoptIfOTSnDAPIExpected_Type = JnxoptIfExDAPI
_JnxoptIfOTSnDAPIExpected_Object = MibTableColumn
jnxoptIfOTSnDAPIExpected = _JnxoptIfOTSnDAPIExpected_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 1, 1, 5),
    _JnxoptIfOTSnDAPIExpected_Type()
)
jnxoptIfOTSnDAPIExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOTSnDAPIExpected.setStatus("current")
_JnxoptIfOTSnSAPIExpected_Type = JnxoptIfExSAPI
_JnxoptIfOTSnSAPIExpected_Object = MibTableColumn
jnxoptIfOTSnSAPIExpected = _JnxoptIfOTSnSAPIExpected_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 1, 1, 6),
    _JnxoptIfOTSnSAPIExpected_Type()
)
jnxoptIfOTSnSAPIExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSAPIExpected.setStatus("current")
_JnxoptIfOTSnTraceIdentifierAccepted_Type = JnxoptIfAcTI
_JnxoptIfOTSnTraceIdentifierAccepted_Object = MibTableColumn
jnxoptIfOTSnTraceIdentifierAccepted = _JnxoptIfOTSnTraceIdentifierAccepted_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 1, 1, 7),
    _JnxoptIfOTSnTraceIdentifierAccepted_Type()
)
jnxoptIfOTSnTraceIdentifierAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnTraceIdentifierAccepted.setStatus("current")
_JnxoptIfOTSnTIMDetMode_Type = JnxoptIfTIMDetMode
_JnxoptIfOTSnTIMDetMode_Object = MibTableColumn
jnxoptIfOTSnTIMDetMode = _JnxoptIfOTSnTIMDetMode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 1, 1, 8),
    _JnxoptIfOTSnTIMDetMode_Type()
)
jnxoptIfOTSnTIMDetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOTSnTIMDetMode.setStatus("current")
_JnxoptIfOTSnTIMActEnabled_Type = TruthValue
_JnxoptIfOTSnTIMActEnabled_Object = MibTableColumn
jnxoptIfOTSnTIMActEnabled = _JnxoptIfOTSnTIMActEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 1, 1, 9),
    _JnxoptIfOTSnTIMActEnabled_Type()
)
jnxoptIfOTSnTIMActEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOTSnTIMActEnabled.setStatus("current")


class _JnxoptIfOTSnCurrentStatus_Type(Bits):
    """Custom type jnxoptIfOTSnCurrentStatus based on Bits"""
    namedValues = NamedValues(
        *(("bdi", 2),
          ("bdiO", 1),
          ("bdiP", 0),
          ("los", 6),
          ("losO", 5),
          ("losP", 4),
          ("tim", 3))
    )

_JnxoptIfOTSnCurrentStatus_Type.__name__ = "Bits"
_JnxoptIfOTSnCurrentStatus_Object = MibTableColumn
jnxoptIfOTSnCurrentStatus = _JnxoptIfOTSnCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 1, 1, 10),
    _JnxoptIfOTSnCurrentStatus_Type()
)
jnxoptIfOTSnCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnCurrentStatus.setStatus("current")
_JnxoptIfOTSnSinkCurrentTable_Object = MibTable
jnxoptIfOTSnSinkCurrentTable = _JnxoptIfOTSnSinkCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkCurrentTable.setStatus("current")
_JnxoptIfOTSnSinkCurrentEntry_Object = MibTableRow
jnxoptIfOTSnSinkCurrentEntry = _JnxoptIfOTSnSinkCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 2, 1)
)
jnxoptIfOTSnSinkCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkCurrentEntry.setStatus("current")
_JnxoptIfOTSnSinkCurrentSuspectedFlag_Type = TruthValue
_JnxoptIfOTSnSinkCurrentSuspectedFlag_Object = MibTableColumn
jnxoptIfOTSnSinkCurrentSuspectedFlag = _JnxoptIfOTSnSinkCurrentSuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 2, 1, 1),
    _JnxoptIfOTSnSinkCurrentSuspectedFlag_Type()
)
jnxoptIfOTSnSinkCurrentSuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkCurrentSuspectedFlag.setStatus("current")
_JnxoptIfOTSnSinkCurrentInputPower_Type = Integer32
_JnxoptIfOTSnSinkCurrentInputPower_Object = MibTableColumn
jnxoptIfOTSnSinkCurrentInputPower = _JnxoptIfOTSnSinkCurrentInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 2, 1, 2),
    _JnxoptIfOTSnSinkCurrentInputPower_Type()
)
jnxoptIfOTSnSinkCurrentInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkCurrentInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkCurrentInputPower.setUnits("0.1 dbm")
_JnxoptIfOTSnSinkCurrentLowInputPower_Type = Integer32
_JnxoptIfOTSnSinkCurrentLowInputPower_Object = MibTableColumn
jnxoptIfOTSnSinkCurrentLowInputPower = _JnxoptIfOTSnSinkCurrentLowInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 2, 1, 3),
    _JnxoptIfOTSnSinkCurrentLowInputPower_Type()
)
jnxoptIfOTSnSinkCurrentLowInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkCurrentLowInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkCurrentLowInputPower.setUnits("0.1 dbm")
_JnxoptIfOTSnSinkCurrentHighInputPower_Type = Integer32
_JnxoptIfOTSnSinkCurrentHighInputPower_Object = MibTableColumn
jnxoptIfOTSnSinkCurrentHighInputPower = _JnxoptIfOTSnSinkCurrentHighInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 2, 1, 4),
    _JnxoptIfOTSnSinkCurrentHighInputPower_Type()
)
jnxoptIfOTSnSinkCurrentHighInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkCurrentHighInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkCurrentHighInputPower.setUnits("0.1 dbm")
_JnxoptIfOTSnSinkCurrentLowerInputPowerThreshold_Type = Integer32
_JnxoptIfOTSnSinkCurrentLowerInputPowerThreshold_Object = MibTableColumn
jnxoptIfOTSnSinkCurrentLowerInputPowerThreshold = _JnxoptIfOTSnSinkCurrentLowerInputPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 2, 1, 5),
    _JnxoptIfOTSnSinkCurrentLowerInputPowerThreshold_Type()
)
jnxoptIfOTSnSinkCurrentLowerInputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkCurrentLowerInputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkCurrentLowerInputPowerThreshold.setUnits("0.1 dbm")
_JnxoptIfOTSnSinkCurrentUpperInputPowerThreshold_Type = Integer32
_JnxoptIfOTSnSinkCurrentUpperInputPowerThreshold_Object = MibTableColumn
jnxoptIfOTSnSinkCurrentUpperInputPowerThreshold = _JnxoptIfOTSnSinkCurrentUpperInputPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 2, 1, 6),
    _JnxoptIfOTSnSinkCurrentUpperInputPowerThreshold_Type()
)
jnxoptIfOTSnSinkCurrentUpperInputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkCurrentUpperInputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkCurrentUpperInputPowerThreshold.setUnits("0.1 dbm")
_JnxoptIfOTSnSinkCurrentOutputPower_Type = Integer32
_JnxoptIfOTSnSinkCurrentOutputPower_Object = MibTableColumn
jnxoptIfOTSnSinkCurrentOutputPower = _JnxoptIfOTSnSinkCurrentOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 2, 1, 7),
    _JnxoptIfOTSnSinkCurrentOutputPower_Type()
)
jnxoptIfOTSnSinkCurrentOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkCurrentOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkCurrentOutputPower.setUnits("0.1 dbm")
_JnxoptIfOTSnSinkCurrentLowOutputPower_Type = Integer32
_JnxoptIfOTSnSinkCurrentLowOutputPower_Object = MibTableColumn
jnxoptIfOTSnSinkCurrentLowOutputPower = _JnxoptIfOTSnSinkCurrentLowOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 2, 1, 8),
    _JnxoptIfOTSnSinkCurrentLowOutputPower_Type()
)
jnxoptIfOTSnSinkCurrentLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkCurrentLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkCurrentLowOutputPower.setUnits("0.1 dbm")
_JnxoptIfOTSnSinkCurrentHighOutputPower_Type = Integer32
_JnxoptIfOTSnSinkCurrentHighOutputPower_Object = MibTableColumn
jnxoptIfOTSnSinkCurrentHighOutputPower = _JnxoptIfOTSnSinkCurrentHighOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 2, 1, 9),
    _JnxoptIfOTSnSinkCurrentHighOutputPower_Type()
)
jnxoptIfOTSnSinkCurrentHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkCurrentHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkCurrentHighOutputPower.setUnits("0.1 dbm")
_JnxoptIfOTSnSinkCurrentLowerOutputPowerThreshold_Type = Integer32
_JnxoptIfOTSnSinkCurrentLowerOutputPowerThreshold_Object = MibTableColumn
jnxoptIfOTSnSinkCurrentLowerOutputPowerThreshold = _JnxoptIfOTSnSinkCurrentLowerOutputPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 2, 1, 10),
    _JnxoptIfOTSnSinkCurrentLowerOutputPowerThreshold_Type()
)
jnxoptIfOTSnSinkCurrentLowerOutputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkCurrentLowerOutputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkCurrentLowerOutputPowerThreshold.setUnits("0.1 dbm")
_JnxoptIfOTSnSinkCurrentUpperOutputPowerThreshold_Type = Integer32
_JnxoptIfOTSnSinkCurrentUpperOutputPowerThreshold_Object = MibTableColumn
jnxoptIfOTSnSinkCurrentUpperOutputPowerThreshold = _JnxoptIfOTSnSinkCurrentUpperOutputPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 2, 1, 11),
    _JnxoptIfOTSnSinkCurrentUpperOutputPowerThreshold_Type()
)
jnxoptIfOTSnSinkCurrentUpperOutputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkCurrentUpperOutputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkCurrentUpperOutputPowerThreshold.setUnits("0.1 dbm")
_JnxoptIfOTSnSinkIntervalTable_Object = MibTable
jnxoptIfOTSnSinkIntervalTable = _JnxoptIfOTSnSinkIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkIntervalTable.setStatus("current")
_JnxoptIfOTSnSinkIntervalEntry_Object = MibTableRow
jnxoptIfOTSnSinkIntervalEntry = _JnxoptIfOTSnSinkIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 3, 1)
)
jnxoptIfOTSnSinkIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "JNX-OPT-IF-MIB", "jnxoptIfOTSnSinkIntervalNumber"),
)
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkIntervalEntry.setStatus("current")
_JnxoptIfOTSnSinkIntervalNumber_Type = JnxoptIfIntervalNumber
_JnxoptIfOTSnSinkIntervalNumber_Object = MibTableColumn
jnxoptIfOTSnSinkIntervalNumber = _JnxoptIfOTSnSinkIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 3, 1, 1),
    _JnxoptIfOTSnSinkIntervalNumber_Type()
)
jnxoptIfOTSnSinkIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkIntervalNumber.setStatus("current")
_JnxoptIfOTSnSinkIntervalSuspectedFlag_Type = TruthValue
_JnxoptIfOTSnSinkIntervalSuspectedFlag_Object = MibTableColumn
jnxoptIfOTSnSinkIntervalSuspectedFlag = _JnxoptIfOTSnSinkIntervalSuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 3, 1, 2),
    _JnxoptIfOTSnSinkIntervalSuspectedFlag_Type()
)
jnxoptIfOTSnSinkIntervalSuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkIntervalSuspectedFlag.setStatus("current")
_JnxoptIfOTSnSinkIntervalLastInputPower_Type = Integer32
_JnxoptIfOTSnSinkIntervalLastInputPower_Object = MibTableColumn
jnxoptIfOTSnSinkIntervalLastInputPower = _JnxoptIfOTSnSinkIntervalLastInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 3, 1, 3),
    _JnxoptIfOTSnSinkIntervalLastInputPower_Type()
)
jnxoptIfOTSnSinkIntervalLastInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkIntervalLastInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkIntervalLastInputPower.setUnits("0.1 dbm")
_JnxoptIfOTSnSinkIntervalLowInputPower_Type = Integer32
_JnxoptIfOTSnSinkIntervalLowInputPower_Object = MibTableColumn
jnxoptIfOTSnSinkIntervalLowInputPower = _JnxoptIfOTSnSinkIntervalLowInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 3, 1, 4),
    _JnxoptIfOTSnSinkIntervalLowInputPower_Type()
)
jnxoptIfOTSnSinkIntervalLowInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkIntervalLowInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkIntervalLowInputPower.setUnits("0.1 dbm")
_JnxoptIfOTSnSinkIntervalHighInputPower_Type = Integer32
_JnxoptIfOTSnSinkIntervalHighInputPower_Object = MibTableColumn
jnxoptIfOTSnSinkIntervalHighInputPower = _JnxoptIfOTSnSinkIntervalHighInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 3, 1, 5),
    _JnxoptIfOTSnSinkIntervalHighInputPower_Type()
)
jnxoptIfOTSnSinkIntervalHighInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkIntervalHighInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkIntervalHighInputPower.setUnits("0.1 dbm")
_JnxoptIfOTSnSinkIntervalLastOutputPower_Type = Integer32
_JnxoptIfOTSnSinkIntervalLastOutputPower_Object = MibTableColumn
jnxoptIfOTSnSinkIntervalLastOutputPower = _JnxoptIfOTSnSinkIntervalLastOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 3, 1, 6),
    _JnxoptIfOTSnSinkIntervalLastOutputPower_Type()
)
jnxoptIfOTSnSinkIntervalLastOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkIntervalLastOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkIntervalLastOutputPower.setUnits("0.1 dbm")
_JnxoptIfOTSnSinkIntervalLowOutputPower_Type = Integer32
_JnxoptIfOTSnSinkIntervalLowOutputPower_Object = MibTableColumn
jnxoptIfOTSnSinkIntervalLowOutputPower = _JnxoptIfOTSnSinkIntervalLowOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 3, 1, 7),
    _JnxoptIfOTSnSinkIntervalLowOutputPower_Type()
)
jnxoptIfOTSnSinkIntervalLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkIntervalLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkIntervalLowOutputPower.setUnits("0.1 dbm")
_JnxoptIfOTSnSinkIntervalHighOutputPower_Type = Integer32
_JnxoptIfOTSnSinkIntervalHighOutputPower_Object = MibTableColumn
jnxoptIfOTSnSinkIntervalHighOutputPower = _JnxoptIfOTSnSinkIntervalHighOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 3, 1, 8),
    _JnxoptIfOTSnSinkIntervalHighOutputPower_Type()
)
jnxoptIfOTSnSinkIntervalHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkIntervalHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkIntervalHighOutputPower.setUnits("0.1 dbm")
_JnxoptIfOTSnSinkCurDayTable_Object = MibTable
jnxoptIfOTSnSinkCurDayTable = _JnxoptIfOTSnSinkCurDayTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 4)
)
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkCurDayTable.setStatus("current")
_JnxoptIfOTSnSinkCurDayEntry_Object = MibTableRow
jnxoptIfOTSnSinkCurDayEntry = _JnxoptIfOTSnSinkCurDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 4, 1)
)
jnxoptIfOTSnSinkCurDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkCurDayEntry.setStatus("current")
_JnxoptIfOTSnSinkCurDaySuspectedFlag_Type = TruthValue
_JnxoptIfOTSnSinkCurDaySuspectedFlag_Object = MibTableColumn
jnxoptIfOTSnSinkCurDaySuspectedFlag = _JnxoptIfOTSnSinkCurDaySuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 4, 1, 1),
    _JnxoptIfOTSnSinkCurDaySuspectedFlag_Type()
)
jnxoptIfOTSnSinkCurDaySuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkCurDaySuspectedFlag.setStatus("current")
_JnxoptIfOTSnSinkCurDayLowInputPower_Type = Integer32
_JnxoptIfOTSnSinkCurDayLowInputPower_Object = MibTableColumn
jnxoptIfOTSnSinkCurDayLowInputPower = _JnxoptIfOTSnSinkCurDayLowInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 4, 1, 2),
    _JnxoptIfOTSnSinkCurDayLowInputPower_Type()
)
jnxoptIfOTSnSinkCurDayLowInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkCurDayLowInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkCurDayLowInputPower.setUnits("0.1 dbm")
_JnxoptIfOTSnSinkCurDayHighInputPower_Type = Integer32
_JnxoptIfOTSnSinkCurDayHighInputPower_Object = MibTableColumn
jnxoptIfOTSnSinkCurDayHighInputPower = _JnxoptIfOTSnSinkCurDayHighInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 4, 1, 3),
    _JnxoptIfOTSnSinkCurDayHighInputPower_Type()
)
jnxoptIfOTSnSinkCurDayHighInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkCurDayHighInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkCurDayHighInputPower.setUnits("0.1 dbm")
_JnxoptIfOTSnSinkCurDayLowOutputPower_Type = Integer32
_JnxoptIfOTSnSinkCurDayLowOutputPower_Object = MibTableColumn
jnxoptIfOTSnSinkCurDayLowOutputPower = _JnxoptIfOTSnSinkCurDayLowOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 4, 1, 4),
    _JnxoptIfOTSnSinkCurDayLowOutputPower_Type()
)
jnxoptIfOTSnSinkCurDayLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkCurDayLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkCurDayLowOutputPower.setUnits("0.1 dbm")
_JnxoptIfOTSnSinkCurDayHighOutputPower_Type = Integer32
_JnxoptIfOTSnSinkCurDayHighOutputPower_Object = MibTableColumn
jnxoptIfOTSnSinkCurDayHighOutputPower = _JnxoptIfOTSnSinkCurDayHighOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 4, 1, 5),
    _JnxoptIfOTSnSinkCurDayHighOutputPower_Type()
)
jnxoptIfOTSnSinkCurDayHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkCurDayHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkCurDayHighOutputPower.setUnits("0.1 dbm")
_JnxoptIfOTSnSinkPrevDayTable_Object = MibTable
jnxoptIfOTSnSinkPrevDayTable = _JnxoptIfOTSnSinkPrevDayTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 5)
)
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkPrevDayTable.setStatus("current")
_JnxoptIfOTSnSinkPrevDayEntry_Object = MibTableRow
jnxoptIfOTSnSinkPrevDayEntry = _JnxoptIfOTSnSinkPrevDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 5, 1)
)
jnxoptIfOTSnSinkPrevDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkPrevDayEntry.setStatus("current")
_JnxoptIfOTSnSinkPrevDaySuspectedFlag_Type = TruthValue
_JnxoptIfOTSnSinkPrevDaySuspectedFlag_Object = MibTableColumn
jnxoptIfOTSnSinkPrevDaySuspectedFlag = _JnxoptIfOTSnSinkPrevDaySuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 5, 1, 1),
    _JnxoptIfOTSnSinkPrevDaySuspectedFlag_Type()
)
jnxoptIfOTSnSinkPrevDaySuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkPrevDaySuspectedFlag.setStatus("current")
_JnxoptIfOTSnSinkPrevDayLastInputPower_Type = Integer32
_JnxoptIfOTSnSinkPrevDayLastInputPower_Object = MibTableColumn
jnxoptIfOTSnSinkPrevDayLastInputPower = _JnxoptIfOTSnSinkPrevDayLastInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 5, 1, 2),
    _JnxoptIfOTSnSinkPrevDayLastInputPower_Type()
)
jnxoptIfOTSnSinkPrevDayLastInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkPrevDayLastInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkPrevDayLastInputPower.setUnits("0.1 dbm")
_JnxoptIfOTSnSinkPrevDayLowInputPower_Type = Integer32
_JnxoptIfOTSnSinkPrevDayLowInputPower_Object = MibTableColumn
jnxoptIfOTSnSinkPrevDayLowInputPower = _JnxoptIfOTSnSinkPrevDayLowInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 5, 1, 3),
    _JnxoptIfOTSnSinkPrevDayLowInputPower_Type()
)
jnxoptIfOTSnSinkPrevDayLowInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkPrevDayLowInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkPrevDayLowInputPower.setUnits("0.1 dbm")
_JnxoptIfOTSnSinkPrevDayHighInputPower_Type = Integer32
_JnxoptIfOTSnSinkPrevDayHighInputPower_Object = MibTableColumn
jnxoptIfOTSnSinkPrevDayHighInputPower = _JnxoptIfOTSnSinkPrevDayHighInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 5, 1, 4),
    _JnxoptIfOTSnSinkPrevDayHighInputPower_Type()
)
jnxoptIfOTSnSinkPrevDayHighInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkPrevDayHighInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkPrevDayHighInputPower.setUnits("0.1 dbm")
_JnxoptIfOTSnSinkPrevDayLastOutputPower_Type = Integer32
_JnxoptIfOTSnSinkPrevDayLastOutputPower_Object = MibTableColumn
jnxoptIfOTSnSinkPrevDayLastOutputPower = _JnxoptIfOTSnSinkPrevDayLastOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 5, 1, 5),
    _JnxoptIfOTSnSinkPrevDayLastOutputPower_Type()
)
jnxoptIfOTSnSinkPrevDayLastOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkPrevDayLastOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkPrevDayLastOutputPower.setUnits("0.1 dbm")
_JnxoptIfOTSnSinkPrevDayLowOutputPower_Type = Integer32
_JnxoptIfOTSnSinkPrevDayLowOutputPower_Object = MibTableColumn
jnxoptIfOTSnSinkPrevDayLowOutputPower = _JnxoptIfOTSnSinkPrevDayLowOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 5, 1, 6),
    _JnxoptIfOTSnSinkPrevDayLowOutputPower_Type()
)
jnxoptIfOTSnSinkPrevDayLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkPrevDayLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkPrevDayLowOutputPower.setUnits("0.1 dbm")
_JnxoptIfOTSnSinkPrevDayHighOutputPower_Type = Integer32
_JnxoptIfOTSnSinkPrevDayHighOutputPower_Object = MibTableColumn
jnxoptIfOTSnSinkPrevDayHighOutputPower = _JnxoptIfOTSnSinkPrevDayHighOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 5, 1, 7),
    _JnxoptIfOTSnSinkPrevDayHighOutputPower_Type()
)
jnxoptIfOTSnSinkPrevDayHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkPrevDayHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkPrevDayHighOutputPower.setUnits("0.1 dbm")
_JnxoptIfOTSnSrcCurrentTable_Object = MibTable
jnxoptIfOTSnSrcCurrentTable = _JnxoptIfOTSnSrcCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 6)
)
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcCurrentTable.setStatus("current")
_JnxoptIfOTSnSrcCurrentEntry_Object = MibTableRow
jnxoptIfOTSnSrcCurrentEntry = _JnxoptIfOTSnSrcCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 6, 1)
)
jnxoptIfOTSnSrcCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcCurrentEntry.setStatus("current")
_JnxoptIfOTSnSrcCurrentSuspectedFlag_Type = TruthValue
_JnxoptIfOTSnSrcCurrentSuspectedFlag_Object = MibTableColumn
jnxoptIfOTSnSrcCurrentSuspectedFlag = _JnxoptIfOTSnSrcCurrentSuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 6, 1, 1),
    _JnxoptIfOTSnSrcCurrentSuspectedFlag_Type()
)
jnxoptIfOTSnSrcCurrentSuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcCurrentSuspectedFlag.setStatus("current")
_JnxoptIfOTSnSrcCurrentOutputPower_Type = Integer32
_JnxoptIfOTSnSrcCurrentOutputPower_Object = MibTableColumn
jnxoptIfOTSnSrcCurrentOutputPower = _JnxoptIfOTSnSrcCurrentOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 6, 1, 2),
    _JnxoptIfOTSnSrcCurrentOutputPower_Type()
)
jnxoptIfOTSnSrcCurrentOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcCurrentOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcCurrentOutputPower.setUnits("0.1 dbm")
_JnxoptIfOTSnSrcCurrentLowOutputPower_Type = Integer32
_JnxoptIfOTSnSrcCurrentLowOutputPower_Object = MibTableColumn
jnxoptIfOTSnSrcCurrentLowOutputPower = _JnxoptIfOTSnSrcCurrentLowOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 6, 1, 3),
    _JnxoptIfOTSnSrcCurrentLowOutputPower_Type()
)
jnxoptIfOTSnSrcCurrentLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcCurrentLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcCurrentLowOutputPower.setUnits("0.1 dbm")
_JnxoptIfOTSnSrcCurrentHighOutputPower_Type = Integer32
_JnxoptIfOTSnSrcCurrentHighOutputPower_Object = MibTableColumn
jnxoptIfOTSnSrcCurrentHighOutputPower = _JnxoptIfOTSnSrcCurrentHighOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 6, 1, 4),
    _JnxoptIfOTSnSrcCurrentHighOutputPower_Type()
)
jnxoptIfOTSnSrcCurrentHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcCurrentHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcCurrentHighOutputPower.setUnits("0.1 dbm")
_JnxoptIfOTSnSrcCurrentLowerOutputPowerThreshold_Type = Integer32
_JnxoptIfOTSnSrcCurrentLowerOutputPowerThreshold_Object = MibTableColumn
jnxoptIfOTSnSrcCurrentLowerOutputPowerThreshold = _JnxoptIfOTSnSrcCurrentLowerOutputPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 6, 1, 5),
    _JnxoptIfOTSnSrcCurrentLowerOutputPowerThreshold_Type()
)
jnxoptIfOTSnSrcCurrentLowerOutputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcCurrentLowerOutputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcCurrentLowerOutputPowerThreshold.setUnits("0.1 dbm")
_JnxoptIfOTSnSrcCurrentUpperOutputPowerThreshold_Type = Integer32
_JnxoptIfOTSnSrcCurrentUpperOutputPowerThreshold_Object = MibTableColumn
jnxoptIfOTSnSrcCurrentUpperOutputPowerThreshold = _JnxoptIfOTSnSrcCurrentUpperOutputPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 6, 1, 6),
    _JnxoptIfOTSnSrcCurrentUpperOutputPowerThreshold_Type()
)
jnxoptIfOTSnSrcCurrentUpperOutputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcCurrentUpperOutputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcCurrentUpperOutputPowerThreshold.setUnits("0.1 dbm")
_JnxoptIfOTSnSrcCurrentInputPower_Type = Integer32
_JnxoptIfOTSnSrcCurrentInputPower_Object = MibTableColumn
jnxoptIfOTSnSrcCurrentInputPower = _JnxoptIfOTSnSrcCurrentInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 6, 1, 7),
    _JnxoptIfOTSnSrcCurrentInputPower_Type()
)
jnxoptIfOTSnSrcCurrentInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcCurrentInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcCurrentInputPower.setUnits("0.1 dbm")
_JnxoptIfOTSnSrcCurrentLowInputPower_Type = Integer32
_JnxoptIfOTSnSrcCurrentLowInputPower_Object = MibTableColumn
jnxoptIfOTSnSrcCurrentLowInputPower = _JnxoptIfOTSnSrcCurrentLowInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 6, 1, 8),
    _JnxoptIfOTSnSrcCurrentLowInputPower_Type()
)
jnxoptIfOTSnSrcCurrentLowInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcCurrentLowInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcCurrentLowInputPower.setUnits("0.1 dbm")
_JnxoptIfOTSnSrcCurrentHighInputPower_Type = Integer32
_JnxoptIfOTSnSrcCurrentHighInputPower_Object = MibTableColumn
jnxoptIfOTSnSrcCurrentHighInputPower = _JnxoptIfOTSnSrcCurrentHighInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 6, 1, 9),
    _JnxoptIfOTSnSrcCurrentHighInputPower_Type()
)
jnxoptIfOTSnSrcCurrentHighInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcCurrentHighInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcCurrentHighInputPower.setUnits("0.1 dbm")
_JnxoptIfOTSnSrcCurrentLowerInputPowerThreshold_Type = Integer32
_JnxoptIfOTSnSrcCurrentLowerInputPowerThreshold_Object = MibTableColumn
jnxoptIfOTSnSrcCurrentLowerInputPowerThreshold = _JnxoptIfOTSnSrcCurrentLowerInputPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 6, 1, 10),
    _JnxoptIfOTSnSrcCurrentLowerInputPowerThreshold_Type()
)
jnxoptIfOTSnSrcCurrentLowerInputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcCurrentLowerInputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcCurrentLowerInputPowerThreshold.setUnits("0.1 dbm")
_JnxoptIfOTSnSrcCurrentUpperInputPowerThreshold_Type = Integer32
_JnxoptIfOTSnSrcCurrentUpperInputPowerThreshold_Object = MibTableColumn
jnxoptIfOTSnSrcCurrentUpperInputPowerThreshold = _JnxoptIfOTSnSrcCurrentUpperInputPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 6, 1, 11),
    _JnxoptIfOTSnSrcCurrentUpperInputPowerThreshold_Type()
)
jnxoptIfOTSnSrcCurrentUpperInputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcCurrentUpperInputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcCurrentUpperInputPowerThreshold.setUnits("0.1 dbm")
_JnxoptIfOTSnSrcIntervalTable_Object = MibTable
jnxoptIfOTSnSrcIntervalTable = _JnxoptIfOTSnSrcIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 7)
)
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcIntervalTable.setStatus("current")
_JnxoptIfOTSnSrcIntervalEntry_Object = MibTableRow
jnxoptIfOTSnSrcIntervalEntry = _JnxoptIfOTSnSrcIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 7, 1)
)
jnxoptIfOTSnSrcIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "JNX-OPT-IF-MIB", "jnxoptIfOTSnSrcIntervalNumber"),
)
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcIntervalEntry.setStatus("current")
_JnxoptIfOTSnSrcIntervalNumber_Type = JnxoptIfIntervalNumber
_JnxoptIfOTSnSrcIntervalNumber_Object = MibTableColumn
jnxoptIfOTSnSrcIntervalNumber = _JnxoptIfOTSnSrcIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 7, 1, 1),
    _JnxoptIfOTSnSrcIntervalNumber_Type()
)
jnxoptIfOTSnSrcIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcIntervalNumber.setStatus("current")
_JnxoptIfOTSnSrcIntervalSuspectedFlag_Type = TruthValue
_JnxoptIfOTSnSrcIntervalSuspectedFlag_Object = MibTableColumn
jnxoptIfOTSnSrcIntervalSuspectedFlag = _JnxoptIfOTSnSrcIntervalSuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 7, 1, 2),
    _JnxoptIfOTSnSrcIntervalSuspectedFlag_Type()
)
jnxoptIfOTSnSrcIntervalSuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcIntervalSuspectedFlag.setStatus("current")
_JnxoptIfOTSnSrcIntervalLastOutputPower_Type = Integer32
_JnxoptIfOTSnSrcIntervalLastOutputPower_Object = MibTableColumn
jnxoptIfOTSnSrcIntervalLastOutputPower = _JnxoptIfOTSnSrcIntervalLastOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 7, 1, 3),
    _JnxoptIfOTSnSrcIntervalLastOutputPower_Type()
)
jnxoptIfOTSnSrcIntervalLastOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcIntervalLastOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcIntervalLastOutputPower.setUnits("0.1 dbm")
_JnxoptIfOTSnSrcIntervalLowOutputPower_Type = Integer32
_JnxoptIfOTSnSrcIntervalLowOutputPower_Object = MibTableColumn
jnxoptIfOTSnSrcIntervalLowOutputPower = _JnxoptIfOTSnSrcIntervalLowOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 7, 1, 4),
    _JnxoptIfOTSnSrcIntervalLowOutputPower_Type()
)
jnxoptIfOTSnSrcIntervalLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcIntervalLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcIntervalLowOutputPower.setUnits("0.1 dbm")
_JnxoptIfOTSnSrcIntervalHighOutputPower_Type = Integer32
_JnxoptIfOTSnSrcIntervalHighOutputPower_Object = MibTableColumn
jnxoptIfOTSnSrcIntervalHighOutputPower = _JnxoptIfOTSnSrcIntervalHighOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 7, 1, 5),
    _JnxoptIfOTSnSrcIntervalHighOutputPower_Type()
)
jnxoptIfOTSnSrcIntervalHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcIntervalHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcIntervalHighOutputPower.setUnits("0.1 dbm")
_JnxoptIfOTSnSrcIntervalLastInputPower_Type = Integer32
_JnxoptIfOTSnSrcIntervalLastInputPower_Object = MibTableColumn
jnxoptIfOTSnSrcIntervalLastInputPower = _JnxoptIfOTSnSrcIntervalLastInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 7, 1, 6),
    _JnxoptIfOTSnSrcIntervalLastInputPower_Type()
)
jnxoptIfOTSnSrcIntervalLastInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcIntervalLastInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcIntervalLastInputPower.setUnits("0.1 dbm")
_JnxoptIfOTSnSrcIntervalLowInputPower_Type = Integer32
_JnxoptIfOTSnSrcIntervalLowInputPower_Object = MibTableColumn
jnxoptIfOTSnSrcIntervalLowInputPower = _JnxoptIfOTSnSrcIntervalLowInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 7, 1, 7),
    _JnxoptIfOTSnSrcIntervalLowInputPower_Type()
)
jnxoptIfOTSnSrcIntervalLowInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcIntervalLowInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcIntervalLowInputPower.setUnits("0.1 dbm")
_JnxoptIfOTSnSrcIntervalHighInputPower_Type = Integer32
_JnxoptIfOTSnSrcIntervalHighInputPower_Object = MibTableColumn
jnxoptIfOTSnSrcIntervalHighInputPower = _JnxoptIfOTSnSrcIntervalHighInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 7, 1, 8),
    _JnxoptIfOTSnSrcIntervalHighInputPower_Type()
)
jnxoptIfOTSnSrcIntervalHighInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcIntervalHighInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcIntervalHighInputPower.setUnits("0.1 dbm")
_JnxoptIfOTSnSrcCurDayTable_Object = MibTable
jnxoptIfOTSnSrcCurDayTable = _JnxoptIfOTSnSrcCurDayTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 8)
)
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcCurDayTable.setStatus("current")
_JnxoptIfOTSnSrcCurDayEntry_Object = MibTableRow
jnxoptIfOTSnSrcCurDayEntry = _JnxoptIfOTSnSrcCurDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 8, 1)
)
jnxoptIfOTSnSrcCurDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcCurDayEntry.setStatus("current")
_JnxoptIfOTSnSrcCurDaySuspectedFlag_Type = TruthValue
_JnxoptIfOTSnSrcCurDaySuspectedFlag_Object = MibTableColumn
jnxoptIfOTSnSrcCurDaySuspectedFlag = _JnxoptIfOTSnSrcCurDaySuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 8, 1, 1),
    _JnxoptIfOTSnSrcCurDaySuspectedFlag_Type()
)
jnxoptIfOTSnSrcCurDaySuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcCurDaySuspectedFlag.setStatus("current")
_JnxoptIfOTSnSrcCurDayLowOutputPower_Type = Integer32
_JnxoptIfOTSnSrcCurDayLowOutputPower_Object = MibTableColumn
jnxoptIfOTSnSrcCurDayLowOutputPower = _JnxoptIfOTSnSrcCurDayLowOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 8, 1, 2),
    _JnxoptIfOTSnSrcCurDayLowOutputPower_Type()
)
jnxoptIfOTSnSrcCurDayLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcCurDayLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcCurDayLowOutputPower.setUnits("0.1 dbm")
_JnxoptIfOTSnSrcCurDayHighOutputPower_Type = Integer32
_JnxoptIfOTSnSrcCurDayHighOutputPower_Object = MibTableColumn
jnxoptIfOTSnSrcCurDayHighOutputPower = _JnxoptIfOTSnSrcCurDayHighOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 8, 1, 3),
    _JnxoptIfOTSnSrcCurDayHighOutputPower_Type()
)
jnxoptIfOTSnSrcCurDayHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcCurDayHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcCurDayHighOutputPower.setUnits("0.1 dbm")
_JnxoptIfOTSnSrcCurDayLowInputPower_Type = Integer32
_JnxoptIfOTSnSrcCurDayLowInputPower_Object = MibTableColumn
jnxoptIfOTSnSrcCurDayLowInputPower = _JnxoptIfOTSnSrcCurDayLowInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 8, 1, 4),
    _JnxoptIfOTSnSrcCurDayLowInputPower_Type()
)
jnxoptIfOTSnSrcCurDayLowInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcCurDayLowInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcCurDayLowInputPower.setUnits("0.1 dbm")
_JnxoptIfOTSnSrcCurDayHighInputPower_Type = Integer32
_JnxoptIfOTSnSrcCurDayHighInputPower_Object = MibTableColumn
jnxoptIfOTSnSrcCurDayHighInputPower = _JnxoptIfOTSnSrcCurDayHighInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 8, 1, 5),
    _JnxoptIfOTSnSrcCurDayHighInputPower_Type()
)
jnxoptIfOTSnSrcCurDayHighInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcCurDayHighInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcCurDayHighInputPower.setUnits("0.1 dbm")
_JnxoptIfOTSnSrcPrevDayTable_Object = MibTable
jnxoptIfOTSnSrcPrevDayTable = _JnxoptIfOTSnSrcPrevDayTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 9)
)
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcPrevDayTable.setStatus("current")
_JnxoptIfOTSnSrcPrevDayEntry_Object = MibTableRow
jnxoptIfOTSnSrcPrevDayEntry = _JnxoptIfOTSnSrcPrevDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 9, 1)
)
jnxoptIfOTSnSrcPrevDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcPrevDayEntry.setStatus("current")
_JnxoptIfOTSnSrcPrevDaySuspectedFlag_Type = TruthValue
_JnxoptIfOTSnSrcPrevDaySuspectedFlag_Object = MibTableColumn
jnxoptIfOTSnSrcPrevDaySuspectedFlag = _JnxoptIfOTSnSrcPrevDaySuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 9, 1, 1),
    _JnxoptIfOTSnSrcPrevDaySuspectedFlag_Type()
)
jnxoptIfOTSnSrcPrevDaySuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcPrevDaySuspectedFlag.setStatus("current")
_JnxoptIfOTSnSrcPrevDayLastOutputPower_Type = Integer32
_JnxoptIfOTSnSrcPrevDayLastOutputPower_Object = MibTableColumn
jnxoptIfOTSnSrcPrevDayLastOutputPower = _JnxoptIfOTSnSrcPrevDayLastOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 9, 1, 2),
    _JnxoptIfOTSnSrcPrevDayLastOutputPower_Type()
)
jnxoptIfOTSnSrcPrevDayLastOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcPrevDayLastOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcPrevDayLastOutputPower.setUnits("0.1 dbm")
_JnxoptIfOTSnSrcPrevDayLowOutputPower_Type = Integer32
_JnxoptIfOTSnSrcPrevDayLowOutputPower_Object = MibTableColumn
jnxoptIfOTSnSrcPrevDayLowOutputPower = _JnxoptIfOTSnSrcPrevDayLowOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 9, 1, 3),
    _JnxoptIfOTSnSrcPrevDayLowOutputPower_Type()
)
jnxoptIfOTSnSrcPrevDayLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcPrevDayLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcPrevDayLowOutputPower.setUnits("0.1 dbm")
_JnxoptIfOTSnSrcPrevDayHighOutputPower_Type = Integer32
_JnxoptIfOTSnSrcPrevDayHighOutputPower_Object = MibTableColumn
jnxoptIfOTSnSrcPrevDayHighOutputPower = _JnxoptIfOTSnSrcPrevDayHighOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 9, 1, 4),
    _JnxoptIfOTSnSrcPrevDayHighOutputPower_Type()
)
jnxoptIfOTSnSrcPrevDayHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcPrevDayHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcPrevDayHighOutputPower.setUnits("0.1 dbm")
_JnxoptIfOTSnSrcPrevDayLastInputPower_Type = Integer32
_JnxoptIfOTSnSrcPrevDayLastInputPower_Object = MibTableColumn
jnxoptIfOTSnSrcPrevDayLastInputPower = _JnxoptIfOTSnSrcPrevDayLastInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 9, 1, 5),
    _JnxoptIfOTSnSrcPrevDayLastInputPower_Type()
)
jnxoptIfOTSnSrcPrevDayLastInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcPrevDayLastInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcPrevDayLastInputPower.setUnits("0.1 dbm")
_JnxoptIfOTSnSrcPrevDayLowInputPower_Type = Integer32
_JnxoptIfOTSnSrcPrevDayLowInputPower_Object = MibTableColumn
jnxoptIfOTSnSrcPrevDayLowInputPower = _JnxoptIfOTSnSrcPrevDayLowInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 9, 1, 6),
    _JnxoptIfOTSnSrcPrevDayLowInputPower_Type()
)
jnxoptIfOTSnSrcPrevDayLowInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcPrevDayLowInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcPrevDayLowInputPower.setUnits("0.1 dbm")
_JnxoptIfOTSnSrcPrevDayHighInputPower_Type = Integer32
_JnxoptIfOTSnSrcPrevDayHighInputPower_Object = MibTableColumn
jnxoptIfOTSnSrcPrevDayHighInputPower = _JnxoptIfOTSnSrcPrevDayHighInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 3, 9, 1, 7),
    _JnxoptIfOTSnSrcPrevDayHighInputPower_Type()
)
jnxoptIfOTSnSrcPrevDayHighInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcPrevDayHighInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTSnSrcPrevDayHighInputPower.setUnits("0.1 dbm")
_JnxoptIfOMSn_ObjectIdentity = ObjectIdentity
jnxoptIfOMSn = _JnxoptIfOMSn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4)
)
_JnxoptIfOMSnConfigTable_Object = MibTable
jnxoptIfOMSnConfigTable = _JnxoptIfOMSnConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    jnxoptIfOMSnConfigTable.setStatus("current")
_JnxoptIfOMSnConfigEntry_Object = MibTableRow
jnxoptIfOMSnConfigEntry = _JnxoptIfOMSnConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 1, 1)
)
jnxoptIfOMSnConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxoptIfOMSnConfigEntry.setStatus("current")
_JnxoptIfOMSnDirectionality_Type = JnxoptIfDirectionality
_JnxoptIfOMSnDirectionality_Object = MibTableColumn
jnxoptIfOMSnDirectionality = _JnxoptIfOMSnDirectionality_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 1, 1, 1),
    _JnxoptIfOMSnDirectionality_Type()
)
jnxoptIfOMSnDirectionality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnDirectionality.setStatus("current")


class _JnxoptIfOMSnCurrentStatus_Type(Bits):
    """Custom type jnxoptIfOMSnCurrentStatus based on Bits"""
    namedValues = NamedValues(
        *(("bdi", 5),
          ("bdiO", 4),
          ("bdiP", 3),
          ("losP", 6),
          ("ssf", 2),
          ("ssfO", 1),
          ("ssfP", 0))
    )

_JnxoptIfOMSnCurrentStatus_Type.__name__ = "Bits"
_JnxoptIfOMSnCurrentStatus_Object = MibTableColumn
jnxoptIfOMSnCurrentStatus = _JnxoptIfOMSnCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 1, 1, 2),
    _JnxoptIfOMSnCurrentStatus_Type()
)
jnxoptIfOMSnCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnCurrentStatus.setStatus("current")
_JnxoptIfOMSnSinkCurrentTable_Object = MibTable
jnxoptIfOMSnSinkCurrentTable = _JnxoptIfOMSnSinkCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkCurrentTable.setStatus("current")
_JnxoptIfOMSnSinkCurrentEntry_Object = MibTableRow
jnxoptIfOMSnSinkCurrentEntry = _JnxoptIfOMSnSinkCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 2, 1)
)
jnxoptIfOMSnSinkCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkCurrentEntry.setStatus("current")
_JnxoptIfOMSnSinkCurrentSuspectedFlag_Type = TruthValue
_JnxoptIfOMSnSinkCurrentSuspectedFlag_Object = MibTableColumn
jnxoptIfOMSnSinkCurrentSuspectedFlag = _JnxoptIfOMSnSinkCurrentSuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 2, 1, 1),
    _JnxoptIfOMSnSinkCurrentSuspectedFlag_Type()
)
jnxoptIfOMSnSinkCurrentSuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkCurrentSuspectedFlag.setStatus("current")
_JnxoptIfOMSnSinkCurrentAggregatedInputPower_Type = Integer32
_JnxoptIfOMSnSinkCurrentAggregatedInputPower_Object = MibTableColumn
jnxoptIfOMSnSinkCurrentAggregatedInputPower = _JnxoptIfOMSnSinkCurrentAggregatedInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 2, 1, 2),
    _JnxoptIfOMSnSinkCurrentAggregatedInputPower_Type()
)
jnxoptIfOMSnSinkCurrentAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkCurrentAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkCurrentAggregatedInputPower.setUnits("0.1 dbm")
_JnxoptIfOMSnSinkCurrentLowAggregatedInputPower_Type = Integer32
_JnxoptIfOMSnSinkCurrentLowAggregatedInputPower_Object = MibTableColumn
jnxoptIfOMSnSinkCurrentLowAggregatedInputPower = _JnxoptIfOMSnSinkCurrentLowAggregatedInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 2, 1, 3),
    _JnxoptIfOMSnSinkCurrentLowAggregatedInputPower_Type()
)
jnxoptIfOMSnSinkCurrentLowAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkCurrentLowAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkCurrentLowAggregatedInputPower.setUnits("0.1 dbm")
_JnxoptIfOMSnSinkCurrentHighAggregatedInputPower_Type = Integer32
_JnxoptIfOMSnSinkCurrentHighAggregatedInputPower_Object = MibTableColumn
jnxoptIfOMSnSinkCurrentHighAggregatedInputPower = _JnxoptIfOMSnSinkCurrentHighAggregatedInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 2, 1, 4),
    _JnxoptIfOMSnSinkCurrentHighAggregatedInputPower_Type()
)
jnxoptIfOMSnSinkCurrentHighAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkCurrentHighAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkCurrentHighAggregatedInputPower.setUnits("0.1 dbm")
_JnxoptIfOMSnSinkCurrentLowerInputPowerThreshold_Type = Integer32
_JnxoptIfOMSnSinkCurrentLowerInputPowerThreshold_Object = MibTableColumn
jnxoptIfOMSnSinkCurrentLowerInputPowerThreshold = _JnxoptIfOMSnSinkCurrentLowerInputPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 2, 1, 5),
    _JnxoptIfOMSnSinkCurrentLowerInputPowerThreshold_Type()
)
jnxoptIfOMSnSinkCurrentLowerInputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkCurrentLowerInputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkCurrentLowerInputPowerThreshold.setUnits("0.1 dbm")
_JnxoptIfOMSnSinkCurrentUpperInputPowerThreshold_Type = Integer32
_JnxoptIfOMSnSinkCurrentUpperInputPowerThreshold_Object = MibTableColumn
jnxoptIfOMSnSinkCurrentUpperInputPowerThreshold = _JnxoptIfOMSnSinkCurrentUpperInputPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 2, 1, 6),
    _JnxoptIfOMSnSinkCurrentUpperInputPowerThreshold_Type()
)
jnxoptIfOMSnSinkCurrentUpperInputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkCurrentUpperInputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkCurrentUpperInputPowerThreshold.setUnits("0.1 dbm")
_JnxoptIfOMSnSinkCurrentOutputPower_Type = Integer32
_JnxoptIfOMSnSinkCurrentOutputPower_Object = MibTableColumn
jnxoptIfOMSnSinkCurrentOutputPower = _JnxoptIfOMSnSinkCurrentOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 2, 1, 7),
    _JnxoptIfOMSnSinkCurrentOutputPower_Type()
)
jnxoptIfOMSnSinkCurrentOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkCurrentOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkCurrentOutputPower.setUnits("0.1 dbm")
_JnxoptIfOMSnSinkCurrentLowOutputPower_Type = Integer32
_JnxoptIfOMSnSinkCurrentLowOutputPower_Object = MibTableColumn
jnxoptIfOMSnSinkCurrentLowOutputPower = _JnxoptIfOMSnSinkCurrentLowOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 2, 1, 8),
    _JnxoptIfOMSnSinkCurrentLowOutputPower_Type()
)
jnxoptIfOMSnSinkCurrentLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkCurrentLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkCurrentLowOutputPower.setUnits("0.1 dbm")
_JnxoptIfOMSnSinkCurrentHighOutputPower_Type = Integer32
_JnxoptIfOMSnSinkCurrentHighOutputPower_Object = MibTableColumn
jnxoptIfOMSnSinkCurrentHighOutputPower = _JnxoptIfOMSnSinkCurrentHighOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 2, 1, 9),
    _JnxoptIfOMSnSinkCurrentHighOutputPower_Type()
)
jnxoptIfOMSnSinkCurrentHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkCurrentHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkCurrentHighOutputPower.setUnits("0.1 dbm")
_JnxoptIfOMSnSinkCurrentLowerOutputPowerThreshold_Type = Integer32
_JnxoptIfOMSnSinkCurrentLowerOutputPowerThreshold_Object = MibTableColumn
jnxoptIfOMSnSinkCurrentLowerOutputPowerThreshold = _JnxoptIfOMSnSinkCurrentLowerOutputPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 2, 1, 10),
    _JnxoptIfOMSnSinkCurrentLowerOutputPowerThreshold_Type()
)
jnxoptIfOMSnSinkCurrentLowerOutputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkCurrentLowerOutputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkCurrentLowerOutputPowerThreshold.setUnits("0.1 dbm")
_JnxoptIfOMSnSinkCurrentUpperOutputPowerThreshold_Type = Integer32
_JnxoptIfOMSnSinkCurrentUpperOutputPowerThreshold_Object = MibTableColumn
jnxoptIfOMSnSinkCurrentUpperOutputPowerThreshold = _JnxoptIfOMSnSinkCurrentUpperOutputPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 2, 1, 11),
    _JnxoptIfOMSnSinkCurrentUpperOutputPowerThreshold_Type()
)
jnxoptIfOMSnSinkCurrentUpperOutputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkCurrentUpperOutputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkCurrentUpperOutputPowerThreshold.setUnits("0.1 dbm")
_JnxoptIfOMSnSinkIntervalTable_Object = MibTable
jnxoptIfOMSnSinkIntervalTable = _JnxoptIfOMSnSinkIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 3)
)
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkIntervalTable.setStatus("current")
_JnxoptIfOMSnSinkIntervalEntry_Object = MibTableRow
jnxoptIfOMSnSinkIntervalEntry = _JnxoptIfOMSnSinkIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 3, 1)
)
jnxoptIfOMSnSinkIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "JNX-OPT-IF-MIB", "jnxoptIfOMSnSinkIntervalNumber"),
)
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkIntervalEntry.setStatus("current")
_JnxoptIfOMSnSinkIntervalNumber_Type = JnxoptIfIntervalNumber
_JnxoptIfOMSnSinkIntervalNumber_Object = MibTableColumn
jnxoptIfOMSnSinkIntervalNumber = _JnxoptIfOMSnSinkIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 3, 1, 1),
    _JnxoptIfOMSnSinkIntervalNumber_Type()
)
jnxoptIfOMSnSinkIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkIntervalNumber.setStatus("current")
_JnxoptIfOMSnSinkIntervalSuspectedFlag_Type = TruthValue
_JnxoptIfOMSnSinkIntervalSuspectedFlag_Object = MibTableColumn
jnxoptIfOMSnSinkIntervalSuspectedFlag = _JnxoptIfOMSnSinkIntervalSuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 3, 1, 2),
    _JnxoptIfOMSnSinkIntervalSuspectedFlag_Type()
)
jnxoptIfOMSnSinkIntervalSuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkIntervalSuspectedFlag.setStatus("current")
_JnxoptIfOMSnSinkIntervalLastAggregatedInputPower_Type = Integer32
_JnxoptIfOMSnSinkIntervalLastAggregatedInputPower_Object = MibTableColumn
jnxoptIfOMSnSinkIntervalLastAggregatedInputPower = _JnxoptIfOMSnSinkIntervalLastAggregatedInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 3, 1, 3),
    _JnxoptIfOMSnSinkIntervalLastAggregatedInputPower_Type()
)
jnxoptIfOMSnSinkIntervalLastAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkIntervalLastAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkIntervalLastAggregatedInputPower.setUnits("0.1 dbm")
_JnxoptIfOMSnSinkIntervalLowAggregatedInputPower_Type = Integer32
_JnxoptIfOMSnSinkIntervalLowAggregatedInputPower_Object = MibTableColumn
jnxoptIfOMSnSinkIntervalLowAggregatedInputPower = _JnxoptIfOMSnSinkIntervalLowAggregatedInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 3, 1, 4),
    _JnxoptIfOMSnSinkIntervalLowAggregatedInputPower_Type()
)
jnxoptIfOMSnSinkIntervalLowAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkIntervalLowAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkIntervalLowAggregatedInputPower.setUnits("0.1 dbm")
_JnxoptIfOMSnSinkIntervalHighAggregatedInputPower_Type = Integer32
_JnxoptIfOMSnSinkIntervalHighAggregatedInputPower_Object = MibTableColumn
jnxoptIfOMSnSinkIntervalHighAggregatedInputPower = _JnxoptIfOMSnSinkIntervalHighAggregatedInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 3, 1, 5),
    _JnxoptIfOMSnSinkIntervalHighAggregatedInputPower_Type()
)
jnxoptIfOMSnSinkIntervalHighAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkIntervalHighAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkIntervalHighAggregatedInputPower.setUnits("0.1 dbm")
_JnxoptIfOMSnSinkIntervalLastOutputPower_Type = Integer32
_JnxoptIfOMSnSinkIntervalLastOutputPower_Object = MibTableColumn
jnxoptIfOMSnSinkIntervalLastOutputPower = _JnxoptIfOMSnSinkIntervalLastOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 3, 1, 6),
    _JnxoptIfOMSnSinkIntervalLastOutputPower_Type()
)
jnxoptIfOMSnSinkIntervalLastOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkIntervalLastOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkIntervalLastOutputPower.setUnits("0.1 dbm")
_JnxoptIfOMSnSinkIntervalLowOutputPower_Type = Integer32
_JnxoptIfOMSnSinkIntervalLowOutputPower_Object = MibTableColumn
jnxoptIfOMSnSinkIntervalLowOutputPower = _JnxoptIfOMSnSinkIntervalLowOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 3, 1, 7),
    _JnxoptIfOMSnSinkIntervalLowOutputPower_Type()
)
jnxoptIfOMSnSinkIntervalLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkIntervalLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkIntervalLowOutputPower.setUnits("0.1 dbm")
_JnxoptIfOMSnSinkIntervalHighOutputPower_Type = Integer32
_JnxoptIfOMSnSinkIntervalHighOutputPower_Object = MibTableColumn
jnxoptIfOMSnSinkIntervalHighOutputPower = _JnxoptIfOMSnSinkIntervalHighOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 3, 1, 8),
    _JnxoptIfOMSnSinkIntervalHighOutputPower_Type()
)
jnxoptIfOMSnSinkIntervalHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkIntervalHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkIntervalHighOutputPower.setUnits("0.1 dbm")
_JnxoptIfOMSnSinkCurDayTable_Object = MibTable
jnxoptIfOMSnSinkCurDayTable = _JnxoptIfOMSnSinkCurDayTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 4)
)
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkCurDayTable.setStatus("current")
_JnxoptIfOMSnSinkCurDayEntry_Object = MibTableRow
jnxoptIfOMSnSinkCurDayEntry = _JnxoptIfOMSnSinkCurDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 4, 1)
)
jnxoptIfOMSnSinkCurDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkCurDayEntry.setStatus("current")
_JnxoptIfOMSnSinkCurDaySuspectedFlag_Type = TruthValue
_JnxoptIfOMSnSinkCurDaySuspectedFlag_Object = MibTableColumn
jnxoptIfOMSnSinkCurDaySuspectedFlag = _JnxoptIfOMSnSinkCurDaySuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 4, 1, 1),
    _JnxoptIfOMSnSinkCurDaySuspectedFlag_Type()
)
jnxoptIfOMSnSinkCurDaySuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkCurDaySuspectedFlag.setStatus("current")
_JnxoptIfOMSnSinkCurDayLowAggregatedInputPower_Type = Integer32
_JnxoptIfOMSnSinkCurDayLowAggregatedInputPower_Object = MibTableColumn
jnxoptIfOMSnSinkCurDayLowAggregatedInputPower = _JnxoptIfOMSnSinkCurDayLowAggregatedInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 4, 1, 2),
    _JnxoptIfOMSnSinkCurDayLowAggregatedInputPower_Type()
)
jnxoptIfOMSnSinkCurDayLowAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkCurDayLowAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkCurDayLowAggregatedInputPower.setUnits("0.1 dbm")
_JnxoptIfOMSnSinkCurDayHighAggregatedInputPower_Type = Integer32
_JnxoptIfOMSnSinkCurDayHighAggregatedInputPower_Object = MibTableColumn
jnxoptIfOMSnSinkCurDayHighAggregatedInputPower = _JnxoptIfOMSnSinkCurDayHighAggregatedInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 4, 1, 3),
    _JnxoptIfOMSnSinkCurDayHighAggregatedInputPower_Type()
)
jnxoptIfOMSnSinkCurDayHighAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkCurDayHighAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkCurDayHighAggregatedInputPower.setUnits("0.1 dbm")
_JnxoptIfOMSnSinkCurDayLowOutputPower_Type = Integer32
_JnxoptIfOMSnSinkCurDayLowOutputPower_Object = MibTableColumn
jnxoptIfOMSnSinkCurDayLowOutputPower = _JnxoptIfOMSnSinkCurDayLowOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 4, 1, 4),
    _JnxoptIfOMSnSinkCurDayLowOutputPower_Type()
)
jnxoptIfOMSnSinkCurDayLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkCurDayLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkCurDayLowOutputPower.setUnits("0.1 dbm")
_JnxoptIfOMSnSinkCurDayHighOutputPower_Type = Integer32
_JnxoptIfOMSnSinkCurDayHighOutputPower_Object = MibTableColumn
jnxoptIfOMSnSinkCurDayHighOutputPower = _JnxoptIfOMSnSinkCurDayHighOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 4, 1, 5),
    _JnxoptIfOMSnSinkCurDayHighOutputPower_Type()
)
jnxoptIfOMSnSinkCurDayHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkCurDayHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkCurDayHighOutputPower.setUnits("0.1 dbm")
_JnxoptIfOMSnSinkPrevDayTable_Object = MibTable
jnxoptIfOMSnSinkPrevDayTable = _JnxoptIfOMSnSinkPrevDayTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 5)
)
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkPrevDayTable.setStatus("current")
_JnxoptIfOMSnSinkPrevDayEntry_Object = MibTableRow
jnxoptIfOMSnSinkPrevDayEntry = _JnxoptIfOMSnSinkPrevDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 5, 1)
)
jnxoptIfOMSnSinkPrevDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkPrevDayEntry.setStatus("current")
_JnxoptIfOMSnSinkPrevDaySuspectedFlag_Type = TruthValue
_JnxoptIfOMSnSinkPrevDaySuspectedFlag_Object = MibTableColumn
jnxoptIfOMSnSinkPrevDaySuspectedFlag = _JnxoptIfOMSnSinkPrevDaySuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 5, 1, 1),
    _JnxoptIfOMSnSinkPrevDaySuspectedFlag_Type()
)
jnxoptIfOMSnSinkPrevDaySuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkPrevDaySuspectedFlag.setStatus("current")
_JnxoptIfOMSnSinkPrevDayLastAggregatedInputPower_Type = Integer32
_JnxoptIfOMSnSinkPrevDayLastAggregatedInputPower_Object = MibTableColumn
jnxoptIfOMSnSinkPrevDayLastAggregatedInputPower = _JnxoptIfOMSnSinkPrevDayLastAggregatedInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 5, 1, 2),
    _JnxoptIfOMSnSinkPrevDayLastAggregatedInputPower_Type()
)
jnxoptIfOMSnSinkPrevDayLastAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkPrevDayLastAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkPrevDayLastAggregatedInputPower.setUnits("0.1 dbm")
_JnxoptIfOMSnSinkPrevDayLowAggregatedInputPower_Type = Integer32
_JnxoptIfOMSnSinkPrevDayLowAggregatedInputPower_Object = MibTableColumn
jnxoptIfOMSnSinkPrevDayLowAggregatedInputPower = _JnxoptIfOMSnSinkPrevDayLowAggregatedInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 5, 1, 3),
    _JnxoptIfOMSnSinkPrevDayLowAggregatedInputPower_Type()
)
jnxoptIfOMSnSinkPrevDayLowAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkPrevDayLowAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkPrevDayLowAggregatedInputPower.setUnits("0.1 dbm")
_JnxoptIfOMSnSinkPrevDayHighAggregatedInputPower_Type = Integer32
_JnxoptIfOMSnSinkPrevDayHighAggregatedInputPower_Object = MibTableColumn
jnxoptIfOMSnSinkPrevDayHighAggregatedInputPower = _JnxoptIfOMSnSinkPrevDayHighAggregatedInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 5, 1, 4),
    _JnxoptIfOMSnSinkPrevDayHighAggregatedInputPower_Type()
)
jnxoptIfOMSnSinkPrevDayHighAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkPrevDayHighAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkPrevDayHighAggregatedInputPower.setUnits("0.1 dbm")
_JnxoptIfOMSnSinkPrevDayLastOutputPower_Type = Integer32
_JnxoptIfOMSnSinkPrevDayLastOutputPower_Object = MibTableColumn
jnxoptIfOMSnSinkPrevDayLastOutputPower = _JnxoptIfOMSnSinkPrevDayLastOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 5, 1, 5),
    _JnxoptIfOMSnSinkPrevDayLastOutputPower_Type()
)
jnxoptIfOMSnSinkPrevDayLastOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkPrevDayLastOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkPrevDayLastOutputPower.setUnits("0.1 dbm")
_JnxoptIfOMSnSinkPrevDayLowOutputPower_Type = Integer32
_JnxoptIfOMSnSinkPrevDayLowOutputPower_Object = MibTableColumn
jnxoptIfOMSnSinkPrevDayLowOutputPower = _JnxoptIfOMSnSinkPrevDayLowOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 5, 1, 6),
    _JnxoptIfOMSnSinkPrevDayLowOutputPower_Type()
)
jnxoptIfOMSnSinkPrevDayLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkPrevDayLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkPrevDayLowOutputPower.setUnits("0.1 dbm")
_JnxoptIfOMSnSinkPrevDayHighOutputPower_Type = Integer32
_JnxoptIfOMSnSinkPrevDayHighOutputPower_Object = MibTableColumn
jnxoptIfOMSnSinkPrevDayHighOutputPower = _JnxoptIfOMSnSinkPrevDayHighOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 5, 1, 7),
    _JnxoptIfOMSnSinkPrevDayHighOutputPower_Type()
)
jnxoptIfOMSnSinkPrevDayHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkPrevDayHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkPrevDayHighOutputPower.setUnits("0.1 dbm")
_JnxoptIfOMSnSrcCurrentTable_Object = MibTable
jnxoptIfOMSnSrcCurrentTable = _JnxoptIfOMSnSrcCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 6)
)
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcCurrentTable.setStatus("current")
_JnxoptIfOMSnSrcCurrentEntry_Object = MibTableRow
jnxoptIfOMSnSrcCurrentEntry = _JnxoptIfOMSnSrcCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 6, 1)
)
jnxoptIfOMSnSrcCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcCurrentEntry.setStatus("current")
_JnxoptIfOMSnSrcCurrentSuspectedFlag_Type = TruthValue
_JnxoptIfOMSnSrcCurrentSuspectedFlag_Object = MibTableColumn
jnxoptIfOMSnSrcCurrentSuspectedFlag = _JnxoptIfOMSnSrcCurrentSuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 6, 1, 1),
    _JnxoptIfOMSnSrcCurrentSuspectedFlag_Type()
)
jnxoptIfOMSnSrcCurrentSuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcCurrentSuspectedFlag.setStatus("current")
_JnxoptIfOMSnSrcCurrentOutputPower_Type = Integer32
_JnxoptIfOMSnSrcCurrentOutputPower_Object = MibTableColumn
jnxoptIfOMSnSrcCurrentOutputPower = _JnxoptIfOMSnSrcCurrentOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 6, 1, 2),
    _JnxoptIfOMSnSrcCurrentOutputPower_Type()
)
jnxoptIfOMSnSrcCurrentOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcCurrentOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcCurrentOutputPower.setUnits("0.1 dbm")
_JnxoptIfOMSnSrcCurrentLowOutputPower_Type = Integer32
_JnxoptIfOMSnSrcCurrentLowOutputPower_Object = MibTableColumn
jnxoptIfOMSnSrcCurrentLowOutputPower = _JnxoptIfOMSnSrcCurrentLowOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 6, 1, 3),
    _JnxoptIfOMSnSrcCurrentLowOutputPower_Type()
)
jnxoptIfOMSnSrcCurrentLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcCurrentLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcCurrentLowOutputPower.setUnits("0.1 dbm")
_JnxoptIfOMSnSrcCurrentHighOutputPower_Type = Integer32
_JnxoptIfOMSnSrcCurrentHighOutputPower_Object = MibTableColumn
jnxoptIfOMSnSrcCurrentHighOutputPower = _JnxoptIfOMSnSrcCurrentHighOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 6, 1, 4),
    _JnxoptIfOMSnSrcCurrentHighOutputPower_Type()
)
jnxoptIfOMSnSrcCurrentHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcCurrentHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcCurrentHighOutputPower.setUnits("0.1 dbm")
_JnxoptIfOMSnSrcCurrentLowerOutputPowerThreshold_Type = Integer32
_JnxoptIfOMSnSrcCurrentLowerOutputPowerThreshold_Object = MibTableColumn
jnxoptIfOMSnSrcCurrentLowerOutputPowerThreshold = _JnxoptIfOMSnSrcCurrentLowerOutputPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 6, 1, 5),
    _JnxoptIfOMSnSrcCurrentLowerOutputPowerThreshold_Type()
)
jnxoptIfOMSnSrcCurrentLowerOutputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcCurrentLowerOutputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcCurrentLowerOutputPowerThreshold.setUnits("0.1 dbm")
_JnxoptIfOMSnSrcCurrentUpperOutputPowerThreshold_Type = Integer32
_JnxoptIfOMSnSrcCurrentUpperOutputPowerThreshold_Object = MibTableColumn
jnxoptIfOMSnSrcCurrentUpperOutputPowerThreshold = _JnxoptIfOMSnSrcCurrentUpperOutputPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 6, 1, 6),
    _JnxoptIfOMSnSrcCurrentUpperOutputPowerThreshold_Type()
)
jnxoptIfOMSnSrcCurrentUpperOutputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcCurrentUpperOutputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcCurrentUpperOutputPowerThreshold.setUnits("0.1 dbm")
_JnxoptIfOMSnSrcCurrentAggregatedInputPower_Type = Integer32
_JnxoptIfOMSnSrcCurrentAggregatedInputPower_Object = MibTableColumn
jnxoptIfOMSnSrcCurrentAggregatedInputPower = _JnxoptIfOMSnSrcCurrentAggregatedInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 6, 1, 7),
    _JnxoptIfOMSnSrcCurrentAggregatedInputPower_Type()
)
jnxoptIfOMSnSrcCurrentAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcCurrentAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcCurrentAggregatedInputPower.setUnits("0.1 dbm")
_JnxoptIfOMSnSrcCurrentLowAggregatedInputPower_Type = Integer32
_JnxoptIfOMSnSrcCurrentLowAggregatedInputPower_Object = MibTableColumn
jnxoptIfOMSnSrcCurrentLowAggregatedInputPower = _JnxoptIfOMSnSrcCurrentLowAggregatedInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 6, 1, 8),
    _JnxoptIfOMSnSrcCurrentLowAggregatedInputPower_Type()
)
jnxoptIfOMSnSrcCurrentLowAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcCurrentLowAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcCurrentLowAggregatedInputPower.setUnits("0.1 dbm")
_JnxoptIfOMSnSrcCurrentHighAggregatedInputPower_Type = Integer32
_JnxoptIfOMSnSrcCurrentHighAggregatedInputPower_Object = MibTableColumn
jnxoptIfOMSnSrcCurrentHighAggregatedInputPower = _JnxoptIfOMSnSrcCurrentHighAggregatedInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 6, 1, 9),
    _JnxoptIfOMSnSrcCurrentHighAggregatedInputPower_Type()
)
jnxoptIfOMSnSrcCurrentHighAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcCurrentHighAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcCurrentHighAggregatedInputPower.setUnits("0.1 dbm")
_JnxoptIfOMSnSrcCurrentLowerInputPowerThreshold_Type = Integer32
_JnxoptIfOMSnSrcCurrentLowerInputPowerThreshold_Object = MibTableColumn
jnxoptIfOMSnSrcCurrentLowerInputPowerThreshold = _JnxoptIfOMSnSrcCurrentLowerInputPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 6, 1, 10),
    _JnxoptIfOMSnSrcCurrentLowerInputPowerThreshold_Type()
)
jnxoptIfOMSnSrcCurrentLowerInputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcCurrentLowerInputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcCurrentLowerInputPowerThreshold.setUnits("0.1 dbm")
_JnxoptIfOMSnSrcCurrentUpperInputPowerThreshold_Type = Integer32
_JnxoptIfOMSnSrcCurrentUpperInputPowerThreshold_Object = MibTableColumn
jnxoptIfOMSnSrcCurrentUpperInputPowerThreshold = _JnxoptIfOMSnSrcCurrentUpperInputPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 6, 1, 11),
    _JnxoptIfOMSnSrcCurrentUpperInputPowerThreshold_Type()
)
jnxoptIfOMSnSrcCurrentUpperInputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcCurrentUpperInputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcCurrentUpperInputPowerThreshold.setUnits("0.1 dbm")
_JnxoptIfOMSnSrcIntervalTable_Object = MibTable
jnxoptIfOMSnSrcIntervalTable = _JnxoptIfOMSnSrcIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 7)
)
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcIntervalTable.setStatus("current")
_JnxoptIfOMSnSrcIntervalEntry_Object = MibTableRow
jnxoptIfOMSnSrcIntervalEntry = _JnxoptIfOMSnSrcIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 7, 1)
)
jnxoptIfOMSnSrcIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "JNX-OPT-IF-MIB", "jnxoptIfOMSnSrcIntervalNumber"),
)
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcIntervalEntry.setStatus("current")
_JnxoptIfOMSnSrcIntervalNumber_Type = JnxoptIfIntervalNumber
_JnxoptIfOMSnSrcIntervalNumber_Object = MibTableColumn
jnxoptIfOMSnSrcIntervalNumber = _JnxoptIfOMSnSrcIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 7, 1, 1),
    _JnxoptIfOMSnSrcIntervalNumber_Type()
)
jnxoptIfOMSnSrcIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcIntervalNumber.setStatus("current")
_JnxoptIfOMSnSrcIntervalSuspectedFlag_Type = TruthValue
_JnxoptIfOMSnSrcIntervalSuspectedFlag_Object = MibTableColumn
jnxoptIfOMSnSrcIntervalSuspectedFlag = _JnxoptIfOMSnSrcIntervalSuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 7, 1, 2),
    _JnxoptIfOMSnSrcIntervalSuspectedFlag_Type()
)
jnxoptIfOMSnSrcIntervalSuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcIntervalSuspectedFlag.setStatus("current")
_JnxoptIfOMSnSrcIntervalLastOutputPower_Type = Integer32
_JnxoptIfOMSnSrcIntervalLastOutputPower_Object = MibTableColumn
jnxoptIfOMSnSrcIntervalLastOutputPower = _JnxoptIfOMSnSrcIntervalLastOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 7, 1, 3),
    _JnxoptIfOMSnSrcIntervalLastOutputPower_Type()
)
jnxoptIfOMSnSrcIntervalLastOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcIntervalLastOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcIntervalLastOutputPower.setUnits("0.1 dbm")
_JnxoptIfOMSnSrcIntervalLowOutputPower_Type = Integer32
_JnxoptIfOMSnSrcIntervalLowOutputPower_Object = MibTableColumn
jnxoptIfOMSnSrcIntervalLowOutputPower = _JnxoptIfOMSnSrcIntervalLowOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 7, 1, 4),
    _JnxoptIfOMSnSrcIntervalLowOutputPower_Type()
)
jnxoptIfOMSnSrcIntervalLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcIntervalLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcIntervalLowOutputPower.setUnits("0.1 dbm")
_JnxoptIfOMSnSrcIntervalHighOutputPower_Type = Integer32
_JnxoptIfOMSnSrcIntervalHighOutputPower_Object = MibTableColumn
jnxoptIfOMSnSrcIntervalHighOutputPower = _JnxoptIfOMSnSrcIntervalHighOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 7, 1, 5),
    _JnxoptIfOMSnSrcIntervalHighOutputPower_Type()
)
jnxoptIfOMSnSrcIntervalHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcIntervalHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcIntervalHighOutputPower.setUnits("0.1 dbm")
_JnxoptIfOMSnSrcIntervalLastAggregatedInputPower_Type = Integer32
_JnxoptIfOMSnSrcIntervalLastAggregatedInputPower_Object = MibTableColumn
jnxoptIfOMSnSrcIntervalLastAggregatedInputPower = _JnxoptIfOMSnSrcIntervalLastAggregatedInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 7, 1, 6),
    _JnxoptIfOMSnSrcIntervalLastAggregatedInputPower_Type()
)
jnxoptIfOMSnSrcIntervalLastAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcIntervalLastAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcIntervalLastAggregatedInputPower.setUnits("0.1 dbm")
_JnxoptIfOMSnSrcIntervalLowAggregatedInputPower_Type = Integer32
_JnxoptIfOMSnSrcIntervalLowAggregatedInputPower_Object = MibTableColumn
jnxoptIfOMSnSrcIntervalLowAggregatedInputPower = _JnxoptIfOMSnSrcIntervalLowAggregatedInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 7, 1, 7),
    _JnxoptIfOMSnSrcIntervalLowAggregatedInputPower_Type()
)
jnxoptIfOMSnSrcIntervalLowAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcIntervalLowAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcIntervalLowAggregatedInputPower.setUnits("0.1 dbm")
_JnxoptIfOMSnSrcIntervalHighAggregatedInputPower_Type = Integer32
_JnxoptIfOMSnSrcIntervalHighAggregatedInputPower_Object = MibTableColumn
jnxoptIfOMSnSrcIntervalHighAggregatedInputPower = _JnxoptIfOMSnSrcIntervalHighAggregatedInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 7, 1, 8),
    _JnxoptIfOMSnSrcIntervalHighAggregatedInputPower_Type()
)
jnxoptIfOMSnSrcIntervalHighAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcIntervalHighAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcIntervalHighAggregatedInputPower.setUnits("0.1 dbm")
_JnxoptIfOMSnSrcCurDayTable_Object = MibTable
jnxoptIfOMSnSrcCurDayTable = _JnxoptIfOMSnSrcCurDayTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 8)
)
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcCurDayTable.setStatus("current")
_JnxoptIfOMSnSrcCurDayEntry_Object = MibTableRow
jnxoptIfOMSnSrcCurDayEntry = _JnxoptIfOMSnSrcCurDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 8, 1)
)
jnxoptIfOMSnSrcCurDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcCurDayEntry.setStatus("current")
_JnxoptIfOMSnSrcCurDaySuspectedFlag_Type = TruthValue
_JnxoptIfOMSnSrcCurDaySuspectedFlag_Object = MibTableColumn
jnxoptIfOMSnSrcCurDaySuspectedFlag = _JnxoptIfOMSnSrcCurDaySuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 8, 1, 1),
    _JnxoptIfOMSnSrcCurDaySuspectedFlag_Type()
)
jnxoptIfOMSnSrcCurDaySuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcCurDaySuspectedFlag.setStatus("current")
_JnxoptIfOMSnSrcCurDayLowOutputPower_Type = Integer32
_JnxoptIfOMSnSrcCurDayLowOutputPower_Object = MibTableColumn
jnxoptIfOMSnSrcCurDayLowOutputPower = _JnxoptIfOMSnSrcCurDayLowOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 8, 1, 2),
    _JnxoptIfOMSnSrcCurDayLowOutputPower_Type()
)
jnxoptIfOMSnSrcCurDayLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcCurDayLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcCurDayLowOutputPower.setUnits("0.1 dbm")
_JnxoptIfOMSnSrcCurDayHighOutputPower_Type = Integer32
_JnxoptIfOMSnSrcCurDayHighOutputPower_Object = MibTableColumn
jnxoptIfOMSnSrcCurDayHighOutputPower = _JnxoptIfOMSnSrcCurDayHighOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 8, 1, 3),
    _JnxoptIfOMSnSrcCurDayHighOutputPower_Type()
)
jnxoptIfOMSnSrcCurDayHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcCurDayHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcCurDayHighOutputPower.setUnits("0.1 dbm")
_JnxoptIfOMSnSrcCurDayLowAggregatedInputPower_Type = Integer32
_JnxoptIfOMSnSrcCurDayLowAggregatedInputPower_Object = MibTableColumn
jnxoptIfOMSnSrcCurDayLowAggregatedInputPower = _JnxoptIfOMSnSrcCurDayLowAggregatedInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 8, 1, 4),
    _JnxoptIfOMSnSrcCurDayLowAggregatedInputPower_Type()
)
jnxoptIfOMSnSrcCurDayLowAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcCurDayLowAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcCurDayLowAggregatedInputPower.setUnits("0.1 dbm")
_JnxoptIfOMSnSrcCurDayHighAggregatedInputPower_Type = Integer32
_JnxoptIfOMSnSrcCurDayHighAggregatedInputPower_Object = MibTableColumn
jnxoptIfOMSnSrcCurDayHighAggregatedInputPower = _JnxoptIfOMSnSrcCurDayHighAggregatedInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 8, 1, 5),
    _JnxoptIfOMSnSrcCurDayHighAggregatedInputPower_Type()
)
jnxoptIfOMSnSrcCurDayHighAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcCurDayHighAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcCurDayHighAggregatedInputPower.setUnits("0.1 dbm")
_JnxoptIfOMSnSrcPrevDayTable_Object = MibTable
jnxoptIfOMSnSrcPrevDayTable = _JnxoptIfOMSnSrcPrevDayTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 9)
)
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcPrevDayTable.setStatus("current")
_JnxoptIfOMSnSrcPrevDayEntry_Object = MibTableRow
jnxoptIfOMSnSrcPrevDayEntry = _JnxoptIfOMSnSrcPrevDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 9, 1)
)
jnxoptIfOMSnSrcPrevDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcPrevDayEntry.setStatus("current")
_JnxoptIfOMSnSrcPrevDaySuspectedFlag_Type = TruthValue
_JnxoptIfOMSnSrcPrevDaySuspectedFlag_Object = MibTableColumn
jnxoptIfOMSnSrcPrevDaySuspectedFlag = _JnxoptIfOMSnSrcPrevDaySuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 9, 1, 1),
    _JnxoptIfOMSnSrcPrevDaySuspectedFlag_Type()
)
jnxoptIfOMSnSrcPrevDaySuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcPrevDaySuspectedFlag.setStatus("current")
_JnxoptIfOMSnSrcPrevDayLastOutputPower_Type = Integer32
_JnxoptIfOMSnSrcPrevDayLastOutputPower_Object = MibTableColumn
jnxoptIfOMSnSrcPrevDayLastOutputPower = _JnxoptIfOMSnSrcPrevDayLastOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 9, 1, 2),
    _JnxoptIfOMSnSrcPrevDayLastOutputPower_Type()
)
jnxoptIfOMSnSrcPrevDayLastOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcPrevDayLastOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcPrevDayLastOutputPower.setUnits("0.1 dbm")
_JnxoptIfOMSnSrcPrevDayLowOutputPower_Type = Integer32
_JnxoptIfOMSnSrcPrevDayLowOutputPower_Object = MibTableColumn
jnxoptIfOMSnSrcPrevDayLowOutputPower = _JnxoptIfOMSnSrcPrevDayLowOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 9, 1, 3),
    _JnxoptIfOMSnSrcPrevDayLowOutputPower_Type()
)
jnxoptIfOMSnSrcPrevDayLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcPrevDayLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcPrevDayLowOutputPower.setUnits("0.1 dbm")
_JnxoptIfOMSnSrcPrevDayHighOutputPower_Type = Integer32
_JnxoptIfOMSnSrcPrevDayHighOutputPower_Object = MibTableColumn
jnxoptIfOMSnSrcPrevDayHighOutputPower = _JnxoptIfOMSnSrcPrevDayHighOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 9, 1, 4),
    _JnxoptIfOMSnSrcPrevDayHighOutputPower_Type()
)
jnxoptIfOMSnSrcPrevDayHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcPrevDayHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcPrevDayHighOutputPower.setUnits("0.1 dbm")
_JnxoptIfOMSnSrcPrevDayLastAggregatedInputPower_Type = Integer32
_JnxoptIfOMSnSrcPrevDayLastAggregatedInputPower_Object = MibTableColumn
jnxoptIfOMSnSrcPrevDayLastAggregatedInputPower = _JnxoptIfOMSnSrcPrevDayLastAggregatedInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 9, 1, 5),
    _JnxoptIfOMSnSrcPrevDayLastAggregatedInputPower_Type()
)
jnxoptIfOMSnSrcPrevDayLastAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcPrevDayLastAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcPrevDayLastAggregatedInputPower.setUnits("0.1 dbm")
_JnxoptIfOMSnSrcPrevDayLowAggregatedInputPower_Type = Integer32
_JnxoptIfOMSnSrcPrevDayLowAggregatedInputPower_Object = MibTableColumn
jnxoptIfOMSnSrcPrevDayLowAggregatedInputPower = _JnxoptIfOMSnSrcPrevDayLowAggregatedInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 9, 1, 6),
    _JnxoptIfOMSnSrcPrevDayLowAggregatedInputPower_Type()
)
jnxoptIfOMSnSrcPrevDayLowAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcPrevDayLowAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcPrevDayLowAggregatedInputPower.setUnits("0.1 dbm")
_JnxoptIfOMSnSrcPrevDayHighAggregatedInputPower_Type = Integer32
_JnxoptIfOMSnSrcPrevDayHighAggregatedInputPower_Object = MibTableColumn
jnxoptIfOMSnSrcPrevDayHighAggregatedInputPower = _JnxoptIfOMSnSrcPrevDayHighAggregatedInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 4, 9, 1, 7),
    _JnxoptIfOMSnSrcPrevDayHighAggregatedInputPower_Type()
)
jnxoptIfOMSnSrcPrevDayHighAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcPrevDayHighAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOMSnSrcPrevDayHighAggregatedInputPower.setUnits("0.1 dbm")
_JnxoptIfOChGroup_ObjectIdentity = ObjectIdentity
jnxoptIfOChGroup = _JnxoptIfOChGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5)
)
_JnxoptIfOChGroupConfigTable_Object = MibTable
jnxoptIfOChGroupConfigTable = _JnxoptIfOChGroupConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    jnxoptIfOChGroupConfigTable.setStatus("current")
_JnxoptIfOChGroupConfigEntry_Object = MibTableRow
jnxoptIfOChGroupConfigEntry = _JnxoptIfOChGroupConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 1, 1)
)
jnxoptIfOChGroupConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxoptIfOChGroupConfigEntry.setStatus("current")
_JnxoptIfOChGroupDirectionality_Type = JnxoptIfDirectionality
_JnxoptIfOChGroupDirectionality_Object = MibTableColumn
jnxoptIfOChGroupDirectionality = _JnxoptIfOChGroupDirectionality_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 1, 1, 1),
    _JnxoptIfOChGroupDirectionality_Type()
)
jnxoptIfOChGroupDirectionality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupDirectionality.setStatus("current")
_JnxoptIfOChGroupSinkCurrentTable_Object = MibTable
jnxoptIfOChGroupSinkCurrentTable = _JnxoptIfOChGroupSinkCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkCurrentTable.setStatus("current")
_JnxoptIfOChGroupSinkCurrentEntry_Object = MibTableRow
jnxoptIfOChGroupSinkCurrentEntry = _JnxoptIfOChGroupSinkCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 2, 1)
)
jnxoptIfOChGroupSinkCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkCurrentEntry.setStatus("current")
_JnxoptIfOChGroupSinkCurrentSuspectedFlag_Type = TruthValue
_JnxoptIfOChGroupSinkCurrentSuspectedFlag_Object = MibTableColumn
jnxoptIfOChGroupSinkCurrentSuspectedFlag = _JnxoptIfOChGroupSinkCurrentSuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 2, 1, 1),
    _JnxoptIfOChGroupSinkCurrentSuspectedFlag_Type()
)
jnxoptIfOChGroupSinkCurrentSuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkCurrentSuspectedFlag.setStatus("current")
_JnxoptIfOChGroupSinkCurrentAggregatedInputPower_Type = Integer32
_JnxoptIfOChGroupSinkCurrentAggregatedInputPower_Object = MibTableColumn
jnxoptIfOChGroupSinkCurrentAggregatedInputPower = _JnxoptIfOChGroupSinkCurrentAggregatedInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 2, 1, 2),
    _JnxoptIfOChGroupSinkCurrentAggregatedInputPower_Type()
)
jnxoptIfOChGroupSinkCurrentAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkCurrentAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkCurrentAggregatedInputPower.setUnits("0.1 dbm")
_JnxoptIfOChGroupSinkCurrentLowAggregatedInputPower_Type = Integer32
_JnxoptIfOChGroupSinkCurrentLowAggregatedInputPower_Object = MibTableColumn
jnxoptIfOChGroupSinkCurrentLowAggregatedInputPower = _JnxoptIfOChGroupSinkCurrentLowAggregatedInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 2, 1, 3),
    _JnxoptIfOChGroupSinkCurrentLowAggregatedInputPower_Type()
)
jnxoptIfOChGroupSinkCurrentLowAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkCurrentLowAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkCurrentLowAggregatedInputPower.setUnits("0.1 dbm")
_JnxoptIfOChGroupSinkCurrentHighAggregatedInputPower_Type = Integer32
_JnxoptIfOChGroupSinkCurrentHighAggregatedInputPower_Object = MibTableColumn
jnxoptIfOChGroupSinkCurrentHighAggregatedInputPower = _JnxoptIfOChGroupSinkCurrentHighAggregatedInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 2, 1, 4),
    _JnxoptIfOChGroupSinkCurrentHighAggregatedInputPower_Type()
)
jnxoptIfOChGroupSinkCurrentHighAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkCurrentHighAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkCurrentHighAggregatedInputPower.setUnits("0.1 dbm")
_JnxoptIfOChGroupSinkCurrentLowerInputPowerThreshold_Type = Integer32
_JnxoptIfOChGroupSinkCurrentLowerInputPowerThreshold_Object = MibTableColumn
jnxoptIfOChGroupSinkCurrentLowerInputPowerThreshold = _JnxoptIfOChGroupSinkCurrentLowerInputPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 2, 1, 5),
    _JnxoptIfOChGroupSinkCurrentLowerInputPowerThreshold_Type()
)
jnxoptIfOChGroupSinkCurrentLowerInputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkCurrentLowerInputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkCurrentLowerInputPowerThreshold.setUnits("0.1 dbm")
_JnxoptIfOChGroupSinkCurrentUpperInputPowerThreshold_Type = Integer32
_JnxoptIfOChGroupSinkCurrentUpperInputPowerThreshold_Object = MibTableColumn
jnxoptIfOChGroupSinkCurrentUpperInputPowerThreshold = _JnxoptIfOChGroupSinkCurrentUpperInputPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 2, 1, 6),
    _JnxoptIfOChGroupSinkCurrentUpperInputPowerThreshold_Type()
)
jnxoptIfOChGroupSinkCurrentUpperInputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkCurrentUpperInputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkCurrentUpperInputPowerThreshold.setUnits("0.1 dbm")
_JnxoptIfOChGroupSinkCurrentOutputPower_Type = Integer32
_JnxoptIfOChGroupSinkCurrentOutputPower_Object = MibTableColumn
jnxoptIfOChGroupSinkCurrentOutputPower = _JnxoptIfOChGroupSinkCurrentOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 2, 1, 7),
    _JnxoptIfOChGroupSinkCurrentOutputPower_Type()
)
jnxoptIfOChGroupSinkCurrentOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkCurrentOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkCurrentOutputPower.setUnits("0.1 dbm")
_JnxoptIfOChGroupSinkCurrentLowOutputPower_Type = Integer32
_JnxoptIfOChGroupSinkCurrentLowOutputPower_Object = MibTableColumn
jnxoptIfOChGroupSinkCurrentLowOutputPower = _JnxoptIfOChGroupSinkCurrentLowOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 2, 1, 8),
    _JnxoptIfOChGroupSinkCurrentLowOutputPower_Type()
)
jnxoptIfOChGroupSinkCurrentLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkCurrentLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkCurrentLowOutputPower.setUnits("0.1 dbm")
_JnxoptIfOChGroupSinkCurrentHighOutputPower_Type = Integer32
_JnxoptIfOChGroupSinkCurrentHighOutputPower_Object = MibTableColumn
jnxoptIfOChGroupSinkCurrentHighOutputPower = _JnxoptIfOChGroupSinkCurrentHighOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 2, 1, 9),
    _JnxoptIfOChGroupSinkCurrentHighOutputPower_Type()
)
jnxoptIfOChGroupSinkCurrentHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkCurrentHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkCurrentHighOutputPower.setUnits("0.1 dbm")
_JnxoptIfOChGroupSinkCurrentLowerOutputPowerThreshold_Type = Integer32
_JnxoptIfOChGroupSinkCurrentLowerOutputPowerThreshold_Object = MibTableColumn
jnxoptIfOChGroupSinkCurrentLowerOutputPowerThreshold = _JnxoptIfOChGroupSinkCurrentLowerOutputPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 2, 1, 10),
    _JnxoptIfOChGroupSinkCurrentLowerOutputPowerThreshold_Type()
)
jnxoptIfOChGroupSinkCurrentLowerOutputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkCurrentLowerOutputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkCurrentLowerOutputPowerThreshold.setUnits("0.1 dbm")
_JnxoptIfOChGroupSinkCurrentUpperOutputPowerThreshold_Type = Integer32
_JnxoptIfOChGroupSinkCurrentUpperOutputPowerThreshold_Object = MibTableColumn
jnxoptIfOChGroupSinkCurrentUpperOutputPowerThreshold = _JnxoptIfOChGroupSinkCurrentUpperOutputPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 2, 1, 11),
    _JnxoptIfOChGroupSinkCurrentUpperOutputPowerThreshold_Type()
)
jnxoptIfOChGroupSinkCurrentUpperOutputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkCurrentUpperOutputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkCurrentUpperOutputPowerThreshold.setUnits("0.1 dbm")
_JnxoptIfOChGroupSinkIntervalTable_Object = MibTable
jnxoptIfOChGroupSinkIntervalTable = _JnxoptIfOChGroupSinkIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 3)
)
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkIntervalTable.setStatus("current")
_JnxoptIfOChGroupSinkIntervalEntry_Object = MibTableRow
jnxoptIfOChGroupSinkIntervalEntry = _JnxoptIfOChGroupSinkIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 3, 1)
)
jnxoptIfOChGroupSinkIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "JNX-OPT-IF-MIB", "jnxoptIfOChGroupSinkIntervalNumber"),
)
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkIntervalEntry.setStatus("current")
_JnxoptIfOChGroupSinkIntervalNumber_Type = JnxoptIfIntervalNumber
_JnxoptIfOChGroupSinkIntervalNumber_Object = MibTableColumn
jnxoptIfOChGroupSinkIntervalNumber = _JnxoptIfOChGroupSinkIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 3, 1, 1),
    _JnxoptIfOChGroupSinkIntervalNumber_Type()
)
jnxoptIfOChGroupSinkIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkIntervalNumber.setStatus("current")
_JnxoptIfOChGroupSinkIntervalSuspectedFlag_Type = TruthValue
_JnxoptIfOChGroupSinkIntervalSuspectedFlag_Object = MibTableColumn
jnxoptIfOChGroupSinkIntervalSuspectedFlag = _JnxoptIfOChGroupSinkIntervalSuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 3, 1, 2),
    _JnxoptIfOChGroupSinkIntervalSuspectedFlag_Type()
)
jnxoptIfOChGroupSinkIntervalSuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkIntervalSuspectedFlag.setStatus("current")
_JnxoptIfOChGroupSinkIntervalLastAggregatedInputPower_Type = Integer32
_JnxoptIfOChGroupSinkIntervalLastAggregatedInputPower_Object = MibTableColumn
jnxoptIfOChGroupSinkIntervalLastAggregatedInputPower = _JnxoptIfOChGroupSinkIntervalLastAggregatedInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 3, 1, 3),
    _JnxoptIfOChGroupSinkIntervalLastAggregatedInputPower_Type()
)
jnxoptIfOChGroupSinkIntervalLastAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkIntervalLastAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkIntervalLastAggregatedInputPower.setUnits("0.1 dbm")
_JnxoptIfOChGroupSinkIntervalLowAggregatedInputPower_Type = Integer32
_JnxoptIfOChGroupSinkIntervalLowAggregatedInputPower_Object = MibTableColumn
jnxoptIfOChGroupSinkIntervalLowAggregatedInputPower = _JnxoptIfOChGroupSinkIntervalLowAggregatedInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 3, 1, 4),
    _JnxoptIfOChGroupSinkIntervalLowAggregatedInputPower_Type()
)
jnxoptIfOChGroupSinkIntervalLowAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkIntervalLowAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkIntervalLowAggregatedInputPower.setUnits("0.1 dbm")
_JnxoptIfOChGroupSinkIntervalHighAggregatedInputPower_Type = Integer32
_JnxoptIfOChGroupSinkIntervalHighAggregatedInputPower_Object = MibTableColumn
jnxoptIfOChGroupSinkIntervalHighAggregatedInputPower = _JnxoptIfOChGroupSinkIntervalHighAggregatedInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 3, 1, 5),
    _JnxoptIfOChGroupSinkIntervalHighAggregatedInputPower_Type()
)
jnxoptIfOChGroupSinkIntervalHighAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkIntervalHighAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkIntervalHighAggregatedInputPower.setUnits("0.1 dbm")
_JnxoptIfOChGroupSinkIntervalLastOutputPower_Type = Integer32
_JnxoptIfOChGroupSinkIntervalLastOutputPower_Object = MibTableColumn
jnxoptIfOChGroupSinkIntervalLastOutputPower = _JnxoptIfOChGroupSinkIntervalLastOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 3, 1, 6),
    _JnxoptIfOChGroupSinkIntervalLastOutputPower_Type()
)
jnxoptIfOChGroupSinkIntervalLastOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkIntervalLastOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkIntervalLastOutputPower.setUnits("0.1 dbm")
_JnxoptIfOChGroupSinkIntervalLowOutputPower_Type = Integer32
_JnxoptIfOChGroupSinkIntervalLowOutputPower_Object = MibTableColumn
jnxoptIfOChGroupSinkIntervalLowOutputPower = _JnxoptIfOChGroupSinkIntervalLowOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 3, 1, 7),
    _JnxoptIfOChGroupSinkIntervalLowOutputPower_Type()
)
jnxoptIfOChGroupSinkIntervalLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkIntervalLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkIntervalLowOutputPower.setUnits("0.1 dbm")
_JnxoptIfOChGroupSinkIntervalHighOutputPower_Type = Integer32
_JnxoptIfOChGroupSinkIntervalHighOutputPower_Object = MibTableColumn
jnxoptIfOChGroupSinkIntervalHighOutputPower = _JnxoptIfOChGroupSinkIntervalHighOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 3, 1, 8),
    _JnxoptIfOChGroupSinkIntervalHighOutputPower_Type()
)
jnxoptIfOChGroupSinkIntervalHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkIntervalHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkIntervalHighOutputPower.setUnits("0.1 dbm")
_JnxoptIfOChGroupSinkCurDayTable_Object = MibTable
jnxoptIfOChGroupSinkCurDayTable = _JnxoptIfOChGroupSinkCurDayTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 4)
)
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkCurDayTable.setStatus("current")
_JnxoptIfOChGroupSinkCurDayEntry_Object = MibTableRow
jnxoptIfOChGroupSinkCurDayEntry = _JnxoptIfOChGroupSinkCurDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 4, 1)
)
jnxoptIfOChGroupSinkCurDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkCurDayEntry.setStatus("current")
_JnxoptIfOChGroupSinkCurDaySuspectedFlag_Type = TruthValue
_JnxoptIfOChGroupSinkCurDaySuspectedFlag_Object = MibTableColumn
jnxoptIfOChGroupSinkCurDaySuspectedFlag = _JnxoptIfOChGroupSinkCurDaySuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 4, 1, 1),
    _JnxoptIfOChGroupSinkCurDaySuspectedFlag_Type()
)
jnxoptIfOChGroupSinkCurDaySuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkCurDaySuspectedFlag.setStatus("current")
_JnxoptIfOChGroupSinkCurDayLowAggregatedInputPower_Type = Integer32
_JnxoptIfOChGroupSinkCurDayLowAggregatedInputPower_Object = MibTableColumn
jnxoptIfOChGroupSinkCurDayLowAggregatedInputPower = _JnxoptIfOChGroupSinkCurDayLowAggregatedInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 4, 1, 2),
    _JnxoptIfOChGroupSinkCurDayLowAggregatedInputPower_Type()
)
jnxoptIfOChGroupSinkCurDayLowAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkCurDayLowAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkCurDayLowAggregatedInputPower.setUnits("0.1 dbm")
_JnxoptIfOChGroupSinkCurDayHighAggregatedInputPower_Type = Integer32
_JnxoptIfOChGroupSinkCurDayHighAggregatedInputPower_Object = MibTableColumn
jnxoptIfOChGroupSinkCurDayHighAggregatedInputPower = _JnxoptIfOChGroupSinkCurDayHighAggregatedInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 4, 1, 3),
    _JnxoptIfOChGroupSinkCurDayHighAggregatedInputPower_Type()
)
jnxoptIfOChGroupSinkCurDayHighAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkCurDayHighAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkCurDayHighAggregatedInputPower.setUnits("0.1 dbm")
_JnxoptIfOChGroupSinkCurDayLowOutputPower_Type = Integer32
_JnxoptIfOChGroupSinkCurDayLowOutputPower_Object = MibTableColumn
jnxoptIfOChGroupSinkCurDayLowOutputPower = _JnxoptIfOChGroupSinkCurDayLowOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 4, 1, 4),
    _JnxoptIfOChGroupSinkCurDayLowOutputPower_Type()
)
jnxoptIfOChGroupSinkCurDayLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkCurDayLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkCurDayLowOutputPower.setUnits("0.1 dbm")
_JnxoptIfOChGroupSinkCurDayHighOutputPower_Type = Integer32
_JnxoptIfOChGroupSinkCurDayHighOutputPower_Object = MibTableColumn
jnxoptIfOChGroupSinkCurDayHighOutputPower = _JnxoptIfOChGroupSinkCurDayHighOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 4, 1, 5),
    _JnxoptIfOChGroupSinkCurDayHighOutputPower_Type()
)
jnxoptIfOChGroupSinkCurDayHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkCurDayHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkCurDayHighOutputPower.setUnits("0.1 dbm")
_JnxoptIfOChGroupSinkPrevDayTable_Object = MibTable
jnxoptIfOChGroupSinkPrevDayTable = _JnxoptIfOChGroupSinkPrevDayTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 5)
)
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkPrevDayTable.setStatus("current")
_JnxoptIfOChGroupSinkPrevDayEntry_Object = MibTableRow
jnxoptIfOChGroupSinkPrevDayEntry = _JnxoptIfOChGroupSinkPrevDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 5, 1)
)
jnxoptIfOChGroupSinkPrevDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkPrevDayEntry.setStatus("current")
_JnxoptIfOChGroupSinkPrevDaySuspectedFlag_Type = TruthValue
_JnxoptIfOChGroupSinkPrevDaySuspectedFlag_Object = MibTableColumn
jnxoptIfOChGroupSinkPrevDaySuspectedFlag = _JnxoptIfOChGroupSinkPrevDaySuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 5, 1, 1),
    _JnxoptIfOChGroupSinkPrevDaySuspectedFlag_Type()
)
jnxoptIfOChGroupSinkPrevDaySuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkPrevDaySuspectedFlag.setStatus("current")
_JnxoptIfOChGroupSinkPrevDayLastAggregatedInputPower_Type = Integer32
_JnxoptIfOChGroupSinkPrevDayLastAggregatedInputPower_Object = MibTableColumn
jnxoptIfOChGroupSinkPrevDayLastAggregatedInputPower = _JnxoptIfOChGroupSinkPrevDayLastAggregatedInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 5, 1, 2),
    _JnxoptIfOChGroupSinkPrevDayLastAggregatedInputPower_Type()
)
jnxoptIfOChGroupSinkPrevDayLastAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkPrevDayLastAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkPrevDayLastAggregatedInputPower.setUnits("0.1 dbm")
_JnxoptIfOChGroupSinkPrevDayLowAggregatedInputPower_Type = Integer32
_JnxoptIfOChGroupSinkPrevDayLowAggregatedInputPower_Object = MibTableColumn
jnxoptIfOChGroupSinkPrevDayLowAggregatedInputPower = _JnxoptIfOChGroupSinkPrevDayLowAggregatedInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 5, 1, 3),
    _JnxoptIfOChGroupSinkPrevDayLowAggregatedInputPower_Type()
)
jnxoptIfOChGroupSinkPrevDayLowAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkPrevDayLowAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkPrevDayLowAggregatedInputPower.setUnits("0.1 dbm")
_JnxoptIfOChGroupSinkPrevDayHighAggregatedInputPower_Type = Integer32
_JnxoptIfOChGroupSinkPrevDayHighAggregatedInputPower_Object = MibTableColumn
jnxoptIfOChGroupSinkPrevDayHighAggregatedInputPower = _JnxoptIfOChGroupSinkPrevDayHighAggregatedInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 5, 1, 4),
    _JnxoptIfOChGroupSinkPrevDayHighAggregatedInputPower_Type()
)
jnxoptIfOChGroupSinkPrevDayHighAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkPrevDayHighAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkPrevDayHighAggregatedInputPower.setUnits("0.1 dbm")
_JnxoptIfOChGroupSinkPrevDayLastOutputPower_Type = Integer32
_JnxoptIfOChGroupSinkPrevDayLastOutputPower_Object = MibTableColumn
jnxoptIfOChGroupSinkPrevDayLastOutputPower = _JnxoptIfOChGroupSinkPrevDayLastOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 5, 1, 5),
    _JnxoptIfOChGroupSinkPrevDayLastOutputPower_Type()
)
jnxoptIfOChGroupSinkPrevDayLastOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkPrevDayLastOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkPrevDayLastOutputPower.setUnits("0.1 dbm")
_JnxoptIfOChGroupSinkPrevDayLowOutputPower_Type = Integer32
_JnxoptIfOChGroupSinkPrevDayLowOutputPower_Object = MibTableColumn
jnxoptIfOChGroupSinkPrevDayLowOutputPower = _JnxoptIfOChGroupSinkPrevDayLowOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 5, 1, 6),
    _JnxoptIfOChGroupSinkPrevDayLowOutputPower_Type()
)
jnxoptIfOChGroupSinkPrevDayLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkPrevDayLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkPrevDayLowOutputPower.setUnits("0.1 dbm")
_JnxoptIfOChGroupSinkPrevDayHighOutputPower_Type = Integer32
_JnxoptIfOChGroupSinkPrevDayHighOutputPower_Object = MibTableColumn
jnxoptIfOChGroupSinkPrevDayHighOutputPower = _JnxoptIfOChGroupSinkPrevDayHighOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 5, 1, 7),
    _JnxoptIfOChGroupSinkPrevDayHighOutputPower_Type()
)
jnxoptIfOChGroupSinkPrevDayHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkPrevDayHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkPrevDayHighOutputPower.setUnits("0.1 dbm")
_JnxoptIfOChGroupSrcCurrentTable_Object = MibTable
jnxoptIfOChGroupSrcCurrentTable = _JnxoptIfOChGroupSrcCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 6)
)
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcCurrentTable.setStatus("current")
_JnxoptIfOChGroupSrcCurrentEntry_Object = MibTableRow
jnxoptIfOChGroupSrcCurrentEntry = _JnxoptIfOChGroupSrcCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 6, 1)
)
jnxoptIfOChGroupSrcCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcCurrentEntry.setStatus("current")
_JnxoptIfOChGroupSrcCurrentSuspectedFlag_Type = TruthValue
_JnxoptIfOChGroupSrcCurrentSuspectedFlag_Object = MibTableColumn
jnxoptIfOChGroupSrcCurrentSuspectedFlag = _JnxoptIfOChGroupSrcCurrentSuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 6, 1, 1),
    _JnxoptIfOChGroupSrcCurrentSuspectedFlag_Type()
)
jnxoptIfOChGroupSrcCurrentSuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcCurrentSuspectedFlag.setStatus("current")
_JnxoptIfOChGroupSrcCurrentOutputPower_Type = Integer32
_JnxoptIfOChGroupSrcCurrentOutputPower_Object = MibTableColumn
jnxoptIfOChGroupSrcCurrentOutputPower = _JnxoptIfOChGroupSrcCurrentOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 6, 1, 2),
    _JnxoptIfOChGroupSrcCurrentOutputPower_Type()
)
jnxoptIfOChGroupSrcCurrentOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcCurrentOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcCurrentOutputPower.setUnits("0.1 dbm")
_JnxoptIfOChGroupSrcCurrentLowOutputPower_Type = Integer32
_JnxoptIfOChGroupSrcCurrentLowOutputPower_Object = MibTableColumn
jnxoptIfOChGroupSrcCurrentLowOutputPower = _JnxoptIfOChGroupSrcCurrentLowOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 6, 1, 3),
    _JnxoptIfOChGroupSrcCurrentLowOutputPower_Type()
)
jnxoptIfOChGroupSrcCurrentLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcCurrentLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcCurrentLowOutputPower.setUnits("0.1 dbm")
_JnxoptIfOChGroupSrcCurrentHighOutputPower_Type = Integer32
_JnxoptIfOChGroupSrcCurrentHighOutputPower_Object = MibTableColumn
jnxoptIfOChGroupSrcCurrentHighOutputPower = _JnxoptIfOChGroupSrcCurrentHighOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 6, 1, 4),
    _JnxoptIfOChGroupSrcCurrentHighOutputPower_Type()
)
jnxoptIfOChGroupSrcCurrentHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcCurrentHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcCurrentHighOutputPower.setUnits("0.1 dbm")
_JnxoptIfOChGroupSrcCurrentLowerOutputPowerThreshold_Type = Integer32
_JnxoptIfOChGroupSrcCurrentLowerOutputPowerThreshold_Object = MibTableColumn
jnxoptIfOChGroupSrcCurrentLowerOutputPowerThreshold = _JnxoptIfOChGroupSrcCurrentLowerOutputPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 6, 1, 5),
    _JnxoptIfOChGroupSrcCurrentLowerOutputPowerThreshold_Type()
)
jnxoptIfOChGroupSrcCurrentLowerOutputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcCurrentLowerOutputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcCurrentLowerOutputPowerThreshold.setUnits("0.1 dbm")
_JnxoptIfOChGroupSrcCurrentUpperOutputPowerThreshold_Type = Integer32
_JnxoptIfOChGroupSrcCurrentUpperOutputPowerThreshold_Object = MibTableColumn
jnxoptIfOChGroupSrcCurrentUpperOutputPowerThreshold = _JnxoptIfOChGroupSrcCurrentUpperOutputPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 6, 1, 6),
    _JnxoptIfOChGroupSrcCurrentUpperOutputPowerThreshold_Type()
)
jnxoptIfOChGroupSrcCurrentUpperOutputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcCurrentUpperOutputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcCurrentUpperOutputPowerThreshold.setUnits("0.1 dbm")
_JnxoptIfOChGroupSrcCurrentAggregatedInputPower_Type = Integer32
_JnxoptIfOChGroupSrcCurrentAggregatedInputPower_Object = MibTableColumn
jnxoptIfOChGroupSrcCurrentAggregatedInputPower = _JnxoptIfOChGroupSrcCurrentAggregatedInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 6, 1, 7),
    _JnxoptIfOChGroupSrcCurrentAggregatedInputPower_Type()
)
jnxoptIfOChGroupSrcCurrentAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcCurrentAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcCurrentAggregatedInputPower.setUnits("0.1 dbm")
_JnxoptIfOChGroupSrcCurrentLowAggregatedInputPower_Type = Integer32
_JnxoptIfOChGroupSrcCurrentLowAggregatedInputPower_Object = MibTableColumn
jnxoptIfOChGroupSrcCurrentLowAggregatedInputPower = _JnxoptIfOChGroupSrcCurrentLowAggregatedInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 6, 1, 8),
    _JnxoptIfOChGroupSrcCurrentLowAggregatedInputPower_Type()
)
jnxoptIfOChGroupSrcCurrentLowAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcCurrentLowAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcCurrentLowAggregatedInputPower.setUnits("0.1 dbm")
_JnxoptIfOChGroupSrcCurrentHighAggregatedInputPower_Type = Integer32
_JnxoptIfOChGroupSrcCurrentHighAggregatedInputPower_Object = MibTableColumn
jnxoptIfOChGroupSrcCurrentHighAggregatedInputPower = _JnxoptIfOChGroupSrcCurrentHighAggregatedInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 6, 1, 9),
    _JnxoptIfOChGroupSrcCurrentHighAggregatedInputPower_Type()
)
jnxoptIfOChGroupSrcCurrentHighAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcCurrentHighAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcCurrentHighAggregatedInputPower.setUnits("0.1 dbm")
_JnxoptIfOChGroupSrcCurrentLowerInputPowerThreshold_Type = Integer32
_JnxoptIfOChGroupSrcCurrentLowerInputPowerThreshold_Object = MibTableColumn
jnxoptIfOChGroupSrcCurrentLowerInputPowerThreshold = _JnxoptIfOChGroupSrcCurrentLowerInputPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 6, 1, 10),
    _JnxoptIfOChGroupSrcCurrentLowerInputPowerThreshold_Type()
)
jnxoptIfOChGroupSrcCurrentLowerInputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcCurrentLowerInputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcCurrentLowerInputPowerThreshold.setUnits("0.1 dbm")
_JnxoptIfOChGroupSrcCurrentUpperInputPowerThreshold_Type = Integer32
_JnxoptIfOChGroupSrcCurrentUpperInputPowerThreshold_Object = MibTableColumn
jnxoptIfOChGroupSrcCurrentUpperInputPowerThreshold = _JnxoptIfOChGroupSrcCurrentUpperInputPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 6, 1, 11),
    _JnxoptIfOChGroupSrcCurrentUpperInputPowerThreshold_Type()
)
jnxoptIfOChGroupSrcCurrentUpperInputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcCurrentUpperInputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcCurrentUpperInputPowerThreshold.setUnits("0.1 dbm")
_JnxoptIfOChGroupSrcIntervalTable_Object = MibTable
jnxoptIfOChGroupSrcIntervalTable = _JnxoptIfOChGroupSrcIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 7)
)
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcIntervalTable.setStatus("current")
_JnxoptIfOChGroupSrcIntervalEntry_Object = MibTableRow
jnxoptIfOChGroupSrcIntervalEntry = _JnxoptIfOChGroupSrcIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 7, 1)
)
jnxoptIfOChGroupSrcIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "JNX-OPT-IF-MIB", "jnxoptIfOChGroupSrcIntervalNumber"),
)
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcIntervalEntry.setStatus("current")
_JnxoptIfOChGroupSrcIntervalNumber_Type = JnxoptIfIntervalNumber
_JnxoptIfOChGroupSrcIntervalNumber_Object = MibTableColumn
jnxoptIfOChGroupSrcIntervalNumber = _JnxoptIfOChGroupSrcIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 7, 1, 1),
    _JnxoptIfOChGroupSrcIntervalNumber_Type()
)
jnxoptIfOChGroupSrcIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcIntervalNumber.setStatus("current")
_JnxoptIfOChGroupSrcIntervalSuspectedFlag_Type = TruthValue
_JnxoptIfOChGroupSrcIntervalSuspectedFlag_Object = MibTableColumn
jnxoptIfOChGroupSrcIntervalSuspectedFlag = _JnxoptIfOChGroupSrcIntervalSuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 7, 1, 2),
    _JnxoptIfOChGroupSrcIntervalSuspectedFlag_Type()
)
jnxoptIfOChGroupSrcIntervalSuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcIntervalSuspectedFlag.setStatus("current")
_JnxoptIfOChGroupSrcIntervalLastOutputPower_Type = Integer32
_JnxoptIfOChGroupSrcIntervalLastOutputPower_Object = MibTableColumn
jnxoptIfOChGroupSrcIntervalLastOutputPower = _JnxoptIfOChGroupSrcIntervalLastOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 7, 1, 3),
    _JnxoptIfOChGroupSrcIntervalLastOutputPower_Type()
)
jnxoptIfOChGroupSrcIntervalLastOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcIntervalLastOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcIntervalLastOutputPower.setUnits("0.1 dbm")
_JnxoptIfOChGroupSrcIntervalLowOutputPower_Type = Integer32
_JnxoptIfOChGroupSrcIntervalLowOutputPower_Object = MibTableColumn
jnxoptIfOChGroupSrcIntervalLowOutputPower = _JnxoptIfOChGroupSrcIntervalLowOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 7, 1, 4),
    _JnxoptIfOChGroupSrcIntervalLowOutputPower_Type()
)
jnxoptIfOChGroupSrcIntervalLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcIntervalLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcIntervalLowOutputPower.setUnits("0.1 dbm")
_JnxoptIfOChGroupSrcIntervalHighOutputPower_Type = Integer32
_JnxoptIfOChGroupSrcIntervalHighOutputPower_Object = MibTableColumn
jnxoptIfOChGroupSrcIntervalHighOutputPower = _JnxoptIfOChGroupSrcIntervalHighOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 7, 1, 5),
    _JnxoptIfOChGroupSrcIntervalHighOutputPower_Type()
)
jnxoptIfOChGroupSrcIntervalHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcIntervalHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcIntervalHighOutputPower.setUnits("0.1 dbm")
_JnxoptIfOChGroupSrcIntervalLastAggregatedInputPower_Type = Integer32
_JnxoptIfOChGroupSrcIntervalLastAggregatedInputPower_Object = MibTableColumn
jnxoptIfOChGroupSrcIntervalLastAggregatedInputPower = _JnxoptIfOChGroupSrcIntervalLastAggregatedInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 7, 1, 6),
    _JnxoptIfOChGroupSrcIntervalLastAggregatedInputPower_Type()
)
jnxoptIfOChGroupSrcIntervalLastAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcIntervalLastAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcIntervalLastAggregatedInputPower.setUnits("0.1 dbm")
_JnxoptIfOChGroupSrcIntervalLowAggregatedInputPower_Type = Integer32
_JnxoptIfOChGroupSrcIntervalLowAggregatedInputPower_Object = MibTableColumn
jnxoptIfOChGroupSrcIntervalLowAggregatedInputPower = _JnxoptIfOChGroupSrcIntervalLowAggregatedInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 7, 1, 7),
    _JnxoptIfOChGroupSrcIntervalLowAggregatedInputPower_Type()
)
jnxoptIfOChGroupSrcIntervalLowAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcIntervalLowAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcIntervalLowAggregatedInputPower.setUnits("0.1 dbm")
_JnxoptIfOChGroupSrcIntervalHighAggregatedInputPower_Type = Integer32
_JnxoptIfOChGroupSrcIntervalHighAggregatedInputPower_Object = MibTableColumn
jnxoptIfOChGroupSrcIntervalHighAggregatedInputPower = _JnxoptIfOChGroupSrcIntervalHighAggregatedInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 7, 1, 8),
    _JnxoptIfOChGroupSrcIntervalHighAggregatedInputPower_Type()
)
jnxoptIfOChGroupSrcIntervalHighAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcIntervalHighAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcIntervalHighAggregatedInputPower.setUnits("0.1 dbm")
_JnxoptIfOChGroupSrcCurDayTable_Object = MibTable
jnxoptIfOChGroupSrcCurDayTable = _JnxoptIfOChGroupSrcCurDayTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 8)
)
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcCurDayTable.setStatus("current")
_JnxoptIfOChGroupSrcCurDayEntry_Object = MibTableRow
jnxoptIfOChGroupSrcCurDayEntry = _JnxoptIfOChGroupSrcCurDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 8, 1)
)
jnxoptIfOChGroupSrcCurDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcCurDayEntry.setStatus("current")
_JnxoptIfOChGroupSrcCurDaySuspectedFlag_Type = TruthValue
_JnxoptIfOChGroupSrcCurDaySuspectedFlag_Object = MibTableColumn
jnxoptIfOChGroupSrcCurDaySuspectedFlag = _JnxoptIfOChGroupSrcCurDaySuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 8, 1, 1),
    _JnxoptIfOChGroupSrcCurDaySuspectedFlag_Type()
)
jnxoptIfOChGroupSrcCurDaySuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcCurDaySuspectedFlag.setStatus("current")
_JnxoptIfOChGroupSrcCurDayLowOutputPower_Type = Integer32
_JnxoptIfOChGroupSrcCurDayLowOutputPower_Object = MibTableColumn
jnxoptIfOChGroupSrcCurDayLowOutputPower = _JnxoptIfOChGroupSrcCurDayLowOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 8, 1, 2),
    _JnxoptIfOChGroupSrcCurDayLowOutputPower_Type()
)
jnxoptIfOChGroupSrcCurDayLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcCurDayLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcCurDayLowOutputPower.setUnits("0.1 dbm")
_JnxoptIfOChGroupSrcCurDayHighOutputPower_Type = Integer32
_JnxoptIfOChGroupSrcCurDayHighOutputPower_Object = MibTableColumn
jnxoptIfOChGroupSrcCurDayHighOutputPower = _JnxoptIfOChGroupSrcCurDayHighOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 8, 1, 3),
    _JnxoptIfOChGroupSrcCurDayHighOutputPower_Type()
)
jnxoptIfOChGroupSrcCurDayHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcCurDayHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcCurDayHighOutputPower.setUnits("0.1 dbm")
_JnxoptIfOChGroupSrcCurDayLowAggregatedInputPower_Type = Integer32
_JnxoptIfOChGroupSrcCurDayLowAggregatedInputPower_Object = MibTableColumn
jnxoptIfOChGroupSrcCurDayLowAggregatedInputPower = _JnxoptIfOChGroupSrcCurDayLowAggregatedInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 8, 1, 4),
    _JnxoptIfOChGroupSrcCurDayLowAggregatedInputPower_Type()
)
jnxoptIfOChGroupSrcCurDayLowAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcCurDayLowAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcCurDayLowAggregatedInputPower.setUnits("0.1 dbm")
_JnxoptIfOChGroupSrcCurDayHighAggregatedInputPower_Type = Integer32
_JnxoptIfOChGroupSrcCurDayHighAggregatedInputPower_Object = MibTableColumn
jnxoptIfOChGroupSrcCurDayHighAggregatedInputPower = _JnxoptIfOChGroupSrcCurDayHighAggregatedInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 8, 1, 5),
    _JnxoptIfOChGroupSrcCurDayHighAggregatedInputPower_Type()
)
jnxoptIfOChGroupSrcCurDayHighAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcCurDayHighAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcCurDayHighAggregatedInputPower.setUnits("0.1 dbm")
_JnxoptIfOChGroupSrcPrevDayTable_Object = MibTable
jnxoptIfOChGroupSrcPrevDayTable = _JnxoptIfOChGroupSrcPrevDayTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 9)
)
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcPrevDayTable.setStatus("current")
_JnxoptIfOChGroupSrcPrevDayEntry_Object = MibTableRow
jnxoptIfOChGroupSrcPrevDayEntry = _JnxoptIfOChGroupSrcPrevDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 9, 1)
)
jnxoptIfOChGroupSrcPrevDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcPrevDayEntry.setStatus("current")
_JnxoptIfOChGroupSrcPrevDaySuspectedFlag_Type = TruthValue
_JnxoptIfOChGroupSrcPrevDaySuspectedFlag_Object = MibTableColumn
jnxoptIfOChGroupSrcPrevDaySuspectedFlag = _JnxoptIfOChGroupSrcPrevDaySuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 9, 1, 1),
    _JnxoptIfOChGroupSrcPrevDaySuspectedFlag_Type()
)
jnxoptIfOChGroupSrcPrevDaySuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcPrevDaySuspectedFlag.setStatus("current")
_JnxoptIfOChGroupSrcPrevDayLastOutputPower_Type = Integer32
_JnxoptIfOChGroupSrcPrevDayLastOutputPower_Object = MibTableColumn
jnxoptIfOChGroupSrcPrevDayLastOutputPower = _JnxoptIfOChGroupSrcPrevDayLastOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 9, 1, 2),
    _JnxoptIfOChGroupSrcPrevDayLastOutputPower_Type()
)
jnxoptIfOChGroupSrcPrevDayLastOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcPrevDayLastOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcPrevDayLastOutputPower.setUnits("0.1 dbm")
_JnxoptIfOChGroupSrcPrevDayLowOutputPower_Type = Integer32
_JnxoptIfOChGroupSrcPrevDayLowOutputPower_Object = MibTableColumn
jnxoptIfOChGroupSrcPrevDayLowOutputPower = _JnxoptIfOChGroupSrcPrevDayLowOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 9, 1, 3),
    _JnxoptIfOChGroupSrcPrevDayLowOutputPower_Type()
)
jnxoptIfOChGroupSrcPrevDayLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcPrevDayLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcPrevDayLowOutputPower.setUnits("0.1 dbm")
_JnxoptIfOChGroupSrcPrevDayHighOutputPower_Type = Integer32
_JnxoptIfOChGroupSrcPrevDayHighOutputPower_Object = MibTableColumn
jnxoptIfOChGroupSrcPrevDayHighOutputPower = _JnxoptIfOChGroupSrcPrevDayHighOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 9, 1, 4),
    _JnxoptIfOChGroupSrcPrevDayHighOutputPower_Type()
)
jnxoptIfOChGroupSrcPrevDayHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcPrevDayHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcPrevDayHighOutputPower.setUnits("0.1 dbm")
_JnxoptIfOChGroupSrcPrevDayLastAggregatedInputPower_Type = Integer32
_JnxoptIfOChGroupSrcPrevDayLastAggregatedInputPower_Object = MibTableColumn
jnxoptIfOChGroupSrcPrevDayLastAggregatedInputPower = _JnxoptIfOChGroupSrcPrevDayLastAggregatedInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 9, 1, 5),
    _JnxoptIfOChGroupSrcPrevDayLastAggregatedInputPower_Type()
)
jnxoptIfOChGroupSrcPrevDayLastAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcPrevDayLastAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcPrevDayLastAggregatedInputPower.setUnits("0.1 dbm")
_JnxoptIfOChGroupSrcPrevDayLowAggregatedInputPower_Type = Integer32
_JnxoptIfOChGroupSrcPrevDayLowAggregatedInputPower_Object = MibTableColumn
jnxoptIfOChGroupSrcPrevDayLowAggregatedInputPower = _JnxoptIfOChGroupSrcPrevDayLowAggregatedInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 9, 1, 6),
    _JnxoptIfOChGroupSrcPrevDayLowAggregatedInputPower_Type()
)
jnxoptIfOChGroupSrcPrevDayLowAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcPrevDayLowAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcPrevDayLowAggregatedInputPower.setUnits("0.1 dbm")
_JnxoptIfOChGroupSrcPrevDayHighAggregatedInputPower_Type = Integer32
_JnxoptIfOChGroupSrcPrevDayHighAggregatedInputPower_Object = MibTableColumn
jnxoptIfOChGroupSrcPrevDayHighAggregatedInputPower = _JnxoptIfOChGroupSrcPrevDayHighAggregatedInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 5, 9, 1, 7),
    _JnxoptIfOChGroupSrcPrevDayHighAggregatedInputPower_Type()
)
jnxoptIfOChGroupSrcPrevDayHighAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcPrevDayHighAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSrcPrevDayHighAggregatedInputPower.setUnits("0.1 dbm")
_JnxoptIfOCh_ObjectIdentity = ObjectIdentity
jnxoptIfOCh = _JnxoptIfOCh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6)
)
_JnxoptIfOChConfigTable_Object = MibTable
jnxoptIfOChConfigTable = _JnxoptIfOChConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    jnxoptIfOChConfigTable.setStatus("current")
_JnxoptIfOChConfigEntry_Object = MibTableRow
jnxoptIfOChConfigEntry = _JnxoptIfOChConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 1, 1)
)
jnxoptIfOChConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxoptIfOChConfigEntry.setStatus("current")
_JnxoptIfOChDirectionality_Type = JnxoptIfDirectionality
_JnxoptIfOChDirectionality_Object = MibTableColumn
jnxoptIfOChDirectionality = _JnxoptIfOChDirectionality_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 1, 1, 1),
    _JnxoptIfOChDirectionality_Type()
)
jnxoptIfOChDirectionality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChDirectionality.setStatus("current")


class _JnxoptIfOChCurrentStatus_Type(Bits):
    """Custom type jnxoptIfOChCurrentStatus based on Bits"""
    namedValues = NamedValues(
        *(("los", 1),
          ("losP", 0),
          ("oci", 2),
          ("ssf", 5),
          ("ssfO", 4),
          ("ssfP", 3))
    )

_JnxoptIfOChCurrentStatus_Type.__name__ = "Bits"
_JnxoptIfOChCurrentStatus_Object = MibTableColumn
jnxoptIfOChCurrentStatus = _JnxoptIfOChCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 1, 1, 2),
    _JnxoptIfOChCurrentStatus_Type()
)
jnxoptIfOChCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChCurrentStatus.setStatus("current")
_JnxoptIfOChSinkCurrentTable_Object = MibTable
jnxoptIfOChSinkCurrentTable = _JnxoptIfOChSinkCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 2)
)
if mibBuilder.loadTexts:
    jnxoptIfOChSinkCurrentTable.setStatus("current")
_JnxoptIfOChSinkCurrentEntry_Object = MibTableRow
jnxoptIfOChSinkCurrentEntry = _JnxoptIfOChSinkCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 2, 1)
)
jnxoptIfOChSinkCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxoptIfOChSinkCurrentEntry.setStatus("current")
_JnxoptIfOChSinkCurrentSuspectedFlag_Type = TruthValue
_JnxoptIfOChSinkCurrentSuspectedFlag_Object = MibTableColumn
jnxoptIfOChSinkCurrentSuspectedFlag = _JnxoptIfOChSinkCurrentSuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 2, 1, 1),
    _JnxoptIfOChSinkCurrentSuspectedFlag_Type()
)
jnxoptIfOChSinkCurrentSuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChSinkCurrentSuspectedFlag.setStatus("current")
_JnxoptIfOChSinkCurrentInputPower_Type = Integer32
_JnxoptIfOChSinkCurrentInputPower_Object = MibTableColumn
jnxoptIfOChSinkCurrentInputPower = _JnxoptIfOChSinkCurrentInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 2, 1, 2),
    _JnxoptIfOChSinkCurrentInputPower_Type()
)
jnxoptIfOChSinkCurrentInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChSinkCurrentInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChSinkCurrentInputPower.setUnits("0.1 dbm")
_JnxoptIfOChSinkCurrentLowInputPower_Type = Integer32
_JnxoptIfOChSinkCurrentLowInputPower_Object = MibTableColumn
jnxoptIfOChSinkCurrentLowInputPower = _JnxoptIfOChSinkCurrentLowInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 2, 1, 3),
    _JnxoptIfOChSinkCurrentLowInputPower_Type()
)
jnxoptIfOChSinkCurrentLowInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChSinkCurrentLowInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChSinkCurrentLowInputPower.setUnits("0.1 dbm")
_JnxoptIfOChSinkCurrentHighInputPower_Type = Integer32
_JnxoptIfOChSinkCurrentHighInputPower_Object = MibTableColumn
jnxoptIfOChSinkCurrentHighInputPower = _JnxoptIfOChSinkCurrentHighInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 2, 1, 4),
    _JnxoptIfOChSinkCurrentHighInputPower_Type()
)
jnxoptIfOChSinkCurrentHighInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChSinkCurrentHighInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChSinkCurrentHighInputPower.setUnits("0.1 dbm")
_JnxoptIfOChSinkCurrentLowerInputPowerThreshold_Type = Integer32
_JnxoptIfOChSinkCurrentLowerInputPowerThreshold_Object = MibTableColumn
jnxoptIfOChSinkCurrentLowerInputPowerThreshold = _JnxoptIfOChSinkCurrentLowerInputPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 2, 1, 5),
    _JnxoptIfOChSinkCurrentLowerInputPowerThreshold_Type()
)
jnxoptIfOChSinkCurrentLowerInputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOChSinkCurrentLowerInputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChSinkCurrentLowerInputPowerThreshold.setUnits("0.1 dbm")
_JnxoptIfOChSinkCurrentUpperInputPowerThreshold_Type = Integer32
_JnxoptIfOChSinkCurrentUpperInputPowerThreshold_Object = MibTableColumn
jnxoptIfOChSinkCurrentUpperInputPowerThreshold = _JnxoptIfOChSinkCurrentUpperInputPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 2, 1, 6),
    _JnxoptIfOChSinkCurrentUpperInputPowerThreshold_Type()
)
jnxoptIfOChSinkCurrentUpperInputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOChSinkCurrentUpperInputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChSinkCurrentUpperInputPowerThreshold.setUnits("0.1 dbm")
_JnxoptIfOChSinkIntervalTable_Object = MibTable
jnxoptIfOChSinkIntervalTable = _JnxoptIfOChSinkIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 3)
)
if mibBuilder.loadTexts:
    jnxoptIfOChSinkIntervalTable.setStatus("current")
_JnxoptIfOChSinkIntervalEntry_Object = MibTableRow
jnxoptIfOChSinkIntervalEntry = _JnxoptIfOChSinkIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 3, 1)
)
jnxoptIfOChSinkIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "JNX-OPT-IF-MIB", "jnxoptIfOChSinkIntervalNumber"),
)
if mibBuilder.loadTexts:
    jnxoptIfOChSinkIntervalEntry.setStatus("current")
_JnxoptIfOChSinkIntervalNumber_Type = JnxoptIfIntervalNumber
_JnxoptIfOChSinkIntervalNumber_Object = MibTableColumn
jnxoptIfOChSinkIntervalNumber = _JnxoptIfOChSinkIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 3, 1, 1),
    _JnxoptIfOChSinkIntervalNumber_Type()
)
jnxoptIfOChSinkIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxoptIfOChSinkIntervalNumber.setStatus("current")
_JnxoptIfOChSinkIntervalSuspectedFlag_Type = TruthValue
_JnxoptIfOChSinkIntervalSuspectedFlag_Object = MibTableColumn
jnxoptIfOChSinkIntervalSuspectedFlag = _JnxoptIfOChSinkIntervalSuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 3, 1, 2),
    _JnxoptIfOChSinkIntervalSuspectedFlag_Type()
)
jnxoptIfOChSinkIntervalSuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChSinkIntervalSuspectedFlag.setStatus("current")
_JnxoptIfOChSinkIntervalLastInputPower_Type = Integer32
_JnxoptIfOChSinkIntervalLastInputPower_Object = MibTableColumn
jnxoptIfOChSinkIntervalLastInputPower = _JnxoptIfOChSinkIntervalLastInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 3, 1, 3),
    _JnxoptIfOChSinkIntervalLastInputPower_Type()
)
jnxoptIfOChSinkIntervalLastInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChSinkIntervalLastInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChSinkIntervalLastInputPower.setUnits("0.1 dbm")
_JnxoptIfOChSinkIntervalLowInputPower_Type = Integer32
_JnxoptIfOChSinkIntervalLowInputPower_Object = MibTableColumn
jnxoptIfOChSinkIntervalLowInputPower = _JnxoptIfOChSinkIntervalLowInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 3, 1, 4),
    _JnxoptIfOChSinkIntervalLowInputPower_Type()
)
jnxoptIfOChSinkIntervalLowInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChSinkIntervalLowInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChSinkIntervalLowInputPower.setUnits("0.1 dbm")
_JnxoptIfOChSinkIntervalHighInputPower_Type = Integer32
_JnxoptIfOChSinkIntervalHighInputPower_Object = MibTableColumn
jnxoptIfOChSinkIntervalHighInputPower = _JnxoptIfOChSinkIntervalHighInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 3, 1, 5),
    _JnxoptIfOChSinkIntervalHighInputPower_Type()
)
jnxoptIfOChSinkIntervalHighInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChSinkIntervalHighInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChSinkIntervalHighInputPower.setUnits("0.1 dbm")
_JnxoptIfOChSinkCurDayTable_Object = MibTable
jnxoptIfOChSinkCurDayTable = _JnxoptIfOChSinkCurDayTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 4)
)
if mibBuilder.loadTexts:
    jnxoptIfOChSinkCurDayTable.setStatus("current")
_JnxoptIfOChSinkCurDayEntry_Object = MibTableRow
jnxoptIfOChSinkCurDayEntry = _JnxoptIfOChSinkCurDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 4, 1)
)
jnxoptIfOChSinkCurDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxoptIfOChSinkCurDayEntry.setStatus("current")
_JnxoptIfOChSinkCurDaySuspectedFlag_Type = TruthValue
_JnxoptIfOChSinkCurDaySuspectedFlag_Object = MibTableColumn
jnxoptIfOChSinkCurDaySuspectedFlag = _JnxoptIfOChSinkCurDaySuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 4, 1, 1),
    _JnxoptIfOChSinkCurDaySuspectedFlag_Type()
)
jnxoptIfOChSinkCurDaySuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChSinkCurDaySuspectedFlag.setStatus("current")
_JnxoptIfOChSinkCurDayLowInputPower_Type = Integer32
_JnxoptIfOChSinkCurDayLowInputPower_Object = MibTableColumn
jnxoptIfOChSinkCurDayLowInputPower = _JnxoptIfOChSinkCurDayLowInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 4, 1, 2),
    _JnxoptIfOChSinkCurDayLowInputPower_Type()
)
jnxoptIfOChSinkCurDayLowInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChSinkCurDayLowInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChSinkCurDayLowInputPower.setUnits("0.1 dbm")
_JnxoptIfOChSinkCurDayHighInputPower_Type = Integer32
_JnxoptIfOChSinkCurDayHighInputPower_Object = MibTableColumn
jnxoptIfOChSinkCurDayHighInputPower = _JnxoptIfOChSinkCurDayHighInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 4, 1, 3),
    _JnxoptIfOChSinkCurDayHighInputPower_Type()
)
jnxoptIfOChSinkCurDayHighInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChSinkCurDayHighInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChSinkCurDayHighInputPower.setUnits("0.1 dbm")
_JnxoptIfOChSinkPrevDayTable_Object = MibTable
jnxoptIfOChSinkPrevDayTable = _JnxoptIfOChSinkPrevDayTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 5)
)
if mibBuilder.loadTexts:
    jnxoptIfOChSinkPrevDayTable.setStatus("current")
_JnxoptIfOChSinkPrevDayEntry_Object = MibTableRow
jnxoptIfOChSinkPrevDayEntry = _JnxoptIfOChSinkPrevDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 5, 1)
)
jnxoptIfOChSinkPrevDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxoptIfOChSinkPrevDayEntry.setStatus("current")
_JnxoptIfOChSinkPrevDaySuspectedFlag_Type = TruthValue
_JnxoptIfOChSinkPrevDaySuspectedFlag_Object = MibTableColumn
jnxoptIfOChSinkPrevDaySuspectedFlag = _JnxoptIfOChSinkPrevDaySuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 5, 1, 1),
    _JnxoptIfOChSinkPrevDaySuspectedFlag_Type()
)
jnxoptIfOChSinkPrevDaySuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChSinkPrevDaySuspectedFlag.setStatus("current")
_JnxoptIfOChSinkPrevDayLastInputPower_Type = Integer32
_JnxoptIfOChSinkPrevDayLastInputPower_Object = MibTableColumn
jnxoptIfOChSinkPrevDayLastInputPower = _JnxoptIfOChSinkPrevDayLastInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 5, 1, 2),
    _JnxoptIfOChSinkPrevDayLastInputPower_Type()
)
jnxoptIfOChSinkPrevDayLastInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChSinkPrevDayLastInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChSinkPrevDayLastInputPower.setUnits("0.1 dbm")
_JnxoptIfOChSinkPrevDayLowInputPower_Type = Integer32
_JnxoptIfOChSinkPrevDayLowInputPower_Object = MibTableColumn
jnxoptIfOChSinkPrevDayLowInputPower = _JnxoptIfOChSinkPrevDayLowInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 5, 1, 3),
    _JnxoptIfOChSinkPrevDayLowInputPower_Type()
)
jnxoptIfOChSinkPrevDayLowInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChSinkPrevDayLowInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChSinkPrevDayLowInputPower.setUnits("0.1 dbm")
_JnxoptIfOChSinkPrevDayHighInputPower_Type = Integer32
_JnxoptIfOChSinkPrevDayHighInputPower_Object = MibTableColumn
jnxoptIfOChSinkPrevDayHighInputPower = _JnxoptIfOChSinkPrevDayHighInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 5, 1, 4),
    _JnxoptIfOChSinkPrevDayHighInputPower_Type()
)
jnxoptIfOChSinkPrevDayHighInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChSinkPrevDayHighInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChSinkPrevDayHighInputPower.setUnits("0.1 dbm")
_JnxoptIfOChSrcCurrentTable_Object = MibTable
jnxoptIfOChSrcCurrentTable = _JnxoptIfOChSrcCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 6)
)
if mibBuilder.loadTexts:
    jnxoptIfOChSrcCurrentTable.setStatus("current")
_JnxoptIfOChSrcCurrentEntry_Object = MibTableRow
jnxoptIfOChSrcCurrentEntry = _JnxoptIfOChSrcCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 6, 1)
)
jnxoptIfOChSrcCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxoptIfOChSrcCurrentEntry.setStatus("current")
_JnxoptIfOChSrcCurrentSuspectedFlag_Type = TruthValue
_JnxoptIfOChSrcCurrentSuspectedFlag_Object = MibTableColumn
jnxoptIfOChSrcCurrentSuspectedFlag = _JnxoptIfOChSrcCurrentSuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 6, 1, 1),
    _JnxoptIfOChSrcCurrentSuspectedFlag_Type()
)
jnxoptIfOChSrcCurrentSuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcCurrentSuspectedFlag.setStatus("current")
_JnxoptIfOChSrcCurrentOutputPower_Type = Integer32
_JnxoptIfOChSrcCurrentOutputPower_Object = MibTableColumn
jnxoptIfOChSrcCurrentOutputPower = _JnxoptIfOChSrcCurrentOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 6, 1, 2),
    _JnxoptIfOChSrcCurrentOutputPower_Type()
)
jnxoptIfOChSrcCurrentOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcCurrentOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcCurrentOutputPower.setUnits("0.1 dbm")
_JnxoptIfOChSrcCurrentLowOutputPower_Type = Integer32
_JnxoptIfOChSrcCurrentLowOutputPower_Object = MibTableColumn
jnxoptIfOChSrcCurrentLowOutputPower = _JnxoptIfOChSrcCurrentLowOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 6, 1, 3),
    _JnxoptIfOChSrcCurrentLowOutputPower_Type()
)
jnxoptIfOChSrcCurrentLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcCurrentLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcCurrentLowOutputPower.setUnits("0.1 dbm")
_JnxoptIfOChSrcCurrentHighOutputPower_Type = Integer32
_JnxoptIfOChSrcCurrentHighOutputPower_Object = MibTableColumn
jnxoptIfOChSrcCurrentHighOutputPower = _JnxoptIfOChSrcCurrentHighOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 6, 1, 4),
    _JnxoptIfOChSrcCurrentHighOutputPower_Type()
)
jnxoptIfOChSrcCurrentHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcCurrentHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcCurrentHighOutputPower.setUnits("0.1 dbm")
_JnxoptIfOChSrcCurrentLowerOutputPowerThreshold_Type = Integer32
_JnxoptIfOChSrcCurrentLowerOutputPowerThreshold_Object = MibTableColumn
jnxoptIfOChSrcCurrentLowerOutputPowerThreshold = _JnxoptIfOChSrcCurrentLowerOutputPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 6, 1, 5),
    _JnxoptIfOChSrcCurrentLowerOutputPowerThreshold_Type()
)
jnxoptIfOChSrcCurrentLowerOutputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcCurrentLowerOutputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcCurrentLowerOutputPowerThreshold.setUnits("0.1 dbm")
_JnxoptIfOChSrcCurrentUpperOutputPowerThreshold_Type = Integer32
_JnxoptIfOChSrcCurrentUpperOutputPowerThreshold_Object = MibTableColumn
jnxoptIfOChSrcCurrentUpperOutputPowerThreshold = _JnxoptIfOChSrcCurrentUpperOutputPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 6, 1, 6),
    _JnxoptIfOChSrcCurrentUpperOutputPowerThreshold_Type()
)
jnxoptIfOChSrcCurrentUpperOutputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcCurrentUpperOutputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcCurrentUpperOutputPowerThreshold.setUnits("0.1 dbm")
_JnxoptIfOChSrcIntervalTable_Object = MibTable
jnxoptIfOChSrcIntervalTable = _JnxoptIfOChSrcIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 7)
)
if mibBuilder.loadTexts:
    jnxoptIfOChSrcIntervalTable.setStatus("current")
_JnxoptIfOChSrcIntervalEntry_Object = MibTableRow
jnxoptIfOChSrcIntervalEntry = _JnxoptIfOChSrcIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 7, 1)
)
jnxoptIfOChSrcIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "JNX-OPT-IF-MIB", "jnxoptIfOChSrcIntervalNumber"),
)
if mibBuilder.loadTexts:
    jnxoptIfOChSrcIntervalEntry.setStatus("current")
_JnxoptIfOChSrcIntervalNumber_Type = JnxoptIfIntervalNumber
_JnxoptIfOChSrcIntervalNumber_Object = MibTableColumn
jnxoptIfOChSrcIntervalNumber = _JnxoptIfOChSrcIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 7, 1, 1),
    _JnxoptIfOChSrcIntervalNumber_Type()
)
jnxoptIfOChSrcIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcIntervalNumber.setStatus("current")
_JnxoptIfOChSrcIntervalSuspectedFlag_Type = TruthValue
_JnxoptIfOChSrcIntervalSuspectedFlag_Object = MibTableColumn
jnxoptIfOChSrcIntervalSuspectedFlag = _JnxoptIfOChSrcIntervalSuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 7, 1, 2),
    _JnxoptIfOChSrcIntervalSuspectedFlag_Type()
)
jnxoptIfOChSrcIntervalSuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcIntervalSuspectedFlag.setStatus("current")
_JnxoptIfOChSrcIntervalLastOutputPower_Type = Integer32
_JnxoptIfOChSrcIntervalLastOutputPower_Object = MibTableColumn
jnxoptIfOChSrcIntervalLastOutputPower = _JnxoptIfOChSrcIntervalLastOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 7, 1, 3),
    _JnxoptIfOChSrcIntervalLastOutputPower_Type()
)
jnxoptIfOChSrcIntervalLastOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcIntervalLastOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcIntervalLastOutputPower.setUnits("0.1 dbm")
_JnxoptIfOChSrcIntervalLowOutputPower_Type = Integer32
_JnxoptIfOChSrcIntervalLowOutputPower_Object = MibTableColumn
jnxoptIfOChSrcIntervalLowOutputPower = _JnxoptIfOChSrcIntervalLowOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 7, 1, 4),
    _JnxoptIfOChSrcIntervalLowOutputPower_Type()
)
jnxoptIfOChSrcIntervalLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcIntervalLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcIntervalLowOutputPower.setUnits("0.1 dbm")
_JnxoptIfOChSrcIntervalHighOutputPower_Type = Integer32
_JnxoptIfOChSrcIntervalHighOutputPower_Object = MibTableColumn
jnxoptIfOChSrcIntervalHighOutputPower = _JnxoptIfOChSrcIntervalHighOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 7, 1, 5),
    _JnxoptIfOChSrcIntervalHighOutputPower_Type()
)
jnxoptIfOChSrcIntervalHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcIntervalHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcIntervalHighOutputPower.setUnits("0.1 dbm")
_JnxoptIfOChSrcCurDayTable_Object = MibTable
jnxoptIfOChSrcCurDayTable = _JnxoptIfOChSrcCurDayTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 8)
)
if mibBuilder.loadTexts:
    jnxoptIfOChSrcCurDayTable.setStatus("current")
_JnxoptIfOChSrcCurDayEntry_Object = MibTableRow
jnxoptIfOChSrcCurDayEntry = _JnxoptIfOChSrcCurDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 8, 1)
)
jnxoptIfOChSrcCurDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxoptIfOChSrcCurDayEntry.setStatus("current")
_JnxoptIfOChSrcCurDaySuspectedFlag_Type = TruthValue
_JnxoptIfOChSrcCurDaySuspectedFlag_Object = MibTableColumn
jnxoptIfOChSrcCurDaySuspectedFlag = _JnxoptIfOChSrcCurDaySuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 8, 1, 1),
    _JnxoptIfOChSrcCurDaySuspectedFlag_Type()
)
jnxoptIfOChSrcCurDaySuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcCurDaySuspectedFlag.setStatus("current")
_JnxoptIfOChSrcCurDayLowOutputPower_Type = Integer32
_JnxoptIfOChSrcCurDayLowOutputPower_Object = MibTableColumn
jnxoptIfOChSrcCurDayLowOutputPower = _JnxoptIfOChSrcCurDayLowOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 8, 1, 2),
    _JnxoptIfOChSrcCurDayLowOutputPower_Type()
)
jnxoptIfOChSrcCurDayLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcCurDayLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcCurDayLowOutputPower.setUnits("0.1 dbm")
_JnxoptIfOChSrcCurDayHighOutputPower_Type = Integer32
_JnxoptIfOChSrcCurDayHighOutputPower_Object = MibTableColumn
jnxoptIfOChSrcCurDayHighOutputPower = _JnxoptIfOChSrcCurDayHighOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 8, 1, 3),
    _JnxoptIfOChSrcCurDayHighOutputPower_Type()
)
jnxoptIfOChSrcCurDayHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcCurDayHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcCurDayHighOutputPower.setUnits("0.1 dbm")
_JnxoptIfOChSrcPrevDayTable_Object = MibTable
jnxoptIfOChSrcPrevDayTable = _JnxoptIfOChSrcPrevDayTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 9)
)
if mibBuilder.loadTexts:
    jnxoptIfOChSrcPrevDayTable.setStatus("current")
_JnxoptIfOChSrcPrevDayEntry_Object = MibTableRow
jnxoptIfOChSrcPrevDayEntry = _JnxoptIfOChSrcPrevDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 9, 1)
)
jnxoptIfOChSrcPrevDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxoptIfOChSrcPrevDayEntry.setStatus("current")
_JnxoptIfOChSrcPrevDaySuspectedFlag_Type = TruthValue
_JnxoptIfOChSrcPrevDaySuspectedFlag_Object = MibTableColumn
jnxoptIfOChSrcPrevDaySuspectedFlag = _JnxoptIfOChSrcPrevDaySuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 9, 1, 1),
    _JnxoptIfOChSrcPrevDaySuspectedFlag_Type()
)
jnxoptIfOChSrcPrevDaySuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcPrevDaySuspectedFlag.setStatus("current")
_JnxoptIfOChSrcPrevDayLastOutputPower_Type = Integer32
_JnxoptIfOChSrcPrevDayLastOutputPower_Object = MibTableColumn
jnxoptIfOChSrcPrevDayLastOutputPower = _JnxoptIfOChSrcPrevDayLastOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 9, 1, 2),
    _JnxoptIfOChSrcPrevDayLastOutputPower_Type()
)
jnxoptIfOChSrcPrevDayLastOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcPrevDayLastOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcPrevDayLastOutputPower.setUnits("0.1 dbm")
_JnxoptIfOChSrcPrevDayLowOutputPower_Type = Integer32
_JnxoptIfOChSrcPrevDayLowOutputPower_Object = MibTableColumn
jnxoptIfOChSrcPrevDayLowOutputPower = _JnxoptIfOChSrcPrevDayLowOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 9, 1, 3),
    _JnxoptIfOChSrcPrevDayLowOutputPower_Type()
)
jnxoptIfOChSrcPrevDayLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcPrevDayLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcPrevDayLowOutputPower.setUnits("0.1 dbm")
_JnxoptIfOChSrcPrevDayHighOutputPower_Type = Integer32
_JnxoptIfOChSrcPrevDayHighOutputPower_Object = MibTableColumn
jnxoptIfOChSrcPrevDayHighOutputPower = _JnxoptIfOChSrcPrevDayHighOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 6, 9, 1, 4),
    _JnxoptIfOChSrcPrevDayHighOutputPower_Type()
)
jnxoptIfOChSrcPrevDayHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcPrevDayHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOChSrcPrevDayHighOutputPower.setUnits("0.1 dbm")
_JnxoptIfOTUk_ObjectIdentity = ObjectIdentity
jnxoptIfOTUk = _JnxoptIfOTUk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 7)
)
_JnxoptIfOTUkConfigTable_Object = MibTable
jnxoptIfOTUkConfigTable = _JnxoptIfOTUkConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    jnxoptIfOTUkConfigTable.setStatus("current")
_JnxoptIfOTUkConfigEntry_Object = MibTableRow
jnxoptIfOTUkConfigEntry = _JnxoptIfOTUkConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 7, 1, 1)
)
jnxoptIfOTUkConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxoptIfOTUkConfigEntry.setStatus("current")
_JnxoptIfOTUkDirectionality_Type = JnxoptIfDirectionality
_JnxoptIfOTUkDirectionality_Object = MibTableColumn
jnxoptIfOTUkDirectionality = _JnxoptIfOTUkDirectionality_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 7, 1, 1, 1),
    _JnxoptIfOTUkDirectionality_Type()
)
jnxoptIfOTUkDirectionality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTUkDirectionality.setStatus("current")
_JnxoptIfOTUkBitRateK_Type = JnxoptIfBitRateK
_JnxoptIfOTUkBitRateK_Object = MibTableColumn
jnxoptIfOTUkBitRateK = _JnxoptIfOTUkBitRateK_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 7, 1, 1, 2),
    _JnxoptIfOTUkBitRateK_Type()
)
jnxoptIfOTUkBitRateK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTUkBitRateK.setStatus("current")
_JnxoptIfOTUkTraceIdentifierTransmitted_Type = JnxoptIfTxTI
_JnxoptIfOTUkTraceIdentifierTransmitted_Object = MibTableColumn
jnxoptIfOTUkTraceIdentifierTransmitted = _JnxoptIfOTUkTraceIdentifierTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 7, 1, 1, 3),
    _JnxoptIfOTUkTraceIdentifierTransmitted_Type()
)
jnxoptIfOTUkTraceIdentifierTransmitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOTUkTraceIdentifierTransmitted.setStatus("current")
_JnxoptIfOTUkDAPIExpected_Type = JnxoptIfExDAPI
_JnxoptIfOTUkDAPIExpected_Object = MibTableColumn
jnxoptIfOTUkDAPIExpected = _JnxoptIfOTUkDAPIExpected_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 7, 1, 1, 4),
    _JnxoptIfOTUkDAPIExpected_Type()
)
jnxoptIfOTUkDAPIExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOTUkDAPIExpected.setStatus("current")
_JnxoptIfOTUkSAPIExpected_Type = JnxoptIfExSAPI
_JnxoptIfOTUkSAPIExpected_Object = MibTableColumn
jnxoptIfOTUkSAPIExpected = _JnxoptIfOTUkSAPIExpected_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 7, 1, 1, 5),
    _JnxoptIfOTUkSAPIExpected_Type()
)
jnxoptIfOTUkSAPIExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOTUkSAPIExpected.setStatus("current")
_JnxoptIfOTUkTraceIdentifierAccepted_Type = JnxoptIfAcTI
_JnxoptIfOTUkTraceIdentifierAccepted_Object = MibTableColumn
jnxoptIfOTUkTraceIdentifierAccepted = _JnxoptIfOTUkTraceIdentifierAccepted_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 7, 1, 1, 6),
    _JnxoptIfOTUkTraceIdentifierAccepted_Type()
)
jnxoptIfOTUkTraceIdentifierAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTUkTraceIdentifierAccepted.setStatus("current")
_JnxoptIfOTUkTIMDetMode_Type = JnxoptIfTIMDetMode
_JnxoptIfOTUkTIMDetMode_Object = MibTableColumn
jnxoptIfOTUkTIMDetMode = _JnxoptIfOTUkTIMDetMode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 7, 1, 1, 7),
    _JnxoptIfOTUkTIMDetMode_Type()
)
jnxoptIfOTUkTIMDetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOTUkTIMDetMode.setStatus("current")
_JnxoptIfOTUkTIMActEnabled_Type = TruthValue
_JnxoptIfOTUkTIMActEnabled_Object = MibTableColumn
jnxoptIfOTUkTIMActEnabled = _JnxoptIfOTUkTIMActEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 7, 1, 1, 8),
    _JnxoptIfOTUkTIMActEnabled_Type()
)
jnxoptIfOTUkTIMActEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOTUkTIMActEnabled.setStatus("current")
_JnxoptIfOTUkDEGThr_Type = JnxoptIfDEGThr
_JnxoptIfOTUkDEGThr_Object = MibTableColumn
jnxoptIfOTUkDEGThr = _JnxoptIfOTUkDEGThr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 7, 1, 1, 9),
    _JnxoptIfOTUkDEGThr_Type()
)
jnxoptIfOTUkDEGThr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOTUkDEGThr.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfOTUkDEGThr.setUnits("percentage")
_JnxoptIfOTUkDEGM_Type = JnxoptIfDEGM
_JnxoptIfOTUkDEGM_Object = MibTableColumn
jnxoptIfOTUkDEGM = _JnxoptIfOTUkDEGM_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 7, 1, 1, 10),
    _JnxoptIfOTUkDEGM_Type()
)
jnxoptIfOTUkDEGM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOTUkDEGM.setStatus("current")
_JnxoptIfOTUkSinkAdaptActive_Type = TruthValue
_JnxoptIfOTUkSinkAdaptActive_Object = MibTableColumn
jnxoptIfOTUkSinkAdaptActive = _JnxoptIfOTUkSinkAdaptActive_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 7, 1, 1, 11),
    _JnxoptIfOTUkSinkAdaptActive_Type()
)
jnxoptIfOTUkSinkAdaptActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOTUkSinkAdaptActive.setStatus("current")
_JnxoptIfOTUkSourceAdaptActive_Type = TruthValue
_JnxoptIfOTUkSourceAdaptActive_Object = MibTableColumn
jnxoptIfOTUkSourceAdaptActive = _JnxoptIfOTUkSourceAdaptActive_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 7, 1, 1, 12),
    _JnxoptIfOTUkSourceAdaptActive_Type()
)
jnxoptIfOTUkSourceAdaptActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOTUkSourceAdaptActive.setStatus("current")
_JnxoptIfOTUkSinkFECEnabled_Type = TruthValue
_JnxoptIfOTUkSinkFECEnabled_Object = MibTableColumn
jnxoptIfOTUkSinkFECEnabled = _JnxoptIfOTUkSinkFECEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 7, 1, 1, 13),
    _JnxoptIfOTUkSinkFECEnabled_Type()
)
jnxoptIfOTUkSinkFECEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfOTUkSinkFECEnabled.setStatus("current")


class _JnxoptIfOTUkCurrentStatus_Type(Bits):
    """Custom type jnxoptIfOTUkCurrentStatus based on Bits"""
    namedValues = NamedValues(
        *(("ais", 5),
          ("bdi", 2),
          ("deg", 1),
          ("lof", 4),
          ("lom", 6),
          ("ssf", 3),
          ("tim", 0))
    )

_JnxoptIfOTUkCurrentStatus_Type.__name__ = "Bits"
_JnxoptIfOTUkCurrentStatus_Object = MibTableColumn
jnxoptIfOTUkCurrentStatus = _JnxoptIfOTUkCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 7, 1, 1, 14),
    _JnxoptIfOTUkCurrentStatus_Type()
)
jnxoptIfOTUkCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfOTUkCurrentStatus.setStatus("current")
_JnxoptIfGCC0ConfigTable_Object = MibTable
jnxoptIfGCC0ConfigTable = _JnxoptIfGCC0ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 7, 2)
)
if mibBuilder.loadTexts:
    jnxoptIfGCC0ConfigTable.setStatus("current")
_JnxoptIfGCC0ConfigEntry_Object = MibTableRow
jnxoptIfGCC0ConfigEntry = _JnxoptIfGCC0ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 7, 2, 1)
)
jnxoptIfGCC0ConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "JNX-OPT-IF-MIB", "jnxoptIfGCC0Directionality"),
)
if mibBuilder.loadTexts:
    jnxoptIfGCC0ConfigEntry.setStatus("current")
_JnxoptIfGCC0Directionality_Type = JnxoptIfDirectionality
_JnxoptIfGCC0Directionality_Object = MibTableColumn
jnxoptIfGCC0Directionality = _JnxoptIfGCC0Directionality_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 7, 2, 1, 1),
    _JnxoptIfGCC0Directionality_Type()
)
jnxoptIfGCC0Directionality.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxoptIfGCC0Directionality.setStatus("current")
_JnxoptIfGCC0Application_Type = SnmpAdminString
_JnxoptIfGCC0Application_Object = MibTableColumn
jnxoptIfGCC0Application = _JnxoptIfGCC0Application_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 7, 2, 1, 2),
    _JnxoptIfGCC0Application_Type()
)
jnxoptIfGCC0Application.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxoptIfGCC0Application.setStatus("current")
_JnxoptIfGCC0RowStatus_Type = RowStatus
_JnxoptIfGCC0RowStatus_Object = MibTableColumn
jnxoptIfGCC0RowStatus = _JnxoptIfGCC0RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 7, 2, 1, 3),
    _JnxoptIfGCC0RowStatus_Type()
)
jnxoptIfGCC0RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxoptIfGCC0RowStatus.setStatus("current")
_JnxoptIfODUk_ObjectIdentity = ObjectIdentity
jnxoptIfODUk = _JnxoptIfODUk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 8)
)
_JnxoptIfODUkConfigTable_Object = MibTable
jnxoptIfODUkConfigTable = _JnxoptIfODUkConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 8, 1)
)
if mibBuilder.loadTexts:
    jnxoptIfODUkConfigTable.setStatus("current")
_JnxoptIfODUkConfigEntry_Object = MibTableRow
jnxoptIfODUkConfigEntry = _JnxoptIfODUkConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 8, 1, 1)
)
jnxoptIfODUkConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxoptIfODUkConfigEntry.setStatus("current")
_JnxoptIfODUkDirectionality_Type = JnxoptIfDirectionality
_JnxoptIfODUkDirectionality_Object = MibTableColumn
jnxoptIfODUkDirectionality = _JnxoptIfODUkDirectionality_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 8, 1, 1, 1),
    _JnxoptIfODUkDirectionality_Type()
)
jnxoptIfODUkDirectionality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfODUkDirectionality.setStatus("current")
_JnxoptIfODUkBitRateK_Type = JnxoptIfBitRateK
_JnxoptIfODUkBitRateK_Object = MibTableColumn
jnxoptIfODUkBitRateK = _JnxoptIfODUkBitRateK_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 8, 1, 1, 2),
    _JnxoptIfODUkBitRateK_Type()
)
jnxoptIfODUkBitRateK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfODUkBitRateK.setStatus("current")


class _JnxoptIfODUkTcmFieldsInUse_Type(Bits):
    """Custom type jnxoptIfODUkTcmFieldsInUse based on Bits"""
    namedValues = NamedValues(
        *(("tcmField1", 0),
          ("tcmField2", 1),
          ("tcmField3", 2),
          ("tcmField4", 3),
          ("tcmField5", 4),
          ("tcmField6", 5))
    )

_JnxoptIfODUkTcmFieldsInUse_Type.__name__ = "Bits"
_JnxoptIfODUkTcmFieldsInUse_Object = MibTableColumn
jnxoptIfODUkTcmFieldsInUse = _JnxoptIfODUkTcmFieldsInUse_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 8, 1, 1, 3),
    _JnxoptIfODUkTcmFieldsInUse_Type()
)
jnxoptIfODUkTcmFieldsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfODUkTcmFieldsInUse.setStatus("current")
_JnxoptIfODUkPositionSeqCurrentSize_Type = Unsigned32
_JnxoptIfODUkPositionSeqCurrentSize_Object = MibTableColumn
jnxoptIfODUkPositionSeqCurrentSize = _JnxoptIfODUkPositionSeqCurrentSize_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 8, 1, 1, 4),
    _JnxoptIfODUkPositionSeqCurrentSize_Type()
)
jnxoptIfODUkPositionSeqCurrentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfODUkPositionSeqCurrentSize.setStatus("current")
_JnxoptIfODUkTtpPresent_Type = TruthValue
_JnxoptIfODUkTtpPresent_Object = MibTableColumn
jnxoptIfODUkTtpPresent = _JnxoptIfODUkTtpPresent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 8, 1, 1, 5),
    _JnxoptIfODUkTtpPresent_Type()
)
jnxoptIfODUkTtpPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfODUkTtpPresent.setStatus("current")
_JnxoptIfODUkTtpConfigTable_Object = MibTable
jnxoptIfODUkTtpConfigTable = _JnxoptIfODUkTtpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 8, 2)
)
if mibBuilder.loadTexts:
    jnxoptIfODUkTtpConfigTable.setStatus("current")
_JnxoptIfODUkTtpConfigEntry_Object = MibTableRow
jnxoptIfODUkTtpConfigEntry = _JnxoptIfODUkTtpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 8, 2, 1)
)
jnxoptIfODUkTtpConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxoptIfODUkTtpConfigEntry.setStatus("current")
_JnxoptIfODUkTtpTraceIdentifierTransmitted_Type = JnxoptIfTxTI
_JnxoptIfODUkTtpTraceIdentifierTransmitted_Object = MibTableColumn
jnxoptIfODUkTtpTraceIdentifierTransmitted = _JnxoptIfODUkTtpTraceIdentifierTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 8, 2, 1, 1),
    _JnxoptIfODUkTtpTraceIdentifierTransmitted_Type()
)
jnxoptIfODUkTtpTraceIdentifierTransmitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfODUkTtpTraceIdentifierTransmitted.setStatus("current")
_JnxoptIfODUkTtpDAPIExpected_Type = JnxoptIfExDAPI
_JnxoptIfODUkTtpDAPIExpected_Object = MibTableColumn
jnxoptIfODUkTtpDAPIExpected = _JnxoptIfODUkTtpDAPIExpected_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 8, 2, 1, 2),
    _JnxoptIfODUkTtpDAPIExpected_Type()
)
jnxoptIfODUkTtpDAPIExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfODUkTtpDAPIExpected.setStatus("current")
_JnxoptIfODUkTtpSAPIExpected_Type = JnxoptIfExSAPI
_JnxoptIfODUkTtpSAPIExpected_Object = MibTableColumn
jnxoptIfODUkTtpSAPIExpected = _JnxoptIfODUkTtpSAPIExpected_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 8, 2, 1, 3),
    _JnxoptIfODUkTtpSAPIExpected_Type()
)
jnxoptIfODUkTtpSAPIExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfODUkTtpSAPIExpected.setStatus("current")
_JnxoptIfODUkTtpTraceIdentifierAccepted_Type = JnxoptIfAcTI
_JnxoptIfODUkTtpTraceIdentifierAccepted_Object = MibTableColumn
jnxoptIfODUkTtpTraceIdentifierAccepted = _JnxoptIfODUkTtpTraceIdentifierAccepted_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 8, 2, 1, 4),
    _JnxoptIfODUkTtpTraceIdentifierAccepted_Type()
)
jnxoptIfODUkTtpTraceIdentifierAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfODUkTtpTraceIdentifierAccepted.setStatus("current")
_JnxoptIfODUkTtpTIMDetMode_Type = JnxoptIfTIMDetMode
_JnxoptIfODUkTtpTIMDetMode_Object = MibTableColumn
jnxoptIfODUkTtpTIMDetMode = _JnxoptIfODUkTtpTIMDetMode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 8, 2, 1, 5),
    _JnxoptIfODUkTtpTIMDetMode_Type()
)
jnxoptIfODUkTtpTIMDetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfODUkTtpTIMDetMode.setStatus("current")
_JnxoptIfODUkTtpTIMActEnabled_Type = TruthValue
_JnxoptIfODUkTtpTIMActEnabled_Object = MibTableColumn
jnxoptIfODUkTtpTIMActEnabled = _JnxoptIfODUkTtpTIMActEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 8, 2, 1, 6),
    _JnxoptIfODUkTtpTIMActEnabled_Type()
)
jnxoptIfODUkTtpTIMActEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfODUkTtpTIMActEnabled.setStatus("current")
_JnxoptIfODUkTtpDEGThr_Type = JnxoptIfDEGThr
_JnxoptIfODUkTtpDEGThr_Object = MibTableColumn
jnxoptIfODUkTtpDEGThr = _JnxoptIfODUkTtpDEGThr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 8, 2, 1, 7),
    _JnxoptIfODUkTtpDEGThr_Type()
)
jnxoptIfODUkTtpDEGThr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfODUkTtpDEGThr.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfODUkTtpDEGThr.setUnits("percentage")
_JnxoptIfODUkTtpDEGM_Type = JnxoptIfDEGM
_JnxoptIfODUkTtpDEGM_Object = MibTableColumn
jnxoptIfODUkTtpDEGM = _JnxoptIfODUkTtpDEGM_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 8, 2, 1, 8),
    _JnxoptIfODUkTtpDEGM_Type()
)
jnxoptIfODUkTtpDEGM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxoptIfODUkTtpDEGM.setStatus("current")


class _JnxoptIfODUkTtpCurrentStatus_Type(Bits):
    """Custom type jnxoptIfODUkTtpCurrentStatus based on Bits"""
    namedValues = NamedValues(
        *(("bdi", 4),
          ("deg", 3),
          ("lck", 1),
          ("oci", 0),
          ("ssf", 5),
          ("tim", 2))
    )

_JnxoptIfODUkTtpCurrentStatus_Type.__name__ = "Bits"
_JnxoptIfODUkTtpCurrentStatus_Object = MibTableColumn
jnxoptIfODUkTtpCurrentStatus = _JnxoptIfODUkTtpCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 8, 2, 1, 9),
    _JnxoptIfODUkTtpCurrentStatus_Type()
)
jnxoptIfODUkTtpCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfODUkTtpCurrentStatus.setStatus("current")
_JnxoptIfODUkPositionSeqTable_Object = MibTable
jnxoptIfODUkPositionSeqTable = _JnxoptIfODUkPositionSeqTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 8, 3)
)
if mibBuilder.loadTexts:
    jnxoptIfODUkPositionSeqTable.setStatus("current")
_JnxoptIfODUkPositionSeqEntry_Object = MibTableRow
jnxoptIfODUkPositionSeqEntry = _JnxoptIfODUkPositionSeqEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 8, 3, 1)
)
jnxoptIfODUkPositionSeqEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "JNX-OPT-IF-MIB", "jnxoptIfODUkPositionSeqIndex"),
)
if mibBuilder.loadTexts:
    jnxoptIfODUkPositionSeqEntry.setStatus("current")


class _JnxoptIfODUkPositionSeqIndex_Type(Unsigned32):
    """Custom type jnxoptIfODUkPositionSeqIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_JnxoptIfODUkPositionSeqIndex_Type.__name__ = "Unsigned32"
_JnxoptIfODUkPositionSeqIndex_Object = MibTableColumn
jnxoptIfODUkPositionSeqIndex = _JnxoptIfODUkPositionSeqIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 8, 3, 1, 1),
    _JnxoptIfODUkPositionSeqIndex_Type()
)
jnxoptIfODUkPositionSeqIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxoptIfODUkPositionSeqIndex.setStatus("current")
_JnxoptIfODUkPositionSeqPosition_Type = Unsigned32
_JnxoptIfODUkPositionSeqPosition_Object = MibTableColumn
jnxoptIfODUkPositionSeqPosition = _JnxoptIfODUkPositionSeqPosition_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 8, 3, 1, 2),
    _JnxoptIfODUkPositionSeqPosition_Type()
)
jnxoptIfODUkPositionSeqPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfODUkPositionSeqPosition.setStatus("current")
_JnxoptIfODUkPositionSeqPointer_Type = RowPointer
_JnxoptIfODUkPositionSeqPointer_Object = MibTableColumn
jnxoptIfODUkPositionSeqPointer = _JnxoptIfODUkPositionSeqPointer_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 8, 3, 1, 3),
    _JnxoptIfODUkPositionSeqPointer_Type()
)
jnxoptIfODUkPositionSeqPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfODUkPositionSeqPointer.setStatus("current")
_JnxoptIfODUkNimConfigTable_Object = MibTable
jnxoptIfODUkNimConfigTable = _JnxoptIfODUkNimConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 8, 4)
)
if mibBuilder.loadTexts:
    jnxoptIfODUkNimConfigTable.setStatus("current")
_JnxoptIfODUkNimConfigEntry_Object = MibTableRow
jnxoptIfODUkNimConfigEntry = _JnxoptIfODUkNimConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 8, 4, 1)
)
jnxoptIfODUkNimConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "JNX-OPT-IF-MIB", "jnxoptIfODUkNimDirectionality"),
)
if mibBuilder.loadTexts:
    jnxoptIfODUkNimConfigEntry.setStatus("current")
_JnxoptIfODUkNimDirectionality_Type = JnxoptIfSinkOrSource
_JnxoptIfODUkNimDirectionality_Object = MibTableColumn
jnxoptIfODUkNimDirectionality = _JnxoptIfODUkNimDirectionality_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 8, 4, 1, 1),
    _JnxoptIfODUkNimDirectionality_Type()
)
jnxoptIfODUkNimDirectionality.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxoptIfODUkNimDirectionality.setStatus("current")
_JnxoptIfODUkNimDAPIExpected_Type = JnxoptIfExDAPI
_JnxoptIfODUkNimDAPIExpected_Object = MibTableColumn
jnxoptIfODUkNimDAPIExpected = _JnxoptIfODUkNimDAPIExpected_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 8, 4, 1, 2),
    _JnxoptIfODUkNimDAPIExpected_Type()
)
jnxoptIfODUkNimDAPIExpected.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxoptIfODUkNimDAPIExpected.setStatus("current")
_JnxoptIfODUkNimSAPIExpected_Type = JnxoptIfExSAPI
_JnxoptIfODUkNimSAPIExpected_Object = MibTableColumn
jnxoptIfODUkNimSAPIExpected = _JnxoptIfODUkNimSAPIExpected_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 8, 4, 1, 3),
    _JnxoptIfODUkNimSAPIExpected_Type()
)
jnxoptIfODUkNimSAPIExpected.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxoptIfODUkNimSAPIExpected.setStatus("current")
_JnxoptIfODUkNimTraceIdentifierAccepted_Type = JnxoptIfAcTI
_JnxoptIfODUkNimTraceIdentifierAccepted_Object = MibTableColumn
jnxoptIfODUkNimTraceIdentifierAccepted = _JnxoptIfODUkNimTraceIdentifierAccepted_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 8, 4, 1, 4),
    _JnxoptIfODUkNimTraceIdentifierAccepted_Type()
)
jnxoptIfODUkNimTraceIdentifierAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfODUkNimTraceIdentifierAccepted.setStatus("current")
_JnxoptIfODUkNimTIMDetMode_Type = JnxoptIfTIMDetMode
_JnxoptIfODUkNimTIMDetMode_Object = MibTableColumn
jnxoptIfODUkNimTIMDetMode = _JnxoptIfODUkNimTIMDetMode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 8, 4, 1, 5),
    _JnxoptIfODUkNimTIMDetMode_Type()
)
jnxoptIfODUkNimTIMDetMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxoptIfODUkNimTIMDetMode.setStatus("current")
_JnxoptIfODUkNimTIMActEnabled_Type = TruthValue
_JnxoptIfODUkNimTIMActEnabled_Object = MibTableColumn
jnxoptIfODUkNimTIMActEnabled = _JnxoptIfODUkNimTIMActEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 8, 4, 1, 6),
    _JnxoptIfODUkNimTIMActEnabled_Type()
)
jnxoptIfODUkNimTIMActEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxoptIfODUkNimTIMActEnabled.setStatus("current")
_JnxoptIfODUkNimDEGThr_Type = JnxoptIfDEGThr
_JnxoptIfODUkNimDEGThr_Object = MibTableColumn
jnxoptIfODUkNimDEGThr = _JnxoptIfODUkNimDEGThr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 8, 4, 1, 7),
    _JnxoptIfODUkNimDEGThr_Type()
)
jnxoptIfODUkNimDEGThr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxoptIfODUkNimDEGThr.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfODUkNimDEGThr.setUnits("percentage")
_JnxoptIfODUkNimDEGM_Type = JnxoptIfDEGM
_JnxoptIfODUkNimDEGM_Object = MibTableColumn
jnxoptIfODUkNimDEGM = _JnxoptIfODUkNimDEGM_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 8, 4, 1, 8),
    _JnxoptIfODUkNimDEGM_Type()
)
jnxoptIfODUkNimDEGM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxoptIfODUkNimDEGM.setStatus("current")


class _JnxoptIfODUkNimCurrentStatus_Type(Bits):
    """Custom type jnxoptIfODUkNimCurrentStatus based on Bits"""
    namedValues = NamedValues(
        *(("bdi", 4),
          ("deg", 3),
          ("lck", 1),
          ("oci", 0),
          ("ssf", 5),
          ("tim", 2))
    )

_JnxoptIfODUkNimCurrentStatus_Type.__name__ = "Bits"
_JnxoptIfODUkNimCurrentStatus_Object = MibTableColumn
jnxoptIfODUkNimCurrentStatus = _JnxoptIfODUkNimCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 8, 4, 1, 9),
    _JnxoptIfODUkNimCurrentStatus_Type()
)
jnxoptIfODUkNimCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfODUkNimCurrentStatus.setStatus("current")
_JnxoptIfODUkNimRowStatus_Type = RowStatus
_JnxoptIfODUkNimRowStatus_Object = MibTableColumn
jnxoptIfODUkNimRowStatus = _JnxoptIfODUkNimRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 8, 4, 1, 10),
    _JnxoptIfODUkNimRowStatus_Type()
)
jnxoptIfODUkNimRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxoptIfODUkNimRowStatus.setStatus("current")
_JnxoptIfGCC12ConfigTable_Object = MibTable
jnxoptIfGCC12ConfigTable = _JnxoptIfGCC12ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 8, 5)
)
if mibBuilder.loadTexts:
    jnxoptIfGCC12ConfigTable.setStatus("current")
_JnxoptIfGCC12ConfigEntry_Object = MibTableRow
jnxoptIfGCC12ConfigEntry = _JnxoptIfGCC12ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 8, 5, 1)
)
jnxoptIfGCC12ConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "JNX-OPT-IF-MIB", "jnxoptIfGCC12Codirectional"),
    (0, "JNX-OPT-IF-MIB", "jnxoptIfGCC12GCCAccess"),
)
if mibBuilder.loadTexts:
    jnxoptIfGCC12ConfigEntry.setStatus("current")
_JnxoptIfGCC12Codirectional_Type = TruthValue
_JnxoptIfGCC12Codirectional_Object = MibTableColumn
jnxoptIfGCC12Codirectional = _JnxoptIfGCC12Codirectional_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 8, 5, 1, 1),
    _JnxoptIfGCC12Codirectional_Type()
)
jnxoptIfGCC12Codirectional.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxoptIfGCC12Codirectional.setStatus("current")


class _JnxoptIfGCC12GCCAccess_Type(Integer32):
    """Custom type jnxoptIfGCC12GCCAccess based on Integer32"""
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


_JnxoptIfGCC12GCCAccess_Type.__name__ = "Integer32"
_JnxoptIfGCC12GCCAccess_Object = MibTableColumn
jnxoptIfGCC12GCCAccess = _JnxoptIfGCC12GCCAccess_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 8, 5, 1, 2),
    _JnxoptIfGCC12GCCAccess_Type()
)
jnxoptIfGCC12GCCAccess.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxoptIfGCC12GCCAccess.setStatus("current")
_JnxoptIfGCC12GCCPassThrough_Type = TruthValue
_JnxoptIfGCC12GCCPassThrough_Object = MibTableColumn
jnxoptIfGCC12GCCPassThrough = _JnxoptIfGCC12GCCPassThrough_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 8, 5, 1, 3),
    _JnxoptIfGCC12GCCPassThrough_Type()
)
jnxoptIfGCC12GCCPassThrough.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxoptIfGCC12GCCPassThrough.setStatus("current")
_JnxoptIfGCC12Application_Type = SnmpAdminString
_JnxoptIfGCC12Application_Object = MibTableColumn
jnxoptIfGCC12Application = _JnxoptIfGCC12Application_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 8, 5, 1, 4),
    _JnxoptIfGCC12Application_Type()
)
jnxoptIfGCC12Application.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxoptIfGCC12Application.setStatus("current")
_JnxoptIfGCC12RowStatus_Type = RowStatus
_JnxoptIfGCC12RowStatus_Object = MibTableColumn
jnxoptIfGCC12RowStatus = _JnxoptIfGCC12RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 8, 5, 1, 5),
    _JnxoptIfGCC12RowStatus_Type()
)
jnxoptIfGCC12RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxoptIfGCC12RowStatus.setStatus("current")
_JnxoptIfODUkT_ObjectIdentity = ObjectIdentity
jnxoptIfODUkT = _JnxoptIfODUkT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 9)
)
_JnxoptIfODUkTConfigTable_Object = MibTable
jnxoptIfODUkTConfigTable = _JnxoptIfODUkTConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 9, 1)
)
if mibBuilder.loadTexts:
    jnxoptIfODUkTConfigTable.setStatus("current")
_JnxoptIfODUkTConfigEntry_Object = MibTableRow
jnxoptIfODUkTConfigEntry = _JnxoptIfODUkTConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 9, 1, 1)
)
jnxoptIfODUkTConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "JNX-OPT-IF-MIB", "jnxoptIfODUkTTcmField"),
    (0, "JNX-OPT-IF-MIB", "jnxoptIfODUkTCodirectional"),
)
if mibBuilder.loadTexts:
    jnxoptIfODUkTConfigEntry.setStatus("current")


class _JnxoptIfODUkTTcmField_Type(Unsigned32):
    """Custom type jnxoptIfODUkTTcmField based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_JnxoptIfODUkTTcmField_Type.__name__ = "Unsigned32"
_JnxoptIfODUkTTcmField_Object = MibTableColumn
jnxoptIfODUkTTcmField = _JnxoptIfODUkTTcmField_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 9, 1, 1, 1),
    _JnxoptIfODUkTTcmField_Type()
)
jnxoptIfODUkTTcmField.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxoptIfODUkTTcmField.setStatus("current")
_JnxoptIfODUkTCodirectional_Type = TruthValue
_JnxoptIfODUkTCodirectional_Object = MibTableColumn
jnxoptIfODUkTCodirectional = _JnxoptIfODUkTCodirectional_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 9, 1, 1, 2),
    _JnxoptIfODUkTCodirectional_Type()
)
jnxoptIfODUkTCodirectional.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxoptIfODUkTCodirectional.setStatus("current")
_JnxoptIfODUkTTraceIdentifierTransmitted_Type = JnxoptIfTxTI
_JnxoptIfODUkTTraceIdentifierTransmitted_Object = MibTableColumn
jnxoptIfODUkTTraceIdentifierTransmitted = _JnxoptIfODUkTTraceIdentifierTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 9, 1, 1, 3),
    _JnxoptIfODUkTTraceIdentifierTransmitted_Type()
)
jnxoptIfODUkTTraceIdentifierTransmitted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxoptIfODUkTTraceIdentifierTransmitted.setStatus("current")
_JnxoptIfODUkTDAPIExpected_Type = JnxoptIfExDAPI
_JnxoptIfODUkTDAPIExpected_Object = MibTableColumn
jnxoptIfODUkTDAPIExpected = _JnxoptIfODUkTDAPIExpected_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 9, 1, 1, 4),
    _JnxoptIfODUkTDAPIExpected_Type()
)
jnxoptIfODUkTDAPIExpected.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxoptIfODUkTDAPIExpected.setStatus("current")
_JnxoptIfODUkTSAPIExpected_Type = JnxoptIfExSAPI
_JnxoptIfODUkTSAPIExpected_Object = MibTableColumn
jnxoptIfODUkTSAPIExpected = _JnxoptIfODUkTSAPIExpected_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 9, 1, 1, 5),
    _JnxoptIfODUkTSAPIExpected_Type()
)
jnxoptIfODUkTSAPIExpected.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxoptIfODUkTSAPIExpected.setStatus("current")
_JnxoptIfODUkTTraceIdentifierAccepted_Type = JnxoptIfAcTI
_JnxoptIfODUkTTraceIdentifierAccepted_Object = MibTableColumn
jnxoptIfODUkTTraceIdentifierAccepted = _JnxoptIfODUkTTraceIdentifierAccepted_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 9, 1, 1, 6),
    _JnxoptIfODUkTTraceIdentifierAccepted_Type()
)
jnxoptIfODUkTTraceIdentifierAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfODUkTTraceIdentifierAccepted.setStatus("current")
_JnxoptIfODUkTTIMDetMode_Type = JnxoptIfTIMDetMode
_JnxoptIfODUkTTIMDetMode_Object = MibTableColumn
jnxoptIfODUkTTIMDetMode = _JnxoptIfODUkTTIMDetMode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 9, 1, 1, 7),
    _JnxoptIfODUkTTIMDetMode_Type()
)
jnxoptIfODUkTTIMDetMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxoptIfODUkTTIMDetMode.setStatus("current")
_JnxoptIfODUkTTIMActEnabled_Type = TruthValue
_JnxoptIfODUkTTIMActEnabled_Object = MibTableColumn
jnxoptIfODUkTTIMActEnabled = _JnxoptIfODUkTTIMActEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 9, 1, 1, 8),
    _JnxoptIfODUkTTIMActEnabled_Type()
)
jnxoptIfODUkTTIMActEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxoptIfODUkTTIMActEnabled.setStatus("current")
_JnxoptIfODUkTDEGThr_Type = JnxoptIfDEGThr
_JnxoptIfODUkTDEGThr_Object = MibTableColumn
jnxoptIfODUkTDEGThr = _JnxoptIfODUkTDEGThr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 9, 1, 1, 9),
    _JnxoptIfODUkTDEGThr_Type()
)
jnxoptIfODUkTDEGThr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxoptIfODUkTDEGThr.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfODUkTDEGThr.setUnits("percentage")
_JnxoptIfODUkTDEGM_Type = JnxoptIfDEGM
_JnxoptIfODUkTDEGM_Object = MibTableColumn
jnxoptIfODUkTDEGM = _JnxoptIfODUkTDEGM_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 9, 1, 1, 10),
    _JnxoptIfODUkTDEGM_Type()
)
jnxoptIfODUkTDEGM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxoptIfODUkTDEGM.setStatus("current")


class _JnxoptIfODUkTSinkMode_Type(Integer32):
    """Custom type jnxoptIfODUkTSinkMode based on Integer32"""
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


_JnxoptIfODUkTSinkMode_Type.__name__ = "Integer32"
_JnxoptIfODUkTSinkMode_Object = MibTableColumn
jnxoptIfODUkTSinkMode = _JnxoptIfODUkTSinkMode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 9, 1, 1, 11),
    _JnxoptIfODUkTSinkMode_Type()
)
jnxoptIfODUkTSinkMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxoptIfODUkTSinkMode.setStatus("current")


class _JnxoptIfODUkTSinkLockSignalAdminState_Type(Integer32):
    """Custom type jnxoptIfODUkTSinkLockSignalAdminState based on Integer32"""
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


_JnxoptIfODUkTSinkLockSignalAdminState_Type.__name__ = "Integer32"
_JnxoptIfODUkTSinkLockSignalAdminState_Object = MibTableColumn
jnxoptIfODUkTSinkLockSignalAdminState = _JnxoptIfODUkTSinkLockSignalAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 9, 1, 1, 12),
    _JnxoptIfODUkTSinkLockSignalAdminState_Type()
)
jnxoptIfODUkTSinkLockSignalAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxoptIfODUkTSinkLockSignalAdminState.setStatus("current")


class _JnxoptIfODUkTSourceLockSignalAdminState_Type(Integer32):
    """Custom type jnxoptIfODUkTSourceLockSignalAdminState based on Integer32"""
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


_JnxoptIfODUkTSourceLockSignalAdminState_Type.__name__ = "Integer32"
_JnxoptIfODUkTSourceLockSignalAdminState_Object = MibTableColumn
jnxoptIfODUkTSourceLockSignalAdminState = _JnxoptIfODUkTSourceLockSignalAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 9, 1, 1, 13),
    _JnxoptIfODUkTSourceLockSignalAdminState_Type()
)
jnxoptIfODUkTSourceLockSignalAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxoptIfODUkTSourceLockSignalAdminState.setStatus("current")


class _JnxoptIfODUkTCurrentStatus_Type(Bits):
    """Custom type jnxoptIfODUkTCurrentStatus based on Bits"""
    namedValues = NamedValues(
        *(("bdi", 4),
          ("deg", 3),
          ("lck", 1),
          ("oci", 0),
          ("ssf", 5),
          ("tim", 2))
    )

_JnxoptIfODUkTCurrentStatus_Type.__name__ = "Bits"
_JnxoptIfODUkTCurrentStatus_Object = MibTableColumn
jnxoptIfODUkTCurrentStatus = _JnxoptIfODUkTCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 9, 1, 1, 14),
    _JnxoptIfODUkTCurrentStatus_Type()
)
jnxoptIfODUkTCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfODUkTCurrentStatus.setStatus("current")
_JnxoptIfODUkTRowStatus_Type = RowStatus
_JnxoptIfODUkTRowStatus_Object = MibTableColumn
jnxoptIfODUkTRowStatus = _JnxoptIfODUkTRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 9, 1, 1, 15),
    _JnxoptIfODUkTRowStatus_Type()
)
jnxoptIfODUkTRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxoptIfODUkTRowStatus.setStatus("current")
_JnxoptIfODUkTNimConfigTable_Object = MibTable
jnxoptIfODUkTNimConfigTable = _JnxoptIfODUkTNimConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 9, 2)
)
if mibBuilder.loadTexts:
    jnxoptIfODUkTNimConfigTable.setStatus("current")
_JnxoptIfODUkTNimConfigEntry_Object = MibTableRow
jnxoptIfODUkTNimConfigEntry = _JnxoptIfODUkTNimConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 9, 2, 1)
)
jnxoptIfODUkTNimConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "JNX-OPT-IF-MIB", "jnxoptIfODUkTNimTcmField"),
    (0, "JNX-OPT-IF-MIB", "jnxoptIfODUkTNimDirectionality"),
)
if mibBuilder.loadTexts:
    jnxoptIfODUkTNimConfigEntry.setStatus("current")


class _JnxoptIfODUkTNimTcmField_Type(Unsigned32):
    """Custom type jnxoptIfODUkTNimTcmField based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_JnxoptIfODUkTNimTcmField_Type.__name__ = "Unsigned32"
_JnxoptIfODUkTNimTcmField_Object = MibTableColumn
jnxoptIfODUkTNimTcmField = _JnxoptIfODUkTNimTcmField_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 9, 2, 1, 1),
    _JnxoptIfODUkTNimTcmField_Type()
)
jnxoptIfODUkTNimTcmField.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxoptIfODUkTNimTcmField.setStatus("current")
_JnxoptIfODUkTNimDirectionality_Type = JnxoptIfSinkOrSource
_JnxoptIfODUkTNimDirectionality_Object = MibTableColumn
jnxoptIfODUkTNimDirectionality = _JnxoptIfODUkTNimDirectionality_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 9, 2, 1, 2),
    _JnxoptIfODUkTNimDirectionality_Type()
)
jnxoptIfODUkTNimDirectionality.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxoptIfODUkTNimDirectionality.setStatus("current")
_JnxoptIfODUkTNimDAPIExpected_Type = JnxoptIfExDAPI
_JnxoptIfODUkTNimDAPIExpected_Object = MibTableColumn
jnxoptIfODUkTNimDAPIExpected = _JnxoptIfODUkTNimDAPIExpected_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 9, 2, 1, 3),
    _JnxoptIfODUkTNimDAPIExpected_Type()
)
jnxoptIfODUkTNimDAPIExpected.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxoptIfODUkTNimDAPIExpected.setStatus("current")
_JnxoptIfODUkTNimSAPIExpected_Type = JnxoptIfExSAPI
_JnxoptIfODUkTNimSAPIExpected_Object = MibTableColumn
jnxoptIfODUkTNimSAPIExpected = _JnxoptIfODUkTNimSAPIExpected_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 9, 2, 1, 4),
    _JnxoptIfODUkTNimSAPIExpected_Type()
)
jnxoptIfODUkTNimSAPIExpected.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxoptIfODUkTNimSAPIExpected.setStatus("current")
_JnxoptIfODUkTNimTraceIdentifierAccepted_Type = JnxoptIfAcTI
_JnxoptIfODUkTNimTraceIdentifierAccepted_Object = MibTableColumn
jnxoptIfODUkTNimTraceIdentifierAccepted = _JnxoptIfODUkTNimTraceIdentifierAccepted_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 9, 2, 1, 5),
    _JnxoptIfODUkTNimTraceIdentifierAccepted_Type()
)
jnxoptIfODUkTNimTraceIdentifierAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfODUkTNimTraceIdentifierAccepted.setStatus("current")
_JnxoptIfODUkTNimTIMDetMode_Type = JnxoptIfTIMDetMode
_JnxoptIfODUkTNimTIMDetMode_Object = MibTableColumn
jnxoptIfODUkTNimTIMDetMode = _JnxoptIfODUkTNimTIMDetMode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 9, 2, 1, 6),
    _JnxoptIfODUkTNimTIMDetMode_Type()
)
jnxoptIfODUkTNimTIMDetMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxoptIfODUkTNimTIMDetMode.setStatus("current")
_JnxoptIfODUkTNimTIMActEnabled_Type = TruthValue
_JnxoptIfODUkTNimTIMActEnabled_Object = MibTableColumn
jnxoptIfODUkTNimTIMActEnabled = _JnxoptIfODUkTNimTIMActEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 9, 2, 1, 7),
    _JnxoptIfODUkTNimTIMActEnabled_Type()
)
jnxoptIfODUkTNimTIMActEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxoptIfODUkTNimTIMActEnabled.setStatus("current")
_JnxoptIfODUkTNimDEGThr_Type = JnxoptIfDEGThr
_JnxoptIfODUkTNimDEGThr_Object = MibTableColumn
jnxoptIfODUkTNimDEGThr = _JnxoptIfODUkTNimDEGThr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 9, 2, 1, 8),
    _JnxoptIfODUkTNimDEGThr_Type()
)
jnxoptIfODUkTNimDEGThr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxoptIfODUkTNimDEGThr.setStatus("current")
if mibBuilder.loadTexts:
    jnxoptIfODUkTNimDEGThr.setUnits("percentage")
_JnxoptIfODUkTNimDEGM_Type = JnxoptIfDEGM
_JnxoptIfODUkTNimDEGM_Object = MibTableColumn
jnxoptIfODUkTNimDEGM = _JnxoptIfODUkTNimDEGM_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 9, 2, 1, 9),
    _JnxoptIfODUkTNimDEGM_Type()
)
jnxoptIfODUkTNimDEGM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxoptIfODUkTNimDEGM.setStatus("current")


class _JnxoptIfODUkTNimCurrentStatus_Type(Bits):
    """Custom type jnxoptIfODUkTNimCurrentStatus based on Bits"""
    namedValues = NamedValues(
        *(("bdi", 4),
          ("deg", 3),
          ("lck", 1),
          ("oci", 0),
          ("ssf", 5),
          ("tim", 2))
    )

_JnxoptIfODUkTNimCurrentStatus_Type.__name__ = "Bits"
_JnxoptIfODUkTNimCurrentStatus_Object = MibTableColumn
jnxoptIfODUkTNimCurrentStatus = _JnxoptIfODUkTNimCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 9, 2, 1, 10),
    _JnxoptIfODUkTNimCurrentStatus_Type()
)
jnxoptIfODUkTNimCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxoptIfODUkTNimCurrentStatus.setStatus("current")
_JnxoptIfODUkTNimRowStatus_Type = RowStatus
_JnxoptIfODUkTNimRowStatus_Object = MibTableColumn
jnxoptIfODUkTNimRowStatus = _JnxoptIfODUkTNimRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 1, 9, 2, 1, 11),
    _JnxoptIfODUkTNimRowStatus_Type()
)
jnxoptIfODUkTNimRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxoptIfODUkTNimRowStatus.setStatus("current")
_JnxoptIfConfs_ObjectIdentity = ObjectIdentity
jnxoptIfConfs = _JnxoptIfConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 2)
)
_JnxoptIfGroups_ObjectIdentity = ObjectIdentity
jnxoptIfGroups = _JnxoptIfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 2, 1)
)
_JnxoptIfCompl_ObjectIdentity = ObjectIdentity
jnxoptIfCompl = _JnxoptIfCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 2, 2)
)

# Managed Objects groups

jnxoptIfOTMnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 2, 1, 1)
)
jnxoptIfOTMnGroup.setObjects(
      *(("JNX-OPT-IF-MIB", "jnxoptIfOTMnOrder"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTMnReduced"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTMnBitRates"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTMnInterfaceType"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTMnTcmMax"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTMnOpticalReach"))
)
if mibBuilder.loadTexts:
    jnxoptIfOTMnGroup.setStatus("current")

jnxoptIfPerfMonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 2, 1, 2)
)
jnxoptIfPerfMonGroup.setObjects(
      *(("JNX-OPT-IF-MIB", "jnxoptIfPerfMonCurrentTimeElapsed"),
        ("JNX-OPT-IF-MIB", "jnxoptIfPerfMonCurDayTimeElapsed"),
        ("JNX-OPT-IF-MIB", "jnxoptIfPerfMonIntervalNumIntervals"),
        ("JNX-OPT-IF-MIB", "jnxoptIfPerfMonIntervalNumInvalidIntervals"))
)
if mibBuilder.loadTexts:
    jnxoptIfPerfMonGroup.setStatus("current")

jnxoptIfOTSnCommonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 2, 1, 3)
)
jnxoptIfOTSnCommonGroup.setObjects(
    ("JNX-OPT-IF-MIB", "jnxoptIfOTSnDirectionality")
)
if mibBuilder.loadTexts:
    jnxoptIfOTSnCommonGroup.setStatus("current")

jnxoptIfOTSnSourceGroupFull = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 2, 1, 4)
)
jnxoptIfOTSnSourceGroupFull.setObjects(
    ("JNX-OPT-IF-MIB", "jnxoptIfOTSnTraceIdentifierTransmitted")
)
if mibBuilder.loadTexts:
    jnxoptIfOTSnSourceGroupFull.setStatus("current")

jnxoptIfOTSnAPRStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 2, 1, 5)
)
jnxoptIfOTSnAPRStatusGroup.setObjects(
    ("JNX-OPT-IF-MIB", "jnxoptIfOTSnAprStatus")
)
if mibBuilder.loadTexts:
    jnxoptIfOTSnAPRStatusGroup.setStatus("current")

jnxoptIfOTSnAPRControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 2, 1, 6)
)
jnxoptIfOTSnAPRControlGroup.setObjects(
    ("JNX-OPT-IF-MIB", "jnxoptIfOTSnAprControl")
)
if mibBuilder.loadTexts:
    jnxoptIfOTSnAPRControlGroup.setStatus("current")

jnxoptIfOTSnSinkGroupBasic = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 2, 1, 7)
)
jnxoptIfOTSnSinkGroupBasic.setObjects(
    ("JNX-OPT-IF-MIB", "jnxoptIfOTSnCurrentStatus")
)
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkGroupBasic.setStatus("current")

jnxoptIfOTSnSinkGroupFull = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 2, 1, 8)
)
jnxoptIfOTSnSinkGroupFull.setObjects(
      *(("JNX-OPT-IF-MIB", "jnxoptIfOTSnDAPIExpected"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSAPIExpected"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnTraceIdentifierAccepted"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnTIMDetMode"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnTIMActEnabled"))
)
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkGroupFull.setStatus("current")

jnxoptIfOTSnSinkPreOtnPMGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 2, 1, 9)
)
jnxoptIfOTSnSinkPreOtnPMGroup.setObjects(
      *(("JNX-OPT-IF-MIB", "jnxoptIfOTSnSinkCurrentSuspectedFlag"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSinkCurrentInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSinkCurrentLowInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSinkCurrentHighInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSinkCurrentOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSinkCurrentLowOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSinkCurrentHighOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSinkIntervalSuspectedFlag"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSinkIntervalLastInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSinkIntervalLowInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSinkIntervalHighInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSinkIntervalLastOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSinkIntervalLowOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSinkIntervalHighOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSinkCurDaySuspectedFlag"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSinkCurDayLowInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSinkCurDayHighInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSinkCurDayLowOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSinkCurDayHighOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSinkPrevDaySuspectedFlag"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSinkPrevDayLastInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSinkPrevDayLowInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSinkPrevDayHighInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSinkPrevDayLastOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSinkPrevDayLowOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSinkPrevDayHighOutputPower"))
)
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkPreOtnPMGroup.setStatus("current")

jnxoptIfOTSnSinkPreOtnPMThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 2, 1, 10)
)
jnxoptIfOTSnSinkPreOtnPMThresholdGroup.setObjects(
      *(("JNX-OPT-IF-MIB", "jnxoptIfOTSnSinkCurrentLowerInputPowerThreshold"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSinkCurrentUpperInputPowerThreshold"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSinkCurrentLowerOutputPowerThreshold"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSinkCurrentUpperOutputPowerThreshold"))
)
if mibBuilder.loadTexts:
    jnxoptIfOTSnSinkPreOtnPMThresholdGroup.setStatus("current")

jnxoptIfOTSnSourcePreOtnPMGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 2, 1, 11)
)
jnxoptIfOTSnSourcePreOtnPMGroup.setObjects(
      *(("JNX-OPT-IF-MIB", "jnxoptIfOTSnSrcCurrentSuspectedFlag"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSrcCurrentOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSrcCurrentLowOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSrcCurrentHighOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSrcCurrentInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSrcCurrentLowInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSrcCurrentHighInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSrcIntervalSuspectedFlag"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSrcIntervalLastOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSrcIntervalLowOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSrcIntervalHighOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSrcIntervalLastInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSrcIntervalLowInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSrcIntervalHighInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSrcCurDaySuspectedFlag"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSrcCurDayLowOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSrcCurDayHighOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSrcCurDayLowInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSrcCurDayHighInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSrcPrevDaySuspectedFlag"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSrcPrevDayLastOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSrcPrevDayLowOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSrcPrevDayHighOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSrcPrevDayLastInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSrcPrevDayLowInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSrcPrevDayHighInputPower"))
)
if mibBuilder.loadTexts:
    jnxoptIfOTSnSourcePreOtnPMGroup.setStatus("current")

jnxoptIfOTSnSourcePreOtnPMThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 2, 1, 12)
)
jnxoptIfOTSnSourcePreOtnPMThresholdGroup.setObjects(
      *(("JNX-OPT-IF-MIB", "jnxoptIfOTSnSrcCurrentLowerOutputPowerThreshold"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSrcCurrentUpperOutputPowerThreshold"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSrcCurrentLowerInputPowerThreshold"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTSnSrcCurrentUpperInputPowerThreshold"))
)
if mibBuilder.loadTexts:
    jnxoptIfOTSnSourcePreOtnPMThresholdGroup.setStatus("current")

jnxoptIfOMSnCommonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 2, 1, 13)
)
jnxoptIfOMSnCommonGroup.setObjects(
    ("JNX-OPT-IF-MIB", "jnxoptIfOMSnDirectionality")
)
if mibBuilder.loadTexts:
    jnxoptIfOMSnCommonGroup.setStatus("current")

jnxoptIfOMSnSinkGroupBasic = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 2, 1, 14)
)
jnxoptIfOMSnSinkGroupBasic.setObjects(
    ("JNX-OPT-IF-MIB", "jnxoptIfOMSnCurrentStatus")
)
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkGroupBasic.setStatus("current")

jnxoptIfOMSnSinkPreOtnPMGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 2, 1, 15)
)
jnxoptIfOMSnSinkPreOtnPMGroup.setObjects(
      *(("JNX-OPT-IF-MIB", "jnxoptIfOMSnSinkCurrentSuspectedFlag"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSinkCurrentAggregatedInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSinkCurrentLowAggregatedInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSinkCurrentHighAggregatedInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSinkCurrentOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSinkCurrentLowOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSinkCurrentHighOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSinkIntervalSuspectedFlag"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSinkIntervalLastAggregatedInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSinkIntervalLowAggregatedInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSinkIntervalHighAggregatedInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSinkIntervalLastOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSinkIntervalLowOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSinkIntervalHighOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSinkCurDaySuspectedFlag"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSinkCurDayLowAggregatedInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSinkCurDayHighAggregatedInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSinkCurDayLowOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSinkCurDayHighOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSinkPrevDaySuspectedFlag"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSinkPrevDayLastAggregatedInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSinkPrevDayLowAggregatedInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSinkPrevDayHighAggregatedInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSinkPrevDayLastOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSinkPrevDayLowOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSinkPrevDayHighOutputPower"))
)
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkPreOtnPMGroup.setStatus("current")

jnxoptIfOMSnSinkPreOtnPMThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 2, 1, 16)
)
jnxoptIfOMSnSinkPreOtnPMThresholdGroup.setObjects(
      *(("JNX-OPT-IF-MIB", "jnxoptIfOMSnSinkCurrentLowerInputPowerThreshold"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSinkCurrentUpperInputPowerThreshold"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSinkCurrentLowerOutputPowerThreshold"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSinkCurrentUpperOutputPowerThreshold"))
)
if mibBuilder.loadTexts:
    jnxoptIfOMSnSinkPreOtnPMThresholdGroup.setStatus("current")

jnxoptIfOMSnSourcePreOtnPMGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 2, 1, 17)
)
jnxoptIfOMSnSourcePreOtnPMGroup.setObjects(
      *(("JNX-OPT-IF-MIB", "jnxoptIfOMSnSrcCurrentSuspectedFlag"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSrcCurrentOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSrcCurrentLowOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSrcCurrentHighOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSrcCurrentAggregatedInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSrcCurrentLowAggregatedInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSrcCurrentHighAggregatedInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSrcIntervalSuspectedFlag"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSrcIntervalLastOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSrcIntervalLowOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSrcIntervalHighOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSrcIntervalLastAggregatedInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSrcIntervalLowAggregatedInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSrcIntervalHighAggregatedInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSrcCurDaySuspectedFlag"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSrcCurDayLowOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSrcCurDayHighOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSrcCurDayLowAggregatedInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSrcCurDayHighAggregatedInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSrcPrevDaySuspectedFlag"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSrcPrevDayLastOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSrcPrevDayLowOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSrcPrevDayHighOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSrcPrevDayLastAggregatedInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSrcPrevDayLowAggregatedInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSrcPrevDayHighAggregatedInputPower"))
)
if mibBuilder.loadTexts:
    jnxoptIfOMSnSourcePreOtnPMGroup.setStatus("current")

jnxoptIfOMSnSourcePreOtnPMThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 2, 1, 18)
)
jnxoptIfOMSnSourcePreOtnPMThresholdGroup.setObjects(
      *(("JNX-OPT-IF-MIB", "jnxoptIfOMSnSrcCurrentLowerOutputPowerThreshold"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSrcCurrentUpperOutputPowerThreshold"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSrcCurrentLowerInputPowerThreshold"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOMSnSrcCurrentUpperInputPowerThreshold"))
)
if mibBuilder.loadTexts:
    jnxoptIfOMSnSourcePreOtnPMThresholdGroup.setStatus("current")

jnxoptIfOChGroupCommonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 2, 1, 19)
)
jnxoptIfOChGroupCommonGroup.setObjects(
    ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupDirectionality")
)
if mibBuilder.loadTexts:
    jnxoptIfOChGroupCommonGroup.setStatus("current")

jnxoptIfOChGroupSinkPreOtnPMGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 2, 1, 20)
)
jnxoptIfOChGroupSinkPreOtnPMGroup.setObjects(
      *(("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSinkCurrentSuspectedFlag"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSinkCurrentAggregatedInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSinkCurrentLowAggregatedInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSinkCurrentHighAggregatedInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSinkCurrentOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSinkCurrentLowOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSinkCurrentHighOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSinkIntervalSuspectedFlag"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSinkIntervalLastAggregatedInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSinkIntervalLowAggregatedInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSinkIntervalHighAggregatedInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSinkIntervalLastOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSinkIntervalLowOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSinkIntervalHighOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSinkCurDaySuspectedFlag"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSinkCurDayLowAggregatedInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSinkCurDayHighAggregatedInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSinkCurDayLowOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSinkCurDayHighOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSinkPrevDaySuspectedFlag"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSinkPrevDayLastAggregatedInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSinkPrevDayLowAggregatedInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSinkPrevDayHighAggregatedInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSinkPrevDayLastOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSinkPrevDayLowOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSinkPrevDayHighOutputPower"))
)
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkPreOtnPMGroup.setStatus("current")

jnxoptIfOChGroupSinkPreOtnPMThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 2, 1, 21)
)
jnxoptIfOChGroupSinkPreOtnPMThresholdGroup.setObjects(
      *(("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSinkCurrentLowerInputPowerThreshold"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSinkCurrentUpperInputPowerThreshold"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSinkCurrentLowerOutputPowerThreshold"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSinkCurrentUpperOutputPowerThreshold"))
)
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSinkPreOtnPMThresholdGroup.setStatus("current")

jnxoptIfOChGroupSourcePreOtnPMGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 2, 1, 22)
)
jnxoptIfOChGroupSourcePreOtnPMGroup.setObjects(
      *(("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSrcCurrentSuspectedFlag"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSrcCurrentOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSrcCurrentLowOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSrcCurrentHighOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSrcCurrentAggregatedInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSrcCurrentLowAggregatedInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSrcCurrentHighAggregatedInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSrcIntervalSuspectedFlag"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSrcIntervalLastOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSrcIntervalLowOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSrcIntervalHighOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSrcIntervalLastAggregatedInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSrcIntervalLowAggregatedInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSrcIntervalHighAggregatedInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSrcCurDaySuspectedFlag"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSrcCurDayLowOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSrcCurDayHighOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSrcCurDayLowAggregatedInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSrcCurDayHighAggregatedInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSrcPrevDaySuspectedFlag"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSrcPrevDayLastOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSrcPrevDayLowOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSrcPrevDayHighOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSrcPrevDayLastAggregatedInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSrcPrevDayLowAggregatedInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSrcPrevDayHighAggregatedInputPower"))
)
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSourcePreOtnPMGroup.setStatus("current")

jnxoptIfOChGroupSourcePreOtnPMThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 2, 1, 23)
)
jnxoptIfOChGroupSourcePreOtnPMThresholdGroup.setObjects(
      *(("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSrcCurrentLowerOutputPowerThreshold"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSrcCurrentUpperOutputPowerThreshold"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSrcCurrentLowerInputPowerThreshold"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChGroupSrcCurrentUpperInputPowerThreshold"))
)
if mibBuilder.loadTexts:
    jnxoptIfOChGroupSourcePreOtnPMThresholdGroup.setStatus("current")

jnxoptIfOChCommonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 2, 1, 24)
)
jnxoptIfOChCommonGroup.setObjects(
    ("JNX-OPT-IF-MIB", "jnxoptIfOChDirectionality")
)
if mibBuilder.loadTexts:
    jnxoptIfOChCommonGroup.setStatus("current")

jnxoptIfOChSinkGroupBasic = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 2, 1, 25)
)
jnxoptIfOChSinkGroupBasic.setObjects(
    ("JNX-OPT-IF-MIB", "jnxoptIfOChCurrentStatus")
)
if mibBuilder.loadTexts:
    jnxoptIfOChSinkGroupBasic.setStatus("current")

jnxoptIfOChSinkPreOtnPMGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 2, 1, 26)
)
jnxoptIfOChSinkPreOtnPMGroup.setObjects(
      *(("JNX-OPT-IF-MIB", "jnxoptIfOChSinkCurrentSuspectedFlag"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChSinkCurrentInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChSinkCurrentLowInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChSinkCurrentHighInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChSinkIntervalSuspectedFlag"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChSinkIntervalLastInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChSinkIntervalLowInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChSinkIntervalHighInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChSinkCurDaySuspectedFlag"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChSinkCurDayLowInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChSinkCurDayHighInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChSinkPrevDaySuspectedFlag"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChSinkPrevDayLastInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChSinkPrevDayLowInputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChSinkPrevDayHighInputPower"))
)
if mibBuilder.loadTexts:
    jnxoptIfOChSinkPreOtnPMGroup.setStatus("current")

jnxoptIfOChSinkPreOtnPMThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 2, 1, 27)
)
jnxoptIfOChSinkPreOtnPMThresholdGroup.setObjects(
      *(("JNX-OPT-IF-MIB", "jnxoptIfOChSinkCurrentLowerInputPowerThreshold"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChSinkCurrentUpperInputPowerThreshold"))
)
if mibBuilder.loadTexts:
    jnxoptIfOChSinkPreOtnPMThresholdGroup.setStatus("current")

jnxoptIfOChSourcePreOtnPMGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 2, 1, 28)
)
jnxoptIfOChSourcePreOtnPMGroup.setObjects(
      *(("JNX-OPT-IF-MIB", "jnxoptIfOChSrcCurrentSuspectedFlag"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChSrcCurrentOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChSrcCurrentLowOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChSrcCurrentHighOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChSrcIntervalSuspectedFlag"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChSrcIntervalLastOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChSrcIntervalLowOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChSrcIntervalHighOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChSrcCurDaySuspectedFlag"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChSrcCurDayLowOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChSrcCurDayHighOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChSrcPrevDaySuspectedFlag"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChSrcPrevDayLastOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChSrcPrevDayLowOutputPower"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChSrcPrevDayHighOutputPower"))
)
if mibBuilder.loadTexts:
    jnxoptIfOChSourcePreOtnPMGroup.setStatus("current")

jnxoptIfOChSourcePreOtnPMThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 2, 1, 29)
)
jnxoptIfOChSourcePreOtnPMThresholdGroup.setObjects(
      *(("JNX-OPT-IF-MIB", "jnxoptIfOChSrcCurrentLowerOutputPowerThreshold"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOChSrcCurrentUpperOutputPowerThreshold"))
)
if mibBuilder.loadTexts:
    jnxoptIfOChSourcePreOtnPMThresholdGroup.setStatus("current")

jnxoptIfOTUkCommonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 2, 1, 30)
)
jnxoptIfOTUkCommonGroup.setObjects(
      *(("JNX-OPT-IF-MIB", "jnxoptIfOTUkDirectionality"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTUkBitRateK"))
)
if mibBuilder.loadTexts:
    jnxoptIfOTUkCommonGroup.setStatus("current")

jnxoptIfOTUkSourceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 2, 1, 31)
)
jnxoptIfOTUkSourceGroup.setObjects(
      *(("JNX-OPT-IF-MIB", "jnxoptIfOTUkTraceIdentifierTransmitted"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTUkSourceAdaptActive"))
)
if mibBuilder.loadTexts:
    jnxoptIfOTUkSourceGroup.setStatus("current")

jnxoptIfOTUkSinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 2, 1, 32)
)
jnxoptIfOTUkSinkGroup.setObjects(
      *(("JNX-OPT-IF-MIB", "jnxoptIfOTUkDAPIExpected"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTUkSAPIExpected"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTUkTraceIdentifierAccepted"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTUkTIMDetMode"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTUkTIMActEnabled"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTUkDEGThr"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTUkDEGM"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTUkSinkAdaptActive"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTUkSinkFECEnabled"),
        ("JNX-OPT-IF-MIB", "jnxoptIfOTUkCurrentStatus"))
)
if mibBuilder.loadTexts:
    jnxoptIfOTUkSinkGroup.setStatus("current")

jnxoptIfGCC0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 2, 1, 33)
)
jnxoptIfGCC0Group.setObjects(
      *(("JNX-OPT-IF-MIB", "jnxoptIfGCC0Application"),
        ("JNX-OPT-IF-MIB", "jnxoptIfGCC0RowStatus"))
)
if mibBuilder.loadTexts:
    jnxoptIfGCC0Group.setStatus("current")

jnxoptIfODUkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 2, 1, 34)
)
jnxoptIfODUkGroup.setObjects(
      *(("JNX-OPT-IF-MIB", "jnxoptIfODUkDirectionality"),
        ("JNX-OPT-IF-MIB", "jnxoptIfODUkBitRateK"),
        ("JNX-OPT-IF-MIB", "jnxoptIfODUkTcmFieldsInUse"),
        ("JNX-OPT-IF-MIB", "jnxoptIfODUkPositionSeqCurrentSize"),
        ("JNX-OPT-IF-MIB", "jnxoptIfODUkPositionSeqPosition"),
        ("JNX-OPT-IF-MIB", "jnxoptIfODUkPositionSeqPointer"),
        ("JNX-OPT-IF-MIB", "jnxoptIfODUkTtpPresent"))
)
if mibBuilder.loadTexts:
    jnxoptIfODUkGroup.setStatus("current")

jnxoptIfODUkTtpSourceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 2, 1, 35)
)
jnxoptIfODUkTtpSourceGroup.setObjects(
    ("JNX-OPT-IF-MIB", "jnxoptIfODUkTtpTraceIdentifierTransmitted")
)
if mibBuilder.loadTexts:
    jnxoptIfODUkTtpSourceGroup.setStatus("current")

jnxoptIfODUkTtpSinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 2, 1, 36)
)
jnxoptIfODUkTtpSinkGroup.setObjects(
      *(("JNX-OPT-IF-MIB", "jnxoptIfODUkTtpDAPIExpected"),
        ("JNX-OPT-IF-MIB", "jnxoptIfODUkTtpSAPIExpected"),
        ("JNX-OPT-IF-MIB", "jnxoptIfODUkTtpTraceIdentifierAccepted"),
        ("JNX-OPT-IF-MIB", "jnxoptIfODUkTtpTIMDetMode"),
        ("JNX-OPT-IF-MIB", "jnxoptIfODUkTtpTIMActEnabled"),
        ("JNX-OPT-IF-MIB", "jnxoptIfODUkTtpDEGThr"),
        ("JNX-OPT-IF-MIB", "jnxoptIfODUkTtpDEGM"),
        ("JNX-OPT-IF-MIB", "jnxoptIfODUkTtpCurrentStatus"))
)
if mibBuilder.loadTexts:
    jnxoptIfODUkTtpSinkGroup.setStatus("current")

jnxoptIfODUkNimGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 2, 1, 37)
)
jnxoptIfODUkNimGroup.setObjects(
      *(("JNX-OPT-IF-MIB", "jnxoptIfODUkNimDAPIExpected"),
        ("JNX-OPT-IF-MIB", "jnxoptIfODUkNimSAPIExpected"),
        ("JNX-OPT-IF-MIB", "jnxoptIfODUkNimTraceIdentifierAccepted"),
        ("JNX-OPT-IF-MIB", "jnxoptIfODUkNimTIMDetMode"),
        ("JNX-OPT-IF-MIB", "jnxoptIfODUkNimTIMActEnabled"),
        ("JNX-OPT-IF-MIB", "jnxoptIfODUkNimDEGThr"),
        ("JNX-OPT-IF-MIB", "jnxoptIfODUkNimDEGM"),
        ("JNX-OPT-IF-MIB", "jnxoptIfODUkNimCurrentStatus"),
        ("JNX-OPT-IF-MIB", "jnxoptIfODUkNimRowStatus"))
)
if mibBuilder.loadTexts:
    jnxoptIfODUkNimGroup.setStatus("current")

jnxoptIfGCC12Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 2, 1, 38)
)
jnxoptIfGCC12Group.setObjects(
      *(("JNX-OPT-IF-MIB", "jnxoptIfGCC12GCCPassThrough"),
        ("JNX-OPT-IF-MIB", "jnxoptIfGCC12Application"),
        ("JNX-OPT-IF-MIB", "jnxoptIfGCC12RowStatus"))
)
if mibBuilder.loadTexts:
    jnxoptIfGCC12Group.setStatus("current")

jnxoptIfODUkTCommonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 2, 1, 39)
)
jnxoptIfODUkTCommonGroup.setObjects(
    ("JNX-OPT-IF-MIB", "jnxoptIfODUkTRowStatus")
)
if mibBuilder.loadTexts:
    jnxoptIfODUkTCommonGroup.setStatus("current")

jnxoptIfODUkTSourceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 2, 1, 40)
)
jnxoptIfODUkTSourceGroup.setObjects(
      *(("JNX-OPT-IF-MIB", "jnxoptIfODUkTTraceIdentifierTransmitted"),
        ("JNX-OPT-IF-MIB", "jnxoptIfODUkTSourceLockSignalAdminState"))
)
if mibBuilder.loadTexts:
    jnxoptIfODUkTSourceGroup.setStatus("current")

jnxoptIfODUkTSinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 2, 1, 41)
)
jnxoptIfODUkTSinkGroup.setObjects(
      *(("JNX-OPT-IF-MIB", "jnxoptIfODUkTDAPIExpected"),
        ("JNX-OPT-IF-MIB", "jnxoptIfODUkTSAPIExpected"),
        ("JNX-OPT-IF-MIB", "jnxoptIfODUkTTraceIdentifierAccepted"),
        ("JNX-OPT-IF-MIB", "jnxoptIfODUkTTIMDetMode"),
        ("JNX-OPT-IF-MIB", "jnxoptIfODUkTTIMActEnabled"),
        ("JNX-OPT-IF-MIB", "jnxoptIfODUkTDEGThr"),
        ("JNX-OPT-IF-MIB", "jnxoptIfODUkTDEGM"),
        ("JNX-OPT-IF-MIB", "jnxoptIfODUkTCurrentStatus"))
)
if mibBuilder.loadTexts:
    jnxoptIfODUkTSinkGroup.setStatus("current")

jnxoptIfODUkTSinkGroupCtp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 2, 1, 42)
)
jnxoptIfODUkTSinkGroupCtp.setObjects(
      *(("JNX-OPT-IF-MIB", "jnxoptIfODUkTSinkMode"),
        ("JNX-OPT-IF-MIB", "jnxoptIfODUkTSinkLockSignalAdminState"))
)
if mibBuilder.loadTexts:
    jnxoptIfODUkTSinkGroupCtp.setStatus("current")

jnxoptIfODUkTNimGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 2, 1, 43)
)
jnxoptIfODUkTNimGroup.setObjects(
      *(("JNX-OPT-IF-MIB", "jnxoptIfODUkTNimDAPIExpected"),
        ("JNX-OPT-IF-MIB", "jnxoptIfODUkTNimSAPIExpected"),
        ("JNX-OPT-IF-MIB", "jnxoptIfODUkTNimTraceIdentifierAccepted"),
        ("JNX-OPT-IF-MIB", "jnxoptIfODUkTNimTIMDetMode"),
        ("JNX-OPT-IF-MIB", "jnxoptIfODUkTNimTIMActEnabled"),
        ("JNX-OPT-IF-MIB", "jnxoptIfODUkTNimDEGThr"),
        ("JNX-OPT-IF-MIB", "jnxoptIfODUkTNimDEGM"),
        ("JNX-OPT-IF-MIB", "jnxoptIfODUkTNimCurrentStatus"),
        ("JNX-OPT-IF-MIB", "jnxoptIfODUkTNimRowStatus"))
)
if mibBuilder.loadTexts:
    jnxoptIfODUkTNimGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

jnxoptIfOtnConfigCompl = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    jnxoptIfOtnConfigCompl.setStatus(
        "current"
    )

jnxoptIfPreOtnPMCompl = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    jnxoptIfPreOtnPMCompl.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JNX-OPT-IF-MIB",
    **{"JnxoptIfAcTI": JnxoptIfAcTI,
       "JnxoptIfBitRateK": JnxoptIfBitRateK,
       "JnxoptIfDEGM": JnxoptIfDEGM,
       "JnxoptIfDEGThr": JnxoptIfDEGThr,
       "JnxoptIfDirectionality": JnxoptIfDirectionality,
       "JnxoptIfSinkOrSource": JnxoptIfSinkOrSource,
       "JnxoptIfExDAPI": JnxoptIfExDAPI,
       "JnxoptIfExSAPI": JnxoptIfExSAPI,
       "JnxoptIfIntervalNumber": JnxoptIfIntervalNumber,
       "JnxoptIfTIMDetMode": JnxoptIfTIMDetMode,
       "JnxoptIfTxTI": JnxoptIfTxTI,
       "jnxoptIfMibModule": jnxoptIfMibModule,
       "jnxoptIfObjects": jnxoptIfObjects,
       "jnxoptIfOTMn": jnxoptIfOTMn,
       "jnxoptIfOTMnTable": jnxoptIfOTMnTable,
       "jnxoptIfOTMnEntry": jnxoptIfOTMnEntry,
       "jnxoptIfOTMnOrder": jnxoptIfOTMnOrder,
       "jnxoptIfOTMnReduced": jnxoptIfOTMnReduced,
       "jnxoptIfOTMnBitRates": jnxoptIfOTMnBitRates,
       "jnxoptIfOTMnInterfaceType": jnxoptIfOTMnInterfaceType,
       "jnxoptIfOTMnTcmMax": jnxoptIfOTMnTcmMax,
       "jnxoptIfOTMnOpticalReach": jnxoptIfOTMnOpticalReach,
       "jnxoptIfPerfMon": jnxoptIfPerfMon,
       "jnxoptIfPerfMonIntervalTable": jnxoptIfPerfMonIntervalTable,
       "jnxoptIfPerfMonIntervalEntry": jnxoptIfPerfMonIntervalEntry,
       "jnxoptIfPerfMonCurrentTimeElapsed": jnxoptIfPerfMonCurrentTimeElapsed,
       "jnxoptIfPerfMonCurDayTimeElapsed": jnxoptIfPerfMonCurDayTimeElapsed,
       "jnxoptIfPerfMonIntervalNumIntervals": jnxoptIfPerfMonIntervalNumIntervals,
       "jnxoptIfPerfMonIntervalNumInvalidIntervals": jnxoptIfPerfMonIntervalNumInvalidIntervals,
       "jnxoptIfOTSn": jnxoptIfOTSn,
       "jnxoptIfOTSnConfigTable": jnxoptIfOTSnConfigTable,
       "jnxoptIfOTSnConfigEntry": jnxoptIfOTSnConfigEntry,
       "jnxoptIfOTSnDirectionality": jnxoptIfOTSnDirectionality,
       "jnxoptIfOTSnAprStatus": jnxoptIfOTSnAprStatus,
       "jnxoptIfOTSnAprControl": jnxoptIfOTSnAprControl,
       "jnxoptIfOTSnTraceIdentifierTransmitted": jnxoptIfOTSnTraceIdentifierTransmitted,
       "jnxoptIfOTSnDAPIExpected": jnxoptIfOTSnDAPIExpected,
       "jnxoptIfOTSnSAPIExpected": jnxoptIfOTSnSAPIExpected,
       "jnxoptIfOTSnTraceIdentifierAccepted": jnxoptIfOTSnTraceIdentifierAccepted,
       "jnxoptIfOTSnTIMDetMode": jnxoptIfOTSnTIMDetMode,
       "jnxoptIfOTSnTIMActEnabled": jnxoptIfOTSnTIMActEnabled,
       "jnxoptIfOTSnCurrentStatus": jnxoptIfOTSnCurrentStatus,
       "jnxoptIfOTSnSinkCurrentTable": jnxoptIfOTSnSinkCurrentTable,
       "jnxoptIfOTSnSinkCurrentEntry": jnxoptIfOTSnSinkCurrentEntry,
       "jnxoptIfOTSnSinkCurrentSuspectedFlag": jnxoptIfOTSnSinkCurrentSuspectedFlag,
       "jnxoptIfOTSnSinkCurrentInputPower": jnxoptIfOTSnSinkCurrentInputPower,
       "jnxoptIfOTSnSinkCurrentLowInputPower": jnxoptIfOTSnSinkCurrentLowInputPower,
       "jnxoptIfOTSnSinkCurrentHighInputPower": jnxoptIfOTSnSinkCurrentHighInputPower,
       "jnxoptIfOTSnSinkCurrentLowerInputPowerThreshold": jnxoptIfOTSnSinkCurrentLowerInputPowerThreshold,
       "jnxoptIfOTSnSinkCurrentUpperInputPowerThreshold": jnxoptIfOTSnSinkCurrentUpperInputPowerThreshold,
       "jnxoptIfOTSnSinkCurrentOutputPower": jnxoptIfOTSnSinkCurrentOutputPower,
       "jnxoptIfOTSnSinkCurrentLowOutputPower": jnxoptIfOTSnSinkCurrentLowOutputPower,
       "jnxoptIfOTSnSinkCurrentHighOutputPower": jnxoptIfOTSnSinkCurrentHighOutputPower,
       "jnxoptIfOTSnSinkCurrentLowerOutputPowerThreshold": jnxoptIfOTSnSinkCurrentLowerOutputPowerThreshold,
       "jnxoptIfOTSnSinkCurrentUpperOutputPowerThreshold": jnxoptIfOTSnSinkCurrentUpperOutputPowerThreshold,
       "jnxoptIfOTSnSinkIntervalTable": jnxoptIfOTSnSinkIntervalTable,
       "jnxoptIfOTSnSinkIntervalEntry": jnxoptIfOTSnSinkIntervalEntry,
       "jnxoptIfOTSnSinkIntervalNumber": jnxoptIfOTSnSinkIntervalNumber,
       "jnxoptIfOTSnSinkIntervalSuspectedFlag": jnxoptIfOTSnSinkIntervalSuspectedFlag,
       "jnxoptIfOTSnSinkIntervalLastInputPower": jnxoptIfOTSnSinkIntervalLastInputPower,
       "jnxoptIfOTSnSinkIntervalLowInputPower": jnxoptIfOTSnSinkIntervalLowInputPower,
       "jnxoptIfOTSnSinkIntervalHighInputPower": jnxoptIfOTSnSinkIntervalHighInputPower,
       "jnxoptIfOTSnSinkIntervalLastOutputPower": jnxoptIfOTSnSinkIntervalLastOutputPower,
       "jnxoptIfOTSnSinkIntervalLowOutputPower": jnxoptIfOTSnSinkIntervalLowOutputPower,
       "jnxoptIfOTSnSinkIntervalHighOutputPower": jnxoptIfOTSnSinkIntervalHighOutputPower,
       "jnxoptIfOTSnSinkCurDayTable": jnxoptIfOTSnSinkCurDayTable,
       "jnxoptIfOTSnSinkCurDayEntry": jnxoptIfOTSnSinkCurDayEntry,
       "jnxoptIfOTSnSinkCurDaySuspectedFlag": jnxoptIfOTSnSinkCurDaySuspectedFlag,
       "jnxoptIfOTSnSinkCurDayLowInputPower": jnxoptIfOTSnSinkCurDayLowInputPower,
       "jnxoptIfOTSnSinkCurDayHighInputPower": jnxoptIfOTSnSinkCurDayHighInputPower,
       "jnxoptIfOTSnSinkCurDayLowOutputPower": jnxoptIfOTSnSinkCurDayLowOutputPower,
       "jnxoptIfOTSnSinkCurDayHighOutputPower": jnxoptIfOTSnSinkCurDayHighOutputPower,
       "jnxoptIfOTSnSinkPrevDayTable": jnxoptIfOTSnSinkPrevDayTable,
       "jnxoptIfOTSnSinkPrevDayEntry": jnxoptIfOTSnSinkPrevDayEntry,
       "jnxoptIfOTSnSinkPrevDaySuspectedFlag": jnxoptIfOTSnSinkPrevDaySuspectedFlag,
       "jnxoptIfOTSnSinkPrevDayLastInputPower": jnxoptIfOTSnSinkPrevDayLastInputPower,
       "jnxoptIfOTSnSinkPrevDayLowInputPower": jnxoptIfOTSnSinkPrevDayLowInputPower,
       "jnxoptIfOTSnSinkPrevDayHighInputPower": jnxoptIfOTSnSinkPrevDayHighInputPower,
       "jnxoptIfOTSnSinkPrevDayLastOutputPower": jnxoptIfOTSnSinkPrevDayLastOutputPower,
       "jnxoptIfOTSnSinkPrevDayLowOutputPower": jnxoptIfOTSnSinkPrevDayLowOutputPower,
       "jnxoptIfOTSnSinkPrevDayHighOutputPower": jnxoptIfOTSnSinkPrevDayHighOutputPower,
       "jnxoptIfOTSnSrcCurrentTable": jnxoptIfOTSnSrcCurrentTable,
       "jnxoptIfOTSnSrcCurrentEntry": jnxoptIfOTSnSrcCurrentEntry,
       "jnxoptIfOTSnSrcCurrentSuspectedFlag": jnxoptIfOTSnSrcCurrentSuspectedFlag,
       "jnxoptIfOTSnSrcCurrentOutputPower": jnxoptIfOTSnSrcCurrentOutputPower,
       "jnxoptIfOTSnSrcCurrentLowOutputPower": jnxoptIfOTSnSrcCurrentLowOutputPower,
       "jnxoptIfOTSnSrcCurrentHighOutputPower": jnxoptIfOTSnSrcCurrentHighOutputPower,
       "jnxoptIfOTSnSrcCurrentLowerOutputPowerThreshold": jnxoptIfOTSnSrcCurrentLowerOutputPowerThreshold,
       "jnxoptIfOTSnSrcCurrentUpperOutputPowerThreshold": jnxoptIfOTSnSrcCurrentUpperOutputPowerThreshold,
       "jnxoptIfOTSnSrcCurrentInputPower": jnxoptIfOTSnSrcCurrentInputPower,
       "jnxoptIfOTSnSrcCurrentLowInputPower": jnxoptIfOTSnSrcCurrentLowInputPower,
       "jnxoptIfOTSnSrcCurrentHighInputPower": jnxoptIfOTSnSrcCurrentHighInputPower,
       "jnxoptIfOTSnSrcCurrentLowerInputPowerThreshold": jnxoptIfOTSnSrcCurrentLowerInputPowerThreshold,
       "jnxoptIfOTSnSrcCurrentUpperInputPowerThreshold": jnxoptIfOTSnSrcCurrentUpperInputPowerThreshold,
       "jnxoptIfOTSnSrcIntervalTable": jnxoptIfOTSnSrcIntervalTable,
       "jnxoptIfOTSnSrcIntervalEntry": jnxoptIfOTSnSrcIntervalEntry,
       "jnxoptIfOTSnSrcIntervalNumber": jnxoptIfOTSnSrcIntervalNumber,
       "jnxoptIfOTSnSrcIntervalSuspectedFlag": jnxoptIfOTSnSrcIntervalSuspectedFlag,
       "jnxoptIfOTSnSrcIntervalLastOutputPower": jnxoptIfOTSnSrcIntervalLastOutputPower,
       "jnxoptIfOTSnSrcIntervalLowOutputPower": jnxoptIfOTSnSrcIntervalLowOutputPower,
       "jnxoptIfOTSnSrcIntervalHighOutputPower": jnxoptIfOTSnSrcIntervalHighOutputPower,
       "jnxoptIfOTSnSrcIntervalLastInputPower": jnxoptIfOTSnSrcIntervalLastInputPower,
       "jnxoptIfOTSnSrcIntervalLowInputPower": jnxoptIfOTSnSrcIntervalLowInputPower,
       "jnxoptIfOTSnSrcIntervalHighInputPower": jnxoptIfOTSnSrcIntervalHighInputPower,
       "jnxoptIfOTSnSrcCurDayTable": jnxoptIfOTSnSrcCurDayTable,
       "jnxoptIfOTSnSrcCurDayEntry": jnxoptIfOTSnSrcCurDayEntry,
       "jnxoptIfOTSnSrcCurDaySuspectedFlag": jnxoptIfOTSnSrcCurDaySuspectedFlag,
       "jnxoptIfOTSnSrcCurDayLowOutputPower": jnxoptIfOTSnSrcCurDayLowOutputPower,
       "jnxoptIfOTSnSrcCurDayHighOutputPower": jnxoptIfOTSnSrcCurDayHighOutputPower,
       "jnxoptIfOTSnSrcCurDayLowInputPower": jnxoptIfOTSnSrcCurDayLowInputPower,
       "jnxoptIfOTSnSrcCurDayHighInputPower": jnxoptIfOTSnSrcCurDayHighInputPower,
       "jnxoptIfOTSnSrcPrevDayTable": jnxoptIfOTSnSrcPrevDayTable,
       "jnxoptIfOTSnSrcPrevDayEntry": jnxoptIfOTSnSrcPrevDayEntry,
       "jnxoptIfOTSnSrcPrevDaySuspectedFlag": jnxoptIfOTSnSrcPrevDaySuspectedFlag,
       "jnxoptIfOTSnSrcPrevDayLastOutputPower": jnxoptIfOTSnSrcPrevDayLastOutputPower,
       "jnxoptIfOTSnSrcPrevDayLowOutputPower": jnxoptIfOTSnSrcPrevDayLowOutputPower,
       "jnxoptIfOTSnSrcPrevDayHighOutputPower": jnxoptIfOTSnSrcPrevDayHighOutputPower,
       "jnxoptIfOTSnSrcPrevDayLastInputPower": jnxoptIfOTSnSrcPrevDayLastInputPower,
       "jnxoptIfOTSnSrcPrevDayLowInputPower": jnxoptIfOTSnSrcPrevDayLowInputPower,
       "jnxoptIfOTSnSrcPrevDayHighInputPower": jnxoptIfOTSnSrcPrevDayHighInputPower,
       "jnxoptIfOMSn": jnxoptIfOMSn,
       "jnxoptIfOMSnConfigTable": jnxoptIfOMSnConfigTable,
       "jnxoptIfOMSnConfigEntry": jnxoptIfOMSnConfigEntry,
       "jnxoptIfOMSnDirectionality": jnxoptIfOMSnDirectionality,
       "jnxoptIfOMSnCurrentStatus": jnxoptIfOMSnCurrentStatus,
       "jnxoptIfOMSnSinkCurrentTable": jnxoptIfOMSnSinkCurrentTable,
       "jnxoptIfOMSnSinkCurrentEntry": jnxoptIfOMSnSinkCurrentEntry,
       "jnxoptIfOMSnSinkCurrentSuspectedFlag": jnxoptIfOMSnSinkCurrentSuspectedFlag,
       "jnxoptIfOMSnSinkCurrentAggregatedInputPower": jnxoptIfOMSnSinkCurrentAggregatedInputPower,
       "jnxoptIfOMSnSinkCurrentLowAggregatedInputPower": jnxoptIfOMSnSinkCurrentLowAggregatedInputPower,
       "jnxoptIfOMSnSinkCurrentHighAggregatedInputPower": jnxoptIfOMSnSinkCurrentHighAggregatedInputPower,
       "jnxoptIfOMSnSinkCurrentLowerInputPowerThreshold": jnxoptIfOMSnSinkCurrentLowerInputPowerThreshold,
       "jnxoptIfOMSnSinkCurrentUpperInputPowerThreshold": jnxoptIfOMSnSinkCurrentUpperInputPowerThreshold,
       "jnxoptIfOMSnSinkCurrentOutputPower": jnxoptIfOMSnSinkCurrentOutputPower,
       "jnxoptIfOMSnSinkCurrentLowOutputPower": jnxoptIfOMSnSinkCurrentLowOutputPower,
       "jnxoptIfOMSnSinkCurrentHighOutputPower": jnxoptIfOMSnSinkCurrentHighOutputPower,
       "jnxoptIfOMSnSinkCurrentLowerOutputPowerThreshold": jnxoptIfOMSnSinkCurrentLowerOutputPowerThreshold,
       "jnxoptIfOMSnSinkCurrentUpperOutputPowerThreshold": jnxoptIfOMSnSinkCurrentUpperOutputPowerThreshold,
       "jnxoptIfOMSnSinkIntervalTable": jnxoptIfOMSnSinkIntervalTable,
       "jnxoptIfOMSnSinkIntervalEntry": jnxoptIfOMSnSinkIntervalEntry,
       "jnxoptIfOMSnSinkIntervalNumber": jnxoptIfOMSnSinkIntervalNumber,
       "jnxoptIfOMSnSinkIntervalSuspectedFlag": jnxoptIfOMSnSinkIntervalSuspectedFlag,
       "jnxoptIfOMSnSinkIntervalLastAggregatedInputPower": jnxoptIfOMSnSinkIntervalLastAggregatedInputPower,
       "jnxoptIfOMSnSinkIntervalLowAggregatedInputPower": jnxoptIfOMSnSinkIntervalLowAggregatedInputPower,
       "jnxoptIfOMSnSinkIntervalHighAggregatedInputPower": jnxoptIfOMSnSinkIntervalHighAggregatedInputPower,
       "jnxoptIfOMSnSinkIntervalLastOutputPower": jnxoptIfOMSnSinkIntervalLastOutputPower,
       "jnxoptIfOMSnSinkIntervalLowOutputPower": jnxoptIfOMSnSinkIntervalLowOutputPower,
       "jnxoptIfOMSnSinkIntervalHighOutputPower": jnxoptIfOMSnSinkIntervalHighOutputPower,
       "jnxoptIfOMSnSinkCurDayTable": jnxoptIfOMSnSinkCurDayTable,
       "jnxoptIfOMSnSinkCurDayEntry": jnxoptIfOMSnSinkCurDayEntry,
       "jnxoptIfOMSnSinkCurDaySuspectedFlag": jnxoptIfOMSnSinkCurDaySuspectedFlag,
       "jnxoptIfOMSnSinkCurDayLowAggregatedInputPower": jnxoptIfOMSnSinkCurDayLowAggregatedInputPower,
       "jnxoptIfOMSnSinkCurDayHighAggregatedInputPower": jnxoptIfOMSnSinkCurDayHighAggregatedInputPower,
       "jnxoptIfOMSnSinkCurDayLowOutputPower": jnxoptIfOMSnSinkCurDayLowOutputPower,
       "jnxoptIfOMSnSinkCurDayHighOutputPower": jnxoptIfOMSnSinkCurDayHighOutputPower,
       "jnxoptIfOMSnSinkPrevDayTable": jnxoptIfOMSnSinkPrevDayTable,
       "jnxoptIfOMSnSinkPrevDayEntry": jnxoptIfOMSnSinkPrevDayEntry,
       "jnxoptIfOMSnSinkPrevDaySuspectedFlag": jnxoptIfOMSnSinkPrevDaySuspectedFlag,
       "jnxoptIfOMSnSinkPrevDayLastAggregatedInputPower": jnxoptIfOMSnSinkPrevDayLastAggregatedInputPower,
       "jnxoptIfOMSnSinkPrevDayLowAggregatedInputPower": jnxoptIfOMSnSinkPrevDayLowAggregatedInputPower,
       "jnxoptIfOMSnSinkPrevDayHighAggregatedInputPower": jnxoptIfOMSnSinkPrevDayHighAggregatedInputPower,
       "jnxoptIfOMSnSinkPrevDayLastOutputPower": jnxoptIfOMSnSinkPrevDayLastOutputPower,
       "jnxoptIfOMSnSinkPrevDayLowOutputPower": jnxoptIfOMSnSinkPrevDayLowOutputPower,
       "jnxoptIfOMSnSinkPrevDayHighOutputPower": jnxoptIfOMSnSinkPrevDayHighOutputPower,
       "jnxoptIfOMSnSrcCurrentTable": jnxoptIfOMSnSrcCurrentTable,
       "jnxoptIfOMSnSrcCurrentEntry": jnxoptIfOMSnSrcCurrentEntry,
       "jnxoptIfOMSnSrcCurrentSuspectedFlag": jnxoptIfOMSnSrcCurrentSuspectedFlag,
       "jnxoptIfOMSnSrcCurrentOutputPower": jnxoptIfOMSnSrcCurrentOutputPower,
       "jnxoptIfOMSnSrcCurrentLowOutputPower": jnxoptIfOMSnSrcCurrentLowOutputPower,
       "jnxoptIfOMSnSrcCurrentHighOutputPower": jnxoptIfOMSnSrcCurrentHighOutputPower,
       "jnxoptIfOMSnSrcCurrentLowerOutputPowerThreshold": jnxoptIfOMSnSrcCurrentLowerOutputPowerThreshold,
       "jnxoptIfOMSnSrcCurrentUpperOutputPowerThreshold": jnxoptIfOMSnSrcCurrentUpperOutputPowerThreshold,
       "jnxoptIfOMSnSrcCurrentAggregatedInputPower": jnxoptIfOMSnSrcCurrentAggregatedInputPower,
       "jnxoptIfOMSnSrcCurrentLowAggregatedInputPower": jnxoptIfOMSnSrcCurrentLowAggregatedInputPower,
       "jnxoptIfOMSnSrcCurrentHighAggregatedInputPower": jnxoptIfOMSnSrcCurrentHighAggregatedInputPower,
       "jnxoptIfOMSnSrcCurrentLowerInputPowerThreshold": jnxoptIfOMSnSrcCurrentLowerInputPowerThreshold,
       "jnxoptIfOMSnSrcCurrentUpperInputPowerThreshold": jnxoptIfOMSnSrcCurrentUpperInputPowerThreshold,
       "jnxoptIfOMSnSrcIntervalTable": jnxoptIfOMSnSrcIntervalTable,
       "jnxoptIfOMSnSrcIntervalEntry": jnxoptIfOMSnSrcIntervalEntry,
       "jnxoptIfOMSnSrcIntervalNumber": jnxoptIfOMSnSrcIntervalNumber,
       "jnxoptIfOMSnSrcIntervalSuspectedFlag": jnxoptIfOMSnSrcIntervalSuspectedFlag,
       "jnxoptIfOMSnSrcIntervalLastOutputPower": jnxoptIfOMSnSrcIntervalLastOutputPower,
       "jnxoptIfOMSnSrcIntervalLowOutputPower": jnxoptIfOMSnSrcIntervalLowOutputPower,
       "jnxoptIfOMSnSrcIntervalHighOutputPower": jnxoptIfOMSnSrcIntervalHighOutputPower,
       "jnxoptIfOMSnSrcIntervalLastAggregatedInputPower": jnxoptIfOMSnSrcIntervalLastAggregatedInputPower,
       "jnxoptIfOMSnSrcIntervalLowAggregatedInputPower": jnxoptIfOMSnSrcIntervalLowAggregatedInputPower,
       "jnxoptIfOMSnSrcIntervalHighAggregatedInputPower": jnxoptIfOMSnSrcIntervalHighAggregatedInputPower,
       "jnxoptIfOMSnSrcCurDayTable": jnxoptIfOMSnSrcCurDayTable,
       "jnxoptIfOMSnSrcCurDayEntry": jnxoptIfOMSnSrcCurDayEntry,
       "jnxoptIfOMSnSrcCurDaySuspectedFlag": jnxoptIfOMSnSrcCurDaySuspectedFlag,
       "jnxoptIfOMSnSrcCurDayLowOutputPower": jnxoptIfOMSnSrcCurDayLowOutputPower,
       "jnxoptIfOMSnSrcCurDayHighOutputPower": jnxoptIfOMSnSrcCurDayHighOutputPower,
       "jnxoptIfOMSnSrcCurDayLowAggregatedInputPower": jnxoptIfOMSnSrcCurDayLowAggregatedInputPower,
       "jnxoptIfOMSnSrcCurDayHighAggregatedInputPower": jnxoptIfOMSnSrcCurDayHighAggregatedInputPower,
       "jnxoptIfOMSnSrcPrevDayTable": jnxoptIfOMSnSrcPrevDayTable,
       "jnxoptIfOMSnSrcPrevDayEntry": jnxoptIfOMSnSrcPrevDayEntry,
       "jnxoptIfOMSnSrcPrevDaySuspectedFlag": jnxoptIfOMSnSrcPrevDaySuspectedFlag,
       "jnxoptIfOMSnSrcPrevDayLastOutputPower": jnxoptIfOMSnSrcPrevDayLastOutputPower,
       "jnxoptIfOMSnSrcPrevDayLowOutputPower": jnxoptIfOMSnSrcPrevDayLowOutputPower,
       "jnxoptIfOMSnSrcPrevDayHighOutputPower": jnxoptIfOMSnSrcPrevDayHighOutputPower,
       "jnxoptIfOMSnSrcPrevDayLastAggregatedInputPower": jnxoptIfOMSnSrcPrevDayLastAggregatedInputPower,
       "jnxoptIfOMSnSrcPrevDayLowAggregatedInputPower": jnxoptIfOMSnSrcPrevDayLowAggregatedInputPower,
       "jnxoptIfOMSnSrcPrevDayHighAggregatedInputPower": jnxoptIfOMSnSrcPrevDayHighAggregatedInputPower,
       "jnxoptIfOChGroup": jnxoptIfOChGroup,
       "jnxoptIfOChGroupConfigTable": jnxoptIfOChGroupConfigTable,
       "jnxoptIfOChGroupConfigEntry": jnxoptIfOChGroupConfigEntry,
       "jnxoptIfOChGroupDirectionality": jnxoptIfOChGroupDirectionality,
       "jnxoptIfOChGroupSinkCurrentTable": jnxoptIfOChGroupSinkCurrentTable,
       "jnxoptIfOChGroupSinkCurrentEntry": jnxoptIfOChGroupSinkCurrentEntry,
       "jnxoptIfOChGroupSinkCurrentSuspectedFlag": jnxoptIfOChGroupSinkCurrentSuspectedFlag,
       "jnxoptIfOChGroupSinkCurrentAggregatedInputPower": jnxoptIfOChGroupSinkCurrentAggregatedInputPower,
       "jnxoptIfOChGroupSinkCurrentLowAggregatedInputPower": jnxoptIfOChGroupSinkCurrentLowAggregatedInputPower,
       "jnxoptIfOChGroupSinkCurrentHighAggregatedInputPower": jnxoptIfOChGroupSinkCurrentHighAggregatedInputPower,
       "jnxoptIfOChGroupSinkCurrentLowerInputPowerThreshold": jnxoptIfOChGroupSinkCurrentLowerInputPowerThreshold,
       "jnxoptIfOChGroupSinkCurrentUpperInputPowerThreshold": jnxoptIfOChGroupSinkCurrentUpperInputPowerThreshold,
       "jnxoptIfOChGroupSinkCurrentOutputPower": jnxoptIfOChGroupSinkCurrentOutputPower,
       "jnxoptIfOChGroupSinkCurrentLowOutputPower": jnxoptIfOChGroupSinkCurrentLowOutputPower,
       "jnxoptIfOChGroupSinkCurrentHighOutputPower": jnxoptIfOChGroupSinkCurrentHighOutputPower,
       "jnxoptIfOChGroupSinkCurrentLowerOutputPowerThreshold": jnxoptIfOChGroupSinkCurrentLowerOutputPowerThreshold,
       "jnxoptIfOChGroupSinkCurrentUpperOutputPowerThreshold": jnxoptIfOChGroupSinkCurrentUpperOutputPowerThreshold,
       "jnxoptIfOChGroupSinkIntervalTable": jnxoptIfOChGroupSinkIntervalTable,
       "jnxoptIfOChGroupSinkIntervalEntry": jnxoptIfOChGroupSinkIntervalEntry,
       "jnxoptIfOChGroupSinkIntervalNumber": jnxoptIfOChGroupSinkIntervalNumber,
       "jnxoptIfOChGroupSinkIntervalSuspectedFlag": jnxoptIfOChGroupSinkIntervalSuspectedFlag,
       "jnxoptIfOChGroupSinkIntervalLastAggregatedInputPower": jnxoptIfOChGroupSinkIntervalLastAggregatedInputPower,
       "jnxoptIfOChGroupSinkIntervalLowAggregatedInputPower": jnxoptIfOChGroupSinkIntervalLowAggregatedInputPower,
       "jnxoptIfOChGroupSinkIntervalHighAggregatedInputPower": jnxoptIfOChGroupSinkIntervalHighAggregatedInputPower,
       "jnxoptIfOChGroupSinkIntervalLastOutputPower": jnxoptIfOChGroupSinkIntervalLastOutputPower,
       "jnxoptIfOChGroupSinkIntervalLowOutputPower": jnxoptIfOChGroupSinkIntervalLowOutputPower,
       "jnxoptIfOChGroupSinkIntervalHighOutputPower": jnxoptIfOChGroupSinkIntervalHighOutputPower,
       "jnxoptIfOChGroupSinkCurDayTable": jnxoptIfOChGroupSinkCurDayTable,
       "jnxoptIfOChGroupSinkCurDayEntry": jnxoptIfOChGroupSinkCurDayEntry,
       "jnxoptIfOChGroupSinkCurDaySuspectedFlag": jnxoptIfOChGroupSinkCurDaySuspectedFlag,
       "jnxoptIfOChGroupSinkCurDayLowAggregatedInputPower": jnxoptIfOChGroupSinkCurDayLowAggregatedInputPower,
       "jnxoptIfOChGroupSinkCurDayHighAggregatedInputPower": jnxoptIfOChGroupSinkCurDayHighAggregatedInputPower,
       "jnxoptIfOChGroupSinkCurDayLowOutputPower": jnxoptIfOChGroupSinkCurDayLowOutputPower,
       "jnxoptIfOChGroupSinkCurDayHighOutputPower": jnxoptIfOChGroupSinkCurDayHighOutputPower,
       "jnxoptIfOChGroupSinkPrevDayTable": jnxoptIfOChGroupSinkPrevDayTable,
       "jnxoptIfOChGroupSinkPrevDayEntry": jnxoptIfOChGroupSinkPrevDayEntry,
       "jnxoptIfOChGroupSinkPrevDaySuspectedFlag": jnxoptIfOChGroupSinkPrevDaySuspectedFlag,
       "jnxoptIfOChGroupSinkPrevDayLastAggregatedInputPower": jnxoptIfOChGroupSinkPrevDayLastAggregatedInputPower,
       "jnxoptIfOChGroupSinkPrevDayLowAggregatedInputPower": jnxoptIfOChGroupSinkPrevDayLowAggregatedInputPower,
       "jnxoptIfOChGroupSinkPrevDayHighAggregatedInputPower": jnxoptIfOChGroupSinkPrevDayHighAggregatedInputPower,
       "jnxoptIfOChGroupSinkPrevDayLastOutputPower": jnxoptIfOChGroupSinkPrevDayLastOutputPower,
       "jnxoptIfOChGroupSinkPrevDayLowOutputPower": jnxoptIfOChGroupSinkPrevDayLowOutputPower,
       "jnxoptIfOChGroupSinkPrevDayHighOutputPower": jnxoptIfOChGroupSinkPrevDayHighOutputPower,
       "jnxoptIfOChGroupSrcCurrentTable": jnxoptIfOChGroupSrcCurrentTable,
       "jnxoptIfOChGroupSrcCurrentEntry": jnxoptIfOChGroupSrcCurrentEntry,
       "jnxoptIfOChGroupSrcCurrentSuspectedFlag": jnxoptIfOChGroupSrcCurrentSuspectedFlag,
       "jnxoptIfOChGroupSrcCurrentOutputPower": jnxoptIfOChGroupSrcCurrentOutputPower,
       "jnxoptIfOChGroupSrcCurrentLowOutputPower": jnxoptIfOChGroupSrcCurrentLowOutputPower,
       "jnxoptIfOChGroupSrcCurrentHighOutputPower": jnxoptIfOChGroupSrcCurrentHighOutputPower,
       "jnxoptIfOChGroupSrcCurrentLowerOutputPowerThreshold": jnxoptIfOChGroupSrcCurrentLowerOutputPowerThreshold,
       "jnxoptIfOChGroupSrcCurrentUpperOutputPowerThreshold": jnxoptIfOChGroupSrcCurrentUpperOutputPowerThreshold,
       "jnxoptIfOChGroupSrcCurrentAggregatedInputPower": jnxoptIfOChGroupSrcCurrentAggregatedInputPower,
       "jnxoptIfOChGroupSrcCurrentLowAggregatedInputPower": jnxoptIfOChGroupSrcCurrentLowAggregatedInputPower,
       "jnxoptIfOChGroupSrcCurrentHighAggregatedInputPower": jnxoptIfOChGroupSrcCurrentHighAggregatedInputPower,
       "jnxoptIfOChGroupSrcCurrentLowerInputPowerThreshold": jnxoptIfOChGroupSrcCurrentLowerInputPowerThreshold,
       "jnxoptIfOChGroupSrcCurrentUpperInputPowerThreshold": jnxoptIfOChGroupSrcCurrentUpperInputPowerThreshold,
       "jnxoptIfOChGroupSrcIntervalTable": jnxoptIfOChGroupSrcIntervalTable,
       "jnxoptIfOChGroupSrcIntervalEntry": jnxoptIfOChGroupSrcIntervalEntry,
       "jnxoptIfOChGroupSrcIntervalNumber": jnxoptIfOChGroupSrcIntervalNumber,
       "jnxoptIfOChGroupSrcIntervalSuspectedFlag": jnxoptIfOChGroupSrcIntervalSuspectedFlag,
       "jnxoptIfOChGroupSrcIntervalLastOutputPower": jnxoptIfOChGroupSrcIntervalLastOutputPower,
       "jnxoptIfOChGroupSrcIntervalLowOutputPower": jnxoptIfOChGroupSrcIntervalLowOutputPower,
       "jnxoptIfOChGroupSrcIntervalHighOutputPower": jnxoptIfOChGroupSrcIntervalHighOutputPower,
       "jnxoptIfOChGroupSrcIntervalLastAggregatedInputPower": jnxoptIfOChGroupSrcIntervalLastAggregatedInputPower,
       "jnxoptIfOChGroupSrcIntervalLowAggregatedInputPower": jnxoptIfOChGroupSrcIntervalLowAggregatedInputPower,
       "jnxoptIfOChGroupSrcIntervalHighAggregatedInputPower": jnxoptIfOChGroupSrcIntervalHighAggregatedInputPower,
       "jnxoptIfOChGroupSrcCurDayTable": jnxoptIfOChGroupSrcCurDayTable,
       "jnxoptIfOChGroupSrcCurDayEntry": jnxoptIfOChGroupSrcCurDayEntry,
       "jnxoptIfOChGroupSrcCurDaySuspectedFlag": jnxoptIfOChGroupSrcCurDaySuspectedFlag,
       "jnxoptIfOChGroupSrcCurDayLowOutputPower": jnxoptIfOChGroupSrcCurDayLowOutputPower,
       "jnxoptIfOChGroupSrcCurDayHighOutputPower": jnxoptIfOChGroupSrcCurDayHighOutputPower,
       "jnxoptIfOChGroupSrcCurDayLowAggregatedInputPower": jnxoptIfOChGroupSrcCurDayLowAggregatedInputPower,
       "jnxoptIfOChGroupSrcCurDayHighAggregatedInputPower": jnxoptIfOChGroupSrcCurDayHighAggregatedInputPower,
       "jnxoptIfOChGroupSrcPrevDayTable": jnxoptIfOChGroupSrcPrevDayTable,
       "jnxoptIfOChGroupSrcPrevDayEntry": jnxoptIfOChGroupSrcPrevDayEntry,
       "jnxoptIfOChGroupSrcPrevDaySuspectedFlag": jnxoptIfOChGroupSrcPrevDaySuspectedFlag,
       "jnxoptIfOChGroupSrcPrevDayLastOutputPower": jnxoptIfOChGroupSrcPrevDayLastOutputPower,
       "jnxoptIfOChGroupSrcPrevDayLowOutputPower": jnxoptIfOChGroupSrcPrevDayLowOutputPower,
       "jnxoptIfOChGroupSrcPrevDayHighOutputPower": jnxoptIfOChGroupSrcPrevDayHighOutputPower,
       "jnxoptIfOChGroupSrcPrevDayLastAggregatedInputPower": jnxoptIfOChGroupSrcPrevDayLastAggregatedInputPower,
       "jnxoptIfOChGroupSrcPrevDayLowAggregatedInputPower": jnxoptIfOChGroupSrcPrevDayLowAggregatedInputPower,
       "jnxoptIfOChGroupSrcPrevDayHighAggregatedInputPower": jnxoptIfOChGroupSrcPrevDayHighAggregatedInputPower,
       "jnxoptIfOCh": jnxoptIfOCh,
       "jnxoptIfOChConfigTable": jnxoptIfOChConfigTable,
       "jnxoptIfOChConfigEntry": jnxoptIfOChConfigEntry,
       "jnxoptIfOChDirectionality": jnxoptIfOChDirectionality,
       "jnxoptIfOChCurrentStatus": jnxoptIfOChCurrentStatus,
       "jnxoptIfOChSinkCurrentTable": jnxoptIfOChSinkCurrentTable,
       "jnxoptIfOChSinkCurrentEntry": jnxoptIfOChSinkCurrentEntry,
       "jnxoptIfOChSinkCurrentSuspectedFlag": jnxoptIfOChSinkCurrentSuspectedFlag,
       "jnxoptIfOChSinkCurrentInputPower": jnxoptIfOChSinkCurrentInputPower,
       "jnxoptIfOChSinkCurrentLowInputPower": jnxoptIfOChSinkCurrentLowInputPower,
       "jnxoptIfOChSinkCurrentHighInputPower": jnxoptIfOChSinkCurrentHighInputPower,
       "jnxoptIfOChSinkCurrentLowerInputPowerThreshold": jnxoptIfOChSinkCurrentLowerInputPowerThreshold,
       "jnxoptIfOChSinkCurrentUpperInputPowerThreshold": jnxoptIfOChSinkCurrentUpperInputPowerThreshold,
       "jnxoptIfOChSinkIntervalTable": jnxoptIfOChSinkIntervalTable,
       "jnxoptIfOChSinkIntervalEntry": jnxoptIfOChSinkIntervalEntry,
       "jnxoptIfOChSinkIntervalNumber": jnxoptIfOChSinkIntervalNumber,
       "jnxoptIfOChSinkIntervalSuspectedFlag": jnxoptIfOChSinkIntervalSuspectedFlag,
       "jnxoptIfOChSinkIntervalLastInputPower": jnxoptIfOChSinkIntervalLastInputPower,
       "jnxoptIfOChSinkIntervalLowInputPower": jnxoptIfOChSinkIntervalLowInputPower,
       "jnxoptIfOChSinkIntervalHighInputPower": jnxoptIfOChSinkIntervalHighInputPower,
       "jnxoptIfOChSinkCurDayTable": jnxoptIfOChSinkCurDayTable,
       "jnxoptIfOChSinkCurDayEntry": jnxoptIfOChSinkCurDayEntry,
       "jnxoptIfOChSinkCurDaySuspectedFlag": jnxoptIfOChSinkCurDaySuspectedFlag,
       "jnxoptIfOChSinkCurDayLowInputPower": jnxoptIfOChSinkCurDayLowInputPower,
       "jnxoptIfOChSinkCurDayHighInputPower": jnxoptIfOChSinkCurDayHighInputPower,
       "jnxoptIfOChSinkPrevDayTable": jnxoptIfOChSinkPrevDayTable,
       "jnxoptIfOChSinkPrevDayEntry": jnxoptIfOChSinkPrevDayEntry,
       "jnxoptIfOChSinkPrevDaySuspectedFlag": jnxoptIfOChSinkPrevDaySuspectedFlag,
       "jnxoptIfOChSinkPrevDayLastInputPower": jnxoptIfOChSinkPrevDayLastInputPower,
       "jnxoptIfOChSinkPrevDayLowInputPower": jnxoptIfOChSinkPrevDayLowInputPower,
       "jnxoptIfOChSinkPrevDayHighInputPower": jnxoptIfOChSinkPrevDayHighInputPower,
       "jnxoptIfOChSrcCurrentTable": jnxoptIfOChSrcCurrentTable,
       "jnxoptIfOChSrcCurrentEntry": jnxoptIfOChSrcCurrentEntry,
       "jnxoptIfOChSrcCurrentSuspectedFlag": jnxoptIfOChSrcCurrentSuspectedFlag,
       "jnxoptIfOChSrcCurrentOutputPower": jnxoptIfOChSrcCurrentOutputPower,
       "jnxoptIfOChSrcCurrentLowOutputPower": jnxoptIfOChSrcCurrentLowOutputPower,
       "jnxoptIfOChSrcCurrentHighOutputPower": jnxoptIfOChSrcCurrentHighOutputPower,
       "jnxoptIfOChSrcCurrentLowerOutputPowerThreshold": jnxoptIfOChSrcCurrentLowerOutputPowerThreshold,
       "jnxoptIfOChSrcCurrentUpperOutputPowerThreshold": jnxoptIfOChSrcCurrentUpperOutputPowerThreshold,
       "jnxoptIfOChSrcIntervalTable": jnxoptIfOChSrcIntervalTable,
       "jnxoptIfOChSrcIntervalEntry": jnxoptIfOChSrcIntervalEntry,
       "jnxoptIfOChSrcIntervalNumber": jnxoptIfOChSrcIntervalNumber,
       "jnxoptIfOChSrcIntervalSuspectedFlag": jnxoptIfOChSrcIntervalSuspectedFlag,
       "jnxoptIfOChSrcIntervalLastOutputPower": jnxoptIfOChSrcIntervalLastOutputPower,
       "jnxoptIfOChSrcIntervalLowOutputPower": jnxoptIfOChSrcIntervalLowOutputPower,
       "jnxoptIfOChSrcIntervalHighOutputPower": jnxoptIfOChSrcIntervalHighOutputPower,
       "jnxoptIfOChSrcCurDayTable": jnxoptIfOChSrcCurDayTable,
       "jnxoptIfOChSrcCurDayEntry": jnxoptIfOChSrcCurDayEntry,
       "jnxoptIfOChSrcCurDaySuspectedFlag": jnxoptIfOChSrcCurDaySuspectedFlag,
       "jnxoptIfOChSrcCurDayLowOutputPower": jnxoptIfOChSrcCurDayLowOutputPower,
       "jnxoptIfOChSrcCurDayHighOutputPower": jnxoptIfOChSrcCurDayHighOutputPower,
       "jnxoptIfOChSrcPrevDayTable": jnxoptIfOChSrcPrevDayTable,
       "jnxoptIfOChSrcPrevDayEntry": jnxoptIfOChSrcPrevDayEntry,
       "jnxoptIfOChSrcPrevDaySuspectedFlag": jnxoptIfOChSrcPrevDaySuspectedFlag,
       "jnxoptIfOChSrcPrevDayLastOutputPower": jnxoptIfOChSrcPrevDayLastOutputPower,
       "jnxoptIfOChSrcPrevDayLowOutputPower": jnxoptIfOChSrcPrevDayLowOutputPower,
       "jnxoptIfOChSrcPrevDayHighOutputPower": jnxoptIfOChSrcPrevDayHighOutputPower,
       "jnxoptIfOTUk": jnxoptIfOTUk,
       "jnxoptIfOTUkConfigTable": jnxoptIfOTUkConfigTable,
       "jnxoptIfOTUkConfigEntry": jnxoptIfOTUkConfigEntry,
       "jnxoptIfOTUkDirectionality": jnxoptIfOTUkDirectionality,
       "jnxoptIfOTUkBitRateK": jnxoptIfOTUkBitRateK,
       "jnxoptIfOTUkTraceIdentifierTransmitted": jnxoptIfOTUkTraceIdentifierTransmitted,
       "jnxoptIfOTUkDAPIExpected": jnxoptIfOTUkDAPIExpected,
       "jnxoptIfOTUkSAPIExpected": jnxoptIfOTUkSAPIExpected,
       "jnxoptIfOTUkTraceIdentifierAccepted": jnxoptIfOTUkTraceIdentifierAccepted,
       "jnxoptIfOTUkTIMDetMode": jnxoptIfOTUkTIMDetMode,
       "jnxoptIfOTUkTIMActEnabled": jnxoptIfOTUkTIMActEnabled,
       "jnxoptIfOTUkDEGThr": jnxoptIfOTUkDEGThr,
       "jnxoptIfOTUkDEGM": jnxoptIfOTUkDEGM,
       "jnxoptIfOTUkSinkAdaptActive": jnxoptIfOTUkSinkAdaptActive,
       "jnxoptIfOTUkSourceAdaptActive": jnxoptIfOTUkSourceAdaptActive,
       "jnxoptIfOTUkSinkFECEnabled": jnxoptIfOTUkSinkFECEnabled,
       "jnxoptIfOTUkCurrentStatus": jnxoptIfOTUkCurrentStatus,
       "jnxoptIfGCC0ConfigTable": jnxoptIfGCC0ConfigTable,
       "jnxoptIfGCC0ConfigEntry": jnxoptIfGCC0ConfigEntry,
       "jnxoptIfGCC0Directionality": jnxoptIfGCC0Directionality,
       "jnxoptIfGCC0Application": jnxoptIfGCC0Application,
       "jnxoptIfGCC0RowStatus": jnxoptIfGCC0RowStatus,
       "jnxoptIfODUk": jnxoptIfODUk,
       "jnxoptIfODUkConfigTable": jnxoptIfODUkConfigTable,
       "jnxoptIfODUkConfigEntry": jnxoptIfODUkConfigEntry,
       "jnxoptIfODUkDirectionality": jnxoptIfODUkDirectionality,
       "jnxoptIfODUkBitRateK": jnxoptIfODUkBitRateK,
       "jnxoptIfODUkTcmFieldsInUse": jnxoptIfODUkTcmFieldsInUse,
       "jnxoptIfODUkPositionSeqCurrentSize": jnxoptIfODUkPositionSeqCurrentSize,
       "jnxoptIfODUkTtpPresent": jnxoptIfODUkTtpPresent,
       "jnxoptIfODUkTtpConfigTable": jnxoptIfODUkTtpConfigTable,
       "jnxoptIfODUkTtpConfigEntry": jnxoptIfODUkTtpConfigEntry,
       "jnxoptIfODUkTtpTraceIdentifierTransmitted": jnxoptIfODUkTtpTraceIdentifierTransmitted,
       "jnxoptIfODUkTtpDAPIExpected": jnxoptIfODUkTtpDAPIExpected,
       "jnxoptIfODUkTtpSAPIExpected": jnxoptIfODUkTtpSAPIExpected,
       "jnxoptIfODUkTtpTraceIdentifierAccepted": jnxoptIfODUkTtpTraceIdentifierAccepted,
       "jnxoptIfODUkTtpTIMDetMode": jnxoptIfODUkTtpTIMDetMode,
       "jnxoptIfODUkTtpTIMActEnabled": jnxoptIfODUkTtpTIMActEnabled,
       "jnxoptIfODUkTtpDEGThr": jnxoptIfODUkTtpDEGThr,
       "jnxoptIfODUkTtpDEGM": jnxoptIfODUkTtpDEGM,
       "jnxoptIfODUkTtpCurrentStatus": jnxoptIfODUkTtpCurrentStatus,
       "jnxoptIfODUkPositionSeqTable": jnxoptIfODUkPositionSeqTable,
       "jnxoptIfODUkPositionSeqEntry": jnxoptIfODUkPositionSeqEntry,
       "jnxoptIfODUkPositionSeqIndex": jnxoptIfODUkPositionSeqIndex,
       "jnxoptIfODUkPositionSeqPosition": jnxoptIfODUkPositionSeqPosition,
       "jnxoptIfODUkPositionSeqPointer": jnxoptIfODUkPositionSeqPointer,
       "jnxoptIfODUkNimConfigTable": jnxoptIfODUkNimConfigTable,
       "jnxoptIfODUkNimConfigEntry": jnxoptIfODUkNimConfigEntry,
       "jnxoptIfODUkNimDirectionality": jnxoptIfODUkNimDirectionality,
       "jnxoptIfODUkNimDAPIExpected": jnxoptIfODUkNimDAPIExpected,
       "jnxoptIfODUkNimSAPIExpected": jnxoptIfODUkNimSAPIExpected,
       "jnxoptIfODUkNimTraceIdentifierAccepted": jnxoptIfODUkNimTraceIdentifierAccepted,
       "jnxoptIfODUkNimTIMDetMode": jnxoptIfODUkNimTIMDetMode,
       "jnxoptIfODUkNimTIMActEnabled": jnxoptIfODUkNimTIMActEnabled,
       "jnxoptIfODUkNimDEGThr": jnxoptIfODUkNimDEGThr,
       "jnxoptIfODUkNimDEGM": jnxoptIfODUkNimDEGM,
       "jnxoptIfODUkNimCurrentStatus": jnxoptIfODUkNimCurrentStatus,
       "jnxoptIfODUkNimRowStatus": jnxoptIfODUkNimRowStatus,
       "jnxoptIfGCC12ConfigTable": jnxoptIfGCC12ConfigTable,
       "jnxoptIfGCC12ConfigEntry": jnxoptIfGCC12ConfigEntry,
       "jnxoptIfGCC12Codirectional": jnxoptIfGCC12Codirectional,
       "jnxoptIfGCC12GCCAccess": jnxoptIfGCC12GCCAccess,
       "jnxoptIfGCC12GCCPassThrough": jnxoptIfGCC12GCCPassThrough,
       "jnxoptIfGCC12Application": jnxoptIfGCC12Application,
       "jnxoptIfGCC12RowStatus": jnxoptIfGCC12RowStatus,
       "jnxoptIfODUkT": jnxoptIfODUkT,
       "jnxoptIfODUkTConfigTable": jnxoptIfODUkTConfigTable,
       "jnxoptIfODUkTConfigEntry": jnxoptIfODUkTConfigEntry,
       "jnxoptIfODUkTTcmField": jnxoptIfODUkTTcmField,
       "jnxoptIfODUkTCodirectional": jnxoptIfODUkTCodirectional,
       "jnxoptIfODUkTTraceIdentifierTransmitted": jnxoptIfODUkTTraceIdentifierTransmitted,
       "jnxoptIfODUkTDAPIExpected": jnxoptIfODUkTDAPIExpected,
       "jnxoptIfODUkTSAPIExpected": jnxoptIfODUkTSAPIExpected,
       "jnxoptIfODUkTTraceIdentifierAccepted": jnxoptIfODUkTTraceIdentifierAccepted,
       "jnxoptIfODUkTTIMDetMode": jnxoptIfODUkTTIMDetMode,
       "jnxoptIfODUkTTIMActEnabled": jnxoptIfODUkTTIMActEnabled,
       "jnxoptIfODUkTDEGThr": jnxoptIfODUkTDEGThr,
       "jnxoptIfODUkTDEGM": jnxoptIfODUkTDEGM,
       "jnxoptIfODUkTSinkMode": jnxoptIfODUkTSinkMode,
       "jnxoptIfODUkTSinkLockSignalAdminState": jnxoptIfODUkTSinkLockSignalAdminState,
       "jnxoptIfODUkTSourceLockSignalAdminState": jnxoptIfODUkTSourceLockSignalAdminState,
       "jnxoptIfODUkTCurrentStatus": jnxoptIfODUkTCurrentStatus,
       "jnxoptIfODUkTRowStatus": jnxoptIfODUkTRowStatus,
       "jnxoptIfODUkTNimConfigTable": jnxoptIfODUkTNimConfigTable,
       "jnxoptIfODUkTNimConfigEntry": jnxoptIfODUkTNimConfigEntry,
       "jnxoptIfODUkTNimTcmField": jnxoptIfODUkTNimTcmField,
       "jnxoptIfODUkTNimDirectionality": jnxoptIfODUkTNimDirectionality,
       "jnxoptIfODUkTNimDAPIExpected": jnxoptIfODUkTNimDAPIExpected,
       "jnxoptIfODUkTNimSAPIExpected": jnxoptIfODUkTNimSAPIExpected,
       "jnxoptIfODUkTNimTraceIdentifierAccepted": jnxoptIfODUkTNimTraceIdentifierAccepted,
       "jnxoptIfODUkTNimTIMDetMode": jnxoptIfODUkTNimTIMDetMode,
       "jnxoptIfODUkTNimTIMActEnabled": jnxoptIfODUkTNimTIMActEnabled,
       "jnxoptIfODUkTNimDEGThr": jnxoptIfODUkTNimDEGThr,
       "jnxoptIfODUkTNimDEGM": jnxoptIfODUkTNimDEGM,
       "jnxoptIfODUkTNimCurrentStatus": jnxoptIfODUkTNimCurrentStatus,
       "jnxoptIfODUkTNimRowStatus": jnxoptIfODUkTNimRowStatus,
       "jnxoptIfConfs": jnxoptIfConfs,
       "jnxoptIfGroups": jnxoptIfGroups,
       "jnxoptIfOTMnGroup": jnxoptIfOTMnGroup,
       "jnxoptIfPerfMonGroup": jnxoptIfPerfMonGroup,
       "jnxoptIfOTSnCommonGroup": jnxoptIfOTSnCommonGroup,
       "jnxoptIfOTSnSourceGroupFull": jnxoptIfOTSnSourceGroupFull,
       "jnxoptIfOTSnAPRStatusGroup": jnxoptIfOTSnAPRStatusGroup,
       "jnxoptIfOTSnAPRControlGroup": jnxoptIfOTSnAPRControlGroup,
       "jnxoptIfOTSnSinkGroupBasic": jnxoptIfOTSnSinkGroupBasic,
       "jnxoptIfOTSnSinkGroupFull": jnxoptIfOTSnSinkGroupFull,
       "jnxoptIfOTSnSinkPreOtnPMGroup": jnxoptIfOTSnSinkPreOtnPMGroup,
       "jnxoptIfOTSnSinkPreOtnPMThresholdGroup": jnxoptIfOTSnSinkPreOtnPMThresholdGroup,
       "jnxoptIfOTSnSourcePreOtnPMGroup": jnxoptIfOTSnSourcePreOtnPMGroup,
       "jnxoptIfOTSnSourcePreOtnPMThresholdGroup": jnxoptIfOTSnSourcePreOtnPMThresholdGroup,
       "jnxoptIfOMSnCommonGroup": jnxoptIfOMSnCommonGroup,
       "jnxoptIfOMSnSinkGroupBasic": jnxoptIfOMSnSinkGroupBasic,
       "jnxoptIfOMSnSinkPreOtnPMGroup": jnxoptIfOMSnSinkPreOtnPMGroup,
       "jnxoptIfOMSnSinkPreOtnPMThresholdGroup": jnxoptIfOMSnSinkPreOtnPMThresholdGroup,
       "jnxoptIfOMSnSourcePreOtnPMGroup": jnxoptIfOMSnSourcePreOtnPMGroup,
       "jnxoptIfOMSnSourcePreOtnPMThresholdGroup": jnxoptIfOMSnSourcePreOtnPMThresholdGroup,
       "jnxoptIfOChGroupCommonGroup": jnxoptIfOChGroupCommonGroup,
       "jnxoptIfOChGroupSinkPreOtnPMGroup": jnxoptIfOChGroupSinkPreOtnPMGroup,
       "jnxoptIfOChGroupSinkPreOtnPMThresholdGroup": jnxoptIfOChGroupSinkPreOtnPMThresholdGroup,
       "jnxoptIfOChGroupSourcePreOtnPMGroup": jnxoptIfOChGroupSourcePreOtnPMGroup,
       "jnxoptIfOChGroupSourcePreOtnPMThresholdGroup": jnxoptIfOChGroupSourcePreOtnPMThresholdGroup,
       "jnxoptIfOChCommonGroup": jnxoptIfOChCommonGroup,
       "jnxoptIfOChSinkGroupBasic": jnxoptIfOChSinkGroupBasic,
       "jnxoptIfOChSinkPreOtnPMGroup": jnxoptIfOChSinkPreOtnPMGroup,
       "jnxoptIfOChSinkPreOtnPMThresholdGroup": jnxoptIfOChSinkPreOtnPMThresholdGroup,
       "jnxoptIfOChSourcePreOtnPMGroup": jnxoptIfOChSourcePreOtnPMGroup,
       "jnxoptIfOChSourcePreOtnPMThresholdGroup": jnxoptIfOChSourcePreOtnPMThresholdGroup,
       "jnxoptIfOTUkCommonGroup": jnxoptIfOTUkCommonGroup,
       "jnxoptIfOTUkSourceGroup": jnxoptIfOTUkSourceGroup,
       "jnxoptIfOTUkSinkGroup": jnxoptIfOTUkSinkGroup,
       "jnxoptIfGCC0Group": jnxoptIfGCC0Group,
       "jnxoptIfODUkGroup": jnxoptIfODUkGroup,
       "jnxoptIfODUkTtpSourceGroup": jnxoptIfODUkTtpSourceGroup,
       "jnxoptIfODUkTtpSinkGroup": jnxoptIfODUkTtpSinkGroup,
       "jnxoptIfODUkNimGroup": jnxoptIfODUkNimGroup,
       "jnxoptIfGCC12Group": jnxoptIfGCC12Group,
       "jnxoptIfODUkTCommonGroup": jnxoptIfODUkTCommonGroup,
       "jnxoptIfODUkTSourceGroup": jnxoptIfODUkTSourceGroup,
       "jnxoptIfODUkTSinkGroup": jnxoptIfODUkTSinkGroup,
       "jnxoptIfODUkTSinkGroupCtp": jnxoptIfODUkTSinkGroupCtp,
       "jnxoptIfODUkTNimGroup": jnxoptIfODUkTNimGroup,
       "jnxoptIfCompl": jnxoptIfCompl,
       "jnxoptIfOtnConfigCompl": jnxoptIfOtnConfigCompl,
       "jnxoptIfPreOtnPMCompl": jnxoptIfPreOtnPMCompl}
)
