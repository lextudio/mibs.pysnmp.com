# SNMP MIB module (NETWORTH-FASTPIPES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETWORTH-FASTPIPES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:21 2024
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

_Networth_ObjectIdentity = ObjectIdentity
networth = _Networth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 215)
)
_NetworthProducts_ObjectIdentity = ObjectIdentity
networthProducts = _NetworthProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 215, 1)
)
_NetworthInternetworking_ObjectIdentity = ObjectIdentity
networthInternetworking = _NetworthInternetworking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 215, 1, 2)
)
_NwFastPipes_ObjectIdentity = ObjectIdentity
nwFastPipes = _NwFastPipes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2)
)


class _NwfpProductType_Type(DisplayString):
    """Custom type nwfpProductType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NwfpProductType_Type.__name__ = "DisplayString"
_NwfpProductType_Object = MibScalar
nwfpProductType = _NwfpProductType_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 1),
    _NwfpProductType_Type()
)
nwfpProductType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwfpProductType.setStatus("mandatory")


class _NwfpReset_Type(Integer32):
    """Custom type nwfpReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no-reset", 1),
          ("reset", 2),
          ("reset-and-erase-config", 3))
    )


_NwfpReset_Type.__name__ = "Integer32"
_NwfpReset_Object = MibScalar
nwfpReset = _NwfpReset_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 2),
    _NwfpReset_Type()
)
nwfpReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwfpReset.setStatus("mandatory")


class _NwfpCurrentSoftwareVersion_Type(DisplayString):
    """Custom type nwfpCurrentSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_NwfpCurrentSoftwareVersion_Type.__name__ = "DisplayString"
_NwfpCurrentSoftwareVersion_Object = MibScalar
nwfpCurrentSoftwareVersion = _NwfpCurrentSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 3),
    _NwfpCurrentSoftwareVersion_Type()
)
nwfpCurrentSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwfpCurrentSoftwareVersion.setStatus("mandatory")


class _NwfpFutureSoftwareVersion_Type(DisplayString):
    """Custom type nwfpFutureSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_NwfpFutureSoftwareVersion_Type.__name__ = "DisplayString"
_NwfpFutureSoftwareVersion_Object = MibScalar
nwfpFutureSoftwareVersion = _NwfpFutureSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 4),
    _NwfpFutureSoftwareVersion_Type()
)
nwfpFutureSoftwareVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwfpFutureSoftwareVersion.setStatus("mandatory")
_NwfpTFTPServerIPAddress_Type = IpAddress
_NwfpTFTPServerIPAddress_Object = MibScalar
nwfpTFTPServerIPAddress = _NwfpTFTPServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 5),
    _NwfpTFTPServerIPAddress_Type()
)
nwfpTFTPServerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwfpTFTPServerIPAddress.setStatus("mandatory")


class _NwfpCurrentUplinkSoftwareVers_Type(DisplayString):
    """Custom type nwfpCurrentUplinkSoftwareVers based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_NwfpCurrentUplinkSoftwareVers_Type.__name__ = "DisplayString"
_NwfpCurrentUplinkSoftwareVers_Object = MibScalar
nwfpCurrentUplinkSoftwareVers = _NwfpCurrentUplinkSoftwareVers_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 6),
    _NwfpCurrentUplinkSoftwareVers_Type()
)
nwfpCurrentUplinkSoftwareVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwfpCurrentUplinkSoftwareVers.setStatus("mandatory")


class _NwfpFutureUplinkSoftwareVers_Type(DisplayString):
    """Custom type nwfpFutureUplinkSoftwareVers based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_NwfpFutureUplinkSoftwareVers_Type.__name__ = "DisplayString"
_NwfpFutureUplinkSoftwareVers_Object = MibScalar
nwfpFutureUplinkSoftwareVers = _NwfpFutureUplinkSoftwareVers_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 7),
    _NwfpFutureUplinkSoftwareVers_Type()
)
nwfpFutureUplinkSoftwareVers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwfpFutureUplinkSoftwareVers.setStatus("mandatory")
_NwfpLastFailureReason_Type = Integer32
_NwfpLastFailureReason_Object = MibScalar
nwfpLastFailureReason = _NwfpLastFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 8),
    _NwfpLastFailureReason_Type()
)
nwfpLastFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwfpLastFailureReason.setStatus("mandatory")


class _NwfpEEPROMVersion_Type(DisplayString):
    """Custom type nwfpEEPROMVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NwfpEEPROMVersion_Type.__name__ = "DisplayString"
_NwfpEEPROMVersion_Object = MibScalar
nwfpEEPROMVersion = _NwfpEEPROMVersion_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 9),
    _NwfpEEPROMVersion_Type()
)
nwfpEEPROMVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwfpEEPROMVersion.setStatus("mandatory")


class _NwfpManufactureDate_Type(DisplayString):
    """Custom type nwfpManufactureDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NwfpManufactureDate_Type.__name__ = "DisplayString"
_NwfpManufactureDate_Object = MibScalar
nwfpManufactureDate = _NwfpManufactureDate_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 10),
    _NwfpManufactureDate_Type()
)
nwfpManufactureDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwfpManufactureDate.setStatus("mandatory")
_NwfpAuthErrIPaddress_Type = IpAddress
_NwfpAuthErrIPaddress_Object = MibScalar
nwfpAuthErrIPaddress = _NwfpAuthErrIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 11),
    _NwfpAuthErrIPaddress_Type()
)
nwfpAuthErrIPaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwfpAuthErrIPaddress.setStatus("mandatory")


class _NwfpRAMsize_Type(Integer32):
    """Custom type nwfpRAMsize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("eight-MB", 8),
          ("four-MB", 4),
          ("one-MB", 1),
          ("two-MB", 2))
    )


_NwfpRAMsize_Type.__name__ = "Integer32"
_NwfpRAMsize_Object = MibScalar
nwfpRAMsize = _NwfpRAMsize_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 12),
    _NwfpRAMsize_Type()
)
nwfpRAMsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwfpRAMsize.setStatus("mandatory")
_NwfpEthernetTable_Object = MibTable
nwfpEthernetTable = _NwfpEthernetTable_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 13)
)
if mibBuilder.loadTexts:
    nwfpEthernetTable.setStatus("mandatory")
_NwfpEthernetEntry_Object = MibTableRow
nwfpEthernetEntry = _NwfpEthernetEntry_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 13, 1)
)
nwfpEthernetEntry.setIndexNames(
    (0, "NETWORTH-FASTPIPES-MIB", "nwfpIfIndex"),
)
if mibBuilder.loadTexts:
    nwfpEthernetEntry.setStatus("mandatory")


class _NwfpIfIndex_Type(Integer32):
    """Custom type nwfpIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_NwfpIfIndex_Type.__name__ = "Integer32"
_NwfpIfIndex_Object = MibTableColumn
nwfpIfIndex = _NwfpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 13, 1, 1),
    _NwfpIfIndex_Type()
)
nwfpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwfpIfIndex.setStatus("mandatory")


class _NwfpBOOTPrequestFlag_Type(Integer32):
    """Custom type nwfpBOOTPrequestFlag based on Integer32"""
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


_NwfpBOOTPrequestFlag_Type.__name__ = "Integer32"
_NwfpBOOTPrequestFlag_Object = MibTableColumn
nwfpBOOTPrequestFlag = _NwfpBOOTPrequestFlag_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 13, 1, 2),
    _NwfpBOOTPrequestFlag_Type()
)
nwfpBOOTPrequestFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwfpBOOTPrequestFlag.setStatus("mandatory")
_NwfpBOOTPServerIPAddress_Type = IpAddress
_NwfpBOOTPServerIPAddress_Object = MibScalar
nwfpBOOTPServerIPAddress = _NwfpBOOTPServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 18),
    _NwfpBOOTPServerIPAddress_Type()
)
nwfpBOOTPServerIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwfpBOOTPServerIPAddress.setStatus("mandatory")
_NwfpBOOTPEthernetIF_Type = Integer32
_NwfpBOOTPEthernetIF_Object = MibScalar
nwfpBOOTPEthernetIF = _NwfpBOOTPEthernetIF_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 19),
    _NwfpBOOTPEthernetIF_Type()
)
nwfpBOOTPEthernetIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwfpBOOTPEthernetIF.setStatus("mandatory")


class _NwfpUplinkSoftwarePath_Type(DisplayString):
    """Custom type nwfpUplinkSoftwarePath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NwfpUplinkSoftwarePath_Type.__name__ = "DisplayString"
_NwfpUplinkSoftwarePath_Object = MibScalar
nwfpUplinkSoftwarePath = _NwfpUplinkSoftwarePath_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 20),
    _NwfpUplinkSoftwarePath_Type()
)
nwfpUplinkSoftwarePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwfpUplinkSoftwarePath.setStatus("mandatory")


class _NwfpSerialNumber_Type(DisplayString):
    """Custom type nwfpSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NwfpSerialNumber_Type.__name__ = "DisplayString"
_NwfpSerialNumber_Object = MibScalar
nwfpSerialNumber = _NwfpSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 21),
    _NwfpSerialNumber_Type()
)
nwfpSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwfpSerialNumber.setStatus("mandatory")


class _NwfpConfiguration_Type(Integer32):
    """Custom type nwfpConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(500,
              501,
              502,
              503,
              504)
        )
    )
    namedValues = NamedValues(
        *(("fsp11", 502),
          ("fsp12", 500),
          ("fsp12fx", 503),
          ("fsp6", 501),
          ("fsp6fl", 504))
    )


_NwfpConfiguration_Type.__name__ = "Integer32"
_NwfpConfiguration_Object = MibScalar
nwfpConfiguration = _NwfpConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 22),
    _NwfpConfiguration_Type()
)
nwfpConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwfpConfiguration.setStatus("mandatory")


class _NwfpUpLinkEEPROMVersion_Type(DisplayString):
    """Custom type nwfpUpLinkEEPROMVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NwfpUpLinkEEPROMVersion_Type.__name__ = "DisplayString"
_NwfpUpLinkEEPROMVersion_Object = MibScalar
nwfpUpLinkEEPROMVersion = _NwfpUpLinkEEPROMVersion_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 23),
    _NwfpUpLinkEEPROMVersion_Type()
)
nwfpUpLinkEEPROMVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwfpUpLinkEEPROMVersion.setStatus("mandatory")


class _NwfpUpLinkManufactureDate_Type(DisplayString):
    """Custom type nwfpUpLinkManufactureDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NwfpUpLinkManufactureDate_Type.__name__ = "DisplayString"
_NwfpUpLinkManufactureDate_Object = MibScalar
nwfpUpLinkManufactureDate = _NwfpUpLinkManufactureDate_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 24),
    _NwfpUpLinkManufactureDate_Type()
)
nwfpUpLinkManufactureDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwfpUpLinkManufactureDate.setStatus("mandatory")


class _NwfpUpLinkSerialNumber_Type(DisplayString):
    """Custom type nwfpUpLinkSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NwfpUpLinkSerialNumber_Type.__name__ = "DisplayString"
_NwfpUpLinkSerialNumber_Object = MibScalar
nwfpUpLinkSerialNumber = _NwfpUpLinkSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 25),
    _NwfpUpLinkSerialNumber_Type()
)
nwfpUpLinkSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwfpUpLinkSerialNumber.setStatus("mandatory")


class _NwfpUpLinkConfiguration_Type(Integer32):
    """Custom type nwfpUpLinkConfiguration based on Integer32"""
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
        *(("atm", 8),
          ("ethernet-100mbps-fx", 7),
          ("ethernet-100mbps-t4", 5),
          ("ethernet-100mbps-tx", 6),
          ("fddi-fiber-das", 2),
          ("fddi-fiber-sas", 3),
          ("fddi-tppmd-sas", 4),
          ("none", 1))
    )


_NwfpUpLinkConfiguration_Type.__name__ = "Integer32"
_NwfpUpLinkConfiguration_Object = MibScalar
nwfpUpLinkConfiguration = _NwfpUpLinkConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 26),
    _NwfpUpLinkConfiguration_Type()
)
nwfpUpLinkConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwfpUpLinkConfiguration.setStatus("mandatory")


class _NwfpSoftwarePath_Type(DisplayString):
    """Custom type nwfpSoftwarePath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NwfpSoftwarePath_Type.__name__ = "DisplayString"
_NwfpSoftwarePath_Object = MibScalar
nwfpSoftwarePath = _NwfpSoftwarePath_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 27),
    _NwfpSoftwarePath_Type()
)
nwfpSoftwarePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwfpSoftwarePath.setStatus("mandatory")


class _NwfpCurrentBooterSoftwareVersion_Type(DisplayString):
    """Custom type nwfpCurrentBooterSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_NwfpCurrentBooterSoftwareVersion_Type.__name__ = "DisplayString"
_NwfpCurrentBooterSoftwareVersion_Object = MibScalar
nwfpCurrentBooterSoftwareVersion = _NwfpCurrentBooterSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 28),
    _NwfpCurrentBooterSoftwareVersion_Type()
)
nwfpCurrentBooterSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwfpCurrentBooterSoftwareVersion.setStatus("mandatory")


class _NwfpFutureBooterSoftwareVersion_Type(DisplayString):
    """Custom type nwfpFutureBooterSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_NwfpFutureBooterSoftwareVersion_Type.__name__ = "DisplayString"
_NwfpFutureBooterSoftwareVersion_Object = MibScalar
nwfpFutureBooterSoftwareVersion = _NwfpFutureBooterSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 29),
    _NwfpFutureBooterSoftwareVersion_Type()
)
nwfpFutureBooterSoftwareVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwfpFutureBooterSoftwareVersion.setStatus("mandatory")


class _NwfpBooterSoftwarePath_Type(DisplayString):
    """Custom type nwfpBooterSoftwarePath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NwfpBooterSoftwarePath_Type.__name__ = "DisplayString"
_NwfpBooterSoftwarePath_Object = MibScalar
nwfpBooterSoftwarePath = _NwfpBooterSoftwarePath_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 30),
    _NwfpBooterSoftwarePath_Type()
)
nwfpBooterSoftwarePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwfpBooterSoftwarePath.setStatus("mandatory")


class _NwfpSaveConfig_Type(Integer32):
    """Custom type nwfpSaveConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("config-info-saved", 1),
          ("save-all", 2))
    )


_NwfpSaveConfig_Type.__name__ = "Integer32"
_NwfpSaveConfig_Object = MibScalar
nwfpSaveConfig = _NwfpSaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 31),
    _NwfpSaveConfig_Type()
)
nwfpSaveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwfpSaveConfig.setStatus("mandatory")


class _NwfpFddiIPFrag_Type(Integer32):
    """Custom type nwfpFddiIPFrag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_NwfpFddiIPFrag_Type.__name__ = "Integer32"
_NwfpFddiIPFrag_Object = MibScalar
nwfpFddiIPFrag = _NwfpFddiIPFrag_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 32),
    _NwfpFddiIPFrag_Type()
)
nwfpFddiIPFrag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwfpFddiIPFrag.setStatus("mandatory")


class _NwfpFddiToEthIPTrans_Type(Integer32):
    """Custom type nwfpFddiToEthIPTrans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 3),
          ("ethernet-802-3-RAW", 2),
          ("ethernet-ii", 1))
    )


_NwfpFddiToEthIPTrans_Type.__name__ = "Integer32"
_NwfpFddiToEthIPTrans_Object = MibScalar
nwfpFddiToEthIPTrans = _NwfpFddiToEthIPTrans_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 33),
    _NwfpFddiToEthIPTrans_Type()
)
nwfpFddiToEthIPTrans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwfpFddiToEthIPTrans.setStatus("mandatory")


class _NwfpFddiSNAPToEthIPXTrans_Type(Integer32):
    """Custom type nwfpFddiSNAPToEthIPXTrans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-ii", 1),
          ("ieee8022snap", 2))
    )


_NwfpFddiSNAPToEthIPXTrans_Type.__name__ = "Integer32"
_NwfpFddiSNAPToEthIPXTrans_Object = MibScalar
nwfpFddiSNAPToEthIPXTrans = _NwfpFddiSNAPToEthIPXTrans_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 34),
    _NwfpFddiSNAPToEthIPXTrans_Type()
)
nwfpFddiSNAPToEthIPXTrans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwfpFddiSNAPToEthIPXTrans.setStatus("mandatory")


class _NwfpFddi8022ToEthIPXTrans_Type(Integer32):
    """Custom type nwfpFddi8022ToEthIPXTrans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-802-3-RAW", 1),
          ("ieee8022", 2))
    )


_NwfpFddi8022ToEthIPXTrans_Type.__name__ = "Integer32"
_NwfpFddi8022ToEthIPXTrans_Object = MibScalar
nwfpFddi8022ToEthIPXTrans = _NwfpFddi8022ToEthIPXTrans_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 35),
    _NwfpFddi8022ToEthIPXTrans_Type()
)
nwfpFddi8022ToEthIPXTrans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwfpFddi8022ToEthIPXTrans.setStatus("mandatory")


class _NwfpFddiLocTrafFiltering_Type(Integer32):
    """Custom type nwfpFddiLocTrafFiltering based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_NwfpFddiLocTrafFiltering_Type.__name__ = "Integer32"
_NwfpFddiLocTrafFiltering_Object = MibScalar
nwfpFddiLocTrafFiltering = _NwfpFddiLocTrafFiltering_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 36),
    _NwfpFddiLocTrafFiltering_Type()
)
nwfpFddiLocTrafFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwfpFddiLocTrafFiltering.setStatus("mandatory")


class _NwfpSpanningTreeEnable_Type(Integer32):
    """Custom type nwfpSpanningTreeEnable based on Integer32"""
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


_NwfpSpanningTreeEnable_Type.__name__ = "Integer32"
_NwfpSpanningTreeEnable_Object = MibScalar
nwfpSpanningTreeEnable = _NwfpSpanningTreeEnable_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 37),
    _NwfpSpanningTreeEnable_Type()
)
nwfpSpanningTreeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwfpSpanningTreeEnable.setStatus("mandatory")
_NwfpTpFdbMaxSize_Type = Integer32
_NwfpTpFdbMaxSize_Object = MibScalar
nwfpTpFdbMaxSize = _NwfpTpFdbMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 38),
    _NwfpTpFdbMaxSize_Type()
)
nwfpTpFdbMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwfpTpFdbMaxSize.setStatus("mandatory")
_NwfpTpFdbNbEntriesUsed_Type = Integer32
_NwfpTpFdbNbEntriesUsed_Object = MibScalar
nwfpTpFdbNbEntriesUsed = _NwfpTpFdbNbEntriesUsed_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 39),
    _NwfpTpFdbNbEntriesUsed_Type()
)
nwfpTpFdbNbEntriesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwfpTpFdbNbEntriesUsed.setStatus("mandatory")


class _NwfpEthIPX8023ToFddiTrans_Type(Integer32):
    """Custom type nwfpEthIPX8023ToFddiTrans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-802-3-RAW", 1),
          ("ieee8022", 2))
    )


_NwfpEthIPX8023ToFddiTrans_Type.__name__ = "Integer32"
_NwfpEthIPX8023ToFddiTrans_Object = MibScalar
nwfpEthIPX8023ToFddiTrans = _NwfpEthIPX8023ToFddiTrans_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 40),
    _NwfpEthIPX8023ToFddiTrans_Type()
)
nwfpEthIPX8023ToFddiTrans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwfpEthIPX8023ToFddiTrans.setStatus("mandatory")
_NwfpPowerSupplyNumber_Type = Integer32
_NwfpPowerSupplyNumber_Object = MibScalar
nwfpPowerSupplyNumber = _NwfpPowerSupplyNumber_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 41),
    _NwfpPowerSupplyNumber_Type()
)
nwfpPowerSupplyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwfpPowerSupplyNumber.setStatus("mandatory")
_NwfpPowerSupplyTable_Object = MibTable
nwfpPowerSupplyTable = _NwfpPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 42)
)
if mibBuilder.loadTexts:
    nwfpPowerSupplyTable.setStatus("mandatory")
_NwfpPowerSupplyEntry_Object = MibTableRow
nwfpPowerSupplyEntry = _NwfpPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 42, 1)
)
nwfpPowerSupplyEntry.setIndexNames(
    (0, "NETWORTH-FASTPIPES-MIB", "nwfpPowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    nwfpPowerSupplyEntry.setStatus("mandatory")
_NwfpPowerSupplyIndex_Type = Integer32
_NwfpPowerSupplyIndex_Object = MibTableColumn
nwfpPowerSupplyIndex = _NwfpPowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 42, 1, 1),
    _NwfpPowerSupplyIndex_Type()
)
nwfpPowerSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwfpPowerSupplyIndex.setStatus("mandatory")


class _NwfpPowerSupplyStatus_Type(Integer32):
    """Custom type nwfpPowerSupplyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bad", 2),
          ("good", 1),
          ("na", 3))
    )


_NwfpPowerSupplyStatus_Type.__name__ = "Integer32"
_NwfpPowerSupplyStatus_Object = MibTableColumn
nwfpPowerSupplyStatus = _NwfpPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 42, 1, 2),
    _NwfpPowerSupplyStatus_Type()
)
nwfpPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwfpPowerSupplyStatus.setStatus("mandatory")
_NwfpFanNumber_Type = Integer32
_NwfpFanNumber_Object = MibScalar
nwfpFanNumber = _NwfpFanNumber_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 43),
    _NwfpFanNumber_Type()
)
nwfpFanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwfpFanNumber.setStatus("mandatory")
_NwfpFanTable_Object = MibTable
nwfpFanTable = _NwfpFanTable_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 44)
)
if mibBuilder.loadTexts:
    nwfpFanTable.setStatus("mandatory")
_NwfpFanEntry_Object = MibTableRow
nwfpFanEntry = _NwfpFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 44, 1)
)
nwfpFanEntry.setIndexNames(
    (0, "NETWORTH-FASTPIPES-MIB", "nwfpFanIndex"),
)
if mibBuilder.loadTexts:
    nwfpFanEntry.setStatus("mandatory")
_NwfpFanIndex_Type = Integer32
_NwfpFanIndex_Object = MibTableColumn
nwfpFanIndex = _NwfpFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 44, 1, 1),
    _NwfpFanIndex_Type()
)
nwfpFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwfpFanIndex.setStatus("mandatory")


class _NwfpFanStatus_Type(Integer32):
    """Custom type nwfpFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bad", 2),
          ("good", 1))
    )


_NwfpFanStatus_Type.__name__ = "Integer32"
_NwfpFanStatus_Object = MibTableColumn
nwfpFanStatus = _NwfpFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 44, 1, 2),
    _NwfpFanStatus_Type()
)
nwfpFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwfpFanStatus.setStatus("mandatory")
_NwfpMonitorPort_Type = Integer32
_NwfpMonitorPort_Object = MibScalar
nwfpMonitorPort = _NwfpMonitorPort_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 45),
    _NwfpMonitorPort_Type()
)
nwfpMonitorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwfpMonitorPort.setStatus("mandatory")
_NwfpMonitorSource_Type = Integer32
_NwfpMonitorSource_Object = MibScalar
nwfpMonitorSource = _NwfpMonitorSource_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 46),
    _NwfpMonitorSource_Type()
)
nwfpMonitorSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwfpMonitorSource.setStatus("mandatory")


class _NwfpMonitorPortStatus_Type(Integer32):
    """Custom type nwfpMonitorPortStatus based on Integer32"""
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


_NwfpMonitorPortStatus_Type.__name__ = "Integer32"
_NwfpMonitorPortStatus_Object = MibScalar
nwfpMonitorPortStatus = _NwfpMonitorPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 215, 1, 2, 2, 47),
    _NwfpMonitorPortStatus_Type()
)
nwfpMonitorPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwfpMonitorPortStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects

nwfpPowerSupplyDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 215, 0, 11)
)
nwfpPowerSupplyDown.setObjects(
      *(("NETWORTH-FASTPIPES-MIB", "nwfpPowerSupplyIndex"),
        ("NETWORTH-FASTPIPES-MIB", "nwfpPowerSupplyStatus"))
)
if mibBuilder.loadTexts:
    nwfpPowerSupplyDown.setStatus(
        ""
    )

nwfpPowerSupplyUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 215, 0, 12)
)
nwfpPowerSupplyUp.setObjects(
      *(("NETWORTH-FASTPIPES-MIB", "nwfpPowerSupplyIndex"),
        ("NETWORTH-FASTPIPES-MIB", "nwfpPowerSupplyStatus"))
)
if mibBuilder.loadTexts:
    nwfpPowerSupplyUp.setStatus(
        ""
    )

nwfpfanDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 215, 0, 13)
)
nwfpfanDown.setObjects(
      *(("NETWORTH-FASTPIPES-MIB", "nwfpFanIndex"),
        ("NETWORTH-FASTPIPES-MIB", "nwfpFanStatus"))
)
if mibBuilder.loadTexts:
    nwfpfanDown.setStatus(
        ""
    )

nwfpfanUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 215, 0, 14)
)
nwfpfanUp.setObjects(
      *(("NETWORTH-FASTPIPES-MIB", "nwfpFanIndex"),
        ("NETWORTH-FASTPIPES-MIB", "nwfpFanStatus"))
)
if mibBuilder.loadTexts:
    nwfpfanUp.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETWORTH-FASTPIPES-MIB",
    **{"networth": networth,
       "nwfpPowerSupplyDown": nwfpPowerSupplyDown,
       "nwfpPowerSupplyUp": nwfpPowerSupplyUp,
       "nwfpfanDown": nwfpfanDown,
       "nwfpfanUp": nwfpfanUp,
       "networthProducts": networthProducts,
       "networthInternetworking": networthInternetworking,
       "nwFastPipes": nwFastPipes,
       "nwfpProductType": nwfpProductType,
       "nwfpReset": nwfpReset,
       "nwfpCurrentSoftwareVersion": nwfpCurrentSoftwareVersion,
       "nwfpFutureSoftwareVersion": nwfpFutureSoftwareVersion,
       "nwfpTFTPServerIPAddress": nwfpTFTPServerIPAddress,
       "nwfpCurrentUplinkSoftwareVers": nwfpCurrentUplinkSoftwareVers,
       "nwfpFutureUplinkSoftwareVers": nwfpFutureUplinkSoftwareVers,
       "nwfpLastFailureReason": nwfpLastFailureReason,
       "nwfpEEPROMVersion": nwfpEEPROMVersion,
       "nwfpManufactureDate": nwfpManufactureDate,
       "nwfpAuthErrIPaddress": nwfpAuthErrIPaddress,
       "nwfpRAMsize": nwfpRAMsize,
       "nwfpEthernetTable": nwfpEthernetTable,
       "nwfpEthernetEntry": nwfpEthernetEntry,
       "nwfpIfIndex": nwfpIfIndex,
       "nwfpBOOTPrequestFlag": nwfpBOOTPrequestFlag,
       "nwfpBOOTPServerIPAddress": nwfpBOOTPServerIPAddress,
       "nwfpBOOTPEthernetIF": nwfpBOOTPEthernetIF,
       "nwfpUplinkSoftwarePath": nwfpUplinkSoftwarePath,
       "nwfpSerialNumber": nwfpSerialNumber,
       "nwfpConfiguration": nwfpConfiguration,
       "nwfpUpLinkEEPROMVersion": nwfpUpLinkEEPROMVersion,
       "nwfpUpLinkManufactureDate": nwfpUpLinkManufactureDate,
       "nwfpUpLinkSerialNumber": nwfpUpLinkSerialNumber,
       "nwfpUpLinkConfiguration": nwfpUpLinkConfiguration,
       "nwfpSoftwarePath": nwfpSoftwarePath,
       "nwfpCurrentBooterSoftwareVersion": nwfpCurrentBooterSoftwareVersion,
       "nwfpFutureBooterSoftwareVersion": nwfpFutureBooterSoftwareVersion,
       "nwfpBooterSoftwarePath": nwfpBooterSoftwarePath,
       "nwfpSaveConfig": nwfpSaveConfig,
       "nwfpFddiIPFrag": nwfpFddiIPFrag,
       "nwfpFddiToEthIPTrans": nwfpFddiToEthIPTrans,
       "nwfpFddiSNAPToEthIPXTrans": nwfpFddiSNAPToEthIPXTrans,
       "nwfpFddi8022ToEthIPXTrans": nwfpFddi8022ToEthIPXTrans,
       "nwfpFddiLocTrafFiltering": nwfpFddiLocTrafFiltering,
       "nwfpSpanningTreeEnable": nwfpSpanningTreeEnable,
       "nwfpTpFdbMaxSize": nwfpTpFdbMaxSize,
       "nwfpTpFdbNbEntriesUsed": nwfpTpFdbNbEntriesUsed,
       "nwfpEthIPX8023ToFddiTrans": nwfpEthIPX8023ToFddiTrans,
       "nwfpPowerSupplyNumber": nwfpPowerSupplyNumber,
       "nwfpPowerSupplyTable": nwfpPowerSupplyTable,
       "nwfpPowerSupplyEntry": nwfpPowerSupplyEntry,
       "nwfpPowerSupplyIndex": nwfpPowerSupplyIndex,
       "nwfpPowerSupplyStatus": nwfpPowerSupplyStatus,
       "nwfpFanNumber": nwfpFanNumber,
       "nwfpFanTable": nwfpFanTable,
       "nwfpFanEntry": nwfpFanEntry,
       "nwfpFanIndex": nwfpFanIndex,
       "nwfpFanStatus": nwfpFanStatus,
       "nwfpMonitorPort": nwfpMonitorPort,
       "nwfpMonitorSource": nwfpMonitorSource,
       "nwfpMonitorPortStatus": nwfpMonitorPortStatus}
)
