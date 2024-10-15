# SNMP MIB module (INTEL-S500-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTEL-S500-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:59 2024
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

(mib2ext,) = mibBuilder.importSymbols(
    "INTEL-GEN-MIB",
    "mib2ext")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_S500_ObjectIdentity = ObjectIdentity
s500 = _S500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 10)
)
_Module_ObjectIdentity = ObjectIdentity
module = _Module_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 1)
)


class _DefaultSwitchMode_Type(Integer32):
    """Custom type defaultSwitchMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 5),
          ("cutThrough", 2),
          ("fragmentFree", 3),
          ("storeAndForward", 4))
    )


_DefaultSwitchMode_Type.__name__ = "Integer32"
_DefaultSwitchMode_Object = MibScalar
defaultSwitchMode = _DefaultSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 1, 1),
    _DefaultSwitchMode_Type()
)
defaultSwitchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultSwitchMode.setStatus("mandatory")


class _DefaultFlowControlMode_Type(Integer32):
    """Custom type defaultFlowControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2))
    )


_DefaultFlowControlMode_Type.__name__ = "Integer32"
_DefaultFlowControlMode_Object = MibScalar
defaultFlowControlMode = _DefaultFlowControlMode_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 1, 2),
    _DefaultFlowControlMode_Type()
)
defaultFlowControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultFlowControlMode.setStatus("mandatory")


class _SmuMaster_Type(Integer32):
    """Custom type smuMaster based on Integer32"""
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


_SmuMaster_Type.__name__ = "Integer32"
_SmuMaster_Object = MibScalar
smuMaster = _SmuMaster_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 1, 3),
    _SmuMaster_Type()
)
smuMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smuMaster.setStatus("mandatory")
_LocalManagementTimeout_Type = Integer32
_LocalManagementTimeout_Object = MibScalar
localManagementTimeout = _LocalManagementTimeout_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 1, 4),
    _LocalManagementTimeout_Type()
)
localManagementTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localManagementTimeout.setStatus("mandatory")


class _TemperatureLevel_Type(Integer32):
    """Custom type temperatureLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("high", 2),
          ("normal", 1))
    )


_TemperatureLevel_Type.__name__ = "Integer32"
_TemperatureLevel_Object = MibScalar
temperatureLevel = _TemperatureLevel_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 1, 5),
    _TemperatureLevel_Type()
)
temperatureLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureLevel.setStatus("mandatory")


class _RedundantPowerSupplyStatus_Type(Integer32):
    """Custom type redundantPowerSupplyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("notPresent", 1),
          ("present", 2))
    )


_RedundantPowerSupplyStatus_Type.__name__ = "Integer32"
_RedundantPowerSupplyStatus_Object = MibScalar
redundantPowerSupplyStatus = _RedundantPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 1, 6),
    _RedundantPowerSupplyStatus_Type()
)
redundantPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundantPowerSupplyStatus.setStatus("mandatory")


class _PortMirroring_Type(Integer32):
    """Custom type portMirroring based on Integer32"""
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


_PortMirroring_Type.__name__ = "Integer32"
_PortMirroring_Object = MibScalar
portMirroring = _PortMirroring_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 1, 7),
    _PortMirroring_Type()
)
portMirroring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portMirroring.setStatus("mandatory")


class _DisableRmon_Type(Integer32):
    """Custom type disableRmon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("destroyAll", 1)
    )


_DisableRmon_Type.__name__ = "Integer32"
_DisableRmon_Object = MibScalar
disableRmon = _DisableRmon_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 1, 8),
    _DisableRmon_Type()
)
disableRmon.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    disableRmon.setStatus("mandatory")


class _IsRmonActive_Type(Integer32):
    """Custom type isRmonActive based on Integer32"""
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


_IsRmonActive_Type.__name__ = "Integer32"
_IsRmonActive_Object = MibScalar
isRmonActive = _IsRmonActive_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 1, 9),
    _IsRmonActive_Type()
)
isRmonActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isRmonActive.setStatus("mandatory")
_SwitchTotalTraffic_Type = Counter32
_SwitchTotalTraffic_Object = MibScalar
switchTotalTraffic = _SwitchTotalTraffic_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 1, 10),
    _SwitchTotalTraffic_Type()
)
switchTotalTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchTotalTraffic.setStatus("mandatory")
_BufferPoolUsed_Type = Integer32
_BufferPoolUsed_Object = MibScalar
bufferPoolUsed = _BufferPoolUsed_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 1, 11),
    _BufferPoolUsed_Type()
)
bufferPoolUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferPoolUsed.setStatus("mandatory")


class _FeaturesBitFlag_Type(OctetString):
    """Custom type featuresBitFlag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_FeaturesBitFlag_Type.__name__ = "OctetString"
_FeaturesBitFlag_Object = MibScalar
featuresBitFlag = _FeaturesBitFlag_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 1, 12),
    _FeaturesBitFlag_Type()
)
featuresBitFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    featuresBitFlag.setStatus("mandatory")
_SwitchBw_Type = Integer32
_SwitchBw_Object = MibScalar
switchBw = _SwitchBw_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 1, 13),
    _SwitchBw_Type()
)
switchBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchBw.setStatus("mandatory")
_OwnMatrixAttachmentPort_Type = Integer32
_OwnMatrixAttachmentPort_Object = MibScalar
ownMatrixAttachmentPort = _OwnMatrixAttachmentPort_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 1, 14),
    _OwnMatrixAttachmentPort_Type()
)
ownMatrixAttachmentPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ownMatrixAttachmentPort.setStatus("mandatory")
_StackCrc_Type = Integer32
_StackCrc_Object = MibScalar
stackCrc = _StackCrc_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 1, 15),
    _StackCrc_Type()
)
stackCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackCrc.setStatus("mandatory")
_Ports_ObjectIdentity = ObjectIdentity
ports = _Ports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 2)
)
_PortSnmpPort_Type = Integer32
_PortSnmpPort_Object = MibScalar
portSnmpPort = _PortSnmpPort_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 2, 1),
    _PortSnmpPort_Type()
)
portSnmpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSnmpPort.setStatus("mandatory")
_PortLastChange_Type = TimeTicks
_PortLastChange_Object = MibScalar
portLastChange = _PortLastChange_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 2, 2),
    _PortLastChange_Type()
)
portLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLastChange.setStatus("mandatory")
_PortInfoTable_Object = MibTable
portInfoTable = _PortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 2, 3)
)
if mibBuilder.loadTexts:
    portInfoTable.setStatus("mandatory")
_PortInfoEntry_Object = MibTableRow
portInfoEntry = _PortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 2, 3, 1)
)
portInfoEntry.setIndexNames(
    (0, "INTEL-S500-MIB", "portInfoChassisIndex"),
    (0, "INTEL-S500-MIB", "portInfoModuleIndex"),
    (0, "INTEL-S500-MIB", "portInfoIndex"),
)
if mibBuilder.loadTexts:
    portInfoEntry.setStatus("mandatory")
_PortInfoChassisIndex_Type = Integer32
_PortInfoChassisIndex_Object = MibTableColumn
portInfoChassisIndex = _PortInfoChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 2, 3, 1, 1),
    _PortInfoChassisIndex_Type()
)
portInfoChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoChassisIndex.setStatus("mandatory")
_PortInfoModuleIndex_Type = Integer32
_PortInfoModuleIndex_Object = MibTableColumn
portInfoModuleIndex = _PortInfoModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 2, 3, 1, 2),
    _PortInfoModuleIndex_Type()
)
portInfoModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoModuleIndex.setStatus("mandatory")
_PortInfoIndex_Type = Integer32
_PortInfoIndex_Object = MibTableColumn
portInfoIndex = _PortInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 2, 3, 1, 3),
    _PortInfoIndex_Type()
)
portInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoIndex.setStatus("mandatory")


class _PortInfoType_Type(Integer32):
    """Custom type portInfoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("core", 3),
          ("gigabaselx", 11),
          ("gigabasesx", 10),
          ("hundredbasefx", 2),
          ("hundredbasetx", 1),
          ("internal", 4),
          ("layer3link", 5))
    )


_PortInfoType_Type.__name__ = "Integer32"
_PortInfoType_Object = MibTableColumn
portInfoType = _PortInfoType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 2, 3, 1, 4),
    _PortInfoType_Type()
)
portInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoType.setStatus("mandatory")
_PortConfTable_Object = MibTable
portConfTable = _PortConfTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 2, 4)
)
if mibBuilder.loadTexts:
    portConfTable.setStatus("mandatory")
_PortConfEntry_Object = MibTableRow
portConfEntry = _PortConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 2, 4, 1)
)
portConfEntry.setIndexNames(
    (0, "INTEL-S500-MIB", "portConfChassisIndex"),
    (0, "INTEL-S500-MIB", "portConfModuleIndex"),
    (0, "INTEL-S500-MIB", "portConfIndex"),
)
if mibBuilder.loadTexts:
    portConfEntry.setStatus("mandatory")
_PortConfChassisIndex_Type = Integer32
_PortConfChassisIndex_Object = MibTableColumn
portConfChassisIndex = _PortConfChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 2, 4, 1, 1),
    _PortConfChassisIndex_Type()
)
portConfChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portConfChassisIndex.setStatus("mandatory")
_PortConfModuleIndex_Type = Integer32
_PortConfModuleIndex_Object = MibTableColumn
portConfModuleIndex = _PortConfModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 2, 4, 1, 2),
    _PortConfModuleIndex_Type()
)
portConfModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portConfModuleIndex.setStatus("mandatory")
_PortConfIndex_Type = Integer32
_PortConfIndex_Object = MibTableColumn
portConfIndex = _PortConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 2, 4, 1, 3),
    _PortConfIndex_Type()
)
portConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portConfIndex.setStatus("mandatory")


class _PortConfDescr_Type(DisplayString):
    """Custom type portConfDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PortConfDescr_Type.__name__ = "DisplayString"
_PortConfDescr_Object = MibTableColumn
portConfDescr = _PortConfDescr_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 2, 4, 1, 4),
    _PortConfDescr_Type()
)
portConfDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfDescr.setStatus("mandatory")


class _PortConfLocation_Type(DisplayString):
    """Custom type portConfLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_PortConfLocation_Type.__name__ = "DisplayString"
_PortConfLocation_Object = MibTableColumn
portConfLocation = _PortConfLocation_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 2, 4, 1, 5),
    _PortConfLocation_Type()
)
portConfLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfLocation.setStatus("mandatory")


class _PortConfConfigSwitchMode_Type(Integer32):
    """Custom type portConfConfigSwitchMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              99)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 5),
          ("cutThrough", 2),
          ("default", 1),
          ("fragmentFree", 3),
          ("notAvailable", 99),
          ("storeAndForward", 4))
    )


_PortConfConfigSwitchMode_Type.__name__ = "Integer32"
_PortConfConfigSwitchMode_Object = MibTableColumn
portConfConfigSwitchMode = _PortConfConfigSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 2, 4, 1, 6),
    _PortConfConfigSwitchMode_Type()
)
portConfConfigSwitchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfConfigSwitchMode.setStatus("mandatory")


class _PortConfFlowControl_Type(Integer32):
    """Custom type portConfFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("disable", 3),
          ("enable", 2),
          ("notAvailable", 99))
    )


_PortConfFlowControl_Type.__name__ = "Integer32"
_PortConfFlowControl_Object = MibTableColumn
portConfFlowControl = _PortConfFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 2, 4, 1, 7),
    _PortConfFlowControl_Type()
)
portConfFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfFlowControl.setStatus("mandatory")


class _PortConfSpeedSupported_Type(Integer32):
    """Custom type portConfSpeedSupported based on Integer32"""
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 99),
          ("speed100Mbit", 2),
          ("speed10And100AndAutoMbit", 4),
          ("speed10And100Mbit", 3),
          ("speed10Mbit", 1),
          ("speed155Mbit", 5),
          ("speed1AndAutoGbit", 7),
          ("speed1Gbit", 6))
    )


_PortConfSpeedSupported_Type.__name__ = "Integer32"
_PortConfSpeedSupported_Object = MibTableColumn
portConfSpeedSupported = _PortConfSpeedSupported_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 2, 4, 1, 8),
    _PortConfSpeedSupported_Type()
)
portConfSpeedSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portConfSpeedSupported.setStatus("mandatory")


class _PortConfDuplexSupported_Type(Integer32):
    """Custom type portConfDuplexSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7,
              99)
        )
    )
    namedValues = NamedValues(
        *(("auto", 4),
          ("autoAndFull", 6),
          ("autoAndHalfAndFull", 7),
          ("full", 2),
          ("half", 1),
          ("halfAndFull", 3),
          ("notAvailable", 99))
    )


_PortConfDuplexSupported_Type.__name__ = "Integer32"
_PortConfDuplexSupported_Object = MibTableColumn
portConfDuplexSupported = _PortConfDuplexSupported_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 2, 4, 1, 9),
    _PortConfDuplexSupported_Type()
)
portConfDuplexSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portConfDuplexSupported.setStatus("mandatory")


class _PortConfConfigSpeed_Type(Integer32):
    """Custom type portConfConfigSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("speed100Mbit", 2),
          ("speed10Mbit", 1),
          ("speed1Gbit", 3))
    )


_PortConfConfigSpeed_Type.__name__ = "Integer32"
_PortConfConfigSpeed_Object = MibTableColumn
portConfConfigSpeed = _PortConfConfigSpeed_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 2, 4, 1, 10),
    _PortConfConfigSpeed_Type()
)
portConfConfigSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfConfigSpeed.setStatus("mandatory")


class _PortConfConfigDuplex_Type(Integer32):
    """Custom type portConfConfigDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("half", 1))
    )


_PortConfConfigDuplex_Type.__name__ = "Integer32"
_PortConfConfigDuplex_Object = MibTableColumn
portConfConfigDuplex = _PortConfConfigDuplex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 2, 4, 1, 11),
    _PortConfConfigDuplex_Type()
)
portConfConfigDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfConfigDuplex.setStatus("mandatory")


class _PortConfConfigAutoNeg_Type(Integer32):
    """Custom type portConfConfigAutoNeg based on Integer32"""
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


_PortConfConfigAutoNeg_Type.__name__ = "Integer32"
_PortConfConfigAutoNeg_Object = MibTableColumn
portConfConfigAutoNeg = _PortConfConfigAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 2, 4, 1, 12),
    _PortConfConfigAutoNeg_Type()
)
portConfConfigAutoNeg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfConfigAutoNeg.setStatus("mandatory")


class _PortConfSpeed_Type(Integer32):
    """Custom type portConfSpeed based on Integer32"""
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 99),
          ("speed100Mbit", 3),
          ("speed10Mbit", 1),
          ("speed155Mbit", 7),
          ("speed1Gbit", 5),
          ("speedAutoDetect100Mbit", 4),
          ("speedAutoDetect10Mbit", 2),
          ("speedAutoDetect1Gbit", 6))
    )


_PortConfSpeed_Type.__name__ = "Integer32"
_PortConfSpeed_Object = MibTableColumn
portConfSpeed = _PortConfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 2, 4, 1, 13),
    _PortConfSpeed_Type()
)
portConfSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portConfSpeed.setStatus("mandatory")


class _PortConfDuplex_Type(Integer32):
    """Custom type portConfDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              99)
        )
    )
    namedValues = NamedValues(
        *(("autoDetectFull", 4),
          ("autoDetectHalf", 2),
          ("full", 3),
          ("half", 1),
          ("notAvailable", 99))
    )


_PortConfDuplex_Type.__name__ = "Integer32"
_PortConfDuplex_Object = MibTableColumn
portConfDuplex = _PortConfDuplex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 2, 4, 1, 14),
    _PortConfDuplex_Type()
)
portConfDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portConfDuplex.setStatus("mandatory")


class _PortConfAutoNeg_Type(Integer32):
    """Custom type portConfAutoNeg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("failed", 3),
          ("manual", 1),
          ("notAvailable", 99))
    )


_PortConfAutoNeg_Type.__name__ = "Integer32"
_PortConfAutoNeg_Object = MibTableColumn
portConfAutoNeg = _PortConfAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 2, 4, 1, 15),
    _PortConfAutoNeg_Type()
)
portConfAutoNeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portConfAutoNeg.setStatus("mandatory")


class _PortConfSwitchMode_Type(Integer32):
    """Custom type portConfSwitchMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              99)
        )
    )
    namedValues = NamedValues(
        *(("adaptiveCutThrough", 2),
          ("adaptiveFragmentFree", 4),
          ("adaptiveStoreAndForward", 6),
          ("cutThrough", 1),
          ("fragmentFree", 3),
          ("notAvailable", 99),
          ("storeAndForward", 5))
    )


_PortConfSwitchMode_Type.__name__ = "Integer32"
_PortConfSwitchMode_Object = MibTableColumn
portConfSwitchMode = _PortConfSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 2, 4, 1, 16),
    _PortConfSwitchMode_Type()
)
portConfSwitchMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portConfSwitchMode.setStatus("mandatory")


class _PortConfTrunkSupported_Type(Integer32):
    """Custom type portConfTrunkSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              99)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 99),
          ("trunkMaster", 3),
          ("trunkSlave", 4),
          ("trunkWidthFour", 2),
          ("trunkWidthTwo", 1))
    )


_PortConfTrunkSupported_Type.__name__ = "Integer32"
_PortConfTrunkSupported_Object = MibTableColumn
portConfTrunkSupported = _PortConfTrunkSupported_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 2, 4, 1, 17),
    _PortConfTrunkSupported_Type()
)
portConfTrunkSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portConfTrunkSupported.setStatus("mandatory")


class _PortConfTrunkConfig_Type(Integer32):
    """Custom type portConfTrunkConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("disable", 99),
          ("trunkWidthFour", 2),
          ("trunkWidthTwo", 1))
    )


_PortConfTrunkConfig_Type.__name__ = "Integer32"
_PortConfTrunkConfig_Object = MibTableColumn
portConfTrunkConfig = _PortConfTrunkConfig_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 2, 4, 1, 18),
    _PortConfTrunkConfig_Type()
)
portConfTrunkConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfTrunkConfig.setStatus("mandatory")


class _PortConfTrunkName_Type(DisplayString):
    """Custom type portConfTrunkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_PortConfTrunkName_Type.__name__ = "DisplayString"
_PortConfTrunkName_Object = MibTableColumn
portConfTrunkName = _PortConfTrunkName_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 2, 4, 1, 19),
    _PortConfTrunkName_Type()
)
portConfTrunkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfTrunkName.setStatus("mandatory")


class _PortConfMirrorSupported_Type(Integer32):
    """Custom type portConfMirrorSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("mirrorDestinationOnly", 2),
          ("mirrorSourceOnly", 1),
          ("mirrorSourceOrDestination", 3),
          ("notAvailable", 99))
    )


_PortConfMirrorSupported_Type.__name__ = "Integer32"
_PortConfMirrorSupported_Object = MibTableColumn
portConfMirrorSupported = _PortConfMirrorSupported_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 2, 4, 1, 20),
    _PortConfMirrorSupported_Type()
)
portConfMirrorSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portConfMirrorSupported.setStatus("mandatory")


class _PortConfMirrorConfig_Type(Integer32):
    """Custom type portConfMirrorConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 99),
          ("mirrorDestination", 2),
          ("mirrorSource", 1))
    )


_PortConfMirrorConfig_Type.__name__ = "Integer32"
_PortConfMirrorConfig_Object = MibTableColumn
portConfMirrorConfig = _PortConfMirrorConfig_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 2, 4, 1, 21),
    _PortConfMirrorConfig_Type()
)
portConfMirrorConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfMirrorConfig.setStatus("mandatory")


class _PortConfVlanSupported_Type(Integer32):
    """Custom type portConfVlanSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              99)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("notAvailable", 99))
    )


_PortConfVlanSupported_Type.__name__ = "Integer32"
_PortConfVlanSupported_Object = MibTableColumn
portConfVlanSupported = _PortConfVlanSupported_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 2, 4, 1, 22),
    _PortConfVlanSupported_Type()
)
portConfVlanSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portConfVlanSupported.setStatus("mandatory")


class _PortAllSpanningTreeMode_Type(Integer32):
    """Custom type portAllSpanningTreeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allDisabled", 2),
          ("allEnabled", 1),
          ("mixed", 3))
    )


_PortAllSpanningTreeMode_Type.__name__ = "Integer32"
_PortAllSpanningTreeMode_Object = MibScalar
portAllSpanningTreeMode = _PortAllSpanningTreeMode_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 2, 5),
    _PortAllSpanningTreeMode_Type()
)
portAllSpanningTreeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAllSpanningTreeMode.setStatus("mandatory")
_Statistic_ObjectIdentity = ObjectIdentity
statistic = _Statistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3)
)
_TxStatTable_Object = MibTable
txStatTable = _TxStatTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 1)
)
if mibBuilder.loadTexts:
    txStatTable.setStatus("mandatory")
_TxStatEntry_Object = MibTableRow
txStatEntry = _TxStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 1, 1)
)
txStatEntry.setIndexNames(
    (0, "INTEL-S500-MIB", "txStatIndex"),
)
if mibBuilder.loadTexts:
    txStatEntry.setStatus("mandatory")
_TxStatIndex_Type = Integer32
_TxStatIndex_Object = MibTableColumn
txStatIndex = _TxStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 1, 1, 1),
    _TxStatIndex_Type()
)
txStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txStatIndex.setStatus("mandatory")
_TxUCPkts64Octets_Type = Counter32
_TxUCPkts64Octets_Object = MibTableColumn
txUCPkts64Octets = _TxUCPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 1, 1, 2),
    _TxUCPkts64Octets_Type()
)
txUCPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txUCPkts64Octets.setStatus("mandatory")
_TxUCPkts65To127Octets_Type = Counter32
_TxUCPkts65To127Octets_Object = MibTableColumn
txUCPkts65To127Octets = _TxUCPkts65To127Octets_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 1, 1, 3),
    _TxUCPkts65To127Octets_Type()
)
txUCPkts65To127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txUCPkts65To127Octets.setStatus("mandatory")
_TxUCPkts128To255Octets_Type = Counter32
_TxUCPkts128To255Octets_Object = MibTableColumn
txUCPkts128To255Octets = _TxUCPkts128To255Octets_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 1, 1, 4),
    _TxUCPkts128To255Octets_Type()
)
txUCPkts128To255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txUCPkts128To255Octets.setStatus("mandatory")
_TxUCPkts256To511Octets_Type = Counter32
_TxUCPkts256To511Octets_Object = MibTableColumn
txUCPkts256To511Octets = _TxUCPkts256To511Octets_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 1, 1, 5),
    _TxUCPkts256To511Octets_Type()
)
txUCPkts256To511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txUCPkts256To511Octets.setStatus("mandatory")
_TxUCPkts512To1023Octets_Type = Counter32
_TxUCPkts512To1023Octets_Object = MibTableColumn
txUCPkts512To1023Octets = _TxUCPkts512To1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 1, 1, 6),
    _TxUCPkts512To1023Octets_Type()
)
txUCPkts512To1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txUCPkts512To1023Octets.setStatus("mandatory")
_TxUCPkts1024To1518Octets_Type = Counter32
_TxUCPkts1024To1518Octets_Object = MibTableColumn
txUCPkts1024To1518Octets = _TxUCPkts1024To1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 1, 1, 7),
    _TxUCPkts1024To1518Octets_Type()
)
txUCPkts1024To1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txUCPkts1024To1518Octets.setStatus("mandatory")
_TxMCPkts64Octets_Type = Counter32
_TxMCPkts64Octets_Object = MibTableColumn
txMCPkts64Octets = _TxMCPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 1, 1, 8),
    _TxMCPkts64Octets_Type()
)
txMCPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txMCPkts64Octets.setStatus("mandatory")
_TxMCPkts65To127Octets_Type = Counter32
_TxMCPkts65To127Octets_Object = MibTableColumn
txMCPkts65To127Octets = _TxMCPkts65To127Octets_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 1, 1, 9),
    _TxMCPkts65To127Octets_Type()
)
txMCPkts65To127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txMCPkts65To127Octets.setStatus("mandatory")
_TxMCPkts128To255Octets_Type = Counter32
_TxMCPkts128To255Octets_Object = MibTableColumn
txMCPkts128To255Octets = _TxMCPkts128To255Octets_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 1, 1, 10),
    _TxMCPkts128To255Octets_Type()
)
txMCPkts128To255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txMCPkts128To255Octets.setStatus("mandatory")
_TxMCPkts256To511Octets_Type = Counter32
_TxMCPkts256To511Octets_Object = MibTableColumn
txMCPkts256To511Octets = _TxMCPkts256To511Octets_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 1, 1, 11),
    _TxMCPkts256To511Octets_Type()
)
txMCPkts256To511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txMCPkts256To511Octets.setStatus("mandatory")
_TxMCPkts512To1023Octets_Type = Counter32
_TxMCPkts512To1023Octets_Object = MibTableColumn
txMCPkts512To1023Octets = _TxMCPkts512To1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 1, 1, 12),
    _TxMCPkts512To1023Octets_Type()
)
txMCPkts512To1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txMCPkts512To1023Octets.setStatus("mandatory")
_TxMCPkts1024To1518Octets_Type = Counter32
_TxMCPkts1024To1518Octets_Object = MibTableColumn
txMCPkts1024To1518Octets = _TxMCPkts1024To1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 1, 1, 13),
    _TxMCPkts1024To1518Octets_Type()
)
txMCPkts1024To1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txMCPkts1024To1518Octets.setStatus("mandatory")
_TxBCPkts64Octets_Type = Counter32
_TxBCPkts64Octets_Object = MibTableColumn
txBCPkts64Octets = _TxBCPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 1, 1, 14),
    _TxBCPkts64Octets_Type()
)
txBCPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txBCPkts64Octets.setStatus("mandatory")
_TxBCPkts65To127Octets_Type = Counter32
_TxBCPkts65To127Octets_Object = MibTableColumn
txBCPkts65To127Octets = _TxBCPkts65To127Octets_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 1, 1, 15),
    _TxBCPkts65To127Octets_Type()
)
txBCPkts65To127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txBCPkts65To127Octets.setStatus("mandatory")
_TxBCPkts128To255Octets_Type = Counter32
_TxBCPkts128To255Octets_Object = MibTableColumn
txBCPkts128To255Octets = _TxBCPkts128To255Octets_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 1, 1, 16),
    _TxBCPkts128To255Octets_Type()
)
txBCPkts128To255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txBCPkts128To255Octets.setStatus("mandatory")
_TxBCPkts256To511Octets_Type = Counter32
_TxBCPkts256To511Octets_Object = MibTableColumn
txBCPkts256To511Octets = _TxBCPkts256To511Octets_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 1, 1, 17),
    _TxBCPkts256To511Octets_Type()
)
txBCPkts256To511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txBCPkts256To511Octets.setStatus("mandatory")
_TxBCPkts512To1023Octets_Type = Counter32
_TxBCPkts512To1023Octets_Object = MibTableColumn
txBCPkts512To1023Octets = _TxBCPkts512To1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 1, 1, 18),
    _TxBCPkts512To1023Octets_Type()
)
txBCPkts512To1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txBCPkts512To1023Octets.setStatus("mandatory")
_TxBCPkts1024To1518Octets_Type = Counter32
_TxBCPkts1024To1518Octets_Object = MibTableColumn
txBCPkts1024To1518Octets = _TxBCPkts1024To1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 1, 1, 19),
    _TxBCPkts1024To1518Octets_Type()
)
txBCPkts1024To1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txBCPkts1024To1518Octets.setStatus("mandatory")
_TxOctetsIllegalAddrType_Type = Counter32
_TxOctetsIllegalAddrType_Object = MibTableColumn
txOctetsIllegalAddrType = _TxOctetsIllegalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 1, 1, 20),
    _TxOctetsIllegalAddrType_Type()
)
txOctetsIllegalAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txOctetsIllegalAddrType.setStatus("mandatory")
_Tx1ArbitFrameDelay_Type = Counter32
_Tx1ArbitFrameDelay_Object = MibTableColumn
tx1ArbitFrameDelay = _Tx1ArbitFrameDelay_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 1, 1, 21),
    _Tx1ArbitFrameDelay_Type()
)
tx1ArbitFrameDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx1ArbitFrameDelay.setStatus("mandatory")
_Tx2ArbitFrameDelay_Type = Counter32
_Tx2ArbitFrameDelay_Object = MibTableColumn
tx2ArbitFrameDelay = _Tx2ArbitFrameDelay_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 1, 1, 22),
    _Tx2ArbitFrameDelay_Type()
)
tx2ArbitFrameDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx2ArbitFrameDelay.setStatus("mandatory")
_Tx3ArbitFrameDelay_Type = Counter32
_Tx3ArbitFrameDelay_Object = MibTableColumn
tx3ArbitFrameDelay = _Tx3ArbitFrameDelay_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 1, 1, 23),
    _Tx3ArbitFrameDelay_Type()
)
tx3ArbitFrameDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx3ArbitFrameDelay.setStatus("mandatory")
_Tx4ArbitFrameDelay_Type = Counter32
_Tx4ArbitFrameDelay_Object = MibTableColumn
tx4ArbitFrameDelay = _Tx4ArbitFrameDelay_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 1, 1, 24),
    _Tx4ArbitFrameDelay_Type()
)
tx4ArbitFrameDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx4ArbitFrameDelay.setStatus("mandatory")
_Tx5ArbitFrameDelay_Type = Counter32
_Tx5ArbitFrameDelay_Object = MibTableColumn
tx5ArbitFrameDelay = _Tx5ArbitFrameDelay_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 1, 1, 25),
    _Tx5ArbitFrameDelay_Type()
)
tx5ArbitFrameDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx5ArbitFrameDelay.setStatus("mandatory")
_Tx6ArbitFrameDelay_Type = Counter32
_Tx6ArbitFrameDelay_Object = MibTableColumn
tx6ArbitFrameDelay = _Tx6ArbitFrameDelay_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 1, 1, 26),
    _Tx6ArbitFrameDelay_Type()
)
tx6ArbitFrameDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx6ArbitFrameDelay.setStatus("mandatory")
_Tx7ArbitFrameDelay_Type = Counter32
_Tx7ArbitFrameDelay_Object = MibTableColumn
tx7ArbitFrameDelay = _Tx7ArbitFrameDelay_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 1, 1, 27),
    _Tx7ArbitFrameDelay_Type()
)
tx7ArbitFrameDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx7ArbitFrameDelay.setStatus("mandatory")
_TxDeferreds_Type = Counter32
_TxDeferreds_Object = MibTableColumn
txDeferreds = _TxDeferreds_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 1, 1, 28),
    _TxDeferreds_Type()
)
txDeferreds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txDeferreds.setStatus("mandatory")
_TxOctetsHis_Type = Counter32
_TxOctetsHis_Object = MibTableColumn
txOctetsHis = _TxOctetsHis_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 1, 1, 29),
    _TxOctetsHis_Type()
)
txOctetsHis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txOctetsHis.setStatus("mandatory")
_TxOctetsLos_Type = Counter32
_TxOctetsLos_Object = MibTableColumn
txOctetsLos = _TxOctetsLos_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 1, 1, 30),
    _TxOctetsLos_Type()
)
txOctetsLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txOctetsLos.setStatus("mandatory")
_TxOctetsOutOfRange_Type = Counter32
_TxOctetsOutOfRange_Object = MibTableColumn
txOctetsOutOfRange = _TxOctetsOutOfRange_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 1, 1, 31),
    _TxOctetsOutOfRange_Type()
)
txOctetsOutOfRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txOctetsOutOfRange.setStatus("mandatory")
_TxExcessiveDeferralsErrors_Type = Counter32
_TxExcessiveDeferralsErrors_Object = MibTableColumn
txExcessiveDeferralsErrors = _TxExcessiveDeferralsErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 1, 1, 32),
    _TxExcessiveDeferralsErrors_Type()
)
txExcessiveDeferralsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txExcessiveDeferralsErrors.setStatus("mandatory")
_TxNiaUnderRunAborts_Type = Counter32
_TxNiaUnderRunAborts_Object = MibTableColumn
txNiaUnderRunAborts = _TxNiaUnderRunAborts_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 1, 1, 34),
    _TxNiaUnderRunAborts_Type()
)
txNiaUnderRunAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txNiaUnderRunAborts.setStatus("mandatory")
_TxExcessiveLengthDrops_Type = Counter32
_TxExcessiveLengthDrops_Object = MibTableColumn
txExcessiveLengthDrops = _TxExcessiveLengthDrops_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 1, 1, 35),
    _TxExcessiveLengthDrops_Type()
)
txExcessiveLengthDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txExcessiveLengthDrops.setStatus("mandatory")
_TxLinkDownEvents_Type = Counter32
_TxLinkDownEvents_Object = MibTableColumn
txLinkDownEvents = _TxLinkDownEvents_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 1, 1, 36),
    _TxLinkDownEvents_Type()
)
txLinkDownEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txLinkDownEvents.setStatus("mandatory")


class _TxAllCounterPackets_Type(OctetString):
    """Custom type txAllCounterPackets based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(127, 127),
    )


_TxAllCounterPackets_Type.__name__ = "OctetString"
_TxAllCounterPackets_Object = MibTableColumn
txAllCounterPackets = _TxAllCounterPackets_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 1, 1, 37),
    _TxAllCounterPackets_Type()
)
txAllCounterPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txAllCounterPackets.setStatus("mandatory")


class _TxAllCounterOthers_Type(OctetString):
    """Custom type txAllCounterOthers based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(127, 127),
    )


_TxAllCounterOthers_Type.__name__ = "OctetString"
_TxAllCounterOthers_Object = MibTableColumn
txAllCounterOthers = _TxAllCounterOthers_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 1, 1, 38),
    _TxAllCounterOthers_Type()
)
txAllCounterOthers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txAllCounterOthers.setStatus("mandatory")
_RxStatTable_Object = MibTable
rxStatTable = _RxStatTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2)
)
if mibBuilder.loadTexts:
    rxStatTable.setStatus("mandatory")
_RxStatEntry_Object = MibTableRow
rxStatEntry = _RxStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1)
)
rxStatEntry.setIndexNames(
    (0, "INTEL-S500-MIB", "rxStatIndex"),
)
if mibBuilder.loadTexts:
    rxStatEntry.setStatus("mandatory")
_RxStatIndex_Type = Integer32
_RxStatIndex_Object = MibTableColumn
rxStatIndex = _RxStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 1),
    _RxStatIndex_Type()
)
rxStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxStatIndex.setStatus("mandatory")
_RxUCPkts64OctetsLocals_Type = Counter32
_RxUCPkts64OctetsLocals_Object = MibTableColumn
rxUCPkts64OctetsLocals = _RxUCPkts64OctetsLocals_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 2),
    _RxUCPkts64OctetsLocals_Type()
)
rxUCPkts64OctetsLocals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxUCPkts64OctetsLocals.setStatus("mandatory")
_RxUCPkts64OctetsForwardeds_Type = Counter32
_RxUCPkts64OctetsForwardeds_Object = MibTableColumn
rxUCPkts64OctetsForwardeds = _RxUCPkts64OctetsForwardeds_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 3),
    _RxUCPkts64OctetsForwardeds_Type()
)
rxUCPkts64OctetsForwardeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxUCPkts64OctetsForwardeds.setStatus("mandatory")
_RxUCPkts65To127OctetsLocals_Type = Counter32
_RxUCPkts65To127OctetsLocals_Object = MibTableColumn
rxUCPkts65To127OctetsLocals = _RxUCPkts65To127OctetsLocals_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 4),
    _RxUCPkts65To127OctetsLocals_Type()
)
rxUCPkts65To127OctetsLocals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxUCPkts65To127OctetsLocals.setStatus("mandatory")
_RxUCPkts65To127OctetsForwardeds_Type = Counter32
_RxUCPkts65To127OctetsForwardeds_Object = MibTableColumn
rxUCPkts65To127OctetsForwardeds = _RxUCPkts65To127OctetsForwardeds_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 5),
    _RxUCPkts65To127OctetsForwardeds_Type()
)
rxUCPkts65To127OctetsForwardeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxUCPkts65To127OctetsForwardeds.setStatus("mandatory")
_RxUCPkts128To255OctetsLocals_Type = Counter32
_RxUCPkts128To255OctetsLocals_Object = MibTableColumn
rxUCPkts128To255OctetsLocals = _RxUCPkts128To255OctetsLocals_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 6),
    _RxUCPkts128To255OctetsLocals_Type()
)
rxUCPkts128To255OctetsLocals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxUCPkts128To255OctetsLocals.setStatus("mandatory")
_RxUCPkts128To255OctetsForwardeds_Type = Counter32
_RxUCPkts128To255OctetsForwardeds_Object = MibTableColumn
rxUCPkts128To255OctetsForwardeds = _RxUCPkts128To255OctetsForwardeds_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 7),
    _RxUCPkts128To255OctetsForwardeds_Type()
)
rxUCPkts128To255OctetsForwardeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxUCPkts128To255OctetsForwardeds.setStatus("mandatory")
_RxUCPkts256To511OctetsLocals_Type = Counter32
_RxUCPkts256To511OctetsLocals_Object = MibTableColumn
rxUCPkts256To511OctetsLocals = _RxUCPkts256To511OctetsLocals_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 8),
    _RxUCPkts256To511OctetsLocals_Type()
)
rxUCPkts256To511OctetsLocals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxUCPkts256To511OctetsLocals.setStatus("mandatory")
_RxUCPkts256To511OctetsForwardeds_Type = Counter32
_RxUCPkts256To511OctetsForwardeds_Object = MibTableColumn
rxUCPkts256To511OctetsForwardeds = _RxUCPkts256To511OctetsForwardeds_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 9),
    _RxUCPkts256To511OctetsForwardeds_Type()
)
rxUCPkts256To511OctetsForwardeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxUCPkts256To511OctetsForwardeds.setStatus("mandatory")
_RxUCPkts512To1023OctetsLocals_Type = Counter32
_RxUCPkts512To1023OctetsLocals_Object = MibTableColumn
rxUCPkts512To1023OctetsLocals = _RxUCPkts512To1023OctetsLocals_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 10),
    _RxUCPkts512To1023OctetsLocals_Type()
)
rxUCPkts512To1023OctetsLocals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxUCPkts512To1023OctetsLocals.setStatus("mandatory")
_RxUCPkts512To1023OctetsForwardeds_Type = Counter32
_RxUCPkts512To1023OctetsForwardeds_Object = MibTableColumn
rxUCPkts512To1023OctetsForwardeds = _RxUCPkts512To1023OctetsForwardeds_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 11),
    _RxUCPkts512To1023OctetsForwardeds_Type()
)
rxUCPkts512To1023OctetsForwardeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxUCPkts512To1023OctetsForwardeds.setStatus("mandatory")
_RxUCPkts1024To1518OctetsLocals_Type = Counter32
_RxUCPkts1024To1518OctetsLocals_Object = MibTableColumn
rxUCPkts1024To1518OctetsLocals = _RxUCPkts1024To1518OctetsLocals_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 12),
    _RxUCPkts1024To1518OctetsLocals_Type()
)
rxUCPkts1024To1518OctetsLocals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxUCPkts1024To1518OctetsLocals.setStatus("mandatory")
_RxUCPkts1024To1518OctetsForwardeds_Type = Counter32
_RxUCPkts1024To1518OctetsForwardeds_Object = MibTableColumn
rxUCPkts1024To1518OctetsForwardeds = _RxUCPkts1024To1518OctetsForwardeds_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 13),
    _RxUCPkts1024To1518OctetsForwardeds_Type()
)
rxUCPkts1024To1518OctetsForwardeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxUCPkts1024To1518OctetsForwardeds.setStatus("mandatory")
_RxShortErrors_Type = Counter32
_RxShortErrors_Object = MibTableColumn
rxShortErrors = _RxShortErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 14),
    _RxShortErrors_Type()
)
rxShortErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxShortErrors.setStatus("mandatory")
_RxRuntErrors_Type = Counter32
_RxRuntErrors_Object = MibTableColumn
rxRuntErrors = _RxRuntErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 15),
    _RxRuntErrors_Type()
)
rxRuntErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxRuntErrors.setStatus("mandatory")
_RxDataRateMMErrors_Type = Counter32
_RxDataRateMMErrors_Object = MibTableColumn
rxDataRateMMErrors = _RxDataRateMMErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 16),
    _RxDataRateMMErrors_Type()
)
rxDataRateMMErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxDataRateMMErrors.setStatus("mandatory")
_RxMCPkts64OctetsLocals_Type = Counter32
_RxMCPkts64OctetsLocals_Object = MibTableColumn
rxMCPkts64OctetsLocals = _RxMCPkts64OctetsLocals_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 17),
    _RxMCPkts64OctetsLocals_Type()
)
rxMCPkts64OctetsLocals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxMCPkts64OctetsLocals.setStatus("mandatory")
_RxMCPkts64OctetsForwardeds_Type = Counter32
_RxMCPkts64OctetsForwardeds_Object = MibTableColumn
rxMCPkts64OctetsForwardeds = _RxMCPkts64OctetsForwardeds_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 18),
    _RxMCPkts64OctetsForwardeds_Type()
)
rxMCPkts64OctetsForwardeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxMCPkts64OctetsForwardeds.setStatus("mandatory")
_RxMCPkts65To127OctetsLocals_Type = Counter32
_RxMCPkts65To127OctetsLocals_Object = MibTableColumn
rxMCPkts65To127OctetsLocals = _RxMCPkts65To127OctetsLocals_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 19),
    _RxMCPkts65To127OctetsLocals_Type()
)
rxMCPkts65To127OctetsLocals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxMCPkts65To127OctetsLocals.setStatus("mandatory")
_RxMCPkts65To127OctetsForwardeds_Type = Counter32
_RxMCPkts65To127OctetsForwardeds_Object = MibTableColumn
rxMCPkts65To127OctetsForwardeds = _RxMCPkts65To127OctetsForwardeds_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 20),
    _RxMCPkts65To127OctetsForwardeds_Type()
)
rxMCPkts65To127OctetsForwardeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxMCPkts65To127OctetsForwardeds.setStatus("mandatory")
_RxMCPkts128To255OctetsLocals_Type = Counter32
_RxMCPkts128To255OctetsLocals_Object = MibTableColumn
rxMCPkts128To255OctetsLocals = _RxMCPkts128To255OctetsLocals_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 21),
    _RxMCPkts128To255OctetsLocals_Type()
)
rxMCPkts128To255OctetsLocals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxMCPkts128To255OctetsLocals.setStatus("mandatory")
_RxMCPkts128To255OctetsForwardeds_Type = Counter32
_RxMCPkts128To255OctetsForwardeds_Object = MibTableColumn
rxMCPkts128To255OctetsForwardeds = _RxMCPkts128To255OctetsForwardeds_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 22),
    _RxMCPkts128To255OctetsForwardeds_Type()
)
rxMCPkts128To255OctetsForwardeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxMCPkts128To255OctetsForwardeds.setStatus("mandatory")
_RxMCPkts256To511OctetsLocals_Type = Counter32
_RxMCPkts256To511OctetsLocals_Object = MibTableColumn
rxMCPkts256To511OctetsLocals = _RxMCPkts256To511OctetsLocals_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 23),
    _RxMCPkts256To511OctetsLocals_Type()
)
rxMCPkts256To511OctetsLocals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxMCPkts256To511OctetsLocals.setStatus("mandatory")
_RxMCPkts256To511OctetsForwardeds_Type = Counter32
_RxMCPkts256To511OctetsForwardeds_Object = MibTableColumn
rxMCPkts256To511OctetsForwardeds = _RxMCPkts256To511OctetsForwardeds_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 24),
    _RxMCPkts256To511OctetsForwardeds_Type()
)
rxMCPkts256To511OctetsForwardeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxMCPkts256To511OctetsForwardeds.setStatus("mandatory")
_RxMCPkts512To1023OctetsLocals_Type = Counter32
_RxMCPkts512To1023OctetsLocals_Object = MibTableColumn
rxMCPkts512To1023OctetsLocals = _RxMCPkts512To1023OctetsLocals_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 25),
    _RxMCPkts512To1023OctetsLocals_Type()
)
rxMCPkts512To1023OctetsLocals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxMCPkts512To1023OctetsLocals.setStatus("mandatory")
_RxMCPkts512To1023OctetsForwardeds_Type = Counter32
_RxMCPkts512To1023OctetsForwardeds_Object = MibTableColumn
rxMCPkts512To1023OctetsForwardeds = _RxMCPkts512To1023OctetsForwardeds_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 26),
    _RxMCPkts512To1023OctetsForwardeds_Type()
)
rxMCPkts512To1023OctetsForwardeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxMCPkts512To1023OctetsForwardeds.setStatus("mandatory")
_RxMCPkts1024To1518OctetsLocals_Type = Counter32
_RxMCPkts1024To1518OctetsLocals_Object = MibTableColumn
rxMCPkts1024To1518OctetsLocals = _RxMCPkts1024To1518OctetsLocals_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 27),
    _RxMCPkts1024To1518OctetsLocals_Type()
)
rxMCPkts1024To1518OctetsLocals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxMCPkts1024To1518OctetsLocals.setStatus("mandatory")
_RxMCPkts1024To1518OctetsForwardeds_Type = Counter32
_RxMCPkts1024To1518OctetsForwardeds_Object = MibTableColumn
rxMCPkts1024To1518OctetsForwardeds = _RxMCPkts1024To1518OctetsForwardeds_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 28),
    _RxMCPkts1024To1518OctetsForwardeds_Type()
)
rxMCPkts1024To1518OctetsForwardeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxMCPkts1024To1518OctetsForwardeds.setStatus("mandatory")
_RxOctetsLocalHis_Type = Counter32
_RxOctetsLocalHis_Object = MibTableColumn
rxOctetsLocalHis = _RxOctetsLocalHis_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 29),
    _RxOctetsLocalHis_Type()
)
rxOctetsLocalHis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxOctetsLocalHis.setStatus("mandatory")
_RxOctetsLocalLos_Type = Counter32
_RxOctetsLocalLos_Object = MibTableColumn
rxOctetsLocalLos = _RxOctetsLocalLos_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 30),
    _RxOctetsLocalLos_Type()
)
rxOctetsLocalLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxOctetsLocalLos.setStatus("mandatory")
_RxOctetsForwardedHis_Type = Counter32
_RxOctetsForwardedHis_Object = MibTableColumn
rxOctetsForwardedHis = _RxOctetsForwardedHis_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 31),
    _RxOctetsForwardedHis_Type()
)
rxOctetsForwardedHis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxOctetsForwardedHis.setStatus("mandatory")
_RxOctetsForwardedLos_Type = Counter32
_RxOctetsForwardedLos_Object = MibTableColumn
rxOctetsForwardedLos = _RxOctetsForwardedLos_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 32),
    _RxOctetsForwardedLos_Type()
)
rxOctetsForwardedLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxOctetsForwardedLos.setStatus("mandatory")
_RxBCPkts64OctetsLocals_Type = Counter32
_RxBCPkts64OctetsLocals_Object = MibTableColumn
rxBCPkts64OctetsLocals = _RxBCPkts64OctetsLocals_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 33),
    _RxBCPkts64OctetsLocals_Type()
)
rxBCPkts64OctetsLocals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxBCPkts64OctetsLocals.setStatus("mandatory")
_RxBCPkts64OctetsForwardeds_Type = Counter32
_RxBCPkts64OctetsForwardeds_Object = MibTableColumn
rxBCPkts64OctetsForwardeds = _RxBCPkts64OctetsForwardeds_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 34),
    _RxBCPkts64OctetsForwardeds_Type()
)
rxBCPkts64OctetsForwardeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxBCPkts64OctetsForwardeds.setStatus("mandatory")
_RxBCPkts65To127OctetsLocals_Type = Counter32
_RxBCPkts65To127OctetsLocals_Object = MibTableColumn
rxBCPkts65To127OctetsLocals = _RxBCPkts65To127OctetsLocals_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 35),
    _RxBCPkts65To127OctetsLocals_Type()
)
rxBCPkts65To127OctetsLocals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxBCPkts65To127OctetsLocals.setStatus("mandatory")
_RxBCPkts65To127OctetsForwardeds_Type = Counter32
_RxBCPkts65To127OctetsForwardeds_Object = MibTableColumn
rxBCPkts65To127OctetsForwardeds = _RxBCPkts65To127OctetsForwardeds_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 36),
    _RxBCPkts65To127OctetsForwardeds_Type()
)
rxBCPkts65To127OctetsForwardeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxBCPkts65To127OctetsForwardeds.setStatus("mandatory")
_RxBCPkts128To255OctetsLocals_Type = Counter32
_RxBCPkts128To255OctetsLocals_Object = MibTableColumn
rxBCPkts128To255OctetsLocals = _RxBCPkts128To255OctetsLocals_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 37),
    _RxBCPkts128To255OctetsLocals_Type()
)
rxBCPkts128To255OctetsLocals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxBCPkts128To255OctetsLocals.setStatus("mandatory")
_RxBCPkts128To255OctetsForwardeds_Type = Counter32
_RxBCPkts128To255OctetsForwardeds_Object = MibTableColumn
rxBCPkts128To255OctetsForwardeds = _RxBCPkts128To255OctetsForwardeds_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 38),
    _RxBCPkts128To255OctetsForwardeds_Type()
)
rxBCPkts128To255OctetsForwardeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxBCPkts128To255OctetsForwardeds.setStatus("mandatory")
_RxBCPkts256To511OctetsLocals_Type = Counter32
_RxBCPkts256To511OctetsLocals_Object = MibTableColumn
rxBCPkts256To511OctetsLocals = _RxBCPkts256To511OctetsLocals_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 39),
    _RxBCPkts256To511OctetsLocals_Type()
)
rxBCPkts256To511OctetsLocals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxBCPkts256To511OctetsLocals.setStatus("mandatory")
_RxBCPkts256To511OctetsForwardeds_Type = Counter32
_RxBCPkts256To511OctetsForwardeds_Object = MibTableColumn
rxBCPkts256To511OctetsForwardeds = _RxBCPkts256To511OctetsForwardeds_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 40),
    _RxBCPkts256To511OctetsForwardeds_Type()
)
rxBCPkts256To511OctetsForwardeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxBCPkts256To511OctetsForwardeds.setStatus("mandatory")
_RxBCPkts512To1023OctetsLocals_Type = Counter32
_RxBCPkts512To1023OctetsLocals_Object = MibTableColumn
rxBCPkts512To1023OctetsLocals = _RxBCPkts512To1023OctetsLocals_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 41),
    _RxBCPkts512To1023OctetsLocals_Type()
)
rxBCPkts512To1023OctetsLocals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxBCPkts512To1023OctetsLocals.setStatus("mandatory")
_RxBCPkts512To1023OctetsForwardeds_Type = Counter32
_RxBCPkts512To1023OctetsForwardeds_Object = MibTableColumn
rxBCPkts512To1023OctetsForwardeds = _RxBCPkts512To1023OctetsForwardeds_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 42),
    _RxBCPkts512To1023OctetsForwardeds_Type()
)
rxBCPkts512To1023OctetsForwardeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxBCPkts512To1023OctetsForwardeds.setStatus("mandatory")
_RxBCPkts1024To1518OctetsLocals_Type = Counter32
_RxBCPkts1024To1518OctetsLocals_Object = MibTableColumn
rxBCPkts1024To1518OctetsLocals = _RxBCPkts1024To1518OctetsLocals_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 43),
    _RxBCPkts1024To1518OctetsLocals_Type()
)
rxBCPkts1024To1518OctetsLocals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxBCPkts1024To1518OctetsLocals.setStatus("mandatory")
_RxBCPkts1024To1518OctetsForwardeds_Type = Counter32
_RxBCPkts1024To1518OctetsForwardeds_Object = MibTableColumn
rxBCPkts1024To1518OctetsForwardeds = _RxBCPkts1024To1518OctetsForwardeds_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 44),
    _RxBCPkts1024To1518OctetsForwardeds_Type()
)
rxBCPkts1024To1518OctetsForwardeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxBCPkts1024To1518OctetsForwardeds.setStatus("mandatory")
_RxFilterMACUnexp2ndPortDrops_Type = Counter32
_RxFilterMACUnexp2ndPortDrops_Object = MibTableColumn
rxFilterMACUnexp2ndPortDrops = _RxFilterMACUnexp2ndPortDrops_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 45),
    _RxFilterMACUnexp2ndPortDrops_Type()
)
rxFilterMACUnexp2ndPortDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxFilterMACUnexp2ndPortDrops.setStatus("mandatory")
_RxFilterIllegalMACDrops_Type = Counter32
_RxFilterIllegalMACDrops_Object = MibTableColumn
rxFilterIllegalMACDrops = _RxFilterIllegalMACDrops_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 46),
    _RxFilterIllegalMACDrops_Type()
)
rxFilterIllegalMACDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxFilterIllegalMACDrops.setStatus("mandatory")
_RxFlowCtrlPram_Type = Counter32
_RxFlowCtrlPram_Object = MibTableColumn
rxFlowCtrlPram = _RxFlowCtrlPram_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 47),
    _RxFlowCtrlPram_Type()
)
rxFlowCtrlPram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxFlowCtrlPram.setStatus("mandatory")
_RxFlowCtrlNimbus_Type = Counter32
_RxFlowCtrlNimbus_Object = MibTableColumn
rxFlowCtrlNimbus = _RxFlowCtrlNimbus_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 48),
    _RxFlowCtrlNimbus_Type()
)
rxFlowCtrlNimbus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxFlowCtrlNimbus.setStatus("mandatory")
_RxPramOverRuns_Type = Counter32
_RxPramOverRuns_Object = MibTableColumn
rxPramOverRuns = _RxPramOverRuns_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 49),
    _RxPramOverRuns_Type()
)
rxPramOverRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxPramOverRuns.setStatus("mandatory")
_RxNimbusOverRuns_Type = Counter32
_RxNimbusOverRuns_Object = MibTableColumn
rxNimbusOverRuns = _RxNimbusOverRuns_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 50),
    _RxNimbusOverRuns_Type()
)
rxNimbusOverRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxNimbusOverRuns.setStatus("mandatory")
_RxVeryLongErrors_Type = Counter32
_RxVeryLongErrors_Object = MibTableColumn
rxVeryLongErrors = _RxVeryLongErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 51),
    _RxVeryLongErrors_Type()
)
rxVeryLongErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxVeryLongErrors.setStatus("mandatory")
_RxLongErrors_Type = Counter32
_RxLongErrors_Object = MibTableColumn
rxLongErrors = _RxLongErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 52),
    _RxLongErrors_Type()
)
rxLongErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxLongErrors.setStatus("mandatory")
_RxPauseMacControlReceived_Type = Counter32
_RxPauseMacControlReceived_Object = MibTableColumn
rxPauseMacControlReceived = _RxPauseMacControlReceived_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 53),
    _RxPauseMacControlReceived_Type()
)
rxPauseMacControlReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxPauseMacControlReceived.setStatus("mandatory")
_RxUnknownMacControlFrame_Type = Counter32
_RxUnknownMacControlFrame_Object = MibTableColumn
rxUnknownMacControlFrame = _RxUnknownMacControlFrame_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 54),
    _RxUnknownMacControlFrame_Type()
)
rxUnknownMacControlFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxUnknownMacControlFrame.setStatus("mandatory")
_RxPiaOutOfPoolDropErrors_Type = Counter32
_RxPiaOutOfPoolDropErrors_Object = MibTableColumn
rxPiaOutOfPoolDropErrors = _RxPiaOutOfPoolDropErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 55),
    _RxPiaOutOfPoolDropErrors_Type()
)
rxPiaOutOfPoolDropErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxPiaOutOfPoolDropErrors.setStatus("mandatory")
_RxCodeViolations_Type = Counter32
_RxCodeViolations_Object = MibTableColumn
rxCodeViolations = _RxCodeViolations_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 56),
    _RxCodeViolations_Type()
)
rxCodeViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxCodeViolations.setStatus("mandatory")
_RxJabberErrors_Type = Counter32
_RxJabberErrors_Object = MibTableColumn
rxJabberErrors = _RxJabberErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 57),
    _RxJabberErrors_Type()
)
rxJabberErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxJabberErrors.setStatus("mandatory")
_RxNiaOverRunDropErrors_Type = Counter32
_RxNiaOverRunDropErrors_Object = MibTableColumn
rxNiaOverRunDropErrors = _RxNiaOverRunDropErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 58),
    _RxNiaOverRunDropErrors_Type()
)
rxNiaOverRunDropErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxNiaOverRunDropErrors.setStatus("mandatory")


class _RxAllCounterPackets_Type(OctetString):
    """Custom type rxAllCounterPackets based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(164, 164),
    )


_RxAllCounterPackets_Type.__name__ = "OctetString"
_RxAllCounterPackets_Object = MibTableColumn
rxAllCounterPackets = _RxAllCounterPackets_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 59),
    _RxAllCounterPackets_Type()
)
rxAllCounterPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxAllCounterPackets.setStatus("mandatory")


class _RxAllCounterOthers_Type(OctetString):
    """Custom type rxAllCounterOthers based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(48, 48),
    )


_RxAllCounterOthers_Type.__name__ = "OctetString"
_RxAllCounterOthers_Object = MibTableColumn
rxAllCounterOthers = _RxAllCounterOthers_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 2, 1, 60),
    _RxAllCounterOthers_Type()
)
rxAllCounterOthers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxAllCounterOthers.setStatus("mandatory")
_TotalRxTxPackets_Type = OctetString
_TotalRxTxPackets_Object = MibScalar
totalRxTxPackets = _TotalRxTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 3),
    _TotalRxTxPackets_Type()
)
totalRxTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalRxTxPackets.setStatus("mandatory")
_TotalCollisions_Type = OctetString
_TotalCollisions_Object = MibScalar
totalCollisions = _TotalCollisions_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 3, 4),
    _TotalCollisions_Type()
)
totalCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalCollisions.setStatus("mandatory")
_AdaptiveForwardMode_ObjectIdentity = ObjectIdentity
adaptiveForwardMode = _AdaptiveForwardMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 4)
)
_AdaptiveForwardModeSampleTime_Type = Integer32
_AdaptiveForwardModeSampleTime_Object = MibScalar
adaptiveForwardModeSampleTime = _AdaptiveForwardModeSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 4, 1),
    _AdaptiveForwardModeSampleTime_Type()
)
adaptiveForwardModeSampleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adaptiveForwardModeSampleTime.setStatus("mandatory")
_AdaptiveForwardModeRuntsOffset_Type = Integer32
_AdaptiveForwardModeRuntsOffset_Object = MibScalar
adaptiveForwardModeRuntsOffset = _AdaptiveForwardModeRuntsOffset_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 4, 2),
    _AdaptiveForwardModeRuntsOffset_Type()
)
adaptiveForwardModeRuntsOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adaptiveForwardModeRuntsOffset.setStatus("mandatory")
_AdaptiveForwardModeRuntsRange_Type = Integer32
_AdaptiveForwardModeRuntsRange_Object = MibScalar
adaptiveForwardModeRuntsRange = _AdaptiveForwardModeRuntsRange_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 4, 3),
    _AdaptiveForwardModeRuntsRange_Type()
)
adaptiveForwardModeRuntsRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adaptiveForwardModeRuntsRange.setStatus("mandatory")
_AdaptiveForwardModeCrcsOffset_Type = Integer32
_AdaptiveForwardModeCrcsOffset_Object = MibScalar
adaptiveForwardModeCrcsOffset = _AdaptiveForwardModeCrcsOffset_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 4, 4),
    _AdaptiveForwardModeCrcsOffset_Type()
)
adaptiveForwardModeCrcsOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adaptiveForwardModeCrcsOffset.setStatus("mandatory")
_AdaptiveForwardModeCrcsRange_Type = Integer32
_AdaptiveForwardModeCrcsRange_Object = MibScalar
adaptiveForwardModeCrcsRange = _AdaptiveForwardModeCrcsRange_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 4, 5),
    _AdaptiveForwardModeCrcsRange_Type()
)
adaptiveForwardModeCrcsRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adaptiveForwardModeCrcsRange.setStatus("mandatory")
_ChipSets_ObjectIdentity = ObjectIdentity
chipSets = _ChipSets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 5)
)
_Smu_ObjectIdentity = ObjectIdentity
smu = _Smu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 6)
)
_SmuModuleTable_Object = MibTable
smuModuleTable = _SmuModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 6, 1)
)
if mibBuilder.loadTexts:
    smuModuleTable.setStatus("mandatory")
_SmuModuleEntry_Object = MibTableRow
smuModuleEntry = _SmuModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 6, 1, 1)
)
smuModuleEntry.setIndexNames(
    (0, "INTEL-S500-MIB", "smuModuleChassisIndex"),
    (0, "INTEL-S500-MIB", "smuModuleIndex"),
)
if mibBuilder.loadTexts:
    smuModuleEntry.setStatus("mandatory")
_SmuModuleChassisIndex_Type = Integer32
_SmuModuleChassisIndex_Object = MibTableColumn
smuModuleChassisIndex = _SmuModuleChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 6, 1, 1, 1),
    _SmuModuleChassisIndex_Type()
)
smuModuleChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smuModuleChassisIndex.setStatus("mandatory")
_SmuModuleIndex_Type = Integer32
_SmuModuleIndex_Object = MibTableColumn
smuModuleIndex = _SmuModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 6, 1, 1, 2),
    _SmuModuleIndex_Type()
)
smuModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smuModuleIndex.setStatus("mandatory")
_SmuModuleState_Type = Integer32
_SmuModuleState_Object = MibTableColumn
smuModuleState = _SmuModuleState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 6, 1, 1, 3),
    _SmuModuleState_Type()
)
smuModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smuModuleState.setStatus("mandatory")
_SmuPortTable_Object = MibTable
smuPortTable = _SmuPortTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 6, 2)
)
if mibBuilder.loadTexts:
    smuPortTable.setStatus("mandatory")
_SmuPortEntry_Object = MibTableRow
smuPortEntry = _SmuPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 6, 2, 1)
)
smuPortEntry.setIndexNames(
    (0, "INTEL-S500-MIB", "smuPortChassisIndex"),
    (0, "INTEL-S500-MIB", "smuPortModuleIndex"),
    (0, "INTEL-S500-MIB", "smuPortIndex"),
)
if mibBuilder.loadTexts:
    smuPortEntry.setStatus("mandatory")
_SmuPortChassisIndex_Type = Integer32
_SmuPortChassisIndex_Object = MibTableColumn
smuPortChassisIndex = _SmuPortChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 6, 2, 1, 1),
    _SmuPortChassisIndex_Type()
)
smuPortChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smuPortChassisIndex.setStatus("mandatory")
_SmuPortModuleIndex_Type = Integer32
_SmuPortModuleIndex_Object = MibTableColumn
smuPortModuleIndex = _SmuPortModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 6, 2, 1, 2),
    _SmuPortModuleIndex_Type()
)
smuPortModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smuPortModuleIndex.setStatus("mandatory")
_SmuPortIndex_Type = Integer32
_SmuPortIndex_Object = MibTableColumn
smuPortIndex = _SmuPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 6, 2, 1, 3),
    _SmuPortIndex_Type()
)
smuPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smuPortIndex.setStatus("mandatory")
_SmuPortAttachedNumber_Type = Integer32
_SmuPortAttachedNumber_Object = MibTableColumn
smuPortAttachedNumber = _SmuPortAttachedNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 6, 2, 1, 4),
    _SmuPortAttachedNumber_Type()
)
smuPortAttachedNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smuPortAttachedNumber.setStatus("mandatory")


class _SmuPortAttachedMac_Type(OctetString):
    """Custom type smuPortAttachedMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_SmuPortAttachedMac_Type.__name__ = "OctetString"
_SmuPortAttachedMac_Object = MibTableColumn
smuPortAttachedMac = _SmuPortAttachedMac_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 6, 2, 1, 5),
    _SmuPortAttachedMac_Type()
)
smuPortAttachedMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smuPortAttachedMac.setStatus("mandatory")
_SmuPortAttachedIp_Type = IpAddress
_SmuPortAttachedIp_Object = MibTableColumn
smuPortAttachedIp = _SmuPortAttachedIp_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 6, 2, 1, 6),
    _SmuPortAttachedIp_Type()
)
smuPortAttachedIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smuPortAttachedIp.setStatus("mandatory")
_PermanentEntries_ObjectIdentity = ObjectIdentity
permanentEntries = _PermanentEntries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 7)
)
_PermanentEntriesTable_Object = MibTable
permanentEntriesTable = _PermanentEntriesTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 7, 1)
)
if mibBuilder.loadTexts:
    permanentEntriesTable.setStatus("mandatory")
_PermanentEntriesEntry_Object = MibTableRow
permanentEntriesEntry = _PermanentEntriesEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 7, 1, 1)
)
permanentEntriesEntry.setIndexNames(
    (0, "INTEL-S500-MIB", "permanentEntriesMACAddr"),
)
if mibBuilder.loadTexts:
    permanentEntriesEntry.setStatus("mandatory")


class _PermanentEntriesMACAddr_Type(OctetString):
    """Custom type permanentEntriesMACAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_PermanentEntriesMACAddr_Type.__name__ = "OctetString"
_PermanentEntriesMACAddr_Object = MibTableColumn
permanentEntriesMACAddr = _PermanentEntriesMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 7, 1, 1, 1),
    _PermanentEntriesMACAddr_Type()
)
permanentEntriesMACAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    permanentEntriesMACAddr.setStatus("mandatory")
_PermanentEntriesPortId_Type = Integer32
_PermanentEntriesPortId_Object = MibTableColumn
permanentEntriesPortId = _PermanentEntriesPortId_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 7, 1, 1, 2),
    _PermanentEntriesPortId_Type()
)
permanentEntriesPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    permanentEntriesPortId.setStatus("mandatory")
_PermanentEntriesCreateObj_Type = Integer32
_PermanentEntriesCreateObj_Object = MibTableColumn
permanentEntriesCreateObj = _PermanentEntriesCreateObj_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 7, 1, 1, 3),
    _PermanentEntriesCreateObj_Type()
)
permanentEntriesCreateObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    permanentEntriesCreateObj.setStatus("mandatory")


class _PermanentEntriesDeleteObj_Type(Integer32):
    """Custom type permanentEntriesDeleteObj based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("delete", 1)
    )


_PermanentEntriesDeleteObj_Type.__name__ = "Integer32"
_PermanentEntriesDeleteObj_Object = MibTableColumn
permanentEntriesDeleteObj = _PermanentEntriesDeleteObj_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 7, 1, 1, 4),
    _PermanentEntriesDeleteObj_Type()
)
permanentEntriesDeleteObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    permanentEntriesDeleteObj.setStatus("mandatory")
_Matrix_ObjectIdentity = ObjectIdentity
matrix = _Matrix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 8)
)
_MatrixModuleTable_Object = MibTable
matrixModuleTable = _MatrixModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 8, 1)
)
if mibBuilder.loadTexts:
    matrixModuleTable.setStatus("mandatory")
_MatrixModuleEntry_Object = MibTableRow
matrixModuleEntry = _MatrixModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 8, 1, 1)
)
matrixModuleEntry.setIndexNames(
    (0, "INTEL-S500-MIB", "matrixModuleIndex"),
)
if mibBuilder.loadTexts:
    matrixModuleEntry.setStatus("mandatory")
_MatrixModuleIndex_Type = Integer32
_MatrixModuleIndex_Object = MibTableColumn
matrixModuleIndex = _MatrixModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 8, 1, 1, 1),
    _MatrixModuleIndex_Type()
)
matrixModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixModuleIndex.setStatus("mandatory")


class _MatrixModuleState_Type(Integer32):
    """Custom type matrixModuleState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              99)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("back", 4),
          ("error", 3),
          ("notAvailable", 99),
          ("standby", 2))
    )


_MatrixModuleState_Type.__name__ = "Integer32"
_MatrixModuleState_Object = MibTableColumn
matrixModuleState = _MatrixModuleState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 8, 1, 1, 2),
    _MatrixModuleState_Type()
)
matrixModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixModuleState.setStatus("mandatory")
_MatrixNumberConnected_Type = Integer32
_MatrixNumberConnected_Object = MibTableColumn
matrixNumberConnected = _MatrixNumberConnected_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 8, 1, 1, 3),
    _MatrixNumberConnected_Type()
)
matrixNumberConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixNumberConnected.setStatus("mandatory")
_MatrixMasterPort_Type = Integer32
_MatrixMasterPort_Object = MibTableColumn
matrixMasterPort = _MatrixMasterPort_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 8, 1, 1, 4),
    _MatrixMasterPort_Type()
)
matrixMasterPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixMasterPort.setStatus("mandatory")
_MatrixPortTable_Object = MibTable
matrixPortTable = _MatrixPortTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 8, 2)
)
if mibBuilder.loadTexts:
    matrixPortTable.setStatus("mandatory")
_MatrixPortEntry_Object = MibTableRow
matrixPortEntry = _MatrixPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 8, 2, 1)
)
matrixPortEntry.setIndexNames(
    (0, "INTEL-S500-MIB", "matrixModuleIndex"),
    (0, "INTEL-S500-MIB", "matrixPortIndex"),
)
if mibBuilder.loadTexts:
    matrixPortEntry.setStatus("mandatory")
_MatrixPortModuleIndex_Type = Integer32
_MatrixPortModuleIndex_Object = MibTableColumn
matrixPortModuleIndex = _MatrixPortModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 8, 2, 1, 1),
    _MatrixPortModuleIndex_Type()
)
matrixPortModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixPortModuleIndex.setStatus("mandatory")
_MatrixPortIndex_Type = Integer32
_MatrixPortIndex_Object = MibTableColumn
matrixPortIndex = _MatrixPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 8, 2, 1, 2),
    _MatrixPortIndex_Type()
)
matrixPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixPortIndex.setStatus("mandatory")
_MatrixPort_Type = Integer32
_MatrixPort_Object = MibTableColumn
matrixPort = _MatrixPort_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 8, 2, 1, 3),
    _MatrixPort_Type()
)
matrixPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixPort.setStatus("mandatory")


class _MatrixPortType_Type(Integer32):
    """Custom type matrixPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              99)
        )
    )
    namedValues = NamedValues(
        *(("atm", 6),
          ("es510", 1),
          ("es520", 2),
          ("es550F", 4),
          ("es550T", 3),
          ("gb2", 5),
          ("notAvailable", 99))
    )


_MatrixPortType_Type.__name__ = "Integer32"
_MatrixPortType_Object = MibTableColumn
matrixPortType = _MatrixPortType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 8, 2, 1, 4),
    _MatrixPortType_Type()
)
matrixPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixPortType.setStatus("mandatory")
_MatrixPortMajVer_Type = Integer32
_MatrixPortMajVer_Object = MibTableColumn
matrixPortMajVer = _MatrixPortMajVer_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 8, 2, 1, 5),
    _MatrixPortMajVer_Type()
)
matrixPortMajVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixPortMajVer.setStatus("mandatory")
_MatrixPortMinVer_Type = Integer32
_MatrixPortMinVer_Object = MibTableColumn
matrixPortMinVer = _MatrixPortMinVer_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 8, 2, 1, 6),
    _MatrixPortMinVer_Type()
)
matrixPortMinVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixPortMinVer.setStatus("mandatory")


class _MatrixPortMac_Type(OctetString):
    """Custom type matrixPortMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MatrixPortMac_Type.__name__ = "OctetString"
_MatrixPortMac_Object = MibTableColumn
matrixPortMac = _MatrixPortMac_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 8, 2, 1, 7),
    _MatrixPortMac_Type()
)
matrixPortMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixPortMac.setStatus("mandatory")
_MatrixPortIp_Type = IpAddress
_MatrixPortIp_Object = MibTableColumn
matrixPortIp = _MatrixPortIp_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 8, 2, 1, 8),
    _MatrixPortIp_Type()
)
matrixPortIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matrixPortIp.setStatus("mandatory")
_MatrixPortSubnetMask_Type = IpAddress
_MatrixPortSubnetMask_Object = MibTableColumn
matrixPortSubnetMask = _MatrixPortSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 8, 2, 1, 9),
    _MatrixPortSubnetMask_Type()
)
matrixPortSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matrixPortSubnetMask.setStatus("mandatory")
_MatrixPortGateway_Type = IpAddress
_MatrixPortGateway_Object = MibTableColumn
matrixPortGateway = _MatrixPortGateway_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 8, 2, 1, 10),
    _MatrixPortGateway_Type()
)
matrixPortGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matrixPortGateway.setStatus("mandatory")
_MatrixLastChange_Type = TimeTicks
_MatrixLastChange_Object = MibScalar
matrixLastChange = _MatrixLastChange_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 8, 3),
    _MatrixLastChange_Type()
)
matrixLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixLastChange.setStatus("mandatory")
_Mediamodules_ObjectIdentity = ObjectIdentity
mediamodules = _Mediamodules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 9)
)
_MediaModuleTable_Object = MibTable
mediaModuleTable = _MediaModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 9, 1)
)
if mibBuilder.loadTexts:
    mediaModuleTable.setStatus("mandatory")
_MediaModuleEntry_Object = MibTableRow
mediaModuleEntry = _MediaModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 9, 1, 1)
)
mediaModuleEntry.setIndexNames(
    (0, "INTEL-S500-MIB", "mediaModuleChassisIndex"),
    (0, "INTEL-S500-MIB", "mediaModuleModuleIndex"),
    (0, "INTEL-S500-MIB", "mediaModuleIndex"),
)
if mibBuilder.loadTexts:
    mediaModuleEntry.setStatus("mandatory")


class _ModuleMode_Type(Integer32):
    """Custom type moduleMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stackMode", 1),
          ("standAloneMode", 2))
    )


_ModuleMode_Type.__name__ = "Integer32"
_ModuleMode_Object = MibTableColumn
moduleMode = _ModuleMode_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 9, 1, 1, 1),
    _ModuleMode_Type()
)
moduleMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleMode.setStatus("mandatory")
_MatrixAttachmentPort_Type = Integer32
_MatrixAttachmentPort_Object = MibTableColumn
matrixAttachmentPort = _MatrixAttachmentPort_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 9, 1, 1, 2),
    _MatrixAttachmentPort_Type()
)
matrixAttachmentPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixAttachmentPort.setStatus("mandatory")
_MediaModuleChange_Type = TimeTicks
_MediaModuleChange_Object = MibScalar
mediaModuleChange = _MediaModuleChange_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 9, 2),
    _MediaModuleChange_Type()
)
mediaModuleChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaModuleChange.setStatus("mandatory")

# Managed Objects groups


# Notification objects

s500PermVioEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 0, 1)
)
s500PermVioEvent.setObjects(
      *(("INTEL-S500-MIB", "portConfChassisIndex"),
        ("INTEL-S500-MIB", "portConfModuleIndex"),
        ("INTEL-S500-MIB", "portConfIndex"))
)
if mibBuilder.loadTexts:
    s500PermVioEvent.setStatus(
        ""
    )

s500AdaptiveForwEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 0, 2)
)
s500AdaptiveForwEvent.setObjects(
      *(("INTEL-S500-MIB", "portConfChassisIndex"),
        ("INTEL-S500-MIB", "portConfModuleIndex"),
        ("INTEL-S500-MIB", "portConfIndex"),
        ("INTEL-S500-MIB", "portConfSwitchMode"),
        ("INTEL-S500-MIB", "portConfSwitchMode"))
)
if mibBuilder.loadTexts:
    s500AdaptiveForwEvent.setStatus(
        ""
    )

s500TemperatureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 0, 3)
)
s500TemperatureEvent.setObjects(
    ("INTEL-S500-MIB", "temperatureLevel")
)
if mibBuilder.loadTexts:
    s500TemperatureEvent.setStatus(
        ""
    )

s500RedundantPowerSupplyEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 6, 10, 0, 4)
)
s500RedundantPowerSupplyEvent.setObjects(
    ("INTEL-S500-MIB", "redundantPowerSupplyStatus")
)
if mibBuilder.loadTexts:
    s500RedundantPowerSupplyEvent.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTEL-S500-MIB",
    **{"s500": s500,
       "s500PermVioEvent": s500PermVioEvent,
       "s500AdaptiveForwEvent": s500AdaptiveForwEvent,
       "s500TemperatureEvent": s500TemperatureEvent,
       "s500RedundantPowerSupplyEvent": s500RedundantPowerSupplyEvent,
       "module": module,
       "defaultSwitchMode": defaultSwitchMode,
       "defaultFlowControlMode": defaultFlowControlMode,
       "smuMaster": smuMaster,
       "localManagementTimeout": localManagementTimeout,
       "temperatureLevel": temperatureLevel,
       "redundantPowerSupplyStatus": redundantPowerSupplyStatus,
       "portMirroring": portMirroring,
       "disableRmon": disableRmon,
       "isRmonActive": isRmonActive,
       "switchTotalTraffic": switchTotalTraffic,
       "bufferPoolUsed": bufferPoolUsed,
       "featuresBitFlag": featuresBitFlag,
       "switchBw": switchBw,
       "ownMatrixAttachmentPort": ownMatrixAttachmentPort,
       "stackCrc": stackCrc,
       "ports": ports,
       "portSnmpPort": portSnmpPort,
       "portLastChange": portLastChange,
       "portInfoTable": portInfoTable,
       "portInfoEntry": portInfoEntry,
       "portInfoChassisIndex": portInfoChassisIndex,
       "portInfoModuleIndex": portInfoModuleIndex,
       "portInfoIndex": portInfoIndex,
       "portInfoType": portInfoType,
       "portConfTable": portConfTable,
       "portConfEntry": portConfEntry,
       "portConfChassisIndex": portConfChassisIndex,
       "portConfModuleIndex": portConfModuleIndex,
       "portConfIndex": portConfIndex,
       "portConfDescr": portConfDescr,
       "portConfLocation": portConfLocation,
       "portConfConfigSwitchMode": portConfConfigSwitchMode,
       "portConfFlowControl": portConfFlowControl,
       "portConfSpeedSupported": portConfSpeedSupported,
       "portConfDuplexSupported": portConfDuplexSupported,
       "portConfConfigSpeed": portConfConfigSpeed,
       "portConfConfigDuplex": portConfConfigDuplex,
       "portConfConfigAutoNeg": portConfConfigAutoNeg,
       "portConfSpeed": portConfSpeed,
       "portConfDuplex": portConfDuplex,
       "portConfAutoNeg": portConfAutoNeg,
       "portConfSwitchMode": portConfSwitchMode,
       "portConfTrunkSupported": portConfTrunkSupported,
       "portConfTrunkConfig": portConfTrunkConfig,
       "portConfTrunkName": portConfTrunkName,
       "portConfMirrorSupported": portConfMirrorSupported,
       "portConfMirrorConfig": portConfMirrorConfig,
       "portConfVlanSupported": portConfVlanSupported,
       "portAllSpanningTreeMode": portAllSpanningTreeMode,
       "statistic": statistic,
       "txStatTable": txStatTable,
       "txStatEntry": txStatEntry,
       "txStatIndex": txStatIndex,
       "txUCPkts64Octets": txUCPkts64Octets,
       "txUCPkts65To127Octets": txUCPkts65To127Octets,
       "txUCPkts128To255Octets": txUCPkts128To255Octets,
       "txUCPkts256To511Octets": txUCPkts256To511Octets,
       "txUCPkts512To1023Octets": txUCPkts512To1023Octets,
       "txUCPkts1024To1518Octets": txUCPkts1024To1518Octets,
       "txMCPkts64Octets": txMCPkts64Octets,
       "txMCPkts65To127Octets": txMCPkts65To127Octets,
       "txMCPkts128To255Octets": txMCPkts128To255Octets,
       "txMCPkts256To511Octets": txMCPkts256To511Octets,
       "txMCPkts512To1023Octets": txMCPkts512To1023Octets,
       "txMCPkts1024To1518Octets": txMCPkts1024To1518Octets,
       "txBCPkts64Octets": txBCPkts64Octets,
       "txBCPkts65To127Octets": txBCPkts65To127Octets,
       "txBCPkts128To255Octets": txBCPkts128To255Octets,
       "txBCPkts256To511Octets": txBCPkts256To511Octets,
       "txBCPkts512To1023Octets": txBCPkts512To1023Octets,
       "txBCPkts1024To1518Octets": txBCPkts1024To1518Octets,
       "txOctetsIllegalAddrType": txOctetsIllegalAddrType,
       "tx1ArbitFrameDelay": tx1ArbitFrameDelay,
       "tx2ArbitFrameDelay": tx2ArbitFrameDelay,
       "tx3ArbitFrameDelay": tx3ArbitFrameDelay,
       "tx4ArbitFrameDelay": tx4ArbitFrameDelay,
       "tx5ArbitFrameDelay": tx5ArbitFrameDelay,
       "tx6ArbitFrameDelay": tx6ArbitFrameDelay,
       "tx7ArbitFrameDelay": tx7ArbitFrameDelay,
       "txDeferreds": txDeferreds,
       "txOctetsHis": txOctetsHis,
       "txOctetsLos": txOctetsLos,
       "txOctetsOutOfRange": txOctetsOutOfRange,
       "txExcessiveDeferralsErrors": txExcessiveDeferralsErrors,
       "txNiaUnderRunAborts": txNiaUnderRunAborts,
       "txExcessiveLengthDrops": txExcessiveLengthDrops,
       "txLinkDownEvents": txLinkDownEvents,
       "txAllCounterPackets": txAllCounterPackets,
       "txAllCounterOthers": txAllCounterOthers,
       "rxStatTable": rxStatTable,
       "rxStatEntry": rxStatEntry,
       "rxStatIndex": rxStatIndex,
       "rxUCPkts64OctetsLocals": rxUCPkts64OctetsLocals,
       "rxUCPkts64OctetsForwardeds": rxUCPkts64OctetsForwardeds,
       "rxUCPkts65To127OctetsLocals": rxUCPkts65To127OctetsLocals,
       "rxUCPkts65To127OctetsForwardeds": rxUCPkts65To127OctetsForwardeds,
       "rxUCPkts128To255OctetsLocals": rxUCPkts128To255OctetsLocals,
       "rxUCPkts128To255OctetsForwardeds": rxUCPkts128To255OctetsForwardeds,
       "rxUCPkts256To511OctetsLocals": rxUCPkts256To511OctetsLocals,
       "rxUCPkts256To511OctetsForwardeds": rxUCPkts256To511OctetsForwardeds,
       "rxUCPkts512To1023OctetsLocals": rxUCPkts512To1023OctetsLocals,
       "rxUCPkts512To1023OctetsForwardeds": rxUCPkts512To1023OctetsForwardeds,
       "rxUCPkts1024To1518OctetsLocals": rxUCPkts1024To1518OctetsLocals,
       "rxUCPkts1024To1518OctetsForwardeds": rxUCPkts1024To1518OctetsForwardeds,
       "rxShortErrors": rxShortErrors,
       "rxRuntErrors": rxRuntErrors,
       "rxDataRateMMErrors": rxDataRateMMErrors,
       "rxMCPkts64OctetsLocals": rxMCPkts64OctetsLocals,
       "rxMCPkts64OctetsForwardeds": rxMCPkts64OctetsForwardeds,
       "rxMCPkts65To127OctetsLocals": rxMCPkts65To127OctetsLocals,
       "rxMCPkts65To127OctetsForwardeds": rxMCPkts65To127OctetsForwardeds,
       "rxMCPkts128To255OctetsLocals": rxMCPkts128To255OctetsLocals,
       "rxMCPkts128To255OctetsForwardeds": rxMCPkts128To255OctetsForwardeds,
       "rxMCPkts256To511OctetsLocals": rxMCPkts256To511OctetsLocals,
       "rxMCPkts256To511OctetsForwardeds": rxMCPkts256To511OctetsForwardeds,
       "rxMCPkts512To1023OctetsLocals": rxMCPkts512To1023OctetsLocals,
       "rxMCPkts512To1023OctetsForwardeds": rxMCPkts512To1023OctetsForwardeds,
       "rxMCPkts1024To1518OctetsLocals": rxMCPkts1024To1518OctetsLocals,
       "rxMCPkts1024To1518OctetsForwardeds": rxMCPkts1024To1518OctetsForwardeds,
       "rxOctetsLocalHis": rxOctetsLocalHis,
       "rxOctetsLocalLos": rxOctetsLocalLos,
       "rxOctetsForwardedHis": rxOctetsForwardedHis,
       "rxOctetsForwardedLos": rxOctetsForwardedLos,
       "rxBCPkts64OctetsLocals": rxBCPkts64OctetsLocals,
       "rxBCPkts64OctetsForwardeds": rxBCPkts64OctetsForwardeds,
       "rxBCPkts65To127OctetsLocals": rxBCPkts65To127OctetsLocals,
       "rxBCPkts65To127OctetsForwardeds": rxBCPkts65To127OctetsForwardeds,
       "rxBCPkts128To255OctetsLocals": rxBCPkts128To255OctetsLocals,
       "rxBCPkts128To255OctetsForwardeds": rxBCPkts128To255OctetsForwardeds,
       "rxBCPkts256To511OctetsLocals": rxBCPkts256To511OctetsLocals,
       "rxBCPkts256To511OctetsForwardeds": rxBCPkts256To511OctetsForwardeds,
       "rxBCPkts512To1023OctetsLocals": rxBCPkts512To1023OctetsLocals,
       "rxBCPkts512To1023OctetsForwardeds": rxBCPkts512To1023OctetsForwardeds,
       "rxBCPkts1024To1518OctetsLocals": rxBCPkts1024To1518OctetsLocals,
       "rxBCPkts1024To1518OctetsForwardeds": rxBCPkts1024To1518OctetsForwardeds,
       "rxFilterMACUnexp2ndPortDrops": rxFilterMACUnexp2ndPortDrops,
       "rxFilterIllegalMACDrops": rxFilterIllegalMACDrops,
       "rxFlowCtrlPram": rxFlowCtrlPram,
       "rxFlowCtrlNimbus": rxFlowCtrlNimbus,
       "rxPramOverRuns": rxPramOverRuns,
       "rxNimbusOverRuns": rxNimbusOverRuns,
       "rxVeryLongErrors": rxVeryLongErrors,
       "rxLongErrors": rxLongErrors,
       "rxPauseMacControlReceived": rxPauseMacControlReceived,
       "rxUnknownMacControlFrame": rxUnknownMacControlFrame,
       "rxPiaOutOfPoolDropErrors": rxPiaOutOfPoolDropErrors,
       "rxCodeViolations": rxCodeViolations,
       "rxJabberErrors": rxJabberErrors,
       "rxNiaOverRunDropErrors": rxNiaOverRunDropErrors,
       "rxAllCounterPackets": rxAllCounterPackets,
       "rxAllCounterOthers": rxAllCounterOthers,
       "totalRxTxPackets": totalRxTxPackets,
       "totalCollisions": totalCollisions,
       "adaptiveForwardMode": adaptiveForwardMode,
       "adaptiveForwardModeSampleTime": adaptiveForwardModeSampleTime,
       "adaptiveForwardModeRuntsOffset": adaptiveForwardModeRuntsOffset,
       "adaptiveForwardModeRuntsRange": adaptiveForwardModeRuntsRange,
       "adaptiveForwardModeCrcsOffset": adaptiveForwardModeCrcsOffset,
       "adaptiveForwardModeCrcsRange": adaptiveForwardModeCrcsRange,
       "chipSets": chipSets,
       "smu": smu,
       "smuModuleTable": smuModuleTable,
       "smuModuleEntry": smuModuleEntry,
       "smuModuleChassisIndex": smuModuleChassisIndex,
       "smuModuleIndex": smuModuleIndex,
       "smuModuleState": smuModuleState,
       "smuPortTable": smuPortTable,
       "smuPortEntry": smuPortEntry,
       "smuPortChassisIndex": smuPortChassisIndex,
       "smuPortModuleIndex": smuPortModuleIndex,
       "smuPortIndex": smuPortIndex,
       "smuPortAttachedNumber": smuPortAttachedNumber,
       "smuPortAttachedMac": smuPortAttachedMac,
       "smuPortAttachedIp": smuPortAttachedIp,
       "permanentEntries": permanentEntries,
       "permanentEntriesTable": permanentEntriesTable,
       "permanentEntriesEntry": permanentEntriesEntry,
       "permanentEntriesMACAddr": permanentEntriesMACAddr,
       "permanentEntriesPortId": permanentEntriesPortId,
       "permanentEntriesCreateObj": permanentEntriesCreateObj,
       "permanentEntriesDeleteObj": permanentEntriesDeleteObj,
       "matrix": matrix,
       "matrixModuleTable": matrixModuleTable,
       "matrixModuleEntry": matrixModuleEntry,
       "matrixModuleIndex": matrixModuleIndex,
       "matrixModuleState": matrixModuleState,
       "matrixNumberConnected": matrixNumberConnected,
       "matrixMasterPort": matrixMasterPort,
       "matrixPortTable": matrixPortTable,
       "matrixPortEntry": matrixPortEntry,
       "matrixPortModuleIndex": matrixPortModuleIndex,
       "matrixPortIndex": matrixPortIndex,
       "matrixPort": matrixPort,
       "matrixPortType": matrixPortType,
       "matrixPortMajVer": matrixPortMajVer,
       "matrixPortMinVer": matrixPortMinVer,
       "matrixPortMac": matrixPortMac,
       "matrixPortIp": matrixPortIp,
       "matrixPortSubnetMask": matrixPortSubnetMask,
       "matrixPortGateway": matrixPortGateway,
       "matrixLastChange": matrixLastChange,
       "mediamodules": mediamodules,
       "mediaModuleTable": mediaModuleTable,
       "mediaModuleEntry": mediaModuleEntry,
       "moduleMode": moduleMode,
       "matrixAttachmentPort": matrixAttachmentPort,
       "mediaModuleChange": mediaModuleChange}
)
