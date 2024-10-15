# SNMP MIB module (RUCKUS-ZD-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RUCKUS-ZD-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:48:54 2024
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(ruckusZDSystemModule,) = mibBuilder.importSymbols(
    "RUCKUS-ROOT-MIB",
    "ruckusZDSystemModule")

(RuckusAdminStatus,
 RuckusCountryCode,
 RuckusNameString,
 RuckusRadioMode,
 RuckusSSID,
 RuckusdB) = mibBuilder.importSymbols(
    "RUCKUS-TC-MIB",
    "RuckusAdminStatus",
    "RuckusCountryCode",
    "RuckusNameString",
    "RuckusRadioMode",
    "RuckusSSID",
    "RuckusdB")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
    "iso")

(DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruckusZDSystemMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuckusZDSystemObjects_ObjectIdentity = ObjectIdentity
ruckusZDSystemObjects = _RuckusZDSystemObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1)
)
_RuckusZDSystemInfo_ObjectIdentity = ObjectIdentity
ruckusZDSystemInfo = _RuckusZDSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 1)
)


class _RuckusZDSystemName_Type(DisplayString):
    """Custom type ruckusZDSystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuckusZDSystemName_Type.__name__ = "DisplayString"
_RuckusZDSystemName_Object = MibScalar
ruckusZDSystemName = _RuckusZDSystemName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 1, 1),
    _RuckusZDSystemName_Type()
)
ruckusZDSystemName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemName.setStatus("current")
_RuckusZDSystemIPAddr_Type = IpAddress
_RuckusZDSystemIPAddr_Object = MibScalar
ruckusZDSystemIPAddr = _RuckusZDSystemIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 1, 2),
    _RuckusZDSystemIPAddr_Type()
)
ruckusZDSystemIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemIPAddr.setStatus("current")
_RuckusZDSystemMacAddr_Type = MacAddress
_RuckusZDSystemMacAddr_Object = MibScalar
ruckusZDSystemMacAddr = _RuckusZDSystemMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 1, 3),
    _RuckusZDSystemMacAddr_Type()
)
ruckusZDSystemMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemMacAddr.setStatus("current")
_RuckusZDSystemUptime_Type = TimeTicks
_RuckusZDSystemUptime_Object = MibScalar
ruckusZDSystemUptime = _RuckusZDSystemUptime_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 1, 8),
    _RuckusZDSystemUptime_Type()
)
ruckusZDSystemUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemUptime.setStatus("current")
_RuckusZDSystemModel_Type = DisplayString
_RuckusZDSystemModel_Object = MibScalar
ruckusZDSystemModel = _RuckusZDSystemModel_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 1, 9),
    _RuckusZDSystemModel_Type()
)
ruckusZDSystemModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemModel.setStatus("current")
_RuckusZDSystemLicensedAPs_Type = Unsigned32
_RuckusZDSystemLicensedAPs_Object = MibScalar
ruckusZDSystemLicensedAPs = _RuckusZDSystemLicensedAPs_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 1, 12),
    _RuckusZDSystemLicensedAPs_Type()
)
ruckusZDSystemLicensedAPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemLicensedAPs.setStatus("current")
_RuckusZDSystemMaxSta_Type = Unsigned32
_RuckusZDSystemMaxSta_Object = MibScalar
ruckusZDSystemMaxSta = _RuckusZDSystemMaxSta_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 1, 13),
    _RuckusZDSystemMaxSta_Type()
)
ruckusZDSystemMaxSta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemMaxSta.setStatus("current")
_RuckusZDSystemSerialNumber_Type = DisplayString
_RuckusZDSystemSerialNumber_Object = MibScalar
ruckusZDSystemSerialNumber = _RuckusZDSystemSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 1, 15),
    _RuckusZDSystemSerialNumber_Type()
)
ruckusZDSystemSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemSerialNumber.setStatus("current")
_RuckusZDSystemVersion_Type = DisplayString
_RuckusZDSystemVersion_Object = MibScalar
ruckusZDSystemVersion = _RuckusZDSystemVersion_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 1, 18),
    _RuckusZDSystemVersion_Type()
)
ruckusZDSystemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemVersion.setStatus("current")
_RuckusZDSystemCountryCode_Type = RuckusCountryCode
_RuckusZDSystemCountryCode_Object = MibScalar
ruckusZDSystemCountryCode = _RuckusZDSystemCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 1, 20),
    _RuckusZDSystemCountryCode_Type()
)
ruckusZDSystemCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemCountryCode.setStatus("current")
_RuckusZDSystemAdminName_Type = DisplayString
_RuckusZDSystemAdminName_Object = MibScalar
ruckusZDSystemAdminName = _RuckusZDSystemAdminName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 1, 25),
    _RuckusZDSystemAdminName_Type()
)
ruckusZDSystemAdminName.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    ruckusZDSystemAdminName.setStatus("current")
_RuckusZDSystemAdminPassword_Type = DisplayString
_RuckusZDSystemAdminPassword_Object = MibScalar
ruckusZDSystemAdminPassword = _RuckusZDSystemAdminPassword_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 1, 26),
    _RuckusZDSystemAdminPassword_Type()
)
ruckusZDSystemAdminPassword.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    ruckusZDSystemAdminPassword.setStatus("current")


class _RuckusZDSystemStatus_Type(Integer32):
    """Custom type ruckusZDSystemStatus based on Integer32"""
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
        *(("master", 1),
          ("noredundancy", 3),
          ("standby", 2))
    )


_RuckusZDSystemStatus_Type.__name__ = "Integer32"
_RuckusZDSystemStatus_Object = MibScalar
ruckusZDSystemStatus = _RuckusZDSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 1, 30),
    _RuckusZDSystemStatus_Type()
)
ruckusZDSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemStatus.setStatus("current")


class _RuckusZDSystemPeerConnectedStatus_Type(Integer32):
    """Custom type ruckusZDSystemPeerConnectedStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("disconnected", 2))
    )


_RuckusZDSystemPeerConnectedStatus_Type.__name__ = "Integer32"
_RuckusZDSystemPeerConnectedStatus_Object = MibScalar
ruckusZDSystemPeerConnectedStatus = _RuckusZDSystemPeerConnectedStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 1, 31),
    _RuckusZDSystemPeerConnectedStatus_Type()
)
ruckusZDSystemPeerConnectedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemPeerConnectedStatus.setStatus("current")
_RuckusZDSystemExpInfo_ObjectIdentity = ObjectIdentity
ruckusZDSystemExpInfo = _RuckusZDSystemExpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 5)
)
_RuckusZDSystemNEId_Type = DisplayString
_RuckusZDSystemNEId_Object = MibScalar
ruckusZDSystemNEId = _RuckusZDSystemNEId_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 5, 50),
    _RuckusZDSystemNEId_Type()
)
ruckusZDSystemNEId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemNEId.setStatus("current")
_RuckusZDSystemManufacturer_Type = DisplayString
_RuckusZDSystemManufacturer_Object = MibScalar
ruckusZDSystemManufacturer = _RuckusZDSystemManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 5, 51),
    _RuckusZDSystemManufacturer_Type()
)
ruckusZDSystemManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemManufacturer.setStatus("current")
_RuckusZDSystemSoftwareName_Type = DisplayString
_RuckusZDSystemSoftwareName_Object = MibScalar
ruckusZDSystemSoftwareName = _RuckusZDSystemSoftwareName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 5, 52),
    _RuckusZDSystemSoftwareName_Type()
)
ruckusZDSystemSoftwareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemSoftwareName.setStatus("current")
_RuckusZDSystemCPUUtil_Type = Unsigned32
_RuckusZDSystemCPUUtil_Object = MibScalar
ruckusZDSystemCPUUtil = _RuckusZDSystemCPUUtil_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 5, 58),
    _RuckusZDSystemCPUUtil_Type()
)
ruckusZDSystemCPUUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemCPUUtil.setStatus("current")
_RuckusZDSystemMemoryUtil_Type = Unsigned32
_RuckusZDSystemMemoryUtil_Object = MibScalar
ruckusZDSystemMemoryUtil = _RuckusZDSystemMemoryUtil_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 5, 59),
    _RuckusZDSystemMemoryUtil_Type()
)
ruckusZDSystemMemoryUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemMemoryUtil.setStatus("current")
_RuckusZDSystemMemorySize_Type = Unsigned32
_RuckusZDSystemMemorySize_Object = MibScalar
ruckusZDSystemMemorySize = _RuckusZDSystemMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 5, 60),
    _RuckusZDSystemMemorySize_Type()
)
ruckusZDSystemMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemMemorySize.setStatus("current")
if mibBuilder.loadTexts:
    ruckusZDSystemMemorySize.setUnits("MB")
_RuckusZDSystemFlashFreeSize_Type = Unsigned32
_RuckusZDSystemFlashFreeSize_Object = MibScalar
ruckusZDSystemFlashFreeSize = _RuckusZDSystemFlashFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 5, 65),
    _RuckusZDSystemFlashFreeSize_Type()
)
ruckusZDSystemFlashFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemFlashFreeSize.setStatus("current")
if mibBuilder.loadTexts:
    ruckusZDSystemFlashFreeSize.setUnits("KByte")
_RuckusZDSystemMgmtVlanID_Type = Unsigned32
_RuckusZDSystemMgmtVlanID_Object = MibScalar
ruckusZDSystemMgmtVlanID = _RuckusZDSystemMgmtVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 5, 67),
    _RuckusZDSystemMgmtVlanID_Type()
)
ruckusZDSystemMgmtVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemMgmtVlanID.setStatus("current")
_RuckusZDSystemtCPUSpeed_Type = Unsigned32
_RuckusZDSystemtCPUSpeed_Object = MibScalar
ruckusZDSystemtCPUSpeed = _RuckusZDSystemtCPUSpeed_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 5, 71),
    _RuckusZDSystemtCPUSpeed_Type()
)
ruckusZDSystemtCPUSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemtCPUSpeed.setStatus("current")
if mibBuilder.loadTexts:
    ruckusZDSystemtCPUSpeed.setUnits("BogoMIPS")
_RuckusZDSystemtFlashModel_Type = DisplayString
_RuckusZDSystemtFlashModel_Object = MibScalar
ruckusZDSystemtFlashModel = _RuckusZDSystemtFlashModel_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 5, 72),
    _RuckusZDSystemtFlashModel_Type()
)
ruckusZDSystemtFlashModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemtFlashModel.setStatus("current")
_RuckusZDSystemtMemModel_Type = DisplayString
_RuckusZDSystemtMemModel_Object = MibScalar
ruckusZDSystemtMemModel = _RuckusZDSystemtMemModel_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 5, 73),
    _RuckusZDSystemtMemModel_Type()
)
ruckusZDSystemtMemModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemtMemModel.setStatus("current")
_RuckusZDSystemStartTime_Type = DisplayString
_RuckusZDSystemStartTime_Object = MibScalar
ruckusZDSystemStartTime = _RuckusZDSystemStartTime_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 5, 74),
    _RuckusZDSystemStartTime_Type()
)
ruckusZDSystemStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemStartTime.setStatus("current")
_RuckusZDSystemCurrentTime_Type = DisplayString
_RuckusZDSystemCurrentTime_Object = MibScalar
ruckusZDSystemCurrentTime = _RuckusZDSystemCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 5, 80),
    _RuckusZDSystemCurrentTime_Type()
)
ruckusZDSystemCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemCurrentTime.setStatus("current")
_RuckusZDSystemAPFirmwareServer_Type = IpAddress
_RuckusZDSystemAPFirmwareServer_Object = MibScalar
ruckusZDSystemAPFirmwareServer = _RuckusZDSystemAPFirmwareServer_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 5, 81),
    _RuckusZDSystemAPFirmwareServer_Type()
)
ruckusZDSystemAPFirmwareServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemAPFirmwareServer.setStatus("current")
_RuckusZDSystemAPConfigServer_Type = IpAddress
_RuckusZDSystemAPConfigServer_Object = MibScalar
ruckusZDSystemAPConfigServer = _RuckusZDSystemAPConfigServer_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 5, 82),
    _RuckusZDSystemAPConfigServer_Type()
)
ruckusZDSystemAPConfigServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemAPConfigServer.setStatus("current")
_RuckusZDSystemIDSAllowedESSID_Type = DisplayString
_RuckusZDSystemIDSAllowedESSID_Object = MibScalar
ruckusZDSystemIDSAllowedESSID = _RuckusZDSystemIDSAllowedESSID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 5, 85),
    _RuckusZDSystemIDSAllowedESSID_Type()
)
ruckusZDSystemIDSAllowedESSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemIDSAllowedESSID.setStatus("current")
_RuckusZDSystemIDSAllowBSSID_Type = DisplayString
_RuckusZDSystemIDSAllowBSSID_Object = MibScalar
ruckusZDSystemIDSAllowBSSID = _RuckusZDSystemIDSAllowBSSID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 5, 86),
    _RuckusZDSystemIDSAllowBSSID_Type()
)
ruckusZDSystemIDSAllowBSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemIDSAllowBSSID.setStatus("current")
_RuckusZDSystemIDSAllowOUI_Type = DisplayString
_RuckusZDSystemIDSAllowOUI_Object = MibScalar
ruckusZDSystemIDSAllowOUI = _RuckusZDSystemIDSAllowOUI_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 5, 87),
    _RuckusZDSystemIDSAllowOUI_Type()
)
ruckusZDSystemIDSAllowOUI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemIDSAllowOUI.setStatus("current")


class _RuckusZDSystemBandwidthUtilValve_Type(Unsigned32):
    """Custom type ruckusZDSystemBandwidthUtilValve based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RuckusZDSystemBandwidthUtilValve_Type.__name__ = "Unsigned32"
_RuckusZDSystemBandwidthUtilValve_Object = MibScalar
ruckusZDSystemBandwidthUtilValve = _RuckusZDSystemBandwidthUtilValve_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 5, 90),
    _RuckusZDSystemBandwidthUtilValve_Type()
)
ruckusZDSystemBandwidthUtilValve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemBandwidthUtilValve.setStatus("current")


class _RuckusZDSystemDropPacketRateValve_Type(Unsigned32):
    """Custom type ruckusZDSystemDropPacketRateValve based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RuckusZDSystemDropPacketRateValve_Type.__name__ = "Unsigned32"
_RuckusZDSystemDropPacketRateValve_Object = MibScalar
ruckusZDSystemDropPacketRateValve = _RuckusZDSystemDropPacketRateValve_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 5, 91),
    _RuckusZDSystemDropPacketRateValve_Type()
)
ruckusZDSystemDropPacketRateValve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemDropPacketRateValve.setStatus("current")


class _RuckusZDSystemCPUUtilValve_Type(Unsigned32):
    """Custom type ruckusZDSystemCPUUtilValve based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RuckusZDSystemCPUUtilValve_Type.__name__ = "Unsigned32"
_RuckusZDSystemCPUUtilValve_Object = MibScalar
ruckusZDSystemCPUUtilValve = _RuckusZDSystemCPUUtilValve_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 5, 92),
    _RuckusZDSystemCPUUtilValve_Type()
)
ruckusZDSystemCPUUtilValve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemCPUUtilValve.setStatus("current")


class _RuckusZDSystemMemUtilValve_Type(Unsigned32):
    """Custom type ruckusZDSystemMemUtilValve based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RuckusZDSystemMemUtilValve_Type.__name__ = "Unsigned32"
_RuckusZDSystemMemUtilValve_Object = MibScalar
ruckusZDSystemMemUtilValve = _RuckusZDSystemMemUtilValve_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 5, 95),
    _RuckusZDSystemMemUtilValve_Type()
)
ruckusZDSystemMemUtilValve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemMemUtilValve.setStatus("current")
_RuckusZDSystemOnlineStaValve_Type = Unsigned32
_RuckusZDSystemOnlineStaValve_Object = MibScalar
ruckusZDSystemOnlineStaValve = _RuckusZDSystemOnlineStaValve_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 5, 96),
    _RuckusZDSystemOnlineStaValve_Type()
)
ruckusZDSystemOnlineStaValve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemOnlineStaValve.setStatus("current")


class _RuckusZDSystemACLocationLongitude_Type(DisplayString):
    """Custom type ruckusZDSystemACLocationLongitude based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuckusZDSystemACLocationLongitude_Type.__name__ = "DisplayString"
_RuckusZDSystemACLocationLongitude_Object = MibScalar
ruckusZDSystemACLocationLongitude = _RuckusZDSystemACLocationLongitude_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 5, 97),
    _RuckusZDSystemACLocationLongitude_Type()
)
ruckusZDSystemACLocationLongitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemACLocationLongitude.setStatus("current")


class _RuckusZDSystemACLocationLatitude_Type(DisplayString):
    """Custom type ruckusZDSystemACLocationLatitude based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuckusZDSystemACLocationLatitude_Type.__name__ = "DisplayString"
_RuckusZDSystemACLocationLatitude_Object = MibScalar
ruckusZDSystemACLocationLatitude = _RuckusZDSystemACLocationLatitude_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 5, 98),
    _RuckusZDSystemACLocationLatitude_Type()
)
ruckusZDSystemACLocationLatitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemACLocationLatitude.setStatus("current")


class _RuckusZDSystemDHCPServer_Type(Integer32):
    """Custom type ruckusZDSystemDHCPServer based on Integer32"""
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


_RuckusZDSystemDHCPServer_Type.__name__ = "Integer32"
_RuckusZDSystemDHCPServer_Object = MibScalar
ruckusZDSystemDHCPServer = _RuckusZDSystemDHCPServer_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 5, 110),
    _RuckusZDSystemDHCPServer_Type()
)
ruckusZDSystemDHCPServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemDHCPServer.setStatus("current")


class _RuckusZDAPCPUvalve_Type(Unsigned32):
    """Custom type ruckusZDAPCPUvalve based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RuckusZDAPCPUvalve_Type.__name__ = "Unsigned32"
_RuckusZDAPCPUvalve_Object = MibScalar
ruckusZDAPCPUvalve = _RuckusZDAPCPUvalve_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 5, 120),
    _RuckusZDAPCPUvalve_Type()
)
ruckusZDAPCPUvalve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDAPCPUvalve.setStatus("current")


class _RuckusZDAPMemoryvalve_Type(Unsigned32):
    """Custom type ruckusZDAPMemoryvalve based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RuckusZDAPMemoryvalve_Type.__name__ = "Unsigned32"
_RuckusZDAPMemoryvalve_Object = MibScalar
ruckusZDAPMemoryvalve = _RuckusZDAPMemoryvalve_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 5, 121),
    _RuckusZDAPMemoryvalve_Type()
)
ruckusZDAPMemoryvalve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDAPMemoryvalve.setStatus("current")


class _RuckusZDHeartBeatStatus_Type(TruthValue):
    """Custom type ruckusZDHeartBeatStatus based on TruthValue"""
    subtypeSpec = TruthValue.subtypeSpec
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


_RuckusZDHeartBeatStatus_Type.__name__ = "TruthValue"
_RuckusZDHeartBeatStatus_Object = MibScalar
ruckusZDHeartBeatStatus = _RuckusZDHeartBeatStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 5, 122),
    _RuckusZDHeartBeatStatus_Type()
)
ruckusZDHeartBeatStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDHeartBeatStatus.setStatus("current")


class _RuckusZDHeartBeatPeriod_Type(Unsigned32):
    """Custom type ruckusZDHeartBeatPeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_RuckusZDHeartBeatPeriod_Type.__name__ = "Unsigned32"
_RuckusZDHeartBeatPeriod_Object = MibScalar
ruckusZDHeartBeatPeriod = _RuckusZDHeartBeatPeriod_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 5, 123),
    _RuckusZDHeartBeatPeriod_Type()
)
ruckusZDHeartBeatPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDHeartBeatPeriod.setStatus("current")
_RuckusZDSystemIPTable_Object = MibTable
ruckusZDSystemIPTable = _RuckusZDSystemIPTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 8)
)
if mibBuilder.loadTexts:
    ruckusZDSystemIPTable.setStatus("current")
_RuckusZDSystemIPEntry_Object = MibTableRow
ruckusZDSystemIPEntry = _RuckusZDSystemIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 8, 1)
)
ruckusZDSystemIPEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ruckusZDSystemIPEntry.setStatus("current")


class _RuckusZDSystemIPVersion_Type(Integer32):
    """Custom type ruckusZDSystemIPVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dualstack", 3),
          ("ipv4", 1),
          ("ipv6", 2))
    )


_RuckusZDSystemIPVersion_Type.__name__ = "Integer32"
_RuckusZDSystemIPVersion_Object = MibTableColumn
ruckusZDSystemIPVersion = _RuckusZDSystemIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 8, 1, 2),
    _RuckusZDSystemIPVersion_Type()
)
ruckusZDSystemIPVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemIPVersion.setStatus("current")


class _RuckusZDSystemIPAddrMode_Type(Integer32):
    """Custom type ruckusZDSystemIPAddrMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 2),
          ("static", 1))
    )


_RuckusZDSystemIPAddrMode_Type.__name__ = "Integer32"
_RuckusZDSystemIPAddrMode_Object = MibTableColumn
ruckusZDSystemIPAddrMode = _RuckusZDSystemIPAddrMode_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 8, 1, 5),
    _RuckusZDSystemIPAddrMode_Type()
)
ruckusZDSystemIPAddrMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemIPAddrMode.setStatus("current")
_RuckusZDSystemIPAddress_Type = IpAddress
_RuckusZDSystemIPAddress_Object = MibTableColumn
ruckusZDSystemIPAddress = _RuckusZDSystemIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 8, 1, 6),
    _RuckusZDSystemIPAddress_Type()
)
ruckusZDSystemIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemIPAddress.setStatus("current")
_RuckusZDSystemIPAddrNetmask_Type = IpAddress
_RuckusZDSystemIPAddrNetmask_Object = MibTableColumn
ruckusZDSystemIPAddrNetmask = _RuckusZDSystemIPAddrNetmask_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 8, 1, 8),
    _RuckusZDSystemIPAddrNetmask_Type()
)
ruckusZDSystemIPAddrNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemIPAddrNetmask.setStatus("current")
_RuckusZDSystemIPGateway_Type = IpAddress
_RuckusZDSystemIPGateway_Object = MibTableColumn
ruckusZDSystemIPGateway = _RuckusZDSystemIPGateway_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 8, 1, 10),
    _RuckusZDSystemIPGateway_Type()
)
ruckusZDSystemIPGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemIPGateway.setStatus("current")
_RuckusZDSystemIPPrimaryDNS_Type = IpAddress
_RuckusZDSystemIPPrimaryDNS_Object = MibTableColumn
ruckusZDSystemIPPrimaryDNS = _RuckusZDSystemIPPrimaryDNS_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 8, 1, 12),
    _RuckusZDSystemIPPrimaryDNS_Type()
)
ruckusZDSystemIPPrimaryDNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemIPPrimaryDNS.setStatus("current")
_RuckusZDSystemIPSecondaryDNS_Type = IpAddress
_RuckusZDSystemIPSecondaryDNS_Object = MibTableColumn
ruckusZDSystemIPSecondaryDNS = _RuckusZDSystemIPSecondaryDNS_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 8, 1, 13),
    _RuckusZDSystemIPSecondaryDNS_Type()
)
ruckusZDSystemIPSecondaryDNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemIPSecondaryDNS.setStatus("current")


class _RuckusZDSystemIPV6AddressModel_Type(Integer32):
    """Custom type ruckusZDSystemIPV6AddressModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto-configuration", 1),
          ("static", 2))
    )


_RuckusZDSystemIPV6AddressModel_Type.__name__ = "Integer32"
_RuckusZDSystemIPV6AddressModel_Object = MibTableColumn
ruckusZDSystemIPV6AddressModel = _RuckusZDSystemIPV6AddressModel_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 8, 1, 20),
    _RuckusZDSystemIPV6AddressModel_Type()
)
ruckusZDSystemIPV6AddressModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemIPV6AddressModel.setStatus("current")


class _RuckusZDSystemIPV6Address_Type(OctetString):
    """Custom type ruckusZDSystemIPV6Address based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 40),
    )


_RuckusZDSystemIPV6Address_Type.__name__ = "OctetString"
_RuckusZDSystemIPV6Address_Object = MibTableColumn
ruckusZDSystemIPV6Address = _RuckusZDSystemIPV6Address_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 8, 1, 21),
    _RuckusZDSystemIPV6Address_Type()
)
ruckusZDSystemIPV6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemIPV6Address.setStatus("current")


class _RuckusZDSystemIPV6PrefixLen_Type(Integer32):
    """Custom type ruckusZDSystemIPV6PrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 128),
    )


_RuckusZDSystemIPV6PrefixLen_Type.__name__ = "Integer32"
_RuckusZDSystemIPV6PrefixLen_Object = MibTableColumn
ruckusZDSystemIPV6PrefixLen = _RuckusZDSystemIPV6PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 8, 1, 22),
    _RuckusZDSystemIPV6PrefixLen_Type()
)
ruckusZDSystemIPV6PrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemIPV6PrefixLen.setStatus("current")


class _RuckusZDSystemIPV6Gateway_Type(OctetString):
    """Custom type ruckusZDSystemIPV6Gateway based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 40),
    )


_RuckusZDSystemIPV6Gateway_Type.__name__ = "OctetString"
_RuckusZDSystemIPV6Gateway_Object = MibTableColumn
ruckusZDSystemIPV6Gateway = _RuckusZDSystemIPV6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 8, 1, 25),
    _RuckusZDSystemIPV6Gateway_Type()
)
ruckusZDSystemIPV6Gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemIPV6Gateway.setStatus("current")


class _RuckusZDSystemIPV6PrimaryDNS_Type(OctetString):
    """Custom type ruckusZDSystemIPV6PrimaryDNS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 40),
    )


_RuckusZDSystemIPV6PrimaryDNS_Type.__name__ = "OctetString"
_RuckusZDSystemIPV6PrimaryDNS_Object = MibTableColumn
ruckusZDSystemIPV6PrimaryDNS = _RuckusZDSystemIPV6PrimaryDNS_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 8, 1, 28),
    _RuckusZDSystemIPV6PrimaryDNS_Type()
)
ruckusZDSystemIPV6PrimaryDNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemIPV6PrimaryDNS.setStatus("current")


class _RuckusZDSystemIPV6SecondaryDNS_Type(OctetString):
    """Custom type ruckusZDSystemIPV6SecondaryDNS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 40),
    )


_RuckusZDSystemIPV6SecondaryDNS_Type.__name__ = "OctetString"
_RuckusZDSystemIPV6SecondaryDNS_Object = MibTableColumn
ruckusZDSystemIPV6SecondaryDNS = _RuckusZDSystemIPV6SecondaryDNS_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 8, 1, 29),
    _RuckusZDSystemIPV6SecondaryDNS_Type()
)
ruckusZDSystemIPV6SecondaryDNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemIPV6SecondaryDNS.setStatus("current")
_RuckusZDSystemServices_ObjectIdentity = ObjectIdentity
ruckusZDSystemServices = _RuckusZDSystemServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12)
)
_RuckusZDSystemNTP_ObjectIdentity = ObjectIdentity
ruckusZDSystemNTP = _RuckusZDSystemNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 3)
)


class _RuckusZDSystemTimeWithNTP_Type(Integer32):
    """Custom type ruckusZDSystemTimeWithNTP based on Integer32"""
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


_RuckusZDSystemTimeWithNTP_Type.__name__ = "Integer32"
_RuckusZDSystemTimeWithNTP_Object = MibScalar
ruckusZDSystemTimeWithNTP = _RuckusZDSystemTimeWithNTP_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 3, 1),
    _RuckusZDSystemTimeWithNTP_Type()
)
ruckusZDSystemTimeWithNTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemTimeWithNTP.setStatus("current")


class _RuckusZDSystemTimeNTPServer_Type(OctetString):
    """Custom type ruckusZDSystemTimeNTPServer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_RuckusZDSystemTimeNTPServer_Type.__name__ = "OctetString"
_RuckusZDSystemTimeNTPServer_Object = MibScalar
ruckusZDSystemTimeNTPServer = _RuckusZDSystemTimeNTPServer_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 3, 2),
    _RuckusZDSystemTimeNTPServer_Type()
)
ruckusZDSystemTimeNTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemTimeNTPServer.setStatus("current")
_RuckusZDSystemSMTP_ObjectIdentity = ObjectIdentity
ruckusZDSystemSMTP = _RuckusZDSystemSMTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 5)
)


class _RuckusZDSystemEmailTriggerEnable_Type(Integer32):
    """Custom type ruckusZDSystemEmailTriggerEnable based on Integer32"""
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


_RuckusZDSystemEmailTriggerEnable_Type.__name__ = "Integer32"
_RuckusZDSystemEmailTriggerEnable_Object = MibScalar
ruckusZDSystemEmailTriggerEnable = _RuckusZDSystemEmailTriggerEnable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 5, 1),
    _RuckusZDSystemEmailTriggerEnable_Type()
)
ruckusZDSystemEmailTriggerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemEmailTriggerEnable.setStatus("current")


class _RuckusZDSystemEmailAddress_Type(DisplayString):
    """Custom type ruckusZDSystemEmailAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuckusZDSystemEmailAddress_Type.__name__ = "DisplayString"
_RuckusZDSystemEmailAddress_Object = MibScalar
ruckusZDSystemEmailAddress = _RuckusZDSystemEmailAddress_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 5, 2),
    _RuckusZDSystemEmailAddress_Type()
)
ruckusZDSystemEmailAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemEmailAddress.setStatus("current")


class _RuckusZDSystemSMTPServerName_Type(DisplayString):
    """Custom type ruckusZDSystemSMTPServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_RuckusZDSystemSMTPServerName_Type.__name__ = "DisplayString"
_RuckusZDSystemSMTPServerName_Object = MibScalar
ruckusZDSystemSMTPServerName = _RuckusZDSystemSMTPServerName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 5, 3),
    _RuckusZDSystemSMTPServerName_Type()
)
ruckusZDSystemSMTPServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemSMTPServerName.setStatus("current")


class _RuckusZDSystemSMTPServerPort_Type(Integer32):
    """Custom type ruckusZDSystemSMTPServerPort based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RuckusZDSystemSMTPServerPort_Type.__name__ = "Integer32"
_RuckusZDSystemSMTPServerPort_Object = MibScalar
ruckusZDSystemSMTPServerPort = _RuckusZDSystemSMTPServerPort_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 5, 4),
    _RuckusZDSystemSMTPServerPort_Type()
)
ruckusZDSystemSMTPServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemSMTPServerPort.setStatus("current")


class _RuckusZDSystemSMTPAuthUsername_Type(DisplayString):
    """Custom type ruckusZDSystemSMTPAuthUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_RuckusZDSystemSMTPAuthUsername_Type.__name__ = "DisplayString"
_RuckusZDSystemSMTPAuthUsername_Object = MibScalar
ruckusZDSystemSMTPAuthUsername = _RuckusZDSystemSMTPAuthUsername_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 5, 5),
    _RuckusZDSystemSMTPAuthUsername_Type()
)
ruckusZDSystemSMTPAuthUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemSMTPAuthUsername.setStatus("current")


class _RuckusZDSystemSMTPAuthPassword_Type(DisplayString):
    """Custom type ruckusZDSystemSMTPAuthPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_RuckusZDSystemSMTPAuthPassword_Type.__name__ = "DisplayString"
_RuckusZDSystemSMTPAuthPassword_Object = MibScalar
ruckusZDSystemSMTPAuthPassword = _RuckusZDSystemSMTPAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 5, 6),
    _RuckusZDSystemSMTPAuthPassword_Type()
)
ruckusZDSystemSMTPAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemSMTPAuthPassword.setStatus("current")


class _RuckusZDSystemFromEmailAddress_Type(DisplayString):
    """Custom type ruckusZDSystemFromEmailAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_RuckusZDSystemFromEmailAddress_Type.__name__ = "DisplayString"
_RuckusZDSystemFromEmailAddress_Object = MibScalar
ruckusZDSystemFromEmailAddress = _RuckusZDSystemFromEmailAddress_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 5, 7),
    _RuckusZDSystemFromEmailAddress_Type()
)
ruckusZDSystemFromEmailAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemFromEmailAddress.setStatus("current")


class _RuckusZDSystemSMTPEncryptionOptions_Type(Integer32):
    """Custom type ruckusZDSystemSMTPEncryptionOptions based on Integer32"""
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
        *(("none", 1),
          ("starttls", 3),
          ("tls", 2))
    )


_RuckusZDSystemSMTPEncryptionOptions_Type.__name__ = "Integer32"
_RuckusZDSystemSMTPEncryptionOptions_Object = MibScalar
ruckusZDSystemSMTPEncryptionOptions = _RuckusZDSystemSMTPEncryptionOptions_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 5, 8),
    _RuckusZDSystemSMTPEncryptionOptions_Type()
)
ruckusZDSystemSMTPEncryptionOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemSMTPEncryptionOptions.setStatus("current")
_RuckusZDSystemSyslog_ObjectIdentity = ObjectIdentity
ruckusZDSystemSyslog = _RuckusZDSystemSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 8)
)


class _RuckusZDSystemLogWithSysLog_Type(Integer32):
    """Custom type ruckusZDSystemLogWithSysLog based on Integer32"""
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


_RuckusZDSystemLogWithSysLog_Type.__name__ = "Integer32"
_RuckusZDSystemLogWithSysLog_Object = MibScalar
ruckusZDSystemLogWithSysLog = _RuckusZDSystemLogWithSysLog_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 8, 1),
    _RuckusZDSystemLogWithSysLog_Type()
)
ruckusZDSystemLogWithSysLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemLogWithSysLog.setStatus("current")


class _RuckusZDSystemSysLogServer_Type(OctetString):
    """Custom type ruckusZDSystemSysLogServer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 40),
    )


_RuckusZDSystemSysLogServer_Type.__name__ = "OctetString"
_RuckusZDSystemSysLogServer_Object = MibScalar
ruckusZDSystemSysLogServer = _RuckusZDSystemSysLogServer_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 8, 2),
    _RuckusZDSystemSysLogServer_Type()
)
ruckusZDSystemSysLogServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemSysLogServer.setStatus("current")
_RuckusZDSystemFlexMaster_ObjectIdentity = ObjectIdentity
ruckusZDSystemFlexMaster = _RuckusZDSystemFlexMaster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 9)
)


class _RuckusZDSystemFlexMasterEnable_Type(Integer32):
    """Custom type ruckusZDSystemFlexMasterEnable based on Integer32"""
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


_RuckusZDSystemFlexMasterEnable_Type.__name__ = "Integer32"
_RuckusZDSystemFlexMasterEnable_Object = MibScalar
ruckusZDSystemFlexMasterEnable = _RuckusZDSystemFlexMasterEnable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 9, 1),
    _RuckusZDSystemFlexMasterEnable_Type()
)
ruckusZDSystemFlexMasterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemFlexMasterEnable.setStatus("current")


class _RuckusZDSystemFlexMasterServer_Type(DisplayString):
    """Custom type ruckusZDSystemFlexMasterServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_RuckusZDSystemFlexMasterServer_Type.__name__ = "DisplayString"
_RuckusZDSystemFlexMasterServer_Object = MibScalar
ruckusZDSystemFlexMasterServer = _RuckusZDSystemFlexMasterServer_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 9, 2),
    _RuckusZDSystemFlexMasterServer_Type()
)
ruckusZDSystemFlexMasterServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemFlexMasterServer.setStatus("current")


class _RuckusZDSystemFlexMasterInterval_Type(Integer32):
    """Custom type ruckusZDSystemFlexMasterInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_RuckusZDSystemFlexMasterInterval_Type.__name__ = "Integer32"
_RuckusZDSystemFlexMasterInterval_Object = MibScalar
ruckusZDSystemFlexMasterInterval = _RuckusZDSystemFlexMasterInterval_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 9, 3),
    _RuckusZDSystemFlexMasterInterval_Type()
)
ruckusZDSystemFlexMasterInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemFlexMasterInterval.setStatus("current")
_RuckusZDSystemStpInfo_ObjectIdentity = ObjectIdentity
ruckusZDSystemStpInfo = _RuckusZDSystemStpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 12)
)
_RuckusZDSystemStpStatus_Type = TruthValue
_RuckusZDSystemStpStatus_Object = MibScalar
ruckusZDSystemStpStatus = _RuckusZDSystemStpStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 12, 1),
    _RuckusZDSystemStpStatus_Type()
)
ruckusZDSystemStpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemStpStatus.setStatus("current")
_RuckusZDSystemSNMP_ObjectIdentity = ObjectIdentity
ruckusZDSystemSNMP = _RuckusZDSystemSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 15)
)
_RuckusZDSystemSNMPTrapInfo_ObjectIdentity = ObjectIdentity
ruckusZDSystemSNMPTrapInfo = _RuckusZDSystemSNMPTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 15, 3)
)


class _RuckusZDSystemSNMPTrapEnable_Type(Integer32):
    """Custom type ruckusZDSystemSNMPTrapEnable based on Integer32"""
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


_RuckusZDSystemSNMPTrapEnable_Type.__name__ = "Integer32"
_RuckusZDSystemSNMPTrapEnable_Object = MibScalar
ruckusZDSystemSNMPTrapEnable = _RuckusZDSystemSNMPTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 15, 3, 1),
    _RuckusZDSystemSNMPTrapEnable_Type()
)
ruckusZDSystemSNMPTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemSNMPTrapEnable.setStatus("current")


class _RuckusZDSystemSNMPTrapVersion_Type(Integer32):
    """Custom type ruckusZDSystemSNMPTrapVersion based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("snmpv2", 1),
          ("snmpv3", 2))
    )


_RuckusZDSystemSNMPTrapVersion_Type.__name__ = "Integer32"
_RuckusZDSystemSNMPTrapVersion_Object = MibScalar
ruckusZDSystemSNMPTrapVersion = _RuckusZDSystemSNMPTrapVersion_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 15, 3, 2),
    _RuckusZDSystemSNMPTrapVersion_Type()
)
ruckusZDSystemSNMPTrapVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemSNMPTrapVersion.setStatus("current")
_RuckusZDSystemSNMPV2TrapSvrTable_Object = MibTable
ruckusZDSystemSNMPV2TrapSvrTable = _RuckusZDSystemSNMPV2TrapSvrTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 15, 3, 35)
)
if mibBuilder.loadTexts:
    ruckusZDSystemSNMPV2TrapSvrTable.setStatus("current")
_RuckusZDSystemSNMPV2TrapSvrEntry_Object = MibTableRow
ruckusZDSystemSNMPV2TrapSvrEntry = _RuckusZDSystemSNMPV2TrapSvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 15, 3, 35, 1)
)
ruckusZDSystemSNMPV2TrapSvrEntry.setIndexNames(
    (0, "RUCKUS-ZD-SYSTEM-MIB", "ruckusZDSystemSNMPV2TrapSvrIndex"),
)
if mibBuilder.loadTexts:
    ruckusZDSystemSNMPV2TrapSvrEntry.setStatus("current")


class _RuckusZDSystemSNMPV2TrapSvrIndex_Type(Integer32):
    """Custom type ruckusZDSystemSNMPV2TrapSvrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_RuckusZDSystemSNMPV2TrapSvrIndex_Type.__name__ = "Integer32"
_RuckusZDSystemSNMPV2TrapSvrIndex_Object = MibTableColumn
ruckusZDSystemSNMPV2TrapSvrIndex = _RuckusZDSystemSNMPV2TrapSvrIndex_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 15, 3, 35, 1, 1),
    _RuckusZDSystemSNMPV2TrapSvrIndex_Type()
)
ruckusZDSystemSNMPV2TrapSvrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemSNMPV2TrapSvrIndex.setStatus("current")


class _RuckusZDSystemSNMPV2TrapServer_Type(OctetString):
    """Custom type ruckusZDSystemSNMPV2TrapServer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 40),
    )


_RuckusZDSystemSNMPV2TrapServer_Type.__name__ = "OctetString"
_RuckusZDSystemSNMPV2TrapServer_Object = MibTableColumn
ruckusZDSystemSNMPV2TrapServer = _RuckusZDSystemSNMPV2TrapServer_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 15, 3, 35, 1, 3),
    _RuckusZDSystemSNMPV2TrapServer_Type()
)
ruckusZDSystemSNMPV2TrapServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemSNMPV2TrapServer.setStatus("current")
_RuckusZDSystemSNMPV2TrapSvrRowStatus_Type = RowStatus
_RuckusZDSystemSNMPV2TrapSvrRowStatus_Object = MibTableColumn
ruckusZDSystemSNMPV2TrapSvrRowStatus = _RuckusZDSystemSNMPV2TrapSvrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 15, 3, 35, 1, 8),
    _RuckusZDSystemSNMPV2TrapSvrRowStatus_Type()
)
ruckusZDSystemSNMPV2TrapSvrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusZDSystemSNMPV2TrapSvrRowStatus.setStatus("current")
_RuckusZDSystemSNMPV3TrapSvrTable_Object = MibTable
ruckusZDSystemSNMPV3TrapSvrTable = _RuckusZDSystemSNMPV3TrapSvrTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 15, 3, 36)
)
if mibBuilder.loadTexts:
    ruckusZDSystemSNMPV3TrapSvrTable.setStatus("current")
_RuckusZDSystemSNMPV3TrapSvrEntry_Object = MibTableRow
ruckusZDSystemSNMPV3TrapSvrEntry = _RuckusZDSystemSNMPV3TrapSvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 15, 3, 36, 1)
)
ruckusZDSystemSNMPV3TrapSvrEntry.setIndexNames(
    (0, "RUCKUS-ZD-SYSTEM-MIB", "ruckusZDSystemSNMPV3TrapSvrIndex"),
)
if mibBuilder.loadTexts:
    ruckusZDSystemSNMPV3TrapSvrEntry.setStatus("current")


class _RuckusZDSystemSNMPV3TrapSvrIndex_Type(Integer32):
    """Custom type ruckusZDSystemSNMPV3TrapSvrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_RuckusZDSystemSNMPV3TrapSvrIndex_Type.__name__ = "Integer32"
_RuckusZDSystemSNMPV3TrapSvrIndex_Object = MibTableColumn
ruckusZDSystemSNMPV3TrapSvrIndex = _RuckusZDSystemSNMPV3TrapSvrIndex_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 15, 3, 36, 1, 1),
    _RuckusZDSystemSNMPV3TrapSvrIndex_Type()
)
ruckusZDSystemSNMPV3TrapSvrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemSNMPV3TrapSvrIndex.setStatus("current")


class _RuckusZDSystemSNMPV3TrapServer_Type(OctetString):
    """Custom type ruckusZDSystemSNMPV3TrapServer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 40),
    )


_RuckusZDSystemSNMPV3TrapServer_Type.__name__ = "OctetString"
_RuckusZDSystemSNMPV3TrapServer_Object = MibTableColumn
ruckusZDSystemSNMPV3TrapServer = _RuckusZDSystemSNMPV3TrapServer_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 15, 3, 36, 1, 5),
    _RuckusZDSystemSNMPV3TrapServer_Type()
)
ruckusZDSystemSNMPV3TrapServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemSNMPV3TrapServer.setStatus("current")


class _RuckusZDSystemSNMPV3TrapUser_Type(DisplayString):
    """Custom type ruckusZDSystemSNMPV3TrapUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuckusZDSystemSNMPV3TrapUser_Type.__name__ = "DisplayString"
_RuckusZDSystemSNMPV3TrapUser_Object = MibTableColumn
ruckusZDSystemSNMPV3TrapUser = _RuckusZDSystemSNMPV3TrapUser_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 15, 3, 36, 1, 8),
    _RuckusZDSystemSNMPV3TrapUser_Type()
)
ruckusZDSystemSNMPV3TrapUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemSNMPV3TrapUser.setStatus("current")


class _RuckusZDSystemSNMPV3TrapAuth_Type(Integer32):
    """Custom type ruckusZDSystemSNMPV3TrapAuth based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("md5", 1),
          ("sha", 2))
    )


_RuckusZDSystemSNMPV3TrapAuth_Type.__name__ = "Integer32"
_RuckusZDSystemSNMPV3TrapAuth_Object = MibTableColumn
ruckusZDSystemSNMPV3TrapAuth = _RuckusZDSystemSNMPV3TrapAuth_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 15, 3, 36, 1, 10),
    _RuckusZDSystemSNMPV3TrapAuth_Type()
)
ruckusZDSystemSNMPV3TrapAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemSNMPV3TrapAuth.setStatus("current")


class _RuckusZDSystemSNMPV3TrapAuthKey_Type(DisplayString):
    """Custom type ruckusZDSystemSNMPV3TrapAuthKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 32),
    )


_RuckusZDSystemSNMPV3TrapAuthKey_Type.__name__ = "DisplayString"
_RuckusZDSystemSNMPV3TrapAuthKey_Object = MibTableColumn
ruckusZDSystemSNMPV3TrapAuthKey = _RuckusZDSystemSNMPV3TrapAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 15, 3, 36, 1, 11),
    _RuckusZDSystemSNMPV3TrapAuthKey_Type()
)
ruckusZDSystemSNMPV3TrapAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemSNMPV3TrapAuthKey.setStatus("current")


class _RuckusZDSystemSNMPV3TrapPrivacy_Type(Integer32):
    """Custom type ruckusZDSystemSNMPV3TrapPrivacy based on Integer32"""
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
        *(("aes", 2),
          ("des", 1),
          ("none", 3))
    )


_RuckusZDSystemSNMPV3TrapPrivacy_Type.__name__ = "Integer32"
_RuckusZDSystemSNMPV3TrapPrivacy_Object = MibTableColumn
ruckusZDSystemSNMPV3TrapPrivacy = _RuckusZDSystemSNMPV3TrapPrivacy_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 15, 3, 36, 1, 15),
    _RuckusZDSystemSNMPV3TrapPrivacy_Type()
)
ruckusZDSystemSNMPV3TrapPrivacy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemSNMPV3TrapPrivacy.setStatus("current")


class _RuckusZDSystemSNMPV3TrapPrivacyKey_Type(DisplayString):
    """Custom type ruckusZDSystemSNMPV3TrapPrivacyKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 32),
    )


_RuckusZDSystemSNMPV3TrapPrivacyKey_Type.__name__ = "DisplayString"
_RuckusZDSystemSNMPV3TrapPrivacyKey_Object = MibTableColumn
ruckusZDSystemSNMPV3TrapPrivacyKey = _RuckusZDSystemSNMPV3TrapPrivacyKey_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 15, 3, 36, 1, 16),
    _RuckusZDSystemSNMPV3TrapPrivacyKey_Type()
)
ruckusZDSystemSNMPV3TrapPrivacyKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemSNMPV3TrapPrivacyKey.setStatus("current")
_RuckusZDSystemSNMPV3TrapSvrRowStatus_Type = RowStatus
_RuckusZDSystemSNMPV3TrapSvrRowStatus_Object = MibTableColumn
ruckusZDSystemSNMPV3TrapSvrRowStatus = _RuckusZDSystemSNMPV3TrapSvrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 15, 3, 36, 1, 20),
    _RuckusZDSystemSNMPV3TrapSvrRowStatus_Type()
)
ruckusZDSystemSNMPV3TrapSvrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusZDSystemSNMPV3TrapSvrRowStatus.setStatus("current")
_RuckusZDSystemSNMPV2Table_Object = MibTable
ruckusZDSystemSNMPV2Table = _RuckusZDSystemSNMPV2Table_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 15, 5)
)
if mibBuilder.loadTexts:
    ruckusZDSystemSNMPV2Table.setStatus("current")
_RuckusZDSystemSNMPV2Entry_Object = MibTableRow
ruckusZDSystemSNMPV2Entry = _RuckusZDSystemSNMPV2Entry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 15, 5, 1)
)
ruckusZDSystemSNMPV2Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ruckusZDSystemSNMPV2Entry.setStatus("current")


class _RuckusZDSystemSNMPEnable_Type(Integer32):
    """Custom type ruckusZDSystemSNMPEnable based on Integer32"""
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


_RuckusZDSystemSNMPEnable_Type.__name__ = "Integer32"
_RuckusZDSystemSNMPEnable_Object = MibTableColumn
ruckusZDSystemSNMPEnable = _RuckusZDSystemSNMPEnable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 15, 5, 1, 2),
    _RuckusZDSystemSNMPEnable_Type()
)
ruckusZDSystemSNMPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemSNMPEnable.setStatus("current")


class _RuckusZDSystemSNMPROCommunity_Type(DisplayString):
    """Custom type ruckusZDSystemSNMPROCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuckusZDSystemSNMPROCommunity_Type.__name__ = "DisplayString"
_RuckusZDSystemSNMPROCommunity_Object = MibTableColumn
ruckusZDSystemSNMPROCommunity = _RuckusZDSystemSNMPROCommunity_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 15, 5, 1, 5),
    _RuckusZDSystemSNMPROCommunity_Type()
)
ruckusZDSystemSNMPROCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemSNMPROCommunity.setStatus("current")


class _RuckusZDSystemSNMPRWCommunity_Type(DisplayString):
    """Custom type ruckusZDSystemSNMPRWCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuckusZDSystemSNMPRWCommunity_Type.__name__ = "DisplayString"
_RuckusZDSystemSNMPRWCommunity_Object = MibTableColumn
ruckusZDSystemSNMPRWCommunity = _RuckusZDSystemSNMPRWCommunity_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 15, 5, 1, 6),
    _RuckusZDSystemSNMPRWCommunity_Type()
)
ruckusZDSystemSNMPRWCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemSNMPRWCommunity.setStatus("current")


class _RuckusZDSystemSNMPSysContact_Type(DisplayString):
    """Custom type ruckusZDSystemSNMPSysContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuckusZDSystemSNMPSysContact_Type.__name__ = "DisplayString"
_RuckusZDSystemSNMPSysContact_Object = MibTableColumn
ruckusZDSystemSNMPSysContact = _RuckusZDSystemSNMPSysContact_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 15, 5, 1, 7),
    _RuckusZDSystemSNMPSysContact_Type()
)
ruckusZDSystemSNMPSysContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemSNMPSysContact.setStatus("current")


class _RuckusZDSystemSNMPSysLocation_Type(DisplayString):
    """Custom type ruckusZDSystemSNMPSysLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuckusZDSystemSNMPSysLocation_Type.__name__ = "DisplayString"
_RuckusZDSystemSNMPSysLocation_Object = MibTableColumn
ruckusZDSystemSNMPSysLocation = _RuckusZDSystemSNMPSysLocation_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 15, 5, 1, 8),
    _RuckusZDSystemSNMPSysLocation_Type()
)
ruckusZDSystemSNMPSysLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemSNMPSysLocation.setStatus("current")
_RuckusZDSystemSNMPV3Table_Object = MibTable
ruckusZDSystemSNMPV3Table = _RuckusZDSystemSNMPV3Table_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 15, 8)
)
if mibBuilder.loadTexts:
    ruckusZDSystemSNMPV3Table.setStatus("current")
_RuckusZDSystemSNMPV3Entry_Object = MibTableRow
ruckusZDSystemSNMPV3Entry = _RuckusZDSystemSNMPV3Entry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 15, 8, 1)
)
ruckusZDSystemSNMPV3Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ruckusZDSystemSNMPV3Entry.setStatus("current")


class _RuckusZDSystemSNMPV3Enable_Type(Integer32):
    """Custom type ruckusZDSystemSNMPV3Enable based on Integer32"""
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


_RuckusZDSystemSNMPV3Enable_Type.__name__ = "Integer32"
_RuckusZDSystemSNMPV3Enable_Object = MibTableColumn
ruckusZDSystemSNMPV3Enable = _RuckusZDSystemSNMPV3Enable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 15, 8, 1, 2),
    _RuckusZDSystemSNMPV3Enable_Type()
)
ruckusZDSystemSNMPV3Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemSNMPV3Enable.setStatus("current")


class _RuckusZDSystemSNMPV3RoUser_Type(DisplayString):
    """Custom type ruckusZDSystemSNMPV3RoUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_RuckusZDSystemSNMPV3RoUser_Type.__name__ = "DisplayString"
_RuckusZDSystemSNMPV3RoUser_Object = MibTableColumn
ruckusZDSystemSNMPV3RoUser = _RuckusZDSystemSNMPV3RoUser_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 15, 8, 1, 5),
    _RuckusZDSystemSNMPV3RoUser_Type()
)
ruckusZDSystemSNMPV3RoUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemSNMPV3RoUser.setStatus("current")


class _RuckusZDSystemSNMPV3RoAuth_Type(Integer32):
    """Custom type ruckusZDSystemSNMPV3RoAuth based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("md5", 1),
          ("sha", 2))
    )


_RuckusZDSystemSNMPV3RoAuth_Type.__name__ = "Integer32"
_RuckusZDSystemSNMPV3RoAuth_Object = MibTableColumn
ruckusZDSystemSNMPV3RoAuth = _RuckusZDSystemSNMPV3RoAuth_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 15, 8, 1, 6),
    _RuckusZDSystemSNMPV3RoAuth_Type()
)
ruckusZDSystemSNMPV3RoAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemSNMPV3RoAuth.setStatus("current")


class _RuckusZDSystemSNMPV3RoAuthKey_Type(DisplayString):
    """Custom type ruckusZDSystemSNMPV3RoAuthKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 32),
    )


_RuckusZDSystemSNMPV3RoAuthKey_Type.__name__ = "DisplayString"
_RuckusZDSystemSNMPV3RoAuthKey_Object = MibTableColumn
ruckusZDSystemSNMPV3RoAuthKey = _RuckusZDSystemSNMPV3RoAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 15, 8, 1, 7),
    _RuckusZDSystemSNMPV3RoAuthKey_Type()
)
ruckusZDSystemSNMPV3RoAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemSNMPV3RoAuthKey.setStatus("current")


class _RuckusZDSystemSNMPV3RoPrivacy_Type(Integer32):
    """Custom type ruckusZDSystemSNMPV3RoPrivacy based on Integer32"""
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
        *(("aes", 2),
          ("des", 1),
          ("none", 3))
    )


_RuckusZDSystemSNMPV3RoPrivacy_Type.__name__ = "Integer32"
_RuckusZDSystemSNMPV3RoPrivacy_Object = MibTableColumn
ruckusZDSystemSNMPV3RoPrivacy = _RuckusZDSystemSNMPV3RoPrivacy_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 15, 8, 1, 8),
    _RuckusZDSystemSNMPV3RoPrivacy_Type()
)
ruckusZDSystemSNMPV3RoPrivacy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemSNMPV3RoPrivacy.setStatus("current")


class _RuckusZDSystemSNMPV3RoPrivacyKey_Type(DisplayString):
    """Custom type ruckusZDSystemSNMPV3RoPrivacyKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 32),
    )


_RuckusZDSystemSNMPV3RoPrivacyKey_Type.__name__ = "DisplayString"
_RuckusZDSystemSNMPV3RoPrivacyKey_Object = MibTableColumn
ruckusZDSystemSNMPV3RoPrivacyKey = _RuckusZDSystemSNMPV3RoPrivacyKey_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 15, 8, 1, 9),
    _RuckusZDSystemSNMPV3RoPrivacyKey_Type()
)
ruckusZDSystemSNMPV3RoPrivacyKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemSNMPV3RoPrivacyKey.setStatus("current")


class _RuckusZDSystemSNMPV3RwUser_Type(DisplayString):
    """Custom type ruckusZDSystemSNMPV3RwUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_RuckusZDSystemSNMPV3RwUser_Type.__name__ = "DisplayString"
_RuckusZDSystemSNMPV3RwUser_Object = MibTableColumn
ruckusZDSystemSNMPV3RwUser = _RuckusZDSystemSNMPV3RwUser_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 15, 8, 1, 12),
    _RuckusZDSystemSNMPV3RwUser_Type()
)
ruckusZDSystemSNMPV3RwUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemSNMPV3RwUser.setStatus("current")


class _RuckusZDSystemSNMPV3RwAuth_Type(Integer32):
    """Custom type ruckusZDSystemSNMPV3RwAuth based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("md5", 1),
          ("sha", 2))
    )


_RuckusZDSystemSNMPV3RwAuth_Type.__name__ = "Integer32"
_RuckusZDSystemSNMPV3RwAuth_Object = MibTableColumn
ruckusZDSystemSNMPV3RwAuth = _RuckusZDSystemSNMPV3RwAuth_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 15, 8, 1, 13),
    _RuckusZDSystemSNMPV3RwAuth_Type()
)
ruckusZDSystemSNMPV3RwAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemSNMPV3RwAuth.setStatus("current")


class _RuckusZDSystemSNMPV3RwAuthKey_Type(DisplayString):
    """Custom type ruckusZDSystemSNMPV3RwAuthKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 32),
    )


_RuckusZDSystemSNMPV3RwAuthKey_Type.__name__ = "DisplayString"
_RuckusZDSystemSNMPV3RwAuthKey_Object = MibTableColumn
ruckusZDSystemSNMPV3RwAuthKey = _RuckusZDSystemSNMPV3RwAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 15, 8, 1, 14),
    _RuckusZDSystemSNMPV3RwAuthKey_Type()
)
ruckusZDSystemSNMPV3RwAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemSNMPV3RwAuthKey.setStatus("current")


class _RuckusZDSystemSNMPV3RwPrivacy_Type(Integer32):
    """Custom type ruckusZDSystemSNMPV3RwPrivacy based on Integer32"""
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
        *(("aes", 2),
          ("des", 1),
          ("none", 3))
    )


_RuckusZDSystemSNMPV3RwPrivacy_Type.__name__ = "Integer32"
_RuckusZDSystemSNMPV3RwPrivacy_Object = MibTableColumn
ruckusZDSystemSNMPV3RwPrivacy = _RuckusZDSystemSNMPV3RwPrivacy_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 15, 8, 1, 15),
    _RuckusZDSystemSNMPV3RwPrivacy_Type()
)
ruckusZDSystemSNMPV3RwPrivacy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemSNMPV3RwPrivacy.setStatus("current")


class _RuckusZDSystemSNMPV3RwPrivacyKey_Type(DisplayString):
    """Custom type ruckusZDSystemSNMPV3RwPrivacyKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 32),
    )


_RuckusZDSystemSNMPV3RwPrivacyKey_Type.__name__ = "DisplayString"
_RuckusZDSystemSNMPV3RwPrivacyKey_Object = MibTableColumn
ruckusZDSystemSNMPV3RwPrivacyKey = _RuckusZDSystemSNMPV3RwPrivacyKey_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 15, 8, 1, 16),
    _RuckusZDSystemSNMPV3RwPrivacyKey_Type()
)
ruckusZDSystemSNMPV3RwPrivacyKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemSNMPV3RwPrivacyKey.setStatus("current")
_RuckusZDSystemLoadBalanceInfo_ObjectIdentity = ObjectIdentity
ruckusZDSystemLoadBalanceInfo = _RuckusZDSystemLoadBalanceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 20)
)
_RuckusZDSystemLoadBalanceStatus_Type = TruthValue
_RuckusZDSystemLoadBalanceStatus_Object = MibScalar
ruckusZDSystemLoadBalanceStatus = _RuckusZDSystemLoadBalanceStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 20, 1),
    _RuckusZDSystemLoadBalanceStatus_Type()
)
ruckusZDSystemLoadBalanceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemLoadBalanceStatus.setStatus("current")
_RuckusZDSystemLoadBalanceUserThreshold_Type = Unsigned32
_RuckusZDSystemLoadBalanceUserThreshold_Object = MibScalar
ruckusZDSystemLoadBalanceUserThreshold = _RuckusZDSystemLoadBalanceUserThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 20, 2),
    _RuckusZDSystemLoadBalanceUserThreshold_Type()
)
ruckusZDSystemLoadBalanceUserThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemLoadBalanceUserThreshold.setStatus("current")
_RuckusZDSystemLoadBalanceUserDifference_Type = Unsigned32
_RuckusZDSystemLoadBalanceUserDifference_Object = MibScalar
ruckusZDSystemLoadBalanceUserDifference = _RuckusZDSystemLoadBalanceUserDifference_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 20, 3),
    _RuckusZDSystemLoadBalanceUserDifference_Type()
)
ruckusZDSystemLoadBalanceUserDifference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemLoadBalanceUserDifference.setStatus("current")
_RuckusZDSystemLoadBalanceTrafficThreshold_Type = Unsigned32
_RuckusZDSystemLoadBalanceTrafficThreshold_Object = MibScalar
ruckusZDSystemLoadBalanceTrafficThreshold = _RuckusZDSystemLoadBalanceTrafficThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 20, 4),
    _RuckusZDSystemLoadBalanceTrafficThreshold_Type()
)
ruckusZDSystemLoadBalanceTrafficThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemLoadBalanceTrafficThreshold.setStatus("current")
_RuckusZDSystemLoadBalanceTrafficDifference_Type = Unsigned32
_RuckusZDSystemLoadBalanceTrafficDifference_Object = MibScalar
ruckusZDSystemLoadBalanceTrafficDifference = _RuckusZDSystemLoadBalanceTrafficDifference_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 20, 5),
    _RuckusZDSystemLoadBalanceTrafficDifference_Type()
)
ruckusZDSystemLoadBalanceTrafficDifference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemLoadBalanceTrafficDifference.setStatus("current")
if mibBuilder.loadTexts:
    ruckusZDSystemLoadBalanceTrafficDifference.setUnits("Kbps")


class _RuckusZDSystemLoadBalanceType_Type(Integer32):
    """Custom type ruckusZDSystemLoadBalanceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("traffic", 2),
          ("user", 1))
    )


_RuckusZDSystemLoadBalanceType_Type.__name__ = "Integer32"
_RuckusZDSystemLoadBalanceType_Object = MibScalar
ruckusZDSystemLoadBalanceType = _RuckusZDSystemLoadBalanceType_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 12, 20, 6),
    _RuckusZDSystemLoadBalanceType_Type()
)
ruckusZDSystemLoadBalanceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDSystemLoadBalanceType.setStatus("current")
_RuckusZDSystemStats_ObjectIdentity = ObjectIdentity
ruckusZDSystemStats = _RuckusZDSystemStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 15)
)
_RuckusZDSystemStatsNumAP_Type = Unsigned32
_RuckusZDSystemStatsNumAP_Object = MibScalar
ruckusZDSystemStatsNumAP = _RuckusZDSystemStatsNumAP_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 15, 1),
    _RuckusZDSystemStatsNumAP_Type()
)
ruckusZDSystemStatsNumAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemStatsNumAP.setStatus("current")
_RuckusZDSystemStatsNumSta_Type = Unsigned32
_RuckusZDSystemStatsNumSta_Object = MibScalar
ruckusZDSystemStatsNumSta = _RuckusZDSystemStatsNumSta_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 15, 2),
    _RuckusZDSystemStatsNumSta_Type()
)
ruckusZDSystemStatsNumSta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemStatsNumSta.setStatus("current")
_RuckusZDSystemStatsNumRogue_Type = Unsigned32
_RuckusZDSystemStatsNumRogue_Object = MibScalar
ruckusZDSystemStatsNumRogue = _RuckusZDSystemStatsNumRogue_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 15, 3),
    _RuckusZDSystemStatsNumRogue_Type()
)
ruckusZDSystemStatsNumRogue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemStatsNumRogue.setStatus("current")
_RuckusZDSystemStatsNumRogueKnown_Type = Unsigned32
_RuckusZDSystemStatsNumRogueKnown_Object = MibScalar
ruckusZDSystemStatsNumRogueKnown = _RuckusZDSystemStatsNumRogueKnown_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 15, 4),
    _RuckusZDSystemStatsNumRogueKnown_Type()
)
ruckusZDSystemStatsNumRogueKnown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemStatsNumRogueKnown.setStatus("current")
_RuckusZDSystemStatsWLANTotalRxPkts_Type = Counter64
_RuckusZDSystemStatsWLANTotalRxPkts_Object = MibScalar
ruckusZDSystemStatsWLANTotalRxPkts = _RuckusZDSystemStatsWLANTotalRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 15, 5),
    _RuckusZDSystemStatsWLANTotalRxPkts_Type()
)
ruckusZDSystemStatsWLANTotalRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemStatsWLANTotalRxPkts.setStatus("current")
_RuckusZDSystemStatsWLANTotalRxBytes_Type = Counter64
_RuckusZDSystemStatsWLANTotalRxBytes_Object = MibScalar
ruckusZDSystemStatsWLANTotalRxBytes = _RuckusZDSystemStatsWLANTotalRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 15, 6),
    _RuckusZDSystemStatsWLANTotalRxBytes_Type()
)
ruckusZDSystemStatsWLANTotalRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemStatsWLANTotalRxBytes.setStatus("current")
_RuckusZDSystemStatsWLANTotalRxMulticast_Type = Counter64
_RuckusZDSystemStatsWLANTotalRxMulticast_Object = MibScalar
ruckusZDSystemStatsWLANTotalRxMulticast = _RuckusZDSystemStatsWLANTotalRxMulticast_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 15, 7),
    _RuckusZDSystemStatsWLANTotalRxMulticast_Type()
)
ruckusZDSystemStatsWLANTotalRxMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemStatsWLANTotalRxMulticast.setStatus("current")
_RuckusZDSystemStatsWLANTotalTxPkts_Type = Counter64
_RuckusZDSystemStatsWLANTotalTxPkts_Object = MibScalar
ruckusZDSystemStatsWLANTotalTxPkts = _RuckusZDSystemStatsWLANTotalTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 15, 8),
    _RuckusZDSystemStatsWLANTotalTxPkts_Type()
)
ruckusZDSystemStatsWLANTotalTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemStatsWLANTotalTxPkts.setStatus("current")
_RuckusZDSystemStatsWLANTotalTxBytes_Type = Counter64
_RuckusZDSystemStatsWLANTotalTxBytes_Object = MibScalar
ruckusZDSystemStatsWLANTotalTxBytes = _RuckusZDSystemStatsWLANTotalTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 15, 9),
    _RuckusZDSystemStatsWLANTotalTxBytes_Type()
)
ruckusZDSystemStatsWLANTotalTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemStatsWLANTotalTxBytes.setStatus("current")
_RuckusZDSystemStatsWLANTotalTxMulticast_Type = Counter64
_RuckusZDSystemStatsWLANTotalTxMulticast_Object = MibScalar
ruckusZDSystemStatsWLANTotalTxMulticast = _RuckusZDSystemStatsWLANTotalTxMulticast_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 15, 10),
    _RuckusZDSystemStatsWLANTotalTxMulticast_Type()
)
ruckusZDSystemStatsWLANTotalTxMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemStatsWLANTotalTxMulticast.setStatus("current")
_RuckusZDSystemStatsWLANTotalTxFail_Type = Counter64
_RuckusZDSystemStatsWLANTotalTxFail_Object = MibScalar
ruckusZDSystemStatsWLANTotalTxFail = _RuckusZDSystemStatsWLANTotalTxFail_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 15, 11),
    _RuckusZDSystemStatsWLANTotalTxFail_Type()
)
ruckusZDSystemStatsWLANTotalTxFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemStatsWLANTotalTxFail.setStatus("current")
_RuckusZDSystemStatsWLANTotalTxRetry_Type = Counter64
_RuckusZDSystemStatsWLANTotalTxRetry_Object = MibScalar
ruckusZDSystemStatsWLANTotalTxRetry = _RuckusZDSystemStatsWLANTotalTxRetry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 15, 12),
    _RuckusZDSystemStatsWLANTotalTxRetry_Type()
)
ruckusZDSystemStatsWLANTotalTxRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemStatsWLANTotalTxRetry.setStatus("current")
_RuckusZDSystemStatsCPUUtil_Type = Unsigned32
_RuckusZDSystemStatsCPUUtil_Object = MibScalar
ruckusZDSystemStatsCPUUtil = _RuckusZDSystemStatsCPUUtil_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 15, 13),
    _RuckusZDSystemStatsCPUUtil_Type()
)
ruckusZDSystemStatsCPUUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemStatsCPUUtil.setStatus("current")
_RuckusZDSystemStatsMemoryUtil_Type = Unsigned32
_RuckusZDSystemStatsMemoryUtil_Object = MibScalar
ruckusZDSystemStatsMemoryUtil = _RuckusZDSystemStatsMemoryUtil_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 15, 14),
    _RuckusZDSystemStatsMemoryUtil_Type()
)
ruckusZDSystemStatsMemoryUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemStatsMemoryUtil.setStatus("current")
_RuckusZDSystemStatsNumRegisteredAP_Type = Unsigned32
_RuckusZDSystemStatsNumRegisteredAP_Object = MibScalar
ruckusZDSystemStatsNumRegisteredAP = _RuckusZDSystemStatsNumRegisteredAP_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 15, 15),
    _RuckusZDSystemStatsNumRegisteredAP_Type()
)
ruckusZDSystemStatsNumRegisteredAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemStatsNumRegisteredAP.setStatus("current")
_RuckusZDSystemStatsWLANTotalAssocFail_Type = Counter64
_RuckusZDSystemStatsWLANTotalAssocFail_Object = MibScalar
ruckusZDSystemStatsWLANTotalAssocFail = _RuckusZDSystemStatsWLANTotalAssocFail_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 15, 16),
    _RuckusZDSystemStatsWLANTotalAssocFail_Type()
)
ruckusZDSystemStatsWLANTotalAssocFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemStatsWLANTotalAssocFail.setStatus("current")
_RuckusZDSystemStatsWLANTotalRxErrFrm_Type = Counter64
_RuckusZDSystemStatsWLANTotalRxErrFrm_Object = MibScalar
ruckusZDSystemStatsWLANTotalRxErrFrm = _RuckusZDSystemStatsWLANTotalRxErrFrm_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 15, 17),
    _RuckusZDSystemStatsWLANTotalRxErrFrm_Type()
)
ruckusZDSystemStatsWLANTotalRxErrFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemStatsWLANTotalRxErrFrm.setStatus("current")
_RuckusZDSystemStatsWLANTotalTxDroppedPkt_Type = Counter64
_RuckusZDSystemStatsWLANTotalTxDroppedPkt_Object = MibScalar
ruckusZDSystemStatsWLANTotalTxDroppedPkt = _RuckusZDSystemStatsWLANTotalTxDroppedPkt_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 15, 19),
    _RuckusZDSystemStatsWLANTotalTxDroppedPkt_Type()
)
ruckusZDSystemStatsWLANTotalTxDroppedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemStatsWLANTotalTxDroppedPkt.setStatus("current")
_RuckusZDSystemStatsWLANTotalTxErrFrm_Type = Counter64
_RuckusZDSystemStatsWLANTotalTxErrFrm_Object = MibScalar
ruckusZDSystemStatsWLANTotalTxErrFrm = _RuckusZDSystemStatsWLANTotalTxErrFrm_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 15, 20),
    _RuckusZDSystemStatsWLANTotalTxErrFrm_Type()
)
ruckusZDSystemStatsWLANTotalTxErrFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemStatsWLANTotalTxErrFrm.setStatus("current")
_RuckusZDSystemStatsWLANTotalTxDroppedFrm_Type = Counter64
_RuckusZDSystemStatsWLANTotalTxDroppedFrm_Object = MibScalar
ruckusZDSystemStatsWLANTotalTxDroppedFrm = _RuckusZDSystemStatsWLANTotalTxDroppedFrm_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 15, 21),
    _RuckusZDSystemStatsWLANTotalTxDroppedFrm_Type()
)
ruckusZDSystemStatsWLANTotalTxDroppedFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemStatsWLANTotalTxDroppedFrm.setStatus("current")
_RuckusZDSystemStatsLanTxRate_Type = Unsigned32
_RuckusZDSystemStatsLanTxRate_Object = MibScalar
ruckusZDSystemStatsLanTxRate = _RuckusZDSystemStatsLanTxRate_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 15, 23),
    _RuckusZDSystemStatsLanTxRate_Type()
)
ruckusZDSystemStatsLanTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemStatsLanTxRate.setStatus("current")
_RuckusZDSystemStatsLanRxRate_Type = Unsigned32
_RuckusZDSystemStatsLanRxRate_Object = MibScalar
ruckusZDSystemStatsLanRxRate = _RuckusZDSystemStatsLanRxRate_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 15, 24),
    _RuckusZDSystemStatsLanRxRate_Type()
)
ruckusZDSystemStatsLanRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemStatsLanRxRate.setStatus("current")
_RuckusZDSystemStatsAllNumSta_Type = Unsigned32
_RuckusZDSystemStatsAllNumSta_Object = MibScalar
ruckusZDSystemStatsAllNumSta = _RuckusZDSystemStatsAllNumSta_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 15, 30),
    _RuckusZDSystemStatsAllNumSta_Type()
)
ruckusZDSystemStatsAllNumSta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDSystemStatsAllNumSta.setStatus("current")
_RuckusZDEthInfo_ObjectIdentity = ObjectIdentity
ruckusZDEthInfo = _RuckusZDEthInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 18)
)
_RuckusZDEthNum_Type = Unsigned32
_RuckusZDEthNum_Object = MibScalar
ruckusZDEthNum = _RuckusZDEthNum_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 18, 1),
    _RuckusZDEthNum_Type()
)
ruckusZDEthNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDEthNum.setStatus("current")
_RuckusZDEthTable_Object = MibTable
ruckusZDEthTable = _RuckusZDEthTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 18, 2)
)
if mibBuilder.loadTexts:
    ruckusZDEthTable.setStatus("current")
_RuckusZDEthEntry_Object = MibTableRow
ruckusZDEthEntry = _RuckusZDEthEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 18, 2, 1)
)
ruckusZDEthEntry.setIndexNames(
    (0, "RUCKUS-ZD-SYSTEM-MIB", "ruckusZDEthIfIndex"),
)
if mibBuilder.loadTexts:
    ruckusZDEthEntry.setStatus("current")
_RuckusZDEthIfIndex_Type = Unsigned32
_RuckusZDEthIfIndex_Object = MibTableColumn
ruckusZDEthIfIndex = _RuckusZDEthIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 18, 2, 1, 1),
    _RuckusZDEthIfIndex_Type()
)
ruckusZDEthIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDEthIfIndex.setStatus("current")
_RuckusZDEthName_Type = DisplayString
_RuckusZDEthName_Object = MibTableColumn
ruckusZDEthName = _RuckusZDEthName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 18, 2, 1, 2),
    _RuckusZDEthName_Type()
)
ruckusZDEthName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEthName.setStatus("current")
_RuckusZDEthDesc_Type = DisplayString
_RuckusZDEthDesc_Object = MibTableColumn
ruckusZDEthDesc = _RuckusZDEthDesc_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 18, 2, 1, 3),
    _RuckusZDEthDesc_Type()
)
ruckusZDEthDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDEthDesc.setStatus("current")


class _RuckusZDEthType_Type(Integer32):
    """Custom type ruckusZDEthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-csmacd", 2),
          ("other", 1))
    )


_RuckusZDEthType_Type.__name__ = "Integer32"
_RuckusZDEthType_Object = MibTableColumn
ruckusZDEthType = _RuckusZDEthType_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 18, 2, 1, 4),
    _RuckusZDEthType_Type()
)
ruckusZDEthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDEthType.setStatus("current")


class _RuckusZDEthStatus_Type(Integer32):
    """Custom type ruckusZDEthStatus based on Integer32"""
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


_RuckusZDEthStatus_Type.__name__ = "Integer32"
_RuckusZDEthStatus_Object = MibTableColumn
ruckusZDEthStatus = _RuckusZDEthStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 18, 2, 1, 5),
    _RuckusZDEthStatus_Type()
)
ruckusZDEthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDEthStatus.setStatus("current")
_RuckusZDEthPhysAddr_Type = MacAddress
_RuckusZDEthPhysAddr_Object = MibTableColumn
ruckusZDEthPhysAddr = _RuckusZDEthPhysAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 18, 2, 1, 6),
    _RuckusZDEthPhysAddr_Type()
)
ruckusZDEthPhysAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDEthPhysAddr.setStatus("current")
_RuckusZDEthMtu_Type = Unsigned32
_RuckusZDEthMtu_Object = MibTableColumn
ruckusZDEthMtu = _RuckusZDEthMtu_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 18, 2, 1, 7),
    _RuckusZDEthMtu_Type()
)
ruckusZDEthMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDEthMtu.setStatus("current")
_RuckusZDEthIfSpeed_Type = Unsigned32
_RuckusZDEthIfSpeed_Object = MibTableColumn
ruckusZDEthIfSpeed = _RuckusZDEthIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 18, 2, 1, 8),
    _RuckusZDEthIfSpeed_Type()
)
ruckusZDEthIfSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDEthIfSpeed.setStatus("current")
if mibBuilder.loadTexts:
    ruckusZDEthIfSpeed.setUnits("Mbps")
_RuckusZDEthUtil_Type = Integer32
_RuckusZDEthUtil_Object = MibTableColumn
ruckusZDEthUtil = _RuckusZDEthUtil_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 18, 2, 1, 9),
    _RuckusZDEthUtil_Type()
)
ruckusZDEthUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDEthUtil.setStatus("current")
_RuckusZDEthTxBcastPkts_Type = Counter32
_RuckusZDEthTxBcastPkts_Object = MibTableColumn
ruckusZDEthTxBcastPkts = _RuckusZDEthTxBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 18, 2, 1, 10),
    _RuckusZDEthTxBcastPkts_Type()
)
ruckusZDEthTxBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDEthTxBcastPkts.setStatus("current")
_RuckusZDEthTxMcastPkts_Type = Counter32
_RuckusZDEthTxMcastPkts_Object = MibTableColumn
ruckusZDEthTxMcastPkts = _RuckusZDEthTxMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 18, 2, 1, 11),
    _RuckusZDEthTxMcastPkts_Type()
)
ruckusZDEthTxMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDEthTxMcastPkts.setStatus("current")
_RuckusZDEthRxBcastPkts_Type = Counter32
_RuckusZDEthRxBcastPkts_Object = MibTableColumn
ruckusZDEthRxBcastPkts = _RuckusZDEthRxBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 18, 2, 1, 12),
    _RuckusZDEthRxBcastPkts_Type()
)
ruckusZDEthRxBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDEthRxBcastPkts.setStatus("current")
_RuckusZDEthRxMcastPkts_Type = Counter32
_RuckusZDEthRxMcastPkts_Object = MibTableColumn
ruckusZDEthRxMcastPkts = _RuckusZDEthRxMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 18, 2, 1, 13),
    _RuckusZDEthRxMcastPkts_Type()
)
ruckusZDEthRxMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDEthRxMcastPkts.setStatus("current")
_RuckusZDEthTxUniPkts_Type = Counter32
_RuckusZDEthTxUniPkts_Object = MibTableColumn
ruckusZDEthTxUniPkts = _RuckusZDEthTxUniPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 18, 2, 1, 14),
    _RuckusZDEthTxUniPkts_Type()
)
ruckusZDEthTxUniPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDEthTxUniPkts.setStatus("current")
_RuckusZDEthRxUniPkts_Type = Counter32
_RuckusZDEthRxUniPkts_Object = MibTableColumn
ruckusZDEthRxUniPkts = _RuckusZDEthRxUniPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 18, 2, 1, 15),
    _RuckusZDEthRxUniPkts_Type()
)
ruckusZDEthRxUniPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDEthRxUniPkts.setStatus("current")
_RuckusZDEthTxPkts_Type = Counter32
_RuckusZDEthTxPkts_Object = MibTableColumn
ruckusZDEthTxPkts = _RuckusZDEthTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 18, 2, 1, 16),
    _RuckusZDEthTxPkts_Type()
)
ruckusZDEthTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDEthTxPkts.setStatus("current")
_RuckusZDEthRxPkts_Type = Counter32
_RuckusZDEthRxPkts_Object = MibTableColumn
ruckusZDEthRxPkts = _RuckusZDEthRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 18, 2, 1, 17),
    _RuckusZDEthRxPkts_Type()
)
ruckusZDEthRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDEthRxPkts.setStatus("current")
_RuckusZDEthDropTxPkts_Type = Counter32
_RuckusZDEthDropTxPkts_Object = MibTableColumn
ruckusZDEthDropTxPkts = _RuckusZDEthDropTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 18, 2, 1, 18),
    _RuckusZDEthDropTxPkts_Type()
)
ruckusZDEthDropTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDEthDropTxPkts.setStatus("current")
_RuckusZDEthDropRxPkts_Type = Counter32
_RuckusZDEthDropRxPkts_Object = MibTableColumn
ruckusZDEthDropRxPkts = _RuckusZDEthDropRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 18, 2, 1, 19),
    _RuckusZDEthDropRxPkts_Type()
)
ruckusZDEthDropRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDEthDropRxPkts.setStatus("current")
_RuckusZDEthTxBytes_Type = Counter32
_RuckusZDEthTxBytes_Object = MibTableColumn
ruckusZDEthTxBytes = _RuckusZDEthTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 18, 2, 1, 20),
    _RuckusZDEthTxBytes_Type()
)
ruckusZDEthTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDEthTxBytes.setStatus("current")
_RuckusZDEthRxBytes_Type = Counter32
_RuckusZDEthRxBytes_Object = MibTableColumn
ruckusZDEthRxBytes = _RuckusZDEthRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1, 1, 1, 18, 2, 1, 21),
    _RuckusZDEthRxBytes_Type()
)
ruckusZDEthRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDEthRxBytes.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUCKUS-ZD-SYSTEM-MIB",
    **{"ruckusZDSystemMIB": ruckusZDSystemMIB,
       "ruckusZDSystemObjects": ruckusZDSystemObjects,
       "ruckusZDSystemInfo": ruckusZDSystemInfo,
       "ruckusZDSystemName": ruckusZDSystemName,
       "ruckusZDSystemIPAddr": ruckusZDSystemIPAddr,
       "ruckusZDSystemMacAddr": ruckusZDSystemMacAddr,
       "ruckusZDSystemUptime": ruckusZDSystemUptime,
       "ruckusZDSystemModel": ruckusZDSystemModel,
       "ruckusZDSystemLicensedAPs": ruckusZDSystemLicensedAPs,
       "ruckusZDSystemMaxSta": ruckusZDSystemMaxSta,
       "ruckusZDSystemSerialNumber": ruckusZDSystemSerialNumber,
       "ruckusZDSystemVersion": ruckusZDSystemVersion,
       "ruckusZDSystemCountryCode": ruckusZDSystemCountryCode,
       "ruckusZDSystemAdminName": ruckusZDSystemAdminName,
       "ruckusZDSystemAdminPassword": ruckusZDSystemAdminPassword,
       "ruckusZDSystemStatus": ruckusZDSystemStatus,
       "ruckusZDSystemPeerConnectedStatus": ruckusZDSystemPeerConnectedStatus,
       "ruckusZDSystemExpInfo": ruckusZDSystemExpInfo,
       "ruckusZDSystemNEId": ruckusZDSystemNEId,
       "ruckusZDSystemManufacturer": ruckusZDSystemManufacturer,
       "ruckusZDSystemSoftwareName": ruckusZDSystemSoftwareName,
       "ruckusZDSystemCPUUtil": ruckusZDSystemCPUUtil,
       "ruckusZDSystemMemoryUtil": ruckusZDSystemMemoryUtil,
       "ruckusZDSystemMemorySize": ruckusZDSystemMemorySize,
       "ruckusZDSystemFlashFreeSize": ruckusZDSystemFlashFreeSize,
       "ruckusZDSystemMgmtVlanID": ruckusZDSystemMgmtVlanID,
       "ruckusZDSystemtCPUSpeed": ruckusZDSystemtCPUSpeed,
       "ruckusZDSystemtFlashModel": ruckusZDSystemtFlashModel,
       "ruckusZDSystemtMemModel": ruckusZDSystemtMemModel,
       "ruckusZDSystemStartTime": ruckusZDSystemStartTime,
       "ruckusZDSystemCurrentTime": ruckusZDSystemCurrentTime,
       "ruckusZDSystemAPFirmwareServer": ruckusZDSystemAPFirmwareServer,
       "ruckusZDSystemAPConfigServer": ruckusZDSystemAPConfigServer,
       "ruckusZDSystemIDSAllowedESSID": ruckusZDSystemIDSAllowedESSID,
       "ruckusZDSystemIDSAllowBSSID": ruckusZDSystemIDSAllowBSSID,
       "ruckusZDSystemIDSAllowOUI": ruckusZDSystemIDSAllowOUI,
       "ruckusZDSystemBandwidthUtilValve": ruckusZDSystemBandwidthUtilValve,
       "ruckusZDSystemDropPacketRateValve": ruckusZDSystemDropPacketRateValve,
       "ruckusZDSystemCPUUtilValve": ruckusZDSystemCPUUtilValve,
       "ruckusZDSystemMemUtilValve": ruckusZDSystemMemUtilValve,
       "ruckusZDSystemOnlineStaValve": ruckusZDSystemOnlineStaValve,
       "ruckusZDSystemACLocationLongitude": ruckusZDSystemACLocationLongitude,
       "ruckusZDSystemACLocationLatitude": ruckusZDSystemACLocationLatitude,
       "ruckusZDSystemDHCPServer": ruckusZDSystemDHCPServer,
       "ruckusZDAPCPUvalve": ruckusZDAPCPUvalve,
       "ruckusZDAPMemoryvalve": ruckusZDAPMemoryvalve,
       "ruckusZDHeartBeatStatus": ruckusZDHeartBeatStatus,
       "ruckusZDHeartBeatPeriod": ruckusZDHeartBeatPeriod,
       "ruckusZDSystemIPTable": ruckusZDSystemIPTable,
       "ruckusZDSystemIPEntry": ruckusZDSystemIPEntry,
       "ruckusZDSystemIPVersion": ruckusZDSystemIPVersion,
       "ruckusZDSystemIPAddrMode": ruckusZDSystemIPAddrMode,
       "ruckusZDSystemIPAddress": ruckusZDSystemIPAddress,
       "ruckusZDSystemIPAddrNetmask": ruckusZDSystemIPAddrNetmask,
       "ruckusZDSystemIPGateway": ruckusZDSystemIPGateway,
       "ruckusZDSystemIPPrimaryDNS": ruckusZDSystemIPPrimaryDNS,
       "ruckusZDSystemIPSecondaryDNS": ruckusZDSystemIPSecondaryDNS,
       "ruckusZDSystemIPV6AddressModel": ruckusZDSystemIPV6AddressModel,
       "ruckusZDSystemIPV6Address": ruckusZDSystemIPV6Address,
       "ruckusZDSystemIPV6PrefixLen": ruckusZDSystemIPV6PrefixLen,
       "ruckusZDSystemIPV6Gateway": ruckusZDSystemIPV6Gateway,
       "ruckusZDSystemIPV6PrimaryDNS": ruckusZDSystemIPV6PrimaryDNS,
       "ruckusZDSystemIPV6SecondaryDNS": ruckusZDSystemIPV6SecondaryDNS,
       "ruckusZDSystemServices": ruckusZDSystemServices,
       "ruckusZDSystemNTP": ruckusZDSystemNTP,
       "ruckusZDSystemTimeWithNTP": ruckusZDSystemTimeWithNTP,
       "ruckusZDSystemTimeNTPServer": ruckusZDSystemTimeNTPServer,
       "ruckusZDSystemSMTP": ruckusZDSystemSMTP,
       "ruckusZDSystemEmailTriggerEnable": ruckusZDSystemEmailTriggerEnable,
       "ruckusZDSystemEmailAddress": ruckusZDSystemEmailAddress,
       "ruckusZDSystemSMTPServerName": ruckusZDSystemSMTPServerName,
       "ruckusZDSystemSMTPServerPort": ruckusZDSystemSMTPServerPort,
       "ruckusZDSystemSMTPAuthUsername": ruckusZDSystemSMTPAuthUsername,
       "ruckusZDSystemSMTPAuthPassword": ruckusZDSystemSMTPAuthPassword,
       "ruckusZDSystemFromEmailAddress": ruckusZDSystemFromEmailAddress,
       "ruckusZDSystemSMTPEncryptionOptions": ruckusZDSystemSMTPEncryptionOptions,
       "ruckusZDSystemSyslog": ruckusZDSystemSyslog,
       "ruckusZDSystemLogWithSysLog": ruckusZDSystemLogWithSysLog,
       "ruckusZDSystemSysLogServer": ruckusZDSystemSysLogServer,
       "ruckusZDSystemFlexMaster": ruckusZDSystemFlexMaster,
       "ruckusZDSystemFlexMasterEnable": ruckusZDSystemFlexMasterEnable,
       "ruckusZDSystemFlexMasterServer": ruckusZDSystemFlexMasterServer,
       "ruckusZDSystemFlexMasterInterval": ruckusZDSystemFlexMasterInterval,
       "ruckusZDSystemStpInfo": ruckusZDSystemStpInfo,
       "ruckusZDSystemStpStatus": ruckusZDSystemStpStatus,
       "ruckusZDSystemSNMP": ruckusZDSystemSNMP,
       "ruckusZDSystemSNMPTrapInfo": ruckusZDSystemSNMPTrapInfo,
       "ruckusZDSystemSNMPTrapEnable": ruckusZDSystemSNMPTrapEnable,
       "ruckusZDSystemSNMPTrapVersion": ruckusZDSystemSNMPTrapVersion,
       "ruckusZDSystemSNMPV2TrapSvrTable": ruckusZDSystemSNMPV2TrapSvrTable,
       "ruckusZDSystemSNMPV2TrapSvrEntry": ruckusZDSystemSNMPV2TrapSvrEntry,
       "ruckusZDSystemSNMPV2TrapSvrIndex": ruckusZDSystemSNMPV2TrapSvrIndex,
       "ruckusZDSystemSNMPV2TrapServer": ruckusZDSystemSNMPV2TrapServer,
       "ruckusZDSystemSNMPV2TrapSvrRowStatus": ruckusZDSystemSNMPV2TrapSvrRowStatus,
       "ruckusZDSystemSNMPV3TrapSvrTable": ruckusZDSystemSNMPV3TrapSvrTable,
       "ruckusZDSystemSNMPV3TrapSvrEntry": ruckusZDSystemSNMPV3TrapSvrEntry,
       "ruckusZDSystemSNMPV3TrapSvrIndex": ruckusZDSystemSNMPV3TrapSvrIndex,
       "ruckusZDSystemSNMPV3TrapServer": ruckusZDSystemSNMPV3TrapServer,
       "ruckusZDSystemSNMPV3TrapUser": ruckusZDSystemSNMPV3TrapUser,
       "ruckusZDSystemSNMPV3TrapAuth": ruckusZDSystemSNMPV3TrapAuth,
       "ruckusZDSystemSNMPV3TrapAuthKey": ruckusZDSystemSNMPV3TrapAuthKey,
       "ruckusZDSystemSNMPV3TrapPrivacy": ruckusZDSystemSNMPV3TrapPrivacy,
       "ruckusZDSystemSNMPV3TrapPrivacyKey": ruckusZDSystemSNMPV3TrapPrivacyKey,
       "ruckusZDSystemSNMPV3TrapSvrRowStatus": ruckusZDSystemSNMPV3TrapSvrRowStatus,
       "ruckusZDSystemSNMPV2Table": ruckusZDSystemSNMPV2Table,
       "ruckusZDSystemSNMPV2Entry": ruckusZDSystemSNMPV2Entry,
       "ruckusZDSystemSNMPEnable": ruckusZDSystemSNMPEnable,
       "ruckusZDSystemSNMPROCommunity": ruckusZDSystemSNMPROCommunity,
       "ruckusZDSystemSNMPRWCommunity": ruckusZDSystemSNMPRWCommunity,
       "ruckusZDSystemSNMPSysContact": ruckusZDSystemSNMPSysContact,
       "ruckusZDSystemSNMPSysLocation": ruckusZDSystemSNMPSysLocation,
       "ruckusZDSystemSNMPV3Table": ruckusZDSystemSNMPV3Table,
       "ruckusZDSystemSNMPV3Entry": ruckusZDSystemSNMPV3Entry,
       "ruckusZDSystemSNMPV3Enable": ruckusZDSystemSNMPV3Enable,
       "ruckusZDSystemSNMPV3RoUser": ruckusZDSystemSNMPV3RoUser,
       "ruckusZDSystemSNMPV3RoAuth": ruckusZDSystemSNMPV3RoAuth,
       "ruckusZDSystemSNMPV3RoAuthKey": ruckusZDSystemSNMPV3RoAuthKey,
       "ruckusZDSystemSNMPV3RoPrivacy": ruckusZDSystemSNMPV3RoPrivacy,
       "ruckusZDSystemSNMPV3RoPrivacyKey": ruckusZDSystemSNMPV3RoPrivacyKey,
       "ruckusZDSystemSNMPV3RwUser": ruckusZDSystemSNMPV3RwUser,
       "ruckusZDSystemSNMPV3RwAuth": ruckusZDSystemSNMPV3RwAuth,
       "ruckusZDSystemSNMPV3RwAuthKey": ruckusZDSystemSNMPV3RwAuthKey,
       "ruckusZDSystemSNMPV3RwPrivacy": ruckusZDSystemSNMPV3RwPrivacy,
       "ruckusZDSystemSNMPV3RwPrivacyKey": ruckusZDSystemSNMPV3RwPrivacyKey,
       "ruckusZDSystemLoadBalanceInfo": ruckusZDSystemLoadBalanceInfo,
       "ruckusZDSystemLoadBalanceStatus": ruckusZDSystemLoadBalanceStatus,
       "ruckusZDSystemLoadBalanceUserThreshold": ruckusZDSystemLoadBalanceUserThreshold,
       "ruckusZDSystemLoadBalanceUserDifference": ruckusZDSystemLoadBalanceUserDifference,
       "ruckusZDSystemLoadBalanceTrafficThreshold": ruckusZDSystemLoadBalanceTrafficThreshold,
       "ruckusZDSystemLoadBalanceTrafficDifference": ruckusZDSystemLoadBalanceTrafficDifference,
       "ruckusZDSystemLoadBalanceType": ruckusZDSystemLoadBalanceType,
       "ruckusZDSystemStats": ruckusZDSystemStats,
       "ruckusZDSystemStatsNumAP": ruckusZDSystemStatsNumAP,
       "ruckusZDSystemStatsNumSta": ruckusZDSystemStatsNumSta,
       "ruckusZDSystemStatsNumRogue": ruckusZDSystemStatsNumRogue,
       "ruckusZDSystemStatsNumRogueKnown": ruckusZDSystemStatsNumRogueKnown,
       "ruckusZDSystemStatsWLANTotalRxPkts": ruckusZDSystemStatsWLANTotalRxPkts,
       "ruckusZDSystemStatsWLANTotalRxBytes": ruckusZDSystemStatsWLANTotalRxBytes,
       "ruckusZDSystemStatsWLANTotalRxMulticast": ruckusZDSystemStatsWLANTotalRxMulticast,
       "ruckusZDSystemStatsWLANTotalTxPkts": ruckusZDSystemStatsWLANTotalTxPkts,
       "ruckusZDSystemStatsWLANTotalTxBytes": ruckusZDSystemStatsWLANTotalTxBytes,
       "ruckusZDSystemStatsWLANTotalTxMulticast": ruckusZDSystemStatsWLANTotalTxMulticast,
       "ruckusZDSystemStatsWLANTotalTxFail": ruckusZDSystemStatsWLANTotalTxFail,
       "ruckusZDSystemStatsWLANTotalTxRetry": ruckusZDSystemStatsWLANTotalTxRetry,
       "ruckusZDSystemStatsCPUUtil": ruckusZDSystemStatsCPUUtil,
       "ruckusZDSystemStatsMemoryUtil": ruckusZDSystemStatsMemoryUtil,
       "ruckusZDSystemStatsNumRegisteredAP": ruckusZDSystemStatsNumRegisteredAP,
       "ruckusZDSystemStatsWLANTotalAssocFail": ruckusZDSystemStatsWLANTotalAssocFail,
       "ruckusZDSystemStatsWLANTotalRxErrFrm": ruckusZDSystemStatsWLANTotalRxErrFrm,
       "ruckusZDSystemStatsWLANTotalTxDroppedPkt": ruckusZDSystemStatsWLANTotalTxDroppedPkt,
       "ruckusZDSystemStatsWLANTotalTxErrFrm": ruckusZDSystemStatsWLANTotalTxErrFrm,
       "ruckusZDSystemStatsWLANTotalTxDroppedFrm": ruckusZDSystemStatsWLANTotalTxDroppedFrm,
       "ruckusZDSystemStatsLanTxRate": ruckusZDSystemStatsLanTxRate,
       "ruckusZDSystemStatsLanRxRate": ruckusZDSystemStatsLanRxRate,
       "ruckusZDSystemStatsAllNumSta": ruckusZDSystemStatsAllNumSta,
       "ruckusZDEthInfo": ruckusZDEthInfo,
       "ruckusZDEthNum": ruckusZDEthNum,
       "ruckusZDEthTable": ruckusZDEthTable,
       "ruckusZDEthEntry": ruckusZDEthEntry,
       "ruckusZDEthIfIndex": ruckusZDEthIfIndex,
       "ruckusZDEthName": ruckusZDEthName,
       "ruckusZDEthDesc": ruckusZDEthDesc,
       "ruckusZDEthType": ruckusZDEthType,
       "ruckusZDEthStatus": ruckusZDEthStatus,
       "ruckusZDEthPhysAddr": ruckusZDEthPhysAddr,
       "ruckusZDEthMtu": ruckusZDEthMtu,
       "ruckusZDEthIfSpeed": ruckusZDEthIfSpeed,
       "ruckusZDEthUtil": ruckusZDEthUtil,
       "ruckusZDEthTxBcastPkts": ruckusZDEthTxBcastPkts,
       "ruckusZDEthTxMcastPkts": ruckusZDEthTxMcastPkts,
       "ruckusZDEthRxBcastPkts": ruckusZDEthRxBcastPkts,
       "ruckusZDEthRxMcastPkts": ruckusZDEthRxMcastPkts,
       "ruckusZDEthTxUniPkts": ruckusZDEthTxUniPkts,
       "ruckusZDEthRxUniPkts": ruckusZDEthRxUniPkts,
       "ruckusZDEthTxPkts": ruckusZDEthTxPkts,
       "ruckusZDEthRxPkts": ruckusZDEthRxPkts,
       "ruckusZDEthDropTxPkts": ruckusZDEthDropTxPkts,
       "ruckusZDEthDropRxPkts": ruckusZDEthDropRxPkts,
       "ruckusZDEthTxBytes": ruckusZDEthTxBytes,
       "ruckusZDEthRxBytes": ruckusZDEthRxBytes}
)
