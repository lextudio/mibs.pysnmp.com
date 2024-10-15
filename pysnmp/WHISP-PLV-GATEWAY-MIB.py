# SNMP MIB module (WHISP-PLV-GATEWAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WHISP-PLV-GATEWAY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:53 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")

(whispPlvGateway,) = mibBuilder.importSymbols(
    "WHISP-GLOBAL-REG-MIB",
    "whispPlvGateway")

(WhispLUID,
 WhispMACAddress) = mibBuilder.importSymbols(
    "WHISP-TC-MIB",
    "WhispLUID",
    "WhispMACAddress")


# MODULE-IDENTITY

whispPlvGatewayMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1)
)
whispPlvGatewayMIB.setRevisions(
        ("2006-07-28 10:30",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WhispPlvGatewayObjects_ObjectIdentity = ObjectIdentity
whispPlvGatewayObjects = _WhispPlvGatewayObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1)
)
_WhispPlvGwInfo_ObjectIdentity = ObjectIdentity
whispPlvGwInfo = _WhispPlvGwInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 1)
)


class _GwInfoModel_Type(DisplayString):
    """Custom type gwInfoModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GwInfoModel_Type.__name__ = "DisplayString"
_GwInfoModel_Object = MibScalar
gwInfoModel = _GwInfoModel_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 1, 1),
    _GwInfoModel_Type()
)
gwInfoModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwInfoModel.setStatus("current")


class _GwInfoSerialNumber_Type(DisplayString):
    """Custom type gwInfoSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GwInfoSerialNumber_Type.__name__ = "DisplayString"
_GwInfoSerialNumber_Object = MibScalar
gwInfoSerialNumber = _GwInfoSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 1, 2),
    _GwInfoSerialNumber_Type()
)
gwInfoSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwInfoSerialNumber.setStatus("current")
_GwInfoLanMac_Type = MacAddress
_GwInfoLanMac_Object = MibScalar
gwInfoLanMac = _GwInfoLanMac_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 1, 3),
    _GwInfoLanMac_Type()
)
gwInfoLanMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwInfoLanMac.setStatus("current")
_GwInfoWanMac_Type = MacAddress
_GwInfoWanMac_Object = MibScalar
gwInfoWanMac = _GwInfoWanMac_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 1, 4),
    _GwInfoWanMac_Type()
)
gwInfoWanMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwInfoWanMac.setStatus("current")
_GwInfoPlcMac_Type = MacAddress
_GwInfoPlcMac_Object = MibScalar
gwInfoPlcMac = _GwInfoPlcMac_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 1, 5),
    _GwInfoPlcMac_Type()
)
gwInfoPlcMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwInfoPlcMac.setStatus("current")


class _GwInfoHardwareVer_Type(DisplayString):
    """Custom type gwInfoHardwareVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GwInfoHardwareVer_Type.__name__ = "DisplayString"
_GwInfoHardwareVer_Object = MibScalar
gwInfoHardwareVer = _GwInfoHardwareVer_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 1, 6),
    _GwInfoHardwareVer_Type()
)
gwInfoHardwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwInfoHardwareVer.setStatus("current")


class _GwInfoDevFirmwareVer_Type(DisplayString):
    """Custom type gwInfoDevFirmwareVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GwInfoDevFirmwareVer_Type.__name__ = "DisplayString"
_GwInfoDevFirmwareVer_Object = MibScalar
gwInfoDevFirmwareVer = _GwInfoDevFirmwareVer_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 1, 7),
    _GwInfoDevFirmwareVer_Type()
)
gwInfoDevFirmwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwInfoDevFirmwareVer.setStatus("current")


class _GwInfoLoaderVer_Type(DisplayString):
    """Custom type gwInfoLoaderVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GwInfoLoaderVer_Type.__name__ = "DisplayString"
_GwInfoLoaderVer_Object = MibScalar
gwInfoLoaderVer = _GwInfoLoaderVer_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 1, 8),
    _GwInfoLoaderVer_Type()
)
gwInfoLoaderVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwInfoLoaderVer.setStatus("current")


class _GwInfoSimFirmwareVer_Type(DisplayString):
    """Custom type gwInfoSimFirmwareVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GwInfoSimFirmwareVer_Type.__name__ = "DisplayString"
_GwInfoSimFirmwareVer_Object = MibScalar
gwInfoSimFirmwareVer = _GwInfoSimFirmwareVer_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 1, 9),
    _GwInfoSimFirmwareVer_Type()
)
gwInfoSimFirmwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwInfoSimFirmwareVer.setStatus("current")
_GwInfoModemCount_Type = Integer32
_GwInfoModemCount_Object = MibScalar
gwInfoModemCount = _GwInfoModemCount_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 1, 10),
    _GwInfoModemCount_Type()
)
gwInfoModemCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwInfoModemCount.setStatus("current")


class _GwInfoDeviceUpgradeStatus_Type(Integer32):
    """Custom type gwInfoDeviceUpgradeStatus based on Integer32"""
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
        *(("failed", 3),
          ("inProgress", 2),
          ("notStarted", 1),
          ("successful", 4))
    )


_GwInfoDeviceUpgradeStatus_Type.__name__ = "Integer32"
_GwInfoDeviceUpgradeStatus_Object = MibScalar
gwInfoDeviceUpgradeStatus = _GwInfoDeviceUpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 1, 11),
    _GwInfoDeviceUpgradeStatus_Type()
)
gwInfoDeviceUpgradeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwInfoDeviceUpgradeStatus.setStatus("current")


class _GwInfoSimUpgradeStatus_Type(Integer32):
    """Custom type gwInfoSimUpgradeStatus based on Integer32"""
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
        *(("failed", 3),
          ("inProgress", 2),
          ("notStarted", 1),
          ("successful", 4))
    )


_GwInfoSimUpgradeStatus_Type.__name__ = "Integer32"
_GwInfoSimUpgradeStatus_Object = MibScalar
gwInfoSimUpgradeStatus = _GwInfoSimUpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 1, 12),
    _GwInfoSimUpgradeStatus_Type()
)
gwInfoSimUpgradeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwInfoSimUpgradeStatus.setStatus("current")
_GwInfoTemperature_Type = Integer32
_GwInfoTemperature_Object = MibScalar
gwInfoTemperature = _GwInfoTemperature_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 1, 13),
    _GwInfoTemperature_Type()
)
gwInfoTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwInfoTemperature.setStatus("current")
if mibBuilder.loadTexts:
    gwInfoTemperature.setUnits("Degrees Centigrade.")
_WhispPlvGwConfig_ObjectIdentity = ObjectIdentity
whispPlvGwConfig = _WhispPlvGwConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 2)
)


class _GwConfNtpConfig_Type(Integer32):
    """Custom type gwConfNtpConfig based on Integer32"""
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


_GwConfNtpConfig_Type.__name__ = "Integer32"
_GwConfNtpConfig_Object = MibScalar
gwConfNtpConfig = _GwConfNtpConfig_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 2, 1),
    _GwConfNtpConfig_Type()
)
gwConfNtpConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwConfNtpConfig.setStatus("current")


class _GwConfNtpServer_Type(DisplayString):
    """Custom type gwConfNtpServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_GwConfNtpServer_Type.__name__ = "DisplayString"
_GwConfNtpServer_Object = MibScalar
gwConfNtpServer = _GwConfNtpServer_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 2, 2),
    _GwConfNtpServer_Type()
)
gwConfNtpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwConfNtpServer.setStatus("current")


class _GwConfTime_Type(DisplayString):
    """Custom type gwConfTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_GwConfTime_Type.__name__ = "DisplayString"
_GwConfTime_Object = MibScalar
gwConfTime = _GwConfTime_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 2, 3),
    _GwConfTime_Type()
)
gwConfTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwConfTime.setStatus("current")


class _GwConfDate_Type(DisplayString):
    """Custom type gwConfDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_GwConfDate_Type.__name__ = "DisplayString"
_GwConfDate_Object = MibScalar
gwConfDate = _GwConfDate_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 2, 4),
    _GwConfDate_Type()
)
gwConfDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwConfDate.setStatus("current")


class _GwConfModemTableTimeout_Type(Integer32):
    """Custom type gwConfModemTableTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 1440),
    )


_GwConfModemTableTimeout_Type.__name__ = "Integer32"
_GwConfModemTableTimeout_Object = MibScalar
gwConfModemTableTimeout = _GwConfModemTableTimeout_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 2, 5),
    _GwConfModemTableTimeout_Type()
)
gwConfModemTableTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwConfModemTableTimeout.setStatus("current")


class _GwConfAutoLogoutTime_Type(Integer32):
    """Custom type gwConfAutoLogoutTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3660),
    )


_GwConfAutoLogoutTime_Type.__name__ = "Integer32"
_GwConfAutoLogoutTime_Object = MibScalar
gwConfAutoLogoutTime = _GwConfAutoLogoutTime_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 2, 6),
    _GwConfAutoLogoutTime_Type()
)
gwConfAutoLogoutTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwConfAutoLogoutTime.setStatus("current")


class _GwConfPSD_Type(OctetString):
    """Custom type gwConfPSD based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(84, 84),
    )


_GwConfPSD_Type.__name__ = "OctetString"
_GwConfPSD_Object = MibScalar
gwConfPSD = _GwConfPSD_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 2, 7),
    _GwConfPSD_Type()
)
gwConfPSD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwConfPSD.setStatus("current")
_WhispPlvGwTrapConfig_ObjectIdentity = ObjectIdentity
whispPlvGwTrapConfig = _WhispPlvGwTrapConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 3)
)
_GwConfTrapIp1_Type = IpAddress
_GwConfTrapIp1_Object = MibScalar
gwConfTrapIp1 = _GwConfTrapIp1_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 3, 1),
    _GwConfTrapIp1_Type()
)
gwConfTrapIp1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwConfTrapIp1.setStatus("current")


class _GwConfTrapCommStr1_Type(DisplayString):
    """Custom type gwConfTrapCommStr1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GwConfTrapCommStr1_Type.__name__ = "DisplayString"
_GwConfTrapCommStr1_Object = MibScalar
gwConfTrapCommStr1 = _GwConfTrapCommStr1_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 3, 2),
    _GwConfTrapCommStr1_Type()
)
gwConfTrapCommStr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwConfTrapCommStr1.setStatus("current")
_GwConfTrapIp2_Type = IpAddress
_GwConfTrapIp2_Object = MibScalar
gwConfTrapIp2 = _GwConfTrapIp2_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 3, 3),
    _GwConfTrapIp2_Type()
)
gwConfTrapIp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwConfTrapIp2.setStatus("current")


class _GwConfTrapCommStr2_Type(DisplayString):
    """Custom type gwConfTrapCommStr2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GwConfTrapCommStr2_Type.__name__ = "DisplayString"
_GwConfTrapCommStr2_Object = MibScalar
gwConfTrapCommStr2 = _GwConfTrapCommStr2_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 3, 4),
    _GwConfTrapCommStr2_Type()
)
gwConfTrapCommStr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwConfTrapCommStr2.setStatus("current")
_GwConfTrapIp3_Type = IpAddress
_GwConfTrapIp3_Object = MibScalar
gwConfTrapIp3 = _GwConfTrapIp3_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 3, 5),
    _GwConfTrapIp3_Type()
)
gwConfTrapIp3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwConfTrapIp3.setStatus("current")


class _GwConfTrapCommStr3_Type(DisplayString):
    """Custom type gwConfTrapCommStr3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GwConfTrapCommStr3_Type.__name__ = "DisplayString"
_GwConfTrapCommStr3_Object = MibScalar
gwConfTrapCommStr3 = _GwConfTrapCommStr3_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 3, 6),
    _GwConfTrapCommStr3_Type()
)
gwConfTrapCommStr3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwConfTrapCommStr3.setStatus("current")
_GwConfTrapIp4_Type = IpAddress
_GwConfTrapIp4_Object = MibScalar
gwConfTrapIp4 = _GwConfTrapIp4_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 3, 7),
    _GwConfTrapIp4_Type()
)
gwConfTrapIp4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwConfTrapIp4.setStatus("current")


class _GwConfTrapCommStr4_Type(DisplayString):
    """Custom type gwConfTrapCommStr4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GwConfTrapCommStr4_Type.__name__ = "DisplayString"
_GwConfTrapCommStr4_Object = MibScalar
gwConfTrapCommStr4 = _GwConfTrapCommStr4_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 3, 8),
    _GwConfTrapCommStr4_Type()
)
gwConfTrapCommStr4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwConfTrapCommStr4.setStatus("current")
_GwConfTrapIp5_Type = IpAddress
_GwConfTrapIp5_Object = MibScalar
gwConfTrapIp5 = _GwConfTrapIp5_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 3, 9),
    _GwConfTrapIp5_Type()
)
gwConfTrapIp5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwConfTrapIp5.setStatus("current")


class _GwConfTrapCommStr5_Type(DisplayString):
    """Custom type gwConfTrapCommStr5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GwConfTrapCommStr5_Type.__name__ = "DisplayString"
_GwConfTrapCommStr5_Object = MibScalar
gwConfTrapCommStr5 = _GwConfTrapCommStr5_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 3, 10),
    _GwConfTrapCommStr5_Type()
)
gwConfTrapCommStr5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwConfTrapCommStr5.setStatus("current")
_GwConfTrapIp6_Type = IpAddress
_GwConfTrapIp6_Object = MibScalar
gwConfTrapIp6 = _GwConfTrapIp6_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 3, 11),
    _GwConfTrapIp6_Type()
)
gwConfTrapIp6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwConfTrapIp6.setStatus("current")


class _GwConfTrapCommStr6_Type(DisplayString):
    """Custom type gwConfTrapCommStr6 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GwConfTrapCommStr6_Type.__name__ = "DisplayString"
_GwConfTrapCommStr6_Object = MibScalar
gwConfTrapCommStr6 = _GwConfTrapCommStr6_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 3, 12),
    _GwConfTrapCommStr6_Type()
)
gwConfTrapCommStr6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwConfTrapCommStr6.setStatus("current")
_GwConfTrapIp7_Type = IpAddress
_GwConfTrapIp7_Object = MibScalar
gwConfTrapIp7 = _GwConfTrapIp7_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 3, 13),
    _GwConfTrapIp7_Type()
)
gwConfTrapIp7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwConfTrapIp7.setStatus("current")


class _GwConfTrapCommStr7_Type(DisplayString):
    """Custom type gwConfTrapCommStr7 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GwConfTrapCommStr7_Type.__name__ = "DisplayString"
_GwConfTrapCommStr7_Object = MibScalar
gwConfTrapCommStr7 = _GwConfTrapCommStr7_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 3, 14),
    _GwConfTrapCommStr7_Type()
)
gwConfTrapCommStr7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwConfTrapCommStr7.setStatus("current")
_GwConfTrapIp8_Type = IpAddress
_GwConfTrapIp8_Object = MibScalar
gwConfTrapIp8 = _GwConfTrapIp8_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 3, 15),
    _GwConfTrapIp8_Type()
)
gwConfTrapIp8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwConfTrapIp8.setStatus("current")


class _GwConfTrapCommStr8_Type(DisplayString):
    """Custom type gwConfTrapCommStr8 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GwConfTrapCommStr8_Type.__name__ = "DisplayString"
_GwConfTrapCommStr8_Object = MibScalar
gwConfTrapCommStr8 = _GwConfTrapCommStr8_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 3, 16),
    _GwConfTrapCommStr8_Type()
)
gwConfTrapCommStr8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwConfTrapCommStr8.setStatus("current")
_GwConfTrapIp9_Type = IpAddress
_GwConfTrapIp9_Object = MibScalar
gwConfTrapIp9 = _GwConfTrapIp9_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 3, 17),
    _GwConfTrapIp9_Type()
)
gwConfTrapIp9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwConfTrapIp9.setStatus("current")


class _GwConfTrapCommStr9_Type(DisplayString):
    """Custom type gwConfTrapCommStr9 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GwConfTrapCommStr9_Type.__name__ = "DisplayString"
_GwConfTrapCommStr9_Object = MibScalar
gwConfTrapCommStr9 = _GwConfTrapCommStr9_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 3, 18),
    _GwConfTrapCommStr9_Type()
)
gwConfTrapCommStr9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwConfTrapCommStr9.setStatus("current")
_GwConfTrapIp10_Type = IpAddress
_GwConfTrapIp10_Object = MibScalar
gwConfTrapIp10 = _GwConfTrapIp10_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 3, 19),
    _GwConfTrapIp10_Type()
)
gwConfTrapIp10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwConfTrapIp10.setStatus("current")


class _GwConfTrapCommStr10_Type(DisplayString):
    """Custom type gwConfTrapCommStr10 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GwConfTrapCommStr10_Type.__name__ = "DisplayString"
_GwConfTrapCommStr10_Object = MibScalar
gwConfTrapCommStr10 = _GwConfTrapCommStr10_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 3, 20),
    _GwConfTrapCommStr10_Type()
)
gwConfTrapCommStr10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwConfTrapCommStr10.setStatus("current")
_WhispPlvGwPwrLnStats_ObjectIdentity = ObjectIdentity
whispPlvGwPwrLnStats = _WhispPlvGwPwrLnStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 4)
)
_GwPwrLnMaxDelay_Type = Integer32
_GwPwrLnMaxDelay_Object = MibScalar
gwPwrLnMaxDelay = _GwPwrLnMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 4, 1),
    _GwPwrLnMaxDelay_Type()
)
gwPwrLnMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwPwrLnMaxDelay.setStatus("current")
_GwPwrLnTxAck_Type = Integer32
_GwPwrLnTxAck_Object = MibScalar
gwPwrLnTxAck = _GwPwrLnTxAck_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 4, 2),
    _GwPwrLnTxAck_Type()
)
gwPwrLnTxAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwPwrLnTxAck.setStatus("current")
_GwPwrLnTxNak_Type = Integer32
_GwPwrLnTxNak_Object = MibScalar
gwPwrLnTxNak = _GwPwrLnTxNak_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 4, 3),
    _GwPwrLnTxNak_Type()
)
gwPwrLnTxNak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwPwrLnTxNak.setStatus("current")
_GwPwrLnTxFail_Type = Integer32
_GwPwrLnTxFail_Object = MibScalar
gwPwrLnTxFail = _GwPwrLnTxFail_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 4, 4),
    _GwPwrLnTxFail_Type()
)
gwPwrLnTxFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwPwrLnTxFail.setStatus("current")
_GwPwrLnTxColl_Type = Integer32
_GwPwrLnTxColl_Object = MibScalar
gwPwrLnTxColl = _GwPwrLnTxColl_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 4, 5),
    _GwPwrLnTxColl_Type()
)
gwPwrLnTxColl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwPwrLnTxColl.setStatus("current")
_GwPwrLnTxCarrLoss_Type = Integer32
_GwPwrLnTxCarrLoss_Object = MibScalar
gwPwrLnTxCarrLoss = _GwPwrLnTxCarrLoss_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 4, 6),
    _GwPwrLnTxCarrLoss_Type()
)
gwPwrLnTxCarrLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwPwrLnTxCarrLoss.setStatus("current")
_GwPwrLnRoboByte40_Type = Integer32
_GwPwrLnRoboByte40_Object = MibScalar
gwPwrLnRoboByte40 = _GwPwrLnRoboByte40_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 4, 7),
    _GwPwrLnRoboByte40_Type()
)
gwPwrLnRoboByte40.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwPwrLnRoboByte40.setStatus("current")
_GwPwrLnRoboFails_Type = Integer32
_GwPwrLnRoboFails_Object = MibScalar
gwPwrLnRoboFails = _GwPwrLnRoboFails_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 4, 8),
    _GwPwrLnRoboFails_Type()
)
gwPwrLnRoboFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwPwrLnRoboFails.setStatus("current")
_GwPwrLnRoboDrops_Type = Integer32
_GwPwrLnRoboDrops_Object = MibScalar
gwPwrLnRoboDrops = _GwPwrLnRoboDrops_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 4, 9),
    _GwPwrLnRoboDrops_Type()
)
gwPwrLnRoboDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwPwrLnRoboDrops.setStatus("current")
_WhispPlvGwAdmConfig_ObjectIdentity = ObjectIdentity
whispPlvGwAdmConfig = _WhispPlvGwAdmConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 5)
)


class _GwAdmConfLoginUsername_Type(DisplayString):
    """Custom type gwAdmConfLoginUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 16),
    )


_GwAdmConfLoginUsername_Type.__name__ = "DisplayString"
_GwAdmConfLoginUsername_Object = MibScalar
gwAdmConfLoginUsername = _GwAdmConfLoginUsername_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 5, 1),
    _GwAdmConfLoginUsername_Type()
)
gwAdmConfLoginUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmConfLoginUsername.setStatus("current")


class _GwAdmConfLoginPassword_Type(DisplayString):
    """Custom type gwAdmConfLoginPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GwAdmConfLoginPassword_Type.__name__ = "DisplayString"
_GwAdmConfLoginPassword_Object = MibScalar
gwAdmConfLoginPassword = _GwAdmConfLoginPassword_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 5, 2),
    _GwAdmConfLoginPassword_Type()
)
gwAdmConfLoginPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmConfLoginPassword.setStatus("current")


class _GwAdmConfNEK_Type(DisplayString):
    """Custom type gwAdmConfNEK based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GwAdmConfNEK_Type.__name__ = "DisplayString"
_GwAdmConfNEK_Object = MibScalar
gwAdmConfNEK = _GwAdmConfNEK_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 5, 3),
    _GwAdmConfNEK_Type()
)
gwAdmConfNEK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmConfNEK.setStatus("current")
_GwAdmConfAuthServIp1_Type = IpAddress
_GwAdmConfAuthServIp1_Object = MibScalar
gwAdmConfAuthServIp1 = _GwAdmConfAuthServIp1_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 5, 4),
    _GwAdmConfAuthServIp1_Type()
)
gwAdmConfAuthServIp1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmConfAuthServIp1.setStatus("current")
_GwAdmConfAuthServIp2_Type = IpAddress
_GwAdmConfAuthServIp2_Object = MibScalar
gwAdmConfAuthServIp2 = _GwAdmConfAuthServIp2_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 5, 5),
    _GwAdmConfAuthServIp2_Type()
)
gwAdmConfAuthServIp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmConfAuthServIp2.setStatus("current")
_GwAdmConfAuthServIp3_Type = IpAddress
_GwAdmConfAuthServIp3_Object = MibScalar
gwAdmConfAuthServIp3 = _GwAdmConfAuthServIp3_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 5, 6),
    _GwAdmConfAuthServIp3_Type()
)
gwAdmConfAuthServIp3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmConfAuthServIp3.setStatus("current")


class _GwAdmConfAuthMode_Type(Integer32):
    """Custom type gwAdmConfAuthMode based on Integer32"""
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


_GwAdmConfAuthMode_Type.__name__ = "Integer32"
_GwAdmConfAuthMode_Object = MibScalar
gwAdmConfAuthMode = _GwAdmConfAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 5, 7),
    _GwAdmConfAuthMode_Type()
)
gwAdmConfAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmConfAuthMode.setStatus("current")


class _GwAdmConfAuthKey_Type(DisplayString):
    """Custom type gwAdmConfAuthKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_GwAdmConfAuthKey_Type.__name__ = "DisplayString"
_GwAdmConfAuthKey_Object = MibScalar
gwAdmConfAuthKey = _GwAdmConfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 5, 8),
    _GwAdmConfAuthKey_Type()
)
gwAdmConfAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmConfAuthKey.setStatus("current")


class _GwAdmConfAuthKeyOption_Type(Integer32):
    """Custom type gwAdmConfAuthKeyOption based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("useDefaultKey", 1),
          ("useKeySet", 2))
    )


_GwAdmConfAuthKeyOption_Type.__name__ = "Integer32"
_GwAdmConfAuthKeyOption_Object = MibScalar
gwAdmConfAuthKeyOption = _GwAdmConfAuthKeyOption_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 5, 9),
    _GwAdmConfAuthKeyOption_Type()
)
gwAdmConfAuthKeyOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmConfAuthKeyOption.setStatus("current")


class _GwAdmConfSnmpGetCommStr_Type(DisplayString):
    """Custom type gwAdmConfSnmpGetCommStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GwAdmConfSnmpGetCommStr_Type.__name__ = "DisplayString"
_GwAdmConfSnmpGetCommStr_Object = MibScalar
gwAdmConfSnmpGetCommStr = _GwAdmConfSnmpGetCommStr_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 5, 10),
    _GwAdmConfSnmpGetCommStr_Type()
)
gwAdmConfSnmpGetCommStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmConfSnmpGetCommStr.setStatus("current")


class _GwAdmConfSnmpSetCommStr_Type(DisplayString):
    """Custom type gwAdmConfSnmpSetCommStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GwAdmConfSnmpSetCommStr_Type.__name__ = "DisplayString"
_GwAdmConfSnmpSetCommStr_Object = MibScalar
gwAdmConfSnmpSetCommStr = _GwAdmConfSnmpSetCommStr_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 5, 11),
    _GwAdmConfSnmpSetCommStr_Type()
)
gwAdmConfSnmpSetCommStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmConfSnmpSetCommStr.setStatus("current")


class _GwAdmConfSnmpAdminCommStr_Type(DisplayString):
    """Custom type gwAdmConfSnmpAdminCommStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GwAdmConfSnmpAdminCommStr_Type.__name__ = "DisplayString"
_GwAdmConfSnmpAdminCommStr_Object = MibScalar
gwAdmConfSnmpAdminCommStr = _GwAdmConfSnmpAdminCommStr_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 5, 12),
    _GwAdmConfSnmpAdminCommStr_Type()
)
gwAdmConfSnmpAdminCommStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmConfSnmpAdminCommStr.setStatus("current")
_GwAdmConfFtpServerIp_Type = IpAddress
_GwAdmConfFtpServerIp_Object = MibScalar
gwAdmConfFtpServerIp = _GwAdmConfFtpServerIp_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 5, 13),
    _GwAdmConfFtpServerIp_Type()
)
gwAdmConfFtpServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmConfFtpServerIp.setStatus("current")


class _GwAdmConfFtpUsername_Type(DisplayString):
    """Custom type gwAdmConfFtpUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GwAdmConfFtpUsername_Type.__name__ = "DisplayString"
_GwAdmConfFtpUsername_Object = MibScalar
gwAdmConfFtpUsername = _GwAdmConfFtpUsername_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 5, 14),
    _GwAdmConfFtpUsername_Type()
)
gwAdmConfFtpUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmConfFtpUsername.setStatus("current")


class _GwAdmConfFtpPassword_Type(DisplayString):
    """Custom type gwAdmConfFtpPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GwAdmConfFtpPassword_Type.__name__ = "DisplayString"
_GwAdmConfFtpPassword_Object = MibScalar
gwAdmConfFtpPassword = _GwAdmConfFtpPassword_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 5, 15),
    _GwAdmConfFtpPassword_Type()
)
gwAdmConfFtpPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmConfFtpPassword.setStatus("current")


class _GwAdmConfFtpFile_Type(DisplayString):
    """Custom type gwAdmConfFtpFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GwAdmConfFtpFile_Type.__name__ = "DisplayString"
_GwAdmConfFtpFile_Object = MibScalar
gwAdmConfFtpFile = _GwAdmConfFtpFile_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 5, 16),
    _GwAdmConfFtpFile_Type()
)
gwAdmConfFtpFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmConfFtpFile.setStatus("current")


class _GwAdmConfDeviceUpgradeStart_Type(Integer32):
    """Custom type gwAdmConfDeviceUpgradeStart based on Integer32"""
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
          ("upgrade", 1))
    )


_GwAdmConfDeviceUpgradeStart_Type.__name__ = "Integer32"
_GwAdmConfDeviceUpgradeStart_Object = MibScalar
gwAdmConfDeviceUpgradeStart = _GwAdmConfDeviceUpgradeStart_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 5, 17),
    _GwAdmConfDeviceUpgradeStart_Type()
)
gwAdmConfDeviceUpgradeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmConfDeviceUpgradeStart.setStatus("current")


class _GwAdmConfSimUpgradeStart_Type(Integer32):
    """Custom type gwAdmConfSimUpgradeStart based on Integer32"""
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
          ("upgrade", 1))
    )


_GwAdmConfSimUpgradeStart_Type.__name__ = "Integer32"
_GwAdmConfSimUpgradeStart_Object = MibScalar
gwAdmConfSimUpgradeStart = _GwAdmConfSimUpgradeStart_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 5, 18),
    _GwAdmConfSimUpgradeStart_Type()
)
gwAdmConfSimUpgradeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmConfSimUpgradeStart.setStatus("current")


class _GwAdmConfSystemReboot_Type(Integer32):
    """Custom type gwAdmConfSystemReboot based on Integer32"""
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
          ("reboot", 1))
    )


_GwAdmConfSystemReboot_Type.__name__ = "Integer32"
_GwAdmConfSystemReboot_Object = MibScalar
gwAdmConfSystemReboot = _GwAdmConfSystemReboot_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 5, 19),
    _GwAdmConfSystemReboot_Type()
)
gwAdmConfSystemReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmConfSystemReboot.setStatus("current")


class _GwAdmConfReset_Type(Integer32):
    """Custom type gwAdmConfReset based on Integer32"""
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
          ("reset", 1))
    )


_GwAdmConfReset_Type.__name__ = "Integer32"
_GwAdmConfReset_Object = MibScalar
gwAdmConfReset = _GwAdmConfReset_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 5, 20),
    _GwAdmConfReset_Type()
)
gwAdmConfReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmConfReset.setStatus("current")


class _GwAdmConfDeviceMode_Type(Integer32):
    """Custom type gwAdmConfDeviceMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nat", 2),
          ("switch", 1))
    )


_GwAdmConfDeviceMode_Type.__name__ = "Integer32"
_GwAdmConfDeviceMode_Object = MibScalar
gwAdmConfDeviceMode = _GwAdmConfDeviceMode_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 5, 21),
    _GwAdmConfDeviceMode_Type()
)
gwAdmConfDeviceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmConfDeviceMode.setStatus("current")


class _GwAdmConfLUIDStart_Type(Integer32):
    """Custom type gwAdmConfLUIDStart based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2047),
    )


_GwAdmConfLUIDStart_Type.__name__ = "Integer32"
_GwAdmConfLUIDStart_Object = MibScalar
gwAdmConfLUIDStart = _GwAdmConfLUIDStart_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 5, 22),
    _GwAdmConfLUIDStart_Type()
)
gwAdmConfLUIDStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmConfLUIDStart.setStatus("current")


class _GwAdmConfLUIDEnd_Type(Integer32):
    """Custom type gwAdmConfLUIDEnd based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2047),
    )


_GwAdmConfLUIDEnd_Type.__name__ = "Integer32"
_GwAdmConfLUIDEnd_Object = MibScalar
gwAdmConfLUIDEnd = _GwAdmConfLUIDEnd_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 5, 23),
    _GwAdmConfLUIDEnd_Type()
)
gwAdmConfLUIDEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmConfLUIDEnd.setStatus("current")


class _GwAdmConfVLANPassthroughStatus_Type(Integer32):
    """Custom type gwAdmConfVLANPassthroughStatus based on Integer32"""
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


_GwAdmConfVLANPassthroughStatus_Type.__name__ = "Integer32"
_GwAdmConfVLANPassthroughStatus_Object = MibScalar
gwAdmConfVLANPassthroughStatus = _GwAdmConfVLANPassthroughStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 5, 24),
    _GwAdmConfVLANPassthroughStatus_Type()
)
gwAdmConfVLANPassthroughStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmConfVLANPassthroughStatus.setStatus("current")


class _GwAdmConfManagementVLANId_Type(Integer32):
    """Custom type gwAdmConfManagementVLANId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_GwAdmConfManagementVLANId_Type.__name__ = "Integer32"
_GwAdmConfManagementVLANId_Object = MibScalar
gwAdmConfManagementVLANId = _GwAdmConfManagementVLANId_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 5, 25),
    _GwAdmConfManagementVLANId_Type()
)
gwAdmConfManagementVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmConfManagementVLANId.setStatus("current")
_WhispPlvGwAdmLanConfig_ObjectIdentity = ObjectIdentity
whispPlvGwAdmLanConfig = _WhispPlvGwAdmLanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 6)
)


class _GwAdmConfLanConfig_Type(Integer32):
    """Custom type gwAdmConfLanConfig based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_GwAdmConfLanConfig_Type.__name__ = "Integer32"
_GwAdmConfLanConfig_Object = MibScalar
gwAdmConfLanConfig = _GwAdmConfLanConfig_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 6, 1),
    _GwAdmConfLanConfig_Type()
)
gwAdmConfLanConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmConfLanConfig.setStatus("current")
_GwAdmConfLanIp_Type = IpAddress
_GwAdmConfLanIp_Object = MibScalar
gwAdmConfLanIp = _GwAdmConfLanIp_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 6, 2),
    _GwAdmConfLanIp_Type()
)
gwAdmConfLanIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmConfLanIp.setStatus("current")
_GwAdmConfLanSubnetMask_Type = IpAddress
_GwAdmConfLanSubnetMask_Object = MibScalar
gwAdmConfLanSubnetMask = _GwAdmConfLanSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 6, 3),
    _GwAdmConfLanSubnetMask_Type()
)
gwAdmConfLanSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmConfLanSubnetMask.setStatus("current")
_GwAdmConfLanGatewayIp_Type = IpAddress
_GwAdmConfLanGatewayIp_Object = MibScalar
gwAdmConfLanGatewayIp = _GwAdmConfLanGatewayIp_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 6, 4),
    _GwAdmConfLanGatewayIp_Type()
)
gwAdmConfLanGatewayIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmConfLanGatewayIp.setStatus("current")
_WhispPlvGwAdmSnmpAcessConfig_ObjectIdentity = ObjectIdentity
whispPlvGwAdmSnmpAcessConfig = _WhispPlvGwAdmSnmpAcessConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 7)
)
_GwAdmSnmpAccessIpNetwork1_Type = IpAddress
_GwAdmSnmpAccessIpNetwork1_Object = MibScalar
gwAdmSnmpAccessIpNetwork1 = _GwAdmSnmpAccessIpNetwork1_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 7, 1),
    _GwAdmSnmpAccessIpNetwork1_Type()
)
gwAdmSnmpAccessIpNetwork1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmSnmpAccessIpNetwork1.setStatus("current")
_GwAdmSnmpAccessIpNetworkMask1_Type = IpAddress
_GwAdmSnmpAccessIpNetworkMask1_Object = MibScalar
gwAdmSnmpAccessIpNetworkMask1 = _GwAdmSnmpAccessIpNetworkMask1_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 7, 2),
    _GwAdmSnmpAccessIpNetworkMask1_Type()
)
gwAdmSnmpAccessIpNetworkMask1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmSnmpAccessIpNetworkMask1.setStatus("current")
_GwAdmSnmpAccessIpNetwork2_Type = IpAddress
_GwAdmSnmpAccessIpNetwork2_Object = MibScalar
gwAdmSnmpAccessIpNetwork2 = _GwAdmSnmpAccessIpNetwork2_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 7, 3),
    _GwAdmSnmpAccessIpNetwork2_Type()
)
gwAdmSnmpAccessIpNetwork2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmSnmpAccessIpNetwork2.setStatus("current")
_GwAdmSnmpAccessIpNetworkMask2_Type = IpAddress
_GwAdmSnmpAccessIpNetworkMask2_Object = MibScalar
gwAdmSnmpAccessIpNetworkMask2 = _GwAdmSnmpAccessIpNetworkMask2_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 7, 4),
    _GwAdmSnmpAccessIpNetworkMask2_Type()
)
gwAdmSnmpAccessIpNetworkMask2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmSnmpAccessIpNetworkMask2.setStatus("current")
_GwAdmSnmpAccessIpNetwork3_Type = IpAddress
_GwAdmSnmpAccessIpNetwork3_Object = MibScalar
gwAdmSnmpAccessIpNetwork3 = _GwAdmSnmpAccessIpNetwork3_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 7, 5),
    _GwAdmSnmpAccessIpNetwork3_Type()
)
gwAdmSnmpAccessIpNetwork3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmSnmpAccessIpNetwork3.setStatus("current")
_GwAdmSnmpAccessIpNetworkMask3_Type = IpAddress
_GwAdmSnmpAccessIpNetworkMask3_Object = MibScalar
gwAdmSnmpAccessIpNetworkMask3 = _GwAdmSnmpAccessIpNetworkMask3_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 7, 6),
    _GwAdmSnmpAccessIpNetworkMask3_Type()
)
gwAdmSnmpAccessIpNetworkMask3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmSnmpAccessIpNetworkMask3.setStatus("current")
_GwAdmSnmpAccessIpNetwork4_Type = IpAddress
_GwAdmSnmpAccessIpNetwork4_Object = MibScalar
gwAdmSnmpAccessIpNetwork4 = _GwAdmSnmpAccessIpNetwork4_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 7, 7),
    _GwAdmSnmpAccessIpNetwork4_Type()
)
gwAdmSnmpAccessIpNetwork4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmSnmpAccessIpNetwork4.setStatus("current")
_GwAdmSnmpAccessIpNetworkMask4_Type = IpAddress
_GwAdmSnmpAccessIpNetworkMask4_Object = MibScalar
gwAdmSnmpAccessIpNetworkMask4 = _GwAdmSnmpAccessIpNetworkMask4_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 7, 8),
    _GwAdmSnmpAccessIpNetworkMask4_Type()
)
gwAdmSnmpAccessIpNetworkMask4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmSnmpAccessIpNetworkMask4.setStatus("current")
_GwAdmSnmpAccessIpNetwork5_Type = IpAddress
_GwAdmSnmpAccessIpNetwork5_Object = MibScalar
gwAdmSnmpAccessIpNetwork5 = _GwAdmSnmpAccessIpNetwork5_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 7, 9),
    _GwAdmSnmpAccessIpNetwork5_Type()
)
gwAdmSnmpAccessIpNetwork5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmSnmpAccessIpNetwork5.setStatus("current")
_GwAdmSnmpAccessIpNetworkMask5_Type = IpAddress
_GwAdmSnmpAccessIpNetworkMask5_Object = MibScalar
gwAdmSnmpAccessIpNetworkMask5 = _GwAdmSnmpAccessIpNetworkMask5_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 7, 10),
    _GwAdmSnmpAccessIpNetworkMask5_Type()
)
gwAdmSnmpAccessIpNetworkMask5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmSnmpAccessIpNetworkMask5.setStatus("current")
_GwAdmSnmpAccessIpNetwork6_Type = IpAddress
_GwAdmSnmpAccessIpNetwork6_Object = MibScalar
gwAdmSnmpAccessIpNetwork6 = _GwAdmSnmpAccessIpNetwork6_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 7, 11),
    _GwAdmSnmpAccessIpNetwork6_Type()
)
gwAdmSnmpAccessIpNetwork6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmSnmpAccessIpNetwork6.setStatus("current")
_GwAdmSnmpAccessIpNetworkMask6_Type = IpAddress
_GwAdmSnmpAccessIpNetworkMask6_Object = MibScalar
gwAdmSnmpAccessIpNetworkMask6 = _GwAdmSnmpAccessIpNetworkMask6_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 7, 12),
    _GwAdmSnmpAccessIpNetworkMask6_Type()
)
gwAdmSnmpAccessIpNetworkMask6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmSnmpAccessIpNetworkMask6.setStatus("current")
_GwAdmSnmpAccessIpNetwork7_Type = IpAddress
_GwAdmSnmpAccessIpNetwork7_Object = MibScalar
gwAdmSnmpAccessIpNetwork7 = _GwAdmSnmpAccessIpNetwork7_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 7, 13),
    _GwAdmSnmpAccessIpNetwork7_Type()
)
gwAdmSnmpAccessIpNetwork7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmSnmpAccessIpNetwork7.setStatus("current")
_GwAdmSnmpAccessIpNetworkMask7_Type = IpAddress
_GwAdmSnmpAccessIpNetworkMask7_Object = MibScalar
gwAdmSnmpAccessIpNetworkMask7 = _GwAdmSnmpAccessIpNetworkMask7_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 7, 14),
    _GwAdmSnmpAccessIpNetworkMask7_Type()
)
gwAdmSnmpAccessIpNetworkMask7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmSnmpAccessIpNetworkMask7.setStatus("current")
_GwAdmSnmpAccessIpNetwork8_Type = IpAddress
_GwAdmSnmpAccessIpNetwork8_Object = MibScalar
gwAdmSnmpAccessIpNetwork8 = _GwAdmSnmpAccessIpNetwork8_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 7, 15),
    _GwAdmSnmpAccessIpNetwork8_Type()
)
gwAdmSnmpAccessIpNetwork8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmSnmpAccessIpNetwork8.setStatus("current")
_GwAdmSnmpAccessIpNetworkMask8_Type = IpAddress
_GwAdmSnmpAccessIpNetworkMask8_Object = MibScalar
gwAdmSnmpAccessIpNetworkMask8 = _GwAdmSnmpAccessIpNetworkMask8_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 7, 16),
    _GwAdmSnmpAccessIpNetworkMask8_Type()
)
gwAdmSnmpAccessIpNetworkMask8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmSnmpAccessIpNetworkMask8.setStatus("current")
_GwAdmSnmpAccessIpNetwork9_Type = IpAddress
_GwAdmSnmpAccessIpNetwork9_Object = MibScalar
gwAdmSnmpAccessIpNetwork9 = _GwAdmSnmpAccessIpNetwork9_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 7, 17),
    _GwAdmSnmpAccessIpNetwork9_Type()
)
gwAdmSnmpAccessIpNetwork9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmSnmpAccessIpNetwork9.setStatus("current")
_GwAdmSnmpAccessIpNetworkMask9_Type = IpAddress
_GwAdmSnmpAccessIpNetworkMask9_Object = MibScalar
gwAdmSnmpAccessIpNetworkMask9 = _GwAdmSnmpAccessIpNetworkMask9_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 7, 18),
    _GwAdmSnmpAccessIpNetworkMask9_Type()
)
gwAdmSnmpAccessIpNetworkMask9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmSnmpAccessIpNetworkMask9.setStatus("current")
_GwAdmSnmpAccessIpNetwork10_Type = IpAddress
_GwAdmSnmpAccessIpNetwork10_Object = MibScalar
gwAdmSnmpAccessIpNetwork10 = _GwAdmSnmpAccessIpNetwork10_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 7, 19),
    _GwAdmSnmpAccessIpNetwork10_Type()
)
gwAdmSnmpAccessIpNetwork10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmSnmpAccessIpNetwork10.setStatus("current")
_GwAdmSnmpAccessIpNetworkMask10_Type = IpAddress
_GwAdmSnmpAccessIpNetworkMask10_Object = MibScalar
gwAdmSnmpAccessIpNetworkMask10 = _GwAdmSnmpAccessIpNetworkMask10_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 7, 20),
    _GwAdmSnmpAccessIpNetworkMask10_Type()
)
gwAdmSnmpAccessIpNetworkMask10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmSnmpAccessIpNetworkMask10.setStatus("current")
_WhispPlvGwAdmWanConfig_ObjectIdentity = ObjectIdentity
whispPlvGwAdmWanConfig = _WhispPlvGwAdmWanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 8)
)


class _GwAdmWConfWanConfig_Type(Integer32):
    """Custom type gwAdmWConfWanConfig based on Integer32"""
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
        *(("dynamicIp", 1),
          ("pppoe", 3),
          ("pptp", 4),
          ("staticIp", 2))
    )


_GwAdmWConfWanConfig_Type.__name__ = "Integer32"
_GwAdmWConfWanConfig_Object = MibScalar
gwAdmWConfWanConfig = _GwAdmWConfWanConfig_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 8, 1),
    _GwAdmWConfWanConfig_Type()
)
gwAdmWConfWanConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmWConfWanConfig.setStatus("current")
_GwAdmWConfWanIp_Type = IpAddress
_GwAdmWConfWanIp_Object = MibScalar
gwAdmWConfWanIp = _GwAdmWConfWanIp_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 8, 2),
    _GwAdmWConfWanIp_Type()
)
gwAdmWConfWanIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmWConfWanIp.setStatus("current")
_GwAdmWConfSubnetMask_Type = IpAddress
_GwAdmWConfSubnetMask_Object = MibScalar
gwAdmWConfSubnetMask = _GwAdmWConfSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 8, 3),
    _GwAdmWConfSubnetMask_Type()
)
gwAdmWConfSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmWConfSubnetMask.setStatus("current")
_GwAdmWConfGateway_Type = IpAddress
_GwAdmWConfGateway_Object = MibScalar
gwAdmWConfGateway = _GwAdmWConfGateway_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 8, 4),
    _GwAdmWConfGateway_Type()
)
gwAdmWConfGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmWConfGateway.setStatus("current")
_GwAdmWConfDNS1_Type = IpAddress
_GwAdmWConfDNS1_Object = MibScalar
gwAdmWConfDNS1 = _GwAdmWConfDNS1_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 8, 5),
    _GwAdmWConfDNS1_Type()
)
gwAdmWConfDNS1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmWConfDNS1.setStatus("current")
_GwAdmWConfDNS2_Type = IpAddress
_GwAdmWConfDNS2_Object = MibScalar
gwAdmWConfDNS2 = _GwAdmWConfDNS2_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 8, 6),
    _GwAdmWConfDNS2_Type()
)
gwAdmWConfDNS2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmWConfDNS2.setStatus("current")


class _GwAdmWConfPppoeUsername_Type(DisplayString):
    """Custom type gwAdmWConfPppoeUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GwAdmWConfPppoeUsername_Type.__name__ = "DisplayString"
_GwAdmWConfPppoeUsername_Object = MibScalar
gwAdmWConfPppoeUsername = _GwAdmWConfPppoeUsername_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 8, 7),
    _GwAdmWConfPppoeUsername_Type()
)
gwAdmWConfPppoeUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmWConfPppoeUsername.setStatus("current")


class _GwAdmWConfPppoePassword_Type(DisplayString):
    """Custom type gwAdmWConfPppoePassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GwAdmWConfPppoePassword_Type.__name__ = "DisplayString"
_GwAdmWConfPppoePassword_Object = MibScalar
gwAdmWConfPppoePassword = _GwAdmWConfPppoePassword_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 8, 8),
    _GwAdmWConfPppoePassword_Type()
)
gwAdmWConfPppoePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmWConfPppoePassword.setStatus("current")


class _GwAdmWConfDhcpConfig_Type(Integer32):
    """Custom type gwAdmWConfDhcpConfig based on Integer32"""
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


_GwAdmWConfDhcpConfig_Type.__name__ = "Integer32"
_GwAdmWConfDhcpConfig_Object = MibScalar
gwAdmWConfDhcpConfig = _GwAdmWConfDhcpConfig_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 8, 9),
    _GwAdmWConfDhcpConfig_Type()
)
gwAdmWConfDhcpConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmWConfDhcpConfig.setStatus("current")
_GwAdmWConfDhcpStartIp_Type = IpAddress
_GwAdmWConfDhcpStartIp_Object = MibScalar
gwAdmWConfDhcpStartIp = _GwAdmWConfDhcpStartIp_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 8, 10),
    _GwAdmWConfDhcpStartIp_Type()
)
gwAdmWConfDhcpStartIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmWConfDhcpStartIp.setStatus("current")
_GwAdmWConfDhcpEndIp_Type = IpAddress
_GwAdmWConfDhcpEndIp_Object = MibScalar
gwAdmWConfDhcpEndIp = _GwAdmWConfDhcpEndIp_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 8, 11),
    _GwAdmWConfDhcpEndIp_Type()
)
gwAdmWConfDhcpEndIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmWConfDhcpEndIp.setStatus("current")


class _GwAdmWConfDhcpLeaseTime_Type(Integer32):
    """Custom type gwAdmWConfDhcpLeaseTime based on Integer32"""
    defaultValue = 5

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
        *(("oneDay", 5),
          ("oneHour", 2),
          ("oneWeek", 7),
          ("thirtyMins", 1),
          ("twelveHours", 4),
          ("twoDays", 6),
          ("twoHours", 3),
          ("twoWeeks", 8))
    )


_GwAdmWConfDhcpLeaseTime_Type.__name__ = "Integer32"
_GwAdmWConfDhcpLeaseTime_Object = MibScalar
gwAdmWConfDhcpLeaseTime = _GwAdmWConfDhcpLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 8, 12),
    _GwAdmWConfDhcpLeaseTime_Type()
)
gwAdmWConfDhcpLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmWConfDhcpLeaseTime.setStatus("current")


class _GwAdmWConfUpnpConfig_Type(Integer32):
    """Custom type gwAdmWConfUpnpConfig based on Integer32"""
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


_GwAdmWConfUpnpConfig_Type.__name__ = "Integer32"
_GwAdmWConfUpnpConfig_Object = MibScalar
gwAdmWConfUpnpConfig = _GwAdmWConfUpnpConfig_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 8, 13),
    _GwAdmWConfUpnpConfig_Type()
)
gwAdmWConfUpnpConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmWConfUpnpConfig.setStatus("current")


class _GwAdmWConfFirewallConfig_Type(Integer32):
    """Custom type gwAdmWConfFirewallConfig based on Integer32"""
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


_GwAdmWConfFirewallConfig_Type.__name__ = "Integer32"
_GwAdmWConfFirewallConfig_Object = MibScalar
gwAdmWConfFirewallConfig = _GwAdmWConfFirewallConfig_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 8, 14),
    _GwAdmWConfFirewallConfig_Type()
)
gwAdmWConfFirewallConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwAdmWConfFirewallConfig.setStatus("current")
_WhispPlvGwModemTable_Object = MibTable
whispPlvGwModemTable = _WhispPlvGwModemTable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 9)
)
if mibBuilder.loadTexts:
    whispPlvGwModemTable.setStatus("current")
_WhispPlvGwModemEntry_Object = MibTableRow
whispPlvGwModemEntry = _WhispPlvGwModemEntry_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 9, 1)
)
whispPlvGwModemEntry.setIndexNames(
    (0, "WHISP-PLV-GATEWAY-MIB", "gwModemLUID"),
)
if mibBuilder.loadTexts:
    whispPlvGwModemEntry.setStatus("current")
_GwModemLUID_Type = WhispLUID
_GwModemLUID_Object = MibTableColumn
gwModemLUID = _GwModemLUID_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 9, 1, 1),
    _GwModemLUID_Type()
)
gwModemLUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwModemLUID.setStatus("current")


class _GwModemDescr_Type(DisplayString):
    """Custom type gwModemDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GwModemDescr_Type.__name__ = "DisplayString"
_GwModemDescr_Object = MibTableColumn
gwModemDescr = _GwModemDescr_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 9, 1, 2),
    _GwModemDescr_Type()
)
gwModemDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwModemDescr.setStatus("current")
_GwModemPhysAddress_Type = WhispMACAddress
_GwModemPhysAddress_Object = MibTableColumn
gwModemPhysAddress = _GwModemPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 9, 1, 3),
    _GwModemPhysAddress_Type()
)
gwModemPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwModemPhysAddress.setStatus("current")
_GwModemIP_Type = IpAddress
_GwModemIP_Object = MibTableColumn
gwModemIP = _GwModemIP_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 9, 1, 4),
    _GwModemIP_Type()
)
gwModemIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwModemIP.setStatus("current")


class _GwModemHardwareVersion_Type(DisplayString):
    """Custom type gwModemHardwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_GwModemHardwareVersion_Type.__name__ = "DisplayString"
_GwModemHardwareVersion_Object = MibTableColumn
gwModemHardwareVersion = _GwModemHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 9, 1, 5),
    _GwModemHardwareVersion_Type()
)
gwModemHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwModemHardwareVersion.setStatus("current")


class _GwModemSoftwareVersion_Type(DisplayString):
    """Custom type gwModemSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_GwModemSoftwareVersion_Type.__name__ = "DisplayString"
_GwModemSoftwareVersion_Object = MibTableColumn
gwModemSoftwareVersion = _GwModemSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 9, 1, 6),
    _GwModemSoftwareVersion_Type()
)
gwModemSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwModemSoftwareVersion.setStatus("current")


class _GwModemSoftwareBootVersion_Type(DisplayString):
    """Custom type gwModemSoftwareBootVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_GwModemSoftwareBootVersion_Type.__name__ = "DisplayString"
_GwModemSoftwareBootVersion_Object = MibTableColumn
gwModemSoftwareBootVersion = _GwModemSoftwareBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 9, 1, 7),
    _GwModemSoftwareBootVersion_Type()
)
gwModemSoftwareBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwModemSoftwareBootVersion.setStatus("current")


class _GwModemSessState_Type(Integer32):
    """Custom type gwModemSessState based on Integer32"""
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
        *(("authChal", 4),
          ("clearing", 2),
          ("idle", 0),
          ("inSession", 1),
          ("notInUse", 6),
          ("reRegDnRst", 3),
          ("registering", 5))
    )


_GwModemSessState_Type.__name__ = "Integer32"
_GwModemSessState_Object = MibTableColumn
gwModemSessState = _GwModemSessState_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 9, 1, 8),
    _GwModemSessState_Type()
)
gwModemSessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwModemSessState.setStatus("current")
_GwModemsessionCount_Type = Integer32
_GwModemsessionCount_Object = MibTableColumn
gwModemsessionCount = _GwModemsessionCount_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 9, 1, 9),
    _GwModemsessionCount_Type()
)
gwModemsessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwModemsessionCount.setStatus("current")
_GwModemMtu_Type = Integer32
_GwModemMtu_Object = MibTableColumn
gwModemMtu = _GwModemMtu_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 9, 1, 10),
    _GwModemMtu_Type()
)
gwModemMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwModemMtu.setStatus("current")
_GwModemSpeed_Type = Gauge32
_GwModemSpeed_Object = MibTableColumn
gwModemSpeed = _GwModemSpeed_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 9, 1, 11),
    _GwModemSpeed_Type()
)
gwModemSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwModemSpeed.setStatus("current")
_GwModemInOctets_Type = Counter32
_GwModemInOctets_Object = MibTableColumn
gwModemInOctets = _GwModemInOctets_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 9, 1, 12),
    _GwModemInOctets_Type()
)
gwModemInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwModemInOctets.setStatus("current")
_GwModemInUcastPkts_Type = Counter32
_GwModemInUcastPkts_Object = MibTableColumn
gwModemInUcastPkts = _GwModemInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 9, 1, 13),
    _GwModemInUcastPkts_Type()
)
gwModemInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwModemInUcastPkts.setStatus("current")
_GwModemInNUcastPkts_Type = Counter32
_GwModemInNUcastPkts_Object = MibTableColumn
gwModemInNUcastPkts = _GwModemInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 9, 1, 14),
    _GwModemInNUcastPkts_Type()
)
gwModemInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwModemInNUcastPkts.setStatus("current")
_GwModemInDiscards_Type = Counter32
_GwModemInDiscards_Object = MibTableColumn
gwModemInDiscards = _GwModemInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 9, 1, 15),
    _GwModemInDiscards_Type()
)
gwModemInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwModemInDiscards.setStatus("current")
_GwModemInError_Type = Counter32
_GwModemInError_Object = MibTableColumn
gwModemInError = _GwModemInError_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 9, 1, 16),
    _GwModemInError_Type()
)
gwModemInError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwModemInError.setStatus("current")
_GwModemInUnknownProtos_Type = Counter32
_GwModemInUnknownProtos_Object = MibTableColumn
gwModemInUnknownProtos = _GwModemInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 9, 1, 17),
    _GwModemInUnknownProtos_Type()
)
gwModemInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwModemInUnknownProtos.setStatus("current")
_GwModemOutOctets_Type = Counter32
_GwModemOutOctets_Object = MibTableColumn
gwModemOutOctets = _GwModemOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 9, 1, 18),
    _GwModemOutOctets_Type()
)
gwModemOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwModemOutOctets.setStatus("current")
_GwModemOutUcastPkts_Type = Counter32
_GwModemOutUcastPkts_Object = MibTableColumn
gwModemOutUcastPkts = _GwModemOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 9, 1, 19),
    _GwModemOutUcastPkts_Type()
)
gwModemOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwModemOutUcastPkts.setStatus("current")
_GwModemOutNUcastPkts_Type = Counter32
_GwModemOutNUcastPkts_Object = MibTableColumn
gwModemOutNUcastPkts = _GwModemOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 9, 1, 20),
    _GwModemOutNUcastPkts_Type()
)
gwModemOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwModemOutNUcastPkts.setStatus("current")
_GwModemOutDiscards_Type = Counter32
_GwModemOutDiscards_Object = MibTableColumn
gwModemOutDiscards = _GwModemOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 9, 1, 21),
    _GwModemOutDiscards_Type()
)
gwModemOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwModemOutDiscards.setStatus("current")
_GwModemOutError_Type = Counter32
_GwModemOutError_Object = MibTableColumn
gwModemOutError = _GwModemOutError_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 9, 1, 22),
    _GwModemOutError_Type()
)
gwModemOutError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwModemOutError.setStatus("current")
_GwModemOutQLen_Type = Gauge32
_GwModemOutQLen_Object = MibTableColumn
gwModemOutQLen = _GwModemOutQLen_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 9, 1, 23),
    _GwModemOutQLen_Type()
)
gwModemOutQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwModemOutQLen.setStatus("current")
_GwModemRoboByte40_Type = Integer32
_GwModemRoboByte40_Object = MibTableColumn
gwModemRoboByte40 = _GwModemRoboByte40_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 9, 1, 24),
    _GwModemRoboByte40_Type()
)
gwModemRoboByte40.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwModemRoboByte40.setStatus("current")
_GwModemRoboFails_Type = Integer32
_GwModemRoboFails_Object = MibTableColumn
gwModemRoboFails = _GwModemRoboFails_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 9, 1, 25),
    _GwModemRoboFails_Type()
)
gwModemRoboFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwModemRoboFails.setStatus("current")
_GwModemRoboDrops_Type = Integer32
_GwModemRoboDrops_Object = MibTableColumn
gwModemRoboDrops = _GwModemRoboDrops_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 9, 1, 26),
    _GwModemRoboDrops_Type()
)
gwModemRoboDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwModemRoboDrops.setStatus("current")


class _GwModemDeviceType_Type(Integer32):
    """Custom type gwModemDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("modem", 0),
          ("other", 2),
          ("repeater", 1))
    )


_GwModemDeviceType_Type.__name__ = "Integer32"
_GwModemDeviceType_Object = MibTableColumn
gwModemDeviceType = _GwModemDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 9, 1, 27),
    _GwModemDeviceType_Type()
)
gwModemDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwModemDeviceType.setStatus("current")


class _GwModemPSD_Type(OctetString):
    """Custom type gwModemPSD based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(84, 84),
    )


_GwModemPSD_Type.__name__ = "OctetString"
_GwModemPSD_Object = MibTableColumn
gwModemPSD = _GwModemPSD_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 1, 9, 1, 28),
    _GwModemPSD_Type()
)
gwModemPSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwModemPSD.setStatus("current")
_WhispPlvGatewayEvents_ObjectIdentity = ObjectIdentity
whispPlvGatewayEvents = _WhispPlvGatewayEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 2)
)
_GwTrapPrefix_ObjectIdentity = ObjectIdentity
gwTrapPrefix = _GwTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 2, 0)
)
_WhispPlvGatewayConformance_ObjectIdentity = ObjectIdentity
whispPlvGatewayConformance = _WhispPlvGatewayConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 3)
)
_WhispPlvGatewayGroups_ObjectIdentity = ObjectIdentity
whispPlvGatewayGroups = _WhispPlvGatewayGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 3, 1)
)
_WhispPlvGatewayCompliances_ObjectIdentity = ObjectIdentity
whispPlvGatewayCompliances = _WhispPlvGatewayCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 3, 2)
)

# Managed Objects groups

whispPlvGatewayInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 3, 1, 1)
)
whispPlvGatewayInfoGroup.setObjects(
      *(("WHISP-PLV-GATEWAY-MIB", "gwInfoModel"),
        ("WHISP-PLV-GATEWAY-MIB", "gwInfoSerialNumber"),
        ("WHISP-PLV-GATEWAY-MIB", "gwInfoLanMac"),
        ("WHISP-PLV-GATEWAY-MIB", "gwInfoWanMac"),
        ("WHISP-PLV-GATEWAY-MIB", "gwInfoPlcMac"),
        ("WHISP-PLV-GATEWAY-MIB", "gwInfoHardwareVer"),
        ("WHISP-PLV-GATEWAY-MIB", "gwInfoDevFirmwareVer"),
        ("WHISP-PLV-GATEWAY-MIB", "gwInfoLoaderVer"),
        ("WHISP-PLV-GATEWAY-MIB", "gwInfoSimFirmwareVer"),
        ("WHISP-PLV-GATEWAY-MIB", "gwInfoModemCount"),
        ("WHISP-PLV-GATEWAY-MIB", "gwInfoDeviceUpgradeStatus"),
        ("WHISP-PLV-GATEWAY-MIB", "gwInfoSimUpgradeStatus"),
        ("WHISP-PLV-GATEWAY-MIB", "gwInfoTemperature"))
)
if mibBuilder.loadTexts:
    whispPlvGatewayInfoGroup.setStatus("current")

whispPlvGatewayConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 3, 1, 2)
)
whispPlvGatewayConfigGroup.setObjects(
      *(("WHISP-PLV-GATEWAY-MIB", "gwConfNtpConfig"),
        ("WHISP-PLV-GATEWAY-MIB", "gwConfNtpServer"),
        ("WHISP-PLV-GATEWAY-MIB", "gwConfTime"),
        ("WHISP-PLV-GATEWAY-MIB", "gwConfDate"),
        ("WHISP-PLV-GATEWAY-MIB", "gwConfModemTableTimeout"),
        ("WHISP-PLV-GATEWAY-MIB", "gwConfAutoLogoutTime"),
        ("WHISP-PLV-GATEWAY-MIB", "gwConfPSD"))
)
if mibBuilder.loadTexts:
    whispPlvGatewayConfigGroup.setStatus("current")

whispPlvGatewayTrapConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 3, 1, 3)
)
whispPlvGatewayTrapConfigGroup.setObjects(
      *(("WHISP-PLV-GATEWAY-MIB", "gwConfTrapIp1"),
        ("WHISP-PLV-GATEWAY-MIB", "gwConfTrapCommStr1"),
        ("WHISP-PLV-GATEWAY-MIB", "gwConfTrapIp2"),
        ("WHISP-PLV-GATEWAY-MIB", "gwConfTrapCommStr2"),
        ("WHISP-PLV-GATEWAY-MIB", "gwConfTrapIp3"),
        ("WHISP-PLV-GATEWAY-MIB", "gwConfTrapCommStr3"),
        ("WHISP-PLV-GATEWAY-MIB", "gwConfTrapIp4"),
        ("WHISP-PLV-GATEWAY-MIB", "gwConfTrapCommStr4"),
        ("WHISP-PLV-GATEWAY-MIB", "gwConfTrapIp5"),
        ("WHISP-PLV-GATEWAY-MIB", "gwConfTrapCommStr5"),
        ("WHISP-PLV-GATEWAY-MIB", "gwConfTrapIp6"),
        ("WHISP-PLV-GATEWAY-MIB", "gwConfTrapCommStr6"),
        ("WHISP-PLV-GATEWAY-MIB", "gwConfTrapIp7"),
        ("WHISP-PLV-GATEWAY-MIB", "gwConfTrapCommStr7"),
        ("WHISP-PLV-GATEWAY-MIB", "gwConfTrapIp8"),
        ("WHISP-PLV-GATEWAY-MIB", "gwConfTrapCommStr8"),
        ("WHISP-PLV-GATEWAY-MIB", "gwConfTrapIp9"),
        ("WHISP-PLV-GATEWAY-MIB", "gwConfTrapCommStr9"),
        ("WHISP-PLV-GATEWAY-MIB", "gwConfTrapIp10"),
        ("WHISP-PLV-GATEWAY-MIB", "gwConfTrapCommStr10"))
)
if mibBuilder.loadTexts:
    whispPlvGatewayTrapConfigGroup.setStatus("current")

whispPlvGatewayPowerlineGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 3, 1, 4)
)
whispPlvGatewayPowerlineGroup.setObjects(
      *(("WHISP-PLV-GATEWAY-MIB", "gwPwrLnMaxDelay"),
        ("WHISP-PLV-GATEWAY-MIB", "gwPwrLnTxAck"),
        ("WHISP-PLV-GATEWAY-MIB", "gwPwrLnTxNak"),
        ("WHISP-PLV-GATEWAY-MIB", "gwPwrLnTxFail"),
        ("WHISP-PLV-GATEWAY-MIB", "gwPwrLnTxColl"),
        ("WHISP-PLV-GATEWAY-MIB", "gwPwrLnTxCarrLoss"),
        ("WHISP-PLV-GATEWAY-MIB", "gwPwrLnRoboByte40"),
        ("WHISP-PLV-GATEWAY-MIB", "gwPwrLnRoboFails"),
        ("WHISP-PLV-GATEWAY-MIB", "gwPwrLnRoboDrops"))
)
if mibBuilder.loadTexts:
    whispPlvGatewayPowerlineGroup.setStatus("current")

whispPlvGatewayAdmConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 3, 1, 5)
)
whispPlvGatewayAdmConfigGroup.setObjects(
      *(("WHISP-PLV-GATEWAY-MIB", "gwAdmConfLoginUsername"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmConfLoginPassword"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmConfNEK"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmConfAuthServIp1"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmConfAuthServIp2"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmConfAuthServIp3"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmConfAuthMode"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmConfAuthKey"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmConfAuthKeyOption"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmConfSnmpGetCommStr"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmConfSnmpSetCommStr"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmConfSnmpAdminCommStr"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmConfFtpServerIp"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmConfFtpUsername"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmConfFtpPassword"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmConfFtpFile"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmConfDeviceUpgradeStart"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmConfSimUpgradeStart"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmConfSystemReboot"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmConfReset"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmConfDeviceMode"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmConfLUIDStart"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmConfLUIDEnd"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmConfVLANPassthroughStatus"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmConfManagementVLANId"))
)
if mibBuilder.loadTexts:
    whispPlvGatewayAdmConfigGroup.setStatus("current")

whispPlvGatewayAdmLanConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 3, 1, 6)
)
whispPlvGatewayAdmLanConfigGroup.setObjects(
      *(("WHISP-PLV-GATEWAY-MIB", "gwAdmConfLanConfig"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmConfLanIp"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmConfLanSubnetMask"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmConfLanGatewayIp"))
)
if mibBuilder.loadTexts:
    whispPlvGatewayAdmLanConfigGroup.setStatus("current")

whispPlvGatewayAdmSnmpAccessConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 3, 1, 7)
)
whispPlvGatewayAdmSnmpAccessConfigGroup.setObjects(
      *(("WHISP-PLV-GATEWAY-MIB", "gwAdmSnmpAccessIpNetwork1"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmSnmpAccessIpNetworkMask1"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmSnmpAccessIpNetwork2"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmSnmpAccessIpNetworkMask2"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmSnmpAccessIpNetwork3"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmSnmpAccessIpNetworkMask3"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmSnmpAccessIpNetwork4"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmSnmpAccessIpNetworkMask4"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmSnmpAccessIpNetwork5"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmSnmpAccessIpNetworkMask5"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmSnmpAccessIpNetwork6"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmSnmpAccessIpNetworkMask6"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmSnmpAccessIpNetwork7"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmSnmpAccessIpNetworkMask7"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmSnmpAccessIpNetwork8"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmSnmpAccessIpNetworkMask8"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmSnmpAccessIpNetwork9"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmSnmpAccessIpNetworkMask9"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmSnmpAccessIpNetwork10"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmSnmpAccessIpNetworkMask10"))
)
if mibBuilder.loadTexts:
    whispPlvGatewayAdmSnmpAccessConfigGroup.setStatus("current")

whispPlvGatewayAdmWanConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 3, 1, 8)
)
whispPlvGatewayAdmWanConfigGroup.setObjects(
      *(("WHISP-PLV-GATEWAY-MIB", "gwAdmWConfWanConfig"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmWConfWanIp"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmWConfSubnetMask"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmWConfGateway"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmWConfDNS1"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmWConfDNS2"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmWConfPppoeUsername"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmWConfPppoePassword"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmWConfDhcpConfig"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmWConfDhcpStartIp"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmWConfDhcpEndIp"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmWConfDhcpLeaseTime"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmWConfUpnpConfig"),
        ("WHISP-PLV-GATEWAY-MIB", "gwAdmWConfFirewallConfig"))
)
if mibBuilder.loadTexts:
    whispPlvGatewayAdmWanConfigGroup.setStatus("current")

whispPlvGatewayAdmModemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 3, 1, 9)
)
whispPlvGatewayAdmModemGroup.setObjects(
      *(("WHISP-PLV-GATEWAY-MIB", "gwModemLUID"),
        ("WHISP-PLV-GATEWAY-MIB", "gwModemDescr"),
        ("WHISP-PLV-GATEWAY-MIB", "gwModemPhysAddress"),
        ("WHISP-PLV-GATEWAY-MIB", "gwModemIP"),
        ("WHISP-PLV-GATEWAY-MIB", "gwModemHardwareVersion"),
        ("WHISP-PLV-GATEWAY-MIB", "gwModemSoftwareVersion"),
        ("WHISP-PLV-GATEWAY-MIB", "gwModemSoftwareBootVersion"),
        ("WHISP-PLV-GATEWAY-MIB", "gwModemSessState"),
        ("WHISP-PLV-GATEWAY-MIB", "gwModemsessionCount"),
        ("WHISP-PLV-GATEWAY-MIB", "gwModemMtu"),
        ("WHISP-PLV-GATEWAY-MIB", "gwModemSpeed"),
        ("WHISP-PLV-GATEWAY-MIB", "gwModemInOctets"),
        ("WHISP-PLV-GATEWAY-MIB", "gwModemInUcastPkts"),
        ("WHISP-PLV-GATEWAY-MIB", "gwModemInNUcastPkts"),
        ("WHISP-PLV-GATEWAY-MIB", "gwModemInDiscards"),
        ("WHISP-PLV-GATEWAY-MIB", "gwModemInError"),
        ("WHISP-PLV-GATEWAY-MIB", "gwModemInUnknownProtos"),
        ("WHISP-PLV-GATEWAY-MIB", "gwModemOutOctets"),
        ("WHISP-PLV-GATEWAY-MIB", "gwModemOutUcastPkts"),
        ("WHISP-PLV-GATEWAY-MIB", "gwModemOutNUcastPkts"),
        ("WHISP-PLV-GATEWAY-MIB", "gwModemOutDiscards"),
        ("WHISP-PLV-GATEWAY-MIB", "gwModemOutError"),
        ("WHISP-PLV-GATEWAY-MIB", "gwModemOutQLen"),
        ("WHISP-PLV-GATEWAY-MIB", "gwModemRoboByte40"),
        ("WHISP-PLV-GATEWAY-MIB", "gwModemRoboFails"),
        ("WHISP-PLV-GATEWAY-MIB", "gwModemRoboDrops"),
        ("WHISP-PLV-GATEWAY-MIB", "gwModemDeviceType"),
        ("WHISP-PLV-GATEWAY-MIB", "gwModemPSD"))
)
if mibBuilder.loadTexts:
    whispPlvGatewayAdmModemGroup.setStatus("current")


# Notification objects

gwTrapRegComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 2, 0, 1)
)
gwTrapRegComplete.setObjects(
      *(("WHISP-PLV-GATEWAY-MIB", "gwModemLUID"),
        ("WHISP-PLV-GATEWAY-MIB", "gwModemPhysAddress"))
)
if mibBuilder.loadTexts:
    gwTrapRegComplete.setStatus(
        "current"
    )

gwTrapRegLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 2, 0, 2)
)
gwTrapRegLost.setObjects(
      *(("WHISP-PLV-GATEWAY-MIB", "gwModemLUID"),
        ("WHISP-PLV-GATEWAY-MIB", "gwModemPhysAddress"))
)
if mibBuilder.loadTexts:
    gwTrapRegLost.setStatus(
        "current"
    )

gwTrapDeviceUpgradeStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 2, 0, 3)
)
gwTrapDeviceUpgradeStarted.setObjects(
      *(("WHISP-PLV-GATEWAY-MIB", "gwInfoDeviceUpgradeStatus"),
        ("WHISP-PLV-GATEWAY-MIB", "gwInfoDevFirmwareVer"))
)
if mibBuilder.loadTexts:
    gwTrapDeviceUpgradeStarted.setStatus(
        "current"
    )

gwTrapDeviceUpgradeCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 2, 0, 4)
)
gwTrapDeviceUpgradeCompleted.setObjects(
      *(("WHISP-PLV-GATEWAY-MIB", "gwInfoDeviceUpgradeStatus"),
        ("WHISP-PLV-GATEWAY-MIB", "gwInfoDevFirmwareVer"))
)
if mibBuilder.loadTexts:
    gwTrapDeviceUpgradeCompleted.setStatus(
        "current"
    )

gwTrapSimUpgradeStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 2, 0, 5)
)
gwTrapSimUpgradeStarted.setObjects(
      *(("WHISP-PLV-GATEWAY-MIB", "gwInfoSimUpgradeStatus"),
        ("WHISP-PLV-GATEWAY-MIB", "gwInfoSimFirmwareVer"))
)
if mibBuilder.loadTexts:
    gwTrapSimUpgradeStarted.setStatus(
        "current"
    )

gwTrapSimUpgradeCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 2, 0, 6)
)
gwTrapSimUpgradeCompleted.setObjects(
      *(("WHISP-PLV-GATEWAY-MIB", "gwInfoSimUpgradeStatus"),
        ("WHISP-PLV-GATEWAY-MIB", "gwInfoSimFirmwareVer"))
)
if mibBuilder.loadTexts:
    gwTrapSimUpgradeCompleted.setStatus(
        "current"
    )


# Notifications groups

whispPlvGatewayNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 3, 1, 10)
)
whispPlvGatewayNotificationsGroup.setObjects(
      *(("WHISP-PLV-GATEWAY-MIB", "gwTrapRegComplete"),
        ("WHISP-PLV-GATEWAY-MIB", "gwTrapRegLost"),
        ("WHISP-PLV-GATEWAY-MIB", "gwTrapDeviceUpgradeStarted"),
        ("WHISP-PLV-GATEWAY-MIB", "gwTrapDeviceUpgradeCompleted"),
        ("WHISP-PLV-GATEWAY-MIB", "gwTrapSimUpgradeStarted"),
        ("WHISP-PLV-GATEWAY-MIB", "gwTrapSimUpgradeCompleted"))
)
if mibBuilder.loadTexts:
    whispPlvGatewayNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

whispPlvGatewayCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 8, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    whispPlvGatewayCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WHISP-PLV-GATEWAY-MIB",
    **{"whispPlvGatewayMIB": whispPlvGatewayMIB,
       "whispPlvGatewayObjects": whispPlvGatewayObjects,
       "whispPlvGwInfo": whispPlvGwInfo,
       "gwInfoModel": gwInfoModel,
       "gwInfoSerialNumber": gwInfoSerialNumber,
       "gwInfoLanMac": gwInfoLanMac,
       "gwInfoWanMac": gwInfoWanMac,
       "gwInfoPlcMac": gwInfoPlcMac,
       "gwInfoHardwareVer": gwInfoHardwareVer,
       "gwInfoDevFirmwareVer": gwInfoDevFirmwareVer,
       "gwInfoLoaderVer": gwInfoLoaderVer,
       "gwInfoSimFirmwareVer": gwInfoSimFirmwareVer,
       "gwInfoModemCount": gwInfoModemCount,
       "gwInfoDeviceUpgradeStatus": gwInfoDeviceUpgradeStatus,
       "gwInfoSimUpgradeStatus": gwInfoSimUpgradeStatus,
       "gwInfoTemperature": gwInfoTemperature,
       "whispPlvGwConfig": whispPlvGwConfig,
       "gwConfNtpConfig": gwConfNtpConfig,
       "gwConfNtpServer": gwConfNtpServer,
       "gwConfTime": gwConfTime,
       "gwConfDate": gwConfDate,
       "gwConfModemTableTimeout": gwConfModemTableTimeout,
       "gwConfAutoLogoutTime": gwConfAutoLogoutTime,
       "gwConfPSD": gwConfPSD,
       "whispPlvGwTrapConfig": whispPlvGwTrapConfig,
       "gwConfTrapIp1": gwConfTrapIp1,
       "gwConfTrapCommStr1": gwConfTrapCommStr1,
       "gwConfTrapIp2": gwConfTrapIp2,
       "gwConfTrapCommStr2": gwConfTrapCommStr2,
       "gwConfTrapIp3": gwConfTrapIp3,
       "gwConfTrapCommStr3": gwConfTrapCommStr3,
       "gwConfTrapIp4": gwConfTrapIp4,
       "gwConfTrapCommStr4": gwConfTrapCommStr4,
       "gwConfTrapIp5": gwConfTrapIp5,
       "gwConfTrapCommStr5": gwConfTrapCommStr5,
       "gwConfTrapIp6": gwConfTrapIp6,
       "gwConfTrapCommStr6": gwConfTrapCommStr6,
       "gwConfTrapIp7": gwConfTrapIp7,
       "gwConfTrapCommStr7": gwConfTrapCommStr7,
       "gwConfTrapIp8": gwConfTrapIp8,
       "gwConfTrapCommStr8": gwConfTrapCommStr8,
       "gwConfTrapIp9": gwConfTrapIp9,
       "gwConfTrapCommStr9": gwConfTrapCommStr9,
       "gwConfTrapIp10": gwConfTrapIp10,
       "gwConfTrapCommStr10": gwConfTrapCommStr10,
       "whispPlvGwPwrLnStats": whispPlvGwPwrLnStats,
       "gwPwrLnMaxDelay": gwPwrLnMaxDelay,
       "gwPwrLnTxAck": gwPwrLnTxAck,
       "gwPwrLnTxNak": gwPwrLnTxNak,
       "gwPwrLnTxFail": gwPwrLnTxFail,
       "gwPwrLnTxColl": gwPwrLnTxColl,
       "gwPwrLnTxCarrLoss": gwPwrLnTxCarrLoss,
       "gwPwrLnRoboByte40": gwPwrLnRoboByte40,
       "gwPwrLnRoboFails": gwPwrLnRoboFails,
       "gwPwrLnRoboDrops": gwPwrLnRoboDrops,
       "whispPlvGwAdmConfig": whispPlvGwAdmConfig,
       "gwAdmConfLoginUsername": gwAdmConfLoginUsername,
       "gwAdmConfLoginPassword": gwAdmConfLoginPassword,
       "gwAdmConfNEK": gwAdmConfNEK,
       "gwAdmConfAuthServIp1": gwAdmConfAuthServIp1,
       "gwAdmConfAuthServIp2": gwAdmConfAuthServIp2,
       "gwAdmConfAuthServIp3": gwAdmConfAuthServIp3,
       "gwAdmConfAuthMode": gwAdmConfAuthMode,
       "gwAdmConfAuthKey": gwAdmConfAuthKey,
       "gwAdmConfAuthKeyOption": gwAdmConfAuthKeyOption,
       "gwAdmConfSnmpGetCommStr": gwAdmConfSnmpGetCommStr,
       "gwAdmConfSnmpSetCommStr": gwAdmConfSnmpSetCommStr,
       "gwAdmConfSnmpAdminCommStr": gwAdmConfSnmpAdminCommStr,
       "gwAdmConfFtpServerIp": gwAdmConfFtpServerIp,
       "gwAdmConfFtpUsername": gwAdmConfFtpUsername,
       "gwAdmConfFtpPassword": gwAdmConfFtpPassword,
       "gwAdmConfFtpFile": gwAdmConfFtpFile,
       "gwAdmConfDeviceUpgradeStart": gwAdmConfDeviceUpgradeStart,
       "gwAdmConfSimUpgradeStart": gwAdmConfSimUpgradeStart,
       "gwAdmConfSystemReboot": gwAdmConfSystemReboot,
       "gwAdmConfReset": gwAdmConfReset,
       "gwAdmConfDeviceMode": gwAdmConfDeviceMode,
       "gwAdmConfLUIDStart": gwAdmConfLUIDStart,
       "gwAdmConfLUIDEnd": gwAdmConfLUIDEnd,
       "gwAdmConfVLANPassthroughStatus": gwAdmConfVLANPassthroughStatus,
       "gwAdmConfManagementVLANId": gwAdmConfManagementVLANId,
       "whispPlvGwAdmLanConfig": whispPlvGwAdmLanConfig,
       "gwAdmConfLanConfig": gwAdmConfLanConfig,
       "gwAdmConfLanIp": gwAdmConfLanIp,
       "gwAdmConfLanSubnetMask": gwAdmConfLanSubnetMask,
       "gwAdmConfLanGatewayIp": gwAdmConfLanGatewayIp,
       "whispPlvGwAdmSnmpAcessConfig": whispPlvGwAdmSnmpAcessConfig,
       "gwAdmSnmpAccessIpNetwork1": gwAdmSnmpAccessIpNetwork1,
       "gwAdmSnmpAccessIpNetworkMask1": gwAdmSnmpAccessIpNetworkMask1,
       "gwAdmSnmpAccessIpNetwork2": gwAdmSnmpAccessIpNetwork2,
       "gwAdmSnmpAccessIpNetworkMask2": gwAdmSnmpAccessIpNetworkMask2,
       "gwAdmSnmpAccessIpNetwork3": gwAdmSnmpAccessIpNetwork3,
       "gwAdmSnmpAccessIpNetworkMask3": gwAdmSnmpAccessIpNetworkMask3,
       "gwAdmSnmpAccessIpNetwork4": gwAdmSnmpAccessIpNetwork4,
       "gwAdmSnmpAccessIpNetworkMask4": gwAdmSnmpAccessIpNetworkMask4,
       "gwAdmSnmpAccessIpNetwork5": gwAdmSnmpAccessIpNetwork5,
       "gwAdmSnmpAccessIpNetworkMask5": gwAdmSnmpAccessIpNetworkMask5,
       "gwAdmSnmpAccessIpNetwork6": gwAdmSnmpAccessIpNetwork6,
       "gwAdmSnmpAccessIpNetworkMask6": gwAdmSnmpAccessIpNetworkMask6,
       "gwAdmSnmpAccessIpNetwork7": gwAdmSnmpAccessIpNetwork7,
       "gwAdmSnmpAccessIpNetworkMask7": gwAdmSnmpAccessIpNetworkMask7,
       "gwAdmSnmpAccessIpNetwork8": gwAdmSnmpAccessIpNetwork8,
       "gwAdmSnmpAccessIpNetworkMask8": gwAdmSnmpAccessIpNetworkMask8,
       "gwAdmSnmpAccessIpNetwork9": gwAdmSnmpAccessIpNetwork9,
       "gwAdmSnmpAccessIpNetworkMask9": gwAdmSnmpAccessIpNetworkMask9,
       "gwAdmSnmpAccessIpNetwork10": gwAdmSnmpAccessIpNetwork10,
       "gwAdmSnmpAccessIpNetworkMask10": gwAdmSnmpAccessIpNetworkMask10,
       "whispPlvGwAdmWanConfig": whispPlvGwAdmWanConfig,
       "gwAdmWConfWanConfig": gwAdmWConfWanConfig,
       "gwAdmWConfWanIp": gwAdmWConfWanIp,
       "gwAdmWConfSubnetMask": gwAdmWConfSubnetMask,
       "gwAdmWConfGateway": gwAdmWConfGateway,
       "gwAdmWConfDNS1": gwAdmWConfDNS1,
       "gwAdmWConfDNS2": gwAdmWConfDNS2,
       "gwAdmWConfPppoeUsername": gwAdmWConfPppoeUsername,
       "gwAdmWConfPppoePassword": gwAdmWConfPppoePassword,
       "gwAdmWConfDhcpConfig": gwAdmWConfDhcpConfig,
       "gwAdmWConfDhcpStartIp": gwAdmWConfDhcpStartIp,
       "gwAdmWConfDhcpEndIp": gwAdmWConfDhcpEndIp,
       "gwAdmWConfDhcpLeaseTime": gwAdmWConfDhcpLeaseTime,
       "gwAdmWConfUpnpConfig": gwAdmWConfUpnpConfig,
       "gwAdmWConfFirewallConfig": gwAdmWConfFirewallConfig,
       "whispPlvGwModemTable": whispPlvGwModemTable,
       "whispPlvGwModemEntry": whispPlvGwModemEntry,
       "gwModemLUID": gwModemLUID,
       "gwModemDescr": gwModemDescr,
       "gwModemPhysAddress": gwModemPhysAddress,
       "gwModemIP": gwModemIP,
       "gwModemHardwareVersion": gwModemHardwareVersion,
       "gwModemSoftwareVersion": gwModemSoftwareVersion,
       "gwModemSoftwareBootVersion": gwModemSoftwareBootVersion,
       "gwModemSessState": gwModemSessState,
       "gwModemsessionCount": gwModemsessionCount,
       "gwModemMtu": gwModemMtu,
       "gwModemSpeed": gwModemSpeed,
       "gwModemInOctets": gwModemInOctets,
       "gwModemInUcastPkts": gwModemInUcastPkts,
       "gwModemInNUcastPkts": gwModemInNUcastPkts,
       "gwModemInDiscards": gwModemInDiscards,
       "gwModemInError": gwModemInError,
       "gwModemInUnknownProtos": gwModemInUnknownProtos,
       "gwModemOutOctets": gwModemOutOctets,
       "gwModemOutUcastPkts": gwModemOutUcastPkts,
       "gwModemOutNUcastPkts": gwModemOutNUcastPkts,
       "gwModemOutDiscards": gwModemOutDiscards,
       "gwModemOutError": gwModemOutError,
       "gwModemOutQLen": gwModemOutQLen,
       "gwModemRoboByte40": gwModemRoboByte40,
       "gwModemRoboFails": gwModemRoboFails,
       "gwModemRoboDrops": gwModemRoboDrops,
       "gwModemDeviceType": gwModemDeviceType,
       "gwModemPSD": gwModemPSD,
       "whispPlvGatewayEvents": whispPlvGatewayEvents,
       "gwTrapPrefix": gwTrapPrefix,
       "gwTrapRegComplete": gwTrapRegComplete,
       "gwTrapRegLost": gwTrapRegLost,
       "gwTrapDeviceUpgradeStarted": gwTrapDeviceUpgradeStarted,
       "gwTrapDeviceUpgradeCompleted": gwTrapDeviceUpgradeCompleted,
       "gwTrapSimUpgradeStarted": gwTrapSimUpgradeStarted,
       "gwTrapSimUpgradeCompleted": gwTrapSimUpgradeCompleted,
       "whispPlvGatewayConformance": whispPlvGatewayConformance,
       "whispPlvGatewayGroups": whispPlvGatewayGroups,
       "whispPlvGatewayInfoGroup": whispPlvGatewayInfoGroup,
       "whispPlvGatewayConfigGroup": whispPlvGatewayConfigGroup,
       "whispPlvGatewayTrapConfigGroup": whispPlvGatewayTrapConfigGroup,
       "whispPlvGatewayPowerlineGroup": whispPlvGatewayPowerlineGroup,
       "whispPlvGatewayAdmConfigGroup": whispPlvGatewayAdmConfigGroup,
       "whispPlvGatewayAdmLanConfigGroup": whispPlvGatewayAdmLanConfigGroup,
       "whispPlvGatewayAdmSnmpAccessConfigGroup": whispPlvGatewayAdmSnmpAccessConfigGroup,
       "whispPlvGatewayAdmWanConfigGroup": whispPlvGatewayAdmWanConfigGroup,
       "whispPlvGatewayAdmModemGroup": whispPlvGatewayAdmModemGroup,
       "whispPlvGatewayNotificationsGroup": whispPlvGatewayNotificationsGroup,
       "whispPlvGatewayCompliances": whispPlvGatewayCompliances,
       "whispPlvGatewayCompliance": whispPlvGatewayCompliance}
)
