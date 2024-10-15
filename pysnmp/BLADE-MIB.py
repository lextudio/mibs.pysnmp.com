# SNMP MIB module (BLADE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BLADE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:59 2024
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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmAgents_ObjectIdentity = ObjectIdentity
ibmAgents = _IbmAgents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3)
)
_NetfinitySupportProcessorAgent_ObjectIdentity = ObjectIdentity
netfinitySupportProcessorAgent = _NetfinitySupportProcessorAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51)
)
_BladeCenterSnmpMIB_ObjectIdentity = ObjectIdentity
bladeCenterSnmpMIB = _BladeCenterSnmpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2)
)
_Monitors_ObjectIdentity = ObjectIdentity
monitors = _Monitors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2)
)
_Temperature_ObjectIdentity = ObjectIdentity
temperature = _Temperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 1)
)
_PlanarTemp_ObjectIdentity = ObjectIdentity
planarTemp = _PlanarTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 1, 1)
)
_MmTemp_Type = OctetString
_MmTemp_Object = MibScalar
mmTemp = _MmTemp_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 1, 1, 2),
    _MmTemp_Type()
)
mmTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmTemp.setStatus("mandatory")
_CpuXTemp_ObjectIdentity = ObjectIdentity
cpuXTemp = _CpuXTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 1, 2)
)
_AmbientTemp_ObjectIdentity = ObjectIdentity
ambientTemp = _AmbientTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 1, 5)
)
_FrontPanelTemp_Type = OctetString
_FrontPanelTemp_Object = MibScalar
frontPanelTemp = _FrontPanelTemp_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 1, 5, 1),
    _FrontPanelTemp_Type()
)
frontPanelTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frontPanelTemp.setStatus("mandatory")
_Voltage_ObjectIdentity = ObjectIdentity
voltage = _Voltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 2)
)
_PlanarVolt_ObjectIdentity = ObjectIdentity
planarVolt = _PlanarVolt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 2, 1)
)
_Plus5Volt_Type = OctetString
_Plus5Volt_Object = MibScalar
plus5Volt = _Plus5Volt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 2, 1, 1),
    _Plus5Volt_Type()
)
plus5Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plus5Volt.setStatus("mandatory")
_Plus3Pt3Volt_Type = OctetString
_Plus3Pt3Volt_Object = MibScalar
plus3Pt3Volt = _Plus3Pt3Volt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 2, 1, 2),
    _Plus3Pt3Volt_Type()
)
plus3Pt3Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plus3Pt3Volt.setStatus("mandatory")
_Plus12Volt_Type = OctetString
_Plus12Volt_Object = MibScalar
plus12Volt = _Plus12Volt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 2, 1, 3),
    _Plus12Volt_Type()
)
plus12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plus12Volt.setStatus("mandatory")
_Minus5Volt_Type = OctetString
_Minus5Volt_Object = MibScalar
minus5Volt = _Minus5Volt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 2, 1, 5),
    _Minus5Volt_Type()
)
minus5Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minus5Volt.setStatus("mandatory")
_Plus2Pt5Volt_Type = OctetString
_Plus2Pt5Volt_Object = MibScalar
plus2Pt5Volt = _Plus2Pt5Volt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 2, 1, 6),
    _Plus2Pt5Volt_Type()
)
plus2Pt5Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plus2Pt5Volt.setStatus("mandatory")
_Plus1Pt8Volt_Type = OctetString
_Plus1Pt8Volt_Object = MibScalar
plus1Pt8Volt = _Plus1Pt8Volt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 2, 1, 8),
    _Plus1Pt8Volt_Type()
)
plus1Pt8Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plus1Pt8Volt.setStatus("mandatory")
_Blowers_ObjectIdentity = ObjectIdentity
blowers = _Blowers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 3)
)
_Blower1speed_Type = OctetString
_Blower1speed_Object = MibScalar
blower1speed = _Blower1speed_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 3, 1),
    _Blower1speed_Type()
)
blower1speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blower1speed.setStatus("mandatory")
_Blower2speed_Type = OctetString
_Blower2speed_Object = MibScalar
blower2speed = _Blower2speed_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 3, 2),
    _Blower2speed_Type()
)
blower2speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blower2speed.setStatus("mandatory")


class _Blower1State_Type(Integer32):
    """Custom type blower1State based on Integer32"""
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
        *(("bad", 3),
          ("good", 1),
          ("unknown", 0),
          ("warning", 2))
    )


_Blower1State_Type.__name__ = "Integer32"
_Blower1State_Object = MibScalar
blower1State = _Blower1State_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 3, 10),
    _Blower1State_Type()
)
blower1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blower1State.setStatus("mandatory")


class _Blower2State_Type(Integer32):
    """Custom type blower2State based on Integer32"""
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
        *(("bad", 3),
          ("good", 1),
          ("unknown", 0),
          ("warning", 2))
    )


_Blower2State_Type.__name__ = "Integer32"
_Blower2State_Object = MibScalar
blower2State = _Blower2State_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 3, 11),
    _Blower2State_Type()
)
blower2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blower2State.setStatus("mandatory")
_PowerModuleHealth_ObjectIdentity = ObjectIdentity
powerModuleHealth = _PowerModuleHealth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 4)
)
_PowerModuleHealthTable_Object = MibTable
powerModuleHealthTable = _PowerModuleHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 4, 1)
)
if mibBuilder.loadTexts:
    powerModuleHealthTable.setStatus("mandatory")
_PowerModuleHealthEntry_Object = MibTableRow
powerModuleHealthEntry = _PowerModuleHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 4, 1, 1)
)
powerModuleHealthEntry.setIndexNames(
    (0, "BLADE-MIB", "powerModuleIndex"),
)
if mibBuilder.loadTexts:
    powerModuleHealthEntry.setStatus("mandatory")
_PowerModuleIndex_Type = Integer32
_PowerModuleIndex_Object = MibTableColumn
powerModuleIndex = _PowerModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 4, 1, 1, 1),
    _PowerModuleIndex_Type()
)
powerModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerModuleIndex.setStatus("mandatory")


class _PowerModuleExists_Type(Integer32):
    """Custom type powerModuleExists based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_PowerModuleExists_Type.__name__ = "Integer32"
_PowerModuleExists_Object = MibTableColumn
powerModuleExists = _PowerModuleExists_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 4, 1, 1, 2),
    _PowerModuleExists_Type()
)
powerModuleExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerModuleExists.setStatus("mandatory")


class _PowerModuleState_Type(Integer32):
    """Custom type powerModuleState based on Integer32"""
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
        *(("good", 1),
          ("notAvailable", 3),
          ("unknown", 0),
          ("warning", 2))
    )


_PowerModuleState_Type.__name__ = "Integer32"
_PowerModuleState_Object = MibTableColumn
powerModuleState = _PowerModuleState_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 4, 1, 1, 3),
    _PowerModuleState_Type()
)
powerModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerModuleState.setStatus("mandatory")
_PowerModuleDetails_Type = OctetString
_PowerModuleDetails_Object = MibTableColumn
powerModuleDetails = _PowerModuleDetails_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 4, 1, 1, 4),
    _PowerModuleDetails_Type()
)
powerModuleDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerModuleDetails.setStatus("mandatory")
_SpStatus_ObjectIdentity = ObjectIdentity
spStatus = _SpStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 5)
)
_MmBistAndChassisStatus_ObjectIdentity = ObjectIdentity
mmBistAndChassisStatus = _MmBistAndChassisStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 5, 2)
)


class _BistSdram_Type(Integer32):
    """Custom type bistSdram based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("testFailed", 1),
          ("testSucceeded", 0))
    )


_BistSdram_Type.__name__ = "Integer32"
_BistSdram_Object = MibScalar
bistSdram = _BistSdram_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 5, 2, 1),
    _BistSdram_Type()
)
bistSdram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bistSdram.setStatus("mandatory")


class _BistRs485Port1_Type(Integer32):
    """Custom type bistRs485Port1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("testFailed", 1),
          ("testSucceeded", 0))
    )


_BistRs485Port1_Type.__name__ = "Integer32"
_BistRs485Port1_Object = MibScalar
bistRs485Port1 = _BistRs485Port1_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 5, 2, 2),
    _BistRs485Port1_Type()
)
bistRs485Port1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bistRs485Port1.setStatus("mandatory")


class _BistRs485Port2_Type(Integer32):
    """Custom type bistRs485Port2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("testFailed", 1),
          ("testSucceeded", 0))
    )


_BistRs485Port2_Type.__name__ = "Integer32"
_BistRs485Port2_Object = MibScalar
bistRs485Port2 = _BistRs485Port2_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 5, 2, 3),
    _BistRs485Port2_Type()
)
bistRs485Port2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bistRs485Port2.setStatus("mandatory")


class _BistNvram_Type(Integer32):
    """Custom type bistNvram based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("testFailed", 1),
          ("testSucceeded", 0))
    )


_BistNvram_Type.__name__ = "Integer32"
_BistNvram_Object = MibScalar
bistNvram = _BistNvram_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 5, 2, 4),
    _BistNvram_Type()
)
bistNvram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bistNvram.setStatus("mandatory")


class _BistRtc_Type(Integer32):
    """Custom type bistRtc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("testFailed", 1),
          ("testSucceeded", 0))
    )


_BistRtc_Type.__name__ = "Integer32"
_BistRtc_Object = MibScalar
bistRtc = _BistRtc_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 5, 2, 6),
    _BistRtc_Type()
)
bistRtc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bistRtc.setStatus("mandatory")


class _BistLocalI2CBus_Type(Integer32):
    """Custom type bistLocalI2CBus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("testFailed", 1),
          ("testSucceeded", 0))
    )


_BistLocalI2CBus_Type.__name__ = "Integer32"
_BistLocalI2CBus_Object = MibScalar
bistLocalI2CBus = _BistLocalI2CBus_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 5, 2, 7),
    _BistLocalI2CBus_Type()
)
bistLocalI2CBus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bistLocalI2CBus.setStatus("mandatory")


class _BistPrimaryMainAppFlashImage_Type(Integer32):
    """Custom type bistPrimaryMainAppFlashImage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("testFailed", 1),
          ("testSucceeded", 0))
    )


_BistPrimaryMainAppFlashImage_Type.__name__ = "Integer32"
_BistPrimaryMainAppFlashImage_Object = MibScalar
bistPrimaryMainAppFlashImage = _BistPrimaryMainAppFlashImage_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 5, 2, 8),
    _BistPrimaryMainAppFlashImage_Type()
)
bistPrimaryMainAppFlashImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bistPrimaryMainAppFlashImage.setStatus("mandatory")


class _BistSecondaryMainAppFlashImage_Type(Integer32):
    """Custom type bistSecondaryMainAppFlashImage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("testFailed", 1),
          ("testSucceeded", 0))
    )


_BistSecondaryMainAppFlashImage_Type.__name__ = "Integer32"
_BistSecondaryMainAppFlashImage_Object = MibScalar
bistSecondaryMainAppFlashImage = _BistSecondaryMainAppFlashImage_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 5, 2, 9),
    _BistSecondaryMainAppFlashImage_Type()
)
bistSecondaryMainAppFlashImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bistSecondaryMainAppFlashImage.setStatus("mandatory")


class _BistBootRomFlashImage_Type(Integer32):
    """Custom type bistBootRomFlashImage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("testFailed", 1),
          ("testSucceeded", 0))
    )


_BistBootRomFlashImage_Type.__name__ = "Integer32"
_BistBootRomFlashImage_Object = MibScalar
bistBootRomFlashImage = _BistBootRomFlashImage_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 5, 2, 10),
    _BistBootRomFlashImage_Type()
)
bistBootRomFlashImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bistBootRomFlashImage.setStatus("mandatory")


class _BistEthernetPort1_Type(Integer32):
    """Custom type bistEthernetPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("testFailed", 1),
          ("testSucceeded", 0))
    )


_BistEthernetPort1_Type.__name__ = "Integer32"
_BistEthernetPort1_Object = MibScalar
bistEthernetPort1 = _BistEthernetPort1_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 5, 2, 11),
    _BistEthernetPort1_Type()
)
bistEthernetPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bistEthernetPort1.setStatus("mandatory")


class _BistEthernetPort2_Type(Integer32):
    """Custom type bistEthernetPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("testFailed", 1),
          ("testSucceeded", 0))
    )


_BistEthernetPort2_Type.__name__ = "Integer32"
_BistEthernetPort2_Object = MibScalar
bistEthernetPort2 = _BistEthernetPort2_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 5, 2, 12),
    _BistEthernetPort2_Type()
)
bistEthernetPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bistEthernetPort2.setStatus("mandatory")


class _BistInternalPCIBus_Type(Integer32):
    """Custom type bistInternalPCIBus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("testFailed", 1),
          ("testSucceeded", 0))
    )


_BistInternalPCIBus_Type.__name__ = "Integer32"
_BistInternalPCIBus_Object = MibScalar
bistInternalPCIBus = _BistInternalPCIBus_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 5, 2, 13),
    _BistInternalPCIBus_Type()
)
bistInternalPCIBus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bistInternalPCIBus.setStatus("mandatory")


class _BistExternalI2CDevices_Type(Integer32):
    """Custom type bistExternalI2CDevices based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("testFailed", 1),
          ("testSucceeded", 0))
    )


_BistExternalI2CDevices_Type.__name__ = "Integer32"
_BistExternalI2CDevices_Object = MibScalar
bistExternalI2CDevices = _BistExternalI2CDevices_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 5, 2, 14),
    _BistExternalI2CDevices_Type()
)
bistExternalI2CDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bistExternalI2CDevices.setStatus("mandatory")


class _BistUSBController_Type(Integer32):
    """Custom type bistUSBController based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("testFailed", 1),
          ("testSucceeded", 0))
    )


_BistUSBController_Type.__name__ = "Integer32"
_BistUSBController_Object = MibScalar
bistUSBController = _BistUSBController_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 5, 2, 15),
    _BistUSBController_Type()
)
bistUSBController.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bistUSBController.setStatus("mandatory")


class _BistVideoCompressorBoard_Type(Integer32):
    """Custom type bistVideoCompressorBoard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("testFailed", 1),
          ("testSucceeded", 0))
    )


_BistVideoCompressorBoard_Type.__name__ = "Integer32"
_BistVideoCompressorBoard_Object = MibScalar
bistVideoCompressorBoard = _BistVideoCompressorBoard_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 5, 2, 16),
    _BistVideoCompressorBoard_Type()
)
bistVideoCompressorBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bistVideoCompressorBoard.setStatus("mandatory")


class _BistPrimaryBus_Type(Integer32):
    """Custom type bistPrimaryBus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("testFailed", 1),
          ("testSucceeded", 0))
    )


_BistPrimaryBus_Type.__name__ = "Integer32"
_BistPrimaryBus_Object = MibScalar
bistPrimaryBus = _BistPrimaryBus_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 5, 2, 17),
    _BistPrimaryBus_Type()
)
bistPrimaryBus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bistPrimaryBus.setStatus("mandatory")


class _BistInternalEthernetSwitch_Type(Integer32):
    """Custom type bistInternalEthernetSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("testFailed", 1),
          ("testSucceeded", 0))
    )


_BistInternalEthernetSwitch_Type.__name__ = "Integer32"
_BistInternalEthernetSwitch_Object = MibScalar
bistInternalEthernetSwitch = _BistInternalEthernetSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 5, 2, 18),
    _BistInternalEthernetSwitch_Type()
)
bistInternalEthernetSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bistInternalEthernetSwitch.setStatus("mandatory")
_BistBladesInstalled_Type = OctetString
_BistBladesInstalled_Object = MibScalar
bistBladesInstalled = _BistBladesInstalled_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 5, 2, 33),
    _BistBladesInstalled_Type()
)
bistBladesInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bistBladesInstalled.setStatus("mandatory")
_BistBladesCommunicating_Type = OctetString
_BistBladesCommunicating_Object = MibScalar
bistBladesCommunicating = _BistBladesCommunicating_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 5, 2, 49),
    _BistBladesCommunicating_Type()
)
bistBladesCommunicating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bistBladesCommunicating.setStatus("mandatory")
_BistBlowersInstalled_Type = OctetString
_BistBlowersInstalled_Object = MibScalar
bistBlowersInstalled = _BistBlowersInstalled_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 5, 2, 65),
    _BistBlowersInstalled_Type()
)
bistBlowersInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bistBlowersInstalled.setStatus("mandatory")
_BistBlowersFunctional_Type = OctetString
_BistBlowersFunctional_Object = MibScalar
bistBlowersFunctional = _BistBlowersFunctional_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 5, 2, 73),
    _BistBlowersFunctional_Type()
)
bistBlowersFunctional.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bistBlowersFunctional.setStatus("mandatory")


class _BistMediaTrayInstalled_Type(Integer32):
    """Custom type bistMediaTrayInstalled based on Integer32"""
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


_BistMediaTrayInstalled_Type.__name__ = "Integer32"
_BistMediaTrayInstalled_Object = MibScalar
bistMediaTrayInstalled = _BistMediaTrayInstalled_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 5, 2, 74),
    _BistMediaTrayInstalled_Type()
)
bistMediaTrayInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bistMediaTrayInstalled.setStatus("mandatory")


class _BistMediaTrayCommunicating_Type(Integer32):
    """Custom type bistMediaTrayCommunicating based on Integer32"""
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


_BistMediaTrayCommunicating_Type.__name__ = "Integer32"
_BistMediaTrayCommunicating_Object = MibScalar
bistMediaTrayCommunicating = _BistMediaTrayCommunicating_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 5, 2, 75),
    _BistMediaTrayCommunicating_Type()
)
bistMediaTrayCommunicating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bistMediaTrayCommunicating.setStatus("mandatory")
_BistPowerModulesInstalled_Type = OctetString
_BistPowerModulesInstalled_Object = MibScalar
bistPowerModulesInstalled = _BistPowerModulesInstalled_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 5, 2, 81),
    _BistPowerModulesInstalled_Type()
)
bistPowerModulesInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bistPowerModulesInstalled.setStatus("mandatory")
_BistPowerModulesFunctional_Type = OctetString
_BistPowerModulesFunctional_Object = MibScalar
bistPowerModulesFunctional = _BistPowerModulesFunctional_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 5, 2, 89),
    _BistPowerModulesFunctional_Type()
)
bistPowerModulesFunctional.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bistPowerModulesFunctional.setStatus("mandatory")
_BistSwitchModulesInstalled_Type = OctetString
_BistSwitchModulesInstalled_Object = MibScalar
bistSwitchModulesInstalled = _BistSwitchModulesInstalled_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 5, 2, 97),
    _BistSwitchModulesInstalled_Type()
)
bistSwitchModulesInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bistSwitchModulesInstalled.setStatus("mandatory")
_BistSwitchModulesCommunicating_Type = OctetString
_BistSwitchModulesCommunicating_Object = MibScalar
bistSwitchModulesCommunicating = _BistSwitchModulesCommunicating_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 5, 2, 113),
    _BistSwitchModulesCommunicating_Type()
)
bistSwitchModulesCommunicating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bistSwitchModulesCommunicating.setStatus("mandatory")
_SystemHealth_ObjectIdentity = ObjectIdentity
systemHealth = _SystemHealth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 7)
)


class _SystemHealthStat_Type(Integer32):
    """Custom type systemHealthStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("critical", 0),
          ("nonCritical", 2),
          ("normal", 255),
          ("systemLevel", 4))
    )


_SystemHealthStat_Type.__name__ = "Integer32"
_SystemHealthStat_Object = MibScalar
systemHealthStat = _SystemHealthStat_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 7, 1),
    _SystemHealthStat_Type()
)
systemHealthStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHealthStat.setStatus("mandatory")
_SystemHealthSummaryTable_Object = MibTable
systemHealthSummaryTable = _SystemHealthSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 7, 2)
)
if mibBuilder.loadTexts:
    systemHealthSummaryTable.setStatus("mandatory")
_SystemHealthSummaryEntry_Object = MibTableRow
systemHealthSummaryEntry = _SystemHealthSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 7, 2, 1)
)
systemHealthSummaryEntry.setIndexNames(
    (0, "BLADE-MIB", "systemHealthSummaryIndex"),
)
if mibBuilder.loadTexts:
    systemHealthSummaryEntry.setStatus("mandatory")
_SystemHealthSummaryIndex_Type = Integer32
_SystemHealthSummaryIndex_Object = MibTableColumn
systemHealthSummaryIndex = _SystemHealthSummaryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 7, 2, 1, 1),
    _SystemHealthSummaryIndex_Type()
)
systemHealthSummaryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHealthSummaryIndex.setStatus("mandatory")
_SystemHealthSummarySeverity_Type = OctetString
_SystemHealthSummarySeverity_Object = MibTableColumn
systemHealthSummarySeverity = _SystemHealthSummarySeverity_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 7, 2, 1, 2),
    _SystemHealthSummarySeverity_Type()
)
systemHealthSummarySeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHealthSummarySeverity.setStatus("mandatory")
_SystemHealthSummaryDescription_Type = OctetString
_SystemHealthSummaryDescription_Object = MibTableColumn
systemHealthSummaryDescription = _SystemHealthSummaryDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 7, 2, 1, 3),
    _SystemHealthSummaryDescription_Type()
)
systemHealthSummaryDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHealthSummaryDescription.setStatus("mandatory")
_Leds_ObjectIdentity = ObjectIdentity
leds = _Leds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 8)
)
_FrontPanelLEDs_ObjectIdentity = ObjectIdentity
frontPanelLEDs = _FrontPanelLEDs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 8, 1)
)


class _SystemErrorLED_Type(Integer32):
    """Custom type systemErrorLED based on Integer32"""
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


_SystemErrorLED_Type.__name__ = "Integer32"
_SystemErrorLED_Object = MibScalar
systemErrorLED = _SystemErrorLED_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 8, 1, 1),
    _SystemErrorLED_Type()
)
systemErrorLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemErrorLED.setStatus("mandatory")


class _InformationLED_Type(Integer32):
    """Custom type informationLED based on Integer32"""
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


_InformationLED_Type.__name__ = "Integer32"
_InformationLED_Object = MibScalar
informationLED = _InformationLED_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 8, 1, 2),
    _InformationLED_Type()
)
informationLED.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    informationLED.setStatus("mandatory")


class _TemperatureLED_Type(Integer32):
    """Custom type temperatureLED based on Integer32"""
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


_TemperatureLED_Type.__name__ = "Integer32"
_TemperatureLED_Object = MibScalar
temperatureLED = _TemperatureLED_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 8, 1, 3),
    _TemperatureLED_Type()
)
temperatureLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureLED.setStatus("mandatory")


class _IdentityLED_Type(Integer32):
    """Custom type identityLED based on Integer32"""
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
        *(("blinking", 2),
          ("notAvailable", 3),
          ("off", 0),
          ("on", 1))
    )


_IdentityLED_Type.__name__ = "Integer32"
_IdentityLED_Object = MibScalar
identityLED = _IdentityLED_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 8, 1, 4),
    _IdentityLED_Type()
)
identityLED.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    identityLED.setStatus("mandatory")
_BladeLEDs_ObjectIdentity = ObjectIdentity
bladeLEDs = _BladeLEDs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 8, 2)
)
_BladeLEDsTable_Object = MibTable
bladeLEDsTable = _BladeLEDsTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 8, 2, 1)
)
if mibBuilder.loadTexts:
    bladeLEDsTable.setStatus("mandatory")
_BladeLEDsEntry_Object = MibTableRow
bladeLEDsEntry = _BladeLEDsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 8, 2, 1, 1)
)
bladeLEDsEntry.setIndexNames(
    (0, "BLADE-MIB", "bladeStatusIndex"),
)
if mibBuilder.loadTexts:
    bladeLEDsEntry.setStatus("mandatory")
_LedBladeIndex_Type = Integer32
_LedBladeIndex_Object = MibTableColumn
ledBladeIndex = _LedBladeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 8, 2, 1, 1, 1),
    _LedBladeIndex_Type()
)
ledBladeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledBladeIndex.setStatus("mandatory")


class _LedBladeId_Type(Integer32):
    """Custom type ledBladeId based on Integer32"""
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
        *(("blade1", 1),
          ("blade10", 10),
          ("blade11", 11),
          ("blade12", 12),
          ("blade13", 13),
          ("blade14", 14),
          ("blade2", 2),
          ("blade3", 3),
          ("blade4", 4),
          ("blade5", 5),
          ("blade6", 6),
          ("blade7", 7),
          ("blade8", 8),
          ("blade9", 9))
    )


_LedBladeId_Type.__name__ = "Integer32"
_LedBladeId_Object = MibTableColumn
ledBladeId = _LedBladeId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 8, 2, 1, 1, 2),
    _LedBladeId_Type()
)
ledBladeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledBladeId.setStatus("mandatory")


class _LedBladeExists_Type(Integer32):
    """Custom type ledBladeExists based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_LedBladeExists_Type.__name__ = "Integer32"
_LedBladeExists_Object = MibTableColumn
ledBladeExists = _LedBladeExists_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 8, 2, 1, 1, 3),
    _LedBladeExists_Type()
)
ledBladeExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledBladeExists.setStatus("mandatory")


class _LedBladePowerState_Type(Integer32):
    """Custom type ledBladePowerState based on Integer32"""
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


_LedBladePowerState_Type.__name__ = "Integer32"
_LedBladePowerState_Object = MibTableColumn
ledBladePowerState = _LedBladePowerState_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 8, 2, 1, 1, 4),
    _LedBladePowerState_Type()
)
ledBladePowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledBladePowerState.setStatus("mandatory")


class _LedBladeHealthState_Type(Integer32):
    """Custom type ledBladeHealthState based on Integer32"""
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
        *(("bad", 3),
          ("good", 1),
          ("unknown", 0),
          ("warning", 2))
    )


_LedBladeHealthState_Type.__name__ = "Integer32"
_LedBladeHealthState_Object = MibTableColumn
ledBladeHealthState = _LedBladeHealthState_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 8, 2, 1, 1, 5),
    _LedBladeHealthState_Type()
)
ledBladeHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledBladeHealthState.setStatus("mandatory")
_LedBladeName_Type = OctetString
_LedBladeName_Object = MibTableColumn
ledBladeName = _LedBladeName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 8, 2, 1, 1, 6),
    _LedBladeName_Type()
)
ledBladeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledBladeName.setStatus("mandatory")


class _LedBladeSystemError_Type(Integer32):
    """Custom type ledBladeSystemError based on Integer32"""
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


_LedBladeSystemError_Type.__name__ = "Integer32"
_LedBladeSystemError_Object = MibTableColumn
ledBladeSystemError = _LedBladeSystemError_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 8, 2, 1, 1, 7),
    _LedBladeSystemError_Type()
)
ledBladeSystemError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledBladeSystemError.setStatus("mandatory")


class _LedBladeInformation_Type(Integer32):
    """Custom type ledBladeInformation based on Integer32"""
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


_LedBladeInformation_Type.__name__ = "Integer32"
_LedBladeInformation_Object = MibTableColumn
ledBladeInformation = _LedBladeInformation_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 8, 2, 1, 1, 8),
    _LedBladeInformation_Type()
)
ledBladeInformation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ledBladeInformation.setStatus("mandatory")


class _LedBladeKVM_Type(Integer32):
    """Custom type ledBladeKVM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blinking", 2),
          ("off", 0),
          ("on", 1))
    )


_LedBladeKVM_Type.__name__ = "Integer32"
_LedBladeKVM_Object = MibTableColumn
ledBladeKVM = _LedBladeKVM_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 8, 2, 1, 1, 9),
    _LedBladeKVM_Type()
)
ledBladeKVM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledBladeKVM.setStatus("mandatory")


class _LedBladeMediaTray_Type(Integer32):
    """Custom type ledBladeMediaTray based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blinking", 2),
          ("off", 0),
          ("on", 1))
    )


_LedBladeMediaTray_Type.__name__ = "Integer32"
_LedBladeMediaTray_Object = MibTableColumn
ledBladeMediaTray = _LedBladeMediaTray_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 8, 2, 1, 1, 10),
    _LedBladeMediaTray_Type()
)
ledBladeMediaTray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledBladeMediaTray.setStatus("mandatory")


class _LedBladeIdentity_Type(Integer32):
    """Custom type ledBladeIdentity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blinking", 2),
          ("off", 0),
          ("on", 1))
    )


_LedBladeIdentity_Type.__name__ = "Integer32"
_LedBladeIdentity_Object = MibTableColumn
ledBladeIdentity = _LedBladeIdentity_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 8, 2, 1, 1, 11),
    _LedBladeIdentity_Type()
)
ledBladeIdentity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ledBladeIdentity.setStatus("mandatory")
_TelcoPanelLEDs_ObjectIdentity = ObjectIdentity
telcoPanelLEDs = _TelcoPanelLEDs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 8, 3)
)


class _CriticalLED_Type(Integer32):
    """Custom type criticalLED based on Integer32"""
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


_CriticalLED_Type.__name__ = "Integer32"
_CriticalLED_Object = MibScalar
criticalLED = _CriticalLED_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 8, 3, 1),
    _CriticalLED_Type()
)
criticalLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    criticalLED.setStatus("mandatory")


class _MajorLED_Type(Integer32):
    """Custom type majorLED based on Integer32"""
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


_MajorLED_Type.__name__ = "Integer32"
_MajorLED_Object = MibScalar
majorLED = _MajorLED_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 8, 3, 2),
    _MajorLED_Type()
)
majorLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    majorLED.setStatus("mandatory")


class _MinorLED_Type(Integer32):
    """Custom type minorLED based on Integer32"""
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


_MinorLED_Type.__name__ = "Integer32"
_MinorLED_Object = MibScalar
minorLED = _MinorLED_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 8, 3, 3),
    _MinorLED_Type()
)
minorLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minorLED.setStatus("mandatory")


class _TelcoIdentityLED_Type(Integer32):
    """Custom type telcoIdentityLED based on Integer32"""
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
        *(("blinking", 2),
          ("notAvailable", 3),
          ("off", 0),
          ("on", 1))
    )


_TelcoIdentityLED_Type.__name__ = "Integer32"
_TelcoIdentityLED_Object = MibScalar
telcoIdentityLED = _TelcoIdentityLED_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 8, 3, 4),
    _TelcoIdentityLED_Type()
)
telcoIdentityLED.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telcoIdentityLED.setStatus("mandatory")


class _TelcoColorSel_Type(Integer32):
    """Custom type telcoColorSel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("amber", 0),
          ("red", 1))
    )


_TelcoColorSel_Type.__name__ = "Integer32"
_TelcoColorSel_Object = MibScalar
telcoColorSel = _TelcoColorSel_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 8, 3, 5),
    _TelcoColorSel_Type()
)
telcoColorSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telcoColorSel.setStatus("mandatory")


class _CriticalityAssertionMode_Type(Integer32):
    """Custom type criticalityAssertionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_CriticalityAssertionMode_Type.__name__ = "Integer32"
_CriticalityAssertionMode_Object = MibScalar
criticalityAssertionMode = _CriticalityAssertionMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 8, 3, 6),
    _CriticalityAssertionMode_Type()
)
criticalityAssertionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    criticalityAssertionMode.setStatus("mandatory")
_SmLEDs_ObjectIdentity = ObjectIdentity
smLEDs = _SmLEDs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 8, 4)
)
_SmLEDsTable_Object = MibTable
smLEDsTable = _SmLEDsTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 8, 4, 1)
)
if mibBuilder.loadTexts:
    smLEDsTable.setStatus("mandatory")
_SmLEDsEntry_Object = MibTableRow
smLEDsEntry = _SmLEDsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 8, 4, 1, 1)
)
smLEDsEntry.setIndexNames(
    (0, "BLADE-MIB", "ledSMIndex"),
)
if mibBuilder.loadTexts:
    smLEDsEntry.setStatus("mandatory")


class _LedSMIndex_Type(Integer32):
    """Custom type ledSMIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_LedSMIndex_Type.__name__ = "Integer32"
_LedSMIndex_Object = MibTableColumn
ledSMIndex = _LedSMIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 8, 4, 1, 1, 1),
    _LedSMIndex_Type()
)
ledSMIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledSMIndex.setStatus("mandatory")


class _LedSMLEDs_Type(OctetString):
    """Custom type ledSMLEDs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_LedSMLEDs_Type.__name__ = "OctetString"
_LedSMLEDs_Object = MibTableColumn
ledSMLEDs = _LedSMLEDs_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 8, 4, 1, 1, 2),
    _LedSMLEDs_Type()
)
ledSMLEDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledSMLEDs.setStatus("mandatory")
_TelcoSystemHealth_ObjectIdentity = ObjectIdentity
telcoSystemHealth = _TelcoSystemHealth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 9)
)


class _TelcoSystemHealthStat_Type(Integer32):
    """Custom type telcoSystemHealthStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("critical", 5),
          ("critical-power", 6),
          ("major", 3),
          ("major-power", 4),
          ("minor", 1),
          ("minor-power", 2),
          ("normal", 255))
    )


_TelcoSystemHealthStat_Type.__name__ = "Integer32"
_TelcoSystemHealthStat_Object = MibScalar
telcoSystemHealthStat = _TelcoSystemHealthStat_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 9, 1),
    _TelcoSystemHealthStat_Type()
)
telcoSystemHealthStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telcoSystemHealthStat.setStatus("mandatory")
_TelcoSystemHealthSummaryTable_Object = MibTable
telcoSystemHealthSummaryTable = _TelcoSystemHealthSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 9, 2)
)
if mibBuilder.loadTexts:
    telcoSystemHealthSummaryTable.setStatus("mandatory")
_TelcoSystemHealthSummaryEntry_Object = MibTableRow
telcoSystemHealthSummaryEntry = _TelcoSystemHealthSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 9, 2, 1)
)
telcoSystemHealthSummaryEntry.setIndexNames(
    (0, "BLADE-MIB", "telcoSystemHealthSummaryIndex"),
)
if mibBuilder.loadTexts:
    telcoSystemHealthSummaryEntry.setStatus("mandatory")
_TelcoSystemHealthSummaryIndex_Type = Integer32
_TelcoSystemHealthSummaryIndex_Object = MibTableColumn
telcoSystemHealthSummaryIndex = _TelcoSystemHealthSummaryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 9, 2, 1, 1),
    _TelcoSystemHealthSummaryIndex_Type()
)
telcoSystemHealthSummaryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telcoSystemHealthSummaryIndex.setStatus("mandatory")
_TelcoSystemHealthSummarySeverity_Type = OctetString
_TelcoSystemHealthSummarySeverity_Object = MibTableColumn
telcoSystemHealthSummarySeverity = _TelcoSystemHealthSummarySeverity_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 9, 2, 1, 2),
    _TelcoSystemHealthSummarySeverity_Type()
)
telcoSystemHealthSummarySeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telcoSystemHealthSummarySeverity.setStatus("mandatory")
_TelcoSystemHealthSummaryDescription_Type = OctetString
_TelcoSystemHealthSummaryDescription_Object = MibTableColumn
telcoSystemHealthSummaryDescription = _TelcoSystemHealthSummaryDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 9, 2, 1, 3),
    _TelcoSystemHealthSummaryDescription_Type()
)
telcoSystemHealthSummaryDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telcoSystemHealthSummaryDescription.setStatus("mandatory")
_TelcoSystemHealthSummaryEventName_Type = Integer32
_TelcoSystemHealthSummaryEventName_Object = MibTableColumn
telcoSystemHealthSummaryEventName = _TelcoSystemHealthSummaryEventName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 9, 2, 1, 4),
    _TelcoSystemHealthSummaryEventName_Type()
)
telcoSystemHealthSummaryEventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telcoSystemHealthSummaryEventName.setStatus("mandatory")
_TelcoSystemHealthSummaryEventKeyID_Type = OctetString
_TelcoSystemHealthSummaryEventKeyID_Object = MibTableColumn
telcoSystemHealthSummaryEventKeyID = _TelcoSystemHealthSummaryEventKeyID_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 9, 2, 1, 5),
    _TelcoSystemHealthSummaryEventKeyID_Type()
)
telcoSystemHealthSummaryEventKeyID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telcoSystemHealthSummaryEventKeyID.setStatus("mandatory")


class _TelcoSystemHealthSummaryAcknowledge_Type(Integer32):
    """Custom type telcoSystemHealthSummaryAcknowledge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("acknowledged", 1),
          ("unacknowledged", 0))
    )


_TelcoSystemHealthSummaryAcknowledge_Type.__name__ = "Integer32"
_TelcoSystemHealthSummaryAcknowledge_Object = MibTableColumn
telcoSystemHealthSummaryAcknowledge = _TelcoSystemHealthSummaryAcknowledge_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 9, 2, 1, 6),
    _TelcoSystemHealthSummaryAcknowledge_Type()
)
telcoSystemHealthSummaryAcknowledge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telcoSystemHealthSummaryAcknowledge.setStatus("mandatory")
_FuelGauge_ObjectIdentity = ObjectIdentity
fuelGauge = _FuelGauge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 10)
)
_FuelGaugeInformation_ObjectIdentity = ObjectIdentity
fuelGaugeInformation = _FuelGaugeInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 10, 1)
)
_FuelGaugeTable_Object = MibTable
fuelGaugeTable = _FuelGaugeTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 10, 1, 1)
)
if mibBuilder.loadTexts:
    fuelGaugeTable.setStatus("mandatory")
_FuelGaugeEntry_Object = MibTableRow
fuelGaugeEntry = _FuelGaugeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 10, 1, 1, 1)
)
fuelGaugeEntry.setIndexNames(
    (0, "BLADE-MIB", "fuelGaugeIndex"),
)
if mibBuilder.loadTexts:
    fuelGaugeEntry.setStatus("mandatory")
_FuelGaugeIndex_Type = Integer32
_FuelGaugeIndex_Object = MibTableColumn
fuelGaugeIndex = _FuelGaugeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 10, 1, 1, 1, 1),
    _FuelGaugeIndex_Type()
)
fuelGaugeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fuelGaugeIndex.setStatus("mandatory")


class _FuelGaugePowerDomainNumber_Type(Integer32):
    """Custom type fuelGaugePowerDomainNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("powerDomain1", 1),
          ("powerDomain2", 2))
    )


_FuelGaugePowerDomainNumber_Type.__name__ = "Integer32"
_FuelGaugePowerDomainNumber_Object = MibTableColumn
fuelGaugePowerDomainNumber = _FuelGaugePowerDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 10, 1, 1, 1, 2),
    _FuelGaugePowerDomainNumber_Type()
)
fuelGaugePowerDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fuelGaugePowerDomainNumber.setStatus("mandatory")
_FuelGaugeStatus_Type = OctetString
_FuelGaugeStatus_Object = MibTableColumn
fuelGaugeStatus = _FuelGaugeStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 10, 1, 1, 1, 3),
    _FuelGaugeStatus_Type()
)
fuelGaugeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fuelGaugeStatus.setStatus("mandatory")
_FuelGaugeFirstPowerModule_Type = OctetString
_FuelGaugeFirstPowerModule_Object = MibTableColumn
fuelGaugeFirstPowerModule = _FuelGaugeFirstPowerModule_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 10, 1, 1, 1, 4),
    _FuelGaugeFirstPowerModule_Type()
)
fuelGaugeFirstPowerModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fuelGaugeFirstPowerModule.setStatus("mandatory")
_FuelGaugeSecondPowerModule_Type = OctetString
_FuelGaugeSecondPowerModule_Object = MibTableColumn
fuelGaugeSecondPowerModule = _FuelGaugeSecondPowerModule_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 10, 1, 1, 1, 5),
    _FuelGaugeSecondPowerModule_Type()
)
fuelGaugeSecondPowerModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fuelGaugeSecondPowerModule.setStatus("mandatory")


class _FuelGaugePowerManagementPolicySetting_Type(Integer32):
    """Custom type fuelGaugePowerManagementPolicySetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonRedundant", 2),
          ("redundantWithPerformanceImpact", 1),
          ("redundantWithoutPerformanceImpact", 0))
    )


_FuelGaugePowerManagementPolicySetting_Type.__name__ = "Integer32"
_FuelGaugePowerManagementPolicySetting_Object = MibTableColumn
fuelGaugePowerManagementPolicySetting = _FuelGaugePowerManagementPolicySetting_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 10, 1, 1, 1, 6),
    _FuelGaugePowerManagementPolicySetting_Type()
)
fuelGaugePowerManagementPolicySetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fuelGaugePowerManagementPolicySetting.setStatus("mandatory")
_FuelGaugeTotalPower_Type = OctetString
_FuelGaugeTotalPower_Object = MibTableColumn
fuelGaugeTotalPower = _FuelGaugeTotalPower_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 10, 1, 1, 1, 7),
    _FuelGaugeTotalPower_Type()
)
fuelGaugeTotalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fuelGaugeTotalPower.setStatus("mandatory")
_FuelGaugeReservedPower_Type = OctetString
_FuelGaugeReservedPower_Object = MibTableColumn
fuelGaugeReservedPower = _FuelGaugeReservedPower_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 10, 1, 1, 1, 8),
    _FuelGaugeReservedPower_Type()
)
fuelGaugeReservedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fuelGaugeReservedPower.setStatus("mandatory")
_FuelGaugeRemainingPower_Type = OctetString
_FuelGaugeRemainingPower_Object = MibTableColumn
fuelGaugeRemainingPower = _FuelGaugeRemainingPower_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 10, 1, 1, 1, 9),
    _FuelGaugeRemainingPower_Type()
)
fuelGaugeRemainingPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fuelGaugeRemainingPower.setStatus("mandatory")
_FuelGaugePowerInUsed_Type = OctetString
_FuelGaugePowerInUsed_Object = MibTableColumn
fuelGaugePowerInUsed = _FuelGaugePowerInUsed_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 10, 1, 1, 1, 10),
    _FuelGaugePowerInUsed_Type()
)
fuelGaugePowerInUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fuelGaugePowerInUsed.setStatus("mandatory")
_PowerDomain1_ObjectIdentity = ObjectIdentity
powerDomain1 = _PowerDomain1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 10, 2)
)
_PowerDomain1Table_Object = MibTable
powerDomain1Table = _PowerDomain1Table_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 10, 2, 1)
)
if mibBuilder.loadTexts:
    powerDomain1Table.setStatus("mandatory")
_PowerDomain1Entry_Object = MibTableRow
powerDomain1Entry = _PowerDomain1Entry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 10, 2, 1, 1)
)
powerDomain1Entry.setIndexNames(
    (0, "BLADE-MIB", "pd1Index"),
)
if mibBuilder.loadTexts:
    powerDomain1Entry.setStatus("mandatory")
_Pd1Index_Type = Integer32
_Pd1Index_Object = MibTableColumn
pd1Index = _Pd1Index_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 10, 2, 1, 1, 1),
    _Pd1Index_Type()
)
pd1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pd1Index.setStatus("mandatory")
_Pd1BayNumber_Type = OctetString
_Pd1BayNumber_Object = MibTableColumn
pd1BayNumber = _Pd1BayNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 10, 2, 1, 1, 2),
    _Pd1BayNumber_Type()
)
pd1BayNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pd1BayNumber.setStatus("mandatory")


class _Pd1BladePrimarySlot_Type(Integer32):
    """Custom type pd1BladePrimarySlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("notApplicable", 255),
          ("yes", 1))
    )


_Pd1BladePrimarySlot_Type.__name__ = "Integer32"
_Pd1BladePrimarySlot_Object = MibTableColumn
pd1BladePrimarySlot = _Pd1BladePrimarySlot_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 10, 2, 1, 1, 3),
    _Pd1BladePrimarySlot_Type()
)
pd1BladePrimarySlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pd1BladePrimarySlot.setStatus("mandatory")


class _Pd1ModuleStatus_Type(Integer32):
    """Custom type pd1ModuleStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("insufficientPower", 0),
          ("moduleIsThrottling", 1),
          ("moduleNotThrottling", 2),
          ("notApplicable", 255))
    )


_Pd1ModuleStatus_Type.__name__ = "Integer32"
_Pd1ModuleStatus_Object = MibTableColumn
pd1ModuleStatus = _Pd1ModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 10, 2, 1, 1, 4),
    _Pd1ModuleStatus_Type()
)
pd1ModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pd1ModuleStatus.setStatus("mandatory")
_Pd1ModuleName_Type = OctetString
_Pd1ModuleName_Object = MibTableColumn
pd1ModuleName = _Pd1ModuleName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 10, 2, 1, 1, 5),
    _Pd1ModuleName_Type()
)
pd1ModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pd1ModuleName.setStatus("mandatory")


class _Pd1ModuleState_Type(Integer32):
    """Custom type pd1ModuleState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 255),
          ("notPresent", 2),
          ("on", 1),
          ("standby", 0))
    )


_Pd1ModuleState_Type.__name__ = "Integer32"
_Pd1ModuleState_Object = MibTableColumn
pd1ModuleState = _Pd1ModuleState_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 10, 2, 1, 1, 6),
    _Pd1ModuleState_Type()
)
pd1ModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pd1ModuleState.setStatus("mandatory")
_Pd1ModuleAllocatedPowerCurrent_Type = OctetString
_Pd1ModuleAllocatedPowerCurrent_Object = MibTableColumn
pd1ModuleAllocatedPowerCurrent = _Pd1ModuleAllocatedPowerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 10, 2, 1, 1, 7),
    _Pd1ModuleAllocatedPowerCurrent_Type()
)
pd1ModuleAllocatedPowerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pd1ModuleAllocatedPowerCurrent.setStatus("mandatory")
_Pd1ModuleAllocatedPowerMax_Type = OctetString
_Pd1ModuleAllocatedPowerMax_Object = MibTableColumn
pd1ModuleAllocatedPowerMax = _Pd1ModuleAllocatedPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 10, 2, 1, 1, 8),
    _Pd1ModuleAllocatedPowerMax_Type()
)
pd1ModuleAllocatedPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pd1ModuleAllocatedPowerMax.setStatus("mandatory")
_Pd1ModuleAllocatedPowerMin_Type = OctetString
_Pd1ModuleAllocatedPowerMin_Object = MibTableColumn
pd1ModuleAllocatedPowerMin = _Pd1ModuleAllocatedPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 10, 2, 1, 1, 9),
    _Pd1ModuleAllocatedPowerMin_Type()
)
pd1ModuleAllocatedPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pd1ModuleAllocatedPowerMin.setStatus("mandatory")
_Pd1ModuleCPUDutyCycles_Type = OctetString
_Pd1ModuleCPUDutyCycles_Object = MibTableColumn
pd1ModuleCPUDutyCycles = _Pd1ModuleCPUDutyCycles_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 10, 2, 1, 1, 10),
    _Pd1ModuleCPUDutyCycles_Type()
)
pd1ModuleCPUDutyCycles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pd1ModuleCPUDutyCycles.setStatus("mandatory")


class _Pd1ModuleThrottle_Type(Integer32):
    """Custom type pd1ModuleThrottle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("notApplicable", 255),
          ("yes", 1))
    )


_Pd1ModuleThrottle_Type.__name__ = "Integer32"
_Pd1ModuleThrottle_Object = MibTableColumn
pd1ModuleThrottle = _Pd1ModuleThrottle_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 10, 2, 1, 1, 11),
    _Pd1ModuleThrottle_Type()
)
pd1ModuleThrottle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pd1ModuleThrottle.setStatus("mandatory")
_PowerDomain2_ObjectIdentity = ObjectIdentity
powerDomain2 = _PowerDomain2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 10, 3)
)
_PowerDomain2Table_Object = MibTable
powerDomain2Table = _PowerDomain2Table_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 10, 3, 1)
)
if mibBuilder.loadTexts:
    powerDomain2Table.setStatus("mandatory")
_PowerDomain2Entry_Object = MibTableRow
powerDomain2Entry = _PowerDomain2Entry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 10, 3, 1, 1)
)
powerDomain2Entry.setIndexNames(
    (0, "BLADE-MIB", "pd2Index"),
)
if mibBuilder.loadTexts:
    powerDomain2Entry.setStatus("mandatory")
_Pd2Index_Type = Integer32
_Pd2Index_Object = MibTableColumn
pd2Index = _Pd2Index_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 10, 3, 1, 1, 1),
    _Pd2Index_Type()
)
pd2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pd2Index.setStatus("mandatory")
_Pd2BayNumber_Type = OctetString
_Pd2BayNumber_Object = MibTableColumn
pd2BayNumber = _Pd2BayNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 10, 3, 1, 1, 2),
    _Pd2BayNumber_Type()
)
pd2BayNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pd2BayNumber.setStatus("mandatory")


class _Pd2BladePrimarySlot_Type(Integer32):
    """Custom type pd2BladePrimarySlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("notApplicable", 255),
          ("yes", 1))
    )


_Pd2BladePrimarySlot_Type.__name__ = "Integer32"
_Pd2BladePrimarySlot_Object = MibTableColumn
pd2BladePrimarySlot = _Pd2BladePrimarySlot_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 10, 3, 1, 1, 3),
    _Pd2BladePrimarySlot_Type()
)
pd2BladePrimarySlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pd2BladePrimarySlot.setStatus("mandatory")


class _Pd2ModuleStatus_Type(Integer32):
    """Custom type pd2ModuleStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("insufficientPower", 0),
          ("moduleIsThrottling", 1),
          ("moduleNotThrottling", 2),
          ("notApplicable", 255))
    )


_Pd2ModuleStatus_Type.__name__ = "Integer32"
_Pd2ModuleStatus_Object = MibTableColumn
pd2ModuleStatus = _Pd2ModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 10, 3, 1, 1, 4),
    _Pd2ModuleStatus_Type()
)
pd2ModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pd2ModuleStatus.setStatus("mandatory")
_Pd2ModuleName_Type = OctetString
_Pd2ModuleName_Object = MibTableColumn
pd2ModuleName = _Pd2ModuleName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 10, 3, 1, 1, 5),
    _Pd2ModuleName_Type()
)
pd2ModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pd2ModuleName.setStatus("mandatory")


class _Pd2ModuleState_Type(Integer32):
    """Custom type pd2ModuleState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 255),
          ("notPresent", 2),
          ("on", 1),
          ("standby", 0))
    )


_Pd2ModuleState_Type.__name__ = "Integer32"
_Pd2ModuleState_Object = MibTableColumn
pd2ModuleState = _Pd2ModuleState_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 10, 3, 1, 1, 6),
    _Pd2ModuleState_Type()
)
pd2ModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pd2ModuleState.setStatus("mandatory")
_Pd2ModuleAllocatedPowerCurrent_Type = OctetString
_Pd2ModuleAllocatedPowerCurrent_Object = MibTableColumn
pd2ModuleAllocatedPowerCurrent = _Pd2ModuleAllocatedPowerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 10, 3, 1, 1, 7),
    _Pd2ModuleAllocatedPowerCurrent_Type()
)
pd2ModuleAllocatedPowerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pd2ModuleAllocatedPowerCurrent.setStatus("mandatory")
_Pd2ModuleAllocatedPowerMax_Type = OctetString
_Pd2ModuleAllocatedPowerMax_Object = MibTableColumn
pd2ModuleAllocatedPowerMax = _Pd2ModuleAllocatedPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 10, 3, 1, 1, 8),
    _Pd2ModuleAllocatedPowerMax_Type()
)
pd2ModuleAllocatedPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pd2ModuleAllocatedPowerMax.setStatus("mandatory")
_Pd2ModuleAllocatedPowerMin_Type = OctetString
_Pd2ModuleAllocatedPowerMin_Object = MibTableColumn
pd2ModuleAllocatedPowerMin = _Pd2ModuleAllocatedPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 10, 3, 1, 1, 9),
    _Pd2ModuleAllocatedPowerMin_Type()
)
pd2ModuleAllocatedPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pd2ModuleAllocatedPowerMin.setStatus("mandatory")
_Pd2ModuleCPUDutyCycles_Type = OctetString
_Pd2ModuleCPUDutyCycles_Object = MibTableColumn
pd2ModuleCPUDutyCycles = _Pd2ModuleCPUDutyCycles_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 10, 3, 1, 1, 10),
    _Pd2ModuleCPUDutyCycles_Type()
)
pd2ModuleCPUDutyCycles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pd2ModuleCPUDutyCycles.setStatus("mandatory")


class _Pd2ModuleThrottle_Type(Integer32):
    """Custom type pd2ModuleThrottle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("notApplicable", 255),
          ("yes", 1))
    )


_Pd2ModuleThrottle_Type.__name__ = "Integer32"
_Pd2ModuleThrottle_Object = MibTableColumn
pd2ModuleThrottle = _Pd2ModuleThrottle_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 10, 3, 1, 1, 11),
    _Pd2ModuleThrottle_Type()
)
pd2ModuleThrottle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pd2ModuleThrottle.setStatus("mandatory")
_MonitorThresholds_ObjectIdentity = ObjectIdentity
monitorThresholds = _MonitorThresholds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 20)
)
_VoltageThresholds_ObjectIdentity = ObjectIdentity
voltageThresholds = _VoltageThresholds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 20, 2)
)
_VoltageThresholdsTable_Object = MibTable
voltageThresholdsTable = _VoltageThresholdsTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 20, 2, 1)
)
if mibBuilder.loadTexts:
    voltageThresholdsTable.setStatus("mandatory")
_VoltageThresholdsEntry_Object = MibTableRow
voltageThresholdsEntry = _VoltageThresholdsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 20, 2, 1, 1)
)
voltageThresholdsEntry.setIndexNames(
    (0, "BLADE-MIB", "voltageThresholdEntryIndex"),
)
if mibBuilder.loadTexts:
    voltageThresholdsEntry.setStatus("mandatory")


class _VoltageThresholdEntryIndex_Type(Integer32):
    """Custom type voltageThresholdEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VoltageThresholdEntryIndex_Type.__name__ = "Integer32"
_VoltageThresholdEntryIndex_Object = MibTableColumn
voltageThresholdEntryIndex = _VoltageThresholdEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 20, 2, 1, 1, 1),
    _VoltageThresholdEntryIndex_Type()
)
voltageThresholdEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageThresholdEntryIndex.setStatus("mandatory")


class _VoltageThresholdEntryName_Type(OctetString):
    """Custom type voltageThresholdEntryName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VoltageThresholdEntryName_Type.__name__ = "OctetString"
_VoltageThresholdEntryName_Object = MibTableColumn
voltageThresholdEntryName = _VoltageThresholdEntryName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 20, 2, 1, 1, 2),
    _VoltageThresholdEntryName_Type()
)
voltageThresholdEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageThresholdEntryName.setStatus("mandatory")
_VoltageThresholdEntryCurrentValue_Type = OctetString
_VoltageThresholdEntryCurrentValue_Object = MibTableColumn
voltageThresholdEntryCurrentValue = _VoltageThresholdEntryCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 20, 2, 1, 1, 3),
    _VoltageThresholdEntryCurrentValue_Type()
)
voltageThresholdEntryCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageThresholdEntryCurrentValue.setStatus("mandatory")
_VoltageThresholdEntryWarningHighValue_Type = OctetString
_VoltageThresholdEntryWarningHighValue_Object = MibTableColumn
voltageThresholdEntryWarningHighValue = _VoltageThresholdEntryWarningHighValue_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 20, 2, 1, 1, 6),
    _VoltageThresholdEntryWarningHighValue_Type()
)
voltageThresholdEntryWarningHighValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageThresholdEntryWarningHighValue.setStatus("mandatory")
_VoltageThresholdEntryWarningResetHighValue_Type = OctetString
_VoltageThresholdEntryWarningResetHighValue_Object = MibTableColumn
voltageThresholdEntryWarningResetHighValue = _VoltageThresholdEntryWarningResetHighValue_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 20, 2, 1, 1, 7),
    _VoltageThresholdEntryWarningResetHighValue_Type()
)
voltageThresholdEntryWarningResetHighValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageThresholdEntryWarningResetHighValue.setStatus("mandatory")
_VoltageThresholdEntryWarningLowValue_Type = OctetString
_VoltageThresholdEntryWarningLowValue_Object = MibTableColumn
voltageThresholdEntryWarningLowValue = _VoltageThresholdEntryWarningLowValue_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 20, 2, 1, 1, 10),
    _VoltageThresholdEntryWarningLowValue_Type()
)
voltageThresholdEntryWarningLowValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageThresholdEntryWarningLowValue.setStatus("mandatory")
_VoltageThresholdEntryWarningResetLowValue_Type = OctetString
_VoltageThresholdEntryWarningResetLowValue_Object = MibTableColumn
voltageThresholdEntryWarningResetLowValue = _VoltageThresholdEntryWarningResetLowValue_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 20, 2, 1, 1, 11),
    _VoltageThresholdEntryWarningResetLowValue_Type()
)
voltageThresholdEntryWarningResetLowValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageThresholdEntryWarningResetLowValue.setStatus("mandatory")
_VpdInformation_ObjectIdentity = ObjectIdentity
vpdInformation = _VpdInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21)
)
_ChassisVpd_ObjectIdentity = ObjectIdentity
chassisVpd = _ChassisVpd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 1)
)
_BladeCenterVpd_ObjectIdentity = ObjectIdentity
bladeCenterVpd = _BladeCenterVpd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 1, 1)
)
_BladeCenterVpdMachineType_Type = OctetString
_BladeCenterVpdMachineType_Object = MibScalar
bladeCenterVpdMachineType = _BladeCenterVpdMachineType_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 1, 1, 1),
    _BladeCenterVpdMachineType_Type()
)
bladeCenterVpdMachineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeCenterVpdMachineType.setStatus("mandatory")
_BladeCenterVpdMachineModel_Type = OctetString
_BladeCenterVpdMachineModel_Object = MibScalar
bladeCenterVpdMachineModel = _BladeCenterVpdMachineModel_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 1, 1, 2),
    _BladeCenterVpdMachineModel_Type()
)
bladeCenterVpdMachineModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeCenterVpdMachineModel.setStatus("mandatory")
_BladeCenterSerialNumber_Type = OctetString
_BladeCenterSerialNumber_Object = MibScalar
bladeCenterSerialNumber = _BladeCenterSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 1, 1, 3),
    _BladeCenterSerialNumber_Type()
)
bladeCenterSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeCenterSerialNumber.setStatus("mandatory")
_BladeCenterUUID_Type = OctetString
_BladeCenterUUID_Object = MibScalar
bladeCenterUUID = _BladeCenterUUID_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 1, 1, 4),
    _BladeCenterUUID_Type()
)
bladeCenterUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeCenterUUID.setStatus("mandatory")
_BladeCenterManufacturingId_Type = OctetString
_BladeCenterManufacturingId_Object = MibScalar
bladeCenterManufacturingId = _BladeCenterManufacturingId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 1, 1, 5),
    _BladeCenterManufacturingId_Type()
)
bladeCenterManufacturingId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeCenterManufacturingId.setStatus("mandatory")
_BladeCenterHardwareRevision_Type = Integer32
_BladeCenterHardwareRevision_Object = MibScalar
bladeCenterHardwareRevision = _BladeCenterHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 1, 1, 6),
    _BladeCenterHardwareRevision_Type()
)
bladeCenterHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeCenterHardwareRevision.setStatus("mandatory")
_BladeCenterFruNumber_Type = OctetString
_BladeCenterFruNumber_Object = MibScalar
bladeCenterFruNumber = _BladeCenterFruNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 1, 1, 7),
    _BladeCenterFruNumber_Type()
)
bladeCenterFruNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeCenterFruNumber.setStatus("mandatory")
_BladeCenterManufDate_Type = OctetString
_BladeCenterManufDate_Object = MibScalar
bladeCenterManufDate = _BladeCenterManufDate_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 1, 1, 8),
    _BladeCenterManufDate_Type()
)
bladeCenterManufDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeCenterManufDate.setStatus("mandatory")
_BladeCenterPartNumber_Type = OctetString
_BladeCenterPartNumber_Object = MibScalar
bladeCenterPartNumber = _BladeCenterPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 1, 1, 9),
    _BladeCenterPartNumber_Type()
)
bladeCenterPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeCenterPartNumber.setStatus("mandatory")
_BladeCenterFruSerial_Type = OctetString
_BladeCenterFruSerial_Object = MibScalar
bladeCenterFruSerial = _BladeCenterFruSerial_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 1, 1, 10),
    _BladeCenterFruSerial_Type()
)
bladeCenterFruSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeCenterFruSerial.setStatus("mandatory")
_MmHardwareVpd_ObjectIdentity = ObjectIdentity
mmHardwareVpd = _MmHardwareVpd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 2)
)
_MmHardwareVpdTable_Object = MibTable
mmHardwareVpdTable = _MmHardwareVpdTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 2, 1)
)
if mibBuilder.loadTexts:
    mmHardwareVpdTable.setStatus("mandatory")
_MmHardwareVpdEntry_Object = MibTableRow
mmHardwareVpdEntry = _MmHardwareVpdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 2, 1, 1)
)
mmHardwareVpdEntry.setIndexNames(
    (0, "BLADE-MIB", "mmHardwareVpdIndex"),
)
if mibBuilder.loadTexts:
    mmHardwareVpdEntry.setStatus("mandatory")
_MmHardwareVpdIndex_Type = Integer32
_MmHardwareVpdIndex_Object = MibTableColumn
mmHardwareVpdIndex = _MmHardwareVpdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 2, 1, 1, 1),
    _MmHardwareVpdIndex_Type()
)
mmHardwareVpdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmHardwareVpdIndex.setStatus("mandatory")
_MmHardwareVpdBayNumber_Type = OctetString
_MmHardwareVpdBayNumber_Object = MibTableColumn
mmHardwareVpdBayNumber = _MmHardwareVpdBayNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 2, 1, 1, 2),
    _MmHardwareVpdBayNumber_Type()
)
mmHardwareVpdBayNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmHardwareVpdBayNumber.setStatus("mandatory")
_MmHardwareVpdManufacturingId_Type = OctetString
_MmHardwareVpdManufacturingId_Object = MibTableColumn
mmHardwareVpdManufacturingId = _MmHardwareVpdManufacturingId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 2, 1, 1, 3),
    _MmHardwareVpdManufacturingId_Type()
)
mmHardwareVpdManufacturingId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmHardwareVpdManufacturingId.setStatus("mandatory")
_MmHardwareVpdFruNumber_Type = OctetString
_MmHardwareVpdFruNumber_Object = MibTableColumn
mmHardwareVpdFruNumber = _MmHardwareVpdFruNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 2, 1, 1, 4),
    _MmHardwareVpdFruNumber_Type()
)
mmHardwareVpdFruNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmHardwareVpdFruNumber.setStatus("mandatory")
_MmHardwareVpdHardwareRevision_Type = Integer32
_MmHardwareVpdHardwareRevision_Object = MibTableColumn
mmHardwareVpdHardwareRevision = _MmHardwareVpdHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 2, 1, 1, 5),
    _MmHardwareVpdHardwareRevision_Type()
)
mmHardwareVpdHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmHardwareVpdHardwareRevision.setStatus("mandatory")
_MmHardwareVpdUuid_Type = OctetString
_MmHardwareVpdUuid_Object = MibTableColumn
mmHardwareVpdUuid = _MmHardwareVpdUuid_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 2, 1, 1, 6),
    _MmHardwareVpdUuid_Type()
)
mmHardwareVpdUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmHardwareVpdUuid.setStatus("mandatory")
_MmHardwareVpdManufDate_Type = OctetString
_MmHardwareVpdManufDate_Object = MibTableColumn
mmHardwareVpdManufDate = _MmHardwareVpdManufDate_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 2, 1, 1, 7),
    _MmHardwareVpdManufDate_Type()
)
mmHardwareVpdManufDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmHardwareVpdManufDate.setStatus("mandatory")
_MmHardwareVpdPartNumber_Type = OctetString
_MmHardwareVpdPartNumber_Object = MibTableColumn
mmHardwareVpdPartNumber = _MmHardwareVpdPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 2, 1, 1, 8),
    _MmHardwareVpdPartNumber_Type()
)
mmHardwareVpdPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmHardwareVpdPartNumber.setStatus("mandatory")
_MmHardwareVpdFruSerial_Type = OctetString
_MmHardwareVpdFruSerial_Object = MibTableColumn
mmHardwareVpdFruSerial = _MmHardwareVpdFruSerial_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 2, 1, 1, 9),
    _MmHardwareVpdFruSerial_Type()
)
mmHardwareVpdFruSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmHardwareVpdFruSerial.setStatus("mandatory")
_MmFirmwareVpd_ObjectIdentity = ObjectIdentity
mmFirmwareVpd = _MmFirmwareVpd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 3)
)
_MmMainApplVpdTable_Object = MibTable
mmMainApplVpdTable = _MmMainApplVpdTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 3, 1)
)
if mibBuilder.loadTexts:
    mmMainApplVpdTable.setStatus("mandatory")
_MmMainApplVpdEntry_Object = MibTableRow
mmMainApplVpdEntry = _MmMainApplVpdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 3, 1, 1)
)
mmMainApplVpdEntry.setIndexNames(
    (0, "BLADE-MIB", "mmMainApplVpdIndex"),
)
if mibBuilder.loadTexts:
    mmMainApplVpdEntry.setStatus("mandatory")
_MmMainApplVpdIndex_Type = Integer32
_MmMainApplVpdIndex_Object = MibTableColumn
mmMainApplVpdIndex = _MmMainApplVpdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 3, 1, 1, 1),
    _MmMainApplVpdIndex_Type()
)
mmMainApplVpdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmMainApplVpdIndex.setStatus("mandatory")
_MmMainApplVpdName_Type = OctetString
_MmMainApplVpdName_Object = MibTableColumn
mmMainApplVpdName = _MmMainApplVpdName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 3, 1, 1, 2),
    _MmMainApplVpdName_Type()
)
mmMainApplVpdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmMainApplVpdName.setStatus("mandatory")
_MmMainApplVpdBuildId_Type = OctetString
_MmMainApplVpdBuildId_Object = MibTableColumn
mmMainApplVpdBuildId = _MmMainApplVpdBuildId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 3, 1, 1, 3),
    _MmMainApplVpdBuildId_Type()
)
mmMainApplVpdBuildId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmMainApplVpdBuildId.setStatus("mandatory")
_MmMainApplVpdRevisonNumber_Type = OctetString
_MmMainApplVpdRevisonNumber_Object = MibTableColumn
mmMainApplVpdRevisonNumber = _MmMainApplVpdRevisonNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 3, 1, 1, 4),
    _MmMainApplVpdRevisonNumber_Type()
)
mmMainApplVpdRevisonNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmMainApplVpdRevisonNumber.setStatus("mandatory")
_MmMainApplVpdFilename_Type = OctetString
_MmMainApplVpdFilename_Object = MibTableColumn
mmMainApplVpdFilename = _MmMainApplVpdFilename_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 3, 1, 1, 5),
    _MmMainApplVpdFilename_Type()
)
mmMainApplVpdFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmMainApplVpdFilename.setStatus("mandatory")
_MmMainApplVpdBuildDate_Type = OctetString
_MmMainApplVpdBuildDate_Object = MibTableColumn
mmMainApplVpdBuildDate = _MmMainApplVpdBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 3, 1, 1, 6),
    _MmMainApplVpdBuildDate_Type()
)
mmMainApplVpdBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmMainApplVpdBuildDate.setStatus("mandatory")
_MmBootROMVpdTable_Object = MibTable
mmBootROMVpdTable = _MmBootROMVpdTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 3, 2)
)
if mibBuilder.loadTexts:
    mmBootROMVpdTable.setStatus("mandatory")
_MmBootROMVpdEntry_Object = MibTableRow
mmBootROMVpdEntry = _MmBootROMVpdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 3, 2, 1)
)
mmBootROMVpdEntry.setIndexNames(
    (0, "BLADE-MIB", "mmBootROMVpdIndex"),
)
if mibBuilder.loadTexts:
    mmBootROMVpdEntry.setStatus("mandatory")
_MmBootROMVpdIndex_Type = Integer32
_MmBootROMVpdIndex_Object = MibTableColumn
mmBootROMVpdIndex = _MmBootROMVpdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 3, 2, 1, 1),
    _MmBootROMVpdIndex_Type()
)
mmBootROMVpdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmBootROMVpdIndex.setStatus("mandatory")
_MmBootROMVpdName_Type = OctetString
_MmBootROMVpdName_Object = MibTableColumn
mmBootROMVpdName = _MmBootROMVpdName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 3, 2, 1, 2),
    _MmBootROMVpdName_Type()
)
mmBootROMVpdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmBootROMVpdName.setStatus("mandatory")
_MmBootROMVpdBuildId_Type = OctetString
_MmBootROMVpdBuildId_Object = MibTableColumn
mmBootROMVpdBuildId = _MmBootROMVpdBuildId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 3, 2, 1, 3),
    _MmBootROMVpdBuildId_Type()
)
mmBootROMVpdBuildId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmBootROMVpdBuildId.setStatus("mandatory")
_MmBootROMVpdRevisonNumber_Type = OctetString
_MmBootROMVpdRevisonNumber_Object = MibTableColumn
mmBootROMVpdRevisonNumber = _MmBootROMVpdRevisonNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 3, 2, 1, 4),
    _MmBootROMVpdRevisonNumber_Type()
)
mmBootROMVpdRevisonNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmBootROMVpdRevisonNumber.setStatus("mandatory")
_MmBootROMVpdFilename_Type = OctetString
_MmBootROMVpdFilename_Object = MibTableColumn
mmBootROMVpdFilename = _MmBootROMVpdFilename_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 3, 2, 1, 5),
    _MmBootROMVpdFilename_Type()
)
mmBootROMVpdFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmBootROMVpdFilename.setStatus("mandatory")
_MmBootROMVpdBuildDate_Type = OctetString
_MmBootROMVpdBuildDate_Object = MibTableColumn
mmBootROMVpdBuildDate = _MmBootROMVpdBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 3, 2, 1, 6),
    _MmBootROMVpdBuildDate_Type()
)
mmBootROMVpdBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmBootROMVpdBuildDate.setStatus("mandatory")
_MmRemoteControlVpdTable_Object = MibTable
mmRemoteControlVpdTable = _MmRemoteControlVpdTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 3, 3)
)
if mibBuilder.loadTexts:
    mmRemoteControlVpdTable.setStatus("mandatory")
_MmRemoteControlVpdEntry_Object = MibTableRow
mmRemoteControlVpdEntry = _MmRemoteControlVpdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 3, 3, 1)
)
mmRemoteControlVpdEntry.setIndexNames(
    (0, "BLADE-MIB", "mmRemoteControlVpdIndex"),
)
if mibBuilder.loadTexts:
    mmRemoteControlVpdEntry.setStatus("mandatory")
_MmRemoteControlVpdIndex_Type = Integer32
_MmRemoteControlVpdIndex_Object = MibTableColumn
mmRemoteControlVpdIndex = _MmRemoteControlVpdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 3, 3, 1, 1),
    _MmRemoteControlVpdIndex_Type()
)
mmRemoteControlVpdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmRemoteControlVpdIndex.setStatus("mandatory")
_MmRemoteControlVpdName_Type = OctetString
_MmRemoteControlVpdName_Object = MibTableColumn
mmRemoteControlVpdName = _MmRemoteControlVpdName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 3, 3, 1, 2),
    _MmRemoteControlVpdName_Type()
)
mmRemoteControlVpdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmRemoteControlVpdName.setStatus("mandatory")
_MmRemoteControlVpdBuildId_Type = OctetString
_MmRemoteControlVpdBuildId_Object = MibTableColumn
mmRemoteControlVpdBuildId = _MmRemoteControlVpdBuildId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 3, 3, 1, 3),
    _MmRemoteControlVpdBuildId_Type()
)
mmRemoteControlVpdBuildId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmRemoteControlVpdBuildId.setStatus("mandatory")
_MmRemoteControlVpdRevisonNumber_Type = OctetString
_MmRemoteControlVpdRevisonNumber_Object = MibTableColumn
mmRemoteControlVpdRevisonNumber = _MmRemoteControlVpdRevisonNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 3, 3, 1, 4),
    _MmRemoteControlVpdRevisonNumber_Type()
)
mmRemoteControlVpdRevisonNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmRemoteControlVpdRevisonNumber.setStatus("mandatory")
_MmRemoteControlVpdFilename_Type = OctetString
_MmRemoteControlVpdFilename_Object = MibTableColumn
mmRemoteControlVpdFilename = _MmRemoteControlVpdFilename_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 3, 3, 1, 5),
    _MmRemoteControlVpdFilename_Type()
)
mmRemoteControlVpdFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmRemoteControlVpdFilename.setStatus("mandatory")
_MmRemoteControlVpdBuildDate_Type = OctetString
_MmRemoteControlVpdBuildDate_Object = MibTableColumn
mmRemoteControlVpdBuildDate = _MmRemoteControlVpdBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 3, 3, 1, 6),
    _MmRemoteControlVpdBuildDate_Type()
)
mmRemoteControlVpdBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmRemoteControlVpdBuildDate.setStatus("mandatory")
_MmPS2toUSBConvVpdTable_Object = MibTable
mmPS2toUSBConvVpdTable = _MmPS2toUSBConvVpdTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 3, 4)
)
if mibBuilder.loadTexts:
    mmPS2toUSBConvVpdTable.setStatus("mandatory")
_MmPS2toUSBConvVpdEntry_Object = MibTableRow
mmPS2toUSBConvVpdEntry = _MmPS2toUSBConvVpdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 3, 4, 1)
)
mmPS2toUSBConvVpdEntry.setIndexNames(
    (0, "BLADE-MIB", "mmPS2toUSBConvVpdIndex"),
)
if mibBuilder.loadTexts:
    mmPS2toUSBConvVpdEntry.setStatus("mandatory")
_MmPS2toUSBConvVpdIndex_Type = Integer32
_MmPS2toUSBConvVpdIndex_Object = MibTableColumn
mmPS2toUSBConvVpdIndex = _MmPS2toUSBConvVpdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 3, 4, 1, 1),
    _MmPS2toUSBConvVpdIndex_Type()
)
mmPS2toUSBConvVpdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmPS2toUSBConvVpdIndex.setStatus("mandatory")
_MmPS2toUSBConvVpdName_Type = OctetString
_MmPS2toUSBConvVpdName_Object = MibTableColumn
mmPS2toUSBConvVpdName = _MmPS2toUSBConvVpdName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 3, 4, 1, 2),
    _MmPS2toUSBConvVpdName_Type()
)
mmPS2toUSBConvVpdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmPS2toUSBConvVpdName.setStatus("mandatory")
_MmPS2toUSBConvVpdBuildId_Type = OctetString
_MmPS2toUSBConvVpdBuildId_Object = MibTableColumn
mmPS2toUSBConvVpdBuildId = _MmPS2toUSBConvVpdBuildId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 3, 4, 1, 3),
    _MmPS2toUSBConvVpdBuildId_Type()
)
mmPS2toUSBConvVpdBuildId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmPS2toUSBConvVpdBuildId.setStatus("mandatory")
_MmPS2toUSBConvVpdRevisonNumber_Type = OctetString
_MmPS2toUSBConvVpdRevisonNumber_Object = MibTableColumn
mmPS2toUSBConvVpdRevisonNumber = _MmPS2toUSBConvVpdRevisonNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 3, 4, 1, 4),
    _MmPS2toUSBConvVpdRevisonNumber_Type()
)
mmPS2toUSBConvVpdRevisonNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmPS2toUSBConvVpdRevisonNumber.setStatus("mandatory")
_MmPS2toUSBConvVpdFilename_Type = OctetString
_MmPS2toUSBConvVpdFilename_Object = MibTableColumn
mmPS2toUSBConvVpdFilename = _MmPS2toUSBConvVpdFilename_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 3, 4, 1, 5),
    _MmPS2toUSBConvVpdFilename_Type()
)
mmPS2toUSBConvVpdFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmPS2toUSBConvVpdFilename.setStatus("mandatory")
_MmPS2toUSBConvVpdBuildDate_Type = OctetString
_MmPS2toUSBConvVpdBuildDate_Object = MibTableColumn
mmPS2toUSBConvVpdBuildDate = _MmPS2toUSBConvVpdBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 3, 4, 1, 6),
    _MmPS2toUSBConvVpdBuildDate_Type()
)
mmPS2toUSBConvVpdBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmPS2toUSBConvVpdBuildDate.setStatus("mandatory")
_MmToUSBIntfVpdTable_Object = MibTable
mmToUSBIntfVpdTable = _MmToUSBIntfVpdTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 3, 5)
)
if mibBuilder.loadTexts:
    mmToUSBIntfVpdTable.setStatus("mandatory")
_MmToUSBIntfVpdEntry_Object = MibTableRow
mmToUSBIntfVpdEntry = _MmToUSBIntfVpdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 3, 5, 1)
)
mmToUSBIntfVpdEntry.setIndexNames(
    (0, "BLADE-MIB", "mmToUSBIntfVpdIndex"),
)
if mibBuilder.loadTexts:
    mmToUSBIntfVpdEntry.setStatus("mandatory")
_MmToUSBIntfVpdIndex_Type = Integer32
_MmToUSBIntfVpdIndex_Object = MibTableColumn
mmToUSBIntfVpdIndex = _MmToUSBIntfVpdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 3, 5, 1, 1),
    _MmToUSBIntfVpdIndex_Type()
)
mmToUSBIntfVpdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmToUSBIntfVpdIndex.setStatus("mandatory")
_MmToUSBIntfVpdName_Type = OctetString
_MmToUSBIntfVpdName_Object = MibTableColumn
mmToUSBIntfVpdName = _MmToUSBIntfVpdName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 3, 5, 1, 2),
    _MmToUSBIntfVpdName_Type()
)
mmToUSBIntfVpdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmToUSBIntfVpdName.setStatus("mandatory")
_MmToUSBIntfVpdBuildId_Type = OctetString
_MmToUSBIntfVpdBuildId_Object = MibTableColumn
mmToUSBIntfVpdBuildId = _MmToUSBIntfVpdBuildId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 3, 5, 1, 3),
    _MmToUSBIntfVpdBuildId_Type()
)
mmToUSBIntfVpdBuildId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmToUSBIntfVpdBuildId.setStatus("mandatory")
_MmToUSBIntfVpdRevisonNumber_Type = OctetString
_MmToUSBIntfVpdRevisonNumber_Object = MibTableColumn
mmToUSBIntfVpdRevisonNumber = _MmToUSBIntfVpdRevisonNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 3, 5, 1, 4),
    _MmToUSBIntfVpdRevisonNumber_Type()
)
mmToUSBIntfVpdRevisonNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmToUSBIntfVpdRevisonNumber.setStatus("mandatory")
_MmToUSBIntfVpdFilename_Type = OctetString
_MmToUSBIntfVpdFilename_Object = MibTableColumn
mmToUSBIntfVpdFilename = _MmToUSBIntfVpdFilename_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 3, 5, 1, 5),
    _MmToUSBIntfVpdFilename_Type()
)
mmToUSBIntfVpdFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmToUSBIntfVpdFilename.setStatus("mandatory")
_MmToUSBIntfVpdBuildDate_Type = OctetString
_MmToUSBIntfVpdBuildDate_Object = MibTableColumn
mmToUSBIntfVpdBuildDate = _MmToUSBIntfVpdBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 3, 5, 1, 6),
    _MmToUSBIntfVpdBuildDate_Type()
)
mmToUSBIntfVpdBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmToUSBIntfVpdBuildDate.setStatus("mandatory")
_BladeHardwareVpd_ObjectIdentity = ObjectIdentity
bladeHardwareVpd = _BladeHardwareVpd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 4)
)
_BladeHardwareVpdTable_Object = MibTable
bladeHardwareVpdTable = _BladeHardwareVpdTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 4, 1)
)
if mibBuilder.loadTexts:
    bladeHardwareVpdTable.setStatus("mandatory")
_BladeHardwareVpdEntry_Object = MibTableRow
bladeHardwareVpdEntry = _BladeHardwareVpdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 4, 1, 1)
)
bladeHardwareVpdEntry.setIndexNames(
    (0, "BLADE-MIB", "bladeHardwareVpdIndex"),
)
if mibBuilder.loadTexts:
    bladeHardwareVpdEntry.setStatus("mandatory")
_BladeHardwareVpdIndex_Type = Integer32
_BladeHardwareVpdIndex_Object = MibTableColumn
bladeHardwareVpdIndex = _BladeHardwareVpdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 4, 1, 1, 1),
    _BladeHardwareVpdIndex_Type()
)
bladeHardwareVpdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeHardwareVpdIndex.setStatus("mandatory")
_BladeHardwareVpdBayNumber_Type = OctetString
_BladeHardwareVpdBayNumber_Object = MibTableColumn
bladeHardwareVpdBayNumber = _BladeHardwareVpdBayNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 4, 1, 1, 2),
    _BladeHardwareVpdBayNumber_Type()
)
bladeHardwareVpdBayNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeHardwareVpdBayNumber.setStatus("mandatory")
_BladeHardwareVpdManufacturingId_Type = OctetString
_BladeHardwareVpdManufacturingId_Object = MibTableColumn
bladeHardwareVpdManufacturingId = _BladeHardwareVpdManufacturingId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 4, 1, 1, 3),
    _BladeHardwareVpdManufacturingId_Type()
)
bladeHardwareVpdManufacturingId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeHardwareVpdManufacturingId.setStatus("mandatory")
_BladeHardwareVpdFruNumber_Type = OctetString
_BladeHardwareVpdFruNumber_Object = MibTableColumn
bladeHardwareVpdFruNumber = _BladeHardwareVpdFruNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 4, 1, 1, 4),
    _BladeHardwareVpdFruNumber_Type()
)
bladeHardwareVpdFruNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeHardwareVpdFruNumber.setStatus("mandatory")
_BladeHardwareVpdHardwareRevision_Type = Integer32
_BladeHardwareVpdHardwareRevision_Object = MibTableColumn
bladeHardwareVpdHardwareRevision = _BladeHardwareVpdHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 4, 1, 1, 5),
    _BladeHardwareVpdHardwareRevision_Type()
)
bladeHardwareVpdHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeHardwareVpdHardwareRevision.setStatus("mandatory")
_BladeHardwareVpdSerialNumber_Type = OctetString
_BladeHardwareVpdSerialNumber_Object = MibTableColumn
bladeHardwareVpdSerialNumber = _BladeHardwareVpdSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 4, 1, 1, 6),
    _BladeHardwareVpdSerialNumber_Type()
)
bladeHardwareVpdSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeHardwareVpdSerialNumber.setStatus("mandatory")
_BladeHardwareVpdMachineType_Type = OctetString
_BladeHardwareVpdMachineType_Object = MibTableColumn
bladeHardwareVpdMachineType = _BladeHardwareVpdMachineType_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 4, 1, 1, 7),
    _BladeHardwareVpdMachineType_Type()
)
bladeHardwareVpdMachineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeHardwareVpdMachineType.setStatus("mandatory")
_BladeHardwareVpdUuid_Type = OctetString
_BladeHardwareVpdUuid_Object = MibTableColumn
bladeHardwareVpdUuid = _BladeHardwareVpdUuid_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 4, 1, 1, 8),
    _BladeHardwareVpdUuid_Type()
)
bladeHardwareVpdUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeHardwareVpdUuid.setStatus("mandatory")
_BladeHardwareVpdManufDate_Type = OctetString
_BladeHardwareVpdManufDate_Object = MibTableColumn
bladeHardwareVpdManufDate = _BladeHardwareVpdManufDate_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 4, 1, 1, 9),
    _BladeHardwareVpdManufDate_Type()
)
bladeHardwareVpdManufDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeHardwareVpdManufDate.setStatus("mandatory")
_BladeHardwareVpdPartNumber_Type = OctetString
_BladeHardwareVpdPartNumber_Object = MibTableColumn
bladeHardwareVpdPartNumber = _BladeHardwareVpdPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 4, 1, 1, 10),
    _BladeHardwareVpdPartNumber_Type()
)
bladeHardwareVpdPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeHardwareVpdPartNumber.setStatus("mandatory")
_BladeHardwareVpdFruSerial_Type = OctetString
_BladeHardwareVpdFruSerial_Object = MibTableColumn
bladeHardwareVpdFruSerial = _BladeHardwareVpdFruSerial_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 4, 1, 1, 11),
    _BladeHardwareVpdFruSerial_Type()
)
bladeHardwareVpdFruSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeHardwareVpdFruSerial.setStatus("mandatory")


class _BladeDaughterVpdCardType_Type(Integer32):
    """Custom type bladeDaughterVpdCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dasd", 2),
          ("network", 1),
          ("unknown", 0))
    )


_BladeDaughterVpdCardType_Type.__name__ = "Integer32"
_BladeDaughterVpdCardType_Object = MibTableColumn
bladeDaughterVpdCardType = _BladeDaughterVpdCardType_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 4, 1, 1, 20),
    _BladeDaughterVpdCardType_Type()
)
bladeDaughterVpdCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeDaughterVpdCardType.setStatus("mandatory")
_BladeDaughterVpdManufacturingId_Type = OctetString
_BladeDaughterVpdManufacturingId_Object = MibTableColumn
bladeDaughterVpdManufacturingId = _BladeDaughterVpdManufacturingId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 4, 1, 1, 21),
    _BladeDaughterVpdManufacturingId_Type()
)
bladeDaughterVpdManufacturingId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeDaughterVpdManufacturingId.setStatus("mandatory")
_BladeDaughterVpdFruNumber_Type = OctetString
_BladeDaughterVpdFruNumber_Object = MibTableColumn
bladeDaughterVpdFruNumber = _BladeDaughterVpdFruNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 4, 1, 1, 22),
    _BladeDaughterVpdFruNumber_Type()
)
bladeDaughterVpdFruNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeDaughterVpdFruNumber.setStatus("mandatory")
_BladeDaughterVpdHardwareRevision_Type = Integer32
_BladeDaughterVpdHardwareRevision_Object = MibTableColumn
bladeDaughterVpdHardwareRevision = _BladeDaughterVpdHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 4, 1, 1, 23),
    _BladeDaughterVpdHardwareRevision_Type()
)
bladeDaughterVpdHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeDaughterVpdHardwareRevision.setStatus("mandatory")
_BladeDaughterVpdSerialNumber_Type = OctetString
_BladeDaughterVpdSerialNumber_Object = MibTableColumn
bladeDaughterVpdSerialNumber = _BladeDaughterVpdSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 4, 1, 1, 24),
    _BladeDaughterVpdSerialNumber_Type()
)
bladeDaughterVpdSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeDaughterVpdSerialNumber.setStatus("mandatory")
_BladeDaughterVpdMachineType_Type = OctetString
_BladeDaughterVpdMachineType_Object = MibTableColumn
bladeDaughterVpdMachineType = _BladeDaughterVpdMachineType_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 4, 1, 1, 25),
    _BladeDaughterVpdMachineType_Type()
)
bladeDaughterVpdMachineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeDaughterVpdMachineType.setStatus("mandatory")
_BladeDaughterVpdUuid_Type = OctetString
_BladeDaughterVpdUuid_Object = MibTableColumn
bladeDaughterVpdUuid = _BladeDaughterVpdUuid_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 4, 1, 1, 26),
    _BladeDaughterVpdUuid_Type()
)
bladeDaughterVpdUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeDaughterVpdUuid.setStatus("mandatory")
_BladeDaughterVpdManufDate_Type = OctetString
_BladeDaughterVpdManufDate_Object = MibTableColumn
bladeDaughterVpdManufDate = _BladeDaughterVpdManufDate_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 4, 1, 1, 27),
    _BladeDaughterVpdManufDate_Type()
)
bladeDaughterVpdManufDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeDaughterVpdManufDate.setStatus("mandatory")
_BladeDaughterVpdPartNumber_Type = OctetString
_BladeDaughterVpdPartNumber_Object = MibTableColumn
bladeDaughterVpdPartNumber = _BladeDaughterVpdPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 4, 1, 1, 28),
    _BladeDaughterVpdPartNumber_Type()
)
bladeDaughterVpdPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeDaughterVpdPartNumber.setStatus("mandatory")
_BladeDaughterVpdFruSerial_Type = OctetString
_BladeDaughterVpdFruSerial_Object = MibTableColumn
bladeDaughterVpdFruSerial = _BladeDaughterVpdFruSerial_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 4, 1, 1, 29),
    _BladeDaughterVpdFruSerial_Type()
)
bladeDaughterVpdFruSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeDaughterVpdFruSerial.setStatus("mandatory")
_BladeMACAddressVpdTable_Object = MibTable
bladeMACAddressVpdTable = _BladeMACAddressVpdTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 4, 2)
)
if mibBuilder.loadTexts:
    bladeMACAddressVpdTable.setStatus("mandatory")
_BladeMACAddressVpdEntry_Object = MibTableRow
bladeMACAddressVpdEntry = _BladeMACAddressVpdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 4, 2, 1)
)
bladeMACAddressVpdEntry.setIndexNames(
    (0, "BLADE-MIB", "bladeMACAddressVpdIndex"),
)
if mibBuilder.loadTexts:
    bladeMACAddressVpdEntry.setStatus("mandatory")
_BladeMACAddressVpdIndex_Type = Integer32
_BladeMACAddressVpdIndex_Object = MibTableColumn
bladeMACAddressVpdIndex = _BladeMACAddressVpdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 4, 2, 1, 1),
    _BladeMACAddressVpdIndex_Type()
)
bladeMACAddressVpdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeMACAddressVpdIndex.setStatus("mandatory")
_BladeMACAddress1Vpd_Type = OctetString
_BladeMACAddress1Vpd_Object = MibTableColumn
bladeMACAddress1Vpd = _BladeMACAddress1Vpd_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 4, 2, 1, 2),
    _BladeMACAddress1Vpd_Type()
)
bladeMACAddress1Vpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeMACAddress1Vpd.setStatus("mandatory")
_BladeMACAddress2Vpd_Type = OctetString
_BladeMACAddress2Vpd_Object = MibTableColumn
bladeMACAddress2Vpd = _BladeMACAddress2Vpd_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 4, 2, 1, 3),
    _BladeMACAddress2Vpd_Type()
)
bladeMACAddress2Vpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeMACAddress2Vpd.setStatus("mandatory")
_BladeMACAddress3Vpd_Type = OctetString
_BladeMACAddress3Vpd_Object = MibTableColumn
bladeMACAddress3Vpd = _BladeMACAddress3Vpd_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 4, 2, 1, 4),
    _BladeMACAddress3Vpd_Type()
)
bladeMACAddress3Vpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeMACAddress3Vpd.setStatus("mandatory")
_BladeMACAddress4Vpd_Type = OctetString
_BladeMACAddress4Vpd_Object = MibTableColumn
bladeMACAddress4Vpd = _BladeMACAddress4Vpd_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 4, 2, 1, 5),
    _BladeMACAddress4Vpd_Type()
)
bladeMACAddress4Vpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeMACAddress4Vpd.setStatus("mandatory")
_BladeDaughterCard1MACAddress1Vpd_Type = OctetString
_BladeDaughterCard1MACAddress1Vpd_Object = MibTableColumn
bladeDaughterCard1MACAddress1Vpd = _BladeDaughterCard1MACAddress1Vpd_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 4, 2, 1, 10),
    _BladeDaughterCard1MACAddress1Vpd_Type()
)
bladeDaughterCard1MACAddress1Vpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeDaughterCard1MACAddress1Vpd.setStatus("mandatory")
_BladeDaughterCard1MACAddress2Vpd_Type = OctetString
_BladeDaughterCard1MACAddress2Vpd_Object = MibTableColumn
bladeDaughterCard1MACAddress2Vpd = _BladeDaughterCard1MACAddress2Vpd_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 4, 2, 1, 11),
    _BladeDaughterCard1MACAddress2Vpd_Type()
)
bladeDaughterCard1MACAddress2Vpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeDaughterCard1MACAddress2Vpd.setStatus("mandatory")
_BladeDaughterCard1MACAddress3Vpd_Type = OctetString
_BladeDaughterCard1MACAddress3Vpd_Object = MibTableColumn
bladeDaughterCard1MACAddress3Vpd = _BladeDaughterCard1MACAddress3Vpd_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 4, 2, 1, 12),
    _BladeDaughterCard1MACAddress3Vpd_Type()
)
bladeDaughterCard1MACAddress3Vpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeDaughterCard1MACAddress3Vpd.setStatus("mandatory")
_BladeDaughterCard1MACAddress4Vpd_Type = OctetString
_BladeDaughterCard1MACAddress4Vpd_Object = MibTableColumn
bladeDaughterCard1MACAddress4Vpd = _BladeDaughterCard1MACAddress4Vpd_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 4, 2, 1, 13),
    _BladeDaughterCard1MACAddress4Vpd_Type()
)
bladeDaughterCard1MACAddress4Vpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeDaughterCard1MACAddress4Vpd.setStatus("mandatory")
_BladeDaughterCard2MACAddress1Vpd_Type = OctetString
_BladeDaughterCard2MACAddress1Vpd_Object = MibTableColumn
bladeDaughterCard2MACAddress1Vpd = _BladeDaughterCard2MACAddress1Vpd_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 4, 2, 1, 18),
    _BladeDaughterCard2MACAddress1Vpd_Type()
)
bladeDaughterCard2MACAddress1Vpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeDaughterCard2MACAddress1Vpd.setStatus("mandatory")
_BladeDaughterCard2MACAddress2Vpd_Type = OctetString
_BladeDaughterCard2MACAddress2Vpd_Object = MibTableColumn
bladeDaughterCard2MACAddress2Vpd = _BladeDaughterCard2MACAddress2Vpd_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 4, 2, 1, 19),
    _BladeDaughterCard2MACAddress2Vpd_Type()
)
bladeDaughterCard2MACAddress2Vpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeDaughterCard2MACAddress2Vpd.setStatus("mandatory")
_BladeDaughterCard2MACAddress3Vpd_Type = OctetString
_BladeDaughterCard2MACAddress3Vpd_Object = MibTableColumn
bladeDaughterCard2MACAddress3Vpd = _BladeDaughterCard2MACAddress3Vpd_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 4, 2, 1, 20),
    _BladeDaughterCard2MACAddress3Vpd_Type()
)
bladeDaughterCard2MACAddress3Vpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeDaughterCard2MACAddress3Vpd.setStatus("mandatory")
_BladeDaughterCard2MACAddress4Vpd_Type = OctetString
_BladeDaughterCard2MACAddress4Vpd_Object = MibTableColumn
bladeDaughterCard2MACAddress4Vpd = _BladeDaughterCard2MACAddress4Vpd_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 4, 2, 1, 21),
    _BladeDaughterCard2MACAddress4Vpd_Type()
)
bladeDaughterCard2MACAddress4Vpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeDaughterCard2MACAddress4Vpd.setStatus("mandatory")
_BladeFirmwareVpd_ObjectIdentity = ObjectIdentity
bladeFirmwareVpd = _BladeFirmwareVpd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 5)
)
_BladeBiosVPDTable_Object = MibTable
bladeBiosVPDTable = _BladeBiosVPDTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 5, 1)
)
if mibBuilder.loadTexts:
    bladeBiosVPDTable.setStatus("mandatory")
_BladeBiosVPDEntry_Object = MibTableRow
bladeBiosVPDEntry = _BladeBiosVPDEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 5, 1, 1)
)
bladeBiosVPDEntry.setIndexNames(
    (0, "BLADE-MIB", "bladeBiosVpdIndex"),
)
if mibBuilder.loadTexts:
    bladeBiosVPDEntry.setStatus("mandatory")
_BladeBiosVpdIndex_Type = Integer32
_BladeBiosVpdIndex_Object = MibTableColumn
bladeBiosVpdIndex = _BladeBiosVpdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 5, 1, 1, 1),
    _BladeBiosVpdIndex_Type()
)
bladeBiosVpdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeBiosVpdIndex.setStatus("mandatory")


class _BladeBiosVpdId_Type(Integer32):
    """Custom type bladeBiosVpdId based on Integer32"""
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
        *(("blade1", 1),
          ("blade10", 10),
          ("blade11", 11),
          ("blade12", 12),
          ("blade13", 13),
          ("blade14", 14),
          ("blade2", 2),
          ("blade3", 3),
          ("blade4", 4),
          ("blade5", 5),
          ("blade6", 6),
          ("blade7", 7),
          ("blade8", 8),
          ("blade9", 9))
    )


_BladeBiosVpdId_Type.__name__ = "Integer32"
_BladeBiosVpdId_Object = MibTableColumn
bladeBiosVpdId = _BladeBiosVpdId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 5, 1, 1, 2),
    _BladeBiosVpdId_Type()
)
bladeBiosVpdId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeBiosVpdId.setStatus("mandatory")


class _BladeBiosVpdExists_Type(Integer32):
    """Custom type bladeBiosVpdExists based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_BladeBiosVpdExists_Type.__name__ = "Integer32"
_BladeBiosVpdExists_Object = MibTableColumn
bladeBiosVpdExists = _BladeBiosVpdExists_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 5, 1, 1, 3),
    _BladeBiosVpdExists_Type()
)
bladeBiosVpdExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeBiosVpdExists.setStatus("mandatory")


class _BladeBiosVpdPowerState_Type(Integer32):
    """Custom type bladeBiosVpdPowerState based on Integer32"""
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


_BladeBiosVpdPowerState_Type.__name__ = "Integer32"
_BladeBiosVpdPowerState_Object = MibTableColumn
bladeBiosVpdPowerState = _BladeBiosVpdPowerState_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 5, 1, 1, 4),
    _BladeBiosVpdPowerState_Type()
)
bladeBiosVpdPowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeBiosVpdPowerState.setStatus("mandatory")
_BladeBiosVpdName_Type = OctetString
_BladeBiosVpdName_Object = MibTableColumn
bladeBiosVpdName = _BladeBiosVpdName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 5, 1, 1, 5),
    _BladeBiosVpdName_Type()
)
bladeBiosVpdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeBiosVpdName.setStatus("mandatory")
_BladeBiosVpdBuildId_Type = OctetString
_BladeBiosVpdBuildId_Object = MibTableColumn
bladeBiosVpdBuildId = _BladeBiosVpdBuildId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 5, 1, 1, 6),
    _BladeBiosVpdBuildId_Type()
)
bladeBiosVpdBuildId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeBiosVpdBuildId.setStatus("mandatory")
_BladeBiosVpdRevision_Type = OctetString
_BladeBiosVpdRevision_Object = MibTableColumn
bladeBiosVpdRevision = _BladeBiosVpdRevision_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 5, 1, 1, 7),
    _BladeBiosVpdRevision_Type()
)
bladeBiosVpdRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeBiosVpdRevision.setStatus("mandatory")
_BladeBiosVpdDate_Type = OctetString
_BladeBiosVpdDate_Object = MibTableColumn
bladeBiosVpdDate = _BladeBiosVpdDate_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 5, 1, 1, 8),
    _BladeBiosVpdDate_Type()
)
bladeBiosVpdDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeBiosVpdDate.setStatus("mandatory")
_BladeDiagsVPDTable_Object = MibTable
bladeDiagsVPDTable = _BladeDiagsVPDTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 5, 2)
)
if mibBuilder.loadTexts:
    bladeDiagsVPDTable.setStatus("mandatory")
_BladeDiagsVPDEntry_Object = MibTableRow
bladeDiagsVPDEntry = _BladeDiagsVPDEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 5, 2, 1)
)
bladeDiagsVPDEntry.setIndexNames(
    (0, "BLADE-MIB", "bladeDiagsVpdIndex"),
)
if mibBuilder.loadTexts:
    bladeDiagsVPDEntry.setStatus("mandatory")
_BladeDiagsVpdIndex_Type = Integer32
_BladeDiagsVpdIndex_Object = MibTableColumn
bladeDiagsVpdIndex = _BladeDiagsVpdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 5, 2, 1, 1),
    _BladeDiagsVpdIndex_Type()
)
bladeDiagsVpdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeDiagsVpdIndex.setStatus("mandatory")


class _BladeDiagsVpdId_Type(Integer32):
    """Custom type bladeDiagsVpdId based on Integer32"""
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
        *(("blade1", 1),
          ("blade10", 10),
          ("blade11", 11),
          ("blade12", 12),
          ("blade13", 13),
          ("blade14", 14),
          ("blade2", 2),
          ("blade3", 3),
          ("blade4", 4),
          ("blade5", 5),
          ("blade6", 6),
          ("blade7", 7),
          ("blade8", 8),
          ("blade9", 9))
    )


_BladeDiagsVpdId_Type.__name__ = "Integer32"
_BladeDiagsVpdId_Object = MibTableColumn
bladeDiagsVpdId = _BladeDiagsVpdId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 5, 2, 1, 2),
    _BladeDiagsVpdId_Type()
)
bladeDiagsVpdId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeDiagsVpdId.setStatus("mandatory")


class _BladeDiagsVpdExists_Type(Integer32):
    """Custom type bladeDiagsVpdExists based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_BladeDiagsVpdExists_Type.__name__ = "Integer32"
_BladeDiagsVpdExists_Object = MibTableColumn
bladeDiagsVpdExists = _BladeDiagsVpdExists_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 5, 2, 1, 3),
    _BladeDiagsVpdExists_Type()
)
bladeDiagsVpdExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeDiagsVpdExists.setStatus("mandatory")


class _BladeDiagsVpdPowerState_Type(Integer32):
    """Custom type bladeDiagsVpdPowerState based on Integer32"""
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


_BladeDiagsVpdPowerState_Type.__name__ = "Integer32"
_BladeDiagsVpdPowerState_Object = MibTableColumn
bladeDiagsVpdPowerState = _BladeDiagsVpdPowerState_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 5, 2, 1, 4),
    _BladeDiagsVpdPowerState_Type()
)
bladeDiagsVpdPowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeDiagsVpdPowerState.setStatus("mandatory")
_BladeDiagsVpdName_Type = OctetString
_BladeDiagsVpdName_Object = MibTableColumn
bladeDiagsVpdName = _BladeDiagsVpdName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 5, 2, 1, 5),
    _BladeDiagsVpdName_Type()
)
bladeDiagsVpdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeDiagsVpdName.setStatus("mandatory")
_BladeDiagsVpdBuildId_Type = OctetString
_BladeDiagsVpdBuildId_Object = MibTableColumn
bladeDiagsVpdBuildId = _BladeDiagsVpdBuildId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 5, 2, 1, 6),
    _BladeDiagsVpdBuildId_Type()
)
bladeDiagsVpdBuildId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeDiagsVpdBuildId.setStatus("mandatory")
_BladeDiagsVpdRevision_Type = OctetString
_BladeDiagsVpdRevision_Object = MibTableColumn
bladeDiagsVpdRevision = _BladeDiagsVpdRevision_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 5, 2, 1, 7),
    _BladeDiagsVpdRevision_Type()
)
bladeDiagsVpdRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeDiagsVpdRevision.setStatus("mandatory")
_BladeDiagsVpdDate_Type = OctetString
_BladeDiagsVpdDate_Object = MibTableColumn
bladeDiagsVpdDate = _BladeDiagsVpdDate_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 5, 2, 1, 8),
    _BladeDiagsVpdDate_Type()
)
bladeDiagsVpdDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeDiagsVpdDate.setStatus("mandatory")
_BladeSysMgmtProcVPDTable_Object = MibTable
bladeSysMgmtProcVPDTable = _BladeSysMgmtProcVPDTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 5, 3)
)
if mibBuilder.loadTexts:
    bladeSysMgmtProcVPDTable.setStatus("mandatory")
_BladeSysMgmtProcVPDEntry_Object = MibTableRow
bladeSysMgmtProcVPDEntry = _BladeSysMgmtProcVPDEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 5, 3, 1)
)
bladeSysMgmtProcVPDEntry.setIndexNames(
    (0, "BLADE-MIB", "bladeSysMgmtProcVpdIndex"),
)
if mibBuilder.loadTexts:
    bladeSysMgmtProcVPDEntry.setStatus("mandatory")
_BladeSysMgmtProcVpdIndex_Type = Integer32
_BladeSysMgmtProcVpdIndex_Object = MibTableColumn
bladeSysMgmtProcVpdIndex = _BladeSysMgmtProcVpdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 5, 3, 1, 1),
    _BladeSysMgmtProcVpdIndex_Type()
)
bladeSysMgmtProcVpdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSysMgmtProcVpdIndex.setStatus("mandatory")


class _BladeSysMgmtProcVpdId_Type(Integer32):
    """Custom type bladeSysMgmtProcVpdId based on Integer32"""
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
        *(("blade1", 1),
          ("blade10", 10),
          ("blade11", 11),
          ("blade12", 12),
          ("blade13", 13),
          ("blade14", 14),
          ("blade2", 2),
          ("blade3", 3),
          ("blade4", 4),
          ("blade5", 5),
          ("blade6", 6),
          ("blade7", 7),
          ("blade8", 8),
          ("blade9", 9))
    )


_BladeSysMgmtProcVpdId_Type.__name__ = "Integer32"
_BladeSysMgmtProcVpdId_Object = MibTableColumn
bladeSysMgmtProcVpdId = _BladeSysMgmtProcVpdId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 5, 3, 1, 2),
    _BladeSysMgmtProcVpdId_Type()
)
bladeSysMgmtProcVpdId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSysMgmtProcVpdId.setStatus("mandatory")


class _BladeSysMgmtProcVpdExists_Type(Integer32):
    """Custom type bladeSysMgmtProcVpdExists based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_BladeSysMgmtProcVpdExists_Type.__name__ = "Integer32"
_BladeSysMgmtProcVpdExists_Object = MibTableColumn
bladeSysMgmtProcVpdExists = _BladeSysMgmtProcVpdExists_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 5, 3, 1, 3),
    _BladeSysMgmtProcVpdExists_Type()
)
bladeSysMgmtProcVpdExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSysMgmtProcVpdExists.setStatus("mandatory")


class _BladeSysMgmtProcVpdPowerState_Type(Integer32):
    """Custom type bladeSysMgmtProcVpdPowerState based on Integer32"""
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


_BladeSysMgmtProcVpdPowerState_Type.__name__ = "Integer32"
_BladeSysMgmtProcVpdPowerState_Object = MibTableColumn
bladeSysMgmtProcVpdPowerState = _BladeSysMgmtProcVpdPowerState_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 5, 3, 1, 4),
    _BladeSysMgmtProcVpdPowerState_Type()
)
bladeSysMgmtProcVpdPowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSysMgmtProcVpdPowerState.setStatus("mandatory")
_BladeSysMgmtProcVpdName_Type = OctetString
_BladeSysMgmtProcVpdName_Object = MibTableColumn
bladeSysMgmtProcVpdName = _BladeSysMgmtProcVpdName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 5, 3, 1, 5),
    _BladeSysMgmtProcVpdName_Type()
)
bladeSysMgmtProcVpdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSysMgmtProcVpdName.setStatus("mandatory")
_BladeSysMgmtProcVpdBuildId_Type = OctetString
_BladeSysMgmtProcVpdBuildId_Object = MibTableColumn
bladeSysMgmtProcVpdBuildId = _BladeSysMgmtProcVpdBuildId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 5, 3, 1, 6),
    _BladeSysMgmtProcVpdBuildId_Type()
)
bladeSysMgmtProcVpdBuildId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSysMgmtProcVpdBuildId.setStatus("mandatory")
_BladeSysMgmtProcVpdRevision_Type = OctetString
_BladeSysMgmtProcVpdRevision_Object = MibTableColumn
bladeSysMgmtProcVpdRevision = _BladeSysMgmtProcVpdRevision_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 5, 3, 1, 7),
    _BladeSysMgmtProcVpdRevision_Type()
)
bladeSysMgmtProcVpdRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSysMgmtProcVpdRevision.setStatus("mandatory")
_SmHardwareVpd_ObjectIdentity = ObjectIdentity
smHardwareVpd = _SmHardwareVpd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 6)
)
_SmHardwareVpdTable_Object = MibTable
smHardwareVpdTable = _SmHardwareVpdTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 6, 1)
)
if mibBuilder.loadTexts:
    smHardwareVpdTable.setStatus("mandatory")
_SmHardwareVpdEntry_Object = MibTableRow
smHardwareVpdEntry = _SmHardwareVpdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 6, 1, 1)
)
smHardwareVpdEntry.setIndexNames(
    (0, "BLADE-MIB", "smHardwareVpdIndex"),
)
if mibBuilder.loadTexts:
    smHardwareVpdEntry.setStatus("mandatory")
_SmHardwareVpdIndex_Type = Integer32
_SmHardwareVpdIndex_Object = MibTableColumn
smHardwareVpdIndex = _SmHardwareVpdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 6, 1, 1, 1),
    _SmHardwareVpdIndex_Type()
)
smHardwareVpdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smHardwareVpdIndex.setStatus("mandatory")
_SmHardwareVpdBayNumber_Type = OctetString
_SmHardwareVpdBayNumber_Object = MibTableColumn
smHardwareVpdBayNumber = _SmHardwareVpdBayNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 6, 1, 1, 2),
    _SmHardwareVpdBayNumber_Type()
)
smHardwareVpdBayNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smHardwareVpdBayNumber.setStatus("mandatory")
_SmHardwareVpdManufacturingId_Type = OctetString
_SmHardwareVpdManufacturingId_Object = MibTableColumn
smHardwareVpdManufacturingId = _SmHardwareVpdManufacturingId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 6, 1, 1, 3),
    _SmHardwareVpdManufacturingId_Type()
)
smHardwareVpdManufacturingId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smHardwareVpdManufacturingId.setStatus("mandatory")
_SmHardwareVpdFruNumber_Type = OctetString
_SmHardwareVpdFruNumber_Object = MibTableColumn
smHardwareVpdFruNumber = _SmHardwareVpdFruNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 6, 1, 1, 4),
    _SmHardwareVpdFruNumber_Type()
)
smHardwareVpdFruNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smHardwareVpdFruNumber.setStatus("mandatory")
_SmHardwareVpdHardwareRevision_Type = Integer32
_SmHardwareVpdHardwareRevision_Object = MibTableColumn
smHardwareVpdHardwareRevision = _SmHardwareVpdHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 6, 1, 1, 5),
    _SmHardwareVpdHardwareRevision_Type()
)
smHardwareVpdHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smHardwareVpdHardwareRevision.setStatus("mandatory")
_SmHardwareVpdUuid_Type = OctetString
_SmHardwareVpdUuid_Object = MibTableColumn
smHardwareVpdUuid = _SmHardwareVpdUuid_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 6, 1, 1, 8),
    _SmHardwareVpdUuid_Type()
)
smHardwareVpdUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smHardwareVpdUuid.setStatus("mandatory")
_SmHardwareVpdManufDate_Type = OctetString
_SmHardwareVpdManufDate_Object = MibTableColumn
smHardwareVpdManufDate = _SmHardwareVpdManufDate_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 6, 1, 1, 9),
    _SmHardwareVpdManufDate_Type()
)
smHardwareVpdManufDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smHardwareVpdManufDate.setStatus("mandatory")
_SmHardwareVpdPartNumber_Type = OctetString
_SmHardwareVpdPartNumber_Object = MibTableColumn
smHardwareVpdPartNumber = _SmHardwareVpdPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 6, 1, 1, 10),
    _SmHardwareVpdPartNumber_Type()
)
smHardwareVpdPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smHardwareVpdPartNumber.setStatus("mandatory")
_SmHardwareVpdFruSerial_Type = OctetString
_SmHardwareVpdFruSerial_Object = MibTableColumn
smHardwareVpdFruSerial = _SmHardwareVpdFruSerial_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 6, 1, 1, 11),
    _SmHardwareVpdFruSerial_Type()
)
smHardwareVpdFruSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smHardwareVpdFruSerial.setStatus("mandatory")
_SmFirmwareVpd_ObjectIdentity = ObjectIdentity
smFirmwareVpd = _SmFirmwareVpd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 7)
)
_SmMainAppVpdTable_Object = MibTable
smMainAppVpdTable = _SmMainAppVpdTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 7, 1)
)
if mibBuilder.loadTexts:
    smMainAppVpdTable.setStatus("mandatory")
_SmMainAppVpdEntry_Object = MibTableRow
smMainAppVpdEntry = _SmMainAppVpdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 7, 1, 1)
)
smMainAppVpdEntry.setIndexNames(
    (0, "BLADE-MIB", "smMainAppVpdIndex"),
)
if mibBuilder.loadTexts:
    smMainAppVpdEntry.setStatus("mandatory")
_SmMainAppVpdIndex_Type = Integer32
_SmMainAppVpdIndex_Object = MibTableColumn
smMainAppVpdIndex = _SmMainAppVpdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 7, 1, 1, 1),
    _SmMainAppVpdIndex_Type()
)
smMainAppVpdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMainAppVpdIndex.setStatus("mandatory")


class _SmMainAppVpdId_Type(Integer32):
    """Custom type smMainAppVpdId based on Integer32"""
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
        *(("module1", 1),
          ("module2", 2),
          ("module3", 3),
          ("module4", 4))
    )


_SmMainAppVpdId_Type.__name__ = "Integer32"
_SmMainAppVpdId_Object = MibTableColumn
smMainAppVpdId = _SmMainAppVpdId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 7, 1, 1, 2),
    _SmMainAppVpdId_Type()
)
smMainAppVpdId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMainAppVpdId.setStatus("mandatory")


class _SmMainAppVpdExists_Type(Integer32):
    """Custom type smMainAppVpdExists based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SmMainAppVpdExists_Type.__name__ = "Integer32"
_SmMainAppVpdExists_Object = MibTableColumn
smMainAppVpdExists = _SmMainAppVpdExists_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 7, 1, 1, 3),
    _SmMainAppVpdExists_Type()
)
smMainAppVpdExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMainAppVpdExists.setStatus("mandatory")


class _SmMainAppVpdSwitchType_Type(Integer32):
    """Custom type smMainAppVpdSwitchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("copperPassThrough", 5),
          ("ethernet", 1),
          ("fibre", 2),
          ("infiniband", 6),
          ("opm", 3),
          ("serialCM", 4),
          ("unknown", 0))
    )


_SmMainAppVpdSwitchType_Type.__name__ = "Integer32"
_SmMainAppVpdSwitchType_Object = MibTableColumn
smMainAppVpdSwitchType = _SmMainAppVpdSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 7, 1, 1, 4),
    _SmMainAppVpdSwitchType_Type()
)
smMainAppVpdSwitchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMainAppVpdSwitchType.setStatus("mandatory")
_SmMainApp1VpdBuildId_Type = OctetString
_SmMainApp1VpdBuildId_Object = MibTableColumn
smMainApp1VpdBuildId = _SmMainApp1VpdBuildId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 7, 1, 1, 5),
    _SmMainApp1VpdBuildId_Type()
)
smMainApp1VpdBuildId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMainApp1VpdBuildId.setStatus("mandatory")
_SmMainApp1VpdBuildDate_Type = OctetString
_SmMainApp1VpdBuildDate_Object = MibTableColumn
smMainApp1VpdBuildDate = _SmMainApp1VpdBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 7, 1, 1, 6),
    _SmMainApp1VpdBuildDate_Type()
)
smMainApp1VpdBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMainApp1VpdBuildDate.setStatus("mandatory")
_SmMainApp1VpdRevisionNumber_Type = OctetString
_SmMainApp1VpdRevisionNumber_Object = MibTableColumn
smMainApp1VpdRevisionNumber = _SmMainApp1VpdRevisionNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 7, 1, 1, 7),
    _SmMainApp1VpdRevisionNumber_Type()
)
smMainApp1VpdRevisionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMainApp1VpdRevisionNumber.setStatus("mandatory")
_SmMainApp2VpdBuildId_Type = OctetString
_SmMainApp2VpdBuildId_Object = MibTableColumn
smMainApp2VpdBuildId = _SmMainApp2VpdBuildId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 7, 1, 1, 8),
    _SmMainApp2VpdBuildId_Type()
)
smMainApp2VpdBuildId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMainApp2VpdBuildId.setStatus("mandatory")
_SmMainApp2VpdBuildDate_Type = OctetString
_SmMainApp2VpdBuildDate_Object = MibTableColumn
smMainApp2VpdBuildDate = _SmMainApp2VpdBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 7, 1, 1, 9),
    _SmMainApp2VpdBuildDate_Type()
)
smMainApp2VpdBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMainApp2VpdBuildDate.setStatus("mandatory")
_SmMainApp2VpdRevisionNumber_Type = OctetString
_SmMainApp2VpdRevisionNumber_Object = MibTableColumn
smMainApp2VpdRevisionNumber = _SmMainApp2VpdRevisionNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 7, 1, 1, 10),
    _SmMainApp2VpdRevisionNumber_Type()
)
smMainApp2VpdRevisionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMainApp2VpdRevisionNumber.setStatus("mandatory")
_SmBootRomVpdTable_Object = MibTable
smBootRomVpdTable = _SmBootRomVpdTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 7, 2)
)
if mibBuilder.loadTexts:
    smBootRomVpdTable.setStatus("mandatory")
_SmBootRomVpdEntry_Object = MibTableRow
smBootRomVpdEntry = _SmBootRomVpdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 7, 2, 1)
)
smBootRomVpdEntry.setIndexNames(
    (0, "BLADE-MIB", "smBootRomVpdIndex"),
)
if mibBuilder.loadTexts:
    smBootRomVpdEntry.setStatus("mandatory")
_SmBootRomVpdIndex_Type = Integer32
_SmBootRomVpdIndex_Object = MibTableColumn
smBootRomVpdIndex = _SmBootRomVpdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 7, 2, 1, 1),
    _SmBootRomVpdIndex_Type()
)
smBootRomVpdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smBootRomVpdIndex.setStatus("mandatory")


class _SmBootRomVpdId_Type(Integer32):
    """Custom type smBootRomVpdId based on Integer32"""
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
        *(("module1", 1),
          ("module2", 2),
          ("module3", 3),
          ("module4", 4))
    )


_SmBootRomVpdId_Type.__name__ = "Integer32"
_SmBootRomVpdId_Object = MibTableColumn
smBootRomVpdId = _SmBootRomVpdId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 7, 2, 1, 2),
    _SmBootRomVpdId_Type()
)
smBootRomVpdId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smBootRomVpdId.setStatus("mandatory")


class _SmBootRomVpdExists_Type(Integer32):
    """Custom type smBootRomVpdExists based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SmBootRomVpdExists_Type.__name__ = "Integer32"
_SmBootRomVpdExists_Object = MibTableColumn
smBootRomVpdExists = _SmBootRomVpdExists_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 7, 2, 1, 3),
    _SmBootRomVpdExists_Type()
)
smBootRomVpdExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smBootRomVpdExists.setStatus("mandatory")


class _SmBootRomVpdSwitchType_Type(Integer32):
    """Custom type smBootRomVpdSwitchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("copperPassThrough", 5),
          ("ethernet", 1),
          ("fibre", 2),
          ("infiniband", 6),
          ("opm", 3),
          ("serialCM", 4),
          ("unknown", 0))
    )


_SmBootRomVpdSwitchType_Type.__name__ = "Integer32"
_SmBootRomVpdSwitchType_Object = MibTableColumn
smBootRomVpdSwitchType = _SmBootRomVpdSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 7, 2, 1, 4),
    _SmBootRomVpdSwitchType_Type()
)
smBootRomVpdSwitchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smBootRomVpdSwitchType.setStatus("mandatory")
_SmBootRomVpdBuildId_Type = OctetString
_SmBootRomVpdBuildId_Object = MibTableColumn
smBootRomVpdBuildId = _SmBootRomVpdBuildId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 7, 2, 1, 5),
    _SmBootRomVpdBuildId_Type()
)
smBootRomVpdBuildId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smBootRomVpdBuildId.setStatus("mandatory")
_SmBootRomVpdBuildDate_Type = OctetString
_SmBootRomVpdBuildDate_Object = MibTableColumn
smBootRomVpdBuildDate = _SmBootRomVpdBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 7, 2, 1, 6),
    _SmBootRomVpdBuildDate_Type()
)
smBootRomVpdBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smBootRomVpdBuildDate.setStatus("mandatory")
_SmBootRomVpdRevisionNumber_Type = OctetString
_SmBootRomVpdRevisionNumber_Object = MibTableColumn
smBootRomVpdRevisionNumber = _SmBootRomVpdRevisionNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 7, 2, 1, 7),
    _SmBootRomVpdRevisionNumber_Type()
)
smBootRomVpdRevisionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smBootRomVpdRevisionNumber.setStatus("mandatory")
_PmHardwareVpd_ObjectIdentity = ObjectIdentity
pmHardwareVpd = _PmHardwareVpd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 8)
)
_PmHardwareVpdTable_Object = MibTable
pmHardwareVpdTable = _PmHardwareVpdTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 8, 1)
)
if mibBuilder.loadTexts:
    pmHardwareVpdTable.setStatus("mandatory")
_PmHardwareVpdEntry_Object = MibTableRow
pmHardwareVpdEntry = _PmHardwareVpdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 8, 1, 1)
)
pmHardwareVpdEntry.setIndexNames(
    (0, "BLADE-MIB", "pmHardwareVpdIndex"),
)
if mibBuilder.loadTexts:
    pmHardwareVpdEntry.setStatus("mandatory")
_PmHardwareVpdIndex_Type = Integer32
_PmHardwareVpdIndex_Object = MibTableColumn
pmHardwareVpdIndex = _PmHardwareVpdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 8, 1, 1, 1),
    _PmHardwareVpdIndex_Type()
)
pmHardwareVpdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmHardwareVpdIndex.setStatus("mandatory")
_PmHardwareVpdBayNumber_Type = OctetString
_PmHardwareVpdBayNumber_Object = MibTableColumn
pmHardwareVpdBayNumber = _PmHardwareVpdBayNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 8, 1, 1, 2),
    _PmHardwareVpdBayNumber_Type()
)
pmHardwareVpdBayNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmHardwareVpdBayNumber.setStatus("mandatory")
_PmHardwareVpdManufacturingId_Type = OctetString
_PmHardwareVpdManufacturingId_Object = MibTableColumn
pmHardwareVpdManufacturingId = _PmHardwareVpdManufacturingId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 8, 1, 1, 3),
    _PmHardwareVpdManufacturingId_Type()
)
pmHardwareVpdManufacturingId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmHardwareVpdManufacturingId.setStatus("mandatory")
_PmHardwareVpdFruNumber_Type = OctetString
_PmHardwareVpdFruNumber_Object = MibTableColumn
pmHardwareVpdFruNumber = _PmHardwareVpdFruNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 8, 1, 1, 4),
    _PmHardwareVpdFruNumber_Type()
)
pmHardwareVpdFruNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmHardwareVpdFruNumber.setStatus("mandatory")
_PmHardwareVpdHardwareRevision_Type = Integer32
_PmHardwareVpdHardwareRevision_Object = MibTableColumn
pmHardwareVpdHardwareRevision = _PmHardwareVpdHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 8, 1, 1, 5),
    _PmHardwareVpdHardwareRevision_Type()
)
pmHardwareVpdHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmHardwareVpdHardwareRevision.setStatus("mandatory")
_PmHardwareVpdUuid_Type = OctetString
_PmHardwareVpdUuid_Object = MibTableColumn
pmHardwareVpdUuid = _PmHardwareVpdUuid_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 8, 1, 1, 8),
    _PmHardwareVpdUuid_Type()
)
pmHardwareVpdUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmHardwareVpdUuid.setStatus("mandatory")
_PmHardwareVpdManufDate_Type = OctetString
_PmHardwareVpdManufDate_Object = MibTableColumn
pmHardwareVpdManufDate = _PmHardwareVpdManufDate_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 8, 1, 1, 9),
    _PmHardwareVpdManufDate_Type()
)
pmHardwareVpdManufDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmHardwareVpdManufDate.setStatus("mandatory")
_PmHardwareVpdPartNumber_Type = OctetString
_PmHardwareVpdPartNumber_Object = MibTableColumn
pmHardwareVpdPartNumber = _PmHardwareVpdPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 8, 1, 1, 10),
    _PmHardwareVpdPartNumber_Type()
)
pmHardwareVpdPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmHardwareVpdPartNumber.setStatus("mandatory")
_PmHardwareVpdFruSerial_Type = OctetString
_PmHardwareVpdFruSerial_Object = MibTableColumn
pmHardwareVpdFruSerial = _PmHardwareVpdFruSerial_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 8, 1, 1, 11),
    _PmHardwareVpdFruSerial_Type()
)
pmHardwareVpdFruSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmHardwareVpdFruSerial.setStatus("mandatory")
_MtHardwareVpd_ObjectIdentity = ObjectIdentity
mtHardwareVpd = _MtHardwareVpd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 9)
)
_MtHardwareVpdManufacturingId_Type = OctetString
_MtHardwareVpdManufacturingId_Object = MibScalar
mtHardwareVpdManufacturingId = _MtHardwareVpdManufacturingId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 9, 3),
    _MtHardwareVpdManufacturingId_Type()
)
mtHardwareVpdManufacturingId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtHardwareVpdManufacturingId.setStatus("mandatory")
_MtHardwareVpdFruNumber_Type = OctetString
_MtHardwareVpdFruNumber_Object = MibScalar
mtHardwareVpdFruNumber = _MtHardwareVpdFruNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 9, 4),
    _MtHardwareVpdFruNumber_Type()
)
mtHardwareVpdFruNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtHardwareVpdFruNumber.setStatus("mandatory")
_MtHardwareVpdHardwareRevision_Type = Integer32
_MtHardwareVpdHardwareRevision_Object = MibScalar
mtHardwareVpdHardwareRevision = _MtHardwareVpdHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 9, 5),
    _MtHardwareVpdHardwareRevision_Type()
)
mtHardwareVpdHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtHardwareVpdHardwareRevision.setStatus("mandatory")
_MtHardwareVpdUuid_Type = OctetString
_MtHardwareVpdUuid_Object = MibScalar
mtHardwareVpdUuid = _MtHardwareVpdUuid_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 9, 8),
    _MtHardwareVpdUuid_Type()
)
mtHardwareVpdUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtHardwareVpdUuid.setStatus("mandatory")
_InventoryManagementVpdTable_Object = MibTable
inventoryManagementVpdTable = _InventoryManagementVpdTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 21)
)
if mibBuilder.loadTexts:
    inventoryManagementVpdTable.setStatus("mandatory")
_InventoryManagementVpdEntry_Object = MibTableRow
inventoryManagementVpdEntry = _InventoryManagementVpdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 21, 1)
)
inventoryManagementVpdEntry.setIndexNames(
    (0, "BLADE-MIB", "componentLevelVpdIndex"),
)
if mibBuilder.loadTexts:
    inventoryManagementVpdEntry.setStatus("mandatory")
_ComponentLevelVpdIndex_Type = Integer32
_ComponentLevelVpdIndex_Object = MibTableColumn
componentLevelVpdIndex = _ComponentLevelVpdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 21, 1, 1),
    _ComponentLevelVpdIndex_Type()
)
componentLevelVpdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentLevelVpdIndex.setStatus("mandatory")
_ComponentLevelVpdFruNumber_Type = OctetString
_ComponentLevelVpdFruNumber_Object = MibTableColumn
componentLevelVpdFruNumber = _ComponentLevelVpdFruNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 21, 1, 2),
    _ComponentLevelVpdFruNumber_Type()
)
componentLevelVpdFruNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentLevelVpdFruNumber.setStatus("mandatory")
_ComponentLevelVpdSerialNumber_Type = OctetString
_ComponentLevelVpdSerialNumber_Object = MibTableColumn
componentLevelVpdSerialNumber = _ComponentLevelVpdSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 21, 1, 3),
    _ComponentLevelVpdSerialNumber_Type()
)
componentLevelVpdSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentLevelVpdSerialNumber.setStatus("mandatory")
_ComponentLevelVpdManufacturingId_Type = OctetString
_ComponentLevelVpdManufacturingId_Object = MibTableColumn
componentLevelVpdManufacturingId = _ComponentLevelVpdManufacturingId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 21, 1, 4),
    _ComponentLevelVpdManufacturingId_Type()
)
componentLevelVpdManufacturingId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentLevelVpdManufacturingId.setStatus("mandatory")
_ComponentLevelVpdBayNumber_Type = OctetString
_ComponentLevelVpdBayNumber_Object = MibTableColumn
componentLevelVpdBayNumber = _ComponentLevelVpdBayNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 21, 1, 5),
    _ComponentLevelVpdBayNumber_Type()
)
componentLevelVpdBayNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentLevelVpdBayNumber.setStatus("mandatory")


class _ComponentLevelVpdTypeCode_Type(Integer32):
    """Custom type componentLevelVpdTypeCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              17,
              18,
              19,
              20,
              21,
              33,
              34,
              35,
              40,
              47,
              81,
              97,
              113,
              129)
        )
    )
    namedValues = NamedValues(
        *(("bladeEthernetDaughterCard", 33),
          ("bladeFiberChannelDaughterCard", 34),
          ("bladeStorageExpansionUnit", 35),
          ("bladeX86FourWay", 4),
          ("bladeX86OneWay", 1),
          ("bladeX86TwoWay", 2),
          ("chassis", 97),
          ("managementModule", 81),
          ("mediaTray", 129),
          ("powerModule", 113),
          ("scalabilityPortModule", 19),
          ("serialPortExpansionCard", 47),
          ("switchModuleCopperPassThrough", 40),
          ("switchModuleEthernet", 17),
          ("switchModuleFiberChannel", 18),
          ("switchModuleInfiniband", 20),
          ("switchModuleMixedProtocol", 21),
          ("unknown", 0))
    )


_ComponentLevelVpdTypeCode_Type.__name__ = "Integer32"
_ComponentLevelVpdTypeCode_Object = MibTableColumn
componentLevelVpdTypeCode = _ComponentLevelVpdTypeCode_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 21, 1, 6),
    _ComponentLevelVpdTypeCode_Type()
)
componentLevelVpdTypeCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentLevelVpdTypeCode.setStatus("mandatory")
_ComponentLevelVpdMachineType_Type = OctetString
_ComponentLevelVpdMachineType_Object = MibTableColumn
componentLevelVpdMachineType = _ComponentLevelVpdMachineType_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 21, 1, 7),
    _ComponentLevelVpdMachineType_Type()
)
componentLevelVpdMachineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentLevelVpdMachineType.setStatus("mandatory")
_ComponentLevelVpdHardwareRevision_Type = Integer32
_ComponentLevelVpdHardwareRevision_Object = MibTableColumn
componentLevelVpdHardwareRevision = _ComponentLevelVpdHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 21, 1, 8),
    _ComponentLevelVpdHardwareRevision_Type()
)
componentLevelVpdHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentLevelVpdHardwareRevision.setStatus("mandatory")
_InventoryManagementActivityVpdTable_Object = MibTable
inventoryManagementActivityVpdTable = _InventoryManagementActivityVpdTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 22)
)
if mibBuilder.loadTexts:
    inventoryManagementActivityVpdTable.setStatus("mandatory")
_InventoryManagementActivityVpdEntry_Object = MibTableRow
inventoryManagementActivityVpdEntry = _InventoryManagementActivityVpdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 22, 1)
)
inventoryManagementActivityVpdEntry.setIndexNames(
    (0, "BLADE-MIB", "componentLevelActivityVpdIndex"),
)
if mibBuilder.loadTexts:
    inventoryManagementActivityVpdEntry.setStatus("mandatory")
_ComponentLevelActivityVpdIndex_Type = Integer32
_ComponentLevelActivityVpdIndex_Object = MibTableColumn
componentLevelActivityVpdIndex = _ComponentLevelActivityVpdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 22, 1, 1),
    _ComponentLevelActivityVpdIndex_Type()
)
componentLevelActivityVpdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentLevelActivityVpdIndex.setStatus("mandatory")
_ComponentLevelActivityVpdFruNumber_Type = OctetString
_ComponentLevelActivityVpdFruNumber_Object = MibTableColumn
componentLevelActivityVpdFruNumber = _ComponentLevelActivityVpdFruNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 22, 1, 2),
    _ComponentLevelActivityVpdFruNumber_Type()
)
componentLevelActivityVpdFruNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentLevelActivityVpdFruNumber.setStatus("mandatory")
_ComponentLevelActivityVpdSerialNumber_Type = OctetString
_ComponentLevelActivityVpdSerialNumber_Object = MibTableColumn
componentLevelActivityVpdSerialNumber = _ComponentLevelActivityVpdSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 22, 1, 3),
    _ComponentLevelActivityVpdSerialNumber_Type()
)
componentLevelActivityVpdSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentLevelActivityVpdSerialNumber.setStatus("mandatory")
_ComponentLevelActivityVpdManufacturingId_Type = OctetString
_ComponentLevelActivityVpdManufacturingId_Object = MibTableColumn
componentLevelActivityVpdManufacturingId = _ComponentLevelActivityVpdManufacturingId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 22, 1, 4),
    _ComponentLevelActivityVpdManufacturingId_Type()
)
componentLevelActivityVpdManufacturingId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentLevelActivityVpdManufacturingId.setStatus("mandatory")
_ComponentLevelActivityVpdBayNumber_Type = OctetString
_ComponentLevelActivityVpdBayNumber_Object = MibTableColumn
componentLevelActivityVpdBayNumber = _ComponentLevelActivityVpdBayNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 22, 1, 5),
    _ComponentLevelActivityVpdBayNumber_Type()
)
componentLevelActivityVpdBayNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentLevelActivityVpdBayNumber.setStatus("mandatory")
_ComponentLevelActivityVpdAction_Type = OctetString
_ComponentLevelActivityVpdAction_Object = MibTableColumn
componentLevelActivityVpdAction = _ComponentLevelActivityVpdAction_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 22, 1, 9),
    _ComponentLevelActivityVpdAction_Type()
)
componentLevelActivityVpdAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentLevelActivityVpdAction.setStatus("mandatory")
_ComponentLevelActivityVpdTimestamp_Type = OctetString
_ComponentLevelActivityVpdTimestamp_Object = MibTableColumn
componentLevelActivityVpdTimestamp = _ComponentLevelActivityVpdTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 2, 21, 22, 1, 10),
    _ComponentLevelActivityVpdTimestamp_Type()
)
componentLevelActivityVpdTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentLevelActivityVpdTimestamp.setStatus("mandatory")
_ErrorLogs_ObjectIdentity = ObjectIdentity
errorLogs = _ErrorLogs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 3)
)
_EventLog_ObjectIdentity = ObjectIdentity
eventLog = _EventLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 3, 4)
)
_ReadEventLogTable_Object = MibTable
readEventLogTable = _ReadEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 3, 4, 2)
)
if mibBuilder.loadTexts:
    readEventLogTable.setStatus("mandatory")
_ReadEventLogEntry_Object = MibTableRow
readEventLogEntry = _ReadEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 3, 4, 2, 1)
)
readEventLogEntry.setIndexNames(
    (0, "BLADE-MIB", "readEventLogIndex"),
)
if mibBuilder.loadTexts:
    readEventLogEntry.setStatus("mandatory")
_ReadEventLogIndex_Type = Integer32
_ReadEventLogIndex_Object = MibTableColumn
readEventLogIndex = _ReadEventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 3, 4, 2, 1, 1),
    _ReadEventLogIndex_Type()
)
readEventLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    readEventLogIndex.setStatus("mandatory")
_ReadEventLogString_Type = OctetString
_ReadEventLogString_Object = MibTableColumn
readEventLogString = _ReadEventLogString_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 3, 4, 2, 1, 2),
    _ReadEventLogString_Type()
)
readEventLogString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    readEventLogString.setStatus("mandatory")


class _ClearEventLog_Type(Integer32):
    """Custom type clearEventLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("execute", 1)
    )


_ClearEventLog_Type.__name__ = "Integer32"
_ClearEventLog_Object = MibScalar
clearEventLog = _ClearEventLog_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 3, 4, 3),
    _ClearEventLog_Type()
)
clearEventLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearEventLog.setStatus("mandatory")


class _MonitorLogStateEvents_Type(Integer32):
    """Custom type monitorLogStateEvents based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MonitorLogStateEvents_Type.__name__ = "Integer32"
_MonitorLogStateEvents_Object = MibScalar
monitorLogStateEvents = _MonitorLogStateEvents_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 3, 4, 4),
    _MonitorLogStateEvents_Type()
)
monitorLogStateEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorLogStateEvents.setStatus("mandatory")
_ConfigureSP_ObjectIdentity = ObjectIdentity
configureSP = _ConfigureSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4)
)
_RemoteAccessConfig_ObjectIdentity = ObjectIdentity
remoteAccessConfig = _RemoteAccessConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1)
)
_GeneralRemoteCfg_ObjectIdentity = ObjectIdentity
generalRemoteCfg = _GeneralRemoteCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 1)
)


class _RemoteAlertRetryCount_Type(Integer32):
    """Custom type remoteAlertRetryCount based on Integer32"""
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
        *(("noretry", 0),
          ("retry1", 1),
          ("retry2", 2),
          ("retry3", 3),
          ("retry4", 4),
          ("retry5", 5),
          ("retry6", 6),
          ("retry7", 7),
          ("retry8", 8))
    )


_RemoteAlertRetryCount_Type.__name__ = "Integer32"
_RemoteAlertRetryCount_Object = MibScalar
remoteAlertRetryCount = _RemoteAlertRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 1, 4),
    _RemoteAlertRetryCount_Type()
)
remoteAlertRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAlertRetryCount.setStatus("mandatory")


class _RemoteAlertRetryDelay_Type(Integer32):
    """Custom type remoteAlertRetryDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              30,
              60,
              90,
              120,
              150,
              180,
              210,
              240)
        )
    )
    namedValues = NamedValues(
        *(("fourMinutes", 240),
          ("noDelay", 0),
          ("oneAndHalfMinutes", 90),
          ("oneHalfMinute", 30),
          ("oneMinute", 60),
          ("threeAndHalfMinutes", 210),
          ("threeMinutes", 180),
          ("twoAndHalfMinutes", 150),
          ("twoMinutes", 120))
    )


_RemoteAlertRetryDelay_Type.__name__ = "Integer32"
_RemoteAlertRetryDelay_Object = MibScalar
remoteAlertRetryDelay = _RemoteAlertRetryDelay_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 1, 5),
    _RemoteAlertRetryDelay_Type()
)
remoteAlertRetryDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAlertRetryDelay.setStatus("mandatory")


class _RemoteAccessTamperDelay_Type(Integer32):
    """Custom type remoteAccessTamperDelay based on Integer32"""
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
              10,
              15,
              20,
              30,
              60,
              120,
              180,
              240)
        )
    )
    namedValues = NamedValues(
        *(("fifteenMinutes", 15),
          ("fiveMinutes", 5),
          ("fourMinutes", 4),
          ("nowait", 0),
          ("oneEightyMinutes", 180),
          ("oneMinute", 1),
          ("oneTwentyMinutes", 120),
          ("sevenMinutes", 7),
          ("sixMinutes", 6),
          ("sixtyMinutes", 60),
          ("tenMinutes", 10),
          ("thirtyMinutes", 30),
          ("threeMinutes", 3),
          ("twentyMinutes", 20),
          ("twoFortyMinutes", 240),
          ("twoMinutes", 2))
    )


_RemoteAccessTamperDelay_Type.__name__ = "Integer32"
_RemoteAccessTamperDelay_Object = MibScalar
remoteAccessTamperDelay = _RemoteAccessTamperDelay_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 1, 6),
    _RemoteAccessTamperDelay_Type()
)
remoteAccessTamperDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAccessTamperDelay.setStatus("mandatory")


class _UserAuthenticationMethod_Type(Integer32):
    """Custom type userAuthenticationMethod based on Integer32"""
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
        *(("ldapFirstThenLocal", 3),
          ("ldapOnly", 1),
          ("localFirstThenLdap", 2),
          ("localOnly", 0))
    )


_UserAuthenticationMethod_Type.__name__ = "Integer32"
_UserAuthenticationMethod_Object = MibScalar
userAuthenticationMethod = _UserAuthenticationMethod_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 1, 7),
    _UserAuthenticationMethod_Type()
)
userAuthenticationMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAuthenticationMethod.setStatus("mandatory")


class _AllowModemLogin_Type(Integer32):
    """Custom type allowModemLogin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AllowModemLogin_Type.__name__ = "Integer32"
_AllowModemLogin_Object = MibScalar
allowModemLogin = _AllowModemLogin_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 1, 8),
    _AllowModemLogin_Type()
)
allowModemLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    allowModemLogin.setStatus("mandatory")
_RemoteAlertIds_ObjectIdentity = ObjectIdentity
remoteAlertIds = _RemoteAlertIds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 3)
)
_RemoteAlertIdsTable_Object = MibTable
remoteAlertIdsTable = _RemoteAlertIdsTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    remoteAlertIdsTable.setStatus("mandatory")
_RemoteAlertIdsEntry_Object = MibTableRow
remoteAlertIdsEntry = _RemoteAlertIdsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 3, 1, 1)
)
remoteAlertIdsEntry.setIndexNames(
    (0, "BLADE-MIB", "remoteAlertIdEntryIndex"),
)
if mibBuilder.loadTexts:
    remoteAlertIdsEntry.setStatus("mandatory")
_RemoteAlertIdEntryIndex_Type = Integer32
_RemoteAlertIdEntryIndex_Object = MibTableColumn
remoteAlertIdEntryIndex = _RemoteAlertIdEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 3, 1, 1, 1),
    _RemoteAlertIdEntryIndex_Type()
)
remoteAlertIdEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAlertIdEntryIndex.setStatus("mandatory")


class _RemoteAlertIdEntryStatus_Type(Integer32):
    """Custom type remoteAlertIdEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabledAndValid", 1),
          ("enabledAndValid", 2),
          ("invalid", 0))
    )


_RemoteAlertIdEntryStatus_Type.__name__ = "Integer32"
_RemoteAlertIdEntryStatus_Object = MibTableColumn
remoteAlertIdEntryStatus = _RemoteAlertIdEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 3, 1, 1, 2),
    _RemoteAlertIdEntryStatus_Type()
)
remoteAlertIdEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAlertIdEntryStatus.setStatus("mandatory")


class _RemoteAlertIdEntryIpOrHostAddress_Type(OctetString):
    """Custom type remoteAlertIdEntryIpOrHostAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_RemoteAlertIdEntryIpOrHostAddress_Type.__name__ = "OctetString"
_RemoteAlertIdEntryIpOrHostAddress_Object = MibTableColumn
remoteAlertIdEntryIpOrHostAddress = _RemoteAlertIdEntryIpOrHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 3, 1, 1, 3),
    _RemoteAlertIdEntryIpOrHostAddress_Type()
)
remoteAlertIdEntryIpOrHostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAlertIdEntryIpOrHostAddress.setStatus("mandatory")


class _RemoteAlertIdEntryTextDescription_Type(OctetString):
    """Custom type remoteAlertIdEntryTextDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_RemoteAlertIdEntryTextDescription_Type.__name__ = "OctetString"
_RemoteAlertIdEntryTextDescription_Object = MibTableColumn
remoteAlertIdEntryTextDescription = _RemoteAlertIdEntryTextDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 3, 1, 1, 4),
    _RemoteAlertIdEntryTextDescription_Type()
)
remoteAlertIdEntryTextDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAlertIdEntryTextDescription.setStatus("mandatory")


class _RemoteAlertIdEntryNotificationType_Type(Integer32):
    """Custom type remoteAlertIdEntryNotificationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
              5,
              8)
        )
    )
    namedValues = NamedValues(
        *(("emailOverLan", 5),
          ("ibmDirectorOverLAN", 8),
          ("snmpOverLan", 4),
          ("unknown", 0))
    )


_RemoteAlertIdEntryNotificationType_Type.__name__ = "Integer32"
_RemoteAlertIdEntryNotificationType_Object = MibTableColumn
remoteAlertIdEntryNotificationType = _RemoteAlertIdEntryNotificationType_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 3, 1, 1, 5),
    _RemoteAlertIdEntryNotificationType_Type()
)
remoteAlertIdEntryNotificationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAlertIdEntryNotificationType.setStatus("mandatory")


class _RemoteAlertIdEmailAddr_Type(OctetString):
    """Custom type remoteAlertIdEmailAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RemoteAlertIdEmailAddr_Type.__name__ = "OctetString"
_RemoteAlertIdEmailAddr_Object = MibTableColumn
remoteAlertIdEmailAddr = _RemoteAlertIdEmailAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 3, 1, 1, 9),
    _RemoteAlertIdEmailAddr_Type()
)
remoteAlertIdEmailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAlertIdEmailAddr.setStatus("mandatory")


class _RemoteAlertIdEntrySelectiveAlert_Type(Integer32):
    """Custom type remoteAlertIdEntrySelectiveAlert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allAlerts", 1),
          ("critOnlyAlerts", 0))
    )


_RemoteAlertIdEntrySelectiveAlert_Type.__name__ = "Integer32"
_RemoteAlertIdEntrySelectiveAlert_Object = MibTableColumn
remoteAlertIdEntrySelectiveAlert = _RemoteAlertIdEntrySelectiveAlert_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 3, 1, 1, 13),
    _RemoteAlertIdEntrySelectiveAlert_Type()
)
remoteAlertIdEntrySelectiveAlert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAlertIdEntrySelectiveAlert.setStatus("mandatory")


class _GenerateTestAlert_Type(Integer32):
    """Custom type generateTestAlert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("execute", 1)
    )


_GenerateTestAlert_Type.__name__ = "Integer32"
_GenerateTestAlert_Object = MibScalar
generateTestAlert = _GenerateTestAlert_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 3, 30),
    _GenerateTestAlert_Type()
)
generateTestAlert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generateTestAlert.setStatus("mandatory")
_RemoteAccessIds_ObjectIdentity = ObjectIdentity
remoteAccessIds = _RemoteAccessIds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4)
)
_RemoteAccessIdsTable_Object = MibTable
remoteAccessIdsTable = _RemoteAccessIdsTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 1)
)
if mibBuilder.loadTexts:
    remoteAccessIdsTable.setStatus("mandatory")
_RemoteAccessIdsEntry_Object = MibTableRow
remoteAccessIdsEntry = _RemoteAccessIdsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 1, 1)
)
remoteAccessIdsEntry.setIndexNames(
    (0, "BLADE-MIB", "remoteAccessIdEntryIndex"),
)
if mibBuilder.loadTexts:
    remoteAccessIdsEntry.setStatus("mandatory")


class _RemoteAccessIdEntryIndex_Type(Integer32):
    """Custom type remoteAccessIdEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RemoteAccessIdEntryIndex_Type.__name__ = "Integer32"
_RemoteAccessIdEntryIndex_Object = MibTableColumn
remoteAccessIdEntryIndex = _RemoteAccessIdEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 1, 1, 1),
    _RemoteAccessIdEntryIndex_Type()
)
remoteAccessIdEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAccessIdEntryIndex.setStatus("mandatory")


class _RemoteAccessIdEntryUserId_Type(OctetString):
    """Custom type remoteAccessIdEntryUserId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RemoteAccessIdEntryUserId_Type.__name__ = "OctetString"
_RemoteAccessIdEntryUserId_Object = MibTableColumn
remoteAccessIdEntryUserId = _RemoteAccessIdEntryUserId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 1, 1, 2),
    _RemoteAccessIdEntryUserId_Type()
)
remoteAccessIdEntryUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAccessIdEntryUserId.setStatus("mandatory")


class _RemoteAccessIdEntryPassword_Type(OctetString):
    """Custom type remoteAccessIdEntryPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RemoteAccessIdEntryPassword_Type.__name__ = "OctetString"
_RemoteAccessIdEntryPassword_Object = MibTableColumn
remoteAccessIdEntryPassword = _RemoteAccessIdEntryPassword_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 1, 1, 3),
    _RemoteAccessIdEntryPassword_Type()
)
remoteAccessIdEntryPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAccessIdEntryPassword.setStatus("mandatory")


class _RemoteAccessIdEntryEncodedLoginPw_Type(OctetString):
    """Custom type remoteAccessIdEntryEncodedLoginPw based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_RemoteAccessIdEntryEncodedLoginPw_Type.__name__ = "OctetString"
_RemoteAccessIdEntryEncodedLoginPw_Object = MibTableColumn
remoteAccessIdEntryEncodedLoginPw = _RemoteAccessIdEntryEncodedLoginPw_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 1, 1, 7),
    _RemoteAccessIdEntryEncodedLoginPw_Type()
)
remoteAccessIdEntryEncodedLoginPw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAccessIdEntryEncodedLoginPw.setStatus("mandatory")
_RemoteAccessUserAuthorityLevelTable_Object = MibTable
remoteAccessUserAuthorityLevelTable = _RemoteAccessUserAuthorityLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 2)
)
if mibBuilder.loadTexts:
    remoteAccessUserAuthorityLevelTable.setStatus("mandatory")
_RemoteAccessUserAuthorityLevelEntry_Object = MibTableRow
remoteAccessUserAuthorityLevelEntry = _RemoteAccessUserAuthorityLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 2, 1)
)
remoteAccessUserAuthorityLevelEntry.setIndexNames(
    (0, "BLADE-MIB", "ualIndex"),
)
if mibBuilder.loadTexts:
    remoteAccessUserAuthorityLevelEntry.setStatus("mandatory")


class _UalIndex_Type(Integer32):
    """Custom type ualIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UalIndex_Type.__name__ = "Integer32"
_UalIndex_Object = MibTableColumn
ualIndex = _UalIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 2, 1, 1),
    _UalIndex_Type()
)
ualIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ualIndex.setStatus("mandatory")


class _UalId_Type(OctetString):
    """Custom type ualId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_UalId_Type.__name__ = "OctetString"
_UalId_Object = MibTableColumn
ualId = _UalId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 2, 1, 2),
    _UalId_Type()
)
ualId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ualId.setStatus("mandatory")


class _UalSupervisor_Type(Integer32):
    """Custom type ualSupervisor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_UalSupervisor_Type.__name__ = "Integer32"
_UalSupervisor_Object = MibTableColumn
ualSupervisor = _UalSupervisor_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 2, 1, 3),
    _UalSupervisor_Type()
)
ualSupervisor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ualSupervisor.setStatus("mandatory")


class _UalReadOnly_Type(Integer32):
    """Custom type ualReadOnly based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_UalReadOnly_Type.__name__ = "Integer32"
_UalReadOnly_Object = MibTableColumn
ualReadOnly = _UalReadOnly_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 2, 1, 4),
    _UalReadOnly_Type()
)
ualReadOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ualReadOnly.setStatus("mandatory")


class _UalAccountManagement_Type(Integer32):
    """Custom type ualAccountManagement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_UalAccountManagement_Type.__name__ = "Integer32"
_UalAccountManagement_Object = MibTableColumn
ualAccountManagement = _UalAccountManagement_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 2, 1, 5),
    _UalAccountManagement_Type()
)
ualAccountManagement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ualAccountManagement.setStatus("mandatory")


class _UalConsoleAccess_Type(Integer32):
    """Custom type ualConsoleAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_UalConsoleAccess_Type.__name__ = "Integer32"
_UalConsoleAccess_Object = MibTableColumn
ualConsoleAccess = _UalConsoleAccess_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 2, 1, 6),
    _UalConsoleAccess_Type()
)
ualConsoleAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ualConsoleAccess.setStatus("mandatory")


class _UalConsoleAndVirtualMediaAccess_Type(Integer32):
    """Custom type ualConsoleAndVirtualMediaAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_UalConsoleAndVirtualMediaAccess_Type.__name__ = "Integer32"
_UalConsoleAndVirtualMediaAccess_Object = MibTableColumn
ualConsoleAndVirtualMediaAccess = _UalConsoleAndVirtualMediaAccess_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 2, 1, 7),
    _UalConsoleAndVirtualMediaAccess_Type()
)
ualConsoleAndVirtualMediaAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ualConsoleAndVirtualMediaAccess.setStatus("mandatory")


class _UalServerPowerAccess_Type(Integer32):
    """Custom type ualServerPowerAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_UalServerPowerAccess_Type.__name__ = "Integer32"
_UalServerPowerAccess_Object = MibTableColumn
ualServerPowerAccess = _UalServerPowerAccess_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 2, 1, 8),
    _UalServerPowerAccess_Type()
)
ualServerPowerAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ualServerPowerAccess.setStatus("mandatory")


class _UalAllowClearLog_Type(Integer32):
    """Custom type ualAllowClearLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_UalAllowClearLog_Type.__name__ = "Integer32"
_UalAllowClearLog_Object = MibTableColumn
ualAllowClearLog = _UalAllowClearLog_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 2, 1, 9),
    _UalAllowClearLog_Type()
)
ualAllowClearLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ualAllowClearLog.setStatus("mandatory")


class _UalAdapterBasicConfig_Type(Integer32):
    """Custom type ualAdapterBasicConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_UalAdapterBasicConfig_Type.__name__ = "Integer32"
_UalAdapterBasicConfig_Object = MibTableColumn
ualAdapterBasicConfig = _UalAdapterBasicConfig_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 2, 1, 10),
    _UalAdapterBasicConfig_Type()
)
ualAdapterBasicConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ualAdapterBasicConfig.setStatus("mandatory")


class _UalAdapterNetworkAndSecurityConfig_Type(Integer32):
    """Custom type ualAdapterNetworkAndSecurityConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_UalAdapterNetworkAndSecurityConfig_Type.__name__ = "Integer32"
_UalAdapterNetworkAndSecurityConfig_Object = MibTableColumn
ualAdapterNetworkAndSecurityConfig = _UalAdapterNetworkAndSecurityConfig_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 2, 1, 11),
    _UalAdapterNetworkAndSecurityConfig_Type()
)
ualAdapterNetworkAndSecurityConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ualAdapterNetworkAndSecurityConfig.setStatus("mandatory")


class _UalAdapterAdvancedConfig_Type(Integer32):
    """Custom type ualAdapterAdvancedConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_UalAdapterAdvancedConfig_Type.__name__ = "Integer32"
_UalAdapterAdvancedConfig_Object = MibTableColumn
ualAdapterAdvancedConfig = _UalAdapterAdvancedConfig_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 2, 1, 12),
    _UalAdapterAdvancedConfig_Type()
)
ualAdapterAdvancedConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ualAdapterAdvancedConfig.setStatus("mandatory")
_RemoteAccessRBSroleTable_Object = MibTable
remoteAccessRBSroleTable = _RemoteAccessRBSroleTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 3)
)
if mibBuilder.loadTexts:
    remoteAccessRBSroleTable.setStatus("mandatory")
_RemoteAccessRBSroleEntry_Object = MibTableRow
remoteAccessRBSroleEntry = _RemoteAccessRBSroleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 3, 1)
)
remoteAccessRBSroleEntry.setIndexNames(
    (0, "BLADE-MIB", "roleIndex"),
)
if mibBuilder.loadTexts:
    remoteAccessRBSroleEntry.setStatus("mandatory")


class _RoleIndex_Type(Integer32):
    """Custom type roleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RoleIndex_Type.__name__ = "Integer32"
_RoleIndex_Object = MibTableColumn
roleIndex = _RoleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 3, 1, 1),
    _RoleIndex_Type()
)
roleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roleIndex.setStatus("mandatory")


class _RoleId_Type(OctetString):
    """Custom type roleId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RoleId_Type.__name__ = "OctetString"
_RoleId_Object = MibTableColumn
roleId = _RoleId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 3, 1, 2),
    _RoleId_Type()
)
roleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roleId.setStatus("mandatory")


class _RbsSupervisor_Type(Integer32):
    """Custom type rbsSupervisor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RbsSupervisor_Type.__name__ = "Integer32"
_RbsSupervisor_Object = MibTableColumn
rbsSupervisor = _RbsSupervisor_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 3, 1, 3),
    _RbsSupervisor_Type()
)
rbsSupervisor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbsSupervisor.setStatus("mandatory")


class _RbsOperator_Type(Integer32):
    """Custom type rbsOperator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RbsOperator_Type.__name__ = "Integer32"
_RbsOperator_Object = MibTableColumn
rbsOperator = _RbsOperator_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 3, 1, 4),
    _RbsOperator_Type()
)
rbsOperator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbsOperator.setStatus("mandatory")


class _RbsChassisOperator_Type(Integer32):
    """Custom type rbsChassisOperator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RbsChassisOperator_Type.__name__ = "Integer32"
_RbsChassisOperator_Object = MibTableColumn
rbsChassisOperator = _RbsChassisOperator_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 3, 1, 5),
    _RbsChassisOperator_Type()
)
rbsChassisOperator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbsChassisOperator.setStatus("mandatory")


class _RbsChassisAccountManagement_Type(Integer32):
    """Custom type rbsChassisAccountManagement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RbsChassisAccountManagement_Type.__name__ = "Integer32"
_RbsChassisAccountManagement_Object = MibTableColumn
rbsChassisAccountManagement = _RbsChassisAccountManagement_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 3, 1, 6),
    _RbsChassisAccountManagement_Type()
)
rbsChassisAccountManagement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbsChassisAccountManagement.setStatus("mandatory")


class _RbsChassisLogManagement_Type(Integer32):
    """Custom type rbsChassisLogManagement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RbsChassisLogManagement_Type.__name__ = "Integer32"
_RbsChassisLogManagement_Object = MibTableColumn
rbsChassisLogManagement = _RbsChassisLogManagement_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 3, 1, 7),
    _RbsChassisLogManagement_Type()
)
rbsChassisLogManagement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbsChassisLogManagement.setStatus("mandatory")


class _RbsChassisConfiguration_Type(Integer32):
    """Custom type rbsChassisConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RbsChassisConfiguration_Type.__name__ = "Integer32"
_RbsChassisConfiguration_Object = MibTableColumn
rbsChassisConfiguration = _RbsChassisConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 3, 1, 8),
    _RbsChassisConfiguration_Type()
)
rbsChassisConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbsChassisConfiguration.setStatus("mandatory")


class _RbsChassisAdministration_Type(Integer32):
    """Custom type rbsChassisAdministration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RbsChassisAdministration_Type.__name__ = "Integer32"
_RbsChassisAdministration_Object = MibTableColumn
rbsChassisAdministration = _RbsChassisAdministration_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 3, 1, 9),
    _RbsChassisAdministration_Type()
)
rbsChassisAdministration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbsChassisAdministration.setStatus("mandatory")


class _RbsBladeOperator_Type(Integer32):
    """Custom type rbsBladeOperator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RbsBladeOperator_Type.__name__ = "Integer32"
_RbsBladeOperator_Object = MibTableColumn
rbsBladeOperator = _RbsBladeOperator_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 3, 1, 10),
    _RbsBladeOperator_Type()
)
rbsBladeOperator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbsBladeOperator.setStatus("mandatory")


class _RbsBladeRemotePresence_Type(Integer32):
    """Custom type rbsBladeRemotePresence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RbsBladeRemotePresence_Type.__name__ = "Integer32"
_RbsBladeRemotePresence_Object = MibTableColumn
rbsBladeRemotePresence = _RbsBladeRemotePresence_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 3, 1, 11),
    _RbsBladeRemotePresence_Type()
)
rbsBladeRemotePresence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbsBladeRemotePresence.setStatus("mandatory")


class _RbsBladeConfiguration_Type(Integer32):
    """Custom type rbsBladeConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RbsBladeConfiguration_Type.__name__ = "Integer32"
_RbsBladeConfiguration_Object = MibTableColumn
rbsBladeConfiguration = _RbsBladeConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 3, 1, 12),
    _RbsBladeConfiguration_Type()
)
rbsBladeConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbsBladeConfiguration.setStatus("mandatory")


class _RbsBladeAdministration_Type(Integer32):
    """Custom type rbsBladeAdministration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RbsBladeAdministration_Type.__name__ = "Integer32"
_RbsBladeAdministration_Object = MibTableColumn
rbsBladeAdministration = _RbsBladeAdministration_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 3, 1, 13),
    _RbsBladeAdministration_Type()
)
rbsBladeAdministration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbsBladeAdministration.setStatus("mandatory")


class _RbsSwitchModuleOperator_Type(Integer32):
    """Custom type rbsSwitchModuleOperator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RbsSwitchModuleOperator_Type.__name__ = "Integer32"
_RbsSwitchModuleOperator_Object = MibTableColumn
rbsSwitchModuleOperator = _RbsSwitchModuleOperator_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 3, 1, 14),
    _RbsSwitchModuleOperator_Type()
)
rbsSwitchModuleOperator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbsSwitchModuleOperator.setStatus("mandatory")


class _RbsSwitchModuleConfiguration_Type(Integer32):
    """Custom type rbsSwitchModuleConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RbsSwitchModuleConfiguration_Type.__name__ = "Integer32"
_RbsSwitchModuleConfiguration_Object = MibTableColumn
rbsSwitchModuleConfiguration = _RbsSwitchModuleConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 3, 1, 15),
    _RbsSwitchModuleConfiguration_Type()
)
rbsSwitchModuleConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbsSwitchModuleConfiguration.setStatus("mandatory")


class _RbsSwitchModuleAdministration_Type(Integer32):
    """Custom type rbsSwitchModuleAdministration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RbsSwitchModuleAdministration_Type.__name__ = "Integer32"
_RbsSwitchModuleAdministration_Object = MibTableColumn
rbsSwitchModuleAdministration = _RbsSwitchModuleAdministration_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 3, 1, 16),
    _RbsSwitchModuleAdministration_Type()
)
rbsSwitchModuleAdministration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbsSwitchModuleAdministration.setStatus("mandatory")
_RemoteAccessRBSscopeTable_Object = MibTable
remoteAccessRBSscopeTable = _RemoteAccessRBSscopeTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 4)
)
if mibBuilder.loadTexts:
    remoteAccessRBSscopeTable.setStatus("mandatory")
_RemoteAccessRBSscopeEntry_Object = MibTableRow
remoteAccessRBSscopeEntry = _RemoteAccessRBSscopeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 4, 1)
)
remoteAccessRBSscopeEntry.setIndexNames(
    (0, "BLADE-MIB", "scopeIndex"),
)
if mibBuilder.loadTexts:
    remoteAccessRBSscopeEntry.setStatus("mandatory")


class _ScopeIndex_Type(Integer32):
    """Custom type scopeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ScopeIndex_Type.__name__ = "Integer32"
_ScopeIndex_Object = MibTableColumn
scopeIndex = _ScopeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 4, 1, 1),
    _ScopeIndex_Type()
)
scopeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scopeIndex.setStatus("mandatory")


class _ScopeId_Type(OctetString):
    """Custom type scopeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ScopeId_Type.__name__ = "OctetString"
_ScopeId_Object = MibTableColumn
scopeId = _ScopeId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 4, 1, 2),
    _ScopeId_Type()
)
scopeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scopeId.setStatus("mandatory")


class _RbsChassis_Type(Integer32):
    """Custom type rbsChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RbsChassis_Type.__name__ = "Integer32"
_RbsChassis_Object = MibTableColumn
rbsChassis = _RbsChassis_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 4, 1, 3),
    _RbsChassis_Type()
)
rbsChassis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbsChassis.setStatus("mandatory")


class _RbsBlade1_Type(Integer32):
    """Custom type rbsBlade1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RbsBlade1_Type.__name__ = "Integer32"
_RbsBlade1_Object = MibTableColumn
rbsBlade1 = _RbsBlade1_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 4, 1, 4),
    _RbsBlade1_Type()
)
rbsBlade1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbsBlade1.setStatus("mandatory")


class _RbsBlade2_Type(Integer32):
    """Custom type rbsBlade2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RbsBlade2_Type.__name__ = "Integer32"
_RbsBlade2_Object = MibTableColumn
rbsBlade2 = _RbsBlade2_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 4, 1, 5),
    _RbsBlade2_Type()
)
rbsBlade2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbsBlade2.setStatus("mandatory")


class _RbsBlade3_Type(Integer32):
    """Custom type rbsBlade3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RbsBlade3_Type.__name__ = "Integer32"
_RbsBlade3_Object = MibTableColumn
rbsBlade3 = _RbsBlade3_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 4, 1, 6),
    _RbsBlade3_Type()
)
rbsBlade3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbsBlade3.setStatus("mandatory")


class _RbsBlade4_Type(Integer32):
    """Custom type rbsBlade4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RbsBlade4_Type.__name__ = "Integer32"
_RbsBlade4_Object = MibTableColumn
rbsBlade4 = _RbsBlade4_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 4, 1, 7),
    _RbsBlade4_Type()
)
rbsBlade4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbsBlade4.setStatus("mandatory")


class _RbsBlade5_Type(Integer32):
    """Custom type rbsBlade5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RbsBlade5_Type.__name__ = "Integer32"
_RbsBlade5_Object = MibTableColumn
rbsBlade5 = _RbsBlade5_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 4, 1, 8),
    _RbsBlade5_Type()
)
rbsBlade5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbsBlade5.setStatus("mandatory")


class _RbsBlade6_Type(Integer32):
    """Custom type rbsBlade6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RbsBlade6_Type.__name__ = "Integer32"
_RbsBlade6_Object = MibTableColumn
rbsBlade6 = _RbsBlade6_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 4, 1, 9),
    _RbsBlade6_Type()
)
rbsBlade6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbsBlade6.setStatus("mandatory")


class _RbsBlade7_Type(Integer32):
    """Custom type rbsBlade7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RbsBlade7_Type.__name__ = "Integer32"
_RbsBlade7_Object = MibTableColumn
rbsBlade7 = _RbsBlade7_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 4, 1, 10),
    _RbsBlade7_Type()
)
rbsBlade7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbsBlade7.setStatus("mandatory")


class _RbsBlade8_Type(Integer32):
    """Custom type rbsBlade8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RbsBlade8_Type.__name__ = "Integer32"
_RbsBlade8_Object = MibTableColumn
rbsBlade8 = _RbsBlade8_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 4, 1, 11),
    _RbsBlade8_Type()
)
rbsBlade8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbsBlade8.setStatus("mandatory")


class _RbsBlade9_Type(Integer32):
    """Custom type rbsBlade9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RbsBlade9_Type.__name__ = "Integer32"
_RbsBlade9_Object = MibTableColumn
rbsBlade9 = _RbsBlade9_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 4, 1, 12),
    _RbsBlade9_Type()
)
rbsBlade9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbsBlade9.setStatus("mandatory")


class _RbsBlade10_Type(Integer32):
    """Custom type rbsBlade10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RbsBlade10_Type.__name__ = "Integer32"
_RbsBlade10_Object = MibTableColumn
rbsBlade10 = _RbsBlade10_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 4, 1, 13),
    _RbsBlade10_Type()
)
rbsBlade10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbsBlade10.setStatus("mandatory")


class _RbsBlade11_Type(Integer32):
    """Custom type rbsBlade11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RbsBlade11_Type.__name__ = "Integer32"
_RbsBlade11_Object = MibTableColumn
rbsBlade11 = _RbsBlade11_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 4, 1, 14),
    _RbsBlade11_Type()
)
rbsBlade11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbsBlade11.setStatus("mandatory")


class _RbsBlade12_Type(Integer32):
    """Custom type rbsBlade12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RbsBlade12_Type.__name__ = "Integer32"
_RbsBlade12_Object = MibTableColumn
rbsBlade12 = _RbsBlade12_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 4, 1, 15),
    _RbsBlade12_Type()
)
rbsBlade12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbsBlade12.setStatus("mandatory")


class _RbsBlade13_Type(Integer32):
    """Custom type rbsBlade13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RbsBlade13_Type.__name__ = "Integer32"
_RbsBlade13_Object = MibTableColumn
rbsBlade13 = _RbsBlade13_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 4, 1, 16),
    _RbsBlade13_Type()
)
rbsBlade13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbsBlade13.setStatus("mandatory")


class _RbsBlade14_Type(Integer32):
    """Custom type rbsBlade14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RbsBlade14_Type.__name__ = "Integer32"
_RbsBlade14_Object = MibTableColumn
rbsBlade14 = _RbsBlade14_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 4, 1, 17),
    _RbsBlade14_Type()
)
rbsBlade14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbsBlade14.setStatus("mandatory")


class _RbsSwitch1_Type(Integer32):
    """Custom type rbsSwitch1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RbsSwitch1_Type.__name__ = "Integer32"
_RbsSwitch1_Object = MibTableColumn
rbsSwitch1 = _RbsSwitch1_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 4, 1, 18),
    _RbsSwitch1_Type()
)
rbsSwitch1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbsSwitch1.setStatus("mandatory")


class _RbsSwitch2_Type(Integer32):
    """Custom type rbsSwitch2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RbsSwitch2_Type.__name__ = "Integer32"
_RbsSwitch2_Object = MibTableColumn
rbsSwitch2 = _RbsSwitch2_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 4, 1, 19),
    _RbsSwitch2_Type()
)
rbsSwitch2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbsSwitch2.setStatus("mandatory")


class _RbsSwitch3_Type(Integer32):
    """Custom type rbsSwitch3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RbsSwitch3_Type.__name__ = "Integer32"
_RbsSwitch3_Object = MibTableColumn
rbsSwitch3 = _RbsSwitch3_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 4, 1, 20),
    _RbsSwitch3_Type()
)
rbsSwitch3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbsSwitch3.setStatus("mandatory")


class _RbsSwitch4_Type(Integer32):
    """Custom type rbsSwitch4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RbsSwitch4_Type.__name__ = "Integer32"
_RbsSwitch4_Object = MibTableColumn
rbsSwitch4 = _RbsSwitch4_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 1, 4, 4, 1, 21),
    _RbsSwitch4_Type()
)
rbsSwitch4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbsSwitch4.setStatus("mandatory")
_RemoteAlerts_ObjectIdentity = ObjectIdentity
remoteAlerts = _RemoteAlerts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 2)
)
_RemoteAlertsCrit_ObjectIdentity = ObjectIdentity
remoteAlertsCrit = _RemoteAlertsCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 2, 1)
)


class _CritTemp_Type(Integer32):
    """Custom type critTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CritTemp_Type.__name__ = "Integer32"
_CritTemp_Object = MibScalar
critTemp = _CritTemp_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 2, 1, 1),
    _CritTemp_Type()
)
critTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    critTemp.setStatus("mandatory")


class _CritVolt_Type(Integer32):
    """Custom type critVolt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CritVolt_Type.__name__ = "Integer32"
_CritVolt_Object = MibScalar
critVolt = _CritVolt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 2, 1, 2),
    _CritVolt_Type()
)
critVolt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    critVolt.setStatus("mandatory")


class _CritMultiBlower_Type(Integer32):
    """Custom type critMultiBlower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CritMultiBlower_Type.__name__ = "Integer32"
_CritMultiBlower_Object = MibScalar
critMultiBlower = _CritMultiBlower_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 2, 1, 4),
    _CritMultiBlower_Type()
)
critMultiBlower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    critMultiBlower.setStatus("mandatory")


class _CritPower_Type(Integer32):
    """Custom type critPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CritPower_Type.__name__ = "Integer32"
_CritPower_Object = MibScalar
critPower = _CritPower_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 2, 1, 5),
    _CritPower_Type()
)
critPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    critPower.setStatus("mandatory")


class _CritHardDrive_Type(Integer32):
    """Custom type critHardDrive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CritHardDrive_Type.__name__ = "Integer32"
_CritHardDrive_Object = MibScalar
critHardDrive = _CritHardDrive_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 2, 1, 6),
    _CritHardDrive_Type()
)
critHardDrive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    critHardDrive.setStatus("mandatory")


class _CritVRM_Type(Integer32):
    """Custom type critVRM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CritVRM_Type.__name__ = "Integer32"
_CritVRM_Object = MibScalar
critVRM = _CritVRM_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 2, 1, 7),
    _CritVRM_Type()
)
critVRM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    critVRM.setStatus("mandatory")


class _CritMultipleSwitchModule_Type(Integer32):
    """Custom type critMultipleSwitchModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CritMultipleSwitchModule_Type.__name__ = "Integer32"
_CritMultipleSwitchModule_Object = MibScalar
critMultipleSwitchModule = _CritMultipleSwitchModule_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 2, 1, 8),
    _CritMultipleSwitchModule_Type()
)
critMultipleSwitchModule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    critMultipleSwitchModule.setStatus("mandatory")


class _CritInvalidConfig_Type(Integer32):
    """Custom type critInvalidConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CritInvalidConfig_Type.__name__ = "Integer32"
_CritInvalidConfig_Object = MibScalar
critInvalidConfig = _CritInvalidConfig_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 2, 1, 9),
    _CritInvalidConfig_Type()
)
critInvalidConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    critInvalidConfig.setStatus("mandatory")
_RemoteAlertsNonCrit_ObjectIdentity = ObjectIdentity
remoteAlertsNonCrit = _RemoteAlertsNonCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 2, 2)
)


class _WarnSingleBlower_Type(Integer32):
    """Custom type warnSingleBlower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_WarnSingleBlower_Type.__name__ = "Integer32"
_WarnSingleBlower_Object = MibScalar
warnSingleBlower = _WarnSingleBlower_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 2, 2, 2),
    _WarnSingleBlower_Type()
)
warnSingleBlower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    warnSingleBlower.setStatus("mandatory")


class _WarnTemp_Type(Integer32):
    """Custom type warnTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_WarnTemp_Type.__name__ = "Integer32"
_WarnTemp_Object = MibScalar
warnTemp = _WarnTemp_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 2, 2, 3),
    _WarnTemp_Type()
)
warnTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    warnTemp.setStatus("mandatory")


class _WarnVoltage_Type(Integer32):
    """Custom type warnVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_WarnVoltage_Type.__name__ = "Integer32"
_WarnVoltage_Object = MibScalar
warnVoltage = _WarnVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 2, 2, 4),
    _WarnVoltage_Type()
)
warnVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    warnVoltage.setStatus("mandatory")


class _WarnRedundantModule_Type(Integer32):
    """Custom type warnRedundantModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_WarnRedundantModule_Type.__name__ = "Integer32"
_WarnRedundantModule_Object = MibScalar
warnRedundantModule = _WarnRedundantModule_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 2, 2, 6),
    _WarnRedundantModule_Type()
)
warnRedundantModule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    warnRedundantModule.setStatus("mandatory")


class _WarnMediaTrayKVMSwitch_Type(Integer32):
    """Custom type warnMediaTrayKVMSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_WarnMediaTrayKVMSwitch_Type.__name__ = "Integer32"
_WarnMediaTrayKVMSwitch_Object = MibScalar
warnMediaTrayKVMSwitch = _WarnMediaTrayKVMSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 2, 2, 7),
    _WarnMediaTrayKVMSwitch_Type()
)
warnMediaTrayKVMSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    warnMediaTrayKVMSwitch.setStatus("mandatory")
_RemoteAlertsSystem_ObjectIdentity = ObjectIdentity
remoteAlertsSystem = _RemoteAlertsSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 2, 3)
)


class _SystemPowerOff_Type(Integer32):
    """Custom type systemPowerOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SystemPowerOff_Type.__name__ = "Integer32"
_SystemPowerOff_Object = MibScalar
systemPowerOff = _SystemPowerOff_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 2, 3, 4),
    _SystemPowerOff_Type()
)
systemPowerOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemPowerOff.setStatus("mandatory")


class _SystemPowerOn_Type(Integer32):
    """Custom type systemPowerOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SystemPowerOn_Type.__name__ = "Integer32"
_SystemPowerOn_Object = MibScalar
systemPowerOn = _SystemPowerOn_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 2, 3, 5),
    _SystemPowerOn_Type()
)
systemPowerOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemPowerOn.setStatus("mandatory")


class _SystemPFA_Type(Integer32):
    """Custom type systemPFA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SystemPFA_Type.__name__ = "Integer32"
_SystemPFA_Object = MibScalar
systemPFA = _SystemPFA_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 2, 3, 8),
    _SystemPFA_Type()
)
systemPFA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemPFA.setStatus("mandatory")


class _SystemInventory_Type(Integer32):
    """Custom type systemInventory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SystemInventory_Type.__name__ = "Integer32"
_SystemInventory_Object = MibScalar
systemInventory = _SystemInventory_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 2, 3, 10),
    _SystemInventory_Type()
)
systemInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemInventory.setStatus("mandatory")


class _SystemLog75PctFull_Type(Integer32):
    """Custom type systemLog75PctFull based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SystemLog75PctFull_Type.__name__ = "Integer32"
_SystemLog75PctFull_Object = MibScalar
systemLog75PctFull = _SystemLog75PctFull_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 2, 3, 11),
    _SystemLog75PctFull_Type()
)
systemLog75PctFull.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLog75PctFull.setStatus("mandatory")


class _NetworkChangeNotification_Type(Integer32):
    """Custom type networkChangeNotification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NetworkChangeNotification_Type.__name__ = "Integer32"
_NetworkChangeNotification_Object = MibScalar
networkChangeNotification = _NetworkChangeNotification_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 2, 3, 12),
    _NetworkChangeNotification_Type()
)
networkChangeNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkChangeNotification.setStatus("mandatory")


class _SystemBladeThrottling_Type(Integer32):
    """Custom type systemBladeThrottling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SystemBladeThrottling_Type.__name__ = "Integer32"
_SystemBladeThrottling_Object = MibScalar
systemBladeThrottling = _SystemBladeThrottling_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 2, 3, 13),
    _SystemBladeThrottling_Type()
)
systemBladeThrottling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemBladeThrottling.setStatus("mandatory")


class _SystemPowerManagement_Type(Integer32):
    """Custom type systemPowerManagement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SystemPowerManagement_Type.__name__ = "Integer32"
_SystemPowerManagement_Object = MibScalar
systemPowerManagement = _SystemPowerManagement_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 2, 3, 14),
    _SystemPowerManagement_Type()
)
systemPowerManagement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemPowerManagement.setStatus("mandatory")
_SpClock_ObjectIdentity = ObjectIdentity
spClock = _SpClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 4)
)
_SpClockDateAndTimeSetting_Type = OctetString
_SpClockDateAndTimeSetting_Object = MibScalar
spClockDateAndTimeSetting = _SpClockDateAndTimeSetting_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 4, 1),
    _SpClockDateAndTimeSetting_Type()
)
spClockDateAndTimeSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spClockDateAndTimeSetting.setStatus("mandatory")
_SpClockTimezoneSetting_Type = OctetString
_SpClockTimezoneSetting_Object = MibScalar
spClockTimezoneSetting = _SpClockTimezoneSetting_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 4, 2),
    _SpClockTimezoneSetting_Type()
)
spClockTimezoneSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spClockTimezoneSetting.setStatus("mandatory")
_SpIdentification_ObjectIdentity = ObjectIdentity
spIdentification = _SpIdentification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 5)
)


class _SpTxtId_Type(OctetString):
    """Custom type spTxtId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SpTxtId_Type.__name__ = "OctetString"
_SpTxtId_Object = MibScalar
spTxtId = _SpTxtId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 5, 1),
    _SpTxtId_Type()
)
spTxtId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spTxtId.setStatus("mandatory")
_NetworkConfiguration_ObjectIdentity = ObjectIdentity
networkConfiguration = _NetworkConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9)
)
_NetworkInterfaces_ObjectIdentity = ObjectIdentity
networkInterfaces = _NetworkInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 1)
)
_ExtEthernetInterface_ObjectIdentity = ObjectIdentity
extEthernetInterface = _ExtEthernetInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 1, 1)
)


class _ExtEthernetInterfaceType_Type(OctetString):
    """Custom type extEthernetInterfaceType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ExtEthernetInterfaceType_Type.__name__ = "OctetString"
_ExtEthernetInterfaceType_Object = MibScalar
extEthernetInterfaceType = _ExtEthernetInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 1, 1, 1),
    _ExtEthernetInterfaceType_Type()
)
extEthernetInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extEthernetInterfaceType.setStatus("mandatory")


class _ExtEthernetInterfaceHostName_Type(OctetString):
    """Custom type extEthernetInterfaceHostName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ExtEthernetInterfaceHostName_Type.__name__ = "OctetString"
_ExtEthernetInterfaceHostName_Object = MibScalar
extEthernetInterfaceHostName = _ExtEthernetInterfaceHostName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 1, 1, 3),
    _ExtEthernetInterfaceHostName_Type()
)
extEthernetInterfaceHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extEthernetInterfaceHostName.setStatus("mandatory")
_ExtEthernetInterfaceIPAddress_Type = IpAddress
_ExtEthernetInterfaceIPAddress_Object = MibScalar
extEthernetInterfaceIPAddress = _ExtEthernetInterfaceIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 1, 1, 4),
    _ExtEthernetInterfaceIPAddress_Type()
)
extEthernetInterfaceIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extEthernetInterfaceIPAddress.setStatus("mandatory")


class _ExtEthernetInterfaceDataRate_Type(Integer32):
    """Custom type extEthernetInterfaceDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("autoSpeed", 5),
          ("enet100Megabit", 4),
          ("enet10Megabit", 3))
    )


_ExtEthernetInterfaceDataRate_Type.__name__ = "Integer32"
_ExtEthernetInterfaceDataRate_Object = MibScalar
extEthernetInterfaceDataRate = _ExtEthernetInterfaceDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 1, 1, 5),
    _ExtEthernetInterfaceDataRate_Type()
)
extEthernetInterfaceDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extEthernetInterfaceDataRate.setStatus("mandatory")


class _ExtEthernetInterfaceDuplexSetting_Type(Integer32):
    """Custom type extEthernetInterfaceDuplexSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoDuplex", 3),
          ("fullDuplex", 1),
          ("halfDuplex", 2))
    )


_ExtEthernetInterfaceDuplexSetting_Type.__name__ = "Integer32"
_ExtEthernetInterfaceDuplexSetting_Object = MibScalar
extEthernetInterfaceDuplexSetting = _ExtEthernetInterfaceDuplexSetting_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 1, 1, 6),
    _ExtEthernetInterfaceDuplexSetting_Type()
)
extEthernetInterfaceDuplexSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extEthernetInterfaceDuplexSetting.setStatus("mandatory")


class _ExtEthernetInterfaceLAA_Type(OctetString):
    """Custom type extEthernetInterfaceLAA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_ExtEthernetInterfaceLAA_Type.__name__ = "OctetString"
_ExtEthernetInterfaceLAA_Object = MibScalar
extEthernetInterfaceLAA = _ExtEthernetInterfaceLAA_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 1, 1, 7),
    _ExtEthernetInterfaceLAA_Type()
)
extEthernetInterfaceLAA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extEthernetInterfaceLAA.setStatus("mandatory")


class _ExtEthernetInterfaceDhcpEnabled_Type(Integer32):
    """Custom type extEthernetInterfaceDhcpEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcpDisabled", 0),
          ("dhcpEnabled", 1),
          ("tryDhcpThenTryStatic", 2))
    )


_ExtEthernetInterfaceDhcpEnabled_Type.__name__ = "Integer32"
_ExtEthernetInterfaceDhcpEnabled_Object = MibScalar
extEthernetInterfaceDhcpEnabled = _ExtEthernetInterfaceDhcpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 1, 1, 8),
    _ExtEthernetInterfaceDhcpEnabled_Type()
)
extEthernetInterfaceDhcpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extEthernetInterfaceDhcpEnabled.setStatus("mandatory")
_ExtEthernetInterfaceGatewayIPAddress_Type = IpAddress
_ExtEthernetInterfaceGatewayIPAddress_Object = MibScalar
extEthernetInterfaceGatewayIPAddress = _ExtEthernetInterfaceGatewayIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 1, 1, 9),
    _ExtEthernetInterfaceGatewayIPAddress_Type()
)
extEthernetInterfaceGatewayIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extEthernetInterfaceGatewayIPAddress.setStatus("mandatory")


class _ExtEthernetInterfaceBIA_Type(OctetString):
    """Custom type extEthernetInterfaceBIA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_ExtEthernetInterfaceBIA_Type.__name__ = "OctetString"
_ExtEthernetInterfaceBIA_Object = MibScalar
extEthernetInterfaceBIA = _ExtEthernetInterfaceBIA_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 1, 1, 10),
    _ExtEthernetInterfaceBIA_Type()
)
extEthernetInterfaceBIA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extEthernetInterfaceBIA.setStatus("mandatory")
_ExtEthernetInterfaceMTU_Type = Integer32
_ExtEthernetInterfaceMTU_Object = MibScalar
extEthernetInterfaceMTU = _ExtEthernetInterfaceMTU_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 1, 1, 13),
    _ExtEthernetInterfaceMTU_Type()
)
extEthernetInterfaceMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extEthernetInterfaceMTU.setStatus("mandatory")
_ExtEthernetInterfaceSubnetMask_Type = IpAddress
_ExtEthernetInterfaceSubnetMask_Object = MibScalar
extEthernetInterfaceSubnetMask = _ExtEthernetInterfaceSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 1, 1, 14),
    _ExtEthernetInterfaceSubnetMask_Type()
)
extEthernetInterfaceSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extEthernetInterfaceSubnetMask.setStatus("mandatory")
_DhcpEthernetInterface_ObjectIdentity = ObjectIdentity
dhcpEthernetInterface = _DhcpEthernetInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 1, 1, 16)
)


class _DhcpHostName_Type(OctetString):
    """Custom type dhcpHostName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DhcpHostName_Type.__name__ = "OctetString"
_DhcpHostName_Object = MibScalar
dhcpHostName = _DhcpHostName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 1, 1, 16, 1),
    _DhcpHostName_Type()
)
dhcpHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpHostName.setStatus("mandatory")
_DhcpIPAddress_Type = IpAddress
_DhcpIPAddress_Object = MibScalar
dhcpIPAddress = _DhcpIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 1, 1, 16, 2),
    _DhcpIPAddress_Type()
)
dhcpIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpIPAddress.setStatus("mandatory")
_DhcpGatewayIPAddress_Type = IpAddress
_DhcpGatewayIPAddress_Object = MibScalar
dhcpGatewayIPAddress = _DhcpGatewayIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 1, 1, 16, 3),
    _DhcpGatewayIPAddress_Type()
)
dhcpGatewayIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpGatewayIPAddress.setStatus("mandatory")
_DhcpSubnetMask_Type = IpAddress
_DhcpSubnetMask_Object = MibScalar
dhcpSubnetMask = _DhcpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 1, 1, 16, 4),
    _DhcpSubnetMask_Type()
)
dhcpSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSubnetMask.setStatus("mandatory")


class _DhcpDomainName_Type(OctetString):
    """Custom type dhcpDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DhcpDomainName_Type.__name__ = "OctetString"
_DhcpDomainName_Object = MibScalar
dhcpDomainName = _DhcpDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 1, 1, 16, 5),
    _DhcpDomainName_Type()
)
dhcpDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpDomainName.setStatus("mandatory")
_DhcpDHCPServer_Type = IpAddress
_DhcpDHCPServer_Object = MibScalar
dhcpDHCPServer = _DhcpDHCPServer_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 1, 1, 16, 6),
    _DhcpDHCPServer_Type()
)
dhcpDHCPServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpDHCPServer.setStatus("mandatory")
_DhcpPrimaryDNSServer_Type = IpAddress
_DhcpPrimaryDNSServer_Object = MibScalar
dhcpPrimaryDNSServer = _DhcpPrimaryDNSServer_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 1, 1, 16, 7),
    _DhcpPrimaryDNSServer_Type()
)
dhcpPrimaryDNSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPrimaryDNSServer.setStatus("mandatory")
_DhcpSecondaryDNSServer_Type = IpAddress
_DhcpSecondaryDNSServer_Object = MibScalar
dhcpSecondaryDNSServer = _DhcpSecondaryDNSServer_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 1, 1, 16, 8),
    _DhcpSecondaryDNSServer_Type()
)
dhcpSecondaryDNSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSecondaryDNSServer.setStatus("mandatory")
_DhcpTertiaryDNSServer_Type = IpAddress
_DhcpTertiaryDNSServer_Object = MibScalar
dhcpTertiaryDNSServer = _DhcpTertiaryDNSServer_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 1, 1, 16, 9),
    _DhcpTertiaryDNSServer_Type()
)
dhcpTertiaryDNSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpTertiaryDNSServer.setStatus("mandatory")
_IntEthernetInterface_ObjectIdentity = ObjectIdentity
intEthernetInterface = _IntEthernetInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 1, 2)
)


class _IntEthernetInterfaceType_Type(OctetString):
    """Custom type intEthernetInterfaceType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_IntEthernetInterfaceType_Type.__name__ = "OctetString"
_IntEthernetInterfaceType_Object = MibScalar
intEthernetInterfaceType = _IntEthernetInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 1, 2, 1),
    _IntEthernetInterfaceType_Type()
)
intEthernetInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intEthernetInterfaceType.setStatus("mandatory")


class _IntEthernetInterfaceEnabled_Type(Integer32):
    """Custom type intEthernetInterfaceEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("interfaceDisabled", 0),
          ("interfaceEnabled", 1))
    )


_IntEthernetInterfaceEnabled_Type.__name__ = "Integer32"
_IntEthernetInterfaceEnabled_Object = MibScalar
intEthernetInterfaceEnabled = _IntEthernetInterfaceEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 1, 2, 2),
    _IntEthernetInterfaceEnabled_Type()
)
intEthernetInterfaceEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intEthernetInterfaceEnabled.setStatus("mandatory")
_IntEthernetInterfaceLocalIPAddress_Type = IpAddress
_IntEthernetInterfaceLocalIPAddress_Object = MibScalar
intEthernetInterfaceLocalIPAddress = _IntEthernetInterfaceLocalIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 1, 2, 4),
    _IntEthernetInterfaceLocalIPAddress_Type()
)
intEthernetInterfaceLocalIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intEthernetInterfaceLocalIPAddress.setStatus("mandatory")


class _IntEthernetInterfaceDataRate_Type(Integer32):
    """Custom type intEthernetInterfaceDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("autoSpeed", 5),
          ("enet100Megabit", 4),
          ("enet10Megabit", 3))
    )


_IntEthernetInterfaceDataRate_Type.__name__ = "Integer32"
_IntEthernetInterfaceDataRate_Object = MibScalar
intEthernetInterfaceDataRate = _IntEthernetInterfaceDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 1, 2, 5),
    _IntEthernetInterfaceDataRate_Type()
)
intEthernetInterfaceDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intEthernetInterfaceDataRate.setStatus("mandatory")


class _IntEthernetInterfaceDuplexSetting_Type(Integer32):
    """Custom type intEthernetInterfaceDuplexSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoDuplex", 3),
          ("fullDuplex", 1),
          ("halfDuplex", 2))
    )


_IntEthernetInterfaceDuplexSetting_Type.__name__ = "Integer32"
_IntEthernetInterfaceDuplexSetting_Object = MibScalar
intEthernetInterfaceDuplexSetting = _IntEthernetInterfaceDuplexSetting_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 1, 2, 6),
    _IntEthernetInterfaceDuplexSetting_Type()
)
intEthernetInterfaceDuplexSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intEthernetInterfaceDuplexSetting.setStatus("mandatory")


class _IntEthernetInterfaceLAA_Type(OctetString):
    """Custom type intEthernetInterfaceLAA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IntEthernetInterfaceLAA_Type.__name__ = "OctetString"
_IntEthernetInterfaceLAA_Object = MibScalar
intEthernetInterfaceLAA = _IntEthernetInterfaceLAA_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 1, 2, 7),
    _IntEthernetInterfaceLAA_Type()
)
intEthernetInterfaceLAA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intEthernetInterfaceLAA.setStatus("mandatory")
_IntEthernetInterfaceGatewayIPAddress_Type = IpAddress
_IntEthernetInterfaceGatewayIPAddress_Object = MibScalar
intEthernetInterfaceGatewayIPAddress = _IntEthernetInterfaceGatewayIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 1, 2, 9),
    _IntEthernetInterfaceGatewayIPAddress_Type()
)
intEthernetInterfaceGatewayIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intEthernetInterfaceGatewayIPAddress.setStatus("mandatory")


class _IntEthernetInterfaceBIA_Type(OctetString):
    """Custom type intEthernetInterfaceBIA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IntEthernetInterfaceBIA_Type.__name__ = "OctetString"
_IntEthernetInterfaceBIA_Object = MibScalar
intEthernetInterfaceBIA = _IntEthernetInterfaceBIA_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 1, 2, 10),
    _IntEthernetInterfaceBIA_Type()
)
intEthernetInterfaceBIA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intEthernetInterfaceBIA.setStatus("mandatory")
_IntEthernetInterfaceMTU_Type = Integer32
_IntEthernetInterfaceMTU_Object = MibScalar
intEthernetInterfaceMTU = _IntEthernetInterfaceMTU_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 1, 2, 13),
    _IntEthernetInterfaceMTU_Type()
)
intEthernetInterfaceMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intEthernetInterfaceMTU.setStatus("mandatory")
_IntEthernetInterfaceSubnetMask_Type = IpAddress
_IntEthernetInterfaceSubnetMask_Object = MibScalar
intEthernetInterfaceSubnetMask = _IntEthernetInterfaceSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 1, 2, 14),
    _IntEthernetInterfaceSubnetMask_Type()
)
intEthernetInterfaceSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intEthernetInterfaceSubnetMask.setStatus("mandatory")
_TcpProtocols_ObjectIdentity = ObjectIdentity
tcpProtocols = _TcpProtocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3)
)
_SnmpAgentConfig_ObjectIdentity = ObjectIdentity
snmpAgentConfig = _SnmpAgentConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 1)
)


class _SnmpSystemContact_Type(OctetString):
    """Custom type snmpSystemContact based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_SnmpSystemContact_Type.__name__ = "OctetString"
_SnmpSystemContact_Object = MibScalar
snmpSystemContact = _SnmpSystemContact_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 1, 1),
    _SnmpSystemContact_Type()
)
snmpSystemContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpSystemContact.setStatus("mandatory")


class _SnmpSystemLocation_Type(OctetString):
    """Custom type snmpSystemLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_SnmpSystemLocation_Type.__name__ = "OctetString"
_SnmpSystemLocation_Object = MibScalar
snmpSystemLocation = _SnmpSystemLocation_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 1, 2),
    _SnmpSystemLocation_Type()
)
snmpSystemLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpSystemLocation.setStatus("mandatory")


class _SnmpSystemAgentTrapsDisable_Type(Integer32):
    """Custom type snmpSystemAgentTrapsDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("trapsDisabled", 1),
          ("trapsEnabled", 0))
    )


_SnmpSystemAgentTrapsDisable_Type.__name__ = "Integer32"
_SnmpSystemAgentTrapsDisable_Object = MibScalar
snmpSystemAgentTrapsDisable = _SnmpSystemAgentTrapsDisable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 1, 3),
    _SnmpSystemAgentTrapsDisable_Type()
)
snmpSystemAgentTrapsDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpSystemAgentTrapsDisable.setStatus("mandatory")
_SnmpAgentCommunityConfig_ObjectIdentity = ObjectIdentity
snmpAgentCommunityConfig = _SnmpAgentCommunityConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 1, 4)
)
_SnmpCommunityTable_Object = MibTable
snmpCommunityTable = _SnmpCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 1, 4, 1)
)
if mibBuilder.loadTexts:
    snmpCommunityTable.setStatus("mandatory")
_SnmpCommunityEntry_Object = MibTableRow
snmpCommunityEntry = _SnmpCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 1, 4, 1, 1)
)
snmpCommunityEntry.setIndexNames(
    (0, "BLADE-MIB", "snmpCommunityEntryIndex"),
)
if mibBuilder.loadTexts:
    snmpCommunityEntry.setStatus("mandatory")


class _SnmpCommunityEntryIndex_Type(Integer32):
    """Custom type snmpCommunityEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnmpCommunityEntryIndex_Type.__name__ = "Integer32"
_SnmpCommunityEntryIndex_Object = MibTableColumn
snmpCommunityEntryIndex = _SnmpCommunityEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 1, 4, 1, 1, 1),
    _SnmpCommunityEntryIndex_Type()
)
snmpCommunityEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpCommunityEntryIndex.setStatus("mandatory")


class _SnmpCommunityEntryCommunityName_Type(OctetString):
    """Custom type snmpCommunityEntryCommunityName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SnmpCommunityEntryCommunityName_Type.__name__ = "OctetString"
_SnmpCommunityEntryCommunityName_Object = MibTableColumn
snmpCommunityEntryCommunityName = _SnmpCommunityEntryCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 1, 4, 1, 1, 2),
    _SnmpCommunityEntryCommunityName_Type()
)
snmpCommunityEntryCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpCommunityEntryCommunityName.setStatus("mandatory")


class _SnmpCommunityEntryCommunityIpAddress1_Type(OctetString):
    """Custom type snmpCommunityEntryCommunityIpAddress1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SnmpCommunityEntryCommunityIpAddress1_Type.__name__ = "OctetString"
_SnmpCommunityEntryCommunityIpAddress1_Object = MibTableColumn
snmpCommunityEntryCommunityIpAddress1 = _SnmpCommunityEntryCommunityIpAddress1_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 1, 4, 1, 1, 3),
    _SnmpCommunityEntryCommunityIpAddress1_Type()
)
snmpCommunityEntryCommunityIpAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpCommunityEntryCommunityIpAddress1.setStatus("mandatory")


class _SnmpCommunityEntryCommunityIpAddress2_Type(OctetString):
    """Custom type snmpCommunityEntryCommunityIpAddress2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SnmpCommunityEntryCommunityIpAddress2_Type.__name__ = "OctetString"
_SnmpCommunityEntryCommunityIpAddress2_Object = MibTableColumn
snmpCommunityEntryCommunityIpAddress2 = _SnmpCommunityEntryCommunityIpAddress2_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 1, 4, 1, 1, 4),
    _SnmpCommunityEntryCommunityIpAddress2_Type()
)
snmpCommunityEntryCommunityIpAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpCommunityEntryCommunityIpAddress2.setStatus("mandatory")


class _SnmpCommunityEntryCommunityIpAddress3_Type(OctetString):
    """Custom type snmpCommunityEntryCommunityIpAddress3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SnmpCommunityEntryCommunityIpAddress3_Type.__name__ = "OctetString"
_SnmpCommunityEntryCommunityIpAddress3_Object = MibTableColumn
snmpCommunityEntryCommunityIpAddress3 = _SnmpCommunityEntryCommunityIpAddress3_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 1, 4, 1, 1, 5),
    _SnmpCommunityEntryCommunityIpAddress3_Type()
)
snmpCommunityEntryCommunityIpAddress3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpCommunityEntryCommunityIpAddress3.setStatus("mandatory")


class _SnmpCommunityEntryCommunityViewType_Type(Integer32):
    """Custom type snmpCommunityEntryCommunityViewType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("read-Traps", 1),
          ("traps-Only", 3),
          ("write-Read-Traps", 2))
    )


_SnmpCommunityEntryCommunityViewType_Type.__name__ = "Integer32"
_SnmpCommunityEntryCommunityViewType_Object = MibTableColumn
snmpCommunityEntryCommunityViewType = _SnmpCommunityEntryCommunityViewType_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 1, 4, 1, 1, 6),
    _SnmpCommunityEntryCommunityViewType_Type()
)
snmpCommunityEntryCommunityViewType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpCommunityEntryCommunityViewType.setStatus("mandatory")


class _Snmpv1SystemAgentEnable_Type(Integer32):
    """Custom type snmpv1SystemAgentEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Snmpv1SystemAgentEnable_Type.__name__ = "Integer32"
_Snmpv1SystemAgentEnable_Object = MibScalar
snmpv1SystemAgentEnable = _Snmpv1SystemAgentEnable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 1, 5),
    _Snmpv1SystemAgentEnable_Type()
)
snmpv1SystemAgentEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpv1SystemAgentEnable.setStatus("mandatory")


class _Snmpv3SystemAgentEnable_Type(Integer32):
    """Custom type snmpv3SystemAgentEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Snmpv3SystemAgentEnable_Type.__name__ = "Integer32"
_Snmpv3SystemAgentEnable_Object = MibScalar
snmpv3SystemAgentEnable = _Snmpv3SystemAgentEnable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 1, 6),
    _Snmpv3SystemAgentEnable_Type()
)
snmpv3SystemAgentEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpv3SystemAgentEnable.setStatus("mandatory")
_SnmpAgentUserProfileConfig_ObjectIdentity = ObjectIdentity
snmpAgentUserProfileConfig = _SnmpAgentUserProfileConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 1, 9)
)
_SnmpUserProfileTable_Object = MibTable
snmpUserProfileTable = _SnmpUserProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 1, 9, 1)
)
if mibBuilder.loadTexts:
    snmpUserProfileTable.setStatus("mandatory")
_SnmpUserProfileEntry_Object = MibTableRow
snmpUserProfileEntry = _SnmpUserProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 1, 9, 1, 1)
)
snmpUserProfileEntry.setIndexNames(
    (0, "BLADE-MIB", "snmpUserProfileEntryIndex"),
)
if mibBuilder.loadTexts:
    snmpUserProfileEntry.setStatus("mandatory")


class _SnmpUserProfileEntryIndex_Type(Integer32):
    """Custom type snmpUserProfileEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnmpUserProfileEntryIndex_Type.__name__ = "Integer32"
_SnmpUserProfileEntryIndex_Object = MibTableColumn
snmpUserProfileEntryIndex = _SnmpUserProfileEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 1, 9, 1, 1, 1),
    _SnmpUserProfileEntryIndex_Type()
)
snmpUserProfileEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpUserProfileEntryIndex.setStatus("mandatory")


class _SnmpUserProfileEntryContextName_Type(OctetString):
    """Custom type snmpUserProfileEntryContextName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SnmpUserProfileEntryContextName_Type.__name__ = "OctetString"
_SnmpUserProfileEntryContextName_Object = MibTableColumn
snmpUserProfileEntryContextName = _SnmpUserProfileEntryContextName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 1, 9, 1, 1, 3),
    _SnmpUserProfileEntryContextName_Type()
)
snmpUserProfileEntryContextName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpUserProfileEntryContextName.setStatus("mandatory")


class _SnmpUserProfileEntryAuthProt_Type(Integer32):
    """Custom type snmpUserProfileEntryAuthProt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("md5", 2),
          ("none", 1),
          ("sha", 3))
    )


_SnmpUserProfileEntryAuthProt_Type.__name__ = "Integer32"
_SnmpUserProfileEntryAuthProt_Object = MibTableColumn
snmpUserProfileEntryAuthProt = _SnmpUserProfileEntryAuthProt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 1, 9, 1, 1, 4),
    _SnmpUserProfileEntryAuthProt_Type()
)
snmpUserProfileEntryAuthProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpUserProfileEntryAuthProt.setStatus("mandatory")


class _SnmpUserProfileEntryPrivProt_Type(Integer32):
    """Custom type snmpUserProfileEntryPrivProt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("des", 2),
          ("none", 1))
    )


_SnmpUserProfileEntryPrivProt_Type.__name__ = "Integer32"
_SnmpUserProfileEntryPrivProt_Object = MibTableColumn
snmpUserProfileEntryPrivProt = _SnmpUserProfileEntryPrivProt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 1, 9, 1, 1, 6),
    _SnmpUserProfileEntryPrivProt_Type()
)
snmpUserProfileEntryPrivProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpUserProfileEntryPrivProt.setStatus("mandatory")


class _SnmpUserProfileEntryPrivPassword_Type(OctetString):
    """Custom type snmpUserProfileEntryPrivPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SnmpUserProfileEntryPrivPassword_Type.__name__ = "OctetString"
_SnmpUserProfileEntryPrivPassword_Object = MibTableColumn
snmpUserProfileEntryPrivPassword = _SnmpUserProfileEntryPrivPassword_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 1, 9, 1, 1, 7),
    _SnmpUserProfileEntryPrivPassword_Type()
)
snmpUserProfileEntryPrivPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpUserProfileEntryPrivPassword.setStatus("mandatory")


class _SnmpUserProfileEntryViewType_Type(Integer32):
    """Custom type snmpUserProfileEntryViewType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("read-Traps", 1),
          ("read-Write-Traps", 2),
          ("traps-Only", 3))
    )


_SnmpUserProfileEntryViewType_Type.__name__ = "Integer32"
_SnmpUserProfileEntryViewType_Object = MibTableColumn
snmpUserProfileEntryViewType = _SnmpUserProfileEntryViewType_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 1, 9, 1, 1, 8),
    _SnmpUserProfileEntryViewType_Type()
)
snmpUserProfileEntryViewType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpUserProfileEntryViewType.setStatus("mandatory")


class _SnmpUserProfileEntryIpAddress_Type(OctetString):
    """Custom type snmpUserProfileEntryIpAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SnmpUserProfileEntryIpAddress_Type.__name__ = "OctetString"
_SnmpUserProfileEntryIpAddress_Object = MibTableColumn
snmpUserProfileEntryIpAddress = _SnmpUserProfileEntryIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 1, 9, 1, 1, 9),
    _SnmpUserProfileEntryIpAddress_Type()
)
snmpUserProfileEntryIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpUserProfileEntryIpAddress.setStatus("mandatory")
_DnsConfig_ObjectIdentity = ObjectIdentity
dnsConfig = _DnsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 2)
)


class _DnsEnabled_Type(Integer32):
    """Custom type dnsEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dnsDisabled", 0),
          ("dnsEnabled", 1))
    )


_DnsEnabled_Type.__name__ = "Integer32"
_DnsEnabled_Object = MibScalar
dnsEnabled = _DnsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 2, 1),
    _DnsEnabled_Type()
)
dnsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsEnabled.setStatus("mandatory")
_DnsServerIPAddress1_Type = IpAddress
_DnsServerIPAddress1_Object = MibScalar
dnsServerIPAddress1 = _DnsServerIPAddress1_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 2, 2),
    _DnsServerIPAddress1_Type()
)
dnsServerIPAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsServerIPAddress1.setStatus("mandatory")
_DnsServerIPAddress2_Type = IpAddress
_DnsServerIPAddress2_Object = MibScalar
dnsServerIPAddress2 = _DnsServerIPAddress2_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 2, 3),
    _DnsServerIPAddress2_Type()
)
dnsServerIPAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsServerIPAddress2.setStatus("mandatory")
_DnsServerIPAddress3_Type = IpAddress
_DnsServerIPAddress3_Object = MibScalar
dnsServerIPAddress3 = _DnsServerIPAddress3_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 2, 4),
    _DnsServerIPAddress3_Type()
)
dnsServerIPAddress3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsServerIPAddress3.setStatus("mandatory")
_SmtpConfig_ObjectIdentity = ObjectIdentity
smtpConfig = _SmtpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 3)
)


class _SmtpServerNameOrIPAddress_Type(OctetString):
    """Custom type smtpServerNameOrIPAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SmtpServerNameOrIPAddress_Type.__name__ = "OctetString"
_SmtpServerNameOrIPAddress_Object = MibScalar
smtpServerNameOrIPAddress = _SmtpServerNameOrIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 3, 1),
    _SmtpServerNameOrIPAddress_Type()
)
smtpServerNameOrIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpServerNameOrIPAddress.setStatus("mandatory")


class _AttachmentsToEmailAlerts_Type(Integer32):
    """Custom type attachmentsToEmailAlerts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("attachEventLog", 1),
          ("noAttachments", 0))
    )


_AttachmentsToEmailAlerts_Type.__name__ = "Integer32"
_AttachmentsToEmailAlerts_Object = MibScalar
attachmentsToEmailAlerts = _AttachmentsToEmailAlerts_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 3, 2),
    _AttachmentsToEmailAlerts_Type()
)
attachmentsToEmailAlerts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    attachmentsToEmailAlerts.setStatus("mandatory")
_TcpApplicationConfig_ObjectIdentity = ObjectIdentity
tcpApplicationConfig = _TcpApplicationConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 4)
)
_TelnetInactivityTimeout_Type = Integer32
_TelnetInactivityTimeout_Object = MibScalar
telnetInactivityTimeout = _TelnetInactivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 4, 1),
    _TelnetInactivityTimeout_Type()
)
telnetInactivityTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetInactivityTimeout.setStatus("mandatory")
_CommandModeInactivityTimeout_Type = Integer32
_CommandModeInactivityTimeout_Object = MibScalar
commandModeInactivityTimeout = _CommandModeInactivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 4, 2),
    _CommandModeInactivityTimeout_Type()
)
commandModeInactivityTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commandModeInactivityTimeout.setStatus("mandatory")


class _CommandModeEnable_Type(Integer32):
    """Custom type commandModeEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("diabled", 0),
          ("enabled", 1))
    )


_CommandModeEnable_Type.__name__ = "Integer32"
_CommandModeEnable_Object = MibScalar
commandModeEnable = _CommandModeEnable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 4, 4),
    _CommandModeEnable_Type()
)
commandModeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commandModeEnable.setStatus("mandatory")


class _SlpAddrType_Type(Integer32):
    """Custom type slpAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("multicast", 0))
    )


_SlpAddrType_Type.__name__ = "Integer32"
_SlpAddrType_Object = MibScalar
slpAddrType = _SlpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 4, 5),
    _SlpAddrType_Type()
)
slpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slpAddrType.setStatus("mandatory")
_SlpMulticastAddr_Type = IpAddress
_SlpMulticastAddr_Object = MibScalar
slpMulticastAddr = _SlpMulticastAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 4, 6),
    _SlpMulticastAddr_Type()
)
slpMulticastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slpMulticastAddr.setStatus("mandatory")
_TcpPortAssignmentCfg_ObjectIdentity = ObjectIdentity
tcpPortAssignmentCfg = _TcpPortAssignmentCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 5)
)
_TcpPortsRestoreDefault_Type = Integer32
_TcpPortsRestoreDefault_Object = MibScalar
tcpPortsRestoreDefault = _TcpPortsRestoreDefault_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 5, 1),
    _TcpPortsRestoreDefault_Type()
)
tcpPortsRestoreDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpPortsRestoreDefault.setStatus("mandatory")
_HttpPortAssignment_Type = Integer32
_HttpPortAssignment_Object = MibScalar
httpPortAssignment = _HttpPortAssignment_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 5, 2),
    _HttpPortAssignment_Type()
)
httpPortAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpPortAssignment.setStatus("mandatory")
_HttpsPortAssignment_Type = Integer32
_HttpsPortAssignment_Object = MibScalar
httpsPortAssignment = _HttpsPortAssignment_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 5, 3),
    _HttpsPortAssignment_Type()
)
httpsPortAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpsPortAssignment.setStatus("mandatory")
_TelnetPortAssignment_Type = Integer32
_TelnetPortAssignment_Object = MibScalar
telnetPortAssignment = _TelnetPortAssignment_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 5, 4),
    _TelnetPortAssignment_Type()
)
telnetPortAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetPortAssignment.setStatus("mandatory")
_SshPortAssignment_Type = Integer32
_SshPortAssignment_Object = MibScalar
sshPortAssignment = _SshPortAssignment_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 5, 5),
    _SshPortAssignment_Type()
)
sshPortAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshPortAssignment.setStatus("mandatory")
_SnmpAgentPortAssignment_Type = Integer32
_SnmpAgentPortAssignment_Object = MibScalar
snmpAgentPortAssignment = _SnmpAgentPortAssignment_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 5, 6),
    _SnmpAgentPortAssignment_Type()
)
snmpAgentPortAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAgentPortAssignment.setStatus("mandatory")
_SnmpTrapsPortAssignment_Type = Integer32
_SnmpTrapsPortAssignment_Object = MibScalar
snmpTrapsPortAssignment = _SnmpTrapsPortAssignment_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 5, 7),
    _SnmpTrapsPortAssignment_Type()
)
snmpTrapsPortAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapsPortAssignment.setStatus("mandatory")
_LdapClientCfg_ObjectIdentity = ObjectIdentity
ldapClientCfg = _LdapClientCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 6)
)


class _LdapServer1NameOrIPAddress_Type(OctetString):
    """Custom type ldapServer1NameOrIPAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LdapServer1NameOrIPAddress_Type.__name__ = "OctetString"
_LdapServer1NameOrIPAddress_Object = MibScalar
ldapServer1NameOrIPAddress = _LdapServer1NameOrIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 6, 1),
    _LdapServer1NameOrIPAddress_Type()
)
ldapServer1NameOrIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapServer1NameOrIPAddress.setStatus("mandatory")
_LdapServer1PortNumber_Type = Integer32
_LdapServer1PortNumber_Object = MibScalar
ldapServer1PortNumber = _LdapServer1PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 6, 2),
    _LdapServer1PortNumber_Type()
)
ldapServer1PortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapServer1PortNumber.setStatus("mandatory")


class _LdapServer2NameOrIPAddress_Type(OctetString):
    """Custom type ldapServer2NameOrIPAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LdapServer2NameOrIPAddress_Type.__name__ = "OctetString"
_LdapServer2NameOrIPAddress_Object = MibScalar
ldapServer2NameOrIPAddress = _LdapServer2NameOrIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 6, 3),
    _LdapServer2NameOrIPAddress_Type()
)
ldapServer2NameOrIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapServer2NameOrIPAddress.setStatus("mandatory")
_LdapServer2PortNumber_Type = Integer32
_LdapServer2PortNumber_Object = MibScalar
ldapServer2PortNumber = _LdapServer2PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 6, 4),
    _LdapServer2PortNumber_Type()
)
ldapServer2PortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapServer2PortNumber.setStatus("mandatory")


class _LdapServer3NameOrIPAddress_Type(OctetString):
    """Custom type ldapServer3NameOrIPAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LdapServer3NameOrIPAddress_Type.__name__ = "OctetString"
_LdapServer3NameOrIPAddress_Object = MibScalar
ldapServer3NameOrIPAddress = _LdapServer3NameOrIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 6, 5),
    _LdapServer3NameOrIPAddress_Type()
)
ldapServer3NameOrIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapServer3NameOrIPAddress.setStatus("mandatory")
_LdapServer3PortNumber_Type = Integer32
_LdapServer3PortNumber_Object = MibScalar
ldapServer3PortNumber = _LdapServer3PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 6, 6),
    _LdapServer3PortNumber_Type()
)
ldapServer3PortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapServer3PortNumber.setStatus("mandatory")


class _LdapRootDN_Type(OctetString):
    """Custom type ldapRootDN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LdapRootDN_Type.__name__ = "OctetString"
_LdapRootDN_Object = MibScalar
ldapRootDN = _LdapRootDN_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 6, 7),
    _LdapRootDN_Type()
)
ldapRootDN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapRootDN.setStatus("mandatory")


class _LdapUserSearchBaseDN_Type(OctetString):
    """Custom type ldapUserSearchBaseDN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LdapUserSearchBaseDN_Type.__name__ = "OctetString"
_LdapUserSearchBaseDN_Object = MibScalar
ldapUserSearchBaseDN = _LdapUserSearchBaseDN_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 6, 8),
    _LdapUserSearchBaseDN_Type()
)
ldapUserSearchBaseDN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapUserSearchBaseDN.setStatus("mandatory")


class _LdapGroupFilter_Type(OctetString):
    """Custom type ldapGroupFilter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LdapGroupFilter_Type.__name__ = "OctetString"
_LdapGroupFilter_Object = MibScalar
ldapGroupFilter = _LdapGroupFilter_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 6, 9),
    _LdapGroupFilter_Type()
)
ldapGroupFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapGroupFilter.setStatus("mandatory")


class _LdapBindingMethod_Type(Integer32):
    """Custom type ldapBindingMethod based on Integer32"""
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
        *(("anonymousAuthentication", 0),
          ("clientAuthentication", 1),
          ("strictUserPrincipalName", 3),
          ("userPrincipalName", 2))
    )


_LdapBindingMethod_Type.__name__ = "Integer32"
_LdapBindingMethod_Object = MibScalar
ldapBindingMethod = _LdapBindingMethod_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 6, 10),
    _LdapBindingMethod_Type()
)
ldapBindingMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapBindingMethod.setStatus("mandatory")


class _LdapClientAuthenticationDN_Type(OctetString):
    """Custom type ldapClientAuthenticationDN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LdapClientAuthenticationDN_Type.__name__ = "OctetString"
_LdapClientAuthenticationDN_Object = MibScalar
ldapClientAuthenticationDN = _LdapClientAuthenticationDN_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 6, 11),
    _LdapClientAuthenticationDN_Type()
)
ldapClientAuthenticationDN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapClientAuthenticationDN.setStatus("mandatory")


class _LdapClientAuthenticationPassword_Type(OctetString):
    """Custom type ldapClientAuthenticationPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_LdapClientAuthenticationPassword_Type.__name__ = "OctetString"
_LdapClientAuthenticationPassword_Object = MibScalar
ldapClientAuthenticationPassword = _LdapClientAuthenticationPassword_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 6, 12),
    _LdapClientAuthenticationPassword_Type()
)
ldapClientAuthenticationPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapClientAuthenticationPassword.setStatus("mandatory")


class _LdapUIDsearchAttribute_Type(OctetString):
    """Custom type ldapUIDsearchAttribute based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LdapUIDsearchAttribute_Type.__name__ = "OctetString"
_LdapUIDsearchAttribute_Object = MibScalar
ldapUIDsearchAttribute = _LdapUIDsearchAttribute_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 6, 13),
    _LdapUIDsearchAttribute_Type()
)
ldapUIDsearchAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapUIDsearchAttribute.setStatus("mandatory")


class _LdapGroupSearchAttribute_Type(OctetString):
    """Custom type ldapGroupSearchAttribute based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LdapGroupSearchAttribute_Type.__name__ = "OctetString"
_LdapGroupSearchAttribute_Object = MibScalar
ldapGroupSearchAttribute = _LdapGroupSearchAttribute_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 6, 14),
    _LdapGroupSearchAttribute_Type()
)
ldapGroupSearchAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapGroupSearchAttribute.setStatus("mandatory")


class _LdapLoginPermissionAttribute_Type(OctetString):
    """Custom type ldapLoginPermissionAttribute based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LdapLoginPermissionAttribute_Type.__name__ = "OctetString"
_LdapLoginPermissionAttribute_Object = MibScalar
ldapLoginPermissionAttribute = _LdapLoginPermissionAttribute_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 6, 15),
    _LdapLoginPermissionAttribute_Type()
)
ldapLoginPermissionAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapLoginPermissionAttribute.setStatus("mandatory")


class _LdapUseDNSOrPreConfiguredServers_Type(Integer32):
    """Custom type ldapUseDNSOrPreConfiguredServers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("useDNSToFindLDAPServers", 1),
          ("usePreConfiguredLDAPServers", 0))
    )


_LdapUseDNSOrPreConfiguredServers_Type.__name__ = "Integer32"
_LdapUseDNSOrPreConfiguredServers_Object = MibScalar
ldapUseDNSOrPreConfiguredServers = _LdapUseDNSOrPreConfiguredServers_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 6, 16),
    _LdapUseDNSOrPreConfiguredServers_Type()
)
ldapUseDNSOrPreConfiguredServers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapUseDNSOrPreConfiguredServers.setStatus("mandatory")


class _LdapDomainSource_Type(Integer32):
    """Custom type ldapDomainSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extractSearchDomainFromLoginID", 0),
          ("tryLoginFirstThenConfiguredValue", 2),
          ("useOnlyConfiguredSearchDomainBelow", 1))
    )


_LdapDomainSource_Type.__name__ = "Integer32"
_LdapDomainSource_Object = MibScalar
ldapDomainSource = _LdapDomainSource_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 6, 17),
    _LdapDomainSource_Type()
)
ldapDomainSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapDomainSource.setStatus("mandatory")


class _LdapSearchDomain_Type(OctetString):
    """Custom type ldapSearchDomain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LdapSearchDomain_Type.__name__ = "OctetString"
_LdapSearchDomain_Object = MibScalar
ldapSearchDomain = _LdapSearchDomain_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 6, 18),
    _LdapSearchDomain_Type()
)
ldapSearchDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapSearchDomain.setStatus("mandatory")


class _LdapServiceName_Type(OctetString):
    """Custom type ldapServiceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_LdapServiceName_Type.__name__ = "OctetString"
_LdapServiceName_Object = MibScalar
ldapServiceName = _LdapServiceName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 6, 19),
    _LdapServiceName_Type()
)
ldapServiceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapServiceName.setStatus("mandatory")
_UplinkCheckConfig_ObjectIdentity = ObjectIdentity
uplinkCheckConfig = _UplinkCheckConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 7)
)


class _UplinkCheckEnabled_Type(Integer32):
    """Custom type uplinkCheckEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("uplinkCheckDisabled", 0),
          ("uplinkCheckEnabled", 1))
    )


_UplinkCheckEnabled_Type.__name__ = "Integer32"
_UplinkCheckEnabled_Object = MibScalar
uplinkCheckEnabled = _UplinkCheckEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 7, 1),
    _UplinkCheckEnabled_Type()
)
uplinkCheckEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uplinkCheckEnabled.setStatus("mandatory")
_UplinkCheckDelay_Type = Integer32
_UplinkCheckDelay_Object = MibScalar
uplinkCheckDelay = _UplinkCheckDelay_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 9, 3, 7, 2),
    _UplinkCheckDelay_Type()
)
uplinkCheckDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uplinkCheckDelay.setStatus("mandatory")
_SolConfiguration_ObjectIdentity = ObjectIdentity
solConfiguration = _SolConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 10)
)
_SolGlobalConfig_ObjectIdentity = ObjectIdentity
solGlobalConfig = _SolGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 10, 1)
)


class _SolEnable_Type(Integer32):
    """Custom type solEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("solDiabled", 0),
          ("solEnabled", 1))
    )


_SolEnable_Type.__name__ = "Integer32"
_SolEnable_Object = MibScalar
solEnable = _SolEnable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 10, 1, 1),
    _SolEnable_Type()
)
solEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    solEnable.setStatus("mandatory")
_SolVlanId_Type = Integer32
_SolVlanId_Object = MibScalar
solVlanId = _SolVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 10, 1, 2),
    _SolVlanId_Type()
)
solVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    solVlanId.setStatus("mandatory")
_SolAccumulateTimeout_Type = Integer32
_SolAccumulateTimeout_Object = MibScalar
solAccumulateTimeout = _SolAccumulateTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 10, 1, 3),
    _SolAccumulateTimeout_Type()
)
solAccumulateTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    solAccumulateTimeout.setStatus("mandatory")
_SolCharSendThreshold_Type = Integer32
_SolCharSendThreshold_Object = MibScalar
solCharSendThreshold = _SolCharSendThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 10, 1, 4),
    _SolCharSendThreshold_Type()
)
solCharSendThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    solCharSendThreshold.setStatus("mandatory")
_SolRetry_Type = Integer32
_SolRetry_Object = MibScalar
solRetry = _SolRetry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 10, 1, 5),
    _SolRetry_Type()
)
solRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    solRetry.setStatus("mandatory")
_SolRetryInterval_Type = Integer32
_SolRetryInterval_Object = MibScalar
solRetryInterval = _SolRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 10, 1, 6),
    _SolRetryInterval_Type()
)
solRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    solRetryInterval.setStatus("mandatory")


class _SolExitToCliKeySeq_Type(OctetString):
    """Custom type solExitToCliKeySeq based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SolExitToCliKeySeq_Type.__name__ = "OctetString"
_SolExitToCliKeySeq_Object = MibScalar
solExitToCliKeySeq = _SolExitToCliKeySeq_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 10, 1, 7),
    _SolExitToCliKeySeq_Type()
)
solExitToCliKeySeq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    solExitToCliKeySeq.setStatus("mandatory")


class _SolResetBladeKeySeq_Type(OctetString):
    """Custom type solResetBladeKeySeq based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SolResetBladeKeySeq_Type.__name__ = "OctetString"
_SolResetBladeKeySeq_Object = MibScalar
solResetBladeKeySeq = _SolResetBladeKeySeq_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 10, 1, 8),
    _SolResetBladeKeySeq_Type()
)
solResetBladeKeySeq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    solResetBladeKeySeq.setStatus("mandatory")
_SolBladeConfig_ObjectIdentity = ObjectIdentity
solBladeConfig = _SolBladeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 10, 2)
)
_SolBladeTable_Object = MibTable
solBladeTable = _SolBladeTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 10, 2, 1)
)
if mibBuilder.loadTexts:
    solBladeTable.setStatus("mandatory")
_SolBladeEntry_Object = MibTableRow
solBladeEntry = _SolBladeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 10, 2, 1, 1)
)
solBladeEntry.setIndexNames(
    (0, "BLADE-MIB", "solBladeIndex"),
)
if mibBuilder.loadTexts:
    solBladeEntry.setStatus("mandatory")
_SolBladeIndex_Type = Integer32
_SolBladeIndex_Object = MibTableColumn
solBladeIndex = _SolBladeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 10, 2, 1, 1, 1),
    _SolBladeIndex_Type()
)
solBladeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solBladeIndex.setStatus("mandatory")
_SolBladeName_Type = OctetString
_SolBladeName_Object = MibTableColumn
solBladeName = _SolBladeName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 10, 2, 1, 1, 2),
    _SolBladeName_Type()
)
solBladeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solBladeName.setStatus("mandatory")


class _SolBladeEnable_Type(Integer32):
    """Custom type solBladeEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("solBladeDiabled", 0),
          ("solBladeEnabled", 1))
    )


_SolBladeEnable_Type.__name__ = "Integer32"
_SolBladeEnable_Object = MibTableColumn
solBladeEnable = _SolBladeEnable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 10, 2, 1, 1, 3),
    _SolBladeEnable_Type()
)
solBladeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    solBladeEnable.setStatus("mandatory")
_SolBladeIpAddr_Type = IpAddress
_SolBladeIpAddr_Object = MibTableColumn
solBladeIpAddr = _SolBladeIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 10, 2, 1, 1, 4),
    _SolBladeIpAddr_Type()
)
solBladeIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solBladeIpAddr.setStatus("mandatory")


class _SolBladeSessionStatus_Type(Integer32):
    """Custom type solBladeSessionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("solSessionActive", 2),
          ("solSessionNotReady", 0),
          ("solSessionReady", 1))
    )


_SolBladeSessionStatus_Type.__name__ = "Integer32"
_SolBladeSessionStatus_Object = MibTableColumn
solBladeSessionStatus = _SolBladeSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 10, 2, 1, 1, 5),
    _SolBladeSessionStatus_Type()
)
solBladeSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solBladeSessionStatus.setStatus("mandatory")


class _SolBladeCapability_Type(Integer32):
    """Custom type solBladeCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notSupport", 0),
          ("support", 1))
    )


_SolBladeCapability_Type.__name__ = "Integer32"
_SolBladeCapability_Object = MibTableColumn
solBladeCapability = _SolBladeCapability_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 4, 10, 2, 1, 1, 6),
    _SolBladeCapability_Type()
)
solBladeCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solBladeCapability.setStatus("mandatory")
_TelcoManagement_ObjectIdentity = ObjectIdentity
telcoManagement = _TelcoManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 5)
)
_TelcoAlarmReq_ObjectIdentity = ObjectIdentity
telcoAlarmReq = _TelcoAlarmReq_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 5, 1)
)
_TelcoAlarmSet_Type = OctetString
_TelcoAlarmSet_Object = MibScalar
telcoAlarmSet = _TelcoAlarmSet_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 5, 1, 1),
    _TelcoAlarmSet_Type()
)
telcoAlarmSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telcoAlarmSet.setStatus("mandatory")
_TelcoAlarmAck_Type = OctetString
_TelcoAlarmAck_Object = MibScalar
telcoAlarmAck = _TelcoAlarmAck_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 5, 1, 2),
    _TelcoAlarmAck_Type()
)
telcoAlarmAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telcoAlarmAck.setStatus("mandatory")
_TelcoAlarmClear_Type = OctetString
_TelcoAlarmClear_Object = MibScalar
telcoAlarmClear = _TelcoAlarmClear_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 5, 1, 3),
    _TelcoAlarmClear_Type()
)
telcoAlarmClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telcoAlarmClear.setStatus("mandatory")
_TelcoOEM_ObjectIdentity = ObjectIdentity
telcoOEM = _TelcoOEM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 5, 127)
)
_TelcoOEMs_Type = OctetString
_TelcoOEMs_Object = MibScalar
telcoOEMs = _TelcoOEMs_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 5, 127, 1),
    _TelcoOEMs_Type()
)
telcoOEMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telcoOEMs.setStatus("mandatory")
_RestartReset_ObjectIdentity = ObjectIdentity
restartReset = _RestartReset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 7)
)


class _RestartSPImmediately_Type(Integer32):
    """Custom type restartSPImmediately based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("execute", 1)
    )


_RestartSPImmediately_Type.__name__ = "Integer32"
_RestartSPImmediately_Object = MibScalar
restartSPImmediately = _RestartSPImmediately_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 7, 4),
    _RestartSPImmediately_Type()
)
restartSPImmediately.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartSPImmediately.setStatus("mandatory")


class _SwitchOverRedundantMM_Type(Integer32):
    """Custom type switchOverRedundantMM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("execute", 1)
    )


_SwitchOverRedundantMM_Type.__name__ = "Integer32"
_SwitchOverRedundantMM_Object = MibScalar
switchOverRedundantMM = _SwitchOverRedundantMM_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 7, 7),
    _SwitchOverRedundantMM_Type()
)
switchOverRedundantMM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchOverRedundantMM.setStatus("mandatory")


class _ResetSPConfigAndRestart_Type(Integer32):
    """Custom type resetSPConfigAndRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("execute", 1)
    )


_ResetSPConfigAndRestart_Type.__name__ = "Integer32"
_ResetSPConfigAndRestart_Object = MibScalar
resetSPConfigAndRestart = _ResetSPConfigAndRestart_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 7, 20),
    _ResetSPConfigAndRestart_Type()
)
resetSPConfigAndRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetSPConfigAndRestart.setStatus("mandatory")
_BladeCenter_ObjectIdentity = ObjectIdentity
bladeCenter = _BladeCenter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22)
)
_ProcessorBlade_ObjectIdentity = ObjectIdentity
processorBlade = _ProcessorBlade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1)
)


class _BladeMediaTrayBladeId_Type(Integer32):
    """Custom type bladeMediaTrayBladeId based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("blade1", 1),
          ("blade10", 10),
          ("blade11", 11),
          ("blade12", 12),
          ("blade13", 13),
          ("blade14", 14),
          ("blade2", 2),
          ("blade3", 3),
          ("blade4", 4),
          ("blade5", 5),
          ("blade6", 6),
          ("blade7", 7),
          ("blade8", 8),
          ("blade9", 9),
          ("managementModule", 0))
    )


_BladeMediaTrayBladeId_Type.__name__ = "Integer32"
_BladeMediaTrayBladeId_Object = MibScalar
bladeMediaTrayBladeId = _BladeMediaTrayBladeId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 1),
    _BladeMediaTrayBladeId_Type()
)
bladeMediaTrayBladeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bladeMediaTrayBladeId.setStatus("mandatory")


class _BladeKVMBladeId_Type(Integer32):
    """Custom type bladeKVMBladeId based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("blade1", 1),
          ("blade10", 10),
          ("blade11", 11),
          ("blade12", 12),
          ("blade13", 13),
          ("blade14", 14),
          ("blade2", 2),
          ("blade3", 3),
          ("blade4", 4),
          ("blade5", 5),
          ("blade6", 6),
          ("blade7", 7),
          ("blade8", 8),
          ("blade9", 9),
          ("managementModule", 0))
    )


_BladeKVMBladeId_Type.__name__ = "Integer32"
_BladeKVMBladeId_Object = MibScalar
bladeKVMBladeId = _BladeKVMBladeId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 2),
    _BladeKVMBladeId_Type()
)
bladeKVMBladeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bladeKVMBladeId.setStatus("mandatory")
_BladeBootSequenceTable_Object = MibTable
bladeBootSequenceTable = _BladeBootSequenceTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 3)
)
if mibBuilder.loadTexts:
    bladeBootSequenceTable.setStatus("mandatory")
_BladeBootSequenceEntry_Object = MibTableRow
bladeBootSequenceEntry = _BladeBootSequenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 3, 1)
)
bladeBootSequenceEntry.setIndexNames(
    (0, "BLADE-MIB", "bootSequenceIndex"),
)
if mibBuilder.loadTexts:
    bladeBootSequenceEntry.setStatus("mandatory")
_BootSequenceIndex_Type = Integer32
_BootSequenceIndex_Object = MibTableColumn
bootSequenceIndex = _BootSequenceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 3, 1, 1),
    _BootSequenceIndex_Type()
)
bootSequenceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootSequenceIndex.setStatus("mandatory")


class _BootSequenceBladeId_Type(Integer32):
    """Custom type bootSequenceBladeId based on Integer32"""
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
        *(("blade1", 1),
          ("blade10", 10),
          ("blade11", 11),
          ("blade12", 12),
          ("blade13", 13),
          ("blade14", 14),
          ("blade2", 2),
          ("blade3", 3),
          ("blade4", 4),
          ("blade5", 5),
          ("blade6", 6),
          ("blade7", 7),
          ("blade8", 8),
          ("blade9", 9))
    )


_BootSequenceBladeId_Type.__name__ = "Integer32"
_BootSequenceBladeId_Object = MibTableColumn
bootSequenceBladeId = _BootSequenceBladeId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 3, 1, 2),
    _BootSequenceBladeId_Type()
)
bootSequenceBladeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootSequenceBladeId.setStatus("mandatory")


class _BootSequenceBladeExists_Type(Integer32):
    """Custom type bootSequenceBladeExists based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_BootSequenceBladeExists_Type.__name__ = "Integer32"
_BootSequenceBladeExists_Object = MibTableColumn
bootSequenceBladeExists = _BootSequenceBladeExists_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 3, 1, 3),
    _BootSequenceBladeExists_Type()
)
bootSequenceBladeExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootSequenceBladeExists.setStatus("mandatory")


class _BootSequenceBladePowerState_Type(Integer32):
    """Custom type bootSequenceBladePowerState based on Integer32"""
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


_BootSequenceBladePowerState_Type.__name__ = "Integer32"
_BootSequenceBladePowerState_Object = MibTableColumn
bootSequenceBladePowerState = _BootSequenceBladePowerState_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 3, 1, 4),
    _BootSequenceBladePowerState_Type()
)
bootSequenceBladePowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootSequenceBladePowerState.setStatus("mandatory")


class _BootSequenceBladeHealthState_Type(Integer32):
    """Custom type bootSequenceBladeHealthState based on Integer32"""
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
        *(("bad", 3),
          ("good", 1),
          ("unknown", 0),
          ("warning", 2))
    )


_BootSequenceBladeHealthState_Type.__name__ = "Integer32"
_BootSequenceBladeHealthState_Object = MibTableColumn
bootSequenceBladeHealthState = _BootSequenceBladeHealthState_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 3, 1, 5),
    _BootSequenceBladeHealthState_Type()
)
bootSequenceBladeHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootSequenceBladeHealthState.setStatus("mandatory")
_BootSequenceBladeName_Type = OctetString
_BootSequenceBladeName_Object = MibTableColumn
bootSequenceBladeName = _BootSequenceBladeName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 3, 1, 6),
    _BootSequenceBladeName_Type()
)
bootSequenceBladeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootSequenceBladeName.setStatus("mandatory")


class _BootSequence1_Type(Integer32):
    """Custom type bootSequence1 based on Integer32"""
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
        *(("cdrom", 2),
          ("floppy", 1),
          ("hardDrive0", 3),
          ("hardDrive1", 4),
          ("hardDrive2", 5),
          ("hardDrive3", 6),
          ("networkBoot", 7),
          ("noneSpecified", 0),
          ("notAvailable", 8))
    )


_BootSequence1_Type.__name__ = "Integer32"
_BootSequence1_Object = MibTableColumn
bootSequence1 = _BootSequence1_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 3, 1, 7),
    _BootSequence1_Type()
)
bootSequence1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootSequence1.setStatus("mandatory")


class _BootSequence2_Type(Integer32):
    """Custom type bootSequence2 based on Integer32"""
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
        *(("cdrom", 2),
          ("floppy", 1),
          ("hardDrive0", 3),
          ("hardDrive1", 4),
          ("hardDrive2", 5),
          ("hardDrive3", 6),
          ("networkBoot", 7),
          ("noneSpecified", 0),
          ("notAvailable", 8))
    )


_BootSequence2_Type.__name__ = "Integer32"
_BootSequence2_Object = MibTableColumn
bootSequence2 = _BootSequence2_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 3, 1, 8),
    _BootSequence2_Type()
)
bootSequence2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootSequence2.setStatus("mandatory")


class _BootSequence3_Type(Integer32):
    """Custom type bootSequence3 based on Integer32"""
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
        *(("cdrom", 2),
          ("floppy", 1),
          ("hardDrive0", 3),
          ("hardDrive1", 4),
          ("hardDrive2", 5),
          ("hardDrive3", 6),
          ("networkBoot", 7),
          ("noneSpecified", 0),
          ("notAvailable", 8))
    )


_BootSequence3_Type.__name__ = "Integer32"
_BootSequence3_Object = MibTableColumn
bootSequence3 = _BootSequence3_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 3, 1, 9),
    _BootSequence3_Type()
)
bootSequence3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootSequence3.setStatus("mandatory")


class _BootSequence4_Type(Integer32):
    """Custom type bootSequence4 based on Integer32"""
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
        *(("cdrom", 2),
          ("floppy", 1),
          ("hardDrive0", 3),
          ("hardDrive1", 4),
          ("hardDrive2", 5),
          ("hardDrive3", 6),
          ("networkBoot", 7),
          ("noneSpecified", 0),
          ("notAvailable", 8))
    )


_BootSequence4_Type.__name__ = "Integer32"
_BootSequence4_Object = MibTableColumn
bootSequence4 = _BootSequence4_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 3, 1, 10),
    _BootSequence4_Type()
)
bootSequence4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootSequence4.setStatus("mandatory")
_BladeRemoteControl_ObjectIdentity = ObjectIdentity
bladeRemoteControl = _BladeRemoteControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 4)
)
_BladeRemoteControlTable_Object = MibTable
bladeRemoteControlTable = _BladeRemoteControlTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 4, 1)
)
if mibBuilder.loadTexts:
    bladeRemoteControlTable.setStatus("mandatory")
_BladeRemoteControlEntry_Object = MibTableRow
bladeRemoteControlEntry = _BladeRemoteControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 4, 1, 1)
)
bladeRemoteControlEntry.setIndexNames(
    (0, "BLADE-MIB", "remoteControlIndex"),
)
if mibBuilder.loadTexts:
    bladeRemoteControlEntry.setStatus("mandatory")
_RemoteControlIndex_Type = Integer32
_RemoteControlIndex_Object = MibTableColumn
remoteControlIndex = _RemoteControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 4, 1, 1, 1),
    _RemoteControlIndex_Type()
)
remoteControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteControlIndex.setStatus("mandatory")


class _RemoteControlBladeId_Type(Integer32):
    """Custom type remoteControlBladeId based on Integer32"""
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
        *(("blade1", 1),
          ("blade10", 10),
          ("blade11", 11),
          ("blade12", 12),
          ("blade13", 13),
          ("blade14", 14),
          ("blade2", 2),
          ("blade3", 3),
          ("blade4", 4),
          ("blade5", 5),
          ("blade6", 6),
          ("blade7", 7),
          ("blade8", 8),
          ("blade9", 9))
    )


_RemoteControlBladeId_Type.__name__ = "Integer32"
_RemoteControlBladeId_Object = MibTableColumn
remoteControlBladeId = _RemoteControlBladeId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 4, 1, 1, 2),
    _RemoteControlBladeId_Type()
)
remoteControlBladeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteControlBladeId.setStatus("mandatory")


class _RemoteControlBladeExists_Type(Integer32):
    """Custom type remoteControlBladeExists based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_RemoteControlBladeExists_Type.__name__ = "Integer32"
_RemoteControlBladeExists_Object = MibTableColumn
remoteControlBladeExists = _RemoteControlBladeExists_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 4, 1, 1, 3),
    _RemoteControlBladeExists_Type()
)
remoteControlBladeExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteControlBladeExists.setStatus("mandatory")


class _RemoteControlBladePowerState_Type(Integer32):
    """Custom type remoteControlBladePowerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("unknown", 255))
    )


_RemoteControlBladePowerState_Type.__name__ = "Integer32"
_RemoteControlBladePowerState_Object = MibTableColumn
remoteControlBladePowerState = _RemoteControlBladePowerState_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 4, 1, 1, 4),
    _RemoteControlBladePowerState_Type()
)
remoteControlBladePowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteControlBladePowerState.setStatus("mandatory")


class _RemoteControlBladeHealthState_Type(Integer32):
    """Custom type remoteControlBladeHealthState based on Integer32"""
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
        *(("bad", 3),
          ("good", 1),
          ("init", 5),
          ("kernel", 4),
          ("unknown", 0),
          ("warning", 2))
    )


_RemoteControlBladeHealthState_Type.__name__ = "Integer32"
_RemoteControlBladeHealthState_Object = MibTableColumn
remoteControlBladeHealthState = _RemoteControlBladeHealthState_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 4, 1, 1, 5),
    _RemoteControlBladeHealthState_Type()
)
remoteControlBladeHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteControlBladeHealthState.setStatus("mandatory")
_RemoteControlBladeName_Type = OctetString
_RemoteControlBladeName_Object = MibTableColumn
remoteControlBladeName = _RemoteControlBladeName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 4, 1, 1, 6),
    _RemoteControlBladeName_Type()
)
remoteControlBladeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteControlBladeName.setStatus("mandatory")


class _RemotePowerControlEnable_Type(Integer32):
    """Custom type remotePowerControlEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RemotePowerControlEnable_Type.__name__ = "Integer32"
_RemotePowerControlEnable_Object = MibTableColumn
remotePowerControlEnable = _RemotePowerControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 4, 1, 1, 7),
    _RemotePowerControlEnable_Type()
)
remotePowerControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remotePowerControlEnable.setStatus("mandatory")


class _RemoteMediaTrayControlEnable_Type(Integer32):
    """Custom type remoteMediaTrayControlEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RemoteMediaTrayControlEnable_Type.__name__ = "Integer32"
_RemoteMediaTrayControlEnable_Object = MibTableColumn
remoteMediaTrayControlEnable = _RemoteMediaTrayControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 4, 1, 1, 8),
    _RemoteMediaTrayControlEnable_Type()
)
remoteMediaTrayControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteMediaTrayControlEnable.setStatus("mandatory")


class _RemoteKVMControlEnable_Type(Integer32):
    """Custom type remoteKVMControlEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RemoteKVMControlEnable_Type.__name__ = "Integer32"
_RemoteKVMControlEnable_Object = MibTableColumn
remoteKVMControlEnable = _RemoteKVMControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 4, 1, 1, 9),
    _RemoteKVMControlEnable_Type()
)
remoteKVMControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteKVMControlEnable.setStatus("mandatory")


class _RemoteWakeOnLanControlEnable_Type(Integer32):
    """Custom type remoteWakeOnLanControlEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RemoteWakeOnLanControlEnable_Type.__name__ = "Integer32"
_RemoteWakeOnLanControlEnable_Object = MibTableColumn
remoteWakeOnLanControlEnable = _RemoteWakeOnLanControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 4, 1, 1, 10),
    _RemoteWakeOnLanControlEnable_Type()
)
remoteWakeOnLanControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteWakeOnLanControlEnable.setStatus("mandatory")
_BladePolicy_ObjectIdentity = ObjectIdentity
bladePolicy = _BladePolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 4, 2)
)


class _BladePolicyPowerControlEnable_Type(Integer32):
    """Custom type bladePolicyPowerControlEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_BladePolicyPowerControlEnable_Type.__name__ = "Integer32"
_BladePolicyPowerControlEnable_Object = MibScalar
bladePolicyPowerControlEnable = _BladePolicyPowerControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 4, 2, 1),
    _BladePolicyPowerControlEnable_Type()
)
bladePolicyPowerControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bladePolicyPowerControlEnable.setStatus("mandatory")


class _BladePolicyMediaTrayControlEnable_Type(Integer32):
    """Custom type bladePolicyMediaTrayControlEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_BladePolicyMediaTrayControlEnable_Type.__name__ = "Integer32"
_BladePolicyMediaTrayControlEnable_Object = MibScalar
bladePolicyMediaTrayControlEnable = _BladePolicyMediaTrayControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 4, 2, 2),
    _BladePolicyMediaTrayControlEnable_Type()
)
bladePolicyMediaTrayControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bladePolicyMediaTrayControlEnable.setStatus("mandatory")


class _BladePolicyKVMControlEnable_Type(Integer32):
    """Custom type bladePolicyKVMControlEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_BladePolicyKVMControlEnable_Type.__name__ = "Integer32"
_BladePolicyKVMControlEnable_Object = MibScalar
bladePolicyKVMControlEnable = _BladePolicyKVMControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 4, 2, 3),
    _BladePolicyKVMControlEnable_Type()
)
bladePolicyKVMControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bladePolicyKVMControlEnable.setStatus("mandatory")


class _BladePolicyWakeOnLanControlEnable_Type(Integer32):
    """Custom type bladePolicyWakeOnLanControlEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_BladePolicyWakeOnLanControlEnable_Type.__name__ = "Integer32"
_BladePolicyWakeOnLanControlEnable_Object = MibScalar
bladePolicyWakeOnLanControlEnable = _BladePolicyWakeOnLanControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 4, 2, 4),
    _BladePolicyWakeOnLanControlEnable_Type()
)
bladePolicyWakeOnLanControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bladePolicyWakeOnLanControlEnable.setStatus("mandatory")
_BladeMonitors_ObjectIdentity = ObjectIdentity
bladeMonitors = _BladeMonitors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5)
)
_BladeSystemStatusTable_Object = MibTable
bladeSystemStatusTable = _BladeSystemStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 1)
)
if mibBuilder.loadTexts:
    bladeSystemStatusTable.setStatus("mandatory")
_BladeSystemStatusEntry_Object = MibTableRow
bladeSystemStatusEntry = _BladeSystemStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 1, 1)
)
bladeSystemStatusEntry.setIndexNames(
    (0, "BLADE-MIB", "bladeStatusIndex"),
)
if mibBuilder.loadTexts:
    bladeSystemStatusEntry.setStatus("mandatory")
_BladeStatusIndex_Type = Integer32
_BladeStatusIndex_Object = MibTableColumn
bladeStatusIndex = _BladeStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 1, 1, 1),
    _BladeStatusIndex_Type()
)
bladeStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeStatusIndex.setStatus("mandatory")


class _BladeId_Type(Integer32):
    """Custom type bladeId based on Integer32"""
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
        *(("blade1", 1),
          ("blade10", 10),
          ("blade11", 11),
          ("blade12", 12),
          ("blade13", 13),
          ("blade14", 14),
          ("blade2", 2),
          ("blade3", 3),
          ("blade4", 4),
          ("blade5", 5),
          ("blade6", 6),
          ("blade7", 7),
          ("blade8", 8),
          ("blade9", 9))
    )


_BladeId_Type.__name__ = "Integer32"
_BladeId_Object = MibTableColumn
bladeId = _BladeId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 1, 1, 2),
    _BladeId_Type()
)
bladeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeId.setStatus("mandatory")


class _BladeExists_Type(Integer32):
    """Custom type bladeExists based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_BladeExists_Type.__name__ = "Integer32"
_BladeExists_Object = MibTableColumn
bladeExists = _BladeExists_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 1, 1, 3),
    _BladeExists_Type()
)
bladeExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeExists.setStatus("mandatory")


class _BladePowerState_Type(Integer32):
    """Custom type bladePowerState based on Integer32"""
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


_BladePowerState_Type.__name__ = "Integer32"
_BladePowerState_Object = MibTableColumn
bladePowerState = _BladePowerState_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 1, 1, 4),
    _BladePowerState_Type()
)
bladePowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladePowerState.setStatus("mandatory")


class _BladeHealthState_Type(Integer32):
    """Custom type bladeHealthState based on Integer32"""
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
        *(("bad", 3),
          ("good", 1),
          ("unknown", 0),
          ("warning", 2))
    )


_BladeHealthState_Type.__name__ = "Integer32"
_BladeHealthState_Object = MibTableColumn
bladeHealthState = _BladeHealthState_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 1, 1, 5),
    _BladeHealthState_Type()
)
bladeHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeHealthState.setStatus("mandatory")
_BladeName_Type = OctetString
_BladeName_Object = MibTableColumn
bladeName = _BladeName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 1, 1, 6),
    _BladeName_Type()
)
bladeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeName.setStatus("mandatory")


class _BladeRemotePowerEnable_Type(Integer32):
    """Custom type bladeRemotePowerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_BladeRemotePowerEnable_Type.__name__ = "Integer32"
_BladeRemotePowerEnable_Object = MibTableColumn
bladeRemotePowerEnable = _BladeRemotePowerEnable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 1, 1, 7),
    _BladeRemotePowerEnable_Type()
)
bladeRemotePowerEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeRemotePowerEnable.setStatus("mandatory")


class _BladeRemoteMediaTrayEnable_Type(Integer32):
    """Custom type bladeRemoteMediaTrayEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_BladeRemoteMediaTrayEnable_Type.__name__ = "Integer32"
_BladeRemoteMediaTrayEnable_Object = MibTableColumn
bladeRemoteMediaTrayEnable = _BladeRemoteMediaTrayEnable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 1, 1, 8),
    _BladeRemoteMediaTrayEnable_Type()
)
bladeRemoteMediaTrayEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeRemoteMediaTrayEnable.setStatus("mandatory")


class _BladeRemoteKVMEnable_Type(Integer32):
    """Custom type bladeRemoteKVMEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_BladeRemoteKVMEnable_Type.__name__ = "Integer32"
_BladeRemoteKVMEnable_Object = MibTableColumn
bladeRemoteKVMEnable = _BladeRemoteKVMEnable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 1, 1, 9),
    _BladeRemoteKVMEnable_Type()
)
bladeRemoteKVMEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeRemoteKVMEnable.setStatus("mandatory")


class _BladeConnectionType_Type(Integer32):
    """Custom type bladeConnectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("fiber", 2),
          ("none", 0))
    )


_BladeConnectionType_Type.__name__ = "Integer32"
_BladeConnectionType_Object = MibTableColumn
bladeConnectionType = _BladeConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 1, 1, 10),
    _BladeConnectionType_Type()
)
bladeConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeConnectionType.setStatus("mandatory")


class _BladeOwnsKVM_Type(Integer32):
    """Custom type bladeOwnsKVM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_BladeOwnsKVM_Type.__name__ = "Integer32"
_BladeOwnsKVM_Object = MibTableColumn
bladeOwnsKVM = _BladeOwnsKVM_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 1, 1, 11),
    _BladeOwnsKVM_Type()
)
bladeOwnsKVM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeOwnsKVM.setStatus("mandatory")


class _BladeOwnsMediaTray_Type(Integer32):
    """Custom type bladeOwnsMediaTray based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_BladeOwnsMediaTray_Type.__name__ = "Integer32"
_BladeOwnsMediaTray_Object = MibTableColumn
bladeOwnsMediaTray = _BladeOwnsMediaTray_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 1, 1, 12),
    _BladeOwnsMediaTray_Type()
)
bladeOwnsMediaTray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeOwnsMediaTray.setStatus("mandatory")


class _BladeRemoteWakeOnLanEnable_Type(Integer32):
    """Custom type bladeRemoteWakeOnLanEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_BladeRemoteWakeOnLanEnable_Type.__name__ = "Integer32"
_BladeRemoteWakeOnLanEnable_Object = MibTableColumn
bladeRemoteWakeOnLanEnable = _BladeRemoteWakeOnLanEnable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 1, 1, 13),
    _BladeRemoteWakeOnLanEnable_Type()
)
bladeRemoteWakeOnLanEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeRemoteWakeOnLanEnable.setStatus("mandatory")


class _BladeServerExpansion_Type(Integer32):
    """Custom type bladeServerExpansion based on Integer32"""
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


_BladeServerExpansion_Type.__name__ = "Integer32"
_BladeServerExpansion_Object = MibTableColumn
bladeServerExpansion = _BladeServerExpansion_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 1, 1, 14),
    _BladeServerExpansion_Type()
)
bladeServerExpansion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeServerExpansion.setStatus("mandatory")
_BladeWidth_Type = Integer32
_BladeWidth_Object = MibTableColumn
bladeWidth = _BladeWidth_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 1, 1, 15),
    _BladeWidth_Type()
)
bladeWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeWidth.setStatus("mandatory")


class _BladeSupportCapacityOnDemand_Type(Integer32):
    """Custom type bladeSupportCapacityOnDemand based on Integer32"""
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


_BladeSupportCapacityOnDemand_Type.__name__ = "Integer32"
_BladeSupportCapacityOnDemand_Object = MibTableColumn
bladeSupportCapacityOnDemand = _BladeSupportCapacityOnDemand_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 1, 1, 16),
    _BladeSupportCapacityOnDemand_Type()
)
bladeSupportCapacityOnDemand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSupportCapacityOnDemand.setStatus("mandatory")
_BladeHealthSummaryTable_Object = MibTable
bladeHealthSummaryTable = _BladeHealthSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 2)
)
if mibBuilder.loadTexts:
    bladeHealthSummaryTable.setStatus("mandatory")
_BladeHealthSummaryEntry_Object = MibTableRow
bladeHealthSummaryEntry = _BladeHealthSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 2, 1)
)
bladeHealthSummaryEntry.setIndexNames(
    (0, "BLADE-MIB", "bladeHealthSummaryIndex"),
)
if mibBuilder.loadTexts:
    bladeHealthSummaryEntry.setStatus("mandatory")
_BladeHealthSummaryIndex_Type = Integer32
_BladeHealthSummaryIndex_Object = MibTableColumn
bladeHealthSummaryIndex = _BladeHealthSummaryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 2, 1, 1),
    _BladeHealthSummaryIndex_Type()
)
bladeHealthSummaryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeHealthSummaryIndex.setStatus("mandatory")


class _BladeHealthSummaryBladeId_Type(Integer32):
    """Custom type bladeHealthSummaryBladeId based on Integer32"""
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
        *(("blade1", 1),
          ("blade10", 10),
          ("blade11", 11),
          ("blade12", 12),
          ("blade13", 13),
          ("blade14", 14),
          ("blade2", 2),
          ("blade3", 3),
          ("blade4", 4),
          ("blade5", 5),
          ("blade6", 6),
          ("blade7", 7),
          ("blade8", 8),
          ("blade9", 9))
    )


_BladeHealthSummaryBladeId_Type.__name__ = "Integer32"
_BladeHealthSummaryBladeId_Object = MibTableColumn
bladeHealthSummaryBladeId = _BladeHealthSummaryBladeId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 2, 1, 2),
    _BladeHealthSummaryBladeId_Type()
)
bladeHealthSummaryBladeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeHealthSummaryBladeId.setStatus("mandatory")
_BladeHealthSummarySeverity_Type = OctetString
_BladeHealthSummarySeverity_Object = MibTableColumn
bladeHealthSummarySeverity = _BladeHealthSummarySeverity_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 2, 1, 3),
    _BladeHealthSummarySeverity_Type()
)
bladeHealthSummarySeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeHealthSummarySeverity.setStatus("mandatory")
_BladeHealthSummaryDescription_Type = OctetString
_BladeHealthSummaryDescription_Object = MibTableColumn
bladeHealthSummaryDescription = _BladeHealthSummaryDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 2, 1, 4),
    _BladeHealthSummaryDescription_Type()
)
bladeHealthSummaryDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeHealthSummaryDescription.setStatus("mandatory")
_BladeTemperaturesTable_Object = MibTable
bladeTemperaturesTable = _BladeTemperaturesTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 3)
)
if mibBuilder.loadTexts:
    bladeTemperaturesTable.setStatus("mandatory")
_BladeTemperaturesEntry_Object = MibTableRow
bladeTemperaturesEntry = _BladeTemperaturesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 3, 1)
)
bladeTemperaturesEntry.setIndexNames(
    (0, "BLADE-MIB", "temperatureIndex"),
)
if mibBuilder.loadTexts:
    bladeTemperaturesEntry.setStatus("mandatory")
_TemperatureIndex_Type = Integer32
_TemperatureIndex_Object = MibTableColumn
temperatureIndex = _TemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 3, 1, 1),
    _TemperatureIndex_Type()
)
temperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureIndex.setStatus("mandatory")


class _TemperatureBladeId_Type(Integer32):
    """Custom type temperatureBladeId based on Integer32"""
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
        *(("blade1", 1),
          ("blade10", 10),
          ("blade11", 11),
          ("blade12", 12),
          ("blade13", 13),
          ("blade14", 14),
          ("blade2", 2),
          ("blade3", 3),
          ("blade4", 4),
          ("blade5", 5),
          ("blade6", 6),
          ("blade7", 7),
          ("blade8", 8),
          ("blade9", 9))
    )


_TemperatureBladeId_Type.__name__ = "Integer32"
_TemperatureBladeId_Object = MibTableColumn
temperatureBladeId = _TemperatureBladeId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 3, 1, 2),
    _TemperatureBladeId_Type()
)
temperatureBladeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureBladeId.setStatus("mandatory")


class _TemperatureBladeExists_Type(Integer32):
    """Custom type temperatureBladeExists based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_TemperatureBladeExists_Type.__name__ = "Integer32"
_TemperatureBladeExists_Object = MibTableColumn
temperatureBladeExists = _TemperatureBladeExists_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 3, 1, 3),
    _TemperatureBladeExists_Type()
)
temperatureBladeExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureBladeExists.setStatus("mandatory")


class _TemperatureBladePowerState_Type(Integer32):
    """Custom type temperatureBladePowerState based on Integer32"""
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


_TemperatureBladePowerState_Type.__name__ = "Integer32"
_TemperatureBladePowerState_Object = MibTableColumn
temperatureBladePowerState = _TemperatureBladePowerState_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 3, 1, 4),
    _TemperatureBladePowerState_Type()
)
temperatureBladePowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureBladePowerState.setStatus("mandatory")
_TemperatureBladeName_Type = OctetString
_TemperatureBladeName_Object = MibTableColumn
temperatureBladeName = _TemperatureBladeName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 3, 1, 5),
    _TemperatureBladeName_Type()
)
temperatureBladeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureBladeName.setStatus("mandatory")
_TemperatureCPU1_Type = OctetString
_TemperatureCPU1_Object = MibTableColumn
temperatureCPU1 = _TemperatureCPU1_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 3, 1, 6),
    _TemperatureCPU1_Type()
)
temperatureCPU1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureCPU1.setStatus("mandatory")
_TemperatureCPU2_Type = OctetString
_TemperatureCPU2_Object = MibTableColumn
temperatureCPU2 = _TemperatureCPU2_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 3, 1, 7),
    _TemperatureCPU2_Type()
)
temperatureCPU2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureCPU2.setStatus("mandatory")
_TemperatureCPU3_Type = OctetString
_TemperatureCPU3_Object = MibTableColumn
temperatureCPU3 = _TemperatureCPU3_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 3, 1, 8),
    _TemperatureCPU3_Type()
)
temperatureCPU3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureCPU3.setStatus("mandatory")
_TemperatureCPU4_Type = OctetString
_TemperatureCPU4_Object = MibTableColumn
temperatureCPU4 = _TemperatureCPU4_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 3, 1, 9),
    _TemperatureCPU4_Type()
)
temperatureCPU4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureCPU4.setStatus("mandatory")
_TemperatureDASD1_Type = OctetString
_TemperatureDASD1_Object = MibTableColumn
temperatureDASD1 = _TemperatureDASD1_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 3, 1, 10),
    _TemperatureDASD1_Type()
)
temperatureDASD1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureDASD1.setStatus("mandatory")


class _BladeSensorTempCapability_Type(Integer32):
    """Custom type bladeSensorTempCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_BladeSensorTempCapability_Type.__name__ = "Integer32"
_BladeSensorTempCapability_Object = MibTableColumn
bladeSensorTempCapability = _BladeSensorTempCapability_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 3, 1, 11),
    _BladeSensorTempCapability_Type()
)
bladeSensorTempCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensorTempCapability.setStatus("mandatory")
_BladeSensor1Temp_Type = OctetString
_BladeSensor1Temp_Object = MibTableColumn
bladeSensor1Temp = _BladeSensor1Temp_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 3, 1, 12),
    _BladeSensor1Temp_Type()
)
bladeSensor1Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor1Temp.setStatus("mandatory")
_BladeSensor2Temp_Type = OctetString
_BladeSensor2Temp_Object = MibTableColumn
bladeSensor2Temp = _BladeSensor2Temp_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 3, 1, 13),
    _BladeSensor2Temp_Type()
)
bladeSensor2Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor2Temp.setStatus("mandatory")
_BladeSensor3Temp_Type = OctetString
_BladeSensor3Temp_Object = MibTableColumn
bladeSensor3Temp = _BladeSensor3Temp_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 3, 1, 14),
    _BladeSensor3Temp_Type()
)
bladeSensor3Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor3Temp.setStatus("mandatory")
_BladeSensor4Temp_Type = OctetString
_BladeSensor4Temp_Object = MibTableColumn
bladeSensor4Temp = _BladeSensor4Temp_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 3, 1, 15),
    _BladeSensor4Temp_Type()
)
bladeSensor4Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor4Temp.setStatus("mandatory")
_BladeSensor5Temp_Type = OctetString
_BladeSensor5Temp_Object = MibTableColumn
bladeSensor5Temp = _BladeSensor5Temp_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 3, 1, 16),
    _BladeSensor5Temp_Type()
)
bladeSensor5Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor5Temp.setStatus("mandatory")
_BladeSensor6Temp_Type = OctetString
_BladeSensor6Temp_Object = MibTableColumn
bladeSensor6Temp = _BladeSensor6Temp_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 3, 1, 17),
    _BladeSensor6Temp_Type()
)
bladeSensor6Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor6Temp.setStatus("mandatory")
_BladeTemperatureThresholdsTable_Object = MibTable
bladeTemperatureThresholdsTable = _BladeTemperatureThresholdsTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 4)
)
if mibBuilder.loadTexts:
    bladeTemperatureThresholdsTable.setStatus("mandatory")
_BladeTemperatureThresholdsEntry_Object = MibTableRow
bladeTemperatureThresholdsEntry = _BladeTemperatureThresholdsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 4, 1)
)
bladeTemperatureThresholdsEntry.setIndexNames(
    (0, "BLADE-MIB", "temperatureThresholdIndex"),
)
if mibBuilder.loadTexts:
    bladeTemperatureThresholdsEntry.setStatus("mandatory")
_TemperatureThresholdIndex_Type = Integer32
_TemperatureThresholdIndex_Object = MibTableColumn
temperatureThresholdIndex = _TemperatureThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 4, 1, 1),
    _TemperatureThresholdIndex_Type()
)
temperatureThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureThresholdIndex.setStatus("mandatory")


class _TemperatureThresholdBladeId_Type(Integer32):
    """Custom type temperatureThresholdBladeId based on Integer32"""
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
        *(("blade1", 1),
          ("blade10", 10),
          ("blade11", 11),
          ("blade12", 12),
          ("blade13", 13),
          ("blade14", 14),
          ("blade2", 2),
          ("blade3", 3),
          ("blade4", 4),
          ("blade5", 5),
          ("blade6", 6),
          ("blade7", 7),
          ("blade8", 8),
          ("blade9", 9))
    )


_TemperatureThresholdBladeId_Type.__name__ = "Integer32"
_TemperatureThresholdBladeId_Object = MibTableColumn
temperatureThresholdBladeId = _TemperatureThresholdBladeId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 4, 1, 2),
    _TemperatureThresholdBladeId_Type()
)
temperatureThresholdBladeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureThresholdBladeId.setStatus("mandatory")


class _TemperatureThresholdBladeExists_Type(Integer32):
    """Custom type temperatureThresholdBladeExists based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_TemperatureThresholdBladeExists_Type.__name__ = "Integer32"
_TemperatureThresholdBladeExists_Object = MibTableColumn
temperatureThresholdBladeExists = _TemperatureThresholdBladeExists_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 4, 1, 3),
    _TemperatureThresholdBladeExists_Type()
)
temperatureThresholdBladeExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureThresholdBladeExists.setStatus("mandatory")


class _TemperatureThresholdBladePowerState_Type(Integer32):
    """Custom type temperatureThresholdBladePowerState based on Integer32"""
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


_TemperatureThresholdBladePowerState_Type.__name__ = "Integer32"
_TemperatureThresholdBladePowerState_Object = MibTableColumn
temperatureThresholdBladePowerState = _TemperatureThresholdBladePowerState_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 4, 1, 4),
    _TemperatureThresholdBladePowerState_Type()
)
temperatureThresholdBladePowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureThresholdBladePowerState.setStatus("mandatory")
_TemperatureThresholdBladeName_Type = OctetString
_TemperatureThresholdBladeName_Object = MibTableColumn
temperatureThresholdBladeName = _TemperatureThresholdBladeName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 4, 1, 5),
    _TemperatureThresholdBladeName_Type()
)
temperatureThresholdBladeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureThresholdBladeName.setStatus("mandatory")
_TemperatureCPU1HardShutdown_Type = OctetString
_TemperatureCPU1HardShutdown_Object = MibTableColumn
temperatureCPU1HardShutdown = _TemperatureCPU1HardShutdown_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 4, 1, 6),
    _TemperatureCPU1HardShutdown_Type()
)
temperatureCPU1HardShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureCPU1HardShutdown.setStatus("mandatory")
_TemperatureCPU1Warning_Type = OctetString
_TemperatureCPU1Warning_Object = MibTableColumn
temperatureCPU1Warning = _TemperatureCPU1Warning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 4, 1, 7),
    _TemperatureCPU1Warning_Type()
)
temperatureCPU1Warning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureCPU1Warning.setStatus("mandatory")
_TemperatureCPU1WarningReset_Type = OctetString
_TemperatureCPU1WarningReset_Object = MibTableColumn
temperatureCPU1WarningReset = _TemperatureCPU1WarningReset_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 4, 1, 8),
    _TemperatureCPU1WarningReset_Type()
)
temperatureCPU1WarningReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureCPU1WarningReset.setStatus("mandatory")
_TemperatureCPU2HardShutdown_Type = OctetString
_TemperatureCPU2HardShutdown_Object = MibTableColumn
temperatureCPU2HardShutdown = _TemperatureCPU2HardShutdown_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 4, 1, 9),
    _TemperatureCPU2HardShutdown_Type()
)
temperatureCPU2HardShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureCPU2HardShutdown.setStatus("mandatory")
_TemperatureCPU2Warning_Type = OctetString
_TemperatureCPU2Warning_Object = MibTableColumn
temperatureCPU2Warning = _TemperatureCPU2Warning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 4, 1, 10),
    _TemperatureCPU2Warning_Type()
)
temperatureCPU2Warning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureCPU2Warning.setStatus("mandatory")
_TemperatureCPU2WarningReset_Type = OctetString
_TemperatureCPU2WarningReset_Object = MibTableColumn
temperatureCPU2WarningReset = _TemperatureCPU2WarningReset_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 4, 1, 11),
    _TemperatureCPU2WarningReset_Type()
)
temperatureCPU2WarningReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureCPU2WarningReset.setStatus("mandatory")
_TemperatureCPU3HardShutdown_Type = OctetString
_TemperatureCPU3HardShutdown_Object = MibTableColumn
temperatureCPU3HardShutdown = _TemperatureCPU3HardShutdown_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 4, 1, 12),
    _TemperatureCPU3HardShutdown_Type()
)
temperatureCPU3HardShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureCPU3HardShutdown.setStatus("mandatory")
_TemperatureCPU3Warning_Type = OctetString
_TemperatureCPU3Warning_Object = MibTableColumn
temperatureCPU3Warning = _TemperatureCPU3Warning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 4, 1, 13),
    _TemperatureCPU3Warning_Type()
)
temperatureCPU3Warning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureCPU3Warning.setStatus("mandatory")
_TemperatureCPU3WarningReset_Type = OctetString
_TemperatureCPU3WarningReset_Object = MibTableColumn
temperatureCPU3WarningReset = _TemperatureCPU3WarningReset_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 4, 1, 14),
    _TemperatureCPU3WarningReset_Type()
)
temperatureCPU3WarningReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureCPU3WarningReset.setStatus("mandatory")
_TemperatureCPU4HardShutdown_Type = OctetString
_TemperatureCPU4HardShutdown_Object = MibTableColumn
temperatureCPU4HardShutdown = _TemperatureCPU4HardShutdown_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 4, 1, 15),
    _TemperatureCPU4HardShutdown_Type()
)
temperatureCPU4HardShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureCPU4HardShutdown.setStatus("mandatory")
_TemperatureCPU4Warning_Type = OctetString
_TemperatureCPU4Warning_Object = MibTableColumn
temperatureCPU4Warning = _TemperatureCPU4Warning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 4, 1, 16),
    _TemperatureCPU4Warning_Type()
)
temperatureCPU4Warning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureCPU4Warning.setStatus("mandatory")
_TemperatureCPU4WarningReset_Type = OctetString
_TemperatureCPU4WarningReset_Object = MibTableColumn
temperatureCPU4WarningReset = _TemperatureCPU4WarningReset_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 4, 1, 17),
    _TemperatureCPU4WarningReset_Type()
)
temperatureCPU4WarningReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureCPU4WarningReset.setStatus("mandatory")
_TemperatureDASD1HardShutdown_Type = OctetString
_TemperatureDASD1HardShutdown_Object = MibTableColumn
temperatureDASD1HardShutdown = _TemperatureDASD1HardShutdown_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 4, 1, 18),
    _TemperatureDASD1HardShutdown_Type()
)
temperatureDASD1HardShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureDASD1HardShutdown.setStatus("mandatory")
_TemperatureDASD1Warning_Type = OctetString
_TemperatureDASD1Warning_Object = MibTableColumn
temperatureDASD1Warning = _TemperatureDASD1Warning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 4, 1, 19),
    _TemperatureDASD1Warning_Type()
)
temperatureDASD1Warning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureDASD1Warning.setStatus("mandatory")
_TemperatureDASD1WarningReset_Type = OctetString
_TemperatureDASD1WarningReset_Object = MibTableColumn
temperatureDASD1WarningReset = _TemperatureDASD1WarningReset_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 4, 1, 20),
    _TemperatureDASD1WarningReset_Type()
)
temperatureDASD1WarningReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureDASD1WarningReset.setStatus("mandatory")


class _BladeTempThresholdSensorCapability_Type(Integer32):
    """Custom type bladeTempThresholdSensorCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_BladeTempThresholdSensorCapability_Type.__name__ = "Integer32"
_BladeTempThresholdSensorCapability_Object = MibTableColumn
bladeTempThresholdSensorCapability = _BladeTempThresholdSensorCapability_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 4, 1, 21),
    _BladeTempThresholdSensorCapability_Type()
)
bladeTempThresholdSensorCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeTempThresholdSensorCapability.setStatus("mandatory")
_TemperatureSensor1HardShutdown_Type = OctetString
_TemperatureSensor1HardShutdown_Object = MibTableColumn
temperatureSensor1HardShutdown = _TemperatureSensor1HardShutdown_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 4, 1, 22),
    _TemperatureSensor1HardShutdown_Type()
)
temperatureSensor1HardShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensor1HardShutdown.setStatus("mandatory")
_TemperatureSensor1Warning_Type = OctetString
_TemperatureSensor1Warning_Object = MibTableColumn
temperatureSensor1Warning = _TemperatureSensor1Warning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 4, 1, 23),
    _TemperatureSensor1Warning_Type()
)
temperatureSensor1Warning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensor1Warning.setStatus("mandatory")
_TemperatureSensor1WarningReset_Type = OctetString
_TemperatureSensor1WarningReset_Object = MibTableColumn
temperatureSensor1WarningReset = _TemperatureSensor1WarningReset_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 4, 1, 24),
    _TemperatureSensor1WarningReset_Type()
)
temperatureSensor1WarningReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensor1WarningReset.setStatus("mandatory")
_TemperatureSensor2HardShutdown_Type = OctetString
_TemperatureSensor2HardShutdown_Object = MibTableColumn
temperatureSensor2HardShutdown = _TemperatureSensor2HardShutdown_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 4, 1, 25),
    _TemperatureSensor2HardShutdown_Type()
)
temperatureSensor2HardShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensor2HardShutdown.setStatus("mandatory")
_TemperatureSensor2Warning_Type = OctetString
_TemperatureSensor2Warning_Object = MibTableColumn
temperatureSensor2Warning = _TemperatureSensor2Warning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 4, 1, 26),
    _TemperatureSensor2Warning_Type()
)
temperatureSensor2Warning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensor2Warning.setStatus("mandatory")
_TemperatureSensor2WarningReset_Type = OctetString
_TemperatureSensor2WarningReset_Object = MibTableColumn
temperatureSensor2WarningReset = _TemperatureSensor2WarningReset_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 4, 1, 27),
    _TemperatureSensor2WarningReset_Type()
)
temperatureSensor2WarningReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensor2WarningReset.setStatus("mandatory")
_TemperatureSensor3HardShutdown_Type = OctetString
_TemperatureSensor3HardShutdown_Object = MibTableColumn
temperatureSensor3HardShutdown = _TemperatureSensor3HardShutdown_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 4, 1, 28),
    _TemperatureSensor3HardShutdown_Type()
)
temperatureSensor3HardShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensor3HardShutdown.setStatus("mandatory")
_TemperatureSensor3Warning_Type = OctetString
_TemperatureSensor3Warning_Object = MibTableColumn
temperatureSensor3Warning = _TemperatureSensor3Warning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 4, 1, 29),
    _TemperatureSensor3Warning_Type()
)
temperatureSensor3Warning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensor3Warning.setStatus("mandatory")
_TemperatureSensor3WarningReset_Type = OctetString
_TemperatureSensor3WarningReset_Object = MibTableColumn
temperatureSensor3WarningReset = _TemperatureSensor3WarningReset_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 4, 1, 30),
    _TemperatureSensor3WarningReset_Type()
)
temperatureSensor3WarningReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensor3WarningReset.setStatus("mandatory")
_TemperatureSensor4HardShutdown_Type = OctetString
_TemperatureSensor4HardShutdown_Object = MibTableColumn
temperatureSensor4HardShutdown = _TemperatureSensor4HardShutdown_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 4, 1, 31),
    _TemperatureSensor4HardShutdown_Type()
)
temperatureSensor4HardShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensor4HardShutdown.setStatus("mandatory")
_TemperatureSensor4Warning_Type = OctetString
_TemperatureSensor4Warning_Object = MibTableColumn
temperatureSensor4Warning = _TemperatureSensor4Warning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 4, 1, 32),
    _TemperatureSensor4Warning_Type()
)
temperatureSensor4Warning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensor4Warning.setStatus("mandatory")
_TemperatureSensor4WarningReset_Type = OctetString
_TemperatureSensor4WarningReset_Object = MibTableColumn
temperatureSensor4WarningReset = _TemperatureSensor4WarningReset_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 4, 1, 33),
    _TemperatureSensor4WarningReset_Type()
)
temperatureSensor4WarningReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensor4WarningReset.setStatus("mandatory")
_TemperatureSensor5HardShutdown_Type = OctetString
_TemperatureSensor5HardShutdown_Object = MibTableColumn
temperatureSensor5HardShutdown = _TemperatureSensor5HardShutdown_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 4, 1, 34),
    _TemperatureSensor5HardShutdown_Type()
)
temperatureSensor5HardShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensor5HardShutdown.setStatus("mandatory")
_TemperatureSensor5Warning_Type = OctetString
_TemperatureSensor5Warning_Object = MibTableColumn
temperatureSensor5Warning = _TemperatureSensor5Warning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 4, 1, 35),
    _TemperatureSensor5Warning_Type()
)
temperatureSensor5Warning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensor5Warning.setStatus("mandatory")
_TemperatureSensor5WarningReset_Type = OctetString
_TemperatureSensor5WarningReset_Object = MibTableColumn
temperatureSensor5WarningReset = _TemperatureSensor5WarningReset_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 4, 1, 36),
    _TemperatureSensor5WarningReset_Type()
)
temperatureSensor5WarningReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensor5WarningReset.setStatus("mandatory")
_TemperatureSensor6HardShutdown_Type = OctetString
_TemperatureSensor6HardShutdown_Object = MibTableColumn
temperatureSensor6HardShutdown = _TemperatureSensor6HardShutdown_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 4, 1, 37),
    _TemperatureSensor6HardShutdown_Type()
)
temperatureSensor6HardShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensor6HardShutdown.setStatus("mandatory")
_TemperatureSensor6Warning_Type = OctetString
_TemperatureSensor6Warning_Object = MibTableColumn
temperatureSensor6Warning = _TemperatureSensor6Warning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 4, 1, 38),
    _TemperatureSensor6Warning_Type()
)
temperatureSensor6Warning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensor6Warning.setStatus("mandatory")
_TemperatureSensor6WarningReset_Type = OctetString
_TemperatureSensor6WarningReset_Object = MibTableColumn
temperatureSensor6WarningReset = _TemperatureSensor6WarningReset_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 4, 1, 39),
    _TemperatureSensor6WarningReset_Type()
)
temperatureSensor6WarningReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensor6WarningReset.setStatus("mandatory")
_BladeVoltagesTable_Object = MibTable
bladeVoltagesTable = _BladeVoltagesTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 5)
)
if mibBuilder.loadTexts:
    bladeVoltagesTable.setStatus("mandatory")
_BladeVoltagesEntry_Object = MibTableRow
bladeVoltagesEntry = _BladeVoltagesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 5, 1)
)
bladeVoltagesEntry.setIndexNames(
    (0, "BLADE-MIB", "voltageIndex"),
)
if mibBuilder.loadTexts:
    bladeVoltagesEntry.setStatus("mandatory")
_VoltageIndex_Type = Integer32
_VoltageIndex_Object = MibTableColumn
voltageIndex = _VoltageIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 5, 1, 1),
    _VoltageIndex_Type()
)
voltageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageIndex.setStatus("mandatory")


class _VoltageBladeId_Type(Integer32):
    """Custom type voltageBladeId based on Integer32"""
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
        *(("blade1", 1),
          ("blade10", 10),
          ("blade11", 11),
          ("blade12", 12),
          ("blade13", 13),
          ("blade14", 14),
          ("blade2", 2),
          ("blade3", 3),
          ("blade4", 4),
          ("blade5", 5),
          ("blade6", 6),
          ("blade7", 7),
          ("blade8", 8),
          ("blade9", 9))
    )


_VoltageBladeId_Type.__name__ = "Integer32"
_VoltageBladeId_Object = MibTableColumn
voltageBladeId = _VoltageBladeId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 5, 1, 2),
    _VoltageBladeId_Type()
)
voltageBladeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageBladeId.setStatus("mandatory")


class _VoltageBladeExists_Type(Integer32):
    """Custom type voltageBladeExists based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_VoltageBladeExists_Type.__name__ = "Integer32"
_VoltageBladeExists_Object = MibTableColumn
voltageBladeExists = _VoltageBladeExists_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 5, 1, 3),
    _VoltageBladeExists_Type()
)
voltageBladeExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageBladeExists.setStatus("mandatory")


class _VoltageBladePowerState_Type(Integer32):
    """Custom type voltageBladePowerState based on Integer32"""
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


_VoltageBladePowerState_Type.__name__ = "Integer32"
_VoltageBladePowerState_Object = MibTableColumn
voltageBladePowerState = _VoltageBladePowerState_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 5, 1, 4),
    _VoltageBladePowerState_Type()
)
voltageBladePowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageBladePowerState.setStatus("mandatory")
_VoltageBladeName_Type = OctetString
_VoltageBladeName_Object = MibTableColumn
voltageBladeName = _VoltageBladeName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 5, 1, 5),
    _VoltageBladeName_Type()
)
voltageBladeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageBladeName.setStatus("mandatory")
_BladePlus5Volt_Type = OctetString
_BladePlus5Volt_Object = MibTableColumn
bladePlus5Volt = _BladePlus5Volt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 5, 1, 6),
    _BladePlus5Volt_Type()
)
bladePlus5Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladePlus5Volt.setStatus("mandatory")
_BladePlus3pt3Volt_Type = OctetString
_BladePlus3pt3Volt_Object = MibTableColumn
bladePlus3pt3Volt = _BladePlus3pt3Volt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 5, 1, 7),
    _BladePlus3pt3Volt_Type()
)
bladePlus3pt3Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladePlus3pt3Volt.setStatus("mandatory")
_BladePlus12Volt_Type = OctetString
_BladePlus12Volt_Object = MibTableColumn
bladePlus12Volt = _BladePlus12Volt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 5, 1, 8),
    _BladePlus12Volt_Type()
)
bladePlus12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladePlus12Volt.setStatus("mandatory")
_BladePlus2pt5Volt_Type = OctetString
_BladePlus2pt5Volt_Object = MibTableColumn
bladePlus2pt5Volt = _BladePlus2pt5Volt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 5, 1, 10),
    _BladePlus2pt5Volt_Type()
)
bladePlus2pt5Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladePlus2pt5Volt.setStatus("mandatory")
_BladePlus1pt5Volt_Type = OctetString
_BladePlus1pt5Volt_Object = MibTableColumn
bladePlus1pt5Volt = _BladePlus1pt5Volt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 5, 1, 11),
    _BladePlus1pt5Volt_Type()
)
bladePlus1pt5Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladePlus1pt5Volt.setStatus("mandatory")
_BladePlus1pt25Volt_Type = OctetString
_BladePlus1pt25Volt_Object = MibTableColumn
bladePlus1pt25Volt = _BladePlus1pt25Volt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 5, 1, 12),
    _BladePlus1pt25Volt_Type()
)
bladePlus1pt25Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladePlus1pt25Volt.setStatus("mandatory")
_BladeVRM1Volt_Type = OctetString
_BladeVRM1Volt_Object = MibTableColumn
bladeVRM1Volt = _BladeVRM1Volt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 5, 1, 13),
    _BladeVRM1Volt_Type()
)
bladeVRM1Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeVRM1Volt.setStatus("mandatory")


class _BladeSensorVoltCapability_Type(Integer32):
    """Custom type bladeSensorVoltCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_BladeSensorVoltCapability_Type.__name__ = "Integer32"
_BladeSensorVoltCapability_Object = MibTableColumn
bladeSensorVoltCapability = _BladeSensorVoltCapability_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 5, 1, 14),
    _BladeSensorVoltCapability_Type()
)
bladeSensorVoltCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensorVoltCapability.setStatus("mandatory")
_BladeSensor1Volt_Type = OctetString
_BladeSensor1Volt_Object = MibTableColumn
bladeSensor1Volt = _BladeSensor1Volt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 5, 1, 15),
    _BladeSensor1Volt_Type()
)
bladeSensor1Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor1Volt.setStatus("mandatory")
_BladeSensor2Volt_Type = OctetString
_BladeSensor2Volt_Object = MibTableColumn
bladeSensor2Volt = _BladeSensor2Volt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 5, 1, 16),
    _BladeSensor2Volt_Type()
)
bladeSensor2Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor2Volt.setStatus("mandatory")
_BladeSensor3Volt_Type = OctetString
_BladeSensor3Volt_Object = MibTableColumn
bladeSensor3Volt = _BladeSensor3Volt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 5, 1, 17),
    _BladeSensor3Volt_Type()
)
bladeSensor3Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor3Volt.setStatus("mandatory")
_BladeSensor4Volt_Type = OctetString
_BladeSensor4Volt_Object = MibTableColumn
bladeSensor4Volt = _BladeSensor4Volt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 5, 1, 18),
    _BladeSensor4Volt_Type()
)
bladeSensor4Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor4Volt.setStatus("mandatory")
_BladeSensor5Volt_Type = OctetString
_BladeSensor5Volt_Object = MibTableColumn
bladeSensor5Volt = _BladeSensor5Volt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 5, 1, 19),
    _BladeSensor5Volt_Type()
)
bladeSensor5Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor5Volt.setStatus("mandatory")
_BladeSensor6Volt_Type = OctetString
_BladeSensor6Volt_Object = MibTableColumn
bladeSensor6Volt = _BladeSensor6Volt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 5, 1, 20),
    _BladeSensor6Volt_Type()
)
bladeSensor6Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor6Volt.setStatus("mandatory")
_BladeSensor7Volt_Type = OctetString
_BladeSensor7Volt_Object = MibTableColumn
bladeSensor7Volt = _BladeSensor7Volt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 5, 1, 21),
    _BladeSensor7Volt_Type()
)
bladeSensor7Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor7Volt.setStatus("mandatory")
_BladeSensor8Volt_Type = OctetString
_BladeSensor8Volt_Object = MibTableColumn
bladeSensor8Volt = _BladeSensor8Volt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 5, 1, 22),
    _BladeSensor8Volt_Type()
)
bladeSensor8Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor8Volt.setStatus("mandatory")
_BladeSensor9Volt_Type = OctetString
_BladeSensor9Volt_Object = MibTableColumn
bladeSensor9Volt = _BladeSensor9Volt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 5, 1, 23),
    _BladeSensor9Volt_Type()
)
bladeSensor9Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor9Volt.setStatus("mandatory")
_BladeSensor10Volt_Type = OctetString
_BladeSensor10Volt_Object = MibTableColumn
bladeSensor10Volt = _BladeSensor10Volt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 5, 1, 24),
    _BladeSensor10Volt_Type()
)
bladeSensor10Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor10Volt.setStatus("mandatory")
_BladeSensor11Volt_Type = OctetString
_BladeSensor11Volt_Object = MibTableColumn
bladeSensor11Volt = _BladeSensor11Volt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 5, 1, 25),
    _BladeSensor11Volt_Type()
)
bladeSensor11Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor11Volt.setStatus("mandatory")
_BladeSensor12Volt_Type = OctetString
_BladeSensor12Volt_Object = MibTableColumn
bladeSensor12Volt = _BladeSensor12Volt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 5, 1, 26),
    _BladeSensor12Volt_Type()
)
bladeSensor12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor12Volt.setStatus("mandatory")
_BladeSensor13Volt_Type = OctetString
_BladeSensor13Volt_Object = MibTableColumn
bladeSensor13Volt = _BladeSensor13Volt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 5, 1, 27),
    _BladeSensor13Volt_Type()
)
bladeSensor13Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor13Volt.setStatus("mandatory")
_BladeSensor14Volt_Type = OctetString
_BladeSensor14Volt_Object = MibTableColumn
bladeSensor14Volt = _BladeSensor14Volt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 5, 1, 28),
    _BladeSensor14Volt_Type()
)
bladeSensor14Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor14Volt.setStatus("mandatory")
_BladeSensor15Volt_Type = OctetString
_BladeSensor15Volt_Object = MibTableColumn
bladeSensor15Volt = _BladeSensor15Volt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 5, 1, 29),
    _BladeSensor15Volt_Type()
)
bladeSensor15Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor15Volt.setStatus("mandatory")
_BladeSensor16Volt_Type = OctetString
_BladeSensor16Volt_Object = MibTableColumn
bladeSensor16Volt = _BladeSensor16Volt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 5, 1, 30),
    _BladeSensor16Volt_Type()
)
bladeSensor16Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor16Volt.setStatus("mandatory")
_BladeSensor17Volt_Type = OctetString
_BladeSensor17Volt_Object = MibTableColumn
bladeSensor17Volt = _BladeSensor17Volt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 5, 1, 31),
    _BladeSensor17Volt_Type()
)
bladeSensor17Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor17Volt.setStatus("mandatory")
_BladeSensor18Volt_Type = OctetString
_BladeSensor18Volt_Object = MibTableColumn
bladeSensor18Volt = _BladeSensor18Volt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 5, 1, 32),
    _BladeSensor18Volt_Type()
)
bladeSensor18Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor18Volt.setStatus("mandatory")
_BladeSensor19Volt_Type = OctetString
_BladeSensor19Volt_Object = MibTableColumn
bladeSensor19Volt = _BladeSensor19Volt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 5, 1, 33),
    _BladeSensor19Volt_Type()
)
bladeSensor19Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor19Volt.setStatus("mandatory")
_BladeSensor20Volt_Type = OctetString
_BladeSensor20Volt_Object = MibTableColumn
bladeSensor20Volt = _BladeSensor20Volt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 5, 1, 34),
    _BladeSensor20Volt_Type()
)
bladeSensor20Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor20Volt.setStatus("mandatory")
_BladeSensor21Volt_Type = OctetString
_BladeSensor21Volt_Object = MibTableColumn
bladeSensor21Volt = _BladeSensor21Volt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 5, 1, 35),
    _BladeSensor21Volt_Type()
)
bladeSensor21Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor21Volt.setStatus("mandatory")
_BladeSensor22Volt_Type = OctetString
_BladeSensor22Volt_Object = MibTableColumn
bladeSensor22Volt = _BladeSensor22Volt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 5, 1, 36),
    _BladeSensor22Volt_Type()
)
bladeSensor22Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor22Volt.setStatus("mandatory")
_BladeSensor23Volt_Type = OctetString
_BladeSensor23Volt_Object = MibTableColumn
bladeSensor23Volt = _BladeSensor23Volt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 5, 1, 37),
    _BladeSensor23Volt_Type()
)
bladeSensor23Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor23Volt.setStatus("mandatory")
_BladeSensor24Volt_Type = OctetString
_BladeSensor24Volt_Object = MibTableColumn
bladeSensor24Volt = _BladeSensor24Volt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 5, 1, 38),
    _BladeSensor24Volt_Type()
)
bladeSensor24Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor24Volt.setStatus("mandatory")
_BladeSensor25Volt_Type = OctetString
_BladeSensor25Volt_Object = MibTableColumn
bladeSensor25Volt = _BladeSensor25Volt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 5, 1, 39),
    _BladeSensor25Volt_Type()
)
bladeSensor25Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor25Volt.setStatus("mandatory")
_BladeSensor26Volt_Type = OctetString
_BladeSensor26Volt_Object = MibTableColumn
bladeSensor26Volt = _BladeSensor26Volt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 5, 1, 40),
    _BladeSensor26Volt_Type()
)
bladeSensor26Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor26Volt.setStatus("mandatory")
_BladeSensor27Volt_Type = OctetString
_BladeSensor27Volt_Object = MibTableColumn
bladeSensor27Volt = _BladeSensor27Volt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 5, 1, 41),
    _BladeSensor27Volt_Type()
)
bladeSensor27Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor27Volt.setStatus("mandatory")
_BladeSensor28Volt_Type = OctetString
_BladeSensor28Volt_Object = MibTableColumn
bladeSensor28Volt = _BladeSensor28Volt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 5, 1, 42),
    _BladeSensor28Volt_Type()
)
bladeSensor28Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor28Volt.setStatus("mandatory")
_BladeSensor29Volt_Type = OctetString
_BladeSensor29Volt_Object = MibTableColumn
bladeSensor29Volt = _BladeSensor29Volt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 5, 1, 43),
    _BladeSensor29Volt_Type()
)
bladeSensor29Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor29Volt.setStatus("mandatory")
_BladeSensor30Volt_Type = OctetString
_BladeSensor30Volt_Object = MibTableColumn
bladeSensor30Volt = _BladeSensor30Volt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 5, 1, 44),
    _BladeSensor30Volt_Type()
)
bladeSensor30Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor30Volt.setStatus("mandatory")
_BladeVoltageThresholdsTable_Object = MibTable
bladeVoltageThresholdsTable = _BladeVoltageThresholdsTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6)
)
if mibBuilder.loadTexts:
    bladeVoltageThresholdsTable.setStatus("mandatory")
_BladeVoltageThresholdsEntry_Object = MibTableRow
bladeVoltageThresholdsEntry = _BladeVoltageThresholdsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1)
)
bladeVoltageThresholdsEntry.setIndexNames(
    (0, "BLADE-MIB", "voltageThresholdIndex"),
)
if mibBuilder.loadTexts:
    bladeVoltageThresholdsEntry.setStatus("mandatory")
_VoltageThresholdIndex_Type = Integer32
_VoltageThresholdIndex_Object = MibTableColumn
voltageThresholdIndex = _VoltageThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 1),
    _VoltageThresholdIndex_Type()
)
voltageThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageThresholdIndex.setStatus("mandatory")


class _VoltageThresholdBladeId_Type(Integer32):
    """Custom type voltageThresholdBladeId based on Integer32"""
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
        *(("blade1", 1),
          ("blade10", 10),
          ("blade11", 11),
          ("blade12", 12),
          ("blade13", 13),
          ("blade14", 14),
          ("blade2", 2),
          ("blade3", 3),
          ("blade4", 4),
          ("blade5", 5),
          ("blade6", 6),
          ("blade7", 7),
          ("blade8", 8),
          ("blade9", 9))
    )


_VoltageThresholdBladeId_Type.__name__ = "Integer32"
_VoltageThresholdBladeId_Object = MibTableColumn
voltageThresholdBladeId = _VoltageThresholdBladeId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 2),
    _VoltageThresholdBladeId_Type()
)
voltageThresholdBladeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageThresholdBladeId.setStatus("mandatory")


class _VoltageThresholdBladeExists_Type(Integer32):
    """Custom type voltageThresholdBladeExists based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_VoltageThresholdBladeExists_Type.__name__ = "Integer32"
_VoltageThresholdBladeExists_Object = MibTableColumn
voltageThresholdBladeExists = _VoltageThresholdBladeExists_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 3),
    _VoltageThresholdBladeExists_Type()
)
voltageThresholdBladeExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageThresholdBladeExists.setStatus("mandatory")


class _VoltageThresholdBladePowerState_Type(Integer32):
    """Custom type voltageThresholdBladePowerState based on Integer32"""
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


_VoltageThresholdBladePowerState_Type.__name__ = "Integer32"
_VoltageThresholdBladePowerState_Object = MibTableColumn
voltageThresholdBladePowerState = _VoltageThresholdBladePowerState_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 4),
    _VoltageThresholdBladePowerState_Type()
)
voltageThresholdBladePowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageThresholdBladePowerState.setStatus("mandatory")
_VoltageThresholdBladeName_Type = OctetString
_VoltageThresholdBladeName_Object = MibTableColumn
voltageThresholdBladeName = _VoltageThresholdBladeName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 5),
    _VoltageThresholdBladeName_Type()
)
voltageThresholdBladeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltageThresholdBladeName.setStatus("mandatory")
_BladePlus5VoltHighWarning_Type = OctetString
_BladePlus5VoltHighWarning_Object = MibTableColumn
bladePlus5VoltHighWarning = _BladePlus5VoltHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 6),
    _BladePlus5VoltHighWarning_Type()
)
bladePlus5VoltHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladePlus5VoltHighWarning.setStatus("mandatory")
_BladePlus5VoltLowWarning_Type = OctetString
_BladePlus5VoltLowWarning_Object = MibTableColumn
bladePlus5VoltLowWarning = _BladePlus5VoltLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 7),
    _BladePlus5VoltLowWarning_Type()
)
bladePlus5VoltLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladePlus5VoltLowWarning.setStatus("mandatory")
_BladePlus3pt3VoltHighWarning_Type = OctetString
_BladePlus3pt3VoltHighWarning_Object = MibTableColumn
bladePlus3pt3VoltHighWarning = _BladePlus3pt3VoltHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 8),
    _BladePlus3pt3VoltHighWarning_Type()
)
bladePlus3pt3VoltHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladePlus3pt3VoltHighWarning.setStatus("mandatory")
_BladePlus3pt3VoltLowWarning_Type = OctetString
_BladePlus3pt3VoltLowWarning_Object = MibTableColumn
bladePlus3pt3VoltLowWarning = _BladePlus3pt3VoltLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 9),
    _BladePlus3pt3VoltLowWarning_Type()
)
bladePlus3pt3VoltLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladePlus3pt3VoltLowWarning.setStatus("mandatory")
_BladePlus12VoltHighWarning_Type = OctetString
_BladePlus12VoltHighWarning_Object = MibTableColumn
bladePlus12VoltHighWarning = _BladePlus12VoltHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 10),
    _BladePlus12VoltHighWarning_Type()
)
bladePlus12VoltHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladePlus12VoltHighWarning.setStatus("mandatory")
_BladePlus12VoltLowWarning_Type = OctetString
_BladePlus12VoltLowWarning_Object = MibTableColumn
bladePlus12VoltLowWarning = _BladePlus12VoltLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 11),
    _BladePlus12VoltLowWarning_Type()
)
bladePlus12VoltLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladePlus12VoltLowWarning.setStatus("mandatory")
_BladePlus2pt5VoltHighWarning_Type = OctetString
_BladePlus2pt5VoltHighWarning_Object = MibTableColumn
bladePlus2pt5VoltHighWarning = _BladePlus2pt5VoltHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 14),
    _BladePlus2pt5VoltHighWarning_Type()
)
bladePlus2pt5VoltHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladePlus2pt5VoltHighWarning.setStatus("mandatory")
_BladePlus2pt5VoltLowWarning_Type = OctetString
_BladePlus2pt5VoltLowWarning_Object = MibTableColumn
bladePlus2pt5VoltLowWarning = _BladePlus2pt5VoltLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 15),
    _BladePlus2pt5VoltLowWarning_Type()
)
bladePlus2pt5VoltLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladePlus2pt5VoltLowWarning.setStatus("mandatory")
_BladePlus1pt5VoltHighWarning_Type = OctetString
_BladePlus1pt5VoltHighWarning_Object = MibTableColumn
bladePlus1pt5VoltHighWarning = _BladePlus1pt5VoltHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 16),
    _BladePlus1pt5VoltHighWarning_Type()
)
bladePlus1pt5VoltHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladePlus1pt5VoltHighWarning.setStatus("mandatory")
_BladePlus1pt5VoltLowWarning_Type = OctetString
_BladePlus1pt5VoltLowWarning_Object = MibTableColumn
bladePlus1pt5VoltLowWarning = _BladePlus1pt5VoltLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 17),
    _BladePlus1pt5VoltLowWarning_Type()
)
bladePlus1pt5VoltLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladePlus1pt5VoltLowWarning.setStatus("mandatory")
_BladePlus1pt25VoltHighWarning_Type = OctetString
_BladePlus1pt25VoltHighWarning_Object = MibTableColumn
bladePlus1pt25VoltHighWarning = _BladePlus1pt25VoltHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 18),
    _BladePlus1pt25VoltHighWarning_Type()
)
bladePlus1pt25VoltHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladePlus1pt25VoltHighWarning.setStatus("mandatory")
_BladePlus1pt25VoltLowWarning_Type = OctetString
_BladePlus1pt25VoltLowWarning_Object = MibTableColumn
bladePlus1pt25VoltLowWarning = _BladePlus1pt25VoltLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 19),
    _BladePlus1pt25VoltLowWarning_Type()
)
bladePlus1pt25VoltLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladePlus1pt25VoltLowWarning.setStatus("mandatory")


class _BladeVoltThresholdSensorCapability_Type(Integer32):
    """Custom type bladeVoltThresholdSensorCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_BladeVoltThresholdSensorCapability_Type.__name__ = "Integer32"
_BladeVoltThresholdSensorCapability_Object = MibTableColumn
bladeVoltThresholdSensorCapability = _BladeVoltThresholdSensorCapability_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 22),
    _BladeVoltThresholdSensorCapability_Type()
)
bladeVoltThresholdSensorCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeVoltThresholdSensorCapability.setStatus("mandatory")
_BladeSensor1VoltHighWarning_Type = OctetString
_BladeSensor1VoltHighWarning_Object = MibTableColumn
bladeSensor1VoltHighWarning = _BladeSensor1VoltHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 23),
    _BladeSensor1VoltHighWarning_Type()
)
bladeSensor1VoltHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor1VoltHighWarning.setStatus("mandatory")
_BladeSensor1VoltLowWarning_Type = OctetString
_BladeSensor1VoltLowWarning_Object = MibTableColumn
bladeSensor1VoltLowWarning = _BladeSensor1VoltLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 24),
    _BladeSensor1VoltLowWarning_Type()
)
bladeSensor1VoltLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor1VoltLowWarning.setStatus("mandatory")
_BladeSensor2VoltHighWarning_Type = OctetString
_BladeSensor2VoltHighWarning_Object = MibTableColumn
bladeSensor2VoltHighWarning = _BladeSensor2VoltHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 25),
    _BladeSensor2VoltHighWarning_Type()
)
bladeSensor2VoltHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor2VoltHighWarning.setStatus("mandatory")
_BladeSensor2VoltLowWarning_Type = OctetString
_BladeSensor2VoltLowWarning_Object = MibTableColumn
bladeSensor2VoltLowWarning = _BladeSensor2VoltLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 26),
    _BladeSensor2VoltLowWarning_Type()
)
bladeSensor2VoltLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor2VoltLowWarning.setStatus("mandatory")
_BladeSensor3VoltHighWarning_Type = OctetString
_BladeSensor3VoltHighWarning_Object = MibTableColumn
bladeSensor3VoltHighWarning = _BladeSensor3VoltHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 27),
    _BladeSensor3VoltHighWarning_Type()
)
bladeSensor3VoltHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor3VoltHighWarning.setStatus("mandatory")
_BladeSensor3VoltLowWarning_Type = OctetString
_BladeSensor3VoltLowWarning_Object = MibTableColumn
bladeSensor3VoltLowWarning = _BladeSensor3VoltLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 28),
    _BladeSensor3VoltLowWarning_Type()
)
bladeSensor3VoltLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor3VoltLowWarning.setStatus("mandatory")
_BladeSensor4VoltHighWarning_Type = OctetString
_BladeSensor4VoltHighWarning_Object = MibTableColumn
bladeSensor4VoltHighWarning = _BladeSensor4VoltHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 29),
    _BladeSensor4VoltHighWarning_Type()
)
bladeSensor4VoltHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor4VoltHighWarning.setStatus("mandatory")
_BladeSensor4VoltLowWarning_Type = OctetString
_BladeSensor4VoltLowWarning_Object = MibTableColumn
bladeSensor4VoltLowWarning = _BladeSensor4VoltLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 30),
    _BladeSensor4VoltLowWarning_Type()
)
bladeSensor4VoltLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor4VoltLowWarning.setStatus("mandatory")
_BladeSensor5VoltHighWarning_Type = OctetString
_BladeSensor5VoltHighWarning_Object = MibTableColumn
bladeSensor5VoltHighWarning = _BladeSensor5VoltHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 31),
    _BladeSensor5VoltHighWarning_Type()
)
bladeSensor5VoltHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor5VoltHighWarning.setStatus("mandatory")
_BladeSensor5VoltLowWarning_Type = OctetString
_BladeSensor5VoltLowWarning_Object = MibTableColumn
bladeSensor5VoltLowWarning = _BladeSensor5VoltLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 32),
    _BladeSensor5VoltLowWarning_Type()
)
bladeSensor5VoltLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor5VoltLowWarning.setStatus("mandatory")
_BladeSensor6VoltHighWarning_Type = OctetString
_BladeSensor6VoltHighWarning_Object = MibTableColumn
bladeSensor6VoltHighWarning = _BladeSensor6VoltHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 33),
    _BladeSensor6VoltHighWarning_Type()
)
bladeSensor6VoltHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor6VoltHighWarning.setStatus("mandatory")
_BladeSensor6VoltLowWarning_Type = OctetString
_BladeSensor6VoltLowWarning_Object = MibTableColumn
bladeSensor6VoltLowWarning = _BladeSensor6VoltLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 34),
    _BladeSensor6VoltLowWarning_Type()
)
bladeSensor6VoltLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor6VoltLowWarning.setStatus("mandatory")
_BladeSensor7VoltHighWarning_Type = OctetString
_BladeSensor7VoltHighWarning_Object = MibTableColumn
bladeSensor7VoltHighWarning = _BladeSensor7VoltHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 35),
    _BladeSensor7VoltHighWarning_Type()
)
bladeSensor7VoltHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor7VoltHighWarning.setStatus("mandatory")
_BladeSensor7VoltLowWarning_Type = OctetString
_BladeSensor7VoltLowWarning_Object = MibTableColumn
bladeSensor7VoltLowWarning = _BladeSensor7VoltLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 36),
    _BladeSensor7VoltLowWarning_Type()
)
bladeSensor7VoltLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor7VoltLowWarning.setStatus("mandatory")
_BladeSensor8VoltHighWarning_Type = OctetString
_BladeSensor8VoltHighWarning_Object = MibTableColumn
bladeSensor8VoltHighWarning = _BladeSensor8VoltHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 37),
    _BladeSensor8VoltHighWarning_Type()
)
bladeSensor8VoltHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor8VoltHighWarning.setStatus("mandatory")
_BladeSensor8VoltLowWarning_Type = OctetString
_BladeSensor8VoltLowWarning_Object = MibTableColumn
bladeSensor8VoltLowWarning = _BladeSensor8VoltLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 38),
    _BladeSensor8VoltLowWarning_Type()
)
bladeSensor8VoltLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor8VoltLowWarning.setStatus("mandatory")
_BladeSensor9VoltHighWarning_Type = OctetString
_BladeSensor9VoltHighWarning_Object = MibTableColumn
bladeSensor9VoltHighWarning = _BladeSensor9VoltHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 39),
    _BladeSensor9VoltHighWarning_Type()
)
bladeSensor9VoltHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor9VoltHighWarning.setStatus("mandatory")
_BladeSensor9VoltLowWarning_Type = OctetString
_BladeSensor9VoltLowWarning_Object = MibTableColumn
bladeSensor9VoltLowWarning = _BladeSensor9VoltLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 40),
    _BladeSensor9VoltLowWarning_Type()
)
bladeSensor9VoltLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor9VoltLowWarning.setStatus("mandatory")
_BladeSensor10VoltHighWarning_Type = OctetString
_BladeSensor10VoltHighWarning_Object = MibTableColumn
bladeSensor10VoltHighWarning = _BladeSensor10VoltHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 41),
    _BladeSensor10VoltHighWarning_Type()
)
bladeSensor10VoltHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor10VoltHighWarning.setStatus("mandatory")
_BladeSensor10VoltLowWarning_Type = OctetString
_BladeSensor10VoltLowWarning_Object = MibTableColumn
bladeSensor10VoltLowWarning = _BladeSensor10VoltLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 42),
    _BladeSensor10VoltLowWarning_Type()
)
bladeSensor10VoltLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor10VoltLowWarning.setStatus("mandatory")
_BladeSensor11VoltHighWarning_Type = OctetString
_BladeSensor11VoltHighWarning_Object = MibTableColumn
bladeSensor11VoltHighWarning = _BladeSensor11VoltHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 43),
    _BladeSensor11VoltHighWarning_Type()
)
bladeSensor11VoltHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor11VoltHighWarning.setStatus("mandatory")
_BladeSensor11VoltLowWarning_Type = OctetString
_BladeSensor11VoltLowWarning_Object = MibTableColumn
bladeSensor11VoltLowWarning = _BladeSensor11VoltLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 44),
    _BladeSensor11VoltLowWarning_Type()
)
bladeSensor11VoltLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor11VoltLowWarning.setStatus("mandatory")
_BladeSensor12VoltHighWarning_Type = OctetString
_BladeSensor12VoltHighWarning_Object = MibTableColumn
bladeSensor12VoltHighWarning = _BladeSensor12VoltHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 45),
    _BladeSensor12VoltHighWarning_Type()
)
bladeSensor12VoltHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor12VoltHighWarning.setStatus("mandatory")
_BladeSensor12VoltLowWarning_Type = OctetString
_BladeSensor12VoltLowWarning_Object = MibTableColumn
bladeSensor12VoltLowWarning = _BladeSensor12VoltLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 46),
    _BladeSensor12VoltLowWarning_Type()
)
bladeSensor12VoltLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor12VoltLowWarning.setStatus("mandatory")
_BladeSensor13VoltHighWarning_Type = OctetString
_BladeSensor13VoltHighWarning_Object = MibTableColumn
bladeSensor13VoltHighWarning = _BladeSensor13VoltHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 47),
    _BladeSensor13VoltHighWarning_Type()
)
bladeSensor13VoltHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor13VoltHighWarning.setStatus("mandatory")
_BladeSensor13VoltLowWarning_Type = OctetString
_BladeSensor13VoltLowWarning_Object = MibTableColumn
bladeSensor13VoltLowWarning = _BladeSensor13VoltLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 48),
    _BladeSensor13VoltLowWarning_Type()
)
bladeSensor13VoltLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor13VoltLowWarning.setStatus("mandatory")
_BladeSensor14VoltHighWarning_Type = OctetString
_BladeSensor14VoltHighWarning_Object = MibTableColumn
bladeSensor14VoltHighWarning = _BladeSensor14VoltHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 49),
    _BladeSensor14VoltHighWarning_Type()
)
bladeSensor14VoltHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor14VoltHighWarning.setStatus("mandatory")
_BladeSensor14VoltLowWarning_Type = OctetString
_BladeSensor14VoltLowWarning_Object = MibTableColumn
bladeSensor14VoltLowWarning = _BladeSensor14VoltLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 50),
    _BladeSensor14VoltLowWarning_Type()
)
bladeSensor14VoltLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor14VoltLowWarning.setStatus("mandatory")
_BladeSensor15VoltHighWarning_Type = OctetString
_BladeSensor15VoltHighWarning_Object = MibTableColumn
bladeSensor15VoltHighWarning = _BladeSensor15VoltHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 51),
    _BladeSensor15VoltHighWarning_Type()
)
bladeSensor15VoltHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor15VoltHighWarning.setStatus("mandatory")
_BladeSensor15VoltLowWarning_Type = OctetString
_BladeSensor15VoltLowWarning_Object = MibTableColumn
bladeSensor15VoltLowWarning = _BladeSensor15VoltLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 52),
    _BladeSensor15VoltLowWarning_Type()
)
bladeSensor15VoltLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor15VoltLowWarning.setStatus("mandatory")
_BladeSensor16VoltHighWarning_Type = OctetString
_BladeSensor16VoltHighWarning_Object = MibTableColumn
bladeSensor16VoltHighWarning = _BladeSensor16VoltHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 53),
    _BladeSensor16VoltHighWarning_Type()
)
bladeSensor16VoltHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor16VoltHighWarning.setStatus("mandatory")
_BladeSensor16VoltLowWarning_Type = OctetString
_BladeSensor16VoltLowWarning_Object = MibTableColumn
bladeSensor16VoltLowWarning = _BladeSensor16VoltLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 54),
    _BladeSensor16VoltLowWarning_Type()
)
bladeSensor16VoltLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor16VoltLowWarning.setStatus("mandatory")
_BladeSensor17VoltHighWarning_Type = OctetString
_BladeSensor17VoltHighWarning_Object = MibTableColumn
bladeSensor17VoltHighWarning = _BladeSensor17VoltHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 55),
    _BladeSensor17VoltHighWarning_Type()
)
bladeSensor17VoltHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor17VoltHighWarning.setStatus("mandatory")
_BladeSensor17VoltLowWarning_Type = OctetString
_BladeSensor17VoltLowWarning_Object = MibTableColumn
bladeSensor17VoltLowWarning = _BladeSensor17VoltLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 56),
    _BladeSensor17VoltLowWarning_Type()
)
bladeSensor17VoltLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor17VoltLowWarning.setStatus("mandatory")
_BladeSensor18VoltHighWarning_Type = OctetString
_BladeSensor18VoltHighWarning_Object = MibTableColumn
bladeSensor18VoltHighWarning = _BladeSensor18VoltHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 57),
    _BladeSensor18VoltHighWarning_Type()
)
bladeSensor18VoltHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor18VoltHighWarning.setStatus("mandatory")
_BladeSensor18VoltLowWarning_Type = OctetString
_BladeSensor18VoltLowWarning_Object = MibTableColumn
bladeSensor18VoltLowWarning = _BladeSensor18VoltLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 58),
    _BladeSensor18VoltLowWarning_Type()
)
bladeSensor18VoltLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor18VoltLowWarning.setStatus("mandatory")
_BladeSensor19VoltHighWarning_Type = OctetString
_BladeSensor19VoltHighWarning_Object = MibTableColumn
bladeSensor19VoltHighWarning = _BladeSensor19VoltHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 59),
    _BladeSensor19VoltHighWarning_Type()
)
bladeSensor19VoltHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor19VoltHighWarning.setStatus("mandatory")
_BladeSensor19VoltLowWarning_Type = OctetString
_BladeSensor19VoltLowWarning_Object = MibTableColumn
bladeSensor19VoltLowWarning = _BladeSensor19VoltLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 60),
    _BladeSensor19VoltLowWarning_Type()
)
bladeSensor19VoltLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor19VoltLowWarning.setStatus("mandatory")
_BladeSensor20VoltHighWarning_Type = OctetString
_BladeSensor20VoltHighWarning_Object = MibTableColumn
bladeSensor20VoltHighWarning = _BladeSensor20VoltHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 61),
    _BladeSensor20VoltHighWarning_Type()
)
bladeSensor20VoltHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor20VoltHighWarning.setStatus("mandatory")
_BladeSensor20VoltLowWarning_Type = OctetString
_BladeSensor20VoltLowWarning_Object = MibTableColumn
bladeSensor20VoltLowWarning = _BladeSensor20VoltLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 62),
    _BladeSensor20VoltLowWarning_Type()
)
bladeSensor20VoltLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor20VoltLowWarning.setStatus("mandatory")
_BladeSensor21VoltHighWarning_Type = OctetString
_BladeSensor21VoltHighWarning_Object = MibTableColumn
bladeSensor21VoltHighWarning = _BladeSensor21VoltHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 63),
    _BladeSensor21VoltHighWarning_Type()
)
bladeSensor21VoltHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor21VoltHighWarning.setStatus("mandatory")
_BladeSensor21VoltLowWarning_Type = OctetString
_BladeSensor21VoltLowWarning_Object = MibTableColumn
bladeSensor21VoltLowWarning = _BladeSensor21VoltLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 64),
    _BladeSensor21VoltLowWarning_Type()
)
bladeSensor21VoltLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor21VoltLowWarning.setStatus("mandatory")
_BladeSensor22VoltHighWarning_Type = OctetString
_BladeSensor22VoltHighWarning_Object = MibTableColumn
bladeSensor22VoltHighWarning = _BladeSensor22VoltHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 65),
    _BladeSensor22VoltHighWarning_Type()
)
bladeSensor22VoltHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor22VoltHighWarning.setStatus("mandatory")
_BladeSensor22VoltLowWarning_Type = OctetString
_BladeSensor22VoltLowWarning_Object = MibTableColumn
bladeSensor22VoltLowWarning = _BladeSensor22VoltLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 66),
    _BladeSensor22VoltLowWarning_Type()
)
bladeSensor22VoltLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor22VoltLowWarning.setStatus("mandatory")
_BladeSensor23VoltHighWarning_Type = OctetString
_BladeSensor23VoltHighWarning_Object = MibTableColumn
bladeSensor23VoltHighWarning = _BladeSensor23VoltHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 67),
    _BladeSensor23VoltHighWarning_Type()
)
bladeSensor23VoltHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor23VoltHighWarning.setStatus("mandatory")
_BladeSensor23VoltLowWarning_Type = OctetString
_BladeSensor23VoltLowWarning_Object = MibTableColumn
bladeSensor23VoltLowWarning = _BladeSensor23VoltLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 68),
    _BladeSensor23VoltLowWarning_Type()
)
bladeSensor23VoltLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor23VoltLowWarning.setStatus("mandatory")
_BladeSensor24VoltHighWarning_Type = OctetString
_BladeSensor24VoltHighWarning_Object = MibTableColumn
bladeSensor24VoltHighWarning = _BladeSensor24VoltHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 69),
    _BladeSensor24VoltHighWarning_Type()
)
bladeSensor24VoltHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor24VoltHighWarning.setStatus("mandatory")
_BladeSensor24VoltLowWarning_Type = OctetString
_BladeSensor24VoltLowWarning_Object = MibTableColumn
bladeSensor24VoltLowWarning = _BladeSensor24VoltLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 70),
    _BladeSensor24VoltLowWarning_Type()
)
bladeSensor24VoltLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor24VoltLowWarning.setStatus("mandatory")
_BladeSensor25VoltHighWarning_Type = OctetString
_BladeSensor25VoltHighWarning_Object = MibTableColumn
bladeSensor25VoltHighWarning = _BladeSensor25VoltHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 71),
    _BladeSensor25VoltHighWarning_Type()
)
bladeSensor25VoltHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor25VoltHighWarning.setStatus("mandatory")
_BladeSensor25VoltLowWarning_Type = OctetString
_BladeSensor25VoltLowWarning_Object = MibTableColumn
bladeSensor25VoltLowWarning = _BladeSensor25VoltLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 72),
    _BladeSensor25VoltLowWarning_Type()
)
bladeSensor25VoltLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor25VoltLowWarning.setStatus("mandatory")
_BladeSensor26VoltHighWarning_Type = OctetString
_BladeSensor26VoltHighWarning_Object = MibTableColumn
bladeSensor26VoltHighWarning = _BladeSensor26VoltHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 73),
    _BladeSensor26VoltHighWarning_Type()
)
bladeSensor26VoltHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor26VoltHighWarning.setStatus("mandatory")
_BladeSensor26VoltLowWarning_Type = OctetString
_BladeSensor26VoltLowWarning_Object = MibTableColumn
bladeSensor26VoltLowWarning = _BladeSensor26VoltLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 74),
    _BladeSensor26VoltLowWarning_Type()
)
bladeSensor26VoltLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor26VoltLowWarning.setStatus("mandatory")
_BladeSensor27VoltHighWarning_Type = OctetString
_BladeSensor27VoltHighWarning_Object = MibTableColumn
bladeSensor27VoltHighWarning = _BladeSensor27VoltHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 75),
    _BladeSensor27VoltHighWarning_Type()
)
bladeSensor27VoltHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor27VoltHighWarning.setStatus("mandatory")
_BladeSensor27VoltLowWarning_Type = OctetString
_BladeSensor27VoltLowWarning_Object = MibTableColumn
bladeSensor27VoltLowWarning = _BladeSensor27VoltLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 76),
    _BladeSensor27VoltLowWarning_Type()
)
bladeSensor27VoltLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor27VoltLowWarning.setStatus("mandatory")
_BladeSensor28VoltHighWarning_Type = OctetString
_BladeSensor28VoltHighWarning_Object = MibTableColumn
bladeSensor28VoltHighWarning = _BladeSensor28VoltHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 77),
    _BladeSensor28VoltHighWarning_Type()
)
bladeSensor28VoltHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor28VoltHighWarning.setStatus("mandatory")
_BladeSensor28VoltLowWarning_Type = OctetString
_BladeSensor28VoltLowWarning_Object = MibTableColumn
bladeSensor28VoltLowWarning = _BladeSensor28VoltLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 78),
    _BladeSensor28VoltLowWarning_Type()
)
bladeSensor28VoltLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor28VoltLowWarning.setStatus("mandatory")
_BladeSensor29VoltHighWarning_Type = OctetString
_BladeSensor29VoltHighWarning_Object = MibTableColumn
bladeSensor29VoltHighWarning = _BladeSensor29VoltHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 79),
    _BladeSensor29VoltHighWarning_Type()
)
bladeSensor29VoltHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor29VoltHighWarning.setStatus("mandatory")
_BladeSensor29VoltLowWarning_Type = OctetString
_BladeSensor29VoltLowWarning_Object = MibTableColumn
bladeSensor29VoltLowWarning = _BladeSensor29VoltLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 80),
    _BladeSensor29VoltLowWarning_Type()
)
bladeSensor29VoltLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor29VoltLowWarning.setStatus("mandatory")
_BladeSensor30VoltHighWarning_Type = OctetString
_BladeSensor30VoltHighWarning_Object = MibTableColumn
bladeSensor30VoltHighWarning = _BladeSensor30VoltHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 81),
    _BladeSensor30VoltHighWarning_Type()
)
bladeSensor30VoltHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor30VoltHighWarning.setStatus("mandatory")
_BladeSensor30VoltLowWarning_Type = OctetString
_BladeSensor30VoltLowWarning_Object = MibTableColumn
bladeSensor30VoltLowWarning = _BladeSensor30VoltLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 5, 6, 1, 82),
    _BladeSensor30VoltLowWarning_Type()
)
bladeSensor30VoltLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSensor30VoltLowWarning.setStatus("mandatory")
_BladePowerRestart_ObjectIdentity = ObjectIdentity
bladePowerRestart = _BladePowerRestart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 6)
)
_BladePowerRestartTable_Object = MibTable
bladePowerRestartTable = _BladePowerRestartTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 6, 1)
)
if mibBuilder.loadTexts:
    bladePowerRestartTable.setStatus("mandatory")
_BladePowerRestartEntry_Object = MibTableRow
bladePowerRestartEntry = _BladePowerRestartEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 6, 1, 1)
)
bladePowerRestartEntry.setIndexNames(
    (0, "BLADE-MIB", "powerRestartIndex"),
)
if mibBuilder.loadTexts:
    bladePowerRestartEntry.setStatus("mandatory")
_PowerRestartIndex_Type = Integer32
_PowerRestartIndex_Object = MibTableColumn
powerRestartIndex = _PowerRestartIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 6, 1, 1, 1),
    _PowerRestartIndex_Type()
)
powerRestartIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerRestartIndex.setStatus("mandatory")


class _PowerRestartBladeId_Type(Integer32):
    """Custom type powerRestartBladeId based on Integer32"""
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
        *(("blade1", 1),
          ("blade10", 10),
          ("blade11", 11),
          ("blade12", 12),
          ("blade13", 13),
          ("blade14", 14),
          ("blade2", 2),
          ("blade3", 3),
          ("blade4", 4),
          ("blade5", 5),
          ("blade6", 6),
          ("blade7", 7),
          ("blade8", 8),
          ("blade9", 9))
    )


_PowerRestartBladeId_Type.__name__ = "Integer32"
_PowerRestartBladeId_Object = MibTableColumn
powerRestartBladeId = _PowerRestartBladeId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 6, 1, 1, 2),
    _PowerRestartBladeId_Type()
)
powerRestartBladeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerRestartBladeId.setStatus("mandatory")


class _PowerRestartBladeExists_Type(Integer32):
    """Custom type powerRestartBladeExists based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_PowerRestartBladeExists_Type.__name__ = "Integer32"
_PowerRestartBladeExists_Object = MibTableColumn
powerRestartBladeExists = _PowerRestartBladeExists_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 6, 1, 1, 3),
    _PowerRestartBladeExists_Type()
)
powerRestartBladeExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerRestartBladeExists.setStatus("mandatory")


class _PowerRestartBladePowerState_Type(Integer32):
    """Custom type powerRestartBladePowerState based on Integer32"""
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


_PowerRestartBladePowerState_Type.__name__ = "Integer32"
_PowerRestartBladePowerState_Object = MibTableColumn
powerRestartBladePowerState = _PowerRestartBladePowerState_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 6, 1, 1, 4),
    _PowerRestartBladePowerState_Type()
)
powerRestartBladePowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerRestartBladePowerState.setStatus("mandatory")


class _PowerRestartBladeHealthState_Type(Integer32):
    """Custom type powerRestartBladeHealthState based on Integer32"""
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
        *(("bad", 3),
          ("good", 1),
          ("unknown", 0),
          ("warning", 2))
    )


_PowerRestartBladeHealthState_Type.__name__ = "Integer32"
_PowerRestartBladeHealthState_Object = MibTableColumn
powerRestartBladeHealthState = _PowerRestartBladeHealthState_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 6, 1, 1, 5),
    _PowerRestartBladeHealthState_Type()
)
powerRestartBladeHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerRestartBladeHealthState.setStatus("mandatory")
_PowerRestartBladeName_Type = OctetString
_PowerRestartBladeName_Object = MibTableColumn
powerRestartBladeName = _PowerRestartBladeName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 6, 1, 1, 6),
    _PowerRestartBladeName_Type()
)
powerRestartBladeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerRestartBladeName.setStatus("mandatory")


class _PowerOnOffBlade_Type(Integer32):
    """Custom type powerOnOffBlade based on Integer32"""
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


_PowerOnOffBlade_Type.__name__ = "Integer32"
_PowerOnOffBlade_Object = MibTableColumn
powerOnOffBlade = _PowerOnOffBlade_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 6, 1, 1, 7),
    _PowerOnOffBlade_Type()
)
powerOnOffBlade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerOnOffBlade.setStatus("mandatory")


class _RestartBlade_Type(Integer32):
    """Custom type restartBlade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("execute", 1)
    )


_RestartBlade_Type.__name__ = "Integer32"
_RestartBlade_Object = MibTableColumn
restartBlade = _RestartBlade_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 6, 1, 1, 8),
    _RestartBlade_Type()
)
restartBlade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartBlade.setStatus("mandatory")


class _RestartBladeSMP_Type(Integer32):
    """Custom type restartBladeSMP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("execute", 1)
    )


_RestartBladeSMP_Type.__name__ = "Integer32"
_RestartBladeSMP_Object = MibTableColumn
restartBladeSMP = _RestartBladeSMP_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 6, 1, 1, 9),
    _RestartBladeSMP_Type()
)
restartBladeSMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartBladeSMP.setStatus("mandatory")


class _RestartBladeNMI_Type(Integer32):
    """Custom type restartBladeNMI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("execute", 1)
    )


_RestartBladeNMI_Type.__name__ = "Integer32"
_RestartBladeNMI_Object = MibTableColumn
restartBladeNMI = _RestartBladeNMI_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 6, 1, 1, 10),
    _RestartBladeNMI_Type()
)
restartBladeNMI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartBladeNMI.setStatus("mandatory")


class _RestartBladeClearNVRAM_Type(Integer32):
    """Custom type restartBladeClearNVRAM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("execute", 1)
    )


_RestartBladeClearNVRAM_Type.__name__ = "Integer32"
_RestartBladeClearNVRAM_Object = MibTableColumn
restartBladeClearNVRAM = _RestartBladeClearNVRAM_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 6, 1, 1, 11),
    _RestartBladeClearNVRAM_Type()
)
restartBladeClearNVRAM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartBladeClearNVRAM.setStatus("mandatory")


class _RestartBladeInvokeDiags_Type(Integer32):
    """Custom type restartBladeInvokeDiags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("execute", 1)
    )


_RestartBladeInvokeDiags_Type.__name__ = "Integer32"
_RestartBladeInvokeDiags_Object = MibTableColumn
restartBladeInvokeDiags = _RestartBladeInvokeDiags_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 6, 1, 1, 12),
    _RestartBladeInvokeDiags_Type()
)
restartBladeInvokeDiags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartBladeInvokeDiags.setStatus("mandatory")


class _RestartBladeInvokeDiagsFromDefaultBootList_Type(Integer32):
    """Custom type restartBladeInvokeDiagsFromDefaultBootList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("execute", 1)
    )


_RestartBladeInvokeDiagsFromDefaultBootList_Type.__name__ = "Integer32"
_RestartBladeInvokeDiagsFromDefaultBootList_Object = MibTableColumn
restartBladeInvokeDiagsFromDefaultBootList = _RestartBladeInvokeDiagsFromDefaultBootList_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 6, 1, 1, 13),
    _RestartBladeInvokeDiagsFromDefaultBootList_Type()
)
restartBladeInvokeDiagsFromDefaultBootList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartBladeInvokeDiagsFromDefaultBootList.setStatus("mandatory")
_BladeConfiguration_ObjectIdentity = ObjectIdentity
bladeConfiguration = _BladeConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 7)
)
_BladeConfigurationTable_Object = MibTable
bladeConfigurationTable = _BladeConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 7, 1)
)
if mibBuilder.loadTexts:
    bladeConfigurationTable.setStatus("mandatory")
_BladeConfigurationEntry_Object = MibTableRow
bladeConfigurationEntry = _BladeConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 7, 1, 1)
)
bladeConfigurationEntry.setIndexNames(
    (0, "BLADE-MIB", "configurationIndex"),
)
if mibBuilder.loadTexts:
    bladeConfigurationEntry.setStatus("mandatory")
_ConfigurationIndex_Type = Integer32
_ConfigurationIndex_Object = MibTableColumn
configurationIndex = _ConfigurationIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 7, 1, 1, 1),
    _ConfigurationIndex_Type()
)
configurationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configurationIndex.setStatus("mandatory")


class _ConfigurationBladeId_Type(Integer32):
    """Custom type configurationBladeId based on Integer32"""
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
        *(("blade1", 1),
          ("blade10", 10),
          ("blade11", 11),
          ("blade12", 12),
          ("blade13", 13),
          ("blade14", 14),
          ("blade2", 2),
          ("blade3", 3),
          ("blade4", 4),
          ("blade5", 5),
          ("blade6", 6),
          ("blade7", 7),
          ("blade8", 8),
          ("blade9", 9))
    )


_ConfigurationBladeId_Type.__name__ = "Integer32"
_ConfigurationBladeId_Object = MibTableColumn
configurationBladeId = _ConfigurationBladeId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 7, 1, 1, 2),
    _ConfigurationBladeId_Type()
)
configurationBladeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configurationBladeId.setStatus("mandatory")


class _ConfigurationBladeExists_Type(Integer32):
    """Custom type configurationBladeExists based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_ConfigurationBladeExists_Type.__name__ = "Integer32"
_ConfigurationBladeExists_Object = MibTableColumn
configurationBladeExists = _ConfigurationBladeExists_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 7, 1, 1, 3),
    _ConfigurationBladeExists_Type()
)
configurationBladeExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configurationBladeExists.setStatus("mandatory")


class _ConfigurationBladePowerState_Type(Integer32):
    """Custom type configurationBladePowerState based on Integer32"""
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


_ConfigurationBladePowerState_Type.__name__ = "Integer32"
_ConfigurationBladePowerState_Object = MibTableColumn
configurationBladePowerState = _ConfigurationBladePowerState_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 7, 1, 1, 4),
    _ConfigurationBladePowerState_Type()
)
configurationBladePowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configurationBladePowerState.setStatus("mandatory")
_ConfigurationBladeName_Type = OctetString
_ConfigurationBladeName_Object = MibTableColumn
configurationBladeName = _ConfigurationBladeName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 7, 1, 1, 5),
    _ConfigurationBladeName_Type()
)
configurationBladeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configurationBladeName.setStatus("mandatory")
_BladePowerManagementPolicy_ObjectIdentity = ObjectIdentity
bladePowerManagementPolicy = _BladePowerManagementPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 7, 2)
)


class _Powerdomain1Oversubscription_Type(Integer32):
    """Custom type powerdomain1Oversubscription based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("non-recoverable", 2),
          ("not-allowed", 0),
          ("recoverable", 1))
    )


_Powerdomain1Oversubscription_Type.__name__ = "Integer32"
_Powerdomain1Oversubscription_Object = MibScalar
powerdomain1Oversubscription = _Powerdomain1Oversubscription_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 7, 2, 1),
    _Powerdomain1Oversubscription_Type()
)
powerdomain1Oversubscription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerdomain1Oversubscription.setStatus("mandatory")


class _Powerdomain2Oversubscription_Type(Integer32):
    """Custom type powerdomain2Oversubscription based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("non-recoverable", 2),
          ("not-allowed", 0),
          ("recoverable", 1))
    )


_Powerdomain2Oversubscription_Type.__name__ = "Integer32"
_Powerdomain2Oversubscription_Object = MibScalar
powerdomain2Oversubscription = _Powerdomain2Oversubscription_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 7, 2, 2),
    _Powerdomain2Oversubscription_Type()
)
powerdomain2Oversubscription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerdomain2Oversubscription.setStatus("mandatory")


class _AcousticMode_Type(Integer32):
    """Custom type acousticMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AcousticMode_Type.__name__ = "Integer32"
_AcousticMode_Object = MibScalar
acousticMode = _AcousticMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 7, 2, 3),
    _AcousticMode_Type()
)
acousticMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acousticMode.setStatus("mandatory")
_BladeIPAddrRangeStart_Type = IpAddress
_BladeIPAddrRangeStart_Object = MibScalar
bladeIPAddrRangeStart = _BladeIPAddrRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 8),
    _BladeIPAddrRangeStart_Type()
)
bladeIPAddrRangeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bladeIPAddrRangeStart.setStatus("mandatory")
_BladeCapacityOnDemand_ObjectIdentity = ObjectIdentity
bladeCapacityOnDemand = _BladeCapacityOnDemand_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 9)
)
_BladeCapacityOnDemandTable_Object = MibTable
bladeCapacityOnDemandTable = _BladeCapacityOnDemandTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 9, 1)
)
if mibBuilder.loadTexts:
    bladeCapacityOnDemandTable.setStatus("mandatory")
_BladeCapacityOnDemandEntry_Object = MibTableRow
bladeCapacityOnDemandEntry = _BladeCapacityOnDemandEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 9, 1, 1)
)
bladeCapacityOnDemandEntry.setIndexNames(
    (0, "BLADE-MIB", "bladeCapacityOnDemandIndex"),
)
if mibBuilder.loadTexts:
    bladeCapacityOnDemandEntry.setStatus("mandatory")
_BladeCapacityOnDemandIndex_Type = Integer32
_BladeCapacityOnDemandIndex_Object = MibTableColumn
bladeCapacityOnDemandIndex = _BladeCapacityOnDemandIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 9, 1, 1, 1),
    _BladeCapacityOnDemandIndex_Type()
)
bladeCapacityOnDemandIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeCapacityOnDemandIndex.setStatus("mandatory")
_BladeCapacityOnDemandBladeName_Type = OctetString
_BladeCapacityOnDemandBladeName_Object = MibTableColumn
bladeCapacityOnDemandBladeName = _BladeCapacityOnDemandBladeName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 9, 1, 1, 2),
    _BladeCapacityOnDemandBladeName_Type()
)
bladeCapacityOnDemandBladeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeCapacityOnDemandBladeName.setStatus("mandatory")


class _BladeCapacityOnDemandState_Type(Integer32):
    """Custom type bladeCapacityOnDemandState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("none", 0),
          ("standby", 1))
    )


_BladeCapacityOnDemandState_Type.__name__ = "Integer32"
_BladeCapacityOnDemandState_Object = MibTableColumn
bladeCapacityOnDemandState = _BladeCapacityOnDemandState_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 9, 1, 1, 3),
    _BladeCapacityOnDemandState_Type()
)
bladeCapacityOnDemandState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bladeCapacityOnDemandState.setStatus("mandatory")
_BladeBootCountPowerOnTime_ObjectIdentity = ObjectIdentity
bladeBootCountPowerOnTime = _BladeBootCountPowerOnTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 10)
)
_BladeBootCountPowerOnTimeTable_Object = MibTable
bladeBootCountPowerOnTimeTable = _BladeBootCountPowerOnTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 10, 1)
)
if mibBuilder.loadTexts:
    bladeBootCountPowerOnTimeTable.setStatus("mandatory")
_BladeBootCountPowerOnTimeEntry_Object = MibTableRow
bladeBootCountPowerOnTimeEntry = _BladeBootCountPowerOnTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 10, 1, 1)
)
bladeBootCountPowerOnTimeEntry.setIndexNames(
    (0, "BLADE-MIB", "bootCountPowerOnTimeBladeIndex"),
)
if mibBuilder.loadTexts:
    bladeBootCountPowerOnTimeEntry.setStatus("mandatory")
_BootCountPowerOnTimeBladeIndex_Type = Integer32
_BootCountPowerOnTimeBladeIndex_Object = MibTableColumn
bootCountPowerOnTimeBladeIndex = _BootCountPowerOnTimeBladeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 10, 1, 1, 1),
    _BootCountPowerOnTimeBladeIndex_Type()
)
bootCountPowerOnTimeBladeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootCountPowerOnTimeBladeIndex.setStatus("mandatory")


class _BootCountPowerOnTimeBladeId_Type(Integer32):
    """Custom type bootCountPowerOnTimeBladeId based on Integer32"""
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
        *(("blade1", 1),
          ("blade10", 10),
          ("blade11", 11),
          ("blade12", 12),
          ("blade13", 13),
          ("blade14", 14),
          ("blade2", 2),
          ("blade3", 3),
          ("blade4", 4),
          ("blade5", 5),
          ("blade6", 6),
          ("blade7", 7),
          ("blade8", 8),
          ("blade9", 9))
    )


_BootCountPowerOnTimeBladeId_Type.__name__ = "Integer32"
_BootCountPowerOnTimeBladeId_Object = MibTableColumn
bootCountPowerOnTimeBladeId = _BootCountPowerOnTimeBladeId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 10, 1, 1, 2),
    _BootCountPowerOnTimeBladeId_Type()
)
bootCountPowerOnTimeBladeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootCountPowerOnTimeBladeId.setStatus("mandatory")
_BootCountPowerOnTimeBoots_Type = Integer32
_BootCountPowerOnTimeBoots_Object = MibTableColumn
bootCountPowerOnTimeBoots = _BootCountPowerOnTimeBoots_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 10, 1, 1, 3),
    _BootCountPowerOnTimeBoots_Type()
)
bootCountPowerOnTimeBoots.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootCountPowerOnTimeBoots.setStatus("mandatory")
_BootCountPowerOnTimeSecs_Type = Integer32
_BootCountPowerOnTimeSecs_Object = MibTableColumn
bootCountPowerOnTimeSecs = _BootCountPowerOnTimeSecs_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 1, 10, 1, 1, 4),
    _BootCountPowerOnTimeSecs_Type()
)
bootCountPowerOnTimeSecs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootCountPowerOnTimeSecs.setStatus("mandatory")
_SwitchModule_ObjectIdentity = ObjectIdentity
switchModule = _SwitchModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3)
)
_SwitchModuleControl_ObjectIdentity = ObjectIdentity
switchModuleControl = _SwitchModuleControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 1)
)
_SmControlTable_Object = MibTable
smControlTable = _SmControlTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 1, 1)
)
if mibBuilder.loadTexts:
    smControlTable.setStatus("mandatory")
_SmControlEntry_Object = MibTableRow
smControlEntry = _SmControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 1, 1, 1)
)
smControlEntry.setIndexNames(
    (0, "BLADE-MIB", "smControlIndex"),
)
if mibBuilder.loadTexts:
    smControlEntry.setStatus("mandatory")
_SmControlIndex_Type = Integer32
_SmControlIndex_Object = MibTableColumn
smControlIndex = _SmControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 1, 1, 1, 1),
    _SmControlIndex_Type()
)
smControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smControlIndex.setStatus("mandatory")


class _SwitchModuleControlId_Type(Integer32):
    """Custom type switchModuleControlId based on Integer32"""
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
        *(("module1", 1),
          ("module2", 2),
          ("module3", 3),
          ("module4", 4))
    )


_SwitchModuleControlId_Type.__name__ = "Integer32"
_SwitchModuleControlId_Object = MibTableColumn
switchModuleControlId = _SwitchModuleControlId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 1, 1, 1, 2),
    _SwitchModuleControlId_Type()
)
switchModuleControlId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchModuleControlId.setStatus("mandatory")


class _SmPostResultsAvailable_Type(Integer32):
    """Custom type smPostResultsAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SmPostResultsAvailable_Type.__name__ = "Integer32"
_SmPostResultsAvailable_Object = MibTableColumn
smPostResultsAvailable = _SmPostResultsAvailable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 1, 1, 1, 3),
    _SmPostResultsAvailable_Type()
)
smPostResultsAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smPostResultsAvailable.setStatus("mandatory")
_SmPostResultsValue_Type = OctetString
_SmPostResultsValue_Object = MibTableColumn
smPostResultsValue = _SmPostResultsValue_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 1, 1, 1, 4),
    _SmPostResultsValue_Type()
)
smPostResultsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smPostResultsValue.setStatus("mandatory")


class _SwitchModuleMemDiagEnableDisable_Type(Integer32):
    """Custom type switchModuleMemDiagEnableDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_SwitchModuleMemDiagEnableDisable_Type.__name__ = "Integer32"
_SwitchModuleMemDiagEnableDisable_Object = MibTableColumn
switchModuleMemDiagEnableDisable = _SwitchModuleMemDiagEnableDisable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 1, 1, 1, 5),
    _SwitchModuleMemDiagEnableDisable_Type()
)
switchModuleMemDiagEnableDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchModuleMemDiagEnableDisable.setStatus("mandatory")


class _SmCfgCtrlEnableDisable_Type(Integer32):
    """Custom type smCfgCtrlEnableDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_SmCfgCtrlEnableDisable_Type.__name__ = "Integer32"
_SmCfgCtrlEnableDisable_Object = MibTableColumn
smCfgCtrlEnableDisable = _SmCfgCtrlEnableDisable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 1, 1, 1, 6),
    _SmCfgCtrlEnableDisable_Type()
)
smCfgCtrlEnableDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smCfgCtrlEnableDisable.setStatus("mandatory")


class _SmExtEthPortsEnableDisable_Type(Integer32):
    """Custom type smExtEthPortsEnableDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SmExtEthPortsEnableDisable_Type.__name__ = "Integer32"
_SmExtEthPortsEnableDisable_Object = MibTableColumn
smExtEthPortsEnableDisable = _SmExtEthPortsEnableDisable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 1, 1, 1, 7),
    _SmExtEthPortsEnableDisable_Type()
)
smExtEthPortsEnableDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smExtEthPortsEnableDisable.setStatus("mandatory")


class _SwitchPingRequest_Type(Integer32):
    """Custom type switchPingRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("execute", 1)
    )


_SwitchPingRequest_Type.__name__ = "Integer32"
_SwitchPingRequest_Object = MibTableColumn
switchPingRequest = _SwitchPingRequest_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 1, 1, 1, 8),
    _SwitchPingRequest_Type()
)
switchPingRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchPingRequest.setStatus("mandatory")


class _SmCfgCtrlOnResetEnableDisable_Type(Integer32):
    """Custom type smCfgCtrlOnResetEnableDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_SmCfgCtrlOnResetEnableDisable_Type.__name__ = "Integer32"
_SmCfgCtrlOnResetEnableDisable_Object = MibTableColumn
smCfgCtrlOnResetEnableDisable = _SmCfgCtrlOnResetEnableDisable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 1, 1, 1, 9),
    _SmCfgCtrlOnResetEnableDisable_Type()
)
smCfgCtrlOnResetEnableDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smCfgCtrlOnResetEnableDisable.setStatus("mandatory")


class _SmHealthState_Type(Integer32):
    """Custom type smHealthState based on Integer32"""
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
        *(("bad", 3),
          ("good", 1),
          ("unknown", 0),
          ("warning", 2))
    )


_SmHealthState_Type.__name__ = "Integer32"
_SmHealthState_Object = MibTableColumn
smHealthState = _SmHealthState_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 1, 1, 1, 15),
    _SmHealthState_Type()
)
smHealthState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smHealthState.setStatus("mandatory")
_SmPowerRestartTable_Object = MibTable
smPowerRestartTable = _SmPowerRestartTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 1, 7)
)
if mibBuilder.loadTexts:
    smPowerRestartTable.setStatus("mandatory")
_SmPowerRestartEntry_Object = MibTableRow
smPowerRestartEntry = _SmPowerRestartEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 1, 7, 1)
)
smPowerRestartEntry.setIndexNames(
    (0, "BLADE-MIB", "smPowerRestartIndex"),
)
if mibBuilder.loadTexts:
    smPowerRestartEntry.setStatus("mandatory")
_SmPowerRestartIndex_Type = Integer32
_SmPowerRestartIndex_Object = MibTableColumn
smPowerRestartIndex = _SmPowerRestartIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 1, 7, 1, 1),
    _SmPowerRestartIndex_Type()
)
smPowerRestartIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smPowerRestartIndex.setStatus("mandatory")


class _SmPowerRestartId_Type(Integer32):
    """Custom type smPowerRestartId based on Integer32"""
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
        *(("module1", 1),
          ("module2", 2),
          ("module3", 3),
          ("module4", 4))
    )


_SmPowerRestartId_Type.__name__ = "Integer32"
_SmPowerRestartId_Object = MibTableColumn
smPowerRestartId = _SmPowerRestartId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 1, 7, 1, 2),
    _SmPowerRestartId_Type()
)
smPowerRestartId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smPowerRestartId.setStatus("mandatory")


class _SmSwitchExists_Type(Integer32):
    """Custom type smSwitchExists based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SmSwitchExists_Type.__name__ = "Integer32"
_SmSwitchExists_Object = MibTableColumn
smSwitchExists = _SmSwitchExists_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 1, 7, 1, 3),
    _SmSwitchExists_Type()
)
smSwitchExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSwitchExists.setStatus("mandatory")


class _SmSwitchType_Type(Integer32):
    """Custom type smSwitchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("fibre", 2),
          ("opm", 3),
          ("serialCM", 4),
          ("unknown", 0))
    )


_SmSwitchType_Type.__name__ = "Integer32"
_SmSwitchType_Object = MibTableColumn
smSwitchType = _SmSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 1, 7, 1, 4),
    _SmSwitchType_Type()
)
smSwitchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSwitchType.setStatus("mandatory")
_SmMACAddress_Type = OctetString
_SmMACAddress_Object = MibTableColumn
smMACAddress = _SmMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 1, 7, 1, 5),
    _SmMACAddress_Type()
)
smMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smMACAddress.setStatus("mandatory")
_SmIPAddress_Type = IpAddress
_SmIPAddress_Object = MibTableColumn
smIPAddress = _SmIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 1, 7, 1, 6),
    _SmIPAddress_Type()
)
smIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smIPAddress.setStatus("mandatory")


class _SwitchModulePowerOnOff_Type(Integer32):
    """Custom type switchModulePowerOnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("poweroff", 0),
          ("poweron", 1))
    )


_SwitchModulePowerOnOff_Type.__name__ = "Integer32"
_SwitchModulePowerOnOff_Object = MibTableColumn
switchModulePowerOnOff = _SwitchModulePowerOnOff_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 1, 7, 1, 7),
    _SwitchModulePowerOnOff_Type()
)
switchModulePowerOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchModulePowerOnOff.setStatus("mandatory")


class _SmReset_Type(Integer32):
    """Custom type smReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("execute", 1)
    )


_SmReset_Type.__name__ = "Integer32"
_SmReset_Object = MibTableColumn
smReset = _SmReset_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 1, 7, 1, 8),
    _SmReset_Type()
)
smReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smReset.setStatus("mandatory")


class _SmResetToDefault_Type(Integer32):
    """Custom type smResetToDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("execute", 1)
    )


_SmResetToDefault_Type.__name__ = "Integer32"
_SmResetToDefault_Object = MibTableColumn
smResetToDefault = _SmResetToDefault_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 1, 7, 1, 9),
    _SmResetToDefault_Type()
)
smResetToDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smResetToDefault.setStatus("mandatory")


class _SmRestartAndRunStdDiag_Type(Integer32):
    """Custom type smRestartAndRunStdDiag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("execute", 1)
    )


_SmRestartAndRunStdDiag_Type.__name__ = "Integer32"
_SmRestartAndRunStdDiag_Object = MibTableColumn
smRestartAndRunStdDiag = _SmRestartAndRunStdDiag_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 1, 7, 1, 10),
    _SmRestartAndRunStdDiag_Type()
)
smRestartAndRunStdDiag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smRestartAndRunStdDiag.setStatus("mandatory")


class _SmRestartAndRunExtDiag_Type(Integer32):
    """Custom type smRestartAndRunExtDiag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("execute", 1)
    )


_SmRestartAndRunExtDiag_Type.__name__ = "Integer32"
_SmRestartAndRunExtDiag_Object = MibTableColumn
smRestartAndRunExtDiag = _SmRestartAndRunExtDiag_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 1, 7, 1, 11),
    _SmRestartAndRunExtDiag_Type()
)
smRestartAndRunExtDiag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smRestartAndRunExtDiag.setStatus("mandatory")


class _SmRestartAndRunFullDiag_Type(Integer32):
    """Custom type smRestartAndRunFullDiag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("execute", 1)
    )


_SmRestartAndRunFullDiag_Type.__name__ = "Integer32"
_SmRestartAndRunFullDiag_Object = MibTableColumn
smRestartAndRunFullDiag = _SmRestartAndRunFullDiag_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 1, 7, 1, 12),
    _SmRestartAndRunFullDiag_Type()
)
smRestartAndRunFullDiag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smRestartAndRunFullDiag.setStatus("mandatory")
_SwitchModuleConfig_ObjectIdentity = ObjectIdentity
switchModuleConfig = _SwitchModuleConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 2)
)
_SwitchMgmtNetworkCfg_ObjectIdentity = ObjectIdentity
switchMgmtNetworkCfg = _SwitchMgmtNetworkCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 2, 1)
)
_SwitchCurrentNwCfg_ObjectIdentity = ObjectIdentity
switchCurrentNwCfg = _SwitchCurrentNwCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 2, 1, 1)
)
_SmCurrentIPInfoTable_Object = MibTable
smCurrentIPInfoTable = _SmCurrentIPInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    smCurrentIPInfoTable.setStatus("mandatory")
_SmCurrentIPInfoEntry_Object = MibTableRow
smCurrentIPInfoEntry = _SmCurrentIPInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 2, 1, 1, 1, 1)
)
smCurrentIPInfoEntry.setIndexNames(
    (0, "BLADE-MIB", "smCurrentIPInfoIndex"),
)
if mibBuilder.loadTexts:
    smCurrentIPInfoEntry.setStatus("mandatory")
_SmCurrentIPInfoIndex_Type = Integer32
_SmCurrentIPInfoIndex_Object = MibTableColumn
smCurrentIPInfoIndex = _SmCurrentIPInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 2, 1, 1, 1, 1, 1),
    _SmCurrentIPInfoIndex_Type()
)
smCurrentIPInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smCurrentIPInfoIndex.setStatus("mandatory")


class _SmCurrentIPInfoId_Type(Integer32):
    """Custom type smCurrentIPInfoId based on Integer32"""
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
        *(("module1", 1),
          ("module2", 2),
          ("module3", 3),
          ("module4", 4))
    )


_SmCurrentIPInfoId_Type.__name__ = "Integer32"
_SmCurrentIPInfoId_Object = MibTableColumn
smCurrentIPInfoId = _SmCurrentIPInfoId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 2, 1, 1, 1, 1, 2),
    _SmCurrentIPInfoId_Type()
)
smCurrentIPInfoId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smCurrentIPInfoId.setStatus("mandatory")


class _SmCurrentIPInfoExists_Type(Integer32):
    """Custom type smCurrentIPInfoExists based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SmCurrentIPInfoExists_Type.__name__ = "Integer32"
_SmCurrentIPInfoExists_Object = MibTableColumn
smCurrentIPInfoExists = _SmCurrentIPInfoExists_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 2, 1, 1, 1, 1, 3),
    _SmCurrentIPInfoExists_Type()
)
smCurrentIPInfoExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smCurrentIPInfoExists.setStatus("mandatory")


class _SmCurrentIPInfoPowerState_Type(Integer32):
    """Custom type smCurrentIPInfoPowerState based on Integer32"""
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


_SmCurrentIPInfoPowerState_Type.__name__ = "Integer32"
_SmCurrentIPInfoPowerState_Object = MibTableColumn
smCurrentIPInfoPowerState = _SmCurrentIPInfoPowerState_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 2, 1, 1, 1, 1, 4),
    _SmCurrentIPInfoPowerState_Type()
)
smCurrentIPInfoPowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smCurrentIPInfoPowerState.setStatus("mandatory")
_SmCurrentIPAddr_Type = IpAddress
_SmCurrentIPAddr_Object = MibTableColumn
smCurrentIPAddr = _SmCurrentIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 2, 1, 1, 1, 1, 6),
    _SmCurrentIPAddr_Type()
)
smCurrentIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smCurrentIPAddr.setStatus("mandatory")
_SmCurrentSubnetMask_Type = IpAddress
_SmCurrentSubnetMask_Object = MibTableColumn
smCurrentSubnetMask = _SmCurrentSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 2, 1, 1, 1, 1, 7),
    _SmCurrentSubnetMask_Type()
)
smCurrentSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smCurrentSubnetMask.setStatus("mandatory")
_SmCurrentGateway_Type = IpAddress
_SmCurrentGateway_Object = MibTableColumn
smCurrentGateway = _SmCurrentGateway_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 2, 1, 1, 1, 1, 8),
    _SmCurrentGateway_Type()
)
smCurrentGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smCurrentGateway.setStatus("mandatory")


class _SmCurrentIPConfigMethod_Type(Integer32):
    """Custom type smCurrentIPConfigMethod based on Integer32"""
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
        *(("bootp", 3),
          ("dhcp", 2),
          ("static", 1),
          ("unknown", 0))
    )


_SmCurrentIPConfigMethod_Type.__name__ = "Integer32"
_SmCurrentIPConfigMethod_Object = MibTableColumn
smCurrentIPConfigMethod = _SmCurrentIPConfigMethod_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 2, 1, 1, 1, 1, 9),
    _SmCurrentIPConfigMethod_Type()
)
smCurrentIPConfigMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smCurrentIPConfigMethod.setStatus("mandatory")
_SwitchNewNwCfg_ObjectIdentity = ObjectIdentity
switchNewNwCfg = _SwitchNewNwCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 2, 1, 2)
)
_SmNewIPInfoTable_Object = MibTable
smNewIPInfoTable = _SmNewIPInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    smNewIPInfoTable.setStatus("mandatory")
_SmNewIPInfoEntry_Object = MibTableRow
smNewIPInfoEntry = _SmNewIPInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 2, 1, 2, 1, 1)
)
smNewIPInfoEntry.setIndexNames(
    (0, "BLADE-MIB", "smNewIPInfoIndex"),
)
if mibBuilder.loadTexts:
    smNewIPInfoEntry.setStatus("mandatory")
_SmNewIPInfoIndex_Type = Integer32
_SmNewIPInfoIndex_Object = MibTableColumn
smNewIPInfoIndex = _SmNewIPInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 2, 1, 2, 1, 1, 1),
    _SmNewIPInfoIndex_Type()
)
smNewIPInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smNewIPInfoIndex.setStatus("mandatory")


class _SmNewIPInfoId_Type(Integer32):
    """Custom type smNewIPInfoId based on Integer32"""
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
        *(("module1", 1),
          ("module2", 2),
          ("module3", 3),
          ("module4", 4))
    )


_SmNewIPInfoId_Type.__name__ = "Integer32"
_SmNewIPInfoId_Object = MibTableColumn
smNewIPInfoId = _SmNewIPInfoId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 2, 1, 2, 1, 1, 2),
    _SmNewIPInfoId_Type()
)
smNewIPInfoId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smNewIPInfoId.setStatus("mandatory")


class _SmNewIPInfoExists_Type(Integer32):
    """Custom type smNewIPInfoExists based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SmNewIPInfoExists_Type.__name__ = "Integer32"
_SmNewIPInfoExists_Object = MibTableColumn
smNewIPInfoExists = _SmNewIPInfoExists_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 2, 1, 2, 1, 1, 3),
    _SmNewIPInfoExists_Type()
)
smNewIPInfoExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smNewIPInfoExists.setStatus("mandatory")


class _SmNewIPInfoPowerState_Type(Integer32):
    """Custom type smNewIPInfoPowerState based on Integer32"""
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


_SmNewIPInfoPowerState_Type.__name__ = "Integer32"
_SmNewIPInfoPowerState_Object = MibTableColumn
smNewIPInfoPowerState = _SmNewIPInfoPowerState_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 2, 1, 2, 1, 1, 4),
    _SmNewIPInfoPowerState_Type()
)
smNewIPInfoPowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smNewIPInfoPowerState.setStatus("mandatory")
_SmNewIPAddr_Type = IpAddress
_SmNewIPAddr_Object = MibTableColumn
smNewIPAddr = _SmNewIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 2, 1, 2, 1, 1, 6),
    _SmNewIPAddr_Type()
)
smNewIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smNewIPAddr.setStatus("mandatory")
_SmNewSubnetMask_Type = IpAddress
_SmNewSubnetMask_Object = MibTableColumn
smNewSubnetMask = _SmNewSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 2, 1, 2, 1, 1, 7),
    _SmNewSubnetMask_Type()
)
smNewSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smNewSubnetMask.setStatus("mandatory")
_SmNewGateway_Type = IpAddress
_SmNewGateway_Object = MibTableColumn
smNewGateway = _SmNewGateway_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 2, 1, 2, 1, 1, 8),
    _SmNewGateway_Type()
)
smNewGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smNewGateway.setStatus("mandatory")


class _SmNewIPConfigMethod_Type(Integer32):
    """Custom type smNewIPConfigMethod based on Integer32"""
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
        *(("bootp", 3),
          ("dhcp", 2),
          ("static", 1),
          ("unknown", 0))
    )


_SmNewIPConfigMethod_Type.__name__ = "Integer32"
_SmNewIPConfigMethod_Object = MibTableColumn
smNewIPConfigMethod = _SmNewIPConfigMethod_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 2, 1, 2, 1, 1, 9),
    _SmNewIPConfigMethod_Type()
)
smNewIPConfigMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smNewIPConfigMethod.setStatus("mandatory")


class _SmNewIPConfigEnableDisable_Type(Integer32):
    """Custom type smNewIPConfigEnableDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SmNewIPConfigEnableDisable_Type.__name__ = "Integer32"
_SmNewIPConfigEnableDisable_Object = MibTableColumn
smNewIPConfigEnableDisable = _SmNewIPConfigEnableDisable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 3, 2, 1, 2, 1, 1, 10),
    _SmNewIPConfigEnableDisable_Type()
)
smNewIPConfigEnableDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smNewIPConfigEnableDisable.setStatus("mandatory")
_ChassisTopology_ObjectIdentity = ObjectIdentity
chassisTopology = _ChassisTopology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 4)
)
_ChassisResponseVersion_Type = Integer32
_ChassisResponseVersion_Object = MibScalar
chassisResponseVersion = _ChassisResponseVersion_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 4, 1),
    _ChassisResponseVersion_Type()
)
chassisResponseVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisResponseVersion.setStatus("mandatory")


class _ChassisFlags_Type(Integer32):
    """Custom type chassisFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rackOrStandAlone", 0),
          ("serverBlade", 1))
    )


_ChassisFlags_Type.__name__ = "Integer32"
_ChassisFlags_Object = MibScalar
chassisFlags = _ChassisFlags_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 4, 2),
    _ChassisFlags_Type()
)
chassisFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisFlags.setStatus("mandatory")
_ChassisName_Type = OctetString
_ChassisName_Object = MibScalar
chassisName = _ChassisName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 4, 3),
    _ChassisName_Type()
)
chassisName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisName.setStatus("mandatory")
_ChassisNoOfPBsSupported_Type = Integer32
_ChassisNoOfPBsSupported_Object = MibScalar
chassisNoOfPBsSupported = _ChassisNoOfPBsSupported_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 4, 19),
    _ChassisNoOfPBsSupported_Type()
)
chassisNoOfPBsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisNoOfPBsSupported.setStatus("mandatory")
_ChassisNoOfSMsSupported_Type = Integer32
_ChassisNoOfSMsSupported_Object = MibScalar
chassisNoOfSMsSupported = _ChassisNoOfSMsSupported_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 4, 20),
    _ChassisNoOfSMsSupported_Type()
)
chassisNoOfSMsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisNoOfSMsSupported.setStatus("mandatory")
_ChassisNoOfMMsSupported_Type = Integer32
_ChassisNoOfMMsSupported_Object = MibScalar
chassisNoOfMMsSupported = _ChassisNoOfMMsSupported_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 4, 21),
    _ChassisNoOfMMsSupported_Type()
)
chassisNoOfMMsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisNoOfMMsSupported.setStatus("mandatory")
_ChassisNoOfPMsSupported_Type = Integer32
_ChassisNoOfPMsSupported_Object = MibScalar
chassisNoOfPMsSupported = _ChassisNoOfPMsSupported_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 4, 22),
    _ChassisNoOfPMsSupported_Type()
)
chassisNoOfPMsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisNoOfPMsSupported.setStatus("mandatory")
_ChassisNoOfMTsSupported_Type = Integer32
_ChassisNoOfMTsSupported_Object = MibScalar
chassisNoOfMTsSupported = _ChassisNoOfMTsSupported_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 4, 23),
    _ChassisNoOfMTsSupported_Type()
)
chassisNoOfMTsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisNoOfMTsSupported.setStatus("mandatory")
_ChassisNoOfBlowersSupported_Type = Integer32
_ChassisNoOfBlowersSupported_Object = MibScalar
chassisNoOfBlowersSupported = _ChassisNoOfBlowersSupported_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 4, 24),
    _ChassisNoOfBlowersSupported_Type()
)
chassisNoOfBlowersSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisNoOfBlowersSupported.setStatus("mandatory")
_ChassisPBsInstalled_Type = OctetString
_ChassisPBsInstalled_Object = MibScalar
chassisPBsInstalled = _ChassisPBsInstalled_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 4, 25),
    _ChassisPBsInstalled_Type()
)
chassisPBsInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPBsInstalled.setStatus("mandatory")
_ChassisSMsInstalled_Type = OctetString
_ChassisSMsInstalled_Object = MibScalar
chassisSMsInstalled = _ChassisSMsInstalled_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 4, 29),
    _ChassisSMsInstalled_Type()
)
chassisSMsInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSMsInstalled.setStatus("mandatory")
_ChassisMMsInstalled_Type = OctetString
_ChassisMMsInstalled_Object = MibScalar
chassisMMsInstalled = _ChassisMMsInstalled_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 4, 30),
    _ChassisMMsInstalled_Type()
)
chassisMMsInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisMMsInstalled.setStatus("mandatory")
_ChassisPMsInstalled_Type = OctetString
_ChassisPMsInstalled_Object = MibScalar
chassisPMsInstalled = _ChassisPMsInstalled_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 4, 31),
    _ChassisPMsInstalled_Type()
)
chassisPMsInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPMsInstalled.setStatus("mandatory")


class _ChassisMTInstalled_Type(Integer32):
    """Custom type chassisMTInstalled based on Integer32"""
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


_ChassisMTInstalled_Type.__name__ = "Integer32"
_ChassisMTInstalled_Object = MibScalar
chassisMTInstalled = _ChassisMTInstalled_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 4, 32),
    _ChassisMTInstalled_Type()
)
chassisMTInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisMTInstalled.setStatus("mandatory")
_ChassisBlowersInstalled_Type = OctetString
_ChassisBlowersInstalled_Object = MibScalar
chassisBlowersInstalled = _ChassisBlowersInstalled_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 4, 33),
    _ChassisBlowersInstalled_Type()
)
chassisBlowersInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisBlowersInstalled.setStatus("mandatory")
_ChassisActiveMM_Type = Integer32
_ChassisActiveMM_Object = MibScalar
chassisActiveMM = _ChassisActiveMM_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 4, 34),
    _ChassisActiveMM_Type()
)
chassisActiveMM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisActiveMM.setStatus("mandatory")
_ChassisKVMOwner_Type = Integer32
_ChassisKVMOwner_Object = MibScalar
chassisKVMOwner = _ChassisKVMOwner_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 4, 35),
    _ChassisKVMOwner_Type()
)
chassisKVMOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisKVMOwner.setStatus("mandatory")
_ChassisMediaTrayOwner_Type = Integer32
_ChassisMediaTrayOwner_Object = MibScalar
chassisMediaTrayOwner = _ChassisMediaTrayOwner_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 4, 36),
    _ChassisMediaTrayOwner_Type()
)
chassisMediaTrayOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisMediaTrayOwner.setStatus("mandatory")
_ManagementModule_ObjectIdentity = ObjectIdentity
managementModule = _ManagementModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 5)
)
_MmStatusTable_Object = MibTable
mmStatusTable = _MmStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 5, 1)
)
if mibBuilder.loadTexts:
    mmStatusTable.setStatus("mandatory")
_MmStatusEntry_Object = MibTableRow
mmStatusEntry = _MmStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 5, 1, 1)
)
mmStatusEntry.setIndexNames(
    (0, "BLADE-MIB", "mmStatusIndex"),
)
if mibBuilder.loadTexts:
    mmStatusEntry.setStatus("mandatory")
_MmStatusIndex_Type = Integer32
_MmStatusIndex_Object = MibTableColumn
mmStatusIndex = _MmStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 5, 1, 1, 1),
    _MmStatusIndex_Type()
)
mmStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmStatusIndex.setStatus("mandatory")


class _MmPresent_Type(Integer32):
    """Custom type mmPresent based on Integer32"""
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


_MmPresent_Type.__name__ = "Integer32"
_MmPresent_Object = MibTableColumn
mmPresent = _MmPresent_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 5, 1, 1, 2),
    _MmPresent_Type()
)
mmPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmPresent.setStatus("mandatory")
_MmExtIpAddress_Type = IpAddress
_MmExtIpAddress_Object = MibTableColumn
mmExtIpAddress = _MmExtIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 5, 1, 1, 3),
    _MmExtIpAddress_Type()
)
mmExtIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmExtIpAddress.setStatus("mandatory")


class _MmPrimary_Type(Integer32):
    """Custom type mmPrimary based on Integer32"""
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


_MmPrimary_Type.__name__ = "Integer32"
_MmPrimary_Object = MibTableColumn
mmPrimary = _MmPrimary_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 5, 1, 1, 4),
    _MmPrimary_Type()
)
mmPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmPrimary.setStatus("mandatory")
_FirmwareUpdate_ObjectIdentity = ObjectIdentity
firmwareUpdate = _FirmwareUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 9)
)


class _FirmwareUpdateTarget_Type(Integer32):
    """Custom type firmwareUpdateTarget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4,
              5,
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("blade1", 10),
          ("blade10", 19),
          ("blade11", 20),
          ("blade12", 21),
          ("blade13", 22),
          ("blade14", 23),
          ("blade2", 11),
          ("blade3", 12),
          ("blade4", 13),
          ("blade5", 14),
          ("blade6", 15),
          ("blade7", 16),
          ("blade8", 17),
          ("blade9", 18),
          ("managementModule", 0),
          ("switchModule1", 2),
          ("switchModule2", 3),
          ("switchModule3", 4),
          ("switchModule4", 5),
          ("unknown", 255))
    )


_FirmwareUpdateTarget_Type.__name__ = "Integer32"
_FirmwareUpdateTarget_Object = MibScalar
firmwareUpdateTarget = _FirmwareUpdateTarget_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 9, 1),
    _FirmwareUpdateTarget_Type()
)
firmwareUpdateTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firmwareUpdateTarget.setStatus("mandatory")


class _FirmwareUpdateTftpServer_Type(OctetString):
    """Custom type firmwareUpdateTftpServer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_FirmwareUpdateTftpServer_Type.__name__ = "OctetString"
_FirmwareUpdateTftpServer_Object = MibScalar
firmwareUpdateTftpServer = _FirmwareUpdateTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 9, 2),
    _FirmwareUpdateTftpServer_Type()
)
firmwareUpdateTftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firmwareUpdateTftpServer.setStatus("mandatory")


class _FirmwareUpdateFileName_Type(OctetString):
    """Custom type firmwareUpdateFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_FirmwareUpdateFileName_Type.__name__ = "OctetString"
_FirmwareUpdateFileName_Object = MibScalar
firmwareUpdateFileName = _FirmwareUpdateFileName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 9, 3),
    _FirmwareUpdateFileName_Type()
)
firmwareUpdateFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firmwareUpdateFileName.setStatus("mandatory")


class _FirmwareUpdateStart_Type(Integer32):
    """Custom type firmwareUpdateStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("execute", 1)
    )


_FirmwareUpdateStart_Type.__name__ = "Integer32"
_FirmwareUpdateStart_Object = MibScalar
firmwareUpdateStart = _FirmwareUpdateStart_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 9, 4),
    _FirmwareUpdateStart_Type()
)
firmwareUpdateStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firmwareUpdateStart.setStatus("mandatory")
_FirmwareUpdateStatus_Type = OctetString
_FirmwareUpdateStatus_Object = MibScalar
firmwareUpdateStatus = _FirmwareUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 9, 5),
    _FirmwareUpdateStatus_Type()
)
firmwareUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareUpdateStatus.setStatus("mandatory")
_IpmiManagement_ObjectIdentity = ObjectIdentity
ipmiManagement = _IpmiManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 20)
)


class _IpmiEnabled_Type(Integer32):
    """Custom type ipmiEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ipmiDisabled", 0),
          ("ipmiEnabled", 1))
    )


_IpmiEnabled_Type.__name__ = "Integer32"
_IpmiEnabled_Object = MibScalar
ipmiEnabled = _IpmiEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 2, 22, 20, 1),
    _IpmiEnabled_Type()
)
ipmiEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmiEnabled.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BLADE-MIB",
    **{"ibm": ibm,
       "ibmAgents": ibmAgents,
       "netfinitySupportProcessorAgent": netfinitySupportProcessorAgent,
       "bladeCenterSnmpMIB": bladeCenterSnmpMIB,
       "monitors": monitors,
       "temperature": temperature,
       "planarTemp": planarTemp,
       "mmTemp": mmTemp,
       "cpuXTemp": cpuXTemp,
       "ambientTemp": ambientTemp,
       "frontPanelTemp": frontPanelTemp,
       "voltage": voltage,
       "planarVolt": planarVolt,
       "plus5Volt": plus5Volt,
       "plus3Pt3Volt": plus3Pt3Volt,
       "plus12Volt": plus12Volt,
       "minus5Volt": minus5Volt,
       "plus2Pt5Volt": plus2Pt5Volt,
       "plus1Pt8Volt": plus1Pt8Volt,
       "blowers": blowers,
       "blower1speed": blower1speed,
       "blower2speed": blower2speed,
       "blower1State": blower1State,
       "blower2State": blower2State,
       "powerModuleHealth": powerModuleHealth,
       "powerModuleHealthTable": powerModuleHealthTable,
       "powerModuleHealthEntry": powerModuleHealthEntry,
       "powerModuleIndex": powerModuleIndex,
       "powerModuleExists": powerModuleExists,
       "powerModuleState": powerModuleState,
       "powerModuleDetails": powerModuleDetails,
       "spStatus": spStatus,
       "mmBistAndChassisStatus": mmBistAndChassisStatus,
       "bistSdram": bistSdram,
       "bistRs485Port1": bistRs485Port1,
       "bistRs485Port2": bistRs485Port2,
       "bistNvram": bistNvram,
       "bistRtc": bistRtc,
       "bistLocalI2CBus": bistLocalI2CBus,
       "bistPrimaryMainAppFlashImage": bistPrimaryMainAppFlashImage,
       "bistSecondaryMainAppFlashImage": bistSecondaryMainAppFlashImage,
       "bistBootRomFlashImage": bistBootRomFlashImage,
       "bistEthernetPort1": bistEthernetPort1,
       "bistEthernetPort2": bistEthernetPort2,
       "bistInternalPCIBus": bistInternalPCIBus,
       "bistExternalI2CDevices": bistExternalI2CDevices,
       "bistUSBController": bistUSBController,
       "bistVideoCompressorBoard": bistVideoCompressorBoard,
       "bistPrimaryBus": bistPrimaryBus,
       "bistInternalEthernetSwitch": bistInternalEthernetSwitch,
       "bistBladesInstalled": bistBladesInstalled,
       "bistBladesCommunicating": bistBladesCommunicating,
       "bistBlowersInstalled": bistBlowersInstalled,
       "bistBlowersFunctional": bistBlowersFunctional,
       "bistMediaTrayInstalled": bistMediaTrayInstalled,
       "bistMediaTrayCommunicating": bistMediaTrayCommunicating,
       "bistPowerModulesInstalled": bistPowerModulesInstalled,
       "bistPowerModulesFunctional": bistPowerModulesFunctional,
       "bistSwitchModulesInstalled": bistSwitchModulesInstalled,
       "bistSwitchModulesCommunicating": bistSwitchModulesCommunicating,
       "systemHealth": systemHealth,
       "systemHealthStat": systemHealthStat,
       "systemHealthSummaryTable": systemHealthSummaryTable,
       "systemHealthSummaryEntry": systemHealthSummaryEntry,
       "systemHealthSummaryIndex": systemHealthSummaryIndex,
       "systemHealthSummarySeverity": systemHealthSummarySeverity,
       "systemHealthSummaryDescription": systemHealthSummaryDescription,
       "leds": leds,
       "frontPanelLEDs": frontPanelLEDs,
       "systemErrorLED": systemErrorLED,
       "informationLED": informationLED,
       "temperatureLED": temperatureLED,
       "identityLED": identityLED,
       "bladeLEDs": bladeLEDs,
       "bladeLEDsTable": bladeLEDsTable,
       "bladeLEDsEntry": bladeLEDsEntry,
       "ledBladeIndex": ledBladeIndex,
       "ledBladeId": ledBladeId,
       "ledBladeExists": ledBladeExists,
       "ledBladePowerState": ledBladePowerState,
       "ledBladeHealthState": ledBladeHealthState,
       "ledBladeName": ledBladeName,
       "ledBladeSystemError": ledBladeSystemError,
       "ledBladeInformation": ledBladeInformation,
       "ledBladeKVM": ledBladeKVM,
       "ledBladeMediaTray": ledBladeMediaTray,
       "ledBladeIdentity": ledBladeIdentity,
       "telcoPanelLEDs": telcoPanelLEDs,
       "criticalLED": criticalLED,
       "majorLED": majorLED,
       "minorLED": minorLED,
       "telcoIdentityLED": telcoIdentityLED,
       "telcoColorSel": telcoColorSel,
       "criticalityAssertionMode": criticalityAssertionMode,
       "smLEDs": smLEDs,
       "smLEDsTable": smLEDsTable,
       "smLEDsEntry": smLEDsEntry,
       "ledSMIndex": ledSMIndex,
       "ledSMLEDs": ledSMLEDs,
       "telcoSystemHealth": telcoSystemHealth,
       "telcoSystemHealthStat": telcoSystemHealthStat,
       "telcoSystemHealthSummaryTable": telcoSystemHealthSummaryTable,
       "telcoSystemHealthSummaryEntry": telcoSystemHealthSummaryEntry,
       "telcoSystemHealthSummaryIndex": telcoSystemHealthSummaryIndex,
       "telcoSystemHealthSummarySeverity": telcoSystemHealthSummarySeverity,
       "telcoSystemHealthSummaryDescription": telcoSystemHealthSummaryDescription,
       "telcoSystemHealthSummaryEventName": telcoSystemHealthSummaryEventName,
       "telcoSystemHealthSummaryEventKeyID": telcoSystemHealthSummaryEventKeyID,
       "telcoSystemHealthSummaryAcknowledge": telcoSystemHealthSummaryAcknowledge,
       "fuelGauge": fuelGauge,
       "fuelGaugeInformation": fuelGaugeInformation,
       "fuelGaugeTable": fuelGaugeTable,
       "fuelGaugeEntry": fuelGaugeEntry,
       "fuelGaugeIndex": fuelGaugeIndex,
       "fuelGaugePowerDomainNumber": fuelGaugePowerDomainNumber,
       "fuelGaugeStatus": fuelGaugeStatus,
       "fuelGaugeFirstPowerModule": fuelGaugeFirstPowerModule,
       "fuelGaugeSecondPowerModule": fuelGaugeSecondPowerModule,
       "fuelGaugePowerManagementPolicySetting": fuelGaugePowerManagementPolicySetting,
       "fuelGaugeTotalPower": fuelGaugeTotalPower,
       "fuelGaugeReservedPower": fuelGaugeReservedPower,
       "fuelGaugeRemainingPower": fuelGaugeRemainingPower,
       "fuelGaugePowerInUsed": fuelGaugePowerInUsed,
       "powerDomain1": powerDomain1,
       "powerDomain1Table": powerDomain1Table,
       "powerDomain1Entry": powerDomain1Entry,
       "pd1Index": pd1Index,
       "pd1BayNumber": pd1BayNumber,
       "pd1BladePrimarySlot": pd1BladePrimarySlot,
       "pd1ModuleStatus": pd1ModuleStatus,
       "pd1ModuleName": pd1ModuleName,
       "pd1ModuleState": pd1ModuleState,
       "pd1ModuleAllocatedPowerCurrent": pd1ModuleAllocatedPowerCurrent,
       "pd1ModuleAllocatedPowerMax": pd1ModuleAllocatedPowerMax,
       "pd1ModuleAllocatedPowerMin": pd1ModuleAllocatedPowerMin,
       "pd1ModuleCPUDutyCycles": pd1ModuleCPUDutyCycles,
       "pd1ModuleThrottle": pd1ModuleThrottle,
       "powerDomain2": powerDomain2,
       "powerDomain2Table": powerDomain2Table,
       "powerDomain2Entry": powerDomain2Entry,
       "pd2Index": pd2Index,
       "pd2BayNumber": pd2BayNumber,
       "pd2BladePrimarySlot": pd2BladePrimarySlot,
       "pd2ModuleStatus": pd2ModuleStatus,
       "pd2ModuleName": pd2ModuleName,
       "pd2ModuleState": pd2ModuleState,
       "pd2ModuleAllocatedPowerCurrent": pd2ModuleAllocatedPowerCurrent,
       "pd2ModuleAllocatedPowerMax": pd2ModuleAllocatedPowerMax,
       "pd2ModuleAllocatedPowerMin": pd2ModuleAllocatedPowerMin,
       "pd2ModuleCPUDutyCycles": pd2ModuleCPUDutyCycles,
       "pd2ModuleThrottle": pd2ModuleThrottle,
       "monitorThresholds": monitorThresholds,
       "voltageThresholds": voltageThresholds,
       "voltageThresholdsTable": voltageThresholdsTable,
       "voltageThresholdsEntry": voltageThresholdsEntry,
       "voltageThresholdEntryIndex": voltageThresholdEntryIndex,
       "voltageThresholdEntryName": voltageThresholdEntryName,
       "voltageThresholdEntryCurrentValue": voltageThresholdEntryCurrentValue,
       "voltageThresholdEntryWarningHighValue": voltageThresholdEntryWarningHighValue,
       "voltageThresholdEntryWarningResetHighValue": voltageThresholdEntryWarningResetHighValue,
       "voltageThresholdEntryWarningLowValue": voltageThresholdEntryWarningLowValue,
       "voltageThresholdEntryWarningResetLowValue": voltageThresholdEntryWarningResetLowValue,
       "vpdInformation": vpdInformation,
       "chassisVpd": chassisVpd,
       "bladeCenterVpd": bladeCenterVpd,
       "bladeCenterVpdMachineType": bladeCenterVpdMachineType,
       "bladeCenterVpdMachineModel": bladeCenterVpdMachineModel,
       "bladeCenterSerialNumber": bladeCenterSerialNumber,
       "bladeCenterUUID": bladeCenterUUID,
       "bladeCenterManufacturingId": bladeCenterManufacturingId,
       "bladeCenterHardwareRevision": bladeCenterHardwareRevision,
       "bladeCenterFruNumber": bladeCenterFruNumber,
       "bladeCenterManufDate": bladeCenterManufDate,
       "bladeCenterPartNumber": bladeCenterPartNumber,
       "bladeCenterFruSerial": bladeCenterFruSerial,
       "mmHardwareVpd": mmHardwareVpd,
       "mmHardwareVpdTable": mmHardwareVpdTable,
       "mmHardwareVpdEntry": mmHardwareVpdEntry,
       "mmHardwareVpdIndex": mmHardwareVpdIndex,
       "mmHardwareVpdBayNumber": mmHardwareVpdBayNumber,
       "mmHardwareVpdManufacturingId": mmHardwareVpdManufacturingId,
       "mmHardwareVpdFruNumber": mmHardwareVpdFruNumber,
       "mmHardwareVpdHardwareRevision": mmHardwareVpdHardwareRevision,
       "mmHardwareVpdUuid": mmHardwareVpdUuid,
       "mmHardwareVpdManufDate": mmHardwareVpdManufDate,
       "mmHardwareVpdPartNumber": mmHardwareVpdPartNumber,
       "mmHardwareVpdFruSerial": mmHardwareVpdFruSerial,
       "mmFirmwareVpd": mmFirmwareVpd,
       "mmMainApplVpdTable": mmMainApplVpdTable,
       "mmMainApplVpdEntry": mmMainApplVpdEntry,
       "mmMainApplVpdIndex": mmMainApplVpdIndex,
       "mmMainApplVpdName": mmMainApplVpdName,
       "mmMainApplVpdBuildId": mmMainApplVpdBuildId,
       "mmMainApplVpdRevisonNumber": mmMainApplVpdRevisonNumber,
       "mmMainApplVpdFilename": mmMainApplVpdFilename,
       "mmMainApplVpdBuildDate": mmMainApplVpdBuildDate,
       "mmBootROMVpdTable": mmBootROMVpdTable,
       "mmBootROMVpdEntry": mmBootROMVpdEntry,
       "mmBootROMVpdIndex": mmBootROMVpdIndex,
       "mmBootROMVpdName": mmBootROMVpdName,
       "mmBootROMVpdBuildId": mmBootROMVpdBuildId,
       "mmBootROMVpdRevisonNumber": mmBootROMVpdRevisonNumber,
       "mmBootROMVpdFilename": mmBootROMVpdFilename,
       "mmBootROMVpdBuildDate": mmBootROMVpdBuildDate,
       "mmRemoteControlVpdTable": mmRemoteControlVpdTable,
       "mmRemoteControlVpdEntry": mmRemoteControlVpdEntry,
       "mmRemoteControlVpdIndex": mmRemoteControlVpdIndex,
       "mmRemoteControlVpdName": mmRemoteControlVpdName,
       "mmRemoteControlVpdBuildId": mmRemoteControlVpdBuildId,
       "mmRemoteControlVpdRevisonNumber": mmRemoteControlVpdRevisonNumber,
       "mmRemoteControlVpdFilename": mmRemoteControlVpdFilename,
       "mmRemoteControlVpdBuildDate": mmRemoteControlVpdBuildDate,
       "mmPS2toUSBConvVpdTable": mmPS2toUSBConvVpdTable,
       "mmPS2toUSBConvVpdEntry": mmPS2toUSBConvVpdEntry,
       "mmPS2toUSBConvVpdIndex": mmPS2toUSBConvVpdIndex,
       "mmPS2toUSBConvVpdName": mmPS2toUSBConvVpdName,
       "mmPS2toUSBConvVpdBuildId": mmPS2toUSBConvVpdBuildId,
       "mmPS2toUSBConvVpdRevisonNumber": mmPS2toUSBConvVpdRevisonNumber,
       "mmPS2toUSBConvVpdFilename": mmPS2toUSBConvVpdFilename,
       "mmPS2toUSBConvVpdBuildDate": mmPS2toUSBConvVpdBuildDate,
       "mmToUSBIntfVpdTable": mmToUSBIntfVpdTable,
       "mmToUSBIntfVpdEntry": mmToUSBIntfVpdEntry,
       "mmToUSBIntfVpdIndex": mmToUSBIntfVpdIndex,
       "mmToUSBIntfVpdName": mmToUSBIntfVpdName,
       "mmToUSBIntfVpdBuildId": mmToUSBIntfVpdBuildId,
       "mmToUSBIntfVpdRevisonNumber": mmToUSBIntfVpdRevisonNumber,
       "mmToUSBIntfVpdFilename": mmToUSBIntfVpdFilename,
       "mmToUSBIntfVpdBuildDate": mmToUSBIntfVpdBuildDate,
       "bladeHardwareVpd": bladeHardwareVpd,
       "bladeHardwareVpdTable": bladeHardwareVpdTable,
       "bladeHardwareVpdEntry": bladeHardwareVpdEntry,
       "bladeHardwareVpdIndex": bladeHardwareVpdIndex,
       "bladeHardwareVpdBayNumber": bladeHardwareVpdBayNumber,
       "bladeHardwareVpdManufacturingId": bladeHardwareVpdManufacturingId,
       "bladeHardwareVpdFruNumber": bladeHardwareVpdFruNumber,
       "bladeHardwareVpdHardwareRevision": bladeHardwareVpdHardwareRevision,
       "bladeHardwareVpdSerialNumber": bladeHardwareVpdSerialNumber,
       "bladeHardwareVpdMachineType": bladeHardwareVpdMachineType,
       "bladeHardwareVpdUuid": bladeHardwareVpdUuid,
       "bladeHardwareVpdManufDate": bladeHardwareVpdManufDate,
       "bladeHardwareVpdPartNumber": bladeHardwareVpdPartNumber,
       "bladeHardwareVpdFruSerial": bladeHardwareVpdFruSerial,
       "bladeDaughterVpdCardType": bladeDaughterVpdCardType,
       "bladeDaughterVpdManufacturingId": bladeDaughterVpdManufacturingId,
       "bladeDaughterVpdFruNumber": bladeDaughterVpdFruNumber,
       "bladeDaughterVpdHardwareRevision": bladeDaughterVpdHardwareRevision,
       "bladeDaughterVpdSerialNumber": bladeDaughterVpdSerialNumber,
       "bladeDaughterVpdMachineType": bladeDaughterVpdMachineType,
       "bladeDaughterVpdUuid": bladeDaughterVpdUuid,
       "bladeDaughterVpdManufDate": bladeDaughterVpdManufDate,
       "bladeDaughterVpdPartNumber": bladeDaughterVpdPartNumber,
       "bladeDaughterVpdFruSerial": bladeDaughterVpdFruSerial,
       "bladeMACAddressVpdTable": bladeMACAddressVpdTable,
       "bladeMACAddressVpdEntry": bladeMACAddressVpdEntry,
       "bladeMACAddressVpdIndex": bladeMACAddressVpdIndex,
       "bladeMACAddress1Vpd": bladeMACAddress1Vpd,
       "bladeMACAddress2Vpd": bladeMACAddress2Vpd,
       "bladeMACAddress3Vpd": bladeMACAddress3Vpd,
       "bladeMACAddress4Vpd": bladeMACAddress4Vpd,
       "bladeDaughterCard1MACAddress1Vpd": bladeDaughterCard1MACAddress1Vpd,
       "bladeDaughterCard1MACAddress2Vpd": bladeDaughterCard1MACAddress2Vpd,
       "bladeDaughterCard1MACAddress3Vpd": bladeDaughterCard1MACAddress3Vpd,
       "bladeDaughterCard1MACAddress4Vpd": bladeDaughterCard1MACAddress4Vpd,
       "bladeDaughterCard2MACAddress1Vpd": bladeDaughterCard2MACAddress1Vpd,
       "bladeDaughterCard2MACAddress2Vpd": bladeDaughterCard2MACAddress2Vpd,
       "bladeDaughterCard2MACAddress3Vpd": bladeDaughterCard2MACAddress3Vpd,
       "bladeDaughterCard2MACAddress4Vpd": bladeDaughterCard2MACAddress4Vpd,
       "bladeFirmwareVpd": bladeFirmwareVpd,
       "bladeBiosVPDTable": bladeBiosVPDTable,
       "bladeBiosVPDEntry": bladeBiosVPDEntry,
       "bladeBiosVpdIndex": bladeBiosVpdIndex,
       "bladeBiosVpdId": bladeBiosVpdId,
       "bladeBiosVpdExists": bladeBiosVpdExists,
       "bladeBiosVpdPowerState": bladeBiosVpdPowerState,
       "bladeBiosVpdName": bladeBiosVpdName,
       "bladeBiosVpdBuildId": bladeBiosVpdBuildId,
       "bladeBiosVpdRevision": bladeBiosVpdRevision,
       "bladeBiosVpdDate": bladeBiosVpdDate,
       "bladeDiagsVPDTable": bladeDiagsVPDTable,
       "bladeDiagsVPDEntry": bladeDiagsVPDEntry,
       "bladeDiagsVpdIndex": bladeDiagsVpdIndex,
       "bladeDiagsVpdId": bladeDiagsVpdId,
       "bladeDiagsVpdExists": bladeDiagsVpdExists,
       "bladeDiagsVpdPowerState": bladeDiagsVpdPowerState,
       "bladeDiagsVpdName": bladeDiagsVpdName,
       "bladeDiagsVpdBuildId": bladeDiagsVpdBuildId,
       "bladeDiagsVpdRevision": bladeDiagsVpdRevision,
       "bladeDiagsVpdDate": bladeDiagsVpdDate,
       "bladeSysMgmtProcVPDTable": bladeSysMgmtProcVPDTable,
       "bladeSysMgmtProcVPDEntry": bladeSysMgmtProcVPDEntry,
       "bladeSysMgmtProcVpdIndex": bladeSysMgmtProcVpdIndex,
       "bladeSysMgmtProcVpdId": bladeSysMgmtProcVpdId,
       "bladeSysMgmtProcVpdExists": bladeSysMgmtProcVpdExists,
       "bladeSysMgmtProcVpdPowerState": bladeSysMgmtProcVpdPowerState,
       "bladeSysMgmtProcVpdName": bladeSysMgmtProcVpdName,
       "bladeSysMgmtProcVpdBuildId": bladeSysMgmtProcVpdBuildId,
       "bladeSysMgmtProcVpdRevision": bladeSysMgmtProcVpdRevision,
       "smHardwareVpd": smHardwareVpd,
       "smHardwareVpdTable": smHardwareVpdTable,
       "smHardwareVpdEntry": smHardwareVpdEntry,
       "smHardwareVpdIndex": smHardwareVpdIndex,
       "smHardwareVpdBayNumber": smHardwareVpdBayNumber,
       "smHardwareVpdManufacturingId": smHardwareVpdManufacturingId,
       "smHardwareVpdFruNumber": smHardwareVpdFruNumber,
       "smHardwareVpdHardwareRevision": smHardwareVpdHardwareRevision,
       "smHardwareVpdUuid": smHardwareVpdUuid,
       "smHardwareVpdManufDate": smHardwareVpdManufDate,
       "smHardwareVpdPartNumber": smHardwareVpdPartNumber,
       "smHardwareVpdFruSerial": smHardwareVpdFruSerial,
       "smFirmwareVpd": smFirmwareVpd,
       "smMainAppVpdTable": smMainAppVpdTable,
       "smMainAppVpdEntry": smMainAppVpdEntry,
       "smMainAppVpdIndex": smMainAppVpdIndex,
       "smMainAppVpdId": smMainAppVpdId,
       "smMainAppVpdExists": smMainAppVpdExists,
       "smMainAppVpdSwitchType": smMainAppVpdSwitchType,
       "smMainApp1VpdBuildId": smMainApp1VpdBuildId,
       "smMainApp1VpdBuildDate": smMainApp1VpdBuildDate,
       "smMainApp1VpdRevisionNumber": smMainApp1VpdRevisionNumber,
       "smMainApp2VpdBuildId": smMainApp2VpdBuildId,
       "smMainApp2VpdBuildDate": smMainApp2VpdBuildDate,
       "smMainApp2VpdRevisionNumber": smMainApp2VpdRevisionNumber,
       "smBootRomVpdTable": smBootRomVpdTable,
       "smBootRomVpdEntry": smBootRomVpdEntry,
       "smBootRomVpdIndex": smBootRomVpdIndex,
       "smBootRomVpdId": smBootRomVpdId,
       "smBootRomVpdExists": smBootRomVpdExists,
       "smBootRomVpdSwitchType": smBootRomVpdSwitchType,
       "smBootRomVpdBuildId": smBootRomVpdBuildId,
       "smBootRomVpdBuildDate": smBootRomVpdBuildDate,
       "smBootRomVpdRevisionNumber": smBootRomVpdRevisionNumber,
       "pmHardwareVpd": pmHardwareVpd,
       "pmHardwareVpdTable": pmHardwareVpdTable,
       "pmHardwareVpdEntry": pmHardwareVpdEntry,
       "pmHardwareVpdIndex": pmHardwareVpdIndex,
       "pmHardwareVpdBayNumber": pmHardwareVpdBayNumber,
       "pmHardwareVpdManufacturingId": pmHardwareVpdManufacturingId,
       "pmHardwareVpdFruNumber": pmHardwareVpdFruNumber,
       "pmHardwareVpdHardwareRevision": pmHardwareVpdHardwareRevision,
       "pmHardwareVpdUuid": pmHardwareVpdUuid,
       "pmHardwareVpdManufDate": pmHardwareVpdManufDate,
       "pmHardwareVpdPartNumber": pmHardwareVpdPartNumber,
       "pmHardwareVpdFruSerial": pmHardwareVpdFruSerial,
       "mtHardwareVpd": mtHardwareVpd,
       "mtHardwareVpdManufacturingId": mtHardwareVpdManufacturingId,
       "mtHardwareVpdFruNumber": mtHardwareVpdFruNumber,
       "mtHardwareVpdHardwareRevision": mtHardwareVpdHardwareRevision,
       "mtHardwareVpdUuid": mtHardwareVpdUuid,
       "inventoryManagementVpdTable": inventoryManagementVpdTable,
       "inventoryManagementVpdEntry": inventoryManagementVpdEntry,
       "componentLevelVpdIndex": componentLevelVpdIndex,
       "componentLevelVpdFruNumber": componentLevelVpdFruNumber,
       "componentLevelVpdSerialNumber": componentLevelVpdSerialNumber,
       "componentLevelVpdManufacturingId": componentLevelVpdManufacturingId,
       "componentLevelVpdBayNumber": componentLevelVpdBayNumber,
       "componentLevelVpdTypeCode": componentLevelVpdTypeCode,
       "componentLevelVpdMachineType": componentLevelVpdMachineType,
       "componentLevelVpdHardwareRevision": componentLevelVpdHardwareRevision,
       "inventoryManagementActivityVpdTable": inventoryManagementActivityVpdTable,
       "inventoryManagementActivityVpdEntry": inventoryManagementActivityVpdEntry,
       "componentLevelActivityVpdIndex": componentLevelActivityVpdIndex,
       "componentLevelActivityVpdFruNumber": componentLevelActivityVpdFruNumber,
       "componentLevelActivityVpdSerialNumber": componentLevelActivityVpdSerialNumber,
       "componentLevelActivityVpdManufacturingId": componentLevelActivityVpdManufacturingId,
       "componentLevelActivityVpdBayNumber": componentLevelActivityVpdBayNumber,
       "componentLevelActivityVpdAction": componentLevelActivityVpdAction,
       "componentLevelActivityVpdTimestamp": componentLevelActivityVpdTimestamp,
       "errorLogs": errorLogs,
       "eventLog": eventLog,
       "readEventLogTable": readEventLogTable,
       "readEventLogEntry": readEventLogEntry,
       "readEventLogIndex": readEventLogIndex,
       "readEventLogString": readEventLogString,
       "clearEventLog": clearEventLog,
       "monitorLogStateEvents": monitorLogStateEvents,
       "configureSP": configureSP,
       "remoteAccessConfig": remoteAccessConfig,
       "generalRemoteCfg": generalRemoteCfg,
       "remoteAlertRetryCount": remoteAlertRetryCount,
       "remoteAlertRetryDelay": remoteAlertRetryDelay,
       "remoteAccessTamperDelay": remoteAccessTamperDelay,
       "userAuthenticationMethod": userAuthenticationMethod,
       "allowModemLogin": allowModemLogin,
       "remoteAlertIds": remoteAlertIds,
       "remoteAlertIdsTable": remoteAlertIdsTable,
       "remoteAlertIdsEntry": remoteAlertIdsEntry,
       "remoteAlertIdEntryIndex": remoteAlertIdEntryIndex,
       "remoteAlertIdEntryStatus": remoteAlertIdEntryStatus,
       "remoteAlertIdEntryIpOrHostAddress": remoteAlertIdEntryIpOrHostAddress,
       "remoteAlertIdEntryTextDescription": remoteAlertIdEntryTextDescription,
       "remoteAlertIdEntryNotificationType": remoteAlertIdEntryNotificationType,
       "remoteAlertIdEmailAddr": remoteAlertIdEmailAddr,
       "remoteAlertIdEntrySelectiveAlert": remoteAlertIdEntrySelectiveAlert,
       "generateTestAlert": generateTestAlert,
       "remoteAccessIds": remoteAccessIds,
       "remoteAccessIdsTable": remoteAccessIdsTable,
       "remoteAccessIdsEntry": remoteAccessIdsEntry,
       "remoteAccessIdEntryIndex": remoteAccessIdEntryIndex,
       "remoteAccessIdEntryUserId": remoteAccessIdEntryUserId,
       "remoteAccessIdEntryPassword": remoteAccessIdEntryPassword,
       "remoteAccessIdEntryEncodedLoginPw": remoteAccessIdEntryEncodedLoginPw,
       "remoteAccessUserAuthorityLevelTable": remoteAccessUserAuthorityLevelTable,
       "remoteAccessUserAuthorityLevelEntry": remoteAccessUserAuthorityLevelEntry,
       "ualIndex": ualIndex,
       "ualId": ualId,
       "ualSupervisor": ualSupervisor,
       "ualReadOnly": ualReadOnly,
       "ualAccountManagement": ualAccountManagement,
       "ualConsoleAccess": ualConsoleAccess,
       "ualConsoleAndVirtualMediaAccess": ualConsoleAndVirtualMediaAccess,
       "ualServerPowerAccess": ualServerPowerAccess,
       "ualAllowClearLog": ualAllowClearLog,
       "ualAdapterBasicConfig": ualAdapterBasicConfig,
       "ualAdapterNetworkAndSecurityConfig": ualAdapterNetworkAndSecurityConfig,
       "ualAdapterAdvancedConfig": ualAdapterAdvancedConfig,
       "remoteAccessRBSroleTable": remoteAccessRBSroleTable,
       "remoteAccessRBSroleEntry": remoteAccessRBSroleEntry,
       "roleIndex": roleIndex,
       "roleId": roleId,
       "rbsSupervisor": rbsSupervisor,
       "rbsOperator": rbsOperator,
       "rbsChassisOperator": rbsChassisOperator,
       "rbsChassisAccountManagement": rbsChassisAccountManagement,
       "rbsChassisLogManagement": rbsChassisLogManagement,
       "rbsChassisConfiguration": rbsChassisConfiguration,
       "rbsChassisAdministration": rbsChassisAdministration,
       "rbsBladeOperator": rbsBladeOperator,
       "rbsBladeRemotePresence": rbsBladeRemotePresence,
       "rbsBladeConfiguration": rbsBladeConfiguration,
       "rbsBladeAdministration": rbsBladeAdministration,
       "rbsSwitchModuleOperator": rbsSwitchModuleOperator,
       "rbsSwitchModuleConfiguration": rbsSwitchModuleConfiguration,
       "rbsSwitchModuleAdministration": rbsSwitchModuleAdministration,
       "remoteAccessRBSscopeTable": remoteAccessRBSscopeTable,
       "remoteAccessRBSscopeEntry": remoteAccessRBSscopeEntry,
       "scopeIndex": scopeIndex,
       "scopeId": scopeId,
       "rbsChassis": rbsChassis,
       "rbsBlade1": rbsBlade1,
       "rbsBlade2": rbsBlade2,
       "rbsBlade3": rbsBlade3,
       "rbsBlade4": rbsBlade4,
       "rbsBlade5": rbsBlade5,
       "rbsBlade6": rbsBlade6,
       "rbsBlade7": rbsBlade7,
       "rbsBlade8": rbsBlade8,
       "rbsBlade9": rbsBlade9,
       "rbsBlade10": rbsBlade10,
       "rbsBlade11": rbsBlade11,
       "rbsBlade12": rbsBlade12,
       "rbsBlade13": rbsBlade13,
       "rbsBlade14": rbsBlade14,
       "rbsSwitch1": rbsSwitch1,
       "rbsSwitch2": rbsSwitch2,
       "rbsSwitch3": rbsSwitch3,
       "rbsSwitch4": rbsSwitch4,
       "remoteAlerts": remoteAlerts,
       "remoteAlertsCrit": remoteAlertsCrit,
       "critTemp": critTemp,
       "critVolt": critVolt,
       "critMultiBlower": critMultiBlower,
       "critPower": critPower,
       "critHardDrive": critHardDrive,
       "critVRM": critVRM,
       "critMultipleSwitchModule": critMultipleSwitchModule,
       "critInvalidConfig": critInvalidConfig,
       "remoteAlertsNonCrit": remoteAlertsNonCrit,
       "warnSingleBlower": warnSingleBlower,
       "warnTemp": warnTemp,
       "warnVoltage": warnVoltage,
       "warnRedundantModule": warnRedundantModule,
       "warnMediaTrayKVMSwitch": warnMediaTrayKVMSwitch,
       "remoteAlertsSystem": remoteAlertsSystem,
       "systemPowerOff": systemPowerOff,
       "systemPowerOn": systemPowerOn,
       "systemPFA": systemPFA,
       "systemInventory": systemInventory,
       "systemLog75PctFull": systemLog75PctFull,
       "networkChangeNotification": networkChangeNotification,
       "systemBladeThrottling": systemBladeThrottling,
       "systemPowerManagement": systemPowerManagement,
       "spClock": spClock,
       "spClockDateAndTimeSetting": spClockDateAndTimeSetting,
       "spClockTimezoneSetting": spClockTimezoneSetting,
       "spIdentification": spIdentification,
       "spTxtId": spTxtId,
       "networkConfiguration": networkConfiguration,
       "networkInterfaces": networkInterfaces,
       "extEthernetInterface": extEthernetInterface,
       "extEthernetInterfaceType": extEthernetInterfaceType,
       "extEthernetInterfaceHostName": extEthernetInterfaceHostName,
       "extEthernetInterfaceIPAddress": extEthernetInterfaceIPAddress,
       "extEthernetInterfaceDataRate": extEthernetInterfaceDataRate,
       "extEthernetInterfaceDuplexSetting": extEthernetInterfaceDuplexSetting,
       "extEthernetInterfaceLAA": extEthernetInterfaceLAA,
       "extEthernetInterfaceDhcpEnabled": extEthernetInterfaceDhcpEnabled,
       "extEthernetInterfaceGatewayIPAddress": extEthernetInterfaceGatewayIPAddress,
       "extEthernetInterfaceBIA": extEthernetInterfaceBIA,
       "extEthernetInterfaceMTU": extEthernetInterfaceMTU,
       "extEthernetInterfaceSubnetMask": extEthernetInterfaceSubnetMask,
       "dhcpEthernetInterface": dhcpEthernetInterface,
       "dhcpHostName": dhcpHostName,
       "dhcpIPAddress": dhcpIPAddress,
       "dhcpGatewayIPAddress": dhcpGatewayIPAddress,
       "dhcpSubnetMask": dhcpSubnetMask,
       "dhcpDomainName": dhcpDomainName,
       "dhcpDHCPServer": dhcpDHCPServer,
       "dhcpPrimaryDNSServer": dhcpPrimaryDNSServer,
       "dhcpSecondaryDNSServer": dhcpSecondaryDNSServer,
       "dhcpTertiaryDNSServer": dhcpTertiaryDNSServer,
       "intEthernetInterface": intEthernetInterface,
       "intEthernetInterfaceType": intEthernetInterfaceType,
       "intEthernetInterfaceEnabled": intEthernetInterfaceEnabled,
       "intEthernetInterfaceLocalIPAddress": intEthernetInterfaceLocalIPAddress,
       "intEthernetInterfaceDataRate": intEthernetInterfaceDataRate,
       "intEthernetInterfaceDuplexSetting": intEthernetInterfaceDuplexSetting,
       "intEthernetInterfaceLAA": intEthernetInterfaceLAA,
       "intEthernetInterfaceGatewayIPAddress": intEthernetInterfaceGatewayIPAddress,
       "intEthernetInterfaceBIA": intEthernetInterfaceBIA,
       "intEthernetInterfaceMTU": intEthernetInterfaceMTU,
       "intEthernetInterfaceSubnetMask": intEthernetInterfaceSubnetMask,
       "tcpProtocols": tcpProtocols,
       "snmpAgentConfig": snmpAgentConfig,
       "snmpSystemContact": snmpSystemContact,
       "snmpSystemLocation": snmpSystemLocation,
       "snmpSystemAgentTrapsDisable": snmpSystemAgentTrapsDisable,
       "snmpAgentCommunityConfig": snmpAgentCommunityConfig,
       "snmpCommunityTable": snmpCommunityTable,
       "snmpCommunityEntry": snmpCommunityEntry,
       "snmpCommunityEntryIndex": snmpCommunityEntryIndex,
       "snmpCommunityEntryCommunityName": snmpCommunityEntryCommunityName,
       "snmpCommunityEntryCommunityIpAddress1": snmpCommunityEntryCommunityIpAddress1,
       "snmpCommunityEntryCommunityIpAddress2": snmpCommunityEntryCommunityIpAddress2,
       "snmpCommunityEntryCommunityIpAddress3": snmpCommunityEntryCommunityIpAddress3,
       "snmpCommunityEntryCommunityViewType": snmpCommunityEntryCommunityViewType,
       "snmpv1SystemAgentEnable": snmpv1SystemAgentEnable,
       "snmpv3SystemAgentEnable": snmpv3SystemAgentEnable,
       "snmpAgentUserProfileConfig": snmpAgentUserProfileConfig,
       "snmpUserProfileTable": snmpUserProfileTable,
       "snmpUserProfileEntry": snmpUserProfileEntry,
       "snmpUserProfileEntryIndex": snmpUserProfileEntryIndex,
       "snmpUserProfileEntryContextName": snmpUserProfileEntryContextName,
       "snmpUserProfileEntryAuthProt": snmpUserProfileEntryAuthProt,
       "snmpUserProfileEntryPrivProt": snmpUserProfileEntryPrivProt,
       "snmpUserProfileEntryPrivPassword": snmpUserProfileEntryPrivPassword,
       "snmpUserProfileEntryViewType": snmpUserProfileEntryViewType,
       "snmpUserProfileEntryIpAddress": snmpUserProfileEntryIpAddress,
       "dnsConfig": dnsConfig,
       "dnsEnabled": dnsEnabled,
       "dnsServerIPAddress1": dnsServerIPAddress1,
       "dnsServerIPAddress2": dnsServerIPAddress2,
       "dnsServerIPAddress3": dnsServerIPAddress3,
       "smtpConfig": smtpConfig,
       "smtpServerNameOrIPAddress": smtpServerNameOrIPAddress,
       "attachmentsToEmailAlerts": attachmentsToEmailAlerts,
       "tcpApplicationConfig": tcpApplicationConfig,
       "telnetInactivityTimeout": telnetInactivityTimeout,
       "commandModeInactivityTimeout": commandModeInactivityTimeout,
       "commandModeEnable": commandModeEnable,
       "slpAddrType": slpAddrType,
       "slpMulticastAddr": slpMulticastAddr,
       "tcpPortAssignmentCfg": tcpPortAssignmentCfg,
       "tcpPortsRestoreDefault": tcpPortsRestoreDefault,
       "httpPortAssignment": httpPortAssignment,
       "httpsPortAssignment": httpsPortAssignment,
       "telnetPortAssignment": telnetPortAssignment,
       "sshPortAssignment": sshPortAssignment,
       "snmpAgentPortAssignment": snmpAgentPortAssignment,
       "snmpTrapsPortAssignment": snmpTrapsPortAssignment,
       "ldapClientCfg": ldapClientCfg,
       "ldapServer1NameOrIPAddress": ldapServer1NameOrIPAddress,
       "ldapServer1PortNumber": ldapServer1PortNumber,
       "ldapServer2NameOrIPAddress": ldapServer2NameOrIPAddress,
       "ldapServer2PortNumber": ldapServer2PortNumber,
       "ldapServer3NameOrIPAddress": ldapServer3NameOrIPAddress,
       "ldapServer3PortNumber": ldapServer3PortNumber,
       "ldapRootDN": ldapRootDN,
       "ldapUserSearchBaseDN": ldapUserSearchBaseDN,
       "ldapGroupFilter": ldapGroupFilter,
       "ldapBindingMethod": ldapBindingMethod,
       "ldapClientAuthenticationDN": ldapClientAuthenticationDN,
       "ldapClientAuthenticationPassword": ldapClientAuthenticationPassword,
       "ldapUIDsearchAttribute": ldapUIDsearchAttribute,
       "ldapGroupSearchAttribute": ldapGroupSearchAttribute,
       "ldapLoginPermissionAttribute": ldapLoginPermissionAttribute,
       "ldapUseDNSOrPreConfiguredServers": ldapUseDNSOrPreConfiguredServers,
       "ldapDomainSource": ldapDomainSource,
       "ldapSearchDomain": ldapSearchDomain,
       "ldapServiceName": ldapServiceName,
       "uplinkCheckConfig": uplinkCheckConfig,
       "uplinkCheckEnabled": uplinkCheckEnabled,
       "uplinkCheckDelay": uplinkCheckDelay,
       "solConfiguration": solConfiguration,
       "solGlobalConfig": solGlobalConfig,
       "solEnable": solEnable,
       "solVlanId": solVlanId,
       "solAccumulateTimeout": solAccumulateTimeout,
       "solCharSendThreshold": solCharSendThreshold,
       "solRetry": solRetry,
       "solRetryInterval": solRetryInterval,
       "solExitToCliKeySeq": solExitToCliKeySeq,
       "solResetBladeKeySeq": solResetBladeKeySeq,
       "solBladeConfig": solBladeConfig,
       "solBladeTable": solBladeTable,
       "solBladeEntry": solBladeEntry,
       "solBladeIndex": solBladeIndex,
       "solBladeName": solBladeName,
       "solBladeEnable": solBladeEnable,
       "solBladeIpAddr": solBladeIpAddr,
       "solBladeSessionStatus": solBladeSessionStatus,
       "solBladeCapability": solBladeCapability,
       "telcoManagement": telcoManagement,
       "telcoAlarmReq": telcoAlarmReq,
       "telcoAlarmSet": telcoAlarmSet,
       "telcoAlarmAck": telcoAlarmAck,
       "telcoAlarmClear": telcoAlarmClear,
       "telcoOEM": telcoOEM,
       "telcoOEMs": telcoOEMs,
       "restartReset": restartReset,
       "restartSPImmediately": restartSPImmediately,
       "switchOverRedundantMM": switchOverRedundantMM,
       "resetSPConfigAndRestart": resetSPConfigAndRestart,
       "bladeCenter": bladeCenter,
       "processorBlade": processorBlade,
       "bladeMediaTrayBladeId": bladeMediaTrayBladeId,
       "bladeKVMBladeId": bladeKVMBladeId,
       "bladeBootSequenceTable": bladeBootSequenceTable,
       "bladeBootSequenceEntry": bladeBootSequenceEntry,
       "bootSequenceIndex": bootSequenceIndex,
       "bootSequenceBladeId": bootSequenceBladeId,
       "bootSequenceBladeExists": bootSequenceBladeExists,
       "bootSequenceBladePowerState": bootSequenceBladePowerState,
       "bootSequenceBladeHealthState": bootSequenceBladeHealthState,
       "bootSequenceBladeName": bootSequenceBladeName,
       "bootSequence1": bootSequence1,
       "bootSequence2": bootSequence2,
       "bootSequence3": bootSequence3,
       "bootSequence4": bootSequence4,
       "bladeRemoteControl": bladeRemoteControl,
       "bladeRemoteControlTable": bladeRemoteControlTable,
       "bladeRemoteControlEntry": bladeRemoteControlEntry,
       "remoteControlIndex": remoteControlIndex,
       "remoteControlBladeId": remoteControlBladeId,
       "remoteControlBladeExists": remoteControlBladeExists,
       "remoteControlBladePowerState": remoteControlBladePowerState,
       "remoteControlBladeHealthState": remoteControlBladeHealthState,
       "remoteControlBladeName": remoteControlBladeName,
       "remotePowerControlEnable": remotePowerControlEnable,
       "remoteMediaTrayControlEnable": remoteMediaTrayControlEnable,
       "remoteKVMControlEnable": remoteKVMControlEnable,
       "remoteWakeOnLanControlEnable": remoteWakeOnLanControlEnable,
       "bladePolicy": bladePolicy,
       "bladePolicyPowerControlEnable": bladePolicyPowerControlEnable,
       "bladePolicyMediaTrayControlEnable": bladePolicyMediaTrayControlEnable,
       "bladePolicyKVMControlEnable": bladePolicyKVMControlEnable,
       "bladePolicyWakeOnLanControlEnable": bladePolicyWakeOnLanControlEnable,
       "bladeMonitors": bladeMonitors,
       "bladeSystemStatusTable": bladeSystemStatusTable,
       "bladeSystemStatusEntry": bladeSystemStatusEntry,
       "bladeStatusIndex": bladeStatusIndex,
       "bladeId": bladeId,
       "bladeExists": bladeExists,
       "bladePowerState": bladePowerState,
       "bladeHealthState": bladeHealthState,
       "bladeName": bladeName,
       "bladeRemotePowerEnable": bladeRemotePowerEnable,
       "bladeRemoteMediaTrayEnable": bladeRemoteMediaTrayEnable,
       "bladeRemoteKVMEnable": bladeRemoteKVMEnable,
       "bladeConnectionType": bladeConnectionType,
       "bladeOwnsKVM": bladeOwnsKVM,
       "bladeOwnsMediaTray": bladeOwnsMediaTray,
       "bladeRemoteWakeOnLanEnable": bladeRemoteWakeOnLanEnable,
       "bladeServerExpansion": bladeServerExpansion,
       "bladeWidth": bladeWidth,
       "bladeSupportCapacityOnDemand": bladeSupportCapacityOnDemand,
       "bladeHealthSummaryTable": bladeHealthSummaryTable,
       "bladeHealthSummaryEntry": bladeHealthSummaryEntry,
       "bladeHealthSummaryIndex": bladeHealthSummaryIndex,
       "bladeHealthSummaryBladeId": bladeHealthSummaryBladeId,
       "bladeHealthSummarySeverity": bladeHealthSummarySeverity,
       "bladeHealthSummaryDescription": bladeHealthSummaryDescription,
       "bladeTemperaturesTable": bladeTemperaturesTable,
       "bladeTemperaturesEntry": bladeTemperaturesEntry,
       "temperatureIndex": temperatureIndex,
       "temperatureBladeId": temperatureBladeId,
       "temperatureBladeExists": temperatureBladeExists,
       "temperatureBladePowerState": temperatureBladePowerState,
       "temperatureBladeName": temperatureBladeName,
       "temperatureCPU1": temperatureCPU1,
       "temperatureCPU2": temperatureCPU2,
       "temperatureCPU3": temperatureCPU3,
       "temperatureCPU4": temperatureCPU4,
       "temperatureDASD1": temperatureDASD1,
       "bladeSensorTempCapability": bladeSensorTempCapability,
       "bladeSensor1Temp": bladeSensor1Temp,
       "bladeSensor2Temp": bladeSensor2Temp,
       "bladeSensor3Temp": bladeSensor3Temp,
       "bladeSensor4Temp": bladeSensor4Temp,
       "bladeSensor5Temp": bladeSensor5Temp,
       "bladeSensor6Temp": bladeSensor6Temp,
       "bladeTemperatureThresholdsTable": bladeTemperatureThresholdsTable,
       "bladeTemperatureThresholdsEntry": bladeTemperatureThresholdsEntry,
       "temperatureThresholdIndex": temperatureThresholdIndex,
       "temperatureThresholdBladeId": temperatureThresholdBladeId,
       "temperatureThresholdBladeExists": temperatureThresholdBladeExists,
       "temperatureThresholdBladePowerState": temperatureThresholdBladePowerState,
       "temperatureThresholdBladeName": temperatureThresholdBladeName,
       "temperatureCPU1HardShutdown": temperatureCPU1HardShutdown,
       "temperatureCPU1Warning": temperatureCPU1Warning,
       "temperatureCPU1WarningReset": temperatureCPU1WarningReset,
       "temperatureCPU2HardShutdown": temperatureCPU2HardShutdown,
       "temperatureCPU2Warning": temperatureCPU2Warning,
       "temperatureCPU2WarningReset": temperatureCPU2WarningReset,
       "temperatureCPU3HardShutdown": temperatureCPU3HardShutdown,
       "temperatureCPU3Warning": temperatureCPU3Warning,
       "temperatureCPU3WarningReset": temperatureCPU3WarningReset,
       "temperatureCPU4HardShutdown": temperatureCPU4HardShutdown,
       "temperatureCPU4Warning": temperatureCPU4Warning,
       "temperatureCPU4WarningReset": temperatureCPU4WarningReset,
       "temperatureDASD1HardShutdown": temperatureDASD1HardShutdown,
       "temperatureDASD1Warning": temperatureDASD1Warning,
       "temperatureDASD1WarningReset": temperatureDASD1WarningReset,
       "bladeTempThresholdSensorCapability": bladeTempThresholdSensorCapability,
       "temperatureSensor1HardShutdown": temperatureSensor1HardShutdown,
       "temperatureSensor1Warning": temperatureSensor1Warning,
       "temperatureSensor1WarningReset": temperatureSensor1WarningReset,
       "temperatureSensor2HardShutdown": temperatureSensor2HardShutdown,
       "temperatureSensor2Warning": temperatureSensor2Warning,
       "temperatureSensor2WarningReset": temperatureSensor2WarningReset,
       "temperatureSensor3HardShutdown": temperatureSensor3HardShutdown,
       "temperatureSensor3Warning": temperatureSensor3Warning,
       "temperatureSensor3WarningReset": temperatureSensor3WarningReset,
       "temperatureSensor4HardShutdown": temperatureSensor4HardShutdown,
       "temperatureSensor4Warning": temperatureSensor4Warning,
       "temperatureSensor4WarningReset": temperatureSensor4WarningReset,
       "temperatureSensor5HardShutdown": temperatureSensor5HardShutdown,
       "temperatureSensor5Warning": temperatureSensor5Warning,
       "temperatureSensor5WarningReset": temperatureSensor5WarningReset,
       "temperatureSensor6HardShutdown": temperatureSensor6HardShutdown,
       "temperatureSensor6Warning": temperatureSensor6Warning,
       "temperatureSensor6WarningReset": temperatureSensor6WarningReset,
       "bladeVoltagesTable": bladeVoltagesTable,
       "bladeVoltagesEntry": bladeVoltagesEntry,
       "voltageIndex": voltageIndex,
       "voltageBladeId": voltageBladeId,
       "voltageBladeExists": voltageBladeExists,
       "voltageBladePowerState": voltageBladePowerState,
       "voltageBladeName": voltageBladeName,
       "bladePlus5Volt": bladePlus5Volt,
       "bladePlus3pt3Volt": bladePlus3pt3Volt,
       "bladePlus12Volt": bladePlus12Volt,
       "bladePlus2pt5Volt": bladePlus2pt5Volt,
       "bladePlus1pt5Volt": bladePlus1pt5Volt,
       "bladePlus1pt25Volt": bladePlus1pt25Volt,
       "bladeVRM1Volt": bladeVRM1Volt,
       "bladeSensorVoltCapability": bladeSensorVoltCapability,
       "bladeSensor1Volt": bladeSensor1Volt,
       "bladeSensor2Volt": bladeSensor2Volt,
       "bladeSensor3Volt": bladeSensor3Volt,
       "bladeSensor4Volt": bladeSensor4Volt,
       "bladeSensor5Volt": bladeSensor5Volt,
       "bladeSensor6Volt": bladeSensor6Volt,
       "bladeSensor7Volt": bladeSensor7Volt,
       "bladeSensor8Volt": bladeSensor8Volt,
       "bladeSensor9Volt": bladeSensor9Volt,
       "bladeSensor10Volt": bladeSensor10Volt,
       "bladeSensor11Volt": bladeSensor11Volt,
       "bladeSensor12Volt": bladeSensor12Volt,
       "bladeSensor13Volt": bladeSensor13Volt,
       "bladeSensor14Volt": bladeSensor14Volt,
       "bladeSensor15Volt": bladeSensor15Volt,
       "bladeSensor16Volt": bladeSensor16Volt,
       "bladeSensor17Volt": bladeSensor17Volt,
       "bladeSensor18Volt": bladeSensor18Volt,
       "bladeSensor19Volt": bladeSensor19Volt,
       "bladeSensor20Volt": bladeSensor20Volt,
       "bladeSensor21Volt": bladeSensor21Volt,
       "bladeSensor22Volt": bladeSensor22Volt,
       "bladeSensor23Volt": bladeSensor23Volt,
       "bladeSensor24Volt": bladeSensor24Volt,
       "bladeSensor25Volt": bladeSensor25Volt,
       "bladeSensor26Volt": bladeSensor26Volt,
       "bladeSensor27Volt": bladeSensor27Volt,
       "bladeSensor28Volt": bladeSensor28Volt,
       "bladeSensor29Volt": bladeSensor29Volt,
       "bladeSensor30Volt": bladeSensor30Volt,
       "bladeVoltageThresholdsTable": bladeVoltageThresholdsTable,
       "bladeVoltageThresholdsEntry": bladeVoltageThresholdsEntry,
       "voltageThresholdIndex": voltageThresholdIndex,
       "voltageThresholdBladeId": voltageThresholdBladeId,
       "voltageThresholdBladeExists": voltageThresholdBladeExists,
       "voltageThresholdBladePowerState": voltageThresholdBladePowerState,
       "voltageThresholdBladeName": voltageThresholdBladeName,
       "bladePlus5VoltHighWarning": bladePlus5VoltHighWarning,
       "bladePlus5VoltLowWarning": bladePlus5VoltLowWarning,
       "bladePlus3pt3VoltHighWarning": bladePlus3pt3VoltHighWarning,
       "bladePlus3pt3VoltLowWarning": bladePlus3pt3VoltLowWarning,
       "bladePlus12VoltHighWarning": bladePlus12VoltHighWarning,
       "bladePlus12VoltLowWarning": bladePlus12VoltLowWarning,
       "bladePlus2pt5VoltHighWarning": bladePlus2pt5VoltHighWarning,
       "bladePlus2pt5VoltLowWarning": bladePlus2pt5VoltLowWarning,
       "bladePlus1pt5VoltHighWarning": bladePlus1pt5VoltHighWarning,
       "bladePlus1pt5VoltLowWarning": bladePlus1pt5VoltLowWarning,
       "bladePlus1pt25VoltHighWarning": bladePlus1pt25VoltHighWarning,
       "bladePlus1pt25VoltLowWarning": bladePlus1pt25VoltLowWarning,
       "bladeVoltThresholdSensorCapability": bladeVoltThresholdSensorCapability,
       "bladeSensor1VoltHighWarning": bladeSensor1VoltHighWarning,
       "bladeSensor1VoltLowWarning": bladeSensor1VoltLowWarning,
       "bladeSensor2VoltHighWarning": bladeSensor2VoltHighWarning,
       "bladeSensor2VoltLowWarning": bladeSensor2VoltLowWarning,
       "bladeSensor3VoltHighWarning": bladeSensor3VoltHighWarning,
       "bladeSensor3VoltLowWarning": bladeSensor3VoltLowWarning,
       "bladeSensor4VoltHighWarning": bladeSensor4VoltHighWarning,
       "bladeSensor4VoltLowWarning": bladeSensor4VoltLowWarning,
       "bladeSensor5VoltHighWarning": bladeSensor5VoltHighWarning,
       "bladeSensor5VoltLowWarning": bladeSensor5VoltLowWarning,
       "bladeSensor6VoltHighWarning": bladeSensor6VoltHighWarning,
       "bladeSensor6VoltLowWarning": bladeSensor6VoltLowWarning,
       "bladeSensor7VoltHighWarning": bladeSensor7VoltHighWarning,
       "bladeSensor7VoltLowWarning": bladeSensor7VoltLowWarning,
       "bladeSensor8VoltHighWarning": bladeSensor8VoltHighWarning,
       "bladeSensor8VoltLowWarning": bladeSensor8VoltLowWarning,
       "bladeSensor9VoltHighWarning": bladeSensor9VoltHighWarning,
       "bladeSensor9VoltLowWarning": bladeSensor9VoltLowWarning,
       "bladeSensor10VoltHighWarning": bladeSensor10VoltHighWarning,
       "bladeSensor10VoltLowWarning": bladeSensor10VoltLowWarning,
       "bladeSensor11VoltHighWarning": bladeSensor11VoltHighWarning,
       "bladeSensor11VoltLowWarning": bladeSensor11VoltLowWarning,
       "bladeSensor12VoltHighWarning": bladeSensor12VoltHighWarning,
       "bladeSensor12VoltLowWarning": bladeSensor12VoltLowWarning,
       "bladeSensor13VoltHighWarning": bladeSensor13VoltHighWarning,
       "bladeSensor13VoltLowWarning": bladeSensor13VoltLowWarning,
       "bladeSensor14VoltHighWarning": bladeSensor14VoltHighWarning,
       "bladeSensor14VoltLowWarning": bladeSensor14VoltLowWarning,
       "bladeSensor15VoltHighWarning": bladeSensor15VoltHighWarning,
       "bladeSensor15VoltLowWarning": bladeSensor15VoltLowWarning,
       "bladeSensor16VoltHighWarning": bladeSensor16VoltHighWarning,
       "bladeSensor16VoltLowWarning": bladeSensor16VoltLowWarning,
       "bladeSensor17VoltHighWarning": bladeSensor17VoltHighWarning,
       "bladeSensor17VoltLowWarning": bladeSensor17VoltLowWarning,
       "bladeSensor18VoltHighWarning": bladeSensor18VoltHighWarning,
       "bladeSensor18VoltLowWarning": bladeSensor18VoltLowWarning,
       "bladeSensor19VoltHighWarning": bladeSensor19VoltHighWarning,
       "bladeSensor19VoltLowWarning": bladeSensor19VoltLowWarning,
       "bladeSensor20VoltHighWarning": bladeSensor20VoltHighWarning,
       "bladeSensor20VoltLowWarning": bladeSensor20VoltLowWarning,
       "bladeSensor21VoltHighWarning": bladeSensor21VoltHighWarning,
       "bladeSensor21VoltLowWarning": bladeSensor21VoltLowWarning,
       "bladeSensor22VoltHighWarning": bladeSensor22VoltHighWarning,
       "bladeSensor22VoltLowWarning": bladeSensor22VoltLowWarning,
       "bladeSensor23VoltHighWarning": bladeSensor23VoltHighWarning,
       "bladeSensor23VoltLowWarning": bladeSensor23VoltLowWarning,
       "bladeSensor24VoltHighWarning": bladeSensor24VoltHighWarning,
       "bladeSensor24VoltLowWarning": bladeSensor24VoltLowWarning,
       "bladeSensor25VoltHighWarning": bladeSensor25VoltHighWarning,
       "bladeSensor25VoltLowWarning": bladeSensor25VoltLowWarning,
       "bladeSensor26VoltHighWarning": bladeSensor26VoltHighWarning,
       "bladeSensor26VoltLowWarning": bladeSensor26VoltLowWarning,
       "bladeSensor27VoltHighWarning": bladeSensor27VoltHighWarning,
       "bladeSensor27VoltLowWarning": bladeSensor27VoltLowWarning,
       "bladeSensor28VoltHighWarning": bladeSensor28VoltHighWarning,
       "bladeSensor28VoltLowWarning": bladeSensor28VoltLowWarning,
       "bladeSensor29VoltHighWarning": bladeSensor29VoltHighWarning,
       "bladeSensor29VoltLowWarning": bladeSensor29VoltLowWarning,
       "bladeSensor30VoltHighWarning": bladeSensor30VoltHighWarning,
       "bladeSensor30VoltLowWarning": bladeSensor30VoltLowWarning,
       "bladePowerRestart": bladePowerRestart,
       "bladePowerRestartTable": bladePowerRestartTable,
       "bladePowerRestartEntry": bladePowerRestartEntry,
       "powerRestartIndex": powerRestartIndex,
       "powerRestartBladeId": powerRestartBladeId,
       "powerRestartBladeExists": powerRestartBladeExists,
       "powerRestartBladePowerState": powerRestartBladePowerState,
       "powerRestartBladeHealthState": powerRestartBladeHealthState,
       "powerRestartBladeName": powerRestartBladeName,
       "powerOnOffBlade": powerOnOffBlade,
       "restartBlade": restartBlade,
       "restartBladeSMP": restartBladeSMP,
       "restartBladeNMI": restartBladeNMI,
       "restartBladeClearNVRAM": restartBladeClearNVRAM,
       "restartBladeInvokeDiags": restartBladeInvokeDiags,
       "restartBladeInvokeDiagsFromDefaultBootList": restartBladeInvokeDiagsFromDefaultBootList,
       "bladeConfiguration": bladeConfiguration,
       "bladeConfigurationTable": bladeConfigurationTable,
       "bladeConfigurationEntry": bladeConfigurationEntry,
       "configurationIndex": configurationIndex,
       "configurationBladeId": configurationBladeId,
       "configurationBladeExists": configurationBladeExists,
       "configurationBladePowerState": configurationBladePowerState,
       "configurationBladeName": configurationBladeName,
       "bladePowerManagementPolicy": bladePowerManagementPolicy,
       "powerdomain1Oversubscription": powerdomain1Oversubscription,
       "powerdomain2Oversubscription": powerdomain2Oversubscription,
       "acousticMode": acousticMode,
       "bladeIPAddrRangeStart": bladeIPAddrRangeStart,
       "bladeCapacityOnDemand": bladeCapacityOnDemand,
       "bladeCapacityOnDemandTable": bladeCapacityOnDemandTable,
       "bladeCapacityOnDemandEntry": bladeCapacityOnDemandEntry,
       "bladeCapacityOnDemandIndex": bladeCapacityOnDemandIndex,
       "bladeCapacityOnDemandBladeName": bladeCapacityOnDemandBladeName,
       "bladeCapacityOnDemandState": bladeCapacityOnDemandState,
       "bladeBootCountPowerOnTime": bladeBootCountPowerOnTime,
       "bladeBootCountPowerOnTimeTable": bladeBootCountPowerOnTimeTable,
       "bladeBootCountPowerOnTimeEntry": bladeBootCountPowerOnTimeEntry,
       "bootCountPowerOnTimeBladeIndex": bootCountPowerOnTimeBladeIndex,
       "bootCountPowerOnTimeBladeId": bootCountPowerOnTimeBladeId,
       "bootCountPowerOnTimeBoots": bootCountPowerOnTimeBoots,
       "bootCountPowerOnTimeSecs": bootCountPowerOnTimeSecs,
       "switchModule": switchModule,
       "switchModuleControl": switchModuleControl,
       "smControlTable": smControlTable,
       "smControlEntry": smControlEntry,
       "smControlIndex": smControlIndex,
       "switchModuleControlId": switchModuleControlId,
       "smPostResultsAvailable": smPostResultsAvailable,
       "smPostResultsValue": smPostResultsValue,
       "switchModuleMemDiagEnableDisable": switchModuleMemDiagEnableDisable,
       "smCfgCtrlEnableDisable": smCfgCtrlEnableDisable,
       "smExtEthPortsEnableDisable": smExtEthPortsEnableDisable,
       "switchPingRequest": switchPingRequest,
       "smCfgCtrlOnResetEnableDisable": smCfgCtrlOnResetEnableDisable,
       "smHealthState": smHealthState,
       "smPowerRestartTable": smPowerRestartTable,
       "smPowerRestartEntry": smPowerRestartEntry,
       "smPowerRestartIndex": smPowerRestartIndex,
       "smPowerRestartId": smPowerRestartId,
       "smSwitchExists": smSwitchExists,
       "smSwitchType": smSwitchType,
       "smMACAddress": smMACAddress,
       "smIPAddress": smIPAddress,
       "switchModulePowerOnOff": switchModulePowerOnOff,
       "smReset": smReset,
       "smResetToDefault": smResetToDefault,
       "smRestartAndRunStdDiag": smRestartAndRunStdDiag,
       "smRestartAndRunExtDiag": smRestartAndRunExtDiag,
       "smRestartAndRunFullDiag": smRestartAndRunFullDiag,
       "switchModuleConfig": switchModuleConfig,
       "switchMgmtNetworkCfg": switchMgmtNetworkCfg,
       "switchCurrentNwCfg": switchCurrentNwCfg,
       "smCurrentIPInfoTable": smCurrentIPInfoTable,
       "smCurrentIPInfoEntry": smCurrentIPInfoEntry,
       "smCurrentIPInfoIndex": smCurrentIPInfoIndex,
       "smCurrentIPInfoId": smCurrentIPInfoId,
       "smCurrentIPInfoExists": smCurrentIPInfoExists,
       "smCurrentIPInfoPowerState": smCurrentIPInfoPowerState,
       "smCurrentIPAddr": smCurrentIPAddr,
       "smCurrentSubnetMask": smCurrentSubnetMask,
       "smCurrentGateway": smCurrentGateway,
       "smCurrentIPConfigMethod": smCurrentIPConfigMethod,
       "switchNewNwCfg": switchNewNwCfg,
       "smNewIPInfoTable": smNewIPInfoTable,
       "smNewIPInfoEntry": smNewIPInfoEntry,
       "smNewIPInfoIndex": smNewIPInfoIndex,
       "smNewIPInfoId": smNewIPInfoId,
       "smNewIPInfoExists": smNewIPInfoExists,
       "smNewIPInfoPowerState": smNewIPInfoPowerState,
       "smNewIPAddr": smNewIPAddr,
       "smNewSubnetMask": smNewSubnetMask,
       "smNewGateway": smNewGateway,
       "smNewIPConfigMethod": smNewIPConfigMethod,
       "smNewIPConfigEnableDisable": smNewIPConfigEnableDisable,
       "chassisTopology": chassisTopology,
       "chassisResponseVersion": chassisResponseVersion,
       "chassisFlags": chassisFlags,
       "chassisName": chassisName,
       "chassisNoOfPBsSupported": chassisNoOfPBsSupported,
       "chassisNoOfSMsSupported": chassisNoOfSMsSupported,
       "chassisNoOfMMsSupported": chassisNoOfMMsSupported,
       "chassisNoOfPMsSupported": chassisNoOfPMsSupported,
       "chassisNoOfMTsSupported": chassisNoOfMTsSupported,
       "chassisNoOfBlowersSupported": chassisNoOfBlowersSupported,
       "chassisPBsInstalled": chassisPBsInstalled,
       "chassisSMsInstalled": chassisSMsInstalled,
       "chassisMMsInstalled": chassisMMsInstalled,
       "chassisPMsInstalled": chassisPMsInstalled,
       "chassisMTInstalled": chassisMTInstalled,
       "chassisBlowersInstalled": chassisBlowersInstalled,
       "chassisActiveMM": chassisActiveMM,
       "chassisKVMOwner": chassisKVMOwner,
       "chassisMediaTrayOwner": chassisMediaTrayOwner,
       "managementModule": managementModule,
       "mmStatusTable": mmStatusTable,
       "mmStatusEntry": mmStatusEntry,
       "mmStatusIndex": mmStatusIndex,
       "mmPresent": mmPresent,
       "mmExtIpAddress": mmExtIpAddress,
       "mmPrimary": mmPrimary,
       "firmwareUpdate": firmwareUpdate,
       "firmwareUpdateTarget": firmwareUpdateTarget,
       "firmwareUpdateTftpServer": firmwareUpdateTftpServer,
       "firmwareUpdateFileName": firmwareUpdateFileName,
       "firmwareUpdateStart": firmwareUpdateStart,
       "firmwareUpdateStatus": firmwareUpdateStatus,
       "ipmiManagement": ipmiManagement,
       "ipmiEnabled": ipmiEnabled}
)
