# SNMP MIB module (CIENA-WS-TYPEDEFS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CIENA-WS-TYPEDEFS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:11 2024
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

(cienaWsConfig,) = mibBuilder.importSymbols(
    "CIENA-WS-MIB",
    "cienaWsConfig")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

cienaWsTypedefsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 13)
)
cienaWsTypedefsMIB.setRevisions(
        ("2016-12-12 00:00",
         "2016-03-03 00:00",
         "2015-02-25 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ChannelsNumber(Unsigned32, TextualConvention):
    status = "current"


class ConnectorTypeDescEnum(Integer32, TextualConvention):
    status = "current"
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
              32,
              33,
              34,
              35,
              36)
        )
    )
    namedValues = NamedValues(
        *(("bnc", 4),
          ("copperpigtail", 33),
          ("fiberjack", 6),
          ("fibrechannelcoaxheaders", 5),
          ("fibrechannelstyle1copperconnector", 2),
          ("fibrechannelstyle2copperconnector", 3),
          ("hssdcii", 32),
          ("lc", 7),
          ("mpo1x12", 12),
          ("mpo2x16", 13),
          ("mtrj", 8),
          ("mu", 9),
          ("mxc2x16", 36),
          ("noseparableconnector", 35),
          ("opticalpigtail", 11),
          ("rj45", 34),
          ("sc", 1),
          ("sg", 10),
          ("unknownorunspecified", 0))
    )



class Decimal1Dig(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-1"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483640, 2147483640),
    )



class Decimal2Dig(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-2"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483600, 2147483600),
    )



class Decimal2DigSmall(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-2"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-3000000, 3000000),
    )



class Decimal3Dig(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-3"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483000, 2147483000),
    )



class DescriptionString(OctetString, TextualConvention):
    status = "current"
    displayHint = "128a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )



class EnabledDisabledEnum(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )



class EnabledDisabledNaEnum(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("na", 2))
    )



class EnhancedOptsEnum(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("no", 2),
          ("yes", 1))
    )



class LicenseStatusEnum(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("compliant", 1),
          ("notcompliant", 0))
    )



class LineModuleTypeBits(Bits, TextualConvention):
    status = "current"


class LineSysEnum(Integer32, TextualConvention):
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
        *(("coloured", 0),
          ("colourless", 1),
          ("contentionless", 2),
          ("cscolored", 3),
          ("cscolorless", 4))
    )



class MacString(OctetString, TextualConvention):
    status = "current"
    displayHint = "20a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )



class ModemChannel(Integer32, TextualConvention):
    status = "current"


class ModemFrequency(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-1"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483640, 2147483640),
    )



class ModuleTypeBits(Bits, TextualConvention):
    status = "current"


class ModuleTypeEnum(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fieldreplaceable", 2),
          ("integrated", 1),
          ("unknown", 0))
    )



class NameString(OctetString, TextualConvention):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class OnOffEnum(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
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



class PortId(Unsigned32, TextualConvention):
    status = "current"


class PortName(OctetString, TextualConvention):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class PtpId(Unsigned32, TextualConvention):
    status = "current"


class RecoverLinkDispersionType(Integer32, TextualConvention):
    status = "current"


class ServiceDomainIdx(Unsigned32, TextualConvention):
    status = "current"


class ServiceIdx(Unsigned32, TextualConvention):
    status = "current"


class StringMaxl128(OctetString, TextualConvention):
    status = "current"
    displayHint = "128a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )



class StringMaxl16(OctetString, TextualConvention):
    status = "current"
    displayHint = "16a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class StringMaxl254(OctetString, TextualConvention):
    status = "current"
    displayHint = "254a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )



class StringMaxl256(OctetString, TextualConvention):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class StringMaxl32(OctetString, TextualConvention):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class StringMaxl50(OctetString, TextualConvention):
    status = "current"
    displayHint = "50a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )



class StringMaxl64(OctetString, TextualConvention):
    status = "current"
    displayHint = "64a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class StringSci(OctetString, TextualConvention):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class TxPowerLvl(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-1"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483640, 2147483640),
    )



class UpDownEnum(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )



class VendorDateString(OctetString, TextualConvention):
    status = "current"
    displayHint = "9a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )



class VendorRvString(OctetString, TextualConvention):
    status = "current"
    displayHint = "4a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )



class WlSpacing(Integer32, TextualConvention):
    status = "current"
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
        *(("fixed100ghz", 1),
          ("fixed200ghz", 2),
          ("fixed50ghz", 0),
          ("flexgrid", 3))
    )



class XcvrId(Unsigned32, TextualConvention):
    status = "current"


class XcvrMode(Integer32, TextualConvention):
    status = "current"
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
        *(("blank", 0),
          ("mode100gig", 3),
          ("mode10gig", 1),
          ("mode16qam", 4),
          ("mode40gig", 2),
          ("mode8qam", 6),
          ("modeqpsk", 5))
    )



class XcvrType(Integer32, TextualConvention):
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
        *(("notavailable", 0),
          ("qsfp28", 3),
          ("qsfpplus", 2),
          ("unsupported", 1),
          ("wavelogic3extreme", 4))
    )



class YesNoEnum(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )



class YesNoNaEnum(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na", 2),
          ("no", 0),
          ("yes", 1))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-WS-TYPEDEFS-MIB",
    **{"ChannelsNumber": ChannelsNumber,
       "ConnectorTypeDescEnum": ConnectorTypeDescEnum,
       "Decimal1Dig": Decimal1Dig,
       "Decimal2Dig": Decimal2Dig,
       "Decimal2DigSmall": Decimal2DigSmall,
       "Decimal3Dig": Decimal3Dig,
       "DescriptionString": DescriptionString,
       "EnabledDisabledEnum": EnabledDisabledEnum,
       "EnabledDisabledNaEnum": EnabledDisabledNaEnum,
       "EnhancedOptsEnum": EnhancedOptsEnum,
       "LicenseStatusEnum": LicenseStatusEnum,
       "LineModuleTypeBits": LineModuleTypeBits,
       "LineSysEnum": LineSysEnum,
       "MacString": MacString,
       "ModemChannel": ModemChannel,
       "ModemFrequency": ModemFrequency,
       "ModuleTypeBits": ModuleTypeBits,
       "ModuleTypeEnum": ModuleTypeEnum,
       "NameString": NameString,
       "OnOffEnum": OnOffEnum,
       "PortId": PortId,
       "PortName": PortName,
       "PtpId": PtpId,
       "RecoverLinkDispersionType": RecoverLinkDispersionType,
       "ServiceDomainIdx": ServiceDomainIdx,
       "ServiceIdx": ServiceIdx,
       "StringMaxl128": StringMaxl128,
       "StringMaxl16": StringMaxl16,
       "StringMaxl254": StringMaxl254,
       "StringMaxl256": StringMaxl256,
       "StringMaxl32": StringMaxl32,
       "StringMaxl50": StringMaxl50,
       "StringMaxl64": StringMaxl64,
       "StringSci": StringSci,
       "TxPowerLvl": TxPowerLvl,
       "UpDownEnum": UpDownEnum,
       "VendorDateString": VendorDateString,
       "VendorRvString": VendorRvString,
       "WlSpacing": WlSpacing,
       "XcvrId": XcvrId,
       "XcvrMode": XcvrMode,
       "XcvrType": XcvrType,
       "YesNoEnum": YesNoEnum,
       "YesNoNaEnum": YesNoNaEnum,
       "cienaWsTypedefsMIB": cienaWsTypedefsMIB}
)
