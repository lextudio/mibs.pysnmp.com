# SNMP MIB module (WHISP-PLV-MODEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WHISP-PLV-MODEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:54 2024
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

(whispPlvModem,) = mibBuilder.importSymbols(
    "WHISP-GLOBAL-REG-MIB",
    "whispPlvModem")


# MODULE-IDENTITY

whispPlvModemMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1)
)
whispPlvModemMIB.setRevisions(
        ("2006-04-04 10:30",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WhispPlvModemObjects_ObjectIdentity = ObjectIdentity
whispPlvModemObjects = _WhispPlvModemObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1)
)
_WhispPlvModemInfo_ObjectIdentity = ObjectIdentity
whispPlvModemInfo = _WhispPlvModemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 1)
)


class _ModemInfoModel_Type(DisplayString):
    """Custom type modemInfoModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ModemInfoModel_Type.__name__ = "DisplayString"
_ModemInfoModel_Object = MibScalar
modemInfoModel = _ModemInfoModel_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 1, 1),
    _ModemInfoModel_Type()
)
modemInfoModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemInfoModel.setStatus("current")


class _ModemInfoSerialNumber_Type(DisplayString):
    """Custom type modemInfoSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ModemInfoSerialNumber_Type.__name__ = "DisplayString"
_ModemInfoSerialNumber_Object = MibScalar
modemInfoSerialNumber = _ModemInfoSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 1, 2),
    _ModemInfoSerialNumber_Type()
)
modemInfoSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemInfoSerialNumber.setStatus("current")
_ModemInfoDeviceMac_Type = MacAddress
_ModemInfoDeviceMac_Object = MibScalar
modemInfoDeviceMac = _ModemInfoDeviceMac_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 1, 3),
    _ModemInfoDeviceMac_Type()
)
modemInfoDeviceMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemInfoDeviceMac.setStatus("current")
_ModemInfoPlcMac_Type = MacAddress
_ModemInfoPlcMac_Object = MibScalar
modemInfoPlcMac = _ModemInfoPlcMac_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 1, 4),
    _ModemInfoPlcMac_Type()
)
modemInfoPlcMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemInfoPlcMac.setStatus("current")


class _ModemInfoHardwareVer_Type(DisplayString):
    """Custom type modemInfoHardwareVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ModemInfoHardwareVer_Type.__name__ = "DisplayString"
_ModemInfoHardwareVer_Object = MibScalar
modemInfoHardwareVer = _ModemInfoHardwareVer_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 1, 5),
    _ModemInfoHardwareVer_Type()
)
modemInfoHardwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemInfoHardwareVer.setStatus("current")


class _ModemInfoDeviceFirmwareVer_Type(DisplayString):
    """Custom type modemInfoDeviceFirmwareVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ModemInfoDeviceFirmwareVer_Type.__name__ = "DisplayString"
_ModemInfoDeviceFirmwareVer_Object = MibScalar
modemInfoDeviceFirmwareVer = _ModemInfoDeviceFirmwareVer_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 1, 6),
    _ModemInfoDeviceFirmwareVer_Type()
)
modemInfoDeviceFirmwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemInfoDeviceFirmwareVer.setStatus("current")


class _ModemInfoBootLoaderVer_Type(DisplayString):
    """Custom type modemInfoBootLoaderVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ModemInfoBootLoaderVer_Type.__name__ = "DisplayString"
_ModemInfoBootLoaderVer_Object = MibScalar
modemInfoBootLoaderVer = _ModemInfoBootLoaderVer_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 1, 7),
    _ModemInfoBootLoaderVer_Type()
)
modemInfoBootLoaderVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemInfoBootLoaderVer.setStatus("current")


class _ModemInfoSimFirmwareVer_Type(DisplayString):
    """Custom type modemInfoSimFirmwareVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ModemInfoSimFirmwareVer_Type.__name__ = "DisplayString"
_ModemInfoSimFirmwareVer_Object = MibScalar
modemInfoSimFirmwareVer = _ModemInfoSimFirmwareVer_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 1, 8),
    _ModemInfoSimFirmwareVer_Type()
)
modemInfoSimFirmwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemInfoSimFirmwareVer.setStatus("current")


class _ModemInfoDeviceUpgradeStatus_Type(Integer32):
    """Custom type modemInfoDeviceUpgradeStatus based on Integer32"""
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


_ModemInfoDeviceUpgradeStatus_Type.__name__ = "Integer32"
_ModemInfoDeviceUpgradeStatus_Object = MibScalar
modemInfoDeviceUpgradeStatus = _ModemInfoDeviceUpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 1, 9),
    _ModemInfoDeviceUpgradeStatus_Type()
)
modemInfoDeviceUpgradeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemInfoDeviceUpgradeStatus.setStatus("current")


class _ModemInfoSimUpgradeStatus_Type(Integer32):
    """Custom type modemInfoSimUpgradeStatus based on Integer32"""
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


_ModemInfoSimUpgradeStatus_Type.__name__ = "Integer32"
_ModemInfoSimUpgradeStatus_Object = MibScalar
modemInfoSimUpgradeStatus = _ModemInfoSimUpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 1, 10),
    _ModemInfoSimUpgradeStatus_Type()
)
modemInfoSimUpgradeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemInfoSimUpgradeStatus.setStatus("current")


class _ModemInfoCurrentMode_Type(Integer32):
    """Custom type modemInfoCurrentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bridge", 1),
          ("nat", 2))
    )


_ModemInfoCurrentMode_Type.__name__ = "Integer32"
_ModemInfoCurrentMode_Object = MibScalar
modemInfoCurrentMode = _ModemInfoCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 1, 11),
    _ModemInfoCurrentMode_Type()
)
modemInfoCurrentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemInfoCurrentMode.setStatus("current")


class _ModemInfoActiveBandwidthConfig_Type(Integer32):
    """Custom type modemInfoActiveBandwidthConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configured", 1),
          ("provisioned", 2))
    )


_ModemInfoActiveBandwidthConfig_Type.__name__ = "Integer32"
_ModemInfoActiveBandwidthConfig_Object = MibScalar
modemInfoActiveBandwidthConfig = _ModemInfoActiveBandwidthConfig_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 1, 12),
    _ModemInfoActiveBandwidthConfig_Type()
)
modemInfoActiveBandwidthConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemInfoActiveBandwidthConfig.setStatus("current")


class _ModemInfoActiveUpLinkBandwidth_Type(Integer32):
    """Custom type modemInfoActiveUpLinkBandwidth based on Integer32"""
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
        *(("fullSpeed", 1),
          ("u10Mbps", 8),
          ("u128Kbps", 3),
          ("u1Mbps", 6),
          ("u256Kbps", 4),
          ("u4Mbps", 7),
          ("u512Kbps", 5),
          ("u64Kbps", 2))
    )


_ModemInfoActiveUpLinkBandwidth_Type.__name__ = "Integer32"
_ModemInfoActiveUpLinkBandwidth_Object = MibScalar
modemInfoActiveUpLinkBandwidth = _ModemInfoActiveUpLinkBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 1, 13),
    _ModemInfoActiveUpLinkBandwidth_Type()
)
modemInfoActiveUpLinkBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemInfoActiveUpLinkBandwidth.setStatus("current")


class _ModemInfoActiveDownLinkBandwidth_Type(Integer32):
    """Custom type modemInfoActiveDownLinkBandwidth based on Integer32"""
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
        *(("d10Mbps", 8),
          ("d128Kbps", 3),
          ("d1Mbps", 6),
          ("d256Kbps", 4),
          ("d4Mbps", 7),
          ("d512Kbps", 5),
          ("d64Kbps", 2),
          ("fullSpeed", 1))
    )


_ModemInfoActiveDownLinkBandwidth_Type.__name__ = "Integer32"
_ModemInfoActiveDownLinkBandwidth_Object = MibScalar
modemInfoActiveDownLinkBandwidth = _ModemInfoActiveDownLinkBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 1, 14),
    _ModemInfoActiveDownLinkBandwidth_Type()
)
modemInfoActiveDownLinkBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemInfoActiveDownLinkBandwidth.setStatus("current")
_WhispPlvModemConfig_ObjectIdentity = ObjectIdentity
whispPlvModemConfig = _WhispPlvModemConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 2)
)


class _ModemConfPacketPriorityConfig_Type(Integer32):
    """Custom type modemConfPacketPriorityConfig based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixedQoS", 1),
          ("tos", 2))
    )


_ModemConfPacketPriorityConfig_Type.__name__ = "Integer32"
_ModemConfPacketPriorityConfig_Object = MibScalar
modemConfPacketPriorityConfig = _ModemConfPacketPriorityConfig_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 2, 1),
    _ModemConfPacketPriorityConfig_Type()
)
modemConfPacketPriorityConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemConfPacketPriorityConfig.setStatus("current")


class _ModemConfFixedQoSConfig_Type(Integer32):
    """Custom type modemConfFixedQoSConfig based on Integer32"""
    defaultValue = 1

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
        *(("background", 2),
          ("bestEffort", 3),
          ("controlLoad", 5),
          ("default", 1),
          ("excellentEffort", 4),
          ("networkControl", 8),
          ("videoOrAudio", 6),
          ("voice", 7))
    )


_ModemConfFixedQoSConfig_Type.__name__ = "Integer32"
_ModemConfFixedQoSConfig_Object = MibScalar
modemConfFixedQoSConfig = _ModemConfFixedQoSConfig_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 2, 2),
    _ModemConfFixedQoSConfig_Type()
)
modemConfFixedQoSConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemConfFixedQoSConfig.setStatus("current")


class _ModemConfUpLinkDataRate_Type(Integer32):
    """Custom type modemConfUpLinkDataRate based on Integer32"""
    defaultValue = 1

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
        *(("fullSpeed", 1),
          ("u10Mbps", 8),
          ("u128Kbps", 3),
          ("u1Mbps", 6),
          ("u256Kbps", 4),
          ("u4Mbps", 7),
          ("u512Kbps", 5),
          ("u64Kbps", 2))
    )


_ModemConfUpLinkDataRate_Type.__name__ = "Integer32"
_ModemConfUpLinkDataRate_Object = MibScalar
modemConfUpLinkDataRate = _ModemConfUpLinkDataRate_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 2, 3),
    _ModemConfUpLinkDataRate_Type()
)
modemConfUpLinkDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemConfUpLinkDataRate.setStatus("current")


class _ModemConfDownLinkDataRate_Type(Integer32):
    """Custom type modemConfDownLinkDataRate based on Integer32"""
    defaultValue = 1

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
        *(("d10Mbps", 8),
          ("d128Kbps", 3),
          ("d1Mbps", 6),
          ("d256Kbps", 4),
          ("d4Mbps", 7),
          ("d512Kbps", 5),
          ("d64Kbps", 2),
          ("fullSpeed", 1))
    )


_ModemConfDownLinkDataRate_Type.__name__ = "Integer32"
_ModemConfDownLinkDataRate_Object = MibScalar
modemConfDownLinkDataRate = _ModemConfDownLinkDataRate_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 2, 4),
    _ModemConfDownLinkDataRate_Type()
)
modemConfDownLinkDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemConfDownLinkDataRate.setStatus("current")


class _ModemConfPSD_Type(OctetString):
    """Custom type modemConfPSD based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(84, 84),
    )


_ModemConfPSD_Type.__name__ = "OctetString"
_ModemConfPSD_Object = MibScalar
modemConfPSD = _ModemConfPSD_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 2, 5),
    _ModemConfPSD_Type()
)
modemConfPSD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemConfPSD.setStatus("current")
_ModemConfUpLinkMir_Type = Integer32
_ModemConfUpLinkMir_Object = MibScalar
modemConfUpLinkMir = _ModemConfUpLinkMir_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 2, 6),
    _ModemConfUpLinkMir_Type()
)
modemConfUpLinkMir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemConfUpLinkMir.setStatus("current")
if mibBuilder.loadTexts:
    modemConfUpLinkMir.setUnits("Kilobits/sec")
_ModemConfDownLinkMir_Type = Integer32
_ModemConfDownLinkMir_Object = MibScalar
modemConfDownLinkMir = _ModemConfDownLinkMir_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 2, 7),
    _ModemConfDownLinkMir_Type()
)
modemConfDownLinkMir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemConfDownLinkMir.setStatus("current")
if mibBuilder.loadTexts:
    modemConfDownLinkMir.setUnits("Kilobits/sec")
_WhispPlvModemTrapConfig_ObjectIdentity = ObjectIdentity
whispPlvModemTrapConfig = _WhispPlvModemTrapConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 3)
)
_ModemConfTrapIp1_Type = IpAddress
_ModemConfTrapIp1_Object = MibScalar
modemConfTrapIp1 = _ModemConfTrapIp1_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 3, 1),
    _ModemConfTrapIp1_Type()
)
modemConfTrapIp1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemConfTrapIp1.setStatus("current")


class _ModemConfTrapCommStr1_Type(DisplayString):
    """Custom type modemConfTrapCommStr1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ModemConfTrapCommStr1_Type.__name__ = "DisplayString"
_ModemConfTrapCommStr1_Object = MibScalar
modemConfTrapCommStr1 = _ModemConfTrapCommStr1_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 3, 2),
    _ModemConfTrapCommStr1_Type()
)
modemConfTrapCommStr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemConfTrapCommStr1.setStatus("current")
_ModemConfTrapIp2_Type = IpAddress
_ModemConfTrapIp2_Object = MibScalar
modemConfTrapIp2 = _ModemConfTrapIp2_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 3, 3),
    _ModemConfTrapIp2_Type()
)
modemConfTrapIp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemConfTrapIp2.setStatus("current")


class _ModemConfTrapCommStr2_Type(DisplayString):
    """Custom type modemConfTrapCommStr2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ModemConfTrapCommStr2_Type.__name__ = "DisplayString"
_ModemConfTrapCommStr2_Object = MibScalar
modemConfTrapCommStr2 = _ModemConfTrapCommStr2_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 3, 4),
    _ModemConfTrapCommStr2_Type()
)
modemConfTrapCommStr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemConfTrapCommStr2.setStatus("current")
_ModemConfTrapIp3_Type = IpAddress
_ModemConfTrapIp3_Object = MibScalar
modemConfTrapIp3 = _ModemConfTrapIp3_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 3, 5),
    _ModemConfTrapIp3_Type()
)
modemConfTrapIp3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemConfTrapIp3.setStatus("current")


class _ModemConfTrapCommStr3_Type(DisplayString):
    """Custom type modemConfTrapCommStr3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ModemConfTrapCommStr3_Type.__name__ = "DisplayString"
_ModemConfTrapCommStr3_Object = MibScalar
modemConfTrapCommStr3 = _ModemConfTrapCommStr3_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 3, 6),
    _ModemConfTrapCommStr3_Type()
)
modemConfTrapCommStr3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemConfTrapCommStr3.setStatus("current")
_ModemConfTrapIp4_Type = IpAddress
_ModemConfTrapIp4_Object = MibScalar
modemConfTrapIp4 = _ModemConfTrapIp4_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 3, 7),
    _ModemConfTrapIp4_Type()
)
modemConfTrapIp4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemConfTrapIp4.setStatus("current")


class _ModemConfTrapCommStr4_Type(DisplayString):
    """Custom type modemConfTrapCommStr4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ModemConfTrapCommStr4_Type.__name__ = "DisplayString"
_ModemConfTrapCommStr4_Object = MibScalar
modemConfTrapCommStr4 = _ModemConfTrapCommStr4_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 3, 8),
    _ModemConfTrapCommStr4_Type()
)
modemConfTrapCommStr4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemConfTrapCommStr4.setStatus("current")
_ModemConfTrapIp5_Type = IpAddress
_ModemConfTrapIp5_Object = MibScalar
modemConfTrapIp5 = _ModemConfTrapIp5_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 3, 9),
    _ModemConfTrapIp5_Type()
)
modemConfTrapIp5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemConfTrapIp5.setStatus("current")


class _ModemConfTrapCommStr5_Type(DisplayString):
    """Custom type modemConfTrapCommStr5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ModemConfTrapCommStr5_Type.__name__ = "DisplayString"
_ModemConfTrapCommStr5_Object = MibScalar
modemConfTrapCommStr5 = _ModemConfTrapCommStr5_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 3, 10),
    _ModemConfTrapCommStr5_Type()
)
modemConfTrapCommStr5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemConfTrapCommStr5.setStatus("current")
_ModemConfTrapIp6_Type = IpAddress
_ModemConfTrapIp6_Object = MibScalar
modemConfTrapIp6 = _ModemConfTrapIp6_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 3, 11),
    _ModemConfTrapIp6_Type()
)
modemConfTrapIp6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemConfTrapIp6.setStatus("current")


class _ModemConfTrapCommStr6_Type(DisplayString):
    """Custom type modemConfTrapCommStr6 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ModemConfTrapCommStr6_Type.__name__ = "DisplayString"
_ModemConfTrapCommStr6_Object = MibScalar
modemConfTrapCommStr6 = _ModemConfTrapCommStr6_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 3, 12),
    _ModemConfTrapCommStr6_Type()
)
modemConfTrapCommStr6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemConfTrapCommStr6.setStatus("current")
_ModemConfTrapIp7_Type = IpAddress
_ModemConfTrapIp7_Object = MibScalar
modemConfTrapIp7 = _ModemConfTrapIp7_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 3, 13),
    _ModemConfTrapIp7_Type()
)
modemConfTrapIp7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemConfTrapIp7.setStatus("current")


class _ModemConfTrapCommStr7_Type(DisplayString):
    """Custom type modemConfTrapCommStr7 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ModemConfTrapCommStr7_Type.__name__ = "DisplayString"
_ModemConfTrapCommStr7_Object = MibScalar
modemConfTrapCommStr7 = _ModemConfTrapCommStr7_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 3, 14),
    _ModemConfTrapCommStr7_Type()
)
modemConfTrapCommStr7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemConfTrapCommStr7.setStatus("current")
_ModemConfTrapIp8_Type = IpAddress
_ModemConfTrapIp8_Object = MibScalar
modemConfTrapIp8 = _ModemConfTrapIp8_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 3, 15),
    _ModemConfTrapIp8_Type()
)
modemConfTrapIp8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemConfTrapIp8.setStatus("current")


class _ModemConfTrapCommStr8_Type(DisplayString):
    """Custom type modemConfTrapCommStr8 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ModemConfTrapCommStr8_Type.__name__ = "DisplayString"
_ModemConfTrapCommStr8_Object = MibScalar
modemConfTrapCommStr8 = _ModemConfTrapCommStr8_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 3, 16),
    _ModemConfTrapCommStr8_Type()
)
modemConfTrapCommStr8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemConfTrapCommStr8.setStatus("current")
_ModemConfTrapIp9_Type = IpAddress
_ModemConfTrapIp9_Object = MibScalar
modemConfTrapIp9 = _ModemConfTrapIp9_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 3, 17),
    _ModemConfTrapIp9_Type()
)
modemConfTrapIp9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemConfTrapIp9.setStatus("current")


class _ModemConfTrapCommStr9_Type(DisplayString):
    """Custom type modemConfTrapCommStr9 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ModemConfTrapCommStr9_Type.__name__ = "DisplayString"
_ModemConfTrapCommStr9_Object = MibScalar
modemConfTrapCommStr9 = _ModemConfTrapCommStr9_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 3, 18),
    _ModemConfTrapCommStr9_Type()
)
modemConfTrapCommStr9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemConfTrapCommStr9.setStatus("current")
_ModemConfTrapIp10_Type = IpAddress
_ModemConfTrapIp10_Object = MibScalar
modemConfTrapIp10 = _ModemConfTrapIp10_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 3, 19),
    _ModemConfTrapIp10_Type()
)
modemConfTrapIp10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemConfTrapIp10.setStatus("current")


class _ModemConfTrapCommStr10_Type(DisplayString):
    """Custom type modemConfTrapCommStr10 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ModemConfTrapCommStr10_Type.__name__ = "DisplayString"
_ModemConfTrapCommStr10_Object = MibScalar
modemConfTrapCommStr10 = _ModemConfTrapCommStr10_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 3, 20),
    _ModemConfTrapCommStr10_Type()
)
modemConfTrapCommStr10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemConfTrapCommStr10.setStatus("current")
_WhispPlvModemAdmConfig_ObjectIdentity = ObjectIdentity
whispPlvModemAdmConfig = _WhispPlvModemAdmConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 4)
)


class _ModemAdmConfIpConfig_Type(Integer32):
    """Custom type modemAdmConfIpConfig based on Integer32"""
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


_ModemAdmConfIpConfig_Type.__name__ = "Integer32"
_ModemAdmConfIpConfig_Object = MibScalar
modemAdmConfIpConfig = _ModemAdmConfIpConfig_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 4, 1),
    _ModemAdmConfIpConfig_Type()
)
modemAdmConfIpConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmConfIpConfig.setStatus("current")
_ModemAdmConfIp_Type = IpAddress
_ModemAdmConfIp_Object = MibScalar
modemAdmConfIp = _ModemAdmConfIp_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 4, 2),
    _ModemAdmConfIp_Type()
)
modemAdmConfIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmConfIp.setStatus("current")
_ModemAdmConfIpSubnetMask_Type = IpAddress
_ModemAdmConfIpSubnetMask_Object = MibScalar
modemAdmConfIpSubnetMask = _ModemAdmConfIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 4, 3),
    _ModemAdmConfIpSubnetMask_Type()
)
modemAdmConfIpSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmConfIpSubnetMask.setStatus("current")


class _ModemAdmConfNEK_Type(DisplayString):
    """Custom type modemAdmConfNEK based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 24),
    )


_ModemAdmConfNEK_Type.__name__ = "DisplayString"
_ModemAdmConfNEK_Object = MibScalar
modemAdmConfNEK = _ModemAdmConfNEK_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 4, 4),
    _ModemAdmConfNEK_Type()
)
modemAdmConfNEK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmConfNEK.setStatus("current")


class _ModemAdmConfSnmpGetCommStr_Type(DisplayString):
    """Custom type modemAdmConfSnmpGetCommStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ModemAdmConfSnmpGetCommStr_Type.__name__ = "DisplayString"
_ModemAdmConfSnmpGetCommStr_Object = MibScalar
modemAdmConfSnmpGetCommStr = _ModemAdmConfSnmpGetCommStr_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 4, 5),
    _ModemAdmConfSnmpGetCommStr_Type()
)
modemAdmConfSnmpGetCommStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmConfSnmpGetCommStr.setStatus("current")


class _ModemAdmConfSnmpSetCommStr_Type(DisplayString):
    """Custom type modemAdmConfSnmpSetCommStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ModemAdmConfSnmpSetCommStr_Type.__name__ = "DisplayString"
_ModemAdmConfSnmpSetCommStr_Object = MibScalar
modemAdmConfSnmpSetCommStr = _ModemAdmConfSnmpSetCommStr_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 4, 6),
    _ModemAdmConfSnmpSetCommStr_Type()
)
modemAdmConfSnmpSetCommStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmConfSnmpSetCommStr.setStatus("current")


class _ModemAdmConfSnmpAdminCommStr_Type(DisplayString):
    """Custom type modemAdmConfSnmpAdminCommStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ModemAdmConfSnmpAdminCommStr_Type.__name__ = "DisplayString"
_ModemAdmConfSnmpAdminCommStr_Object = MibScalar
modemAdmConfSnmpAdminCommStr = _ModemAdmConfSnmpAdminCommStr_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 4, 7),
    _ModemAdmConfSnmpAdminCommStr_Type()
)
modemAdmConfSnmpAdminCommStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmConfSnmpAdminCommStr.setStatus("current")


class _ModemAdmConfLoginUsername_Type(DisplayString):
    """Custom type modemAdmConfLoginUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 16),
    )


_ModemAdmConfLoginUsername_Type.__name__ = "DisplayString"
_ModemAdmConfLoginUsername_Object = MibScalar
modemAdmConfLoginUsername = _ModemAdmConfLoginUsername_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 4, 8),
    _ModemAdmConfLoginUsername_Type()
)
modemAdmConfLoginUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmConfLoginUsername.setStatus("current")


class _ModemAdmConfLoginPassword_Type(DisplayString):
    """Custom type modemAdmConfLoginPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ModemAdmConfLoginPassword_Type.__name__ = "DisplayString"
_ModemAdmConfLoginPassword_Object = MibScalar
modemAdmConfLoginPassword = _ModemAdmConfLoginPassword_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 4, 9),
    _ModemAdmConfLoginPassword_Type()
)
modemAdmConfLoginPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmConfLoginPassword.setStatus("current")
_ModemAdmConfFtpServerIp_Type = IpAddress
_ModemAdmConfFtpServerIp_Object = MibScalar
modemAdmConfFtpServerIp = _ModemAdmConfFtpServerIp_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 4, 10),
    _ModemAdmConfFtpServerIp_Type()
)
modemAdmConfFtpServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmConfFtpServerIp.setStatus("current")


class _ModemAdmConfFtpUsername_Type(DisplayString):
    """Custom type modemAdmConfFtpUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ModemAdmConfFtpUsername_Type.__name__ = "DisplayString"
_ModemAdmConfFtpUsername_Object = MibScalar
modemAdmConfFtpUsername = _ModemAdmConfFtpUsername_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 4, 11),
    _ModemAdmConfFtpUsername_Type()
)
modemAdmConfFtpUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmConfFtpUsername.setStatus("current")


class _ModemAdmConfFtpPassword_Type(DisplayString):
    """Custom type modemAdmConfFtpPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ModemAdmConfFtpPassword_Type.__name__ = "DisplayString"
_ModemAdmConfFtpPassword_Object = MibScalar
modemAdmConfFtpPassword = _ModemAdmConfFtpPassword_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 4, 12),
    _ModemAdmConfFtpPassword_Type()
)
modemAdmConfFtpPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmConfFtpPassword.setStatus("current")


class _ModemAdmConfFtpFile_Type(DisplayString):
    """Custom type modemAdmConfFtpFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ModemAdmConfFtpFile_Type.__name__ = "DisplayString"
_ModemAdmConfFtpFile_Object = MibScalar
modemAdmConfFtpFile = _ModemAdmConfFtpFile_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 4, 13),
    _ModemAdmConfFtpFile_Type()
)
modemAdmConfFtpFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmConfFtpFile.setStatus("current")


class _ModemAdmConfDeviceUpgradeStart_Type(Integer32):
    """Custom type modemAdmConfDeviceUpgradeStart based on Integer32"""
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


_ModemAdmConfDeviceUpgradeStart_Type.__name__ = "Integer32"
_ModemAdmConfDeviceUpgradeStart_Object = MibScalar
modemAdmConfDeviceUpgradeStart = _ModemAdmConfDeviceUpgradeStart_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 4, 14),
    _ModemAdmConfDeviceUpgradeStart_Type()
)
modemAdmConfDeviceUpgradeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmConfDeviceUpgradeStart.setStatus("current")


class _ModemAdmConfSimUpgradeStart_Type(Integer32):
    """Custom type modemAdmConfSimUpgradeStart based on Integer32"""
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


_ModemAdmConfSimUpgradeStart_Type.__name__ = "Integer32"
_ModemAdmConfSimUpgradeStart_Object = MibScalar
modemAdmConfSimUpgradeStart = _ModemAdmConfSimUpgradeStart_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 4, 15),
    _ModemAdmConfSimUpgradeStart_Type()
)
modemAdmConfSimUpgradeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmConfSimUpgradeStart.setStatus("current")


class _ModemAdmConfSystemReboot_Type(Integer32):
    """Custom type modemAdmConfSystemReboot based on Integer32"""
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


_ModemAdmConfSystemReboot_Type.__name__ = "Integer32"
_ModemAdmConfSystemReboot_Object = MibScalar
modemAdmConfSystemReboot = _ModemAdmConfSystemReboot_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 4, 16),
    _ModemAdmConfSystemReboot_Type()
)
modemAdmConfSystemReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmConfSystemReboot.setStatus("current")


class _ModemAdmConfReset_Type(Integer32):
    """Custom type modemAdmConfReset based on Integer32"""
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


_ModemAdmConfReset_Type.__name__ = "Integer32"
_ModemAdmConfReset_Object = MibScalar
modemAdmConfReset = _ModemAdmConfReset_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 4, 17),
    _ModemAdmConfReset_Type()
)
modemAdmConfReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmConfReset.setStatus("current")
_WhispPlvModemAdmWConfig_ObjectIdentity = ObjectIdentity
whispPlvModemAdmWConfig = _WhispPlvModemAdmWConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 5)
)


class _ModemAdmWConfNatConfig_Type(Integer32):
    """Custom type modemAdmWConfNatConfig based on Integer32"""
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


_ModemAdmWConfNatConfig_Type.__name__ = "Integer32"
_ModemAdmWConfNatConfig_Object = MibScalar
modemAdmWConfNatConfig = _ModemAdmWConfNatConfig_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 5, 1),
    _ModemAdmWConfNatConfig_Type()
)
modemAdmWConfNatConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmWConfNatConfig.setStatus("current")


class _ModemAdmWConfWanConfig_Type(Integer32):
    """Custom type modemAdmWConfWanConfig based on Integer32"""
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


_ModemAdmWConfWanConfig_Type.__name__ = "Integer32"
_ModemAdmWConfWanConfig_Object = MibScalar
modemAdmWConfWanConfig = _ModemAdmWConfWanConfig_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 5, 2),
    _ModemAdmWConfWanConfig_Type()
)
modemAdmWConfWanConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmWConfWanConfig.setStatus("current")
_ModemAdmWConfWanIp_Type = IpAddress
_ModemAdmWConfWanIp_Object = MibScalar
modemAdmWConfWanIp = _ModemAdmWConfWanIp_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 5, 3),
    _ModemAdmWConfWanIp_Type()
)
modemAdmWConfWanIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmWConfWanIp.setStatus("current")
_ModemAdmWConfSubnetMask_Type = IpAddress
_ModemAdmWConfSubnetMask_Object = MibScalar
modemAdmWConfSubnetMask = _ModemAdmWConfSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 5, 4),
    _ModemAdmWConfSubnetMask_Type()
)
modemAdmWConfSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmWConfSubnetMask.setStatus("current")
_ModemAdmWConfGateway_Type = IpAddress
_ModemAdmWConfGateway_Object = MibScalar
modemAdmWConfGateway = _ModemAdmWConfGateway_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 5, 5),
    _ModemAdmWConfGateway_Type()
)
modemAdmWConfGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmWConfGateway.setStatus("current")
_ModemAdmWConfDNS1_Type = IpAddress
_ModemAdmWConfDNS1_Object = MibScalar
modemAdmWConfDNS1 = _ModemAdmWConfDNS1_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 5, 6),
    _ModemAdmWConfDNS1_Type()
)
modemAdmWConfDNS1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmWConfDNS1.setStatus("current")
_ModemAdmWConfDNS2_Type = IpAddress
_ModemAdmWConfDNS2_Object = MibScalar
modemAdmWConfDNS2 = _ModemAdmWConfDNS2_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 5, 7),
    _ModemAdmWConfDNS2_Type()
)
modemAdmWConfDNS2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmWConfDNS2.setStatus("current")


class _ModemAdmWConfDhcpConfig_Type(Integer32):
    """Custom type modemAdmWConfDhcpConfig based on Integer32"""
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


_ModemAdmWConfDhcpConfig_Type.__name__ = "Integer32"
_ModemAdmWConfDhcpConfig_Object = MibScalar
modemAdmWConfDhcpConfig = _ModemAdmWConfDhcpConfig_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 5, 8),
    _ModemAdmWConfDhcpConfig_Type()
)
modemAdmWConfDhcpConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmWConfDhcpConfig.setStatus("current")
_ModemAdmWConfDhcpStartIp_Type = IpAddress
_ModemAdmWConfDhcpStartIp_Object = MibScalar
modemAdmWConfDhcpStartIp = _ModemAdmWConfDhcpStartIp_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 5, 9),
    _ModemAdmWConfDhcpStartIp_Type()
)
modemAdmWConfDhcpStartIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmWConfDhcpStartIp.setStatus("current")
_ModemAdmWConfDhcpEndIp_Type = IpAddress
_ModemAdmWConfDhcpEndIp_Object = MibScalar
modemAdmWConfDhcpEndIp = _ModemAdmWConfDhcpEndIp_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 5, 10),
    _ModemAdmWConfDhcpEndIp_Type()
)
modemAdmWConfDhcpEndIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmWConfDhcpEndIp.setStatus("current")


class _ModemAdmWConfDhcpLeaseTime_Type(Integer32):
    """Custom type modemAdmWConfDhcpLeaseTime based on Integer32"""
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


_ModemAdmWConfDhcpLeaseTime_Type.__name__ = "Integer32"
_ModemAdmWConfDhcpLeaseTime_Object = MibScalar
modemAdmWConfDhcpLeaseTime = _ModemAdmWConfDhcpLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 5, 11),
    _ModemAdmWConfDhcpLeaseTime_Type()
)
modemAdmWConfDhcpLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmWConfDhcpLeaseTime.setStatus("current")


class _ModemAdmWConfDmzConfig_Type(Integer32):
    """Custom type modemAdmWConfDmzConfig based on Integer32"""
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


_ModemAdmWConfDmzConfig_Type.__name__ = "Integer32"
_ModemAdmWConfDmzConfig_Object = MibScalar
modemAdmWConfDmzConfig = _ModemAdmWConfDmzConfig_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 5, 12),
    _ModemAdmWConfDmzConfig_Type()
)
modemAdmWConfDmzConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmWConfDmzConfig.setStatus("current")
_ModemAdmWConfDmzIp_Type = IpAddress
_ModemAdmWConfDmzIp_Object = MibScalar
modemAdmWConfDmzIp = _ModemAdmWConfDmzIp_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 5, 13),
    _ModemAdmWConfDmzIp_Type()
)
modemAdmWConfDmzIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmWConfDmzIp.setStatus("current")
_WhispPlvModemAdmSnmpAcessConfig_ObjectIdentity = ObjectIdentity
whispPlvModemAdmSnmpAcessConfig = _WhispPlvModemAdmSnmpAcessConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 6)
)
_ModemAdmSnmpAccessIpNetwork1_Type = IpAddress
_ModemAdmSnmpAccessIpNetwork1_Object = MibScalar
modemAdmSnmpAccessIpNetwork1 = _ModemAdmSnmpAccessIpNetwork1_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 6, 1),
    _ModemAdmSnmpAccessIpNetwork1_Type()
)
modemAdmSnmpAccessIpNetwork1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmSnmpAccessIpNetwork1.setStatus("current")
_ModemAdmSnmpAccessIpNetworkMask1_Type = IpAddress
_ModemAdmSnmpAccessIpNetworkMask1_Object = MibScalar
modemAdmSnmpAccessIpNetworkMask1 = _ModemAdmSnmpAccessIpNetworkMask1_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 6, 2),
    _ModemAdmSnmpAccessIpNetworkMask1_Type()
)
modemAdmSnmpAccessIpNetworkMask1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmSnmpAccessIpNetworkMask1.setStatus("current")
_ModemAdmSnmpAccessIpNetwork2_Type = IpAddress
_ModemAdmSnmpAccessIpNetwork2_Object = MibScalar
modemAdmSnmpAccessIpNetwork2 = _ModemAdmSnmpAccessIpNetwork2_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 6, 3),
    _ModemAdmSnmpAccessIpNetwork2_Type()
)
modemAdmSnmpAccessIpNetwork2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmSnmpAccessIpNetwork2.setStatus("current")
_ModemAdmSnmpAccessIpNetworkMask2_Type = IpAddress
_ModemAdmSnmpAccessIpNetworkMask2_Object = MibScalar
modemAdmSnmpAccessIpNetworkMask2 = _ModemAdmSnmpAccessIpNetworkMask2_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 6, 4),
    _ModemAdmSnmpAccessIpNetworkMask2_Type()
)
modemAdmSnmpAccessIpNetworkMask2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmSnmpAccessIpNetworkMask2.setStatus("current")
_ModemAdmSnmpAccessIpNetwork3_Type = IpAddress
_ModemAdmSnmpAccessIpNetwork3_Object = MibScalar
modemAdmSnmpAccessIpNetwork3 = _ModemAdmSnmpAccessIpNetwork3_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 6, 5),
    _ModemAdmSnmpAccessIpNetwork3_Type()
)
modemAdmSnmpAccessIpNetwork3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmSnmpAccessIpNetwork3.setStatus("current")
_ModemAdmSnmpAccessIpNetworkMask3_Type = IpAddress
_ModemAdmSnmpAccessIpNetworkMask3_Object = MibScalar
modemAdmSnmpAccessIpNetworkMask3 = _ModemAdmSnmpAccessIpNetworkMask3_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 6, 6),
    _ModemAdmSnmpAccessIpNetworkMask3_Type()
)
modemAdmSnmpAccessIpNetworkMask3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmSnmpAccessIpNetworkMask3.setStatus("current")
_ModemAdmSnmpAccessIpNetwork4_Type = IpAddress
_ModemAdmSnmpAccessIpNetwork4_Object = MibScalar
modemAdmSnmpAccessIpNetwork4 = _ModemAdmSnmpAccessIpNetwork4_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 6, 7),
    _ModemAdmSnmpAccessIpNetwork4_Type()
)
modemAdmSnmpAccessIpNetwork4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmSnmpAccessIpNetwork4.setStatus("current")
_ModemAdmSnmpAccessIpNetworkMask4_Type = IpAddress
_ModemAdmSnmpAccessIpNetworkMask4_Object = MibScalar
modemAdmSnmpAccessIpNetworkMask4 = _ModemAdmSnmpAccessIpNetworkMask4_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 6, 8),
    _ModemAdmSnmpAccessIpNetworkMask4_Type()
)
modemAdmSnmpAccessIpNetworkMask4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmSnmpAccessIpNetworkMask4.setStatus("current")
_ModemAdmSnmpAccessIpNetwork5_Type = IpAddress
_ModemAdmSnmpAccessIpNetwork5_Object = MibScalar
modemAdmSnmpAccessIpNetwork5 = _ModemAdmSnmpAccessIpNetwork5_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 6, 9),
    _ModemAdmSnmpAccessIpNetwork5_Type()
)
modemAdmSnmpAccessIpNetwork5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmSnmpAccessIpNetwork5.setStatus("current")
_ModemAdmSnmpAccessIpNetworkMask5_Type = IpAddress
_ModemAdmSnmpAccessIpNetworkMask5_Object = MibScalar
modemAdmSnmpAccessIpNetworkMask5 = _ModemAdmSnmpAccessIpNetworkMask5_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 6, 10),
    _ModemAdmSnmpAccessIpNetworkMask5_Type()
)
modemAdmSnmpAccessIpNetworkMask5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmSnmpAccessIpNetworkMask5.setStatus("current")
_ModemAdmSnmpAccessIpNetwork6_Type = IpAddress
_ModemAdmSnmpAccessIpNetwork6_Object = MibScalar
modemAdmSnmpAccessIpNetwork6 = _ModemAdmSnmpAccessIpNetwork6_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 6, 11),
    _ModemAdmSnmpAccessIpNetwork6_Type()
)
modemAdmSnmpAccessIpNetwork6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmSnmpAccessIpNetwork6.setStatus("current")
_ModemAdmSnmpAccessIpNetworkMask6_Type = IpAddress
_ModemAdmSnmpAccessIpNetworkMask6_Object = MibScalar
modemAdmSnmpAccessIpNetworkMask6 = _ModemAdmSnmpAccessIpNetworkMask6_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 6, 12),
    _ModemAdmSnmpAccessIpNetworkMask6_Type()
)
modemAdmSnmpAccessIpNetworkMask6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmSnmpAccessIpNetworkMask6.setStatus("current")
_ModemAdmSnmpAccessIpNetwork7_Type = IpAddress
_ModemAdmSnmpAccessIpNetwork7_Object = MibScalar
modemAdmSnmpAccessIpNetwork7 = _ModemAdmSnmpAccessIpNetwork7_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 6, 13),
    _ModemAdmSnmpAccessIpNetwork7_Type()
)
modemAdmSnmpAccessIpNetwork7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmSnmpAccessIpNetwork7.setStatus("current")
_ModemAdmSnmpAccessIpNetworkMask7_Type = IpAddress
_ModemAdmSnmpAccessIpNetworkMask7_Object = MibScalar
modemAdmSnmpAccessIpNetworkMask7 = _ModemAdmSnmpAccessIpNetworkMask7_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 6, 14),
    _ModemAdmSnmpAccessIpNetworkMask7_Type()
)
modemAdmSnmpAccessIpNetworkMask7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmSnmpAccessIpNetworkMask7.setStatus("current")
_ModemAdmSnmpAccessIpNetwork8_Type = IpAddress
_ModemAdmSnmpAccessIpNetwork8_Object = MibScalar
modemAdmSnmpAccessIpNetwork8 = _ModemAdmSnmpAccessIpNetwork8_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 6, 15),
    _ModemAdmSnmpAccessIpNetwork8_Type()
)
modemAdmSnmpAccessIpNetwork8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmSnmpAccessIpNetwork8.setStatus("current")
_ModemAdmSnmpAccessIpNetworkMask8_Type = IpAddress
_ModemAdmSnmpAccessIpNetworkMask8_Object = MibScalar
modemAdmSnmpAccessIpNetworkMask8 = _ModemAdmSnmpAccessIpNetworkMask8_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 6, 16),
    _ModemAdmSnmpAccessIpNetworkMask8_Type()
)
modemAdmSnmpAccessIpNetworkMask8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmSnmpAccessIpNetworkMask8.setStatus("current")
_ModemAdmSnmpAccessIpNetwork9_Type = IpAddress
_ModemAdmSnmpAccessIpNetwork9_Object = MibScalar
modemAdmSnmpAccessIpNetwork9 = _ModemAdmSnmpAccessIpNetwork9_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 6, 17),
    _ModemAdmSnmpAccessIpNetwork9_Type()
)
modemAdmSnmpAccessIpNetwork9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmSnmpAccessIpNetwork9.setStatus("current")
_ModemAdmSnmpAccessIpNetworkMask9_Type = IpAddress
_ModemAdmSnmpAccessIpNetworkMask9_Object = MibScalar
modemAdmSnmpAccessIpNetworkMask9 = _ModemAdmSnmpAccessIpNetworkMask9_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 6, 18),
    _ModemAdmSnmpAccessIpNetworkMask9_Type()
)
modemAdmSnmpAccessIpNetworkMask9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmSnmpAccessIpNetworkMask9.setStatus("current")
_ModemAdmSnmpAccessIpNetwork10_Type = IpAddress
_ModemAdmSnmpAccessIpNetwork10_Object = MibScalar
modemAdmSnmpAccessIpNetwork10 = _ModemAdmSnmpAccessIpNetwork10_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 6, 19),
    _ModemAdmSnmpAccessIpNetwork10_Type()
)
modemAdmSnmpAccessIpNetwork10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmSnmpAccessIpNetwork10.setStatus("current")
_ModemAdmSnmpAccessIpNetworkMask10_Type = IpAddress
_ModemAdmSnmpAccessIpNetworkMask10_Object = MibScalar
modemAdmSnmpAccessIpNetworkMask10 = _ModemAdmSnmpAccessIpNetworkMask10_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 6, 20),
    _ModemAdmSnmpAccessIpNetworkMask10_Type()
)
modemAdmSnmpAccessIpNetworkMask10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmSnmpAccessIpNetworkMask10.setStatus("current")
_WhispPlvModemAdmRepeaterConfig_ObjectIdentity = ObjectIdentity
whispPlvModemAdmRepeaterConfig = _WhispPlvModemAdmRepeaterConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 7)
)


class _ModemAdmRepeaterConfOperatingMode_Type(Integer32):
    """Custom type modemAdmRepeaterConfOperatingMode based on Integer32"""
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
        *(("normal", 1),
          ("repeater", 2),
          ("useWithRepeater", 3))
    )


_ModemAdmRepeaterConfOperatingMode_Type.__name__ = "Integer32"
_ModemAdmRepeaterConfOperatingMode_Object = MibScalar
modemAdmRepeaterConfOperatingMode = _ModemAdmRepeaterConfOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 7, 1),
    _ModemAdmRepeaterConfOperatingMode_Type()
)
modemAdmRepeaterConfOperatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmRepeaterConfOperatingMode.setStatus("current")
_ModemAdmRepeaterConfModemMAC1_Type = MacAddress
_ModemAdmRepeaterConfModemMAC1_Object = MibScalar
modemAdmRepeaterConfModemMAC1 = _ModemAdmRepeaterConfModemMAC1_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 7, 2),
    _ModemAdmRepeaterConfModemMAC1_Type()
)
modemAdmRepeaterConfModemMAC1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmRepeaterConfModemMAC1.setStatus("current")
_ModemAdmRepeaterConfModemMAC2_Type = MacAddress
_ModemAdmRepeaterConfModemMAC2_Object = MibScalar
modemAdmRepeaterConfModemMAC2 = _ModemAdmRepeaterConfModemMAC2_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 7, 3),
    _ModemAdmRepeaterConfModemMAC2_Type()
)
modemAdmRepeaterConfModemMAC2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmRepeaterConfModemMAC2.setStatus("current")
_ModemAdmRepeaterConfModemMAC3_Type = MacAddress
_ModemAdmRepeaterConfModemMAC3_Object = MibScalar
modemAdmRepeaterConfModemMAC3 = _ModemAdmRepeaterConfModemMAC3_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 7, 4),
    _ModemAdmRepeaterConfModemMAC3_Type()
)
modemAdmRepeaterConfModemMAC3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmRepeaterConfModemMAC3.setStatus("current")
_ModemAdmRepeaterConfModemMAC4_Type = MacAddress
_ModemAdmRepeaterConfModemMAC4_Object = MibScalar
modemAdmRepeaterConfModemMAC4 = _ModemAdmRepeaterConfModemMAC4_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 7, 5),
    _ModemAdmRepeaterConfModemMAC4_Type()
)
modemAdmRepeaterConfModemMAC4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmRepeaterConfModemMAC4.setStatus("current")
_WhispPlvModemAdmVLANTable_Object = MibTable
whispPlvModemAdmVLANTable = _WhispPlvModemAdmVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 8)
)
if mibBuilder.loadTexts:
    whispPlvModemAdmVLANTable.setStatus("current")
_WhispPlvModemAdmVLANEntry_Object = MibTableRow
whispPlvModemAdmVLANEntry = _WhispPlvModemAdmVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 8, 1)
)
whispPlvModemAdmVLANEntry.setIndexNames(
    (0, "WHISP-PLV-MODEM-MIB", "modemAdmVLANIndex"),
)
if mibBuilder.loadTexts:
    whispPlvModemAdmVLANEntry.setStatus("current")


class _ModemAdmVLANIndex_Type(Integer32):
    """Custom type modemAdmVLANIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ModemAdmVLANIndex_Type.__name__ = "Integer32"
_ModemAdmVLANIndex_Object = MibTableColumn
modemAdmVLANIndex = _ModemAdmVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 8, 1, 1),
    _ModemAdmVLANIndex_Type()
)
modemAdmVLANIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    modemAdmVLANIndex.setStatus("current")
_ModemAdmVLANPhysAddress_Type = MacAddress
_ModemAdmVLANPhysAddress_Object = MibTableColumn
modemAdmVLANPhysAddress = _ModemAdmVLANPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 8, 1, 2),
    _ModemAdmVLANPhysAddress_Type()
)
modemAdmVLANPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemAdmVLANPhysAddress.setStatus("current")


class _ModemAdmVLANId_Type(Integer32):
    """Custom type modemAdmVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_ModemAdmVLANId_Type.__name__ = "Integer32"
_ModemAdmVLANId_Object = MibTableColumn
modemAdmVLANId = _ModemAdmVLANId_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 1, 8, 1, 3),
    _ModemAdmVLANId_Type()
)
modemAdmVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAdmVLANId.setStatus("current")
_WhispPlvModemEvents_ObjectIdentity = ObjectIdentity
whispPlvModemEvents = _WhispPlvModemEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 2)
)
_ModemTrapPrefix_ObjectIdentity = ObjectIdentity
modemTrapPrefix = _ModemTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 2, 0)
)
_WhispPlvModemConformance_ObjectIdentity = ObjectIdentity
whispPlvModemConformance = _WhispPlvModemConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 3)
)
_WhispPlvModemGroups_ObjectIdentity = ObjectIdentity
whispPlvModemGroups = _WhispPlvModemGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 3, 1)
)
_WhispPlvModemCompliances_ObjectIdentity = ObjectIdentity
whispPlvModemCompliances = _WhispPlvModemCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 3, 2)
)

# Managed Objects groups

whispPlvModemInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 3, 1, 1)
)
whispPlvModemInfoGroup.setObjects(
      *(("WHISP-PLV-MODEM-MIB", "modemInfoModel"),
        ("WHISP-PLV-MODEM-MIB", "modemInfoSerialNumber"),
        ("WHISP-PLV-MODEM-MIB", "modemInfoDeviceMac"),
        ("WHISP-PLV-MODEM-MIB", "modemInfoPlcMac"),
        ("WHISP-PLV-MODEM-MIB", "modemInfoHardwareVer"),
        ("WHISP-PLV-MODEM-MIB", "modemInfoDeviceFirmwareVer"),
        ("WHISP-PLV-MODEM-MIB", "modemInfoBootLoaderVer"),
        ("WHISP-PLV-MODEM-MIB", "modemInfoSimFirmwareVer"),
        ("WHISP-PLV-MODEM-MIB", "modemInfoDeviceUpgradeStatus"),
        ("WHISP-PLV-MODEM-MIB", "modemInfoSimUpgradeStatus"),
        ("WHISP-PLV-MODEM-MIB", "modemInfoCurrentMode"),
        ("WHISP-PLV-MODEM-MIB", "modemInfoActiveBandwidthConfig"),
        ("WHISP-PLV-MODEM-MIB", "modemInfoActiveUpLinkBandwidth"),
        ("WHISP-PLV-MODEM-MIB", "modemInfoActiveDownLinkBandwidth"))
)
if mibBuilder.loadTexts:
    whispPlvModemInfoGroup.setStatus("current")

whispPlvModemConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 3, 1, 2)
)
whispPlvModemConfigGroup.setObjects(
      *(("WHISP-PLV-MODEM-MIB", "modemConfPacketPriorityConfig"),
        ("WHISP-PLV-MODEM-MIB", "modemConfFixedQoSConfig"),
        ("WHISP-PLV-MODEM-MIB", "modemConfUpLinkDataRate"),
        ("WHISP-PLV-MODEM-MIB", "modemConfDownLinkDataRate"),
        ("WHISP-PLV-MODEM-MIB", "modemConfPSD"),
        ("WHISP-PLV-MODEM-MIB", "modemConfUpLinkMir"),
        ("WHISP-PLV-MODEM-MIB", "modemConfDownLinkMir"))
)
if mibBuilder.loadTexts:
    whispPlvModemConfigGroup.setStatus("current")

whispPlvModemTrapConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 3, 1, 3)
)
whispPlvModemTrapConfigGroup.setObjects(
      *(("WHISP-PLV-MODEM-MIB", "modemConfTrapIp1"),
        ("WHISP-PLV-MODEM-MIB", "modemConfTrapCommStr1"),
        ("WHISP-PLV-MODEM-MIB", "modemConfTrapIp2"),
        ("WHISP-PLV-MODEM-MIB", "modemConfTrapCommStr2"),
        ("WHISP-PLV-MODEM-MIB", "modemConfTrapIp3"),
        ("WHISP-PLV-MODEM-MIB", "modemConfTrapCommStr3"),
        ("WHISP-PLV-MODEM-MIB", "modemConfTrapIp4"),
        ("WHISP-PLV-MODEM-MIB", "modemConfTrapCommStr4"),
        ("WHISP-PLV-MODEM-MIB", "modemConfTrapIp5"),
        ("WHISP-PLV-MODEM-MIB", "modemConfTrapCommStr5"),
        ("WHISP-PLV-MODEM-MIB", "modemConfTrapIp6"),
        ("WHISP-PLV-MODEM-MIB", "modemConfTrapCommStr6"),
        ("WHISP-PLV-MODEM-MIB", "modemConfTrapIp7"),
        ("WHISP-PLV-MODEM-MIB", "modemConfTrapCommStr7"),
        ("WHISP-PLV-MODEM-MIB", "modemConfTrapIp8"),
        ("WHISP-PLV-MODEM-MIB", "modemConfTrapCommStr8"),
        ("WHISP-PLV-MODEM-MIB", "modemConfTrapIp9"),
        ("WHISP-PLV-MODEM-MIB", "modemConfTrapCommStr9"),
        ("WHISP-PLV-MODEM-MIB", "modemConfTrapIp10"),
        ("WHISP-PLV-MODEM-MIB", "modemConfTrapCommStr10"))
)
if mibBuilder.loadTexts:
    whispPlvModemTrapConfigGroup.setStatus("current")

whispPlvModemAdmConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 3, 1, 4)
)
whispPlvModemAdmConfigGroup.setObjects(
      *(("WHISP-PLV-MODEM-MIB", "modemAdmConfIpConfig"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmConfIp"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmConfIpSubnetMask"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmConfNEK"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmConfSnmpGetCommStr"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmConfSnmpSetCommStr"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmConfSnmpAdminCommStr"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmConfLoginUsername"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmConfLoginPassword"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmConfFtpServerIp"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmConfFtpUsername"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmConfFtpPassword"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmConfFtpFile"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmConfDeviceUpgradeStart"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmConfSimUpgradeStart"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmConfSystemReboot"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmConfReset"))
)
if mibBuilder.loadTexts:
    whispPlvModemAdmConfigGroup.setStatus("current")

whispPlvModemAdmWConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 3, 1, 5)
)
whispPlvModemAdmWConfigGroup.setObjects(
      *(("WHISP-PLV-MODEM-MIB", "modemAdmWConfNatConfig"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmWConfWanConfig"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmWConfWanIp"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmWConfSubnetMask"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmWConfGateway"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmWConfDNS1"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmWConfDNS2"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmWConfDhcpConfig"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmWConfDhcpStartIp"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmWConfDhcpEndIp"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmWConfDhcpLeaseTime"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmWConfDmzConfig"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmWConfDmzIp"))
)
if mibBuilder.loadTexts:
    whispPlvModemAdmWConfigGroup.setStatus("current")

whispPlvModemAdmSnmpAcessConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 3, 1, 6)
)
whispPlvModemAdmSnmpAcessConfigGroup.setObjects(
      *(("WHISP-PLV-MODEM-MIB", "modemAdmSnmpAccessIpNetwork1"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmSnmpAccessIpNetworkMask1"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmSnmpAccessIpNetwork2"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmSnmpAccessIpNetworkMask2"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmSnmpAccessIpNetwork3"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmSnmpAccessIpNetworkMask3"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmSnmpAccessIpNetwork4"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmSnmpAccessIpNetworkMask4"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmSnmpAccessIpNetwork5"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmSnmpAccessIpNetworkMask5"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmSnmpAccessIpNetwork6"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmSnmpAccessIpNetworkMask6"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmSnmpAccessIpNetwork7"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmSnmpAccessIpNetworkMask7"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmSnmpAccessIpNetwork8"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmSnmpAccessIpNetworkMask8"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmSnmpAccessIpNetwork9"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmSnmpAccessIpNetworkMask9"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmSnmpAccessIpNetwork10"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmSnmpAccessIpNetworkMask10"))
)
if mibBuilder.loadTexts:
    whispPlvModemAdmSnmpAcessConfigGroup.setStatus("current")

whispPlvModemAdmRepeaterConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 3, 1, 8)
)
whispPlvModemAdmRepeaterConfigGroup.setObjects(
      *(("WHISP-PLV-MODEM-MIB", "modemAdmRepeaterConfOperatingMode"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmRepeaterConfModemMAC1"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmRepeaterConfModemMAC2"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmRepeaterConfModemMAC3"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmRepeaterConfModemMAC4"))
)
if mibBuilder.loadTexts:
    whispPlvModemAdmRepeaterConfigGroup.setStatus("current")

whispPlvModemAdmVLANConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 3, 1, 9)
)
whispPlvModemAdmVLANConfigGroup.setObjects(
      *(("WHISP-PLV-MODEM-MIB", "modemAdmVLANPhysAddress"),
        ("WHISP-PLV-MODEM-MIB", "modemAdmVLANId"))
)
if mibBuilder.loadTexts:
    whispPlvModemAdmVLANConfigGroup.setStatus("current")


# Notification objects

modemTrapDeviceUpgradeStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 2, 0, 1)
)
modemTrapDeviceUpgradeStarted.setObjects(
      *(("WHISP-PLV-MODEM-MIB", "modemInfoDeviceUpgradeStatus"),
        ("WHISP-PLV-MODEM-MIB", "modemInfoDeviceFirmwareVer"))
)
if mibBuilder.loadTexts:
    modemTrapDeviceUpgradeStarted.setStatus(
        "current"
    )

modemTrapDeviceUpgradeCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 2, 0, 2)
)
modemTrapDeviceUpgradeCompleted.setObjects(
      *(("WHISP-PLV-MODEM-MIB", "modemInfoDeviceUpgradeStatus"),
        ("WHISP-PLV-MODEM-MIB", "modemInfoDeviceFirmwareVer"))
)
if mibBuilder.loadTexts:
    modemTrapDeviceUpgradeCompleted.setStatus(
        "current"
    )

modemTrapSimUpgradeStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 2, 0, 3)
)
modemTrapSimUpgradeStarted.setObjects(
      *(("WHISP-PLV-MODEM-MIB", "modemInfoSimUpgradeStatus"),
        ("WHISP-PLV-MODEM-MIB", "modemInfoSimFirmwareVer"))
)
if mibBuilder.loadTexts:
    modemTrapSimUpgradeStarted.setStatus(
        "current"
    )

modemTrapSimUpgradeCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 2, 0, 4)
)
modemTrapSimUpgradeCompleted.setObjects(
      *(("WHISP-PLV-MODEM-MIB", "modemInfoSimUpgradeStatus"),
        ("WHISP-PLV-MODEM-MIB", "modemInfoSimFirmwareVer"))
)
if mibBuilder.loadTexts:
    modemTrapSimUpgradeCompleted.setStatus(
        "current"
    )


# Notifications groups

whispPlvModemNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 3, 1, 7)
)
whispPlvModemNotificationsGroup.setObjects(
      *(("WHISP-PLV-MODEM-MIB", "modemTrapDeviceUpgradeStarted"),
        ("WHISP-PLV-MODEM-MIB", "modemTrapDeviceUpgradeCompleted"),
        ("WHISP-PLV-MODEM-MIB", "modemTrapSimUpgradeStarted"),
        ("WHISP-PLV-MODEM-MIB", "modemTrapSimUpgradeCompleted"))
)
if mibBuilder.loadTexts:
    whispPlvModemNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

whispPlvModemCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 7, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    whispPlvModemCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WHISP-PLV-MODEM-MIB",
    **{"whispPlvModemMIB": whispPlvModemMIB,
       "whispPlvModemObjects": whispPlvModemObjects,
       "whispPlvModemInfo": whispPlvModemInfo,
       "modemInfoModel": modemInfoModel,
       "modemInfoSerialNumber": modemInfoSerialNumber,
       "modemInfoDeviceMac": modemInfoDeviceMac,
       "modemInfoPlcMac": modemInfoPlcMac,
       "modemInfoHardwareVer": modemInfoHardwareVer,
       "modemInfoDeviceFirmwareVer": modemInfoDeviceFirmwareVer,
       "modemInfoBootLoaderVer": modemInfoBootLoaderVer,
       "modemInfoSimFirmwareVer": modemInfoSimFirmwareVer,
       "modemInfoDeviceUpgradeStatus": modemInfoDeviceUpgradeStatus,
       "modemInfoSimUpgradeStatus": modemInfoSimUpgradeStatus,
       "modemInfoCurrentMode": modemInfoCurrentMode,
       "modemInfoActiveBandwidthConfig": modemInfoActiveBandwidthConfig,
       "modemInfoActiveUpLinkBandwidth": modemInfoActiveUpLinkBandwidth,
       "modemInfoActiveDownLinkBandwidth": modemInfoActiveDownLinkBandwidth,
       "whispPlvModemConfig": whispPlvModemConfig,
       "modemConfPacketPriorityConfig": modemConfPacketPriorityConfig,
       "modemConfFixedQoSConfig": modemConfFixedQoSConfig,
       "modemConfUpLinkDataRate": modemConfUpLinkDataRate,
       "modemConfDownLinkDataRate": modemConfDownLinkDataRate,
       "modemConfPSD": modemConfPSD,
       "modemConfUpLinkMir": modemConfUpLinkMir,
       "modemConfDownLinkMir": modemConfDownLinkMir,
       "whispPlvModemTrapConfig": whispPlvModemTrapConfig,
       "modemConfTrapIp1": modemConfTrapIp1,
       "modemConfTrapCommStr1": modemConfTrapCommStr1,
       "modemConfTrapIp2": modemConfTrapIp2,
       "modemConfTrapCommStr2": modemConfTrapCommStr2,
       "modemConfTrapIp3": modemConfTrapIp3,
       "modemConfTrapCommStr3": modemConfTrapCommStr3,
       "modemConfTrapIp4": modemConfTrapIp4,
       "modemConfTrapCommStr4": modemConfTrapCommStr4,
       "modemConfTrapIp5": modemConfTrapIp5,
       "modemConfTrapCommStr5": modemConfTrapCommStr5,
       "modemConfTrapIp6": modemConfTrapIp6,
       "modemConfTrapCommStr6": modemConfTrapCommStr6,
       "modemConfTrapIp7": modemConfTrapIp7,
       "modemConfTrapCommStr7": modemConfTrapCommStr7,
       "modemConfTrapIp8": modemConfTrapIp8,
       "modemConfTrapCommStr8": modemConfTrapCommStr8,
       "modemConfTrapIp9": modemConfTrapIp9,
       "modemConfTrapCommStr9": modemConfTrapCommStr9,
       "modemConfTrapIp10": modemConfTrapIp10,
       "modemConfTrapCommStr10": modemConfTrapCommStr10,
       "whispPlvModemAdmConfig": whispPlvModemAdmConfig,
       "modemAdmConfIpConfig": modemAdmConfIpConfig,
       "modemAdmConfIp": modemAdmConfIp,
       "modemAdmConfIpSubnetMask": modemAdmConfIpSubnetMask,
       "modemAdmConfNEK": modemAdmConfNEK,
       "modemAdmConfSnmpGetCommStr": modemAdmConfSnmpGetCommStr,
       "modemAdmConfSnmpSetCommStr": modemAdmConfSnmpSetCommStr,
       "modemAdmConfSnmpAdminCommStr": modemAdmConfSnmpAdminCommStr,
       "modemAdmConfLoginUsername": modemAdmConfLoginUsername,
       "modemAdmConfLoginPassword": modemAdmConfLoginPassword,
       "modemAdmConfFtpServerIp": modemAdmConfFtpServerIp,
       "modemAdmConfFtpUsername": modemAdmConfFtpUsername,
       "modemAdmConfFtpPassword": modemAdmConfFtpPassword,
       "modemAdmConfFtpFile": modemAdmConfFtpFile,
       "modemAdmConfDeviceUpgradeStart": modemAdmConfDeviceUpgradeStart,
       "modemAdmConfSimUpgradeStart": modemAdmConfSimUpgradeStart,
       "modemAdmConfSystemReboot": modemAdmConfSystemReboot,
       "modemAdmConfReset": modemAdmConfReset,
       "whispPlvModemAdmWConfig": whispPlvModemAdmWConfig,
       "modemAdmWConfNatConfig": modemAdmWConfNatConfig,
       "modemAdmWConfWanConfig": modemAdmWConfWanConfig,
       "modemAdmWConfWanIp": modemAdmWConfWanIp,
       "modemAdmWConfSubnetMask": modemAdmWConfSubnetMask,
       "modemAdmWConfGateway": modemAdmWConfGateway,
       "modemAdmWConfDNS1": modemAdmWConfDNS1,
       "modemAdmWConfDNS2": modemAdmWConfDNS2,
       "modemAdmWConfDhcpConfig": modemAdmWConfDhcpConfig,
       "modemAdmWConfDhcpStartIp": modemAdmWConfDhcpStartIp,
       "modemAdmWConfDhcpEndIp": modemAdmWConfDhcpEndIp,
       "modemAdmWConfDhcpLeaseTime": modemAdmWConfDhcpLeaseTime,
       "modemAdmWConfDmzConfig": modemAdmWConfDmzConfig,
       "modemAdmWConfDmzIp": modemAdmWConfDmzIp,
       "whispPlvModemAdmSnmpAcessConfig": whispPlvModemAdmSnmpAcessConfig,
       "modemAdmSnmpAccessIpNetwork1": modemAdmSnmpAccessIpNetwork1,
       "modemAdmSnmpAccessIpNetworkMask1": modemAdmSnmpAccessIpNetworkMask1,
       "modemAdmSnmpAccessIpNetwork2": modemAdmSnmpAccessIpNetwork2,
       "modemAdmSnmpAccessIpNetworkMask2": modemAdmSnmpAccessIpNetworkMask2,
       "modemAdmSnmpAccessIpNetwork3": modemAdmSnmpAccessIpNetwork3,
       "modemAdmSnmpAccessIpNetworkMask3": modemAdmSnmpAccessIpNetworkMask3,
       "modemAdmSnmpAccessIpNetwork4": modemAdmSnmpAccessIpNetwork4,
       "modemAdmSnmpAccessIpNetworkMask4": modemAdmSnmpAccessIpNetworkMask4,
       "modemAdmSnmpAccessIpNetwork5": modemAdmSnmpAccessIpNetwork5,
       "modemAdmSnmpAccessIpNetworkMask5": modemAdmSnmpAccessIpNetworkMask5,
       "modemAdmSnmpAccessIpNetwork6": modemAdmSnmpAccessIpNetwork6,
       "modemAdmSnmpAccessIpNetworkMask6": modemAdmSnmpAccessIpNetworkMask6,
       "modemAdmSnmpAccessIpNetwork7": modemAdmSnmpAccessIpNetwork7,
       "modemAdmSnmpAccessIpNetworkMask7": modemAdmSnmpAccessIpNetworkMask7,
       "modemAdmSnmpAccessIpNetwork8": modemAdmSnmpAccessIpNetwork8,
       "modemAdmSnmpAccessIpNetworkMask8": modemAdmSnmpAccessIpNetworkMask8,
       "modemAdmSnmpAccessIpNetwork9": modemAdmSnmpAccessIpNetwork9,
       "modemAdmSnmpAccessIpNetworkMask9": modemAdmSnmpAccessIpNetworkMask9,
       "modemAdmSnmpAccessIpNetwork10": modemAdmSnmpAccessIpNetwork10,
       "modemAdmSnmpAccessIpNetworkMask10": modemAdmSnmpAccessIpNetworkMask10,
       "whispPlvModemAdmRepeaterConfig": whispPlvModemAdmRepeaterConfig,
       "modemAdmRepeaterConfOperatingMode": modemAdmRepeaterConfOperatingMode,
       "modemAdmRepeaterConfModemMAC1": modemAdmRepeaterConfModemMAC1,
       "modemAdmRepeaterConfModemMAC2": modemAdmRepeaterConfModemMAC2,
       "modemAdmRepeaterConfModemMAC3": modemAdmRepeaterConfModemMAC3,
       "modemAdmRepeaterConfModemMAC4": modemAdmRepeaterConfModemMAC4,
       "whispPlvModemAdmVLANTable": whispPlvModemAdmVLANTable,
       "whispPlvModemAdmVLANEntry": whispPlvModemAdmVLANEntry,
       "modemAdmVLANIndex": modemAdmVLANIndex,
       "modemAdmVLANPhysAddress": modemAdmVLANPhysAddress,
       "modemAdmVLANId": modemAdmVLANId,
       "whispPlvModemEvents": whispPlvModemEvents,
       "modemTrapPrefix": modemTrapPrefix,
       "modemTrapDeviceUpgradeStarted": modemTrapDeviceUpgradeStarted,
       "modemTrapDeviceUpgradeCompleted": modemTrapDeviceUpgradeCompleted,
       "modemTrapSimUpgradeStarted": modemTrapSimUpgradeStarted,
       "modemTrapSimUpgradeCompleted": modemTrapSimUpgradeCompleted,
       "whispPlvModemConformance": whispPlvModemConformance,
       "whispPlvModemGroups": whispPlvModemGroups,
       "whispPlvModemInfoGroup": whispPlvModemInfoGroup,
       "whispPlvModemConfigGroup": whispPlvModemConfigGroup,
       "whispPlvModemTrapConfigGroup": whispPlvModemTrapConfigGroup,
       "whispPlvModemAdmConfigGroup": whispPlvModemAdmConfigGroup,
       "whispPlvModemAdmWConfigGroup": whispPlvModemAdmWConfigGroup,
       "whispPlvModemAdmSnmpAcessConfigGroup": whispPlvModemAdmSnmpAcessConfigGroup,
       "whispPlvModemNotificationsGroup": whispPlvModemNotificationsGroup,
       "whispPlvModemAdmRepeaterConfigGroup": whispPlvModemAdmRepeaterConfigGroup,
       "whispPlvModemAdmVLANConfigGroup": whispPlvModemAdmVLANConfigGroup,
       "whispPlvModemCompliances": whispPlvModemCompliances,
       "whispPlvModemCompliance": whispPlvModemCompliance}
)
