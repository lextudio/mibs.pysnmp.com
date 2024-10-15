# SNMP MIB module (ALCATEL-IND1-TP-DEVICES) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-TP-DEVICES
# Produced by pysmi-1.5.4 at Mon Oct 14 20:37:27 2024
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

(hardwareIND1Devices,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "hardwareIND1Devices")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1TpDevicesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2)
)
alcatelIND1TpDevicesMIB.setRevisions(
        ("2004-03-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FamilyOmniAccess4000_ObjectIdentity = ObjectIdentity
familyOmniAccess4000 = _FamilyOmniAccess4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    familyOmniAccess4000.setStatus("current")
_ChassisOmniAccess4000_ObjectIdentity = ObjectIdentity
chassisOmniAccess4000 = _ChassisOmniAccess4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    chassisOmniAccess4000.setStatus("current")
_DeviceOmniAccess4012_ObjectIdentity = ObjectIdentity
deviceOmniAccess4012 = _DeviceOmniAccess4012_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    deviceOmniAccess4012.setStatus("current")
_DeviceOmniAccess4024_ObjectIdentity = ObjectIdentity
deviceOmniAccess4024 = _DeviceOmniAccess4024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    deviceOmniAccess4024.setStatus("current")
_DeviceOmniAccess4102_ObjectIdentity = ObjectIdentity
deviceOmniAccess4102 = _DeviceOmniAccess4102_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    deviceOmniAccess4102.setStatus("current")
_FansOmniAccess4000_ObjectIdentity = ObjectIdentity
fansOmniAccess4000 = _FansOmniAccess4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    fansOmniAccess4000.setStatus("current")
_PowersOmniAccess4000_ObjectIdentity = ObjectIdentity
powersOmniAccess4000 = _PowersOmniAccess4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 1, 3)
)
if mibBuilder.loadTexts:
    powersOmniAccess4000.setStatus("current")
_ModulesOmniAccess4000_ObjectIdentity = ObjectIdentity
modulesOmniAccess4000 = _ModulesOmniAccess4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 1, 4)
)
if mibBuilder.loadTexts:
    modulesOmniAccess4000.setStatus("current")
_FamilyOmniAccessWireless_ObjectIdentity = ObjectIdentity
familyOmniAccessWireless = _FamilyOmniAccessWireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    familyOmniAccessWireless.setStatus("current")
_ChassisOmniAccessWireless_ObjectIdentity = ObjectIdentity
chassisOmniAccessWireless = _ChassisOmniAccessWireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    chassisOmniAccessWireless.setStatus("current")
_ChassisOmniAccessWirelessSwitch_ObjectIdentity = ObjectIdentity
chassisOmniAccessWirelessSwitch = _ChassisOmniAccessWirelessSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    chassisOmniAccessWirelessSwitch.setStatus("current")
_DeviceOmniAccess5000_ObjectIdentity = ObjectIdentity
deviceOmniAccess5000 = _DeviceOmniAccess5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    deviceOmniAccess5000.setStatus("current")
_DeviceOmniAccess4324_ObjectIdentity = ObjectIdentity
deviceOmniAccess4324 = _DeviceOmniAccess4324_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    deviceOmniAccess4324.setStatus("current")
_DeviceOmniAccess4308_ObjectIdentity = ObjectIdentity
deviceOmniAccess4308 = _DeviceOmniAccess4308_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    deviceOmniAccess4308.setStatus("current")
_DeviceOmniAccess6000_ObjectIdentity = ObjectIdentity
deviceOmniAccess6000 = _DeviceOmniAccess6000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    deviceOmniAccess6000.setStatus("current")
_ChassisOmniAccess6000Wireless_ObjectIdentity = ObjectIdentity
chassisOmniAccess6000Wireless = _ChassisOmniAccess6000Wireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 2, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    chassisOmniAccess6000Wireless.setStatus("current")
_DeviceOmniAccess6000PS2_ObjectIdentity = ObjectIdentity
deviceOmniAccess6000PS2 = _DeviceOmniAccess6000PS2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 2, 1, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    deviceOmniAccess6000PS2.setStatus("current")
_FansOmniAccess6000Wireless_ObjectIdentity = ObjectIdentity
fansOmniAccess6000Wireless = _FansOmniAccess6000Wireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 2, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    fansOmniAccess6000Wireless.setStatus("current")
_PowersOmniAccess6000Wireless_ObjectIdentity = ObjectIdentity
powersOmniAccess6000Wireless = _PowersOmniAccess6000Wireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 2, 1, 1, 4, 3)
)
if mibBuilder.loadTexts:
    powersOmniAccess6000Wireless.setStatus("current")
_ModulesOmniAccess6000Wireless_ObjectIdentity = ObjectIdentity
modulesOmniAccess6000Wireless = _ModulesOmniAccess6000Wireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 2, 1, 1, 4, 4)
)
if mibBuilder.loadTexts:
    modulesOmniAccess6000Wireless.setStatus("current")
_DeviceOmniAccess6000SCI48_ObjectIdentity = ObjectIdentity
deviceOmniAccess6000SCI48 = _DeviceOmniAccess6000SCI48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 2, 1, 1, 4, 4, 1)
)
if mibBuilder.loadTexts:
    deviceOmniAccess6000SCI48.setStatus("current")
_DeviceOmniAccess6000SCII256_ObjectIdentity = ObjectIdentity
deviceOmniAccess6000SCII256 = _DeviceOmniAccess6000SCII256_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 2, 1, 1, 4, 4, 3)
)
if mibBuilder.loadTexts:
    deviceOmniAccess6000SCII256.setStatus("current")
_DeviceOmniAccess6000LC2G_ObjectIdentity = ObjectIdentity
deviceOmniAccess6000LC2G = _DeviceOmniAccess6000LC2G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 2, 1, 1, 4, 4, 4)
)
if mibBuilder.loadTexts:
    deviceOmniAccess6000LC2G.setStatus("current")
_DeviceOmniAccess6000LC2G24F_ObjectIdentity = ObjectIdentity
deviceOmniAccess6000LC2G24F = _DeviceOmniAccess6000LC2G24F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 2, 1, 1, 4, 4, 5)
)
if mibBuilder.loadTexts:
    deviceOmniAccess6000LC2G24F.setStatus("current")
_DeviceOmniAccess6000LC2G24FP_ObjectIdentity = ObjectIdentity
deviceOmniAccess6000LC2G24FP = _DeviceOmniAccess6000LC2G24FP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 2, 1, 1, 4, 4, 6)
)
if mibBuilder.loadTexts:
    deviceOmniAccess6000LC2G24FP.setStatus("current")
_DeviceOmniAccess6000S3C20G_ObjectIdentity = ObjectIdentity
deviceOmniAccess6000S3C20G = _DeviceOmniAccess6000S3C20G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 2, 1, 1, 4, 4, 7)
)
if mibBuilder.loadTexts:
    deviceOmniAccess6000S3C20G.setStatus("current")
_DeviceOmniAccess4302_ObjectIdentity = ObjectIdentity
deviceOmniAccess4302 = _DeviceOmniAccess4302_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 2, 1, 1, 5)
)
if mibBuilder.loadTexts:
    deviceOmniAccess4302.setStatus("current")
_DeviceOmniAccess4504_ObjectIdentity = ObjectIdentity
deviceOmniAccess4504 = _DeviceOmniAccess4504_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 2, 1, 1, 6)
)
if mibBuilder.loadTexts:
    deviceOmniAccess4504.setStatus("current")
_DeviceOmniAccess4604_ObjectIdentity = ObjectIdentity
deviceOmniAccess4604 = _DeviceOmniAccess4604_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 2, 1, 1, 7)
)
if mibBuilder.loadTexts:
    deviceOmniAccess4604.setStatus("current")
_DeviceOmniAccess4704_ObjectIdentity = ObjectIdentity
deviceOmniAccess4704 = _DeviceOmniAccess4704_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 2, 1, 1, 8)
)
if mibBuilder.loadTexts:
    deviceOmniAccess4704.setStatus("current")
_DeviceOmniAccess4304_ObjectIdentity = ObjectIdentity
deviceOmniAccess4304 = _DeviceOmniAccess4304_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 2, 1, 1, 9)
)
if mibBuilder.loadTexts:
    deviceOmniAccess4304.setStatus("current")
_DeviceOmniAccess4306_ObjectIdentity = ObjectIdentity
deviceOmniAccess4306 = _DeviceOmniAccess4306_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 2, 1, 1, 10)
)
if mibBuilder.loadTexts:
    deviceOmniAccess4306.setStatus("current")
_DeviceOmniAccess4306G_ObjectIdentity = ObjectIdentity
deviceOmniAccess4306G = _DeviceOmniAccess4306G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 2, 1, 1, 11)
)
if mibBuilder.loadTexts:
    deviceOmniAccess4306G.setStatus("current")
_DeviceOmniAccess4306GW_ObjectIdentity = ObjectIdentity
deviceOmniAccess4306GW = _DeviceOmniAccess4306GW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 2, 1, 1, 12)
)
if mibBuilder.loadTexts:
    deviceOmniAccess4306GW.setStatus("current")
_ChassisOmniAccessWirelessAP_ObjectIdentity = ObjectIdentity
chassisOmniAccessWirelessAP = _ChassisOmniAccessWirelessAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    chassisOmniAccessWirelessAP.setStatus("current")
_DeviceOmniAccessAP60_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP60 = _DeviceOmniAccessAP60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP60.setStatus("current")
_DeviceOmniAccessAP61_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP61 = _DeviceOmniAccessAP61_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP61.setStatus("current")
_DeviceOmniAccessAP70_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP70 = _DeviceOmniAccessAP70_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP70.setStatus("current")
_DeviceOmniAccessAP80S_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP80S = _DeviceOmniAccessAP80S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 2, 1, 2, 4)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP80S.setStatus("current")
_DeviceOmniAccessAP80M_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP80M = _DeviceOmniAccessAP80M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 2, 1, 2, 5)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP80M.setStatus("current")
_DeviceOmniAccessAP65_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP65 = _DeviceOmniAccessAP65_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 2, 1, 2, 6)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP65.setStatus("current")
_DeviceOmniAccessAP40_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP40 = _DeviceOmniAccessAP40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 2, 1, 2, 7)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP40.setStatus("current")
_DeviceOmniAccessAP85_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP85 = _DeviceOmniAccessAP85_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 2, 1, 2, 8)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP85.setStatus("current")
_DeviceOmniAccessAP41_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP41 = _DeviceOmniAccessAP41_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 2, 1, 2, 9)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP41.setStatus("current")
_DeviceOmniAccessAP120_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP120 = _DeviceOmniAccessAP120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 2, 1, 2, 10)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP120.setStatus("current")
_DeviceOmniAccessAP121_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP121 = _DeviceOmniAccessAP121_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 2, 1, 2, 11)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP121.setStatus("current")
_DeviceOmniAccessAP124_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP124 = _DeviceOmniAccessAP124_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 2, 1, 2, 12)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP124.setStatus("current")
_DeviceOmniAccessAP125_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP125 = _DeviceOmniAccessAP125_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 2, 1, 2, 13)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP125.setStatus("current")
_DeviceOmniAccessAP120ABG_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP120ABG = _DeviceOmniAccessAP120ABG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 2, 1, 2, 14)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP120ABG.setStatus("current")
_DeviceOmniAccessAP121ABG_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP121ABG = _DeviceOmniAccessAP121ABG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 2, 1, 2, 15)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP121ABG.setStatus("current")
_DeviceOmniAccessAP124ABG_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP124ABG = _DeviceOmniAccessAP124ABG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 2, 1, 2, 16)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP124ABG.setStatus("current")
_DeviceOmniAccessAP125ABG_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP125ABG = _DeviceOmniAccessAP125ABG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 2, 1, 2, 17)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP125ABG.setStatus("current")
_FansOmniAccessWireless_ObjectIdentity = ObjectIdentity
fansOmniAccessWireless = _FansOmniAccessWireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 2, 2)
)
if mibBuilder.loadTexts:
    fansOmniAccessWireless.setStatus("current")
_PowersOmniAccessWireless_ObjectIdentity = ObjectIdentity
powersOmniAccessWireless = _PowersOmniAccessWireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 2, 3)
)
if mibBuilder.loadTexts:
    powersOmniAccessWireless.setStatus("current")
_ModulesOmniAccessWireless_ObjectIdentity = ObjectIdentity
modulesOmniAccessWireless = _ModulesOmniAccessWireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 2, 4)
)
if mibBuilder.loadTexts:
    modulesOmniAccessWireless.setStatus("current")
_FamilyOmniAccessWAN_ObjectIdentity = ObjectIdentity
familyOmniAccessWAN = _FamilyOmniAccessWAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    familyOmniAccessWAN.setStatus("current")
_ChassisOmniAccessWAN_ObjectIdentity = ObjectIdentity
chassisOmniAccessWAN = _ChassisOmniAccessWAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    chassisOmniAccessWAN.setStatus("current")
_DeviceOmniAccess604T1_ObjectIdentity = ObjectIdentity
deviceOmniAccess604T1 = _DeviceOmniAccess604T1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 3, 1, 20)
)
if mibBuilder.loadTexts:
    deviceOmniAccess604T1.setStatus("current")
_DeviceOmniAccess604E1_ObjectIdentity = ObjectIdentity
deviceOmniAccess604E1 = _DeviceOmniAccess604E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 3, 1, 21)
)
if mibBuilder.loadTexts:
    deviceOmniAccess604E1.setStatus("current")
_DeviceOmniAccess602T1_ObjectIdentity = ObjectIdentity
deviceOmniAccess602T1 = _DeviceOmniAccess602T1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 3, 1, 22)
)
if mibBuilder.loadTexts:
    deviceOmniAccess602T1.setStatus("current")
_DeviceOmniAccess602E1_ObjectIdentity = ObjectIdentity
deviceOmniAccess602E1 = _DeviceOmniAccess602E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 3, 1, 23)
)
if mibBuilder.loadTexts:
    deviceOmniAccess602E1.setStatus("current")
_DeviceOmniAccess601_ObjectIdentity = ObjectIdentity
deviceOmniAccess601 = _DeviceOmniAccess601_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 3, 1, 30)
)
if mibBuilder.loadTexts:
    deviceOmniAccess601.setStatus("current")
_DeviceOmniAccess601SBU_ObjectIdentity = ObjectIdentity
deviceOmniAccess601SBU = _DeviceOmniAccess601SBU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 3, 1, 31)
)
if mibBuilder.loadTexts:
    deviceOmniAccess601SBU.setStatus("current")
_DeviceOmniAccess625_ObjectIdentity = ObjectIdentity
deviceOmniAccess625 = _DeviceOmniAccess625_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 3, 1, 32)
)
if mibBuilder.loadTexts:
    deviceOmniAccess625.setStatus("current")
_DeviceOmniAccess601SBST_ObjectIdentity = ObjectIdentity
deviceOmniAccess601SBST = _DeviceOmniAccess601SBST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 3, 1, 33)
)
if mibBuilder.loadTexts:
    deviceOmniAccess601SBST.setStatus("current")
_DeviceOmniAccess601BU_ObjectIdentity = ObjectIdentity
deviceOmniAccess601BU = _DeviceOmniAccess601BU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 3, 1, 34)
)
if mibBuilder.loadTexts:
    deviceOmniAccess601BU.setStatus("current")
_DeviceOmniAccess601BST_ObjectIdentity = ObjectIdentity
deviceOmniAccess601BST = _DeviceOmniAccess601BST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 3, 1, 35)
)
if mibBuilder.loadTexts:
    deviceOmniAccess601BST.setStatus("current")
_FansOmniAccessWAN_ObjectIdentity = ObjectIdentity
fansOmniAccessWAN = _FansOmniAccessWAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 3, 2)
)
if mibBuilder.loadTexts:
    fansOmniAccessWAN.setStatus("current")
_PowersOmniAccessWAN_ObjectIdentity = ObjectIdentity
powersOmniAccessWAN = _PowersOmniAccessWAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 3, 3)
)
if mibBuilder.loadTexts:
    powersOmniAccessWAN.setStatus("current")
_ModulesOmniAccessWAN_ObjectIdentity = ObjectIdentity
modulesOmniAccessWAN = _ModulesOmniAccessWAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 3, 4)
)
if mibBuilder.loadTexts:
    modulesOmniAccessWAN.setStatus("current")
_Family6200_ObjectIdentity = ObjectIdentity
family6200 = _Family6200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 4)
)
if mibBuilder.loadTexts:
    family6200.setStatus("current")
_Chassis6200_ObjectIdentity = ObjectIdentity
chassis6200 = _Chassis6200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 4, 1)
)
if mibBuilder.loadTexts:
    chassis6200.setStatus("current")
_Device6224_ObjectIdentity = ObjectIdentity
device6224 = _Device6224_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    device6224.setStatus("current")
_Device6224P_ObjectIdentity = ObjectIdentity
device6224P = _Device6224P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 4, 1, 2)
)
if mibBuilder.loadTexts:
    device6224P.setStatus("current")
_Device6248_ObjectIdentity = ObjectIdentity
device6248 = _Device6248_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 4, 1, 3)
)
if mibBuilder.loadTexts:
    device6248.setStatus("current")
_Device6248P_ObjectIdentity = ObjectIdentity
device6248P = _Device6248P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 4, 1, 4)
)
if mibBuilder.loadTexts:
    device6248P.setStatus("current")
_Device6224U_ObjectIdentity = ObjectIdentity
device6224U = _Device6224U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 4, 1, 5)
)
if mibBuilder.loadTexts:
    device6224U.setStatus("current")
_Device6212_ObjectIdentity = ObjectIdentity
device6212 = _Device6212_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 4, 1, 6)
)
if mibBuilder.loadTexts:
    device6212.setStatus("current")
_Device6212P_ObjectIdentity = ObjectIdentity
device6212P = _Device6212P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 4, 1, 7)
)
if mibBuilder.loadTexts:
    device6212P.setStatus("current")
_Fans6200_ObjectIdentity = ObjectIdentity
fans6200 = _Fans6200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 4, 2)
)
if mibBuilder.loadTexts:
    fans6200.setStatus("current")
_Powers6200_ObjectIdentity = ObjectIdentity
powers6200 = _Powers6200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 4, 3)
)
if mibBuilder.loadTexts:
    powers6200.setStatus("current")
_Modules6200_ObjectIdentity = ObjectIdentity
modules6200 = _Modules6200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 4, 4)
)
if mibBuilder.loadTexts:
    modules6200.setStatus("current")
_FamilyOAG_ObjectIdentity = ObjectIdentity
familyOAG = _FamilyOAG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 5)
)
if mibBuilder.loadTexts:
    familyOAG.setStatus("current")
_ChassisOAG_ObjectIdentity = ObjectIdentity
chassisOAG = _ChassisOAG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 5, 1)
)
if mibBuilder.loadTexts:
    chassisOAG.setStatus("current")
_DeviceOAG1000_ObjectIdentity = ObjectIdentity
deviceOAG1000 = _DeviceOAG1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 5, 1, 1)
)
if mibBuilder.loadTexts:
    deviceOAG1000.setStatus("current")
_DeviceOAG2400_ObjectIdentity = ObjectIdentity
deviceOAG2400 = _DeviceOAG2400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 5, 1, 2)
)
if mibBuilder.loadTexts:
    deviceOAG2400.setStatus("current")
_FansOAG_ObjectIdentity = ObjectIdentity
fansOAG = _FansOAG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 5, 2)
)
if mibBuilder.loadTexts:
    fansOAG.setStatus("current")
_PowersOAG_ObjectIdentity = ObjectIdentity
powersOAG = _PowersOAG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 5, 3)
)
if mibBuilder.loadTexts:
    powersOAG.setStatus("current")
_ModulesOAG_ObjectIdentity = ObjectIdentity
modulesOAG = _ModulesOAG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 5, 4)
)
if mibBuilder.loadTexts:
    modulesOAG.setStatus("current")
_FamilyOA7XX_ObjectIdentity = ObjectIdentity
familyOA7XX = _FamilyOA7XX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 6)
)
if mibBuilder.loadTexts:
    familyOA7XX.setStatus("current")
_ChassisOA7XX_ObjectIdentity = ObjectIdentity
chassisOA7XX = _ChassisOA7XX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 6, 1)
)
if mibBuilder.loadTexts:
    chassisOA7XX.setStatus("current")
_DeviceOA740_ObjectIdentity = ObjectIdentity
deviceOA740 = _DeviceOA740_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 6, 1, 1)
)
if mibBuilder.loadTexts:
    deviceOA740.setStatus("current")
_DeviceOA780_ObjectIdentity = ObjectIdentity
deviceOA780 = _DeviceOA780_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 6, 1, 2)
)
if mibBuilder.loadTexts:
    deviceOA780.setStatus("current")
_FansOA7XX_ObjectIdentity = ObjectIdentity
fansOA7XX = _FansOA7XX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 6, 2)
)
if mibBuilder.loadTexts:
    fansOA7XX.setStatus("current")
_PowersOA7XX_ObjectIdentity = ObjectIdentity
powersOA7XX = _PowersOA7XX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 6, 3)
)
if mibBuilder.loadTexts:
    powersOA7XX.setStatus("current")
_ModulesOA7XX_ObjectIdentity = ObjectIdentity
modulesOA7XX = _ModulesOA7XX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 2, 6, 4)
)
if mibBuilder.loadTexts:
    modulesOA7XX.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-TP-DEVICES",
    **{"alcatelIND1TpDevicesMIB": alcatelIND1TpDevicesMIB,
       "familyOmniAccess4000": familyOmniAccess4000,
       "chassisOmniAccess4000": chassisOmniAccess4000,
       "deviceOmniAccess4012": deviceOmniAccess4012,
       "deviceOmniAccess4024": deviceOmniAccess4024,
       "deviceOmniAccess4102": deviceOmniAccess4102,
       "fansOmniAccess4000": fansOmniAccess4000,
       "powersOmniAccess4000": powersOmniAccess4000,
       "modulesOmniAccess4000": modulesOmniAccess4000,
       "familyOmniAccessWireless": familyOmniAccessWireless,
       "chassisOmniAccessWireless": chassisOmniAccessWireless,
       "chassisOmniAccessWirelessSwitch": chassisOmniAccessWirelessSwitch,
       "deviceOmniAccess5000": deviceOmniAccess5000,
       "deviceOmniAccess4324": deviceOmniAccess4324,
       "deviceOmniAccess4308": deviceOmniAccess4308,
       "deviceOmniAccess6000": deviceOmniAccess6000,
       "chassisOmniAccess6000Wireless": chassisOmniAccess6000Wireless,
       "deviceOmniAccess6000PS2": deviceOmniAccess6000PS2,
       "fansOmniAccess6000Wireless": fansOmniAccess6000Wireless,
       "powersOmniAccess6000Wireless": powersOmniAccess6000Wireless,
       "modulesOmniAccess6000Wireless": modulesOmniAccess6000Wireless,
       "deviceOmniAccess6000SCI48": deviceOmniAccess6000SCI48,
       "deviceOmniAccess6000SCII256": deviceOmniAccess6000SCII256,
       "deviceOmniAccess6000LC2G": deviceOmniAccess6000LC2G,
       "deviceOmniAccess6000LC2G24F": deviceOmniAccess6000LC2G24F,
       "deviceOmniAccess6000LC2G24FP": deviceOmniAccess6000LC2G24FP,
       "deviceOmniAccess6000S3C20G": deviceOmniAccess6000S3C20G,
       "deviceOmniAccess4302": deviceOmniAccess4302,
       "deviceOmniAccess4504": deviceOmniAccess4504,
       "deviceOmniAccess4604": deviceOmniAccess4604,
       "deviceOmniAccess4704": deviceOmniAccess4704,
       "deviceOmniAccess4304": deviceOmniAccess4304,
       "deviceOmniAccess4306": deviceOmniAccess4306,
       "deviceOmniAccess4306G": deviceOmniAccess4306G,
       "deviceOmniAccess4306GW": deviceOmniAccess4306GW,
       "chassisOmniAccessWirelessAP": chassisOmniAccessWirelessAP,
       "deviceOmniAccessAP60": deviceOmniAccessAP60,
       "deviceOmniAccessAP61": deviceOmniAccessAP61,
       "deviceOmniAccessAP70": deviceOmniAccessAP70,
       "deviceOmniAccessAP80S": deviceOmniAccessAP80S,
       "deviceOmniAccessAP80M": deviceOmniAccessAP80M,
       "deviceOmniAccessAP65": deviceOmniAccessAP65,
       "deviceOmniAccessAP40": deviceOmniAccessAP40,
       "deviceOmniAccessAP85": deviceOmniAccessAP85,
       "deviceOmniAccessAP41": deviceOmniAccessAP41,
       "deviceOmniAccessAP120": deviceOmniAccessAP120,
       "deviceOmniAccessAP121": deviceOmniAccessAP121,
       "deviceOmniAccessAP124": deviceOmniAccessAP124,
       "deviceOmniAccessAP125": deviceOmniAccessAP125,
       "deviceOmniAccessAP120ABG": deviceOmniAccessAP120ABG,
       "deviceOmniAccessAP121ABG": deviceOmniAccessAP121ABG,
       "deviceOmniAccessAP124ABG": deviceOmniAccessAP124ABG,
       "deviceOmniAccessAP125ABG": deviceOmniAccessAP125ABG,
       "fansOmniAccessWireless": fansOmniAccessWireless,
       "powersOmniAccessWireless": powersOmniAccessWireless,
       "modulesOmniAccessWireless": modulesOmniAccessWireless,
       "familyOmniAccessWAN": familyOmniAccessWAN,
       "chassisOmniAccessWAN": chassisOmniAccessWAN,
       "deviceOmniAccess604T1": deviceOmniAccess604T1,
       "deviceOmniAccess604E1": deviceOmniAccess604E1,
       "deviceOmniAccess602T1": deviceOmniAccess602T1,
       "deviceOmniAccess602E1": deviceOmniAccess602E1,
       "deviceOmniAccess601": deviceOmniAccess601,
       "deviceOmniAccess601SBU": deviceOmniAccess601SBU,
       "deviceOmniAccess625": deviceOmniAccess625,
       "deviceOmniAccess601SBST": deviceOmniAccess601SBST,
       "deviceOmniAccess601BU": deviceOmniAccess601BU,
       "deviceOmniAccess601BST": deviceOmniAccess601BST,
       "fansOmniAccessWAN": fansOmniAccessWAN,
       "powersOmniAccessWAN": powersOmniAccessWAN,
       "modulesOmniAccessWAN": modulesOmniAccessWAN,
       "family6200": family6200,
       "chassis6200": chassis6200,
       "device6224": device6224,
       "device6224P": device6224P,
       "device6248": device6248,
       "device6248P": device6248P,
       "device6224U": device6224U,
       "device6212": device6212,
       "device6212P": device6212P,
       "fans6200": fans6200,
       "powers6200": powers6200,
       "modules6200": modules6200,
       "familyOAG": familyOAG,
       "chassisOAG": chassisOAG,
       "deviceOAG1000": deviceOAG1000,
       "deviceOAG2400": deviceOAG2400,
       "fansOAG": fansOAG,
       "powersOAG": powersOAG,
       "modulesOAG": modulesOAG,
       "familyOA7XX": familyOA7XX,
       "chassisOA7XX": chassisOA7XX,
       "deviceOA740": deviceOA740,
       "deviceOA780": deviceOA780,
       "fansOA7XX": fansOA7XX,
       "powersOA7XX": powersOA7XX,
       "modulesOA7XX": modulesOA7XX}
)
