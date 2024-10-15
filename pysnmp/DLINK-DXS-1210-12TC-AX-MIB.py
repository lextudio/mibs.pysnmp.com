# SNMP MIB module (DLINK-DXS-1210-12TC-AX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DLINK-DXS-1210-12TC-AX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:30:46 2024
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

(dot1dBasePort,
 dot1dBasePortEntry,
 dot1dBridge) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort",
    "dot1dBasePortEntry",
    "dot1dBridge")

(Dscp,) = mibBuilder.importSymbols(
    "DIFFSERV-DSCP-TC",
    "Dscp")

(AddressFamilyNumbers,) = mibBuilder.importSymbols(
    "IANA-ADDRESS-FAMILY-NUMBERS-MIB",
    "AddressFamilyNumbers")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

(SnmpAdminString,
 SnmpEngineID,
 SnmpSecurityLevel) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString",
    "SnmpEngineID",
    "SnmpSecurityLevel")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class VlanIndex(Unsigned32, TextualConvention):
    status = "current"


class PortList(OctetString, TextualConvention):
    status = "current"


class VlanList(OctetString, TextualConvention):
    status = "current"


class BridgeId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class Timeout(Integer32, TextualConvention):
    status = "current"
    displayHint = "d4"


class OwnerString(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class RmonStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("createRequest", 2),
          ("invalid", 4),
          ("underCreation", 3),
          ("valid", 1))
    )



class OperationResponseStatus(Integer32, TextualConvention):
    status = "current"
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("arpFailure", 8),
          ("interfaceInactiveToTarget", 7),
          ("internalError", 3),
          ("invalidHostAddress", 11),
          ("maxConcurrentLimitReached", 9),
          ("noRouteToTarget", 6),
          ("requestTimedOut", 4),
          ("responseReceived", 1),
          ("unableToResolveDnsName", 10),
          ("unknown", 2),
          ("unknownDestinationAddress", 5))
    )



class LldpChassisIdSubtype(Integer32, TextualConvention):
    status = "current"
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
        *(("chassisComponent", 1),
          ("interfaceAlias", 2),
          ("interfaceName", 6),
          ("local", 7),
          ("macAddress", 4),
          ("networkAddress", 5),
          ("portComponent", 3))
    )



class LldpChassisId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



class LldpPortIdSubtype(Integer32, TextualConvention):
    status = "current"
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
        *(("agentCircuitId", 6),
          ("interfaceAlias", 1),
          ("interfaceName", 5),
          ("local", 7),
          ("macAddress", 3),
          ("networkAddress", 4),
          ("portComponent", 2))
    )



class LldpPortId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



class LldpManAddrIfSubtype(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ifIndex", 2),
          ("systemPortNumber", 3),
          ("unknown", 1))
    )



class LldpManAddress(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )



class LldpSystemCapabilitiesMap(Bits, TextualConvention):
    status = "current"


class LldpPortNumber(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )



class LldpPortList(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )



class TimeFilter(TimeTicks, TextualConvention):
    status = "current"


class LldpPowerPortClass(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pClassPD", 2),
          ("pClassPSE", 1))
    )



class LldpLinkAggStatusMap(Bits, TextualConvention):
    status = "current"


class ZeroBasedCounter32(Gauge32, TextualConvention):
    status = "current"


class Ipv6Address(OctetString, TextualConvention):
    status = "current"
    displayHint = "2x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )



class InetAddressPrefixLength(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2040),
    )



class DStormCtlTrafficType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("multicast", 2),
          ("unicast", 3))
    )



class DStormCtlThrType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("kbps", 2),
          ("percentage", 3),
          ("pps", 1))
    )



class DStormCtlThrTypeValue(Integer32, TextualConvention):
    status = "current"


class VlanIdOrNone(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )



class LldpXMedDeviceClass(Integer32, TextualConvention):
    status = "current"
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
        *(("endpointClass1", 1),
          ("endpointClass2", 2),
          ("endpointClass3", 3),
          ("networkConnectivity", 4),
          ("notDefined", 0))
    )



class LldpXMedCapabilities(Bits, TextualConvention):
    status = "current"


class PolicyAppType(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_D_link_ObjectIdentity = ObjectIdentity
d_link = _D_link_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171)
)
_Dlink_products_ObjectIdentity = ObjectIdentity
dlink_products = _Dlink_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10)
)
_Dlink_DXS1210SeriesProd_ObjectIdentity = ObjectIdentity
dlink_DXS1210SeriesProd = _Dlink_DXS1210SeriesProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139)
)
_Dxs_1210_12tc_ObjectIdentity = ObjectIdentity
dxs_1210_12tc = _Dxs_1210_12tc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1)
)
_Dxs_1210_12tc_AX_ObjectIdentity = ObjectIdentity
dxs_1210_12tc_AX = _Dxs_1210_12tc_AX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1)
)
_DlinkDeviceInfo_ObjectIdentity = ObjectIdentity
dlinkDeviceInfo = _DlinkDeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1)
)
_DeviceInfoGroup_ObjectIdentity = ObjectIdentity
deviceInfoGroup = _DeviceInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1)
)
_DeviceInformation_ObjectIdentity = ObjectIdentity
deviceInformation = _DeviceInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 1)
)


class _DeviceInfoDeviceType_Type(DisplayString):
    """Custom type deviceInfoDeviceType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_DeviceInfoDeviceType_Type.__name__ = "DisplayString"
_DeviceInfoDeviceType_Object = MibScalar
deviceInfoDeviceType = _DeviceInfoDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 1, 1),
    _DeviceInfoDeviceType_Type()
)
deviceInfoDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceInfoDeviceType.setStatus("current")


class _DeviceInfoBootPROMVersion_Type(DisplayString):
    """Custom type deviceInfoBootPROMVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_DeviceInfoBootPROMVersion_Type.__name__ = "DisplayString"
_DeviceInfoBootPROMVersion_Object = MibScalar
deviceInfoBootPROMVersion = _DeviceInfoBootPROMVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 1, 2),
    _DeviceInfoBootPROMVersion_Type()
)
deviceInfoBootPROMVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceInfoBootPROMVersion.setStatus("current")


class _DeviceInfoFirmwareVersion_Type(DisplayString):
    """Custom type deviceInfoFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_DeviceInfoFirmwareVersion_Type.__name__ = "DisplayString"
_DeviceInfoFirmwareVersion_Object = MibScalar
deviceInfoFirmwareVersion = _DeviceInfoFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 1, 3),
    _DeviceInfoFirmwareVersion_Type()
)
deviceInfoFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceInfoFirmwareVersion.setStatus("current")


class _DeviceInfoHardwareVersion_Type(DisplayString):
    """Custom type deviceInfoHardwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_DeviceInfoHardwareVersion_Type.__name__ = "DisplayString"
_DeviceInfoHardwareVersion_Object = MibScalar
deviceInfoHardwareVersion = _DeviceInfoHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 1, 4),
    _DeviceInfoHardwareVersion_Type()
)
deviceInfoHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceInfoHardwareVersion.setStatus("current")
_DeviceInfoMACAddress_Type = MacAddress
_DeviceInfoMACAddress_Object = MibScalar
deviceInfoMACAddress = _DeviceInfoMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 1, 5),
    _DeviceInfoMACAddress_Type()
)
deviceInfoMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceInfoMACAddress.setStatus("current")


class _DeviceInfoSystemTime_Type(DisplayString):
    """Custom type deviceInfoSystemTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_DeviceInfoSystemTime_Type.__name__ = "DisplayString"
_DeviceInfoSystemTime_Object = MibScalar
deviceInfoSystemTime = _DeviceInfoSystemTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 1, 6),
    _DeviceInfoSystemTime_Type()
)
deviceInfoSystemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceInfoSystemTime.setStatus("current")


class _DeviceInfoSerialNumber_Type(DisplayString):
    """Custom type deviceInfoSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_DeviceInfoSerialNumber_Type.__name__ = "DisplayString"
_DeviceInfoSerialNumber_Object = MibScalar
deviceInfoSerialNumber = _DeviceInfoSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 1, 7),
    _DeviceInfoSerialNumber_Type()
)
deviceInfoSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceInfoSerialNumber.setStatus("current")
_DeviceSwitchCPULast5SecUsage_Type = Integer32
_DeviceSwitchCPULast5SecUsage_Object = MibScalar
deviceSwitchCPULast5SecUsage = _DeviceSwitchCPULast5SecUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 1, 8),
    _DeviceSwitchCPULast5SecUsage_Type()
)
deviceSwitchCPULast5SecUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceSwitchCPULast5SecUsage.setStatus("current")
_DeviceFunction_ObjectIdentity = ObjectIdentity
deviceFunction = _DeviceFunction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2)
)
_FirmwareInformationTable_Object = MibTable
firmwareInformationTable = _FirmwareInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    firmwareInformationTable.setStatus("current")
_FirmwareInformationEntry_Object = MibTableRow
firmwareInformationEntry = _FirmwareInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 1, 1)
)
firmwareInformationEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "firmwareInfoImageID"),
)
if mibBuilder.loadTexts:
    firmwareInformationEntry.setStatus("current")
_FirmwareInfoImageID_Type = Integer32
_FirmwareInfoImageID_Object = MibTableColumn
firmwareInfoImageID = _FirmwareInfoImageID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 1, 1, 1),
    _FirmwareInfoImageID_Type()
)
firmwareInfoImageID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareInfoImageID.setStatus("current")


class _FirmwareInfoVersion_Type(DisplayString):
    """Custom type firmwareInfoVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_FirmwareInfoVersion_Type.__name__ = "DisplayString"
_FirmwareInfoVersion_Object = MibTableColumn
firmwareInfoVersion = _FirmwareInfoVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 1, 1, 2),
    _FirmwareInfoVersion_Type()
)
firmwareInfoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareInfoVersion.setStatus("current")
_FirmwareInfoSizeB_Type = Unsigned32
_FirmwareInfoSizeB_Object = MibTableColumn
firmwareInfoSizeB = _FirmwareInfoSizeB_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 1, 1, 3),
    _FirmwareInfoSizeB_Type()
)
firmwareInfoSizeB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareInfoSizeB.setStatus("current")


class _FirmwareInfoUpdateTime_Type(DisplayString):
    """Custom type firmwareInfoUpdateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_FirmwareInfoUpdateTime_Type.__name__ = "DisplayString"
_FirmwareInfoUpdateTime_Object = MibTableColumn
firmwareInfoUpdateTime = _FirmwareInfoUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 1, 1, 4),
    _FirmwareInfoUpdateTime_Type()
)
firmwareInfoUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareInfoUpdateTime.setStatus("current")
_DevFunFwUpgradeAndBackup_ObjectIdentity = ObjectIdentity
devFunFwUpgradeAndBackup = _DevFunFwUpgradeAndBackup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 2)
)
_DevFunFwServerIpAddrType_Type = InetAddressType
_DevFunFwServerIpAddrType_Object = MibScalar
devFunFwServerIpAddrType = _DevFunFwServerIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 2, 1),
    _DevFunFwServerIpAddrType_Type()
)
devFunFwServerIpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devFunFwServerIpAddrType.setStatus("current")
_DevFunFwServerIpvxAddr_Type = InetAddress
_DevFunFwServerIpvxAddr_Object = MibScalar
devFunFwServerIpvxAddr = _DevFunFwServerIpvxAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 2, 2),
    _DevFunFwServerIpvxAddr_Type()
)
devFunFwServerIpvxAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devFunFwServerIpvxAddr.setStatus("current")


class _DevFunFwServerInterfaceName_Type(OctetString):
    """Custom type devFunFwServerInterfaceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DevFunFwServerInterfaceName_Type.__name__ = "OctetString"
_DevFunFwServerInterfaceName_Object = MibScalar
devFunFwServerInterfaceName = _DevFunFwServerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 2, 3),
    _DevFunFwServerInterfaceName_Type()
)
devFunFwServerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devFunFwServerInterfaceName.setStatus("current")


class _DevFunFwSrcFilename_Type(DisplayString):
    """Custom type devFunFwSrcFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_DevFunFwSrcFilename_Type.__name__ = "DisplayString"
_DevFunFwSrcFilename_Object = MibScalar
devFunFwSrcFilename = _DevFunFwSrcFilename_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 2, 4),
    _DevFunFwSrcFilename_Type()
)
devFunFwSrcFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devFunFwSrcFilename.setStatus("current")


class _DevFunFwOperation_Type(Integer32):
    """Custom type devFunFwOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("download", 1),
          ("none", 0),
          ("upload", 2))
    )


_DevFunFwOperation_Type.__name__ = "Integer32"
_DevFunFwOperation_Object = MibScalar
devFunFwOperation = _DevFunFwOperation_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 2, 5),
    _DevFunFwOperation_Type()
)
devFunFwOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devFunFwOperation.setStatus("current")


class _DevFunFwOperationStatus_Type(Integer32):
    """Custom type devFunFwOperationStatus based on Integer32"""
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
        *(("failure", 2),
          ("none", 0),
          ("progressing", 3),
          ("success", 1),
          ("transmit", 4))
    )


_DevFunFwOperationStatus_Type.__name__ = "Integer32"
_DevFunFwOperationStatus_Object = MibScalar
devFunFwOperationStatus = _DevFunFwOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 2, 6),
    _DevFunFwOperationStatus_Type()
)
devFunFwOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devFunFwOperationStatus.setStatus("current")


class _DevFunFwTransferPercentage_Type(Integer32):
    """Custom type devFunFwTransferPercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DevFunFwTransferPercentage_Type.__name__ = "Integer32"
_DevFunFwTransferPercentage_Object = MibScalar
devFunFwTransferPercentage = _DevFunFwTransferPercentage_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 2, 7),
    _DevFunFwTransferPercentage_Type()
)
devFunFwTransferPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devFunFwTransferPercentage.setStatus("current")


class _DevFunFwRetryCount_Type(Integer32):
    """Custom type devFunFwRetryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_DevFunFwRetryCount_Type.__name__ = "Integer32"
_DevFunFwRetryCount_Object = MibScalar
devFunFwRetryCount = _DevFunFwRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 2, 8),
    _DevFunFwRetryCount_Type()
)
devFunFwRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devFunFwRetryCount.setStatus("current")


class _DevFunFwServerStatus_Type(Integer32):
    """Custom type devFunFwServerStatus based on Integer32"""
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
        *(("accessViolation", 3),
          ("buffertoosmall", 12),
          ("connecthostfail", 6),
          ("createfilefail", 10),
          ("fileexists", 5),
          ("filetoohuge", 11),
          ("internalerror", 1),
          ("invalidarg", 7),
          ("memoryfull", 4),
          ("nofileerror", 2),
          ("ok", 0),
          ("programming", 14),
          ("readfail", 8),
          ("serverfail", 13),
          ("writefail", 9))
    )


_DevFunFwServerStatus_Type.__name__ = "Integer32"
_DevFunFwServerStatus_Object = MibScalar
devFunFwServerStatus = _DevFunFwServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 2, 9),
    _DevFunFwServerStatus_Type()
)
devFunFwServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devFunFwServerStatus.setStatus("current")


class _DevFwOperationImageId_Type(Integer32):
    """Custom type devFwOperationImageId based on Integer32"""
    defaultValue = 1


_DevFwOperationImageId_Object = MibScalar
devFwOperationImageId = _DevFwOperationImageId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 2, 10),
    _DevFwOperationImageId_Type()
)
devFwOperationImageId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devFwOperationImageId.setStatus("current")


class _DevFwNextBootImageId_Type(Integer32):
    """Custom type devFwNextBootImageId based on Integer32"""
    defaultValue = 1


_DevFwNextBootImageId_Object = MibScalar
devFwNextBootImageId = _DevFwNextBootImageId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 2, 11),
    _DevFwNextBootImageId_Type()
)
devFwNextBootImageId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devFwNextBootImageId.setStatus("current")
_DevFwActualBootImageId_Type = Integer32
_DevFwActualBootImageId_Object = MibScalar
devFwActualBootImageId = _DevFwActualBootImageId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 2, 12),
    _DevFwActualBootImageId_Type()
)
devFwActualBootImageId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devFwActualBootImageId.setStatus("current")
_DevFunConfigInfo_ObjectIdentity = ObjectIdentity
devFunConfigInfo = _DevFunConfigInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 3)
)
_DevFunCfgInfoTable_Object = MibTable
devFunCfgInfoTable = _DevFunCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    devFunCfgInfoTable.setStatus("current")
_DevFunCfgInfoEntry_Object = MibTableRow
devFunCfgInfoEntry = _DevFunCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 3, 1, 1)
)
devFunCfgInfoEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "devFunCfgId"),
)
if mibBuilder.loadTexts:
    devFunCfgInfoEntry.setStatus("current")
_DevFunCfgId_Type = Integer32
_DevFunCfgId_Object = MibTableColumn
devFunCfgId = _DevFunCfgId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 3, 1, 1, 1),
    _DevFunCfgId_Type()
)
devFunCfgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devFunCfgId.setStatus("current")


class _DevFunCfgSize_Type(Integer32):
    """Custom type devFunCfgSize based on Integer32"""
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


_DevFunCfgSize_Type.__name__ = "Integer32"
_DevFunCfgSize_Object = MibTableColumn
devFunCfgSize = _DevFunCfgSize_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 3, 1, 1, 2),
    _DevFunCfgSize_Type()
)
devFunCfgSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devFunCfgSize.setStatus("current")
_DevFunCfgUpdateTime_Type = DisplayString
_DevFunCfgUpdateTime_Object = MibTableColumn
devFunCfgUpdateTime = _DevFunCfgUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 3, 1, 1, 3),
    _DevFunCfgUpdateTime_Type()
)
devFunCfgUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devFunCfgUpdateTime.setStatus("current")
_DevFunConfiguration_ObjectIdentity = ObjectIdentity
devFunConfiguration = _DevFunConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 4)
)
_DevFunCfgServerIpAddrType_Type = InetAddressType
_DevFunCfgServerIpAddrType_Object = MibScalar
devFunCfgServerIpAddrType = _DevFunCfgServerIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 4, 1),
    _DevFunCfgServerIpAddrType_Type()
)
devFunCfgServerIpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devFunCfgServerIpAddrType.setStatus("current")
_DevFunCfgServerIpvxAddr_Type = InetAddress
_DevFunCfgServerIpvxAddr_Object = MibScalar
devFunCfgServerIpvxAddr = _DevFunCfgServerIpvxAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 4, 2),
    _DevFunCfgServerIpvxAddr_Type()
)
devFunCfgServerIpvxAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devFunCfgServerIpvxAddr.setStatus("current")


class _DevFunCfgSrcFilename_Type(DisplayString):
    """Custom type devFunCfgSrcFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_DevFunCfgSrcFilename_Type.__name__ = "DisplayString"
_DevFunCfgSrcFilename_Object = MibScalar
devFunCfgSrcFilename = _DevFunCfgSrcFilename_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 4, 3),
    _DevFunCfgSrcFilename_Type()
)
devFunCfgSrcFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devFunCfgSrcFilename.setStatus("current")


class _DevFunCfgStartUpConfigID_Type(Integer32):
    """Custom type devFunCfgStartUpConfigID based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("config1", 1),
          ("config2", 2))
    )


_DevFunCfgStartUpConfigID_Type.__name__ = "Integer32"
_DevFunCfgStartUpConfigID_Object = MibScalar
devFunCfgStartUpConfigID = _DevFunCfgStartUpConfigID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 4, 4),
    _DevFunCfgStartUpConfigID_Type()
)
devFunCfgStartUpConfigID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devFunCfgStartUpConfigID.setStatus("current")


class _DevFunCfgOperConfigID_Type(Integer32):
    """Custom type devFunCfgOperConfigID based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("config1", 1),
          ("config2", 2))
    )


_DevFunCfgOperConfigID_Type.__name__ = "Integer32"
_DevFunCfgOperConfigID_Object = MibScalar
devFunCfgOperConfigID = _DevFunCfgOperConfigID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 4, 5),
    _DevFunCfgOperConfigID_Type()
)
devFunCfgOperConfigID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devFunCfgOperConfigID.setStatus("current")


class _DevFunCfgOperation_Type(Integer32):
    """Custom type devFunCfgOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("download", 1),
          ("none", 0),
          ("upload", 2))
    )


_DevFunCfgOperation_Type.__name__ = "Integer32"
_DevFunCfgOperation_Object = MibScalar
devFunCfgOperation = _DevFunCfgOperation_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 4, 6),
    _DevFunCfgOperation_Type()
)
devFunCfgOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devFunCfgOperation.setStatus("current")


class _DevFunCfgSave_Type(Integer32):
    """Custom type devFunCfgSave based on Integer32"""
    defaultValue = 2

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


_DevFunCfgSave_Type.__name__ = "Integer32"
_DevFunCfgSave_Object = MibScalar
devFunCfgSave = _DevFunCfgSave_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 4, 7),
    _DevFunCfgSave_Type()
)
devFunCfgSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devFunCfgSave.setStatus("current")


class _DevFunCfgOperationStatus_Type(Integer32):
    """Custom type devFunCfgOperationStatus based on Integer32"""
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
        *(("failure", 2),
          ("none", 0),
          ("progressing", 3),
          ("success", 1),
          ("transmit", 4))
    )


_DevFunCfgOperationStatus_Type.__name__ = "Integer32"
_DevFunCfgOperationStatus_Object = MibScalar
devFunCfgOperationStatus = _DevFunCfgOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 4, 8),
    _DevFunCfgOperationStatus_Type()
)
devFunCfgOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devFunCfgOperationStatus.setStatus("current")


class _DevFunCfgTransferPercentage_Type(Integer32):
    """Custom type devFunCfgTransferPercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DevFunCfgTransferPercentage_Type.__name__ = "Integer32"
_DevFunCfgTransferPercentage_Object = MibScalar
devFunCfgTransferPercentage = _DevFunCfgTransferPercentage_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 4, 9),
    _DevFunCfgTransferPercentage_Type()
)
devFunCfgTransferPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devFunCfgTransferPercentage.setStatus("current")


class _DevFunCfgServerInterfaceName_Type(OctetString):
    """Custom type devFunCfgServerInterfaceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DevFunCfgServerInterfaceName_Type.__name__ = "OctetString"
_DevFunCfgServerInterfaceName_Object = MibScalar
devFunCfgServerInterfaceName = _DevFunCfgServerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 4, 10),
    _DevFunCfgServerInterfaceName_Type()
)
devFunCfgServerInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devFunCfgServerInterfaceName.setStatus("current")


class _DevFunCfgServerStatus_Type(Integer32):
    """Custom type devFunCfgServerStatus based on Integer32"""
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
        *(("accessViolation", 3),
          ("buffertoosmall", 12),
          ("connecthostfail", 6),
          ("createfilefail", 10),
          ("fileexists", 5),
          ("filetoohuge", 11),
          ("internalerror", 1),
          ("invalidarg", 7),
          ("memoryfull", 4),
          ("nofileerror", 2),
          ("ok", 0),
          ("programming", 14),
          ("readfail", 8),
          ("serverfail", 13),
          ("writefail", 9))
    )


_DevFunCfgServerStatus_Type.__name__ = "Integer32"
_DevFunCfgServerStatus_Object = MibScalar
devFunCfgServerStatus = _DevFunCfgServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 4, 11),
    _DevFunCfgServerStatus_Type()
)
devFunCfgServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devFunCfgServerStatus.setStatus("current")


class _DevFunCfgCurrStartUpConfigID_Type(Integer32):
    """Custom type devFunCfgCurrStartUpConfigID based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("config1", 1),
          ("config2", 2))
    )


_DevFunCfgCurrStartUpConfigID_Type.__name__ = "Integer32"
_DevFunCfgCurrStartUpConfigID_Object = MibScalar
devFunCfgCurrStartUpConfigID = _DevFunCfgCurrStartUpConfigID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 4, 12),
    _DevFunCfgCurrStartUpConfigID_Type()
)
devFunCfgCurrStartUpConfigID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devFunCfgCurrStartUpConfigID.setStatus("current")
_DevFunLogBackup_ObjectIdentity = ObjectIdentity
devFunLogBackup = _DevFunLogBackup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 5)
)


class _DevFunLogBackupToTftpIpType_Type(Integer32):
    """Custom type devFunLogBackupToTftpIpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_DevFunLogBackupToTftpIpType_Type.__name__ = "Integer32"
_DevFunLogBackupToTftpIpType_Object = MibScalar
devFunLogBackupToTftpIpType = _DevFunLogBackupToTftpIpType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 5, 1),
    _DevFunLogBackupToTftpIpType_Type()
)
devFunLogBackupToTftpIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devFunLogBackupToTftpIpType.setStatus("current")
_DevFunLogBackupToTftpIpAddr_Type = InetAddress
_DevFunLogBackupToTftpIpAddr_Object = MibScalar
devFunLogBackupToTftpIpAddr = _DevFunLogBackupToTftpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 5, 2),
    _DevFunLogBackupToTftpIpAddr_Type()
)
devFunLogBackupToTftpIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devFunLogBackupToTftpIpAddr.setStatus("current")


class _DevFunLogBackupToTftpDestURL_Type(DisplayString):
    """Custom type devFunLogBackupToTftpDestURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_DevFunLogBackupToTftpDestURL_Type.__name__ = "DisplayString"
_DevFunLogBackupToTftpDestURL_Object = MibScalar
devFunLogBackupToTftpDestURL = _DevFunLogBackupToTftpDestURL_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 5, 3),
    _DevFunLogBackupToTftpDestURL_Type()
)
devFunLogBackupToTftpDestURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devFunLogBackupToTftpDestURL.setStatus("obsolete")


class _DevFunLogBackupToTftpOper_Type(Integer32):
    """Custom type devFunLogBackupToTftpOper based on Integer32"""
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


_DevFunLogBackupToTftpOper_Type.__name__ = "Integer32"
_DevFunLogBackupToTftpOper_Object = MibScalar
devFunLogBackupToTftpOper = _DevFunLogBackupToTftpOper_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 5, 4),
    _DevFunLogBackupToTftpOper_Type()
)
devFunLogBackupToTftpOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devFunLogBackupToTftpOper.setStatus("obsolete")


class _DevFunLogBackupToTftStatus_Type(Integer32):
    """Custom type devFunLogBackupToTftStatus based on Integer32"""
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
          ("none", 0),
          ("progressing", 3),
          ("success", 1))
    )


_DevFunLogBackupToTftStatus_Type.__name__ = "Integer32"
_DevFunLogBackupToTftStatus_Object = MibScalar
devFunLogBackupToTftStatus = _DevFunLogBackupToTftStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 5, 5),
    _DevFunLogBackupToTftStatus_Type()
)
devFunLogBackupToTftStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devFunLogBackupToTftStatus.setStatus("obsolete")
_DevFunPing_ObjectIdentity = ObjectIdentity
devFunPing = _DevFunPing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 6)
)


class _DevPingDestIpType_Type(Integer32):
    """Custom type devPingDestIpType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_DevPingDestIpType_Type.__name__ = "Integer32"
_DevPingDestIpType_Object = MibScalar
devPingDestIpType = _DevPingDestIpType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 6, 1),
    _DevPingDestIpType_Type()
)
devPingDestIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devPingDestIpType.setStatus("current")
_DevPingDestIpAddr_Type = InetAddress
_DevPingDestIpAddr_Object = MibScalar
devPingDestIpAddr = _DevPingDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 6, 2),
    _DevPingDestIpAddr_Type()
)
devPingDestIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devPingDestIpAddr.setStatus("current")


class _DevPingTimeout_Type(Integer32):
    """Custom type devPingTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_DevPingTimeout_Type.__name__ = "Integer32"
_DevPingTimeout_Object = MibScalar
devPingTimeout = _DevPingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 6, 3),
    _DevPingTimeout_Type()
)
devPingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devPingTimeout.setStatus("current")


class _DevPingTimes_Type(Integer32):
    """Custom type devPingTimes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DevPingTimes_Type.__name__ = "Integer32"
_DevPingTimes_Object = MibScalar
devPingTimes = _DevPingTimes_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 6, 4),
    _DevPingTimes_Type()
)
devPingTimes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devPingTimes.setStatus("current")


class _DevPingStart_Type(Integer32):
    """Custom type devPingStart based on Integer32"""
    defaultValue = 2

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


_DevPingStart_Type.__name__ = "Integer32"
_DevPingStart_Object = MibScalar
devPingStart = _DevPingStart_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 6, 5),
    _DevPingStart_Type()
)
devPingStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devPingStart.setStatus("current")


class _DevPingStatus_Type(Integer32):
    """Custom type devPingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("completed", 3),
          ("notinitiated", 1),
          ("progress", 2))
    )


_DevPingStatus_Type.__name__ = "Integer32"
_DevPingStatus_Object = MibScalar
devPingStatus = _DevPingStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 6, 6),
    _DevPingStatus_Type()
)
devPingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devPingStatus.setStatus("current")
_DevPingSuccesses_Type = Integer32
_DevPingSuccesses_Object = MibScalar
devPingSuccesses = _DevPingSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 6, 7),
    _DevPingSuccesses_Type()
)
devPingSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devPingSuccesses.setStatus("current")
_DevPingV4ProbeHistoryTable_Object = MibTable
devPingV4ProbeHistoryTable = _DevPingV4ProbeHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 6, 8)
)
if mibBuilder.loadTexts:
    devPingV4ProbeHistoryTable.setStatus("current")
_DevPingV4ProbeHistoryEntry_Object = MibTableRow
devPingV4ProbeHistoryEntry = _DevPingV4ProbeHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 6, 8, 1)
)
devPingV4ProbeHistoryEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "devPingIndex"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "devPingProbeIndex"),
)
if mibBuilder.loadTexts:
    devPingV4ProbeHistoryEntry.setStatus("current")
_DevPingIndex_Type = Integer32
_DevPingIndex_Object = MibTableColumn
devPingIndex = _DevPingIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 6, 8, 1, 1),
    _DevPingIndex_Type()
)
devPingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devPingIndex.setStatus("current")
_DevPingProbeIndex_Type = Integer32
_DevPingProbeIndex_Object = MibTableColumn
devPingProbeIndex = _DevPingProbeIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 6, 8, 1, 2),
    _DevPingProbeIndex_Type()
)
devPingProbeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devPingProbeIndex.setStatus("current")
_DevPingProbeHistoryResponseTime_Type = Unsigned32
_DevPingProbeHistoryResponseTime_Object = MibTableColumn
devPingProbeHistoryResponseTime = _DevPingProbeHistoryResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 6, 8, 1, 3),
    _DevPingProbeHistoryResponseTime_Type()
)
devPingProbeHistoryResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devPingProbeHistoryResponseTime.setStatus("current")
_DevIpv6PingProbeHistoryTable_Object = MibTable
devIpv6PingProbeHistoryTable = _DevIpv6PingProbeHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 6, 9)
)
if mibBuilder.loadTexts:
    devIpv6PingProbeHistoryTable.setStatus("current")
_DevIpv6PingProbeHistoryEntry_Object = MibTableRow
devIpv6PingProbeHistoryEntry = _DevIpv6PingProbeHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 6, 9, 1)
)
devIpv6PingProbeHistoryEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "devIpv6PingIndex"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "devIpv6PingProbeIndex"),
)
if mibBuilder.loadTexts:
    devIpv6PingProbeHistoryEntry.setStatus("current")
_DevIpv6PingIndex_Type = Integer32
_DevIpv6PingIndex_Object = MibTableColumn
devIpv6PingIndex = _DevIpv6PingIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 6, 9, 1, 1),
    _DevIpv6PingIndex_Type()
)
devIpv6PingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devIpv6PingIndex.setStatus("current")
_DevIpv6PingProbeIndex_Type = Integer32
_DevIpv6PingProbeIndex_Object = MibTableColumn
devIpv6PingProbeIndex = _DevIpv6PingProbeIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 6, 9, 1, 2),
    _DevIpv6PingProbeIndex_Type()
)
devIpv6PingProbeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devIpv6PingProbeIndex.setStatus("current")
_DevIpv6PingProbeHistoryResponseTime_Type = Unsigned32
_DevIpv6PingProbeHistoryResponseTime_Object = MibTableColumn
devIpv6PingProbeHistoryResponseTime = _DevIpv6PingProbeHistoryResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 6, 9, 1, 3),
    _DevIpv6PingProbeHistoryResponseTime_Type()
)
devIpv6PingProbeHistoryResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devIpv6PingProbeHistoryResponseTime.setStatus("current")
_DevFunLangMgmt_ObjectIdentity = ObjectIdentity
devFunLangMgmt = _DevFunLangMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 7)
)


class _DevFunLangMgmtFile_Type(DisplayString):
    """Custom type devFunLangMgmtFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_DevFunLangMgmtFile_Type.__name__ = "DisplayString"
_DevFunLangMgmtFile_Object = MibScalar
devFunLangMgmtFile = _DevFunLangMgmtFile_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 7, 1),
    _DevFunLangMgmtFile_Type()
)
devFunLangMgmtFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devFunLangMgmtFile.setStatus("obsolete")
_DevFunLangMgmtApply_Type = TruthValue
_DevFunLangMgmtApply_Object = MibScalar
devFunLangMgmtApply = _DevFunLangMgmtApply_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 7, 2),
    _DevFunLangMgmtApply_Type()
)
devFunLangMgmtApply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devFunLangMgmtApply.setStatus("current")


class _DevFunRestart_Type(Integer32):
    """Custom type devFunRestart based on Integer32"""
    defaultValue = 1

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
        *(("noreboot", 1),
          ("reboot", 2),
          ("reset", 3),
          ("resetwithoutip", 4))
    )


_DevFunRestart_Type.__name__ = "Integer32"
_DevFunRestart_Object = MibScalar
devFunRestart = _DevFunRestart_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 8),
    _DevFunRestart_Type()
)
devFunRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devFunRestart.setStatus("current")


class _DevFunWizardIgnoreNextTime_Type(Integer32):
    """Custom type devFunWizardIgnoreNextTime based on Integer32"""
    defaultValue = 2

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


_DevFunWizardIgnoreNextTime_Type.__name__ = "Integer32"
_DevFunWizardIgnoreNextTime_Object = MibScalar
devFunWizardIgnoreNextTime = _DevFunWizardIgnoreNextTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 2, 9),
    _DevFunWizardIgnoreNextTime_Type()
)
devFunWizardIgnoreNextTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devFunWizardIgnoreNextTime.setStatus("current")
_DeviceErrorCodeInformation_ObjectIdentity = ObjectIdentity
deviceErrorCodeInformation = _DeviceErrorCodeInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 3)
)
_DeviceErrorCodeTable_Object = MibTable
deviceErrorCodeTable = _DeviceErrorCodeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    deviceErrorCodeTable.setStatus("current")
_DeviceErrorCodeEntry_Object = MibTableRow
deviceErrorCodeEntry = _DeviceErrorCodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 3, 1, 1)
)
deviceErrorCodeEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "devErrorCodeIndex"),
)
if mibBuilder.loadTexts:
    deviceErrorCodeEntry.setStatus("current")
_DevErrorCodeIndex_Type = Integer32
_DevErrorCodeIndex_Object = MibTableColumn
devErrorCodeIndex = _DevErrorCodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 3, 1, 1, 1),
    _DevErrorCodeIndex_Type()
)
devErrorCodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devErrorCodeIndex.setStatus("current")
_DevErrorString_Type = DisplayString
_DevErrorString_Object = MibTableColumn
devErrorString = _DevErrorString_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 3, 1, 1, 2),
    _DevErrorString_Type()
)
devErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devErrorString.setStatus("current")
_DeviceFan_ObjectIdentity = ObjectIdentity
deviceFan = _DeviceFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 4)
)


class _DeviceFanStatus_Type(Integer32):
    """Custom type deviceFanStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fail", 1),
          ("ok", 0))
    )


_DeviceFanStatus_Type.__name__ = "Integer32"
_DeviceFanStatus_Object = MibScalar
deviceFanStatus = _DeviceFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 1, 1, 4, 1),
    _DeviceFanStatus_Type()
)
deviceFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceFanStatus.setStatus("current")
_DlinkSystem_ObjectIdentity = ObjectIdentity
dlinkSystem = _DlinkSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2)
)
_SysInformationGroup_ObjectIdentity = ObjectIdentity
sysInformationGroup = _SysInformationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 1)
)


class _SystemName_Type(DisplayString):
    """Custom type systemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SystemName_Type.__name__ = "DisplayString"
_SystemName_Object = MibScalar
systemName = _SystemName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 1, 1),
    _SystemName_Type()
)
systemName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemName.setStatus("current")


class _SystemLocation_Type(DisplayString):
    """Custom type systemLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemLocation_Type.__name__ = "DisplayString"
_SystemLocation_Object = MibScalar
systemLocation = _SystemLocation_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 1, 2),
    _SystemLocation_Type()
)
systemLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLocation.setStatus("current")


class _SystemContact_Type(DisplayString):
    """Custom type systemContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemContact_Type.__name__ = "DisplayString"
_SystemContact_Object = MibScalar
systemContact = _SystemContact_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 1, 3),
    _SystemContact_Type()
)
systemContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemContact.setStatus("current")
_SyslogGroup_ObjectIdentity = ObjectIdentity
syslogGroup = _SyslogGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 4)
)
_SyslogMIBObjects_ObjectIdentity = ObjectIdentity
syslogMIBObjects = _SyslogMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 4, 1)
)
_SyslogGeneral_ObjectIdentity = ObjectIdentity
syslogGeneral = _SyslogGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 4, 1, 1)
)


class _SyslogSourceInterfaceState_Type(Integer32):
    """Custom type syslogSourceInterfaceState based on Integer32"""
    defaultValue = 1

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


_SyslogSourceInterfaceState_Type.__name__ = "Integer32"
_SyslogSourceInterfaceState_Object = MibScalar
syslogSourceInterfaceState = _SyslogSourceInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 4, 1, 1, 1),
    _SyslogSourceInterfaceState_Type()
)
syslogSourceInterfaceState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogSourceInterfaceState.setStatus("current")


class _SyslogSourceInterfaceVID_Type(Integer32):
    """Custom type syslogSourceInterfaceVID based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SyslogSourceInterfaceVID_Type.__name__ = "Integer32"
_SyslogSourceInterfaceVID_Object = MibScalar
syslogSourceInterfaceVID = _SyslogSourceInterfaceVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 4, 1, 1, 2),
    _SyslogSourceInterfaceVID_Type()
)
syslogSourceInterfaceVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogSourceInterfaceVID.setStatus("current")
_SyslogLogbuffer_ObjectIdentity = ObjectIdentity
syslogLogbuffer = _SyslogLogbuffer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 4, 1, 2)
)


class _SyslogClearLogBuffer_Type(TruthValue):
    """Custom type syslogClearLogBuffer based on TruthValue"""


_SyslogClearLogBuffer_Object = MibScalar
syslogClearLogBuffer = _SyslogClearLogBuffer_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 4, 1, 2, 1),
    _SyslogClearLogBuffer_Type()
)
syslogClearLogBuffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogClearLogBuffer.setStatus("current")


class _SyslogLogBufferEnabled_Type(Integer32):
    """Custom type syslogLogBufferEnabled based on Integer32"""
    defaultValue = 1

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


_SyslogLogBufferEnabled_Type.__name__ = "Integer32"
_SyslogLogBufferEnabled_Object = MibScalar
syslogLogBufferEnabled = _SyslogLogBufferEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 4, 1, 2, 2),
    _SyslogLogBufferEnabled_Type()
)
syslogLogBufferEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogLogBufferEnabled.setStatus("current")


class _SyslogLogBufSeverity_Type(Integer32):
    """Custom type syslogLogBufSeverity based on Integer32"""
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
        *(("alerts", 1),
          ("critical", 2),
          ("debugging", 7),
          ("emergencies", 0),
          ("errors", 3),
          ("informational", 6),
          ("notifications", 5),
          ("warnings", 4))
    )


_SyslogLogBufSeverity_Type.__name__ = "Integer32"
_SyslogLogBufSeverity_Object = MibScalar
syslogLogBufSeverity = _SyslogLogBufSeverity_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 4, 1, 2, 3),
    _SyslogLogBufSeverity_Type()
)
syslogLogBufSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogLogBufSeverity.setStatus("current")
_SyslogLogBufWriteDelay_Type = Integer32
_SyslogLogBufWriteDelay_Object = MibScalar
syslogLogBufWriteDelay = _SyslogLogBufWriteDelay_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 4, 1, 2, 4),
    _SyslogLogBufWriteDelay_Type()
)
syslogLogBufWriteDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogLogBufWriteDelay.setStatus("current")
if mibBuilder.loadTexts:
    syslogLogBufWriteDelay.setUnits("seconds")
_SyslogServerTable_Object = MibTable
syslogServerTable = _SyslogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 4, 1, 5)
)
if mibBuilder.loadTexts:
    syslogServerTable.setStatus("current")
_SyslogServerEntry_Object = MibTableRow
syslogServerEntry = _SyslogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 4, 1, 5, 1)
)
syslogServerEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "syslogServerIndex"),
)
if mibBuilder.loadTexts:
    syslogServerEntry.setStatus("current")


class _SyslogServerIndex_Type(Integer32):
    """Custom type syslogServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SyslogServerIndex_Type.__name__ = "Integer32"
_SyslogServerIndex_Object = MibTableColumn
syslogServerIndex = _SyslogServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 4, 1, 5, 1, 1),
    _SyslogServerIndex_Type()
)
syslogServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogServerIndex.setStatus("current")
_SyslogServerAddressType_Type = InetAddressType
_SyslogServerAddressType_Object = MibTableColumn
syslogServerAddressType = _SyslogServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 4, 1, 5, 1, 2),
    _SyslogServerAddressType_Type()
)
syslogServerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServerAddressType.setStatus("current")
_SyslogServerAddress_Type = InetAddress
_SyslogServerAddress_Object = MibTableColumn
syslogServerAddress = _SyslogServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 4, 1, 5, 1, 3),
    _SyslogServerAddress_Type()
)
syslogServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServerAddress.setStatus("current")


class _SyslogServerPort_Type(Integer32):
    """Custom type syslogServerPort based on Integer32"""
    defaultValue = 514

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(514, 514),
        ValueRangeConstraint(1024, 65535),
    )


_SyslogServerPort_Type.__name__ = "Integer32"
_SyslogServerPort_Object = MibTableColumn
syslogServerPort = _SyslogServerPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 4, 1, 5, 1, 4),
    _SyslogServerPort_Type()
)
syslogServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServerPort.setStatus("current")


class _SyslogServerSeverity_Type(Integer32):
    """Custom type syslogServerSeverity based on Integer32"""
    defaultValue = 4

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
        *(("alerts", 1),
          ("critical", 2),
          ("debugging", 7),
          ("emergencie", 0),
          ("error", 3),
          ("informational", 6),
          ("notification", 5),
          ("warning", 4))
    )


_SyslogServerSeverity_Type.__name__ = "Integer32"
_SyslogServerSeverity_Object = MibTableColumn
syslogServerSeverity = _SyslogServerSeverity_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 4, 1, 5, 1, 5),
    _SyslogServerSeverity_Type()
)
syslogServerSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServerSeverity.setStatus("current")


class _SyslogServerFacility_Type(Integer32):
    """Custom type syslogServerFacility based on Integer32"""
    defaultValue = 0

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
        *(("audit", 13),
          ("auth", 4),
          ("authpriv", 10),
          ("console", 14),
          ("cron", 9),
          ("cron2", 15),
          ("daemon", 3),
          ("ftp", 11),
          ("kern", 0),
          ("local0", 16),
          ("local1", 17),
          ("local2", 18),
          ("local3", 19),
          ("local4", 20),
          ("local5", 21),
          ("local6", 22),
          ("local7", 23),
          ("lpr", 6),
          ("mail", 2),
          ("news", 7),
          ("ntp", 12),
          ("syslog", 5),
          ("user", 1),
          ("uucp", 8))
    )


_SyslogServerFacility_Type.__name__ = "Integer32"
_SyslogServerFacility_Object = MibTableColumn
syslogServerFacility = _SyslogServerFacility_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 4, 1, 5, 1, 6),
    _SyslogServerFacility_Type()
)
syslogServerFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServerFacility.setStatus("current")
_SyslogServerRowstatus_Type = RowStatus
_SyslogServerRowstatus_Object = MibTableColumn
syslogServerRowstatus = _SyslogServerRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 4, 1, 5, 1, 7),
    _SyslogServerRowstatus_Type()
)
syslogServerRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogServerRowstatus.setStatus("current")
_SyslogBufferTableNum_Type = Unsigned32
_SyslogBufferTableNum_Object = MibScalar
syslogBufferTableNum = _SyslogBufferTableNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 4, 1, 6),
    _SyslogBufferTableNum_Type()
)
syslogBufferTableNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogBufferTableNum.setStatus("current")
_SyslogBufferTable_Object = MibTable
syslogBufferTable = _SyslogBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 4, 1, 7)
)
if mibBuilder.loadTexts:
    syslogBufferTable.setStatus("current")
_SyslogBufferEntry_Object = MibTableRow
syslogBufferEntry = _SyslogBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 4, 1, 7, 1)
)
syslogBufferEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "syslogBufferIndex"),
)
if mibBuilder.loadTexts:
    syslogBufferEntry.setStatus("current")


class _SyslogBufferIndex_Type(Unsigned32):
    """Custom type syslogBufferIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_SyslogBufferIndex_Type.__name__ = "Unsigned32"
_SyslogBufferIndex_Object = MibTableColumn
syslogBufferIndex = _SyslogBufferIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 4, 1, 7, 1, 1),
    _SyslogBufferIndex_Type()
)
syslogBufferIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogBufferIndex.setStatus("current")
_SyslogBufferDateAndTime_Type = DisplayString
_SyslogBufferDateAndTime_Object = MibTableColumn
syslogBufferDateAndTime = _SyslogBufferDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 4, 1, 7, 1, 2),
    _SyslogBufferDateAndTime_Type()
)
syslogBufferDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogBufferDateAndTime.setStatus("current")
_SyslogBufferDescription_Type = DisplayString
_SyslogBufferDescription_Object = MibTableColumn
syslogBufferDescription = _SyslogBufferDescription_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 4, 1, 7, 1, 3),
    _SyslogBufferDescription_Type()
)
syslogBufferDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogBufferDescription.setStatus("current")


class _SyslogBufferSeverity_Type(Integer32):
    """Custom type syslogBufferSeverity based on Integer32"""
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
        *(("alerts", 1),
          ("critical", 2),
          ("debugging", 7),
          ("emergencie", 0),
          ("error", 3),
          ("informational", 6),
          ("notification", 5),
          ("warning", 4))
    )


_SyslogBufferSeverity_Type.__name__ = "Integer32"
_SyslogBufferSeverity_Object = MibTableColumn
syslogBufferSeverity = _SyslogBufferSeverity_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 4, 1, 7, 1, 4),
    _SyslogBufferSeverity_Type()
)
syslogBufferSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogBufferSeverity.setStatus("current")
_SysPortConfigGroup_ObjectIdentity = ObjectIdentity
sysPortConfigGroup = _SysPortConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13)
)
_PortCtrlTable_Object = MibTable
portCtrlTable = _PortCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 1)
)
if mibBuilder.loadTexts:
    portCtrlTable.setStatus("current")
_PortCtrlEntry_Object = MibTableRow
portCtrlEntry = _PortCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 1, 1)
)
portCtrlEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "portSetIndex"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "portSetMediaType"),
)
if mibBuilder.loadTexts:
    portCtrlEntry.setStatus("current")


class _PortSetIndex_Type(Integer32):
    """Custom type portSetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PortSetIndex_Type.__name__ = "Integer32"
_PortSetIndex_Object = MibTableColumn
portSetIndex = _PortSetIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 1, 1, 1),
    _PortSetIndex_Type()
)
portSetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSetIndex.setStatus("current")


class _PortSetMediaType_Type(Integer32):
    """Custom type portSetMediaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copper", 1),
          ("fiber", 2))
    )


_PortSetMediaType_Type.__name__ = "Integer32"
_PortSetMediaType_Object = MibTableColumn
portSetMediaType = _PortSetMediaType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 1, 1, 2),
    _PortSetMediaType_Type()
)
portSetMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSetMediaType.setStatus("current")


class _PortSetState_Type(Integer32):
    """Custom type portSetState based on Integer32"""
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


_PortSetState_Type.__name__ = "Integer32"
_PortSetState_Object = MibTableColumn
portSetState = _PortSetState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 1, 1, 3),
    _PortSetState_Type()
)
portSetState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSetState.setStatus("current")


class _PortSetAutoDowngrade_Type(Integer32):
    """Custom type portSetAutoDowngrade based on Integer32"""
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


_PortSetAutoDowngrade_Type.__name__ = "Integer32"
_PortSetAutoDowngrade_Object = MibTableColumn
portSetAutoDowngrade = _PortSetAutoDowngrade_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 1, 1, 4),
    _PortSetAutoDowngrade_Type()
)
portSetAutoDowngrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSetAutoDowngrade.setStatus("current")


class _PortSetFlowControl_Type(Integer32):
    """Custom type portSetFlowControl based on Integer32"""
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


_PortSetFlowControl_Type.__name__ = "Integer32"
_PortSetFlowControl_Object = MibTableColumn
portSetFlowControl = _PortSetFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 1, 1, 5),
    _PortSetFlowControl_Type()
)
portSetFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSetFlowControl.setStatus("current")


class _PortSetDuplex_Type(Integer32):
    """Custom type portSetDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("full", 2))
    )


_PortSetDuplex_Type.__name__ = "Integer32"
_PortSetDuplex_Object = MibTableColumn
portSetDuplex = _PortSetDuplex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 1, 1, 6),
    _PortSetDuplex_Type()
)
portSetDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSetDuplex.setStatus("current")


class _PortSetSpeed_Type(Integer32):
    """Custom type portSetSpeed based on Integer32"""
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
        *(("auto", 1),
          ("rate1000M", 3),
          ("rate1000M-Master", 4),
          ("rate1000M-Slave", 5),
          ("rate100M", 2),
          ("rate10G", 6))
    )


_PortSetSpeed_Type.__name__ = "Integer32"
_PortSetSpeed_Object = MibTableColumn
portSetSpeed = _PortSetSpeed_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 1, 1, 7),
    _PortSetSpeed_Type()
)
portSetSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSetSpeed.setStatus("current")


class _PortSetCapaAdvertised_Type(Integer32):
    """Custom type portSetCapaAdvertised based on Integer32"""
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
        *(("adv100M", 1),
          ("adv100M_10G", 5),
          ("adv100M_1G", 3),
          ("adv100M_1G_10G", 7),
          ("adv10G", 4),
          ("adv1G", 2),
          ("adv1G_10G", 6))
    )


_PortSetCapaAdvertised_Type.__name__ = "Integer32"
_PortSetCapaAdvertised_Object = MibTableColumn
portSetCapaAdvertised = _PortSetCapaAdvertised_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 1, 1, 8),
    _PortSetCapaAdvertised_Type()
)
portSetCapaAdvertised.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSetCapaAdvertised.setStatus("current")


class _PortSetDescription_Type(DisplayString):
    """Custom type portSetDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_PortSetDescription_Type.__name__ = "DisplayString"
_PortSetDescription_Object = MibTableColumn
portSetDescription = _PortSetDescription_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 1, 1, 9),
    _PortSetDescription_Type()
)
portSetDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSetDescription.setStatus("current")


class _PortSetLinkStatus_Type(Integer32):
    """Custom type portSetLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_PortSetLinkStatus_Type.__name__ = "Integer32"
_PortSetLinkStatus_Object = MibTableColumn
portSetLinkStatus = _PortSetLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 1, 1, 10),
    _PortSetLinkStatus_Type()
)
portSetLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSetLinkStatus.setStatus("current")
_PortStatusTable_Object = MibTable
portStatusTable = _PortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 2)
)
if mibBuilder.loadTexts:
    portStatusTable.setStatus("current")
_PortStatusEntry_Object = MibTableRow
portStatusEntry = _PortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 2, 1)
)
portStatusEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "portStaIndex"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "portStaMediaType"),
)
if mibBuilder.loadTexts:
    portStatusEntry.setStatus("current")


class _PortStaIndex_Type(Integer32):
    """Custom type portStaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PortStaIndex_Type.__name__ = "Integer32"
_PortStaIndex_Object = MibTableColumn
portStaIndex = _PortStaIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 2, 1, 1),
    _PortStaIndex_Type()
)
portStaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStaIndex.setStatus("current")


class _PortStaMediaType_Type(Integer32):
    """Custom type portStaMediaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copper", 1),
          ("fiber", 2))
    )


_PortStaMediaType_Type.__name__ = "Integer32"
_PortStaMediaType_Object = MibTableColumn
portStaMediaType = _PortStaMediaType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 2, 1, 2),
    _PortStaMediaType_Type()
)
portStaMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStaMediaType.setStatus("current")


class _PortStaStatus_Type(Integer32):
    """Custom type portStaStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("notconnected", 2))
    )


_PortStaStatus_Type.__name__ = "Integer32"
_PortStaStatus_Object = MibTableColumn
portStaStatus = _PortStaStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 2, 1, 3),
    _PortStaStatus_Type()
)
portStaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStaStatus.setStatus("current")
_PortStaMacAddr_Type = MacAddress
_PortStaMacAddr_Object = MibTableColumn
portStaMacAddr = _PortStaMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 2, 1, 4),
    _PortStaMacAddr_Type()
)
portStaMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStaMacAddr.setStatus("current")
_PortStaVlan_Type = Integer32
_PortStaVlan_Object = MibTableColumn
portStaVlan = _PortStaVlan_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 2, 1, 5),
    _PortStaVlan_Type()
)
portStaVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStaVlan.setStatus("current")


class _PortStaFlowCtrlOpSend_Type(Integer32):
    """Custom type portStaFlowCtrlOpSend based on Integer32"""
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


_PortStaFlowCtrlOpSend_Type.__name__ = "Integer32"
_PortStaFlowCtrlOpSend_Object = MibTableColumn
portStaFlowCtrlOpSend = _PortStaFlowCtrlOpSend_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 2, 1, 6),
    _PortStaFlowCtrlOpSend_Type()
)
portStaFlowCtrlOpSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStaFlowCtrlOpSend.setStatus("current")


class _PortStaFlowCtrlOpRece_Type(Integer32):
    """Custom type portStaFlowCtrlOpRece based on Integer32"""
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


_PortStaFlowCtrlOpRece_Type.__name__ = "Integer32"
_PortStaFlowCtrlOpRece_Object = MibTableColumn
portStaFlowCtrlOpRece = _PortStaFlowCtrlOpRece_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 2, 1, 7),
    _PortStaFlowCtrlOpRece_Type()
)
portStaFlowCtrlOpRece.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStaFlowCtrlOpRece.setStatus("current")


class _PortStaDuplex_Type(Integer32):
    """Custom type portStaDuplex based on Integer32"""
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
        *(("auto", 1),
          ("auto-falf", 4),
          ("auto-full", 3),
          ("full", 2))
    )


_PortStaDuplex_Type.__name__ = "Integer32"
_PortStaDuplex_Object = MibTableColumn
portStaDuplex = _PortStaDuplex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 2, 1, 8),
    _PortStaDuplex_Type()
)
portStaDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStaDuplex.setStatus("current")


class _PortStaSpeed_Type(Integer32):
    """Custom type portStaSpeed based on Integer32"""
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
        *(("auto", 1),
          ("auto-rate1000M", 8),
          ("auto-rate100M", 7),
          ("auto-rate10G", 9),
          ("rate1000M", 3),
          ("rate1000M-Master", 4),
          ("rate1000M-Slave", 5),
          ("rate100M", 2),
          ("rate10G", 6))
    )


_PortStaSpeed_Type.__name__ = "Integer32"
_PortStaSpeed_Object = MibTableColumn
portStaSpeed = _PortStaSpeed_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 2, 1, 9),
    _PortStaSpeed_Type()
)
portStaSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStaSpeed.setStatus("current")


class _ErrDisAssertTrapState_Type(Integer32):
    """Custom type errDisAssertTrapState based on Integer32"""
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


_ErrDisAssertTrapState_Type.__name__ = "Integer32"
_ErrDisAssertTrapState_Object = MibScalar
errDisAssertTrapState = _ErrDisAssertTrapState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 3),
    _ErrDisAssertTrapState_Type()
)
errDisAssertTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errDisAssertTrapState.setStatus("current")


class _ErrDisClearTrapState_Type(Integer32):
    """Custom type errDisClearTrapState based on Integer32"""
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


_ErrDisClearTrapState_Type.__name__ = "Integer32"
_ErrDisClearTrapState_Object = MibScalar
errDisClearTrapState = _ErrDisClearTrapState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 4),
    _ErrDisClearTrapState_Type()
)
errDisClearTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errDisClearTrapState.setStatus("current")
_ErrDisNotificationRate_Type = Integer32
_ErrDisNotificationRate_Object = MibScalar
errDisNotificationRate = _ErrDisNotificationRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 5),
    _ErrDisNotificationRate_Type()
)
errDisNotificationRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errDisNotificationRate.setStatus("current")
_ErrDisIfStatusTable_Object = MibTable
errDisIfStatusTable = _ErrDisIfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 6)
)
if mibBuilder.loadTexts:
    errDisIfStatusTable.setStatus("current")
_ErrDisIfStatusEntry_Object = MibTableRow
errDisIfStatusEntry = _ErrDisIfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 6, 1)
)
errDisIfStatusEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "errDisIfStatusPortIndex"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "errDisIfStatusVlanIndex"),
)
if mibBuilder.loadTexts:
    errDisIfStatusEntry.setStatus("current")
_ErrDisIfStatusPortIndex_Type = Integer32
_ErrDisIfStatusPortIndex_Object = MibTableColumn
errDisIfStatusPortIndex = _ErrDisIfStatusPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 6, 1, 1),
    _ErrDisIfStatusPortIndex_Type()
)
errDisIfStatusPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errDisIfStatusPortIndex.setStatus("current")
_ErrDisIfStatusVlanIndex_Type = Integer32
_ErrDisIfStatusVlanIndex_Object = MibTableColumn
errDisIfStatusVlanIndex = _ErrDisIfStatusVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 6, 1, 2),
    _ErrDisIfStatusVlanIndex_Type()
)
errDisIfStatusVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errDisIfStatusVlanIndex.setStatus("current")


class _ErrDisPortState_Type(Integer32):
    """Custom type errDisPortState based on Integer32"""
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


_ErrDisPortState_Type.__name__ = "Integer32"
_ErrDisPortState_Object = MibTableColumn
errDisPortState = _ErrDisPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 6, 1, 3),
    _ErrDisPortState_Type()
)
errDisPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errDisPortState.setStatus("current")


class _ErrDisPortConnectStatus_Type(Integer32):
    """Custom type errDisPortConnectStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("err-disabled", 2),
          ("other", 1))
    )


_ErrDisPortConnectStatus_Type.__name__ = "Integer32"
_ErrDisPortConnectStatus_Object = MibTableColumn
errDisPortConnectStatus = _ErrDisPortConnectStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 6, 1, 4),
    _ErrDisPortConnectStatus_Type()
)
errDisPortConnectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errDisPortConnectStatus.setStatus("current")


class _ErrDisPortReason_Type(Integer32):
    """Custom type errDisPortReason based on Integer32"""
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
        *(("arpRateLimit", 3),
          ("bpduRateLimit", 4),
          ("dhcpRateLimit", 5),
          ("loopbackDetect", 6),
          ("portsecurity", 1),
          ("stormControl", 2))
    )


_ErrDisPortReason_Type.__name__ = "Integer32"
_ErrDisPortReason_Object = MibTableColumn
errDisPortReason = _ErrDisPortReason_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 6, 1, 5),
    _ErrDisPortReason_Type()
)
errDisPortReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errDisPortReason.setStatus("current")
_ErrDisPortRecoveryTimeLeft_Type = Integer32
_ErrDisPortRecoveryTimeLeft_Object = MibTableColumn
errDisPortRecoveryTimeLeft = _ErrDisPortRecoveryTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 6, 1, 6),
    _ErrDisPortRecoveryTimeLeft_Type()
)
errDisPortRecoveryTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errDisPortRecoveryTimeLeft.setStatus("current")
_ErrDisRecoveryTable_Object = MibTable
errDisRecoveryTable = _ErrDisRecoveryTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 7)
)
if mibBuilder.loadTexts:
    errDisRecoveryTable.setStatus("current")
_ErrDisRecoveryEntry_Object = MibTableRow
errDisRecoveryEntry = _ErrDisRecoveryEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 7, 1)
)
errDisRecoveryEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "errDisRecoveryReason"),
)
if mibBuilder.loadTexts:
    errDisRecoveryEntry.setStatus("current")


class _ErrDisRecoveryReason_Type(Integer32):
    """Custom type errDisRecoveryReason based on Integer32"""
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
        *(("arpRateLimit", 3),
          ("bpduRateLimit", 4),
          ("dhcpRateLimit", 5),
          ("loopbackDetect", 6),
          ("portsecurity", 1),
          ("stormControl", 2))
    )


_ErrDisRecoveryReason_Type.__name__ = "Integer32"
_ErrDisRecoveryReason_Object = MibTableColumn
errDisRecoveryReason = _ErrDisRecoveryReason_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 7, 1, 1),
    _ErrDisRecoveryReason_Type()
)
errDisRecoveryReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errDisRecoveryReason.setStatus("current")


class _ErrDisRecoveryStatus_Type(Integer32):
    """Custom type errDisRecoveryStatus based on Integer32"""
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


_ErrDisRecoveryStatus_Type.__name__ = "Integer32"
_ErrDisRecoveryStatus_Object = MibTableColumn
errDisRecoveryStatus = _ErrDisRecoveryStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 7, 1, 2),
    _ErrDisRecoveryStatus_Type()
)
errDisRecoveryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errDisRecoveryStatus.setStatus("current")
_ErrDisRecoveryInterval_Type = Integer32
_ErrDisRecoveryInterval_Object = MibTableColumn
errDisRecoveryInterval = _ErrDisRecoveryInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 7, 1, 3),
    _ErrDisRecoveryInterval_Type()
)
errDisRecoveryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errDisRecoveryInterval.setStatus("current")
_ErrDisTraps_ObjectIdentity = ObjectIdentity
errDisTraps = _ErrDisTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 8)
)
_ErrDisTrapsList_ObjectIdentity = ObjectIdentity
errDisTrapsList = _ErrDisTrapsList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 8, 0)
)
_JumboFrameTable_Object = MibTable
jumboFrameTable = _JumboFrameTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 14)
)
if mibBuilder.loadTexts:
    jumboFrameTable.setStatus("current")
_JumboFrameEntry_Object = MibTableRow
jumboFrameEntry = _JumboFrameEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 14, 1)
)
jumboFrameEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    jumboFrameEntry.setStatus("current")
_PortIndex_Type = Integer32
_PortIndex_Object = MibTableColumn
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 14, 1, 1),
    _PortIndex_Type()
)
portIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIndex.setStatus("current")


class _MaxReceFrameSize_Type(Integer32):
    """Custom type maxReceFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1518, 9216),
    )


_MaxReceFrameSize_Type.__name__ = "Integer32"
_MaxReceFrameSize_Object = MibTableColumn
maxReceFrameSize = _MaxReceFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 14, 1, 2),
    _MaxReceFrameSize_Type()
)
maxReceFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxReceFrameSize.setStatus("current")
_SysSNTPSettingGroup_ObjectIdentity = ObjectIdentity
sysSNTPSettingGroup = _SysSNTPSettingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 17)
)
_SntpClockSettings_ObjectIdentity = ObjectIdentity
sntpClockSettings = _SntpClockSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 17, 1)
)
_SntpTimeSeconds_Type = Integer32
_SntpTimeSeconds_Object = MibScalar
sntpTimeSeconds = _SntpTimeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 17, 1, 1),
    _SntpTimeSeconds_Type()
)
sntpTimeSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpTimeSeconds.setStatus("current")
_SntpTimeZoneSettings_ObjectIdentity = ObjectIdentity
sntpTimeZoneSettings = _SntpTimeZoneSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 17, 2)
)


class _SntpSummerTimeState_Type(Integer32):
    """Custom type sntpSummerTimeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("date", 3),
          ("disable", 1),
          ("recurring", 2))
    )


_SntpSummerTimeState_Type.__name__ = "Integer32"
_SntpSummerTimeState_Object = MibScalar
sntpSummerTimeState = _SntpSummerTimeState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 17, 2, 1),
    _SntpSummerTimeState_Type()
)
sntpSummerTimeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpSummerTimeState.setStatus("current")
_SntpGMTMinutes_Type = Integer32
_SntpGMTMinutes_Object = MibScalar
sntpGMTMinutes = _SntpGMTMinutes_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 17, 2, 2),
    _SntpGMTMinutes_Type()
)
sntpGMTMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpGMTMinutes.setStatus("current")
_SntpSummerTimeStart_Type = DisplayString
_SntpSummerTimeStart_Object = MibScalar
sntpSummerTimeStart = _SntpSummerTimeStart_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 17, 2, 3),
    _SntpSummerTimeStart_Type()
)
sntpSummerTimeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpSummerTimeStart.setStatus("current")
_SntpSummerTimeEnd_Type = DisplayString
_SntpSummerTimeEnd_Object = MibScalar
sntpSummerTimeEnd = _SntpSummerTimeEnd_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 17, 2, 4),
    _SntpSummerTimeEnd_Type()
)
sntpSummerTimeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpSummerTimeEnd.setStatus("current")
_SntpSummerTimeOffset_Type = Integer32
_SntpSummerTimeOffset_Object = MibScalar
sntpSummerTimeOffset = _SntpSummerTimeOffset_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 17, 2, 5),
    _SntpSummerTimeOffset_Type()
)
sntpSummerTimeOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpSummerTimeOffset.setStatus("current")
_SntpSNTPSettings_ObjectIdentity = ObjectIdentity
sntpSNTPSettings = _SntpSNTPSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 17, 3)
)


class _SntpGlobalState_Type(Integer32):
    """Custom type sntpGlobalState based on Integer32"""
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


_SntpGlobalState_Type.__name__ = "Integer32"
_SntpGlobalState_Object = MibScalar
sntpGlobalState = _SntpGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 17, 3, 1),
    _SntpGlobalState_Type()
)
sntpGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpGlobalState.setStatus("current")
_SntpPollInterval_Type = Integer32
_SntpPollInterval_Object = MibScalar
sntpPollInterval = _SntpPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 17, 3, 2),
    _SntpPollInterval_Type()
)
sntpPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpPollInterval.setStatus("current")
_SntpServerTable_Object = MibTable
sntpServerTable = _SntpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 17, 3, 3)
)
if mibBuilder.loadTexts:
    sntpServerTable.setStatus("current")
_SntpServerEntry_Object = MibTableRow
sntpServerEntry = _SntpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 17, 3, 3, 1)
)
sntpServerEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "sntpServerAddrType"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "sntpServerAddr"),
)
if mibBuilder.loadTexts:
    sntpServerEntry.setStatus("current")


class _SntpServerAddrType_Type(Integer32):
    """Custom type sntpServerAddrType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_SntpServerAddrType_Type.__name__ = "Integer32"
_SntpServerAddrType_Object = MibTableColumn
sntpServerAddrType = _SntpServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 17, 3, 3, 1, 1),
    _SntpServerAddrType_Type()
)
sntpServerAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpServerAddrType.setStatus("current")
_SntpServerAddr_Type = InetAddress
_SntpServerAddr_Object = MibTableColumn
sntpServerAddr = _SntpServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 17, 3, 3, 1, 2),
    _SntpServerAddr_Type()
)
sntpServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpServerAddr.setStatus("current")
_SntpServerStratum_Type = Integer32
_SntpServerStratum_Object = MibTableColumn
sntpServerStratum = _SntpServerStratum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 17, 3, 3, 1, 3),
    _SntpServerStratum_Type()
)
sntpServerStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpServerStratum.setStatus("current")
_SntpServerVersion_Type = Integer32
_SntpServerVersion_Object = MibTableColumn
sntpServerVersion = _SntpServerVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 17, 3, 3, 1, 4),
    _SntpServerVersion_Type()
)
sntpServerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpServerVersion.setStatus("current")
_SntpServerLastReceive_Type = TimeTicks
_SntpServerLastReceive_Object = MibTableColumn
sntpServerLastReceive = _SntpServerLastReceive_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 17, 3, 3, 1, 5),
    _SntpServerLastReceive_Type()
)
sntpServerLastReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpServerLastReceive.setStatus("current")
_SntpServerSynced_Type = TruthValue
_SntpServerSynced_Object = MibTableColumn
sntpServerSynced = _SntpServerSynced_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 17, 3, 3, 1, 6),
    _SntpServerSynced_Type()
)
sntpServerSynced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpServerSynced.setStatus("current")
_SntpServerRowStatus_Type = RowStatus
_SntpServerRowStatus_Object = MibTableColumn
sntpServerRowStatus = _SntpServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 17, 3, 3, 1, 7),
    _SntpServerRowStatus_Type()
)
sntpServerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpServerRowStatus.setStatus("current")
_SysTimeRangeGroup_ObjectIdentity = ObjectIdentity
sysTimeRangeGroup = _SysTimeRangeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 38)
)
_TimeRangeTable_Object = MibTable
timeRangeTable = _TimeRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 38, 1)
)
if mibBuilder.loadTexts:
    timeRangeTable.setStatus("current")
_TimeRangeEntry_Object = MibTableRow
timeRangeEntry = _TimeRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 38, 1, 1)
)
timeRangeEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "timeRangeName"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "timeRangeIndex"),
)
if mibBuilder.loadTexts:
    timeRangeEntry.setStatus("current")


class _TimeRangeName_Type(DisplayString):
    """Custom type timeRangeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_TimeRangeName_Type.__name__ = "DisplayString"
_TimeRangeName_Object = MibTableColumn
timeRangeName = _TimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 38, 1, 1, 1),
    _TimeRangeName_Type()
)
timeRangeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeRangeName.setStatus("current")


class _TimeRangeIndex_Type(Integer32):
    """Custom type timeRangeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_TimeRangeIndex_Type.__name__ = "Integer32"
_TimeRangeIndex_Object = MibTableColumn
timeRangeIndex = _TimeRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 38, 1, 1, 2),
    _TimeRangeIndex_Type()
)
timeRangeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeRangeIndex.setStatus("current")


class _TimeRangeStartHour_Type(Integer32):
    """Custom type timeRangeStartHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TimeRangeStartHour_Type.__name__ = "Integer32"
_TimeRangeStartHour_Object = MibTableColumn
timeRangeStartHour = _TimeRangeStartHour_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 38, 1, 1, 3),
    _TimeRangeStartHour_Type()
)
timeRangeStartHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeRangeStartHour.setStatus("current")


class _TimeRangeStartMinute_Type(Integer32):
    """Custom type timeRangeStartMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TimeRangeStartMinute_Type.__name__ = "Integer32"
_TimeRangeStartMinute_Object = MibTableColumn
timeRangeStartMinute = _TimeRangeStartMinute_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 38, 1, 1, 4),
    _TimeRangeStartMinute_Type()
)
timeRangeStartMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeRangeStartMinute.setStatus("current")


class _TimeRangeEndHour_Type(Integer32):
    """Custom type timeRangeEndHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TimeRangeEndHour_Type.__name__ = "Integer32"
_TimeRangeEndHour_Object = MibTableColumn
timeRangeEndHour = _TimeRangeEndHour_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 38, 1, 1, 5),
    _TimeRangeEndHour_Type()
)
timeRangeEndHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeRangeEndHour.setStatus("current")


class _TimeRangeEndMinute_Type(Integer32):
    """Custom type timeRangeEndMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TimeRangeEndMinute_Type.__name__ = "Integer32"
_TimeRangeEndMinute_Object = MibTableColumn
timeRangeEndMinute = _TimeRangeEndMinute_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 38, 1, 1, 6),
    _TimeRangeEndMinute_Type()
)
timeRangeEndMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeRangeEndMinute.setStatus("current")


class _TimeRangeWeekday_Type(Bits):
    """Custom type timeRangeWeekday based on Bits"""
    namedValues = NamedValues(
        *(("friday", 1),
          ("monday", 5),
          ("saturday", 0),
          ("sunday", 6),
          ("thursday", 2),
          ("tuesday", 4),
          ("wednesday", 3))
    )

_TimeRangeWeekday_Type.__name__ = "Bits"
_TimeRangeWeekday_Object = MibTableColumn
timeRangeWeekday = _TimeRangeWeekday_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 38, 1, 1, 7),
    _TimeRangeWeekday_Type()
)
timeRangeWeekday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeRangeWeekday.setStatus("current")
_TimeRangeRowStatus_Type = RowStatus
_TimeRangeRowStatus_Object = MibTableColumn
timeRangeRowStatus = _TimeRangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 38, 1, 1, 8),
    _TimeRangeRowStatus_Type()
)
timeRangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timeRangeRowStatus.setStatus("current")
_DlinkManagement_ObjectIdentity = ObjectIdentity
dlinkManagement = _DlinkManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3)
)
_MgtUserAccountGroup_ObjectIdentity = ObjectIdentity
mgtUserAccountGroup = _MgtUserAccountGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 1)
)
_UserAccountsManagementSettings_ObjectIdentity = ObjectIdentity
userAccountsManagementSettings = _UserAccountsManagementSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 1, 1)
)
_UserAccountsTable_Object = MibTable
userAccountsTable = _UserAccountsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    userAccountsTable.setStatus("current")
_UserAccountsEntry_Object = MibTableRow
userAccountsEntry = _UserAccountsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 1, 1, 1, 1)
)
userAccountsEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "userName"),
)
if mibBuilder.loadTexts:
    userAccountsEntry.setStatus("current")


class _UserName_Type(SnmpAdminString):
    """Custom type userName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_UserName_Type.__name__ = "SnmpAdminString"
_UserName_Object = MibTableColumn
userName = _UserName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 1, 1, 1, 1, 1),
    _UserName_Type()
)
userName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userName.setStatus("current")


class _UserPrivilege_Type(Unsigned32):
    """Custom type userPrivilege based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_UserPrivilege_Type.__name__ = "Unsigned32"
_UserPrivilege_Object = MibTableColumn
userPrivilege = _UserPrivilege_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 1, 1, 1, 1, 2),
    _UserPrivilege_Type()
)
userPrivilege.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userPrivilege.setStatus("current")


class _UserEncryptControl_Type(Integer32):
    """Custom type userEncryptControl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enabled", 1))
    )


_UserEncryptControl_Type.__name__ = "Integer32"
_UserEncryptControl_Object = MibTableColumn
userEncryptControl = _UserEncryptControl_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 1, 1, 1, 1, 3),
    _UserEncryptControl_Type()
)
userEncryptControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userEncryptControl.setStatus("current")


class _UserPassword_Type(DisplayString):
    """Custom type userPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_UserPassword_Type.__name__ = "DisplayString"
_UserPassword_Object = MibTableColumn
userPassword = _UserPassword_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 1, 1, 1, 1, 4),
    _UserPassword_Type()
)
userPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userPassword.setStatus("current")
_UserRowStatus_Type = RowStatus
_UserRowStatus_Object = MibTableColumn
userRowStatus = _UserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 1, 1, 1, 1, 5),
    _UserRowStatus_Type()
)
userRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userRowStatus.setStatus("current")
_UserAccountsSessionTable_ObjectIdentity = ObjectIdentity
userAccountsSessionTable = _UserAccountsSessionTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 1, 2)
)
_UserSessionTableEntry_Object = MibTable
userSessionTableEntry = _UserSessionTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    userSessionTableEntry.setStatus("current")
_UserSessionEntry_Object = MibTableRow
userSessionEntry = _UserSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 1, 2, 1, 1)
)
userSessionEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "sessionID"),
)
if mibBuilder.loadTexts:
    userSessionEntry.setStatus("current")
_SessionID_Type = Unsigned32
_SessionID_Object = MibTableColumn
sessionID = _SessionID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 1, 2, 1, 1, 1),
    _SessionID_Type()
)
sessionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionID.setStatus("current")
_LiveTime_Type = TimeTicks
_LiveTime_Object = MibTableColumn
liveTime = _LiveTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 1, 2, 1, 1, 2),
    _LiveTime_Type()
)
liveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    liveTime.setStatus("current")


class _LoginType_Type(Integer32):
    """Custom type loginType based on Integer32"""
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
        *(("console", 4),
          ("http", 1),
          ("ssh", 3),
          ("telnet", 2))
    )


_LoginType_Type.__name__ = "Integer32"
_LoginType_Object = MibTableColumn
loginType = _LoginType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 1, 2, 1, 1, 3),
    _LoginType_Type()
)
loginType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loginType.setStatus("current")
_LoginIP_Type = InetAddress
_LoginIP_Object = MibTableColumn
loginIP = _LoginIP_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 1, 2, 1, 1, 4),
    _LoginIP_Type()
)
loginIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loginIP.setStatus("current")
_LoginUserLevel_Type = Integer32
_LoginUserLevel_Object = MibTableColumn
loginUserLevel = _LoginUserLevel_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 1, 2, 1, 1, 5),
    _LoginUserLevel_Type()
)
loginUserLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loginUserLevel.setStatus("current")
_LoginUserName_Type = DisplayString
_LoginUserName_Object = MibTableColumn
loginUserName = _LoginUserName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 1, 2, 1, 1, 6),
    _LoginUserName_Type()
)
loginUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loginUserName.setStatus("current")
_MgtPasswordEncryptionGroup_ObjectIdentity = ObjectIdentity
mgtPasswordEncryptionGroup = _MgtPasswordEncryptionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 2)
)


class _PasswordEncryptionStatus_Type(Integer32):
    """Custom type passwordEncryptionStatus based on Integer32"""
    defaultValue = 2

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


_PasswordEncryptionStatus_Type.__name__ = "Integer32"
_PasswordEncryptionStatus_Object = MibScalar
passwordEncryptionStatus = _PasswordEncryptionStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 2, 1),
    _PasswordEncryptionStatus_Type()
)
passwordEncryptionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    passwordEncryptionStatus.setStatus("current")
_MgtSnmpGroup_ObjectIdentity = ObjectIdentity
mgtSnmpGroup = _MgtSnmpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3)
)
_SnmpGlobalSettings_ObjectIdentity = ObjectIdentity
snmpGlobalSettings = _SnmpGlobalSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 1)
)


class _SnmpGlobalState_Type(Integer32):
    """Custom type snmpGlobalState based on Integer32"""
    defaultValue = 1

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


_SnmpGlobalState_Type.__name__ = "Integer32"
_SnmpGlobalState_Object = MibScalar
snmpGlobalState = _SnmpGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 1, 1),
    _SnmpGlobalState_Type()
)
snmpGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpGlobalState.setStatus("current")


class _SnmpResBroadReq_Type(Integer32):
    """Custom type snmpResBroadReq based on Integer32"""
    defaultValue = 2

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


_SnmpResBroadReq_Type.__name__ = "Integer32"
_SnmpResBroadReq_Object = MibScalar
snmpResBroadReq = _SnmpResBroadReq_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 1, 2),
    _SnmpResBroadReq_Type()
)
snmpResBroadReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpResBroadReq.setStatus("current")


class _SnmpUDPPort_Type(Unsigned32):
    """Custom type snmpUDPPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnmpUDPPort_Type.__name__ = "Unsigned32"
_SnmpUDPPort_Object = MibScalar
snmpUDPPort = _SnmpUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 1, 3),
    _SnmpUDPPort_Type()
)
snmpUDPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpUDPPort.setStatus("current")


class _SnmpTrapSourceInterface_Type(SnmpAdminString):
    """Custom type snmpTrapSourceInterface based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnmpTrapSourceInterface_Type.__name__ = "SnmpAdminString"
_SnmpTrapSourceInterface_Object = MibScalar
snmpTrapSourceInterface = _SnmpTrapSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 1, 4),
    _SnmpTrapSourceInterface_Type()
)
snmpTrapSourceInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapSourceInterface.setStatus("current")


class _SnmpTrapGlobalState_Type(Integer32):
    """Custom type snmpTrapGlobalState based on Integer32"""
    defaultValue = 1

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


_SnmpTrapGlobalState_Type.__name__ = "Integer32"
_SnmpTrapGlobalState_Object = MibScalar
snmpTrapGlobalState = _SnmpTrapGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 1, 5),
    _SnmpTrapGlobalState_Type()
)
snmpTrapGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapGlobalState.setStatus("current")


class _SnmpTrapSNMPAuthTrap_Type(Integer32):
    """Custom type snmpTrapSNMPAuthTrap based on Integer32"""
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


_SnmpTrapSNMPAuthTrap_Type.__name__ = "Integer32"
_SnmpTrapSNMPAuthTrap_Object = MibScalar
snmpTrapSNMPAuthTrap = _SnmpTrapSNMPAuthTrap_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 1, 6),
    _SnmpTrapSNMPAuthTrap_Type()
)
snmpTrapSNMPAuthTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapSNMPAuthTrap.setStatus("current")


class _SnmpTrapPortLinkUp_Type(Integer32):
    """Custom type snmpTrapPortLinkUp based on Integer32"""
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


_SnmpTrapPortLinkUp_Type.__name__ = "Integer32"
_SnmpTrapPortLinkUp_Object = MibScalar
snmpTrapPortLinkUp = _SnmpTrapPortLinkUp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 1, 7),
    _SnmpTrapPortLinkUp_Type()
)
snmpTrapPortLinkUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapPortLinkUp.setStatus("current")


class _SnmpTrapPortLinkDown_Type(Integer32):
    """Custom type snmpTrapPortLinkDown based on Integer32"""
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


_SnmpTrapPortLinkDown_Type.__name__ = "Integer32"
_SnmpTrapPortLinkDown_Object = MibScalar
snmpTrapPortLinkDown = _SnmpTrapPortLinkDown_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 1, 8),
    _SnmpTrapPortLinkDown_Type()
)
snmpTrapPortLinkDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapPortLinkDown.setStatus("current")


class _SnmpTrapColdstart_Type(Integer32):
    """Custom type snmpTrapColdstart based on Integer32"""
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


_SnmpTrapColdstart_Type.__name__ = "Integer32"
_SnmpTrapColdstart_Object = MibScalar
snmpTrapColdstart = _SnmpTrapColdstart_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 1, 9),
    _SnmpTrapColdstart_Type()
)
snmpTrapColdstart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapColdstart.setStatus("current")


class _SnmpTrapWarmstart_Type(Integer32):
    """Custom type snmpTrapWarmstart based on Integer32"""
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


_SnmpTrapWarmstart_Type.__name__ = "Integer32"
_SnmpTrapWarmstart_Object = MibScalar
snmpTrapWarmstart = _SnmpTrapWarmstart_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 1, 10),
    _SnmpTrapWarmstart_Type()
)
snmpTrapWarmstart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapWarmstart.setStatus("current")
_SnmpView_ObjectIdentity = ObjectIdentity
snmpView = _SnmpView_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 3)
)
_SnmpViewTable_Object = MibTable
snmpViewTable = _SnmpViewTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 3, 1)
)
if mibBuilder.loadTexts:
    snmpViewTable.setStatus("current")
_SnmpViewEntry_Object = MibTableRow
snmpViewEntry = _SnmpViewEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 3, 1, 1)
)
snmpViewEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "snmpViewName"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "snmpViewSubtree"),
)
if mibBuilder.loadTexts:
    snmpViewEntry.setStatus("current")


class _SnmpViewName_Type(SnmpAdminString):
    """Custom type snmpViewName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnmpViewName_Type.__name__ = "SnmpAdminString"
_SnmpViewName_Object = MibTableColumn
snmpViewName = _SnmpViewName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 3, 1, 1, 1),
    _SnmpViewName_Type()
)
snmpViewName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpViewName.setStatus("current")
_SnmpViewSubtree_Type = ObjectIdentifier
_SnmpViewSubtree_Object = MibTableColumn
snmpViewSubtree = _SnmpViewSubtree_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 3, 1, 1, 2),
    _SnmpViewSubtree_Type()
)
snmpViewSubtree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpViewSubtree.setStatus("current")


class _SnmpViewType_Type(Integer32):
    """Custom type snmpViewType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("excluded", 2),
          ("included", 1))
    )


_SnmpViewType_Type.__name__ = "Integer32"
_SnmpViewType_Object = MibTableColumn
snmpViewType = _SnmpViewType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 3, 1, 1, 3),
    _SnmpViewType_Type()
)
snmpViewType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpViewType.setStatus("current")
_SnmpViewStatus_Type = RowStatus
_SnmpViewStatus_Object = MibTableColumn
snmpViewStatus = _SnmpViewStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 3, 1, 1, 4),
    _SnmpViewStatus_Type()
)
snmpViewStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpViewStatus.setStatus("current")
_SnmpCommunity_ObjectIdentity = ObjectIdentity
snmpCommunity = _SnmpCommunity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 4)
)
_SnmpCommunityTable_Object = MibTable
snmpCommunityTable = _SnmpCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 4, 1)
)
if mibBuilder.loadTexts:
    snmpCommunityTable.setStatus("current")
_SnmpCommunityEntry_Object = MibTableRow
snmpCommunityEntry = _SnmpCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 4, 1, 1)
)
snmpCommunityEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "snmpCommName"),
)
if mibBuilder.loadTexts:
    snmpCommunityEntry.setStatus("current")
_SnmpCommName_Type = SnmpAdminString
_SnmpCommName_Object = MibTableColumn
snmpCommName = _SnmpCommName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 4, 1, 1, 1),
    _SnmpCommName_Type()
)
snmpCommName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpCommName.setStatus("current")


class _SnmpCommKeyType_Type(Integer32):
    """Custom type snmpCommKeyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("encrypted", 2),
          ("plainText", 1))
    )


_SnmpCommKeyType_Type.__name__ = "Integer32"
_SnmpCommKeyType_Object = MibTableColumn
snmpCommKeyType = _SnmpCommKeyType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 4, 1, 1, 2),
    _SnmpCommKeyType_Type()
)
snmpCommKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpCommKeyType.setStatus("current")


class _SnmpCommViewName_Type(SnmpAdminString):
    """Custom type snmpCommViewName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnmpCommViewName_Type.__name__ = "SnmpAdminString"
_SnmpCommViewName_Object = MibTableColumn
snmpCommViewName = _SnmpCommViewName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 4, 1, 1, 3),
    _SnmpCommViewName_Type()
)
snmpCommViewName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpCommViewName.setStatus("current")


class _SnmpCommAccessRight_Type(Integer32):
    """Custom type snmpCommAccessRight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 1),
          ("readWrite", 2))
    )


_SnmpCommAccessRight_Type.__name__ = "Integer32"
_SnmpCommAccessRight_Object = MibTableColumn
snmpCommAccessRight = _SnmpCommAccessRight_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 4, 1, 1, 4),
    _SnmpCommAccessRight_Type()
)
snmpCommAccessRight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpCommAccessRight.setStatus("current")
_SnmpCommIPAccListName_Type = SnmpAdminString
_SnmpCommIPAccListName_Object = MibTableColumn
snmpCommIPAccListName = _SnmpCommIPAccListName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 4, 1, 1, 5),
    _SnmpCommIPAccListName_Type()
)
snmpCommIPAccListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpCommIPAccListName.setStatus("current")
_SnmpCommStatus_Type = RowStatus
_SnmpCommStatus_Object = MibTableColumn
snmpCommStatus = _SnmpCommStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 4, 1, 1, 6),
    _SnmpCommStatus_Type()
)
snmpCommStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpCommStatus.setStatus("current")
_SnmpGroup_ObjectIdentity = ObjectIdentity
snmpGroup = _SnmpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 5)
)
_SnmpGroupTable_Object = MibTable
snmpGroupTable = _SnmpGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 5, 1)
)
if mibBuilder.loadTexts:
    snmpGroupTable.setStatus("current")
_SnmpGroupEntry_Object = MibTableRow
snmpGroupEntry = _SnmpGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 5, 1, 1)
)
snmpGroupEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "snmpGroupName"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "snmpGroupSecurityModel"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "snmpGroupSecurityLevel"),
)
if mibBuilder.loadTexts:
    snmpGroupEntry.setStatus("current")


class _SnmpGroupName_Type(SnmpAdminString):
    """Custom type snmpGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnmpGroupName_Type.__name__ = "SnmpAdminString"
_SnmpGroupName_Object = MibTableColumn
snmpGroupName = _SnmpGroupName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 5, 1, 1, 1),
    _SnmpGroupName_Type()
)
snmpGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpGroupName.setStatus("current")


class _SnmpGroupSecurityModel_Type(Integer32):
    """Custom type snmpGroupSecurityModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2c", 2),
          ("v3", 3))
    )


_SnmpGroupSecurityModel_Type.__name__ = "Integer32"
_SnmpGroupSecurityModel_Object = MibTableColumn
snmpGroupSecurityModel = _SnmpGroupSecurityModel_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 5, 1, 1, 2),
    _SnmpGroupSecurityModel_Type()
)
snmpGroupSecurityModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpGroupSecurityModel.setStatus("current")


class _SnmpGroupSecurityLevel_Type(Integer32):
    """Custom type snmpGroupSecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("authNoPriv", 2),
          ("authPriv", 3),
          ("noAuthNoPriv", 1))
    )


_SnmpGroupSecurityLevel_Type.__name__ = "Integer32"
_SnmpGroupSecurityLevel_Object = MibTableColumn
snmpGroupSecurityLevel = _SnmpGroupSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 5, 1, 1, 3),
    _SnmpGroupSecurityLevel_Type()
)
snmpGroupSecurityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpGroupSecurityLevel.setStatus("current")


class _SnmpGroupReadViewName_Type(SnmpAdminString):
    """Custom type snmpGroupReadViewName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnmpGroupReadViewName_Type.__name__ = "SnmpAdminString"
_SnmpGroupReadViewName_Object = MibTableColumn
snmpGroupReadViewName = _SnmpGroupReadViewName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 5, 1, 1, 4),
    _SnmpGroupReadViewName_Type()
)
snmpGroupReadViewName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpGroupReadViewName.setStatus("current")


class _SnmpGroupWriteViewName_Type(SnmpAdminString):
    """Custom type snmpGroupWriteViewName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnmpGroupWriteViewName_Type.__name__ = "SnmpAdminString"
_SnmpGroupWriteViewName_Object = MibTableColumn
snmpGroupWriteViewName = _SnmpGroupWriteViewName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 5, 1, 1, 5),
    _SnmpGroupWriteViewName_Type()
)
snmpGroupWriteViewName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpGroupWriteViewName.setStatus("current")


class _SnmpGroupNotifyViewName_Type(SnmpAdminString):
    """Custom type snmpGroupNotifyViewName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnmpGroupNotifyViewName_Type.__name__ = "SnmpAdminString"
_SnmpGroupNotifyViewName_Object = MibTableColumn
snmpGroupNotifyViewName = _SnmpGroupNotifyViewName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 5, 1, 1, 6),
    _SnmpGroupNotifyViewName_Type()
)
snmpGroupNotifyViewName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpGroupNotifyViewName.setStatus("current")


class _SnmpGroupIpListName_Type(SnmpAdminString):
    """Custom type snmpGroupIpListName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnmpGroupIpListName_Type.__name__ = "SnmpAdminString"
_SnmpGroupIpListName_Object = MibTableColumn
snmpGroupIpListName = _SnmpGroupIpListName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 5, 1, 1, 7),
    _SnmpGroupIpListName_Type()
)
snmpGroupIpListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpGroupIpListName.setStatus("current")
_SnmpGroupStatus_Type = RowStatus
_SnmpGroupStatus_Object = MibTableColumn
snmpGroupStatus = _SnmpGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 5, 1, 1, 8),
    _SnmpGroupStatus_Type()
)
snmpGroupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpGroupStatus.setStatus("current")
_SnmpEngineID_Type = SnmpEngineID
_SnmpEngineID_Object = MibScalar
snmpEngineID = _SnmpEngineID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 6),
    _SnmpEngineID_Type()
)
snmpEngineID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpEngineID.setStatus("current")
_SnmpUser_ObjectIdentity = ObjectIdentity
snmpUser = _SnmpUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 7)
)
_SnmpUserTable_Object = MibTable
snmpUserTable = _SnmpUserTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 7, 1)
)
if mibBuilder.loadTexts:
    snmpUserTable.setStatus("current")
_SnmpUserEntry_Object = MibTableRow
snmpUserEntry = _SnmpUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 7, 1, 1)
)
snmpUserEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "snmpUserName"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "snmpUserVersion"),
)
if mibBuilder.loadTexts:
    snmpUserEntry.setStatus("current")


class _SnmpUserName_Type(SnmpAdminString):
    """Custom type snmpUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnmpUserName_Type.__name__ = "SnmpAdminString"
_SnmpUserName_Object = MibTableColumn
snmpUserName = _SnmpUserName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 7, 1, 1, 1),
    _SnmpUserName_Type()
)
snmpUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpUserName.setStatus("current")


class _SnmpUserVersion_Type(Integer32):
    """Custom type snmpUserVersion based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2c", 2),
          ("v3", 3))
    )


_SnmpUserVersion_Type.__name__ = "Integer32"
_SnmpUserVersion_Object = MibTableColumn
snmpUserVersion = _SnmpUserVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 7, 1, 1, 2),
    _SnmpUserVersion_Type()
)
snmpUserVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpUserVersion.setStatus("current")


class _SnmpUserGroupName_Type(SnmpAdminString):
    """Custom type snmpUserGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnmpUserGroupName_Type.__name__ = "SnmpAdminString"
_SnmpUserGroupName_Object = MibTableColumn
snmpUserGroupName = _SnmpUserGroupName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 7, 1, 1, 3),
    _SnmpUserGroupName_Type()
)
snmpUserGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpUserGroupName.setStatus("current")


class _SnmpUserV3Encrypt_Type(Integer32):
    """Custom type snmpUserV3Encrypt based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("key", 2),
          ("none", 0),
          ("password", 1))
    )


_SnmpUserV3Encrypt_Type.__name__ = "Integer32"
_SnmpUserV3Encrypt_Object = MibTableColumn
snmpUserV3Encrypt = _SnmpUserV3Encrypt_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 7, 1, 1, 4),
    _SnmpUserV3Encrypt_Type()
)
snmpUserV3Encrypt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpUserV3Encrypt.setStatus("current")


class _SnmpUserAuthProtocol_Type(Integer32):
    """Custom type snmpUserAuthProtocol based on Integer32"""
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


_SnmpUserAuthProtocol_Type.__name__ = "Integer32"
_SnmpUserAuthProtocol_Object = MibTableColumn
snmpUserAuthProtocol = _SnmpUserAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 7, 1, 1, 5),
    _SnmpUserAuthProtocol_Type()
)
snmpUserAuthProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpUserAuthProtocol.setStatus("current")


class _SnmpUserAuthProtocolPassword_Type(SnmpAdminString):
    """Custom type snmpUserAuthProtocolPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnmpUserAuthProtocolPassword_Type.__name__ = "SnmpAdminString"
_SnmpUserAuthProtocolPassword_Object = MibTableColumn
snmpUserAuthProtocolPassword = _SnmpUserAuthProtocolPassword_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 7, 1, 1, 6),
    _SnmpUserAuthProtocolPassword_Type()
)
snmpUserAuthProtocolPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpUserAuthProtocolPassword.setStatus("current")


class _SnmpUserPrivProtocol_Type(Integer32):
    """Custom type snmpUserPrivProtocol based on Integer32"""
    defaultValue = 1

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


_SnmpUserPrivProtocol_Type.__name__ = "Integer32"
_SnmpUserPrivProtocol_Object = MibTableColumn
snmpUserPrivProtocol = _SnmpUserPrivProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 7, 1, 1, 7),
    _SnmpUserPrivProtocol_Type()
)
snmpUserPrivProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpUserPrivProtocol.setStatus("current")


class _SnmpUserPrivProtocolPassword_Type(SnmpAdminString):
    """Custom type snmpUserPrivProtocolPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnmpUserPrivProtocolPassword_Type.__name__ = "SnmpAdminString"
_SnmpUserPrivProtocolPassword_Object = MibTableColumn
snmpUserPrivProtocolPassword = _SnmpUserPrivProtocolPassword_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 7, 1, 1, 8),
    _SnmpUserPrivProtocolPassword_Type()
)
snmpUserPrivProtocolPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpUserPrivProtocolPassword.setStatus("current")


class _SnmpUserAuthProtoByKey_Type(Integer32):
    """Custom type snmpUserAuthProtoByKey based on Integer32"""
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


_SnmpUserAuthProtoByKey_Type.__name__ = "Integer32"
_SnmpUserAuthProtoByKey_Object = MibTableColumn
snmpUserAuthProtoByKey = _SnmpUserAuthProtoByKey_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 7, 1, 1, 9),
    _SnmpUserAuthProtoByKey_Type()
)
snmpUserAuthProtoByKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpUserAuthProtoByKey.setStatus("current")


class _SnmpUserAuthProtoKey_Type(SnmpAdminString):
    """Custom type snmpUserAuthProtoKey based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnmpUserAuthProtoKey_Type.__name__ = "SnmpAdminString"
_SnmpUserAuthProtoKey_Object = MibTableColumn
snmpUserAuthProtoKey = _SnmpUserAuthProtoKey_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 7, 1, 1, 10),
    _SnmpUserAuthProtoKey_Type()
)
snmpUserAuthProtoKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpUserAuthProtoKey.setStatus("current")


class _SnmpUserPrivProtoByKey_Type(Integer32):
    """Custom type snmpUserPrivProtoByKey based on Integer32"""
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


_SnmpUserPrivProtoByKey_Type.__name__ = "Integer32"
_SnmpUserPrivProtoByKey_Object = MibTableColumn
snmpUserPrivProtoByKey = _SnmpUserPrivProtoByKey_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 7, 1, 1, 11),
    _SnmpUserPrivProtoByKey_Type()
)
snmpUserPrivProtoByKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpUserPrivProtoByKey.setStatus("current")


class _SnmpUserPrivProtoKey_Type(SnmpAdminString):
    """Custom type snmpUserPrivProtoKey based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnmpUserPrivProtoKey_Type.__name__ = "SnmpAdminString"
_SnmpUserPrivProtoKey_Object = MibTableColumn
snmpUserPrivProtoKey = _SnmpUserPrivProtoKey_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 7, 1, 1, 12),
    _SnmpUserPrivProtoKey_Type()
)
snmpUserPrivProtoKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpUserPrivProtoKey.setStatus("current")


class _SnmpUserIpListName_Type(SnmpAdminString):
    """Custom type snmpUserIpListName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnmpUserIpListName_Type.__name__ = "SnmpAdminString"
_SnmpUserIpListName_Object = MibTableColumn
snmpUserIpListName = _SnmpUserIpListName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 7, 1, 1, 13),
    _SnmpUserIpListName_Type()
)
snmpUserIpListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpUserIpListName.setStatus("current")
_SnmpUserStatus_Type = RowStatus
_SnmpUserStatus_Object = MibTableColumn
snmpUserStatus = _SnmpUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 7, 1, 1, 14),
    _SnmpUserStatus_Type()
)
snmpUserStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpUserStatus.setStatus("current")
_SnmpHost_ObjectIdentity = ObjectIdentity
snmpHost = _SnmpHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 8)
)
_SnmpHostTable_Object = MibTable
snmpHostTable = _SnmpHostTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 8, 1)
)
if mibBuilder.loadTexts:
    snmpHostTable.setStatus("current")
_SnmpHostEntry_Object = MibTableRow
snmpHostEntry = _SnmpHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 8, 1, 1)
)
snmpHostEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "snmpHostAddress"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "snmpHostIPType"),
)
if mibBuilder.loadTexts:
    snmpHostEntry.setStatus("current")
_SnmpHostAddress_Type = InetAddress
_SnmpHostAddress_Object = MibTableColumn
snmpHostAddress = _SnmpHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 8, 1, 1, 1),
    _SnmpHostAddress_Type()
)
snmpHostAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpHostAddress.setStatus("current")


class _SnmpHostIPType_Type(Integer32):
    """Custom type snmpHostIPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("iPv4", 1),
          ("iPv6", 2))
    )


_SnmpHostIPType_Type.__name__ = "Integer32"
_SnmpHostIPType_Object = MibTableColumn
snmpHostIPType = _SnmpHostIPType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 8, 1, 1, 2),
    _SnmpHostIPType_Type()
)
snmpHostIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpHostIPType.setStatus("current")


class _SnmpHostVersion_Type(Integer32):
    """Custom type snmpHostVersion based on Integer32"""
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
        *(("authNoPriv", 4),
          ("authPriv", 5),
          ("noAuthNoPriv", 3),
          ("v1", 1),
          ("v2c", 2))
    )


_SnmpHostVersion_Type.__name__ = "Integer32"
_SnmpHostVersion_Object = MibTableColumn
snmpHostVersion = _SnmpHostVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 8, 1, 1, 3),
    _SnmpHostVersion_Type()
)
snmpHostVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpHostVersion.setStatus("current")


class _SnmpHostUDPPort_Type(Integer32):
    """Custom type snmpHostUDPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnmpHostUDPPort_Type.__name__ = "Integer32"
_SnmpHostUDPPort_Object = MibTableColumn
snmpHostUDPPort = _SnmpHostUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 8, 1, 1, 4),
    _SnmpHostUDPPort_Type()
)
snmpHostUDPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpHostUDPPort.setStatus("current")


class _SnmpHostCommunityName_Type(SnmpAdminString):
    """Custom type snmpHostCommunityName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnmpHostCommunityName_Type.__name__ = "SnmpAdminString"
_SnmpHostCommunityName_Object = MibTableColumn
snmpHostCommunityName = _SnmpHostCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 8, 1, 1, 5),
    _SnmpHostCommunityName_Type()
)
snmpHostCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpHostCommunityName.setStatus("current")
_SnmpHostStatus_Type = RowStatus
_SnmpHostStatus_Object = MibTableColumn
snmpHostStatus = _SnmpHostStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 3, 8, 1, 1, 6),
    _SnmpHostStatus_Type()
)
snmpHostStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpHostStatus.setStatus("current")
_MgtRMONGroup_ObjectIdentity = ObjectIdentity
mgtRMONGroup = _MgtRMONGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4)
)


class _RmonRisingAlarmTrapState_Type(Integer32):
    """Custom type rmonRisingAlarmTrapState based on Integer32"""
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


_RmonRisingAlarmTrapState_Type.__name__ = "Integer32"
_RmonRisingAlarmTrapState_Object = MibScalar
rmonRisingAlarmTrapState = _RmonRisingAlarmTrapState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 1),
    _RmonRisingAlarmTrapState_Type()
)
rmonRisingAlarmTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonRisingAlarmTrapState.setStatus("current")


class _RmonFallingAlarmTrapState_Type(Integer32):
    """Custom type rmonFallingAlarmTrapState based on Integer32"""
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


_RmonFallingAlarmTrapState_Type.__name__ = "Integer32"
_RmonFallingAlarmTrapState_Object = MibScalar
rmonFallingAlarmTrapState = _RmonFallingAlarmTrapState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 2),
    _RmonFallingAlarmTrapState_Type()
)
rmonFallingAlarmTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonFallingAlarmTrapState.setStatus("current")
_RmonStatistics_ObjectIdentity = ObjectIdentity
rmonStatistics = _RmonStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 3)
)
_RmonStatsTable_Object = MibTable
rmonStatsTable = _RmonStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 3, 1)
)
if mibBuilder.loadTexts:
    rmonStatsTable.setStatus("current")
_RmonStatsEntry_Object = MibTableRow
rmonStatsEntry = _RmonStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 3, 1, 1)
)
rmonStatsEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "rmonStatsIndex"),
)
if mibBuilder.loadTexts:
    rmonStatsEntry.setStatus("current")


class _RmonStatsIndex_Type(Integer32):
    """Custom type rmonStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RmonStatsIndex_Type.__name__ = "Integer32"
_RmonStatsIndex_Object = MibTableColumn
rmonStatsIndex = _RmonStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 3, 1, 1, 1),
    _RmonStatsIndex_Type()
)
rmonStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonStatsIndex.setStatus("current")
_RmonStatsDataSource_Type = ObjectIdentifier
_RmonStatsDataSource_Object = MibTableColumn
rmonStatsDataSource = _RmonStatsDataSource_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 3, 1, 1, 2),
    _RmonStatsDataSource_Type()
)
rmonStatsDataSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonStatsDataSource.setStatus("current")
_RmonStatsOwner_Type = OwnerString
_RmonStatsOwner_Object = MibTableColumn
rmonStatsOwner = _RmonStatsOwner_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 3, 1, 1, 3),
    _RmonStatsOwner_Type()
)
rmonStatsOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonStatsOwner.setStatus("current")
_RmonStatsOctets_Type = Counter32
_RmonStatsOctets_Object = MibTableColumn
rmonStatsOctets = _RmonStatsOctets_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 3, 1, 1, 4),
    _RmonStatsOctets_Type()
)
rmonStatsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonStatsOctets.setStatus("current")
if mibBuilder.loadTexts:
    rmonStatsOctets.setUnits("Octets")
_RmonStatsPkts_Type = Counter32
_RmonStatsPkts_Object = MibTableColumn
rmonStatsPkts = _RmonStatsPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 3, 1, 1, 5),
    _RmonStatsPkts_Type()
)
rmonStatsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonStatsPkts.setStatus("current")
if mibBuilder.loadTexts:
    rmonStatsPkts.setUnits("Packets")
_RmonStatsBroadcastPkts_Type = Counter32
_RmonStatsBroadcastPkts_Object = MibTableColumn
rmonStatsBroadcastPkts = _RmonStatsBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 3, 1, 1, 6),
    _RmonStatsBroadcastPkts_Type()
)
rmonStatsBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonStatsBroadcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    rmonStatsBroadcastPkts.setUnits("Packets")
_RmonStatsMulticastPkts_Type = Counter32
_RmonStatsMulticastPkts_Object = MibTableColumn
rmonStatsMulticastPkts = _RmonStatsMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 3, 1, 1, 7),
    _RmonStatsMulticastPkts_Type()
)
rmonStatsMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonStatsMulticastPkts.setStatus("current")
if mibBuilder.loadTexts:
    rmonStatsMulticastPkts.setUnits("Packets")
_RmonStatsUndersizePkts_Type = Counter32
_RmonStatsUndersizePkts_Object = MibTableColumn
rmonStatsUndersizePkts = _RmonStatsUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 3, 1, 1, 8),
    _RmonStatsUndersizePkts_Type()
)
rmonStatsUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonStatsUndersizePkts.setStatus("current")
if mibBuilder.loadTexts:
    rmonStatsUndersizePkts.setUnits("Packets")
_RmonStatsOversizePkts_Type = Counter32
_RmonStatsOversizePkts_Object = MibTableColumn
rmonStatsOversizePkts = _RmonStatsOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 3, 1, 1, 9),
    _RmonStatsOversizePkts_Type()
)
rmonStatsOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonStatsOversizePkts.setStatus("current")
if mibBuilder.loadTexts:
    rmonStatsOversizePkts.setUnits("Packets")
_RmonStatsFragments_Type = Counter32
_RmonStatsFragments_Object = MibTableColumn
rmonStatsFragments = _RmonStatsFragments_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 3, 1, 1, 10),
    _RmonStatsFragments_Type()
)
rmonStatsFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonStatsFragments.setStatus("current")
if mibBuilder.loadTexts:
    rmonStatsFragments.setUnits("Packets")
_RmonStatsJabbers_Type = Counter32
_RmonStatsJabbers_Object = MibTableColumn
rmonStatsJabbers = _RmonStatsJabbers_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 3, 1, 1, 11),
    _RmonStatsJabbers_Type()
)
rmonStatsJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonStatsJabbers.setStatus("current")
if mibBuilder.loadTexts:
    rmonStatsJabbers.setUnits("Packets")
_RmonStatsCRCErrors_Type = Counter32
_RmonStatsCRCErrors_Object = MibTableColumn
rmonStatsCRCErrors = _RmonStatsCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 3, 1, 1, 12),
    _RmonStatsCRCErrors_Type()
)
rmonStatsCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonStatsCRCErrors.setStatus("current")
if mibBuilder.loadTexts:
    rmonStatsCRCErrors.setUnits("Packets")
_RmonStatsCollisions_Type = Counter32
_RmonStatsCollisions_Object = MibTableColumn
rmonStatsCollisions = _RmonStatsCollisions_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 3, 1, 1, 13),
    _RmonStatsCollisions_Type()
)
rmonStatsCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonStatsCollisions.setStatus("current")
if mibBuilder.loadTexts:
    rmonStatsCollisions.setUnits("Collisions")
_RmonStatsDropEvents_Type = Counter32
_RmonStatsDropEvents_Object = MibTableColumn
rmonStatsDropEvents = _RmonStatsDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 3, 1, 1, 14),
    _RmonStatsDropEvents_Type()
)
rmonStatsDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonStatsDropEvents.setStatus("current")
_RmonStatsPkts64Octets_Type = Counter32
_RmonStatsPkts64Octets_Object = MibTableColumn
rmonStatsPkts64Octets = _RmonStatsPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 3, 1, 1, 15),
    _RmonStatsPkts64Octets_Type()
)
rmonStatsPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonStatsPkts64Octets.setStatus("current")
if mibBuilder.loadTexts:
    rmonStatsPkts64Octets.setUnits("Packets")
_RmonStatsPkts65to127Octets_Type = Counter32
_RmonStatsPkts65to127Octets_Object = MibTableColumn
rmonStatsPkts65to127Octets = _RmonStatsPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 3, 1, 1, 16),
    _RmonStatsPkts65to127Octets_Type()
)
rmonStatsPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonStatsPkts65to127Octets.setStatus("current")
if mibBuilder.loadTexts:
    rmonStatsPkts65to127Octets.setUnits("Packets")
_RmonStatsPkts128to255Octets_Type = Counter32
_RmonStatsPkts128to255Octets_Object = MibTableColumn
rmonStatsPkts128to255Octets = _RmonStatsPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 3, 1, 1, 17),
    _RmonStatsPkts128to255Octets_Type()
)
rmonStatsPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonStatsPkts128to255Octets.setStatus("current")
if mibBuilder.loadTexts:
    rmonStatsPkts128to255Octets.setUnits("Packets")
_RmonStatsPkts256to511Octets_Type = Counter32
_RmonStatsPkts256to511Octets_Object = MibTableColumn
rmonStatsPkts256to511Octets = _RmonStatsPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 3, 1, 1, 18),
    _RmonStatsPkts256to511Octets_Type()
)
rmonStatsPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonStatsPkts256to511Octets.setStatus("current")
if mibBuilder.loadTexts:
    rmonStatsPkts256to511Octets.setUnits("Packets")
_RmonStatsPkts512to1023Octets_Type = Counter32
_RmonStatsPkts512to1023Octets_Object = MibTableColumn
rmonStatsPkts512to1023Octets = _RmonStatsPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 3, 1, 1, 19),
    _RmonStatsPkts512to1023Octets_Type()
)
rmonStatsPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonStatsPkts512to1023Octets.setStatus("current")
if mibBuilder.loadTexts:
    rmonStatsPkts512to1023Octets.setUnits("Packets")
_RmonStatsPkts1024to1518Octets_Type = Counter32
_RmonStatsPkts1024to1518Octets_Object = MibTableColumn
rmonStatsPkts1024to1518Octets = _RmonStatsPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 3, 1, 1, 20),
    _RmonStatsPkts1024to1518Octets_Type()
)
rmonStatsPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonStatsPkts1024to1518Octets.setStatus("current")
if mibBuilder.loadTexts:
    rmonStatsPkts1024to1518Octets.setUnits("Packets")
_RmonStatsStatus_Type = RmonStatus
_RmonStatsStatus_Object = MibTableColumn
rmonStatsStatus = _RmonStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 3, 1, 1, 21),
    _RmonStatsStatus_Type()
)
rmonStatsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonStatsStatus.setStatus("current")
_RmonHistory_ObjectIdentity = ObjectIdentity
rmonHistory = _RmonHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 4)
)
_RmonHistoryControlTable_Object = MibTable
rmonHistoryControlTable = _RmonHistoryControlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 4, 1)
)
if mibBuilder.loadTexts:
    rmonHistoryControlTable.setStatus("current")
_RmonHistoryControlEntry_Object = MibTableRow
rmonHistoryControlEntry = _RmonHistoryControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 4, 1, 1)
)
rmonHistoryControlEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "rmonHistoryControlIndex"),
)
if mibBuilder.loadTexts:
    rmonHistoryControlEntry.setStatus("current")


class _RmonHistoryControlIndex_Type(Integer32):
    """Custom type rmonHistoryControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RmonHistoryControlIndex_Type.__name__ = "Integer32"
_RmonHistoryControlIndex_Object = MibTableColumn
rmonHistoryControlIndex = _RmonHistoryControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 4, 1, 1, 1),
    _RmonHistoryControlIndex_Type()
)
rmonHistoryControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonHistoryControlIndex.setStatus("current")
_RmonHistoryControlDataSource_Type = ObjectIdentifier
_RmonHistoryControlDataSource_Object = MibTableColumn
rmonHistoryControlDataSource = _RmonHistoryControlDataSource_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 4, 1, 1, 2),
    _RmonHistoryControlDataSource_Type()
)
rmonHistoryControlDataSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonHistoryControlDataSource.setStatus("current")


class _RmonHistoryControlBucketsRequested_Type(Integer32):
    """Custom type rmonHistoryControlBucketsRequested based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RmonHistoryControlBucketsRequested_Type.__name__ = "Integer32"
_RmonHistoryControlBucketsRequested_Object = MibTableColumn
rmonHistoryControlBucketsRequested = _RmonHistoryControlBucketsRequested_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 4, 1, 1, 3),
    _RmonHistoryControlBucketsRequested_Type()
)
rmonHistoryControlBucketsRequested.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonHistoryControlBucketsRequested.setStatus("current")


class _RmonHistoryControlBucketsGranted_Type(Integer32):
    """Custom type rmonHistoryControlBucketsGranted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RmonHistoryControlBucketsGranted_Type.__name__ = "Integer32"
_RmonHistoryControlBucketsGranted_Object = MibTableColumn
rmonHistoryControlBucketsGranted = _RmonHistoryControlBucketsGranted_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 4, 1, 1, 4),
    _RmonHistoryControlBucketsGranted_Type()
)
rmonHistoryControlBucketsGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonHistoryControlBucketsGranted.setStatus("current")


class _RmonHistoryControlInterval_Type(Integer32):
    """Custom type rmonHistoryControlInterval based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_RmonHistoryControlInterval_Type.__name__ = "Integer32"
_RmonHistoryControlInterval_Object = MibTableColumn
rmonHistoryControlInterval = _RmonHistoryControlInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 4, 1, 1, 5),
    _RmonHistoryControlInterval_Type()
)
rmonHistoryControlInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonHistoryControlInterval.setStatus("current")
if mibBuilder.loadTexts:
    rmonHistoryControlInterval.setUnits("Seconds")
_RmonHistoryControlOwner_Type = OwnerString
_RmonHistoryControlOwner_Object = MibTableColumn
rmonHistoryControlOwner = _RmonHistoryControlOwner_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 4, 1, 1, 6),
    _RmonHistoryControlOwner_Type()
)
rmonHistoryControlOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonHistoryControlOwner.setStatus("current")
_RmonHistoryControlStatus_Type = RmonStatus
_RmonHistoryControlStatus_Object = MibTableColumn
rmonHistoryControlStatus = _RmonHistoryControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 4, 1, 1, 7),
    _RmonHistoryControlStatus_Type()
)
rmonHistoryControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonHistoryControlStatus.setStatus("current")
_RmonHistoryTable_Object = MibTable
rmonHistoryTable = _RmonHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 4, 2)
)
if mibBuilder.loadTexts:
    rmonHistoryTable.setStatus("current")
_RmonHistoryEntry_Object = MibTableRow
rmonHistoryEntry = _RmonHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 4, 2, 1)
)
rmonHistoryEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "rmonHistoryIndex"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "rmonHistorySampleIndex"),
)
if mibBuilder.loadTexts:
    rmonHistoryEntry.setStatus("current")


class _RmonHistoryIndex_Type(Integer32):
    """Custom type rmonHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RmonHistoryIndex_Type.__name__ = "Integer32"
_RmonHistoryIndex_Object = MibTableColumn
rmonHistoryIndex = _RmonHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 4, 2, 1, 1),
    _RmonHistoryIndex_Type()
)
rmonHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonHistoryIndex.setStatus("current")


class _RmonHistorySampleIndex_Type(Integer32):
    """Custom type rmonHistorySampleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RmonHistorySampleIndex_Type.__name__ = "Integer32"
_RmonHistorySampleIndex_Object = MibTableColumn
rmonHistorySampleIndex = _RmonHistorySampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 4, 2, 1, 2),
    _RmonHistorySampleIndex_Type()
)
rmonHistorySampleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonHistorySampleIndex.setStatus("current")
_RmonHistoryOctets_Type = Counter32
_RmonHistoryOctets_Object = MibTableColumn
rmonHistoryOctets = _RmonHistoryOctets_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 4, 2, 1, 3),
    _RmonHistoryOctets_Type()
)
rmonHistoryOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonHistoryOctets.setStatus("current")
if mibBuilder.loadTexts:
    rmonHistoryOctets.setUnits("Octets")
_RmonHistoryPkts_Type = Counter32
_RmonHistoryPkts_Object = MibTableColumn
rmonHistoryPkts = _RmonHistoryPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 4, 2, 1, 4),
    _RmonHistoryPkts_Type()
)
rmonHistoryPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonHistoryPkts.setStatus("current")
if mibBuilder.loadTexts:
    rmonHistoryPkts.setUnits("Packets")
_RmonHistoryBroadcastPkts_Type = Counter32
_RmonHistoryBroadcastPkts_Object = MibTableColumn
rmonHistoryBroadcastPkts = _RmonHistoryBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 4, 2, 1, 5),
    _RmonHistoryBroadcastPkts_Type()
)
rmonHistoryBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonHistoryBroadcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    rmonHistoryBroadcastPkts.setUnits("Packets")
_RmonHistoryMulticastPkts_Type = Counter32
_RmonHistoryMulticastPkts_Object = MibTableColumn
rmonHistoryMulticastPkts = _RmonHistoryMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 4, 2, 1, 6),
    _RmonHistoryMulticastPkts_Type()
)
rmonHistoryMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonHistoryMulticastPkts.setStatus("current")
if mibBuilder.loadTexts:
    rmonHistoryMulticastPkts.setUnits("Packets")


class _RmonHistoryUtilization_Type(Integer32):
    """Custom type rmonHistoryUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_RmonHistoryUtilization_Type.__name__ = "Integer32"
_RmonHistoryUtilization_Object = MibTableColumn
rmonHistoryUtilization = _RmonHistoryUtilization_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 4, 2, 1, 7),
    _RmonHistoryUtilization_Type()
)
rmonHistoryUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonHistoryUtilization.setStatus("current")
_RmonHistoryUndersizePkts_Type = Counter32
_RmonHistoryUndersizePkts_Object = MibTableColumn
rmonHistoryUndersizePkts = _RmonHistoryUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 4, 2, 1, 8),
    _RmonHistoryUndersizePkts_Type()
)
rmonHistoryUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonHistoryUndersizePkts.setStatus("current")
if mibBuilder.loadTexts:
    rmonHistoryUndersizePkts.setUnits("Packets")
_RmonHistoryOversizePkts_Type = Counter32
_RmonHistoryOversizePkts_Object = MibTableColumn
rmonHistoryOversizePkts = _RmonHistoryOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 4, 2, 1, 9),
    _RmonHistoryOversizePkts_Type()
)
rmonHistoryOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonHistoryOversizePkts.setStatus("current")
if mibBuilder.loadTexts:
    rmonHistoryOversizePkts.setUnits("Packets")
_RmonHistoryFragments_Type = Counter32
_RmonHistoryFragments_Object = MibTableColumn
rmonHistoryFragments = _RmonHistoryFragments_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 4, 2, 1, 10),
    _RmonHistoryFragments_Type()
)
rmonHistoryFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonHistoryFragments.setStatus("current")
if mibBuilder.loadTexts:
    rmonHistoryFragments.setUnits("Packets")
_RmonHistoryJabbers_Type = Counter32
_RmonHistoryJabbers_Object = MibTableColumn
rmonHistoryJabbers = _RmonHistoryJabbers_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 4, 2, 1, 11),
    _RmonHistoryJabbers_Type()
)
rmonHistoryJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonHistoryJabbers.setStatus("current")
if mibBuilder.loadTexts:
    rmonHistoryJabbers.setUnits("Packets")
_RmonHistoryCRCErrors_Type = Counter32
_RmonHistoryCRCErrors_Object = MibTableColumn
rmonHistoryCRCErrors = _RmonHistoryCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 4, 2, 1, 12),
    _RmonHistoryCRCErrors_Type()
)
rmonHistoryCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonHistoryCRCErrors.setStatus("current")
if mibBuilder.loadTexts:
    rmonHistoryCRCErrors.setUnits("Packets")
_RmonHistoryCollisions_Type = Counter32
_RmonHistoryCollisions_Object = MibTableColumn
rmonHistoryCollisions = _RmonHistoryCollisions_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 4, 2, 1, 13),
    _RmonHistoryCollisions_Type()
)
rmonHistoryCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonHistoryCollisions.setStatus("current")
if mibBuilder.loadTexts:
    rmonHistoryCollisions.setUnits("Collisions")
_RmonHistoryDropEvents_Type = Counter32
_RmonHistoryDropEvents_Object = MibTableColumn
rmonHistoryDropEvents = _RmonHistoryDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 4, 2, 1, 14),
    _RmonHistoryDropEvents_Type()
)
rmonHistoryDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonHistoryDropEvents.setStatus("current")
_RmonAlarm_ObjectIdentity = ObjectIdentity
rmonAlarm = _RmonAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 5)
)
_RmonAlarmTable_Object = MibTable
rmonAlarmTable = _RmonAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 5, 1)
)
if mibBuilder.loadTexts:
    rmonAlarmTable.setStatus("current")
_RmonAlarmEntry_Object = MibTableRow
rmonAlarmEntry = _RmonAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 5, 1, 1)
)
rmonAlarmEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "rmonAlarmIndex"),
)
if mibBuilder.loadTexts:
    rmonAlarmEntry.setStatus("current")


class _RmonAlarmIndex_Type(Integer32):
    """Custom type rmonAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RmonAlarmIndex_Type.__name__ = "Integer32"
_RmonAlarmIndex_Object = MibTableColumn
rmonAlarmIndex = _RmonAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 5, 1, 1, 1),
    _RmonAlarmIndex_Type()
)
rmonAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonAlarmIndex.setStatus("current")
_RmonAlarmInterval_Type = Integer32
_RmonAlarmInterval_Object = MibTableColumn
rmonAlarmInterval = _RmonAlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 5, 1, 1, 2),
    _RmonAlarmInterval_Type()
)
rmonAlarmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonAlarmInterval.setStatus("current")
if mibBuilder.loadTexts:
    rmonAlarmInterval.setUnits("Seconds")
_RmonAlarmVariable_Type = ObjectIdentifier
_RmonAlarmVariable_Object = MibTableColumn
rmonAlarmVariable = _RmonAlarmVariable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 5, 1, 1, 3),
    _RmonAlarmVariable_Type()
)
rmonAlarmVariable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonAlarmVariable.setStatus("current")


class _RmonAlarmSampleType_Type(Integer32):
    """Custom type rmonAlarmSampleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absoluteValue", 1),
          ("deltaValue", 2))
    )


_RmonAlarmSampleType_Type.__name__ = "Integer32"
_RmonAlarmSampleType_Object = MibTableColumn
rmonAlarmSampleType = _RmonAlarmSampleType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 5, 1, 1, 4),
    _RmonAlarmSampleType_Type()
)
rmonAlarmSampleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonAlarmSampleType.setStatus("current")
_RmonAlarmValue_Type = Integer32
_RmonAlarmValue_Object = MibTableColumn
rmonAlarmValue = _RmonAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 5, 1, 1, 5),
    _RmonAlarmValue_Type()
)
rmonAlarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonAlarmValue.setStatus("current")


class _RmonAlarmStartupAlarm_Type(Integer32):
    """Custom type rmonAlarmStartupAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fallingAlarm", 2),
          ("risingAlarm", 1),
          ("risingOrFallingAlarm", 3))
    )


_RmonAlarmStartupAlarm_Type.__name__ = "Integer32"
_RmonAlarmStartupAlarm_Object = MibTableColumn
rmonAlarmStartupAlarm = _RmonAlarmStartupAlarm_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 5, 1, 1, 6),
    _RmonAlarmStartupAlarm_Type()
)
rmonAlarmStartupAlarm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonAlarmStartupAlarm.setStatus("current")
_RmonAlarmRisingThreshold_Type = Integer32
_RmonAlarmRisingThreshold_Object = MibTableColumn
rmonAlarmRisingThreshold = _RmonAlarmRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 5, 1, 1, 7),
    _RmonAlarmRisingThreshold_Type()
)
rmonAlarmRisingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonAlarmRisingThreshold.setStatus("current")
_RmonAlarmFallingThreshold_Type = Integer32
_RmonAlarmFallingThreshold_Object = MibTableColumn
rmonAlarmFallingThreshold = _RmonAlarmFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 5, 1, 1, 8),
    _RmonAlarmFallingThreshold_Type()
)
rmonAlarmFallingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonAlarmFallingThreshold.setStatus("current")


class _RmonAlarmRisingEventNumber_Type(Integer32):
    """Custom type rmonAlarmRisingEventNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmonAlarmRisingEventNumber_Type.__name__ = "Integer32"
_RmonAlarmRisingEventNumber_Object = MibTableColumn
rmonAlarmRisingEventNumber = _RmonAlarmRisingEventNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 5, 1, 1, 9),
    _RmonAlarmRisingEventNumber_Type()
)
rmonAlarmRisingEventNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonAlarmRisingEventNumber.setStatus("current")


class _RmonAlarmFallingEventNumber_Type(Integer32):
    """Custom type rmonAlarmFallingEventNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmonAlarmFallingEventNumber_Type.__name__ = "Integer32"
_RmonAlarmFallingEventNumber_Object = MibTableColumn
rmonAlarmFallingEventNumber = _RmonAlarmFallingEventNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 5, 1, 1, 10),
    _RmonAlarmFallingEventNumber_Type()
)
rmonAlarmFallingEventNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonAlarmFallingEventNumber.setStatus("current")
_RmonAlarmOwner_Type = OwnerString
_RmonAlarmOwner_Object = MibTableColumn
rmonAlarmOwner = _RmonAlarmOwner_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 5, 1, 1, 11),
    _RmonAlarmOwner_Type()
)
rmonAlarmOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonAlarmOwner.setStatus("current")
_RmonAlarmStatus_Type = RmonStatus
_RmonAlarmStatus_Object = MibTableColumn
rmonAlarmStatus = _RmonAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 5, 1, 1, 12),
    _RmonAlarmStatus_Type()
)
rmonAlarmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonAlarmStatus.setStatus("current")
_RmonEvent_ObjectIdentity = ObjectIdentity
rmonEvent = _RmonEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 6)
)
_RmonEventTable_Object = MibTable
rmonEventTable = _RmonEventTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 6, 1)
)
if mibBuilder.loadTexts:
    rmonEventTable.setStatus("current")
_RmonEventEntry_Object = MibTableRow
rmonEventEntry = _RmonEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 6, 1, 1)
)
rmonEventEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "rmonEventIndex"),
)
if mibBuilder.loadTexts:
    rmonEventEntry.setStatus("current")


class _RmonEventIndex_Type(Integer32):
    """Custom type rmonEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RmonEventIndex_Type.__name__ = "Integer32"
_RmonEventIndex_Object = MibTableColumn
rmonEventIndex = _RmonEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 6, 1, 1, 1),
    _RmonEventIndex_Type()
)
rmonEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonEventIndex.setStatus("current")


class _RmonEventDescription_Type(DisplayString):
    """Custom type rmonEventDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_RmonEventDescription_Type.__name__ = "DisplayString"
_RmonEventDescription_Object = MibTableColumn
rmonEventDescription = _RmonEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 6, 1, 1, 2),
    _RmonEventDescription_Type()
)
rmonEventDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonEventDescription.setStatus("current")


class _RmonEventType_Type(Integer32):
    """Custom type rmonEventType based on Integer32"""
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
        *(("log", 2),
          ("logandtrap", 4),
          ("none", 1),
          ("snmptrap", 3))
    )


_RmonEventType_Type.__name__ = "Integer32"
_RmonEventType_Object = MibTableColumn
rmonEventType = _RmonEventType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 6, 1, 1, 3),
    _RmonEventType_Type()
)
rmonEventType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonEventType.setStatus("current")
_RmonEventCommunity_Type = OwnerString
_RmonEventCommunity_Object = MibTableColumn
rmonEventCommunity = _RmonEventCommunity_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 6, 1, 1, 4),
    _RmonEventCommunity_Type()
)
rmonEventCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonEventCommunity.setStatus("current")
_RmonEventOwner_Type = OwnerString
_RmonEventOwner_Object = MibTableColumn
rmonEventOwner = _RmonEventOwner_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 6, 1, 1, 5),
    _RmonEventOwner_Type()
)
rmonEventOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonEventOwner.setStatus("current")
_RmonEventStatus_Type = RmonStatus
_RmonEventStatus_Object = MibTableColumn
rmonEventStatus = _RmonEventStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 6, 1, 1, 6),
    _RmonEventStatus_Type()
)
rmonEventStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonEventStatus.setStatus("current")
_RmonEventLastTimeSent_Type = TimeTicks
_RmonEventLastTimeSent_Object = MibTableColumn
rmonEventLastTimeSent = _RmonEventLastTimeSent_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 6, 1, 1, 7),
    _RmonEventLastTimeSent_Type()
)
rmonEventLastTimeSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonEventLastTimeSent.setStatus("current")
_RmonLogTable_Object = MibTable
rmonLogTable = _RmonLogTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 6, 2)
)
if mibBuilder.loadTexts:
    rmonLogTable.setStatus("current")
_RmonLogEntry_Object = MibTableRow
rmonLogEntry = _RmonLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 6, 2, 1)
)
rmonLogEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "rmonLogEventIndex"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "rmonLogIndex"),
)
if mibBuilder.loadTexts:
    rmonLogEntry.setStatus("current")


class _RmonLogEventIndex_Type(Integer32):
    """Custom type rmonLogEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RmonLogEventIndex_Type.__name__ = "Integer32"
_RmonLogEventIndex_Object = MibTableColumn
rmonLogEventIndex = _RmonLogEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 6, 2, 1, 1),
    _RmonLogEventIndex_Type()
)
rmonLogEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLogEventIndex.setStatus("current")


class _RmonLogIndex_Type(Integer32):
    """Custom type rmonLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RmonLogIndex_Type.__name__ = "Integer32"
_RmonLogIndex_Object = MibTableColumn
rmonLogIndex = _RmonLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 6, 2, 1, 2),
    _RmonLogIndex_Type()
)
rmonLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLogIndex.setStatus("current")
_RmonLogTime_Type = TimeTicks
_RmonLogTime_Object = MibTableColumn
rmonLogTime = _RmonLogTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 6, 2, 1, 3),
    _RmonLogTime_Type()
)
rmonLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLogTime.setStatus("current")


class _RmonLogDescription_Type(DisplayString):
    """Custom type rmonLogDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RmonLogDescription_Type.__name__ = "DisplayString"
_RmonLogDescription_Object = MibTableColumn
rmonLogDescription = _RmonLogDescription_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 4, 6, 2, 1, 4),
    _RmonLogDescription_Type()
)
rmonLogDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonLogDescription.setStatus("current")
_MgtTelnetWebGroup_ObjectIdentity = ObjectIdentity
mgtTelnetWebGroup = _MgtTelnetWebGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 5)
)


class _TelnetState_Type(Integer32):
    """Custom type telnetState based on Integer32"""
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


_TelnetState_Type.__name__ = "Integer32"
_TelnetState_Object = MibScalar
telnetState = _TelnetState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 5, 1),
    _TelnetState_Type()
)
telnetState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetState.setStatus("current")


class _TelnetPort_Type(Integer32):
    """Custom type telnetPort based on Integer32"""
    defaultValue = 23

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TelnetPort_Type.__name__ = "Integer32"
_TelnetPort_Object = MibScalar
telnetPort = _TelnetPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 5, 2),
    _TelnetPort_Type()
)
telnetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetPort.setStatus("current")


class _WebState_Type(Integer32):
    """Custom type webState based on Integer32"""
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


_WebState_Type.__name__ = "Integer32"
_WebState_Object = MibScalar
webState = _WebState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 5, 3),
    _WebState_Type()
)
webState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webState.setStatus("current")


class _WebPort_Type(Integer32):
    """Custom type webPort based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WebPort_Type.__name__ = "Integer32"
_WebPort_Object = MibScalar
webPort = _WebPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 5, 4),
    _WebPort_Type()
)
webPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webPort.setStatus("current")
_MgtSessionTimeoutGroup_ObjectIdentity = ObjectIdentity
mgtSessionTimeoutGroup = _MgtSessionTimeoutGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 6)
)


class _SessionTimeoutWeb_Type(Integer32):
    """Custom type sessionTimeoutWeb based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 36000),
    )


_SessionTimeoutWeb_Type.__name__ = "Integer32"
_SessionTimeoutWeb_Object = MibScalar
sessionTimeoutWeb = _SessionTimeoutWeb_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 6, 1),
    _SessionTimeoutWeb_Type()
)
sessionTimeoutWeb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sessionTimeoutWeb.setStatus("current")


class _SessionTimeoutTelnet_Type(Integer32):
    """Custom type sessionTimeoutTelnet based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1439),
    )


_SessionTimeoutTelnet_Type.__name__ = "Integer32"
_SessionTimeoutTelnet_Object = MibScalar
sessionTimeoutTelnet = _SessionTimeoutTelnet_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 6, 2),
    _SessionTimeoutTelnet_Type()
)
sessionTimeoutTelnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sessionTimeoutTelnet.setStatus("current")
_MgtDDPGroup_ObjectIdentity = ObjectIdentity
mgtDDPGroup = _MgtDDPGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 14)
)


class _DdpStatus_Type(Integer32):
    """Custom type ddpStatus based on Integer32"""
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


_DdpStatus_Type.__name__ = "Integer32"
_DdpStatus_Object = MibScalar
ddpStatus = _DdpStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 14, 1),
    _DdpStatus_Type()
)
ddpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddpStatus.setStatus("current")


class _DdpReportTime_Type(Integer32):
    """Custom type ddpReportTime based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              30,
              60,
              90,
              120)
        )
    )
    namedValues = NamedValues(
        *(("never", 0),
          ("offset120sec", 120),
          ("offset30sec", 30),
          ("offset60sec", 60),
          ("offset90sec", 90))
    )


_DdpReportTime_Type.__name__ = "Integer32"
_DdpReportTime_Object = MibScalar
ddpReportTime = _DdpReportTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 14, 2),
    _DdpReportTime_Type()
)
ddpReportTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddpReportTime.setStatus("current")
_DdpTable_Object = MibTable
ddpTable = _DdpTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 14, 3)
)
if mibBuilder.loadTexts:
    ddpTable.setStatus("current")
_DdpEntry_Object = MibTableRow
ddpEntry = _DdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 14, 3, 1)
)
ddpEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "ddpPort"),
)
if mibBuilder.loadTexts:
    ddpEntry.setStatus("current")


class _DdpPort_Type(Integer32):
    """Custom type ddpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DdpPort_Type.__name__ = "Integer32"
_DdpPort_Object = MibTableColumn
ddpPort = _DdpPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 14, 3, 1, 1),
    _DdpPort_Type()
)
ddpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpPort.setStatus("current")


class _DdpPortStatus_Type(Integer32):
    """Custom type ddpPortStatus based on Integer32"""
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


_DdpPortStatus_Type.__name__ = "Integer32"
_DdpPortStatus_Object = MibTableColumn
ddpPortStatus = _DdpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 3, 14, 3, 1, 2),
    _DdpPortStatus_Type()
)
ddpPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddpPortStatus.setStatus("current")
_DlinkL2Features_ObjectIdentity = ObjectIdentity
dlinkL2Features = _DlinkL2Features_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4)
)
_L2FDBGroup_ObjectIdentity = ObjectIdentity
l2FDBGroup = _L2FDBGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 1)
)
_FdbStaticFDB_ObjectIdentity = ObjectIdentity
fdbStaticFDB = _FdbStaticFDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 1, 1)
)
_FdbUnicastStaticFDB_ObjectIdentity = ObjectIdentity
fdbUnicastStaticFDB = _FdbUnicastStaticFDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 1, 1, 1)
)
_FdbUnicastStaticFDBTable_Object = MibTable
fdbUnicastStaticFDBTable = _FdbUnicastStaticFDBTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    fdbUnicastStaticFDBTable.setStatus("current")
_FdbUnicastStaticFDBEntry_Object = MibTableRow
fdbUnicastStaticFDBEntry = _FdbUnicastStaticFDBEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 1, 1, 1, 1, 1)
)
fdbUnicastStaticFDBEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "fdbUnicastStaticFDBVID"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "fdbUnicastStaticFDBMACAddr"),
)
if mibBuilder.loadTexts:
    fdbUnicastStaticFDBEntry.setStatus("current")


class _FdbUnicastStaticFDBVID_Type(Integer32):
    """Custom type fdbUnicastStaticFDBVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FdbUnicastStaticFDBVID_Type.__name__ = "Integer32"
_FdbUnicastStaticFDBVID_Object = MibTableColumn
fdbUnicastStaticFDBVID = _FdbUnicastStaticFDBVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 1, 1, 1, 1, 1, 1),
    _FdbUnicastStaticFDBVID_Type()
)
fdbUnicastStaticFDBVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbUnicastStaticFDBVID.setStatus("current")
_FdbUnicastStaticFDBMACAddr_Type = MacAddress
_FdbUnicastStaticFDBMACAddr_Object = MibTableColumn
fdbUnicastStaticFDBMACAddr = _FdbUnicastStaticFDBMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 1, 1, 1, 1, 1, 2),
    _FdbUnicastStaticFDBMACAddr_Type()
)
fdbUnicastStaticFDBMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbUnicastStaticFDBMACAddr.setStatus("current")
_FdbUnicastStaticFDBPort_Type = InterfaceIndex
_FdbUnicastStaticFDBPort_Object = MibTableColumn
fdbUnicastStaticFDBPort = _FdbUnicastStaticFDBPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 1, 1, 1, 1, 1, 3),
    _FdbUnicastStaticFDBPort_Type()
)
fdbUnicastStaticFDBPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdbUnicastStaticFDBPort.setStatus("current")


class _FdbUnicastStaticFDBState_Type(Integer32):
    """Custom type fdbUnicastStaticFDBState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permanent", 1),
          ("permanentDrop", 2))
    )


_FdbUnicastStaticFDBState_Type.__name__ = "Integer32"
_FdbUnicastStaticFDBState_Object = MibTableColumn
fdbUnicastStaticFDBState = _FdbUnicastStaticFDBState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 1, 1, 1, 1, 1, 4),
    _FdbUnicastStaticFDBState_Type()
)
fdbUnicastStaticFDBState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdbUnicastStaticFDBState.setStatus("current")
_FdbUnicastStaticFDBRowStatus_Type = RowStatus
_FdbUnicastStaticFDBRowStatus_Object = MibTableColumn
fdbUnicastStaticFDBRowStatus = _FdbUnicastStaticFDBRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 1, 1, 1, 1, 1, 5),
    _FdbUnicastStaticFDBRowStatus_Type()
)
fdbUnicastStaticFDBRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdbUnicastStaticFDBRowStatus.setStatus("current")
_FdbMulticastStaticFDB_ObjectIdentity = ObjectIdentity
fdbMulticastStaticFDB = _FdbMulticastStaticFDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 1, 1, 2)
)
_FdMulticastStaticFDBTable_Object = MibTable
fdMulticastStaticFDBTable = _FdMulticastStaticFDBTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fdMulticastStaticFDBTable.setStatus("current")
_FdbMulticastStaticFDBEntry_Object = MibTableRow
fdbMulticastStaticFDBEntry = _FdbMulticastStaticFDBEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 1, 1, 2, 1, 1)
)
fdbMulticastStaticFDBEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "fdbMulticastStaticFDBVID"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "fdbMulticastStaticFDBMACAddr"),
)
if mibBuilder.loadTexts:
    fdbMulticastStaticFDBEntry.setStatus("current")


class _FdbMulticastStaticFDBVID_Type(Integer32):
    """Custom type fdbMulticastStaticFDBVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FdbMulticastStaticFDBVID_Type.__name__ = "Integer32"
_FdbMulticastStaticFDBVID_Object = MibTableColumn
fdbMulticastStaticFDBVID = _FdbMulticastStaticFDBVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 1, 1, 2, 1, 1, 1),
    _FdbMulticastStaticFDBVID_Type()
)
fdbMulticastStaticFDBVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbMulticastStaticFDBVID.setStatus("current")
_FdbMulticastStaticFDBMACAddr_Type = MacAddress
_FdbMulticastStaticFDBMACAddr_Object = MibTableColumn
fdbMulticastStaticFDBMACAddr = _FdbMulticastStaticFDBMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 1, 1, 2, 1, 1, 2),
    _FdbMulticastStaticFDBMACAddr_Type()
)
fdbMulticastStaticFDBMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbMulticastStaticFDBMACAddr.setStatus("current")
_FdbMulticastStaticFDBEgressPorts_Type = PortList
_FdbMulticastStaticFDBEgressPorts_Object = MibTableColumn
fdbMulticastStaticFDBEgressPorts = _FdbMulticastStaticFDBEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 1, 1, 2, 1, 1, 3),
    _FdbMulticastStaticFDBEgressPorts_Type()
)
fdbMulticastStaticFDBEgressPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdbMulticastStaticFDBEgressPorts.setStatus("current")
_FdbMulticastStaticFDBRowStatus_Type = RowStatus
_FdbMulticastStaticFDBRowStatus_Object = MibTableColumn
fdbMulticastStaticFDBRowStatus = _FdbMulticastStaticFDBRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 1, 1, 2, 1, 1, 4),
    _FdbMulticastStaticFDBRowStatus_Type()
)
fdbMulticastStaticFDBRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdbMulticastStaticFDBRowStatus.setStatus("current")
_FdbMACAddressTableSettings_ObjectIdentity = ObjectIdentity
fdbMACAddressTableSettings = _FdbMACAddressTableSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 1, 2)
)
_FdbMACAddrGlobalSettings_ObjectIdentity = ObjectIdentity
fdbMACAddrGlobalSettings = _FdbMACAddrGlobalSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 1, 2, 1)
)


class _FdbMACAddrAgingTime_Type(Integer32):
    """Custom type fdbMACAddrAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_FdbMACAddrAgingTime_Type.__name__ = "Integer32"
_FdbMACAddrAgingTime_Object = MibScalar
fdbMACAddrAgingTime = _FdbMACAddrAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 1, 2, 1, 1),
    _FdbMACAddrAgingTime_Type()
)
fdbMACAddrAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdbMACAddrAgingTime.setStatus("current")


class _FdbMACAddrAgingDestinationHit_Type(Integer32):
    """Custom type fdbMACAddrAgingDestinationHit based on Integer32"""
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


_FdbMACAddrAgingDestinationHit_Type.__name__ = "Integer32"
_FdbMACAddrAgingDestinationHit_Object = MibScalar
fdbMACAddrAgingDestinationHit = _FdbMACAddrAgingDestinationHit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 1, 2, 1, 2),
    _FdbMACAddrAgingDestinationHit_Type()
)
fdbMACAddrAgingDestinationHit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdbMACAddrAgingDestinationHit.setStatus("current")
_FdbMACAddressLearningTable_Object = MibTable
fdbMACAddressLearningTable = _FdbMACAddressLearningTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 1, 2, 2)
)
if mibBuilder.loadTexts:
    fdbMACAddressLearningTable.setStatus("current")
_FdbMACAddressLearningEntry_Object = MibTableRow
fdbMACAddressLearningEntry = _FdbMACAddressLearningEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 1, 2, 2, 1)
)
fdbMACAddressLearningEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "fdbMACAddressLearningPort"),
)
if mibBuilder.loadTexts:
    fdbMACAddressLearningEntry.setStatus("current")
_FdbMACAddressLearningPort_Type = InterfaceIndex
_FdbMACAddressLearningPort_Object = MibTableColumn
fdbMACAddressLearningPort = _FdbMACAddressLearningPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 1, 2, 2, 1, 1),
    _FdbMACAddressLearningPort_Type()
)
fdbMACAddressLearningPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbMACAddressLearningPort.setStatus("current")


class _FdbMACAddressLearningState_Type(Integer32):
    """Custom type fdbMACAddressLearningState based on Integer32"""
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


_FdbMACAddressLearningState_Type.__name__ = "Integer32"
_FdbMACAddressLearningState_Object = MibTableColumn
fdbMACAddressLearningState = _FdbMACAddressLearningState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 1, 2, 2, 1, 2),
    _FdbMACAddressLearningState_Type()
)
fdbMACAddressLearningState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdbMACAddressLearningState.setStatus("current")
_FdbMACAddressTable_Object = MibTable
fdbMACAddressTable = _FdbMACAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 1, 3)
)
if mibBuilder.loadTexts:
    fdbMACAddressTable.setStatus("current")
_FdbMACAddressTableEntry_Object = MibTableRow
fdbMACAddressTableEntry = _FdbMACAddressTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 1, 3, 1)
)
fdbMACAddressTableEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "fdbMACAddrTabVID"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "fdbMACAddrTabMACAddr"),
)
if mibBuilder.loadTexts:
    fdbMACAddressTableEntry.setStatus("current")


class _FdbMACAddrTabVID_Type(Integer32):
    """Custom type fdbMACAddrTabVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FdbMACAddrTabVID_Type.__name__ = "Integer32"
_FdbMACAddrTabVID_Object = MibTableColumn
fdbMACAddrTabVID = _FdbMACAddrTabVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 1, 3, 1, 1),
    _FdbMACAddrTabVID_Type()
)
fdbMACAddrTabVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbMACAddrTabVID.setStatus("current")
_FdbMACAddrTabMACAddr_Type = MacAddress
_FdbMACAddrTabMACAddr_Object = MibTableColumn
fdbMACAddrTabMACAddr = _FdbMACAddrTabMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 1, 3, 1, 2),
    _FdbMACAddrTabMACAddr_Type()
)
fdbMACAddrTabMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbMACAddrTabMACAddr.setStatus("current")


class _FdbMACAddrTabType_Type(Integer32):
    """Custom type fdbMACAddrTabType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 3),
          ("self", 4),
          ("static", 5))
    )


_FdbMACAddrTabType_Type.__name__ = "Integer32"
_FdbMACAddrTabType_Object = MibTableColumn
fdbMACAddrTabType = _FdbMACAddrTabType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 1, 3, 1, 3),
    _FdbMACAddrTabType_Type()
)
fdbMACAddrTabType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbMACAddrTabType.setStatus("current")
_FdbMACAddrTabPort_Type = DisplayString
_FdbMACAddrTabPort_Object = MibTableColumn
fdbMACAddrTabPort = _FdbMACAddrTabPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 1, 3, 1, 4),
    _FdbMACAddrTabPort_Type()
)
fdbMACAddrTabPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbMACAddrTabPort.setStatus("current")
_FdbMACAddressClear_ObjectIdentity = ObjectIdentity
fdbMACAddressClear = _FdbMACAddressClear_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 1, 4)
)


class _FdbClearId_Type(Unsigned32):
    """Custom type fdbClearId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FdbClearId_Type.__name__ = "Unsigned32"
_FdbClearId_Object = MibScalar
fdbClearId = _FdbClearId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 1, 4, 1),
    _FdbClearId_Type()
)
fdbClearId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdbClearId.setStatus("current")
_FdbClearMac_Type = MacAddress
_FdbClearMac_Object = MibScalar
fdbClearMac = _FdbClearMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 1, 4, 2),
    _FdbClearMac_Type()
)
fdbClearMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdbClearMac.setStatus("current")


class _FdbClearAction_Type(Integer32):
    """Custom type fdbClearAction based on Integer32"""
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
        *(("clearAll", 1),
          ("clearByMAC", 4),
          ("clearByPort", 3),
          ("clearByVlanId", 2))
    )


_FdbClearAction_Type.__name__ = "Integer32"
_FdbClearAction_Object = MibScalar
fdbClearAction = _FdbClearAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 1, 4, 3),
    _FdbClearAction_Type()
)
fdbClearAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdbClearAction.setStatus("current")
_L2Dot1qVlanGroup_ObjectIdentity = ObjectIdentity
l2Dot1qVlanGroup = _L2Dot1qVlanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 2)
)


class _Dot1qVlanAsyOnOff_Type(Integer32):
    """Custom type dot1qVlanAsyOnOff based on Integer32"""
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


_Dot1qVlanAsyOnOff_Type.__name__ = "Integer32"
_Dot1qVlanAsyOnOff_Object = MibScalar
dot1qVlanAsyOnOff = _Dot1qVlanAsyOnOff_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 2, 1),
    _Dot1qVlanAsyOnOff_Type()
)
dot1qVlanAsyOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qVlanAsyOnOff.setStatus("current")
_Dot1qVlanTable_Object = MibTable
dot1qVlanTable = _Dot1qVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    dot1qVlanTable.setStatus("current")
_Dot1qVlanEntry_Object = MibTableRow
dot1qVlanEntry = _Dot1qVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 2, 2, 1)
)
dot1qVlanEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "dot1qVlanid"),
)
if mibBuilder.loadTexts:
    dot1qVlanEntry.setStatus("current")


class _Dot1qVlanid_Type(Integer32):
    """Custom type dot1qVlanid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Dot1qVlanid_Type.__name__ = "Integer32"
_Dot1qVlanid_Object = MibTableColumn
dot1qVlanid = _Dot1qVlanid_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 2, 2, 1, 1),
    _Dot1qVlanid_Type()
)
dot1qVlanid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qVlanid.setStatus("current")


class _Dot1qVlanName_Type(SnmpAdminString):
    """Custom type dot1qVlanName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Dot1qVlanName_Type.__name__ = "SnmpAdminString"
_Dot1qVlanName_Object = MibTableColumn
dot1qVlanName = _Dot1qVlanName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 2, 2, 1, 2),
    _Dot1qVlanName_Type()
)
dot1qVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qVlanName.setStatus("current")
_Dot1qVlanEgressPorts_Type = PortList
_Dot1qVlanEgressPorts_Object = MibTableColumn
dot1qVlanEgressPorts = _Dot1qVlanEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 2, 2, 1, 3),
    _Dot1qVlanEgressPorts_Type()
)
dot1qVlanEgressPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qVlanEgressPorts.setStatus("current")
_Dot1qVlanUntaggedPorts_Type = PortList
_Dot1qVlanUntaggedPorts_Object = MibTableColumn
dot1qVlanUntaggedPorts = _Dot1qVlanUntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 2, 2, 1, 4),
    _Dot1qVlanUntaggedPorts_Type()
)
dot1qVlanUntaggedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qVlanUntaggedPorts.setStatus("current")
_Dot1qVlanRowStatus_Type = RowStatus
_Dot1qVlanRowStatus_Object = MibTableColumn
dot1qVlanRowStatus = _Dot1qVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 2, 2, 1, 99),
    _Dot1qVlanRowStatus_Type()
)
dot1qVlanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qVlanRowStatus.setStatus("current")
_Dot1qVlanPortTable_Object = MibTable
dot1qVlanPortTable = _Dot1qVlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 2, 3)
)
if mibBuilder.loadTexts:
    dot1qVlanPortTable.setStatus("current")
_Dot1qVlanPortEntry_Object = MibTableRow
dot1qVlanPortEntry = _Dot1qVlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 2, 3, 1)
)
dot1qVlanPortEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "dot1qVlanPortIndex"),
)
if mibBuilder.loadTexts:
    dot1qVlanPortEntry.setStatus("current")
_Dot1qVlanPortIndex_Type = Integer32
_Dot1qVlanPortIndex_Object = MibTableColumn
dot1qVlanPortIndex = _Dot1qVlanPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 2, 3, 1, 1),
    _Dot1qVlanPortIndex_Type()
)
dot1qVlanPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qVlanPortIndex.setStatus("current")


class _Dot1qVlanPortVlanMode_Type(Integer32):
    """Custom type dot1qVlanPortVlanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("access", 1),
          ("hybrid", 3),
          ("trunk", 2))
    )


_Dot1qVlanPortVlanMode_Type.__name__ = "Integer32"
_Dot1qVlanPortVlanMode_Object = MibTableColumn
dot1qVlanPortVlanMode = _Dot1qVlanPortVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 2, 3, 1, 2),
    _Dot1qVlanPortVlanMode_Type()
)
dot1qVlanPortVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qVlanPortVlanMode.setStatus("current")


class _Dot1qVlanPortAcceptableFrameType_Type(Integer32):
    """Custom type dot1qVlanPortAcceptableFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("admitAll", 1),
          ("admitTagged", 2),
          ("admitUntagged", 3))
    )


_Dot1qVlanPortAcceptableFrameType_Type.__name__ = "Integer32"
_Dot1qVlanPortAcceptableFrameType_Object = MibTableColumn
dot1qVlanPortAcceptableFrameType = _Dot1qVlanPortAcceptableFrameType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 2, 3, 1, 3),
    _Dot1qVlanPortAcceptableFrameType_Type()
)
dot1qVlanPortAcceptableFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qVlanPortAcceptableFrameType.setStatus("current")


class _Dot1qVlanPortIngressChecking_Type(Integer32):
    """Custom type dot1qVlanPortIngressChecking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_Dot1qVlanPortIngressChecking_Type.__name__ = "Integer32"
_Dot1qVlanPortIngressChecking_Object = MibTableColumn
dot1qVlanPortIngressChecking = _Dot1qVlanPortIngressChecking_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 2, 3, 1, 4),
    _Dot1qVlanPortIngressChecking_Type()
)
dot1qVlanPortIngressChecking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qVlanPortIngressChecking.setStatus("current")


class _Dot1qVlanPortNativeVlanStatus_Type(Integer32):
    """Custom type dot1qVlanPortNativeVlanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("tag", 1),
          ("untag", 2))
    )


_Dot1qVlanPortNativeVlanStatus_Type.__name__ = "Integer32"
_Dot1qVlanPortNativeVlanStatus_Object = MibTableColumn
dot1qVlanPortNativeVlanStatus = _Dot1qVlanPortNativeVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 2, 3, 1, 5),
    _Dot1qVlanPortNativeVlanStatus_Type()
)
dot1qVlanPortNativeVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qVlanPortNativeVlanStatus.setStatus("current")
_Dot1qVlanPortNativeVlanId_Type = Integer32
_Dot1qVlanPortNativeVlanId_Object = MibTableColumn
dot1qVlanPortNativeVlanId = _Dot1qVlanPortNativeVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 2, 3, 1, 6),
    _Dot1qVlanPortNativeVlanId_Type()
)
dot1qVlanPortNativeVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qVlanPortNativeVlanId.setStatus("current")
_Dot1qVlanPortTagVlanList_Type = VlanList
_Dot1qVlanPortTagVlanList_Object = MibTableColumn
dot1qVlanPortTagVlanList = _Dot1qVlanPortTagVlanList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 2, 3, 1, 7),
    _Dot1qVlanPortTagVlanList_Type()
)
dot1qVlanPortTagVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qVlanPortTagVlanList.setStatus("current")
_Dot1qVlanPortUntagVlanList_Type = VlanList
_Dot1qVlanPortUntagVlanList_Object = MibTableColumn
dot1qVlanPortUntagVlanList = _Dot1qVlanPortUntagVlanList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 2, 3, 1, 8),
    _Dot1qVlanPortUntagVlanList_Type()
)
dot1qVlanPortUntagVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qVlanPortUntagVlanList.setStatus("current")
_L2STPGroup_ObjectIdentity = ObjectIdentity
l2STPGroup = _L2STPGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3)
)
_StpProtocolSetting_ObjectIdentity = ObjectIdentity
stpProtocolSetting = _StpProtocolSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 1)
)


class _StpStatus_Type(Integer32):
    """Custom type stpStatus based on Integer32"""
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


_StpStatus_Type.__name__ = "Integer32"
_StpStatus_Object = MibScalar
stpStatus = _StpStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 1, 1),
    _StpStatus_Type()
)
stpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpStatus.setStatus("current")


class _StpNewRootTrapState_Type(Integer32):
    """Custom type stpNewRootTrapState based on Integer32"""
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


_StpNewRootTrapState_Type.__name__ = "Integer32"
_StpNewRootTrapState_Object = MibScalar
stpNewRootTrapState = _StpNewRootTrapState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 1, 2),
    _StpNewRootTrapState_Type()
)
stpNewRootTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpNewRootTrapState.setStatus("current")


class _StpTopologyChangeTrapState_Type(Integer32):
    """Custom type stpTopologyChangeTrapState based on Integer32"""
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


_StpTopologyChangeTrapState_Type.__name__ = "Integer32"
_StpTopologyChangeTrapState_Object = MibScalar
stpTopologyChangeTrapState = _StpTopologyChangeTrapState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 1, 3),
    _StpTopologyChangeTrapState_Type()
)
stpTopologyChangeTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpTopologyChangeTrapState.setStatus("current")


class _StpVersion_Type(Integer32):
    """Custom type stpVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mstp", 3),
          ("rstp", 2),
          ("stpCompatible", 0))
    )


_StpVersion_Type.__name__ = "Integer32"
_StpVersion_Object = MibScalar
stpVersion = _StpVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 1, 4),
    _StpVersion_Type()
)
stpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpVersion.setStatus("current")


class _StpBridgePriority_Type(Integer32):
    """Custom type stpBridgePriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_StpBridgePriority_Type.__name__ = "Integer32"
_StpBridgePriority_Object = MibScalar
stpBridgePriority = _StpBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 1, 5),
    _StpBridgePriority_Type()
)
stpBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpBridgePriority.setStatus("current")


class _StpBridgeMaxAge_Type(Timeout):
    """Custom type stpBridgeMaxAge based on Timeout"""
    defaultValue = 2000

    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_StpBridgeMaxAge_Type.__name__ = "Timeout"
_StpBridgeMaxAge_Object = MibScalar
stpBridgeMaxAge = _StpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 1, 6),
    _StpBridgeMaxAge_Type()
)
stpBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpBridgeMaxAge.setStatus("current")


class _StpBridgeHelloTime_Type(Timeout):
    """Custom type stpBridgeHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_StpBridgeHelloTime_Type.__name__ = "Timeout"
_StpBridgeHelloTime_Object = MibScalar
stpBridgeHelloTime = _StpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 1, 7),
    _StpBridgeHelloTime_Type()
)
stpBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpBridgeHelloTime.setStatus("current")


class _StpBridgeForwardDelay_Type(Timeout):
    """Custom type stpBridgeForwardDelay based on Timeout"""
    defaultValue = 1500

    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_StpBridgeForwardDelay_Type.__name__ = "Timeout"
_StpBridgeForwardDelay_Object = MibScalar
stpBridgeForwardDelay = _StpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 1, 8),
    _StpBridgeForwardDelay_Type()
)
stpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpBridgeForwardDelay.setStatus("current")


class _StpMaxHopCount_Type(Integer32):
    """Custom type stpMaxHopCount based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_StpMaxHopCount_Type.__name__ = "Integer32"
_StpMaxHopCount_Object = MibScalar
stpMaxHopCount = _StpMaxHopCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 1, 9),
    _StpMaxHopCount_Type()
)
stpMaxHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpMaxHopCount.setStatus("current")


class _StpTxHoldCount_Type(Integer32):
    """Custom type stpTxHoldCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_StpTxHoldCount_Type.__name__ = "Integer32"
_StpTxHoldCount_Object = MibScalar
stpTxHoldCount = _StpTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 1, 10),
    _StpTxHoldCount_Type()
)
stpTxHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpTxHoldCount.setStatus("current")
_StpPortConfigurationTable_Object = MibTable
stpPortConfigurationTable = _StpPortConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 2)
)
if mibBuilder.loadTexts:
    stpPortConfigurationTable.setStatus("current")
_StpPortConfigurationEntry_Object = MibTableRow
stpPortConfigurationEntry = _StpPortConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 2, 1)
)
stpPortConfigurationEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "stpPort"),
)
if mibBuilder.loadTexts:
    stpPortConfigurationEntry.setStatus("current")


class _StpPort_Type(Integer32):
    """Custom type stpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_StpPort_Type.__name__ = "Integer32"
_StpPort_Object = MibTableColumn
stpPort = _StpPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 2, 1, 1),
    _StpPort_Type()
)
stpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPort.setStatus("current")


class _StpPortAdminPathCost_Type(Integer32):
    """Custom type stpPortAdminPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_StpPortAdminPathCost_Type.__name__ = "Integer32"
_StpPortAdminPathCost_Object = MibTableColumn
stpPortAdminPathCost = _StpPortAdminPathCost_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 2, 1, 2),
    _StpPortAdminPathCost_Type()
)
stpPortAdminPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortAdminPathCost.setStatus("current")


class _StpPortPathCost_Type(Integer32):
    """Custom type stpPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_StpPortPathCost_Type.__name__ = "Integer32"
_StpPortPathCost_Object = MibTableColumn
stpPortPathCost = _StpPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 2, 1, 3),
    _StpPortPathCost_Type()
)
stpPortPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortPathCost.setStatus("current")


class _StpPortState_Type(Integer32):
    """Custom type stpPortState based on Integer32"""
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


_StpPortState_Type.__name__ = "Integer32"
_StpPortState_Object = MibTableColumn
stpPortState = _StpPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 2, 1, 4),
    _StpPortState_Type()
)
stpPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortState.setStatus("current")
_StpPortGuardRoot_Type = TruthValue
_StpPortGuardRoot_Object = MibTableColumn
stpPortGuardRoot = _StpPortGuardRoot_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 2, 1, 5),
    _StpPortGuardRoot_Type()
)
stpPortGuardRoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortGuardRoot.setStatus("current")


class _StpPortLinkType_Type(Integer32):
    """Custom type stpPortLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("p2p", 0),
          ("shared", 1))
    )


_StpPortLinkType_Type.__name__ = "Integer32"
_StpPortLinkType_Object = MibTableColumn
stpPortLinkType = _StpPortLinkType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 2, 1, 6),
    _StpPortLinkType_Type()
)
stpPortLinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortLinkType.setStatus("current")


class _StpPortOperLinkType_Type(Integer32):
    """Custom type stpPortOperLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("p2p", 1),
          ("shared", 2))
    )


_StpPortOperLinkType_Type.__name__ = "Integer32"
_StpPortOperLinkType_Object = MibTableColumn
stpPortOperLinkType = _StpPortOperLinkType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 2, 1, 7),
    _StpPortOperLinkType_Type()
)
stpPortOperLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortOperLinkType.setStatus("current")


class _StpPortFast_Type(Integer32):
    """Custom type stpPortFast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("edge", 0),
          ("network", 2))
    )


_StpPortFast_Type.__name__ = "Integer32"
_StpPortFast_Object = MibTableColumn
stpPortFast = _StpPortFast_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 2, 1, 8),
    _StpPortFast_Type()
)
stpPortFast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortFast.setStatus("current")


class _StpPortOperFast_Type(Integer32):
    """Custom type stpPortOperFast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("edge", 1),
          ("non-edge", 2))
    )


_StpPortOperFast_Type.__name__ = "Integer32"
_StpPortOperFast_Object = MibTableColumn
stpPortOperFast = _StpPortOperFast_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 2, 1, 9),
    _StpPortOperFast_Type()
)
stpPortOperFast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortOperFast.setStatus("current")
_StpPortTCNFilter_Type = TruthValue
_StpPortTCNFilter_Object = MibTableColumn
stpPortTCNFilter = _StpPortTCNFilter_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 2, 1, 10),
    _StpPortTCNFilter_Type()
)
stpPortTCNFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortTCNFilter.setStatus("current")


class _StpPortFowardBPDU_Type(Integer32):
    """Custom type stpPortFowardBPDU based on Integer32"""
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


_StpPortFowardBPDU_Type.__name__ = "Integer32"
_StpPortFowardBPDU_Object = MibTableColumn
stpPortFowardBPDU = _StpPortFowardBPDU_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 2, 1, 11),
    _StpPortFowardBPDU_Type()
)
stpPortFowardBPDU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortFowardBPDU.setStatus("current")


class _StpPortPriority_Type(Integer32):
    """Custom type stpPortPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_StpPortPriority_Type.__name__ = "Integer32"
_StpPortPriority_Object = MibTableColumn
stpPortPriority = _StpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 2, 1, 12),
    _StpPortPriority_Type()
)
stpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortPriority.setStatus("current")


class _StpPortHelloTime_Type(Timeout):
    """Custom type stpPortHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_StpPortHelloTime_Type.__name__ = "Timeout"
_StpPortHelloTime_Object = MibTableColumn
stpPortHelloTime = _StpPortHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 2, 1, 13),
    _StpPortHelloTime_Type()
)
stpPortHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortHelloTime.setStatus("current")
_MstConfiguration_ObjectIdentity = ObjectIdentity
mstConfiguration = _MstConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 3)
)


class _MstiConfigurationName_Type(DisplayString):
    """Custom type mstiConfigurationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MstiConfigurationName_Type.__name__ = "DisplayString"
_MstiConfigurationName_Object = MibScalar
mstiConfigurationName = _MstiConfigurationName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 3, 1),
    _MstiConfigurationName_Type()
)
mstiConfigurationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstiConfigurationName.setStatus("current")


class _MstiRevisionLevel_Type(Integer32):
    """Custom type mstiRevisionLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MstiRevisionLevel_Type.__name__ = "Integer32"
_MstiRevisionLevel_Object = MibScalar
mstiRevisionLevel = _MstiRevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 3, 2),
    _MstiRevisionLevel_Type()
)
mstiRevisionLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstiRevisionLevel.setStatus("current")


class _MstMstiConfigDigest_Type(OctetString):
    """Custom type mstMstiConfigDigest based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MstMstiConfigDigest_Type.__name__ = "OctetString"
_MstMstiConfigDigest_Object = MibScalar
mstMstiConfigDigest = _MstMstiConfigDigest_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 3, 3),
    _MstMstiConfigDigest_Type()
)
mstMstiConfigDigest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstMstiConfigDigest.setStatus("current")
_MstVlanMstiMappingTable_Object = MibTable
mstVlanMstiMappingTable = _MstVlanMstiMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 3, 4)
)
if mibBuilder.loadTexts:
    mstVlanMstiMappingTable.setStatus("current")
_MstVlanMstiMappingEntry_Object = MibTableRow
mstVlanMstiMappingEntry = _MstVlanMstiMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 3, 4, 1)
)
mstVlanMstiMappingEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "mstInstanceIndex"),
)
if mibBuilder.loadTexts:
    mstVlanMstiMappingEntry.setStatus("current")


class _MstInstanceIndex_Type(Integer32):
    """Custom type mstInstanceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_MstInstanceIndex_Type.__name__ = "Integer32"
_MstInstanceIndex_Object = MibTableColumn
mstInstanceIndex = _MstInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 3, 4, 1, 1),
    _MstInstanceIndex_Type()
)
mstInstanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstInstanceIndex.setStatus("current")


class _MstSetVlanList_Type(OctetString):
    """Custom type mstSetVlanList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_MstSetVlanList_Type.__name__ = "OctetString"
_MstSetVlanList_Object = MibTableColumn
mstSetVlanList = _MstSetVlanList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 3, 4, 1, 2),
    _MstSetVlanList_Type()
)
mstSetVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstSetVlanList.setStatus("current")


class _MstResetVlanList_Type(OctetString):
    """Custom type mstResetVlanList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_MstResetVlanList_Type.__name__ = "OctetString"
_MstResetVlanList_Object = MibTableColumn
mstResetVlanList = _MstResetVlanList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 3, 4, 1, 3),
    _MstResetVlanList_Type()
)
mstResetVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstResetVlanList.setStatus("current")


class _MstInstanceVlanMapped_Type(OctetString):
    """Custom type mstInstanceVlanMapped based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstInstanceVlanMapped_Type.__name__ = "OctetString"
_MstInstanceVlanMapped_Object = MibTableColumn
mstInstanceVlanMapped = _MstInstanceVlanMapped_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 3, 4, 1, 4),
    _MstInstanceVlanMapped_Type()
)
mstInstanceVlanMapped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstInstanceVlanMapped.setStatus("current")


class _MstInstanceVlanMapped2k_Type(OctetString):
    """Custom type mstInstanceVlanMapped2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstInstanceVlanMapped2k_Type.__name__ = "OctetString"
_MstInstanceVlanMapped2k_Object = MibTableColumn
mstInstanceVlanMapped2k = _MstInstanceVlanMapped2k_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 3, 4, 1, 5),
    _MstInstanceVlanMapped2k_Type()
)
mstInstanceVlanMapped2k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstInstanceVlanMapped2k.setStatus("current")


class _MstInstanceVlanMapped3k_Type(OctetString):
    """Custom type mstInstanceVlanMapped3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstInstanceVlanMapped3k_Type.__name__ = "OctetString"
_MstInstanceVlanMapped3k_Object = MibTableColumn
mstInstanceVlanMapped3k = _MstInstanceVlanMapped3k_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 3, 4, 1, 6),
    _MstInstanceVlanMapped3k_Type()
)
mstInstanceVlanMapped3k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstInstanceVlanMapped3k.setStatus("current")


class _MstInstanceVlanMapped4k_Type(OctetString):
    """Custom type mstInstanceVlanMapped4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstInstanceVlanMapped4k_Type.__name__ = "OctetString"
_MstInstanceVlanMapped4k_Object = MibTableColumn
mstInstanceVlanMapped4k = _MstInstanceVlanMapped4k_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 3, 4, 1, 7),
    _MstInstanceVlanMapped4k_Type()
)
mstInstanceVlanMapped4k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstInstanceVlanMapped4k.setStatus("current")
_StpInstance_ObjectIdentity = ObjectIdentity
stpInstance = _StpInstance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 4)
)


class _MstCistBridgePriority_Type(Integer32):
    """Custom type mstCistBridgePriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_MstCistBridgePriority_Type.__name__ = "Integer32"
_MstCistBridgePriority_Object = MibScalar
mstCistBridgePriority = _MstCistBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 4, 1),
    _MstCistBridgePriority_Type()
)
mstCistBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstCistBridgePriority.setStatus("current")


class _MstCistStatus_Type(Integer32):
    """Custom type mstCistStatus based on Integer32"""
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


_MstCistStatus_Type.__name__ = "Integer32"
_MstCistStatus_Object = MibScalar
mstCistStatus = _MstCistStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 4, 2),
    _MstCistStatus_Type()
)
mstCistStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstCistStatus.setStatus("current")
_MstCistPortDesignatedRoot_Type = BridgeId
_MstCistPortDesignatedRoot_Object = MibScalar
mstCistPortDesignatedRoot = _MstCistPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 4, 3),
    _MstCistPortDesignatedRoot_Type()
)
mstCistPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstCistPortDesignatedRoot.setStatus("current")
_MstCistRegionalRoot_Type = BridgeId
_MstCistRegionalRoot_Object = MibScalar
mstCistRegionalRoot = _MstCistRegionalRoot_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 4, 4),
    _MstCistRegionalRoot_Type()
)
mstCistRegionalRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstCistRegionalRoot.setStatus("current")
_MstCistPortDesignatedBridge_Type = BridgeId
_MstCistPortDesignatedBridge_Object = MibScalar
mstCistPortDesignatedBridge = _MstCistPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 4, 5),
    _MstCistPortDesignatedBridge_Type()
)
mstCistPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstCistPortDesignatedBridge.setStatus("current")
_MstMstiBridgeTable_Object = MibTable
mstMstiBridgeTable = _MstMstiBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 4, 6)
)
if mibBuilder.loadTexts:
    mstMstiBridgeTable.setStatus("current")
_MstMstiBridgeEntry_Object = MibTableRow
mstMstiBridgeEntry = _MstMstiBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 4, 6, 1)
)
mstMstiBridgeEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "mstMstiInstanceIndex"),
)
if mibBuilder.loadTexts:
    mstMstiBridgeEntry.setStatus("current")


class _MstMstiInstanceIndex_Type(Integer32):
    """Custom type mstMstiInstanceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_MstMstiInstanceIndex_Type.__name__ = "Integer32"
_MstMstiInstanceIndex_Object = MibTableColumn
mstMstiInstanceIndex = _MstMstiInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 4, 6, 1, 1),
    _MstMstiInstanceIndex_Type()
)
mstMstiInstanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstMstiInstanceIndex.setStatus("current")


class _MstMstiBridgePriority_Type(Integer32):
    """Custom type mstMstiBridgePriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_MstMstiBridgePriority_Type.__name__ = "Integer32"
_MstMstiBridgePriority_Object = MibTableColumn
mstMstiBridgePriority = _MstMstiBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 4, 6, 1, 2),
    _MstMstiBridgePriority_Type()
)
mstMstiBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstMstiBridgePriority.setStatus("current")


class _MstMstiStatus_Type(Integer32):
    """Custom type mstMstiStatus based on Integer32"""
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


_MstMstiStatus_Type.__name__ = "Integer32"
_MstMstiStatus_Object = MibTableColumn
mstMstiStatus = _MstMstiStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 4, 6, 1, 3),
    _MstMstiStatus_Type()
)
mstMstiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstMstiStatus.setStatus("current")
_MstMstiPortDesignatedRoot_Type = BridgeId
_MstMstiPortDesignatedRoot_Object = MibTableColumn
mstMstiPortDesignatedRoot = _MstMstiPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 4, 6, 1, 4),
    _MstMstiPortDesignatedRoot_Type()
)
mstMstiPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstMstiPortDesignatedRoot.setStatus("current")
_MstMstiBridgeRegionalRoot_Type = BridgeId
_MstMstiBridgeRegionalRoot_Object = MibTableColumn
mstMstiBridgeRegionalRoot = _MstMstiBridgeRegionalRoot_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 4, 6, 1, 5),
    _MstMstiBridgeRegionalRoot_Type()
)
mstMstiBridgeRegionalRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstMstiBridgeRegionalRoot.setStatus("current")
_MstMstiPortDesignatedBridge_Type = BridgeId
_MstMstiPortDesignatedBridge_Object = MibTableColumn
mstMstiPortDesignatedBridge = _MstMstiPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 4, 6, 1, 6),
    _MstMstiPortDesignatedBridge_Type()
)
mstMstiPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstMstiPortDesignatedBridge.setStatus("current")
_MstMstiTopChanges_Type = Counter32
_MstMstiTopChanges_Object = MibTableColumn
mstMstiTopChanges = _MstMstiTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 4, 6, 1, 7),
    _MstMstiTopChanges_Type()
)
mstMstiTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstMstiTopChanges.setStatus("current")
_StpInstancePortTable_ObjectIdentity = ObjectIdentity
stpInstancePortTable = _StpInstancePortTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 5)
)
_MstCistPortTable_Object = MibTable
mstCistPortTable = _MstCistPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 5, 1)
)
if mibBuilder.loadTexts:
    mstCistPortTable.setStatus("current")
_MstCistPortEntry_Object = MibTableRow
mstCistPortEntry = _MstCistPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 5, 1, 1)
)
mstCistPortEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "mstCistPort"),
)
if mibBuilder.loadTexts:
    mstCistPortEntry.setStatus("current")


class _MstCistPort_Type(Integer32):
    """Custom type mstCistPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MstCistPort_Type.__name__ = "Integer32"
_MstCistPort_Object = MibTableColumn
mstCistPort = _MstCistPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 5, 1, 1, 1),
    _MstCistPort_Type()
)
mstCistPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstCistPort.setStatus("current")


class _MstCistPortAdminPathCost_Type(Integer32):
    """Custom type mstCistPortAdminPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_MstCistPortAdminPathCost_Type.__name__ = "Integer32"
_MstCistPortAdminPathCost_Object = MibTableColumn
mstCistPortAdminPathCost = _MstCistPortAdminPathCost_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 5, 1, 1, 2),
    _MstCistPortAdminPathCost_Type()
)
mstCistPortAdminPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstCistPortAdminPathCost.setStatus("current")


class _MstCistPortPathCost_Type(Integer32):
    """Custom type mstCistPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_MstCistPortPathCost_Type.__name__ = "Integer32"
_MstCistPortPathCost_Object = MibTableColumn
mstCistPortPathCost = _MstCistPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 5, 1, 1, 3),
    _MstCistPortPathCost_Type()
)
mstCistPortPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstCistPortPathCost.setStatus("current")


class _MstCistPortPriority_Type(Integer32):
    """Custom type mstCistPortPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_MstCistPortPriority_Type.__name__ = "Integer32"
_MstCistPortPriority_Object = MibTableColumn
mstCistPortPriority = _MstCistPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 5, 1, 1, 4),
    _MstCistPortPriority_Type()
)
mstCistPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstCistPortPriority.setStatus("current")


class _MstCistPortState_Type(Integer32):
    """Custom type mstCistPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("discarding", 2),
          ("forwarding", 5),
          ("learning", 4))
    )


_MstCistPortState_Type.__name__ = "Integer32"
_MstCistPortState_Object = MibTableColumn
mstCistPortState = _MstCistPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 5, 1, 1, 5),
    _MstCistPortState_Type()
)
mstCistPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstCistPortState.setStatus("current")


class _MstCistCurrentPortRole_Type(Integer32):
    """Custom type mstCistCurrentPortRole based on Integer32"""
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
        *(("alternate", 1),
          ("backup", 2),
          ("designated", 4),
          ("disabled", 0),
          ("master", 5),
          ("root", 3))
    )


_MstCistCurrentPortRole_Type.__name__ = "Integer32"
_MstCistCurrentPortRole_Object = MibTableColumn
mstCistCurrentPortRole = _MstCistCurrentPortRole_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 5, 1, 1, 6),
    _MstCistCurrentPortRole_Type()
)
mstCistCurrentPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstCistCurrentPortRole.setStatus("current")
_MstCistPortProtocolMigration_Type = TruthValue
_MstCistPortProtocolMigration_Object = MibTableColumn
mstCistPortProtocolMigration = _MstCistPortProtocolMigration_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 5, 1, 1, 7),
    _MstCistPortProtocolMigration_Type()
)
mstCistPortProtocolMigration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstCistPortProtocolMigration.setStatus("current")
_MstMstiPortTable_Object = MibTable
mstMstiPortTable = _MstMstiPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 5, 2)
)
if mibBuilder.loadTexts:
    mstMstiPortTable.setStatus("current")
_MstMstiPortEntry_Object = MibTableRow
mstMstiPortEntry = _MstMstiPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 5, 2, 1)
)
mstMstiPortEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "mstMstiPort"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "mstMstiPortInstanceIndex"),
)
if mibBuilder.loadTexts:
    mstMstiPortEntry.setStatus("current")


class _MstMstiPort_Type(Integer32):
    """Custom type mstMstiPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MstMstiPort_Type.__name__ = "Integer32"
_MstMstiPort_Object = MibTableColumn
mstMstiPort = _MstMstiPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 5, 2, 1, 1),
    _MstMstiPort_Type()
)
mstMstiPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstMstiPort.setStatus("current")


class _MstMstiPortInstanceIndex_Type(Integer32):
    """Custom type mstMstiPortInstanceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_MstMstiPortInstanceIndex_Type.__name__ = "Integer32"
_MstMstiPortInstanceIndex_Object = MibTableColumn
mstMstiPortInstanceIndex = _MstMstiPortInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 5, 2, 1, 2),
    _MstMstiPortInstanceIndex_Type()
)
mstMstiPortInstanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstMstiPortInstanceIndex.setStatus("current")


class _MstMstiPortAdminPathCost_Type(Integer32):
    """Custom type mstMstiPortAdminPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_MstMstiPortAdminPathCost_Type.__name__ = "Integer32"
_MstMstiPortAdminPathCost_Object = MibTableColumn
mstMstiPortAdminPathCost = _MstMstiPortAdminPathCost_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 5, 2, 1, 3),
    _MstMstiPortAdminPathCost_Type()
)
mstMstiPortAdminPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstMstiPortAdminPathCost.setStatus("current")


class _MstMstiPortPathCost_Type(Integer32):
    """Custom type mstMstiPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_MstMstiPortPathCost_Type.__name__ = "Integer32"
_MstMstiPortPathCost_Object = MibTableColumn
mstMstiPortPathCost = _MstMstiPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 5, 2, 1, 4),
    _MstMstiPortPathCost_Type()
)
mstMstiPortPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstMstiPortPathCost.setStatus("current")


class _MstMstiPortPriority_Type(Integer32):
    """Custom type mstMstiPortPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_MstMstiPortPriority_Type.__name__ = "Integer32"
_MstMstiPortPriority_Object = MibTableColumn
mstMstiPortPriority = _MstMstiPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 5, 2, 1, 5),
    _MstMstiPortPriority_Type()
)
mstMstiPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstMstiPortPriority.setStatus("current")


class _MstMstiPortState_Type(Integer32):
    """Custom type mstMstiPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("discarding", 2),
          ("forwarding", 5),
          ("learning", 4))
    )


_MstMstiPortState_Type.__name__ = "Integer32"
_MstMstiPortState_Object = MibTableColumn
mstMstiPortState = _MstMstiPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 5, 2, 1, 6),
    _MstMstiPortState_Type()
)
mstMstiPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstMstiPortState.setStatus("current")


class _MstMstiCurrentPortRole_Type(Integer32):
    """Custom type mstMstiCurrentPortRole based on Integer32"""
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
        *(("alternate", 1),
          ("backup", 2),
          ("designated", 4),
          ("disabled", 0),
          ("master", 5),
          ("root", 3))
    )


_MstMstiCurrentPortRole_Type.__name__ = "Integer32"
_MstMstiCurrentPortRole_Object = MibTableColumn
mstMstiCurrentPortRole = _MstMstiCurrentPortRole_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 5, 2, 1, 7),
    _MstMstiCurrentPortRole_Type()
)
mstMstiCurrentPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstMstiCurrentPortRole.setStatus("current")
_StpTraps_ObjectIdentity = ObjectIdentity
stpTraps = _StpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 6)
)
_StpTrapsList_ObjectIdentity = ObjectIdentity
stpTrapsList = _StpTrapsList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 6, 0)
)
_L2LBDGroup_ObjectIdentity = ObjectIdentity
l2LBDGroup = _L2LBDGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 4)
)
_LbdGlobalSettings_ObjectIdentity = ObjectIdentity
lbdGlobalSettings = _LbdGlobalSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 4, 1)
)


class _LbdState_Type(Integer32):
    """Custom type lbdState based on Integer32"""
    defaultValue = 2

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


_LbdState_Type.__name__ = "Integer32"
_LbdState_Object = MibScalar
lbdState = _LbdState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 4, 1, 1),
    _LbdState_Type()
)
lbdState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbdState.setStatus("current")


class _LbdMode_Type(Integer32):
    """Custom type lbdMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port", 1),
          ("vlan", 2))
    )


_LbdMode_Type.__name__ = "Integer32"
_LbdMode_Object = MibScalar
lbdMode = _LbdMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 4, 1, 2),
    _LbdMode_Type()
)
lbdMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbdMode.setStatus("current")
_LbdEnabledVLANIDList_Type = DisplayString
_LbdEnabledVLANIDList_Object = MibScalar
lbdEnabledVLANIDList = _LbdEnabledVLANIDList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 4, 1, 3),
    _LbdEnabledVLANIDList_Type()
)
lbdEnabledVLANIDList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbdEnabledVLANIDList.setStatus("current")


class _LbdInterval_Type(Integer32):
    """Custom type lbdInterval based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_LbdInterval_Type.__name__ = "Integer32"
_LbdInterval_Object = MibScalar
lbdInterval = _LbdInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 4, 1, 4),
    _LbdInterval_Type()
)
lbdInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbdInterval.setStatus("current")


class _LbdTrapState_Type(Integer32):
    """Custom type lbdTrapState based on Integer32"""
    defaultValue = 2

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


_LbdTrapState_Type.__name__ = "Integer32"
_LbdTrapState_Object = MibScalar
lbdTrapState = _LbdTrapState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 4, 1, 5),
    _LbdTrapState_Type()
)
lbdTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbdTrapState.setStatus("current")


class _LbdAction_Type(Integer32):
    """Custom type lbdAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 2),
          ("shutdown", 1))
    )


_LbdAction_Type.__name__ = "Integer32"
_LbdAction_Object = MibScalar
lbdAction = _LbdAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 4, 1, 6),
    _LbdAction_Type()
)
lbdAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbdAction.setStatus("current")
_LbdPortSettings_ObjectIdentity = ObjectIdentity
lbdPortSettings = _LbdPortSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 4, 2)
)
_LbdportTable_Object = MibTable
lbdportTable = _LbdportTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 4, 2, 1)
)
if mibBuilder.loadTexts:
    lbdportTable.setStatus("current")
_LbdportEntry_Object = MibTableRow
lbdportEntry = _LbdportEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 4, 2, 1, 1)
)
lbdportEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lbdportIndex"),
)
if mibBuilder.loadTexts:
    lbdportEntry.setStatus("current")
_LbdportIndex_Type = Integer32
_LbdportIndex_Object = MibTableColumn
lbdportIndex = _LbdportIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 4, 2, 1, 1, 1),
    _LbdportIndex_Type()
)
lbdportIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbdportIndex.setStatus("current")


class _LbdportState_Type(Integer32):
    """Custom type lbdportState based on Integer32"""
    defaultValue = 2

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


_LbdportState_Type.__name__ = "Integer32"
_LbdportState_Object = MibTableColumn
lbdportState = _LbdportState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 4, 2, 1, 1, 2),
    _LbdportState_Type()
)
lbdportState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbdportState.setStatus("current")


class _LbdportResult_Type(Integer32):
    """Custom type lbdportResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("normal", 1))
    )


_LbdportResult_Type.__name__ = "Integer32"
_LbdportResult_Object = MibTableColumn
lbdportResult = _LbdportResult_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 4, 2, 1, 1, 3),
    _LbdportResult_Type()
)
lbdportResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbdportResult.setStatus("current")
_LbdportTimeLeft_Type = SnmpAdminString
_LbdportTimeLeft_Object = MibTableColumn
lbdportTimeLeft = _LbdportTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 4, 2, 1, 1, 4),
    _LbdportTimeLeft_Type()
)
lbdportTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbdportTimeLeft.setStatus("current")
_LbdVlanSettings_ObjectIdentity = ObjectIdentity
lbdVlanSettings = _LbdVlanSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 4, 3)
)
_LbdVlanLoopTable_Object = MibTable
lbdVlanLoopTable = _LbdVlanLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 4, 3, 1)
)
if mibBuilder.loadTexts:
    lbdVlanLoopTable.setStatus("current")
_LbdVlanLoopEntry_Object = MibTableRow
lbdVlanLoopEntry = _LbdVlanLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 4, 3, 1, 1)
)
lbdVlanLoopEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lbdVlanLoopIndex"),
)
if mibBuilder.loadTexts:
    lbdVlanLoopEntry.setStatus("current")
_LbdVlanLoopIndex_Type = Integer32
_LbdVlanLoopIndex_Object = MibTableColumn
lbdVlanLoopIndex = _LbdVlanLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 4, 3, 1, 1, 1),
    _LbdVlanLoopIndex_Type()
)
lbdVlanLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbdVlanLoopIndex.setStatus("current")
_LbdVlanLoopPorts_Type = PortList
_LbdVlanLoopPorts_Object = MibTableColumn
lbdVlanLoopPorts = _LbdVlanLoopPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 4, 3, 1, 1, 2),
    _LbdVlanLoopPorts_Type()
)
lbdVlanLoopPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbdVlanLoopPorts.setStatus("current")
_LbdTraps_ObjectIdentity = ObjectIdentity
lbdTraps = _LbdTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 4, 4)
)
_LbdTrapsList_ObjectIdentity = ObjectIdentity
lbdTrapsList = _LbdTrapsList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 4, 4, 0)
)
_L2LAGroup_ObjectIdentity = ObjectIdentity
l2LAGroup = _L2LAGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 5)
)
_LaSystem_ObjectIdentity = ObjectIdentity
laSystem = _LaSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 5, 1)
)


class _LaSystemPriority_Type(Integer32):
    """Custom type laSystemPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LaSystemPriority_Type.__name__ = "Integer32"
_LaSystemPriority_Object = MibScalar
laSystemPriority = _LaSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 5, 1, 1),
    _LaSystemPriority_Type()
)
laSystemPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laSystemPriority.setStatus("current")


class _LaSystemLoadBalanceAlgorithm_Type(Integer32):
    """Custom type laSystemLoadBalanceAlgorithm based on Integer32"""
    defaultValue = 1

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
        *(("ipDst", 5),
          ("ipSrc", 4),
          ("ipSrcDst", 6),
          ("macDst", 2),
          ("macSrc", 1),
          ("macSrcDst", 3))
    )


_LaSystemLoadBalanceAlgorithm_Type.__name__ = "Integer32"
_LaSystemLoadBalanceAlgorithm_Object = MibScalar
laSystemLoadBalanceAlgorithm = _LaSystemLoadBalanceAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 5, 1, 2),
    _LaSystemLoadBalanceAlgorithm_Type()
)
laSystemLoadBalanceAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laSystemLoadBalanceAlgorithm.setStatus("current")
_LaActorSystemID_Type = MacAddress
_LaActorSystemID_Object = MibScalar
laActorSystemID = _LaActorSystemID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 5, 1, 3),
    _LaActorSystemID_Type()
)
laActorSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laActorSystemID.setStatus("current")
_LaChannel_ObjectIdentity = ObjectIdentity
laChannel = _LaChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 5, 2)
)
_LaPortChannelTable_Object = MibTable
laPortChannelTable = _LaPortChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 5, 2, 1)
)
if mibBuilder.loadTexts:
    laPortChannelTable.setStatus("current")
_LaPortChannelEntry_Object = MibTableRow
laPortChannelEntry = _LaPortChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 5, 2, 1, 1)
)
laPortChannelEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "laPortChannelIfIndex"),
)
if mibBuilder.loadTexts:
    laPortChannelEntry.setStatus("current")
_LaPortChannelIfIndex_Type = InterfaceIndex
_LaPortChannelIfIndex_Object = MibTableColumn
laPortChannelIfIndex = _LaPortChannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 5, 2, 1, 1, 1),
    _LaPortChannelIfIndex_Type()
)
laPortChannelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laPortChannelIfIndex.setStatus("current")


class _LaPortChannelMaxPorts_Type(Integer32):
    """Custom type laPortChannelMaxPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LaPortChannelMaxPorts_Type.__name__ = "Integer32"
_LaPortChannelMaxPorts_Object = MibTableColumn
laPortChannelMaxPorts = _LaPortChannelMaxPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 5, 2, 1, 1, 2),
    _LaPortChannelMaxPorts_Type()
)
laPortChannelMaxPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laPortChannelMaxPorts.setStatus("current")


class _LaPortChannelMemberNumber_Type(Integer32):
    """Custom type laPortChannelMemberNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LaPortChannelMemberNumber_Type.__name__ = "Integer32"
_LaPortChannelMemberNumber_Object = MibTableColumn
laPortChannelMemberNumber = _LaPortChannelMemberNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 5, 2, 1, 1, 3),
    _LaPortChannelMemberNumber_Type()
)
laPortChannelMemberNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laPortChannelMemberNumber.setStatus("current")
_LaPortChannelMemberList_Type = PortList
_LaPortChannelMemberList_Object = MibTableColumn
laPortChannelMemberList = _LaPortChannelMemberList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 5, 2, 1, 1, 4),
    _LaPortChannelMemberList_Type()
)
laPortChannelMemberList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laPortChannelMemberList.setStatus("current")


class _LaSystemChannelGroupID_Type(Integer32):
    """Custom type laSystemChannelGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LaSystemChannelGroupID_Type.__name__ = "Integer32"
_LaSystemChannelGroupID_Object = MibTableColumn
laSystemChannelGroupID = _LaSystemChannelGroupID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 5, 2, 1, 1, 5),
    _LaSystemChannelGroupID_Type()
)
laSystemChannelGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laSystemChannelGroupID.setStatus("current")


class _LaPortChannelMode_Type(Integer32):
    """Custom type laPortChannelMode based on Integer32"""
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
        *(("active", 1),
          ("disabled", 4),
          ("on", 3),
          ("passive", 2))
    )


_LaPortChannelMode_Type.__name__ = "Integer32"
_LaPortChannelMode_Object = MibTableColumn
laPortChannelMode = _LaPortChannelMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 5, 2, 1, 1, 6),
    _LaPortChannelMode_Type()
)
laPortChannelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laPortChannelMode.setStatus("current")
_LaChannelDetailTable_Object = MibTable
laChannelDetailTable = _LaChannelDetailTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 5, 2, 2)
)
if mibBuilder.loadTexts:
    laChannelDetailTable.setStatus("current")
_LaChannelDetailEntry_Object = MibTableRow
laChannelDetailEntry = _LaChannelDetailEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 5, 2, 2, 1)
)
laChannelDetailEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "laChannelDetailPort"),
)
if mibBuilder.loadTexts:
    laChannelDetailEntry.setStatus("current")
_LaChannelDetailPort_Type = InterfaceIndex
_LaChannelDetailPort_Object = MibTableColumn
laChannelDetailPort = _LaChannelDetailPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 5, 2, 2, 1, 1),
    _LaChannelDetailPort_Type()
)
laChannelDetailPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laChannelDetailPort.setStatus("current")


class _LaChannelDetailLACPTimeout_Type(Integer32):
    """Custom type laChannelDetailLACPTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("long", 2),
          ("short", 1))
    )


_LaChannelDetailLACPTimeout_Type.__name__ = "Integer32"
_LaChannelDetailLACPTimeout_Object = MibTableColumn
laChannelDetailLACPTimeout = _LaChannelDetailLACPTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 5, 2, 2, 1, 2),
    _LaChannelDetailLACPTimeout_Type()
)
laChannelDetailLACPTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laChannelDetailLACPTimeout.setStatus("current")


class _LaChannelDetailWorkingMode_Type(Integer32):
    """Custom type laChannelDetailWorkingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("passive", 2))
    )


_LaChannelDetailWorkingMode_Type.__name__ = "Integer32"
_LaChannelDetailWorkingMode_Object = MibTableColumn
laChannelDetailWorkingMode = _LaChannelDetailWorkingMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 5, 2, 2, 1, 3),
    _LaChannelDetailWorkingMode_Type()
)
laChannelDetailWorkingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laChannelDetailWorkingMode.setStatus("current")


class _LaChannelDetailLACPState_Type(Integer32):
    """Custom type laChannelDetailLACPState based on Integer32"""
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
        *(("down", 2),
          ("standby", 1),
          ("upInBndl", 0),
          ("upIndividual", 3))
    )


_LaChannelDetailLACPState_Type.__name__ = "Integer32"
_LaChannelDetailLACPState_Object = MibTableColumn
laChannelDetailLACPState = _LaChannelDetailLACPState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 5, 2, 2, 1, 4),
    _LaChannelDetailLACPState_Type()
)
laChannelDetailLACPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laChannelDetailLACPState.setStatus("current")


class _LaChannelDetailPortPriority_Type(Integer32):
    """Custom type laChannelDetailPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LaChannelDetailPortPriority_Type.__name__ = "Integer32"
_LaChannelDetailPortPriority_Object = MibTableColumn
laChannelDetailPortPriority = _LaChannelDetailPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 5, 2, 2, 1, 5),
    _LaChannelDetailPortPriority_Type()
)
laChannelDetailPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laChannelDetailPortPriority.setStatus("current")


class _LaChannelDetailPortNumber_Type(Integer32):
    """Custom type laChannelDetailPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LaChannelDetailPortNumber_Type.__name__ = "Integer32"
_LaChannelDetailPortNumber_Object = MibTableColumn
laChannelDetailPortNumber = _LaChannelDetailPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 5, 2, 2, 1, 6),
    _LaChannelDetailPortNumber_Type()
)
laChannelDetailPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laChannelDetailPortNumber.setStatus("current")
_LaChannelNeighborTable_Object = MibTable
laChannelNeighborTable = _LaChannelNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 5, 2, 3)
)
if mibBuilder.loadTexts:
    laChannelNeighborTable.setStatus("current")
_LaChannelNeighborEntry_Object = MibTableRow
laChannelNeighborEntry = _LaChannelNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 5, 2, 3, 1)
)
laChannelNeighborEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "laChannelNeighborPort"),
)
if mibBuilder.loadTexts:
    laChannelNeighborEntry.setStatus("current")
_LaChannelNeighborPort_Type = InterfaceIndex
_LaChannelNeighborPort_Object = MibTableColumn
laChannelNeighborPort = _LaChannelNeighborPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 5, 2, 3, 1, 1),
    _LaChannelNeighborPort_Type()
)
laChannelNeighborPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laChannelNeighborPort.setStatus("current")
_LaChannelNeighborSystemPriority_Type = Integer32
_LaChannelNeighborSystemPriority_Object = MibTableColumn
laChannelNeighborSystemPriority = _LaChannelNeighborSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 5, 2, 3, 1, 2),
    _LaChannelNeighborSystemPriority_Type()
)
laChannelNeighborSystemPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laChannelNeighborSystemPriority.setStatus("current")
_LaChannelNeighborSystemID_Type = MacAddress
_LaChannelNeighborSystemID_Object = MibTableColumn
laChannelNeighborSystemID = _LaChannelNeighborSystemID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 5, 2, 3, 1, 3),
    _LaChannelNeighborSystemID_Type()
)
laChannelNeighborSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laChannelNeighborSystemID.setStatus("current")


class _LaChannelNeighborPortNo_Type(Integer32):
    """Custom type laChannelNeighborPortNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LaChannelNeighborPortNo_Type.__name__ = "Integer32"
_LaChannelNeighborPortNo_Object = MibTableColumn
laChannelNeighborPortNo = _LaChannelNeighborPortNo_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 5, 2, 3, 1, 4),
    _LaChannelNeighborPortNo_Type()
)
laChannelNeighborPortNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laChannelNeighborPortNo.setStatus("current")


class _LaChannelNeighborLACPTimeout_Type(Integer32):
    """Custom type laChannelNeighborLACPTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("long", 2),
          ("short", 1))
    )


_LaChannelNeighborLACPTimeout_Type.__name__ = "Integer32"
_LaChannelNeighborLACPTimeout_Object = MibTableColumn
laChannelNeighborLACPTimeout = _LaChannelNeighborLACPTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 5, 2, 3, 1, 5),
    _LaChannelNeighborLACPTimeout_Type()
)
laChannelNeighborLACPTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laChannelNeighborLACPTimeout.setStatus("current")


class _LaChannelNeighborWorkingMode_Type(Integer32):
    """Custom type laChannelNeighborWorkingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("passive", 2))
    )


_LaChannelNeighborWorkingMode_Type.__name__ = "Integer32"
_LaChannelNeighborWorkingMode_Object = MibTableColumn
laChannelNeighborWorkingMode = _LaChannelNeighborWorkingMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 5, 2, 3, 1, 6),
    _LaChannelNeighborWorkingMode_Type()
)
laChannelNeighborWorkingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laChannelNeighborWorkingMode.setStatus("current")


class _LaChannelNeighborPortPriority_Type(Integer32):
    """Custom type laChannelNeighborPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LaChannelNeighborPortPriority_Type.__name__ = "Integer32"
_LaChannelNeighborPortPriority_Object = MibTableColumn
laChannelNeighborPortPriority = _LaChannelNeighborPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 5, 2, 3, 1, 7),
    _LaChannelNeighborPortPriority_Type()
)
laChannelNeighborPortPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laChannelNeighborPortPriority.setStatus("current")
_L2MulticastCtrlGroup_ObjectIdentity = ObjectIdentity
l2MulticastCtrlGroup = _L2MulticastCtrlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6)
)
_IgsSystem_ObjectIdentity = ObjectIdentity
igsSystem = _IgsSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 1)
)


class _IgsStatus_Type(Integer32):
    """Custom type igsStatus based on Integer32"""
    defaultValue = 2

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


_IgsStatus_Type.__name__ = "Integer32"
_IgsStatus_Object = MibScalar
igsStatus = _IgsStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 1, 1),
    _IgsStatus_Type()
)
igsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsStatus.setStatus("current")


class _IgsClearIgmpSnoopByVlanId_Type(VlanIdOrNone):
    """Custom type igsClearIgmpSnoopByVlanId based on VlanIdOrNone"""
    defaultValue = 0


_IgsClearIgmpSnoopByVlanId_Object = MibScalar
igsClearIgmpSnoopByVlanId = _IgsClearIgmpSnoopByVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 1, 3),
    _IgsClearIgmpSnoopByVlanId_Type()
)
igsClearIgmpSnoopByVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsClearIgmpSnoopByVlanId.setStatus("current")
_IgsVlan_ObjectIdentity = ObjectIdentity
igsVlan = _IgsVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 2)
)
_IgsVlanFilterTable_Object = MibTable
igsVlanFilterTable = _IgsVlanFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 2, 1)
)
if mibBuilder.loadTexts:
    igsVlanFilterTable.setStatus("current")
_IgsVlanFilterEntry_Object = MibTableRow
igsVlanFilterEntry = _IgsVlanFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 2, 1, 1)
)
igsVlanFilterEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "igsVlanFilterVlanId"),
)
if mibBuilder.loadTexts:
    igsVlanFilterEntry.setStatus("current")


class _IgsVlanFilterVlanId_Type(Integer32):
    """Custom type igsVlanFilterVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_IgsVlanFilterVlanId_Type.__name__ = "Integer32"
_IgsVlanFilterVlanId_Object = MibTableColumn
igsVlanFilterVlanId = _IgsVlanFilterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 2, 1, 1, 1),
    _IgsVlanFilterVlanId_Type()
)
igsVlanFilterVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanFilterVlanId.setStatus("current")


class _IgsVlanSnoopStatus_Type(Integer32):
    """Custom type igsVlanSnoopStatus based on Integer32"""
    defaultValue = 2

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


_IgsVlanSnoopStatus_Type.__name__ = "Integer32"
_IgsVlanSnoopStatus_Object = MibTableColumn
igsVlanSnoopStatus = _IgsVlanSnoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 2, 1, 1, 2),
    _IgsVlanSnoopStatus_Type()
)
igsVlanSnoopStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsVlanSnoopStatus.setStatus("current")


class _IgsVlanFastLeave_Type(Integer32):
    """Custom type igsVlanFastLeave based on Integer32"""
    defaultValue = 2

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


_IgsVlanFastLeave_Type.__name__ = "Integer32"
_IgsVlanFastLeave_Object = MibTableColumn
igsVlanFastLeave = _IgsVlanFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 2, 1, 1, 4),
    _IgsVlanFastLeave_Type()
)
igsVlanFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsVlanFastLeave.setStatus("current")


class _IgsVlanQuerier_Type(Integer32):
    """Custom type igsVlanQuerier based on Integer32"""
    defaultValue = 2

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


_IgsVlanQuerier_Type.__name__ = "Integer32"
_IgsVlanQuerier_Object = MibTableColumn
igsVlanQuerier = _IgsVlanQuerier_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 2, 1, 1, 7),
    _IgsVlanQuerier_Type()
)
igsVlanQuerier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanQuerier.setStatus("current")


class _IgsVlanCfgQuerier_Type(Integer32):
    """Custom type igsVlanCfgQuerier based on Integer32"""
    defaultValue = 2

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


_IgsVlanCfgQuerier_Type.__name__ = "Integer32"
_IgsVlanCfgQuerier_Object = MibTableColumn
igsVlanCfgQuerier = _IgsVlanCfgQuerier_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 2, 1, 1, 8),
    _IgsVlanCfgQuerier_Type()
)
igsVlanCfgQuerier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsVlanCfgQuerier.setStatus("current")


class _IgsVlanQuerierVersion_Type(Integer32):
    """Custom type igsVlanQuerierVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2", 2),
          ("v3", 3))
    )


_IgsVlanQuerierVersion_Type.__name__ = "Integer32"
_IgsVlanQuerierVersion_Object = MibTableColumn
igsVlanQuerierVersion = _IgsVlanQuerierVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 2, 1, 1, 9),
    _IgsVlanQuerierVersion_Type()
)
igsVlanQuerierVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsVlanQuerierVersion.setStatus("current")


class _IgsVlanQueryInterval_Type(Integer32):
    """Custom type igsVlanQueryInterval based on Integer32"""
    defaultValue = 125

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31744),
    )


_IgsVlanQueryInterval_Type.__name__ = "Integer32"
_IgsVlanQueryInterval_Object = MibTableColumn
igsVlanQueryInterval = _IgsVlanQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 2, 1, 1, 10),
    _IgsVlanQueryInterval_Type()
)
igsVlanQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsVlanQueryInterval.setStatus("current")


class _IgsVlanMaxResponseTime_Type(Integer32):
    """Custom type igsVlanMaxResponseTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_IgsVlanMaxResponseTime_Type.__name__ = "Integer32"
_IgsVlanMaxResponseTime_Object = MibTableColumn
igsVlanMaxResponseTime = _IgsVlanMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 2, 1, 1, 11),
    _IgsVlanMaxResponseTime_Type()
)
igsVlanMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsVlanMaxResponseTime.setStatus("current")


class _IgsVlanRobustnessValue_Type(Integer32):
    """Custom type igsVlanRobustnessValue based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_IgsVlanRobustnessValue_Type.__name__ = "Integer32"
_IgsVlanRobustnessValue_Object = MibTableColumn
igsVlanRobustnessValue = _IgsVlanRobustnessValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 2, 1, 1, 12),
    _IgsVlanRobustnessValue_Type()
)
igsVlanRobustnessValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsVlanRobustnessValue.setStatus("current")


class _IgsVlanLastMemberQueryInterval_Type(Integer32):
    """Custom type igsVlanLastMemberQueryInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_IgsVlanLastMemberQueryInterval_Type.__name__ = "Integer32"
_IgsVlanLastMemberQueryInterval_Object = MibTableColumn
igsVlanLastMemberQueryInterval = _IgsVlanLastMemberQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 2, 1, 1, 13),
    _IgsVlanLastMemberQueryInterval_Type()
)
igsVlanLastMemberQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsVlanLastMemberQueryInterval.setStatus("current")
_IgsVlanMulticastGroupTable_Object = MibTable
igsVlanMulticastGroupTable = _IgsVlanMulticastGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 2, 2)
)
if mibBuilder.loadTexts:
    igsVlanMulticastGroupTable.setStatus("current")
_IgsVlanMulticastGroupEntry_Object = MibTableRow
igsVlanMulticastGroupEntry = _IgsVlanMulticastGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 2, 2, 1)
)
igsVlanMulticastGroupEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "igsVlanMulticastGroupVlanId"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "igsVlanMulticastGroupIpAddress"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "igsVlanMulticastGroupReceiverPortIndex"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "igsVlanMulticastGroupReceiverSrcAddr"),
)
if mibBuilder.loadTexts:
    igsVlanMulticastGroupEntry.setStatus("current")


class _IgsVlanMulticastGroupVlanId_Type(Integer32):
    """Custom type igsVlanMulticastGroupVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_IgsVlanMulticastGroupVlanId_Type.__name__ = "Integer32"
_IgsVlanMulticastGroupVlanId_Object = MibTableColumn
igsVlanMulticastGroupVlanId = _IgsVlanMulticastGroupVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 2, 2, 1, 1),
    _IgsVlanMulticastGroupVlanId_Type()
)
igsVlanMulticastGroupVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanMulticastGroupVlanId.setStatus("current")
_IgsVlanMulticastGroupIpAddress_Type = IpAddress
_IgsVlanMulticastGroupIpAddress_Object = MibTableColumn
igsVlanMulticastGroupIpAddress = _IgsVlanMulticastGroupIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 2, 2, 1, 2),
    _IgsVlanMulticastGroupIpAddress_Type()
)
igsVlanMulticastGroupIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanMulticastGroupIpAddress.setStatus("current")
_IgsVlanMulticastGroupReceiverPortIndex_Type = InterfaceIndex
_IgsVlanMulticastGroupReceiverPortIndex_Object = MibTableColumn
igsVlanMulticastGroupReceiverPortIndex = _IgsVlanMulticastGroupReceiverPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 2, 2, 1, 3),
    _IgsVlanMulticastGroupReceiverPortIndex_Type()
)
igsVlanMulticastGroupReceiverPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanMulticastGroupReceiverPortIndex.setStatus("current")
_IgsVlanMulticastGroupReceiverSrcAddr_Type = IpAddress
_IgsVlanMulticastGroupReceiverSrcAddr_Object = MibTableColumn
igsVlanMulticastGroupReceiverSrcAddr = _IgsVlanMulticastGroupReceiverSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 2, 2, 1, 4),
    _IgsVlanMulticastGroupReceiverSrcAddr_Type()
)
igsVlanMulticastGroupReceiverSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanMulticastGroupReceiverSrcAddr.setStatus("current")
_IgsVlanMulticastGroupMacAddress_Type = MacAddress
_IgsVlanMulticastGroupMacAddress_Object = MibTableColumn
igsVlanMulticastGroupMacAddress = _IgsVlanMulticastGroupMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 2, 2, 1, 5),
    _IgsVlanMulticastGroupMacAddress_Type()
)
igsVlanMulticastGroupMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanMulticastGroupMacAddress.setStatus("current")
_IgsVlanMulticastGroupExp_Type = TimeTicks
_IgsVlanMulticastGroupExp_Object = MibTableColumn
igsVlanMulticastGroupExp = _IgsVlanMulticastGroupExp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 2, 2, 1, 7),
    _IgsVlanMulticastGroupExp_Type()
)
igsVlanMulticastGroupExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanMulticastGroupExp.setStatus("current")
_IgsVlanMulticastGroupPortList_Type = PortList
_IgsVlanMulticastGroupPortList_Object = MibTableColumn
igsVlanMulticastGroupPortList = _IgsVlanMulticastGroupPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 2, 2, 1, 8),
    _IgsVlanMulticastGroupPortList_Type()
)
igsVlanMulticastGroupPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanMulticastGroupPortList.setStatus("current")
_IgsVlanStaticMcastGrpTable_Object = MibTable
igsVlanStaticMcastGrpTable = _IgsVlanStaticMcastGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 2, 3)
)
if mibBuilder.loadTexts:
    igsVlanStaticMcastGrpTable.setStatus("current")
_IgsVlanStaticMcastGrpEntry_Object = MibTableRow
igsVlanStaticMcastGrpEntry = _IgsVlanStaticMcastGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 2, 3, 1)
)
igsVlanStaticMcastGrpEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "igsVlanStaticMcastGrpVlanId"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "igsVlanStaticMcastGrpGroupAddress"),
)
if mibBuilder.loadTexts:
    igsVlanStaticMcastGrpEntry.setStatus("current")


class _IgsVlanStaticMcastGrpVlanId_Type(Integer32):
    """Custom type igsVlanStaticMcastGrpVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_IgsVlanStaticMcastGrpVlanId_Type.__name__ = "Integer32"
_IgsVlanStaticMcastGrpVlanId_Object = MibTableColumn
igsVlanStaticMcastGrpVlanId = _IgsVlanStaticMcastGrpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 2, 3, 1, 1),
    _IgsVlanStaticMcastGrpVlanId_Type()
)
igsVlanStaticMcastGrpVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanStaticMcastGrpVlanId.setStatus("current")
_IgsVlanStaticMcastGrpGroupAddress_Type = InetAddress
_IgsVlanStaticMcastGrpGroupAddress_Object = MibTableColumn
igsVlanStaticMcastGrpGroupAddress = _IgsVlanStaticMcastGrpGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 2, 3, 1, 2),
    _IgsVlanStaticMcastGrpGroupAddress_Type()
)
igsVlanStaticMcastGrpGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanStaticMcastGrpGroupAddress.setStatus("current")
_IgsVlanStaticMcastGrpPortList_Type = PortList
_IgsVlanStaticMcastGrpPortList_Object = MibTableColumn
igsVlanStaticMcastGrpPortList = _IgsVlanStaticMcastGrpPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 2, 3, 1, 3),
    _IgsVlanStaticMcastGrpPortList_Type()
)
igsVlanStaticMcastGrpPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsVlanStaticMcastGrpPortList.setStatus("current")
_IgsVlanStaticMcastGrpRowStatus_Type = RowStatus
_IgsVlanStaticMcastGrpRowStatus_Object = MibTableColumn
igsVlanStaticMcastGrpRowStatus = _IgsVlanStaticMcastGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 2, 3, 1, 4),
    _IgsVlanStaticMcastGrpRowStatus_Type()
)
igsVlanStaticMcastGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igsVlanStaticMcastGrpRowStatus.setStatus("current")
_IgsVlanRouterTable_Object = MibTable
igsVlanRouterTable = _IgsVlanRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 2, 4)
)
if mibBuilder.loadTexts:
    igsVlanRouterTable.setStatus("current")
_IgsVlanRouterEntry_Object = MibTableRow
igsVlanRouterEntry = _IgsVlanRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 2, 4, 1)
)
igsVlanRouterEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "igsVlanRouterVlanId"),
)
if mibBuilder.loadTexts:
    igsVlanRouterEntry.setStatus("current")


class _IgsVlanRouterVlanId_Type(Integer32):
    """Custom type igsVlanRouterVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_IgsVlanRouterVlanId_Type.__name__ = "Integer32"
_IgsVlanRouterVlanId_Object = MibTableColumn
igsVlanRouterVlanId = _IgsVlanRouterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 2, 4, 1, 1),
    _IgsVlanRouterVlanId_Type()
)
igsVlanRouterVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanRouterVlanId.setStatus("current")
_IgsVlanRouterStaticPortList_Type = PortList
_IgsVlanRouterStaticPortList_Object = MibTableColumn
igsVlanRouterStaticPortList = _IgsVlanRouterStaticPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 2, 4, 1, 2),
    _IgsVlanRouterStaticPortList_Type()
)
igsVlanRouterStaticPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsVlanRouterStaticPortList.setStatus("current")
_IgsVlanRouterBlockPortList_Type = PortList
_IgsVlanRouterBlockPortList_Object = MibTableColumn
igsVlanRouterBlockPortList = _IgsVlanRouterBlockPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 2, 4, 1, 3),
    _IgsVlanRouterBlockPortList_Type()
)
igsVlanRouterBlockPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsVlanRouterBlockPortList.setStatus("current")
_IgsVlanRouterDynamicPortList_Type = PortList
_IgsVlanRouterDynamicPortList_Object = MibTableColumn
igsVlanRouterDynamicPortList = _IgsVlanRouterDynamicPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 2, 4, 1, 4),
    _IgsVlanRouterDynamicPortList_Type()
)
igsVlanRouterDynamicPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanRouterDynamicPortList.setStatus("current")
_IgsStats_ObjectIdentity = ObjectIdentity
igsStats = _IgsStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 3)
)
_IgsStatsTable_Object = MibTable
igsStatsTable = _IgsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 3, 1)
)
if mibBuilder.loadTexts:
    igsStatsTable.setStatus("current")
_IgsStatsEntry_Object = MibTableRow
igsStatsEntry = _IgsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 3, 1, 1)
)
igsStatsEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "igsStatsVlanId"),
)
if mibBuilder.loadTexts:
    igsStatsEntry.setStatus("current")


class _IgsStatsVlanId_Type(Integer32):
    """Custom type igsStatsVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_IgsStatsVlanId_Type.__name__ = "Integer32"
_IgsStatsVlanId_Object = MibTableColumn
igsStatsVlanId = _IgsStatsVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 3, 1, 1, 1),
    _IgsStatsVlanId_Type()
)
igsStatsVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsStatsVlanId.setStatus("current")
_IgsStatsIGMPv1RxReport_Type = Counter32
_IgsStatsIGMPv1RxReport_Object = MibTableColumn
igsStatsIGMPv1RxReport = _IgsStatsIGMPv1RxReport_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 3, 1, 1, 2),
    _IgsStatsIGMPv1RxReport_Type()
)
igsStatsIGMPv1RxReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsStatsIGMPv1RxReport.setStatus("current")
_IgsStatsIGMPv1RxQueries_Type = Counter32
_IgsStatsIGMPv1RxQueries_Object = MibTableColumn
igsStatsIGMPv1RxQueries = _IgsStatsIGMPv1RxQueries_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 3, 1, 1, 3),
    _IgsStatsIGMPv1RxQueries_Type()
)
igsStatsIGMPv1RxQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsStatsIGMPv1RxQueries.setStatus("current")
_IgsStatsIGMPv1TxReport_Type = Counter32
_IgsStatsIGMPv1TxReport_Object = MibTableColumn
igsStatsIGMPv1TxReport = _IgsStatsIGMPv1TxReport_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 3, 1, 1, 4),
    _IgsStatsIGMPv1TxReport_Type()
)
igsStatsIGMPv1TxReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsStatsIGMPv1TxReport.setStatus("current")
_IgsStatsIGMPv1TxQueries_Type = Counter32
_IgsStatsIGMPv1TxQueries_Object = MibTableColumn
igsStatsIGMPv1TxQueries = _IgsStatsIGMPv1TxQueries_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 3, 1, 1, 5),
    _IgsStatsIGMPv1TxQueries_Type()
)
igsStatsIGMPv1TxQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsStatsIGMPv1TxQueries.setStatus("current")
_IgsStatsIGMPv2RxReport_Type = Counter32
_IgsStatsIGMPv2RxReport_Object = MibTableColumn
igsStatsIGMPv2RxReport = _IgsStatsIGMPv2RxReport_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 3, 1, 1, 6),
    _IgsStatsIGMPv2RxReport_Type()
)
igsStatsIGMPv2RxReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsStatsIGMPv2RxReport.setStatus("current")
_IgsStatsIGMPv2RxQueries_Type = Counter32
_IgsStatsIGMPv2RxQueries_Object = MibTableColumn
igsStatsIGMPv2RxQueries = _IgsStatsIGMPv2RxQueries_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 3, 1, 1, 7),
    _IgsStatsIGMPv2RxQueries_Type()
)
igsStatsIGMPv2RxQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsStatsIGMPv2RxQueries.setStatus("current")
_IgsStatsIGMPv2RxLeave_Type = Counter32
_IgsStatsIGMPv2RxLeave_Object = MibTableColumn
igsStatsIGMPv2RxLeave = _IgsStatsIGMPv2RxLeave_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 3, 1, 1, 8),
    _IgsStatsIGMPv2RxLeave_Type()
)
igsStatsIGMPv2RxLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsStatsIGMPv2RxLeave.setStatus("current")
_IgsStatsIGMPv2TxReport_Type = Counter32
_IgsStatsIGMPv2TxReport_Object = MibTableColumn
igsStatsIGMPv2TxReport = _IgsStatsIGMPv2TxReport_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 3, 1, 1, 9),
    _IgsStatsIGMPv2TxReport_Type()
)
igsStatsIGMPv2TxReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsStatsIGMPv2TxReport.setStatus("current")
_IgsStatsIGMPv2TxQueries_Type = Counter32
_IgsStatsIGMPv2TxQueries_Object = MibTableColumn
igsStatsIGMPv2TxQueries = _IgsStatsIGMPv2TxQueries_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 3, 1, 1, 10),
    _IgsStatsIGMPv2TxQueries_Type()
)
igsStatsIGMPv2TxQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsStatsIGMPv2TxQueries.setStatus("current")
_IgsStatsIGMPv2TxLeave_Type = Counter32
_IgsStatsIGMPv2TxLeave_Object = MibTableColumn
igsStatsIGMPv2TxLeave = _IgsStatsIGMPv2TxLeave_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 3, 1, 1, 11),
    _IgsStatsIGMPv2TxLeave_Type()
)
igsStatsIGMPv2TxLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsStatsIGMPv2TxLeave.setStatus("current")
_IgsStatsIGMPv3RxReport_Type = Counter32
_IgsStatsIGMPv3RxReport_Object = MibTableColumn
igsStatsIGMPv3RxReport = _IgsStatsIGMPv3RxReport_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 3, 1, 1, 12),
    _IgsStatsIGMPv3RxReport_Type()
)
igsStatsIGMPv3RxReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsStatsIGMPv3RxReport.setStatus("current")
_IgsStatsIGMPv3RxQueries_Type = Counter32
_IgsStatsIGMPv3RxQueries_Object = MibTableColumn
igsStatsIGMPv3RxQueries = _IgsStatsIGMPv3RxQueries_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 3, 1, 1, 13),
    _IgsStatsIGMPv3RxQueries_Type()
)
igsStatsIGMPv3RxQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsStatsIGMPv3RxQueries.setStatus("current")
_IgsStatsIGMPv3TxReport_Type = Counter32
_IgsStatsIGMPv3TxReport_Object = MibTableColumn
igsStatsIGMPv3TxReport = _IgsStatsIGMPv3TxReport_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 3, 1, 1, 14),
    _IgsStatsIGMPv3TxReport_Type()
)
igsStatsIGMPv3TxReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsStatsIGMPv3TxReport.setStatus("current")
_IgsStatsIGMPv3TxQueries_Type = Counter32
_IgsStatsIGMPv3TxQueries_Object = MibTableColumn
igsStatsIGMPv3TxQueries = _IgsStatsIGMPv3TxQueries_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 3, 1, 1, 15),
    _IgsStatsIGMPv3TxQueries_Type()
)
igsStatsIGMPv3TxQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsStatsIGMPv3TxQueries.setStatus("current")
_MldSystem_ObjectIdentity = ObjectIdentity
mldSystem = _MldSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 4)
)


class _MldStatus_Type(Integer32):
    """Custom type mldStatus based on Integer32"""
    defaultValue = 2

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


_MldStatus_Type.__name__ = "Integer32"
_MldStatus_Object = MibScalar
mldStatus = _MldStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 4, 1),
    _MldStatus_Type()
)
mldStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldStatus.setStatus("current")


class _MldClearIgmpSnoopByVlanId_Type(VlanIdOrNone):
    """Custom type mldClearIgmpSnoopByVlanId based on VlanIdOrNone"""
    defaultValue = 0


_MldClearIgmpSnoopByVlanId_Object = MibScalar
mldClearIgmpSnoopByVlanId = _MldClearIgmpSnoopByVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 4, 3),
    _MldClearIgmpSnoopByVlanId_Type()
)
mldClearIgmpSnoopByVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldClearIgmpSnoopByVlanId.setStatus("current")
_MldVlan_ObjectIdentity = ObjectIdentity
mldVlan = _MldVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 5)
)
_MldVlanFilterTable_Object = MibTable
mldVlanFilterTable = _MldVlanFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 5, 1)
)
if mibBuilder.loadTexts:
    mldVlanFilterTable.setStatus("current")
_MldVlanFilterEntry_Object = MibTableRow
mldVlanFilterEntry = _MldVlanFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 5, 1, 1)
)
mldVlanFilterEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "mldVlanFilterVlanId"),
)
if mibBuilder.loadTexts:
    mldVlanFilterEntry.setStatus("current")


class _MldVlanFilterVlanId_Type(Integer32):
    """Custom type mldVlanFilterVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MldVlanFilterVlanId_Type.__name__ = "Integer32"
_MldVlanFilterVlanId_Object = MibTableColumn
mldVlanFilterVlanId = _MldVlanFilterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 5, 1, 1, 1),
    _MldVlanFilterVlanId_Type()
)
mldVlanFilterVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldVlanFilterVlanId.setStatus("current")


class _MldVlanSnoopStatus_Type(Integer32):
    """Custom type mldVlanSnoopStatus based on Integer32"""
    defaultValue = 2

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


_MldVlanSnoopStatus_Type.__name__ = "Integer32"
_MldVlanSnoopStatus_Object = MibTableColumn
mldVlanSnoopStatus = _MldVlanSnoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 5, 1, 1, 2),
    _MldVlanSnoopStatus_Type()
)
mldVlanSnoopStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldVlanSnoopStatus.setStatus("current")


class _MldVlanFastLeave_Type(Integer32):
    """Custom type mldVlanFastLeave based on Integer32"""
    defaultValue = 2

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


_MldVlanFastLeave_Type.__name__ = "Integer32"
_MldVlanFastLeave_Object = MibTableColumn
mldVlanFastLeave = _MldVlanFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 5, 1, 1, 4),
    _MldVlanFastLeave_Type()
)
mldVlanFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldVlanFastLeave.setStatus("current")


class _MldVlanQuerier_Type(Integer32):
    """Custom type mldVlanQuerier based on Integer32"""
    defaultValue = 2

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


_MldVlanQuerier_Type.__name__ = "Integer32"
_MldVlanQuerier_Object = MibTableColumn
mldVlanQuerier = _MldVlanQuerier_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 5, 1, 1, 7),
    _MldVlanQuerier_Type()
)
mldVlanQuerier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldVlanQuerier.setStatus("current")


class _MldVlanCfgQuerier_Type(Integer32):
    """Custom type mldVlanCfgQuerier based on Integer32"""
    defaultValue = 2

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


_MldVlanCfgQuerier_Type.__name__ = "Integer32"
_MldVlanCfgQuerier_Object = MibTableColumn
mldVlanCfgQuerier = _MldVlanCfgQuerier_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 5, 1, 1, 8),
    _MldVlanCfgQuerier_Type()
)
mldVlanCfgQuerier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldVlanCfgQuerier.setStatus("current")


class _MldVlanQuerierVersion_Type(Integer32):
    """Custom type mldVlanQuerierVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2", 2),
          ("v3", 3))
    )


_MldVlanQuerierVersion_Type.__name__ = "Integer32"
_MldVlanQuerierVersion_Object = MibTableColumn
mldVlanQuerierVersion = _MldVlanQuerierVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 5, 1, 1, 9),
    _MldVlanQuerierVersion_Type()
)
mldVlanQuerierVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldVlanQuerierVersion.setStatus("current")


class _MldVlanQueryInterval_Type(Integer32):
    """Custom type mldVlanQueryInterval based on Integer32"""
    defaultValue = 125

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31744),
    )


_MldVlanQueryInterval_Type.__name__ = "Integer32"
_MldVlanQueryInterval_Object = MibTableColumn
mldVlanQueryInterval = _MldVlanQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 5, 1, 1, 10),
    _MldVlanQueryInterval_Type()
)
mldVlanQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldVlanQueryInterval.setStatus("current")


class _MldVlanMaxResponseTime_Type(Integer32):
    """Custom type mldVlanMaxResponseTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_MldVlanMaxResponseTime_Type.__name__ = "Integer32"
_MldVlanMaxResponseTime_Object = MibTableColumn
mldVlanMaxResponseTime = _MldVlanMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 5, 1, 1, 11),
    _MldVlanMaxResponseTime_Type()
)
mldVlanMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldVlanMaxResponseTime.setStatus("current")


class _MldVlanRobustnessValue_Type(Integer32):
    """Custom type mldVlanRobustnessValue based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_MldVlanRobustnessValue_Type.__name__ = "Integer32"
_MldVlanRobustnessValue_Object = MibTableColumn
mldVlanRobustnessValue = _MldVlanRobustnessValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 5, 1, 1, 12),
    _MldVlanRobustnessValue_Type()
)
mldVlanRobustnessValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldVlanRobustnessValue.setStatus("current")


class _MldVlanLastListenerQueryInterval_Type(Integer32):
    """Custom type mldVlanLastListenerQueryInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_MldVlanLastListenerQueryInterval_Type.__name__ = "Integer32"
_MldVlanLastListenerQueryInterval_Object = MibTableColumn
mldVlanLastListenerQueryInterval = _MldVlanLastListenerQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 5, 1, 1, 13),
    _MldVlanLastListenerQueryInterval_Type()
)
mldVlanLastListenerQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldVlanLastListenerQueryInterval.setStatus("current")
_MldVlanMulticastGroupTable_Object = MibTable
mldVlanMulticastGroupTable = _MldVlanMulticastGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 5, 2)
)
if mibBuilder.loadTexts:
    mldVlanMulticastGroupTable.setStatus("current")
_MldVlanMulticastGroupEntry_Object = MibTableRow
mldVlanMulticastGroupEntry = _MldVlanMulticastGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 5, 2, 1)
)
mldVlanMulticastGroupEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "mldVlanMulticastGroupVlanId"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "mldVlanMulticastGroupIpAddress"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "mldVlanMulticastGroupReceiverPortIndex"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "mldVlanMulticastGroupReceiverSrcAddr"),
)
if mibBuilder.loadTexts:
    mldVlanMulticastGroupEntry.setStatus("current")


class _MldVlanMulticastGroupVlanId_Type(Integer32):
    """Custom type mldVlanMulticastGroupVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MldVlanMulticastGroupVlanId_Type.__name__ = "Integer32"
_MldVlanMulticastGroupVlanId_Object = MibTableColumn
mldVlanMulticastGroupVlanId = _MldVlanMulticastGroupVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 5, 2, 1, 1),
    _MldVlanMulticastGroupVlanId_Type()
)
mldVlanMulticastGroupVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldVlanMulticastGroupVlanId.setStatus("current")
_MldVlanMulticastGroupIpAddress_Type = Ipv6Address
_MldVlanMulticastGroupIpAddress_Object = MibTableColumn
mldVlanMulticastGroupIpAddress = _MldVlanMulticastGroupIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 5, 2, 1, 2),
    _MldVlanMulticastGroupIpAddress_Type()
)
mldVlanMulticastGroupIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldVlanMulticastGroupIpAddress.setStatus("current")
_MldVlanMulticastGroupReceiverPortIndex_Type = InterfaceIndex
_MldVlanMulticastGroupReceiverPortIndex_Object = MibTableColumn
mldVlanMulticastGroupReceiverPortIndex = _MldVlanMulticastGroupReceiverPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 5, 2, 1, 3),
    _MldVlanMulticastGroupReceiverPortIndex_Type()
)
mldVlanMulticastGroupReceiverPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldVlanMulticastGroupReceiverPortIndex.setStatus("current")
_MldVlanMulticastGroupReceiverSrcAddr_Type = Ipv6Address
_MldVlanMulticastGroupReceiverSrcAddr_Object = MibTableColumn
mldVlanMulticastGroupReceiverSrcAddr = _MldVlanMulticastGroupReceiverSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 5, 2, 1, 4),
    _MldVlanMulticastGroupReceiverSrcAddr_Type()
)
mldVlanMulticastGroupReceiverSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldVlanMulticastGroupReceiverSrcAddr.setStatus("current")
_MldVlanMulticastGroupMacAddress_Type = MacAddress
_MldVlanMulticastGroupMacAddress_Object = MibTableColumn
mldVlanMulticastGroupMacAddress = _MldVlanMulticastGroupMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 5, 2, 1, 5),
    _MldVlanMulticastGroupMacAddress_Type()
)
mldVlanMulticastGroupMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldVlanMulticastGroupMacAddress.setStatus("current")
_MldVlanMulticastGroupExp_Type = TimeTicks
_MldVlanMulticastGroupExp_Object = MibTableColumn
mldVlanMulticastGroupExp = _MldVlanMulticastGroupExp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 5, 2, 1, 7),
    _MldVlanMulticastGroupExp_Type()
)
mldVlanMulticastGroupExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldVlanMulticastGroupExp.setStatus("current")
_MldVlanMulticastGroupPortList_Type = PortList
_MldVlanMulticastGroupPortList_Object = MibTableColumn
mldVlanMulticastGroupPortList = _MldVlanMulticastGroupPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 5, 2, 1, 8),
    _MldVlanMulticastGroupPortList_Type()
)
mldVlanMulticastGroupPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldVlanMulticastGroupPortList.setStatus("current")
_MldVlanStaticMcastGrpTable_Object = MibTable
mldVlanStaticMcastGrpTable = _MldVlanStaticMcastGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 5, 3)
)
if mibBuilder.loadTexts:
    mldVlanStaticMcastGrpTable.setStatus("current")
_MldVlanStaticMcastGrpEntry_Object = MibTableRow
mldVlanStaticMcastGrpEntry = _MldVlanStaticMcastGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 5, 3, 1)
)
mldVlanStaticMcastGrpEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "mldVlanStaticMcastGrpVlanId"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "mldVlanStaticMcastGrpGroupAddress"),
)
if mibBuilder.loadTexts:
    mldVlanStaticMcastGrpEntry.setStatus("current")


class _MldVlanStaticMcastGrpVlanId_Type(Integer32):
    """Custom type mldVlanStaticMcastGrpVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MldVlanStaticMcastGrpVlanId_Type.__name__ = "Integer32"
_MldVlanStaticMcastGrpVlanId_Object = MibTableColumn
mldVlanStaticMcastGrpVlanId = _MldVlanStaticMcastGrpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 5, 3, 1, 1),
    _MldVlanStaticMcastGrpVlanId_Type()
)
mldVlanStaticMcastGrpVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldVlanStaticMcastGrpVlanId.setStatus("current")
_MldVlanStaticMcastGrpGroupAddress_Type = InetAddress
_MldVlanStaticMcastGrpGroupAddress_Object = MibTableColumn
mldVlanStaticMcastGrpGroupAddress = _MldVlanStaticMcastGrpGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 5, 3, 1, 2),
    _MldVlanStaticMcastGrpGroupAddress_Type()
)
mldVlanStaticMcastGrpGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldVlanStaticMcastGrpGroupAddress.setStatus("current")
_MldVlanStaticMcastGrpPortList_Type = PortList
_MldVlanStaticMcastGrpPortList_Object = MibTableColumn
mldVlanStaticMcastGrpPortList = _MldVlanStaticMcastGrpPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 5, 3, 1, 3),
    _MldVlanStaticMcastGrpPortList_Type()
)
mldVlanStaticMcastGrpPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldVlanStaticMcastGrpPortList.setStatus("current")
_MldVlanStaticMcastGrpRowStatus_Type = RowStatus
_MldVlanStaticMcastGrpRowStatus_Object = MibTableColumn
mldVlanStaticMcastGrpRowStatus = _MldVlanStaticMcastGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 5, 3, 1, 4),
    _MldVlanStaticMcastGrpRowStatus_Type()
)
mldVlanStaticMcastGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mldVlanStaticMcastGrpRowStatus.setStatus("current")
_MldVlanRouterTable_Object = MibTable
mldVlanRouterTable = _MldVlanRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 5, 4)
)
if mibBuilder.loadTexts:
    mldVlanRouterTable.setStatus("current")
_MldVlanRouterEntry_Object = MibTableRow
mldVlanRouterEntry = _MldVlanRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 5, 4, 1)
)
mldVlanRouterEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "mldVlanRouterVlanId"),
)
if mibBuilder.loadTexts:
    mldVlanRouterEntry.setStatus("current")


class _MldVlanRouterVlanId_Type(Integer32):
    """Custom type mldVlanRouterVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MldVlanRouterVlanId_Type.__name__ = "Integer32"
_MldVlanRouterVlanId_Object = MibTableColumn
mldVlanRouterVlanId = _MldVlanRouterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 5, 4, 1, 1),
    _MldVlanRouterVlanId_Type()
)
mldVlanRouterVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldVlanRouterVlanId.setStatus("current")
_MldVlanRouterStaticPortList_Type = PortList
_MldVlanRouterStaticPortList_Object = MibTableColumn
mldVlanRouterStaticPortList = _MldVlanRouterStaticPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 5, 4, 1, 2),
    _MldVlanRouterStaticPortList_Type()
)
mldVlanRouterStaticPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldVlanRouterStaticPortList.setStatus("current")
_MldVlanRouterBlockPortList_Type = PortList
_MldVlanRouterBlockPortList_Object = MibTableColumn
mldVlanRouterBlockPortList = _MldVlanRouterBlockPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 5, 4, 1, 3),
    _MldVlanRouterBlockPortList_Type()
)
mldVlanRouterBlockPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldVlanRouterBlockPortList.setStatus("current")
_MldVlanRouterDynamicPortList_Type = PortList
_MldVlanRouterDynamicPortList_Object = MibTableColumn
mldVlanRouterDynamicPortList = _MldVlanRouterDynamicPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 5, 4, 1, 4),
    _MldVlanRouterDynamicPortList_Type()
)
mldVlanRouterDynamicPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldVlanRouterDynamicPortList.setStatus("current")
_MldStats_ObjectIdentity = ObjectIdentity
mldStats = _MldStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 6)
)
_MldStatsTable_Object = MibTable
mldStatsTable = _MldStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 6, 1)
)
if mibBuilder.loadTexts:
    mldStatsTable.setStatus("current")
_MldStatsEntry_Object = MibTableRow
mldStatsEntry = _MldStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 6, 1, 1)
)
mldStatsEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "mldStatsVlanId"),
)
if mibBuilder.loadTexts:
    mldStatsEntry.setStatus("current")


class _MldStatsVlanId_Type(Integer32):
    """Custom type mldStatsVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MldStatsVlanId_Type.__name__ = "Integer32"
_MldStatsVlanId_Object = MibTableColumn
mldStatsVlanId = _MldStatsVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 6, 1, 1, 1),
    _MldStatsVlanId_Type()
)
mldStatsVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldStatsVlanId.setStatus("current")
_MldStatsMLDv1RxReport_Type = Counter32
_MldStatsMLDv1RxReport_Object = MibTableColumn
mldStatsMLDv1RxReport = _MldStatsMLDv1RxReport_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 6, 1, 1, 2),
    _MldStatsMLDv1RxReport_Type()
)
mldStatsMLDv1RxReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldStatsMLDv1RxReport.setStatus("current")
_MldStatsMLDv1RxDone_Type = Counter32
_MldStatsMLDv1RxDone_Object = MibTableColumn
mldStatsMLDv1RxDone = _MldStatsMLDv1RxDone_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 6, 1, 1, 3),
    _MldStatsMLDv1RxDone_Type()
)
mldStatsMLDv1RxDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldStatsMLDv1RxDone.setStatus("current")
_MldStatsMLDv1TxReport_Type = Counter32
_MldStatsMLDv1TxReport_Object = MibTableColumn
mldStatsMLDv1TxReport = _MldStatsMLDv1TxReport_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 6, 1, 1, 4),
    _MldStatsMLDv1TxReport_Type()
)
mldStatsMLDv1TxReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldStatsMLDv1TxReport.setStatus("current")
_MldStatsMLDv1TxDone_Type = Counter32
_MldStatsMLDv1TxDone_Object = MibTableColumn
mldStatsMLDv1TxDone = _MldStatsMLDv1TxDone_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 6, 1, 1, 5),
    _MldStatsMLDv1TxDone_Type()
)
mldStatsMLDv1TxDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldStatsMLDv1TxDone.setStatus("current")
_MldStatsMLDv2RxReport_Type = Counter32
_MldStatsMLDv2RxReport_Object = MibTableColumn
mldStatsMLDv2RxReport = _MldStatsMLDv2RxReport_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 6, 1, 1, 6),
    _MldStatsMLDv2RxReport_Type()
)
mldStatsMLDv2RxReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldStatsMLDv2RxReport.setStatus("current")
_MldStatsMLDv2TxReport_Type = Counter32
_MldStatsMLDv2TxReport_Object = MibTableColumn
mldStatsMLDv2TxReport = _MldStatsMLDv2TxReport_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 6, 1, 1, 7),
    _MldStatsMLDv2TxReport_Type()
)
mldStatsMLDv2TxReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldStatsMLDv2TxReport.setStatus("current")
_MldStatsRxQueries_Type = Counter32
_MldStatsRxQueries_Object = MibTableColumn
mldStatsRxQueries = _MldStatsRxQueries_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 6, 1, 1, 8),
    _MldStatsRxQueries_Type()
)
mldStatsRxQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldStatsRxQueries.setStatus("current")
_MldStatsTxQueries_Type = Counter32
_MldStatsTxQueries_Object = MibTableColumn
mldStatsTxQueries = _MldStatsTxQueries_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 6, 1, 1, 9),
    _MldStatsTxQueries_Type()
)
mldStatsTxQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldStatsTxQueries.setStatus("current")
_MulticastFilterVlanTable_Object = MibTable
multicastFilterVlanTable = _MulticastFilterVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 7)
)
if mibBuilder.loadTexts:
    multicastFilterVlanTable.setStatus("current")
_MulticastFilterVlanEntry_Object = MibTableRow
multicastFilterVlanEntry = _MulticastFilterVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 7, 1)
)
multicastFilterVlanEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "multicastFilterVlanIndex"),
)
if mibBuilder.loadTexts:
    multicastFilterVlanEntry.setStatus("current")
_MulticastFilterVlanIndex_Type = Integer32
_MulticastFilterVlanIndex_Object = MibTableColumn
multicastFilterVlanIndex = _MulticastFilterVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 7, 1, 1),
    _MulticastFilterVlanIndex_Type()
)
multicastFilterVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastFilterVlanIndex.setStatus("current")


class _MulticastFilterVlanType_Type(Integer32):
    """Custom type multicastFilterVlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filter", 1),
          ("forward", 0))
    )


_MulticastFilterVlanType_Type.__name__ = "Integer32"
_MulticastFilterVlanType_Object = MibTableColumn
multicastFilterVlanType = _MulticastFilterVlanType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 6, 7, 1, 2),
    _MulticastFilterVlanType_Type()
)
multicastFilterVlanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastFilterVlanType.setStatus("current")
_L2LLDPGroup_ObjectIdentity = ObjectIdentity
l2LLDPGroup = _L2LLDPGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7)
)


class _LldpState_Type(Integer32):
    """Custom type lldpState based on Integer32"""
    defaultValue = 2

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


_LldpState_Type.__name__ = "Integer32"
_LldpState_Object = MibScalar
lldpState = _LldpState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 1),
    _LldpState_Type()
)
lldpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpState.setStatus("current")


class _LldpForwardState_Type(Integer32):
    """Custom type lldpForwardState based on Integer32"""
    defaultValue = 2

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


_LldpForwardState_Type.__name__ = "Integer32"
_LldpForwardState_Object = MibScalar
lldpForwardState = _LldpForwardState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 2),
    _LldpForwardState_Type()
)
lldpForwardState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpForwardState.setStatus("current")


class _LldpTrapState_Type(Integer32):
    """Custom type lldpTrapState based on Integer32"""
    defaultValue = 2

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


_LldpTrapState_Type.__name__ = "Integer32"
_LldpTrapState_Object = MibScalar
lldpTrapState = _LldpTrapState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 3),
    _LldpTrapState_Type()
)
lldpTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpTrapState.setStatus("current")


class _LldpMEDTrapState_Type(Integer32):
    """Custom type lldpMEDTrapState based on Integer32"""
    defaultValue = 2

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


_LldpMEDTrapState_Type.__name__ = "Integer32"
_LldpMEDTrapState_Object = MibScalar
lldpMEDTrapState = _LldpMEDTrapState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 4),
    _LldpMEDTrapState_Type()
)
lldpMEDTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpMEDTrapState.setStatus("current")


class _LldpMsgTxInterval_Type(Integer32):
    """Custom type lldpMsgTxInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 32768),
    )


_LldpMsgTxInterval_Type.__name__ = "Integer32"
_LldpMsgTxInterval_Object = MibScalar
lldpMsgTxInterval = _LldpMsgTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 5),
    _LldpMsgTxInterval_Type()
)
lldpMsgTxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpMsgTxInterval.setStatus("current")


class _LldpMsgHoldMultiplier_Type(Integer32):
    """Custom type lldpMsgHoldMultiplier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_LldpMsgHoldMultiplier_Type.__name__ = "Integer32"
_LldpMsgHoldMultiplier_Object = MibScalar
lldpMsgHoldMultiplier = _LldpMsgHoldMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 6),
    _LldpMsgHoldMultiplier_Type()
)
lldpMsgHoldMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpMsgHoldMultiplier.setStatus("current")


class _LldpReinitDelay_Type(Integer32):
    """Custom type lldpReinitDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_LldpReinitDelay_Type.__name__ = "Integer32"
_LldpReinitDelay_Object = MibScalar
lldpReinitDelay = _LldpReinitDelay_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 7),
    _LldpReinitDelay_Type()
)
lldpReinitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpReinitDelay.setStatus("current")


class _LldpTxDelay_Type(Integer32):
    """Custom type lldpTxDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_LldpTxDelay_Type.__name__ = "Integer32"
_LldpTxDelay_Object = MibScalar
lldpTxDelay = _LldpTxDelay_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 8),
    _LldpTxDelay_Type()
)
lldpTxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpTxDelay.setStatus("current")
_LldpPortConfigTable_Object = MibTable
lldpPortConfigTable = _LldpPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 10)
)
if mibBuilder.loadTexts:
    lldpPortConfigTable.setStatus("current")
_LldpPortConfigEntry_Object = MibTableRow
lldpPortConfigEntry = _LldpPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 10, 1)
)
lldpPortConfigEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpPortConfigPortNum"),
)
if mibBuilder.loadTexts:
    lldpPortConfigEntry.setStatus("current")
_LldpPortConfigPortNum_Type = LldpPortNumber
_LldpPortConfigPortNum_Object = MibTableColumn
lldpPortConfigPortNum = _LldpPortConfigPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 10, 1, 1),
    _LldpPortConfigPortNum_Type()
)
lldpPortConfigPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpPortConfigPortNum.setStatus("current")


class _LldpPortConfigAdminStatus_Type(Integer32):
    """Custom type lldpPortConfigAdminStatus based on Integer32"""
    defaultValue = 3

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
        *(("disabled", 4),
          ("rxOnly", 2),
          ("txAndRx", 3),
          ("txOnly", 1))
    )


_LldpPortConfigAdminStatus_Type.__name__ = "Integer32"
_LldpPortConfigAdminStatus_Object = MibTableColumn
lldpPortConfigAdminStatus = _LldpPortConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 10, 1, 2),
    _LldpPortConfigAdminStatus_Type()
)
lldpPortConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpPortConfigAdminStatus.setStatus("current")


class _LldpPortConfigSubtype_Type(Integer32):
    """Custom type lldpPortConfigSubtype based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("macAddress", 2))
    )


_LldpPortConfigSubtype_Type.__name__ = "Integer32"
_LldpPortConfigSubtype_Object = MibTableColumn
lldpPortConfigSubtype = _LldpPortConfigSubtype_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 10, 1, 3),
    _LldpPortConfigSubtype_Type()
)
lldpPortConfigSubtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpPortConfigSubtype.setStatus("current")


class _LldpPortConfigTLVsTxEnable_Type(Bits):
    """Custom type lldpPortConfigTLVsTxEnable based on Bits"""
    namedValues = NamedValues(
        *(("portDesc", 0),
          ("sysCap", 3),
          ("sysDesc", 2),
          ("sysName", 1))
    )

_LldpPortConfigTLVsTxEnable_Type.__name__ = "Bits"
_LldpPortConfigTLVsTxEnable_Object = MibTableColumn
lldpPortConfigTLVsTxEnable = _LldpPortConfigTLVsTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 10, 1, 4),
    _LldpPortConfigTLVsTxEnable_Type()
)
lldpPortConfigTLVsTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpPortConfigTLVsTxEnable.setStatus("current")
_LldpPortStatsClear_Type = Integer32
_LldpPortStatsClear_Object = MibTableColumn
lldpPortStatsClear = _LldpPortStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 10, 1, 5),
    _LldpPortStatsClear_Type()
)
lldpPortStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpPortStatsClear.setStatus("current")
_LldpPortNeighborClear_Type = Integer32
_LldpPortNeighborClear_Object = MibTableColumn
lldpPortNeighborClear = _LldpPortNeighborClear_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 10, 1, 6),
    _LldpPortNeighborClear_Type()
)
lldpPortNeighborClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpPortNeighborClear.setStatus("current")
_LldpConfigManAddrTable_Object = MibTable
lldpConfigManAddrTable = _LldpConfigManAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 11)
)
if mibBuilder.loadTexts:
    lldpConfigManAddrTable.setStatus("current")
_LldpConfigManAddrEntry_Object = MibTableRow
lldpConfigManAddrEntry = _LldpConfigManAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 11, 1)
)
lldpConfigManAddrEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpConfigManAddrSubtype"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpConfigManAddr"),
)
if mibBuilder.loadTexts:
    lldpConfigManAddrEntry.setStatus("current")
_LldpConfigManAddrSubtype_Type = AddressFamilyNumbers
_LldpConfigManAddrSubtype_Object = MibTableColumn
lldpConfigManAddrSubtype = _LldpConfigManAddrSubtype_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 11, 1, 1),
    _LldpConfigManAddrSubtype_Type()
)
lldpConfigManAddrSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpConfigManAddrSubtype.setStatus("current")
_LldpConfigManAddr_Type = InetAddress
_LldpConfigManAddr_Object = MibTableColumn
lldpConfigManAddr = _LldpConfigManAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 11, 1, 2),
    _LldpConfigManAddr_Type()
)
lldpConfigManAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpConfigManAddr.setStatus("current")


class _LldpConfigManAddrPortsTxEnable_Type(LldpPortList):
    """Custom type lldpConfigManAddrPortsTxEnable based on LldpPortList"""
    defaultHexValue = ""


_LldpConfigManAddrPortsTxEnable_Object = MibTableColumn
lldpConfigManAddrPortsTxEnable = _LldpConfigManAddrPortsTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 11, 1, 3),
    _LldpConfigManAddrPortsTxEnable_Type()
)
lldpConfigManAddrPortsTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpConfigManAddrPortsTxEnable.setStatus("current")
_LldpXdot1Objects_ObjectIdentity = ObjectIdentity
lldpXdot1Objects = _LldpXdot1Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13)
)
_LldpXdot1Config_ObjectIdentity = ObjectIdentity
lldpXdot1Config = _LldpXdot1Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 1)
)
_LldpXdot1ConfigPortVlanTable_Object = MibTable
lldpXdot1ConfigPortVlanTable = _LldpXdot1ConfigPortVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 1, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1ConfigPortVlanTable.setStatus("current")
_LldpXdot1ConfigPortVlanEntry_Object = MibTableRow
lldpXdot1ConfigPortVlanEntry = _LldpXdot1ConfigPortVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 1, 1, 1)
)
lldpXdot1ConfigPortVlanEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXdot1ConfigVlanPortNum"),
)
if mibBuilder.loadTexts:
    lldpXdot1ConfigPortVlanEntry.setStatus("current")
_LldpXdot1ConfigVlanPortNum_Type = LldpPortNumber
_LldpXdot1ConfigVlanPortNum_Object = MibTableColumn
lldpXdot1ConfigVlanPortNum = _LldpXdot1ConfigVlanPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 1, 1, 1, 1),
    _LldpXdot1ConfigVlanPortNum_Type()
)
lldpXdot1ConfigVlanPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1ConfigVlanPortNum.setStatus("current")


class _LldpXdot1ConfigPortVlanTxEnable_Type(TruthValue):
    """Custom type lldpXdot1ConfigPortVlanTxEnable based on TruthValue"""


_LldpXdot1ConfigPortVlanTxEnable_Object = MibTableColumn
lldpXdot1ConfigPortVlanTxEnable = _LldpXdot1ConfigPortVlanTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 1, 1, 1, 2),
    _LldpXdot1ConfigPortVlanTxEnable_Type()
)
lldpXdot1ConfigPortVlanTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1ConfigPortVlanTxEnable.setStatus("current")
_LldpXdot1ConfigVlanNameTable_Object = MibTable
lldpXdot1ConfigVlanNameTable = _LldpXdot1ConfigVlanNameTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 1, 2)
)
if mibBuilder.loadTexts:
    lldpXdot1ConfigVlanNameTable.setStatus("current")
_LldpXdot1ConfigVlanNameEntry_Object = MibTableRow
lldpXdot1ConfigVlanNameEntry = _LldpXdot1ConfigVlanNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 1, 2, 1)
)
lldpXdot1ConfigVlanNameEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXdot1LocConfigVlanNamePortNum"),
)
if mibBuilder.loadTexts:
    lldpXdot1ConfigVlanNameEntry.setStatus("current")
_LldpXdot1LocConfigVlanNamePortNum_Type = LldpPortNumber
_LldpXdot1LocConfigVlanNamePortNum_Object = MibTableColumn
lldpXdot1LocConfigVlanNamePortNum = _LldpXdot1LocConfigVlanNamePortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 1, 2, 1, 1),
    _LldpXdot1LocConfigVlanNamePortNum_Type()
)
lldpXdot1LocConfigVlanNamePortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1LocConfigVlanNamePortNum.setStatus("current")


class _LldpXdot1ConfigVlanNameTxEnableVlanList_Type(OctetString):
    """Custom type lldpXdot1ConfigVlanNameTxEnableVlanList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_LldpXdot1ConfigVlanNameTxEnableVlanList_Type.__name__ = "OctetString"
_LldpXdot1ConfigVlanNameTxEnableVlanList_Object = MibTableColumn
lldpXdot1ConfigVlanNameTxEnableVlanList = _LldpXdot1ConfigVlanNameTxEnableVlanList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 1, 2, 1, 2),
    _LldpXdot1ConfigVlanNameTxEnableVlanList_Type()
)
lldpXdot1ConfigVlanNameTxEnableVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1ConfigVlanNameTxEnableVlanList.setStatus("current")
_LldpXdot1ConfigProtoVlanTable_Object = MibTable
lldpXdot1ConfigProtoVlanTable = _LldpXdot1ConfigProtoVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 1, 3)
)
if mibBuilder.loadTexts:
    lldpXdot1ConfigProtoVlanTable.setStatus("current")
_LldpXdot1ConfigProtoVlanEntry_Object = MibTableRow
lldpXdot1ConfigProtoVlanEntry = _LldpXdot1ConfigProtoVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 1, 3, 1)
)
lldpXdot1ConfigProtoVlanEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXdot1ConfigProtoVlanPortNum"),
)
if mibBuilder.loadTexts:
    lldpXdot1ConfigProtoVlanEntry.setStatus("current")
_LldpXdot1ConfigProtoVlanPortNum_Type = LldpPortNumber
_LldpXdot1ConfigProtoVlanPortNum_Object = MibTableColumn
lldpXdot1ConfigProtoVlanPortNum = _LldpXdot1ConfigProtoVlanPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 1, 3, 1, 1),
    _LldpXdot1ConfigProtoVlanPortNum_Type()
)
lldpXdot1ConfigProtoVlanPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1ConfigProtoVlanPortNum.setStatus("current")


class _LldpXdot1ConfigProtoVlanTxEnable_Type(TruthValue):
    """Custom type lldpXdot1ConfigProtoVlanTxEnable based on TruthValue"""


_LldpXdot1ConfigProtoVlanTxEnable_Object = MibTableColumn
lldpXdot1ConfigProtoVlanTxEnable = _LldpXdot1ConfigProtoVlanTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 1, 3, 1, 2),
    _LldpXdot1ConfigProtoVlanTxEnable_Type()
)
lldpXdot1ConfigProtoVlanTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1ConfigProtoVlanTxEnable.setStatus("current")
_LldpXdot1ConfigProtocolTable_Object = MibTable
lldpXdot1ConfigProtocolTable = _LldpXdot1ConfigProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 1, 4)
)
if mibBuilder.loadTexts:
    lldpXdot1ConfigProtocolTable.setStatus("current")
_LldpXdot1ConfigProtocolEntry_Object = MibTableRow
lldpXdot1ConfigProtocolEntry = _LldpXdot1ConfigProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 1, 4, 1)
)
lldpXdot1ConfigProtocolEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXdot1ConfigProtocolPortNum"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXdot1ConfigProtocolIndex"),
)
if mibBuilder.loadTexts:
    lldpXdot1ConfigProtocolEntry.setStatus("current")
_LldpXdot1ConfigProtocolPortNum_Type = LldpPortNumber
_LldpXdot1ConfigProtocolPortNum_Object = MibTableColumn
lldpXdot1ConfigProtocolPortNum = _LldpXdot1ConfigProtocolPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 1, 4, 1, 1),
    _LldpXdot1ConfigProtocolPortNum_Type()
)
lldpXdot1ConfigProtocolPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1ConfigProtocolPortNum.setStatus("current")


class _LldpXdot1ConfigProtocolIndex_Type(Integer32):
    """Custom type lldpXdot1ConfigProtocolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpXdot1ConfigProtocolIndex_Type.__name__ = "Integer32"
_LldpXdot1ConfigProtocolIndex_Object = MibTableColumn
lldpXdot1ConfigProtocolIndex = _LldpXdot1ConfigProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 1, 4, 1, 2),
    _LldpXdot1ConfigProtocolIndex_Type()
)
lldpXdot1ConfigProtocolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1ConfigProtocolIndex.setStatus("current")


class _LldpXdot1ConfigProtocolTxEnable_Type(TruthValue):
    """Custom type lldpXdot1ConfigProtocolTxEnable based on TruthValue"""


_LldpXdot1ConfigProtocolTxEnable_Object = MibTableColumn
lldpXdot1ConfigProtocolTxEnable = _LldpXdot1ConfigProtocolTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 1, 4, 1, 3),
    _LldpXdot1ConfigProtocolTxEnable_Type()
)
lldpXdot1ConfigProtocolTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1ConfigProtocolTxEnable.setStatus("current")
_LldpXdot1LocalData_ObjectIdentity = ObjectIdentity
lldpXdot1LocalData = _LldpXdot1LocalData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 2)
)
_LldpXdot1LocTable_Object = MibTable
lldpXdot1LocTable = _LldpXdot1LocTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 2, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1LocTable.setStatus("current")
_LldpXdot1LocEntry_Object = MibTableRow
lldpXdot1LocEntry = _LldpXdot1LocEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 2, 1, 1)
)
lldpXdot1LocEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXdot1LocPortNum"),
)
if mibBuilder.loadTexts:
    lldpXdot1LocEntry.setStatus("current")
_LldpXdot1LocPortNum_Type = LldpPortNumber
_LldpXdot1LocPortNum_Object = MibTableColumn
lldpXdot1LocPortNum = _LldpXdot1LocPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 2, 1, 1, 1),
    _LldpXdot1LocPortNum_Type()
)
lldpXdot1LocPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1LocPortNum.setStatus("current")


class _LldpXdot1LocPortVlanId_Type(Integer32):
    """Custom type lldpXdot1LocPortVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )


_LldpXdot1LocPortVlanId_Type.__name__ = "Integer32"
_LldpXdot1LocPortVlanId_Object = MibTableColumn
lldpXdot1LocPortVlanId = _LldpXdot1LocPortVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 2, 1, 1, 2),
    _LldpXdot1LocPortVlanId_Type()
)
lldpXdot1LocPortVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1LocPortVlanId.setStatus("current")
_LldpXdot1LocProtoVlanTable_Object = MibTable
lldpXdot1LocProtoVlanTable = _LldpXdot1LocProtoVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 2, 2)
)
if mibBuilder.loadTexts:
    lldpXdot1LocProtoVlanTable.setStatus("current")
_LldpXdot1LocProtoVlanEntry_Object = MibTableRow
lldpXdot1LocProtoVlanEntry = _LldpXdot1LocProtoVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 2, 2, 1)
)
lldpXdot1LocProtoVlanEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXdot1LocProtoVlanPortNum"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXdot1LocProtoVlanId"),
)
if mibBuilder.loadTexts:
    lldpXdot1LocProtoVlanEntry.setStatus("current")
_LldpXdot1LocProtoVlanPortNum_Type = LldpPortNumber
_LldpXdot1LocProtoVlanPortNum_Object = MibTableColumn
lldpXdot1LocProtoVlanPortNum = _LldpXdot1LocProtoVlanPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 2, 2, 1, 1),
    _LldpXdot1LocProtoVlanPortNum_Type()
)
lldpXdot1LocProtoVlanPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1LocProtoVlanPortNum.setStatus("current")


class _LldpXdot1LocProtoVlanId_Type(Integer32):
    """Custom type lldpXdot1LocProtoVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )


_LldpXdot1LocProtoVlanId_Type.__name__ = "Integer32"
_LldpXdot1LocProtoVlanId_Object = MibTableColumn
lldpXdot1LocProtoVlanId = _LldpXdot1LocProtoVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 2, 2, 1, 2),
    _LldpXdot1LocProtoVlanId_Type()
)
lldpXdot1LocProtoVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1LocProtoVlanId.setStatus("current")
_LldpXdot1LocProtoVlanSupported_Type = TruthValue
_LldpXdot1LocProtoVlanSupported_Object = MibTableColumn
lldpXdot1LocProtoVlanSupported = _LldpXdot1LocProtoVlanSupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 2, 2, 1, 3),
    _LldpXdot1LocProtoVlanSupported_Type()
)
lldpXdot1LocProtoVlanSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1LocProtoVlanSupported.setStatus("current")
_LldpXdot1LocProtoVlanEnabled_Type = TruthValue
_LldpXdot1LocProtoVlanEnabled_Object = MibTableColumn
lldpXdot1LocProtoVlanEnabled = _LldpXdot1LocProtoVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 2, 2, 1, 4),
    _LldpXdot1LocProtoVlanEnabled_Type()
)
lldpXdot1LocProtoVlanEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1LocProtoVlanEnabled.setStatus("current")
_LldpXdot1LocVlanNameTable_Object = MibTable
lldpXdot1LocVlanNameTable = _LldpXdot1LocVlanNameTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 2, 3)
)
if mibBuilder.loadTexts:
    lldpXdot1LocVlanNameTable.setStatus("current")
_LldpXdot1LocVlanNameEntry_Object = MibTableRow
lldpXdot1LocVlanNameEntry = _LldpXdot1LocVlanNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 2, 3, 1)
)
lldpXdot1LocVlanNameEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXdot1LocVlanNamePortNum"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXdot1LocVlanId"),
)
if mibBuilder.loadTexts:
    lldpXdot1LocVlanNameEntry.setStatus("current")
_LldpXdot1LocVlanNamePortNum_Type = LldpPortNumber
_LldpXdot1LocVlanNamePortNum_Object = MibTableColumn
lldpXdot1LocVlanNamePortNum = _LldpXdot1LocVlanNamePortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 2, 3, 1, 1),
    _LldpXdot1LocVlanNamePortNum_Type()
)
lldpXdot1LocVlanNamePortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1LocVlanNamePortNum.setStatus("current")
_LldpXdot1LocVlanId_Type = VlanId
_LldpXdot1LocVlanId_Object = MibTableColumn
lldpXdot1LocVlanId = _LldpXdot1LocVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 2, 3, 1, 2),
    _LldpXdot1LocVlanId_Type()
)
lldpXdot1LocVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1LocVlanId.setStatus("current")


class _LldpXdot1LocVlanName_Type(SnmpAdminString):
    """Custom type lldpXdot1LocVlanName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_LldpXdot1LocVlanName_Type.__name__ = "SnmpAdminString"
_LldpXdot1LocVlanName_Object = MibTableColumn
lldpXdot1LocVlanName = _LldpXdot1LocVlanName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 2, 3, 1, 3),
    _LldpXdot1LocVlanName_Type()
)
lldpXdot1LocVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1LocVlanName.setStatus("current")
_LldpXdot1LocProtocolTable_Object = MibTable
lldpXdot1LocProtocolTable = _LldpXdot1LocProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 2, 4)
)
if mibBuilder.loadTexts:
    lldpXdot1LocProtocolTable.setStatus("current")
_LldpXdot1LocProtocolEntry_Object = MibTableRow
lldpXdot1LocProtocolEntry = _LldpXdot1LocProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 2, 4, 1)
)
lldpXdot1LocProtocolEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXdot1LocProtocolPortNum"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXdot1LocProtocolIndex"),
)
if mibBuilder.loadTexts:
    lldpXdot1LocProtocolEntry.setStatus("current")
_LldpXdot1LocProtocolPortNum_Type = LldpPortNumber
_LldpXdot1LocProtocolPortNum_Object = MibTableColumn
lldpXdot1LocProtocolPortNum = _LldpXdot1LocProtocolPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 2, 4, 1, 1),
    _LldpXdot1LocProtocolPortNum_Type()
)
lldpXdot1LocProtocolPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1LocProtocolPortNum.setStatus("current")


class _LldpXdot1LocProtocolIndex_Type(Integer32):
    """Custom type lldpXdot1LocProtocolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpXdot1LocProtocolIndex_Type.__name__ = "Integer32"
_LldpXdot1LocProtocolIndex_Object = MibTableColumn
lldpXdot1LocProtocolIndex = _LldpXdot1LocProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 2, 4, 1, 2),
    _LldpXdot1LocProtocolIndex_Type()
)
lldpXdot1LocProtocolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1LocProtocolIndex.setStatus("current")


class _LldpXdot1LocProtocolId_Type(OctetString):
    """Custom type lldpXdot1LocProtocolId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_LldpXdot1LocProtocolId_Type.__name__ = "OctetString"
_LldpXdot1LocProtocolId_Object = MibTableColumn
lldpXdot1LocProtocolId = _LldpXdot1LocProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 2, 4, 1, 3),
    _LldpXdot1LocProtocolId_Type()
)
lldpXdot1LocProtocolId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1LocProtocolId.setStatus("current")
_LldpXdot1RemoteData_ObjectIdentity = ObjectIdentity
lldpXdot1RemoteData = _LldpXdot1RemoteData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 3)
)
_LldpXdot1RemTable_Object = MibTable
lldpXdot1RemTable = _LldpXdot1RemTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 3, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1RemTable.setStatus("current")
_LldpXdot1RemEntry_Object = MibTableRow
lldpXdot1RemEntry = _LldpXdot1RemEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 3, 1, 1)
)
lldpXdot1RemEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXdot1RemTimeMark"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXdot1RemLocalPortNum"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXdot1RemIndex"),
)
if mibBuilder.loadTexts:
    lldpXdot1RemEntry.setStatus("current")
_LldpXdot1RemTimeMark_Type = TimeFilter
_LldpXdot1RemTimeMark_Object = MibTableColumn
lldpXdot1RemTimeMark = _LldpXdot1RemTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 3, 1, 1, 1),
    _LldpXdot1RemTimeMark_Type()
)
lldpXdot1RemTimeMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemTimeMark.setStatus("current")
_LldpXdot1RemLocalPortNum_Type = LldpPortNumber
_LldpXdot1RemLocalPortNum_Object = MibTableColumn
lldpXdot1RemLocalPortNum = _LldpXdot1RemLocalPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 3, 1, 1, 2),
    _LldpXdot1RemLocalPortNum_Type()
)
lldpXdot1RemLocalPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemLocalPortNum.setStatus("current")


class _LldpXdot1RemIndex_Type(Integer32):
    """Custom type lldpXdot1RemIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpXdot1RemIndex_Type.__name__ = "Integer32"
_LldpXdot1RemIndex_Object = MibTableColumn
lldpXdot1RemIndex = _LldpXdot1RemIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 3, 1, 1, 3),
    _LldpXdot1RemIndex_Type()
)
lldpXdot1RemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemIndex.setStatus("current")


class _LldpXdot1RemPortVlanId_Type(Integer32):
    """Custom type lldpXdot1RemPortVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )


_LldpXdot1RemPortVlanId_Type.__name__ = "Integer32"
_LldpXdot1RemPortVlanId_Object = MibTableColumn
lldpXdot1RemPortVlanId = _LldpXdot1RemPortVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 3, 1, 1, 4),
    _LldpXdot1RemPortVlanId_Type()
)
lldpXdot1RemPortVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemPortVlanId.setStatus("current")
_LldpXdot1RemProtoVlanTable_Object = MibTable
lldpXdot1RemProtoVlanTable = _LldpXdot1RemProtoVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 3, 2)
)
if mibBuilder.loadTexts:
    lldpXdot1RemProtoVlanTable.setStatus("current")
_LldpXdot1RemProtoVlanEntry_Object = MibTableRow
lldpXdot1RemProtoVlanEntry = _LldpXdot1RemProtoVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 3, 2, 1)
)
lldpXdot1RemProtoVlanEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXdot1RemProtoVlanTimeMark"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXdot1RemProtoVlanLocalPortNum"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXdot1RemProtoVlanIndex"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXdot1RemProtoVlanId"),
)
if mibBuilder.loadTexts:
    lldpXdot1RemProtoVlanEntry.setStatus("current")
_LldpXdot1RemProtoVlanTimeMark_Type = TimeFilter
_LldpXdot1RemProtoVlanTimeMark_Object = MibTableColumn
lldpXdot1RemProtoVlanTimeMark = _LldpXdot1RemProtoVlanTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 3, 2, 1, 1),
    _LldpXdot1RemProtoVlanTimeMark_Type()
)
lldpXdot1RemProtoVlanTimeMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemProtoVlanTimeMark.setStatus("current")
_LldpXdot1RemProtoVlanLocalPortNum_Type = LldpPortNumber
_LldpXdot1RemProtoVlanLocalPortNum_Object = MibTableColumn
lldpXdot1RemProtoVlanLocalPortNum = _LldpXdot1RemProtoVlanLocalPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 3, 2, 1, 2),
    _LldpXdot1RemProtoVlanLocalPortNum_Type()
)
lldpXdot1RemProtoVlanLocalPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemProtoVlanLocalPortNum.setStatus("current")


class _LldpXdot1RemProtoVlanIndex_Type(Integer32):
    """Custom type lldpXdot1RemProtoVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpXdot1RemProtoVlanIndex_Type.__name__ = "Integer32"
_LldpXdot1RemProtoVlanIndex_Object = MibTableColumn
lldpXdot1RemProtoVlanIndex = _LldpXdot1RemProtoVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 3, 2, 1, 3),
    _LldpXdot1RemProtoVlanIndex_Type()
)
lldpXdot1RemProtoVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemProtoVlanIndex.setStatus("current")


class _LldpXdot1RemProtoVlanId_Type(Integer32):
    """Custom type lldpXdot1RemProtoVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )


_LldpXdot1RemProtoVlanId_Type.__name__ = "Integer32"
_LldpXdot1RemProtoVlanId_Object = MibTableColumn
lldpXdot1RemProtoVlanId = _LldpXdot1RemProtoVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 3, 2, 1, 4),
    _LldpXdot1RemProtoVlanId_Type()
)
lldpXdot1RemProtoVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1RemProtoVlanId.setStatus("current")
_LldpXdot1RemProtoVlanSupported_Type = TruthValue
_LldpXdot1RemProtoVlanSupported_Object = MibTableColumn
lldpXdot1RemProtoVlanSupported = _LldpXdot1RemProtoVlanSupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 3, 2, 1, 5),
    _LldpXdot1RemProtoVlanSupported_Type()
)
lldpXdot1RemProtoVlanSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemProtoVlanSupported.setStatus("current")
_LldpXdot1RemProtoVlanEnabled_Type = TruthValue
_LldpXdot1RemProtoVlanEnabled_Object = MibTableColumn
lldpXdot1RemProtoVlanEnabled = _LldpXdot1RemProtoVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 3, 2, 1, 6),
    _LldpXdot1RemProtoVlanEnabled_Type()
)
lldpXdot1RemProtoVlanEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemProtoVlanEnabled.setStatus("current")
_LldpXdot1RemVlanNameTable_Object = MibTable
lldpXdot1RemVlanNameTable = _LldpXdot1RemVlanNameTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 3, 3)
)
if mibBuilder.loadTexts:
    lldpXdot1RemVlanNameTable.setStatus("current")
_LldpXdot1RemVlanNameEntry_Object = MibTableRow
lldpXdot1RemVlanNameEntry = _LldpXdot1RemVlanNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 3, 3, 1)
)
lldpXdot1RemVlanNameEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXdot1RemVlanNameTimeMark"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXdot1RemVlanNameLocalPortNum"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXdot1RemVlanNameIndex"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXdot1RemVlanId"),
)
if mibBuilder.loadTexts:
    lldpXdot1RemVlanNameEntry.setStatus("current")
_LldpXdot1RemVlanNameTimeMark_Type = TimeFilter
_LldpXdot1RemVlanNameTimeMark_Object = MibTableColumn
lldpXdot1RemVlanNameTimeMark = _LldpXdot1RemVlanNameTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 3, 3, 1, 1),
    _LldpXdot1RemVlanNameTimeMark_Type()
)
lldpXdot1RemVlanNameTimeMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemVlanNameTimeMark.setStatus("current")
_LldpXdot1RemVlanNameLocalPortNum_Type = LldpPortNumber
_LldpXdot1RemVlanNameLocalPortNum_Object = MibTableColumn
lldpXdot1RemVlanNameLocalPortNum = _LldpXdot1RemVlanNameLocalPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 3, 3, 1, 2),
    _LldpXdot1RemVlanNameLocalPortNum_Type()
)
lldpXdot1RemVlanNameLocalPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemVlanNameLocalPortNum.setStatus("current")


class _LldpXdot1RemVlanNameIndex_Type(Integer32):
    """Custom type lldpXdot1RemVlanNameIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpXdot1RemVlanNameIndex_Type.__name__ = "Integer32"
_LldpXdot1RemVlanNameIndex_Object = MibTableColumn
lldpXdot1RemVlanNameIndex = _LldpXdot1RemVlanNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 3, 3, 1, 3),
    _LldpXdot1RemVlanNameIndex_Type()
)
lldpXdot1RemVlanNameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemVlanNameIndex.setStatus("current")
_LldpXdot1RemVlanId_Type = VlanId
_LldpXdot1RemVlanId_Object = MibTableColumn
lldpXdot1RemVlanId = _LldpXdot1RemVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 3, 3, 1, 4),
    _LldpXdot1RemVlanId_Type()
)
lldpXdot1RemVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemVlanId.setStatus("current")


class _LldpXdot1RemVlanName_Type(SnmpAdminString):
    """Custom type lldpXdot1RemVlanName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_LldpXdot1RemVlanName_Type.__name__ = "SnmpAdminString"
_LldpXdot1RemVlanName_Object = MibTableColumn
lldpXdot1RemVlanName = _LldpXdot1RemVlanName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 3, 3, 1, 5),
    _LldpXdot1RemVlanName_Type()
)
lldpXdot1RemVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemVlanName.setStatus("current")
_LldpXdot1RemProtocolTable_Object = MibTable
lldpXdot1RemProtocolTable = _LldpXdot1RemProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 3, 4)
)
if mibBuilder.loadTexts:
    lldpXdot1RemProtocolTable.setStatus("current")
_LldpXdot1RemProtocolEntry_Object = MibTableRow
lldpXdot1RemProtocolEntry = _LldpXdot1RemProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 3, 4, 1)
)
lldpXdot1RemProtocolEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXdot1RemProtocolTimeMark"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXdot1RemProtocolLocalPortNum"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXdot1RemProtocolIndex"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXdot1RemProtocolIdIndex"),
)
if mibBuilder.loadTexts:
    lldpXdot1RemProtocolEntry.setStatus("current")
_LldpXdot1RemProtocolTimeMark_Type = TimeFilter
_LldpXdot1RemProtocolTimeMark_Object = MibTableColumn
lldpXdot1RemProtocolTimeMark = _LldpXdot1RemProtocolTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 3, 4, 1, 1),
    _LldpXdot1RemProtocolTimeMark_Type()
)
lldpXdot1RemProtocolTimeMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemProtocolTimeMark.setStatus("current")
_LldpXdot1RemProtocolLocalPortNum_Type = LldpPortNumber
_LldpXdot1RemProtocolLocalPortNum_Object = MibTableColumn
lldpXdot1RemProtocolLocalPortNum = _LldpXdot1RemProtocolLocalPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 3, 4, 1, 2),
    _LldpXdot1RemProtocolLocalPortNum_Type()
)
lldpXdot1RemProtocolLocalPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemProtocolLocalPortNum.setStatus("current")


class _LldpXdot1RemProtocolIndex_Type(Integer32):
    """Custom type lldpXdot1RemProtocolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpXdot1RemProtocolIndex_Type.__name__ = "Integer32"
_LldpXdot1RemProtocolIndex_Object = MibTableColumn
lldpXdot1RemProtocolIndex = _LldpXdot1RemProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 3, 4, 1, 3),
    _LldpXdot1RemProtocolIndex_Type()
)
lldpXdot1RemProtocolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemProtocolIndex.setStatus("current")


class _LldpXdot1RemProtocolIdIndex_Type(Integer32):
    """Custom type lldpXdot1RemProtocolIdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpXdot1RemProtocolIdIndex_Type.__name__ = "Integer32"
_LldpXdot1RemProtocolIdIndex_Object = MibTableColumn
lldpXdot1RemProtocolIdIndex = _LldpXdot1RemProtocolIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 3, 4, 1, 4),
    _LldpXdot1RemProtocolIdIndex_Type()
)
lldpXdot1RemProtocolIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemProtocolIdIndex.setStatus("current")


class _LldpXdot1RemProtocolId_Type(OctetString):
    """Custom type lldpXdot1RemProtocolId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_LldpXdot1RemProtocolId_Type.__name__ = "OctetString"
_LldpXdot1RemProtocolId_Object = MibTableColumn
lldpXdot1RemProtocolId = _LldpXdot1RemProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 13, 3, 4, 1, 5),
    _LldpXdot1RemProtocolId_Type()
)
lldpXdot1RemProtocolId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemProtocolId.setStatus("current")
_LldpXdot3Objects_ObjectIdentity = ObjectIdentity
lldpXdot3Objects = _LldpXdot3Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14)
)
_LldpXdot3Config_ObjectIdentity = ObjectIdentity
lldpXdot3Config = _LldpXdot3Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 1)
)
_LldpXdot3PortConfigTable_Object = MibTable
lldpXdot3PortConfigTable = _LldpXdot3PortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 1, 1)
)
if mibBuilder.loadTexts:
    lldpXdot3PortConfigTable.setStatus("current")
_LldpXdot3PortConfigEntry_Object = MibTableRow
lldpXdot3PortConfigEntry = _LldpXdot3PortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 1, 1, 1)
)
lldpXdot3PortConfigEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXdot3PortConfigPortNum"),
)
if mibBuilder.loadTexts:
    lldpXdot3PortConfigEntry.setStatus("current")
_LldpXdot3PortConfigPortNum_Type = LldpPortNumber
_LldpXdot3PortConfigPortNum_Object = MibTableColumn
lldpXdot3PortConfigPortNum = _LldpXdot3PortConfigPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 1, 1, 1, 1),
    _LldpXdot3PortConfigPortNum_Type()
)
lldpXdot3PortConfigPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3PortConfigPortNum.setStatus("current")


class _LldpXdot3PortConfigTLVsTxEnable_Type(Bits):
    """Custom type lldpXdot3PortConfigTLVsTxEnable based on Bits"""
    namedValues = NamedValues(
        *(("linkAggregation", 2),
          ("macPhyConfigStatus", 0),
          ("maxFrameSize", 3),
          ("powerViaMDI", 1))
    )

_LldpXdot3PortConfigTLVsTxEnable_Type.__name__ = "Bits"
_LldpXdot3PortConfigTLVsTxEnable_Object = MibTableColumn
lldpXdot3PortConfigTLVsTxEnable = _LldpXdot3PortConfigTLVsTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 1, 1, 1, 2),
    _LldpXdot3PortConfigTLVsTxEnable_Type()
)
lldpXdot3PortConfigTLVsTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot3PortConfigTLVsTxEnable.setStatus("current")
_LldpXdot3LocalData_ObjectIdentity = ObjectIdentity
lldpXdot3LocalData = _LldpXdot3LocalData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 2)
)
_LldpXdot3LocPortTable_Object = MibTable
lldpXdot3LocPortTable = _LldpXdot3LocPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 2, 1)
)
if mibBuilder.loadTexts:
    lldpXdot3LocPortTable.setStatus("current")
_LldpXdot3LocPortEntry_Object = MibTableRow
lldpXdot3LocPortEntry = _LldpXdot3LocPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 2, 1, 1)
)
lldpXdot3LocPortEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXdot3LocPortNum"),
)
if mibBuilder.loadTexts:
    lldpXdot3LocPortEntry.setStatus("current")
_LldpXdot3LocPortNum_Type = LldpPortNumber
_LldpXdot3LocPortNum_Object = MibTableColumn
lldpXdot3LocPortNum = _LldpXdot3LocPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 2, 1, 1, 1),
    _LldpXdot3LocPortNum_Type()
)
lldpXdot3LocPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocPortNum.setStatus("current")
_LldpXdot3LocPortAutoNegSupported_Type = TruthValue
_LldpXdot3LocPortAutoNegSupported_Object = MibTableColumn
lldpXdot3LocPortAutoNegSupported = _LldpXdot3LocPortAutoNegSupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 2, 1, 1, 2),
    _LldpXdot3LocPortAutoNegSupported_Type()
)
lldpXdot3LocPortAutoNegSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocPortAutoNegSupported.setStatus("current")
_LldpXdot3LocPortAutoNegEnabled_Type = TruthValue
_LldpXdot3LocPortAutoNegEnabled_Object = MibTableColumn
lldpXdot3LocPortAutoNegEnabled = _LldpXdot3LocPortAutoNegEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 2, 1, 1, 3),
    _LldpXdot3LocPortAutoNegEnabled_Type()
)
lldpXdot3LocPortAutoNegEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocPortAutoNegEnabled.setStatus("current")


class _LldpXdot3LocPortAutoNegAdvertisedCap_Type(OctetString):
    """Custom type lldpXdot3LocPortAutoNegAdvertisedCap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_LldpXdot3LocPortAutoNegAdvertisedCap_Type.__name__ = "OctetString"
_LldpXdot3LocPortAutoNegAdvertisedCap_Object = MibTableColumn
lldpXdot3LocPortAutoNegAdvertisedCap = _LldpXdot3LocPortAutoNegAdvertisedCap_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 2, 1, 1, 4),
    _LldpXdot3LocPortAutoNegAdvertisedCap_Type()
)
lldpXdot3LocPortAutoNegAdvertisedCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocPortAutoNegAdvertisedCap.setStatus("current")


class _LldpXdot3LocPortOperMauType_Type(Integer32):
    """Custom type lldpXdot3LocPortOperMauType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LldpXdot3LocPortOperMauType_Type.__name__ = "Integer32"
_LldpXdot3LocPortOperMauType_Object = MibTableColumn
lldpXdot3LocPortOperMauType = _LldpXdot3LocPortOperMauType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 2, 1, 1, 5),
    _LldpXdot3LocPortOperMauType_Type()
)
lldpXdot3LocPortOperMauType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocPortOperMauType.setStatus("current")
_LldpXdot3LocPowerTable_Object = MibTable
lldpXdot3LocPowerTable = _LldpXdot3LocPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 2, 2)
)
if mibBuilder.loadTexts:
    lldpXdot3LocPowerTable.setStatus("current")
_LldpXdot3LocPowerEntry_Object = MibTableRow
lldpXdot3LocPowerEntry = _LldpXdot3LocPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 2, 2, 1)
)
lldpXdot3LocPowerEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXdot3LocPowerPortNum"),
)
if mibBuilder.loadTexts:
    lldpXdot3LocPowerEntry.setStatus("current")
_LldpXdot3LocPowerPortNum_Type = LldpPortNumber
_LldpXdot3LocPowerPortNum_Object = MibTableColumn
lldpXdot3LocPowerPortNum = _LldpXdot3LocPowerPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 2, 2, 1, 1),
    _LldpXdot3LocPowerPortNum_Type()
)
lldpXdot3LocPowerPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocPowerPortNum.setStatus("current")
_LldpXdot3LocPowerPortClass_Type = LldpPowerPortClass
_LldpXdot3LocPowerPortClass_Object = MibTableColumn
lldpXdot3LocPowerPortClass = _LldpXdot3LocPowerPortClass_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 2, 2, 1, 2),
    _LldpXdot3LocPowerPortClass_Type()
)
lldpXdot3LocPowerPortClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocPowerPortClass.setStatus("current")
_LldpXdot3LocPowerMDISupported_Type = TruthValue
_LldpXdot3LocPowerMDISupported_Object = MibTableColumn
lldpXdot3LocPowerMDISupported = _LldpXdot3LocPowerMDISupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 2, 2, 1, 3),
    _LldpXdot3LocPowerMDISupported_Type()
)
lldpXdot3LocPowerMDISupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocPowerMDISupported.setStatus("current")
_LldpXdot3LocPowerMDIEnabled_Type = TruthValue
_LldpXdot3LocPowerMDIEnabled_Object = MibTableColumn
lldpXdot3LocPowerMDIEnabled = _LldpXdot3LocPowerMDIEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 2, 2, 1, 4),
    _LldpXdot3LocPowerMDIEnabled_Type()
)
lldpXdot3LocPowerMDIEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocPowerMDIEnabled.setStatus("current")
_LldpXdot3LocPowerPairControlable_Type = TruthValue
_LldpXdot3LocPowerPairControlable_Object = MibTableColumn
lldpXdot3LocPowerPairControlable = _LldpXdot3LocPowerPairControlable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 2, 2, 1, 5),
    _LldpXdot3LocPowerPairControlable_Type()
)
lldpXdot3LocPowerPairControlable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocPowerPairControlable.setStatus("current")


class _LldpXdot3LocPowerPairs_Type(Integer32):
    """Custom type lldpXdot3LocPowerPairs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_LldpXdot3LocPowerPairs_Type.__name__ = "Integer32"
_LldpXdot3LocPowerPairs_Object = MibTableColumn
lldpXdot3LocPowerPairs = _LldpXdot3LocPowerPairs_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 2, 2, 1, 6),
    _LldpXdot3LocPowerPairs_Type()
)
lldpXdot3LocPowerPairs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocPowerPairs.setStatus("current")


class _LldpXdot3LocPowerClass_Type(Integer32):
    """Custom type lldpXdot3LocPowerClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(5, 5),
    )


_LldpXdot3LocPowerClass_Type.__name__ = "Integer32"
_LldpXdot3LocPowerClass_Object = MibTableColumn
lldpXdot3LocPowerClass = _LldpXdot3LocPowerClass_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 2, 2, 1, 7),
    _LldpXdot3LocPowerClass_Type()
)
lldpXdot3LocPowerClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocPowerClass.setStatus("current")
_LldpXdot3LocLinkAggTable_Object = MibTable
lldpXdot3LocLinkAggTable = _LldpXdot3LocLinkAggTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 2, 3)
)
if mibBuilder.loadTexts:
    lldpXdot3LocLinkAggTable.setStatus("current")
_LldpXdot3LocLinkAggEntry_Object = MibTableRow
lldpXdot3LocLinkAggEntry = _LldpXdot3LocLinkAggEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 2, 3, 1)
)
lldpXdot3LocLinkAggEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXdot3LocLinkAggPortNum"),
)
if mibBuilder.loadTexts:
    lldpXdot3LocLinkAggEntry.setStatus("current")
_LldpXdot3LocLinkAggPortNum_Type = LldpPortNumber
_LldpXdot3LocLinkAggPortNum_Object = MibTableColumn
lldpXdot3LocLinkAggPortNum = _LldpXdot3LocLinkAggPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 2, 3, 1, 1),
    _LldpXdot3LocLinkAggPortNum_Type()
)
lldpXdot3LocLinkAggPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocLinkAggPortNum.setStatus("current")
_LldpXdot3LocLinkAggStatus_Type = LldpLinkAggStatusMap
_LldpXdot3LocLinkAggStatus_Object = MibTableColumn
lldpXdot3LocLinkAggStatus = _LldpXdot3LocLinkAggStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 2, 3, 1, 2),
    _LldpXdot3LocLinkAggStatus_Type()
)
lldpXdot3LocLinkAggStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocLinkAggStatus.setStatus("current")


class _LldpXdot3LocLinkAggPortId_Type(Integer32):
    """Custom type lldpXdot3LocLinkAggPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_LldpXdot3LocLinkAggPortId_Type.__name__ = "Integer32"
_LldpXdot3LocLinkAggPortId_Object = MibTableColumn
lldpXdot3LocLinkAggPortId = _LldpXdot3LocLinkAggPortId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 2, 3, 1, 3),
    _LldpXdot3LocLinkAggPortId_Type()
)
lldpXdot3LocLinkAggPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocLinkAggPortId.setStatus("current")
_LldpXdot3LocMaxFrameSizeTable_Object = MibTable
lldpXdot3LocMaxFrameSizeTable = _LldpXdot3LocMaxFrameSizeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 2, 4)
)
if mibBuilder.loadTexts:
    lldpXdot3LocMaxFrameSizeTable.setStatus("current")
_LldpXdot3LocMaxFrameSizeEntry_Object = MibTableRow
lldpXdot3LocMaxFrameSizeEntry = _LldpXdot3LocMaxFrameSizeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 2, 4, 1)
)
lldpXdot3LocMaxFrameSizeEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXdot3LocMaxFrameSizePortNum"),
)
if mibBuilder.loadTexts:
    lldpXdot3LocMaxFrameSizeEntry.setStatus("current")
_LldpXdot3LocMaxFrameSizePortNum_Type = LldpPortNumber
_LldpXdot3LocMaxFrameSizePortNum_Object = MibTableColumn
lldpXdot3LocMaxFrameSizePortNum = _LldpXdot3LocMaxFrameSizePortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 2, 4, 1, 1),
    _LldpXdot3LocMaxFrameSizePortNum_Type()
)
lldpXdot3LocMaxFrameSizePortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocMaxFrameSizePortNum.setStatus("current")


class _LldpXdot3LocMaxFrameSize_Type(Integer32):
    """Custom type lldpXdot3LocMaxFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LldpXdot3LocMaxFrameSize_Type.__name__ = "Integer32"
_LldpXdot3LocMaxFrameSize_Object = MibTableColumn
lldpXdot3LocMaxFrameSize = _LldpXdot3LocMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 2, 4, 1, 2),
    _LldpXdot3LocMaxFrameSize_Type()
)
lldpXdot3LocMaxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocMaxFrameSize.setStatus("current")
_LldpXdot3RemoteData_ObjectIdentity = ObjectIdentity
lldpXdot3RemoteData = _LldpXdot3RemoteData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 3)
)
_LldpXdot3RemPortTable_Object = MibTable
lldpXdot3RemPortTable = _LldpXdot3RemPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 3, 1)
)
if mibBuilder.loadTexts:
    lldpXdot3RemPortTable.setStatus("current")
_LldpXdot3RemPortEntry_Object = MibTableRow
lldpXdot3RemPortEntry = _LldpXdot3RemPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 3, 1, 1)
)
lldpXdot3RemPortEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXdot3RemTimeMark"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXdot3RemLocalPortNum"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXdot3RemIndex"),
)
if mibBuilder.loadTexts:
    lldpXdot3RemPortEntry.setStatus("current")
_LldpXdot3RemTimeMark_Type = TimeFilter
_LldpXdot3RemTimeMark_Object = MibTableColumn
lldpXdot3RemTimeMark = _LldpXdot3RemTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 3, 1, 1, 1),
    _LldpXdot3RemTimeMark_Type()
)
lldpXdot3RemTimeMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemTimeMark.setStatus("current")
_LldpXdot3RemLocalPortNum_Type = LldpPortNumber
_LldpXdot3RemLocalPortNum_Object = MibTableColumn
lldpXdot3RemLocalPortNum = _LldpXdot3RemLocalPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 3, 1, 1, 2),
    _LldpXdot3RemLocalPortNum_Type()
)
lldpXdot3RemLocalPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemLocalPortNum.setStatus("current")


class _LldpXdot3RemIndex_Type(Integer32):
    """Custom type lldpXdot3RemIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpXdot3RemIndex_Type.__name__ = "Integer32"
_LldpXdot3RemIndex_Object = MibTableColumn
lldpXdot3RemIndex = _LldpXdot3RemIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 3, 1, 1, 3),
    _LldpXdot3RemIndex_Type()
)
lldpXdot3RemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemIndex.setStatus("current")
_LldpXdot3RemPortAutoNegSupported_Type = TruthValue
_LldpXdot3RemPortAutoNegSupported_Object = MibTableColumn
lldpXdot3RemPortAutoNegSupported = _LldpXdot3RemPortAutoNegSupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 3, 1, 1, 4),
    _LldpXdot3RemPortAutoNegSupported_Type()
)
lldpXdot3RemPortAutoNegSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemPortAutoNegSupported.setStatus("current")
_LldpXdot3RemPortAutoNegEnabled_Type = TruthValue
_LldpXdot3RemPortAutoNegEnabled_Object = MibTableColumn
lldpXdot3RemPortAutoNegEnabled = _LldpXdot3RemPortAutoNegEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 3, 1, 1, 5),
    _LldpXdot3RemPortAutoNegEnabled_Type()
)
lldpXdot3RemPortAutoNegEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemPortAutoNegEnabled.setStatus("current")


class _LldpXdot3RemPortAutoNegAdvertisedCap_Type(OctetString):
    """Custom type lldpXdot3RemPortAutoNegAdvertisedCap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_LldpXdot3RemPortAutoNegAdvertisedCap_Type.__name__ = "OctetString"
_LldpXdot3RemPortAutoNegAdvertisedCap_Object = MibTableColumn
lldpXdot3RemPortAutoNegAdvertisedCap = _LldpXdot3RemPortAutoNegAdvertisedCap_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 3, 1, 1, 6),
    _LldpXdot3RemPortAutoNegAdvertisedCap_Type()
)
lldpXdot3RemPortAutoNegAdvertisedCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemPortAutoNegAdvertisedCap.setStatus("current")


class _LldpXdot3RemPortOperMauType_Type(Integer32):
    """Custom type lldpXdot3RemPortOperMauType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LldpXdot3RemPortOperMauType_Type.__name__ = "Integer32"
_LldpXdot3RemPortOperMauType_Object = MibTableColumn
lldpXdot3RemPortOperMauType = _LldpXdot3RemPortOperMauType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 3, 1, 1, 7),
    _LldpXdot3RemPortOperMauType_Type()
)
lldpXdot3RemPortOperMauType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemPortOperMauType.setStatus("current")
_LldpXdot3RemPowerTable_Object = MibTable
lldpXdot3RemPowerTable = _LldpXdot3RemPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 3, 2)
)
if mibBuilder.loadTexts:
    lldpXdot3RemPowerTable.setStatus("current")
_LldpXdot3RemPowerEntry_Object = MibTableRow
lldpXdot3RemPowerEntry = _LldpXdot3RemPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 3, 2, 1)
)
lldpXdot3RemPowerEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXdot3RemPowerTimeMark"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXdot3RemPowerLocalPortNum"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXdot3RemPowerIndex"),
)
if mibBuilder.loadTexts:
    lldpXdot3RemPowerEntry.setStatus("current")
_LldpXdot3RemPowerTimeMark_Type = TimeFilter
_LldpXdot3RemPowerTimeMark_Object = MibTableColumn
lldpXdot3RemPowerTimeMark = _LldpXdot3RemPowerTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 3, 2, 1, 1),
    _LldpXdot3RemPowerTimeMark_Type()
)
lldpXdot3RemPowerTimeMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemPowerTimeMark.setStatus("current")
_LldpXdot3RemPowerLocalPortNum_Type = LldpPortNumber
_LldpXdot3RemPowerLocalPortNum_Object = MibTableColumn
lldpXdot3RemPowerLocalPortNum = _LldpXdot3RemPowerLocalPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 3, 2, 1, 2),
    _LldpXdot3RemPowerLocalPortNum_Type()
)
lldpXdot3RemPowerLocalPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemPowerLocalPortNum.setStatus("current")


class _LldpXdot3RemPowerIndex_Type(Integer32):
    """Custom type lldpXdot3RemPowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpXdot3RemPowerIndex_Type.__name__ = "Integer32"
_LldpXdot3RemPowerIndex_Object = MibTableColumn
lldpXdot3RemPowerIndex = _LldpXdot3RemPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 3, 2, 1, 3),
    _LldpXdot3RemPowerIndex_Type()
)
lldpXdot3RemPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemPowerIndex.setStatus("current")
_LldpXdot3RemPowerPortClass_Type = LldpPowerPortClass
_LldpXdot3RemPowerPortClass_Object = MibTableColumn
lldpXdot3RemPowerPortClass = _LldpXdot3RemPowerPortClass_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 3, 2, 1, 4),
    _LldpXdot3RemPowerPortClass_Type()
)
lldpXdot3RemPowerPortClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemPowerPortClass.setStatus("current")
_LldpXdot3RemPowerMDISupported_Type = TruthValue
_LldpXdot3RemPowerMDISupported_Object = MibTableColumn
lldpXdot3RemPowerMDISupported = _LldpXdot3RemPowerMDISupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 3, 2, 1, 5),
    _LldpXdot3RemPowerMDISupported_Type()
)
lldpXdot3RemPowerMDISupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemPowerMDISupported.setStatus("current")
_LldpXdot3RemPowerMDIEnabled_Type = TruthValue
_LldpXdot3RemPowerMDIEnabled_Object = MibTableColumn
lldpXdot3RemPowerMDIEnabled = _LldpXdot3RemPowerMDIEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 3, 2, 1, 6),
    _LldpXdot3RemPowerMDIEnabled_Type()
)
lldpXdot3RemPowerMDIEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemPowerMDIEnabled.setStatus("current")
_LldpXdot3RemPowerPairControlable_Type = TruthValue
_LldpXdot3RemPowerPairControlable_Object = MibTableColumn
lldpXdot3RemPowerPairControlable = _LldpXdot3RemPowerPairControlable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 3, 2, 1, 7),
    _LldpXdot3RemPowerPairControlable_Type()
)
lldpXdot3RemPowerPairControlable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemPowerPairControlable.setStatus("current")


class _LldpXdot3RemPowerPairs_Type(Integer32):
    """Custom type lldpXdot3RemPowerPairs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_LldpXdot3RemPowerPairs_Type.__name__ = "Integer32"
_LldpXdot3RemPowerPairs_Object = MibTableColumn
lldpXdot3RemPowerPairs = _LldpXdot3RemPowerPairs_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 3, 2, 1, 8),
    _LldpXdot3RemPowerPairs_Type()
)
lldpXdot3RemPowerPairs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemPowerPairs.setStatus("current")


class _LldpXdot3RemPowerClass_Type(Integer32):
    """Custom type lldpXdot3RemPowerClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(5, 5),
    )


_LldpXdot3RemPowerClass_Type.__name__ = "Integer32"
_LldpXdot3RemPowerClass_Object = MibTableColumn
lldpXdot3RemPowerClass = _LldpXdot3RemPowerClass_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 3, 2, 1, 9),
    _LldpXdot3RemPowerClass_Type()
)
lldpXdot3RemPowerClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemPowerClass.setStatus("current")
_LldpXdot3RemLinkAggTable_Object = MibTable
lldpXdot3RemLinkAggTable = _LldpXdot3RemLinkAggTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 3, 3)
)
if mibBuilder.loadTexts:
    lldpXdot3RemLinkAggTable.setStatus("current")
_LldpXdot3RemLinkAggEntry_Object = MibTableRow
lldpXdot3RemLinkAggEntry = _LldpXdot3RemLinkAggEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 3, 3, 1)
)
lldpXdot3RemLinkAggEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXdot3RemLinkAggTimeMark"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXdot3RemLinkAggLocalPortNum"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXdot3RemLinkAggIndex"),
)
if mibBuilder.loadTexts:
    lldpXdot3RemLinkAggEntry.setStatus("current")
_LldpXdot3RemLinkAggTimeMark_Type = TimeFilter
_LldpXdot3RemLinkAggTimeMark_Object = MibTableColumn
lldpXdot3RemLinkAggTimeMark = _LldpXdot3RemLinkAggTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 3, 3, 1, 1),
    _LldpXdot3RemLinkAggTimeMark_Type()
)
lldpXdot3RemLinkAggTimeMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemLinkAggTimeMark.setStatus("current")
_LldpXdot3RemLinkAggLocalPortNum_Type = LldpPortNumber
_LldpXdot3RemLinkAggLocalPortNum_Object = MibTableColumn
lldpXdot3RemLinkAggLocalPortNum = _LldpXdot3RemLinkAggLocalPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 3, 3, 1, 2),
    _LldpXdot3RemLinkAggLocalPortNum_Type()
)
lldpXdot3RemLinkAggLocalPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemLinkAggLocalPortNum.setStatus("current")


class _LldpXdot3RemLinkAggIndex_Type(Integer32):
    """Custom type lldpXdot3RemLinkAggIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpXdot3RemLinkAggIndex_Type.__name__ = "Integer32"
_LldpXdot3RemLinkAggIndex_Object = MibTableColumn
lldpXdot3RemLinkAggIndex = _LldpXdot3RemLinkAggIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 3, 3, 1, 3),
    _LldpXdot3RemLinkAggIndex_Type()
)
lldpXdot3RemLinkAggIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemLinkAggIndex.setStatus("current")
_LldpXdot3RemLinkAggStatus_Type = LldpLinkAggStatusMap
_LldpXdot3RemLinkAggStatus_Object = MibTableColumn
lldpXdot3RemLinkAggStatus = _LldpXdot3RemLinkAggStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 3, 3, 1, 4),
    _LldpXdot3RemLinkAggStatus_Type()
)
lldpXdot3RemLinkAggStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemLinkAggStatus.setStatus("current")


class _LldpXdot3RemLinkAggPortId_Type(Integer32):
    """Custom type lldpXdot3RemLinkAggPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_LldpXdot3RemLinkAggPortId_Type.__name__ = "Integer32"
_LldpXdot3RemLinkAggPortId_Object = MibTableColumn
lldpXdot3RemLinkAggPortId = _LldpXdot3RemLinkAggPortId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 3, 3, 1, 5),
    _LldpXdot3RemLinkAggPortId_Type()
)
lldpXdot3RemLinkAggPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemLinkAggPortId.setStatus("current")
_LldpXdot3RemMaxFrameSizeTable_Object = MibTable
lldpXdot3RemMaxFrameSizeTable = _LldpXdot3RemMaxFrameSizeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 3, 4)
)
if mibBuilder.loadTexts:
    lldpXdot3RemMaxFrameSizeTable.setStatus("current")
_LldpXdot3RemMaxFrameSizeEntry_Object = MibTableRow
lldpXdot3RemMaxFrameSizeEntry = _LldpXdot3RemMaxFrameSizeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 3, 4, 1)
)
lldpXdot3RemMaxFrameSizeEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXdot3RemMaxFrameSizeTimeMark"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXdot3RemMaxFrameSizeLocalPortNum"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXdot3RemMaxFrameSizeIndex"),
)
if mibBuilder.loadTexts:
    lldpXdot3RemMaxFrameSizeEntry.setStatus("current")
_LldpXdot3RemMaxFrameSizeTimeMark_Type = TimeFilter
_LldpXdot3RemMaxFrameSizeTimeMark_Object = MibTableColumn
lldpXdot3RemMaxFrameSizeTimeMark = _LldpXdot3RemMaxFrameSizeTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 3, 4, 1, 1),
    _LldpXdot3RemMaxFrameSizeTimeMark_Type()
)
lldpXdot3RemMaxFrameSizeTimeMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemMaxFrameSizeTimeMark.setStatus("current")
_LldpXdot3RemMaxFrameSizeLocalPortNum_Type = LldpPortNumber
_LldpXdot3RemMaxFrameSizeLocalPortNum_Object = MibTableColumn
lldpXdot3RemMaxFrameSizeLocalPortNum = _LldpXdot3RemMaxFrameSizeLocalPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 3, 4, 1, 2),
    _LldpXdot3RemMaxFrameSizeLocalPortNum_Type()
)
lldpXdot3RemMaxFrameSizeLocalPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemMaxFrameSizeLocalPortNum.setStatus("current")


class _LldpXdot3RemMaxFrameSizeIndex_Type(Integer32):
    """Custom type lldpXdot3RemMaxFrameSizeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpXdot3RemMaxFrameSizeIndex_Type.__name__ = "Integer32"
_LldpXdot3RemMaxFrameSizeIndex_Object = MibTableColumn
lldpXdot3RemMaxFrameSizeIndex = _LldpXdot3RemMaxFrameSizeIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 3, 4, 1, 3),
    _LldpXdot3RemMaxFrameSizeIndex_Type()
)
lldpXdot3RemMaxFrameSizeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemMaxFrameSizeIndex.setStatus("current")


class _LldpXdot3RemMaxFrameSize_Type(Integer32):
    """Custom type lldpXdot3RemMaxFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LldpXdot3RemMaxFrameSize_Type.__name__ = "Integer32"
_LldpXdot3RemMaxFrameSize_Object = MibTableColumn
lldpXdot3RemMaxFrameSize = _LldpXdot3RemMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 14, 3, 4, 1, 4),
    _LldpXdot3RemMaxFrameSize_Type()
)
lldpXdot3RemMaxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemMaxFrameSize.setStatus("current")
_LldpStatistics_ObjectIdentity = ObjectIdentity
lldpStatistics = _LldpStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 15)
)
_LldpStatsRemTablesLastChangeTime_Type = TimeStamp
_LldpStatsRemTablesLastChangeTime_Object = MibScalar
lldpStatsRemTablesLastChangeTime = _LldpStatsRemTablesLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 15, 1),
    _LldpStatsRemTablesLastChangeTime_Type()
)
lldpStatsRemTablesLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpStatsRemTablesLastChangeTime.setStatus("current")
_LldpStatsRemTablesInserts_Type = ZeroBasedCounter32
_LldpStatsRemTablesInserts_Object = MibScalar
lldpStatsRemTablesInserts = _LldpStatsRemTablesInserts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 15, 2),
    _LldpStatsRemTablesInserts_Type()
)
lldpStatsRemTablesInserts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpStatsRemTablesInserts.setStatus("current")
if mibBuilder.loadTexts:
    lldpStatsRemTablesInserts.setUnits("table entries")
_LldpStatsRemTablesDeletes_Type = ZeroBasedCounter32
_LldpStatsRemTablesDeletes_Object = MibScalar
lldpStatsRemTablesDeletes = _LldpStatsRemTablesDeletes_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 15, 3),
    _LldpStatsRemTablesDeletes_Type()
)
lldpStatsRemTablesDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpStatsRemTablesDeletes.setStatus("current")
if mibBuilder.loadTexts:
    lldpStatsRemTablesDeletes.setUnits("table entries")
_LldpStatsRemTablesDrops_Type = ZeroBasedCounter32
_LldpStatsRemTablesDrops_Object = MibScalar
lldpStatsRemTablesDrops = _LldpStatsRemTablesDrops_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 15, 4),
    _LldpStatsRemTablesDrops_Type()
)
lldpStatsRemTablesDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpStatsRemTablesDrops.setStatus("current")
if mibBuilder.loadTexts:
    lldpStatsRemTablesDrops.setUnits("table entries")
_LldpStatsRemTablesAgeouts_Type = ZeroBasedCounter32
_LldpStatsRemTablesAgeouts_Object = MibScalar
lldpStatsRemTablesAgeouts = _LldpStatsRemTablesAgeouts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 15, 5),
    _LldpStatsRemTablesAgeouts_Type()
)
lldpStatsRemTablesAgeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpStatsRemTablesAgeouts.setStatus("current")
_LldpStatsTxPortTable_Object = MibTable
lldpStatsTxPortTable = _LldpStatsTxPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 15, 6)
)
if mibBuilder.loadTexts:
    lldpStatsTxPortTable.setStatus("current")
_LldpStatsTxPortEntry_Object = MibTableRow
lldpStatsTxPortEntry = _LldpStatsTxPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 15, 6, 1)
)
lldpStatsTxPortEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpStatsTxPortNum"),
)
if mibBuilder.loadTexts:
    lldpStatsTxPortEntry.setStatus("current")
_LldpStatsTxPortNum_Type = LldpPortNumber
_LldpStatsTxPortNum_Object = MibTableColumn
lldpStatsTxPortNum = _LldpStatsTxPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 15, 6, 1, 1),
    _LldpStatsTxPortNum_Type()
)
lldpStatsTxPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpStatsTxPortNum.setStatus("current")
_LldpStatsTxPortFramesTotal_Type = Counter32
_LldpStatsTxPortFramesTotal_Object = MibTableColumn
lldpStatsTxPortFramesTotal = _LldpStatsTxPortFramesTotal_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 15, 6, 1, 2),
    _LldpStatsTxPortFramesTotal_Type()
)
lldpStatsTxPortFramesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpStatsTxPortFramesTotal.setStatus("current")
_LldpRxStatsPortTable_Object = MibTable
lldpRxStatsPortTable = _LldpRxStatsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 15, 7)
)
if mibBuilder.loadTexts:
    lldpRxStatsPortTable.setStatus("current")
_LldpRxStatsPortEntry_Object = MibTableRow
lldpRxStatsPortEntry = _LldpRxStatsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 15, 7, 1)
)
lldpRxStatsPortEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpStatsRxPortNum"),
)
if mibBuilder.loadTexts:
    lldpRxStatsPortEntry.setStatus("current")
_LldpStatsRxPortNum_Type = LldpPortNumber
_LldpStatsRxPortNum_Object = MibTableColumn
lldpStatsRxPortNum = _LldpStatsRxPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 15, 7, 1, 1),
    _LldpStatsRxPortNum_Type()
)
lldpStatsRxPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpStatsRxPortNum.setStatus("current")
_LldpStatsRxPortFramesDiscardedTotal_Type = Counter32
_LldpStatsRxPortFramesDiscardedTotal_Object = MibTableColumn
lldpStatsRxPortFramesDiscardedTotal = _LldpStatsRxPortFramesDiscardedTotal_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 15, 7, 1, 2),
    _LldpStatsRxPortFramesDiscardedTotal_Type()
)
lldpStatsRxPortFramesDiscardedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpStatsRxPortFramesDiscardedTotal.setStatus("current")
_LldpStatsRxPortFramesErrors_Type = Counter32
_LldpStatsRxPortFramesErrors_Object = MibTableColumn
lldpStatsRxPortFramesErrors = _LldpStatsRxPortFramesErrors_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 15, 7, 1, 3),
    _LldpStatsRxPortFramesErrors_Type()
)
lldpStatsRxPortFramesErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpStatsRxPortFramesErrors.setStatus("current")
_LldpStatsRxPortFramesTotal_Type = Counter32
_LldpStatsRxPortFramesTotal_Object = MibTableColumn
lldpStatsRxPortFramesTotal = _LldpStatsRxPortFramesTotal_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 15, 7, 1, 4),
    _LldpStatsRxPortFramesTotal_Type()
)
lldpStatsRxPortFramesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpStatsRxPortFramesTotal.setStatus("current")
_LldpStatsRxPortTLVsDiscardedTotal_Type = Counter32
_LldpStatsRxPortTLVsDiscardedTotal_Object = MibTableColumn
lldpStatsRxPortTLVsDiscardedTotal = _LldpStatsRxPortTLVsDiscardedTotal_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 15, 7, 1, 5),
    _LldpStatsRxPortTLVsDiscardedTotal_Type()
)
lldpStatsRxPortTLVsDiscardedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpStatsRxPortTLVsDiscardedTotal.setStatus("current")
_LldpStatsRxPortTLVsUnrecognizedTotal_Type = Counter32
_LldpStatsRxPortTLVsUnrecognizedTotal_Object = MibTableColumn
lldpStatsRxPortTLVsUnrecognizedTotal = _LldpStatsRxPortTLVsUnrecognizedTotal_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 15, 7, 1, 6),
    _LldpStatsRxPortTLVsUnrecognizedTotal_Type()
)
lldpStatsRxPortTLVsUnrecognizedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpStatsRxPortTLVsUnrecognizedTotal.setStatus("current")
_LldpStatsRxPortAgeoutsTotal_Type = ZeroBasedCounter32
_LldpStatsRxPortAgeoutsTotal_Object = MibTableColumn
lldpStatsRxPortAgeoutsTotal = _LldpStatsRxPortAgeoutsTotal_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 15, 7, 1, 7),
    _LldpStatsRxPortAgeoutsTotal_Type()
)
lldpStatsRxPortAgeoutsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpStatsRxPortAgeoutsTotal.setStatus("current")
_LldpStatsRemTablesClear_Type = Integer32
_LldpStatsRemTablesClear_Object = MibScalar
lldpStatsRemTablesClear = _LldpStatsRemTablesClear_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 15, 8),
    _LldpStatsRemTablesClear_Type()
)
lldpStatsRemTablesClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpStatsRemTablesClear.setStatus("current")
_LldpLocalSystemData_ObjectIdentity = ObjectIdentity
lldpLocalSystemData = _LldpLocalSystemData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 16)
)
_LldpLocChassisIdSubtype_Type = LldpChassisIdSubtype
_LldpLocChassisIdSubtype_Object = MibScalar
lldpLocChassisIdSubtype = _LldpLocChassisIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 16, 1),
    _LldpLocChassisIdSubtype_Type()
)
lldpLocChassisIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocChassisIdSubtype.setStatus("current")
_LldpLocChassisId_Type = LldpChassisId
_LldpLocChassisId_Object = MibScalar
lldpLocChassisId = _LldpLocChassisId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 16, 2),
    _LldpLocChassisId_Type()
)
lldpLocChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocChassisId.setStatus("current")


class _LldpLocSysName_Type(SnmpAdminString):
    """Custom type lldpLocSysName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpLocSysName_Type.__name__ = "SnmpAdminString"
_LldpLocSysName_Object = MibScalar
lldpLocSysName = _LldpLocSysName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 16, 3),
    _LldpLocSysName_Type()
)
lldpLocSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocSysName.setStatus("current")


class _LldpLocSysDesc_Type(SnmpAdminString):
    """Custom type lldpLocSysDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpLocSysDesc_Type.__name__ = "SnmpAdminString"
_LldpLocSysDesc_Object = MibScalar
lldpLocSysDesc = _LldpLocSysDesc_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 16, 4),
    _LldpLocSysDesc_Type()
)
lldpLocSysDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocSysDesc.setStatus("current")
_LldpLocSysCapSupported_Type = LldpSystemCapabilitiesMap
_LldpLocSysCapSupported_Object = MibScalar
lldpLocSysCapSupported = _LldpLocSysCapSupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 16, 5),
    _LldpLocSysCapSupported_Type()
)
lldpLocSysCapSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocSysCapSupported.setStatus("current")
_LldpLocSysCapEnabled_Type = LldpSystemCapabilitiesMap
_LldpLocSysCapEnabled_Object = MibScalar
lldpLocSysCapEnabled = _LldpLocSysCapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 16, 6),
    _LldpLocSysCapEnabled_Type()
)
lldpLocSysCapEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocSysCapEnabled.setStatus("current")
_LldpLocPortTable_Object = MibTable
lldpLocPortTable = _LldpLocPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 16, 7)
)
if mibBuilder.loadTexts:
    lldpLocPortTable.setStatus("current")
_LldpLocPortEntry_Object = MibTableRow
lldpLocPortEntry = _LldpLocPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 16, 7, 1)
)
lldpLocPortEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpLocPortNum"),
)
if mibBuilder.loadTexts:
    lldpLocPortEntry.setStatus("current")
_LldpLocPortNum_Type = LldpPortNumber
_LldpLocPortNum_Object = MibTableColumn
lldpLocPortNum = _LldpLocPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 16, 7, 1, 1),
    _LldpLocPortNum_Type()
)
lldpLocPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocPortNum.setStatus("current")


class _LldpLocPortIdSubtype_Type(Integer32):
    """Custom type lldpLocPortIdSubtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("macAddress", 2))
    )


_LldpLocPortIdSubtype_Type.__name__ = "Integer32"
_LldpLocPortIdSubtype_Object = MibTableColumn
lldpLocPortIdSubtype = _LldpLocPortIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 16, 7, 1, 2),
    _LldpLocPortIdSubtype_Type()
)
lldpLocPortIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocPortIdSubtype.setStatus("current")
_LldpLocPortId_Type = OctetString
_LldpLocPortId_Object = MibTableColumn
lldpLocPortId = _LldpLocPortId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 16, 7, 1, 3),
    _LldpLocPortId_Type()
)
lldpLocPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocPortId.setStatus("current")


class _LldpLocPortDesc_Type(SnmpAdminString):
    """Custom type lldpLocPortDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpLocPortDesc_Type.__name__ = "SnmpAdminString"
_LldpLocPortDesc_Object = MibTableColumn
lldpLocPortDesc = _LldpLocPortDesc_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 16, 7, 1, 4),
    _LldpLocPortDesc_Type()
)
lldpLocPortDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocPortDesc.setStatus("current")
_LldpLocManAddrTable_Object = MibTable
lldpLocManAddrTable = _LldpLocManAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 16, 8)
)
if mibBuilder.loadTexts:
    lldpLocManAddrTable.setStatus("current")
_LldpLocManAddrEntry_Object = MibTableRow
lldpLocManAddrEntry = _LldpLocManAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 16, 8, 1)
)
lldpLocManAddrEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpLocManAddrSubtype"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpLocManAddr"),
)
if mibBuilder.loadTexts:
    lldpLocManAddrEntry.setStatus("current")
_LldpLocManAddrSubtype_Type = AddressFamilyNumbers
_LldpLocManAddrSubtype_Object = MibTableColumn
lldpLocManAddrSubtype = _LldpLocManAddrSubtype_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 16, 8, 1, 1),
    _LldpLocManAddrSubtype_Type()
)
lldpLocManAddrSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocManAddrSubtype.setStatus("current")
_LldpLocManAddr_Type = InetAddress
_LldpLocManAddr_Object = MibTableColumn
lldpLocManAddr = _LldpLocManAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 16, 8, 1, 2),
    _LldpLocManAddr_Type()
)
lldpLocManAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocManAddr.setStatus("current")
_LldpLocManAddrLen_Type = Integer32
_LldpLocManAddrLen_Object = MibTableColumn
lldpLocManAddrLen = _LldpLocManAddrLen_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 16, 8, 1, 3),
    _LldpLocManAddrLen_Type()
)
lldpLocManAddrLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocManAddrLen.setStatus("current")
_LldpLocManAddrIfSubtype_Type = LldpManAddrIfSubtype
_LldpLocManAddrIfSubtype_Object = MibTableColumn
lldpLocManAddrIfSubtype = _LldpLocManAddrIfSubtype_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 16, 8, 1, 4),
    _LldpLocManAddrIfSubtype_Type()
)
lldpLocManAddrIfSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocManAddrIfSubtype.setStatus("current")
_LldpLocManAddrIfId_Type = Integer32
_LldpLocManAddrIfId_Object = MibTableColumn
lldpLocManAddrIfId = _LldpLocManAddrIfId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 16, 8, 1, 5),
    _LldpLocManAddrIfId_Type()
)
lldpLocManAddrIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocManAddrIfId.setStatus("current")
_LldpLocManAddrOID_Type = ObjectIdentifier
_LldpLocManAddrOID_Object = MibTableColumn
lldpLocManAddrOID = _LldpLocManAddrOID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 16, 8, 1, 6),
    _LldpLocManAddrOID_Type()
)
lldpLocManAddrOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocManAddrOID.setStatus("current")
_LldpRemoteSystemsData_ObjectIdentity = ObjectIdentity
lldpRemoteSystemsData = _LldpRemoteSystemsData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 17)
)
_LldpRemTable_Object = MibTable
lldpRemTable = _LldpRemTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 17, 1)
)
if mibBuilder.loadTexts:
    lldpRemTable.setStatus("current")
_LldpRemEntry_Object = MibTableRow
lldpRemEntry = _LldpRemEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 17, 1, 1)
)
lldpRemEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpRemTimeMark"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpRemLocalPortNum"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpRemIndex"),
)
if mibBuilder.loadTexts:
    lldpRemEntry.setStatus("current")
_LldpRemTimeMark_Type = TimeFilter
_LldpRemTimeMark_Object = MibTableColumn
lldpRemTimeMark = _LldpRemTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 17, 1, 1, 1),
    _LldpRemTimeMark_Type()
)
lldpRemTimeMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemTimeMark.setStatus("current")
_LldpRemLocalPortNum_Type = LldpPortNumber
_LldpRemLocalPortNum_Object = MibTableColumn
lldpRemLocalPortNum = _LldpRemLocalPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 17, 1, 1, 2),
    _LldpRemLocalPortNum_Type()
)
lldpRemLocalPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemLocalPortNum.setStatus("current")


class _LldpRemIndex_Type(Integer32):
    """Custom type lldpRemIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpRemIndex_Type.__name__ = "Integer32"
_LldpRemIndex_Object = MibTableColumn
lldpRemIndex = _LldpRemIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 17, 1, 1, 3),
    _LldpRemIndex_Type()
)
lldpRemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemIndex.setStatus("current")
_LldpRemChassisIdSubtype_Type = LldpChassisIdSubtype
_LldpRemChassisIdSubtype_Object = MibTableColumn
lldpRemChassisIdSubtype = _LldpRemChassisIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 17, 1, 1, 4),
    _LldpRemChassisIdSubtype_Type()
)
lldpRemChassisIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemChassisIdSubtype.setStatus("current")
_LldpRemChassisId_Type = LldpChassisId
_LldpRemChassisId_Object = MibTableColumn
lldpRemChassisId = _LldpRemChassisId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 17, 1, 1, 5),
    _LldpRemChassisId_Type()
)
lldpRemChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemChassisId.setStatus("current")
_LldpRemPortIdSubtype_Type = LldpPortIdSubtype
_LldpRemPortIdSubtype_Object = MibTableColumn
lldpRemPortIdSubtype = _LldpRemPortIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 17, 1, 1, 6),
    _LldpRemPortIdSubtype_Type()
)
lldpRemPortIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemPortIdSubtype.setStatus("current")
_LldpRemPortId_Type = LldpPortId
_LldpRemPortId_Object = MibTableColumn
lldpRemPortId = _LldpRemPortId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 17, 1, 1, 7),
    _LldpRemPortId_Type()
)
lldpRemPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemPortId.setStatus("current")


class _LldpRemPortDesc_Type(SnmpAdminString):
    """Custom type lldpRemPortDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpRemPortDesc_Type.__name__ = "SnmpAdminString"
_LldpRemPortDesc_Object = MibTableColumn
lldpRemPortDesc = _LldpRemPortDesc_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 17, 1, 1, 8),
    _LldpRemPortDesc_Type()
)
lldpRemPortDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemPortDesc.setStatus("current")


class _LldpRemSysName_Type(SnmpAdminString):
    """Custom type lldpRemSysName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpRemSysName_Type.__name__ = "SnmpAdminString"
_LldpRemSysName_Object = MibTableColumn
lldpRemSysName = _LldpRemSysName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 17, 1, 1, 9),
    _LldpRemSysName_Type()
)
lldpRemSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemSysName.setStatus("current")


class _LldpRemSysDesc_Type(SnmpAdminString):
    """Custom type lldpRemSysDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpRemSysDesc_Type.__name__ = "SnmpAdminString"
_LldpRemSysDesc_Object = MibTableColumn
lldpRemSysDesc = _LldpRemSysDesc_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 17, 1, 1, 10),
    _LldpRemSysDesc_Type()
)
lldpRemSysDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemSysDesc.setStatus("current")
_LldpRemSysCapSupported_Type = LldpSystemCapabilitiesMap
_LldpRemSysCapSupported_Object = MibTableColumn
lldpRemSysCapSupported = _LldpRemSysCapSupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 17, 1, 1, 11),
    _LldpRemSysCapSupported_Type()
)
lldpRemSysCapSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemSysCapSupported.setStatus("current")
_LldpRemSysCapEnabled_Type = LldpSystemCapabilitiesMap
_LldpRemSysCapEnabled_Object = MibTableColumn
lldpRemSysCapEnabled = _LldpRemSysCapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 17, 1, 1, 12),
    _LldpRemSysCapEnabled_Type()
)
lldpRemSysCapEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemSysCapEnabled.setStatus("current")
_LldpRemManAddrTable_Object = MibTable
lldpRemManAddrTable = _LldpRemManAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 17, 2)
)
if mibBuilder.loadTexts:
    lldpRemManAddrTable.setStatus("current")
_LldpRemManAddrEntry_Object = MibTableRow
lldpRemManAddrEntry = _LldpRemManAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 17, 2, 1)
)
lldpRemManAddrEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpRemManTimeMark"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpRemManLocalPortNum"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpRemManIndex"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpRemManAddrSubtype"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpRemManAddr"),
)
if mibBuilder.loadTexts:
    lldpRemManAddrEntry.setStatus("current")
_LldpRemManTimeMark_Type = TimeFilter
_LldpRemManTimeMark_Object = MibTableColumn
lldpRemManTimeMark = _LldpRemManTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 17, 2, 1, 1),
    _LldpRemManTimeMark_Type()
)
lldpRemManTimeMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemManTimeMark.setStatus("current")
_LldpRemManLocalPortNum_Type = LldpPortNumber
_LldpRemManLocalPortNum_Object = MibTableColumn
lldpRemManLocalPortNum = _LldpRemManLocalPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 17, 2, 1, 2),
    _LldpRemManLocalPortNum_Type()
)
lldpRemManLocalPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemManLocalPortNum.setStatus("current")


class _LldpRemManIndex_Type(Integer32):
    """Custom type lldpRemManIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpRemManIndex_Type.__name__ = "Integer32"
_LldpRemManIndex_Object = MibTableColumn
lldpRemManIndex = _LldpRemManIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 17, 2, 1, 3),
    _LldpRemManIndex_Type()
)
lldpRemManIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemManIndex.setStatus("current")
_LldpRemManAddrSubtype_Type = AddressFamilyNumbers
_LldpRemManAddrSubtype_Object = MibTableColumn
lldpRemManAddrSubtype = _LldpRemManAddrSubtype_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 17, 2, 1, 4),
    _LldpRemManAddrSubtype_Type()
)
lldpRemManAddrSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemManAddrSubtype.setStatus("current")
_LldpRemManAddr_Type = InetAddress
_LldpRemManAddr_Object = MibTableColumn
lldpRemManAddr = _LldpRemManAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 17, 2, 1, 5),
    _LldpRemManAddr_Type()
)
lldpRemManAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemManAddr.setStatus("current")
_LldpRemManAddrIfSubtype_Type = LldpManAddrIfSubtype
_LldpRemManAddrIfSubtype_Object = MibTableColumn
lldpRemManAddrIfSubtype = _LldpRemManAddrIfSubtype_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 17, 2, 1, 6),
    _LldpRemManAddrIfSubtype_Type()
)
lldpRemManAddrIfSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemManAddrIfSubtype.setStatus("current")
_LldpRemManAddrIfId_Type = Integer32
_LldpRemManAddrIfId_Object = MibTableColumn
lldpRemManAddrIfId = _LldpRemManAddrIfId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 17, 2, 1, 7),
    _LldpRemManAddrIfId_Type()
)
lldpRemManAddrIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemManAddrIfId.setStatus("current")
_LldpRemManAddrOID_Type = ObjectIdentifier
_LldpRemManAddrOID_Object = MibTableColumn
lldpRemManAddrOID = _LldpRemManAddrOID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 17, 2, 1, 8),
    _LldpRemManAddrOID_Type()
)
lldpRemManAddrOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemManAddrOID.setStatus("current")
_LldpRemUnknownTLVTable_Object = MibTable
lldpRemUnknownTLVTable = _LldpRemUnknownTLVTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 17, 3)
)
if mibBuilder.loadTexts:
    lldpRemUnknownTLVTable.setStatus("current")
_LldpRemUnknownTLVEntry_Object = MibTableRow
lldpRemUnknownTLVEntry = _LldpRemUnknownTLVEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 17, 3, 1)
)
lldpRemUnknownTLVEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpRemUnknownTimeMark"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpRemUnknownLocalPortNum"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpRemUnknownIndex"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpRemUnknownTLVType"),
)
if mibBuilder.loadTexts:
    lldpRemUnknownTLVEntry.setStatus("current")
_LldpRemUnknownTimeMark_Type = TimeFilter
_LldpRemUnknownTimeMark_Object = MibTableColumn
lldpRemUnknownTimeMark = _LldpRemUnknownTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 17, 3, 1, 1),
    _LldpRemUnknownTimeMark_Type()
)
lldpRemUnknownTimeMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemUnknownTimeMark.setStatus("current")
_LldpRemUnknownLocalPortNum_Type = LldpPortNumber
_LldpRemUnknownLocalPortNum_Object = MibTableColumn
lldpRemUnknownLocalPortNum = _LldpRemUnknownLocalPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 17, 3, 1, 2),
    _LldpRemUnknownLocalPortNum_Type()
)
lldpRemUnknownLocalPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemUnknownLocalPortNum.setStatus("current")


class _LldpRemUnknownIndex_Type(Integer32):
    """Custom type lldpRemUnknownIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpRemUnknownIndex_Type.__name__ = "Integer32"
_LldpRemUnknownIndex_Object = MibTableColumn
lldpRemUnknownIndex = _LldpRemUnknownIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 17, 3, 1, 3),
    _LldpRemUnknownIndex_Type()
)
lldpRemUnknownIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemUnknownIndex.setStatus("current")


class _LldpRemUnknownTLVType_Type(Integer32):
    """Custom type lldpRemUnknownTLVType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9, 126),
    )


_LldpRemUnknownTLVType_Type.__name__ = "Integer32"
_LldpRemUnknownTLVType_Object = MibTableColumn
lldpRemUnknownTLVType = _LldpRemUnknownTLVType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 17, 3, 1, 4),
    _LldpRemUnknownTLVType_Type()
)
lldpRemUnknownTLVType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemUnknownTLVType.setStatus("current")


class _LldpRemUnknownTLVInfo_Type(OctetString):
    """Custom type lldpRemUnknownTLVInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 511),
    )


_LldpRemUnknownTLVInfo_Type.__name__ = "OctetString"
_LldpRemUnknownTLVInfo_Object = MibTableColumn
lldpRemUnknownTLVInfo = _LldpRemUnknownTLVInfo_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 17, 3, 1, 5),
    _LldpRemUnknownTLVInfo_Type()
)
lldpRemUnknownTLVInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemUnknownTLVInfo.setStatus("current")
_LldpXMedNotifications_ObjectIdentity = ObjectIdentity
lldpXMedNotifications = _LldpXMedNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 18)
)
_LldpXMedObjects_ObjectIdentity = ObjectIdentity
lldpXMedObjects = _LldpXMedObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19)
)
_LldpXMedConfig_ObjectIdentity = ObjectIdentity
lldpXMedConfig = _LldpXMedConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 1)
)
_LldpXMedLocDeviceClass_Type = LldpXMedDeviceClass
_LldpXMedLocDeviceClass_Object = MibScalar
lldpXMedLocDeviceClass = _LldpXMedLocDeviceClass_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 1, 1),
    _LldpXMedLocDeviceClass_Type()
)
lldpXMedLocDeviceClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedLocDeviceClass.setStatus("current")
_LldpXMedPortConfigTable_Object = MibTable
lldpXMedPortConfigTable = _LldpXMedPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 1, 2)
)
if mibBuilder.loadTexts:
    lldpXMedPortConfigTable.setStatus("current")
_LldpXMedPortConfigEntry_Object = MibTableRow
lldpXMedPortConfigEntry = _LldpXMedPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 1, 2, 1)
)
lldpXMedPortConfigEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXMedPortConfigPortNum"),
)
if mibBuilder.loadTexts:
    lldpXMedPortConfigEntry.setStatus("current")
_LldpXMedPortConfigPortNum_Type = LldpPortNumber
_LldpXMedPortConfigPortNum_Object = MibTableColumn
lldpXMedPortConfigPortNum = _LldpXMedPortConfigPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 1, 2, 1, 1),
    _LldpXMedPortConfigPortNum_Type()
)
lldpXMedPortConfigPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedPortConfigPortNum.setStatus("current")
_LldpXMedPortCapSupported_Type = LldpXMedCapabilities
_LldpXMedPortCapSupported_Object = MibTableColumn
lldpXMedPortCapSupported = _LldpXMedPortCapSupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 1, 2, 1, 2),
    _LldpXMedPortCapSupported_Type()
)
lldpXMedPortCapSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedPortCapSupported.setStatus("current")
_LldpXMedPortConfigTLVsTxEnable_Type = LldpXMedCapabilities
_LldpXMedPortConfigTLVsTxEnable_Object = MibTableColumn
lldpXMedPortConfigTLVsTxEnable = _LldpXMedPortConfigTLVsTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 1, 2, 1, 3),
    _LldpXMedPortConfigTLVsTxEnable_Type()
)
lldpXMedPortConfigTLVsTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXMedPortConfigTLVsTxEnable.setStatus("current")


class _LldpXMedPortConfigNotifEnable_Type(TruthValue):
    """Custom type lldpXMedPortConfigNotifEnable based on TruthValue"""


_LldpXMedPortConfigNotifEnable_Object = MibTableColumn
lldpXMedPortConfigNotifEnable = _LldpXMedPortConfigNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 1, 2, 1, 4),
    _LldpXMedPortConfigNotifEnable_Type()
)
lldpXMedPortConfigNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXMedPortConfigNotifEnable.setStatus("current")


class _LldpXMedFastStartRepeatCount_Type(Unsigned32):
    """Custom type lldpXMedFastStartRepeatCount based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_LldpXMedFastStartRepeatCount_Type.__name__ = "Unsigned32"
_LldpXMedFastStartRepeatCount_Object = MibScalar
lldpXMedFastStartRepeatCount = _LldpXMedFastStartRepeatCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 1, 3),
    _LldpXMedFastStartRepeatCount_Type()
)
lldpXMedFastStartRepeatCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXMedFastStartRepeatCount.setStatus("current")
_LldpXMedLocalData_ObjectIdentity = ObjectIdentity
lldpXMedLocalData = _LldpXMedLocalData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 2)
)
_LldpXMedLocMediaPolicyTable_Object = MibTable
lldpXMedLocMediaPolicyTable = _LldpXMedLocMediaPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 2, 1)
)
if mibBuilder.loadTexts:
    lldpXMedLocMediaPolicyTable.setStatus("current")
_LldpXMedLocMediaPolicyEntry_Object = MibTableRow
lldpXMedLocMediaPolicyEntry = _LldpXMedLocMediaPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 2, 1, 1)
)
lldpXMedLocMediaPolicyEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXMedLocMediaPolicyPortNum"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXMedLocMediaPolicyAppType"),
)
if mibBuilder.loadTexts:
    lldpXMedLocMediaPolicyEntry.setStatus("current")
_LldpXMedLocMediaPolicyPortNum_Type = LldpPortNumber
_LldpXMedLocMediaPolicyPortNum_Object = MibTableColumn
lldpXMedLocMediaPolicyPortNum = _LldpXMedLocMediaPolicyPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 2, 1, 1, 1),
    _LldpXMedLocMediaPolicyPortNum_Type()
)
lldpXMedLocMediaPolicyPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedLocMediaPolicyPortNum.setStatus("current")
_LldpXMedLocMediaPolicyAppType_Type = PolicyAppType
_LldpXMedLocMediaPolicyAppType_Object = MibTableColumn
lldpXMedLocMediaPolicyAppType = _LldpXMedLocMediaPolicyAppType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 2, 1, 1, 2),
    _LldpXMedLocMediaPolicyAppType_Type()
)
lldpXMedLocMediaPolicyAppType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXMedLocMediaPolicyAppType.setStatus("current")


class _LldpXMedLocMediaPolicyVlanID_Type(Integer32):
    """Custom type lldpXMedLocMediaPolicyVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(4095, 4095),
    )


_LldpXMedLocMediaPolicyVlanID_Type.__name__ = "Integer32"
_LldpXMedLocMediaPolicyVlanID_Object = MibTableColumn
lldpXMedLocMediaPolicyVlanID = _LldpXMedLocMediaPolicyVlanID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 2, 1, 1, 3),
    _LldpXMedLocMediaPolicyVlanID_Type()
)
lldpXMedLocMediaPolicyVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedLocMediaPolicyVlanID.setStatus("current")


class _LldpXMedLocMediaPolicyPriority_Type(Integer32):
    """Custom type lldpXMedLocMediaPolicyPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_LldpXMedLocMediaPolicyPriority_Type.__name__ = "Integer32"
_LldpXMedLocMediaPolicyPriority_Object = MibTableColumn
lldpXMedLocMediaPolicyPriority = _LldpXMedLocMediaPolicyPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 2, 1, 1, 4),
    _LldpXMedLocMediaPolicyPriority_Type()
)
lldpXMedLocMediaPolicyPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedLocMediaPolicyPriority.setStatus("current")
_LldpXMedLocMediaPolicyDscp_Type = Dscp
_LldpXMedLocMediaPolicyDscp_Object = MibTableColumn
lldpXMedLocMediaPolicyDscp = _LldpXMedLocMediaPolicyDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 2, 1, 1, 5),
    _LldpXMedLocMediaPolicyDscp_Type()
)
lldpXMedLocMediaPolicyDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedLocMediaPolicyDscp.setStatus("current")
_LldpXMedLocMediaPolicyUnknown_Type = TruthValue
_LldpXMedLocMediaPolicyUnknown_Object = MibTableColumn
lldpXMedLocMediaPolicyUnknown = _LldpXMedLocMediaPolicyUnknown_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 2, 1, 1, 6),
    _LldpXMedLocMediaPolicyUnknown_Type()
)
lldpXMedLocMediaPolicyUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedLocMediaPolicyUnknown.setStatus("current")
_LldpXMedLocMediaPolicyTagged_Type = TruthValue
_LldpXMedLocMediaPolicyTagged_Object = MibTableColumn
lldpXMedLocMediaPolicyTagged = _LldpXMedLocMediaPolicyTagged_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 2, 1, 1, 7),
    _LldpXMedLocMediaPolicyTagged_Type()
)
lldpXMedLocMediaPolicyTagged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedLocMediaPolicyTagged.setStatus("current")


class _LldpXMedLocHardwareRev_Type(SnmpAdminString):
    """Custom type lldpXMedLocHardwareRev based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LldpXMedLocHardwareRev_Type.__name__ = "SnmpAdminString"
_LldpXMedLocHardwareRev_Object = MibScalar
lldpXMedLocHardwareRev = _LldpXMedLocHardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 2, 2),
    _LldpXMedLocHardwareRev_Type()
)
lldpXMedLocHardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedLocHardwareRev.setStatus("current")


class _LldpXMedLocFirmwareRev_Type(SnmpAdminString):
    """Custom type lldpXMedLocFirmwareRev based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LldpXMedLocFirmwareRev_Type.__name__ = "SnmpAdminString"
_LldpXMedLocFirmwareRev_Object = MibScalar
lldpXMedLocFirmwareRev = _LldpXMedLocFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 2, 3),
    _LldpXMedLocFirmwareRev_Type()
)
lldpXMedLocFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedLocFirmwareRev.setStatus("current")


class _LldpXMedLocSoftwareRev_Type(SnmpAdminString):
    """Custom type lldpXMedLocSoftwareRev based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LldpXMedLocSoftwareRev_Type.__name__ = "SnmpAdminString"
_LldpXMedLocSoftwareRev_Object = MibScalar
lldpXMedLocSoftwareRev = _LldpXMedLocSoftwareRev_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 2, 4),
    _LldpXMedLocSoftwareRev_Type()
)
lldpXMedLocSoftwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedLocSoftwareRev.setStatus("current")


class _LldpXMedLocSerialNum_Type(SnmpAdminString):
    """Custom type lldpXMedLocSerialNum based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LldpXMedLocSerialNum_Type.__name__ = "SnmpAdminString"
_LldpXMedLocSerialNum_Object = MibScalar
lldpXMedLocSerialNum = _LldpXMedLocSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 2, 5),
    _LldpXMedLocSerialNum_Type()
)
lldpXMedLocSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedLocSerialNum.setStatus("current")


class _LldpXMedLocMfgName_Type(SnmpAdminString):
    """Custom type lldpXMedLocMfgName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LldpXMedLocMfgName_Type.__name__ = "SnmpAdminString"
_LldpXMedLocMfgName_Object = MibScalar
lldpXMedLocMfgName = _LldpXMedLocMfgName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 2, 6),
    _LldpXMedLocMfgName_Type()
)
lldpXMedLocMfgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedLocMfgName.setStatus("current")


class _LldpXMedLocModelName_Type(SnmpAdminString):
    """Custom type lldpXMedLocModelName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LldpXMedLocModelName_Type.__name__ = "SnmpAdminString"
_LldpXMedLocModelName_Object = MibScalar
lldpXMedLocModelName = _LldpXMedLocModelName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 2, 7),
    _LldpXMedLocModelName_Type()
)
lldpXMedLocModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedLocModelName.setStatus("current")


class _LldpXMedLocAssetID_Type(SnmpAdminString):
    """Custom type lldpXMedLocAssetID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LldpXMedLocAssetID_Type.__name__ = "SnmpAdminString"
_LldpXMedLocAssetID_Object = MibScalar
lldpXMedLocAssetID = _LldpXMedLocAssetID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 2, 8),
    _LldpXMedLocAssetID_Type()
)
lldpXMedLocAssetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedLocAssetID.setStatus("current")


class _LldpXMedLocXPoEDeviceType_Type(Integer32):
    """Custom type lldpXMedLocXPoEDeviceType based on Integer32"""
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
        *(("none", 4),
          ("pdDevice", 3),
          ("pseDevice", 2),
          ("unknown", 1))
    )


_LldpXMedLocXPoEDeviceType_Type.__name__ = "Integer32"
_LldpXMedLocXPoEDeviceType_Object = MibScalar
lldpXMedLocXPoEDeviceType = _LldpXMedLocXPoEDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 2, 10),
    _LldpXMedLocXPoEDeviceType_Type()
)
lldpXMedLocXPoEDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedLocXPoEDeviceType.setStatus("current")
_LldpXMedRemoteData_ObjectIdentity = ObjectIdentity
lldpXMedRemoteData = _LldpXMedRemoteData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 3)
)
_LldpXMedRemCapabilitiesTable_Object = MibTable
lldpXMedRemCapabilitiesTable = _LldpXMedRemCapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 3, 1)
)
if mibBuilder.loadTexts:
    lldpXMedRemCapabilitiesTable.setStatus("current")
_LldpXMedRemCapabilitiesEntry_Object = MibTableRow
lldpXMedRemCapabilitiesEntry = _LldpXMedRemCapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 3, 1, 1)
)
lldpXMedRemCapabilitiesEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXMedRemCapTimeMark"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXMedRemCapPortNum"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXMedRemCapIndex"),
)
if mibBuilder.loadTexts:
    lldpXMedRemCapabilitiesEntry.setStatus("current")
_LldpXMedRemCapTimeMark_Type = TimeFilter
_LldpXMedRemCapTimeMark_Object = MibTableColumn
lldpXMedRemCapTimeMark = _LldpXMedRemCapTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 3, 1, 1, 1),
    _LldpXMedRemCapTimeMark_Type()
)
lldpXMedRemCapTimeMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedRemCapTimeMark.setStatus("current")
_LldpXMedRemCapPortNum_Type = LldpPortNumber
_LldpXMedRemCapPortNum_Object = MibTableColumn
lldpXMedRemCapPortNum = _LldpXMedRemCapPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 3, 1, 1, 2),
    _LldpXMedRemCapPortNum_Type()
)
lldpXMedRemCapPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedRemCapPortNum.setStatus("current")


class _LldpXMedRemCapIndex_Type(Integer32):
    """Custom type lldpXMedRemCapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpXMedRemCapIndex_Type.__name__ = "Integer32"
_LldpXMedRemCapIndex_Object = MibTableColumn
lldpXMedRemCapIndex = _LldpXMedRemCapIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 3, 1, 1, 3),
    _LldpXMedRemCapIndex_Type()
)
lldpXMedRemCapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedRemCapIndex.setStatus("current")
_LldpXMedRemCapSupported_Type = LldpXMedCapabilities
_LldpXMedRemCapSupported_Object = MibTableColumn
lldpXMedRemCapSupported = _LldpXMedRemCapSupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 3, 1, 1, 4),
    _LldpXMedRemCapSupported_Type()
)
lldpXMedRemCapSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedRemCapSupported.setStatus("current")
_LldpXMedRemMediaPolicyTable_Object = MibTable
lldpXMedRemMediaPolicyTable = _LldpXMedRemMediaPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 3, 2)
)
if mibBuilder.loadTexts:
    lldpXMedRemMediaPolicyTable.setStatus("current")
_LldpXMedRemMediaPolicyEntry_Object = MibTableRow
lldpXMedRemMediaPolicyEntry = _LldpXMedRemMediaPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 3, 2, 1)
)
lldpXMedRemMediaPolicyEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXMedRemMediaPolicyTimeMark"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXMedRemMediaPolicyPortNum"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXMedRemMediaPolicyIndex"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXMedRemMediaPolicyAppType"),
)
if mibBuilder.loadTexts:
    lldpXMedRemMediaPolicyEntry.setStatus("current")
_LldpXMedRemMediaPolicyTimeMark_Type = TimeFilter
_LldpXMedRemMediaPolicyTimeMark_Object = MibTableColumn
lldpXMedRemMediaPolicyTimeMark = _LldpXMedRemMediaPolicyTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 3, 2, 1, 1),
    _LldpXMedRemMediaPolicyTimeMark_Type()
)
lldpXMedRemMediaPolicyTimeMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedRemMediaPolicyTimeMark.setStatus("current")
_LldpXMedRemMediaPolicyPortNum_Type = LldpPortNumber
_LldpXMedRemMediaPolicyPortNum_Object = MibTableColumn
lldpXMedRemMediaPolicyPortNum = _LldpXMedRemMediaPolicyPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 3, 2, 1, 2),
    _LldpXMedRemMediaPolicyPortNum_Type()
)
lldpXMedRemMediaPolicyPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedRemMediaPolicyPortNum.setStatus("current")


class _LldpXMedRemMediaPolicyIndex_Type(Integer32):
    """Custom type lldpXMedRemMediaPolicyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpXMedRemMediaPolicyIndex_Type.__name__ = "Integer32"
_LldpXMedRemMediaPolicyIndex_Object = MibTableColumn
lldpXMedRemMediaPolicyIndex = _LldpXMedRemMediaPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 3, 2, 1, 3),
    _LldpXMedRemMediaPolicyIndex_Type()
)
lldpXMedRemMediaPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedRemMediaPolicyIndex.setStatus("current")
_LldpXMedRemMediaPolicyAppType_Type = PolicyAppType
_LldpXMedRemMediaPolicyAppType_Object = MibTableColumn
lldpXMedRemMediaPolicyAppType = _LldpXMedRemMediaPolicyAppType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 3, 2, 1, 4),
    _LldpXMedRemMediaPolicyAppType_Type()
)
lldpXMedRemMediaPolicyAppType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXMedRemMediaPolicyAppType.setStatus("current")


class _LldpXMedRemMediaPolicyVlanID_Type(Integer32):
    """Custom type lldpXMedRemMediaPolicyVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(4095, 4095),
    )


_LldpXMedRemMediaPolicyVlanID_Type.__name__ = "Integer32"
_LldpXMedRemMediaPolicyVlanID_Object = MibTableColumn
lldpXMedRemMediaPolicyVlanID = _LldpXMedRemMediaPolicyVlanID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 3, 2, 1, 5),
    _LldpXMedRemMediaPolicyVlanID_Type()
)
lldpXMedRemMediaPolicyVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedRemMediaPolicyVlanID.setStatus("current")


class _LldpXMedRemMediaPolicyPriority_Type(Integer32):
    """Custom type lldpXMedRemMediaPolicyPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_LldpXMedRemMediaPolicyPriority_Type.__name__ = "Integer32"
_LldpXMedRemMediaPolicyPriority_Object = MibTableColumn
lldpXMedRemMediaPolicyPriority = _LldpXMedRemMediaPolicyPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 3, 2, 1, 6),
    _LldpXMedRemMediaPolicyPriority_Type()
)
lldpXMedRemMediaPolicyPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedRemMediaPolicyPriority.setStatus("current")
_LldpXMedRemMediaPolicyDscp_Type = Dscp
_LldpXMedRemMediaPolicyDscp_Object = MibTableColumn
lldpXMedRemMediaPolicyDscp = _LldpXMedRemMediaPolicyDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 3, 2, 1, 7),
    _LldpXMedRemMediaPolicyDscp_Type()
)
lldpXMedRemMediaPolicyDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedRemMediaPolicyDscp.setStatus("current")
_LldpXMedRemMediaPolicyUnknown_Type = TruthValue
_LldpXMedRemMediaPolicyUnknown_Object = MibTableColumn
lldpXMedRemMediaPolicyUnknown = _LldpXMedRemMediaPolicyUnknown_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 3, 2, 1, 8),
    _LldpXMedRemMediaPolicyUnknown_Type()
)
lldpXMedRemMediaPolicyUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedRemMediaPolicyUnknown.setStatus("current")
_LldpXMedRemMediaPolicyTagged_Type = TruthValue
_LldpXMedRemMediaPolicyTagged_Object = MibTableColumn
lldpXMedRemMediaPolicyTagged = _LldpXMedRemMediaPolicyTagged_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 3, 2, 1, 9),
    _LldpXMedRemMediaPolicyTagged_Type()
)
lldpXMedRemMediaPolicyTagged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedRemMediaPolicyTagged.setStatus("current")
_LldpXMedRemInventoryTable_Object = MibTable
lldpXMedRemInventoryTable = _LldpXMedRemInventoryTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 3, 3)
)
if mibBuilder.loadTexts:
    lldpXMedRemInventoryTable.setStatus("current")
_LldpXMedRemInventoryEntry_Object = MibTableRow
lldpXMedRemInventoryEntry = _LldpXMedRemInventoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 3, 3, 1)
)
lldpXMedRemInventoryEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXMedRemTimeMark"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXMedRemPortNum"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "lldpXMedRemIndex"),
)
if mibBuilder.loadTexts:
    lldpXMedRemInventoryEntry.setStatus("current")
_LldpXMedRemTimeMark_Type = TimeFilter
_LldpXMedRemTimeMark_Object = MibTableColumn
lldpXMedRemTimeMark = _LldpXMedRemTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 3, 3, 1, 1),
    _LldpXMedRemTimeMark_Type()
)
lldpXMedRemTimeMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedRemTimeMark.setStatus("current")
_LldpXMedRemPortNum_Type = LldpPortNumber
_LldpXMedRemPortNum_Object = MibTableColumn
lldpXMedRemPortNum = _LldpXMedRemPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 3, 3, 1, 2),
    _LldpXMedRemPortNum_Type()
)
lldpXMedRemPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedRemPortNum.setStatus("current")


class _LldpXMedRemIndex_Type(Integer32):
    """Custom type lldpXMedRemIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpXMedRemIndex_Type.__name__ = "Integer32"
_LldpXMedRemIndex_Object = MibTableColumn
lldpXMedRemIndex = _LldpXMedRemIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 3, 3, 1, 3),
    _LldpXMedRemIndex_Type()
)
lldpXMedRemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedRemIndex.setStatus("current")


class _LldpXMedRemHardwareRev_Type(SnmpAdminString):
    """Custom type lldpXMedRemHardwareRev based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LldpXMedRemHardwareRev_Type.__name__ = "SnmpAdminString"
_LldpXMedRemHardwareRev_Object = MibTableColumn
lldpXMedRemHardwareRev = _LldpXMedRemHardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 3, 3, 1, 4),
    _LldpXMedRemHardwareRev_Type()
)
lldpXMedRemHardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedRemHardwareRev.setStatus("current")


class _LldpXMedRemFirmwareRev_Type(SnmpAdminString):
    """Custom type lldpXMedRemFirmwareRev based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LldpXMedRemFirmwareRev_Type.__name__ = "SnmpAdminString"
_LldpXMedRemFirmwareRev_Object = MibTableColumn
lldpXMedRemFirmwareRev = _LldpXMedRemFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 3, 3, 1, 5),
    _LldpXMedRemFirmwareRev_Type()
)
lldpXMedRemFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedRemFirmwareRev.setStatus("current")


class _LldpXMedRemSoftwareRev_Type(SnmpAdminString):
    """Custom type lldpXMedRemSoftwareRev based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LldpXMedRemSoftwareRev_Type.__name__ = "SnmpAdminString"
_LldpXMedRemSoftwareRev_Object = MibTableColumn
lldpXMedRemSoftwareRev = _LldpXMedRemSoftwareRev_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 3, 3, 1, 6),
    _LldpXMedRemSoftwareRev_Type()
)
lldpXMedRemSoftwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedRemSoftwareRev.setStatus("current")


class _LldpXMedRemSerialNum_Type(SnmpAdminString):
    """Custom type lldpXMedRemSerialNum based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LldpXMedRemSerialNum_Type.__name__ = "SnmpAdminString"
_LldpXMedRemSerialNum_Object = MibTableColumn
lldpXMedRemSerialNum = _LldpXMedRemSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 3, 3, 1, 7),
    _LldpXMedRemSerialNum_Type()
)
lldpXMedRemSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedRemSerialNum.setStatus("current")


class _LldpXMedRemMfgName_Type(SnmpAdminString):
    """Custom type lldpXMedRemMfgName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LldpXMedRemMfgName_Type.__name__ = "SnmpAdminString"
_LldpXMedRemMfgName_Object = MibTableColumn
lldpXMedRemMfgName = _LldpXMedRemMfgName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 3, 3, 1, 8),
    _LldpXMedRemMfgName_Type()
)
lldpXMedRemMfgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedRemMfgName.setStatus("current")


class _LldpXMedRemModelName_Type(SnmpAdminString):
    """Custom type lldpXMedRemModelName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LldpXMedRemModelName_Type.__name__ = "SnmpAdminString"
_LldpXMedRemModelName_Object = MibTableColumn
lldpXMedRemModelName = _LldpXMedRemModelName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 3, 3, 1, 9),
    _LldpXMedRemModelName_Type()
)
lldpXMedRemModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedRemModelName.setStatus("current")


class _LldpXMedRemAssetID_Type(SnmpAdminString):
    """Custom type lldpXMedRemAssetID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LldpXMedRemAssetID_Type.__name__ = "SnmpAdminString"
_LldpXMedRemAssetID_Object = MibTableColumn
lldpXMedRemAssetID = _LldpXMedRemAssetID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 19, 3, 3, 1, 10),
    _LldpXMedRemAssetID_Type()
)
lldpXMedRemAssetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXMedRemAssetID.setStatus("current")
_DlinkL3Features_ObjectIdentity = ObjectIdentity
dlinkL3Features = _DlinkL3Features_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5)
)
_L3ARPGroup_ObjectIdentity = ObjectIdentity
l3ARPGroup = _L3ARPGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 1)
)
_ArpAgingTime_ObjectIdentity = ObjectIdentity
arpAgingTime = _ArpAgingTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 1, 1)
)
_ArpAgingTimeTable_Object = MibTable
arpAgingTimeTable = _ArpAgingTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    arpAgingTimeTable.setStatus("current")
_ArpAgingTimeEntry_Object = MibTableRow
arpAgingTimeEntry = _ArpAgingTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 1, 1, 1, 1)
)
arpAgingTimeEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "arpAgingTimeIntrefaceID"),
)
if mibBuilder.loadTexts:
    arpAgingTimeEntry.setStatus("current")
_ArpAgingTimeIntrefaceID_Type = Integer32
_ArpAgingTimeIntrefaceID_Object = MibTableColumn
arpAgingTimeIntrefaceID = _ArpAgingTimeIntrefaceID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 1, 1, 1, 1, 1),
    _ArpAgingTimeIntrefaceID_Type()
)
arpAgingTimeIntrefaceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpAgingTimeIntrefaceID.setStatus("current")


class _ArpAgingTimeTimeout_Type(Integer32):
    """Custom type arpAgingTimeTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ArpAgingTimeTimeout_Type.__name__ = "Integer32"
_ArpAgingTimeTimeout_Object = MibTableColumn
arpAgingTimeTimeout = _ArpAgingTimeTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 1, 1, 1, 1, 2),
    _ArpAgingTimeTimeout_Type()
)
arpAgingTimeTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpAgingTimeTimeout.setStatus("current")
_ArpARPTable_ObjectIdentity = ObjectIdentity
arpARPTable = _ArpARPTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 1, 2)
)
_ArpTable_Object = MibTable
arpTable = _ArpTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    arpTable.setStatus("current")
_ArpEntry_Object = MibTableRow
arpEntry = _ArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 1, 2, 1, 1)
)
arpEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "arpIntrefaceID"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "arpIpAddr"),
)
if mibBuilder.loadTexts:
    arpEntry.setStatus("current")


class _ArpIntrefaceID_Type(Integer32):
    """Custom type arpIntrefaceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ArpIntrefaceID_Type.__name__ = "Integer32"
_ArpIntrefaceID_Object = MibTableColumn
arpIntrefaceID = _ArpIntrefaceID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 1, 2, 1, 1, 1),
    _ArpIntrefaceID_Type()
)
arpIntrefaceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpIntrefaceID.setStatus("current")
_ArpIpAddr_Type = IpAddress
_ArpIpAddr_Object = MibTableColumn
arpIpAddr = _ArpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 1, 2, 1, 1, 2),
    _ArpIpAddr_Type()
)
arpIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpIpAddr.setStatus("current")
_ArpMacAddress_Type = MacAddress
_ArpMacAddress_Object = MibTableColumn
arpMacAddress = _ArpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 1, 2, 1, 1, 3),
    _ArpMacAddress_Type()
)
arpMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpMacAddress.setStatus("current")


class _ArpType_Type(Integer32):
    """Custom type arpType based on Integer32"""
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
        *(("dynamic", 3),
          ("invalid", 2),
          ("other", 1),
          ("static", 4))
    )


_ArpType_Type.__name__ = "Integer32"
_ArpType_Object = MibTableColumn
arpType = _ArpType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 1, 2, 1, 1, 4),
    _ArpType_Type()
)
arpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpType.setStatus("current")
_ArpRowStatus_Type = RowStatus
_ArpRowStatus_Object = MibTableColumn
arpRowStatus = _ArpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 1, 2, 1, 1, 5),
    _ArpRowStatus_Type()
)
arpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arpRowStatus.setStatus("current")
_L3IpMgmtGroup_ObjectIdentity = ObjectIdentity
l3IpMgmtGroup = _L3IpMgmtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3)
)
_MultiIfMainTable_Object = MibTable
multiIfMainTable = _MultiIfMainTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 1)
)
if mibBuilder.loadTexts:
    multiIfMainTable.setStatus("current")
_MultiIfMainEntry_Object = MibTableRow
multiIfMainEntry = _MultiIfMainEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 1, 1)
)
multiIfMainEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "multiIfMainIndex"),
)
if mibBuilder.loadTexts:
    multiIfMainEntry.setStatus("current")
_MultiIfMainIndex_Type = InterfaceIndex
_MultiIfMainIndex_Object = MibTableColumn
multiIfMainIndex = _MultiIfMainIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 1, 1, 1),
    _MultiIfMainIndex_Type()
)
multiIfMainIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiIfMainIndex.setStatus("current")


class _MultiIfMainAdminStatus_Type(Integer32):
    """Custom type multiIfMainAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_MultiIfMainAdminStatus_Type.__name__ = "Integer32"
_MultiIfMainAdminStatus_Object = MibTableColumn
multiIfMainAdminStatus = _MultiIfMainAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 1, 1, 2),
    _MultiIfMainAdminStatus_Type()
)
multiIfMainAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    multiIfMainAdminStatus.setStatus("current")


class _MultiIfMainOperStatus_Type(Integer32):
    """Custom type multiIfMainOperStatus based on Integer32"""
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
        *(("dormant", 5),
          ("down", 2),
          ("lowerLayerDown", 7),
          ("notPresent", 6),
          ("testing", 3),
          ("unknown", 4),
          ("up", 1))
    )


_MultiIfMainOperStatus_Type.__name__ = "Integer32"
_MultiIfMainOperStatus_Object = MibTableColumn
multiIfMainOperStatus = _MultiIfMainOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 1, 1, 3),
    _MultiIfMainOperStatus_Type()
)
multiIfMainOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiIfMainOperStatus.setStatus("current")
_MultiIfIpBindVlanId_Type = Integer32
_MultiIfIpBindVlanId_Object = MibTableColumn
multiIfIpBindVlanId = _MultiIfIpBindVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 1, 1, 4),
    _MultiIfIpBindVlanId_Type()
)
multiIfIpBindVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multiIfIpBindVlanId.setStatus("current")


class _MultiL3VlanIfName_Type(DisplayString):
    """Custom type multiL3VlanIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MultiL3VlanIfName_Type.__name__ = "DisplayString"
_MultiL3VlanIfName_Object = MibTableColumn
multiL3VlanIfName = _MultiL3VlanIfName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 1, 1, 5),
    _MultiL3VlanIfName_Type()
)
multiL3VlanIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiL3VlanIfName.setStatus("current")
_MultiIfMainRowStatus_Type = RowStatus
_MultiIfMainRowStatus_Object = MibTableColumn
multiIfMainRowStatus = _MultiIfMainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 1, 1, 6),
    _MultiIfMainRowStatus_Type()
)
multiIfMainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    multiIfMainRowStatus.setStatus("current")
_MultiIfIpTable_Object = MibTable
multiIfIpTable = _MultiIfIpTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 2)
)
if mibBuilder.loadTexts:
    multiIfIpTable.setStatus("current")
_MultiIfIpEntry_Object = MibTableRow
multiIfIpEntry = _MultiIfIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 2, 1)
)
multiIfIpEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "multiIfIpIndex"),
)
if mibBuilder.loadTexts:
    multiIfIpEntry.setStatus("current")
_MultiIfIpIndex_Type = InterfaceIndex
_MultiIfIpIndex_Object = MibTableColumn
multiIfIpIndex = _MultiIfIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 2, 1, 1),
    _MultiIfIpIndex_Type()
)
multiIfIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiIfIpIndex.setStatus("current")


class _MultiIfIpAddrAllocMethod_Type(Integer32):
    """Custom type multiIfIpAddrAllocMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("manual", 1))
    )


_MultiIfIpAddrAllocMethod_Type.__name__ = "Integer32"
_MultiIfIpAddrAllocMethod_Object = MibTableColumn
multiIfIpAddrAllocMethod = _MultiIfIpAddrAllocMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 2, 1, 2),
    _MultiIfIpAddrAllocMethod_Type()
)
multiIfIpAddrAllocMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multiIfIpAddrAllocMethod.setStatus("current")


class _MultiIfIpAddr_Type(IpAddress):
    """Custom type multiIfIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_MultiIfIpAddr_Object = MibTableColumn
multiIfIpAddr = _MultiIfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 2, 1, 3),
    _MultiIfIpAddr_Type()
)
multiIfIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multiIfIpAddr.setStatus("current")
_MultiIfIpSubnetMask_Type = IpAddress
_MultiIfIpSubnetMask_Object = MibTableColumn
multiIfIpSubnetMask = _MultiIfIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 2, 1, 4),
    _MultiIfIpSubnetMask_Type()
)
multiIfIpSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multiIfIpSubnetMask.setStatus("current")
_MultiRouteTable_Object = MibTable
multiRouteTable = _MultiRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 3)
)
if mibBuilder.loadTexts:
    multiRouteTable.setStatus("current")
_MultiRouteEntry_Object = MibTableRow
multiRouteEntry = _MultiRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 3, 1)
)
multiRouteEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "multiRouteDest"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "multiRouteMask"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "multiRouteTos"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "multiRouteNextHop"),
)
if mibBuilder.loadTexts:
    multiRouteEntry.setStatus("current")
_MultiRouteDest_Type = IpAddress
_MultiRouteDest_Object = MibTableColumn
multiRouteDest = _MultiRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 3, 1, 1),
    _MultiRouteDest_Type()
)
multiRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    multiRouteDest.setStatus("current")
_MultiRouteMask_Type = IpAddress
_MultiRouteMask_Object = MibTableColumn
multiRouteMask = _MultiRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 3, 1, 2),
    _MultiRouteMask_Type()
)
multiRouteMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    multiRouteMask.setStatus("current")


class _MultiRouteTos_Type(Integer32):
    """Custom type multiRouteTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MultiRouteTos_Type.__name__ = "Integer32"
_MultiRouteTos_Object = MibTableColumn
multiRouteTos = _MultiRouteTos_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 3, 1, 3),
    _MultiRouteTos_Type()
)
multiRouteTos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    multiRouteTos.setStatus("current")
_MultiRouteNextHop_Type = IpAddress
_MultiRouteNextHop_Object = MibTableColumn
multiRouteNextHop = _MultiRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 3, 1, 4),
    _MultiRouteNextHop_Type()
)
multiRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    multiRouteNextHop.setStatus("current")
_MultiRouteIfIndex_Type = Integer32
_MultiRouteIfIndex_Object = MibTableColumn
multiRouteIfIndex = _MultiRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 3, 1, 5),
    _MultiRouteIfIndex_Type()
)
multiRouteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiRouteIfIndex.setStatus("current")
_MultiRouteStatus_Type = RowStatus
_MultiRouteStatus_Object = MibTableColumn
multiRouteStatus = _MultiRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 3, 1, 6),
    _MultiRouteStatus_Type()
)
multiRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    multiRouteStatus.setStatus("current")
_MultiIpv6IfTable_Object = MibTable
multiIpv6IfTable = _MultiIpv6IfTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 4)
)
if mibBuilder.loadTexts:
    multiIpv6IfTable.setStatus("current")
_MultiIpv6IfEntry_Object = MibTableRow
multiIpv6IfEntry = _MultiIpv6IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 4, 1)
)
multiIpv6IfEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "multiIpv6IfIndex"),
)
if mibBuilder.loadTexts:
    multiIpv6IfEntry.setStatus("current")
_MultiIpv6IfIndex_Type = InterfaceIndex
_MultiIpv6IfIndex_Object = MibTableColumn
multiIpv6IfIndex = _MultiIpv6IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 4, 1, 1),
    _MultiIpv6IfIndex_Type()
)
multiIpv6IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiIpv6IfIndex.setStatus("current")


class _MultiIpv6IfAdminStatus_Type(Integer32):
    """Custom type multiIpv6IfAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_MultiIpv6IfAdminStatus_Type.__name__ = "Integer32"
_MultiIpv6IfAdminStatus_Object = MibTableColumn
multiIpv6IfAdminStatus = _MultiIpv6IfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 4, 1, 2),
    _MultiIpv6IfAdminStatus_Type()
)
multiIpv6IfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multiIpv6IfAdminStatus.setStatus("current")


class _MultiIpv6IfOperStatus_Type(Integer32):
    """Custom type multiIpv6IfOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("stale", 3),
          ("up", 1))
    )


_MultiIpv6IfOperStatus_Type.__name__ = "Integer32"
_MultiIpv6IfOperStatus_Object = MibTableColumn
multiIpv6IfOperStatus = _MultiIpv6IfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 4, 1, 3),
    _MultiIpv6IfOperStatus_Type()
)
multiIpv6IfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiIpv6IfOperStatus.setStatus("current")


class _MultiIpv6IfRetransmitTime_Type(Integer32):
    """Custom type multiIpv6IfRetransmitTime based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_MultiIpv6IfRetransmitTime_Type.__name__ = "Integer32"
_MultiIpv6IfRetransmitTime_Object = MibTableColumn
multiIpv6IfRetransmitTime = _MultiIpv6IfRetransmitTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 4, 1, 4),
    _MultiIpv6IfRetransmitTime_Type()
)
multiIpv6IfRetransmitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multiIpv6IfRetransmitTime.setStatus("current")
_MultiIpv6AddrTable_Object = MibTable
multiIpv6AddrTable = _MultiIpv6AddrTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 5)
)
if mibBuilder.loadTexts:
    multiIpv6AddrTable.setStatus("current")
_MultiIpv6AddrEntry_Object = MibTableRow
multiIpv6AddrEntry = _MultiIpv6AddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 5, 1)
)
multiIpv6AddrEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "multiIpv6AddrIndex"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "multiIpv6AddrAddress"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "multiIpv6AddrPrefixLen"),
)
if mibBuilder.loadTexts:
    multiIpv6AddrEntry.setStatus("current")
_MultiIpv6AddrIndex_Type = InterfaceIndex
_MultiIpv6AddrIndex_Object = MibTableColumn
multiIpv6AddrIndex = _MultiIpv6AddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 5, 1, 1),
    _MultiIpv6AddrIndex_Type()
)
multiIpv6AddrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiIpv6AddrIndex.setStatus("current")
_MultiIpv6AddrAddress_Type = Ipv6Address
_MultiIpv6AddrAddress_Object = MibTableColumn
multiIpv6AddrAddress = _MultiIpv6AddrAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 5, 1, 2),
    _MultiIpv6AddrAddress_Type()
)
multiIpv6AddrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiIpv6AddrAddress.setStatus("current")


class _MultiIpv6AddrPrefixLen_Type(Integer32):
    """Custom type multiIpv6AddrPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MultiIpv6AddrPrefixLen_Type.__name__ = "Integer32"
_MultiIpv6AddrPrefixLen_Object = MibTableColumn
multiIpv6AddrPrefixLen = _MultiIpv6AddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 5, 1, 3),
    _MultiIpv6AddrPrefixLen_Type()
)
multiIpv6AddrPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiIpv6AddrPrefixLen.setStatus("current")
_MultiIpv6AddrAdminStatus_Type = RowStatus
_MultiIpv6AddrAdminStatus_Object = MibTableColumn
multiIpv6AddrAdminStatus = _MultiIpv6AddrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 5, 1, 4),
    _MultiIpv6AddrAdminStatus_Type()
)
multiIpv6AddrAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    multiIpv6AddrAdminStatus.setStatus("current")


class _MultiIpv6AddrType_Type(Integer32):
    """Custom type multiIpv6AddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("anycast", 2),
          ("linklocal", 3),
          ("unicast", 1))
    )


_MultiIpv6AddrType_Type.__name__ = "Integer32"
_MultiIpv6AddrType_Object = MibTableColumn
multiIpv6AddrType = _MultiIpv6AddrType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 5, 1, 5),
    _MultiIpv6AddrType_Type()
)
multiIpv6AddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multiIpv6AddrType.setStatus("current")


class _MultiIpv6AddrCfgMethod_Type(Integer32):
    """Custom type multiIpv6AddrCfgMethod based on Integer32"""
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
        *(("dynamic", 4),
          ("stateful", 3),
          ("stateless", 2),
          ("static", 1))
    )


_MultiIpv6AddrCfgMethod_Type.__name__ = "Integer32"
_MultiIpv6AddrCfgMethod_Object = MibTableColumn
multiIpv6AddrCfgMethod = _MultiIpv6AddrCfgMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 5, 1, 6),
    _MultiIpv6AddrCfgMethod_Type()
)
multiIpv6AddrCfgMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiIpv6AddrCfgMethod.setStatus("current")


class _MultiIpv6AddrOperStatus_Type(Integer32):
    """Custom type multiIpv6AddrOperStatus based on Integer32"""
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
        *(("complete", 2),
          ("down", 3),
          ("failed", 4),
          ("tentative", 1))
    )


_MultiIpv6AddrOperStatus_Type.__name__ = "Integer32"
_MultiIpv6AddrOperStatus_Object = MibTableColumn
multiIpv6AddrOperStatus = _MultiIpv6AddrOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 5, 1, 7),
    _MultiIpv6AddrOperStatus_Type()
)
multiIpv6AddrOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiIpv6AddrOperStatus.setStatus("current")
_MultiIPv6neighborTable_Object = MibTable
multiIPv6neighborTable = _MultiIPv6neighborTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 6)
)
if mibBuilder.loadTexts:
    multiIPv6neighborTable.setStatus("current")
_MultiIpv6NeighborEntry_Object = MibTableRow
multiIpv6NeighborEntry = _MultiIpv6NeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 6, 1)
)
multiIpv6NeighborEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "multiIpv6NeighborIndex"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "multiIpv6NeighborAddr"),
)
if mibBuilder.loadTexts:
    multiIpv6NeighborEntry.setStatus("current")
_MultiIpv6NeighborIndex_Type = Integer32
_MultiIpv6NeighborIndex_Object = MibTableColumn
multiIpv6NeighborIndex = _MultiIpv6NeighborIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 6, 1, 1),
    _MultiIpv6NeighborIndex_Type()
)
multiIpv6NeighborIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiIpv6NeighborIndex.setStatus("current")
_MultiIpv6NeighborAddr_Type = Ipv6Address
_MultiIpv6NeighborAddr_Object = MibTableColumn
multiIpv6NeighborAddr = _MultiIpv6NeighborAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 6, 1, 2),
    _MultiIpv6NeighborAddr_Type()
)
multiIpv6NeighborAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiIpv6NeighborAddr.setStatus("current")
_MultiIpv6NeighborMacAddr_Type = MacAddress
_MultiIpv6NeighborMacAddr_Object = MibTableColumn
multiIpv6NeighborMacAddr = _MultiIpv6NeighborMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 6, 1, 3),
    _MultiIpv6NeighborMacAddr_Type()
)
multiIpv6NeighborMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multiIpv6NeighborMacAddr.setStatus("current")


class _MultiIpv6NeighborType_Type(Integer32):
    """Custom type multiIpv6NeighborType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_MultiIpv6NeighborType_Type.__name__ = "Integer32"
_MultiIpv6NeighborType_Object = MibTableColumn
multiIpv6NeighborType = _MultiIpv6NeighborType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 6, 1, 4),
    _MultiIpv6NeighborType_Type()
)
multiIpv6NeighborType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiIpv6NeighborType.setStatus("current")


class _MultiIpv6NeighborCacheState_Type(Integer32):
    """Custom type multiIpv6NeighborCacheState based on Integer32"""
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
        *(("delay", 5),
          ("incomplete", 3),
          ("notinservice", 7),
          ("probe", 6),
          ("reachable", 2),
          ("stale", 4),
          ("static", 1))
    )


_MultiIpv6NeighborCacheState_Type.__name__ = "Integer32"
_MultiIpv6NeighborCacheState_Object = MibTableColumn
multiIpv6NeighborCacheState = _MultiIpv6NeighborCacheState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 6, 1, 5),
    _MultiIpv6NeighborCacheState_Type()
)
multiIpv6NeighborCacheState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiIpv6NeighborCacheState.setStatus("current")
_MultiIpv6NeighborRowStatus_Type = RowStatus
_MultiIpv6NeighborRowStatus_Object = MibTableColumn
multiIpv6NeighborRowStatus = _MultiIpv6NeighborRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 6, 1, 6),
    _MultiIpv6NeighborRowStatus_Type()
)
multiIpv6NeighborRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multiIpv6NeighborRowStatus.setStatus("current")
_MultiIpv6RouteTable_Object = MibTable
multiIpv6RouteTable = _MultiIpv6RouteTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 7)
)
if mibBuilder.loadTexts:
    multiIpv6RouteTable.setStatus("current")
_MultiIpv6RouteEntry_Object = MibTableRow
multiIpv6RouteEntry = _MultiIpv6RouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 7, 1)
)
multiIpv6RouteEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "multiIpv6RouteDest"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "multiIpv6RoutePfxLength"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "multiIpv6RouteProtocol"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "multiIpv6RouteNextHop"),
)
if mibBuilder.loadTexts:
    multiIpv6RouteEntry.setStatus("current")
_MultiIpv6RouteDest_Type = Ipv6Address
_MultiIpv6RouteDest_Object = MibTableColumn
multiIpv6RouteDest = _MultiIpv6RouteDest_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 7, 1, 1),
    _MultiIpv6RouteDest_Type()
)
multiIpv6RouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiIpv6RouteDest.setStatus("current")


class _MultiIpv6RoutePfxLength_Type(Integer32):
    """Custom type multiIpv6RoutePfxLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_MultiIpv6RoutePfxLength_Type.__name__ = "Integer32"
_MultiIpv6RoutePfxLength_Object = MibTableColumn
multiIpv6RoutePfxLength = _MultiIpv6RoutePfxLength_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 7, 1, 2),
    _MultiIpv6RoutePfxLength_Type()
)
multiIpv6RoutePfxLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiIpv6RoutePfxLength.setStatus("current")


class _MultiIpv6RouteProtocol_Type(Integer32):
    """Custom type multiIpv6RouteProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_MultiIpv6RouteProtocol_Type.__name__ = "Integer32"
_MultiIpv6RouteProtocol_Object = MibTableColumn
multiIpv6RouteProtocol = _MultiIpv6RouteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 7, 1, 3),
    _MultiIpv6RouteProtocol_Type()
)
multiIpv6RouteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiIpv6RouteProtocol.setStatus("current")
_MultiIpv6RouteNextHop_Type = Ipv6Address
_MultiIpv6RouteNextHop_Object = MibTableColumn
multiIpv6RouteNextHop = _MultiIpv6RouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 7, 1, 4),
    _MultiIpv6RouteNextHop_Type()
)
multiIpv6RouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiIpv6RouteNextHop.setStatus("current")
_MultiIpv6RouteIfIndex_Type = InterfaceIndex
_MultiIpv6RouteIfIndex_Object = MibTableColumn
multiIpv6RouteIfIndex = _MultiIpv6RouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 7, 1, 5),
    _MultiIpv6RouteIfIndex_Type()
)
multiIpv6RouteIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multiIpv6RouteIfIndex.setStatus("current")
_MultiIpv6RouteAdminStatus_Type = RowStatus
_MultiIpv6RouteAdminStatus_Object = MibTableColumn
multiIpv6RouteAdminStatus = _MultiIpv6RouteAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 7, 1, 6),
    _MultiIpv6RouteAdminStatus_Type()
)
multiIpv6RouteAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    multiIpv6RouteAdminStatus.setStatus("current")
_DhcpClientTable_Object = MibTable
dhcpClientTable = _DhcpClientTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 8)
)
if mibBuilder.loadTexts:
    dhcpClientTable.setStatus("current")
_DhcpClientEntry_Object = MibTableRow
dhcpClientEntry = _DhcpClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 8, 1)
)
dhcpClientEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "dhcpClientIfIndex"),
)
if mibBuilder.loadTexts:
    dhcpClientEntry.setStatus("current")
_DhcpClientIfIndex_Type = InterfaceIndex
_DhcpClientIfIndex_Object = MibTableColumn
dhcpClientIfIndex = _DhcpClientIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 8, 1, 1),
    _DhcpClientIfIndex_Type()
)
dhcpClientIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpClientIfIndex.setStatus("current")
_DhcpClientClientIdIfIdx_Type = InterfaceIndex
_DhcpClientClientIdIfIdx_Object = MibTableColumn
dhcpClientClientIdIfIdx = _DhcpClientClientIdIfIdx_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 8, 1, 2),
    _DhcpClientClientIdIfIdx_Type()
)
dhcpClientClientIdIfIdx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpClientClientIdIfIdx.setStatus("current")


class _DhcpClientClassIdType_Type(Integer32):
    """Custom type dhcpClientClassIdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("hex", 2))
    )


_DhcpClientClassIdType_Type.__name__ = "Integer32"
_DhcpClientClassIdType_Object = MibTableColumn
dhcpClientClassIdType = _DhcpClientClassIdType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 8, 1, 3),
    _DhcpClientClassIdType_Type()
)
dhcpClientClassIdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpClientClassIdType.setStatus("current")
_DhcpClientClassId_Type = OctetString
_DhcpClientClassId_Object = MibTableColumn
dhcpClientClassId = _DhcpClientClassId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 8, 1, 4),
    _DhcpClientClassId_Type()
)
dhcpClientClassId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpClientClassId.setStatus("current")


class _DhcpClientHostName_Type(DisplayString):
    """Custom type dhcpClientHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DhcpClientHostName_Type.__name__ = "DisplayString"
_DhcpClientHostName_Object = MibTableColumn
dhcpClientHostName = _DhcpClientHostName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 8, 1, 5),
    _DhcpClientHostName_Type()
)
dhcpClientHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpClientHostName.setStatus("current")


class _DhcpClientLeaseDay_Type(Integer32):
    """Custom type dhcpClientLeaseDay based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 10000),
    )


_DhcpClientLeaseDay_Type.__name__ = "Integer32"
_DhcpClientLeaseDay_Object = MibTableColumn
dhcpClientLeaseDay = _DhcpClientLeaseDay_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 8, 1, 6),
    _DhcpClientLeaseDay_Type()
)
dhcpClientLeaseDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpClientLeaseDay.setStatus("current")


class _DhcpClientLeaseHour_Type(Unsigned32):
    """Custom type dhcpClientLeaseHour based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_DhcpClientLeaseHour_Type.__name__ = "Unsigned32"
_DhcpClientLeaseHour_Object = MibTableColumn
dhcpClientLeaseHour = _DhcpClientLeaseHour_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 8, 1, 7),
    _DhcpClientLeaseHour_Type()
)
dhcpClientLeaseHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpClientLeaseHour.setStatus("current")


class _DhcpClientLeaseMinute_Type(Unsigned32):
    """Custom type dhcpClientLeaseMinute based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_DhcpClientLeaseMinute_Type.__name__ = "Unsigned32"
_DhcpClientLeaseMinute_Object = MibTableColumn
dhcpClientLeaseMinute = _DhcpClientLeaseMinute_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 8, 1, 8),
    _DhcpClientLeaseMinute_Type()
)
dhcpClientLeaseMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpClientLeaseMinute.setStatus("current")
_Dhcp6ClientTable_Object = MibTable
dhcp6ClientTable = _Dhcp6ClientTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 9)
)
if mibBuilder.loadTexts:
    dhcp6ClientTable.setStatus("current")
_Dhcp6ClientEntry_Object = MibTableRow
dhcp6ClientEntry = _Dhcp6ClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 9, 1)
)
dhcp6ClientEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "dhcp6ClientIndex"),
)
if mibBuilder.loadTexts:
    dhcp6ClientEntry.setStatus("current")
_Dhcp6ClientIndex_Type = InterfaceIndex
_Dhcp6ClientIndex_Object = MibTableColumn
dhcp6ClientIndex = _Dhcp6ClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 9, 1, 1),
    _Dhcp6ClientIndex_Type()
)
dhcp6ClientIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcp6ClientIndex.setStatus("current")


class _Dhcp6ClientEnabled_Type(Integer32):
    """Custom type dhcp6ClientEnabled based on Integer32"""
    defaultValue = 2

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


_Dhcp6ClientEnabled_Type.__name__ = "Integer32"
_Dhcp6ClientEnabled_Object = MibTableColumn
dhcp6ClientEnabled = _Dhcp6ClientEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 9, 1, 2),
    _Dhcp6ClientEnabled_Type()
)
dhcp6ClientEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcp6ClientEnabled.setStatus("current")


class _Dhcp6ClientRapidCommit_Type(Integer32):
    """Custom type dhcp6ClientRapidCommit based on Integer32"""
    defaultValue = 2

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


_Dhcp6ClientRapidCommit_Type.__name__ = "Integer32"
_Dhcp6ClientRapidCommit_Object = MibTableColumn
dhcp6ClientRapidCommit = _Dhcp6ClientRapidCommit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 5, 3, 9, 1, 3),
    _Dhcp6ClientRapidCommit_Type()
)
dhcp6ClientRapidCommit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcp6ClientRapidCommit.setStatus("current")
_DlinkQoS_ObjectIdentity = ObjectIdentity
dlinkQoS = _DlinkQoS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6)
)
_QosBasicSettingsGroup_ObjectIdentity = ObjectIdentity
qosBasicSettingsGroup = _QosBasicSettingsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1)
)
_QosBasPortDefaultCoS_ObjectIdentity = ObjectIdentity
qosBasPortDefaultCoS = _QosBasPortDefaultCoS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 1)
)
_QosPortDefaultCoSTable_Object = MibTable
qosPortDefaultCoSTable = _QosPortDefaultCoSTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 1, 1)
)
if mibBuilder.loadTexts:
    qosPortDefaultCoSTable.setStatus("current")
_QosPortDefaultCoSEntry_Object = MibTableRow
qosPortDefaultCoSEntry = _QosPortDefaultCoSEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 1, 1, 1)
)
qosPortDefaultCoSEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "qosPortindex"),
)
if mibBuilder.loadTexts:
    qosPortDefaultCoSEntry.setStatus("current")
_QosPortindex_Type = Integer32
_QosPortindex_Object = MibTableColumn
qosPortindex = _QosPortindex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 1, 1, 1, 1),
    _QosPortindex_Type()
)
qosPortindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPortindex.setStatus("current")


class _QosPortDefMode_Type(Integer32):
    """Custom type qosPortDefMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("defaultCoS", 1),
          ("none", 2))
    )


_QosPortDefMode_Type.__name__ = "Integer32"
_QosPortDefMode_Object = MibTableColumn
qosPortDefMode = _QosPortDefMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 1, 1, 1, 2),
    _QosPortDefMode_Type()
)
qosPortDefMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPortDefMode.setStatus("current")


class _QosPortDefCos_Type(Integer32):
    """Custom type qosPortDefCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosPortDefCos_Type.__name__ = "Integer32"
_QosPortDefCos_Object = MibTableColumn
qosPortDefCos = _QosPortDefCos_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 1, 1, 1, 3),
    _QosPortDefCos_Type()
)
qosPortDefCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosPortDefCos.setStatus("current")


class _QosPortDefOverride_Type(Integer32):
    """Custom type qosPortDefOverride based on Integer32"""
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


_QosPortDefOverride_Type.__name__ = "Integer32"
_QosPortDefOverride_Object = MibTableColumn
qosPortDefOverride = _QosPortDefOverride_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 1, 1, 1, 4),
    _QosPortDefOverride_Type()
)
qosPortDefOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPortDefOverride.setStatus("current")
_QosBasPortScheMethod_ObjectIdentity = ObjectIdentity
qosBasPortScheMethod = _QosBasPortScheMethod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 2)
)
_QosPortSchedulerMethodTable_Object = MibTable
qosPortSchedulerMethodTable = _QosPortSchedulerMethodTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    qosPortSchedulerMethodTable.setStatus("current")
_QosPortSchedulerMethodEntry_Object = MibTableRow
qosPortSchedulerMethodEntry = _QosPortSchedulerMethodEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 2, 1, 1)
)
qosPortSchedulerMethodEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "qosSchedulingModeBasePort"),
)
if mibBuilder.loadTexts:
    qosPortSchedulerMethodEntry.setStatus("current")
_QosSchedulingModeBasePort_Type = Integer32
_QosSchedulingModeBasePort_Object = MibTableColumn
qosSchedulingModeBasePort = _QosSchedulingModeBasePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 2, 1, 1, 1),
    _QosSchedulingModeBasePort_Type()
)
qosSchedulingModeBasePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosSchedulingModeBasePort.setStatus("current")


class _QosSchedulingMode_Type(Integer32):
    """Custom type qosSchedulingMode based on Integer32"""
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
        *(("rr", 2),
          ("sp", 1),
          ("wdrr", 4),
          ("wrr", 3))
    )


_QosSchedulingMode_Type.__name__ = "Integer32"
_QosSchedulingMode_Object = MibTableColumn
qosSchedulingMode = _QosSchedulingMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 2, 1, 1, 2),
    _QosSchedulingMode_Type()
)
qosSchedulingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosSchedulingMode.setStatus("current")
_QosBasQueueSettings_ObjectIdentity = ObjectIdentity
qosBasQueueSettings = _QosBasQueueSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 3)
)
_QosQueueSettingsTable_Object = MibTable
qosQueueSettingsTable = _QosQueueSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 3, 1)
)
if mibBuilder.loadTexts:
    qosQueueSettingsTable.setStatus("current")
_QosQueueSettingsEntry_Object = MibTableRow
qosQueueSettingsEntry = _QosQueueSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 3, 1, 1)
)
qosQueueSettingsEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "qosQueueBasePort"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "qosQueueID"),
)
if mibBuilder.loadTexts:
    qosQueueSettingsEntry.setStatus("current")
_QosQueueBasePort_Type = Integer32
_QosQueueBasePort_Object = MibTableColumn
qosQueueBasePort = _QosQueueBasePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 3, 1, 1, 1),
    _QosQueueBasePort_Type()
)
qosQueueBasePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosQueueBasePort.setStatus("current")


class _QosQueueID_Type(Integer32):
    """Custom type qosQueueID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosQueueID_Type.__name__ = "Integer32"
_QosQueueID_Object = MibTableColumn
qosQueueID = _QosQueueID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 3, 1, 1, 2),
    _QosQueueID_Type()
)
qosQueueID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosQueueID.setStatus("current")


class _QosQueueWrrWeight_Type(Integer32):
    """Custom type qosQueueWrrWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_QosQueueWrrWeight_Type.__name__ = "Integer32"
_QosQueueWrrWeight_Object = MibTableColumn
qosQueueWrrWeight = _QosQueueWrrWeight_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 3, 1, 1, 3),
    _QosQueueWrrWeight_Type()
)
qosQueueWrrWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosQueueWrrWeight.setStatus("current")


class _QosQueueQuantum_Type(Integer32):
    """Custom type qosQueueQuantum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_QosQueueQuantum_Type.__name__ = "Integer32"
_QosQueueQuantum_Object = MibTableColumn
qosQueueQuantum = _QosQueueQuantum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 3, 1, 1, 4),
    _QosQueueQuantum_Type()
)
qosQueueQuantum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosQueueQuantum.setStatus("current")
_QosBasCoS2QueueMapping_ObjectIdentity = ObjectIdentity
qosBasCoS2QueueMapping = _QosBasCoS2QueueMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 4)
)
_QosCoS2QueueTable_Object = MibTable
qosCoS2QueueTable = _QosCoS2QueueTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 4, 1)
)
if mibBuilder.loadTexts:
    qosCoS2QueueTable.setStatus("current")
_QosCoS2QueueEntry_Object = MibTableRow
qosCoS2QueueEntry = _QosCoS2QueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 4, 1, 1)
)
qosCoS2QueueEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "qosCoS2QueCos"),
)
if mibBuilder.loadTexts:
    qosCoS2QueueEntry.setStatus("current")


class _QosCoS2QueCos_Type(Integer32):
    """Custom type qosCoS2QueCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosCoS2QueCos_Type.__name__ = "Integer32"
_QosCoS2QueCos_Object = MibTableColumn
qosCoS2QueCos = _QosCoS2QueCos_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 4, 1, 1, 1),
    _QosCoS2QueCos_Type()
)
qosCoS2QueCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCoS2QueCos.setStatus("current")


class _QosCos2QueQueueID_Type(Integer32):
    """Custom type qosCos2QueQueueID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosCos2QueQueueID_Type.__name__ = "Integer32"
_QosCos2QueQueueID_Object = MibTableColumn
qosCos2QueQueueID = _QosCos2QueQueueID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 4, 1, 1, 2),
    _QosCos2QueQueueID_Type()
)
qosCos2QueQueueID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosCos2QueQueueID.setStatus("current")
_QosBasPortRateLimiting_ObjectIdentity = ObjectIdentity
qosBasPortRateLimiting = _QosBasPortRateLimiting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 5)
)
_QosPortRateLimitingTable_Object = MibTable
qosPortRateLimitingTable = _QosPortRateLimitingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 5, 1)
)
if mibBuilder.loadTexts:
    qosPortRateLimitingTable.setStatus("current")
_QosPortRateLimitingEntry_Object = MibTableRow
qosPortRateLimitingEntry = _QosPortRateLimitingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 5, 1, 1)
)
qosPortRateLimitingEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "qosBandwidthBasePort"),
)
if mibBuilder.loadTexts:
    qosPortRateLimitingEntry.setStatus("current")
_QosBandwidthBasePort_Type = Integer32
_QosBandwidthBasePort_Object = MibTableColumn
qosBandwidthBasePort = _QosBandwidthBasePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 5, 1, 1, 1),
    _QosBandwidthBasePort_Type()
)
qosBandwidthBasePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosBandwidthBasePort.setStatus("current")


class _QosBandwidthRxRate_Type(Integer32):
    """Custom type qosBandwidthRxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_QosBandwidthRxRate_Type.__name__ = "Integer32"
_QosBandwidthRxRate_Object = MibTableColumn
qosBandwidthRxRate = _QosBandwidthRxRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 5, 1, 1, 2),
    _QosBandwidthRxRate_Type()
)
qosBandwidthRxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosBandwidthRxRate.setStatus("current")


class _QosBandwidthRxRateMode_Type(Integer32):
    """Custom type qosBandwidthRxRateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("percent", 2),
          ("rate", 1))
    )


_QosBandwidthRxRateMode_Type.__name__ = "Integer32"
_QosBandwidthRxRateMode_Object = MibTableColumn
qosBandwidthRxRateMode = _QosBandwidthRxRateMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 5, 1, 1, 3),
    _QosBandwidthRxRateMode_Type()
)
qosBandwidthRxRateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosBandwidthRxRateMode.setStatus("current")


class _QosBandwidthRxBurst_Type(Integer32):
    """Custom type qosBandwidthRxBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128000),
    )


_QosBandwidthRxBurst_Type.__name__ = "Integer32"
_QosBandwidthRxBurst_Object = MibTableColumn
qosBandwidthRxBurst = _QosBandwidthRxBurst_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 5, 1, 1, 4),
    _QosBandwidthRxBurst_Type()
)
qosBandwidthRxBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosBandwidthRxBurst.setStatus("current")


class _QosBandwidthTxRate_Type(Integer32):
    """Custom type qosBandwidthTxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_QosBandwidthTxRate_Type.__name__ = "Integer32"
_QosBandwidthTxRate_Object = MibTableColumn
qosBandwidthTxRate = _QosBandwidthTxRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 5, 1, 1, 5),
    _QosBandwidthTxRate_Type()
)
qosBandwidthTxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosBandwidthTxRate.setStatus("current")


class _QosBandwidthTxRateMode_Type(Integer32):
    """Custom type qosBandwidthTxRateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("percent", 2),
          ("rate", 1))
    )


_QosBandwidthTxRateMode_Type.__name__ = "Integer32"
_QosBandwidthTxRateMode_Object = MibTableColumn
qosBandwidthTxRateMode = _QosBandwidthTxRateMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 5, 1, 1, 6),
    _QosBandwidthTxRateMode_Type()
)
qosBandwidthTxRateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosBandwidthTxRateMode.setStatus("current")


class _QosBandwidthTxBurst_Type(Integer32):
    """Custom type qosBandwidthTxBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128000),
    )


_QosBandwidthTxBurst_Type.__name__ = "Integer32"
_QosBandwidthTxBurst_Object = MibTableColumn
qosBandwidthTxBurst = _QosBandwidthTxBurst_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 5, 1, 1, 7),
    _QosBandwidthTxBurst_Type()
)
qosBandwidthTxBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosBandwidthTxBurst.setStatus("current")
_QosBasQueueRateLimiting_ObjectIdentity = ObjectIdentity
qosBasQueueRateLimiting = _QosBasQueueRateLimiting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 6)
)
_QosQueueRateLimitingTable_Object = MibTable
qosQueueRateLimitingTable = _QosQueueRateLimitingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 6, 1)
)
if mibBuilder.loadTexts:
    qosQueueRateLimitingTable.setStatus("current")
_QosQueueRateLimitingEntry_Object = MibTableRow
qosQueueRateLimitingEntry = _QosQueueRateLimitingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 6, 1, 1)
)
qosQueueRateLimitingEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "qosQueueBandwidthBasePort"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "qosQueueBandwidthQueId"),
)
if mibBuilder.loadTexts:
    qosQueueRateLimitingEntry.setStatus("current")
_QosQueueBandwidthBasePort_Type = Integer32
_QosQueueBandwidthBasePort_Object = MibTableColumn
qosQueueBandwidthBasePort = _QosQueueBandwidthBasePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 6, 1, 1, 1),
    _QosQueueBandwidthBasePort_Type()
)
qosQueueBandwidthBasePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosQueueBandwidthBasePort.setStatus("current")


class _QosQueueBandwidthQueId_Type(Unsigned32):
    """Custom type qosQueueBandwidthQueId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_QosQueueBandwidthQueId_Type.__name__ = "Unsigned32"
_QosQueueBandwidthQueId_Object = MibTableColumn
qosQueueBandwidthQueId = _QosQueueBandwidthQueId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 6, 1, 1, 2),
    _QosQueueBandwidthQueId_Type()
)
qosQueueBandwidthQueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosQueueBandwidthQueId.setStatus("current")


class _QosQueueBandwidthMinRate_Type(Integer32):
    """Custom type qosQueueBandwidthMinRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_QosQueueBandwidthMinRate_Type.__name__ = "Integer32"
_QosQueueBandwidthMinRate_Object = MibTableColumn
qosQueueBandwidthMinRate = _QosQueueBandwidthMinRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 6, 1, 1, 3),
    _QosQueueBandwidthMinRate_Type()
)
qosQueueBandwidthMinRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosQueueBandwidthMinRate.setStatus("current")


class _QosQueueBandwidthMaxRate_Type(Integer32):
    """Custom type qosQueueBandwidthMaxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_QosQueueBandwidthMaxRate_Type.__name__ = "Integer32"
_QosQueueBandwidthMaxRate_Object = MibTableColumn
qosQueueBandwidthMaxRate = _QosQueueBandwidthMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 6, 1, 1, 4),
    _QosQueueBandwidthMaxRate_Type()
)
qosQueueBandwidthMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosQueueBandwidthMaxRate.setStatus("current")


class _QosQueueBandwidthRateMode_Type(Integer32):
    """Custom type qosQueueBandwidthRateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("percent", 2),
          ("rate", 1))
    )


_QosQueueBandwidthRateMode_Type.__name__ = "Integer32"
_QosQueueBandwidthRateMode_Object = MibTableColumn
qosQueueBandwidthRateMode = _QosQueueBandwidthRateMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 6, 1, 1, 5),
    _QosQueueBandwidthRateMode_Type()
)
qosQueueBandwidthRateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosQueueBandwidthRateMode.setStatus("current")
_QosBasDscpMapCos_ObjectIdentity = ObjectIdentity
qosBasDscpMapCos = _QosBasDscpMapCos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 7)
)
_QosDscpMapCosTable_Object = MibTable
qosDscpMapCosTable = _QosDscpMapCosTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 7, 1)
)
if mibBuilder.loadTexts:
    qosDscpMapCosTable.setStatus("current")
_QosDscpMapCosEntry_Object = MibTableRow
qosDscpMapCosEntry = _QosDscpMapCosEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 7, 1, 1)
)
qosDscpMapCosEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "qosPortIndex"),
)
if mibBuilder.loadTexts:
    qosDscpMapCosEntry.setStatus("current")
_QosPortIndex_Type = Integer32
_QosPortIndex_Object = MibTableColumn
qosPortIndex = _QosPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 7, 1, 1, 1),
    _QosPortIndex_Type()
)
qosPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPortIndex.setStatus("current")


class _QosTrustMode_Type(Integer32):
    """Custom type qosTrustMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cos", 0),
          ("dscp", 1))
    )


_QosTrustMode_Type.__name__ = "Integer32"
_QosTrustMode_Object = MibTableColumn
qosTrustMode = _QosTrustMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 7, 1, 1, 2),
    _QosTrustMode_Type()
)
qosTrustMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTrustMode.setStatus("current")
_QosDscpValueMapCosTable_Object = MibTable
qosDscpValueMapCosTable = _QosDscpValueMapCosTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 7, 2)
)
if mibBuilder.loadTexts:
    qosDscpValueMapCosTable.setStatus("current")
_QosDscpValueMapCosEntry_Object = MibTableRow
qosDscpValueMapCosEntry = _QosDscpValueMapCosEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 7, 2, 1)
)
qosDscpValueMapCosEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "qosDscpPort"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "qosDscpCos"),
)
if mibBuilder.loadTexts:
    qosDscpValueMapCosEntry.setStatus("current")
_QosDscpPort_Type = Integer32
_QosDscpPort_Object = MibTableColumn
qosDscpPort = _QosDscpPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 7, 2, 1, 1),
    _QosDscpPort_Type()
)
qosDscpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosDscpPort.setStatus("current")
_QosDscpCos_Type = Integer32
_QosDscpCos_Object = MibTableColumn
qosDscpCos = _QosDscpCos_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 7, 2, 1, 2),
    _QosDscpCos_Type()
)
qosDscpCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosDscpCos.setStatus("current")
_QosDscpMapCosList_Type = PortList
_QosDscpMapCosList_Object = MibTableColumn
qosDscpMapCosList = _QosDscpMapCosList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 6, 1, 7, 2, 1, 3),
    _QosDscpMapCosList_Type()
)
qosDscpMapCosList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDscpMapCosList.setStatus("current")
_DlinkACL_ObjectIdentity = ObjectIdentity
dlinkACL = _DlinkACL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7)
)
_AclGroup_ObjectIdentity = ObjectIdentity
aclGroup = _AclGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1)
)
_AclProfile_ObjectIdentity = ObjectIdentity
aclProfile = _AclProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 1)
)
_AclProfileTable_Object = MibTable
aclProfileTable = _AclProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 1, 1)
)
if mibBuilder.loadTexts:
    aclProfileTable.setStatus("current")
_AclProfileEntry_Object = MibTableRow
aclProfileEntry = _AclProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 1, 1, 1)
)
aclProfileEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "aclProfileNo"),
)
if mibBuilder.loadTexts:
    aclProfileEntry.setStatus("current")


class _AclProfileNo_Type(Integer32):
    """Custom type aclProfileNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_AclProfileNo_Type.__name__ = "Integer32"
_AclProfileNo_Object = MibTableColumn
aclProfileNo = _AclProfileNo_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 1, 1, 1, 1),
    _AclProfileNo_Type()
)
aclProfileNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclProfileNo.setStatus("current")


class _AclProfileName_Type(SnmpAdminString):
    """Custom type aclProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AclProfileName_Type.__name__ = "SnmpAdminString"
_AclProfileName_Object = MibTableColumn
aclProfileName = _AclProfileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 1, 1, 1, 2),
    _AclProfileName_Type()
)
aclProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileName.setStatus("current")


class _AclProfileType_Type(Integer32):
    """Custom type aclProfileType based on Integer32"""
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
        *(("expert", 6),
          ("l2", 1),
          ("l3v4", 2),
          ("l3v4Ext", 3),
          ("l3v6", 4),
          ("l3v6Ext", 5))
    )


_AclProfileType_Type.__name__ = "Integer32"
_AclProfileType_Object = MibTableColumn
aclProfileType = _AclProfileType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 1, 1, 1, 3),
    _AclProfileType_Type()
)
aclProfileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileType.setStatus("current")


class _AclProfileRuleCount_Type(Integer32):
    """Custom type aclProfileRuleCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclProfileRuleCount_Type.__name__ = "Integer32"
_AclProfileRuleCount_Object = MibTableColumn
aclProfileRuleCount = _AclProfileRuleCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 1, 1, 1, 4),
    _AclProfileRuleCount_Type()
)
aclProfileRuleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclProfileRuleCount.setStatus("current")


class _AclProfileRemark_Type(SnmpAdminString):
    """Custom type aclProfileRemark based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AclProfileRemark_Type.__name__ = "SnmpAdminString"
_AclProfileRemark_Object = MibTableColumn
aclProfileRemark = _AclProfileRemark_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 1, 1, 1, 5),
    _AclProfileRemark_Type()
)
aclProfileRemark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRemark.setStatus("current")


class _AclProfileRuleIdStart_Type(Integer32):
    """Custom type aclProfileRuleIdStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AclProfileRuleIdStart_Type.__name__ = "Integer32"
_AclProfileRuleIdStart_Object = MibTableColumn
aclProfileRuleIdStart = _AclProfileRuleIdStart_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 1, 1, 1, 6),
    _AclProfileRuleIdStart_Type()
)
aclProfileRuleIdStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleIdStart.setStatus("current")


class _AclProfileRuleIdStep_Type(Integer32):
    """Custom type aclProfileRuleIdStep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AclProfileRuleIdStep_Type.__name__ = "Integer32"
_AclProfileRuleIdStep_Object = MibTableColumn
aclProfileRuleIdStep = _AclProfileRuleIdStep_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 1, 1, 1, 7),
    _AclProfileRuleIdStep_Type()
)
aclProfileRuleIdStep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleIdStep.setStatus("current")


class _AclProfileRuleCounterState_Type(Integer32):
    """Custom type aclProfileRuleCounterState based on Integer32"""
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


_AclProfileRuleCounterState_Type.__name__ = "Integer32"
_AclProfileRuleCounterState_Object = MibTableColumn
aclProfileRuleCounterState = _AclProfileRuleCounterState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 1, 1, 1, 8),
    _AclProfileRuleCounterState_Type()
)
aclProfileRuleCounterState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleCounterState.setStatus("current")


class _AclProfileRuleCounterClear_Type(Integer32):
    """Custom type aclProfileRuleCounterClear based on Integer32"""
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


_AclProfileRuleCounterClear_Type.__name__ = "Integer32"
_AclProfileRuleCounterClear_Object = MibTableColumn
aclProfileRuleCounterClear = _AclProfileRuleCounterClear_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 1, 1, 1, 9),
    _AclProfileRuleCounterClear_Type()
)
aclProfileRuleCounterClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleCounterClear.setStatus("current")
_AclProfileStatus_Type = RowStatus
_AclProfileStatus_Object = MibTableColumn
aclProfileStatus = _AclProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 1, 1, 1, 10),
    _AclProfileStatus_Type()
)
aclProfileStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileStatus.setStatus("current")
_AclL2Rule_ObjectIdentity = ObjectIdentity
aclL2Rule = _AclL2Rule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 2)
)
_AclL2RuleTable_Object = MibTable
aclL2RuleTable = _AclL2RuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 2, 1)
)
if mibBuilder.loadTexts:
    aclL2RuleTable.setStatus("current")
_AclL2RuleEntry_Object = MibTableRow
aclL2RuleEntry = _AclL2RuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 2, 1, 1)
)
aclL2RuleEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "aclL2ProfileID"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "aclL2AccessID"),
)
if mibBuilder.loadTexts:
    aclL2RuleEntry.setStatus("current")


class _AclL2ProfileID_Type(Integer32):
    """Custom type aclL2ProfileID based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_AclL2ProfileID_Type.__name__ = "Integer32"
_AclL2ProfileID_Object = MibTableColumn
aclL2ProfileID = _AclL2ProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 2, 1, 1, 1),
    _AclL2ProfileID_Type()
)
aclL2ProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL2ProfileID.setStatus("current")


class _AclL2AccessID_Type(Integer32):
    """Custom type aclL2AccessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AclL2AccessID_Type.__name__ = "Integer32"
_AclL2AccessID_Object = MibTableColumn
aclL2AccessID = _AclL2AccessID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 2, 1, 1, 2),
    _AclL2AccessID_Type()
)
aclL2AccessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL2AccessID.setStatus("current")


class _AclL2RuleEtherType_Type(Integer32):
    """Custom type aclL2RuleEtherType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclL2RuleEtherType_Type.__name__ = "Integer32"
_AclL2RuleEtherType_Object = MibTableColumn
aclL2RuleEtherType = _AclL2RuleEtherType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 2, 1, 1, 3),
    _AclL2RuleEtherType_Type()
)
aclL2RuleEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2RuleEtherType.setStatus("current")
_AclL2RuleDstMacAddr_Type = MacAddress
_AclL2RuleDstMacAddr_Object = MibTableColumn
aclL2RuleDstMacAddr = _AclL2RuleDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 2, 1, 1, 4),
    _AclL2RuleDstMacAddr_Type()
)
aclL2RuleDstMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2RuleDstMacAddr.setStatus("current")
_AclL2RuleSrcMacAddr_Type = MacAddress
_AclL2RuleSrcMacAddr_Object = MibTableColumn
aclL2RuleSrcMacAddr = _AclL2RuleSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 2, 1, 1, 5),
    _AclL2RuleSrcMacAddr_Type()
)
aclL2RuleSrcMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2RuleSrcMacAddr.setStatus("current")


class _AclL2RuleVlanId_Type(Integer32):
    """Custom type aclL2RuleVlanId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4094),
    )


_AclL2RuleVlanId_Type.__name__ = "Integer32"
_AclL2RuleVlanId_Object = MibTableColumn
aclL2RuleVlanId = _AclL2RuleVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 2, 1, 1, 6),
    _AclL2RuleVlanId_Type()
)
aclL2RuleVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2RuleVlanId.setStatus("current")


class _AclL2Rule1pPriority_Type(Integer32):
    """Custom type aclL2Rule1pPriority based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_AclL2Rule1pPriority_Type.__name__ = "Integer32"
_AclL2Rule1pPriority_Object = MibTableColumn
aclL2Rule1pPriority = _AclL2Rule1pPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 2, 1, 1, 7),
    _AclL2Rule1pPriority_Type()
)
aclL2Rule1pPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2Rule1pPriority.setStatus("current")
_AclL2RuleDstMacAddrMask_Type = MacAddress
_AclL2RuleDstMacAddrMask_Object = MibTableColumn
aclL2RuleDstMacAddrMask = _AclL2RuleDstMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 2, 1, 1, 8),
    _AclL2RuleDstMacAddrMask_Type()
)
aclL2RuleDstMacAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2RuleDstMacAddrMask.setStatus("current")
_AclL2RuleSrcMacAddrMask_Type = MacAddress
_AclL2RuleSrcMacAddrMask_Object = MibTableColumn
aclL2RuleSrcMacAddrMask = _AclL2RuleSrcMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 2, 1, 1, 9),
    _AclL2RuleSrcMacAddrMask_Type()
)
aclL2RuleSrcMacAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2RuleSrcMacAddrMask.setStatus("current")


class _AclL2RuleTimeRange_Type(SnmpAdminString):
    """Custom type aclL2RuleTimeRange based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AclL2RuleTimeRange_Type.__name__ = "SnmpAdminString"
_AclL2RuleTimeRange_Object = MibTableColumn
aclL2RuleTimeRange = _AclL2RuleTimeRange_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 2, 1, 1, 10),
    _AclL2RuleTimeRange_Type()
)
aclL2RuleTimeRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2RuleTimeRange.setStatus("current")


class _AclL2RuleAction_Type(Integer32):
    """Custom type aclL2RuleAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("drop", 2))
    )


_AclL2RuleAction_Type.__name__ = "Integer32"
_AclL2RuleAction_Object = MibTableColumn
aclL2RuleAction = _AclL2RuleAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 2, 1, 1, 11),
    _AclL2RuleAction_Type()
)
aclL2RuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2RuleAction.setStatus("current")


class _AclL2RuleEtherTypeMask_Type(Integer32):
    """Custom type aclL2RuleEtherTypeMask based on Integer32"""
    defaultValue = -1


_AclL2RuleEtherTypeMask_Object = MibTableColumn
aclL2RuleEtherTypeMask = _AclL2RuleEtherTypeMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 2, 1, 1, 12),
    _AclL2RuleEtherTypeMask_Type()
)
aclL2RuleEtherTypeMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2RuleEtherTypeMask.setStatus("current")
_AclL2RuleMatchCount_Type = Counter32
_AclL2RuleMatchCount_Object = MibTableColumn
aclL2RuleMatchCount = _AclL2RuleMatchCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 2, 1, 1, 13),
    _AclL2RuleMatchCount_Type()
)
aclL2RuleMatchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL2RuleMatchCount.setStatus("current")
_AclL2RuleStatus_Type = RowStatus
_AclL2RuleStatus_Object = MibTableColumn
aclL2RuleStatus = _AclL2RuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 2, 1, 1, 14),
    _AclL2RuleStatus_Type()
)
aclL2RuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2RuleStatus.setStatus("current")
_AclL3v4Rule_ObjectIdentity = ObjectIdentity
aclL3v4Rule = _AclL3v4Rule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 3)
)
_AclL3v4RuleTable_Object = MibTable
aclL3v4RuleTable = _AclL3v4RuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 3, 1)
)
if mibBuilder.loadTexts:
    aclL3v4RuleTable.setStatus("current")
_AclL3v4RuleEntry_Object = MibTableRow
aclL3v4RuleEntry = _AclL3v4RuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 3, 1, 1)
)
aclL3v4RuleEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "aclL3v4RuleProfileNo"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "aclL3v4RuleAccessID"),
)
if mibBuilder.loadTexts:
    aclL3v4RuleEntry.setStatus("current")


class _AclL3v4RuleProfileNo_Type(Integer32):
    """Custom type aclL3v4RuleProfileNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_AclL3v4RuleProfileNo_Type.__name__ = "Integer32"
_AclL3v4RuleProfileNo_Object = MibTableColumn
aclL3v4RuleProfileNo = _AclL3v4RuleProfileNo_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 3, 1, 1, 1),
    _AclL3v4RuleProfileNo_Type()
)
aclL3v4RuleProfileNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL3v4RuleProfileNo.setStatus("current")


class _AclL3v4RuleAccessID_Type(Integer32):
    """Custom type aclL3v4RuleAccessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AclL3v4RuleAccessID_Type.__name__ = "Integer32"
_AclL3v4RuleAccessID_Object = MibTableColumn
aclL3v4RuleAccessID = _AclL3v4RuleAccessID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 3, 1, 1, 2),
    _AclL3v4RuleAccessID_Type()
)
aclL3v4RuleAccessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL3v4RuleAccessID.setStatus("current")


class _AclL3v4RuleDstIpAddr_Type(IpAddress):
    """Custom type aclL3v4RuleDstIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_AclL3v4RuleDstIpAddr_Object = MibTableColumn
aclL3v4RuleDstIpAddr = _AclL3v4RuleDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 3, 1, 1, 3),
    _AclL3v4RuleDstIpAddr_Type()
)
aclL3v4RuleDstIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4RuleDstIpAddr.setStatus("current")


class _AclL3v4RuleSrcIpAddr_Type(IpAddress):
    """Custom type aclL3v4RuleSrcIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_AclL3v4RuleSrcIpAddr_Object = MibTableColumn
aclL3v4RuleSrcIpAddr = _AclL3v4RuleSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 3, 1, 1, 4),
    _AclL3v4RuleSrcIpAddr_Type()
)
aclL3v4RuleSrcIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4RuleSrcIpAddr.setStatus("current")


class _AclL3v4RuleDstIpAddrMask_Type(IpAddress):
    """Custom type aclL3v4RuleDstIpAddrMask based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_AclL3v4RuleDstIpAddrMask_Object = MibTableColumn
aclL3v4RuleDstIpAddrMask = _AclL3v4RuleDstIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 3, 1, 1, 5),
    _AclL3v4RuleDstIpAddrMask_Type()
)
aclL3v4RuleDstIpAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4RuleDstIpAddrMask.setStatus("current")


class _AclL3v4RuleSrcIpAddrMask_Type(IpAddress):
    """Custom type aclL3v4RuleSrcIpAddrMask based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_AclL3v4RuleSrcIpAddrMask_Object = MibTableColumn
aclL3v4RuleSrcIpAddrMask = _AclL3v4RuleSrcIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 3, 1, 1, 6),
    _AclL3v4RuleSrcIpAddrMask_Type()
)
aclL3v4RuleSrcIpAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4RuleSrcIpAddrMask.setStatus("current")


class _AclL3v4RuleAction_Type(Integer32):
    """Custom type aclL3v4RuleAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("drop", 2))
    )


_AclL3v4RuleAction_Type.__name__ = "Integer32"
_AclL3v4RuleAction_Object = MibTableColumn
aclL3v4RuleAction = _AclL3v4RuleAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 3, 1, 1, 7),
    _AclL3v4RuleAction_Type()
)
aclL3v4RuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4RuleAction.setStatus("current")


class _AclL3v4RuleTimeRange_Type(SnmpAdminString):
    """Custom type aclL3v4RuleTimeRange based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AclL3v4RuleTimeRange_Type.__name__ = "SnmpAdminString"
_AclL3v4RuleTimeRange_Object = MibTableColumn
aclL3v4RuleTimeRange = _AclL3v4RuleTimeRange_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 3, 1, 1, 8),
    _AclL3v4RuleTimeRange_Type()
)
aclL3v4RuleTimeRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4RuleTimeRange.setStatus("current")
_AclL3v4RuleMatchCount_Type = Counter32
_AclL3v4RuleMatchCount_Object = MibTableColumn
aclL3v4RuleMatchCount = _AclL3v4RuleMatchCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 3, 1, 1, 9),
    _AclL3v4RuleMatchCount_Type()
)
aclL3v4RuleMatchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL3v4RuleMatchCount.setStatus("current")
_AclL3v4RuleStatus_Type = RowStatus
_AclL3v4RuleStatus_Object = MibTableColumn
aclL3v4RuleStatus = _AclL3v4RuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 3, 1, 1, 10),
    _AclL3v4RuleStatus_Type()
)
aclL3v4RuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4RuleStatus.setStatus("current")
_AclL3v4ExtRule_ObjectIdentity = ObjectIdentity
aclL3v4ExtRule = _AclL3v4ExtRule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 4)
)
_AclL3v4ExtRuleTable_Object = MibTable
aclL3v4ExtRuleTable = _AclL3v4ExtRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 4, 1)
)
if mibBuilder.loadTexts:
    aclL3v4ExtRuleTable.setStatus("current")
_AclL3v4ExtRuleEntry_Object = MibTableRow
aclL3v4ExtRuleEntry = _AclL3v4ExtRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 4, 1, 1)
)
aclL3v4ExtRuleEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "aclL3v4ExtRuleProfileNo"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "aclL3v4ExtRuleAccessID"),
)
if mibBuilder.loadTexts:
    aclL3v4ExtRuleEntry.setStatus("current")


class _AclL3v4ExtRuleProfileNo_Type(Integer32):
    """Custom type aclL3v4ExtRuleProfileNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_AclL3v4ExtRuleProfileNo_Type.__name__ = "Integer32"
_AclL3v4ExtRuleProfileNo_Object = MibTableColumn
aclL3v4ExtRuleProfileNo = _AclL3v4ExtRuleProfileNo_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 4, 1, 1, 1),
    _AclL3v4ExtRuleProfileNo_Type()
)
aclL3v4ExtRuleProfileNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleProfileNo.setStatus("current")


class _AclL3v4ExtRuleAccessID_Type(Integer32):
    """Custom type aclL3v4ExtRuleAccessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AclL3v4ExtRuleAccessID_Type.__name__ = "Integer32"
_AclL3v4ExtRuleAccessID_Object = MibTableColumn
aclL3v4ExtRuleAccessID = _AclL3v4ExtRuleAccessID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 4, 1, 1, 2),
    _AclL3v4ExtRuleAccessID_Type()
)
aclL3v4ExtRuleAccessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleAccessID.setStatus("current")


class _AclL3v4ExtRuleProtocol_Type(Integer32):
    """Custom type aclL3v4ExtRuleProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              6,
              17,
              47,
              50,
              88,
              89,
              94,
              103,
              108,
              112)
        )
    )
    namedValues = NamedValues(
        *(("eigrp", 88),
          ("esp", 50),
          ("gre", 47),
          ("icmp", 1),
          ("igmp", 2),
          ("ipinip", 94),
          ("none", 0),
          ("ospf", 89),
          ("pcp", 108),
          ("pim", 103),
          ("tcp", 6),
          ("udp", 17),
          ("vrrp", 112))
    )


_AclL3v4ExtRuleProtocol_Type.__name__ = "Integer32"
_AclL3v4ExtRuleProtocol_Object = MibTableColumn
aclL3v4ExtRuleProtocol = _AclL3v4ExtRuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 4, 1, 1, 3),
    _AclL3v4ExtRuleProtocol_Type()
)
aclL3v4ExtRuleProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleProtocol.setStatus("current")


class _AclL3v4ExtRuleFragments_Type(Integer32):
    """Custom type aclL3v4ExtRuleFragments based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("none", 0))
    )


_AclL3v4ExtRuleFragments_Type.__name__ = "Integer32"
_AclL3v4ExtRuleFragments_Object = MibTableColumn
aclL3v4ExtRuleFragments = _AclL3v4ExtRuleFragments_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 4, 1, 1, 4),
    _AclL3v4ExtRuleFragments_Type()
)
aclL3v4ExtRuleFragments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleFragments.setStatus("current")


class _AclL3v4ExtRuleICMPMessageType_Type(Integer32):
    """Custom type aclL3v4ExtRuleICMPMessageType based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_AclL3v4ExtRuleICMPMessageType_Type.__name__ = "Integer32"
_AclL3v4ExtRuleICMPMessageType_Object = MibTableColumn
aclL3v4ExtRuleICMPMessageType = _AclL3v4ExtRuleICMPMessageType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 4, 1, 1, 5),
    _AclL3v4ExtRuleICMPMessageType_Type()
)
aclL3v4ExtRuleICMPMessageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleICMPMessageType.setStatus("current")


class _AclL3v4ExtRuleICMPMessageCode_Type(Integer32):
    """Custom type aclL3v4ExtRuleICMPMessageCode based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_AclL3v4ExtRuleICMPMessageCode_Type.__name__ = "Integer32"
_AclL3v4ExtRuleICMPMessageCode_Object = MibTableColumn
aclL3v4ExtRuleICMPMessageCode = _AclL3v4ExtRuleICMPMessageCode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 4, 1, 1, 6),
    _AclL3v4ExtRuleICMPMessageCode_Type()
)
aclL3v4ExtRuleICMPMessageCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleICMPMessageCode.setStatus("current")


class _AclL3v4ExtRuleDstIpAddr_Type(IpAddress):
    """Custom type aclL3v4ExtRuleDstIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_AclL3v4ExtRuleDstIpAddr_Object = MibTableColumn
aclL3v4ExtRuleDstIpAddr = _AclL3v4ExtRuleDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 4, 1, 1, 7),
    _AclL3v4ExtRuleDstIpAddr_Type()
)
aclL3v4ExtRuleDstIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleDstIpAddr.setStatus("current")


class _AclL3v4ExtRuleSrcIpAddr_Type(IpAddress):
    """Custom type aclL3v4ExtRuleSrcIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_AclL3v4ExtRuleSrcIpAddr_Object = MibTableColumn
aclL3v4ExtRuleSrcIpAddr = _AclL3v4ExtRuleSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 4, 1, 1, 8),
    _AclL3v4ExtRuleSrcIpAddr_Type()
)
aclL3v4ExtRuleSrcIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleSrcIpAddr.setStatus("current")


class _AclL3v4ExtRuleDstIpAddrMask_Type(IpAddress):
    """Custom type aclL3v4ExtRuleDstIpAddrMask based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_AclL3v4ExtRuleDstIpAddrMask_Object = MibTableColumn
aclL3v4ExtRuleDstIpAddrMask = _AclL3v4ExtRuleDstIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 4, 1, 1, 9),
    _AclL3v4ExtRuleDstIpAddrMask_Type()
)
aclL3v4ExtRuleDstIpAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleDstIpAddrMask.setStatus("current")


class _AclL3v4ExtRuleSrcIpAddrMask_Type(IpAddress):
    """Custom type aclL3v4ExtRuleSrcIpAddrMask based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_AclL3v4ExtRuleSrcIpAddrMask_Object = MibTableColumn
aclL3v4ExtRuleSrcIpAddrMask = _AclL3v4ExtRuleSrcIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 4, 1, 1, 10),
    _AclL3v4ExtRuleSrcIpAddrMask_Type()
)
aclL3v4ExtRuleSrcIpAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleSrcIpAddrMask.setStatus("current")


class _AclL3v4ExtRuleTcpUdpDstOperator_Type(Integer32):
    """Custom type aclL3v4ExtRuleTcpUdpDstOperator based on Integer32"""
    defaultValue = 1

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
        *(("eq", 2),
          ("gt", 3),
          ("lt", 4),
          ("neq", 5),
          ("none", 1),
          ("range", 6))
    )


_AclL3v4ExtRuleTcpUdpDstOperator_Type.__name__ = "Integer32"
_AclL3v4ExtRuleTcpUdpDstOperator_Object = MibTableColumn
aclL3v4ExtRuleTcpUdpDstOperator = _AclL3v4ExtRuleTcpUdpDstOperator_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 4, 1, 1, 11),
    _AclL3v4ExtRuleTcpUdpDstOperator_Type()
)
aclL3v4ExtRuleTcpUdpDstOperator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleTcpUdpDstOperator.setStatus("current")


class _AclL3v4ExtRuleTcpUdpDstPort_Type(Integer32):
    """Custom type aclL3v4ExtRuleTcpUdpDstPort based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_AclL3v4ExtRuleTcpUdpDstPort_Type.__name__ = "Integer32"
_AclL3v4ExtRuleTcpUdpDstPort_Object = MibTableColumn
aclL3v4ExtRuleTcpUdpDstPort = _AclL3v4ExtRuleTcpUdpDstPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 4, 1, 1, 12),
    _AclL3v4ExtRuleTcpUdpDstPort_Type()
)
aclL3v4ExtRuleTcpUdpDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleTcpUdpDstPort.setStatus("current")


class _AclL3v4ExtRuleTcpUdpMinDstPort_Type(Unsigned32):
    """Custom type aclL3v4ExtRuleTcpUdpMinDstPort based on Unsigned32"""
    defaultValue = 0


_AclL3v4ExtRuleTcpUdpMinDstPort_Object = MibTableColumn
aclL3v4ExtRuleTcpUdpMinDstPort = _AclL3v4ExtRuleTcpUdpMinDstPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 4, 1, 1, 13),
    _AclL3v4ExtRuleTcpUdpMinDstPort_Type()
)
aclL3v4ExtRuleTcpUdpMinDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleTcpUdpMinDstPort.setStatus("current")


class _AclL3v4ExtRuleTcpUdpMaxDstPort_Type(Unsigned32):
    """Custom type aclL3v4ExtRuleTcpUdpMaxDstPort based on Unsigned32"""
    defaultValue = 65535


_AclL3v4ExtRuleTcpUdpMaxDstPort_Object = MibTableColumn
aclL3v4ExtRuleTcpUdpMaxDstPort = _AclL3v4ExtRuleTcpUdpMaxDstPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 4, 1, 1, 14),
    _AclL3v4ExtRuleTcpUdpMaxDstPort_Type()
)
aclL3v4ExtRuleTcpUdpMaxDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleTcpUdpMaxDstPort.setStatus("current")


class _AclL3v4ExtRuleTcpUdpSrcOperator_Type(Integer32):
    """Custom type aclL3v4ExtRuleTcpUdpSrcOperator based on Integer32"""
    defaultValue = 1

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
        *(("eq", 2),
          ("gt", 3),
          ("lt", 4),
          ("neq", 5),
          ("none", 1),
          ("range", 6))
    )


_AclL3v4ExtRuleTcpUdpSrcOperator_Type.__name__ = "Integer32"
_AclL3v4ExtRuleTcpUdpSrcOperator_Object = MibTableColumn
aclL3v4ExtRuleTcpUdpSrcOperator = _AclL3v4ExtRuleTcpUdpSrcOperator_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 4, 1, 1, 15),
    _AclL3v4ExtRuleTcpUdpSrcOperator_Type()
)
aclL3v4ExtRuleTcpUdpSrcOperator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleTcpUdpSrcOperator.setStatus("current")


class _AclL3v4ExtRuleTcpUdpSrcPort_Type(Integer32):
    """Custom type aclL3v4ExtRuleTcpUdpSrcPort based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_AclL3v4ExtRuleTcpUdpSrcPort_Type.__name__ = "Integer32"
_AclL3v4ExtRuleTcpUdpSrcPort_Object = MibTableColumn
aclL3v4ExtRuleTcpUdpSrcPort = _AclL3v4ExtRuleTcpUdpSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 4, 1, 1, 16),
    _AclL3v4ExtRuleTcpUdpSrcPort_Type()
)
aclL3v4ExtRuleTcpUdpSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleTcpUdpSrcPort.setStatus("current")


class _AclL3v4ExtRuleTcpUdpMinSrcPort_Type(Unsigned32):
    """Custom type aclL3v4ExtRuleTcpUdpMinSrcPort based on Unsigned32"""
    defaultValue = 0


_AclL3v4ExtRuleTcpUdpMinSrcPort_Object = MibTableColumn
aclL3v4ExtRuleTcpUdpMinSrcPort = _AclL3v4ExtRuleTcpUdpMinSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 4, 1, 1, 17),
    _AclL3v4ExtRuleTcpUdpMinSrcPort_Type()
)
aclL3v4ExtRuleTcpUdpMinSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleTcpUdpMinSrcPort.setStatus("current")


class _AclL3v4ExtRuleTcpUdpMaxSrcPort_Type(Unsigned32):
    """Custom type aclL3v4ExtRuleTcpUdpMaxSrcPort based on Unsigned32"""
    defaultValue = 65535


_AclL3v4ExtRuleTcpUdpMaxSrcPort_Object = MibTableColumn
aclL3v4ExtRuleTcpUdpMaxSrcPort = _AclL3v4ExtRuleTcpUdpMaxSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 4, 1, 1, 18),
    _AclL3v4ExtRuleTcpUdpMaxSrcPort_Type()
)
aclL3v4ExtRuleTcpUdpMaxSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleTcpUdpMaxSrcPort.setStatus("current")


class _AclL3v4ExtRuleIPPrecedence_Type(Integer32):
    """Custom type aclL3v4ExtRuleIPPrecedence based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_AclL3v4ExtRuleIPPrecedence_Type.__name__ = "Integer32"
_AclL3v4ExtRuleIPPrecedence_Object = MibTableColumn
aclL3v4ExtRuleIPPrecedence = _AclL3v4ExtRuleIPPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 4, 1, 1, 19),
    _AclL3v4ExtRuleIPPrecedence_Type()
)
aclL3v4ExtRuleIPPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleIPPrecedence.setStatus("current")


class _AclL3v4ExtRuleDscp_Type(Integer32):
    """Custom type aclL3v4ExtRuleDscp based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_AclL3v4ExtRuleDscp_Type.__name__ = "Integer32"
_AclL3v4ExtRuleDscp_Object = MibTableColumn
aclL3v4ExtRuleDscp = _AclL3v4ExtRuleDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 4, 1, 1, 20),
    _AclL3v4ExtRuleDscp_Type()
)
aclL3v4ExtRuleDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleDscp.setStatus("current")


class _AclL3v4ExtRuleToS_Type(Integer32):
    """Custom type aclL3v4ExtRuleToS based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 15),
    )


_AclL3v4ExtRuleToS_Type.__name__ = "Integer32"
_AclL3v4ExtRuleToS_Object = MibTableColumn
aclL3v4ExtRuleToS = _AclL3v4ExtRuleToS_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 4, 1, 1, 21),
    _AclL3v4ExtRuleToS_Type()
)
aclL3v4ExtRuleToS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleToS.setStatus("current")


class _AclL3v4ExtRuleTcpAckBit_Type(Integer32):
    """Custom type aclL3v4ExtRuleTcpAckBit based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dont_care", 3),
          ("establish", 1),
          ("notEstablish", 2))
    )


_AclL3v4ExtRuleTcpAckBit_Type.__name__ = "Integer32"
_AclL3v4ExtRuleTcpAckBit_Object = MibTableColumn
aclL3v4ExtRuleTcpAckBit = _AclL3v4ExtRuleTcpAckBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 4, 1, 1, 22),
    _AclL3v4ExtRuleTcpAckBit_Type()
)
aclL3v4ExtRuleTcpAckBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleTcpAckBit.setStatus("current")


class _AclL3v4ExtRuleTcpRstBit_Type(Integer32):
    """Custom type aclL3v4ExtRuleTcpRstBit based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dont_care", 3),
          ("establish", 1),
          ("notEstablish", 2))
    )


_AclL3v4ExtRuleTcpRstBit_Type.__name__ = "Integer32"
_AclL3v4ExtRuleTcpRstBit_Object = MibTableColumn
aclL3v4ExtRuleTcpRstBit = _AclL3v4ExtRuleTcpRstBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 4, 1, 1, 23),
    _AclL3v4ExtRuleTcpRstBit_Type()
)
aclL3v4ExtRuleTcpRstBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleTcpRstBit.setStatus("current")


class _AclL3v4ExtRuleTcpUrgBit_Type(Integer32):
    """Custom type aclL3v4ExtRuleTcpUrgBit based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dont_care", 3),
          ("establish", 1),
          ("notEstablish", 2))
    )


_AclL3v4ExtRuleTcpUrgBit_Type.__name__ = "Integer32"
_AclL3v4ExtRuleTcpUrgBit_Object = MibTableColumn
aclL3v4ExtRuleTcpUrgBit = _AclL3v4ExtRuleTcpUrgBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 4, 1, 1, 24),
    _AclL3v4ExtRuleTcpUrgBit_Type()
)
aclL3v4ExtRuleTcpUrgBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleTcpUrgBit.setStatus("current")


class _AclL3v4ExtRuleTcpPshBit_Type(Integer32):
    """Custom type aclL3v4ExtRuleTcpPshBit based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dont_care", 3),
          ("establish", 1),
          ("notEstablish", 2))
    )


_AclL3v4ExtRuleTcpPshBit_Type.__name__ = "Integer32"
_AclL3v4ExtRuleTcpPshBit_Object = MibTableColumn
aclL3v4ExtRuleTcpPshBit = _AclL3v4ExtRuleTcpPshBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 4, 1, 1, 25),
    _AclL3v4ExtRuleTcpPshBit_Type()
)
aclL3v4ExtRuleTcpPshBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleTcpPshBit.setStatus("current")


class _AclL3v4ExtRuleTcpSynBit_Type(Integer32):
    """Custom type aclL3v4ExtRuleTcpSynBit based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dont_care", 3),
          ("establish", 1),
          ("notEstablish", 2))
    )


_AclL3v4ExtRuleTcpSynBit_Type.__name__ = "Integer32"
_AclL3v4ExtRuleTcpSynBit_Object = MibTableColumn
aclL3v4ExtRuleTcpSynBit = _AclL3v4ExtRuleTcpSynBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 4, 1, 1, 26),
    _AclL3v4ExtRuleTcpSynBit_Type()
)
aclL3v4ExtRuleTcpSynBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleTcpSynBit.setStatus("current")


class _AclL3v4ExtRuleTcpFinBit_Type(Integer32):
    """Custom type aclL3v4ExtRuleTcpFinBit based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dont_care", 3),
          ("establish", 1),
          ("notEstablish", 2))
    )


_AclL3v4ExtRuleTcpFinBit_Type.__name__ = "Integer32"
_AclL3v4ExtRuleTcpFinBit_Object = MibTableColumn
aclL3v4ExtRuleTcpFinBit = _AclL3v4ExtRuleTcpFinBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 4, 1, 1, 27),
    _AclL3v4ExtRuleTcpFinBit_Type()
)
aclL3v4ExtRuleTcpFinBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleTcpFinBit.setStatus("current")


class _AclL3v4ExtRuleAction_Type(Integer32):
    """Custom type aclL3v4ExtRuleAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("drop", 2))
    )


_AclL3v4ExtRuleAction_Type.__name__ = "Integer32"
_AclL3v4ExtRuleAction_Object = MibTableColumn
aclL3v4ExtRuleAction = _AclL3v4ExtRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 4, 1, 1, 28),
    _AclL3v4ExtRuleAction_Type()
)
aclL3v4ExtRuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleAction.setStatus("current")


class _AclL3v4ExtRuleTimeRange_Type(SnmpAdminString):
    """Custom type aclL3v4ExtRuleTimeRange based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AclL3v4ExtRuleTimeRange_Type.__name__ = "SnmpAdminString"
_AclL3v4ExtRuleTimeRange_Object = MibTableColumn
aclL3v4ExtRuleTimeRange = _AclL3v4ExtRuleTimeRange_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 4, 1, 1, 29),
    _AclL3v4ExtRuleTimeRange_Type()
)
aclL3v4ExtRuleTimeRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleTimeRange.setStatus("current")
_AclL3v4ExtRuleMatchCount_Type = Counter32
_AclL3v4ExtRuleMatchCount_Object = MibTableColumn
aclL3v4ExtRuleMatchCount = _AclL3v4ExtRuleMatchCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 4, 1, 1, 30),
    _AclL3v4ExtRuleMatchCount_Type()
)
aclL3v4ExtRuleMatchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleMatchCount.setStatus("current")
_AclL3v4ExtRuleStatus_Type = RowStatus
_AclL3v4ExtRuleStatus_Object = MibTableColumn
aclL3v4ExtRuleStatus = _AclL3v4ExtRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 4, 1, 1, 31),
    _AclL3v4ExtRuleStatus_Type()
)
aclL3v4ExtRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleStatus.setStatus("current")
_AclL3v6Rule_ObjectIdentity = ObjectIdentity
aclL3v6Rule = _AclL3v6Rule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 5)
)
_AclL3v6RuleTable_Object = MibTable
aclL3v6RuleTable = _AclL3v6RuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 5, 1)
)
if mibBuilder.loadTexts:
    aclL3v6RuleTable.setStatus("current")
_AclL3v6RuleEntry_Object = MibTableRow
aclL3v6RuleEntry = _AclL3v6RuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 5, 1, 1)
)
aclL3v6RuleEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "aclL3v6RuleProfileNo"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "aclL3v6RuleAccessID"),
)
if mibBuilder.loadTexts:
    aclL3v6RuleEntry.setStatus("current")


class _AclL3v6RuleProfileNo_Type(Integer32):
    """Custom type aclL3v6RuleProfileNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_AclL3v6RuleProfileNo_Type.__name__ = "Integer32"
_AclL3v6RuleProfileNo_Object = MibTableColumn
aclL3v6RuleProfileNo = _AclL3v6RuleProfileNo_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 5, 1, 1, 1),
    _AclL3v6RuleProfileNo_Type()
)
aclL3v6RuleProfileNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL3v6RuleProfileNo.setStatus("current")


class _AclL3v6RuleAccessID_Type(Integer32):
    """Custom type aclL3v6RuleAccessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AclL3v6RuleAccessID_Type.__name__ = "Integer32"
_AclL3v6RuleAccessID_Object = MibTableColumn
aclL3v6RuleAccessID = _AclL3v6RuleAccessID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 5, 1, 1, 2),
    _AclL3v6RuleAccessID_Type()
)
aclL3v6RuleAccessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL3v6RuleAccessID.setStatus("current")
_AclL3v6RuleDstIpv6Addr_Type = Ipv6Address
_AclL3v6RuleDstIpv6Addr_Object = MibTableColumn
aclL3v6RuleDstIpv6Addr = _AclL3v6RuleDstIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 5, 1, 1, 3),
    _AclL3v6RuleDstIpv6Addr_Type()
)
aclL3v6RuleDstIpv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v6RuleDstIpv6Addr.setStatus("current")
_AclL3v6RuleSrcIpv6Addr_Type = Ipv6Address
_AclL3v6RuleSrcIpv6Addr_Object = MibTableColumn
aclL3v6RuleSrcIpv6Addr = _AclL3v6RuleSrcIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 5, 1, 1, 4),
    _AclL3v6RuleSrcIpv6Addr_Type()
)
aclL3v6RuleSrcIpv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v6RuleSrcIpv6Addr.setStatus("current")


class _AclL3v6RuleDstIpv6AddrPrefixLen_Type(InetAddressPrefixLength):
    """Custom type aclL3v6RuleDstIpv6AddrPrefixLen based on InetAddressPrefixLength"""
    defaultValue = 0


_AclL3v6RuleDstIpv6AddrPrefixLen_Object = MibTableColumn
aclL3v6RuleDstIpv6AddrPrefixLen = _AclL3v6RuleDstIpv6AddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 5, 1, 1, 5),
    _AclL3v6RuleDstIpv6AddrPrefixLen_Type()
)
aclL3v6RuleDstIpv6AddrPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v6RuleDstIpv6AddrPrefixLen.setStatus("current")


class _AclL3v6RuleSrcIpv6AddrPrefixLen_Type(InetAddressPrefixLength):
    """Custom type aclL3v6RuleSrcIpv6AddrPrefixLen based on InetAddressPrefixLength"""
    defaultValue = 0


_AclL3v6RuleSrcIpv6AddrPrefixLen_Object = MibTableColumn
aclL3v6RuleSrcIpv6AddrPrefixLen = _AclL3v6RuleSrcIpv6AddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 5, 1, 1, 6),
    _AclL3v6RuleSrcIpv6AddrPrefixLen_Type()
)
aclL3v6RuleSrcIpv6AddrPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v6RuleSrcIpv6AddrPrefixLen.setStatus("current")


class _AclL3v6RuleAction_Type(Integer32):
    """Custom type aclL3v6RuleAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("drop", 2))
    )


_AclL3v6RuleAction_Type.__name__ = "Integer32"
_AclL3v6RuleAction_Object = MibTableColumn
aclL3v6RuleAction = _AclL3v6RuleAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 5, 1, 1, 7),
    _AclL3v6RuleAction_Type()
)
aclL3v6RuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v6RuleAction.setStatus("current")


class _AclL3v6RuleTimeRange_Type(SnmpAdminString):
    """Custom type aclL3v6RuleTimeRange based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AclL3v6RuleTimeRange_Type.__name__ = "SnmpAdminString"
_AclL3v6RuleTimeRange_Object = MibTableColumn
aclL3v6RuleTimeRange = _AclL3v6RuleTimeRange_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 5, 1, 1, 8),
    _AclL3v6RuleTimeRange_Type()
)
aclL3v6RuleTimeRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v6RuleTimeRange.setStatus("current")
_AclL3v6RuleMatchCount_Type = Counter32
_AclL3v6RuleMatchCount_Object = MibTableColumn
aclL3v6RuleMatchCount = _AclL3v6RuleMatchCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 5, 1, 1, 9),
    _AclL3v6RuleMatchCount_Type()
)
aclL3v6RuleMatchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL3v6RuleMatchCount.setStatus("current")
_AclL3v6RuleStatus_Type = RowStatus
_AclL3v6RuleStatus_Object = MibTableColumn
aclL3v6RuleStatus = _AclL3v6RuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 5, 1, 1, 10),
    _AclL3v6RuleStatus_Type()
)
aclL3v6RuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v6RuleStatus.setStatus("current")
_AclL3v6ExtRule_ObjectIdentity = ObjectIdentity
aclL3v6ExtRule = _AclL3v6ExtRule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 6)
)
_AclL3v6ExtRuleTable_Object = MibTable
aclL3v6ExtRuleTable = _AclL3v6ExtRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 6, 1)
)
if mibBuilder.loadTexts:
    aclL3v6ExtRuleTable.setStatus("current")
_AclL3v6ExtRuleEntry_Object = MibTableRow
aclL3v6ExtRuleEntry = _AclL3v6ExtRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 6, 1, 1)
)
aclL3v6ExtRuleEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "aclL3v6ExtRuleProfileNo"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "aclL3v6ExtRuleAccessID"),
)
if mibBuilder.loadTexts:
    aclL3v6ExtRuleEntry.setStatus("current")


class _AclL3v6ExtRuleProfileNo_Type(Integer32):
    """Custom type aclL3v6ExtRuleProfileNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_AclL3v6ExtRuleProfileNo_Type.__name__ = "Integer32"
_AclL3v6ExtRuleProfileNo_Object = MibTableColumn
aclL3v6ExtRuleProfileNo = _AclL3v6ExtRuleProfileNo_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 6, 1, 1, 1),
    _AclL3v6ExtRuleProfileNo_Type()
)
aclL3v6ExtRuleProfileNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL3v6ExtRuleProfileNo.setStatus("current")


class _AclL3v6ExtRuleAccessID_Type(Integer32):
    """Custom type aclL3v6ExtRuleAccessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AclL3v6ExtRuleAccessID_Type.__name__ = "Integer32"
_AclL3v6ExtRuleAccessID_Object = MibTableColumn
aclL3v6ExtRuleAccessID = _AclL3v6ExtRuleAccessID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 6, 1, 1, 2),
    _AclL3v6ExtRuleAccessID_Type()
)
aclL3v6ExtRuleAccessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL3v6ExtRuleAccessID.setStatus("current")


class _AclL3v6ExtRuleDscp_Type(Integer32):
    """Custom type aclL3v6ExtRuleDscp based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_AclL3v6ExtRuleDscp_Type.__name__ = "Integer32"
_AclL3v6ExtRuleDscp_Object = MibTableColumn
aclL3v6ExtRuleDscp = _AclL3v6ExtRuleDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 6, 1, 1, 3),
    _AclL3v6ExtRuleDscp_Type()
)
aclL3v6ExtRuleDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v6ExtRuleDscp.setStatus("current")


class _AclL3v6ExtRuleProtocol_Type(Integer32):
    """Custom type aclL3v6ExtRuleProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AclL3v6ExtRuleProtocol_Type.__name__ = "Integer32"
_AclL3v6ExtRuleProtocol_Object = MibTableColumn
aclL3v6ExtRuleProtocol = _AclL3v6ExtRuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 6, 1, 1, 4),
    _AclL3v6ExtRuleProtocol_Type()
)
aclL3v6ExtRuleProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v6ExtRuleProtocol.setStatus("current")


class _AclL3v6ExtRuleFragments_Type(Integer32):
    """Custom type aclL3v6ExtRuleFragments based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("none", 0))
    )


_AclL3v6ExtRuleFragments_Type.__name__ = "Integer32"
_AclL3v6ExtRuleFragments_Object = MibTableColumn
aclL3v6ExtRuleFragments = _AclL3v6ExtRuleFragments_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 6, 1, 1, 5),
    _AclL3v6ExtRuleFragments_Type()
)
aclL3v6ExtRuleFragments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v6ExtRuleFragments.setStatus("current")


class _AclL3v6ExtRuleTcpUdpDstOperator_Type(Integer32):
    """Custom type aclL3v6ExtRuleTcpUdpDstOperator based on Integer32"""
    defaultValue = 1

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
        *(("eq", 2),
          ("gt", 3),
          ("lt", 4),
          ("neq", 5),
          ("none", 1),
          ("range", 6))
    )


_AclL3v6ExtRuleTcpUdpDstOperator_Type.__name__ = "Integer32"
_AclL3v6ExtRuleTcpUdpDstOperator_Object = MibTableColumn
aclL3v6ExtRuleTcpUdpDstOperator = _AclL3v6ExtRuleTcpUdpDstOperator_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 6, 1, 1, 6),
    _AclL3v6ExtRuleTcpUdpDstOperator_Type()
)
aclL3v6ExtRuleTcpUdpDstOperator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v6ExtRuleTcpUdpDstOperator.setStatus("current")


class _AclL3v6ExtRuleTcpUdpDstPort_Type(Integer32):
    """Custom type aclL3v6ExtRuleTcpUdpDstPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclL3v6ExtRuleTcpUdpDstPort_Type.__name__ = "Integer32"
_AclL3v6ExtRuleTcpUdpDstPort_Object = MibTableColumn
aclL3v6ExtRuleTcpUdpDstPort = _AclL3v6ExtRuleTcpUdpDstPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 6, 1, 1, 7),
    _AclL3v6ExtRuleTcpUdpDstPort_Type()
)
aclL3v6ExtRuleTcpUdpDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v6ExtRuleTcpUdpDstPort.setStatus("current")


class _AclL3v6ExtRuleTcpUdpMinDstPort_Type(Unsigned32):
    """Custom type aclL3v6ExtRuleTcpUdpMinDstPort based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclL3v6ExtRuleTcpUdpMinDstPort_Type.__name__ = "Unsigned32"
_AclL3v6ExtRuleTcpUdpMinDstPort_Object = MibTableColumn
aclL3v6ExtRuleTcpUdpMinDstPort = _AclL3v6ExtRuleTcpUdpMinDstPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 6, 1, 1, 8),
    _AclL3v6ExtRuleTcpUdpMinDstPort_Type()
)
aclL3v6ExtRuleTcpUdpMinDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v6ExtRuleTcpUdpMinDstPort.setStatus("current")


class _AclL3v6ExtRuleTcpUdpMaxDstPort_Type(Unsigned32):
    """Custom type aclL3v6ExtRuleTcpUdpMaxDstPort based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclL3v6ExtRuleTcpUdpMaxDstPort_Type.__name__ = "Unsigned32"
_AclL3v6ExtRuleTcpUdpMaxDstPort_Object = MibTableColumn
aclL3v6ExtRuleTcpUdpMaxDstPort = _AclL3v6ExtRuleTcpUdpMaxDstPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 6, 1, 1, 9),
    _AclL3v6ExtRuleTcpUdpMaxDstPort_Type()
)
aclL3v6ExtRuleTcpUdpMaxDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v6ExtRuleTcpUdpMaxDstPort.setStatus("current")


class _AclL3v6ExtRuleTcpUdpSrcOperator_Type(Integer32):
    """Custom type aclL3v6ExtRuleTcpUdpSrcOperator based on Integer32"""
    defaultValue = 1

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
        *(("eq", 2),
          ("gt", 3),
          ("lt", 4),
          ("neq", 5),
          ("none", 1),
          ("range", 6))
    )


_AclL3v6ExtRuleTcpUdpSrcOperator_Type.__name__ = "Integer32"
_AclL3v6ExtRuleTcpUdpSrcOperator_Object = MibTableColumn
aclL3v6ExtRuleTcpUdpSrcOperator = _AclL3v6ExtRuleTcpUdpSrcOperator_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 6, 1, 1, 10),
    _AclL3v6ExtRuleTcpUdpSrcOperator_Type()
)
aclL3v6ExtRuleTcpUdpSrcOperator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v6ExtRuleTcpUdpSrcOperator.setStatus("current")


class _AclL3v6ExtRuleTcpUdpSrcPort_Type(Integer32):
    """Custom type aclL3v6ExtRuleTcpUdpSrcPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclL3v6ExtRuleTcpUdpSrcPort_Type.__name__ = "Integer32"
_AclL3v6ExtRuleTcpUdpSrcPort_Object = MibTableColumn
aclL3v6ExtRuleTcpUdpSrcPort = _AclL3v6ExtRuleTcpUdpSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 6, 1, 1, 11),
    _AclL3v6ExtRuleTcpUdpSrcPort_Type()
)
aclL3v6ExtRuleTcpUdpSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v6ExtRuleTcpUdpSrcPort.setStatus("current")


class _AclL3v6ExtRuleTcpUdpMinSrcPort_Type(Unsigned32):
    """Custom type aclL3v6ExtRuleTcpUdpMinSrcPort based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclL3v6ExtRuleTcpUdpMinSrcPort_Type.__name__ = "Unsigned32"
_AclL3v6ExtRuleTcpUdpMinSrcPort_Object = MibTableColumn
aclL3v6ExtRuleTcpUdpMinSrcPort = _AclL3v6ExtRuleTcpUdpMinSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 6, 1, 1, 12),
    _AclL3v6ExtRuleTcpUdpMinSrcPort_Type()
)
aclL3v6ExtRuleTcpUdpMinSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v6ExtRuleTcpUdpMinSrcPort.setStatus("current")


class _AclL3v6ExtRuleTcpUdpMaxSrcPort_Type(Unsigned32):
    """Custom type aclL3v6ExtRuleTcpUdpMaxSrcPort based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclL3v6ExtRuleTcpUdpMaxSrcPort_Type.__name__ = "Unsigned32"
_AclL3v6ExtRuleTcpUdpMaxSrcPort_Object = MibTableColumn
aclL3v6ExtRuleTcpUdpMaxSrcPort = _AclL3v6ExtRuleTcpUdpMaxSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 6, 1, 1, 13),
    _AclL3v6ExtRuleTcpUdpMaxSrcPort_Type()
)
aclL3v6ExtRuleTcpUdpMaxSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v6ExtRuleTcpUdpMaxSrcPort.setStatus("current")


class _AclL3v6ExtRuleICMPv6MessageType_Type(Integer32):
    """Custom type aclL3v6ExtRuleICMPv6MessageType based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_AclL3v6ExtRuleICMPv6MessageType_Type.__name__ = "Integer32"
_AclL3v6ExtRuleICMPv6MessageType_Object = MibTableColumn
aclL3v6ExtRuleICMPv6MessageType = _AclL3v6ExtRuleICMPv6MessageType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 6, 1, 1, 14),
    _AclL3v6ExtRuleICMPv6MessageType_Type()
)
aclL3v6ExtRuleICMPv6MessageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v6ExtRuleICMPv6MessageType.setStatus("current")


class _AclL3v6ExtRuleICMPv6MessageCode_Type(Integer32):
    """Custom type aclL3v6ExtRuleICMPv6MessageCode based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_AclL3v6ExtRuleICMPv6MessageCode_Type.__name__ = "Integer32"
_AclL3v6ExtRuleICMPv6MessageCode_Object = MibTableColumn
aclL3v6ExtRuleICMPv6MessageCode = _AclL3v6ExtRuleICMPv6MessageCode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 6, 1, 1, 15),
    _AclL3v6ExtRuleICMPv6MessageCode_Type()
)
aclL3v6ExtRuleICMPv6MessageCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v6ExtRuleICMPv6MessageCode.setStatus("current")
_AclL3v6ExtRuleDstIpv6Addr_Type = Ipv6Address
_AclL3v6ExtRuleDstIpv6Addr_Object = MibTableColumn
aclL3v6ExtRuleDstIpv6Addr = _AclL3v6ExtRuleDstIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 6, 1, 1, 16),
    _AclL3v6ExtRuleDstIpv6Addr_Type()
)
aclL3v6ExtRuleDstIpv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v6ExtRuleDstIpv6Addr.setStatus("current")
_AclL3v6ExtRuleSrcIpv6Addr_Type = Ipv6Address
_AclL3v6ExtRuleSrcIpv6Addr_Object = MibTableColumn
aclL3v6ExtRuleSrcIpv6Addr = _AclL3v6ExtRuleSrcIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 6, 1, 1, 17),
    _AclL3v6ExtRuleSrcIpv6Addr_Type()
)
aclL3v6ExtRuleSrcIpv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v6ExtRuleSrcIpv6Addr.setStatus("current")


class _AclL3v6ExtRuleDstIpv6AddrPrefixLen_Type(InetAddressPrefixLength):
    """Custom type aclL3v6ExtRuleDstIpv6AddrPrefixLen based on InetAddressPrefixLength"""
    defaultValue = 0


_AclL3v6ExtRuleDstIpv6AddrPrefixLen_Object = MibTableColumn
aclL3v6ExtRuleDstIpv6AddrPrefixLen = _AclL3v6ExtRuleDstIpv6AddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 6, 1, 1, 18),
    _AclL3v6ExtRuleDstIpv6AddrPrefixLen_Type()
)
aclL3v6ExtRuleDstIpv6AddrPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v6ExtRuleDstIpv6AddrPrefixLen.setStatus("current")


class _AclL3v6ExtRuleSrcIpv6AddrPrefixLen_Type(InetAddressPrefixLength):
    """Custom type aclL3v6ExtRuleSrcIpv6AddrPrefixLen based on InetAddressPrefixLength"""
    defaultValue = 0


_AclL3v6ExtRuleSrcIpv6AddrPrefixLen_Object = MibTableColumn
aclL3v6ExtRuleSrcIpv6AddrPrefixLen = _AclL3v6ExtRuleSrcIpv6AddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 6, 1, 1, 19),
    _AclL3v6ExtRuleSrcIpv6AddrPrefixLen_Type()
)
aclL3v6ExtRuleSrcIpv6AddrPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v6ExtRuleSrcIpv6AddrPrefixLen.setStatus("current")


class _AclL3v6ExtRuleTcpAckBit_Type(Integer32):
    """Custom type aclL3v6ExtRuleTcpAckBit based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dont_care", 3),
          ("establish", 1),
          ("notEstablish", 2))
    )


_AclL3v6ExtRuleTcpAckBit_Type.__name__ = "Integer32"
_AclL3v6ExtRuleTcpAckBit_Object = MibTableColumn
aclL3v6ExtRuleTcpAckBit = _AclL3v6ExtRuleTcpAckBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 6, 1, 1, 20),
    _AclL3v6ExtRuleTcpAckBit_Type()
)
aclL3v6ExtRuleTcpAckBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclL3v6ExtRuleTcpAckBit.setStatus("current")


class _AclL3v6ExtRuleTcpRstBit_Type(Integer32):
    """Custom type aclL3v6ExtRuleTcpRstBit based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dont_care", 3),
          ("establish", 1),
          ("notEstablish", 2))
    )


_AclL3v6ExtRuleTcpRstBit_Type.__name__ = "Integer32"
_AclL3v6ExtRuleTcpRstBit_Object = MibTableColumn
aclL3v6ExtRuleTcpRstBit = _AclL3v6ExtRuleTcpRstBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 6, 1, 1, 21),
    _AclL3v6ExtRuleTcpRstBit_Type()
)
aclL3v6ExtRuleTcpRstBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclL3v6ExtRuleTcpRstBit.setStatus("current")


class _AclL3v6ExtRuleTcpUrgBit_Type(Integer32):
    """Custom type aclL3v6ExtRuleTcpUrgBit based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dont_care", 3),
          ("establish", 1),
          ("notEstablish", 2))
    )


_AclL3v6ExtRuleTcpUrgBit_Type.__name__ = "Integer32"
_AclL3v6ExtRuleTcpUrgBit_Object = MibTableColumn
aclL3v6ExtRuleTcpUrgBit = _AclL3v6ExtRuleTcpUrgBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 6, 1, 1, 22),
    _AclL3v6ExtRuleTcpUrgBit_Type()
)
aclL3v6ExtRuleTcpUrgBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclL3v6ExtRuleTcpUrgBit.setStatus("current")


class _AclL3v6ExtRuleTcpPshBit_Type(Integer32):
    """Custom type aclL3v6ExtRuleTcpPshBit based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dont_care", 3),
          ("establish", 1),
          ("notEstablish", 2))
    )


_AclL3v6ExtRuleTcpPshBit_Type.__name__ = "Integer32"
_AclL3v6ExtRuleTcpPshBit_Object = MibTableColumn
aclL3v6ExtRuleTcpPshBit = _AclL3v6ExtRuleTcpPshBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 6, 1, 1, 23),
    _AclL3v6ExtRuleTcpPshBit_Type()
)
aclL3v6ExtRuleTcpPshBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclL3v6ExtRuleTcpPshBit.setStatus("current")


class _AclL3v6ExtRuleTcpSynBit_Type(Integer32):
    """Custom type aclL3v6ExtRuleTcpSynBit based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dont_care", 3),
          ("establish", 1),
          ("notEstablish", 2))
    )


_AclL3v6ExtRuleTcpSynBit_Type.__name__ = "Integer32"
_AclL3v6ExtRuleTcpSynBit_Object = MibTableColumn
aclL3v6ExtRuleTcpSynBit = _AclL3v6ExtRuleTcpSynBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 6, 1, 1, 24),
    _AclL3v6ExtRuleTcpSynBit_Type()
)
aclL3v6ExtRuleTcpSynBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclL3v6ExtRuleTcpSynBit.setStatus("current")


class _AclL3v6ExtRuleTcpFinBit_Type(Integer32):
    """Custom type aclL3v6ExtRuleTcpFinBit based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dont_care", 3),
          ("establish", 1),
          ("notEstablish", 2))
    )


_AclL3v6ExtRuleTcpFinBit_Type.__name__ = "Integer32"
_AclL3v6ExtRuleTcpFinBit_Object = MibTableColumn
aclL3v6ExtRuleTcpFinBit = _AclL3v6ExtRuleTcpFinBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 6, 1, 1, 25),
    _AclL3v6ExtRuleTcpFinBit_Type()
)
aclL3v6ExtRuleTcpFinBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclL3v6ExtRuleTcpFinBit.setStatus("current")


class _AclL3v6ExtRuleFlowLabel_Type(Integer32):
    """Custom type aclL3v6ExtRuleFlowLabel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1048575),
    )


_AclL3v6ExtRuleFlowLabel_Type.__name__ = "Integer32"
_AclL3v6ExtRuleFlowLabel_Object = MibTableColumn
aclL3v6ExtRuleFlowLabel = _AclL3v6ExtRuleFlowLabel_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 6, 1, 1, 26),
    _AclL3v6ExtRuleFlowLabel_Type()
)
aclL3v6ExtRuleFlowLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v6ExtRuleFlowLabel.setStatus("current")


class _AclL3v6ExtRuleAction_Type(Integer32):
    """Custom type aclL3v6ExtRuleAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("drop", 2))
    )


_AclL3v6ExtRuleAction_Type.__name__ = "Integer32"
_AclL3v6ExtRuleAction_Object = MibTableColumn
aclL3v6ExtRuleAction = _AclL3v6ExtRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 6, 1, 1, 27),
    _AclL3v6ExtRuleAction_Type()
)
aclL3v6ExtRuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v6ExtRuleAction.setStatus("current")


class _AclL3v6ExtRuleTimeRange_Type(SnmpAdminString):
    """Custom type aclL3v6ExtRuleTimeRange based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AclL3v6ExtRuleTimeRange_Type.__name__ = "SnmpAdminString"
_AclL3v6ExtRuleTimeRange_Object = MibTableColumn
aclL3v6ExtRuleTimeRange = _AclL3v6ExtRuleTimeRange_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 6, 1, 1, 28),
    _AclL3v6ExtRuleTimeRange_Type()
)
aclL3v6ExtRuleTimeRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v6ExtRuleTimeRange.setStatus("current")
_AclL3v6ExtRuleMatchCount_Type = Counter32
_AclL3v6ExtRuleMatchCount_Object = MibTableColumn
aclL3v6ExtRuleMatchCount = _AclL3v6ExtRuleMatchCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 6, 1, 1, 29),
    _AclL3v6ExtRuleMatchCount_Type()
)
aclL3v6ExtRuleMatchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL3v6ExtRuleMatchCount.setStatus("current")
_AclL3v6ExtRuleStatus_Type = RowStatus
_AclL3v6ExtRuleStatus_Object = MibTableColumn
aclL3v6ExtRuleStatus = _AclL3v6ExtRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 6, 1, 1, 30),
    _AclL3v6ExtRuleStatus_Type()
)
aclL3v6ExtRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v6ExtRuleStatus.setStatus("current")
_AclExpertExtRule_ObjectIdentity = ObjectIdentity
aclExpertExtRule = _AclExpertExtRule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 7)
)
_AclExpertExtRuleTable_Object = MibTable
aclExpertExtRuleTable = _AclExpertExtRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 7, 1)
)
if mibBuilder.loadTexts:
    aclExpertExtRuleTable.setStatus("current")
_AclExpertExtRuleEntry_Object = MibTableRow
aclExpertExtRuleEntry = _AclExpertExtRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 7, 1, 1)
)
aclExpertExtRuleEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "aclExpertExtRuleProfileNo"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "aclExpertExtRuleAccessID"),
)
if mibBuilder.loadTexts:
    aclExpertExtRuleEntry.setStatus("current")


class _AclExpertExtRuleProfileNo_Type(Integer32):
    """Custom type aclExpertExtRuleProfileNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_AclExpertExtRuleProfileNo_Type.__name__ = "Integer32"
_AclExpertExtRuleProfileNo_Object = MibTableColumn
aclExpertExtRuleProfileNo = _AclExpertExtRuleProfileNo_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 7, 1, 1, 1),
    _AclExpertExtRuleProfileNo_Type()
)
aclExpertExtRuleProfileNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclExpertExtRuleProfileNo.setStatus("current")


class _AclExpertExtRuleAccessID_Type(Integer32):
    """Custom type aclExpertExtRuleAccessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AclExpertExtRuleAccessID_Type.__name__ = "Integer32"
_AclExpertExtRuleAccessID_Object = MibTableColumn
aclExpertExtRuleAccessID = _AclExpertExtRuleAccessID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 7, 1, 1, 2),
    _AclExpertExtRuleAccessID_Type()
)
aclExpertExtRuleAccessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclExpertExtRuleAccessID.setStatus("current")


class _AclExpertExtRuleProtocol_Type(Integer32):
    """Custom type aclExpertExtRuleProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              6,
              17,
              47,
              50,
              88,
              89,
              94,
              103,
              108,
              112)
        )
    )
    namedValues = NamedValues(
        *(("eigrp", 88),
          ("esp", 50),
          ("gre", 47),
          ("icmp", 1),
          ("igmp", 2),
          ("ipinip", 94),
          ("none", 0),
          ("ospf", 89),
          ("pcp", 108),
          ("pim", 103),
          ("tcp", 6),
          ("udp", 17),
          ("vrrp", 112))
    )


_AclExpertExtRuleProtocol_Type.__name__ = "Integer32"
_AclExpertExtRuleProtocol_Object = MibTableColumn
aclExpertExtRuleProtocol = _AclExpertExtRuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 7, 1, 1, 3),
    _AclExpertExtRuleProtocol_Type()
)
aclExpertExtRuleProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExpertExtRuleProtocol.setStatus("current")


class _AclExpertExtRuleFragments_Type(Integer32):
    """Custom type aclExpertExtRuleFragments based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("none", 0))
    )


_AclExpertExtRuleFragments_Type.__name__ = "Integer32"
_AclExpertExtRuleFragments_Object = MibTableColumn
aclExpertExtRuleFragments = _AclExpertExtRuleFragments_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 7, 1, 1, 4),
    _AclExpertExtRuleFragments_Type()
)
aclExpertExtRuleFragments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExpertExtRuleFragments.setStatus("current")


class _AclExpertExtRuleICMPMessageType_Type(Integer32):
    """Custom type aclExpertExtRuleICMPMessageType based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_AclExpertExtRuleICMPMessageType_Type.__name__ = "Integer32"
_AclExpertExtRuleICMPMessageType_Object = MibTableColumn
aclExpertExtRuleICMPMessageType = _AclExpertExtRuleICMPMessageType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 7, 1, 1, 5),
    _AclExpertExtRuleICMPMessageType_Type()
)
aclExpertExtRuleICMPMessageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExpertExtRuleICMPMessageType.setStatus("current")


class _AclExpertExtRuleICMPMessageCode_Type(Integer32):
    """Custom type aclExpertExtRuleICMPMessageCode based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_AclExpertExtRuleICMPMessageCode_Type.__name__ = "Integer32"
_AclExpertExtRuleICMPMessageCode_Object = MibTableColumn
aclExpertExtRuleICMPMessageCode = _AclExpertExtRuleICMPMessageCode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 7, 1, 1, 6),
    _AclExpertExtRuleICMPMessageCode_Type()
)
aclExpertExtRuleICMPMessageCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExpertExtRuleICMPMessageCode.setStatus("current")


class _AclExpertExtRuleDstIpAddr_Type(IpAddress):
    """Custom type aclExpertExtRuleDstIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_AclExpertExtRuleDstIpAddr_Object = MibTableColumn
aclExpertExtRuleDstIpAddr = _AclExpertExtRuleDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 7, 1, 1, 7),
    _AclExpertExtRuleDstIpAddr_Type()
)
aclExpertExtRuleDstIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExpertExtRuleDstIpAddr.setStatus("current")


class _AclExpertExtRuleSrcIpAddr_Type(IpAddress):
    """Custom type aclExpertExtRuleSrcIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_AclExpertExtRuleSrcIpAddr_Object = MibTableColumn
aclExpertExtRuleSrcIpAddr = _AclExpertExtRuleSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 7, 1, 1, 8),
    _AclExpertExtRuleSrcIpAddr_Type()
)
aclExpertExtRuleSrcIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExpertExtRuleSrcIpAddr.setStatus("current")


class _AclExpertExtRuleDstIpAddrMask_Type(IpAddress):
    """Custom type aclExpertExtRuleDstIpAddrMask based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_AclExpertExtRuleDstIpAddrMask_Object = MibTableColumn
aclExpertExtRuleDstIpAddrMask = _AclExpertExtRuleDstIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 7, 1, 1, 9),
    _AclExpertExtRuleDstIpAddrMask_Type()
)
aclExpertExtRuleDstIpAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExpertExtRuleDstIpAddrMask.setStatus("current")


class _AclExpertExtRuleSrcIpAddrMask_Type(IpAddress):
    """Custom type aclExpertExtRuleSrcIpAddrMask based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_AclExpertExtRuleSrcIpAddrMask_Object = MibTableColumn
aclExpertExtRuleSrcIpAddrMask = _AclExpertExtRuleSrcIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 7, 1, 1, 10),
    _AclExpertExtRuleSrcIpAddrMask_Type()
)
aclExpertExtRuleSrcIpAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExpertExtRuleSrcIpAddrMask.setStatus("current")


class _AclExpertExtRuleTcpUdpDstOperator_Type(Integer32):
    """Custom type aclExpertExtRuleTcpUdpDstOperator based on Integer32"""
    defaultValue = 1

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
        *(("eq", 2),
          ("gt", 3),
          ("lt", 4),
          ("neq", 5),
          ("none", 1),
          ("range", 6))
    )


_AclExpertExtRuleTcpUdpDstOperator_Type.__name__ = "Integer32"
_AclExpertExtRuleTcpUdpDstOperator_Object = MibTableColumn
aclExpertExtRuleTcpUdpDstOperator = _AclExpertExtRuleTcpUdpDstOperator_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 7, 1, 1, 11),
    _AclExpertExtRuleTcpUdpDstOperator_Type()
)
aclExpertExtRuleTcpUdpDstOperator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExpertExtRuleTcpUdpDstOperator.setStatus("current")


class _AclExpertExtRuleTcpUdpDstPort_Type(Integer32):
    """Custom type aclExpertExtRuleTcpUdpDstPort based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_AclExpertExtRuleTcpUdpDstPort_Type.__name__ = "Integer32"
_AclExpertExtRuleTcpUdpDstPort_Object = MibTableColumn
aclExpertExtRuleTcpUdpDstPort = _AclExpertExtRuleTcpUdpDstPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 7, 1, 1, 12),
    _AclExpertExtRuleTcpUdpDstPort_Type()
)
aclExpertExtRuleTcpUdpDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExpertExtRuleTcpUdpDstPort.setStatus("current")


class _AclExpertExtRuleTcpUdpMinDstPort_Type(Integer32):
    """Custom type aclExpertExtRuleTcpUdpMinDstPort based on Integer32"""
    defaultValue = 0


_AclExpertExtRuleTcpUdpMinDstPort_Object = MibTableColumn
aclExpertExtRuleTcpUdpMinDstPort = _AclExpertExtRuleTcpUdpMinDstPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 7, 1, 1, 13),
    _AclExpertExtRuleTcpUdpMinDstPort_Type()
)
aclExpertExtRuleTcpUdpMinDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExpertExtRuleTcpUdpMinDstPort.setStatus("current")


class _AclExpertExtRuleTcpUdpMaxDstPort_Type(Integer32):
    """Custom type aclExpertExtRuleTcpUdpMaxDstPort based on Integer32"""
    defaultValue = 0


_AclExpertExtRuleTcpUdpMaxDstPort_Object = MibTableColumn
aclExpertExtRuleTcpUdpMaxDstPort = _AclExpertExtRuleTcpUdpMaxDstPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 7, 1, 1, 14),
    _AclExpertExtRuleTcpUdpMaxDstPort_Type()
)
aclExpertExtRuleTcpUdpMaxDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExpertExtRuleTcpUdpMaxDstPort.setStatus("current")


class _AclExpertExtRuleTcpUdpSrcOperator_Type(Integer32):
    """Custom type aclExpertExtRuleTcpUdpSrcOperator based on Integer32"""
    defaultValue = 1

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
        *(("eq", 2),
          ("gt", 3),
          ("lt", 4),
          ("neq", 5),
          ("none", 1),
          ("range", 6))
    )


_AclExpertExtRuleTcpUdpSrcOperator_Type.__name__ = "Integer32"
_AclExpertExtRuleTcpUdpSrcOperator_Object = MibTableColumn
aclExpertExtRuleTcpUdpSrcOperator = _AclExpertExtRuleTcpUdpSrcOperator_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 7, 1, 1, 15),
    _AclExpertExtRuleTcpUdpSrcOperator_Type()
)
aclExpertExtRuleTcpUdpSrcOperator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExpertExtRuleTcpUdpSrcOperator.setStatus("current")


class _AclExpertExtRuleTcpUdpSrcPort_Type(Integer32):
    """Custom type aclExpertExtRuleTcpUdpSrcPort based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_AclExpertExtRuleTcpUdpSrcPort_Type.__name__ = "Integer32"
_AclExpertExtRuleTcpUdpSrcPort_Object = MibTableColumn
aclExpertExtRuleTcpUdpSrcPort = _AclExpertExtRuleTcpUdpSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 7, 1, 1, 16),
    _AclExpertExtRuleTcpUdpSrcPort_Type()
)
aclExpertExtRuleTcpUdpSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExpertExtRuleTcpUdpSrcPort.setStatus("current")


class _AclExpertExtRuleTcpUdpMinSrcPort_Type(Integer32):
    """Custom type aclExpertExtRuleTcpUdpMinSrcPort based on Integer32"""
    defaultValue = 0


_AclExpertExtRuleTcpUdpMinSrcPort_Object = MibTableColumn
aclExpertExtRuleTcpUdpMinSrcPort = _AclExpertExtRuleTcpUdpMinSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 7, 1, 1, 17),
    _AclExpertExtRuleTcpUdpMinSrcPort_Type()
)
aclExpertExtRuleTcpUdpMinSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExpertExtRuleTcpUdpMinSrcPort.setStatus("current")


class _AclExpertExtRuleTcpUdpMaxSrcPort_Type(Integer32):
    """Custom type aclExpertExtRuleTcpUdpMaxSrcPort based on Integer32"""
    defaultValue = 0


_AclExpertExtRuleTcpUdpMaxSrcPort_Object = MibTableColumn
aclExpertExtRuleTcpUdpMaxSrcPort = _AclExpertExtRuleTcpUdpMaxSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 7, 1, 1, 18),
    _AclExpertExtRuleTcpUdpMaxSrcPort_Type()
)
aclExpertExtRuleTcpUdpMaxSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExpertExtRuleTcpUdpMaxSrcPort.setStatus("current")


class _AclExpertExtRuleIPPrecedence_Type(Integer32):
    """Custom type aclExpertExtRuleIPPrecedence based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_AclExpertExtRuleIPPrecedence_Type.__name__ = "Integer32"
_AclExpertExtRuleIPPrecedence_Object = MibTableColumn
aclExpertExtRuleIPPrecedence = _AclExpertExtRuleIPPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 7, 1, 1, 19),
    _AclExpertExtRuleIPPrecedence_Type()
)
aclExpertExtRuleIPPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclExpertExtRuleIPPrecedence.setStatus("current")


class _AclExpertExtRuleDscp_Type(Integer32):
    """Custom type aclExpertExtRuleDscp based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_AclExpertExtRuleDscp_Type.__name__ = "Integer32"
_AclExpertExtRuleDscp_Object = MibTableColumn
aclExpertExtRuleDscp = _AclExpertExtRuleDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 7, 1, 1, 20),
    _AclExpertExtRuleDscp_Type()
)
aclExpertExtRuleDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclExpertExtRuleDscp.setStatus("current")


class _AclExpertExtRuleToS_Type(Integer32):
    """Custom type aclExpertExtRuleToS based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 15),
    )


_AclExpertExtRuleToS_Type.__name__ = "Integer32"
_AclExpertExtRuleToS_Object = MibTableColumn
aclExpertExtRuleToS = _AclExpertExtRuleToS_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 7, 1, 1, 21),
    _AclExpertExtRuleToS_Type()
)
aclExpertExtRuleToS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExpertExtRuleToS.setStatus("current")


class _AclExpertExtRuleTcpAckBit_Type(Integer32):
    """Custom type aclExpertExtRuleTcpAckBit based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dont_care", 3),
          ("establish", 1),
          ("notEstablish", 2))
    )


_AclExpertExtRuleTcpAckBit_Type.__name__ = "Integer32"
_AclExpertExtRuleTcpAckBit_Object = MibTableColumn
aclExpertExtRuleTcpAckBit = _AclExpertExtRuleTcpAckBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 7, 1, 1, 22),
    _AclExpertExtRuleTcpAckBit_Type()
)
aclExpertExtRuleTcpAckBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclExpertExtRuleTcpAckBit.setStatus("current")


class _AclExpertExtRuleTcpRstBit_Type(Integer32):
    """Custom type aclExpertExtRuleTcpRstBit based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dont_care", 3),
          ("establish", 1),
          ("notEstablish", 2))
    )


_AclExpertExtRuleTcpRstBit_Type.__name__ = "Integer32"
_AclExpertExtRuleTcpRstBit_Object = MibTableColumn
aclExpertExtRuleTcpRstBit = _AclExpertExtRuleTcpRstBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 7, 1, 1, 23),
    _AclExpertExtRuleTcpRstBit_Type()
)
aclExpertExtRuleTcpRstBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclExpertExtRuleTcpRstBit.setStatus("current")


class _AclExpertExtRuleTcpUrgBit_Type(Integer32):
    """Custom type aclExpertExtRuleTcpUrgBit based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dont_care", 3),
          ("establish", 1),
          ("notEstablish", 2))
    )


_AclExpertExtRuleTcpUrgBit_Type.__name__ = "Integer32"
_AclExpertExtRuleTcpUrgBit_Object = MibTableColumn
aclExpertExtRuleTcpUrgBit = _AclExpertExtRuleTcpUrgBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 7, 1, 1, 24),
    _AclExpertExtRuleTcpUrgBit_Type()
)
aclExpertExtRuleTcpUrgBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclExpertExtRuleTcpUrgBit.setStatus("current")


class _AclExpertExtRuleTcpPshBit_Type(Integer32):
    """Custom type aclExpertExtRuleTcpPshBit based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dont_care", 3),
          ("establish", 1),
          ("notEstablish", 2))
    )


_AclExpertExtRuleTcpPshBit_Type.__name__ = "Integer32"
_AclExpertExtRuleTcpPshBit_Object = MibTableColumn
aclExpertExtRuleTcpPshBit = _AclExpertExtRuleTcpPshBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 7, 1, 1, 25),
    _AclExpertExtRuleTcpPshBit_Type()
)
aclExpertExtRuleTcpPshBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclExpertExtRuleTcpPshBit.setStatus("current")


class _AclExpertExtRuleTcpSynBit_Type(Integer32):
    """Custom type aclExpertExtRuleTcpSynBit based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dont_care", 3),
          ("establish", 1),
          ("notEstablish", 2))
    )


_AclExpertExtRuleTcpSynBit_Type.__name__ = "Integer32"
_AclExpertExtRuleTcpSynBit_Object = MibTableColumn
aclExpertExtRuleTcpSynBit = _AclExpertExtRuleTcpSynBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 7, 1, 1, 26),
    _AclExpertExtRuleTcpSynBit_Type()
)
aclExpertExtRuleTcpSynBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclExpertExtRuleTcpSynBit.setStatus("current")


class _AclExpertExtRuleTcpFinBit_Type(Integer32):
    """Custom type aclExpertExtRuleTcpFinBit based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dont_care", 3),
          ("establish", 1),
          ("notEstablish", 2))
    )


_AclExpertExtRuleTcpFinBit_Type.__name__ = "Integer32"
_AclExpertExtRuleTcpFinBit_Object = MibTableColumn
aclExpertExtRuleTcpFinBit = _AclExpertExtRuleTcpFinBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 7, 1, 1, 27),
    _AclExpertExtRuleTcpFinBit_Type()
)
aclExpertExtRuleTcpFinBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclExpertExtRuleTcpFinBit.setStatus("current")
_AclExpertExtRuleDstMacAddr_Type = MacAddress
_AclExpertExtRuleDstMacAddr_Object = MibTableColumn
aclExpertExtRuleDstMacAddr = _AclExpertExtRuleDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 7, 1, 1, 28),
    _AclExpertExtRuleDstMacAddr_Type()
)
aclExpertExtRuleDstMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExpertExtRuleDstMacAddr.setStatus("current")
_AclExpertExtRuleSrcMacAddr_Type = MacAddress
_AclExpertExtRuleSrcMacAddr_Object = MibTableColumn
aclExpertExtRuleSrcMacAddr = _AclExpertExtRuleSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 7, 1, 1, 29),
    _AclExpertExtRuleSrcMacAddr_Type()
)
aclExpertExtRuleSrcMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExpertExtRuleSrcMacAddr.setStatus("current")


class _AclExpertExtRuleVlanId_Type(Integer32):
    """Custom type aclExpertExtRuleVlanId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4094),
    )


_AclExpertExtRuleVlanId_Type.__name__ = "Integer32"
_AclExpertExtRuleVlanId_Object = MibTableColumn
aclExpertExtRuleVlanId = _AclExpertExtRuleVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 7, 1, 1, 30),
    _AclExpertExtRuleVlanId_Type()
)
aclExpertExtRuleVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExpertExtRuleVlanId.setStatus("current")


class _AclExpertExtRule1pPriority_Type(Integer32):
    """Custom type aclExpertExtRule1pPriority based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_AclExpertExtRule1pPriority_Type.__name__ = "Integer32"
_AclExpertExtRule1pPriority_Object = MibTableColumn
aclExpertExtRule1pPriority = _AclExpertExtRule1pPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 7, 1, 1, 31),
    _AclExpertExtRule1pPriority_Type()
)
aclExpertExtRule1pPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExpertExtRule1pPriority.setStatus("current")
_AclExpertExtRuleDstMacAddrMask_Type = MacAddress
_AclExpertExtRuleDstMacAddrMask_Object = MibTableColumn
aclExpertExtRuleDstMacAddrMask = _AclExpertExtRuleDstMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 7, 1, 1, 32),
    _AclExpertExtRuleDstMacAddrMask_Type()
)
aclExpertExtRuleDstMacAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExpertExtRuleDstMacAddrMask.setStatus("current")
_AclExpertExtRuleSrcMacAddrMask_Type = MacAddress
_AclExpertExtRuleSrcMacAddrMask_Object = MibTableColumn
aclExpertExtRuleSrcMacAddrMask = _AclExpertExtRuleSrcMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 7, 1, 1, 33),
    _AclExpertExtRuleSrcMacAddrMask_Type()
)
aclExpertExtRuleSrcMacAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExpertExtRuleSrcMacAddrMask.setStatus("current")


class _AclExpertExtRuleAction_Type(Integer32):
    """Custom type aclExpertExtRuleAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("drop", 2))
    )


_AclExpertExtRuleAction_Type.__name__ = "Integer32"
_AclExpertExtRuleAction_Object = MibTableColumn
aclExpertExtRuleAction = _AclExpertExtRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 7, 1, 1, 34),
    _AclExpertExtRuleAction_Type()
)
aclExpertExtRuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExpertExtRuleAction.setStatus("current")


class _AclExpertExtRuleTimeRange_Type(SnmpAdminString):
    """Custom type aclExpertExtRuleTimeRange based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AclExpertExtRuleTimeRange_Type.__name__ = "SnmpAdminString"
_AclExpertExtRuleTimeRange_Object = MibTableColumn
aclExpertExtRuleTimeRange = _AclExpertExtRuleTimeRange_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 7, 1, 1, 35),
    _AclExpertExtRuleTimeRange_Type()
)
aclExpertExtRuleTimeRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExpertExtRuleTimeRange.setStatus("current")
_AclExpertExtRuleMatchCount_Type = Counter32
_AclExpertExtRuleMatchCount_Object = MibTableColumn
aclExpertExtRuleMatchCount = _AclExpertExtRuleMatchCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 7, 1, 1, 36),
    _AclExpertExtRuleMatchCount_Type()
)
aclExpertExtRuleMatchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclExpertExtRuleMatchCount.setStatus("current")
_AclExpertExtRuleStatus_Type = RowStatus
_AclExpertExtRuleStatus_Object = MibTableColumn
aclExpertExtRuleStatus = _AclExpertExtRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 7, 1, 1, 37),
    _AclExpertExtRuleStatus_Type()
)
aclExpertExtRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExpertExtRuleStatus.setStatus("current")
_AclPortBindGroup_ObjectIdentity = ObjectIdentity
aclPortBindGroup = _AclPortBindGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 8)
)
_AclPortGroupTable_Object = MibTable
aclPortGroupTable = _AclPortGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 8, 1)
)
if mibBuilder.loadTexts:
    aclPortGroupTable.setStatus("current")
_AclPortGroupEntry_Object = MibTableRow
aclPortGroupEntry = _AclPortGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 8, 1, 1)
)
aclPortGroupEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "aclPortIndex"),
)
if mibBuilder.loadTexts:
    aclPortGroupEntry.setStatus("current")
_AclPortIndex_Type = Integer32
_AclPortIndex_Object = MibTableColumn
aclPortIndex = _AclPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 8, 1, 1, 1),
    _AclPortIndex_Type()
)
aclPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclPortIndex.setStatus("current")


class _AclPortDirection_Type(Integer32):
    """Custom type aclPortDirection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("in", 1)
    )


_AclPortDirection_Type.__name__ = "Integer32"
_AclPortDirection_Object = MibTableColumn
aclPortDirection = _AclPortDirection_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 8, 1, 1, 2),
    _AclPortDirection_Type()
)
aclPortDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclPortDirection.setStatus("current")


class _AclPortL2ProfileNo_Type(Integer32):
    """Custom type aclPortL2ProfileNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_AclPortL2ProfileNo_Type.__name__ = "Integer32"
_AclPortL2ProfileNo_Object = MibTableColumn
aclPortL2ProfileNo = _AclPortL2ProfileNo_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 8, 1, 1, 3),
    _AclPortL2ProfileNo_Type()
)
aclPortL2ProfileNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclPortL2ProfileNo.setStatus("current")


class _AclPortL3v4StdProfileNo_Type(Integer32):
    """Custom type aclPortL3v4StdProfileNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_AclPortL3v4StdProfileNo_Type.__name__ = "Integer32"
_AclPortL3v4StdProfileNo_Object = MibTableColumn
aclPortL3v4StdProfileNo = _AclPortL3v4StdProfileNo_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 8, 1, 1, 4),
    _AclPortL3v4StdProfileNo_Type()
)
aclPortL3v4StdProfileNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclPortL3v4StdProfileNo.setStatus("current")


class _AclPortL3v4ExtProfileNo_Type(Integer32):
    """Custom type aclPortL3v4ExtProfileNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_AclPortL3v4ExtProfileNo_Type.__name__ = "Integer32"
_AclPortL3v4ExtProfileNo_Object = MibTableColumn
aclPortL3v4ExtProfileNo = _AclPortL3v4ExtProfileNo_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 8, 1, 1, 5),
    _AclPortL3v4ExtProfileNo_Type()
)
aclPortL3v4ExtProfileNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclPortL3v4ExtProfileNo.setStatus("current")


class _AclPortL3v6StdProfileNo_Type(Integer32):
    """Custom type aclPortL3v6StdProfileNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_AclPortL3v6StdProfileNo_Type.__name__ = "Integer32"
_AclPortL3v6StdProfileNo_Object = MibTableColumn
aclPortL3v6StdProfileNo = _AclPortL3v6StdProfileNo_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 8, 1, 1, 6),
    _AclPortL3v6StdProfileNo_Type()
)
aclPortL3v6StdProfileNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclPortL3v6StdProfileNo.setStatus("current")


class _AclPortL3v6ExtProfileNo_Type(Integer32):
    """Custom type aclPortL3v6ExtProfileNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_AclPortL3v6ExtProfileNo_Type.__name__ = "Integer32"
_AclPortL3v6ExtProfileNo_Object = MibTableColumn
aclPortL3v6ExtProfileNo = _AclPortL3v6ExtProfileNo_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 8, 1, 1, 7),
    _AclPortL3v6ExtProfileNo_Type()
)
aclPortL3v6ExtProfileNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclPortL3v6ExtProfileNo.setStatus("current")


class _AclPortExpertProfileNo_Type(Integer32):
    """Custom type aclPortExpertProfileNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_AclPortExpertProfileNo_Type.__name__ = "Integer32"
_AclPortExpertProfileNo_Object = MibTableColumn
aclPortExpertProfileNo = _AclPortExpertProfileNo_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 7, 1, 8, 1, 1, 8),
    _AclPortExpertProfileNo_Type()
)
aclPortExpertProfileNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclPortExpertProfileNo.setStatus("current")
_DlinkSecurity_ObjectIdentity = ObjectIdentity
dlinkSecurity = _DlinkSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8)
)
_SecurityportSecurityGroup_ObjectIdentity = ObjectIdentity
securityportSecurityGroup = _SecurityportSecurityGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 1)
)
_PortSecurityGlobalSettings_ObjectIdentity = ObjectIdentity
portSecurityGlobalSettings = _PortSecurityGlobalSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 1, 1)
)


class _PortSecurityTrapState_Type(Bits):
    """Custom type portSecurityTrapState based on Bits"""
    namedValues = NamedValues(
        ("portSecExceedMLA", 0)
    )

_PortSecurityTrapState_Type.__name__ = "Bits"
_PortSecurityTrapState_Object = MibScalar
portSecurityTrapState = _PortSecurityTrapState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 1, 1, 1),
    _PortSecurityTrapState_Type()
)
portSecurityTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityTrapState.setStatus("current")


class _PortSecurityTrapRate_Type(Integer32):
    """Custom type portSecurityTrapRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_PortSecurityTrapRate_Type.__name__ = "Integer32"
_PortSecurityTrapRate_Object = MibScalar
portSecurityTrapRate = _PortSecurityTrapRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 1, 1, 2),
    _PortSecurityTrapRate_Type()
)
portSecurityTrapRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityTrapRate.setStatus("current")


class _PortSecuritySysMaxAddr_Type(Integer32):
    """Custom type portSecuritySysMaxAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6656),
    )


_PortSecuritySysMaxAddr_Type.__name__ = "Integer32"
_PortSecuritySysMaxAddr_Object = MibScalar
portSecuritySysMaxAddr = _PortSecuritySysMaxAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 1, 1, 3),
    _PortSecuritySysMaxAddr_Type()
)
portSecuritySysMaxAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecuritySysMaxAddr.setStatus("current")
_PortSecurityPortSettings_ObjectIdentity = ObjectIdentity
portSecurityPortSettings = _PortSecurityPortSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 1, 2)
)
_PortSecurityTable_Object = MibTable
portSecurityTable = _PortSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 1, 2, 1)
)
if mibBuilder.loadTexts:
    portSecurityTable.setStatus("current")
_PortSecurityEntry_Object = MibTableRow
portSecurityEntry = _PortSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 1, 2, 1, 1)
)
portSecurityEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "portSecurityPort"),
)
if mibBuilder.loadTexts:
    portSecurityEntry.setStatus("current")
_PortSecurityPort_Type = Integer32
_PortSecurityPort_Object = MibTableColumn
portSecurityPort = _PortSecurityPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 1, 2, 1, 1, 1),
    _PortSecurityPort_Type()
)
portSecurityPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityPort.setStatus("current")


class _PortSecurityState_Type(Integer32):
    """Custom type portSecurityState based on Integer32"""
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


_PortSecurityState_Type.__name__ = "Integer32"
_PortSecurityState_Object = MibTableColumn
portSecurityState = _PortSecurityState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 1, 2, 1, 1, 2),
    _PortSecurityState_Type()
)
portSecurityState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityState.setStatus("current")


class _PortSecuritySysMax_Type(Integer32):
    """Custom type portSecuritySysMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6656),
    )


_PortSecuritySysMax_Type.__name__ = "Integer32"
_PortSecuritySysMax_Object = MibTableColumn
portSecuritySysMax = _PortSecuritySysMax_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 1, 2, 1, 1, 3),
    _PortSecuritySysMax_Type()
)
portSecuritySysMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecuritySysMax.setStatus("current")


class _PortSecurityVioAction_Type(Integer32):
    """Custom type portSecurityVioAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("protect", 1),
          ("restrict", 2),
          ("shutdown", 3))
    )


_PortSecurityVioAction_Type.__name__ = "Integer32"
_PortSecurityVioAction_Object = MibTableColumn
portSecurityVioAction = _PortSecurityVioAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 1, 2, 1, 1, 4),
    _PortSecurityVioAction_Type()
)
portSecurityVioAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityVioAction.setStatus("current")


class _PortSecuritySecurMode_Type(Integer32):
    """Custom type portSecuritySecurMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deleteOnTimeout", 2),
          ("permanent", 3))
    )


_PortSecuritySecurMode_Type.__name__ = "Integer32"
_PortSecuritySecurMode_Object = MibTableColumn
portSecuritySecurMode = _PortSecuritySecurMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 1, 2, 1, 1, 5),
    _PortSecuritySecurMode_Type()
)
portSecuritySecurMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecuritySecurMode.setStatus("current")


class _PortSecurityAgingTime_Type(Integer32):
    """Custom type portSecurityAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_PortSecurityAgingTime_Type.__name__ = "Integer32"
_PortSecurityAgingTime_Object = MibTableColumn
portSecurityAgingTime = _PortSecurityAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 1, 2, 1, 1, 6),
    _PortSecurityAgingTime_Type()
)
portSecurityAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityAgingTime.setStatus("current")


class _PortSecurityAgingType_Type(Integer32):
    """Custom type portSecurityAgingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absolute", 1),
          ("inactivity", 2))
    )


_PortSecurityAgingType_Type.__name__ = "Integer32"
_PortSecurityAgingType_Object = MibTableColumn
portSecurityAgingType = _PortSecurityAgingType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 1, 2, 1, 1, 7),
    _PortSecurityAgingType_Type()
)
portSecurityAgingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityAgingType.setStatus("current")


class _PortSecurityCurrentNo_Type(Integer32):
    """Custom type portSecurityCurrentNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_PortSecurityCurrentNo_Type.__name__ = "Integer32"
_PortSecurityCurrentNo_Object = MibTableColumn
portSecurityCurrentNo = _PortSecurityCurrentNo_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 1, 2, 1, 1, 8),
    _PortSecurityCurrentNo_Type()
)
portSecurityCurrentNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSecurityCurrentNo.setStatus("current")


class _PortSecurityVioCount_Type(Integer32):
    """Custom type portSecurityVioCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_PortSecurityVioCount_Type.__name__ = "Integer32"
_PortSecurityVioCount_Object = MibTableColumn
portSecurityVioCount = _PortSecurityVioCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 1, 2, 1, 1, 9),
    _PortSecurityVioCount_Type()
)
portSecurityVioCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSecurityVioCount.setStatus("current")


class _PortSecurityCurState_Type(Integer32):
    """Custom type portSecurityCurState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("err-disabled", 2),
          ("forwarding", 1),
          ("other", 0))
    )


_PortSecurityCurState_Type.__name__ = "Integer32"
_PortSecurityCurState_Object = MibTableColumn
portSecurityCurState = _PortSecurityCurState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 1, 2, 1, 1, 10),
    _PortSecurityCurState_Type()
)
portSecurityCurState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSecurityCurState.setStatus("current")
_PortSecurityAddressEntries_ObjectIdentity = ObjectIdentity
portSecurityAddressEntries = _PortSecurityAddressEntries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 1, 3)
)
_PortSecAddrTable_Object = MibTable
portSecAddrTable = _PortSecAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 1, 3, 1)
)
if mibBuilder.loadTexts:
    portSecAddrTable.setStatus("current")
_PortSecAddrEntry_Object = MibTableRow
portSecAddrEntry = _PortSecAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 1, 3, 1, 1)
)
portSecAddrEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "portSecAddrVID"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "portSecAddrMAC"),
)
if mibBuilder.loadTexts:
    portSecAddrEntry.setStatus("current")
_PortSecAddrVID_Type = Unsigned32
_PortSecAddrVID_Object = MibTableColumn
portSecAddrVID = _PortSecAddrVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 1, 3, 1, 1, 1),
    _PortSecAddrVID_Type()
)
portSecAddrVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSecAddrVID.setStatus("current")
_PortSecAddrMAC_Type = MacAddress
_PortSecAddrMAC_Object = MibTableColumn
portSecAddrMAC = _PortSecAddrMAC_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 1, 3, 1, 1, 2),
    _PortSecAddrMAC_Type()
)
portSecAddrMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSecAddrMAC.setStatus("current")
_PortSecAddrPort_Type = Integer32
_PortSecAddrPort_Object = MibTableColumn
portSecAddrPort = _PortSecAddrPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 1, 3, 1, 1, 3),
    _PortSecAddrPort_Type()
)
portSecAddrPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecAddrPort.setStatus("current")


class _PortSecAddrType_Type(Integer32):
    """Custom type portSecAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deleteOnTimeout", 2),
          ("permanent", 3))
    )


_PortSecAddrType_Type.__name__ = "Integer32"
_PortSecAddrType_Object = MibTableColumn
portSecAddrType = _PortSecAddrType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 1, 3, 1, 1, 4),
    _PortSecAddrType_Type()
)
portSecAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSecAddrType.setStatus("current")
_PortSecAddrRowStatus_Type = RowStatus
_PortSecAddrRowStatus_Object = MibTableColumn
portSecAddrRowStatus = _PortSecAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 1, 3, 1, 1, 5),
    _PortSecAddrRowStatus_Type()
)
portSecAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portSecAddrRowStatus.setStatus("current")
_PortSecAddrRemainTime_Type = Integer32
_PortSecAddrRemainTime_Object = MibTableColumn
portSecAddrRemainTime = _PortSecAddrRemainTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 1, 3, 1, 1, 6),
    _PortSecAddrRemainTime_Type()
)
portSecAddrRemainTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSecAddrRemainTime.setStatus("current")
_PortSecurityTraps_ObjectIdentity = ObjectIdentity
portSecurityTraps = _PortSecurityTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 1, 4)
)
_PortSecurityTrapList_ObjectIdentity = ObjectIdentity
portSecurityTrapList = _PortSecurityTrapList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 1, 4, 0)
)
_SecurityDhcpSerScrGroup_ObjectIdentity = ObjectIdentity
securityDhcpSerScrGroup = _SecurityDhcpSerScrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 7)
)
_DhcpSerScrGlobSettings_ObjectIdentity = ObjectIdentity
dhcpSerScrGlobSettings = _DhcpSerScrGlobSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 7, 1)
)


class _DhcpSerScrGlobTrapState_Type(Integer32):
    """Custom type dhcpSerScrGlobTrapState based on Integer32"""
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


_DhcpSerScrGlobTrapState_Type.__name__ = "Integer32"
_DhcpSerScrGlobTrapState_Object = MibScalar
dhcpSerScrGlobTrapState = _DhcpSerScrGlobTrapState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 7, 1, 1),
    _DhcpSerScrGlobTrapState_Type()
)
dhcpSerScrGlobTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSerScrGlobTrapState.setStatus("current")
_DhcpSerScrLogBufEntries_Type = Integer32
_DhcpSerScrLogBufEntries_Object = MibScalar
dhcpSerScrLogBufEntries = _DhcpSerScrLogBufEntries_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 7, 1, 2),
    _DhcpSerScrLogBufEntries_Type()
)
dhcpSerScrLogBufEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSerScrLogBufEntries.setStatus("current")
_DhcpSerScrLogClear_Type = TruthValue
_DhcpSerScrLogClear_Object = MibScalar
dhcpSerScrLogClear = _DhcpSerScrLogClear_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 7, 1, 3),
    _DhcpSerScrLogClear_Type()
)
dhcpSerScrLogClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSerScrLogClear.setStatus("current")
_DhcpSerScrProfileTable_Object = MibTable
dhcpSerScrProfileTable = _DhcpSerScrProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 7, 1, 4)
)
if mibBuilder.loadTexts:
    dhcpSerScrProfileTable.setStatus("current")
_DhcpSerScrProfileEntry_Object = MibTableRow
dhcpSerScrProfileEntry = _DhcpSerScrProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 7, 1, 4, 1)
)
dhcpSerScrProfileEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "dhcpSerScrProfileName"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "dhcpSerScrProfileClientMac"),
)
if mibBuilder.loadTexts:
    dhcpSerScrProfileEntry.setStatus("current")
_DhcpSerScrProfileName_Type = DisplayString
_DhcpSerScrProfileName_Object = MibTableColumn
dhcpSerScrProfileName = _DhcpSerScrProfileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 7, 1, 4, 1, 1),
    _DhcpSerScrProfileName_Type()
)
dhcpSerScrProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSerScrProfileName.setStatus("current")
_DhcpSerScrProfileClientMac_Type = MacAddress
_DhcpSerScrProfileClientMac_Object = MibTableColumn
dhcpSerScrProfileClientMac = _DhcpSerScrProfileClientMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 7, 1, 4, 1, 2),
    _DhcpSerScrProfileClientMac_Type()
)
dhcpSerScrProfileClientMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSerScrProfileClientMac.setStatus("current")
_DhcpSerScrProfileRowStatus_Type = RowStatus
_DhcpSerScrProfileRowStatus_Object = MibTableColumn
dhcpSerScrProfileRowStatus = _DhcpSerScrProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 7, 1, 4, 1, 3),
    _DhcpSerScrProfileRowStatus_Type()
)
dhcpSerScrProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSerScrProfileRowStatus.setStatus("current")
_DhcpSerScrLogTable_Object = MibTable
dhcpSerScrLogTable = _DhcpSerScrLogTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 7, 1, 5)
)
if mibBuilder.loadTexts:
    dhcpSerScrLogTable.setStatus("current")
_DhcpSerScrLogEntry_Object = MibTableRow
dhcpSerScrLogEntry = _DhcpSerScrLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 7, 1, 5, 1)
)
dhcpSerScrLogEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "dhcpSerScrLogIndex"),
)
if mibBuilder.loadTexts:
    dhcpSerScrLogEntry.setStatus("current")
_DhcpSerScrLogIndex_Type = Unsigned32
_DhcpSerScrLogIndex_Object = MibTableColumn
dhcpSerScrLogIndex = _DhcpSerScrLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 7, 1, 5, 1, 1),
    _DhcpSerScrLogIndex_Type()
)
dhcpSerScrLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSerScrLogIndex.setStatus("current")
_DhcpSerScrLogVlanID_Type = Integer32
_DhcpSerScrLogVlanID_Object = MibTableColumn
dhcpSerScrLogVlanID = _DhcpSerScrLogVlanID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 7, 1, 5, 1, 2),
    _DhcpSerScrLogVlanID_Type()
)
dhcpSerScrLogVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSerScrLogVlanID.setStatus("current")
_DhcpSerScrLogIPAddr_Type = InetAddress
_DhcpSerScrLogIPAddr_Object = MibTableColumn
dhcpSerScrLogIPAddr = _DhcpSerScrLogIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 7, 1, 5, 1, 3),
    _DhcpSerScrLogIPAddr_Type()
)
dhcpSerScrLogIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSerScrLogIPAddr.setStatus("current")
_DhcpSerScrLogMacAddr_Type = MacAddress
_DhcpSerScrLogMacAddr_Object = MibTableColumn
dhcpSerScrLogMacAddr = _DhcpSerScrLogMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 7, 1, 5, 1, 4),
    _DhcpSerScrLogMacAddr_Type()
)
dhcpSerScrLogMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSerScrLogMacAddr.setStatus("current")
_DhcpSerScrLogOccurrence_Type = DisplayString
_DhcpSerScrLogOccurrence_Object = MibTableColumn
dhcpSerScrLogOccurrence = _DhcpSerScrLogOccurrence_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 7, 1, 5, 1, 5),
    _DhcpSerScrLogOccurrence_Type()
)
dhcpSerScrLogOccurrence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSerScrLogOccurrence.setStatus("current")
_DhcpSerScrPortSettings_ObjectIdentity = ObjectIdentity
dhcpSerScrPortSettings = _DhcpSerScrPortSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 7, 2)
)
_DhcpSerScrPortTable_Object = MibTable
dhcpSerScrPortTable = _DhcpSerScrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 7, 2, 1)
)
if mibBuilder.loadTexts:
    dhcpSerScrPortTable.setStatus("current")
_DhcpSerScrPortEntry_Object = MibTableRow
dhcpSerScrPortEntry = _DhcpSerScrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 7, 2, 1, 1)
)
dhcpSerScrPortEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "dhcpSerScrPortIndex"),
)
if mibBuilder.loadTexts:
    dhcpSerScrPortEntry.setStatus("current")
_DhcpSerScrPortIndex_Type = Integer32
_DhcpSerScrPortIndex_Object = MibTableColumn
dhcpSerScrPortIndex = _DhcpSerScrPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 7, 2, 1, 1, 1),
    _DhcpSerScrPortIndex_Type()
)
dhcpSerScrPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSerScrPortIndex.setStatus("current")


class _DhcpSerScrPortState_Type(Integer32):
    """Custom type dhcpSerScrPortState based on Integer32"""
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


_DhcpSerScrPortState_Type.__name__ = "Integer32"
_DhcpSerScrPortState_Object = MibTableColumn
dhcpSerScrPortState = _DhcpSerScrPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 7, 2, 1, 1, 2),
    _DhcpSerScrPortState_Type()
)
dhcpSerScrPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSerScrPortState.setStatus("current")
_DhcpSerScrPortServerAddrType_Type = InetAddressType
_DhcpSerScrPortServerAddrType_Object = MibTableColumn
dhcpSerScrPortServerAddrType = _DhcpSerScrPortServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 7, 2, 1, 1, 3),
    _DhcpSerScrPortServerAddrType_Type()
)
dhcpSerScrPortServerAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSerScrPortServerAddrType.setStatus("current")
_DhcpSerScrPortServerIP_Type = InetAddress
_DhcpSerScrPortServerIP_Object = MibTableColumn
dhcpSerScrPortServerIP = _DhcpSerScrPortServerIP_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 7, 2, 1, 1, 4),
    _DhcpSerScrPortServerIP_Type()
)
dhcpSerScrPortServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSerScrPortServerIP.setStatus("current")
_DhcpSerScrPortProfileName_Type = DisplayString
_DhcpSerScrPortProfileName_Object = MibTableColumn
dhcpSerScrPortProfileName = _DhcpSerScrPortProfileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 7, 2, 1, 1, 5),
    _DhcpSerScrPortProfileName_Type()
)
dhcpSerScrPortProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSerScrPortProfileName.setStatus("current")
_DhcpSerScrTraps_ObjectIdentity = ObjectIdentity
dhcpSerScrTraps = _DhcpSerScrTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 7, 3)
)
_DhcpSerScrTrapList_ObjectIdentity = ObjectIdentity
dhcpSerScrTrapList = _DhcpSerScrTrapList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 7, 3, 0)
)
_SecuritySafeGuardGroup_ObjectIdentity = ObjectIdentity
securitySafeGuardGroup = _SecuritySafeGuardGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 13)
)


class _SafeGuardEnable_Type(Integer32):
    """Custom type safeGuardEnable based on Integer32"""
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


_SafeGuardEnable_Type.__name__ = "Integer32"
_SafeGuardEnable_Object = MibScalar
safeGuardEnable = _SafeGuardEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 13, 1),
    _SafeGuardEnable_Type()
)
safeGuardEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    safeGuardEnable.setStatus("current")
_SecurityTrustedHostGroup_ObjectIdentity = ObjectIdentity
securityTrustedHostGroup = _SecurityTrustedHostGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 14)
)
_TrustedHostTable_Object = MibTable
trustedHostTable = _TrustedHostTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 14, 1)
)
if mibBuilder.loadTexts:
    trustedHostTable.setStatus("current")
_TrustedHostEntry_Object = MibTableRow
trustedHostEntry = _TrustedHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 14, 1, 1)
)
trustedHostEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "trustedHostType"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "trustedHostACLName"),
)
if mibBuilder.loadTexts:
    trustedHostEntry.setStatus("current")


class _TrustedHostType_Type(Integer32):
    """Custom type trustedHostType based on Integer32"""
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
        *(("http", 3),
          ("https", 4),
          ("ping", 2),
          ("telnet", 1))
    )


_TrustedHostType_Type.__name__ = "Integer32"
_TrustedHostType_Object = MibTableColumn
trustedHostType = _TrustedHostType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 14, 1, 1, 1),
    _TrustedHostType_Type()
)
trustedHostType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trustedHostType.setStatus("current")


class _TrustedHostACLName_Type(DisplayString):
    """Custom type trustedHostACLName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TrustedHostACLName_Type.__name__ = "DisplayString"
_TrustedHostACLName_Object = MibTableColumn
trustedHostACLName = _TrustedHostACLName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 14, 1, 1, 2),
    _TrustedHostACLName_Type()
)
trustedHostACLName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trustedHostACLName.setStatus("current")
_TrustedHostRowStatus_Type = RowStatus
_TrustedHostRowStatus_Object = MibTableColumn
trustedHostRowStatus = _TrustedHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 14, 1, 1, 3),
    _TrustedHostRowStatus_Type()
)
trustedHostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trustedHostRowStatus.setStatus("current")
_SecurityTrafficSegmentationGroup_ObjectIdentity = ObjectIdentity
securityTrafficSegmentationGroup = _SecurityTrafficSegmentationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 15)
)
_TrafficSegmentationTable_Object = MibTable
trafficSegmentationTable = _TrafficSegmentationTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 15, 1)
)
if mibBuilder.loadTexts:
    trafficSegmentationTable.setStatus("current")
_TrafficSegmentationEntry_Object = MibTableRow
trafficSegmentationEntry = _TrafficSegmentationEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 15, 1, 1)
)
trafficSegmentationEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "trafficSegmentationIfIndex"),
)
if mibBuilder.loadTexts:
    trafficSegmentationEntry.setStatus("current")
_TrafficSegmentationIfIndex_Type = InterfaceIndex
_TrafficSegmentationIfIndex_Object = MibTableColumn
trafficSegmentationIfIndex = _TrafficSegmentationIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 15, 1, 1, 1),
    _TrafficSegmentationIfIndex_Type()
)
trafficSegmentationIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficSegmentationIfIndex.setStatus("current")
_TrafficSegmentationMemberList_Type = PortList
_TrafficSegmentationMemberList_Object = MibTableColumn
trafficSegmentationMemberList = _TrafficSegmentationMemberList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 15, 1, 1, 2),
    _TrafficSegmentationMemberList_Type()
)
trafficSegmentationMemberList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficSegmentationMemberList.setStatus("current")
_SecurityStormCtrlGroup_ObjectIdentity = ObjectIdentity
securityStormCtrlGroup = _SecurityStormCtrlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 16)
)
_StormCtrlMIBObjects_ObjectIdentity = ObjectIdentity
stormCtrlMIBObjects = _StormCtrlMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 16, 1)
)
_StormCtrlGentrl_ObjectIdentity = ObjectIdentity
stormCtrlGentrl = _StormCtrlGentrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 16, 1, 1)
)


class _StormCtrlNotifyEnable_Type(Integer32):
    """Custom type stormCtrlNotifyEnable based on Integer32"""
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
        *(("both", 3),
          ("none", 0),
          ("stormCleared", 2),
          ("stormOccurred", 1))
    )


_StormCtrlNotifyEnable_Type.__name__ = "Integer32"
_StormCtrlNotifyEnable_Object = MibScalar
stormCtrlNotifyEnable = _StormCtrlNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 16, 1, 1, 1),
    _StormCtrlNotifyEnable_Type()
)
stormCtrlNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stormCtrlNotifyEnable.setStatus("current")


class _StormCtrlPollingInterval_Type(Integer32):
    """Custom type stormCtrlPollingInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 600),
    )


_StormCtrlPollingInterval_Type.__name__ = "Integer32"
_StormCtrlPollingInterval_Object = MibScalar
stormCtrlPollingInterval = _StormCtrlPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 16, 1, 1, 2),
    _StormCtrlPollingInterval_Type()
)
stormCtrlPollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stormCtrlPollingInterval.setStatus("current")


class _StormCtrlPollingRetries_Type(Integer32):
    """Custom type stormCtrlPollingRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 360),
    )


_StormCtrlPollingRetries_Type.__name__ = "Integer32"
_StormCtrlPollingRetries_Object = MibScalar
stormCtrlPollingRetries = _StormCtrlPollingRetries_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 16, 1, 1, 3),
    _StormCtrlPollingRetries_Type()
)
stormCtrlPollingRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stormCtrlPollingRetries.setStatus("current")
_StormCtrlTable_Object = MibTable
stormCtrlTable = _StormCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 16, 1, 1, 4)
)
if mibBuilder.loadTexts:
    stormCtrlTable.setStatus("current")
_StormCtrlEntry_Object = MibTableRow
stormCtrlEntry = _StormCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 16, 1, 1, 4, 1)
)
stormCtrlEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "stormCtrlIndex"),
)
if mibBuilder.loadTexts:
    stormCtrlEntry.setStatus("current")


class _StormCtrlIndex_Type(Integer32):
    """Custom type stormCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_StormCtrlIndex_Type.__name__ = "Integer32"
_StormCtrlIndex_Object = MibTableColumn
stormCtrlIndex = _StormCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 16, 1, 1, 4, 1, 1),
    _StormCtrlIndex_Type()
)
stormCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stormCtrlIndex.setStatus("current")


class _StormCtrlActionMode_Type(Integer32):
    """Custom type stormCtrlActionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("none", 0),
          ("shutdown", 2))
    )


_StormCtrlActionMode_Type.__name__ = "Integer32"
_StormCtrlActionMode_Object = MibTableColumn
stormCtrlActionMode = _StormCtrlActionMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 16, 1, 1, 4, 1, 2),
    _StormCtrlActionMode_Type()
)
stormCtrlActionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stormCtrlActionMode.setStatus("current")


class _StormCtrlLevelType_Type(Integer32):
    """Custom type stormCtrlLevelType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("kbps", 2),
          ("pps", 1))
    )


_StormCtrlLevelType_Type.__name__ = "Integer32"
_StormCtrlLevelType_Object = MibTableColumn
stormCtrlLevelType = _StormCtrlLevelType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 16, 1, 1, 4, 1, 3),
    _StormCtrlLevelType_Type()
)
stormCtrlLevelType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stormCtrlLevelType.setStatus("current")
_StormCtrlThresholdTable_Object = MibTable
stormCtrlThresholdTable = _StormCtrlThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 16, 1, 1, 5)
)
if mibBuilder.loadTexts:
    stormCtrlThresholdTable.setStatus("current")
_StormCtrlThresholdEntry_Object = MibTableRow
stormCtrlThresholdEntry = _StormCtrlThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 16, 1, 1, 5, 1)
)
stormCtrlThresholdEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "stormCtrlThresholdIndex"),
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "stormCtrlThresholdType"),
)
if mibBuilder.loadTexts:
    stormCtrlThresholdEntry.setStatus("current")


class _StormCtrlThresholdIndex_Type(Integer32):
    """Custom type stormCtrlThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_StormCtrlThresholdIndex_Type.__name__ = "Integer32"
_StormCtrlThresholdIndex_Object = MibTableColumn
stormCtrlThresholdIndex = _StormCtrlThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 16, 1, 1, 5, 1, 1),
    _StormCtrlThresholdIndex_Type()
)
stormCtrlThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stormCtrlThresholdIndex.setStatus("current")


class _StormCtrlThresholdType_Type(Integer32):
    """Custom type stormCtrlThresholdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("multicast", 2),
          ("unicast", 3))
    )


_StormCtrlThresholdType_Type.__name__ = "Integer32"
_StormCtrlThresholdType_Object = MibTableColumn
stormCtrlThresholdType = _StormCtrlThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 16, 1, 1, 5, 1, 2),
    _StormCtrlThresholdType_Type()
)
stormCtrlThresholdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stormCtrlThresholdType.setStatus("current")


class _StormCtrlThresholdRiseThre_Type(Integer32):
    """Custom type stormCtrlThresholdRiseThre based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StormCtrlThresholdRiseThre_Type.__name__ = "Integer32"
_StormCtrlThresholdRiseThre_Object = MibTableColumn
stormCtrlThresholdRiseThre = _StormCtrlThresholdRiseThre_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 16, 1, 1, 5, 1, 3),
    _StormCtrlThresholdRiseThre_Type()
)
stormCtrlThresholdRiseThre.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stormCtrlThresholdRiseThre.setStatus("current")


class _StormCtrlThresholdLowThre_Type(Integer32):
    """Custom type stormCtrlThresholdLowThre based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StormCtrlThresholdLowThre_Type.__name__ = "Integer32"
_StormCtrlThresholdLowThre_Object = MibTableColumn
stormCtrlThresholdLowThre = _StormCtrlThresholdLowThre_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 16, 1, 1, 5, 1, 4),
    _StormCtrlThresholdLowThre_Type()
)
stormCtrlThresholdLowThre.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stormCtrlThresholdLowThre.setStatus("current")
_StormCtrlThresholdCurrRate_Type = Integer32
_StormCtrlThresholdCurrRate_Object = MibTableColumn
stormCtrlThresholdCurrRate = _StormCtrlThresholdCurrRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 16, 1, 1, 5, 1, 5),
    _StormCtrlThresholdCurrRate_Type()
)
stormCtrlThresholdCurrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stormCtrlThresholdCurrRate.setStatus("current")


class _StormCtrlThresholdStormState_Type(Integer32):
    """Custom type stormCtrlThresholdStormState based on Integer32"""
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
        *(("dropped", 2),
          ("errorDisabled", 3),
          ("forwarding", 1),
          ("inactive", 5),
          ("linkDown", 4))
    )


_StormCtrlThresholdStormState_Type.__name__ = "Integer32"
_StormCtrlThresholdStormState_Object = MibTableColumn
stormCtrlThresholdStormState = _StormCtrlThresholdStormState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 16, 1, 1, 5, 1, 6),
    _StormCtrlThresholdStormState_Type()
)
stormCtrlThresholdStormState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stormCtrlThresholdStormState.setStatus("current")
_StormCtrlTraps_ObjectIdentity = ObjectIdentity
stormCtrlTraps = _StormCtrlTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 16, 1, 1, 6)
)
_StormCtrlTrapsList_ObjectIdentity = ObjectIdentity
stormCtrlTrapsList = _StormCtrlTrapsList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 16, 1, 1, 6, 0)
)
_SecurityDoSprevGroup_ObjectIdentity = ObjectIdentity
securityDoSprevGroup = _SecurityDoSprevGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 17)
)
_DoSCtrlTable_Object = MibTable
doSCtrlTable = _DoSCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 17, 1)
)
if mibBuilder.loadTexts:
    doSCtrlTable.setStatus("current")
_DoSCtrlEntry_Object = MibTableRow
doSCtrlEntry = _DoSCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 17, 1, 1)
)
doSCtrlEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "doSCtrlType"),
)
if mibBuilder.loadTexts:
    doSCtrlEntry.setStatus("current")


class _DoSCtrlType_Type(Integer32):
    """Custom type doSCtrlType based on Integer32"""
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
        *(("blat-attack", 2),
          ("land-attack", 1),
          ("ping-of-death-attack", 7),
          ("tcp-null-scan", 3),
          ("tcp-syn-srcport-less-1024", 6),
          ("tcp-synfin", 5),
          ("tcp-tiny-fragment-attack", 8),
          ("tcp-xmascan", 4))
    )


_DoSCtrlType_Type.__name__ = "Integer32"
_DoSCtrlType_Object = MibTableColumn
doSCtrlType = _DoSCtrlType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 17, 1, 1, 1),
    _DoSCtrlType_Type()
)
doSCtrlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doSCtrlType.setStatus("current")


class _DoSCtrlState_Type(Integer32):
    """Custom type doSCtrlState based on Integer32"""
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


_DoSCtrlState_Type.__name__ = "Integer32"
_DoSCtrlState_Object = MibTableColumn
doSCtrlState = _DoSCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 17, 1, 1, 2),
    _DoSCtrlState_Type()
)
doSCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    doSCtrlState.setStatus("current")


class _DoSCtrlActionType_Type(Integer32):
    """Custom type doSCtrlActionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("drop", 1)
    )


_DoSCtrlActionType_Type.__name__ = "Integer32"
_DoSCtrlActionType_Object = MibTableColumn
doSCtrlActionType = _DoSCtrlActionType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 17, 1, 1, 3),
    _DoSCtrlActionType_Type()
)
doSCtrlActionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    doSCtrlActionType.setStatus("current")
_SecuritySSLGroup_ObjectIdentity = ObjectIdentity
securitySSLGroup = _SecuritySSLGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 19)
)
_SslObjects_ObjectIdentity = ObjectIdentity
sslObjects = _SslObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 19, 1)
)


class _SslServerStatus_Type(Integer32):
    """Custom type sslServerStatus based on Integer32"""
    defaultValue = 2

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


_SslServerStatus_Type.__name__ = "Integer32"
_SslServerStatus_Object = MibScalar
sslServerStatus = _SslServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 19, 1, 1),
    _SslServerStatus_Type()
)
sslServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslServerStatus.setStatus("current")


class _ServicePolicyName_Type(DisplayString):
    """Custom type servicePolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ServicePolicyName_Type.__name__ = "DisplayString"
_ServicePolicyName_Object = MibScalar
servicePolicyName = _ServicePolicyName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 19, 1, 2),
    _ServicePolicyName_Type()
)
servicePolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    servicePolicyName.setStatus("current")
_SslConfiguration_ObjectIdentity = ObjectIdentity
sslConfiguration = _SslConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 19, 1, 4)
)
_SslServicePolicyTable_Object = MibTable
sslServicePolicyTable = _SslServicePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 19, 1, 4, 3)
)
if mibBuilder.loadTexts:
    sslServicePolicyTable.setStatus("current")
_SslServicePolicyEntry_Object = MibTableRow
sslServicePolicyEntry = _SslServicePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 19, 1, 4, 3, 1)
)
sslServicePolicyEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "sslServicePolicyName"),
)
if mibBuilder.loadTexts:
    sslServicePolicyEntry.setStatus("current")


class _SslServicePolicyName_Type(DisplayString):
    """Custom type sslServicePolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SslServicePolicyName_Type.__name__ = "DisplayString"
_SslServicePolicyName_Object = MibTableColumn
sslServicePolicyName = _SslServicePolicyName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 19, 1, 4, 3, 1, 1),
    _SslServicePolicyName_Type()
)
sslServicePolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslServicePolicyName.setStatus("current")


class _SslServicePolicyCipherSuites_Type(Bits):
    """Custom type sslServicePolicyCipherSuites based on Bits"""
    namedValues = NamedValues(
        *(("dh-rsa-3des-sha", 5),
          ("dh-rsa-des-sha", 4),
          ("dhe-rsa-with-aes-128-cbc-sha", 9),
          ("dhe-rsa-with-aes-256-cbc-sha", 10),
          ("rsa-3des-sha", 3),
          ("rsa-des-sha", 2),
          ("rsa-exp1024-des-sha", 6),
          ("rsa-null-md5", 0),
          ("rsa-null-sha", 1),
          ("rsa-with-aes-128-cbc-sha", 7),
          ("rsa-with-aes-256-cbc-sha", 8))
    )

_SslServicePolicyCipherSuites_Type.__name__ = "Bits"
_SslServicePolicyCipherSuites_Object = MibTableColumn
sslServicePolicyCipherSuites = _SslServicePolicyCipherSuites_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 19, 1, 4, 3, 1, 2),
    _SslServicePolicyCipherSuites_Type()
)
sslServicePolicyCipherSuites.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslServicePolicyCipherSuites.setStatus("current")


class _SslServicePolicyCacheTimeout_Type(Unsigned32):
    """Custom type sslServicePolicyCacheTimeout based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_SslServicePolicyCacheTimeout_Type.__name__ = "Unsigned32"
_SslServicePolicyCacheTimeout_Object = MibTableColumn
sslServicePolicyCacheTimeout = _SslServicePolicyCacheTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 19, 1, 4, 3, 1, 4),
    _SslServicePolicyCacheTimeout_Type()
)
sslServicePolicyCacheTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sslServicePolicyCacheTimeout.setStatus("current")
_SslServicePolicyRowStatus_Type = RowStatus
_SslServicePolicyRowStatus_Object = MibTableColumn
sslServicePolicyRowStatus = _SslServicePolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 19, 1, 4, 3, 1, 5),
    _SslServicePolicyRowStatus_Type()
)
sslServicePolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sslServicePolicyRowStatus.setStatus("current")
_DlinkOAM_ObjectIdentity = ObjectIdentity
dlinkOAM = _DlinkOAM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 9)
)
_OamCableDiagGroup_ObjectIdentity = ObjectIdentity
oamCableDiagGroup = _OamCableDiagGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 9, 1)
)


class _CableDiagTriggerIndex_Type(Integer32):
    """Custom type cableDiagTriggerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 28),
    )


_CableDiagTriggerIndex_Type.__name__ = "Integer32"
_CableDiagTriggerIndex_Object = MibScalar
cableDiagTriggerIndex = _CableDiagTriggerIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 9, 1, 1),
    _CableDiagTriggerIndex_Type()
)
cableDiagTriggerIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cableDiagTriggerIndex.setStatus("current")
_CableDiagTestPairTable_Object = MibTable
cableDiagTestPairTable = _CableDiagTestPairTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 9, 1, 2)
)
if mibBuilder.loadTexts:
    cableDiagTestPairTable.setStatus("current")
_CableDiagTestPairEntry_Object = MibTableRow
cableDiagTestPairEntry = _CableDiagTestPairEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 9, 1, 2, 1)
)
cableDiagTestPairEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "cableDiagTestPortPair"),
)
if mibBuilder.loadTexts:
    cableDiagTestPairEntry.setStatus("current")
_CableDiagTestPortPair_Type = Integer32
_CableDiagTestPortPair_Object = MibTableColumn
cableDiagTestPortPair = _CableDiagTestPortPair_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 9, 1, 2, 1, 1),
    _CableDiagTestPortPair_Type()
)
cableDiagTestPortPair.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagTestPortPair.setStatus("current")


class _CableDiagTestResultPair1_Type(Integer32):
    """Custom type cableDiagTestResultPair1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("crosstalk", 4),
          ("notAvailable", 5),
          ("ok", 0),
          ("open", 1),
          ("short", 2))
    )


_CableDiagTestResultPair1_Type.__name__ = "Integer32"
_CableDiagTestResultPair1_Object = MibTableColumn
cableDiagTestResultPair1 = _CableDiagTestResultPair1_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 9, 1, 2, 1, 2),
    _CableDiagTestResultPair1_Type()
)
cableDiagTestResultPair1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagTestResultPair1.setStatus("current")


class _CableDiagTestResultPair2_Type(Integer32):
    """Custom type cableDiagTestResultPair2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("crosstalk", 4),
          ("notAvailable", 5),
          ("ok", 0),
          ("open", 1),
          ("short", 2))
    )


_CableDiagTestResultPair2_Type.__name__ = "Integer32"
_CableDiagTestResultPair2_Object = MibTableColumn
cableDiagTestResultPair2 = _CableDiagTestResultPair2_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 9, 1, 2, 1, 3),
    _CableDiagTestResultPair2_Type()
)
cableDiagTestResultPair2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagTestResultPair2.setStatus("current")


class _CableDiagTestResultPair3_Type(Integer32):
    """Custom type cableDiagTestResultPair3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("crosstalk", 4),
          ("notAvailable", 5),
          ("ok", 0),
          ("open", 1),
          ("short", 2))
    )


_CableDiagTestResultPair3_Type.__name__ = "Integer32"
_CableDiagTestResultPair3_Object = MibTableColumn
cableDiagTestResultPair3 = _CableDiagTestResultPair3_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 9, 1, 2, 1, 4),
    _CableDiagTestResultPair3_Type()
)
cableDiagTestResultPair3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagTestResultPair3.setStatus("current")


class _CableDiagTestResultPair4_Type(Integer32):
    """Custom type cableDiagTestResultPair4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("crosstalk", 4),
          ("notAvailable", 5),
          ("ok", 0),
          ("open", 1),
          ("short", 2))
    )


_CableDiagTestResultPair4_Type.__name__ = "Integer32"
_CableDiagTestResultPair4_Object = MibTableColumn
cableDiagTestResultPair4 = _CableDiagTestResultPair4_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 9, 1, 2, 1, 5),
    _CableDiagTestResultPair4_Type()
)
cableDiagTestResultPair4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagTestResultPair4.setStatus("current")
_CableDiagTestLenPair1_Type = Integer32
_CableDiagTestLenPair1_Object = MibTableColumn
cableDiagTestLenPair1 = _CableDiagTestLenPair1_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 9, 1, 2, 1, 6),
    _CableDiagTestLenPair1_Type()
)
cableDiagTestLenPair1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagTestLenPair1.setStatus("current")
_CableDiagTestLenPair2_Type = Integer32
_CableDiagTestLenPair2_Object = MibTableColumn
cableDiagTestLenPair2 = _CableDiagTestLenPair2_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 9, 1, 2, 1, 7),
    _CableDiagTestLenPair2_Type()
)
cableDiagTestLenPair2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagTestLenPair2.setStatus("current")
_CableDiagTestLenPair3_Type = Integer32
_CableDiagTestLenPair3_Object = MibTableColumn
cableDiagTestLenPair3 = _CableDiagTestLenPair3_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 9, 1, 2, 1, 8),
    _CableDiagTestLenPair3_Type()
)
cableDiagTestLenPair3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagTestLenPair3.setStatus("current")
_CableDiagTestLenPair4_Type = Integer32
_CableDiagTestLenPair4_Object = MibTableColumn
cableDiagTestLenPair4 = _CableDiagTestLenPair4_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 9, 1, 2, 1, 9),
    _CableDiagTestLenPair4_Type()
)
cableDiagTestLenPair4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagTestLenPair4.setStatus("current")
_CableDiagTestLenPairClear_Type = Integer32
_CableDiagTestLenPairClear_Object = MibTableColumn
cableDiagTestLenPairClear = _CableDiagTestLenPairClear_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 9, 1, 2, 1, 10),
    _CableDiagTestLenPairClear_Type()
)
cableDiagTestLenPairClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cableDiagTestLenPairClear.setStatus("current")
_DlinkMonitoring_ObjectIdentity = ObjectIdentity
dlinkMonitoring = _DlinkMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10)
)
_MonStatisticsGroup_ObjectIdentity = ObjectIdentity
monStatisticsGroup = _MonStatisticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2)
)
_StatisticsCounters_ObjectIdentity = ObjectIdentity
statisticsCounters = _StatisticsCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 1)
)
_StatisticsCountersTable_Object = MibTable
statisticsCountersTable = _StatisticsCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 1, 1)
)
if mibBuilder.loadTexts:
    statisticsCountersTable.setStatus("current")
_StatisticsCountersEntry_Object = MibTableRow
statisticsCountersEntry = _StatisticsCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 1, 1, 1)
)
statisticsCountersEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "statPort"),
)
if mibBuilder.loadTexts:
    statisticsCountersEntry.setStatus("current")
_StatPort_Type = InterfaceIndex
_StatPort_Object = MibTableColumn
statPort = _StatPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 1, 1, 1, 1),
    _StatPort_Type()
)
statPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPort.setStatus("current")
_StatPortRxRateBytes_Type = Counter32
_StatPortRxRateBytes_Object = MibTableColumn
statPortRxRateBytes = _StatPortRxRateBytes_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 1, 1, 1, 2),
    _StatPortRxRateBytes_Type()
)
statPortRxRateBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPortRxRateBytes.setStatus("current")
_StatPortRxRatePackets_Type = Counter32
_StatPortRxRatePackets_Object = MibTableColumn
statPortRxRatePackets = _StatPortRxRatePackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 1, 1, 1, 3),
    _StatPortRxRatePackets_Type()
)
statPortRxRatePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPortRxRatePackets.setStatus("current")
_StatPortRxTotalBytes_Type = Counter64
_StatPortRxTotalBytes_Object = MibTableColumn
statPortRxTotalBytes = _StatPortRxTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 1, 1, 1, 4),
    _StatPortRxTotalBytes_Type()
)
statPortRxTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPortRxTotalBytes.setStatus("current")
_StatPortRxTotalPackets_Type = Counter64
_StatPortRxTotalPackets_Object = MibTableColumn
statPortRxTotalPackets = _StatPortRxTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 1, 1, 1, 5),
    _StatPortRxTotalPackets_Type()
)
statPortRxTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPortRxTotalPackets.setStatus("current")
_StatPortTxRateBytes_Type = Counter32
_StatPortTxRateBytes_Object = MibTableColumn
statPortTxRateBytes = _StatPortTxRateBytes_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 1, 1, 1, 6),
    _StatPortTxRateBytes_Type()
)
statPortTxRateBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPortTxRateBytes.setStatus("current")
_StatPortTxRatePackets_Type = Counter32
_StatPortTxRatePackets_Object = MibTableColumn
statPortTxRatePackets = _StatPortTxRatePackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 1, 1, 1, 7),
    _StatPortTxRatePackets_Type()
)
statPortTxRatePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPortTxRatePackets.setStatus("current")
_StatPortTxTotalBytes_Type = Counter64
_StatPortTxTotalBytes_Object = MibTableColumn
statPortTxTotalBytes = _StatPortTxTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 1, 1, 1, 8),
    _StatPortTxTotalBytes_Type()
)
statPortTxTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPortTxTotalBytes.setStatus("current")
_StatPortTxTotalPackets_Type = Counter64
_StatPortTxTotalPackets_Object = MibTableColumn
statPortTxTotalPackets = _StatPortTxTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 1, 1, 1, 9),
    _StatPortTxTotalPackets_Type()
)
statPortTxTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPortTxTotalPackets.setStatus("current")
_StatPortRxMulticast_Type = Counter64
_StatPortRxMulticast_Object = MibTableColumn
statPortRxMulticast = _StatPortRxMulticast_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 1, 1, 1, 10),
    _StatPortRxMulticast_Type()
)
statPortRxMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPortRxMulticast.setStatus("current")
_StatPortRxUnicast_Type = Counter64
_StatPortRxUnicast_Object = MibTableColumn
statPortRxUnicast = _StatPortRxUnicast_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 1, 1, 1, 11),
    _StatPortRxUnicast_Type()
)
statPortRxUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPortRxUnicast.setStatus("current")
_StatPortRxBroadcast_Type = Counter64
_StatPortRxBroadcast_Object = MibTableColumn
statPortRxBroadcast = _StatPortRxBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 1, 1, 1, 12),
    _StatPortRxBroadcast_Type()
)
statPortRxBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPortRxBroadcast.setStatus("current")
_StatPortTxMulticast_Type = Counter64
_StatPortTxMulticast_Object = MibTableColumn
statPortTxMulticast = _StatPortTxMulticast_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 1, 1, 1, 13),
    _StatPortTxMulticast_Type()
)
statPortTxMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPortTxMulticast.setStatus("current")
_StatPortTxUnicast_Type = Counter64
_StatPortTxUnicast_Object = MibTableColumn
statPortTxUnicast = _StatPortTxUnicast_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 1, 1, 1, 14),
    _StatPortTxUnicast_Type()
)
statPortTxUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPortTxUnicast.setStatus("current")
_StatPortTxBroadcast_Type = Counter64
_StatPortTxBroadcast_Object = MibTableColumn
statPortTxBroadcast = _StatPortTxBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 1, 1, 1, 15),
    _StatPortTxBroadcast_Type()
)
statPortTxBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPortTxBroadcast.setStatus("current")
_StatCountersrxHCPkt64Octets_Type = Counter64
_StatCountersrxHCPkt64Octets_Object = MibTableColumn
statCountersrxHCPkt64Octets = _StatCountersrxHCPkt64Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 1, 1, 1, 16),
    _StatCountersrxHCPkt64Octets_Type()
)
statCountersrxHCPkt64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statCountersrxHCPkt64Octets.setStatus("current")
_StatCountersrxHCPkt65to127Octets_Type = Counter64
_StatCountersrxHCPkt65to127Octets_Object = MibTableColumn
statCountersrxHCPkt65to127Octets = _StatCountersrxHCPkt65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 1, 1, 1, 17),
    _StatCountersrxHCPkt65to127Octets_Type()
)
statCountersrxHCPkt65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statCountersrxHCPkt65to127Octets.setStatus("current")
_StatCountersrxHCPkt128to255Octets_Type = Counter64
_StatCountersrxHCPkt128to255Octets_Object = MibTableColumn
statCountersrxHCPkt128to255Octets = _StatCountersrxHCPkt128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 1, 1, 1, 18),
    _StatCountersrxHCPkt128to255Octets_Type()
)
statCountersrxHCPkt128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statCountersrxHCPkt128to255Octets.setStatus("current")
_StatCountersrxHCPkt256to511Octets_Type = Counter64
_StatCountersrxHCPkt256to511Octets_Object = MibTableColumn
statCountersrxHCPkt256to511Octets = _StatCountersrxHCPkt256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 1, 1, 1, 19),
    _StatCountersrxHCPkt256to511Octets_Type()
)
statCountersrxHCPkt256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statCountersrxHCPkt256to511Octets.setStatus("current")
_StatCountersrxHCPkt512to1023Octets_Type = Counter64
_StatCountersrxHCPkt512to1023Octets_Object = MibTableColumn
statCountersrxHCPkt512to1023Octets = _StatCountersrxHCPkt512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 1, 1, 1, 20),
    _StatCountersrxHCPkt512to1023Octets_Type()
)
statCountersrxHCPkt512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statCountersrxHCPkt512to1023Octets.setStatus("current")
_StatCountersrxHCPkt1024to1518Octets_Type = Counter64
_StatCountersrxHCPkt1024to1518Octets_Object = MibTableColumn
statCountersrxHCPkt1024to1518Octets = _StatCountersrxHCPkt1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 1, 1, 1, 21),
    _StatCountersrxHCPkt1024to1518Octets_Type()
)
statCountersrxHCPkt1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statCountersrxHCPkt1024to1518Octets.setStatus("current")
_StatCountersrxHCPkt1519to2047Octets_Type = Counter64
_StatCountersrxHCPkt1519to2047Octets_Object = MibTableColumn
statCountersrxHCPkt1519to2047Octets = _StatCountersrxHCPkt1519to2047Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 1, 1, 1, 22),
    _StatCountersrxHCPkt1519to2047Octets_Type()
)
statCountersrxHCPkt1519to2047Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statCountersrxHCPkt1519to2047Octets.setStatus("current")
_StatCountersrxHCPkt2048to4095Octets_Type = Counter64
_StatCountersrxHCPkt2048to4095Octets_Object = MibTableColumn
statCountersrxHCPkt2048to4095Octets = _StatCountersrxHCPkt2048to4095Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 1, 1, 1, 23),
    _StatCountersrxHCPkt2048to4095Octets_Type()
)
statCountersrxHCPkt2048to4095Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statCountersrxHCPkt2048to4095Octets.setStatus("current")
_StatCountersrxHCPkt4096to9216Octets_Type = Counter64
_StatCountersrxHCPkt4096to9216Octets_Object = MibTableColumn
statCountersrxHCPkt4096to9216Octets = _StatCountersrxHCPkt4096to9216Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 1, 1, 1, 24),
    _StatCountersrxHCPkt4096to9216Octets_Type()
)
statCountersrxHCPkt4096to9216Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statCountersrxHCPkt4096to9216Octets.setStatus("current")
_StatCounterstxHCPkt64Octets_Type = Counter64
_StatCounterstxHCPkt64Octets_Object = MibTableColumn
statCounterstxHCPkt64Octets = _StatCounterstxHCPkt64Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 1, 1, 1, 25),
    _StatCounterstxHCPkt64Octets_Type()
)
statCounterstxHCPkt64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statCounterstxHCPkt64Octets.setStatus("current")
_StatCounterstxHCPkt65to127Octets_Type = Counter64
_StatCounterstxHCPkt65to127Octets_Object = MibTableColumn
statCounterstxHCPkt65to127Octets = _StatCounterstxHCPkt65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 1, 1, 1, 26),
    _StatCounterstxHCPkt65to127Octets_Type()
)
statCounterstxHCPkt65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statCounterstxHCPkt65to127Octets.setStatus("current")
_StatCounterstxHCPkt128to255Octets_Type = Counter64
_StatCounterstxHCPkt128to255Octets_Object = MibTableColumn
statCounterstxHCPkt128to255Octets = _StatCounterstxHCPkt128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 1, 1, 1, 27),
    _StatCounterstxHCPkt128to255Octets_Type()
)
statCounterstxHCPkt128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statCounterstxHCPkt128to255Octets.setStatus("current")
_StatCounterstxHCPkt256to511Octets_Type = Counter64
_StatCounterstxHCPkt256to511Octets_Object = MibTableColumn
statCounterstxHCPkt256to511Octets = _StatCounterstxHCPkt256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 1, 1, 1, 28),
    _StatCounterstxHCPkt256to511Octets_Type()
)
statCounterstxHCPkt256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statCounterstxHCPkt256to511Octets.setStatus("current")
_StatCounterstxHCPkt512to1023Octets_Type = Counter64
_StatCounterstxHCPkt512to1023Octets_Object = MibTableColumn
statCounterstxHCPkt512to1023Octets = _StatCounterstxHCPkt512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 1, 1, 1, 29),
    _StatCounterstxHCPkt512to1023Octets_Type()
)
statCounterstxHCPkt512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statCounterstxHCPkt512to1023Octets.setStatus("current")
_StatCounterstxHCPkt1024to1518Octets_Type = Counter64
_StatCounterstxHCPkt1024to1518Octets_Object = MibTableColumn
statCounterstxHCPkt1024to1518Octets = _StatCounterstxHCPkt1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 1, 1, 1, 30),
    _StatCounterstxHCPkt1024to1518Octets_Type()
)
statCounterstxHCPkt1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statCounterstxHCPkt1024to1518Octets.setStatus("current")
_StatCounterstxHCPkt1519to2047Octets_Type = Counter64
_StatCounterstxHCPkt1519to2047Octets_Object = MibTableColumn
statCounterstxHCPkt1519to2047Octets = _StatCounterstxHCPkt1519to2047Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 1, 1, 1, 31),
    _StatCounterstxHCPkt1519to2047Octets_Type()
)
statCounterstxHCPkt1519to2047Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statCounterstxHCPkt1519to2047Octets.setStatus("current")
_StatCounterstxHCPkt2048to4095Octets_Type = Counter64
_StatCounterstxHCPkt2048to4095Octets_Object = MibTableColumn
statCounterstxHCPkt2048to4095Octets = _StatCounterstxHCPkt2048to4095Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 1, 1, 1, 32),
    _StatCounterstxHCPkt2048to4095Octets_Type()
)
statCounterstxHCPkt2048to4095Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statCounterstxHCPkt2048to4095Octets.setStatus("current")
_StatCounterstxHCPkt4096to9216Octets_Type = Counter64
_StatCounterstxHCPkt4096to9216Octets_Object = MibTableColumn
statCounterstxHCPkt4096to9216Octets = _StatCounterstxHCPkt4096to9216Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 1, 1, 1, 33),
    _StatCounterstxHCPkt4096to9216Octets_Type()
)
statCounterstxHCPkt4096to9216Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statCounterstxHCPkt4096to9216Octets.setStatus("current")
_StatisticsErrorCounters_ObjectIdentity = ObjectIdentity
statisticsErrorCounters = _StatisticsErrorCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 2)
)
_StatisticsErrorTable_Object = MibTable
statisticsErrorTable = _StatisticsErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 2, 1)
)
if mibBuilder.loadTexts:
    statisticsErrorTable.setStatus("current")
_StatisticsErrorEntry_Object = MibTableRow
statisticsErrorEntry = _StatisticsErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 2, 1, 1)
)
statisticsErrorEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "statPortCountPort"),
)
if mibBuilder.loadTexts:
    statisticsErrorEntry.setStatus("current")
_StatPortCountPort_Type = InterfaceIndex
_StatPortCountPort_Object = MibTableColumn
statPortCountPort = _StatPortCountPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 2, 1, 1, 1),
    _StatPortCountPort_Type()
)
statPortCountPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPortCountPort.setStatus("current")
_StatCountersrxDroppkts_Type = Counter32
_StatCountersrxDroppkts_Object = MibTableColumn
statCountersrxDroppkts = _StatCountersrxDroppkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 2, 1, 1, 2),
    _StatCountersrxDroppkts_Type()
)
statCountersrxDroppkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statCountersrxDroppkts.setStatus("current")
_StatCountersrxMTUDropPkts_Type = Counter32
_StatCountersrxMTUDropPkts_Object = MibTableColumn
statCountersrxMTUDropPkts = _StatCountersrxMTUDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 2, 1, 1, 3),
    _StatCountersrxMTUDropPkts_Type()
)
statCountersrxMTUDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statCountersrxMTUDropPkts.setStatus("current")
_StatPortCountDeferredTx_Type = Counter32
_StatPortCountDeferredTx_Object = MibTableColumn
statPortCountDeferredTx = _StatPortCountDeferredTx_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 2, 1, 1, 4),
    _StatPortCountDeferredTx_Type()
)
statPortCountDeferredTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPortCountDeferredTx.setStatus("current")
_StatCountersdot3StatsSingleColFrames_Type = Counter32
_StatCountersdot3StatsSingleColFrames_Object = MibTableColumn
statCountersdot3StatsSingleColFrames = _StatCountersdot3StatsSingleColFrames_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 2, 1, 1, 5),
    _StatCountersdot3StatsSingleColFrames_Type()
)
statCountersdot3StatsSingleColFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statCountersdot3StatsSingleColFrames.setStatus("current")
_StatPortCountExcessCol_Type = Counter32
_StatPortCountExcessCol_Object = MibTableColumn
statPortCountExcessCol = _StatPortCountExcessCol_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 2, 1, 1, 6),
    _StatPortCountExcessCol_Type()
)
statPortCountExcessCol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPortCountExcessCol.setStatus("current")
_StatPortCountLateCol_Type = Counter32
_StatPortCountLateCol_Object = MibTableColumn
statPortCountLateCol = _StatPortCountLateCol_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 2, 1, 1, 7),
    _StatPortCountLateCol_Type()
)
statPortCountLateCol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPortCountLateCol.setStatus("current")
_StatPortCountAlignErr_Type = Counter32
_StatPortCountAlignErr_Object = MibTableColumn
statPortCountAlignErr = _StatPortCountAlignErr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 2, 1, 1, 8),
    _StatPortCountAlignErr_Type()
)
statPortCountAlignErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPortCountAlignErr.setStatus("current")
_StatPortCountFCSErr_Type = Counter32
_StatPortCountFCSErr_Object = MibTableColumn
statPortCountFCSErr = _StatPortCountFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 2, 1, 1, 9),
    _StatPortCountFCSErr_Type()
)
statPortCountFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPortCountFCSErr.setStatus("current")
_StatCountersifOutDiscards_Type = Counter32
_StatCountersifOutDiscards_Object = MibTableColumn
statCountersifOutDiscards = _StatCountersifOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 2, 1, 1, 10),
    _StatCountersifOutDiscards_Type()
)
statCountersifOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statCountersifOutDiscards.setStatus("current")
_StatPortCountMultiCol_Type = Counter32
_StatPortCountMultiCol_Object = MibTableColumn
statPortCountMultiCol = _StatPortCountMultiCol_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 2, 1, 1, 11),
    _StatPortCountMultiCol_Type()
)
statPortCountMultiCol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPortCountMultiCol.setStatus("current")
_StatPortCountCarriSen_Type = Counter32
_StatPortCountCarriSen_Object = MibTableColumn
statPortCountCarriSen = _StatPortCountCarriSen_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 2, 1, 1, 12),
    _StatPortCountCarriSen_Type()
)
statPortCountCarriSen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPortCountCarriSen.setStatus("current")
_StatPortCountSQETestErr_Type = Counter32
_StatPortCountSQETestErr_Object = MibTableColumn
statPortCountSQETestErr = _StatPortCountSQETestErr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 2, 1, 1, 13),
    _StatPortCountSQETestErr_Type()
)
statPortCountSQETestErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPortCountSQETestErr.setStatus("current")
_StatCountersdot3StatsDeferredTransmisions_Type = Counter32
_StatCountersdot3StatsDeferredTransmisions_Object = MibTableColumn
statCountersdot3StatsDeferredTransmisions = _StatCountersdot3StatsDeferredTransmisions_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 2, 1, 1, 14),
    _StatCountersdot3StatsDeferredTransmisions_Type()
)
statCountersdot3StatsDeferredTransmisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statCountersdot3StatsDeferredTransmisions.setStatus("current")
_StatPortCountIntMacTx_Type = Counter32
_StatPortCountIntMacTx_Object = MibTableColumn
statPortCountIntMacTx = _StatPortCountIntMacTx_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 2, 1, 1, 15),
    _StatPortCountIntMacTx_Type()
)
statPortCountIntMacTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPortCountIntMacTx.setStatus("current")
_StatPortCountIntMacRx_Type = Counter32
_StatPortCountIntMacRx_Object = MibTableColumn
statPortCountIntMacRx = _StatPortCountIntMacRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 2, 1, 1, 16),
    _StatPortCountIntMacRx_Type()
)
statPortCountIntMacRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPortCountIntMacRx.setStatus("current")
_StatCountersrxCRCAlignErrors_Type = Counter32
_StatCountersrxCRCAlignErrors_Object = MibTableColumn
statCountersrxCRCAlignErrors = _StatCountersrxCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 2, 1, 1, 17),
    _StatCountersrxCRCAlignErrors_Type()
)
statCountersrxCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statCountersrxCRCAlignErrors.setStatus("current")
_StatCountersrxUndersizedPkts_Type = Counter32
_StatCountersrxUndersizedPkts_Object = MibTableColumn
statCountersrxUndersizedPkts = _StatCountersrxUndersizedPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 2, 1, 1, 18),
    _StatCountersrxUndersizedPkts_Type()
)
statCountersrxUndersizedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statCountersrxUndersizedPkts.setStatus("current")
_StatCountersrxOversizedPkts_Type = Counter32
_StatCountersrxOversizedPkts_Object = MibTableColumn
statCountersrxOversizedPkts = _StatCountersrxOversizedPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 2, 1, 1, 19),
    _StatCountersrxOversizedPkts_Type()
)
statCountersrxOversizedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statCountersrxOversizedPkts.setStatus("current")
_StatCountersrxFragmentPkts_Type = Counter32
_StatCountersrxFragmentPkts_Object = MibTableColumn
statCountersrxFragmentPkts = _StatCountersrxFragmentPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 2, 1, 1, 20),
    _StatCountersrxFragmentPkts_Type()
)
statCountersrxFragmentPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statCountersrxFragmentPkts.setStatus("current")
_StatCountersrxJabbers_Type = Counter32
_StatCountersrxJabbers_Object = MibTableColumn
statCountersrxJabbers = _StatCountersrxJabbers_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 2, 1, 1, 21),
    _StatCountersrxJabbers_Type()
)
statCountersrxJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statCountersrxJabbers.setStatus("current")
_StatCountersrxSymbolErrors_Type = Counter32
_StatCountersrxSymbolErrors_Object = MibTableColumn
statCountersrxSymbolErrors = _StatCountersrxSymbolErrors_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 2, 1, 1, 22),
    _StatCountersrxSymbolErrors_Type()
)
statCountersrxSymbolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statCountersrxSymbolErrors.setStatus("current")
_StatCountersrxMulticastDropPkts_Type = Counter32
_StatCountersrxMulticastDropPkts_Object = MibTableColumn
statCountersrxMulticastDropPkts = _StatCountersrxMulticastDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 2, 1, 1, 23),
    _StatCountersrxMulticastDropPkts_Type()
)
statCountersrxMulticastDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statCountersrxMulticastDropPkts.setStatus("current")
_StatCountersifInErrors_Type = Counter32
_StatCountersifInErrors_Object = MibTableColumn
statCountersifInErrors = _StatCountersifInErrors_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 2, 1, 1, 24),
    _StatCountersifInErrors_Type()
)
statCountersifInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statCountersifInErrors.setStatus("current")
_StatCountersifOutErrors_Type = Counter32
_StatCountersifOutErrors_Object = MibTableColumn
statCountersifOutErrors = _StatCountersifOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 2, 1, 1, 25),
    _StatCountersifOutErrors_Type()
)
statCountersifOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statCountersifOutErrors.setStatus("current")
_StatCountersifInDiscards_Type = Counter32
_StatCountersifInDiscards_Object = MibTableColumn
statCountersifInDiscards = _StatCountersifInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 2, 1, 1, 26),
    _StatCountersifInDiscards_Type()
)
statCountersifInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statCountersifInDiscards.setStatus("current")
_StatCountersifInUnknownProtos_Type = Counter32
_StatCountersifInUnknownProtos_Object = MibTableColumn
statCountersifInUnknownProtos = _StatCountersifInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 2, 1, 1, 27),
    _StatCountersifInUnknownProtos_Type()
)
statCountersifInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statCountersifInUnknownProtos.setStatus("current")
_StatCounterstxDelayExceededDiscards_Type = Counter32
_StatCounterstxDelayExceededDiscards_Object = MibTableColumn
statCounterstxDelayExceededDiscards = _StatCounterstxDelayExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 2, 1, 1, 28),
    _StatCounterstxDelayExceededDiscards_Type()
)
statCounterstxDelayExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statCounterstxDelayExceededDiscards.setStatus("current")
_StatisticsClear_ObjectIdentity = ObjectIdentity
statisticsClear = _StatisticsClear_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 3)
)
_StatisticsCounterClearTable_Object = MibTable
statisticsCounterClearTable = _StatisticsCounterClearTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 3, 1)
)
if mibBuilder.loadTexts:
    statisticsCounterClearTable.setStatus("current")
_StatisticsCounterClearEntry_Object = MibTableRow
statisticsCounterClearEntry = _StatisticsCounterClearEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 3, 1, 1)
)
statisticsCounterClearEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "statCounterClearIndex"),
)
if mibBuilder.loadTexts:
    statisticsCounterClearEntry.setStatus("current")
_StatCounterClearIndex_Type = Integer32
_StatCounterClearIndex_Object = MibTableColumn
statCounterClearIndex = _StatCounterClearIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 3, 1, 1, 1),
    _StatCounterClearIndex_Type()
)
statCounterClearIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statCounterClearIndex.setStatus("current")


class _StatCounterClearStatus_Type(Integer32):
    """Custom type statCounterClearStatus based on Integer32"""
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


_StatCounterClearStatus_Type.__name__ = "Integer32"
_StatCounterClearStatus_Object = MibTableColumn
statCounterClearStatus = _StatCounterClearStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 3, 1, 1, 2),
    _StatCounterClearStatus_Type()
)
statCounterClearStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statCounterClearStatus.setStatus("current")
_StatCounterLinkChange_Type = Integer32
_StatCounterLinkChange_Object = MibTableColumn
statCounterLinkChange = _StatCounterLinkChange_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 2, 3, 1, 1, 3),
    _StatCounterLinkChange_Type()
)
statCounterLinkChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statCounterLinkChange.setStatus("current")
_MonMirrorGroup_ObjectIdentity = ObjectIdentity
monMirrorGroup = _MonMirrorGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 3)
)
_MirrorSessionTable_Object = MibTable
mirrorSessionTable = _MirrorSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 3, 1)
)
if mibBuilder.loadTexts:
    mirrorSessionTable.setStatus("current")
_MirrorSessionEntry_Object = MibTableRow
mirrorSessionEntry = _MirrorSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 3, 1, 1)
)
mirrorSessionEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "mirrorSessionNumber"),
)
if mibBuilder.loadTexts:
    mirrorSessionEntry.setStatus("current")


class _MirrorSessionNumber_Type(Integer32):
    """Custom type mirrorSessionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_MirrorSessionNumber_Type.__name__ = "Integer32"
_MirrorSessionNumber_Object = MibTableColumn
mirrorSessionNumber = _MirrorSessionNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 3, 1, 1, 1),
    _MirrorSessionNumber_Type()
)
mirrorSessionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mirrorSessionNumber.setStatus("current")


class _MirrorDestinationPort_Type(Integer32):
    """Custom type mirrorDestinationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_MirrorDestinationPort_Type.__name__ = "Integer32"
_MirrorDestinationPort_Object = MibTableColumn
mirrorDestinationPort = _MirrorDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 3, 1, 1, 2),
    _MirrorDestinationPort_Type()
)
mirrorDestinationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrorDestinationPort.setStatus("current")
_MirrorSourceIngressPort_Type = PortList
_MirrorSourceIngressPort_Object = MibTableColumn
mirrorSourceIngressPort = _MirrorSourceIngressPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 3, 1, 1, 3),
    _MirrorSourceIngressPort_Type()
)
mirrorSourceIngressPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrorSourceIngressPort.setStatus("current")
_MirrorSourceEgressPort_Type = PortList
_MirrorSourceEgressPort_Object = MibTableColumn
mirrorSourceEgressPort = _MirrorSourceEgressPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 3, 1, 1, 4),
    _MirrorSourceEgressPort_Type()
)
mirrorSourceEgressPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrorSourceEgressPort.setStatus("current")
_MirrorSessionRowStatus_Type = RowStatus
_MirrorSessionRowStatus_Object = MibTableColumn
mirrorSessionRowStatus = _MirrorSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 10, 3, 1, 1, 5),
    _MirrorSessionRowStatus_Type()
)
mirrorSessionRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrorSessionRowStatus.setStatus("current")
_DlinkGreen_ObjectIdentity = ObjectIdentity
dlinkGreen = _DlinkGreen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 11)
)
_DlinkPowersavingGroup_ObjectIdentity = ObjectIdentity
dlinkPowersavingGroup = _DlinkPowersavingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 11, 1)
)
_PowerSavingGlobalSettings_ObjectIdentity = ObjectIdentity
powerSavingGlobalSettings = _PowerSavingGlobalSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 11, 1, 1)
)


class _PsgFunctionVersion_Type(DisplayString):
    """Custom type psgFunctionVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_PsgFunctionVersion_Type.__name__ = "DisplayString"
_PsgFunctionVersion_Object = MibScalar
psgFunctionVersion = _PsgFunctionVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 11, 1, 1, 1),
    _PsgFunctionVersion_Type()
)
psgFunctionVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psgFunctionVersion.setStatus("current")


class _PsgScheduledPortShutdown_Type(Integer32):
    """Custom type psgScheduledPortShutdown based on Integer32"""
    defaultValue = 2

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


_PsgScheduledPortShutdown_Type.__name__ = "Integer32"
_PsgScheduledPortShutdown_Object = MibScalar
psgScheduledPortShutdown = _PsgScheduledPortShutdown_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 11, 1, 1, 2),
    _PsgScheduledPortShutdown_Type()
)
psgScheduledPortShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psgScheduledPortShutdown.setStatus("current")


class _PsgScheduledHibernation_Type(Integer32):
    """Custom type psgScheduledHibernation based on Integer32"""
    defaultValue = 2

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


_PsgScheduledHibernation_Type.__name__ = "Integer32"
_PsgScheduledHibernation_Object = MibScalar
psgScheduledHibernation = _PsgScheduledHibernation_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 11, 1, 1, 3),
    _PsgScheduledHibernation_Type()
)
psgScheduledHibernation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psgScheduledHibernation.setStatus("current")


class _PsgScheduledDimLED_Type(Integer32):
    """Custom type psgScheduledDimLED based on Integer32"""
    defaultValue = 2

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


_PsgScheduledDimLED_Type.__name__ = "Integer32"
_PsgScheduledDimLED_Object = MibScalar
psgScheduledDimLED = _PsgScheduledDimLED_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 11, 1, 1, 4),
    _PsgScheduledDimLED_Type()
)
psgScheduledDimLED.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psgScheduledDimLED.setStatus("current")


class _PsgAdministrativeDimLED_Type(Integer32):
    """Custom type psgAdministrativeDimLED based on Integer32"""
    defaultValue = 2

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


_PsgAdministrativeDimLED_Type.__name__ = "Integer32"
_PsgAdministrativeDimLED_Object = MibScalar
psgAdministrativeDimLED = _PsgAdministrativeDimLED_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 11, 1, 1, 5),
    _PsgAdministrativeDimLED_Type()
)
psgAdministrativeDimLED.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psgAdministrativeDimLED.setStatus("current")
_PowerSavingTimeRangeSettings_ObjectIdentity = ObjectIdentity
powerSavingTimeRangeSettings = _PowerSavingTimeRangeSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 11, 1, 2)
)


class _PsgDimLEDShutOffTimeProfile_Type(DisplayString):
    """Custom type psgDimLEDShutOffTimeProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_PsgDimLEDShutOffTimeProfile_Type.__name__ = "DisplayString"
_PsgDimLEDShutOffTimeProfile_Object = MibScalar
psgDimLEDShutOffTimeProfile = _PsgDimLEDShutOffTimeProfile_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 11, 1, 2, 1),
    _PsgDimLEDShutOffTimeProfile_Type()
)
psgDimLEDShutOffTimeProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psgDimLEDShutOffTimeProfile.setStatus("current")


class _PsgHibernationTimeProfile_Type(DisplayString):
    """Custom type psgHibernationTimeProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_PsgHibernationTimeProfile_Type.__name__ = "DisplayString"
_PsgHibernationTimeProfile_Object = MibScalar
psgHibernationTimeProfile = _PsgHibernationTimeProfile_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 11, 1, 2, 2),
    _PsgHibernationTimeProfile_Type()
)
psgHibernationTimeProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psgHibernationTimeProfile.setStatus("current")
_PowerSavingShutdownSettings_ObjectIdentity = ObjectIdentity
powerSavingShutdownSettings = _PowerSavingShutdownSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 11, 1, 3)
)
_PowerSavingShutdownTable_Object = MibTable
powerSavingShutdownTable = _PowerSavingShutdownTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 11, 1, 3, 1)
)
if mibBuilder.loadTexts:
    powerSavingShutdownTable.setStatus("current")
_PowerSavingShutdownEntry_Object = MibTableRow
powerSavingShutdownEntry = _PowerSavingShutdownEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 11, 1, 3, 1, 1)
)
powerSavingShutdownEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "psShutdownPort"),
)
if mibBuilder.loadTexts:
    powerSavingShutdownEntry.setStatus("current")
_PsShutdownPort_Type = Integer32
_PsShutdownPort_Object = MibTableColumn
psShutdownPort = _PsShutdownPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 11, 1, 3, 1, 1, 1),
    _PsShutdownPort_Type()
)
psShutdownPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psShutdownPort.setStatus("current")


class _PsShutdownTimeRange_Type(DisplayString):
    """Custom type psShutdownTimeRange based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_PsShutdownTimeRange_Type.__name__ = "DisplayString"
_PsShutdownTimeRange_Object = MibTableColumn
psShutdownTimeRange = _PsShutdownTimeRange_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 11, 1, 3, 1, 1, 2),
    _PsShutdownTimeRange_Type()
)
psShutdownTimeRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psShutdownTimeRange.setStatus("current")
_DlinkEEEGroup_ObjectIdentity = ObjectIdentity
dlinkEEEGroup = _DlinkEEEGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 11, 2)
)
_GreenEeeTable_Object = MibTable
greenEeeTable = _GreenEeeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 11, 2, 1)
)
if mibBuilder.loadTexts:
    greenEeeTable.setStatus("current")
_GreenEeeEntry_Object = MibTableRow
greenEeeEntry = _GreenEeeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 11, 2, 1, 1)
)
greenEeeEntry.setIndexNames(
    (0, "DLINK-DXS-1210-12TC-AX-MIB", "eeePort"),
)
if mibBuilder.loadTexts:
    greenEeeEntry.setStatus("current")
_EeePort_Type = Integer32
_EeePort_Object = MibTableColumn
eeePort = _EeePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 11, 2, 1, 1, 1),
    _EeePort_Type()
)
eeePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eeePort.setStatus("current")


class _Eeestate_Type(Integer32):
    """Custom type eeestate based on Integer32"""
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


_Eeestate_Type.__name__ = "Integer32"
_Eeestate_Object = MibTableColumn
eeestate = _Eeestate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 11, 2, 1, 1, 2),
    _Eeestate_Type()
)
eeestate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eeestate.setStatus("current")

# Managed Objects groups


# Notification objects

errDisNotifyPortDisabledAssert = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 8, 0, 1)
)
if mibBuilder.loadTexts:
    errDisNotifyPortDisabledAssert.setStatus(
        "current"
    )

errDisNotifyPortDisabledClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 8, 0, 2)
)
if mibBuilder.loadTexts:
    errDisNotifyPortDisabledClear.setStatus(
        "current"
    )

errDisNotifyVlanDisabledAssert = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 8, 0, 3)
)
if mibBuilder.loadTexts:
    errDisNotifyVlanDisabledAssert.setStatus(
        "current"
    )

errDisNotifyVlanDisabledClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 2, 13, 8, 0, 4)
)
if mibBuilder.loadTexts:
    errDisNotifyVlanDisabledClear.setStatus(
        "current"
    )

stpNewRootTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 6, 0, 1)
)
if mibBuilder.loadTexts:
    stpNewRootTrap.setStatus(
        "current"
    )

stpTopologyChgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 3, 6, 0, 2)
)
if mibBuilder.loadTexts:
    stpTopologyChgTrap.setStatus(
        "current"
    )

lbdLoopOccur = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 4, 4, 0, 1)
)
if mibBuilder.loadTexts:
    lbdLoopOccur.setStatus(
        "current"
    )

lbdLoopRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 4, 4, 0, 2)
)
if mibBuilder.loadTexts:
    lbdLoopRecover.setStatus(
        "current"
    )

lldpXMedTopologyChangeDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 4, 7, 18, 1)
)
lldpXMedTopologyChangeDetected.setObjects(
      *(("DLINK-DXS-1210-12TC-AX-MIB", "lldpRemChassisIdSubtype"),
        ("DLINK-DXS-1210-12TC-AX-MIB", "lldpRemChassisId"))
)
if mibBuilder.loadTexts:
    lldpXMedTopologyChangeDetected.setStatus(
        "current"
    )

portSecurityViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 1, 4, 0, 1)
)
portSecurityViolation.setObjects(
      *(("DLINK-DXS-1210-12TC-AX-MIB", "portSecurityPort"),
        ("DLINK-DXS-1210-12TC-AX-MIB", "portSecurityVioCount"))
)
if mibBuilder.loadTexts:
    portSecurityViolation.setStatus(
        "current"
    )

dhcpSerScrAttackDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 7, 3, 0, 1)
)
if mibBuilder.loadTexts:
    dhcpSerScrAttackDetect.setStatus(
        "current"
    )

stormCtrlTrapsStormOccur = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 16, 1, 1, 6, 0, 1)
)
if mibBuilder.loadTexts:
    stormCtrlTrapsStormOccur.setStatus(
        "current"
    )

stormCtrlTrapsStormClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 139, 1, 1, 8, 16, 1, 1, 6, 0, 2)
)
if mibBuilder.loadTexts:
    stormCtrlTrapsStormClear.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINK-DXS-1210-12TC-AX-MIB",
    **{"VlanIndex": VlanIndex,
       "PortList": PortList,
       "VlanList": VlanList,
       "BridgeId": BridgeId,
       "Timeout": Timeout,
       "OwnerString": OwnerString,
       "RmonStatus": RmonStatus,
       "OperationResponseStatus": OperationResponseStatus,
       "LldpChassisIdSubtype": LldpChassisIdSubtype,
       "LldpChassisId": LldpChassisId,
       "LldpPortIdSubtype": LldpPortIdSubtype,
       "LldpPortId": LldpPortId,
       "LldpManAddrIfSubtype": LldpManAddrIfSubtype,
       "LldpManAddress": LldpManAddress,
       "LldpSystemCapabilitiesMap": LldpSystemCapabilitiesMap,
       "LldpPortNumber": LldpPortNumber,
       "LldpPortList": LldpPortList,
       "TimeFilter": TimeFilter,
       "LldpPowerPortClass": LldpPowerPortClass,
       "LldpLinkAggStatusMap": LldpLinkAggStatusMap,
       "ZeroBasedCounter32": ZeroBasedCounter32,
       "Ipv6Address": Ipv6Address,
       "InetAddressPrefixLength": InetAddressPrefixLength,
       "DStormCtlTrafficType": DStormCtlTrafficType,
       "DStormCtlThrType": DStormCtlThrType,
       "DStormCtlThrTypeValue": DStormCtlThrTypeValue,
       "VlanIdOrNone": VlanIdOrNone,
       "LldpXMedDeviceClass": LldpXMedDeviceClass,
       "LldpXMedCapabilities": LldpXMedCapabilities,
       "PolicyAppType": PolicyAppType,
       "d-link": d_link,
       "dlink-products": dlink_products,
       "dlink-DXS1210SeriesProd": dlink_DXS1210SeriesProd,
       "dxs-1210-12tc": dxs_1210_12tc,
       "dxs-1210-12tc-AX": dxs_1210_12tc_AX,
       "dlinkDeviceInfo": dlinkDeviceInfo,
       "deviceInfoGroup": deviceInfoGroup,
       "deviceInformation": deviceInformation,
       "deviceInfoDeviceType": deviceInfoDeviceType,
       "deviceInfoBootPROMVersion": deviceInfoBootPROMVersion,
       "deviceInfoFirmwareVersion": deviceInfoFirmwareVersion,
       "deviceInfoHardwareVersion": deviceInfoHardwareVersion,
       "deviceInfoMACAddress": deviceInfoMACAddress,
       "deviceInfoSystemTime": deviceInfoSystemTime,
       "deviceInfoSerialNumber": deviceInfoSerialNumber,
       "deviceSwitchCPULast5SecUsage": deviceSwitchCPULast5SecUsage,
       "deviceFunction": deviceFunction,
       "firmwareInformationTable": firmwareInformationTable,
       "firmwareInformationEntry": firmwareInformationEntry,
       "firmwareInfoImageID": firmwareInfoImageID,
       "firmwareInfoVersion": firmwareInfoVersion,
       "firmwareInfoSizeB": firmwareInfoSizeB,
       "firmwareInfoUpdateTime": firmwareInfoUpdateTime,
       "devFunFwUpgradeAndBackup": devFunFwUpgradeAndBackup,
       "devFunFwServerIpAddrType": devFunFwServerIpAddrType,
       "devFunFwServerIpvxAddr": devFunFwServerIpvxAddr,
       "devFunFwServerInterfaceName": devFunFwServerInterfaceName,
       "devFunFwSrcFilename": devFunFwSrcFilename,
       "devFunFwOperation": devFunFwOperation,
       "devFunFwOperationStatus": devFunFwOperationStatus,
       "devFunFwTransferPercentage": devFunFwTransferPercentage,
       "devFunFwRetryCount": devFunFwRetryCount,
       "devFunFwServerStatus": devFunFwServerStatus,
       "devFwOperationImageId": devFwOperationImageId,
       "devFwNextBootImageId": devFwNextBootImageId,
       "devFwActualBootImageId": devFwActualBootImageId,
       "devFunConfigInfo": devFunConfigInfo,
       "devFunCfgInfoTable": devFunCfgInfoTable,
       "devFunCfgInfoEntry": devFunCfgInfoEntry,
       "devFunCfgId": devFunCfgId,
       "devFunCfgSize": devFunCfgSize,
       "devFunCfgUpdateTime": devFunCfgUpdateTime,
       "devFunConfiguration": devFunConfiguration,
       "devFunCfgServerIpAddrType": devFunCfgServerIpAddrType,
       "devFunCfgServerIpvxAddr": devFunCfgServerIpvxAddr,
       "devFunCfgSrcFilename": devFunCfgSrcFilename,
       "devFunCfgStartUpConfigID": devFunCfgStartUpConfigID,
       "devFunCfgOperConfigID": devFunCfgOperConfigID,
       "devFunCfgOperation": devFunCfgOperation,
       "devFunCfgSave": devFunCfgSave,
       "devFunCfgOperationStatus": devFunCfgOperationStatus,
       "devFunCfgTransferPercentage": devFunCfgTransferPercentage,
       "devFunCfgServerInterfaceName": devFunCfgServerInterfaceName,
       "devFunCfgServerStatus": devFunCfgServerStatus,
       "devFunCfgCurrStartUpConfigID": devFunCfgCurrStartUpConfigID,
       "devFunLogBackup": devFunLogBackup,
       "devFunLogBackupToTftpIpType": devFunLogBackupToTftpIpType,
       "devFunLogBackupToTftpIpAddr": devFunLogBackupToTftpIpAddr,
       "devFunLogBackupToTftpDestURL": devFunLogBackupToTftpDestURL,
       "devFunLogBackupToTftpOper": devFunLogBackupToTftpOper,
       "devFunLogBackupToTftStatus": devFunLogBackupToTftStatus,
       "devFunPing": devFunPing,
       "devPingDestIpType": devPingDestIpType,
       "devPingDestIpAddr": devPingDestIpAddr,
       "devPingTimeout": devPingTimeout,
       "devPingTimes": devPingTimes,
       "devPingStart": devPingStart,
       "devPingStatus": devPingStatus,
       "devPingSuccesses": devPingSuccesses,
       "devPingV4ProbeHistoryTable": devPingV4ProbeHistoryTable,
       "devPingV4ProbeHistoryEntry": devPingV4ProbeHistoryEntry,
       "devPingIndex": devPingIndex,
       "devPingProbeIndex": devPingProbeIndex,
       "devPingProbeHistoryResponseTime": devPingProbeHistoryResponseTime,
       "devIpv6PingProbeHistoryTable": devIpv6PingProbeHistoryTable,
       "devIpv6PingProbeHistoryEntry": devIpv6PingProbeHistoryEntry,
       "devIpv6PingIndex": devIpv6PingIndex,
       "devIpv6PingProbeIndex": devIpv6PingProbeIndex,
       "devIpv6PingProbeHistoryResponseTime": devIpv6PingProbeHistoryResponseTime,
       "devFunLangMgmt": devFunLangMgmt,
       "devFunLangMgmtFile": devFunLangMgmtFile,
       "devFunLangMgmtApply": devFunLangMgmtApply,
       "devFunRestart": devFunRestart,
       "devFunWizardIgnoreNextTime": devFunWizardIgnoreNextTime,
       "deviceErrorCodeInformation": deviceErrorCodeInformation,
       "deviceErrorCodeTable": deviceErrorCodeTable,
       "deviceErrorCodeEntry": deviceErrorCodeEntry,
       "devErrorCodeIndex": devErrorCodeIndex,
       "devErrorString": devErrorString,
       "deviceFan": deviceFan,
       "deviceFanStatus": deviceFanStatus,
       "dlinkSystem": dlinkSystem,
       "sysInformationGroup": sysInformationGroup,
       "systemName": systemName,
       "systemLocation": systemLocation,
       "systemContact": systemContact,
       "syslogGroup": syslogGroup,
       "syslogMIBObjects": syslogMIBObjects,
       "syslogGeneral": syslogGeneral,
       "syslogSourceInterfaceState": syslogSourceInterfaceState,
       "syslogSourceInterfaceVID": syslogSourceInterfaceVID,
       "syslogLogbuffer": syslogLogbuffer,
       "syslogClearLogBuffer": syslogClearLogBuffer,
       "syslogLogBufferEnabled": syslogLogBufferEnabled,
       "syslogLogBufSeverity": syslogLogBufSeverity,
       "syslogLogBufWriteDelay": syslogLogBufWriteDelay,
       "syslogServerTable": syslogServerTable,
       "syslogServerEntry": syslogServerEntry,
       "syslogServerIndex": syslogServerIndex,
       "syslogServerAddressType": syslogServerAddressType,
       "syslogServerAddress": syslogServerAddress,
       "syslogServerPort": syslogServerPort,
       "syslogServerSeverity": syslogServerSeverity,
       "syslogServerFacility": syslogServerFacility,
       "syslogServerRowstatus": syslogServerRowstatus,
       "syslogBufferTableNum": syslogBufferTableNum,
       "syslogBufferTable": syslogBufferTable,
       "syslogBufferEntry": syslogBufferEntry,
       "syslogBufferIndex": syslogBufferIndex,
       "syslogBufferDateAndTime": syslogBufferDateAndTime,
       "syslogBufferDescription": syslogBufferDescription,
       "syslogBufferSeverity": syslogBufferSeverity,
       "sysPortConfigGroup": sysPortConfigGroup,
       "portCtrlTable": portCtrlTable,
       "portCtrlEntry": portCtrlEntry,
       "portSetIndex": portSetIndex,
       "portSetMediaType": portSetMediaType,
       "portSetState": portSetState,
       "portSetAutoDowngrade": portSetAutoDowngrade,
       "portSetFlowControl": portSetFlowControl,
       "portSetDuplex": portSetDuplex,
       "portSetSpeed": portSetSpeed,
       "portSetCapaAdvertised": portSetCapaAdvertised,
       "portSetDescription": portSetDescription,
       "portSetLinkStatus": portSetLinkStatus,
       "portStatusTable": portStatusTable,
       "portStatusEntry": portStatusEntry,
       "portStaIndex": portStaIndex,
       "portStaMediaType": portStaMediaType,
       "portStaStatus": portStaStatus,
       "portStaMacAddr": portStaMacAddr,
       "portStaVlan": portStaVlan,
       "portStaFlowCtrlOpSend": portStaFlowCtrlOpSend,
       "portStaFlowCtrlOpRece": portStaFlowCtrlOpRece,
       "portStaDuplex": portStaDuplex,
       "portStaSpeed": portStaSpeed,
       "errDisAssertTrapState": errDisAssertTrapState,
       "errDisClearTrapState": errDisClearTrapState,
       "errDisNotificationRate": errDisNotificationRate,
       "errDisIfStatusTable": errDisIfStatusTable,
       "errDisIfStatusEntry": errDisIfStatusEntry,
       "errDisIfStatusPortIndex": errDisIfStatusPortIndex,
       "errDisIfStatusVlanIndex": errDisIfStatusVlanIndex,
       "errDisPortState": errDisPortState,
       "errDisPortConnectStatus": errDisPortConnectStatus,
       "errDisPortReason": errDisPortReason,
       "errDisPortRecoveryTimeLeft": errDisPortRecoveryTimeLeft,
       "errDisRecoveryTable": errDisRecoveryTable,
       "errDisRecoveryEntry": errDisRecoveryEntry,
       "errDisRecoveryReason": errDisRecoveryReason,
       "errDisRecoveryStatus": errDisRecoveryStatus,
       "errDisRecoveryInterval": errDisRecoveryInterval,
       "errDisTraps": errDisTraps,
       "errDisTrapsList": errDisTrapsList,
       "errDisNotifyPortDisabledAssert": errDisNotifyPortDisabledAssert,
       "errDisNotifyPortDisabledClear": errDisNotifyPortDisabledClear,
       "errDisNotifyVlanDisabledAssert": errDisNotifyVlanDisabledAssert,
       "errDisNotifyVlanDisabledClear": errDisNotifyVlanDisabledClear,
       "jumboFrameTable": jumboFrameTable,
       "jumboFrameEntry": jumboFrameEntry,
       "portIndex": portIndex,
       "maxReceFrameSize": maxReceFrameSize,
       "sysSNTPSettingGroup": sysSNTPSettingGroup,
       "sntpClockSettings": sntpClockSettings,
       "sntpTimeSeconds": sntpTimeSeconds,
       "sntpTimeZoneSettings": sntpTimeZoneSettings,
       "sntpSummerTimeState": sntpSummerTimeState,
       "sntpGMTMinutes": sntpGMTMinutes,
       "sntpSummerTimeStart": sntpSummerTimeStart,
       "sntpSummerTimeEnd": sntpSummerTimeEnd,
       "sntpSummerTimeOffset": sntpSummerTimeOffset,
       "sntpSNTPSettings": sntpSNTPSettings,
       "sntpGlobalState": sntpGlobalState,
       "sntpPollInterval": sntpPollInterval,
       "sntpServerTable": sntpServerTable,
       "sntpServerEntry": sntpServerEntry,
       "sntpServerAddrType": sntpServerAddrType,
       "sntpServerAddr": sntpServerAddr,
       "sntpServerStratum": sntpServerStratum,
       "sntpServerVersion": sntpServerVersion,
       "sntpServerLastReceive": sntpServerLastReceive,
       "sntpServerSynced": sntpServerSynced,
       "sntpServerRowStatus": sntpServerRowStatus,
       "sysTimeRangeGroup": sysTimeRangeGroup,
       "timeRangeTable": timeRangeTable,
       "timeRangeEntry": timeRangeEntry,
       "timeRangeName": timeRangeName,
       "timeRangeIndex": timeRangeIndex,
       "timeRangeStartHour": timeRangeStartHour,
       "timeRangeStartMinute": timeRangeStartMinute,
       "timeRangeEndHour": timeRangeEndHour,
       "timeRangeEndMinute": timeRangeEndMinute,
       "timeRangeWeekday": timeRangeWeekday,
       "timeRangeRowStatus": timeRangeRowStatus,
       "dlinkManagement": dlinkManagement,
       "mgtUserAccountGroup": mgtUserAccountGroup,
       "userAccountsManagementSettings": userAccountsManagementSettings,
       "userAccountsTable": userAccountsTable,
       "userAccountsEntry": userAccountsEntry,
       "userName": userName,
       "userPrivilege": userPrivilege,
       "userEncryptControl": userEncryptControl,
       "userPassword": userPassword,
       "userRowStatus": userRowStatus,
       "userAccountsSessionTable": userAccountsSessionTable,
       "userSessionTableEntry": userSessionTableEntry,
       "userSessionEntry": userSessionEntry,
       "sessionID": sessionID,
       "liveTime": liveTime,
       "loginType": loginType,
       "loginIP": loginIP,
       "loginUserLevel": loginUserLevel,
       "loginUserName": loginUserName,
       "mgtPasswordEncryptionGroup": mgtPasswordEncryptionGroup,
       "passwordEncryptionStatus": passwordEncryptionStatus,
       "mgtSnmpGroup": mgtSnmpGroup,
       "snmpGlobalSettings": snmpGlobalSettings,
       "snmpGlobalState": snmpGlobalState,
       "snmpResBroadReq": snmpResBroadReq,
       "snmpUDPPort": snmpUDPPort,
       "snmpTrapSourceInterface": snmpTrapSourceInterface,
       "snmpTrapGlobalState": snmpTrapGlobalState,
       "snmpTrapSNMPAuthTrap": snmpTrapSNMPAuthTrap,
       "snmpTrapPortLinkUp": snmpTrapPortLinkUp,
       "snmpTrapPortLinkDown": snmpTrapPortLinkDown,
       "snmpTrapColdstart": snmpTrapColdstart,
       "snmpTrapWarmstart": snmpTrapWarmstart,
       "snmpView": snmpView,
       "snmpViewTable": snmpViewTable,
       "snmpViewEntry": snmpViewEntry,
       "snmpViewName": snmpViewName,
       "snmpViewSubtree": snmpViewSubtree,
       "snmpViewType": snmpViewType,
       "snmpViewStatus": snmpViewStatus,
       "snmpCommunity": snmpCommunity,
       "snmpCommunityTable": snmpCommunityTable,
       "snmpCommunityEntry": snmpCommunityEntry,
       "snmpCommName": snmpCommName,
       "snmpCommKeyType": snmpCommKeyType,
       "snmpCommViewName": snmpCommViewName,
       "snmpCommAccessRight": snmpCommAccessRight,
       "snmpCommIPAccListName": snmpCommIPAccListName,
       "snmpCommStatus": snmpCommStatus,
       "snmpGroup": snmpGroup,
       "snmpGroupTable": snmpGroupTable,
       "snmpGroupEntry": snmpGroupEntry,
       "snmpGroupName": snmpGroupName,
       "snmpGroupSecurityModel": snmpGroupSecurityModel,
       "snmpGroupSecurityLevel": snmpGroupSecurityLevel,
       "snmpGroupReadViewName": snmpGroupReadViewName,
       "snmpGroupWriteViewName": snmpGroupWriteViewName,
       "snmpGroupNotifyViewName": snmpGroupNotifyViewName,
       "snmpGroupIpListName": snmpGroupIpListName,
       "snmpGroupStatus": snmpGroupStatus,
       "snmpEngineID": snmpEngineID,
       "snmpUser": snmpUser,
       "snmpUserTable": snmpUserTable,
       "snmpUserEntry": snmpUserEntry,
       "snmpUserName": snmpUserName,
       "snmpUserVersion": snmpUserVersion,
       "snmpUserGroupName": snmpUserGroupName,
       "snmpUserV3Encrypt": snmpUserV3Encrypt,
       "snmpUserAuthProtocol": snmpUserAuthProtocol,
       "snmpUserAuthProtocolPassword": snmpUserAuthProtocolPassword,
       "snmpUserPrivProtocol": snmpUserPrivProtocol,
       "snmpUserPrivProtocolPassword": snmpUserPrivProtocolPassword,
       "snmpUserAuthProtoByKey": snmpUserAuthProtoByKey,
       "snmpUserAuthProtoKey": snmpUserAuthProtoKey,
       "snmpUserPrivProtoByKey": snmpUserPrivProtoByKey,
       "snmpUserPrivProtoKey": snmpUserPrivProtoKey,
       "snmpUserIpListName": snmpUserIpListName,
       "snmpUserStatus": snmpUserStatus,
       "snmpHost": snmpHost,
       "snmpHostTable": snmpHostTable,
       "snmpHostEntry": snmpHostEntry,
       "snmpHostAddress": snmpHostAddress,
       "snmpHostIPType": snmpHostIPType,
       "snmpHostVersion": snmpHostVersion,
       "snmpHostUDPPort": snmpHostUDPPort,
       "snmpHostCommunityName": snmpHostCommunityName,
       "snmpHostStatus": snmpHostStatus,
       "mgtRMONGroup": mgtRMONGroup,
       "rmonRisingAlarmTrapState": rmonRisingAlarmTrapState,
       "rmonFallingAlarmTrapState": rmonFallingAlarmTrapState,
       "rmonStatistics": rmonStatistics,
       "rmonStatsTable": rmonStatsTable,
       "rmonStatsEntry": rmonStatsEntry,
       "rmonStatsIndex": rmonStatsIndex,
       "rmonStatsDataSource": rmonStatsDataSource,
       "rmonStatsOwner": rmonStatsOwner,
       "rmonStatsOctets": rmonStatsOctets,
       "rmonStatsPkts": rmonStatsPkts,
       "rmonStatsBroadcastPkts": rmonStatsBroadcastPkts,
       "rmonStatsMulticastPkts": rmonStatsMulticastPkts,
       "rmonStatsUndersizePkts": rmonStatsUndersizePkts,
       "rmonStatsOversizePkts": rmonStatsOversizePkts,
       "rmonStatsFragments": rmonStatsFragments,
       "rmonStatsJabbers": rmonStatsJabbers,
       "rmonStatsCRCErrors": rmonStatsCRCErrors,
       "rmonStatsCollisions": rmonStatsCollisions,
       "rmonStatsDropEvents": rmonStatsDropEvents,
       "rmonStatsPkts64Octets": rmonStatsPkts64Octets,
       "rmonStatsPkts65to127Octets": rmonStatsPkts65to127Octets,
       "rmonStatsPkts128to255Octets": rmonStatsPkts128to255Octets,
       "rmonStatsPkts256to511Octets": rmonStatsPkts256to511Octets,
       "rmonStatsPkts512to1023Octets": rmonStatsPkts512to1023Octets,
       "rmonStatsPkts1024to1518Octets": rmonStatsPkts1024to1518Octets,
       "rmonStatsStatus": rmonStatsStatus,
       "rmonHistory": rmonHistory,
       "rmonHistoryControlTable": rmonHistoryControlTable,
       "rmonHistoryControlEntry": rmonHistoryControlEntry,
       "rmonHistoryControlIndex": rmonHistoryControlIndex,
       "rmonHistoryControlDataSource": rmonHistoryControlDataSource,
       "rmonHistoryControlBucketsRequested": rmonHistoryControlBucketsRequested,
       "rmonHistoryControlBucketsGranted": rmonHistoryControlBucketsGranted,
       "rmonHistoryControlInterval": rmonHistoryControlInterval,
       "rmonHistoryControlOwner": rmonHistoryControlOwner,
       "rmonHistoryControlStatus": rmonHistoryControlStatus,
       "rmonHistoryTable": rmonHistoryTable,
       "rmonHistoryEntry": rmonHistoryEntry,
       "rmonHistoryIndex": rmonHistoryIndex,
       "rmonHistorySampleIndex": rmonHistorySampleIndex,
       "rmonHistoryOctets": rmonHistoryOctets,
       "rmonHistoryPkts": rmonHistoryPkts,
       "rmonHistoryBroadcastPkts": rmonHistoryBroadcastPkts,
       "rmonHistoryMulticastPkts": rmonHistoryMulticastPkts,
       "rmonHistoryUtilization": rmonHistoryUtilization,
       "rmonHistoryUndersizePkts": rmonHistoryUndersizePkts,
       "rmonHistoryOversizePkts": rmonHistoryOversizePkts,
       "rmonHistoryFragments": rmonHistoryFragments,
       "rmonHistoryJabbers": rmonHistoryJabbers,
       "rmonHistoryCRCErrors": rmonHistoryCRCErrors,
       "rmonHistoryCollisions": rmonHistoryCollisions,
       "rmonHistoryDropEvents": rmonHistoryDropEvents,
       "rmonAlarm": rmonAlarm,
       "rmonAlarmTable": rmonAlarmTable,
       "rmonAlarmEntry": rmonAlarmEntry,
       "rmonAlarmIndex": rmonAlarmIndex,
       "rmonAlarmInterval": rmonAlarmInterval,
       "rmonAlarmVariable": rmonAlarmVariable,
       "rmonAlarmSampleType": rmonAlarmSampleType,
       "rmonAlarmValue": rmonAlarmValue,
       "rmonAlarmStartupAlarm": rmonAlarmStartupAlarm,
       "rmonAlarmRisingThreshold": rmonAlarmRisingThreshold,
       "rmonAlarmFallingThreshold": rmonAlarmFallingThreshold,
       "rmonAlarmRisingEventNumber": rmonAlarmRisingEventNumber,
       "rmonAlarmFallingEventNumber": rmonAlarmFallingEventNumber,
       "rmonAlarmOwner": rmonAlarmOwner,
       "rmonAlarmStatus": rmonAlarmStatus,
       "rmonEvent": rmonEvent,
       "rmonEventTable": rmonEventTable,
       "rmonEventEntry": rmonEventEntry,
       "rmonEventIndex": rmonEventIndex,
       "rmonEventDescription": rmonEventDescription,
       "rmonEventType": rmonEventType,
       "rmonEventCommunity": rmonEventCommunity,
       "rmonEventOwner": rmonEventOwner,
       "rmonEventStatus": rmonEventStatus,
       "rmonEventLastTimeSent": rmonEventLastTimeSent,
       "rmonLogTable": rmonLogTable,
       "rmonLogEntry": rmonLogEntry,
       "rmonLogEventIndex": rmonLogEventIndex,
       "rmonLogIndex": rmonLogIndex,
       "rmonLogTime": rmonLogTime,
       "rmonLogDescription": rmonLogDescription,
       "mgtTelnetWebGroup": mgtTelnetWebGroup,
       "telnetState": telnetState,
       "telnetPort": telnetPort,
       "webState": webState,
       "webPort": webPort,
       "mgtSessionTimeoutGroup": mgtSessionTimeoutGroup,
       "sessionTimeoutWeb": sessionTimeoutWeb,
       "sessionTimeoutTelnet": sessionTimeoutTelnet,
       "mgtDDPGroup": mgtDDPGroup,
       "ddpStatus": ddpStatus,
       "ddpReportTime": ddpReportTime,
       "ddpTable": ddpTable,
       "ddpEntry": ddpEntry,
       "ddpPort": ddpPort,
       "ddpPortStatus": ddpPortStatus,
       "dlinkL2Features": dlinkL2Features,
       "l2FDBGroup": l2FDBGroup,
       "fdbStaticFDB": fdbStaticFDB,
       "fdbUnicastStaticFDB": fdbUnicastStaticFDB,
       "fdbUnicastStaticFDBTable": fdbUnicastStaticFDBTable,
       "fdbUnicastStaticFDBEntry": fdbUnicastStaticFDBEntry,
       "fdbUnicastStaticFDBVID": fdbUnicastStaticFDBVID,
       "fdbUnicastStaticFDBMACAddr": fdbUnicastStaticFDBMACAddr,
       "fdbUnicastStaticFDBPort": fdbUnicastStaticFDBPort,
       "fdbUnicastStaticFDBState": fdbUnicastStaticFDBState,
       "fdbUnicastStaticFDBRowStatus": fdbUnicastStaticFDBRowStatus,
       "fdbMulticastStaticFDB": fdbMulticastStaticFDB,
       "fdMulticastStaticFDBTable": fdMulticastStaticFDBTable,
       "fdbMulticastStaticFDBEntry": fdbMulticastStaticFDBEntry,
       "fdbMulticastStaticFDBVID": fdbMulticastStaticFDBVID,
       "fdbMulticastStaticFDBMACAddr": fdbMulticastStaticFDBMACAddr,
       "fdbMulticastStaticFDBEgressPorts": fdbMulticastStaticFDBEgressPorts,
       "fdbMulticastStaticFDBRowStatus": fdbMulticastStaticFDBRowStatus,
       "fdbMACAddressTableSettings": fdbMACAddressTableSettings,
       "fdbMACAddrGlobalSettings": fdbMACAddrGlobalSettings,
       "fdbMACAddrAgingTime": fdbMACAddrAgingTime,
       "fdbMACAddrAgingDestinationHit": fdbMACAddrAgingDestinationHit,
       "fdbMACAddressLearningTable": fdbMACAddressLearningTable,
       "fdbMACAddressLearningEntry": fdbMACAddressLearningEntry,
       "fdbMACAddressLearningPort": fdbMACAddressLearningPort,
       "fdbMACAddressLearningState": fdbMACAddressLearningState,
       "fdbMACAddressTable": fdbMACAddressTable,
       "fdbMACAddressTableEntry": fdbMACAddressTableEntry,
       "fdbMACAddrTabVID": fdbMACAddrTabVID,
       "fdbMACAddrTabMACAddr": fdbMACAddrTabMACAddr,
       "fdbMACAddrTabType": fdbMACAddrTabType,
       "fdbMACAddrTabPort": fdbMACAddrTabPort,
       "fdbMACAddressClear": fdbMACAddressClear,
       "fdbClearId": fdbClearId,
       "fdbClearMac": fdbClearMac,
       "fdbClearAction": fdbClearAction,
       "l2Dot1qVlanGroup": l2Dot1qVlanGroup,
       "dot1qVlanAsyOnOff": dot1qVlanAsyOnOff,
       "dot1qVlanTable": dot1qVlanTable,
       "dot1qVlanEntry": dot1qVlanEntry,
       "dot1qVlanid": dot1qVlanid,
       "dot1qVlanName": dot1qVlanName,
       "dot1qVlanEgressPorts": dot1qVlanEgressPorts,
       "dot1qVlanUntaggedPorts": dot1qVlanUntaggedPorts,
       "dot1qVlanRowStatus": dot1qVlanRowStatus,
       "dot1qVlanPortTable": dot1qVlanPortTable,
       "dot1qVlanPortEntry": dot1qVlanPortEntry,
       "dot1qVlanPortIndex": dot1qVlanPortIndex,
       "dot1qVlanPortVlanMode": dot1qVlanPortVlanMode,
       "dot1qVlanPortAcceptableFrameType": dot1qVlanPortAcceptableFrameType,
       "dot1qVlanPortIngressChecking": dot1qVlanPortIngressChecking,
       "dot1qVlanPortNativeVlanStatus": dot1qVlanPortNativeVlanStatus,
       "dot1qVlanPortNativeVlanId": dot1qVlanPortNativeVlanId,
       "dot1qVlanPortTagVlanList": dot1qVlanPortTagVlanList,
       "dot1qVlanPortUntagVlanList": dot1qVlanPortUntagVlanList,
       "l2STPGroup": l2STPGroup,
       "stpProtocolSetting": stpProtocolSetting,
       "stpStatus": stpStatus,
       "stpNewRootTrapState": stpNewRootTrapState,
       "stpTopologyChangeTrapState": stpTopologyChangeTrapState,
       "stpVersion": stpVersion,
       "stpBridgePriority": stpBridgePriority,
       "stpBridgeMaxAge": stpBridgeMaxAge,
       "stpBridgeHelloTime": stpBridgeHelloTime,
       "stpBridgeForwardDelay": stpBridgeForwardDelay,
       "stpMaxHopCount": stpMaxHopCount,
       "stpTxHoldCount": stpTxHoldCount,
       "stpPortConfigurationTable": stpPortConfigurationTable,
       "stpPortConfigurationEntry": stpPortConfigurationEntry,
       "stpPort": stpPort,
       "stpPortAdminPathCost": stpPortAdminPathCost,
       "stpPortPathCost": stpPortPathCost,
       "stpPortState": stpPortState,
       "stpPortGuardRoot": stpPortGuardRoot,
       "stpPortLinkType": stpPortLinkType,
       "stpPortOperLinkType": stpPortOperLinkType,
       "stpPortFast": stpPortFast,
       "stpPortOperFast": stpPortOperFast,
       "stpPortTCNFilter": stpPortTCNFilter,
       "stpPortFowardBPDU": stpPortFowardBPDU,
       "stpPortPriority": stpPortPriority,
       "stpPortHelloTime": stpPortHelloTime,
       "mstConfiguration": mstConfiguration,
       "mstiConfigurationName": mstiConfigurationName,
       "mstiRevisionLevel": mstiRevisionLevel,
       "mstMstiConfigDigest": mstMstiConfigDigest,
       "mstVlanMstiMappingTable": mstVlanMstiMappingTable,
       "mstVlanMstiMappingEntry": mstVlanMstiMappingEntry,
       "mstInstanceIndex": mstInstanceIndex,
       "mstSetVlanList": mstSetVlanList,
       "mstResetVlanList": mstResetVlanList,
       "mstInstanceVlanMapped": mstInstanceVlanMapped,
       "mstInstanceVlanMapped2k": mstInstanceVlanMapped2k,
       "mstInstanceVlanMapped3k": mstInstanceVlanMapped3k,
       "mstInstanceVlanMapped4k": mstInstanceVlanMapped4k,
       "stpInstance": stpInstance,
       "mstCistBridgePriority": mstCistBridgePriority,
       "mstCistStatus": mstCistStatus,
       "mstCistPortDesignatedRoot": mstCistPortDesignatedRoot,
       "mstCistRegionalRoot": mstCistRegionalRoot,
       "mstCistPortDesignatedBridge": mstCistPortDesignatedBridge,
       "mstMstiBridgeTable": mstMstiBridgeTable,
       "mstMstiBridgeEntry": mstMstiBridgeEntry,
       "mstMstiInstanceIndex": mstMstiInstanceIndex,
       "mstMstiBridgePriority": mstMstiBridgePriority,
       "mstMstiStatus": mstMstiStatus,
       "mstMstiPortDesignatedRoot": mstMstiPortDesignatedRoot,
       "mstMstiBridgeRegionalRoot": mstMstiBridgeRegionalRoot,
       "mstMstiPortDesignatedBridge": mstMstiPortDesignatedBridge,
       "mstMstiTopChanges": mstMstiTopChanges,
       "stpInstancePortTable": stpInstancePortTable,
       "mstCistPortTable": mstCistPortTable,
       "mstCistPortEntry": mstCistPortEntry,
       "mstCistPort": mstCistPort,
       "mstCistPortAdminPathCost": mstCistPortAdminPathCost,
       "mstCistPortPathCost": mstCistPortPathCost,
       "mstCistPortPriority": mstCistPortPriority,
       "mstCistPortState": mstCistPortState,
       "mstCistCurrentPortRole": mstCistCurrentPortRole,
       "mstCistPortProtocolMigration": mstCistPortProtocolMigration,
       "mstMstiPortTable": mstMstiPortTable,
       "mstMstiPortEntry": mstMstiPortEntry,
       "mstMstiPort": mstMstiPort,
       "mstMstiPortInstanceIndex": mstMstiPortInstanceIndex,
       "mstMstiPortAdminPathCost": mstMstiPortAdminPathCost,
       "mstMstiPortPathCost": mstMstiPortPathCost,
       "mstMstiPortPriority": mstMstiPortPriority,
       "mstMstiPortState": mstMstiPortState,
       "mstMstiCurrentPortRole": mstMstiCurrentPortRole,
       "stpTraps": stpTraps,
       "stpTrapsList": stpTrapsList,
       "stpNewRootTrap": stpNewRootTrap,
       "stpTopologyChgTrap": stpTopologyChgTrap,
       "l2LBDGroup": l2LBDGroup,
       "lbdGlobalSettings": lbdGlobalSettings,
       "lbdState": lbdState,
       "lbdMode": lbdMode,
       "lbdEnabledVLANIDList": lbdEnabledVLANIDList,
       "lbdInterval": lbdInterval,
       "lbdTrapState": lbdTrapState,
       "lbdAction": lbdAction,
       "lbdPortSettings": lbdPortSettings,
       "lbdportTable": lbdportTable,
       "lbdportEntry": lbdportEntry,
       "lbdportIndex": lbdportIndex,
       "lbdportState": lbdportState,
       "lbdportResult": lbdportResult,
       "lbdportTimeLeft": lbdportTimeLeft,
       "lbdVlanSettings": lbdVlanSettings,
       "lbdVlanLoopTable": lbdVlanLoopTable,
       "lbdVlanLoopEntry": lbdVlanLoopEntry,
       "lbdVlanLoopIndex": lbdVlanLoopIndex,
       "lbdVlanLoopPorts": lbdVlanLoopPorts,
       "lbdTraps": lbdTraps,
       "lbdTrapsList": lbdTrapsList,
       "lbdLoopOccur": lbdLoopOccur,
       "lbdLoopRecover": lbdLoopRecover,
       "l2LAGroup": l2LAGroup,
       "laSystem": laSystem,
       "laSystemPriority": laSystemPriority,
       "laSystemLoadBalanceAlgorithm": laSystemLoadBalanceAlgorithm,
       "laActorSystemID": laActorSystemID,
       "laChannel": laChannel,
       "laPortChannelTable": laPortChannelTable,
       "laPortChannelEntry": laPortChannelEntry,
       "laPortChannelIfIndex": laPortChannelIfIndex,
       "laPortChannelMaxPorts": laPortChannelMaxPorts,
       "laPortChannelMemberNumber": laPortChannelMemberNumber,
       "laPortChannelMemberList": laPortChannelMemberList,
       "laSystemChannelGroupID": laSystemChannelGroupID,
       "laPortChannelMode": laPortChannelMode,
       "laChannelDetailTable": laChannelDetailTable,
       "laChannelDetailEntry": laChannelDetailEntry,
       "laChannelDetailPort": laChannelDetailPort,
       "laChannelDetailLACPTimeout": laChannelDetailLACPTimeout,
       "laChannelDetailWorkingMode": laChannelDetailWorkingMode,
       "laChannelDetailLACPState": laChannelDetailLACPState,
       "laChannelDetailPortPriority": laChannelDetailPortPriority,
       "laChannelDetailPortNumber": laChannelDetailPortNumber,
       "laChannelNeighborTable": laChannelNeighborTable,
       "laChannelNeighborEntry": laChannelNeighborEntry,
       "laChannelNeighborPort": laChannelNeighborPort,
       "laChannelNeighborSystemPriority": laChannelNeighborSystemPriority,
       "laChannelNeighborSystemID": laChannelNeighborSystemID,
       "laChannelNeighborPortNo": laChannelNeighborPortNo,
       "laChannelNeighborLACPTimeout": laChannelNeighborLACPTimeout,
       "laChannelNeighborWorkingMode": laChannelNeighborWorkingMode,
       "laChannelNeighborPortPriority": laChannelNeighborPortPriority,
       "l2MulticastCtrlGroup": l2MulticastCtrlGroup,
       "igsSystem": igsSystem,
       "igsStatus": igsStatus,
       "igsClearIgmpSnoopByVlanId": igsClearIgmpSnoopByVlanId,
       "igsVlan": igsVlan,
       "igsVlanFilterTable": igsVlanFilterTable,
       "igsVlanFilterEntry": igsVlanFilterEntry,
       "igsVlanFilterVlanId": igsVlanFilterVlanId,
       "igsVlanSnoopStatus": igsVlanSnoopStatus,
       "igsVlanFastLeave": igsVlanFastLeave,
       "igsVlanQuerier": igsVlanQuerier,
       "igsVlanCfgQuerier": igsVlanCfgQuerier,
       "igsVlanQuerierVersion": igsVlanQuerierVersion,
       "igsVlanQueryInterval": igsVlanQueryInterval,
       "igsVlanMaxResponseTime": igsVlanMaxResponseTime,
       "igsVlanRobustnessValue": igsVlanRobustnessValue,
       "igsVlanLastMemberQueryInterval": igsVlanLastMemberQueryInterval,
       "igsVlanMulticastGroupTable": igsVlanMulticastGroupTable,
       "igsVlanMulticastGroupEntry": igsVlanMulticastGroupEntry,
       "igsVlanMulticastGroupVlanId": igsVlanMulticastGroupVlanId,
       "igsVlanMulticastGroupIpAddress": igsVlanMulticastGroupIpAddress,
       "igsVlanMulticastGroupReceiverPortIndex": igsVlanMulticastGroupReceiverPortIndex,
       "igsVlanMulticastGroupReceiverSrcAddr": igsVlanMulticastGroupReceiverSrcAddr,
       "igsVlanMulticastGroupMacAddress": igsVlanMulticastGroupMacAddress,
       "igsVlanMulticastGroupExp": igsVlanMulticastGroupExp,
       "igsVlanMulticastGroupPortList": igsVlanMulticastGroupPortList,
       "igsVlanStaticMcastGrpTable": igsVlanStaticMcastGrpTable,
       "igsVlanStaticMcastGrpEntry": igsVlanStaticMcastGrpEntry,
       "igsVlanStaticMcastGrpVlanId": igsVlanStaticMcastGrpVlanId,
       "igsVlanStaticMcastGrpGroupAddress": igsVlanStaticMcastGrpGroupAddress,
       "igsVlanStaticMcastGrpPortList": igsVlanStaticMcastGrpPortList,
       "igsVlanStaticMcastGrpRowStatus": igsVlanStaticMcastGrpRowStatus,
       "igsVlanRouterTable": igsVlanRouterTable,
       "igsVlanRouterEntry": igsVlanRouterEntry,
       "igsVlanRouterVlanId": igsVlanRouterVlanId,
       "igsVlanRouterStaticPortList": igsVlanRouterStaticPortList,
       "igsVlanRouterBlockPortList": igsVlanRouterBlockPortList,
       "igsVlanRouterDynamicPortList": igsVlanRouterDynamicPortList,
       "igsStats": igsStats,
       "igsStatsTable": igsStatsTable,
       "igsStatsEntry": igsStatsEntry,
       "igsStatsVlanId": igsStatsVlanId,
       "igsStatsIGMPv1RxReport": igsStatsIGMPv1RxReport,
       "igsStatsIGMPv1RxQueries": igsStatsIGMPv1RxQueries,
       "igsStatsIGMPv1TxReport": igsStatsIGMPv1TxReport,
       "igsStatsIGMPv1TxQueries": igsStatsIGMPv1TxQueries,
       "igsStatsIGMPv2RxReport": igsStatsIGMPv2RxReport,
       "igsStatsIGMPv2RxQueries": igsStatsIGMPv2RxQueries,
       "igsStatsIGMPv2RxLeave": igsStatsIGMPv2RxLeave,
       "igsStatsIGMPv2TxReport": igsStatsIGMPv2TxReport,
       "igsStatsIGMPv2TxQueries": igsStatsIGMPv2TxQueries,
       "igsStatsIGMPv2TxLeave": igsStatsIGMPv2TxLeave,
       "igsStatsIGMPv3RxReport": igsStatsIGMPv3RxReport,
       "igsStatsIGMPv3RxQueries": igsStatsIGMPv3RxQueries,
       "igsStatsIGMPv3TxReport": igsStatsIGMPv3TxReport,
       "igsStatsIGMPv3TxQueries": igsStatsIGMPv3TxQueries,
       "mldSystem": mldSystem,
       "mldStatus": mldStatus,
       "mldClearIgmpSnoopByVlanId": mldClearIgmpSnoopByVlanId,
       "mldVlan": mldVlan,
       "mldVlanFilterTable": mldVlanFilterTable,
       "mldVlanFilterEntry": mldVlanFilterEntry,
       "mldVlanFilterVlanId": mldVlanFilterVlanId,
       "mldVlanSnoopStatus": mldVlanSnoopStatus,
       "mldVlanFastLeave": mldVlanFastLeave,
       "mldVlanQuerier": mldVlanQuerier,
       "mldVlanCfgQuerier": mldVlanCfgQuerier,
       "mldVlanQuerierVersion": mldVlanQuerierVersion,
       "mldVlanQueryInterval": mldVlanQueryInterval,
       "mldVlanMaxResponseTime": mldVlanMaxResponseTime,
       "mldVlanRobustnessValue": mldVlanRobustnessValue,
       "mldVlanLastListenerQueryInterval": mldVlanLastListenerQueryInterval,
       "mldVlanMulticastGroupTable": mldVlanMulticastGroupTable,
       "mldVlanMulticastGroupEntry": mldVlanMulticastGroupEntry,
       "mldVlanMulticastGroupVlanId": mldVlanMulticastGroupVlanId,
       "mldVlanMulticastGroupIpAddress": mldVlanMulticastGroupIpAddress,
       "mldVlanMulticastGroupReceiverPortIndex": mldVlanMulticastGroupReceiverPortIndex,
       "mldVlanMulticastGroupReceiverSrcAddr": mldVlanMulticastGroupReceiverSrcAddr,
       "mldVlanMulticastGroupMacAddress": mldVlanMulticastGroupMacAddress,
       "mldVlanMulticastGroupExp": mldVlanMulticastGroupExp,
       "mldVlanMulticastGroupPortList": mldVlanMulticastGroupPortList,
       "mldVlanStaticMcastGrpTable": mldVlanStaticMcastGrpTable,
       "mldVlanStaticMcastGrpEntry": mldVlanStaticMcastGrpEntry,
       "mldVlanStaticMcastGrpVlanId": mldVlanStaticMcastGrpVlanId,
       "mldVlanStaticMcastGrpGroupAddress": mldVlanStaticMcastGrpGroupAddress,
       "mldVlanStaticMcastGrpPortList": mldVlanStaticMcastGrpPortList,
       "mldVlanStaticMcastGrpRowStatus": mldVlanStaticMcastGrpRowStatus,
       "mldVlanRouterTable": mldVlanRouterTable,
       "mldVlanRouterEntry": mldVlanRouterEntry,
       "mldVlanRouterVlanId": mldVlanRouterVlanId,
       "mldVlanRouterStaticPortList": mldVlanRouterStaticPortList,
       "mldVlanRouterBlockPortList": mldVlanRouterBlockPortList,
       "mldVlanRouterDynamicPortList": mldVlanRouterDynamicPortList,
       "mldStats": mldStats,
       "mldStatsTable": mldStatsTable,
       "mldStatsEntry": mldStatsEntry,
       "mldStatsVlanId": mldStatsVlanId,
       "mldStatsMLDv1RxReport": mldStatsMLDv1RxReport,
       "mldStatsMLDv1RxDone": mldStatsMLDv1RxDone,
       "mldStatsMLDv1TxReport": mldStatsMLDv1TxReport,
       "mldStatsMLDv1TxDone": mldStatsMLDv1TxDone,
       "mldStatsMLDv2RxReport": mldStatsMLDv2RxReport,
       "mldStatsMLDv2TxReport": mldStatsMLDv2TxReport,
       "mldStatsRxQueries": mldStatsRxQueries,
       "mldStatsTxQueries": mldStatsTxQueries,
       "multicastFilterVlanTable": multicastFilterVlanTable,
       "multicastFilterVlanEntry": multicastFilterVlanEntry,
       "multicastFilterVlanIndex": multicastFilterVlanIndex,
       "multicastFilterVlanType": multicastFilterVlanType,
       "l2LLDPGroup": l2LLDPGroup,
       "lldpState": lldpState,
       "lldpForwardState": lldpForwardState,
       "lldpTrapState": lldpTrapState,
       "lldpMEDTrapState": lldpMEDTrapState,
       "lldpMsgTxInterval": lldpMsgTxInterval,
       "lldpMsgHoldMultiplier": lldpMsgHoldMultiplier,
       "lldpReinitDelay": lldpReinitDelay,
       "lldpTxDelay": lldpTxDelay,
       "lldpPortConfigTable": lldpPortConfigTable,
       "lldpPortConfigEntry": lldpPortConfigEntry,
       "lldpPortConfigPortNum": lldpPortConfigPortNum,
       "lldpPortConfigAdminStatus": lldpPortConfigAdminStatus,
       "lldpPortConfigSubtype": lldpPortConfigSubtype,
       "lldpPortConfigTLVsTxEnable": lldpPortConfigTLVsTxEnable,
       "lldpPortStatsClear": lldpPortStatsClear,
       "lldpPortNeighborClear": lldpPortNeighborClear,
       "lldpConfigManAddrTable": lldpConfigManAddrTable,
       "lldpConfigManAddrEntry": lldpConfigManAddrEntry,
       "lldpConfigManAddrSubtype": lldpConfigManAddrSubtype,
       "lldpConfigManAddr": lldpConfigManAddr,
       "lldpConfigManAddrPortsTxEnable": lldpConfigManAddrPortsTxEnable,
       "lldpXdot1Objects": lldpXdot1Objects,
       "lldpXdot1Config": lldpXdot1Config,
       "lldpXdot1ConfigPortVlanTable": lldpXdot1ConfigPortVlanTable,
       "lldpXdot1ConfigPortVlanEntry": lldpXdot1ConfigPortVlanEntry,
       "lldpXdot1ConfigVlanPortNum": lldpXdot1ConfigVlanPortNum,
       "lldpXdot1ConfigPortVlanTxEnable": lldpXdot1ConfigPortVlanTxEnable,
       "lldpXdot1ConfigVlanNameTable": lldpXdot1ConfigVlanNameTable,
       "lldpXdot1ConfigVlanNameEntry": lldpXdot1ConfigVlanNameEntry,
       "lldpXdot1LocConfigVlanNamePortNum": lldpXdot1LocConfigVlanNamePortNum,
       "lldpXdot1ConfigVlanNameTxEnableVlanList": lldpXdot1ConfigVlanNameTxEnableVlanList,
       "lldpXdot1ConfigProtoVlanTable": lldpXdot1ConfigProtoVlanTable,
       "lldpXdot1ConfigProtoVlanEntry": lldpXdot1ConfigProtoVlanEntry,
       "lldpXdot1ConfigProtoVlanPortNum": lldpXdot1ConfigProtoVlanPortNum,
       "lldpXdot1ConfigProtoVlanTxEnable": lldpXdot1ConfigProtoVlanTxEnable,
       "lldpXdot1ConfigProtocolTable": lldpXdot1ConfigProtocolTable,
       "lldpXdot1ConfigProtocolEntry": lldpXdot1ConfigProtocolEntry,
       "lldpXdot1ConfigProtocolPortNum": lldpXdot1ConfigProtocolPortNum,
       "lldpXdot1ConfigProtocolIndex": lldpXdot1ConfigProtocolIndex,
       "lldpXdot1ConfigProtocolTxEnable": lldpXdot1ConfigProtocolTxEnable,
       "lldpXdot1LocalData": lldpXdot1LocalData,
       "lldpXdot1LocTable": lldpXdot1LocTable,
       "lldpXdot1LocEntry": lldpXdot1LocEntry,
       "lldpXdot1LocPortNum": lldpXdot1LocPortNum,
       "lldpXdot1LocPortVlanId": lldpXdot1LocPortVlanId,
       "lldpXdot1LocProtoVlanTable": lldpXdot1LocProtoVlanTable,
       "lldpXdot1LocProtoVlanEntry": lldpXdot1LocProtoVlanEntry,
       "lldpXdot1LocProtoVlanPortNum": lldpXdot1LocProtoVlanPortNum,
       "lldpXdot1LocProtoVlanId": lldpXdot1LocProtoVlanId,
       "lldpXdot1LocProtoVlanSupported": lldpXdot1LocProtoVlanSupported,
       "lldpXdot1LocProtoVlanEnabled": lldpXdot1LocProtoVlanEnabled,
       "lldpXdot1LocVlanNameTable": lldpXdot1LocVlanNameTable,
       "lldpXdot1LocVlanNameEntry": lldpXdot1LocVlanNameEntry,
       "lldpXdot1LocVlanNamePortNum": lldpXdot1LocVlanNamePortNum,
       "lldpXdot1LocVlanId": lldpXdot1LocVlanId,
       "lldpXdot1LocVlanName": lldpXdot1LocVlanName,
       "lldpXdot1LocProtocolTable": lldpXdot1LocProtocolTable,
       "lldpXdot1LocProtocolEntry": lldpXdot1LocProtocolEntry,
       "lldpXdot1LocProtocolPortNum": lldpXdot1LocProtocolPortNum,
       "lldpXdot1LocProtocolIndex": lldpXdot1LocProtocolIndex,
       "lldpXdot1LocProtocolId": lldpXdot1LocProtocolId,
       "lldpXdot1RemoteData": lldpXdot1RemoteData,
       "lldpXdot1RemTable": lldpXdot1RemTable,
       "lldpXdot1RemEntry": lldpXdot1RemEntry,
       "lldpXdot1RemTimeMark": lldpXdot1RemTimeMark,
       "lldpXdot1RemLocalPortNum": lldpXdot1RemLocalPortNum,
       "lldpXdot1RemIndex": lldpXdot1RemIndex,
       "lldpXdot1RemPortVlanId": lldpXdot1RemPortVlanId,
       "lldpXdot1RemProtoVlanTable": lldpXdot1RemProtoVlanTable,
       "lldpXdot1RemProtoVlanEntry": lldpXdot1RemProtoVlanEntry,
       "lldpXdot1RemProtoVlanTimeMark": lldpXdot1RemProtoVlanTimeMark,
       "lldpXdot1RemProtoVlanLocalPortNum": lldpXdot1RemProtoVlanLocalPortNum,
       "lldpXdot1RemProtoVlanIndex": lldpXdot1RemProtoVlanIndex,
       "lldpXdot1RemProtoVlanId": lldpXdot1RemProtoVlanId,
       "lldpXdot1RemProtoVlanSupported": lldpXdot1RemProtoVlanSupported,
       "lldpXdot1RemProtoVlanEnabled": lldpXdot1RemProtoVlanEnabled,
       "lldpXdot1RemVlanNameTable": lldpXdot1RemVlanNameTable,
       "lldpXdot1RemVlanNameEntry": lldpXdot1RemVlanNameEntry,
       "lldpXdot1RemVlanNameTimeMark": lldpXdot1RemVlanNameTimeMark,
       "lldpXdot1RemVlanNameLocalPortNum": lldpXdot1RemVlanNameLocalPortNum,
       "lldpXdot1RemVlanNameIndex": lldpXdot1RemVlanNameIndex,
       "lldpXdot1RemVlanId": lldpXdot1RemVlanId,
       "lldpXdot1RemVlanName": lldpXdot1RemVlanName,
       "lldpXdot1RemProtocolTable": lldpXdot1RemProtocolTable,
       "lldpXdot1RemProtocolEntry": lldpXdot1RemProtocolEntry,
       "lldpXdot1RemProtocolTimeMark": lldpXdot1RemProtocolTimeMark,
       "lldpXdot1RemProtocolLocalPortNum": lldpXdot1RemProtocolLocalPortNum,
       "lldpXdot1RemProtocolIndex": lldpXdot1RemProtocolIndex,
       "lldpXdot1RemProtocolIdIndex": lldpXdot1RemProtocolIdIndex,
       "lldpXdot1RemProtocolId": lldpXdot1RemProtocolId,
       "lldpXdot3Objects": lldpXdot3Objects,
       "lldpXdot3Config": lldpXdot3Config,
       "lldpXdot3PortConfigTable": lldpXdot3PortConfigTable,
       "lldpXdot3PortConfigEntry": lldpXdot3PortConfigEntry,
       "lldpXdot3PortConfigPortNum": lldpXdot3PortConfigPortNum,
       "lldpXdot3PortConfigTLVsTxEnable": lldpXdot3PortConfigTLVsTxEnable,
       "lldpXdot3LocalData": lldpXdot3LocalData,
       "lldpXdot3LocPortTable": lldpXdot3LocPortTable,
       "lldpXdot3LocPortEntry": lldpXdot3LocPortEntry,
       "lldpXdot3LocPortNum": lldpXdot3LocPortNum,
       "lldpXdot3LocPortAutoNegSupported": lldpXdot3LocPortAutoNegSupported,
       "lldpXdot3LocPortAutoNegEnabled": lldpXdot3LocPortAutoNegEnabled,
       "lldpXdot3LocPortAutoNegAdvertisedCap": lldpXdot3LocPortAutoNegAdvertisedCap,
       "lldpXdot3LocPortOperMauType": lldpXdot3LocPortOperMauType,
       "lldpXdot3LocPowerTable": lldpXdot3LocPowerTable,
       "lldpXdot3LocPowerEntry": lldpXdot3LocPowerEntry,
       "lldpXdot3LocPowerPortNum": lldpXdot3LocPowerPortNum,
       "lldpXdot3LocPowerPortClass": lldpXdot3LocPowerPortClass,
       "lldpXdot3LocPowerMDISupported": lldpXdot3LocPowerMDISupported,
       "lldpXdot3LocPowerMDIEnabled": lldpXdot3LocPowerMDIEnabled,
       "lldpXdot3LocPowerPairControlable": lldpXdot3LocPowerPairControlable,
       "lldpXdot3LocPowerPairs": lldpXdot3LocPowerPairs,
       "lldpXdot3LocPowerClass": lldpXdot3LocPowerClass,
       "lldpXdot3LocLinkAggTable": lldpXdot3LocLinkAggTable,
       "lldpXdot3LocLinkAggEntry": lldpXdot3LocLinkAggEntry,
       "lldpXdot3LocLinkAggPortNum": lldpXdot3LocLinkAggPortNum,
       "lldpXdot3LocLinkAggStatus": lldpXdot3LocLinkAggStatus,
       "lldpXdot3LocLinkAggPortId": lldpXdot3LocLinkAggPortId,
       "lldpXdot3LocMaxFrameSizeTable": lldpXdot3LocMaxFrameSizeTable,
       "lldpXdot3LocMaxFrameSizeEntry": lldpXdot3LocMaxFrameSizeEntry,
       "lldpXdot3LocMaxFrameSizePortNum": lldpXdot3LocMaxFrameSizePortNum,
       "lldpXdot3LocMaxFrameSize": lldpXdot3LocMaxFrameSize,
       "lldpXdot3RemoteData": lldpXdot3RemoteData,
       "lldpXdot3RemPortTable": lldpXdot3RemPortTable,
       "lldpXdot3RemPortEntry": lldpXdot3RemPortEntry,
       "lldpXdot3RemTimeMark": lldpXdot3RemTimeMark,
       "lldpXdot3RemLocalPortNum": lldpXdot3RemLocalPortNum,
       "lldpXdot3RemIndex": lldpXdot3RemIndex,
       "lldpXdot3RemPortAutoNegSupported": lldpXdot3RemPortAutoNegSupported,
       "lldpXdot3RemPortAutoNegEnabled": lldpXdot3RemPortAutoNegEnabled,
       "lldpXdot3RemPortAutoNegAdvertisedCap": lldpXdot3RemPortAutoNegAdvertisedCap,
       "lldpXdot3RemPortOperMauType": lldpXdot3RemPortOperMauType,
       "lldpXdot3RemPowerTable": lldpXdot3RemPowerTable,
       "lldpXdot3RemPowerEntry": lldpXdot3RemPowerEntry,
       "lldpXdot3RemPowerTimeMark": lldpXdot3RemPowerTimeMark,
       "lldpXdot3RemPowerLocalPortNum": lldpXdot3RemPowerLocalPortNum,
       "lldpXdot3RemPowerIndex": lldpXdot3RemPowerIndex,
       "lldpXdot3RemPowerPortClass": lldpXdot3RemPowerPortClass,
       "lldpXdot3RemPowerMDISupported": lldpXdot3RemPowerMDISupported,
       "lldpXdot3RemPowerMDIEnabled": lldpXdot3RemPowerMDIEnabled,
       "lldpXdot3RemPowerPairControlable": lldpXdot3RemPowerPairControlable,
       "lldpXdot3RemPowerPairs": lldpXdot3RemPowerPairs,
       "lldpXdot3RemPowerClass": lldpXdot3RemPowerClass,
       "lldpXdot3RemLinkAggTable": lldpXdot3RemLinkAggTable,
       "lldpXdot3RemLinkAggEntry": lldpXdot3RemLinkAggEntry,
       "lldpXdot3RemLinkAggTimeMark": lldpXdot3RemLinkAggTimeMark,
       "lldpXdot3RemLinkAggLocalPortNum": lldpXdot3RemLinkAggLocalPortNum,
       "lldpXdot3RemLinkAggIndex": lldpXdot3RemLinkAggIndex,
       "lldpXdot3RemLinkAggStatus": lldpXdot3RemLinkAggStatus,
       "lldpXdot3RemLinkAggPortId": lldpXdot3RemLinkAggPortId,
       "lldpXdot3RemMaxFrameSizeTable": lldpXdot3RemMaxFrameSizeTable,
       "lldpXdot3RemMaxFrameSizeEntry": lldpXdot3RemMaxFrameSizeEntry,
       "lldpXdot3RemMaxFrameSizeTimeMark": lldpXdot3RemMaxFrameSizeTimeMark,
       "lldpXdot3RemMaxFrameSizeLocalPortNum": lldpXdot3RemMaxFrameSizeLocalPortNum,
       "lldpXdot3RemMaxFrameSizeIndex": lldpXdot3RemMaxFrameSizeIndex,
       "lldpXdot3RemMaxFrameSize": lldpXdot3RemMaxFrameSize,
       "lldpStatistics": lldpStatistics,
       "lldpStatsRemTablesLastChangeTime": lldpStatsRemTablesLastChangeTime,
       "lldpStatsRemTablesInserts": lldpStatsRemTablesInserts,
       "lldpStatsRemTablesDeletes": lldpStatsRemTablesDeletes,
       "lldpStatsRemTablesDrops": lldpStatsRemTablesDrops,
       "lldpStatsRemTablesAgeouts": lldpStatsRemTablesAgeouts,
       "lldpStatsTxPortTable": lldpStatsTxPortTable,
       "lldpStatsTxPortEntry": lldpStatsTxPortEntry,
       "lldpStatsTxPortNum": lldpStatsTxPortNum,
       "lldpStatsTxPortFramesTotal": lldpStatsTxPortFramesTotal,
       "lldpRxStatsPortTable": lldpRxStatsPortTable,
       "lldpRxStatsPortEntry": lldpRxStatsPortEntry,
       "lldpStatsRxPortNum": lldpStatsRxPortNum,
       "lldpStatsRxPortFramesDiscardedTotal": lldpStatsRxPortFramesDiscardedTotal,
       "lldpStatsRxPortFramesErrors": lldpStatsRxPortFramesErrors,
       "lldpStatsRxPortFramesTotal": lldpStatsRxPortFramesTotal,
       "lldpStatsRxPortTLVsDiscardedTotal": lldpStatsRxPortTLVsDiscardedTotal,
       "lldpStatsRxPortTLVsUnrecognizedTotal": lldpStatsRxPortTLVsUnrecognizedTotal,
       "lldpStatsRxPortAgeoutsTotal": lldpStatsRxPortAgeoutsTotal,
       "lldpStatsRemTablesClear": lldpStatsRemTablesClear,
       "lldpLocalSystemData": lldpLocalSystemData,
       "lldpLocChassisIdSubtype": lldpLocChassisIdSubtype,
       "lldpLocChassisId": lldpLocChassisId,
       "lldpLocSysName": lldpLocSysName,
       "lldpLocSysDesc": lldpLocSysDesc,
       "lldpLocSysCapSupported": lldpLocSysCapSupported,
       "lldpLocSysCapEnabled": lldpLocSysCapEnabled,
       "lldpLocPortTable": lldpLocPortTable,
       "lldpLocPortEntry": lldpLocPortEntry,
       "lldpLocPortNum": lldpLocPortNum,
       "lldpLocPortIdSubtype": lldpLocPortIdSubtype,
       "lldpLocPortId": lldpLocPortId,
       "lldpLocPortDesc": lldpLocPortDesc,
       "lldpLocManAddrTable": lldpLocManAddrTable,
       "lldpLocManAddrEntry": lldpLocManAddrEntry,
       "lldpLocManAddrSubtype": lldpLocManAddrSubtype,
       "lldpLocManAddr": lldpLocManAddr,
       "lldpLocManAddrLen": lldpLocManAddrLen,
       "lldpLocManAddrIfSubtype": lldpLocManAddrIfSubtype,
       "lldpLocManAddrIfId": lldpLocManAddrIfId,
       "lldpLocManAddrOID": lldpLocManAddrOID,
       "lldpRemoteSystemsData": lldpRemoteSystemsData,
       "lldpRemTable": lldpRemTable,
       "lldpRemEntry": lldpRemEntry,
       "lldpRemTimeMark": lldpRemTimeMark,
       "lldpRemLocalPortNum": lldpRemLocalPortNum,
       "lldpRemIndex": lldpRemIndex,
       "lldpRemChassisIdSubtype": lldpRemChassisIdSubtype,
       "lldpRemChassisId": lldpRemChassisId,
       "lldpRemPortIdSubtype": lldpRemPortIdSubtype,
       "lldpRemPortId": lldpRemPortId,
       "lldpRemPortDesc": lldpRemPortDesc,
       "lldpRemSysName": lldpRemSysName,
       "lldpRemSysDesc": lldpRemSysDesc,
       "lldpRemSysCapSupported": lldpRemSysCapSupported,
       "lldpRemSysCapEnabled": lldpRemSysCapEnabled,
       "lldpRemManAddrTable": lldpRemManAddrTable,
       "lldpRemManAddrEntry": lldpRemManAddrEntry,
       "lldpRemManTimeMark": lldpRemManTimeMark,
       "lldpRemManLocalPortNum": lldpRemManLocalPortNum,
       "lldpRemManIndex": lldpRemManIndex,
       "lldpRemManAddrSubtype": lldpRemManAddrSubtype,
       "lldpRemManAddr": lldpRemManAddr,
       "lldpRemManAddrIfSubtype": lldpRemManAddrIfSubtype,
       "lldpRemManAddrIfId": lldpRemManAddrIfId,
       "lldpRemManAddrOID": lldpRemManAddrOID,
       "lldpRemUnknownTLVTable": lldpRemUnknownTLVTable,
       "lldpRemUnknownTLVEntry": lldpRemUnknownTLVEntry,
       "lldpRemUnknownTimeMark": lldpRemUnknownTimeMark,
       "lldpRemUnknownLocalPortNum": lldpRemUnknownLocalPortNum,
       "lldpRemUnknownIndex": lldpRemUnknownIndex,
       "lldpRemUnknownTLVType": lldpRemUnknownTLVType,
       "lldpRemUnknownTLVInfo": lldpRemUnknownTLVInfo,
       "lldpXMedNotifications": lldpXMedNotifications,
       "lldpXMedTopologyChangeDetected": lldpXMedTopologyChangeDetected,
       "lldpXMedObjects": lldpXMedObjects,
       "lldpXMedConfig": lldpXMedConfig,
       "lldpXMedLocDeviceClass": lldpXMedLocDeviceClass,
       "lldpXMedPortConfigTable": lldpXMedPortConfigTable,
       "lldpXMedPortConfigEntry": lldpXMedPortConfigEntry,
       "lldpXMedPortConfigPortNum": lldpXMedPortConfigPortNum,
       "lldpXMedPortCapSupported": lldpXMedPortCapSupported,
       "lldpXMedPortConfigTLVsTxEnable": lldpXMedPortConfigTLVsTxEnable,
       "lldpXMedPortConfigNotifEnable": lldpXMedPortConfigNotifEnable,
       "lldpXMedFastStartRepeatCount": lldpXMedFastStartRepeatCount,
       "lldpXMedLocalData": lldpXMedLocalData,
       "lldpXMedLocMediaPolicyTable": lldpXMedLocMediaPolicyTable,
       "lldpXMedLocMediaPolicyEntry": lldpXMedLocMediaPolicyEntry,
       "lldpXMedLocMediaPolicyPortNum": lldpXMedLocMediaPolicyPortNum,
       "lldpXMedLocMediaPolicyAppType": lldpXMedLocMediaPolicyAppType,
       "lldpXMedLocMediaPolicyVlanID": lldpXMedLocMediaPolicyVlanID,
       "lldpXMedLocMediaPolicyPriority": lldpXMedLocMediaPolicyPriority,
       "lldpXMedLocMediaPolicyDscp": lldpXMedLocMediaPolicyDscp,
       "lldpXMedLocMediaPolicyUnknown": lldpXMedLocMediaPolicyUnknown,
       "lldpXMedLocMediaPolicyTagged": lldpXMedLocMediaPolicyTagged,
       "lldpXMedLocHardwareRev": lldpXMedLocHardwareRev,
       "lldpXMedLocFirmwareRev": lldpXMedLocFirmwareRev,
       "lldpXMedLocSoftwareRev": lldpXMedLocSoftwareRev,
       "lldpXMedLocSerialNum": lldpXMedLocSerialNum,
       "lldpXMedLocMfgName": lldpXMedLocMfgName,
       "lldpXMedLocModelName": lldpXMedLocModelName,
       "lldpXMedLocAssetID": lldpXMedLocAssetID,
       "lldpXMedLocXPoEDeviceType": lldpXMedLocXPoEDeviceType,
       "lldpXMedRemoteData": lldpXMedRemoteData,
       "lldpXMedRemCapabilitiesTable": lldpXMedRemCapabilitiesTable,
       "lldpXMedRemCapabilitiesEntry": lldpXMedRemCapabilitiesEntry,
       "lldpXMedRemCapTimeMark": lldpXMedRemCapTimeMark,
       "lldpXMedRemCapPortNum": lldpXMedRemCapPortNum,
       "lldpXMedRemCapIndex": lldpXMedRemCapIndex,
       "lldpXMedRemCapSupported": lldpXMedRemCapSupported,
       "lldpXMedRemMediaPolicyTable": lldpXMedRemMediaPolicyTable,
       "lldpXMedRemMediaPolicyEntry": lldpXMedRemMediaPolicyEntry,
       "lldpXMedRemMediaPolicyTimeMark": lldpXMedRemMediaPolicyTimeMark,
       "lldpXMedRemMediaPolicyPortNum": lldpXMedRemMediaPolicyPortNum,
       "lldpXMedRemMediaPolicyIndex": lldpXMedRemMediaPolicyIndex,
       "lldpXMedRemMediaPolicyAppType": lldpXMedRemMediaPolicyAppType,
       "lldpXMedRemMediaPolicyVlanID": lldpXMedRemMediaPolicyVlanID,
       "lldpXMedRemMediaPolicyPriority": lldpXMedRemMediaPolicyPriority,
       "lldpXMedRemMediaPolicyDscp": lldpXMedRemMediaPolicyDscp,
       "lldpXMedRemMediaPolicyUnknown": lldpXMedRemMediaPolicyUnknown,
       "lldpXMedRemMediaPolicyTagged": lldpXMedRemMediaPolicyTagged,
       "lldpXMedRemInventoryTable": lldpXMedRemInventoryTable,
       "lldpXMedRemInventoryEntry": lldpXMedRemInventoryEntry,
       "lldpXMedRemTimeMark": lldpXMedRemTimeMark,
       "lldpXMedRemPortNum": lldpXMedRemPortNum,
       "lldpXMedRemIndex": lldpXMedRemIndex,
       "lldpXMedRemHardwareRev": lldpXMedRemHardwareRev,
       "lldpXMedRemFirmwareRev": lldpXMedRemFirmwareRev,
       "lldpXMedRemSoftwareRev": lldpXMedRemSoftwareRev,
       "lldpXMedRemSerialNum": lldpXMedRemSerialNum,
       "lldpXMedRemMfgName": lldpXMedRemMfgName,
       "lldpXMedRemModelName": lldpXMedRemModelName,
       "lldpXMedRemAssetID": lldpXMedRemAssetID,
       "dlinkL3Features": dlinkL3Features,
       "l3ARPGroup": l3ARPGroup,
       "arpAgingTime": arpAgingTime,
       "arpAgingTimeTable": arpAgingTimeTable,
       "arpAgingTimeEntry": arpAgingTimeEntry,
       "arpAgingTimeIntrefaceID": arpAgingTimeIntrefaceID,
       "arpAgingTimeTimeout": arpAgingTimeTimeout,
       "arpARPTable": arpARPTable,
       "arpTable": arpTable,
       "arpEntry": arpEntry,
       "arpIntrefaceID": arpIntrefaceID,
       "arpIpAddr": arpIpAddr,
       "arpMacAddress": arpMacAddress,
       "arpType": arpType,
       "arpRowStatus": arpRowStatus,
       "l3IpMgmtGroup": l3IpMgmtGroup,
       "multiIfMainTable": multiIfMainTable,
       "multiIfMainEntry": multiIfMainEntry,
       "multiIfMainIndex": multiIfMainIndex,
       "multiIfMainAdminStatus": multiIfMainAdminStatus,
       "multiIfMainOperStatus": multiIfMainOperStatus,
       "multiIfIpBindVlanId": multiIfIpBindVlanId,
       "multiL3VlanIfName": multiL3VlanIfName,
       "multiIfMainRowStatus": multiIfMainRowStatus,
       "multiIfIpTable": multiIfIpTable,
       "multiIfIpEntry": multiIfIpEntry,
       "multiIfIpIndex": multiIfIpIndex,
       "multiIfIpAddrAllocMethod": multiIfIpAddrAllocMethod,
       "multiIfIpAddr": multiIfIpAddr,
       "multiIfIpSubnetMask": multiIfIpSubnetMask,
       "multiRouteTable": multiRouteTable,
       "multiRouteEntry": multiRouteEntry,
       "multiRouteDest": multiRouteDest,
       "multiRouteMask": multiRouteMask,
       "multiRouteTos": multiRouteTos,
       "multiRouteNextHop": multiRouteNextHop,
       "multiRouteIfIndex": multiRouteIfIndex,
       "multiRouteStatus": multiRouteStatus,
       "multiIpv6IfTable": multiIpv6IfTable,
       "multiIpv6IfEntry": multiIpv6IfEntry,
       "multiIpv6IfIndex": multiIpv6IfIndex,
       "multiIpv6IfAdminStatus": multiIpv6IfAdminStatus,
       "multiIpv6IfOperStatus": multiIpv6IfOperStatus,
       "multiIpv6IfRetransmitTime": multiIpv6IfRetransmitTime,
       "multiIpv6AddrTable": multiIpv6AddrTable,
       "multiIpv6AddrEntry": multiIpv6AddrEntry,
       "multiIpv6AddrIndex": multiIpv6AddrIndex,
       "multiIpv6AddrAddress": multiIpv6AddrAddress,
       "multiIpv6AddrPrefixLen": multiIpv6AddrPrefixLen,
       "multiIpv6AddrAdminStatus": multiIpv6AddrAdminStatus,
       "multiIpv6AddrType": multiIpv6AddrType,
       "multiIpv6AddrCfgMethod": multiIpv6AddrCfgMethod,
       "multiIpv6AddrOperStatus": multiIpv6AddrOperStatus,
       "multiIPv6neighborTable": multiIPv6neighborTable,
       "multiIpv6NeighborEntry": multiIpv6NeighborEntry,
       "multiIpv6NeighborIndex": multiIpv6NeighborIndex,
       "multiIpv6NeighborAddr": multiIpv6NeighborAddr,
       "multiIpv6NeighborMacAddr": multiIpv6NeighborMacAddr,
       "multiIpv6NeighborType": multiIpv6NeighborType,
       "multiIpv6NeighborCacheState": multiIpv6NeighborCacheState,
       "multiIpv6NeighborRowStatus": multiIpv6NeighborRowStatus,
       "multiIpv6RouteTable": multiIpv6RouteTable,
       "multiIpv6RouteEntry": multiIpv6RouteEntry,
       "multiIpv6RouteDest": multiIpv6RouteDest,
       "multiIpv6RoutePfxLength": multiIpv6RoutePfxLength,
       "multiIpv6RouteProtocol": multiIpv6RouteProtocol,
       "multiIpv6RouteNextHop": multiIpv6RouteNextHop,
       "multiIpv6RouteIfIndex": multiIpv6RouteIfIndex,
       "multiIpv6RouteAdminStatus": multiIpv6RouteAdminStatus,
       "dhcpClientTable": dhcpClientTable,
       "dhcpClientEntry": dhcpClientEntry,
       "dhcpClientIfIndex": dhcpClientIfIndex,
       "dhcpClientClientIdIfIdx": dhcpClientClientIdIfIdx,
       "dhcpClientClassIdType": dhcpClientClassIdType,
       "dhcpClientClassId": dhcpClientClassId,
       "dhcpClientHostName": dhcpClientHostName,
       "dhcpClientLeaseDay": dhcpClientLeaseDay,
       "dhcpClientLeaseHour": dhcpClientLeaseHour,
       "dhcpClientLeaseMinute": dhcpClientLeaseMinute,
       "dhcp6ClientTable": dhcp6ClientTable,
       "dhcp6ClientEntry": dhcp6ClientEntry,
       "dhcp6ClientIndex": dhcp6ClientIndex,
       "dhcp6ClientEnabled": dhcp6ClientEnabled,
       "dhcp6ClientRapidCommit": dhcp6ClientRapidCommit,
       "dlinkQoS": dlinkQoS,
       "qosBasicSettingsGroup": qosBasicSettingsGroup,
       "qosBasPortDefaultCoS": qosBasPortDefaultCoS,
       "qosPortDefaultCoSTable": qosPortDefaultCoSTable,
       "qosPortDefaultCoSEntry": qosPortDefaultCoSEntry,
       "qosPortindex": qosPortindex,
       "qosPortDefMode": qosPortDefMode,
       "qosPortDefCos": qosPortDefCos,
       "qosPortDefOverride": qosPortDefOverride,
       "qosBasPortScheMethod": qosBasPortScheMethod,
       "qosPortSchedulerMethodTable": qosPortSchedulerMethodTable,
       "qosPortSchedulerMethodEntry": qosPortSchedulerMethodEntry,
       "qosSchedulingModeBasePort": qosSchedulingModeBasePort,
       "qosSchedulingMode": qosSchedulingMode,
       "qosBasQueueSettings": qosBasQueueSettings,
       "qosQueueSettingsTable": qosQueueSettingsTable,
       "qosQueueSettingsEntry": qosQueueSettingsEntry,
       "qosQueueBasePort": qosQueueBasePort,
       "qosQueueID": qosQueueID,
       "qosQueueWrrWeight": qosQueueWrrWeight,
       "qosQueueQuantum": qosQueueQuantum,
       "qosBasCoS2QueueMapping": qosBasCoS2QueueMapping,
       "qosCoS2QueueTable": qosCoS2QueueTable,
       "qosCoS2QueueEntry": qosCoS2QueueEntry,
       "qosCoS2QueCos": qosCoS2QueCos,
       "qosCos2QueQueueID": qosCos2QueQueueID,
       "qosBasPortRateLimiting": qosBasPortRateLimiting,
       "qosPortRateLimitingTable": qosPortRateLimitingTable,
       "qosPortRateLimitingEntry": qosPortRateLimitingEntry,
       "qosBandwidthBasePort": qosBandwidthBasePort,
       "qosBandwidthRxRate": qosBandwidthRxRate,
       "qosBandwidthRxRateMode": qosBandwidthRxRateMode,
       "qosBandwidthRxBurst": qosBandwidthRxBurst,
       "qosBandwidthTxRate": qosBandwidthTxRate,
       "qosBandwidthTxRateMode": qosBandwidthTxRateMode,
       "qosBandwidthTxBurst": qosBandwidthTxBurst,
       "qosBasQueueRateLimiting": qosBasQueueRateLimiting,
       "qosQueueRateLimitingTable": qosQueueRateLimitingTable,
       "qosQueueRateLimitingEntry": qosQueueRateLimitingEntry,
       "qosQueueBandwidthBasePort": qosQueueBandwidthBasePort,
       "qosQueueBandwidthQueId": qosQueueBandwidthQueId,
       "qosQueueBandwidthMinRate": qosQueueBandwidthMinRate,
       "qosQueueBandwidthMaxRate": qosQueueBandwidthMaxRate,
       "qosQueueBandwidthRateMode": qosQueueBandwidthRateMode,
       "qosBasDscpMapCos": qosBasDscpMapCos,
       "qosDscpMapCosTable": qosDscpMapCosTable,
       "qosDscpMapCosEntry": qosDscpMapCosEntry,
       "qosPortIndex": qosPortIndex,
       "qosTrustMode": qosTrustMode,
       "qosDscpValueMapCosTable": qosDscpValueMapCosTable,
       "qosDscpValueMapCosEntry": qosDscpValueMapCosEntry,
       "qosDscpPort": qosDscpPort,
       "qosDscpCos": qosDscpCos,
       "qosDscpMapCosList": qosDscpMapCosList,
       "dlinkACL": dlinkACL,
       "aclGroup": aclGroup,
       "aclProfile": aclProfile,
       "aclProfileTable": aclProfileTable,
       "aclProfileEntry": aclProfileEntry,
       "aclProfileNo": aclProfileNo,
       "aclProfileName": aclProfileName,
       "aclProfileType": aclProfileType,
       "aclProfileRuleCount": aclProfileRuleCount,
       "aclProfileRemark": aclProfileRemark,
       "aclProfileRuleIdStart": aclProfileRuleIdStart,
       "aclProfileRuleIdStep": aclProfileRuleIdStep,
       "aclProfileRuleCounterState": aclProfileRuleCounterState,
       "aclProfileRuleCounterClear": aclProfileRuleCounterClear,
       "aclProfileStatus": aclProfileStatus,
       "aclL2Rule": aclL2Rule,
       "aclL2RuleTable": aclL2RuleTable,
       "aclL2RuleEntry": aclL2RuleEntry,
       "aclL2ProfileID": aclL2ProfileID,
       "aclL2AccessID": aclL2AccessID,
       "aclL2RuleEtherType": aclL2RuleEtherType,
       "aclL2RuleDstMacAddr": aclL2RuleDstMacAddr,
       "aclL2RuleSrcMacAddr": aclL2RuleSrcMacAddr,
       "aclL2RuleVlanId": aclL2RuleVlanId,
       "aclL2Rule1pPriority": aclL2Rule1pPriority,
       "aclL2RuleDstMacAddrMask": aclL2RuleDstMacAddrMask,
       "aclL2RuleSrcMacAddrMask": aclL2RuleSrcMacAddrMask,
       "aclL2RuleTimeRange": aclL2RuleTimeRange,
       "aclL2RuleAction": aclL2RuleAction,
       "aclL2RuleEtherTypeMask": aclL2RuleEtherTypeMask,
       "aclL2RuleMatchCount": aclL2RuleMatchCount,
       "aclL2RuleStatus": aclL2RuleStatus,
       "aclL3v4Rule": aclL3v4Rule,
       "aclL3v4RuleTable": aclL3v4RuleTable,
       "aclL3v4RuleEntry": aclL3v4RuleEntry,
       "aclL3v4RuleProfileNo": aclL3v4RuleProfileNo,
       "aclL3v4RuleAccessID": aclL3v4RuleAccessID,
       "aclL3v4RuleDstIpAddr": aclL3v4RuleDstIpAddr,
       "aclL3v4RuleSrcIpAddr": aclL3v4RuleSrcIpAddr,
       "aclL3v4RuleDstIpAddrMask": aclL3v4RuleDstIpAddrMask,
       "aclL3v4RuleSrcIpAddrMask": aclL3v4RuleSrcIpAddrMask,
       "aclL3v4RuleAction": aclL3v4RuleAction,
       "aclL3v4RuleTimeRange": aclL3v4RuleTimeRange,
       "aclL3v4RuleMatchCount": aclL3v4RuleMatchCount,
       "aclL3v4RuleStatus": aclL3v4RuleStatus,
       "aclL3v4ExtRule": aclL3v4ExtRule,
       "aclL3v4ExtRuleTable": aclL3v4ExtRuleTable,
       "aclL3v4ExtRuleEntry": aclL3v4ExtRuleEntry,
       "aclL3v4ExtRuleProfileNo": aclL3v4ExtRuleProfileNo,
       "aclL3v4ExtRuleAccessID": aclL3v4ExtRuleAccessID,
       "aclL3v4ExtRuleProtocol": aclL3v4ExtRuleProtocol,
       "aclL3v4ExtRuleFragments": aclL3v4ExtRuleFragments,
       "aclL3v4ExtRuleICMPMessageType": aclL3v4ExtRuleICMPMessageType,
       "aclL3v4ExtRuleICMPMessageCode": aclL3v4ExtRuleICMPMessageCode,
       "aclL3v4ExtRuleDstIpAddr": aclL3v4ExtRuleDstIpAddr,
       "aclL3v4ExtRuleSrcIpAddr": aclL3v4ExtRuleSrcIpAddr,
       "aclL3v4ExtRuleDstIpAddrMask": aclL3v4ExtRuleDstIpAddrMask,
       "aclL3v4ExtRuleSrcIpAddrMask": aclL3v4ExtRuleSrcIpAddrMask,
       "aclL3v4ExtRuleTcpUdpDstOperator": aclL3v4ExtRuleTcpUdpDstOperator,
       "aclL3v4ExtRuleTcpUdpDstPort": aclL3v4ExtRuleTcpUdpDstPort,
       "aclL3v4ExtRuleTcpUdpMinDstPort": aclL3v4ExtRuleTcpUdpMinDstPort,
       "aclL3v4ExtRuleTcpUdpMaxDstPort": aclL3v4ExtRuleTcpUdpMaxDstPort,
       "aclL3v4ExtRuleTcpUdpSrcOperator": aclL3v4ExtRuleTcpUdpSrcOperator,
       "aclL3v4ExtRuleTcpUdpSrcPort": aclL3v4ExtRuleTcpUdpSrcPort,
       "aclL3v4ExtRuleTcpUdpMinSrcPort": aclL3v4ExtRuleTcpUdpMinSrcPort,
       "aclL3v4ExtRuleTcpUdpMaxSrcPort": aclL3v4ExtRuleTcpUdpMaxSrcPort,
       "aclL3v4ExtRuleIPPrecedence": aclL3v4ExtRuleIPPrecedence,
       "aclL3v4ExtRuleDscp": aclL3v4ExtRuleDscp,
       "aclL3v4ExtRuleToS": aclL3v4ExtRuleToS,
       "aclL3v4ExtRuleTcpAckBit": aclL3v4ExtRuleTcpAckBit,
       "aclL3v4ExtRuleTcpRstBit": aclL3v4ExtRuleTcpRstBit,
       "aclL3v4ExtRuleTcpUrgBit": aclL3v4ExtRuleTcpUrgBit,
       "aclL3v4ExtRuleTcpPshBit": aclL3v4ExtRuleTcpPshBit,
       "aclL3v4ExtRuleTcpSynBit": aclL3v4ExtRuleTcpSynBit,
       "aclL3v4ExtRuleTcpFinBit": aclL3v4ExtRuleTcpFinBit,
       "aclL3v4ExtRuleAction": aclL3v4ExtRuleAction,
       "aclL3v4ExtRuleTimeRange": aclL3v4ExtRuleTimeRange,
       "aclL3v4ExtRuleMatchCount": aclL3v4ExtRuleMatchCount,
       "aclL3v4ExtRuleStatus": aclL3v4ExtRuleStatus,
       "aclL3v6Rule": aclL3v6Rule,
       "aclL3v6RuleTable": aclL3v6RuleTable,
       "aclL3v6RuleEntry": aclL3v6RuleEntry,
       "aclL3v6RuleProfileNo": aclL3v6RuleProfileNo,
       "aclL3v6RuleAccessID": aclL3v6RuleAccessID,
       "aclL3v6RuleDstIpv6Addr": aclL3v6RuleDstIpv6Addr,
       "aclL3v6RuleSrcIpv6Addr": aclL3v6RuleSrcIpv6Addr,
       "aclL3v6RuleDstIpv6AddrPrefixLen": aclL3v6RuleDstIpv6AddrPrefixLen,
       "aclL3v6RuleSrcIpv6AddrPrefixLen": aclL3v6RuleSrcIpv6AddrPrefixLen,
       "aclL3v6RuleAction": aclL3v6RuleAction,
       "aclL3v6RuleTimeRange": aclL3v6RuleTimeRange,
       "aclL3v6RuleMatchCount": aclL3v6RuleMatchCount,
       "aclL3v6RuleStatus": aclL3v6RuleStatus,
       "aclL3v6ExtRule": aclL3v6ExtRule,
       "aclL3v6ExtRuleTable": aclL3v6ExtRuleTable,
       "aclL3v6ExtRuleEntry": aclL3v6ExtRuleEntry,
       "aclL3v6ExtRuleProfileNo": aclL3v6ExtRuleProfileNo,
       "aclL3v6ExtRuleAccessID": aclL3v6ExtRuleAccessID,
       "aclL3v6ExtRuleDscp": aclL3v6ExtRuleDscp,
       "aclL3v6ExtRuleProtocol": aclL3v6ExtRuleProtocol,
       "aclL3v6ExtRuleFragments": aclL3v6ExtRuleFragments,
       "aclL3v6ExtRuleTcpUdpDstOperator": aclL3v6ExtRuleTcpUdpDstOperator,
       "aclL3v6ExtRuleTcpUdpDstPort": aclL3v6ExtRuleTcpUdpDstPort,
       "aclL3v6ExtRuleTcpUdpMinDstPort": aclL3v6ExtRuleTcpUdpMinDstPort,
       "aclL3v6ExtRuleTcpUdpMaxDstPort": aclL3v6ExtRuleTcpUdpMaxDstPort,
       "aclL3v6ExtRuleTcpUdpSrcOperator": aclL3v6ExtRuleTcpUdpSrcOperator,
       "aclL3v6ExtRuleTcpUdpSrcPort": aclL3v6ExtRuleTcpUdpSrcPort,
       "aclL3v6ExtRuleTcpUdpMinSrcPort": aclL3v6ExtRuleTcpUdpMinSrcPort,
       "aclL3v6ExtRuleTcpUdpMaxSrcPort": aclL3v6ExtRuleTcpUdpMaxSrcPort,
       "aclL3v6ExtRuleICMPv6MessageType": aclL3v6ExtRuleICMPv6MessageType,
       "aclL3v6ExtRuleICMPv6MessageCode": aclL3v6ExtRuleICMPv6MessageCode,
       "aclL3v6ExtRuleDstIpv6Addr": aclL3v6ExtRuleDstIpv6Addr,
       "aclL3v6ExtRuleSrcIpv6Addr": aclL3v6ExtRuleSrcIpv6Addr,
       "aclL3v6ExtRuleDstIpv6AddrPrefixLen": aclL3v6ExtRuleDstIpv6AddrPrefixLen,
       "aclL3v6ExtRuleSrcIpv6AddrPrefixLen": aclL3v6ExtRuleSrcIpv6AddrPrefixLen,
       "aclL3v6ExtRuleTcpAckBit": aclL3v6ExtRuleTcpAckBit,
       "aclL3v6ExtRuleTcpRstBit": aclL3v6ExtRuleTcpRstBit,
       "aclL3v6ExtRuleTcpUrgBit": aclL3v6ExtRuleTcpUrgBit,
       "aclL3v6ExtRuleTcpPshBit": aclL3v6ExtRuleTcpPshBit,
       "aclL3v6ExtRuleTcpSynBit": aclL3v6ExtRuleTcpSynBit,
       "aclL3v6ExtRuleTcpFinBit": aclL3v6ExtRuleTcpFinBit,
       "aclL3v6ExtRuleFlowLabel": aclL3v6ExtRuleFlowLabel,
       "aclL3v6ExtRuleAction": aclL3v6ExtRuleAction,
       "aclL3v6ExtRuleTimeRange": aclL3v6ExtRuleTimeRange,
       "aclL3v6ExtRuleMatchCount": aclL3v6ExtRuleMatchCount,
       "aclL3v6ExtRuleStatus": aclL3v6ExtRuleStatus,
       "aclExpertExtRule": aclExpertExtRule,
       "aclExpertExtRuleTable": aclExpertExtRuleTable,
       "aclExpertExtRuleEntry": aclExpertExtRuleEntry,
       "aclExpertExtRuleProfileNo": aclExpertExtRuleProfileNo,
       "aclExpertExtRuleAccessID": aclExpertExtRuleAccessID,
       "aclExpertExtRuleProtocol": aclExpertExtRuleProtocol,
       "aclExpertExtRuleFragments": aclExpertExtRuleFragments,
       "aclExpertExtRuleICMPMessageType": aclExpertExtRuleICMPMessageType,
       "aclExpertExtRuleICMPMessageCode": aclExpertExtRuleICMPMessageCode,
       "aclExpertExtRuleDstIpAddr": aclExpertExtRuleDstIpAddr,
       "aclExpertExtRuleSrcIpAddr": aclExpertExtRuleSrcIpAddr,
       "aclExpertExtRuleDstIpAddrMask": aclExpertExtRuleDstIpAddrMask,
       "aclExpertExtRuleSrcIpAddrMask": aclExpertExtRuleSrcIpAddrMask,
       "aclExpertExtRuleTcpUdpDstOperator": aclExpertExtRuleTcpUdpDstOperator,
       "aclExpertExtRuleTcpUdpDstPort": aclExpertExtRuleTcpUdpDstPort,
       "aclExpertExtRuleTcpUdpMinDstPort": aclExpertExtRuleTcpUdpMinDstPort,
       "aclExpertExtRuleTcpUdpMaxDstPort": aclExpertExtRuleTcpUdpMaxDstPort,
       "aclExpertExtRuleTcpUdpSrcOperator": aclExpertExtRuleTcpUdpSrcOperator,
       "aclExpertExtRuleTcpUdpSrcPort": aclExpertExtRuleTcpUdpSrcPort,
       "aclExpertExtRuleTcpUdpMinSrcPort": aclExpertExtRuleTcpUdpMinSrcPort,
       "aclExpertExtRuleTcpUdpMaxSrcPort": aclExpertExtRuleTcpUdpMaxSrcPort,
       "aclExpertExtRuleIPPrecedence": aclExpertExtRuleIPPrecedence,
       "aclExpertExtRuleDscp": aclExpertExtRuleDscp,
       "aclExpertExtRuleToS": aclExpertExtRuleToS,
       "aclExpertExtRuleTcpAckBit": aclExpertExtRuleTcpAckBit,
       "aclExpertExtRuleTcpRstBit": aclExpertExtRuleTcpRstBit,
       "aclExpertExtRuleTcpUrgBit": aclExpertExtRuleTcpUrgBit,
       "aclExpertExtRuleTcpPshBit": aclExpertExtRuleTcpPshBit,
       "aclExpertExtRuleTcpSynBit": aclExpertExtRuleTcpSynBit,
       "aclExpertExtRuleTcpFinBit": aclExpertExtRuleTcpFinBit,
       "aclExpertExtRuleDstMacAddr": aclExpertExtRuleDstMacAddr,
       "aclExpertExtRuleSrcMacAddr": aclExpertExtRuleSrcMacAddr,
       "aclExpertExtRuleVlanId": aclExpertExtRuleVlanId,
       "aclExpertExtRule1pPriority": aclExpertExtRule1pPriority,
       "aclExpertExtRuleDstMacAddrMask": aclExpertExtRuleDstMacAddrMask,
       "aclExpertExtRuleSrcMacAddrMask": aclExpertExtRuleSrcMacAddrMask,
       "aclExpertExtRuleAction": aclExpertExtRuleAction,
       "aclExpertExtRuleTimeRange": aclExpertExtRuleTimeRange,
       "aclExpertExtRuleMatchCount": aclExpertExtRuleMatchCount,
       "aclExpertExtRuleStatus": aclExpertExtRuleStatus,
       "aclPortBindGroup": aclPortBindGroup,
       "aclPortGroupTable": aclPortGroupTable,
       "aclPortGroupEntry": aclPortGroupEntry,
       "aclPortIndex": aclPortIndex,
       "aclPortDirection": aclPortDirection,
       "aclPortL2ProfileNo": aclPortL2ProfileNo,
       "aclPortL3v4StdProfileNo": aclPortL3v4StdProfileNo,
       "aclPortL3v4ExtProfileNo": aclPortL3v4ExtProfileNo,
       "aclPortL3v6StdProfileNo": aclPortL3v6StdProfileNo,
       "aclPortL3v6ExtProfileNo": aclPortL3v6ExtProfileNo,
       "aclPortExpertProfileNo": aclPortExpertProfileNo,
       "dlinkSecurity": dlinkSecurity,
       "securityportSecurityGroup": securityportSecurityGroup,
       "portSecurityGlobalSettings": portSecurityGlobalSettings,
       "portSecurityTrapState": portSecurityTrapState,
       "portSecurityTrapRate": portSecurityTrapRate,
       "portSecuritySysMaxAddr": portSecuritySysMaxAddr,
       "portSecurityPortSettings": portSecurityPortSettings,
       "portSecurityTable": portSecurityTable,
       "portSecurityEntry": portSecurityEntry,
       "portSecurityPort": portSecurityPort,
       "portSecurityState": portSecurityState,
       "portSecuritySysMax": portSecuritySysMax,
       "portSecurityVioAction": portSecurityVioAction,
       "portSecuritySecurMode": portSecuritySecurMode,
       "portSecurityAgingTime": portSecurityAgingTime,
       "portSecurityAgingType": portSecurityAgingType,
       "portSecurityCurrentNo": portSecurityCurrentNo,
       "portSecurityVioCount": portSecurityVioCount,
       "portSecurityCurState": portSecurityCurState,
       "portSecurityAddressEntries": portSecurityAddressEntries,
       "portSecAddrTable": portSecAddrTable,
       "portSecAddrEntry": portSecAddrEntry,
       "portSecAddrVID": portSecAddrVID,
       "portSecAddrMAC": portSecAddrMAC,
       "portSecAddrPort": portSecAddrPort,
       "portSecAddrType": portSecAddrType,
       "portSecAddrRowStatus": portSecAddrRowStatus,
       "portSecAddrRemainTime": portSecAddrRemainTime,
       "portSecurityTraps": portSecurityTraps,
       "portSecurityTrapList": portSecurityTrapList,
       "portSecurityViolation": portSecurityViolation,
       "securityDhcpSerScrGroup": securityDhcpSerScrGroup,
       "dhcpSerScrGlobSettings": dhcpSerScrGlobSettings,
       "dhcpSerScrGlobTrapState": dhcpSerScrGlobTrapState,
       "dhcpSerScrLogBufEntries": dhcpSerScrLogBufEntries,
       "dhcpSerScrLogClear": dhcpSerScrLogClear,
       "dhcpSerScrProfileTable": dhcpSerScrProfileTable,
       "dhcpSerScrProfileEntry": dhcpSerScrProfileEntry,
       "dhcpSerScrProfileName": dhcpSerScrProfileName,
       "dhcpSerScrProfileClientMac": dhcpSerScrProfileClientMac,
       "dhcpSerScrProfileRowStatus": dhcpSerScrProfileRowStatus,
       "dhcpSerScrLogTable": dhcpSerScrLogTable,
       "dhcpSerScrLogEntry": dhcpSerScrLogEntry,
       "dhcpSerScrLogIndex": dhcpSerScrLogIndex,
       "dhcpSerScrLogVlanID": dhcpSerScrLogVlanID,
       "dhcpSerScrLogIPAddr": dhcpSerScrLogIPAddr,
       "dhcpSerScrLogMacAddr": dhcpSerScrLogMacAddr,
       "dhcpSerScrLogOccurrence": dhcpSerScrLogOccurrence,
       "dhcpSerScrPortSettings": dhcpSerScrPortSettings,
       "dhcpSerScrPortTable": dhcpSerScrPortTable,
       "dhcpSerScrPortEntry": dhcpSerScrPortEntry,
       "dhcpSerScrPortIndex": dhcpSerScrPortIndex,
       "dhcpSerScrPortState": dhcpSerScrPortState,
       "dhcpSerScrPortServerAddrType": dhcpSerScrPortServerAddrType,
       "dhcpSerScrPortServerIP": dhcpSerScrPortServerIP,
       "dhcpSerScrPortProfileName": dhcpSerScrPortProfileName,
       "dhcpSerScrTraps": dhcpSerScrTraps,
       "dhcpSerScrTrapList": dhcpSerScrTrapList,
       "dhcpSerScrAttackDetect": dhcpSerScrAttackDetect,
       "securitySafeGuardGroup": securitySafeGuardGroup,
       "safeGuardEnable": safeGuardEnable,
       "securityTrustedHostGroup": securityTrustedHostGroup,
       "trustedHostTable": trustedHostTable,
       "trustedHostEntry": trustedHostEntry,
       "trustedHostType": trustedHostType,
       "trustedHostACLName": trustedHostACLName,
       "trustedHostRowStatus": trustedHostRowStatus,
       "securityTrafficSegmentationGroup": securityTrafficSegmentationGroup,
       "trafficSegmentationTable": trafficSegmentationTable,
       "trafficSegmentationEntry": trafficSegmentationEntry,
       "trafficSegmentationIfIndex": trafficSegmentationIfIndex,
       "trafficSegmentationMemberList": trafficSegmentationMemberList,
       "securityStormCtrlGroup": securityStormCtrlGroup,
       "stormCtrlMIBObjects": stormCtrlMIBObjects,
       "stormCtrlGentrl": stormCtrlGentrl,
       "stormCtrlNotifyEnable": stormCtrlNotifyEnable,
       "stormCtrlPollingInterval": stormCtrlPollingInterval,
       "stormCtrlPollingRetries": stormCtrlPollingRetries,
       "stormCtrlTable": stormCtrlTable,
       "stormCtrlEntry": stormCtrlEntry,
       "stormCtrlIndex": stormCtrlIndex,
       "stormCtrlActionMode": stormCtrlActionMode,
       "stormCtrlLevelType": stormCtrlLevelType,
       "stormCtrlThresholdTable": stormCtrlThresholdTable,
       "stormCtrlThresholdEntry": stormCtrlThresholdEntry,
       "stormCtrlThresholdIndex": stormCtrlThresholdIndex,
       "stormCtrlThresholdType": stormCtrlThresholdType,
       "stormCtrlThresholdRiseThre": stormCtrlThresholdRiseThre,
       "stormCtrlThresholdLowThre": stormCtrlThresholdLowThre,
       "stormCtrlThresholdCurrRate": stormCtrlThresholdCurrRate,
       "stormCtrlThresholdStormState": stormCtrlThresholdStormState,
       "stormCtrlTraps": stormCtrlTraps,
       "stormCtrlTrapsList": stormCtrlTrapsList,
       "stormCtrlTrapsStormOccur": stormCtrlTrapsStormOccur,
       "stormCtrlTrapsStormClear": stormCtrlTrapsStormClear,
       "securityDoSprevGroup": securityDoSprevGroup,
       "doSCtrlTable": doSCtrlTable,
       "doSCtrlEntry": doSCtrlEntry,
       "doSCtrlType": doSCtrlType,
       "doSCtrlState": doSCtrlState,
       "doSCtrlActionType": doSCtrlActionType,
       "securitySSLGroup": securitySSLGroup,
       "sslObjects": sslObjects,
       "sslServerStatus": sslServerStatus,
       "servicePolicyName": servicePolicyName,
       "sslConfiguration": sslConfiguration,
       "sslServicePolicyTable": sslServicePolicyTable,
       "sslServicePolicyEntry": sslServicePolicyEntry,
       "sslServicePolicyName": sslServicePolicyName,
       "sslServicePolicyCipherSuites": sslServicePolicyCipherSuites,
       "sslServicePolicyCacheTimeout": sslServicePolicyCacheTimeout,
       "sslServicePolicyRowStatus": sslServicePolicyRowStatus,
       "dlinkOAM": dlinkOAM,
       "oamCableDiagGroup": oamCableDiagGroup,
       "cableDiagTriggerIndex": cableDiagTriggerIndex,
       "cableDiagTestPairTable": cableDiagTestPairTable,
       "cableDiagTestPairEntry": cableDiagTestPairEntry,
       "cableDiagTestPortPair": cableDiagTestPortPair,
       "cableDiagTestResultPair1": cableDiagTestResultPair1,
       "cableDiagTestResultPair2": cableDiagTestResultPair2,
       "cableDiagTestResultPair3": cableDiagTestResultPair3,
       "cableDiagTestResultPair4": cableDiagTestResultPair4,
       "cableDiagTestLenPair1": cableDiagTestLenPair1,
       "cableDiagTestLenPair2": cableDiagTestLenPair2,
       "cableDiagTestLenPair3": cableDiagTestLenPair3,
       "cableDiagTestLenPair4": cableDiagTestLenPair4,
       "cableDiagTestLenPairClear": cableDiagTestLenPairClear,
       "dlinkMonitoring": dlinkMonitoring,
       "monStatisticsGroup": monStatisticsGroup,
       "statisticsCounters": statisticsCounters,
       "statisticsCountersTable": statisticsCountersTable,
       "statisticsCountersEntry": statisticsCountersEntry,
       "statPort": statPort,
       "statPortRxRateBytes": statPortRxRateBytes,
       "statPortRxRatePackets": statPortRxRatePackets,
       "statPortRxTotalBytes": statPortRxTotalBytes,
       "statPortRxTotalPackets": statPortRxTotalPackets,
       "statPortTxRateBytes": statPortTxRateBytes,
       "statPortTxRatePackets": statPortTxRatePackets,
       "statPortTxTotalBytes": statPortTxTotalBytes,
       "statPortTxTotalPackets": statPortTxTotalPackets,
       "statPortRxMulticast": statPortRxMulticast,
       "statPortRxUnicast": statPortRxUnicast,
       "statPortRxBroadcast": statPortRxBroadcast,
       "statPortTxMulticast": statPortTxMulticast,
       "statPortTxUnicast": statPortTxUnicast,
       "statPortTxBroadcast": statPortTxBroadcast,
       "statCountersrxHCPkt64Octets": statCountersrxHCPkt64Octets,
       "statCountersrxHCPkt65to127Octets": statCountersrxHCPkt65to127Octets,
       "statCountersrxHCPkt128to255Octets": statCountersrxHCPkt128to255Octets,
       "statCountersrxHCPkt256to511Octets": statCountersrxHCPkt256to511Octets,
       "statCountersrxHCPkt512to1023Octets": statCountersrxHCPkt512to1023Octets,
       "statCountersrxHCPkt1024to1518Octets": statCountersrxHCPkt1024to1518Octets,
       "statCountersrxHCPkt1519to2047Octets": statCountersrxHCPkt1519to2047Octets,
       "statCountersrxHCPkt2048to4095Octets": statCountersrxHCPkt2048to4095Octets,
       "statCountersrxHCPkt4096to9216Octets": statCountersrxHCPkt4096to9216Octets,
       "statCounterstxHCPkt64Octets": statCounterstxHCPkt64Octets,
       "statCounterstxHCPkt65to127Octets": statCounterstxHCPkt65to127Octets,
       "statCounterstxHCPkt128to255Octets": statCounterstxHCPkt128to255Octets,
       "statCounterstxHCPkt256to511Octets": statCounterstxHCPkt256to511Octets,
       "statCounterstxHCPkt512to1023Octets": statCounterstxHCPkt512to1023Octets,
       "statCounterstxHCPkt1024to1518Octets": statCounterstxHCPkt1024to1518Octets,
       "statCounterstxHCPkt1519to2047Octets": statCounterstxHCPkt1519to2047Octets,
       "statCounterstxHCPkt2048to4095Octets": statCounterstxHCPkt2048to4095Octets,
       "statCounterstxHCPkt4096to9216Octets": statCounterstxHCPkt4096to9216Octets,
       "statisticsErrorCounters": statisticsErrorCounters,
       "statisticsErrorTable": statisticsErrorTable,
       "statisticsErrorEntry": statisticsErrorEntry,
       "statPortCountPort": statPortCountPort,
       "statCountersrxDroppkts": statCountersrxDroppkts,
       "statCountersrxMTUDropPkts": statCountersrxMTUDropPkts,
       "statPortCountDeferredTx": statPortCountDeferredTx,
       "statCountersdot3StatsSingleColFrames": statCountersdot3StatsSingleColFrames,
       "statPortCountExcessCol": statPortCountExcessCol,
       "statPortCountLateCol": statPortCountLateCol,
       "statPortCountAlignErr": statPortCountAlignErr,
       "statPortCountFCSErr": statPortCountFCSErr,
       "statCountersifOutDiscards": statCountersifOutDiscards,
       "statPortCountMultiCol": statPortCountMultiCol,
       "statPortCountCarriSen": statPortCountCarriSen,
       "statPortCountSQETestErr": statPortCountSQETestErr,
       "statCountersdot3StatsDeferredTransmisions": statCountersdot3StatsDeferredTransmisions,
       "statPortCountIntMacTx": statPortCountIntMacTx,
       "statPortCountIntMacRx": statPortCountIntMacRx,
       "statCountersrxCRCAlignErrors": statCountersrxCRCAlignErrors,
       "statCountersrxUndersizedPkts": statCountersrxUndersizedPkts,
       "statCountersrxOversizedPkts": statCountersrxOversizedPkts,
       "statCountersrxFragmentPkts": statCountersrxFragmentPkts,
       "statCountersrxJabbers": statCountersrxJabbers,
       "statCountersrxSymbolErrors": statCountersrxSymbolErrors,
       "statCountersrxMulticastDropPkts": statCountersrxMulticastDropPkts,
       "statCountersifInErrors": statCountersifInErrors,
       "statCountersifOutErrors": statCountersifOutErrors,
       "statCountersifInDiscards": statCountersifInDiscards,
       "statCountersifInUnknownProtos": statCountersifInUnknownProtos,
       "statCounterstxDelayExceededDiscards": statCounterstxDelayExceededDiscards,
       "statisticsClear": statisticsClear,
       "statisticsCounterClearTable": statisticsCounterClearTable,
       "statisticsCounterClearEntry": statisticsCounterClearEntry,
       "statCounterClearIndex": statCounterClearIndex,
       "statCounterClearStatus": statCounterClearStatus,
       "statCounterLinkChange": statCounterLinkChange,
       "monMirrorGroup": monMirrorGroup,
       "mirrorSessionTable": mirrorSessionTable,
       "mirrorSessionEntry": mirrorSessionEntry,
       "mirrorSessionNumber": mirrorSessionNumber,
       "mirrorDestinationPort": mirrorDestinationPort,
       "mirrorSourceIngressPort": mirrorSourceIngressPort,
       "mirrorSourceEgressPort": mirrorSourceEgressPort,
       "mirrorSessionRowStatus": mirrorSessionRowStatus,
       "dlinkGreen": dlinkGreen,
       "dlinkPowersavingGroup": dlinkPowersavingGroup,
       "powerSavingGlobalSettings": powerSavingGlobalSettings,
       "psgFunctionVersion": psgFunctionVersion,
       "psgScheduledPortShutdown": psgScheduledPortShutdown,
       "psgScheduledHibernation": psgScheduledHibernation,
       "psgScheduledDimLED": psgScheduledDimLED,
       "psgAdministrativeDimLED": psgAdministrativeDimLED,
       "powerSavingTimeRangeSettings": powerSavingTimeRangeSettings,
       "psgDimLEDShutOffTimeProfile": psgDimLEDShutOffTimeProfile,
       "psgHibernationTimeProfile": psgHibernationTimeProfile,
       "powerSavingShutdownSettings": powerSavingShutdownSettings,
       "powerSavingShutdownTable": powerSavingShutdownTable,
       "powerSavingShutdownEntry": powerSavingShutdownEntry,
       "psShutdownPort": psShutdownPort,
       "psShutdownTimeRange": psShutdownTimeRange,
       "dlinkEEEGroup": dlinkEEEGroup,
       "greenEeeTable": greenEeeTable,
       "greenEeeEntry": greenEeeEntry,
       "eeePort": eeePort,
       "eeestate": eeestate}
)
