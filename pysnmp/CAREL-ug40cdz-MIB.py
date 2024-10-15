# SNMP MIB module (CAREL-ug40cdz-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CAREL-ug40cdz-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:35 2024
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
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysContact,
 sysLocation,
 sysName) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysContact",
    "sysLocation",
    "sysName")

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

ug40cdzMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1)
)
ug40cdzMIB.setRevisions(
        ("2006-04-11 16:45",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Carel_ObjectIdentity = ObjectIdentity
carel = _Carel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839)
)
_Systm_ObjectIdentity = ObjectIdentity
systm = _Systm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 1)
)
_AgentRelease_Type = Integer32
_AgentRelease_Object = MibScalar
agentRelease = _AgentRelease_Object(
    (1, 3, 6, 1, 4, 1, 9839, 1, 1),
    _AgentRelease_Type()
)
agentRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRelease.setStatus("current")
if mibBuilder.loadTexts:
    agentRelease.setUnits("N/A")
_AgentCode_Type = Integer32
_AgentCode_Object = MibScalar
agentCode = _AgentCode_Object(
    (1, 3, 6, 1, 4, 1, 9839, 1, 2),
    _AgentCode_Type()
)
agentCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCode.setStatus("current")
if mibBuilder.loadTexts:
    agentCode.setUnits("N/A")
_Instruments_ObjectIdentity = ObjectIdentity
instruments = _Instruments_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2)
)
_WebGateInfo_ObjectIdentity = ObjectIdentity
webGateInfo = _WebGateInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 0)
)
_AgentParameters_ObjectIdentity = ObjectIdentity
agentParameters = _AgentParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 0, 1)
)


class _NetSize_Type(Integer32):
    """Custom type netSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_NetSize_Type.__name__ = "Integer32"
_NetSize_Object = MibScalar
netSize = _NetSize_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 0, 1, 1),
    _NetSize_Type()
)
netSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netSize.setStatus("current")
if mibBuilder.loadTexts:
    netSize.setUnits("N/A")


class _BaudRate_Type(Integer32):
    """Custom type baudRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1200, 1200),
        ValueRangeConstraint(2400, 2400),
        ValueRangeConstraint(4800, 4800),
        ValueRangeConstraint(9600, 9600),
        ValueRangeConstraint(19200, 19200),
    )


_BaudRate_Type.__name__ = "Integer32"
_BaudRate_Object = MibScalar
baudRate = _BaudRate_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 0, 1, 2),
    _BaudRate_Type()
)
baudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baudRate.setStatus("current")
if mibBuilder.loadTexts:
    baudRate.setUnits("N/A")
_UnitTypeGroup_ObjectIdentity = ObjectIdentity
unitTypeGroup = _UnitTypeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 0, 2)
)
_Unit1_Type_Type = DisplayString
_Unit1_Type_Object = MibScalar
unit1_Type = _Unit1_Type_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 0, 2, 1),
    _Unit1_Type_Type()
)
unit1_Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1_Type.setStatus("current")
if mibBuilder.loadTexts:
    unit1_Type.setUnits("N/A")
_UnitCodeGroup_ObjectIdentity = ObjectIdentity
unitCodeGroup = _UnitCodeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 0, 3)
)
_Unit1_Code_Type = Integer32
_Unit1_Code_Object = MibScalar
unit1_Code = _Unit1_Code_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 0, 3, 1),
    _Unit1_Code_Type()
)
unit1_Code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1_Code.setStatus("current")
if mibBuilder.loadTexts:
    unit1_Code.setUnits("N/A")
_UnitSoftwareReleaseGroup_ObjectIdentity = ObjectIdentity
unitSoftwareReleaseGroup = _UnitSoftwareReleaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 0, 4)
)
_Unit1_SoftwareRelease_Type = Integer32
_Unit1_SoftwareRelease_Object = MibScalar
unit1_SoftwareRelease = _Unit1_SoftwareRelease_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 0, 4, 1),
    _Unit1_SoftwareRelease_Type()
)
unit1_SoftwareRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1_SoftwareRelease.setStatus("current")
if mibBuilder.loadTexts:
    unit1_SoftwareRelease.setUnits("N/A")
_UnitMinSoftwareReleaseGroup_ObjectIdentity = ObjectIdentity
unitMinSoftwareReleaseGroup = _UnitMinSoftwareReleaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 0, 5)
)
_Unit1_MinSoftwareRelease_Type = Integer32
_Unit1_MinSoftwareRelease_Object = MibScalar
unit1_MinSoftwareRelease = _Unit1_MinSoftwareRelease_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 0, 5, 1),
    _Unit1_MinSoftwareRelease_Type()
)
unit1_MinSoftwareRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1_MinSoftwareRelease.setStatus("current")
if mibBuilder.loadTexts:
    unit1_MinSoftwareRelease.setUnits("N/A")
_UnitMaxSoftwareReleaseGroup_ObjectIdentity = ObjectIdentity
unitMaxSoftwareReleaseGroup = _UnitMaxSoftwareReleaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 0, 6)
)
_Unit1_MaxSoftwareRelease_Type = Integer32
_Unit1_MaxSoftwareRelease_Object = MibScalar
unit1_MaxSoftwareRelease = _Unit1_MaxSoftwareRelease_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 0, 6, 1),
    _Unit1_MaxSoftwareRelease_Type()
)
unit1_MaxSoftwareRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1_MaxSoftwareRelease.setStatus("current")
if mibBuilder.loadTexts:
    unit1_MaxSoftwareRelease.setUnits("N/A")
_UnitNoAnswerCounterGroup_ObjectIdentity = ObjectIdentity
unitNoAnswerCounterGroup = _UnitNoAnswerCounterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 0, 7)
)
_Unit1_NoAnswerCounter_Type = Integer32
_Unit1_NoAnswerCounter_Object = MibScalar
unit1_NoAnswerCounter = _Unit1_NoAnswerCounter_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 0, 7, 1),
    _Unit1_NoAnswerCounter_Type()
)
unit1_NoAnswerCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1_NoAnswerCounter.setStatus("current")
if mibBuilder.loadTexts:
    unit1_NoAnswerCounter.setUnits("N/A")
_UnitErrorChecksumCounterGroup_ObjectIdentity = ObjectIdentity
unitErrorChecksumCounterGroup = _UnitErrorChecksumCounterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 0, 8)
)
_Unit1_ErrorChecksumCounter_Type = Integer32
_Unit1_ErrorChecksumCounter_Object = MibScalar
unit1_ErrorChecksumCounter = _Unit1_ErrorChecksumCounter_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 0, 8, 1),
    _Unit1_ErrorChecksumCounter_Type()
)
unit1_ErrorChecksumCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1_ErrorChecksumCounter.setStatus("current")
if mibBuilder.loadTexts:
    unit1_ErrorChecksumCounter.setUnits("N/A")
_UnitTimeoutCounterGroup_ObjectIdentity = ObjectIdentity
unitTimeoutCounterGroup = _UnitTimeoutCounterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 0, 9)
)
_Unit1_TimeoutCounter_Type = Integer32
_Unit1_TimeoutCounter_Object = MibScalar
unit1_TimeoutCounter = _Unit1_TimeoutCounter_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 0, 9, 1),
    _Unit1_TimeoutCounter_Type()
)
unit1_TimeoutCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1_TimeoutCounter.setStatus("current")
if mibBuilder.loadTexts:
    unit1_TimeoutCounter.setUnits("N/A")
_DigitalObjects_ObjectIdentity = ObjectIdentity
digitalObjects = _DigitalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1)
)


class _SystemOn_Type(Integer32):
    """Custom type systemOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SystemOn_Type.__name__ = "Integer32"
_SystemOn_Object = MibScalar
systemOn = _SystemOn_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 1),
    _SystemOn_Type()
)
systemOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemOn.setStatus("current")
if mibBuilder.loadTexts:
    systemOn.setUnits("N/A")


class _Compressore1_Type(Integer32):
    """Custom type compressore1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Compressore1_Type.__name__ = "Integer32"
_Compressore1_Object = MibScalar
compressore1 = _Compressore1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 2),
    _Compressore1_Type()
)
compressore1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compressore1.setStatus("current")
if mibBuilder.loadTexts:
    compressore1.setUnits("N/A")


class _Compressore2_Type(Integer32):
    """Custom type compressore2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Compressore2_Type.__name__ = "Integer32"
_Compressore2_Object = MibScalar
compressore2 = _Compressore2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 3),
    _Compressore2_Type()
)
compressore2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compressore2.setStatus("current")
if mibBuilder.loadTexts:
    compressore2.setUnits("N/A")


class _Compressore3_Type(Integer32):
    """Custom type compressore3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Compressore3_Type.__name__ = "Integer32"
_Compressore3_Object = MibScalar
compressore3 = _Compressore3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 4),
    _Compressore3_Type()
)
compressore3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compressore3.setStatus("current")
if mibBuilder.loadTexts:
    compressore3.setUnits("N/A")


class _Compressore4_Type(Integer32):
    """Custom type compressore4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Compressore4_Type.__name__ = "Integer32"
_Compressore4_Object = MibScalar
compressore4 = _Compressore4_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 5),
    _Compressore4_Type()
)
compressore4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compressore4.setStatus("current")
if mibBuilder.loadTexts:
    compressore4.setUnits("N/A")


class _Heating1_Type(Integer32):
    """Custom type heating1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Heating1_Type.__name__ = "Integer32"
_Heating1_Object = MibScalar
heating1 = _Heating1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 6),
    _Heating1_Type()
)
heating1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heating1.setStatus("current")
if mibBuilder.loadTexts:
    heating1.setUnits("N/A")


class _Heating2_Type(Integer32):
    """Custom type heating2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Heating2_Type.__name__ = "Integer32"
_Heating2_Object = MibScalar
heating2 = _Heating2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 7),
    _Heating2_Type()
)
heating2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heating2.setStatus("current")
if mibBuilder.loadTexts:
    heating2.setUnits("N/A")


class _HotGasCoil_Type(Integer32):
    """Custom type hotGasCoil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HotGasCoil_Type.__name__ = "Integer32"
_HotGasCoil_Object = MibScalar
hotGasCoil = _HotGasCoil_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 9),
    _HotGasCoil_Type()
)
hotGasCoil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hotGasCoil.setStatus("current")
if mibBuilder.loadTexts:
    hotGasCoil.setUnits("N/A")


class _Dehumidification_Type(Integer32):
    """Custom type dehumidification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Dehumidification_Type.__name__ = "Integer32"
_Dehumidification_Object = MibScalar
dehumidification = _Dehumidification_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 10),
    _Dehumidification_Type()
)
dehumidification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dehumidification.setStatus("current")
if mibBuilder.loadTexts:
    dehumidification.setUnits("N/A")


class _Humidification_Type(Integer32):
    """Custom type humidification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Humidification_Type.__name__ = "Integer32"
_Humidification_Object = MibScalar
humidification = _Humidification_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 11),
    _Humidification_Type()
)
humidification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidification.setStatus("current")
if mibBuilder.loadTexts:
    humidification.setUnits("N/A")


class _Emerg_Type(Integer32):
    """Custom type emerg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Emerg_Type.__name__ = "Integer32"
_Emerg_Object = MibScalar
emerg = _Emerg_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 12),
    _Emerg_Type()
)
emerg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emerg.setStatus("current")
if mibBuilder.loadTexts:
    emerg.setUnits("N/A")


class _AlarmAccess_Type(Integer32):
    """Custom type alarmAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmAccess_Type.__name__ = "Integer32"
_AlarmAccess_Object = MibScalar
alarmAccess = _AlarmAccess_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 20),
    _AlarmAccess_Type()
)
alarmAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmAccess.setStatus("current")
if mibBuilder.loadTexts:
    alarmAccess.setUnits("N/A")


class _AlarmRoomHT_Type(Integer32):
    """Custom type alarmRoomHT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmRoomHT_Type.__name__ = "Integer32"
_AlarmRoomHT_Object = MibScalar
alarmRoomHT = _AlarmRoomHT_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 21),
    _AlarmRoomHT_Type()
)
alarmRoomHT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmRoomHT.setStatus("current")
if mibBuilder.loadTexts:
    alarmRoomHT.setUnits("N/A")


class _AlarmRoomLT_Type(Integer32):
    """Custom type alarmRoomLT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmRoomLT_Type.__name__ = "Integer32"
_AlarmRoomLT_Object = MibScalar
alarmRoomLT = _AlarmRoomLT_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 22),
    _AlarmRoomLT_Type()
)
alarmRoomLT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmRoomLT.setStatus("current")
if mibBuilder.loadTexts:
    alarmRoomLT.setUnits("N/A")


class _AlarmRoomHH_Type(Integer32):
    """Custom type alarmRoomHH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmRoomHH_Type.__name__ = "Integer32"
_AlarmRoomHH_Object = MibScalar
alarmRoomHH = _AlarmRoomHH_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 23),
    _AlarmRoomHH_Type()
)
alarmRoomHH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmRoomHH.setStatus("current")
if mibBuilder.loadTexts:
    alarmRoomHH.setUnits("N/A")


class _AlarmRoomLH_Type(Integer32):
    """Custom type alarmRoomLH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmRoomLH_Type.__name__ = "Integer32"
_AlarmRoomLH_Object = MibScalar
alarmRoomLH = _AlarmRoomLH_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 24),
    _AlarmRoomLH_Type()
)
alarmRoomLH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmRoomLH.setStatus("current")
if mibBuilder.loadTexts:
    alarmRoomLH.setUnits("N/A")


class _AlarmRoomEAP_Type(Integer32):
    """Custom type alarmRoomEAP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmRoomEAP_Type.__name__ = "Integer32"
_AlarmRoomEAP_Object = MibScalar
alarmRoomEAP = _AlarmRoomEAP_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 25),
    _AlarmRoomEAP_Type()
)
alarmRoomEAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmRoomEAP.setStatus("current")
if mibBuilder.loadTexts:
    alarmRoomEAP.setUnits("N/A")


class _AlarmFilter_Type(Integer32):
    """Custom type alarmFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmFilter_Type.__name__ = "Integer32"
_AlarmFilter_Object = MibScalar
alarmFilter = _AlarmFilter_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 26),
    _AlarmFilter_Type()
)
alarmFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmFilter.setStatus("current")
if mibBuilder.loadTexts:
    alarmFilter.setUnits("N/A")


class _AlarmFlood_Type(Integer32):
    """Custom type alarmFlood based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmFlood_Type.__name__ = "Integer32"
_AlarmFlood_Object = MibScalar
alarmFlood = _AlarmFlood_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 27),
    _AlarmFlood_Type()
)
alarmFlood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmFlood.setStatus("current")
if mibBuilder.loadTexts:
    alarmFlood.setUnits("N/A")


class _AlarmAirFlow_Type(Integer32):
    """Custom type alarmAirFlow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmAirFlow_Type.__name__ = "Integer32"
_AlarmAirFlow_Object = MibScalar
alarmAirFlow = _AlarmAirFlow_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 28),
    _AlarmAirFlow_Type()
)
alarmAirFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmAirFlow.setStatus("current")
if mibBuilder.loadTexts:
    alarmAirFlow.setUnits("N/A")


class _AlarmHeater_Type(Integer32):
    """Custom type alarmHeater based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmHeater_Type.__name__ = "Integer32"
_AlarmHeater_Object = MibScalar
alarmHeater = _AlarmHeater_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 29),
    _AlarmHeater_Type()
)
alarmHeater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmHeater.setStatus("current")
if mibBuilder.loadTexts:
    alarmHeater.setUnits("N/A")


class _AlarmHP1_Type(Integer32):
    """Custom type alarmHP1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmHP1_Type.__name__ = "Integer32"
_AlarmHP1_Object = MibScalar
alarmHP1 = _AlarmHP1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 30),
    _AlarmHP1_Type()
)
alarmHP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmHP1.setStatus("current")
if mibBuilder.loadTexts:
    alarmHP1.setUnits("N/A")


class _AlarmHP2_Type(Integer32):
    """Custom type alarmHP2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmHP2_Type.__name__ = "Integer32"
_AlarmHP2_Object = MibScalar
alarmHP2 = _AlarmHP2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 31),
    _AlarmHP2_Type()
)
alarmHP2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmHP2.setStatus("current")
if mibBuilder.loadTexts:
    alarmHP2.setUnits("N/A")


class _AlarmLP1_Type(Integer32):
    """Custom type alarmLP1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmLP1_Type.__name__ = "Integer32"
_AlarmLP1_Object = MibScalar
alarmLP1 = _AlarmLP1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 32),
    _AlarmLP1_Type()
)
alarmLP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLP1.setStatus("current")
if mibBuilder.loadTexts:
    alarmLP1.setUnits("N/A")


class _AlarmLP2_Type(Integer32):
    """Custom type alarmLP2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmLP2_Type.__name__ = "Integer32"
_AlarmLP2_Object = MibScalar
alarmLP2 = _AlarmLP2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 33),
    _AlarmLP2_Type()
)
alarmLP2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLP2.setStatus("current")
if mibBuilder.loadTexts:
    alarmLP2.setUnits("N/A")


class _AlarmEXV1_Type(Integer32):
    """Custom type alarmEXV1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmEXV1_Type.__name__ = "Integer32"
_AlarmEXV1_Object = MibScalar
alarmEXV1 = _AlarmEXV1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 34),
    _AlarmEXV1_Type()
)
alarmEXV1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmEXV1.setStatus("current")
if mibBuilder.loadTexts:
    alarmEXV1.setUnits("N/A")


class _AlarmEXV2_Type(Integer32):
    """Custom type alarmEXV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmEXV2_Type.__name__ = "Integer32"
_AlarmEXV2_Object = MibScalar
alarmEXV2 = _AlarmEXV2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 35),
    _AlarmEXV2_Type()
)
alarmEXV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmEXV2.setStatus("current")
if mibBuilder.loadTexts:
    alarmEXV2.setUnits("N/A")


class _AlarmPSE_Type(Integer32):
    """Custom type alarmPSE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmPSE_Type.__name__ = "Integer32"
_AlarmPSE_Object = MibScalar
alarmPSE = _AlarmPSE_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 36),
    _AlarmPSE_Type()
)
alarmPSE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmPSE.setStatus("current")
if mibBuilder.loadTexts:
    alarmPSE.setUnits("N/A")


class _AlarmSmokeFire_Type(Integer32):
    """Custom type alarmSmokeFire based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmSmokeFire_Type.__name__ = "Integer32"
_AlarmSmokeFire_Object = MibScalar
alarmSmokeFire = _AlarmSmokeFire_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 37),
    _AlarmSmokeFire_Type()
)
alarmSmokeFire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSmokeFire.setStatus("current")
if mibBuilder.loadTexts:
    alarmSmokeFire.setUnits("N/A")


class _AlarmLAN_Type(Integer32):
    """Custom type alarmLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmLAN_Type.__name__ = "Integer32"
_AlarmLAN_Object = MibScalar
alarmLAN = _AlarmLAN_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 38),
    _AlarmLAN_Type()
)
alarmLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLAN.setStatus("current")
if mibBuilder.loadTexts:
    alarmLAN.setUnits("N/A")


class _AlarmHUHC_Type(Integer32):
    """Custom type alarmHUHC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmHUHC_Type.__name__ = "Integer32"
_AlarmHUHC_Object = MibScalar
alarmHUHC = _AlarmHUHC_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 39),
    _AlarmHUHC_Type()
)
alarmHUHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmHUHC.setStatus("current")
if mibBuilder.loadTexts:
    alarmHUHC.setUnits("N/A")


class _AlarmHUPL_Type(Integer32):
    """Custom type alarmHUPL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmHUPL_Type.__name__ = "Integer32"
_AlarmHUPL_Object = MibScalar
alarmHUPL = _AlarmHUPL_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 40),
    _AlarmHUPL_Type()
)
alarmHUPL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmHUPL.setStatus("current")
if mibBuilder.loadTexts:
    alarmHUPL.setUnits("N/A")


class _AlarmHUWL_Type(Integer32):
    """Custom type alarmHUWL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmHUWL_Type.__name__ = "Integer32"
_AlarmHUWL_Object = MibScalar
alarmHUWL = _AlarmHUWL_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 41),
    _AlarmHUWL_Type()
)
alarmHUWL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmHUWL.setStatus("current")
if mibBuilder.loadTexts:
    alarmHUWL.setUnits("N/A")


class _AlarmCWDHT_Type(Integer32):
    """Custom type alarmCWDHT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmCWDHT_Type.__name__ = "Integer32"
_AlarmCWDHT_Object = MibScalar
alarmCWDHT = _AlarmCWDHT_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 42),
    _AlarmCWDHT_Type()
)
alarmCWDHT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCWDHT.setStatus("current")
if mibBuilder.loadTexts:
    alarmCWDHT.setUnits("N/A")


class _AlarmCWF_Type(Integer32):
    """Custom type alarmCWF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmCWF_Type.__name__ = "Integer32"
_AlarmCWF_Object = MibScalar
alarmCWF = _AlarmCWF_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 43),
    _AlarmCWF_Type()
)
alarmCWF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCWF.setStatus("current")
if mibBuilder.loadTexts:
    alarmCWF.setUnits("N/A")


class _AlarmCWFF_Type(Integer32):
    """Custom type alarmCWFF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmCWFF_Type.__name__ = "Integer32"
_AlarmCWFF_Object = MibScalar
alarmCWFF = _AlarmCWFF_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 44),
    _AlarmCWFF_Type()
)
alarmCWFF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCWFF.setStatus("current")
if mibBuilder.loadTexts:
    alarmCWFF.setUnits("N/A")


class _AlarmCWHT_Type(Integer32):
    """Custom type alarmCWHT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmCWHT_Type.__name__ = "Integer32"
_AlarmCWHT_Object = MibScalar
alarmCWHT = _AlarmCWHT_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 45),
    _AlarmCWHT_Type()
)
alarmCWHT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCWHT.setStatus("current")
if mibBuilder.loadTexts:
    alarmCWHT.setUnits("N/A")


class _AlarmRTS_Type(Integer32):
    """Custom type alarmRTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmRTS_Type.__name__ = "Integer32"
_AlarmRTS_Object = MibScalar
alarmRTS = _AlarmRTS_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 46),
    _AlarmRTS_Type()
)
alarmRTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmRTS.setStatus("current")
if mibBuilder.loadTexts:
    alarmRTS.setUnits("N/A")


class _AlarmHWS_Type(Integer32):
    """Custom type alarmHWS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmHWS_Type.__name__ = "Integer32"
_AlarmHWS_Object = MibScalar
alarmHWS = _AlarmHWS_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 47),
    _AlarmHWS_Type()
)
alarmHWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmHWS.setStatus("current")
if mibBuilder.loadTexts:
    alarmHWS.setUnits("N/A")


class _AlarmCWS_Type(Integer32):
    """Custom type alarmCWS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmCWS_Type.__name__ = "Integer32"
_AlarmCWS_Object = MibScalar
alarmCWS = _AlarmCWS_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 48),
    _AlarmCWS_Type()
)
alarmCWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCWS.setStatus("current")
if mibBuilder.loadTexts:
    alarmCWS.setUnits("N/A")


class _AlarmOTS_Type(Integer32):
    """Custom type alarmOTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmOTS_Type.__name__ = "Integer32"
_AlarmOTS_Object = MibScalar
alarmOTS = _AlarmOTS_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 49),
    _AlarmOTS_Type()
)
alarmOTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmOTS.setStatus("current")
if mibBuilder.loadTexts:
    alarmOTS.setUnits("N/A")


class _AlarmDTS_Type(Integer32):
    """Custom type alarmDTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmDTS_Type.__name__ = "Integer32"
_AlarmDTS_Object = MibScalar
alarmDTS = _AlarmDTS_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 50),
    _AlarmDTS_Type()
)
alarmDTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmDTS.setStatus("current")
if mibBuilder.loadTexts:
    alarmDTS.setUnits("N/A")


class _AlarmRHS_Type(Integer32):
    """Custom type alarmRHS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmRHS_Type.__name__ = "Integer32"
_AlarmRHS_Object = MibScalar
alarmRHS = _AlarmRHS_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 51),
    _AlarmRHS_Type()
)
alarmRHS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmRHS.setStatus("current")
if mibBuilder.loadTexts:
    alarmRHS.setUnits("N/A")


class _AlarmCWOTS_Type(Integer32):
    """Custom type alarmCWOTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmCWOTS_Type.__name__ = "Integer32"
_AlarmCWOTS_Object = MibScalar
alarmCWOTS = _AlarmCWOTS_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 52),
    _AlarmCWOTS_Type()
)
alarmCWOTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCWOTS.setStatus("current")
if mibBuilder.loadTexts:
    alarmCWOTS.setUnits("N/A")


class _AlarmC1Hours_Type(Integer32):
    """Custom type alarmC1Hours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmC1Hours_Type.__name__ = "Integer32"
_AlarmC1Hours_Object = MibScalar
alarmC1Hours = _AlarmC1Hours_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 53),
    _AlarmC1Hours_Type()
)
alarmC1Hours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmC1Hours.setStatus("current")
if mibBuilder.loadTexts:
    alarmC1Hours.setUnits("N/A")


class _AlarmC2Hours_Type(Integer32):
    """Custom type alarmC2Hours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmC2Hours_Type.__name__ = "Integer32"
_AlarmC2Hours_Object = MibScalar
alarmC2Hours = _AlarmC2Hours_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 54),
    _AlarmC2Hours_Type()
)
alarmC2Hours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmC2Hours.setStatus("current")
if mibBuilder.loadTexts:
    alarmC2Hours.setUnits("N/A")


class _AlarmC3Hours_Type(Integer32):
    """Custom type alarmC3Hours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmC3Hours_Type.__name__ = "Integer32"
_AlarmC3Hours_Object = MibScalar
alarmC3Hours = _AlarmC3Hours_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 55),
    _AlarmC3Hours_Type()
)
alarmC3Hours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmC3Hours.setStatus("current")
if mibBuilder.loadTexts:
    alarmC3Hours.setUnits("N/A")


class _AlarmC4Hours_Type(Integer32):
    """Custom type alarmC4Hours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmC4Hours_Type.__name__ = "Integer32"
_AlarmC4Hours_Object = MibScalar
alarmC4Hours = _AlarmC4Hours_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 56),
    _AlarmC4Hours_Type()
)
alarmC4Hours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmC4Hours.setStatus("current")
if mibBuilder.loadTexts:
    alarmC4Hours.setUnits("N/A")


class _AlarmFilterHours_Type(Integer32):
    """Custom type alarmFilterHours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmFilterHours_Type.__name__ = "Integer32"
_AlarmFilterHours_Object = MibScalar
alarmFilterHours = _AlarmFilterHours_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 57),
    _AlarmFilterHours_Type()
)
alarmFilterHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmFilterHours.setStatus("current")
if mibBuilder.loadTexts:
    alarmFilterHours.setUnits("N/A")


class _AlarmHeat1Hours_Type(Integer32):
    """Custom type alarmHeat1Hours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmHeat1Hours_Type.__name__ = "Integer32"
_AlarmHeat1Hours_Object = MibScalar
alarmHeat1Hours = _AlarmHeat1Hours_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 58),
    _AlarmHeat1Hours_Type()
)
alarmHeat1Hours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmHeat1Hours.setStatus("current")
if mibBuilder.loadTexts:
    alarmHeat1Hours.setUnits("N/A")


class _AlarmHeat2Hours_Type(Integer32):
    """Custom type alarmHeat2Hours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmHeat2Hours_Type.__name__ = "Integer32"
_AlarmHeat2Hours_Object = MibScalar
alarmHeat2Hours = _AlarmHeat2Hours_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 59),
    _AlarmHeat2Hours_Type()
)
alarmHeat2Hours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmHeat2Hours.setStatus("current")
if mibBuilder.loadTexts:
    alarmHeat2Hours.setUnits("N/A")


class _AlarmHumHours_Type(Integer32):
    """Custom type alarmHumHours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmHumHours_Type.__name__ = "Integer32"
_AlarmHumHours_Object = MibScalar
alarmHumHours = _AlarmHumHours_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 60),
    _AlarmHumHours_Type()
)
alarmHumHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmHumHours.setStatus("current")
if mibBuilder.loadTexts:
    alarmHumHours.setUnits("N/A")


class _AlarmUnitHours_Type(Integer32):
    """Custom type alarmUnitHours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmUnitHours_Type.__name__ = "Integer32"
_AlarmUnitHours_Object = MibScalar
alarmUnitHours = _AlarmUnitHours_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 61),
    _AlarmUnitHours_Type()
)
alarmUnitHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmUnitHours.setStatus("current")
if mibBuilder.loadTexts:
    alarmUnitHours.setUnits("N/A")


class _AlarmDI2_Type(Integer32):
    """Custom type alarmDI2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmDI2_Type.__name__ = "Integer32"
_AlarmDI2_Object = MibScalar
alarmDI2 = _AlarmDI2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 62),
    _AlarmDI2_Type()
)
alarmDI2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmDI2.setStatus("current")
if mibBuilder.loadTexts:
    alarmDI2.setUnits("N/A")


class _AlarmDI4_Type(Integer32):
    """Custom type alarmDI4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmDI4_Type.__name__ = "Integer32"
_AlarmDI4_Object = MibScalar
alarmDI4 = _AlarmDI4_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 63),
    _AlarmDI4_Type()
)
alarmDI4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmDI4.setStatus("current")
if mibBuilder.loadTexts:
    alarmDI4.setUnits("N/A")


class _AlarmDI6_Type(Integer32):
    """Custom type alarmDI6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmDI6_Type.__name__ = "Integer32"
_AlarmDI6_Object = MibScalar
alarmDI6 = _AlarmDI6_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 64),
    _AlarmDI6_Type()
)
alarmDI6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmDI6.setStatus("current")
if mibBuilder.loadTexts:
    alarmDI6.setUnits("N/A")


class _AlarmHum_Type(Integer32):
    """Custom type alarmHum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmHum_Type.__name__ = "Integer32"
_AlarmHum_Object = MibScalar
alarmHum = _AlarmHum_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 65),
    _AlarmHum_Type()
)
alarmHum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmHum.setStatus("current")
if mibBuilder.loadTexts:
    alarmHum.setUnits("N/A")


class _AlarmGeneral_Type(Integer32):
    """Custom type alarmGeneral based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmGeneral_Type.__name__ = "Integer32"
_AlarmGeneral_Object = MibScalar
alarmGeneral = _AlarmGeneral_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 66),
    _AlarmGeneral_Type()
)
alarmGeneral.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmGeneral.setStatus("current")
if mibBuilder.loadTexts:
    alarmGeneral.setUnits("N/A")


class _Alarm2ndLevel_Type(Integer32):
    """Custom type alarm2ndLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarm2ndLevel_Type.__name__ = "Integer32"
_Alarm2ndLevel_Object = MibScalar
alarm2ndLevel = _Alarm2ndLevel_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 67),
    _Alarm2ndLevel_Type()
)
alarm2ndLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarm2ndLevel.setStatus("current")
if mibBuilder.loadTexts:
    alarm2ndLevel.setUnits("N/A")


class _AlarmA_Type(Integer32):
    """Custom type alarmA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmA_Type.__name__ = "Integer32"
_AlarmA_Object = MibScalar
alarmA = _AlarmA_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 68),
    _AlarmA_Type()
)
alarmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmA.setStatus("current")
if mibBuilder.loadTexts:
    alarmA.setUnits("N/A")


class _AlarmB_Type(Integer32):
    """Custom type alarmB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmB_Type.__name__ = "Integer32"
_AlarmB_Object = MibScalar
alarmB = _AlarmB_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 69),
    _AlarmB_Type()
)
alarmB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmB.setStatus("current")
if mibBuilder.loadTexts:
    alarmB.setUnits("N/A")


class _AlarmC_Type(Integer32):
    """Custom type alarmC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmC_Type.__name__ = "Integer32"
_AlarmC_Object = MibScalar
alarmC = _AlarmC_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 70),
    _AlarmC_Type()
)
alarmC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmC.setStatus("current")
if mibBuilder.loadTexts:
    alarmC.setUnits("N/A")


class _SelDXCW_Type(Integer32):
    """Custom type selDXCW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SelDXCW_Type.__name__ = "Integer32"
_SelDXCW_Object = MibScalar
selDXCW = _SelDXCW_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 71),
    _SelDXCW_Type()
)
selDXCW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    selDXCW.setStatus("current")
if mibBuilder.loadTexts:
    selDXCW.setUnits("N/A")


class _SelSW_Type(Integer32):
    """Custom type selSW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SelSW_Type.__name__ = "Integer32"
_SelSW_Object = MibScalar
selSW = _SelSW_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 72),
    _SelSW_Type()
)
selSW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    selSW.setStatus("current")
if mibBuilder.loadTexts:
    selSW.setUnits("N/A")


class _SystemOnOff_Type(Integer32):
    """Custom type systemOnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SystemOnOff_Type.__name__ = "Integer32"
_SystemOnOff_Object = MibScalar
systemOnOff = _SystemOnOff_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 75),
    _SystemOnOff_Type()
)
systemOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemOnOff.setStatus("current")
if mibBuilder.loadTexts:
    systemOnOff.setUnits("N/A")


class _ResetAlarm_Type(Integer32):
    """Custom type resetAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ResetAlarm_Type.__name__ = "Integer32"
_ResetAlarm_Object = MibScalar
resetAlarm = _ResetAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 76),
    _ResetAlarm_Type()
)
resetAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetAlarm.setStatus("current")
if mibBuilder.loadTexts:
    resetAlarm.setUnits("N/A")


class _ResetHrsFilt_Type(Integer32):
    """Custom type resetHrsFilt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ResetHrsFilt_Type.__name__ = "Integer32"
_ResetHrsFilt_Object = MibScalar
resetHrsFilt = _ResetHrsFilt_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 77),
    _ResetHrsFilt_Type()
)
resetHrsFilt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetHrsFilt.setStatus("current")
if mibBuilder.loadTexts:
    resetHrsFilt.setUnits("N/A")


class _ResetHrC1_Type(Integer32):
    """Custom type resetHrC1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ResetHrC1_Type.__name__ = "Integer32"
_ResetHrC1_Object = MibScalar
resetHrC1 = _ResetHrC1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 78),
    _ResetHrC1_Type()
)
resetHrC1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetHrC1.setStatus("current")
if mibBuilder.loadTexts:
    resetHrC1.setUnits("N/A")


class _ResetHrC2_Type(Integer32):
    """Custom type resetHrC2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ResetHrC2_Type.__name__ = "Integer32"
_ResetHrC2_Object = MibScalar
resetHrC2 = _ResetHrC2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 79),
    _ResetHrC2_Type()
)
resetHrC2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetHrC2.setStatus("current")
if mibBuilder.loadTexts:
    resetHrC2.setUnits("N/A")


class _ResetHrC3_Type(Integer32):
    """Custom type resetHrC3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ResetHrC3_Type.__name__ = "Integer32"
_ResetHrC3_Object = MibScalar
resetHrC3 = _ResetHrC3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 80),
    _ResetHrC3_Type()
)
resetHrC3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetHrC3.setStatus("current")
if mibBuilder.loadTexts:
    resetHrC3.setUnits("N/A")


class _ResetHrC4_Type(Integer32):
    """Custom type resetHrC4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ResetHrC4_Type.__name__ = "Integer32"
_ResetHrC4_Object = MibScalar
resetHrC4 = _ResetHrC4_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 81),
    _ResetHrC4_Type()
)
resetHrC4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetHrC4.setStatus("current")
if mibBuilder.loadTexts:
    resetHrC4.setUnits("N/A")


class _ResetStC1_Type(Integer32):
    """Custom type resetStC1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ResetStC1_Type.__name__ = "Integer32"
_ResetStC1_Object = MibScalar
resetStC1 = _ResetStC1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 82),
    _ResetStC1_Type()
)
resetStC1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetStC1.setStatus("current")
if mibBuilder.loadTexts:
    resetStC1.setUnits("N/A")


class _ResetStC2_Type(Integer32):
    """Custom type resetStC2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ResetStC2_Type.__name__ = "Integer32"
_ResetStC2_Object = MibScalar
resetStC2 = _ResetStC2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 83),
    _ResetStC2_Type()
)
resetStC2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetStC2.setStatus("current")
if mibBuilder.loadTexts:
    resetStC2.setUnits("N/A")


class _ResetStC3_Type(Integer32):
    """Custom type resetStC3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ResetStC3_Type.__name__ = "Integer32"
_ResetStC3_Object = MibScalar
resetStC3 = _ResetStC3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 84),
    _ResetStC3_Type()
)
resetStC3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetStC3.setStatus("current")
if mibBuilder.loadTexts:
    resetStC3.setUnits("N/A")


class _ResetStC4_Type(Integer32):
    """Custom type resetStC4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ResetStC4_Type.__name__ = "Integer32"
_ResetStC4_Object = MibScalar
resetStC4 = _ResetStC4_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 85),
    _ResetStC4_Type()
)
resetStC4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetStC4.setStatus("current")
if mibBuilder.loadTexts:
    resetStC4.setUnits("N/A")


class _ResetHrH1_Type(Integer32):
    """Custom type resetHrH1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ResetHrH1_Type.__name__ = "Integer32"
_ResetHrH1_Object = MibScalar
resetHrH1 = _ResetHrH1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 86),
    _ResetHrH1_Type()
)
resetHrH1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetHrH1.setStatus("current")
if mibBuilder.loadTexts:
    resetHrH1.setUnits("N/A")


class _ResetHrH2_Type(Integer32):
    """Custom type resetHrH2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ResetHrH2_Type.__name__ = "Integer32"
_ResetHrH2_Object = MibScalar
resetHrH2 = _ResetHrH2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 87),
    _ResetHrH2_Type()
)
resetHrH2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetHrH2.setStatus("current")
if mibBuilder.loadTexts:
    resetHrH2.setUnits("N/A")


class _ResetStH1_Type(Integer32):
    """Custom type resetStH1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ResetStH1_Type.__name__ = "Integer32"
_ResetStH1_Object = MibScalar
resetStH1 = _ResetStH1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 88),
    _ResetStH1_Type()
)
resetStH1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetStH1.setStatus("current")
if mibBuilder.loadTexts:
    resetStH1.setUnits("N/A")


class _ResetStH2_Type(Integer32):
    """Custom type resetStH2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ResetStH2_Type.__name__ = "Integer32"
_ResetStH2_Object = MibScalar
resetStH2 = _ResetStH2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 89),
    _ResetStH2_Type()
)
resetStH2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetStH2.setStatus("current")
if mibBuilder.loadTexts:
    resetStH2.setUnits("N/A")


class _ResetHrHU_Type(Integer32):
    """Custom type resetHrHU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ResetHrHU_Type.__name__ = "Integer32"
_ResetHrHU_Object = MibScalar
resetHrHU = _ResetHrHU_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 90),
    _ResetHrHU_Type()
)
resetHrHU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetHrHU.setStatus("current")
if mibBuilder.loadTexts:
    resetHrHU.setUnits("N/A")


class _ResetStHU_Type(Integer32):
    """Custom type resetStHU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ResetStHU_Type.__name__ = "Integer32"
_ResetStHU_Object = MibScalar
resetStHU = _ResetStHU_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 91),
    _ResetStHU_Type()
)
resetStHU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetStHU.setStatus("current")
if mibBuilder.loadTexts:
    resetStHU.setUnits("N/A")


class _ResetHrACU_Type(Integer32):
    """Custom type resetHrACU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ResetHrACU_Type.__name__ = "Integer32"
_ResetHrACU_Object = MibScalar
resetHrACU = _ResetHrACU_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 92),
    _ResetHrACU_Type()
)
resetHrACU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetHrACU.setStatus("current")
if mibBuilder.loadTexts:
    resetHrACU.setUnits("N/A")


class _Sleepmode_Type(Integer32):
    """Custom type sleepmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sleepmode_Type.__name__ = "Integer32"
_Sleepmode_Object = MibScalar
sleepmode = _Sleepmode_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 95),
    _Sleepmode_Type()
)
sleepmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleepmode.setStatus("current")
if mibBuilder.loadTexts:
    sleepmode.setUnits("N/A")


class _Smtest_Type(Integer32):
    """Custom type smtest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Smtest_Type.__name__ = "Integer32"
_Smtest_Object = MibScalar
smtest = _Smtest_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 96),
    _Smtest_Type()
)
smtest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtest.setStatus("current")
if mibBuilder.loadTexts:
    smtest.setUnits("N/A")


class _EnablemeanT_Type(Integer32):
    """Custom type enablemeanT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_EnablemeanT_Type.__name__ = "Integer32"
_EnablemeanT_Object = MibScalar
enablemeanT = _EnablemeanT_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 97),
    _EnablemeanT_Type()
)
enablemeanT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enablemeanT.setStatus("current")
if mibBuilder.loadTexts:
    enablemeanT.setUnits("N/A")
_AnalogObjects_ObjectIdentity = ObjectIdentity
analogObjects = _AnalogObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2)
)


class _RoomTemp_Type(Integer32):
    """Custom type roomTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_RoomTemp_Type.__name__ = "Integer32"
_RoomTemp_Object = MibScalar
roomTemp = _RoomTemp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 1),
    _RoomTemp_Type()
)
roomTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roomTemp.setStatus("current")
if mibBuilder.loadTexts:
    roomTemp.setUnits("degrees C")


class _OutdoorTemp_Type(Integer32):
    """Custom type outdoorTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_OutdoorTemp_Type.__name__ = "Integer32"
_OutdoorTemp_Object = MibScalar
outdoorTemp = _OutdoorTemp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 2),
    _OutdoorTemp_Type()
)
outdoorTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outdoorTemp.setStatus("current")
if mibBuilder.loadTexts:
    outdoorTemp.setUnits("degrees C")


class _DeliveryTemp_Type(Integer32):
    """Custom type deliveryTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_DeliveryTemp_Type.__name__ = "Integer32"
_DeliveryTemp_Object = MibScalar
deliveryTemp = _DeliveryTemp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 3),
    _DeliveryTemp_Type()
)
deliveryTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deliveryTemp.setStatus("current")
if mibBuilder.loadTexts:
    deliveryTemp.setUnits("degrees C")


class _CwTemp_Type(Integer32):
    """Custom type cwTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_CwTemp_Type.__name__ = "Integer32"
_CwTemp_Object = MibScalar
cwTemp = _CwTemp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 4),
    _CwTemp_Type()
)
cwTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwTemp.setStatus("current")
if mibBuilder.loadTexts:
    cwTemp.setUnits("degrees C")


class _HwTemp_Type(Integer32):
    """Custom type hwTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_HwTemp_Type.__name__ = "Integer32"
_HwTemp_Object = MibScalar
hwTemp = _HwTemp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 5),
    _HwTemp_Type()
)
hwTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTemp.setStatus("current")
if mibBuilder.loadTexts:
    hwTemp.setUnits("degrees C")


class _RoomRH_Type(Integer32):
    """Custom type roomRH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_RoomRH_Type.__name__ = "Integer32"
_RoomRH_Object = MibScalar
roomRH = _RoomRH_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 6),
    _RoomRH_Type()
)
roomRH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roomRH.setStatus("current")
if mibBuilder.loadTexts:
    roomRH.setUnits("rH%")


class _CwoTemp_Type(Integer32):
    """Custom type cwoTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_CwoTemp_Type.__name__ = "Integer32"
_CwoTemp_Object = MibScalar
cwoTemp = _CwoTemp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 7),
    _CwoTemp_Type()
)
cwoTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoTemp.setStatus("current")
if mibBuilder.loadTexts:
    cwoTemp.setUnits("degrees C")


class _EvapPress1_Type(Integer32):
    """Custom type evapPress1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_EvapPress1_Type.__name__ = "Integer32"
_EvapPress1_Object = MibScalar
evapPress1 = _EvapPress1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 8),
    _EvapPress1_Type()
)
evapPress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evapPress1.setStatus("current")
if mibBuilder.loadTexts:
    evapPress1.setUnits("bar")


class _EvapPress2_Type(Integer32):
    """Custom type evapPress2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_EvapPress2_Type.__name__ = "Integer32"
_EvapPress2_Object = MibScalar
evapPress2 = _EvapPress2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 9),
    _EvapPress2_Type()
)
evapPress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evapPress2.setStatus("current")
if mibBuilder.loadTexts:
    evapPress2.setUnits("bar")


class _SuctTemp1_Type(Integer32):
    """Custom type suctTemp1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_SuctTemp1_Type.__name__ = "Integer32"
_SuctTemp1_Object = MibScalar
suctTemp1 = _SuctTemp1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 10),
    _SuctTemp1_Type()
)
suctTemp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    suctTemp1.setStatus("current")
if mibBuilder.loadTexts:
    suctTemp1.setUnits("degrees C")


class _SuctTemp2_Type(Integer32):
    """Custom type suctTemp2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_SuctTemp2_Type.__name__ = "Integer32"
_SuctTemp2_Object = MibScalar
suctTemp2 = _SuctTemp2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 11),
    _SuctTemp2_Type()
)
suctTemp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    suctTemp2.setStatus("current")
if mibBuilder.loadTexts:
    suctTemp2.setUnits("degrees C")


class _EvapTemp1_Type(Integer32):
    """Custom type evapTemp1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_EvapTemp1_Type.__name__ = "Integer32"
_EvapTemp1_Object = MibScalar
evapTemp1 = _EvapTemp1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 12),
    _EvapTemp1_Type()
)
evapTemp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evapTemp1.setStatus("current")
if mibBuilder.loadTexts:
    evapTemp1.setUnits("degrees C")


class _EvapTemp2_Type(Integer32):
    """Custom type evapTemp2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_EvapTemp2_Type.__name__ = "Integer32"
_EvapTemp2_Object = MibScalar
evapTemp2 = _EvapTemp2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 13),
    _EvapTemp2_Type()
)
evapTemp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evapTemp2.setStatus("current")
if mibBuilder.loadTexts:
    evapTemp2.setUnits("degrees C")


class _Ssh1_Type(Integer32):
    """Custom type ssh1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Ssh1_Type.__name__ = "Integer32"
_Ssh1_Object = MibScalar
ssh1 = _Ssh1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 14),
    _Ssh1_Type()
)
ssh1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssh1.setStatus("current")
if mibBuilder.loadTexts:
    ssh1.setUnits("degrees C")


class _Ssh2_Type(Integer32):
    """Custom type ssh2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Ssh2_Type.__name__ = "Integer32"
_Ssh2_Object = MibScalar
ssh2 = _Ssh2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 15),
    _Ssh2_Type()
)
ssh2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssh2.setStatus("current")
if mibBuilder.loadTexts:
    ssh2.setUnits("degrees C")


class _CoolRamp_Type(Integer32):
    """Custom type coolRamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_CoolRamp_Type.__name__ = "Integer32"
_CoolRamp_Object = MibScalar
coolRamp = _CoolRamp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 16),
    _CoolRamp_Type()
)
coolRamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolRamp.setStatus("current")
if mibBuilder.loadTexts:
    coolRamp.setUnits("%")


class _HeatRamp_Type(Integer32):
    """Custom type heatRamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_HeatRamp_Type.__name__ = "Integer32"
_HeatRamp_Object = MibScalar
heatRamp = _HeatRamp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 17),
    _HeatRamp_Type()
)
heatRamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heatRamp.setStatus("current")
if mibBuilder.loadTexts:
    heatRamp.setUnits("%")


class _FanSpeed_Type(Integer32):
    """Custom type fanSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_FanSpeed_Type.__name__ = "Integer32"
_FanSpeed_Object = MibScalar
fanSpeed = _FanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 18),
    _FanSpeed_Type()
)
fanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanSpeed.setStatus("current")
if mibBuilder.loadTexts:
    fanSpeed.setUnits("%")


class _CoolSetP_Type(Integer32):
    """Custom type coolSetP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_CoolSetP_Type.__name__ = "Integer32"
_CoolSetP_Object = MibScalar
coolSetP = _CoolSetP_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 20),
    _CoolSetP_Type()
)
coolSetP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coolSetP.setStatus("current")
if mibBuilder.loadTexts:
    coolSetP.setUnits("degrees C")


class _CoolDiff_Type(Integer32):
    """Custom type coolDiff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_CoolDiff_Type.__name__ = "Integer32"
_CoolDiff_Object = MibScalar
coolDiff = _CoolDiff_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 21),
    _CoolDiff_Type()
)
coolDiff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coolDiff.setStatus("current")
if mibBuilder.loadTexts:
    coolDiff.setUnits("degrees C")


class _Cool2SetP_Type(Integer32):
    """Custom type cool2SetP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Cool2SetP_Type.__name__ = "Integer32"
_Cool2SetP_Object = MibScalar
cool2SetP = _Cool2SetP_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 22),
    _Cool2SetP_Type()
)
cool2SetP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cool2SetP.setStatus("current")
if mibBuilder.loadTexts:
    cool2SetP.setUnits("degrees C")


class _HeatSetP_Type(Integer32):
    """Custom type heatSetP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_HeatSetP_Type.__name__ = "Integer32"
_HeatSetP_Object = MibScalar
heatSetP = _HeatSetP_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 23),
    _HeatSetP_Type()
)
heatSetP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heatSetP.setStatus("current")
if mibBuilder.loadTexts:
    heatSetP.setUnits("degrees C")


class _Heat2SetP_Type(Integer32):
    """Custom type heat2SetP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Heat2SetP_Type.__name__ = "Integer32"
_Heat2SetP_Object = MibScalar
heat2SetP = _Heat2SetP_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 24),
    _Heat2SetP_Type()
)
heat2SetP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heat2SetP.setStatus("current")
if mibBuilder.loadTexts:
    heat2SetP.setUnits("degrees C")


class _HeatDiff_Type(Integer32):
    """Custom type heatDiff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_HeatDiff_Type.__name__ = "Integer32"
_HeatDiff_Object = MibScalar
heatDiff = _HeatDiff_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 25),
    _HeatDiff_Type()
)
heatDiff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heatDiff.setStatus("current")
if mibBuilder.loadTexts:
    heatDiff.setUnits("degrees C")


class _ThrsHT_Type(Integer32):
    """Custom type thrsHT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_ThrsHT_Type.__name__ = "Integer32"
_ThrsHT_Object = MibScalar
thrsHT = _ThrsHT_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 26),
    _ThrsHT_Type()
)
thrsHT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thrsHT.setStatus("current")
if mibBuilder.loadTexts:
    thrsHT.setUnits("degrees C x10")


class _ThrsLT_Type(Integer32):
    """Custom type thrsLT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_ThrsLT_Type.__name__ = "Integer32"
_ThrsLT_Object = MibScalar
thrsLT = _ThrsLT_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 27),
    _ThrsLT_Type()
)
thrsLT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thrsLT.setStatus("current")
if mibBuilder.loadTexts:
    thrsLT.setUnits("degrees C x10")


class _SmCoolSetp_Type(Integer32):
    """Custom type smCoolSetp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_SmCoolSetp_Type.__name__ = "Integer32"
_SmCoolSetp_Object = MibScalar
smCoolSetp = _SmCoolSetp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 28),
    _SmCoolSetp_Type()
)
smCoolSetp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smCoolSetp.setStatus("current")
if mibBuilder.loadTexts:
    smCoolSetp.setUnits("degrees C")


class _SmHeatSetp_Type(Integer32):
    """Custom type smHeatSetp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_SmHeatSetp_Type.__name__ = "Integer32"
_SmHeatSetp_Object = MibScalar
smHeatSetp = _SmHeatSetp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 29),
    _SmHeatSetp_Type()
)
smHeatSetp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smHeatSetp.setStatus("current")
if mibBuilder.loadTexts:
    smHeatSetp.setUnits("degrees C")


class _CwDehumSetp_Type(Integer32):
    """Custom type cwDehumSetp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_CwDehumSetp_Type.__name__ = "Integer32"
_CwDehumSetp_Object = MibScalar
cwDehumSetp = _CwDehumSetp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 30),
    _CwDehumSetp_Type()
)
cwDehumSetp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwDehumSetp.setStatus("current")
if mibBuilder.loadTexts:
    cwDehumSetp.setUnits("degrees C")


class _CwHtThrsh_Type(Integer32):
    """Custom type cwHtThrsh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_CwHtThrsh_Type.__name__ = "Integer32"
_CwHtThrsh_Object = MibScalar
cwHtThrsh = _CwHtThrsh_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 31),
    _CwHtThrsh_Type()
)
cwHtThrsh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwHtThrsh.setStatus("current")
if mibBuilder.loadTexts:
    cwHtThrsh.setUnits("degrees C")


class _CwModeSetp_Type(Integer32):
    """Custom type cwModeSetp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_CwModeSetp_Type.__name__ = "Integer32"
_CwModeSetp_Object = MibScalar
cwModeSetp = _CwModeSetp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 32),
    _CwModeSetp_Type()
)
cwModeSetp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwModeSetp.setStatus("current")
if mibBuilder.loadTexts:
    cwModeSetp.setUnits("degrees C")


class _RadcoolSpES_Type(Integer32):
    """Custom type radcoolSpES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_RadcoolSpES_Type.__name__ = "Integer32"
_RadcoolSpES_Object = MibScalar
radcoolSpES = _RadcoolSpES_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 33),
    _RadcoolSpES_Type()
)
radcoolSpES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radcoolSpES.setStatus("current")
if mibBuilder.loadTexts:
    radcoolSpES.setUnits("degrees C")


class _RadcoolSpDX_Type(Integer32):
    """Custom type radcoolSpDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_RadcoolSpDX_Type.__name__ = "Integer32"
_RadcoolSpDX_Object = MibScalar
radcoolSpDX = _RadcoolSpDX_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 34),
    _RadcoolSpDX_Type()
)
radcoolSpDX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radcoolSpDX.setStatus("current")
if mibBuilder.loadTexts:
    radcoolSpDX.setUnits("degrees C")


class _DelTempLimit_Type(Integer32):
    """Custom type delTempLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_DelTempLimit_Type.__name__ = "Integer32"
_DelTempLimit_Object = MibScalar
delTempLimit = _DelTempLimit_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 35),
    _DelTempLimit_Type()
)
delTempLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    delTempLimit.setStatus("current")
if mibBuilder.loadTexts:
    delTempLimit.setUnits("degrees C x10")


class _DtAutChgMLT_Type(Integer32):
    """Custom type dtAutChgMLT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_DtAutChgMLT_Type.__name__ = "Integer32"
_DtAutChgMLT_Object = MibScalar
dtAutChgMLT = _DtAutChgMLT_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 36),
    _DtAutChgMLT_Type()
)
dtAutChgMLT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtAutChgMLT.setStatus("current")
if mibBuilder.loadTexts:
    dtAutChgMLT.setUnits("degrees C")
_IntegerObjects_ObjectIdentity = ObjectIdentity
integerObjects = _IntegerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3)
)


class _FilterWorkH_Type(Integer32):
    """Custom type filterWorkH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_FilterWorkH_Type.__name__ = "Integer32"
_FilterWorkH_Object = MibScalar
filterWorkH = _FilterWorkH_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 1),
    _FilterWorkH_Type()
)
filterWorkH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterWorkH.setStatus("current")
if mibBuilder.loadTexts:
    filterWorkH.setUnits("h")


class _UnitWorkH_Type(Integer32):
    """Custom type unitWorkH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_UnitWorkH_Type.__name__ = "Integer32"
_UnitWorkH_Object = MibScalar
unitWorkH = _UnitWorkH_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 2),
    _UnitWorkH_Type()
)
unitWorkH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitWorkH.setStatus("current")
if mibBuilder.loadTexts:
    unitWorkH.setUnits("h")


class _Compr1WorkH_Type(Integer32):
    """Custom type compr1WorkH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Compr1WorkH_Type.__name__ = "Integer32"
_Compr1WorkH_Object = MibScalar
compr1WorkH = _Compr1WorkH_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 3),
    _Compr1WorkH_Type()
)
compr1WorkH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compr1WorkH.setStatus("current")
if mibBuilder.loadTexts:
    compr1WorkH.setUnits("h")


class _Compr2WorkH_Type(Integer32):
    """Custom type compr2WorkH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Compr2WorkH_Type.__name__ = "Integer32"
_Compr2WorkH_Object = MibScalar
compr2WorkH = _Compr2WorkH_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 4),
    _Compr2WorkH_Type()
)
compr2WorkH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compr2WorkH.setStatus("current")
if mibBuilder.loadTexts:
    compr2WorkH.setUnits("h")


class _Compr3WorkH_Type(Integer32):
    """Custom type compr3WorkH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Compr3WorkH_Type.__name__ = "Integer32"
_Compr3WorkH_Object = MibScalar
compr3WorkH = _Compr3WorkH_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 5),
    _Compr3WorkH_Type()
)
compr3WorkH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compr3WorkH.setStatus("current")
if mibBuilder.loadTexts:
    compr3WorkH.setUnits("h")


class _Compr4WorkH_Type(Integer32):
    """Custom type compr4WorkH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Compr4WorkH_Type.__name__ = "Integer32"
_Compr4WorkH_Object = MibScalar
compr4WorkH = _Compr4WorkH_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 6),
    _Compr4WorkH_Type()
)
compr4WorkH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compr4WorkH.setStatus("current")
if mibBuilder.loadTexts:
    compr4WorkH.setUnits("h")


class _Heat1WorkH_Type(Integer32):
    """Custom type heat1WorkH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Heat1WorkH_Type.__name__ = "Integer32"
_Heat1WorkH_Object = MibScalar
heat1WorkH = _Heat1WorkH_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 7),
    _Heat1WorkH_Type()
)
heat1WorkH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heat1WorkH.setStatus("current")
if mibBuilder.loadTexts:
    heat1WorkH.setUnits("h")


class _Heat2WorkH_Type(Integer32):
    """Custom type heat2WorkH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Heat2WorkH_Type.__name__ = "Integer32"
_Heat2WorkH_Object = MibScalar
heat2WorkH = _Heat2WorkH_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 8),
    _Heat2WorkH_Type()
)
heat2WorkH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heat2WorkH.setStatus("current")
if mibBuilder.loadTexts:
    heat2WorkH.setUnits("h")


class _HumiWorkH_Type(Integer32):
    """Custom type humiWorkH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_HumiWorkH_Type.__name__ = "Integer32"
_HumiWorkH_Object = MibScalar
humiWorkH = _HumiWorkH_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 9),
    _HumiWorkH_Type()
)
humiWorkH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humiWorkH.setStatus("current")
if mibBuilder.loadTexts:
    humiWorkH.setUnits("h")


class _DehumPband_Type(Integer32):
    """Custom type dehumPband based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_DehumPband_Type.__name__ = "Integer32"
_DehumPband_Object = MibScalar
dehumPband = _DehumPband_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 12),
    _DehumPband_Type()
)
dehumPband.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dehumPband.setStatus("current")
if mibBuilder.loadTexts:
    dehumPband.setUnits("rH%")


class _HumidPband_Type(Integer32):
    """Custom type humidPband based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_HumidPband_Type.__name__ = "Integer32"
_HumidPband_Object = MibScalar
humidPband = _HumidPband_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 13),
    _HumidPband_Type()
)
humidPband.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidPband.setStatus("current")
if mibBuilder.loadTexts:
    humidPband.setUnits("rH%")


class _HhAlarmThrsh_Type(Integer32):
    """Custom type hhAlarmThrsh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_HhAlarmThrsh_Type.__name__ = "Integer32"
_HhAlarmThrsh_Object = MibScalar
hhAlarmThrsh = _HhAlarmThrsh_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 14),
    _HhAlarmThrsh_Type()
)
hhAlarmThrsh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhAlarmThrsh.setStatus("current")
if mibBuilder.loadTexts:
    hhAlarmThrsh.setUnits("rH%")


class _LhAlarmThrsh_Type(Integer32):
    """Custom type lhAlarmThrsh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_LhAlarmThrsh_Type.__name__ = "Integer32"
_LhAlarmThrsh_Object = MibScalar
lhAlarmThrsh = _LhAlarmThrsh_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 15),
    _LhAlarmThrsh_Type()
)
lhAlarmThrsh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lhAlarmThrsh.setStatus("current")
if mibBuilder.loadTexts:
    lhAlarmThrsh.setUnits("rH%")


class _DehumSetp_Type(Integer32):
    """Custom type dehumSetp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_DehumSetp_Type.__name__ = "Integer32"
_DehumSetp_Object = MibScalar
dehumSetp = _DehumSetp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 16),
    _DehumSetp_Type()
)
dehumSetp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dehumSetp.setStatus("current")
if mibBuilder.loadTexts:
    dehumSetp.setUnits("rH%")


class _SmDehumSetp_Type(Integer32):
    """Custom type smDehumSetp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_SmDehumSetp_Type.__name__ = "Integer32"
_SmDehumSetp_Object = MibScalar
smDehumSetp = _SmDehumSetp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 17),
    _SmDehumSetp_Type()
)
smDehumSetp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smDehumSetp.setStatus("current")
if mibBuilder.loadTexts:
    smDehumSetp.setUnits("rH%")


class _HumidSetp_Type(Integer32):
    """Custom type humidSetp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_HumidSetp_Type.__name__ = "Integer32"
_HumidSetp_Object = MibScalar
humidSetp = _HumidSetp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 18),
    _HumidSetp_Type()
)
humidSetp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidSetp.setStatus("current")
if mibBuilder.loadTexts:
    humidSetp.setUnits("rH%")


class _SmHumidSetp_Type(Integer32):
    """Custom type smHumidSetp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_SmHumidSetp_Type.__name__ = "Integer32"
_SmHumidSetp_Object = MibScalar
smHumidSetp = _SmHumidSetp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 19),
    _SmHumidSetp_Type()
)
smHumidSetp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smHumidSetp.setStatus("current")
if mibBuilder.loadTexts:
    smHumidSetp.setUnits("rH%")


class _PwOnDelay_Type(Integer32):
    """Custom type pwOnDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_PwOnDelay_Type.__name__ = "Integer32"
_PwOnDelay_Object = MibScalar
pwOnDelay = _PwOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 20),
    _PwOnDelay_Type()
)
pwOnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwOnDelay.setStatus("current")
if mibBuilder.loadTexts:
    pwOnDelay.setUnits("s")


class _RegulDelay_Type(Integer32):
    """Custom type regulDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_RegulDelay_Type.__name__ = "Integer32"
_RegulDelay_Object = MibScalar
regulDelay = _RegulDelay_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 21),
    _RegulDelay_Type()
)
regulDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regulDelay.setStatus("current")
if mibBuilder.loadTexts:
    regulDelay.setUnits("s")


class _LowPdelay_Type(Integer32):
    """Custom type lowPdelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_LowPdelay_Type.__name__ = "Integer32"
_LowPdelay_Object = MibScalar
lowPdelay = _LowPdelay_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 22),
    _LowPdelay_Type()
)
lowPdelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowPdelay.setStatus("current")
if mibBuilder.loadTexts:
    lowPdelay.setUnits("s")


class _ThAlarmdelay_Type(Integer32):
    """Custom type thAlarmdelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_ThAlarmdelay_Type.__name__ = "Integer32"
_ThAlarmdelay_Object = MibScalar
thAlarmdelay = _ThAlarmdelay_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 23),
    _ThAlarmdelay_Type()
)
thAlarmdelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thAlarmdelay.setStatus("current")
if mibBuilder.loadTexts:
    thAlarmdelay.setUnits("min")


class _RegExcTime_Type(Integer32):
    """Custom type regExcTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_RegExcTime_Type.__name__ = "Integer32"
_RegExcTime_Object = MibScalar
regExcTime = _RegExcTime_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 24),
    _RegExcTime_Type()
)
regExcTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regExcTime.setStatus("current")
if mibBuilder.loadTexts:
    regExcTime.setUnits("min")


class _StdbyTime_Type(Integer32):
    """Custom type stdbyTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_StdbyTime_Type.__name__ = "Integer32"
_StdbyTime_Object = MibScalar
stdbyTime = _StdbyTime_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 25),
    _StdbyTime_Type()
)
stdbyTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stdbyTime.setStatus("current")
if mibBuilder.loadTexts:
    stdbyTime.setUnits("h")


class _LanUnit_Type(Integer32):
    """Custom type lanUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_LanUnit_Type.__name__ = "Integer32"
_LanUnit_Object = MibScalar
lanUnit = _LanUnit_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 27),
    _LanUnit_Type()
)
lanUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanUnit.setStatus("current")
if mibBuilder.loadTexts:
    lanUnit.setUnits("n")


class _SmCycleTime_Type(Integer32):
    """Custom type smCycleTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_SmCycleTime_Type.__name__ = "Integer32"
_SmCycleTime_Object = MibScalar
smCycleTime = _SmCycleTime_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 28),
    _SmCycleTime_Type()
)
smCycleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smCycleTime.setStatus("current")
if mibBuilder.loadTexts:
    smCycleTime.setUnits("min")


class _Exv1steps_Type(Integer32):
    """Custom type exv1steps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Exv1steps_Type.__name__ = "Integer32"
_Exv1steps_Object = MibScalar
exv1steps = _Exv1steps_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 29),
    _Exv1steps_Type()
)
exv1steps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exv1steps.setStatus("current")
if mibBuilder.loadTexts:
    exv1steps.setUnits("n")


class _Exv2steps_Type(Integer32):
    """Custom type exv2steps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Exv2steps_Type.__name__ = "Integer32"
_Exv2steps_Object = MibScalar
exv2steps = _Exv2steps_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 30),
    _Exv2steps_Type()
)
exv2steps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exv2steps.setStatus("current")
if mibBuilder.loadTexts:
    exv2steps.setUnits("n")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CAREL-ug40cdz-MIB",
    **{"carel": carel,
       "systm": systm,
       "agentRelease": agentRelease,
       "agentCode": agentCode,
       "instruments": instruments,
       "webGateInfo": webGateInfo,
       "agentParameters": agentParameters,
       "netSize": netSize,
       "baudRate": baudRate,
       "unitTypeGroup": unitTypeGroup,
       "unit1-Type": unit1_Type,
       "unitCodeGroup": unitCodeGroup,
       "unit1-Code": unit1_Code,
       "unitSoftwareReleaseGroup": unitSoftwareReleaseGroup,
       "unit1-SoftwareRelease": unit1_SoftwareRelease,
       "unitMinSoftwareReleaseGroup": unitMinSoftwareReleaseGroup,
       "unit1-MinSoftwareRelease": unit1_MinSoftwareRelease,
       "unitMaxSoftwareReleaseGroup": unitMaxSoftwareReleaseGroup,
       "unit1-MaxSoftwareRelease": unit1_MaxSoftwareRelease,
       "unitNoAnswerCounterGroup": unitNoAnswerCounterGroup,
       "unit1-NoAnswerCounter": unit1_NoAnswerCounter,
       "unitErrorChecksumCounterGroup": unitErrorChecksumCounterGroup,
       "unit1-ErrorChecksumCounter": unit1_ErrorChecksumCounter,
       "unitTimeoutCounterGroup": unitTimeoutCounterGroup,
       "unit1-TimeoutCounter": unit1_TimeoutCounter,
       "ug40cdzMIB": ug40cdzMIB,
       "digitalObjects": digitalObjects,
       "systemOn": systemOn,
       "compressore1": compressore1,
       "compressore2": compressore2,
       "compressore3": compressore3,
       "compressore4": compressore4,
       "heating1": heating1,
       "heating2": heating2,
       "hotGasCoil": hotGasCoil,
       "dehumidification": dehumidification,
       "humidification": humidification,
       "emerg": emerg,
       "alarmAccess": alarmAccess,
       "alarmRoomHT": alarmRoomHT,
       "alarmRoomLT": alarmRoomLT,
       "alarmRoomHH": alarmRoomHH,
       "alarmRoomLH": alarmRoomLH,
       "alarmRoomEAP": alarmRoomEAP,
       "alarmFilter": alarmFilter,
       "alarmFlood": alarmFlood,
       "alarmAirFlow": alarmAirFlow,
       "alarmHeater": alarmHeater,
       "alarmHP1": alarmHP1,
       "alarmHP2": alarmHP2,
       "alarmLP1": alarmLP1,
       "alarmLP2": alarmLP2,
       "alarmEXV1": alarmEXV1,
       "alarmEXV2": alarmEXV2,
       "alarmPSE": alarmPSE,
       "alarmSmokeFire": alarmSmokeFire,
       "alarmLAN": alarmLAN,
       "alarmHUHC": alarmHUHC,
       "alarmHUPL": alarmHUPL,
       "alarmHUWL": alarmHUWL,
       "alarmCWDHT": alarmCWDHT,
       "alarmCWF": alarmCWF,
       "alarmCWFF": alarmCWFF,
       "alarmCWHT": alarmCWHT,
       "alarmRTS": alarmRTS,
       "alarmHWS": alarmHWS,
       "alarmCWS": alarmCWS,
       "alarmOTS": alarmOTS,
       "alarmDTS": alarmDTS,
       "alarmRHS": alarmRHS,
       "alarmCWOTS": alarmCWOTS,
       "alarmC1Hours": alarmC1Hours,
       "alarmC2Hours": alarmC2Hours,
       "alarmC3Hours": alarmC3Hours,
       "alarmC4Hours": alarmC4Hours,
       "alarmFilterHours": alarmFilterHours,
       "alarmHeat1Hours": alarmHeat1Hours,
       "alarmHeat2Hours": alarmHeat2Hours,
       "alarmHumHours": alarmHumHours,
       "alarmUnitHours": alarmUnitHours,
       "alarmDI2": alarmDI2,
       "alarmDI4": alarmDI4,
       "alarmDI6": alarmDI6,
       "alarmHum": alarmHum,
       "alarmGeneral": alarmGeneral,
       "alarm2ndLevel": alarm2ndLevel,
       "alarmA": alarmA,
       "alarmB": alarmB,
       "alarmC": alarmC,
       "selDXCW": selDXCW,
       "selSW": selSW,
       "systemOnOff": systemOnOff,
       "resetAlarm": resetAlarm,
       "resetHrsFilt": resetHrsFilt,
       "resetHrC1": resetHrC1,
       "resetHrC2": resetHrC2,
       "resetHrC3": resetHrC3,
       "resetHrC4": resetHrC4,
       "resetStC1": resetStC1,
       "resetStC2": resetStC2,
       "resetStC3": resetStC3,
       "resetStC4": resetStC4,
       "resetHrH1": resetHrH1,
       "resetHrH2": resetHrH2,
       "resetStH1": resetStH1,
       "resetStH2": resetStH2,
       "resetHrHU": resetHrHU,
       "resetStHU": resetStHU,
       "resetHrACU": resetHrACU,
       "sleepmode": sleepmode,
       "smtest": smtest,
       "enablemeanT": enablemeanT,
       "analogObjects": analogObjects,
       "roomTemp": roomTemp,
       "outdoorTemp": outdoorTemp,
       "deliveryTemp": deliveryTemp,
       "cwTemp": cwTemp,
       "hwTemp": hwTemp,
       "roomRH": roomRH,
       "cwoTemp": cwoTemp,
       "evapPress1": evapPress1,
       "evapPress2": evapPress2,
       "suctTemp1": suctTemp1,
       "suctTemp2": suctTemp2,
       "evapTemp1": evapTemp1,
       "evapTemp2": evapTemp2,
       "ssh1": ssh1,
       "ssh2": ssh2,
       "coolRamp": coolRamp,
       "heatRamp": heatRamp,
       "fanSpeed": fanSpeed,
       "coolSetP": coolSetP,
       "coolDiff": coolDiff,
       "cool2SetP": cool2SetP,
       "heatSetP": heatSetP,
       "heat2SetP": heat2SetP,
       "heatDiff": heatDiff,
       "thrsHT": thrsHT,
       "thrsLT": thrsLT,
       "smCoolSetp": smCoolSetp,
       "smHeatSetp": smHeatSetp,
       "cwDehumSetp": cwDehumSetp,
       "cwHtThrsh": cwHtThrsh,
       "cwModeSetp": cwModeSetp,
       "radcoolSpES": radcoolSpES,
       "radcoolSpDX": radcoolSpDX,
       "delTempLimit": delTempLimit,
       "dtAutChgMLT": dtAutChgMLT,
       "integerObjects": integerObjects,
       "filterWorkH": filterWorkH,
       "unitWorkH": unitWorkH,
       "compr1WorkH": compr1WorkH,
       "compr2WorkH": compr2WorkH,
       "compr3WorkH": compr3WorkH,
       "compr4WorkH": compr4WorkH,
       "heat1WorkH": heat1WorkH,
       "heat2WorkH": heat2WorkH,
       "humiWorkH": humiWorkH,
       "dehumPband": dehumPband,
       "humidPband": humidPband,
       "hhAlarmThrsh": hhAlarmThrsh,
       "lhAlarmThrsh": lhAlarmThrsh,
       "dehumSetp": dehumSetp,
       "smDehumSetp": smDehumSetp,
       "humidSetp": humidSetp,
       "smHumidSetp": smHumidSetp,
       "pwOnDelay": pwOnDelay,
       "regulDelay": regulDelay,
       "lowPdelay": lowPdelay,
       "thAlarmdelay": thAlarmdelay,
       "regExcTime": regExcTime,
       "stdbyTime": stdbyTime,
       "lanUnit": lanUnit,
       "smCycleTime": smCycleTime,
       "exv1steps": exv1steps,
       "exv2steps": exv2steps}
)
