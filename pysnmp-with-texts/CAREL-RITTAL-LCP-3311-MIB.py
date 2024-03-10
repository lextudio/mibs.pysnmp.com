"""SNMP MIB module (CAREL-RITTAL-LCP-3311-MIB) expressed in pysnmp data model.

This Python module is designed to be imported and executed by the
pysnmp library.

See https://www.pysnmp.com/pysnmp for further information.

Notes
-----
ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CAREL-RITTAL-LCP-3311-MIB.txt
Produced by pysmi-1.3.3 at Sun Mar 10 10:25:33 2024
On host MacBook-Pro.local platform Darwin version 23.4.0 by user lextm
Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]
"""
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

(NotificationGroup,
 ObjectGroup,
 ModuleCompliance) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "NotificationGroup",
    "ObjectGroup",
    "ModuleCompliance")

(ModuleIdentity,
 Bits,
 Integer32,
 Counter32,
 IpAddress,
 TimeTicks,
 Gauge32,
 NotificationType,
 Unsigned32,
 ObjectIdentity,
 iso,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 enterprises,
 Counter64,
 MibIdentifier) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "ModuleIdentity",
    "Bits",
    "Integer32",
    "Counter32",
    "IpAddress",
    "TimeTicks",
    "Gauge32",
    "NotificationType",
    "Unsigned32",
    "ObjectIdentity",
    "iso",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "enterprises",
    "Counter64",
    "MibIdentifier")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

carel = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9839)
)
carel.setRevisions(
        ("2021-06-29 00:00",)
)
carel.setLastUpdated("202106290000Z")
if mibBuilder.loadTexts:
    carel.setOrganization("""\
Epiecs
""")
carel.setContactInfo("""\
EPIECS epiecs.be Email: gregorybers@epiecs.be
""")
if mibBuilder.loadTexts:
    carel.setDescription("""\
Custom MIB for Rittal LCP 3311 chillers connected to a pco web card
""")


# Types definitions


# TEXTUAL-CONVENTIONS



class DivBy10(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"
    if mibBuilder.loadTexts:
        description = """\
Fixed point, one decimal
"""


# MIB Managed Objects in the order of their OIDs

_Rittal_ObjectIdentity = ObjectIdentity
rittal = _Rittal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2606)
)
_RittalLCP3311_ObjectIdentity = ObjectIdentity
rittalLCP3311 = _RittalLCP3311_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2)
)
_Sensors_ObjectIdentity = ObjectIdentity
sensors = _Sensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1)
)
_Digital_ObjectIdentity = ObjectIdentity
digital = _Digital_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 1)
)


class _CompressorOverloadAlarm_Type(Integer32):
    """Custom type compressorOverloadAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("ok", 0))
    )


_CompressorOverloadAlarm_Type.__name__ = "Integer32"
_CompressorOverloadAlarm_Object = MibScalar
compressorOverloadAlarm = _CompressorOverloadAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 1, 2),
    _CompressorOverloadAlarm_Type()
)
compressorOverloadAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compressorOverloadAlarm.setStatus("current")
if mibBuilder.loadTexts:
    compressorOverloadAlarm.setDescription("""\
Compressor overload alarm ok (0), alarm (1)
""")


class _HighPressureAlarm_Type(Integer32):
    """Custom type highPressureAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("ok", 0))
    )


_HighPressureAlarm_Type.__name__ = "Integer32"
_HighPressureAlarm_Object = MibScalar
highPressureAlarm = _HighPressureAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 1, 3),
    _HighPressureAlarm_Type()
)
highPressureAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    highPressureAlarm.setStatus("current")
if mibBuilder.loadTexts:
    highPressureAlarm.setDescription("""\
High pressure alarm ok (0), alarm (1)
""")


class _RemoteOnOff_Type(Integer32):
    """Custom type remoteOnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_RemoteOnOff_Type.__name__ = "Integer32"
_RemoteOnOff_Object = MibScalar
remoteOnOff = _RemoteOnOff_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 1, 8),
    _RemoteOnOff_Type()
)
remoteOnOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteOnOff.setStatus("current")
if mibBuilder.loadTexts:
    remoteOnOff.setDescription("""\
Remote On/Off off (0), on (1)
""")


class _InverterAlarm_Type(Integer32):
    """Custom type inverterAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("ok", 0))
    )


_InverterAlarm_Type.__name__ = "Integer32"
_InverterAlarm_Object = MibScalar
inverterAlarm = _InverterAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 1, 11),
    _InverterAlarm_Type()
)
inverterAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterAlarm.setStatus("current")
if mibBuilder.loadTexts:
    inverterAlarm.setDescription("""\
Inverter alarm ok (0), alarm (1)
""")


class _DriveAlarm_Type(Integer32):
    """Custom type driveAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("ok", 0))
    )


_DriveAlarm_Type.__name__ = "Integer32"
_DriveAlarm_Object = MibScalar
driveAlarm = _DriveAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 1, 12),
    _DriveAlarm_Type()
)
driveAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveAlarm.setStatus("current")
if mibBuilder.loadTexts:
    driveAlarm.setDescription("""\
Power+ drive off-line alarm ok (0), alarm (1)
""")


class _InverterOnOff_Type(Integer32):
    """Custom type inverterOnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_InverterOnOff_Type.__name__ = "Integer32"
_InverterOnOff_Object = MibScalar
inverterOnOff = _InverterOnOff_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 1, 17),
    _InverterOnOff_Type()
)
inverterOnOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterOnOff.setStatus("current")
if mibBuilder.loadTexts:
    inverterOnOff.setDescription("""\
Inverter On/Off off (0), on (1)
""")


class _GeneralAlarm_Type(Integer32):
    """Custom type generalAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("ok", 0))
    )


_GeneralAlarm_Type.__name__ = "Integer32"
_GeneralAlarm_Object = MibScalar
generalAlarm = _GeneralAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 1, 23),
    _GeneralAlarm_Type()
)
generalAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generalAlarm.setStatus("current")
if mibBuilder.loadTexts:
    generalAlarm.setDescription("""\
General alarm ok (0), alarm (1)
""")


class _ResetAllAlarms_Type(Integer32):
    """Custom type resetAllAlarms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_ResetAllAlarms_Type.__name__ = "Integer32"
_ResetAllAlarms_Object = MibScalar
resetAllAlarms = _ResetAllAlarms_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 1, 29),
    _ResetAllAlarms_Type()
)
resetAllAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetAllAlarms.setStatus("current")
if mibBuilder.loadTexts:
    resetAllAlarms.setDescription("""\
Reset all alarms no (0), yes (1)
""")


class _CompressorEnvelopeAlarm_Type(Integer32):
    """Custom type compressorEnvelopeAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("ok", 0))
    )


_CompressorEnvelopeAlarm_Type.__name__ = "Integer32"
_CompressorEnvelopeAlarm_Object = MibScalar
compressorEnvelopeAlarm = _CompressorEnvelopeAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 1, 30),
    _CompressorEnvelopeAlarm_Type()
)
compressorEnvelopeAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compressorEnvelopeAlarm.setStatus("current")
if mibBuilder.loadTexts:
    compressorEnvelopeAlarm.setDescription("""\
Compressor forced off working out envelope ok (0), alarm (1)
""")


class _CompressorStartupFailureAlarm_Type(Integer32):
    """Custom type compressorStartupFailureAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("ok", 0))
    )


_CompressorStartupFailureAlarm_Type.__name__ = "Integer32"
_CompressorStartupFailureAlarm_Object = MibScalar
compressorStartupFailureAlarm = _CompressorStartupFailureAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 1, 31),
    _CompressorStartupFailureAlarm_Type()
)
compressorStartupFailureAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compressorStartupFailureAlarm.setStatus("current")
if mibBuilder.loadTexts:
    compressorStartupFailureAlarm.setDescription("""\
Compressor startup failure alarm, reached max retries ok (0), alarm (1)
""")


class _MaxDischargeTemperatureAlarm_Type(Integer32):
    """Custom type maxDischargeTemperatureAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("ok", 0))
    )


_MaxDischargeTemperatureAlarm_Type.__name__ = "Integer32"
_MaxDischargeTemperatureAlarm_Object = MibScalar
maxDischargeTemperatureAlarm = _MaxDischargeTemperatureAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 1, 33),
    _MaxDischargeTemperatureAlarm_Type()
)
maxDischargeTemperatureAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxDischargeTemperatureAlarm.setStatus("current")
if mibBuilder.loadTexts:
    maxDischargeTemperatureAlarm.setDescription("""\
Maximum discharge temperature has been reached ok (0), alarm (1)
""")


class _CompressorDeltaPressureAlarm_Type(Integer32):
    """Custom type compressorDeltaPressureAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("ok", 0))
    )


_CompressorDeltaPressureAlarm_Type.__name__ = "Integer32"
_CompressorDeltaPressureAlarm_Object = MibScalar
compressorDeltaPressureAlarm = _CompressorDeltaPressureAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 1, 35),
    _CompressorDeltaPressureAlarm_Type()
)
compressorDeltaPressureAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compressorDeltaPressureAlarm.setStatus("current")
if mibBuilder.loadTexts:
    compressorDeltaPressureAlarm.setDescription("""\
Delta pressure too big to startup compressor ok (0), alarm (1)
""")


class _OilReturnAlarm_Type(Integer32):
    """Custom type oilReturnAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("ok", 0))
    )


_OilReturnAlarm_Type.__name__ = "Integer32"
_OilReturnAlarm_Object = MibScalar
oilReturnAlarm = _OilReturnAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 1, 36),
    _OilReturnAlarm_Type()
)
oilReturnAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oilReturnAlarm.setStatus("current")
if mibBuilder.loadTexts:
    oilReturnAlarm.setDescription("""\
Oil return alarm for when the compressor is running. Lubrication issue. ok (0),
alarm (1)
""")


class _OutputTemperatureTopProbeAlarm_Type(Integer32):
    """Custom type outputTemperatureTopProbeAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("ok", 0))
    )


_OutputTemperatureTopProbeAlarm_Type.__name__ = "Integer32"
_OutputTemperatureTopProbeAlarm_Object = MibScalar
outputTemperatureTopProbeAlarm = _OutputTemperatureTopProbeAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 1, 38),
    _OutputTemperatureTopProbeAlarm_Type()
)
outputTemperatureTopProbeAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputTemperatureTopProbeAlarm.setStatus("current")
if mibBuilder.loadTexts:
    outputTemperatureTopProbeAlarm.setDescription("""\
Top output temperature probe broken ok (0), alarm (1)
""")


class _OutputTemperatureMidProbeAlarm_Type(Integer32):
    """Custom type outputTemperatureMidProbeAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("ok", 0))
    )


_OutputTemperatureMidProbeAlarm_Type.__name__ = "Integer32"
_OutputTemperatureMidProbeAlarm_Object = MibScalar
outputTemperatureMidProbeAlarm = _OutputTemperatureMidProbeAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 1, 39),
    _OutputTemperatureMidProbeAlarm_Type()
)
outputTemperatureMidProbeAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputTemperatureMidProbeAlarm.setStatus("current")
if mibBuilder.loadTexts:
    outputTemperatureMidProbeAlarm.setDescription("""\
Mid output temperature probe broken ok (0), alarm (1)
""")


class _OutputTemperatureBottomProbeAlarm_Type(Integer32):
    """Custom type outputTemperatureBottomProbeAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("ok", 0))
    )


_OutputTemperatureBottomProbeAlarm_Type.__name__ = "Integer32"
_OutputTemperatureBottomProbeAlarm_Object = MibScalar
outputTemperatureBottomProbeAlarm = _OutputTemperatureBottomProbeAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 1, 40),
    _OutputTemperatureBottomProbeAlarm_Type()
)
outputTemperatureBottomProbeAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputTemperatureBottomProbeAlarm.setStatus("current")
if mibBuilder.loadTexts:
    outputTemperatureBottomProbeAlarm.setDescription("""\
Bottom output temperature probe broken ok (0), alarm (1)
""")


class _InputTemperatureTopProbeAlarm_Type(Integer32):
    """Custom type inputTemperatureTopProbeAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("ok", 0))
    )


_InputTemperatureTopProbeAlarm_Type.__name__ = "Integer32"
_InputTemperatureTopProbeAlarm_Object = MibScalar
inputTemperatureTopProbeAlarm = _InputTemperatureTopProbeAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 1, 42),
    _InputTemperatureTopProbeAlarm_Type()
)
inputTemperatureTopProbeAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputTemperatureTopProbeAlarm.setStatus("current")
if mibBuilder.loadTexts:
    inputTemperatureTopProbeAlarm.setDescription("""\
Top input temperature probe broken ok (0), alarm (1)
""")


class _InputTemperatureMidProbeAlarm_Type(Integer32):
    """Custom type inputTemperatureMidProbeAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("ok", 0))
    )


_InputTemperatureMidProbeAlarm_Type.__name__ = "Integer32"
_InputTemperatureMidProbeAlarm_Object = MibScalar
inputTemperatureMidProbeAlarm = _InputTemperatureMidProbeAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 1, 43),
    _InputTemperatureMidProbeAlarm_Type()
)
inputTemperatureMidProbeAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputTemperatureMidProbeAlarm.setStatus("current")
if mibBuilder.loadTexts:
    inputTemperatureMidProbeAlarm.setDescription("""\
Mid input temperature probe broken ok (0), alarm (1)
""")


class _InputTemperatureBottomProbeAlarm_Type(Integer32):
    """Custom type inputTemperatureBottomProbeAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("ok", 0))
    )


_InputTemperatureBottomProbeAlarm_Type.__name__ = "Integer32"
_InputTemperatureBottomProbeAlarm_Object = MibScalar
inputTemperatureBottomProbeAlarm = _InputTemperatureBottomProbeAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 1, 44),
    _InputTemperatureBottomProbeAlarm_Type()
)
inputTemperatureBottomProbeAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputTemperatureBottomProbeAlarm.setStatus("current")
if mibBuilder.loadTexts:
    inputTemperatureBottomProbeAlarm.setDescription("""\
Bottom input temperature probe broken ok (0), alarm (1)
""")


class _CompressorDischargeTemperatureProbeAlarm_Type(Integer32):
    """Custom type compressorDischargeTemperatureProbeAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("ok", 0))
    )


_CompressorDischargeTemperatureProbeAlarm_Type.__name__ = "Integer32"
_CompressorDischargeTemperatureProbeAlarm_Object = MibScalar
compressorDischargeTemperatureProbeAlarm = _CompressorDischargeTemperatureProbeAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 1, 45),
    _CompressorDischargeTemperatureProbeAlarm_Type()
)
compressorDischargeTemperatureProbeAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compressorDischargeTemperatureProbeAlarm.setStatus("current")
if mibBuilder.loadTexts:
    compressorDischargeTemperatureProbeAlarm.setDescription("""\
Compressor discharge temperature probe broken ok (0), alarm (1)
""")


class _CompressorSuctionTemperatureProbeAlarm_Type(Integer32):
    """Custom type compressorSuctionTemperatureProbeAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("ok", 0))
    )


_CompressorSuctionTemperatureProbeAlarm_Type.__name__ = "Integer32"
_CompressorSuctionTemperatureProbeAlarm_Object = MibScalar
compressorSuctionTemperatureProbeAlarm = _CompressorSuctionTemperatureProbeAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 1, 46),
    _CompressorSuctionTemperatureProbeAlarm_Type()
)
compressorSuctionTemperatureProbeAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compressorSuctionTemperatureProbeAlarm.setStatus("current")
if mibBuilder.loadTexts:
    compressorSuctionTemperatureProbeAlarm.setDescription("""\
Compressor suction temperature probe broken ok (0), alarm (1)
""")


class _CompressorDischargePressureProbeAlarm_Type(Integer32):
    """Custom type compressorDischargePressureProbeAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("ok", 0))
    )


_CompressorDischargePressureProbeAlarm_Type.__name__ = "Integer32"
_CompressorDischargePressureProbeAlarm_Object = MibScalar
compressorDischargePressureProbeAlarm = _CompressorDischargePressureProbeAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 1, 47),
    _CompressorDischargePressureProbeAlarm_Type()
)
compressorDischargePressureProbeAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compressorDischargePressureProbeAlarm.setStatus("current")
if mibBuilder.loadTexts:
    compressorDischargePressureProbeAlarm.setDescription("""\
Compressor discharge pressure probe broken ok (0), alarm (1)
""")


class _CompressorSuctionPressureProbeAlarm_Type(Integer32):
    """Custom type compressorSuctionPressureProbeAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("ok", 0))
    )


_CompressorSuctionPressureProbeAlarm_Type.__name__ = "Integer32"
_CompressorSuctionPressureProbeAlarm_Object = MibScalar
compressorSuctionPressureProbeAlarm = _CompressorSuctionPressureProbeAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 1, 48),
    _CompressorSuctionPressureProbeAlarm_Type()
)
compressorSuctionPressureProbeAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compressorSuctionPressureProbeAlarm.setStatus("current")
if mibBuilder.loadTexts:
    compressorSuctionPressureProbeAlarm.setDescription("""\
Compressor suction pressure probe broken ok (0), alarm (1)
""")


class _Reboot_Type(Integer32):
    """Custom type reboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Reboot_Type.__name__ = "Integer32"
_Reboot_Object = MibScalar
reboot = _Reboot_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 1, 100),
    _Reboot_Type()
)
reboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reboot.setStatus("current")
if mibBuilder.loadTexts:
    reboot.setDescription("""\
Reboot the system no (0), yes (1)
""")
_Analog_ObjectIdentity = ObjectIdentity
analog = _Analog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 2)
)
_OutputTemperatureTopSensor_Type = DivBy10
_OutputTemperatureTopSensor_Object = MibScalar
outputTemperatureTopSensor = _OutputTemperatureTopSensor_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 2, 2),
    _OutputTemperatureTopSensor_Type()
)
outputTemperatureTopSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputTemperatureTopSensor.setStatus("current")
if mibBuilder.loadTexts:
    outputTemperatureTopSensor.setUnits("C")
if mibBuilder.loadTexts:
    outputTemperatureTopSensor.setDescription("""\
Top sensor output temperature in Celcius
""")
_OutputTemperatureMidSensor_Type = DivBy10
_OutputTemperatureMidSensor_Object = MibScalar
outputTemperatureMidSensor = _OutputTemperatureMidSensor_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 2, 3),
    _OutputTemperatureMidSensor_Type()
)
outputTemperatureMidSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputTemperatureMidSensor.setStatus("current")
if mibBuilder.loadTexts:
    outputTemperatureMidSensor.setUnits("C")
if mibBuilder.loadTexts:
    outputTemperatureMidSensor.setDescription("""\
Mid sensor output temperature in Celcius
""")
_OutputTemperatureBottomSensor_Type = DivBy10
_OutputTemperatureBottomSensor_Object = MibScalar
outputTemperatureBottomSensor = _OutputTemperatureBottomSensor_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 2, 4),
    _OutputTemperatureBottomSensor_Type()
)
outputTemperatureBottomSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputTemperatureBottomSensor.setStatus("current")
if mibBuilder.loadTexts:
    outputTemperatureBottomSensor.setUnits("C")
if mibBuilder.loadTexts:
    outputTemperatureBottomSensor.setDescription("""\
Bottom sensor output temperature in Celcius
""")
_InputTemperatureTopSensor_Type = DivBy10
_InputTemperatureTopSensor_Object = MibScalar
inputTemperatureTopSensor = _InputTemperatureTopSensor_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 2, 6),
    _InputTemperatureTopSensor_Type()
)
inputTemperatureTopSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputTemperatureTopSensor.setStatus("current")
if mibBuilder.loadTexts:
    inputTemperatureTopSensor.setUnits("C")
if mibBuilder.loadTexts:
    inputTemperatureTopSensor.setDescription("""\
Top sensor input temperature in Celcius
""")
_InputTemperatureMidSensor_Type = DivBy10
_InputTemperatureMidSensor_Object = MibScalar
inputTemperatureMidSensor = _InputTemperatureMidSensor_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 2, 7),
    _InputTemperatureMidSensor_Type()
)
inputTemperatureMidSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputTemperatureMidSensor.setStatus("current")
if mibBuilder.loadTexts:
    inputTemperatureMidSensor.setUnits("C")
if mibBuilder.loadTexts:
    inputTemperatureMidSensor.setDescription("""\
Mid sensor input temperature in Celcius
""")
_InputTemperatureBottomSensor_Type = DivBy10
_InputTemperatureBottomSensor_Object = MibScalar
inputTemperatureBottomSensor = _InputTemperatureBottomSensor_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 2, 8),
    _InputTemperatureBottomSensor_Type()
)
inputTemperatureBottomSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputTemperatureBottomSensor.setStatus("current")
if mibBuilder.loadTexts:
    inputTemperatureBottomSensor.setUnits("C")
if mibBuilder.loadTexts:
    inputTemperatureBottomSensor.setDescription("""\
Bottom sensor input temperature in Celcius
""")
_CompressorDischargeTemperature_Type = DivBy10
_CompressorDischargeTemperature_Object = MibScalar
compressorDischargeTemperature = _CompressorDischargeTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 2, 9),
    _CompressorDischargeTemperature_Type()
)
compressorDischargeTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compressorDischargeTemperature.setStatus("current")
if mibBuilder.loadTexts:
    compressorDischargeTemperature.setUnits("C")
if mibBuilder.loadTexts:
    compressorDischargeTemperature.setDescription("""\
Compressor discharge temperature
""")
_CompressorSuctionTemperature_Type = DivBy10
_CompressorSuctionTemperature_Object = MibScalar
compressorSuctionTemperature = _CompressorSuctionTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 2, 10),
    _CompressorSuctionTemperature_Type()
)
compressorSuctionTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compressorSuctionTemperature.setStatus("current")
if mibBuilder.loadTexts:
    compressorSuctionTemperature.setUnits("C")
if mibBuilder.loadTexts:
    compressorSuctionTemperature.setDescription("""\
Compressor suction temperature
""")
_CompressorDischargePressure_Type = DivBy10
_CompressorDischargePressure_Object = MibScalar
compressorDischargePressure = _CompressorDischargePressure_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 2, 11),
    _CompressorDischargePressure_Type()
)
compressorDischargePressure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compressorDischargePressure.setStatus("current")
if mibBuilder.loadTexts:
    compressorDischargePressure.setUnits("bar")
if mibBuilder.loadTexts:
    compressorDischargePressure.setDescription("""\
Compressor discharge pressure
""")
_CompressorSuctionPressure_Type = DivBy10
_CompressorSuctionPressure_Object = MibScalar
compressorSuctionPressure = _CompressorSuctionPressure_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 2, 12),
    _CompressorSuctionPressure_Type()
)
compressorSuctionPressure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compressorSuctionPressure.setStatus("current")
if mibBuilder.loadTexts:
    compressorSuctionPressure.setUnits("bar")
if mibBuilder.loadTexts:
    compressorSuctionPressure.setDescription("""\
Compressor suction pressure
""")
_EvaporatorTemperature_Type = DivBy10
_EvaporatorTemperature_Object = MibScalar
evaporatorTemperature = _EvaporatorTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 2, 13),
    _EvaporatorTemperature_Type()
)
evaporatorTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evaporatorTemperature.setStatus("current")
if mibBuilder.loadTexts:
    evaporatorTemperature.setUnits("C")
if mibBuilder.loadTexts:
    evaporatorTemperature.setDescription("""\
Evaporator temperature from Low pressure conversion
""")
_CondensingTemperature_Type = DivBy10
_CondensingTemperature_Object = MibScalar
condensingTemperature = _CondensingTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 2, 14),
    _CondensingTemperature_Type()
)
condensingTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    condensingTemperature.setStatus("current")
if mibBuilder.loadTexts:
    condensingTemperature.setUnits("C")
if mibBuilder.loadTexts:
    condensingTemperature.setDescription("""\
Condensing temperature from High pressure conversion
""")
_InputTemperatureAverage_Type = DivBy10
_InputTemperatureAverage_Object = MibScalar
inputTemperatureAverage = _InputTemperatureAverage_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 2, 21),
    _InputTemperatureAverage_Type()
)
inputTemperatureAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputTemperatureAverage.setStatus("current")
if mibBuilder.loadTexts:
    inputTemperatureAverage.setUnits("C")
if mibBuilder.loadTexts:
    inputTemperatureAverage.setDescription("""\
Average input temperature in Celcius
""")
_OutputTemperatureAverage_Type = DivBy10
_OutputTemperatureAverage_Object = MibScalar
outputTemperatureAverage = _OutputTemperatureAverage_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 2, 22),
    _OutputTemperatureAverage_Type()
)
outputTemperatureAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputTemperatureAverage.setStatus("current")
if mibBuilder.loadTexts:
    outputTemperatureAverage.setUnits("C")
if mibBuilder.loadTexts:
    outputTemperatureAverage.setDescription("""\
Average output temperature in Celcius
""")
_CompressorRotorSpeed_Type = DivBy10
_CompressorRotorSpeed_Object = MibScalar
compressorRotorSpeed = _CompressorRotorSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 2, 45),
    _CompressorRotorSpeed_Type()
)
compressorRotorSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compressorRotorSpeed.setStatus("current")
if mibBuilder.loadTexts:
    compressorRotorSpeed.setUnits("rps")
if mibBuilder.loadTexts:
    compressorRotorSpeed.setDescription("""\
Compressor rotor speed
""")
_CompressorMotorCurrent_Type = DivBy10
_CompressorMotorCurrent_Object = MibScalar
compressorMotorCurrent = _CompressorMotorCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 2, 46),
    _CompressorMotorCurrent_Type()
)
compressorMotorCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compressorMotorCurrent.setStatus("current")
if mibBuilder.loadTexts:
    compressorMotorCurrent.setUnits("A")
if mibBuilder.loadTexts:
    compressorMotorCurrent.setDescription("""\
Compressor motor current
""")
_LcpSetpoint_Type = DivBy10
_LcpSetpoint_Object = MibScalar
lcpSetpoint = _LcpSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 2, 48),
    _LcpSetpoint_Type()
)
lcpSetpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcpSetpoint.setStatus("current")
if mibBuilder.loadTexts:
    lcpSetpoint.setUnits("C")
if mibBuilder.loadTexts:
    lcpSetpoint.setDescription("""\
Main LCP setpoint
""")
_Integer_ObjectIdentity = ObjectIdentity
integer = _Integer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 3)
)


class _CompressorRotorSpeedHz_Type(Integer32):
    """Custom type compressorRotorSpeedHz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_CompressorRotorSpeedHz_Type.__name__ = "Integer32"
_CompressorRotorSpeedHz_Object = MibScalar
compressorRotorSpeedHz = _CompressorRotorSpeedHz_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 3, 1),
    _CompressorRotorSpeedHz_Type()
)
compressorRotorSpeedHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compressorRotorSpeedHz.setStatus("current")
if mibBuilder.loadTexts:
    compressorRotorSpeedHz.setUnits("Hz")
if mibBuilder.loadTexts:
    compressorRotorSpeedHz.setDescription("""\
Compressor rotor speed in Hz
""")


class _DriverPowerStatus_Type(Integer32):
    """Custom type driverPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 3),
          ("run", 2),
          ("stop", 1))
    )


_DriverPowerStatus_Type.__name__ = "Integer32"
_DriverPowerStatus_Object = MibScalar
driverPowerStatus = _DriverPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 3, 2),
    _DriverPowerStatus_Type()
)
driverPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driverPowerStatus.setStatus("current")
if mibBuilder.loadTexts:
    driverPowerStatus.setDescription("""\
Driver power status stop (1), run (2), alarm (3)
""")


class _CurrentErrorCode_Type(Integer32):
    """Custom type currentErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
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
              33)
        )
    )
    namedValues = NamedValues(
        *(("ALA02", 2),
          ("ALA03", 3),
          ("ALA04", 4),
          ("ALA05", 5),
          ("ALA06", 6),
          ("ALA07", 7),
          ("ALA08", 8),
          ("ALA09", 9),
          ("ALA10", 10),
          ("ALA11", 11),
          ("ALA12", 12),
          ("ALB01", 13),
          ("ALB02", 14),
          ("ALB03", 15),
          ("ALC01", 16),
          ("ALC03", 17),
          ("ALC04", 18),
          ("ALC05", 19),
          ("ALC06", 20),
          ("ALD02", 22),
          ("ALD03", 23),
          ("ALD04", 24),
          ("ALD05", 25),
          ("ALD06", 26),
          ("ALD07", 27),
          ("ALD08", 28),
          ("ALD09", 29),
          ("ALF01", 21),
          ("ALL01", 30),
          ("ALL02", 31),
          ("ALL99", 32),
          ("ALW04", 33),
          ("OK", 0))
    )


_CurrentErrorCode_Type.__name__ = "Integer32"
_CurrentErrorCode_Object = MibScalar
currentErrorCode = _CurrentErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 3, 3),
    _CurrentErrorCode_Type()
)
currentErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentErrorCode.setStatus("current")
if mibBuilder.loadTexts:
    currentErrorCode.setDescription("""\
Current error code
""")
_DriverTemperature_Type = DivBy10
_DriverTemperature_Object = MibScalar
driverTemperature = _DriverTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 3, 4),
    _DriverTemperature_Type()
)
driverTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driverTemperature.setStatus("current")
if mibBuilder.loadTexts:
    driverTemperature.setUnits("C")
if mibBuilder.loadTexts:
    driverTemperature.setDescription("""\
Driver Power+ Temperature
""")
_DcBusVoltage_Type = DivBy10
_DcBusVoltage_Object = MibScalar
dcBusVoltage = _DcBusVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 3, 5),
    _DcBusVoltage_Type()
)
dcBusVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBusVoltage.setStatus("current")
if mibBuilder.loadTexts:
    dcBusVoltage.setUnits("V")
if mibBuilder.loadTexts:
    dcBusVoltage.setDescription("""\
Power+ DC Voltage
""")
_MotorVoltage_Type = DivBy10
_MotorVoltage_Object = MibScalar
motorVoltage = _MotorVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 3, 6),
    _MotorVoltage_Type()
)
motorVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motorVoltage.setStatus("current")
if mibBuilder.loadTexts:
    motorVoltage.setUnits("V")
if mibBuilder.loadTexts:
    motorVoltage.setDescription("""\
Motor Voltage
""")
_PowerRequest_Type = DivBy10
_PowerRequest_Object = MibScalar
powerRequest = _PowerRequest_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 3, 7),
    _PowerRequest_Type()
)
powerRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerRequest.setStatus("current")
if mibBuilder.loadTexts:
    powerRequest.setUnits("%")
if mibBuilder.loadTexts:
    powerRequest.setDescription("""\
Request of power for inverter after envelop
""")


class _UnitOnOff_Type(Integer32):
    """Custom type unitOnOff based on Integer32"""
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
        *(("auto", 3),
          ("energy-save", 2),
          ("off", 0),
          ("on", 1))
    )


_UnitOnOff_Type.__name__ = "Integer32"
_UnitOnOff_Object = MibScalar
unitOnOff = _UnitOnOff_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 3, 13),
    _UnitOnOff_Type()
)
unitOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitOnOff.setStatus("current")
if mibBuilder.loadTexts:
    unitOnOff.setDescription("""\
Unit on/off state off (0), on (1), energy-save (2), auto (3)
""")


class _EnvelopeZone_Type(Integer32):
    """Custom type envelopeZone based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("current-limit", 3),
          ("maximum-compression-ratio", 1),
          ("maximum-discharge-power", 2),
          ("maximum-suction-power", 4),
          ("minimum-compression-ratio", 5),
          ("minimum-delta-power", 6),
          ("minimum-discharge-power", 7),
          ("minimum-suction-power", 8),
          ("ok", 0))
    )


_EnvelopeZone_Type.__name__ = "Integer32"
_EnvelopeZone_Object = MibScalar
envelopeZone = _EnvelopeZone_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 3, 14),
    _EnvelopeZone_Type()
)
envelopeZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envelopeZone.setStatus("current")
if mibBuilder.loadTexts:
    envelopeZone.setDescription("""\
envelope zone ok (0), maximum compression ratio (1), maximum discharge power
(2), current limit (3), maximum suction power(4), minimum compression ratio
(5), minimum delta power (6), minimum discharge power(7), minimum suction power
(8)
""")


class _CoolingCapacity_Type(Integer32):
    """Custom type coolingCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CoolingCapacity_Type.__name__ = "Integer32"
_CoolingCapacity_Object = MibScalar
coolingCapacity = _CoolingCapacity_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 3, 16),
    _CoolingCapacity_Type()
)
coolingCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingCapacity.setStatus("current")
if mibBuilder.loadTexts:
    coolingCapacity.setUnits("%")
if mibBuilder.loadTexts:
    coolingCapacity.setDescription("""\
Actual EVD valve cooling capacity
""")


class _EvdValveSteps_Type(Integer32):
    """Custom type evdValveSteps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 540),
    )


_EvdValveSteps_Type.__name__ = "Integer32"
_EvdValveSteps_Object = MibScalar
evdValveSteps = _EvdValveSteps_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 3, 17),
    _EvdValveSteps_Type()
)
evdValveSteps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evdValveSteps.setStatus("current")
if mibBuilder.loadTexts:
    evdValveSteps.setUnits("steps")
if mibBuilder.loadTexts:
    evdValveSteps.setDescription("""\
EVD valve steps position
""")


class _FanSpeedPercent_Type(Integer32):
    """Custom type fanSpeedPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FanSpeedPercent_Type.__name__ = "Integer32"
_FanSpeedPercent_Object = MibScalar
fanSpeedPercent = _FanSpeedPercent_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 3, 28),
    _FanSpeedPercent_Type()
)
fanSpeedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanSpeedPercent.setStatus("current")
if mibBuilder.loadTexts:
    fanSpeedPercent.setUnits("%")
if mibBuilder.loadTexts:
    fanSpeedPercent.setDescription("""\
The fan speed percentage
""")


class _FanSpeedRpm_Type(Integer32):
    """Custom type fanSpeedRpm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3700),
    )


_FanSpeedRpm_Type.__name__ = "Integer32"
_FanSpeedRpm_Object = MibScalar
fanSpeedRpm = _FanSpeedRpm_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 3, 29),
    _FanSpeedRpm_Type()
)
fanSpeedRpm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanSpeedRpm.setStatus("current")
if mibBuilder.loadTexts:
    fanSpeedRpm.setUnits("rpm")
if mibBuilder.loadTexts:
    fanSpeedRpm.setDescription("""\
The fan speed rpm
""")


class _EvdValveOpening_Type(Integer32):
    """Custom type evdValveOpening based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_EvdValveOpening_Type.__name__ = "Integer32"
_EvdValveOpening_Object = MibScalar
evdValveOpening = _EvdValveOpening_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2606, 2, 1, 3, 30),
    _EvdValveOpening_Type()
)
evdValveOpening.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evdValveOpening.setStatus("current")
if mibBuilder.loadTexts:
    evdValveOpening.setUnits("%")
if mibBuilder.loadTexts:
    evdValveOpening.setDescription("""\
Actual EVD valve opening
""")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CAREL-RITTAL-LCP-3311-MIB",
    **{"DivBy10": DivBy10,
       "carel": carel,
       "rittal": rittal,
       "rittalLCP3311": rittalLCP3311,
       "sensors": sensors,
       "digital": digital,
       "compressorOverloadAlarm": compressorOverloadAlarm,
       "highPressureAlarm": highPressureAlarm,
       "remoteOnOff": remoteOnOff,
       "inverterAlarm": inverterAlarm,
       "driveAlarm": driveAlarm,
       "inverterOnOff": inverterOnOff,
       "generalAlarm": generalAlarm,
       "resetAllAlarms": resetAllAlarms,
       "compressorEnvelopeAlarm": compressorEnvelopeAlarm,
       "compressorStartupFailureAlarm": compressorStartupFailureAlarm,
       "maxDischargeTemperatureAlarm": maxDischargeTemperatureAlarm,
       "compressorDeltaPressureAlarm": compressorDeltaPressureAlarm,
       "oilReturnAlarm": oilReturnAlarm,
       "outputTemperatureTopProbeAlarm": outputTemperatureTopProbeAlarm,
       "outputTemperatureMidProbeAlarm": outputTemperatureMidProbeAlarm,
       "outputTemperatureBottomProbeAlarm": outputTemperatureBottomProbeAlarm,
       "inputTemperatureTopProbeAlarm": inputTemperatureTopProbeAlarm,
       "inputTemperatureMidProbeAlarm": inputTemperatureMidProbeAlarm,
       "inputTemperatureBottomProbeAlarm": inputTemperatureBottomProbeAlarm,
       "compressorDischargeTemperatureProbeAlarm": compressorDischargeTemperatureProbeAlarm,
       "compressorSuctionTemperatureProbeAlarm": compressorSuctionTemperatureProbeAlarm,
       "compressorDischargePressureProbeAlarm": compressorDischargePressureProbeAlarm,
       "compressorSuctionPressureProbeAlarm": compressorSuctionPressureProbeAlarm,
       "reboot": reboot,
       "analog": analog,
       "outputTemperatureTopSensor": outputTemperatureTopSensor,
       "outputTemperatureMidSensor": outputTemperatureMidSensor,
       "outputTemperatureBottomSensor": outputTemperatureBottomSensor,
       "inputTemperatureTopSensor": inputTemperatureTopSensor,
       "inputTemperatureMidSensor": inputTemperatureMidSensor,
       "inputTemperatureBottomSensor": inputTemperatureBottomSensor,
       "compressorDischargeTemperature": compressorDischargeTemperature,
       "compressorSuctionTemperature": compressorSuctionTemperature,
       "compressorDischargePressure": compressorDischargePressure,
       "compressorSuctionPressure": compressorSuctionPressure,
       "evaporatorTemperature": evaporatorTemperature,
       "condensingTemperature": condensingTemperature,
       "inputTemperatureAverage": inputTemperatureAverage,
       "outputTemperatureAverage": outputTemperatureAverage,
       "compressorRotorSpeed": compressorRotorSpeed,
       "compressorMotorCurrent": compressorMotorCurrent,
       "lcpSetpoint": lcpSetpoint,
       "integer": integer,
       "compressorRotorSpeedHz": compressorRotorSpeedHz,
       "driverPowerStatus": driverPowerStatus,
       "currentErrorCode": currentErrorCode,
       "driverTemperature": driverTemperature,
       "dcBusVoltage": dcBusVoltage,
       "motorVoltage": motorVoltage,
       "powerRequest": powerRequest,
       "unitOnOff": unitOnOff,
       "envelopeZone": envelopeZone,
       "coolingCapacity": coolingCapacity,
       "evdValveSteps": evdValveSteps,
       "fanSpeedPercent": fanSpeedPercent,
       "fanSpeedRpm": fanSpeedRpm,
       "evdValveOpening": evdValveOpening}
)
