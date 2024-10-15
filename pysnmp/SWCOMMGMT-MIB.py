# SNMP MIB module (SWCOMMGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SWCOMMGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:59:10 2024
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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")

(privateMgmt,) = mibBuilder.importSymbols(
    "SWPRIMGMT-MIB",
    "privateMgmt")


# MODULE-IDENTITY

swComMgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ErrorReturnCode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209)
        )
    )
    namedValues = NamedValues(
        *(("arpClassIdOnlyForIpSubnetVlan", 207),
          ("arpClassIdSpecified", 206),
          ("arpClassIdWithExistVid", 209),
          ("cannotModifyMltMemberPort", 201),
          ("cannotModifyVlanPortWithMltMemberPort", 205),
          ("ipSubnetVlanArpClassIdCannotBeZero", 208),
          ("mltWithDifferentVlan", 204),
          ("moreThan4PortsInMlt", 203),
          ("onlyOnePortInMlt", 202))
    )



# MIB Managed Objects in the order of their OIDs

_AgentConfigInfo_ObjectIdentity = ObjectIdentity
agentConfigInfo = _AgentConfigInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1)
)
_AgentBasicInfo_ObjectIdentity = ObjectIdentity
agentBasicInfo = _AgentBasicInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 1)
)


class _AgentRuntimeSwVersion_Type(DisplayString):
    """Custom type agentRuntimeSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_AgentRuntimeSwVersion_Type.__name__ = "DisplayString"
_AgentRuntimeSwVersion_Object = MibScalar
agentRuntimeSwVersion = _AgentRuntimeSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 1, 1),
    _AgentRuntimeSwVersion_Type()
)
agentRuntimeSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRuntimeSwVersion.setStatus("current")


class _AgentPromFwVersion_Type(DisplayString):
    """Custom type agentPromFwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_AgentPromFwVersion_Type.__name__ = "DisplayString"
_AgentPromFwVersion_Object = MibScalar
agentPromFwVersion = _AgentPromFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 1, 2),
    _AgentPromFwVersion_Type()
)
agentPromFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPromFwVersion.setStatus("current")


class _AgentHwRevision_Type(DisplayString):
    """Custom type agentHwRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_AgentHwRevision_Type.__name__ = "DisplayString"
_AgentHwRevision_Object = MibScalar
agentHwRevision = _AgentHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 1, 3),
    _AgentHwRevision_Type()
)
agentHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentHwRevision.setStatus("current")


class _AgentDeviceSerialNumber_Type(DisplayString):
    """Custom type agentDeviceSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 42),
    )


_AgentDeviceSerialNumber_Type.__name__ = "DisplayString"
_AgentDeviceSerialNumber_Object = MibScalar
agentDeviceSerialNumber = _AgentDeviceSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 1, 5),
    _AgentDeviceSerialNumber_Type()
)
agentDeviceSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDeviceSerialNumber.setStatus("current")


class _AgentMgmtProtocolCapability_Type(Integer32):
    """Custom type agentMgmtProtocolCapability based on Integer32"""
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
        *(("other", 1),
          ("snmp-ip", 2),
          ("snmp-ip-ipx", 4),
          ("snmp-ipx", 3))
    )


_AgentMgmtProtocolCapability_Type.__name__ = "Integer32"
_AgentMgmtProtocolCapability_Object = MibScalar
agentMgmtProtocolCapability = _AgentMgmtProtocolCapability_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 1, 6),
    _AgentMgmtProtocolCapability_Type()
)
agentMgmtProtocolCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMgmtProtocolCapability.setStatus("current")
_AgentMibCapabilityTable_Object = MibTable
agentMibCapabilityTable = _AgentMibCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 1, 7)
)
if mibBuilder.loadTexts:
    agentMibCapabilityTable.setStatus("current")
_AgentMibCapabilityEntry_Object = MibTableRow
agentMibCapabilityEntry = _AgentMibCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 1, 7, 1)
)
agentMibCapabilityEntry.setIndexNames(
    (0, "SWCOMMGMT-MIB", "agentMibCapabilityIndex"),
)
if mibBuilder.loadTexts:
    agentMibCapabilityEntry.setStatus("current")


class _AgentMibCapabilityIndex_Type(Integer32):
    """Custom type agentMibCapabilityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AgentMibCapabilityIndex_Type.__name__ = "Integer32"
_AgentMibCapabilityIndex_Object = MibTableColumn
agentMibCapabilityIndex = _AgentMibCapabilityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 1, 7, 1, 1),
    _AgentMibCapabilityIndex_Type()
)
agentMibCapabilityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMibCapabilityIndex.setStatus("current")


class _AgentMibCapabilityDescr_Type(DisplayString):
    """Custom type agentMibCapabilityDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AgentMibCapabilityDescr_Type.__name__ = "DisplayString"
_AgentMibCapabilityDescr_Object = MibTableColumn
agentMibCapabilityDescr = _AgentMibCapabilityDescr_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 1, 7, 1, 2),
    _AgentMibCapabilityDescr_Type()
)
agentMibCapabilityDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMibCapabilityDescr.setStatus("current")


class _AgentMibCapabilityVersion_Type(Integer32):
    """Custom type agentMibCapabilityVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AgentMibCapabilityVersion_Type.__name__ = "Integer32"
_AgentMibCapabilityVersion_Object = MibTableColumn
agentMibCapabilityVersion = _AgentMibCapabilityVersion_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 1, 7, 1, 3),
    _AgentMibCapabilityVersion_Type()
)
agentMibCapabilityVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMibCapabilityVersion.setStatus("current")


class _AgentMibCapabilityType_Type(Integer32):
    """Custom type agentMibCapabilityType based on Integer32"""
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
        *(("experiment", 4),
          ("other", 1),
          ("proprietary", 3),
          ("standard", 2))
    )


_AgentMibCapabilityType_Type.__name__ = "Integer32"
_AgentMibCapabilityType_Object = MibTableColumn
agentMibCapabilityType = _AgentMibCapabilityType_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 1, 7, 1, 4),
    _AgentMibCapabilityType_Type()
)
agentMibCapabilityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMibCapabilityType.setStatus("current")


class _AgentStatusConsoleInUse_Type(Integer32):
    """Custom type agentStatusConsoleInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("in-use", 2),
          ("not-in-use", 3),
          ("other", 1))
    )


_AgentStatusConsoleInUse_Type.__name__ = "Integer32"
_AgentStatusConsoleInUse_Object = MibScalar
agentStatusConsoleInUse = _AgentStatusConsoleInUse_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 1, 8),
    _AgentStatusConsoleInUse_Type()
)
agentStatusConsoleInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStatusConsoleInUse.setStatus("current")


class _AgentSerialPortDataBits_Type(Integer32):
    """Custom type agentSerialPortDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AgentSerialPortDataBits_Type.__name__ = "Integer32"
_AgentSerialPortDataBits_Object = MibScalar
agentSerialPortDataBits = _AgentSerialPortDataBits_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 1, 9),
    _AgentSerialPortDataBits_Type()
)
agentSerialPortDataBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSerialPortDataBits.setStatus("current")


class _AgentSerialPortParityBits_Type(Integer32):
    """Custom type agentSerialPortParityBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("none", 1)
    )


_AgentSerialPortParityBits_Type.__name__ = "Integer32"
_AgentSerialPortParityBits_Object = MibScalar
agentSerialPortParityBits = _AgentSerialPortParityBits_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 1, 10),
    _AgentSerialPortParityBits_Type()
)
agentSerialPortParityBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSerialPortParityBits.setStatus("current")


class _AgentSerialPortStopBits_Type(Integer32):
    """Custom type agentSerialPortStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AgentSerialPortStopBits_Type.__name__ = "Integer32"
_AgentSerialPortStopBits_Object = MibScalar
agentSerialPortStopBits = _AgentSerialPortStopBits_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 1, 11),
    _AgentSerialPortStopBits_Type()
)
agentSerialPortStopBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSerialPortStopBits.setStatus("current")


class _AgentPrimaryPowerState_Type(Integer32):
    """Custom type agentPrimaryPowerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-ready", 2),
          ("ready", 1))
    )


_AgentPrimaryPowerState_Type.__name__ = "Integer32"
_AgentPrimaryPowerState_Object = MibScalar
agentPrimaryPowerState = _AgentPrimaryPowerState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 1, 12),
    _AgentPrimaryPowerState_Type()
)
agentPrimaryPowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPrimaryPowerState.setStatus("current")


class _AgentRedundantPowerState_Type(Integer32):
    """Custom type agentRedundantPowerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-ready", 2),
          ("ready", 1))
    )


_AgentRedundantPowerState_Type.__name__ = "Integer32"
_AgentRedundantPowerState_Object = MibScalar
agentRedundantPowerState = _AgentRedundantPowerState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 1, 13),
    _AgentRedundantPowerState_Type()
)
agentRedundantPowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRedundantPowerState.setStatus("current")
_AgentBasicConfig_ObjectIdentity = ObjectIdentity
agentBasicConfig = _AgentBasicConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 2)
)


class _AgentFirmwareFile_Type(DisplayString):
    """Custom type agentFirmwareFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AgentFirmwareFile_Type.__name__ = "DisplayString"
_AgentFirmwareFile_Object = MibScalar
agentFirmwareFile = _AgentFirmwareFile_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 2, 1),
    _AgentFirmwareFile_Type()
)
agentFirmwareFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentFirmwareFile.setStatus("current")
_AgentFirmwareSourceAddr_Type = IpAddress
_AgentFirmwareSourceAddr_Object = MibScalar
agentFirmwareSourceAddr = _AgentFirmwareSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 2, 2),
    _AgentFirmwareSourceAddr_Type()
)
agentFirmwareSourceAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentFirmwareSourceAddr.setStatus("current")


class _AgentFirmwareUpdateCtrl_Type(Integer32):
    """Custom type agentFirmwareUpdateCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activate", 2),
          ("other", 1))
    )


_AgentFirmwareUpdateCtrl_Type.__name__ = "Integer32"
_AgentFirmwareUpdateCtrl_Object = MibScalar
agentFirmwareUpdateCtrl = _AgentFirmwareUpdateCtrl_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 2, 3),
    _AgentFirmwareUpdateCtrl_Type()
)
agentFirmwareUpdateCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentFirmwareUpdateCtrl.setStatus("current")


class _AgentFirmwareUpdateState_Type(Integer32):
    """Custom type agentFirmwareUpdateState based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("complete", 7),
          ("disk-full", 6),
          ("file-not-found", 5),
          ("in-process", 2),
          ("invalid-file", 3),
          ("other", 1),
          ("tftp-establish-fail", 9),
          ("time-out", 8),
          ("violation", 4))
    )


_AgentFirmwareUpdateState_Type.__name__ = "Integer32"
_AgentFirmwareUpdateState_Object = MibScalar
agentFirmwareUpdateState = _AgentFirmwareUpdateState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 2, 4),
    _AgentFirmwareUpdateState_Type()
)
agentFirmwareUpdateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentFirmwareUpdateState.setStatus("current")


class _AgentSystemRestart_Type(Integer32):
    """Custom type agentSystemRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cold-start", 2),
          ("no-restart", 3),
          ("other", 1))
    )


_AgentSystemRestart_Type.__name__ = "Integer32"
_AgentSystemRestart_Object = MibScalar
agentSystemRestart = _AgentSystemRestart_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 2, 5),
    _AgentSystemRestart_Type()
)
agentSystemRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSystemRestart.setStatus("current")


class _AgentRs232PortConfig_Type(Integer32):
    """Custom type agentRs232PortConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("console", 2),
          ("other", 1),
          ("out-of-band", 3))
    )


_AgentRs232PortConfig_Type.__name__ = "Integer32"
_AgentRs232PortConfig_Object = MibScalar
agentRs232PortConfig = _AgentRs232PortConfig_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 2, 6),
    _AgentRs232PortConfig_Type()
)
agentRs232PortConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRs232PortConfig.setStatus("current")


class _AgentBaudRateConfig_Type(Integer32):
    """Custom type agentBaudRateConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("baudRate-115200", 7),
          ("baudRate-19200", 4),
          ("baudRate-2400", 2),
          ("baudRate-38400", 5),
          ("baudRate-57200", 6),
          ("baudRate-9600", 3),
          ("other", 1))
    )


_AgentBaudRateConfig_Type.__name__ = "Integer32"
_AgentBaudRateConfig_Object = MibScalar
agentBaudRateConfig = _AgentBaudRateConfig_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 2, 7),
    _AgentBaudRateConfig_Type()
)
agentBaudRateConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBaudRateConfig.setStatus("current")


class _AgentAutoLogoutConfig_Type(Integer32):
    """Custom type agentAutoLogoutConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("autoLogout-10mins", 5),
          ("autoLogout-15mins", 6),
          ("autoLogout-2mins", 3),
          ("autoLogout-5mins", 4),
          ("never", 2),
          ("other", 1))
    )


_AgentAutoLogoutConfig_Type.__name__ = "Integer32"
_AgentAutoLogoutConfig_Object = MibScalar
agentAutoLogoutConfig = _AgentAutoLogoutConfig_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 2, 8),
    _AgentAutoLogoutConfig_Type()
)
agentAutoLogoutConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAutoLogoutConfig.setStatus("current")


class _AgentTelnetState_Type(Integer32):
    """Custom type agentTelnetState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_AgentTelnetState_Type.__name__ = "Integer32"
_AgentTelnetState_Object = MibScalar
agentTelnetState = _AgentTelnetState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 2, 9),
    _AgentTelnetState_Type()
)
agentTelnetState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTelnetState.setStatus("current")


class _AgentWebState_Type(Integer32):
    """Custom type agentWebState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_AgentWebState_Type.__name__ = "Integer32"
_AgentWebState_Object = MibScalar
agentWebState = _AgentWebState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 2, 10),
    _AgentWebState_Type()
)
agentWebState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentWebState.setStatus("current")


class _AgentFactoryReset_Type(Integer32):
    """Custom type agentFactoryReset based on Integer32"""
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
        *(("config", 3),
          ("no-reset", 5),
          ("other", 1),
          ("reset", 2),
          ("system", 4))
    )


_AgentFactoryReset_Type.__name__ = "Integer32"
_AgentFactoryReset_Object = MibScalar
agentFactoryReset = _AgentFactoryReset_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 2, 11),
    _AgentFactoryReset_Type()
)
agentFactoryReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentFactoryReset.setStatus("current")
_AgentIpProtoConfig_ObjectIdentity = ObjectIdentity
agentIpProtoConfig = _AgentIpProtoConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 3)
)


class _AgentIpNumOfIf_Type(Integer32):
    """Custom type agentIpNumOfIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AgentIpNumOfIf_Type.__name__ = "Integer32"
_AgentIpNumOfIf_Object = MibScalar
agentIpNumOfIf = _AgentIpNumOfIf_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 3, 1),
    _AgentIpNumOfIf_Type()
)
agentIpNumOfIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpNumOfIf.setStatus("current")
_AgentIpIfTable_Object = MibTable
agentIpIfTable = _AgentIpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    agentIpIfTable.setStatus("current")
_AgentIpIfEntry_Object = MibTableRow
agentIpIfEntry = _AgentIpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 3, 2, 1)
)
agentIpIfEntry.setIndexNames(
    (0, "SWCOMMGMT-MIB", "agentIpIfIndex"),
)
if mibBuilder.loadTexts:
    agentIpIfEntry.setStatus("current")


class _AgentIpIfIndex_Type(Integer32):
    """Custom type agentIpIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgentIpIfIndex_Type.__name__ = "Integer32"
_AgentIpIfIndex_Object = MibTableColumn
agentIpIfIndex = _AgentIpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 3, 2, 1, 1),
    _AgentIpIfIndex_Type()
)
agentIpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpIfIndex.setStatus("current")
_AgentIpIfAddress_Type = IpAddress
_AgentIpIfAddress_Object = MibTableColumn
agentIpIfAddress = _AgentIpIfAddress_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 3, 2, 1, 2),
    _AgentIpIfAddress_Type()
)
agentIpIfAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpIfAddress.setStatus("current")
_AgentIpIfNetMask_Type = IpAddress
_AgentIpIfNetMask_Object = MibTableColumn
agentIpIfNetMask = _AgentIpIfNetMask_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 3, 2, 1, 3),
    _AgentIpIfNetMask_Type()
)
agentIpIfNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpIfNetMask.setStatus("current")
_AgentIpIfDefaultRouter_Type = IpAddress
_AgentIpIfDefaultRouter_Object = MibTableColumn
agentIpIfDefaultRouter = _AgentIpIfDefaultRouter_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 3, 2, 1, 4),
    _AgentIpIfDefaultRouter_Type()
)
agentIpIfDefaultRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpIfDefaultRouter.setStatus("current")
_AgentIpIfMacAddr_Type = PhysAddress
_AgentIpIfMacAddr_Object = MibTableColumn
agentIpIfMacAddr = _AgentIpIfMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 3, 2, 1, 5),
    _AgentIpIfMacAddr_Type()
)
agentIpIfMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpIfMacAddr.setStatus("current")


class _AgentIpIfType_Type(Integer32):
    """Custom type agentIpIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6,
              28)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-csmacd", 6),
          ("other", 1),
          ("slip", 28))
    )


_AgentIpIfType_Type.__name__ = "Integer32"
_AgentIpIfType_Object = MibTableColumn
agentIpIfType = _AgentIpIfType_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 3, 2, 1, 6),
    _AgentIpIfType_Type()
)
agentIpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpIfType.setStatus("current")
_AgentIpBootServerAddr_Type = IpAddress
_AgentIpBootServerAddr_Object = MibScalar
agentIpBootServerAddr = _AgentIpBootServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 3, 3),
    _AgentIpBootServerAddr_Type()
)
agentIpBootServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpBootServerAddr.setStatus("current")


class _AgentIpGetIpFromBootpServer_Type(Integer32):
    """Custom type agentIpGetIpFromBootpServer based on Integer32"""
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
        *(("frombootp", 3),
          ("fromdhcp", 4),
          ("manual", 2),
          ("other", 1))
    )


_AgentIpGetIpFromBootpServer_Type.__name__ = "Integer32"
_AgentIpGetIpFromBootpServer_Object = MibScalar
agentIpGetIpFromBootpServer = _AgentIpGetIpFromBootpServer_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 3, 4),
    _AgentIpGetIpFromBootpServer_Type()
)
agentIpGetIpFromBootpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpGetIpFromBootpServer.setStatus("current")
_AgentIpSystemIpAddr_Type = IpAddress
_AgentIpSystemIpAddr_Object = MibScalar
agentIpSystemIpAddr = _AgentIpSystemIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 3, 5),
    _AgentIpSystemIpAddr_Type()
)
agentIpSystemIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpSystemIpAddr.setStatus("current")
_AgentIpSystemSubnetMask_Type = IpAddress
_AgentIpSystemSubnetMask_Object = MibScalar
agentIpSystemSubnetMask = _AgentIpSystemSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 3, 6),
    _AgentIpSystemSubnetMask_Type()
)
agentIpSystemSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpSystemSubnetMask.setStatus("current")
_AgentIpDefaultGateway_Type = IpAddress
_AgentIpDefaultGateway_Object = MibScalar
agentIpDefaultGateway = _AgentIpDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 3, 7),
    _AgentIpDefaultGateway_Type()
)
agentIpDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpDefaultGateway.setStatus("current")
_AgentCommunityTable_Object = MibTable
agentCommunityTable = _AgentCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    agentCommunityTable.setStatus("current")
_AgentCommunityEntry_Object = MibTableRow
agentCommunityEntry = _AgentCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 4, 1)
)
agentCommunityEntry.setIndexNames(
    (0, "SWCOMMGMT-MIB", "agentCommunityString"),
)
if mibBuilder.loadTexts:
    agentCommunityEntry.setStatus("current")


class _AgentCommunityString_Type(DisplayString):
    """Custom type agentCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AgentCommunityString_Type.__name__ = "DisplayString"
_AgentCommunityString_Object = MibTableColumn
agentCommunityString = _AgentCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 4, 1, 1),
    _AgentCommunityString_Type()
)
agentCommunityString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCommunityString.setStatus("current")


class _AgentCommunityLevel_Type(Integer32):
    """Custom type agentCommunityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("read-only", 2),
          ("read-write", 3))
    )


_AgentCommunityLevel_Type.__name__ = "Integer32"
_AgentCommunityLevel_Object = MibTableColumn
agentCommunityLevel = _AgentCommunityLevel_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 4, 1, 2),
    _AgentCommunityLevel_Type()
)
agentCommunityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCommunityLevel.setStatus("current")


class _AgentCommunitystate_Type(Integer32):
    """Custom type agentCommunitystate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1),
          ("valid", 3))
    )


_AgentCommunitystate_Type.__name__ = "Integer32"
_AgentCommunitystate_Object = MibTableColumn
agentCommunitystate = _AgentCommunitystate_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 4, 1, 3),
    _AgentCommunitystate_Type()
)
agentCommunitystate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCommunitystate.setStatus("current")
_AgentTrustHostTable_Object = MibTable
agentTrustHostTable = _AgentTrustHostTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    agentTrustHostTable.setStatus("current")
_AgentTrustHostEntry_Object = MibTableRow
agentTrustHostEntry = _AgentTrustHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 5, 1)
)
agentTrustHostEntry.setIndexNames(
    (0, "SWCOMMGMT-MIB", "agentTrustHostId"),
)
if mibBuilder.loadTexts:
    agentTrustHostEntry.setStatus("current")


class _AgentTrustHostId_Type(Integer32):
    """Custom type agentTrustHostId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AgentTrustHostId_Type.__name__ = "Integer32"
_AgentTrustHostId_Object = MibTableColumn
agentTrustHostId = _AgentTrustHostId_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 5, 1, 1),
    _AgentTrustHostId_Type()
)
agentTrustHostId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentTrustHostId.setStatus("current")
_AgentTrustHostIPAddr_Type = IpAddress
_AgentTrustHostIPAddr_Object = MibTableColumn
agentTrustHostIPAddr = _AgentTrustHostIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 5, 1, 2),
    _AgentTrustHostIPAddr_Type()
)
agentTrustHostIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTrustHostIPAddr.setStatus("current")


class _AgentTrustHostState_Type(Integer32):
    """Custom type agentTrustHostState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1),
          ("valid", 3))
    )


_AgentTrustHostState_Type.__name__ = "Integer32"
_AgentTrustHostState_Object = MibTableColumn
agentTrustHostState = _AgentTrustHostState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 5, 1, 3),
    _AgentTrustHostState_Type()
)
agentTrustHostState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTrustHostState.setStatus("current")
_AgentTrustHostIPMask_Type = IpAddress
_AgentTrustHostIPMask_Object = MibTableColumn
agentTrustHostIPMask = _AgentTrustHostIPMask_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 5, 1, 4),
    _AgentTrustHostIPMask_Type()
)
agentTrustHostIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTrustHostIPMask.setStatus("current")
_AgentLogConfig_ObjectIdentity = ObjectIdentity
agentLogConfig = _AgentLogConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 6)
)


class _AgentLogUploadLogFileName_Type(DisplayString):
    """Custom type agentLogUploadLogFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AgentLogUploadLogFileName_Type.__name__ = "DisplayString"
_AgentLogUploadLogFileName_Object = MibScalar
agentLogUploadLogFileName = _AgentLogUploadLogFileName_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 6, 1),
    _AgentLogUploadLogFileName_Type()
)
agentLogUploadLogFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLogUploadLogFileName.setStatus("current")
_AgentLogUploadLogSourceAddr_Type = IpAddress
_AgentLogUploadLogSourceAddr_Object = MibScalar
agentLogUploadLogSourceAddr = _AgentLogUploadLogSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 6, 2),
    _AgentLogUploadLogSourceAddr_Type()
)
agentLogUploadLogSourceAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLogUploadLogSourceAddr.setStatus("current")


class _AgentLogUploadLog_Type(Integer32):
    """Custom type agentLogUploadLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("normal", 1))
    )


_AgentLogUploadLog_Type.__name__ = "Integer32"
_AgentLogUploadLog_Object = MibScalar
agentLogUploadLog = _AgentLogUploadLog_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 6, 3),
    _AgentLogUploadLog_Type()
)
agentLogUploadLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLogUploadLog.setStatus("current")


class _AgentLogUploadLogState_Type(Integer32):
    """Custom type agentLogUploadLogState based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("complete", 7),
          ("disk-full", 6),
          ("file-not-found", 5),
          ("in-process", 2),
          ("invalid-file", 3),
          ("other", 1),
          ("tftp-establish-fail", 9),
          ("time-out", 8),
          ("violation", 4))
    )


_AgentLogUploadLogState_Type.__name__ = "Integer32"
_AgentLogUploadLogState_Object = MibScalar
agentLogUploadLogState = _AgentLogUploadLogState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 6, 4),
    _AgentLogUploadLogState_Type()
)
agentLogUploadLogState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLogUploadLogState.setStatus("current")


class _AgentLogClearLog_Type(Integer32):
    """Custom type agentLogClearLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("normal", 1))
    )


_AgentLogClearLog_Type.__name__ = "Integer32"
_AgentLogClearLog_Object = MibScalar
agentLogClearLog = _AgentLogClearLog_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 6, 5),
    _AgentLogClearLog_Type()
)
agentLogClearLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLogClearLog.setStatus("current")
_AgentTblSize_ObjectIdentity = ObjectIdentity
agentTblSize = _AgentTblSize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 7)
)


class _AgentArpNumber_Type(Integer32):
    """Custom type agentArpNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AgentArpNumber_Type.__name__ = "Integer32"
_AgentArpNumber_Object = MibScalar
agentArpNumber = _AgentArpNumber_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 7, 1),
    _AgentArpNumber_Type()
)
agentArpNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentArpNumber.setStatus("current")


class _AgentIpNumber_Type(Integer32):
    """Custom type agentIpNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AgentIpNumber_Type.__name__ = "Integer32"
_AgentIpNumber_Object = MibScalar
agentIpNumber = _AgentIpNumber_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 7, 2),
    _AgentIpNumber_Type()
)
agentIpNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpNumber.setStatus("current")


class _AgentStaticVlanNumber_Type(Integer32):
    """Custom type agentStaticVlanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AgentStaticVlanNumber_Type.__name__ = "Integer32"
_AgentStaticVlanNumber_Object = MibScalar
agentStaticVlanNumber = _AgentStaticVlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 7, 3),
    _AgentStaticVlanNumber_Type()
)
agentStaticVlanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStaticVlanNumber.setStatus("current")
_AgentRTC_ObjectIdentity = ObjectIdentity
agentRTC = _AgentRTC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 8)
)


class _AgentRTCYear_Type(Integer32):
    """Custom type agentRTCYear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1980, 3999),
    )


_AgentRTCYear_Type.__name__ = "Integer32"
_AgentRTCYear_Object = MibScalar
agentRTCYear = _AgentRTCYear_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 8, 1),
    _AgentRTCYear_Type()
)
agentRTCYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRTCYear.setStatus("current")


class _AgentRTCMonth_Type(Integer32):
    """Custom type agentRTCMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_AgentRTCMonth_Type.__name__ = "Integer32"
_AgentRTCMonth_Object = MibScalar
agentRTCMonth = _AgentRTCMonth_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 8, 2),
    _AgentRTCMonth_Type()
)
agentRTCMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRTCMonth.setStatus("current")


class _AgentRTCDate_Type(Integer32):
    """Custom type agentRTCDate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_AgentRTCDate_Type.__name__ = "Integer32"
_AgentRTCDate_Object = MibScalar
agentRTCDate = _AgentRTCDate_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 8, 3),
    _AgentRTCDate_Type()
)
agentRTCDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRTCDate.setStatus("current")


class _AgentRTCHour_Type(Integer32):
    """Custom type agentRTCHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_AgentRTCHour_Type.__name__ = "Integer32"
_AgentRTCHour_Object = MibScalar
agentRTCHour = _AgentRTCHour_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 8, 4),
    _AgentRTCHour_Type()
)
agentRTCHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRTCHour.setStatus("current")


class _AgentRTCMinute_Type(Integer32):
    """Custom type agentRTCMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_AgentRTCMinute_Type.__name__ = "Integer32"
_AgentRTCMinute_Object = MibScalar
agentRTCMinute = _AgentRTCMinute_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 8, 5),
    _AgentRTCMinute_Type()
)
agentRTCMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRTCMinute.setStatus("current")


class _AgentRTCSecond_Type(Integer32):
    """Custom type agentRTCSecond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_AgentRTCSecond_Type.__name__ = "Integer32"
_AgentRTCSecond_Object = MibScalar
agentRTCSecond = _AgentRTCSecond_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 8, 6),
    _AgentRTCSecond_Type()
)
agentRTCSecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRTCSecond.setStatus("current")


class _AgentRTCWeekDay_Type(Integer32):
    """Custom type agentRTCWeekDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("date-Friday", 6),
          ("date-Monday", 2),
          ("date-Saturday", 7),
          ("date-Sunday", 1),
          ("date-Thursday", 5),
          ("date-Tuesday", 3),
          ("date-Wednesday", 4))
    )


_AgentRTCWeekDay_Type.__name__ = "Integer32"
_AgentRTCWeekDay_Object = MibScalar
agentRTCWeekDay = _AgentRTCWeekDay_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 8, 7),
    _AgentRTCWeekDay_Type()
)
agentRTCWeekDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRTCWeekDay.setStatus("current")
_AgentMIBTraps_ObjectIdentity = ObjectIdentity
agentMIBTraps = _AgentMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 9)
)
_AgentSyslog_ObjectIdentity = ObjectIdentity
agentSyslog = _AgentSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 10)
)


class _AgentSyslogState_Type(Integer32):
    """Custom type agentSyslogState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_AgentSyslogState_Type.__name__ = "Integer32"
_AgentSyslogState_Object = MibScalar
agentSyslogState = _AgentSyslogState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 10, 1),
    _AgentSyslogState_Type()
)
agentSyslogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSyslogState.setStatus("current")


class _AgentSyslogMaxHostSupport_Type(Integer32):
    """Custom type agentSyslogMaxHostSupport based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_AgentSyslogMaxHostSupport_Type.__name__ = "Integer32"
_AgentSyslogMaxHostSupport_Object = MibScalar
agentSyslogMaxHostSupport = _AgentSyslogMaxHostSupport_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 10, 2),
    _AgentSyslogMaxHostSupport_Type()
)
agentSyslogMaxHostSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSyslogMaxHostSupport.setStatus("current")
_AgentSyslogHostTable_Object = MibTable
agentSyslogHostTable = _AgentSyslogHostTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 10, 3)
)
if mibBuilder.loadTexts:
    agentSyslogHostTable.setStatus("current")
_AgentSyslogHostEntry_Object = MibTableRow
agentSyslogHostEntry = _AgentSyslogHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 10, 3, 1)
)
agentSyslogHostEntry.setIndexNames(
    (0, "SWCOMMGMT-MIB", "agentSyslogHostId"),
)
if mibBuilder.loadTexts:
    agentSyslogHostEntry.setStatus("current")


class _AgentSyslogHostId_Type(Integer32):
    """Custom type agentSyslogHostId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AgentSyslogHostId_Type.__name__ = "Integer32"
_AgentSyslogHostId_Object = MibTableColumn
agentSyslogHostId = _AgentSyslogHostId_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 10, 3, 1, 1),
    _AgentSyslogHostId_Type()
)
agentSyslogHostId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSyslogHostId.setStatus("current")
_AgentSyslogHostIp_Type = IpAddress
_AgentSyslogHostIp_Object = MibTableColumn
agentSyslogHostIp = _AgentSyslogHostIp_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 10, 3, 1, 2),
    _AgentSyslogHostIp_Type()
)
agentSyslogHostIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSyslogHostIp.setStatus("current")


class _AgentSyslogHostSeverity_Type(Bits):
    """Custom type agentSyslogHostSeverity based on Bits"""
    namedValues = NamedValues(
        *(("error", 2),
          ("fatal", 3),
          ("informational", 0),
          ("warning", 1))
    )

_AgentSyslogHostSeverity_Type.__name__ = "Bits"
_AgentSyslogHostSeverity_Object = MibTableColumn
agentSyslogHostSeverity = _AgentSyslogHostSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 10, 3, 1, 3),
    _AgentSyslogHostSeverity_Type()
)
agentSyslogHostSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSyslogHostSeverity.setStatus("current")


class _AgentSyslogHostFacility_Type(Integer32):
    """Custom type agentSyslogHostFacility based on Integer32"""
    defaultValue = 8

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("local0", 1),
          ("local1", 2),
          ("local2", 3),
          ("local3", 4),
          ("local4", 5),
          ("local5", 6),
          ("local6", 7),
          ("local7", 8))
    )


_AgentSyslogHostFacility_Type.__name__ = "Integer32"
_AgentSyslogHostFacility_Object = MibTableColumn
agentSyslogHostFacility = _AgentSyslogHostFacility_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 10, 3, 1, 4),
    _AgentSyslogHostFacility_Type()
)
agentSyslogHostFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSyslogHostFacility.setStatus("current")


class _AgentSyslogHostUDPPort_Type(Integer32):
    """Custom type agentSyslogHostUDPPort based on Integer32"""
    defaultValue = 514

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(514, 530),
    )


_AgentSyslogHostUDPPort_Type.__name__ = "Integer32"
_AgentSyslogHostUDPPort_Object = MibTableColumn
agentSyslogHostUDPPort = _AgentSyslogHostUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 10, 3, 1, 5),
    _AgentSyslogHostUDPPort_Type()
)
agentSyslogHostUDPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSyslogHostUDPPort.setStatus("current")


class _AgentSyslogHostState_Type(Integer32):
    """Custom type agentSyslogHostState based on Integer32"""
    defaultValue = 2

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
        *(("disabled", 2),
          ("enabled", 3),
          ("invalid", 4),
          ("other", 1))
    )


_AgentSyslogHostState_Type.__name__ = "Integer32"
_AgentSyslogHostState_Object = MibTableColumn
agentSyslogHostState = _AgentSyslogHostState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 10, 3, 1, 6),
    _AgentSyslogHostState_Type()
)
agentSyslogHostState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSyslogHostState.setStatus("current")


class _AgentRemoteUserLogState_Type(Integer32):
    """Custom type agentRemoteUserLogState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_AgentRemoteUserLogState_Type.__name__ = "Integer32"
_AgentRemoteUserLogState_Object = MibScalar
agentRemoteUserLogState = _AgentRemoteUserLogState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 10, 4),
    _AgentRemoteUserLogState_Type()
)
agentRemoteUserLogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRemoteUserLogState.setStatus("current")

# Managed Objects groups


# Notification objects

primaryPowerOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 0, 1)
)
if mibBuilder.loadTexts:
    primaryPowerOn.setStatus(
        ""
    )

primaryPowerOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 0, 2)
)
if mibBuilder.loadTexts:
    primaryPowerOff.setStatus(
        ""
    )

redundantPowerOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 0, 3)
)
if mibBuilder.loadTexts:
    redundantPowerOn.setStatus(
        ""
    )

redundantPowerOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 0, 4)
)
if mibBuilder.loadTexts:
    redundantPowerOff.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWCOMMGMT-MIB",
    **{"ErrorReturnCode": ErrorReturnCode,
       "swComMgmtMIB": swComMgmtMIB,
       "primaryPowerOn": primaryPowerOn,
       "primaryPowerOff": primaryPowerOff,
       "redundantPowerOn": redundantPowerOn,
       "redundantPowerOff": redundantPowerOff,
       "agentConfigInfo": agentConfigInfo,
       "agentBasicInfo": agentBasicInfo,
       "agentRuntimeSwVersion": agentRuntimeSwVersion,
       "agentPromFwVersion": agentPromFwVersion,
       "agentHwRevision": agentHwRevision,
       "agentDeviceSerialNumber": agentDeviceSerialNumber,
       "agentMgmtProtocolCapability": agentMgmtProtocolCapability,
       "agentMibCapabilityTable": agentMibCapabilityTable,
       "agentMibCapabilityEntry": agentMibCapabilityEntry,
       "agentMibCapabilityIndex": agentMibCapabilityIndex,
       "agentMibCapabilityDescr": agentMibCapabilityDescr,
       "agentMibCapabilityVersion": agentMibCapabilityVersion,
       "agentMibCapabilityType": agentMibCapabilityType,
       "agentStatusConsoleInUse": agentStatusConsoleInUse,
       "agentSerialPortDataBits": agentSerialPortDataBits,
       "agentSerialPortParityBits": agentSerialPortParityBits,
       "agentSerialPortStopBits": agentSerialPortStopBits,
       "agentPrimaryPowerState": agentPrimaryPowerState,
       "agentRedundantPowerState": agentRedundantPowerState,
       "agentBasicConfig": agentBasicConfig,
       "agentFirmwareFile": agentFirmwareFile,
       "agentFirmwareSourceAddr": agentFirmwareSourceAddr,
       "agentFirmwareUpdateCtrl": agentFirmwareUpdateCtrl,
       "agentFirmwareUpdateState": agentFirmwareUpdateState,
       "agentSystemRestart": agentSystemRestart,
       "agentRs232PortConfig": agentRs232PortConfig,
       "agentBaudRateConfig": agentBaudRateConfig,
       "agentAutoLogoutConfig": agentAutoLogoutConfig,
       "agentTelnetState": agentTelnetState,
       "agentWebState": agentWebState,
       "agentFactoryReset": agentFactoryReset,
       "agentIpProtoConfig": agentIpProtoConfig,
       "agentIpNumOfIf": agentIpNumOfIf,
       "agentIpIfTable": agentIpIfTable,
       "agentIpIfEntry": agentIpIfEntry,
       "agentIpIfIndex": agentIpIfIndex,
       "agentIpIfAddress": agentIpIfAddress,
       "agentIpIfNetMask": agentIpIfNetMask,
       "agentIpIfDefaultRouter": agentIpIfDefaultRouter,
       "agentIpIfMacAddr": agentIpIfMacAddr,
       "agentIpIfType": agentIpIfType,
       "agentIpBootServerAddr": agentIpBootServerAddr,
       "agentIpGetIpFromBootpServer": agentIpGetIpFromBootpServer,
       "agentIpSystemIpAddr": agentIpSystemIpAddr,
       "agentIpSystemSubnetMask": agentIpSystemSubnetMask,
       "agentIpDefaultGateway": agentIpDefaultGateway,
       "agentCommunityTable": agentCommunityTable,
       "agentCommunityEntry": agentCommunityEntry,
       "agentCommunityString": agentCommunityString,
       "agentCommunityLevel": agentCommunityLevel,
       "agentCommunitystate": agentCommunitystate,
       "agentTrustHostTable": agentTrustHostTable,
       "agentTrustHostEntry": agentTrustHostEntry,
       "agentTrustHostId": agentTrustHostId,
       "agentTrustHostIPAddr": agentTrustHostIPAddr,
       "agentTrustHostState": agentTrustHostState,
       "agentTrustHostIPMask": agentTrustHostIPMask,
       "agentLogConfig": agentLogConfig,
       "agentLogUploadLogFileName": agentLogUploadLogFileName,
       "agentLogUploadLogSourceAddr": agentLogUploadLogSourceAddr,
       "agentLogUploadLog": agentLogUploadLog,
       "agentLogUploadLogState": agentLogUploadLogState,
       "agentLogClearLog": agentLogClearLog,
       "agentTblSize": agentTblSize,
       "agentArpNumber": agentArpNumber,
       "agentIpNumber": agentIpNumber,
       "agentStaticVlanNumber": agentStaticVlanNumber,
       "agentRTC": agentRTC,
       "agentRTCYear": agentRTCYear,
       "agentRTCMonth": agentRTCMonth,
       "agentRTCDate": agentRTCDate,
       "agentRTCHour": agentRTCHour,
       "agentRTCMinute": agentRTCMinute,
       "agentRTCSecond": agentRTCSecond,
       "agentRTCWeekDay": agentRTCWeekDay,
       "agentMIBTraps": agentMIBTraps,
       "agentSyslog": agentSyslog,
       "agentSyslogState": agentSyslogState,
       "agentSyslogMaxHostSupport": agentSyslogMaxHostSupport,
       "agentSyslogHostTable": agentSyslogHostTable,
       "agentSyslogHostEntry": agentSyslogHostEntry,
       "agentSyslogHostId": agentSyslogHostId,
       "agentSyslogHostIp": agentSyslogHostIp,
       "agentSyslogHostSeverity": agentSyslogHostSeverity,
       "agentSyslogHostFacility": agentSyslogHostFacility,
       "agentSyslogHostUDPPort": agentSyslogHostUDPPort,
       "agentSyslogHostState": agentSyslogHostState,
       "agentRemoteUserLogState": agentRemoteUserLogState}
)
