# SNMP MIB module (TIMETRA-OTU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIMETRA-OTU-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:03:45 2024
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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(TmnxActionType,) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TmnxActionType")


# MODULE-IDENTITY

tmnxOtuMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 62)
)
tmnxOtuMIBModule.setRevisions(
        ("1909-02-28 00:00",
         "1908-10-23 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxOtuFecMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enhanced", 2),
          ("g709fec", 1))
    )



class TmnxOtu2LanDataRate(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dr11049", 1),
          ("dr11096", 2),
          ("notApplicable", 0))
    )



class TmnxOtuSFSDMethod(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bip8", 2),
          ("fec", 1))
    )



class TmnxOtuTtiMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("bytes", 2),
          ("string", 1))
    )



class TmnxOtuTtiString(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class TmnxOtuAlarms(Bits, TextualConvention):
    status = "current"


class TmnxOtuPsiPayloadType(Integer32, TextualConvention):
    status = "current"
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
              16,
              17,
              32,
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
              253,
              254)
        )
    )
    namedValues = NamedValues(
        *(("asyncCbr", 2),
          ("atm", 4),
          ("auto", 0),
          ("bitStrNoOctet", 17),
          ("bitStrOctet", 16),
          ("exp", 1),
          ("gfp", 5),
          ("gmp", 7),
          ("nullTest", 253),
          ("oduMux", 32),
          ("prbsTest", 254),
          ("rsvd80", 128),
          ("rsvd81", 129),
          ("rsvd82", 130),
          ("rsvd83", 131),
          ("rsvd84", 132),
          ("rsvd85", 133),
          ("rsvd86", 134),
          ("rsvd87", 135),
          ("rsvd88", 136),
          ("rsvd89", 137),
          ("rsvd8A", 138),
          ("rsvd8B", 139),
          ("rsvd8C", 140),
          ("rsvd8D", 141),
          ("rsvd8E", 142),
          ("rsvd8F", 143),
          ("syncCbr", 3),
          ("vcat", 6))
    )



class TmnxOtuTimReaction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("squelchRx", 1))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxOtuConformance_ObjectIdentity = ObjectIdentity
tmnxOtuConformance = _TmnxOtuConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 62)
)
_TmnxOtuCompliances_ObjectIdentity = ObjectIdentity
tmnxOtuCompliances = _TmnxOtuCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 62, 1)
)
_TmnxOtuGroups_ObjectIdentity = ObjectIdentity
tmnxOtuGroups = _TmnxOtuGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 62, 2)
)
_TmnxOtuGroupsV7v0_ObjectIdentity = ObjectIdentity
tmnxOtuGroupsV7v0 = _TmnxOtuGroupsV7v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 62, 2, 5)
)
_TmnxOtuGroupsV8v0_ObjectIdentity = ObjectIdentity
tmnxOtuGroupsV8v0 = _TmnxOtuGroupsV8v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 62, 2, 6)
)
_TmnxOtuObjs_ObjectIdentity = ObjectIdentity
tmnxOtuObjs = _TmnxOtuObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62)
)
_TmnxOtuConfigurationTimeStamps_ObjectIdentity = ObjectIdentity
tmnxOtuConfigurationTimeStamps = _TmnxOtuConfigurationTimeStamps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 0)
)
_TmnxOtuIfTableLastChanged_Type = TimeStamp
_TmnxOtuIfTableLastChanged_Object = MibScalar
tmnxOtuIfTableLastChanged = _TmnxOtuIfTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 0, 1),
    _TmnxOtuIfTableLastChanged_Type()
)
tmnxOtuIfTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfTableLastChanged.setStatus("current")
_TmnxOtuConfigurations_ObjectIdentity = ObjectIdentity
tmnxOtuConfigurations = _TmnxOtuConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 1)
)
_TmnxOtuIfTable_Object = MibTable
tmnxOtuIfTable = _TmnxOtuIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxOtuIfTable.setStatus("current")
_TmnxOtuIfEntry_Object = MibTableRow
tmnxOtuIfEntry = _TmnxOtuIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 1, 1, 1)
)
tmnxOtuIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tmnxOtuIfEntry.setStatus("current")
_TmnxOtuIfRowStatus_Type = RowStatus
_TmnxOtuIfRowStatus_Object = MibTableColumn
tmnxOtuIfRowStatus = _TmnxOtuIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 1, 1, 1, 1),
    _TmnxOtuIfRowStatus_Type()
)
tmnxOtuIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOtuIfRowStatus.setStatus("current")
_TmnxOtuIfTimeStamp_Type = TimeStamp
_TmnxOtuIfTimeStamp_Object = MibTableColumn
tmnxOtuIfTimeStamp = _TmnxOtuIfTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 1, 1, 1, 2),
    _TmnxOtuIfTimeStamp_Type()
)
tmnxOtuIfTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfTimeStamp.setStatus("current")


class _TmnxOtuIfFecMode_Type(TmnxOtuFecMode):
    """Custom type tmnxOtuIfFecMode based on TmnxOtuFecMode"""


_TmnxOtuIfFecMode_Object = MibTableColumn
tmnxOtuIfFecMode = _TmnxOtuIfFecMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 1, 1, 1, 3),
    _TmnxOtuIfFecMode_Type()
)
tmnxOtuIfFecMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOtuIfFecMode.setStatus("current")


class _TmnxOtuIfSfSdMethod_Type(TmnxOtuSFSDMethod):
    """Custom type tmnxOtuIfSfSdMethod based on TmnxOtuSFSDMethod"""


_TmnxOtuIfSfSdMethod_Object = MibTableColumn
tmnxOtuIfSfSdMethod = _TmnxOtuIfSfSdMethod_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 1, 1, 1, 4),
    _TmnxOtuIfSfSdMethod_Type()
)
tmnxOtuIfSfSdMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOtuIfSfSdMethod.setStatus("current")


class _TmnxOtuIfBerSfThreshold_Type(Unsigned32):
    """Custom type tmnxOtuIfBerSfThreshold based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 6),
    )


_TmnxOtuIfBerSfThreshold_Type.__name__ = "Unsigned32"
_TmnxOtuIfBerSfThreshold_Object = MibTableColumn
tmnxOtuIfBerSfThreshold = _TmnxOtuIfBerSfThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 1, 1, 1, 5),
    _TmnxOtuIfBerSfThreshold_Type()
)
tmnxOtuIfBerSfThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOtuIfBerSfThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfBerSfThreshold.setUnits("error bits in 1/10e-n bits received")


class _TmnxOtuIfBerSdThreshold_Type(Unsigned32):
    """Custom type tmnxOtuIfBerSdThreshold based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 9),
    )


_TmnxOtuIfBerSdThreshold_Type.__name__ = "Unsigned32"
_TmnxOtuIfBerSdThreshold_Object = MibTableColumn
tmnxOtuIfBerSdThreshold = _TmnxOtuIfBerSdThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 1, 1, 1, 6),
    _TmnxOtuIfBerSdThreshold_Type()
)
tmnxOtuIfBerSdThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOtuIfBerSdThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfBerSdThreshold.setUnits("error bits in 1/10^n bits received")
_TmnxOtuIfOtuOperDataRate_Type = Unsigned32
_TmnxOtuIfOtuOperDataRate_Object = MibTableColumn
tmnxOtuIfOtuOperDataRate = _TmnxOtuIfOtuOperDataRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 1, 1, 1, 7),
    _TmnxOtuIfOtuOperDataRate_Type()
)
tmnxOtuIfOtuOperDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfOtuOperDataRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfOtuOperDataRate.setUnits("Mb/s")


class _TmnxOtuIfOtu2LanDataRate_Type(TmnxOtu2LanDataRate):
    """Custom type tmnxOtuIfOtu2LanDataRate based on TmnxOtu2LanDataRate"""


_TmnxOtuIfOtu2LanDataRate_Object = MibTableColumn
tmnxOtuIfOtu2LanDataRate = _TmnxOtuIfOtu2LanDataRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 1, 1, 1, 8),
    _TmnxOtuIfOtu2LanDataRate_Type()
)
tmnxOtuIfOtu2LanDataRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOtuIfOtu2LanDataRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfOtu2LanDataRate.setUnits("Gb/s")


class _TmnxOtuIfCfgAlarms_Type(TmnxOtuAlarms):
    """Custom type tmnxOtuIfCfgAlarms based on TmnxOtuAlarms"""
    defaultBinValue = "111101010001"


_TmnxOtuIfCfgAlarms_Object = MibTableColumn
tmnxOtuIfCfgAlarms = _TmnxOtuIfCfgAlarms_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 1, 1, 1, 9),
    _TmnxOtuIfCfgAlarms_Type()
)
tmnxOtuIfCfgAlarms.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOtuIfCfgAlarms.setStatus("current")
_TmnxOtuIfAlarmState_Type = TmnxOtuAlarms
_TmnxOtuIfAlarmState_Object = MibTableColumn
tmnxOtuIfAlarmState = _TmnxOtuIfAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 1, 1, 1, 10),
    _TmnxOtuIfAlarmState_Type()
)
tmnxOtuIfAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfAlarmState.setStatus("current")


class _TmnxOtuIfHoldTimeUp_Type(Unsigned32):
    """Custom type tmnxOtuIfHoldTimeUp based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxOtuIfHoldTimeUp_Type.__name__ = "Unsigned32"
_TmnxOtuIfHoldTimeUp_Object = MibTableColumn
tmnxOtuIfHoldTimeUp = _TmnxOtuIfHoldTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 1, 1, 1, 11),
    _TmnxOtuIfHoldTimeUp_Type()
)
tmnxOtuIfHoldTimeUp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOtuIfHoldTimeUp.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxOtuIfHoldTimeUp.setUnits("100s of milliseconds")


class _TmnxOtuIfHoldTimeDown_Type(Unsigned32):
    """Custom type tmnxOtuIfHoldTimeDown based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxOtuIfHoldTimeDown_Type.__name__ = "Unsigned32"
_TmnxOtuIfHoldTimeDown_Object = MibTableColumn
tmnxOtuIfHoldTimeDown = _TmnxOtuIfHoldTimeDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 1, 1, 1, 12),
    _TmnxOtuIfHoldTimeDown_Type()
)
tmnxOtuIfHoldTimeDown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOtuIfHoldTimeDown.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxOtuIfHoldTimeDown.setUnits("100s of milliseconds")
_TmnxOtuIfSmTtiTxMode_Type = TmnxOtuTtiMode
_TmnxOtuIfSmTtiTxMode_Object = MibTableColumn
tmnxOtuIfSmTtiTxMode = _TmnxOtuIfSmTtiTxMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 1, 1, 1, 13),
    _TmnxOtuIfSmTtiTxMode_Type()
)
tmnxOtuIfSmTtiTxMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOtuIfSmTtiTxMode.setStatus("current")


class _TmnxOtuIfSmTtiTx_Type(TmnxOtuTtiString):
    """Custom type tmnxOtuIfSmTtiTx based on TmnxOtuTtiString"""
    subtypeSpec = TmnxOtuTtiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TmnxOtuIfSmTtiTx_Type.__name__ = "TmnxOtuTtiString"
_TmnxOtuIfSmTtiTx_Object = MibTableColumn
tmnxOtuIfSmTtiTx = _TmnxOtuIfSmTtiTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 1, 1, 1, 14),
    _TmnxOtuIfSmTtiTx_Type()
)
tmnxOtuIfSmTtiTx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOtuIfSmTtiTx.setStatus("current")


class _TmnxOtuIfSmTtiRx_Type(TmnxOtuTtiString):
    """Custom type tmnxOtuIfSmTtiRx based on TmnxOtuTtiString"""
    subtypeSpec = TmnxOtuTtiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TmnxOtuIfSmTtiRx_Type.__name__ = "TmnxOtuTtiString"
_TmnxOtuIfSmTtiRx_Object = MibTableColumn
tmnxOtuIfSmTtiRx = _TmnxOtuIfSmTtiRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 1, 1, 1, 15),
    _TmnxOtuIfSmTtiRx_Type()
)
tmnxOtuIfSmTtiRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfSmTtiRx.setStatus("current")
_TmnxOtuIfSmTtiExpMode_Type = TmnxOtuTtiMode
_TmnxOtuIfSmTtiExpMode_Object = MibTableColumn
tmnxOtuIfSmTtiExpMode = _TmnxOtuIfSmTtiExpMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 1, 1, 1, 16),
    _TmnxOtuIfSmTtiExpMode_Type()
)
tmnxOtuIfSmTtiExpMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOtuIfSmTtiExpMode.setStatus("current")
_TmnxOtuIfSmTtiExpCopyRx_Type = TmnxActionType
_TmnxOtuIfSmTtiExpCopyRx_Object = MibTableColumn
tmnxOtuIfSmTtiExpCopyRx = _TmnxOtuIfSmTtiExpCopyRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 1, 1, 1, 17),
    _TmnxOtuIfSmTtiExpCopyRx_Type()
)
tmnxOtuIfSmTtiExpCopyRx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOtuIfSmTtiExpCopyRx.setStatus("current")


class _TmnxOtuIfSmTtiExp_Type(TmnxOtuTtiString):
    """Custom type tmnxOtuIfSmTtiExp based on TmnxOtuTtiString"""
    subtypeSpec = TmnxOtuTtiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TmnxOtuIfSmTtiExp_Type.__name__ = "TmnxOtuTtiString"
_TmnxOtuIfSmTtiExp_Object = MibTableColumn
tmnxOtuIfSmTtiExp = _TmnxOtuIfSmTtiExp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 1, 1, 1, 18),
    _TmnxOtuIfSmTtiExp_Type()
)
tmnxOtuIfSmTtiExp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOtuIfSmTtiExp.setStatus("current")
_TmnxOtuIfPmTtiTxMode_Type = TmnxOtuTtiMode
_TmnxOtuIfPmTtiTxMode_Object = MibTableColumn
tmnxOtuIfPmTtiTxMode = _TmnxOtuIfPmTtiTxMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 1, 1, 1, 19),
    _TmnxOtuIfPmTtiTxMode_Type()
)
tmnxOtuIfPmTtiTxMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOtuIfPmTtiTxMode.setStatus("current")


class _TmnxOtuIfPmTtiTx_Type(TmnxOtuTtiString):
    """Custom type tmnxOtuIfPmTtiTx based on TmnxOtuTtiString"""
    subtypeSpec = TmnxOtuTtiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TmnxOtuIfPmTtiTx_Type.__name__ = "TmnxOtuTtiString"
_TmnxOtuIfPmTtiTx_Object = MibTableColumn
tmnxOtuIfPmTtiTx = _TmnxOtuIfPmTtiTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 1, 1, 1, 20),
    _TmnxOtuIfPmTtiTx_Type()
)
tmnxOtuIfPmTtiTx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOtuIfPmTtiTx.setStatus("current")


class _TmnxOtuIfPmTtiRx_Type(TmnxOtuTtiString):
    """Custom type tmnxOtuIfPmTtiRx based on TmnxOtuTtiString"""
    subtypeSpec = TmnxOtuTtiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TmnxOtuIfPmTtiRx_Type.__name__ = "TmnxOtuTtiString"
_TmnxOtuIfPmTtiRx_Object = MibTableColumn
tmnxOtuIfPmTtiRx = _TmnxOtuIfPmTtiRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 1, 1, 1, 21),
    _TmnxOtuIfPmTtiRx_Type()
)
tmnxOtuIfPmTtiRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfPmTtiRx.setStatus("current")
_TmnxOtuIfPmTtiExpMode_Type = TmnxOtuTtiMode
_TmnxOtuIfPmTtiExpMode_Object = MibTableColumn
tmnxOtuIfPmTtiExpMode = _TmnxOtuIfPmTtiExpMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 1, 1, 1, 22),
    _TmnxOtuIfPmTtiExpMode_Type()
)
tmnxOtuIfPmTtiExpMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOtuIfPmTtiExpMode.setStatus("current")
_TmnxOtuIfPmTtiExpCopyRx_Type = TmnxActionType
_TmnxOtuIfPmTtiExpCopyRx_Object = MibTableColumn
tmnxOtuIfPmTtiExpCopyRx = _TmnxOtuIfPmTtiExpCopyRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 1, 1, 1, 23),
    _TmnxOtuIfPmTtiExpCopyRx_Type()
)
tmnxOtuIfPmTtiExpCopyRx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOtuIfPmTtiExpCopyRx.setStatus("current")


class _TmnxOtuIfPmTtiExp_Type(TmnxOtuTtiString):
    """Custom type tmnxOtuIfPmTtiExp based on TmnxOtuTtiString"""
    subtypeSpec = TmnxOtuTtiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TmnxOtuIfPmTtiExp_Type.__name__ = "TmnxOtuTtiString"
_TmnxOtuIfPmTtiExp_Object = MibTableColumn
tmnxOtuIfPmTtiExp = _TmnxOtuIfPmTtiExp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 1, 1, 1, 24),
    _TmnxOtuIfPmTtiExp_Type()
)
tmnxOtuIfPmTtiExp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOtuIfPmTtiExp.setStatus("current")
_TmnxOtuIfPsiTtiTxMode_Type = TmnxOtuTtiMode
_TmnxOtuIfPsiTtiTxMode_Object = MibTableColumn
tmnxOtuIfPsiTtiTxMode = _TmnxOtuIfPsiTtiTxMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 1, 1, 1, 25),
    _TmnxOtuIfPsiTtiTxMode_Type()
)
tmnxOtuIfPsiTtiTxMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOtuIfPsiTtiTxMode.setStatus("current")
_TmnxOtuIfPsiTtiTx_Type = TmnxOtuTtiString
_TmnxOtuIfPsiTtiTx_Object = MibTableColumn
tmnxOtuIfPsiTtiTx = _TmnxOtuIfPsiTtiTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 1, 1, 1, 26),
    _TmnxOtuIfPsiTtiTx_Type()
)
tmnxOtuIfPsiTtiTx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOtuIfPsiTtiTx.setStatus("current")
_TmnxOtuIfPsiTtiRx_Type = TmnxOtuTtiString
_TmnxOtuIfPsiTtiRx_Object = MibTableColumn
tmnxOtuIfPsiTtiRx = _TmnxOtuIfPsiTtiRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 1, 1, 1, 27),
    _TmnxOtuIfPsiTtiRx_Type()
)
tmnxOtuIfPsiTtiRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfPsiTtiRx.setStatus("current")
_TmnxOtuIfPsiTtiExpMode_Type = TmnxOtuTtiMode
_TmnxOtuIfPsiTtiExpMode_Object = MibTableColumn
tmnxOtuIfPsiTtiExpMode = _TmnxOtuIfPsiTtiExpMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 1, 1, 1, 28),
    _TmnxOtuIfPsiTtiExpMode_Type()
)
tmnxOtuIfPsiTtiExpMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOtuIfPsiTtiExpMode.setStatus("current")
_TmnxOtuIfPsiTtiExpCopyRx_Type = TmnxActionType
_TmnxOtuIfPsiTtiExpCopyRx_Object = MibTableColumn
tmnxOtuIfPsiTtiExpCopyRx = _TmnxOtuIfPsiTtiExpCopyRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 1, 1, 1, 29),
    _TmnxOtuIfPsiTtiExpCopyRx_Type()
)
tmnxOtuIfPsiTtiExpCopyRx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOtuIfPsiTtiExpCopyRx.setStatus("current")


class _TmnxOtuIfPsiTtiExp_Type(TmnxOtuTtiString):
    """Custom type tmnxOtuIfPsiTtiExp based on TmnxOtuTtiString"""
    subtypeSpec = TmnxOtuTtiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxOtuIfPsiTtiExp_Type.__name__ = "TmnxOtuTtiString"
_TmnxOtuIfPsiTtiExp_Object = MibTableColumn
tmnxOtuIfPsiTtiExp = _TmnxOtuIfPsiTtiExp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 1, 1, 1, 30),
    _TmnxOtuIfPsiTtiExp_Type()
)
tmnxOtuIfPsiTtiExp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOtuIfPsiTtiExp.setStatus("current")
_TmnxOtuIfPsiPayloadTypeTx_Type = TmnxOtuPsiPayloadType
_TmnxOtuIfPsiPayloadTypeTx_Object = MibTableColumn
tmnxOtuIfPsiPayloadTypeTx = _TmnxOtuIfPsiPayloadTypeTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 1, 1, 1, 31),
    _TmnxOtuIfPsiPayloadTypeTx_Type()
)
tmnxOtuIfPsiPayloadTypeTx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOtuIfPsiPayloadTypeTx.setStatus("current")
_TmnxOtuIfPsiPayloadTypeRx_Type = TmnxOtuPsiPayloadType
_TmnxOtuIfPsiPayloadTypeRx_Object = MibTableColumn
tmnxOtuIfPsiPayloadTypeRx = _TmnxOtuIfPsiPayloadTypeRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 1, 1, 1, 32),
    _TmnxOtuIfPsiPayloadTypeRx_Type()
)
tmnxOtuIfPsiPayloadTypeRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfPsiPayloadTypeRx.setStatus("current")
_TmnxOtuIfPsiPayloadTypeExp_Type = TmnxOtuPsiPayloadType
_TmnxOtuIfPsiPayloadTypeExp_Object = MibTableColumn
tmnxOtuIfPsiPayloadTypeExp = _TmnxOtuIfPsiPayloadTypeExp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 1, 1, 1, 33),
    _TmnxOtuIfPsiPayloadTypeExp_Type()
)
tmnxOtuIfPsiPayloadTypeExp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOtuIfPsiPayloadTypeExp.setStatus("current")


class _TmnxOtuIfGfpMappingEnable_Type(TruthValue):
    """Custom type tmnxOtuIfGfpMappingEnable based on TruthValue"""


_TmnxOtuIfGfpMappingEnable_Object = MibTableColumn
tmnxOtuIfGfpMappingEnable = _TmnxOtuIfGfpMappingEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 1, 1, 1, 34),
    _TmnxOtuIfGfpMappingEnable_Type()
)
tmnxOtuIfGfpMappingEnable.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOtuIfGfpMappingEnable.setStatus("current")


class _TmnxOtuIfAsyncMappingEnable_Type(TruthValue):
    """Custom type tmnxOtuIfAsyncMappingEnable based on TruthValue"""


_TmnxOtuIfAsyncMappingEnable_Object = MibTableColumn
tmnxOtuIfAsyncMappingEnable = _TmnxOtuIfAsyncMappingEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 1, 1, 1, 35),
    _TmnxOtuIfAsyncMappingEnable_Type()
)
tmnxOtuIfAsyncMappingEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOtuIfAsyncMappingEnable.setStatus("current")


class _TmnxOtuIfSmTimReaction_Type(TmnxOtuTimReaction):
    """Custom type tmnxOtuIfSmTimReaction based on TmnxOtuTimReaction"""


_TmnxOtuIfSmTimReaction_Object = MibTableColumn
tmnxOtuIfSmTimReaction = _TmnxOtuIfSmTimReaction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 1, 1, 1, 36),
    _TmnxOtuIfSmTimReaction_Type()
)
tmnxOtuIfSmTimReaction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOtuIfSmTimReaction.setStatus("current")


class _TmnxOtuIfPmTimReaction_Type(TmnxOtuTimReaction):
    """Custom type tmnxOtuIfPmTimReaction based on TmnxOtuTimReaction"""


_TmnxOtuIfPmTimReaction_Object = MibTableColumn
tmnxOtuIfPmTimReaction = _TmnxOtuIfPmTimReaction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 1, 1, 1, 37),
    _TmnxOtuIfPmTimReaction_Type()
)
tmnxOtuIfPmTimReaction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOtuIfPmTimReaction.setStatus("current")


class _TmnxOtuIfPsiTimReaction_Type(TmnxOtuTimReaction):
    """Custom type tmnxOtuIfPsiTimReaction based on TmnxOtuTimReaction"""


_TmnxOtuIfPsiTimReaction_Object = MibTableColumn
tmnxOtuIfPsiTimReaction = _TmnxOtuIfPsiTimReaction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 1, 1, 1, 38),
    _TmnxOtuIfPsiTimReaction_Type()
)
tmnxOtuIfPsiTimReaction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOtuIfPsiTimReaction.setStatus("current")


class _TmnxOtuIfPsiPlmReaction_Type(TmnxOtuTimReaction):
    """Custom type tmnxOtuIfPsiPlmReaction based on TmnxOtuTimReaction"""


_TmnxOtuIfPsiPlmReaction_Object = MibTableColumn
tmnxOtuIfPsiPlmReaction = _TmnxOtuIfPsiPlmReaction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 1, 1, 1, 39),
    _TmnxOtuIfPsiPlmReaction_Type()
)
tmnxOtuIfPsiPlmReaction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOtuIfPsiPlmReaction.setStatus("current")
_TmnxOtuStatistics_ObjectIdentity = ObjectIdentity
tmnxOtuStatistics = _TmnxOtuStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2)
)
_TmnxOtuIfRawStatsTable_Object = MibTable
tmnxOtuIfRawStatsTable = _TmnxOtuIfRawStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsTable.setStatus("current")
_TmnxOtuIfRawStatsEntry_Object = MibTableRow
tmnxOtuIfRawStatsEntry = _TmnxOtuIfRawStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 1, 1)
)
tmnxOtuIfRawStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsEntry.setStatus("current")
_TmnxOtuIfRawStatsFECCorrZeros_Type = Counter32
_TmnxOtuIfRawStatsFECCorrZeros_Object = MibTableColumn
tmnxOtuIfRawStatsFECCorrZeros = _TmnxOtuIfRawStatsFECCorrZeros_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 1, 1, 1),
    _TmnxOtuIfRawStatsFECCorrZeros_Type()
)
tmnxOtuIfRawStatsFECCorrZeros.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsFECCorrZeros.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsFECCorrZeros.setUnits("bits")
_TmnxOtuIfRawStatsOFFECCorrZeros_Type = Counter32
_TmnxOtuIfRawStatsOFFECCorrZeros_Object = MibTableColumn
tmnxOtuIfRawStatsOFFECCorrZeros = _TmnxOtuIfRawStatsOFFECCorrZeros_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 1, 1, 2),
    _TmnxOtuIfRawStatsOFFECCorrZeros_Type()
)
tmnxOtuIfRawStatsOFFECCorrZeros.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsOFFECCorrZeros.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsOFFECCorrZeros.setUnits("count")
_TmnxOtuIfRawStatsHCFECCorrZeros_Type = Counter64
_TmnxOtuIfRawStatsHCFECCorrZeros_Object = MibTableColumn
tmnxOtuIfRawStatsHCFECCorrZeros = _TmnxOtuIfRawStatsHCFECCorrZeros_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 1, 1, 3),
    _TmnxOtuIfRawStatsHCFECCorrZeros_Type()
)
tmnxOtuIfRawStatsHCFECCorrZeros.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsHCFECCorrZeros.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsHCFECCorrZeros.setUnits("bits")
_TmnxOtuIfRawStatsFECCorrOnes_Type = Counter32
_TmnxOtuIfRawStatsFECCorrOnes_Object = MibTableColumn
tmnxOtuIfRawStatsFECCorrOnes = _TmnxOtuIfRawStatsFECCorrOnes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 1, 1, 4),
    _TmnxOtuIfRawStatsFECCorrOnes_Type()
)
tmnxOtuIfRawStatsFECCorrOnes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsFECCorrOnes.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsFECCorrOnes.setUnits("bits")
_TmnxOtuIfRawStatsOFFECCorrOnes_Type = Counter32
_TmnxOtuIfRawStatsOFFECCorrOnes_Object = MibTableColumn
tmnxOtuIfRawStatsOFFECCorrOnes = _TmnxOtuIfRawStatsOFFECCorrOnes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 1, 1, 5),
    _TmnxOtuIfRawStatsOFFECCorrOnes_Type()
)
tmnxOtuIfRawStatsOFFECCorrOnes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsOFFECCorrOnes.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsOFFECCorrOnes.setUnits("count")
_TmnxOtuIfRawStatsHCFECCorrOnes_Type = Counter64
_TmnxOtuIfRawStatsHCFECCorrOnes_Object = MibTableColumn
tmnxOtuIfRawStatsHCFECCorrOnes = _TmnxOtuIfRawStatsHCFECCorrOnes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 1, 1, 6),
    _TmnxOtuIfRawStatsHCFECCorrOnes_Type()
)
tmnxOtuIfRawStatsHCFECCorrOnes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsHCFECCorrOnes.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsHCFECCorrOnes.setUnits("bits")
_TmnxOtuIfRawStatsFECUncorrSR_Type = Counter32
_TmnxOtuIfRawStatsFECUncorrSR_Object = MibTableColumn
tmnxOtuIfRawStatsFECUncorrSR = _TmnxOtuIfRawStatsFECUncorrSR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 1, 1, 7),
    _TmnxOtuIfRawStatsFECUncorrSR_Type()
)
tmnxOtuIfRawStatsFECUncorrSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsFECUncorrSR.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsFECUncorrSR.setUnits("Sub-Rows")
_TmnxOtuIfRawStatsOFFECUncorrSR_Type = Counter32
_TmnxOtuIfRawStatsOFFECUncorrSR_Object = MibTableColumn
tmnxOtuIfRawStatsOFFECUncorrSR = _TmnxOtuIfRawStatsOFFECUncorrSR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 1, 1, 8),
    _TmnxOtuIfRawStatsOFFECUncorrSR_Type()
)
tmnxOtuIfRawStatsOFFECUncorrSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsOFFECUncorrSR.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsOFFECUncorrSR.setUnits("count")
_TmnxOtuIfRawStatsHCFECUncorrSR_Type = Counter64
_TmnxOtuIfRawStatsHCFECUncorrSR_Object = MibTableColumn
tmnxOtuIfRawStatsHCFECUncorrSR = _TmnxOtuIfRawStatsHCFECUncorrSR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 1, 1, 9),
    _TmnxOtuIfRawStatsHCFECUncorrSR_Type()
)
tmnxOtuIfRawStatsHCFECUncorrSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsHCFECUncorrSR.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsHCFECUncorrSR.setUnits("Sub-Rows")
_TmnxOtuIfRawStatsFECSES_Type = Counter32
_TmnxOtuIfRawStatsFECSES_Object = MibTableColumn
tmnxOtuIfRawStatsFECSES = _TmnxOtuIfRawStatsFECSES_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 1, 1, 10),
    _TmnxOtuIfRawStatsFECSES_Type()
)
tmnxOtuIfRawStatsFECSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsFECSES.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsFECSES.setUnits("seconds")
_TmnxOtuIfRawStatsSMBIP8_Type = Counter32
_TmnxOtuIfRawStatsSMBIP8_Object = MibTableColumn
tmnxOtuIfRawStatsSMBIP8 = _TmnxOtuIfRawStatsSMBIP8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 1, 1, 11),
    _TmnxOtuIfRawStatsSMBIP8_Type()
)
tmnxOtuIfRawStatsSMBIP8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsSMBIP8.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsSMBIP8.setUnits("bits")
_TmnxOtuIfRawStatsOFSMBIP8_Type = Counter32
_TmnxOtuIfRawStatsOFSMBIP8_Object = MibTableColumn
tmnxOtuIfRawStatsOFSMBIP8 = _TmnxOtuIfRawStatsOFSMBIP8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 1, 1, 12),
    _TmnxOtuIfRawStatsOFSMBIP8_Type()
)
tmnxOtuIfRawStatsOFSMBIP8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsOFSMBIP8.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsOFSMBIP8.setUnits("count")
_TmnxOtuIfRawStatsHCSMBIP8_Type = Counter64
_TmnxOtuIfRawStatsHCSMBIP8_Object = MibTableColumn
tmnxOtuIfRawStatsHCSMBIP8 = _TmnxOtuIfRawStatsHCSMBIP8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 1, 1, 13),
    _TmnxOtuIfRawStatsHCSMBIP8_Type()
)
tmnxOtuIfRawStatsHCSMBIP8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsHCSMBIP8.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsHCSMBIP8.setUnits("bits")
_TmnxOtuIfRawStatsSMBEI_Type = Counter32
_TmnxOtuIfRawStatsSMBEI_Object = MibTableColumn
tmnxOtuIfRawStatsSMBEI = _TmnxOtuIfRawStatsSMBEI_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 1, 1, 14),
    _TmnxOtuIfRawStatsSMBEI_Type()
)
tmnxOtuIfRawStatsSMBEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsSMBEI.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsSMBEI.setUnits("bits")
_TmnxOtuIfRawStatsOFSMBEI_Type = Counter32
_TmnxOtuIfRawStatsOFSMBEI_Object = MibTableColumn
tmnxOtuIfRawStatsOFSMBEI = _TmnxOtuIfRawStatsOFSMBEI_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 1, 1, 15),
    _TmnxOtuIfRawStatsOFSMBEI_Type()
)
tmnxOtuIfRawStatsOFSMBEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsOFSMBEI.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsOFSMBEI.setUnits("count")
_TmnxOtuIfRawStatsHCSMBEI_Type = Counter64
_TmnxOtuIfRawStatsHCSMBEI_Object = MibTableColumn
tmnxOtuIfRawStatsHCSMBEI = _TmnxOtuIfRawStatsHCSMBEI_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 1, 1, 16),
    _TmnxOtuIfRawStatsHCSMBEI_Type()
)
tmnxOtuIfRawStatsHCSMBEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsHCSMBEI.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsHCSMBEI.setUnits("bits")
_TmnxOtuIfRawStatsSMSES_Type = Counter32
_TmnxOtuIfRawStatsSMSES_Object = MibTableColumn
tmnxOtuIfRawStatsSMSES = _TmnxOtuIfRawStatsSMSES_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 1, 1, 17),
    _TmnxOtuIfRawStatsSMSES_Type()
)
tmnxOtuIfRawStatsSMSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsSMSES.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsSMSES.setUnits("seconds")
_TmnxOtuIfRawStatsPMBIP8_Type = Counter32
_TmnxOtuIfRawStatsPMBIP8_Object = MibTableColumn
tmnxOtuIfRawStatsPMBIP8 = _TmnxOtuIfRawStatsPMBIP8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 1, 1, 18),
    _TmnxOtuIfRawStatsPMBIP8_Type()
)
tmnxOtuIfRawStatsPMBIP8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsPMBIP8.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsPMBIP8.setUnits("bits")
_TmnxOtuIfRawStatsOFPMBIP8_Type = Counter32
_TmnxOtuIfRawStatsOFPMBIP8_Object = MibTableColumn
tmnxOtuIfRawStatsOFPMBIP8 = _TmnxOtuIfRawStatsOFPMBIP8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 1, 1, 19),
    _TmnxOtuIfRawStatsOFPMBIP8_Type()
)
tmnxOtuIfRawStatsOFPMBIP8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsOFPMBIP8.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsOFPMBIP8.setUnits("count")
_TmnxOtuIfRawStatsHCPMBIP8_Type = Counter64
_TmnxOtuIfRawStatsHCPMBIP8_Object = MibTableColumn
tmnxOtuIfRawStatsHCPMBIP8 = _TmnxOtuIfRawStatsHCPMBIP8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 1, 1, 20),
    _TmnxOtuIfRawStatsHCPMBIP8_Type()
)
tmnxOtuIfRawStatsHCPMBIP8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsHCPMBIP8.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsHCPMBIP8.setUnits("bits")
_TmnxOtuIfRawStatsPMBEI_Type = Counter32
_TmnxOtuIfRawStatsPMBEI_Object = MibTableColumn
tmnxOtuIfRawStatsPMBEI = _TmnxOtuIfRawStatsPMBEI_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 1, 1, 21),
    _TmnxOtuIfRawStatsPMBEI_Type()
)
tmnxOtuIfRawStatsPMBEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsPMBEI.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsPMBEI.setUnits("bits")
_TmnxOtuIfRawStatsOFPMBEI_Type = Counter32
_TmnxOtuIfRawStatsOFPMBEI_Object = MibTableColumn
tmnxOtuIfRawStatsOFPMBEI = _TmnxOtuIfRawStatsOFPMBEI_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 1, 1, 22),
    _TmnxOtuIfRawStatsOFPMBEI_Type()
)
tmnxOtuIfRawStatsOFPMBEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsOFPMBEI.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsOFPMBEI.setUnits("count")
_TmnxOtuIfRawStatsHCPMBEI_Type = Counter64
_TmnxOtuIfRawStatsHCPMBEI_Object = MibTableColumn
tmnxOtuIfRawStatsHCPMBEI = _TmnxOtuIfRawStatsHCPMBEI_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 1, 1, 23),
    _TmnxOtuIfRawStatsHCPMBEI_Type()
)
tmnxOtuIfRawStatsHCPMBEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsHCPMBEI.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsHCPMBEI.setUnits("bits")
_TmnxOtuIfRawStatsPMSES_Type = Counter32
_TmnxOtuIfRawStatsPMSES_Object = MibTableColumn
tmnxOtuIfRawStatsPMSES = _TmnxOtuIfRawStatsPMSES_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 1, 1, 24),
    _TmnxOtuIfRawStatsPMSES_Type()
)
tmnxOtuIfRawStatsPMSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsPMSES.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsPMSES.setUnits("seconds")
_TmnxOtuIfRawStatsFECES_Type = Counter32
_TmnxOtuIfRawStatsFECES_Object = MibTableColumn
tmnxOtuIfRawStatsFECES = _TmnxOtuIfRawStatsFECES_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 1, 1, 25),
    _TmnxOtuIfRawStatsFECES_Type()
)
tmnxOtuIfRawStatsFECES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsFECES.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsFECES.setUnits("seconds")
_TmnxOtuIfRawStatsFECUAS_Type = Counter32
_TmnxOtuIfRawStatsFECUAS_Object = MibTableColumn
tmnxOtuIfRawStatsFECUAS = _TmnxOtuIfRawStatsFECUAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 1, 1, 26),
    _TmnxOtuIfRawStatsFECUAS_Type()
)
tmnxOtuIfRawStatsFECUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsFECUAS.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsFECUAS.setUnits("seconds")
_TmnxOtuIfRawStatsSMES_Type = Counter32
_TmnxOtuIfRawStatsSMES_Object = MibTableColumn
tmnxOtuIfRawStatsSMES = _TmnxOtuIfRawStatsSMES_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 1, 1, 27),
    _TmnxOtuIfRawStatsSMES_Type()
)
tmnxOtuIfRawStatsSMES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsSMES.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsSMES.setUnits("seconds")
_TmnxOtuIfRawStatsSMUAS_Type = Counter32
_TmnxOtuIfRawStatsSMUAS_Object = MibTableColumn
tmnxOtuIfRawStatsSMUAS = _TmnxOtuIfRawStatsSMUAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 1, 1, 28),
    _TmnxOtuIfRawStatsSMUAS_Type()
)
tmnxOtuIfRawStatsSMUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsSMUAS.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsSMUAS.setUnits("seconds")
_TmnxOtuIfRawStatsPMES_Type = Counter32
_TmnxOtuIfRawStatsPMES_Object = MibTableColumn
tmnxOtuIfRawStatsPMES = _TmnxOtuIfRawStatsPMES_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 1, 1, 29),
    _TmnxOtuIfRawStatsPMES_Type()
)
tmnxOtuIfRawStatsPMES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsPMES.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsPMES.setUnits("seconds")
_TmnxOtuIfRawStatsPMUAS_Type = Counter32
_TmnxOtuIfRawStatsPMUAS_Object = MibTableColumn
tmnxOtuIfRawStatsPMUAS = _TmnxOtuIfRawStatsPMUAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 1, 1, 30),
    _TmnxOtuIfRawStatsPMUAS_Type()
)
tmnxOtuIfRawStatsPMUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsPMUAS.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsPMUAS.setUnits("seconds")
_TmnxOtuIfRawStatsNPJ_Type = Counter32
_TmnxOtuIfRawStatsNPJ_Object = MibTableColumn
tmnxOtuIfRawStatsNPJ = _TmnxOtuIfRawStatsNPJ_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 1, 1, 31),
    _TmnxOtuIfRawStatsNPJ_Type()
)
tmnxOtuIfRawStatsNPJ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsNPJ.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsNPJ.setUnits("count")
_TmnxOtuIfRawStatsPPJ_Type = Counter32
_TmnxOtuIfRawStatsPPJ_Object = MibTableColumn
tmnxOtuIfRawStatsPPJ = _TmnxOtuIfRawStatsPPJ_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 1, 1, 32),
    _TmnxOtuIfRawStatsPPJ_Type()
)
tmnxOtuIfRawStatsPPJ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsPPJ.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsPPJ.setUnits("count")
_TmnxOtuIfRawStatsElapsedSec_Type = Counter32
_TmnxOtuIfRawStatsElapsedSec_Object = MibTableColumn
tmnxOtuIfRawStatsElapsedSec = _TmnxOtuIfRawStatsElapsedSec_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 1, 1, 33),
    _TmnxOtuIfRawStatsElapsedSec_Type()
)
tmnxOtuIfRawStatsElapsedSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsElapsedSec.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfRawStatsElapsedSec.setUnits("seconds")
_TmnxOtuIfIntervalStatsTable_Object = MibTable
tmnxOtuIfIntervalStatsTable = _TmnxOtuIfIntervalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 2)
)
if mibBuilder.loadTexts:
    tmnxOtuIfIntervalStatsTable.setStatus("current")
_TmnxOtuIfIntervalStatsEntry_Object = MibTableRow
tmnxOtuIfIntervalStatsEntry = _TmnxOtuIfIntervalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 2, 1)
)
tmnxOtuIfIntervalStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TIMETRA-OTU-MIB", "tmnxOtuIfIntvlStatsIndex"),
)
if mibBuilder.loadTexts:
    tmnxOtuIfIntervalStatsEntry.setStatus("current")


class _TmnxOtuIfIntvlStatsIndex_Type(Unsigned32):
    """Custom type tmnxOtuIfIntvlStatsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 96),
    )


_TmnxOtuIfIntvlStatsIndex_Type.__name__ = "Unsigned32"
_TmnxOtuIfIntvlStatsIndex_Object = MibTableColumn
tmnxOtuIfIntvlStatsIndex = _TmnxOtuIfIntvlStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 2, 1, 1),
    _TmnxOtuIfIntvlStatsIndex_Type()
)
tmnxOtuIfIntvlStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOtuIfIntvlStatsIndex.setStatus("current")
_TmnxOtuIfIntvlStatsIsValid_Type = TruthValue
_TmnxOtuIfIntvlStatsIsValid_Object = MibTableColumn
tmnxOtuIfIntvlStatsIsValid = _TmnxOtuIfIntvlStatsIsValid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 2, 1, 2),
    _TmnxOtuIfIntvlStatsIsValid_Type()
)
tmnxOtuIfIntvlStatsIsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfIntvlStatsIsValid.setStatus("current")
_TmnxOtuIfIntvlStatsFECCorrZeros_Type = Counter32
_TmnxOtuIfIntvlStatsFECCorrZeros_Object = MibTableColumn
tmnxOtuIfIntvlStatsFECCorrZeros = _TmnxOtuIfIntvlStatsFECCorrZeros_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 2, 1, 3),
    _TmnxOtuIfIntvlStatsFECCorrZeros_Type()
)
tmnxOtuIfIntvlStatsFECCorrZeros.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfIntvlStatsFECCorrZeros.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfIntvlStatsFECCorrZeros.setUnits("bits")
_TmnxOtuIfIntvlStatsFECCorrOnes_Type = Counter32
_TmnxOtuIfIntvlStatsFECCorrOnes_Object = MibTableColumn
tmnxOtuIfIntvlStatsFECCorrOnes = _TmnxOtuIfIntvlStatsFECCorrOnes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 2, 1, 4),
    _TmnxOtuIfIntvlStatsFECCorrOnes_Type()
)
tmnxOtuIfIntvlStatsFECCorrOnes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfIntvlStatsFECCorrOnes.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfIntvlStatsFECCorrOnes.setUnits("bits")
_TmnxOtuIfIntvlStatsFECUncorrSR_Type = Counter32
_TmnxOtuIfIntvlStatsFECUncorrSR_Object = MibTableColumn
tmnxOtuIfIntvlStatsFECUncorrSR = _TmnxOtuIfIntvlStatsFECUncorrSR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 2, 1, 5),
    _TmnxOtuIfIntvlStatsFECUncorrSR_Type()
)
tmnxOtuIfIntvlStatsFECUncorrSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfIntvlStatsFECUncorrSR.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfIntvlStatsFECUncorrSR.setUnits("Sub-Rows")
_TmnxOtuIfIntvlStatsFECSES_Type = Counter32
_TmnxOtuIfIntvlStatsFECSES_Object = MibTableColumn
tmnxOtuIfIntvlStatsFECSES = _TmnxOtuIfIntvlStatsFECSES_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 2, 1, 6),
    _TmnxOtuIfIntvlStatsFECSES_Type()
)
tmnxOtuIfIntvlStatsFECSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfIntvlStatsFECSES.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfIntvlStatsFECSES.setUnits("seconds")
_TmnxOtuIfIntvlStatsSMBIP8_Type = Counter32
_TmnxOtuIfIntvlStatsSMBIP8_Object = MibTableColumn
tmnxOtuIfIntvlStatsSMBIP8 = _TmnxOtuIfIntvlStatsSMBIP8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 2, 1, 7),
    _TmnxOtuIfIntvlStatsSMBIP8_Type()
)
tmnxOtuIfIntvlStatsSMBIP8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfIntvlStatsSMBIP8.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfIntvlStatsSMBIP8.setUnits("bits")
_TmnxOtuIfIntvlStatsSMBEI_Type = Counter32
_TmnxOtuIfIntvlStatsSMBEI_Object = MibTableColumn
tmnxOtuIfIntvlStatsSMBEI = _TmnxOtuIfIntvlStatsSMBEI_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 2, 1, 8),
    _TmnxOtuIfIntvlStatsSMBEI_Type()
)
tmnxOtuIfIntvlStatsSMBEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfIntvlStatsSMBEI.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfIntvlStatsSMBEI.setUnits("bits")
_TmnxOtuIfIntvlStatsSMSES_Type = Counter32
_TmnxOtuIfIntvlStatsSMSES_Object = MibTableColumn
tmnxOtuIfIntvlStatsSMSES = _TmnxOtuIfIntvlStatsSMSES_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 2, 1, 9),
    _TmnxOtuIfIntvlStatsSMSES_Type()
)
tmnxOtuIfIntvlStatsSMSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfIntvlStatsSMSES.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfIntvlStatsSMSES.setUnits("seconds")
_TmnxOtuIfIntvlStatsPMBIP8_Type = Counter32
_TmnxOtuIfIntvlStatsPMBIP8_Object = MibTableColumn
tmnxOtuIfIntvlStatsPMBIP8 = _TmnxOtuIfIntvlStatsPMBIP8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 2, 1, 10),
    _TmnxOtuIfIntvlStatsPMBIP8_Type()
)
tmnxOtuIfIntvlStatsPMBIP8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfIntvlStatsPMBIP8.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfIntvlStatsPMBIP8.setUnits("bits")
_TmnxOtuIfIntvlStatsPMBEI_Type = Counter32
_TmnxOtuIfIntvlStatsPMBEI_Object = MibTableColumn
tmnxOtuIfIntvlStatsPMBEI = _TmnxOtuIfIntvlStatsPMBEI_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 2, 1, 11),
    _TmnxOtuIfIntvlStatsPMBEI_Type()
)
tmnxOtuIfIntvlStatsPMBEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfIntvlStatsPMBEI.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfIntvlStatsPMBEI.setUnits("bits")
_TmnxOtuIfIntvlStatsPMSES_Type = Counter32
_TmnxOtuIfIntvlStatsPMSES_Object = MibTableColumn
tmnxOtuIfIntvlStatsPMSES = _TmnxOtuIfIntvlStatsPMSES_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 2, 1, 12),
    _TmnxOtuIfIntvlStatsPMSES_Type()
)
tmnxOtuIfIntvlStatsPMSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfIntvlStatsPMSES.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfIntvlStatsPMSES.setUnits("seconds")
_TmnxOtuIfIntvlStatsFECES_Type = Counter32
_TmnxOtuIfIntvlStatsFECES_Object = MibTableColumn
tmnxOtuIfIntvlStatsFECES = _TmnxOtuIfIntvlStatsFECES_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 2, 1, 13),
    _TmnxOtuIfIntvlStatsFECES_Type()
)
tmnxOtuIfIntvlStatsFECES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfIntvlStatsFECES.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfIntvlStatsFECES.setUnits("seconds")
_TmnxOtuIfIntvlStatsFECUAS_Type = Counter32
_TmnxOtuIfIntvlStatsFECUAS_Object = MibTableColumn
tmnxOtuIfIntvlStatsFECUAS = _TmnxOtuIfIntvlStatsFECUAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 2, 1, 14),
    _TmnxOtuIfIntvlStatsFECUAS_Type()
)
tmnxOtuIfIntvlStatsFECUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfIntvlStatsFECUAS.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfIntvlStatsFECUAS.setUnits("seconds")
_TmnxOtuIfIntvlStatsSMES_Type = Counter32
_TmnxOtuIfIntvlStatsSMES_Object = MibTableColumn
tmnxOtuIfIntvlStatsSMES = _TmnxOtuIfIntvlStatsSMES_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 2, 1, 15),
    _TmnxOtuIfIntvlStatsSMES_Type()
)
tmnxOtuIfIntvlStatsSMES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfIntvlStatsSMES.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfIntvlStatsSMES.setUnits("seconds")
_TmnxOtuIfIntvlStatsSMUAS_Type = Counter32
_TmnxOtuIfIntvlStatsSMUAS_Object = MibTableColumn
tmnxOtuIfIntvlStatsSMUAS = _TmnxOtuIfIntvlStatsSMUAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 2, 1, 16),
    _TmnxOtuIfIntvlStatsSMUAS_Type()
)
tmnxOtuIfIntvlStatsSMUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfIntvlStatsSMUAS.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfIntvlStatsSMUAS.setUnits("seconds")
_TmnxOtuIfIntvlStatsPMES_Type = Counter32
_TmnxOtuIfIntvlStatsPMES_Object = MibTableColumn
tmnxOtuIfIntvlStatsPMES = _TmnxOtuIfIntvlStatsPMES_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 2, 1, 17),
    _TmnxOtuIfIntvlStatsPMES_Type()
)
tmnxOtuIfIntvlStatsPMES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfIntvlStatsPMES.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfIntvlStatsPMES.setUnits("seconds")
_TmnxOtuIfIntvlStatsPMUAS_Type = Counter32
_TmnxOtuIfIntvlStatsPMUAS_Object = MibTableColumn
tmnxOtuIfIntvlStatsPMUAS = _TmnxOtuIfIntvlStatsPMUAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 2, 1, 18),
    _TmnxOtuIfIntvlStatsPMUAS_Type()
)
tmnxOtuIfIntvlStatsPMUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfIntvlStatsPMUAS.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfIntvlStatsPMUAS.setUnits("seconds")
_TmnxOtuIfIntvlStatsNPJ_Type = Counter32
_TmnxOtuIfIntvlStatsNPJ_Object = MibTableColumn
tmnxOtuIfIntvlStatsNPJ = _TmnxOtuIfIntvlStatsNPJ_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 2, 1, 19),
    _TmnxOtuIfIntvlStatsNPJ_Type()
)
tmnxOtuIfIntvlStatsNPJ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfIntvlStatsNPJ.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfIntvlStatsNPJ.setUnits("count")
_TmnxOtuIfIntvlStatsPPJ_Type = Counter32
_TmnxOtuIfIntvlStatsPPJ_Object = MibTableColumn
tmnxOtuIfIntvlStatsPPJ = _TmnxOtuIfIntvlStatsPPJ_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 2, 1, 20),
    _TmnxOtuIfIntvlStatsPPJ_Type()
)
tmnxOtuIfIntvlStatsPPJ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfIntvlStatsPPJ.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfIntvlStatsPPJ.setUnits("count")
_TmnxOtuIfIntvlStatsElapsedSec_Type = Counter32
_TmnxOtuIfIntvlStatsElapsedSec_Object = MibTableColumn
tmnxOtuIfIntvlStatsElapsedSec = _TmnxOtuIfIntvlStatsElapsedSec_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 62, 2, 2, 1, 21),
    _TmnxOtuIfIntvlStatsElapsedSec_Type()
)
tmnxOtuIfIntvlStatsElapsedSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOtuIfIntvlStatsElapsedSec.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOtuIfIntvlStatsElapsedSec.setUnits("seconds")
_TmnxOtuNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxOtuNotifyPrefix = _TmnxOtuNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 62)
)
_TmnxOtuNotifications_ObjectIdentity = ObjectIdentity
tmnxOtuNotifications = _TmnxOtuNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 62, 0)
)

# Managed Objects groups

tmnxOtuIfBaseConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 62, 2, 1)
)
tmnxOtuIfBaseConfigGroup.setObjects(
      *(("TIMETRA-OTU-MIB", "tmnxOtuIfTableLastChanged"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfRowStatus"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfTimeStamp"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfFecMode"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfSfSdMethod"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfBerSfThreshold"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfBerSdThreshold"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfOtu2LanDataRate"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfCfgAlarms"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfAlarmState"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfHoldTimeUp"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfHoldTimeDown"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfOtuOperDataRate"))
)
if mibBuilder.loadTexts:
    tmnxOtuIfBaseConfigGroup.setStatus("obsolete")

tmnxOtuIfSMGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 62, 2, 2)
)
tmnxOtuIfSMGroup.setObjects(
      *(("TIMETRA-OTU-MIB", "tmnxOtuIfSmTtiTxMode"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfSmTtiTx"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfSmTtiRx"))
)
if mibBuilder.loadTexts:
    tmnxOtuIfSMGroup.setStatus("current")

tmnxOtuStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 62, 2, 3)
)
tmnxOtuStatsGroup.setObjects(
      *(("TIMETRA-OTU-MIB", "tmnxOtuIfRawStatsFECCorrZeros"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfRawStatsOFFECCorrZeros"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfRawStatsHCFECCorrZeros"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfRawStatsFECCorrOnes"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfRawStatsOFFECCorrOnes"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfRawStatsHCFECCorrOnes"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfRawStatsFECUncorrSR"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfRawStatsOFFECUncorrSR"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfRawStatsHCFECUncorrSR"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfRawStatsFECSES"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfRawStatsSMBIP8"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfRawStatsOFSMBIP8"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfRawStatsHCSMBIP8"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfRawStatsSMBEI"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfRawStatsOFSMBEI"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfRawStatsHCSMBEI"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfRawStatsSMSES"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfRawStatsPMBIP8"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfRawStatsOFPMBIP8"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfRawStatsHCPMBIP8"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfRawStatsPMBEI"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfRawStatsOFPMBEI"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfRawStatsHCPMBEI"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfRawStatsPMSES"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfIntvlStatsIsValid"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfIntvlStatsFECCorrZeros"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfIntvlStatsFECCorrOnes"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfIntvlStatsFECUncorrSR"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfIntvlStatsFECSES"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfIntvlStatsSMBIP8"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfIntvlStatsSMBEI"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfIntvlStatsSMSES"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfIntvlStatsPMBIP8"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfIntvlStatsPMBEI"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfIntvlStatsPMSES"))
)
if mibBuilder.loadTexts:
    tmnxOtuStatsGroup.setStatus("current")

tmnxOtuIfBaseConfigGroupV8v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 62, 2, 6, 1)
)
tmnxOtuIfBaseConfigGroupV8v0.setObjects(
      *(("TIMETRA-OTU-MIB", "tmnxOtuIfTableLastChanged"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfRowStatus"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfTimeStamp"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfFecMode"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfSfSdMethod"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfBerSfThreshold"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfBerSdThreshold"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfOtu2LanDataRate"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfCfgAlarms"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfAlarmState"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfOtuOperDataRate"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfAsyncMappingEnable"))
)
if mibBuilder.loadTexts:
    tmnxOtuIfBaseConfigGroupV8v0.setStatus("current")

tmnxOtuIfSMGroupV8v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 62, 2, 6, 2)
)
tmnxOtuIfSMGroupV8v0.setObjects(
      *(("TIMETRA-OTU-MIB", "tmnxOtuIfSmTtiTxMode"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfSmTtiTx"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfSmTtiRx"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfSmTtiExpMode"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfSmTtiExpCopyRx"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfSmTtiExp"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfSmTimReaction"))
)
if mibBuilder.loadTexts:
    tmnxOtuIfSMGroupV8v0.setStatus("current")

tmnxOtuStatsGroupV8v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 62, 2, 6, 3)
)
tmnxOtuStatsGroupV8v0.setObjects(
      *(("TIMETRA-OTU-MIB", "tmnxOtuIfRawStatsFECES"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfRawStatsFECUAS"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfRawStatsSMES"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfRawStatsSMUAS"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfRawStatsPMES"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfRawStatsPMUAS"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfRawStatsNPJ"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfRawStatsPPJ"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfRawStatsElapsedSec"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfIntvlStatsFECES"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfIntvlStatsFECUAS"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfIntvlStatsSMES"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfIntvlStatsSMUAS"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfIntvlStatsPMES"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfIntvlStatsPMUAS"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfIntvlStatsPPJ"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfIntvlStatsNPJ"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfIntvlStatsElapsedSec"))
)
if mibBuilder.loadTexts:
    tmnxOtuStatsGroupV8v0.setStatus("current")

tmnxOtuIfPMGroupV8v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 62, 2, 6, 4)
)
tmnxOtuIfPMGroupV8v0.setObjects(
      *(("TIMETRA-OTU-MIB", "tmnxOtuIfPmTtiTxMode"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfPmTtiTx"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfPmTtiRx"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfPmTtiExpMode"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfPmTtiExpCopyRx"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfPmTtiExp"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfPmTimReaction"))
)
if mibBuilder.loadTexts:
    tmnxOtuIfPMGroupV8v0.setStatus("current")

tmnxOtuIfPSIGroupV8v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 62, 2, 6, 5)
)
tmnxOtuIfPSIGroupV8v0.setObjects(
      *(("TIMETRA-OTU-MIB", "tmnxOtuIfPsiTtiTxMode"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfPsiTtiTx"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfPsiTtiRx"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfPsiTtiExpMode"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfPsiTtiExpCopyRx"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfPsiTtiExp"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfPsiPayloadTypeTx"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfPsiPayloadTypeRx"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfPsiPayloadTypeExp"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfPsiTimReaction"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfPsiPlmReaction"))
)
if mibBuilder.loadTexts:
    tmnxOtuIfPSIGroupV8v0.setStatus("current")

tmnxOtuObsoleteV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 62, 2, 6, 6)
)
tmnxOtuObsoleteV8v0Group.setObjects(
      *(("TIMETRA-OTU-MIB", "tmnxOtuIfHoldTimeUp"),
        ("TIMETRA-OTU-MIB", "tmnxOtuIfHoldTimeDown"))
)
if mibBuilder.loadTexts:
    tmnxOtuObsoleteV8v0Group.setStatus("current")


# Notification objects

tmnxOtuIfAlarmNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 62, 0, 1)
)
tmnxOtuIfAlarmNotification.setObjects(
    ("TIMETRA-OTU-MIB", "tmnxOtuIfAlarmState")
)
if mibBuilder.loadTexts:
    tmnxOtuIfAlarmNotification.setStatus(
        "current"
    )


# Notifications groups

tmnxOtuNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 62, 2, 4)
)
tmnxOtuNotificationGroup.setObjects(
    ("TIMETRA-OTU-MIB", "tmnxOtuIfAlarmNotification")
)
if mibBuilder.loadTexts:
    tmnxOtuNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxOtuCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 62, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxOtuCompliance.setStatus(
        "obsolete"
    )

tmnxOtuComplianceV8v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 62, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxOtuComplianceV8v0.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-OTU-MIB",
    **{"TmnxOtuFecMode": TmnxOtuFecMode,
       "TmnxOtu2LanDataRate": TmnxOtu2LanDataRate,
       "TmnxOtuSFSDMethod": TmnxOtuSFSDMethod,
       "TmnxOtuTtiMode": TmnxOtuTtiMode,
       "TmnxOtuTtiString": TmnxOtuTtiString,
       "TmnxOtuAlarms": TmnxOtuAlarms,
       "TmnxOtuPsiPayloadType": TmnxOtuPsiPayloadType,
       "TmnxOtuTimReaction": TmnxOtuTimReaction,
       "tmnxOtuMIBModule": tmnxOtuMIBModule,
       "tmnxOtuConformance": tmnxOtuConformance,
       "tmnxOtuCompliances": tmnxOtuCompliances,
       "tmnxOtuCompliance": tmnxOtuCompliance,
       "tmnxOtuComplianceV8v0": tmnxOtuComplianceV8v0,
       "tmnxOtuGroups": tmnxOtuGroups,
       "tmnxOtuIfBaseConfigGroup": tmnxOtuIfBaseConfigGroup,
       "tmnxOtuIfSMGroup": tmnxOtuIfSMGroup,
       "tmnxOtuStatsGroup": tmnxOtuStatsGroup,
       "tmnxOtuNotificationGroup": tmnxOtuNotificationGroup,
       "tmnxOtuGroupsV7v0": tmnxOtuGroupsV7v0,
       "tmnxOtuGroupsV8v0": tmnxOtuGroupsV8v0,
       "tmnxOtuIfBaseConfigGroupV8v0": tmnxOtuIfBaseConfigGroupV8v0,
       "tmnxOtuIfSMGroupV8v0": tmnxOtuIfSMGroupV8v0,
       "tmnxOtuStatsGroupV8v0": tmnxOtuStatsGroupV8v0,
       "tmnxOtuIfPMGroupV8v0": tmnxOtuIfPMGroupV8v0,
       "tmnxOtuIfPSIGroupV8v0": tmnxOtuIfPSIGroupV8v0,
       "tmnxOtuObsoleteV8v0Group": tmnxOtuObsoleteV8v0Group,
       "tmnxOtuObjs": tmnxOtuObjs,
       "tmnxOtuConfigurationTimeStamps": tmnxOtuConfigurationTimeStamps,
       "tmnxOtuIfTableLastChanged": tmnxOtuIfTableLastChanged,
       "tmnxOtuConfigurations": tmnxOtuConfigurations,
       "tmnxOtuIfTable": tmnxOtuIfTable,
       "tmnxOtuIfEntry": tmnxOtuIfEntry,
       "tmnxOtuIfRowStatus": tmnxOtuIfRowStatus,
       "tmnxOtuIfTimeStamp": tmnxOtuIfTimeStamp,
       "tmnxOtuIfFecMode": tmnxOtuIfFecMode,
       "tmnxOtuIfSfSdMethod": tmnxOtuIfSfSdMethod,
       "tmnxOtuIfBerSfThreshold": tmnxOtuIfBerSfThreshold,
       "tmnxOtuIfBerSdThreshold": tmnxOtuIfBerSdThreshold,
       "tmnxOtuIfOtuOperDataRate": tmnxOtuIfOtuOperDataRate,
       "tmnxOtuIfOtu2LanDataRate": tmnxOtuIfOtu2LanDataRate,
       "tmnxOtuIfCfgAlarms": tmnxOtuIfCfgAlarms,
       "tmnxOtuIfAlarmState": tmnxOtuIfAlarmState,
       "tmnxOtuIfHoldTimeUp": tmnxOtuIfHoldTimeUp,
       "tmnxOtuIfHoldTimeDown": tmnxOtuIfHoldTimeDown,
       "tmnxOtuIfSmTtiTxMode": tmnxOtuIfSmTtiTxMode,
       "tmnxOtuIfSmTtiTx": tmnxOtuIfSmTtiTx,
       "tmnxOtuIfSmTtiRx": tmnxOtuIfSmTtiRx,
       "tmnxOtuIfSmTtiExpMode": tmnxOtuIfSmTtiExpMode,
       "tmnxOtuIfSmTtiExpCopyRx": tmnxOtuIfSmTtiExpCopyRx,
       "tmnxOtuIfSmTtiExp": tmnxOtuIfSmTtiExp,
       "tmnxOtuIfPmTtiTxMode": tmnxOtuIfPmTtiTxMode,
       "tmnxOtuIfPmTtiTx": tmnxOtuIfPmTtiTx,
       "tmnxOtuIfPmTtiRx": tmnxOtuIfPmTtiRx,
       "tmnxOtuIfPmTtiExpMode": tmnxOtuIfPmTtiExpMode,
       "tmnxOtuIfPmTtiExpCopyRx": tmnxOtuIfPmTtiExpCopyRx,
       "tmnxOtuIfPmTtiExp": tmnxOtuIfPmTtiExp,
       "tmnxOtuIfPsiTtiTxMode": tmnxOtuIfPsiTtiTxMode,
       "tmnxOtuIfPsiTtiTx": tmnxOtuIfPsiTtiTx,
       "tmnxOtuIfPsiTtiRx": tmnxOtuIfPsiTtiRx,
       "tmnxOtuIfPsiTtiExpMode": tmnxOtuIfPsiTtiExpMode,
       "tmnxOtuIfPsiTtiExpCopyRx": tmnxOtuIfPsiTtiExpCopyRx,
       "tmnxOtuIfPsiTtiExp": tmnxOtuIfPsiTtiExp,
       "tmnxOtuIfPsiPayloadTypeTx": tmnxOtuIfPsiPayloadTypeTx,
       "tmnxOtuIfPsiPayloadTypeRx": tmnxOtuIfPsiPayloadTypeRx,
       "tmnxOtuIfPsiPayloadTypeExp": tmnxOtuIfPsiPayloadTypeExp,
       "tmnxOtuIfGfpMappingEnable": tmnxOtuIfGfpMappingEnable,
       "tmnxOtuIfAsyncMappingEnable": tmnxOtuIfAsyncMappingEnable,
       "tmnxOtuIfSmTimReaction": tmnxOtuIfSmTimReaction,
       "tmnxOtuIfPmTimReaction": tmnxOtuIfPmTimReaction,
       "tmnxOtuIfPsiTimReaction": tmnxOtuIfPsiTimReaction,
       "tmnxOtuIfPsiPlmReaction": tmnxOtuIfPsiPlmReaction,
       "tmnxOtuStatistics": tmnxOtuStatistics,
       "tmnxOtuIfRawStatsTable": tmnxOtuIfRawStatsTable,
       "tmnxOtuIfRawStatsEntry": tmnxOtuIfRawStatsEntry,
       "tmnxOtuIfRawStatsFECCorrZeros": tmnxOtuIfRawStatsFECCorrZeros,
       "tmnxOtuIfRawStatsOFFECCorrZeros": tmnxOtuIfRawStatsOFFECCorrZeros,
       "tmnxOtuIfRawStatsHCFECCorrZeros": tmnxOtuIfRawStatsHCFECCorrZeros,
       "tmnxOtuIfRawStatsFECCorrOnes": tmnxOtuIfRawStatsFECCorrOnes,
       "tmnxOtuIfRawStatsOFFECCorrOnes": tmnxOtuIfRawStatsOFFECCorrOnes,
       "tmnxOtuIfRawStatsHCFECCorrOnes": tmnxOtuIfRawStatsHCFECCorrOnes,
       "tmnxOtuIfRawStatsFECUncorrSR": tmnxOtuIfRawStatsFECUncorrSR,
       "tmnxOtuIfRawStatsOFFECUncorrSR": tmnxOtuIfRawStatsOFFECUncorrSR,
       "tmnxOtuIfRawStatsHCFECUncorrSR": tmnxOtuIfRawStatsHCFECUncorrSR,
       "tmnxOtuIfRawStatsFECSES": tmnxOtuIfRawStatsFECSES,
       "tmnxOtuIfRawStatsSMBIP8": tmnxOtuIfRawStatsSMBIP8,
       "tmnxOtuIfRawStatsOFSMBIP8": tmnxOtuIfRawStatsOFSMBIP8,
       "tmnxOtuIfRawStatsHCSMBIP8": tmnxOtuIfRawStatsHCSMBIP8,
       "tmnxOtuIfRawStatsSMBEI": tmnxOtuIfRawStatsSMBEI,
       "tmnxOtuIfRawStatsOFSMBEI": tmnxOtuIfRawStatsOFSMBEI,
       "tmnxOtuIfRawStatsHCSMBEI": tmnxOtuIfRawStatsHCSMBEI,
       "tmnxOtuIfRawStatsSMSES": tmnxOtuIfRawStatsSMSES,
       "tmnxOtuIfRawStatsPMBIP8": tmnxOtuIfRawStatsPMBIP8,
       "tmnxOtuIfRawStatsOFPMBIP8": tmnxOtuIfRawStatsOFPMBIP8,
       "tmnxOtuIfRawStatsHCPMBIP8": tmnxOtuIfRawStatsHCPMBIP8,
       "tmnxOtuIfRawStatsPMBEI": tmnxOtuIfRawStatsPMBEI,
       "tmnxOtuIfRawStatsOFPMBEI": tmnxOtuIfRawStatsOFPMBEI,
       "tmnxOtuIfRawStatsHCPMBEI": tmnxOtuIfRawStatsHCPMBEI,
       "tmnxOtuIfRawStatsPMSES": tmnxOtuIfRawStatsPMSES,
       "tmnxOtuIfRawStatsFECES": tmnxOtuIfRawStatsFECES,
       "tmnxOtuIfRawStatsFECUAS": tmnxOtuIfRawStatsFECUAS,
       "tmnxOtuIfRawStatsSMES": tmnxOtuIfRawStatsSMES,
       "tmnxOtuIfRawStatsSMUAS": tmnxOtuIfRawStatsSMUAS,
       "tmnxOtuIfRawStatsPMES": tmnxOtuIfRawStatsPMES,
       "tmnxOtuIfRawStatsPMUAS": tmnxOtuIfRawStatsPMUAS,
       "tmnxOtuIfRawStatsNPJ": tmnxOtuIfRawStatsNPJ,
       "tmnxOtuIfRawStatsPPJ": tmnxOtuIfRawStatsPPJ,
       "tmnxOtuIfRawStatsElapsedSec": tmnxOtuIfRawStatsElapsedSec,
       "tmnxOtuIfIntervalStatsTable": tmnxOtuIfIntervalStatsTable,
       "tmnxOtuIfIntervalStatsEntry": tmnxOtuIfIntervalStatsEntry,
       "tmnxOtuIfIntvlStatsIndex": tmnxOtuIfIntvlStatsIndex,
       "tmnxOtuIfIntvlStatsIsValid": tmnxOtuIfIntvlStatsIsValid,
       "tmnxOtuIfIntvlStatsFECCorrZeros": tmnxOtuIfIntvlStatsFECCorrZeros,
       "tmnxOtuIfIntvlStatsFECCorrOnes": tmnxOtuIfIntvlStatsFECCorrOnes,
       "tmnxOtuIfIntvlStatsFECUncorrSR": tmnxOtuIfIntvlStatsFECUncorrSR,
       "tmnxOtuIfIntvlStatsFECSES": tmnxOtuIfIntvlStatsFECSES,
       "tmnxOtuIfIntvlStatsSMBIP8": tmnxOtuIfIntvlStatsSMBIP8,
       "tmnxOtuIfIntvlStatsSMBEI": tmnxOtuIfIntvlStatsSMBEI,
       "tmnxOtuIfIntvlStatsSMSES": tmnxOtuIfIntvlStatsSMSES,
       "tmnxOtuIfIntvlStatsPMBIP8": tmnxOtuIfIntvlStatsPMBIP8,
       "tmnxOtuIfIntvlStatsPMBEI": tmnxOtuIfIntvlStatsPMBEI,
       "tmnxOtuIfIntvlStatsPMSES": tmnxOtuIfIntvlStatsPMSES,
       "tmnxOtuIfIntvlStatsFECES": tmnxOtuIfIntvlStatsFECES,
       "tmnxOtuIfIntvlStatsFECUAS": tmnxOtuIfIntvlStatsFECUAS,
       "tmnxOtuIfIntvlStatsSMES": tmnxOtuIfIntvlStatsSMES,
       "tmnxOtuIfIntvlStatsSMUAS": tmnxOtuIfIntvlStatsSMUAS,
       "tmnxOtuIfIntvlStatsPMES": tmnxOtuIfIntvlStatsPMES,
       "tmnxOtuIfIntvlStatsPMUAS": tmnxOtuIfIntvlStatsPMUAS,
       "tmnxOtuIfIntvlStatsNPJ": tmnxOtuIfIntvlStatsNPJ,
       "tmnxOtuIfIntvlStatsPPJ": tmnxOtuIfIntvlStatsPPJ,
       "tmnxOtuIfIntvlStatsElapsedSec": tmnxOtuIfIntvlStatsElapsedSec,
       "tmnxOtuNotifyPrefix": tmnxOtuNotifyPrefix,
       "tmnxOtuNotifications": tmnxOtuNotifications,
       "tmnxOtuIfAlarmNotification": tmnxOtuIfAlarmNotification}
)
