# SNMP MIB module (SYNSO-UPSMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SYNSO-UPSMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:00:09 2024
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

(upsBatteryStatus,
 upsBatteryTemperature,
 upsBatteryVoltage,
 upsInputCurrent,
 upsInputFrequency,
 upsInputVoltage) = mibBuilder.importSymbols(
    "UPS-MIB",
    "upsBatteryStatus",
    "upsBatteryTemperature",
    "upsBatteryVoltage",
    "upsInputCurrent",
    "upsInputFrequency",
    "upsInputVoltage")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Synso_ObjectIdentity = ObjectIdentity
synso = _Synso_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9557)
)
_SynsoUpsSoftware_ObjectIdentity = ObjectIdentity
synsoUpsSoftware = _SynsoUpsSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9557, 1)
)
_SyupsBasicSetting_ObjectIdentity = ObjectIdentity
syupsBasicSetting = _SyupsBasicSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9557, 1, 1)
)


class _SyupsPlatForm_Type(DisplayString):
    """Custom type syupsPlatForm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SyupsPlatForm_Type.__name__ = "DisplayString"
_SyupsPlatForm_Object = MibScalar
syupsPlatForm = _SyupsPlatForm_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 1, 1),
    _SyupsPlatForm_Type()
)
syupsPlatForm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syupsPlatForm.setStatus("mandatory")
_SyupsFeatureTable_Object = MibTable
syupsFeatureTable = _SyupsFeatureTable_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 1, 2)
)
if mibBuilder.loadTexts:
    syupsFeatureTable.setStatus("mandatory")
_SyupsFeatureEntry_Object = MibTableRow
syupsFeatureEntry = _SyupsFeatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 1, 2, 1)
)
syupsFeatureEntry.setIndexNames(
    (0, "SYNSO-UPSMIB", "syupsFeature"),
)
if mibBuilder.loadTexts:
    syupsFeatureEntry.setStatus("mandatory")
_SyupsFeature_Type = Integer32
_SyupsFeature_Object = MibTableColumn
syupsFeature = _SyupsFeature_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 1, 2, 1, 1),
    _SyupsFeature_Type()
)
syupsFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syupsFeature.setStatus("mandatory")
_SyupsSupportInfo_Type = DisplayString
_SyupsSupportInfo_Object = MibTableColumn
syupsSupportInfo = _SyupsSupportInfo_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 1, 2, 1, 2),
    _SyupsSupportInfo_Type()
)
syupsSupportInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syupsSupportInfo.setStatus("mandatory")
_SyupsSystemStartTime_Type = Integer32
_SyupsSystemStartTime_Object = MibScalar
syupsSystemStartTime = _SyupsSystemStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 1, 3),
    _SyupsSystemStartTime_Type()
)
syupsSystemStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syupsSystemStartTime.setStatus("mandatory")


class _SyupsSignalType_Type(Integer32):
    """Custom type syupsSignalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("basicSignal", 0),
          ("smartSignal", 1))
    )


_SyupsSignalType_Type.__name__ = "Integer32"
_SyupsSignalType_Object = MibScalar
syupsSignalType = _SyupsSignalType_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 1, 4),
    _SyupsSignalType_Type()
)
syupsSignalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsSignalType.setStatus("mandatory")
_SyupsBasicSignalDefinition_Type = Integer32
_SyupsBasicSignalDefinition_Object = MibScalar
syupsBasicSignalDefinition = _SyupsBasicSignalDefinition_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 1, 5),
    _SyupsBasicSignalDefinition_Type()
)
syupsBasicSignalDefinition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syupsBasicSignalDefinition.setStatus("mandatory")


class _SyupsUpsComPort_Type(DisplayString):
    """Custom type syupsUpsComPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SyupsUpsComPort_Type.__name__ = "DisplayString"
_SyupsUpsComPort_Object = MibScalar
syupsUpsComPort = _SyupsUpsComPort_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 1, 6),
    _SyupsUpsComPort_Type()
)
syupsUpsComPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsUpsComPort.setStatus("mandatory")


class _SyupsModemComPort_Type(DisplayString):
    """Custom type syupsModemComPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SyupsModemComPort_Type.__name__ = "DisplayString"
_SyupsModemComPort_Object = MibScalar
syupsModemComPort = _SyupsModemComPort_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 1, 7),
    _SyupsModemComPort_Type()
)
syupsModemComPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsModemComPort.setStatus("mandatory")
_SyupsUpsExtension_ObjectIdentity = ObjectIdentity
syupsUpsExtension = _SyupsUpsExtension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9557, 1, 2)
)
_SyupsUpsAlarm_Type = Integer32
_SyupsUpsAlarm_Object = MibScalar
syupsUpsAlarm = _SyupsUpsAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 2, 1),
    _SyupsUpsAlarm_Type()
)
syupsUpsAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syupsUpsAlarm.setStatus("mandatory")


class _SyupsSerialNo_Type(DisplayString):
    """Custom type syupsSerialNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SyupsSerialNo_Type.__name__ = "DisplayString"
_SyupsSerialNo_Object = MibScalar
syupsSerialNo = _SyupsSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 2, 2),
    _SyupsSerialNo_Type()
)
syupsSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syupsSerialNo.setStatus("mandatory")
_SyupsConfigBatteryVoltage_Type = Integer32
_SyupsConfigBatteryVoltage_Object = MibScalar
syupsConfigBatteryVoltage = _SyupsConfigBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 2, 3),
    _SyupsConfigBatteryVoltage_Type()
)
syupsConfigBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syupsConfigBatteryVoltage.setStatus("mandatory")
_SyupsBatteryReplaceDate_Type = Integer32
_SyupsBatteryReplaceDate_Object = MibScalar
syupsBatteryReplaceDate = _SyupsBatteryReplaceDate_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 2, 4),
    _SyupsBatteryReplaceDate_Type()
)
syupsBatteryReplaceDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsBatteryReplaceDate.setStatus("mandatory")
_SyupsNoOutlet_Type = Integer32
_SyupsNoOutlet_Object = MibScalar
syupsNoOutlet = _SyupsNoOutlet_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 2, 5),
    _SyupsNoOutlet_Type()
)
syupsNoOutlet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syupsNoOutlet.setStatus("mandatory")
_SyupsOutletParamter_Type = DisplayString
_SyupsOutletParamter_Object = MibScalar
syupsOutletParamter = _SyupsOutletParamter_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 2, 6),
    _SyupsOutletParamter_Type()
)
syupsOutletParamter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsOutletParamter.setStatus("mandatory")


class _SyupsShutdownDepend_Type(DisplayString):
    """Custom type syupsShutdownDepend based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SyupsShutdownDepend_Type.__name__ = "DisplayString"
_SyupsShutdownDepend_Object = MibScalar
syupsShutdownDepend = _SyupsShutdownDepend_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 2, 7),
    _SyupsShutdownDepend_Type()
)
syupsShutdownDepend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsShutdownDepend.setStatus("mandatory")
_SyupsEnableAutoSave_Type = Integer32
_SyupsEnableAutoSave_Object = MibScalar
syupsEnableAutoSave = _SyupsEnableAutoSave_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 2, 8),
    _SyupsEnableAutoSave_Type()
)
syupsEnableAutoSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsEnableAutoSave.setStatus("mandatory")
_SyupsShutdownOsDelay_Type = Integer32
_SyupsShutdownOsDelay_Object = MibScalar
syupsShutdownOsDelay = _SyupsShutdownOsDelay_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 2, 9),
    _SyupsShutdownOsDelay_Type()
)
syupsShutdownOsDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsShutdownOsDelay.setStatus("mandatory")
_SyupsShutdownUpsDelay_Type = Integer32
_SyupsShutdownUpsDelay_Object = MibScalar
syupsShutdownUpsDelay = _SyupsShutdownUpsDelay_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 2, 10),
    _SyupsShutdownUpsDelay_Type()
)
syupsShutdownUpsDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsShutdownUpsDelay.setStatus("mandatory")
_SyupsSaveConfig_Type = Integer32
_SyupsSaveConfig_Object = MibScalar
syupsSaveConfig = _SyupsSaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 2, 11),
    _SyupsSaveConfig_Type()
)
syupsSaveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsSaveConfig.setStatus("mandatory")
_SyupsNoOutlets_Type = Integer32
_SyupsNoOutlets_Object = MibScalar
syupsNoOutlets = _SyupsNoOutlets_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 2, 12),
    _SyupsNoOutlets_Type()
)
syupsNoOutlets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syupsNoOutlets.setStatus("mandatory")
_SyupsOutletTable_Object = MibTable
syupsOutletTable = _SyupsOutletTable_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 2, 13)
)
if mibBuilder.loadTexts:
    syupsOutletTable.setStatus("mandatory")
_SyupsOutletEntry_Object = MibTableRow
syupsOutletEntry = _SyupsOutletEntry_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 2, 13, 1)
)
syupsOutletEntry.setIndexNames(
    (0, "SYNSO-UPSMIB", "syupsOutletIndex"),
)
if mibBuilder.loadTexts:
    syupsOutletEntry.setStatus("mandatory")
_SyupsOutletIndex_Type = Integer32
_SyupsOutletIndex_Object = MibTableColumn
syupsOutletIndex = _SyupsOutletIndex_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 2, 13, 1, 1),
    _SyupsOutletIndex_Type()
)
syupsOutletIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    syupsOutletIndex.setStatus("mandatory")


class _SyupsOutletDescription_Type(DisplayString):
    """Custom type syupsOutletDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SyupsOutletDescription_Type.__name__ = "DisplayString"
_SyupsOutletDescription_Object = MibTableColumn
syupsOutletDescription = _SyupsOutletDescription_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 2, 13, 1, 2),
    _SyupsOutletDescription_Type()
)
syupsOutletDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsOutletDescription.setStatus("mandatory")
_SyupsOutletShutdownDelay_Type = Integer32
_SyupsOutletShutdownDelay_Object = MibTableColumn
syupsOutletShutdownDelay = _SyupsOutletShutdownDelay_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 2, 13, 1, 3),
    _SyupsOutletShutdownDelay_Type()
)
syupsOutletShutdownDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsOutletShutdownDelay.setStatus("mandatory")


class _SyupsOutletShutdownDepend_Type(DisplayString):
    """Custom type syupsOutletShutdownDepend based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SyupsOutletShutdownDepend_Type.__name__ = "DisplayString"
_SyupsOutletShutdownDepend_Object = MibTableColumn
syupsOutletShutdownDepend = _SyupsOutletShutdownDepend_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 2, 13, 1, 4),
    _SyupsOutletShutdownDepend_Type()
)
syupsOutletShutdownDepend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsOutletShutdownDepend.setStatus("mandatory")
_SyupsOutletOperator_Type = DisplayString
_SyupsOutletOperator_Object = MibScalar
syupsOutletOperator = _SyupsOutletOperator_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 2, 14),
    _SyupsOutletOperator_Type()
)
syupsOutletOperator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsOutletOperator.setStatus("mandatory")
_SyupsEventAction_ObjectIdentity = ObjectIdentity
syupsEventAction = _SyupsEventAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9557, 1, 3)
)
_SyupsNoEventActionEntries_Type = Integer32
_SyupsNoEventActionEntries_Object = MibScalar
syupsNoEventActionEntries = _SyupsNoEventActionEntries_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 3, 1),
    _SyupsNoEventActionEntries_Type()
)
syupsNoEventActionEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syupsNoEventActionEntries.setStatus("mandatory")
_SyupsEventActionTable_Object = MibTable
syupsEventActionTable = _SyupsEventActionTable_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 3, 2)
)
if mibBuilder.loadTexts:
    syupsEventActionTable.setStatus("mandatory")
_SyupsEventActionEntry_Object = MibTableRow
syupsEventActionEntry = _SyupsEventActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 3, 2, 1)
)
syupsEventActionEntry.setIndexNames(
    (0, "SYNSO-UPSMIB", "syupsEventId"),
)
if mibBuilder.loadTexts:
    syupsEventActionEntry.setStatus("mandatory")
_SyupsEventId_Type = Integer32
_SyupsEventId_Object = MibTableColumn
syupsEventId = _SyupsEventId_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 3, 2, 1, 1),
    _SyupsEventId_Type()
)
syupsEventId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syupsEventId.setStatus("mandatory")


class _SyupsLogEnable_Type(Integer32):
    """Custom type syupsLogEnable based on Integer32"""
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


_SyupsLogEnable_Type.__name__ = "Integer32"
_SyupsLogEnable_Object = MibTableColumn
syupsLogEnable = _SyupsLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 3, 2, 1, 2),
    _SyupsLogEnable_Type()
)
syupsLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsLogEnable.setStatus("mandatory")


class _SyupsNotifyEnable_Type(Integer32):
    """Custom type syupsNotifyEnable based on Integer32"""
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


_SyupsNotifyEnable_Type.__name__ = "Integer32"
_SyupsNotifyEnable_Object = MibTableColumn
syupsNotifyEnable = _SyupsNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 3, 2, 1, 3),
    _SyupsNotifyEnable_Type()
)
syupsNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsNotifyEnable.setStatus("mandatory")
_SyupsNotifyDelay_Type = Integer32
_SyupsNotifyDelay_Object = MibTableColumn
syupsNotifyDelay = _SyupsNotifyDelay_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 3, 2, 1, 4),
    _SyupsNotifyDelay_Type()
)
syupsNotifyDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsNotifyDelay.setStatus("mandatory")


class _SyupsNotifyMessage_Type(DisplayString):
    """Custom type syupsNotifyMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SyupsNotifyMessage_Type.__name__ = "DisplayString"
_SyupsNotifyMessage_Object = MibTableColumn
syupsNotifyMessage = _SyupsNotifyMessage_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 3, 2, 1, 5),
    _SyupsNotifyMessage_Type()
)
syupsNotifyMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsNotifyMessage.setStatus("mandatory")
_SyupsNotifyPeriod_Type = Integer32
_SyupsNotifyPeriod_Object = MibTableColumn
syupsNotifyPeriod = _SyupsNotifyPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 3, 2, 1, 6),
    _SyupsNotifyPeriod_Type()
)
syupsNotifyPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsNotifyPeriod.setStatus("mandatory")


class _SyupsNotifyUsers_Type(DisplayString):
    """Custom type syupsNotifyUsers based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SyupsNotifyUsers_Type.__name__ = "DisplayString"
_SyupsNotifyUsers_Object = MibTableColumn
syupsNotifyUsers = _SyupsNotifyUsers_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 3, 2, 1, 7),
    _SyupsNotifyUsers_Type()
)
syupsNotifyUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsNotifyUsers.setStatus("mandatory")


class _SyupsEmailEnable_Type(Integer32):
    """Custom type syupsEmailEnable based on Integer32"""
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


_SyupsEmailEnable_Type.__name__ = "Integer32"
_SyupsEmailEnable_Object = MibTableColumn
syupsEmailEnable = _SyupsEmailEnable_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 3, 2, 1, 8),
    _SyupsEmailEnable_Type()
)
syupsEmailEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsEmailEnable.setStatus("mandatory")
_SyupsEmailDelay_Type = Integer32
_SyupsEmailDelay_Object = MibTableColumn
syupsEmailDelay = _SyupsEmailDelay_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 3, 2, 1, 9),
    _SyupsEmailDelay_Type()
)
syupsEmailDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsEmailDelay.setStatus("mandatory")


class _SyupsEmailMessage_Type(DisplayString):
    """Custom type syupsEmailMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SyupsEmailMessage_Type.__name__ = "DisplayString"
_SyupsEmailMessage_Object = MibTableColumn
syupsEmailMessage = _SyupsEmailMessage_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 3, 2, 1, 10),
    _SyupsEmailMessage_Type()
)
syupsEmailMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsEmailMessage.setStatus("mandatory")


class _SyupsEmailUsers_Type(DisplayString):
    """Custom type syupsEmailUsers based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SyupsEmailUsers_Type.__name__ = "DisplayString"
_SyupsEmailUsers_Object = MibTableColumn
syupsEmailUsers = _SyupsEmailUsers_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 3, 2, 1, 11),
    _SyupsEmailUsers_Type()
)
syupsEmailUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsEmailUsers.setStatus("mandatory")


class _SyupsPageEnable_Type(Integer32):
    """Custom type syupsPageEnable based on Integer32"""
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


_SyupsPageEnable_Type.__name__ = "Integer32"
_SyupsPageEnable_Object = MibTableColumn
syupsPageEnable = _SyupsPageEnable_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 3, 2, 1, 12),
    _SyupsPageEnable_Type()
)
syupsPageEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsPageEnable.setStatus("mandatory")
_SyupsPageDelay_Type = Integer32
_SyupsPageDelay_Object = MibTableColumn
syupsPageDelay = _SyupsPageDelay_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 3, 2, 1, 13),
    _SyupsPageDelay_Type()
)
syupsPageDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsPageDelay.setStatus("mandatory")


class _SyupsPageMessage_Type(DisplayString):
    """Custom type syupsPageMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SyupsPageMessage_Type.__name__ = "DisplayString"
_SyupsPageMessage_Object = MibTableColumn
syupsPageMessage = _SyupsPageMessage_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 3, 2, 1, 14),
    _SyupsPageMessage_Type()
)
syupsPageMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsPageMessage.setStatus("mandatory")


class _SyupsPageUsers_Type(DisplayString):
    """Custom type syupsPageUsers based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SyupsPageUsers_Type.__name__ = "DisplayString"
_SyupsPageUsers_Object = MibTableColumn
syupsPageUsers = _SyupsPageUsers_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 3, 2, 1, 15),
    _SyupsPageUsers_Type()
)
syupsPageUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsPageUsers.setStatus("mandatory")


class _SyupsCommandEnable_Type(Integer32):
    """Custom type syupsCommandEnable based on Integer32"""
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


_SyupsCommandEnable_Type.__name__ = "Integer32"
_SyupsCommandEnable_Object = MibTableColumn
syupsCommandEnable = _SyupsCommandEnable_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 3, 2, 1, 16),
    _SyupsCommandEnable_Type()
)
syupsCommandEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsCommandEnable.setStatus("mandatory")
_SyupsCommandDelay_Type = Integer32
_SyupsCommandDelay_Object = MibTableColumn
syupsCommandDelay = _SyupsCommandDelay_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 3, 2, 1, 17),
    _SyupsCommandDelay_Type()
)
syupsCommandDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsCommandDelay.setStatus("mandatory")


class _SyupsCommandFile_Type(DisplayString):
    """Custom type syupsCommandFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SyupsCommandFile_Type.__name__ = "DisplayString"
_SyupsCommandFile_Object = MibTableColumn
syupsCommandFile = _SyupsCommandFile_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 3, 2, 1, 18),
    _SyupsCommandFile_Type()
)
syupsCommandFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsCommandFile.setStatus("mandatory")


class _SyupsShutdownEnable_Type(Integer32):
    """Custom type syupsShutdownEnable based on Integer32"""
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


_SyupsShutdownEnable_Type.__name__ = "Integer32"
_SyupsShutdownEnable_Object = MibTableColumn
syupsShutdownEnable = _SyupsShutdownEnable_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 3, 2, 1, 19),
    _SyupsShutdownEnable_Type()
)
syupsShutdownEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsShutdownEnable.setStatus("mandatory")
_SyupsShutdownDelay_Type = Integer32
_SyupsShutdownDelay_Object = MibTableColumn
syupsShutdownDelay = _SyupsShutdownDelay_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 3, 2, 1, 20),
    _SyupsShutdownDelay_Type()
)
syupsShutdownDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsShutdownDelay.setStatus("mandatory")
_SyupsHistory_ObjectIdentity = ObjectIdentity
syupsHistory = _SyupsHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9557, 1, 4)
)
_SyupsMaxEventFileLength_Type = Integer32
_SyupsMaxEventFileLength_Object = MibScalar
syupsMaxEventFileLength = _SyupsMaxEventFileLength_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 4, 1),
    _SyupsMaxEventFileLength_Type()
)
syupsMaxEventFileLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsMaxEventFileLength.setStatus("mandatory")
_SyupsEventNumRecords_Type = Integer32
_SyupsEventNumRecords_Object = MibScalar
syupsEventNumRecords = _SyupsEventNumRecords_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 4, 2),
    _SyupsEventNumRecords_Type()
)
syupsEventNumRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syupsEventNumRecords.setStatus("mandatory")
_SyupsEventTable_Object = MibTable
syupsEventTable = _SyupsEventTable_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 4, 3)
)
if mibBuilder.loadTexts:
    syupsEventTable.setStatus("mandatory")
_SyupsEventEntry_Object = MibTableRow
syupsEventEntry = _SyupsEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 4, 3, 1)
)
syupsEventEntry.setIndexNames(
    (0, "SYNSO-UPSMIB", "syupsEventIndex"),
)
if mibBuilder.loadTexts:
    syupsEventEntry.setStatus("mandatory")
_SyupsEventIndex_Type = Integer32
_SyupsEventIndex_Object = MibTableColumn
syupsEventIndex = _SyupsEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 4, 3, 1, 1),
    _SyupsEventIndex_Type()
)
syupsEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syupsEventIndex.setStatus("mandatory")
_SyupsEventRecord_Type = DisplayString
_SyupsEventRecord_Object = MibTableColumn
syupsEventRecord = _SyupsEventRecord_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 4, 3, 1, 2),
    _SyupsEventRecord_Type()
)
syupsEventRecord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syupsEventRecord.setStatus("mandatory")
_SyupsDataRecordInterval_Type = Integer32
_SyupsDataRecordInterval_Object = MibScalar
syupsDataRecordInterval = _SyupsDataRecordInterval_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 4, 4),
    _SyupsDataRecordInterval_Type()
)
syupsDataRecordInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsDataRecordInterval.setStatus("mandatory")
_SyupsMaxDataFileLength_Type = Integer32
_SyupsMaxDataFileLength_Object = MibScalar
syupsMaxDataFileLength = _SyupsMaxDataFileLength_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 4, 5),
    _SyupsMaxDataFileLength_Type()
)
syupsMaxDataFileLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsMaxDataFileLength.setStatus("mandatory")
_SyupsDataNumRecords_Type = Integer32
_SyupsDataNumRecords_Object = MibScalar
syupsDataNumRecords = _SyupsDataNumRecords_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 4, 6),
    _SyupsDataNumRecords_Type()
)
syupsDataNumRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syupsDataNumRecords.setStatus("mandatory")
_SyupsDataTable_Object = MibTable
syupsDataTable = _SyupsDataTable_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 4, 7)
)
if mibBuilder.loadTexts:
    syupsDataTable.setStatus("mandatory")
_SyupsDataEntry_Object = MibTableRow
syupsDataEntry = _SyupsDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 4, 7, 1)
)
syupsDataEntry.setIndexNames(
    (0, "SYNSO-UPSMIB", "syupsDataIndex"),
)
if mibBuilder.loadTexts:
    syupsDataEntry.setStatus("mandatory")
_SyupsDataIndex_Type = Integer32
_SyupsDataIndex_Object = MibTableColumn
syupsDataIndex = _SyupsDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 4, 7, 1, 1),
    _SyupsDataIndex_Type()
)
syupsDataIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syupsDataIndex.setStatus("mandatory")
_SyupsDataRecord_Type = DisplayString
_SyupsDataRecord_Object = MibTableColumn
syupsDataRecord = _SyupsDataRecord_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 4, 7, 1, 2),
    _SyupsDataRecord_Type()
)
syupsDataRecord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syupsDataRecord.setStatus("mandatory")
_SyupsHistoryOperator_Type = DisplayString
_SyupsHistoryOperator_Object = MibScalar
syupsHistoryOperator = _SyupsHistoryOperator_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 4, 8),
    _SyupsHistoryOperator_Type()
)
syupsHistoryOperator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsHistoryOperator.setStatus("mandatory")
_SyupsScopeSettings_Type = DisplayString
_SyupsScopeSettings_Object = MibScalar
syupsScopeSettings = _SyupsScopeSettings_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 4, 9),
    _SyupsScopeSettings_Type()
)
syupsScopeSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsScopeSettings.setStatus("mandatory")
_SyupsSchedule_ObjectIdentity = ObjectIdentity
syupsSchedule = _SyupsSchedule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9557, 1, 5)
)
_SyupsNoSchEntries_Type = Integer32
_SyupsNoSchEntries_Object = MibScalar
syupsNoSchEntries = _SyupsNoSchEntries_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 5, 1),
    _SyupsNoSchEntries_Type()
)
syupsNoSchEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syupsNoSchEntries.setStatus("mandatory")
_SyupsSchOperator_Type = DisplayString
_SyupsSchOperator_Object = MibScalar
syupsSchOperator = _SyupsSchOperator_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 5, 2),
    _SyupsSchOperator_Type()
)
syupsSchOperator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsSchOperator.setStatus("mandatory")
_SyupsSchTable_Object = MibTable
syupsSchTable = _SyupsSchTable_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 5, 3)
)
if mibBuilder.loadTexts:
    syupsSchTable.setStatus("mandatory")
_SyupsSchEntry_Object = MibTableRow
syupsSchEntry = _SyupsSchEntry_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 5, 3, 1)
)
syupsSchEntry.setIndexNames(
    (0, "SYNSO-UPSMIB", "syupsSchIndex"),
)
if mibBuilder.loadTexts:
    syupsSchEntry.setStatus("mandatory")
_SyupsSchIndex_Type = Integer32
_SyupsSchIndex_Object = MibTableColumn
syupsSchIndex = _SyupsSchIndex_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 5, 3, 1, 1),
    _SyupsSchIndex_Type()
)
syupsSchIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syupsSchIndex.setStatus("mandatory")
_SyupsSchStartDate_Type = DisplayString
_SyupsSchStartDate_Object = MibTableColumn
syupsSchStartDate = _SyupsSchStartDate_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 5, 3, 1, 2),
    _SyupsSchStartDate_Type()
)
syupsSchStartDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syupsSchStartDate.setStatus("mandatory")
_SyupsSchStartTime_Type = DisplayString
_SyupsSchStartTime_Object = MibTableColumn
syupsSchStartTime = _SyupsSchStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 5, 3, 1, 3),
    _SyupsSchStartTime_Type()
)
syupsSchStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syupsSchStartTime.setStatus("mandatory")


class _SyupsSchWeekDay_Type(Integer32):
    """Custom type syupsSchWeekDay based on Integer32"""
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
        *(("friday", 5),
          ("monday", 1),
          ("saturday", 6),
          ("sunday", 0),
          ("thursday", 4),
          ("tuesday", 2),
          ("wednesday", 3))
    )


_SyupsSchWeekDay_Type.__name__ = "Integer32"
_SyupsSchWeekDay_Object = MibTableColumn
syupsSchWeekDay = _SyupsSchWeekDay_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 5, 3, 1, 4),
    _SyupsSchWeekDay_Type()
)
syupsSchWeekDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syupsSchWeekDay.setStatus("mandatory")
_SyupsSchAction_Type = Integer32
_SyupsSchAction_Object = MibTableColumn
syupsSchAction = _SyupsSchAction_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 5, 3, 1, 5),
    _SyupsSchAction_Type()
)
syupsSchAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syupsSchAction.setStatus("mandatory")


class _SyupsSchRepeat_Type(Integer32):
    """Custom type syupsSchRepeat based on Integer32"""
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
        *(("daily", 2),
          ("monthly", 4),
          ("once", 1),
          ("weekly", 3))
    )


_SyupsSchRepeat_Type.__name__ = "Integer32"
_SyupsSchRepeat_Object = MibTableColumn
syupsSchRepeat = _SyupsSchRepeat_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 5, 3, 1, 6),
    _SyupsSchRepeat_Type()
)
syupsSchRepeat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syupsSchRepeat.setStatus("mandatory")
_SyupsCoworker_ObjectIdentity = ObjectIdentity
syupsCoworker = _SyupsCoworker_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9557, 1, 6)
)
_SyupsNoAccessControl_Type = Integer32
_SyupsNoAccessControl_Object = MibScalar
syupsNoAccessControl = _SyupsNoAccessControl_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 6, 1),
    _SyupsNoAccessControl_Type()
)
syupsNoAccessControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syupsNoAccessControl.setStatus("mandatory")
_SyupsAccessControlOperator_Type = DisplayString
_SyupsAccessControlOperator_Object = MibScalar
syupsAccessControlOperator = _SyupsAccessControlOperator_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 6, 2),
    _SyupsAccessControlOperator_Type()
)
syupsAccessControlOperator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsAccessControlOperator.setStatus("mandatory")
_SyupsAccessControlTable_Object = MibTable
syupsAccessControlTable = _SyupsAccessControlTable_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 6, 3)
)
if mibBuilder.loadTexts:
    syupsAccessControlTable.setStatus("mandatory")
_SyupsAccessControlEntry_Object = MibTableRow
syupsAccessControlEntry = _SyupsAccessControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 6, 3, 1)
)
syupsAccessControlEntry.setIndexNames(
    (0, "SYNSO-UPSMIB", "syupsAccessControlIndex"),
)
if mibBuilder.loadTexts:
    syupsAccessControlEntry.setStatus("mandatory")
_SyupsAccessControlIndex_Type = Integer32
_SyupsAccessControlIndex_Object = MibTableColumn
syupsAccessControlIndex = _SyupsAccessControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 6, 3, 1, 1),
    _SyupsAccessControlIndex_Type()
)
syupsAccessControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syupsAccessControlIndex.setStatus("mandatory")
_SyupsAccessControlSetting_Type = DisplayString
_SyupsAccessControlSetting_Object = MibTableColumn
syupsAccessControlSetting = _SyupsAccessControlSetting_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 6, 3, 1, 2),
    _SyupsAccessControlSetting_Type()
)
syupsAccessControlSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syupsAccessControlSetting.setStatus("mandatory")
_SyupsNoTrapReceiver_Type = Integer32
_SyupsNoTrapReceiver_Object = MibScalar
syupsNoTrapReceiver = _SyupsNoTrapReceiver_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 6, 4),
    _SyupsNoTrapReceiver_Type()
)
syupsNoTrapReceiver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syupsNoTrapReceiver.setStatus("mandatory")
_SyupsTrapReceiverOperator_Type = DisplayString
_SyupsTrapReceiverOperator_Object = MibScalar
syupsTrapReceiverOperator = _SyupsTrapReceiverOperator_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 6, 5),
    _SyupsTrapReceiverOperator_Type()
)
syupsTrapReceiverOperator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syupsTrapReceiverOperator.setStatus("mandatory")
_SyupsTrapReceiverTable_Object = MibTable
syupsTrapReceiverTable = _SyupsTrapReceiverTable_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 6, 6)
)
if mibBuilder.loadTexts:
    syupsTrapReceiverTable.setStatus("mandatory")
_SyupsTrapReceiverEntry_Object = MibTableRow
syupsTrapReceiverEntry = _SyupsTrapReceiverEntry_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 6, 6, 1)
)
syupsTrapReceiverEntry.setIndexNames(
    (0, "SYNSO-UPSMIB", "syupsTrapReceiverIndex"),
)
if mibBuilder.loadTexts:
    syupsTrapReceiverEntry.setStatus("mandatory")
_SyupsTrapReceiverIndex_Type = Integer32
_SyupsTrapReceiverIndex_Object = MibTableColumn
syupsTrapReceiverIndex = _SyupsTrapReceiverIndex_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 6, 6, 1, 1),
    _SyupsTrapReceiverIndex_Type()
)
syupsTrapReceiverIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syupsTrapReceiverIndex.setStatus("mandatory")
_SyupsTrapReceiverSetting_Type = DisplayString
_SyupsTrapReceiverSetting_Object = MibTableColumn
syupsTrapReceiverSetting = _SyupsTrapReceiverSetting_Object(
    (1, 3, 6, 1, 4, 1, 9557, 1, 6, 6, 1, 2),
    _SyupsTrapReceiverSetting_Type()
)
syupsTrapReceiverSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syupsTrapReceiverSetting.setStatus("mandatory")
_SyupsTraps_ObjectIdentity = ObjectIdentity
syupsTraps = _SyupsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9557, 1, 7)
)

# Managed Objects groups


# Notification objects

syupsTrapOverTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 9557, 1, 7, 1)
)
syupsTrapOverTemperature.setObjects(
    ("UPS-MIB", "upsBatteryTemperature")
)
if mibBuilder.loadTexts:
    syupsTrapOverTemperature.setStatus(
        "current"
    )

syupsTrapOverCurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9557, 1, 7, 2)
)
syupsTrapOverCurrent.setObjects(
    ("UPS-MIB", "upsInputCurrent")
)
if mibBuilder.loadTexts:
    syupsTrapOverCurrent.setStatus(
        "current"
    )

syupsTrapOverVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 9557, 1, 7, 3)
)
syupsTrapOverVoltage.setObjects(
    ("UPS-MIB", "upsInputVoltage")
)
if mibBuilder.loadTexts:
    syupsTrapOverVoltage.setStatus(
        "current"
    )

syupsTrapUnderVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 9557, 1, 7, 4)
)
syupsTrapUnderVoltage.setObjects(
    ("UPS-MIB", "upsInputVoltage")
)
if mibBuilder.loadTexts:
    syupsTrapUnderVoltage.setStatus(
        "current"
    )

syupsOffFrequency = NotificationType(
    (1, 3, 6, 1, 4, 1, 9557, 1, 7, 5)
)
syupsOffFrequency.setObjects(
    ("UPS-MIB", "upsInputFrequency")
)
if mibBuilder.loadTexts:
    syupsOffFrequency.setStatus(
        "current"
    )

syupsLowBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 9557, 1, 7, 6)
)
syupsLowBattery.setObjects(
      *(("UPS-MIB", "upsBatteryStatus"),
        ("UPS-MIB", "upsBatteryVoltage"))
)
if mibBuilder.loadTexts:
    syupsLowBattery.setStatus(
        "current"
    )

syupsBadBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 9557, 1, 7, 7)
)
syupsBadBattery.setObjects(
      *(("UPS-MIB", "upsBatteryStatus"),
        ("UPS-MIB", "upsBatteryVoltage"))
)
if mibBuilder.loadTexts:
    syupsBadBattery.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYNSO-UPSMIB",
    **{"synso": synso,
       "synsoUpsSoftware": synsoUpsSoftware,
       "syupsBasicSetting": syupsBasicSetting,
       "syupsPlatForm": syupsPlatForm,
       "syupsFeatureTable": syupsFeatureTable,
       "syupsFeatureEntry": syupsFeatureEntry,
       "syupsFeature": syupsFeature,
       "syupsSupportInfo": syupsSupportInfo,
       "syupsSystemStartTime": syupsSystemStartTime,
       "syupsSignalType": syupsSignalType,
       "syupsBasicSignalDefinition": syupsBasicSignalDefinition,
       "syupsUpsComPort": syupsUpsComPort,
       "syupsModemComPort": syupsModemComPort,
       "syupsUpsExtension": syupsUpsExtension,
       "syupsUpsAlarm": syupsUpsAlarm,
       "syupsSerialNo": syupsSerialNo,
       "syupsConfigBatteryVoltage": syupsConfigBatteryVoltage,
       "syupsBatteryReplaceDate": syupsBatteryReplaceDate,
       "syupsNoOutlet": syupsNoOutlet,
       "syupsOutletParamter": syupsOutletParamter,
       "syupsShutdownDepend": syupsShutdownDepend,
       "syupsEnableAutoSave": syupsEnableAutoSave,
       "syupsShutdownOsDelay": syupsShutdownOsDelay,
       "syupsShutdownUpsDelay": syupsShutdownUpsDelay,
       "syupsSaveConfig": syupsSaveConfig,
       "syupsNoOutlets": syupsNoOutlets,
       "syupsOutletTable": syupsOutletTable,
       "syupsOutletEntry": syupsOutletEntry,
       "syupsOutletIndex": syupsOutletIndex,
       "syupsOutletDescription": syupsOutletDescription,
       "syupsOutletShutdownDelay": syupsOutletShutdownDelay,
       "syupsOutletShutdownDepend": syupsOutletShutdownDepend,
       "syupsOutletOperator": syupsOutletOperator,
       "syupsEventAction": syupsEventAction,
       "syupsNoEventActionEntries": syupsNoEventActionEntries,
       "syupsEventActionTable": syupsEventActionTable,
       "syupsEventActionEntry": syupsEventActionEntry,
       "syupsEventId": syupsEventId,
       "syupsLogEnable": syupsLogEnable,
       "syupsNotifyEnable": syupsNotifyEnable,
       "syupsNotifyDelay": syupsNotifyDelay,
       "syupsNotifyMessage": syupsNotifyMessage,
       "syupsNotifyPeriod": syupsNotifyPeriod,
       "syupsNotifyUsers": syupsNotifyUsers,
       "syupsEmailEnable": syupsEmailEnable,
       "syupsEmailDelay": syupsEmailDelay,
       "syupsEmailMessage": syupsEmailMessage,
       "syupsEmailUsers": syupsEmailUsers,
       "syupsPageEnable": syupsPageEnable,
       "syupsPageDelay": syupsPageDelay,
       "syupsPageMessage": syupsPageMessage,
       "syupsPageUsers": syupsPageUsers,
       "syupsCommandEnable": syupsCommandEnable,
       "syupsCommandDelay": syupsCommandDelay,
       "syupsCommandFile": syupsCommandFile,
       "syupsShutdownEnable": syupsShutdownEnable,
       "syupsShutdownDelay": syupsShutdownDelay,
       "syupsHistory": syupsHistory,
       "syupsMaxEventFileLength": syupsMaxEventFileLength,
       "syupsEventNumRecords": syupsEventNumRecords,
       "syupsEventTable": syupsEventTable,
       "syupsEventEntry": syupsEventEntry,
       "syupsEventIndex": syupsEventIndex,
       "syupsEventRecord": syupsEventRecord,
       "syupsDataRecordInterval": syupsDataRecordInterval,
       "syupsMaxDataFileLength": syupsMaxDataFileLength,
       "syupsDataNumRecords": syupsDataNumRecords,
       "syupsDataTable": syupsDataTable,
       "syupsDataEntry": syupsDataEntry,
       "syupsDataIndex": syupsDataIndex,
       "syupsDataRecord": syupsDataRecord,
       "syupsHistoryOperator": syupsHistoryOperator,
       "syupsScopeSettings": syupsScopeSettings,
       "syupsSchedule": syupsSchedule,
       "syupsNoSchEntries": syupsNoSchEntries,
       "syupsSchOperator": syupsSchOperator,
       "syupsSchTable": syupsSchTable,
       "syupsSchEntry": syupsSchEntry,
       "syupsSchIndex": syupsSchIndex,
       "syupsSchStartDate": syupsSchStartDate,
       "syupsSchStartTime": syupsSchStartTime,
       "syupsSchWeekDay": syupsSchWeekDay,
       "syupsSchAction": syupsSchAction,
       "syupsSchRepeat": syupsSchRepeat,
       "syupsCoworker": syupsCoworker,
       "syupsNoAccessControl": syupsNoAccessControl,
       "syupsAccessControlOperator": syupsAccessControlOperator,
       "syupsAccessControlTable": syupsAccessControlTable,
       "syupsAccessControlEntry": syupsAccessControlEntry,
       "syupsAccessControlIndex": syupsAccessControlIndex,
       "syupsAccessControlSetting": syupsAccessControlSetting,
       "syupsNoTrapReceiver": syupsNoTrapReceiver,
       "syupsTrapReceiverOperator": syupsTrapReceiverOperator,
       "syupsTrapReceiverTable": syupsTrapReceiverTable,
       "syupsTrapReceiverEntry": syupsTrapReceiverEntry,
       "syupsTrapReceiverIndex": syupsTrapReceiverIndex,
       "syupsTrapReceiverSetting": syupsTrapReceiverSetting,
       "syupsTraps": syupsTraps,
       "syupsTrapOverTemperature": syupsTrapOverTemperature,
       "syupsTrapOverCurrent": syupsTrapOverCurrent,
       "syupsTrapOverVoltage": syupsTrapOverVoltage,
       "syupsTrapUnderVoltage": syupsTrapUnderVoltage,
       "syupsOffFrequency": syupsOffFrequency,
       "syupsLowBattery": syupsLowBattery,
       "syupsBadBattery": syupsBadBattery}
)
