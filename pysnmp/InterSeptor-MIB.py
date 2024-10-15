# SNMP MIB module (InterSeptor-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/InterSeptor-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:12:32 2024
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
    "NotificationType",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Jacarta_ObjectIdentity = ObjectIdentity
jacarta = _Jacarta_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19011)
)
_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19011, 1)
)
_WebAppliance_ObjectIdentity = ObjectIdentity
webAppliance = _WebAppliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3)
)
_InSept_ObjectIdentity = ObjectIdentity
inSept = _InSept_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1)
)
_InSeptObjects_ObjectIdentity = ObjectIdentity
inSeptObjects = _InSeptObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1)
)
_InSeptIdent_ObjectIdentity = ObjectIdentity
inSeptIdent = _InSeptIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 1)
)


class _InSeptIdentManufacturer_Type(DisplayString):
    """Custom type inSeptIdentManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_InSeptIdentManufacturer_Type.__name__ = "DisplayString"
_InSeptIdentManufacturer_Object = MibScalar
inSeptIdentManufacturer = _InSeptIdentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 1, 1),
    _InSeptIdentManufacturer_Type()
)
inSeptIdentManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSeptIdentManufacturer.setStatus("mandatory")


class _InSeptIdentModel_Type(DisplayString):
    """Custom type inSeptIdentModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_InSeptIdentModel_Type.__name__ = "DisplayString"
_InSeptIdentModel_Object = MibScalar
inSeptIdentModel = _InSeptIdentModel_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 1, 2),
    _InSeptIdentModel_Type()
)
inSeptIdentModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSeptIdentModel.setStatus("mandatory")


class _InSeptIdentAgentSoftwareVersion_Type(DisplayString):
    """Custom type inSeptIdentAgentSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_InSeptIdentAgentSoftwareVersion_Type.__name__ = "DisplayString"
_InSeptIdentAgentSoftwareVersion_Object = MibScalar
inSeptIdentAgentSoftwareVersion = _InSeptIdentAgentSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 1, 3),
    _InSeptIdentAgentSoftwareVersion_Type()
)
inSeptIdentAgentSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSeptIdentAgentSoftwareVersion.setStatus("mandatory")


class _InSeptIdentName_Type(DisplayString):
    """Custom type inSeptIdentName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_InSeptIdentName_Type.__name__ = "DisplayString"
_InSeptIdentName_Object = MibScalar
inSeptIdentName = _InSeptIdentName_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 1, 4),
    _InSeptIdentName_Type()
)
inSeptIdentName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptIdentName.setStatus("mandatory")
_InSeptConfig_ObjectIdentity = ObjectIdentity
inSeptConfig = _InSeptConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2)
)
_InSeptConfigMibVersion_Type = Integer32
_InSeptConfigMibVersion_Object = MibScalar
inSeptConfigMibVersion = _InSeptConfigMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 1),
    _InSeptConfigMibVersion_Type()
)
inSeptConfigMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSeptConfigMibVersion.setStatus("mandatory")
_InSeptConfigNetwork_ObjectIdentity = ObjectIdentity
inSeptConfigNetwork = _InSeptConfigNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 2)
)
_InSeptConfigIpAddress_Type = IpAddress
_InSeptConfigIpAddress_Object = MibScalar
inSeptConfigIpAddress = _InSeptConfigIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 2, 1),
    _InSeptConfigIpAddress_Type()
)
inSeptConfigIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptConfigIpAddress.setStatus("mandatory")
_InSeptConfigGateway_Type = IpAddress
_InSeptConfigGateway_Object = MibScalar
inSeptConfigGateway = _InSeptConfigGateway_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 2, 2),
    _InSeptConfigGateway_Type()
)
inSeptConfigGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptConfigGateway.setStatus("mandatory")
_InSeptConfigSubnetMask_Type = IpAddress
_InSeptConfigSubnetMask_Object = MibScalar
inSeptConfigSubnetMask = _InSeptConfigSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 2, 3),
    _InSeptConfigSubnetMask_Type()
)
inSeptConfigSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptConfigSubnetMask.setStatus("mandatory")
_InSeptConfigDateTime_ObjectIdentity = ObjectIdentity
inSeptConfigDateTime = _InSeptConfigDateTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 3)
)


class _InSeptConfigDate_Type(DisplayString):
    """Custom type inSeptConfigDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_InSeptConfigDate_Type.__name__ = "DisplayString"
_InSeptConfigDate_Object = MibScalar
inSeptConfigDate = _InSeptConfigDate_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 3, 1),
    _InSeptConfigDate_Type()
)
inSeptConfigDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptConfigDate.setStatus("mandatory")


class _InSeptConfigTime_Type(DisplayString):
    """Custom type inSeptConfigTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_InSeptConfigTime_Type.__name__ = "DisplayString"
_InSeptConfigTime_Object = MibScalar
inSeptConfigTime = _InSeptConfigTime_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 3, 2),
    _InSeptConfigTime_Type()
)
inSeptConfigTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptConfigTime.setStatus("mandatory")


class _InSeptConfigTimeFromNtp_Type(Integer32):
    """Custom type inSeptConfigTimeFromNtp based on Integer32"""
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


_InSeptConfigTimeFromNtp_Type.__name__ = "Integer32"
_InSeptConfigTimeFromNtp_Object = MibScalar
inSeptConfigTimeFromNtp = _InSeptConfigTimeFromNtp_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 3, 3),
    _InSeptConfigTimeFromNtp_Type()
)
inSeptConfigTimeFromNtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptConfigTimeFromNtp.setStatus("mandatory")
_InSeptConfigNtpIpAddress_Type = IpAddress
_InSeptConfigNtpIpAddress_Object = MibScalar
inSeptConfigNtpIpAddress = _InSeptConfigNtpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 3, 4),
    _InSeptConfigNtpIpAddress_Type()
)
inSeptConfigNtpIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptConfigNtpIpAddress.setStatus("mandatory")


class _InSeptConfigNtpTimeZone_Type(Integer32):
    """Custom type inSeptConfigNtpTimeZone based on Integer32"""
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
              26,
              27,
              28)
        )
    )
    namedValues = NamedValues(
        *(("gMT-0000", 14),
          ("gMT-0100", 13),
          ("gMT-0200", 12),
          ("gMT-0300", 11),
          ("gMT-0330", 10),
          ("gMT-0400", 9),
          ("gMT-0500", 8),
          ("gMT-0600", 7),
          ("gMT-0700", 6),
          ("gMT-0800", 5),
          ("gMT-0900", 4),
          ("gMT-1000", 3),
          ("gMT-1100", 2),
          ("gMT-1200", 1),
          ("gMT0100", 15),
          ("gMT0200", 16),
          ("gMT0300", 17),
          ("gMT0330", 18),
          ("gMT0400", 19),
          ("gMT0500", 20),
          ("gMT0530", 21),
          ("gMT0600", 22),
          ("gMT0700", 23),
          ("gMT0800", 24),
          ("gMT0900", 25),
          ("gMT1000", 26),
          ("gMT1100", 27),
          ("gMT1200", 28))
    )


_InSeptConfigNtpTimeZone_Type.__name__ = "Integer32"
_InSeptConfigNtpTimeZone_Object = MibScalar
inSeptConfigNtpTimeZone = _InSeptConfigNtpTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 3, 5),
    _InSeptConfigNtpTimeZone_Type()
)
inSeptConfigNtpTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptConfigNtpTimeZone.setStatus("mandatory")


class _InSeptConfigDayLightSaving_Type(Integer32):
    """Custom type inSeptConfigDayLightSaving based on Integer32"""
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


_InSeptConfigDayLightSaving_Type.__name__ = "Integer32"
_InSeptConfigDayLightSaving_Object = MibScalar
inSeptConfigDayLightSaving = _InSeptConfigDayLightSaving_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 3, 6),
    _InSeptConfigDayLightSaving_Type()
)
inSeptConfigDayLightSaving.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptConfigDayLightSaving.setStatus("mandatory")
_InSeptConfigLog_ObjectIdentity = ObjectIdentity
inSeptConfigLog = _InSeptConfigLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 4)
)


class _InSeptConfigHistoryLogFrequency_Type(Integer32):
    """Custom type inSeptConfigHistoryLogFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 3600),
    )


_InSeptConfigHistoryLogFrequency_Type.__name__ = "Integer32"
_InSeptConfigHistoryLogFrequency_Object = MibScalar
inSeptConfigHistoryLogFrequency = _InSeptConfigHistoryLogFrequency_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 4, 1),
    _InSeptConfigHistoryLogFrequency_Type()
)
inSeptConfigHistoryLogFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptConfigHistoryLogFrequency.setStatus("mandatory")


class _InSeptConfigExtHistoryLogFrequency_Type(Integer32):
    """Custom type inSeptConfigExtHistoryLogFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_InSeptConfigExtHistoryLogFrequency_Type.__name__ = "Integer32"
_InSeptConfigExtHistoryLogFrequency_Object = MibScalar
inSeptConfigExtHistoryLogFrequency = _InSeptConfigExtHistoryLogFrequency_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 4, 2),
    _InSeptConfigExtHistoryLogFrequency_Type()
)
inSeptConfigExtHistoryLogFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptConfigExtHistoryLogFrequency.setStatus("mandatory")


class _InSeptConfigConfigurationLog_Type(Integer32):
    """Custom type inSeptConfigConfigurationLog based on Integer32"""
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


_InSeptConfigConfigurationLog_Type.__name__ = "Integer32"
_InSeptConfigConfigurationLog_Object = MibScalar
inSeptConfigConfigurationLog = _InSeptConfigConfigurationLog_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 4, 3),
    _InSeptConfigConfigurationLog_Type()
)
inSeptConfigConfigurationLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptConfigConfigurationLog.setStatus("mandatory")


class _InSeptConfigDhcpStatue_Type(Integer32):
    """Custom type inSeptConfigDhcpStatue based on Integer32"""
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


_InSeptConfigDhcpStatue_Type.__name__ = "Integer32"
_InSeptConfigDhcpStatue_Object = MibScalar
inSeptConfigDhcpStatue = _InSeptConfigDhcpStatue_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 5),
    _InSeptConfigDhcpStatue_Type()
)
inSeptConfigDhcpStatue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptConfigDhcpStatue.setStatus("mandatory")


class _InSeptConfigPingStatue_Type(Integer32):
    """Custom type inSeptConfigPingStatue based on Integer32"""
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


_InSeptConfigPingStatue_Type.__name__ = "Integer32"
_InSeptConfigPingStatue_Object = MibScalar
inSeptConfigPingStatue = _InSeptConfigPingStatue_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 6),
    _InSeptConfigPingStatue_Type()
)
inSeptConfigPingStatue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptConfigPingStatue.setStatus("mandatory")


class _InSeptConfigTftpStatue_Type(Integer32):
    """Custom type inSeptConfigTftpStatue based on Integer32"""
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


_InSeptConfigTftpStatue_Type.__name__ = "Integer32"
_InSeptConfigTftpStatue_Object = MibScalar
inSeptConfigTftpStatue = _InSeptConfigTftpStatue_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 7),
    _InSeptConfigTftpStatue_Type()
)
inSeptConfigTftpStatue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptConfigTftpStatue.setStatus("mandatory")
_InSeptConfigTelnet_ObjectIdentity = ObjectIdentity
inSeptConfigTelnet = _InSeptConfigTelnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 8)
)


class _InSeptConfigTelnetStatue_Type(Integer32):
    """Custom type inSeptConfigTelnetStatue based on Integer32"""
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


_InSeptConfigTelnetStatue_Type.__name__ = "Integer32"
_InSeptConfigTelnetStatue_Object = MibScalar
inSeptConfigTelnetStatue = _InSeptConfigTelnetStatue_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 8, 1),
    _InSeptConfigTelnetStatue_Type()
)
inSeptConfigTelnetStatue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptConfigTelnetStatue.setStatus("mandatory")


class _InSeptConfigTelnetPortNumber_Type(Integer32):
    """Custom type inSeptConfigTelnetPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_InSeptConfigTelnetPortNumber_Type.__name__ = "Integer32"
_InSeptConfigTelnetPortNumber_Object = MibScalar
inSeptConfigTelnetPortNumber = _InSeptConfigTelnetPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 8, 2),
    _InSeptConfigTelnetPortNumber_Type()
)
inSeptConfigTelnetPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptConfigTelnetPortNumber.setStatus("mandatory")
_InSeptConfigHttp_ObjectIdentity = ObjectIdentity
inSeptConfigHttp = _InSeptConfigHttp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 9)
)


class _InSeptConfigHttpStatue_Type(Integer32):
    """Custom type inSeptConfigHttpStatue based on Integer32"""
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


_InSeptConfigHttpStatue_Type.__name__ = "Integer32"
_InSeptConfigHttpStatue_Object = MibScalar
inSeptConfigHttpStatue = _InSeptConfigHttpStatue_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 9, 1),
    _InSeptConfigHttpStatue_Type()
)
inSeptConfigHttpStatue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptConfigHttpStatue.setStatus("mandatory")


class _InSeptConfigHttpPortNumber_Type(Integer32):
    """Custom type inSeptConfigHttpPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_InSeptConfigHttpPortNumber_Type.__name__ = "Integer32"
_InSeptConfigHttpPortNumber_Object = MibScalar
inSeptConfigHttpPortNumber = _InSeptConfigHttpPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 9, 2),
    _InSeptConfigHttpPortNumber_Type()
)
inSeptConfigHttpPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptConfigHttpPortNumber.setStatus("mandatory")


class _InSeptConfigHttpSecurity_Type(Integer32):
    """Custom type inSeptConfigHttpSecurity based on Integer32"""
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


_InSeptConfigHttpSecurity_Type.__name__ = "Integer32"
_InSeptConfigHttpSecurity_Object = MibScalar
inSeptConfigHttpSecurity = _InSeptConfigHttpSecurity_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 9, 3),
    _InSeptConfigHttpSecurity_Type()
)
inSeptConfigHttpSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptConfigHttpSecurity.setStatus("mandatory")
_InSeptConfigSnmp_ObjectIdentity = ObjectIdentity
inSeptConfigSnmp = _InSeptConfigSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 10)
)


class _InSeptConfigSnmpStatue_Type(Integer32):
    """Custom type inSeptConfigSnmpStatue based on Integer32"""
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


_InSeptConfigSnmpStatue_Type.__name__ = "Integer32"
_InSeptConfigSnmpStatue_Object = MibScalar
inSeptConfigSnmpStatue = _InSeptConfigSnmpStatue_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 10, 1),
    _InSeptConfigSnmpStatue_Type()
)
inSeptConfigSnmpStatue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptConfigSnmpStatue.setStatus("mandatory")


class _InSeptConfigSnmpPortNumber_Type(Integer32):
    """Custom type inSeptConfigSnmpPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_InSeptConfigSnmpPortNumber_Type.__name__ = "Integer32"
_InSeptConfigSnmpPortNumber_Object = MibScalar
inSeptConfigSnmpPortNumber = _InSeptConfigSnmpPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 10, 2),
    _InSeptConfigSnmpPortNumber_Type()
)
inSeptConfigSnmpPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptConfigSnmpPortNumber.setStatus("mandatory")
_InSeptConfigControl_ObjectIdentity = ObjectIdentity
inSeptConfigControl = _InSeptConfigControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 11)
)


class _InSeptConfigResetToDefault_Type(Integer32):
    """Custom type inSeptConfigResetToDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 2),
          ("reset", 1))
    )


_InSeptConfigResetToDefault_Type.__name__ = "Integer32"
_InSeptConfigResetToDefault_Object = MibScalar
inSeptConfigResetToDefault = _InSeptConfigResetToDefault_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 11, 1),
    _InSeptConfigResetToDefault_Type()
)
inSeptConfigResetToDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptConfigResetToDefault.setStatus("mandatory")


class _InSeptConfigRestart_Type(Integer32):
    """Custom type inSeptConfigRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 2),
          ("restart", 1))
    )


_InSeptConfigRestart_Type.__name__ = "Integer32"
_InSeptConfigRestart_Object = MibScalar
inSeptConfigRestart = _InSeptConfigRestart_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 11, 2),
    _InSeptConfigRestart_Type()
)
inSeptConfigRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptConfigRestart.setStatus("mandatory")
_InSeptConfigTrap_ObjectIdentity = ObjectIdentity
inSeptConfigTrap = _InSeptConfigTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 12)
)
_InSeptConfigTrapRetryCount_Type = Integer32
_InSeptConfigTrapRetryCount_Object = MibScalar
inSeptConfigTrapRetryCount = _InSeptConfigTrapRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 12, 1),
    _InSeptConfigTrapRetryCount_Type()
)
inSeptConfigTrapRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptConfigTrapRetryCount.setStatus("mandatory")
_InSeptConfigTrapRetryTime_Type = Integer32
_InSeptConfigTrapRetryTime_Object = MibScalar
inSeptConfigTrapRetryTime = _InSeptConfigTrapRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 12, 2),
    _InSeptConfigTrapRetryTime_Type()
)
inSeptConfigTrapRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptConfigTrapRetryTime.setStatus("mandatory")
_InSeptConfigTrapAckSignature_Type = Integer32
_InSeptConfigTrapAckSignature_Object = MibScalar
inSeptConfigTrapAckSignature = _InSeptConfigTrapAckSignature_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 12, 3),
    _InSeptConfigTrapAckSignature_Type()
)
inSeptConfigTrapAckSignature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptConfigTrapAckSignature.setStatus("mandatory")


class _InSeptConfigPollRate_Type(Integer32):
    """Custom type inSeptConfigPollRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 60),
    )


_InSeptConfigPollRate_Type.__name__ = "Integer32"
_InSeptConfigPollRate_Object = MibScalar
inSeptConfigPollRate = _InSeptConfigPollRate_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 13),
    _InSeptConfigPollRate_Type()
)
inSeptConfigPollRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptConfigPollRate.setStatus("mandatory")
_InSeptConfigTrapsReceiversTable_Object = MibTable
inSeptConfigTrapsReceiversTable = _InSeptConfigTrapsReceiversTable_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 14)
)
if mibBuilder.loadTexts:
    inSeptConfigTrapsReceiversTable.setStatus("mandatory")
_InSeptConfigTrapsReceiversEntry_Object = MibTableRow
inSeptConfigTrapsReceiversEntry = _InSeptConfigTrapsReceiversEntry_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 14, 1)
)
inSeptConfigTrapsReceiversEntry.setIndexNames(
    (0, "InterSeptor-MIB", "inSepttrapsIndex"),
)
if mibBuilder.loadTexts:
    inSeptConfigTrapsReceiversEntry.setStatus("mandatory")


class _InSepttrapsIndex_Type(Integer32):
    """Custom type inSepttrapsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_InSepttrapsIndex_Type.__name__ = "Integer32"
_InSepttrapsIndex_Object = MibTableColumn
inSepttrapsIndex = _InSepttrapsIndex_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 14, 1, 1),
    _InSepttrapsIndex_Type()
)
inSepttrapsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSepttrapsIndex.setStatus("mandatory")
_InSepttrapsReceiverAddr_Type = IpAddress
_InSepttrapsReceiverAddr_Object = MibTableColumn
inSepttrapsReceiverAddr = _InSepttrapsReceiverAddr_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 14, 1, 2),
    _InSepttrapsReceiverAddr_Type()
)
inSepttrapsReceiverAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSepttrapsReceiverAddr.setStatus("mandatory")


class _InSeptreceiverCommunityString_Type(DisplayString):
    """Custom type inSeptreceiverCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_InSeptreceiverCommunityString_Type.__name__ = "DisplayString"
_InSeptreceiverCommunityString_Object = MibTableColumn
inSeptreceiverCommunityString = _InSeptreceiverCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 14, 1, 3),
    _InSeptreceiverCommunityString_Type()
)
inSeptreceiverCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptreceiverCommunityString.setStatus("mandatory")


class _InSeptreceiverSeverityLevel_Type(Integer32):
    """Custom type inSeptreceiverSeverityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("informational", 1),
          ("severe", 3),
          ("warning", 2))
    )


_InSeptreceiverSeverityLevel_Type.__name__ = "Integer32"
_InSeptreceiverSeverityLevel_Object = MibTableColumn
inSeptreceiverSeverityLevel = _InSeptreceiverSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 14, 1, 4),
    _InSeptreceiverSeverityLevel_Type()
)
inSeptreceiverSeverityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptreceiverSeverityLevel.setStatus("mandatory")


class _InSeptreceiverDescription_Type(DisplayString):
    """Custom type inSeptreceiverDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_InSeptreceiverDescription_Type.__name__ = "DisplayString"
_InSeptreceiverDescription_Object = MibTableColumn
inSeptreceiverDescription = _InSeptreceiverDescription_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 14, 1, 5),
    _InSeptreceiverDescription_Type()
)
inSeptreceiverDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptreceiverDescription.setStatus("mandatory")
_InSeptConfigAccessControlTable_Object = MibTable
inSeptConfigAccessControlTable = _InSeptConfigAccessControlTable_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 15)
)
if mibBuilder.loadTexts:
    inSeptConfigAccessControlTable.setStatus("mandatory")
_InSeptConfigAccessControlEntry_Object = MibTableRow
inSeptConfigAccessControlEntry = _InSeptConfigAccessControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 15, 1)
)
inSeptConfigAccessControlEntry.setIndexNames(
    (0, "InterSeptor-MIB", "accessIndex"),
)
if mibBuilder.loadTexts:
    inSeptConfigAccessControlEntry.setStatus("mandatory")


class _AccessIndex_Type(Integer32):
    """Custom type accessIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AccessIndex_Type.__name__ = "Integer32"
_AccessIndex_Object = MibTableColumn
accessIndex = _AccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 15, 1, 1),
    _AccessIndex_Type()
)
accessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessIndex.setStatus("mandatory")
_AccessControlAddr_Type = IpAddress
_AccessControlAddr_Object = MibTableColumn
accessControlAddr = _AccessControlAddr_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 15, 1, 2),
    _AccessControlAddr_Type()
)
accessControlAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessControlAddr.setStatus("mandatory")


class _AccessCommunityString_Type(DisplayString):
    """Custom type accessCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_AccessCommunityString_Type.__name__ = "DisplayString"
_AccessCommunityString_Object = MibTableColumn
accessCommunityString = _AccessCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 15, 1, 3),
    _AccessCommunityString_Type()
)
accessCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessCommunityString.setStatus("mandatory")


class _AccessControlMode_Type(Integer32):
    """Custom type accessControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notAccess", 3),
          ("read-write", 2),
          ("readOnly", 1))
    )


_AccessControlMode_Type.__name__ = "Integer32"
_AccessControlMode_Object = MibTableColumn
accessControlMode = _AccessControlMode_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 15, 1, 4),
    _AccessControlMode_Type()
)
accessControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessControlMode.setStatus("mandatory")


class _InSeptConfigTemperatureUnit_Type(Integer32):
    """Custom type inSeptConfigTemperatureUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("celsius", 1),
          ("fahrenheit", 2))
    )


_InSeptConfigTemperatureUnit_Type.__name__ = "Integer32"
_InSeptConfigTemperatureUnit_Object = MibScalar
inSeptConfigTemperatureUnit = _InSeptConfigTemperatureUnit_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 16),
    _InSeptConfigTemperatureUnit_Type()
)
inSeptConfigTemperatureUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptConfigTemperatureUnit.setStatus("mandatory")


class _InSeptConfigDateFormat_Type(Integer32):
    """Custom type inSeptConfigDateFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dd-mm-yyyy", 1),
          ("mm-dd-yyyy", 2))
    )


_InSeptConfigDateFormat_Type.__name__ = "Integer32"
_InSeptConfigDateFormat_Object = MibScalar
inSeptConfigDateFormat = _InSeptConfigDateFormat_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 2, 17),
    _InSeptConfigDateFormat_Type()
)
inSeptConfigDateFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptConfigDateFormat.setStatus("mandatory")
_InSeptsensorMonitor_ObjectIdentity = ObjectIdentity
inSeptsensorMonitor = _InSeptsensorMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 3)
)
_InSeptsensorMonitorSensorNumber_Type = Integer32
_InSeptsensorMonitorSensorNumber_Object = MibScalar
inSeptsensorMonitorSensorNumber = _InSeptsensorMonitorSensorNumber_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 3, 1),
    _InSeptsensorMonitorSensorNumber_Type()
)
inSeptsensorMonitorSensorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSeptsensorMonitorSensorNumber.setStatus("mandatory")
_InSeptsensorMonitorSensorTable_Object = MibTable
inSeptsensorMonitorSensorTable = _InSeptsensorMonitorSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    inSeptsensorMonitorSensorTable.setStatus("mandatory")
_InSeptsensorMonitorSensorEntry_Object = MibTableRow
inSeptsensorMonitorSensorEntry = _InSeptsensorMonitorSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 3, 2, 1)
)
inSeptsensorMonitorSensorEntry.setIndexNames(
    (0, "InterSeptor-MIB", "inSeptsensorMonitorDeviceIndex"),
)
if mibBuilder.loadTexts:
    inSeptsensorMonitorSensorEntry.setStatus("mandatory")


class _InSeptsensorMonitorDeviceIndex_Type(Integer32):
    """Custom type inSeptsensorMonitorDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_InSeptsensorMonitorDeviceIndex_Type.__name__ = "Integer32"
_InSeptsensorMonitorDeviceIndex_Object = MibTableColumn
inSeptsensorMonitorDeviceIndex = _InSeptsensorMonitorDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 3, 2, 1, 1),
    _InSeptsensorMonitorDeviceIndex_Type()
)
inSeptsensorMonitorDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSeptsensorMonitorDeviceIndex.setStatus("mandatory")


class _InSeptsensorMonitorDeviceStatus_Type(Integer32):
    """Custom type inSeptsensorMonitorDeviceStatus based on Integer32"""
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
          ("eMD-HT", 3),
          ("eMD-T", 4),
          ("unknown", 1))
    )


_InSeptsensorMonitorDeviceStatus_Type.__name__ = "Integer32"
_InSeptsensorMonitorDeviceStatus_Object = MibTableColumn
inSeptsensorMonitorDeviceStatus = _InSeptsensorMonitorDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 3, 2, 1, 2),
    _InSeptsensorMonitorDeviceStatus_Type()
)
inSeptsensorMonitorDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSeptsensorMonitorDeviceStatus.setStatus("mandatory")
_InSeptsensorMonitorDeviceTemperature_Type = Integer32
_InSeptsensorMonitorDeviceTemperature_Object = MibTableColumn
inSeptsensorMonitorDeviceTemperature = _InSeptsensorMonitorDeviceTemperature_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 3, 2, 1, 3),
    _InSeptsensorMonitorDeviceTemperature_Type()
)
inSeptsensorMonitorDeviceTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSeptsensorMonitorDeviceTemperature.setStatus("mandatory")


class _InSeptsensorMonitorDeviceTemperatureAlarm_Type(Integer32):
    """Custom type inSeptsensorMonitorDeviceTemperatureAlarm based on Integer32"""
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
        *(("disabled", 2),
          ("highCritical", 7),
          ("highWarning", 6),
          ("lowCritical", 5),
          ("lowWarning", 4),
          ("normal", 3),
          ("unknown", 1))
    )


_InSeptsensorMonitorDeviceTemperatureAlarm_Type.__name__ = "Integer32"
_InSeptsensorMonitorDeviceTemperatureAlarm_Object = MibTableColumn
inSeptsensorMonitorDeviceTemperatureAlarm = _InSeptsensorMonitorDeviceTemperatureAlarm_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 3, 2, 1, 4),
    _InSeptsensorMonitorDeviceTemperatureAlarm_Type()
)
inSeptsensorMonitorDeviceTemperatureAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSeptsensorMonitorDeviceTemperatureAlarm.setStatus("mandatory")
_InSeptsensorMonitorDeviceHumidity_Type = Integer32
_InSeptsensorMonitorDeviceHumidity_Object = MibTableColumn
inSeptsensorMonitorDeviceHumidity = _InSeptsensorMonitorDeviceHumidity_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 3, 2, 1, 5),
    _InSeptsensorMonitorDeviceHumidity_Type()
)
inSeptsensorMonitorDeviceHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSeptsensorMonitorDeviceHumidity.setStatus("mandatory")


class _InSeptsensorMonitorDeviceHumidityAlarm_Type(Integer32):
    """Custom type inSeptsensorMonitorDeviceHumidityAlarm based on Integer32"""
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
        *(("disabled", 2),
          ("highCritical", 7),
          ("highWarning", 6),
          ("lowCritical", 5),
          ("lowWarning", 4),
          ("normal", 3),
          ("unknown", 1))
    )


_InSeptsensorMonitorDeviceHumidityAlarm_Type.__name__ = "Integer32"
_InSeptsensorMonitorDeviceHumidityAlarm_Object = MibTableColumn
inSeptsensorMonitorDeviceHumidityAlarm = _InSeptsensorMonitorDeviceHumidityAlarm_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 3, 2, 1, 6),
    _InSeptsensorMonitorDeviceHumidityAlarm_Type()
)
inSeptsensorMonitorDeviceHumidityAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSeptsensorMonitorDeviceHumidityAlarm.setStatus("mandatory")


class _InSeptsensorMonitorAlarm1_Type(Integer32):
    """Custom type inSeptsensorMonitorAlarm1 based on Integer32"""
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
        *(("active", 3),
          ("disabled", 2),
          ("inactive", 4),
          ("unknown", 1))
    )


_InSeptsensorMonitorAlarm1_Type.__name__ = "Integer32"
_InSeptsensorMonitorAlarm1_Object = MibTableColumn
inSeptsensorMonitorAlarm1 = _InSeptsensorMonitorAlarm1_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 3, 2, 1, 7),
    _InSeptsensorMonitorAlarm1_Type()
)
inSeptsensorMonitorAlarm1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSeptsensorMonitorAlarm1.setStatus("mandatory")


class _InSeptsensorMonitorAlarm2_Type(Integer32):
    """Custom type inSeptsensorMonitorAlarm2 based on Integer32"""
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
        *(("active", 3),
          ("disabled", 2),
          ("inactive", 4),
          ("unknown", 1))
    )


_InSeptsensorMonitorAlarm2_Type.__name__ = "Integer32"
_InSeptsensorMonitorAlarm2_Object = MibTableColumn
inSeptsensorMonitorAlarm2 = _InSeptsensorMonitorAlarm2_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 3, 2, 1, 8),
    _InSeptsensorMonitorAlarm2_Type()
)
inSeptsensorMonitorAlarm2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSeptsensorMonitorAlarm2.setStatus("mandatory")
_InSeptsensorConfig_ObjectIdentity = ObjectIdentity
inSeptsensorConfig = _InSeptsensorConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4)
)
_InSeptsensorConfigSensorNumber_Type = Integer32
_InSeptsensorConfigSensorNumber_Object = MibScalar
inSeptsensorConfigSensorNumber = _InSeptsensorConfigSensorNumber_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 1),
    _InSeptsensorConfigSensorNumber_Type()
)
inSeptsensorConfigSensorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensorNumber.setStatus("mandatory")
_InSeptsensorConfigSensorTable_Object = MibTable
inSeptsensorConfigSensorTable = _InSeptsensorConfigSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    inSeptsensorConfigSensorTable.setStatus("mandatory")
_InSeptsensorConfigSensorEntry_Object = MibTableRow
inSeptsensorConfigSensorEntry = _InSeptsensorConfigSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 2, 1)
)
inSeptsensorConfigSensorEntry.setIndexNames(
    (0, "InterSeptor-MIB", "inSeptsensorConfigDeviceIndex"),
)
if mibBuilder.loadTexts:
    inSeptsensorConfigSensorEntry.setStatus("mandatory")


class _InSeptsensorConfigDeviceIndex_Type(Integer32):
    """Custom type inSeptsensorConfigDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_InSeptsensorConfigDeviceIndex_Type.__name__ = "Integer32"
_InSeptsensorConfigDeviceIndex_Object = MibTableColumn
inSeptsensorConfigDeviceIndex = _InSeptsensorConfigDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 2, 1, 1),
    _InSeptsensorConfigDeviceIndex_Type()
)
inSeptsensorConfigDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSeptsensorConfigDeviceIndex.setStatus("mandatory")


class _InSeptsensorConfigDeviceName_Type(DisplayString):
    """Custom type inSeptsensorConfigDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_InSeptsensorConfigDeviceName_Type.__name__ = "DisplayString"
_InSeptsensorConfigDeviceName_Object = MibTableColumn
inSeptsensorConfigDeviceName = _InSeptsensorConfigDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 2, 1, 2),
    _InSeptsensorConfigDeviceName_Type()
)
inSeptsensorConfigDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigDeviceName.setStatus("mandatory")


class _InSeptsensorConfigDeviceState_Type(Integer32):
    """Custom type inSeptsensorConfigDeviceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("disabled", 1))
    )


_InSeptsensorConfigDeviceState_Type.__name__ = "Integer32"
_InSeptsensorConfigDeviceState_Object = MibTableColumn
inSeptsensorConfigDeviceState = _InSeptsensorConfigDeviceState_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 2, 1, 3),
    _InSeptsensorConfigDeviceState_Type()
)
inSeptsensorConfigDeviceState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigDeviceState.setStatus("mandatory")
_InSeptsensorConfigSensor1_ObjectIdentity = ObjectIdentity
inSeptsensorConfigSensor1 = _InSeptsensorConfigSensor1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 3)
)


class _InSeptsensorConfigSensor1DeviceName_Type(DisplayString):
    """Custom type inSeptsensorConfigSensor1DeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_InSeptsensorConfigSensor1DeviceName_Type.__name__ = "DisplayString"
_InSeptsensorConfigSensor1DeviceName_Object = MibScalar
inSeptsensorConfigSensor1DeviceName = _InSeptsensorConfigSensor1DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 3, 1),
    _InSeptsensorConfigSensor1DeviceName_Type()
)
inSeptsensorConfigSensor1DeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor1DeviceName.setStatus("mandatory")


class _InSeptsensorConfigSensor1DeviceState_Type(Integer32):
    """Custom type inSeptsensorConfigSensor1DeviceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("disabled", 1))
    )


_InSeptsensorConfigSensor1DeviceState_Type.__name__ = "Integer32"
_InSeptsensorConfigSensor1DeviceState_Object = MibScalar
inSeptsensorConfigSensor1DeviceState = _InSeptsensorConfigSensor1DeviceState_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 3, 2),
    _InSeptsensorConfigSensor1DeviceState_Type()
)
inSeptsensorConfigSensor1DeviceState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor1DeviceState.setStatus("mandatory")
_InSeptsensorConfigSensor1Temperature_ObjectIdentity = ObjectIdentity
inSeptsensorConfigSensor1Temperature = _InSeptsensorConfigSensor1Temperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 3, 3)
)


class _InSeptsensorConfigSensor1TemperatureName_Type(DisplayString):
    """Custom type inSeptsensorConfigSensor1TemperatureName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_InSeptsensorConfigSensor1TemperatureName_Type.__name__ = "DisplayString"
_InSeptsensorConfigSensor1TemperatureName_Object = MibScalar
inSeptsensorConfigSensor1TemperatureName = _InSeptsensorConfigSensor1TemperatureName_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 3, 3, 1),
    _InSeptsensorConfigSensor1TemperatureName_Type()
)
inSeptsensorConfigSensor1TemperatureName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor1TemperatureName.setStatus("mandatory")
_InSeptsensorConfigSensor1TemperatureLowWarning_Type = Integer32
_InSeptsensorConfigSensor1TemperatureLowWarning_Object = MibScalar
inSeptsensorConfigSensor1TemperatureLowWarning = _InSeptsensorConfigSensor1TemperatureLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 3, 3, 2),
    _InSeptsensorConfigSensor1TemperatureLowWarning_Type()
)
inSeptsensorConfigSensor1TemperatureLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor1TemperatureLowWarning.setStatus("mandatory")
_InSeptsensorConfigSensor1TemperatureLowCritical_Type = Integer32
_InSeptsensorConfigSensor1TemperatureLowCritical_Object = MibScalar
inSeptsensorConfigSensor1TemperatureLowCritical = _InSeptsensorConfigSensor1TemperatureLowCritical_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 3, 3, 3),
    _InSeptsensorConfigSensor1TemperatureLowCritical_Type()
)
inSeptsensorConfigSensor1TemperatureLowCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor1TemperatureLowCritical.setStatus("mandatory")
_InSeptsensorConfigSensor1TemperatureHighWarning_Type = Integer32
_InSeptsensorConfigSensor1TemperatureHighWarning_Object = MibScalar
inSeptsensorConfigSensor1TemperatureHighWarning = _InSeptsensorConfigSensor1TemperatureHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 3, 3, 4),
    _InSeptsensorConfigSensor1TemperatureHighWarning_Type()
)
inSeptsensorConfigSensor1TemperatureHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor1TemperatureHighWarning.setStatus("mandatory")
_InSeptsensorConfigSensor1TemperatureHighCritical_Type = Integer32
_InSeptsensorConfigSensor1TemperatureHighCritical_Object = MibScalar
inSeptsensorConfigSensor1TemperatureHighCritical = _InSeptsensorConfigSensor1TemperatureHighCritical_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 3, 3, 5),
    _InSeptsensorConfigSensor1TemperatureHighCritical_Type()
)
inSeptsensorConfigSensor1TemperatureHighCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor1TemperatureHighCritical.setStatus("mandatory")
_InSeptsensorConfigSensor1TemperatureHysteresis_Type = Integer32
_InSeptsensorConfigSensor1TemperatureHysteresis_Object = MibScalar
inSeptsensorConfigSensor1TemperatureHysteresis = _InSeptsensorConfigSensor1TemperatureHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 3, 3, 6),
    _InSeptsensorConfigSensor1TemperatureHysteresis_Type()
)
inSeptsensorConfigSensor1TemperatureHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor1TemperatureHysteresis.setStatus("mandatory")


class _InSeptsensorConfigSensor1TemperatureCalibration_Type(Integer32):
    """Custom type inSeptsensorConfigSensor1TemperatureCalibration based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("temperatureIncrease0Point0", 1),
          ("temperatureIncrease0Point5", 2),
          ("temperatureIncrease1Point0", 3),
          ("temperatureIncrease1Point5", 4),
          ("temperatureIncrease2Point0", 5),
          ("temperatureIncrease2Point5", 6),
          ("temperatureIncrease3Point0", 7),
          ("temperatureMinus0Point5", 8),
          ("temperatureMinus1Point0", 9),
          ("temperatureMinus1Point5", 10),
          ("temperatureMinus2Point0", 11),
          ("temperatureMinus2Point5", 12),
          ("temperatureMinusPoint0", 13))
    )


_InSeptsensorConfigSensor1TemperatureCalibration_Type.__name__ = "Integer32"
_InSeptsensorConfigSensor1TemperatureCalibration_Object = MibScalar
inSeptsensorConfigSensor1TemperatureCalibration = _InSeptsensorConfigSensor1TemperatureCalibration_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 3, 3, 7),
    _InSeptsensorConfigSensor1TemperatureCalibration_Type()
)
inSeptsensorConfigSensor1TemperatureCalibration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor1TemperatureCalibration.setStatus("mandatory")


class _InSeptsensorConfigSensor1TemperatureLowWarningStatus_Type(Integer32):
    """Custom type inSeptsensorConfigSensor1TemperatureLowWarningStatus based on Integer32"""
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


_InSeptsensorConfigSensor1TemperatureLowWarningStatus_Type.__name__ = "Integer32"
_InSeptsensorConfigSensor1TemperatureLowWarningStatus_Object = MibScalar
inSeptsensorConfigSensor1TemperatureLowWarningStatus = _InSeptsensorConfigSensor1TemperatureLowWarningStatus_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 3, 3, 8),
    _InSeptsensorConfigSensor1TemperatureLowWarningStatus_Type()
)
inSeptsensorConfigSensor1TemperatureLowWarningStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor1TemperatureLowWarningStatus.setStatus("mandatory")


class _InSeptsensorConfigSensor1TemperatureLowCriticalStatus_Type(Integer32):
    """Custom type inSeptsensorConfigSensor1TemperatureLowCriticalStatus based on Integer32"""
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


_InSeptsensorConfigSensor1TemperatureLowCriticalStatus_Type.__name__ = "Integer32"
_InSeptsensorConfigSensor1TemperatureLowCriticalStatus_Object = MibScalar
inSeptsensorConfigSensor1TemperatureLowCriticalStatus = _InSeptsensorConfigSensor1TemperatureLowCriticalStatus_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 3, 3, 9),
    _InSeptsensorConfigSensor1TemperatureLowCriticalStatus_Type()
)
inSeptsensorConfigSensor1TemperatureLowCriticalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor1TemperatureLowCriticalStatus.setStatus("mandatory")


class _InSeptsensorConfigSensor1TemperatureHighWarningStatus_Type(Integer32):
    """Custom type inSeptsensorConfigSensor1TemperatureHighWarningStatus based on Integer32"""
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


_InSeptsensorConfigSensor1TemperatureHighWarningStatus_Type.__name__ = "Integer32"
_InSeptsensorConfigSensor1TemperatureHighWarningStatus_Object = MibScalar
inSeptsensorConfigSensor1TemperatureHighWarningStatus = _InSeptsensorConfigSensor1TemperatureHighWarningStatus_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 3, 3, 10),
    _InSeptsensorConfigSensor1TemperatureHighWarningStatus_Type()
)
inSeptsensorConfigSensor1TemperatureHighWarningStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor1TemperatureHighWarningStatus.setStatus("mandatory")


class _InSeptsensorConfigSensor1TemperatureHighCriticalStatus_Type(Integer32):
    """Custom type inSeptsensorConfigSensor1TemperatureHighCriticalStatus based on Integer32"""
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


_InSeptsensorConfigSensor1TemperatureHighCriticalStatus_Type.__name__ = "Integer32"
_InSeptsensorConfigSensor1TemperatureHighCriticalStatus_Object = MibScalar
inSeptsensorConfigSensor1TemperatureHighCriticalStatus = _InSeptsensorConfigSensor1TemperatureHighCriticalStatus_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 3, 3, 11),
    _InSeptsensorConfigSensor1TemperatureHighCriticalStatus_Type()
)
inSeptsensorConfigSensor1TemperatureHighCriticalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor1TemperatureHighCriticalStatus.setStatus("mandatory")
_InSeptsensorConfigSensor1Humidity_ObjectIdentity = ObjectIdentity
inSeptsensorConfigSensor1Humidity = _InSeptsensorConfigSensor1Humidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 3, 4)
)


class _InSeptsensorConfigSensor1HumdityName_Type(DisplayString):
    """Custom type inSeptsensorConfigSensor1HumdityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_InSeptsensorConfigSensor1HumdityName_Type.__name__ = "DisplayString"
_InSeptsensorConfigSensor1HumdityName_Object = MibScalar
inSeptsensorConfigSensor1HumdityName = _InSeptsensorConfigSensor1HumdityName_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 3, 4, 1),
    _InSeptsensorConfigSensor1HumdityName_Type()
)
inSeptsensorConfigSensor1HumdityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor1HumdityName.setStatus("mandatory")
_InSeptsensorConfigSensor1HumidityLowWarning_Type = Integer32
_InSeptsensorConfigSensor1HumidityLowWarning_Object = MibScalar
inSeptsensorConfigSensor1HumidityLowWarning = _InSeptsensorConfigSensor1HumidityLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 3, 4, 2),
    _InSeptsensorConfigSensor1HumidityLowWarning_Type()
)
inSeptsensorConfigSensor1HumidityLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor1HumidityLowWarning.setStatus("mandatory")
_InSeptsensorConfigSensor1HumidityLowCritical_Type = Integer32
_InSeptsensorConfigSensor1HumidityLowCritical_Object = MibScalar
inSeptsensorConfigSensor1HumidityLowCritical = _InSeptsensorConfigSensor1HumidityLowCritical_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 3, 4, 3),
    _InSeptsensorConfigSensor1HumidityLowCritical_Type()
)
inSeptsensorConfigSensor1HumidityLowCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor1HumidityLowCritical.setStatus("mandatory")
_InSeptsensorConfigSensor1HumidityHighWarning_Type = Integer32
_InSeptsensorConfigSensor1HumidityHighWarning_Object = MibScalar
inSeptsensorConfigSensor1HumidityHighWarning = _InSeptsensorConfigSensor1HumidityHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 3, 4, 4),
    _InSeptsensorConfigSensor1HumidityHighWarning_Type()
)
inSeptsensorConfigSensor1HumidityHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor1HumidityHighWarning.setStatus("mandatory")
_InSeptsensorConfigSensor1HumidityHighCritical_Type = Integer32
_InSeptsensorConfigSensor1HumidityHighCritical_Object = MibScalar
inSeptsensorConfigSensor1HumidityHighCritical = _InSeptsensorConfigSensor1HumidityHighCritical_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 3, 4, 5),
    _InSeptsensorConfigSensor1HumidityHighCritical_Type()
)
inSeptsensorConfigSensor1HumidityHighCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor1HumidityHighCritical.setStatus("mandatory")
_InSeptsensorConfigSensor1HumidityHysteresis_Type = Integer32
_InSeptsensorConfigSensor1HumidityHysteresis_Object = MibScalar
inSeptsensorConfigSensor1HumidityHysteresis = _InSeptsensorConfigSensor1HumidityHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 3, 4, 6),
    _InSeptsensorConfigSensor1HumidityHysteresis_Type()
)
inSeptsensorConfigSensor1HumidityHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor1HumidityHysteresis.setStatus("mandatory")


class _InSeptsensorConfigSensor1HumidityCalibration_Type(Integer32):
    """Custom type inSeptsensorConfigSensor1HumidityCalibration based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("humidityIncrease0Point0", 1),
          ("humidityIncrease1Point0", 2),
          ("humidityIncrease2Point0", 3),
          ("humidityIncrease3Point0", 4),
          ("humidityIncrease4Point0", 5),
          ("humidityIncrease5Point0", 6),
          ("humidityIncrease6Point0", 7),
          ("humidityMinus1Point0", 8),
          ("humidityMinus2Point0", 9),
          ("humidityMinus3Point0", 10),
          ("humidityMinus4Point0", 11),
          ("humidityMinus5Point0", 12),
          ("humidityMinus6Point0", 13))
    )


_InSeptsensorConfigSensor1HumidityCalibration_Type.__name__ = "Integer32"
_InSeptsensorConfigSensor1HumidityCalibration_Object = MibScalar
inSeptsensorConfigSensor1HumidityCalibration = _InSeptsensorConfigSensor1HumidityCalibration_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 3, 4, 7),
    _InSeptsensorConfigSensor1HumidityCalibration_Type()
)
inSeptsensorConfigSensor1HumidityCalibration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor1HumidityCalibration.setStatus("mandatory")


class _InSeptsensorConfigSensor1HumidityLowWarningStatus_Type(Integer32):
    """Custom type inSeptsensorConfigSensor1HumidityLowWarningStatus based on Integer32"""
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


_InSeptsensorConfigSensor1HumidityLowWarningStatus_Type.__name__ = "Integer32"
_InSeptsensorConfigSensor1HumidityLowWarningStatus_Object = MibScalar
inSeptsensorConfigSensor1HumidityLowWarningStatus = _InSeptsensorConfigSensor1HumidityLowWarningStatus_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 3, 4, 8),
    _InSeptsensorConfigSensor1HumidityLowWarningStatus_Type()
)
inSeptsensorConfigSensor1HumidityLowWarningStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor1HumidityLowWarningStatus.setStatus("mandatory")


class _InSeptsensorConfigSensor1HumidityLowCriticalStatus_Type(Integer32):
    """Custom type inSeptsensorConfigSensor1HumidityLowCriticalStatus based on Integer32"""
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


_InSeptsensorConfigSensor1HumidityLowCriticalStatus_Type.__name__ = "Integer32"
_InSeptsensorConfigSensor1HumidityLowCriticalStatus_Object = MibScalar
inSeptsensorConfigSensor1HumidityLowCriticalStatus = _InSeptsensorConfigSensor1HumidityLowCriticalStatus_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 3, 4, 9),
    _InSeptsensorConfigSensor1HumidityLowCriticalStatus_Type()
)
inSeptsensorConfigSensor1HumidityLowCriticalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor1HumidityLowCriticalStatus.setStatus("mandatory")


class _InSeptsensorConfigSensor1HumidityHighWarningStatus_Type(Integer32):
    """Custom type inSeptsensorConfigSensor1HumidityHighWarningStatus based on Integer32"""
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


_InSeptsensorConfigSensor1HumidityHighWarningStatus_Type.__name__ = "Integer32"
_InSeptsensorConfigSensor1HumidityHighWarningStatus_Object = MibScalar
inSeptsensorConfigSensor1HumidityHighWarningStatus = _InSeptsensorConfigSensor1HumidityHighWarningStatus_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 3, 4, 10),
    _InSeptsensorConfigSensor1HumidityHighWarningStatus_Type()
)
inSeptsensorConfigSensor1HumidityHighWarningStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor1HumidityHighWarningStatus.setStatus("mandatory")


class _InSeptsensorConfigSensor1HumidityHighCriticalStatus_Type(Integer32):
    """Custom type inSeptsensorConfigSensor1HumidityHighCriticalStatus based on Integer32"""
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


_InSeptsensorConfigSensor1HumidityHighCriticalStatus_Type.__name__ = "Integer32"
_InSeptsensorConfigSensor1HumidityHighCriticalStatus_Object = MibScalar
inSeptsensorConfigSensor1HumidityHighCriticalStatus = _InSeptsensorConfigSensor1HumidityHighCriticalStatus_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 3, 4, 11),
    _InSeptsensorConfigSensor1HumidityHighCriticalStatus_Type()
)
inSeptsensorConfigSensor1HumidityHighCriticalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor1HumidityHighCriticalStatus.setStatus("mandatory")
_InSeptsensorConfigSensor1Alarm1_ObjectIdentity = ObjectIdentity
inSeptsensorConfigSensor1Alarm1 = _InSeptsensorConfigSensor1Alarm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 3, 5)
)


class _InSeptsensorConfigSensor1Alarm1Name_Type(DisplayString):
    """Custom type inSeptsensorConfigSensor1Alarm1Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_InSeptsensorConfigSensor1Alarm1Name_Type.__name__ = "DisplayString"
_InSeptsensorConfigSensor1Alarm1Name_Object = MibScalar
inSeptsensorConfigSensor1Alarm1Name = _InSeptsensorConfigSensor1Alarm1Name_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 3, 5, 1),
    _InSeptsensorConfigSensor1Alarm1Name_Type()
)
inSeptsensorConfigSensor1Alarm1Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor1Alarm1Name.setStatus("mandatory")


class _InSeptsensorConfigSensor1Alarm1State_Type(Integer32):
    """Custom type inSeptsensorConfigSensor1Alarm1State based on Integer32"""
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
        *(("disabled", 1),
          ("highActive", 4),
          ("lowActive", 5),
          ("normalClose", 3),
          ("normalOpen", 2))
    )


_InSeptsensorConfigSensor1Alarm1State_Type.__name__ = "Integer32"
_InSeptsensorConfigSensor1Alarm1State_Object = MibScalar
inSeptsensorConfigSensor1Alarm1State = _InSeptsensorConfigSensor1Alarm1State_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 3, 5, 2),
    _InSeptsensorConfigSensor1Alarm1State_Type()
)
inSeptsensorConfigSensor1Alarm1State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor1Alarm1State.setStatus("mandatory")
_InSeptsensorConfigSensor1Alarm1Hysteresis_Type = Integer32
_InSeptsensorConfigSensor1Alarm1Hysteresis_Object = MibScalar
inSeptsensorConfigSensor1Alarm1Hysteresis = _InSeptsensorConfigSensor1Alarm1Hysteresis_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 3, 5, 3),
    _InSeptsensorConfigSensor1Alarm1Hysteresis_Type()
)
inSeptsensorConfigSensor1Alarm1Hysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor1Alarm1Hysteresis.setStatus("mandatory")
_InSeptsensorConfigSensor1Alarm2_ObjectIdentity = ObjectIdentity
inSeptsensorConfigSensor1Alarm2 = _InSeptsensorConfigSensor1Alarm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 3, 6)
)


class _InSeptsensorConfigSensor1Alarm2Name_Type(DisplayString):
    """Custom type inSeptsensorConfigSensor1Alarm2Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_InSeptsensorConfigSensor1Alarm2Name_Type.__name__ = "DisplayString"
_InSeptsensorConfigSensor1Alarm2Name_Object = MibScalar
inSeptsensorConfigSensor1Alarm2Name = _InSeptsensorConfigSensor1Alarm2Name_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 3, 6, 1),
    _InSeptsensorConfigSensor1Alarm2Name_Type()
)
inSeptsensorConfigSensor1Alarm2Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor1Alarm2Name.setStatus("mandatory")


class _InSeptsensorConfigSensor1Alarm2State_Type(Integer32):
    """Custom type inSeptsensorConfigSensor1Alarm2State based on Integer32"""
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
        *(("disabled", 1),
          ("highActive", 4),
          ("lowActive", 5),
          ("normalClose", 3),
          ("normalOpen", 2))
    )


_InSeptsensorConfigSensor1Alarm2State_Type.__name__ = "Integer32"
_InSeptsensorConfigSensor1Alarm2State_Object = MibScalar
inSeptsensorConfigSensor1Alarm2State = _InSeptsensorConfigSensor1Alarm2State_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 3, 6, 2),
    _InSeptsensorConfigSensor1Alarm2State_Type()
)
inSeptsensorConfigSensor1Alarm2State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor1Alarm2State.setStatus("mandatory")
_InSeptsensorConfigSensor1Alarm2Hysteresis_Type = Integer32
_InSeptsensorConfigSensor1Alarm2Hysteresis_Object = MibScalar
inSeptsensorConfigSensor1Alarm2Hysteresis = _InSeptsensorConfigSensor1Alarm2Hysteresis_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 3, 6, 3),
    _InSeptsensorConfigSensor1Alarm2Hysteresis_Type()
)
inSeptsensorConfigSensor1Alarm2Hysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor1Alarm2Hysteresis.setStatus("mandatory")
_InSeptsensorConfigSensor2_ObjectIdentity = ObjectIdentity
inSeptsensorConfigSensor2 = _InSeptsensorConfigSensor2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 4)
)


class _InSeptsensorConfigSensor2DeviceName_Type(DisplayString):
    """Custom type inSeptsensorConfigSensor2DeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_InSeptsensorConfigSensor2DeviceName_Type.__name__ = "DisplayString"
_InSeptsensorConfigSensor2DeviceName_Object = MibScalar
inSeptsensorConfigSensor2DeviceName = _InSeptsensorConfigSensor2DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 4, 1),
    _InSeptsensorConfigSensor2DeviceName_Type()
)
inSeptsensorConfigSensor2DeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor2DeviceName.setStatus("mandatory")


class _InSeptsensorConfigSensor2DeviceState_Type(Integer32):
    """Custom type inSeptsensorConfigSensor2DeviceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("disabled", 1))
    )


_InSeptsensorConfigSensor2DeviceState_Type.__name__ = "Integer32"
_InSeptsensorConfigSensor2DeviceState_Object = MibScalar
inSeptsensorConfigSensor2DeviceState = _InSeptsensorConfigSensor2DeviceState_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 4, 2),
    _InSeptsensorConfigSensor2DeviceState_Type()
)
inSeptsensorConfigSensor2DeviceState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor2DeviceState.setStatus("mandatory")
_InSeptsensorConfigSensor2Temperature_ObjectIdentity = ObjectIdentity
inSeptsensorConfigSensor2Temperature = _InSeptsensorConfigSensor2Temperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 4, 3)
)


class _InSeptsensorConfigSensor2TemperatureName_Type(DisplayString):
    """Custom type inSeptsensorConfigSensor2TemperatureName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_InSeptsensorConfigSensor2TemperatureName_Type.__name__ = "DisplayString"
_InSeptsensorConfigSensor2TemperatureName_Object = MibScalar
inSeptsensorConfigSensor2TemperatureName = _InSeptsensorConfigSensor2TemperatureName_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 4, 3, 1),
    _InSeptsensorConfigSensor2TemperatureName_Type()
)
inSeptsensorConfigSensor2TemperatureName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor2TemperatureName.setStatus("mandatory")
_InSeptsensorConfigSensor2TemperatureLowWarning_Type = Integer32
_InSeptsensorConfigSensor2TemperatureLowWarning_Object = MibScalar
inSeptsensorConfigSensor2TemperatureLowWarning = _InSeptsensorConfigSensor2TemperatureLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 4, 3, 2),
    _InSeptsensorConfigSensor2TemperatureLowWarning_Type()
)
inSeptsensorConfigSensor2TemperatureLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor2TemperatureLowWarning.setStatus("mandatory")
_InSeptsensorConfigSensor2TemperatureLowCritical_Type = Integer32
_InSeptsensorConfigSensor2TemperatureLowCritical_Object = MibScalar
inSeptsensorConfigSensor2TemperatureLowCritical = _InSeptsensorConfigSensor2TemperatureLowCritical_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 4, 3, 3),
    _InSeptsensorConfigSensor2TemperatureLowCritical_Type()
)
inSeptsensorConfigSensor2TemperatureLowCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor2TemperatureLowCritical.setStatus("mandatory")
_InSeptsensorConfigSensor2TemperatureHighWarning_Type = Integer32
_InSeptsensorConfigSensor2TemperatureHighWarning_Object = MibScalar
inSeptsensorConfigSensor2TemperatureHighWarning = _InSeptsensorConfigSensor2TemperatureHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 4, 3, 4),
    _InSeptsensorConfigSensor2TemperatureHighWarning_Type()
)
inSeptsensorConfigSensor2TemperatureHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor2TemperatureHighWarning.setStatus("mandatory")
_InSeptsensorConfigSensor2TemperatureHighCritical_Type = Integer32
_InSeptsensorConfigSensor2TemperatureHighCritical_Object = MibScalar
inSeptsensorConfigSensor2TemperatureHighCritical = _InSeptsensorConfigSensor2TemperatureHighCritical_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 4, 3, 5),
    _InSeptsensorConfigSensor2TemperatureHighCritical_Type()
)
inSeptsensorConfigSensor2TemperatureHighCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor2TemperatureHighCritical.setStatus("mandatory")
_InSeptsensorConfigSensor2TemperatureHysteresis_Type = Integer32
_InSeptsensorConfigSensor2TemperatureHysteresis_Object = MibScalar
inSeptsensorConfigSensor2TemperatureHysteresis = _InSeptsensorConfigSensor2TemperatureHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 4, 3, 6),
    _InSeptsensorConfigSensor2TemperatureHysteresis_Type()
)
inSeptsensorConfigSensor2TemperatureHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor2TemperatureHysteresis.setStatus("mandatory")


class _InSeptsensorConfigSensor2TemperatureCalibration_Type(Integer32):
    """Custom type inSeptsensorConfigSensor2TemperatureCalibration based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("temperatureIncrease0Point0", 1),
          ("temperatureIncrease0Point5", 2),
          ("temperatureIncrease1Point0", 3),
          ("temperatureIncrease1Point5", 4),
          ("temperatureIncrease2Point0", 5),
          ("temperatureIncrease2Point5", 6),
          ("temperatureIncrease3Point0", 7),
          ("temperatureMinus0Point5", 8),
          ("temperatureMinus1Point0", 9),
          ("temperatureMinus1Point5", 10),
          ("temperatureMinus2Point0", 11),
          ("temperatureMinus2Point5", 12),
          ("temperatureMinusPoint0", 13))
    )


_InSeptsensorConfigSensor2TemperatureCalibration_Type.__name__ = "Integer32"
_InSeptsensorConfigSensor2TemperatureCalibration_Object = MibScalar
inSeptsensorConfigSensor2TemperatureCalibration = _InSeptsensorConfigSensor2TemperatureCalibration_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 4, 3, 7),
    _InSeptsensorConfigSensor2TemperatureCalibration_Type()
)
inSeptsensorConfigSensor2TemperatureCalibration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor2TemperatureCalibration.setStatus("mandatory")


class _InSeptsensorConfigSensor2TemperatureLowWarningStatus_Type(Integer32):
    """Custom type inSeptsensorConfigSensor2TemperatureLowWarningStatus based on Integer32"""
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


_InSeptsensorConfigSensor2TemperatureLowWarningStatus_Type.__name__ = "Integer32"
_InSeptsensorConfigSensor2TemperatureLowWarningStatus_Object = MibScalar
inSeptsensorConfigSensor2TemperatureLowWarningStatus = _InSeptsensorConfigSensor2TemperatureLowWarningStatus_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 4, 3, 8),
    _InSeptsensorConfigSensor2TemperatureLowWarningStatus_Type()
)
inSeptsensorConfigSensor2TemperatureLowWarningStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor2TemperatureLowWarningStatus.setStatus("mandatory")


class _InSeptsensorConfigSensor2TemperatureLowCriticalStatus_Type(Integer32):
    """Custom type inSeptsensorConfigSensor2TemperatureLowCriticalStatus based on Integer32"""
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


_InSeptsensorConfigSensor2TemperatureLowCriticalStatus_Type.__name__ = "Integer32"
_InSeptsensorConfigSensor2TemperatureLowCriticalStatus_Object = MibScalar
inSeptsensorConfigSensor2TemperatureLowCriticalStatus = _InSeptsensorConfigSensor2TemperatureLowCriticalStatus_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 4, 3, 9),
    _InSeptsensorConfigSensor2TemperatureLowCriticalStatus_Type()
)
inSeptsensorConfigSensor2TemperatureLowCriticalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor2TemperatureLowCriticalStatus.setStatus("mandatory")


class _InSeptsensorConfigSensor2TemperatureHighWarningStatus_Type(Integer32):
    """Custom type inSeptsensorConfigSensor2TemperatureHighWarningStatus based on Integer32"""
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


_InSeptsensorConfigSensor2TemperatureHighWarningStatus_Type.__name__ = "Integer32"
_InSeptsensorConfigSensor2TemperatureHighWarningStatus_Object = MibScalar
inSeptsensorConfigSensor2TemperatureHighWarningStatus = _InSeptsensorConfigSensor2TemperatureHighWarningStatus_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 4, 3, 10),
    _InSeptsensorConfigSensor2TemperatureHighWarningStatus_Type()
)
inSeptsensorConfigSensor2TemperatureHighWarningStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor2TemperatureHighWarningStatus.setStatus("mandatory")


class _InSeptsensorConfigSensor2TemperatureHighCriticalStatus_Type(Integer32):
    """Custom type inSeptsensorConfigSensor2TemperatureHighCriticalStatus based on Integer32"""
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


_InSeptsensorConfigSensor2TemperatureHighCriticalStatus_Type.__name__ = "Integer32"
_InSeptsensorConfigSensor2TemperatureHighCriticalStatus_Object = MibScalar
inSeptsensorConfigSensor2TemperatureHighCriticalStatus = _InSeptsensorConfigSensor2TemperatureHighCriticalStatus_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 4, 3, 11),
    _InSeptsensorConfigSensor2TemperatureHighCriticalStatus_Type()
)
inSeptsensorConfigSensor2TemperatureHighCriticalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor2TemperatureHighCriticalStatus.setStatus("mandatory")
_InSeptsensorConfigSensor2Humidity_ObjectIdentity = ObjectIdentity
inSeptsensorConfigSensor2Humidity = _InSeptsensorConfigSensor2Humidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 4, 4)
)


class _InSeptsensorConfigSensor2HumdityName_Type(DisplayString):
    """Custom type inSeptsensorConfigSensor2HumdityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_InSeptsensorConfigSensor2HumdityName_Type.__name__ = "DisplayString"
_InSeptsensorConfigSensor2HumdityName_Object = MibScalar
inSeptsensorConfigSensor2HumdityName = _InSeptsensorConfigSensor2HumdityName_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 4, 4, 1),
    _InSeptsensorConfigSensor2HumdityName_Type()
)
inSeptsensorConfigSensor2HumdityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor2HumdityName.setStatus("mandatory")
_InSeptsensorConfigSensor2HumidityLowWarning_Type = Integer32
_InSeptsensorConfigSensor2HumidityLowWarning_Object = MibScalar
inSeptsensorConfigSensor2HumidityLowWarning = _InSeptsensorConfigSensor2HumidityLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 4, 4, 2),
    _InSeptsensorConfigSensor2HumidityLowWarning_Type()
)
inSeptsensorConfigSensor2HumidityLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor2HumidityLowWarning.setStatus("mandatory")
_InSeptsensorConfigSensor2HumidityLowCritical_Type = Integer32
_InSeptsensorConfigSensor2HumidityLowCritical_Object = MibScalar
inSeptsensorConfigSensor2HumidityLowCritical = _InSeptsensorConfigSensor2HumidityLowCritical_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 4, 4, 3),
    _InSeptsensorConfigSensor2HumidityLowCritical_Type()
)
inSeptsensorConfigSensor2HumidityLowCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor2HumidityLowCritical.setStatus("mandatory")
_InSeptsensorConfigSensor2HumidityHighWarning_Type = Integer32
_InSeptsensorConfigSensor2HumidityHighWarning_Object = MibScalar
inSeptsensorConfigSensor2HumidityHighWarning = _InSeptsensorConfigSensor2HumidityHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 4, 4, 4),
    _InSeptsensorConfigSensor2HumidityHighWarning_Type()
)
inSeptsensorConfigSensor2HumidityHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor2HumidityHighWarning.setStatus("mandatory")
_InSeptsensorConfigSensor2HumidityHighCritical_Type = Integer32
_InSeptsensorConfigSensor2HumidityHighCritical_Object = MibScalar
inSeptsensorConfigSensor2HumidityHighCritical = _InSeptsensorConfigSensor2HumidityHighCritical_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 4, 4, 5),
    _InSeptsensorConfigSensor2HumidityHighCritical_Type()
)
inSeptsensorConfigSensor2HumidityHighCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor2HumidityHighCritical.setStatus("mandatory")
_InSeptsensorConfigSensor2HumidityHysteresis_Type = Integer32
_InSeptsensorConfigSensor2HumidityHysteresis_Object = MibScalar
inSeptsensorConfigSensor2HumidityHysteresis = _InSeptsensorConfigSensor2HumidityHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 4, 4, 6),
    _InSeptsensorConfigSensor2HumidityHysteresis_Type()
)
inSeptsensorConfigSensor2HumidityHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor2HumidityHysteresis.setStatus("mandatory")


class _InSeptsensorConfigSensor2HumidityCalibration_Type(Integer32):
    """Custom type inSeptsensorConfigSensor2HumidityCalibration based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("humidityIncrease0Point0", 1),
          ("humidityIncrease1Point0", 2),
          ("humidityIncrease2Point0", 3),
          ("humidityIncrease3Point0", 4),
          ("humidityIncrease4Point0", 5),
          ("humidityIncrease5Point0", 6),
          ("humidityIncrease6Point0", 7),
          ("humidityMinus1Point0", 8),
          ("humidityMinus2Point0", 9),
          ("humidityMinus3Point0", 10),
          ("humidityMinus4Point0", 11),
          ("humidityMinus5Point0", 12),
          ("humidityMinus6Point0", 13))
    )


_InSeptsensorConfigSensor2HumidityCalibration_Type.__name__ = "Integer32"
_InSeptsensorConfigSensor2HumidityCalibration_Object = MibScalar
inSeptsensorConfigSensor2HumidityCalibration = _InSeptsensorConfigSensor2HumidityCalibration_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 4, 4, 7),
    _InSeptsensorConfigSensor2HumidityCalibration_Type()
)
inSeptsensorConfigSensor2HumidityCalibration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor2HumidityCalibration.setStatus("mandatory")


class _InSeptsensorConfigSensor2HumidityLowWarningStatus_Type(Integer32):
    """Custom type inSeptsensorConfigSensor2HumidityLowWarningStatus based on Integer32"""
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


_InSeptsensorConfigSensor2HumidityLowWarningStatus_Type.__name__ = "Integer32"
_InSeptsensorConfigSensor2HumidityLowWarningStatus_Object = MibScalar
inSeptsensorConfigSensor2HumidityLowWarningStatus = _InSeptsensorConfigSensor2HumidityLowWarningStatus_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 4, 4, 8),
    _InSeptsensorConfigSensor2HumidityLowWarningStatus_Type()
)
inSeptsensorConfigSensor2HumidityLowWarningStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor2HumidityLowWarningStatus.setStatus("mandatory")


class _InSeptsensorConfigSensor2HumidityLowCriticalStatus_Type(Integer32):
    """Custom type inSeptsensorConfigSensor2HumidityLowCriticalStatus based on Integer32"""
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


_InSeptsensorConfigSensor2HumidityLowCriticalStatus_Type.__name__ = "Integer32"
_InSeptsensorConfigSensor2HumidityLowCriticalStatus_Object = MibScalar
inSeptsensorConfigSensor2HumidityLowCriticalStatus = _InSeptsensorConfigSensor2HumidityLowCriticalStatus_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 4, 4, 9),
    _InSeptsensorConfigSensor2HumidityLowCriticalStatus_Type()
)
inSeptsensorConfigSensor2HumidityLowCriticalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor2HumidityLowCriticalStatus.setStatus("mandatory")


class _InSeptsensorConfigSensor2HumidityHighWarningStatus_Type(Integer32):
    """Custom type inSeptsensorConfigSensor2HumidityHighWarningStatus based on Integer32"""
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


_InSeptsensorConfigSensor2HumidityHighWarningStatus_Type.__name__ = "Integer32"
_InSeptsensorConfigSensor2HumidityHighWarningStatus_Object = MibScalar
inSeptsensorConfigSensor2HumidityHighWarningStatus = _InSeptsensorConfigSensor2HumidityHighWarningStatus_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 4, 4, 10),
    _InSeptsensorConfigSensor2HumidityHighWarningStatus_Type()
)
inSeptsensorConfigSensor2HumidityHighWarningStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor2HumidityHighWarningStatus.setStatus("mandatory")


class _InSeptsensorConfigSensor2HumidityHighCriticalStatus_Type(Integer32):
    """Custom type inSeptsensorConfigSensor2HumidityHighCriticalStatus based on Integer32"""
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


_InSeptsensorConfigSensor2HumidityHighCriticalStatus_Type.__name__ = "Integer32"
_InSeptsensorConfigSensor2HumidityHighCriticalStatus_Object = MibScalar
inSeptsensorConfigSensor2HumidityHighCriticalStatus = _InSeptsensorConfigSensor2HumidityHighCriticalStatus_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 4, 4, 11),
    _InSeptsensorConfigSensor2HumidityHighCriticalStatus_Type()
)
inSeptsensorConfigSensor2HumidityHighCriticalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor2HumidityHighCriticalStatus.setStatus("mandatory")
_InSeptsensorConfigSensor2Alarm1_ObjectIdentity = ObjectIdentity
inSeptsensorConfigSensor2Alarm1 = _InSeptsensorConfigSensor2Alarm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 4, 5)
)


class _InSeptsensorConfigSensor2Alarm1Name_Type(DisplayString):
    """Custom type inSeptsensorConfigSensor2Alarm1Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_InSeptsensorConfigSensor2Alarm1Name_Type.__name__ = "DisplayString"
_InSeptsensorConfigSensor2Alarm1Name_Object = MibScalar
inSeptsensorConfigSensor2Alarm1Name = _InSeptsensorConfigSensor2Alarm1Name_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 4, 5, 1),
    _InSeptsensorConfigSensor2Alarm1Name_Type()
)
inSeptsensorConfigSensor2Alarm1Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor2Alarm1Name.setStatus("mandatory")


class _InSeptsensorConfigSensor2Alarm1State_Type(Integer32):
    """Custom type inSeptsensorConfigSensor2Alarm1State based on Integer32"""
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
        *(("disabled", 1),
          ("highActive", 4),
          ("lowActive", 5),
          ("normalClose", 3),
          ("normalOpen", 2))
    )


_InSeptsensorConfigSensor2Alarm1State_Type.__name__ = "Integer32"
_InSeptsensorConfigSensor2Alarm1State_Object = MibScalar
inSeptsensorConfigSensor2Alarm1State = _InSeptsensorConfigSensor2Alarm1State_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 4, 5, 2),
    _InSeptsensorConfigSensor2Alarm1State_Type()
)
inSeptsensorConfigSensor2Alarm1State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor2Alarm1State.setStatus("mandatory")
_InSeptsensorConfigSensor2Alarm1Hysteresis_Type = Integer32
_InSeptsensorConfigSensor2Alarm1Hysteresis_Object = MibScalar
inSeptsensorConfigSensor2Alarm1Hysteresis = _InSeptsensorConfigSensor2Alarm1Hysteresis_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 4, 5, 3),
    _InSeptsensorConfigSensor2Alarm1Hysteresis_Type()
)
inSeptsensorConfigSensor2Alarm1Hysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor2Alarm1Hysteresis.setStatus("mandatory")
_InSeptsensorConfigSensor2Alarm2_ObjectIdentity = ObjectIdentity
inSeptsensorConfigSensor2Alarm2 = _InSeptsensorConfigSensor2Alarm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 4, 6)
)


class _InSeptsensorConfigSensor2Alarm2Name_Type(DisplayString):
    """Custom type inSeptsensorConfigSensor2Alarm2Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_InSeptsensorConfigSensor2Alarm2Name_Type.__name__ = "DisplayString"
_InSeptsensorConfigSensor2Alarm2Name_Object = MibScalar
inSeptsensorConfigSensor2Alarm2Name = _InSeptsensorConfigSensor2Alarm2Name_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 4, 6, 1),
    _InSeptsensorConfigSensor2Alarm2Name_Type()
)
inSeptsensorConfigSensor2Alarm2Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor2Alarm2Name.setStatus("mandatory")


class _InSeptsensorConfigSensor2Alarm2State_Type(Integer32):
    """Custom type inSeptsensorConfigSensor2Alarm2State based on Integer32"""
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
        *(("disabled", 1),
          ("highActive", 4),
          ("lowActive", 5),
          ("normalClose", 3),
          ("normalOpen", 2))
    )


_InSeptsensorConfigSensor2Alarm2State_Type.__name__ = "Integer32"
_InSeptsensorConfigSensor2Alarm2State_Object = MibScalar
inSeptsensorConfigSensor2Alarm2State = _InSeptsensorConfigSensor2Alarm2State_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 4, 6, 2),
    _InSeptsensorConfigSensor2Alarm2State_Type()
)
inSeptsensorConfigSensor2Alarm2State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor2Alarm2State.setStatus("mandatory")
_InSeptsensorConfigSensor2Alarm2Hysteresis_Type = Integer32
_InSeptsensorConfigSensor2Alarm2Hysteresis_Object = MibScalar
inSeptsensorConfigSensor2Alarm2Hysteresis = _InSeptsensorConfigSensor2Alarm2Hysteresis_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 1, 4, 4, 6, 3),
    _InSeptsensorConfigSensor2Alarm2Hysteresis_Type()
)
inSeptsensorConfigSensor2Alarm2Hysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSeptsensorConfigSensor2Alarm2Hysteresis.setStatus("mandatory")
_InSeptTraps_ObjectIdentity = ObjectIdentity
inSeptTraps = _InSeptTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 2)
)

# Managed Objects groups


# Notification objects

inSeptCommunicationRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 2, 0, 1)
)
if mibBuilder.loadTexts:
    inSeptCommunicationRestored.setStatus(
        ""
    )

inSeptCommunicationLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 2, 0, 2)
)
if mibBuilder.loadTexts:
    inSeptCommunicationLost.setStatus(
        ""
    )

inSeptAlarm1Inactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 2, 0, 3)
)
if mibBuilder.loadTexts:
    inSeptAlarm1Inactive.setStatus(
        ""
    )

inSeptAlarm1Active = NotificationType(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 2, 0, 4)
)
if mibBuilder.loadTexts:
    inSeptAlarm1Active.setStatus(
        ""
    )

inSeptAlarm2Inactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 2, 0, 5)
)
if mibBuilder.loadTexts:
    inSeptAlarm2Inactive.setStatus(
        ""
    )

inSeptAlarm2Active = NotificationType(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 2, 0, 6)
)
if mibBuilder.loadTexts:
    inSeptAlarm2Active.setStatus(
        ""
    )

inSeptTemperatureNotHighWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 2, 0, 7)
)
if mibBuilder.loadTexts:
    inSeptTemperatureNotHighWarning.setStatus(
        ""
    )

inSeptTemperatureHighWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 2, 0, 8)
)
if mibBuilder.loadTexts:
    inSeptTemperatureHighWarning.setStatus(
        ""
    )

inSeptTemperatureNotLowWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 2, 0, 9)
)
if mibBuilder.loadTexts:
    inSeptTemperatureNotLowWarning.setStatus(
        ""
    )

inSeptTemperatureLowWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 2, 0, 10)
)
if mibBuilder.loadTexts:
    inSeptTemperatureLowWarning.setStatus(
        ""
    )

inSeptTemperatureNotHighCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 2, 0, 11)
)
if mibBuilder.loadTexts:
    inSeptTemperatureNotHighCritical.setStatus(
        ""
    )

inSeptTemperatureHighCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 2, 0, 12)
)
if mibBuilder.loadTexts:
    inSeptTemperatureHighCritical.setStatus(
        ""
    )

inSeptTemperatureNotLowCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 2, 0, 13)
)
if mibBuilder.loadTexts:
    inSeptTemperatureNotLowCritical.setStatus(
        ""
    )

inSeptTemperatureLowCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 2, 0, 14)
)
if mibBuilder.loadTexts:
    inSeptTemperatureLowCritical.setStatus(
        ""
    )

inSeptHumidityNotHighWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 2, 0, 15)
)
if mibBuilder.loadTexts:
    inSeptHumidityNotHighWarning.setStatus(
        ""
    )

inSeptHumidityHighWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 2, 0, 16)
)
if mibBuilder.loadTexts:
    inSeptHumidityHighWarning.setStatus(
        ""
    )

inSeptHumidityNotLowWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 2, 0, 17)
)
if mibBuilder.loadTexts:
    inSeptHumidityNotLowWarning.setStatus(
        ""
    )

inSeptHumidityLowWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 2, 0, 18)
)
if mibBuilder.loadTexts:
    inSeptHumidityLowWarning.setStatus(
        ""
    )

inSeptHumidityNotHighCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 2, 0, 19)
)
if mibBuilder.loadTexts:
    inSeptHumidityNotHighCritical.setStatus(
        ""
    )

inSeptHumidityHighCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 2, 0, 20)
)
if mibBuilder.loadTexts:
    inSeptHumidityHighCritical.setStatus(
        ""
    )

inSeptHumidityNotLowCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 2, 0, 21)
)
if mibBuilder.loadTexts:
    inSeptHumidityNotLowCritical.setStatus(
        ""
    )

inSeptHumidityLowCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 1, 2, 0, 22)
)
if mibBuilder.loadTexts:
    inSeptHumidityLowCritical.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "InterSeptor-MIB",
    **{"jacarta": jacarta,
       "product": product,
       "webAppliance": webAppliance,
       "inSept": inSept,
       "inSeptObjects": inSeptObjects,
       "inSeptIdent": inSeptIdent,
       "inSeptIdentManufacturer": inSeptIdentManufacturer,
       "inSeptIdentModel": inSeptIdentModel,
       "inSeptIdentAgentSoftwareVersion": inSeptIdentAgentSoftwareVersion,
       "inSeptIdentName": inSeptIdentName,
       "inSeptConfig": inSeptConfig,
       "inSeptConfigMibVersion": inSeptConfigMibVersion,
       "inSeptConfigNetwork": inSeptConfigNetwork,
       "inSeptConfigIpAddress": inSeptConfigIpAddress,
       "inSeptConfigGateway": inSeptConfigGateway,
       "inSeptConfigSubnetMask": inSeptConfigSubnetMask,
       "inSeptConfigDateTime": inSeptConfigDateTime,
       "inSeptConfigDate": inSeptConfigDate,
       "inSeptConfigTime": inSeptConfigTime,
       "inSeptConfigTimeFromNtp": inSeptConfigTimeFromNtp,
       "inSeptConfigNtpIpAddress": inSeptConfigNtpIpAddress,
       "inSeptConfigNtpTimeZone": inSeptConfigNtpTimeZone,
       "inSeptConfigDayLightSaving": inSeptConfigDayLightSaving,
       "inSeptConfigLog": inSeptConfigLog,
       "inSeptConfigHistoryLogFrequency": inSeptConfigHistoryLogFrequency,
       "inSeptConfigExtHistoryLogFrequency": inSeptConfigExtHistoryLogFrequency,
       "inSeptConfigConfigurationLog": inSeptConfigConfigurationLog,
       "inSeptConfigDhcpStatue": inSeptConfigDhcpStatue,
       "inSeptConfigPingStatue": inSeptConfigPingStatue,
       "inSeptConfigTftpStatue": inSeptConfigTftpStatue,
       "inSeptConfigTelnet": inSeptConfigTelnet,
       "inSeptConfigTelnetStatue": inSeptConfigTelnetStatue,
       "inSeptConfigTelnetPortNumber": inSeptConfigTelnetPortNumber,
       "inSeptConfigHttp": inSeptConfigHttp,
       "inSeptConfigHttpStatue": inSeptConfigHttpStatue,
       "inSeptConfigHttpPortNumber": inSeptConfigHttpPortNumber,
       "inSeptConfigHttpSecurity": inSeptConfigHttpSecurity,
       "inSeptConfigSnmp": inSeptConfigSnmp,
       "inSeptConfigSnmpStatue": inSeptConfigSnmpStatue,
       "inSeptConfigSnmpPortNumber": inSeptConfigSnmpPortNumber,
       "inSeptConfigControl": inSeptConfigControl,
       "inSeptConfigResetToDefault": inSeptConfigResetToDefault,
       "inSeptConfigRestart": inSeptConfigRestart,
       "inSeptConfigTrap": inSeptConfigTrap,
       "inSeptConfigTrapRetryCount": inSeptConfigTrapRetryCount,
       "inSeptConfigTrapRetryTime": inSeptConfigTrapRetryTime,
       "inSeptConfigTrapAckSignature": inSeptConfigTrapAckSignature,
       "inSeptConfigPollRate": inSeptConfigPollRate,
       "inSeptConfigTrapsReceiversTable": inSeptConfigTrapsReceiversTable,
       "inSeptConfigTrapsReceiversEntry": inSeptConfigTrapsReceiversEntry,
       "inSepttrapsIndex": inSepttrapsIndex,
       "inSepttrapsReceiverAddr": inSepttrapsReceiverAddr,
       "inSeptreceiverCommunityString": inSeptreceiverCommunityString,
       "inSeptreceiverSeverityLevel": inSeptreceiverSeverityLevel,
       "inSeptreceiverDescription": inSeptreceiverDescription,
       "inSeptConfigAccessControlTable": inSeptConfigAccessControlTable,
       "inSeptConfigAccessControlEntry": inSeptConfigAccessControlEntry,
       "accessIndex": accessIndex,
       "accessControlAddr": accessControlAddr,
       "accessCommunityString": accessCommunityString,
       "accessControlMode": accessControlMode,
       "inSeptConfigTemperatureUnit": inSeptConfigTemperatureUnit,
       "inSeptConfigDateFormat": inSeptConfigDateFormat,
       "inSeptsensorMonitor": inSeptsensorMonitor,
       "inSeptsensorMonitorSensorNumber": inSeptsensorMonitorSensorNumber,
       "inSeptsensorMonitorSensorTable": inSeptsensorMonitorSensorTable,
       "inSeptsensorMonitorSensorEntry": inSeptsensorMonitorSensorEntry,
       "inSeptsensorMonitorDeviceIndex": inSeptsensorMonitorDeviceIndex,
       "inSeptsensorMonitorDeviceStatus": inSeptsensorMonitorDeviceStatus,
       "inSeptsensorMonitorDeviceTemperature": inSeptsensorMonitorDeviceTemperature,
       "inSeptsensorMonitorDeviceTemperatureAlarm": inSeptsensorMonitorDeviceTemperatureAlarm,
       "inSeptsensorMonitorDeviceHumidity": inSeptsensorMonitorDeviceHumidity,
       "inSeptsensorMonitorDeviceHumidityAlarm": inSeptsensorMonitorDeviceHumidityAlarm,
       "inSeptsensorMonitorAlarm1": inSeptsensorMonitorAlarm1,
       "inSeptsensorMonitorAlarm2": inSeptsensorMonitorAlarm2,
       "inSeptsensorConfig": inSeptsensorConfig,
       "inSeptsensorConfigSensorNumber": inSeptsensorConfigSensorNumber,
       "inSeptsensorConfigSensorTable": inSeptsensorConfigSensorTable,
       "inSeptsensorConfigSensorEntry": inSeptsensorConfigSensorEntry,
       "inSeptsensorConfigDeviceIndex": inSeptsensorConfigDeviceIndex,
       "inSeptsensorConfigDeviceName": inSeptsensorConfigDeviceName,
       "inSeptsensorConfigDeviceState": inSeptsensorConfigDeviceState,
       "inSeptsensorConfigSensor1": inSeptsensorConfigSensor1,
       "inSeptsensorConfigSensor1DeviceName": inSeptsensorConfigSensor1DeviceName,
       "inSeptsensorConfigSensor1DeviceState": inSeptsensorConfigSensor1DeviceState,
       "inSeptsensorConfigSensor1Temperature": inSeptsensorConfigSensor1Temperature,
       "inSeptsensorConfigSensor1TemperatureName": inSeptsensorConfigSensor1TemperatureName,
       "inSeptsensorConfigSensor1TemperatureLowWarning": inSeptsensorConfigSensor1TemperatureLowWarning,
       "inSeptsensorConfigSensor1TemperatureLowCritical": inSeptsensorConfigSensor1TemperatureLowCritical,
       "inSeptsensorConfigSensor1TemperatureHighWarning": inSeptsensorConfigSensor1TemperatureHighWarning,
       "inSeptsensorConfigSensor1TemperatureHighCritical": inSeptsensorConfigSensor1TemperatureHighCritical,
       "inSeptsensorConfigSensor1TemperatureHysteresis": inSeptsensorConfigSensor1TemperatureHysteresis,
       "inSeptsensorConfigSensor1TemperatureCalibration": inSeptsensorConfigSensor1TemperatureCalibration,
       "inSeptsensorConfigSensor1TemperatureLowWarningStatus": inSeptsensorConfigSensor1TemperatureLowWarningStatus,
       "inSeptsensorConfigSensor1TemperatureLowCriticalStatus": inSeptsensorConfigSensor1TemperatureLowCriticalStatus,
       "inSeptsensorConfigSensor1TemperatureHighWarningStatus": inSeptsensorConfigSensor1TemperatureHighWarningStatus,
       "inSeptsensorConfigSensor1TemperatureHighCriticalStatus": inSeptsensorConfigSensor1TemperatureHighCriticalStatus,
       "inSeptsensorConfigSensor1Humidity": inSeptsensorConfigSensor1Humidity,
       "inSeptsensorConfigSensor1HumdityName": inSeptsensorConfigSensor1HumdityName,
       "inSeptsensorConfigSensor1HumidityLowWarning": inSeptsensorConfigSensor1HumidityLowWarning,
       "inSeptsensorConfigSensor1HumidityLowCritical": inSeptsensorConfigSensor1HumidityLowCritical,
       "inSeptsensorConfigSensor1HumidityHighWarning": inSeptsensorConfigSensor1HumidityHighWarning,
       "inSeptsensorConfigSensor1HumidityHighCritical": inSeptsensorConfigSensor1HumidityHighCritical,
       "inSeptsensorConfigSensor1HumidityHysteresis": inSeptsensorConfigSensor1HumidityHysteresis,
       "inSeptsensorConfigSensor1HumidityCalibration": inSeptsensorConfigSensor1HumidityCalibration,
       "inSeptsensorConfigSensor1HumidityLowWarningStatus": inSeptsensorConfigSensor1HumidityLowWarningStatus,
       "inSeptsensorConfigSensor1HumidityLowCriticalStatus": inSeptsensorConfigSensor1HumidityLowCriticalStatus,
       "inSeptsensorConfigSensor1HumidityHighWarningStatus": inSeptsensorConfigSensor1HumidityHighWarningStatus,
       "inSeptsensorConfigSensor1HumidityHighCriticalStatus": inSeptsensorConfigSensor1HumidityHighCriticalStatus,
       "inSeptsensorConfigSensor1Alarm1": inSeptsensorConfigSensor1Alarm1,
       "inSeptsensorConfigSensor1Alarm1Name": inSeptsensorConfigSensor1Alarm1Name,
       "inSeptsensorConfigSensor1Alarm1State": inSeptsensorConfigSensor1Alarm1State,
       "inSeptsensorConfigSensor1Alarm1Hysteresis": inSeptsensorConfigSensor1Alarm1Hysteresis,
       "inSeptsensorConfigSensor1Alarm2": inSeptsensorConfigSensor1Alarm2,
       "inSeptsensorConfigSensor1Alarm2Name": inSeptsensorConfigSensor1Alarm2Name,
       "inSeptsensorConfigSensor1Alarm2State": inSeptsensorConfigSensor1Alarm2State,
       "inSeptsensorConfigSensor1Alarm2Hysteresis": inSeptsensorConfigSensor1Alarm2Hysteresis,
       "inSeptsensorConfigSensor2": inSeptsensorConfigSensor2,
       "inSeptsensorConfigSensor2DeviceName": inSeptsensorConfigSensor2DeviceName,
       "inSeptsensorConfigSensor2DeviceState": inSeptsensorConfigSensor2DeviceState,
       "inSeptsensorConfigSensor2Temperature": inSeptsensorConfigSensor2Temperature,
       "inSeptsensorConfigSensor2TemperatureName": inSeptsensorConfigSensor2TemperatureName,
       "inSeptsensorConfigSensor2TemperatureLowWarning": inSeptsensorConfigSensor2TemperatureLowWarning,
       "inSeptsensorConfigSensor2TemperatureLowCritical": inSeptsensorConfigSensor2TemperatureLowCritical,
       "inSeptsensorConfigSensor2TemperatureHighWarning": inSeptsensorConfigSensor2TemperatureHighWarning,
       "inSeptsensorConfigSensor2TemperatureHighCritical": inSeptsensorConfigSensor2TemperatureHighCritical,
       "inSeptsensorConfigSensor2TemperatureHysteresis": inSeptsensorConfigSensor2TemperatureHysteresis,
       "inSeptsensorConfigSensor2TemperatureCalibration": inSeptsensorConfigSensor2TemperatureCalibration,
       "inSeptsensorConfigSensor2TemperatureLowWarningStatus": inSeptsensorConfigSensor2TemperatureLowWarningStatus,
       "inSeptsensorConfigSensor2TemperatureLowCriticalStatus": inSeptsensorConfigSensor2TemperatureLowCriticalStatus,
       "inSeptsensorConfigSensor2TemperatureHighWarningStatus": inSeptsensorConfigSensor2TemperatureHighWarningStatus,
       "inSeptsensorConfigSensor2TemperatureHighCriticalStatus": inSeptsensorConfigSensor2TemperatureHighCriticalStatus,
       "inSeptsensorConfigSensor2Humidity": inSeptsensorConfigSensor2Humidity,
       "inSeptsensorConfigSensor2HumdityName": inSeptsensorConfigSensor2HumdityName,
       "inSeptsensorConfigSensor2HumidityLowWarning": inSeptsensorConfigSensor2HumidityLowWarning,
       "inSeptsensorConfigSensor2HumidityLowCritical": inSeptsensorConfigSensor2HumidityLowCritical,
       "inSeptsensorConfigSensor2HumidityHighWarning": inSeptsensorConfigSensor2HumidityHighWarning,
       "inSeptsensorConfigSensor2HumidityHighCritical": inSeptsensorConfigSensor2HumidityHighCritical,
       "inSeptsensorConfigSensor2HumidityHysteresis": inSeptsensorConfigSensor2HumidityHysteresis,
       "inSeptsensorConfigSensor2HumidityCalibration": inSeptsensorConfigSensor2HumidityCalibration,
       "inSeptsensorConfigSensor2HumidityLowWarningStatus": inSeptsensorConfigSensor2HumidityLowWarningStatus,
       "inSeptsensorConfigSensor2HumidityLowCriticalStatus": inSeptsensorConfigSensor2HumidityLowCriticalStatus,
       "inSeptsensorConfigSensor2HumidityHighWarningStatus": inSeptsensorConfigSensor2HumidityHighWarningStatus,
       "inSeptsensorConfigSensor2HumidityHighCriticalStatus": inSeptsensorConfigSensor2HumidityHighCriticalStatus,
       "inSeptsensorConfigSensor2Alarm1": inSeptsensorConfigSensor2Alarm1,
       "inSeptsensorConfigSensor2Alarm1Name": inSeptsensorConfigSensor2Alarm1Name,
       "inSeptsensorConfigSensor2Alarm1State": inSeptsensorConfigSensor2Alarm1State,
       "inSeptsensorConfigSensor2Alarm1Hysteresis": inSeptsensorConfigSensor2Alarm1Hysteresis,
       "inSeptsensorConfigSensor2Alarm2": inSeptsensorConfigSensor2Alarm2,
       "inSeptsensorConfigSensor2Alarm2Name": inSeptsensorConfigSensor2Alarm2Name,
       "inSeptsensorConfigSensor2Alarm2State": inSeptsensorConfigSensor2Alarm2State,
       "inSeptsensorConfigSensor2Alarm2Hysteresis": inSeptsensorConfigSensor2Alarm2Hysteresis,
       "inSeptTraps": inSeptTraps,
       "inSeptCommunicationRestored": inSeptCommunicationRestored,
       "inSeptCommunicationLost": inSeptCommunicationLost,
       "inSeptAlarm1Inactive": inSeptAlarm1Inactive,
       "inSeptAlarm1Active": inSeptAlarm1Active,
       "inSeptAlarm2Inactive": inSeptAlarm2Inactive,
       "inSeptAlarm2Active": inSeptAlarm2Active,
       "inSeptTemperatureNotHighWarning": inSeptTemperatureNotHighWarning,
       "inSeptTemperatureHighWarning": inSeptTemperatureHighWarning,
       "inSeptTemperatureNotLowWarning": inSeptTemperatureNotLowWarning,
       "inSeptTemperatureLowWarning": inSeptTemperatureLowWarning,
       "inSeptTemperatureNotHighCritical": inSeptTemperatureNotHighCritical,
       "inSeptTemperatureHighCritical": inSeptTemperatureHighCritical,
       "inSeptTemperatureNotLowCritical": inSeptTemperatureNotLowCritical,
       "inSeptTemperatureLowCritical": inSeptTemperatureLowCritical,
       "inSeptHumidityNotHighWarning": inSeptHumidityNotHighWarning,
       "inSeptHumidityHighWarning": inSeptHumidityHighWarning,
       "inSeptHumidityNotLowWarning": inSeptHumidityNotLowWarning,
       "inSeptHumidityLowWarning": inSeptHumidityLowWarning,
       "inSeptHumidityNotHighCritical": inSeptHumidityNotHighCritical,
       "inSeptHumidityHighCritical": inSeptHumidityHighCritical,
       "inSeptHumidityNotLowCritical": inSeptHumidityNotLowCritical,
       "inSeptHumidityLowCritical": inSeptHumidityLowCritical}
)
