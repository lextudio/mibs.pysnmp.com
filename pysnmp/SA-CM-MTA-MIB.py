# SNMP MIB module (SA-CM-MTA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SA-CM-MTA-MIB
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

saCmMta = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 78, 1)
)
saCmMta.setRevisions(
        ("2016-12-23 00:00",)
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


class _SaCmMtaDevice_Type(Integer32):
    """Custom type saCmMtaDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SaCmMtaDevice_Type.__name__ = "Integer32"
_SaCmMtaDevice_Object = MibScalar
saCmMtaDevice = _SaCmMtaDevice_Object(
    (1, 3, 6, 1, 4, 1, 1429, 78, 1, 1),
    _SaCmMtaDevice_Type()
)
saCmMtaDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saCmMtaDevice.setStatus("current")


class _SaCmMtaIpFilters_Type(Integer32):
    """Custom type saCmMtaIpFilters based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("openMta", 1),
          ("perSpec", 0))
    )


_SaCmMtaIpFilters_Type.__name__ = "Integer32"
_SaCmMtaIpFilters_Object = MibScalar
saCmMtaIpFilters = _SaCmMtaIpFilters_Object(
    (1, 3, 6, 1, 4, 1, 1429, 78, 1, 3),
    _SaCmMtaIpFilters_Type()
)
saCmMtaIpFilters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saCmMtaIpFilters.setStatus("current")


class _SaCmMtaSidCount_Type(Integer32):
    """Custom type saCmMtaSidCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(16, 16),
    )


_SaCmMtaSidCount_Type.__name__ = "Integer32"
_SaCmMtaSidCount_Object = MibScalar
saCmMtaSidCount = _SaCmMtaSidCount_Object(
    (1, 3, 6, 1, 4, 1, 1429, 78, 1, 5),
    _SaCmMtaSidCount_Type()
)
saCmMtaSidCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saCmMtaSidCount.setStatus("current")


class _SaCmMtaProvisioningMode_Type(Integer32):
    """Custom type saCmMtaProvisioningMode based on Integer32"""
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
              6)
        )
    )
    namedValues = NamedValues(
        *(("oneConfigFile", 1),
          ("packetCable", 0),
          ("twoConfigFilesDHCP", 2),
          ("twoConfigFilesDHCPmacAddress", 4),
          ("twoConfigFilesMacAddressOnly", 5),
          ("twoConfigFilesSNMP", 3),
          ("webPage", 6))
    )


_SaCmMtaProvisioningMode_Type.__name__ = "Integer32"
_SaCmMtaProvisioningMode_Object = MibScalar
saCmMtaProvisioningMode = _SaCmMtaProvisioningMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 78, 1, 7),
    _SaCmMtaProvisioningMode_Type()
)
saCmMtaProvisioningMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saCmMtaProvisioningMode.setStatus("current")


class _SaCmMtaDhcpPktcOption_Type(Integer32):
    """Custom type saCmMtaDhcpPktcOption based on Integer32"""
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
        *(("require122", 0),
          ("require177", 2),
          ("requireNone", 1))
    )


_SaCmMtaDhcpPktcOption_Type.__name__ = "Integer32"
_SaCmMtaDhcpPktcOption_Object = MibScalar
saCmMtaDhcpPktcOption = _SaCmMtaDhcpPktcOption_Object(
    (1, 3, 6, 1, 4, 1, 1429, 78, 1, 8),
    _SaCmMtaDhcpPktcOption_Type()
)
saCmMtaDhcpPktcOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saCmMtaDhcpPktcOption.setStatus("current")


class _SaCmMtaRequireTod_Type(Integer32):
    """Custom type saCmMtaRequireTod based on Integer32"""
    defaultValue = 1

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


_SaCmMtaRequireTod_Type.__name__ = "Integer32"
_SaCmMtaRequireTod_Object = MibScalar
saCmMtaRequireTod = _SaCmMtaRequireTod_Object(
    (1, 3, 6, 1, 4, 1, 1429, 78, 1, 10),
    _SaCmMtaRequireTod_Type()
)
saCmMtaRequireTod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saCmMtaRequireTod.setStatus("current")


class _SaCmMtaDecryptMtaConfigFile_Type(Integer32):
    """Custom type saCmMtaDecryptMtaConfigFile based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("RSA-CM-cert", 2),
          ("disable", 1))
    )


_SaCmMtaDecryptMtaConfigFile_Type.__name__ = "Integer32"
_SaCmMtaDecryptMtaConfigFile_Object = MibScalar
saCmMtaDecryptMtaConfigFile = _SaCmMtaDecryptMtaConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 1429, 78, 1, 13),
    _SaCmMtaDecryptMtaConfigFile_Type()
)
saCmMtaDecryptMtaConfigFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saCmMtaDecryptMtaConfigFile.setStatus("current")


class _SaCmMtaSwUpgradeControlTimer_Type(Integer32):
    """Custom type saCmMtaSwUpgradeControlTimer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7200),
    )


_SaCmMtaSwUpgradeControlTimer_Type.__name__ = "Integer32"
_SaCmMtaSwUpgradeControlTimer_Object = MibScalar
saCmMtaSwUpgradeControlTimer = _SaCmMtaSwUpgradeControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 1429, 78, 1, 14),
    _SaCmMtaSwUpgradeControlTimer_Type()
)
saCmMtaSwUpgradeControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saCmMtaSwUpgradeControlTimer.setStatus("current")
if mibBuilder.loadTexts:
    saCmMtaSwUpgradeControlTimer.setUnits("seconds")


class _SaCmMtaDhcpOptionSixty_Type(SnmpAdminString):
    """Custom type saCmMtaDhcpOptionSixty based on SnmpAdminString"""
    defaultValue = OctetString("pktc1.0")


_SaCmMtaDhcpOptionSixty_Object = MibScalar
saCmMtaDhcpOptionSixty = _SaCmMtaDhcpOptionSixty_Object(
    (1, 3, 6, 1, 4, 1, 1429, 78, 1, 20),
    _SaCmMtaDhcpOptionSixty_Type()
)
saCmMtaDhcpOptionSixty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saCmMtaDhcpOptionSixty.setStatus("current")


class _SaCmMtaProvSnmpSetCommunityString_Type(SnmpAdminString):
    """Custom type saCmMtaProvSnmpSetCommunityString based on SnmpAdminString"""
    defaultValue = OctetString("public")


_SaCmMtaProvSnmpSetCommunityString_Object = MibScalar
saCmMtaProvSnmpSetCommunityString = _SaCmMtaProvSnmpSetCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 1429, 78, 1, 26),
    _SaCmMtaProvSnmpSetCommunityString_Type()
)
saCmMtaProvSnmpSetCommunityString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saCmMtaProvSnmpSetCommunityString.setStatus("current")
_SaCmMtaCliAccess_ObjectIdentity = ObjectIdentity
saCmMtaCliAccess = _SaCmMtaCliAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 78, 1, 1001)
)


class _SaCmMtaCliAccessPasswordType_Type(Integer32):
    """Custom type saCmMtaCliAccessPasswordType based on Integer32"""
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
        *(("md5", 1),
          ("plain", 0),
          ("pod", 2))
    )


_SaCmMtaCliAccessPasswordType_Type.__name__ = "Integer32"
_SaCmMtaCliAccessPasswordType_Object = MibScalar
saCmMtaCliAccessPasswordType = _SaCmMtaCliAccessPasswordType_Object(
    (1, 3, 6, 1, 4, 1, 1429, 78, 1, 1001, 5),
    _SaCmMtaCliAccessPasswordType_Type()
)
saCmMtaCliAccessPasswordType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saCmMtaCliAccessPasswordType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SA-CM-MTA-MIB",
    **{"sa": sa,
       "saVoip": saVoip,
       "saCmMta": saCmMta,
       "saCmMtaDevice": saCmMtaDevice,
       "saCmMtaIpFilters": saCmMtaIpFilters,
       "saCmMtaSidCount": saCmMtaSidCount,
       "saCmMtaProvisioningMode": saCmMtaProvisioningMode,
       "saCmMtaDhcpPktcOption": saCmMtaDhcpPktcOption,
       "saCmMtaRequireTod": saCmMtaRequireTod,
       "saCmMtaDecryptMtaConfigFile": saCmMtaDecryptMtaConfigFile,
       "saCmMtaSwUpgradeControlTimer": saCmMtaSwUpgradeControlTimer,
       "saCmMtaDhcpOptionSixty": saCmMtaDhcpOptionSixty,
       "saCmMtaProvSnmpSetCommunityString": saCmMtaProvSnmpSetCommunityString,
       "saCmMtaCliAccess": saCmMtaCliAccess,
       "saCmMtaCliAccessPasswordType": saCmMtaCliAccessPasswordType}
)
