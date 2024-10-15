# SNMP MIB module (SA-HARDWARE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SA-HARDWARE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:14 2024
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

saHardware = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 78, 4)
)
saHardware.setRevisions(
        ("2015-05-11 00:00",
         "2015-04-13 00:00",
         "2015-04-03 00:00",
         "2015-01-14 00:00",
         "1901-12-15 00:00",
         "2014-11-20 00:00",
         "2014-07-31 00:00",
         "1904-06-14 00:00",
         "1914-02-11 00:00",
         "2014-01-13 00:00",
         "2014-01-10 00:00",
         "1913-10-17 00:00",
         "1913-07-04 00:00",
         "1913-06-07 00:00",
         "1913-05-30 00:00",
         "1913-02-06 00:00",
         "1912-12-05 00:00",
         "1912-11-28 00:00",
         "1912-11-07 00:00",
         "1912-08-23 00:00",
         "1912-05-08 00:00",
         "1912-04-10 00:00",
         "1911-09-02 00:00",
         "1911-08-19 00:00",
         "1911-06-13 00:00",
         "1910-11-16 00:00",
         "1910-10-26 00:00",
         "1910-10-18 00:00",
         "1910-04-27 00:00",
         "1910-04-07 00:00",
         "1909-11-05 00:00",
         "1909-10-05 00:00",
         "1908-01-17 00:00",
         "1907-09-20 00:00",
         "1907-07-16 00:00",
         "1906-09-11 00:00",
         "1906-08-07 00:00",
         "1905-12-02 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sa_ObjectIdentity = ObjectIdentity
sa = _Sa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429)
)
_SaVoip_ObjectIdentity = ObjectIdentity
saVoip = _SaVoip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 78)
)
_SaHwDescr_ObjectIdentity = ObjectIdentity
saHwDescr = _SaHwDescr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 78, 4, 1)
)
_SaHwDescrModel_Type = SnmpAdminString
_SaHwDescrModel_Object = MibScalar
saHwDescrModel = _SaHwDescrModel_Object(
    (1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 1),
    _SaHwDescrModel_Type()
)
saHwDescrModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saHwDescrModel.setStatus("current")
_SaHwDescrHardwareVersion_Type = SnmpAdminString
_SaHwDescrHardwareVersion_Object = MibScalar
saHwDescrHardwareVersion = _SaHwDescrHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 2),
    _SaHwDescrHardwareVersion_Type()
)
saHwDescrHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saHwDescrHardwareVersion.setStatus("current")
_SaHwDescrSerialNumber_Type = SnmpAdminString
_SaHwDescrSerialNumber_Object = MibScalar
saHwDescrSerialNumber = _SaHwDescrSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 3),
    _SaHwDescrSerialNumber_Type()
)
saHwDescrSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saHwDescrSerialNumber.setStatus("current")
_SaHwDescrCmMacAddress_Type = SnmpAdminString
_SaHwDescrCmMacAddress_Object = MibScalar
saHwDescrCmMacAddress = _SaHwDescrCmMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 4),
    _SaHwDescrCmMacAddress_Type()
)
saHwDescrCmMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saHwDescrCmMacAddress.setStatus("current")
_SaHwDescrManufactureDate_Type = SnmpAdminString
_SaHwDescrManufactureDate_Object = MibScalar
saHwDescrManufactureDate = _SaHwDescrManufactureDate_Object(
    (1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 5),
    _SaHwDescrManufactureDate_Type()
)
saHwDescrManufactureDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saHwDescrManufactureDate.setStatus("current")


class _SaHwDescrPowerSupply_Type(Integer32):
    """Custom type saHwDescrPowerSupply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal-switching", 1))
    )


_SaHwDescrPowerSupply_Type.__name__ = "Integer32"
_SaHwDescrPowerSupply_Object = MibScalar
saHwDescrPowerSupply = _SaHwDescrPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 6),
    _SaHwDescrPowerSupply_Type()
)
saHwDescrPowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saHwDescrPowerSupply.setStatus("current")


class _SaHwDescrDiplexer_Type(Integer32):
    """Custom type saHwDescrDiplexer based on Integer32"""
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
        *(("europe-5-65", 2),
          ("europe-5-85", 6),
          ("japan", 3),
          ("korea", 4),
          ("none", 0),
          ("north-america-5-42", 1),
          ("north-america-85-108", 5))
    )


_SaHwDescrDiplexer_Type.__name__ = "Integer32"
_SaHwDescrDiplexer_Object = MibScalar
saHwDescrDiplexer = _SaHwDescrDiplexer_Object(
    (1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 7),
    _SaHwDescrDiplexer_Type()
)
saHwDescrDiplexer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saHwDescrDiplexer.setStatus("current")


class _SaHwDescrMainProcessor_Type(Integer32):
    """Custom type saHwDescrMainProcessor based on Integer32"""
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
              23,
              24,
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("bcm3349", 1),
          ("bcm3349ipbg", 6),
          ("bcm3349kfb", 2),
          ("bcm3361", 8),
          ("bcm3368", 3),
          ("bcm3371", 13),
          ("bcm3378", 9),
          ("bcm3379", 14),
          ("bcm3380", 10),
          ("bcm3381A1", 4),
          ("bcm3381A2", 5),
          ("bcm3382", 12),
          ("bcm3383", 15),
          ("bcm3384", 21),
          ("bcm33843E", 22),
          ("bcm33843Z", 18),
          ("bcm3384ZU", 26),
          ("bcm3385", 23),
          ("puma6", 16),
          ("puma6-B2", 19),
          ("puma6-D", 24),
          ("puma6MG", 17),
          ("puma6MG-B2", 20),
          ("puma6MG-D", 25),
          ("tipuma5", 7),
          ("tipuma5Tc4800", 11))
    )


_SaHwDescrMainProcessor_Type.__name__ = "Integer32"
_SaHwDescrMainProcessor_Object = MibScalar
saHwDescrMainProcessor = _SaHwDescrMainProcessor_Object(
    (1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 8),
    _SaHwDescrMainProcessor_Type()
)
saHwDescrMainProcessor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saHwDescrMainProcessor.setStatus("current")


class _SaHwDescrTuner_Type(Integer32):
    """Custom type saHwDescrTuner based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("bcm3419", 1),
          ("bcm3420", 2),
          ("bcm3420iml", 4),
          ("bcm3420x3", 3),
          ("bcm3421", 6),
          ("bcmInternal", 7),
          ("mt2170", 5),
          ("mxl265", 8),
          ("mxl265d", 11),
          ("mxl265v2", 9),
          ("mxl267", 10),
          ("mxl267d", 12),
          ("none", 0))
    )


_SaHwDescrTuner_Type.__name__ = "Integer32"
_SaHwDescrTuner_Object = MibScalar
saHwDescrTuner = _SaHwDescrTuner_Object(
    (1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 9),
    _SaHwDescrTuner_Type()
)
saHwDescrTuner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saHwDescrTuner.setStatus("current")


class _SaHwDescrSlic_Type(Integer32):
    """Custom type saHwDescrSlic based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("le88276", 5),
          ("le9500b", 1),
          ("le9500c", 2),
          ("le9500d", 3),
          ("le9500s", 7),
          ("le9520ddtc", 4),
          ("le9520s", 8),
          ("le9530d", 6),
          ("le9531d", 10),
          ("le9540d", 9),
          ("le9541d", 12),
          ("le9652", 13),
          ("none", 0),
          ("zl88702", 11))
    )


_SaHwDescrSlic_Type.__name__ = "Integer32"
_SaHwDescrSlic_Object = MibScalar
saHwDescrSlic = _SaHwDescrSlic_Object(
    (1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 10),
    _SaHwDescrSlic_Type()
)
saHwDescrSlic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saHwDescrSlic.setStatus("current")
_SaHwDescrMemoryMain_Type = Integer32
_SaHwDescrMemoryMain_Object = MibScalar
saHwDescrMemoryMain = _SaHwDescrMemoryMain_Object(
    (1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 11),
    _SaHwDescrMemoryMain_Type()
)
saHwDescrMemoryMain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saHwDescrMemoryMain.setStatus("current")
if mibBuilder.loadTexts:
    saHwDescrMemoryMain.setUnits("Megabytes")
_SaHwDescrMemoryFlash_Type = Integer32
_SaHwDescrMemoryFlash_Object = MibScalar
saHwDescrMemoryFlash = _SaHwDescrMemoryFlash_Object(
    (1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 12),
    _SaHwDescrMemoryFlash_Type()
)
saHwDescrMemoryFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saHwDescrMemoryFlash.setStatus("current")
if mibBuilder.loadTexts:
    saHwDescrMemoryFlash.setUnits("Megabytes")


class _SaHwDescrWirelessType_Type(Integer32):
    """Custom type saHwDescrWirelessType based on Integer32"""
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
        *(("ieee80211ac", 4),
          ("ieee80211b", 1),
          ("ieee80211g", 2),
          ("ieee80211n", 3),
          ("ieee80211n-ieee80211ac", 5),
          ("none", 0))
    )


_SaHwDescrWirelessType_Type.__name__ = "Integer32"
_SaHwDescrWirelessType_Object = MibScalar
saHwDescrWirelessType = _SaHwDescrWirelessType_Object(
    (1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 13),
    _SaHwDescrWirelessType_Type()
)
saHwDescrWirelessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saHwDescrWirelessType.setStatus("current")


class _SaHwDescrWirelessChip_Type(Integer32):
    """Custom type saHwDescrWirelessChip based on Integer32"""
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
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33)
        )
    )
    namedValues = NamedValues(
        *(("ath9380", 11),
          ("ath9381sp-ath9580sp", 13),
          ("ath9381sp-qca9880", 31),
          ("ath9580", 12),
          ("bcm4306", 1),
          ("bcm4313", 7),
          ("bcm4318", 2),
          ("bcm4318E", 3),
          ("bcm43217", 8),
          ("bcm43217-bcm4360hp", 22),
          ("bcm43217hp", 20),
          ("bcm43217hp-bcm4331sp", 23),
          ("bcm43217hp-bcm4360sp", 24),
          ("bcm43217sp-bcm43228sp", 10),
          ("bcm43217sp-bcm4331sp", 16),
          ("bcm43217sp-bcm4360sp", 18),
          ("bcm4322", 4),
          ("bcm43224-dualBand", 5),
          ("bcm43225-singleBand", 6),
          ("bcm43228", 9),
          ("bcm43228hp", 21),
          ("bcm43228hp-5ghz", 32),
          ("bcm43228sp-5ghz", 14),
          ("bcm4331hp-bcm43217sp", 25),
          ("bcm4331hp-bcm43228sp", 26),
          ("bcm4331hp-bcm4331hp", 28),
          ("bcm4331hp-bcm4331sp", 27),
          ("bcm4331hp-bcm4360hp", 30),
          ("bcm4331hp-bcm4360sp", 29),
          ("bcm4331sp", 15),
          ("bcm4331sp-bcm4331sp", 17),
          ("bcm4331sp-bcm4360hp", 19),
          ("clr240-cl2330", 33),
          ("none", 0))
    )


_SaHwDescrWirelessChip_Type.__name__ = "Integer32"
_SaHwDescrWirelessChip_Object = MibScalar
saHwDescrWirelessChip = _SaHwDescrWirelessChip_Object(
    (1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 14),
    _SaHwDescrWirelessChip_Type()
)
saHwDescrWirelessChip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saHwDescrWirelessChip.setStatus("current")


class _SaHwDescrDectType_Type(Integer32):
    """Custom type saHwDescrDectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("europe", 2),
          ("none", 0),
          ("north-america", 1))
    )


_SaHwDescrDectType_Type.__name__ = "Integer32"
_SaHwDescrDectType_Object = MibScalar
saHwDescrDectType = _SaHwDescrDectType_Object(
    (1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 15),
    _SaHwDescrDectType_Type()
)
saHwDescrDectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saHwDescrDectType.setStatus("current")


class _SaHwDescrUsbType_Type(Integer32):
    """Custom type saHwDescrUsbType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("usb11", 1),
          ("usb203380G", 5),
          ("usb20w3381", 3),
          ("usb20wPLX", 2),
          ("usb20wPuma5", 4),
          ("usb20wPuma6", 6),
          ("usb20wPuma6MG", 7),
          ("usb30wBCM", 8))
    )


_SaHwDescrUsbType_Type.__name__ = "Integer32"
_SaHwDescrUsbType_Object = MibScalar
saHwDescrUsbType = _SaHwDescrUsbType_Object(
    (1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 16),
    _SaHwDescrUsbType_Type()
)
saHwDescrUsbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saHwDescrUsbType.setStatus("current")
_SaHwDescrFactoryId_Type = Integer32
_SaHwDescrFactoryId_Object = MibScalar
saHwDescrFactoryId = _SaHwDescrFactoryId_Object(
    (1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 17),
    _SaHwDescrFactoryId_Type()
)
saHwDescrFactoryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saHwDescrFactoryId.setStatus("current")


class _SaHwDescrDmsType_Type(Integer32):
    """Custom type saHwDescrDmsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dms1", 1),
          ("none", 0))
    )


_SaHwDescrDmsType_Type.__name__ = "Integer32"
_SaHwDescrDmsType_Object = MibScalar
saHwDescrDmsType = _SaHwDescrDmsType_Object(
    (1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 18),
    _SaHwDescrDmsType_Type()
)
saHwDescrDmsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saHwDescrDmsType.setStatus("current")


class _SaHwDescrMocaType_Type(Integer32):
    """Custom type saHwDescrMocaType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("ad9965", 6),
          ("bcm6803", 5),
          ("en2210", 1),
          ("en2510", 2),
          ("en2710", 3),
          ("en2810", 8),
          ("moca20wBCM", 7),
          ("none", 0),
          ("vxc1030", 4))
    )


_SaHwDescrMocaType_Type.__name__ = "Integer32"
_SaHwDescrMocaType_Object = MibScalar
saHwDescrMocaType = _SaHwDescrMocaType_Object(
    (1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 19),
    _SaHwDescrMocaType_Type()
)
saHwDescrMocaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saHwDescrMocaType.setStatus("current")


class _SaHwDescrEthSwitch_Type(Integer32):
    """Custom type saHwDescrEthSwitch based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("ar8316", 5),
          ("bcm53101e", 6),
          ("bcm53115s", 4),
          ("bcm53124s", 7),
          ("bcm5325e", 3),
          ("bcm5325m", 1),
          ("internalBCM", 9),
          ("marv6095f", 2),
          ("marv6172", 8),
          ("none", 0))
    )


_SaHwDescrEthSwitch_Type.__name__ = "Integer32"
_SaHwDescrEthSwitch_Object = MibScalar
saHwDescrEthSwitch = _SaHwDescrEthSwitch_Object(
    (1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 20),
    _SaHwDescrEthSwitch_Type()
)
saHwDescrEthSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saHwDescrEthSwitch.setStatus("current")
_SaHwDescrIntCount_ObjectIdentity = ObjectIdentity
saHwDescrIntCount = _SaHwDescrIntCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 101)
)
_SaHwDescrIntCountEthernet_Type = Integer32
_SaHwDescrIntCountEthernet_Object = MibScalar
saHwDescrIntCountEthernet = _SaHwDescrIntCountEthernet_Object(
    (1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 101, 1),
    _SaHwDescrIntCountEthernet_Type()
)
saHwDescrIntCountEthernet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saHwDescrIntCountEthernet.setStatus("current")
_SaHwDescrIntCountUsb_Type = Integer32
_SaHwDescrIntCountUsb_Object = MibScalar
saHwDescrIntCountUsb = _SaHwDescrIntCountUsb_Object(
    (1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 101, 2),
    _SaHwDescrIntCountUsb_Type()
)
saHwDescrIntCountUsb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saHwDescrIntCountUsb.setStatus("current")
_SaHwDescrIntCountPhoneLine_Type = Integer32
_SaHwDescrIntCountPhoneLine_Object = MibScalar
saHwDescrIntCountPhoneLine = _SaHwDescrIntCountPhoneLine_Object(
    (1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 101, 3),
    _SaHwDescrIntCountPhoneLine_Type()
)
saHwDescrIntCountPhoneLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saHwDescrIntCountPhoneLine.setStatus("current")
_SaHwDescrIntCountMaxBattery_Type = Integer32
_SaHwDescrIntCountMaxBattery_Object = MibScalar
saHwDescrIntCountMaxBattery = _SaHwDescrIntCountMaxBattery_Object(
    (1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 101, 4),
    _SaHwDescrIntCountMaxBattery_Type()
)
saHwDescrIntCountMaxBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saHwDescrIntCountMaxBattery.setStatus("current")
_SaHwDescrIntCountWireless_Type = Integer32
_SaHwDescrIntCountWireless_Object = MibScalar
saHwDescrIntCountWireless = _SaHwDescrIntCountWireless_Object(
    (1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 101, 5),
    _SaHwDescrIntCountWireless_Type()
)
saHwDescrIntCountWireless.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saHwDescrIntCountWireless.setStatus("current")
_SaHwDescrIntCountDect_Type = Integer32
_SaHwDescrIntCountDect_Object = MibScalar
saHwDescrIntCountDect = _SaHwDescrIntCountDect_Object(
    (1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 101, 6),
    _SaHwDescrIntCountDect_Type()
)
saHwDescrIntCountDect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saHwDescrIntCountDect.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SA-HARDWARE-MIB",
    **{"sa": sa,
       "saVoip": saVoip,
       "saHardware": saHardware,
       "saHwDescr": saHwDescr,
       "saHwDescrModel": saHwDescrModel,
       "saHwDescrHardwareVersion": saHwDescrHardwareVersion,
       "saHwDescrSerialNumber": saHwDescrSerialNumber,
       "saHwDescrCmMacAddress": saHwDescrCmMacAddress,
       "saHwDescrManufactureDate": saHwDescrManufactureDate,
       "saHwDescrPowerSupply": saHwDescrPowerSupply,
       "saHwDescrDiplexer": saHwDescrDiplexer,
       "saHwDescrMainProcessor": saHwDescrMainProcessor,
       "saHwDescrTuner": saHwDescrTuner,
       "saHwDescrSlic": saHwDescrSlic,
       "saHwDescrMemoryMain": saHwDescrMemoryMain,
       "saHwDescrMemoryFlash": saHwDescrMemoryFlash,
       "saHwDescrWirelessType": saHwDescrWirelessType,
       "saHwDescrWirelessChip": saHwDescrWirelessChip,
       "saHwDescrDectType": saHwDescrDectType,
       "saHwDescrUsbType": saHwDescrUsbType,
       "saHwDescrFactoryId": saHwDescrFactoryId,
       "saHwDescrDmsType": saHwDescrDmsType,
       "saHwDescrMocaType": saHwDescrMocaType,
       "saHwDescrEthSwitch": saHwDescrEthSwitch,
       "saHwDescrIntCount": saHwDescrIntCount,
       "saHwDescrIntCountEthernet": saHwDescrIntCountEthernet,
       "saHwDescrIntCountUsb": saHwDescrIntCountUsb,
       "saHwDescrIntCountPhoneLine": saHwDescrIntCountPhoneLine,
       "saHwDescrIntCountMaxBattery": saHwDescrIntCountMaxBattery,
       "saHwDescrIntCountWireless": saHwDescrIntCountWireless,
       "saHwDescrIntCountDect": saHwDescrIntCountDect}
)
