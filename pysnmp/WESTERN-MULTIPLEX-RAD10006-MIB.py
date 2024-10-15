# SNMP MIB module (WESTERN-MULTIPLEX-RAD10006-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WESTERN-MULTIPLEX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:46 2024
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(trapSequenceNumber,) = mibBuilder.importSymbols(
    "WESTERN-MULTIPLEX-MIB",
    "trapSequenceNumber")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Western_multiplex_ObjectIdentity = ObjectIdentity
western_multiplex = _Western_multiplex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3727)
)
_Tsunami100_06_ObjectIdentity = ObjectIdentity
tsunami100_06 = _Tsunami100_06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3727, 20)
)
_Radio_ObjectIdentity = ObjectIdentity
radio = _Radio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20)
)
_Config_ObjectIdentity = ObjectIdentity
config = _Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 1)
)


class _CnfgT1LineCode_Type(Integer32):
    """Custom type cnfgT1LineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ami", 2),
          ("b8zs", 1))
    )


_CnfgT1LineCode_Type.__name__ = "Integer32"
_CnfgT1LineCode_Object = MibScalar
cnfgT1LineCode = _CnfgT1LineCode_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 1, 1),
    _CnfgT1LineCode_Type()
)
cnfgT1LineCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfgT1LineCode.setStatus("mandatory")


class _CnfgT1LineBuildOut_Type(Integer32):
    """Custom type cnfgT1LineBuildOut based on Integer32"""
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
        *(("lb-0-133-ft", 1),
          ("lb-133-266-ft", 2),
          ("lb-266-399-ft", 3),
          ("lb-399-533-ft", 4),
          ("lb-533-655-ft", 5))
    )


_CnfgT1LineBuildOut_Type.__name__ = "Integer32"
_CnfgT1LineBuildOut_Object = MibScalar
cnfgT1LineBuildOut = _CnfgT1LineBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 1, 2),
    _CnfgT1LineBuildOut_Type()
)
cnfgT1LineBuildOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfgT1LineBuildOut.setStatus("mandatory")


class _CnfgT1NearEndRadioLoopback_Type(Integer32):
    """Custom type cnfgT1NearEndRadioLoopback based on Integer32"""
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


_CnfgT1NearEndRadioLoopback_Type.__name__ = "Integer32"
_CnfgT1NearEndRadioLoopback_Object = MibScalar
cnfgT1NearEndRadioLoopback = _CnfgT1NearEndRadioLoopback_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 1, 3),
    _CnfgT1NearEndRadioLoopback_Type()
)
cnfgT1NearEndRadioLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfgT1NearEndRadioLoopback.setStatus("mandatory")


class _CnfgT1FarEndRadioLoopback_Type(Integer32):
    """Custom type cnfgT1FarEndRadioLoopback based on Integer32"""
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


_CnfgT1FarEndRadioLoopback_Type.__name__ = "Integer32"
_CnfgT1FarEndRadioLoopback_Object = MibScalar
cnfgT1FarEndRadioLoopback = _CnfgT1FarEndRadioLoopback_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 1, 4),
    _CnfgT1FarEndRadioLoopback_Type()
)
cnfgT1FarEndRadioLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfgT1FarEndRadioLoopback.setStatus("mandatory")


class _CnfgT1InputAlarm_Type(Integer32):
    """Custom type cnfgT1InputAlarm based on Integer32"""
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


_CnfgT1InputAlarm_Type.__name__ = "Integer32"
_CnfgT1InputAlarm_Object = MibScalar
cnfgT1InputAlarm = _CnfgT1InputAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 1, 5),
    _CnfgT1InputAlarm_Type()
)
cnfgT1InputAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfgT1InputAlarm.setStatus("mandatory")


class _CnfgAIS_Type(Integer32):
    """Custom type cnfgAIS based on Integer32"""
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


_CnfgAIS_Type.__name__ = "Integer32"
_CnfgAIS_Object = MibScalar
cnfgAIS = _CnfgAIS_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 1, 6),
    _CnfgAIS_Type()
)
cnfgAIS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfgAIS.setStatus("mandatory")


class _CnfgOrderwireAddr_Type(DisplayString):
    """Custom type cnfgOrderwireAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_CnfgOrderwireAddr_Type.__name__ = "DisplayString"
_CnfgOrderwireAddr_Object = MibScalar
cnfgOrderwireAddr = _CnfgOrderwireAddr_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 1, 7),
    _CnfgOrderwireAddr_Type()
)
cnfgOrderwireAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfgOrderwireAddr.setStatus("mandatory")


class _CnfgLinkSecurityCode_Type(DisplayString):
    """Custom type cnfgLinkSecurityCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_CnfgLinkSecurityCode_Type.__name__ = "DisplayString"
_CnfgLinkSecurityCode_Object = MibScalar
cnfgLinkSecurityCode = _CnfgLinkSecurityCode_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 1, 8),
    _CnfgLinkSecurityCode_Type()
)
cnfgLinkSecurityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfgLinkSecurityCode.setStatus("mandatory")


class _CnfgLearningFilter_Type(Integer32):
    """Custom type cnfgLearningFilter based on Integer32"""
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


_CnfgLearningFilter_Type.__name__ = "Integer32"
_CnfgLearningFilter_Object = MibScalar
cnfgLearningFilter = _CnfgLearningFilter_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 1, 9),
    _CnfgLearningFilter_Type()
)
cnfgLearningFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfgLearningFilter.setStatus("mandatory")


class _CnfgFiberOpticInterface_Type(Integer32):
    """Custom type cnfgFiberOpticInterface based on Integer32"""
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


_CnfgFiberOpticInterface_Type.__name__ = "Integer32"
_CnfgFiberOpticInterface_Object = MibScalar
cnfgFiberOpticInterface = _CnfgFiberOpticInterface_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 1, 10),
    _CnfgFiberOpticInterface_Type()
)
cnfgFiberOpticInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfgFiberOpticInterface.setStatus("mandatory")


class _CnfgEthernetDuplex_Type(Integer32):
    """Custom type cnfgEthernetDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full-duplex", 1),
          ("half-duplex", 2))
    )


_CnfgEthernetDuplex_Type.__name__ = "Integer32"
_CnfgEthernetDuplex_Object = MibScalar
cnfgEthernetDuplex = _CnfgEthernetDuplex_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 1, 11),
    _CnfgEthernetDuplex_Type()
)
cnfgEthernetDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfgEthernetDuplex.setStatus("mandatory")


class _CnfgDataRate_Type(Integer32):
    """Custom type cnfgDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("datarate2", 2),
          ("datarate3", 3),
          ("full-duplex-45-MB", 1))
    )


_CnfgDataRate_Type.__name__ = "Integer32"
_CnfgDataRate_Object = MibScalar
cnfgDataRate = _CnfgDataRate_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 1, 12),
    _CnfgDataRate_Type()
)
cnfgDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfgDataRate.setStatus("mandatory")


class _CnfgInterfaceType_Type(Integer32):
    """Custom type cnfgInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("t1-100BaseT", 1),
          ("t1-10BaseT", 2))
    )


_CnfgInterfaceType_Type.__name__ = "Integer32"
_CnfgInterfaceType_Object = MibScalar
cnfgInterfaceType = _CnfgInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 1, 13),
    _CnfgInterfaceType_Type()
)
cnfgInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfgInterfaceType.setStatus("mandatory")


class _CnfgIDUSWVersion_Type(DisplayString):
    """Custom type cnfgIDUSWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CnfgIDUSWVersion_Type.__name__ = "DisplayString"
_CnfgIDUSWVersion_Object = MibScalar
cnfgIDUSWVersion = _CnfgIDUSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 1, 14),
    _CnfgIDUSWVersion_Type()
)
cnfgIDUSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfgIDUSWVersion.setStatus("mandatory")


class _CnfgNMUSWVersion_Type(DisplayString):
    """Custom type cnfgNMUSWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CnfgNMUSWVersion_Type.__name__ = "DisplayString"
_CnfgNMUSWVersion_Object = MibScalar
cnfgNMUSWVersion = _CnfgNMUSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 1, 15),
    _CnfgNMUSWVersion_Type()
)
cnfgNMUSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfgNMUSWVersion.setStatus("mandatory")
_Status_ObjectIdentity = ObjectIdentity
status = _Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 2)
)


class _StatRadioLogHealth_Type(Integer32):
    """Custom type statRadioLogHealth based on Integer32"""
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
        *(("critical-health", 5),
          ("major-health", 4),
          ("minor-health", 3),
          ("normal-health", 1),
          ("warning-health", 2))
    )


_StatRadioLogHealth_Type.__name__ = "Integer32"
_StatRadioLogHealth_Object = MibScalar
statRadioLogHealth = _StatRadioLogHealth_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 2, 1),
    _StatRadioLogHealth_Type()
)
statRadioLogHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statRadioLogHealth.setStatus("mandatory")


class _StatNMULink_Type(Integer32):
    """Custom type statNMULink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("link-down", 1),
          ("link-up", 2))
    )


_StatNMULink_Type.__name__ = "Integer32"
_StatNMULink_Object = MibScalar
statNMULink = _StatNMULink_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 2, 2),
    _StatNMULink_Type()
)
statNMULink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statNMULink.setStatus("mandatory")


class _StatAlarmSummary_Type(Integer32):
    """Custom type statAlarmSummary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm-normal", 2),
          ("alarm-triggered", 3),
          ("alarm-unknown", 1))
    )


_StatAlarmSummary_Type.__name__ = "Integer32"
_StatAlarmSummary_Object = MibScalar
statAlarmSummary = _StatAlarmSummary_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 2, 3),
    _StatAlarmSummary_Type()
)
statAlarmSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statAlarmSummary.setStatus("mandatory")


class _StatT1Input_Type(Integer32):
    """Custom type statT1Input based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm-normal", 2),
          ("alarm-triggered", 3),
          ("alarm-unknown", 1))
    )


_StatT1Input_Type.__name__ = "Integer32"
_StatT1Input_Object = MibScalar
statT1Input = _StatT1Input_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 2, 21),
    _StatT1Input_Type()
)
statT1Input.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statT1Input.setStatus("mandatory")


class _StatT1CodeViolation_Type(Integer32):
    """Custom type statT1CodeViolation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm-normal", 2),
          ("alarm-triggered", 3),
          ("alarm-unknown", 1))
    )


_StatT1CodeViolation_Type.__name__ = "Integer32"
_StatT1CodeViolation_Object = MibScalar
statT1CodeViolation = _StatT1CodeViolation_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 2, 22),
    _StatT1CodeViolation_Type()
)
statT1CodeViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statT1CodeViolation.setStatus("mandatory")


class _StatT1LineDriver_Type(Integer32):
    """Custom type statT1LineDriver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm-normal", 2),
          ("alarm-triggered", 3),
          ("alarm-unknown", 1))
    )


_StatT1LineDriver_Type.__name__ = "Integer32"
_StatT1LineDriver_Object = MibScalar
statT1LineDriver = _StatT1LineDriver_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 2, 23),
    _StatT1LineDriver_Type()
)
statT1LineDriver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statT1LineDriver.setStatus("mandatory")


class _StatT1AIS_Type(Integer32):
    """Custom type statT1AIS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm-normal", 2),
          ("alarm-triggered", 3),
          ("alarm-unknown", 1))
    )


_StatT1AIS_Type.__name__ = "Integer32"
_StatT1AIS_Object = MibScalar
statT1AIS = _StatT1AIS_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 2, 24),
    _StatT1AIS_Type()
)
statT1AIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statT1AIS.setStatus("mandatory")


class _StatRadioSync_Type(Integer32):
    """Custom type statRadioSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm-normal", 2),
          ("alarm-triggered", 3),
          ("alarm-unknown", 1))
    )


_StatRadioSync_Type.__name__ = "Integer32"
_StatRadioSync_Object = MibScalar
statRadioSync = _StatRadioSync_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 2, 25),
    _StatRadioSync_Type()
)
statRadioSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statRadioSync.setStatus("mandatory")


class _StatBitError_Type(Integer32):
    """Custom type statBitError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm-normal", 2),
          ("alarm-triggered", 3),
          ("alarm-unknown", 1))
    )


_StatBitError_Type.__name__ = "Integer32"
_StatBitError_Object = MibScalar
statBitError = _StatBitError_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 2, 26),
    _StatBitError_Type()
)
statBitError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statBitError.setStatus("mandatory")


class _StatFan1_Type(Integer32):
    """Custom type statFan1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm-normal", 2),
          ("alarm-triggered", 3),
          ("alarm-unknown", 1))
    )


_StatFan1_Type.__name__ = "Integer32"
_StatFan1_Object = MibScalar
statFan1 = _StatFan1_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 2, 27),
    _StatFan1_Type()
)
statFan1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statFan1.setStatus("mandatory")


class _StatFan2_Type(Integer32):
    """Custom type statFan2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm-normal", 2),
          ("alarm-triggered", 3),
          ("alarm-unknown", 1))
    )


_StatFan2_Type.__name__ = "Integer32"
_StatFan2_Object = MibScalar
statFan2 = _StatFan2_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 2, 28),
    _StatFan2_Type()
)
statFan2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statFan2.setStatus("mandatory")


class _StatRxSynth_Type(Integer32):
    """Custom type statRxSynth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm-normal", 2),
          ("alarm-triggered", 3),
          ("alarm-unknown", 1))
    )


_StatRxSynth_Type.__name__ = "Integer32"
_StatRxSynth_Object = MibScalar
statRxSynth = _StatRxSynth_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 2, 29),
    _StatRxSynth_Type()
)
statRxSynth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statRxSynth.setStatus("mandatory")


class _StatTxSynth_Type(Integer32):
    """Custom type statTxSynth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm-normal", 2),
          ("alarm-triggered", 3),
          ("alarm-unknown", 1))
    )


_StatTxSynth_Type.__name__ = "Integer32"
_StatTxSynth_Object = MibScalar
statTxSynth = _StatTxSynth_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 2, 30),
    _StatTxSynth_Type()
)
statTxSynth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statTxSynth.setStatus("mandatory")
_Mgmt_ObjectIdentity = ObjectIdentity
mgmt = _Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 3)
)


class _MgmtNMULinkTrapControl_Type(Integer32):
    """Custom type mgmtNMULinkTrapControl based on Integer32"""
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
        *(("no-trap", 1),
          ("send-trap-on-alarm-transition", 2),
          ("send-trap-on-both-transitions", 4),
          ("send-trap-on-normal-transition", 3))
    )


_MgmtNMULinkTrapControl_Type.__name__ = "Integer32"
_MgmtNMULinkTrapControl_Object = MibScalar
mgmtNMULinkTrapControl = _MgmtNMULinkTrapControl_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 3, 1),
    _MgmtNMULinkTrapControl_Type()
)
mgmtNMULinkTrapControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtNMULinkTrapControl.setStatus("mandatory")


class _MgmtNMULinkSeverity_Type(Integer32):
    """Custom type mgmtNMULinkSeverity based on Integer32"""
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
        *(("critical", 5),
          ("major", 4),
          ("minor", 3),
          ("normal", 1),
          ("warning", 2))
    )


_MgmtNMULinkSeverity_Type.__name__ = "Integer32"
_MgmtNMULinkSeverity_Object = MibScalar
mgmtNMULinkSeverity = _MgmtNMULinkSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 3, 2),
    _MgmtNMULinkSeverity_Type()
)
mgmtNMULinkSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtNMULinkSeverity.setStatus("mandatory")


class _MgmtT1InputTrapControl_Type(Integer32):
    """Custom type mgmtT1InputTrapControl based on Integer32"""
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
        *(("no-trap", 1),
          ("send-trap-on-alarm-transition", 2),
          ("send-trap-on-both-transitions", 4),
          ("send-trap-on-normal-transition", 3))
    )


_MgmtT1InputTrapControl_Type.__name__ = "Integer32"
_MgmtT1InputTrapControl_Object = MibScalar
mgmtT1InputTrapControl = _MgmtT1InputTrapControl_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 3, 3),
    _MgmtT1InputTrapControl_Type()
)
mgmtT1InputTrapControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtT1InputTrapControl.setStatus("mandatory")


class _MgmtT1InputSeverity_Type(Integer32):
    """Custom type mgmtT1InputSeverity based on Integer32"""
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
        *(("critical", 5),
          ("major", 4),
          ("minor", 3),
          ("normal", 1),
          ("warning", 2))
    )


_MgmtT1InputSeverity_Type.__name__ = "Integer32"
_MgmtT1InputSeverity_Object = MibScalar
mgmtT1InputSeverity = _MgmtT1InputSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 3, 4),
    _MgmtT1InputSeverity_Type()
)
mgmtT1InputSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtT1InputSeverity.setStatus("mandatory")


class _MgmtT1CodeViolationTrapControl_Type(Integer32):
    """Custom type mgmtT1CodeViolationTrapControl based on Integer32"""
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
        *(("no-trap", 1),
          ("send-trap-on-alarm-transition", 2),
          ("send-trap-on-both-transitions", 4),
          ("send-trap-on-normal-transition", 3))
    )


_MgmtT1CodeViolationTrapControl_Type.__name__ = "Integer32"
_MgmtT1CodeViolationTrapControl_Object = MibScalar
mgmtT1CodeViolationTrapControl = _MgmtT1CodeViolationTrapControl_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 3, 5),
    _MgmtT1CodeViolationTrapControl_Type()
)
mgmtT1CodeViolationTrapControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtT1CodeViolationTrapControl.setStatus("mandatory")


class _MgmtT1CodeViolationSeverity_Type(Integer32):
    """Custom type mgmtT1CodeViolationSeverity based on Integer32"""
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
        *(("critical", 5),
          ("major", 4),
          ("minor", 3),
          ("normal", 1),
          ("warning", 2))
    )


_MgmtT1CodeViolationSeverity_Type.__name__ = "Integer32"
_MgmtT1CodeViolationSeverity_Object = MibScalar
mgmtT1CodeViolationSeverity = _MgmtT1CodeViolationSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 3, 6),
    _MgmtT1CodeViolationSeverity_Type()
)
mgmtT1CodeViolationSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtT1CodeViolationSeverity.setStatus("mandatory")


class _MgmtT1LineDriverTrapControl_Type(Integer32):
    """Custom type mgmtT1LineDriverTrapControl based on Integer32"""
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
        *(("no-trap", 1),
          ("send-trap-on-alarm-transition", 2),
          ("send-trap-on-both-transitions", 4),
          ("send-trap-on-normal-transition", 3))
    )


_MgmtT1LineDriverTrapControl_Type.__name__ = "Integer32"
_MgmtT1LineDriverTrapControl_Object = MibScalar
mgmtT1LineDriverTrapControl = _MgmtT1LineDriverTrapControl_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 3, 7),
    _MgmtT1LineDriverTrapControl_Type()
)
mgmtT1LineDriverTrapControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtT1LineDriverTrapControl.setStatus("mandatory")


class _MgmtT1LineDriverSeverity_Type(Integer32):
    """Custom type mgmtT1LineDriverSeverity based on Integer32"""
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
        *(("critical", 5),
          ("major", 4),
          ("minor", 3),
          ("normal", 1),
          ("warning", 2))
    )


_MgmtT1LineDriverSeverity_Type.__name__ = "Integer32"
_MgmtT1LineDriverSeverity_Object = MibScalar
mgmtT1LineDriverSeverity = _MgmtT1LineDriverSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 3, 8),
    _MgmtT1LineDriverSeverity_Type()
)
mgmtT1LineDriverSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtT1LineDriverSeverity.setStatus("mandatory")


class _MgmtT1AISTrapControl_Type(Integer32):
    """Custom type mgmtT1AISTrapControl based on Integer32"""
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
        *(("no-trap", 1),
          ("send-trap-on-alarm-transition", 2),
          ("send-trap-on-both-transitions", 4),
          ("send-trap-on-normal-transition", 3))
    )


_MgmtT1AISTrapControl_Type.__name__ = "Integer32"
_MgmtT1AISTrapControl_Object = MibScalar
mgmtT1AISTrapControl = _MgmtT1AISTrapControl_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 3, 9),
    _MgmtT1AISTrapControl_Type()
)
mgmtT1AISTrapControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtT1AISTrapControl.setStatus("mandatory")


class _MgmtT1AISSeverity_Type(Integer32):
    """Custom type mgmtT1AISSeverity based on Integer32"""
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
        *(("critical", 5),
          ("major", 4),
          ("minor", 3),
          ("normal", 1),
          ("warning", 2))
    )


_MgmtT1AISSeverity_Type.__name__ = "Integer32"
_MgmtT1AISSeverity_Object = MibScalar
mgmtT1AISSeverity = _MgmtT1AISSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 3, 10),
    _MgmtT1AISSeverity_Type()
)
mgmtT1AISSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtT1AISSeverity.setStatus("mandatory")


class _MgmtRadioSyncTrapControl_Type(Integer32):
    """Custom type mgmtRadioSyncTrapControl based on Integer32"""
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
        *(("no-trap", 1),
          ("send-trap-on-alarm-transition", 2),
          ("send-trap-on-both-transitions", 4),
          ("send-trap-on-normal-transition", 3))
    )


_MgmtRadioSyncTrapControl_Type.__name__ = "Integer32"
_MgmtRadioSyncTrapControl_Object = MibScalar
mgmtRadioSyncTrapControl = _MgmtRadioSyncTrapControl_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 3, 11),
    _MgmtRadioSyncTrapControl_Type()
)
mgmtRadioSyncTrapControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtRadioSyncTrapControl.setStatus("mandatory")


class _MgmtRadioSyncSeverity_Type(Integer32):
    """Custom type mgmtRadioSyncSeverity based on Integer32"""
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
        *(("critical", 5),
          ("major", 4),
          ("minor", 3),
          ("normal", 1),
          ("warning", 2))
    )


_MgmtRadioSyncSeverity_Type.__name__ = "Integer32"
_MgmtRadioSyncSeverity_Object = MibScalar
mgmtRadioSyncSeverity = _MgmtRadioSyncSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 3, 12),
    _MgmtRadioSyncSeverity_Type()
)
mgmtRadioSyncSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtRadioSyncSeverity.setStatus("mandatory")


class _MgmtBitErrorTrapControl_Type(Integer32):
    """Custom type mgmtBitErrorTrapControl based on Integer32"""
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
        *(("no-trap", 1),
          ("send-trap-on-alarm-transition", 2),
          ("send-trap-on-both-transitions", 4),
          ("send-trap-on-normal-transition", 3))
    )


_MgmtBitErrorTrapControl_Type.__name__ = "Integer32"
_MgmtBitErrorTrapControl_Object = MibScalar
mgmtBitErrorTrapControl = _MgmtBitErrorTrapControl_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 3, 13),
    _MgmtBitErrorTrapControl_Type()
)
mgmtBitErrorTrapControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtBitErrorTrapControl.setStatus("mandatory")


class _MgmtBitErrorSeverity_Type(Integer32):
    """Custom type mgmtBitErrorSeverity based on Integer32"""
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
        *(("critical", 5),
          ("major", 4),
          ("minor", 3),
          ("normal", 1),
          ("warning", 2))
    )


_MgmtBitErrorSeverity_Type.__name__ = "Integer32"
_MgmtBitErrorSeverity_Object = MibScalar
mgmtBitErrorSeverity = _MgmtBitErrorSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 3, 14),
    _MgmtBitErrorSeverity_Type()
)
mgmtBitErrorSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtBitErrorSeverity.setStatus("mandatory")


class _MgmtFan1TrapControl_Type(Integer32):
    """Custom type mgmtFan1TrapControl based on Integer32"""
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
        *(("no-trap", 1),
          ("send-trap-on-alarm-transition", 2),
          ("send-trap-on-both-transitions", 4),
          ("send-trap-on-normal-transition", 3))
    )


_MgmtFan1TrapControl_Type.__name__ = "Integer32"
_MgmtFan1TrapControl_Object = MibScalar
mgmtFan1TrapControl = _MgmtFan1TrapControl_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 3, 15),
    _MgmtFan1TrapControl_Type()
)
mgmtFan1TrapControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtFan1TrapControl.setStatus("mandatory")


class _MgmtFan1Severity_Type(Integer32):
    """Custom type mgmtFan1Severity based on Integer32"""
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
        *(("critical", 5),
          ("major", 4),
          ("minor", 3),
          ("normal", 1),
          ("warning", 2))
    )


_MgmtFan1Severity_Type.__name__ = "Integer32"
_MgmtFan1Severity_Object = MibScalar
mgmtFan1Severity = _MgmtFan1Severity_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 3, 16),
    _MgmtFan1Severity_Type()
)
mgmtFan1Severity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtFan1Severity.setStatus("mandatory")


class _MgmtFan2TrapControl_Type(Integer32):
    """Custom type mgmtFan2TrapControl based on Integer32"""
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
        *(("no-trap", 1),
          ("send-trap-on-alarm-transition", 2),
          ("send-trap-on-both-transitions", 4),
          ("send-trap-on-normal-transition", 3))
    )


_MgmtFan2TrapControl_Type.__name__ = "Integer32"
_MgmtFan2TrapControl_Object = MibScalar
mgmtFan2TrapControl = _MgmtFan2TrapControl_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 3, 17),
    _MgmtFan2TrapControl_Type()
)
mgmtFan2TrapControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtFan2TrapControl.setStatus("mandatory")


class _MgmtFan2Severity_Type(Integer32):
    """Custom type mgmtFan2Severity based on Integer32"""
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
        *(("critical", 5),
          ("major", 4),
          ("minor", 3),
          ("normal", 1),
          ("warning", 2))
    )


_MgmtFan2Severity_Type.__name__ = "Integer32"
_MgmtFan2Severity_Object = MibScalar
mgmtFan2Severity = _MgmtFan2Severity_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 3, 18),
    _MgmtFan2Severity_Type()
)
mgmtFan2Severity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtFan2Severity.setStatus("mandatory")


class _MgmtRxSynthTrapControl_Type(Integer32):
    """Custom type mgmtRxSynthTrapControl based on Integer32"""
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
        *(("no-trap", 1),
          ("send-trap-on-alarm-transition", 2),
          ("send-trap-on-both-transitions", 4),
          ("send-trap-on-normal-transition", 3))
    )


_MgmtRxSynthTrapControl_Type.__name__ = "Integer32"
_MgmtRxSynthTrapControl_Object = MibScalar
mgmtRxSynthTrapControl = _MgmtRxSynthTrapControl_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 3, 19),
    _MgmtRxSynthTrapControl_Type()
)
mgmtRxSynthTrapControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtRxSynthTrapControl.setStatus("mandatory")


class _MgmtRxSynthSeverity_Type(Integer32):
    """Custom type mgmtRxSynthSeverity based on Integer32"""
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
        *(("critical", 5),
          ("major", 4),
          ("minor", 3),
          ("normal", 1),
          ("warning", 2))
    )


_MgmtRxSynthSeverity_Type.__name__ = "Integer32"
_MgmtRxSynthSeverity_Object = MibScalar
mgmtRxSynthSeverity = _MgmtRxSynthSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 3, 20),
    _MgmtRxSynthSeverity_Type()
)
mgmtRxSynthSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtRxSynthSeverity.setStatus("mandatory")


class _MgmtTxSynthTrapControl_Type(Integer32):
    """Custom type mgmtTxSynthTrapControl based on Integer32"""
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
        *(("no-trap", 1),
          ("send-trap-on-alarm-transition", 2),
          ("send-trap-on-both-transitions", 4),
          ("send-trap-on-normal-transition", 3))
    )


_MgmtTxSynthTrapControl_Type.__name__ = "Integer32"
_MgmtTxSynthTrapControl_Object = MibScalar
mgmtTxSynthTrapControl = _MgmtTxSynthTrapControl_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 3, 21),
    _MgmtTxSynthTrapControl_Type()
)
mgmtTxSynthTrapControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtTxSynthTrapControl.setStatus("mandatory")


class _MgmtTxSynthSeverity_Type(Integer32):
    """Custom type mgmtTxSynthSeverity based on Integer32"""
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
        *(("critical", 5),
          ("major", 4),
          ("minor", 3),
          ("normal", 1),
          ("warning", 2))
    )


_MgmtTxSynthSeverity_Type.__name__ = "Integer32"
_MgmtTxSynthSeverity_Object = MibScalar
mgmtTxSynthSeverity = _MgmtTxSynthSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 3, 22),
    _MgmtTxSynthSeverity_Type()
)
mgmtTxSynthSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtTxSynthSeverity.setStatus("mandatory")


class _MgmtTrapHysteresis_Type(Integer32):
    """Custom type mgmtTrapHysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_MgmtTrapHysteresis_Type.__name__ = "Integer32"
_MgmtTrapHysteresis_Object = MibScalar
mgmtTrapHysteresis = _MgmtTrapHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 3, 61),
    _MgmtTrapHysteresis_Type()
)
mgmtTrapHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtTrapHysteresis.setStatus("mandatory")
_Perf_ObjectIdentity = ObjectIdentity
perf = _Perf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 4)
)


class _PerfCurrentBER_Type(DisplayString):
    """Custom type perfCurrentBER based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_PerfCurrentBER_Type.__name__ = "DisplayString"
_PerfCurrentBER_Object = MibScalar
perfCurrentBER = _PerfCurrentBER_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 4, 1),
    _PerfCurrentBER_Type()
)
perfCurrentBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfCurrentBER.setStatus("mandatory")
_PerfCurrentRSL_Type = Integer32
_PerfCurrentRSL_Object = MibScalar
perfCurrentRSL = _PerfCurrentRSL_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 4, 2),
    _PerfCurrentRSL_Type()
)
perfCurrentRSL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfCurrentRSL.setStatus("mandatory")
_PerfErrorSeconds_Type = Integer32
_PerfErrorSeconds_Object = MibScalar
perfErrorSeconds = _PerfErrorSeconds_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 4, 3),
    _PerfErrorSeconds_Type()
)
perfErrorSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfErrorSeconds.setStatus("mandatory")
_PerfSeverelyErroredSeconds_Type = Integer32
_PerfSeverelyErroredSeconds_Object = MibScalar
perfSeverelyErroredSeconds = _PerfSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 4, 4),
    _PerfSeverelyErroredSeconds_Type()
)
perfSeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfSeverelyErroredSeconds.setStatus("mandatory")
_PerfMinRSL_Type = Integer32
_PerfMinRSL_Object = MibScalar
perfMinRSL = _PerfMinRSL_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 4, 5),
    _PerfMinRSL_Type()
)
perfMinRSL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfMinRSL.setStatus("mandatory")
_PerfMaxRSL_Type = Integer32
_PerfMaxRSL_Object = MibScalar
perfMaxRSL = _PerfMaxRSL_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 4, 6),
    _PerfMaxRSL_Type()
)
perfMaxRSL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfMaxRSL.setStatus("mandatory")
_PerfElapsedSecondsSinceReset_Type = Integer32
_PerfElapsedSecondsSinceReset_Object = MibScalar
perfElapsedSecondsSinceReset = _PerfElapsedSecondsSinceReset_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 4, 7),
    _PerfElapsedSecondsSinceReset_Type()
)
perfElapsedSecondsSinceReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfElapsedSecondsSinceReset.setStatus("mandatory")


class _PerfHistoryReset_Type(Integer32):
    """Custom type perfHistoryReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("history-reset", 1),
          ("normal", 2))
    )


_PerfHistoryReset_Type.__name__ = "Integer32"
_PerfHistoryReset_Object = MibScalar
perfHistoryReset = _PerfHistoryReset_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 4, 8),
    _PerfHistoryReset_Type()
)
perfHistoryReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    perfHistoryReset.setStatus("mandatory")

# Managed Objects groups


# Notification objects

nmuLinkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 2, 0, 1)
)
nmuLinkTrap.setObjects(
      *(("WESTERN-MULTIPLEX-MIB", "trapSequenceNumber"),
        ("WESTERN-MULTIPLEX-RAD10006-MIB", "mgmtNMULinkSeverity"),
        ("WESTERN-MULTIPLEX-RAD10006-MIB", "statNMULink"))
)
if mibBuilder.loadTexts:
    nmuLinkTrap.setStatus(
        ""
    )

t1InTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 2, 0, 2)
)
t1InTrap.setObjects(
      *(("WESTERN-MULTIPLEX-MIB", "trapSequenceNumber"),
        ("WESTERN-MULTIPLEX-RAD10006-MIB", "mgmtT1InputSeverity"),
        ("WESTERN-MULTIPLEX-RAD10006-MIB", "statT1Input"))
)
if mibBuilder.loadTexts:
    t1InTrap.setStatus(
        ""
    )

t1CvTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 2, 0, 3)
)
t1CvTrap.setObjects(
      *(("WESTERN-MULTIPLEX-MIB", "trapSequenceNumber"),
        ("WESTERN-MULTIPLEX-RAD10006-MIB", "mgmtT1CodeViolationSeverity"),
        ("WESTERN-MULTIPLEX-RAD10006-MIB", "statT1CodeViolation"))
)
if mibBuilder.loadTexts:
    t1CvTrap.setStatus(
        ""
    )

t1LoTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 2, 0, 4)
)
t1LoTrap.setObjects(
      *(("WESTERN-MULTIPLEX-MIB", "trapSequenceNumber"),
        ("WESTERN-MULTIPLEX-RAD10006-MIB", "mgmtT1LineDriverSeverity"),
        ("WESTERN-MULTIPLEX-RAD10006-MIB", "statT1LineDriver"))
)
if mibBuilder.loadTexts:
    t1LoTrap.setStatus(
        ""
    )

t1AisTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 2, 0, 5)
)
t1AisTrap.setObjects(
      *(("WESTERN-MULTIPLEX-MIB", "trapSequenceNumber"),
        ("WESTERN-MULTIPLEX-RAD10006-MIB", "mgmtT1AISSeverity"),
        ("WESTERN-MULTIPLEX-RAD10006-MIB", "statT1AIS"))
)
if mibBuilder.loadTexts:
    t1AisTrap.setStatus(
        ""
    )

radioSyncTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 2, 0, 6)
)
radioSyncTrap.setObjects(
      *(("WESTERN-MULTIPLEX-MIB", "trapSequenceNumber"),
        ("WESTERN-MULTIPLEX-RAD10006-MIB", "mgmtRadioSyncSeverity"),
        ("WESTERN-MULTIPLEX-RAD10006-MIB", "statRadioSync"))
)
if mibBuilder.loadTexts:
    radioSyncTrap.setStatus(
        ""
    )

berTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 2, 0, 7)
)
berTrap.setObjects(
      *(("WESTERN-MULTIPLEX-MIB", "trapSequenceNumber"),
        ("WESTERN-MULTIPLEX-RAD10006-MIB", "mgmtBitErrorSeverity"),
        ("WESTERN-MULTIPLEX-RAD10006-MIB", "statBitError"))
)
if mibBuilder.loadTexts:
    berTrap.setStatus(
        ""
    )

fan1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 2, 0, 8)
)
fan1Trap.setObjects(
      *(("WESTERN-MULTIPLEX-MIB", "trapSequenceNumber"),
        ("WESTERN-MULTIPLEX-RAD10006-MIB", "mgmtFan1Severity"),
        ("WESTERN-MULTIPLEX-RAD10006-MIB", "statFan1"))
)
if mibBuilder.loadTexts:
    fan1Trap.setStatus(
        ""
    )

fan2Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 2, 0, 9)
)
fan2Trap.setObjects(
      *(("WESTERN-MULTIPLEX-MIB", "trapSequenceNumber"),
        ("WESTERN-MULTIPLEX-RAD10006-MIB", "mgmtFan2Severity"),
        ("WESTERN-MULTIPLEX-RAD10006-MIB", "statFan2"))
)
if mibBuilder.loadTexts:
    fan2Trap.setStatus(
        ""
    )

rxSynthTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 2, 0, 10)
)
rxSynthTrap.setObjects(
      *(("WESTERN-MULTIPLEX-MIB", "trapSequenceNumber"),
        ("WESTERN-MULTIPLEX-RAD10006-MIB", "mgmtRxSynthSeverity"),
        ("WESTERN-MULTIPLEX-RAD10006-MIB", "statRxSynth"))
)
if mibBuilder.loadTexts:
    rxSynthTrap.setStatus(
        ""
    )

txSynthTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3727, 20, 20, 2, 0, 11)
)
txSynthTrap.setObjects(
      *(("WESTERN-MULTIPLEX-MIB", "trapSequenceNumber"),
        ("WESTERN-MULTIPLEX-RAD10006-MIB", "mgmtTxSynthSeverity"),
        ("WESTERN-MULTIPLEX-RAD10006-MIB", "statTxSynth"))
)
if mibBuilder.loadTexts:
    txSynthTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WESTERN-MULTIPLEX-RAD10006-MIB",
    **{"western-multiplex": western_multiplex,
       "tsunami100-06": tsunami100_06,
       "radio": radio,
       "config": config,
       "cnfgT1LineCode": cnfgT1LineCode,
       "cnfgT1LineBuildOut": cnfgT1LineBuildOut,
       "cnfgT1NearEndRadioLoopback": cnfgT1NearEndRadioLoopback,
       "cnfgT1FarEndRadioLoopback": cnfgT1FarEndRadioLoopback,
       "cnfgT1InputAlarm": cnfgT1InputAlarm,
       "cnfgAIS": cnfgAIS,
       "cnfgOrderwireAddr": cnfgOrderwireAddr,
       "cnfgLinkSecurityCode": cnfgLinkSecurityCode,
       "cnfgLearningFilter": cnfgLearningFilter,
       "cnfgFiberOpticInterface": cnfgFiberOpticInterface,
       "cnfgEthernetDuplex": cnfgEthernetDuplex,
       "cnfgDataRate": cnfgDataRate,
       "cnfgInterfaceType": cnfgInterfaceType,
       "cnfgIDUSWVersion": cnfgIDUSWVersion,
       "cnfgNMUSWVersion": cnfgNMUSWVersion,
       "status": status,
       "nmuLinkTrap": nmuLinkTrap,
       "t1InTrap": t1InTrap,
       "t1CvTrap": t1CvTrap,
       "t1LoTrap": t1LoTrap,
       "t1AisTrap": t1AisTrap,
       "radioSyncTrap": radioSyncTrap,
       "berTrap": berTrap,
       "fan1Trap": fan1Trap,
       "fan2Trap": fan2Trap,
       "rxSynthTrap": rxSynthTrap,
       "txSynthTrap": txSynthTrap,
       "statRadioLogHealth": statRadioLogHealth,
       "statNMULink": statNMULink,
       "statAlarmSummary": statAlarmSummary,
       "statT1Input": statT1Input,
       "statT1CodeViolation": statT1CodeViolation,
       "statT1LineDriver": statT1LineDriver,
       "statT1AIS": statT1AIS,
       "statRadioSync": statRadioSync,
       "statBitError": statBitError,
       "statFan1": statFan1,
       "statFan2": statFan2,
       "statRxSynth": statRxSynth,
       "statTxSynth": statTxSynth,
       "mgmt": mgmt,
       "mgmtNMULinkTrapControl": mgmtNMULinkTrapControl,
       "mgmtNMULinkSeverity": mgmtNMULinkSeverity,
       "mgmtT1InputTrapControl": mgmtT1InputTrapControl,
       "mgmtT1InputSeverity": mgmtT1InputSeverity,
       "mgmtT1CodeViolationTrapControl": mgmtT1CodeViolationTrapControl,
       "mgmtT1CodeViolationSeverity": mgmtT1CodeViolationSeverity,
       "mgmtT1LineDriverTrapControl": mgmtT1LineDriverTrapControl,
       "mgmtT1LineDriverSeverity": mgmtT1LineDriverSeverity,
       "mgmtT1AISTrapControl": mgmtT1AISTrapControl,
       "mgmtT1AISSeverity": mgmtT1AISSeverity,
       "mgmtRadioSyncTrapControl": mgmtRadioSyncTrapControl,
       "mgmtRadioSyncSeverity": mgmtRadioSyncSeverity,
       "mgmtBitErrorTrapControl": mgmtBitErrorTrapControl,
       "mgmtBitErrorSeverity": mgmtBitErrorSeverity,
       "mgmtFan1TrapControl": mgmtFan1TrapControl,
       "mgmtFan1Severity": mgmtFan1Severity,
       "mgmtFan2TrapControl": mgmtFan2TrapControl,
       "mgmtFan2Severity": mgmtFan2Severity,
       "mgmtRxSynthTrapControl": mgmtRxSynthTrapControl,
       "mgmtRxSynthSeverity": mgmtRxSynthSeverity,
       "mgmtTxSynthTrapControl": mgmtTxSynthTrapControl,
       "mgmtTxSynthSeverity": mgmtTxSynthSeverity,
       "mgmtTrapHysteresis": mgmtTrapHysteresis,
       "perf": perf,
       "perfCurrentBER": perfCurrentBER,
       "perfCurrentRSL": perfCurrentRSL,
       "perfErrorSeconds": perfErrorSeconds,
       "perfSeverelyErroredSeconds": perfSeverelyErroredSeconds,
       "perfMinRSL": perfMinRSL,
       "perfMaxRSL": perfMaxRSL,
       "perfElapsedSecondsSinceReset": perfElapsedSecondsSinceReset,
       "perfHistoryReset": perfHistoryReset}
)
