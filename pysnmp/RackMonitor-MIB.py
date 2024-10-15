# SNMP MIB module (RackMonitor-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RackMonitor-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:48:57 2024
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

_Powerware_ObjectIdentity = ObjectIdentity
powerware = _Powerware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534)
)
_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6)
)
_DataCenter_ObjectIdentity = ObjectIdentity
dataCenter = _DataCenter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 7)
)
_EnvironmentalMonitor_ObjectIdentity = ObjectIdentity
environmentalMonitor = _EnvironmentalMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1)
)
_InsObjects_ObjectIdentity = ObjectIdentity
insObjects = _InsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1)
)
_RmIdent_ObjectIdentity = ObjectIdentity
rmIdent = _RmIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 1)
)


class _InsIdentManufacturer_Type(DisplayString):
    """Custom type insIdentManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_InsIdentManufacturer_Type.__name__ = "DisplayString"
_InsIdentManufacturer_Object = MibScalar
insIdentManufacturer = _InsIdentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 1, 1),
    _InsIdentManufacturer_Type()
)
insIdentManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insIdentManufacturer.setStatus("mandatory")


class _InsIdentModel_Type(DisplayString):
    """Custom type insIdentModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_InsIdentModel_Type.__name__ = "DisplayString"
_InsIdentModel_Object = MibScalar
insIdentModel = _InsIdentModel_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 1, 2),
    _InsIdentModel_Type()
)
insIdentModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insIdentModel.setStatus("mandatory")


class _InsIdentAgentSoftwareVersion_Type(DisplayString):
    """Custom type insIdentAgentSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_InsIdentAgentSoftwareVersion_Type.__name__ = "DisplayString"
_InsIdentAgentSoftwareVersion_Object = MibScalar
insIdentAgentSoftwareVersion = _InsIdentAgentSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 1, 3),
    _InsIdentAgentSoftwareVersion_Type()
)
insIdentAgentSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insIdentAgentSoftwareVersion.setStatus("mandatory")


class _InsIdentName_Type(DisplayString):
    """Custom type insIdentName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_InsIdentName_Type.__name__ = "DisplayString"
_InsIdentName_Object = MibScalar
insIdentName = _InsIdentName_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 1, 4),
    _InsIdentName_Type()
)
insIdentName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    insIdentName.setStatus("mandatory")
_RmConfig_ObjectIdentity = ObjectIdentity
rmConfig = _RmConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2)
)
_RmConfigMibVersion_Type = Integer32
_RmConfigMibVersion_Object = MibScalar
rmConfigMibVersion = _RmConfigMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 1),
    _RmConfigMibVersion_Type()
)
rmConfigMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmConfigMibVersion.setStatus("mandatory")
_RmConfigNetwork_ObjectIdentity = ObjectIdentity
rmConfigNetwork = _RmConfigNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 2)
)
_RmConfigIpAddress_Type = IpAddress
_RmConfigIpAddress_Object = MibScalar
rmConfigIpAddress = _RmConfigIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 2, 1),
    _RmConfigIpAddress_Type()
)
rmConfigIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmConfigIpAddress.setStatus("mandatory")
_RmConfigGateway_Type = IpAddress
_RmConfigGateway_Object = MibScalar
rmConfigGateway = _RmConfigGateway_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 2, 2),
    _RmConfigGateway_Type()
)
rmConfigGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmConfigGateway.setStatus("mandatory")
_RmConfigSubnetMask_Type = IpAddress
_RmConfigSubnetMask_Object = MibScalar
rmConfigSubnetMask = _RmConfigSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 2, 3),
    _RmConfigSubnetMask_Type()
)
rmConfigSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmConfigSubnetMask.setStatus("mandatory")
_RmConfigDateTime_ObjectIdentity = ObjectIdentity
rmConfigDateTime = _RmConfigDateTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 3)
)


class _RmConfigDate_Type(DisplayString):
    """Custom type rmConfigDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_RmConfigDate_Type.__name__ = "DisplayString"
_RmConfigDate_Object = MibScalar
rmConfigDate = _RmConfigDate_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 3, 1),
    _RmConfigDate_Type()
)
rmConfigDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmConfigDate.setStatus("mandatory")


class _RmConfigTime_Type(DisplayString):
    """Custom type rmConfigTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_RmConfigTime_Type.__name__ = "DisplayString"
_RmConfigTime_Object = MibScalar
rmConfigTime = _RmConfigTime_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 3, 2),
    _RmConfigTime_Type()
)
rmConfigTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmConfigTime.setStatus("mandatory")


class _RmConfigTimeFromNtp_Type(Integer32):
    """Custom type rmConfigTimeFromNtp based on Integer32"""
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


_RmConfigTimeFromNtp_Type.__name__ = "Integer32"
_RmConfigTimeFromNtp_Object = MibScalar
rmConfigTimeFromNtp = _RmConfigTimeFromNtp_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 3, 3),
    _RmConfigTimeFromNtp_Type()
)
rmConfigTimeFromNtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmConfigTimeFromNtp.setStatus("mandatory")
_RmConfigNtpIpAddress_Type = IpAddress
_RmConfigNtpIpAddress_Object = MibScalar
rmConfigNtpIpAddress = _RmConfigNtpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 3, 4),
    _RmConfigNtpIpAddress_Type()
)
rmConfigNtpIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmConfigNtpIpAddress.setStatus("mandatory")


class _RmConfigNtpTimeZone_Type(Integer32):
    """Custom type rmConfigNtpTimeZone based on Integer32"""
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


_RmConfigNtpTimeZone_Type.__name__ = "Integer32"
_RmConfigNtpTimeZone_Object = MibScalar
rmConfigNtpTimeZone = _RmConfigNtpTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 3, 5),
    _RmConfigNtpTimeZone_Type()
)
rmConfigNtpTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmConfigNtpTimeZone.setStatus("mandatory")


class _RmConfigDayLightSaving_Type(Integer32):
    """Custom type rmConfigDayLightSaving based on Integer32"""
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


_RmConfigDayLightSaving_Type.__name__ = "Integer32"
_RmConfigDayLightSaving_Object = MibScalar
rmConfigDayLightSaving = _RmConfigDayLightSaving_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 3, 6),
    _RmConfigDayLightSaving_Type()
)
rmConfigDayLightSaving.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmConfigDayLightSaving.setStatus("mandatory")
_RmConfigLog_ObjectIdentity = ObjectIdentity
rmConfigLog = _RmConfigLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 4)
)


class _RmConfigHistoryLogFrequency_Type(Integer32):
    """Custom type rmConfigHistoryLogFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 3600),
    )


_RmConfigHistoryLogFrequency_Type.__name__ = "Integer32"
_RmConfigHistoryLogFrequency_Object = MibScalar
rmConfigHistoryLogFrequency = _RmConfigHistoryLogFrequency_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 4, 1),
    _RmConfigHistoryLogFrequency_Type()
)
rmConfigHistoryLogFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmConfigHistoryLogFrequency.setStatus("mandatory")


class _RmConfigExtHistoryLogFrequency_Type(Integer32):
    """Custom type rmConfigExtHistoryLogFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_RmConfigExtHistoryLogFrequency_Type.__name__ = "Integer32"
_RmConfigExtHistoryLogFrequency_Object = MibScalar
rmConfigExtHistoryLogFrequency = _RmConfigExtHistoryLogFrequency_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 4, 2),
    _RmConfigExtHistoryLogFrequency_Type()
)
rmConfigExtHistoryLogFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmConfigExtHistoryLogFrequency.setStatus("mandatory")


class _RmConfigConfigurationLog_Type(Integer32):
    """Custom type rmConfigConfigurationLog based on Integer32"""
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


_RmConfigConfigurationLog_Type.__name__ = "Integer32"
_RmConfigConfigurationLog_Object = MibScalar
rmConfigConfigurationLog = _RmConfigConfigurationLog_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 4, 3),
    _RmConfigConfigurationLog_Type()
)
rmConfigConfigurationLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmConfigConfigurationLog.setStatus("mandatory")


class _RmConfigDhcpStatue_Type(Integer32):
    """Custom type rmConfigDhcpStatue based on Integer32"""
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


_RmConfigDhcpStatue_Type.__name__ = "Integer32"
_RmConfigDhcpStatue_Object = MibScalar
rmConfigDhcpStatue = _RmConfigDhcpStatue_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 5),
    _RmConfigDhcpStatue_Type()
)
rmConfigDhcpStatue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmConfigDhcpStatue.setStatus("mandatory")


class _RmConfigPingStatue_Type(Integer32):
    """Custom type rmConfigPingStatue based on Integer32"""
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


_RmConfigPingStatue_Type.__name__ = "Integer32"
_RmConfigPingStatue_Object = MibScalar
rmConfigPingStatue = _RmConfigPingStatue_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 6),
    _RmConfigPingStatue_Type()
)
rmConfigPingStatue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmConfigPingStatue.setStatus("mandatory")


class _RmConfigTftpStatue_Type(Integer32):
    """Custom type rmConfigTftpStatue based on Integer32"""
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


_RmConfigTftpStatue_Type.__name__ = "Integer32"
_RmConfigTftpStatue_Object = MibScalar
rmConfigTftpStatue = _RmConfigTftpStatue_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 7),
    _RmConfigTftpStatue_Type()
)
rmConfigTftpStatue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmConfigTftpStatue.setStatus("mandatory")
_RmConfigTelnet_ObjectIdentity = ObjectIdentity
rmConfigTelnet = _RmConfigTelnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 8)
)


class _RmConfigTelnetStatue_Type(Integer32):
    """Custom type rmConfigTelnetStatue based on Integer32"""
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


_RmConfigTelnetStatue_Type.__name__ = "Integer32"
_RmConfigTelnetStatue_Object = MibScalar
rmConfigTelnetStatue = _RmConfigTelnetStatue_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 8, 1),
    _RmConfigTelnetStatue_Type()
)
rmConfigTelnetStatue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmConfigTelnetStatue.setStatus("mandatory")


class _RmConfigTelnetPortNumber_Type(Integer32):
    """Custom type rmConfigTelnetPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RmConfigTelnetPortNumber_Type.__name__ = "Integer32"
_RmConfigTelnetPortNumber_Object = MibScalar
rmConfigTelnetPortNumber = _RmConfigTelnetPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 8, 2),
    _RmConfigTelnetPortNumber_Type()
)
rmConfigTelnetPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmConfigTelnetPortNumber.setStatus("mandatory")
_RmConfigHttp_ObjectIdentity = ObjectIdentity
rmConfigHttp = _RmConfigHttp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 9)
)


class _RmConfigHttpStatue_Type(Integer32):
    """Custom type rmConfigHttpStatue based on Integer32"""
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


_RmConfigHttpStatue_Type.__name__ = "Integer32"
_RmConfigHttpStatue_Object = MibScalar
rmConfigHttpStatue = _RmConfigHttpStatue_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 9, 1),
    _RmConfigHttpStatue_Type()
)
rmConfigHttpStatue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmConfigHttpStatue.setStatus("mandatory")


class _RmConfigHttpPortNumber_Type(Integer32):
    """Custom type rmConfigHttpPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RmConfigHttpPortNumber_Type.__name__ = "Integer32"
_RmConfigHttpPortNumber_Object = MibScalar
rmConfigHttpPortNumber = _RmConfigHttpPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 9, 2),
    _RmConfigHttpPortNumber_Type()
)
rmConfigHttpPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmConfigHttpPortNumber.setStatus("mandatory")


class _RmConfigHttpSecurity_Type(Integer32):
    """Custom type rmConfigHttpSecurity based on Integer32"""
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


_RmConfigHttpSecurity_Type.__name__ = "Integer32"
_RmConfigHttpSecurity_Object = MibScalar
rmConfigHttpSecurity = _RmConfigHttpSecurity_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 9, 3),
    _RmConfigHttpSecurity_Type()
)
rmConfigHttpSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmConfigHttpSecurity.setStatus("mandatory")
_RmConfigSnmp_ObjectIdentity = ObjectIdentity
rmConfigSnmp = _RmConfigSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 10)
)


class _RmConfigSnmpStatue_Type(Integer32):
    """Custom type rmConfigSnmpStatue based on Integer32"""
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


_RmConfigSnmpStatue_Type.__name__ = "Integer32"
_RmConfigSnmpStatue_Object = MibScalar
rmConfigSnmpStatue = _RmConfigSnmpStatue_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 10, 1),
    _RmConfigSnmpStatue_Type()
)
rmConfigSnmpStatue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmConfigSnmpStatue.setStatus("mandatory")


class _RmConfigSnmpPortNumber_Type(Integer32):
    """Custom type rmConfigSnmpPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RmConfigSnmpPortNumber_Type.__name__ = "Integer32"
_RmConfigSnmpPortNumber_Object = MibScalar
rmConfigSnmpPortNumber = _RmConfigSnmpPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 10, 2),
    _RmConfigSnmpPortNumber_Type()
)
rmConfigSnmpPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmConfigSnmpPortNumber.setStatus("mandatory")
_RmConfigControl_ObjectIdentity = ObjectIdentity
rmConfigControl = _RmConfigControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 11)
)


class _RmConfigResetToDefault_Type(Integer32):
    """Custom type rmConfigResetToDefault based on Integer32"""
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


_RmConfigResetToDefault_Type.__name__ = "Integer32"
_RmConfigResetToDefault_Object = MibScalar
rmConfigResetToDefault = _RmConfigResetToDefault_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 11, 1),
    _RmConfigResetToDefault_Type()
)
rmConfigResetToDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmConfigResetToDefault.setStatus("mandatory")


class _RmConfigRestart_Type(Integer32):
    """Custom type rmConfigRestart based on Integer32"""
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


_RmConfigRestart_Type.__name__ = "Integer32"
_RmConfigRestart_Object = MibScalar
rmConfigRestart = _RmConfigRestart_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 11, 2),
    _RmConfigRestart_Type()
)
rmConfigRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmConfigRestart.setStatus("mandatory")
_RmConfigTrap_ObjectIdentity = ObjectIdentity
rmConfigTrap = _RmConfigTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 12)
)
_RmConfigTrapRetryCount_Type = Integer32
_RmConfigTrapRetryCount_Object = MibScalar
rmConfigTrapRetryCount = _RmConfigTrapRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 12, 1),
    _RmConfigTrapRetryCount_Type()
)
rmConfigTrapRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmConfigTrapRetryCount.setStatus("mandatory")
_RmConfigTrapRetryTime_Type = Integer32
_RmConfigTrapRetryTime_Object = MibScalar
rmConfigTrapRetryTime = _RmConfigTrapRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 12, 2),
    _RmConfigTrapRetryTime_Type()
)
rmConfigTrapRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmConfigTrapRetryTime.setStatus("mandatory")
_RmConfigTrapAckSignature_Type = Integer32
_RmConfigTrapAckSignature_Object = MibScalar
rmConfigTrapAckSignature = _RmConfigTrapAckSignature_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 12, 3),
    _RmConfigTrapAckSignature_Type()
)
rmConfigTrapAckSignature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmConfigTrapAckSignature.setStatus("mandatory")


class _RmConfigPollRate_Type(Integer32):
    """Custom type rmConfigPollRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 60),
    )


_RmConfigPollRate_Type.__name__ = "Integer32"
_RmConfigPollRate_Object = MibScalar
rmConfigPollRate = _RmConfigPollRate_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 13),
    _RmConfigPollRate_Type()
)
rmConfigPollRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmConfigPollRate.setStatus("mandatory")
_RmConfigTrapsReceiversTable_Object = MibTable
rmConfigTrapsReceiversTable = _RmConfigTrapsReceiversTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 14)
)
if mibBuilder.loadTexts:
    rmConfigTrapsReceiversTable.setStatus("mandatory")
_RmConfigTrapsReceiversEntry_Object = MibTableRow
rmConfigTrapsReceiversEntry = _RmConfigTrapsReceiversEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 14, 1)
)
rmConfigTrapsReceiversEntry.setIndexNames(
    (0, "RackMonitor-MIB", "trapsIndex"),
)
if mibBuilder.loadTexts:
    rmConfigTrapsReceiversEntry.setStatus("mandatory")


class _TrapsIndex_Type(Integer32):
    """Custom type trapsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TrapsIndex_Type.__name__ = "Integer32"
_TrapsIndex_Object = MibTableColumn
trapsIndex = _TrapsIndex_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 14, 1, 1),
    _TrapsIndex_Type()
)
trapsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapsIndex.setStatus("mandatory")
_TrapsReceiverAddr_Type = IpAddress
_TrapsReceiverAddr_Object = MibTableColumn
trapsReceiverAddr = _TrapsReceiverAddr_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 14, 1, 2),
    _TrapsReceiverAddr_Type()
)
trapsReceiverAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapsReceiverAddr.setStatus("mandatory")


class _ReceiverCommunityString_Type(DisplayString):
    """Custom type receiverCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_ReceiverCommunityString_Type.__name__ = "DisplayString"
_ReceiverCommunityString_Object = MibTableColumn
receiverCommunityString = _ReceiverCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 14, 1, 3),
    _ReceiverCommunityString_Type()
)
receiverCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    receiverCommunityString.setStatus("mandatory")


class _ReceiverSeverityLevel_Type(Integer32):
    """Custom type receiverSeverityLevel based on Integer32"""
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


_ReceiverSeverityLevel_Type.__name__ = "Integer32"
_ReceiverSeverityLevel_Object = MibTableColumn
receiverSeverityLevel = _ReceiverSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 14, 1, 4),
    _ReceiverSeverityLevel_Type()
)
receiverSeverityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    receiverSeverityLevel.setStatus("mandatory")


class _ReceiverDescription_Type(DisplayString):
    """Custom type receiverDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ReceiverDescription_Type.__name__ = "DisplayString"
_ReceiverDescription_Object = MibTableColumn
receiverDescription = _ReceiverDescription_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 14, 1, 5),
    _ReceiverDescription_Type()
)
receiverDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    receiverDescription.setStatus("mandatory")
_RmConfigAccessControlTable_Object = MibTable
rmConfigAccessControlTable = _RmConfigAccessControlTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 15)
)
if mibBuilder.loadTexts:
    rmConfigAccessControlTable.setStatus("mandatory")
_RmConfigAccessControlEntry_Object = MibTableRow
rmConfigAccessControlEntry = _RmConfigAccessControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 15, 1)
)
rmConfigAccessControlEntry.setIndexNames(
    (0, "RackMonitor-MIB", "accessIndex"),
)
if mibBuilder.loadTexts:
    rmConfigAccessControlEntry.setStatus("mandatory")


class _AccessIndex_Type(Integer32):
    """Custom type accessIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AccessIndex_Type.__name__ = "Integer32"
_AccessIndex_Object = MibTableColumn
accessIndex = _AccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 15, 1, 1),
    _AccessIndex_Type()
)
accessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessIndex.setStatus("mandatory")
_AccessControlAddr_Type = IpAddress
_AccessControlAddr_Object = MibTableColumn
accessControlAddr = _AccessControlAddr_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 15, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 15, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 15, 1, 4),
    _AccessControlMode_Type()
)
accessControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessControlMode.setStatus("mandatory")


class _RmConfigTemperatureUnit_Type(Integer32):
    """Custom type rmConfigTemperatureUnit based on Integer32"""
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


_RmConfigTemperatureUnit_Type.__name__ = "Integer32"
_RmConfigTemperatureUnit_Object = MibScalar
rmConfigTemperatureUnit = _RmConfigTemperatureUnit_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 16),
    _RmConfigTemperatureUnit_Type()
)
rmConfigTemperatureUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmConfigTemperatureUnit.setStatus("mandatory")


class _RmConfigDateFormat_Type(Integer32):
    """Custom type rmConfigDateFormat based on Integer32"""
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
        *(("dd-mm-yyyy", 2),
          ("dd-mmm-yyyy", 4),
          ("mm-dd-yyyy", 1),
          ("yyyy-mm-dd", 3))
    )


_RmConfigDateFormat_Type.__name__ = "Integer32"
_RmConfigDateFormat_Object = MibScalar
rmConfigDateFormat = _RmConfigDateFormat_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 2, 17),
    _RmConfigDateFormat_Type()
)
rmConfigDateFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmConfigDateFormat.setStatus("mandatory")
_SensorMonitor_ObjectIdentity = ObjectIdentity
sensorMonitor = _SensorMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 3)
)
_SmSensorNumber_Type = Integer32
_SmSensorNumber_Object = MibScalar
smSensorNumber = _SmSensorNumber_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 3, 1),
    _SmSensorNumber_Type()
)
smSensorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSensorNumber.setStatus("mandatory")
_SmSensorTable_Object = MibTable
smSensorTable = _SmSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    smSensorTable.setStatus("mandatory")
_SmSensorEntry_Object = MibTableRow
smSensorEntry = _SmSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 3, 2, 1)
)
smSensorEntry.setIndexNames(
    (0, "RackMonitor-MIB", "smDeviceIndex"),
)
if mibBuilder.loadTexts:
    smSensorEntry.setStatus("mandatory")


class _SmDeviceIndex_Type(Integer32):
    """Custom type smDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SmDeviceIndex_Type.__name__ = "Integer32"
_SmDeviceIndex_Object = MibTableColumn
smDeviceIndex = _SmDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 3, 2, 1, 1),
    _SmDeviceIndex_Type()
)
smDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smDeviceIndex.setStatus("mandatory")


class _SmDeviceStatus_Type(Integer32):
    """Custom type smDeviceStatus based on Integer32"""
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
          ("unknow", 1))
    )


_SmDeviceStatus_Type.__name__ = "Integer32"
_SmDeviceStatus_Object = MibTableColumn
smDeviceStatus = _SmDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 3, 2, 1, 2),
    _SmDeviceStatus_Type()
)
smDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smDeviceStatus.setStatus("mandatory")
_SmDeviceTemperature_Type = Integer32
_SmDeviceTemperature_Object = MibTableColumn
smDeviceTemperature = _SmDeviceTemperature_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 3, 2, 1, 3),
    _SmDeviceTemperature_Type()
)
smDeviceTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smDeviceTemperature.setStatus("mandatory")


class _SmDeviceTemperatureAlarm_Type(Integer32):
    """Custom type smDeviceTemperatureAlarm based on Integer32"""
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
          ("unknow", 1))
    )


_SmDeviceTemperatureAlarm_Type.__name__ = "Integer32"
_SmDeviceTemperatureAlarm_Object = MibTableColumn
smDeviceTemperatureAlarm = _SmDeviceTemperatureAlarm_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 3, 2, 1, 4),
    _SmDeviceTemperatureAlarm_Type()
)
smDeviceTemperatureAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smDeviceTemperatureAlarm.setStatus("mandatory")
_SmDeviceHumidity_Type = Integer32
_SmDeviceHumidity_Object = MibTableColumn
smDeviceHumidity = _SmDeviceHumidity_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 3, 2, 1, 5),
    _SmDeviceHumidity_Type()
)
smDeviceHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smDeviceHumidity.setStatus("mandatory")


class _SmDeviceHumidityAlarm_Type(Integer32):
    """Custom type smDeviceHumidityAlarm based on Integer32"""
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
          ("unknow", 1))
    )


_SmDeviceHumidityAlarm_Type.__name__ = "Integer32"
_SmDeviceHumidityAlarm_Object = MibTableColumn
smDeviceHumidityAlarm = _SmDeviceHumidityAlarm_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 3, 2, 1, 6),
    _SmDeviceHumidityAlarm_Type()
)
smDeviceHumidityAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smDeviceHumidityAlarm.setStatus("mandatory")


class _SmAlarm1_Type(Integer32):
    """Custom type smAlarm1 based on Integer32"""
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
          ("unknow", 1))
    )


_SmAlarm1_Type.__name__ = "Integer32"
_SmAlarm1_Object = MibTableColumn
smAlarm1 = _SmAlarm1_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 3, 2, 1, 7),
    _SmAlarm1_Type()
)
smAlarm1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smAlarm1.setStatus("mandatory")


class _SmAlarm2_Type(Integer32):
    """Custom type smAlarm2 based on Integer32"""
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
          ("unknow", 1))
    )


_SmAlarm2_Type.__name__ = "Integer32"
_SmAlarm2_Object = MibTableColumn
smAlarm2 = _SmAlarm2_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 3, 2, 1, 8),
    _SmAlarm2_Type()
)
smAlarm2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smAlarm2.setStatus("mandatory")
_SensorConfig_ObjectIdentity = ObjectIdentity
sensorConfig = _SensorConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4)
)
_ScSensorNumber_Type = Integer32
_ScSensorNumber_Object = MibScalar
scSensorNumber = _ScSensorNumber_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 1),
    _ScSensorNumber_Type()
)
scSensorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scSensorNumber.setStatus("mandatory")
_ScSensorTable_Object = MibTable
scSensorTable = _ScSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    scSensorTable.setStatus("mandatory")
_ScSensorEntry_Object = MibTableRow
scSensorEntry = _ScSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 2, 1)
)
scSensorEntry.setIndexNames(
    (0, "RackMonitor-MIB", "scDeviceIndex"),
)
if mibBuilder.loadTexts:
    scSensorEntry.setStatus("mandatory")


class _ScDeviceIndex_Type(Integer32):
    """Custom type scDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ScDeviceIndex_Type.__name__ = "Integer32"
_ScDeviceIndex_Object = MibTableColumn
scDeviceIndex = _ScDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 2, 1, 1),
    _ScDeviceIndex_Type()
)
scDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDeviceIndex.setStatus("mandatory")


class _ScDeviceName_Type(DisplayString):
    """Custom type scDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ScDeviceName_Type.__name__ = "DisplayString"
_ScDeviceName_Object = MibTableColumn
scDeviceName = _ScDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 2, 1, 2),
    _ScDeviceName_Type()
)
scDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scDeviceName.setStatus("mandatory")


class _ScDeviceState_Type(Integer32):
    """Custom type scDeviceState based on Integer32"""
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


_ScDeviceState_Type.__name__ = "Integer32"
_ScDeviceState_Object = MibTableColumn
scDeviceState = _ScDeviceState_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 2, 1, 3),
    _ScDeviceState_Type()
)
scDeviceState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scDeviceState.setStatus("mandatory")
_ScSensor1_ObjectIdentity = ObjectIdentity
scSensor1 = _ScSensor1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 3)
)


class _ScSensor1DeviceName_Type(DisplayString):
    """Custom type scSensor1DeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ScSensor1DeviceName_Type.__name__ = "DisplayString"
_ScSensor1DeviceName_Object = MibScalar
scSensor1DeviceName = _ScSensor1DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 3, 1),
    _ScSensor1DeviceName_Type()
)
scSensor1DeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor1DeviceName.setStatus("mandatory")


class _ScSensor1DeviceState_Type(Integer32):
    """Custom type scSensor1DeviceState based on Integer32"""
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


_ScSensor1DeviceState_Type.__name__ = "Integer32"
_ScSensor1DeviceState_Object = MibScalar
scSensor1DeviceState = _ScSensor1DeviceState_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 3, 2),
    _ScSensor1DeviceState_Type()
)
scSensor1DeviceState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor1DeviceState.setStatus("mandatory")
_ScSensor1Temperature_ObjectIdentity = ObjectIdentity
scSensor1Temperature = _ScSensor1Temperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 3, 3)
)


class _ScSensor1TemperatureName_Type(DisplayString):
    """Custom type scSensor1TemperatureName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ScSensor1TemperatureName_Type.__name__ = "DisplayString"
_ScSensor1TemperatureName_Object = MibScalar
scSensor1TemperatureName = _ScSensor1TemperatureName_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 3, 3, 1),
    _ScSensor1TemperatureName_Type()
)
scSensor1TemperatureName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor1TemperatureName.setStatus("mandatory")
_ScSensor1TemperatureLowWarning_Type = Integer32
_ScSensor1TemperatureLowWarning_Object = MibScalar
scSensor1TemperatureLowWarning = _ScSensor1TemperatureLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 3, 3, 2),
    _ScSensor1TemperatureLowWarning_Type()
)
scSensor1TemperatureLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor1TemperatureLowWarning.setStatus("mandatory")
_ScSensor1TemperatureLowCritical_Type = Integer32
_ScSensor1TemperatureLowCritical_Object = MibScalar
scSensor1TemperatureLowCritical = _ScSensor1TemperatureLowCritical_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 3, 3, 3),
    _ScSensor1TemperatureLowCritical_Type()
)
scSensor1TemperatureLowCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor1TemperatureLowCritical.setStatus("mandatory")
_ScSensor1TemperatureHighWarning_Type = Integer32
_ScSensor1TemperatureHighWarning_Object = MibScalar
scSensor1TemperatureHighWarning = _ScSensor1TemperatureHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 3, 3, 4),
    _ScSensor1TemperatureHighWarning_Type()
)
scSensor1TemperatureHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor1TemperatureHighWarning.setStatus("mandatory")
_ScSensor1TemperatureHighCritical_Type = Integer32
_ScSensor1TemperatureHighCritical_Object = MibScalar
scSensor1TemperatureHighCritical = _ScSensor1TemperatureHighCritical_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 3, 3, 5),
    _ScSensor1TemperatureHighCritical_Type()
)
scSensor1TemperatureHighCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor1TemperatureHighCritical.setStatus("mandatory")
_ScSensor1TemperatureHysteresis_Type = Integer32
_ScSensor1TemperatureHysteresis_Object = MibScalar
scSensor1TemperatureHysteresis = _ScSensor1TemperatureHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 3, 3, 6),
    _ScSensor1TemperatureHysteresis_Type()
)
scSensor1TemperatureHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor1TemperatureHysteresis.setStatus("mandatory")


class _ScSensor1TemperatureCalibration_Type(Integer32):
    """Custom type scSensor1TemperatureCalibration based on Integer32"""
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


_ScSensor1TemperatureCalibration_Type.__name__ = "Integer32"
_ScSensor1TemperatureCalibration_Object = MibScalar
scSensor1TemperatureCalibration = _ScSensor1TemperatureCalibration_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 3, 3, 7),
    _ScSensor1TemperatureCalibration_Type()
)
scSensor1TemperatureCalibration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor1TemperatureCalibration.setStatus("mandatory")


class _ScSensor1TemperatureLowWarningStatus_Type(Integer32):
    """Custom type scSensor1TemperatureLowWarningStatus based on Integer32"""
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


_ScSensor1TemperatureLowWarningStatus_Type.__name__ = "Integer32"
_ScSensor1TemperatureLowWarningStatus_Object = MibScalar
scSensor1TemperatureLowWarningStatus = _ScSensor1TemperatureLowWarningStatus_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 3, 3, 8),
    _ScSensor1TemperatureLowWarningStatus_Type()
)
scSensor1TemperatureLowWarningStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor1TemperatureLowWarningStatus.setStatus("mandatory")


class _ScSensor1TemperatureLowCriticalStatus_Type(Integer32):
    """Custom type scSensor1TemperatureLowCriticalStatus based on Integer32"""
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


_ScSensor1TemperatureLowCriticalStatus_Type.__name__ = "Integer32"
_ScSensor1TemperatureLowCriticalStatus_Object = MibScalar
scSensor1TemperatureLowCriticalStatus = _ScSensor1TemperatureLowCriticalStatus_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 3, 3, 9),
    _ScSensor1TemperatureLowCriticalStatus_Type()
)
scSensor1TemperatureLowCriticalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor1TemperatureLowCriticalStatus.setStatus("mandatory")


class _ScSensor1TemperatureHighWarningStatus_Type(Integer32):
    """Custom type scSensor1TemperatureHighWarningStatus based on Integer32"""
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


_ScSensor1TemperatureHighWarningStatus_Type.__name__ = "Integer32"
_ScSensor1TemperatureHighWarningStatus_Object = MibScalar
scSensor1TemperatureHighWarningStatus = _ScSensor1TemperatureHighWarningStatus_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 3, 3, 10),
    _ScSensor1TemperatureHighWarningStatus_Type()
)
scSensor1TemperatureHighWarningStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor1TemperatureHighWarningStatus.setStatus("mandatory")


class _ScSensor1TemperatureHighCriticalStatus_Type(Integer32):
    """Custom type scSensor1TemperatureHighCriticalStatus based on Integer32"""
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


_ScSensor1TemperatureHighCriticalStatus_Type.__name__ = "Integer32"
_ScSensor1TemperatureHighCriticalStatus_Object = MibScalar
scSensor1TemperatureHighCriticalStatus = _ScSensor1TemperatureHighCriticalStatus_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 3, 3, 11),
    _ScSensor1TemperatureHighCriticalStatus_Type()
)
scSensor1TemperatureHighCriticalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor1TemperatureHighCriticalStatus.setStatus("mandatory")
_ScSensor1Humidity_ObjectIdentity = ObjectIdentity
scSensor1Humidity = _ScSensor1Humidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 3, 4)
)


class _ScSensor1HumdityName_Type(DisplayString):
    """Custom type scSensor1HumdityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ScSensor1HumdityName_Type.__name__ = "DisplayString"
_ScSensor1HumdityName_Object = MibScalar
scSensor1HumdityName = _ScSensor1HumdityName_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 3, 4, 1),
    _ScSensor1HumdityName_Type()
)
scSensor1HumdityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor1HumdityName.setStatus("mandatory")
_ScSensor1HumidityLowWarning_Type = Integer32
_ScSensor1HumidityLowWarning_Object = MibScalar
scSensor1HumidityLowWarning = _ScSensor1HumidityLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 3, 4, 2),
    _ScSensor1HumidityLowWarning_Type()
)
scSensor1HumidityLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor1HumidityLowWarning.setStatus("mandatory")
_ScSensor1HumidityLowCritical_Type = Integer32
_ScSensor1HumidityLowCritical_Object = MibScalar
scSensor1HumidityLowCritical = _ScSensor1HumidityLowCritical_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 3, 4, 3),
    _ScSensor1HumidityLowCritical_Type()
)
scSensor1HumidityLowCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor1HumidityLowCritical.setStatus("mandatory")
_ScSensor1HumidityHighWarning_Type = Integer32
_ScSensor1HumidityHighWarning_Object = MibScalar
scSensor1HumidityHighWarning = _ScSensor1HumidityHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 3, 4, 4),
    _ScSensor1HumidityHighWarning_Type()
)
scSensor1HumidityHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor1HumidityHighWarning.setStatus("mandatory")
_ScSensor1HumidityHighCritical_Type = Integer32
_ScSensor1HumidityHighCritical_Object = MibScalar
scSensor1HumidityHighCritical = _ScSensor1HumidityHighCritical_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 3, 4, 5),
    _ScSensor1HumidityHighCritical_Type()
)
scSensor1HumidityHighCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor1HumidityHighCritical.setStatus("mandatory")
_ScSensor1HumidityHysteresis_Type = Integer32
_ScSensor1HumidityHysteresis_Object = MibScalar
scSensor1HumidityHysteresis = _ScSensor1HumidityHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 3, 4, 6),
    _ScSensor1HumidityHysteresis_Type()
)
scSensor1HumidityHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor1HumidityHysteresis.setStatus("mandatory")


class _ScSensor1HumidityCalibration_Type(Integer32):
    """Custom type scSensor1HumidityCalibration based on Integer32"""
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


_ScSensor1HumidityCalibration_Type.__name__ = "Integer32"
_ScSensor1HumidityCalibration_Object = MibScalar
scSensor1HumidityCalibration = _ScSensor1HumidityCalibration_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 3, 4, 7),
    _ScSensor1HumidityCalibration_Type()
)
scSensor1HumidityCalibration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor1HumidityCalibration.setStatus("mandatory")


class _ScSensor1HumidityLowWarningStatus_Type(Integer32):
    """Custom type scSensor1HumidityLowWarningStatus based on Integer32"""
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


_ScSensor1HumidityLowWarningStatus_Type.__name__ = "Integer32"
_ScSensor1HumidityLowWarningStatus_Object = MibScalar
scSensor1HumidityLowWarningStatus = _ScSensor1HumidityLowWarningStatus_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 3, 4, 8),
    _ScSensor1HumidityLowWarningStatus_Type()
)
scSensor1HumidityLowWarningStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor1HumidityLowWarningStatus.setStatus("mandatory")


class _ScSensor1HumidityLowCriticalStatus_Type(Integer32):
    """Custom type scSensor1HumidityLowCriticalStatus based on Integer32"""
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


_ScSensor1HumidityLowCriticalStatus_Type.__name__ = "Integer32"
_ScSensor1HumidityLowCriticalStatus_Object = MibScalar
scSensor1HumidityLowCriticalStatus = _ScSensor1HumidityLowCriticalStatus_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 3, 4, 9),
    _ScSensor1HumidityLowCriticalStatus_Type()
)
scSensor1HumidityLowCriticalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor1HumidityLowCriticalStatus.setStatus("mandatory")


class _ScSensor1HumidityHighWarningStatus_Type(Integer32):
    """Custom type scSensor1HumidityHighWarningStatus based on Integer32"""
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


_ScSensor1HumidityHighWarningStatus_Type.__name__ = "Integer32"
_ScSensor1HumidityHighWarningStatus_Object = MibScalar
scSensor1HumidityHighWarningStatus = _ScSensor1HumidityHighWarningStatus_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 3, 4, 10),
    _ScSensor1HumidityHighWarningStatus_Type()
)
scSensor1HumidityHighWarningStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor1HumidityHighWarningStatus.setStatus("mandatory")


class _ScSensor1HumidityHighCriticalStatus_Type(Integer32):
    """Custom type scSensor1HumidityHighCriticalStatus based on Integer32"""
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


_ScSensor1HumidityHighCriticalStatus_Type.__name__ = "Integer32"
_ScSensor1HumidityHighCriticalStatus_Object = MibScalar
scSensor1HumidityHighCriticalStatus = _ScSensor1HumidityHighCriticalStatus_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 3, 4, 11),
    _ScSensor1HumidityHighCriticalStatus_Type()
)
scSensor1HumidityHighCriticalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor1HumidityHighCriticalStatus.setStatus("mandatory")
_ScSensor1Alarm1_ObjectIdentity = ObjectIdentity
scSensor1Alarm1 = _ScSensor1Alarm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 3, 5)
)


class _ScSensor1Alarm1Name_Type(DisplayString):
    """Custom type scSensor1Alarm1Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ScSensor1Alarm1Name_Type.__name__ = "DisplayString"
_ScSensor1Alarm1Name_Object = MibScalar
scSensor1Alarm1Name = _ScSensor1Alarm1Name_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 3, 5, 1),
    _ScSensor1Alarm1Name_Type()
)
scSensor1Alarm1Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor1Alarm1Name.setStatus("mandatory")


class _ScSensor1Alarm1State_Type(Integer32):
    """Custom type scSensor1Alarm1State based on Integer32"""
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


_ScSensor1Alarm1State_Type.__name__ = "Integer32"
_ScSensor1Alarm1State_Object = MibScalar
scSensor1Alarm1State = _ScSensor1Alarm1State_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 3, 5, 2),
    _ScSensor1Alarm1State_Type()
)
scSensor1Alarm1State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor1Alarm1State.setStatus("mandatory")
_ScSensor1Alarm1Hysteresis_Type = Integer32
_ScSensor1Alarm1Hysteresis_Object = MibScalar
scSensor1Alarm1Hysteresis = _ScSensor1Alarm1Hysteresis_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 3, 5, 3),
    _ScSensor1Alarm1Hysteresis_Type()
)
scSensor1Alarm1Hysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor1Alarm1Hysteresis.setStatus("mandatory")
_ScSensor1Alarm2_ObjectIdentity = ObjectIdentity
scSensor1Alarm2 = _ScSensor1Alarm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 3, 6)
)


class _ScSensor1Alarm2Name_Type(DisplayString):
    """Custom type scSensor1Alarm2Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ScSensor1Alarm2Name_Type.__name__ = "DisplayString"
_ScSensor1Alarm2Name_Object = MibScalar
scSensor1Alarm2Name = _ScSensor1Alarm2Name_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 3, 6, 1),
    _ScSensor1Alarm2Name_Type()
)
scSensor1Alarm2Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor1Alarm2Name.setStatus("mandatory")


class _ScSensor1Alarm2State_Type(Integer32):
    """Custom type scSensor1Alarm2State based on Integer32"""
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


_ScSensor1Alarm2State_Type.__name__ = "Integer32"
_ScSensor1Alarm2State_Object = MibScalar
scSensor1Alarm2State = _ScSensor1Alarm2State_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 3, 6, 2),
    _ScSensor1Alarm2State_Type()
)
scSensor1Alarm2State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor1Alarm2State.setStatus("mandatory")
_ScSensor1Alarm2Hysteresis_Type = Integer32
_ScSensor1Alarm2Hysteresis_Object = MibScalar
scSensor1Alarm2Hysteresis = _ScSensor1Alarm2Hysteresis_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 3, 6, 3),
    _ScSensor1Alarm2Hysteresis_Type()
)
scSensor1Alarm2Hysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor1Alarm2Hysteresis.setStatus("mandatory")
_ScSensor2_ObjectIdentity = ObjectIdentity
scSensor2 = _ScSensor2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 4)
)


class _ScSensor2DeviceName_Type(DisplayString):
    """Custom type scSensor2DeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ScSensor2DeviceName_Type.__name__ = "DisplayString"
_ScSensor2DeviceName_Object = MibScalar
scSensor2DeviceName = _ScSensor2DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 4, 1),
    _ScSensor2DeviceName_Type()
)
scSensor2DeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor2DeviceName.setStatus("mandatory")


class _ScSensor2DeviceState_Type(Integer32):
    """Custom type scSensor2DeviceState based on Integer32"""
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


_ScSensor2DeviceState_Type.__name__ = "Integer32"
_ScSensor2DeviceState_Object = MibScalar
scSensor2DeviceState = _ScSensor2DeviceState_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 4, 2),
    _ScSensor2DeviceState_Type()
)
scSensor2DeviceState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor2DeviceState.setStatus("mandatory")
_ScSensor2Temperature_ObjectIdentity = ObjectIdentity
scSensor2Temperature = _ScSensor2Temperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 4, 3)
)


class _ScSensor2TemperatureName_Type(DisplayString):
    """Custom type scSensor2TemperatureName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ScSensor2TemperatureName_Type.__name__ = "DisplayString"
_ScSensor2TemperatureName_Object = MibScalar
scSensor2TemperatureName = _ScSensor2TemperatureName_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 4, 3, 1),
    _ScSensor2TemperatureName_Type()
)
scSensor2TemperatureName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor2TemperatureName.setStatus("mandatory")
_ScSensor2TemperatureLowWarning_Type = Integer32
_ScSensor2TemperatureLowWarning_Object = MibScalar
scSensor2TemperatureLowWarning = _ScSensor2TemperatureLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 4, 3, 2),
    _ScSensor2TemperatureLowWarning_Type()
)
scSensor2TemperatureLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor2TemperatureLowWarning.setStatus("mandatory")
_ScSensor2TemperatureLowCritical_Type = Integer32
_ScSensor2TemperatureLowCritical_Object = MibScalar
scSensor2TemperatureLowCritical = _ScSensor2TemperatureLowCritical_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 4, 3, 3),
    _ScSensor2TemperatureLowCritical_Type()
)
scSensor2TemperatureLowCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor2TemperatureLowCritical.setStatus("mandatory")
_ScSensor2TemperatureHighWarning_Type = Integer32
_ScSensor2TemperatureHighWarning_Object = MibScalar
scSensor2TemperatureHighWarning = _ScSensor2TemperatureHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 4, 3, 4),
    _ScSensor2TemperatureHighWarning_Type()
)
scSensor2TemperatureHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor2TemperatureHighWarning.setStatus("mandatory")
_ScSensor2TemperatureHighCritical_Type = Integer32
_ScSensor2TemperatureHighCritical_Object = MibScalar
scSensor2TemperatureHighCritical = _ScSensor2TemperatureHighCritical_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 4, 3, 5),
    _ScSensor2TemperatureHighCritical_Type()
)
scSensor2TemperatureHighCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor2TemperatureHighCritical.setStatus("mandatory")
_ScSensor2TemperatureHysteresis_Type = Integer32
_ScSensor2TemperatureHysteresis_Object = MibScalar
scSensor2TemperatureHysteresis = _ScSensor2TemperatureHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 4, 3, 6),
    _ScSensor2TemperatureHysteresis_Type()
)
scSensor2TemperatureHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor2TemperatureHysteresis.setStatus("mandatory")


class _ScSensor2TemperatureCalibration_Type(Integer32):
    """Custom type scSensor2TemperatureCalibration based on Integer32"""
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


_ScSensor2TemperatureCalibration_Type.__name__ = "Integer32"
_ScSensor2TemperatureCalibration_Object = MibScalar
scSensor2TemperatureCalibration = _ScSensor2TemperatureCalibration_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 4, 3, 7),
    _ScSensor2TemperatureCalibration_Type()
)
scSensor2TemperatureCalibration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor2TemperatureCalibration.setStatus("mandatory")


class _ScSensor2TemperatureLowWarningStatus_Type(Integer32):
    """Custom type scSensor2TemperatureLowWarningStatus based on Integer32"""
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


_ScSensor2TemperatureLowWarningStatus_Type.__name__ = "Integer32"
_ScSensor2TemperatureLowWarningStatus_Object = MibScalar
scSensor2TemperatureLowWarningStatus = _ScSensor2TemperatureLowWarningStatus_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 4, 3, 8),
    _ScSensor2TemperatureLowWarningStatus_Type()
)
scSensor2TemperatureLowWarningStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor2TemperatureLowWarningStatus.setStatus("mandatory")


class _ScSensor2TemperatureLowCriticalStatus_Type(Integer32):
    """Custom type scSensor2TemperatureLowCriticalStatus based on Integer32"""
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


_ScSensor2TemperatureLowCriticalStatus_Type.__name__ = "Integer32"
_ScSensor2TemperatureLowCriticalStatus_Object = MibScalar
scSensor2TemperatureLowCriticalStatus = _ScSensor2TemperatureLowCriticalStatus_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 4, 3, 9),
    _ScSensor2TemperatureLowCriticalStatus_Type()
)
scSensor2TemperatureLowCriticalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor2TemperatureLowCriticalStatus.setStatus("mandatory")


class _ScSensor2TemperatureHighWarningStatus_Type(Integer32):
    """Custom type scSensor2TemperatureHighWarningStatus based on Integer32"""
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


_ScSensor2TemperatureHighWarningStatus_Type.__name__ = "Integer32"
_ScSensor2TemperatureHighWarningStatus_Object = MibScalar
scSensor2TemperatureHighWarningStatus = _ScSensor2TemperatureHighWarningStatus_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 4, 3, 10),
    _ScSensor2TemperatureHighWarningStatus_Type()
)
scSensor2TemperatureHighWarningStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor2TemperatureHighWarningStatus.setStatus("mandatory")


class _ScSensor2TemperatureHighCriticalStatus_Type(Integer32):
    """Custom type scSensor2TemperatureHighCriticalStatus based on Integer32"""
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


_ScSensor2TemperatureHighCriticalStatus_Type.__name__ = "Integer32"
_ScSensor2TemperatureHighCriticalStatus_Object = MibScalar
scSensor2TemperatureHighCriticalStatus = _ScSensor2TemperatureHighCriticalStatus_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 4, 3, 11),
    _ScSensor2TemperatureHighCriticalStatus_Type()
)
scSensor2TemperatureHighCriticalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor2TemperatureHighCriticalStatus.setStatus("mandatory")
_ScSensor2Humidity_ObjectIdentity = ObjectIdentity
scSensor2Humidity = _ScSensor2Humidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 4, 4)
)


class _ScSensor2HumdityName_Type(DisplayString):
    """Custom type scSensor2HumdityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ScSensor2HumdityName_Type.__name__ = "DisplayString"
_ScSensor2HumdityName_Object = MibScalar
scSensor2HumdityName = _ScSensor2HumdityName_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 4, 4, 1),
    _ScSensor2HumdityName_Type()
)
scSensor2HumdityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor2HumdityName.setStatus("mandatory")
_ScSensor2HumidityLowWarning_Type = Integer32
_ScSensor2HumidityLowWarning_Object = MibScalar
scSensor2HumidityLowWarning = _ScSensor2HumidityLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 4, 4, 2),
    _ScSensor2HumidityLowWarning_Type()
)
scSensor2HumidityLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor2HumidityLowWarning.setStatus("mandatory")
_ScSensor2HumidityLowCritical_Type = Integer32
_ScSensor2HumidityLowCritical_Object = MibScalar
scSensor2HumidityLowCritical = _ScSensor2HumidityLowCritical_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 4, 4, 3),
    _ScSensor2HumidityLowCritical_Type()
)
scSensor2HumidityLowCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor2HumidityLowCritical.setStatus("mandatory")
_ScSensor2HumidityHighWarning_Type = Integer32
_ScSensor2HumidityHighWarning_Object = MibScalar
scSensor2HumidityHighWarning = _ScSensor2HumidityHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 4, 4, 4),
    _ScSensor2HumidityHighWarning_Type()
)
scSensor2HumidityHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor2HumidityHighWarning.setStatus("mandatory")
_ScSensor2HumidityHighCritical_Type = Integer32
_ScSensor2HumidityHighCritical_Object = MibScalar
scSensor2HumidityHighCritical = _ScSensor2HumidityHighCritical_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 4, 4, 5),
    _ScSensor2HumidityHighCritical_Type()
)
scSensor2HumidityHighCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor2HumidityHighCritical.setStatus("mandatory")
_ScSensor2HumidityHysteresis_Type = Integer32
_ScSensor2HumidityHysteresis_Object = MibScalar
scSensor2HumidityHysteresis = _ScSensor2HumidityHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 4, 4, 6),
    _ScSensor2HumidityHysteresis_Type()
)
scSensor2HumidityHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor2HumidityHysteresis.setStatus("mandatory")


class _ScSensor2HumidityCalibration_Type(Integer32):
    """Custom type scSensor2HumidityCalibration based on Integer32"""
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


_ScSensor2HumidityCalibration_Type.__name__ = "Integer32"
_ScSensor2HumidityCalibration_Object = MibScalar
scSensor2HumidityCalibration = _ScSensor2HumidityCalibration_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 4, 4, 7),
    _ScSensor2HumidityCalibration_Type()
)
scSensor2HumidityCalibration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor2HumidityCalibration.setStatus("mandatory")


class _ScSensor2HumidityLowWarningStatus_Type(Integer32):
    """Custom type scSensor2HumidityLowWarningStatus based on Integer32"""
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


_ScSensor2HumidityLowWarningStatus_Type.__name__ = "Integer32"
_ScSensor2HumidityLowWarningStatus_Object = MibScalar
scSensor2HumidityLowWarningStatus = _ScSensor2HumidityLowWarningStatus_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 4, 4, 8),
    _ScSensor2HumidityLowWarningStatus_Type()
)
scSensor2HumidityLowWarningStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor2HumidityLowWarningStatus.setStatus("mandatory")


class _ScSensor2HumidityLowCriticalStatus_Type(Integer32):
    """Custom type scSensor2HumidityLowCriticalStatus based on Integer32"""
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


_ScSensor2HumidityLowCriticalStatus_Type.__name__ = "Integer32"
_ScSensor2HumidityLowCriticalStatus_Object = MibScalar
scSensor2HumidityLowCriticalStatus = _ScSensor2HumidityLowCriticalStatus_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 4, 4, 9),
    _ScSensor2HumidityLowCriticalStatus_Type()
)
scSensor2HumidityLowCriticalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor2HumidityLowCriticalStatus.setStatus("mandatory")


class _ScSensor2HumidityHighWarningStatus_Type(Integer32):
    """Custom type scSensor2HumidityHighWarningStatus based on Integer32"""
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


_ScSensor2HumidityHighWarningStatus_Type.__name__ = "Integer32"
_ScSensor2HumidityHighWarningStatus_Object = MibScalar
scSensor2HumidityHighWarningStatus = _ScSensor2HumidityHighWarningStatus_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 4, 4, 10),
    _ScSensor2HumidityHighWarningStatus_Type()
)
scSensor2HumidityHighWarningStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor2HumidityHighWarningStatus.setStatus("mandatory")


class _ScSensor2HumidityHighCriticalStatus_Type(Integer32):
    """Custom type scSensor2HumidityHighCriticalStatus based on Integer32"""
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


_ScSensor2HumidityHighCriticalStatus_Type.__name__ = "Integer32"
_ScSensor2HumidityHighCriticalStatus_Object = MibScalar
scSensor2HumidityHighCriticalStatus = _ScSensor2HumidityHighCriticalStatus_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 4, 4, 11),
    _ScSensor2HumidityHighCriticalStatus_Type()
)
scSensor2HumidityHighCriticalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor2HumidityHighCriticalStatus.setStatus("mandatory")
_ScSensor2Alarm1_ObjectIdentity = ObjectIdentity
scSensor2Alarm1 = _ScSensor2Alarm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 4, 5)
)


class _ScSensor2Alarm1Name_Type(DisplayString):
    """Custom type scSensor2Alarm1Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ScSensor2Alarm1Name_Type.__name__ = "DisplayString"
_ScSensor2Alarm1Name_Object = MibScalar
scSensor2Alarm1Name = _ScSensor2Alarm1Name_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 4, 5, 1),
    _ScSensor2Alarm1Name_Type()
)
scSensor2Alarm1Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor2Alarm1Name.setStatus("mandatory")


class _ScSensor2Alarm1State_Type(Integer32):
    """Custom type scSensor2Alarm1State based on Integer32"""
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


_ScSensor2Alarm1State_Type.__name__ = "Integer32"
_ScSensor2Alarm1State_Object = MibScalar
scSensor2Alarm1State = _ScSensor2Alarm1State_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 4, 5, 2),
    _ScSensor2Alarm1State_Type()
)
scSensor2Alarm1State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor2Alarm1State.setStatus("mandatory")
_ScSensor2Alarm1Hysteresis_Type = Integer32
_ScSensor2Alarm1Hysteresis_Object = MibScalar
scSensor2Alarm1Hysteresis = _ScSensor2Alarm1Hysteresis_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 4, 5, 3),
    _ScSensor2Alarm1Hysteresis_Type()
)
scSensor2Alarm1Hysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor2Alarm1Hysteresis.setStatus("mandatory")
_ScSensor2Alarm2_ObjectIdentity = ObjectIdentity
scSensor2Alarm2 = _ScSensor2Alarm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 4, 6)
)


class _ScSensor2Alarm2Name_Type(DisplayString):
    """Custom type scSensor2Alarm2Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ScSensor2Alarm2Name_Type.__name__ = "DisplayString"
_ScSensor2Alarm2Name_Object = MibScalar
scSensor2Alarm2Name = _ScSensor2Alarm2Name_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 4, 6, 1),
    _ScSensor2Alarm2Name_Type()
)
scSensor2Alarm2Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor2Alarm2Name.setStatus("mandatory")


class _ScSensor2Alarm2State_Type(Integer32):
    """Custom type scSensor2Alarm2State based on Integer32"""
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


_ScSensor2Alarm2State_Type.__name__ = "Integer32"
_ScSensor2Alarm2State_Object = MibScalar
scSensor2Alarm2State = _ScSensor2Alarm2State_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 4, 6, 2),
    _ScSensor2Alarm2State_Type()
)
scSensor2Alarm2State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor2Alarm2State.setStatus("mandatory")
_ScSensor2Alarm2Hysteresis_Type = Integer32
_ScSensor2Alarm2Hysteresis_Object = MibScalar
scSensor2Alarm2Hysteresis = _ScSensor2Alarm2Hysteresis_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 1, 4, 4, 6, 3),
    _ScSensor2Alarm2Hysteresis_Type()
)
scSensor2Alarm2Hysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSensor2Alarm2Hysteresis.setStatus("mandatory")
_RmTraps_ObjectIdentity = ObjectIdentity
rmTraps = _RmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 2)
)

# Managed Objects groups


# Notification objects

rmCommunicationRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 2, 0, 1)
)
if mibBuilder.loadTexts:
    rmCommunicationRestored.setStatus(
        ""
    )

rmCommunicationLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 2, 0, 2)
)
if mibBuilder.loadTexts:
    rmCommunicationLost.setStatus(
        ""
    )

rmAlarm1Inactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 2, 0, 3)
)
if mibBuilder.loadTexts:
    rmAlarm1Inactive.setStatus(
        ""
    )

rmAlarm1Active = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 2, 0, 4)
)
if mibBuilder.loadTexts:
    rmAlarm1Active.setStatus(
        ""
    )

rmAlarm2Inactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 2, 0, 5)
)
if mibBuilder.loadTexts:
    rmAlarm2Inactive.setStatus(
        ""
    )

rmAlarm2Active = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 2, 0, 6)
)
if mibBuilder.loadTexts:
    rmAlarm2Active.setStatus(
        ""
    )

rmTemperatureNotHighWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 2, 0, 7)
)
if mibBuilder.loadTexts:
    rmTemperatureNotHighWarning.setStatus(
        ""
    )

rmTemperatureHighWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 2, 0, 8)
)
if mibBuilder.loadTexts:
    rmTemperatureHighWarning.setStatus(
        ""
    )

rmTemperatureNotLowWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 2, 0, 9)
)
if mibBuilder.loadTexts:
    rmTemperatureNotLowWarning.setStatus(
        ""
    )

rmTemperatureLowWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 2, 0, 10)
)
if mibBuilder.loadTexts:
    rmTemperatureLowWarning.setStatus(
        ""
    )

rmTemperatureNotHighCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 2, 0, 11)
)
if mibBuilder.loadTexts:
    rmTemperatureNotHighCritical.setStatus(
        ""
    )

rmTemperatureHighCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 2, 0, 12)
)
if mibBuilder.loadTexts:
    rmTemperatureHighCritical.setStatus(
        ""
    )

rmTemperatureNotLowCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 2, 0, 13)
)
if mibBuilder.loadTexts:
    rmTemperatureNotLowCritical.setStatus(
        ""
    )

rmTemperatureLowCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 2, 0, 14)
)
if mibBuilder.loadTexts:
    rmTemperatureLowCritical.setStatus(
        ""
    )

rmHumidityNotHighWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 2, 0, 15)
)
if mibBuilder.loadTexts:
    rmHumidityNotHighWarning.setStatus(
        ""
    )

rmHumidityHighWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 2, 0, 16)
)
if mibBuilder.loadTexts:
    rmHumidityHighWarning.setStatus(
        ""
    )

rmHumidityNotLowWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 2, 0, 17)
)
if mibBuilder.loadTexts:
    rmHumidityNotLowWarning.setStatus(
        ""
    )

rmHumidityLowWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 2, 0, 18)
)
if mibBuilder.loadTexts:
    rmHumidityLowWarning.setStatus(
        ""
    )

rmHumidityNotHighCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 2, 0, 19)
)
if mibBuilder.loadTexts:
    rmHumidityNotHighCritical.setStatus(
        ""
    )

rmHumidityHighCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 2, 0, 20)
)
if mibBuilder.loadTexts:
    rmHumidityHighCritical.setStatus(
        ""
    )

rmHumidityNotLowCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 2, 0, 21)
)
if mibBuilder.loadTexts:
    rmHumidityNotLowCritical.setStatus(
        ""
    )

rmHumidityLowCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1, 2, 0, 22)
)
if mibBuilder.loadTexts:
    rmHumidityLowCritical.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RackMonitor-MIB",
    **{"powerware": powerware,
       "product": product,
       "dataCenter": dataCenter,
       "environmentalMonitor": environmentalMonitor,
       "insObjects": insObjects,
       "rmIdent": rmIdent,
       "insIdentManufacturer": insIdentManufacturer,
       "insIdentModel": insIdentModel,
       "insIdentAgentSoftwareVersion": insIdentAgentSoftwareVersion,
       "insIdentName": insIdentName,
       "rmConfig": rmConfig,
       "rmConfigMibVersion": rmConfigMibVersion,
       "rmConfigNetwork": rmConfigNetwork,
       "rmConfigIpAddress": rmConfigIpAddress,
       "rmConfigGateway": rmConfigGateway,
       "rmConfigSubnetMask": rmConfigSubnetMask,
       "rmConfigDateTime": rmConfigDateTime,
       "rmConfigDate": rmConfigDate,
       "rmConfigTime": rmConfigTime,
       "rmConfigTimeFromNtp": rmConfigTimeFromNtp,
       "rmConfigNtpIpAddress": rmConfigNtpIpAddress,
       "rmConfigNtpTimeZone": rmConfigNtpTimeZone,
       "rmConfigDayLightSaving": rmConfigDayLightSaving,
       "rmConfigLog": rmConfigLog,
       "rmConfigHistoryLogFrequency": rmConfigHistoryLogFrequency,
       "rmConfigExtHistoryLogFrequency": rmConfigExtHistoryLogFrequency,
       "rmConfigConfigurationLog": rmConfigConfigurationLog,
       "rmConfigDhcpStatue": rmConfigDhcpStatue,
       "rmConfigPingStatue": rmConfigPingStatue,
       "rmConfigTftpStatue": rmConfigTftpStatue,
       "rmConfigTelnet": rmConfigTelnet,
       "rmConfigTelnetStatue": rmConfigTelnetStatue,
       "rmConfigTelnetPortNumber": rmConfigTelnetPortNumber,
       "rmConfigHttp": rmConfigHttp,
       "rmConfigHttpStatue": rmConfigHttpStatue,
       "rmConfigHttpPortNumber": rmConfigHttpPortNumber,
       "rmConfigHttpSecurity": rmConfigHttpSecurity,
       "rmConfigSnmp": rmConfigSnmp,
       "rmConfigSnmpStatue": rmConfigSnmpStatue,
       "rmConfigSnmpPortNumber": rmConfigSnmpPortNumber,
       "rmConfigControl": rmConfigControl,
       "rmConfigResetToDefault": rmConfigResetToDefault,
       "rmConfigRestart": rmConfigRestart,
       "rmConfigTrap": rmConfigTrap,
       "rmConfigTrapRetryCount": rmConfigTrapRetryCount,
       "rmConfigTrapRetryTime": rmConfigTrapRetryTime,
       "rmConfigTrapAckSignature": rmConfigTrapAckSignature,
       "rmConfigPollRate": rmConfigPollRate,
       "rmConfigTrapsReceiversTable": rmConfigTrapsReceiversTable,
       "rmConfigTrapsReceiversEntry": rmConfigTrapsReceiversEntry,
       "trapsIndex": trapsIndex,
       "trapsReceiverAddr": trapsReceiverAddr,
       "receiverCommunityString": receiverCommunityString,
       "receiverSeverityLevel": receiverSeverityLevel,
       "receiverDescription": receiverDescription,
       "rmConfigAccessControlTable": rmConfigAccessControlTable,
       "rmConfigAccessControlEntry": rmConfigAccessControlEntry,
       "accessIndex": accessIndex,
       "accessControlAddr": accessControlAddr,
       "accessCommunityString": accessCommunityString,
       "accessControlMode": accessControlMode,
       "rmConfigTemperatureUnit": rmConfigTemperatureUnit,
       "rmConfigDateFormat": rmConfigDateFormat,
       "sensorMonitor": sensorMonitor,
       "smSensorNumber": smSensorNumber,
       "smSensorTable": smSensorTable,
       "smSensorEntry": smSensorEntry,
       "smDeviceIndex": smDeviceIndex,
       "smDeviceStatus": smDeviceStatus,
       "smDeviceTemperature": smDeviceTemperature,
       "smDeviceTemperatureAlarm": smDeviceTemperatureAlarm,
       "smDeviceHumidity": smDeviceHumidity,
       "smDeviceHumidityAlarm": smDeviceHumidityAlarm,
       "smAlarm1": smAlarm1,
       "smAlarm2": smAlarm2,
       "sensorConfig": sensorConfig,
       "scSensorNumber": scSensorNumber,
       "scSensorTable": scSensorTable,
       "scSensorEntry": scSensorEntry,
       "scDeviceIndex": scDeviceIndex,
       "scDeviceName": scDeviceName,
       "scDeviceState": scDeviceState,
       "scSensor1": scSensor1,
       "scSensor1DeviceName": scSensor1DeviceName,
       "scSensor1DeviceState": scSensor1DeviceState,
       "scSensor1Temperature": scSensor1Temperature,
       "scSensor1TemperatureName": scSensor1TemperatureName,
       "scSensor1TemperatureLowWarning": scSensor1TemperatureLowWarning,
       "scSensor1TemperatureLowCritical": scSensor1TemperatureLowCritical,
       "scSensor1TemperatureHighWarning": scSensor1TemperatureHighWarning,
       "scSensor1TemperatureHighCritical": scSensor1TemperatureHighCritical,
       "scSensor1TemperatureHysteresis": scSensor1TemperatureHysteresis,
       "scSensor1TemperatureCalibration": scSensor1TemperatureCalibration,
       "scSensor1TemperatureLowWarningStatus": scSensor1TemperatureLowWarningStatus,
       "scSensor1TemperatureLowCriticalStatus": scSensor1TemperatureLowCriticalStatus,
       "scSensor1TemperatureHighWarningStatus": scSensor1TemperatureHighWarningStatus,
       "scSensor1TemperatureHighCriticalStatus": scSensor1TemperatureHighCriticalStatus,
       "scSensor1Humidity": scSensor1Humidity,
       "scSensor1HumdityName": scSensor1HumdityName,
       "scSensor1HumidityLowWarning": scSensor1HumidityLowWarning,
       "scSensor1HumidityLowCritical": scSensor1HumidityLowCritical,
       "scSensor1HumidityHighWarning": scSensor1HumidityHighWarning,
       "scSensor1HumidityHighCritical": scSensor1HumidityHighCritical,
       "scSensor1HumidityHysteresis": scSensor1HumidityHysteresis,
       "scSensor1HumidityCalibration": scSensor1HumidityCalibration,
       "scSensor1HumidityLowWarningStatus": scSensor1HumidityLowWarningStatus,
       "scSensor1HumidityLowCriticalStatus": scSensor1HumidityLowCriticalStatus,
       "scSensor1HumidityHighWarningStatus": scSensor1HumidityHighWarningStatus,
       "scSensor1HumidityHighCriticalStatus": scSensor1HumidityHighCriticalStatus,
       "scSensor1Alarm1": scSensor1Alarm1,
       "scSensor1Alarm1Name": scSensor1Alarm1Name,
       "scSensor1Alarm1State": scSensor1Alarm1State,
       "scSensor1Alarm1Hysteresis": scSensor1Alarm1Hysteresis,
       "scSensor1Alarm2": scSensor1Alarm2,
       "scSensor1Alarm2Name": scSensor1Alarm2Name,
       "scSensor1Alarm2State": scSensor1Alarm2State,
       "scSensor1Alarm2Hysteresis": scSensor1Alarm2Hysteresis,
       "scSensor2": scSensor2,
       "scSensor2DeviceName": scSensor2DeviceName,
       "scSensor2DeviceState": scSensor2DeviceState,
       "scSensor2Temperature": scSensor2Temperature,
       "scSensor2TemperatureName": scSensor2TemperatureName,
       "scSensor2TemperatureLowWarning": scSensor2TemperatureLowWarning,
       "scSensor2TemperatureLowCritical": scSensor2TemperatureLowCritical,
       "scSensor2TemperatureHighWarning": scSensor2TemperatureHighWarning,
       "scSensor2TemperatureHighCritical": scSensor2TemperatureHighCritical,
       "scSensor2TemperatureHysteresis": scSensor2TemperatureHysteresis,
       "scSensor2TemperatureCalibration": scSensor2TemperatureCalibration,
       "scSensor2TemperatureLowWarningStatus": scSensor2TemperatureLowWarningStatus,
       "scSensor2TemperatureLowCriticalStatus": scSensor2TemperatureLowCriticalStatus,
       "scSensor2TemperatureHighWarningStatus": scSensor2TemperatureHighWarningStatus,
       "scSensor2TemperatureHighCriticalStatus": scSensor2TemperatureHighCriticalStatus,
       "scSensor2Humidity": scSensor2Humidity,
       "scSensor2HumdityName": scSensor2HumdityName,
       "scSensor2HumidityLowWarning": scSensor2HumidityLowWarning,
       "scSensor2HumidityLowCritical": scSensor2HumidityLowCritical,
       "scSensor2HumidityHighWarning": scSensor2HumidityHighWarning,
       "scSensor2HumidityHighCritical": scSensor2HumidityHighCritical,
       "scSensor2HumidityHysteresis": scSensor2HumidityHysteresis,
       "scSensor2HumidityCalibration": scSensor2HumidityCalibration,
       "scSensor2HumidityLowWarningStatus": scSensor2HumidityLowWarningStatus,
       "scSensor2HumidityLowCriticalStatus": scSensor2HumidityLowCriticalStatus,
       "scSensor2HumidityHighWarningStatus": scSensor2HumidityHighWarningStatus,
       "scSensor2HumidityHighCriticalStatus": scSensor2HumidityHighCriticalStatus,
       "scSensor2Alarm1": scSensor2Alarm1,
       "scSensor2Alarm1Name": scSensor2Alarm1Name,
       "scSensor2Alarm1State": scSensor2Alarm1State,
       "scSensor2Alarm1Hysteresis": scSensor2Alarm1Hysteresis,
       "scSensor2Alarm2": scSensor2Alarm2,
       "scSensor2Alarm2Name": scSensor2Alarm2Name,
       "scSensor2Alarm2State": scSensor2Alarm2State,
       "scSensor2Alarm2Hysteresis": scSensor2Alarm2Hysteresis,
       "rmTraps": rmTraps,
       "rmCommunicationRestored": rmCommunicationRestored,
       "rmCommunicationLost": rmCommunicationLost,
       "rmAlarm1Inactive": rmAlarm1Inactive,
       "rmAlarm1Active": rmAlarm1Active,
       "rmAlarm2Inactive": rmAlarm2Inactive,
       "rmAlarm2Active": rmAlarm2Active,
       "rmTemperatureNotHighWarning": rmTemperatureNotHighWarning,
       "rmTemperatureHighWarning": rmTemperatureHighWarning,
       "rmTemperatureNotLowWarning": rmTemperatureNotLowWarning,
       "rmTemperatureLowWarning": rmTemperatureLowWarning,
       "rmTemperatureNotHighCritical": rmTemperatureNotHighCritical,
       "rmTemperatureHighCritical": rmTemperatureHighCritical,
       "rmTemperatureNotLowCritical": rmTemperatureNotLowCritical,
       "rmTemperatureLowCritical": rmTemperatureLowCritical,
       "rmHumidityNotHighWarning": rmHumidityNotHighWarning,
       "rmHumidityHighWarning": rmHumidityHighWarning,
       "rmHumidityNotLowWarning": rmHumidityNotLowWarning,
       "rmHumidityLowWarning": rmHumidityLowWarning,
       "rmHumidityNotHighCritical": rmHumidityNotHighCritical,
       "rmHumidityHighCritical": rmHumidityHighCritical,
       "rmHumidityNotLowCritical": rmHumidityNotLowCritical,
       "rmHumidityLowCritical": rmHumidityLowCritical}
)
