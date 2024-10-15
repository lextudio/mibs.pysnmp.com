# SNMP MIB module (AIRPORT-BASESTATION-3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AIRPORT-BASESTATION-3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:17 2024
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

baseStation3 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 63, 501, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Apple_ObjectIdentity = ObjectIdentity
apple = _Apple_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 63)
)
_Airport_ObjectIdentity = ObjectIdentity
airport = _Airport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 63, 501)
)
_Abs3SysConf_ObjectIdentity = ObjectIdentity
abs3SysConf = _Abs3SysConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 63, 501, 3, 1)
)
_SysConfName_Type = DisplayString
_SysConfName_Object = MibScalar
sysConfName = _SysConfName_Object(
    (1, 3, 6, 1, 4, 1, 63, 501, 3, 1, 1),
    _SysConfName_Type()
)
sysConfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfName.setStatus("current")
_SysConfContact_Type = DisplayString
_SysConfContact_Object = MibScalar
sysConfContact = _SysConfContact_Object(
    (1, 3, 6, 1, 4, 1, 63, 501, 3, 1, 2),
    _SysConfContact_Type()
)
sysConfContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfContact.setStatus("current")
_SysConfLocation_Type = DisplayString
_SysConfLocation_Object = MibScalar
sysConfLocation = _SysConfLocation_Object(
    (1, 3, 6, 1, 4, 1, 63, 501, 3, 1, 3),
    _SysConfLocation_Type()
)
sysConfLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfLocation.setStatus("current")
_SysConfUptime_Type = Integer32
_SysConfUptime_Object = MibScalar
sysConfUptime = _SysConfUptime_Object(
    (1, 3, 6, 1, 4, 1, 63, 501, 3, 1, 4),
    _SysConfUptime_Type()
)
sysConfUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysConfUptime.setStatus("current")
_SysConfFirmwareVersion_Type = DisplayString
_SysConfFirmwareVersion_Object = MibScalar
sysConfFirmwareVersion = _SysConfFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 63, 501, 3, 1, 5),
    _SysConfFirmwareVersion_Type()
)
sysConfFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysConfFirmwareVersion.setStatus("current")
_Wireless_ObjectIdentity = ObjectIdentity
wireless = _Wireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 63, 501, 3, 2)
)
_WirelessNumber_Type = Integer32
_WirelessNumber_Object = MibScalar
wirelessNumber = _WirelessNumber_Object(
    (1, 3, 6, 1, 4, 1, 63, 501, 3, 2, 1),
    _WirelessNumber_Type()
)
wirelessNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessNumber.setStatus("current")
_WirelessClientsTable_Object = MibTable
wirelessClientsTable = _WirelessClientsTable_Object(
    (1, 3, 6, 1, 4, 1, 63, 501, 3, 2, 2)
)
if mibBuilder.loadTexts:
    wirelessClientsTable.setStatus("current")
_WirelessClient_Object = MibTableRow
wirelessClient = _WirelessClient_Object(
    (1, 3, 6, 1, 4, 1, 63, 501, 3, 2, 2, 1)
)
wirelessClient.setIndexNames(
    (0, "AIRPORT-BASESTATION-3-MIB", "wirelessPhysAddress"),
)
if mibBuilder.loadTexts:
    wirelessClient.setStatus("current")
_WirelessPhysAddress_Type = PhysAddress
_WirelessPhysAddress_Object = MibTableColumn
wirelessPhysAddress = _WirelessPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 63, 501, 3, 2, 2, 1, 1),
    _WirelessPhysAddress_Type()
)
wirelessPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessPhysAddress.setStatus("current")


class _WirelessType_Type(Integer32):
    """Custom type wirelessType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sta", 1),
          ("wds", 2))
    )


_WirelessType_Type.__name__ = "Integer32"
_WirelessType_Object = MibTableColumn
wirelessType = _WirelessType_Object(
    (1, 3, 6, 1, 4, 1, 63, 501, 3, 2, 2, 1, 2),
    _WirelessType_Type()
)
wirelessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessType.setStatus("current")
_WirelessDataRates_Type = DisplayString
_WirelessDataRates_Object = MibTableColumn
wirelessDataRates = _WirelessDataRates_Object(
    (1, 3, 6, 1, 4, 1, 63, 501, 3, 2, 2, 1, 3),
    _WirelessDataRates_Type()
)
wirelessDataRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessDataRates.setStatus("current")
_WirelessTimeAssociated_Type = Integer32
_WirelessTimeAssociated_Object = MibTableColumn
wirelessTimeAssociated = _WirelessTimeAssociated_Object(
    (1, 3, 6, 1, 4, 1, 63, 501, 3, 2, 2, 1, 4),
    _WirelessTimeAssociated_Type()
)
wirelessTimeAssociated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessTimeAssociated.setStatus("current")
_WirelessLastRefreshTime_Type = Integer32
_WirelessLastRefreshTime_Object = MibTableColumn
wirelessLastRefreshTime = _WirelessLastRefreshTime_Object(
    (1, 3, 6, 1, 4, 1, 63, 501, 3, 2, 2, 1, 5),
    _WirelessLastRefreshTime_Type()
)
wirelessLastRefreshTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLastRefreshTime.setStatus("current")
_WirelessStrength_Type = Integer32
_WirelessStrength_Object = MibTableColumn
wirelessStrength = _WirelessStrength_Object(
    (1, 3, 6, 1, 4, 1, 63, 501, 3, 2, 2, 1, 6),
    _WirelessStrength_Type()
)
wirelessStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessStrength.setStatus("current")
_WirelessNoise_Type = Integer32
_WirelessNoise_Object = MibTableColumn
wirelessNoise = _WirelessNoise_Object(
    (1, 3, 6, 1, 4, 1, 63, 501, 3, 2, 2, 1, 7),
    _WirelessNoise_Type()
)
wirelessNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessNoise.setStatus("current")
_WirelessRate_Type = Integer32
_WirelessRate_Object = MibTableColumn
wirelessRate = _WirelessRate_Object(
    (1, 3, 6, 1, 4, 1, 63, 501, 3, 2, 2, 1, 8),
    _WirelessRate_Type()
)
wirelessRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessRate.setStatus("current")
_WirelessNumRX_Type = Integer32
_WirelessNumRX_Object = MibTableColumn
wirelessNumRX = _WirelessNumRX_Object(
    (1, 3, 6, 1, 4, 1, 63, 501, 3, 2, 2, 1, 9),
    _WirelessNumRX_Type()
)
wirelessNumRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessNumRX.setStatus("current")
_WirelessNumTX_Type = Integer32
_WirelessNumTX_Object = MibTableColumn
wirelessNumTX = _WirelessNumTX_Object(
    (1, 3, 6, 1, 4, 1, 63, 501, 3, 2, 2, 1, 10),
    _WirelessNumTX_Type()
)
wirelessNumTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessNumTX.setStatus("current")
_WirelessNumRXErrors_Type = Integer32
_WirelessNumRXErrors_Object = MibTableColumn
wirelessNumRXErrors = _WirelessNumRXErrors_Object(
    (1, 3, 6, 1, 4, 1, 63, 501, 3, 2, 2, 1, 11),
    _WirelessNumRXErrors_Type()
)
wirelessNumRXErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessNumRXErrors.setStatus("current")
_WirelessNumTXErrors_Type = Integer32
_WirelessNumTXErrors_Object = MibTableColumn
wirelessNumTXErrors = _WirelessNumTXErrors_Object(
    (1, 3, 6, 1, 4, 1, 63, 501, 3, 2, 2, 1, 12),
    _WirelessNumTXErrors_Type()
)
wirelessNumTXErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessNumTXErrors.setStatus("current")
_DhcpServer_ObjectIdentity = ObjectIdentity
dhcpServer = _DhcpServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 63, 501, 3, 3)
)
_DhcpNumber_Type = Integer32
_DhcpNumber_Object = MibScalar
dhcpNumber = _DhcpNumber_Object(
    (1, 3, 6, 1, 4, 1, 63, 501, 3, 3, 1),
    _DhcpNumber_Type()
)
dhcpNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpNumber.setStatus("current")
_DhcpClientsTable_Object = MibTable
dhcpClientsTable = _DhcpClientsTable_Object(
    (1, 3, 6, 1, 4, 1, 63, 501, 3, 3, 2)
)
if mibBuilder.loadTexts:
    dhcpClientsTable.setStatus("current")
_DhcpClient_Object = MibTableRow
dhcpClient = _DhcpClient_Object(
    (1, 3, 6, 1, 4, 1, 63, 501, 3, 3, 2, 1)
)
dhcpClient.setIndexNames(
    (0, "AIRPORT-BASESTATION-3-MIB", "dhcpPhysAddress"),
)
if mibBuilder.loadTexts:
    dhcpClient.setStatus("current")
_DhcpPhysAddress_Type = PhysAddress
_DhcpPhysAddress_Object = MibTableColumn
dhcpPhysAddress = _DhcpPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 63, 501, 3, 3, 2, 1, 1),
    _DhcpPhysAddress_Type()
)
dhcpPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPhysAddress.setStatus("current")
_DhcpIpAddress_Type = IpAddress
_DhcpIpAddress_Object = MibTableColumn
dhcpIpAddress = _DhcpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 63, 501, 3, 3, 2, 1, 2),
    _DhcpIpAddress_Type()
)
dhcpIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpIpAddress.setStatus("current")
_DhcpClientID_Type = OctetString
_DhcpClientID_Object = MibTableColumn
dhcpClientID = _DhcpClientID_Object(
    (1, 3, 6, 1, 4, 1, 63, 501, 3, 3, 2, 1, 3),
    _DhcpClientID_Type()
)
dhcpClientID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpClientID.setStatus("current")
_DhcpLeaseTime_Type = Integer32
_DhcpLeaseTime_Object = MibTableColumn
dhcpLeaseTime = _DhcpLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 63, 501, 3, 3, 2, 1, 4),
    _DhcpLeaseTime_Type()
)
dhcpLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpLeaseTime.setStatus("current")
_PhysicalInterfaces_ObjectIdentity = ObjectIdentity
physicalInterfaces = _PhysicalInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 63, 501, 3, 4)
)
_PhysicalInterfaceCount_Type = Integer32
_PhysicalInterfaceCount_Object = MibScalar
physicalInterfaceCount = _PhysicalInterfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 63, 501, 3, 4, 1),
    _PhysicalInterfaceCount_Type()
)
physicalInterfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalInterfaceCount.setStatus("current")
_PhysicalInterfacesTable_Object = MibTable
physicalInterfacesTable = _PhysicalInterfacesTable_Object(
    (1, 3, 6, 1, 4, 1, 63, 501, 3, 4, 2)
)
if mibBuilder.loadTexts:
    physicalInterfacesTable.setStatus("current")
_PhysicalInterface_Object = MibTableRow
physicalInterface = _PhysicalInterface_Object(
    (1, 3, 6, 1, 4, 1, 63, 501, 3, 4, 2, 1)
)
physicalInterface.setIndexNames(
    (0, "AIRPORT-BASESTATION-3-MIB", "physicalInterfaceIndex"),
)
if mibBuilder.loadTexts:
    physicalInterface.setStatus("current")
_PhysicalInterfaceIndex_Type = Integer32
_PhysicalInterfaceIndex_Object = MibTableColumn
physicalInterfaceIndex = _PhysicalInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 63, 501, 3, 4, 2, 1, 1),
    _PhysicalInterfaceIndex_Type()
)
physicalInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalInterfaceIndex.setStatus("current")
_PhysicalInterfaceName_Type = OctetString
_PhysicalInterfaceName_Object = MibTableColumn
physicalInterfaceName = _PhysicalInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 63, 501, 3, 4, 2, 1, 2),
    _PhysicalInterfaceName_Type()
)
physicalInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalInterfaceName.setStatus("current")
_PhysicalInterfaceUnit_Type = Integer32
_PhysicalInterfaceUnit_Object = MibTableColumn
physicalInterfaceUnit = _PhysicalInterfaceUnit_Object(
    (1, 3, 6, 1, 4, 1, 63, 501, 3, 4, 2, 1, 3),
    _PhysicalInterfaceUnit_Type()
)
physicalInterfaceUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalInterfaceUnit.setStatus("current")
_PhysicalInterfaceSpeed_Type = Integer32
_PhysicalInterfaceSpeed_Object = MibTableColumn
physicalInterfaceSpeed = _PhysicalInterfaceSpeed_Object(
    (1, 3, 6, 1, 4, 1, 63, 501, 3, 4, 2, 1, 4),
    _PhysicalInterfaceSpeed_Type()
)
physicalInterfaceSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalInterfaceSpeed.setStatus("current")


class _PhysicalInterfaceState_Type(Integer32):
    """Custom type physicalInterfaceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 0),
          ("linkUp", 1))
    )


_PhysicalInterfaceState_Type.__name__ = "Integer32"
_PhysicalInterfaceState_Object = MibTableColumn
physicalInterfaceState = _PhysicalInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 63, 501, 3, 4, 2, 1, 5),
    _PhysicalInterfaceState_Type()
)
physicalInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalInterfaceState.setStatus("current")


class _PhysicalInterfaceDuplex_Type(Integer32):
    """Custom type physicalInterfaceDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 0))
    )


_PhysicalInterfaceDuplex_Type.__name__ = "Integer32"
_PhysicalInterfaceDuplex_Object = MibTableColumn
physicalInterfaceDuplex = _PhysicalInterfaceDuplex_Object(
    (1, 3, 6, 1, 4, 1, 63, 501, 3, 4, 2, 1, 6),
    _PhysicalInterfaceDuplex_Type()
)
physicalInterfaceDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalInterfaceDuplex.setStatus("current")
_PhysicalInterfaceNumTX_Type = Integer32
_PhysicalInterfaceNumTX_Object = MibTableColumn
physicalInterfaceNumTX = _PhysicalInterfaceNumTX_Object(
    (1, 3, 6, 1, 4, 1, 63, 501, 3, 4, 2, 1, 7),
    _PhysicalInterfaceNumTX_Type()
)
physicalInterfaceNumTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalInterfaceNumTX.setStatus("current")
_PhysicalInterfaceNumRX_Type = Integer32
_PhysicalInterfaceNumRX_Object = MibTableColumn
physicalInterfaceNumRX = _PhysicalInterfaceNumRX_Object(
    (1, 3, 6, 1, 4, 1, 63, 501, 3, 4, 2, 1, 8),
    _PhysicalInterfaceNumRX_Type()
)
physicalInterfaceNumRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalInterfaceNumRX.setStatus("current")
_PhysicalInterfaceNumTXError_Type = Integer32
_PhysicalInterfaceNumTXError_Object = MibTableColumn
physicalInterfaceNumTXError = _PhysicalInterfaceNumTXError_Object(
    (1, 3, 6, 1, 4, 1, 63, 501, 3, 4, 2, 1, 9),
    _PhysicalInterfaceNumTXError_Type()
)
physicalInterfaceNumTXError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalInterfaceNumTXError.setStatus("current")
_PhysicalInterfaceNumRXError_Type = Integer32
_PhysicalInterfaceNumRXError_Object = MibTableColumn
physicalInterfaceNumRXError = _PhysicalInterfaceNumRXError_Object(
    (1, 3, 6, 1, 4, 1, 63, 501, 3, 4, 2, 1, 10),
    _PhysicalInterfaceNumRXError_Type()
)
physicalInterfaceNumRXError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalInterfaceNumRXError.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AIRPORT-BASESTATION-3-MIB",
    **{"apple": apple,
       "airport": airport,
       "baseStation3": baseStation3,
       "abs3SysConf": abs3SysConf,
       "sysConfName": sysConfName,
       "sysConfContact": sysConfContact,
       "sysConfLocation": sysConfLocation,
       "sysConfUptime": sysConfUptime,
       "sysConfFirmwareVersion": sysConfFirmwareVersion,
       "wireless": wireless,
       "wirelessNumber": wirelessNumber,
       "wirelessClientsTable": wirelessClientsTable,
       "wirelessClient": wirelessClient,
       "wirelessPhysAddress": wirelessPhysAddress,
       "wirelessType": wirelessType,
       "wirelessDataRates": wirelessDataRates,
       "wirelessTimeAssociated": wirelessTimeAssociated,
       "wirelessLastRefreshTime": wirelessLastRefreshTime,
       "wirelessStrength": wirelessStrength,
       "wirelessNoise": wirelessNoise,
       "wirelessRate": wirelessRate,
       "wirelessNumRX": wirelessNumRX,
       "wirelessNumTX": wirelessNumTX,
       "wirelessNumRXErrors": wirelessNumRXErrors,
       "wirelessNumTXErrors": wirelessNumTXErrors,
       "dhcpServer": dhcpServer,
       "dhcpNumber": dhcpNumber,
       "dhcpClientsTable": dhcpClientsTable,
       "dhcpClient": dhcpClient,
       "dhcpPhysAddress": dhcpPhysAddress,
       "dhcpIpAddress": dhcpIpAddress,
       "dhcpClientID": dhcpClientID,
       "dhcpLeaseTime": dhcpLeaseTime,
       "physicalInterfaces": physicalInterfaces,
       "physicalInterfaceCount": physicalInterfaceCount,
       "physicalInterfacesTable": physicalInterfacesTable,
       "physicalInterface": physicalInterface,
       "physicalInterfaceIndex": physicalInterfaceIndex,
       "physicalInterfaceName": physicalInterfaceName,
       "physicalInterfaceUnit": physicalInterfaceUnit,
       "physicalInterfaceSpeed": physicalInterfaceSpeed,
       "physicalInterfaceState": physicalInterfaceState,
       "physicalInterfaceDuplex": physicalInterfaceDuplex,
       "physicalInterfaceNumTX": physicalInterfaceNumTX,
       "physicalInterfaceNumRX": physicalInterfaceNumRX,
       "physicalInterfaceNumTXError": physicalInterfaceNumTXError,
       "physicalInterfaceNumRXError": physicalInterfaceNumRXError}
)
