# SNMP MIB module (MICROSENS-CWDM8-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MICROSENS-CWDM8-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:57 2024
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

_Microsens_ObjectIdentity = ObjectIdentity
microsens = _Microsens_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181)
)
_Cwdm_ObjectIdentity = ObjectIdentity
cwdm = _Cwdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 6)
)
_EightChannelCwdm_ObjectIdentity = ObjectIdentity
eightChannelCwdm = _EightChannelCwdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4)
)
_DeviceTable_Object = MibTable
deviceTable = _DeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 1)
)
if mibBuilder.loadTexts:
    deviceTable.setStatus("mandatory")
_DeviceTableEntry_Object = MibTableRow
deviceTableEntry = _DeviceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 1, 1)
)
deviceTableEntry.setIndexNames(
    (0, "MICROSENS-CWDM8-MIB", "deviceId"),
)
if mibBuilder.loadTexts:
    deviceTableEntry.setStatus("mandatory")
_DeviceId_Type = Integer32
_DeviceId_Object = MibTableColumn
deviceId = _DeviceId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 1, 1, 1),
    _DeviceId_Type()
)
deviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceId.setStatus("mandatory")


class _DeviceArtNo_Type(DisplayString):
    """Custom type deviceArtNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DeviceArtNo_Type.__name__ = "DisplayString"
_DeviceArtNo_Object = MibTableColumn
deviceArtNo = _DeviceArtNo_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 1, 1, 2),
    _DeviceArtNo_Type()
)
deviceArtNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceArtNo.setStatus("mandatory")


class _DeviceSerNo_Type(DisplayString):
    """Custom type deviceSerNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DeviceSerNo_Type.__name__ = "DisplayString"
_DeviceSerNo_Object = MibTableColumn
deviceSerNo = _DeviceSerNo_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 1, 1, 3),
    _DeviceSerNo_Type()
)
deviceSerNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceSerNo.setStatus("mandatory")


class _DeviceDesc_Type(DisplayString):
    """Custom type deviceDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DeviceDesc_Type.__name__ = "DisplayString"
_DeviceDesc_Object = MibTableColumn
deviceDesc = _DeviceDesc_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 1, 1, 4),
    _DeviceDesc_Type()
)
deviceDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceDesc.setStatus("mandatory")


class _DeviceTemperature_Type(Integer32):
    """Custom type deviceTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -255
        )
    )
    namedValues = NamedValues(
        ("unknown", -255)
    )


_DeviceTemperature_Type.__name__ = "Integer32"
_DeviceTemperature_Object = MibTableColumn
deviceTemperature = _DeviceTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 1, 1, 5),
    _DeviceTemperature_Type()
)
deviceTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceTemperature.setStatus("mandatory")


class _DeviceTempAlarmThreshold_Type(Integer32):
    """Custom type deviceTempAlarmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -255
        )
    )
    namedValues = NamedValues(
        ("unknown", -255)
    )


_DeviceTempAlarmThreshold_Type.__name__ = "Integer32"
_DeviceTempAlarmThreshold_Object = MibTableColumn
deviceTempAlarmThreshold = _DeviceTempAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 1, 1, 6),
    _DeviceTempAlarmThreshold_Type()
)
deviceTempAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceTempAlarmThreshold.setStatus("mandatory")


class _DeviceTempAlarm_Type(Integer32):
    """Custom type deviceTempAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-255,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("no-alarm", 0),
          ("unknown", -255))
    )


_DeviceTempAlarm_Type.__name__ = "Integer32"
_DeviceTempAlarm_Object = MibTableColumn
deviceTempAlarm = _DeviceTempAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 1, 1, 7),
    _DeviceTempAlarm_Type()
)
deviceTempAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceTempAlarm.setStatus("mandatory")


class _DeviceTempShutdown_Type(Integer32):
    """Custom type deviceTempShutdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-255,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("no-alarm", 0),
          ("unknown", -255))
    )


_DeviceTempShutdown_Type.__name__ = "Integer32"
_DeviceTempShutdown_Object = MibTableColumn
deviceTempShutdown = _DeviceTempShutdown_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 1, 1, 8),
    _DeviceTempShutdown_Type()
)
deviceTempShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceTempShutdown.setStatus("mandatory")


class _DeviceTrPowerFailureAlarm_Type(Integer32):
    """Custom type deviceTrPowerFailureAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-255,
              0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm-channel-1-4", 1),
          ("alarm-channel-1-8", 3),
          ("alarm-channel-5-8", 2),
          ("no-alarm", 0),
          ("unknown", -255))
    )


_DeviceTrPowerFailureAlarm_Type.__name__ = "Integer32"
_DeviceTrPowerFailureAlarm_Object = MibTableColumn
deviceTrPowerFailureAlarm = _DeviceTrPowerFailureAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 1, 1, 9),
    _DeviceTrPowerFailureAlarm_Type()
)
deviceTrPowerFailureAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceTrPowerFailureAlarm.setStatus("mandatory")


class _DeviceMinorAlarm_Type(Integer32):
    """Custom type deviceMinorAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-255,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("no-alarm", 0),
          ("unknown", -255))
    )


_DeviceMinorAlarm_Type.__name__ = "Integer32"
_DeviceMinorAlarm_Object = MibTableColumn
deviceMinorAlarm = _DeviceMinorAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 1, 1, 10),
    _DeviceMinorAlarm_Type()
)
deviceMinorAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceMinorAlarm.setStatus("mandatory")


class _DeviceMajorAlarm_Type(Integer32):
    """Custom type deviceMajorAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-255,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("no-alarm", 0),
          ("unknown", -255))
    )


_DeviceMajorAlarm_Type.__name__ = "Integer32"
_DeviceMajorAlarm_Object = MibTableColumn
deviceMajorAlarm = _DeviceMajorAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 1, 1, 11),
    _DeviceMajorAlarm_Type()
)
deviceMajorAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceMajorAlarm.setStatus("mandatory")
_PortTable_Object = MibTable
portTable = _PortTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 2)
)
if mibBuilder.loadTexts:
    portTable.setStatus("mandatory")
_PortTableEntry_Object = MibTableRow
portTableEntry = _PortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 2, 1)
)
portTableEntry.setIndexNames(
    (0, "MICROSENS-CWDM8-MIB", "portId"),
)
if mibBuilder.loadTexts:
    portTableEntry.setStatus("mandatory")
_PortId_Type = Integer32
_PortId_Object = MibTableColumn
portId = _PortId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 2, 1, 1),
    _PortId_Type()
)
portId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portId.setStatus("mandatory")


class _PortChannelEnabled_Type(Integer32):
    """Custom type portChannelEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-255,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("unknown", -255))
    )


_PortChannelEnabled_Type.__name__ = "Integer32"
_PortChannelEnabled_Object = MibTableColumn
portChannelEnabled = _PortChannelEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 2, 1, 2),
    _PortChannelEnabled_Type()
)
portChannelEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portChannelEnabled.setStatus("mandatory")


class _PortLinkThroughLocalLine_Type(Integer32):
    """Custom type portLinkThroughLocalLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-255,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("unknown", -255))
    )


_PortLinkThroughLocalLine_Type.__name__ = "Integer32"
_PortLinkThroughLocalLine_Object = MibTableColumn
portLinkThroughLocalLine = _PortLinkThroughLocalLine_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 2, 1, 3),
    _PortLinkThroughLocalLine_Type()
)
portLinkThroughLocalLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLinkThroughLocalLine.setStatus("mandatory")


class _PortLinkThroughLineLocal_Type(Integer32):
    """Custom type portLinkThroughLineLocal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-255,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("unknown", -255))
    )


_PortLinkThroughLineLocal_Type.__name__ = "Integer32"
_PortLinkThroughLineLocal_Object = MibTableColumn
portLinkThroughLineLocal = _PortLinkThroughLineLocal_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 2, 1, 4),
    _PortLinkThroughLineLocal_Type()
)
portLinkThroughLineLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLinkThroughLineLocal.setStatus("mandatory")


class _PortLocalModuleInstalled_Type(Integer32):
    """Custom type portLocalModuleInstalled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-255,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("installed", 1),
          ("not-installed", 0),
          ("unknown", -255))
    )


_PortLocalModuleInstalled_Type.__name__ = "Integer32"
_PortLocalModuleInstalled_Object = MibTableColumn
portLocalModuleInstalled = _PortLocalModuleInstalled_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 2, 1, 5),
    _PortLocalModuleInstalled_Type()
)
portLocalModuleInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLocalModuleInstalled.setStatus("mandatory")


class _PortLineModuleInstalled_Type(Integer32):
    """Custom type portLineModuleInstalled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-255,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("installed", 1),
          ("not-installed", 0),
          ("unknown", -255))
    )


_PortLineModuleInstalled_Type.__name__ = "Integer32"
_PortLineModuleInstalled_Object = MibTableColumn
portLineModuleInstalled = _PortLineModuleInstalled_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 2, 1, 6),
    _PortLineModuleInstalled_Type()
)
portLineModuleInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLineModuleInstalled.setStatus("mandatory")


class _PortLocalLink_Type(Integer32):
    """Custom type portLocalLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-255,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("unknown", -255))
    )


_PortLocalLink_Type.__name__ = "Integer32"
_PortLocalLink_Object = MibTableColumn
portLocalLink = _PortLocalLink_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 2, 1, 7),
    _PortLocalLink_Type()
)
portLocalLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLocalLink.setStatus("mandatory")


class _PortLineLink_Type(Integer32):
    """Custom type portLineLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-255,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("unknown", -255))
    )


_PortLineLink_Type.__name__ = "Integer32"
_PortLineLink_Object = MibTableColumn
portLineLink = _PortLineLink_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 2, 1, 8),
    _PortLineLink_Type()
)
portLineLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLineLink.setStatus("mandatory")


class _PortLocalTxFault_Type(Integer32):
    """Custom type portLocalTxFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-255,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("no-error", 0),
          ("unknown", -255))
    )


_PortLocalTxFault_Type.__name__ = "Integer32"
_PortLocalTxFault_Object = MibTableColumn
portLocalTxFault = _PortLocalTxFault_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 2, 1, 9),
    _PortLocalTxFault_Type()
)
portLocalTxFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLocalTxFault.setStatus("mandatory")


class _PortLineTxFault_Type(Integer32):
    """Custom type portLineTxFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-255,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("no-error", 0),
          ("unknown", -255))
    )


_PortLineTxFault_Type.__name__ = "Integer32"
_PortLineTxFault_Object = MibTableColumn
portLineTxFault = _PortLineTxFault_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 2, 1, 10),
    _PortLineTxFault_Type()
)
portLineTxFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLineTxFault.setStatus("mandatory")


class _PortLocalPowerFault_Type(Integer32):
    """Custom type portLocalPowerFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-255,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("no-error", 0),
          ("unknown", -255))
    )


_PortLocalPowerFault_Type.__name__ = "Integer32"
_PortLocalPowerFault_Object = MibTableColumn
portLocalPowerFault = _PortLocalPowerFault_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 2, 1, 11),
    _PortLocalPowerFault_Type()
)
portLocalPowerFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLocalPowerFault.setStatus("mandatory")


class _PortLinePowerFault_Type(Integer32):
    """Custom type portLinePowerFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-255,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("no-error", 0),
          ("unknown", -255))
    )


_PortLinePowerFault_Type.__name__ = "Integer32"
_PortLinePowerFault_Object = MibTableColumn
portLinePowerFault = _PortLinePowerFault_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 2, 1, 12),
    _PortLinePowerFault_Type()
)
portLinePowerFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLinePowerFault.setStatus("mandatory")


class _PortRateSelect_Type(Integer32):
    """Custom type portRateSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-255,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("reduced", 0),
          ("unknown", -255))
    )


_PortRateSelect_Type.__name__ = "Integer32"
_PortRateSelect_Object = MibTableColumn
portRateSelect = _PortRateSelect_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 2, 1, 13),
    _PortRateSelect_Type()
)
portRateSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portRateSelect.setStatus("mandatory")
_LocalModuleTable_Object = MibTable
localModuleTable = _LocalModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 3)
)
if mibBuilder.loadTexts:
    localModuleTable.setStatus("mandatory")
_LocalModuleTableEntry_Object = MibTableRow
localModuleTableEntry = _LocalModuleTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 3, 1)
)
localModuleTableEntry.setIndexNames(
    (0, "MICROSENS-CWDM8-MIB", "localModuleId"),
)
if mibBuilder.loadTexts:
    localModuleTableEntry.setStatus("mandatory")
_LocalModuleId_Type = Integer32
_LocalModuleId_Object = MibTableColumn
localModuleId = _LocalModuleId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 3, 1, 1),
    _LocalModuleId_Type()
)
localModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localModuleId.setStatus("mandatory")


class _LocalModuleConnector_Type(Integer32):
    """Custom type localModuleConnector based on Integer32"""
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
              32,
              33)
        )
    )
    namedValues = NamedValues(
        *(("bnc-tnc", 4),
          ("coaxial-headers", 5),
          ("copperpigtail", 33),
          ("fiberjack", 6),
          ("hssdc2", 32),
          ("lc", 7),
          ("mt-rj", 8),
          ("mu", 9),
          ("opticalpigtail", 11),
          ("sc", 1),
          ("sg", 10),
          ("style1-copper", 2),
          ("style2-copper", 3),
          ("unknown", 0))
    )


_LocalModuleConnector_Type.__name__ = "Integer32"
_LocalModuleConnector_Object = MibTableColumn
localModuleConnector = _LocalModuleConnector_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 3, 1, 2),
    _LocalModuleConnector_Type()
)
localModuleConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localModuleConnector.setStatus("mandatory")


class _LocalModuleTrCodeSonet_Type(Integer32):
    """Custom type localModuleTrCodeSonet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              16,
              32,
              64,
              128,
              256,
              512)
        )
    )
    namedValues = NamedValues(
        *(("oc12-multi-mode-short-reach", 16),
          ("oc12-single-mode-intermediate-reach", 32),
          ("oc12-single-mode-long-reach", 64),
          ("oc3-multi-mode-short-reach", 1),
          ("oc3-single-mode-intermediate-reach", 2),
          ("oc3-single-mode-long-reach", 4),
          ("oc48-intermediate-reach", 256),
          ("oc48-long-reach", 512),
          ("oc48-short-reach", 128),
          ("unknown", 0))
    )


_LocalModuleTrCodeSonet_Type.__name__ = "Integer32"
_LocalModuleTrCodeSonet_Object = MibTableColumn
localModuleTrCodeSonet = _LocalModuleTrCodeSonet_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 3, 1, 3),
    _LocalModuleTrCodeSonet_Type()
)
localModuleTrCodeSonet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localModuleTrCodeSonet.setStatus("mandatory")


class _LocalModuleTrCodeGigabit_Type(Integer32):
    """Custom type localModuleTrCodeGigabit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("base-1000-cx", 4),
          ("base-1000-lx", 2),
          ("base-1000-sx", 1),
          ("base-1000-t", 8),
          ("unknown", 0))
    )


_LocalModuleTrCodeGigabit_Type.__name__ = "Integer32"
_LocalModuleTrCodeGigabit_Object = MibTableColumn
localModuleTrCodeGigabit = _LocalModuleTrCodeGigabit_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 3, 1, 4),
    _LocalModuleTrCodeGigabit_Type()
)
localModuleTrCodeGigabit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localModuleTrCodeGigabit.setStatus("mandatory")


class _LocalModuleTrCodeFbLinkLength_Type(Integer32):
    """Custom type localModuleTrCodeFbLinkLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("intermediate-distance", 2),
          ("long-distance", 1),
          ("short-distance", 4),
          ("unknown", 0))
    )


_LocalModuleTrCodeFbLinkLength_Type.__name__ = "Integer32"
_LocalModuleTrCodeFbLinkLength_Object = MibTableColumn
localModuleTrCodeFbLinkLength = _LocalModuleTrCodeFbLinkLength_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 3, 1, 5),
    _LocalModuleTrCodeFbLinkLength_Type()
)
localModuleTrCodeFbLinkLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localModuleTrCodeFbLinkLength.setStatus("mandatory")


class _LocalModuleTrCodeFbTrTech_Type(Integer32):
    """Custom type localModuleTrCodeFbTrTech based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("electrical-inter-enclosure", 16),
          ("electrical-intra-enclosure", 8),
          ("longwave-laser-LC", 32),
          ("longwave-laser-LL", 1),
          ("shortwave-laser-OFC", 2),
          ("shortwave-laser-no-OFC", 4),
          ("unknown", 0))
    )


_LocalModuleTrCodeFbTrTech_Type.__name__ = "Integer32"
_LocalModuleTrCodeFbTrTech_Object = MibTableColumn
localModuleTrCodeFbTrTech = _LocalModuleTrCodeFbTrTech_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 3, 1, 6),
    _LocalModuleTrCodeFbTrTech_Type()
)
localModuleTrCodeFbTrTech.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localModuleTrCodeFbTrTech.setStatus("mandatory")


class _LocalModuleTrCodeFbTrMedia_Type(Integer32):
    """Custom type localModuleTrCodeFbTrMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4,
              8,
              16,
              32,
              64,
              128)
        )
    )
    namedValues = NamedValues(
        *(("miniature-coax", 32),
          ("multi-mode-50", 4),
          ("multi-mode-62-5", 8),
          ("shielded-twisted-pair", 64),
          ("single-mode", 1),
          ("twin-axial-pair", 128),
          ("unknown", 0),
          ("video-coax", 16))
    )


_LocalModuleTrCodeFbTrMedia_Type.__name__ = "Integer32"
_LocalModuleTrCodeFbTrMedia_Object = MibTableColumn
localModuleTrCodeFbTrMedia = _LocalModuleTrCodeFbTrMedia_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 3, 1, 7),
    _LocalModuleTrCodeFbTrMedia_Type()
)
localModuleTrCodeFbTrMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localModuleTrCodeFbTrMedia.setStatus("mandatory")


class _LocalModuleTrCodeFbSpeed_Type(Integer32):
    """Custom type localModuleTrCodeFbSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4,
              16)
        )
    )
    namedValues = NamedValues(
        *(("speed-100MBytes-per-sec", 1),
          ("speed-200MBytes-per-sec", 4),
          ("speed-400MBytes-per-sec", 16),
          ("unknown", 0))
    )


_LocalModuleTrCodeFbSpeed_Type.__name__ = "Integer32"
_LocalModuleTrCodeFbSpeed_Object = MibTableColumn
localModuleTrCodeFbSpeed = _LocalModuleTrCodeFbSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 3, 1, 8),
    _LocalModuleTrCodeFbSpeed_Type()
)
localModuleTrCodeFbSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localModuleTrCodeFbSpeed.setStatus("mandatory")


class _LocalModuleBrNominal_Type(Integer32):
    """Custom type localModuleBrNominal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -255
        )
    )
    namedValues = NamedValues(
        ("unknown", -255)
    )


_LocalModuleBrNominal_Type.__name__ = "Integer32"
_LocalModuleBrNominal_Object = MibTableColumn
localModuleBrNominal = _LocalModuleBrNominal_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 3, 1, 9),
    _LocalModuleBrNominal_Type()
)
localModuleBrNominal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localModuleBrNominal.setStatus("mandatory")


class _LocalModuleLength9km_Type(Integer32):
    """Custom type localModuleLength9km based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -255
        )
    )
    namedValues = NamedValues(
        ("unknown", -255)
    )


_LocalModuleLength9km_Type.__name__ = "Integer32"
_LocalModuleLength9km_Object = MibTableColumn
localModuleLength9km = _LocalModuleLength9km_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 3, 1, 10),
    _LocalModuleLength9km_Type()
)
localModuleLength9km.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localModuleLength9km.setStatus("mandatory")


class _LocalModuleLength9m_Type(Integer32):
    """Custom type localModuleLength9m based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -255
        )
    )
    namedValues = NamedValues(
        ("unknown", -255)
    )


_LocalModuleLength9m_Type.__name__ = "Integer32"
_LocalModuleLength9m_Object = MibTableColumn
localModuleLength9m = _LocalModuleLength9m_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 3, 1, 11),
    _LocalModuleLength9m_Type()
)
localModuleLength9m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localModuleLength9m.setStatus("mandatory")


class _LocalModuleLength50_Type(Integer32):
    """Custom type localModuleLength50 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -255
        )
    )
    namedValues = NamedValues(
        ("unknown", -255)
    )


_LocalModuleLength50_Type.__name__ = "Integer32"
_LocalModuleLength50_Object = MibTableColumn
localModuleLength50 = _LocalModuleLength50_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 3, 1, 12),
    _LocalModuleLength50_Type()
)
localModuleLength50.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localModuleLength50.setStatus("mandatory")


class _LocalModuleLength62_Type(Integer32):
    """Custom type localModuleLength62 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -255
        )
    )
    namedValues = NamedValues(
        ("unknown", -255)
    )


_LocalModuleLength62_Type.__name__ = "Integer32"
_LocalModuleLength62_Object = MibTableColumn
localModuleLength62 = _LocalModuleLength62_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 3, 1, 13),
    _LocalModuleLength62_Type()
)
localModuleLength62.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localModuleLength62.setStatus("mandatory")


class _LocalModuleLengthCopper_Type(Integer32):
    """Custom type localModuleLengthCopper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -255
        )
    )
    namedValues = NamedValues(
        ("unknown", -255)
    )


_LocalModuleLengthCopper_Type.__name__ = "Integer32"
_LocalModuleLengthCopper_Object = MibTableColumn
localModuleLengthCopper = _LocalModuleLengthCopper_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 3, 1, 14),
    _LocalModuleLengthCopper_Type()
)
localModuleLengthCopper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localModuleLengthCopper.setStatus("mandatory")


class _LocalModuleVendorSN_Type(DisplayString):
    """Custom type localModuleVendorSN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_LocalModuleVendorSN_Type.__name__ = "DisplayString"
_LocalModuleVendorSN_Object = MibTableColumn
localModuleVendorSN = _LocalModuleVendorSN_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 3, 1, 15),
    _LocalModuleVendorSN_Type()
)
localModuleVendorSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localModuleVendorSN.setStatus("mandatory")


class _LocalModuleDateCode_Type(DisplayString):
    """Custom type localModuleDateCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_LocalModuleDateCode_Type.__name__ = "DisplayString"
_LocalModuleDateCode_Object = MibTableColumn
localModuleDateCode = _LocalModuleDateCode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 3, 1, 16),
    _LocalModuleDateCode_Type()
)
localModuleDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localModuleDateCode.setStatus("mandatory")


class _LocalModuleLaserCurrent_Type(Integer32):
    """Custom type localModuleLaserCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -255
        )
    )
    namedValues = NamedValues(
        ("unknown", -255)
    )


_LocalModuleLaserCurrent_Type.__name__ = "Integer32"
_LocalModuleLaserCurrent_Object = MibTableColumn
localModuleLaserCurrent = _LocalModuleLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 3, 1, 17),
    _LocalModuleLaserCurrent_Type()
)
localModuleLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localModuleLaserCurrent.setStatus("optional")


class _LocalModuleTransmittedPower_Type(Integer32):
    """Custom type localModuleTransmittedPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -255
        )
    )
    namedValues = NamedValues(
        ("unknown", -255)
    )


_LocalModuleTransmittedPower_Type.__name__ = "Integer32"
_LocalModuleTransmittedPower_Object = MibTableColumn
localModuleTransmittedPower = _LocalModuleTransmittedPower_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 3, 1, 18),
    _LocalModuleTransmittedPower_Type()
)
localModuleTransmittedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localModuleTransmittedPower.setStatus("optional")


class _LocalModuleReceivedPower_Type(Integer32):
    """Custom type localModuleReceivedPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -255
        )
    )
    namedValues = NamedValues(
        ("unknown", -255)
    )


_LocalModuleReceivedPower_Type.__name__ = "Integer32"
_LocalModuleReceivedPower_Object = MibTableColumn
localModuleReceivedPower = _LocalModuleReceivedPower_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 3, 1, 19),
    _LocalModuleReceivedPower_Type()
)
localModuleReceivedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localModuleReceivedPower.setStatus("optional")


class _LocalModuleLaserTemperature_Type(Integer32):
    """Custom type localModuleLaserTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -255
        )
    )
    namedValues = NamedValues(
        ("unknown", -255)
    )


_LocalModuleLaserTemperature_Type.__name__ = "Integer32"
_LocalModuleLaserTemperature_Object = MibTableColumn
localModuleLaserTemperature = _LocalModuleLaserTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 3, 1, 20),
    _LocalModuleLaserTemperature_Type()
)
localModuleLaserTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localModuleLaserTemperature.setStatus("optional")


class _LocalModuleVoltage_Type(Integer32):
    """Custom type localModuleVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -255
        )
    )
    namedValues = NamedValues(
        ("unknown", -255)
    )


_LocalModuleVoltage_Type.__name__ = "Integer32"
_LocalModuleVoltage_Object = MibTableColumn
localModuleVoltage = _LocalModuleVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 3, 1, 21),
    _LocalModuleVoltage_Type()
)
localModuleVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localModuleVoltage.setStatus("optional")
_LineModuleTable_Object = MibTable
lineModuleTable = _LineModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 4)
)
if mibBuilder.loadTexts:
    lineModuleTable.setStatus("mandatory")
_LineModuleTableEntry_Object = MibTableRow
lineModuleTableEntry = _LineModuleTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 4, 1)
)
lineModuleTableEntry.setIndexNames(
    (0, "MICROSENS-CWDM8-MIB", "lineModuleId"),
)
if mibBuilder.loadTexts:
    lineModuleTableEntry.setStatus("mandatory")
_LineModuleId_Type = Integer32
_LineModuleId_Object = MibTableColumn
lineModuleId = _LineModuleId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 4, 1, 1),
    _LineModuleId_Type()
)
lineModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineModuleId.setStatus("mandatory")


class _LineModuleConnector_Type(Integer32):
    """Custom type lineModuleConnector based on Integer32"""
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
              32,
              33)
        )
    )
    namedValues = NamedValues(
        *(("bnc-tnc", 4),
          ("coaxial-headers", 5),
          ("copperpigtail", 33),
          ("fiberjack", 6),
          ("hssdc2", 32),
          ("lc", 7),
          ("mt-rj", 8),
          ("mu", 9),
          ("opticalpigtail", 11),
          ("sc", 1),
          ("sg", 10),
          ("style1-copper", 2),
          ("style2-copper", 3),
          ("unknown", 0))
    )


_LineModuleConnector_Type.__name__ = "Integer32"
_LineModuleConnector_Object = MibTableColumn
lineModuleConnector = _LineModuleConnector_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 4, 1, 2),
    _LineModuleConnector_Type()
)
lineModuleConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineModuleConnector.setStatus("mandatory")


class _LineModuleTrCodeSonet_Type(Integer32):
    """Custom type lineModuleTrCodeSonet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              16,
              32,
              64,
              128,
              256,
              512)
        )
    )
    namedValues = NamedValues(
        *(("oc12-multi-mode-short-reach", 16),
          ("oc12-single-mode-intermediate-reach", 32),
          ("oc12-single-mode-long-reach", 64),
          ("oc3-multi-mode-short-reach", 1),
          ("oc3-single-mode-intermediate-reach", 2),
          ("oc3-single-mode-long-reach", 4),
          ("oc48-intermediate-reach", 256),
          ("oc48-long-reach", 512),
          ("oc48-short-reach", 128),
          ("unknown", 0))
    )


_LineModuleTrCodeSonet_Type.__name__ = "Integer32"
_LineModuleTrCodeSonet_Object = MibTableColumn
lineModuleTrCodeSonet = _LineModuleTrCodeSonet_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 4, 1, 3),
    _LineModuleTrCodeSonet_Type()
)
lineModuleTrCodeSonet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineModuleTrCodeSonet.setStatus("mandatory")


class _LineModuleTrCodeGigabit_Type(Integer32):
    """Custom type lineModuleTrCodeGigabit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("base-1000-CX", 4),
          ("base-1000-LX", 2),
          ("base-1000-SX", 1),
          ("base-1000-T", 8),
          ("unknown", 0))
    )


_LineModuleTrCodeGigabit_Type.__name__ = "Integer32"
_LineModuleTrCodeGigabit_Object = MibTableColumn
lineModuleTrCodeGigabit = _LineModuleTrCodeGigabit_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 4, 1, 4),
    _LineModuleTrCodeGigabit_Type()
)
lineModuleTrCodeGigabit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineModuleTrCodeGigabit.setStatus("mandatory")


class _LineModuleTrCodeFbLinkLength_Type(Integer32):
    """Custom type lineModuleTrCodeFbLinkLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("intermediate-distance", 2),
          ("long-distance", 1),
          ("short-distance", 4),
          ("unknown", 0))
    )


_LineModuleTrCodeFbLinkLength_Type.__name__ = "Integer32"
_LineModuleTrCodeFbLinkLength_Object = MibTableColumn
lineModuleTrCodeFbLinkLength = _LineModuleTrCodeFbLinkLength_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 4, 1, 5),
    _LineModuleTrCodeFbLinkLength_Type()
)
lineModuleTrCodeFbLinkLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineModuleTrCodeFbLinkLength.setStatus("mandatory")


class _LineModuleTrCodeFbTrTech_Type(Integer32):
    """Custom type lineModuleTrCodeFbTrTech based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("electrical-inter-enclosure", 16),
          ("electrical-intra-enclosure", 8),
          ("longwave-laser-LC", 32),
          ("longwave-laser-LL", 1),
          ("shortwave-laser-OFC", 2),
          ("shortwave-laser-no-OFC", 4),
          ("unknown", 0))
    )


_LineModuleTrCodeFbTrTech_Type.__name__ = "Integer32"
_LineModuleTrCodeFbTrTech_Object = MibTableColumn
lineModuleTrCodeFbTrTech = _LineModuleTrCodeFbTrTech_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 4, 1, 6),
    _LineModuleTrCodeFbTrTech_Type()
)
lineModuleTrCodeFbTrTech.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineModuleTrCodeFbTrTech.setStatus("mandatory")


class _LineModuleTrCodeFbTrMedia_Type(Integer32):
    """Custom type lineModuleTrCodeFbTrMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4,
              8,
              16,
              32,
              64,
              128)
        )
    )
    namedValues = NamedValues(
        *(("miniature-coax", 32),
          ("multi-mode-50", 4),
          ("multi-mode-62-5", 8),
          ("shielded-twisted-pair", 64),
          ("single-mode", 1),
          ("twin-axial-pair", 128),
          ("unknown", 0),
          ("video-coax", 16))
    )


_LineModuleTrCodeFbTrMedia_Type.__name__ = "Integer32"
_LineModuleTrCodeFbTrMedia_Object = MibTableColumn
lineModuleTrCodeFbTrMedia = _LineModuleTrCodeFbTrMedia_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 4, 1, 7),
    _LineModuleTrCodeFbTrMedia_Type()
)
lineModuleTrCodeFbTrMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineModuleTrCodeFbTrMedia.setStatus("mandatory")


class _LineModuleTrCodeFbSpeed_Type(Integer32):
    """Custom type lineModuleTrCodeFbSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4,
              16)
        )
    )
    namedValues = NamedValues(
        *(("speed-100MBytes-per-sec", 1),
          ("speed-200MBytes-per-sec", 4),
          ("speed-400MBytes-per-sec", 16),
          ("unknown", 0))
    )


_LineModuleTrCodeFbSpeed_Type.__name__ = "Integer32"
_LineModuleTrCodeFbSpeed_Object = MibTableColumn
lineModuleTrCodeFbSpeed = _LineModuleTrCodeFbSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 4, 1, 8),
    _LineModuleTrCodeFbSpeed_Type()
)
lineModuleTrCodeFbSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineModuleTrCodeFbSpeed.setStatus("mandatory")


class _LineModuleBrNominal_Type(Integer32):
    """Custom type lineModuleBrNominal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -255
        )
    )
    namedValues = NamedValues(
        ("unknown", -255)
    )


_LineModuleBrNominal_Type.__name__ = "Integer32"
_LineModuleBrNominal_Object = MibTableColumn
lineModuleBrNominal = _LineModuleBrNominal_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 4, 1, 9),
    _LineModuleBrNominal_Type()
)
lineModuleBrNominal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineModuleBrNominal.setStatus("mandatory")


class _LineModuleLength9km_Type(Integer32):
    """Custom type lineModuleLength9km based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -255
        )
    )
    namedValues = NamedValues(
        ("unknown", -255)
    )


_LineModuleLength9km_Type.__name__ = "Integer32"
_LineModuleLength9km_Object = MibTableColumn
lineModuleLength9km = _LineModuleLength9km_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 4, 1, 10),
    _LineModuleLength9km_Type()
)
lineModuleLength9km.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineModuleLength9km.setStatus("mandatory")


class _LineModuleLength9m_Type(Integer32):
    """Custom type lineModuleLength9m based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -255
        )
    )
    namedValues = NamedValues(
        ("unknown", -255)
    )


_LineModuleLength9m_Type.__name__ = "Integer32"
_LineModuleLength9m_Object = MibTableColumn
lineModuleLength9m = _LineModuleLength9m_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 4, 1, 11),
    _LineModuleLength9m_Type()
)
lineModuleLength9m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineModuleLength9m.setStatus("mandatory")


class _LineModuleLength50_Type(Integer32):
    """Custom type lineModuleLength50 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -255
        )
    )
    namedValues = NamedValues(
        ("unknown", -255)
    )


_LineModuleLength50_Type.__name__ = "Integer32"
_LineModuleLength50_Object = MibTableColumn
lineModuleLength50 = _LineModuleLength50_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 4, 1, 12),
    _LineModuleLength50_Type()
)
lineModuleLength50.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineModuleLength50.setStatus("mandatory")


class _LineModuleLength62_Type(Integer32):
    """Custom type lineModuleLength62 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -255
        )
    )
    namedValues = NamedValues(
        ("unknown", -255)
    )


_LineModuleLength62_Type.__name__ = "Integer32"
_LineModuleLength62_Object = MibTableColumn
lineModuleLength62 = _LineModuleLength62_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 4, 1, 13),
    _LineModuleLength62_Type()
)
lineModuleLength62.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineModuleLength62.setStatus("mandatory")


class _LineModuleLengthCopper_Type(Integer32):
    """Custom type lineModuleLengthCopper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -255
        )
    )
    namedValues = NamedValues(
        ("unknown", -255)
    )


_LineModuleLengthCopper_Type.__name__ = "Integer32"
_LineModuleLengthCopper_Object = MibTableColumn
lineModuleLengthCopper = _LineModuleLengthCopper_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 4, 1, 14),
    _LineModuleLengthCopper_Type()
)
lineModuleLengthCopper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineModuleLengthCopper.setStatus("mandatory")


class _LineModuleVendorSN_Type(DisplayString):
    """Custom type lineModuleVendorSN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_LineModuleVendorSN_Type.__name__ = "DisplayString"
_LineModuleVendorSN_Object = MibTableColumn
lineModuleVendorSN = _LineModuleVendorSN_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 4, 1, 15),
    _LineModuleVendorSN_Type()
)
lineModuleVendorSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineModuleVendorSN.setStatus("mandatory")


class _LineModuleDateCode_Type(DisplayString):
    """Custom type lineModuleDateCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_LineModuleDateCode_Type.__name__ = "DisplayString"
_LineModuleDateCode_Object = MibTableColumn
lineModuleDateCode = _LineModuleDateCode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 4, 1, 16),
    _LineModuleDateCode_Type()
)
lineModuleDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineModuleDateCode.setStatus("mandatory")


class _LineModuleLaserCurrent_Type(Integer32):
    """Custom type lineModuleLaserCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -255
        )
    )
    namedValues = NamedValues(
        ("unknown", -255)
    )


_LineModuleLaserCurrent_Type.__name__ = "Integer32"
_LineModuleLaserCurrent_Object = MibTableColumn
lineModuleLaserCurrent = _LineModuleLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 4, 1, 17),
    _LineModuleLaserCurrent_Type()
)
lineModuleLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineModuleLaserCurrent.setStatus("mandatory")


class _LineModuleTransmittedPower_Type(Integer32):
    """Custom type lineModuleTransmittedPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -255
        )
    )
    namedValues = NamedValues(
        ("unknown", -255)
    )


_LineModuleTransmittedPower_Type.__name__ = "Integer32"
_LineModuleTransmittedPower_Object = MibTableColumn
lineModuleTransmittedPower = _LineModuleTransmittedPower_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 4, 1, 18),
    _LineModuleTransmittedPower_Type()
)
lineModuleTransmittedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineModuleTransmittedPower.setStatus("mandatory")


class _LineModuleReceivedPower_Type(Integer32):
    """Custom type lineModuleReceivedPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -255
        )
    )
    namedValues = NamedValues(
        ("unknown", -255)
    )


_LineModuleReceivedPower_Type.__name__ = "Integer32"
_LineModuleReceivedPower_Object = MibTableColumn
lineModuleReceivedPower = _LineModuleReceivedPower_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 4, 1, 19),
    _LineModuleReceivedPower_Type()
)
lineModuleReceivedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineModuleReceivedPower.setStatus("mandatory")


class _LineModuleLaserTemperature_Type(Integer32):
    """Custom type lineModuleLaserTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -255
        )
    )
    namedValues = NamedValues(
        ("unknown", -255)
    )


_LineModuleLaserTemperature_Type.__name__ = "Integer32"
_LineModuleLaserTemperature_Object = MibTableColumn
lineModuleLaserTemperature = _LineModuleLaserTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 4, 1, 20),
    _LineModuleLaserTemperature_Type()
)
lineModuleLaserTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineModuleLaserTemperature.setStatus("mandatory")


class _LineModuleVoltage_Type(Integer32):
    """Custom type lineModuleVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -255
        )
    )
    namedValues = NamedValues(
        ("unknown", -255)
    )


_LineModuleVoltage_Type.__name__ = "Integer32"
_LineModuleVoltage_Object = MibTableColumn
lineModuleVoltage = _LineModuleVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 4, 1, 21),
    _LineModuleVoltage_Type()
)
lineModuleVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineModuleVoltage.setStatus("mandatory")
_PowerTable_Object = MibTable
powerTable = _PowerTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 5)
)
if mibBuilder.loadTexts:
    powerTable.setStatus("mandatory")
_PowerTableEntry_Object = MibTableRow
powerTableEntry = _PowerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 5, 1)
)
powerTableEntry.setIndexNames(
    (0, "MICROSENS-CWDM8-MIB", "powerId"),
)
if mibBuilder.loadTexts:
    powerTableEntry.setStatus("mandatory")
_PowerId_Type = Integer32
_PowerId_Object = MibTableColumn
powerId = _PowerId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 5, 1, 1),
    _PowerId_Type()
)
powerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerId.setStatus("mandatory")


class _PowerArtNo_Type(DisplayString):
    """Custom type powerArtNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PowerArtNo_Type.__name__ = "DisplayString"
_PowerArtNo_Object = MibTableColumn
powerArtNo = _PowerArtNo_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 5, 1, 2),
    _PowerArtNo_Type()
)
powerArtNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerArtNo.setStatus("mandatory")


class _PowerSerNo_Type(DisplayString):
    """Custom type powerSerNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PowerSerNo_Type.__name__ = "DisplayString"
_PowerSerNo_Object = MibTableColumn
powerSerNo = _PowerSerNo_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 5, 1, 3),
    _PowerSerNo_Type()
)
powerSerNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSerNo.setStatus("mandatory")


class _PowerDesc_Type(DisplayString):
    """Custom type powerDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PowerDesc_Type.__name__ = "DisplayString"
_PowerDesc_Object = MibTableColumn
powerDesc = _PowerDesc_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 5, 1, 4),
    _PowerDesc_Type()
)
powerDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDesc.setStatus("mandatory")


class _PowerTemperature_Type(Integer32):
    """Custom type powerTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -255
        )
    )
    namedValues = NamedValues(
        ("unknown", -255)
    )


_PowerTemperature_Type.__name__ = "Integer32"
_PowerTemperature_Object = MibTableColumn
powerTemperature = _PowerTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 5, 1, 5),
    _PowerTemperature_Type()
)
powerTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerTemperature.setStatus("mandatory")


class _PowerStatus_Type(Integer32):
    """Custom type powerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-255,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("not-active", 0),
          ("unknown", -255))
    )


_PowerStatus_Type.__name__ = "Integer32"
_PowerStatus_Object = MibTableColumn
powerStatus = _PowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 5, 1, 6),
    _PowerStatus_Type()
)
powerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerStatus.setStatus("mandatory")


class _PowerSuppliedPower_Type(Integer32):
    """Custom type powerSuppliedPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -255
        )
    )
    namedValues = NamedValues(
        ("unknown", -255)
    )


_PowerSuppliedPower_Type.__name__ = "Integer32"
_PowerSuppliedPower_Object = MibTableColumn
powerSuppliedPower = _PowerSuppliedPower_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 5, 1, 7),
    _PowerSuppliedPower_Type()
)
powerSuppliedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSuppliedPower.setStatus("mandatory")


class _PowerLoad_Type(Integer32):
    """Custom type powerLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -255
        )
    )
    namedValues = NamedValues(
        ("unknown", -255)
    )


_PowerLoad_Type.__name__ = "Integer32"
_PowerLoad_Object = MibTableColumn
powerLoad = _PowerLoad_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 5, 1, 8),
    _PowerLoad_Type()
)
powerLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerLoad.setStatus("mandatory")


class _PowerFanStatus_Type(Integer32):
    """Custom type powerFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-255,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("not-active", 0),
          ("unknown", -255))
    )


_PowerFanStatus_Type.__name__ = "Integer32"
_PowerFanStatus_Object = MibTableColumn
powerFanStatus = _PowerFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 5, 1, 9),
    _PowerFanStatus_Type()
)
powerFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerFanStatus.setStatus("mandatory")
_LineIfTable_Object = MibTable
lineIfTable = _LineIfTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 6)
)
if mibBuilder.loadTexts:
    lineIfTable.setStatus("mandatory")
_LineIfTableEntry_Object = MibTableRow
lineIfTableEntry = _LineIfTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 6, 1)
)
lineIfTableEntry.setIndexNames(
    (0, "MICROSENS-CWDM8-MIB", "lineIfId"),
)
if mibBuilder.loadTexts:
    lineIfTableEntry.setStatus("mandatory")
_LineIfId_Type = Integer32
_LineIfId_Object = MibTableColumn
lineIfId = _LineIfId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 6, 1, 1),
    _LineIfId_Type()
)
lineIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineIfId.setStatus("mandatory")


class _LineIfArtNo_Type(DisplayString):
    """Custom type lineIfArtNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_LineIfArtNo_Type.__name__ = "DisplayString"
_LineIfArtNo_Object = MibTableColumn
lineIfArtNo = _LineIfArtNo_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 6, 1, 2),
    _LineIfArtNo_Type()
)
lineIfArtNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineIfArtNo.setStatus("mandatory")


class _LineIfSerNo_Type(DisplayString):
    """Custom type lineIfSerNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_LineIfSerNo_Type.__name__ = "DisplayString"
_LineIfSerNo_Object = MibTableColumn
lineIfSerNo = _LineIfSerNo_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 6, 1, 3),
    _LineIfSerNo_Type()
)
lineIfSerNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineIfSerNo.setStatus("mandatory")


class _LineIfWestLinkStatus_Type(Integer32):
    """Custom type lineIfWestLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-255,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("unknown", -255))
    )


_LineIfWestLinkStatus_Type.__name__ = "Integer32"
_LineIfWestLinkStatus_Object = MibTableColumn
lineIfWestLinkStatus = _LineIfWestLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 6, 1, 4),
    _LineIfWestLinkStatus_Type()
)
lineIfWestLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineIfWestLinkStatus.setStatus("optional")


class _LineIfEastLinkStatus_Type(Integer32):
    """Custom type lineIfEastLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-255,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("unknown", -255))
    )


_LineIfEastLinkStatus_Type.__name__ = "Integer32"
_LineIfEastLinkStatus_Object = MibTableColumn
lineIfEastLinkStatus = _LineIfEastLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 6, 1, 5),
    _LineIfEastLinkStatus_Type()
)
lineIfEastLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineIfEastLinkStatus.setStatus("optional")


class _LineIfWestChannelStatus_Type(Integer32):
    """Custom type lineIfWestChannelStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-255,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("in-use", 1),
          ("not-in-use", 0),
          ("unknown", -255))
    )


_LineIfWestChannelStatus_Type.__name__ = "Integer32"
_LineIfWestChannelStatus_Object = MibTableColumn
lineIfWestChannelStatus = _LineIfWestChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 6, 1, 6),
    _LineIfWestChannelStatus_Type()
)
lineIfWestChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineIfWestChannelStatus.setStatus("optional")


class _LineIfEastChannelStatus_Type(Integer32):
    """Custom type lineIfEastChannelStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-255,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("in-use", 1),
          ("not-in-use", 0),
          ("unknown", -255))
    )


_LineIfEastChannelStatus_Type.__name__ = "Integer32"
_LineIfEastChannelStatus_Object = MibTableColumn
lineIfEastChannelStatus = _LineIfEastChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 6, 1, 7),
    _LineIfEastChannelStatus_Type()
)
lineIfEastChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineIfEastChannelStatus.setStatus("optional")


class _LineIfWestLinkRcvPower_Type(Integer32):
    """Custom type lineIfWestLinkRcvPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -255
        )
    )
    namedValues = NamedValues(
        ("unknown", -255)
    )


_LineIfWestLinkRcvPower_Type.__name__ = "Integer32"
_LineIfWestLinkRcvPower_Object = MibTableColumn
lineIfWestLinkRcvPower = _LineIfWestLinkRcvPower_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 6, 1, 8),
    _LineIfWestLinkRcvPower_Type()
)
lineIfWestLinkRcvPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineIfWestLinkRcvPower.setStatus("optional")


class _LineIfEastLinkRcvPower_Type(Integer32):
    """Custom type lineIfEastLinkRcvPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -255
        )
    )
    namedValues = NamedValues(
        ("unknown", -255)
    )


_LineIfEastLinkRcvPower_Type.__name__ = "Integer32"
_LineIfEastLinkRcvPower_Object = MibTableColumn
lineIfEastLinkRcvPower = _LineIfEastLinkRcvPower_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 6, 1, 9),
    _LineIfEastLinkRcvPower_Type()
)
lineIfEastLinkRcvPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineIfEastLinkRcvPower.setStatus("optional")
_PassiveTable_Object = MibTable
passiveTable = _PassiveTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 7)
)
if mibBuilder.loadTexts:
    passiveTable.setStatus("mandatory")
_PassiveTableEntry_Object = MibTableRow
passiveTableEntry = _PassiveTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 7, 1)
)
passiveTableEntry.setIndexNames(
    (0, "MICROSENS-CWDM8-MIB", "passiveId"),
)
if mibBuilder.loadTexts:
    passiveTableEntry.setStatus("mandatory")
_PassiveId_Type = Integer32
_PassiveId_Object = MibTableColumn
passiveId = _PassiveId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 7, 1, 1),
    _PassiveId_Type()
)
passiveId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    passiveId.setStatus("mandatory")


class _PassiveArtNo_Type(DisplayString):
    """Custom type passiveArtNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PassiveArtNo_Type.__name__ = "DisplayString"
_PassiveArtNo_Object = MibTableColumn
passiveArtNo = _PassiveArtNo_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 7, 1, 2),
    _PassiveArtNo_Type()
)
passiveArtNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    passiveArtNo.setStatus("mandatory")


class _PassiveSerNo_Type(DisplayString):
    """Custom type passiveSerNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PassiveSerNo_Type.__name__ = "DisplayString"
_PassiveSerNo_Object = MibTableColumn
passiveSerNo = _PassiveSerNo_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 7, 1, 3),
    _PassiveSerNo_Type()
)
passiveSerNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    passiveSerNo.setStatus("mandatory")
_ChannelCount_Type = Integer32
_ChannelCount_Object = MibScalar
channelCount = _ChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 100),
    _ChannelCount_Type()
)
channelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelCount.setStatus("mandatory")

# Managed Objects groups


# Notification objects

minorAlarmRelayTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 0, 0)
)
minorAlarmRelayTrap.setObjects(
    ("MICROSENS-CWDM8-MIB", "deviceMinorAlarm")
)
if mibBuilder.loadTexts:
    minorAlarmRelayTrap.setStatus(
        ""
    )

majorAlarmRelayTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 0, 1)
)
majorAlarmRelayTrap.setObjects(
    ("MICROSENS-CWDM8-MIB", "deviceMajorAlarm")
)
if mibBuilder.loadTexts:
    majorAlarmRelayTrap.setStatus(
        ""
    )

devicePowerSupplyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 0, 2)
)
devicePowerSupplyTrap.setObjects(
      *(("MICROSENS-CWDM8-MIB", "powerId"),
        ("MICROSENS-CWDM8-MIB", "powerStatus"))
)
if mibBuilder.loadTexts:
    devicePowerSupplyTrap.setStatus(
        ""
    )

deviceTemperatureAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 0, 3)
)
deviceTemperatureAlarmTrap.setObjects(
      *(("MICROSENS-CWDM8-MIB", "deviceTemperature"),
        ("MICROSENS-CWDM8-MIB", "deviceTempAlarm"))
)
if mibBuilder.loadTexts:
    deviceTemperatureAlarmTrap.setStatus(
        ""
    )

deviceTemperatureShutdownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 0, 4)
)
deviceTemperatureShutdownTrap.setObjects(
      *(("MICROSENS-CWDM8-MIB", "deviceTemperature"),
        ("MICROSENS-CWDM8-MIB", "deviceTempShutdown"))
)
if mibBuilder.loadTexts:
    deviceTemperatureShutdownTrap.setStatus(
        ""
    )

fanAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 0, 5)
)
fanAlarmTrap.setObjects(
      *(("MICROSENS-CWDM8-MIB", "powerId"),
        ("MICROSENS-CWDM8-MIB", "powerFanStatus"))
)
if mibBuilder.loadTexts:
    fanAlarmTrap.setStatus(
        ""
    )

portLocalLinkChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 0, 6)
)
portLocalLinkChangeTrap.setObjects(
      *(("MICROSENS-CWDM8-MIB", "portId"),
        ("MICROSENS-CWDM8-MIB", "portLocalLink"))
)
if mibBuilder.loadTexts:
    portLocalLinkChangeTrap.setStatus(
        ""
    )

portLineLinkChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 6, 4, 0, 7)
)
portLineLinkChangeTrap.setObjects(
      *(("MICROSENS-CWDM8-MIB", "portId"),
        ("MICROSENS-CWDM8-MIB", "portLineLink"))
)
if mibBuilder.loadTexts:
    portLineLinkChangeTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MICROSENS-CWDM8-MIB",
    **{"microsens": microsens,
       "cwdm": cwdm,
       "eightChannelCwdm": eightChannelCwdm,
       "minorAlarmRelayTrap": minorAlarmRelayTrap,
       "majorAlarmRelayTrap": majorAlarmRelayTrap,
       "devicePowerSupplyTrap": devicePowerSupplyTrap,
       "deviceTemperatureAlarmTrap": deviceTemperatureAlarmTrap,
       "deviceTemperatureShutdownTrap": deviceTemperatureShutdownTrap,
       "fanAlarmTrap": fanAlarmTrap,
       "portLocalLinkChangeTrap": portLocalLinkChangeTrap,
       "portLineLinkChangeTrap": portLineLinkChangeTrap,
       "deviceTable": deviceTable,
       "deviceTableEntry": deviceTableEntry,
       "deviceId": deviceId,
       "deviceArtNo": deviceArtNo,
       "deviceSerNo": deviceSerNo,
       "deviceDesc": deviceDesc,
       "deviceTemperature": deviceTemperature,
       "deviceTempAlarmThreshold": deviceTempAlarmThreshold,
       "deviceTempAlarm": deviceTempAlarm,
       "deviceTempShutdown": deviceTempShutdown,
       "deviceTrPowerFailureAlarm": deviceTrPowerFailureAlarm,
       "deviceMinorAlarm": deviceMinorAlarm,
       "deviceMajorAlarm": deviceMajorAlarm,
       "portTable": portTable,
       "portTableEntry": portTableEntry,
       "portId": portId,
       "portChannelEnabled": portChannelEnabled,
       "portLinkThroughLocalLine": portLinkThroughLocalLine,
       "portLinkThroughLineLocal": portLinkThroughLineLocal,
       "portLocalModuleInstalled": portLocalModuleInstalled,
       "portLineModuleInstalled": portLineModuleInstalled,
       "portLocalLink": portLocalLink,
       "portLineLink": portLineLink,
       "portLocalTxFault": portLocalTxFault,
       "portLineTxFault": portLineTxFault,
       "portLocalPowerFault": portLocalPowerFault,
       "portLinePowerFault": portLinePowerFault,
       "portRateSelect": portRateSelect,
       "localModuleTable": localModuleTable,
       "localModuleTableEntry": localModuleTableEntry,
       "localModuleId": localModuleId,
       "localModuleConnector": localModuleConnector,
       "localModuleTrCodeSonet": localModuleTrCodeSonet,
       "localModuleTrCodeGigabit": localModuleTrCodeGigabit,
       "localModuleTrCodeFbLinkLength": localModuleTrCodeFbLinkLength,
       "localModuleTrCodeFbTrTech": localModuleTrCodeFbTrTech,
       "localModuleTrCodeFbTrMedia": localModuleTrCodeFbTrMedia,
       "localModuleTrCodeFbSpeed": localModuleTrCodeFbSpeed,
       "localModuleBrNominal": localModuleBrNominal,
       "localModuleLength9km": localModuleLength9km,
       "localModuleLength9m": localModuleLength9m,
       "localModuleLength50": localModuleLength50,
       "localModuleLength62": localModuleLength62,
       "localModuleLengthCopper": localModuleLengthCopper,
       "localModuleVendorSN": localModuleVendorSN,
       "localModuleDateCode": localModuleDateCode,
       "localModuleLaserCurrent": localModuleLaserCurrent,
       "localModuleTransmittedPower": localModuleTransmittedPower,
       "localModuleReceivedPower": localModuleReceivedPower,
       "localModuleLaserTemperature": localModuleLaserTemperature,
       "localModuleVoltage": localModuleVoltage,
       "lineModuleTable": lineModuleTable,
       "lineModuleTableEntry": lineModuleTableEntry,
       "lineModuleId": lineModuleId,
       "lineModuleConnector": lineModuleConnector,
       "lineModuleTrCodeSonet": lineModuleTrCodeSonet,
       "lineModuleTrCodeGigabit": lineModuleTrCodeGigabit,
       "lineModuleTrCodeFbLinkLength": lineModuleTrCodeFbLinkLength,
       "lineModuleTrCodeFbTrTech": lineModuleTrCodeFbTrTech,
       "lineModuleTrCodeFbTrMedia": lineModuleTrCodeFbTrMedia,
       "lineModuleTrCodeFbSpeed": lineModuleTrCodeFbSpeed,
       "lineModuleBrNominal": lineModuleBrNominal,
       "lineModuleLength9km": lineModuleLength9km,
       "lineModuleLength9m": lineModuleLength9m,
       "lineModuleLength50": lineModuleLength50,
       "lineModuleLength62": lineModuleLength62,
       "lineModuleLengthCopper": lineModuleLengthCopper,
       "lineModuleVendorSN": lineModuleVendorSN,
       "lineModuleDateCode": lineModuleDateCode,
       "lineModuleLaserCurrent": lineModuleLaserCurrent,
       "lineModuleTransmittedPower": lineModuleTransmittedPower,
       "lineModuleReceivedPower": lineModuleReceivedPower,
       "lineModuleLaserTemperature": lineModuleLaserTemperature,
       "lineModuleVoltage": lineModuleVoltage,
       "powerTable": powerTable,
       "powerTableEntry": powerTableEntry,
       "powerId": powerId,
       "powerArtNo": powerArtNo,
       "powerSerNo": powerSerNo,
       "powerDesc": powerDesc,
       "powerTemperature": powerTemperature,
       "powerStatus": powerStatus,
       "powerSuppliedPower": powerSuppliedPower,
       "powerLoad": powerLoad,
       "powerFanStatus": powerFanStatus,
       "lineIfTable": lineIfTable,
       "lineIfTableEntry": lineIfTableEntry,
       "lineIfId": lineIfId,
       "lineIfArtNo": lineIfArtNo,
       "lineIfSerNo": lineIfSerNo,
       "lineIfWestLinkStatus": lineIfWestLinkStatus,
       "lineIfEastLinkStatus": lineIfEastLinkStatus,
       "lineIfWestChannelStatus": lineIfWestChannelStatus,
       "lineIfEastChannelStatus": lineIfEastChannelStatus,
       "lineIfWestLinkRcvPower": lineIfWestLinkRcvPower,
       "lineIfEastLinkRcvPower": lineIfEastLinkRcvPower,
       "passiveTable": passiveTable,
       "passiveTableEntry": passiveTableEntry,
       "passiveId": passiveId,
       "passiveArtNo": passiveArtNo,
       "passiveSerNo": passiveSerNo,
       "channelCount": channelCount}
)
