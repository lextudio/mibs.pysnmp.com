# SNMP MIB module (NSCRTV-ROOT) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NSCRTV-ROOT
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:32 2024
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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
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

_NscrtvRoot_ObjectIdentity = ObjectIdentity
nscrtvRoot = _NscrtvRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409)
)
_NscrtvHFCemsTree_ObjectIdentity = ObjectIdentity
nscrtvHFCemsTree = _NscrtvHFCemsTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 1)
)
_PropertyIdent_ObjectIdentity = ObjectIdentity
propertyIdent = _PropertyIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 1, 1)
)
_AnalogPropertyTable_Object = MibTable
analogPropertyTable = _AnalogPropertyTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 1, 1)
)
if mibBuilder.loadTexts:
    analogPropertyTable.setStatus("mandatory")
_AnalogPropertyEntry_Object = MibTableRow
analogPropertyEntry = _AnalogPropertyEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 1, 1, 1)
)
analogPropertyEntry.setIndexNames(
    (0, "NSCRTV-ROOT", "analogParameterOID"),
)
if mibBuilder.loadTexts:
    analogPropertyEntry.setStatus("mandatory")
_AnalogParameterOID_Type = ObjectIdentifier
_AnalogParameterOID_Object = MibTableColumn
analogParameterOID = _AnalogParameterOID_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 1, 1, 1, 1),
    _AnalogParameterOID_Type()
)
analogParameterOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analogParameterOID.setStatus("mandatory")


class _AlarmEnable_Type(OctetString):
    """Custom type alarmEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AlarmEnable_Type.__name__ = "OctetString"
_AlarmEnable_Object = MibTableColumn
alarmEnable = _AlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 1, 1, 1, 2),
    _AlarmEnable_Type()
)
alarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmEnable.setStatus("mandatory")


class _AnalogAlarmState_Type(Integer32):
    """Custom type analogAlarmState based on Integer32"""
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
        *(("aasHI", 3),
          ("aasHIHI", 2),
          ("aasLO", 4),
          ("aasLOLO", 5),
          ("aasNominal", 1))
    )


_AnalogAlarmState_Type.__name__ = "Integer32"
_AnalogAlarmState_Object = MibTableColumn
analogAlarmState = _AnalogAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 1, 1, 1, 3),
    _AnalogAlarmState_Type()
)
analogAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analogAlarmState.setStatus("mandatory")
_AnalogAlarmHIHI_Type = Integer32
_AnalogAlarmHIHI_Object = MibTableColumn
analogAlarmHIHI = _AnalogAlarmHIHI_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 1, 1, 1, 4),
    _AnalogAlarmHIHI_Type()
)
analogAlarmHIHI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogAlarmHIHI.setStatus("mandatory")
_AnalogAlarmHI_Type = Integer32
_AnalogAlarmHI_Object = MibTableColumn
analogAlarmHI = _AnalogAlarmHI_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 1, 1, 1, 5),
    _AnalogAlarmHI_Type()
)
analogAlarmHI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogAlarmHI.setStatus("mandatory")
_AnalogAlarmLO_Type = Integer32
_AnalogAlarmLO_Object = MibTableColumn
analogAlarmLO = _AnalogAlarmLO_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 1, 1, 1, 6),
    _AnalogAlarmLO_Type()
)
analogAlarmLO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogAlarmLO.setStatus("mandatory")
_AnalogAlarmLOLO_Type = Integer32
_AnalogAlarmLOLO_Object = MibTableColumn
analogAlarmLOLO = _AnalogAlarmLOLO_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 1, 1, 1, 7),
    _AnalogAlarmLOLO_Type()
)
analogAlarmLOLO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogAlarmLOLO.setStatus("mandatory")
_AnalogAlarmDeadband_Type = Integer32
_AnalogAlarmDeadband_Object = MibTableColumn
analogAlarmDeadband = _AnalogAlarmDeadband_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 1, 1, 1, 8),
    _AnalogAlarmDeadband_Type()
)
analogAlarmDeadband.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogAlarmDeadband.setStatus("mandatory")
_DiscretePropertyTable_Object = MibTable
discretePropertyTable = _DiscretePropertyTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 1, 2)
)
if mibBuilder.loadTexts:
    discretePropertyTable.setStatus("mandatory")
_DiscretePropertyEntry_Object = MibTableRow
discretePropertyEntry = _DiscretePropertyEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 1, 2, 1)
)
discretePropertyEntry.setIndexNames(
    (0, "NSCRTV-ROOT", "discreteParameterOID"),
    (0, "NSCRTV-ROOT", "discreteAlarmValue"),
)
if mibBuilder.loadTexts:
    discretePropertyEntry.setStatus("mandatory")
_DiscreteParameterOID_Type = ObjectIdentifier
_DiscreteParameterOID_Object = MibTableColumn
discreteParameterOID = _DiscreteParameterOID_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 1, 2, 1, 1),
    _DiscreteParameterOID_Type()
)
discreteParameterOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    discreteParameterOID.setStatus("mandatory")
_DiscreteAlarmValue_Type = Integer32
_DiscreteAlarmValue_Object = MibTableColumn
discreteAlarmValue = _DiscreteAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 1, 2, 1, 2),
    _DiscreteAlarmValue_Type()
)
discreteAlarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    discreteAlarmValue.setStatus("mandatory")


class _DiscreteAlarmEnable_Type(Integer32):
    """Custom type discreteAlarmEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enableMajor", 2),
          ("enableMinor", 3))
    )


_DiscreteAlarmEnable_Type.__name__ = "Integer32"
_DiscreteAlarmEnable_Object = MibTableColumn
discreteAlarmEnable = _DiscreteAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 1, 2, 1, 3),
    _DiscreteAlarmEnable_Type()
)
discreteAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    discreteAlarmEnable.setStatus("mandatory")


class _DiscreteAlarmState_Type(Integer32):
    """Custom type discreteAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("dasDiscreteMajor", 6),
          ("dasDiscreteMinor", 7),
          ("dasNominal", 1))
    )


_DiscreteAlarmState_Type.__name__ = "Integer32"
_DiscreteAlarmState_Object = MibTableColumn
discreteAlarmState = _DiscreteAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 1, 2, 1, 4),
    _DiscreteAlarmState_Type()
)
discreteAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    discreteAlarmState.setStatus("mandatory")
_CurrentAlarmTable_Object = MibTable
currentAlarmTable = _CurrentAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 1, 3)
)
if mibBuilder.loadTexts:
    currentAlarmTable.setStatus("mandatory")
_CurrentAlarmEntry_Object = MibTableRow
currentAlarmEntry = _CurrentAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 1, 3, 1)
)
currentAlarmEntry.setIndexNames(
    (0, "NSCRTV-ROOT", "currentAlarmOID"),
)
if mibBuilder.loadTexts:
    currentAlarmEntry.setStatus("mandatory")
_CurrentAlarmOID_Type = ObjectIdentifier
_CurrentAlarmOID_Object = MibTableColumn
currentAlarmOID = _CurrentAlarmOID_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 1, 3, 1, 1),
    _CurrentAlarmOID_Type()
)
currentAlarmOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentAlarmOID.setStatus("mandatory")


class _CurrentAlarmState_Type(Integer32):
    """Custom type currentAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("caasDiscreteMajor", 6),
          ("caasDiscreteMinor", 7),
          ("caasHI", 3),
          ("caasHIHI", 2),
          ("caasLO", 4),
          ("caasLOLO", 5))
    )


_CurrentAlarmState_Type.__name__ = "Integer32"
_CurrentAlarmState_Object = MibTableColumn
currentAlarmState = _CurrentAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 1, 3, 1, 2),
    _CurrentAlarmState_Type()
)
currentAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentAlarmState.setStatus("mandatory")
_CurrentAlarmValue_Type = Integer32
_CurrentAlarmValue_Object = MibTableColumn
currentAlarmValue = _CurrentAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 1, 3, 1, 3),
    _CurrentAlarmValue_Type()
)
currentAlarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentAlarmValue.setStatus("mandatory")
_AlarmsIdent_ObjectIdentity = ObjectIdentity
alarmsIdent = _AlarmsIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 1, 2)
)
_AlarmLogNumberOfEntries_Type = Integer32
_AlarmLogNumberOfEntries_Object = MibScalar
alarmLogNumberOfEntries = _AlarmLogNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 2, 1),
    _AlarmLogNumberOfEntries_Type()
)
alarmLogNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLogNumberOfEntries.setStatus("mandatory")
_AlarmLogLastIndex_Type = Integer32
_AlarmLogLastIndex_Object = MibScalar
alarmLogLastIndex = _AlarmLogLastIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 2, 2),
    _AlarmLogLastIndex_Type()
)
alarmLogLastIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLogLastIndex.setStatus("mandatory")
_AlarmLogTable_Object = MibTable
alarmLogTable = _AlarmLogTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 2, 3)
)
if mibBuilder.loadTexts:
    alarmLogTable.setStatus("mandatory")
_AlarmLogEntry_Object = MibTableRow
alarmLogEntry = _AlarmLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 2, 3, 1)
)
alarmLogEntry.setIndexNames(
    (0, "NSCRTV-ROOT", "alarmLogIndex"),
)
if mibBuilder.loadTexts:
    alarmLogEntry.setStatus("mandatory")


class _AlarmLogIndex_Type(Integer32):
    """Custom type alarmLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_AlarmLogIndex_Type.__name__ = "Integer32"
_AlarmLogIndex_Object = MibTableColumn
alarmLogIndex = _AlarmLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 2, 3, 1, 1),
    _AlarmLogIndex_Type()
)
alarmLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLogIndex.setStatus("mandatory")


class _AlarmLogInformation_Type(OctetString):
    """Custom type alarmLogInformation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 255),
    )


_AlarmLogInformation_Type.__name__ = "OctetString"
_AlarmLogInformation_Object = MibTableColumn
alarmLogInformation = _AlarmLogInformation_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 2, 3, 1, 2),
    _AlarmLogInformation_Type()
)
alarmLogInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLogInformation.setStatus("mandatory")
_AlarmText_Type = DisplayString
_AlarmText_Object = MibScalar
alarmText = _AlarmText_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 2, 4),
    _AlarmText_Type()
)
alarmText.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmText.setStatus("optional")
_CommonIdent_ObjectIdentity = ObjectIdentity
commonIdent = _CommonIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3)
)
_CommonAdminGroup_ObjectIdentity = ObjectIdentity
commonAdminGroup = _CommonAdminGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 1)
)


class _CommonNELogicalID_Type(OctetString):
    """Custom type commonNELogicalID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CommonNELogicalID_Type.__name__ = "OctetString"
_CommonNELogicalID_Object = MibScalar
commonNELogicalID = _CommonNELogicalID_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 1, 1),
    _CommonNELogicalID_Type()
)
commonNELogicalID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonNELogicalID.setStatus("mandatory")


class _CommonNEVendor_Type(DisplayString):
    """Custom type commonNEVendor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CommonNEVendor_Type.__name__ = "DisplayString"
_CommonNEVendor_Object = MibScalar
commonNEVendor = _CommonNEVendor_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 1, 2),
    _CommonNEVendor_Type()
)
commonNEVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonNEVendor.setStatus("mandatory")


class _CommonNEModelNumber_Type(DisplayString):
    """Custom type commonNEModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CommonNEModelNumber_Type.__name__ = "DisplayString"
_CommonNEModelNumber_Object = MibScalar
commonNEModelNumber = _CommonNEModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 1, 3),
    _CommonNEModelNumber_Type()
)
commonNEModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonNEModelNumber.setStatus("mandatory")


class _CommonNESerialNumber_Type(DisplayString):
    """Custom type commonNESerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CommonNESerialNumber_Type.__name__ = "DisplayString"
_CommonNESerialNumber_Object = MibScalar
commonNESerialNumber = _CommonNESerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 1, 4),
    _CommonNESerialNumber_Type()
)
commonNESerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonNESerialNumber.setStatus("mandatory")


class _CommonNEVendorInfo_Type(DisplayString):
    """Custom type commonNEVendorInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CommonNEVendorInfo_Type.__name__ = "DisplayString"
_CommonNEVendorInfo_Object = MibScalar
commonNEVendorInfo = _CommonNEVendorInfo_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 1, 5),
    _CommonNEVendorInfo_Type()
)
commonNEVendorInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonNEVendorInfo.setStatus("optional")


class _CommonNEStatus_Type(OctetString):
    """Custom type commonNEStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_CommonNEStatus_Type.__name__ = "OctetString"
_CommonNEStatus_Object = MibScalar
commonNEStatus = _CommonNEStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 1, 6),
    _CommonNEStatus_Type()
)
commonNEStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonNEStatus.setStatus("mandatory")


class _CommonReset_Type(Integer32):
    """Custom type commonReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_CommonReset_Type.__name__ = "Integer32"
_CommonReset_Object = MibScalar
commonReset = _CommonReset_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 1, 7),
    _CommonReset_Type()
)
commonReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonReset.setStatus("mandatory")


class _CommonAlarmDetectionControl_Type(Integer32):
    """Custom type commonAlarmDetectionControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("detectionDisabled", 1),
          ("detectionEnabled", 2),
          ("detectionEnabledAndRegenerate", 3))
    )


_CommonAlarmDetectionControl_Type.__name__ = "Integer32"
_CommonAlarmDetectionControl_Object = MibScalar
commonAlarmDetectionControl = _CommonAlarmDetectionControl_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 1, 8),
    _CommonAlarmDetectionControl_Type()
)
commonAlarmDetectionControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonAlarmDetectionControl.setStatus("mandatory")
_CommonNetworkAddress_Type = IpAddress
_CommonNetworkAddress_Object = MibScalar
commonNetworkAddress = _CommonNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 1, 9),
    _CommonNetworkAddress_Type()
)
commonNetworkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonNetworkAddress.setStatus("mandatory")
_CommonCheckCode_Type = Integer32
_CommonCheckCode_Object = MibScalar
commonCheckCode = _CommonCheckCode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 1, 10),
    _CommonCheckCode_Type()
)
commonCheckCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonCheckCode.setStatus("mandatory")


class _CommonTrapCommunityString_Type(OctetString):
    """Custom type commonTrapCommunityString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CommonTrapCommunityString_Type.__name__ = "OctetString"
_CommonTrapCommunityString_Object = MibScalar
commonTrapCommunityString = _CommonTrapCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 1, 11),
    _CommonTrapCommunityString_Type()
)
commonTrapCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonTrapCommunityString.setStatus("mandatory")


class _CommonTamperStatus_Type(Integer32):
    """Custom type commonTamperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("compromised", 2),
          ("intact", 1))
    )


_CommonTamperStatus_Type.__name__ = "Integer32"
_CommonTamperStatus_Object = MibScalar
commonTamperStatus = _CommonTamperStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 1, 12),
    _CommonTamperStatus_Type()
)
commonTamperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonTamperStatus.setStatus("optional")


class _CommonInternalTemperature_Type(Integer32):
    """Custom type commonInternalTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_CommonInternalTemperature_Type.__name__ = "Integer32"
_CommonInternalTemperature_Object = MibScalar
commonInternalTemperature = _CommonInternalTemperature_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 1, 13),
    _CommonInternalTemperature_Type()
)
commonInternalTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonInternalTemperature.setStatus("optional")
_CommonTime_Type = Integer32
_CommonTime_Object = MibScalar
commonTime = _CommonTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 1, 14),
    _CommonTime_Type()
)
commonTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonTime.setStatus("optional")
_CommonVarBindings_Type = Integer32
_CommonVarBindings_Object = MibScalar
commonVarBindings = _CommonVarBindings_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 1, 15),
    _CommonVarBindings_Type()
)
commonVarBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonVarBindings.setStatus("mandatory")


class _CommonResetCause_Type(Integer32):
    """Custom type commonResetCause based on Integer32"""
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
        *(("command", 3),
          ("craft", 5),
          ("other", 1),
          ("powerup", 2),
          ("watchdog", 4))
    )


_CommonResetCause_Type.__name__ = "Integer32"
_CommonResetCause_Object = MibScalar
commonResetCause = _CommonResetCause_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 1, 16),
    _CommonResetCause_Type()
)
commonResetCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonResetCause.setStatus("mandatory")


class _CommonCraftStatus_Type(Integer32):
    """Custom type commonCraftStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 2),
          ("disconnected", 1))
    )


_CommonCraftStatus_Type.__name__ = "Integer32"
_CommonCraftStatus_Object = MibScalar
commonCraftStatus = _CommonCraftStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 1, 17),
    _CommonCraftStatus_Type()
)
commonCraftStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonCraftStatus.setStatus("mandatory")
_CommonDeviceOID_Type = ObjectIdentifier
_CommonDeviceOID_Object = MibScalar
commonDeviceOID = _CommonDeviceOID_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 1, 18),
    _CommonDeviceOID_Type()
)
commonDeviceOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonDeviceOID.setStatus("optional")


class _CommonDeviceId_Type(OctetString):
    """Custom type commonDeviceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_CommonDeviceId_Type.__name__ = "OctetString"
_CommonDeviceId_Object = MibScalar
commonDeviceId = _CommonDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 1, 19),
    _CommonDeviceId_Type()
)
commonDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonDeviceId.setStatus("optional")


class _Commondownload_Type(Integer32):
    """Custom type commondownload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_Commondownload_Type.__name__ = "Integer32"
_Commondownload_Object = MibScalar
commondownload = _Commondownload_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 1, 20),
    _Commondownload_Type()
)
commondownload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commondownload.setStatus("mandatory")
_CommonAdminUseRf_ObjectIdentity = ObjectIdentity
commonAdminUseRf = _CommonAdminUseRf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 2)
)
_CommonMACGroup_ObjectIdentity = ObjectIdentity
commonMACGroup = _CommonMACGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 2, 1)
)
_CommonMacAddress_ObjectIdentity = ObjectIdentity
commonMacAddress = _CommonMacAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 2, 1, 1)
)
_CommonPhysAddress_Type = OctetString
_CommonPhysAddress_Object = MibScalar
commonPhysAddress = _CommonPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 2, 1, 1, 1),
    _CommonPhysAddress_Type()
)
commonPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonPhysAddress.setStatus("mandatory")


class _CommonMaxMulticastAddresses_Type(Integer32):
    """Custom type commonMaxMulticastAddresses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 255),
    )


_CommonMaxMulticastAddresses_Type.__name__ = "Integer32"
_CommonMaxMulticastAddresses_Object = MibScalar
commonMaxMulticastAddresses = _CommonMaxMulticastAddresses_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 2, 1, 1, 2),
    _CommonMaxMulticastAddresses_Type()
)
commonMaxMulticastAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonMaxMulticastAddresses.setStatus("mandatory")
_CommonMulticastAddressTable_Object = MibTable
commonMulticastAddressTable = _CommonMulticastAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    commonMulticastAddressTable.setStatus("mandatory")
_CommonMulticastAddressEntry_Object = MibTableRow
commonMulticastAddressEntry = _CommonMulticastAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 2, 1, 1, 3, 1)
)
commonMulticastAddressEntry.setIndexNames(
    (0, "NSCRTV-ROOT", "commonMulticastAddressIndex"),
)
if mibBuilder.loadTexts:
    commonMulticastAddressEntry.setStatus("mandatory")


class _CommonMulticastAddressIndex_Type(Integer32):
    """Custom type commonMulticastAddressIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CommonMulticastAddressIndex_Type.__name__ = "Integer32"
_CommonMulticastAddressIndex_Object = MibTableColumn
commonMulticastAddressIndex = _CommonMulticastAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 2, 1, 1, 3, 1, 1),
    _CommonMulticastAddressIndex_Type()
)
commonMulticastAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonMulticastAddressIndex.setStatus("mandatory")


class _CommonMulticastAddressNumber_Type(OctetString):
    """Custom type commonMulticastAddressNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_CommonMulticastAddressNumber_Type.__name__ = "OctetString"
_CommonMulticastAddressNumber_Object = MibTableColumn
commonMulticastAddressNumber = _CommonMulticastAddressNumber_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 2, 1, 1, 3, 1, 2),
    _CommonMulticastAddressNumber_Type()
)
commonMulticastAddressNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonMulticastAddressNumber.setStatus("mandatory")
_CommonBackoffParams_ObjectIdentity = ObjectIdentity
commonBackoffParams = _CommonBackoffParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 2, 1, 2)
)


class _CommonBackoffPeriod_Type(Integer32):
    """Custom type commonBackoffPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_CommonBackoffPeriod_Type.__name__ = "Integer32"
_CommonBackoffPeriod_Object = MibScalar
commonBackoffPeriod = _CommonBackoffPeriod_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 2, 1, 2, 1),
    _CommonBackoffPeriod_Type()
)
commonBackoffPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonBackoffPeriod.setStatus("mandatory")


class _CommonACKTimeoutWindow_Type(Integer32):
    """Custom type commonACKTimeoutWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CommonACKTimeoutWindow_Type.__name__ = "Integer32"
_CommonACKTimeoutWindow_Object = MibScalar
commonACKTimeoutWindow = _CommonACKTimeoutWindow_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 2, 1, 2, 2),
    _CommonACKTimeoutWindow_Type()
)
commonACKTimeoutWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonACKTimeoutWindow.setStatus("mandatory")


class _CommonMaximumMACLayerRetries_Type(Integer32):
    """Custom type commonMaximumMACLayerRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CommonMaximumMACLayerRetries_Type.__name__ = "Integer32"
_CommonMaximumMACLayerRetries_Object = MibScalar
commonMaximumMACLayerRetries = _CommonMaximumMACLayerRetries_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 2, 1, 2, 3),
    _CommonMaximumMACLayerRetries_Type()
)
commonMaximumMACLayerRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonMaximumMACLayerRetries.setStatus("mandatory")
_CommonMaxPayloadSize_Type = Integer32
_CommonMaxPayloadSize_Object = MibScalar
commonMaxPayloadSize = _CommonMaxPayloadSize_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 2, 1, 2, 4),
    _CommonMaxPayloadSize_Type()
)
commonMaxPayloadSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonMaxPayloadSize.setStatus("mandatory")


class _CommonBackoffMinimumExponent_Type(Integer32):
    """Custom type commonBackoffMinimumExponent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CommonBackoffMinimumExponent_Type.__name__ = "Integer32"
_CommonBackoffMinimumExponent_Object = MibScalar
commonBackoffMinimumExponent = _CommonBackoffMinimumExponent_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 2, 1, 2, 5),
    _CommonBackoffMinimumExponent_Type()
)
commonBackoffMinimumExponent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonBackoffMinimumExponent.setStatus("mandatory")


class _CommonBackoffMaximumExponent_Type(Integer32):
    """Custom type commonBackoffMaximumExponent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CommonBackoffMaximumExponent_Type.__name__ = "Integer32"
_CommonBackoffMaximumExponent_Object = MibScalar
commonBackoffMaximumExponent = _CommonBackoffMaximumExponent_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 2, 1, 2, 6),
    _CommonBackoffMaximumExponent_Type()
)
commonBackoffMaximumExponent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonBackoffMaximumExponent.setStatus("mandatory")
_CommonMacStats_ObjectIdentity = ObjectIdentity
commonMacStats = _CommonMacStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 2, 1, 3)
)
_CommonForwardPathLOSEvents_Type = Counter32
_CommonForwardPathLOSEvents_Object = MibScalar
commonForwardPathLOSEvents = _CommonForwardPathLOSEvents_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 2, 1, 3, 1),
    _CommonForwardPathLOSEvents_Type()
)
commonForwardPathLOSEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonForwardPathLOSEvents.setStatus("optional")
_CommonForwardPathFramingErrors_Type = Counter32
_CommonForwardPathFramingErrors_Object = MibScalar
commonForwardPathFramingErrors = _CommonForwardPathFramingErrors_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 2, 1, 3, 2),
    _CommonForwardPathFramingErrors_Type()
)
commonForwardPathFramingErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonForwardPathFramingErrors.setStatus("optional")
_CommonForwardPathCRCErrors_Type = Counter32
_CommonForwardPathCRCErrors_Object = MibScalar
commonForwardPathCRCErrors = _CommonForwardPathCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 2, 1, 3, 3),
    _CommonForwardPathCRCErrors_Type()
)
commonForwardPathCRCErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonForwardPathCRCErrors.setStatus("optional")
_CommonInvalidMacCmds_Type = Counter32
_CommonInvalidMacCmds_Object = MibScalar
commonInvalidMacCmds = _CommonInvalidMacCmds_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 2, 1, 3, 4),
    _CommonInvalidMacCmds_Type()
)
commonInvalidMacCmds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonInvalidMacCmds.setStatus("optional")
_CommonBackwardPathCollisionTimes_Type = Counter32
_CommonBackwardPathCollisionTimes_Object = MibScalar
commonBackwardPathCollisionTimes = _CommonBackwardPathCollisionTimes_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 2, 1, 3, 5),
    _CommonBackwardPathCollisionTimes_Type()
)
commonBackwardPathCollisionTimes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonBackwardPathCollisionTimes.setStatus("optional")
_CommonRfGroup_ObjectIdentity = ObjectIdentity
commonRfGroup = _CommonRfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 2, 2)
)


class _CommonReturnPathFrequency_Type(Integer32):
    """Custom type commonReturnPathFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_CommonReturnPathFrequency_Type.__name__ = "Integer32"
_CommonReturnPathFrequency_Object = MibScalar
commonReturnPathFrequency = _CommonReturnPathFrequency_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 2, 2, 1),
    _CommonReturnPathFrequency_Type()
)
commonReturnPathFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonReturnPathFrequency.setStatus("mandatory")


class _CommonForwardPathFrequency_Type(Integer32):
    """Custom type commonForwardPathFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_CommonForwardPathFrequency_Type.__name__ = "Integer32"
_CommonForwardPathFrequency_Object = MibScalar
commonForwardPathFrequency = _CommonForwardPathFrequency_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 2, 2, 2),
    _CommonForwardPathFrequency_Type()
)
commonForwardPathFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonForwardPathFrequency.setStatus("mandatory")


class _CommonProvisionedReturnPowerLevel_Type(Integer32):
    """Custom type commonProvisionedReturnPowerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_CommonProvisionedReturnPowerLevel_Type.__name__ = "Integer32"
_CommonProvisionedReturnPowerLevel_Object = MibScalar
commonProvisionedReturnPowerLevel = _CommonProvisionedReturnPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 2, 2, 3),
    _CommonProvisionedReturnPowerLevel_Type()
)
commonProvisionedReturnPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonProvisionedReturnPowerLevel.setStatus("mandatory")


class _CommonForwardPathReceiveLevel_Type(Integer32):
    """Custom type commonForwardPathReceiveLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_CommonForwardPathReceiveLevel_Type.__name__ = "Integer32"
_CommonForwardPathReceiveLevel_Object = MibScalar
commonForwardPathReceiveLevel = _CommonForwardPathReceiveLevel_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 2, 2, 4),
    _CommonForwardPathReceiveLevel_Type()
)
commonForwardPathReceiveLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonForwardPathReceiveLevel.setStatus("optional")


class _CommonMaxReturnPower_Type(Integer32):
    """Custom type commonMaxReturnPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_CommonMaxReturnPower_Type.__name__ = "Integer32"
_CommonMaxReturnPower_Object = MibScalar
commonMaxReturnPower = _CommonMaxReturnPower_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 2, 2, 5),
    _CommonMaxReturnPower_Type()
)
commonMaxReturnPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonMaxReturnPower.setStatus("mandatory")
_CommonAdminUseEthernet_ObjectIdentity = ObjectIdentity
commonAdminUseEthernet = _CommonAdminUseEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 3)
)
_CommonAgentGroup_ObjectIdentity = ObjectIdentity
commonAgentGroup = _CommonAgentGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 3, 1)
)


class _CommonAgentBootWay_Type(Integer32):
    """Custom type commonAgentBootWay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bootBOOTP", 2),
          ("bootDefault", 1),
          ("bootTFTP", 3))
    )


_CommonAgentBootWay_Type.__name__ = "Integer32"
_CommonAgentBootWay_Object = MibScalar
commonAgentBootWay = _CommonAgentBootWay_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 3, 1, 1),
    _CommonAgentBootWay_Type()
)
commonAgentBootWay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonAgentBootWay.setStatus("mandatory")


class _CommonAgentReset_Type(Integer32):
    """Custom type commonAgentReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_CommonAgentReset_Type.__name__ = "Integer32"
_CommonAgentReset_Object = MibScalar
commonAgentReset = _CommonAgentReset_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 3, 1, 2),
    _CommonAgentReset_Type()
)
commonAgentReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonAgentReset.setStatus("mandatory")
_CommonAgentMaxTraps_Type = Integer32
_CommonAgentMaxTraps_Object = MibScalar
commonAgentMaxTraps = _CommonAgentMaxTraps_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 3, 1, 3),
    _CommonAgentMaxTraps_Type()
)
commonAgentMaxTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonAgentMaxTraps.setStatus("mandatory")
_CommonAgentTrapMinInterval_Type = Integer32
_CommonAgentTrapMinInterval_Object = MibScalar
commonAgentTrapMinInterval = _CommonAgentTrapMinInterval_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 3, 1, 4),
    _CommonAgentTrapMinInterval_Type()
)
commonAgentTrapMinInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonAgentTrapMinInterval.setStatus("mandatory")
_CommonAgentTrapMaxInterval_Type = Integer32
_CommonAgentTrapMaxInterval_Object = MibScalar
commonAgentTrapMaxInterval = _CommonAgentTrapMaxInterval_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 3, 1, 5),
    _CommonAgentTrapMaxInterval_Type()
)
commonAgentTrapMaxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonAgentTrapMaxInterval.setStatus("mandatory")


class _CommonTrapAck_Type(OctetString):
    """Custom type commonTrapAck based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 255),
    )


_CommonTrapAck_Type.__name__ = "OctetString"
_CommonTrapAck_Object = MibScalar
commonTrapAck = _CommonTrapAck_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 3, 1, 6),
    _CommonTrapAck_Type()
)
commonTrapAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonTrapAck.setStatus("optional")
_CommonAgentTrapTable_Object = MibTable
commonAgentTrapTable = _CommonAgentTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 3, 1, 7)
)
if mibBuilder.loadTexts:
    commonAgentTrapTable.setStatus("mandatory")
_CommonAgentTrapEntry_Object = MibTableRow
commonAgentTrapEntry = _CommonAgentTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 3, 1, 7, 1)
)
commonAgentTrapEntry.setIndexNames(
    (0, "NSCRTV-ROOT", "commonAgentTrapIndex"),
)
if mibBuilder.loadTexts:
    commonAgentTrapEntry.setStatus("mandatory")
_CommonAgentTrapIndex_Type = Integer32
_CommonAgentTrapIndex_Object = MibTableColumn
commonAgentTrapIndex = _CommonAgentTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 3, 1, 7, 1, 1),
    _CommonAgentTrapIndex_Type()
)
commonAgentTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonAgentTrapIndex.setStatus("mandatory")
_CommonAgentTrapIP_Type = IpAddress
_CommonAgentTrapIP_Object = MibTableColumn
commonAgentTrapIP = _CommonAgentTrapIP_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 3, 1, 7, 1, 2),
    _CommonAgentTrapIP_Type()
)
commonAgentTrapIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonAgentTrapIP.setStatus("mandatory")


class _CommonAgentTrapCommunity_Type(DisplayString):
    """Custom type commonAgentTrapCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CommonAgentTrapCommunity_Type.__name__ = "DisplayString"
_CommonAgentTrapCommunity_Object = MibTableColumn
commonAgentTrapCommunity = _CommonAgentTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 3, 1, 7, 1, 3),
    _CommonAgentTrapCommunity_Type()
)
commonAgentTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonAgentTrapCommunity.setStatus("mandatory")


class _CommonAgentTrapStatus_Type(Integer32):
    """Custom type commonAgentTrapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("commonAgentTrapDisable", 2),
          ("commonAgentTrapEnable", 1))
    )


_CommonAgentTrapStatus_Type.__name__ = "Integer32"
_CommonAgentTrapStatus_Object = MibTableColumn
commonAgentTrapStatus = _CommonAgentTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 3, 1, 7, 1, 4),
    _CommonAgentTrapStatus_Type()
)
commonAgentTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonAgentTrapStatus.setStatus("mandatory")
_CommonDeviceGroup_ObjectIdentity = ObjectIdentity
commonDeviceGroup = _CommonDeviceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 3, 2)
)
_CommonDeviceNum_Type = Integer32
_CommonDeviceNum_Object = MibScalar
commonDeviceNum = _CommonDeviceNum_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 3, 2, 1),
    _CommonDeviceNum_Type()
)
commonDeviceNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonDeviceNum.setStatus("mandatory")
_CommonDeviceInfoTable_Object = MibTable
commonDeviceInfoTable = _CommonDeviceInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 3, 2, 2)
)
if mibBuilder.loadTexts:
    commonDeviceInfoTable.setStatus("mandatory")
_CommonDeviceInfoEntry_Object = MibTableRow
commonDeviceInfoEntry = _CommonDeviceInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 3, 2, 2, 1)
)
commonDeviceInfoEntry.setIndexNames(
    (0, "NSCRTV-ROOT", "commonDeviceSlot"),
)
if mibBuilder.loadTexts:
    commonDeviceInfoEntry.setStatus("mandatory")
_CommonDeviceSlot_Type = Integer32
_CommonDeviceSlot_Object = MibTableColumn
commonDeviceSlot = _CommonDeviceSlot_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 3, 2, 2, 1, 1),
    _CommonDeviceSlot_Type()
)
commonDeviceSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonDeviceSlot.setStatus("mandatory")


class _CommonDevicesID_Type(OctetString):
    """Custom type commonDevicesID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CommonDevicesID_Type.__name__ = "OctetString"
_CommonDevicesID_Object = MibTableColumn
commonDevicesID = _CommonDevicesID_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 3, 2, 2, 1, 2),
    _CommonDevicesID_Type()
)
commonDevicesID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonDevicesID.setStatus("mandatory")


class _CommonDeviceVendor_Type(DisplayString):
    """Custom type commonDeviceVendor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CommonDeviceVendor_Type.__name__ = "DisplayString"
_CommonDeviceVendor_Object = MibTableColumn
commonDeviceVendor = _CommonDeviceVendor_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 3, 2, 2, 1, 3),
    _CommonDeviceVendor_Type()
)
commonDeviceVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonDeviceVendor.setStatus("mandatory")


class _CommonDeviceModelNumber_Type(DisplayString):
    """Custom type commonDeviceModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CommonDeviceModelNumber_Type.__name__ = "DisplayString"
_CommonDeviceModelNumber_Object = MibTableColumn
commonDeviceModelNumber = _CommonDeviceModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 3, 2, 2, 1, 4),
    _CommonDeviceModelNumber_Type()
)
commonDeviceModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonDeviceModelNumber.setStatus("mandatory")


class _CommonDeviceSerialNumber_Type(DisplayString):
    """Custom type commonDeviceSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CommonDeviceSerialNumber_Type.__name__ = "DisplayString"
_CommonDeviceSerialNumber_Object = MibTableColumn
commonDeviceSerialNumber = _CommonDeviceSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 3, 2, 2, 1, 5),
    _CommonDeviceSerialNumber_Type()
)
commonDeviceSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonDeviceSerialNumber.setStatus("mandatory")


class _CommonDeviceVendorInfo_Type(DisplayString):
    """Custom type commonDeviceVendorInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CommonDeviceVendorInfo_Type.__name__ = "DisplayString"
_CommonDeviceVendorInfo_Object = MibTableColumn
commonDeviceVendorInfo = _CommonDeviceVendorInfo_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 3, 2, 2, 1, 6),
    _CommonDeviceVendorInfo_Type()
)
commonDeviceVendorInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonDeviceVendorInfo.setStatus("optional")


class _CommonDeviceStatus_Type(OctetString):
    """Custom type commonDeviceStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_CommonDeviceStatus_Type.__name__ = "OctetString"
_CommonDeviceStatus_Object = MibTableColumn
commonDeviceStatus = _CommonDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 3, 2, 2, 1, 7),
    _CommonDeviceStatus_Type()
)
commonDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonDeviceStatus.setStatus("mandatory")


class _CommonDeviceReset_Type(Integer32):
    """Custom type commonDeviceReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_CommonDeviceReset_Type.__name__ = "Integer32"
_CommonDeviceReset_Object = MibTableColumn
commonDeviceReset = _CommonDeviceReset_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 3, 2, 2, 1, 8),
    _CommonDeviceReset_Type()
)
commonDeviceReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonDeviceReset.setStatus("mandatory")


class _CommonDeviceAlarmDetectionControl_Type(Integer32):
    """Custom type commonDeviceAlarmDetectionControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("detectionDisabled", 1),
          ("detectionEnabled", 2),
          ("detectionEnabledAndRegenerate", 3))
    )


_CommonDeviceAlarmDetectionControl_Type.__name__ = "Integer32"
_CommonDeviceAlarmDetectionControl_Object = MibTableColumn
commonDeviceAlarmDetectionControl = _CommonDeviceAlarmDetectionControl_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 3, 2, 2, 1, 9),
    _CommonDeviceAlarmDetectionControl_Type()
)
commonDeviceAlarmDetectionControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commonDeviceAlarmDetectionControl.setStatus("mandatory")
_CommonDeviceMACAddress_Type = IpAddress
_CommonDeviceMACAddress_Object = MibTableColumn
commonDeviceMACAddress = _CommonDeviceMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 3, 2, 2, 1, 10),
    _CommonDeviceMACAddress_Type()
)
commonDeviceMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonDeviceMACAddress.setStatus("mandatory")


class _CommonDeviceTamperStatus_Type(Integer32):
    """Custom type commonDeviceTamperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("compromised", 2),
          ("intact", 1))
    )


_CommonDeviceTamperStatus_Type.__name__ = "Integer32"
_CommonDeviceTamperStatus_Object = MibTableColumn
commonDeviceTamperStatus = _CommonDeviceTamperStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 3, 2, 2, 1, 11),
    _CommonDeviceTamperStatus_Type()
)
commonDeviceTamperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonDeviceTamperStatus.setStatus("optional")


class _CommonDeviceInternalTemperature_Type(Integer32):
    """Custom type commonDeviceInternalTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_CommonDeviceInternalTemperature_Type.__name__ = "Integer32"
_CommonDeviceInternalTemperature_Object = MibTableColumn
commonDeviceInternalTemperature = _CommonDeviceInternalTemperature_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 3, 2, 2, 1, 12),
    _CommonDeviceInternalTemperature_Type()
)
commonDeviceInternalTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonDeviceInternalTemperature.setStatus("optional")


class _CommonDeviceResetCause_Type(Integer32):
    """Custom type commonDeviceResetCause based on Integer32"""
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
        *(("command", 3),
          ("craft", 5),
          ("other", 1),
          ("powerup", 2),
          ("watchdog", 4))
    )


_CommonDeviceResetCause_Type.__name__ = "Integer32"
_CommonDeviceResetCause_Object = MibTableColumn
commonDeviceResetCause = _CommonDeviceResetCause_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 3, 2, 2, 1, 13),
    _CommonDeviceResetCause_Type()
)
commonDeviceResetCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonDeviceResetCause.setStatus("mandatory")


class _CommonDeviceCraftStatus_Type(Integer32):
    """Custom type commonDeviceCraftStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 2),
          ("disconnected", 1))
    )


_CommonDeviceCraftStatus_Type.__name__ = "Integer32"
_CommonDeviceCraftStatus_Object = MibTableColumn
commonDeviceCraftStatus = _CommonDeviceCraftStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 3, 2, 2, 1, 14),
    _CommonDeviceCraftStatus_Type()
)
commonDeviceCraftStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonDeviceCraftStatus.setStatus("mandatory")
_CommonDevicesOID_Type = ObjectIdentifier
_CommonDevicesOID_Object = MibTableColumn
commonDevicesOID = _CommonDevicesOID_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 3, 2, 2, 1, 15),
    _CommonDevicesOID_Type()
)
commonDevicesOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonDevicesOID.setStatus("mandatory")
_CommonDeviceAcct_Type = Counter32
_CommonDeviceAcct_Object = MibTableColumn
commonDeviceAcct = _CommonDeviceAcct_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 3, 2, 2, 1, 16),
    _CommonDeviceAcct_Type()
)
commonDeviceAcct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonDeviceAcct.setStatus("optional")


class _CommonDeviceName_Type(DisplayString):
    """Custom type commonDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CommonDeviceName_Type.__name__ = "DisplayString"
_CommonDeviceName_Object = MibTableColumn
commonDeviceName = _CommonDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 3, 2, 2, 1, 17),
    _CommonDeviceName_Type()
)
commonDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonDeviceName.setStatus("mandatory")


class _CommonDeviceMFD_Type(DisplayString):
    """Custom type commonDeviceMFD based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_CommonDeviceMFD_Type.__name__ = "DisplayString"
_CommonDeviceMFD_Object = MibTableColumn
commonDeviceMFD = _CommonDeviceMFD_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 3, 2, 2, 1, 18),
    _CommonDeviceMFD_Type()
)
commonDeviceMFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonDeviceMFD.setStatus("mandatory")


class _CommonDeviceFW_Type(DisplayString):
    """Custom type commonDeviceFW based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CommonDeviceFW_Type.__name__ = "DisplayString"
_CommonDeviceFW_Object = MibTableColumn
commonDeviceFW = _CommonDeviceFW_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 3, 3, 2, 2, 1, 19),
    _CommonDeviceFW_Type()
)
commonDeviceFW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commonDeviceFW.setStatus("mandatory")
_OaIdent_ObjectIdentity = ObjectIdentity
oaIdent = _OaIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 1, 11)
)
_OaVendorOID_Type = ObjectIdentifier
_OaVendorOID_Object = MibScalar
oaVendorOID = _OaVendorOID_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 11, 1),
    _OaVendorOID_Type()
)
oaVendorOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaVendorOID.setStatus("optional")


class _OaOutputOpticalPower_Type(Integer32):
    """Custom type oaOutputOpticalPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OaOutputOpticalPower_Type.__name__ = "Integer32"
_OaOutputOpticalPower_Object = MibScalar
oaOutputOpticalPower = _OaOutputOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 11, 2),
    _OaOutputOpticalPower_Type()
)
oaOutputOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaOutputOpticalPower.setStatus("mandatory")


class _OaInputOpticalPower_Type(Integer32):
    """Custom type oaInputOpticalPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_OaInputOpticalPower_Type.__name__ = "Integer32"
_OaInputOpticalPower_Object = MibScalar
oaInputOpticalPower = _OaInputOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 11, 3),
    _OaInputOpticalPower_Type()
)
oaInputOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaInputOpticalPower.setStatus("mandatory")
_OaPumpTable_Object = MibTable
oaPumpTable = _OaPumpTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 11, 4)
)
if mibBuilder.loadTexts:
    oaPumpTable.setStatus("mandatory")
_OaPumpEntry_Object = MibTableRow
oaPumpEntry = _OaPumpEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 11, 4, 1)
)
oaPumpEntry.setIndexNames(
    (0, "NSCRTV-ROOT", "oaPumpIndex"),
)
if mibBuilder.loadTexts:
    oaPumpEntry.setStatus("mandatory")
_OaPumpIndex_Type = Integer32
_OaPumpIndex_Object = MibTableColumn
oaPumpIndex = _OaPumpIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 11, 4, 1, 1),
    _OaPumpIndex_Type()
)
oaPumpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaPumpIndex.setStatus("mandatory")


class _OaPumpBIAS_Type(Integer32):
    """Custom type oaPumpBIAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OaPumpBIAS_Type.__name__ = "Integer32"
_OaPumpBIAS_Object = MibTableColumn
oaPumpBIAS = _OaPumpBIAS_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 11, 4, 1, 2),
    _OaPumpBIAS_Type()
)
oaPumpBIAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaPumpBIAS.setStatus("mandatory")


class _OaPumpTEC_Type(Integer32):
    """Custom type oaPumpTEC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_OaPumpTEC_Type.__name__ = "Integer32"
_OaPumpTEC_Object = MibTableColumn
oaPumpTEC = _OaPumpTEC_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 11, 4, 1, 3),
    _OaPumpTEC_Type()
)
oaPumpTEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaPumpTEC.setStatus("optional")


class _OaPumpTemp_Type(Integer32):
    """Custom type oaPumpTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32768),
    )


_OaPumpTemp_Type.__name__ = "Integer32"
_OaPumpTemp_Object = MibTableColumn
oaPumpTemp = _OaPumpTemp_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 11, 4, 1, 4),
    _OaPumpTemp_Type()
)
oaPumpTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaPumpTemp.setStatus("mandatory")


class _OaNumberDCPowerSupply_Type(Integer32):
    """Custom type oaNumberDCPowerSupply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_OaNumberDCPowerSupply_Type.__name__ = "Integer32"
_OaNumberDCPowerSupply_Object = MibScalar
oaNumberDCPowerSupply = _OaNumberDCPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 11, 5),
    _OaNumberDCPowerSupply_Type()
)
oaNumberDCPowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaNumberDCPowerSupply.setStatus("mandatory")


class _OaDCPowerSupplyMode_Type(Integer32):
    """Custom type oaDCPowerSupplyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aloneSupply", 3),
          ("loadsharing", 1),
          ("switchedRedundant", 2))
    )


_OaDCPowerSupplyMode_Type.__name__ = "Integer32"
_OaDCPowerSupplyMode_Object = MibScalar
oaDCPowerSupplyMode = _OaDCPowerSupplyMode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 11, 6),
    _OaDCPowerSupplyMode_Type()
)
oaDCPowerSupplyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDCPowerSupplyMode.setStatus("optional")
_OaDCPowerTable_Object = MibTable
oaDCPowerTable = _OaDCPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 11, 7)
)
if mibBuilder.loadTexts:
    oaDCPowerTable.setStatus("mandatory")
_OaDCPowerEntry_Object = MibTableRow
oaDCPowerEntry = _OaDCPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 11, 7, 1)
)
oaDCPowerEntry.setIndexNames(
    (0, "NSCRTV-ROOT", "oaDCPowerIndex"),
)
if mibBuilder.loadTexts:
    oaDCPowerEntry.setStatus("mandatory")
_OaDCPowerIndex_Type = Integer32
_OaDCPowerIndex_Object = MibTableColumn
oaDCPowerIndex = _OaDCPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 11, 7, 1, 1),
    _OaDCPowerIndex_Type()
)
oaDCPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDCPowerIndex.setStatus("mandatory")


class _OaDCPowerVoltage_Type(Integer32):
    """Custom type oaDCPowerVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_OaDCPowerVoltage_Type.__name__ = "Integer32"
_OaDCPowerVoltage_Object = MibTableColumn
oaDCPowerVoltage = _OaDCPowerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 11, 7, 1, 2),
    _OaDCPowerVoltage_Type()
)
oaDCPowerVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDCPowerVoltage.setStatus("mandatory")


class _OaDCPowerCurrent_Type(Integer32):
    """Custom type oaDCPowerCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OaDCPowerCurrent_Type.__name__ = "Integer32"
_OaDCPowerCurrent_Object = MibTableColumn
oaDCPowerCurrent = _OaDCPowerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 11, 7, 1, 3),
    _OaDCPowerCurrent_Type()
)
oaDCPowerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDCPowerCurrent.setStatus("mandatory")
_OaDCPowerName_Type = DisplayString
_OaDCPowerName_Object = MibTableColumn
oaDCPowerName = _OaDCPowerName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 11, 7, 1, 4),
    _OaDCPowerName_Type()
)
oaDCPowerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDCPowerName.setStatus("mandatory")


class _OaOutputOpticalPowerSet_Type(Integer32):
    """Custom type oaOutputOpticalPowerSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OaOutputOpticalPowerSet_Type.__name__ = "Integer32"
_OaOutputOpticalPowerSet_Object = MibScalar
oaOutputOpticalPowerSet = _OaOutputOpticalPowerSet_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 11, 11),
    _OaOutputOpticalPowerSet_Type()
)
oaOutputOpticalPowerSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaOutputOpticalPowerSet.setStatus("mandatory")


class _OaGainSet_Type(Integer32):
    """Custom type oaGainSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OaGainSet_Type.__name__ = "Integer32"
_OaGainSet_Object = MibScalar
oaGainSet = _OaGainSet_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 11, 12),
    _OaGainSet_Type()
)
oaGainSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaGainSet.setStatus("mandatory")


class _PowerSupplyStatusA_Type(Integer32):
    """Custom type powerSupplyStatusA based on Integer32"""
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
        *(("failure", 2),
          ("nominal", 1),
          ("notInstalled", 3),
          ("undefined", 0))
    )


_PowerSupplyStatusA_Type.__name__ = "Integer32"
_PowerSupplyStatusA_Object = MibScalar
powerSupplyStatusA = _PowerSupplyStatusA_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 11, 32),
    _PowerSupplyStatusA_Type()
)
powerSupplyStatusA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyStatusA.setStatus("current")
if mibBuilder.loadTexts:
    powerSupplyStatusA.setUnits("no units")


class _PowerSupplyStatusB_Type(Integer32):
    """Custom type powerSupplyStatusB based on Integer32"""
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
        *(("failure", 2),
          ("nominal", 1),
          ("notInstalled", 3),
          ("undefined", 0))
    )


_PowerSupplyStatusB_Type.__name__ = "Integer32"
_PowerSupplyStatusB_Object = MibScalar
powerSupplyStatusB = _PowerSupplyStatusB_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 11, 33),
    _PowerSupplyStatusB_Type()
)
powerSupplyStatusB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyStatusB.setStatus("current")
if mibBuilder.loadTexts:
    powerSupplyStatusB.setUnits("no units")

# Managed Objects groups


# Notification objects

hfcColdStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 17409, 1, 0, 0)
)
hfcColdStart.setObjects(
      *(("NSCRTV-ROOT", "commonPhysAddress"),
        ("NSCRTV-ROOT", "commonNELogicalID"))
)
if mibBuilder.loadTexts:
    hfcColdStart.setStatus(
        ""
    )

hfcAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 17409, 1, 0, 1)
)
hfcAlarmEvent.setObjects(
      *(("NSCRTV-ROOT", "commonPhysAddress"),
        ("NSCRTV-ROOT", "commonNELogicalID"),
        ("NSCRTV-ROOT", "alarmLogInformation"),
        ("NSCRTV-ROOT", "alarmText"))
)
if mibBuilder.loadTexts:
    hfcAlarmEvent.setStatus(
        ""
    )

hfcWarmStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 17409, 1, 0, 2)
)
hfcWarmStart.setObjects(
      *(("NSCRTV-ROOT", "commonPhysAddress"),
        ("NSCRTV-ROOT", "commonNELogicalID"))
)
if mibBuilder.loadTexts:
    hfcWarmStart.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NSCRTV-ROOT",
    **{"nscrtvRoot": nscrtvRoot,
       "nscrtvHFCemsTree": nscrtvHFCemsTree,
       "hfcColdStart": hfcColdStart,
       "hfcAlarmEvent": hfcAlarmEvent,
       "hfcWarmStart": hfcWarmStart,
       "propertyIdent": propertyIdent,
       "analogPropertyTable": analogPropertyTable,
       "analogPropertyEntry": analogPropertyEntry,
       "analogParameterOID": analogParameterOID,
       "alarmEnable": alarmEnable,
       "analogAlarmState": analogAlarmState,
       "analogAlarmHIHI": analogAlarmHIHI,
       "analogAlarmHI": analogAlarmHI,
       "analogAlarmLO": analogAlarmLO,
       "analogAlarmLOLO": analogAlarmLOLO,
       "analogAlarmDeadband": analogAlarmDeadband,
       "discretePropertyTable": discretePropertyTable,
       "discretePropertyEntry": discretePropertyEntry,
       "discreteParameterOID": discreteParameterOID,
       "discreteAlarmValue": discreteAlarmValue,
       "discreteAlarmEnable": discreteAlarmEnable,
       "discreteAlarmState": discreteAlarmState,
       "currentAlarmTable": currentAlarmTable,
       "currentAlarmEntry": currentAlarmEntry,
       "currentAlarmOID": currentAlarmOID,
       "currentAlarmState": currentAlarmState,
       "currentAlarmValue": currentAlarmValue,
       "alarmsIdent": alarmsIdent,
       "alarmLogNumberOfEntries": alarmLogNumberOfEntries,
       "alarmLogLastIndex": alarmLogLastIndex,
       "alarmLogTable": alarmLogTable,
       "alarmLogEntry": alarmLogEntry,
       "alarmLogIndex": alarmLogIndex,
       "alarmLogInformation": alarmLogInformation,
       "alarmText": alarmText,
       "commonIdent": commonIdent,
       "commonAdminGroup": commonAdminGroup,
       "commonNELogicalID": commonNELogicalID,
       "commonNEVendor": commonNEVendor,
       "commonNEModelNumber": commonNEModelNumber,
       "commonNESerialNumber": commonNESerialNumber,
       "commonNEVendorInfo": commonNEVendorInfo,
       "commonNEStatus": commonNEStatus,
       "commonReset": commonReset,
       "commonAlarmDetectionControl": commonAlarmDetectionControl,
       "commonNetworkAddress": commonNetworkAddress,
       "commonCheckCode": commonCheckCode,
       "commonTrapCommunityString": commonTrapCommunityString,
       "commonTamperStatus": commonTamperStatus,
       "commonInternalTemperature": commonInternalTemperature,
       "commonTime": commonTime,
       "commonVarBindings": commonVarBindings,
       "commonResetCause": commonResetCause,
       "commonCraftStatus": commonCraftStatus,
       "commonDeviceOID": commonDeviceOID,
       "commonDeviceId": commonDeviceId,
       "commondownload": commondownload,
       "commonAdminUseRf": commonAdminUseRf,
       "commonMACGroup": commonMACGroup,
       "commonMacAddress": commonMacAddress,
       "commonPhysAddress": commonPhysAddress,
       "commonMaxMulticastAddresses": commonMaxMulticastAddresses,
       "commonMulticastAddressTable": commonMulticastAddressTable,
       "commonMulticastAddressEntry": commonMulticastAddressEntry,
       "commonMulticastAddressIndex": commonMulticastAddressIndex,
       "commonMulticastAddressNumber": commonMulticastAddressNumber,
       "commonBackoffParams": commonBackoffParams,
       "commonBackoffPeriod": commonBackoffPeriod,
       "commonACKTimeoutWindow": commonACKTimeoutWindow,
       "commonMaximumMACLayerRetries": commonMaximumMACLayerRetries,
       "commonMaxPayloadSize": commonMaxPayloadSize,
       "commonBackoffMinimumExponent": commonBackoffMinimumExponent,
       "commonBackoffMaximumExponent": commonBackoffMaximumExponent,
       "commonMacStats": commonMacStats,
       "commonForwardPathLOSEvents": commonForwardPathLOSEvents,
       "commonForwardPathFramingErrors": commonForwardPathFramingErrors,
       "commonForwardPathCRCErrors": commonForwardPathCRCErrors,
       "commonInvalidMacCmds": commonInvalidMacCmds,
       "commonBackwardPathCollisionTimes": commonBackwardPathCollisionTimes,
       "commonRfGroup": commonRfGroup,
       "commonReturnPathFrequency": commonReturnPathFrequency,
       "commonForwardPathFrequency": commonForwardPathFrequency,
       "commonProvisionedReturnPowerLevel": commonProvisionedReturnPowerLevel,
       "commonForwardPathReceiveLevel": commonForwardPathReceiveLevel,
       "commonMaxReturnPower": commonMaxReturnPower,
       "commonAdminUseEthernet": commonAdminUseEthernet,
       "commonAgentGroup": commonAgentGroup,
       "commonAgentBootWay": commonAgentBootWay,
       "commonAgentReset": commonAgentReset,
       "commonAgentMaxTraps": commonAgentMaxTraps,
       "commonAgentTrapMinInterval": commonAgentTrapMinInterval,
       "commonAgentTrapMaxInterval": commonAgentTrapMaxInterval,
       "commonTrapAck": commonTrapAck,
       "commonAgentTrapTable": commonAgentTrapTable,
       "commonAgentTrapEntry": commonAgentTrapEntry,
       "commonAgentTrapIndex": commonAgentTrapIndex,
       "commonAgentTrapIP": commonAgentTrapIP,
       "commonAgentTrapCommunity": commonAgentTrapCommunity,
       "commonAgentTrapStatus": commonAgentTrapStatus,
       "commonDeviceGroup": commonDeviceGroup,
       "commonDeviceNum": commonDeviceNum,
       "commonDeviceInfoTable": commonDeviceInfoTable,
       "commonDeviceInfoEntry": commonDeviceInfoEntry,
       "commonDeviceSlot": commonDeviceSlot,
       "commonDevicesID": commonDevicesID,
       "commonDeviceVendor": commonDeviceVendor,
       "commonDeviceModelNumber": commonDeviceModelNumber,
       "commonDeviceSerialNumber": commonDeviceSerialNumber,
       "commonDeviceVendorInfo": commonDeviceVendorInfo,
       "commonDeviceStatus": commonDeviceStatus,
       "commonDeviceReset": commonDeviceReset,
       "commonDeviceAlarmDetectionControl": commonDeviceAlarmDetectionControl,
       "commonDeviceMACAddress": commonDeviceMACAddress,
       "commonDeviceTamperStatus": commonDeviceTamperStatus,
       "commonDeviceInternalTemperature": commonDeviceInternalTemperature,
       "commonDeviceResetCause": commonDeviceResetCause,
       "commonDeviceCraftStatus": commonDeviceCraftStatus,
       "commonDevicesOID": commonDevicesOID,
       "commonDeviceAcct": commonDeviceAcct,
       "commonDeviceName": commonDeviceName,
       "commonDeviceMFD": commonDeviceMFD,
       "commonDeviceFW": commonDeviceFW,
       "oaIdent": oaIdent,
       "oaVendorOID": oaVendorOID,
       "oaOutputOpticalPower": oaOutputOpticalPower,
       "oaInputOpticalPower": oaInputOpticalPower,
       "oaPumpTable": oaPumpTable,
       "oaPumpEntry": oaPumpEntry,
       "oaPumpIndex": oaPumpIndex,
       "oaPumpBIAS": oaPumpBIAS,
       "oaPumpTEC": oaPumpTEC,
       "oaPumpTemp": oaPumpTemp,
       "oaNumberDCPowerSupply": oaNumberDCPowerSupply,
       "oaDCPowerSupplyMode": oaDCPowerSupplyMode,
       "oaDCPowerTable": oaDCPowerTable,
       "oaDCPowerEntry": oaDCPowerEntry,
       "oaDCPowerIndex": oaDCPowerIndex,
       "oaDCPowerVoltage": oaDCPowerVoltage,
       "oaDCPowerCurrent": oaDCPowerCurrent,
       "oaDCPowerName": oaDCPowerName,
       "oaOutputOpticalPowerSet": oaOutputOpticalPowerSet,
       "oaGainSet": oaGainSet,
       "powerSupplyStatusA": powerSupplyStatusA,
       "powerSupplyStatusB": powerSupplyStatusB}
)
