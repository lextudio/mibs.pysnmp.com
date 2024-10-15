# SNMP MIB module (XLDV20-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XLDV20-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:18:43 2024
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

(onu,) = mibBuilder.importSymbols(
    "AN-MIB",
    "onu")

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



class Xldv20ControlStatus(Integer32):
    """Custom type Xldv20ControlStatus based on Integer32"""
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
        *(("requestBusy", 2),
          ("requestFailed", 4),
          ("requestIdle", 1),
          ("requestPassed", 3))
    )





class Xldv20OperState(Integer32):
    """Custom type Xldv20OperState based on Integer32"""
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





class Xldv20SlotStatus(Integer32):
    """Custom type Xldv20SlotStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("empty", 2),
          ("unknown", 0),
          ("used", 1))
    )





class Xldv20AdminState(Integer32):
    """Custom type Xldv20AdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 2),
          ("unlocked", 1))
    )





class Xldv20AvailStatus(Integer32):
    """Custom type Xldv20AvailStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("degraded", 3),
          ("dependency", 7),
          ("failed", 2),
          ("notInstalled", 5),
          ("offline", 4))
    )





class Xldv20LinkState(Integer32):
    """Custom type Xldv20LinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              6,
              7,
              255)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("download", 4),
          ("idle", 1),
          ("quiet", 0),
          ("remoteDownload", 6),
          ("sleepMode", 7),
          ("train", 2),
          ("unknown", 255))
    )





class Xldv20DbuReadStatus(Integer32):
    """Custom type Xldv20DbuReadStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7081,
              7082,
              7083,
              7084)
        )
    )
    namedValues = NamedValues(
        *(("dbuFileCreationFailed", 7083),
          ("dbuFileTransmissionFailed", 7084),
          ("dbuReadComplete", 7081),
          ("dbuReadFailed", 7082))
    )





class Xldv20TelnetAccess(Integer32):
    """Custom type Xldv20TelnetAccess based on Integer32"""
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
        *(("noAccess", 4),
          ("read", 1),
          ("trace", 2),
          ("write", 3))
    )





class Xldv20TvTelnetSessionStatus(Integer32):
    """Custom type Xldv20TvTelnetSessionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("stopped", 2))
    )





class Xldv20EndpointType(Integer32):
    """Custom type Xldv20EndpointType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("sink", 2),
          ("source", 1))
    )





class Xldv20RstResult(Integer32):
    """Custom type Xldv20RstResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            4
        )
    )
    namedValues = NamedValues(
        ("requestFailed", 4)
    )





class Xldv20ImaGroupState(Integer32):
    """Custom type Xldv20ImaGroupState based on Integer32"""
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
        *(("blocked", 8),
          ("configAbortIncompatibleSymmetry", 5),
          ("configAbortOther", 6),
          ("configAbortUnsupported", 4),
          ("configAbortUnsupportedImaVersion", 10),
          ("insufficientLinks", 7),
          ("notConfigured", 1),
          ("operational", 9),
          ("startUp", 2),
          ("startUpAck", 3))
    )





class Xldv20ImaGroupFailureStatus(Integer32):
    """Custom type Xldv20ImaGroupFailureStatus based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("blockedFe", 11),
          ("blockedNe", 10),
          ("failedAssymetricFe", 7),
          ("failedAssymetricNe", 6),
          ("insufficientLinksFe", 9),
          ("insufficientLinksNe", 8),
          ("invalidImaVersionFe", 14),
          ("invalidImaVersionNe", 13),
          ("invalidValueFe", 5),
          ("invalidValueNe", 4),
          ("noFailure", 1),
          ("otherFailure", 12),
          ("startUpFe", 3),
          ("startUpNe", 2))
    )





class Xldv20ImaGroupTxClkMode(Integer32):
    """Custom type Xldv20ImaGroupTxClkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ctc", 1),
          ("itc", 2))
    )





class Xldv20ImaGroupSymmetry(Integer32):
    """Custom type Xldv20ImaGroupSymmetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("asymmetricConfiguration", 3),
          ("asymmetricOperation", 2),
          ("symmetricOperation", 1))
    )





class Xldv20ImaFrameLength(Integer32):
    """Custom type Xldv20ImaFrameLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(32,
              64,
              128,
              256)
        )
    )
    namedValues = NamedValues(
        *(("m128", 128),
          ("m256", 256),
          ("m32", 32),
          ("m64", 64))
    )





class Xldv20ImaLinkState(Integer32):
    """Custom type Xldv20ImaLinkState based on Integer32"""
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
        *(("active", 8),
          ("notInGroup", 1),
          ("unusableFailed", 6),
          ("unusableFault", 3),
          ("unusableInhibited", 5),
          ("unusableMisconnected", 4),
          ("unusableNoGivenReason", 2),
          ("usable", 7))
    )





class Xldv20ImaLinkFailureStatus(Integer32):
    """Custom type Xldv20ImaLinkFailureStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 6),
          ("farEndRxLinkUnusable", 9),
          ("farEndTxLinkUnusable", 8),
          ("fault", 7),
          ("imaLinkFailure", 2),
          ("lifFailure", 3),
          ("lodsFailure", 4),
          ("misConnected", 5),
          ("noFailure", 1))
    )





class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )





class MilliSeconds(Integer32):
    """Custom type MilliSeconds based on Integer32"""




class Xldv20HwUnitType(Integer32):
    """Custom type Xldv20HwUnitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("equipment", 1),
          ("equipmentHolder", 2),
          ("plugInUnit", 3))
    )





class Xldv20IfType(Integer32):
    """Custom type Xldv20IfType based on Integer32"""
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
              20,
              21,
              22,
              23,
              24,
              25,
              107)
        )
    )
    namedValues = NamedValues(
        *(("adc", 3),
          ("adr", 4),
          ("atmIma", 107),
          ("d1fIma", 23),
          ("d1nIma", 22),
          ("d3f", 12),
          ("d3n", 11),
          ("e1fIma", 21),
          ("e1nIma", 20),
          ("e3f", 14),
          ("e3n", 13),
          ("eth", 10),
          ("ibm", 5),
          ("pon", 7),
          ("s1f", 2),
          ("s1n", 1),
          ("s3f", 16),
          ("s3n", 15),
          ("sdc", 24),
          ("sdr", 25),
          ("tca", 6),
          ("vdc", 8),
          ("vdr", 9))
    )





class Xldv20AlarmState(Integer32):
    """Custom type Xldv20AlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              105,
              114,
              115,
              116,
              117,
              123,
              130,
              131,
              132,
              141,
              407,
              408,
              409,
              410,
              411,
              412,
              413,
              450,
              451,
              452,
              453,
              454,
              455,
              456)
        )
    )
    namedValues = NamedValues(
        *(("actFault", 16),
          ("ais", 114),
          ("blockedFe", 455),
          ("configAbort", 451),
          ("configAbortFe", 452),
          ("excBER", 407),
          ("hpEBER", 1),
          ("hpUNEQ", 2),
          ("imaMinNumOfLinks", 456),
          ("immMNR", 130),
          ("insufficientLinks", 453),
          ("insufficientLinksFe", 454),
          ("internalFault", 123),
          ("lcd", 3),
          ("lif", 408),
          ("lods", 409),
          ("lof", 4),
          ("lol", 132),
          ("lop", 5),
          ("los", 6),
          ("lpr", 131),
          ("msAIS", 7),
          ("msEBER", 8),
          ("msRDI", 9),
          ("msSD", 10),
          ("noAlarm", 0),
          ("pAIS", 11),
          ("pRDI", 12),
          ("plcpLof", 116),
          ("plcpRDI", 117),
          ("rai", 413),
          ("rdi", 115),
          ("rfiIma", 412),
          ("rsEBER", 13),
          ("rxUnusableFe", 411),
          ("slm", 14),
          ("startUpFe", 450),
          ("tim", 15),
          ("txUnusableFe", 410),
          ("wrongServiceConfigData", 141),
          ("xmissionErr", 105))
    )





class Xldv20SuppressionType(Integer32):
    """Custom type Xldv20SuppressionType based on Integer32"""
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
        *(("allTraps", 2),
          ("noAlarms", 4),
          ("noEvents", 3),
          ("noTraps", 1))
    )





class Xldv20TrafficType(Integer32):
    """Custom type Xldv20TrafficType based on Integer32"""
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
        *(("cbr", 1),
          ("nrtVbr", 3),
          ("rtVbr", 4),
          ("ubr", 2))
    )





class Xldv20TrafficDirection(Integer32):
    """Custom type Xldv20TrafficDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 1),
          ("downstream", 3),
          ("upstream", 2))
    )





class Xldv20EqhType(Integer32):
    """Custom type Xldv20EqhType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("basicShelf", 3),
          ("cpeShelf", 7),
          ("extendedShelf", 4),
          ("ntAdslShelf", 5),
          ("ntVdslShelf", 6),
          ("shelf", 1),
          ("slot", 2))
    )





class Xldv20LineType(Integer32):
    """Custom type Xldv20LineType based on Integer32"""
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
        *(("coax", 5),
          ("ds3plcp", 8),
          ("e3direct", 7),
          ("longSingleMode", 4),
          ("mediumSingleMode", 3),
          ("other", 1),
          ("shortSingleMode", 2),
          ("utp", 6))
    )





class Xldv20S1nS3nEberThreshold(Integer32):
    """Custom type Xldv20S1nS3nEberThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("exp10E3", 1),
          ("exp10E4", 2),
          ("exp10E5", 3),
          ("noSupervision", 255))
    )





class Xldv20S1nS3nSDThreshold(Integer32):
    """Custom type Xldv20S1nS3nSDThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7,
              255)
        )
    )
    namedValues = NamedValues(
        *(("exp10E5", 3),
          ("exp10E6", 4),
          ("exp10E7", 5),
          ("exp10E8", 6),
          ("exp10E9", 7),
          ("noSupervision", 255))
    )





class Xldv20AlarmSeverity(Integer32):
    """Custom type Xldv20AlarmSeverity based on Integer32"""
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("noAlarming", 5),
          ("warning", 4))
    )





class Xldv20AlmSevProfileIndex(Integer32):
    """Custom type Xldv20AlmSevProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )





class Xldv20AlmFiltProfileIndex(Integer32):
    """Custom type Xldv20AlmFiltProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )





class Xldv20RiResultType(Integer32):
    """Custom type Xldv20RiResultType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("riFileCreationFailed", 2),
          ("riFileTransmissionFailed", 3),
          ("riRemoteInventoryComplete", 1))
    )





class Xldv20RowStatus(Integer32):
    """Custom type Xldv20RowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )





class Xldv20CodingType(Integer32):
    """Custom type Xldv20CodingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dsx3B3ZS", 2),
          ("e3HDB3", 1))
    )





class Xldv20ExtAlarmActivityState(Integer32):
    """Custom type Xldv20ExtAlarmActivityState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1),
          ("undeterminate", 0))
    )





class Xldv20EmptyCellType(Integer32):
    """Custom type Xldv20EmptyCellType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("unassigned", 2))
    )





class Xldv20LogType(Integer32):
    """Custom type Xldv20LogType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hwmLog", 1),
          ("swTraceLog", 3),
          ("sweLog", 2))
    )





class Xldv20SucAllOfType(Integer32):
    """Custom type Xldv20SucAllOfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              10)
        )
    )
    namedValues = NamedValues(
        *(("sucLoadTypeUnknown", 10),
          ("sucUpgrAll", 2),
          ("sucUpgrSingle", 1))
    )





class Xldv20ResetLevel(Integer32):
    """Custom type Xldv20ResetLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("plugInUnit", 3),
          ("system", 4))
    )





class Xldv20VdcRateDn(Integer32):
    """Custom type Xldv20VdcRateDn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              6,
              8,
              12,
              16,
              24,
              32,
              48,
              64)
        )
    )
    namedValues = NamedValues(
        *(("rateDn12", 12),
          ("rateDn16", 16),
          ("rateDn2", 2),
          ("rateDn24", 24),
          ("rateDn32", 32),
          ("rateDn4", 4),
          ("rateDn48", 48),
          ("rateDn6", 6),
          ("rateDn64", 64),
          ("rateDn8", 8))
    )





class Xldv20VdcRateUp(Integer32):
    """Custom type Xldv20VdcRateUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              12,
              16)
        )
    )
    namedValues = NamedValues(
        *(("rateUp1", 1),
          ("rateUp12", 12),
          ("rateUp16", 16),
          ("rateUp2", 2),
          ("rateUp4", 4),
          ("rateUp8", 8))
    )





class Xldv20VdcLatencyDn(Integer32):
    """Custom type Xldv20VdcLatencyDn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4,
              8,
              12,
              16,
              20,
              32)
        )
    )
    namedValues = NamedValues(
        *(("latencyDn0", 0),
          ("latencyDn12", 12),
          ("latencyDn16", 16),
          ("latencyDn2", 2),
          ("latencyDn20", 20),
          ("latencyDn32", 32),
          ("latencyDn4", 4),
          ("latencyDn8", 8))
    )





class Xldv20VdcLatencyUp(Integer32):
    """Custom type Xldv20VdcLatencyUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4,
              8,
              10,
              20)
        )
    )
    namedValues = NamedValues(
        *(("latencyUp0", 0),
          ("latencyUp10", 10),
          ("latencyUp2", 2),
          ("latencyUp20", 20),
          ("latencyUp4", 4),
          ("latencyUp8", 8))
    )





class Xldv20VdcPowerBoostAdaptationType(Integer32):
    """Custom type Xldv20VdcPowerBoostAdaptationType based on Integer32"""
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
        *(("bothDisabled", 4),
          ("bothEnabled", 3),
          ("ntEnabled", 2),
          ("suEnabled", 1))
    )





class Xldv20VdcVdslMode(Integer32):
    """Custom type Xldv20VdcVdslMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adslFriendly", 1),
          ("vdslEfficient", 2))
    )





class Xldv20VdcPsdMask(Integer32):
    """Custom type Xldv20VdcPsdMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("m1", 1),
          ("m2", 2))
    )





class Xldv20EthNtMode(Integer32):
    """Custom type Xldv20EthNtMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("bridging", 1),
          ("currentConfiguration", 4),
          ("routing", 2))
    )





class Xldv20E3nPayloadType(Integer32):
    """Custom type Xldv20E3nPayloadType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("atm", 3),
          ("nonSpecific", 2),
          ("unequipped", 1))
    )





class Xldv20CallpAlarmState(Integer32):
    """Custom type Xldv20CallpAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarmPresent", 2),
          ("noAlarm", 1))
    )





class Xldv20TpAlarmState(Integer32):
    """Custom type Xldv20TpAlarmState based on Integer32"""
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
        *(("downstreamAlarm", 3),
          ("noAlarm", 1),
          ("upAndDownstreamAlarm", 4),
          ("upstreamAlarm", 2))
    )





class Xldv20Latency(Integer32):
    """Custom type Xldv20Latency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              256)
        )
    )
    namedValues = NamedValues(
        *(("fast", 256),
          ("interleavedHigh", 1),
          ("interleavedLow", 0))
    )





class Xldv20TestType(Integer32):
    """Custom type Xldv20TestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("endToEnd", 2),
          ("segment", 1))
    )





class Xldv20FlowDirection(Integer32):
    """Custom type Xldv20FlowDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inwards", 2),
          ("outwards", 3),
          ("undefined", 1))
    )





class Xldv20OamLevel(Integer32):
    """Custom type Xldv20OamLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("f1", 1),
          ("f2", 2),
          ("f3", 3),
          ("f4", 4),
          ("f5", 5),
          ("undefined", 0))
    )





class Xldv20TrapIds(Integer32):
    """Custom type Xldv20TrapIds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              38,
              40,
              41,
              42,
              44,
              45,
              46,
              100,
              101,
              105,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              127,
              128,
              130,
              131,
              132,
              135,
              136,
              137,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              150,
              151,
              152,
              200,
              400,
              401,
              402,
              403,
              404,
              405,
              406,
              407,
              408,
              409,
              410,
              411,
              412,
              413,
              450,
              451,
              452,
              453,
              454,
              455,
              456,
              457,
              458)
        )
    )
    namedValues = NamedValues(
        *(("trAIS", 114),
          ("trActCcReload", 44),
          ("trActFault", 16),
          ("trActivateLoadResult", 34),
          ("trAgentRunning", 26),
          ("trAltTestResult", 33),
          ("trAtmLayerMultiAlarm", 135),
          ("trAttributeValueChange", 124),
          ("trBlockedFe", 455),
          ("trChangeRate", 31),
          ("trCmuReadyForReset", 32),
          ("trConfigAbort", 451),
          ("trConfigAbortFe", 452),
          ("trContinuityCheckVcEntryCreated", 405),
          ("trContinuityCheckVcEntryDeleted", 406),
          ("trContinuityCheckVpEntryCreated", 403),
          ("trContinuityCheckVpEntryDeleted", 404),
          ("trDbBackup", 119),
          ("trDbRestore", 150),
          ("trExcBER", 407),
          ("trExternalAlarm", 110),
          ("trFtpError", 38),
          ("trHpExcBER", 1),
          ("trHpUNEQ", 2),
          ("trHwmLogRead", 41),
          ("trHwuControl", 112),
          ("trImaMinNumOfLinks", 456),
          ("trImmMNR", 130),
          ("trInsufficientLinks", 453),
          ("trInsufficientLinksFe", 454),
          ("trInternalFault", 123),
          ("trLOC", 145),
          ("trLcd", 3),
          ("trLctSession", 25),
          ("trLif", 408),
          ("trLods", 409),
          ("trLof", 4),
          ("trLol", 132),
          ("trLop", 5),
          ("trLos", 6),
          ("trLpr", 131),
          ("trMaxTrapId", 458),
          ("trMsAIS", 7),
          ("trMsExcBER", 8),
          ("trMsRDI", 9),
          ("trMsSD", 10),
          ("trNoTrapId", 0),
          ("trObjCreate", 100),
          ("trObjDelete", 101),
          ("trPAIS", 11),
          ("trPRDI", 12),
          ("trPUUpgradeSucc", 35),
          ("trPlcpLof", 116),
          ("trPlcpRDI", 117),
          ("trPltTestResult", 28),
          ("trRAI", 413),
          ("trRDI", 115),
          ("trReadSAPSContentFileReady", 121),
          ("trRemInvReady", 118),
          ("trReplaceableUnitFailure", 18),
          ("trReplaceableUnitNotInstalled", 20),
          ("trReplaceableUnitPlugged", 142),
          ("trReplaceableUnitProblem", 19),
          ("trReplaceableUnitRemoved", 113),
          ("trReplaceableUnitReset", 22),
          ("trReplaceableUnitResetEnd", 23),
          ("trReplaceableUnitSwMismatch", 21),
          ("trReplaceableUnitSwMissing", 122),
          ("trReplaceableUnitTypeMismatch", 17),
          ("trReplaceableUnitUnplugged", 143),
          ("trRfiIma", 412),
          ("trRsExcBER", 13),
          ("trRstResult", 27),
          ("trRxUnusableFe", 411),
          ("trSlm", 14),
          ("trStartUpFe", 450),
          ("trStartupEnd", 24),
          ("trStateChangeAdmin", 29),
          ("trStateChangeAvail", 457),
          ("trStateChangeOper", 30),
          ("trStateChangeOperExt", 144),
          ("trSwVersionSet", 120),
          ("trSweLogRead", 40),
          ("trTelnetSession", 136),
          ("trThresholdCrossingAlert", 200),
          ("trTim", 15),
          ("trTraceLogRead", 42),
          ("trTxUnusableFe", 410),
          ("trUnitReadyForReset", 111),
          ("trUnitUpgradeNotRequested", 152),
          ("trUpgradeCancelled", 36),
          ("trUpgradeEndRequestResult", 151),
          ("trVclCACProblem", 139),
          ("trVclCcCreation", 127),
          ("trVclCcDeletion", 128),
          ("trVpcTpCACProblem", 402),
          ("trVpcTpCreation", 400),
          ("trVpcTpDeletion", 401),
          ("trVplCACProblem", 137),
          ("trVplCcCreation", 45),
          ("trVplCcDeletion", 46),
          ("trVplTpReload", 140),
          ("trWrongServiceConfigData", 141),
          ("trXmissionErr", 105))
    )





class Xldv20Requester(Integer32):
    """Custom type Xldv20Requester based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hwm", 2),
          ("tmn", 1))
    )





class Xldv20TimeZone(Integer32):
    """Custom type Xldv20TimeZone based on Integer32"""
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
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44)
        )
    )
    namedValues = NamedValues(
        *(("gmt-10Hawaii", 3),
          ("gmt-11MidwayIslandsSamoa", 2),
          ("gmt-12Eniwetok", 1),
          ("gmt-1AzorenKaverdIslands", 16),
          ("gmt-2MiddleAtlantic", 15),
          ("gmt-330Neufundland", 13),
          ("gmt-3BrasiliaBuenosAiresGeorgetown", 14),
          ("gmt-4CaracasLaPazMontrealQuebec", 12),
          ("gmt-5BogotaLimaQuito", 9),
          ("gmt-5IndianaEast", 10),
          ("gmt-5NewYorkMiamiAtlantaDetroitToronto", 11),
          ("gmt-6ChicagoDallasKansasCityWinnipeg", 7),
          ("gmt-6MexicoCityTegucigalpaSaskatchewan", 8),
          ("gmt-7ArizonaDenverSaltLakeCityCalgary", 6),
          ("gmt-8TijuanaLosAngelesSeattleVancouver", 5),
          ("gmt-9Alaska", 4),
          ("gmt10BrisbaneCanberraMlebourneSydney", 39),
          ("gmt10GuamPortMoresbyHobart", 40),
          ("gmt10Wladiwostok", 41),
          ("gmt11MagadanSalomonenNewCaledonia", 42),
          ("gmt12AucklandWellington", 43),
          ("gmt12FidschiKamtschatkaMarschallIslands", 44),
          ("gmt1AmsterdamMadridParisBelgradZagreb", 18),
          ("gmt1BerlinBernRomeStockholmVienna", 19),
          ("gmt1BudapestPrahaBratislavaWarschau", 20),
          ("gmt2AthensIstanbulMinskBukarest", 21),
          ("gmt2HararePretoriaHelsinkiRevalRiga", 22),
          ("gmt2IsraelKairo", 23),
          ("gmt330Teheran", 27),
          ("gmt3BagdadKuwaitErRiad", 24),
          ("gmt3MoskowStPetersburgWolgograd", 25),
          ("gmt3Nairobi", 26),
          ("gmt430Kabul", 29),
          ("gmt4AbuDhabiMuskatBakuTiflis", 28),
          ("gmt530BombayKaluttaMadrasNewDehli", 32),
          ("gmt5IslamabadKarartschiTaschkent", 30),
          ("gmt5Jekaterinburg", 31),
          ("gmt6AkmolaAlmaAtaDhakaColombo", 33),
          ("gmt7BangkokHanoiJakarta", 34),
          ("gmt8PekingChongqingHongkongUrumchi", 35),
          ("gmt8PerthSingapurTaipeh", 36),
          ("gmt930AdelaideDarwin", 38),
          ("gmt9IrkutskOsakaSapporoTokyoSeoul", 37),
          ("gmtCasablancaDublinLissabonLondon", 17))
    )





class Xldv20DayLightSavingTime(Integer32):
    """Custom type Xldv20DayLightSavingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              10)
        )
    )
    namedValues = NamedValues(
        *(("summerTime1", 1),
          ("summerTime2", 2),
          ("winterTime", 10))
    )





class Xldv20AdslMargin(Integer32):
    """Custom type Xldv20AdslMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-127,
              -126,
              -125,
              -124,
              -123,
              -122,
              -121,
              -120,
              -119,
              -118,
              -117,
              -116,
              -115,
              -114,
              -113,
              -112,
              -111,
              -110,
              -109,
              -108,
              -107,
              -106,
              -105,
              -104,
              -103,
              -102,
              -101,
              -100,
              -99,
              -98,
              -97,
              -96,
              -95,
              -94,
              -93,
              -92,
              -91,
              -90,
              -89,
              -88,
              -87,
              -86,
              -85,
              -84,
              -83,
              -82,
              -81,
              -80,
              -79,
              -78,
              -77,
              -76,
              -75,
              -74,
              -73,
              -72,
              -71,
              -70,
              -69,
              -68,
              -67,
              -66,
              -65,
              -64,
              -63,
              -62,
              -61,
              -60,
              -59,
              -58,
              -57,
              -56,
              -55,
              -54,
              -53,
              -52,
              -51,
              -50,
              -49,
              -48,
              -47,
              -46,
              -45,
              -44,
              -43,
              -42,
              -41,
              -40,
              -39,
              -38,
              -37,
              -36,
              -35,
              -34,
              -33,
              -32,
              -31,
              -30,
              -29,
              -28,
              -27,
              -26,
              -25,
              -24,
              -23,
              -22,
              -21,
              -20,
              -19,
              -18,
              -17,
              -16,
              -15,
              -14,
              -13,
              -12,
              -11,
              -10,
              -9,
              -8,
              -7,
              -6,
              -5,
              -4,
              -3,
              -2,
              -1,
              0,
              1,
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
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              32766,
              32767)
        )
    )
    namedValues = NamedValues(
        *(("dB-1", -1),
          ("dB-10", -10),
          ("dB-100", -100),
          ("dB-101", -101),
          ("dB-102", -102),
          ("dB-103", -103),
          ("dB-104", -104),
          ("dB-105", -105),
          ("dB-106", -106),
          ("dB-107", -107),
          ("dB-108", -108),
          ("dB-109", -109),
          ("dB-11", -11),
          ("dB-110", -110),
          ("dB-111", -111),
          ("dB-112", -112),
          ("dB-113", -113),
          ("dB-114", -114),
          ("dB-115", -115),
          ("dB-116", -116),
          ("dB-117", -117),
          ("dB-118", -118),
          ("dB-119", -119),
          ("dB-12", -12),
          ("dB-120", -120),
          ("dB-121", -121),
          ("dB-122", -122),
          ("dB-123", -123),
          ("dB-124", -124),
          ("dB-125", -125),
          ("dB-126", -126),
          ("dB-127", -127),
          ("dB-13", -13),
          ("dB-14", -14),
          ("dB-15", -15),
          ("dB-16", -16),
          ("dB-17", -17),
          ("dB-18", -18),
          ("dB-19", -19),
          ("dB-2", -2),
          ("dB-20", -20),
          ("dB-21", -21),
          ("dB-22", -22),
          ("dB-23", -23),
          ("dB-24", -24),
          ("dB-25", -25),
          ("dB-26", -26),
          ("dB-27", -27),
          ("dB-28", -28),
          ("dB-29", -29),
          ("dB-3", -3),
          ("dB-30", -30),
          ("dB-31", -31),
          ("dB-32", -32),
          ("dB-33", -33),
          ("dB-34", -34),
          ("dB-35", -35),
          ("dB-36", -36),
          ("dB-37", -37),
          ("dB-38", -38),
          ("dB-39", -39),
          ("dB-4", -4),
          ("dB-40", -40),
          ("dB-41", -41),
          ("dB-42", -42),
          ("dB-43", -43),
          ("dB-44", -44),
          ("dB-45", -45),
          ("dB-46", -46),
          ("dB-47", -47),
          ("dB-48", -48),
          ("dB-49", -49),
          ("dB-5", -5),
          ("dB-50", -50),
          ("dB-51", -51),
          ("dB-52", -52),
          ("dB-53", -53),
          ("dB-54", -54),
          ("dB-55", -55),
          ("dB-56", -56),
          ("dB-57", -57),
          ("dB-58", -58),
          ("dB-59", -59),
          ("dB-6", -6),
          ("dB-60", -60),
          ("dB-61", -61),
          ("dB-62", -62),
          ("dB-63", -63),
          ("dB-64", -64),
          ("dB-65", -65),
          ("dB-66", -66),
          ("dB-67", -67),
          ("dB-68", -68),
          ("dB-69", -69),
          ("dB-7", -7),
          ("dB-70", -70),
          ("dB-71", -71),
          ("dB-72", -72),
          ("dB-73", -73),
          ("dB-74", -74),
          ("dB-75", -75),
          ("dB-76", -76),
          ("dB-77", -77),
          ("dB-78", -78),
          ("dB-79", -79),
          ("dB-8", -8),
          ("dB-80", -80),
          ("dB-81", -81),
          ("dB-82", -82),
          ("dB-83", -83),
          ("dB-84", -84),
          ("dB-85", -85),
          ("dB-86", -86),
          ("dB-87", -87),
          ("dB-88", -88),
          ("dB-89", -89),
          ("dB-9", -9),
          ("dB-90", -90),
          ("dB-91", -91),
          ("dB-92", -92),
          ("dB-93", -93),
          ("dB-94", -94),
          ("dB-95", -95),
          ("dB-96", -96),
          ("dB-97", -97),
          ("dB-98", -98),
          ("dB-99", -99),
          ("dB0", 0),
          ("dB1", 1),
          ("dB10", 10),
          ("dB100", 100),
          ("dB101", 101),
          ("dB102", 102),
          ("dB103", 103),
          ("dB104", 104),
          ("dB105", 105),
          ("dB106", 106),
          ("dB107", 107),
          ("dB108", 108),
          ("dB109", 109),
          ("dB11", 11),
          ("dB110", 110),
          ("dB111", 111),
          ("dB112", 112),
          ("dB113", 113),
          ("dB114", 114),
          ("dB115", 115),
          ("dB116", 116),
          ("dB117", 117),
          ("dB118", 118),
          ("dB119", 119),
          ("dB12", 12),
          ("dB120", 120),
          ("dB121", 121),
          ("dB122", 122),
          ("dB123", 123),
          ("dB124", 124),
          ("dB125", 125),
          ("dB126", 126),
          ("dB127", 127),
          ("dB128", 128),
          ("dB13", 13),
          ("dB14", 14),
          ("dB15", 15),
          ("dB16", 16),
          ("dB17", 17),
          ("dB18", 18),
          ("dB19", 19),
          ("dB2", 2),
          ("dB20", 20),
          ("dB21", 21),
          ("dB22", 22),
          ("dB23", 23),
          ("dB24", 24),
          ("dB25", 25),
          ("dB26", 26),
          ("dB27", 27),
          ("dB28", 28),
          ("dB29", 29),
          ("dB3", 3),
          ("dB30", 30),
          ("dB31", 31),
          ("dB32", 32),
          ("dB33", 33),
          ("dB34", 34),
          ("dB35", 35),
          ("dB36", 36),
          ("dB37", 37),
          ("dB38", 38),
          ("dB39", 39),
          ("dB4", 4),
          ("dB40", 40),
          ("dB41", 41),
          ("dB42", 42),
          ("dB43", 43),
          ("dB44", 44),
          ("dB45", 45),
          ("dB46", 46),
          ("dB47", 47),
          ("dB48", 48),
          ("dB49", 49),
          ("dB5", 5),
          ("dB50", 50),
          ("dB51", 51),
          ("dB52", 52),
          ("dB53", 53),
          ("dB54", 54),
          ("dB55", 55),
          ("dB56", 56),
          ("dB57", 57),
          ("dB58", 58),
          ("dB59", 59),
          ("dB6", 6),
          ("dB60", 60),
          ("dB61", 61),
          ("dB62", 62),
          ("dB63", 63),
          ("dB64", 64),
          ("dB65", 65),
          ("dB66", 66),
          ("dB67", 67),
          ("dB68", 68),
          ("dB69", 69),
          ("dB7", 7),
          ("dB70", 70),
          ("dB71", 71),
          ("dB72", 72),
          ("dB73", 73),
          ("dB74", 74),
          ("dB75", 75),
          ("dB76", 76),
          ("dB77", 77),
          ("dB78", 78),
          ("dB79", 79),
          ("dB8", 8),
          ("dB80", 80),
          ("dB81", 81),
          ("dB82", 82),
          ("dB83", 83),
          ("dB84", 84),
          ("dB85", 85),
          ("dB86", 86),
          ("dB87", 87),
          ("dB88", 88),
          ("dB89", 89),
          ("dB9", 9),
          ("dB90", 90),
          ("dB91", 91),
          ("dB92", 92),
          ("dB93", 93),
          ("dB94", 94),
          ("dB95", 95),
          ("dB96", 96),
          ("dB97", 97),
          ("dB98", 98),
          ("dB99", 99),
          ("marginInvalid", 32767),
          ("marginNotApplicable", 32766))
    )





class Xldv20AdslAttenuation(Integer32):
    """Custom type Xldv20AdslAttenuation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
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
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              212,
              213,
              214,
              215,
              216,
              217,
              218,
              219,
              220,
              221,
              222,
              223,
              224,
              225,
              226,
              227,
              228,
              229,
              230,
              231,
              232,
              233,
              234,
              235,
              236,
              237,
              238,
              239,
              240,
              241,
              242,
              243,
              244,
              245,
              246,
              247,
              248,
              249,
              250,
              251,
              252,
              253,
              254,
              255,
              32766,
              32767)
        )
    )
    namedValues = NamedValues(
        *(("attenuationInvalid", 32767),
          ("attenuationNotApplicable", 32766),
          ("dB0", 0),
          ("dB0Dot5", 1),
          ("dB1", 2),
          ("dB10", 20),
          ("dB100", 200),
          ("dB100Dot5", 201),
          ("dB101", 202),
          ("dB101Dot5", 203),
          ("dB102", 204),
          ("dB102Dot5", 205),
          ("dB103", 206),
          ("dB103Dot5", 207),
          ("dB104", 208),
          ("dB104Dot5", 209),
          ("dB105", 210),
          ("dB105Dot5", 211),
          ("dB106", 212),
          ("dB106Dot5", 213),
          ("dB107", 214),
          ("dB107Dot5", 215),
          ("dB108", 216),
          ("dB108Dot5", 217),
          ("dB109", 218),
          ("dB109Dot5", 219),
          ("dB10Dot5", 21),
          ("dB11", 22),
          ("dB110", 220),
          ("dB110Dot5", 221),
          ("dB111", 222),
          ("dB111Dot5", 223),
          ("dB112", 224),
          ("dB112Dot5", 225),
          ("dB113", 226),
          ("dB113Dot5", 227),
          ("dB114", 228),
          ("dB114Dot5", 229),
          ("dB115", 230),
          ("dB115Dot5", 231),
          ("dB116", 232),
          ("dB116Dot5", 233),
          ("dB117", 234),
          ("dB117Dot5", 235),
          ("dB118", 236),
          ("dB118Dot5", 237),
          ("dB119", 238),
          ("dB119Dot5", 239),
          ("dB11Dot5", 23),
          ("dB12", 24),
          ("dB120", 240),
          ("dB120Dot5", 241),
          ("dB121", 242),
          ("dB121Dot5", 243),
          ("dB122", 244),
          ("dB122Dot5", 245),
          ("dB123", 246),
          ("dB123Dot5", 247),
          ("dB124", 248),
          ("dB124Dot5", 249),
          ("dB125", 250),
          ("dB125Dot5", 251),
          ("dB126", 252),
          ("dB126Dot5", 253),
          ("dB127", 254),
          ("dB127Dot5", 255),
          ("dB12Dot5", 25),
          ("dB13", 26),
          ("dB13Dot5", 27),
          ("dB14", 28),
          ("dB14Dot5", 29),
          ("dB15", 30),
          ("dB15Dot5", 31),
          ("dB16", 32),
          ("dB16Dot5", 33),
          ("dB17", 34),
          ("dB17Dot5", 35),
          ("dB18", 36),
          ("dB18Dot5", 37),
          ("dB19", 38),
          ("dB19Dot5", 39),
          ("dB1Dot5", 3),
          ("dB2", 4),
          ("dB20", 40),
          ("dB20Dot5", 41),
          ("dB21", 42),
          ("dB21Dot5", 43),
          ("dB22", 44),
          ("dB22Dot5", 45),
          ("dB23", 46),
          ("dB23Dot5", 47),
          ("dB24", 48),
          ("dB24Dot5", 49),
          ("dB25", 50),
          ("dB25Dot5", 51),
          ("dB26", 52),
          ("dB26Dot5", 53),
          ("dB27", 54),
          ("dB27Dot5", 55),
          ("dB28", 56),
          ("dB28Dot5", 57),
          ("dB29", 58),
          ("dB29Dot5", 59),
          ("dB2Dot5", 5),
          ("dB3", 6),
          ("dB30", 60),
          ("dB30Dot5", 61),
          ("dB31", 62),
          ("dB31Dot5", 63),
          ("dB32", 64),
          ("dB32Dot5", 65),
          ("dB33", 66),
          ("dB33Dot5", 67),
          ("dB34", 68),
          ("dB34Dot5", 69),
          ("dB35", 70),
          ("dB35Dot5", 71),
          ("dB36", 72),
          ("dB36Dot5", 73),
          ("dB37", 74),
          ("dB37Dot5", 75),
          ("dB38", 76),
          ("dB38Dot5", 77),
          ("dB39", 78),
          ("dB39Dot5", 79),
          ("dB3Dot5", 7),
          ("dB4", 8),
          ("dB40", 80),
          ("dB40Dot5", 81),
          ("dB41", 82),
          ("dB41Dot5", 83),
          ("dB42", 84),
          ("dB42Dot5", 85),
          ("dB43", 86),
          ("dB43Dot5", 87),
          ("dB44", 88),
          ("dB44Dot5", 89),
          ("dB45", 90),
          ("dB45Dot5", 91),
          ("dB46", 92),
          ("dB46Dot5", 93),
          ("dB47", 94),
          ("dB47Dot5", 95),
          ("dB48", 96),
          ("dB48Dot5", 97),
          ("dB49", 98),
          ("dB49Dot5", 99),
          ("dB4Dot5", 9),
          ("dB5", 10),
          ("dB50", 100),
          ("dB50Dot5", 101),
          ("dB51", 102),
          ("dB51Dot5", 103),
          ("dB52", 104),
          ("dB52Dot5", 105),
          ("dB53", 106),
          ("dB53Dot5", 107),
          ("dB54", 108),
          ("dB54Dot5", 109),
          ("dB55", 110),
          ("dB55Dot5", 111),
          ("dB56", 112),
          ("dB56Dot5", 113),
          ("dB57", 114),
          ("dB57Dot5", 115),
          ("dB58", 116),
          ("dB58Dot5", 117),
          ("dB59", 118),
          ("dB59Dot5", 119),
          ("dB5Dot5", 11),
          ("dB6", 12),
          ("dB60", 120),
          ("dB60Dot5", 121),
          ("dB61", 122),
          ("dB61Dot5", 123),
          ("dB62", 124),
          ("dB62Dot5", 125),
          ("dB63", 126),
          ("dB63Dot5", 127),
          ("dB64", 128),
          ("dB64Dot5", 129),
          ("dB65", 130),
          ("dB65Dot5", 131),
          ("dB66", 132),
          ("dB66Dot5", 133),
          ("dB67", 134),
          ("dB67Dot5", 135),
          ("dB68", 136),
          ("dB68Dot5", 137),
          ("dB69", 138),
          ("dB69Dot5", 139),
          ("dB6Dot5", 13),
          ("dB7", 14),
          ("dB70", 140),
          ("dB70Dot5", 141),
          ("dB71", 142),
          ("dB71Dot5", 143),
          ("dB72", 144),
          ("dB72Dot5", 145),
          ("dB73", 146),
          ("dB73Dot5", 147),
          ("dB74", 148),
          ("dB74Dot5", 149),
          ("dB75", 150),
          ("dB75Dot5", 151),
          ("dB76", 152),
          ("dB76Dot5", 153),
          ("dB77", 154),
          ("dB77Dot5", 155),
          ("dB78", 156),
          ("dB78Dot5", 157),
          ("dB79", 158),
          ("dB79Dot5", 159),
          ("dB7Dot5", 15),
          ("dB8", 16),
          ("dB80", 160),
          ("dB80Dot5", 161),
          ("dB81", 162),
          ("dB81Dot5", 163),
          ("dB82", 164),
          ("dB82Dot5", 165),
          ("dB83", 166),
          ("dB83Dot5", 167),
          ("dB84", 168),
          ("dB84Dot5", 169),
          ("dB85", 170),
          ("dB85Dot5", 171),
          ("dB86", 172),
          ("dB86Dot5", 173),
          ("dB87", 174),
          ("dB87Dot5", 175),
          ("dB88", 176),
          ("dB88Dot5", 177),
          ("dB89", 178),
          ("dB89Dot5", 179),
          ("dB8Dot5", 17),
          ("dB9", 18),
          ("dB90", 180),
          ("dB90Dot5", 181),
          ("dB91", 182),
          ("dB91Dot5", 183),
          ("dB92", 184),
          ("dB92Dot5", 185),
          ("dB93", 186),
          ("dB93Dot5", 187),
          ("dB94", 188),
          ("dB94Dot5", 189),
          ("dB95", 190),
          ("dB95Dot5", 191),
          ("dB96", 192),
          ("dB96Dot5", 193),
          ("dB97", 194),
          ("dB97Dot5", 195),
          ("dB98", 196),
          ("dB98Dot5", 197),
          ("dB99", 198),
          ("dB99Dot5", 199),
          ("dB9Dot5", 19))
    )





class Xldv20AdslMinMargin(Integer32):
    """Custom type Xldv20AdslMinMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-6,
              -5,
              -4,
              -3,
              -2,
              -1,
              0,
              1,
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("auto", 255),
          ("dB-1", -1),
          ("dB-2", -2),
          ("dB-3", -3),
          ("dB-4", -4),
          ("dB-5", -5),
          ("dB-6", -6),
          ("dB0", 0),
          ("dB1", 1),
          ("dB10", 10),
          ("dB11", 11),
          ("dB12", 12),
          ("dB2", 2),
          ("dB3", 3),
          ("dB4", 4),
          ("dB5", 5),
          ("dB6", 6),
          ("dB7", 7),
          ("dB8", 8),
          ("dB9", 9))
    )





class Xldv20AdslOutputPower(Integer32):
    """Custom type Xldv20AdslOutputPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-31,
              -30,
              -29,
              -28,
              -27,
              -26,
              -25,
              -24,
              -23,
              -22,
              -21,
              -20,
              -19,
              -18,
              -17,
              -16,
              -15,
              -14,
              -13,
              -12,
              -11,
              -10,
              -9,
              -8,
              -7,
              -6,
              -5,
              -4,
              -3,
              -2,
              -1,
              0,
              1,
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
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              32767)
        )
    )
    namedValues = NamedValues(
        *(("dBm-1", -1),
          ("dBm-10", -10),
          ("dBm-11", -11),
          ("dBm-12", -12),
          ("dBm-13", -13),
          ("dBm-14", -14),
          ("dBm-15", -15),
          ("dBm-16", -16),
          ("dBm-17", -17),
          ("dBm-18", -18),
          ("dBm-19", -19),
          ("dBm-2", -2),
          ("dBm-20", -20),
          ("dBm-21", -21),
          ("dBm-22", -22),
          ("dBm-23", -23),
          ("dBm-24", -24),
          ("dBm-25", -25),
          ("dBm-26", -26),
          ("dBm-27", -27),
          ("dBm-28", -28),
          ("dBm-29", -29),
          ("dBm-3", -3),
          ("dBm-30", -30),
          ("dBm-31", -31),
          ("dBm-4", -4),
          ("dBm-5", -5),
          ("dBm-6", -6),
          ("dBm-7", -7),
          ("dBm-8", -8),
          ("dBm-9", -9),
          ("dBm0", 0),
          ("dBm1", 1),
          ("dBm10", 10),
          ("dBm11", 11),
          ("dBm12", 12),
          ("dBm13", 13),
          ("dBm14", 14),
          ("dBm15", 15),
          ("dBm16", 16),
          ("dBm17", 17),
          ("dBm18", 18),
          ("dBm19", 19),
          ("dBm2", 2),
          ("dBm20", 20),
          ("dBm21", 21),
          ("dBm22", 22),
          ("dBm23", 23),
          ("dBm24", 24),
          ("dBm25", 25),
          ("dBm26", 26),
          ("dBm27", 27),
          ("dBm28", 28),
          ("dBm29", 29),
          ("dBm3", 3),
          ("dBm30", 30),
          ("dBm31", 31),
          ("dBm32", 32),
          ("dBm4", 4),
          ("dBm5", 5),
          ("dBm6", 6),
          ("dBm7", 7),
          ("dBm8", 8),
          ("dBm9", 9),
          ("outputPowerInvalid", 32767))
    )





class Xldv20StartupResult(Integer32):
    """Custom type Xldv20StartupResult based on Integer32"""
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
        *(("suFailed", 2),
          ("suFinished", 1),
          ("suInProgress", 4),
          ("suStandaloneStartupFinished", 3))
    )





class Xldv20StartupType(Integer32):
    """Custom type Xldv20StartupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6300,
              6301,
              6302,
              6303,
              6304)
        )
    )
    namedValues = NamedValues(
        *(("cmuUpgrade", 6303),
          ("cold", 6301),
          ("powerUp", 6304),
          ("reload", 6302),
          ("warm", 6300))
    )





class Xldv20SnmLctSession(Integer32):
    """Custom type Xldv20SnmLctSession based on Integer32"""
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
        *(("connected", 1),
          ("disconnected", 2),
          ("onuCutSession", 5),
          ("sessionCancelled", 3),
          ("sessionTimeout", 4))
    )





class Xldv20RepSource(Integer32):
    """Custom type Xldv20RepSource based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("extAlarm", 5),
          ("hwm", 1),
          ("tlm", 2),
          ("vccTp", 6),
          ("vclCC", 14),
          ("vclNni", 11),
          ("vclTp", 9),
          ("vclUni", 12),
          ("vpcTp", 7),
          ("vplCC", 13),
          ("vplNni", 3),
          ("vplTp", 10),
          ("vplUni", 4))
    )





class Xldv20PollingFlagType(Integer32):
    """Custom type Xldv20PollingFlagType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flagNotSet", 2),
          ("flagSet", 1))
    )





class Xldv20TerminalType(Integer32):
    """Custom type Xldv20TerminalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              10)
        )
    )
    namedValues = NamedValues(
        *(("lct", 2),
          ("tmn", 1),
          ("unknown", 10))
    )





class Xldv20ChannelType(Integer32):
    """Custom type Xldv20ChannelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              10)
        )
    )
    namedValues = NamedValues(
        *(("inband", 1),
          ("outband", 2),
          ("unknown", 10))
    )





class Xldv20XdslServiceType(Integer32):
    """Custom type Xldv20XdslServiceType based on Integer32"""
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
        *(("ansiT1Dot413", 2),
          ("gDotAll", 4),
          ("gDotHsMode", 1),
          ("gDotLiteMode", 3))
    )





class Xldv20XdslServiceTypeCurrent(Integer32):
    """Custom type Xldv20XdslServiceTypeCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              10)
        )
    )
    namedValues = NamedValues(
        *(("ansiT1Dot413", 2),
          ("gDotDmtMode", 1),
          ("gDotLiteMode", 3),
          ("serviceTypeUnknown", 10))
    )





class Xldv20LoopMode(Integer32):
    """Custom type Xldv20LoopMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("loopAndForward", 2))
    )





class Xldv20XdslInitStatus(Integer32):
    """Custom type Xldv20XdslInitStatus based on Integer32"""
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
              18,
              19,
              20,
              21,
              255)
        )
    )
    namedValues = NamedValues(
        *(("adaptationCombinationInvalid", 10),
          ("adrNotCapableOfDualLatency", 13),
          ("alarmsDetected", 20),
          ("channelRatesExceedsSystemLimits", 9),
          ("communicationFailed", 2),
          ("configuredDualChannelInvalid", 11),
          ("configuredMinMaxRelationInvalid", 8),
          ("configuredRatesOutOfRange", 7),
          ("fastRetrainProfileError", 3),
          ("gliteModeNotPossibleInPCM", 19),
          ("initStatusUnknown", 21),
          ("marginLessThanMinMargin", 12),
          ("noInitError", 255),
          ("ntNotPresent", 1),
          ("ntNotPresentDetectedOnCi", 18),
          ("rateParameterConfigurationError", 4),
          ("reserved1", 14),
          ("reserved2", 15),
          ("serviceTypeAdcRequestRejected", 6),
          ("serviceTypeAdrRequestRejected", 5),
          ("trainingBlockedByCi", 17),
          ("trainingBlockedBySu", 16))
    )





class Xldv20AdcTrainingMode(Integer32):
    """Custom type Xldv20AdcTrainingMode based on Integer32"""
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
        *(("avoidParallelTrainingOnCI", 2),
          ("avoidParallelTrainingOnSU", 3),
          ("combinedTraining", 4),
          ("enableParallelTraining", 1))
    )





class Xldv20SdslServiceType(Integer32):
    """Custom type Xldv20SdslServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearChannelFraming", 2),
          ("diamondLaneFraming", 1),
          ("ituFraming", 3))
    )





class Xldv20AdslDataRateDown(Integer32):
    """Custom type Xldv20AdslDataRateDown based on Integer32"""
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
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
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
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              212,
              213,
              214,
              215,
              216,
              217,
              218,
              219,
              220,
              221,
              222,
              223,
              224,
              225,
              226,
              227,
              228,
              229,
              230,
              231,
              232,
              233,
              234,
              235,
              236,
              237,
              238,
              239,
              240,
              241,
              242,
              243,
              244,
              245,
              246,
              247,
              248,
              249,
              250,
              251,
              252,
              253)
        )
    )
    namedValues = NamedValues(
        *(("kbps1024Cps2415", 32),
          ("kbps1056Cps2490", 33),
          ("kbps1088Cps2566", 34),
          ("kbps1120Cps2641", 35),
          ("kbps1152Cps2716", 36),
          ("kbps1184Cps2792", 37),
          ("kbps1216Cps2867", 38),
          ("kbps1248Cps2943", 39),
          ("kbps1280Cps3018", 40),
          ("kbps128Cps301", 4),
          ("kbps1312Cps3094", 41),
          ("kbps1344Cps3169", 42),
          ("kbps1376Cps3245", 43),
          ("kbps1408Cps3320", 44),
          ("kbps1440Cps3396", 45),
          ("kbps1472Cps3471", 46),
          ("kbps1504Cps3547", 47),
          ("kbps1536Cps3622", 48),
          ("kbps1568Cps3698", 49),
          ("kbps1600Cps3773", 50),
          ("kbps160Cps377", 5),
          ("kbps1632Cps3849", 51),
          ("kbps1664Cps3924", 52),
          ("kbps1696Cps4000", 53),
          ("kbps1728Cps4075", 54),
          ("kbps1760Cps4150", 55),
          ("kbps1792Cps4226", 56),
          ("kbps1824Cps4301", 57),
          ("kbps1856Cps4377", 58),
          ("kbps1888Cps4452", 59),
          ("kbps1920Cps4528", 60),
          ("kbps192Cps452", 6),
          ("kbps1952Cps4603", 61),
          ("kbps1984Cps4679", 62),
          ("kbps2016Cps4754", 63),
          ("kbps2048Cps4830", 64),
          ("kbps2080Cps4905", 65),
          ("kbps2112Cps4981", 66),
          ("kbps2144Cps5056", 67),
          ("kbps2176Cps5132", 68),
          ("kbps2208Cps5207", 69),
          ("kbps2240Cps5283", 70),
          ("kbps224Cps528", 7),
          ("kbps2272Cps5358", 71),
          ("kbps2304Cps5433", 72),
          ("kbps2336Cps5509", 73),
          ("kbps2368Cps5584", 74),
          ("kbps2400Cps5660", 75),
          ("kbps2432Cps5735", 76),
          ("kbps2464Cps5811", 77),
          ("kbps2496Cps5886", 78),
          ("kbps2528Cps5962", 79),
          ("kbps2560Cps6037", 80),
          ("kbps256Cps603", 8),
          ("kbps2592Cps6113", 81),
          ("kbps2624Cps6188", 82),
          ("kbps2656Cps6264", 83),
          ("kbps2688Cps6339", 84),
          ("kbps2720Cps6415", 85),
          ("kbps2752Cps6490", 86),
          ("kbps2784Cps6566", 87),
          ("kbps2816Cps6641", 88),
          ("kbps2848Cps6716", 89),
          ("kbps2880Cps6792", 90),
          ("kbps288Cps679", 9),
          ("kbps2912Cps6867", 91),
          ("kbps2944Cps6943", 92),
          ("kbps2976Cps7018", 93),
          ("kbps3008Cps7094", 94),
          ("kbps3040Cps7169", 95),
          ("kbps3072Cps7245", 96),
          ("kbps3104Cps7320", 97),
          ("kbps3136Cps7396", 98),
          ("kbps3168Cps7471", 99),
          ("kbps3200Cps7547", 100),
          ("kbps320Cps754", 10),
          ("kbps3232Cps7622", 101),
          ("kbps3264Cps7698", 102),
          ("kbps3296Cps7773", 103),
          ("kbps32Cps75", 1),
          ("kbps3328Cps7849", 104),
          ("kbps3360Cps7924", 105),
          ("kbps3392Cps8000", 106),
          ("kbps3424Cps8075", 107),
          ("kbps3456Cps8150", 108),
          ("kbps3488Cps8226", 109),
          ("kbps3520Cps8301", 110),
          ("kbps352Cps830", 11),
          ("kbps3552Cps8377", 111),
          ("kbps3584Cps8452", 112),
          ("kbps3616Cps8528", 113),
          ("kbps3648Cps8603", 114),
          ("kbps3680Cps8679", 115),
          ("kbps3712Cps8754", 116),
          ("kbps3744Cps8830", 117),
          ("kbps3776Cps8905", 118),
          ("kbps3808Cps8981", 119),
          ("kbps3840Cps9056", 120),
          ("kbps384Cps905", 12),
          ("kbps3872Cps9132", 121),
          ("kbps3904Cps9207", 122),
          ("kbps3936Cps9283", 123),
          ("kbps3968Cps9358", 124),
          ("kbps4000Cps9433", 125),
          ("kbps4032Cps9509", 126),
          ("kbps4064Cps9584", 127),
          ("kbps4096Cps9660", 128),
          ("kbps4128Cps9735", 129),
          ("kbps4160Cps9811", 130),
          ("kbps416Cps981", 13),
          ("kbps4192Cps9886", 131),
          ("kbps4224Cps9962", 132),
          ("kbps4256Cps10037", 133),
          ("kbps4288Cps10113", 134),
          ("kbps4320Cps10188", 135),
          ("kbps4352Cps10264", 136),
          ("kbps4384Cps10339", 137),
          ("kbps4416Cps10415", 138),
          ("kbps4448Cps10490", 139),
          ("kbps4480Cps10566", 140),
          ("kbps448Cps1056", 14),
          ("kbps4512Cps10641", 141),
          ("kbps4544Cps10716", 142),
          ("kbps4576Cps10792", 143),
          ("kbps4608Cps10867", 144),
          ("kbps4640Cps10943", 145),
          ("kbps4672Cps11018", 146),
          ("kbps4704Cps11094", 147),
          ("kbps4736Cps11169", 148),
          ("kbps4768Cps11245", 149),
          ("kbps4800Cps11320", 150),
          ("kbps480Cps1132", 15),
          ("kbps4832Cps11396", 151),
          ("kbps4864Cps11471", 152),
          ("kbps4896Cps11547", 153),
          ("kbps4928Cps11622", 154),
          ("kbps4960Cps11698", 155),
          ("kbps4992Cps11773", 156),
          ("kbps5024Cps11849", 157),
          ("kbps5056Cps11924", 158),
          ("kbps5088Cps12000", 159),
          ("kbps5120Cps12075", 160),
          ("kbps512Cps1207", 16),
          ("kbps5152Cps12150", 161),
          ("kbps5184Cps12226", 162),
          ("kbps5216Cps12301", 163),
          ("kbps5248Cps12377", 164),
          ("kbps5280Cps12452", 165),
          ("kbps5312Cps12528", 166),
          ("kbps5344Cps12603", 167),
          ("kbps5376Cps12679", 168),
          ("kbps5408Cps12754", 169),
          ("kbps5440Cps12830", 170),
          ("kbps544Cps1283", 17),
          ("kbps5472Cps12905", 171),
          ("kbps5504Cps12981", 172),
          ("kbps5536Cps13056", 173),
          ("kbps5568Cps13132", 174),
          ("kbps5600Cps13207", 175),
          ("kbps5632Cps13283", 176),
          ("kbps5664Cps13358", 177),
          ("kbps5696Cps13433", 178),
          ("kbps5728Cps13509", 179),
          ("kbps5760Cps13584", 180),
          ("kbps576Cps1358", 18),
          ("kbps5792Cps13660", 181),
          ("kbps5824Cps13735", 182),
          ("kbps5856Cps13811", 183),
          ("kbps5888Cps13886", 184),
          ("kbps5920Cps13962", 185),
          ("kbps5952Cps14037", 186),
          ("kbps5984Cps14113", 187),
          ("kbps6016Cps14188", 188),
          ("kbps6048Cps14264", 189),
          ("kbps6080Cps14339", 190),
          ("kbps608Cps1433", 19),
          ("kbps6112Cps14415", 191),
          ("kbps6144Cps14490", 192),
          ("kbps6176Cps14566", 193),
          ("kbps6208Cps14641", 194),
          ("kbps6240Cps14716", 195),
          ("kbps6272Cps14792", 196),
          ("kbps6304Cps14867", 197),
          ("kbps6336Cps14943", 198),
          ("kbps6368Cps15018", 199),
          ("kbps6400Cps15094", 200),
          ("kbps640Cps1509", 20),
          ("kbps6432Cps15169", 201),
          ("kbps6464Cps15245", 202),
          ("kbps6496Cps15320", 203),
          ("kbps64Cps150", 2),
          ("kbps6528Cps15396", 204),
          ("kbps6560Cps15471", 205),
          ("kbps6592Cps15547", 206),
          ("kbps6624Cps15622", 207),
          ("kbps6656Cps15698", 208),
          ("kbps6688Cps15773", 209),
          ("kbps6720Cps15849", 210),
          ("kbps672Cps1584", 21),
          ("kbps6752Cps15924", 211),
          ("kbps6784Cps16000", 212),
          ("kbps6816Cps16075", 213),
          ("kbps6848Cps16150", 214),
          ("kbps6880Cps16226", 215),
          ("kbps6912Cps16301", 216),
          ("kbps6944Cps16377", 217),
          ("kbps6976Cps16452", 218),
          ("kbps7008Cps16528", 219),
          ("kbps7040Cps16603", 220),
          ("kbps704Cps1660", 22),
          ("kbps7072Cps16679", 221),
          ("kbps7104Cps16754", 222),
          ("kbps7136Cps16830", 223),
          ("kbps7168Cps16905", 224),
          ("kbps7200Cps16981", 225),
          ("kbps7232Cps17056", 226),
          ("kbps7264Cps17132", 227),
          ("kbps7296Cps17207", 228),
          ("kbps7328Cps17283", 229),
          ("kbps7360Cps17358", 230),
          ("kbps736Cps1735", 23),
          ("kbps7392Cps17433", 231),
          ("kbps7424Cps17509", 232),
          ("kbps7456Cps17584", 233),
          ("kbps7488Cps17660", 234),
          ("kbps7520Cps17735", 235),
          ("kbps7552Cps17811", 236),
          ("kbps7584Cps17886", 237),
          ("kbps7616Cps17962", 238),
          ("kbps7648Cps18037", 239),
          ("kbps7680Cps18113", 240),
          ("kbps768Cps1811", 24),
          ("kbps7712Cps18188", 241),
          ("kbps7744Cps18264", 242),
          ("kbps7776Cps18339", 243),
          ("kbps7808Cps18415", 244),
          ("kbps7840Cps18490", 245),
          ("kbps7872Cps18566", 246),
          ("kbps7904Cps18641", 247),
          ("kbps7936Cps18716", 248),
          ("kbps7968Cps18792", 249),
          ("kbps8000Cps18867", 250),
          ("kbps800Cps1886", 25),
          ("kbps8032Cps18943", 251),
          ("kbps8064Cps19018", 252),
          ("kbps8096Cps19094", 253),
          ("kbps832Cps1962", 26),
          ("kbps864Cps2037", 27),
          ("kbps896Cps2113", 28),
          ("kbps928Cps2188", 29),
          ("kbps960Cps2264", 30),
          ("kbps96Cps226", 3),
          ("kbps992Cps2339", 31))
    )





class Xldv20AdslDataRateUp(Integer32):
    """Custom type Xldv20AdslDataRateUp based on Integer32"""
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
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("kbps128Cps301", 4),
          ("kbps160Cps377", 5),
          ("kbps192Cps452", 6),
          ("kbps224Cps528", 7),
          ("kbps256Cps603", 8),
          ("kbps288Cps679", 9),
          ("kbps320Cps754", 10),
          ("kbps32Cps75", 1),
          ("kbps352Cps830", 11),
          ("kbps384Cps905", 12),
          ("kbps416Cps981", 13),
          ("kbps448Cps1056", 14),
          ("kbps480Cps1132", 15),
          ("kbps512Cps1207", 16),
          ("kbps544Cps1283", 17),
          ("kbps576Cps1358", 18),
          ("kbps608Cps1433", 19),
          ("kbps640Cps1509", 20),
          ("kbps64Cps150", 2),
          ("kbps672Cps1584", 21),
          ("kbps704Cps1660", 22),
          ("kbps736Cps1735", 23),
          ("kbps768Cps1811", 24),
          ("kbps96Cps226", 3))
    )





class Xldv20AdslDataRateDownCurrent(Integer32):
    """Custom type Xldv20AdslDataRateDownCurrent based on Integer32"""
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
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
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
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              212,
              213,
              214,
              215,
              216,
              217,
              218,
              219,
              220,
              221,
              222,
              223,
              224,
              225,
              226,
              227,
              228,
              229,
              230,
              231,
              232,
              233,
              234,
              235,
              236,
              237,
              238,
              239,
              240,
              241,
              242,
              243,
              244,
              245,
              246,
              247,
              248,
              249,
              250,
              251,
              252,
              253,
              32767)
        )
    )
    namedValues = NamedValues(
        *(("kbps1024Cps2415", 32),
          ("kbps1056Cps2490", 33),
          ("kbps1088Cps2566", 34),
          ("kbps1120Cps2641", 35),
          ("kbps1152Cps2716", 36),
          ("kbps1184Cps2792", 37),
          ("kbps1216Cps2867", 38),
          ("kbps1248Cps2943", 39),
          ("kbps1280Cps3018", 40),
          ("kbps128Cps301", 4),
          ("kbps1312Cps3094", 41),
          ("kbps1344Cps3169", 42),
          ("kbps1376Cps3245", 43),
          ("kbps1408Cps3320", 44),
          ("kbps1440Cps3396", 45),
          ("kbps1472Cps3471", 46),
          ("kbps1504Cps3547", 47),
          ("kbps1536Cps3622", 48),
          ("kbps1568Cps3698", 49),
          ("kbps1600Cps3773", 50),
          ("kbps160Cps377", 5),
          ("kbps1632Cps3849", 51),
          ("kbps1664Cps3924", 52),
          ("kbps1696Cps4000", 53),
          ("kbps1728Cps4075", 54),
          ("kbps1760Cps4150", 55),
          ("kbps1792Cps4226", 56),
          ("kbps1824Cps4301", 57),
          ("kbps1856Cps4377", 58),
          ("kbps1888Cps4452", 59),
          ("kbps1920Cps4528", 60),
          ("kbps192Cps452", 6),
          ("kbps1952Cps4603", 61),
          ("kbps1984Cps4679", 62),
          ("kbps2016Cps4754", 63),
          ("kbps2048Cps4830", 64),
          ("kbps2080Cps4905", 65),
          ("kbps2112Cps4981", 66),
          ("kbps2144Cps5056", 67),
          ("kbps2176Cps5132", 68),
          ("kbps2208Cps5207", 69),
          ("kbps2240Cps5283", 70),
          ("kbps224Cps528", 7),
          ("kbps2272Cps5358", 71),
          ("kbps2304Cps5433", 72),
          ("kbps2336Cps5509", 73),
          ("kbps2368Cps5584", 74),
          ("kbps2400Cps5660", 75),
          ("kbps2432Cps5735", 76),
          ("kbps2464Cps5811", 77),
          ("kbps2496Cps5886", 78),
          ("kbps2528Cps5962", 79),
          ("kbps2560Cps6037", 80),
          ("kbps256Cps603", 8),
          ("kbps2592Cps6113", 81),
          ("kbps2624Cps6188", 82),
          ("kbps2656Cps6264", 83),
          ("kbps2688Cps6339", 84),
          ("kbps2720Cps6415", 85),
          ("kbps2752Cps6490", 86),
          ("kbps2784Cps6566", 87),
          ("kbps2816Cps6641", 88),
          ("kbps2848Cps6716", 89),
          ("kbps2880Cps6792", 90),
          ("kbps288Cps679", 9),
          ("kbps2912Cps6867", 91),
          ("kbps2944Cps6943", 92),
          ("kbps2976Cps7018", 93),
          ("kbps3008Cps7094", 94),
          ("kbps3040Cps7169", 95),
          ("kbps3072Cps7245", 96),
          ("kbps3104Cps7320", 97),
          ("kbps3136Cps7396", 98),
          ("kbps3168Cps7471", 99),
          ("kbps3200Cps7547", 100),
          ("kbps320Cps754", 10),
          ("kbps3232Cps7622", 101),
          ("kbps3264Cps7698", 102),
          ("kbps3296Cps7773", 103),
          ("kbps32Cps75", 1),
          ("kbps3328Cps7849", 104),
          ("kbps3360Cps7924", 105),
          ("kbps3392Cps8000", 106),
          ("kbps3424Cps8075", 107),
          ("kbps3456Cps8150", 108),
          ("kbps3488Cps8226", 109),
          ("kbps3520Cps8301", 110),
          ("kbps352Cps830", 11),
          ("kbps3552Cps8377", 111),
          ("kbps3584Cps8452", 112),
          ("kbps3616Cps8528", 113),
          ("kbps3648Cps8603", 114),
          ("kbps3680Cps8679", 115),
          ("kbps3712Cps8754", 116),
          ("kbps3744Cps8830", 117),
          ("kbps3776Cps8905", 118),
          ("kbps3808Cps8981", 119),
          ("kbps3840Cps9056", 120),
          ("kbps384Cps905", 12),
          ("kbps3872Cps9132", 121),
          ("kbps3904Cps9207", 122),
          ("kbps3936Cps9283", 123),
          ("kbps3968Cps9358", 124),
          ("kbps4000Cps9433", 125),
          ("kbps4032Cps9509", 126),
          ("kbps4064Cps9584", 127),
          ("kbps4096Cps9660", 128),
          ("kbps4128Cps9735", 129),
          ("kbps4160Cps9811", 130),
          ("kbps416Cps981", 13),
          ("kbps4192Cps9886", 131),
          ("kbps4224Cps9962", 132),
          ("kbps4256Cps10037", 133),
          ("kbps4288Cps10113", 134),
          ("kbps4320Cps10188", 135),
          ("kbps4352Cps10264", 136),
          ("kbps4384Cps10339", 137),
          ("kbps4416Cps10415", 138),
          ("kbps4448Cps10490", 139),
          ("kbps4480Cps10566", 140),
          ("kbps448Cps1056", 14),
          ("kbps4512Cps10641", 141),
          ("kbps4544Cps10716", 142),
          ("kbps4576Cps10792", 143),
          ("kbps4608Cps10867", 144),
          ("kbps4640Cps10943", 145),
          ("kbps4672Cps11018", 146),
          ("kbps4704Cps11094", 147),
          ("kbps4736Cps11169", 148),
          ("kbps4768Cps11245", 149),
          ("kbps4800Cps11320", 150),
          ("kbps480Cps1132", 15),
          ("kbps4832Cps11396", 151),
          ("kbps4864Cps11471", 152),
          ("kbps4896Cps11547", 153),
          ("kbps4928Cps11622", 154),
          ("kbps4960Cps11698", 155),
          ("kbps4992Cps11773", 156),
          ("kbps5024Cps11849", 157),
          ("kbps5056Cps11924", 158),
          ("kbps5088Cps12000", 159),
          ("kbps5120Cps12075", 160),
          ("kbps512Cps1207", 16),
          ("kbps5152Cps12150", 161),
          ("kbps5184Cps12226", 162),
          ("kbps5216Cps12301", 163),
          ("kbps5248Cps12377", 164),
          ("kbps5280Cps12452", 165),
          ("kbps5312Cps12528", 166),
          ("kbps5344Cps12603", 167),
          ("kbps5376Cps12679", 168),
          ("kbps5408Cps12754", 169),
          ("kbps5440Cps12830", 170),
          ("kbps544Cps1283", 17),
          ("kbps5472Cps12905", 171),
          ("kbps5504Cps12981", 172),
          ("kbps5536Cps13056", 173),
          ("kbps5568Cps13132", 174),
          ("kbps5600Cps13207", 175),
          ("kbps5632Cps13283", 176),
          ("kbps5664Cps13358", 177),
          ("kbps5696Cps13433", 178),
          ("kbps5728Cps13509", 179),
          ("kbps5760Cps13584", 180),
          ("kbps576Cps1358", 18),
          ("kbps5792Cps13660", 181),
          ("kbps5824Cps13735", 182),
          ("kbps5856Cps13811", 183),
          ("kbps5888Cps13886", 184),
          ("kbps5920Cps13962", 185),
          ("kbps5952Cps14037", 186),
          ("kbps5984Cps14113", 187),
          ("kbps6016Cps14188", 188),
          ("kbps6048Cps14264", 189),
          ("kbps6080Cps14339", 190),
          ("kbps608Cps1433", 19),
          ("kbps6112Cps14415", 191),
          ("kbps6144Cps14490", 192),
          ("kbps6176Cps14566", 193),
          ("kbps6208Cps14641", 194),
          ("kbps6240Cps14716", 195),
          ("kbps6272Cps14792", 196),
          ("kbps6304Cps14867", 197),
          ("kbps6336Cps14943", 198),
          ("kbps6368Cps15018", 199),
          ("kbps6400Cps15094", 200),
          ("kbps640Cps1509", 20),
          ("kbps6432Cps15169", 201),
          ("kbps6464Cps15245", 202),
          ("kbps6496Cps15320", 203),
          ("kbps64Cps150", 2),
          ("kbps6528Cps15396", 204),
          ("kbps6560Cps15471", 205),
          ("kbps6592Cps15547", 206),
          ("kbps6624Cps15622", 207),
          ("kbps6656Cps15698", 208),
          ("kbps6688Cps15773", 209),
          ("kbps6720Cps15849", 210),
          ("kbps672Cps1584", 21),
          ("kbps6752Cps15924", 211),
          ("kbps6784Cps16000", 212),
          ("kbps6816Cps16075", 213),
          ("kbps6848Cps16150", 214),
          ("kbps6880Cps16226", 215),
          ("kbps6912Cps16301", 216),
          ("kbps6944Cps16377", 217),
          ("kbps6976Cps16452", 218),
          ("kbps7008Cps16528", 219),
          ("kbps7040Cps16603", 220),
          ("kbps704Cps1660", 22),
          ("kbps7072Cps16679", 221),
          ("kbps7104Cps16754", 222),
          ("kbps7136Cps16830", 223),
          ("kbps7168Cps16905", 224),
          ("kbps7200Cps16981", 225),
          ("kbps7232Cps17056", 226),
          ("kbps7264Cps17132", 227),
          ("kbps7296Cps17207", 228),
          ("kbps7328Cps17283", 229),
          ("kbps7360Cps17358", 230),
          ("kbps736Cps1735", 23),
          ("kbps7392Cps17433", 231),
          ("kbps7424Cps17509", 232),
          ("kbps7456Cps17584", 233),
          ("kbps7488Cps17660", 234),
          ("kbps7520Cps17735", 235),
          ("kbps7552Cps17811", 236),
          ("kbps7584Cps17886", 237),
          ("kbps7616Cps17962", 238),
          ("kbps7648Cps18037", 239),
          ("kbps7680Cps18113", 240),
          ("kbps768Cps1811", 24),
          ("kbps7712Cps18188", 241),
          ("kbps7744Cps18264", 242),
          ("kbps7776Cps18339", 243),
          ("kbps7808Cps18415", 244),
          ("kbps7840Cps18490", 245),
          ("kbps7872Cps18566", 246),
          ("kbps7904Cps18641", 247),
          ("kbps7936Cps18716", 248),
          ("kbps7968Cps18792", 249),
          ("kbps8000Cps18867", 250),
          ("kbps800Cps1886", 25),
          ("kbps8032Cps18943", 251),
          ("kbps8064Cps19018", 252),
          ("kbps8096Cps19094", 253),
          ("kbps832Cps1962", 26),
          ("kbps864Cps2037", 27),
          ("kbps896Cps2113", 28),
          ("kbps928Cps2188", 29),
          ("kbps960Cps2264", 30),
          ("kbps96Cps226", 3),
          ("kbps992Cps2339", 31),
          ("rateInvalid", 32767))
    )





class Xldv20AdslDataRateUpCurrent(Integer32):
    """Custom type Xldv20AdslDataRateUpCurrent based on Integer32"""
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
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              32767)
        )
    )
    namedValues = NamedValues(
        *(("kbps128Cps301", 4),
          ("kbps160Cps377", 5),
          ("kbps192Cps452", 6),
          ("kbps224Cps528", 7),
          ("kbps256Cps603", 8),
          ("kbps288Cps679", 9),
          ("kbps320Cps754", 10),
          ("kbps32Cps75", 1),
          ("kbps352Cps830", 11),
          ("kbps384Cps905", 12),
          ("kbps416Cps981", 13),
          ("kbps448Cps1056", 14),
          ("kbps480Cps1132", 15),
          ("kbps512Cps1207", 16),
          ("kbps544Cps1283", 17),
          ("kbps576Cps1358", 18),
          ("kbps608Cps1433", 19),
          ("kbps640Cps1509", 20),
          ("kbps64Cps150", 2),
          ("kbps672Cps1584", 21),
          ("kbps704Cps1660", 22),
          ("kbps736Cps1735", 23),
          ("kbps768Cps1811", 24),
          ("kbps96Cps226", 3),
          ("rateInvalid", 32767))
    )





class Xldv20SdslDataRate(Integer32):
    """Custom type Xldv20SdslDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              24,
              25,
              36,
              37,
              48,
              49,
              54,
              72)
        )
    )
    namedValues = NamedValues(
        *(("kbps1152Cps2716", 36),
          ("kbps1168Cps2754", 37),
          ("kbps1536Cps3622", 48),
          ("kbps1552Cps3660", 49),
          ("kbps160Cps377", 5),
          ("kbps1744Cps4113", 54),
          ("kbps192Cps452", 6),
          ("kbps208Cps490", 7),
          ("kbps2320Cps5471", 72),
          ("kbps256Cps603", 8),
          ("kbps288Cps679", 9),
          ("kbps320Cps754", 10),
          ("kbps352Cps830", 11),
          ("kbps384Cps905", 12),
          ("kbps400Cps943", 13),
          ("kbps768Cps1811", 24),
          ("kbps784Cps1849", 25))
    )





class Xldv20SdslDataRateCurrent(Integer32):
    """Custom type Xldv20SdslDataRateCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              24,
              25,
              36,
              37,
              48,
              49,
              54,
              72,
              32767)
        )
    )
    namedValues = NamedValues(
        *(("kbps1152Cps2716", 36),
          ("kbps1168Cps2754", 37),
          ("kbps1536Cps3622", 48),
          ("kbps1552Cps3660", 49),
          ("kbps160Cps377", 5),
          ("kbps1744Cps4113", 54),
          ("kbps192Cps452", 6),
          ("kbps208Cps490", 7),
          ("kbps2320Cps5471", 72),
          ("kbps256Cps603", 8),
          ("kbps288Cps679", 9),
          ("kbps320Cps754", 10),
          ("kbps352Cps830", 11),
          ("kbps384Cps905", 12),
          ("kbps400Cps943", 13),
          ("kbps768Cps1811", 24),
          ("kbps784Cps1849", 25),
          ("rateInvalid", 32767))
    )





class Xldv20ControlReq(Integer32):
    """Custom type Xldv20ControlReq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              11,
              12,
              13,
              14,
              15,
              16,
              1000,
              1051,
              1052,
              1053,
              1054,
              1055,
              1056,
              1057,
              2001,
              2002,
              2003,
              2004,
              2005,
              2006,
              2007,
              2008,
              2009,
              2010,
              2011,
              2012,
              2013,
              2100,
              2101,
              2102,
              2103,
              2106,
              2107,
              2108,
              2109,
              2110,
              2114,
              2115,
              2116,
              2117,
              2118,
              2119,
              2120,
              2121,
              2122,
              2123,
              2132,
              2133,
              2134,
              2135,
              2136,
              2137,
              2138,
              2140,
              2141,
              2142,
              2143,
              2144,
              2150,
              2151,
              2152,
              2153,
              2200,
              2251,
              2252,
              2253,
              2254,
              2255,
              2256,
              2257,
              2300,
              2351,
              2352,
              2353,
              2354,
              2355,
              2356,
              2400,
              2451,
              2452,
              2453,
              2551,
              2552,
              2553,
              2554,
              2555,
              2556,
              2557,
              2558,
              2559,
              2560,
              2561,
              2562,
              2563,
              3000,
              3001,
              3002,
              3100,
              3101,
              3102,
              3103,
              3104,
              3105,
              3106,
              3107,
              3108,
              3109,
              3110,
              3111,
              3112,
              3113,
              3114,
              3115,
              3116,
              4000,
              4001,
              5000,
              5119,
              5150,
              5151,
              5152,
              5153,
              5154,
              5155,
              5156,
              5157,
              5158,
              5161,
              5162,
              5500,
              5600,
              5901,
              5902,
              6000,
              6211,
              6213,
              6214,
              6300,
              6301,
              6302,
              6303,
              6353,
              6354,
              6355,
              6356,
              6980,
              7000,
              7081,
              7082,
              7083,
              7084,
              8000,
              8001,
              8003,
              8004,
              8006,
              8050,
              8051,
              8052,
              8053,
              8054,
              8320,
              8321,
              8322,
              8323,
              8324,
              8325,
              8326,
              8327,
              8328,
              8329,
              8330,
              8331,
              8332,
              8333,
              8334,
              8335,
              8336,
              8337,
              8400,
              8401,
              8402,
              8404,
              8408,
              8416,
              8432,
              8464,
              9000,
              9050,
              9051,
              9052,
              9053,
              9054,
              9055,
              9100,
              9101,
              9102,
              9103,
              9104,
              9105,
              9106,
              9107,
              9108,
              9109,
              9200,
              9201,
              9202,
              9203)
        )
    )
    namedValues = NamedValues(
        *(("actCellDelayVariationDownstreamFaulty", 2109),
          ("actCellDelayVariationUpstreamFaulty", 2108),
          ("actControlReqFaulty", 2103),
          ("actEthVpcTpDeletionNotAllowed", 2257),
          ("actLineBlocked", 2122),
          ("actMBSDownstreamFaulty", 2117),
          ("actMBSUpstreamFaulty", 2116),
          ("actMaxCcsPerPortExceeded", 2140),
          ("actMaxNrOfCcsInDbExceeded", 2143),
          ("actMaxNrOfCcsOnHwExceeded", 2144),
          ("actMaxNumberOfVcsToSmall", 2141),
          ("actNumberOfVcsFaulty", 2136),
          ("actPeakCellRateDownstreamFaulty", 2107),
          ("actPeakCellRateUpstreamFaulty", 2106),
          ("actPortLocationIdFaulty", 2102),
          ("actSCRDownstreamFaulty", 2115),
          ("actSCRUpstreamFaulty", 2114),
          ("actSegmentEndPointNniFaulty", 2134),
          ("actSegmentEndPointNtFaulty", 2142),
          ("actSegmentEndPointUniFaulty", 2133),
          ("actTrafficDirectionFaulty", 2119),
          ("actTrafficTypeFaulty", 2110),
          ("actVbrCDVTDownstreamFaulty", 2138),
          ("actVbrCDVTUpstreamFaulty", 2137),
          ("actVciNniFaulty", 2120),
          ("actVciUniFaulty", 2121),
          ("actVclCCExists", 2135),
          ("actVpcTpExists", 2123),
          ("actVpcTpNotExisting", 2118),
          ("actVpiNniFaulty", 2100),
          ("actVpiUniFaulty", 2101),
          ("actWrongLiType", 2132),
          ("activateData", 5000),
          ("aswTimeout", 14),
          ("backupDb", 9000),
          ("bandwidthDownstreamWarning", 5157),
          ("bandwidthUpstreamWarning", 5156),
          ("cacBwOverflowDown", 2552),
          ("cacBwOverflowUp", 2551),
          ("cacBwWarningDown", 2559),
          ("cacBwWarningUp", 2558),
          ("cacInternalError", 2563),
          ("cacLineBlockedByTlm", 2553),
          ("cacMbsOverflowDown", 2557),
          ("cacMbsOverflowUp", 2556),
          ("cacMbsScrError", 2562),
          ("cacMbsWarningDown", 2561),
          ("cacMbsWarningUp", 2560),
          ("cacTrafficDirectionConflict", 2555),
          ("cacTrafficTypeConflict", 2554),
          ("ccExists", 2151),
          ("changeHwUnitForced", 3002),
          ("cold", 6301),
          ("commExecStarted", 5),
          ("commandFailed", 15),
          ("commandSucceeded", 16),
          ("configEth", 2200),
          ("configEthFailed", 2251),
          ("configInbandTmn", 2400),
          ("configInbandTmnFailed", 2451),
          ("continuityCheckAlreadyDisabled", 2352),
          ("continuityCheckAlreadyEnabled", 2351),
          ("continuityCheckNotSupportedOnNt", 2355),
          ("continuityCheckReject", 2353),
          ("continuityCheckRequest", 2300),
          ("continuityCheckTestTypeConflict", 2354),
          ("continuityCheckTrafficDirectionConflict", 2356),
          ("createEthVclCC", 2011),
          ("createEthVpcTp", 2007),
          ("createEthVplCC", 2003),
          ("createHwUnit", 3000),
          ("createVclCC", 2009),
          ("createVpcTp", 2005),
          ("createVplCC", 2001),
          ("dbReadFailed", 9055),
          ("dbReload", 6303),
          ("dbmDbReadFailed", 9105),
          ("dbmFlashAccessFailed", 9104),
          ("dbmLocalBackupFailed", 9102),
          ("dbmLocalBackupFileFaulty", 9106),
          ("dbmLocalBackupOk", 9100),
          ("dbmRemoteBackupFailed", 9103),
          ("dbmRemoteBackupFileFaulty", 9107),
          ("dbmRemoteBackupOk", 9101),
          ("dbmRestoreFailed", 9108),
          ("dbmRestoreOk", 9109),
          ("dbuFileCreationFailed", 7083),
          ("dbuFileTransmissionFailed", 7084),
          ("dbuReadComplete", 7081),
          ("dbuReadFailed", 7082),
          ("dbuReadRequest", 7000),
          ("deleteEthVclCC", 2012),
          ("deleteEthVpcTp", 2008),
          ("deleteEthVplCC", 2004),
          ("deleteHwUnit", 3001),
          ("deleteVclCC", 2010),
          ("deleteVpcTp", 2006),
          ("deleteVplCC", 2002),
          ("ethModeInvalid", 2252),
          ("ethVciPeakCellRateUpstreamFaulty", 2256),
          ("ethVciTrafficTypeFaulty", 2255),
          ("ethVciUniNotExisting", 2254),
          ("ethVpiUniNotExisting", 2253),
          ("flashAccessFailed", 9054),
          ("hwuCcExisting", 3114),
          ("hwuCommandFailed", 3101),
          ("hwuContainingUnitNotAvail", 3107),
          ("hwuCreateHwUnitComplete", 3113),
          ("hwuEqhTypeNotAvail", 3104),
          ("hwuEquTypeNotAvail", 3103),
          ("hwuForcedChangeNotAllowed", 3115),
          ("hwuObjExists", 3102),
          ("hwuObjNotAvail", 3108),
          ("hwuObjNotEmpty", 3109),
          ("hwuObjNotLocked", 3110),
          ("hwuObjNotValid", 3111),
          ("hwuOk", 3112),
          ("hwuParamFaulty", 3100),
          ("hwuPiuTypeNotAccepted", 3106),
          ("hwuPiuTypeNotAvail", 3105),
          ("hwuUpgradeRunning", 3116),
          ("imaBwError", 9201),
          ("imaSetMinNumFailed", 9203),
          ("imaSetMinNumOk", 9202),
          ("imaSetMinNumTxLinks", 9200),
          ("inbandVciExists", 2453),
          ("inbandVpiExists", 2452),
          ("lineNotEnabled", 2150),
          ("localBackupFailed", 9052),
          ("localBackupOk", 9050),
          ("loopDiagRequest", 5500),
          ("loopTestBusy", 5902),
          ("loopTestReject", 5901),
          ("loopTestRequest", 5600),
          ("mbsDownstreamWarning", 5119),
          ("mbsUpstreamWarning", 5158),
          ("modifyNumberOfVcs", 2013),
          ("noCurrentAlarms", 6214),
          ("noRequest", 1),
          ("paramFaulty", 11),
          ("reload", 6302),
          ("remoteBackupFailed", 9053),
          ("remoteBackupOk", 9051),
          ("requestBusy", 12),
          ("resourceProblem", 5150),
          ("resourceProblemDownstream", 5153),
          ("resourceProblemUpstream", 5152),
          ("riAllData", 4001),
          ("riSingleBoard", 4000),
          ("rjPiuNotAvail", 6355),
          ("rjResetNotSupported", 6356),
          ("rjRstRunning", 6354),
          ("rjUpgRunning", 6353),
          ("rstRequestFailed", 6980),
          ("setDataFailed", 13),
          ("snmFtpError", 1053),
          ("snmUpFtpAccountFailed", 1055),
          ("snmUpFtpDescPathFailed", 1057),
          ("snmUpFtpIpAddrFailed", 1054),
          ("snmUpFtpPasswdFailed", 1056),
          ("snmUpdateComplete", 1051),
          ("snmUpdateFailed", 1052),
          ("snmUpdateSnmpConfigFile", 1000),
          ("startSendingAlarms", 6213),
          ("sucActivateLoad", 8001),
          ("sucAlreadyLoaded", 8054),
          ("sucDbAccessFailed", 8322),
          ("sucDbBackupFault", 8335),
          ("sucFepromCopyFault", 8331),
          ("sucFtpCrcError", 8328),
          ("sucFtpSendError", 8334),
          ("sucFtpServerNoteAvailable", 8333),
          ("sucFtpTransError", 8327),
          ("sucGetSwVersions", 8004),
          ("sucGetSwVersionsFailed", 8052),
          ("sucNotOk", 8321),
          ("sucOk", 8320),
          ("sucPiuUnlocked", 8323),
          ("sucReadSAPSContentFile", 8003),
          ("sucSwHwMismatch", 8329),
          ("sucTransmissionError", 8324),
          ("sucUnitTypeMismatch", 8326),
          ("sucUpdateDescFileFailed", 8332),
          ("sucUpgrDbAccessFault", 8051),
          ("sucUpgrEndRequest", 8006),
          ("sucUpgrMissParameter", 8053),
          ("sucUpgrStartRequest", 8000),
          ("sucUpgrTaskCreationFault", 8050),
          ("sucUpgrWrongAvState", 8330),
          ("sucUpgradeComplete", 8336),
          ("sucUpgradeNotComplete", 8337),
          ("sucWrongSwVersion", 8325),
          ("sutCrashed", 8404),
          ("sutDone", 8416),
          ("sutFtpDone", 8408),
          ("sutInitialized", 8400),
          ("sutObsolete", 8464),
          ("sutReadyForReset", 8432),
          ("sutStarted", 8402),
          ("sutToDo", 8401),
          ("updateAlmList", 6000),
          ("updateFiltList", 6211),
          ("vciTrafficTypeInvalid", 2153),
          ("vpProblem", 5151),
          ("vpProblemDownstream", 5155),
          ("vpProblemUpstream", 5154),
          ("vpiUniNotExisting", 2152),
          ("warm", 6300),
          ("wrongAdminState", 5161),
          ("wrongXdslServiceType", 5162))
    )




# TEXTUAL-CONVENTIONS



class Unsigned16(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_Xldv20_ObjectIdentity = ObjectIdentity
xldv20 = _Xldv20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4)
)
_Xldv20SnmpMgmt_ObjectIdentity = ObjectIdentity
xldv20SnmpMgmt = _Xldv20SnmpMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 1)
)
_Xldv20SnmpControl_ObjectIdentity = ObjectIdentity
xldv20SnmpControl = _Xldv20SnmpControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 1, 1)
)
_Xldv20SnmTmnTrapFlowControl_Type = Xldv20SuppressionType
_Xldv20SnmTmnTrapFlowControl_Object = MibScalar
xldv20SnmTmnTrapFlowControl = _Xldv20SnmTmnTrapFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 1, 1, 1),
    _Xldv20SnmTmnTrapFlowControl_Type()
)
xldv20SnmTmnTrapFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20SnmTmnTrapFlowControl.setStatus("mandatory")
_Xldv20SnmLctTrapFlowControl_Type = Xldv20SuppressionType
_Xldv20SnmLctTrapFlowControl_Object = MibScalar
xldv20SnmLctTrapFlowControl = _Xldv20SnmLctTrapFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 1, 1, 2),
    _Xldv20SnmLctTrapFlowControl_Type()
)
xldv20SnmLctTrapFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20SnmLctTrapFlowControl.setStatus("mandatory")
_Xldv20SnmControlReq_Type = Xldv20ControlReq
_Xldv20SnmControlReq_Object = MibScalar
xldv20SnmControlReq = _Xldv20SnmControlReq_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 1, 1, 3),
    _Xldv20SnmControlReq_Type()
)
xldv20SnmControlReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20SnmControlReq.setStatus("mandatory")
_Xldv20SnmControlStatus_Type = Xldv20ControlStatus
_Xldv20SnmControlStatus_Object = MibScalar
xldv20SnmControlStatus = _Xldv20SnmControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 1, 1, 4),
    _Xldv20SnmControlStatus_Type()
)
xldv20SnmControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20SnmControlStatus.setStatus("mandatory")


class _Xldv20SnmLctConnected_Type(Integer32):
    """Custom type xldv20SnmLctConnected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Xldv20SnmLctConnected_Type.__name__ = "Integer32"
_Xldv20SnmLctConnected_Object = MibScalar
xldv20SnmLctConnected = _Xldv20SnmLctConnected_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 1, 1, 5),
    _Xldv20SnmLctConnected_Type()
)
xldv20SnmLctConnected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20SnmLctConnected.setStatus("mandatory")


class _Xldv20SnmTmnConnected_Type(Integer32):
    """Custom type xldv20SnmTmnConnected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Xldv20SnmTmnConnected_Type.__name__ = "Integer32"
_Xldv20SnmTmnConnected_Object = MibScalar
xldv20SnmTmnConnected = _Xldv20SnmTmnConnected_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 1, 1, 6),
    _Xldv20SnmTmnConnected_Type()
)
xldv20SnmTmnConnected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20SnmTmnConnected.setStatus("mandatory")
_Xldv20SnmMaxResponseTime_Type = Integer32
_Xldv20SnmMaxResponseTime_Object = MibScalar
xldv20SnmMaxResponseTime = _Xldv20SnmMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 1, 1, 7),
    _Xldv20SnmMaxResponseTime_Type()
)
xldv20SnmMaxResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20SnmMaxResponseTime.setStatus("mandatory")
_Xldv20SnmTmnMaxNumber_Type = Unsigned16
_Xldv20SnmTmnMaxNumber_Object = MibScalar
xldv20SnmTmnMaxNumber = _Xldv20SnmTmnMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 1, 1, 8),
    _Xldv20SnmTmnMaxNumber_Type()
)
xldv20SnmTmnMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20SnmTmnMaxNumber.setStatus("mandatory")
_Xldv20SnmTmnSpecificIndex_Type = Unsigned16
_Xldv20SnmTmnSpecificIndex_Object = MibScalar
xldv20SnmTmnSpecificIndex = _Xldv20SnmTmnSpecificIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 1, 1, 9),
    _Xldv20SnmTmnSpecificIndex_Type()
)
xldv20SnmTmnSpecificIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20SnmTmnSpecificIndex.setStatus("mandatory")
_Xldv20SnmCallpPollingFlag_Type = Xldv20PollingFlagType
_Xldv20SnmCallpPollingFlag_Object = MibScalar
xldv20SnmCallpPollingFlag = _Xldv20SnmCallpPollingFlag_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 1, 1, 10),
    _Xldv20SnmCallpPollingFlag_Type()
)
xldv20SnmCallpPollingFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20SnmCallpPollingFlag.setStatus("mandatory")
_Xldv20SnmLctSessionPollingFlag_Type = Xldv20PollingFlagType
_Xldv20SnmLctSessionPollingFlag_Object = MibScalar
xldv20SnmLctSessionPollingFlag = _Xldv20SnmLctSessionPollingFlag_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 1, 1, 11),
    _Xldv20SnmLctSessionPollingFlag_Type()
)
xldv20SnmLctSessionPollingFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20SnmLctSessionPollingFlag.setStatus("mandatory")
_Xldv20SnmControlReqResult_Type = Xldv20ControlReq
_Xldv20SnmControlReqResult_Object = MibScalar
xldv20SnmControlReqResult = _Xldv20SnmControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 1, 1, 12),
    _Xldv20SnmControlReqResult_Type()
)
xldv20SnmControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20SnmControlReqResult.setStatus("mandatory")
_Xldv20SnmStartupResult_Type = Xldv20StartupResult
_Xldv20SnmStartupResult_Object = MibScalar
xldv20SnmStartupResult = _Xldv20SnmStartupResult_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 1, 1, 13),
    _Xldv20SnmStartupResult_Type()
)
xldv20SnmStartupResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20SnmStartupResult.setStatus("mandatory")
_Xldv20SnmControlTimeStamp_Type = TimeTicks
_Xldv20SnmControlTimeStamp_Object = MibScalar
xldv20SnmControlTimeStamp = _Xldv20SnmControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 1, 1, 14),
    _Xldv20SnmControlTimeStamp_Type()
)
xldv20SnmControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20SnmControlTimeStamp.setStatus("mandatory")
_Xldv20TmnTable_Object = MibTable
xldv20TmnTable = _Xldv20TmnTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    xldv20TmnTable.setStatus("mandatory")
_Xldv20TmnEntry_Object = MibTableRow
xldv20TmnEntry = _Xldv20TmnEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 1, 2, 1)
)
xldv20TmnEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20TmnIndex"),
)
if mibBuilder.loadTexts:
    xldv20TmnEntry.setStatus("mandatory")


class _Xldv20TmnIndex_Type(Integer32):
    """Custom type xldv20TmnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_Xldv20TmnIndex_Type.__name__ = "Integer32"
_Xldv20TmnIndex_Object = MibTableColumn
xldv20TmnIndex = _Xldv20TmnIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 1, 2, 1, 1),
    _Xldv20TmnIndex_Type()
)
xldv20TmnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20TmnIndex.setStatus("mandatory")
_Xldv20TmnOrLctTerminal_Type = Xldv20TerminalType
_Xldv20TmnOrLctTerminal_Object = MibTableColumn
xldv20TmnOrLctTerminal = _Xldv20TmnOrLctTerminal_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 1, 2, 1, 2),
    _Xldv20TmnOrLctTerminal_Type()
)
xldv20TmnOrLctTerminal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20TmnOrLctTerminal.setStatus("mandatory")
_Xldv20TmnInOrOutBand_Type = Xldv20ChannelType
_Xldv20TmnInOrOutBand_Object = MibTableColumn
xldv20TmnInOrOutBand = _Xldv20TmnInOrOutBand_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 1, 2, 1, 3),
    _Xldv20TmnInOrOutBand_Type()
)
xldv20TmnInOrOutBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20TmnInOrOutBand.setStatus("mandatory")


class _Xldv20TmnConnected_Type(Integer32):
    """Custom type xldv20TmnConnected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Xldv20TmnConnected_Type.__name__ = "Integer32"
_Xldv20TmnConnected_Object = MibTableColumn
xldv20TmnConnected = _Xldv20TmnConnected_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 1, 2, 1, 4),
    _Xldv20TmnConnected_Type()
)
xldv20TmnConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20TmnConnected.setStatus("mandatory")
_Xldv20TmnTrapFlowControl_Type = Xldv20SuppressionType
_Xldv20TmnTrapFlowControl_Object = MibTableColumn
xldv20TmnTrapFlowControl = _Xldv20TmnTrapFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 1, 2, 1, 5),
    _Xldv20TmnTrapFlowControl_Type()
)
xldv20TmnTrapFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20TmnTrapFlowControl.setStatus("mandatory")
_Xldv20TmnLctSessionPollingFlag_Type = Xldv20PollingFlagType
_Xldv20TmnLctSessionPollingFlag_Object = MibTableColumn
xldv20TmnLctSessionPollingFlag = _Xldv20TmnLctSessionPollingFlag_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 1, 2, 1, 6),
    _Xldv20TmnLctSessionPollingFlag_Type()
)
xldv20TmnLctSessionPollingFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20TmnLctSessionPollingFlag.setStatus("mandatory")
_Xldv20CallP_ObjectIdentity = ObjectIdentity
xldv20CallP = _Xldv20CallP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2)
)
_Xldv20AtmCcControl_ObjectIdentity = ObjectIdentity
xldv20AtmCcControl = _Xldv20AtmCcControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 1)
)
_Xldv20ActOperationalState_Type = Xldv20OperState
_Xldv20ActOperationalState_Object = MibScalar
xldv20ActOperationalState = _Xldv20ActOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 1, 1),
    _Xldv20ActOperationalState_Type()
)
xldv20ActOperationalState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20ActOperationalState.setStatus("mandatory")
_Xldv20ActControlReq_Type = Xldv20ControlReq
_Xldv20ActControlReq_Object = MibScalar
xldv20ActControlReq = _Xldv20ActControlReq_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 1, 2),
    _Xldv20ActControlReq_Type()
)
xldv20ActControlReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20ActControlReq.setStatus("mandatory")
_Xldv20ActControlStatus_Type = Xldv20ControlStatus
_Xldv20ActControlStatus_Object = MibScalar
xldv20ActControlStatus = _Xldv20ActControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 1, 3),
    _Xldv20ActControlStatus_Type()
)
xldv20ActControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ActControlStatus.setStatus("mandatory")


class _Xldv20ActVpiNni_Type(Integer32):
    """Custom type xldv20ActVpiNni based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Xldv20ActVpiNni_Type.__name__ = "Integer32"
_Xldv20ActVpiNni_Object = MibScalar
xldv20ActVpiNni = _Xldv20ActVpiNni_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 1, 4),
    _Xldv20ActVpiNni_Type()
)
xldv20ActVpiNni.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20ActVpiNni.setStatus("mandatory")


class _Xldv20ActVpiUni_Type(Integer32):
    """Custom type xldv20ActVpiUni based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Xldv20ActVpiUni_Type.__name__ = "Integer32"
_Xldv20ActVpiUni_Object = MibScalar
xldv20ActVpiUni = _Xldv20ActVpiUni_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 1, 5),
    _Xldv20ActVpiUni_Type()
)
xldv20ActVpiUni.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20ActVpiUni.setStatus("mandatory")


class _Xldv20ActVciNni_Type(Integer32):
    """Custom type xldv20ActVciNni based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 3500),
    )


_Xldv20ActVciNni_Type.__name__ = "Integer32"
_Xldv20ActVciNni_Object = MibScalar
xldv20ActVciNni = _Xldv20ActVciNni_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 1, 6),
    _Xldv20ActVciNni_Type()
)
xldv20ActVciNni.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20ActVciNni.setStatus("mandatory")


class _Xldv20ActVciUni_Type(Integer32):
    """Custom type xldv20ActVciUni based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 3500),
    )


_Xldv20ActVciUni_Type.__name__ = "Integer32"
_Xldv20ActVciUni_Object = MibScalar
xldv20ActVciUni = _Xldv20ActVciUni_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 1, 7),
    _Xldv20ActVciUni_Type()
)
xldv20ActVciUni.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20ActVciUni.setStatus("mandatory")
_Xldv20ActIfIndex_Type = Unsigned16
_Xldv20ActIfIndex_Object = MibScalar
xldv20ActIfIndex = _Xldv20ActIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 1, 8),
    _Xldv20ActIfIndex_Type()
)
xldv20ActIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20ActIfIndex.setStatus("mandatory")


class _Xldv20ActPeakCellRateUpstream_Type(Integer32):
    """Custom type xldv20ActPeakCellRateUpstream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 160000000),
    )


_Xldv20ActPeakCellRateUpstream_Type.__name__ = "Integer32"
_Xldv20ActPeakCellRateUpstream_Object = MibScalar
xldv20ActPeakCellRateUpstream = _Xldv20ActPeakCellRateUpstream_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 1, 9),
    _Xldv20ActPeakCellRateUpstream_Type()
)
xldv20ActPeakCellRateUpstream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20ActPeakCellRateUpstream.setStatus("mandatory")


class _Xldv20ActPeakCellRateDownstream_Type(Integer32):
    """Custom type xldv20ActPeakCellRateDownstream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 160000000),
    )


_Xldv20ActPeakCellRateDownstream_Type.__name__ = "Integer32"
_Xldv20ActPeakCellRateDownstream_Object = MibScalar
xldv20ActPeakCellRateDownstream = _Xldv20ActPeakCellRateDownstream_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 1, 10),
    _Xldv20ActPeakCellRateDownstream_Type()
)
xldv20ActPeakCellRateDownstream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20ActPeakCellRateDownstream.setStatus("mandatory")


class _Xldv20ActCellDelayVariationToleranceUpstream_Type(Integer32):
    """Custom type xldv20ActCellDelayVariationToleranceUpstream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 200000),
    )


_Xldv20ActCellDelayVariationToleranceUpstream_Type.__name__ = "Integer32"
_Xldv20ActCellDelayVariationToleranceUpstream_Object = MibScalar
xldv20ActCellDelayVariationToleranceUpstream = _Xldv20ActCellDelayVariationToleranceUpstream_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 1, 11),
    _Xldv20ActCellDelayVariationToleranceUpstream_Type()
)
xldv20ActCellDelayVariationToleranceUpstream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20ActCellDelayVariationToleranceUpstream.setStatus("mandatory")


class _Xldv20ActCellDelayVariationToleranceDownstream_Type(Integer32):
    """Custom type xldv20ActCellDelayVariationToleranceDownstream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 200000),
    )


_Xldv20ActCellDelayVariationToleranceDownstream_Type.__name__ = "Integer32"
_Xldv20ActCellDelayVariationToleranceDownstream_Object = MibScalar
xldv20ActCellDelayVariationToleranceDownstream = _Xldv20ActCellDelayVariationToleranceDownstream_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 1, 12),
    _Xldv20ActCellDelayVariationToleranceDownstream_Type()
)
xldv20ActCellDelayVariationToleranceDownstream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20ActCellDelayVariationToleranceDownstream.setStatus("mandatory")
_Xldv20ActTrafficType_Type = Xldv20TrafficType
_Xldv20ActTrafficType_Object = MibScalar
xldv20ActTrafficType = _Xldv20ActTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 1, 13),
    _Xldv20ActTrafficType_Type()
)
xldv20ActTrafficType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20ActTrafficType.setStatus("mandatory")
_Xldv20ActTrafficDirection_Type = Xldv20TrafficDirection
_Xldv20ActTrafficDirection_Object = MibScalar
xldv20ActTrafficDirection = _Xldv20ActTrafficDirection_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 1, 14),
    _Xldv20ActTrafficDirection_Type()
)
xldv20ActTrafficDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20ActTrafficDirection.setStatus("mandatory")


class _Xldv20ActSustainableCellRateUpstream_Type(Integer32):
    """Custom type xldv20ActSustainableCellRateUpstream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 155000000),
    )


_Xldv20ActSustainableCellRateUpstream_Type.__name__ = "Integer32"
_Xldv20ActSustainableCellRateUpstream_Object = MibScalar
xldv20ActSustainableCellRateUpstream = _Xldv20ActSustainableCellRateUpstream_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 1, 15),
    _Xldv20ActSustainableCellRateUpstream_Type()
)
xldv20ActSustainableCellRateUpstream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20ActSustainableCellRateUpstream.setStatus("mandatory")


class _Xldv20ActSustainableCellRateDownstream_Type(Integer32):
    """Custom type xldv20ActSustainableCellRateDownstream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 155000000),
    )


_Xldv20ActSustainableCellRateDownstream_Type.__name__ = "Integer32"
_Xldv20ActSustainableCellRateDownstream_Object = MibScalar
xldv20ActSustainableCellRateDownstream = _Xldv20ActSustainableCellRateDownstream_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 1, 16),
    _Xldv20ActSustainableCellRateDownstream_Type()
)
xldv20ActSustainableCellRateDownstream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20ActSustainableCellRateDownstream.setStatus("mandatory")


class _Xldv20ActMaximumBurstSizeUpstream_Type(Integer32):
    """Custom type xldv20ActMaximumBurstSizeUpstream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_Xldv20ActMaximumBurstSizeUpstream_Type.__name__ = "Integer32"
_Xldv20ActMaximumBurstSizeUpstream_Object = MibScalar
xldv20ActMaximumBurstSizeUpstream = _Xldv20ActMaximumBurstSizeUpstream_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 1, 17),
    _Xldv20ActMaximumBurstSizeUpstream_Type()
)
xldv20ActMaximumBurstSizeUpstream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20ActMaximumBurstSizeUpstream.setStatus("mandatory")


class _Xldv20ActMaximumBurstSizeDownstream_Type(Integer32):
    """Custom type xldv20ActMaximumBurstSizeDownstream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1500),
    )


_Xldv20ActMaximumBurstSizeDownstream_Type.__name__ = "Integer32"
_Xldv20ActMaximumBurstSizeDownstream_Object = MibScalar
xldv20ActMaximumBurstSizeDownstream = _Xldv20ActMaximumBurstSizeDownstream_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 1, 18),
    _Xldv20ActMaximumBurstSizeDownstream_Type()
)
xldv20ActMaximumBurstSizeDownstream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20ActMaximumBurstSizeDownstream.setStatus("mandatory")


class _Xldv20ActSegmentEndPointNni_Type(Integer32):
    """Custom type xldv20ActSegmentEndPointNni based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Xldv20ActSegmentEndPointNni_Type.__name__ = "Integer32"
_Xldv20ActSegmentEndPointNni_Object = MibScalar
xldv20ActSegmentEndPointNni = _Xldv20ActSegmentEndPointNni_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 1, 19),
    _Xldv20ActSegmentEndPointNni_Type()
)
xldv20ActSegmentEndPointNni.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20ActSegmentEndPointNni.setStatus("mandatory")


class _Xldv20ActSegmentEndPointUni_Type(Integer32):
    """Custom type xldv20ActSegmentEndPointUni based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Xldv20ActSegmentEndPointUni_Type.__name__ = "Integer32"
_Xldv20ActSegmentEndPointUni_Object = MibScalar
xldv20ActSegmentEndPointUni = _Xldv20ActSegmentEndPointUni_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 1, 20),
    _Xldv20ActSegmentEndPointUni_Type()
)
xldv20ActSegmentEndPointUni.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20ActSegmentEndPointUni.setStatus("mandatory")
_Xldv20ActEthMode_Type = Xldv20EthNtMode
_Xldv20ActEthMode_Object = MibScalar
xldv20ActEthMode = _Xldv20ActEthMode_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 1, 21),
    _Xldv20ActEthMode_Type()
)
xldv20ActEthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20ActEthMode.setStatus("mandatory")


class _Xldv20ActEthE164Isp_Type(OctetString):
    """Custom type xldv20ActEthE164Isp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Xldv20ActEthE164Isp_Type.__name__ = "OctetString"
_Xldv20ActEthE164Isp_Object = MibScalar
xldv20ActEthE164Isp = _Xldv20ActEthE164Isp_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 1, 22),
    _Xldv20ActEthE164Isp_Type()
)
xldv20ActEthE164Isp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20ActEthE164Isp.setStatus("mandatory")
_Xldv20ActEthIpAddressNt_Type = IpAddress
_Xldv20ActEthIpAddressNt_Object = MibScalar
xldv20ActEthIpAddressNt = _Xldv20ActEthIpAddressNt_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 1, 23),
    _Xldv20ActEthIpAddressNt_Type()
)
xldv20ActEthIpAddressNt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20ActEthIpAddressNt.setStatus("mandatory")
_Xldv20ActEthIpAddressSubnetMaskNt_Type = IpAddress
_Xldv20ActEthIpAddressSubnetMaskNt_Object = MibScalar
xldv20ActEthIpAddressSubnetMaskNt = _Xldv20ActEthIpAddressSubnetMaskNt_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 1, 24),
    _Xldv20ActEthIpAddressSubnetMaskNt_Type()
)
xldv20ActEthIpAddressSubnetMaskNt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20ActEthIpAddressSubnetMaskNt.setStatus("mandatory")
_Xldv20ActEthIpAddressCo_Type = IpAddress
_Xldv20ActEthIpAddressCo_Object = MibScalar
xldv20ActEthIpAddressCo = _Xldv20ActEthIpAddressCo_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 1, 25),
    _Xldv20ActEthIpAddressCo_Type()
)
xldv20ActEthIpAddressCo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20ActEthIpAddressCo.setStatus("mandatory")
_Xldv20ActEthIpAddressSubnetMaskCo_Type = IpAddress
_Xldv20ActEthIpAddressSubnetMaskCo_Object = MibScalar
xldv20ActEthIpAddressSubnetMaskCo = _Xldv20ActEthIpAddressSubnetMaskCo_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 1, 26),
    _Xldv20ActEthIpAddressSubnetMaskCo_Type()
)
xldv20ActEthIpAddressSubnetMaskCo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20ActEthIpAddressSubnetMaskCo.setStatus("mandatory")
_Xldv20ActEthIpAddressRemoteRouter_Type = IpAddress
_Xldv20ActEthIpAddressRemoteRouter_Object = MibScalar
xldv20ActEthIpAddressRemoteRouter = _Xldv20ActEthIpAddressRemoteRouter_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 1, 27),
    _Xldv20ActEthIpAddressRemoteRouter_Type()
)
xldv20ActEthIpAddressRemoteRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20ActEthIpAddressRemoteRouter.setStatus("mandatory")
_Xldv20ActTestTypeNni_Type = Xldv20TestType
_Xldv20ActTestTypeNni_Object = MibScalar
xldv20ActTestTypeNni = _Xldv20ActTestTypeNni_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 1, 28),
    _Xldv20ActTestTypeNni_Type()
)
xldv20ActTestTypeNni.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20ActTestTypeNni.setStatus("mandatory")
_Xldv20ActContinuityCheckNni_Type = Xldv20OperState
_Xldv20ActContinuityCheckNni_Object = MibScalar
xldv20ActContinuityCheckNni = _Xldv20ActContinuityCheckNni_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 1, 29),
    _Xldv20ActContinuityCheckNni_Type()
)
xldv20ActContinuityCheckNni.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20ActContinuityCheckNni.setStatus("mandatory")
_Xldv20ActEndpointTypeNni_Type = Xldv20EndpointType
_Xldv20ActEndpointTypeNni_Object = MibScalar
xldv20ActEndpointTypeNni = _Xldv20ActEndpointTypeNni_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 1, 30),
    _Xldv20ActEndpointTypeNni_Type()
)
xldv20ActEndpointTypeNni.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20ActEndpointTypeNni.setStatus("mandatory")
_Xldv20ActTestTypeUni_Type = Xldv20TestType
_Xldv20ActTestTypeUni_Object = MibScalar
xldv20ActTestTypeUni = _Xldv20ActTestTypeUni_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 1, 31),
    _Xldv20ActTestTypeUni_Type()
)
xldv20ActTestTypeUni.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20ActTestTypeUni.setStatus("mandatory")
_Xldv20ActContinuityCheckUni_Type = Xldv20OperState
_Xldv20ActContinuityCheckUni_Object = MibScalar
xldv20ActContinuityCheckUni = _Xldv20ActContinuityCheckUni_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 1, 32),
    _Xldv20ActContinuityCheckUni_Type()
)
xldv20ActContinuityCheckUni.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20ActContinuityCheckUni.setStatus("mandatory")
_Xldv20ActEndpointTypeUni_Type = Xldv20EndpointType
_Xldv20ActEndpointTypeUni_Object = MibScalar
xldv20ActEndpointTypeUni = _Xldv20ActEndpointTypeUni_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 1, 33),
    _Xldv20ActEndpointTypeUni_Type()
)
xldv20ActEndpointTypeUni.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20ActEndpointTypeUni.setStatus("mandatory")
_Xldv20ActControlReqResult_Type = Xldv20ControlReq
_Xldv20ActControlReqResult_Object = MibScalar
xldv20ActControlReqResult = _Xldv20ActControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 1, 34),
    _Xldv20ActControlReqResult_Type()
)
xldv20ActControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ActControlReqResult.setStatus("mandatory")


class _Xldv20ActInbandVpi_Type(Integer32):
    """Custom type xldv20ActInbandVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Xldv20ActInbandVpi_Type.__name__ = "Integer32"
_Xldv20ActInbandVpi_Object = MibScalar
xldv20ActInbandVpi = _Xldv20ActInbandVpi_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 1, 35),
    _Xldv20ActInbandVpi_Type()
)
xldv20ActInbandVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20ActInbandVpi.setStatus("mandatory")


class _Xldv20ActInbandVci_Type(Integer32):
    """Custom type xldv20ActInbandVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 127),
    )


_Xldv20ActInbandVci_Type.__name__ = "Integer32"
_Xldv20ActInbandVci_Object = MibScalar
xldv20ActInbandVci = _Xldv20ActInbandVci_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 1, 36),
    _Xldv20ActInbandVci_Type()
)
xldv20ActInbandVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20ActInbandVci.setStatus("mandatory")


class _Xldv20ActCallpTableIndex_Type(Integer32):
    """Custom type xldv20ActCallpTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4144),
    )


_Xldv20ActCallpTableIndex_Type.__name__ = "Integer32"
_Xldv20ActCallpTableIndex_Object = MibScalar
xldv20ActCallpTableIndex = _Xldv20ActCallpTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 1, 37),
    _Xldv20ActCallpTableIndex_Type()
)
xldv20ActCallpTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ActCallpTableIndex.setStatus("mandatory")


class _Xldv20ActMaxVciValue_Type(Integer32):
    """Custom type xldv20ActMaxVciValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 3500),
    )


_Xldv20ActMaxVciValue_Type.__name__ = "Integer32"
_Xldv20ActMaxVciValue_Object = MibScalar
xldv20ActMaxVciValue = _Xldv20ActMaxVciValue_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 1, 38),
    _Xldv20ActMaxVciValue_Type()
)
xldv20ActMaxVciValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20ActMaxVciValue.setStatus("mandatory")


class _Xldv20ActVbrCDVTUpstream_Type(Integer32):
    """Custom type xldv20ActVbrCDVTUpstream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 504000000),
    )


_Xldv20ActVbrCDVTUpstream_Type.__name__ = "Integer32"
_Xldv20ActVbrCDVTUpstream_Object = MibScalar
xldv20ActVbrCDVTUpstream = _Xldv20ActVbrCDVTUpstream_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 1, 39),
    _Xldv20ActVbrCDVTUpstream_Type()
)
xldv20ActVbrCDVTUpstream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20ActVbrCDVTUpstream.setStatus("mandatory")


class _Xldv20ActVbrCDVTDownstream_Type(Integer32):
    """Custom type xldv20ActVbrCDVTDownstream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 504000000),
    )


_Xldv20ActVbrCDVTDownstream_Type.__name__ = "Integer32"
_Xldv20ActVbrCDVTDownstream_Object = MibScalar
xldv20ActVbrCDVTDownstream = _Xldv20ActVbrCDVTDownstream_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 1, 40),
    _Xldv20ActVbrCDVTDownstream_Type()
)
xldv20ActVbrCDVTDownstream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20ActVbrCDVTDownstream.setStatus("mandatory")
_Xldv20ActControlTimeStamp_Type = TimeTicks
_Xldv20ActControlTimeStamp_Object = MibScalar
xldv20ActControlTimeStamp = _Xldv20ActControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 1, 41),
    _Xldv20ActControlTimeStamp_Type()
)
xldv20ActControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ActControlTimeStamp.setStatus("mandatory")


class _Xldv20ActSegmentEndPointNt_Type(Integer32):
    """Custom type xldv20ActSegmentEndPointNt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Xldv20ActSegmentEndPointNt_Type.__name__ = "Integer32"
_Xldv20ActSegmentEndPointNt_Object = MibScalar
xldv20ActSegmentEndPointNt = _Xldv20ActSegmentEndPointNt_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 1, 42),
    _Xldv20ActSegmentEndPointNt_Type()
)
xldv20ActSegmentEndPointNt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20ActSegmentEndPointNt.setStatus("mandatory")
_Xldv20ActTestTypeNt_Type = Xldv20TestType
_Xldv20ActTestTypeNt_Object = MibScalar
xldv20ActTestTypeNt = _Xldv20ActTestTypeNt_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 1, 43),
    _Xldv20ActTestTypeNt_Type()
)
xldv20ActTestTypeNt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20ActTestTypeNt.setStatus("mandatory")
_Xldv20ActContinuityCheckNt_Type = Xldv20OperState
_Xldv20ActContinuityCheckNt_Object = MibScalar
xldv20ActContinuityCheckNt = _Xldv20ActContinuityCheckNt_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 1, 44),
    _Xldv20ActContinuityCheckNt_Type()
)
xldv20ActContinuityCheckNt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20ActContinuityCheckNt.setStatus("mandatory")
_Xldv20ActEndpointTypeNt_Type = Xldv20EndpointType
_Xldv20ActEndpointTypeNt_Object = MibScalar
xldv20ActEndpointTypeNt = _Xldv20ActEndpointTypeNt_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 1, 45),
    _Xldv20ActEndpointTypeNt_Type()
)
xldv20ActEndpointTypeNt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20ActEndpointTypeNt.setStatus("mandatory")


class _Xldv20ActCDVTAutoConfig_Type(Integer32):
    """Custom type xldv20ActCDVTAutoConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Xldv20ActCDVTAutoConfig_Type.__name__ = "Integer32"
_Xldv20ActCDVTAutoConfig_Object = MibScalar
xldv20ActCDVTAutoConfig = _Xldv20ActCDVTAutoConfig_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 1, 46),
    _Xldv20ActCDVTAutoConfig_Type()
)
xldv20ActCDVTAutoConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20ActCDVTAutoConfig.setStatus("mandatory")
_Xldv20AtmCrossConnectTable_Object = MibTable
xldv20AtmCrossConnectTable = _Xldv20AtmCrossConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    xldv20AtmCrossConnectTable.setStatus("mandatory")
_Xldv20AtmCrossConnectEntry_Object = MibTableRow
xldv20AtmCrossConnectEntry = _Xldv20AtmCrossConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 2, 1)
)
xldv20AtmCrossConnectEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20AccVpiNniIndex"),
)
if mibBuilder.loadTexts:
    xldv20AtmCrossConnectEntry.setStatus("mandatory")
_Xldv20AccOperationalState_Type = Xldv20OperState
_Xldv20AccOperationalState_Object = MibTableColumn
xldv20AccOperationalState = _Xldv20AccOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 2, 1, 1),
    _Xldv20AccOperationalState_Type()
)
xldv20AccOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AccOperationalState.setStatus("mandatory")


class _Xldv20AccTerminationPointA_Type(Integer32):
    """Custom type xldv20AccTerminationPointA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_Xldv20AccTerminationPointA_Type.__name__ = "Integer32"
_Xldv20AccTerminationPointA_Object = MibTableColumn
xldv20AccTerminationPointA = _Xldv20AccTerminationPointA_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 2, 1, 2),
    _Xldv20AccTerminationPointA_Type()
)
xldv20AccTerminationPointA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AccTerminationPointA.setStatus("mandatory")


class _Xldv20AccTerminationPointZ_Type(Integer32):
    """Custom type xldv20AccTerminationPointZ based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_Xldv20AccTerminationPointZ_Type.__name__ = "Integer32"
_Xldv20AccTerminationPointZ_Object = MibTableColumn
xldv20AccTerminationPointZ = _Xldv20AccTerminationPointZ_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 2, 1, 3),
    _Xldv20AccTerminationPointZ_Type()
)
xldv20AccTerminationPointZ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AccTerminationPointZ.setStatus("mandatory")
_Xldv20AccLineIndex_Type = Unsigned16
_Xldv20AccLineIndex_Object = MibTableColumn
xldv20AccLineIndex = _Xldv20AccLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 2, 1, 4),
    _Xldv20AccLineIndex_Type()
)
xldv20AccLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AccLineIndex.setStatus("mandatory")


class _Xldv20AccEthVpcIndex_Type(Integer32):
    """Custom type xldv20AccEthVpcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_Xldv20AccEthVpcIndex_Type.__name__ = "Integer32"
_Xldv20AccEthVpcIndex_Object = MibTableColumn
xldv20AccEthVpcIndex = _Xldv20AccEthVpcIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 2, 1, 5),
    _Xldv20AccEthVpcIndex_Type()
)
xldv20AccEthVpcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AccEthVpcIndex.setStatus("mandatory")


class _Xldv20AccEthVccIndex_Type(Integer32):
    """Custom type xldv20AccEthVccIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Xldv20AccEthVccIndex_Type.__name__ = "Integer32"
_Xldv20AccEthVccIndex_Object = MibTableColumn
xldv20AccEthVccIndex = _Xldv20AccEthVccIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 2, 1, 6),
    _Xldv20AccEthVccIndex_Type()
)
xldv20AccEthVccIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AccEthVccIndex.setStatus("mandatory")


class _Xldv20AccVpiNniIndex_Type(Integer32):
    """Custom type xldv20AccVpiNniIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_Xldv20AccVpiNniIndex_Type.__name__ = "Integer32"
_Xldv20AccVpiNniIndex_Object = MibTableColumn
xldv20AccVpiNniIndex = _Xldv20AccVpiNniIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 2, 1, 7),
    _Xldv20AccVpiNniIndex_Type()
)
xldv20AccVpiNniIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AccVpiNniIndex.setStatus("mandatory")
_Xldv20AccAlarmState_Type = Xldv20CallpAlarmState
_Xldv20AccAlarmState_Object = MibTableColumn
xldv20AccAlarmState = _Xldv20AccAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 2, 1, 8),
    _Xldv20AccAlarmState_Type()
)
xldv20AccAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AccAlarmState.setStatus("mandatory")
_Xldv20AccAdminState_Type = Xldv20AdminState
_Xldv20AccAdminState_Object = MibTableColumn
xldv20AccAdminState = _Xldv20AccAdminState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 2, 1, 9),
    _Xldv20AccAdminState_Type()
)
xldv20AccAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20AccAdminState.setStatus("mandatory")


class _Xldv20AccAtmfVplIndex_Type(Integer32):
    """Custom type xldv20AccAtmfVplIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4000),
    )


_Xldv20AccAtmfVplIndex_Type.__name__ = "Integer32"
_Xldv20AccAtmfVplIndex_Object = MibTableColumn
xldv20AccAtmfVplIndex = _Xldv20AccAtmfVplIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 2, 1, 10),
    _Xldv20AccAtmfVplIndex_Type()
)
xldv20AccAtmfVplIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AccAtmfVplIndex.setStatus("mandatory")
_Xldv20VplTpTable_Object = MibTable
xldv20VplTpTable = _Xldv20VplTpTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 3)
)
if mibBuilder.loadTexts:
    xldv20VplTpTable.setStatus("mandatory")
_Xldv20VplTpEntry_Object = MibTableRow
xldv20VplTpEntry = _Xldv20VplTpEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 3, 1)
)
xldv20VplTpEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20VplIndex"),
)
if mibBuilder.loadTexts:
    xldv20VplTpEntry.setStatus("mandatory")
_Xldv20VplOperationalState_Type = Xldv20OperState
_Xldv20VplOperationalState_Object = MibTableColumn
xldv20VplOperationalState = _Xldv20VplOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 3, 1, 1),
    _Xldv20VplOperationalState_Type()
)
xldv20VplOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VplOperationalState.setStatus("mandatory")


class _Xldv20VplVpiValue_Type(Integer32):
    """Custom type xldv20VplVpiValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Xldv20VplVpiValue_Type.__name__ = "Integer32"
_Xldv20VplVpiValue_Object = MibTableColumn
xldv20VplVpiValue = _Xldv20VplVpiValue_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 3, 1, 2),
    _Xldv20VplVpiValue_Type()
)
xldv20VplVpiValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VplVpiValue.setStatus("mandatory")
_Xldv20VplHwUnitIndex_Type = Unsigned16
_Xldv20VplHwUnitIndex_Object = MibTableColumn
xldv20VplHwUnitIndex = _Xldv20VplHwUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 3, 1, 3),
    _Xldv20VplHwUnitIndex_Type()
)
xldv20VplHwUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VplHwUnitIndex.setStatus("mandatory")
_Xldv20VplIfIndex_Type = Unsigned16
_Xldv20VplIfIndex_Object = MibTableColumn
xldv20VplIfIndex = _Xldv20VplIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 3, 1, 4),
    _Xldv20VplIfIndex_Type()
)
xldv20VplIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VplIfIndex.setStatus("mandatory")
_Xldv20VplPeakCellRateUpstream_Type = Unsigned32
_Xldv20VplPeakCellRateUpstream_Object = MibTableColumn
xldv20VplPeakCellRateUpstream = _Xldv20VplPeakCellRateUpstream_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 3, 1, 5),
    _Xldv20VplPeakCellRateUpstream_Type()
)
xldv20VplPeakCellRateUpstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VplPeakCellRateUpstream.setStatus("mandatory")
_Xldv20VplPeakCellRateDownstream_Type = Unsigned32
_Xldv20VplPeakCellRateDownstream_Object = MibTableColumn
xldv20VplPeakCellRateDownstream = _Xldv20VplPeakCellRateDownstream_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 3, 1, 6),
    _Xldv20VplPeakCellRateDownstream_Type()
)
xldv20VplPeakCellRateDownstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VplPeakCellRateDownstream.setStatus("mandatory")


class _Xldv20VplCellDelayVariationToleranceUpstream_Type(Integer32):
    """Custom type xldv20VplCellDelayVariationToleranceUpstream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 200000),
    )


_Xldv20VplCellDelayVariationToleranceUpstream_Type.__name__ = "Integer32"
_Xldv20VplCellDelayVariationToleranceUpstream_Object = MibTableColumn
xldv20VplCellDelayVariationToleranceUpstream = _Xldv20VplCellDelayVariationToleranceUpstream_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 3, 1, 7),
    _Xldv20VplCellDelayVariationToleranceUpstream_Type()
)
xldv20VplCellDelayVariationToleranceUpstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VplCellDelayVariationToleranceUpstream.setStatus("mandatory")


class _Xldv20VplCellDelayVariationToleranceDownstream_Type(Integer32):
    """Custom type xldv20VplCellDelayVariationToleranceDownstream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 200000),
    )


_Xldv20VplCellDelayVariationToleranceDownstream_Type.__name__ = "Integer32"
_Xldv20VplCellDelayVariationToleranceDownstream_Object = MibTableColumn
xldv20VplCellDelayVariationToleranceDownstream = _Xldv20VplCellDelayVariationToleranceDownstream_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 3, 1, 8),
    _Xldv20VplCellDelayVariationToleranceDownstream_Type()
)
xldv20VplCellDelayVariationToleranceDownstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VplCellDelayVariationToleranceDownstream.setStatus("mandatory")
_Xldv20VplTrafficType_Type = Xldv20TrafficType
_Xldv20VplTrafficType_Object = MibTableColumn
xldv20VplTrafficType = _Xldv20VplTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 3, 1, 9),
    _Xldv20VplTrafficType_Type()
)
xldv20VplTrafficType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VplTrafficType.setStatus("mandatory")
_Xldv20VplTrafficDirection_Type = Xldv20TrafficDirection
_Xldv20VplTrafficDirection_Object = MibTableColumn
xldv20VplTrafficDirection = _Xldv20VplTrafficDirection_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 3, 1, 10),
    _Xldv20VplTrafficDirection_Type()
)
xldv20VplTrafficDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VplTrafficDirection.setStatus("mandatory")
_Xldv20VplConnectivityPointer_Type = Unsigned16
_Xldv20VplConnectivityPointer_Object = MibTableColumn
xldv20VplConnectivityPointer = _Xldv20VplConnectivityPointer_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 3, 1, 11),
    _Xldv20VplConnectivityPointer_Type()
)
xldv20VplConnectivityPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VplConnectivityPointer.setStatus("mandatory")
_Xldv20VplLineIndex_Type = Unsigned16
_Xldv20VplLineIndex_Object = MibTableColumn
xldv20VplLineIndex = _Xldv20VplLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 3, 1, 12),
    _Xldv20VplLineIndex_Type()
)
xldv20VplLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VplLineIndex.setStatus("mandatory")


class _Xldv20VplSegmentEndPoint_Type(Integer32):
    """Custom type xldv20VplSegmentEndPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Xldv20VplSegmentEndPoint_Type.__name__ = "Integer32"
_Xldv20VplSegmentEndPoint_Object = MibTableColumn
xldv20VplSegmentEndPoint = _Xldv20VplSegmentEndPoint_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 3, 1, 13),
    _Xldv20VplSegmentEndPoint_Type()
)
xldv20VplSegmentEndPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VplSegmentEndPoint.setStatus("mandatory")
_Xldv20VplSustainableCellRateUpstream_Type = Unsigned32
_Xldv20VplSustainableCellRateUpstream_Object = MibTableColumn
xldv20VplSustainableCellRateUpstream = _Xldv20VplSustainableCellRateUpstream_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 3, 1, 14),
    _Xldv20VplSustainableCellRateUpstream_Type()
)
xldv20VplSustainableCellRateUpstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VplSustainableCellRateUpstream.setStatus("mandatory")
_Xldv20VplSustainableCellRateDownstream_Type = Unsigned32
_Xldv20VplSustainableCellRateDownstream_Object = MibTableColumn
xldv20VplSustainableCellRateDownstream = _Xldv20VplSustainableCellRateDownstream_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 3, 1, 15),
    _Xldv20VplSustainableCellRateDownstream_Type()
)
xldv20VplSustainableCellRateDownstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VplSustainableCellRateDownstream.setStatus("mandatory")


class _Xldv20VplMaximumBurstSizeUpstream_Type(Integer32):
    """Custom type xldv20VplMaximumBurstSizeUpstream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_Xldv20VplMaximumBurstSizeUpstream_Type.__name__ = "Integer32"
_Xldv20VplMaximumBurstSizeUpstream_Object = MibTableColumn
xldv20VplMaximumBurstSizeUpstream = _Xldv20VplMaximumBurstSizeUpstream_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 3, 1, 16),
    _Xldv20VplMaximumBurstSizeUpstream_Type()
)
xldv20VplMaximumBurstSizeUpstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VplMaximumBurstSizeUpstream.setStatus("mandatory")


class _Xldv20VplMaximumBurstSizeDownstream_Type(Integer32):
    """Custom type xldv20VplMaximumBurstSizeDownstream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_Xldv20VplMaximumBurstSizeDownstream_Type.__name__ = "Integer32"
_Xldv20VplMaximumBurstSizeDownstream_Object = MibTableColumn
xldv20VplMaximumBurstSizeDownstream = _Xldv20VplMaximumBurstSizeDownstream_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 3, 1, 17),
    _Xldv20VplMaximumBurstSizeDownstream_Type()
)
xldv20VplMaximumBurstSizeDownstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VplMaximumBurstSizeDownstream.setStatus("mandatory")
_Xldv20VplAlarmSeverityIndex_Type = Xldv20AlmSevProfileIndex
_Xldv20VplAlarmSeverityIndex_Object = MibTableColumn
xldv20VplAlarmSeverityIndex = _Xldv20VplAlarmSeverityIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 3, 1, 18),
    _Xldv20VplAlarmSeverityIndex_Type()
)
xldv20VplAlarmSeverityIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20VplAlarmSeverityIndex.setStatus("mandatory")
_Xldv20VplAlarmFilteringIndex_Type = Xldv20AlmFiltProfileIndex
_Xldv20VplAlarmFilteringIndex_Object = MibTableColumn
xldv20VplAlarmFilteringIndex = _Xldv20VplAlarmFilteringIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 3, 1, 19),
    _Xldv20VplAlarmFilteringIndex_Type()
)
xldv20VplAlarmFilteringIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20VplAlarmFilteringIndex.setStatus("mandatory")


class _Xldv20VplCvpIndexSegment_Type(Integer32):
    """Custom type xldv20VplCvpIndexSegment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_Xldv20VplCvpIndexSegment_Type.__name__ = "Integer32"
_Xldv20VplCvpIndexSegment_Object = MibTableColumn
xldv20VplCvpIndexSegment = _Xldv20VplCvpIndexSegment_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 3, 1, 20),
    _Xldv20VplCvpIndexSegment_Type()
)
xldv20VplCvpIndexSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VplCvpIndexSegment.setStatus("mandatory")


class _Xldv20VplIndex_Type(Integer32):
    """Custom type xldv20VplIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4000),
    )


_Xldv20VplIndex_Type.__name__ = "Integer32"
_Xldv20VplIndex_Object = MibTableColumn
xldv20VplIndex = _Xldv20VplIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 3, 1, 21),
    _Xldv20VplIndex_Type()
)
xldv20VplIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VplIndex.setStatus("mandatory")
_Xldv20VplLOCAlarm_Type = Xldv20TpAlarmState
_Xldv20VplLOCAlarm_Object = MibTableColumn
xldv20VplLOCAlarm = _Xldv20VplLOCAlarm_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 3, 1, 22),
    _Xldv20VplLOCAlarm_Type()
)
xldv20VplLOCAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VplLOCAlarm.setStatus("mandatory")


class _Xldv20VplVbrCDVTUpstream_Type(Integer32):
    """Custom type xldv20VplVbrCDVTUpstream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 504000000),
    )


_Xldv20VplVbrCDVTUpstream_Type.__name__ = "Integer32"
_Xldv20VplVbrCDVTUpstream_Object = MibTableColumn
xldv20VplVbrCDVTUpstream = _Xldv20VplVbrCDVTUpstream_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 3, 1, 23),
    _Xldv20VplVbrCDVTUpstream_Type()
)
xldv20VplVbrCDVTUpstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VplVbrCDVTUpstream.setStatus("mandatory")


class _Xldv20VplVbrCDVTDownstream_Type(Integer32):
    """Custom type xldv20VplVbrCDVTDownstream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 504000000),
    )


_Xldv20VplVbrCDVTDownstream_Type.__name__ = "Integer32"
_Xldv20VplVbrCDVTDownstream_Object = MibTableColumn
xldv20VplVbrCDVTDownstream = _Xldv20VplVbrCDVTDownstream_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 3, 1, 24),
    _Xldv20VplVbrCDVTDownstream_Type()
)
xldv20VplVbrCDVTDownstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VplVbrCDVTDownstream.setStatus("mandatory")
_Xldv20VpcTpTable_Object = MibTable
xldv20VpcTpTable = _Xldv20VpcTpTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 4)
)
if mibBuilder.loadTexts:
    xldv20VpcTpTable.setStatus("mandatory")
_Xldv20VpcTpEntry_Object = MibTableRow
xldv20VpcTpEntry = _Xldv20VpcTpEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 4, 1)
)
xldv20VpcTpEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20VpcIndex"),
)
if mibBuilder.loadTexts:
    xldv20VpcTpEntry.setStatus("mandatory")
_Xldv20VpcOperationalState_Type = Xldv20OperState
_Xldv20VpcOperationalState_Object = MibTableColumn
xldv20VpcOperationalState = _Xldv20VpcOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 4, 1, 1),
    _Xldv20VpcOperationalState_Type()
)
xldv20VpcOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VpcOperationalState.setStatus("mandatory")


class _Xldv20VpcVpiValue_Type(Integer32):
    """Custom type xldv20VpcVpiValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Xldv20VpcVpiValue_Type.__name__ = "Integer32"
_Xldv20VpcVpiValue_Object = MibTableColumn
xldv20VpcVpiValue = _Xldv20VpcVpiValue_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 4, 1, 2),
    _Xldv20VpcVpiValue_Type()
)
xldv20VpcVpiValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VpcVpiValue.setStatus("mandatory")
_Xldv20VpcHwUnitIndex_Type = Unsigned16
_Xldv20VpcHwUnitIndex_Object = MibTableColumn
xldv20VpcHwUnitIndex = _Xldv20VpcHwUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 4, 1, 3),
    _Xldv20VpcHwUnitIndex_Type()
)
xldv20VpcHwUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VpcHwUnitIndex.setStatus("mandatory")
_Xldv20VpcIfIndex_Type = Unsigned16
_Xldv20VpcIfIndex_Object = MibTableColumn
xldv20VpcIfIndex = _Xldv20VpcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 4, 1, 4),
    _Xldv20VpcIfIndex_Type()
)
xldv20VpcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VpcIfIndex.setStatus("mandatory")
_Xldv20VpcPeakCellRateUpstream_Type = Unsigned32
_Xldv20VpcPeakCellRateUpstream_Object = MibTableColumn
xldv20VpcPeakCellRateUpstream = _Xldv20VpcPeakCellRateUpstream_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 4, 1, 5),
    _Xldv20VpcPeakCellRateUpstream_Type()
)
xldv20VpcPeakCellRateUpstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VpcPeakCellRateUpstream.setStatus("mandatory")
_Xldv20VpcPeakCellRateDownstream_Type = Unsigned32
_Xldv20VpcPeakCellRateDownstream_Object = MibTableColumn
xldv20VpcPeakCellRateDownstream = _Xldv20VpcPeakCellRateDownstream_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 4, 1, 6),
    _Xldv20VpcPeakCellRateDownstream_Type()
)
xldv20VpcPeakCellRateDownstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VpcPeakCellRateDownstream.setStatus("mandatory")


class _Xldv20VpcCellDelayVariationToleranceUpstream_Type(Integer32):
    """Custom type xldv20VpcCellDelayVariationToleranceUpstream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 200000),
    )


_Xldv20VpcCellDelayVariationToleranceUpstream_Type.__name__ = "Integer32"
_Xldv20VpcCellDelayVariationToleranceUpstream_Object = MibTableColumn
xldv20VpcCellDelayVariationToleranceUpstream = _Xldv20VpcCellDelayVariationToleranceUpstream_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 4, 1, 7),
    _Xldv20VpcCellDelayVariationToleranceUpstream_Type()
)
xldv20VpcCellDelayVariationToleranceUpstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VpcCellDelayVariationToleranceUpstream.setStatus("mandatory")


class _Xldv20VpcCellDelayVariationToleranceDownstream_Type(Integer32):
    """Custom type xldv20VpcCellDelayVariationToleranceDownstream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 200000),
    )


_Xldv20VpcCellDelayVariationToleranceDownstream_Type.__name__ = "Integer32"
_Xldv20VpcCellDelayVariationToleranceDownstream_Object = MibTableColumn
xldv20VpcCellDelayVariationToleranceDownstream = _Xldv20VpcCellDelayVariationToleranceDownstream_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 4, 1, 8),
    _Xldv20VpcCellDelayVariationToleranceDownstream_Type()
)
xldv20VpcCellDelayVariationToleranceDownstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VpcCellDelayVariationToleranceDownstream.setStatus("mandatory")
_Xldv20VpcTrafficType_Type = Xldv20TrafficType
_Xldv20VpcTrafficType_Object = MibTableColumn
xldv20VpcTrafficType = _Xldv20VpcTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 4, 1, 9),
    _Xldv20VpcTrafficType_Type()
)
xldv20VpcTrafficType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VpcTrafficType.setStatus("mandatory")
_Xldv20VpcTrafficDirection_Type = Xldv20TrafficDirection
_Xldv20VpcTrafficDirection_Object = MibTableColumn
xldv20VpcTrafficDirection = _Xldv20VpcTrafficDirection_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 4, 1, 10),
    _Xldv20VpcTrafficDirection_Type()
)
xldv20VpcTrafficDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VpcTrafficDirection.setStatus("mandatory")
_Xldv20VpcLineIndex_Type = Unsigned16
_Xldv20VpcLineIndex_Object = MibTableColumn
xldv20VpcLineIndex = _Xldv20VpcLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 4, 1, 11),
    _Xldv20VpcLineIndex_Type()
)
xldv20VpcLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VpcLineIndex.setStatus("mandatory")


class _Xldv20VpcSegmentEndPoint_Type(Integer32):
    """Custom type xldv20VpcSegmentEndPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Xldv20VpcSegmentEndPoint_Type.__name__ = "Integer32"
_Xldv20VpcSegmentEndPoint_Object = MibTableColumn
xldv20VpcSegmentEndPoint = _Xldv20VpcSegmentEndPoint_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 4, 1, 12),
    _Xldv20VpcSegmentEndPoint_Type()
)
xldv20VpcSegmentEndPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VpcSegmentEndPoint.setStatus("mandatory")
_Xldv20VpcSustainableCellRateUpstream_Type = Unsigned32
_Xldv20VpcSustainableCellRateUpstream_Object = MibTableColumn
xldv20VpcSustainableCellRateUpstream = _Xldv20VpcSustainableCellRateUpstream_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 4, 1, 13),
    _Xldv20VpcSustainableCellRateUpstream_Type()
)
xldv20VpcSustainableCellRateUpstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VpcSustainableCellRateUpstream.setStatus("mandatory")
_Xldv20VpcSustainableCellRateDownstream_Type = Unsigned32
_Xldv20VpcSustainableCellRateDownstream_Object = MibTableColumn
xldv20VpcSustainableCellRateDownstream = _Xldv20VpcSustainableCellRateDownstream_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 4, 1, 14),
    _Xldv20VpcSustainableCellRateDownstream_Type()
)
xldv20VpcSustainableCellRateDownstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VpcSustainableCellRateDownstream.setStatus("mandatory")


class _Xldv20VpcMaximumBurstSizeUpstream_Type(Integer32):
    """Custom type xldv20VpcMaximumBurstSizeUpstream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_Xldv20VpcMaximumBurstSizeUpstream_Type.__name__ = "Integer32"
_Xldv20VpcMaximumBurstSizeUpstream_Object = MibTableColumn
xldv20VpcMaximumBurstSizeUpstream = _Xldv20VpcMaximumBurstSizeUpstream_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 4, 1, 15),
    _Xldv20VpcMaximumBurstSizeUpstream_Type()
)
xldv20VpcMaximumBurstSizeUpstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VpcMaximumBurstSizeUpstream.setStatus("mandatory")


class _Xldv20VpcMaximumBurstSizeDownstream_Type(Integer32):
    """Custom type xldv20VpcMaximumBurstSizeDownstream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_Xldv20VpcMaximumBurstSizeDownstream_Type.__name__ = "Integer32"
_Xldv20VpcMaximumBurstSizeDownstream_Object = MibTableColumn
xldv20VpcMaximumBurstSizeDownstream = _Xldv20VpcMaximumBurstSizeDownstream_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 4, 1, 16),
    _Xldv20VpcMaximumBurstSizeDownstream_Type()
)
xldv20VpcMaximumBurstSizeDownstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VpcMaximumBurstSizeDownstream.setStatus("mandatory")
_Xldv20VpcAlarmSeverityIndex_Type = Xldv20AlmSevProfileIndex
_Xldv20VpcAlarmSeverityIndex_Object = MibTableColumn
xldv20VpcAlarmSeverityIndex = _Xldv20VpcAlarmSeverityIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 4, 1, 17),
    _Xldv20VpcAlarmSeverityIndex_Type()
)
xldv20VpcAlarmSeverityIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20VpcAlarmSeverityIndex.setStatus("mandatory")
_Xldv20VpcAlarmFilteringIndex_Type = Xldv20AlmFiltProfileIndex
_Xldv20VpcAlarmFilteringIndex_Object = MibTableColumn
xldv20VpcAlarmFilteringIndex = _Xldv20VpcAlarmFilteringIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 4, 1, 18),
    _Xldv20VpcAlarmFilteringIndex_Type()
)
xldv20VpcAlarmFilteringIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20VpcAlarmFilteringIndex.setStatus("mandatory")


class _Xldv20VpcCvpIndexSegment_Type(Integer32):
    """Custom type xldv20VpcCvpIndexSegment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_Xldv20VpcCvpIndexSegment_Type.__name__ = "Integer32"
_Xldv20VpcCvpIndexSegment_Object = MibTableColumn
xldv20VpcCvpIndexSegment = _Xldv20VpcCvpIndexSegment_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 4, 1, 19),
    _Xldv20VpcCvpIndexSegment_Type()
)
xldv20VpcCvpIndexSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VpcCvpIndexSegment.setStatus("mandatory")


class _Xldv20VpcCvpIndexEndToEnd_Type(Integer32):
    """Custom type xldv20VpcCvpIndexEndToEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_Xldv20VpcCvpIndexEndToEnd_Type.__name__ = "Integer32"
_Xldv20VpcCvpIndexEndToEnd_Object = MibTableColumn
xldv20VpcCvpIndexEndToEnd = _Xldv20VpcCvpIndexEndToEnd_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 4, 1, 20),
    _Xldv20VpcCvpIndexEndToEnd_Type()
)
xldv20VpcCvpIndexEndToEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VpcCvpIndexEndToEnd.setStatus("mandatory")


class _Xldv20VpcIndex_Type(Integer32):
    """Custom type xldv20VpcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_Xldv20VpcIndex_Type.__name__ = "Integer32"
_Xldv20VpcIndex_Object = MibTableColumn
xldv20VpcIndex = _Xldv20VpcIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 4, 1, 21),
    _Xldv20VpcIndex_Type()
)
xldv20VpcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VpcIndex.setStatus("mandatory")
_Xldv20VpcAISAlarm_Type = Xldv20TpAlarmState
_Xldv20VpcAISAlarm_Object = MibTableColumn
xldv20VpcAISAlarm = _Xldv20VpcAISAlarm_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 4, 1, 22),
    _Xldv20VpcAISAlarm_Type()
)
xldv20VpcAISAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VpcAISAlarm.setStatus("mandatory")
_Xldv20VpcRDIAlarm_Type = Xldv20TpAlarmState
_Xldv20VpcRDIAlarm_Object = MibTableColumn
xldv20VpcRDIAlarm = _Xldv20VpcRDIAlarm_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 4, 1, 23),
    _Xldv20VpcRDIAlarm_Type()
)
xldv20VpcRDIAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VpcRDIAlarm.setStatus("mandatory")
_Xldv20VpcLOCAlarm_Type = Xldv20TpAlarmState
_Xldv20VpcLOCAlarm_Object = MibTableColumn
xldv20VpcLOCAlarm = _Xldv20VpcLOCAlarm_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 4, 1, 24),
    _Xldv20VpcLOCAlarm_Type()
)
xldv20VpcLOCAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VpcLOCAlarm.setStatus("mandatory")


class _Xldv20VpcNumberOfVcs_Type(Integer32):
    """Custom type xldv20VpcNumberOfVcs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3469),
    )


_Xldv20VpcNumberOfVcs_Type.__name__ = "Integer32"
_Xldv20VpcNumberOfVcs_Object = MibTableColumn
xldv20VpcNumberOfVcs = _Xldv20VpcNumberOfVcs_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 4, 1, 25),
    _Xldv20VpcNumberOfVcs_Type()
)
xldv20VpcNumberOfVcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VpcNumberOfVcs.setStatus("mandatory")


class _Xldv20VpcVbrCDVTUpstream_Type(Integer32):
    """Custom type xldv20VpcVbrCDVTUpstream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 504000000),
    )


_Xldv20VpcVbrCDVTUpstream_Type.__name__ = "Integer32"
_Xldv20VpcVbrCDVTUpstream_Object = MibTableColumn
xldv20VpcVbrCDVTUpstream = _Xldv20VpcVbrCDVTUpstream_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 4, 1, 26),
    _Xldv20VpcVbrCDVTUpstream_Type()
)
xldv20VpcVbrCDVTUpstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VpcVbrCDVTUpstream.setStatus("mandatory")


class _Xldv20VpcVbrCDVTDownstream_Type(Integer32):
    """Custom type xldv20VpcVbrCDVTDownstream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 504000000),
    )


_Xldv20VpcVbrCDVTDownstream_Type.__name__ = "Integer32"
_Xldv20VpcVbrCDVTDownstream_Object = MibTableColumn
xldv20VpcVbrCDVTDownstream = _Xldv20VpcVbrCDVTDownstream_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 4, 1, 27),
    _Xldv20VpcVbrCDVTDownstream_Type()
)
xldv20VpcVbrCDVTDownstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VpcVbrCDVTDownstream.setStatus("mandatory")
_Xldv20VpcEmSpecific_Type = Unsigned16
_Xldv20VpcEmSpecific_Object = MibTableColumn
xldv20VpcEmSpecific = _Xldv20VpcEmSpecific_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 4, 1, 28),
    _Xldv20VpcEmSpecific_Type()
)
xldv20VpcEmSpecific.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20VpcEmSpecific.setStatus("mandatory")


class _Xldv20VpcEthVpcIndex_Type(Integer32):
    """Custom type xldv20VpcEthVpcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_Xldv20VpcEthVpcIndex_Type.__name__ = "Integer32"
_Xldv20VpcEthVpcIndex_Object = MibTableColumn
xldv20VpcEthVpcIndex = _Xldv20VpcEthVpcIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 4, 1, 29),
    _Xldv20VpcEthVpcIndex_Type()
)
xldv20VpcEthVpcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VpcEthVpcIndex.setStatus("mandatory")


class _Xldv20VpcAtmfVplIndex_Type(Integer32):
    """Custom type xldv20VpcAtmfVplIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4000),
    )


_Xldv20VpcAtmfVplIndex_Type.__name__ = "Integer32"
_Xldv20VpcAtmfVplIndex_Object = MibTableColumn
xldv20VpcAtmfVplIndex = _Xldv20VpcAtmfVplIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 4, 1, 30),
    _Xldv20VpcAtmfVplIndex_Type()
)
xldv20VpcAtmfVplIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VpcAtmfVplIndex.setStatus("mandatory")
_Xldv20VccTpTable_Object = MibTable
xldv20VccTpTable = _Xldv20VccTpTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 5)
)
if mibBuilder.loadTexts:
    xldv20VccTpTable.setStatus("mandatory")
_Xldv20VccTpEntry_Object = MibTableRow
xldv20VccTpEntry = _Xldv20VccTpEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 5, 1)
)
xldv20VccTpEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20VccIndex"),
)
if mibBuilder.loadTexts:
    xldv20VccTpEntry.setStatus("mandatory")
_Xldv20VccOperationalState_Type = Xldv20OperState
_Xldv20VccOperationalState_Object = MibTableColumn
xldv20VccOperationalState = _Xldv20VccOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 5, 1, 1),
    _Xldv20VccOperationalState_Type()
)
xldv20VccOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VccOperationalState.setStatus("mandatory")


class _Xldv20VccVciValue_Type(Integer32):
    """Custom type xldv20VccVciValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 3500),
    )


_Xldv20VccVciValue_Type.__name__ = "Integer32"
_Xldv20VccVciValue_Object = MibTableColumn
xldv20VccVciValue = _Xldv20VccVciValue_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 5, 1, 2),
    _Xldv20VccVciValue_Type()
)
xldv20VccVciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VccVciValue.setStatus("mandatory")


class _Xldv20VccVpcIndex_Type(Integer32):
    """Custom type xldv20VccVpcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_Xldv20VccVpcIndex_Type.__name__ = "Integer32"
_Xldv20VccVpcIndex_Object = MibTableColumn
xldv20VccVpcIndex = _Xldv20VccVpcIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 5, 1, 3),
    _Xldv20VccVpcIndex_Type()
)
xldv20VccVpcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VccVpcIndex.setStatus("mandatory")
_Xldv20VccHwUnitIndex_Type = Unsigned16
_Xldv20VccHwUnitIndex_Object = MibTableColumn
xldv20VccHwUnitIndex = _Xldv20VccHwUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 5, 1, 4),
    _Xldv20VccHwUnitIndex_Type()
)
xldv20VccHwUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VccHwUnitIndex.setStatus("mandatory")
_Xldv20VccAlarmSeverityIndex_Type = Xldv20AlmSevProfileIndex
_Xldv20VccAlarmSeverityIndex_Object = MibTableColumn
xldv20VccAlarmSeverityIndex = _Xldv20VccAlarmSeverityIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 5, 1, 5),
    _Xldv20VccAlarmSeverityIndex_Type()
)
xldv20VccAlarmSeverityIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20VccAlarmSeverityIndex.setStatus("mandatory")
_Xldv20VccAlarmFilteringIndex_Type = Xldv20AlmFiltProfileIndex
_Xldv20VccAlarmFilteringIndex_Object = MibTableColumn
xldv20VccAlarmFilteringIndex = _Xldv20VccAlarmFilteringIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 5, 1, 6),
    _Xldv20VccAlarmFilteringIndex_Type()
)
xldv20VccAlarmFilteringIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VccAlarmFilteringIndex.setStatus("mandatory")
_Xldv20VccLineIndex_Type = Unsigned16
_Xldv20VccLineIndex_Object = MibTableColumn
xldv20VccLineIndex = _Xldv20VccLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 5, 1, 7),
    _Xldv20VccLineIndex_Type()
)
xldv20VccLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VccLineIndex.setStatus("mandatory")


class _Xldv20VccIndex_Type(Integer32):
    """Custom type xldv20VccIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_Xldv20VccIndex_Type.__name__ = "Integer32"
_Xldv20VccIndex_Object = MibTableColumn
xldv20VccIndex = _Xldv20VccIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 5, 1, 8),
    _Xldv20VccIndex_Type()
)
xldv20VccIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VccIndex.setStatus("mandatory")
_Xldv20VccAISAlarm_Type = Xldv20TpAlarmState
_Xldv20VccAISAlarm_Object = MibTableColumn
xldv20VccAISAlarm = _Xldv20VccAISAlarm_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 5, 1, 9),
    _Xldv20VccAISAlarm_Type()
)
xldv20VccAISAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VccAISAlarm.setStatus("mandatory")
_Xldv20VccRDIAlarm_Type = Xldv20TpAlarmState
_Xldv20VccRDIAlarm_Object = MibTableColumn
xldv20VccRDIAlarm = _Xldv20VccRDIAlarm_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 5, 1, 10),
    _Xldv20VccRDIAlarm_Type()
)
xldv20VccRDIAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VccRDIAlarm.setStatus("mandatory")
_Xldv20VccLOCAlarm_Type = Xldv20TpAlarmState
_Xldv20VccLOCAlarm_Object = MibTableColumn
xldv20VccLOCAlarm = _Xldv20VccLOCAlarm_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 5, 1, 11),
    _Xldv20VccLOCAlarm_Type()
)
xldv20VccLOCAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VccLOCAlarm.setStatus("mandatory")
_Xldv20VccCvcIndexSegment_Type = Unsigned16
_Xldv20VccCvcIndexSegment_Object = MibTableColumn
xldv20VccCvcIndexSegment = _Xldv20VccCvcIndexSegment_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 5, 1, 12),
    _Xldv20VccCvcIndexSegment_Type()
)
xldv20VccCvcIndexSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VccCvcIndexSegment.setStatus("mandatory")
_Xldv20VccCvcIndexEndToEnd_Type = Unsigned16
_Xldv20VccCvcIndexEndToEnd_Object = MibTableColumn
xldv20VccCvcIndexEndToEnd = _Xldv20VccCvcIndexEndToEnd_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 5, 1, 13),
    _Xldv20VccCvcIndexEndToEnd_Type()
)
xldv20VccCvcIndexEndToEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VccCvcIndexEndToEnd.setStatus("mandatory")
_Xldv20VcCrossConnectTable_Object = MibTable
xldv20VcCrossConnectTable = _Xldv20VcCrossConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 6)
)
if mibBuilder.loadTexts:
    xldv20VcCrossConnectTable.setStatus("mandatory")
_Xldv20VcCrossConnectEntry_Object = MibTableRow
xldv20VcCrossConnectEntry = _Xldv20VcCrossConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 6, 1)
)
xldv20VcCrossConnectEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20VcxIndex"),
)
if mibBuilder.loadTexts:
    xldv20VcCrossConnectEntry.setStatus("mandatory")
_Xldv20VcxOperationalState_Type = Xldv20OperState
_Xldv20VcxOperationalState_Object = MibTableColumn
xldv20VcxOperationalState = _Xldv20VcxOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 6, 1, 1),
    _Xldv20VcxOperationalState_Type()
)
xldv20VcxOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VcxOperationalState.setStatus("mandatory")


class _Xldv20VcxTerminationPointA_Type(Integer32):
    """Custom type xldv20VcxTerminationPointA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_Xldv20VcxTerminationPointA_Type.__name__ = "Integer32"
_Xldv20VcxTerminationPointA_Object = MibTableColumn
xldv20VcxTerminationPointA = _Xldv20VcxTerminationPointA_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 6, 1, 2),
    _Xldv20VcxTerminationPointA_Type()
)
xldv20VcxTerminationPointA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VcxTerminationPointA.setStatus("mandatory")


class _Xldv20VcxTerminationPointZ_Type(Integer32):
    """Custom type xldv20VcxTerminationPointZ based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_Xldv20VcxTerminationPointZ_Type.__name__ = "Integer32"
_Xldv20VcxTerminationPointZ_Object = MibTableColumn
xldv20VcxTerminationPointZ = _Xldv20VcxTerminationPointZ_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 6, 1, 3),
    _Xldv20VcxTerminationPointZ_Type()
)
xldv20VcxTerminationPointZ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VcxTerminationPointZ.setStatus("mandatory")
_Xldv20VcxLineIndex_Type = Unsigned16
_Xldv20VcxLineIndex_Object = MibTableColumn
xldv20VcxLineIndex = _Xldv20VcxLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 6, 1, 4),
    _Xldv20VcxLineIndex_Type()
)
xldv20VcxLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VcxLineIndex.setStatus("mandatory")


class _Xldv20VcxEthVpcIndex_Type(Integer32):
    """Custom type xldv20VcxEthVpcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_Xldv20VcxEthVpcIndex_Type.__name__ = "Integer32"
_Xldv20VcxEthVpcIndex_Object = MibTableColumn
xldv20VcxEthVpcIndex = _Xldv20VcxEthVpcIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 6, 1, 5),
    _Xldv20VcxEthVpcIndex_Type()
)
xldv20VcxEthVpcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VcxEthVpcIndex.setStatus("mandatory")


class _Xldv20VcxEthVccIndex_Type(Integer32):
    """Custom type xldv20VcxEthVccIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Xldv20VcxEthVccIndex_Type.__name__ = "Integer32"
_Xldv20VcxEthVccIndex_Object = MibTableColumn
xldv20VcxEthVccIndex = _Xldv20VcxEthVccIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 6, 1, 6),
    _Xldv20VcxEthVccIndex_Type()
)
xldv20VcxEthVccIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VcxEthVccIndex.setStatus("mandatory")
_Xldv20VcxVpcNniIndex_Type = Unsigned16
_Xldv20VcxVpcNniIndex_Object = MibTableColumn
xldv20VcxVpcNniIndex = _Xldv20VcxVpcNniIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 6, 1, 7),
    _Xldv20VcxVpcNniIndex_Type()
)
xldv20VcxVpcNniIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VcxVpcNniIndex.setStatus("mandatory")
_Xldv20VcxVpcUniIndex_Type = Unsigned16
_Xldv20VcxVpcUniIndex_Object = MibTableColumn
xldv20VcxVpcUniIndex = _Xldv20VcxVpcUniIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 6, 1, 8),
    _Xldv20VcxVpcUniIndex_Type()
)
xldv20VcxVpcUniIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VcxVpcUniIndex.setStatus("mandatory")


class _Xldv20VcxIndex_Type(Integer32):
    """Custom type xldv20VcxIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_Xldv20VcxIndex_Type.__name__ = "Integer32"
_Xldv20VcxIndex_Object = MibTableColumn
xldv20VcxIndex = _Xldv20VcxIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 6, 1, 9),
    _Xldv20VcxIndex_Type()
)
xldv20VcxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VcxIndex.setStatus("mandatory")
_Xldv20VcxAlarmState_Type = Xldv20CallpAlarmState
_Xldv20VcxAlarmState_Object = MibTableColumn
xldv20VcxAlarmState = _Xldv20VcxAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 6, 1, 10),
    _Xldv20VcxAlarmState_Type()
)
xldv20VcxAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VcxAlarmState.setStatus("mandatory")
_Xldv20VcxAdminState_Type = Xldv20AdminState
_Xldv20VcxAdminState_Object = MibTableColumn
xldv20VcxAdminState = _Xldv20VcxAdminState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 6, 1, 11),
    _Xldv20VcxAdminState_Type()
)
xldv20VcxAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20VcxAdminState.setStatus("mandatory")


class _Xldv20VcxAtmfVplIndex_Type(Integer32):
    """Custom type xldv20VcxAtmfVplIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4000),
    )


_Xldv20VcxAtmfVplIndex_Type.__name__ = "Integer32"
_Xldv20VcxAtmfVplIndex_Object = MibTableColumn
xldv20VcxAtmfVplIndex = _Xldv20VcxAtmfVplIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 6, 1, 12),
    _Xldv20VcxAtmfVplIndex_Type()
)
xldv20VcxAtmfVplIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VcxAtmfVplIndex.setStatus("mandatory")
_Xldv20VclTpTable_Object = MibTable
xldv20VclTpTable = _Xldv20VclTpTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 7)
)
if mibBuilder.loadTexts:
    xldv20VclTpTable.setStatus("mandatory")
_Xldv20VclTpEntry_Object = MibTableRow
xldv20VclTpEntry = _Xldv20VclTpEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 7, 1)
)
xldv20VclTpEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20VclIndex"),
)
if mibBuilder.loadTexts:
    xldv20VclTpEntry.setStatus("mandatory")
_Xldv20VclOperationalState_Type = Xldv20OperState
_Xldv20VclOperationalState_Object = MibTableColumn
xldv20VclOperationalState = _Xldv20VclOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 7, 1, 1),
    _Xldv20VclOperationalState_Type()
)
xldv20VclOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VclOperationalState.setStatus("mandatory")


class _Xldv20VclVpiValue_Type(Integer32):
    """Custom type xldv20VclVpiValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Xldv20VclVpiValue_Type.__name__ = "Integer32"
_Xldv20VclVpiValue_Object = MibTableColumn
xldv20VclVpiValue = _Xldv20VclVpiValue_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 7, 1, 2),
    _Xldv20VclVpiValue_Type()
)
xldv20VclVpiValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VclVpiValue.setStatus("mandatory")


class _Xldv20VclVciValue_Type(Integer32):
    """Custom type xldv20VclVciValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 3500),
    )


_Xldv20VclVciValue_Type.__name__ = "Integer32"
_Xldv20VclVciValue_Object = MibTableColumn
xldv20VclVciValue = _Xldv20VclVciValue_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 7, 1, 3),
    _Xldv20VclVciValue_Type()
)
xldv20VclVciValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VclVciValue.setStatus("mandatory")
_Xldv20VclHwUnitIndex_Type = Unsigned16
_Xldv20VclHwUnitIndex_Object = MibTableColumn
xldv20VclHwUnitIndex = _Xldv20VclHwUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 7, 1, 4),
    _Xldv20VclHwUnitIndex_Type()
)
xldv20VclHwUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VclHwUnitIndex.setStatus("mandatory")
_Xldv20VclIfIndex_Type = Unsigned16
_Xldv20VclIfIndex_Object = MibTableColumn
xldv20VclIfIndex = _Xldv20VclIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 7, 1, 5),
    _Xldv20VclIfIndex_Type()
)
xldv20VclIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VclIfIndex.setStatus("mandatory")
_Xldv20VclPeakCellRateUpstream_Type = Unsigned32
_Xldv20VclPeakCellRateUpstream_Object = MibTableColumn
xldv20VclPeakCellRateUpstream = _Xldv20VclPeakCellRateUpstream_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 7, 1, 6),
    _Xldv20VclPeakCellRateUpstream_Type()
)
xldv20VclPeakCellRateUpstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VclPeakCellRateUpstream.setStatus("mandatory")
_Xldv20VclPeakCellRateDownstream_Type = Unsigned32
_Xldv20VclPeakCellRateDownstream_Object = MibTableColumn
xldv20VclPeakCellRateDownstream = _Xldv20VclPeakCellRateDownstream_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 7, 1, 7),
    _Xldv20VclPeakCellRateDownstream_Type()
)
xldv20VclPeakCellRateDownstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VclPeakCellRateDownstream.setStatus("mandatory")


class _Xldv20VclCellDelayVariationToleranceUpstream_Type(Integer32):
    """Custom type xldv20VclCellDelayVariationToleranceUpstream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 200000),
    )


_Xldv20VclCellDelayVariationToleranceUpstream_Type.__name__ = "Integer32"
_Xldv20VclCellDelayVariationToleranceUpstream_Object = MibTableColumn
xldv20VclCellDelayVariationToleranceUpstream = _Xldv20VclCellDelayVariationToleranceUpstream_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 7, 1, 8),
    _Xldv20VclCellDelayVariationToleranceUpstream_Type()
)
xldv20VclCellDelayVariationToleranceUpstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VclCellDelayVariationToleranceUpstream.setStatus("mandatory")


class _Xldv20VclCellDelayVariationToleranceDownstream_Type(Integer32):
    """Custom type xldv20VclCellDelayVariationToleranceDownstream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 200000),
    )


_Xldv20VclCellDelayVariationToleranceDownstream_Type.__name__ = "Integer32"
_Xldv20VclCellDelayVariationToleranceDownstream_Object = MibTableColumn
xldv20VclCellDelayVariationToleranceDownstream = _Xldv20VclCellDelayVariationToleranceDownstream_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 7, 1, 9),
    _Xldv20VclCellDelayVariationToleranceDownstream_Type()
)
xldv20VclCellDelayVariationToleranceDownstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VclCellDelayVariationToleranceDownstream.setStatus("mandatory")
_Xldv20VclTrafficType_Type = Xldv20TrafficType
_Xldv20VclTrafficType_Object = MibTableColumn
xldv20VclTrafficType = _Xldv20VclTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 7, 1, 10),
    _Xldv20VclTrafficType_Type()
)
xldv20VclTrafficType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VclTrafficType.setStatus("mandatory")
_Xldv20VclTrafficDirection_Type = Xldv20TrafficDirection
_Xldv20VclTrafficDirection_Object = MibTableColumn
xldv20VclTrafficDirection = _Xldv20VclTrafficDirection_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 7, 1, 11),
    _Xldv20VclTrafficDirection_Type()
)
xldv20VclTrafficDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VclTrafficDirection.setStatus("mandatory")
_Xldv20VclConnectivityPointer_Type = Unsigned16
_Xldv20VclConnectivityPointer_Object = MibTableColumn
xldv20VclConnectivityPointer = _Xldv20VclConnectivityPointer_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 7, 1, 12),
    _Xldv20VclConnectivityPointer_Type()
)
xldv20VclConnectivityPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VclConnectivityPointer.setStatus("mandatory")
_Xldv20VclLineIndex_Type = Unsigned16
_Xldv20VclLineIndex_Object = MibTableColumn
xldv20VclLineIndex = _Xldv20VclLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 7, 1, 13),
    _Xldv20VclLineIndex_Type()
)
xldv20VclLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VclLineIndex.setStatus("mandatory")


class _Xldv20VclSegmentEndPoint_Type(Integer32):
    """Custom type xldv20VclSegmentEndPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Xldv20VclSegmentEndPoint_Type.__name__ = "Integer32"
_Xldv20VclSegmentEndPoint_Object = MibTableColumn
xldv20VclSegmentEndPoint = _Xldv20VclSegmentEndPoint_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 7, 1, 14),
    _Xldv20VclSegmentEndPoint_Type()
)
xldv20VclSegmentEndPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VclSegmentEndPoint.setStatus("mandatory")
_Xldv20VclSustainableCellRateUpstream_Type = Unsigned32
_Xldv20VclSustainableCellRateUpstream_Object = MibTableColumn
xldv20VclSustainableCellRateUpstream = _Xldv20VclSustainableCellRateUpstream_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 7, 1, 15),
    _Xldv20VclSustainableCellRateUpstream_Type()
)
xldv20VclSustainableCellRateUpstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VclSustainableCellRateUpstream.setStatus("mandatory")
_Xldv20VclSustainableCellRateDownstream_Type = Unsigned32
_Xldv20VclSustainableCellRateDownstream_Object = MibTableColumn
xldv20VclSustainableCellRateDownstream = _Xldv20VclSustainableCellRateDownstream_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 7, 1, 16),
    _Xldv20VclSustainableCellRateDownstream_Type()
)
xldv20VclSustainableCellRateDownstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VclSustainableCellRateDownstream.setStatus("mandatory")


class _Xldv20VclMaximumBurstSizeUpstream_Type(Integer32):
    """Custom type xldv20VclMaximumBurstSizeUpstream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_Xldv20VclMaximumBurstSizeUpstream_Type.__name__ = "Integer32"
_Xldv20VclMaximumBurstSizeUpstream_Object = MibTableColumn
xldv20VclMaximumBurstSizeUpstream = _Xldv20VclMaximumBurstSizeUpstream_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 7, 1, 17),
    _Xldv20VclMaximumBurstSizeUpstream_Type()
)
xldv20VclMaximumBurstSizeUpstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VclMaximumBurstSizeUpstream.setStatus("mandatory")


class _Xldv20VclMaximumBurstSizeDownstream_Type(Integer32):
    """Custom type xldv20VclMaximumBurstSizeDownstream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_Xldv20VclMaximumBurstSizeDownstream_Type.__name__ = "Integer32"
_Xldv20VclMaximumBurstSizeDownstream_Object = MibTableColumn
xldv20VclMaximumBurstSizeDownstream = _Xldv20VclMaximumBurstSizeDownstream_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 7, 1, 18),
    _Xldv20VclMaximumBurstSizeDownstream_Type()
)
xldv20VclMaximumBurstSizeDownstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VclMaximumBurstSizeDownstream.setStatus("mandatory")
_Xldv20VclAlarmSeverityIndex_Type = Xldv20AlmSevProfileIndex
_Xldv20VclAlarmSeverityIndex_Object = MibTableColumn
xldv20VclAlarmSeverityIndex = _Xldv20VclAlarmSeverityIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 7, 1, 19),
    _Xldv20VclAlarmSeverityIndex_Type()
)
xldv20VclAlarmSeverityIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20VclAlarmSeverityIndex.setStatus("mandatory")
_Xldv20VclAlarmFilteringIndex_Type = Xldv20AlmFiltProfileIndex
_Xldv20VclAlarmFilteringIndex_Object = MibTableColumn
xldv20VclAlarmFilteringIndex = _Xldv20VclAlarmFilteringIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 7, 1, 20),
    _Xldv20VclAlarmFilteringIndex_Type()
)
xldv20VclAlarmFilteringIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20VclAlarmFilteringIndex.setStatus("mandatory")
_Xldv20VclCvcIndexSegment_Type = Unsigned16
_Xldv20VclCvcIndexSegment_Object = MibTableColumn
xldv20VclCvcIndexSegment = _Xldv20VclCvcIndexSegment_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 7, 1, 21),
    _Xldv20VclCvcIndexSegment_Type()
)
xldv20VclCvcIndexSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VclCvcIndexSegment.setStatus("mandatory")


class _Xldv20VclIndex_Type(Integer32):
    """Custom type xldv20VclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4000),
    )


_Xldv20VclIndex_Type.__name__ = "Integer32"
_Xldv20VclIndex_Object = MibTableColumn
xldv20VclIndex = _Xldv20VclIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 7, 1, 22),
    _Xldv20VclIndex_Type()
)
xldv20VclIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VclIndex.setStatus("mandatory")
_Xldv20VclLOCAlarm_Type = Xldv20TpAlarmState
_Xldv20VclLOCAlarm_Object = MibTableColumn
xldv20VclLOCAlarm = _Xldv20VclLOCAlarm_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 7, 1, 23),
    _Xldv20VclLOCAlarm_Type()
)
xldv20VclLOCAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VclLOCAlarm.setStatus("mandatory")


class _Xldv20VclVpcIndex_Type(Integer32):
    """Custom type xldv20VclVpcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_Xldv20VclVpcIndex_Type.__name__ = "Integer32"
_Xldv20VclVpcIndex_Object = MibTableColumn
xldv20VclVpcIndex = _Xldv20VclVpcIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 7, 1, 24),
    _Xldv20VclVpcIndex_Type()
)
xldv20VclVpcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VclVpcIndex.setStatus("mandatory")


class _Xldv20VclVbrCDVTUpstream_Type(Integer32):
    """Custom type xldv20VclVbrCDVTUpstream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 504000000),
    )


_Xldv20VclVbrCDVTUpstream_Type.__name__ = "Integer32"
_Xldv20VclVbrCDVTUpstream_Object = MibTableColumn
xldv20VclVbrCDVTUpstream = _Xldv20VclVbrCDVTUpstream_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 7, 1, 25),
    _Xldv20VclVbrCDVTUpstream_Type()
)
xldv20VclVbrCDVTUpstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VclVbrCDVTUpstream.setStatus("mandatory")


class _Xldv20VclVbrCDVTDownstream_Type(Integer32):
    """Custom type xldv20VclVbrCDVTDownstream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 504000000),
    )


_Xldv20VclVbrCDVTDownstream_Type.__name__ = "Integer32"
_Xldv20VclVbrCDVTDownstream_Object = MibTableColumn
xldv20VclVbrCDVTDownstream = _Xldv20VclVbrCDVTDownstream_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 7, 1, 26),
    _Xldv20VclVbrCDVTDownstream_Type()
)
xldv20VclVbrCDVTDownstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20VclVbrCDVTDownstream.setStatus("mandatory")
_Xldv20EthernetConfigTable_Object = MibTable
xldv20EthernetConfigTable = _Xldv20EthernetConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 10)
)
if mibBuilder.loadTexts:
    xldv20EthernetConfigTable.setStatus("mandatory")
_Xldv20EthernetConfigEntry_Object = MibTableRow
xldv20EthernetConfigEntry = _Xldv20EthernetConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 10, 1)
)
xldv20EthernetConfigEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20IfIndex"),
)
if mibBuilder.loadTexts:
    xldv20EthernetConfigEntry.setStatus("mandatory")
_Xldv20EthMode_Type = Xldv20EthNtMode
_Xldv20EthMode_Object = MibTableColumn
xldv20EthMode = _Xldv20EthMode_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 10, 1, 1),
    _Xldv20EthMode_Type()
)
xldv20EthMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20EthMode.setStatus("mandatory")


class _Xldv20EthE164Isp_Type(OctetString):
    """Custom type xldv20EthE164Isp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Xldv20EthE164Isp_Type.__name__ = "OctetString"
_Xldv20EthE164Isp_Object = MibTableColumn
xldv20EthE164Isp = _Xldv20EthE164Isp_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 10, 1, 2),
    _Xldv20EthE164Isp_Type()
)
xldv20EthE164Isp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20EthE164Isp.setStatus("mandatory")
_Xldv20EthIpAddressNt_Type = IpAddress
_Xldv20EthIpAddressNt_Object = MibTableColumn
xldv20EthIpAddressNt = _Xldv20EthIpAddressNt_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 10, 1, 3),
    _Xldv20EthIpAddressNt_Type()
)
xldv20EthIpAddressNt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20EthIpAddressNt.setStatus("mandatory")
_Xldv20EthIpAddressSubnetMaskNt_Type = IpAddress
_Xldv20EthIpAddressSubnetMaskNt_Object = MibTableColumn
xldv20EthIpAddressSubnetMaskNt = _Xldv20EthIpAddressSubnetMaskNt_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 10, 1, 4),
    _Xldv20EthIpAddressSubnetMaskNt_Type()
)
xldv20EthIpAddressSubnetMaskNt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20EthIpAddressSubnetMaskNt.setStatus("mandatory")
_Xldv20EthIpAddressCo_Type = IpAddress
_Xldv20EthIpAddressCo_Object = MibTableColumn
xldv20EthIpAddressCo = _Xldv20EthIpAddressCo_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 10, 1, 5),
    _Xldv20EthIpAddressCo_Type()
)
xldv20EthIpAddressCo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20EthIpAddressCo.setStatus("mandatory")
_Xldv20EthIpAddressSubnetMaskCo_Type = IpAddress
_Xldv20EthIpAddressSubnetMaskCo_Object = MibTableColumn
xldv20EthIpAddressSubnetMaskCo = _Xldv20EthIpAddressSubnetMaskCo_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 10, 1, 6),
    _Xldv20EthIpAddressSubnetMaskCo_Type()
)
xldv20EthIpAddressSubnetMaskCo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20EthIpAddressSubnetMaskCo.setStatus("mandatory")
_Xldv20EthIpAddressRemoteRouter_Type = IpAddress
_Xldv20EthIpAddressRemoteRouter_Object = MibTableColumn
xldv20EthIpAddressRemoteRouter = _Xldv20EthIpAddressRemoteRouter_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 10, 1, 7),
    _Xldv20EthIpAddressRemoteRouter_Type()
)
xldv20EthIpAddressRemoteRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20EthIpAddressRemoteRouter.setStatus("mandatory")
_Xldv20ContinuityCheckVpTable_Object = MibTable
xldv20ContinuityCheckVpTable = _Xldv20ContinuityCheckVpTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 11)
)
if mibBuilder.loadTexts:
    xldv20ContinuityCheckVpTable.setStatus("mandatory")
_Xldv20ContinuityCheckVpEntry_Object = MibTableRow
xldv20ContinuityCheckVpEntry = _Xldv20ContinuityCheckVpEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 11, 1)
)
xldv20ContinuityCheckVpEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20CvpIndex"),
)
if mibBuilder.loadTexts:
    xldv20ContinuityCheckVpEntry.setStatus("mandatory")
_Xldv20CvpIndex_Type = Unsigned16
_Xldv20CvpIndex_Object = MibTableColumn
xldv20CvpIndex = _Xldv20CvpIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 11, 1, 1),
    _Xldv20CvpIndex_Type()
)
xldv20CvpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20CvpIndex.setStatus("mandatory")
_Xldv20CvpEndpointType_Type = Xldv20EndpointType
_Xldv20CvpEndpointType_Object = MibTableColumn
xldv20CvpEndpointType = _Xldv20CvpEndpointType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 11, 1, 2),
    _Xldv20CvpEndpointType_Type()
)
xldv20CvpEndpointType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20CvpEndpointType.setStatus("mandatory")
_Xldv20CvpTestType_Type = Xldv20TestType
_Xldv20CvpTestType_Object = MibTableColumn
xldv20CvpTestType = _Xldv20CvpTestType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 11, 1, 3),
    _Xldv20CvpTestType_Type()
)
xldv20CvpTestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20CvpTestType.setStatus("mandatory")
_Xldv20CvpOperationalState_Type = Xldv20OperState
_Xldv20CvpOperationalState_Object = MibTableColumn
xldv20CvpOperationalState = _Xldv20CvpOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 11, 1, 4),
    _Xldv20CvpOperationalState_Type()
)
xldv20CvpOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20CvpOperationalState.setStatus("mandatory")


class _Xldv20CvpVpTpIndex_Type(Integer32):
    """Custom type xldv20CvpVpTpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5000),
    )


_Xldv20CvpVpTpIndex_Type.__name__ = "Integer32"
_Xldv20CvpVpTpIndex_Object = MibTableColumn
xldv20CvpVpTpIndex = _Xldv20CvpVpTpIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 11, 1, 5),
    _Xldv20CvpVpTpIndex_Type()
)
xldv20CvpVpTpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20CvpVpTpIndex.setStatus("mandatory")
_Xldv20CvpObjectType_Type = Xldv20RepSource
_Xldv20CvpObjectType_Object = MibTableColumn
xldv20CvpObjectType = _Xldv20CvpObjectType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 11, 1, 6),
    _Xldv20CvpObjectType_Type()
)
xldv20CvpObjectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20CvpObjectType.setStatus("mandatory")
_Xldv20ContinuityCheckVcTable_Object = MibTable
xldv20ContinuityCheckVcTable = _Xldv20ContinuityCheckVcTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 12)
)
if mibBuilder.loadTexts:
    xldv20ContinuityCheckVcTable.setStatus("mandatory")
_Xldv20ContinuityCheckVcEntry_Object = MibTableRow
xldv20ContinuityCheckVcEntry = _Xldv20ContinuityCheckVcEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 12, 1)
)
xldv20ContinuityCheckVcEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20CvcIndex"),
)
if mibBuilder.loadTexts:
    xldv20ContinuityCheckVcEntry.setStatus("mandatory")
_Xldv20CvcIndex_Type = Unsigned16
_Xldv20CvcIndex_Object = MibTableColumn
xldv20CvcIndex = _Xldv20CvcIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 12, 1, 1),
    _Xldv20CvcIndex_Type()
)
xldv20CvcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20CvcIndex.setStatus("mandatory")
_Xldv20CvcEndpointType_Type = Xldv20EndpointType
_Xldv20CvcEndpointType_Object = MibTableColumn
xldv20CvcEndpointType = _Xldv20CvcEndpointType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 12, 1, 2),
    _Xldv20CvcEndpointType_Type()
)
xldv20CvcEndpointType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20CvcEndpointType.setStatus("mandatory")
_Xldv20CvcTestType_Type = Xldv20TestType
_Xldv20CvcTestType_Object = MibTableColumn
xldv20CvcTestType = _Xldv20CvcTestType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 12, 1, 3),
    _Xldv20CvcTestType_Type()
)
xldv20CvcTestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20CvcTestType.setStatus("mandatory")
_Xldv20CvcOperationalState_Type = Xldv20OperState
_Xldv20CvcOperationalState_Object = MibTableColumn
xldv20CvcOperationalState = _Xldv20CvcOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 12, 1, 4),
    _Xldv20CvcOperationalState_Type()
)
xldv20CvcOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20CvcOperationalState.setStatus("mandatory")


class _Xldv20CvcVcTpIndex_Type(Integer32):
    """Custom type xldv20CvcVcTpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4000),
    )


_Xldv20CvcVcTpIndex_Type.__name__ = "Integer32"
_Xldv20CvcVcTpIndex_Object = MibTableColumn
xldv20CvcVcTpIndex = _Xldv20CvcVcTpIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 12, 1, 5),
    _Xldv20CvcVcTpIndex_Type()
)
xldv20CvcVcTpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20CvcVcTpIndex.setStatus("mandatory")
_Xldv20CvcObjectType_Type = Xldv20RepSource
_Xldv20CvcObjectType_Object = MibTableColumn
xldv20CvcObjectType = _Xldv20CvcObjectType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 12, 1, 6),
    _Xldv20CvcObjectType_Type()
)
xldv20CvcObjectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20CvcObjectType.setStatus("mandatory")
_Xldv20ContinuityCheckControl_ObjectIdentity = ObjectIdentity
xldv20ContinuityCheckControl = _Xldv20ContinuityCheckControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 13)
)
_Xldv20CocControlReq_Type = Xldv20ControlReq
_Xldv20CocControlReq_Object = MibScalar
xldv20CocControlReq = _Xldv20CocControlReq_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 13, 1),
    _Xldv20CocControlReq_Type()
)
xldv20CocControlReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20CocControlReq.setStatus("mandatory")
_Xldv20CocControlStatus_Type = Xldv20ControlStatus
_Xldv20CocControlStatus_Object = MibScalar
xldv20CocControlStatus = _Xldv20CocControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 13, 2),
    _Xldv20CocControlStatus_Type()
)
xldv20CocControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20CocControlStatus.setStatus("mandatory")
_Xldv20CocEndpointType_Type = Xldv20EndpointType
_Xldv20CocEndpointType_Object = MibScalar
xldv20CocEndpointType = _Xldv20CocEndpointType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 13, 3),
    _Xldv20CocEndpointType_Type()
)
xldv20CocEndpointType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20CocEndpointType.setStatus("mandatory")
_Xldv20CocObjectType_Type = Xldv20RepSource
_Xldv20CocObjectType_Object = MibScalar
xldv20CocObjectType = _Xldv20CocObjectType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 13, 4),
    _Xldv20CocObjectType_Type()
)
xldv20CocObjectType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20CocObjectType.setStatus("mandatory")
_Xldv20CocTestType_Type = Xldv20TestType
_Xldv20CocTestType_Object = MibScalar
xldv20CocTestType = _Xldv20CocTestType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 13, 5),
    _Xldv20CocTestType_Type()
)
xldv20CocTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20CocTestType.setStatus("mandatory")
_Xldv20CocIndex_Type = Unsigned16
_Xldv20CocIndex_Object = MibScalar
xldv20CocIndex = _Xldv20CocIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 13, 6),
    _Xldv20CocIndex_Type()
)
xldv20CocIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20CocIndex.setStatus("mandatory")
_Xldv20CocControlReqResult_Type = Xldv20ControlReq
_Xldv20CocControlReqResult_Object = MibScalar
xldv20CocControlReqResult = _Xldv20CocControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 13, 7),
    _Xldv20CocControlReqResult_Type()
)
xldv20CocControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20CocControlReqResult.setStatus("mandatory")
_Xldv20CocControlTimeStamp_Type = TimeTicks
_Xldv20CocControlTimeStamp_Object = MibScalar
xldv20CocControlTimeStamp = _Xldv20CocControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 13, 8),
    _Xldv20CocControlTimeStamp_Type()
)
xldv20CocControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20CocControlTimeStamp.setStatus("mandatory")
_Xldv20InbandTmn_ObjectIdentity = ObjectIdentity
xldv20InbandTmn = _Xldv20InbandTmn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 14)
)


class _Xldv20InbandVpiCurrent_Type(Integer32):
    """Custom type xldv20InbandVpiCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Xldv20InbandVpiCurrent_Type.__name__ = "Integer32"
_Xldv20InbandVpiCurrent_Object = MibScalar
xldv20InbandVpiCurrent = _Xldv20InbandVpiCurrent_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 14, 1),
    _Xldv20InbandVpiCurrent_Type()
)
xldv20InbandVpiCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20InbandVpiCurrent.setStatus("mandatory")


class _Xldv20InbandVciCurrent_Type(Integer32):
    """Custom type xldv20InbandVciCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Xldv20InbandVciCurrent_Type.__name__ = "Integer32"
_Xldv20InbandVciCurrent_Object = MibScalar
xldv20InbandVciCurrent = _Xldv20InbandVciCurrent_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 14, 2),
    _Xldv20InbandVciCurrent_Type()
)
xldv20InbandVciCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20InbandVciCurrent.setStatus("mandatory")


class _Xldv20InbandVpiConfig_Type(Integer32):
    """Custom type xldv20InbandVpiConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Xldv20InbandVpiConfig_Type.__name__ = "Integer32"
_Xldv20InbandVpiConfig_Object = MibScalar
xldv20InbandVpiConfig = _Xldv20InbandVpiConfig_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 14, 3),
    _Xldv20InbandVpiConfig_Type()
)
xldv20InbandVpiConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20InbandVpiConfig.setStatus("mandatory")


class _Xldv20InbandVciConfig_Type(Integer32):
    """Custom type xldv20InbandVciConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Xldv20InbandVciConfig_Type.__name__ = "Integer32"
_Xldv20InbandVciConfig_Object = MibScalar
xldv20InbandVciConfig = _Xldv20InbandVciConfig_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 2, 14, 4),
    _Xldv20InbandVciConfig_Type()
)
xldv20InbandVciConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20InbandVciConfig.setStatus("mandatory")
_Xldv20Hwm_ObjectIdentity = ObjectIdentity
xldv20Hwm = _Xldv20Hwm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3)
)
_Xldv20AtmNe_ObjectIdentity = ObjectIdentity
xldv20AtmNe = _Xldv20AtmNe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 1)
)


class _Xldv20NeLocation_Type(OctetString):
    """Custom type xldv20NeLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Xldv20NeLocation_Type.__name__ = "OctetString"
_Xldv20NeLocation_Object = MibScalar
xldv20NeLocation = _Xldv20NeLocation_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 1, 1),
    _Xldv20NeLocation_Type()
)
xldv20NeLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20NeLocation.setStatus("mandatory")
_Xldv20NeVendor_Type = DisplayString
_Xldv20NeVendor_Object = MibScalar
xldv20NeVendor = _Xldv20NeVendor_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 1, 2),
    _Xldv20NeVendor_Type()
)
xldv20NeVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20NeVendor.setStatus("mandatory")
_Xldv20NeVersion_Type = DisplayString
_Xldv20NeVersion_Object = MibScalar
xldv20NeVersion = _Xldv20NeVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 1, 3),
    _Xldv20NeVersion_Type()
)
xldv20NeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20NeVersion.setStatus("mandatory")
_Xldv20NeExternalTime_Type = TimeTicks
_Xldv20NeExternalTime_Object = MibScalar
xldv20NeExternalTime = _Xldv20NeExternalTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 1, 4),
    _Xldv20NeExternalTime_Type()
)
xldv20NeExternalTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20NeExternalTime.setStatus("mandatory")
_Xldv20NeTimeZone_Type = Xldv20TimeZone
_Xldv20NeTimeZone_Object = MibScalar
xldv20NeTimeZone = _Xldv20NeTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 1, 5),
    _Xldv20NeTimeZone_Type()
)
xldv20NeTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20NeTimeZone.setStatus("mandatory")
_Xldv20NeDescriptorFileName_Type = DisplayString
_Xldv20NeDescriptorFileName_Object = MibScalar
xldv20NeDescriptorFileName = _Xldv20NeDescriptorFileName_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 1, 6),
    _Xldv20NeDescriptorFileName_Type()
)
xldv20NeDescriptorFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20NeDescriptorFileName.setStatus("mandatory")
_Xldv20NeExternalTime45020_Type = TimeTicks
_Xldv20NeExternalTime45020_Object = MibScalar
xldv20NeExternalTime45020 = _Xldv20NeExternalTime45020_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 1, 7),
    _Xldv20NeExternalTime45020_Type()
)
xldv20NeExternalTime45020.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20NeExternalTime45020.setStatus("mandatory")
_Xldv20NeSummerTime_Type = Xldv20DayLightSavingTime
_Xldv20NeSummerTime_Object = MibScalar
xldv20NeSummerTime = _Xldv20NeSummerTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 1, 8),
    _Xldv20NeSummerTime_Type()
)
xldv20NeSummerTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20NeSummerTime.setStatus("mandatory")
_Xldv20HwUnitTable_Object = MibTable
xldv20HwUnitTable = _Xldv20HwUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 2)
)
if mibBuilder.loadTexts:
    xldv20HwUnitTable.setStatus("mandatory")
_Xldv20HwUnitEntry_Object = MibTableRow
xldv20HwUnitEntry = _Xldv20HwUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 2, 1)
)
xldv20HwUnitEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20HwUnitIndex"),
)
if mibBuilder.loadTexts:
    xldv20HwUnitEntry.setStatus("mandatory")
_Xldv20HwUnitIndex_Type = Unsigned16
_Xldv20HwUnitIndex_Object = MibTableColumn
xldv20HwUnitIndex = _Xldv20HwUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 2, 1, 1),
    _Xldv20HwUnitIndex_Type()
)
xldv20HwUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20HwUnitIndex.setStatus("mandatory")
_Xldv20HwUnitType_Type = Xldv20HwUnitType
_Xldv20HwUnitType_Object = MibTableColumn
xldv20HwUnitType = _Xldv20HwUnitType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 2, 1, 2),
    _Xldv20HwUnitType_Type()
)
xldv20HwUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20HwUnitType.setStatus("mandatory")
_Xldv20HwContainmentTable_Object = MibTable
xldv20HwContainmentTable = _Xldv20HwContainmentTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 3)
)
if mibBuilder.loadTexts:
    xldv20HwContainmentTable.setStatus("mandatory")
_Xldv20HwContainmentEntry_Object = MibTableRow
xldv20HwContainmentEntry = _Xldv20HwContainmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 3, 1)
)
xldv20HwContainmentEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20HwContainingUnitIndex"),
    (0, "XLDV20-MIB", "xldv20HwContainedUnitAddr"),
)
if mibBuilder.loadTexts:
    xldv20HwContainmentEntry.setStatus("mandatory")
_Xldv20HwContainingUnitIndex_Type = Unsigned16
_Xldv20HwContainingUnitIndex_Object = MibTableColumn
xldv20HwContainingUnitIndex = _Xldv20HwContainingUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 3, 1, 1),
    _Xldv20HwContainingUnitIndex_Type()
)
xldv20HwContainingUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20HwContainingUnitIndex.setStatus("mandatory")


class _Xldv20HwContainedUnitAddr_Type(Integer32):
    """Custom type xldv20HwContainedUnitAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_Xldv20HwContainedUnitAddr_Type.__name__ = "Integer32"
_Xldv20HwContainedUnitAddr_Object = MibTableColumn
xldv20HwContainedUnitAddr = _Xldv20HwContainedUnitAddr_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 3, 1, 2),
    _Xldv20HwContainedUnitAddr_Type()
)
xldv20HwContainedUnitAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20HwContainedUnitAddr.setStatus("mandatory")
_Xldv20HwContainedUnitIndex_Type = Unsigned16
_Xldv20HwContainedUnitIndex_Object = MibTableColumn
xldv20HwContainedUnitIndex = _Xldv20HwContainedUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 3, 1, 3),
    _Xldv20HwContainedUnitIndex_Type()
)
xldv20HwContainedUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20HwContainedUnitIndex.setStatus("mandatory")
_Xldv20HwEquipTable_Object = MibTable
xldv20HwEquipTable = _Xldv20HwEquipTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 4)
)
if mibBuilder.loadTexts:
    xldv20HwEquipTable.setStatus("mandatory")
_Xldv20HwEquipEntry_Object = MibTableRow
xldv20HwEquipEntry = _Xldv20HwEquipEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 4, 1)
)
xldv20HwEquipEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20HwUnitIndex"),
)
if mibBuilder.loadTexts:
    xldv20HwEquipEntry.setStatus("mandatory")


class _Xldv20EquType_Type(DisplayString):
    """Custom type xldv20EquType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Xldv20EquType_Type.__name__ = "DisplayString"
_Xldv20EquType_Object = MibTableColumn
xldv20EquType = _Xldv20EquType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 4, 1, 1),
    _Xldv20EquType_Type()
)
xldv20EquType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20EquType.setStatus("mandatory")


class _Xldv20EquLocation_Type(OctetString):
    """Custom type xldv20EquLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Xldv20EquLocation_Type.__name__ = "OctetString"
_Xldv20EquLocation_Object = MibTableColumn
xldv20EquLocation = _Xldv20EquLocation_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 4, 1, 2),
    _Xldv20EquLocation_Type()
)
xldv20EquLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20EquLocation.setStatus("mandatory")


class _Xldv20EquUserLabel_Type(OctetString):
    """Custom type xldv20EquUserLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Xldv20EquUserLabel_Type.__name__ = "OctetString"
_Xldv20EquUserLabel_Object = MibTableColumn
xldv20EquUserLabel = _Xldv20EquUserLabel_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 4, 1, 3),
    _Xldv20EquUserLabel_Type()
)
xldv20EquUserLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20EquUserLabel.setStatus("mandatory")
_Xldv20EquConnectedPiuIndex_Type = Unsigned16
_Xldv20EquConnectedPiuIndex_Object = MibTableColumn
xldv20EquConnectedPiuIndex = _Xldv20EquConnectedPiuIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 4, 1, 4),
    _Xldv20EquConnectedPiuIndex_Type()
)
xldv20EquConnectedPiuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20EquConnectedPiuIndex.setStatus("mandatory")


class _Xldv20EquConnectedPiuPort_Type(Integer32):
    """Custom type xldv20EquConnectedPiuPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Xldv20EquConnectedPiuPort_Type.__name__ = "Integer32"
_Xldv20EquConnectedPiuPort_Object = MibTableColumn
xldv20EquConnectedPiuPort = _Xldv20EquConnectedPiuPort_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 4, 1, 5),
    _Xldv20EquConnectedPiuPort_Type()
)
xldv20EquConnectedPiuPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20EquConnectedPiuPort.setStatus("mandatory")
_Xldv20HwEquipHolderTable_Object = MibTable
xldv20HwEquipHolderTable = _Xldv20HwEquipHolderTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 5)
)
if mibBuilder.loadTexts:
    xldv20HwEquipHolderTable.setStatus("mandatory")
_Xldv20HwEquipHolderEntry_Object = MibTableRow
xldv20HwEquipHolderEntry = _Xldv20HwEquipHolderEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 5, 1)
)
xldv20HwEquipHolderEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20HwUnitIndex"),
)
if mibBuilder.loadTexts:
    xldv20HwEquipHolderEntry.setStatus("mandatory")
_Xldv20EqhType_Type = Xldv20EqhType
_Xldv20EqhType_Object = MibTableColumn
xldv20EqhType = _Xldv20EqhType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 5, 1, 1),
    _Xldv20EqhType_Type()
)
xldv20EqhType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20EqhType.setStatus("mandatory")


class _Xldv20EqhAccPiuTypes_Type(DisplayString):
    """Custom type xldv20EqhAccPiuTypes based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_Xldv20EqhAccPiuTypes_Type.__name__ = "DisplayString"
_Xldv20EqhAccPiuTypes_Object = MibTableColumn
xldv20EqhAccPiuTypes = _Xldv20EqhAccPiuTypes_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 5, 1, 2),
    _Xldv20EqhAccPiuTypes_Type()
)
xldv20EqhAccPiuTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20EqhAccPiuTypes.setStatus("mandatory")
_Xldv20EqhSlotStatus_Type = Xldv20SlotStatus
_Xldv20EqhSlotStatus_Object = MibTableColumn
xldv20EqhSlotStatus = _Xldv20EqhSlotStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 5, 1, 3),
    _Xldv20EqhSlotStatus_Type()
)
xldv20EqhSlotStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20EqhSlotStatus.setStatus("mandatory")


class _Xldv20EqhSwVersion_Type(OctetString):
    """Custom type xldv20EqhSwVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Xldv20EqhSwVersion_Type.__name__ = "OctetString"
_Xldv20EqhSwVersion_Object = MibTableColumn
xldv20EqhSwVersion = _Xldv20EqhSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 5, 1, 4),
    _Xldv20EqhSwVersion_Type()
)
xldv20EqhSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20EqhSwVersion.setStatus("mandatory")


class _Xldv20EqhMnemoCode_Type(OctetString):
    """Custom type xldv20EqhMnemoCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_Xldv20EqhMnemoCode_Type.__name__ = "OctetString"
_Xldv20EqhMnemoCode_Object = MibTableColumn
xldv20EqhMnemoCode = _Xldv20EqhMnemoCode_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 5, 1, 5),
    _Xldv20EqhMnemoCode_Type()
)
xldv20EqhMnemoCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20EqhMnemoCode.setStatus("mandatory")


class _Xldv20EqhFwCode_Type(OctetString):
    """Custom type xldv20EqhFwCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Xldv20EqhFwCode_Type.__name__ = "OctetString"
_Xldv20EqhFwCode_Object = MibTableColumn
xldv20EqhFwCode = _Xldv20EqhFwCode_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 5, 1, 6),
    _Xldv20EqhFwCode_Type()
)
xldv20EqhFwCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20EqhFwCode.setStatus("mandatory")


class _Xldv20EqhRiMnemoCode_Type(DisplayString):
    """Custom type xldv20EqhRiMnemoCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Xldv20EqhRiMnemoCode_Type.__name__ = "DisplayString"
_Xldv20EqhRiMnemoCode_Object = MibTableColumn
xldv20EqhRiMnemoCode = _Xldv20EqhRiMnemoCode_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 5, 1, 7),
    _Xldv20EqhRiMnemoCode_Type()
)
xldv20EqhRiMnemoCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20EqhRiMnemoCode.setStatus("mandatory")


class _Xldv20EqhRiFwItemNumber_Type(DisplayString):
    """Custom type xldv20EqhRiFwItemNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Xldv20EqhRiFwItemNumber_Type.__name__ = "DisplayString"
_Xldv20EqhRiFwItemNumber_Object = MibTableColumn
xldv20EqhRiFwItemNumber = _Xldv20EqhRiFwItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 5, 1, 8),
    _Xldv20EqhRiFwItemNumber_Type()
)
xldv20EqhRiFwItemNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20EqhRiFwItemNumber.setStatus("mandatory")


class _Xldv20EqhRiFwIssue_Type(DisplayString):
    """Custom type xldv20EqhRiFwIssue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Xldv20EqhRiFwIssue_Type.__name__ = "DisplayString"
_Xldv20EqhRiFwIssue_Object = MibTableColumn
xldv20EqhRiFwIssue = _Xldv20EqhRiFwIssue_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 5, 1, 9),
    _Xldv20EqhRiFwIssue_Type()
)
xldv20EqhRiFwIssue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20EqhRiFwIssue.setStatus("mandatory")


class _Xldv20EqhRiHwItemNumber_Type(DisplayString):
    """Custom type xldv20EqhRiHwItemNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Xldv20EqhRiHwItemNumber_Type.__name__ = "DisplayString"
_Xldv20EqhRiHwItemNumber_Object = MibTableColumn
xldv20EqhRiHwItemNumber = _Xldv20EqhRiHwItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 5, 1, 10),
    _Xldv20EqhRiHwItemNumber_Type()
)
xldv20EqhRiHwItemNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20EqhRiHwItemNumber.setStatus("mandatory")


class _Xldv20EqhRiHwIssue_Type(DisplayString):
    """Custom type xldv20EqhRiHwIssue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Xldv20EqhRiHwIssue_Type.__name__ = "DisplayString"
_Xldv20EqhRiHwIssue_Object = MibTableColumn
xldv20EqhRiHwIssue = _Xldv20EqhRiHwIssue_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 5, 1, 11),
    _Xldv20EqhRiHwIssue_Type()
)
xldv20EqhRiHwIssue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20EqhRiHwIssue.setStatus("mandatory")


class _Xldv20EqhRiSerialNumber_Type(DisplayString):
    """Custom type xldv20EqhRiSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Xldv20EqhRiSerialNumber_Type.__name__ = "DisplayString"
_Xldv20EqhRiSerialNumber_Object = MibTableColumn
xldv20EqhRiSerialNumber = _Xldv20EqhRiSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 5, 1, 12),
    _Xldv20EqhRiSerialNumber_Type()
)
xldv20EqhRiSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20EqhRiSerialNumber.setStatus("mandatory")
_Xldv20HwPlugInUnitTable_Object = MibTable
xldv20HwPlugInUnitTable = _Xldv20HwPlugInUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 6)
)
if mibBuilder.loadTexts:
    xldv20HwPlugInUnitTable.setStatus("mandatory")
_Xldv20HwPlugInUnitEntry_Object = MibTableRow
xldv20HwPlugInUnitEntry = _Xldv20HwPlugInUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 6, 1)
)
xldv20HwPlugInUnitEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20HwUnitIndex"),
)
if mibBuilder.loadTexts:
    xldv20HwPlugInUnitEntry.setStatus("mandatory")
_Xldv20PiuAdminState_Type = Xldv20AdminState
_Xldv20PiuAdminState_Object = MibTableColumn
xldv20PiuAdminState = _Xldv20PiuAdminState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 6, 1, 1),
    _Xldv20PiuAdminState_Type()
)
xldv20PiuAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20PiuAdminState.setStatus("mandatory")
_Xldv20PiuAvailStatus_Type = Xldv20AvailStatus
_Xldv20PiuAvailStatus_Object = MibTableColumn
xldv20PiuAvailStatus = _Xldv20PiuAvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 6, 1, 2),
    _Xldv20PiuAvailStatus_Type()
)
xldv20PiuAvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20PiuAvailStatus.setStatus("mandatory")
_Xldv20PiuOperState_Type = Xldv20OperState
_Xldv20PiuOperState_Object = MibTableColumn
xldv20PiuOperState = _Xldv20PiuOperState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 6, 1, 3),
    _Xldv20PiuOperState_Type()
)
xldv20PiuOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20PiuOperState.setStatus("mandatory")


class _Xldv20PiuType_Type(DisplayString):
    """Custom type xldv20PiuType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Xldv20PiuType_Type.__name__ = "DisplayString"
_Xldv20PiuType_Object = MibTableColumn
xldv20PiuType = _Xldv20PiuType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 6, 1, 4),
    _Xldv20PiuType_Type()
)
xldv20PiuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20PiuType.setStatus("mandatory")
_Xldv20PiuAlarmSeverityIndex_Type = Xldv20AlmSevProfileIndex
_Xldv20PiuAlarmSeverityIndex_Object = MibTableColumn
xldv20PiuAlarmSeverityIndex = _Xldv20PiuAlarmSeverityIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 6, 1, 5),
    _Xldv20PiuAlarmSeverityIndex_Type()
)
xldv20PiuAlarmSeverityIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20PiuAlarmSeverityIndex.setStatus("mandatory")
_Xldv20PiuAlarmFilteringIndex_Type = Xldv20AlmFiltProfileIndex
_Xldv20PiuAlarmFilteringIndex_Object = MibTableColumn
xldv20PiuAlarmFilteringIndex = _Xldv20PiuAlarmFilteringIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 6, 1, 6),
    _Xldv20PiuAlarmFilteringIndex_Type()
)
xldv20PiuAlarmFilteringIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20PiuAlarmFilteringIndex.setStatus("mandatory")
_Xldv20PiuUpgradeResult_Type = Xldv20ControlReq
_Xldv20PiuUpgradeResult_Object = MibTableColumn
xldv20PiuUpgradeResult = _Xldv20PiuUpgradeResult_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 6, 1, 7),
    _Xldv20PiuUpgradeResult_Type()
)
xldv20PiuUpgradeResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20PiuUpgradeResult.setStatus("mandatory")
_Xldv20HwuControl_ObjectIdentity = ObjectIdentity
xldv20HwuControl = _Xldv20HwuControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 7)
)
_Xldv20HwuControlReq_Type = Xldv20ControlReq
_Xldv20HwuControlReq_Object = MibScalar
xldv20HwuControlReq = _Xldv20HwuControlReq_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 7, 1),
    _Xldv20HwuControlReq_Type()
)
xldv20HwuControlReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20HwuControlReq.setStatus("mandatory")
_Xldv20HwuControlStatus_Type = Xldv20ControlStatus
_Xldv20HwuControlStatus_Object = MibScalar
xldv20HwuControlStatus = _Xldv20HwuControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 7, 2),
    _Xldv20HwuControlStatus_Type()
)
xldv20HwuControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20HwuControlStatus.setStatus("mandatory")
_Xldv20HwuUnitType_Type = Xldv20HwUnitType
_Xldv20HwuUnitType_Object = MibScalar
xldv20HwuUnitType = _Xldv20HwuUnitType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 7, 3),
    _Xldv20HwuUnitType_Type()
)
xldv20HwuUnitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20HwuUnitType.setStatus("mandatory")


class _Xldv20HwuEquType_Type(OctetString):
    """Custom type xldv20HwuEquType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_Xldv20HwuEquType_Type.__name__ = "OctetString"
_Xldv20HwuEquType_Object = MibScalar
xldv20HwuEquType = _Xldv20HwuEquType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 7, 4),
    _Xldv20HwuEquType_Type()
)
xldv20HwuEquType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20HwuEquType.setStatus("mandatory")
_Xldv20HwuEqhType_Type = Xldv20EqhType
_Xldv20HwuEqhType_Object = MibScalar
xldv20HwuEqhType = _Xldv20HwuEqhType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 7, 5),
    _Xldv20HwuEqhType_Type()
)
xldv20HwuEqhType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20HwuEqhType.setStatus("mandatory")


class _Xldv20HwuPiuType_Type(OctetString):
    """Custom type xldv20HwuPiuType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_Xldv20HwuPiuType_Type.__name__ = "OctetString"
_Xldv20HwuPiuType_Object = MibScalar
xldv20HwuPiuType = _Xldv20HwuPiuType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 7, 6),
    _Xldv20HwuPiuType_Type()
)
xldv20HwuPiuType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20HwuPiuType.setStatus("mandatory")
_Xldv20HwuContainingUnitIndex_Type = Unsigned16
_Xldv20HwuContainingUnitIndex_Object = MibScalar
xldv20HwuContainingUnitIndex = _Xldv20HwuContainingUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 7, 7),
    _Xldv20HwuContainingUnitIndex_Type()
)
xldv20HwuContainingUnitIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20HwuContainingUnitIndex.setStatus("mandatory")


class _Xldv20HwuContainedUnitAddr_Type(Integer32):
    """Custom type xldv20HwuContainedUnitAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_Xldv20HwuContainedUnitAddr_Type.__name__ = "Integer32"
_Xldv20HwuContainedUnitAddr_Object = MibScalar
xldv20HwuContainedUnitAddr = _Xldv20HwuContainedUnitAddr_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 7, 8),
    _Xldv20HwuContainedUnitAddr_Type()
)
xldv20HwuContainedUnitAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20HwuContainedUnitAddr.setStatus("mandatory")
_Xldv20HwuUnitIndex_Type = Unsigned16
_Xldv20HwuUnitIndex_Object = MibScalar
xldv20HwuUnitIndex = _Xldv20HwuUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 7, 9),
    _Xldv20HwuUnitIndex_Type()
)
xldv20HwuUnitIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20HwuUnitIndex.setStatus("mandatory")
_Xldv20HwuControlTimer_Type = Unsigned32
_Xldv20HwuControlTimer_Object = MibScalar
xldv20HwuControlTimer = _Xldv20HwuControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 7, 10),
    _Xldv20HwuControlTimer_Type()
)
xldv20HwuControlTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20HwuControlTimer.setStatus("mandatory")
_Xldv20HwuControlReqResult_Type = Xldv20ControlReq
_Xldv20HwuControlReqResult_Object = MibScalar
xldv20HwuControlReqResult = _Xldv20HwuControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 7, 11),
    _Xldv20HwuControlReqResult_Type()
)
xldv20HwuControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20HwuControlReqResult.setStatus("mandatory")
_Xldv20HwuControlTimeStamp_Type = TimeTicks
_Xldv20HwuControlTimeStamp_Object = MibScalar
xldv20HwuControlTimeStamp = _Xldv20HwuControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 7, 12),
    _Xldv20HwuControlTimeStamp_Type()
)
xldv20HwuControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20HwuControlTimeStamp.setStatus("mandatory")
_Xldv20RemoteInventory_ObjectIdentity = ObjectIdentity
xldv20RemoteInventory = _Xldv20RemoteInventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 9)
)
_Xldv20RiControlReq_Type = Xldv20ControlReq
_Xldv20RiControlReq_Object = MibScalar
xldv20RiControlReq = _Xldv20RiControlReq_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 9, 1),
    _Xldv20RiControlReq_Type()
)
xldv20RiControlReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20RiControlReq.setStatus("mandatory")
_Xldv20RiControlStatus_Type = Xldv20ControlStatus
_Xldv20RiControlStatus_Object = MibScalar
xldv20RiControlStatus = _Xldv20RiControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 9, 2),
    _Xldv20RiControlStatus_Type()
)
xldv20RiControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20RiControlStatus.setStatus("mandatory")
_Xldv20RiControlTimer_Type = Unsigned32
_Xldv20RiControlTimer_Object = MibScalar
xldv20RiControlTimer = _Xldv20RiControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 9, 3),
    _Xldv20RiControlTimer_Type()
)
xldv20RiControlTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20RiControlTimer.setStatus("mandatory")


class _Xldv20RiResultFilePath_Type(OctetString):
    """Custom type xldv20RiResultFilePath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_Xldv20RiResultFilePath_Type.__name__ = "OctetString"
_Xldv20RiResultFilePath_Object = MibScalar
xldv20RiResultFilePath = _Xldv20RiResultFilePath_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 9, 4),
    _Xldv20RiResultFilePath_Type()
)
xldv20RiResultFilePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20RiResultFilePath.setStatus("mandatory")
_Xldv20RiHwUnitIndex_Type = Unsigned16
_Xldv20RiHwUnitIndex_Object = MibScalar
xldv20RiHwUnitIndex = _Xldv20RiHwUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 9, 5),
    _Xldv20RiHwUnitIndex_Type()
)
xldv20RiHwUnitIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20RiHwUnitIndex.setStatus("mandatory")
_Xldv20RiControlReqResult_Type = Xldv20ControlReq
_Xldv20RiControlReqResult_Object = MibScalar
xldv20RiControlReqResult = _Xldv20RiControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 9, 6),
    _Xldv20RiControlReqResult_Type()
)
xldv20RiControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20RiControlReqResult.setStatus("mandatory")
_Xldv20RiControlTimeStamp_Type = TimeTicks
_Xldv20RiControlTimeStamp_Object = MibScalar
xldv20RiControlTimeStamp = _Xldv20RiControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 9, 7),
    _Xldv20RiControlTimeStamp_Type()
)
xldv20RiControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20RiControlTimeStamp.setStatus("mandatory")
_Xldv20HwUnitMappingTable_Object = MibTable
xldv20HwUnitMappingTable = _Xldv20HwUnitMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 10)
)
if mibBuilder.loadTexts:
    xldv20HwUnitMappingTable.setStatus("mandatory")
_Xldv20HwUnitMappingEntry_Object = MibTableRow
xldv20HwUnitMappingEntry = _Xldv20HwUnitMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 10, 1)
)
xldv20HwUnitMappingEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20HwmHwUnitIndex"),
    (0, "XLDV20-MIB", "xldv20HwmIfIndex"),
)
if mibBuilder.loadTexts:
    xldv20HwUnitMappingEntry.setStatus("mandatory")
_Xldv20HwmHwUnitIndex_Type = Unsigned16
_Xldv20HwmHwUnitIndex_Object = MibTableColumn
xldv20HwmHwUnitIndex = _Xldv20HwmHwUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 10, 1, 1),
    _Xldv20HwmHwUnitIndex_Type()
)
xldv20HwmHwUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20HwmHwUnitIndex.setStatus("mandatory")
_Xldv20HwmIfIndex_Type = Unsigned16
_Xldv20HwmIfIndex_Object = MibTableColumn
xldv20HwmIfIndex = _Xldv20HwmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 3, 10, 1, 2),
    _Xldv20HwmIfIndex_Type()
)
xldv20HwmIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20HwmIfIndex.setStatus("mandatory")
_Xldv20Tlm_ObjectIdentity = ObjectIdentity
xldv20Tlm = _Xldv20Tlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4)
)
_Xldv20IfTable_Object = MibTable
xldv20IfTable = _Xldv20IfTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 1)
)
if mibBuilder.loadTexts:
    xldv20IfTable.setStatus("mandatory")
_Xldv20IfEntry_Object = MibTableRow
xldv20IfEntry = _Xldv20IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 1, 1)
)
xldv20IfEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20IfIndex"),
)
if mibBuilder.loadTexts:
    xldv20IfEntry.setStatus("mandatory")
_Xldv20IfIndex_Type = Unsigned16
_Xldv20IfIndex_Object = MibTableColumn
xldv20IfIndex = _Xldv20IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 1, 1, 1),
    _Xldv20IfIndex_Type()
)
xldv20IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20IfIndex.setStatus("mandatory")
_Xldv20IfType_Type = Xldv20IfType
_Xldv20IfType_Object = MibTableColumn
xldv20IfType = _Xldv20IfType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 1, 1, 2),
    _Xldv20IfType_Type()
)
xldv20IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20IfType.setStatus("mandatory")
_Xldv20IfLineIndex_Type = Unsigned16
_Xldv20IfLineIndex_Object = MibTableColumn
xldv20IfLineIndex = _Xldv20IfLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 1, 1, 3),
    _Xldv20IfLineIndex_Type()
)
xldv20IfLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20IfLineIndex.setStatus("mandatory")
_Xldv20IfHwUnitIndex_Type = Unsigned16
_Xldv20IfHwUnitIndex_Object = MibTableColumn
xldv20IfHwUnitIndex = _Xldv20IfHwUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 1, 1, 4),
    _Xldv20IfHwUnitIndex_Type()
)
xldv20IfHwUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20IfHwUnitIndex.setStatus("mandatory")


class _Xldv20IfHwPortId_Type(Integer32):
    """Custom type xldv20IfHwPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Xldv20IfHwPortId_Type.__name__ = "Integer32"
_Xldv20IfHwPortId_Object = MibTableColumn
xldv20IfHwPortId = _Xldv20IfHwPortId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 1, 1, 5),
    _Xldv20IfHwPortId_Type()
)
xldv20IfHwPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20IfHwPortId.setStatus("mandatory")
_Xldv20IfConnectivityIndex_Type = Unsigned16
_Xldv20IfConnectivityIndex_Object = MibTableColumn
xldv20IfConnectivityIndex = _Xldv20IfConnectivityIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 1, 1, 6),
    _Xldv20IfConnectivityIndex_Type()
)
xldv20IfConnectivityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20IfConnectivityIndex.setStatus("mandatory")
_Xldv20IfOperState_Type = Xldv20OperState
_Xldv20IfOperState_Object = MibTableColumn
xldv20IfOperState = _Xldv20IfOperState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 1, 1, 7),
    _Xldv20IfOperState_Type()
)
xldv20IfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20IfOperState.setStatus("mandatory")
_Xldv20IfAdminState_Type = Xldv20AdminState
_Xldv20IfAdminState_Object = MibTableColumn
xldv20IfAdminState = _Xldv20IfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 1, 1, 8),
    _Xldv20IfAdminState_Type()
)
xldv20IfAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20IfAdminState.setStatus("mandatory")
_Xldv20IfAlarmState_Type = Xldv20AlarmState
_Xldv20IfAlarmState_Object = MibTableColumn
xldv20IfAlarmState = _Xldv20IfAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 1, 1, 9),
    _Xldv20IfAlarmState_Type()
)
xldv20IfAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20IfAlarmState.setStatus("mandatory")
_Xldv20IfAlarmSeverityIndex_Type = Xldv20AlmSevProfileIndex
_Xldv20IfAlarmSeverityIndex_Object = MibTableColumn
xldv20IfAlarmSeverityIndex = _Xldv20IfAlarmSeverityIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 1, 1, 10),
    _Xldv20IfAlarmSeverityIndex_Type()
)
xldv20IfAlarmSeverityIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20IfAlarmSeverityIndex.setStatus("mandatory")
_Xldv20IfAlarmFilteringIndex_Type = Xldv20AlmFiltProfileIndex
_Xldv20IfAlarmFilteringIndex_Object = MibTableColumn
xldv20IfAlarmFilteringIndex = _Xldv20IfAlarmFilteringIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 1, 1, 11),
    _Xldv20IfAlarmFilteringIndex_Type()
)
xldv20IfAlarmFilteringIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20IfAlarmFilteringIndex.setStatus("mandatory")
_Xldv20AdcControl_ObjectIdentity = ObjectIdentity
xldv20AdcControl = _Xldv20AdcControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 2)
)
_Xldv20AdcCtrlControlReq_Type = Xldv20ControlReq
_Xldv20AdcCtrlControlReq_Object = MibScalar
xldv20AdcCtrlControlReq = _Xldv20AdcCtrlControlReq_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 2, 1),
    _Xldv20AdcCtrlControlReq_Type()
)
xldv20AdcCtrlControlReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20AdcCtrlControlReq.setStatus("mandatory")
_Xldv20AdcCtrlControlStatus_Type = Xldv20ControlStatus
_Xldv20AdcCtrlControlStatus_Object = MibScalar
xldv20AdcCtrlControlStatus = _Xldv20AdcCtrlControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 2, 2),
    _Xldv20AdcCtrlControlStatus_Type()
)
xldv20AdcCtrlControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AdcCtrlControlStatus.setStatus("mandatory")
_Xldv20AdcCtrlIfIndex_Type = Unsigned16
_Xldv20AdcCtrlIfIndex_Object = MibScalar
xldv20AdcCtrlIfIndex = _Xldv20AdcCtrlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 2, 3),
    _Xldv20AdcCtrlIfIndex_Type()
)
xldv20AdcCtrlIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20AdcCtrlIfIndex.setStatus("mandatory")
_Xldv20AdcCtrlMinRateDn_Type = Xldv20AdslDataRateDown
_Xldv20AdcCtrlMinRateDn_Object = MibScalar
xldv20AdcCtrlMinRateDn = _Xldv20AdcCtrlMinRateDn_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 2, 4),
    _Xldv20AdcCtrlMinRateDn_Type()
)
xldv20AdcCtrlMinRateDn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20AdcCtrlMinRateDn.setStatus("mandatory")
_Xldv20AdcCtrlMinRateUp_Type = Xldv20AdslDataRateUp
_Xldv20AdcCtrlMinRateUp_Object = MibScalar
xldv20AdcCtrlMinRateUp = _Xldv20AdcCtrlMinRateUp_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 2, 5),
    _Xldv20AdcCtrlMinRateUp_Type()
)
xldv20AdcCtrlMinRateUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20AdcCtrlMinRateUp.setStatus("mandatory")
_Xldv20AdcCtrlMaxRateDn_Type = Xldv20AdslDataRateDown
_Xldv20AdcCtrlMaxRateDn_Object = MibScalar
xldv20AdcCtrlMaxRateDn = _Xldv20AdcCtrlMaxRateDn_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 2, 6),
    _Xldv20AdcCtrlMaxRateDn_Type()
)
xldv20AdcCtrlMaxRateDn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20AdcCtrlMaxRateDn.setStatus("mandatory")
_Xldv20AdcCtrlMaxRateUp_Type = Xldv20AdslDataRateUp
_Xldv20AdcCtrlMaxRateUp_Object = MibScalar
xldv20AdcCtrlMaxRateUp = _Xldv20AdcCtrlMaxRateUp_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 2, 7),
    _Xldv20AdcCtrlMaxRateUp_Type()
)
xldv20AdcCtrlMaxRateUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20AdcCtrlMaxRateUp.setStatus("mandatory")


class _Xldv20AdcCtrlMarginDn_Type(Integer32):
    """Custom type xldv20AdcCtrlMarginDn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Xldv20AdcCtrlMarginDn_Type.__name__ = "Integer32"
_Xldv20AdcCtrlMarginDn_Object = MibScalar
xldv20AdcCtrlMarginDn = _Xldv20AdcCtrlMarginDn_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 2, 8),
    _Xldv20AdcCtrlMarginDn_Type()
)
xldv20AdcCtrlMarginDn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20AdcCtrlMarginDn.setStatus("mandatory")


class _Xldv20AdcCtrlMarginUp_Type(Integer32):
    """Custom type xldv20AdcCtrlMarginUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Xldv20AdcCtrlMarginUp_Type.__name__ = "Integer32"
_Xldv20AdcCtrlMarginUp_Object = MibScalar
xldv20AdcCtrlMarginUp = _Xldv20AdcCtrlMarginUp_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 2, 9),
    _Xldv20AdcCtrlMarginUp_Type()
)
xldv20AdcCtrlMarginUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20AdcCtrlMarginUp.setStatus("mandatory")
_Xldv20AdcCtrlLatencyDn_Type = Xldv20Latency
_Xldv20AdcCtrlLatencyDn_Object = MibScalar
xldv20AdcCtrlLatencyDn = _Xldv20AdcCtrlLatencyDn_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 2, 10),
    _Xldv20AdcCtrlLatencyDn_Type()
)
xldv20AdcCtrlLatencyDn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20AdcCtrlLatencyDn.setStatus("mandatory")
_Xldv20AdcCtrlLatencyUp_Type = Xldv20Latency
_Xldv20AdcCtrlLatencyUp_Object = MibScalar
xldv20AdcCtrlLatencyUp = _Xldv20AdcCtrlLatencyUp_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 2, 11),
    _Xldv20AdcCtrlLatencyUp_Type()
)
xldv20AdcCtrlLatencyUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20AdcCtrlLatencyUp.setStatus("mandatory")
_Xldv20AdcCtrlMinMarginDn_Type = Xldv20AdslMinMargin
_Xldv20AdcCtrlMinMarginDn_Object = MibScalar
xldv20AdcCtrlMinMarginDn = _Xldv20AdcCtrlMinMarginDn_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 2, 12),
    _Xldv20AdcCtrlMinMarginDn_Type()
)
xldv20AdcCtrlMinMarginDn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20AdcCtrlMinMarginDn.setStatus("mandatory")
_Xldv20AdcCtrlMinMarginUp_Type = Xldv20AdslMinMargin
_Xldv20AdcCtrlMinMarginUp_Object = MibScalar
xldv20AdcCtrlMinMarginUp = _Xldv20AdcCtrlMinMarginUp_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 2, 13),
    _Xldv20AdcCtrlMinMarginUp_Type()
)
xldv20AdcCtrlMinMarginUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20AdcCtrlMinMarginUp.setStatus("mandatory")
_Xldv20AdcCtrlControlReqResult_Type = Xldv20ControlReq
_Xldv20AdcCtrlControlReqResult_Object = MibScalar
xldv20AdcCtrlControlReqResult = _Xldv20AdcCtrlControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 2, 14),
    _Xldv20AdcCtrlControlReqResult_Type()
)
xldv20AdcCtrlControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AdcCtrlControlReqResult.setStatus("mandatory")
_Xldv20AdcCtrlXdslServiceType_Type = Xldv20XdslServiceType
_Xldv20AdcCtrlXdslServiceType_Object = MibScalar
xldv20AdcCtrlXdslServiceType = _Xldv20AdcCtrlXdslServiceType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 2, 15),
    _Xldv20AdcCtrlXdslServiceType_Type()
)
xldv20AdcCtrlXdslServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20AdcCtrlXdslServiceType.setStatus("mandatory")
_Xldv20AdcCtrlControlTimeStamp_Type = TimeTicks
_Xldv20AdcCtrlControlTimeStamp_Object = MibScalar
xldv20AdcCtrlControlTimeStamp = _Xldv20AdcCtrlControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 2, 16),
    _Xldv20AdcCtrlControlTimeStamp_Type()
)
xldv20AdcCtrlControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AdcCtrlControlTimeStamp.setStatus("mandatory")
_Xldv20AdcCtrlTrainingMode_Type = Xldv20AdcTrainingMode
_Xldv20AdcCtrlTrainingMode_Object = MibScalar
xldv20AdcCtrlTrainingMode = _Xldv20AdcCtrlTrainingMode_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 2, 17),
    _Xldv20AdcCtrlTrainingMode_Type()
)
xldv20AdcCtrlTrainingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20AdcCtrlTrainingMode.setStatus("mandatory")
_Xldv20VdcControl_ObjectIdentity = ObjectIdentity
xldv20VdcControl = _Xldv20VdcControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 3)
)
_Xldv20VdcCtrlControlReq_Type = Xldv20ControlReq
_Xldv20VdcCtrlControlReq_Object = MibScalar
xldv20VdcCtrlControlReq = _Xldv20VdcCtrlControlReq_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 3, 1),
    _Xldv20VdcCtrlControlReq_Type()
)
xldv20VdcCtrlControlReq.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20VdcCtrlControlReq.setStatus("mandatory")
_Xldv20VdcCtrlControlStatus_Type = Xldv20ControlStatus
_Xldv20VdcCtrlControlStatus_Object = MibScalar
xldv20VdcCtrlControlStatus = _Xldv20VdcCtrlControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 3, 2),
    _Xldv20VdcCtrlControlStatus_Type()
)
xldv20VdcCtrlControlStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20VdcCtrlControlStatus.setStatus("mandatory")
_Xldv20VdcCtrlIfIndex_Type = Unsigned16
_Xldv20VdcCtrlIfIndex_Object = MibScalar
xldv20VdcCtrlIfIndex = _Xldv20VdcCtrlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 3, 3),
    _Xldv20VdcCtrlIfIndex_Type()
)
xldv20VdcCtrlIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20VdcCtrlIfIndex.setStatus("mandatory")
_Xldv20VdcCtrlMinRateDn_Type = Xldv20VdcRateDn
_Xldv20VdcCtrlMinRateDn_Object = MibScalar
xldv20VdcCtrlMinRateDn = _Xldv20VdcCtrlMinRateDn_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 3, 4),
    _Xldv20VdcCtrlMinRateDn_Type()
)
xldv20VdcCtrlMinRateDn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20VdcCtrlMinRateDn.setStatus("mandatory")
_Xldv20VdcCtrlMinRateUp_Type = Xldv20VdcRateUp
_Xldv20VdcCtrlMinRateUp_Object = MibScalar
xldv20VdcCtrlMinRateUp = _Xldv20VdcCtrlMinRateUp_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 3, 5),
    _Xldv20VdcCtrlMinRateUp_Type()
)
xldv20VdcCtrlMinRateUp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20VdcCtrlMinRateUp.setStatus("mandatory")
_Xldv20VdcCtrlMaxRateDn_Type = Xldv20VdcRateDn
_Xldv20VdcCtrlMaxRateDn_Object = MibScalar
xldv20VdcCtrlMaxRateDn = _Xldv20VdcCtrlMaxRateDn_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 3, 6),
    _Xldv20VdcCtrlMaxRateDn_Type()
)
xldv20VdcCtrlMaxRateDn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20VdcCtrlMaxRateDn.setStatus("mandatory")
_Xldv20VdcCtrlMaxRateUp_Type = Xldv20VdcRateUp
_Xldv20VdcCtrlMaxRateUp_Object = MibScalar
xldv20VdcCtrlMaxRateUp = _Xldv20VdcCtrlMaxRateUp_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 3, 7),
    _Xldv20VdcCtrlMaxRateUp_Type()
)
xldv20VdcCtrlMaxRateUp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20VdcCtrlMaxRateUp.setStatus("mandatory")
_Xldv20VdcCtrlLatencyDn_Type = Xldv20VdcLatencyDn
_Xldv20VdcCtrlLatencyDn_Object = MibScalar
xldv20VdcCtrlLatencyDn = _Xldv20VdcCtrlLatencyDn_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 3, 8),
    _Xldv20VdcCtrlLatencyDn_Type()
)
xldv20VdcCtrlLatencyDn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20VdcCtrlLatencyDn.setStatus("mandatory")
_Xldv20VdcCtrlLatencyUp_Type = Xldv20VdcLatencyUp
_Xldv20VdcCtrlLatencyUp_Object = MibScalar
xldv20VdcCtrlLatencyUp = _Xldv20VdcCtrlLatencyUp_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 3, 9),
    _Xldv20VdcCtrlLatencyUp_Type()
)
xldv20VdcCtrlLatencyUp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20VdcCtrlLatencyUp.setStatus("mandatory")
_Xldv20VdcCtrlPowerBoost_Type = Xldv20VdcPowerBoostAdaptationType
_Xldv20VdcCtrlPowerBoost_Object = MibScalar
xldv20VdcCtrlPowerBoost = _Xldv20VdcCtrlPowerBoost_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 3, 10),
    _Xldv20VdcCtrlPowerBoost_Type()
)
xldv20VdcCtrlPowerBoost.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20VdcCtrlPowerBoost.setStatus("mandatory")
_Xldv20VdcCtrlWarmStart_Type = Xldv20OperState
_Xldv20VdcCtrlWarmStart_Object = MibScalar
xldv20VdcCtrlWarmStart = _Xldv20VdcCtrlWarmStart_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 3, 11),
    _Xldv20VdcCtrlWarmStart_Type()
)
xldv20VdcCtrlWarmStart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20VdcCtrlWarmStart.setStatus("mandatory")
_Xldv20VdcCtrlVdslMode_Type = Xldv20VdcVdslMode
_Xldv20VdcCtrlVdslMode_Object = MibScalar
xldv20VdcCtrlVdslMode = _Xldv20VdcCtrlVdslMode_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 3, 12),
    _Xldv20VdcCtrlVdslMode_Type()
)
xldv20VdcCtrlVdslMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20VdcCtrlVdslMode.setStatus("mandatory")
_Xldv20VdcCtrlSleepMode_Type = Xldv20OperState
_Xldv20VdcCtrlSleepMode_Object = MibScalar
xldv20VdcCtrlSleepMode = _Xldv20VdcCtrlSleepMode_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 3, 13),
    _Xldv20VdcCtrlSleepMode_Type()
)
xldv20VdcCtrlSleepMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20VdcCtrlSleepMode.setStatus("mandatory")
_Xldv20VdcCtrlPsdMask_Type = Xldv20VdcPsdMask
_Xldv20VdcCtrlPsdMask_Object = MibScalar
xldv20VdcCtrlPsdMask = _Xldv20VdcCtrlPsdMask_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 3, 14),
    _Xldv20VdcCtrlPsdMask_Type()
)
xldv20VdcCtrlPsdMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20VdcCtrlPsdMask.setStatus("mandatory")
_Xldv20VdcCtrlPowerAdaptation_Type = Xldv20VdcPowerBoostAdaptationType
_Xldv20VdcCtrlPowerAdaptation_Object = MibScalar
xldv20VdcCtrlPowerAdaptation = _Xldv20VdcCtrlPowerAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 3, 15),
    _Xldv20VdcCtrlPowerAdaptation_Type()
)
xldv20VdcCtrlPowerAdaptation.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20VdcCtrlPowerAdaptation.setStatus("mandatory")
_Xldv20VdcCtrlControlReqResult_Type = Xldv20ControlReq
_Xldv20VdcCtrlControlReqResult_Object = MibScalar
xldv20VdcCtrlControlReqResult = _Xldv20VdcCtrlControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 3, 16),
    _Xldv20VdcCtrlControlReqResult_Type()
)
xldv20VdcCtrlControlReqResult.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20VdcCtrlControlReqResult.setStatus("mandatory")
_Xldv20VdcCtrlControlTimeStamp_Type = TimeTicks
_Xldv20VdcCtrlControlTimeStamp_Object = MibScalar
xldv20VdcCtrlControlTimeStamp = _Xldv20VdcCtrlControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 3, 17),
    _Xldv20VdcCtrlControlTimeStamp_Type()
)
xldv20VdcCtrlControlTimeStamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20VdcCtrlControlTimeStamp.setStatus("mandatory")
_Xldv20AdcPPTPTable_Object = MibTable
xldv20AdcPPTPTable = _Xldv20AdcPPTPTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 4)
)
if mibBuilder.loadTexts:
    xldv20AdcPPTPTable.setStatus("mandatory")
_Xldv20AdcPPTPEntry_Object = MibTableRow
xldv20AdcPPTPEntry = _Xldv20AdcPPTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 4, 1)
)
xldv20AdcPPTPEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20IfIndex"),
)
if mibBuilder.loadTexts:
    xldv20AdcPPTPEntry.setStatus("mandatory")
_Xldv20AdcMinRateDnCfg_Type = Xldv20AdslDataRateDown
_Xldv20AdcMinRateDnCfg_Object = MibTableColumn
xldv20AdcMinRateDnCfg = _Xldv20AdcMinRateDnCfg_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 4, 1, 1),
    _Xldv20AdcMinRateDnCfg_Type()
)
xldv20AdcMinRateDnCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AdcMinRateDnCfg.setStatus("mandatory")
_Xldv20AdcMinRateUpCfg_Type = Xldv20AdslDataRateUp
_Xldv20AdcMinRateUpCfg_Object = MibTableColumn
xldv20AdcMinRateUpCfg = _Xldv20AdcMinRateUpCfg_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 4, 1, 2),
    _Xldv20AdcMinRateUpCfg_Type()
)
xldv20AdcMinRateUpCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AdcMinRateUpCfg.setStatus("mandatory")
_Xldv20AdcMaxRateDnCfg_Type = Xldv20AdslDataRateDown
_Xldv20AdcMaxRateDnCfg_Object = MibTableColumn
xldv20AdcMaxRateDnCfg = _Xldv20AdcMaxRateDnCfg_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 4, 1, 3),
    _Xldv20AdcMaxRateDnCfg_Type()
)
xldv20AdcMaxRateDnCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AdcMaxRateDnCfg.setStatus("mandatory")
_Xldv20AdcMaxRateUpCfg_Type = Xldv20AdslDataRateUp
_Xldv20AdcMaxRateUpCfg_Object = MibTableColumn
xldv20AdcMaxRateUpCfg = _Xldv20AdcMaxRateUpCfg_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 4, 1, 4),
    _Xldv20AdcMaxRateUpCfg_Type()
)
xldv20AdcMaxRateUpCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AdcMaxRateUpCfg.setStatus("mandatory")


class _Xldv20AdcMarginDnCfg_Type(Integer32):
    """Custom type xldv20AdcMarginDnCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Xldv20AdcMarginDnCfg_Type.__name__ = "Integer32"
_Xldv20AdcMarginDnCfg_Object = MibTableColumn
xldv20AdcMarginDnCfg = _Xldv20AdcMarginDnCfg_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 4, 1, 5),
    _Xldv20AdcMarginDnCfg_Type()
)
xldv20AdcMarginDnCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AdcMarginDnCfg.setStatus("mandatory")


class _Xldv20AdcMarginUpCfg_Type(Integer32):
    """Custom type xldv20AdcMarginUpCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Xldv20AdcMarginUpCfg_Type.__name__ = "Integer32"
_Xldv20AdcMarginUpCfg_Object = MibTableColumn
xldv20AdcMarginUpCfg = _Xldv20AdcMarginUpCfg_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 4, 1, 6),
    _Xldv20AdcMarginUpCfg_Type()
)
xldv20AdcMarginUpCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AdcMarginUpCfg.setStatus("mandatory")
_Xldv20AdcMinMarginDnCfg_Type = Xldv20AdslMinMargin
_Xldv20AdcMinMarginDnCfg_Object = MibTableColumn
xldv20AdcMinMarginDnCfg = _Xldv20AdcMinMarginDnCfg_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 4, 1, 7),
    _Xldv20AdcMinMarginDnCfg_Type()
)
xldv20AdcMinMarginDnCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AdcMinMarginDnCfg.setStatus("mandatory")
_Xldv20AdcMinMarginUpCfg_Type = Xldv20AdslMinMargin
_Xldv20AdcMinMarginUpCfg_Object = MibTableColumn
xldv20AdcMinMarginUpCfg = _Xldv20AdcMinMarginUpCfg_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 4, 1, 8),
    _Xldv20AdcMinMarginUpCfg_Type()
)
xldv20AdcMinMarginUpCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AdcMinMarginUpCfg.setStatus("mandatory")
_Xldv20AdcLatencyDnCfg_Type = Xldv20Latency
_Xldv20AdcLatencyDnCfg_Object = MibTableColumn
xldv20AdcLatencyDnCfg = _Xldv20AdcLatencyDnCfg_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 4, 1, 10),
    _Xldv20AdcLatencyDnCfg_Type()
)
xldv20AdcLatencyDnCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AdcLatencyDnCfg.setStatus("mandatory")
_Xldv20AdcLatencyUpCfg_Type = Xldv20Latency
_Xldv20AdcLatencyUpCfg_Object = MibTableColumn
xldv20AdcLatencyUpCfg = _Xldv20AdcLatencyUpCfg_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 4, 1, 11),
    _Xldv20AdcLatencyUpCfg_Type()
)
xldv20AdcLatencyUpCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AdcLatencyUpCfg.setStatus("mandatory")
_Xldv20AdcRateDn_Type = Xldv20AdslDataRateDownCurrent
_Xldv20AdcRateDn_Object = MibTableColumn
xldv20AdcRateDn = _Xldv20AdcRateDn_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 4, 1, 12),
    _Xldv20AdcRateDn_Type()
)
xldv20AdcRateDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AdcRateDn.setStatus("mandatory")
_Xldv20AdcRateUp_Type = Xldv20AdslDataRateUpCurrent
_Xldv20AdcRateUp_Object = MibTableColumn
xldv20AdcRateUp = _Xldv20AdcRateUp_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 4, 1, 13),
    _Xldv20AdcRateUp_Type()
)
xldv20AdcRateUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AdcRateUp.setStatus("mandatory")
_Xldv20AdcMarginDn_Type = Xldv20AdslMargin
_Xldv20AdcMarginDn_Object = MibTableColumn
xldv20AdcMarginDn = _Xldv20AdcMarginDn_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 4, 1, 14),
    _Xldv20AdcMarginDn_Type()
)
xldv20AdcMarginDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AdcMarginDn.setStatus("mandatory")
_Xldv20AdcMarginUp_Type = Xldv20AdslMargin
_Xldv20AdcMarginUp_Object = MibTableColumn
xldv20AdcMarginUp = _Xldv20AdcMarginUp_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 4, 1, 15),
    _Xldv20AdcMarginUp_Type()
)
xldv20AdcMarginUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AdcMarginUp.setStatus("mandatory")
_Xldv20AdcAttenuationDn_Type = Xldv20AdslAttenuation
_Xldv20AdcAttenuationDn_Object = MibTableColumn
xldv20AdcAttenuationDn = _Xldv20AdcAttenuationDn_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 4, 1, 16),
    _Xldv20AdcAttenuationDn_Type()
)
xldv20AdcAttenuationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AdcAttenuationDn.setStatus("mandatory")
_Xldv20AdcAttenuationUp_Type = Xldv20AdslAttenuation
_Xldv20AdcAttenuationUp_Object = MibTableColumn
xldv20AdcAttenuationUp = _Xldv20AdcAttenuationUp_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 4, 1, 17),
    _Xldv20AdcAttenuationUp_Type()
)
xldv20AdcAttenuationUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AdcAttenuationUp.setStatus("mandatory")
_Xldv20AdcLinkState_Type = Xldv20LinkState
_Xldv20AdcLinkState_Object = MibTableColumn
xldv20AdcLinkState = _Xldv20AdcLinkState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 4, 1, 18),
    _Xldv20AdcLinkState_Type()
)
xldv20AdcLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AdcLinkState.setStatus("mandatory")
_Xldv20AdcAISOnLOS_Type = Xldv20OperState
_Xldv20AdcAISOnLOS_Object = MibTableColumn
xldv20AdcAISOnLOS = _Xldv20AdcAISOnLOS_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 4, 1, 19),
    _Xldv20AdcAISOnLOS_Type()
)
xldv20AdcAISOnLOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20AdcAISOnLOS.setStatus("mandatory")
_Xldv20AdcAISOnACT_Type = Xldv20OperState
_Xldv20AdcAISOnACT_Object = MibTableColumn
xldv20AdcAISOnACT = _Xldv20AdcAISOnACT_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 4, 1, 20),
    _Xldv20AdcAISOnACT_Type()
)
xldv20AdcAISOnACT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20AdcAISOnACT.setStatus("mandatory")


class _Xldv20AdcGuaranteedBandwidthUsage_Type(Integer32):
    """Custom type xldv20AdcGuaranteedBandwidthUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Xldv20AdcGuaranteedBandwidthUsage_Type.__name__ = "Integer32"
_Xldv20AdcGuaranteedBandwidthUsage_Object = MibTableColumn
xldv20AdcGuaranteedBandwidthUsage = _Xldv20AdcGuaranteedBandwidthUsage_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 4, 1, 21),
    _Xldv20AdcGuaranteedBandwidthUsage_Type()
)
xldv20AdcGuaranteedBandwidthUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AdcGuaranteedBandwidthUsage.setStatus("mandatory")
_Xldv20AdcXdslServiceTypeCfg_Type = Xldv20XdslServiceType
_Xldv20AdcXdslServiceTypeCfg_Object = MibTableColumn
xldv20AdcXdslServiceTypeCfg = _Xldv20AdcXdslServiceTypeCfg_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 4, 1, 22),
    _Xldv20AdcXdslServiceTypeCfg_Type()
)
xldv20AdcXdslServiceTypeCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AdcXdslServiceTypeCfg.setStatus("mandatory")
_Xldv20AdcInitStatus_Type = Xldv20XdslInitStatus
_Xldv20AdcInitStatus_Object = MibTableColumn
xldv20AdcInitStatus = _Xldv20AdcInitStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 4, 1, 23),
    _Xldv20AdcInitStatus_Type()
)
xldv20AdcInitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AdcInitStatus.setStatus("mandatory")
_Xldv20AdcTransceiverOutputPower_Type = Xldv20AdslOutputPower
_Xldv20AdcTransceiverOutputPower_Object = MibTableColumn
xldv20AdcTransceiverOutputPower = _Xldv20AdcTransceiverOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 4, 1, 24),
    _Xldv20AdcTransceiverOutputPower_Type()
)
xldv20AdcTransceiverOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AdcTransceiverOutputPower.setStatus("mandatory")


class _Xldv20AdcFirstUsedSubCarrierUpstream_Type(Integer32):
    """Custom type xldv20AdcFirstUsedSubCarrierUpstream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_Xldv20AdcFirstUsedSubCarrierUpstream_Type.__name__ = "Integer32"
_Xldv20AdcFirstUsedSubCarrierUpstream_Object = MibTableColumn
xldv20AdcFirstUsedSubCarrierUpstream = _Xldv20AdcFirstUsedSubCarrierUpstream_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 4, 1, 25),
    _Xldv20AdcFirstUsedSubCarrierUpstream_Type()
)
xldv20AdcFirstUsedSubCarrierUpstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AdcFirstUsedSubCarrierUpstream.setStatus("mandatory")


class _Xldv20AdcFirstUsedSubCarrierDownstream_Type(Integer32):
    """Custom type xldv20AdcFirstUsedSubCarrierDownstream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Xldv20AdcFirstUsedSubCarrierDownstream_Type.__name__ = "Integer32"
_Xldv20AdcFirstUsedSubCarrierDownstream_Object = MibTableColumn
xldv20AdcFirstUsedSubCarrierDownstream = _Xldv20AdcFirstUsedSubCarrierDownstream_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 4, 1, 26),
    _Xldv20AdcFirstUsedSubCarrierDownstream_Type()
)
xldv20AdcFirstUsedSubCarrierDownstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AdcFirstUsedSubCarrierDownstream.setStatus("mandatory")


class _Xldv20AdcLastUsedSubCarrierUpstream_Type(Integer32):
    """Custom type xldv20AdcLastUsedSubCarrierUpstream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_Xldv20AdcLastUsedSubCarrierUpstream_Type.__name__ = "Integer32"
_Xldv20AdcLastUsedSubCarrierUpstream_Object = MibTableColumn
xldv20AdcLastUsedSubCarrierUpstream = _Xldv20AdcLastUsedSubCarrierUpstream_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 4, 1, 27),
    _Xldv20AdcLastUsedSubCarrierUpstream_Type()
)
xldv20AdcLastUsedSubCarrierUpstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AdcLastUsedSubCarrierUpstream.setStatus("mandatory")


class _Xldv20AdcLastUsedSubCarrierDownstream_Type(Integer32):
    """Custom type xldv20AdcLastUsedSubCarrierDownstream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Xldv20AdcLastUsedSubCarrierDownstream_Type.__name__ = "Integer32"
_Xldv20AdcLastUsedSubCarrierDownstream_Object = MibTableColumn
xldv20AdcLastUsedSubCarrierDownstream = _Xldv20AdcLastUsedSubCarrierDownstream_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 4, 1, 28),
    _Xldv20AdcLastUsedSubCarrierDownstream_Type()
)
xldv20AdcLastUsedSubCarrierDownstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AdcLastUsedSubCarrierDownstream.setStatus("mandatory")
_Xldv20AdcXdslServiceType_Type = Xldv20XdslServiceTypeCurrent
_Xldv20AdcXdslServiceType_Object = MibTableColumn
xldv20AdcXdslServiceType = _Xldv20AdcXdslServiceType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 4, 1, 29),
    _Xldv20AdcXdslServiceType_Type()
)
xldv20AdcXdslServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AdcXdslServiceType.setStatus("mandatory")
_Xldv20VdcPPTPTable_Object = MibTable
xldv20VdcPPTPTable = _Xldv20VdcPPTPTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 5)
)
if mibBuilder.loadTexts:
    xldv20VdcPPTPTable.setStatus("mandatory")
_Xldv20VdcPPTPEntry_Object = MibTableRow
xldv20VdcPPTPEntry = _Xldv20VdcPPTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 5, 1)
)
xldv20VdcPPTPEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20IfIndex"),
)
if mibBuilder.loadTexts:
    xldv20VdcPPTPEntry.setStatus("mandatory")
_Xldv20VdcMinRateDnCfg_Type = Xldv20VdcRateDn
_Xldv20VdcMinRateDnCfg_Object = MibTableColumn
xldv20VdcMinRateDnCfg = _Xldv20VdcMinRateDnCfg_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 5, 1, 1),
    _Xldv20VdcMinRateDnCfg_Type()
)
xldv20VdcMinRateDnCfg.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20VdcMinRateDnCfg.setStatus("mandatory")
_Xldv20VdcMinRateUpCfg_Type = Xldv20VdcRateUp
_Xldv20VdcMinRateUpCfg_Object = MibTableColumn
xldv20VdcMinRateUpCfg = _Xldv20VdcMinRateUpCfg_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 5, 1, 2),
    _Xldv20VdcMinRateUpCfg_Type()
)
xldv20VdcMinRateUpCfg.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20VdcMinRateUpCfg.setStatus("mandatory")
_Xldv20VdcMaxRateDnCfg_Type = Xldv20VdcRateDn
_Xldv20VdcMaxRateDnCfg_Object = MibTableColumn
xldv20VdcMaxRateDnCfg = _Xldv20VdcMaxRateDnCfg_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 5, 1, 3),
    _Xldv20VdcMaxRateDnCfg_Type()
)
xldv20VdcMaxRateDnCfg.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20VdcMaxRateDnCfg.setStatus("mandatory")
_Xldv20VdcMaxRateUpCfg_Type = Xldv20VdcRateUp
_Xldv20VdcMaxRateUpCfg_Object = MibTableColumn
xldv20VdcMaxRateUpCfg = _Xldv20VdcMaxRateUpCfg_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 5, 1, 4),
    _Xldv20VdcMaxRateUpCfg_Type()
)
xldv20VdcMaxRateUpCfg.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20VdcMaxRateUpCfg.setStatus("mandatory")
_Xldv20VdcLatencyDnCfg_Type = Xldv20VdcLatencyDn
_Xldv20VdcLatencyDnCfg_Object = MibTableColumn
xldv20VdcLatencyDnCfg = _Xldv20VdcLatencyDnCfg_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 5, 1, 5),
    _Xldv20VdcLatencyDnCfg_Type()
)
xldv20VdcLatencyDnCfg.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20VdcLatencyDnCfg.setStatus("mandatory")
_Xldv20VdcLatencyUpCfg_Type = Xldv20VdcLatencyUp
_Xldv20VdcLatencyUpCfg_Object = MibTableColumn
xldv20VdcLatencyUpCfg = _Xldv20VdcLatencyUpCfg_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 5, 1, 6),
    _Xldv20VdcLatencyUpCfg_Type()
)
xldv20VdcLatencyUpCfg.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20VdcLatencyUpCfg.setStatus("mandatory")
_Xldv20VdcPowerBoostCfg_Type = Xldv20VdcPowerBoostAdaptationType
_Xldv20VdcPowerBoostCfg_Object = MibTableColumn
xldv20VdcPowerBoostCfg = _Xldv20VdcPowerBoostCfg_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 5, 1, 7),
    _Xldv20VdcPowerBoostCfg_Type()
)
xldv20VdcPowerBoostCfg.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20VdcPowerBoostCfg.setStatus("mandatory")
_Xldv20VdcWarmStartCfg_Type = Xldv20OperState
_Xldv20VdcWarmStartCfg_Object = MibTableColumn
xldv20VdcWarmStartCfg = _Xldv20VdcWarmStartCfg_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 5, 1, 8),
    _Xldv20VdcWarmStartCfg_Type()
)
xldv20VdcWarmStartCfg.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20VdcWarmStartCfg.setStatus("mandatory")
_Xldv20VdcVdslModeCfg_Type = Xldv20VdcVdslMode
_Xldv20VdcVdslModeCfg_Object = MibTableColumn
xldv20VdcVdslModeCfg = _Xldv20VdcVdslModeCfg_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 5, 1, 9),
    _Xldv20VdcVdslModeCfg_Type()
)
xldv20VdcVdslModeCfg.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20VdcVdslModeCfg.setStatus("mandatory")
_Xldv20VdcSleepModeCfg_Type = Xldv20OperState
_Xldv20VdcSleepModeCfg_Object = MibTableColumn
xldv20VdcSleepModeCfg = _Xldv20VdcSleepModeCfg_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 5, 1, 10),
    _Xldv20VdcSleepModeCfg_Type()
)
xldv20VdcSleepModeCfg.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20VdcSleepModeCfg.setStatus("mandatory")
_Xldv20VdcPsdMaskCfg_Type = Xldv20VdcPsdMask
_Xldv20VdcPsdMaskCfg_Object = MibTableColumn
xldv20VdcPsdMaskCfg = _Xldv20VdcPsdMaskCfg_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 5, 1, 11),
    _Xldv20VdcPsdMaskCfg_Type()
)
xldv20VdcPsdMaskCfg.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20VdcPsdMaskCfg.setStatus("mandatory")
_Xldv20VdcPowerAdaptationCfg_Type = Xldv20VdcPowerBoostAdaptationType
_Xldv20VdcPowerAdaptationCfg_Object = MibTableColumn
xldv20VdcPowerAdaptationCfg = _Xldv20VdcPowerAdaptationCfg_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 5, 1, 12),
    _Xldv20VdcPowerAdaptationCfg_Type()
)
xldv20VdcPowerAdaptationCfg.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20VdcPowerAdaptationCfg.setStatus("mandatory")
_Xldv20VdcRateDn_Type = Xldv20VdcRateDn
_Xldv20VdcRateDn_Object = MibTableColumn
xldv20VdcRateDn = _Xldv20VdcRateDn_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 5, 1, 13),
    _Xldv20VdcRateDn_Type()
)
xldv20VdcRateDn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20VdcRateDn.setStatus("mandatory")
_Xldv20VdcRateUp_Type = Xldv20VdcRateUp
_Xldv20VdcRateUp_Object = MibTableColumn
xldv20VdcRateUp = _Xldv20VdcRateUp_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 5, 1, 14),
    _Xldv20VdcRateUp_Type()
)
xldv20VdcRateUp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20VdcRateUp.setStatus("mandatory")
_Xldv20VdcMarginDn_Type = Integer32
_Xldv20VdcMarginDn_Object = MibTableColumn
xldv20VdcMarginDn = _Xldv20VdcMarginDn_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 5, 1, 15),
    _Xldv20VdcMarginDn_Type()
)
xldv20VdcMarginDn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20VdcMarginDn.setStatus("mandatory")
_Xldv20VdcMarginUp_Type = Integer32
_Xldv20VdcMarginUp_Object = MibTableColumn
xldv20VdcMarginUp = _Xldv20VdcMarginUp_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 5, 1, 16),
    _Xldv20VdcMarginUp_Type()
)
xldv20VdcMarginUp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20VdcMarginUp.setStatus("mandatory")
_Xldv20VdcAttenuationDn_Type = Integer32
_Xldv20VdcAttenuationDn_Object = MibTableColumn
xldv20VdcAttenuationDn = _Xldv20VdcAttenuationDn_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 5, 1, 17),
    _Xldv20VdcAttenuationDn_Type()
)
xldv20VdcAttenuationDn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20VdcAttenuationDn.setStatus("mandatory")
_Xldv20VdcAttenuationUp_Type = Integer32
_Xldv20VdcAttenuationUp_Object = MibTableColumn
xldv20VdcAttenuationUp = _Xldv20VdcAttenuationUp_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 5, 1, 18),
    _Xldv20VdcAttenuationUp_Type()
)
xldv20VdcAttenuationUp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20VdcAttenuationUp.setStatus("mandatory")
_Xldv20VdcLinkState_Type = Xldv20LinkState
_Xldv20VdcLinkState_Object = MibTableColumn
xldv20VdcLinkState = _Xldv20VdcLinkState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 5, 1, 19),
    _Xldv20VdcLinkState_Type()
)
xldv20VdcLinkState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20VdcLinkState.setStatus("mandatory")


class _Xldv20VdcGuaranteedBandwidthUsage_Type(Integer32):
    """Custom type xldv20VdcGuaranteedBandwidthUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Xldv20VdcGuaranteedBandwidthUsage_Type.__name__ = "Integer32"
_Xldv20VdcGuaranteedBandwidthUsage_Object = MibTableColumn
xldv20VdcGuaranteedBandwidthUsage = _Xldv20VdcGuaranteedBandwidthUsage_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 5, 1, 20),
    _Xldv20VdcGuaranteedBandwidthUsage_Type()
)
xldv20VdcGuaranteedBandwidthUsage.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20VdcGuaranteedBandwidthUsage.setStatus("mandatory")
_Xldv20IbmPPTPTable_Object = MibTable
xldv20IbmPPTPTable = _Xldv20IbmPPTPTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 6)
)
if mibBuilder.loadTexts:
    xldv20IbmPPTPTable.setStatus("mandatory")
_Xldv20IbmPPTPEntry_Object = MibTableRow
xldv20IbmPPTPEntry = _Xldv20IbmPPTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 6, 1)
)
xldv20IbmPPTPEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20IfIndex"),
)
if mibBuilder.loadTexts:
    xldv20IbmPPTPEntry.setStatus("mandatory")
_Xldv20IbmAISOnLOS_Type = Xldv20OperState
_Xldv20IbmAISOnLOS_Object = MibTableColumn
xldv20IbmAISOnLOS = _Xldv20IbmAISOnLOS_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 6, 1, 1),
    _Xldv20IbmAISOnLOS_Type()
)
xldv20IbmAISOnLOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20IbmAISOnLOS.setStatus("mandatory")
_Xldv20IbmVpAISFiltering_Type = Xldv20OperState
_Xldv20IbmVpAISFiltering_Object = MibTableColumn
xldv20IbmVpAISFiltering = _Xldv20IbmVpAISFiltering_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 6, 1, 2),
    _Xldv20IbmVpAISFiltering_Type()
)
xldv20IbmVpAISFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20IbmVpAISFiltering.setStatus("mandatory")
_Xldv20Ds3NePPTPTable_Object = MibTable
xldv20Ds3NePPTPTable = _Xldv20Ds3NePPTPTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 7)
)
if mibBuilder.loadTexts:
    xldv20Ds3NePPTPTable.setStatus("mandatory")
_Xldv20Ds3NePPTPEntry_Object = MibTableRow
xldv20Ds3NePPTPEntry = _Xldv20Ds3NePPTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 7, 1)
)
xldv20Ds3NePPTPEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20IfIndex"),
)
if mibBuilder.loadTexts:
    xldv20Ds3NePPTPEntry.setStatus("mandatory")
_Xldv20D3nType_Type = Xldv20LineType
_Xldv20D3nType_Object = MibTableColumn
xldv20D3nType = _Xldv20D3nType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 7, 1, 1),
    _Xldv20D3nType_Type()
)
xldv20D3nType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20D3nType.setStatus("mandatory")
_Xldv20D3nCodingType_Type = Xldv20CodingType
_Xldv20D3nCodingType_Object = MibTableColumn
xldv20D3nCodingType = _Xldv20D3nCodingType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 7, 1, 2),
    _Xldv20D3nCodingType_Type()
)
xldv20D3nCodingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20D3nCodingType.setStatus("mandatory")
_Xldv20D3nPayloadScramblingActivate_Type = Xldv20OperState
_Xldv20D3nPayloadScramblingActivate_Object = MibTableColumn
xldv20D3nPayloadScramblingActivate = _Xldv20D3nPayloadScramblingActivate_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 7, 1, 3),
    _Xldv20D3nPayloadScramblingActivate_Type()
)
xldv20D3nPayloadScramblingActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20D3nPayloadScramblingActivate.setStatus("mandatory")
_Xldv20D3nEmptyCellType_Type = Xldv20EmptyCellType
_Xldv20D3nEmptyCellType_Object = MibTableColumn
xldv20D3nEmptyCellType = _Xldv20D3nEmptyCellType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 7, 1, 4),
    _Xldv20D3nEmptyCellType_Type()
)
xldv20D3nEmptyCellType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20D3nEmptyCellType.setStatus("mandatory")


class _Xldv20D3nBandwidthUsage_Type(Integer32):
    """Custom type xldv20D3nBandwidthUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Xldv20D3nBandwidthUsage_Type.__name__ = "Integer32"
_Xldv20D3nBandwidthUsage_Object = MibTableColumn
xldv20D3nBandwidthUsage = _Xldv20D3nBandwidthUsage_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 7, 1, 5),
    _Xldv20D3nBandwidthUsage_Type()
)
xldv20D3nBandwidthUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20D3nBandwidthUsage.setStatus("mandatory")
_Xldv20E3NePPTPTable_Object = MibTable
xldv20E3NePPTPTable = _Xldv20E3NePPTPTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 8)
)
if mibBuilder.loadTexts:
    xldv20E3NePPTPTable.setStatus("mandatory")
_Xldv20E3NePPTPEntry_Object = MibTableRow
xldv20E3NePPTPEntry = _Xldv20E3NePPTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 8, 1)
)
xldv20E3NePPTPEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20IfIndex"),
)
if mibBuilder.loadTexts:
    xldv20E3NePPTPEntry.setStatus("mandatory")
_Xldv20E3nType_Type = Xldv20LineType
_Xldv20E3nType_Object = MibTableColumn
xldv20E3nType = _Xldv20E3nType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 8, 1, 1),
    _Xldv20E3nType_Type()
)
xldv20E3nType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20E3nType.setStatus("mandatory")
_Xldv20E3nCodingType_Type = Xldv20CodingType
_Xldv20E3nCodingType_Object = MibTableColumn
xldv20E3nCodingType = _Xldv20E3nCodingType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 8, 1, 2),
    _Xldv20E3nCodingType_Type()
)
xldv20E3nCodingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20E3nCodingType.setStatus("mandatory")


class _Xldv20E3nTrailTraceSend_Type(OctetString):
    """Custom type xldv20E3nTrailTraceSend based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Xldv20E3nTrailTraceSend_Type.__name__ = "OctetString"
_Xldv20E3nTrailTraceSend_Object = MibTableColumn
xldv20E3nTrailTraceSend = _Xldv20E3nTrailTraceSend_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 8, 1, 3),
    _Xldv20E3nTrailTraceSend_Type()
)
xldv20E3nTrailTraceSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20E3nTrailTraceSend.setStatus("mandatory")
_Xldv20E3nTrailTraceSendDefault_Type = Xldv20OperState
_Xldv20E3nTrailTraceSendDefault_Object = MibTableColumn
xldv20E3nTrailTraceSendDefault = _Xldv20E3nTrailTraceSendDefault_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 8, 1, 4),
    _Xldv20E3nTrailTraceSendDefault_Type()
)
xldv20E3nTrailTraceSendDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20E3nTrailTraceSendDefault.setStatus("mandatory")


class _Xldv20E3nTrailTraceExpect_Type(OctetString):
    """Custom type xldv20E3nTrailTraceExpect based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Xldv20E3nTrailTraceExpect_Type.__name__ = "OctetString"
_Xldv20E3nTrailTraceExpect_Object = MibTableColumn
xldv20E3nTrailTraceExpect = _Xldv20E3nTrailTraceExpect_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 8, 1, 5),
    _Xldv20E3nTrailTraceExpect_Type()
)
xldv20E3nTrailTraceExpect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20E3nTrailTraceExpect.setStatus("mandatory")
_Xldv20E3nTrailTraceTIMDetectionActivate_Type = Xldv20OperState
_Xldv20E3nTrailTraceTIMDetectionActivate_Object = MibTableColumn
xldv20E3nTrailTraceTIMDetectionActivate = _Xldv20E3nTrailTraceTIMDetectionActivate_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 8, 1, 6),
    _Xldv20E3nTrailTraceTIMDetectionActivate_Type()
)
xldv20E3nTrailTraceTIMDetectionActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20E3nTrailTraceTIMDetectionActivate.setStatus("mandatory")


class _Xldv20E3nTrailTraceReceive_Type(OctetString):
    """Custom type xldv20E3nTrailTraceReceive based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Xldv20E3nTrailTraceReceive_Type.__name__ = "OctetString"
_Xldv20E3nTrailTraceReceive_Object = MibTableColumn
xldv20E3nTrailTraceReceive = _Xldv20E3nTrailTraceReceive_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 8, 1, 7),
    _Xldv20E3nTrailTraceReceive_Type()
)
xldv20E3nTrailTraceReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20E3nTrailTraceReceive.setStatus("mandatory")
_Xldv20E3nEmptyCellType_Type = Xldv20EmptyCellType
_Xldv20E3nEmptyCellType_Object = MibTableColumn
xldv20E3nEmptyCellType = _Xldv20E3nEmptyCellType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 8, 1, 8),
    _Xldv20E3nEmptyCellType_Type()
)
xldv20E3nEmptyCellType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20E3nEmptyCellType.setStatus("mandatory")
_Xldv20E3nPayloadType_Type = Xldv20E3nPayloadType
_Xldv20E3nPayloadType_Object = MibTableColumn
xldv20E3nPayloadType = _Xldv20E3nPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 8, 1, 9),
    _Xldv20E3nPayloadType_Type()
)
xldv20E3nPayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20E3nPayloadType.setStatus("mandatory")


class _Xldv20E3nBandwidthUsage_Type(Integer32):
    """Custom type xldv20E3nBandwidthUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Xldv20E3nBandwidthUsage_Type.__name__ = "Integer32"
_Xldv20E3nBandwidthUsage_Object = MibTableColumn
xldv20E3nBandwidthUsage = _Xldv20E3nBandwidthUsage_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 8, 1, 10),
    _Xldv20E3nBandwidthUsage_Type()
)
xldv20E3nBandwidthUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20E3nBandwidthUsage.setStatus("mandatory")
_Xldv20Stm1NePPTPTable_Object = MibTable
xldv20Stm1NePPTPTable = _Xldv20Stm1NePPTPTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 9)
)
if mibBuilder.loadTexts:
    xldv20Stm1NePPTPTable.setStatus("mandatory")
_Xldv20Stm1NePPTPEntry_Object = MibTableRow
xldv20Stm1NePPTPEntry = _Xldv20Stm1NePPTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 9, 1)
)
xldv20Stm1NePPTPEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20IfIndex"),
)
if mibBuilder.loadTexts:
    xldv20Stm1NePPTPEntry.setStatus("mandatory")
_Xldv20S1nLineType_Type = Xldv20LineType
_Xldv20S1nLineType_Object = MibTableColumn
xldv20S1nLineType = _Xldv20S1nLineType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 9, 1, 1),
    _Xldv20S1nLineType_Type()
)
xldv20S1nLineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20S1nLineType.setStatus("mandatory")


class _Xldv20S1nPathTraceSend_Type(OctetString):
    """Custom type xldv20S1nPathTraceSend based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Xldv20S1nPathTraceSend_Type.__name__ = "OctetString"
_Xldv20S1nPathTraceSend_Object = MibTableColumn
xldv20S1nPathTraceSend = _Xldv20S1nPathTraceSend_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 9, 1, 2),
    _Xldv20S1nPathTraceSend_Type()
)
xldv20S1nPathTraceSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20S1nPathTraceSend.setStatus("mandatory")
_Xldv20S1nPathTraceSendDefault_Type = Xldv20OperState
_Xldv20S1nPathTraceSendDefault_Object = MibTableColumn
xldv20S1nPathTraceSendDefault = _Xldv20S1nPathTraceSendDefault_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 9, 1, 3),
    _Xldv20S1nPathTraceSendDefault_Type()
)
xldv20S1nPathTraceSendDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20S1nPathTraceSendDefault.setStatus("mandatory")


class _Xldv20S1nPathTraceExpect_Type(OctetString):
    """Custom type xldv20S1nPathTraceExpect based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Xldv20S1nPathTraceExpect_Type.__name__ = "OctetString"
_Xldv20S1nPathTraceExpect_Object = MibTableColumn
xldv20S1nPathTraceExpect = _Xldv20S1nPathTraceExpect_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 9, 1, 4),
    _Xldv20S1nPathTraceExpect_Type()
)
xldv20S1nPathTraceExpect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20S1nPathTraceExpect.setStatus("mandatory")
_Xldv20S1nPathTraceTIMDetectionActivate_Type = Xldv20OperState
_Xldv20S1nPathTraceTIMDetectionActivate_Object = MibTableColumn
xldv20S1nPathTraceTIMDetectionActivate = _Xldv20S1nPathTraceTIMDetectionActivate_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 9, 1, 5),
    _Xldv20S1nPathTraceTIMDetectionActivate_Type()
)
xldv20S1nPathTraceTIMDetectionActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20S1nPathTraceTIMDetectionActivate.setStatus("mandatory")


class _Xldv20S1nPathTraceReceive_Type(OctetString):
    """Custom type xldv20S1nPathTraceReceive based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Xldv20S1nPathTraceReceive_Type.__name__ = "OctetString"
_Xldv20S1nPathTraceReceive_Object = MibTableColumn
xldv20S1nPathTraceReceive = _Xldv20S1nPathTraceReceive_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 9, 1, 6),
    _Xldv20S1nPathTraceReceive_Type()
)
xldv20S1nPathTraceReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20S1nPathTraceReceive.setStatus("mandatory")
_Xldv20S1nHpEberThreshold_Type = Xldv20S1nS3nEberThreshold
_Xldv20S1nHpEberThreshold_Object = MibTableColumn
xldv20S1nHpEberThreshold = _Xldv20S1nHpEberThreshold_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 9, 1, 7),
    _Xldv20S1nHpEberThreshold_Type()
)
xldv20S1nHpEberThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20S1nHpEberThreshold.setStatus("mandatory")
_Xldv20S1nMsEberThreshold_Type = Xldv20S1nS3nEberThreshold
_Xldv20S1nMsEberThreshold_Object = MibTableColumn
xldv20S1nMsEberThreshold = _Xldv20S1nMsEberThreshold_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 9, 1, 8),
    _Xldv20S1nMsEberThreshold_Type()
)
xldv20S1nMsEberThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20S1nMsEberThreshold.setStatus("mandatory")
_Xldv20S1nRsEberThreshold_Type = Xldv20S1nS3nEberThreshold
_Xldv20S1nRsEberThreshold_Object = MibTableColumn
xldv20S1nRsEberThreshold = _Xldv20S1nRsEberThreshold_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 9, 1, 9),
    _Xldv20S1nRsEberThreshold_Type()
)
xldv20S1nRsEberThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20S1nRsEberThreshold.setStatus("mandatory")
_Xldv20S1nSDThreshold_Type = Xldv20S1nS3nSDThreshold
_Xldv20S1nSDThreshold_Object = MibTableColumn
xldv20S1nSDThreshold = _Xldv20S1nSDThreshold_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 9, 1, 10),
    _Xldv20S1nSDThreshold_Type()
)
xldv20S1nSDThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20S1nSDThreshold.setStatus("mandatory")
_Xldv20S1nRDIAISOnEber_Type = Xldv20OperState
_Xldv20S1nRDIAISOnEber_Object = MibTableColumn
xldv20S1nRDIAISOnEber = _Xldv20S1nRDIAISOnEber_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 9, 1, 11),
    _Xldv20S1nRDIAISOnEber_Type()
)
xldv20S1nRDIAISOnEber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20S1nRDIAISOnEber.setStatus("mandatory")
_Xldv20S1nSignalLabelReceive_Type = Integer32
_Xldv20S1nSignalLabelReceive_Object = MibTableColumn
xldv20S1nSignalLabelReceive = _Xldv20S1nSignalLabelReceive_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 9, 1, 12),
    _Xldv20S1nSignalLabelReceive_Type()
)
xldv20S1nSignalLabelReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20S1nSignalLabelReceive.setStatus("mandatory")
_Xldv20S1nEmptyCellType_Type = Xldv20EmptyCellType
_Xldv20S1nEmptyCellType_Object = MibTableColumn
xldv20S1nEmptyCellType = _Xldv20S1nEmptyCellType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 9, 1, 13),
    _Xldv20S1nEmptyCellType_Type()
)
xldv20S1nEmptyCellType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20S1nEmptyCellType.setStatus("mandatory")


class _Xldv20S1nBandwidthUsage_Type(Integer32):
    """Custom type xldv20S1nBandwidthUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Xldv20S1nBandwidthUsage_Type.__name__ = "Integer32"
_Xldv20S1nBandwidthUsage_Object = MibTableColumn
xldv20S1nBandwidthUsage = _Xldv20S1nBandwidthUsage_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 9, 1, 14),
    _Xldv20S1nBandwidthUsage_Type()
)
xldv20S1nBandwidthUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20S1nBandwidthUsage.setStatus("mandatory")
_Xldv20Sts3NePPTPTable_Object = MibTable
xldv20Sts3NePPTPTable = _Xldv20Sts3NePPTPTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 10)
)
if mibBuilder.loadTexts:
    xldv20Sts3NePPTPTable.setStatus("mandatory")
_Xldv20Sts3NePPTPEntry_Object = MibTableRow
xldv20Sts3NePPTPEntry = _Xldv20Sts3NePPTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 10, 1)
)
xldv20Sts3NePPTPEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20IfIndex"),
)
if mibBuilder.loadTexts:
    xldv20Sts3NePPTPEntry.setStatus("mandatory")
_Xldv20S3nLineType_Type = Xldv20LineType
_Xldv20S3nLineType_Object = MibTableColumn
xldv20S3nLineType = _Xldv20S3nLineType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 10, 1, 1),
    _Xldv20S3nLineType_Type()
)
xldv20S3nLineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20S3nLineType.setStatus("mandatory")


class _Xldv20S3nPathTraceSend_Type(OctetString):
    """Custom type xldv20S3nPathTraceSend based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Xldv20S3nPathTraceSend_Type.__name__ = "OctetString"
_Xldv20S3nPathTraceSend_Object = MibTableColumn
xldv20S3nPathTraceSend = _Xldv20S3nPathTraceSend_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 10, 1, 2),
    _Xldv20S3nPathTraceSend_Type()
)
xldv20S3nPathTraceSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20S3nPathTraceSend.setStatus("mandatory")
_Xldv20S3nPathTraceSendDefault_Type = Xldv20OperState
_Xldv20S3nPathTraceSendDefault_Object = MibTableColumn
xldv20S3nPathTraceSendDefault = _Xldv20S3nPathTraceSendDefault_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 10, 1, 3),
    _Xldv20S3nPathTraceSendDefault_Type()
)
xldv20S3nPathTraceSendDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20S3nPathTraceSendDefault.setStatus("mandatory")


class _Xldv20S3nPathTraceExpect_Type(OctetString):
    """Custom type xldv20S3nPathTraceExpect based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Xldv20S3nPathTraceExpect_Type.__name__ = "OctetString"
_Xldv20S3nPathTraceExpect_Object = MibTableColumn
xldv20S3nPathTraceExpect = _Xldv20S3nPathTraceExpect_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 10, 1, 4),
    _Xldv20S3nPathTraceExpect_Type()
)
xldv20S3nPathTraceExpect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20S3nPathTraceExpect.setStatus("mandatory")
_Xldv20S3nPathTraceTIMDetectionActivate_Type = Xldv20OperState
_Xldv20S3nPathTraceTIMDetectionActivate_Object = MibTableColumn
xldv20S3nPathTraceTIMDetectionActivate = _Xldv20S3nPathTraceTIMDetectionActivate_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 10, 1, 5),
    _Xldv20S3nPathTraceTIMDetectionActivate_Type()
)
xldv20S3nPathTraceTIMDetectionActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20S3nPathTraceTIMDetectionActivate.setStatus("mandatory")


class _Xldv20S3nPathTraceReceive_Type(OctetString):
    """Custom type xldv20S3nPathTraceReceive based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Xldv20S3nPathTraceReceive_Type.__name__ = "OctetString"
_Xldv20S3nPathTraceReceive_Object = MibTableColumn
xldv20S3nPathTraceReceive = _Xldv20S3nPathTraceReceive_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 10, 1, 6),
    _Xldv20S3nPathTraceReceive_Type()
)
xldv20S3nPathTraceReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20S3nPathTraceReceive.setStatus("mandatory")
_Xldv20S3nPathTraceSync_Type = Xldv20OperState
_Xldv20S3nPathTraceSync_Object = MibTableColumn
xldv20S3nPathTraceSync = _Xldv20S3nPathTraceSync_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 10, 1, 7),
    _Xldv20S3nPathTraceSync_Type()
)
xldv20S3nPathTraceSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20S3nPathTraceSync.setStatus("mandatory")
_Xldv20S3nPathTraceSendCRCActivate_Type = Xldv20OperState
_Xldv20S3nPathTraceSendCRCActivate_Object = MibTableColumn
xldv20S3nPathTraceSendCRCActivate = _Xldv20S3nPathTraceSendCRCActivate_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 10, 1, 8),
    _Xldv20S3nPathTraceSendCRCActivate_Type()
)
xldv20S3nPathTraceSendCRCActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20S3nPathTraceSendCRCActivate.setStatus("mandatory")
_Xldv20S3nPathTraceReceiveCRCActivate_Type = Xldv20OperState
_Xldv20S3nPathTraceReceiveCRCActivate_Object = MibTableColumn
xldv20S3nPathTraceReceiveCRCActivate = _Xldv20S3nPathTraceReceiveCRCActivate_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 10, 1, 9),
    _Xldv20S3nPathTraceReceiveCRCActivate_Type()
)
xldv20S3nPathTraceReceiveCRCActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20S3nPathTraceReceiveCRCActivate.setStatus("mandatory")
_Xldv20S3nHpEberThreshold_Type = Xldv20S1nS3nEberThreshold
_Xldv20S3nHpEberThreshold_Object = MibTableColumn
xldv20S3nHpEberThreshold = _Xldv20S3nHpEberThreshold_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 10, 1, 10),
    _Xldv20S3nHpEberThreshold_Type()
)
xldv20S3nHpEberThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20S3nHpEberThreshold.setStatus("mandatory")
_Xldv20S3nMsEberThreshold_Type = Xldv20S1nS3nEberThreshold
_Xldv20S3nMsEberThreshold_Object = MibTableColumn
xldv20S3nMsEberThreshold = _Xldv20S3nMsEberThreshold_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 10, 1, 11),
    _Xldv20S3nMsEberThreshold_Type()
)
xldv20S3nMsEberThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20S3nMsEberThreshold.setStatus("mandatory")
_Xldv20S3nRsEberThreshold_Type = Xldv20S1nS3nEberThreshold
_Xldv20S3nRsEberThreshold_Object = MibTableColumn
xldv20S3nRsEberThreshold = _Xldv20S3nRsEberThreshold_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 10, 1, 12),
    _Xldv20S3nRsEberThreshold_Type()
)
xldv20S3nRsEberThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20S3nRsEberThreshold.setStatus("mandatory")
_Xldv20S3nSDThreshold_Type = Xldv20S1nS3nSDThreshold
_Xldv20S3nSDThreshold_Object = MibTableColumn
xldv20S3nSDThreshold = _Xldv20S3nSDThreshold_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 10, 1, 13),
    _Xldv20S3nSDThreshold_Type()
)
xldv20S3nSDThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20S3nSDThreshold.setStatus("mandatory")
_Xldv20S3nSignalLabelReceive_Type = Integer32
_Xldv20S3nSignalLabelReceive_Object = MibTableColumn
xldv20S3nSignalLabelReceive = _Xldv20S3nSignalLabelReceive_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 10, 1, 14),
    _Xldv20S3nSignalLabelReceive_Type()
)
xldv20S3nSignalLabelReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20S3nSignalLabelReceive.setStatus("mandatory")
_Xldv20S3nEmptyCellType_Type = Xldv20EmptyCellType
_Xldv20S3nEmptyCellType_Object = MibTableColumn
xldv20S3nEmptyCellType = _Xldv20S3nEmptyCellType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 10, 1, 15),
    _Xldv20S3nEmptyCellType_Type()
)
xldv20S3nEmptyCellType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20S3nEmptyCellType.setStatus("mandatory")


class _Xldv20S3nBandwidthUsage_Type(Integer32):
    """Custom type xldv20S3nBandwidthUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Xldv20S3nBandwidthUsage_Type.__name__ = "Integer32"
_Xldv20S3nBandwidthUsage_Object = MibTableColumn
xldv20S3nBandwidthUsage = _Xldv20S3nBandwidthUsage_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 10, 1, 16),
    _Xldv20S3nBandwidthUsage_Type()
)
xldv20S3nBandwidthUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20S3nBandwidthUsage.setStatus("mandatory")
_Xldv20Dsx1ConfigTable_Object = MibTable
xldv20Dsx1ConfigTable = _Xldv20Dsx1ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 11)
)
if mibBuilder.loadTexts:
    xldv20Dsx1ConfigTable.setStatus("mandatory")
_Xldv20Dsx1ConfigEntry_Object = MibTableRow
xldv20Dsx1ConfigEntry = _Xldv20Dsx1ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 11, 1)
)
xldv20Dsx1ConfigEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20IfIndex"),
)
if mibBuilder.loadTexts:
    xldv20Dsx1ConfigEntry.setStatus("mandatory")


class _Xldv20Dsx1LineType_Type(Integer32):
    """Custom type xldv20Dsx1LineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("dsx1D4", 3),
          ("dsx1E1", 4),
          ("dsx1E1-CRC", 5),
          ("dsx1E1-CRC-MF", 7),
          ("dsx1E1-MF", 6),
          ("dsx1ESF", 2),
          ("other", 1))
    )


_Xldv20Dsx1LineType_Type.__name__ = "Integer32"
_Xldv20Dsx1LineType_Object = MibTableColumn
xldv20Dsx1LineType = _Xldv20Dsx1LineType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 11, 1, 1),
    _Xldv20Dsx1LineType_Type()
)
xldv20Dsx1LineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20Dsx1LineType.setStatus("mandatory")


class _Xldv20Dsx1LineCoding_Type(Integer32):
    """Custom type xldv20Dsx1LineCoding based on Integer32"""
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
        *(("dsx1AMI", 5),
          ("dsx1B8ZS", 2),
          ("dsx1HDB3", 3),
          ("dsx1JBZS", 1),
          ("dsx1ZBTSI", 4),
          ("other", 6))
    )


_Xldv20Dsx1LineCoding_Type.__name__ = "Integer32"
_Xldv20Dsx1LineCoding_Object = MibTableColumn
xldv20Dsx1LineCoding = _Xldv20Dsx1LineCoding_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 11, 1, 2),
    _Xldv20Dsx1LineCoding_Type()
)
xldv20Dsx1LineCoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20Dsx1LineCoding.setStatus("mandatory")


class _Xldv20Dsx1LoopbackConfig_Type(Integer32):
    """Custom type xldv20Dsx1LoopbackConfig based on Integer32"""
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
        *(("dsx1LineLoop", 3),
          ("dsx1NoLoop", 1),
          ("dsx1OtherLoop", 4),
          ("dsx1PayloadLoop", 2))
    )


_Xldv20Dsx1LoopbackConfig_Type.__name__ = "Integer32"
_Xldv20Dsx1LoopbackConfig_Object = MibTableColumn
xldv20Dsx1LoopbackConfig = _Xldv20Dsx1LoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 11, 1, 3),
    _Xldv20Dsx1LoopbackConfig_Type()
)
xldv20Dsx1LoopbackConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20Dsx1LoopbackConfig.setStatus("mandatory")


class _Xldv20Dsx1SignalMode_Type(Integer32):
    """Custom type xldv20Dsx1SignalMode based on Integer32"""
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
        *(("bitOriented", 3),
          ("messageOriented", 4),
          ("none", 1),
          ("robbedBit", 2))
    )


_Xldv20Dsx1SignalMode_Type.__name__ = "Integer32"
_Xldv20Dsx1SignalMode_Object = MibTableColumn
xldv20Dsx1SignalMode = _Xldv20Dsx1SignalMode_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 11, 1, 4),
    _Xldv20Dsx1SignalMode_Type()
)
xldv20Dsx1SignalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20Dsx1SignalMode.setStatus("mandatory")


class _Xldv20Dsx1TransmitClockSource_Type(Integer32):
    """Custom type xldv20Dsx1TransmitClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("localTiming", 2),
          ("loopTiming", 1),
          ("throughTiming", 3))
    )


_Xldv20Dsx1TransmitClockSource_Type.__name__ = "Integer32"
_Xldv20Dsx1TransmitClockSource_Object = MibTableColumn
xldv20Dsx1TransmitClockSource = _Xldv20Dsx1TransmitClockSource_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 11, 1, 5),
    _Xldv20Dsx1TransmitClockSource_Type()
)
xldv20Dsx1TransmitClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20Dsx1TransmitClockSource.setStatus("mandatory")


class _Xldv20Dsx1Fdl_Type(Integer32):
    """Custom type xldv20Dsx1Fdl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("dsx1Ansi-T1-403", 2),
          ("dsx1Att-54016", 4),
          ("dsx1Fdl-none", 8),
          ("other", 1))
    )


_Xldv20Dsx1Fdl_Type.__name__ = "Integer32"
_Xldv20Dsx1Fdl_Object = MibTableColumn
xldv20Dsx1Fdl = _Xldv20Dsx1Fdl_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 11, 1, 6),
    _Xldv20Dsx1Fdl_Type()
)
xldv20Dsx1Fdl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20Dsx1Fdl.setStatus("mandatory")
_Xldv20SdcControl_ObjectIdentity = ObjectIdentity
xldv20SdcControl = _Xldv20SdcControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 12)
)
_Xldv20SdcCtrlControlReq_Type = Xldv20ControlReq
_Xldv20SdcCtrlControlReq_Object = MibScalar
xldv20SdcCtrlControlReq = _Xldv20SdcCtrlControlReq_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 12, 1),
    _Xldv20SdcCtrlControlReq_Type()
)
xldv20SdcCtrlControlReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20SdcCtrlControlReq.setStatus("mandatory")
_Xldv20SdcCtrlControlStatus_Type = Xldv20ControlStatus
_Xldv20SdcCtrlControlStatus_Object = MibScalar
xldv20SdcCtrlControlStatus = _Xldv20SdcCtrlControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 12, 2),
    _Xldv20SdcCtrlControlStatus_Type()
)
xldv20SdcCtrlControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20SdcCtrlControlStatus.setStatus("mandatory")
_Xldv20SdcCtrlIfIndex_Type = Unsigned16
_Xldv20SdcCtrlIfIndex_Object = MibScalar
xldv20SdcCtrlIfIndex = _Xldv20SdcCtrlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 12, 3),
    _Xldv20SdcCtrlIfIndex_Type()
)
xldv20SdcCtrlIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20SdcCtrlIfIndex.setStatus("mandatory")
_Xldv20SdcCtrlRate_Type = Xldv20SdslDataRate
_Xldv20SdcCtrlRate_Object = MibScalar
xldv20SdcCtrlRate = _Xldv20SdcCtrlRate_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 12, 4),
    _Xldv20SdcCtrlRate_Type()
)
xldv20SdcCtrlRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20SdcCtrlRate.setStatus("mandatory")
_Xldv20SdcCtrlXdslServiceType_Type = Xldv20SdslServiceType
_Xldv20SdcCtrlXdslServiceType_Object = MibScalar
xldv20SdcCtrlXdslServiceType = _Xldv20SdcCtrlXdslServiceType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 12, 5),
    _Xldv20SdcCtrlXdslServiceType_Type()
)
xldv20SdcCtrlXdslServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20SdcCtrlXdslServiceType.setStatus("mandatory")
_Xldv20SdcCtrlControlReqResult_Type = Xldv20ControlReq
_Xldv20SdcCtrlControlReqResult_Object = MibScalar
xldv20SdcCtrlControlReqResult = _Xldv20SdcCtrlControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 12, 6),
    _Xldv20SdcCtrlControlReqResult_Type()
)
xldv20SdcCtrlControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20SdcCtrlControlReqResult.setStatus("mandatory")
_Xldv20SdcCtrlControlTimeStamp_Type = TimeTicks
_Xldv20SdcCtrlControlTimeStamp_Object = MibScalar
xldv20SdcCtrlControlTimeStamp = _Xldv20SdcCtrlControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 12, 7),
    _Xldv20SdcCtrlControlTimeStamp_Type()
)
xldv20SdcCtrlControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20SdcCtrlControlTimeStamp.setStatus("mandatory")


class _Xldv20SdcCtrlMinMarginUp_Type(Integer32):
    """Custom type xldv20SdcCtrlMinMarginUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 128),
    )


_Xldv20SdcCtrlMinMarginUp_Type.__name__ = "Integer32"
_Xldv20SdcCtrlMinMarginUp_Object = MibScalar
xldv20SdcCtrlMinMarginUp = _Xldv20SdcCtrlMinMarginUp_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 12, 8),
    _Xldv20SdcCtrlMinMarginUp_Type()
)
xldv20SdcCtrlMinMarginUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20SdcCtrlMinMarginUp.setStatus("mandatory")
_Xldv20SdcPPTPTable_Object = MibTable
xldv20SdcPPTPTable = _Xldv20SdcPPTPTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 13)
)
if mibBuilder.loadTexts:
    xldv20SdcPPTPTable.setStatus("mandatory")
_Xldv20SdcPPTPEntry_Object = MibTableRow
xldv20SdcPPTPEntry = _Xldv20SdcPPTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 13, 1)
)
xldv20SdcPPTPEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20IfIndex"),
)
if mibBuilder.loadTexts:
    xldv20SdcPPTPEntry.setStatus("mandatory")
_Xldv20SdcRateCfg_Type = Xldv20SdslDataRate
_Xldv20SdcRateCfg_Object = MibTableColumn
xldv20SdcRateCfg = _Xldv20SdcRateCfg_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 13, 1, 1),
    _Xldv20SdcRateCfg_Type()
)
xldv20SdcRateCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20SdcRateCfg.setStatus("mandatory")
_Xldv20SdcXdslServiceTypeCfg_Type = Xldv20SdslServiceType
_Xldv20SdcXdslServiceTypeCfg_Object = MibTableColumn
xldv20SdcXdslServiceTypeCfg = _Xldv20SdcXdslServiceTypeCfg_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 13, 1, 2),
    _Xldv20SdcXdslServiceTypeCfg_Type()
)
xldv20SdcXdslServiceTypeCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20SdcXdslServiceTypeCfg.setStatus("mandatory")
_Xldv20SdcRate_Type = Xldv20SdslDataRateCurrent
_Xldv20SdcRate_Object = MibTableColumn
xldv20SdcRate = _Xldv20SdcRate_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 13, 1, 3),
    _Xldv20SdcRate_Type()
)
xldv20SdcRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20SdcRate.setStatus("mandatory")
_Xldv20SdcMarginDn_Type = Xldv20AdslMargin
_Xldv20SdcMarginDn_Object = MibTableColumn
xldv20SdcMarginDn = _Xldv20SdcMarginDn_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 13, 1, 4),
    _Xldv20SdcMarginDn_Type()
)
xldv20SdcMarginDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20SdcMarginDn.setStatus("mandatory")
_Xldv20SdcMarginUp_Type = Xldv20AdslMargin
_Xldv20SdcMarginUp_Object = MibTableColumn
xldv20SdcMarginUp = _Xldv20SdcMarginUp_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 13, 1, 5),
    _Xldv20SdcMarginUp_Type()
)
xldv20SdcMarginUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20SdcMarginUp.setStatus("mandatory")
_Xldv20SdcAttenuationDn_Type = Xldv20AdslAttenuation
_Xldv20SdcAttenuationDn_Object = MibTableColumn
xldv20SdcAttenuationDn = _Xldv20SdcAttenuationDn_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 13, 1, 6),
    _Xldv20SdcAttenuationDn_Type()
)
xldv20SdcAttenuationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20SdcAttenuationDn.setStatus("mandatory")
_Xldv20SdcAttenuationUp_Type = Xldv20AdslAttenuation
_Xldv20SdcAttenuationUp_Object = MibTableColumn
xldv20SdcAttenuationUp = _Xldv20SdcAttenuationUp_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 13, 1, 7),
    _Xldv20SdcAttenuationUp_Type()
)
xldv20SdcAttenuationUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20SdcAttenuationUp.setStatus("mandatory")
_Xldv20SdcLinkState_Type = Xldv20LinkState
_Xldv20SdcLinkState_Object = MibTableColumn
xldv20SdcLinkState = _Xldv20SdcLinkState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 13, 1, 8),
    _Xldv20SdcLinkState_Type()
)
xldv20SdcLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20SdcLinkState.setStatus("mandatory")
_Xldv20SdcAISOnLOS_Type = Xldv20OperState
_Xldv20SdcAISOnLOS_Object = MibTableColumn
xldv20SdcAISOnLOS = _Xldv20SdcAISOnLOS_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 13, 1, 9),
    _Xldv20SdcAISOnLOS_Type()
)
xldv20SdcAISOnLOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20SdcAISOnLOS.setStatus("mandatory")
_Xldv20SdcAISOnACT_Type = Xldv20OperState
_Xldv20SdcAISOnACT_Object = MibTableColumn
xldv20SdcAISOnACT = _Xldv20SdcAISOnACT_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 13, 1, 10),
    _Xldv20SdcAISOnACT_Type()
)
xldv20SdcAISOnACT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20SdcAISOnACT.setStatus("mandatory")


class _Xldv20SdcGuaranteedBandwidthUsage_Type(Integer32):
    """Custom type xldv20SdcGuaranteedBandwidthUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Xldv20SdcGuaranteedBandwidthUsage_Type.__name__ = "Integer32"
_Xldv20SdcGuaranteedBandwidthUsage_Object = MibTableColumn
xldv20SdcGuaranteedBandwidthUsage = _Xldv20SdcGuaranteedBandwidthUsage_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 13, 1, 11),
    _Xldv20SdcGuaranteedBandwidthUsage_Type()
)
xldv20SdcGuaranteedBandwidthUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20SdcGuaranteedBandwidthUsage.setStatus("mandatory")
_Xldv20SdcInitStatus_Type = Xldv20XdslInitStatus
_Xldv20SdcInitStatus_Object = MibTableColumn
xldv20SdcInitStatus = _Xldv20SdcInitStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 13, 1, 12),
    _Xldv20SdcInitStatus_Type()
)
xldv20SdcInitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20SdcInitStatus.setStatus("mandatory")


class _Xldv20SdcMinMarginUpCfg_Type(Integer32):
    """Custom type xldv20SdcMinMarginUpCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 128),
    )


_Xldv20SdcMinMarginUpCfg_Type.__name__ = "Integer32"
_Xldv20SdcMinMarginUpCfg_Object = MibTableColumn
xldv20SdcMinMarginUpCfg = _Xldv20SdcMinMarginUpCfg_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 13, 1, 13),
    _Xldv20SdcMinMarginUpCfg_Type()
)
xldv20SdcMinMarginUpCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20SdcMinMarginUpCfg.setStatus("mandatory")
_Xldv20SdcTransceiverOutputPower_Type = Xldv20AdslOutputPower
_Xldv20SdcTransceiverOutputPower_Object = MibTableColumn
xldv20SdcTransceiverOutputPower = _Xldv20SdcTransceiverOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 13, 1, 14),
    _Xldv20SdcTransceiverOutputPower_Type()
)
xldv20SdcTransceiverOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20SdcTransceiverOutputPower.setStatus("mandatory")
_Xldv20SdcXdslServiceType_Type = Xldv20XdslServiceTypeCurrent
_Xldv20SdcXdslServiceType_Object = MibTableColumn
xldv20SdcXdslServiceType = _Xldv20SdcXdslServiceType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 4, 13, 1, 15),
    _Xldv20SdcXdslServiceType_Type()
)
xldv20SdcXdslServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20SdcXdslServiceType.setStatus("mandatory")
_Xldv20TlmOam_ObjectIdentity = ObjectIdentity
xldv20TlmOam = _Xldv20TlmOam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 5)
)
_Xldv20LoopBackPointTable_Object = MibTable
xldv20LoopBackPointTable = _Xldv20LoopBackPointTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 5, 1)
)
if mibBuilder.loadTexts:
    xldv20LoopBackPointTable.setStatus("mandatory")
_Xldv20LbpEntry_Object = MibTableRow
xldv20LbpEntry = _Xldv20LbpEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 5, 1, 1)
)
xldv20LbpEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20IfIndex"),
)
if mibBuilder.loadTexts:
    xldv20LbpEntry.setStatus("mandatory")


class _Xldv20LbpLoopLocId_Type(OctetString):
    """Custom type xldv20LbpLoopLocId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Xldv20LbpLoopLocId_Type.__name__ = "OctetString"
_Xldv20LbpLoopLocId_Object = MibTableColumn
xldv20LbpLoopLocId = _Xldv20LbpLoopLocId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 5, 1, 1, 1),
    _Xldv20LbpLoopLocId_Type()
)
xldv20LbpLoopLocId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20LbpLoopLocId.setStatus("mandatory")
_Xldv20LbpLoopMode_Type = Xldv20LoopMode
_Xldv20LbpLoopMode_Object = MibTableColumn
xldv20LbpLoopMode = _Xldv20LbpLoopMode_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 5, 1, 1, 2),
    _Xldv20LbpLoopMode_Type()
)
xldv20LbpLoopMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20LbpLoopMode.setStatus("mandatory")
_Xldv20PhyLoopTest_ObjectIdentity = ObjectIdentity
xldv20PhyLoopTest = _Xldv20PhyLoopTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 5, 2)
)
_Xldv20PltIfIndex_Type = Unsigned16
_Xldv20PltIfIndex_Object = MibScalar
xldv20PltIfIndex = _Xldv20PltIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 5, 2, 1),
    _Xldv20PltIfIndex_Type()
)
xldv20PltIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20PltIfIndex.setStatus("mandatory")
_Xldv20PltControlReq_Type = Xldv20ControlReq
_Xldv20PltControlReq_Object = MibScalar
xldv20PltControlReq = _Xldv20PltControlReq_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 5, 2, 2),
    _Xldv20PltControlReq_Type()
)
xldv20PltControlReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20PltControlReq.setStatus("mandatory")
_Xldv20PltControlStatus_Type = Xldv20ControlStatus
_Xldv20PltControlStatus_Object = MibScalar
xldv20PltControlStatus = _Xldv20PltControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 5, 2, 3),
    _Xldv20PltControlStatus_Type()
)
xldv20PltControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20PltControlStatus.setStatus("mandatory")
_Xldv20PltControlTimer_Type = Unsigned32
_Xldv20PltControlTimer_Object = MibScalar
xldv20PltControlTimer = _Xldv20PltControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 5, 2, 4),
    _Xldv20PltControlTimer_Type()
)
xldv20PltControlTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20PltControlTimer.setStatus("mandatory")
_Xldv20PltControlReqResult_Type = Xldv20ControlReq
_Xldv20PltControlReqResult_Object = MibScalar
xldv20PltControlReqResult = _Xldv20PltControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 5, 2, 5),
    _Xldv20PltControlReqResult_Type()
)
xldv20PltControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20PltControlReqResult.setStatus("mandatory")
_Xldv20PltControlTimeStamp_Type = TimeTicks
_Xldv20PltControlTimeStamp_Object = MibScalar
xldv20PltControlTimeStamp = _Xldv20PltControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 5, 2, 6),
    _Xldv20PltControlTimeStamp_Type()
)
xldv20PltControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20PltControlTimeStamp.setStatus("mandatory")
_Xldv20AtmLoopTest_ObjectIdentity = ObjectIdentity
xldv20AtmLoopTest = _Xldv20AtmLoopTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 5, 3)
)
_Xldv20AltIfIndex_Type = Unsigned16
_Xldv20AltIfIndex_Object = MibScalar
xldv20AltIfIndex = _Xldv20AltIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 5, 3, 1),
    _Xldv20AltIfIndex_Type()
)
xldv20AltIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20AltIfIndex.setStatus("mandatory")


class _Xldv20AltVpi_Type(Integer32):
    """Custom type xldv20AltVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Xldv20AltVpi_Type.__name__ = "Integer32"
_Xldv20AltVpi_Object = MibScalar
xldv20AltVpi = _Xldv20AltVpi_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 5, 3, 2),
    _Xldv20AltVpi_Type()
)
xldv20AltVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20AltVpi.setStatus("mandatory")


class _Xldv20AltLoopLocId_Type(OctetString):
    """Custom type xldv20AltLoopLocId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Xldv20AltLoopLocId_Type.__name__ = "OctetString"
_Xldv20AltLoopLocId_Object = MibScalar
xldv20AltLoopLocId = _Xldv20AltLoopLocId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 5, 3, 3),
    _Xldv20AltLoopLocId_Type()
)
xldv20AltLoopLocId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20AltLoopLocId.setStatus("mandatory")
_Xldv20AltControlReq_Type = Xldv20ControlReq
_Xldv20AltControlReq_Object = MibScalar
xldv20AltControlReq = _Xldv20AltControlReq_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 5, 3, 4),
    _Xldv20AltControlReq_Type()
)
xldv20AltControlReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20AltControlReq.setStatus("mandatory")
_Xldv20AltControlStatus_Type = Xldv20ControlStatus
_Xldv20AltControlStatus_Object = MibScalar
xldv20AltControlStatus = _Xldv20AltControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 5, 3, 5),
    _Xldv20AltControlStatus_Type()
)
xldv20AltControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AltControlStatus.setStatus("mandatory")
_Xldv20AltControlTimer_Type = Unsigned32
_Xldv20AltControlTimer_Object = MibScalar
xldv20AltControlTimer = _Xldv20AltControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 5, 3, 6),
    _Xldv20AltControlTimer_Type()
)
xldv20AltControlTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AltControlTimer.setStatus("mandatory")
_Xldv20AltOamLevel_Type = Xldv20OamLevel
_Xldv20AltOamLevel_Object = MibScalar
xldv20AltOamLevel = _Xldv20AltOamLevel_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 5, 3, 7),
    _Xldv20AltOamLevel_Type()
)
xldv20AltOamLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20AltOamLevel.setStatus("mandatory")
_Xldv20AltLoopTestType_Type = Xldv20TestType
_Xldv20AltLoopTestType_Object = MibScalar
xldv20AltLoopTestType = _Xldv20AltLoopTestType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 5, 3, 8),
    _Xldv20AltLoopTestType_Type()
)
xldv20AltLoopTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20AltLoopTestType.setStatus("mandatory")


class _Xldv20AltVci_Type(Integer32):
    """Custom type xldv20AltVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Xldv20AltVci_Type.__name__ = "Integer32"
_Xldv20AltVci_Object = MibScalar
xldv20AltVci = _Xldv20AltVci_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 5, 3, 9),
    _Xldv20AltVci_Type()
)
xldv20AltVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20AltVci.setStatus("mandatory")
_Xldv20AltControlReqResult_Type = Xldv20ControlReq
_Xldv20AltControlReqResult_Object = MibScalar
xldv20AltControlReqResult = _Xldv20AltControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 5, 3, 10),
    _Xldv20AltControlReqResult_Type()
)
xldv20AltControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AltControlReqResult.setStatus("mandatory")
_Xldv20AltFlowDirection_Type = Xldv20FlowDirection
_Xldv20AltFlowDirection_Object = MibScalar
xldv20AltFlowDirection = _Xldv20AltFlowDirection_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 5, 3, 11),
    _Xldv20AltFlowDirection_Type()
)
xldv20AltFlowDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20AltFlowDirection.setStatus("mandatory")
_Xldv20AltControlTimeStamp_Type = TimeTicks
_Xldv20AltControlTimeStamp_Object = MibScalar
xldv20AltControlTimeStamp = _Xldv20AltControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 5, 3, 12),
    _Xldv20AltControlTimeStamp_Type()
)
xldv20AltControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AltControlTimeStamp.setStatus("mandatory")
_Xldv20MultipleLoopbackResultTable_Object = MibTable
xldv20MultipleLoopbackResultTable = _Xldv20MultipleLoopbackResultTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 5, 4)
)
if mibBuilder.loadTexts:
    xldv20MultipleLoopbackResultTable.setStatus("mandatory")
_Xldv20MlbEntry_Object = MibTableRow
xldv20MlbEntry = _Xldv20MlbEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 5, 4, 1)
)
xldv20MlbEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20MlbIndex"),
)
if mibBuilder.loadTexts:
    xldv20MlbEntry.setStatus("mandatory")
_Xldv20MlbIndex_Type = Unsigned16
_Xldv20MlbIndex_Object = MibTableColumn
xldv20MlbIndex = _Xldv20MlbIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 5, 4, 1, 1),
    _Xldv20MlbIndex_Type()
)
xldv20MlbIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20MlbIndex.setStatus("mandatory")


class _Xldv20MlbLoopLocId_Type(OctetString):
    """Custom type xldv20MlbLoopLocId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Xldv20MlbLoopLocId_Type.__name__ = "OctetString"
_Xldv20MlbLoopLocId_Object = MibTableColumn
xldv20MlbLoopLocId = _Xldv20MlbLoopLocId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 5, 4, 1, 2),
    _Xldv20MlbLoopLocId_Type()
)
xldv20MlbLoopLocId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20MlbLoopLocId.setStatus("mandatory")
_Xldv20Alarming_ObjectIdentity = ObjectIdentity
xldv20Alarming = _Xldv20Alarming_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6)
)
_Xldv20ExternalAlarmsTable_Object = MibTable
xldv20ExternalAlarmsTable = _Xldv20ExternalAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 1)
)
if mibBuilder.loadTexts:
    xldv20ExternalAlarmsTable.setStatus("mandatory")
_Xldv20ExternalAlarmEntry_Object = MibTableRow
xldv20ExternalAlarmEntry = _Xldv20ExternalAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 1, 1)
)
xldv20ExternalAlarmEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20ExtAlarmIndex"),
)
if mibBuilder.loadTexts:
    xldv20ExternalAlarmEntry.setStatus("mandatory")


class _Xldv20ExtAlarmIndex_Type(Integer32):
    """Custom type xldv20ExtAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Xldv20ExtAlarmIndex_Type.__name__ = "Integer32"
_Xldv20ExtAlarmIndex_Object = MibTableColumn
xldv20ExtAlarmIndex = _Xldv20ExtAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 1, 1, 1),
    _Xldv20ExtAlarmIndex_Type()
)
xldv20ExtAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ExtAlarmIndex.setStatus("mandatory")
_Xldv20ExtAlarmAdminState_Type = Xldv20AdminState
_Xldv20ExtAlarmAdminState_Object = MibTableColumn
xldv20ExtAlarmAdminState = _Xldv20ExtAlarmAdminState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 1, 1, 2),
    _Xldv20ExtAlarmAdminState_Type()
)
xldv20ExtAlarmAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20ExtAlarmAdminState.setStatus("mandatory")
_Xldv20ExtAlarmOperState_Type = Xldv20OperState
_Xldv20ExtAlarmOperState_Object = MibTableColumn
xldv20ExtAlarmOperState = _Xldv20ExtAlarmOperState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 1, 1, 3),
    _Xldv20ExtAlarmOperState_Type()
)
xldv20ExtAlarmOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ExtAlarmOperState.setStatus("mandatory")
_Xldv20ExtAlarmActivityState_Type = Xldv20ExtAlarmActivityState
_Xldv20ExtAlarmActivityState_Object = MibTableColumn
xldv20ExtAlarmActivityState = _Xldv20ExtAlarmActivityState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 1, 1, 4),
    _Xldv20ExtAlarmActivityState_Type()
)
xldv20ExtAlarmActivityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ExtAlarmActivityState.setStatus("mandatory")
_Xldv20ExtAlarmSeverityIndex_Type = Xldv20AlmSevProfileIndex
_Xldv20ExtAlarmSeverityIndex_Object = MibTableColumn
xldv20ExtAlarmSeverityIndex = _Xldv20ExtAlarmSeverityIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 1, 1, 5),
    _Xldv20ExtAlarmSeverityIndex_Type()
)
xldv20ExtAlarmSeverityIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20ExtAlarmSeverityIndex.setStatus("mandatory")
_Xldv20ExtAlarmFilteringIndex_Type = Xldv20AlmFiltProfileIndex
_Xldv20ExtAlarmFilteringIndex_Object = MibTableColumn
xldv20ExtAlarmFilteringIndex = _Xldv20ExtAlarmFilteringIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 1, 1, 6),
    _Xldv20ExtAlarmFilteringIndex_Type()
)
xldv20ExtAlarmFilteringIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ExtAlarmFilteringIndex.setStatus("mandatory")


class _Xldv20ExtAlarmName_Type(OctetString):
    """Custom type xldv20ExtAlarmName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_Xldv20ExtAlarmName_Type.__name__ = "OctetString"
_Xldv20ExtAlarmName_Object = MibTableColumn
xldv20ExtAlarmName = _Xldv20ExtAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 1, 1, 7),
    _Xldv20ExtAlarmName_Type()
)
xldv20ExtAlarmName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20ExtAlarmName.setStatus("mandatory")
_Xldv20AlarmSeverityProfileTable_Object = MibTable
xldv20AlarmSeverityProfileTable = _Xldv20AlarmSeverityProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 2)
)
if mibBuilder.loadTexts:
    xldv20AlarmSeverityProfileTable.setStatus("mandatory")
_Xldv20AlarmSeverityProfileEntry_Object = MibTableRow
xldv20AlarmSeverityProfileEntry = _Xldv20AlarmSeverityProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 2, 1)
)
xldv20AlarmSeverityProfileEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20AlmSevProfileIndex"),
)
if mibBuilder.loadTexts:
    xldv20AlarmSeverityProfileEntry.setStatus("mandatory")
_Xldv20AlmSevProfileIndex_Type = Xldv20AlmSevProfileIndex
_Xldv20AlmSevProfileIndex_Object = MibTableColumn
xldv20AlmSevProfileIndex = _Xldv20AlmSevProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 2, 1, 1),
    _Xldv20AlmSevProfileIndex_Type()
)
xldv20AlmSevProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AlmSevProfileIndex.setStatus("mandatory")
_Xldv20AlmSevProfileRowStatus_Type = Xldv20RowStatus
_Xldv20AlmSevProfileRowStatus_Object = MibTableColumn
xldv20AlmSevProfileRowStatus = _Xldv20AlmSevProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 2, 1, 2),
    _Xldv20AlmSevProfileRowStatus_Type()
)
xldv20AlmSevProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20AlmSevProfileRowStatus.setStatus("mandatory")
_Xldv20AlarmSeverityTable_Object = MibTable
xldv20AlarmSeverityTable = _Xldv20AlarmSeverityTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 3)
)
if mibBuilder.loadTexts:
    xldv20AlarmSeverityTable.setStatus("mandatory")
_Xldv20AlarmSeverityEntry_Object = MibTableRow
xldv20AlarmSeverityEntry = _Xldv20AlarmSeverityEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 3, 1)
)
xldv20AlarmSeverityEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20AlmSevProfileIndex"),
    (0, "XLDV20-MIB", "xldv20AlmSevTrapId"),
)
if mibBuilder.loadTexts:
    xldv20AlarmSeverityEntry.setStatus("mandatory")
_Xldv20AlmSevTrapId_Type = Xldv20TrapIds
_Xldv20AlmSevTrapId_Object = MibTableColumn
xldv20AlmSevTrapId = _Xldv20AlmSevTrapId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 3, 1, 1),
    _Xldv20AlmSevTrapId_Type()
)
xldv20AlmSevTrapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AlmSevTrapId.setStatus("mandatory")
_Xldv20AlmSeverity_Type = Xldv20AlarmSeverity
_Xldv20AlmSeverity_Object = MibTableColumn
xldv20AlmSeverity = _Xldv20AlmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 3, 1, 2),
    _Xldv20AlmSeverity_Type()
)
xldv20AlmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20AlmSeverity.setStatus("mandatory")
_Xldv20AlarmFilteringProfileTable_Object = MibTable
xldv20AlarmFilteringProfileTable = _Xldv20AlarmFilteringProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 4)
)
if mibBuilder.loadTexts:
    xldv20AlarmFilteringProfileTable.setStatus("mandatory")
_Xldv20AlarmFilteringProfileEntry_Object = MibTableRow
xldv20AlarmFilteringProfileEntry = _Xldv20AlarmFilteringProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 4, 1)
)
xldv20AlarmFilteringProfileEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20AlmFiltProfileIndex"),
)
if mibBuilder.loadTexts:
    xldv20AlarmFilteringProfileEntry.setStatus("mandatory")
_Xldv20AlmFiltProfileIndex_Type = Xldv20AlmFiltProfileIndex
_Xldv20AlmFiltProfileIndex_Object = MibTableColumn
xldv20AlmFiltProfileIndex = _Xldv20AlmFiltProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 4, 1, 1),
    _Xldv20AlmFiltProfileIndex_Type()
)
xldv20AlmFiltProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AlmFiltProfileIndex.setStatus("mandatory")
_Xldv20AlmFiltProfileRowStatus_Type = Xldv20RowStatus
_Xldv20AlmFiltProfileRowStatus_Object = MibTableColumn
xldv20AlmFiltProfileRowStatus = _Xldv20AlmFiltProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 4, 1, 2),
    _Xldv20AlmFiltProfileRowStatus_Type()
)
xldv20AlmFiltProfileRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AlmFiltProfileRowStatus.setStatus("mandatory")
_Xldv20AlarmFilteringTable_Object = MibTable
xldv20AlarmFilteringTable = _Xldv20AlarmFilteringTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 5)
)
if mibBuilder.loadTexts:
    xldv20AlarmFilteringTable.setStatus("mandatory")
_Xldv20AlarmFilteringEntry_Object = MibTableRow
xldv20AlarmFilteringEntry = _Xldv20AlarmFilteringEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 5, 1)
)
xldv20AlarmFilteringEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20AlmFiltProfileIndex"),
    (0, "XLDV20-MIB", "xldv20AlmFiltTrapId"),
)
if mibBuilder.loadTexts:
    xldv20AlarmFilteringEntry.setStatus("mandatory")
_Xldv20AlmFiltTrapId_Type = Xldv20TrapIds
_Xldv20AlmFiltTrapId_Object = MibTableColumn
xldv20AlmFiltTrapId = _Xldv20AlmFiltTrapId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 5, 1, 1),
    _Xldv20AlmFiltTrapId_Type()
)
xldv20AlmFiltTrapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AlmFiltTrapId.setStatus("mandatory")


class _Xldv20AlmTempFilter_Type(Integer32):
    """Custom type xldv20AlmTempFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_Xldv20AlmTempFilter_Type.__name__ = "Integer32"
_Xldv20AlmTempFilter_Object = MibTableColumn
xldv20AlmTempFilter = _Xldv20AlmTempFilter_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 5, 1, 2),
    _Xldv20AlmTempFilter_Type()
)
xldv20AlmTempFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AlmTempFilter.setStatus("mandatory")
_Xldv20AlarmListTable_Object = MibTable
xldv20AlarmListTable = _Xldv20AlarmListTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 6)
)
if mibBuilder.loadTexts:
    xldv20AlarmListTable.setStatus("mandatory")
_Xldv20AlarmListEntry_Object = MibTableRow
xldv20AlarmListEntry = _Xldv20AlarmListEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 6, 1)
)
xldv20AlarmListEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20AlmIndex"),
)
if mibBuilder.loadTexts:
    xldv20AlarmListEntry.setStatus("mandatory")


class _Xldv20AlmIndex_Type(Integer32):
    """Custom type xldv20AlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 700),
    )


_Xldv20AlmIndex_Type.__name__ = "Integer32"
_Xldv20AlmIndex_Object = MibTableColumn
xldv20AlmIndex = _Xldv20AlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 6, 1, 1),
    _Xldv20AlmIndex_Type()
)
xldv20AlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AlmIndex.setStatus("mandatory")
_Xldv20AlmNatureOfAlarm_Type = Xldv20TrapIds
_Xldv20AlmNatureOfAlarm_Object = MibTableColumn
xldv20AlmNatureOfAlarm = _Xldv20AlmNatureOfAlarm_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 6, 1, 2),
    _Xldv20AlmNatureOfAlarm_Type()
)
xldv20AlmNatureOfAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AlmNatureOfAlarm.setStatus("mandatory")


class _Xldv20AlmSpecProblem_Type(Integer32):
    """Custom type xldv20AlmSpecProblem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Xldv20AlmSpecProblem_Type.__name__ = "Integer32"
_Xldv20AlmSpecProblem_Object = MibTableColumn
xldv20AlmSpecProblem = _Xldv20AlmSpecProblem_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 6, 1, 3),
    _Xldv20AlmSpecProblem_Type()
)
xldv20AlmSpecProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AlmSpecProblem.setStatus("mandatory")


class _Xldv20AlmSpecProblemText_Type(OctetString):
    """Custom type xldv20AlmSpecProblemText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_Xldv20AlmSpecProblemText_Type.__name__ = "OctetString"
_Xldv20AlmSpecProblemText_Object = MibTableColumn
xldv20AlmSpecProblemText = _Xldv20AlmSpecProblemText_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 6, 1, 4),
    _Xldv20AlmSpecProblemText_Type()
)
xldv20AlmSpecProblemText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AlmSpecProblemText.setStatus("mandatory")
_Xldv20AlmRepEntityId_Type = Integer32
_Xldv20AlmRepEntityId_Object = MibTableColumn
xldv20AlmRepEntityId = _Xldv20AlmRepEntityId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 6, 1, 5),
    _Xldv20AlmRepEntityId_Type()
)
xldv20AlmRepEntityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AlmRepEntityId.setStatus("mandatory")
_Xldv20AlmRepSource_Type = Xldv20RepSource
_Xldv20AlmRepSource_Object = MibTableColumn
xldv20AlmRepSource = _Xldv20AlmRepSource_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 6, 1, 6),
    _Xldv20AlmRepSource_Type()
)
xldv20AlmRepSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AlmRepSource.setStatus("mandatory")
_Xldv20AlmFailedComponent_Type = Integer32
_Xldv20AlmFailedComponent_Object = MibTableColumn
xldv20AlmFailedComponent = _Xldv20AlmFailedComponent_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 6, 1, 7),
    _Xldv20AlmFailedComponent_Type()
)
xldv20AlmFailedComponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AlmFailedComponent.setStatus("mandatory")
_Xldv20AlmFailedComponentRepSource_Type = Xldv20RepSource
_Xldv20AlmFailedComponentRepSource_Object = MibTableColumn
xldv20AlmFailedComponentRepSource = _Xldv20AlmFailedComponentRepSource_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 6, 1, 8),
    _Xldv20AlmFailedComponentRepSource_Type()
)
xldv20AlmFailedComponentRepSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AlmFailedComponentRepSource.setStatus("mandatory")
_Xldv20AlmSeverityOfFailure_Type = Xldv20AlarmSeverity
_Xldv20AlmSeverityOfFailure_Object = MibTableColumn
xldv20AlmSeverityOfFailure = _Xldv20AlmSeverityOfFailure_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 6, 1, 9),
    _Xldv20AlmSeverityOfFailure_Type()
)
xldv20AlmSeverityOfFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AlmSeverityOfFailure.setStatus("mandatory")
_Xldv20AlmPropRepairAction_Type = Integer32
_Xldv20AlmPropRepairAction_Object = MibTableColumn
xldv20AlmPropRepairAction = _Xldv20AlmPropRepairAction_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 6, 1, 10),
    _Xldv20AlmPropRepairAction_Type()
)
xldv20AlmPropRepairAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AlmPropRepairAction.setStatus("mandatory")
_Xldv20AlmTimeAndDate_Type = Integer32
_Xldv20AlmTimeAndDate_Object = MibTableColumn
xldv20AlmTimeAndDate = _Xldv20AlmTimeAndDate_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 6, 1, 11),
    _Xldv20AlmTimeAndDate_Type()
)
xldv20AlmTimeAndDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AlmTimeAndDate.setStatus("mandatory")
_Xldv20AlmControl_ObjectIdentity = ObjectIdentity
xldv20AlmControl = _Xldv20AlmControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 7)
)
_Xldv20AlmControlReq_Type = Xldv20ControlReq
_Xldv20AlmControlReq_Object = MibScalar
xldv20AlmControlReq = _Xldv20AlmControlReq_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 7, 1),
    _Xldv20AlmControlReq_Type()
)
xldv20AlmControlReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20AlmControlReq.setStatus("mandatory")
_Xldv20AlmControlStatus_Type = Xldv20ControlStatus
_Xldv20AlmControlStatus_Object = MibScalar
xldv20AlmControlStatus = _Xldv20AlmControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 7, 2),
    _Xldv20AlmControlStatus_Type()
)
xldv20AlmControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AlmControlStatus.setStatus("mandatory")
_Xldv20AlmControlReqResult_Type = Xldv20ControlReq
_Xldv20AlmControlReqResult_Object = MibScalar
xldv20AlmControlReqResult = _Xldv20AlmControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 7, 3),
    _Xldv20AlmControlReqResult_Type()
)
xldv20AlmControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AlmControlReqResult.setStatus("mandatory")
_Xldv20AlmControlTimeStamp_Type = TimeTicks
_Xldv20AlmControlTimeStamp_Object = MibScalar
xldv20AlmControlTimeStamp = _Xldv20AlmControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 7, 4),
    _Xldv20AlmControlTimeStamp_Type()
)
xldv20AlmControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20AlmControlTimeStamp.setStatus("mandatory")
_Xldv20Reset_ObjectIdentity = ObjectIdentity
xldv20Reset = _Xldv20Reset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 8)
)
_Xldv20RstControlReq_Type = Xldv20ControlReq
_Xldv20RstControlReq_Object = MibScalar
xldv20RstControlReq = _Xldv20RstControlReq_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 8, 1),
    _Xldv20RstControlReq_Type()
)
xldv20RstControlReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20RstControlReq.setStatus("mandatory")
_Xldv20RstControlStatus_Type = Xldv20ControlStatus
_Xldv20RstControlStatus_Object = MibScalar
xldv20RstControlStatus = _Xldv20RstControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 8, 2),
    _Xldv20RstControlStatus_Type()
)
xldv20RstControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20RstControlStatus.setStatus("mandatory")
_Xldv20RstLevel_Type = Xldv20ResetLevel
_Xldv20RstLevel_Object = MibScalar
xldv20RstLevel = _Xldv20RstLevel_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 8, 3),
    _Xldv20RstLevel_Type()
)
xldv20RstLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20RstLevel.setStatus("mandatory")
_Xldv20RstHwUnitIndex_Type = Unsigned16
_Xldv20RstHwUnitIndex_Object = MibScalar
xldv20RstHwUnitIndex = _Xldv20RstHwUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 8, 4),
    _Xldv20RstHwUnitIndex_Type()
)
xldv20RstHwUnitIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20RstHwUnitIndex.setStatus("mandatory")
_Xldv20RstControlTimer_Type = Unsigned32
_Xldv20RstControlTimer_Object = MibScalar
xldv20RstControlTimer = _Xldv20RstControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 8, 5),
    _Xldv20RstControlTimer_Type()
)
xldv20RstControlTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20RstControlTimer.setStatus("mandatory")
_Xldv20RstControlReqResult_Type = Xldv20ControlReq
_Xldv20RstControlReqResult_Object = MibScalar
xldv20RstControlReqResult = _Xldv20RstControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 8, 6),
    _Xldv20RstControlReqResult_Type()
)
xldv20RstControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20RstControlReqResult.setStatus("mandatory")
_Xldv20RstControlTimeStamp_Type = TimeTicks
_Xldv20RstControlTimeStamp_Object = MibScalar
xldv20RstControlTimeStamp = _Xldv20RstControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 6, 8, 7),
    _Xldv20RstControlTimeStamp_Type()
)
xldv20RstControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20RstControlTimeStamp.setStatus("mandatory")
_Xldv20Swm_ObjectIdentity = ObjectIdentity
xldv20Swm = _Xldv20Swm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 7)
)
_Xldv20SwmLogHandler_ObjectIdentity = ObjectIdentity
xldv20SwmLogHandler = _Xldv20SwmLogHandler_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 7, 1)
)
_Xldv20DbuControlReq_Type = Xldv20ControlReq
_Xldv20DbuControlReq_Object = MibScalar
xldv20DbuControlReq = _Xldv20DbuControlReq_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 7, 1, 1),
    _Xldv20DbuControlReq_Type()
)
xldv20DbuControlReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20DbuControlReq.setStatus("mandatory")
_Xldv20DbuControlStatus_Type = Xldv20ControlStatus
_Xldv20DbuControlStatus_Object = MibScalar
xldv20DbuControlStatus = _Xldv20DbuControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 7, 1, 2),
    _Xldv20DbuControlStatus_Type()
)
xldv20DbuControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20DbuControlStatus.setStatus("mandatory")


class _Xldv20DbuResultFilePath_Type(OctetString):
    """Custom type xldv20DbuResultFilePath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 150),
    )


_Xldv20DbuResultFilePath_Type.__name__ = "OctetString"
_Xldv20DbuResultFilePath_Object = MibScalar
xldv20DbuResultFilePath = _Xldv20DbuResultFilePath_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 7, 1, 3),
    _Xldv20DbuResultFilePath_Type()
)
xldv20DbuResultFilePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20DbuResultFilePath.setStatus("mandatory")
_Xldv20DbuLogType_Type = Xldv20LogType
_Xldv20DbuLogType_Object = MibScalar
xldv20DbuLogType = _Xldv20DbuLogType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 7, 1, 4),
    _Xldv20DbuLogType_Type()
)
xldv20DbuLogType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20DbuLogType.setStatus("mandatory")


class _Xldv20DbuNumEntries_Type(Integer32):
    """Custom type xldv20DbuNumEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Xldv20DbuNumEntries_Type.__name__ = "Integer32"
_Xldv20DbuNumEntries_Object = MibScalar
xldv20DbuNumEntries = _Xldv20DbuNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 7, 1, 5),
    _Xldv20DbuNumEntries_Type()
)
xldv20DbuNumEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20DbuNumEntries.setStatus("mandatory")
_Xldv20DbuControlTimer_Type = Unsigned32
_Xldv20DbuControlTimer_Object = MibScalar
xldv20DbuControlTimer = _Xldv20DbuControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 7, 1, 6),
    _Xldv20DbuControlTimer_Type()
)
xldv20DbuControlTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20DbuControlTimer.setStatus("mandatory")
_Xldv20DbuControlReqResult_Type = Xldv20ControlReq
_Xldv20DbuControlReqResult_Object = MibScalar
xldv20DbuControlReqResult = _Xldv20DbuControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 7, 1, 7),
    _Xldv20DbuControlReqResult_Type()
)
xldv20DbuControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20DbuControlReqResult.setStatus("mandatory")
_Xldv20DbuHwUnitIndex_Type = Unsigned16
_Xldv20DbuHwUnitIndex_Object = MibScalar
xldv20DbuHwUnitIndex = _Xldv20DbuHwUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 7, 1, 8),
    _Xldv20DbuHwUnitIndex_Type()
)
xldv20DbuHwUnitIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20DbuHwUnitIndex.setStatus("mandatory")
_Xldv20DbuControlTimeStamp_Type = TimeTicks
_Xldv20DbuControlTimeStamp_Object = MibScalar
xldv20DbuControlTimeStamp = _Xldv20DbuControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 7, 1, 9),
    _Xldv20DbuControlTimeStamp_Type()
)
xldv20DbuControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20DbuControlTimeStamp.setStatus("mandatory")
_Xldv20SwmUpgradeControl_ObjectIdentity = ObjectIdentity
xldv20SwmUpgradeControl = _Xldv20SwmUpgradeControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 7, 2)
)


class _Xldv20SucUnit_Type(OctetString):
    """Custom type xldv20SucUnit based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Xldv20SucUnit_Type.__name__ = "OctetString"
_Xldv20SucUnit_Object = MibScalar
xldv20SucUnit = _Xldv20SucUnit_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 7, 2, 1),
    _Xldv20SucUnit_Type()
)
xldv20SucUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20SucUnit.setStatus("mandatory")
_Xldv20SucAllOfType_Type = Xldv20SucAllOfType
_Xldv20SucAllOfType_Object = MibScalar
xldv20SucAllOfType = _Xldv20SucAllOfType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 7, 2, 2),
    _Xldv20SucAllOfType_Type()
)
xldv20SucAllOfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20SucAllOfType.setStatus("mandatory")


class _Xldv20SucVersionNo_Type(OctetString):
    """Custom type xldv20SucVersionNo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Xldv20SucVersionNo_Type.__name__ = "OctetString"
_Xldv20SucVersionNo_Object = MibScalar
xldv20SucVersionNo = _Xldv20SucVersionNo_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 7, 2, 3),
    _Xldv20SucVersionNo_Type()
)
xldv20SucVersionNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20SucVersionNo.setStatus("mandatory")
_Xldv20SucHwUnitIndex_Type = Unsigned16
_Xldv20SucHwUnitIndex_Object = MibScalar
xldv20SucHwUnitIndex = _Xldv20SucHwUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 7, 2, 4),
    _Xldv20SucHwUnitIndex_Type()
)
xldv20SucHwUnitIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20SucHwUnitIndex.setStatus("mandatory")


class _Xldv20SucPathName_Type(OctetString):
    """Custom type xldv20SucPathName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 121),
    )


_Xldv20SucPathName_Type.__name__ = "OctetString"
_Xldv20SucPathName_Object = MibScalar
xldv20SucPathName = _Xldv20SucPathName_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 7, 2, 5),
    _Xldv20SucPathName_Type()
)
xldv20SucPathName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20SucPathName.setStatus("mandatory")


class _Xldv20SucFileName_Type(OctetString):
    """Custom type xldv20SucFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 33),
    )


_Xldv20SucFileName_Type.__name__ = "OctetString"
_Xldv20SucFileName_Object = MibScalar
xldv20SucFileName = _Xldv20SucFileName_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 7, 2, 6),
    _Xldv20SucFileName_Type()
)
xldv20SucFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20SucFileName.setStatus("mandatory")
_Xldv20SucControlReq_Type = Xldv20ControlReq
_Xldv20SucControlReq_Object = MibScalar
xldv20SucControlReq = _Xldv20SucControlReq_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 7, 2, 7),
    _Xldv20SucControlReq_Type()
)
xldv20SucControlReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20SucControlReq.setStatus("mandatory")
_Xldv20SucControlStatus_Type = Xldv20ControlStatus
_Xldv20SucControlStatus_Object = MibScalar
xldv20SucControlStatus = _Xldv20SucControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 7, 2, 8),
    _Xldv20SucControlStatus_Type()
)
xldv20SucControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20SucControlStatus.setStatus("mandatory")
_Xldv20SucControlTimer_Type = Unsigned32
_Xldv20SucControlTimer_Object = MibScalar
xldv20SucControlTimer = _Xldv20SucControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 7, 2, 9),
    _Xldv20SucControlTimer_Type()
)
xldv20SucControlTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20SucControlTimer.setStatus("mandatory")
_Xldv20SucNumberOfTraps_Type = Integer32
_Xldv20SucNumberOfTraps_Object = MibScalar
xldv20SucNumberOfTraps = _Xldv20SucNumberOfTraps_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 7, 2, 10),
    _Xldv20SucNumberOfTraps_Type()
)
xldv20SucNumberOfTraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20SucNumberOfTraps.setStatus("mandatory")


class _Xldv20SucDefaultSwVersion_Type(DisplayString):
    """Custom type xldv20SucDefaultSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Xldv20SucDefaultSwVersion_Type.__name__ = "DisplayString"
_Xldv20SucDefaultSwVersion_Object = MibScalar
xldv20SucDefaultSwVersion = _Xldv20SucDefaultSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 7, 2, 11),
    _Xldv20SucDefaultSwVersion_Type()
)
xldv20SucDefaultSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20SucDefaultSwVersion.setStatus("mandatory")


class _Xldv20SucPredecessorSwVersion_Type(DisplayString):
    """Custom type xldv20SucPredecessorSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Xldv20SucPredecessorSwVersion_Type.__name__ = "DisplayString"
_Xldv20SucPredecessorSwVersion_Object = MibScalar
xldv20SucPredecessorSwVersion = _Xldv20SucPredecessorSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 7, 2, 12),
    _Xldv20SucPredecessorSwVersion_Type()
)
xldv20SucPredecessorSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20SucPredecessorSwVersion.setStatus("mandatory")


class _Xldv20SucPrePredecessorSwVersion_Type(DisplayString):
    """Custom type xldv20SucPrePredecessorSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Xldv20SucPrePredecessorSwVersion_Type.__name__ = "DisplayString"
_Xldv20SucPrePredecessorSwVersion_Object = MibScalar
xldv20SucPrePredecessorSwVersion = _Xldv20SucPrePredecessorSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 7, 2, 13),
    _Xldv20SucPrePredecessorSwVersion_Type()
)
xldv20SucPrePredecessorSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20SucPrePredecessorSwVersion.setStatus("mandatory")
_Xldv20SucControlReqResult_Type = Xldv20ControlReq
_Xldv20SucControlReqResult_Object = MibScalar
xldv20SucControlReqResult = _Xldv20SucControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 7, 2, 14),
    _Xldv20SucControlReqResult_Type()
)
xldv20SucControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20SucControlReqResult.setStatus("mandatory")
_Xldv20SucControlTimeStamp_Type = TimeTicks
_Xldv20SucControlTimeStamp_Object = MibScalar
xldv20SucControlTimeStamp = _Xldv20SucControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 7, 2, 15),
    _Xldv20SucControlTimeStamp_Type()
)
xldv20SucControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20SucControlTimeStamp.setStatus("mandatory")
_Xldv20SwUpgradeTaskTable_Object = MibTable
xldv20SwUpgradeTaskTable = _Xldv20SwUpgradeTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 7, 3)
)
if mibBuilder.loadTexts:
    xldv20SwUpgradeTaskTable.setStatus("mandatory")
_Xldv20SutTaskTableEntry_Object = MibTableRow
xldv20SutTaskTableEntry = _Xldv20SutTaskTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 7, 3, 1)
)
xldv20SutTaskTableEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20SutIndex"),
)
if mibBuilder.loadTexts:
    xldv20SutTaskTableEntry.setStatus("mandatory")
_Xldv20SutIndex_Type = Unsigned16
_Xldv20SutIndex_Object = MibTableColumn
xldv20SutIndex = _Xldv20SutIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 7, 3, 1, 1),
    _Xldv20SutIndex_Type()
)
xldv20SutIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20SutIndex.setStatus("mandatory")


class _Xldv20SutPiuType_Type(OctetString):
    """Custom type xldv20SutPiuType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Xldv20SutPiuType_Type.__name__ = "OctetString"
_Xldv20SutPiuType_Object = MibTableColumn
xldv20SutPiuType = _Xldv20SutPiuType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 7, 3, 1, 2),
    _Xldv20SutPiuType_Type()
)
xldv20SutPiuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20SutPiuType.setStatus("mandatory")
_Xldv20SutHwUnitIndex_Type = Unsigned16
_Xldv20SutHwUnitIndex_Object = MibTableColumn
xldv20SutHwUnitIndex = _Xldv20SutHwUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 7, 3, 1, 3),
    _Xldv20SutHwUnitIndex_Type()
)
xldv20SutHwUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20SutHwUnitIndex.setStatus("mandatory")


class _Xldv20SutSwVersion_Type(OctetString):
    """Custom type xldv20SutSwVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Xldv20SutSwVersion_Type.__name__ = "OctetString"
_Xldv20SutSwVersion_Object = MibTableColumn
xldv20SutSwVersion = _Xldv20SutSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 7, 3, 1, 4),
    _Xldv20SutSwVersion_Type()
)
xldv20SutSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20SutSwVersion.setStatus("mandatory")
_Xldv20SutRequester_Type = Xldv20Requester
_Xldv20SutRequester_Object = MibTableColumn
xldv20SutRequester = _Xldv20SutRequester_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 7, 3, 1, 5),
    _Xldv20SutRequester_Type()
)
xldv20SutRequester.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20SutRequester.setStatus("mandatory")
_Xldv20SutUpgradeState_Type = Xldv20ControlReq
_Xldv20SutUpgradeState_Object = MibTableColumn
xldv20SutUpgradeState = _Xldv20SutUpgradeState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 7, 3, 1, 6),
    _Xldv20SutUpgradeState_Type()
)
xldv20SutUpgradeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20SutUpgradeState.setStatus("mandatory")
_Xldv20SutUpgradeResult_Type = Xldv20ControlReq
_Xldv20SutUpgradeResult_Object = MibTableColumn
xldv20SutUpgradeResult = _Xldv20SutUpgradeResult_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 7, 3, 1, 7),
    _Xldv20SutUpgradeResult_Type()
)
xldv20SutUpgradeResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20SutUpgradeResult.setStatus("mandatory")
_Xldv20SutTimeStamp_Type = TimeTicks
_Xldv20SutTimeStamp_Object = MibTableColumn
xldv20SutTimeStamp = _Xldv20SutTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 7, 3, 1, 8),
    _Xldv20SutTimeStamp_Type()
)
xldv20SutTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20SutTimeStamp.setStatus("mandatory")
_Xldv20StcSecureTelnetControl_ObjectIdentity = ObjectIdentity
xldv20StcSecureTelnetControl = _Xldv20StcSecureTelnetControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 7, 4)
)
_Xldv20StcTelnetAccess_Type = Xldv20TelnetAccess
_Xldv20StcTelnetAccess_Object = MibScalar
xldv20StcTelnetAccess = _Xldv20StcTelnetAccess_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 7, 4, 1),
    _Xldv20StcTelnetAccess_Type()
)
xldv20StcTelnetAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20StcTelnetAccess.setStatus("mandatory")
_Xldv20Dbm_ObjectIdentity = ObjectIdentity
xldv20Dbm = _Xldv20Dbm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 8)
)
_Xldv20DbmControl_ObjectIdentity = ObjectIdentity
xldv20DbmControl = _Xldv20DbmControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 8, 1)
)
_Xldv20DbmControlReq_Type = Xldv20ControlReq
_Xldv20DbmControlReq_Object = MibScalar
xldv20DbmControlReq = _Xldv20DbmControlReq_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 8, 1, 1),
    _Xldv20DbmControlReq_Type()
)
xldv20DbmControlReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20DbmControlReq.setStatus("mandatory")
_Xldv20DbmControlStatus_Type = Xldv20ControlStatus
_Xldv20DbmControlStatus_Object = MibScalar
xldv20DbmControlStatus = _Xldv20DbmControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 8, 1, 2),
    _Xldv20DbmControlStatus_Type()
)
xldv20DbmControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20DbmControlStatus.setStatus("mandatory")
_Xldv20DbmControlTimer_Type = Unsigned32
_Xldv20DbmControlTimer_Object = MibScalar
xldv20DbmControlTimer = _Xldv20DbmControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 8, 1, 3),
    _Xldv20DbmControlTimer_Type()
)
xldv20DbmControlTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20DbmControlTimer.setStatus("mandatory")


class _Xldv20DbmBackupPeriod_Type(Integer32):
    """Custom type xldv20DbmBackupPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(12, 48),
    )


_Xldv20DbmBackupPeriod_Type.__name__ = "Integer32"
_Xldv20DbmBackupPeriod_Object = MibScalar
xldv20DbmBackupPeriod = _Xldv20DbmBackupPeriod_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 8, 1, 4),
    _Xldv20DbmBackupPeriod_Type()
)
xldv20DbmBackupPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20DbmBackupPeriod.setStatus("mandatory")


class _Xldv20DbmBackupStartTime_Type(Integer32):
    """Custom type xldv20DbmBackupStartTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_Xldv20DbmBackupStartTime_Type.__name__ = "Integer32"
_Xldv20DbmBackupStartTime_Object = MibScalar
xldv20DbmBackupStartTime = _Xldv20DbmBackupStartTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 8, 1, 5),
    _Xldv20DbmBackupStartTime_Type()
)
xldv20DbmBackupStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20DbmBackupStartTime.setStatus("mandatory")
_Xldv20DbmControlReqResultLocal_Type = Xldv20ControlReq
_Xldv20DbmControlReqResultLocal_Object = MibScalar
xldv20DbmControlReqResultLocal = _Xldv20DbmControlReqResultLocal_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 8, 1, 6),
    _Xldv20DbmControlReqResultLocal_Type()
)
xldv20DbmControlReqResultLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20DbmControlReqResultLocal.setStatus("mandatory")
_Xldv20DbmControlReqResultRemote_Type = Xldv20ControlReq
_Xldv20DbmControlReqResultRemote_Object = MibScalar
xldv20DbmControlReqResultRemote = _Xldv20DbmControlReqResultRemote_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 8, 1, 7),
    _Xldv20DbmControlReqResultRemote_Type()
)
xldv20DbmControlReqResultRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20DbmControlReqResultRemote.setStatus("mandatory")


class _Xldv20DbmPathAndFileName_Type(OctetString):
    """Custom type xldv20DbmPathAndFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 150),
    )


_Xldv20DbmPathAndFileName_Type.__name__ = "OctetString"
_Xldv20DbmPathAndFileName_Object = MibScalar
xldv20DbmPathAndFileName = _Xldv20DbmPathAndFileName_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 8, 1, 8),
    _Xldv20DbmPathAndFileName_Type()
)
xldv20DbmPathAndFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20DbmPathAndFileName.setStatus("mandatory")
_Xldv20DbmControlTimeStamp_Type = TimeTicks
_Xldv20DbmControlTimeStamp_Object = MibScalar
xldv20DbmControlTimeStamp = _Xldv20DbmControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 8, 1, 9),
    _Xldv20DbmControlTimeStamp_Type()
)
xldv20DbmControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20DbmControlTimeStamp.setStatus("mandatory")
_Xldv20TlmIma_ObjectIdentity = ObjectIdentity
xldv20TlmIma = _Xldv20TlmIma_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9)
)
_Xldv20ImaMibObjects_ObjectIdentity = ObjectIdentity
xldv20ImaMibObjects = _Xldv20ImaMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1)
)


class _Xldv20ImaGroupNumber_Type(Integer32):
    """Custom type xldv20ImaGroupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Xldv20ImaGroupNumber_Type.__name__ = "Integer32"
_Xldv20ImaGroupNumber_Object = MibScalar
xldv20ImaGroupNumber = _Xldv20ImaGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 1),
    _Xldv20ImaGroupNumber_Type()
)
xldv20ImaGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaGroupNumber.setStatus("mandatory")
_Xldv20ImaControl_ObjectIdentity = ObjectIdentity
xldv20ImaControl = _Xldv20ImaControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 2)
)
_Xldv20ImaControlReq_Type = Xldv20ControlReq
_Xldv20ImaControlReq_Object = MibScalar
xldv20ImaControlReq = _Xldv20ImaControlReq_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 2, 1),
    _Xldv20ImaControlReq_Type()
)
xldv20ImaControlReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20ImaControlReq.setStatus("mandatory")


class _Xldv20ImaControlMinNumLinks_Type(Integer32):
    """Custom type xldv20ImaControlMinNumLinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Xldv20ImaControlMinNumLinks_Type.__name__ = "Integer32"
_Xldv20ImaControlMinNumLinks_Object = MibScalar
xldv20ImaControlMinNumLinks = _Xldv20ImaControlMinNumLinks_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 2, 2),
    _Xldv20ImaControlMinNumLinks_Type()
)
xldv20ImaControlMinNumLinks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20ImaControlMinNumLinks.setStatus("mandatory")


class _Xldv20ImaControlGroupIndex_Type(Integer32):
    """Custom type xldv20ImaControlGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Xldv20ImaControlGroupIndex_Type.__name__ = "Integer32"
_Xldv20ImaControlGroupIndex_Object = MibScalar
xldv20ImaControlGroupIndex = _Xldv20ImaControlGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 2, 3),
    _Xldv20ImaControlGroupIndex_Type()
)
xldv20ImaControlGroupIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20ImaControlGroupIndex.setStatus("mandatory")
_Xldv20ImaControlReqResult_Type = Xldv20ControlReq
_Xldv20ImaControlReqResult_Object = MibScalar
xldv20ImaControlReqResult = _Xldv20ImaControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 2, 4),
    _Xldv20ImaControlReqResult_Type()
)
xldv20ImaControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaControlReqResult.setStatus("mandatory")
_Xldv20ImaControlTimeStamp_Type = TimeTicks
_Xldv20ImaControlTimeStamp_Object = MibScalar
xldv20ImaControlTimeStamp = _Xldv20ImaControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 2, 5),
    _Xldv20ImaControlTimeStamp_Type()
)
xldv20ImaControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaControlTimeStamp.setStatus("mandatory")
_Xldv20ImaControlStatus_Type = Xldv20ControlStatus
_Xldv20ImaControlStatus_Object = MibScalar
xldv20ImaControlStatus = _Xldv20ImaControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 2, 6),
    _Xldv20ImaControlStatus_Type()
)
xldv20ImaControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaControlStatus.setStatus("mandatory")
_Xldv20ImaControlTimer_Type = Unsigned32
_Xldv20ImaControlTimer_Object = MibScalar
xldv20ImaControlTimer = _Xldv20ImaControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 2, 7),
    _Xldv20ImaControlTimer_Type()
)
xldv20ImaControlTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaControlTimer.setStatus("mandatory")
_Xldv20ImaGroupTable_Object = MibTable
xldv20ImaGroupTable = _Xldv20ImaGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 3)
)
if mibBuilder.loadTexts:
    xldv20ImaGroupTable.setStatus("mandatory")
_Xldv20ImaGroupEntry_Object = MibTableRow
xldv20ImaGroupEntry = _Xldv20ImaGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 3, 1)
)
xldv20ImaGroupEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20ImaGroupIndex"),
)
if mibBuilder.loadTexts:
    xldv20ImaGroupEntry.setStatus("mandatory")


class _Xldv20ImaGroupIndex_Type(Integer32):
    """Custom type xldv20ImaGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Xldv20ImaGroupIndex_Type.__name__ = "Integer32"
_Xldv20ImaGroupIndex_Object = MibTableColumn
xldv20ImaGroupIndex = _Xldv20ImaGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 3, 1, 1),
    _Xldv20ImaGroupIndex_Type()
)
xldv20ImaGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaGroupIndex.setStatus("mandatory")
_Xldv20ImaGroupRowStatus_Type = Xldv20RowStatus
_Xldv20ImaGroupRowStatus_Object = MibTableColumn
xldv20ImaGroupRowStatus = _Xldv20ImaGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 3, 1, 2),
    _Xldv20ImaGroupRowStatus_Type()
)
xldv20ImaGroupRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaGroupRowStatus.setStatus("mandatory")
_Xldv20ImaGroupIfIndex_Type = Unsigned16
_Xldv20ImaGroupIfIndex_Object = MibTableColumn
xldv20ImaGroupIfIndex = _Xldv20ImaGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 3, 1, 3),
    _Xldv20ImaGroupIfIndex_Type()
)
xldv20ImaGroupIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaGroupIfIndex.setStatus("mandatory")
_Xldv20ImaGroupNeState_Type = Xldv20ImaGroupState
_Xldv20ImaGroupNeState_Object = MibTableColumn
xldv20ImaGroupNeState = _Xldv20ImaGroupNeState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 3, 1, 4),
    _Xldv20ImaGroupNeState_Type()
)
xldv20ImaGroupNeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaGroupNeState.setStatus("mandatory")
_Xldv20ImaGroupFeState_Type = Xldv20ImaGroupState
_Xldv20ImaGroupFeState_Object = MibTableColumn
xldv20ImaGroupFeState = _Xldv20ImaGroupFeState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 3, 1, 5),
    _Xldv20ImaGroupFeState_Type()
)
xldv20ImaGroupFeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaGroupFeState.setStatus("mandatory")
_Xldv20ImaGroupFailureStatus_Type = Xldv20ImaGroupFailureStatus
_Xldv20ImaGroupFailureStatus_Object = MibTableColumn
xldv20ImaGroupFailureStatus = _Xldv20ImaGroupFailureStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 3, 1, 6),
    _Xldv20ImaGroupFailureStatus_Type()
)
xldv20ImaGroupFailureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaGroupFailureStatus.setStatus("mandatory")
_Xldv20ImaGroupSymmetry_Type = Xldv20ImaGroupSymmetry
_Xldv20ImaGroupSymmetry_Object = MibTableColumn
xldv20ImaGroupSymmetry = _Xldv20ImaGroupSymmetry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 3, 1, 7),
    _Xldv20ImaGroupSymmetry_Type()
)
xldv20ImaGroupSymmetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaGroupSymmetry.setStatus("mandatory")


class _Xldv20ImaGroupMinNumTxLinks_Type(Integer32):
    """Custom type xldv20ImaGroupMinNumTxLinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Xldv20ImaGroupMinNumTxLinks_Type.__name__ = "Integer32"
_Xldv20ImaGroupMinNumTxLinks_Object = MibTableColumn
xldv20ImaGroupMinNumTxLinks = _Xldv20ImaGroupMinNumTxLinks_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 3, 1, 8),
    _Xldv20ImaGroupMinNumTxLinks_Type()
)
xldv20ImaGroupMinNumTxLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaGroupMinNumTxLinks.setStatus("mandatory")


class _Xldv20ImaGroupMinNumRxLinks_Type(Integer32):
    """Custom type xldv20ImaGroupMinNumRxLinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Xldv20ImaGroupMinNumRxLinks_Type.__name__ = "Integer32"
_Xldv20ImaGroupMinNumRxLinks_Object = MibTableColumn
xldv20ImaGroupMinNumRxLinks = _Xldv20ImaGroupMinNumRxLinks_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 3, 1, 9),
    _Xldv20ImaGroupMinNumRxLinks_Type()
)
xldv20ImaGroupMinNumRxLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaGroupMinNumRxLinks.setStatus("mandatory")
_Xldv20ImaGroupNeTxClkMode_Type = Xldv20ImaGroupTxClkMode
_Xldv20ImaGroupNeTxClkMode_Object = MibTableColumn
xldv20ImaGroupNeTxClkMode = _Xldv20ImaGroupNeTxClkMode_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 3, 1, 10),
    _Xldv20ImaGroupNeTxClkMode_Type()
)
xldv20ImaGroupNeTxClkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaGroupNeTxClkMode.setStatus("mandatory")
_Xldv20ImaGroupFeTxClkMode_Type = Xldv20ImaGroupTxClkMode
_Xldv20ImaGroupFeTxClkMode_Object = MibTableColumn
xldv20ImaGroupFeTxClkMode = _Xldv20ImaGroupFeTxClkMode_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 3, 1, 11),
    _Xldv20ImaGroupFeTxClkMode_Type()
)
xldv20ImaGroupFeTxClkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaGroupFeTxClkMode.setStatus("mandatory")
_Xldv20ImaGroupTxTimingRefLink_Type = Unsigned16
_Xldv20ImaGroupTxTimingRefLink_Object = MibTableColumn
xldv20ImaGroupTxTimingRefLink = _Xldv20ImaGroupTxTimingRefLink_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 3, 1, 12),
    _Xldv20ImaGroupTxTimingRefLink_Type()
)
xldv20ImaGroupTxTimingRefLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaGroupTxTimingRefLink.setStatus("mandatory")
_Xldv20ImaGroupRxTimingRefLink_Type = Unsigned16
_Xldv20ImaGroupRxTimingRefLink_Object = MibTableColumn
xldv20ImaGroupRxTimingRefLink = _Xldv20ImaGroupRxTimingRefLink_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 3, 1, 13),
    _Xldv20ImaGroupRxTimingRefLink_Type()
)
xldv20ImaGroupRxTimingRefLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaGroupRxTimingRefLink.setStatus("mandatory")
_Xldv20ImaGroupLastChange_Type = TimeTicks
_Xldv20ImaGroupLastChange_Object = MibTableColumn
xldv20ImaGroupLastChange = _Xldv20ImaGroupLastChange_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 3, 1, 14),
    _Xldv20ImaGroupLastChange_Type()
)
xldv20ImaGroupLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaGroupLastChange.setStatus("mandatory")


class _Xldv20ImaGroupTxImaId_Type(Integer32):
    """Custom type xldv20ImaGroupTxImaId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Xldv20ImaGroupTxImaId_Type.__name__ = "Integer32"
_Xldv20ImaGroupTxImaId_Object = MibTableColumn
xldv20ImaGroupTxImaId = _Xldv20ImaGroupTxImaId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 3, 1, 15),
    _Xldv20ImaGroupTxImaId_Type()
)
xldv20ImaGroupTxImaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20ImaGroupTxImaId.setStatus("mandatory")


class _Xldv20ImaGroupRxImaId_Type(Integer32):
    """Custom type xldv20ImaGroupRxImaId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Xldv20ImaGroupRxImaId_Type.__name__ = "Integer32"
_Xldv20ImaGroupRxImaId_Object = MibTableColumn
xldv20ImaGroupRxImaId = _Xldv20ImaGroupRxImaId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 3, 1, 16),
    _Xldv20ImaGroupRxImaId_Type()
)
xldv20ImaGroupRxImaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaGroupRxImaId.setStatus("mandatory")
_Xldv20ImaGroupTxFrameLength_Type = Xldv20ImaFrameLength
_Xldv20ImaGroupTxFrameLength_Object = MibTableColumn
xldv20ImaGroupTxFrameLength = _Xldv20ImaGroupTxFrameLength_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 3, 1, 17),
    _Xldv20ImaGroupTxFrameLength_Type()
)
xldv20ImaGroupTxFrameLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaGroupTxFrameLength.setStatus("mandatory")
_Xldv20ImaGroupRxFrameLength_Type = Xldv20ImaFrameLength
_Xldv20ImaGroupRxFrameLength_Object = MibTableColumn
xldv20ImaGroupRxFrameLength = _Xldv20ImaGroupRxFrameLength_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 3, 1, 18),
    _Xldv20ImaGroupRxFrameLength_Type()
)
xldv20ImaGroupRxFrameLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaGroupRxFrameLength.setStatus("mandatory")
_Xldv20ImaGroupDiffDelayMax_Type = MilliSeconds
_Xldv20ImaGroupDiffDelayMax_Object = MibTableColumn
xldv20ImaGroupDiffDelayMax = _Xldv20ImaGroupDiffDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 3, 1, 19),
    _Xldv20ImaGroupDiffDelayMax_Type()
)
xldv20ImaGroupDiffDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaGroupDiffDelayMax.setStatus("mandatory")
_Xldv20ImaGroupLeastDelayLink_Type = Unsigned16
_Xldv20ImaGroupLeastDelayLink_Object = MibTableColumn
xldv20ImaGroupLeastDelayLink = _Xldv20ImaGroupLeastDelayLink_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 3, 1, 20),
    _Xldv20ImaGroupLeastDelayLink_Type()
)
xldv20ImaGroupLeastDelayLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaGroupLeastDelayLink.setStatus("mandatory")
_Xldv20ImaGroupDiffDelayMaxObs_Type = MilliSeconds
_Xldv20ImaGroupDiffDelayMaxObs_Object = MibTableColumn
xldv20ImaGroupDiffDelayMaxObs = _Xldv20ImaGroupDiffDelayMaxObs_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 3, 1, 21),
    _Xldv20ImaGroupDiffDelayMaxObs_Type()
)
xldv20ImaGroupDiffDelayMaxObs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaGroupDiffDelayMaxObs.setStatus("mandatory")


class _Xldv20ImaGroupAlphaValue_Type(Integer32):
    """Custom type xldv20ImaGroupAlphaValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Xldv20ImaGroupAlphaValue_Type.__name__ = "Integer32"
_Xldv20ImaGroupAlphaValue_Object = MibTableColumn
xldv20ImaGroupAlphaValue = _Xldv20ImaGroupAlphaValue_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 3, 1, 22),
    _Xldv20ImaGroupAlphaValue_Type()
)
xldv20ImaGroupAlphaValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaGroupAlphaValue.setStatus("mandatory")


class _Xldv20ImaGroupBetaValue_Type(Integer32):
    """Custom type xldv20ImaGroupBetaValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Xldv20ImaGroupBetaValue_Type.__name__ = "Integer32"
_Xldv20ImaGroupBetaValue_Object = MibTableColumn
xldv20ImaGroupBetaValue = _Xldv20ImaGroupBetaValue_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 3, 1, 23),
    _Xldv20ImaGroupBetaValue_Type()
)
xldv20ImaGroupBetaValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaGroupBetaValue.setStatus("mandatory")


class _Xldv20ImaGroupGammaValue_Type(Integer32):
    """Custom type xldv20ImaGroupGammaValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Xldv20ImaGroupGammaValue_Type.__name__ = "Integer32"
_Xldv20ImaGroupGammaValue_Object = MibTableColumn
xldv20ImaGroupGammaValue = _Xldv20ImaGroupGammaValue_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 3, 1, 24),
    _Xldv20ImaGroupGammaValue_Type()
)
xldv20ImaGroupGammaValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaGroupGammaValue.setStatus("mandatory")
_Xldv20ImaGroupRunningSecs_Type = Gauge32
_Xldv20ImaGroupRunningSecs_Object = MibTableColumn
xldv20ImaGroupRunningSecs = _Xldv20ImaGroupRunningSecs_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 3, 1, 25),
    _Xldv20ImaGroupRunningSecs_Type()
)
xldv20ImaGroupRunningSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaGroupRunningSecs.setStatus("mandatory")
_Xldv20ImaGroupUnavailSecs_Type = Counter32
_Xldv20ImaGroupUnavailSecs_Object = MibTableColumn
xldv20ImaGroupUnavailSecs = _Xldv20ImaGroupUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 3, 1, 26),
    _Xldv20ImaGroupUnavailSecs_Type()
)
xldv20ImaGroupUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaGroupUnavailSecs.setStatus("mandatory")
_Xldv20ImaGroupNeNumFailures_Type = Counter32
_Xldv20ImaGroupNeNumFailures_Object = MibTableColumn
xldv20ImaGroupNeNumFailures = _Xldv20ImaGroupNeNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 3, 1, 27),
    _Xldv20ImaGroupNeNumFailures_Type()
)
xldv20ImaGroupNeNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaGroupNeNumFailures.setStatus("mandatory")
_Xldv20ImaGroupFeNumFailures_Type = Counter32
_Xldv20ImaGroupFeNumFailures_Object = MibTableColumn
xldv20ImaGroupFeNumFailures = _Xldv20ImaGroupFeNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 3, 1, 28),
    _Xldv20ImaGroupFeNumFailures_Type()
)
xldv20ImaGroupFeNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaGroupFeNumFailures.setStatus("mandatory")
_Xldv20ImaGroupNumTxCfgLinks_Type = Gauge32
_Xldv20ImaGroupNumTxCfgLinks_Object = MibTableColumn
xldv20ImaGroupNumTxCfgLinks = _Xldv20ImaGroupNumTxCfgLinks_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 3, 1, 29),
    _Xldv20ImaGroupNumTxCfgLinks_Type()
)
xldv20ImaGroupNumTxCfgLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaGroupNumTxCfgLinks.setStatus("mandatory")
_Xldv20ImaGroupNumRxCfgLinks_Type = Gauge32
_Xldv20ImaGroupNumRxCfgLinks_Object = MibTableColumn
xldv20ImaGroupNumRxCfgLinks = _Xldv20ImaGroupNumRxCfgLinks_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 3, 1, 30),
    _Xldv20ImaGroupNumRxCfgLinks_Type()
)
xldv20ImaGroupNumRxCfgLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaGroupNumRxCfgLinks.setStatus("mandatory")
_Xldv20ImaGroupNumTxActLinks_Type = Gauge32
_Xldv20ImaGroupNumTxActLinks_Object = MibTableColumn
xldv20ImaGroupNumTxActLinks = _Xldv20ImaGroupNumTxActLinks_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 3, 1, 31),
    _Xldv20ImaGroupNumTxActLinks_Type()
)
xldv20ImaGroupNumTxActLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaGroupNumTxActLinks.setStatus("mandatory")
_Xldv20ImaGroupNumRxActLinks_Type = Gauge32
_Xldv20ImaGroupNumRxActLinks_Object = MibTableColumn
xldv20ImaGroupNumRxActLinks = _Xldv20ImaGroupNumRxActLinks_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 3, 1, 32),
    _Xldv20ImaGroupNumRxActLinks_Type()
)
xldv20ImaGroupNumRxActLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaGroupNumRxActLinks.setStatus("mandatory")


class _Xldv20ImaGroupBandwidthUsage_Type(Integer32):
    """Custom type xldv20ImaGroupBandwidthUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Xldv20ImaGroupBandwidthUsage_Type.__name__ = "Integer32"
_Xldv20ImaGroupBandwidthUsage_Object = MibTableColumn
xldv20ImaGroupBandwidthUsage = _Xldv20ImaGroupBandwidthUsage_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 3, 1, 33),
    _Xldv20ImaGroupBandwidthUsage_Type()
)
xldv20ImaGroupBandwidthUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaGroupBandwidthUsage.setStatus("mandatory")
_Xldv20ImaGroupMappingTable_Object = MibTable
xldv20ImaGroupMappingTable = _Xldv20ImaGroupMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 4)
)
if mibBuilder.loadTexts:
    xldv20ImaGroupMappingTable.setStatus("mandatory")
_Xldv20ImaGroupMappingEntry_Object = MibTableRow
xldv20ImaGroupMappingEntry = _Xldv20ImaGroupMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 4, 1)
)
xldv20ImaGroupMappingEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20IfIndex"),
)
if mibBuilder.loadTexts:
    xldv20ImaGroupMappingEntry.setStatus("mandatory")
_Xldv20ImaGroupMappingIndex_Type = Unsigned32
_Xldv20ImaGroupMappingIndex_Object = MibTableColumn
xldv20ImaGroupMappingIndex = _Xldv20ImaGroupMappingIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 4, 1, 1),
    _Xldv20ImaGroupMappingIndex_Type()
)
xldv20ImaGroupMappingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaGroupMappingIndex.setStatus("mandatory")
_Xldv20ImaLinkTable_Object = MibTable
xldv20ImaLinkTable = _Xldv20ImaLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 5)
)
if mibBuilder.loadTexts:
    xldv20ImaLinkTable.setStatus("mandatory")
_Xldv20ImaLinkEntry_Object = MibTableRow
xldv20ImaLinkEntry = _Xldv20ImaLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 5, 1)
)
xldv20ImaLinkEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20IfIndex"),
)
if mibBuilder.loadTexts:
    xldv20ImaLinkEntry.setStatus("mandatory")
_Xldv20ImaLinkRowStatus_Type = Xldv20RowStatus
_Xldv20ImaLinkRowStatus_Object = MibTableColumn
xldv20ImaLinkRowStatus = _Xldv20ImaLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 5, 1, 1),
    _Xldv20ImaLinkRowStatus_Type()
)
xldv20ImaLinkRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaLinkRowStatus.setStatus("mandatory")
_Xldv20ImaLinkGroupIndex_Type = Integer32
_Xldv20ImaLinkGroupIndex_Object = MibTableColumn
xldv20ImaLinkGroupIndex = _Xldv20ImaLinkGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 5, 1, 2),
    _Xldv20ImaLinkGroupIndex_Type()
)
xldv20ImaLinkGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaLinkGroupIndex.setStatus("mandatory")
_Xldv20ImaLinkNeTxState_Type = Xldv20ImaLinkState
_Xldv20ImaLinkNeTxState_Object = MibTableColumn
xldv20ImaLinkNeTxState = _Xldv20ImaLinkNeTxState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 5, 1, 3),
    _Xldv20ImaLinkNeTxState_Type()
)
xldv20ImaLinkNeTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaLinkNeTxState.setStatus("mandatory")
_Xldv20ImaLinkNeRxState_Type = Xldv20ImaLinkState
_Xldv20ImaLinkNeRxState_Object = MibTableColumn
xldv20ImaLinkNeRxState = _Xldv20ImaLinkNeRxState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 5, 1, 4),
    _Xldv20ImaLinkNeRxState_Type()
)
xldv20ImaLinkNeRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaLinkNeRxState.setStatus("mandatory")
_Xldv20ImaLinkFeTxState_Type = Xldv20ImaLinkState
_Xldv20ImaLinkFeTxState_Object = MibTableColumn
xldv20ImaLinkFeTxState = _Xldv20ImaLinkFeTxState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 5, 1, 5),
    _Xldv20ImaLinkFeTxState_Type()
)
xldv20ImaLinkFeTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaLinkFeTxState.setStatus("mandatory")
_Xldv20ImaLinkFeRxState_Type = Xldv20ImaLinkState
_Xldv20ImaLinkFeRxState_Object = MibTableColumn
xldv20ImaLinkFeRxState = _Xldv20ImaLinkFeRxState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 5, 1, 6),
    _Xldv20ImaLinkFeRxState_Type()
)
xldv20ImaLinkFeRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaLinkFeRxState.setStatus("mandatory")
_Xldv20ImaLinkNeRxFailureStatus_Type = Xldv20ImaLinkFailureStatus
_Xldv20ImaLinkNeRxFailureStatus_Object = MibTableColumn
xldv20ImaLinkNeRxFailureStatus = _Xldv20ImaLinkNeRxFailureStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 5, 1, 7),
    _Xldv20ImaLinkNeRxFailureStatus_Type()
)
xldv20ImaLinkNeRxFailureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaLinkNeRxFailureStatus.setStatus("mandatory")
_Xldv20ImaLinkFeRxFailureStatus_Type = Xldv20ImaLinkFailureStatus
_Xldv20ImaLinkFeRxFailureStatus_Object = MibTableColumn
xldv20ImaLinkFeRxFailureStatus = _Xldv20ImaLinkFeRxFailureStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 5, 1, 8),
    _Xldv20ImaLinkFeRxFailureStatus_Type()
)
xldv20ImaLinkFeRxFailureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaLinkFeRxFailureStatus.setStatus("mandatory")


class _Xldv20ImaLinkTxLid_Type(Integer32):
    """Custom type xldv20ImaLinkTxLid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Xldv20ImaLinkTxLid_Type.__name__ = "Integer32"
_Xldv20ImaLinkTxLid_Object = MibTableColumn
xldv20ImaLinkTxLid = _Xldv20ImaLinkTxLid_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 5, 1, 9),
    _Xldv20ImaLinkTxLid_Type()
)
xldv20ImaLinkTxLid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaLinkTxLid.setStatus("mandatory")


class _Xldv20ImaLinkRxLid_Type(Integer32):
    """Custom type xldv20ImaLinkRxLid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Xldv20ImaLinkRxLid_Type.__name__ = "Integer32"
_Xldv20ImaLinkRxLid_Object = MibTableColumn
xldv20ImaLinkRxLid = _Xldv20ImaLinkRxLid_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 5, 1, 10),
    _Xldv20ImaLinkRxLid_Type()
)
xldv20ImaLinkRxLid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaLinkRxLid.setStatus("mandatory")
_Xldv20ImaLinkImaViolations_Type = Counter32
_Xldv20ImaLinkImaViolations_Object = MibTableColumn
xldv20ImaLinkImaViolations = _Xldv20ImaLinkImaViolations_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 5, 1, 11),
    _Xldv20ImaLinkImaViolations_Type()
)
xldv20ImaLinkImaViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaLinkImaViolations.setStatus("mandatory")
_Xldv20ImaLinkOifAnomalies_Type = Counter32
_Xldv20ImaLinkOifAnomalies_Object = MibTableColumn
xldv20ImaLinkOifAnomalies = _Xldv20ImaLinkOifAnomalies_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 5, 1, 12),
    _Xldv20ImaLinkOifAnomalies_Type()
)
xldv20ImaLinkOifAnomalies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaLinkOifAnomalies.setStatus("mandatory")
_Xldv20ImaLinkNeSevErroredSecs_Type = Counter32
_Xldv20ImaLinkNeSevErroredSecs_Object = MibTableColumn
xldv20ImaLinkNeSevErroredSecs = _Xldv20ImaLinkNeSevErroredSecs_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 5, 1, 13),
    _Xldv20ImaLinkNeSevErroredSecs_Type()
)
xldv20ImaLinkNeSevErroredSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaLinkNeSevErroredSecs.setStatus("mandatory")
_Xldv20ImaLinkFeSevErroredSecs_Type = Counter32
_Xldv20ImaLinkFeSevErroredSecs_Object = MibTableColumn
xldv20ImaLinkFeSevErroredSecs = _Xldv20ImaLinkFeSevErroredSecs_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 5, 1, 14),
    _Xldv20ImaLinkFeSevErroredSecs_Type()
)
xldv20ImaLinkFeSevErroredSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaLinkFeSevErroredSecs.setStatus("mandatory")
_Xldv20ImaLinkNeUnavailSecs_Type = Counter32
_Xldv20ImaLinkNeUnavailSecs_Object = MibTableColumn
xldv20ImaLinkNeUnavailSecs = _Xldv20ImaLinkNeUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 5, 1, 15),
    _Xldv20ImaLinkNeUnavailSecs_Type()
)
xldv20ImaLinkNeUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaLinkNeUnavailSecs.setStatus("mandatory")
_Xldv20ImaLinkFeUnavailSecs_Type = Counter32
_Xldv20ImaLinkFeUnavailSecs_Object = MibTableColumn
xldv20ImaLinkFeUnavailSecs = _Xldv20ImaLinkFeUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 5, 1, 16),
    _Xldv20ImaLinkFeUnavailSecs_Type()
)
xldv20ImaLinkFeUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaLinkFeUnavailSecs.setStatus("mandatory")
_Xldv20ImaLinkNeTxUnusableSecs_Type = Counter32
_Xldv20ImaLinkNeTxUnusableSecs_Object = MibTableColumn
xldv20ImaLinkNeTxUnusableSecs = _Xldv20ImaLinkNeTxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 5, 1, 17),
    _Xldv20ImaLinkNeTxUnusableSecs_Type()
)
xldv20ImaLinkNeTxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaLinkNeTxUnusableSecs.setStatus("mandatory")
_Xldv20ImaLinkNeRxUnusableSecs_Type = Counter32
_Xldv20ImaLinkNeRxUnusableSecs_Object = MibTableColumn
xldv20ImaLinkNeRxUnusableSecs = _Xldv20ImaLinkNeRxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 5, 1, 18),
    _Xldv20ImaLinkNeRxUnusableSecs_Type()
)
xldv20ImaLinkNeRxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaLinkNeRxUnusableSecs.setStatus("mandatory")
_Xldv20ImaLinkFeTxUnusableSecs_Type = Counter32
_Xldv20ImaLinkFeTxUnusableSecs_Object = MibTableColumn
xldv20ImaLinkFeTxUnusableSecs = _Xldv20ImaLinkFeTxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 5, 1, 19),
    _Xldv20ImaLinkFeTxUnusableSecs_Type()
)
xldv20ImaLinkFeTxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaLinkFeTxUnusableSecs.setStatus("mandatory")
_Xldv20ImaLinkFeRxUnusableSecs_Type = Counter32
_Xldv20ImaLinkFeRxUnusableSecs_Object = MibTableColumn
xldv20ImaLinkFeRxUnusableSecs = _Xldv20ImaLinkFeRxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 5, 1, 20),
    _Xldv20ImaLinkFeRxUnusableSecs_Type()
)
xldv20ImaLinkFeRxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaLinkFeRxUnusableSecs.setStatus("mandatory")
_Xldv20ImaLinkNeTxNumFailures_Type = Counter32
_Xldv20ImaLinkNeTxNumFailures_Object = MibTableColumn
xldv20ImaLinkNeTxNumFailures = _Xldv20ImaLinkNeTxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 5, 1, 21),
    _Xldv20ImaLinkNeTxNumFailures_Type()
)
xldv20ImaLinkNeTxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaLinkNeTxNumFailures.setStatus("mandatory")
_Xldv20ImaLinkNeRxNumFailures_Type = Counter32
_Xldv20ImaLinkNeRxNumFailures_Object = MibTableColumn
xldv20ImaLinkNeRxNumFailures = _Xldv20ImaLinkNeRxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 5, 1, 22),
    _Xldv20ImaLinkNeRxNumFailures_Type()
)
xldv20ImaLinkNeRxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaLinkNeRxNumFailures.setStatus("mandatory")
_Xldv20ImaLinkFeTxNumFailures_Type = Counter32
_Xldv20ImaLinkFeTxNumFailures_Object = MibTableColumn
xldv20ImaLinkFeTxNumFailures = _Xldv20ImaLinkFeTxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 5, 1, 23),
    _Xldv20ImaLinkFeTxNumFailures_Type()
)
xldv20ImaLinkFeTxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaLinkFeTxNumFailures.setStatus("mandatory")
_Xldv20ImaLinkFeRxNumFailures_Type = Counter32
_Xldv20ImaLinkFeRxNumFailures_Object = MibTableColumn
xldv20ImaLinkFeRxNumFailures = _Xldv20ImaLinkFeRxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 5, 1, 24),
    _Xldv20ImaLinkFeRxNumFailures_Type()
)
xldv20ImaLinkFeRxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaLinkFeRxNumFailures.setStatus("mandatory")
_Xldv20ImaLinkTxStuffs_Type = Counter32
_Xldv20ImaLinkTxStuffs_Object = MibTableColumn
xldv20ImaLinkTxStuffs = _Xldv20ImaLinkTxStuffs_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 5, 1, 25),
    _Xldv20ImaLinkTxStuffs_Type()
)
xldv20ImaLinkTxStuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaLinkTxStuffs.setStatus("mandatory")
_Xldv20ImaLinkRxStuffs_Type = Counter32
_Xldv20ImaLinkRxStuffs_Object = MibTableColumn
xldv20ImaLinkRxStuffs = _Xldv20ImaLinkRxStuffs_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 9, 1, 5, 1, 26),
    _Xldv20ImaLinkRxStuffs_Type()
)
xldv20ImaLinkRxStuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20ImaLinkRxStuffs.setStatus("mandatory")
_Xldv20Traps_ObjectIdentity = ObjectIdentity
xldv20Traps = _Xldv20Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10)
)
_Xldv20TrapVars_ObjectIdentity = ObjectIdentity
xldv20TrapVars = _Xldv20TrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1)
)
_Xldv20TvStartupResult_Type = Xldv20StartupResult
_Xldv20TvStartupResult_Object = MibScalar
xldv20TvStartupResult = _Xldv20TvStartupResult_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 1),
    _Xldv20TvStartupResult_Type()
)
xldv20TvStartupResult.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvStartupResult.setStatus("mandatory")
_Xldv20TvStartupType_Type = Xldv20StartupType
_Xldv20TvStartupType_Object = MibScalar
xldv20TvStartupType = _Xldv20TvStartupType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 2),
    _Xldv20TvStartupType_Type()
)
xldv20TvStartupType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvStartupType.setStatus("mandatory")
_Xldv20TvSnmLctSession_Type = Xldv20SnmLctSession
_Xldv20TvSnmLctSession_Object = MibScalar
xldv20TvSnmLctSession = _Xldv20TvSnmLctSession_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 3),
    _Xldv20TvSnmLctSession_Type()
)
xldv20TvSnmLctSession.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvSnmLctSession.setStatus("mandatory")
_Xldv20TvRepEntity_Type = Unsigned16
_Xldv20TvRepEntity_Object = MibScalar
xldv20TvRepEntity = _Xldv20TvRepEntity_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 4),
    _Xldv20TvRepEntity_Type()
)
xldv20TvRepEntity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvRepEntity.setStatus("mandatory")
_Xldv20TvRepSource_Type = Xldv20RepSource
_Xldv20TvRepSource_Object = MibScalar
xldv20TvRepSource = _Xldv20TvRepSource_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 5),
    _Xldv20TvRepSource_Type()
)
xldv20TvRepSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvRepSource.setStatus("mandatory")
_Xldv20TvTimeAndDate_Type = Integer32
_Xldv20TvTimeAndDate_Object = MibScalar
xldv20TvTimeAndDate = _Xldv20TvTimeAndDate_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 6),
    _Xldv20TvTimeAndDate_Type()
)
xldv20TvTimeAndDate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvTimeAndDate.setStatus("mandatory")


class _Xldv20TvActCcReloadResult_Type(Integer32):
    """Custom type xldv20TvActCcReloadResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lineIndexFaulty", 3),
          ("notOk", 2),
          ("ok", 1))
    )


_Xldv20TvActCcReloadResult_Type.__name__ = "Integer32"
_Xldv20TvActCcReloadResult_Object = MibScalar
xldv20TvActCcReloadResult = _Xldv20TvActCcReloadResult_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 7),
    _Xldv20TvActCcReloadResult_Type()
)
xldv20TvActCcReloadResult.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvActCcReloadResult.setStatus("mandatory")
_Xldv20TvActCcStatus_Type = Integer32
_Xldv20TvActCcStatus_Object = MibScalar
xldv20TvActCcStatus = _Xldv20TvActCcStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 8),
    _Xldv20TvActCcStatus_Type()
)
xldv20TvActCcStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvActCcStatus.setStatus("mandatory")
_Xldv20TvAlmNatureOfAlarm_Type = Xldv20TrapIds
_Xldv20TvAlmNatureOfAlarm_Object = MibScalar
xldv20TvAlmNatureOfAlarm = _Xldv20TvAlmNatureOfAlarm_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 9),
    _Xldv20TvAlmNatureOfAlarm_Type()
)
xldv20TvAlmNatureOfAlarm.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvAlmNatureOfAlarm.setStatus("mandatory")
_Xldv20TvAlmSpecProblem_Type = Integer32
_Xldv20TvAlmSpecProblem_Object = MibScalar
xldv20TvAlmSpecProblem = _Xldv20TvAlmSpecProblem_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 10),
    _Xldv20TvAlmSpecProblem_Type()
)
xldv20TvAlmSpecProblem.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvAlmSpecProblem.setStatus("mandatory")
_Xldv20TvAlmFailedComponent_Type = Integer32
_Xldv20TvAlmFailedComponent_Object = MibScalar
xldv20TvAlmFailedComponent = _Xldv20TvAlmFailedComponent_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 11),
    _Xldv20TvAlmFailedComponent_Type()
)
xldv20TvAlmFailedComponent.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvAlmFailedComponent.setStatus("mandatory")
_Xldv20TvAlmSeverityOfFailure_Type = Xldv20AlarmSeverity
_Xldv20TvAlmSeverityOfFailure_Object = MibScalar
xldv20TvAlmSeverityOfFailure = _Xldv20TvAlmSeverityOfFailure_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 12),
    _Xldv20TvAlmSeverityOfFailure_Type()
)
xldv20TvAlmSeverityOfFailure.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvAlmSeverityOfFailure.setStatus("mandatory")


class _Xldv20TvAlmStatus_Type(Integer32):
    """Custom type xldv20TvAlmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("present", 0))
    )


_Xldv20TvAlmStatus_Type.__name__ = "Integer32"
_Xldv20TvAlmStatus_Object = MibScalar
xldv20TvAlmStatus = _Xldv20TvAlmStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 13),
    _Xldv20TvAlmStatus_Type()
)
xldv20TvAlmStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvAlmStatus.setStatus("mandatory")
_Xldv20TvAlmPropRepairAction_Type = Integer32
_Xldv20TvAlmPropRepairAction_Object = MibScalar
xldv20TvAlmPropRepairAction = _Xldv20TvAlmPropRepairAction_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 14),
    _Xldv20TvAlmPropRepairAction_Type()
)
xldv20TvAlmPropRepairAction.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvAlmPropRepairAction.setStatus("mandatory")
_Xldv20TvAlmFailedComponentRepSource_Type = Xldv20RepSource
_Xldv20TvAlmFailedComponentRepSource_Object = MibScalar
xldv20TvAlmFailedComponentRepSource = _Xldv20TvAlmFailedComponentRepSource_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 15),
    _Xldv20TvAlmFailedComponentRepSource_Type()
)
xldv20TvAlmFailedComponentRepSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvAlmFailedComponentRepSource.setStatus("mandatory")
_Xldv20TvStcOldAdminStatus_Type = Xldv20AdminState
_Xldv20TvStcOldAdminStatus_Object = MibScalar
xldv20TvStcOldAdminStatus = _Xldv20TvStcOldAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 16),
    _Xldv20TvStcOldAdminStatus_Type()
)
xldv20TvStcOldAdminStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvStcOldAdminStatus.setStatus("mandatory")
_Xldv20TvStcNewAdminStatus_Type = Xldv20AdminState
_Xldv20TvStcNewAdminStatus_Object = MibScalar
xldv20TvStcNewAdminStatus = _Xldv20TvStcNewAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 17),
    _Xldv20TvStcNewAdminStatus_Type()
)
xldv20TvStcNewAdminStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvStcNewAdminStatus.setStatus("mandatory")
_Xldv20TvStcOldOperStatus_Type = Xldv20OperState
_Xldv20TvStcOldOperStatus_Object = MibScalar
xldv20TvStcOldOperStatus = _Xldv20TvStcOldOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 18),
    _Xldv20TvStcOldOperStatus_Type()
)
xldv20TvStcOldOperStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvStcOldOperStatus.setStatus("mandatory")
_Xldv20TvStcNewOperStatus_Type = Xldv20OperState
_Xldv20TvStcNewOperStatus_Object = MibScalar
xldv20TvStcNewOperStatus = _Xldv20TvStcNewOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 19),
    _Xldv20TvStcNewOperStatus_Type()
)
xldv20TvStcNewOperStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvStcNewOperStatus.setStatus("mandatory")
_Xldv20TvTsrControlStatus_Type = Xldv20ControlStatus
_Xldv20TvTsrControlStatus_Object = MibScalar
xldv20TvTsrControlStatus = _Xldv20TvTsrControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 20),
    _Xldv20TvTsrControlStatus_Type()
)
xldv20TvTsrControlStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvTsrControlStatus.setStatus("mandatory")
_Xldv20TvRstResult_Type = Xldv20RstResult
_Xldv20TvRstResult_Object = MibScalar
xldv20TvRstResult = _Xldv20TvRstResult_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 21),
    _Xldv20TvRstResult_Type()
)
xldv20TvRstResult.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvRstResult.setStatus("mandatory")
_Xldv20TvRstHwUnitIndex_Type = Unsigned16
_Xldv20TvRstHwUnitIndex_Object = MibScalar
xldv20TvRstHwUnitIndex = _Xldv20TvRstHwUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 22),
    _Xldv20TvRstHwUnitIndex_Type()
)
xldv20TvRstHwUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvRstHwUnitIndex.setStatus("mandatory")
_Xldv20TvHweResetType_Type = Xldv20StartupType
_Xldv20TvHweResetType_Object = MibScalar
xldv20TvHweResetType = _Xldv20TvHweResetType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 23),
    _Xldv20TvHweResetType_Type()
)
xldv20TvHweResetType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvHweResetType.setStatus("mandatory")
_Xldv20TvAdcControlStatus_Type = Integer32
_Xldv20TvAdcControlStatus_Object = MibScalar
xldv20TvAdcControlStatus = _Xldv20TvAdcControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 24),
    _Xldv20TvAdcControlStatus_Type()
)
xldv20TvAdcControlStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvAdcControlStatus.setStatus("mandatory")
_Xldv20TvSucResult_Type = Xldv20ControlReq
_Xldv20TvSucResult_Object = MibScalar
xldv20TvSucResult = _Xldv20TvSucResult_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 25),
    _Xldv20TvSucResult_Type()
)
xldv20TvSucResult.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvSucResult.setStatus("mandatory")


class _Xldv20TvSucUnit_Type(DisplayString):
    """Custom type xldv20TvSucUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Xldv20TvSucUnit_Type.__name__ = "DisplayString"
_Xldv20TvSucUnit_Object = MibScalar
xldv20TvSucUnit = _Xldv20TvSucUnit_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 26),
    _Xldv20TvSucUnit_Type()
)
xldv20TvSucUnit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvSucUnit.setStatus("mandatory")
_Xldv20TvSucHwUnitIndex_Type = Unsigned16
_Xldv20TvSucHwUnitIndex_Object = MibScalar
xldv20TvSucHwUnitIndex = _Xldv20TvSucHwUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 27),
    _Xldv20TvSucHwUnitIndex_Type()
)
xldv20TvSucHwUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvSucHwUnitIndex.setStatus("mandatory")


class _Xldv20TvSucVersionNo_Type(DisplayString):
    """Custom type xldv20TvSucVersionNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Xldv20TvSucVersionNo_Type.__name__ = "DisplayString"
_Xldv20TvSucVersionNo_Object = MibScalar
xldv20TvSucVersionNo = _Xldv20TvSucVersionNo_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 28),
    _Xldv20TvSucVersionNo_Type()
)
xldv20TvSucVersionNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvSucVersionNo.setStatus("mandatory")


class _Xldv20TvSucPathName_Type(DisplayString):
    """Custom type xldv20TvSucPathName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 150),
    )


_Xldv20TvSucPathName_Type.__name__ = "DisplayString"
_Xldv20TvSucPathName_Object = MibScalar
xldv20TvSucPathName = _Xldv20TvSucPathName_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 29),
    _Xldv20TvSucPathName_Type()
)
xldv20TvSucPathName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvSucPathName.setStatus("mandatory")


class _Xldv20TvSucFileName_Type(DisplayString):
    """Custom type xldv20TvSucFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_Xldv20TvSucFileName_Type.__name__ = "DisplayString"
_Xldv20TvSucFileName_Object = MibScalar
xldv20TvSucFileName = _Xldv20TvSucFileName_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 30),
    _Xldv20TvSucFileName_Type()
)
xldv20TvSucFileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvSucFileName.setStatus("mandatory")
_Xldv20TvDbuSweLogReadResult_Type = Xldv20DbuReadStatus
_Xldv20TvDbuSweLogReadResult_Object = MibScalar
xldv20TvDbuSweLogReadResult = _Xldv20TvDbuSweLogReadResult_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 31),
    _Xldv20TvDbuSweLogReadResult_Type()
)
xldv20TvDbuSweLogReadResult.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvDbuSweLogReadResult.setStatus("mandatory")
_Xldv20TvDbuHwmLogReadResult_Type = Xldv20DbuReadStatus
_Xldv20TvDbuHwmLogReadResult_Object = MibScalar
xldv20TvDbuHwmLogReadResult = _Xldv20TvDbuHwmLogReadResult_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 32),
    _Xldv20TvDbuHwmLogReadResult_Type()
)
xldv20TvDbuHwmLogReadResult.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvDbuHwmLogReadResult.setStatus("mandatory")
_Xldv20TvDbuSwTraceLogReadResult_Type = Xldv20DbuReadStatus
_Xldv20TvDbuSwTraceLogReadResult_Object = MibScalar
xldv20TvDbuSwTraceLogReadResult = _Xldv20TvDbuSwTraceLogReadResult_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 33),
    _Xldv20TvDbuSwTraceLogReadResult_Type()
)
xldv20TvDbuSwTraceLogReadResult.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvDbuSwTraceLogReadResult.setStatus("mandatory")
_Xldv20TvHwUnitType_Type = Xldv20HwUnitType
_Xldv20TvHwUnitType_Object = MibScalar
xldv20TvHwUnitType = _Xldv20TvHwUnitType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 34),
    _Xldv20TvHwUnitType_Type()
)
xldv20TvHwUnitType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvHwUnitType.setStatus("mandatory")
_Xldv20TvHwContainingUnitIndex_Type = Unsigned16
_Xldv20TvHwContainingUnitIndex_Object = MibScalar
xldv20TvHwContainingUnitIndex = _Xldv20TvHwContainingUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 35),
    _Xldv20TvHwContainingUnitIndex_Type()
)
xldv20TvHwContainingUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvHwContainingUnitIndex.setStatus("mandatory")


class _Xldv20TvHwContainedUnitAddr_Type(Integer32):
    """Custom type xldv20TvHwContainedUnitAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_Xldv20TvHwContainedUnitAddr_Type.__name__ = "Integer32"
_Xldv20TvHwContainedUnitAddr_Object = MibScalar
xldv20TvHwContainedUnitAddr = _Xldv20TvHwContainedUnitAddr_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 36),
    _Xldv20TvHwContainedUnitAddr_Type()
)
xldv20TvHwContainedUnitAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvHwContainedUnitAddr.setStatus("mandatory")
_Xldv20TvHwuControlResult_Type = Xldv20ControlReq
_Xldv20TvHwuControlResult_Object = MibScalar
xldv20TvHwuControlResult = _Xldv20TvHwuControlResult_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 37),
    _Xldv20TvHwuControlResult_Type()
)
xldv20TvHwuControlResult.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvHwuControlResult.setStatus("mandatory")
_Xldv20TvRiRemInvResult_Type = Xldv20RiResultType
_Xldv20TvRiRemInvResult_Object = MibScalar
xldv20TvRiRemInvResult = _Xldv20TvRiRemInvResult_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 38),
    _Xldv20TvRiRemInvResult_Type()
)
xldv20TvRiRemInvResult.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvRiRemInvResult.setStatus("mandatory")


class _Xldv20TvVersionNrCmuLoad_Type(DisplayString):
    """Custom type xldv20TvVersionNrCmuLoad based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Xldv20TvVersionNrCmuLoad_Type.__name__ = "DisplayString"
_Xldv20TvVersionNrCmuLoad_Object = MibScalar
xldv20TvVersionNrCmuLoad = _Xldv20TvVersionNrCmuLoad_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 39),
    _Xldv20TvVersionNrCmuLoad_Type()
)
xldv20TvVersionNrCmuLoad.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvVersionNrCmuLoad.setStatus("mandatory")
_Xldv20TvBackupResult_Type = Xldv20ControlReq
_Xldv20TvBackupResult_Object = MibScalar
xldv20TvBackupResult = _Xldv20TvBackupResult_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 40),
    _Xldv20TvBackupResult_Type()
)
xldv20TvBackupResult.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvBackupResult.setStatus("mandatory")
_Xldv20TvVpiNni_Type = Integer32
_Xldv20TvVpiNni_Object = MibScalar
xldv20TvVpiNni = _Xldv20TvVpiNni_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 41),
    _Xldv20TvVpiNni_Type()
)
xldv20TvVpiNni.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvVpiNni.setStatus("mandatory")
_Xldv20TvVpiNniIndex_Type = Unsigned16
_Xldv20TvVpiNniIndex_Object = MibScalar
xldv20TvVpiNniIndex = _Xldv20TvVpiNniIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 42),
    _Xldv20TvVpiNniIndex_Type()
)
xldv20TvVpiNniIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvVpiNniIndex.setStatus("mandatory")
_Xldv20TvVplTerminationPointA_Type = Integer32
_Xldv20TvVplTerminationPointA_Object = MibScalar
xldv20TvVplTerminationPointA = _Xldv20TvVplTerminationPointA_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 43),
    _Xldv20TvVplTerminationPointA_Type()
)
xldv20TvVplTerminationPointA.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvVplTerminationPointA.setStatus("mandatory")
_Xldv20TvVplTerminationPointZ_Type = Integer32
_Xldv20TvVplTerminationPointZ_Object = MibScalar
xldv20TvVplTerminationPointZ = _Xldv20TvVplTerminationPointZ_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 44),
    _Xldv20TvVplTerminationPointZ_Type()
)
xldv20TvVplTerminationPointZ.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvVplTerminationPointZ.setStatus("mandatory")


class _Xldv20TvSnmMibVersion_Type(DisplayString):
    """Custom type xldv20TvSnmMibVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Xldv20TvSnmMibVersion_Type.__name__ = "DisplayString"
_Xldv20TvSnmMibVersion_Object = MibScalar
xldv20TvSnmMibVersion = _Xldv20TvSnmMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 47),
    _Xldv20TvSnmMibVersion_Type()
)
xldv20TvSnmMibVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvSnmMibVersion.setStatus("mandatory")


class _Xldv20TvSnmAgentVersion_Type(DisplayString):
    """Custom type xldv20TvSnmAgentVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Xldv20TvSnmAgentVersion_Type.__name__ = "DisplayString"
_Xldv20TvSnmAgentVersion_Object = MibScalar
xldv20TvSnmAgentVersion = _Xldv20TvSnmAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 48),
    _Xldv20TvSnmAgentVersion_Type()
)
xldv20TvSnmAgentVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvSnmAgentVersion.setStatus("mandatory")
_Xldv20TvVciNni_Type = Integer32
_Xldv20TvVciNni_Object = MibScalar
xldv20TvVciNni = _Xldv20TvVciNni_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 49),
    _Xldv20TvVciNni_Type()
)
xldv20TvVciNni.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvVciNni.setStatus("mandatory")
_Xldv20TvVciNniIndex_Type = Unsigned16
_Xldv20TvVciNniIndex_Object = MibScalar
xldv20TvVciNniIndex = _Xldv20TvVciNniIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 50),
    _Xldv20TvVciNniIndex_Type()
)
xldv20TvVciNniIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvVciNniIndex.setStatus("mandatory")
_Xldv20TvVclTerminationPointA_Type = Integer32
_Xldv20TvVclTerminationPointA_Object = MibScalar
xldv20TvVclTerminationPointA = _Xldv20TvVclTerminationPointA_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 51),
    _Xldv20TvVclTerminationPointA_Type()
)
xldv20TvVclTerminationPointA.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvVclTerminationPointA.setStatus("mandatory")
_Xldv20TvVclTerminationPointZ_Type = Integer32
_Xldv20TvVclTerminationPointZ_Object = MibScalar
xldv20TvVclTerminationPointZ = _Xldv20TvVclTerminationPointZ_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 52),
    _Xldv20TvVclTerminationPointZ_Type()
)
xldv20TvVclTerminationPointZ.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvVclTerminationPointZ.setStatus("mandatory")
_Xldv20TvVpcTpIndex_Type = Unsigned16
_Xldv20TvVpcTpIndex_Object = MibScalar
xldv20TvVpcTpIndex = _Xldv20TvVpcTpIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 53),
    _Xldv20TvVpcTpIndex_Type()
)
xldv20TvVpcTpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvVpcTpIndex.setStatus("mandatory")
_Xldv20TvVpcNniIndex_Type = Unsigned16
_Xldv20TvVpcNniIndex_Object = MibScalar
xldv20TvVpcNniIndex = _Xldv20TvVpcNniIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 54),
    _Xldv20TvVpcNniIndex_Type()
)
xldv20TvVpcNniIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvVpcNniIndex.setStatus("mandatory")
_Xldv20TvVpcUniIndex_Type = Unsigned16
_Xldv20TvVpcUniIndex_Object = MibScalar
xldv20TvVpcUniIndex = _Xldv20TvVpcUniIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 55),
    _Xldv20TvVpcUniIndex_Type()
)
xldv20TvVpcUniIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvVpcUniIndex.setStatus("mandatory")
_Xldv20TvEthVccTpIndex_Type = Unsigned16
_Xldv20TvEthVccTpIndex_Object = MibScalar
xldv20TvEthVccTpIndex = _Xldv20TvEthVccTpIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 56),
    _Xldv20TvEthVccTpIndex_Type()
)
xldv20TvEthVccTpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvEthVccTpIndex.setStatus("mandatory")
_Xldv20TvVpiValue_Type = Integer32
_Xldv20TvVpiValue_Object = MibScalar
xldv20TvVpiValue = _Xldv20TvVpiValue_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 57),
    _Xldv20TvVpiValue_Type()
)
xldv20TvVpiValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvVpiValue.setStatus("mandatory")
_Xldv20TvVciValue_Type = Unsigned16
_Xldv20TvVciValue_Object = MibScalar
xldv20TvVciValue = _Xldv20TvVciValue_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 58),
    _Xldv20TvVciValue_Type()
)
xldv20TvVciValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvVciValue.setStatus("mandatory")
_Xldv20TvVplTpIndex_Type = Integer32
_Xldv20TvVplTpIndex_Object = MibScalar
xldv20TvVplTpIndex = _Xldv20TvVplTpIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 59),
    _Xldv20TvVplTpIndex_Type()
)
xldv20TvVplTpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvVplTpIndex.setStatus("mandatory")
_Xldv20TvVplIfIndex_Type = Integer32
_Xldv20TvVplIfIndex_Object = MibScalar
xldv20TvVplIfIndex = _Xldv20TvVplIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 60),
    _Xldv20TvVplIfIndex_Type()
)
xldv20TvVplIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvVplIfIndex.setStatus("mandatory")


class _Xldv20TvAlmFailedComponentString_Type(OctetString):
    """Custom type xldv20TvAlmFailedComponentString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_Xldv20TvAlmFailedComponentString_Type.__name__ = "OctetString"
_Xldv20TvAlmFailedComponentString_Object = MibScalar
xldv20TvAlmFailedComponentString = _Xldv20TvAlmFailedComponentString_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 61),
    _Xldv20TvAlmFailedComponentString_Type()
)
xldv20TvAlmFailedComponentString.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvAlmFailedComponentString.setStatus("mandatory")
_Xldv20TvTelnetSession_Type = Xldv20TvTelnetSessionStatus
_Xldv20TvTelnetSession_Object = MibScalar
xldv20TvTelnetSession = _Xldv20TvTelnetSession_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 62),
    _Xldv20TvTelnetSession_Type()
)
xldv20TvTelnetSession.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvTelnetSession.setStatus("mandatory")
_Xldv20TvEthIfIndex_Type = Integer32
_Xldv20TvEthIfIndex_Object = MibScalar
xldv20TvEthIfIndex = _Xldv20TvEthIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 63),
    _Xldv20TvEthIfIndex_Type()
)
xldv20TvEthIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvEthIfIndex.setStatus("mandatory")
_Xldv20TvCACProblemType_Type = Xldv20ControlReq
_Xldv20TvCACProblemType_Object = MibScalar
xldv20TvCACProblemType = _Xldv20TvCACProblemType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 64),
    _Xldv20TvCACProblemType_Type()
)
xldv20TvCACProblemType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvCACProblemType.setStatus("mandatory")


class _Xldv20TvCACBandwidthUsageUp_Type(Integer32):
    """Custom type xldv20TvCACBandwidthUsageUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Xldv20TvCACBandwidthUsageUp_Type.__name__ = "Integer32"
_Xldv20TvCACBandwidthUsageUp_Object = MibScalar
xldv20TvCACBandwidthUsageUp = _Xldv20TvCACBandwidthUsageUp_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 65),
    _Xldv20TvCACBandwidthUsageUp_Type()
)
xldv20TvCACBandwidthUsageUp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvCACBandwidthUsageUp.setStatus("mandatory")
_Xldv20TvEthVpcTpIndex_Type = Unsigned16
_Xldv20TvEthVpcTpIndex_Object = MibScalar
xldv20TvEthVpcTpIndex = _Xldv20TvEthVpcTpIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 66),
    _Xldv20TvEthVpcTpIndex_Type()
)
xldv20TvEthVpcTpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvEthVpcTpIndex.setStatus("mandatory")
_Xldv20TvEthEntryIndex_Type = Unsigned16
_Xldv20TvEthEntryIndex_Object = MibScalar
xldv20TvEthEntryIndex = _Xldv20TvEthEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 68),
    _Xldv20TvEthEntryIndex_Type()
)
xldv20TvEthEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvEthEntryIndex.setStatus("mandatory")
_Xldv20TvRepEntityExt_Type = Unsigned16
_Xldv20TvRepEntityExt_Object = MibScalar
xldv20TvRepEntityExt = _Xldv20TvRepEntityExt_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 69),
    _Xldv20TvRepEntityExt_Type()
)
xldv20TvRepEntityExt.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvRepEntityExt.setStatus("mandatory")


class _Xldv20TvTelnetSessionUser_Type(DisplayString):
    """Custom type xldv20TvTelnetSessionUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Xldv20TvTelnetSessionUser_Type.__name__ = "DisplayString"
_Xldv20TvTelnetSessionUser_Object = MibScalar
xldv20TvTelnetSessionUser = _Xldv20TvTelnetSessionUser_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 70),
    _Xldv20TvTelnetSessionUser_Type()
)
xldv20TvTelnetSessionUser.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvTelnetSessionUser.setStatus("mandatory")
_Xldv20TvIndexSegment_Type = Unsigned16
_Xldv20TvIndexSegment_Object = MibScalar
xldv20TvIndexSegment = _Xldv20TvIndexSegment_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 71),
    _Xldv20TvIndexSegment_Type()
)
xldv20TvIndexSegment.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvIndexSegment.setStatus("mandatory")
_Xldv20TvIndexEndToEnd_Type = Unsigned16
_Xldv20TvIndexEndToEnd_Object = MibScalar
xldv20TvIndexEndToEnd = _Xldv20TvIndexEndToEnd_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 72),
    _Xldv20TvIndexEndToEnd_Type()
)
xldv20TvIndexEndToEnd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvIndexEndToEnd.setStatus("mandatory")
_Xldv20TvRestoreResult_Type = Xldv20ControlReq
_Xldv20TvRestoreResult_Object = MibScalar
xldv20TvRestoreResult = _Xldv20TvRestoreResult_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 75),
    _Xldv20TvRestoreResult_Type()
)
xldv20TvRestoreResult.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvRestoreResult.setStatus("mandatory")


class _Xldv20TvCACBandwidthUsageDown_Type(Integer32):
    """Custom type xldv20TvCACBandwidthUsageDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Xldv20TvCACBandwidthUsageDown_Type.__name__ = "Integer32"
_Xldv20TvCACBandwidthUsageDown_Object = MibScalar
xldv20TvCACBandwidthUsageDown = _Xldv20TvCACBandwidthUsageDown_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 76),
    _Xldv20TvCACBandwidthUsageDown_Type()
)
xldv20TvCACBandwidthUsageDown.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvCACBandwidthUsageDown.setStatus("mandatory")
_Xldv20TvCallpObjectType_Type = Xldv20RepSource
_Xldv20TvCallpObjectType_Object = MibScalar
xldv20TvCallpObjectType = _Xldv20TvCallpObjectType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 77),
    _Xldv20TvCallpObjectType_Type()
)
xldv20TvCallpObjectType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvCallpObjectType.setStatus("mandatory")


class _Xldv20TvVpcTpIfIndex_Type(Integer32):
    """Custom type xldv20TvVpcTpIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9192),
    )


_Xldv20TvVpcTpIfIndex_Type.__name__ = "Integer32"
_Xldv20TvVpcTpIfIndex_Object = MibScalar
xldv20TvVpcTpIfIndex = _Xldv20TvVpcTpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 79),
    _Xldv20TvVpcTpIfIndex_Type()
)
xldv20TvVpcTpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvVpcTpIfIndex.setStatus("mandatory")


class _Xldv20TvAlmSpecProblemText_Type(OctetString):
    """Custom type xldv20TvAlmSpecProblemText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_Xldv20TvAlmSpecProblemText_Type.__name__ = "OctetString"
_Xldv20TvAlmSpecProblemText_Object = MibScalar
xldv20TvAlmSpecProblemText = _Xldv20TvAlmSpecProblemText_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 80),
    _Xldv20TvAlmSpecProblemText_Type()
)
xldv20TvAlmSpecProblemText.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvAlmSpecProblemText.setStatus("mandatory")
_Xldv20TvImaSetNumResult_Type = Xldv20ControlReq
_Xldv20TvImaSetNumResult_Object = MibScalar
xldv20TvImaSetNumResult = _Xldv20TvImaSetNumResult_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 81),
    _Xldv20TvImaSetNumResult_Type()
)
xldv20TvImaSetNumResult.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvImaSetNumResult.setStatus("mandatory")
_Xldv20TvStcOldAvailStatus_Type = Xldv20AvailStatus
_Xldv20TvStcOldAvailStatus_Object = MibScalar
xldv20TvStcOldAvailStatus = _Xldv20TvStcOldAvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 82),
    _Xldv20TvStcOldAvailStatus_Type()
)
xldv20TvStcOldAvailStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvStcOldAvailStatus.setStatus("mandatory")
_Xldv20TvStcNewAvailStatus_Type = Xldv20AvailStatus
_Xldv20TvStcNewAvailStatus_Object = MibScalar
xldv20TvStcNewAvailStatus = _Xldv20TvStcNewAvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 1, 83),
    _Xldv20TvStcNewAvailStatus_Type()
)
xldv20TvStcNewAvailStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20TvStcNewAvailStatus.setStatus("mandatory")
_Xldv20TrapTypes_ObjectIdentity = ObjectIdentity
xldv20TrapTypes = _Xldv20TrapTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 2)
)

# Managed Objects groups


# Notification objects

xldv20TrHpExcBER = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 1)
)
xldv20TrHpExcBER.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponent"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblemText"))
)
if mibBuilder.loadTexts:
    xldv20TrHpExcBER.setStatus(
        ""
    )

xldv20TrHpUNEQ = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 2)
)
xldv20TrHpUNEQ.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponent"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblemText"))
)
if mibBuilder.loadTexts:
    xldv20TrHpUNEQ.setStatus(
        ""
    )

xldv20TrLcd = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 3)
)
xldv20TrLcd.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponent"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblemText"))
)
if mibBuilder.loadTexts:
    xldv20TrLcd.setStatus(
        ""
    )

xldv20TrLof = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 4)
)
xldv20TrLof.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponent"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblemText"))
)
if mibBuilder.loadTexts:
    xldv20TrLof.setStatus(
        ""
    )

xldv20TrLop = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 5)
)
xldv20TrLop.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponent"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblemText"))
)
if mibBuilder.loadTexts:
    xldv20TrLop.setStatus(
        ""
    )

xldv20TrLos = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 6)
)
xldv20TrLos.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponent"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblemText"))
)
if mibBuilder.loadTexts:
    xldv20TrLos.setStatus(
        ""
    )

xldv20TrMsAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 7)
)
xldv20TrMsAIS.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponent"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblemText"))
)
if mibBuilder.loadTexts:
    xldv20TrMsAIS.setStatus(
        ""
    )

xldv20TrMsExcBER = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 8)
)
xldv20TrMsExcBER.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponent"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblemText"))
)
if mibBuilder.loadTexts:
    xldv20TrMsExcBER.setStatus(
        ""
    )

xldv20TrMsRDI = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 9)
)
xldv20TrMsRDI.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponent"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblemText"))
)
if mibBuilder.loadTexts:
    xldv20TrMsRDI.setStatus(
        ""
    )

xldv20TrMsSD = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 10)
)
xldv20TrMsSD.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponent"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblemText"))
)
if mibBuilder.loadTexts:
    xldv20TrMsSD.setStatus(
        ""
    )

xldv20TrPAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 11)
)
xldv20TrPAIS.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponent"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblemText"))
)
if mibBuilder.loadTexts:
    xldv20TrPAIS.setStatus(
        ""
    )

xldv20TrPRDI = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 12)
)
xldv20TrPRDI.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponent"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblemText"))
)
if mibBuilder.loadTexts:
    xldv20TrPRDI.setStatus(
        ""
    )

xldv20TrRsExcBER = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 13)
)
xldv20TrRsExcBER.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponent"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblemText"))
)
if mibBuilder.loadTexts:
    xldv20TrRsExcBER.setStatus(
        ""
    )

xldv20TrSlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 14)
)
xldv20TrSlm.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponent"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblemText"))
)
if mibBuilder.loadTexts:
    xldv20TrSlm.setStatus(
        ""
    )

xldv20TrTim = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 15)
)
xldv20TrTim.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponent"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblemText"))
)
if mibBuilder.loadTexts:
    xldv20TrTim.setStatus(
        ""
    )

xldv20TrActFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 16)
)
xldv20TrActFault.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponent"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblemText"))
)
if mibBuilder.loadTexts:
    xldv20TrActFault.setStatus(
        ""
    )

xldv20TrReplaceableUnitTypeMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 17)
)
xldv20TrReplaceableUnitTypeMismatch.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponent"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblemText"))
)
if mibBuilder.loadTexts:
    xldv20TrReplaceableUnitTypeMismatch.setStatus(
        ""
    )

xldv20TrReplaceableUnitFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 18)
)
xldv20TrReplaceableUnitFailure.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponent"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblemText"))
)
if mibBuilder.loadTexts:
    xldv20TrReplaceableUnitFailure.setStatus(
        ""
    )

xldv20TrReplaceableUnitProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 19)
)
xldv20TrReplaceableUnitProblem.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponent"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblemText"))
)
if mibBuilder.loadTexts:
    xldv20TrReplaceableUnitProblem.setStatus(
        ""
    )

xldv20TrReplaceableUnitNotInstalled = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 20)
)
xldv20TrReplaceableUnitNotInstalled.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponent"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblemText"))
)
if mibBuilder.loadTexts:
    xldv20TrReplaceableUnitNotInstalled.setStatus(
        ""
    )

xldv20TrReplaceableUnitSwMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 21)
)
xldv20TrReplaceableUnitSwMismatch.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponent"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblemText"))
)
if mibBuilder.loadTexts:
    xldv20TrReplaceableUnitSwMismatch.setStatus(
        ""
    )

xldv20TrReplaceableUnitReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 22)
)
xldv20TrReplaceableUnitReset.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvHweResetType"))
)
if mibBuilder.loadTexts:
    xldv20TrReplaceableUnitReset.setStatus(
        ""
    )

xldv20TrReplaceableUnitResetEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 23)
)
xldv20TrReplaceableUnitResetEnd.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"))
)
if mibBuilder.loadTexts:
    xldv20TrReplaceableUnitResetEnd.setStatus(
        ""
    )

xldv20TrStartupEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 24)
)
xldv20TrStartupEnd.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvStartupResult"),
        ("XLDV20-MIB", "xldv20TvStartupType"),
        ("XLDV20-MIB", "xldv20TvSnmMibVersion"),
        ("XLDV20-MIB", "xldv20TvSnmAgentVersion"),
        ("XLDV20-MIB", "xldv20TvVersionNrCmuLoad"))
)
if mibBuilder.loadTexts:
    xldv20TrStartupEnd.setStatus(
        ""
    )

xldv20TrLctSession = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 25)
)
xldv20TrLctSession.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvSnmLctSession"))
)
if mibBuilder.loadTexts:
    xldv20TrLctSession.setStatus(
        ""
    )

xldv20TrSnmAgentRunning = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 26)
)
xldv20TrSnmAgentRunning.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvSnmMibVersion"),
        ("XLDV20-MIB", "xldv20TvSnmAgentVersion"))
)
if mibBuilder.loadTexts:
    xldv20TrSnmAgentRunning.setStatus(
        ""
    )

xldv20TrRstResult = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 27)
)
xldv20TrRstResult.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRstResult"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvRstHwUnitIndex"))
)
if mibBuilder.loadTexts:
    xldv20TrRstResult.setStatus(
        ""
    )

xldv20TrPltTestResult = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 28)
)
xldv20TrPltTestResult.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvTsrControlStatus"))
)
if mibBuilder.loadTexts:
    xldv20TrPltTestResult.setStatus(
        ""
    )

xldv20TrStateChangeAdmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 29)
)
xldv20TrStateChangeAdmin.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvStcOldAdminStatus"),
        ("XLDV20-MIB", "xldv20TvStcNewAdminStatus"))
)
if mibBuilder.loadTexts:
    xldv20TrStateChangeAdmin.setStatus(
        ""
    )

xldv20TrStateChangeOper = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 30)
)
xldv20TrStateChangeOper.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvStcOldOperStatus"),
        ("XLDV20-MIB", "xldv20TvStcNewOperStatus"))
)
if mibBuilder.loadTexts:
    xldv20TrStateChangeOper.setStatus(
        ""
    )

xldv20TrChangeRate = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 31)
)
xldv20TrChangeRate.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvAdcControlStatus"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"))
)
if mibBuilder.loadTexts:
    xldv20TrChangeRate.setStatus(
        ""
    )

xldv20TrCmuReadyForReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 32)
)
xldv20TrCmuReadyForReset.setObjects(
    ("XLDV20-MIB", "xldv20TvTimeAndDate")
)
if mibBuilder.loadTexts:
    xldv20TrCmuReadyForReset.setStatus(
        ""
    )

xldv20TrAltTestResult = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 33)
)
xldv20TrAltTestResult.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvTsrControlStatus"))
)
if mibBuilder.loadTexts:
    xldv20TrAltTestResult.setStatus(
        ""
    )

xldv20TrActivateLoadResult = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 34)
)
xldv20TrActivateLoadResult.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvSucResult"),
        ("XLDV20-MIB", "xldv20TvSucUnit"),
        ("XLDV20-MIB", "xldv20TvSucHwUnitIndex"))
)
if mibBuilder.loadTexts:
    xldv20TrActivateLoadResult.setStatus(
        ""
    )

xldv20TrPuUpgradeSucc = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 35)
)
xldv20TrPuUpgradeSucc.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvSucUnit"),
        ("XLDV20-MIB", "xldv20TvSucHwUnitIndex"),
        ("XLDV20-MIB", "xldv20TvSucVersionNo"))
)
if mibBuilder.loadTexts:
    xldv20TrPuUpgradeSucc.setStatus(
        ""
    )

xldv20TrUpgradeCancelled = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 36)
)
xldv20TrUpgradeCancelled.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvSucUnit"),
        ("XLDV20-MIB", "xldv20TvSucHwUnitIndex"),
        ("XLDV20-MIB", "xldv20TvSucVersionNo"),
        ("XLDV20-MIB", "xldv20TvSucResult"))
)
if mibBuilder.loadTexts:
    xldv20TrUpgradeCancelled.setStatus(
        ""
    )

xldv20TrFtpError = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 38)
)
xldv20TrFtpError.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvSucUnit"),
        ("XLDV20-MIB", "xldv20TvSucPathName"),
        ("XLDV20-MIB", "xldv20TvSucFileName"),
        ("XLDV20-MIB", "xldv20TvSucResult"))
)
if mibBuilder.loadTexts:
    xldv20TrFtpError.setStatus(
        ""
    )

xldv20TrSweLogRead = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 40)
)
xldv20TrSweLogRead.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvDbuSweLogReadResult"))
)
if mibBuilder.loadTexts:
    xldv20TrSweLogRead.setStatus(
        ""
    )

xldv20TrHwmLogRead = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 41)
)
xldv20TrHwmLogRead.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvDbuHwmLogReadResult"))
)
if mibBuilder.loadTexts:
    xldv20TrHwmLogRead.setStatus(
        ""
    )

xldv20TrTraceLogRead = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 42)
)
xldv20TrTraceLogRead.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvDbuSwTraceLogReadResult"))
)
if mibBuilder.loadTexts:
    xldv20TrTraceLogRead.setStatus(
        ""
    )

xldv20TrVplCcCreation = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 45)
)
xldv20TrVplCcCreation.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvVpiNni"),
        ("XLDV20-MIB", "xldv20TvVpiNniIndex"),
        ("XLDV20-MIB", "xldv20TvVplTerminationPointA"),
        ("XLDV20-MIB", "xldv20TvVplTerminationPointZ"),
        ("XLDV20-MIB", "xldv20TvEthVpcTpIndex"),
        ("XLDV20-MIB", "xldv20TvEthVccTpIndex"),
        ("XLDV20-MIB", "xldv20TvVplTpIndex"))
)
if mibBuilder.loadTexts:
    xldv20TrVplCcCreation.setStatus(
        ""
    )

xldv20TrVplCcDeletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 46)
)
xldv20TrVplCcDeletion.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvVpiNni"),
        ("XLDV20-MIB", "xldv20TvVpiNniIndex"),
        ("XLDV20-MIB", "xldv20TvVplTerminationPointA"),
        ("XLDV20-MIB", "xldv20TvVplTerminationPointZ"),
        ("XLDV20-MIB", "xldv20TvEthVpcTpIndex"),
        ("XLDV20-MIB", "xldv20TvEthVccTpIndex"),
        ("XLDV20-MIB", "xldv20TvVplTpIndex"))
)
if mibBuilder.loadTexts:
    xldv20TrVplCcDeletion.setStatus(
        ""
    )

xldv20TrObjCreate = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 100)
)
xldv20TrObjCreate.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvHwUnitType"),
        ("XLDV20-MIB", "xldv20TvHwContainingUnitIndex"),
        ("XLDV20-MIB", "xldv20TvHwContainedUnitAddr"))
)
if mibBuilder.loadTexts:
    xldv20TrObjCreate.setStatus(
        ""
    )

xldv20TrObjDelete = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 101)
)
xldv20TrObjDelete.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvHwUnitType"),
        ("XLDV20-MIB", "xldv20TvHwContainingUnitIndex"),
        ("XLDV20-MIB", "xldv20TvHwContainedUnitAddr"))
)
if mibBuilder.loadTexts:
    xldv20TrObjDelete.setStatus(
        ""
    )

xldv20TrXmissionErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 105)
)
xldv20TrXmissionErr.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponent"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblemText"))
)
if mibBuilder.loadTexts:
    xldv20TrXmissionErr.setStatus(
        ""
    )

xldv20TrExternalAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 110)
)
xldv20TrExternalAlarm.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponent"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblemText"))
)
if mibBuilder.loadTexts:
    xldv20TrExternalAlarm.setStatus(
        ""
    )

xldv20TrUnitReadyForReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 111)
)
xldv20TrUnitReadyForReset.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvSucUnit"),
        ("XLDV20-MIB", "xldv20TvSucHwUnitIndex"),
        ("XLDV20-MIB", "xldv20TvSucVersionNo"))
)
if mibBuilder.loadTexts:
    xldv20TrUnitReadyForReset.setStatus(
        ""
    )

xldv20TrHwuControl = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 112)
)
xldv20TrHwuControl.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvHwuControlResult"))
)
if mibBuilder.loadTexts:
    xldv20TrHwuControl.setStatus(
        ""
    )

xldv20TrReplaceableUnitRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 113)
)
xldv20TrReplaceableUnitRemoved.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponent"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblemText"))
)
if mibBuilder.loadTexts:
    xldv20TrReplaceableUnitRemoved.setStatus(
        ""
    )

xldv20TrAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 114)
)
xldv20TrAIS.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponent"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblemText"))
)
if mibBuilder.loadTexts:
    xldv20TrAIS.setStatus(
        ""
    )

xldv20TrRDI = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 115)
)
xldv20TrRDI.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponent"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblemText"))
)
if mibBuilder.loadTexts:
    xldv20TrRDI.setStatus(
        ""
    )

xldv20TrPlcpLof = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 116)
)
xldv20TrPlcpLof.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponent"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblemText"))
)
if mibBuilder.loadTexts:
    xldv20TrPlcpLof.setStatus(
        ""
    )

xldv20TrPlcpRDI = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 117)
)
xldv20TrPlcpRDI.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponent"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblemText"))
)
if mibBuilder.loadTexts:
    xldv20TrPlcpRDI.setStatus(
        ""
    )

xldv20TrRemInvReady = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 118)
)
xldv20TrRemInvReady.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRiRemInvResult"))
)
if mibBuilder.loadTexts:
    xldv20TrRemInvReady.setStatus(
        ""
    )

xldv20TrDbBackup = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 119)
)
xldv20TrDbBackup.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvBackupResult"))
)
if mibBuilder.loadTexts:
    xldv20TrDbBackup.setStatus(
        ""
    )

xldv20TrSwVersionSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 120)
)
xldv20TrSwVersionSet.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvRepEntity"))
)
if mibBuilder.loadTexts:
    xldv20TrSwVersionSet.setStatus(
        ""
    )

xldv20TrReadSAPSContentFileReady = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 121)
)
xldv20TrReadSAPSContentFileReady.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvSucResult"))
)
if mibBuilder.loadTexts:
    xldv20TrReadSAPSContentFileReady.setStatus(
        ""
    )

xldv20TrReplaceableUnitSwMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 122)
)
xldv20TrReplaceableUnitSwMissing.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponent"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblemText"))
)
if mibBuilder.loadTexts:
    xldv20TrReplaceableUnitSwMissing.setStatus(
        ""
    )

xldv20TrInternalFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 123)
)
xldv20TrInternalFault.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponent"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblemText"))
)
if mibBuilder.loadTexts:
    xldv20TrInternalFault.setStatus(
        ""
    )

xldv20TrVclCcCreation = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 127)
)
xldv20TrVclCcCreation.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvVpiNni"),
        ("XLDV20-MIB", "xldv20TvVciNni"),
        ("XLDV20-MIB", "xldv20TvVciNniIndex"),
        ("XLDV20-MIB", "xldv20TvVclTerminationPointA"),
        ("XLDV20-MIB", "xldv20TvVclTerminationPointZ"),
        ("XLDV20-MIB", "xldv20TvEthVpcTpIndex"),
        ("XLDV20-MIB", "xldv20TvEthVccTpIndex"),
        ("XLDV20-MIB", "xldv20TvVplTpIndex"))
)
if mibBuilder.loadTexts:
    xldv20TrVclCcCreation.setStatus(
        ""
    )

xldv20TrVclCcDeletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 128)
)
xldv20TrVclCcDeletion.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvVpiNni"),
        ("XLDV20-MIB", "xldv20TvVciNni"),
        ("XLDV20-MIB", "xldv20TvVciNniIndex"),
        ("XLDV20-MIB", "xldv20TvVclTerminationPointA"),
        ("XLDV20-MIB", "xldv20TvVclTerminationPointZ"),
        ("XLDV20-MIB", "xldv20TvEthVpcTpIndex"),
        ("XLDV20-MIB", "xldv20TvEthVccTpIndex"),
        ("XLDV20-MIB", "xldv20TvEthEntryIndex"),
        ("XLDV20-MIB", "xldv20TvVplTpIndex"))
)
if mibBuilder.loadTexts:
    xldv20TrVclCcDeletion.setStatus(
        ""
    )

xldv20TrImmMNR = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 130)
)
xldv20TrImmMNR.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponent"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblemText"))
)
if mibBuilder.loadTexts:
    xldv20TrImmMNR.setStatus(
        ""
    )

xldv20TrLpr = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 131)
)
xldv20TrLpr.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponent"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblemText"))
)
if mibBuilder.loadTexts:
    xldv20TrLpr.setStatus(
        ""
    )

xldv20TrLol = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 132)
)
xldv20TrLol.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponent"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblemText"))
)
if mibBuilder.loadTexts:
    xldv20TrLol.setStatus(
        ""
    )

xldv20TrAtmLayerMultiAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 135)
)
xldv20TrAtmLayerMultiAlarm.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentString"))
)
if mibBuilder.loadTexts:
    xldv20TrAtmLayerMultiAlarm.setStatus(
        ""
    )

xldv20TrTelnetSession = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 136)
)
xldv20TrTelnetSession.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvTelnetSession"),
        ("XLDV20-MIB", "xldv20TvTelnetSessionUser"))
)
if mibBuilder.loadTexts:
    xldv20TrTelnetSession.setStatus(
        ""
    )

xldv20TrVplCACProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 137)
)
xldv20TrVplCACProblem.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvVpiValue"),
        ("XLDV20-MIB", "xldv20TvVplIfIndex"),
        ("XLDV20-MIB", "xldv20TvCACProblemType"),
        ("XLDV20-MIB", "xldv20TvCACBandwidthUsageUp"),
        ("XLDV20-MIB", "xldv20TvCACBandwidthUsageDown"))
)
if mibBuilder.loadTexts:
    xldv20TrVplCACProblem.setStatus(
        ""
    )

xldv20TrVclCACProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 139)
)
xldv20TrVclCACProblem.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvVpiValue"),
        ("XLDV20-MIB", "xldv20TvVplIfIndex"),
        ("XLDV20-MIB", "xldv20TvVplTpIndex"),
        ("XLDV20-MIB", "xldv20TvVciValue"),
        ("XLDV20-MIB", "xldv20TvCACProblemType"),
        ("XLDV20-MIB", "xldv20TvCACBandwidthUsageUp"),
        ("XLDV20-MIB", "xldv20TvCACBandwidthUsageDown"))
)
if mibBuilder.loadTexts:
    xldv20TrVclCACProblem.setStatus(
        ""
    )

xldv20TrWrongServiceConfigData = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 141)
)
xldv20TrWrongServiceConfigData.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponent"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblemText"))
)
if mibBuilder.loadTexts:
    xldv20TrWrongServiceConfigData.setStatus(
        ""
    )

xldv20TrReplaceableUnitPlugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 142)
)
xldv20TrReplaceableUnitPlugged.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"))
)
if mibBuilder.loadTexts:
    xldv20TrReplaceableUnitPlugged.setStatus(
        ""
    )

xldv20TrReplaceableUnitUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 143)
)
xldv20TrReplaceableUnitUnplugged.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"))
)
if mibBuilder.loadTexts:
    xldv20TrReplaceableUnitUnplugged.setStatus(
        ""
    )

xldv20TrStateChangeOperExt = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 144)
)
xldv20TrStateChangeOperExt.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntityExt"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvStcOldOperStatus"),
        ("XLDV20-MIB", "xldv20TvStcNewOperStatus"))
)
if mibBuilder.loadTexts:
    xldv20TrStateChangeOperExt.setStatus(
        ""
    )

xldv20TrLOC = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 145)
)
xldv20TrLOC.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponent"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblemText"))
)
if mibBuilder.loadTexts:
    xldv20TrLOC.setStatus(
        ""
    )

xldv20TrDbRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 150)
)
xldv20TrDbRestore.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRestoreResult"))
)
if mibBuilder.loadTexts:
    xldv20TrDbRestore.setStatus(
        ""
    )

xldv20TrUpgradeEndRequestResult = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 151)
)
xldv20TrUpgradeEndRequestResult.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvSucResult"))
)
if mibBuilder.loadTexts:
    xldv20TrUpgradeEndRequestResult.setStatus(
        ""
    )

xldv20TrUnitUpgradeNotRequested = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 152)
)
xldv20TrUnitUpgradeNotRequested.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvSucUnit"),
        ("XLDV20-MIB", "xldv20TvSucHwUnitIndex"),
        ("XLDV20-MIB", "xldv20TvSucVersionNo"))
)
if mibBuilder.loadTexts:
    xldv20TrUnitUpgradeNotRequested.setStatus(
        ""
    )

xldv20TrVpcTpCreation = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 400)
)
xldv20TrVpcTpCreation.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvVpiValue"),
        ("XLDV20-MIB", "xldv20TvVpcTpIndex"))
)
if mibBuilder.loadTexts:
    xldv20TrVpcTpCreation.setStatus(
        ""
    )

xldv20TrVpcTpDeletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 401)
)
xldv20TrVpcTpDeletion.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvVpiValue"),
        ("XLDV20-MIB", "xldv20TvVpcTpIndex"))
)
if mibBuilder.loadTexts:
    xldv20TrVpcTpDeletion.setStatus(
        ""
    )

xldv20TrVpcTpCACProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 402)
)
xldv20TrVpcTpCACProblem.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvVpiValue"),
        ("XLDV20-MIB", "xldv20TvVpcTpIfIndex"),
        ("XLDV20-MIB", "xldv20TvCACProblemType"),
        ("XLDV20-MIB", "xldv20TvCACBandwidthUsageUp"),
        ("XLDV20-MIB", "xldv20TvCACBandwidthUsageDown"))
)
if mibBuilder.loadTexts:
    xldv20TrVpcTpCACProblem.setStatus(
        ""
    )

xldv20TrContinuityCheckVpEntryCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 403)
)
xldv20TrContinuityCheckVpEntryCreated.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvCallpObjectType"),
        ("XLDV20-MIB", "xldv20TvIndexSegment"),
        ("XLDV20-MIB", "xldv20TvIndexEndToEnd"))
)
if mibBuilder.loadTexts:
    xldv20TrContinuityCheckVpEntryCreated.setStatus(
        ""
    )

xldv20TrContinuityCheckVpEntryDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 404)
)
xldv20TrContinuityCheckVpEntryDeleted.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvCallpObjectType"),
        ("XLDV20-MIB", "xldv20TvIndexSegment"),
        ("XLDV20-MIB", "xldv20TvIndexEndToEnd"))
)
if mibBuilder.loadTexts:
    xldv20TrContinuityCheckVpEntryDeleted.setStatus(
        ""
    )

xldv20TrContinuityCheckVcEntryCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 405)
)
xldv20TrContinuityCheckVcEntryCreated.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvCallpObjectType"),
        ("XLDV20-MIB", "xldv20TvIndexSegment"),
        ("XLDV20-MIB", "xldv20TvIndexEndToEnd"))
)
if mibBuilder.loadTexts:
    xldv20TrContinuityCheckVcEntryCreated.setStatus(
        ""
    )

xldv20TrContinuityCheckVcEntryDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 406)
)
xldv20TrContinuityCheckVcEntryDeleted.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvCallpObjectType"),
        ("XLDV20-MIB", "xldv20TvIndexSegment"),
        ("XLDV20-MIB", "xldv20TvIndexEndToEnd"))
)
if mibBuilder.loadTexts:
    xldv20TrContinuityCheckVcEntryDeleted.setStatus(
        ""
    )

xldv20TrExcBER = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 407)
)
xldv20TrExcBER.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponent"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblemText"))
)
if mibBuilder.loadTexts:
    xldv20TrExcBER.setStatus(
        ""
    )

xldv20TrLif = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 408)
)
xldv20TrLif.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponent"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblemText"))
)
if mibBuilder.loadTexts:
    xldv20TrLif.setStatus(
        ""
    )

xldv20TrLods = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 409)
)
xldv20TrLods.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponent"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblemText"))
)
if mibBuilder.loadTexts:
    xldv20TrLods.setStatus(
        ""
    )

xldv20TrTxUnusableFe = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 410)
)
xldv20TrTxUnusableFe.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponent"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblemText"))
)
if mibBuilder.loadTexts:
    xldv20TrTxUnusableFe.setStatus(
        ""
    )

xldv20TrRxUnusableFe = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 411)
)
xldv20TrRxUnusableFe.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponent"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblemText"))
)
if mibBuilder.loadTexts:
    xldv20TrRxUnusableFe.setStatus(
        ""
    )

xldv20TrRfiIma = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 412)
)
xldv20TrRfiIma.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponent"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblemText"))
)
if mibBuilder.loadTexts:
    xldv20TrRfiIma.setStatus(
        ""
    )

xldv20TrRAI = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 413)
)
xldv20TrRAI.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponent"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblemText"))
)
if mibBuilder.loadTexts:
    xldv20TrRAI.setStatus(
        ""
    )

xldv20TrStartUpFe = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 450)
)
xldv20TrStartUpFe.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponent"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblemText"))
)
if mibBuilder.loadTexts:
    xldv20TrStartUpFe.setStatus(
        ""
    )

xldv20TrConfigAbort = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 451)
)
xldv20TrConfigAbort.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponent"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblemText"))
)
if mibBuilder.loadTexts:
    xldv20TrConfigAbort.setStatus(
        ""
    )

xldv20TrConfigAbortFe = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 452)
)
xldv20TrConfigAbortFe.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponent"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblemText"))
)
if mibBuilder.loadTexts:
    xldv20TrConfigAbortFe.setStatus(
        ""
    )

xldv20TrInsufficientLinks = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 453)
)
xldv20TrInsufficientLinks.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponent"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblemText"))
)
if mibBuilder.loadTexts:
    xldv20TrInsufficientLinks.setStatus(
        ""
    )

xldv20TrInsufficientLinksFe = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 454)
)
xldv20TrInsufficientLinksFe.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponent"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblemText"))
)
if mibBuilder.loadTexts:
    xldv20TrInsufficientLinksFe.setStatus(
        ""
    )

xldv20TrBlockedFe = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 455)
)
xldv20TrBlockedFe.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblem"),
        ("XLDV20-MIB", "xldv20TvAlmNatureOfAlarm"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponent"),
        ("XLDV20-MIB", "xldv20TvAlmFailedComponentRepSource"),
        ("XLDV20-MIB", "xldv20TvAlmSeverityOfFailure"),
        ("XLDV20-MIB", "xldv20TvAlmStatus"),
        ("XLDV20-MIB", "xldv20TvAlmPropRepairAction"),
        ("XLDV20-MIB", "xldv20TvAlmSpecProblemText"))
)
if mibBuilder.loadTexts:
    xldv20TrBlockedFe.setStatus(
        ""
    )

xldv20TrImaMinNumOfLinks = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 456)
)
xldv20TrImaMinNumOfLinks.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvImaSetNumResult"))
)
if mibBuilder.loadTexts:
    xldv20TrImaMinNumOfLinks.setStatus(
        ""
    )

xldv20TrStateChangeAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 457)
)
xldv20TrStateChangeAvail.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20-MIB", "xldv20TvRepEntity"),
        ("XLDV20-MIB", "xldv20TvRepSource"),
        ("XLDV20-MIB", "xldv20TvStcOldAvailStatus"),
        ("XLDV20-MIB", "xldv20TvStcNewAvailStatus"))
)
if mibBuilder.loadTexts:
    xldv20TrStateChangeAvail.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XLDV20-MIB",
    **{"Xldv20ControlStatus": Xldv20ControlStatus,
       "Xldv20OperState": Xldv20OperState,
       "Xldv20SlotStatus": Xldv20SlotStatus,
       "Xldv20AdminState": Xldv20AdminState,
       "Xldv20AvailStatus": Xldv20AvailStatus,
       "Xldv20LinkState": Xldv20LinkState,
       "Xldv20DbuReadStatus": Xldv20DbuReadStatus,
       "Xldv20TelnetAccess": Xldv20TelnetAccess,
       "Xldv20TvTelnetSessionStatus": Xldv20TvTelnetSessionStatus,
       "Xldv20EndpointType": Xldv20EndpointType,
       "Xldv20RstResult": Xldv20RstResult,
       "Xldv20ImaGroupState": Xldv20ImaGroupState,
       "Xldv20ImaGroupFailureStatus": Xldv20ImaGroupFailureStatus,
       "Xldv20ImaGroupTxClkMode": Xldv20ImaGroupTxClkMode,
       "Xldv20ImaGroupSymmetry": Xldv20ImaGroupSymmetry,
       "Xldv20ImaFrameLength": Xldv20ImaFrameLength,
       "Xldv20ImaLinkState": Xldv20ImaLinkState,
       "Xldv20ImaLinkFailureStatus": Xldv20ImaLinkFailureStatus,
       "DisplayString": DisplayString,
       "Unsigned16": Unsigned16,
       "MilliSeconds": MilliSeconds,
       "Xldv20HwUnitType": Xldv20HwUnitType,
       "Xldv20IfType": Xldv20IfType,
       "Xldv20AlarmState": Xldv20AlarmState,
       "Xldv20SuppressionType": Xldv20SuppressionType,
       "Xldv20TrafficType": Xldv20TrafficType,
       "Xldv20TrafficDirection": Xldv20TrafficDirection,
       "Xldv20EqhType": Xldv20EqhType,
       "Xldv20LineType": Xldv20LineType,
       "Xldv20S1nS3nEberThreshold": Xldv20S1nS3nEberThreshold,
       "Xldv20S1nS3nSDThreshold": Xldv20S1nS3nSDThreshold,
       "Xldv20AlarmSeverity": Xldv20AlarmSeverity,
       "Xldv20AlmSevProfileIndex": Xldv20AlmSevProfileIndex,
       "Xldv20AlmFiltProfileIndex": Xldv20AlmFiltProfileIndex,
       "Xldv20RiResultType": Xldv20RiResultType,
       "Xldv20RowStatus": Xldv20RowStatus,
       "Xldv20CodingType": Xldv20CodingType,
       "Xldv20ExtAlarmActivityState": Xldv20ExtAlarmActivityState,
       "Xldv20EmptyCellType": Xldv20EmptyCellType,
       "Xldv20LogType": Xldv20LogType,
       "Xldv20SucAllOfType": Xldv20SucAllOfType,
       "Xldv20ResetLevel": Xldv20ResetLevel,
       "Xldv20VdcRateDn": Xldv20VdcRateDn,
       "Xldv20VdcRateUp": Xldv20VdcRateUp,
       "Xldv20VdcLatencyDn": Xldv20VdcLatencyDn,
       "Xldv20VdcLatencyUp": Xldv20VdcLatencyUp,
       "Xldv20VdcPowerBoostAdaptationType": Xldv20VdcPowerBoostAdaptationType,
       "Xldv20VdcVdslMode": Xldv20VdcVdslMode,
       "Xldv20VdcPsdMask": Xldv20VdcPsdMask,
       "Xldv20EthNtMode": Xldv20EthNtMode,
       "Xldv20E3nPayloadType": Xldv20E3nPayloadType,
       "Xldv20CallpAlarmState": Xldv20CallpAlarmState,
       "Xldv20TpAlarmState": Xldv20TpAlarmState,
       "Xldv20Latency": Xldv20Latency,
       "Xldv20TestType": Xldv20TestType,
       "Xldv20FlowDirection": Xldv20FlowDirection,
       "Xldv20OamLevel": Xldv20OamLevel,
       "Xldv20TrapIds": Xldv20TrapIds,
       "Xldv20Requester": Xldv20Requester,
       "Xldv20TimeZone": Xldv20TimeZone,
       "Xldv20DayLightSavingTime": Xldv20DayLightSavingTime,
       "Xldv20AdslMargin": Xldv20AdslMargin,
       "Xldv20AdslAttenuation": Xldv20AdslAttenuation,
       "Xldv20AdslMinMargin": Xldv20AdslMinMargin,
       "Xldv20AdslOutputPower": Xldv20AdslOutputPower,
       "Xldv20StartupResult": Xldv20StartupResult,
       "Xldv20StartupType": Xldv20StartupType,
       "Xldv20SnmLctSession": Xldv20SnmLctSession,
       "Xldv20RepSource": Xldv20RepSource,
       "Xldv20PollingFlagType": Xldv20PollingFlagType,
       "Xldv20TerminalType": Xldv20TerminalType,
       "Xldv20ChannelType": Xldv20ChannelType,
       "Xldv20XdslServiceType": Xldv20XdslServiceType,
       "Xldv20XdslServiceTypeCurrent": Xldv20XdslServiceTypeCurrent,
       "Xldv20LoopMode": Xldv20LoopMode,
       "Xldv20XdslInitStatus": Xldv20XdslInitStatus,
       "Xldv20AdcTrainingMode": Xldv20AdcTrainingMode,
       "Xldv20SdslServiceType": Xldv20SdslServiceType,
       "Xldv20AdslDataRateDown": Xldv20AdslDataRateDown,
       "Xldv20AdslDataRateUp": Xldv20AdslDataRateUp,
       "Xldv20AdslDataRateDownCurrent": Xldv20AdslDataRateDownCurrent,
       "Xldv20AdslDataRateUpCurrent": Xldv20AdslDataRateUpCurrent,
       "Xldv20SdslDataRate": Xldv20SdslDataRate,
       "Xldv20SdslDataRateCurrent": Xldv20SdslDataRateCurrent,
       "Xldv20ControlReq": Xldv20ControlReq,
       "xldv20": xldv20,
       "xldv20SnmpMgmt": xldv20SnmpMgmt,
       "xldv20SnmpControl": xldv20SnmpControl,
       "xldv20SnmTmnTrapFlowControl": xldv20SnmTmnTrapFlowControl,
       "xldv20SnmLctTrapFlowControl": xldv20SnmLctTrapFlowControl,
       "xldv20SnmControlReq": xldv20SnmControlReq,
       "xldv20SnmControlStatus": xldv20SnmControlStatus,
       "xldv20SnmLctConnected": xldv20SnmLctConnected,
       "xldv20SnmTmnConnected": xldv20SnmTmnConnected,
       "xldv20SnmMaxResponseTime": xldv20SnmMaxResponseTime,
       "xldv20SnmTmnMaxNumber": xldv20SnmTmnMaxNumber,
       "xldv20SnmTmnSpecificIndex": xldv20SnmTmnSpecificIndex,
       "xldv20SnmCallpPollingFlag": xldv20SnmCallpPollingFlag,
       "xldv20SnmLctSessionPollingFlag": xldv20SnmLctSessionPollingFlag,
       "xldv20SnmControlReqResult": xldv20SnmControlReqResult,
       "xldv20SnmStartupResult": xldv20SnmStartupResult,
       "xldv20SnmControlTimeStamp": xldv20SnmControlTimeStamp,
       "xldv20TmnTable": xldv20TmnTable,
       "xldv20TmnEntry": xldv20TmnEntry,
       "xldv20TmnIndex": xldv20TmnIndex,
       "xldv20TmnOrLctTerminal": xldv20TmnOrLctTerminal,
       "xldv20TmnInOrOutBand": xldv20TmnInOrOutBand,
       "xldv20TmnConnected": xldv20TmnConnected,
       "xldv20TmnTrapFlowControl": xldv20TmnTrapFlowControl,
       "xldv20TmnLctSessionPollingFlag": xldv20TmnLctSessionPollingFlag,
       "xldv20CallP": xldv20CallP,
       "xldv20AtmCcControl": xldv20AtmCcControl,
       "xldv20ActOperationalState": xldv20ActOperationalState,
       "xldv20ActControlReq": xldv20ActControlReq,
       "xldv20ActControlStatus": xldv20ActControlStatus,
       "xldv20ActVpiNni": xldv20ActVpiNni,
       "xldv20ActVpiUni": xldv20ActVpiUni,
       "xldv20ActVciNni": xldv20ActVciNni,
       "xldv20ActVciUni": xldv20ActVciUni,
       "xldv20ActIfIndex": xldv20ActIfIndex,
       "xldv20ActPeakCellRateUpstream": xldv20ActPeakCellRateUpstream,
       "xldv20ActPeakCellRateDownstream": xldv20ActPeakCellRateDownstream,
       "xldv20ActCellDelayVariationToleranceUpstream": xldv20ActCellDelayVariationToleranceUpstream,
       "xldv20ActCellDelayVariationToleranceDownstream": xldv20ActCellDelayVariationToleranceDownstream,
       "xldv20ActTrafficType": xldv20ActTrafficType,
       "xldv20ActTrafficDirection": xldv20ActTrafficDirection,
       "xldv20ActSustainableCellRateUpstream": xldv20ActSustainableCellRateUpstream,
       "xldv20ActSustainableCellRateDownstream": xldv20ActSustainableCellRateDownstream,
       "xldv20ActMaximumBurstSizeUpstream": xldv20ActMaximumBurstSizeUpstream,
       "xldv20ActMaximumBurstSizeDownstream": xldv20ActMaximumBurstSizeDownstream,
       "xldv20ActSegmentEndPointNni": xldv20ActSegmentEndPointNni,
       "xldv20ActSegmentEndPointUni": xldv20ActSegmentEndPointUni,
       "xldv20ActEthMode": xldv20ActEthMode,
       "xldv20ActEthE164Isp": xldv20ActEthE164Isp,
       "xldv20ActEthIpAddressNt": xldv20ActEthIpAddressNt,
       "xldv20ActEthIpAddressSubnetMaskNt": xldv20ActEthIpAddressSubnetMaskNt,
       "xldv20ActEthIpAddressCo": xldv20ActEthIpAddressCo,
       "xldv20ActEthIpAddressSubnetMaskCo": xldv20ActEthIpAddressSubnetMaskCo,
       "xldv20ActEthIpAddressRemoteRouter": xldv20ActEthIpAddressRemoteRouter,
       "xldv20ActTestTypeNni": xldv20ActTestTypeNni,
       "xldv20ActContinuityCheckNni": xldv20ActContinuityCheckNni,
       "xldv20ActEndpointTypeNni": xldv20ActEndpointTypeNni,
       "xldv20ActTestTypeUni": xldv20ActTestTypeUni,
       "xldv20ActContinuityCheckUni": xldv20ActContinuityCheckUni,
       "xldv20ActEndpointTypeUni": xldv20ActEndpointTypeUni,
       "xldv20ActControlReqResult": xldv20ActControlReqResult,
       "xldv20ActInbandVpi": xldv20ActInbandVpi,
       "xldv20ActInbandVci": xldv20ActInbandVci,
       "xldv20ActCallpTableIndex": xldv20ActCallpTableIndex,
       "xldv20ActMaxVciValue": xldv20ActMaxVciValue,
       "xldv20ActVbrCDVTUpstream": xldv20ActVbrCDVTUpstream,
       "xldv20ActVbrCDVTDownstream": xldv20ActVbrCDVTDownstream,
       "xldv20ActControlTimeStamp": xldv20ActControlTimeStamp,
       "xldv20ActSegmentEndPointNt": xldv20ActSegmentEndPointNt,
       "xldv20ActTestTypeNt": xldv20ActTestTypeNt,
       "xldv20ActContinuityCheckNt": xldv20ActContinuityCheckNt,
       "xldv20ActEndpointTypeNt": xldv20ActEndpointTypeNt,
       "xldv20ActCDVTAutoConfig": xldv20ActCDVTAutoConfig,
       "xldv20AtmCrossConnectTable": xldv20AtmCrossConnectTable,
       "xldv20AtmCrossConnectEntry": xldv20AtmCrossConnectEntry,
       "xldv20AccOperationalState": xldv20AccOperationalState,
       "xldv20AccTerminationPointA": xldv20AccTerminationPointA,
       "xldv20AccTerminationPointZ": xldv20AccTerminationPointZ,
       "xldv20AccLineIndex": xldv20AccLineIndex,
       "xldv20AccEthVpcIndex": xldv20AccEthVpcIndex,
       "xldv20AccEthVccIndex": xldv20AccEthVccIndex,
       "xldv20AccVpiNniIndex": xldv20AccVpiNniIndex,
       "xldv20AccAlarmState": xldv20AccAlarmState,
       "xldv20AccAdminState": xldv20AccAdminState,
       "xldv20AccAtmfVplIndex": xldv20AccAtmfVplIndex,
       "xldv20VplTpTable": xldv20VplTpTable,
       "xldv20VplTpEntry": xldv20VplTpEntry,
       "xldv20VplOperationalState": xldv20VplOperationalState,
       "xldv20VplVpiValue": xldv20VplVpiValue,
       "xldv20VplHwUnitIndex": xldv20VplHwUnitIndex,
       "xldv20VplIfIndex": xldv20VplIfIndex,
       "xldv20VplPeakCellRateUpstream": xldv20VplPeakCellRateUpstream,
       "xldv20VplPeakCellRateDownstream": xldv20VplPeakCellRateDownstream,
       "xldv20VplCellDelayVariationToleranceUpstream": xldv20VplCellDelayVariationToleranceUpstream,
       "xldv20VplCellDelayVariationToleranceDownstream": xldv20VplCellDelayVariationToleranceDownstream,
       "xldv20VplTrafficType": xldv20VplTrafficType,
       "xldv20VplTrafficDirection": xldv20VplTrafficDirection,
       "xldv20VplConnectivityPointer": xldv20VplConnectivityPointer,
       "xldv20VplLineIndex": xldv20VplLineIndex,
       "xldv20VplSegmentEndPoint": xldv20VplSegmentEndPoint,
       "xldv20VplSustainableCellRateUpstream": xldv20VplSustainableCellRateUpstream,
       "xldv20VplSustainableCellRateDownstream": xldv20VplSustainableCellRateDownstream,
       "xldv20VplMaximumBurstSizeUpstream": xldv20VplMaximumBurstSizeUpstream,
       "xldv20VplMaximumBurstSizeDownstream": xldv20VplMaximumBurstSizeDownstream,
       "xldv20VplAlarmSeverityIndex": xldv20VplAlarmSeverityIndex,
       "xldv20VplAlarmFilteringIndex": xldv20VplAlarmFilteringIndex,
       "xldv20VplCvpIndexSegment": xldv20VplCvpIndexSegment,
       "xldv20VplIndex": xldv20VplIndex,
       "xldv20VplLOCAlarm": xldv20VplLOCAlarm,
       "xldv20VplVbrCDVTUpstream": xldv20VplVbrCDVTUpstream,
       "xldv20VplVbrCDVTDownstream": xldv20VplVbrCDVTDownstream,
       "xldv20VpcTpTable": xldv20VpcTpTable,
       "xldv20VpcTpEntry": xldv20VpcTpEntry,
       "xldv20VpcOperationalState": xldv20VpcOperationalState,
       "xldv20VpcVpiValue": xldv20VpcVpiValue,
       "xldv20VpcHwUnitIndex": xldv20VpcHwUnitIndex,
       "xldv20VpcIfIndex": xldv20VpcIfIndex,
       "xldv20VpcPeakCellRateUpstream": xldv20VpcPeakCellRateUpstream,
       "xldv20VpcPeakCellRateDownstream": xldv20VpcPeakCellRateDownstream,
       "xldv20VpcCellDelayVariationToleranceUpstream": xldv20VpcCellDelayVariationToleranceUpstream,
       "xldv20VpcCellDelayVariationToleranceDownstream": xldv20VpcCellDelayVariationToleranceDownstream,
       "xldv20VpcTrafficType": xldv20VpcTrafficType,
       "xldv20VpcTrafficDirection": xldv20VpcTrafficDirection,
       "xldv20VpcLineIndex": xldv20VpcLineIndex,
       "xldv20VpcSegmentEndPoint": xldv20VpcSegmentEndPoint,
       "xldv20VpcSustainableCellRateUpstream": xldv20VpcSustainableCellRateUpstream,
       "xldv20VpcSustainableCellRateDownstream": xldv20VpcSustainableCellRateDownstream,
       "xldv20VpcMaximumBurstSizeUpstream": xldv20VpcMaximumBurstSizeUpstream,
       "xldv20VpcMaximumBurstSizeDownstream": xldv20VpcMaximumBurstSizeDownstream,
       "xldv20VpcAlarmSeverityIndex": xldv20VpcAlarmSeverityIndex,
       "xldv20VpcAlarmFilteringIndex": xldv20VpcAlarmFilteringIndex,
       "xldv20VpcCvpIndexSegment": xldv20VpcCvpIndexSegment,
       "xldv20VpcCvpIndexEndToEnd": xldv20VpcCvpIndexEndToEnd,
       "xldv20VpcIndex": xldv20VpcIndex,
       "xldv20VpcAISAlarm": xldv20VpcAISAlarm,
       "xldv20VpcRDIAlarm": xldv20VpcRDIAlarm,
       "xldv20VpcLOCAlarm": xldv20VpcLOCAlarm,
       "xldv20VpcNumberOfVcs": xldv20VpcNumberOfVcs,
       "xldv20VpcVbrCDVTUpstream": xldv20VpcVbrCDVTUpstream,
       "xldv20VpcVbrCDVTDownstream": xldv20VpcVbrCDVTDownstream,
       "xldv20VpcEmSpecific": xldv20VpcEmSpecific,
       "xldv20VpcEthVpcIndex": xldv20VpcEthVpcIndex,
       "xldv20VpcAtmfVplIndex": xldv20VpcAtmfVplIndex,
       "xldv20VccTpTable": xldv20VccTpTable,
       "xldv20VccTpEntry": xldv20VccTpEntry,
       "xldv20VccOperationalState": xldv20VccOperationalState,
       "xldv20VccVciValue": xldv20VccVciValue,
       "xldv20VccVpcIndex": xldv20VccVpcIndex,
       "xldv20VccHwUnitIndex": xldv20VccHwUnitIndex,
       "xldv20VccAlarmSeverityIndex": xldv20VccAlarmSeverityIndex,
       "xldv20VccAlarmFilteringIndex": xldv20VccAlarmFilteringIndex,
       "xldv20VccLineIndex": xldv20VccLineIndex,
       "xldv20VccIndex": xldv20VccIndex,
       "xldv20VccAISAlarm": xldv20VccAISAlarm,
       "xldv20VccRDIAlarm": xldv20VccRDIAlarm,
       "xldv20VccLOCAlarm": xldv20VccLOCAlarm,
       "xldv20VccCvcIndexSegment": xldv20VccCvcIndexSegment,
       "xldv20VccCvcIndexEndToEnd": xldv20VccCvcIndexEndToEnd,
       "xldv20VcCrossConnectTable": xldv20VcCrossConnectTable,
       "xldv20VcCrossConnectEntry": xldv20VcCrossConnectEntry,
       "xldv20VcxOperationalState": xldv20VcxOperationalState,
       "xldv20VcxTerminationPointA": xldv20VcxTerminationPointA,
       "xldv20VcxTerminationPointZ": xldv20VcxTerminationPointZ,
       "xldv20VcxLineIndex": xldv20VcxLineIndex,
       "xldv20VcxEthVpcIndex": xldv20VcxEthVpcIndex,
       "xldv20VcxEthVccIndex": xldv20VcxEthVccIndex,
       "xldv20VcxVpcNniIndex": xldv20VcxVpcNniIndex,
       "xldv20VcxVpcUniIndex": xldv20VcxVpcUniIndex,
       "xldv20VcxIndex": xldv20VcxIndex,
       "xldv20VcxAlarmState": xldv20VcxAlarmState,
       "xldv20VcxAdminState": xldv20VcxAdminState,
       "xldv20VcxAtmfVplIndex": xldv20VcxAtmfVplIndex,
       "xldv20VclTpTable": xldv20VclTpTable,
       "xldv20VclTpEntry": xldv20VclTpEntry,
       "xldv20VclOperationalState": xldv20VclOperationalState,
       "xldv20VclVpiValue": xldv20VclVpiValue,
       "xldv20VclVciValue": xldv20VclVciValue,
       "xldv20VclHwUnitIndex": xldv20VclHwUnitIndex,
       "xldv20VclIfIndex": xldv20VclIfIndex,
       "xldv20VclPeakCellRateUpstream": xldv20VclPeakCellRateUpstream,
       "xldv20VclPeakCellRateDownstream": xldv20VclPeakCellRateDownstream,
       "xldv20VclCellDelayVariationToleranceUpstream": xldv20VclCellDelayVariationToleranceUpstream,
       "xldv20VclCellDelayVariationToleranceDownstream": xldv20VclCellDelayVariationToleranceDownstream,
       "xldv20VclTrafficType": xldv20VclTrafficType,
       "xldv20VclTrafficDirection": xldv20VclTrafficDirection,
       "xldv20VclConnectivityPointer": xldv20VclConnectivityPointer,
       "xldv20VclLineIndex": xldv20VclLineIndex,
       "xldv20VclSegmentEndPoint": xldv20VclSegmentEndPoint,
       "xldv20VclSustainableCellRateUpstream": xldv20VclSustainableCellRateUpstream,
       "xldv20VclSustainableCellRateDownstream": xldv20VclSustainableCellRateDownstream,
       "xldv20VclMaximumBurstSizeUpstream": xldv20VclMaximumBurstSizeUpstream,
       "xldv20VclMaximumBurstSizeDownstream": xldv20VclMaximumBurstSizeDownstream,
       "xldv20VclAlarmSeverityIndex": xldv20VclAlarmSeverityIndex,
       "xldv20VclAlarmFilteringIndex": xldv20VclAlarmFilteringIndex,
       "xldv20VclCvcIndexSegment": xldv20VclCvcIndexSegment,
       "xldv20VclIndex": xldv20VclIndex,
       "xldv20VclLOCAlarm": xldv20VclLOCAlarm,
       "xldv20VclVpcIndex": xldv20VclVpcIndex,
       "xldv20VclVbrCDVTUpstream": xldv20VclVbrCDVTUpstream,
       "xldv20VclVbrCDVTDownstream": xldv20VclVbrCDVTDownstream,
       "xldv20EthernetConfigTable": xldv20EthernetConfigTable,
       "xldv20EthernetConfigEntry": xldv20EthernetConfigEntry,
       "xldv20EthMode": xldv20EthMode,
       "xldv20EthE164Isp": xldv20EthE164Isp,
       "xldv20EthIpAddressNt": xldv20EthIpAddressNt,
       "xldv20EthIpAddressSubnetMaskNt": xldv20EthIpAddressSubnetMaskNt,
       "xldv20EthIpAddressCo": xldv20EthIpAddressCo,
       "xldv20EthIpAddressSubnetMaskCo": xldv20EthIpAddressSubnetMaskCo,
       "xldv20EthIpAddressRemoteRouter": xldv20EthIpAddressRemoteRouter,
       "xldv20ContinuityCheckVpTable": xldv20ContinuityCheckVpTable,
       "xldv20ContinuityCheckVpEntry": xldv20ContinuityCheckVpEntry,
       "xldv20CvpIndex": xldv20CvpIndex,
       "xldv20CvpEndpointType": xldv20CvpEndpointType,
       "xldv20CvpTestType": xldv20CvpTestType,
       "xldv20CvpOperationalState": xldv20CvpOperationalState,
       "xldv20CvpVpTpIndex": xldv20CvpVpTpIndex,
       "xldv20CvpObjectType": xldv20CvpObjectType,
       "xldv20ContinuityCheckVcTable": xldv20ContinuityCheckVcTable,
       "xldv20ContinuityCheckVcEntry": xldv20ContinuityCheckVcEntry,
       "xldv20CvcIndex": xldv20CvcIndex,
       "xldv20CvcEndpointType": xldv20CvcEndpointType,
       "xldv20CvcTestType": xldv20CvcTestType,
       "xldv20CvcOperationalState": xldv20CvcOperationalState,
       "xldv20CvcVcTpIndex": xldv20CvcVcTpIndex,
       "xldv20CvcObjectType": xldv20CvcObjectType,
       "xldv20ContinuityCheckControl": xldv20ContinuityCheckControl,
       "xldv20CocControlReq": xldv20CocControlReq,
       "xldv20CocControlStatus": xldv20CocControlStatus,
       "xldv20CocEndpointType": xldv20CocEndpointType,
       "xldv20CocObjectType": xldv20CocObjectType,
       "xldv20CocTestType": xldv20CocTestType,
       "xldv20CocIndex": xldv20CocIndex,
       "xldv20CocControlReqResult": xldv20CocControlReqResult,
       "xldv20CocControlTimeStamp": xldv20CocControlTimeStamp,
       "xldv20InbandTmn": xldv20InbandTmn,
       "xldv20InbandVpiCurrent": xldv20InbandVpiCurrent,
       "xldv20InbandVciCurrent": xldv20InbandVciCurrent,
       "xldv20InbandVpiConfig": xldv20InbandVpiConfig,
       "xldv20InbandVciConfig": xldv20InbandVciConfig,
       "xldv20Hwm": xldv20Hwm,
       "xldv20AtmNe": xldv20AtmNe,
       "xldv20NeLocation": xldv20NeLocation,
       "xldv20NeVendor": xldv20NeVendor,
       "xldv20NeVersion": xldv20NeVersion,
       "xldv20NeExternalTime": xldv20NeExternalTime,
       "xldv20NeTimeZone": xldv20NeTimeZone,
       "xldv20NeDescriptorFileName": xldv20NeDescriptorFileName,
       "xldv20NeExternalTime45020": xldv20NeExternalTime45020,
       "xldv20NeSummerTime": xldv20NeSummerTime,
       "xldv20HwUnitTable": xldv20HwUnitTable,
       "xldv20HwUnitEntry": xldv20HwUnitEntry,
       "xldv20HwUnitIndex": xldv20HwUnitIndex,
       "xldv20HwUnitType": xldv20HwUnitType,
       "xldv20HwContainmentTable": xldv20HwContainmentTable,
       "xldv20HwContainmentEntry": xldv20HwContainmentEntry,
       "xldv20HwContainingUnitIndex": xldv20HwContainingUnitIndex,
       "xldv20HwContainedUnitAddr": xldv20HwContainedUnitAddr,
       "xldv20HwContainedUnitIndex": xldv20HwContainedUnitIndex,
       "xldv20HwEquipTable": xldv20HwEquipTable,
       "xldv20HwEquipEntry": xldv20HwEquipEntry,
       "xldv20EquType": xldv20EquType,
       "xldv20EquLocation": xldv20EquLocation,
       "xldv20EquUserLabel": xldv20EquUserLabel,
       "xldv20EquConnectedPiuIndex": xldv20EquConnectedPiuIndex,
       "xldv20EquConnectedPiuPort": xldv20EquConnectedPiuPort,
       "xldv20HwEquipHolderTable": xldv20HwEquipHolderTable,
       "xldv20HwEquipHolderEntry": xldv20HwEquipHolderEntry,
       "xldv20EqhType": xldv20EqhType,
       "xldv20EqhAccPiuTypes": xldv20EqhAccPiuTypes,
       "xldv20EqhSlotStatus": xldv20EqhSlotStatus,
       "xldv20EqhSwVersion": xldv20EqhSwVersion,
       "xldv20EqhMnemoCode": xldv20EqhMnemoCode,
       "xldv20EqhFwCode": xldv20EqhFwCode,
       "xldv20EqhRiMnemoCode": xldv20EqhRiMnemoCode,
       "xldv20EqhRiFwItemNumber": xldv20EqhRiFwItemNumber,
       "xldv20EqhRiFwIssue": xldv20EqhRiFwIssue,
       "xldv20EqhRiHwItemNumber": xldv20EqhRiHwItemNumber,
       "xldv20EqhRiHwIssue": xldv20EqhRiHwIssue,
       "xldv20EqhRiSerialNumber": xldv20EqhRiSerialNumber,
       "xldv20HwPlugInUnitTable": xldv20HwPlugInUnitTable,
       "xldv20HwPlugInUnitEntry": xldv20HwPlugInUnitEntry,
       "xldv20PiuAdminState": xldv20PiuAdminState,
       "xldv20PiuAvailStatus": xldv20PiuAvailStatus,
       "xldv20PiuOperState": xldv20PiuOperState,
       "xldv20PiuType": xldv20PiuType,
       "xldv20PiuAlarmSeverityIndex": xldv20PiuAlarmSeverityIndex,
       "xldv20PiuAlarmFilteringIndex": xldv20PiuAlarmFilteringIndex,
       "xldv20PiuUpgradeResult": xldv20PiuUpgradeResult,
       "xldv20HwuControl": xldv20HwuControl,
       "xldv20HwuControlReq": xldv20HwuControlReq,
       "xldv20HwuControlStatus": xldv20HwuControlStatus,
       "xldv20HwuUnitType": xldv20HwuUnitType,
       "xldv20HwuEquType": xldv20HwuEquType,
       "xldv20HwuEqhType": xldv20HwuEqhType,
       "xldv20HwuPiuType": xldv20HwuPiuType,
       "xldv20HwuContainingUnitIndex": xldv20HwuContainingUnitIndex,
       "xldv20HwuContainedUnitAddr": xldv20HwuContainedUnitAddr,
       "xldv20HwuUnitIndex": xldv20HwuUnitIndex,
       "xldv20HwuControlTimer": xldv20HwuControlTimer,
       "xldv20HwuControlReqResult": xldv20HwuControlReqResult,
       "xldv20HwuControlTimeStamp": xldv20HwuControlTimeStamp,
       "xldv20RemoteInventory": xldv20RemoteInventory,
       "xldv20RiControlReq": xldv20RiControlReq,
       "xldv20RiControlStatus": xldv20RiControlStatus,
       "xldv20RiControlTimer": xldv20RiControlTimer,
       "xldv20RiResultFilePath": xldv20RiResultFilePath,
       "xldv20RiHwUnitIndex": xldv20RiHwUnitIndex,
       "xldv20RiControlReqResult": xldv20RiControlReqResult,
       "xldv20RiControlTimeStamp": xldv20RiControlTimeStamp,
       "xldv20HwUnitMappingTable": xldv20HwUnitMappingTable,
       "xldv20HwUnitMappingEntry": xldv20HwUnitMappingEntry,
       "xldv20HwmHwUnitIndex": xldv20HwmHwUnitIndex,
       "xldv20HwmIfIndex": xldv20HwmIfIndex,
       "xldv20Tlm": xldv20Tlm,
       "xldv20IfTable": xldv20IfTable,
       "xldv20IfEntry": xldv20IfEntry,
       "xldv20IfIndex": xldv20IfIndex,
       "xldv20IfType": xldv20IfType,
       "xldv20IfLineIndex": xldv20IfLineIndex,
       "xldv20IfHwUnitIndex": xldv20IfHwUnitIndex,
       "xldv20IfHwPortId": xldv20IfHwPortId,
       "xldv20IfConnectivityIndex": xldv20IfConnectivityIndex,
       "xldv20IfOperState": xldv20IfOperState,
       "xldv20IfAdminState": xldv20IfAdminState,
       "xldv20IfAlarmState": xldv20IfAlarmState,
       "xldv20IfAlarmSeverityIndex": xldv20IfAlarmSeverityIndex,
       "xldv20IfAlarmFilteringIndex": xldv20IfAlarmFilteringIndex,
       "xldv20AdcControl": xldv20AdcControl,
       "xldv20AdcCtrlControlReq": xldv20AdcCtrlControlReq,
       "xldv20AdcCtrlControlStatus": xldv20AdcCtrlControlStatus,
       "xldv20AdcCtrlIfIndex": xldv20AdcCtrlIfIndex,
       "xldv20AdcCtrlMinRateDn": xldv20AdcCtrlMinRateDn,
       "xldv20AdcCtrlMinRateUp": xldv20AdcCtrlMinRateUp,
       "xldv20AdcCtrlMaxRateDn": xldv20AdcCtrlMaxRateDn,
       "xldv20AdcCtrlMaxRateUp": xldv20AdcCtrlMaxRateUp,
       "xldv20AdcCtrlMarginDn": xldv20AdcCtrlMarginDn,
       "xldv20AdcCtrlMarginUp": xldv20AdcCtrlMarginUp,
       "xldv20AdcCtrlLatencyDn": xldv20AdcCtrlLatencyDn,
       "xldv20AdcCtrlLatencyUp": xldv20AdcCtrlLatencyUp,
       "xldv20AdcCtrlMinMarginDn": xldv20AdcCtrlMinMarginDn,
       "xldv20AdcCtrlMinMarginUp": xldv20AdcCtrlMinMarginUp,
       "xldv20AdcCtrlControlReqResult": xldv20AdcCtrlControlReqResult,
       "xldv20AdcCtrlXdslServiceType": xldv20AdcCtrlXdslServiceType,
       "xldv20AdcCtrlControlTimeStamp": xldv20AdcCtrlControlTimeStamp,
       "xldv20AdcCtrlTrainingMode": xldv20AdcCtrlTrainingMode,
       "xldv20VdcControl": xldv20VdcControl,
       "xldv20VdcCtrlControlReq": xldv20VdcCtrlControlReq,
       "xldv20VdcCtrlControlStatus": xldv20VdcCtrlControlStatus,
       "xldv20VdcCtrlIfIndex": xldv20VdcCtrlIfIndex,
       "xldv20VdcCtrlMinRateDn": xldv20VdcCtrlMinRateDn,
       "xldv20VdcCtrlMinRateUp": xldv20VdcCtrlMinRateUp,
       "xldv20VdcCtrlMaxRateDn": xldv20VdcCtrlMaxRateDn,
       "xldv20VdcCtrlMaxRateUp": xldv20VdcCtrlMaxRateUp,
       "xldv20VdcCtrlLatencyDn": xldv20VdcCtrlLatencyDn,
       "xldv20VdcCtrlLatencyUp": xldv20VdcCtrlLatencyUp,
       "xldv20VdcCtrlPowerBoost": xldv20VdcCtrlPowerBoost,
       "xldv20VdcCtrlWarmStart": xldv20VdcCtrlWarmStart,
       "xldv20VdcCtrlVdslMode": xldv20VdcCtrlVdslMode,
       "xldv20VdcCtrlSleepMode": xldv20VdcCtrlSleepMode,
       "xldv20VdcCtrlPsdMask": xldv20VdcCtrlPsdMask,
       "xldv20VdcCtrlPowerAdaptation": xldv20VdcCtrlPowerAdaptation,
       "xldv20VdcCtrlControlReqResult": xldv20VdcCtrlControlReqResult,
       "xldv20VdcCtrlControlTimeStamp": xldv20VdcCtrlControlTimeStamp,
       "xldv20AdcPPTPTable": xldv20AdcPPTPTable,
       "xldv20AdcPPTPEntry": xldv20AdcPPTPEntry,
       "xldv20AdcMinRateDnCfg": xldv20AdcMinRateDnCfg,
       "xldv20AdcMinRateUpCfg": xldv20AdcMinRateUpCfg,
       "xldv20AdcMaxRateDnCfg": xldv20AdcMaxRateDnCfg,
       "xldv20AdcMaxRateUpCfg": xldv20AdcMaxRateUpCfg,
       "xldv20AdcMarginDnCfg": xldv20AdcMarginDnCfg,
       "xldv20AdcMarginUpCfg": xldv20AdcMarginUpCfg,
       "xldv20AdcMinMarginDnCfg": xldv20AdcMinMarginDnCfg,
       "xldv20AdcMinMarginUpCfg": xldv20AdcMinMarginUpCfg,
       "xldv20AdcLatencyDnCfg": xldv20AdcLatencyDnCfg,
       "xldv20AdcLatencyUpCfg": xldv20AdcLatencyUpCfg,
       "xldv20AdcRateDn": xldv20AdcRateDn,
       "xldv20AdcRateUp": xldv20AdcRateUp,
       "xldv20AdcMarginDn": xldv20AdcMarginDn,
       "xldv20AdcMarginUp": xldv20AdcMarginUp,
       "xldv20AdcAttenuationDn": xldv20AdcAttenuationDn,
       "xldv20AdcAttenuationUp": xldv20AdcAttenuationUp,
       "xldv20AdcLinkState": xldv20AdcLinkState,
       "xldv20AdcAISOnLOS": xldv20AdcAISOnLOS,
       "xldv20AdcAISOnACT": xldv20AdcAISOnACT,
       "xldv20AdcGuaranteedBandwidthUsage": xldv20AdcGuaranteedBandwidthUsage,
       "xldv20AdcXdslServiceTypeCfg": xldv20AdcXdslServiceTypeCfg,
       "xldv20AdcInitStatus": xldv20AdcInitStatus,
       "xldv20AdcTransceiverOutputPower": xldv20AdcTransceiverOutputPower,
       "xldv20AdcFirstUsedSubCarrierUpstream": xldv20AdcFirstUsedSubCarrierUpstream,
       "xldv20AdcFirstUsedSubCarrierDownstream": xldv20AdcFirstUsedSubCarrierDownstream,
       "xldv20AdcLastUsedSubCarrierUpstream": xldv20AdcLastUsedSubCarrierUpstream,
       "xldv20AdcLastUsedSubCarrierDownstream": xldv20AdcLastUsedSubCarrierDownstream,
       "xldv20AdcXdslServiceType": xldv20AdcXdslServiceType,
       "xldv20VdcPPTPTable": xldv20VdcPPTPTable,
       "xldv20VdcPPTPEntry": xldv20VdcPPTPEntry,
       "xldv20VdcMinRateDnCfg": xldv20VdcMinRateDnCfg,
       "xldv20VdcMinRateUpCfg": xldv20VdcMinRateUpCfg,
       "xldv20VdcMaxRateDnCfg": xldv20VdcMaxRateDnCfg,
       "xldv20VdcMaxRateUpCfg": xldv20VdcMaxRateUpCfg,
       "xldv20VdcLatencyDnCfg": xldv20VdcLatencyDnCfg,
       "xldv20VdcLatencyUpCfg": xldv20VdcLatencyUpCfg,
       "xldv20VdcPowerBoostCfg": xldv20VdcPowerBoostCfg,
       "xldv20VdcWarmStartCfg": xldv20VdcWarmStartCfg,
       "xldv20VdcVdslModeCfg": xldv20VdcVdslModeCfg,
       "xldv20VdcSleepModeCfg": xldv20VdcSleepModeCfg,
       "xldv20VdcPsdMaskCfg": xldv20VdcPsdMaskCfg,
       "xldv20VdcPowerAdaptationCfg": xldv20VdcPowerAdaptationCfg,
       "xldv20VdcRateDn": xldv20VdcRateDn,
       "xldv20VdcRateUp": xldv20VdcRateUp,
       "xldv20VdcMarginDn": xldv20VdcMarginDn,
       "xldv20VdcMarginUp": xldv20VdcMarginUp,
       "xldv20VdcAttenuationDn": xldv20VdcAttenuationDn,
       "xldv20VdcAttenuationUp": xldv20VdcAttenuationUp,
       "xldv20VdcLinkState": xldv20VdcLinkState,
       "xldv20VdcGuaranteedBandwidthUsage": xldv20VdcGuaranteedBandwidthUsage,
       "xldv20IbmPPTPTable": xldv20IbmPPTPTable,
       "xldv20IbmPPTPEntry": xldv20IbmPPTPEntry,
       "xldv20IbmAISOnLOS": xldv20IbmAISOnLOS,
       "xldv20IbmVpAISFiltering": xldv20IbmVpAISFiltering,
       "xldv20Ds3NePPTPTable": xldv20Ds3NePPTPTable,
       "xldv20Ds3NePPTPEntry": xldv20Ds3NePPTPEntry,
       "xldv20D3nType": xldv20D3nType,
       "xldv20D3nCodingType": xldv20D3nCodingType,
       "xldv20D3nPayloadScramblingActivate": xldv20D3nPayloadScramblingActivate,
       "xldv20D3nEmptyCellType": xldv20D3nEmptyCellType,
       "xldv20D3nBandwidthUsage": xldv20D3nBandwidthUsage,
       "xldv20E3NePPTPTable": xldv20E3NePPTPTable,
       "xldv20E3NePPTPEntry": xldv20E3NePPTPEntry,
       "xldv20E3nType": xldv20E3nType,
       "xldv20E3nCodingType": xldv20E3nCodingType,
       "xldv20E3nTrailTraceSend": xldv20E3nTrailTraceSend,
       "xldv20E3nTrailTraceSendDefault": xldv20E3nTrailTraceSendDefault,
       "xldv20E3nTrailTraceExpect": xldv20E3nTrailTraceExpect,
       "xldv20E3nTrailTraceTIMDetectionActivate": xldv20E3nTrailTraceTIMDetectionActivate,
       "xldv20E3nTrailTraceReceive": xldv20E3nTrailTraceReceive,
       "xldv20E3nEmptyCellType": xldv20E3nEmptyCellType,
       "xldv20E3nPayloadType": xldv20E3nPayloadType,
       "xldv20E3nBandwidthUsage": xldv20E3nBandwidthUsage,
       "xldv20Stm1NePPTPTable": xldv20Stm1NePPTPTable,
       "xldv20Stm1NePPTPEntry": xldv20Stm1NePPTPEntry,
       "xldv20S1nLineType": xldv20S1nLineType,
       "xldv20S1nPathTraceSend": xldv20S1nPathTraceSend,
       "xldv20S1nPathTraceSendDefault": xldv20S1nPathTraceSendDefault,
       "xldv20S1nPathTraceExpect": xldv20S1nPathTraceExpect,
       "xldv20S1nPathTraceTIMDetectionActivate": xldv20S1nPathTraceTIMDetectionActivate,
       "xldv20S1nPathTraceReceive": xldv20S1nPathTraceReceive,
       "xldv20S1nHpEberThreshold": xldv20S1nHpEberThreshold,
       "xldv20S1nMsEberThreshold": xldv20S1nMsEberThreshold,
       "xldv20S1nRsEberThreshold": xldv20S1nRsEberThreshold,
       "xldv20S1nSDThreshold": xldv20S1nSDThreshold,
       "xldv20S1nRDIAISOnEber": xldv20S1nRDIAISOnEber,
       "xldv20S1nSignalLabelReceive": xldv20S1nSignalLabelReceive,
       "xldv20S1nEmptyCellType": xldv20S1nEmptyCellType,
       "xldv20S1nBandwidthUsage": xldv20S1nBandwidthUsage,
       "xldv20Sts3NePPTPTable": xldv20Sts3NePPTPTable,
       "xldv20Sts3NePPTPEntry": xldv20Sts3NePPTPEntry,
       "xldv20S3nLineType": xldv20S3nLineType,
       "xldv20S3nPathTraceSend": xldv20S3nPathTraceSend,
       "xldv20S3nPathTraceSendDefault": xldv20S3nPathTraceSendDefault,
       "xldv20S3nPathTraceExpect": xldv20S3nPathTraceExpect,
       "xldv20S3nPathTraceTIMDetectionActivate": xldv20S3nPathTraceTIMDetectionActivate,
       "xldv20S3nPathTraceReceive": xldv20S3nPathTraceReceive,
       "xldv20S3nPathTraceSync": xldv20S3nPathTraceSync,
       "xldv20S3nPathTraceSendCRCActivate": xldv20S3nPathTraceSendCRCActivate,
       "xldv20S3nPathTraceReceiveCRCActivate": xldv20S3nPathTraceReceiveCRCActivate,
       "xldv20S3nHpEberThreshold": xldv20S3nHpEberThreshold,
       "xldv20S3nMsEberThreshold": xldv20S3nMsEberThreshold,
       "xldv20S3nRsEberThreshold": xldv20S3nRsEberThreshold,
       "xldv20S3nSDThreshold": xldv20S3nSDThreshold,
       "xldv20S3nSignalLabelReceive": xldv20S3nSignalLabelReceive,
       "xldv20S3nEmptyCellType": xldv20S3nEmptyCellType,
       "xldv20S3nBandwidthUsage": xldv20S3nBandwidthUsage,
       "xldv20Dsx1ConfigTable": xldv20Dsx1ConfigTable,
       "xldv20Dsx1ConfigEntry": xldv20Dsx1ConfigEntry,
       "xldv20Dsx1LineType": xldv20Dsx1LineType,
       "xldv20Dsx1LineCoding": xldv20Dsx1LineCoding,
       "xldv20Dsx1LoopbackConfig": xldv20Dsx1LoopbackConfig,
       "xldv20Dsx1SignalMode": xldv20Dsx1SignalMode,
       "xldv20Dsx1TransmitClockSource": xldv20Dsx1TransmitClockSource,
       "xldv20Dsx1Fdl": xldv20Dsx1Fdl,
       "xldv20SdcControl": xldv20SdcControl,
       "xldv20SdcCtrlControlReq": xldv20SdcCtrlControlReq,
       "xldv20SdcCtrlControlStatus": xldv20SdcCtrlControlStatus,
       "xldv20SdcCtrlIfIndex": xldv20SdcCtrlIfIndex,
       "xldv20SdcCtrlRate": xldv20SdcCtrlRate,
       "xldv20SdcCtrlXdslServiceType": xldv20SdcCtrlXdslServiceType,
       "xldv20SdcCtrlControlReqResult": xldv20SdcCtrlControlReqResult,
       "xldv20SdcCtrlControlTimeStamp": xldv20SdcCtrlControlTimeStamp,
       "xldv20SdcCtrlMinMarginUp": xldv20SdcCtrlMinMarginUp,
       "xldv20SdcPPTPTable": xldv20SdcPPTPTable,
       "xldv20SdcPPTPEntry": xldv20SdcPPTPEntry,
       "xldv20SdcRateCfg": xldv20SdcRateCfg,
       "xldv20SdcXdslServiceTypeCfg": xldv20SdcXdslServiceTypeCfg,
       "xldv20SdcRate": xldv20SdcRate,
       "xldv20SdcMarginDn": xldv20SdcMarginDn,
       "xldv20SdcMarginUp": xldv20SdcMarginUp,
       "xldv20SdcAttenuationDn": xldv20SdcAttenuationDn,
       "xldv20SdcAttenuationUp": xldv20SdcAttenuationUp,
       "xldv20SdcLinkState": xldv20SdcLinkState,
       "xldv20SdcAISOnLOS": xldv20SdcAISOnLOS,
       "xldv20SdcAISOnACT": xldv20SdcAISOnACT,
       "xldv20SdcGuaranteedBandwidthUsage": xldv20SdcGuaranteedBandwidthUsage,
       "xldv20SdcInitStatus": xldv20SdcInitStatus,
       "xldv20SdcMinMarginUpCfg": xldv20SdcMinMarginUpCfg,
       "xldv20SdcTransceiverOutputPower": xldv20SdcTransceiverOutputPower,
       "xldv20SdcXdslServiceType": xldv20SdcXdslServiceType,
       "xldv20TlmOam": xldv20TlmOam,
       "xldv20LoopBackPointTable": xldv20LoopBackPointTable,
       "xldv20LbpEntry": xldv20LbpEntry,
       "xldv20LbpLoopLocId": xldv20LbpLoopLocId,
       "xldv20LbpLoopMode": xldv20LbpLoopMode,
       "xldv20PhyLoopTest": xldv20PhyLoopTest,
       "xldv20PltIfIndex": xldv20PltIfIndex,
       "xldv20PltControlReq": xldv20PltControlReq,
       "xldv20PltControlStatus": xldv20PltControlStatus,
       "xldv20PltControlTimer": xldv20PltControlTimer,
       "xldv20PltControlReqResult": xldv20PltControlReqResult,
       "xldv20PltControlTimeStamp": xldv20PltControlTimeStamp,
       "xldv20AtmLoopTest": xldv20AtmLoopTest,
       "xldv20AltIfIndex": xldv20AltIfIndex,
       "xldv20AltVpi": xldv20AltVpi,
       "xldv20AltLoopLocId": xldv20AltLoopLocId,
       "xldv20AltControlReq": xldv20AltControlReq,
       "xldv20AltControlStatus": xldv20AltControlStatus,
       "xldv20AltControlTimer": xldv20AltControlTimer,
       "xldv20AltOamLevel": xldv20AltOamLevel,
       "xldv20AltLoopTestType": xldv20AltLoopTestType,
       "xldv20AltVci": xldv20AltVci,
       "xldv20AltControlReqResult": xldv20AltControlReqResult,
       "xldv20AltFlowDirection": xldv20AltFlowDirection,
       "xldv20AltControlTimeStamp": xldv20AltControlTimeStamp,
       "xldv20MultipleLoopbackResultTable": xldv20MultipleLoopbackResultTable,
       "xldv20MlbEntry": xldv20MlbEntry,
       "xldv20MlbIndex": xldv20MlbIndex,
       "xldv20MlbLoopLocId": xldv20MlbLoopLocId,
       "xldv20Alarming": xldv20Alarming,
       "xldv20ExternalAlarmsTable": xldv20ExternalAlarmsTable,
       "xldv20ExternalAlarmEntry": xldv20ExternalAlarmEntry,
       "xldv20ExtAlarmIndex": xldv20ExtAlarmIndex,
       "xldv20ExtAlarmAdminState": xldv20ExtAlarmAdminState,
       "xldv20ExtAlarmOperState": xldv20ExtAlarmOperState,
       "xldv20ExtAlarmActivityState": xldv20ExtAlarmActivityState,
       "xldv20ExtAlarmSeverityIndex": xldv20ExtAlarmSeverityIndex,
       "xldv20ExtAlarmFilteringIndex": xldv20ExtAlarmFilteringIndex,
       "xldv20ExtAlarmName": xldv20ExtAlarmName,
       "xldv20AlarmSeverityProfileTable": xldv20AlarmSeverityProfileTable,
       "xldv20AlarmSeverityProfileEntry": xldv20AlarmSeverityProfileEntry,
       "xldv20AlmSevProfileIndex": xldv20AlmSevProfileIndex,
       "xldv20AlmSevProfileRowStatus": xldv20AlmSevProfileRowStatus,
       "xldv20AlarmSeverityTable": xldv20AlarmSeverityTable,
       "xldv20AlarmSeverityEntry": xldv20AlarmSeverityEntry,
       "xldv20AlmSevTrapId": xldv20AlmSevTrapId,
       "xldv20AlmSeverity": xldv20AlmSeverity,
       "xldv20AlarmFilteringProfileTable": xldv20AlarmFilteringProfileTable,
       "xldv20AlarmFilteringProfileEntry": xldv20AlarmFilteringProfileEntry,
       "xldv20AlmFiltProfileIndex": xldv20AlmFiltProfileIndex,
       "xldv20AlmFiltProfileRowStatus": xldv20AlmFiltProfileRowStatus,
       "xldv20AlarmFilteringTable": xldv20AlarmFilteringTable,
       "xldv20AlarmFilteringEntry": xldv20AlarmFilteringEntry,
       "xldv20AlmFiltTrapId": xldv20AlmFiltTrapId,
       "xldv20AlmTempFilter": xldv20AlmTempFilter,
       "xldv20AlarmListTable": xldv20AlarmListTable,
       "xldv20AlarmListEntry": xldv20AlarmListEntry,
       "xldv20AlmIndex": xldv20AlmIndex,
       "xldv20AlmNatureOfAlarm": xldv20AlmNatureOfAlarm,
       "xldv20AlmSpecProblem": xldv20AlmSpecProblem,
       "xldv20AlmSpecProblemText": xldv20AlmSpecProblemText,
       "xldv20AlmRepEntityId": xldv20AlmRepEntityId,
       "xldv20AlmRepSource": xldv20AlmRepSource,
       "xldv20AlmFailedComponent": xldv20AlmFailedComponent,
       "xldv20AlmFailedComponentRepSource": xldv20AlmFailedComponentRepSource,
       "xldv20AlmSeverityOfFailure": xldv20AlmSeverityOfFailure,
       "xldv20AlmPropRepairAction": xldv20AlmPropRepairAction,
       "xldv20AlmTimeAndDate": xldv20AlmTimeAndDate,
       "xldv20AlmControl": xldv20AlmControl,
       "xldv20AlmControlReq": xldv20AlmControlReq,
       "xldv20AlmControlStatus": xldv20AlmControlStatus,
       "xldv20AlmControlReqResult": xldv20AlmControlReqResult,
       "xldv20AlmControlTimeStamp": xldv20AlmControlTimeStamp,
       "xldv20Reset": xldv20Reset,
       "xldv20RstControlReq": xldv20RstControlReq,
       "xldv20RstControlStatus": xldv20RstControlStatus,
       "xldv20RstLevel": xldv20RstLevel,
       "xldv20RstHwUnitIndex": xldv20RstHwUnitIndex,
       "xldv20RstControlTimer": xldv20RstControlTimer,
       "xldv20RstControlReqResult": xldv20RstControlReqResult,
       "xldv20RstControlTimeStamp": xldv20RstControlTimeStamp,
       "xldv20Swm": xldv20Swm,
       "xldv20SwmLogHandler": xldv20SwmLogHandler,
       "xldv20DbuControlReq": xldv20DbuControlReq,
       "xldv20DbuControlStatus": xldv20DbuControlStatus,
       "xldv20DbuResultFilePath": xldv20DbuResultFilePath,
       "xldv20DbuLogType": xldv20DbuLogType,
       "xldv20DbuNumEntries": xldv20DbuNumEntries,
       "xldv20DbuControlTimer": xldv20DbuControlTimer,
       "xldv20DbuControlReqResult": xldv20DbuControlReqResult,
       "xldv20DbuHwUnitIndex": xldv20DbuHwUnitIndex,
       "xldv20DbuControlTimeStamp": xldv20DbuControlTimeStamp,
       "xldv20SwmUpgradeControl": xldv20SwmUpgradeControl,
       "xldv20SucUnit": xldv20SucUnit,
       "xldv20SucAllOfType": xldv20SucAllOfType,
       "xldv20SucVersionNo": xldv20SucVersionNo,
       "xldv20SucHwUnitIndex": xldv20SucHwUnitIndex,
       "xldv20SucPathName": xldv20SucPathName,
       "xldv20SucFileName": xldv20SucFileName,
       "xldv20SucControlReq": xldv20SucControlReq,
       "xldv20SucControlStatus": xldv20SucControlStatus,
       "xldv20SucControlTimer": xldv20SucControlTimer,
       "xldv20SucNumberOfTraps": xldv20SucNumberOfTraps,
       "xldv20SucDefaultSwVersion": xldv20SucDefaultSwVersion,
       "xldv20SucPredecessorSwVersion": xldv20SucPredecessorSwVersion,
       "xldv20SucPrePredecessorSwVersion": xldv20SucPrePredecessorSwVersion,
       "xldv20SucControlReqResult": xldv20SucControlReqResult,
       "xldv20SucControlTimeStamp": xldv20SucControlTimeStamp,
       "xldv20SwUpgradeTaskTable": xldv20SwUpgradeTaskTable,
       "xldv20SutTaskTableEntry": xldv20SutTaskTableEntry,
       "xldv20SutIndex": xldv20SutIndex,
       "xldv20SutPiuType": xldv20SutPiuType,
       "xldv20SutHwUnitIndex": xldv20SutHwUnitIndex,
       "xldv20SutSwVersion": xldv20SutSwVersion,
       "xldv20SutRequester": xldv20SutRequester,
       "xldv20SutUpgradeState": xldv20SutUpgradeState,
       "xldv20SutUpgradeResult": xldv20SutUpgradeResult,
       "xldv20SutTimeStamp": xldv20SutTimeStamp,
       "xldv20StcSecureTelnetControl": xldv20StcSecureTelnetControl,
       "xldv20StcTelnetAccess": xldv20StcTelnetAccess,
       "xldv20Dbm": xldv20Dbm,
       "xldv20DbmControl": xldv20DbmControl,
       "xldv20DbmControlReq": xldv20DbmControlReq,
       "xldv20DbmControlStatus": xldv20DbmControlStatus,
       "xldv20DbmControlTimer": xldv20DbmControlTimer,
       "xldv20DbmBackupPeriod": xldv20DbmBackupPeriod,
       "xldv20DbmBackupStartTime": xldv20DbmBackupStartTime,
       "xldv20DbmControlReqResultLocal": xldv20DbmControlReqResultLocal,
       "xldv20DbmControlReqResultRemote": xldv20DbmControlReqResultRemote,
       "xldv20DbmPathAndFileName": xldv20DbmPathAndFileName,
       "xldv20DbmControlTimeStamp": xldv20DbmControlTimeStamp,
       "xldv20TlmIma": xldv20TlmIma,
       "xldv20ImaMibObjects": xldv20ImaMibObjects,
       "xldv20ImaGroupNumber": xldv20ImaGroupNumber,
       "xldv20ImaControl": xldv20ImaControl,
       "xldv20ImaControlReq": xldv20ImaControlReq,
       "xldv20ImaControlMinNumLinks": xldv20ImaControlMinNumLinks,
       "xldv20ImaControlGroupIndex": xldv20ImaControlGroupIndex,
       "xldv20ImaControlReqResult": xldv20ImaControlReqResult,
       "xldv20ImaControlTimeStamp": xldv20ImaControlTimeStamp,
       "xldv20ImaControlStatus": xldv20ImaControlStatus,
       "xldv20ImaControlTimer": xldv20ImaControlTimer,
       "xldv20ImaGroupTable": xldv20ImaGroupTable,
       "xldv20ImaGroupEntry": xldv20ImaGroupEntry,
       "xldv20ImaGroupIndex": xldv20ImaGroupIndex,
       "xldv20ImaGroupRowStatus": xldv20ImaGroupRowStatus,
       "xldv20ImaGroupIfIndex": xldv20ImaGroupIfIndex,
       "xldv20ImaGroupNeState": xldv20ImaGroupNeState,
       "xldv20ImaGroupFeState": xldv20ImaGroupFeState,
       "xldv20ImaGroupFailureStatus": xldv20ImaGroupFailureStatus,
       "xldv20ImaGroupSymmetry": xldv20ImaGroupSymmetry,
       "xldv20ImaGroupMinNumTxLinks": xldv20ImaGroupMinNumTxLinks,
       "xldv20ImaGroupMinNumRxLinks": xldv20ImaGroupMinNumRxLinks,
       "xldv20ImaGroupNeTxClkMode": xldv20ImaGroupNeTxClkMode,
       "xldv20ImaGroupFeTxClkMode": xldv20ImaGroupFeTxClkMode,
       "xldv20ImaGroupTxTimingRefLink": xldv20ImaGroupTxTimingRefLink,
       "xldv20ImaGroupRxTimingRefLink": xldv20ImaGroupRxTimingRefLink,
       "xldv20ImaGroupLastChange": xldv20ImaGroupLastChange,
       "xldv20ImaGroupTxImaId": xldv20ImaGroupTxImaId,
       "xldv20ImaGroupRxImaId": xldv20ImaGroupRxImaId,
       "xldv20ImaGroupTxFrameLength": xldv20ImaGroupTxFrameLength,
       "xldv20ImaGroupRxFrameLength": xldv20ImaGroupRxFrameLength,
       "xldv20ImaGroupDiffDelayMax": xldv20ImaGroupDiffDelayMax,
       "xldv20ImaGroupLeastDelayLink": xldv20ImaGroupLeastDelayLink,
       "xldv20ImaGroupDiffDelayMaxObs": xldv20ImaGroupDiffDelayMaxObs,
       "xldv20ImaGroupAlphaValue": xldv20ImaGroupAlphaValue,
       "xldv20ImaGroupBetaValue": xldv20ImaGroupBetaValue,
       "xldv20ImaGroupGammaValue": xldv20ImaGroupGammaValue,
       "xldv20ImaGroupRunningSecs": xldv20ImaGroupRunningSecs,
       "xldv20ImaGroupUnavailSecs": xldv20ImaGroupUnavailSecs,
       "xldv20ImaGroupNeNumFailures": xldv20ImaGroupNeNumFailures,
       "xldv20ImaGroupFeNumFailures": xldv20ImaGroupFeNumFailures,
       "xldv20ImaGroupNumTxCfgLinks": xldv20ImaGroupNumTxCfgLinks,
       "xldv20ImaGroupNumRxCfgLinks": xldv20ImaGroupNumRxCfgLinks,
       "xldv20ImaGroupNumTxActLinks": xldv20ImaGroupNumTxActLinks,
       "xldv20ImaGroupNumRxActLinks": xldv20ImaGroupNumRxActLinks,
       "xldv20ImaGroupBandwidthUsage": xldv20ImaGroupBandwidthUsage,
       "xldv20ImaGroupMappingTable": xldv20ImaGroupMappingTable,
       "xldv20ImaGroupMappingEntry": xldv20ImaGroupMappingEntry,
       "xldv20ImaGroupMappingIndex": xldv20ImaGroupMappingIndex,
       "xldv20ImaLinkTable": xldv20ImaLinkTable,
       "xldv20ImaLinkEntry": xldv20ImaLinkEntry,
       "xldv20ImaLinkRowStatus": xldv20ImaLinkRowStatus,
       "xldv20ImaLinkGroupIndex": xldv20ImaLinkGroupIndex,
       "xldv20ImaLinkNeTxState": xldv20ImaLinkNeTxState,
       "xldv20ImaLinkNeRxState": xldv20ImaLinkNeRxState,
       "xldv20ImaLinkFeTxState": xldv20ImaLinkFeTxState,
       "xldv20ImaLinkFeRxState": xldv20ImaLinkFeRxState,
       "xldv20ImaLinkNeRxFailureStatus": xldv20ImaLinkNeRxFailureStatus,
       "xldv20ImaLinkFeRxFailureStatus": xldv20ImaLinkFeRxFailureStatus,
       "xldv20ImaLinkTxLid": xldv20ImaLinkTxLid,
       "xldv20ImaLinkRxLid": xldv20ImaLinkRxLid,
       "xldv20ImaLinkImaViolations": xldv20ImaLinkImaViolations,
       "xldv20ImaLinkOifAnomalies": xldv20ImaLinkOifAnomalies,
       "xldv20ImaLinkNeSevErroredSecs": xldv20ImaLinkNeSevErroredSecs,
       "xldv20ImaLinkFeSevErroredSecs": xldv20ImaLinkFeSevErroredSecs,
       "xldv20ImaLinkNeUnavailSecs": xldv20ImaLinkNeUnavailSecs,
       "xldv20ImaLinkFeUnavailSecs": xldv20ImaLinkFeUnavailSecs,
       "xldv20ImaLinkNeTxUnusableSecs": xldv20ImaLinkNeTxUnusableSecs,
       "xldv20ImaLinkNeRxUnusableSecs": xldv20ImaLinkNeRxUnusableSecs,
       "xldv20ImaLinkFeTxUnusableSecs": xldv20ImaLinkFeTxUnusableSecs,
       "xldv20ImaLinkFeRxUnusableSecs": xldv20ImaLinkFeRxUnusableSecs,
       "xldv20ImaLinkNeTxNumFailures": xldv20ImaLinkNeTxNumFailures,
       "xldv20ImaLinkNeRxNumFailures": xldv20ImaLinkNeRxNumFailures,
       "xldv20ImaLinkFeTxNumFailures": xldv20ImaLinkFeTxNumFailures,
       "xldv20ImaLinkFeRxNumFailures": xldv20ImaLinkFeRxNumFailures,
       "xldv20ImaLinkTxStuffs": xldv20ImaLinkTxStuffs,
       "xldv20ImaLinkRxStuffs": xldv20ImaLinkRxStuffs,
       "xldv20Traps": xldv20Traps,
       "xldv20TrHpExcBER": xldv20TrHpExcBER,
       "xldv20TrHpUNEQ": xldv20TrHpUNEQ,
       "xldv20TrLcd": xldv20TrLcd,
       "xldv20TrLof": xldv20TrLof,
       "xldv20TrLop": xldv20TrLop,
       "xldv20TrLos": xldv20TrLos,
       "xldv20TrMsAIS": xldv20TrMsAIS,
       "xldv20TrMsExcBER": xldv20TrMsExcBER,
       "xldv20TrMsRDI": xldv20TrMsRDI,
       "xldv20TrMsSD": xldv20TrMsSD,
       "xldv20TrPAIS": xldv20TrPAIS,
       "xldv20TrPRDI": xldv20TrPRDI,
       "xldv20TrRsExcBER": xldv20TrRsExcBER,
       "xldv20TrSlm": xldv20TrSlm,
       "xldv20TrTim": xldv20TrTim,
       "xldv20TrActFault": xldv20TrActFault,
       "xldv20TrReplaceableUnitTypeMismatch": xldv20TrReplaceableUnitTypeMismatch,
       "xldv20TrReplaceableUnitFailure": xldv20TrReplaceableUnitFailure,
       "xldv20TrReplaceableUnitProblem": xldv20TrReplaceableUnitProblem,
       "xldv20TrReplaceableUnitNotInstalled": xldv20TrReplaceableUnitNotInstalled,
       "xldv20TrReplaceableUnitSwMismatch": xldv20TrReplaceableUnitSwMismatch,
       "xldv20TrReplaceableUnitReset": xldv20TrReplaceableUnitReset,
       "xldv20TrReplaceableUnitResetEnd": xldv20TrReplaceableUnitResetEnd,
       "xldv20TrStartupEnd": xldv20TrStartupEnd,
       "xldv20TrLctSession": xldv20TrLctSession,
       "xldv20TrSnmAgentRunning": xldv20TrSnmAgentRunning,
       "xldv20TrRstResult": xldv20TrRstResult,
       "xldv20TrPltTestResult": xldv20TrPltTestResult,
       "xldv20TrStateChangeAdmin": xldv20TrStateChangeAdmin,
       "xldv20TrStateChangeOper": xldv20TrStateChangeOper,
       "xldv20TrChangeRate": xldv20TrChangeRate,
       "xldv20TrCmuReadyForReset": xldv20TrCmuReadyForReset,
       "xldv20TrAltTestResult": xldv20TrAltTestResult,
       "xldv20TrActivateLoadResult": xldv20TrActivateLoadResult,
       "xldv20TrPuUpgradeSucc": xldv20TrPuUpgradeSucc,
       "xldv20TrUpgradeCancelled": xldv20TrUpgradeCancelled,
       "xldv20TrFtpError": xldv20TrFtpError,
       "xldv20TrSweLogRead": xldv20TrSweLogRead,
       "xldv20TrHwmLogRead": xldv20TrHwmLogRead,
       "xldv20TrTraceLogRead": xldv20TrTraceLogRead,
       "xldv20TrVplCcCreation": xldv20TrVplCcCreation,
       "xldv20TrVplCcDeletion": xldv20TrVplCcDeletion,
       "xldv20TrObjCreate": xldv20TrObjCreate,
       "xldv20TrObjDelete": xldv20TrObjDelete,
       "xldv20TrXmissionErr": xldv20TrXmissionErr,
       "xldv20TrExternalAlarm": xldv20TrExternalAlarm,
       "xldv20TrUnitReadyForReset": xldv20TrUnitReadyForReset,
       "xldv20TrHwuControl": xldv20TrHwuControl,
       "xldv20TrReplaceableUnitRemoved": xldv20TrReplaceableUnitRemoved,
       "xldv20TrAIS": xldv20TrAIS,
       "xldv20TrRDI": xldv20TrRDI,
       "xldv20TrPlcpLof": xldv20TrPlcpLof,
       "xldv20TrPlcpRDI": xldv20TrPlcpRDI,
       "xldv20TrRemInvReady": xldv20TrRemInvReady,
       "xldv20TrDbBackup": xldv20TrDbBackup,
       "xldv20TrSwVersionSet": xldv20TrSwVersionSet,
       "xldv20TrReadSAPSContentFileReady": xldv20TrReadSAPSContentFileReady,
       "xldv20TrReplaceableUnitSwMissing": xldv20TrReplaceableUnitSwMissing,
       "xldv20TrInternalFault": xldv20TrInternalFault,
       "xldv20TrVclCcCreation": xldv20TrVclCcCreation,
       "xldv20TrVclCcDeletion": xldv20TrVclCcDeletion,
       "xldv20TrImmMNR": xldv20TrImmMNR,
       "xldv20TrLpr": xldv20TrLpr,
       "xldv20TrLol": xldv20TrLol,
       "xldv20TrAtmLayerMultiAlarm": xldv20TrAtmLayerMultiAlarm,
       "xldv20TrTelnetSession": xldv20TrTelnetSession,
       "xldv20TrVplCACProblem": xldv20TrVplCACProblem,
       "xldv20TrVclCACProblem": xldv20TrVclCACProblem,
       "xldv20TrWrongServiceConfigData": xldv20TrWrongServiceConfigData,
       "xldv20TrReplaceableUnitPlugged": xldv20TrReplaceableUnitPlugged,
       "xldv20TrReplaceableUnitUnplugged": xldv20TrReplaceableUnitUnplugged,
       "xldv20TrStateChangeOperExt": xldv20TrStateChangeOperExt,
       "xldv20TrLOC": xldv20TrLOC,
       "xldv20TrDbRestore": xldv20TrDbRestore,
       "xldv20TrUpgradeEndRequestResult": xldv20TrUpgradeEndRequestResult,
       "xldv20TrUnitUpgradeNotRequested": xldv20TrUnitUpgradeNotRequested,
       "xldv20TrVpcTpCreation": xldv20TrVpcTpCreation,
       "xldv20TrVpcTpDeletion": xldv20TrVpcTpDeletion,
       "xldv20TrVpcTpCACProblem": xldv20TrVpcTpCACProblem,
       "xldv20TrContinuityCheckVpEntryCreated": xldv20TrContinuityCheckVpEntryCreated,
       "xldv20TrContinuityCheckVpEntryDeleted": xldv20TrContinuityCheckVpEntryDeleted,
       "xldv20TrContinuityCheckVcEntryCreated": xldv20TrContinuityCheckVcEntryCreated,
       "xldv20TrContinuityCheckVcEntryDeleted": xldv20TrContinuityCheckVcEntryDeleted,
       "xldv20TrExcBER": xldv20TrExcBER,
       "xldv20TrLif": xldv20TrLif,
       "xldv20TrLods": xldv20TrLods,
       "xldv20TrTxUnusableFe": xldv20TrTxUnusableFe,
       "xldv20TrRxUnusableFe": xldv20TrRxUnusableFe,
       "xldv20TrRfiIma": xldv20TrRfiIma,
       "xldv20TrRAI": xldv20TrRAI,
       "xldv20TrStartUpFe": xldv20TrStartUpFe,
       "xldv20TrConfigAbort": xldv20TrConfigAbort,
       "xldv20TrConfigAbortFe": xldv20TrConfigAbortFe,
       "xldv20TrInsufficientLinks": xldv20TrInsufficientLinks,
       "xldv20TrInsufficientLinksFe": xldv20TrInsufficientLinksFe,
       "xldv20TrBlockedFe": xldv20TrBlockedFe,
       "xldv20TrImaMinNumOfLinks": xldv20TrImaMinNumOfLinks,
       "xldv20TrStateChangeAvail": xldv20TrStateChangeAvail,
       "xldv20TrapVars": xldv20TrapVars,
       "xldv20TvStartupResult": xldv20TvStartupResult,
       "xldv20TvStartupType": xldv20TvStartupType,
       "xldv20TvSnmLctSession": xldv20TvSnmLctSession,
       "xldv20TvRepEntity": xldv20TvRepEntity,
       "xldv20TvRepSource": xldv20TvRepSource,
       "xldv20TvTimeAndDate": xldv20TvTimeAndDate,
       "xldv20TvActCcReloadResult": xldv20TvActCcReloadResult,
       "xldv20TvActCcStatus": xldv20TvActCcStatus,
       "xldv20TvAlmNatureOfAlarm": xldv20TvAlmNatureOfAlarm,
       "xldv20TvAlmSpecProblem": xldv20TvAlmSpecProblem,
       "xldv20TvAlmFailedComponent": xldv20TvAlmFailedComponent,
       "xldv20TvAlmSeverityOfFailure": xldv20TvAlmSeverityOfFailure,
       "xldv20TvAlmStatus": xldv20TvAlmStatus,
       "xldv20TvAlmPropRepairAction": xldv20TvAlmPropRepairAction,
       "xldv20TvAlmFailedComponentRepSource": xldv20TvAlmFailedComponentRepSource,
       "xldv20TvStcOldAdminStatus": xldv20TvStcOldAdminStatus,
       "xldv20TvStcNewAdminStatus": xldv20TvStcNewAdminStatus,
       "xldv20TvStcOldOperStatus": xldv20TvStcOldOperStatus,
       "xldv20TvStcNewOperStatus": xldv20TvStcNewOperStatus,
       "xldv20TvTsrControlStatus": xldv20TvTsrControlStatus,
       "xldv20TvRstResult": xldv20TvRstResult,
       "xldv20TvRstHwUnitIndex": xldv20TvRstHwUnitIndex,
       "xldv20TvHweResetType": xldv20TvHweResetType,
       "xldv20TvAdcControlStatus": xldv20TvAdcControlStatus,
       "xldv20TvSucResult": xldv20TvSucResult,
       "xldv20TvSucUnit": xldv20TvSucUnit,
       "xldv20TvSucHwUnitIndex": xldv20TvSucHwUnitIndex,
       "xldv20TvSucVersionNo": xldv20TvSucVersionNo,
       "xldv20TvSucPathName": xldv20TvSucPathName,
       "xldv20TvSucFileName": xldv20TvSucFileName,
       "xldv20TvDbuSweLogReadResult": xldv20TvDbuSweLogReadResult,
       "xldv20TvDbuHwmLogReadResult": xldv20TvDbuHwmLogReadResult,
       "xldv20TvDbuSwTraceLogReadResult": xldv20TvDbuSwTraceLogReadResult,
       "xldv20TvHwUnitType": xldv20TvHwUnitType,
       "xldv20TvHwContainingUnitIndex": xldv20TvHwContainingUnitIndex,
       "xldv20TvHwContainedUnitAddr": xldv20TvHwContainedUnitAddr,
       "xldv20TvHwuControlResult": xldv20TvHwuControlResult,
       "xldv20TvRiRemInvResult": xldv20TvRiRemInvResult,
       "xldv20TvVersionNrCmuLoad": xldv20TvVersionNrCmuLoad,
       "xldv20TvBackupResult": xldv20TvBackupResult,
       "xldv20TvVpiNni": xldv20TvVpiNni,
       "xldv20TvVpiNniIndex": xldv20TvVpiNniIndex,
       "xldv20TvVplTerminationPointA": xldv20TvVplTerminationPointA,
       "xldv20TvVplTerminationPointZ": xldv20TvVplTerminationPointZ,
       "xldv20TvSnmMibVersion": xldv20TvSnmMibVersion,
       "xldv20TvSnmAgentVersion": xldv20TvSnmAgentVersion,
       "xldv20TvVciNni": xldv20TvVciNni,
       "xldv20TvVciNniIndex": xldv20TvVciNniIndex,
       "xldv20TvVclTerminationPointA": xldv20TvVclTerminationPointA,
       "xldv20TvVclTerminationPointZ": xldv20TvVclTerminationPointZ,
       "xldv20TvVpcTpIndex": xldv20TvVpcTpIndex,
       "xldv20TvVpcNniIndex": xldv20TvVpcNniIndex,
       "xldv20TvVpcUniIndex": xldv20TvVpcUniIndex,
       "xldv20TvEthVccTpIndex": xldv20TvEthVccTpIndex,
       "xldv20TvVpiValue": xldv20TvVpiValue,
       "xldv20TvVciValue": xldv20TvVciValue,
       "xldv20TvVplTpIndex": xldv20TvVplTpIndex,
       "xldv20TvVplIfIndex": xldv20TvVplIfIndex,
       "xldv20TvAlmFailedComponentString": xldv20TvAlmFailedComponentString,
       "xldv20TvTelnetSession": xldv20TvTelnetSession,
       "xldv20TvEthIfIndex": xldv20TvEthIfIndex,
       "xldv20TvCACProblemType": xldv20TvCACProblemType,
       "xldv20TvCACBandwidthUsageUp": xldv20TvCACBandwidthUsageUp,
       "xldv20TvEthVpcTpIndex": xldv20TvEthVpcTpIndex,
       "xldv20TvEthEntryIndex": xldv20TvEthEntryIndex,
       "xldv20TvRepEntityExt": xldv20TvRepEntityExt,
       "xldv20TvTelnetSessionUser": xldv20TvTelnetSessionUser,
       "xldv20TvIndexSegment": xldv20TvIndexSegment,
       "xldv20TvIndexEndToEnd": xldv20TvIndexEndToEnd,
       "xldv20TvRestoreResult": xldv20TvRestoreResult,
       "xldv20TvCACBandwidthUsageDown": xldv20TvCACBandwidthUsageDown,
       "xldv20TvCallpObjectType": xldv20TvCallpObjectType,
       "xldv20TvVpcTpIfIndex": xldv20TvVpcTpIfIndex,
       "xldv20TvAlmSpecProblemText": xldv20TvAlmSpecProblemText,
       "xldv20TvImaSetNumResult": xldv20TvImaSetNumResult,
       "xldv20TvStcOldAvailStatus": xldv20TvStcOldAvailStatus,
       "xldv20TvStcNewAvailStatus": xldv20TvStcNewAvailStatus,
       "xldv20TrapTypes": xldv20TrapTypes}
)
