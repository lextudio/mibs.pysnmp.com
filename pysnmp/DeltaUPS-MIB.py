# SNMP MIB module (DeltaUPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DeltaUPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:35:46 2024
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

_Delta_ObjectIdentity = ObjectIdentity
delta = _Delta_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254)
)
_Ups_ObjectIdentity = ObjectIdentity
ups = _Ups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2)
)
_Upsv4_ObjectIdentity = ObjectIdentity
upsv4 = _Upsv4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4)
)
_DupsIdent_ObjectIdentity = ObjectIdentity
dupsIdent = _DupsIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 1)
)


class _DupsIdentManufacturer_Type(DisplayString):
    """Custom type dupsIdentManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DupsIdentManufacturer_Type.__name__ = "DisplayString"
_DupsIdentManufacturer_Object = MibScalar
dupsIdentManufacturer = _DupsIdentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 1, 1),
    _DupsIdentManufacturer_Type()
)
dupsIdentManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsIdentManufacturer.setStatus("mandatory")


class _DupsIdentModel_Type(DisplayString):
    """Custom type dupsIdentModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_DupsIdentModel_Type.__name__ = "DisplayString"
_DupsIdentModel_Object = MibScalar
dupsIdentModel = _DupsIdentModel_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 1, 2),
    _DupsIdentModel_Type()
)
dupsIdentModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsIdentModel.setStatus("mandatory")


class _DupsIdentUPSSoftwareVersion_Type(DisplayString):
    """Custom type dupsIdentUPSSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_DupsIdentUPSSoftwareVersion_Type.__name__ = "DisplayString"
_DupsIdentUPSSoftwareVersion_Object = MibScalar
dupsIdentUPSSoftwareVersion = _DupsIdentUPSSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 1, 3),
    _DupsIdentUPSSoftwareVersion_Type()
)
dupsIdentUPSSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsIdentUPSSoftwareVersion.setStatus("mandatory")


class _DupsIdentAgentSoftwareVersion_Type(DisplayString):
    """Custom type dupsIdentAgentSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_DupsIdentAgentSoftwareVersion_Type.__name__ = "DisplayString"
_DupsIdentAgentSoftwareVersion_Object = MibScalar
dupsIdentAgentSoftwareVersion = _DupsIdentAgentSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 1, 4),
    _DupsIdentAgentSoftwareVersion_Type()
)
dupsIdentAgentSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsIdentAgentSoftwareVersion.setStatus("mandatory")


class _DupsIdentName_Type(DisplayString):
    """Custom type dupsIdentName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_DupsIdentName_Type.__name__ = "DisplayString"
_DupsIdentName_Object = MibScalar
dupsIdentName = _DupsIdentName_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 1, 5),
    _DupsIdentName_Type()
)
dupsIdentName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dupsIdentName.setStatus("mandatory")


class _DupsAttachedDevices_Type(DisplayString):
    """Custom type dupsAttachedDevices based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_DupsAttachedDevices_Type.__name__ = "DisplayString"
_DupsAttachedDevices_Object = MibScalar
dupsAttachedDevices = _DupsAttachedDevices_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 1, 6),
    _DupsAttachedDevices_Type()
)
dupsAttachedDevices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dupsAttachedDevices.setStatus("mandatory")
_DupsRatingOutputVA_Type = Integer32
_DupsRatingOutputVA_Object = MibScalar
dupsRatingOutputVA = _DupsRatingOutputVA_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 1, 7),
    _DupsRatingOutputVA_Type()
)
dupsRatingOutputVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsRatingOutputVA.setStatus("mandatory")
_DupsRatingOutputVoltage_Type = Integer32
_DupsRatingOutputVoltage_Object = MibScalar
dupsRatingOutputVoltage = _DupsRatingOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 1, 8),
    _DupsRatingOutputVoltage_Type()
)
dupsRatingOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsRatingOutputVoltage.setStatus("mandatory")
_DupsRatingOutputFrequency_Type = Integer32
_DupsRatingOutputFrequency_Object = MibScalar
dupsRatingOutputFrequency = _DupsRatingOutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 1, 9),
    _DupsRatingOutputFrequency_Type()
)
dupsRatingOutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsRatingOutputFrequency.setStatus("mandatory")
_DupsRatingInputVoltage_Type = Integer32
_DupsRatingInputVoltage_Object = MibScalar
dupsRatingInputVoltage = _DupsRatingInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 1, 10),
    _DupsRatingInputVoltage_Type()
)
dupsRatingInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsRatingInputVoltage.setStatus("mandatory")
_DupsRatingInputFrequency_Type = Integer32
_DupsRatingInputFrequency_Object = MibScalar
dupsRatingInputFrequency = _DupsRatingInputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 1, 11),
    _DupsRatingInputFrequency_Type()
)
dupsRatingInputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsRatingInputFrequency.setStatus("mandatory")
_DupsRatingBatteryVoltage_Type = Integer32
_DupsRatingBatteryVoltage_Object = MibScalar
dupsRatingBatteryVoltage = _DupsRatingBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 1, 12),
    _DupsRatingBatteryVoltage_Type()
)
dupsRatingBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsRatingBatteryVoltage.setStatus("mandatory")
_DupsLowTransferVoltUpBound_Type = Integer32
_DupsLowTransferVoltUpBound_Object = MibScalar
dupsLowTransferVoltUpBound = _DupsLowTransferVoltUpBound_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 1, 13),
    _DupsLowTransferVoltUpBound_Type()
)
dupsLowTransferVoltUpBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsLowTransferVoltUpBound.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsLowTransferVoltUpBound.setUnits("Volt")
_DupsLowTransferVoltLowBound_Type = Integer32
_DupsLowTransferVoltLowBound_Object = MibScalar
dupsLowTransferVoltLowBound = _DupsLowTransferVoltLowBound_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 1, 14),
    _DupsLowTransferVoltLowBound_Type()
)
dupsLowTransferVoltLowBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsLowTransferVoltLowBound.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsLowTransferVoltLowBound.setUnits("Volt")
_DupsHighTransferVoltUpBound_Type = Integer32
_DupsHighTransferVoltUpBound_Object = MibScalar
dupsHighTransferVoltUpBound = _DupsHighTransferVoltUpBound_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 1, 15),
    _DupsHighTransferVoltUpBound_Type()
)
dupsHighTransferVoltUpBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsHighTransferVoltUpBound.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsHighTransferVoltUpBound.setUnits("Volt")
_DupsHighTransferVoltLowBound_Type = Integer32
_DupsHighTransferVoltLowBound_Object = MibScalar
dupsHighTransferVoltLowBound = _DupsHighTransferVoltLowBound_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 1, 16),
    _DupsHighTransferVoltLowBound_Type()
)
dupsHighTransferVoltLowBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsHighTransferVoltLowBound.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsHighTransferVoltLowBound.setUnits("Volt")
_DupsLowBattTime_Type = Integer32
_DupsLowBattTime_Object = MibScalar
dupsLowBattTime = _DupsLowBattTime_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 1, 17),
    _DupsLowBattTime_Type()
)
dupsLowBattTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsLowBattTime.setStatus("mandatory")
_DupsOutletRelays_Type = Integer32
_DupsOutletRelays_Object = MibScalar
dupsOutletRelays = _DupsOutletRelays_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 1, 18),
    _DupsOutletRelays_Type()
)
dupsOutletRelays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsOutletRelays.setStatus("mandatory")


class _DupsType_Type(Integer32):
    """Custom type dupsType based on Integer32"""
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
        *(("3phase", 4),
          ("line-interactive", 3),
          ("off-line", 2),
          ("on-line", 1),
          ("splite-phase", 5))
    )


_DupsType_Type.__name__ = "Integer32"
_DupsType_Object = MibScalar
dupsType = _DupsType_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 1, 19),
    _DupsType_Type()
)
dupsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsType.setStatus("mandatory")
_DupsControl_ObjectIdentity = ObjectIdentity
dupsControl = _DupsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 2)
)


class _DupsShutdownType_Type(Integer32):
    """Custom type dupsShutdownType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("output", 1),
          ("system", 2))
    )


_DupsShutdownType_Type.__name__ = "Integer32"
_DupsShutdownType_Object = MibScalar
dupsShutdownType = _DupsShutdownType_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 2, 1),
    _DupsShutdownType_Type()
)
dupsShutdownType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dupsShutdownType.setStatus("mandatory")


class _DupsAutoReboot_Type(Integer32):
    """Custom type dupsAutoReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_DupsAutoReboot_Type.__name__ = "Integer32"
_DupsAutoReboot_Object = MibScalar
dupsAutoReboot = _DupsAutoReboot_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 2, 2),
    _DupsAutoReboot_Type()
)
dupsAutoReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dupsAutoReboot.setStatus("mandatory")
_DupsShutdownAction_Type = Integer32
_DupsShutdownAction_Object = MibScalar
dupsShutdownAction = _DupsShutdownAction_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 2, 3),
    _DupsShutdownAction_Type()
)
dupsShutdownAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dupsShutdownAction.setStatus("mandatory")
_DupsRestartAction_Type = Integer32
_DupsRestartAction_Object = MibScalar
dupsRestartAction = _DupsRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 2, 4),
    _DupsRestartAction_Type()
)
dupsRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dupsRestartAction.setStatus("mandatory")
_DupsSetOutletRelay_Type = Integer32
_DupsSetOutletRelay_Object = MibScalar
dupsSetOutletRelay = _DupsSetOutletRelay_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 2, 5),
    _DupsSetOutletRelay_Type()
)
dupsSetOutletRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dupsSetOutletRelay.setStatus("mandatory")
_DupsRelayOffDelay_Type = Integer32
_DupsRelayOffDelay_Object = MibScalar
dupsRelayOffDelay = _DupsRelayOffDelay_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 2, 6),
    _DupsRelayOffDelay_Type()
)
dupsRelayOffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dupsRelayOffDelay.setStatus("mandatory")
_DupsRelayOnDelay_Type = Integer32
_DupsRelayOnDelay_Object = MibScalar
dupsRelayOnDelay = _DupsRelayOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 2, 7),
    _DupsRelayOnDelay_Type()
)
dupsRelayOnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dupsRelayOnDelay.setStatus("mandatory")
_DupsConfig_ObjectIdentity = ObjectIdentity
dupsConfig = _DupsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 3)
)


class _DupsConfigBuzzerAlarm_Type(Integer32):
    """Custom type dupsConfigBuzzerAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("silence", 2))
    )


_DupsConfigBuzzerAlarm_Type.__name__ = "Integer32"
_DupsConfigBuzzerAlarm_Object = MibScalar
dupsConfigBuzzerAlarm = _DupsConfigBuzzerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 3, 1),
    _DupsConfigBuzzerAlarm_Type()
)
dupsConfigBuzzerAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dupsConfigBuzzerAlarm.setStatus("mandatory")


class _DupsConfigBuzzerState_Type(Integer32):
    """Custom type dupsConfigBuzzerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_DupsConfigBuzzerState_Type.__name__ = "Integer32"
_DupsConfigBuzzerState_Object = MibScalar
dupsConfigBuzzerState = _DupsConfigBuzzerState_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 3, 2),
    _DupsConfigBuzzerState_Type()
)
dupsConfigBuzzerState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dupsConfigBuzzerState.setStatus("mandatory")


class _DupsConfigSensitivity_Type(Integer32):
    """Custom type dupsConfigSensitivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low", 2),
          ("normal", 0),
          ("reduced", 1))
    )


_DupsConfigSensitivity_Type.__name__ = "Integer32"
_DupsConfigSensitivity_Object = MibScalar
dupsConfigSensitivity = _DupsConfigSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 3, 3),
    _DupsConfigSensitivity_Type()
)
dupsConfigSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dupsConfigSensitivity.setStatus("mandatory")
_DupsConfigLowVoltageTransferPoint_Type = Integer32
_DupsConfigLowVoltageTransferPoint_Object = MibScalar
dupsConfigLowVoltageTransferPoint = _DupsConfigLowVoltageTransferPoint_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 3, 4),
    _DupsConfigLowVoltageTransferPoint_Type()
)
dupsConfigLowVoltageTransferPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dupsConfigLowVoltageTransferPoint.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsConfigLowVoltageTransferPoint.setUnits("Volt")
_DupsConfigHighVoltageTransferPoint_Type = Integer32
_DupsConfigHighVoltageTransferPoint_Object = MibScalar
dupsConfigHighVoltageTransferPoint = _DupsConfigHighVoltageTransferPoint_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 3, 5),
    _DupsConfigHighVoltageTransferPoint_Type()
)
dupsConfigHighVoltageTransferPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dupsConfigHighVoltageTransferPoint.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsConfigHighVoltageTransferPoint.setUnits("Volt")
_DupsConfigShutdownOSDelay_Type = Integer32
_DupsConfigShutdownOSDelay_Object = MibScalar
dupsConfigShutdownOSDelay = _DupsConfigShutdownOSDelay_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 3, 6),
    _DupsConfigShutdownOSDelay_Type()
)
dupsConfigShutdownOSDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dupsConfigShutdownOSDelay.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsConfigShutdownOSDelay.setUnits("Second")
_DupsConfigUPSBootDelay_Type = Integer32
_DupsConfigUPSBootDelay_Object = MibScalar
dupsConfigUPSBootDelay = _DupsConfigUPSBootDelay_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 3, 7),
    _DupsConfigUPSBootDelay_Type()
)
dupsConfigUPSBootDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dupsConfigUPSBootDelay.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsConfigUPSBootDelay.setUnits("Second")
_DupsConfigExternalBatteryPack_Type = Integer32
_DupsConfigExternalBatteryPack_Object = MibScalar
dupsConfigExternalBatteryPack = _DupsConfigExternalBatteryPack_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 3, 8),
    _DupsConfigExternalBatteryPack_Type()
)
dupsConfigExternalBatteryPack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dupsConfigExternalBatteryPack.setStatus("mandatory")
_DupsInput_ObjectIdentity = ObjectIdentity
dupsInput = _DupsInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 4)
)
_DupsInputNumLines_Type = Integer32
_DupsInputNumLines_Object = MibScalar
dupsInputNumLines = _DupsInputNumLines_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 4, 1),
    _DupsInputNumLines_Type()
)
dupsInputNumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsInputNumLines.setStatus("mandatory")
_DupsInputFrequency1_Type = Integer32
_DupsInputFrequency1_Object = MibScalar
dupsInputFrequency1 = _DupsInputFrequency1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 4, 2),
    _DupsInputFrequency1_Type()
)
dupsInputFrequency1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsInputFrequency1.setStatus("mandatory")
_DupsInputVoltage1_Type = Integer32
_DupsInputVoltage1_Object = MibScalar
dupsInputVoltage1 = _DupsInputVoltage1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 4, 3),
    _DupsInputVoltage1_Type()
)
dupsInputVoltage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsInputVoltage1.setStatus("mandatory")
_DupsInputCurrent1_Type = Integer32
_DupsInputCurrent1_Object = MibScalar
dupsInputCurrent1 = _DupsInputCurrent1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 4, 4),
    _DupsInputCurrent1_Type()
)
dupsInputCurrent1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsInputCurrent1.setStatus("mandatory")
_DupsInputFrequency2_Type = Integer32
_DupsInputFrequency2_Object = MibScalar
dupsInputFrequency2 = _DupsInputFrequency2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 4, 5),
    _DupsInputFrequency2_Type()
)
dupsInputFrequency2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsInputFrequency2.setStatus("mandatory")
_DupsInputVoltage2_Type = Integer32
_DupsInputVoltage2_Object = MibScalar
dupsInputVoltage2 = _DupsInputVoltage2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 4, 6),
    _DupsInputVoltage2_Type()
)
dupsInputVoltage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsInputVoltage2.setStatus("mandatory")
_DupsInputCurrent2_Type = Integer32
_DupsInputCurrent2_Object = MibScalar
dupsInputCurrent2 = _DupsInputCurrent2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 4, 7),
    _DupsInputCurrent2_Type()
)
dupsInputCurrent2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsInputCurrent2.setStatus("mandatory")
_DupsInputFrequency3_Type = Integer32
_DupsInputFrequency3_Object = MibScalar
dupsInputFrequency3 = _DupsInputFrequency3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 4, 8),
    _DupsInputFrequency3_Type()
)
dupsInputFrequency3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsInputFrequency3.setStatus("mandatory")
_DupsInputVoltage3_Type = Integer32
_DupsInputVoltage3_Object = MibScalar
dupsInputVoltage3 = _DupsInputVoltage3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 4, 9),
    _DupsInputVoltage3_Type()
)
dupsInputVoltage3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsInputVoltage3.setStatus("mandatory")
_DupsInputCurrent3_Type = Integer32
_DupsInputCurrent3_Object = MibScalar
dupsInputCurrent3 = _DupsInputCurrent3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 4, 10),
    _DupsInputCurrent3_Type()
)
dupsInputCurrent3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsInputCurrent3.setStatus("mandatory")
_DupsOutput_ObjectIdentity = ObjectIdentity
dupsOutput = _DupsOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 5)
)


class _DupsOutputSource_Type(Integer32):
    """Custom type dupsOutputSource based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("battery", 1),
          ("boosting", 4),
          ("bypass", 2),
          ("manualBypass", 5),
          ("none", 7),
          ("normal", 0),
          ("other", 6),
          ("reducing", 3))
    )


_DupsOutputSource_Type.__name__ = "Integer32"
_DupsOutputSource_Object = MibScalar
dupsOutputSource = _DupsOutputSource_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 5, 1),
    _DupsOutputSource_Type()
)
dupsOutputSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsOutputSource.setStatus("mandatory")
_DupsOutputFrequency_Type = Integer32
_DupsOutputFrequency_Object = MibScalar
dupsOutputFrequency = _DupsOutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 5, 2),
    _DupsOutputFrequency_Type()
)
dupsOutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsOutputFrequency.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsOutputFrequency.setUnits("0.1 Hertz")
_DupsOutputNumLines_Type = Integer32
_DupsOutputNumLines_Object = MibScalar
dupsOutputNumLines = _DupsOutputNumLines_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 5, 3),
    _DupsOutputNumLines_Type()
)
dupsOutputNumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsOutputNumLines.setStatus("mandatory")
_DupsOutputVoltage1_Type = Integer32
_DupsOutputVoltage1_Object = MibScalar
dupsOutputVoltage1 = _DupsOutputVoltage1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 5, 4),
    _DupsOutputVoltage1_Type()
)
dupsOutputVoltage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsOutputVoltage1.setStatus("mandatory")
_DupsOutputCurrent1_Type = Integer32
_DupsOutputCurrent1_Object = MibScalar
dupsOutputCurrent1 = _DupsOutputCurrent1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 5, 5),
    _DupsOutputCurrent1_Type()
)
dupsOutputCurrent1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsOutputCurrent1.setStatus("mandatory")
_DupsOutputPower1_Type = Integer32
_DupsOutputPower1_Object = MibScalar
dupsOutputPower1 = _DupsOutputPower1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 5, 6),
    _DupsOutputPower1_Type()
)
dupsOutputPower1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsOutputPower1.setStatus("mandatory")
_DupsOutputLoad1_Type = Integer32
_DupsOutputLoad1_Object = MibScalar
dupsOutputLoad1 = _DupsOutputLoad1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 5, 7),
    _DupsOutputLoad1_Type()
)
dupsOutputLoad1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsOutputLoad1.setStatus("mandatory")
_DupsOutputVoltage2_Type = Integer32
_DupsOutputVoltage2_Object = MibScalar
dupsOutputVoltage2 = _DupsOutputVoltage2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 5, 8),
    _DupsOutputVoltage2_Type()
)
dupsOutputVoltage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsOutputVoltage2.setStatus("mandatory")
_DupsOutputCurrent2_Type = Integer32
_DupsOutputCurrent2_Object = MibScalar
dupsOutputCurrent2 = _DupsOutputCurrent2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 5, 9),
    _DupsOutputCurrent2_Type()
)
dupsOutputCurrent2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsOutputCurrent2.setStatus("mandatory")
_DupsOutputPower2_Type = Integer32
_DupsOutputPower2_Object = MibScalar
dupsOutputPower2 = _DupsOutputPower2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 5, 10),
    _DupsOutputPower2_Type()
)
dupsOutputPower2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsOutputPower2.setStatus("mandatory")
_DupsOutputLoad2_Type = Integer32
_DupsOutputLoad2_Object = MibScalar
dupsOutputLoad2 = _DupsOutputLoad2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 5, 11),
    _DupsOutputLoad2_Type()
)
dupsOutputLoad2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsOutputLoad2.setStatus("mandatory")
_DupsOutputVoltage3_Type = Integer32
_DupsOutputVoltage3_Object = MibScalar
dupsOutputVoltage3 = _DupsOutputVoltage3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 5, 12),
    _DupsOutputVoltage3_Type()
)
dupsOutputVoltage3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsOutputVoltage3.setStatus("mandatory")
_DupsOutputCurrent3_Type = Integer32
_DupsOutputCurrent3_Object = MibScalar
dupsOutputCurrent3 = _DupsOutputCurrent3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 5, 13),
    _DupsOutputCurrent3_Type()
)
dupsOutputCurrent3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsOutputCurrent3.setStatus("mandatory")
_DupsOutputPower3_Type = Integer32
_DupsOutputPower3_Object = MibScalar
dupsOutputPower3 = _DupsOutputPower3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 5, 14),
    _DupsOutputPower3_Type()
)
dupsOutputPower3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsOutputPower3.setStatus("mandatory")
_DupsOutputLoad3_Type = Integer32
_DupsOutputLoad3_Object = MibScalar
dupsOutputLoad3 = _DupsOutputLoad3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 5, 15),
    _DupsOutputLoad3_Type()
)
dupsOutputLoad3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsOutputLoad3.setStatus("mandatory")
_DupsBypass_ObjectIdentity = ObjectIdentity
dupsBypass = _DupsBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 6)
)
_DupsBypassFrequency_Type = Integer32
_DupsBypassFrequency_Object = MibScalar
dupsBypassFrequency = _DupsBypassFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 6, 1),
    _DupsBypassFrequency_Type()
)
dupsBypassFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsBypassFrequency.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsBypassFrequency.setUnits("0.1 Hertz")
_DupsBypassNumLines_Type = Integer32
_DupsBypassNumLines_Object = MibScalar
dupsBypassNumLines = _DupsBypassNumLines_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 6, 2),
    _DupsBypassNumLines_Type()
)
dupsBypassNumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsBypassNumLines.setStatus("mandatory")
_DupsBypassVoltage1_Type = Integer32
_DupsBypassVoltage1_Object = MibScalar
dupsBypassVoltage1 = _DupsBypassVoltage1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 6, 3),
    _DupsBypassVoltage1_Type()
)
dupsBypassVoltage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsBypassVoltage1.setStatus("mandatory")
_DupsBypassCurrent1_Type = Integer32
_DupsBypassCurrent1_Object = MibScalar
dupsBypassCurrent1 = _DupsBypassCurrent1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 6, 4),
    _DupsBypassCurrent1_Type()
)
dupsBypassCurrent1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsBypassCurrent1.setStatus("mandatory")
_DupsBypassPower1_Type = Integer32
_DupsBypassPower1_Object = MibScalar
dupsBypassPower1 = _DupsBypassPower1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 6, 5),
    _DupsBypassPower1_Type()
)
dupsBypassPower1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsBypassPower1.setStatus("mandatory")
_DupsBypassVoltage2_Type = Integer32
_DupsBypassVoltage2_Object = MibScalar
dupsBypassVoltage2 = _DupsBypassVoltage2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 6, 6),
    _DupsBypassVoltage2_Type()
)
dupsBypassVoltage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsBypassVoltage2.setStatus("mandatory")
_DupsBypassCurrent2_Type = Integer32
_DupsBypassCurrent2_Object = MibScalar
dupsBypassCurrent2 = _DupsBypassCurrent2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 6, 7),
    _DupsBypassCurrent2_Type()
)
dupsBypassCurrent2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsBypassCurrent2.setStatus("mandatory")
_DupsBypassPower2_Type = Integer32
_DupsBypassPower2_Object = MibScalar
dupsBypassPower2 = _DupsBypassPower2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 6, 8),
    _DupsBypassPower2_Type()
)
dupsBypassPower2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsBypassPower2.setStatus("mandatory")
_DupsBypassVoltage3_Type = Integer32
_DupsBypassVoltage3_Object = MibScalar
dupsBypassVoltage3 = _DupsBypassVoltage3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 6, 9),
    _DupsBypassVoltage3_Type()
)
dupsBypassVoltage3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsBypassVoltage3.setStatus("mandatory")
_DupsBypassCurrent3_Type = Integer32
_DupsBypassCurrent3_Object = MibScalar
dupsBypassCurrent3 = _DupsBypassCurrent3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 6, 10),
    _DupsBypassCurrent3_Type()
)
dupsBypassCurrent3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsBypassCurrent3.setStatus("mandatory")
_DupsBypassPower3_Type = Integer32
_DupsBypassPower3_Object = MibScalar
dupsBypassPower3 = _DupsBypassPower3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 6, 11),
    _DupsBypassPower3_Type()
)
dupsBypassPower3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsBypassPower3.setStatus("mandatory")
_DupsBattery_ObjectIdentity = ObjectIdentity
dupsBattery = _DupsBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 7)
)


class _DupsBatteryCondiction_Type(Integer32):
    """Custom type dupsBatteryCondiction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("good", 0),
          ("replace", 2),
          ("weak", 1))
    )


_DupsBatteryCondiction_Type.__name__ = "Integer32"
_DupsBatteryCondiction_Object = MibScalar
dupsBatteryCondiction = _DupsBatteryCondiction_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 7, 1),
    _DupsBatteryCondiction_Type()
)
dupsBatteryCondiction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsBatteryCondiction.setStatus("mandatory")


class _DupsBatteryStatus_Type(Integer32):
    """Custom type dupsBatteryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("depleted", 2),
          ("low", 1),
          ("ok", 0))
    )


_DupsBatteryStatus_Type.__name__ = "Integer32"
_DupsBatteryStatus_Object = MibScalar
dupsBatteryStatus = _DupsBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 7, 2),
    _DupsBatteryStatus_Type()
)
dupsBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsBatteryStatus.setStatus("mandatory")


class _DupsBatteryCharge_Type(Integer32):
    """Custom type dupsBatteryCharge based on Integer32"""
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
        *(("charging", 1),
          ("discharging", 3),
          ("floating", 0),
          ("resting", 2))
    )


_DupsBatteryCharge_Type.__name__ = "Integer32"
_DupsBatteryCharge_Object = MibScalar
dupsBatteryCharge = _DupsBatteryCharge_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 7, 3),
    _DupsBatteryCharge_Type()
)
dupsBatteryCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsBatteryCharge.setStatus("mandatory")
_DupsSecondsOnBattery_Type = Integer32
_DupsSecondsOnBattery_Object = MibScalar
dupsSecondsOnBattery = _DupsSecondsOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 7, 4),
    _DupsSecondsOnBattery_Type()
)
dupsSecondsOnBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsSecondsOnBattery.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsSecondsOnBattery.setUnits("seconds")
_DupsBatteryEstimatedTime_Type = Integer32
_DupsBatteryEstimatedTime_Object = MibScalar
dupsBatteryEstimatedTime = _DupsBatteryEstimatedTime_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 7, 5),
    _DupsBatteryEstimatedTime_Type()
)
dupsBatteryEstimatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsBatteryEstimatedTime.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsBatteryEstimatedTime.setUnits("minutes")
_DupsBatteryVoltage_Type = Integer32
_DupsBatteryVoltage_Object = MibScalar
dupsBatteryVoltage = _DupsBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 7, 6),
    _DupsBatteryVoltage_Type()
)
dupsBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsBatteryVoltage.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsBatteryVoltage.setUnits("0.1 Volt DC")
_DupsBatteryCurrent_Type = Integer32
_DupsBatteryCurrent_Object = MibScalar
dupsBatteryCurrent = _DupsBatteryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 7, 7),
    _DupsBatteryCurrent_Type()
)
dupsBatteryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsBatteryCurrent.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsBatteryCurrent.setUnits("0.1 Amp DC")


class _DupsBatteryCapacity_Type(Integer32):
    """Custom type dupsBatteryCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DupsBatteryCapacity_Type.__name__ = "Integer32"
_DupsBatteryCapacity_Object = MibScalar
dupsBatteryCapacity = _DupsBatteryCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 7, 8),
    _DupsBatteryCapacity_Type()
)
dupsBatteryCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsBatteryCapacity.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsBatteryCapacity.setUnits("percent")
_DupsTemperature_Type = Integer32
_DupsTemperature_Object = MibScalar
dupsTemperature = _DupsTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 7, 9),
    _DupsTemperature_Type()
)
dupsTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsTemperature.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsTemperature.setUnits("degrees Centigrade")


class _DupsLastReplaceDate_Type(DisplayString):
    """Custom type dupsLastReplaceDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DupsLastReplaceDate_Type.__name__ = "DisplayString"
_DupsLastReplaceDate_Object = MibScalar
dupsLastReplaceDate = _DupsLastReplaceDate_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 7, 10),
    _DupsLastReplaceDate_Type()
)
dupsLastReplaceDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsLastReplaceDate.setStatus("mandatory")


class _DupsNextReplaceDate_Type(DisplayString):
    """Custom type dupsNextReplaceDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DupsNextReplaceDate_Type.__name__ = "DisplayString"
_DupsNextReplaceDate_Object = MibScalar
dupsNextReplaceDate = _DupsNextReplaceDate_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 7, 11),
    _DupsNextReplaceDate_Type()
)
dupsNextReplaceDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsNextReplaceDate.setStatus("mandatory")
_DupsTest_ObjectIdentity = ObjectIdentity
dupsTest = _DupsTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 8)
)


class _DupsTestType_Type(Integer32):
    """Custom type dupsTestType based on Integer32"""
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
        *(("abort", 0),
          ("batteryTest", 2),
          ("generalTest", 1),
          ("testFor10sec", 3),
          ("testUntilBattlow", 4))
    )


_DupsTestType_Type.__name__ = "Integer32"
_DupsTestType_Object = MibScalar
dupsTestType = _DupsTestType_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 8, 1),
    _DupsTestType_Type()
)
dupsTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dupsTestType.setStatus("mandatory")


class _DupsTestResultsSummary_Type(Integer32):
    """Custom type dupsTestResultsSummary based on Integer32"""
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
        *(("batteryTestFail", 4),
          ("deepBatteryTestFail", 5),
          ("donePass", 1),
          ("generalTestFail", 3),
          ("inProgress", 2),
          ("noTestsInitiated", 0))
    )


_DupsTestResultsSummary_Type.__name__ = "Integer32"
_DupsTestResultsSummary_Object = MibScalar
dupsTestResultsSummary = _DupsTestResultsSummary_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 8, 2),
    _DupsTestResultsSummary_Type()
)
dupsTestResultsSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsTestResultsSummary.setStatus("mandatory")


class _DupsTestResultsDetail_Type(DisplayString):
    """Custom type dupsTestResultsDetail based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DupsTestResultsDetail_Type.__name__ = "DisplayString"
_DupsTestResultsDetail_Object = MibScalar
dupsTestResultsDetail = _DupsTestResultsDetail_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 8, 3),
    _DupsTestResultsDetail_Type()
)
dupsTestResultsDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsTestResultsDetail.setStatus("mandatory")
_DupsAlarm_ObjectIdentity = ObjectIdentity
dupsAlarm = _DupsAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 9)
)


class _DupsAlarmDisconnect_Type(Integer32):
    """Custom type dupsAlarmDisconnect based on Integer32"""
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


_DupsAlarmDisconnect_Type.__name__ = "Integer32"
_DupsAlarmDisconnect_Object = MibScalar
dupsAlarmDisconnect = _DupsAlarmDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 9, 1),
    _DupsAlarmDisconnect_Type()
)
dupsAlarmDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmDisconnect.setStatus("mandatory")


class _DupsAlarmPowerFail_Type(Integer32):
    """Custom type dupsAlarmPowerFail based on Integer32"""
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


_DupsAlarmPowerFail_Type.__name__ = "Integer32"
_DupsAlarmPowerFail_Object = MibScalar
dupsAlarmPowerFail = _DupsAlarmPowerFail_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 9, 2),
    _DupsAlarmPowerFail_Type()
)
dupsAlarmPowerFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmPowerFail.setStatus("mandatory")


class _DupsAlarmBatteryLow_Type(Integer32):
    """Custom type dupsAlarmBatteryLow based on Integer32"""
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


_DupsAlarmBatteryLow_Type.__name__ = "Integer32"
_DupsAlarmBatteryLow_Object = MibScalar
dupsAlarmBatteryLow = _DupsAlarmBatteryLow_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 9, 3),
    _DupsAlarmBatteryLow_Type()
)
dupsAlarmBatteryLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmBatteryLow.setStatus("mandatory")


class _DupsAlarmLoadWarning_Type(Integer32):
    """Custom type dupsAlarmLoadWarning based on Integer32"""
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


_DupsAlarmLoadWarning_Type.__name__ = "Integer32"
_DupsAlarmLoadWarning_Object = MibScalar
dupsAlarmLoadWarning = _DupsAlarmLoadWarning_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 9, 4),
    _DupsAlarmLoadWarning_Type()
)
dupsAlarmLoadWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmLoadWarning.setStatus("mandatory")


class _DupsAlarmLoadSeverity_Type(Integer32):
    """Custom type dupsAlarmLoadSeverity based on Integer32"""
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


_DupsAlarmLoadSeverity_Type.__name__ = "Integer32"
_DupsAlarmLoadSeverity_Object = MibScalar
dupsAlarmLoadSeverity = _DupsAlarmLoadSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 9, 5),
    _DupsAlarmLoadSeverity_Type()
)
dupsAlarmLoadSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmLoadSeverity.setStatus("mandatory")


class _DupsAlarmLoadOnBypass_Type(Integer32):
    """Custom type dupsAlarmLoadOnBypass based on Integer32"""
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


_DupsAlarmLoadOnBypass_Type.__name__ = "Integer32"
_DupsAlarmLoadOnBypass_Object = MibScalar
dupsAlarmLoadOnBypass = _DupsAlarmLoadOnBypass_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 9, 6),
    _DupsAlarmLoadOnBypass_Type()
)
dupsAlarmLoadOnBypass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmLoadOnBypass.setStatus("mandatory")


class _DupsAlarmUPSFault_Type(Integer32):
    """Custom type dupsAlarmUPSFault based on Integer32"""
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


_DupsAlarmUPSFault_Type.__name__ = "Integer32"
_DupsAlarmUPSFault_Object = MibScalar
dupsAlarmUPSFault = _DupsAlarmUPSFault_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 9, 7),
    _DupsAlarmUPSFault_Type()
)
dupsAlarmUPSFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmUPSFault.setStatus("mandatory")


class _DupsAlarmBatteryGroundFault_Type(Integer32):
    """Custom type dupsAlarmBatteryGroundFault based on Integer32"""
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


_DupsAlarmBatteryGroundFault_Type.__name__ = "Integer32"
_DupsAlarmBatteryGroundFault_Object = MibScalar
dupsAlarmBatteryGroundFault = _DupsAlarmBatteryGroundFault_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 9, 8),
    _DupsAlarmBatteryGroundFault_Type()
)
dupsAlarmBatteryGroundFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmBatteryGroundFault.setStatus("mandatory")


class _DupsAlarmTestInProgress_Type(Integer32):
    """Custom type dupsAlarmTestInProgress based on Integer32"""
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


_DupsAlarmTestInProgress_Type.__name__ = "Integer32"
_DupsAlarmTestInProgress_Object = MibScalar
dupsAlarmTestInProgress = _DupsAlarmTestInProgress_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 9, 9),
    _DupsAlarmTestInProgress_Type()
)
dupsAlarmTestInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmTestInProgress.setStatus("mandatory")


class _DupsAlarmBatteryTestFail_Type(Integer32):
    """Custom type dupsAlarmBatteryTestFail based on Integer32"""
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


_DupsAlarmBatteryTestFail_Type.__name__ = "Integer32"
_DupsAlarmBatteryTestFail_Object = MibScalar
dupsAlarmBatteryTestFail = _DupsAlarmBatteryTestFail_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 9, 10),
    _DupsAlarmBatteryTestFail_Type()
)
dupsAlarmBatteryTestFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmBatteryTestFail.setStatus("mandatory")


class _DupsAlarmFuseFailure_Type(Integer32):
    """Custom type dupsAlarmFuseFailure based on Integer32"""
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


_DupsAlarmFuseFailure_Type.__name__ = "Integer32"
_DupsAlarmFuseFailure_Object = MibScalar
dupsAlarmFuseFailure = _DupsAlarmFuseFailure_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 9, 11),
    _DupsAlarmFuseFailure_Type()
)
dupsAlarmFuseFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmFuseFailure.setStatus("mandatory")


class _DupsAlarmOutputOverload_Type(Integer32):
    """Custom type dupsAlarmOutputOverload based on Integer32"""
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


_DupsAlarmOutputOverload_Type.__name__ = "Integer32"
_DupsAlarmOutputOverload_Object = MibScalar
dupsAlarmOutputOverload = _DupsAlarmOutputOverload_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 9, 12),
    _DupsAlarmOutputOverload_Type()
)
dupsAlarmOutputOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmOutputOverload.setStatus("mandatory")


class _DupsAlarmOutputOverCurrent_Type(Integer32):
    """Custom type dupsAlarmOutputOverCurrent based on Integer32"""
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


_DupsAlarmOutputOverCurrent_Type.__name__ = "Integer32"
_DupsAlarmOutputOverCurrent_Object = MibScalar
dupsAlarmOutputOverCurrent = _DupsAlarmOutputOverCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 9, 13),
    _DupsAlarmOutputOverCurrent_Type()
)
dupsAlarmOutputOverCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmOutputOverCurrent.setStatus("mandatory")


class _DupsAlarmInverterAbnormal_Type(Integer32):
    """Custom type dupsAlarmInverterAbnormal based on Integer32"""
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


_DupsAlarmInverterAbnormal_Type.__name__ = "Integer32"
_DupsAlarmInverterAbnormal_Object = MibScalar
dupsAlarmInverterAbnormal = _DupsAlarmInverterAbnormal_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 9, 14),
    _DupsAlarmInverterAbnormal_Type()
)
dupsAlarmInverterAbnormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmInverterAbnormal.setStatus("mandatory")


class _DupsAlarmRectifierAbnormal_Type(Integer32):
    """Custom type dupsAlarmRectifierAbnormal based on Integer32"""
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


_DupsAlarmRectifierAbnormal_Type.__name__ = "Integer32"
_DupsAlarmRectifierAbnormal_Object = MibScalar
dupsAlarmRectifierAbnormal = _DupsAlarmRectifierAbnormal_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 9, 15),
    _DupsAlarmRectifierAbnormal_Type()
)
dupsAlarmRectifierAbnormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmRectifierAbnormal.setStatus("mandatory")


class _DupsAlarmReserveAbnormal_Type(Integer32):
    """Custom type dupsAlarmReserveAbnormal based on Integer32"""
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


_DupsAlarmReserveAbnormal_Type.__name__ = "Integer32"
_DupsAlarmReserveAbnormal_Object = MibScalar
dupsAlarmReserveAbnormal = _DupsAlarmReserveAbnormal_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 9, 16),
    _DupsAlarmReserveAbnormal_Type()
)
dupsAlarmReserveAbnormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmReserveAbnormal.setStatus("mandatory")


class _DupsAlarmLoadOnReserve_Type(Integer32):
    """Custom type dupsAlarmLoadOnReserve based on Integer32"""
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


_DupsAlarmLoadOnReserve_Type.__name__ = "Integer32"
_DupsAlarmLoadOnReserve_Object = MibScalar
dupsAlarmLoadOnReserve = _DupsAlarmLoadOnReserve_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 9, 17),
    _DupsAlarmLoadOnReserve_Type()
)
dupsAlarmLoadOnReserve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmLoadOnReserve.setStatus("mandatory")


class _DupsAlarmOverTemperature_Type(Integer32):
    """Custom type dupsAlarmOverTemperature based on Integer32"""
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


_DupsAlarmOverTemperature_Type.__name__ = "Integer32"
_DupsAlarmOverTemperature_Object = MibScalar
dupsAlarmOverTemperature = _DupsAlarmOverTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 9, 18),
    _DupsAlarmOverTemperature_Type()
)
dupsAlarmOverTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmOverTemperature.setStatus("mandatory")


class _DupsAlarmOutputBad_Type(Integer32):
    """Custom type dupsAlarmOutputBad based on Integer32"""
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


_DupsAlarmOutputBad_Type.__name__ = "Integer32"
_DupsAlarmOutputBad_Object = MibScalar
dupsAlarmOutputBad = _DupsAlarmOutputBad_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 9, 19),
    _DupsAlarmOutputBad_Type()
)
dupsAlarmOutputBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmOutputBad.setStatus("mandatory")


class _DupsAlarmBypassBad_Type(Integer32):
    """Custom type dupsAlarmBypassBad based on Integer32"""
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


_DupsAlarmBypassBad_Type.__name__ = "Integer32"
_DupsAlarmBypassBad_Object = MibScalar
dupsAlarmBypassBad = _DupsAlarmBypassBad_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 9, 20),
    _DupsAlarmBypassBad_Type()
)
dupsAlarmBypassBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmBypassBad.setStatus("mandatory")


class _DupsAlarmUPSOff_Type(Integer32):
    """Custom type dupsAlarmUPSOff based on Integer32"""
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


_DupsAlarmUPSOff_Type.__name__ = "Integer32"
_DupsAlarmUPSOff_Object = MibScalar
dupsAlarmUPSOff = _DupsAlarmUPSOff_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 9, 21),
    _DupsAlarmUPSOff_Type()
)
dupsAlarmUPSOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmUPSOff.setStatus("mandatory")


class _DupsAlarmChargerFail_Type(Integer32):
    """Custom type dupsAlarmChargerFail based on Integer32"""
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


_DupsAlarmChargerFail_Type.__name__ = "Integer32"
_DupsAlarmChargerFail_Object = MibScalar
dupsAlarmChargerFail = _DupsAlarmChargerFail_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 9, 22),
    _DupsAlarmChargerFail_Type()
)
dupsAlarmChargerFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmChargerFail.setStatus("mandatory")


class _DupsAlarmFanFail_Type(Integer32):
    """Custom type dupsAlarmFanFail based on Integer32"""
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


_DupsAlarmFanFail_Type.__name__ = "Integer32"
_DupsAlarmFanFail_Object = MibScalar
dupsAlarmFanFail = _DupsAlarmFanFail_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 9, 23),
    _DupsAlarmFanFail_Type()
)
dupsAlarmFanFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmFanFail.setStatus("mandatory")


class _DupsAlarmEconomicMode_Type(Integer32):
    """Custom type dupsAlarmEconomicMode based on Integer32"""
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


_DupsAlarmEconomicMode_Type.__name__ = "Integer32"
_DupsAlarmEconomicMode_Object = MibScalar
dupsAlarmEconomicMode = _DupsAlarmEconomicMode_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 9, 24),
    _DupsAlarmEconomicMode_Type()
)
dupsAlarmEconomicMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmEconomicMode.setStatus("mandatory")


class _DupsAlarmOutputOff_Type(Integer32):
    """Custom type dupsAlarmOutputOff based on Integer32"""
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


_DupsAlarmOutputOff_Type.__name__ = "Integer32"
_DupsAlarmOutputOff_Object = MibScalar
dupsAlarmOutputOff = _DupsAlarmOutputOff_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 9, 25),
    _DupsAlarmOutputOff_Type()
)
dupsAlarmOutputOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmOutputOff.setStatus("mandatory")


class _DupsAlarmSmartShutdown_Type(Integer32):
    """Custom type dupsAlarmSmartShutdown based on Integer32"""
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


_DupsAlarmSmartShutdown_Type.__name__ = "Integer32"
_DupsAlarmSmartShutdown_Object = MibScalar
dupsAlarmSmartShutdown = _DupsAlarmSmartShutdown_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 9, 26),
    _DupsAlarmSmartShutdown_Type()
)
dupsAlarmSmartShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmSmartShutdown.setStatus("mandatory")


class _DupsAlarmEmergencyPowerOff_Type(Integer32):
    """Custom type dupsAlarmEmergencyPowerOff based on Integer32"""
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


_DupsAlarmEmergencyPowerOff_Type.__name__ = "Integer32"
_DupsAlarmEmergencyPowerOff_Object = MibScalar
dupsAlarmEmergencyPowerOff = _DupsAlarmEmergencyPowerOff_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 9, 27),
    _DupsAlarmEmergencyPowerOff_Type()
)
dupsAlarmEmergencyPowerOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmEmergencyPowerOff.setStatus("mandatory")


class _DupsAlarmUPSShutdown_Type(Integer32):
    """Custom type dupsAlarmUPSShutdown based on Integer32"""
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


_DupsAlarmUPSShutdown_Type.__name__ = "Integer32"
_DupsAlarmUPSShutdown_Object = MibScalar
dupsAlarmUPSShutdown = _DupsAlarmUPSShutdown_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 9, 28),
    _DupsAlarmUPSShutdown_Type()
)
dupsAlarmUPSShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmUPSShutdown.setStatus("mandatory")
_DupsEnvironment_ObjectIdentity = ObjectIdentity
dupsEnvironment = _DupsEnvironment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 10)
)
_DupsEnvTemperature_Type = Integer32
_DupsEnvTemperature_Object = MibScalar
dupsEnvTemperature = _DupsEnvTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 10, 1),
    _DupsEnvTemperature_Type()
)
dupsEnvTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsEnvTemperature.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsEnvTemperature.setUnits("degrees Centigrade")
_DupsEnvHumidity_Type = Integer32
_DupsEnvHumidity_Object = MibScalar
dupsEnvHumidity = _DupsEnvHumidity_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 10, 2),
    _DupsEnvHumidity_Type()
)
dupsEnvHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsEnvHumidity.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsEnvHumidity.setUnits("percentage")
_DupsEnvSetTemperatureLimit_Type = Integer32
_DupsEnvSetTemperatureLimit_Object = MibScalar
dupsEnvSetTemperatureLimit = _DupsEnvSetTemperatureLimit_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 10, 3),
    _DupsEnvSetTemperatureLimit_Type()
)
dupsEnvSetTemperatureLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dupsEnvSetTemperatureLimit.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsEnvSetTemperatureLimit.setUnits("degrees Centigrade")
_DupsEnvSetHumidityLimit_Type = Integer32
_DupsEnvSetHumidityLimit_Object = MibScalar
dupsEnvSetHumidityLimit = _DupsEnvSetHumidityLimit_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 10, 4),
    _DupsEnvSetHumidityLimit_Type()
)
dupsEnvSetHumidityLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dupsEnvSetHumidityLimit.setStatus("mandatory")
if mibBuilder.loadTexts:
    dupsEnvSetHumidityLimit.setUnits("percentage")


class _DupsEnvSetEnvRelay1_Type(Integer32):
    """Custom type dupsEnvSetEnvRelay1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normalClose", 1),
          ("normalOpen", 0))
    )


_DupsEnvSetEnvRelay1_Type.__name__ = "Integer32"
_DupsEnvSetEnvRelay1_Object = MibScalar
dupsEnvSetEnvRelay1 = _DupsEnvSetEnvRelay1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 10, 5),
    _DupsEnvSetEnvRelay1_Type()
)
dupsEnvSetEnvRelay1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dupsEnvSetEnvRelay1.setStatus("mandatory")


class _DupsEnvSetEnvRelay2_Type(Integer32):
    """Custom type dupsEnvSetEnvRelay2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normalClose", 1),
          ("normalOpen", 0))
    )


_DupsEnvSetEnvRelay2_Type.__name__ = "Integer32"
_DupsEnvSetEnvRelay2_Object = MibScalar
dupsEnvSetEnvRelay2 = _DupsEnvSetEnvRelay2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 10, 6),
    _DupsEnvSetEnvRelay2_Type()
)
dupsEnvSetEnvRelay2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dupsEnvSetEnvRelay2.setStatus("mandatory")


class _DupsEnvSetEnvRelay3_Type(Integer32):
    """Custom type dupsEnvSetEnvRelay3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normalClose", 1),
          ("normalOpen", 0))
    )


_DupsEnvSetEnvRelay3_Type.__name__ = "Integer32"
_DupsEnvSetEnvRelay3_Object = MibScalar
dupsEnvSetEnvRelay3 = _DupsEnvSetEnvRelay3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 10, 7),
    _DupsEnvSetEnvRelay3_Type()
)
dupsEnvSetEnvRelay3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dupsEnvSetEnvRelay3.setStatus("mandatory")


class _DupsEnvSetEnvRelay4_Type(Integer32):
    """Custom type dupsEnvSetEnvRelay4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normalClose", 1),
          ("normalOpen", 0))
    )


_DupsEnvSetEnvRelay4_Type.__name__ = "Integer32"
_DupsEnvSetEnvRelay4_Object = MibScalar
dupsEnvSetEnvRelay4 = _DupsEnvSetEnvRelay4_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 10, 8),
    _DupsEnvSetEnvRelay4_Type()
)
dupsEnvSetEnvRelay4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dupsEnvSetEnvRelay4.setStatus("mandatory")


class _DupsAlarmOverEnvTemperature_Type(Integer32):
    """Custom type dupsAlarmOverEnvTemperature based on Integer32"""
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


_DupsAlarmOverEnvTemperature_Type.__name__ = "Integer32"
_DupsAlarmOverEnvTemperature_Object = MibScalar
dupsAlarmOverEnvTemperature = _DupsAlarmOverEnvTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 10, 9),
    _DupsAlarmOverEnvTemperature_Type()
)
dupsAlarmOverEnvTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmOverEnvTemperature.setStatus("mandatory")


class _DupsAlarmOverEnvHumidity_Type(Integer32):
    """Custom type dupsAlarmOverEnvHumidity based on Integer32"""
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


_DupsAlarmOverEnvHumidity_Type.__name__ = "Integer32"
_DupsAlarmOverEnvHumidity_Object = MibScalar
dupsAlarmOverEnvHumidity = _DupsAlarmOverEnvHumidity_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 10, 10),
    _DupsAlarmOverEnvHumidity_Type()
)
dupsAlarmOverEnvHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmOverEnvHumidity.setStatus("mandatory")


class _DupsAlarmEnvRelay1_Type(Integer32):
    """Custom type dupsAlarmEnvRelay1 based on Integer32"""
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


_DupsAlarmEnvRelay1_Type.__name__ = "Integer32"
_DupsAlarmEnvRelay1_Object = MibScalar
dupsAlarmEnvRelay1 = _DupsAlarmEnvRelay1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 10, 11),
    _DupsAlarmEnvRelay1_Type()
)
dupsAlarmEnvRelay1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmEnvRelay1.setStatus("mandatory")


class _DupsAlarmEnvRelay2_Type(Integer32):
    """Custom type dupsAlarmEnvRelay2 based on Integer32"""
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


_DupsAlarmEnvRelay2_Type.__name__ = "Integer32"
_DupsAlarmEnvRelay2_Object = MibScalar
dupsAlarmEnvRelay2 = _DupsAlarmEnvRelay2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 10, 12),
    _DupsAlarmEnvRelay2_Type()
)
dupsAlarmEnvRelay2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmEnvRelay2.setStatus("mandatory")


class _DupsAlarmEnvRelay3_Type(Integer32):
    """Custom type dupsAlarmEnvRelay3 based on Integer32"""
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


_DupsAlarmEnvRelay3_Type.__name__ = "Integer32"
_DupsAlarmEnvRelay3_Object = MibScalar
dupsAlarmEnvRelay3 = _DupsAlarmEnvRelay3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 10, 13),
    _DupsAlarmEnvRelay3_Type()
)
dupsAlarmEnvRelay3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmEnvRelay3.setStatus("mandatory")


class _DupsAlarmEnvRelay4_Type(Integer32):
    """Custom type dupsAlarmEnvRelay4 based on Integer32"""
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


_DupsAlarmEnvRelay4_Type.__name__ = "Integer32"
_DupsAlarmEnvRelay4_Object = MibScalar
dupsAlarmEnvRelay4 = _DupsAlarmEnvRelay4_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 10, 14),
    _DupsAlarmEnvRelay4_Type()
)
dupsAlarmEnvRelay4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dupsAlarmEnvRelay4.setStatus("mandatory")
_DupsTraps_ObjectIdentity = ObjectIdentity
dupsTraps = _DupsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20)
)

# Managed Objects groups


# Notification objects

dupsCommunicationLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 1)
)
if mibBuilder.loadTexts:
    dupsCommunicationLost.setStatus(
        ""
    )

dupsCommunicationEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 2)
)
if mibBuilder.loadTexts:
    dupsCommunicationEstablished.setStatus(
        ""
    )

dupsPowerFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 3)
)
if mibBuilder.loadTexts:
    dupsPowerFail.setStatus(
        ""
    )

dupsPowerRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 4)
)
if mibBuilder.loadTexts:
    dupsPowerRestored.setStatus(
        ""
    )

dupsLowBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 5)
)
if mibBuilder.loadTexts:
    dupsLowBattery.setStatus(
        ""
    )

dupsReturnFromLowBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 6)
)
if mibBuilder.loadTexts:
    dupsReturnFromLowBattery.setStatus(
        ""
    )

dupsLoadWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 7)
)
if mibBuilder.loadTexts:
    dupsLoadWarning.setStatus(
        ""
    )

dupsNoLongerLoadWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 8)
)
if mibBuilder.loadTexts:
    dupsNoLongerLoadWarning.setStatus(
        ""
    )

dupsLoadSeverity = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 9)
)
if mibBuilder.loadTexts:
    dupsLoadSeverity.setStatus(
        ""
    )

dupsNoLongerLoadSeverity = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 10)
)
if mibBuilder.loadTexts:
    dupsNoLongerLoadSeverity.setStatus(
        ""
    )

dupsLoadOnBypass = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 11)
)
if mibBuilder.loadTexts:
    dupsLoadOnBypass.setStatus(
        ""
    )

dupsNoLongerLoadOnBypass = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 12)
)
if mibBuilder.loadTexts:
    dupsNoLongerLoadOnBypass.setStatus(
        ""
    )

dupsUPSFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 13)
)
if mibBuilder.loadTexts:
    dupsUPSFault.setStatus(
        ""
    )

dupsReturnFromUPSFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 14)
)
if mibBuilder.loadTexts:
    dupsReturnFromUPSFault.setStatus(
        ""
    )

dupsBatteryGroundFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 15)
)
if mibBuilder.loadTexts:
    dupsBatteryGroundFault.setStatus(
        ""
    )

dupsNoLongerBatteryFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 16)
)
if mibBuilder.loadTexts:
    dupsNoLongerBatteryFault.setStatus(
        ""
    )

dupsTestInProgress = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 17)
)
if mibBuilder.loadTexts:
    dupsTestInProgress.setStatus(
        ""
    )

dupsBatteryTestFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 18)
)
if mibBuilder.loadTexts:
    dupsBatteryTestFail.setStatus(
        ""
    )

dupsFuseFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 19)
)
if mibBuilder.loadTexts:
    dupsFuseFailure.setStatus(
        ""
    )

dupsFuseRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 20)
)
if mibBuilder.loadTexts:
    dupsFuseRecovered.setStatus(
        ""
    )

dupsOutputOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 21)
)
if mibBuilder.loadTexts:
    dupsOutputOverload.setStatus(
        ""
    )

dupsNoLongerOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 22)
)
if mibBuilder.loadTexts:
    dupsNoLongerOverload.setStatus(
        ""
    )

dupsOutputOverCurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 23)
)
if mibBuilder.loadTexts:
    dupsOutputOverCurrent.setStatus(
        ""
    )

dupsNoLongerOutputOverCurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 24)
)
if mibBuilder.loadTexts:
    dupsNoLongerOutputOverCurrent.setStatus(
        ""
    )

dupsInverterAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 25)
)
if mibBuilder.loadTexts:
    dupsInverterAbnormal.setStatus(
        ""
    )

dupsInverterRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 26)
)
if mibBuilder.loadTexts:
    dupsInverterRecovered.setStatus(
        ""
    )

dupsRectifierAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 27)
)
if mibBuilder.loadTexts:
    dupsRectifierAbnormal.setStatus(
        ""
    )

dupsRectifierRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 28)
)
if mibBuilder.loadTexts:
    dupsRectifierRecovered.setStatus(
        ""
    )

dupsReserveAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 29)
)
if mibBuilder.loadTexts:
    dupsReserveAbnormal.setStatus(
        ""
    )

dupsReserveRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 30)
)
if mibBuilder.loadTexts:
    dupsReserveRecovered.setStatus(
        ""
    )

dupsLoadOnReserve = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 31)
)
if mibBuilder.loadTexts:
    dupsLoadOnReserve.setStatus(
        ""
    )

dupsNoLongerLoadOnReserve = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 32)
)
if mibBuilder.loadTexts:
    dupsNoLongerLoadOnReserve.setStatus(
        ""
    )

dupsEnvOverTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 33)
)
if mibBuilder.loadTexts:
    dupsEnvOverTemperature.setStatus(
        ""
    )

dupsNoLongerEnvOverTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 34)
)
if mibBuilder.loadTexts:
    dupsNoLongerEnvOverTemperature.setStatus(
        ""
    )

dupsEnvOverHumidity = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 35)
)
if mibBuilder.loadTexts:
    dupsEnvOverHumidity.setStatus(
        ""
    )

dupsNoLongerEnvOverHumidity = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 36)
)
if mibBuilder.loadTexts:
    dupsNoLongerEnvOverHumidity.setStatus(
        ""
    )

dupsEnvRelay1Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 37)
)
if mibBuilder.loadTexts:
    dupsEnvRelay1Alarm.setStatus(
        ""
    )

dupsEnvRelay1Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 38)
)
if mibBuilder.loadTexts:
    dupsEnvRelay1Normal.setStatus(
        ""
    )

dupsEnvRelay2Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 39)
)
if mibBuilder.loadTexts:
    dupsEnvRelay2Alarm.setStatus(
        ""
    )

dupsEnvRelay2Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 40)
)
if mibBuilder.loadTexts:
    dupsEnvRelay2Normal.setStatus(
        ""
    )

dupsEnvRelay3Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 41)
)
if mibBuilder.loadTexts:
    dupsEnvRelay3Alarm.setStatus(
        ""
    )

dupsEnvRelay3Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 42)
)
if mibBuilder.loadTexts:
    dupsEnvRelay3Normal.setStatus(
        ""
    )

dupsEnvRelay4Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 43)
)
if mibBuilder.loadTexts:
    dupsEnvRelay4Alarm.setStatus(
        ""
    )

dupsEnvRelay4Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 44)
)
if mibBuilder.loadTexts:
    dupsEnvRelay4Normal.setStatus(
        ""
    )

dupsSmartShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 45)
)
if mibBuilder.loadTexts:
    dupsSmartShutdown.setStatus(
        ""
    )

dupsCancelShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 46)
)
if mibBuilder.loadTexts:
    dupsCancelShutdown.setStatus(
        ""
    )

dupsTestCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 47)
)
if mibBuilder.loadTexts:
    dupsTestCompleted.setStatus(
        ""
    )

dupsEPOON = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 48)
)
if mibBuilder.loadTexts:
    dupsEPOON.setStatus(
        ""
    )

dupsEPOOFF = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 49)
)
if mibBuilder.loadTexts:
    dupsEPOOFF.setStatus(
        ""
    )

dupsOverTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 50)
)
if mibBuilder.loadTexts:
    dupsOverTemperature.setStatus(
        ""
    )

dupsNormalTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 51)
)
if mibBuilder.loadTexts:
    dupsNormalTemperature.setStatus(
        ""
    )

dupsBattReplace = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 52)
)
if mibBuilder.loadTexts:
    dupsBattReplace.setStatus(
        ""
    )

dupsReturnFromBattReplace = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 4, 20, 0, 53)
)
if mibBuilder.loadTexts:
    dupsReturnFromBattReplace.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DeltaUPS-MIB",
    **{"delta": delta,
       "ups": ups,
       "upsv4": upsv4,
       "dupsIdent": dupsIdent,
       "dupsIdentManufacturer": dupsIdentManufacturer,
       "dupsIdentModel": dupsIdentModel,
       "dupsIdentUPSSoftwareVersion": dupsIdentUPSSoftwareVersion,
       "dupsIdentAgentSoftwareVersion": dupsIdentAgentSoftwareVersion,
       "dupsIdentName": dupsIdentName,
       "dupsAttachedDevices": dupsAttachedDevices,
       "dupsRatingOutputVA": dupsRatingOutputVA,
       "dupsRatingOutputVoltage": dupsRatingOutputVoltage,
       "dupsRatingOutputFrequency": dupsRatingOutputFrequency,
       "dupsRatingInputVoltage": dupsRatingInputVoltage,
       "dupsRatingInputFrequency": dupsRatingInputFrequency,
       "dupsRatingBatteryVoltage": dupsRatingBatteryVoltage,
       "dupsLowTransferVoltUpBound": dupsLowTransferVoltUpBound,
       "dupsLowTransferVoltLowBound": dupsLowTransferVoltLowBound,
       "dupsHighTransferVoltUpBound": dupsHighTransferVoltUpBound,
       "dupsHighTransferVoltLowBound": dupsHighTransferVoltLowBound,
       "dupsLowBattTime": dupsLowBattTime,
       "dupsOutletRelays": dupsOutletRelays,
       "dupsType": dupsType,
       "dupsControl": dupsControl,
       "dupsShutdownType": dupsShutdownType,
       "dupsAutoReboot": dupsAutoReboot,
       "dupsShutdownAction": dupsShutdownAction,
       "dupsRestartAction": dupsRestartAction,
       "dupsSetOutletRelay": dupsSetOutletRelay,
       "dupsRelayOffDelay": dupsRelayOffDelay,
       "dupsRelayOnDelay": dupsRelayOnDelay,
       "dupsConfig": dupsConfig,
       "dupsConfigBuzzerAlarm": dupsConfigBuzzerAlarm,
       "dupsConfigBuzzerState": dupsConfigBuzzerState,
       "dupsConfigSensitivity": dupsConfigSensitivity,
       "dupsConfigLowVoltageTransferPoint": dupsConfigLowVoltageTransferPoint,
       "dupsConfigHighVoltageTransferPoint": dupsConfigHighVoltageTransferPoint,
       "dupsConfigShutdownOSDelay": dupsConfigShutdownOSDelay,
       "dupsConfigUPSBootDelay": dupsConfigUPSBootDelay,
       "dupsConfigExternalBatteryPack": dupsConfigExternalBatteryPack,
       "dupsInput": dupsInput,
       "dupsInputNumLines": dupsInputNumLines,
       "dupsInputFrequency1": dupsInputFrequency1,
       "dupsInputVoltage1": dupsInputVoltage1,
       "dupsInputCurrent1": dupsInputCurrent1,
       "dupsInputFrequency2": dupsInputFrequency2,
       "dupsInputVoltage2": dupsInputVoltage2,
       "dupsInputCurrent2": dupsInputCurrent2,
       "dupsInputFrequency3": dupsInputFrequency3,
       "dupsInputVoltage3": dupsInputVoltage3,
       "dupsInputCurrent3": dupsInputCurrent3,
       "dupsOutput": dupsOutput,
       "dupsOutputSource": dupsOutputSource,
       "dupsOutputFrequency": dupsOutputFrequency,
       "dupsOutputNumLines": dupsOutputNumLines,
       "dupsOutputVoltage1": dupsOutputVoltage1,
       "dupsOutputCurrent1": dupsOutputCurrent1,
       "dupsOutputPower1": dupsOutputPower1,
       "dupsOutputLoad1": dupsOutputLoad1,
       "dupsOutputVoltage2": dupsOutputVoltage2,
       "dupsOutputCurrent2": dupsOutputCurrent2,
       "dupsOutputPower2": dupsOutputPower2,
       "dupsOutputLoad2": dupsOutputLoad2,
       "dupsOutputVoltage3": dupsOutputVoltage3,
       "dupsOutputCurrent3": dupsOutputCurrent3,
       "dupsOutputPower3": dupsOutputPower3,
       "dupsOutputLoad3": dupsOutputLoad3,
       "dupsBypass": dupsBypass,
       "dupsBypassFrequency": dupsBypassFrequency,
       "dupsBypassNumLines": dupsBypassNumLines,
       "dupsBypassVoltage1": dupsBypassVoltage1,
       "dupsBypassCurrent1": dupsBypassCurrent1,
       "dupsBypassPower1": dupsBypassPower1,
       "dupsBypassVoltage2": dupsBypassVoltage2,
       "dupsBypassCurrent2": dupsBypassCurrent2,
       "dupsBypassPower2": dupsBypassPower2,
       "dupsBypassVoltage3": dupsBypassVoltage3,
       "dupsBypassCurrent3": dupsBypassCurrent3,
       "dupsBypassPower3": dupsBypassPower3,
       "dupsBattery": dupsBattery,
       "dupsBatteryCondiction": dupsBatteryCondiction,
       "dupsBatteryStatus": dupsBatteryStatus,
       "dupsBatteryCharge": dupsBatteryCharge,
       "dupsSecondsOnBattery": dupsSecondsOnBattery,
       "dupsBatteryEstimatedTime": dupsBatteryEstimatedTime,
       "dupsBatteryVoltage": dupsBatteryVoltage,
       "dupsBatteryCurrent": dupsBatteryCurrent,
       "dupsBatteryCapacity": dupsBatteryCapacity,
       "dupsTemperature": dupsTemperature,
       "dupsLastReplaceDate": dupsLastReplaceDate,
       "dupsNextReplaceDate": dupsNextReplaceDate,
       "dupsTest": dupsTest,
       "dupsTestType": dupsTestType,
       "dupsTestResultsSummary": dupsTestResultsSummary,
       "dupsTestResultsDetail": dupsTestResultsDetail,
       "dupsAlarm": dupsAlarm,
       "dupsAlarmDisconnect": dupsAlarmDisconnect,
       "dupsAlarmPowerFail": dupsAlarmPowerFail,
       "dupsAlarmBatteryLow": dupsAlarmBatteryLow,
       "dupsAlarmLoadWarning": dupsAlarmLoadWarning,
       "dupsAlarmLoadSeverity": dupsAlarmLoadSeverity,
       "dupsAlarmLoadOnBypass": dupsAlarmLoadOnBypass,
       "dupsAlarmUPSFault": dupsAlarmUPSFault,
       "dupsAlarmBatteryGroundFault": dupsAlarmBatteryGroundFault,
       "dupsAlarmTestInProgress": dupsAlarmTestInProgress,
       "dupsAlarmBatteryTestFail": dupsAlarmBatteryTestFail,
       "dupsAlarmFuseFailure": dupsAlarmFuseFailure,
       "dupsAlarmOutputOverload": dupsAlarmOutputOverload,
       "dupsAlarmOutputOverCurrent": dupsAlarmOutputOverCurrent,
       "dupsAlarmInverterAbnormal": dupsAlarmInverterAbnormal,
       "dupsAlarmRectifierAbnormal": dupsAlarmRectifierAbnormal,
       "dupsAlarmReserveAbnormal": dupsAlarmReserveAbnormal,
       "dupsAlarmLoadOnReserve": dupsAlarmLoadOnReserve,
       "dupsAlarmOverTemperature": dupsAlarmOverTemperature,
       "dupsAlarmOutputBad": dupsAlarmOutputBad,
       "dupsAlarmBypassBad": dupsAlarmBypassBad,
       "dupsAlarmUPSOff": dupsAlarmUPSOff,
       "dupsAlarmChargerFail": dupsAlarmChargerFail,
       "dupsAlarmFanFail": dupsAlarmFanFail,
       "dupsAlarmEconomicMode": dupsAlarmEconomicMode,
       "dupsAlarmOutputOff": dupsAlarmOutputOff,
       "dupsAlarmSmartShutdown": dupsAlarmSmartShutdown,
       "dupsAlarmEmergencyPowerOff": dupsAlarmEmergencyPowerOff,
       "dupsAlarmUPSShutdown": dupsAlarmUPSShutdown,
       "dupsEnvironment": dupsEnvironment,
       "dupsEnvTemperature": dupsEnvTemperature,
       "dupsEnvHumidity": dupsEnvHumidity,
       "dupsEnvSetTemperatureLimit": dupsEnvSetTemperatureLimit,
       "dupsEnvSetHumidityLimit": dupsEnvSetHumidityLimit,
       "dupsEnvSetEnvRelay1": dupsEnvSetEnvRelay1,
       "dupsEnvSetEnvRelay2": dupsEnvSetEnvRelay2,
       "dupsEnvSetEnvRelay3": dupsEnvSetEnvRelay3,
       "dupsEnvSetEnvRelay4": dupsEnvSetEnvRelay4,
       "dupsAlarmOverEnvTemperature": dupsAlarmOverEnvTemperature,
       "dupsAlarmOverEnvHumidity": dupsAlarmOverEnvHumidity,
       "dupsAlarmEnvRelay1": dupsAlarmEnvRelay1,
       "dupsAlarmEnvRelay2": dupsAlarmEnvRelay2,
       "dupsAlarmEnvRelay3": dupsAlarmEnvRelay3,
       "dupsAlarmEnvRelay4": dupsAlarmEnvRelay4,
       "dupsTraps": dupsTraps,
       "dupsCommunicationLost": dupsCommunicationLost,
       "dupsCommunicationEstablished": dupsCommunicationEstablished,
       "dupsPowerFail": dupsPowerFail,
       "dupsPowerRestored": dupsPowerRestored,
       "dupsLowBattery": dupsLowBattery,
       "dupsReturnFromLowBattery": dupsReturnFromLowBattery,
       "dupsLoadWarning": dupsLoadWarning,
       "dupsNoLongerLoadWarning": dupsNoLongerLoadWarning,
       "dupsLoadSeverity": dupsLoadSeverity,
       "dupsNoLongerLoadSeverity": dupsNoLongerLoadSeverity,
       "dupsLoadOnBypass": dupsLoadOnBypass,
       "dupsNoLongerLoadOnBypass": dupsNoLongerLoadOnBypass,
       "dupsUPSFault": dupsUPSFault,
       "dupsReturnFromUPSFault": dupsReturnFromUPSFault,
       "dupsBatteryGroundFault": dupsBatteryGroundFault,
       "dupsNoLongerBatteryFault": dupsNoLongerBatteryFault,
       "dupsTestInProgress": dupsTestInProgress,
       "dupsBatteryTestFail": dupsBatteryTestFail,
       "dupsFuseFailure": dupsFuseFailure,
       "dupsFuseRecovered": dupsFuseRecovered,
       "dupsOutputOverload": dupsOutputOverload,
       "dupsNoLongerOverload": dupsNoLongerOverload,
       "dupsOutputOverCurrent": dupsOutputOverCurrent,
       "dupsNoLongerOutputOverCurrent": dupsNoLongerOutputOverCurrent,
       "dupsInverterAbnormal": dupsInverterAbnormal,
       "dupsInverterRecovered": dupsInverterRecovered,
       "dupsRectifierAbnormal": dupsRectifierAbnormal,
       "dupsRectifierRecovered": dupsRectifierRecovered,
       "dupsReserveAbnormal": dupsReserveAbnormal,
       "dupsReserveRecovered": dupsReserveRecovered,
       "dupsLoadOnReserve": dupsLoadOnReserve,
       "dupsNoLongerLoadOnReserve": dupsNoLongerLoadOnReserve,
       "dupsEnvOverTemperature": dupsEnvOverTemperature,
       "dupsNoLongerEnvOverTemperature": dupsNoLongerEnvOverTemperature,
       "dupsEnvOverHumidity": dupsEnvOverHumidity,
       "dupsNoLongerEnvOverHumidity": dupsNoLongerEnvOverHumidity,
       "dupsEnvRelay1Alarm": dupsEnvRelay1Alarm,
       "dupsEnvRelay1Normal": dupsEnvRelay1Normal,
       "dupsEnvRelay2Alarm": dupsEnvRelay2Alarm,
       "dupsEnvRelay2Normal": dupsEnvRelay2Normal,
       "dupsEnvRelay3Alarm": dupsEnvRelay3Alarm,
       "dupsEnvRelay3Normal": dupsEnvRelay3Normal,
       "dupsEnvRelay4Alarm": dupsEnvRelay4Alarm,
       "dupsEnvRelay4Normal": dupsEnvRelay4Normal,
       "dupsSmartShutdown": dupsSmartShutdown,
       "dupsCancelShutdown": dupsCancelShutdown,
       "dupsTestCompleted": dupsTestCompleted,
       "dupsEPOON": dupsEPOON,
       "dupsEPOOFF": dupsEPOOFF,
       "dupsOverTemperature": dupsOverTemperature,
       "dupsNormalTemperature": dupsNormalTemperature,
       "dupsBattReplace": dupsBattReplace,
       "dupsReturnFromBattReplace": dupsReturnFromBattReplace}
)
