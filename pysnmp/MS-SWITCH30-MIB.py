# SNMP MIB module (MS-SWITCH30-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MS-SWITCH30-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:23:51 2024
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

mib3 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3)
)
mib3.setRevisions(
        ("2011-04-11 00:00",
         "2011-03-03 00:00",
         "2010-12-18 00:00",
         "2010-08-30 00:00",
         "2010-06-24 00:00",
         "2010-05-03 00:00",
         "2010-01-19 00:00",
         "2009-12-22 00:00",
         "2009-11-17 00:00",
         "2009-06-03 00:00",
         "2009-04-29 00:00",
         "2009-01-12 00:00",
         "2008-09-01 00:00",
         "2008-06-17 00:00",
         "2007-07-12 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Microsens_ObjectIdentity = ObjectIdentity
microsens = _Microsens_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181)
)
_ManagedSwitches_ObjectIdentity = ObjectIdentity
managedSwitches = _ManagedSwitches_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10)
)
_Device_ObjectIdentity = ObjectIdentity
device = _Device_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 1)
)


class _DeviceArtNo_Type(DisplayString):
    """Custom type deviceArtNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DeviceArtNo_Type.__name__ = "DisplayString"
_DeviceArtNo_Object = MibScalar
deviceArtNo = _DeviceArtNo_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 1, 1),
    _DeviceArtNo_Type()
)
deviceArtNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceArtNo.setStatus("current")


class _DeviceSerNo_Type(DisplayString):
    """Custom type deviceSerNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DeviceSerNo_Type.__name__ = "DisplayString"
_DeviceSerNo_Object = MibScalar
deviceSerNo = _DeviceSerNo_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 1, 2),
    _DeviceSerNo_Type()
)
deviceSerNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceSerNo.setStatus("current")


class _DeviceHardware_Type(DisplayString):
    """Custom type deviceHardware based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DeviceHardware_Type.__name__ = "DisplayString"
_DeviceHardware_Object = MibScalar
deviceHardware = _DeviceHardware_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 1, 3),
    _DeviceHardware_Type()
)
deviceHardware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceHardware.setStatus("current")


class _DeviceDescription_Type(DisplayString):
    """Custom type deviceDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DeviceDescription_Type.__name__ = "DisplayString"
_DeviceDescription_Object = MibScalar
deviceDescription = _DeviceDescription_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 1, 4),
    _DeviceDescription_Type()
)
deviceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceDescription.setStatus("current")


class _DeviceName_Type(DisplayString):
    """Custom type deviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_DeviceName_Type.__name__ = "DisplayString"
_DeviceName_Object = MibScalar
deviceName = _DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 1, 5),
    _DeviceName_Type()
)
deviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceName.setStatus("current")


class _DeviceLocation_Type(DisplayString):
    """Custom type deviceLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_DeviceLocation_Type.__name__ = "DisplayString"
_DeviceLocation_Object = MibScalar
deviceLocation = _DeviceLocation_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 1, 6),
    _DeviceLocation_Type()
)
deviceLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceLocation.setStatus("current")


class _DeviceContact_Type(DisplayString):
    """Custom type deviceContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_DeviceContact_Type.__name__ = "DisplayString"
_DeviceContact_Object = MibScalar
deviceContact = _DeviceContact_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 1, 7),
    _DeviceContact_Type()
)
deviceContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceContact.setStatus("current")


class _DeviceGroup_Type(DisplayString):
    """Custom type deviceGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_DeviceGroup_Type.__name__ = "DisplayString"
_DeviceGroup_Object = MibScalar
deviceGroup = _DeviceGroup_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 1, 8),
    _DeviceGroup_Type()
)
deviceGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceGroup.setStatus("current")
_DeviceTemperature_Type = Integer32
_DeviceTemperature_Object = MibScalar
deviceTemperature = _DeviceTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 1, 9),
    _DeviceTemperature_Type()
)
deviceTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceTemperature.setStatus("current")


class _DeviceTemperatureLevel_Type(Integer32):
    """Custom type deviceTemperatureLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("criticalHigh", 5),
          ("criticalLow", 1),
          ("high", 4),
          ("low", 2),
          ("normal", 3),
          ("shutdown", 6),
          ("undefined", 254),
          ("unsupported", 255))
    )


_DeviceTemperatureLevel_Type.__name__ = "Integer32"
_DeviceTemperatureLevel_Object = MibScalar
deviceTemperatureLevel = _DeviceTemperatureLevel_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 1, 10),
    _DeviceTemperatureLevel_Type()
)
deviceTemperatureLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceTemperatureLevel.setStatus("current")
_DeviceUpTime_Type = TimeTicks
_DeviceUpTime_Object = MibScalar
deviceUpTime = _DeviceUpTime_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 1, 11),
    _DeviceUpTime_Type()
)
deviceUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceUpTime.setStatus("current")
_DeviceFddActiveTime_Type = TimeTicks
_DeviceFddActiveTime_Object = MibScalar
deviceFddActiveTime = _DeviceFddActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 1, 12),
    _DeviceFddActiveTime_Type()
)
deviceFddActiveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceFddActiveTime.setStatus("current")
_DeviceFddPassiveTime_Type = TimeTicks
_DeviceFddPassiveTime_Object = MibScalar
deviceFddPassiveTime = _DeviceFddPassiveTime_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 1, 13),
    _DeviceFddPassiveTime_Type()
)
deviceFddPassiveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceFddPassiveTime.setStatus("current")


class _DeviceInventory_Type(DisplayString):
    """Custom type deviceInventory based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DeviceInventory_Type.__name__ = "DisplayString"
_DeviceInventory_Object = MibScalar
deviceInventory = _DeviceInventory_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 1, 14),
    _DeviceInventory_Type()
)
deviceInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceInventory.setStatus("current")
_Agent_ObjectIdentity = ObjectIdentity
agent = _Agent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 2)
)


class _AgentFirmware_Type(DisplayString):
    """Custom type agentFirmware based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AgentFirmware_Type.__name__ = "DisplayString"
_AgentFirmware_Object = MibScalar
agentFirmware = _AgentFirmware_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 2, 1),
    _AgentFirmware_Type()
)
agentFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentFirmware.setStatus("current")
_AgentMacAddress_Type = PhysAddress
_AgentMacAddress_Object = MibScalar
agentMacAddress = _AgentMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 2, 2),
    _AgentMacAddress_Type()
)
agentMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMacAddress.setStatus("current")


class _AgentIpMode_Type(Integer32):
    """Custom type agentIpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 2),
          ("static", 1),
          ("undefined", 254),
          ("unsupported", 255))
    )


_AgentIpMode_Type.__name__ = "Integer32"
_AgentIpMode_Object = MibScalar
agentIpMode = _AgentIpMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 2, 3),
    _AgentIpMode_Type()
)
agentIpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpMode.setStatus("current")
_AgentIpAddress_Type = IpAddress
_AgentIpAddress_Object = MibScalar
agentIpAddress = _AgentIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 2, 4),
    _AgentIpAddress_Type()
)
agentIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpAddress.setStatus("current")
_AgentSubnetMask_Type = IpAddress
_AgentSubnetMask_Object = MibScalar
agentSubnetMask = _AgentSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 2, 5),
    _AgentSubnetMask_Type()
)
agentSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSubnetMask.setStatus("current")
_AgentGateway_Type = IpAddress
_AgentGateway_Object = MibScalar
agentGateway = _AgentGateway_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 2, 6),
    _AgentGateway_Type()
)
agentGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentGateway.setStatus("current")


class _AgentConfigReset_Type(Integer32):
    """Custom type agentConfigReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normalOperation", 0),
          ("reset", 1))
    )


_AgentConfigReset_Type.__name__ = "Integer32"
_AgentConfigReset_Object = MibScalar
agentConfigReset = _AgentConfigReset_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 2, 7),
    _AgentConfigReset_Type()
)
agentConfigReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigReset.setStatus("current")


class _AgentConfigFactoryDefault_Type(Integer32):
    """Custom type agentConfigFactoryDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("factoryResetPerm", 2),
          ("factoryResetTemp", 1),
          ("normalOperation", 0))
    )


_AgentConfigFactoryDefault_Type.__name__ = "Integer32"
_AgentConfigFactoryDefault_Object = MibScalar
agentConfigFactoryDefault = _AgentConfigFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 2, 8),
    _AgentConfigFactoryDefault_Type()
)
agentConfigFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigFactoryDefault.setStatus("current")


class _AgentConfigEnableFactoryButton_Type(Integer32):
    """Custom type agentConfigEnableFactoryButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_AgentConfigEnableFactoryButton_Type.__name__ = "Integer32"
_AgentConfigEnableFactoryButton_Object = MibScalar
agentConfigEnableFactoryButton = _AgentConfigEnableFactoryButton_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 2, 9),
    _AgentConfigEnableFactoryButton_Type()
)
agentConfigEnableFactoryButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigEnableFactoryButton.setStatus("current")


class _AgentSecureAddressFlag_Type(Integer32):
    """Custom type agentSecureAddressFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("unsupported", 255),
          ("useNormal", 2),
          ("useSecure", 1))
    )


_AgentSecureAddressFlag_Type.__name__ = "Integer32"
_AgentSecureAddressFlag_Object = MibScalar
agentSecureAddressFlag = _AgentSecureAddressFlag_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 2, 10),
    _AgentSecureAddressFlag_Type()
)
agentSecureAddressFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSecureAddressFlag.setStatus("current")


class _AgentStorageMediaCardStatus_Type(Integer32):
    """Custom type agentStorageMediaCardStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("bootedFromCard", 4),
          ("bootedFromCardwithMac", 5),
          ("invalidCardDetected", 2),
          ("noCardInserted", 1),
          ("unsupported", 255),
          ("validCardDetected", 3))
    )


_AgentStorageMediaCardStatus_Type.__name__ = "Integer32"
_AgentStorageMediaCardStatus_Object = MibScalar
agentStorageMediaCardStatus = _AgentStorageMediaCardStatus_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 2, 11),
    _AgentStorageMediaCardStatus_Type()
)
agentStorageMediaCardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStorageMediaCardStatus.setStatus("current")


class _AgentStorageMediaCardBoot_Type(Integer32):
    """Custom type agentStorageMediaCardBoot based on Integer32"""
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
        *(("bootSmcPerm", 2),
          ("bootSmcTemp", 1),
          ("normalOperation", 0),
          ("unsupported", 255))
    )


_AgentStorageMediaCardBoot_Type.__name__ = "Integer32"
_AgentStorageMediaCardBoot_Object = MibScalar
agentStorageMediaCardBoot = _AgentStorageMediaCardBoot_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 2, 12),
    _AgentStorageMediaCardBoot_Type()
)
agentStorageMediaCardBoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStorageMediaCardBoot.setStatus("current")


class _AgentStorageMediaCardMac_Type(Integer32):
    """Custom type agentStorageMediaCardMac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("unsupported", 255),
          ("useMacFromSMC", 1),
          ("useOriginalMac", 2))
    )


_AgentStorageMediaCardMac_Type.__name__ = "Integer32"
_AgentStorageMediaCardMac_Object = MibScalar
agentStorageMediaCardMac = _AgentStorageMediaCardMac_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 2, 13),
    _AgentStorageMediaCardMac_Type()
)
agentStorageMediaCardMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStorageMediaCardMac.setStatus("current")


class _AgentStoreConfigToStorageMediaCard_Type(Integer32):
    """Custom type agentStoreConfigToStorageMediaCard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("normalOperation", 0),
          ("store", 1),
          ("unsupported", 255))
    )


_AgentStoreConfigToStorageMediaCard_Type.__name__ = "Integer32"
_AgentStoreConfigToStorageMediaCard_Object = MibScalar
agentStoreConfigToStorageMediaCard = _AgentStoreConfigToStorageMediaCard_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 2, 14),
    _AgentStoreConfigToStorageMediaCard_Type()
)
agentStoreConfigToStorageMediaCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStoreConfigToStorageMediaCard.setStatus("current")
_Port_ObjectIdentity = ObjectIdentity
port = _Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 3)
)
_PortCount_Type = Integer32
_PortCount_Object = MibScalar
portCount = _PortCount_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 3, 1),
    _PortCount_Type()
)
portCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCount.setStatus("current")
_PortStatusTable_Object = MibTable
portStatusTable = _PortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 3, 10)
)
if mibBuilder.loadTexts:
    portStatusTable.setStatus("current")
_PortStatusTableEntry_Object = MibTableRow
portStatusTableEntry = _PortStatusTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 3, 10, 1)
)
portStatusTableEntry.setIndexNames(
    (0, "MS-SWITCH30-MIB", "portStatusId"),
)
if mibBuilder.loadTexts:
    portStatusTableEntry.setStatus("current")


class _PortStatusId_Type(Integer32):
    """Custom type portStatusId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_PortStatusId_Type.__name__ = "Integer32"
_PortStatusId_Object = MibTableColumn
portStatusId = _PortStatusId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 3, 10, 1, 1),
    _PortStatusId_Type()
)
portStatusId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusId.setStatus("current")


class _PortStatusType_Type(Integer32):
    """Custom type portStatusType based on Integer32"""
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
              254)
        )
    )
    namedValues = NamedValues(
        *(("port-fx100", 3),
          ("port-fx100-1000-sfp", 4),
          ("port-t10-100-1000", 2),
          ("port-tx10-100", 1),
          ("port-tx10-100-1000-1x9", 7),
          ("port-tx10-100-1000-sfp", 6),
          ("port-x1000", 5),
          ("undefined", 254))
    )


_PortStatusType_Type.__name__ = "Integer32"
_PortStatusType_Object = MibTableColumn
portStatusType = _PortStatusType_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 3, 10, 1, 2),
    _PortStatusType_Type()
)
portStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusType.setStatus("current")


class _PortStatusLink_Type(Integer32):
    """Custom type portStatusLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("undefined", 254),
          ("up", 1))
    )


_PortStatusLink_Type.__name__ = "Integer32"
_PortStatusLink_Object = MibTableColumn
portStatusLink = _PortStatusLink_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 3, 10, 1, 3),
    _PortStatusLink_Type()
)
portStatusLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusLink.setStatus("current")


class _PortStatusSpeed_Type(Integer32):
    """Custom type portStatusSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              254)
        )
    )
    namedValues = NamedValues(
        *(("speed10", 1),
          ("speed100", 2),
          ("speed1000", 3),
          ("undefined", 254))
    )


_PortStatusSpeed_Type.__name__ = "Integer32"
_PortStatusSpeed_Object = MibTableColumn
portStatusSpeed = _PortStatusSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 3, 10, 1, 4),
    _PortStatusSpeed_Type()
)
portStatusSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusSpeed.setStatus("current")


class _PortStatusDuplex_Type(Integer32):
    """Custom type portStatusDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254)
        )
    )
    namedValues = NamedValues(
        *(("fullduplex", 2),
          ("halfduplex", 1),
          ("undefined", 254))
    )


_PortStatusDuplex_Type.__name__ = "Integer32"
_PortStatusDuplex_Object = MibTableColumn
portStatusDuplex = _PortStatusDuplex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 3, 10, 1, 5),
    _PortStatusDuplex_Type()
)
portStatusDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusDuplex.setStatus("current")


class _PortStatusFlowControl_Type(Integer32):
    """Custom type portStatusFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("undefined", 254),
          ("unsupported", 255))
    )


_PortStatusFlowControl_Type.__name__ = "Integer32"
_PortStatusFlowControl_Object = MibTableColumn
portStatusFlowControl = _PortStatusFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 3, 10, 1, 6),
    _PortStatusFlowControl_Type()
)
portStatusFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusFlowControl.setStatus("current")


class _PortStatusPinout_Type(Integer32):
    """Custom type portStatusPinout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("mdi", 1),
          ("mdix", 2),
          ("undefined", 254),
          ("unsupported", 255))
    )


_PortStatusPinout_Type.__name__ = "Integer32"
_PortStatusPinout_Object = MibTableColumn
portStatusPinout = _PortStatusPinout_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 3, 10, 1, 7),
    _PortStatusPinout_Type()
)
portStatusPinout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusPinout.setStatus("current")


class _PortStatusFarEndFault_Type(Integer32):
    """Custom type portStatusFarEndFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("detected", 1),
          ("undefined", 254),
          ("undetected", 2),
          ("unsupported", 255))
    )


_PortStatusFarEndFault_Type.__name__ = "Integer32"
_PortStatusFarEndFault_Object = MibTableColumn
portStatusFarEndFault = _PortStatusFarEndFault_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 3, 10, 1, 8),
    _PortStatusFarEndFault_Type()
)
portStatusFarEndFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusFarEndFault.setStatus("current")


class _PortStatusRxNetload_Type(Integer32):
    """Custom type portStatusRxNetload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_PortStatusRxNetload_Type.__name__ = "Integer32"
_PortStatusRxNetload_Object = MibTableColumn
portStatusRxNetload = _PortStatusRxNetload_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 3, 10, 1, 9),
    _PortStatusRxNetload_Type()
)
portStatusRxNetload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusRxNetload.setStatus("current")


class _PortStatusTxNetload_Type(Integer32):
    """Custom type portStatusTxNetload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_PortStatusTxNetload_Type.__name__ = "Integer32"
_PortStatusTxNetload_Object = MibTableColumn
portStatusTxNetload = _PortStatusTxNetload_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 3, 10, 1, 10),
    _PortStatusTxNetload_Type()
)
portStatusTxNetload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusTxNetload.setStatus("current")
_PortConfigTable_Object = MibTable
portConfigTable = _PortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 3, 20)
)
if mibBuilder.loadTexts:
    portConfigTable.setStatus("current")
_PortConfigTableEntry_Object = MibTableRow
portConfigTableEntry = _PortConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 3, 20, 1)
)
portConfigTableEntry.setIndexNames(
    (0, "MS-SWITCH30-MIB", "portConfigId"),
)
if mibBuilder.loadTexts:
    portConfigTableEntry.setStatus("current")


class _PortConfigId_Type(Integer32):
    """Custom type portConfigId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_PortConfigId_Type.__name__ = "Integer32"
_PortConfigId_Object = MibTableColumn
portConfigId = _PortConfigId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 3, 20, 1, 1),
    _PortConfigId_Type()
)
portConfigId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portConfigId.setStatus("current")


class _PortConfigAlias_Type(DisplayString):
    """Custom type portConfigAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_PortConfigAlias_Type.__name__ = "DisplayString"
_PortConfigAlias_Object = MibTableColumn
portConfigAlias = _PortConfigAlias_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 3, 20, 1, 2),
    _PortConfigAlias_Type()
)
portConfigAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigAlias.setStatus("current")


class _PortConfigEnable_Type(Integer32):
    """Custom type portConfigEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("undefined", 254),
          ("unsupported", 255))
    )


_PortConfigEnable_Type.__name__ = "Integer32"
_PortConfigEnable_Object = MibTableColumn
portConfigEnable = _PortConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 3, 20, 1, 3),
    _PortConfigEnable_Type()
)
portConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigEnable.setStatus("current")


class _PortConfigAutonego_Type(Integer32):
    """Custom type portConfigAutonego based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("undefined", 254),
          ("unsupported", 255))
    )


_PortConfigAutonego_Type.__name__ = "Integer32"
_PortConfigAutonego_Object = MibTableColumn
portConfigAutonego = _PortConfigAutonego_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 3, 20, 1, 4),
    _PortConfigAutonego_Type()
)
portConfigAutonego.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigAutonego.setStatus("current")


class _PortConfigSpeed_Type(Integer32):
    """Custom type portConfigSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("force10", 1),
          ("force100", 2),
          ("force1000", 3),
          ("undefined", 254),
          ("unsupported", 255))
    )


_PortConfigSpeed_Type.__name__ = "Integer32"
_PortConfigSpeed_Object = MibTableColumn
portConfigSpeed = _PortConfigSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 3, 20, 1, 5),
    _PortConfigSpeed_Type()
)
portConfigSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigSpeed.setStatus("current")


class _PortConfigDuplex_Type(Integer32):
    """Custom type portConfigDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("forcefull", 2),
          ("forcehalf", 1),
          ("undefined", 254),
          ("unsupported", 255))
    )


_PortConfigDuplex_Type.__name__ = "Integer32"
_PortConfigDuplex_Object = MibTableColumn
portConfigDuplex = _PortConfigDuplex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 3, 20, 1, 6),
    _PortConfigDuplex_Type()
)
portConfigDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigDuplex.setStatus("current")


class _PortConfigFlowControl_Type(Integer32):
    """Custom type portConfigFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("advertise", 1),
          ("avoid", 2),
          ("undefined", 254),
          ("unsupported", 255))
    )


_PortConfigFlowControl_Type.__name__ = "Integer32"
_PortConfigFlowControl_Object = MibTableColumn
portConfigFlowControl = _PortConfigFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 3, 20, 1, 7),
    _PortConfigFlowControl_Type()
)
portConfigFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigFlowControl.setStatus("current")


class _PortConfigPinout_Type(Integer32):
    """Custom type portConfigPinout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("mdi", 1),
          ("mdix", 2),
          ("undefined", 254),
          ("unsupported", 255))
    )


_PortConfigPinout_Type.__name__ = "Integer32"
_PortConfigPinout_Object = MibTableColumn
portConfigPinout = _PortConfigPinout_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 3, 20, 1, 8),
    _PortConfigPinout_Type()
)
portConfigPinout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigPinout.setStatus("current")


class _PortConfigFarEndFault_Type(Integer32):
    """Custom type portConfigFarEndFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disalbed", 2),
          ("enabled", 1),
          ("undefined", 254),
          ("unsupported", 255))
    )


_PortConfigFarEndFault_Type.__name__ = "Integer32"
_PortConfigFarEndFault_Object = MibTableColumn
portConfigFarEndFault = _PortConfigFarEndFault_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 3, 20, 1, 9),
    _PortConfigFarEndFault_Type()
)
portConfigFarEndFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigFarEndFault.setStatus("current")


class _PortConfigAdvertise_Type(Integer32):
    """Custom type portConfigAdvertise based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("advertiseGigabit", 1),
          ("avoidGigabit", 2),
          ("undefined", 254),
          ("unsupported", 255))
    )


_PortConfigAdvertise_Type.__name__ = "Integer32"
_PortConfigAdvertise_Object = MibTableColumn
portConfigAdvertise = _PortConfigAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 3, 20, 1, 10),
    _PortConfigAdvertise_Type()
)
portConfigAdvertise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigAdvertise.setStatus("current")


class _PortConfigFibreDownDetection_Type(Integer32):
    """Custom type portConfigFibreDownDetection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disalbed", 2),
          ("enabled", 1),
          ("undefined", 254),
          ("unsupported", 255))
    )


_PortConfigFibreDownDetection_Type.__name__ = "Integer32"
_PortConfigFibreDownDetection_Object = MibTableColumn
portConfigFibreDownDetection = _PortConfigFibreDownDetection_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 3, 20, 1, 11),
    _PortConfigFibreDownDetection_Type()
)
portConfigFibreDownDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigFibreDownDetection.setStatus("current")
_Vlan_ObjectIdentity = ObjectIdentity
vlan = _Vlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4)
)


class _VlanSupport_Type(Integer32):
    """Custom type vlanSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notsupported", 255),
          ("supported", 1))
    )


_VlanSupport_Type.__name__ = "Integer32"
_VlanSupport_Object = MibScalar
vlanSupport = _VlanSupport_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 1),
    _VlanSupport_Type()
)
vlanSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSupport.setStatus("current")


class _VlanEnable_Type(Integer32):
    """Custom type vlanEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("undefined", 254),
          ("unsupported", 255))
    )


_VlanEnable_Type.__name__ = "Integer32"
_VlanEnable_Object = MibScalar
vlanEnable = _VlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 2),
    _VlanEnable_Type()
)
vlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanEnable.setStatus("current")


class _VlanForceDefaultVID_Type(Integer32):
    """Custom type vlanForceDefaultVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("perport", 3),
          ("unsupported", 255))
    )


_VlanForceDefaultVID_Type.__name__ = "Integer32"
_VlanForceDefaultVID_Object = MibScalar
vlanForceDefaultVID = _VlanForceDefaultVID_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 3),
    _VlanForceDefaultVID_Type()
)
vlanForceDefaultVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanForceDefaultVID.setStatus("current")
_VlanFilterCount_Type = Integer32
_VlanFilterCount_Object = MibScalar
vlanFilterCount = _VlanFilterCount_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 4),
    _VlanFilterCount_Type()
)
vlanFilterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanFilterCount.setStatus("current")


class _VlanVoiceVID_Type(Integer32):
    """Custom type vlanVoiceVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_VlanVoiceVID_Type.__name__ = "Integer32"
_VlanVoiceVID_Object = MibScalar
vlanVoiceVID = _VlanVoiceVID_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 5),
    _VlanVoiceVID_Type()
)
vlanVoiceVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanVoiceVID.setStatus("current")


class _VlanRstpVID_Type(Integer32):
    """Custom type vlanRstpVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_VlanRstpVID_Type.__name__ = "Integer32"
_VlanRstpVID_Object = MibScalar
vlanRstpVID = _VlanRstpVID_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 6),
    _VlanRstpVID_Type()
)
vlanRstpVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanRstpVID.setStatus("current")


class _VlanUnauthVID_Type(Integer32):
    """Custom type vlanUnauthVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_VlanUnauthVID_Type.__name__ = "Integer32"
_VlanUnauthVID_Object = MibScalar
vlanUnauthVID = _VlanUnauthVID_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 7),
    _VlanUnauthVID_Type()
)
vlanUnauthVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanUnauthVID.setStatus("current")
_VlanPortTable_Object = MibTable
vlanPortTable = _VlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 10)
)
if mibBuilder.loadTexts:
    vlanPortTable.setStatus("current")
_VlanPortTableEntry_Object = MibTableRow
vlanPortTableEntry = _VlanPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 10, 1)
)
vlanPortTableEntry.setIndexNames(
    (0, "MS-SWITCH30-MIB", "vlanPortId"),
)
if mibBuilder.loadTexts:
    vlanPortTableEntry.setStatus("current")


class _VlanPortId_Type(Integer32):
    """Custom type vlanPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_VlanPortId_Type.__name__ = "Integer32"
_VlanPortId_Object = MibTableColumn
vlanPortId = _VlanPortId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 10, 1, 1),
    _VlanPortId_Type()
)
vlanPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPortId.setStatus("current")


class _VlanPortMode_Type(Integer32):
    """Custom type vlanPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("access", 1),
          ("hybrid", 3),
          ("trunk", 2),
          ("undefined", 254),
          ("unsupported", 255))
    )


_VlanPortMode_Type.__name__ = "Integer32"
_VlanPortMode_Object = MibTableColumn
vlanPortMode = _VlanPortMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 10, 1, 2),
    _VlanPortMode_Type()
)
vlanPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPortMode.setStatus("current")


class _VlanDefaultVID_Type(Integer32):
    """Custom type vlanDefaultVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_VlanDefaultVID_Type.__name__ = "Integer32"
_VlanDefaultVID_Object = MibTableColumn
vlanDefaultVID = _VlanDefaultVID_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 10, 1, 3),
    _VlanDefaultVID_Type()
)
vlanDefaultVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanDefaultVID.setStatus("current")


class _VlanDefaultPriority_Type(Integer32):
    """Custom type vlanDefaultPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VlanDefaultPriority_Type.__name__ = "Integer32"
_VlanDefaultPriority_Object = MibTableColumn
vlanDefaultPriority = _VlanDefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 10, 1, 4),
    _VlanDefaultPriority_Type()
)
vlanDefaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanDefaultPriority.setStatus("current")


class _VlanPortFlags_Type(Integer32):
    """Custom type vlanPortFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_VlanPortFlags_Type.__name__ = "Integer32"
_VlanPortFlags_Object = MibTableColumn
vlanPortFlags = _VlanPortFlags_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 10, 1, 5),
    _VlanPortFlags_Type()
)
vlanPortFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPortFlags.setStatus("current")
_VlanFilterTable_Object = MibTable
vlanFilterTable = _VlanFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 20)
)
if mibBuilder.loadTexts:
    vlanFilterTable.setStatus("current")
_VlanFilterTableEntry_Object = MibTableRow
vlanFilterTableEntry = _VlanFilterTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 20, 1)
)
vlanFilterTableEntry.setIndexNames(
    (0, "MS-SWITCH30-MIB", "vlanFilterId"),
)
if mibBuilder.loadTexts:
    vlanFilterTableEntry.setStatus("current")


class _VlanFilterId_Type(Integer32):
    """Custom type vlanFilterId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_VlanFilterId_Type.__name__ = "Integer32"
_VlanFilterId_Object = MibTableColumn
vlanFilterId = _VlanFilterId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 20, 1, 1),
    _VlanFilterId_Type()
)
vlanFilterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanFilterId.setStatus("current")


class _VlanFilterVID_Type(Integer32):
    """Custom type vlanFilterVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_VlanFilterVID_Type.__name__ = "Integer32"
_VlanFilterVID_Object = MibTableColumn
vlanFilterVID = _VlanFilterVID_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 20, 1, 2),
    _VlanFilterVID_Type()
)
vlanFilterVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanFilterVID.setStatus("current")


class _VlanFilterAlias_Type(DisplayString):
    """Custom type vlanFilterAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VlanFilterAlias_Type.__name__ = "DisplayString"
_VlanFilterAlias_Object = MibTableColumn
vlanFilterAlias = _VlanFilterAlias_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 20, 1, 3),
    _VlanFilterAlias_Type()
)
vlanFilterAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanFilterAlias.setStatus("current")


class _VlanFilterEnable_Type(Integer32):
    """Custom type vlanFilterEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_VlanFilterEnable_Type.__name__ = "Integer32"
_VlanFilterEnable_Object = MibTableColumn
vlanFilterEnable = _VlanFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 20, 1, 4),
    _VlanFilterEnable_Type()
)
vlanFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanFilterEnable.setStatus("current")


class _VlanMemberManager_Type(Integer32):
    """Custom type vlanMemberManager based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_VlanMemberManager_Type.__name__ = "Integer32"
_VlanMemberManager_Object = MibTableColumn
vlanMemberManager = _VlanMemberManager_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 20, 1, 5),
    _VlanMemberManager_Type()
)
vlanMemberManager.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMemberManager.setStatus("current")


class _VlanMemberPort1_Type(Integer32):
    """Custom type vlanMemberPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_VlanMemberPort1_Type.__name__ = "Integer32"
_VlanMemberPort1_Object = MibTableColumn
vlanMemberPort1 = _VlanMemberPort1_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 20, 1, 6),
    _VlanMemberPort1_Type()
)
vlanMemberPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMemberPort1.setStatus("current")


class _VlanMemberPort2_Type(Integer32):
    """Custom type vlanMemberPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_VlanMemberPort2_Type.__name__ = "Integer32"
_VlanMemberPort2_Object = MibTableColumn
vlanMemberPort2 = _VlanMemberPort2_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 20, 1, 7),
    _VlanMemberPort2_Type()
)
vlanMemberPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMemberPort2.setStatus("current")


class _VlanMemberPort3_Type(Integer32):
    """Custom type vlanMemberPort3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_VlanMemberPort3_Type.__name__ = "Integer32"
_VlanMemberPort3_Object = MibTableColumn
vlanMemberPort3 = _VlanMemberPort3_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 20, 1, 8),
    _VlanMemberPort3_Type()
)
vlanMemberPort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMemberPort3.setStatus("current")


class _VlanMemberPort4_Type(Integer32):
    """Custom type vlanMemberPort4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_VlanMemberPort4_Type.__name__ = "Integer32"
_VlanMemberPort4_Object = MibTableColumn
vlanMemberPort4 = _VlanMemberPort4_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 20, 1, 9),
    _VlanMemberPort4_Type()
)
vlanMemberPort4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMemberPort4.setStatus("current")


class _VlanMemberPort5_Type(Integer32):
    """Custom type vlanMemberPort5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_VlanMemberPort5_Type.__name__ = "Integer32"
_VlanMemberPort5_Object = MibTableColumn
vlanMemberPort5 = _VlanMemberPort5_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 20, 1, 10),
    _VlanMemberPort5_Type()
)
vlanMemberPort5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMemberPort5.setStatus("current")


class _VlanMemberPort6_Type(Integer32):
    """Custom type vlanMemberPort6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_VlanMemberPort6_Type.__name__ = "Integer32"
_VlanMemberPort6_Object = MibTableColumn
vlanMemberPort6 = _VlanMemberPort6_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 20, 1, 11),
    _VlanMemberPort6_Type()
)
vlanMemberPort6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMemberPort6.setStatus("current")


class _VlanMemberPort7_Type(Integer32):
    """Custom type vlanMemberPort7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_VlanMemberPort7_Type.__name__ = "Integer32"
_VlanMemberPort7_Object = MibTableColumn
vlanMemberPort7 = _VlanMemberPort7_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 20, 1, 12),
    _VlanMemberPort7_Type()
)
vlanMemberPort7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMemberPort7.setStatus("current")


class _VlanMemberPort8_Type(Integer32):
    """Custom type vlanMemberPort8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_VlanMemberPort8_Type.__name__ = "Integer32"
_VlanMemberPort8_Object = MibTableColumn
vlanMemberPort8 = _VlanMemberPort8_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 20, 1, 13),
    _VlanMemberPort8_Type()
)
vlanMemberPort8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMemberPort8.setStatus("current")


class _VlanMemberPort9_Type(Integer32):
    """Custom type vlanMemberPort9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_VlanMemberPort9_Type.__name__ = "Integer32"
_VlanMemberPort9_Object = MibTableColumn
vlanMemberPort9 = _VlanMemberPort9_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 20, 1, 14),
    _VlanMemberPort9_Type()
)
vlanMemberPort9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMemberPort9.setStatus("current")


class _VlanMemberPort10_Type(Integer32):
    """Custom type vlanMemberPort10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_VlanMemberPort10_Type.__name__ = "Integer32"
_VlanMemberPort10_Object = MibTableColumn
vlanMemberPort10 = _VlanMemberPort10_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 20, 1, 15),
    _VlanMemberPort10_Type()
)
vlanMemberPort10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMemberPort10.setStatus("current")


class _VlanMemberPort11_Type(Integer32):
    """Custom type vlanMemberPort11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_VlanMemberPort11_Type.__name__ = "Integer32"
_VlanMemberPort11_Object = MibTableColumn
vlanMemberPort11 = _VlanMemberPort11_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 20, 1, 16),
    _VlanMemberPort11_Type()
)
vlanMemberPort11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMemberPort11.setStatus("current")


class _VlanMemberPort12_Type(Integer32):
    """Custom type vlanMemberPort12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_VlanMemberPort12_Type.__name__ = "Integer32"
_VlanMemberPort12_Object = MibTableColumn
vlanMemberPort12 = _VlanMemberPort12_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 20, 1, 17),
    _VlanMemberPort12_Type()
)
vlanMemberPort12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMemberPort12.setStatus("current")


class _VlanMemberPort13_Type(Integer32):
    """Custom type vlanMemberPort13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_VlanMemberPort13_Type.__name__ = "Integer32"
_VlanMemberPort13_Object = MibTableColumn
vlanMemberPort13 = _VlanMemberPort13_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 20, 1, 18),
    _VlanMemberPort13_Type()
)
vlanMemberPort13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMemberPort13.setStatus("current")


class _VlanMemberPort14_Type(Integer32):
    """Custom type vlanMemberPort14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_VlanMemberPort14_Type.__name__ = "Integer32"
_VlanMemberPort14_Object = MibTableColumn
vlanMemberPort14 = _VlanMemberPort14_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 20, 1, 19),
    _VlanMemberPort14_Type()
)
vlanMemberPort14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMemberPort14.setStatus("current")


class _VlanMemberPort15_Type(Integer32):
    """Custom type vlanMemberPort15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_VlanMemberPort15_Type.__name__ = "Integer32"
_VlanMemberPort15_Object = MibTableColumn
vlanMemberPort15 = _VlanMemberPort15_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 20, 1, 20),
    _VlanMemberPort15_Type()
)
vlanMemberPort15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMemberPort15.setStatus("current")


class _VlanMemberPort16_Type(Integer32):
    """Custom type vlanMemberPort16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_VlanMemberPort16_Type.__name__ = "Integer32"
_VlanMemberPort16_Object = MibTableColumn
vlanMemberPort16 = _VlanMemberPort16_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 20, 1, 21),
    _VlanMemberPort16_Type()
)
vlanMemberPort16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMemberPort16.setStatus("current")


class _VlanMemberPort17_Type(Integer32):
    """Custom type vlanMemberPort17 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_VlanMemberPort17_Type.__name__ = "Integer32"
_VlanMemberPort17_Object = MibTableColumn
vlanMemberPort17 = _VlanMemberPort17_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 20, 1, 22),
    _VlanMemberPort17_Type()
)
vlanMemberPort17.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMemberPort17.setStatus("current")


class _VlanMemberPort18_Type(Integer32):
    """Custom type vlanMemberPort18 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_VlanMemberPort18_Type.__name__ = "Integer32"
_VlanMemberPort18_Object = MibTableColumn
vlanMemberPort18 = _VlanMemberPort18_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 20, 1, 23),
    _VlanMemberPort18_Type()
)
vlanMemberPort18.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMemberPort18.setStatus("current")


class _VlanMemberPort19_Type(Integer32):
    """Custom type vlanMemberPort19 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_VlanMemberPort19_Type.__name__ = "Integer32"
_VlanMemberPort19_Object = MibTableColumn
vlanMemberPort19 = _VlanMemberPort19_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 20, 1, 24),
    _VlanMemberPort19_Type()
)
vlanMemberPort19.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMemberPort19.setStatus("current")


class _VlanMemberPort20_Type(Integer32):
    """Custom type vlanMemberPort20 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_VlanMemberPort20_Type.__name__ = "Integer32"
_VlanMemberPort20_Object = MibTableColumn
vlanMemberPort20 = _VlanMemberPort20_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 20, 1, 25),
    _VlanMemberPort20_Type()
)
vlanMemberPort20.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMemberPort20.setStatus("current")


class _VlanMemberPort21_Type(Integer32):
    """Custom type vlanMemberPort21 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_VlanMemberPort21_Type.__name__ = "Integer32"
_VlanMemberPort21_Object = MibTableColumn
vlanMemberPort21 = _VlanMemberPort21_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 20, 1, 26),
    _VlanMemberPort21_Type()
)
vlanMemberPort21.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMemberPort21.setStatus("current")


class _VlanMemberPort22_Type(Integer32):
    """Custom type vlanMemberPort22 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_VlanMemberPort22_Type.__name__ = "Integer32"
_VlanMemberPort22_Object = MibTableColumn
vlanMemberPort22 = _VlanMemberPort22_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 20, 1, 27),
    _VlanMemberPort22_Type()
)
vlanMemberPort22.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMemberPort22.setStatus("current")


class _VlanMemberPort23_Type(Integer32):
    """Custom type vlanMemberPort23 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_VlanMemberPort23_Type.__name__ = "Integer32"
_VlanMemberPort23_Object = MibTableColumn
vlanMemberPort23 = _VlanMemberPort23_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 20, 1, 28),
    _VlanMemberPort23_Type()
)
vlanMemberPort23.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMemberPort23.setStatus("current")


class _VlanMemberPort24_Type(Integer32):
    """Custom type vlanMemberPort24 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_VlanMemberPort24_Type.__name__ = "Integer32"
_VlanMemberPort24_Object = MibTableColumn
vlanMemberPort24 = _VlanMemberPort24_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 20, 1, 29),
    _VlanMemberPort24_Type()
)
vlanMemberPort24.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMemberPort24.setStatus("current")
_VlanFilterEnhTable_Object = MibTable
vlanFilterEnhTable = _VlanFilterEnhTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 30)
)
if mibBuilder.loadTexts:
    vlanFilterEnhTable.setStatus("current")
_VlanFilterEnhTableEntry_Object = MibTableRow
vlanFilterEnhTableEntry = _VlanFilterEnhTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 30, 1)
)
vlanFilterEnhTableEntry.setIndexNames(
    (0, "MS-SWITCH30-MIB", "vlanFilterEnhId"),
)
if mibBuilder.loadTexts:
    vlanFilterEnhTableEntry.setStatus("current")


class _VlanFilterEnhId_Type(Integer32):
    """Custom type vlanFilterEnhId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_VlanFilterEnhId_Type.__name__ = "Integer32"
_VlanFilterEnhId_Object = MibTableColumn
vlanFilterEnhId = _VlanFilterEnhId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 30, 1, 1),
    _VlanFilterEnhId_Type()
)
vlanFilterEnhId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanFilterEnhId.setStatus("current")


class _VlanFilterEnhFlags_Type(Integer32):
    """Custom type vlanFilterEnhFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_VlanFilterEnhFlags_Type.__name__ = "Integer32"
_VlanFilterEnhFlags_Object = MibTableColumn
vlanFilterEnhFlags = _VlanFilterEnhFlags_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 30, 1, 2),
    _VlanFilterEnhFlags_Type()
)
vlanFilterEnhFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanFilterEnhFlags.setStatus("current")


class _VlanFilterEnhPriOverride_Type(Integer32):
    """Custom type vlanFilterEnhPriOverride based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VlanFilterEnhPriOverride_Type.__name__ = "Integer32"
_VlanFilterEnhPriOverride_Object = MibTableColumn
vlanFilterEnhPriOverride = _VlanFilterEnhPriOverride_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 4, 30, 1, 3),
    _VlanFilterEnhPriOverride_Type()
)
vlanFilterEnhPriOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanFilterEnhPriOverride.setStatus("current")
_Prioritization_ObjectIdentity = ObjectIdentity
prioritization = _Prioritization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 5)
)


class _PrioSupport_Type(Integer32):
    """Custom type prioSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 255))
    )


_PrioSupport_Type.__name__ = "Integer32"
_PrioSupport_Object = MibScalar
prioSupport = _PrioSupport_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 5, 1),
    _PrioSupport_Type()
)
prioSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prioSupport.setStatus("current")
_PrioQueueCount_Type = Integer32
_PrioQueueCount_Object = MibScalar
prioQueueCount = _PrioQueueCount_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 5, 2),
    _PrioQueueCount_Type()
)
prioQueueCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prioQueueCount.setStatus("current")


class _PrioQueueScheme_Type(Integer32):
    """Custom type prioQueueScheme based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 2),
          ("unsupported", 255),
          ("weighted", 1))
    )


_PrioQueueScheme_Type.__name__ = "Integer32"
_PrioQueueScheme_Object = MibScalar
prioQueueScheme = _PrioQueueScheme_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 5, 3),
    _PrioQueueScheme_Type()
)
prioQueueScheme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioQueueScheme.setStatus("current")


class _PrioPortEnable_Type(Integer32):
    """Custom type prioPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_PrioPortEnable_Type.__name__ = "Integer32"
_PrioPortEnable_Object = MibScalar
prioPortEnable = _PrioPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 5, 4),
    _PrioPortEnable_Type()
)
prioPortEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prioPortEnable.setStatus("current")


class _PrioIeeeTagEnable_Type(Integer32):
    """Custom type prioIeeeTagEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_PrioIeeeTagEnable_Type.__name__ = "Integer32"
_PrioIeeeTagEnable_Object = MibScalar
prioIeeeTagEnable = _PrioIeeeTagEnable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 5, 5),
    _PrioIeeeTagEnable_Type()
)
prioIeeeTagEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioIeeeTagEnable.setStatus("current")


class _PrioDiffservEnable_Type(Integer32):
    """Custom type prioDiffservEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_PrioDiffservEnable_Type.__name__ = "Integer32"
_PrioDiffservEnable_Object = MibScalar
prioDiffservEnable = _PrioDiffservEnable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 5, 6),
    _PrioDiffservEnable_Type()
)
prioDiffservEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioDiffservEnable.setStatus("current")
_PrioPortTable_Object = MibTable
prioPortTable = _PrioPortTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 5, 10)
)
if mibBuilder.loadTexts:
    prioPortTable.setStatus("current")
_PrioPortTableEntry_Object = MibTableRow
prioPortTableEntry = _PrioPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 5, 10, 1)
)
prioPortTableEntry.setIndexNames(
    (0, "MS-SWITCH30-MIB", "prioPortId"),
)
if mibBuilder.loadTexts:
    prioPortTableEntry.setStatus("current")


class _PrioPortId_Type(Integer32):
    """Custom type prioPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_PrioPortId_Type.__name__ = "Integer32"
_PrioPortId_Object = MibTableColumn
prioPortId = _PrioPortId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 5, 10, 1, 1),
    _PrioPortId_Type()
)
prioPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prioPortId.setStatus("current")


class _PrioPortQueue_Type(Integer32):
    """Custom type prioPortQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_PrioPortQueue_Type.__name__ = "Integer32"
_PrioPortQueue_Object = MibTableColumn
prioPortQueue = _PrioPortQueue_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 5, 10, 1, 2),
    _PrioPortQueue_Type()
)
prioPortQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioPortQueue.setStatus("current")
_PrioIeeeTagTable_Object = MibTable
prioIeeeTagTable = _PrioIeeeTagTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 5, 20)
)
if mibBuilder.loadTexts:
    prioIeeeTagTable.setStatus("current")
_PrioIeeeTagTableEntry_Object = MibTableRow
prioIeeeTagTableEntry = _PrioIeeeTagTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 5, 20, 1)
)
prioIeeeTagTableEntry.setIndexNames(
    (0, "MS-SWITCH30-MIB", "prioIeeeTagId"),
)
if mibBuilder.loadTexts:
    prioIeeeTagTableEntry.setStatus("current")


class _PrioIeeeTagId_Type(Integer32):
    """Custom type prioIeeeTagId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PrioIeeeTagId_Type.__name__ = "Integer32"
_PrioIeeeTagId_Object = MibTableColumn
prioIeeeTagId = _PrioIeeeTagId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 5, 20, 1, 1),
    _PrioIeeeTagId_Type()
)
prioIeeeTagId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prioIeeeTagId.setStatus("current")
_PrioIeeeTagQueue_Type = Integer32
_PrioIeeeTagQueue_Object = MibTableColumn
prioIeeeTagQueue = _PrioIeeeTagQueue_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 5, 20, 1, 2),
    _PrioIeeeTagQueue_Type()
)
prioIeeeTagQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioIeeeTagQueue.setStatus("current")
_PrioDiffservTable_Object = MibTable
prioDiffservTable = _PrioDiffservTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 5, 30)
)
if mibBuilder.loadTexts:
    prioDiffservTable.setStatus("current")
_PrioDiffservTableEntry_Object = MibTableRow
prioDiffservTableEntry = _PrioDiffservTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 5, 30, 1)
)
prioDiffservTableEntry.setIndexNames(
    (0, "MS-SWITCH30-MIB", "prioDiffservId"),
)
if mibBuilder.loadTexts:
    prioDiffservTableEntry.setStatus("current")


class _PrioDiffservId_Type(Integer32):
    """Custom type prioDiffservId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_PrioDiffservId_Type.__name__ = "Integer32"
_PrioDiffservId_Object = MibTableColumn
prioDiffservId = _PrioDiffservId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 5, 30, 1, 1),
    _PrioDiffservId_Type()
)
prioDiffservId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prioDiffservId.setStatus("current")
_PrioDiffservQueue_Type = Integer32
_PrioDiffservQueue_Object = MibTableColumn
prioDiffservQueue = _PrioDiffservQueue_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 5, 30, 1, 2),
    _PrioDiffservQueue_Type()
)
prioDiffservQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioDiffservQueue.setStatus("current")
_Monitor_ObjectIdentity = ObjectIdentity
monitor = _Monitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 6)
)


class _MonitorSupport_Type(Integer32):
    """Custom type monitorSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 255))
    )


_MonitorSupport_Type.__name__ = "Integer32"
_MonitorSupport_Object = MibScalar
monitorSupport = _MonitorSupport_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 6, 1),
    _MonitorSupport_Type()
)
monitorSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorSupport.setStatus("current")


class _MonitorMode_Type(Integer32):
    """Custom type monitorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("both", 2),
          ("disabled", 3),
          ("hubmode", 4),
          ("txonly", 1),
          ("unsupported", 255))
    )


_MonitorMode_Type.__name__ = "Integer32"
_MonitorMode_Object = MibScalar
monitorMode = _MonitorMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 6, 2),
    _MonitorMode_Type()
)
monitorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorMode.setStatus("current")


class _MonitorSource_Type(Integer32):
    """Custom type monitorSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_MonitorSource_Type.__name__ = "Integer32"
_MonitorSource_Object = MibScalar
monitorSource = _MonitorSource_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 6, 3),
    _MonitorSource_Type()
)
monitorSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorSource.setStatus("current")


class _MonitorDestination_Type(Integer32):
    """Custom type monitorDestination based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_MonitorDestination_Type.__name__ = "Integer32"
_MonitorDestination_Object = MibScalar
monitorDestination = _MonitorDestination_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 6, 4),
    _MonitorDestination_Type()
)
monitorDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorDestination.setStatus("current")
_Ring_ObjectIdentity = ObjectIdentity
ring = _Ring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 7)
)


class _RingSupport_Type(Integer32):
    """Custom type ringSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 255))
    )


_RingSupport_Type.__name__ = "Integer32"
_RingSupport_Object = MibScalar
ringSupport = _RingSupport_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 7, 1),
    _RingSupport_Type()
)
ringSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringSupport.setStatus("current")
_RingCount_Type = Integer32
_RingCount_Object = MibScalar
ringCount = _RingCount_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 7, 2),
    _RingCount_Type()
)
ringCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringCount.setStatus("current")
_RingTable_Object = MibTable
ringTable = _RingTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 7, 10)
)
if mibBuilder.loadTexts:
    ringTable.setStatus("current")
_RingTableEntry_Object = MibTableRow
ringTableEntry = _RingTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 7, 10, 1)
)
ringTableEntry.setIndexNames(
    (0, "MS-SWITCH30-MIB", "ringId"),
)
if mibBuilder.loadTexts:
    ringTableEntry.setStatus("current")


class _RingId_Type(Integer32):
    """Custom type ringId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_RingId_Type.__name__ = "Integer32"
_RingId_Object = MibTableColumn
ringId = _RingId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 7, 10, 1, 1),
    _RingId_Type()
)
ringId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringId.setStatus("current")


class _RingMode_Type(Integer32):
    """Custom type ringMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("master", 2),
          ("slave", 1),
          ("unsupported", 255))
    )


_RingMode_Type.__name__ = "Integer32"
_RingMode_Object = MibTableColumn
ringMode = _RingMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 7, 10, 1, 2),
    _RingMode_Type()
)
ringMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringMode.setStatus("current")


class _RingPortA_Type(Integer32):
    """Custom type ringPortA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_RingPortA_Type.__name__ = "Integer32"
_RingPortA_Object = MibTableColumn
ringPortA = _RingPortA_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 7, 10, 1, 3),
    _RingPortA_Type()
)
ringPortA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringPortA.setStatus("current")


class _RingPortB_Type(Integer32):
    """Custom type ringPortB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_RingPortB_Type.__name__ = "Integer32"
_RingPortB_Object = MibTableColumn
ringPortB = _RingPortB_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 7, 10, 1, 4),
    _RingPortB_Type()
)
ringPortB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringPortB.setStatus("current")


class _RingNumber_Type(Integer32):
    """Custom type ringNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RingNumber_Type.__name__ = "Integer32"
_RingNumber_Object = MibTableColumn
ringNumber = _RingNumber_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 7, 10, 1, 5),
    _RingNumber_Type()
)
ringNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringNumber.setStatus("current")


class _RingStatus_Type(Integer32):
    """Custom type ringStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ringDisabled", 3),
          ("ringFailure", 2),
          ("ringOk", 1),
          ("unsupported", 255))
    )


_RingStatus_Type.__name__ = "Integer32"
_RingStatus_Object = MibTableColumn
ringStatus = _RingStatus_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 7, 10, 1, 6),
    _RingStatus_Type()
)
ringStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStatus.setStatus("current")
_RingAlarmDuration_Type = TimeTicks
_RingAlarmDuration_Object = MibTableColumn
ringAlarmDuration = _RingAlarmDuration_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 7, 10, 1, 7),
    _RingAlarmDuration_Type()
)
ringAlarmDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringAlarmDuration.setStatus("current")
_Couplingred_ObjectIdentity = ObjectIdentity
couplingred = _Couplingred_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 8)
)


class _CouplingredSupport_Type(Integer32):
    """Custom type couplingredSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 255))
    )


_CouplingredSupport_Type.__name__ = "Integer32"
_CouplingredSupport_Object = MibScalar
couplingredSupport = _CouplingredSupport_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 8, 1),
    _CouplingredSupport_Type()
)
couplingredSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    couplingredSupport.setStatus("current")


class _CouplingredPort_Type(Integer32):
    """Custom type couplingredPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_CouplingredPort_Type.__name__ = "Integer32"
_CouplingredPort_Object = MibScalar
couplingredPort = _CouplingredPort_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 8, 2),
    _CouplingredPort_Type()
)
couplingredPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    couplingredPort.setStatus("current")


class _CouplingredMode_Type(Integer32):
    """Custom type couplingredMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("backup", 1),
          ("disabled", 3),
          ("main", 2),
          ("unsupported", 255))
    )


_CouplingredMode_Type.__name__ = "Integer32"
_CouplingredMode_Object = MibScalar
couplingredMode = _CouplingredMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 8, 3),
    _CouplingredMode_Type()
)
couplingredMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    couplingredMode.setStatus("current")
_CouplingredPartnerIp_Type = IpAddress
_CouplingredPartnerIp_Object = MibScalar
couplingredPartnerIp = _CouplingredPartnerIp_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 8, 4),
    _CouplingredPartnerIp_Type()
)
couplingredPartnerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    couplingredPartnerIp.setStatus("current")


class _CouplingredStatus_Type(Integer32):
    """Custom type couplingredStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 1),
          ("disabled", 0),
          ("forwarding", 3),
          ("link", 2),
          ("standby", 4),
          ("undefined", 5),
          ("unsupported", 255))
    )


_CouplingredStatus_Type.__name__ = "Integer32"
_CouplingredStatus_Object = MibScalar
couplingredStatus = _CouplingredStatus_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 8, 5),
    _CouplingredStatus_Type()
)
couplingredStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    couplingredStatus.setStatus("current")


class _CouplingredPartnerStatus_Type(Integer32):
    """Custom type couplingredPartnerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 1),
          ("disabled", 0),
          ("forwarding", 3),
          ("link", 2),
          ("standby", 4),
          ("undefined", 5),
          ("unsupported", 255))
    )


_CouplingredPartnerStatus_Type.__name__ = "Integer32"
_CouplingredPartnerStatus_Object = MibScalar
couplingredPartnerStatus = _CouplingredPartnerStatus_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 8, 6),
    _CouplingredPartnerStatus_Type()
)
couplingredPartnerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    couplingredPartnerStatus.setStatus("current")
_CouplingredValidationFlag_Type = Integer32
_CouplingredValidationFlag_Object = MibScalar
couplingredValidationFlag = _CouplingredValidationFlag_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 8, 7),
    _CouplingredValidationFlag_Type()
)
couplingredValidationFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    couplingredValidationFlag.setStatus("current")
_Sfp_ObjectIdentity = ObjectIdentity
sfp = _Sfp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 9)
)


class _SfpSupport_Type(Integer32):
    """Custom type sfpSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 255))
    )


_SfpSupport_Type.__name__ = "Integer32"
_SfpSupport_Object = MibScalar
sfpSupport = _SfpSupport_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 9, 1),
    _SfpSupport_Type()
)
sfpSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpSupport.setStatus("current")
_SfpCount_Type = Integer32
_SfpCount_Object = MibScalar
sfpCount = _SfpCount_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 9, 2),
    _SfpCount_Type()
)
sfpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpCount.setStatus("current")
_SfpTable_Object = MibTable
sfpTable = _SfpTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 9, 10)
)
if mibBuilder.loadTexts:
    sfpTable.setStatus("current")
_SfpTableEntry_Object = MibTableRow
sfpTableEntry = _SfpTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 9, 10, 1)
)
sfpTableEntry.setIndexNames(
    (0, "MS-SWITCH30-MIB", "sfpId"),
)
if mibBuilder.loadTexts:
    sfpTableEntry.setStatus("current")


class _SfpId_Type(Integer32):
    """Custom type sfpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_SfpId_Type.__name__ = "Integer32"
_SfpId_Object = MibTableColumn
sfpId = _SfpId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 9, 10, 1, 1),
    _SfpId_Type()
)
sfpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpId.setStatus("current")
_SfpPortnumber_Type = Integer32
_SfpPortnumber_Object = MibTableColumn
sfpPortnumber = _SfpPortnumber_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 9, 10, 1, 2),
    _SfpPortnumber_Type()
)
sfpPortnumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpPortnumber.setStatus("current")


class _SfpDetect_Type(Integer32):
    """Custom type sfpDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("plugged", 1),
          ("unplugged", 2),
          ("unsupported", 255))
    )


_SfpDetect_Type.__name__ = "Integer32"
_SfpDetect_Object = MibTableColumn
sfpDetect = _SfpDetect_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 9, 10, 1, 3),
    _SfpDetect_Type()
)
sfpDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDetect.setStatus("current")


class _SfpVendor_Type(DisplayString):
    """Custom type sfpVendor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SfpVendor_Type.__name__ = "DisplayString"
_SfpVendor_Object = MibTableColumn
sfpVendor = _SfpVendor_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 9, 10, 1, 4),
    _SfpVendor_Type()
)
sfpVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpVendor.setStatus("current")


class _SfpVendorPartnumber_Type(DisplayString):
    """Custom type sfpVendorPartnumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SfpVendorPartnumber_Type.__name__ = "DisplayString"
_SfpVendorPartnumber_Object = MibTableColumn
sfpVendorPartnumber = _SfpVendorPartnumber_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 9, 10, 1, 5),
    _SfpVendorPartnumber_Type()
)
sfpVendorPartnumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpVendorPartnumber.setStatus("current")


class _SfpVendorSerialnumber_Type(DisplayString):
    """Custom type sfpVendorSerialnumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SfpVendorSerialnumber_Type.__name__ = "DisplayString"
_SfpVendorSerialnumber_Object = MibTableColumn
sfpVendorSerialnumber = _SfpVendorSerialnumber_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 9, 10, 1, 6),
    _SfpVendorSerialnumber_Type()
)
sfpVendorSerialnumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpVendorSerialnumber.setStatus("current")


class _SfpConnector_Type(Integer32):
    """Custom type sfpConnector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              7,
              8,
              255)
        )
    )
    namedValues = NamedValues(
        *(("connLC", 7),
          ("connMTRJ", 8),
          ("connSC", 1),
          ("unsupported", 255))
    )


_SfpConnector_Type.__name__ = "Integer32"
_SfpConnector_Object = MibTableColumn
sfpConnector = _SfpConnector_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 9, 10, 1, 7),
    _SfpConnector_Type()
)
sfpConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConnector.setStatus("current")
_SfpNominalBitrate_Type = Integer32
_SfpNominalBitrate_Object = MibTableColumn
sfpNominalBitrate = _SfpNominalBitrate_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 9, 10, 1, 8),
    _SfpNominalBitrate_Type()
)
sfpNominalBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpNominalBitrate.setStatus("current")


class _SfpDiagnostic_Type(Integer32):
    """Custom type sfpDiagnostic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("supportedWithExternalCalibration", 2),
          ("supportedWithInternalCalibration", 1),
          ("undefined", 254),
          ("unsupported", 255))
    )


_SfpDiagnostic_Type.__name__ = "Integer32"
_SfpDiagnostic_Object = MibTableColumn
sfpDiagnostic = _SfpDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 9, 10, 1, 9),
    _SfpDiagnostic_Type()
)
sfpDiagnostic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagnostic.setStatus("current")
_SfpTemperature_Type = Integer32
_SfpTemperature_Object = MibTableColumn
sfpTemperature = _SfpTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 9, 10, 1, 10),
    _SfpTemperature_Type()
)
sfpTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpTemperature.setStatus("current")
_SfpVoltage_Type = Integer32
_SfpVoltage_Object = MibTableColumn
sfpVoltage = _SfpVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 9, 10, 1, 11),
    _SfpVoltage_Type()
)
sfpVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpVoltage.setStatus("current")
_SfpTxBias_Type = Integer32
_SfpTxBias_Object = MibTableColumn
sfpTxBias = _SfpTxBias_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 9, 10, 1, 12),
    _SfpTxBias_Type()
)
sfpTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpTxBias.setStatus("current")
_SfpTxPower_Type = Integer32
_SfpTxPower_Object = MibTableColumn
sfpTxPower = _SfpTxPower_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 9, 10, 1, 13),
    _SfpTxPower_Type()
)
sfpTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpTxPower.setStatus("current")
_SfpRxPower_Type = Integer32
_SfpRxPower_Object = MibTableColumn
sfpRxPower = _SfpRxPower_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 9, 10, 1, 14),
    _SfpRxPower_Type()
)
sfpRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpRxPower.setStatus("current")


class _SfpWarnings_Type(Bits):
    """Custom type sfpWarnings based on Bits"""
    namedValues = NamedValues(
        *(("rxPowerHighWarn", 8),
          ("rxPowerLowWarn", 9),
          ("tempHighWarn", 0),
          ("tempLowWarn", 1),
          ("txBiasHighWarn", 4),
          ("txBiasLowWarn", 5),
          ("txPowerHighWarn", 6),
          ("txPowerLowWarn", 7),
          ("vccHighWarn", 2),
          ("vccLowWarn", 3))
    )

_SfpWarnings_Type.__name__ = "Bits"
_SfpWarnings_Object = MibTableColumn
sfpWarnings = _SfpWarnings_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 9, 10, 1, 15),
    _SfpWarnings_Type()
)
sfpWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpWarnings.setStatus("current")


class _SfpAlarms_Type(Bits):
    """Custom type sfpAlarms based on Bits"""
    namedValues = NamedValues(
        *(("rxPowerHighAlarm", 8),
          ("rxPowerLowAlarm", 9),
          ("tempHighAlarm", 0),
          ("tempLowAlarm", 1),
          ("txBiasHighAlarm", 4),
          ("txBiasLowAlarm", 5),
          ("txPowerHighAlarm", 6),
          ("txPowerLowAlarm", 7),
          ("vccHighAlarm", 2),
          ("vccLowAlarm", 3))
    )

_SfpAlarms_Type.__name__ = "Bits"
_SfpAlarms_Object = MibTableColumn
sfpAlarms = _SfpAlarms_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 9, 10, 1, 16),
    _SfpAlarms_Type()
)
sfpAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpAlarms.setStatus("current")
_Relais_ObjectIdentity = ObjectIdentity
relais = _Relais_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 11)
)


class _RelaisSupport_Type(Integer32):
    """Custom type relaisSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 255))
    )


_RelaisSupport_Type.__name__ = "Integer32"
_RelaisSupport_Object = MibScalar
relaisSupport = _RelaisSupport_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 11, 1),
    _RelaisSupport_Type()
)
relaisSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaisSupport.setStatus("current")
_RelaisCount_Type = Integer32
_RelaisCount_Object = MibScalar
relaisCount = _RelaisCount_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 11, 2),
    _RelaisCount_Type()
)
relaisCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaisCount.setStatus("current")
_RelaisTable_Object = MibTable
relaisTable = _RelaisTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 11, 10)
)
if mibBuilder.loadTexts:
    relaisTable.setStatus("current")
_RelaisTableEntry_Object = MibTableRow
relaisTableEntry = _RelaisTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 11, 10, 1)
)
relaisTableEntry.setIndexNames(
    (0, "MS-SWITCH30-MIB", "relaisId"),
)
if mibBuilder.loadTexts:
    relaisTableEntry.setStatus("current")


class _RelaisId_Type(Integer32):
    """Custom type relaisId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_RelaisId_Type.__name__ = "Integer32"
_RelaisId_Object = MibTableColumn
relaisId = _RelaisId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 11, 10, 1, 1),
    _RelaisId_Type()
)
relaisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaisId.setStatus("current")


class _RelaisAlias_Type(DisplayString):
    """Custom type relaisAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RelaisAlias_Type.__name__ = "DisplayString"
_RelaisAlias_Object = MibTableColumn
relaisAlias = _RelaisAlias_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 11, 10, 1, 2),
    _RelaisAlias_Type()
)
relaisAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relaisAlias.setStatus("current")


class _RelaisMode_Type(Integer32):
    """Custom type relaisMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("closeOnEvent", 2),
          ("openOnEvent", 1),
          ("unsupported", 255))
    )


_RelaisMode_Type.__name__ = "Integer32"
_RelaisMode_Object = MibTableColumn
relaisMode = _RelaisMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 11, 10, 1, 3),
    _RelaisMode_Type()
)
relaisMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relaisMode.setStatus("current")


class _RelaisStatus_Type(Integer32):
    """Custom type relaisStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("opened", 2),
          ("unsupported", 255))
    )


_RelaisStatus_Type.__name__ = "Integer32"
_RelaisStatus_Object = MibTableColumn
relaisStatus = _RelaisStatus_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 11, 10, 1, 4),
    _RelaisStatus_Type()
)
relaisStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relaisStatus.setStatus("current")
_Portaccessctrl_ObjectIdentity = ObjectIdentity
portaccessctrl = _Portaccessctrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12)
)


class _PacSupport_Type(Integer32):
    """Custom type pacSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 255))
    )


_PacSupport_Type.__name__ = "Integer32"
_PacSupport_Object = MibScalar
pacSupport = _PacSupport_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 1),
    _PacSupport_Type()
)
pacSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pacSupport.setStatus("current")


class _PacEnable_Type(Integer32):
    """Custom type pacEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_PacEnable_Type.__name__ = "Integer32"
_PacEnable_Object = MibScalar
pacEnable = _PacEnable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 2),
    _PacEnable_Type()
)
pacEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pacEnable.setStatus("current")


class _PacUnauthMode_Type(Integer32):
    """Custom type pacUnauthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("block", 1),
          ("unsupported", 255),
          ("useDefaultVID", 2))
    )


_PacUnauthMode_Type.__name__ = "Integer32"
_PacUnauthMode_Object = MibScalar
pacUnauthMode = _PacUnauthMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 3),
    _PacUnauthMode_Type()
)
pacUnauthMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pacUnauthMode.setStatus("current")


class _PacUnauthVID_Type(Integer32):
    """Custom type pacUnauthVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_PacUnauthVID_Type.__name__ = "Integer32"
_PacUnauthVID_Object = MibScalar
pacUnauthVID = _PacUnauthVID_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 4),
    _PacUnauthVID_Type()
)
pacUnauthVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pacUnauthVID.setStatus("current")
_PacMaxNumberOfAllowedHostsPerPort_Type = Integer32
_PacMaxNumberOfAllowedHostsPerPort_Object = MibScalar
pacMaxNumberOfAllowedHostsPerPort = _PacMaxNumberOfAllowedHostsPerPort_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 5),
    _PacMaxNumberOfAllowedHostsPerPort_Type()
)
pacMaxNumberOfAllowedHostsPerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pacMaxNumberOfAllowedHostsPerPort.setStatus("current")


class _PacFallbackRequestEnable_Type(Integer32):
    """Custom type pacFallbackRequestEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_PacFallbackRequestEnable_Type.__name__ = "Integer32"
_PacFallbackRequestEnable_Object = MibScalar
pacFallbackRequestEnable = _PacFallbackRequestEnable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 6),
    _PacFallbackRequestEnable_Type()
)
pacFallbackRequestEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pacFallbackRequestEnable.setStatus("current")


class _PacFallbackRequestTimeout_Type(Integer32):
    """Custom type pacFallbackRequestTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_PacFallbackRequestTimeout_Type.__name__ = "Integer32"
_PacFallbackRequestTimeout_Object = MibScalar
pacFallbackRequestTimeout = _PacFallbackRequestTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 7),
    _PacFallbackRequestTimeout_Type()
)
pacFallbackRequestTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pacFallbackRequestTimeout.setStatus("current")


class _PacFallbackRejectsEnable_Type(Integer32):
    """Custom type pacFallbackRejectsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_PacFallbackRejectsEnable_Type.__name__ = "Integer32"
_PacFallbackRejectsEnable_Object = MibScalar
pacFallbackRejectsEnable = _PacFallbackRejectsEnable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 8),
    _PacFallbackRejectsEnable_Type()
)
pacFallbackRejectsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pacFallbackRejectsEnable.setStatus("current")


class _PacFallbackMaxRejects_Type(Integer32):
    """Custom type pacFallbackMaxRejects based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PacFallbackMaxRejects_Type.__name__ = "Integer32"
_PacFallbackMaxRejects_Object = MibScalar
pacFallbackMaxRejects = _PacFallbackMaxRejects_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 9),
    _PacFallbackMaxRejects_Type()
)
pacFallbackMaxRejects.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pacFallbackMaxRejects.setStatus("current")


class _PacSupplicantTimeout_Type(Integer32):
    """Custom type pacSupplicantTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PacSupplicantTimeout_Type.__name__ = "Integer32"
_PacSupplicantTimeout_Object = MibScalar
pacSupplicantTimeout = _PacSupplicantTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 10),
    _PacSupplicantTimeout_Type()
)
pacSupplicantTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pacSupplicantTimeout.setStatus("current")


class _PacReauthEnable_Type(Integer32):
    """Custom type pacReauthEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_PacReauthEnable_Type.__name__ = "Integer32"
_PacReauthEnable_Object = MibScalar
pacReauthEnable = _PacReauthEnable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 11),
    _PacReauthEnable_Type()
)
pacReauthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pacReauthEnable.setStatus("current")


class _PacReauthTime_Type(Integer32):
    """Custom type pacReauthTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PacReauthTime_Type.__name__ = "Integer32"
_PacReauthTime_Object = MibScalar
pacReauthTime = _PacReauthTime_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 12),
    _PacReauthTime_Type()
)
pacReauthTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pacReauthTime.setStatus("current")
_PacStatusTable_Object = MibTable
pacStatusTable = _PacStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 100)
)
if mibBuilder.loadTexts:
    pacStatusTable.setStatus("current")
_PacStatusTableEntry_Object = MibTableRow
pacStatusTableEntry = _PacStatusTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 100, 1)
)
pacStatusTableEntry.setIndexNames(
    (0, "MS-SWITCH30-MIB", "pacStatPortId"),
)
if mibBuilder.loadTexts:
    pacStatusTableEntry.setStatus("current")


class _PacStatPortId_Type(Integer32):
    """Custom type pacStatPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_PacStatPortId_Type.__name__ = "Integer32"
_PacStatPortId_Object = MibTableColumn
pacStatPortId = _PacStatPortId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 100, 1, 1),
    _PacStatPortId_Type()
)
pacStatPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pacStatPortId.setStatus("current")


class _PacStatPortMode_Type(Integer32):
    """Custom type pacStatPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("forceAuthorized", 1),
          ("forceUnauthorized", 5),
          ("ieee8021xAuthentication", 4),
          ("macLocking", 2),
          ("radiusMacAuthentication", 3),
          ("undefined", 254),
          ("unsupported", 255))
    )


_PacStatPortMode_Type.__name__ = "Integer32"
_PacStatPortMode_Object = MibTableColumn
pacStatPortMode = _PacStatPortMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 100, 1, 2),
    _PacStatPortMode_Type()
)
pacStatPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pacStatPortMode.setStatus("current")


class _PacStatPortStatus_Type(Integer32):
    """Custom type pacStatPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("authorized", 1),
          ("unauthorized", 2),
          ("undefined", 254),
          ("unsupported", 255))
    )


_PacStatPortStatus_Type.__name__ = "Integer32"
_PacStatPortStatus_Object = MibTableColumn
pacStatPortStatus = _PacStatPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 100, 1, 3),
    _PacStatPortStatus_Type()
)
pacStatPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pacStatPortStatus.setStatus("current")


class _PacStatUserStatus1_Type(Integer32):
    """Custom type pacStatUserStatus1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              11,
              12,
              20,
              21,
              22,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("authorized1", 10),
          ("authorized2", 20),
          ("tobedone1", 12),
          ("tobedone2", 22),
          ("unauthorized1", 11),
          ("unauthorized2", 21),
          ("undefined", 254),
          ("unsupported", 255))
    )


_PacStatUserStatus1_Type.__name__ = "Integer32"
_PacStatUserStatus1_Object = MibTableColumn
pacStatUserStatus1 = _PacStatUserStatus1_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 100, 1, 4),
    _PacStatUserStatus1_Type()
)
pacStatUserStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pacStatUserStatus1.setStatus("current")


class _PacStatUserStatus2_Type(Integer32):
    """Custom type pacStatUserStatus2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              11,
              12,
              20,
              21,
              22,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("authorized1", 10),
          ("authorized2", 20),
          ("tobedone1", 12),
          ("tobedone2", 22),
          ("unauthorized1", 11),
          ("unauthorized2", 21),
          ("undefined", 254),
          ("unsupported", 255))
    )


_PacStatUserStatus2_Type.__name__ = "Integer32"
_PacStatUserStatus2_Object = MibTableColumn
pacStatUserStatus2 = _PacStatUserStatus2_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 100, 1, 5),
    _PacStatUserStatus2_Type()
)
pacStatUserStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pacStatUserStatus2.setStatus("current")


class _PacStatUserStatus3_Type(Integer32):
    """Custom type pacStatUserStatus3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              11,
              12,
              20,
              21,
              22,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("authorized1", 10),
          ("authorized2", 20),
          ("tobedone1", 12),
          ("tobedone2", 22),
          ("unauthorized1", 11),
          ("unauthorized2", 21),
          ("undefined", 254),
          ("unsupported", 255))
    )


_PacStatUserStatus3_Type.__name__ = "Integer32"
_PacStatUserStatus3_Object = MibTableColumn
pacStatUserStatus3 = _PacStatUserStatus3_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 100, 1, 6),
    _PacStatUserStatus3_Type()
)
pacStatUserStatus3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pacStatUserStatus3.setStatus("current")


class _PacStatUserStatus4_Type(Integer32):
    """Custom type pacStatUserStatus4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              11,
              12,
              20,
              21,
              22,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("authorized1", 10),
          ("authorized2", 20),
          ("tobedone1", 12),
          ("tobedone2", 22),
          ("unauthorized1", 11),
          ("unauthorized2", 21),
          ("undefined", 254),
          ("unsupported", 255))
    )


_PacStatUserStatus4_Type.__name__ = "Integer32"
_PacStatUserStatus4_Object = MibTableColumn
pacStatUserStatus4 = _PacStatUserStatus4_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 100, 1, 7),
    _PacStatUserStatus4_Type()
)
pacStatUserStatus4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pacStatUserStatus4.setStatus("current")
_PacStatUserMac1_Type = PhysAddress
_PacStatUserMac1_Object = MibTableColumn
pacStatUserMac1 = _PacStatUserMac1_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 100, 1, 8),
    _PacStatUserMac1_Type()
)
pacStatUserMac1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pacStatUserMac1.setStatus("current")
_PacStatUserMac2_Type = PhysAddress
_PacStatUserMac2_Object = MibTableColumn
pacStatUserMac2 = _PacStatUserMac2_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 100, 1, 9),
    _PacStatUserMac2_Type()
)
pacStatUserMac2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pacStatUserMac2.setStatus("current")
_PacStatUserMac3_Type = PhysAddress
_PacStatUserMac3_Object = MibTableColumn
pacStatUserMac3 = _PacStatUserMac3_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 100, 1, 10),
    _PacStatUserMac3_Type()
)
pacStatUserMac3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pacStatUserMac3.setStatus("current")
_PacStatUserMac4_Type = PhysAddress
_PacStatUserMac4_Object = MibTableColumn
pacStatUserMac4 = _PacStatUserMac4_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 100, 1, 11),
    _PacStatUserMac4_Type()
)
pacStatUserMac4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pacStatUserMac4.setStatus("current")


class _PacStatUserName1_Type(DisplayString):
    """Custom type pacStatUserName1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PacStatUserName1_Type.__name__ = "DisplayString"
_PacStatUserName1_Object = MibTableColumn
pacStatUserName1 = _PacStatUserName1_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 100, 1, 12),
    _PacStatUserName1_Type()
)
pacStatUserName1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pacStatUserName1.setStatus("current")


class _PacStatUserName2_Type(DisplayString):
    """Custom type pacStatUserName2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PacStatUserName2_Type.__name__ = "DisplayString"
_PacStatUserName2_Object = MibTableColumn
pacStatUserName2 = _PacStatUserName2_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 100, 1, 13),
    _PacStatUserName2_Type()
)
pacStatUserName2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pacStatUserName2.setStatus("current")


class _PacStatUserName3_Type(DisplayString):
    """Custom type pacStatUserName3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PacStatUserName3_Type.__name__ = "DisplayString"
_PacStatUserName3_Object = MibTableColumn
pacStatUserName3 = _PacStatUserName3_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 100, 1, 14),
    _PacStatUserName3_Type()
)
pacStatUserName3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pacStatUserName3.setStatus("current")


class _PacStatUserName4_Type(DisplayString):
    """Custom type pacStatUserName4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PacStatUserName4_Type.__name__ = "DisplayString"
_PacStatUserName4_Object = MibTableColumn
pacStatUserName4 = _PacStatUserName4_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 100, 1, 15),
    _PacStatUserName4_Type()
)
pacStatUserName4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pacStatUserName4.setStatus("current")
_PacStatUserIp1_Type = IpAddress
_PacStatUserIp1_Object = MibTableColumn
pacStatUserIp1 = _PacStatUserIp1_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 100, 1, 16),
    _PacStatUserIp1_Type()
)
pacStatUserIp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pacStatUserIp1.setStatus("current")
_PacStatUserIp2_Type = IpAddress
_PacStatUserIp2_Object = MibTableColumn
pacStatUserIp2 = _PacStatUserIp2_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 100, 1, 17),
    _PacStatUserIp2_Type()
)
pacStatUserIp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pacStatUserIp2.setStatus("current")
_PacStatUserIp3_Type = IpAddress
_PacStatUserIp3_Object = MibTableColumn
pacStatUserIp3 = _PacStatUserIp3_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 100, 1, 18),
    _PacStatUserIp3_Type()
)
pacStatUserIp3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pacStatUserIp3.setStatus("current")
_PacStatUserIp4_Type = IpAddress
_PacStatUserIp4_Object = MibTableColumn
pacStatUserIp4 = _PacStatUserIp4_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 100, 1, 19),
    _PacStatUserIp4_Type()
)
pacStatUserIp4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pacStatUserIp4.setStatus("current")
_PacConfigTable_Object = MibTable
pacConfigTable = _PacConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 110)
)
if mibBuilder.loadTexts:
    pacConfigTable.setStatus("current")
_PacConfigTableEntry_Object = MibTableRow
pacConfigTableEntry = _PacConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 110, 1)
)
pacConfigTableEntry.setIndexNames(
    (0, "MS-SWITCH30-MIB", "pacConfPortId"),
)
if mibBuilder.loadTexts:
    pacConfigTableEntry.setStatus("current")


class _PacConfPortId_Type(Integer32):
    """Custom type pacConfPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_PacConfPortId_Type.__name__ = "Integer32"
_PacConfPortId_Object = MibTableColumn
pacConfPortId = _PacConfPortId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 110, 1, 1),
    _PacConfPortId_Type()
)
pacConfPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pacConfPortId.setStatus("current")


class _PacConfMode_Type(Integer32):
    """Custom type pacConfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("forceAuthorized", 1),
          ("forceUnauthorized", 5),
          ("ieee8021xAuthentication", 4),
          ("macLocking", 2),
          ("radiusMacAuthentication", 3),
          ("undefined", 254),
          ("unsupported", 255))
    )


_PacConfMode_Type.__name__ = "Integer32"
_PacConfMode_Object = MibTableColumn
pacConfMode = _PacConfMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 110, 1, 2),
    _PacConfMode_Type()
)
pacConfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pacConfMode.setStatus("current")


class _PacConfMaxMacCount_Type(Integer32):
    """Custom type pacConfMaxMacCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_PacConfMaxMacCount_Type.__name__ = "Integer32"
_PacConfMaxMacCount_Object = MibTableColumn
pacConfMaxMacCount = _PacConfMaxMacCount_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 110, 1, 3),
    _PacConfMaxMacCount_Type()
)
pacConfMaxMacCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pacConfMaxMacCount.setStatus("current")
_PacMacLockingTable_Object = MibTable
pacMacLockingTable = _PacMacLockingTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 120)
)
if mibBuilder.loadTexts:
    pacMacLockingTable.setStatus("current")
_PacMacLockTableEntry_Object = MibTableRow
pacMacLockTableEntry = _PacMacLockTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 120, 1)
)
pacMacLockTableEntry.setIndexNames(
    (0, "MS-SWITCH30-MIB", "pacMacLockPortId"),
)
if mibBuilder.loadTexts:
    pacMacLockTableEntry.setStatus("current")


class _PacMacLockPortId_Type(Integer32):
    """Custom type pacMacLockPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_PacMacLockPortId_Type.__name__ = "Integer32"
_PacMacLockPortId_Object = MibTableColumn
pacMacLockPortId = _PacMacLockPortId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 120, 1, 1),
    _PacMacLockPortId_Type()
)
pacMacLockPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pacMacLockPortId.setStatus("current")


class _PacMacLockEnable1_Type(Integer32):
    """Custom type pacMacLockEnable1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_PacMacLockEnable1_Type.__name__ = "Integer32"
_PacMacLockEnable1_Object = MibTableColumn
pacMacLockEnable1 = _PacMacLockEnable1_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 120, 1, 2),
    _PacMacLockEnable1_Type()
)
pacMacLockEnable1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pacMacLockEnable1.setStatus("current")


class _PacMacLockEnable2_Type(Integer32):
    """Custom type pacMacLockEnable2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_PacMacLockEnable2_Type.__name__ = "Integer32"
_PacMacLockEnable2_Object = MibTableColumn
pacMacLockEnable2 = _PacMacLockEnable2_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 120, 1, 3),
    _PacMacLockEnable2_Type()
)
pacMacLockEnable2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pacMacLockEnable2.setStatus("current")


class _PacMacLockEnable3_Type(Integer32):
    """Custom type pacMacLockEnable3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_PacMacLockEnable3_Type.__name__ = "Integer32"
_PacMacLockEnable3_Object = MibTableColumn
pacMacLockEnable3 = _PacMacLockEnable3_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 120, 1, 4),
    _PacMacLockEnable3_Type()
)
pacMacLockEnable3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pacMacLockEnable3.setStatus("current")


class _PacMacLockEnable4_Type(Integer32):
    """Custom type pacMacLockEnable4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_PacMacLockEnable4_Type.__name__ = "Integer32"
_PacMacLockEnable4_Object = MibTableColumn
pacMacLockEnable4 = _PacMacLockEnable4_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 120, 1, 5),
    _PacMacLockEnable4_Type()
)
pacMacLockEnable4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pacMacLockEnable4.setStatus("current")


class _PacMacLockLearn1_Type(Integer32):
    """Custom type pacMacLockLearn1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 2),
          ("learn", 1),
          ("unsupported", 255))
    )


_PacMacLockLearn1_Type.__name__ = "Integer32"
_PacMacLockLearn1_Object = MibTableColumn
pacMacLockLearn1 = _PacMacLockLearn1_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 120, 1, 6),
    _PacMacLockLearn1_Type()
)
pacMacLockLearn1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pacMacLockLearn1.setStatus("current")


class _PacMacLockLearn2_Type(Integer32):
    """Custom type pacMacLockLearn2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 2),
          ("learn", 1),
          ("unsupported", 255))
    )


_PacMacLockLearn2_Type.__name__ = "Integer32"
_PacMacLockLearn2_Object = MibTableColumn
pacMacLockLearn2 = _PacMacLockLearn2_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 120, 1, 7),
    _PacMacLockLearn2_Type()
)
pacMacLockLearn2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pacMacLockLearn2.setStatus("current")


class _PacMacLockLearn3_Type(Integer32):
    """Custom type pacMacLockLearn3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 2),
          ("learn", 1),
          ("unsupported", 255))
    )


_PacMacLockLearn3_Type.__name__ = "Integer32"
_PacMacLockLearn3_Object = MibTableColumn
pacMacLockLearn3 = _PacMacLockLearn3_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 120, 1, 8),
    _PacMacLockLearn3_Type()
)
pacMacLockLearn3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pacMacLockLearn3.setStatus("current")


class _PacMacLockLearn4_Type(Integer32):
    """Custom type pacMacLockLearn4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 2),
          ("learn", 1),
          ("unsupported", 255))
    )


_PacMacLockLearn4_Type.__name__ = "Integer32"
_PacMacLockLearn4_Object = MibTableColumn
pacMacLockLearn4 = _PacMacLockLearn4_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 120, 1, 9),
    _PacMacLockLearn4_Type()
)
pacMacLockLearn4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pacMacLockLearn4.setStatus("current")
_PacLockedMac1_Type = PhysAddress
_PacLockedMac1_Object = MibTableColumn
pacLockedMac1 = _PacLockedMac1_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 120, 1, 10),
    _PacLockedMac1_Type()
)
pacLockedMac1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pacLockedMac1.setStatus("current")
_PacLockedMac2_Type = PhysAddress
_PacLockedMac2_Object = MibTableColumn
pacLockedMac2 = _PacLockedMac2_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 120, 1, 11),
    _PacLockedMac2_Type()
)
pacLockedMac2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pacLockedMac2.setStatus("current")
_PacLockedMac3_Type = PhysAddress
_PacLockedMac3_Object = MibTableColumn
pacLockedMac3 = _PacLockedMac3_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 120, 1, 12),
    _PacLockedMac3_Type()
)
pacLockedMac3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pacLockedMac3.setStatus("current")
_PacLockedMac4_Type = PhysAddress
_PacLockedMac4_Object = MibTableColumn
pacLockedMac4 = _PacLockedMac4_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 12, 120, 1, 13),
    _PacLockedMac4_Type()
)
pacLockedMac4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pacLockedMac4.setStatus("current")
_Igmps_ObjectIdentity = ObjectIdentity
igmps = _Igmps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13)
)


class _IgmpsSupport_Type(Integer32):
    """Custom type igmpsSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 255))
    )


_IgmpsSupport_Type.__name__ = "Integer32"
_IgmpsSupport_Object = MibScalar
igmpsSupport = _IgmpsSupport_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 1),
    _IgmpsSupport_Type()
)
igmpsSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpsSupport.setStatus("current")


class _IgmpsEnable_Type(Integer32):
    """Custom type igmpsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_IgmpsEnable_Type.__name__ = "Integer32"
_IgmpsEnable_Object = MibScalar
igmpsEnable = _IgmpsEnable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 2),
    _IgmpsEnable_Type()
)
igmpsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpsEnable.setStatus("current")


class _IgmpsFastLeave_Type(Integer32):
    """Custom type igmpsFastLeave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_IgmpsFastLeave_Type.__name__ = "Integer32"
_IgmpsFastLeave_Object = MibScalar
igmpsFastLeave = _IgmpsFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 3),
    _IgmpsFastLeave_Type()
)
igmpsFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpsFastLeave.setStatus("current")


class _IgmpsReportAggregation_Type(Integer32):
    """Custom type igmpsReportAggregation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_IgmpsReportAggregation_Type.__name__ = "Integer32"
_IgmpsReportAggregation_Object = MibScalar
igmpsReportAggregation = _IgmpsReportAggregation_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 4),
    _IgmpsReportAggregation_Type()
)
igmpsReportAggregation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpsReportAggregation.setStatus("current")


class _IgmpsFloodingUnregPack_Type(Integer32):
    """Custom type igmpsFloodingUnregPack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_IgmpsFloodingUnregPack_Type.__name__ = "Integer32"
_IgmpsFloodingUnregPack_Object = MibScalar
igmpsFloodingUnregPack = _IgmpsFloodingUnregPack_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 5),
    _IgmpsFloodingUnregPack_Type()
)
igmpsFloodingUnregPack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpsFloodingUnregPack.setStatus("current")
_IgmpsMaxGroupLimit_Type = Integer32
_IgmpsMaxGroupLimit_Object = MibScalar
igmpsMaxGroupLimit = _IgmpsMaxGroupLimit_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 6),
    _IgmpsMaxGroupLimit_Type()
)
igmpsMaxGroupLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpsMaxGroupLimit.setStatus("current")
_IgmpsGroupLimit_Type = Integer32
_IgmpsGroupLimit_Object = MibScalar
igmpsGroupLimit = _IgmpsGroupLimit_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 7),
    _IgmpsGroupLimit_Type()
)
igmpsGroupLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpsGroupLimit.setStatus("current")
_IgmpsGroupNumber_Type = Integer32
_IgmpsGroupNumber_Object = MibScalar
igmpsGroupNumber = _IgmpsGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 8),
    _IgmpsGroupNumber_Type()
)
igmpsGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpsGroupNumber.setStatus("current")


class _IgmpsRouterDetection_Type(Integer32):
    """Custom type igmpsRouterDetection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("discovery", 1),
          ("query", 2),
          ("unsupported", 255))
    )


_IgmpsRouterDetection_Type.__name__ = "Integer32"
_IgmpsRouterDetection_Object = MibScalar
igmpsRouterDetection = _IgmpsRouterDetection_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 9),
    _IgmpsRouterDetection_Type()
)
igmpsRouterDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpsRouterDetection.setStatus("current")


class _IgmpsGroupMembershipInterval_Type(Integer32):
    """Custom type igmpsGroupMembershipInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 1000),
    )


_IgmpsGroupMembershipInterval_Type.__name__ = "Integer32"
_IgmpsGroupMembershipInterval_Object = MibScalar
igmpsGroupMembershipInterval = _IgmpsGroupMembershipInterval_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 10),
    _IgmpsGroupMembershipInterval_Type()
)
igmpsGroupMembershipInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpsGroupMembershipInterval.setStatus("current")


class _IgmpsMaximumResposeTime_Type(Integer32):
    """Custom type igmpsMaximumResposeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_IgmpsMaximumResposeTime_Type.__name__ = "Integer32"
_IgmpsMaximumResposeTime_Object = MibScalar
igmpsMaximumResposeTime = _IgmpsMaximumResposeTime_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 11),
    _IgmpsMaximumResposeTime_Type()
)
igmpsMaximumResposeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpsMaximumResposeTime.setStatus("current")


class _IgmpsLastMemeberQueryTime_Type(Integer32):
    """Custom type igmpsLastMemeberQueryTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 175),
    )


_IgmpsLastMemeberQueryTime_Type.__name__ = "Integer32"
_IgmpsLastMemeberQueryTime_Object = MibScalar
igmpsLastMemeberQueryTime = _IgmpsLastMemeberQueryTime_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 12),
    _IgmpsLastMemeberQueryTime_Type()
)
igmpsLastMemeberQueryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpsLastMemeberQueryTime.setStatus("current")


class _IgmpsNeighborDeadInterval_Type(Integer32):
    """Custom type igmpsNeighborDeadInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(12, 554),
    )


_IgmpsNeighborDeadInterval_Type.__name__ = "Integer32"
_IgmpsNeighborDeadInterval_Object = MibScalar
igmpsNeighborDeadInterval = _IgmpsNeighborDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 13),
    _IgmpsNeighborDeadInterval_Type()
)
igmpsNeighborDeadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpsNeighborDeadInterval.setStatus("current")


class _IgmpsRouterAgingTime_Type(Integer32):
    """Custom type igmpsRouterAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 1000),
    )


_IgmpsRouterAgingTime_Type.__name__ = "Integer32"
_IgmpsRouterAgingTime_Object = MibScalar
igmpsRouterAgingTime = _IgmpsRouterAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 14),
    _IgmpsRouterAgingTime_Type()
)
igmpsRouterAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpsRouterAgingTime.setStatus("current")
_IgmpsRxMessageGeneralQuery_Type = Integer32
_IgmpsRxMessageGeneralQuery_Object = MibScalar
igmpsRxMessageGeneralQuery = _IgmpsRxMessageGeneralQuery_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 15),
    _IgmpsRxMessageGeneralQuery_Type()
)
igmpsRxMessageGeneralQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpsRxMessageGeneralQuery.setStatus("current")
_IgmpsRxMessageSpecificQuery_Type = Integer32
_IgmpsRxMessageSpecificQuery_Object = MibScalar
igmpsRxMessageSpecificQuery = _IgmpsRxMessageSpecificQuery_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 16),
    _IgmpsRxMessageSpecificQuery_Type()
)
igmpsRxMessageSpecificQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpsRxMessageSpecificQuery.setStatus("current")
_IgmpsRxMessageReport_Type = Integer32
_IgmpsRxMessageReport_Object = MibScalar
igmpsRxMessageReport = _IgmpsRxMessageReport_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 17),
    _IgmpsRxMessageReport_Type()
)
igmpsRxMessageReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpsRxMessageReport.setStatus("current")
_IgmpsRxMessageLeave_Type = Integer32
_IgmpsRxMessageLeave_Object = MibScalar
igmpsRxMessageLeave = _IgmpsRxMessageLeave_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 18),
    _IgmpsRxMessageLeave_Type()
)
igmpsRxMessageLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpsRxMessageLeave.setStatus("current")
_IgmpsRxMessageAdvertisement_Type = Integer32
_IgmpsRxMessageAdvertisement_Object = MibScalar
igmpsRxMessageAdvertisement = _IgmpsRxMessageAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 19),
    _IgmpsRxMessageAdvertisement_Type()
)
igmpsRxMessageAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpsRxMessageAdvertisement.setStatus("current")
_IgmpsRxMessageTermination_Type = Integer32
_IgmpsRxMessageTermination_Object = MibScalar
igmpsRxMessageTermination = _IgmpsRxMessageTermination_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 20),
    _IgmpsRxMessageTermination_Type()
)
igmpsRxMessageTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpsRxMessageTermination.setStatus("current")
_IgmpsTxMessageSolicitation_Type = Integer32
_IgmpsTxMessageSolicitation_Object = MibScalar
igmpsTxMessageSolicitation = _IgmpsTxMessageSolicitation_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 21),
    _IgmpsTxMessageSolicitation_Type()
)
igmpsTxMessageSolicitation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpsTxMessageSolicitation.setStatus("current")


class _IgmpsCounterReset_Type(Integer32):
    """Custom type igmpsCounterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("normalOperation", 0),
          ("reset", 1),
          ("unsupported", 255))
    )


_IgmpsCounterReset_Type.__name__ = "Integer32"
_IgmpsCounterReset_Object = MibScalar
igmpsCounterReset = _IgmpsCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 22),
    _IgmpsCounterReset_Type()
)
igmpsCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpsCounterReset.setStatus("current")
_IgmpsPortTable_Object = MibTable
igmpsPortTable = _IgmpsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 30)
)
if mibBuilder.loadTexts:
    igmpsPortTable.setStatus("current")
_IgmpsPortTableEntry_Object = MibTableRow
igmpsPortTableEntry = _IgmpsPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 30, 1)
)
igmpsPortTableEntry.setIndexNames(
    (0, "MS-SWITCH30-MIB", "igmpsPortId"),
)
if mibBuilder.loadTexts:
    igmpsPortTableEntry.setStatus("current")


class _IgmpsPortId_Type(Integer32):
    """Custom type igmpsPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_IgmpsPortId_Type.__name__ = "Integer32"
_IgmpsPortId_Object = MibTableColumn
igmpsPortId = _IgmpsPortId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 30, 1, 1),
    _IgmpsPortId_Type()
)
igmpsPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpsPortId.setStatus("current")


class _IgmpsPortSnooping_Type(Integer32):
    """Custom type igmpsPortSnooping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_IgmpsPortSnooping_Type.__name__ = "Integer32"
_IgmpsPortSnooping_Object = MibTableColumn
igmpsPortSnooping = _IgmpsPortSnooping_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 30, 1, 2),
    _IgmpsPortSnooping_Type()
)
igmpsPortSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpsPortSnooping.setStatus("current")


class _IgmpsPortStaticRouter_Type(Integer32):
    """Custom type igmpsPortStaticRouter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_IgmpsPortStaticRouter_Type.__name__ = "Integer32"
_IgmpsPortStaticRouter_Object = MibTableColumn
igmpsPortStaticRouter = _IgmpsPortStaticRouter_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 30, 1, 3),
    _IgmpsPortStaticRouter_Type()
)
igmpsPortStaticRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpsPortStaticRouter.setStatus("current")


class _IgmpsPortDynamicRouter_Type(Integer32):
    """Custom type igmpsPortDynamicRouter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("detected", 1),
          ("undetected", 2),
          ("unsupported", 255))
    )


_IgmpsPortDynamicRouter_Type.__name__ = "Integer32"
_IgmpsPortDynamicRouter_Object = MibTableColumn
igmpsPortDynamicRouter = _IgmpsPortDynamicRouter_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 30, 1, 4),
    _IgmpsPortDynamicRouter_Type()
)
igmpsPortDynamicRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpsPortDynamicRouter.setStatus("current")
_IgmpsGroupTable_Object = MibTable
igmpsGroupTable = _IgmpsGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 40)
)
if mibBuilder.loadTexts:
    igmpsGroupTable.setStatus("current")
_IgmpsGroupTableEntry_Object = MibTableRow
igmpsGroupTableEntry = _IgmpsGroupTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 40, 1)
)
igmpsGroupTableEntry.setIndexNames(
    (0, "MS-SWITCH30-MIB", "igmpsGroupId"),
)
if mibBuilder.loadTexts:
    igmpsGroupTableEntry.setStatus("current")
_IgmpsGroupId_Type = Unsigned32
_IgmpsGroupId_Object = MibTableColumn
igmpsGroupId = _IgmpsGroupId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 40, 1, 1),
    _IgmpsGroupId_Type()
)
igmpsGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpsGroupId.setStatus("current")
_IgmpsGroupMac_Type = PhysAddress
_IgmpsGroupMac_Object = MibTableColumn
igmpsGroupMac = _IgmpsGroupMac_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 40, 1, 2),
    _IgmpsGroupMac_Type()
)
igmpsGroupMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpsGroupMac.setStatus("current")
_IgmpsGroupVlanId_Type = Integer32
_IgmpsGroupVlanId_Object = MibTableColumn
igmpsGroupVlanId = _IgmpsGroupVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 40, 1, 3),
    _IgmpsGroupVlanId_Type()
)
igmpsGroupVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpsGroupVlanId.setStatus("current")
_IgmpsGroupTimestamp_Type = Integer32
_IgmpsGroupTimestamp_Object = MibTableColumn
igmpsGroupTimestamp = _IgmpsGroupTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 40, 1, 4),
    _IgmpsGroupTimestamp_Type()
)
igmpsGroupTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpsGroupTimestamp.setStatus("current")


class _IgmpsGroupLeaveFlag_Type(Integer32):
    """Custom type igmpsGroupLeaveFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("unset", 2),
          ("unsupported", 255))
    )


_IgmpsGroupLeaveFlag_Type.__name__ = "Integer32"
_IgmpsGroupLeaveFlag_Object = MibTableColumn
igmpsGroupLeaveFlag = _IgmpsGroupLeaveFlag_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 40, 1, 5),
    _IgmpsGroupLeaveFlag_Type()
)
igmpsGroupLeaveFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpsGroupLeaveFlag.setStatus("current")


class _IgmpsGroupMemberPort1_Type(Integer32):
    """Custom type igmpsGroupMemberPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_IgmpsGroupMemberPort1_Type.__name__ = "Integer32"
_IgmpsGroupMemberPort1_Object = MibTableColumn
igmpsGroupMemberPort1 = _IgmpsGroupMemberPort1_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 40, 1, 6),
    _IgmpsGroupMemberPort1_Type()
)
igmpsGroupMemberPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpsGroupMemberPort1.setStatus("current")


class _IgmpsGroupMemberPort2_Type(Integer32):
    """Custom type igmpsGroupMemberPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_IgmpsGroupMemberPort2_Type.__name__ = "Integer32"
_IgmpsGroupMemberPort2_Object = MibTableColumn
igmpsGroupMemberPort2 = _IgmpsGroupMemberPort2_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 40, 1, 7),
    _IgmpsGroupMemberPort2_Type()
)
igmpsGroupMemberPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpsGroupMemberPort2.setStatus("current")


class _IgmpsGroupMemberPort3_Type(Integer32):
    """Custom type igmpsGroupMemberPort3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_IgmpsGroupMemberPort3_Type.__name__ = "Integer32"
_IgmpsGroupMemberPort3_Object = MibTableColumn
igmpsGroupMemberPort3 = _IgmpsGroupMemberPort3_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 40, 1, 8),
    _IgmpsGroupMemberPort3_Type()
)
igmpsGroupMemberPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpsGroupMemberPort3.setStatus("current")


class _IgmpsGroupMemberPort4_Type(Integer32):
    """Custom type igmpsGroupMemberPort4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_IgmpsGroupMemberPort4_Type.__name__ = "Integer32"
_IgmpsGroupMemberPort4_Object = MibTableColumn
igmpsGroupMemberPort4 = _IgmpsGroupMemberPort4_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 40, 1, 9),
    _IgmpsGroupMemberPort4_Type()
)
igmpsGroupMemberPort4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpsGroupMemberPort4.setStatus("current")


class _IgmpsGroupMemberPort5_Type(Integer32):
    """Custom type igmpsGroupMemberPort5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_IgmpsGroupMemberPort5_Type.__name__ = "Integer32"
_IgmpsGroupMemberPort5_Object = MibTableColumn
igmpsGroupMemberPort5 = _IgmpsGroupMemberPort5_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 40, 1, 10),
    _IgmpsGroupMemberPort5_Type()
)
igmpsGroupMemberPort5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpsGroupMemberPort5.setStatus("current")


class _IgmpsGroupMemberPort6_Type(Integer32):
    """Custom type igmpsGroupMemberPort6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_IgmpsGroupMemberPort6_Type.__name__ = "Integer32"
_IgmpsGroupMemberPort6_Object = MibTableColumn
igmpsGroupMemberPort6 = _IgmpsGroupMemberPort6_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 40, 1, 11),
    _IgmpsGroupMemberPort6_Type()
)
igmpsGroupMemberPort6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpsGroupMemberPort6.setStatus("current")


class _IgmpsGroupMemberPort7_Type(Integer32):
    """Custom type igmpsGroupMemberPort7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_IgmpsGroupMemberPort7_Type.__name__ = "Integer32"
_IgmpsGroupMemberPort7_Object = MibTableColumn
igmpsGroupMemberPort7 = _IgmpsGroupMemberPort7_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 40, 1, 12),
    _IgmpsGroupMemberPort7_Type()
)
igmpsGroupMemberPort7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpsGroupMemberPort7.setStatus("current")


class _IgmpsGroupMemberPort8_Type(Integer32):
    """Custom type igmpsGroupMemberPort8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_IgmpsGroupMemberPort8_Type.__name__ = "Integer32"
_IgmpsGroupMemberPort8_Object = MibTableColumn
igmpsGroupMemberPort8 = _IgmpsGroupMemberPort8_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 40, 1, 13),
    _IgmpsGroupMemberPort8_Type()
)
igmpsGroupMemberPort8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpsGroupMemberPort8.setStatus("current")


class _IgmpsGroupMemberPort9_Type(Integer32):
    """Custom type igmpsGroupMemberPort9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_IgmpsGroupMemberPort9_Type.__name__ = "Integer32"
_IgmpsGroupMemberPort9_Object = MibTableColumn
igmpsGroupMemberPort9 = _IgmpsGroupMemberPort9_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 40, 1, 14),
    _IgmpsGroupMemberPort9_Type()
)
igmpsGroupMemberPort9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpsGroupMemberPort9.setStatus("current")


class _IgmpsGroupMemberPort10_Type(Integer32):
    """Custom type igmpsGroupMemberPort10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_IgmpsGroupMemberPort10_Type.__name__ = "Integer32"
_IgmpsGroupMemberPort10_Object = MibTableColumn
igmpsGroupMemberPort10 = _IgmpsGroupMemberPort10_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 40, 1, 15),
    _IgmpsGroupMemberPort10_Type()
)
igmpsGroupMemberPort10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpsGroupMemberPort10.setStatus("current")


class _IgmpsGroupMemberPort11_Type(Integer32):
    """Custom type igmpsGroupMemberPort11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_IgmpsGroupMemberPort11_Type.__name__ = "Integer32"
_IgmpsGroupMemberPort11_Object = MibTableColumn
igmpsGroupMemberPort11 = _IgmpsGroupMemberPort11_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 40, 1, 16),
    _IgmpsGroupMemberPort11_Type()
)
igmpsGroupMemberPort11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpsGroupMemberPort11.setStatus("current")


class _IgmpsGroupMemberPort12_Type(Integer32):
    """Custom type igmpsGroupMemberPort12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_IgmpsGroupMemberPort12_Type.__name__ = "Integer32"
_IgmpsGroupMemberPort12_Object = MibTableColumn
igmpsGroupMemberPort12 = _IgmpsGroupMemberPort12_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 40, 1, 17),
    _IgmpsGroupMemberPort12_Type()
)
igmpsGroupMemberPort12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpsGroupMemberPort12.setStatus("current")


class _IgmpsGroupMemberPort13_Type(Integer32):
    """Custom type igmpsGroupMemberPort13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_IgmpsGroupMemberPort13_Type.__name__ = "Integer32"
_IgmpsGroupMemberPort13_Object = MibTableColumn
igmpsGroupMemberPort13 = _IgmpsGroupMemberPort13_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 40, 1, 18),
    _IgmpsGroupMemberPort13_Type()
)
igmpsGroupMemberPort13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpsGroupMemberPort13.setStatus("current")


class _IgmpsGroupMemberPort14_Type(Integer32):
    """Custom type igmpsGroupMemberPort14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_IgmpsGroupMemberPort14_Type.__name__ = "Integer32"
_IgmpsGroupMemberPort14_Object = MibTableColumn
igmpsGroupMemberPort14 = _IgmpsGroupMemberPort14_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 40, 1, 19),
    _IgmpsGroupMemberPort14_Type()
)
igmpsGroupMemberPort14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpsGroupMemberPort14.setStatus("current")


class _IgmpsGroupMemberPort15_Type(Integer32):
    """Custom type igmpsGroupMemberPort15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_IgmpsGroupMemberPort15_Type.__name__ = "Integer32"
_IgmpsGroupMemberPort15_Object = MibTableColumn
igmpsGroupMemberPort15 = _IgmpsGroupMemberPort15_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 40, 1, 20),
    _IgmpsGroupMemberPort15_Type()
)
igmpsGroupMemberPort15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpsGroupMemberPort15.setStatus("current")


class _IgmpsGroupMemberPort16_Type(Integer32):
    """Custom type igmpsGroupMemberPort16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_IgmpsGroupMemberPort16_Type.__name__ = "Integer32"
_IgmpsGroupMemberPort16_Object = MibTableColumn
igmpsGroupMemberPort16 = _IgmpsGroupMemberPort16_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 40, 1, 21),
    _IgmpsGroupMemberPort16_Type()
)
igmpsGroupMemberPort16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpsGroupMemberPort16.setStatus("current")


class _IgmpsGroupMemberPort17_Type(Integer32):
    """Custom type igmpsGroupMemberPort17 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_IgmpsGroupMemberPort17_Type.__name__ = "Integer32"
_IgmpsGroupMemberPort17_Object = MibTableColumn
igmpsGroupMemberPort17 = _IgmpsGroupMemberPort17_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 40, 1, 22),
    _IgmpsGroupMemberPort17_Type()
)
igmpsGroupMemberPort17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpsGroupMemberPort17.setStatus("current")


class _IgmpsGroupMemberPort18_Type(Integer32):
    """Custom type igmpsGroupMemberPort18 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_IgmpsGroupMemberPort18_Type.__name__ = "Integer32"
_IgmpsGroupMemberPort18_Object = MibTableColumn
igmpsGroupMemberPort18 = _IgmpsGroupMemberPort18_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 40, 1, 23),
    _IgmpsGroupMemberPort18_Type()
)
igmpsGroupMemberPort18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpsGroupMemberPort18.setStatus("current")


class _IgmpsGroupMemberPort19_Type(Integer32):
    """Custom type igmpsGroupMemberPort19 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_IgmpsGroupMemberPort19_Type.__name__ = "Integer32"
_IgmpsGroupMemberPort19_Object = MibTableColumn
igmpsGroupMemberPort19 = _IgmpsGroupMemberPort19_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 40, 1, 24),
    _IgmpsGroupMemberPort19_Type()
)
igmpsGroupMemberPort19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpsGroupMemberPort19.setStatus("current")


class _IgmpsGroupMemberPort20_Type(Integer32):
    """Custom type igmpsGroupMemberPort20 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_IgmpsGroupMemberPort20_Type.__name__ = "Integer32"
_IgmpsGroupMemberPort20_Object = MibTableColumn
igmpsGroupMemberPort20 = _IgmpsGroupMemberPort20_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 40, 1, 25),
    _IgmpsGroupMemberPort20_Type()
)
igmpsGroupMemberPort20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpsGroupMemberPort20.setStatus("current")


class _IgmpsGroupMemberPort21_Type(Integer32):
    """Custom type igmpsGroupMemberPort21 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_IgmpsGroupMemberPort21_Type.__name__ = "Integer32"
_IgmpsGroupMemberPort21_Object = MibTableColumn
igmpsGroupMemberPort21 = _IgmpsGroupMemberPort21_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 40, 1, 26),
    _IgmpsGroupMemberPort21_Type()
)
igmpsGroupMemberPort21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpsGroupMemberPort21.setStatus("current")


class _IgmpsGroupMemberPort22_Type(Integer32):
    """Custom type igmpsGroupMemberPort22 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_IgmpsGroupMemberPort22_Type.__name__ = "Integer32"
_IgmpsGroupMemberPort22_Object = MibTableColumn
igmpsGroupMemberPort22 = _IgmpsGroupMemberPort22_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 40, 1, 27),
    _IgmpsGroupMemberPort22_Type()
)
igmpsGroupMemberPort22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpsGroupMemberPort22.setStatus("current")


class _IgmpsGroupMemberPort23_Type(Integer32):
    """Custom type igmpsGroupMemberPort23 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_IgmpsGroupMemberPort23_Type.__name__ = "Integer32"
_IgmpsGroupMemberPort23_Object = MibTableColumn
igmpsGroupMemberPort23 = _IgmpsGroupMemberPort23_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 40, 1, 28),
    _IgmpsGroupMemberPort23_Type()
)
igmpsGroupMemberPort23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpsGroupMemberPort23.setStatus("current")


class _IgmpsGroupMemberPort24_Type(Integer32):
    """Custom type igmpsGroupMemberPort24 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unsupported", 255),
          ("yes", 1))
    )


_IgmpsGroupMemberPort24_Type.__name__ = "Integer32"
_IgmpsGroupMemberPort24_Object = MibTableColumn
igmpsGroupMemberPort24 = _IgmpsGroupMemberPort24_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 13, 40, 1, 29),
    _IgmpsGroupMemberPort24_Type()
)
igmpsGroupMemberPort24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpsGroupMemberPort24.setStatus("current")
_Rtc_ObjectIdentity = ObjectIdentity
rtc = _Rtc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 15)
)


class _RtcSupport_Type(Integer32):
    """Custom type rtcSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 255))
    )


_RtcSupport_Type.__name__ = "Integer32"
_RtcSupport_Object = MibScalar
rtcSupport = _RtcSupport_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 15, 1),
    _RtcSupport_Type()
)
rtcSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcSupport.setStatus("current")


class _RtcFlags_Type(Integer32):
    """Custom type rtcFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("dstenabled", 2),
          ("sntpenabled", 1),
          ("unsupported", 255))
    )


_RtcFlags_Type.__name__ = "Integer32"
_RtcFlags_Object = MibScalar
rtcFlags = _RtcFlags_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 15, 2),
    _RtcFlags_Type()
)
rtcFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtcFlags.setStatus("current")


class _RtcLocalTime_Type(DisplayString):
    """Custom type rtcLocalTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(25, 25),
    )


_RtcLocalTime_Type.__name__ = "DisplayString"
_RtcLocalTime_Object = MibScalar
rtcLocalTime = _RtcLocalTime_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 15, 3),
    _RtcLocalTime_Type()
)
rtcLocalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcLocalTime.setStatus("current")


class _RtcManualTime_Type(DisplayString):
    """Custom type rtcManualTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(25, 25),
    )


_RtcManualTime_Type.__name__ = "DisplayString"
_RtcManualTime_Object = MibScalar
rtcManualTime = _RtcManualTime_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 15, 4),
    _RtcManualTime_Type()
)
rtcManualTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtcManualTime.setStatus("current")


class _RtcTimeStatus_Type(Integer32):
    """Custom type rtcTimeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("manuallyset", 2),
          ("synchronized", 3),
          ("unset", 1),
          ("unsupported", 255),
          ("unsynchronized", 4))
    )


_RtcTimeStatus_Type.__name__ = "Integer32"
_RtcTimeStatus_Object = MibScalar
rtcTimeStatus = _RtcTimeStatus_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 15, 5),
    _RtcTimeStatus_Type()
)
rtcTimeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcTimeStatus.setStatus("current")


class _RtcTimezoneOffset_Type(Integer32):
    """Custom type rtcTimezoneOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-24, 24),
    )


_RtcTimezoneOffset_Type.__name__ = "Integer32"
_RtcTimezoneOffset_Object = MibScalar
rtcTimezoneOffset = _RtcTimezoneOffset_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 15, 6),
    _RtcTimezoneOffset_Type()
)
rtcTimezoneOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtcTimezoneOffset.setStatus("current")


class _RtcDSTOffset_Type(Integer32):
    """Custom type rtcDSTOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 120),
    )


_RtcDSTOffset_Type.__name__ = "Integer32"
_RtcDSTOffset_Object = MibScalar
rtcDSTOffset = _RtcDSTOffset_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 15, 7),
    _RtcDSTOffset_Type()
)
rtcDSTOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtcDSTOffset.setStatus("current")


class _RtcDSTbegin_Type(OctetString):
    """Custom type rtcDSTbegin based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_RtcDSTbegin_Type.__name__ = "OctetString"
_RtcDSTbegin_Object = MibScalar
rtcDSTbegin = _RtcDSTbegin_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 15, 8),
    _RtcDSTbegin_Type()
)
rtcDSTbegin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtcDSTbegin.setStatus("current")


class _RtcDSTend_Type(OctetString):
    """Custom type rtcDSTend based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_RtcDSTend_Type.__name__ = "OctetString"
_RtcDSTend_Object = MibScalar
rtcDSTend = _RtcDSTend_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 15, 9),
    _RtcDSTend_Type()
)
rtcDSTend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtcDSTend.setStatus("current")


class _RtcDSTstatus_Type(Integer32):
    """Custom type rtcDSTstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("isdst", 1),
          ("isnotdst", 2),
          ("unsupported", 255))
    )


_RtcDSTstatus_Type.__name__ = "Integer32"
_RtcDSTstatus_Object = MibScalar
rtcDSTstatus = _RtcDSTstatus_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 15, 10),
    _RtcDSTstatus_Type()
)
rtcDSTstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcDSTstatus.setStatus("current")
_RtcSNTPsyncInterval_Type = Integer32
_RtcSNTPsyncInterval_Object = MibScalar
rtcSNTPsyncInterval = _RtcSNTPsyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 15, 11),
    _RtcSNTPsyncInterval_Type()
)
rtcSNTPsyncInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtcSNTPsyncInterval.setStatus("current")


class _RtcSNTPsyncNow_Type(Integer32):
    """Custom type rtcSNTPsyncNow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("normalOperation", 0),
          ("syncNow", 1),
          ("unsupported", 255))
    )


_RtcSNTPsyncNow_Type.__name__ = "Integer32"
_RtcSNTPsyncNow_Object = MibScalar
rtcSNTPsyncNow = _RtcSNTPsyncNow_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 15, 12),
    _RtcSNTPsyncNow_Type()
)
rtcSNTPsyncNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtcSNTPsyncNow.setStatus("current")


class _RtcSNTPServerCount_Type(Integer32):
    """Custom type rtcSNTPServerCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_RtcSNTPServerCount_Type.__name__ = "Integer32"
_RtcSNTPServerCount_Object = MibScalar
rtcSNTPServerCount = _RtcSNTPServerCount_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 15, 13),
    _RtcSNTPServerCount_Type()
)
rtcSNTPServerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcSNTPServerCount.setStatus("current")
_RtcSNTPServerTable_Object = MibTable
rtcSNTPServerTable = _RtcSNTPServerTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 15, 20)
)
if mibBuilder.loadTexts:
    rtcSNTPServerTable.setStatus("current")
_RtcSNTPServerTableEntry_Object = MibTableRow
rtcSNTPServerTableEntry = _RtcSNTPServerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 15, 20, 1)
)
rtcSNTPServerTableEntry.setIndexNames(
    (0, "MS-SWITCH30-MIB", "rtcSNTPServerId"),
)
if mibBuilder.loadTexts:
    rtcSNTPServerTableEntry.setStatus("current")


class _RtcSNTPServerId_Type(Integer32):
    """Custom type rtcSNTPServerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_RtcSNTPServerId_Type.__name__ = "Integer32"
_RtcSNTPServerId_Object = MibTableColumn
rtcSNTPServerId = _RtcSNTPServerId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 15, 20, 1, 1),
    _RtcSNTPServerId_Type()
)
rtcSNTPServerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcSNTPServerId.setStatus("current")


class _RtcSNTPServerStatus_Type(Integer32):
    """Custom type rtcSNTPServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              7,
              255)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 5),
          ("busy", 1),
          ("nomemory", 3),
          ("ok", 0),
          ("portbusy", 4),
          ("timeout", 2),
          ("unknown", 7),
          ("unsupported", 255))
    )


_RtcSNTPServerStatus_Type.__name__ = "Integer32"
_RtcSNTPServerStatus_Object = MibTableColumn
rtcSNTPServerStatus = _RtcSNTPServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 15, 20, 1, 2),
    _RtcSNTPServerStatus_Type()
)
rtcSNTPServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcSNTPServerStatus.setStatus("current")


class _RtcSNTPServerEnable_Type(Integer32):
    """Custom type rtcSNTPServerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_RtcSNTPServerEnable_Type.__name__ = "Integer32"
_RtcSNTPServerEnable_Object = MibTableColumn
rtcSNTPServerEnable = _RtcSNTPServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 15, 20, 1, 3),
    _RtcSNTPServerEnable_Type()
)
rtcSNTPServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtcSNTPServerEnable.setStatus("current")
_RtcSNTPServerIpAddress_Type = IpAddress
_RtcSNTPServerIpAddress_Object = MibTableColumn
rtcSNTPServerIpAddress = _RtcSNTPServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 15, 20, 1, 4),
    _RtcSNTPServerIpAddress_Type()
)
rtcSNTPServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtcSNTPServerIpAddress.setStatus("current")
_Consoleinterface_ObjectIdentity = ObjectIdentity
consoleinterface = _Consoleinterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 20)
)


class _ConsoleSupport_Type(Integer32):
    """Custom type consoleSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ConsoleSupport_Type.__name__ = "Integer32"
_ConsoleSupport_Object = MibScalar
consoleSupport = _ConsoleSupport_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 20, 1),
    _ConsoleSupport_Type()
)
consoleSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consoleSupport.setStatus("current")


class _ConsoleEnable_Type(Integer32):
    """Custom type consoleEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ConsoleEnable_Type.__name__ = "Integer32"
_ConsoleEnable_Object = MibScalar
consoleEnable = _ConsoleEnable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 20, 2),
    _ConsoleEnable_Type()
)
consoleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleEnable.setStatus("current")
_ConsoleTimeout_Type = Integer32
_ConsoleTimeout_Object = MibScalar
consoleTimeout = _ConsoleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 20, 3),
    _ConsoleTimeout_Type()
)
consoleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleTimeout.setStatus("current")


class _ConsoleApplyMode_Type(Integer32):
    """Custom type consoleApplyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("applyAndSaveImmediately", 1),
          ("applyAndSaveManually", 3),
          ("saveManually", 2))
    )


_ConsoleApplyMode_Type.__name__ = "Integer32"
_ConsoleApplyMode_Object = MibScalar
consoleApplyMode = _ConsoleApplyMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 20, 4),
    _ConsoleApplyMode_Type()
)
consoleApplyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleApplyMode.setStatus("current")


class _ConsolePrompt_Type(DisplayString):
    """Custom type consolePrompt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ConsolePrompt_Type.__name__ = "DisplayString"
_ConsolePrompt_Object = MibScalar
consolePrompt = _ConsolePrompt_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 20, 5),
    _ConsolePrompt_Type()
)
consolePrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consolePrompt.setStatus("current")
_Webinterface_ObjectIdentity = ObjectIdentity
webinterface = _Webinterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 21)
)


class _WebSupport_Type(Integer32):
    """Custom type webSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_WebSupport_Type.__name__ = "Integer32"
_WebSupport_Object = MibScalar
webSupport = _WebSupport_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 21, 1),
    _WebSupport_Type()
)
webSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webSupport.setStatus("current")


class _WebEnable_Type(Integer32):
    """Custom type webEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_WebEnable_Type.__name__ = "Integer32"
_WebEnable_Object = MibScalar
webEnable = _WebEnable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 21, 2),
    _WebEnable_Type()
)
webEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webEnable.setStatus("current")
_Snmpinterface_ObjectIdentity = ObjectIdentity
snmpinterface = _Snmpinterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 22)
)


class _SnmpSupport_Type(Integer32):
    """Custom type snmpSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SnmpSupport_Type.__name__ = "Integer32"
_SnmpSupport_Object = MibScalar
snmpSupport = _SnmpSupport_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 22, 1),
    _SnmpSupport_Type()
)
snmpSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpSupport.setStatus("current")


class _SnmpEnable_Type(Integer32):
    """Custom type snmpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SnmpEnable_Type.__name__ = "Integer32"
_SnmpEnable_Object = MibScalar
snmpEnable = _SnmpEnable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 22, 2),
    _SnmpEnable_Type()
)
snmpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpEnable.setStatus("current")


class _SnmpApplyMode_Type(Integer32):
    """Custom type snmpApplyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("applyAndSaveImmediately", 1),
          ("applyAndSaveManually", 3),
          ("saveManually", 2))
    )


_SnmpApplyMode_Type.__name__ = "Integer32"
_SnmpApplyMode_Object = MibScalar
snmpApplyMode = _SnmpApplyMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 22, 3),
    _SnmpApplyMode_Type()
)
snmpApplyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpApplyMode.setStatus("current")


class _SnmpApply_Type(Integer32):
    """Custom type snmpApply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("applyAndSaveNow", 2),
          ("applyNow", 1),
          ("normalOperation", 0))
    )


_SnmpApply_Type.__name__ = "Integer32"
_SnmpApply_Object = MibScalar
snmpApply = _SnmpApply_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 22, 4),
    _SnmpApply_Type()
)
snmpApply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpApply.setStatus("current")


class _SnmpTrapTest_Type(Integer32):
    """Custom type snmpTrapTest based on Integer32"""
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
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              255)
        )
    )
    namedValues = NamedValues(
        *(("entAccesspermission", 21),
          ("entAuthpwfail", 19),
          ("entErrorcounter", 10),
          ("entFactoryreset", 8),
          ("entLinkchange", 7),
          ("entLoginfailure", 16),
          ("entOverundervoltage", 11),
          ("entPoelimitexceeded", 13),
          ("entPrivpwfail", 20),
          ("entRingalarm", 18),
          ("entRingbroken", 17),
          ("entSeclevelfail", 22),
          ("entSfpplugchange", 15),
          ("entSupplystatuschange", 14),
          ("entTemplevelchange", 9),
          ("entTempshutdown", 12),
          ("genAuthfailure", 5),
          ("genColdstart", 1),
          ("genEgpneighborloss", 6),
          ("genLinkdown", 3),
          ("genLinkup", 4),
          ("genWarmstart", 2),
          ("inactive", 0),
          ("unsupported", 255))
    )


_SnmpTrapTest_Type.__name__ = "Integer32"
_SnmpTrapTest_Object = MibScalar
snmpTrapTest = _SnmpTrapTest_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 22, 5),
    _SnmpTrapTest_Type()
)
snmpTrapTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapTest.setStatus("current")
_SnmpTrapDestCount_Type = Integer32
_SnmpTrapDestCount_Object = MibScalar
snmpTrapDestCount = _SnmpTrapDestCount_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 22, 6),
    _SnmpTrapDestCount_Type()
)
snmpTrapDestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTrapDestCount.setStatus("current")


class _SnmpCommunityRead_Type(DisplayString):
    """Custom type snmpCommunityRead based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SnmpCommunityRead_Type.__name__ = "DisplayString"
_SnmpCommunityRead_Object = MibScalar
snmpCommunityRead = _SnmpCommunityRead_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 22, 7),
    _SnmpCommunityRead_Type()
)
snmpCommunityRead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpCommunityRead.setStatus("current")


class _SnmpCommunityWrite_Type(DisplayString):
    """Custom type snmpCommunityWrite based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SnmpCommunityWrite_Type.__name__ = "DisplayString"
_SnmpCommunityWrite_Object = MibScalar
snmpCommunityWrite = _SnmpCommunityWrite_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 22, 8),
    _SnmpCommunityWrite_Type()
)
snmpCommunityWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpCommunityWrite.setStatus("current")


class _SnmpTrapEnable_Type(Integer32):
    """Custom type snmpTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_SnmpTrapEnable_Type.__name__ = "Integer32"
_SnmpTrapEnable_Object = MibScalar
snmpTrapEnable = _SnmpTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 22, 9),
    _SnmpTrapEnable_Type()
)
snmpTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapEnable.setStatus("current")
_SnmpTrapDestTable_Object = MibTable
snmpTrapDestTable = _SnmpTrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 22, 10)
)
if mibBuilder.loadTexts:
    snmpTrapDestTable.setStatus("current")
_SnmpTrapDestTableEntry_Object = MibTableRow
snmpTrapDestTableEntry = _SnmpTrapDestTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 22, 10, 1)
)
snmpTrapDestTableEntry.setIndexNames(
    (0, "MS-SWITCH30-MIB", "snmpTrapDestId"),
)
if mibBuilder.loadTexts:
    snmpTrapDestTableEntry.setStatus("current")


class _SnmpTrapDestId_Type(Integer32):
    """Custom type snmpTrapDestId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SnmpTrapDestId_Type.__name__ = "Integer32"
_SnmpTrapDestId_Object = MibTableColumn
snmpTrapDestId = _SnmpTrapDestId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 22, 10, 1, 1),
    _SnmpTrapDestId_Type()
)
snmpTrapDestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTrapDestId.setStatus("current")


class _SnmpTrapDestAlias_Type(DisplayString):
    """Custom type snmpTrapDestAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SnmpTrapDestAlias_Type.__name__ = "DisplayString"
_SnmpTrapDestAlias_Object = MibTableColumn
snmpTrapDestAlias = _SnmpTrapDestAlias_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 22, 10, 1, 2),
    _SnmpTrapDestAlias_Type()
)
snmpTrapDestAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapDestAlias.setStatus("current")


class _SnmpTrapDestEn_Type(Integer32):
    """Custom type snmpTrapDestEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("unsupported", 255),
          ("v1", 1),
          ("v2C", 2),
          ("v3", 3))
    )


_SnmpTrapDestEn_Type.__name__ = "Integer32"
_SnmpTrapDestEn_Object = MibTableColumn
snmpTrapDestEn = _SnmpTrapDestEn_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 22, 10, 1, 3),
    _SnmpTrapDestEn_Type()
)
snmpTrapDestEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapDestEn.setStatus("current")
_SnmpTrapDestIP_Type = IpAddress
_SnmpTrapDestIP_Object = MibTableColumn
snmpTrapDestIP = _SnmpTrapDestIP_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 22, 10, 1, 4),
    _SnmpTrapDestIP_Type()
)
snmpTrapDestIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapDestIP.setStatus("current")


class _SnmpTrapDestCommunity_Type(DisplayString):
    """Custom type snmpTrapDestCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SnmpTrapDestCommunity_Type.__name__ = "DisplayString"
_SnmpTrapDestCommunity_Object = MibTableColumn
snmpTrapDestCommunity = _SnmpTrapDestCommunity_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 22, 10, 1, 5),
    _SnmpTrapDestCommunity_Type()
)
snmpTrapDestCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapDestCommunity.setStatus("current")


class _SnmpTrapGenColdstart_Type(Integer32):
    """Custom type snmpTrapGenColdstart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_SnmpTrapGenColdstart_Type.__name__ = "Integer32"
_SnmpTrapGenColdstart_Object = MibTableColumn
snmpTrapGenColdstart = _SnmpTrapGenColdstart_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 22, 10, 1, 6),
    _SnmpTrapGenColdstart_Type()
)
snmpTrapGenColdstart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapGenColdstart.setStatus("current")


class _SnmpTrapGenWarmstart_Type(Integer32):
    """Custom type snmpTrapGenWarmstart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_SnmpTrapGenWarmstart_Type.__name__ = "Integer32"
_SnmpTrapGenWarmstart_Object = MibTableColumn
snmpTrapGenWarmstart = _SnmpTrapGenWarmstart_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 22, 10, 1, 7),
    _SnmpTrapGenWarmstart_Type()
)
snmpTrapGenWarmstart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTrapGenWarmstart.setStatus("current")


class _SnmpTrapGenLinkDown_Type(Integer32):
    """Custom type snmpTrapGenLinkDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_SnmpTrapGenLinkDown_Type.__name__ = "Integer32"
_SnmpTrapGenLinkDown_Object = MibTableColumn
snmpTrapGenLinkDown = _SnmpTrapGenLinkDown_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 22, 10, 1, 8),
    _SnmpTrapGenLinkDown_Type()
)
snmpTrapGenLinkDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapGenLinkDown.setStatus("current")


class _SnmpTrapGenLinkUp_Type(Integer32):
    """Custom type snmpTrapGenLinkUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_SnmpTrapGenLinkUp_Type.__name__ = "Integer32"
_SnmpTrapGenLinkUp_Object = MibTableColumn
snmpTrapGenLinkUp = _SnmpTrapGenLinkUp_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 22, 10, 1, 9),
    _SnmpTrapGenLinkUp_Type()
)
snmpTrapGenLinkUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapGenLinkUp.setStatus("current")


class _SnmpTrapGenAuthFailure_Type(Integer32):
    """Custom type snmpTrapGenAuthFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_SnmpTrapGenAuthFailure_Type.__name__ = "Integer32"
_SnmpTrapGenAuthFailure_Object = MibTableColumn
snmpTrapGenAuthFailure = _SnmpTrapGenAuthFailure_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 22, 10, 1, 10),
    _SnmpTrapGenAuthFailure_Type()
)
snmpTrapGenAuthFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapGenAuthFailure.setStatus("current")


class _SnmpTrapGenEgpNeighborLoss_Type(Integer32):
    """Custom type snmpTrapGenEgpNeighborLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_SnmpTrapGenEgpNeighborLoss_Type.__name__ = "Integer32"
_SnmpTrapGenEgpNeighborLoss_Object = MibTableColumn
snmpTrapGenEgpNeighborLoss = _SnmpTrapGenEgpNeighborLoss_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 22, 10, 1, 11),
    _SnmpTrapGenEgpNeighborLoss_Type()
)
snmpTrapGenEgpNeighborLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTrapGenEgpNeighborLoss.setStatus("current")


class _SnmpTrapEntLinkChange_Type(Integer32):
    """Custom type snmpTrapEntLinkChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_SnmpTrapEntLinkChange_Type.__name__ = "Integer32"
_SnmpTrapEntLinkChange_Object = MibTableColumn
snmpTrapEntLinkChange = _SnmpTrapEntLinkChange_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 22, 10, 1, 12),
    _SnmpTrapEntLinkChange_Type()
)
snmpTrapEntLinkChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapEntLinkChange.setStatus("current")


class _SnmpTrapEntFactoryReset_Type(Integer32):
    """Custom type snmpTrapEntFactoryReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_SnmpTrapEntFactoryReset_Type.__name__ = "Integer32"
_SnmpTrapEntFactoryReset_Object = MibTableColumn
snmpTrapEntFactoryReset = _SnmpTrapEntFactoryReset_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 22, 10, 1, 13),
    _SnmpTrapEntFactoryReset_Type()
)
snmpTrapEntFactoryReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapEntFactoryReset.setStatus("current")


class _SnmpTrapEntTemperatureLevelChange_Type(Integer32):
    """Custom type snmpTrapEntTemperatureLevelChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_SnmpTrapEntTemperatureLevelChange_Type.__name__ = "Integer32"
_SnmpTrapEntTemperatureLevelChange_Object = MibTableColumn
snmpTrapEntTemperatureLevelChange = _SnmpTrapEntTemperatureLevelChange_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 22, 10, 1, 14),
    _SnmpTrapEntTemperatureLevelChange_Type()
)
snmpTrapEntTemperatureLevelChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapEntTemperatureLevelChange.setStatus("current")


class _SnmpTrapEntErrorCounter_Type(Integer32):
    """Custom type snmpTrapEntErrorCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_SnmpTrapEntErrorCounter_Type.__name__ = "Integer32"
_SnmpTrapEntErrorCounter_Object = MibTableColumn
snmpTrapEntErrorCounter = _SnmpTrapEntErrorCounter_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 22, 10, 1, 15),
    _SnmpTrapEntErrorCounter_Type()
)
snmpTrapEntErrorCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapEntErrorCounter.setStatus("current")


class _SnmpTrapEntUnderOverVoltage_Type(Integer32):
    """Custom type snmpTrapEntUnderOverVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_SnmpTrapEntUnderOverVoltage_Type.__name__ = "Integer32"
_SnmpTrapEntUnderOverVoltage_Object = MibTableColumn
snmpTrapEntUnderOverVoltage = _SnmpTrapEntUnderOverVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 22, 10, 1, 16),
    _SnmpTrapEntUnderOverVoltage_Type()
)
snmpTrapEntUnderOverVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapEntUnderOverVoltage.setStatus("current")


class _SnmpTrapEntTempShutDown_Type(Integer32):
    """Custom type snmpTrapEntTempShutDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_SnmpTrapEntTempShutDown_Type.__name__ = "Integer32"
_SnmpTrapEntTempShutDown_Object = MibTableColumn
snmpTrapEntTempShutDown = _SnmpTrapEntTempShutDown_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 22, 10, 1, 17),
    _SnmpTrapEntTempShutDown_Type()
)
snmpTrapEntTempShutDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapEntTempShutDown.setStatus("current")


class _SnmpTrapEntPoeLimitExceeded_Type(Integer32):
    """Custom type snmpTrapEntPoeLimitExceeded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_SnmpTrapEntPoeLimitExceeded_Type.__name__ = "Integer32"
_SnmpTrapEntPoeLimitExceeded_Object = MibTableColumn
snmpTrapEntPoeLimitExceeded = _SnmpTrapEntPoeLimitExceeded_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 22, 10, 1, 18),
    _SnmpTrapEntPoeLimitExceeded_Type()
)
snmpTrapEntPoeLimitExceeded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapEntPoeLimitExceeded.setStatus("current")


class _SnmpTrapEntSupplyStatusChange_Type(Integer32):
    """Custom type snmpTrapEntSupplyStatusChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_SnmpTrapEntSupplyStatusChange_Type.__name__ = "Integer32"
_SnmpTrapEntSupplyStatusChange_Object = MibTableColumn
snmpTrapEntSupplyStatusChange = _SnmpTrapEntSupplyStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 22, 10, 1, 19),
    _SnmpTrapEntSupplyStatusChange_Type()
)
snmpTrapEntSupplyStatusChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapEntSupplyStatusChange.setStatus("current")


class _SnmpTrapEntSfpPlugChange_Type(Integer32):
    """Custom type snmpTrapEntSfpPlugChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_SnmpTrapEntSfpPlugChange_Type.__name__ = "Integer32"
_SnmpTrapEntSfpPlugChange_Object = MibTableColumn
snmpTrapEntSfpPlugChange = _SnmpTrapEntSfpPlugChange_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 22, 10, 1, 20),
    _SnmpTrapEntSfpPlugChange_Type()
)
snmpTrapEntSfpPlugChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapEntSfpPlugChange.setStatus("current")


class _SnmpTrapEntLoginFailure_Type(Integer32):
    """Custom type snmpTrapEntLoginFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_SnmpTrapEntLoginFailure_Type.__name__ = "Integer32"
_SnmpTrapEntLoginFailure_Object = MibTableColumn
snmpTrapEntLoginFailure = _SnmpTrapEntLoginFailure_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 22, 10, 1, 21),
    _SnmpTrapEntLoginFailure_Type()
)
snmpTrapEntLoginFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapEntLoginFailure.setStatus("current")


class _SnmpTrapEntRingBroken_Type(Integer32):
    """Custom type snmpTrapEntRingBroken based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_SnmpTrapEntRingBroken_Type.__name__ = "Integer32"
_SnmpTrapEntRingBroken_Object = MibTableColumn
snmpTrapEntRingBroken = _SnmpTrapEntRingBroken_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 22, 10, 1, 22),
    _SnmpTrapEntRingBroken_Type()
)
snmpTrapEntRingBroken.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapEntRingBroken.setStatus("current")


class _SnmpTrapEntRingAlarm_Type(Integer32):
    """Custom type snmpTrapEntRingAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_SnmpTrapEntRingAlarm_Type.__name__ = "Integer32"
_SnmpTrapEntRingAlarm_Object = MibTableColumn
snmpTrapEntRingAlarm = _SnmpTrapEntRingAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 22, 10, 1, 23),
    _SnmpTrapEntRingAlarm_Type()
)
snmpTrapEntRingAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapEntRingAlarm.setStatus("current")


class _SnmpTrapEntAuthPwFail_Type(Integer32):
    """Custom type snmpTrapEntAuthPwFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_SnmpTrapEntAuthPwFail_Type.__name__ = "Integer32"
_SnmpTrapEntAuthPwFail_Object = MibTableColumn
snmpTrapEntAuthPwFail = _SnmpTrapEntAuthPwFail_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 22, 10, 1, 24),
    _SnmpTrapEntAuthPwFail_Type()
)
snmpTrapEntAuthPwFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapEntAuthPwFail.setStatus("current")


class _SnmpTrapEntPrivPwFail_Type(Integer32):
    """Custom type snmpTrapEntPrivPwFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_SnmpTrapEntPrivPwFail_Type.__name__ = "Integer32"
_SnmpTrapEntPrivPwFail_Object = MibTableColumn
snmpTrapEntPrivPwFail = _SnmpTrapEntPrivPwFail_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 22, 10, 1, 25),
    _SnmpTrapEntPrivPwFail_Type()
)
snmpTrapEntPrivPwFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapEntPrivPwFail.setStatus("current")


class _SnmpTrapEntAccessPermission_Type(Integer32):
    """Custom type snmpTrapEntAccessPermission based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_SnmpTrapEntAccessPermission_Type.__name__ = "Integer32"
_SnmpTrapEntAccessPermission_Object = MibTableColumn
snmpTrapEntAccessPermission = _SnmpTrapEntAccessPermission_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 22, 10, 1, 26),
    _SnmpTrapEntAccessPermission_Type()
)
snmpTrapEntAccessPermission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapEntAccessPermission.setStatus("current")


class _SnmpTrapEntSeclevelFail_Type(Integer32):
    """Custom type snmpTrapEntSeclevelFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_SnmpTrapEntSeclevelFail_Type.__name__ = "Integer32"
_SnmpTrapEntSeclevelFail_Object = MibTableColumn
snmpTrapEntSeclevelFail = _SnmpTrapEntSeclevelFail_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 22, 10, 1, 27),
    _SnmpTrapEntSeclevelFail_Type()
)
snmpTrapEntSeclevelFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapEntSeclevelFail.setStatus("current")
_Udpinterface_ObjectIdentity = ObjectIdentity
udpinterface = _Udpinterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 23)
)


class _UdpSupport_Type(Integer32):
    """Custom type udpSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 255))
    )


_UdpSupport_Type.__name__ = "Integer32"
_UdpSupport_Object = MibScalar
udpSupport = _UdpSupport_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 23, 1),
    _UdpSupport_Type()
)
udpSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpSupport.setStatus("current")


class _UdpEnable_Type(Integer32):
    """Custom type udpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_UdpEnable_Type.__name__ = "Integer32"
_UdpEnable_Object = MibScalar
udpEnable = _UdpEnable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 23, 2),
    _UdpEnable_Type()
)
udpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    udpEnable.setStatus("current")
_Syslog_ObjectIdentity = ObjectIdentity
syslog = _Syslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 24)
)


class _SyslogSupport_Type(Integer32):
    """Custom type syslogSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 255))
    )


_SyslogSupport_Type.__name__ = "Integer32"
_SyslogSupport_Object = MibScalar
syslogSupport = _SyslogSupport_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 24, 1),
    _SyslogSupport_Type()
)
syslogSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogSupport.setStatus("current")


class _SyslogEnable_Type(Integer32):
    """Custom type syslogEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_SyslogEnable_Type.__name__ = "Integer32"
_SyslogEnable_Object = MibScalar
syslogEnable = _SyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 24, 2),
    _SyslogEnable_Type()
)
syslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogEnable.setStatus("current")


class _SyslogMessageTest_Type(Integer32):
    """Custom type syslogMessageTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("sendmessage", 1),
          ("unsupported", 255))
    )


_SyslogMessageTest_Type.__name__ = "Integer32"
_SyslogMessageTest_Object = MibScalar
syslogMessageTest = _SyslogMessageTest_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 24, 3),
    _SyslogMessageTest_Type()
)
syslogMessageTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogMessageTest.setStatus("current")
_SyslogDestCount_Type = Integer32
_SyslogDestCount_Object = MibScalar
syslogDestCount = _SyslogDestCount_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 24, 4),
    _SyslogDestCount_Type()
)
syslogDestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogDestCount.setStatus("current")
_SyslogDestTable_Object = MibTable
syslogDestTable = _SyslogDestTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 24, 10)
)
if mibBuilder.loadTexts:
    syslogDestTable.setStatus("current")
_SyslogDestTableEntry_Object = MibTableRow
syslogDestTableEntry = _SyslogDestTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 24, 10, 1)
)
syslogDestTableEntry.setIndexNames(
    (0, "MS-SWITCH30-MIB", "syslogDestId"),
)
if mibBuilder.loadTexts:
    syslogDestTableEntry.setStatus("current")


class _SyslogDestId_Type(Integer32):
    """Custom type syslogDestId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SyslogDestId_Type.__name__ = "Integer32"
_SyslogDestId_Object = MibTableColumn
syslogDestId = _SyslogDestId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 24, 10, 1, 1),
    _SyslogDestId_Type()
)
syslogDestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogDestId.setStatus("current")


class _SyslogDestAlias_Type(DisplayString):
    """Custom type syslogDestAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SyslogDestAlias_Type.__name__ = "DisplayString"
_SyslogDestAlias_Object = MibTableColumn
syslogDestAlias = _SyslogDestAlias_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 24, 10, 1, 2),
    _SyslogDestAlias_Type()
)
syslogDestAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogDestAlias.setStatus("current")


class _SyslogDestEnable_Type(Integer32):
    """Custom type syslogDestEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_SyslogDestEnable_Type.__name__ = "Integer32"
_SyslogDestEnable_Object = MibTableColumn
syslogDestEnable = _SyslogDestEnable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 24, 10, 1, 3),
    _SyslogDestEnable_Type()
)
syslogDestEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogDestEnable.setStatus("current")
_SyslogDestIpAddress_Type = IpAddress
_SyslogDestIpAddress_Object = MibTableColumn
syslogDestIpAddress = _SyslogDestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 24, 10, 1, 4),
    _SyslogDestIpAddress_Type()
)
syslogDestIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogDestIpAddress.setStatus("current")
_SyslogDestPort_Type = Integer32
_SyslogDestPort_Object = MibTableColumn
syslogDestPort = _SyslogDestPort_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 24, 10, 1, 5),
    _SyslogDestPort_Type()
)
syslogDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogDestPort.setStatus("current")


class _SyslogDestFacility_Type(Integer32):
    """Custom type syslogDestFacility based on Integer32"""
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
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("clockDeamon1", 9),
          ("clockDeamon2", 15),
          ("ftpDeamon", 11),
          ("kernelMessage", 0),
          ("linePrinterSubsystem", 6),
          ("localUse0", 16),
          ("localUse1", 17),
          ("localUse2", 18),
          ("localUse3", 19),
          ("localUse4", 20),
          ("localUse5", 21),
          ("localUse6", 22),
          ("localUse7", 23),
          ("logAlert", 14),
          ("logAudit", 13),
          ("mailSystem", 2),
          ("networkNewsSubsystem", 7),
          ("ntpSubsystem", 12),
          ("securityMessage1", 4),
          ("securityMessage2", 10),
          ("syslogdMessage", 5),
          ("systemDaemon", 3),
          ("userLevelMessage", 1),
          ("uucpSubsystem", 8))
    )


_SyslogDestFacility_Type.__name__ = "Integer32"
_SyslogDestFacility_Object = MibTableColumn
syslogDestFacility = _SyslogDestFacility_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 24, 10, 1, 6),
    _SyslogDestFacility_Type()
)
syslogDestFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogDestFacility.setStatus("current")


class _SyslogDestEventFilter_Type(Bits):
    """Custom type syslogDestEventFilter based on Bits"""
    namedValues = NamedValues(
        *(("configchange", 2),
          ("debug", 29),
          ("firmwareupdate", 4),
          ("linkchange", 1),
          ("login", 3),
          ("poe", 10),
          ("portauth", 6),
          ("powerredundancy", 5),
          ("reset", 0),
          ("ring", 8),
          ("rtc", 11),
          ("sfp", 9),
          ("statusreport", 30),
          ("temperature", 7),
          ("test", 31),
          ("vct", 12))
    )

_SyslogDestEventFilter_Type.__name__ = "Bits"
_SyslogDestEventFilter_Object = MibTableColumn
syslogDestEventFilter = _SyslogDestEventFilter_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 24, 10, 1, 7),
    _SyslogDestEventFilter_Type()
)
syslogDestEventFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogDestEventFilter.setStatus("current")
_Radius_ObjectIdentity = ObjectIdentity
radius = _Radius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 25)
)


class _RadiusSupport_Type(Integer32):
    """Custom type radiusSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 255))
    )


_RadiusSupport_Type.__name__ = "Integer32"
_RadiusSupport_Object = MibScalar
radiusSupport = _RadiusSupport_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 25, 1),
    _RadiusSupport_Type()
)
radiusSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusSupport.setStatus("current")


class _RadiusAccessEnable_Type(Integer32):
    """Custom type radiusAccessEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_RadiusAccessEnable_Type.__name__ = "Integer32"
_RadiusAccessEnable_Object = MibScalar
radiusAccessEnable = _RadiusAccessEnable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 25, 2),
    _RadiusAccessEnable_Type()
)
radiusAccessEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAccessEnable.setStatus("current")


class _RadiusAccountEnable_Type(Integer32):
    """Custom type radiusAccountEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_RadiusAccountEnable_Type.__name__ = "Integer32"
_RadiusAccountEnable_Object = MibScalar
radiusAccountEnable = _RadiusAccountEnable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 25, 3),
    _RadiusAccountEnable_Type()
)
radiusAccountEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAccountEnable.setStatus("current")
_RadiusServerCount_Type = Integer32
_RadiusServerCount_Object = MibScalar
radiusServerCount = _RadiusServerCount_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 25, 4),
    _RadiusServerCount_Type()
)
radiusServerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusServerCount.setStatus("current")


class _RadiusMacAuthPassword_Type(DisplayString):
    """Custom type radiusMacAuthPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RadiusMacAuthPassword_Type.__name__ = "DisplayString"
_RadiusMacAuthPassword_Object = MibScalar
radiusMacAuthPassword = _RadiusMacAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 25, 5),
    _RadiusMacAuthPassword_Type()
)
radiusMacAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusMacAuthPassword.setStatus("current")


class _RadiusUseMacAsPassword_Type(Integer32):
    """Custom type radiusUseMacAsPassword based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_RadiusUseMacAsPassword_Type.__name__ = "Integer32"
_RadiusUseMacAsPassword_Object = MibScalar
radiusUseMacAsPassword = _RadiusUseMacAsPassword_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 25, 6),
    _RadiusUseMacAsPassword_Type()
)
radiusUseMacAsPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusUseMacAsPassword.setStatus("current")


class _RadiusMacSeparator_Type(DisplayString):
    """Custom type radiusMacSeparator based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_RadiusMacSeparator_Type.__name__ = "DisplayString"
_RadiusMacSeparator_Object = MibScalar
radiusMacSeparator = _RadiusMacSeparator_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 25, 7),
    _RadiusMacSeparator_Type()
)
radiusMacSeparator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusMacSeparator.setStatus("current")


class _RadiusTimeout_Type(Integer32):
    """Custom type radiusTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RadiusTimeout_Type.__name__ = "Integer32"
_RadiusTimeout_Object = MibScalar
radiusTimeout = _RadiusTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 25, 8),
    _RadiusTimeout_Type()
)
radiusTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusTimeout.setStatus("current")
_RadiusServerTable_Object = MibTable
radiusServerTable = _RadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 25, 10)
)
if mibBuilder.loadTexts:
    radiusServerTable.setStatus("current")
_RadiusServerTableEntry_Object = MibTableRow
radiusServerTableEntry = _RadiusServerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 25, 10, 1)
)
radiusServerTableEntry.setIndexNames(
    (0, "MS-SWITCH30-MIB", "radiusServerId"),
)
if mibBuilder.loadTexts:
    radiusServerTableEntry.setStatus("current")


class _RadiusServerId_Type(Integer32):
    """Custom type radiusServerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RadiusServerId_Type.__name__ = "Integer32"
_RadiusServerId_Object = MibTableColumn
radiusServerId = _RadiusServerId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 25, 10, 1, 1),
    _RadiusServerId_Type()
)
radiusServerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusServerId.setStatus("current")


class _RadiusServerAlias_Type(DisplayString):
    """Custom type radiusServerAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RadiusServerAlias_Type.__name__ = "DisplayString"
_RadiusServerAlias_Object = MibTableColumn
radiusServerAlias = _RadiusServerAlias_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 25, 10, 1, 2),
    _RadiusServerAlias_Type()
)
radiusServerAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerAlias.setStatus("current")


class _RadiusServerEnableAccess_Type(Integer32):
    """Custom type radiusServerEnableAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_RadiusServerEnableAccess_Type.__name__ = "Integer32"
_RadiusServerEnableAccess_Object = MibTableColumn
radiusServerEnableAccess = _RadiusServerEnableAccess_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 25, 10, 1, 3),
    _RadiusServerEnableAccess_Type()
)
radiusServerEnableAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerEnableAccess.setStatus("current")


class _RadiusServerEnableAccount_Type(Integer32):
    """Custom type radiusServerEnableAccount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_RadiusServerEnableAccount_Type.__name__ = "Integer32"
_RadiusServerEnableAccount_Object = MibTableColumn
radiusServerEnableAccount = _RadiusServerEnableAccount_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 25, 10, 1, 4),
    _RadiusServerEnableAccount_Type()
)
radiusServerEnableAccount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerEnableAccount.setStatus("current")
_RadiusServerIpAddress_Type = IpAddress
_RadiusServerIpAddress_Object = MibTableColumn
radiusServerIpAddress = _RadiusServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 25, 10, 1, 5),
    _RadiusServerIpAddress_Type()
)
radiusServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerIpAddress.setStatus("current")
_RadiusServerAccessPort_Type = Integer32
_RadiusServerAccessPort_Object = MibTableColumn
radiusServerAccessPort = _RadiusServerAccessPort_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 25, 10, 1, 6),
    _RadiusServerAccessPort_Type()
)
radiusServerAccessPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerAccessPort.setStatus("current")
_RadiusServerAccountPort_Type = Integer32
_RadiusServerAccountPort_Object = MibTableColumn
radiusServerAccountPort = _RadiusServerAccountPort_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 25, 10, 1, 7),
    _RadiusServerAccountPort_Type()
)
radiusServerAccountPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerAccountPort.setStatus("current")


class _RadiusServerSecret_Type(DisplayString):
    """Custom type radiusServerSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RadiusServerSecret_Type.__name__ = "DisplayString"
_RadiusServerSecret_Object = MibTableColumn
radiusServerSecret = _RadiusServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 25, 10, 1, 8),
    _RadiusServerSecret_Type()
)
radiusServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerSecret.setStatus("current")
_Supply_ObjectIdentity = ObjectIdentity
supply = _Supply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 30)
)
_SupplyCount_Type = Integer32
_SupplyCount_Object = MibScalar
supplyCount = _SupplyCount_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 30, 1),
    _SupplyCount_Type()
)
supplyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supplyCount.setStatus("current")
_SupplyTable_Object = MibTable
supplyTable = _SupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 30, 10)
)
if mibBuilder.loadTexts:
    supplyTable.setStatus("current")
_SupplyTableEntry_Object = MibTableRow
supplyTableEntry = _SupplyTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 30, 10, 1)
)
supplyTableEntry.setIndexNames(
    (0, "MS-SWITCH30-MIB", "supplyId"),
)
if mibBuilder.loadTexts:
    supplyTableEntry.setStatus("current")


class _SupplyId_Type(Integer32):
    """Custom type supplyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SupplyId_Type.__name__ = "Integer32"
_SupplyId_Object = MibTableColumn
supplyId = _SupplyId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 30, 10, 1, 1),
    _SupplyId_Type()
)
supplyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supplyId.setStatus("current")


class _SupplyUsed_Type(Integer32):
    """Custom type supplyUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("unsupported", 255),
          ("unused", 2),
          ("used", 1))
    )


_SupplyUsed_Type.__name__ = "Integer32"
_SupplyUsed_Object = MibTableColumn
supplyUsed = _SupplyUsed_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 30, 10, 1, 2),
    _SupplyUsed_Type()
)
supplyUsed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    supplyUsed.setStatus("current")


class _SupplyStatus_Type(Integer32):
    """Custom type supplyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("undefined", 254),
          ("unsupported", 255),
          ("valid", 1))
    )


_SupplyStatus_Type.__name__ = "Integer32"
_SupplyStatus_Object = MibTableColumn
supplyStatus = _SupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 30, 10, 1, 3),
    _SupplyStatus_Type()
)
supplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supplyStatus.setStatus("current")
_Poepse_ObjectIdentity = ObjectIdentity
poepse = _Poepse_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 31)
)


class _PoepseSupport_Type(Integer32):
    """Custom type poepseSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 255))
    )


_PoepseSupport_Type.__name__ = "Integer32"
_PoepseSupport_Object = MibScalar
poepseSupport = _PoepseSupport_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 31, 1),
    _PoepseSupport_Type()
)
poepseSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poepseSupport.setStatus("current")


class _PoepseEnable_Type(Integer32):
    """Custom type poepseEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_PoepseEnable_Type.__name__ = "Integer32"
_PoepseEnable_Object = MibScalar
poepseEnable = _PoepseEnable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 31, 2),
    _PoepseEnable_Type()
)
poepseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poepseEnable.setStatus("current")
_PoepseTotalInputPower_Type = Integer32
_PoepseTotalInputPower_Object = MibScalar
poepseTotalInputPower = _PoepseTotalInputPower_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 31, 3),
    _PoepseTotalInputPower_Type()
)
poepseTotalInputPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poepseTotalInputPower.setStatus("current")
_PoepseMaxInputPower_Type = Integer32
_PoepseMaxInputPower_Object = MibScalar
poepseMaxInputPower = _PoepseMaxInputPower_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 31, 4),
    _PoepseMaxInputPower_Type()
)
poepseMaxInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poepseMaxInputPower.setStatus("current")
_PoepseDeviceSupplyPower_Type = Integer32
_PoepseDeviceSupplyPower_Object = MibScalar
poepseDeviceSupplyPower = _PoepseDeviceSupplyPower_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 31, 5),
    _PoepseDeviceSupplyPower_Type()
)
poepseDeviceSupplyPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poepseDeviceSupplyPower.setStatus("current")
_PseAvailablePower_Type = Integer32
_PseAvailablePower_Object = MibScalar
pseAvailablePower = _PseAvailablePower_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 31, 6),
    _PseAvailablePower_Type()
)
pseAvailablePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pseAvailablePower.setStatus("current")


class _PoepseExtendedVoltage_Type(Integer32):
    """Custom type poepseExtendedVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_PoepseExtendedVoltage_Type.__name__ = "Integer32"
_PoepseExtendedVoltage_Object = MibScalar
poepseExtendedVoltage = _PoepseExtendedVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 31, 7),
    _PoepseExtendedVoltage_Type()
)
poepseExtendedVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poepseExtendedVoltage.setStatus("current")
_PoepsePortTable_Object = MibTable
poepsePortTable = _PoepsePortTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 31, 10)
)
if mibBuilder.loadTexts:
    poepsePortTable.setStatus("current")
_PoepsePortTableEntry_Object = MibTableRow
poepsePortTableEntry = _PoepsePortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 31, 10, 1)
)
poepsePortTableEntry.setIndexNames(
    (0, "MS-SWITCH30-MIB", "poepsePortId"),
)
if mibBuilder.loadTexts:
    poepsePortTableEntry.setStatus("current")


class _PoepsePortId_Type(Integer32):
    """Custom type poepsePortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_PoepsePortId_Type.__name__ = "Integer32"
_PoepsePortId_Object = MibTableColumn
poepsePortId = _PoepsePortId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 31, 10, 1, 1),
    _PoepsePortId_Type()
)
poepsePortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poepsePortId.setStatus("current")


class _PoepsePortMode_Type(Integer32):
    """Custom type poepsePortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("poe8023af", 1),
          ("poeDisabled", 3),
          ("poeForced", 2),
          ("undefined", 254),
          ("unsupported", 255))
    )


_PoepsePortMode_Type.__name__ = "Integer32"
_PoepsePortMode_Object = MibTableColumn
poepsePortMode = _PoepsePortMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 31, 10, 1, 2),
    _PoepsePortMode_Type()
)
poepsePortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poepsePortMode.setStatus("current")


class _PoepsePortStatus_Type(Integer32):
    """Custom type poepsePortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 4),
          ("discovering", 1),
          ("fault", 3),
          ("off", 0),
          ("overcurrent", 5),
          ("powered", 2),
          ("undefined", 254),
          ("unsupported", 255))
    )


_PoepsePortStatus_Type.__name__ = "Integer32"
_PoepsePortStatus_Object = MibTableColumn
poepsePortStatus = _PoepsePortStatus_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 31, 10, 1, 3),
    _PoepsePortStatus_Type()
)
poepsePortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poepsePortStatus.setStatus("current")


class _PoepsePortMaxPower_Type(Integer32):
    """Custom type poepsePortMaxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15400),
    )


_PoepsePortMaxPower_Type.__name__ = "Integer32"
_PoepsePortMaxPower_Object = MibTableColumn
poepsePortMaxPower = _PoepsePortMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 31, 10, 1, 4),
    _PoepsePortMaxPower_Type()
)
poepsePortMaxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poepsePortMaxPower.setStatus("current")
_PoepsePortMeasuredPower_Type = Integer32
_PoepsePortMeasuredPower_Object = MibTableColumn
poepsePortMeasuredPower = _PoepsePortMeasuredPower_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 31, 10, 1, 5),
    _PoepsePortMeasuredPower_Type()
)
poepsePortMeasuredPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poepsePortMeasuredPower.setStatus("current")


class _PoepsePortMaxClass_Type(Integer32):
    """Custom type poepsePortMaxClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3),
          ("class4", 4),
          ("undefined", 254),
          ("unsupported", 255))
    )


_PoepsePortMaxClass_Type.__name__ = "Integer32"
_PoepsePortMaxClass_Object = MibTableColumn
poepsePortMaxClass = _PoepsePortMaxClass_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 31, 10, 1, 6),
    _PoepsePortMaxClass_Type()
)
poepsePortMaxClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poepsePortMaxClass.setStatus("current")


class _PoepsePortDetectedClass_Type(Integer32):
    """Custom type poepsePortDetectedClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3),
          ("class4", 4),
          ("undefined", 254),
          ("unsupported", 255))
    )


_PoepsePortDetectedClass_Type.__name__ = "Integer32"
_PoepsePortDetectedClass_Object = MibTableColumn
poepsePortDetectedClass = _PoepsePortDetectedClass_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 31, 10, 1, 7),
    _PoepsePortDetectedClass_Type()
)
poepsePortDetectedClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poepsePortDetectedClass.setStatus("current")
_PoepsePortMeasuredVoltage_Type = Integer32
_PoepsePortMeasuredVoltage_Object = MibTableColumn
poepsePortMeasuredVoltage = _PoepsePortMeasuredVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 31, 10, 1, 8),
    _PoepsePortMeasuredVoltage_Type()
)
poepsePortMeasuredVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poepsePortMeasuredVoltage.setStatus("current")
_Poepd_ObjectIdentity = ObjectIdentity
poepd = _Poepd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 32)
)


class _PoepdSupport_Type(Integer32):
    """Custom type poepdSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 255))
    )


_PoepdSupport_Type.__name__ = "Integer32"
_PoepdSupport_Object = MibScalar
poepdSupport = _PoepdSupport_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 32, 1),
    _PoepdSupport_Type()
)
poepdSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poepdSupport.setStatus("current")
_Hardwarecode_ObjectIdentity = ObjectIdentity
hardwarecode = _Hardwarecode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 33)
)


class _HardwarecodeSupport_Type(Integer32):
    """Custom type hardwarecodeSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 255))
    )


_HardwarecodeSupport_Type.__name__ = "Integer32"
_HardwarecodeSupport_Object = MibScalar
hardwarecodeSupport = _HardwarecodeSupport_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 33, 1),
    _HardwarecodeSupport_Type()
)
hardwarecodeSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwarecodeSupport.setStatus("current")
_HardwarecodeNumber_Type = Integer32
_HardwarecodeNumber_Object = MibScalar
hardwarecodeNumber = _HardwarecodeNumber_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 33, 2),
    _HardwarecodeNumber_Type()
)
hardwarecodeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwarecodeNumber.setStatus("current")
_Spanningtree_ObjectIdentity = ObjectIdentity
spanningtree = _Spanningtree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 34)
)


class _StpSupport_Type(Integer32):
    """Custom type stpSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 255))
    )


_StpSupport_Type.__name__ = "Integer32"
_StpSupport_Object = MibScalar
stpSupport = _StpSupport_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 34, 1),
    _StpSupport_Type()
)
stpSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpSupport.setStatus("current")


class _StpEnable_Type(Integer32):
    """Custom type stpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 255))
    )


_StpEnable_Type.__name__ = "Integer32"
_StpEnable_Object = MibScalar
stpEnable = _StpEnable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 34, 2),
    _StpEnable_Type()
)
stpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpEnable.setStatus("current")
_MsSwitchNotifications_ObjectIdentity = ObjectIdentity
msSwitchNotifications = _MsSwitchNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 100)
)

# Managed Objects groups


# Notification objects

linkChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 100, 1)
)
linkChangeNotification.setObjects(
      *(("MS-SWITCH30-MIB", "portStatusId"),
        ("MS-SWITCH30-MIB", "portStatusLink"))
)
if mibBuilder.loadTexts:
    linkChangeNotification.setStatus(
        "current"
    )

factoryResetNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 100, 2)
)
if mibBuilder.loadTexts:
    factoryResetNotification.setStatus(
        "current"
    )

temperatureLevelChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 100, 3)
)
temperatureLevelChangeNotification.setObjects(
    ("MS-SWITCH30-MIB", "deviceTemperatureLevel")
)
if mibBuilder.loadTexts:
    temperatureLevelChangeNotification.setStatus(
        "current"
    )

errorcountNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 100, 4)
)
errorcountNotification.setObjects(
    ("MS-SWITCH30-MIB", "portStatusId")
)
if mibBuilder.loadTexts:
    errorcountNotification.setStatus(
        "current"
    )

underOverVoltageNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 100, 5)
)
underOverVoltageNotification.setObjects(
    ("MS-SWITCH30-MIB", "portStatusId")
)
if mibBuilder.loadTexts:
    underOverVoltageNotification.setStatus(
        "current"
    )

temperatureShutdownNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 100, 6)
)
if mibBuilder.loadTexts:
    temperatureShutdownNotification.setStatus(
        "current"
    )

portPoELimitExceededNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 100, 7)
)
portPoELimitExceededNotification.setObjects(
    ("MS-SWITCH30-MIB", "portStatusId")
)
if mibBuilder.loadTexts:
    portPoELimitExceededNotification.setStatus(
        "current"
    )

powerSupplyStatusChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 100, 8)
)
powerSupplyStatusChangeNotification.setObjects(
    ("MS-SWITCH30-MIB", "supplyId")
)
if mibBuilder.loadTexts:
    powerSupplyStatusChangeNotification.setStatus(
        "current"
    )

sfpPlugChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 100, 9)
)
sfpPlugChangeNotification.setObjects(
      *(("MS-SWITCH30-MIB", "sfpPortnumber"),
        ("MS-SWITCH30-MIB", "sfpDetect"))
)
if mibBuilder.loadTexts:
    sfpPlugChangeNotification.setStatus(
        "current"
    )

loginFailureNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 100, 10)
)
if mibBuilder.loadTexts:
    loginFailureNotification.setStatus(
        "current"
    )

ringBrokenNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 100, 11)
)
ringBrokenNotification.setObjects(
      *(("MS-SWITCH30-MIB", "ringNumber"),
        ("MS-SWITCH30-MIB", "portStatusId"),
        ("MS-SWITCH30-MIB", "portStatusLink"))
)
if mibBuilder.loadTexts:
    ringBrokenNotification.setStatus(
        "current"
    )

ringAlarmNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 100, 12)
)
ringAlarmNotification.setObjects(
      *(("MS-SWITCH30-MIB", "ringNumber"),
        ("MS-SWITCH30-MIB", "ringStatus"),
        ("MS-SWITCH30-MIB", "ringAlarmDuration"))
)
if mibBuilder.loadTexts:
    ringAlarmNotification.setStatus(
        "current"
    )

snmpv3AuthenticationPwFailNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 100, 13)
)
if mibBuilder.loadTexts:
    snmpv3AuthenticationPwFailNotification.setStatus(
        "current"
    )

snmpv3PrivacyPwFailNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 100, 14)
)
if mibBuilder.loadTexts:
    snmpv3PrivacyPwFailNotification.setStatus(
        "current"
    )

snmpv3AccessPermissionNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 100, 15)
)
if mibBuilder.loadTexts:
    snmpv3AccessPermissionNotification.setStatus(
        "current"
    )

snmpv3SeclevelFailNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3181, 10, 3, 100, 16)
)
if mibBuilder.loadTexts:
    snmpv3SeclevelFailNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MS-SWITCH30-MIB",
    **{"microsens": microsens,
       "managedSwitches": managedSwitches,
       "mib3": mib3,
       "device": device,
       "deviceArtNo": deviceArtNo,
       "deviceSerNo": deviceSerNo,
       "deviceHardware": deviceHardware,
       "deviceDescription": deviceDescription,
       "deviceName": deviceName,
       "deviceLocation": deviceLocation,
       "deviceContact": deviceContact,
       "deviceGroup": deviceGroup,
       "deviceTemperature": deviceTemperature,
       "deviceTemperatureLevel": deviceTemperatureLevel,
       "deviceUpTime": deviceUpTime,
       "deviceFddActiveTime": deviceFddActiveTime,
       "deviceFddPassiveTime": deviceFddPassiveTime,
       "deviceInventory": deviceInventory,
       "agent": agent,
       "agentFirmware": agentFirmware,
       "agentMacAddress": agentMacAddress,
       "agentIpMode": agentIpMode,
       "agentIpAddress": agentIpAddress,
       "agentSubnetMask": agentSubnetMask,
       "agentGateway": agentGateway,
       "agentConfigReset": agentConfigReset,
       "agentConfigFactoryDefault": agentConfigFactoryDefault,
       "agentConfigEnableFactoryButton": agentConfigEnableFactoryButton,
       "agentSecureAddressFlag": agentSecureAddressFlag,
       "agentStorageMediaCardStatus": agentStorageMediaCardStatus,
       "agentStorageMediaCardBoot": agentStorageMediaCardBoot,
       "agentStorageMediaCardMac": agentStorageMediaCardMac,
       "agentStoreConfigToStorageMediaCard": agentStoreConfigToStorageMediaCard,
       "port": port,
       "portCount": portCount,
       "portStatusTable": portStatusTable,
       "portStatusTableEntry": portStatusTableEntry,
       "portStatusId": portStatusId,
       "portStatusType": portStatusType,
       "portStatusLink": portStatusLink,
       "portStatusSpeed": portStatusSpeed,
       "portStatusDuplex": portStatusDuplex,
       "portStatusFlowControl": portStatusFlowControl,
       "portStatusPinout": portStatusPinout,
       "portStatusFarEndFault": portStatusFarEndFault,
       "portStatusRxNetload": portStatusRxNetload,
       "portStatusTxNetload": portStatusTxNetload,
       "portConfigTable": portConfigTable,
       "portConfigTableEntry": portConfigTableEntry,
       "portConfigId": portConfigId,
       "portConfigAlias": portConfigAlias,
       "portConfigEnable": portConfigEnable,
       "portConfigAutonego": portConfigAutonego,
       "portConfigSpeed": portConfigSpeed,
       "portConfigDuplex": portConfigDuplex,
       "portConfigFlowControl": portConfigFlowControl,
       "portConfigPinout": portConfigPinout,
       "portConfigFarEndFault": portConfigFarEndFault,
       "portConfigAdvertise": portConfigAdvertise,
       "portConfigFibreDownDetection": portConfigFibreDownDetection,
       "vlan": vlan,
       "vlanSupport": vlanSupport,
       "vlanEnable": vlanEnable,
       "vlanForceDefaultVID": vlanForceDefaultVID,
       "vlanFilterCount": vlanFilterCount,
       "vlanVoiceVID": vlanVoiceVID,
       "vlanRstpVID": vlanRstpVID,
       "vlanUnauthVID": vlanUnauthVID,
       "vlanPortTable": vlanPortTable,
       "vlanPortTableEntry": vlanPortTableEntry,
       "vlanPortId": vlanPortId,
       "vlanPortMode": vlanPortMode,
       "vlanDefaultVID": vlanDefaultVID,
       "vlanDefaultPriority": vlanDefaultPriority,
       "vlanPortFlags": vlanPortFlags,
       "vlanFilterTable": vlanFilterTable,
       "vlanFilterTableEntry": vlanFilterTableEntry,
       "vlanFilterId": vlanFilterId,
       "vlanFilterVID": vlanFilterVID,
       "vlanFilterAlias": vlanFilterAlias,
       "vlanFilterEnable": vlanFilterEnable,
       "vlanMemberManager": vlanMemberManager,
       "vlanMemberPort1": vlanMemberPort1,
       "vlanMemberPort2": vlanMemberPort2,
       "vlanMemberPort3": vlanMemberPort3,
       "vlanMemberPort4": vlanMemberPort4,
       "vlanMemberPort5": vlanMemberPort5,
       "vlanMemberPort6": vlanMemberPort6,
       "vlanMemberPort7": vlanMemberPort7,
       "vlanMemberPort8": vlanMemberPort8,
       "vlanMemberPort9": vlanMemberPort9,
       "vlanMemberPort10": vlanMemberPort10,
       "vlanMemberPort11": vlanMemberPort11,
       "vlanMemberPort12": vlanMemberPort12,
       "vlanMemberPort13": vlanMemberPort13,
       "vlanMemberPort14": vlanMemberPort14,
       "vlanMemberPort15": vlanMemberPort15,
       "vlanMemberPort16": vlanMemberPort16,
       "vlanMemberPort17": vlanMemberPort17,
       "vlanMemberPort18": vlanMemberPort18,
       "vlanMemberPort19": vlanMemberPort19,
       "vlanMemberPort20": vlanMemberPort20,
       "vlanMemberPort21": vlanMemberPort21,
       "vlanMemberPort22": vlanMemberPort22,
       "vlanMemberPort23": vlanMemberPort23,
       "vlanMemberPort24": vlanMemberPort24,
       "vlanFilterEnhTable": vlanFilterEnhTable,
       "vlanFilterEnhTableEntry": vlanFilterEnhTableEntry,
       "vlanFilterEnhId": vlanFilterEnhId,
       "vlanFilterEnhFlags": vlanFilterEnhFlags,
       "vlanFilterEnhPriOverride": vlanFilterEnhPriOverride,
       "prioritization": prioritization,
       "prioSupport": prioSupport,
       "prioQueueCount": prioQueueCount,
       "prioQueueScheme": prioQueueScheme,
       "prioPortEnable": prioPortEnable,
       "prioIeeeTagEnable": prioIeeeTagEnable,
       "prioDiffservEnable": prioDiffservEnable,
       "prioPortTable": prioPortTable,
       "prioPortTableEntry": prioPortTableEntry,
       "prioPortId": prioPortId,
       "prioPortQueue": prioPortQueue,
       "prioIeeeTagTable": prioIeeeTagTable,
       "prioIeeeTagTableEntry": prioIeeeTagTableEntry,
       "prioIeeeTagId": prioIeeeTagId,
       "prioIeeeTagQueue": prioIeeeTagQueue,
       "prioDiffservTable": prioDiffservTable,
       "prioDiffservTableEntry": prioDiffservTableEntry,
       "prioDiffservId": prioDiffservId,
       "prioDiffservQueue": prioDiffservQueue,
       "monitor": monitor,
       "monitorSupport": monitorSupport,
       "monitorMode": monitorMode,
       "monitorSource": monitorSource,
       "monitorDestination": monitorDestination,
       "ring": ring,
       "ringSupport": ringSupport,
       "ringCount": ringCount,
       "ringTable": ringTable,
       "ringTableEntry": ringTableEntry,
       "ringId": ringId,
       "ringMode": ringMode,
       "ringPortA": ringPortA,
       "ringPortB": ringPortB,
       "ringNumber": ringNumber,
       "ringStatus": ringStatus,
       "ringAlarmDuration": ringAlarmDuration,
       "couplingred": couplingred,
       "couplingredSupport": couplingredSupport,
       "couplingredPort": couplingredPort,
       "couplingredMode": couplingredMode,
       "couplingredPartnerIp": couplingredPartnerIp,
       "couplingredStatus": couplingredStatus,
       "couplingredPartnerStatus": couplingredPartnerStatus,
       "couplingredValidationFlag": couplingredValidationFlag,
       "sfp": sfp,
       "sfpSupport": sfpSupport,
       "sfpCount": sfpCount,
       "sfpTable": sfpTable,
       "sfpTableEntry": sfpTableEntry,
       "sfpId": sfpId,
       "sfpPortnumber": sfpPortnumber,
       "sfpDetect": sfpDetect,
       "sfpVendor": sfpVendor,
       "sfpVendorPartnumber": sfpVendorPartnumber,
       "sfpVendorSerialnumber": sfpVendorSerialnumber,
       "sfpConnector": sfpConnector,
       "sfpNominalBitrate": sfpNominalBitrate,
       "sfpDiagnostic": sfpDiagnostic,
       "sfpTemperature": sfpTemperature,
       "sfpVoltage": sfpVoltage,
       "sfpTxBias": sfpTxBias,
       "sfpTxPower": sfpTxPower,
       "sfpRxPower": sfpRxPower,
       "sfpWarnings": sfpWarnings,
       "sfpAlarms": sfpAlarms,
       "relais": relais,
       "relaisSupport": relaisSupport,
       "relaisCount": relaisCount,
       "relaisTable": relaisTable,
       "relaisTableEntry": relaisTableEntry,
       "relaisId": relaisId,
       "relaisAlias": relaisAlias,
       "relaisMode": relaisMode,
       "relaisStatus": relaisStatus,
       "portaccessctrl": portaccessctrl,
       "pacSupport": pacSupport,
       "pacEnable": pacEnable,
       "pacUnauthMode": pacUnauthMode,
       "pacUnauthVID": pacUnauthVID,
       "pacMaxNumberOfAllowedHostsPerPort": pacMaxNumberOfAllowedHostsPerPort,
       "pacFallbackRequestEnable": pacFallbackRequestEnable,
       "pacFallbackRequestTimeout": pacFallbackRequestTimeout,
       "pacFallbackRejectsEnable": pacFallbackRejectsEnable,
       "pacFallbackMaxRejects": pacFallbackMaxRejects,
       "pacSupplicantTimeout": pacSupplicantTimeout,
       "pacReauthEnable": pacReauthEnable,
       "pacReauthTime": pacReauthTime,
       "pacStatusTable": pacStatusTable,
       "pacStatusTableEntry": pacStatusTableEntry,
       "pacStatPortId": pacStatPortId,
       "pacStatPortMode": pacStatPortMode,
       "pacStatPortStatus": pacStatPortStatus,
       "pacStatUserStatus1": pacStatUserStatus1,
       "pacStatUserStatus2": pacStatUserStatus2,
       "pacStatUserStatus3": pacStatUserStatus3,
       "pacStatUserStatus4": pacStatUserStatus4,
       "pacStatUserMac1": pacStatUserMac1,
       "pacStatUserMac2": pacStatUserMac2,
       "pacStatUserMac3": pacStatUserMac3,
       "pacStatUserMac4": pacStatUserMac4,
       "pacStatUserName1": pacStatUserName1,
       "pacStatUserName2": pacStatUserName2,
       "pacStatUserName3": pacStatUserName3,
       "pacStatUserName4": pacStatUserName4,
       "pacStatUserIp1": pacStatUserIp1,
       "pacStatUserIp2": pacStatUserIp2,
       "pacStatUserIp3": pacStatUserIp3,
       "pacStatUserIp4": pacStatUserIp4,
       "pacConfigTable": pacConfigTable,
       "pacConfigTableEntry": pacConfigTableEntry,
       "pacConfPortId": pacConfPortId,
       "pacConfMode": pacConfMode,
       "pacConfMaxMacCount": pacConfMaxMacCount,
       "pacMacLockingTable": pacMacLockingTable,
       "pacMacLockTableEntry": pacMacLockTableEntry,
       "pacMacLockPortId": pacMacLockPortId,
       "pacMacLockEnable1": pacMacLockEnable1,
       "pacMacLockEnable2": pacMacLockEnable2,
       "pacMacLockEnable3": pacMacLockEnable3,
       "pacMacLockEnable4": pacMacLockEnable4,
       "pacMacLockLearn1": pacMacLockLearn1,
       "pacMacLockLearn2": pacMacLockLearn2,
       "pacMacLockLearn3": pacMacLockLearn3,
       "pacMacLockLearn4": pacMacLockLearn4,
       "pacLockedMac1": pacLockedMac1,
       "pacLockedMac2": pacLockedMac2,
       "pacLockedMac3": pacLockedMac3,
       "pacLockedMac4": pacLockedMac4,
       "igmps": igmps,
       "igmpsSupport": igmpsSupport,
       "igmpsEnable": igmpsEnable,
       "igmpsFastLeave": igmpsFastLeave,
       "igmpsReportAggregation": igmpsReportAggregation,
       "igmpsFloodingUnregPack": igmpsFloodingUnregPack,
       "igmpsMaxGroupLimit": igmpsMaxGroupLimit,
       "igmpsGroupLimit": igmpsGroupLimit,
       "igmpsGroupNumber": igmpsGroupNumber,
       "igmpsRouterDetection": igmpsRouterDetection,
       "igmpsGroupMembershipInterval": igmpsGroupMembershipInterval,
       "igmpsMaximumResposeTime": igmpsMaximumResposeTime,
       "igmpsLastMemeberQueryTime": igmpsLastMemeberQueryTime,
       "igmpsNeighborDeadInterval": igmpsNeighborDeadInterval,
       "igmpsRouterAgingTime": igmpsRouterAgingTime,
       "igmpsRxMessageGeneralQuery": igmpsRxMessageGeneralQuery,
       "igmpsRxMessageSpecificQuery": igmpsRxMessageSpecificQuery,
       "igmpsRxMessageReport": igmpsRxMessageReport,
       "igmpsRxMessageLeave": igmpsRxMessageLeave,
       "igmpsRxMessageAdvertisement": igmpsRxMessageAdvertisement,
       "igmpsRxMessageTermination": igmpsRxMessageTermination,
       "igmpsTxMessageSolicitation": igmpsTxMessageSolicitation,
       "igmpsCounterReset": igmpsCounterReset,
       "igmpsPortTable": igmpsPortTable,
       "igmpsPortTableEntry": igmpsPortTableEntry,
       "igmpsPortId": igmpsPortId,
       "igmpsPortSnooping": igmpsPortSnooping,
       "igmpsPortStaticRouter": igmpsPortStaticRouter,
       "igmpsPortDynamicRouter": igmpsPortDynamicRouter,
       "igmpsGroupTable": igmpsGroupTable,
       "igmpsGroupTableEntry": igmpsGroupTableEntry,
       "igmpsGroupId": igmpsGroupId,
       "igmpsGroupMac": igmpsGroupMac,
       "igmpsGroupVlanId": igmpsGroupVlanId,
       "igmpsGroupTimestamp": igmpsGroupTimestamp,
       "igmpsGroupLeaveFlag": igmpsGroupLeaveFlag,
       "igmpsGroupMemberPort1": igmpsGroupMemberPort1,
       "igmpsGroupMemberPort2": igmpsGroupMemberPort2,
       "igmpsGroupMemberPort3": igmpsGroupMemberPort3,
       "igmpsGroupMemberPort4": igmpsGroupMemberPort4,
       "igmpsGroupMemberPort5": igmpsGroupMemberPort5,
       "igmpsGroupMemberPort6": igmpsGroupMemberPort6,
       "igmpsGroupMemberPort7": igmpsGroupMemberPort7,
       "igmpsGroupMemberPort8": igmpsGroupMemberPort8,
       "igmpsGroupMemberPort9": igmpsGroupMemberPort9,
       "igmpsGroupMemberPort10": igmpsGroupMemberPort10,
       "igmpsGroupMemberPort11": igmpsGroupMemberPort11,
       "igmpsGroupMemberPort12": igmpsGroupMemberPort12,
       "igmpsGroupMemberPort13": igmpsGroupMemberPort13,
       "igmpsGroupMemberPort14": igmpsGroupMemberPort14,
       "igmpsGroupMemberPort15": igmpsGroupMemberPort15,
       "igmpsGroupMemberPort16": igmpsGroupMemberPort16,
       "igmpsGroupMemberPort17": igmpsGroupMemberPort17,
       "igmpsGroupMemberPort18": igmpsGroupMemberPort18,
       "igmpsGroupMemberPort19": igmpsGroupMemberPort19,
       "igmpsGroupMemberPort20": igmpsGroupMemberPort20,
       "igmpsGroupMemberPort21": igmpsGroupMemberPort21,
       "igmpsGroupMemberPort22": igmpsGroupMemberPort22,
       "igmpsGroupMemberPort23": igmpsGroupMemberPort23,
       "igmpsGroupMemberPort24": igmpsGroupMemberPort24,
       "rtc": rtc,
       "rtcSupport": rtcSupport,
       "rtcFlags": rtcFlags,
       "rtcLocalTime": rtcLocalTime,
       "rtcManualTime": rtcManualTime,
       "rtcTimeStatus": rtcTimeStatus,
       "rtcTimezoneOffset": rtcTimezoneOffset,
       "rtcDSTOffset": rtcDSTOffset,
       "rtcDSTbegin": rtcDSTbegin,
       "rtcDSTend": rtcDSTend,
       "rtcDSTstatus": rtcDSTstatus,
       "rtcSNTPsyncInterval": rtcSNTPsyncInterval,
       "rtcSNTPsyncNow": rtcSNTPsyncNow,
       "rtcSNTPServerCount": rtcSNTPServerCount,
       "rtcSNTPServerTable": rtcSNTPServerTable,
       "rtcSNTPServerTableEntry": rtcSNTPServerTableEntry,
       "rtcSNTPServerId": rtcSNTPServerId,
       "rtcSNTPServerStatus": rtcSNTPServerStatus,
       "rtcSNTPServerEnable": rtcSNTPServerEnable,
       "rtcSNTPServerIpAddress": rtcSNTPServerIpAddress,
       "consoleinterface": consoleinterface,
       "consoleSupport": consoleSupport,
       "consoleEnable": consoleEnable,
       "consoleTimeout": consoleTimeout,
       "consoleApplyMode": consoleApplyMode,
       "consolePrompt": consolePrompt,
       "webinterface": webinterface,
       "webSupport": webSupport,
       "webEnable": webEnable,
       "snmpinterface": snmpinterface,
       "snmpSupport": snmpSupport,
       "snmpEnable": snmpEnable,
       "snmpApplyMode": snmpApplyMode,
       "snmpApply": snmpApply,
       "snmpTrapTest": snmpTrapTest,
       "snmpTrapDestCount": snmpTrapDestCount,
       "snmpCommunityRead": snmpCommunityRead,
       "snmpCommunityWrite": snmpCommunityWrite,
       "snmpTrapEnable": snmpTrapEnable,
       "snmpTrapDestTable": snmpTrapDestTable,
       "snmpTrapDestTableEntry": snmpTrapDestTableEntry,
       "snmpTrapDestId": snmpTrapDestId,
       "snmpTrapDestAlias": snmpTrapDestAlias,
       "snmpTrapDestEn": snmpTrapDestEn,
       "snmpTrapDestIP": snmpTrapDestIP,
       "snmpTrapDestCommunity": snmpTrapDestCommunity,
       "snmpTrapGenColdstart": snmpTrapGenColdstart,
       "snmpTrapGenWarmstart": snmpTrapGenWarmstart,
       "snmpTrapGenLinkDown": snmpTrapGenLinkDown,
       "snmpTrapGenLinkUp": snmpTrapGenLinkUp,
       "snmpTrapGenAuthFailure": snmpTrapGenAuthFailure,
       "snmpTrapGenEgpNeighborLoss": snmpTrapGenEgpNeighborLoss,
       "snmpTrapEntLinkChange": snmpTrapEntLinkChange,
       "snmpTrapEntFactoryReset": snmpTrapEntFactoryReset,
       "snmpTrapEntTemperatureLevelChange": snmpTrapEntTemperatureLevelChange,
       "snmpTrapEntErrorCounter": snmpTrapEntErrorCounter,
       "snmpTrapEntUnderOverVoltage": snmpTrapEntUnderOverVoltage,
       "snmpTrapEntTempShutDown": snmpTrapEntTempShutDown,
       "snmpTrapEntPoeLimitExceeded": snmpTrapEntPoeLimitExceeded,
       "snmpTrapEntSupplyStatusChange": snmpTrapEntSupplyStatusChange,
       "snmpTrapEntSfpPlugChange": snmpTrapEntSfpPlugChange,
       "snmpTrapEntLoginFailure": snmpTrapEntLoginFailure,
       "snmpTrapEntRingBroken": snmpTrapEntRingBroken,
       "snmpTrapEntRingAlarm": snmpTrapEntRingAlarm,
       "snmpTrapEntAuthPwFail": snmpTrapEntAuthPwFail,
       "snmpTrapEntPrivPwFail": snmpTrapEntPrivPwFail,
       "snmpTrapEntAccessPermission": snmpTrapEntAccessPermission,
       "snmpTrapEntSeclevelFail": snmpTrapEntSeclevelFail,
       "udpinterface": udpinterface,
       "udpSupport": udpSupport,
       "udpEnable": udpEnable,
       "syslog": syslog,
       "syslogSupport": syslogSupport,
       "syslogEnable": syslogEnable,
       "syslogMessageTest": syslogMessageTest,
       "syslogDestCount": syslogDestCount,
       "syslogDestTable": syslogDestTable,
       "syslogDestTableEntry": syslogDestTableEntry,
       "syslogDestId": syslogDestId,
       "syslogDestAlias": syslogDestAlias,
       "syslogDestEnable": syslogDestEnable,
       "syslogDestIpAddress": syslogDestIpAddress,
       "syslogDestPort": syslogDestPort,
       "syslogDestFacility": syslogDestFacility,
       "syslogDestEventFilter": syslogDestEventFilter,
       "radius": radius,
       "radiusSupport": radiusSupport,
       "radiusAccessEnable": radiusAccessEnable,
       "radiusAccountEnable": radiusAccountEnable,
       "radiusServerCount": radiusServerCount,
       "radiusMacAuthPassword": radiusMacAuthPassword,
       "radiusUseMacAsPassword": radiusUseMacAsPassword,
       "radiusMacSeparator": radiusMacSeparator,
       "radiusTimeout": radiusTimeout,
       "radiusServerTable": radiusServerTable,
       "radiusServerTableEntry": radiusServerTableEntry,
       "radiusServerId": radiusServerId,
       "radiusServerAlias": radiusServerAlias,
       "radiusServerEnableAccess": radiusServerEnableAccess,
       "radiusServerEnableAccount": radiusServerEnableAccount,
       "radiusServerIpAddress": radiusServerIpAddress,
       "radiusServerAccessPort": radiusServerAccessPort,
       "radiusServerAccountPort": radiusServerAccountPort,
       "radiusServerSecret": radiusServerSecret,
       "supply": supply,
       "supplyCount": supplyCount,
       "supplyTable": supplyTable,
       "supplyTableEntry": supplyTableEntry,
       "supplyId": supplyId,
       "supplyUsed": supplyUsed,
       "supplyStatus": supplyStatus,
       "poepse": poepse,
       "poepseSupport": poepseSupport,
       "poepseEnable": poepseEnable,
       "poepseTotalInputPower": poepseTotalInputPower,
       "poepseMaxInputPower": poepseMaxInputPower,
       "poepseDeviceSupplyPower": poepseDeviceSupplyPower,
       "pseAvailablePower": pseAvailablePower,
       "poepseExtendedVoltage": poepseExtendedVoltage,
       "poepsePortTable": poepsePortTable,
       "poepsePortTableEntry": poepsePortTableEntry,
       "poepsePortId": poepsePortId,
       "poepsePortMode": poepsePortMode,
       "poepsePortStatus": poepsePortStatus,
       "poepsePortMaxPower": poepsePortMaxPower,
       "poepsePortMeasuredPower": poepsePortMeasuredPower,
       "poepsePortMaxClass": poepsePortMaxClass,
       "poepsePortDetectedClass": poepsePortDetectedClass,
       "poepsePortMeasuredVoltage": poepsePortMeasuredVoltage,
       "poepd": poepd,
       "poepdSupport": poepdSupport,
       "hardwarecode": hardwarecode,
       "hardwarecodeSupport": hardwarecodeSupport,
       "hardwarecodeNumber": hardwarecodeNumber,
       "spanningtree": spanningtree,
       "stpSupport": stpSupport,
       "stpEnable": stpEnable,
       "msSwitchNotifications": msSwitchNotifications,
       "linkChangeNotification": linkChangeNotification,
       "factoryResetNotification": factoryResetNotification,
       "temperatureLevelChangeNotification": temperatureLevelChangeNotification,
       "errorcountNotification": errorcountNotification,
       "underOverVoltageNotification": underOverVoltageNotification,
       "temperatureShutdownNotification": temperatureShutdownNotification,
       "portPoELimitExceededNotification": portPoELimitExceededNotification,
       "powerSupplyStatusChangeNotification": powerSupplyStatusChangeNotification,
       "sfpPlugChangeNotification": sfpPlugChangeNotification,
       "loginFailureNotification": loginFailureNotification,
       "ringBrokenNotification": ringBrokenNotification,
       "ringAlarmNotification": ringAlarmNotification,
       "snmpv3AuthenticationPwFailNotification": snmpv3AuthenticationPwFailNotification,
       "snmpv3PrivacyPwFailNotification": snmpv3PrivacyPwFailNotification,
       "snmpv3AccessPermissionNotification": snmpv3AccessPermissionNotification,
       "snmpv3SeclevelFailNotification": snmpv3SeclevelFailNotification}
)
