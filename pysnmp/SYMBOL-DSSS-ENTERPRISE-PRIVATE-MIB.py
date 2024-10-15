# SNMP MIB module (SYMBOL-DSSS-ENTERPRISE-PRIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SYMBOL-DSSS-ENTERPRISE-PRIVATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:59:38 2024
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

(snmp,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "snmp")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class WEPKeytype128b(OctetString):
    """Custom type WEPKeytype128b based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Symbol_ObjectIdentity = ObjectIdentity
symbol = _Symbol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388)
)
_Spectrum24_ObjectIdentity = ObjectIdentity
spectrum24 = _Spectrum24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 1)
)
_Dsap_ObjectIdentity = ObjectIdentity
dsap = _Dsap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 1, 5)
)
_ApConfigMgmt_ObjectIdentity = ObjectIdentity
apConfigMgmt = _ApConfigMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1)
)
_ApManufactureInfo_ObjectIdentity = ObjectIdentity
apManufactureInfo = _ApManufactureInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 1)
)


class _ApModelnumber_Type(DisplayString):
    """Custom type apModelnumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ApModelnumber_Type.__name__ = "DisplayString"
_ApModelnumber_Object = MibScalar
apModelnumber = _ApModelnumber_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 1, 1),
    _ApModelnumber_Type()
)
apModelnumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apModelnumber.setStatus("mandatory")


class _ApSerialnumber_Type(DisplayString):
    """Custom type apSerialnumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_ApSerialnumber_Type.__name__ = "DisplayString"
_ApSerialnumber_Object = MibScalar
apSerialnumber = _ApSerialnumber_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 1, 2),
    _ApSerialnumber_Type()
)
apSerialnumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSerialnumber.setStatus("mandatory")


class _ApHardwareRev_Type(DisplayString):
    """Custom type apHardwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_ApHardwareRev_Type.__name__ = "DisplayString"
_ApHardwareRev_Object = MibScalar
apHardwareRev = _ApHardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 1, 3),
    _ApHardwareRev_Type()
)
apHardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apHardwareRev.setStatus("mandatory")
_ApMyMacAddr_Type = PhysAddress
_ApMyMacAddr_Object = MibScalar
apMyMacAddr = _ApMyMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 1, 4),
    _ApMyMacAddr_Type()
)
apMyMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMyMacAddr.setStatus("mandatory")


class _ApAPFirmwareRev_Type(DisplayString):
    """Custom type apAPFirmwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_ApAPFirmwareRev_Type.__name__ = "DisplayString"
_ApAPFirmwareRev_Object = MibScalar
apAPFirmwareRev = _ApAPFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 1, 5),
    _ApAPFirmwareRev_Type()
)
apAPFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAPFirmwareRev.setStatus("mandatory")


class _ApRFFirmwareRev_Type(DisplayString):
    """Custom type apRFFirmwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ApRFFirmwareRev_Type.__name__ = "DisplayString"
_ApRFFirmwareRev_Object = MibScalar
apRFFirmwareRev = _ApRFFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 1, 6),
    _ApRFFirmwareRev_Type()
)
apRFFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRFFirmwareRev.setStatus("mandatory")


class _ApMfgDate_Type(DisplayString):
    """Custom type apMfgDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ApMfgDate_Type.__name__ = "DisplayString"
_ApMfgDate_Object = MibScalar
apMfgDate = _ApMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 1, 7),
    _ApMfgDate_Type()
)
apMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMfgDate.setStatus("mandatory")


class _ApHTMLFileRev_Type(DisplayString):
    """Custom type apHTMLFileRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_ApHTMLFileRev_Type.__name__ = "DisplayString"
_ApHTMLFileRev_Object = MibScalar
apHTMLFileRev = _ApHTMLFileRev_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 1, 8),
    _ApHTMLFileRev_Type()
)
apHTMLFileRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apHTMLFileRev.setStatus("mandatory")


class _ApVendorID_Type(Integer32):
    """Custom type apVendorID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("ericsson", 8),
          ("intel", 9),
          ("symbol", 5),
          ("threeCom", 6))
    )


_ApVendorID_Type.__name__ = "Integer32"
_ApVendorID_Object = MibScalar
apVendorID = _ApVendorID_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 1, 9),
    _ApVendorID_Type()
)
apVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apVendorID.setStatus("mandatory")
_ApSystemConfig_ObjectIdentity = ObjectIdentity
apSystemConfig = _ApSystemConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 2)
)


class _ApUnitName_Type(DisplayString):
    """Custom type apUnitName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ApUnitName_Type.__name__ = "DisplayString"
_ApUnitName_Object = MibScalar
apUnitName = _ApUnitName_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 2, 1),
    _ApUnitName_Type()
)
apUnitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apUnitName.setStatus("mandatory")
_ApMyIPAddr_Type = IpAddress
_ApMyIPAddr_Object = MibScalar
apMyIPAddr = _ApMyIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 2, 2),
    _ApMyIPAddr_Type()
)
apMyIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apMyIPAddr.setStatus("mandatory")
_ApSubnetMask_Type = IpAddress
_ApSubnetMask_Object = MibScalar
apSubnetMask = _ApSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 2, 3),
    _ApSubnetMask_Type()
)
apSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSubnetMask.setStatus("mandatory")
_ApGatewayIPAddr_Type = IpAddress
_ApGatewayIPAddr_Object = MibScalar
apGatewayIPAddr = _ApGatewayIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 2, 4),
    _ApGatewayIPAddr_Type()
)
apGatewayIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apGatewayIPAddr.setStatus("mandatory")


class _ApDefaultInterface_Type(Integer32):
    """Custom type apDefaultInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("ppp", 2),
          ("wlap", 3))
    )


_ApDefaultInterface_Type.__name__ = "Integer32"
_ApDefaultInterface_Object = MibScalar
apDefaultInterface = _ApDefaultInterface_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 2, 5),
    _ApDefaultInterface_Type()
)
apDefaultInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apDefaultInterface.setStatus("mandatory")


class _ApEnetPortState_Type(Integer32):
    """Custom type apEnetPortState based on Integer32"""
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


_ApEnetPortState_Type.__name__ = "Integer32"
_ApEnetPortState_Object = MibScalar
apEnetPortState = _ApEnetPortState_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 2, 6),
    _ApEnetPortState_Type()
)
apEnetPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apEnetPortState.setStatus("mandatory")
_ApEthernetTimeOut_Type = Integer32
_ApEthernetTimeOut_Object = MibScalar
apEthernetTimeOut = _ApEthernetTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 2, 7),
    _ApEthernetTimeOut_Type()
)
apEthernetTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apEthernetTimeOut.setStatus("mandatory")


class _ApTelnetEnable_Type(Integer32):
    """Custom type apTelnetEnable based on Integer32"""
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


_ApTelnetEnable_Type.__name__ = "Integer32"
_ApTelnetEnable_Object = MibScalar
apTelnetEnable = _ApTelnetEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 2, 8),
    _ApTelnetEnable_Type()
)
apTelnetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apTelnetEnable.setStatus("mandatory")


class _ApAccCtrlEnable_Type(Integer32):
    """Custom type apAccCtrlEnable based on Integer32"""
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


_ApAccCtrlEnable_Type.__name__ = "Integer32"
_ApAccCtrlEnable_Object = MibScalar
apAccCtrlEnable = _ApAccCtrlEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 2, 9),
    _ApAccCtrlEnable_Type()
)
apAccCtrlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAccCtrlEnable.setStatus("mandatory")


class _ApTypeFilterEnable_Type(Integer32):
    """Custom type apTypeFilterEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("discard", 3),
          ("forward", 2))
    )


_ApTypeFilterEnable_Type.__name__ = "Integer32"
_ApTypeFilterEnable_Object = MibScalar
apTypeFilterEnable = _ApTypeFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 2, 10),
    _ApTypeFilterEnable_Type()
)
apTypeFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apTypeFilterEnable.setStatus("mandatory")


class _ApWNMPEnable_Type(Integer32):
    """Custom type apWNMPEnable based on Integer32"""
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


_ApWNMPEnable_Type.__name__ = "Integer32"
_ApWNMPEnable_Object = MibScalar
apWNMPEnable = _ApWNMPEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 2, 13),
    _ApWNMPEnable_Type()
)
apWNMPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWNMPEnable.setStatus("mandatory")


class _ApAPStateXchgEnable_Type(Integer32):
    """Custom type apAPStateXchgEnable based on Integer32"""
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


_ApAPStateXchgEnable_Type.__name__ = "Integer32"
_ApAPStateXchgEnable_Object = MibScalar
apAPStateXchgEnable = _ApAPStateXchgEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 2, 14),
    _ApAPStateXchgEnable_Type()
)
apAPStateXchgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAPStateXchgEnable.setStatus("mandatory")


class _ApS24MobileIPEnable_Type(Integer32):
    """Custom type apS24MobileIPEnable based on Integer32"""
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


_ApS24MobileIPEnable_Type.__name__ = "Integer32"
_ApS24MobileIPEnable_Object = MibScalar
apS24MobileIPEnable = _ApS24MobileIPEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 2, 15),
    _ApS24MobileIPEnable_Type()
)
apS24MobileIPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apS24MobileIPEnable.setStatus("mandatory")


class _ApAgentAdInterval_Type(Integer32):
    """Custom type apAgentAdInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1200),
    )


_ApAgentAdInterval_Type.__name__ = "Integer32"
_ApAgentAdInterval_Object = MibScalar
apAgentAdInterval = _ApAgentAdInterval_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 2, 16),
    _ApAgentAdInterval_Type()
)
apAgentAdInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAgentAdInterval.setStatus("mandatory")


class _ApWebServerEnable_Type(Integer32):
    """Custom type apWebServerEnable based on Integer32"""
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


_ApWebServerEnable_Type.__name__ = "Integer32"
_ApWebServerEnable_Object = MibScalar
apWebServerEnable = _ApWebServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 2, 17),
    _ApWebServerEnable_Type()
)
apWebServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWebServerEnable.setStatus("mandatory")


class _ApMobileHomeMD5Key_Type(DisplayString):
    """Custom type apMobileHomeMD5Key based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 13),
    )


_ApMobileHomeMD5Key_Type.__name__ = "DisplayString"
_ApMobileHomeMD5Key_Object = MibScalar
apMobileHomeMD5Key = _ApMobileHomeMD5Key_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 2, 18),
    _ApMobileHomeMD5Key_Type()
)
apMobileHomeMD5Key.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apMobileHomeMD5Key.setStatus("mandatory")
_ApAdditionalGatewaysTable_Object = MibTable
apAdditionalGatewaysTable = _ApAdditionalGatewaysTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 2, 19)
)
if mibBuilder.loadTexts:
    apAdditionalGatewaysTable.setStatus("mandatory")
_ApAdditionalGatewaysEntry_Object = MibTableRow
apAdditionalGatewaysEntry = _ApAdditionalGatewaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 2, 19, 1)
)
apAdditionalGatewaysEntry.setIndexNames(
    (0, "SYMBOL-DSSS-ENTERPRISE-PRIVATE-MIB", "additionalGatewaysIndex"),
)
if mibBuilder.loadTexts:
    apAdditionalGatewaysEntry.setStatus("mandatory")


class _AdditionalGatewaysIndex_Type(Integer32):
    """Custom type additionalGatewaysIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AdditionalGatewaysIndex_Type.__name__ = "Integer32"
_AdditionalGatewaysIndex_Object = MibTableColumn
additionalGatewaysIndex = _AdditionalGatewaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 2, 19, 1, 1),
    _AdditionalGatewaysIndex_Type()
)
additionalGatewaysIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    additionalGatewaysIndex.setStatus("mandatory")
_ApAdditionalGatewaysIPAddr_Type = IpAddress
_ApAdditionalGatewaysIPAddr_Object = MibTableColumn
apAdditionalGatewaysIPAddr = _ApAdditionalGatewaysIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 2, 19, 1, 2),
    _ApAdditionalGatewaysIPAddr_Type()
)
apAdditionalGatewaysIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAdditionalGatewaysIPAddr.setStatus("mandatory")


class _ApMUMUDisallowed_Type(Integer32):
    """Custom type apMUMUDisallowed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_ApMUMUDisallowed_Type.__name__ = "Integer32"
_ApMUMUDisallowed_Object = MibScalar
apMUMUDisallowed = _ApMUMUDisallowed_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 2, 20),
    _ApMUMUDisallowed_Type()
)
apMUMUDisallowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apMUMUDisallowed.setStatus("mandatory")


class _ApEncryptAdmin_Type(Integer32):
    """Custom type apEncryptAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 2),
          ("serial", 1))
    )


_ApEncryptAdmin_Type.__name__ = "Integer32"
_ApEncryptAdmin_Object = MibScalar
apEncryptAdmin = _ApEncryptAdmin_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 2, 21),
    _ApEncryptAdmin_Type()
)
apEncryptAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEncryptAdmin.setStatus("mandatory")
_ApSNMPInfo_ObjectIdentity = ObjectIdentity
apSNMPInfo = _ApSNMPInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 3)
)


class _ApSNMPMode_Type(Integer32):
    """Custom type apSNMPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("readonly", 2),
          ("readwrite", 3))
    )


_ApSNMPMode_Type.__name__ = "Integer32"
_ApSNMPMode_Object = MibScalar
apSNMPMode = _ApSNMPMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 3, 1),
    _ApSNMPMode_Type()
)
apSNMPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSNMPMode.setStatus("mandatory")


class _ApROCommunityName_Type(DisplayString):
    """Custom type apROCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ApROCommunityName_Type.__name__ = "DisplayString"
_ApROCommunityName_Object = MibScalar
apROCommunityName = _ApROCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 3, 2),
    _ApROCommunityName_Type()
)
apROCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apROCommunityName.setStatus("mandatory")


class _ApRWCommunityName_Type(DisplayString):
    """Custom type apRWCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 13),
    )


_ApRWCommunityName_Type.__name__ = "DisplayString"
_ApRWCommunityName_Object = MibScalar
apRWCommunityName = _ApRWCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 3, 3),
    _ApRWCommunityName_Type()
)
apRWCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRWCommunityName.setStatus("mandatory")
_ApTrapHost1IpAdr_Type = IpAddress
_ApTrapHost1IpAdr_Object = MibScalar
apTrapHost1IpAdr = _ApTrapHost1IpAdr_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 3, 4),
    _ApTrapHost1IpAdr_Type()
)
apTrapHost1IpAdr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apTrapHost1IpAdr.setStatus("mandatory")


class _ApAllTrapsEnable_Type(Integer32):
    """Custom type apAllTrapsEnable based on Integer32"""
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


_ApAllTrapsEnable_Type.__name__ = "Integer32"
_ApAllTrapsEnable_Object = MibScalar
apAllTrapsEnable = _ApAllTrapsEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 3, 5),
    _ApAllTrapsEnable_Type()
)
apAllTrapsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAllTrapsEnable.setStatus("mandatory")


class _ApColdBootTrapEnable_Type(Integer32):
    """Custom type apColdBootTrapEnable based on Integer32"""
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
        *(("all-TrapHosts", 4),
          ("disabled", 1),
          ("trapHost1", 2),
          ("trapHost2", 3))
    )


_ApColdBootTrapEnable_Type.__name__ = "Integer32"
_ApColdBootTrapEnable_Object = MibScalar
apColdBootTrapEnable = _ApColdBootTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 3, 6),
    _ApColdBootTrapEnable_Type()
)
apColdBootTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apColdBootTrapEnable.setStatus("mandatory")


class _ApAuthenFailureTrapEnable_Type(Integer32):
    """Custom type apAuthenFailureTrapEnable based on Integer32"""
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
        *(("all-TrapHosts", 4),
          ("disabled", 1),
          ("trapHost1", 2),
          ("trapHost2", 3))
    )


_ApAuthenFailureTrapEnable_Type.__name__ = "Integer32"
_ApAuthenFailureTrapEnable_Object = MibScalar
apAuthenFailureTrapEnable = _ApAuthenFailureTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 3, 7),
    _ApAuthenFailureTrapEnable_Type()
)
apAuthenFailureTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAuthenFailureTrapEnable.setStatus("mandatory")


class _ApRFTrapEnable_Type(Integer32):
    """Custom type apRFTrapEnable based on Integer32"""
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
        *(("all-TrapHosts", 4),
          ("disabled", 1),
          ("trapHost1", 2),
          ("trapHost2", 3))
    )


_ApRFTrapEnable_Type.__name__ = "Integer32"
_ApRFTrapEnable_Object = MibScalar
apRFTrapEnable = _ApRFTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 3, 8),
    _ApRFTrapEnable_Type()
)
apRFTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRFTrapEnable.setStatus("mandatory")


class _ApACLTrapEnable_Type(Integer32):
    """Custom type apACLTrapEnable based on Integer32"""
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
        *(("all-TrapHosts", 4),
          ("disabled", 1),
          ("trapHost1", 2),
          ("trapHost2", 3))
    )


_ApACLTrapEnable_Type.__name__ = "Integer32"
_ApACLTrapEnable_Object = MibScalar
apACLTrapEnable = _ApACLTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 3, 9),
    _ApACLTrapEnable_Type()
)
apACLTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apACLTrapEnable.setStatus("mandatory")


class _ApMUStateChngTrapEnable_Type(Integer32):
    """Custom type apMUStateChngTrapEnable based on Integer32"""
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
        *(("all-TrapHosts", 4),
          ("disabled", 1),
          ("trapHost1", 2),
          ("trapHost2", 3))
    )


_ApMUStateChngTrapEnable_Type.__name__ = "Integer32"
_ApMUStateChngTrapEnable_Object = MibScalar
apMUStateChngTrapEnable = _ApMUStateChngTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 3, 10),
    _ApMUStateChngTrapEnable_Type()
)
apMUStateChngTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apMUStateChngTrapEnable.setStatus("mandatory")


class _ApWLAPConnChngTrapEnable_Type(Integer32):
    """Custom type apWLAPConnChngTrapEnable based on Integer32"""
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
        *(("all-TrapHosts", 4),
          ("disabled", 1),
          ("trapHost1", 2),
          ("trapHost2", 3))
    )


_ApWLAPConnChngTrapEnable_Type.__name__ = "Integer32"
_ApWLAPConnChngTrapEnable_Object = MibScalar
apWLAPConnChngTrapEnable = _ApWLAPConnChngTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 3, 11),
    _ApWLAPConnChngTrapEnable_Type()
)
apWLAPConnChngTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWLAPConnChngTrapEnable.setStatus("mandatory")


class _ApDHCPChangeEnable_Type(Integer32):
    """Custom type apDHCPChangeEnable based on Integer32"""
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
        *(("all-TrapHosts", 4),
          ("disabled", 1),
          ("trapHost1", 2),
          ("trapHost2", 3))
    )


_ApDHCPChangeEnable_Type.__name__ = "Integer32"
_ApDHCPChangeEnable_Object = MibScalar
apDHCPChangeEnable = _ApDHCPChangeEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 3, 12),
    _ApDHCPChangeEnable_Type()
)
apDHCPChangeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apDHCPChangeEnable.setStatus("mandatory")
_ApSNMPRequests_Type = Counter32
_ApSNMPRequests_Object = MibScalar
apSNMPRequests = _ApSNMPRequests_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 3, 13),
    _ApSNMPRequests_Type()
)
apSNMPRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSNMPRequests.setStatus("mandatory")
_ApSNMPTraps_Type = Counter32
_ApSNMPTraps_Object = MibScalar
apSNMPTraps = _ApSNMPTraps_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 3, 14),
    _ApSNMPTraps_Type()
)
apSNMPTraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSNMPTraps.setStatus("mandatory")
_ApTrapHost2IpAdr_Type = IpAddress
_ApTrapHost2IpAdr_Object = MibScalar
apTrapHost2IpAdr = _ApTrapHost2IpAdr_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 3, 15),
    _ApTrapHost2IpAdr_Type()
)
apTrapHost2IpAdr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apTrapHost2IpAdr.setStatus("mandatory")
_ApRFConfig_ObjectIdentity = ObjectIdentity
apRFConfig = _ApRFConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 4)
)


class _ApRFPortState_Type(Integer32):
    """Custom type apRFPortState based on Integer32"""
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


_ApRFPortState_Type.__name__ = "Integer32"
_ApRFPortState_Object = MibScalar
apRFPortState = _ApRFPortState_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 4, 1),
    _ApRFPortState_Type()
)
apRFPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRFPortState.setStatus("mandatory")


class _ApNetID_Type(DisplayString):
    """Custom type apNetID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ApNetID_Type.__name__ = "DisplayString"
_ApNetID_Object = MibScalar
apNetID = _ApNetID_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 4, 2),
    _ApNetID_Type()
)
apNetID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apNetID.setStatus("mandatory")
_ApCountryName_Type = DisplayString
_ApCountryName_Object = MibScalar
apCountryName = _ApCountryName_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 4, 5),
    _ApCountryName_Type()
)
apCountryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCountryName.setStatus("mandatory")


class _ApAntennaSelect_Type(Integer32):
    """Custom type apAntennaSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("diversity-On", 2),
          ("primary-only", 1))
    )


_ApAntennaSelect_Type.__name__ = "Integer32"
_ApAntennaSelect_Object = MibScalar
apAntennaSelect = _ApAntennaSelect_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 4, 6),
    _ApAntennaSelect_Type()
)
apAntennaSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAntennaSelect.setStatus("mandatory")


class _ApBCMCQMax_Type(Integer32):
    """Custom type apBCMCQMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_ApBCMCQMax_Type.__name__ = "Integer32"
_ApBCMCQMax_Object = MibScalar
apBCMCQMax = _ApBCMCQMax_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 4, 8),
    _ApBCMCQMax_Type()
)
apBCMCQMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBCMCQMax.setStatus("mandatory")
_ApReassemblyTimeOut_Type = Integer32
_ApReassemblyTimeOut_Object = MibScalar
apReassemblyTimeOut = _ApReassemblyTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 4, 9),
    _ApReassemblyTimeOut_Type()
)
apReassemblyTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apReassemblyTimeOut.setStatus("mandatory")


class _ApMaxRetries_Type(Integer32):
    """Custom type apMaxRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_ApMaxRetries_Type.__name__ = "Integer32"
_ApMaxRetries_Object = MibScalar
apMaxRetries = _ApMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 4, 10),
    _ApMaxRetries_Type()
)
apMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apMaxRetries.setStatus("mandatory")


class _ApMulticastMask_Type(OctetString):
    """Custom type apMulticastMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_ApMulticastMask_Type.__name__ = "OctetString"
_ApMulticastMask_Object = MibScalar
apMulticastMask = _ApMulticastMask_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 4, 11),
    _ApMulticastMask_Type()
)
apMulticastMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apMulticastMask.setStatus("mandatory")


class _ApAcceptBCESSID_Type(Integer32):
    """Custom type apAcceptBCESSID based on Integer32"""
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


_ApAcceptBCESSID_Type.__name__ = "Integer32"
_ApAcceptBCESSID_Object = MibScalar
apAcceptBCESSID = _ApAcceptBCESSID_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 4, 14),
    _ApAcceptBCESSID_Type()
)
apAcceptBCESSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAcceptBCESSID.setStatus("mandatory")


class _ApMUInactivityTimeOut_Type(Integer32):
    """Custom type apMUInactivityTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 600),
    )


_ApMUInactivityTimeOut_Type.__name__ = "Integer32"
_ApMUInactivityTimeOut_Object = MibScalar
apMUInactivityTimeOut = _ApMUInactivityTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 4, 15),
    _ApMUInactivityTimeOut_Type()
)
apMUInactivityTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apMUInactivityTimeOut.setStatus("mandatory")


class _ApWLAPMode_Type(Integer32):
    """Custom type apWLAPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("link-required", 3))
    )


_ApWLAPMode_Type.__name__ = "Integer32"
_ApWLAPMode_Object = MibScalar
apWLAPMode = _ApWLAPMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 4, 16),
    _ApWLAPMode_Type()
)
apWLAPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWLAPMode.setStatus("mandatory")


class _ApWLAPPriority_Type(OctetString):
    """Custom type apWLAPPriority based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_ApWLAPPriority_Type.__name__ = "OctetString"
_ApWLAPPriority_Object = MibScalar
apWLAPPriority = _ApWLAPPriority_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 4, 17),
    _ApWLAPPriority_Type()
)
apWLAPPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWLAPPriority.setStatus("mandatory")
_ApWLAPManualBSSID_Type = PhysAddress
_ApWLAPManualBSSID_Object = MibScalar
apWLAPManualBSSID = _ApWLAPManualBSSID_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 4, 18),
    _ApWLAPManualBSSID_Type()
)
apWLAPManualBSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWLAPManualBSSID.setStatus("mandatory")
_ApWLAPHelloTime_Type = Integer32
_ApWLAPHelloTime_Object = MibScalar
apWLAPHelloTime = _ApWLAPHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 4, 19),
    _ApWLAPHelloTime_Type()
)
apWLAPHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWLAPHelloTime.setStatus("mandatory")
_ApWLAPMaxAge_Type = Integer32
_ApWLAPMaxAge_Object = MibScalar
apWLAPMaxAge = _ApWLAPMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 4, 20),
    _ApWLAPMaxAge_Type()
)
apWLAPMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWLAPMaxAge.setStatus("mandatory")
_ApWLAPFwdDelay_Type = Integer32
_ApWLAPFwdDelay_Object = MibScalar
apWLAPFwdDelay = _ApWLAPFwdDelay_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 4, 21),
    _ApWLAPFwdDelay_Type()
)
apWLAPFwdDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWLAPFwdDelay.setStatus("mandatory")


class _ApMaxMUTrigger_Type(Integer32):
    """Custom type apMaxMUTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ApMaxMUTrigger_Type.__name__ = "Integer32"
_ApMaxMUTrigger_Object = MibScalar
apMaxMUTrigger = _ApMaxMUTrigger_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 4, 24),
    _ApMaxMUTrigger_Type()
)
apMaxMUTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apMaxMUTrigger.setStatus("mandatory")


class _ApMaxRetriesVoice_Type(Integer32):
    """Custom type apMaxRetriesVoice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_ApMaxRetriesVoice_Type.__name__ = "Integer32"
_ApMaxRetriesVoice_Object = MibScalar
apMaxRetriesVoice = _ApMaxRetriesVoice_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 4, 25),
    _ApMaxRetriesVoice_Type()
)
apMaxRetriesVoice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apMaxRetriesVoice.setStatus("mandatory")


class _ApMcastMaskVoice_Type(OctetString):
    """Custom type apMcastMaskVoice based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_ApMcastMaskVoice_Type.__name__ = "OctetString"
_ApMcastMaskVoice_Object = MibScalar
apMcastMaskVoice = _ApMcastMaskVoice_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 4, 26),
    _ApMcastMaskVoice_Type()
)
apMcastMaskVoice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apMcastMaskVoice.setStatus("mandatory")


class _ApWEPAlgorithm_Type(Integer32):
    """Custom type apWEPAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wep-128b-Key", 1),
          ("wep-40b-Key", 2))
    )


_ApWEPAlgorithm_Type.__name__ = "Integer32"
_ApWEPAlgorithm_Object = MibScalar
apWEPAlgorithm = _ApWEPAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 4, 30),
    _ApWEPAlgorithm_Type()
)
apWEPAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWEPAlgorithm.setStatus("mandatory")


class _ApRFRate11Mb_Type(Integer32):
    """Custom type apRFRate11Mb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-used", 2),
          ("optional", 1),
          ("required", 3))
    )


_ApRFRate11Mb_Type.__name__ = "Integer32"
_ApRFRate11Mb_Object = MibScalar
apRFRate11Mb = _ApRFRate11Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 4, 31),
    _ApRFRate11Mb_Type()
)
apRFRate11Mb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRFRate11Mb.setStatus("mandatory")


class _ApRFRate5_5Mb_Type(Integer32):
    """Custom type apRFRate5_5Mb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-used", 2),
          ("optional", 1),
          ("required", 3))
    )


_ApRFRate5_5Mb_Type.__name__ = "Integer32"
_ApRFRate5_5Mb_Object = MibScalar
apRFRate5_5Mb = _ApRFRate5_5Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 4, 32),
    _ApRFRate5_5Mb_Type()
)
apRFRate5_5Mb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRFRate5_5Mb.setStatus("mandatory")


class _ApRFRate2Mb_Type(Integer32):
    """Custom type apRFRate2Mb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-used", 2),
          ("optional", 1),
          ("required", 3))
    )


_ApRFRate2Mb_Type.__name__ = "Integer32"
_ApRFRate2Mb_Object = MibScalar
apRFRate2Mb = _ApRFRate2Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 4, 33),
    _ApRFRate2Mb_Type()
)
apRFRate2Mb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRFRate2Mb.setStatus("mandatory")


class _ApRFRate1Mb_Type(Integer32):
    """Custom type apRFRate1Mb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-used", 2),
          ("optional", 1),
          ("required", 3))
    )


_ApRFRate1Mb_Type.__name__ = "Integer32"
_ApRFRate1Mb_Object = MibScalar
apRFRate1Mb = _ApRFRate1Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 4, 34),
    _ApRFRate1Mb_Type()
)
apRFRate1Mb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRFRate1Mb.setStatus("mandatory")


class _ApRFPreamble_Type(Integer32):
    """Custom type apRFPreamble based on Integer32"""
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


_ApRFPreamble_Type.__name__ = "Integer32"
_ApRFPreamble_Object = MibScalar
apRFPreamble = _ApRFPreamble_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 4, 35),
    _ApRFPreamble_Type()
)
apRFPreamble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRFPreamble.setStatus("mandatory")


class _ApRadioType_Type(Integer32):
    """Custom type apRadioType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ds11-V2", 1),
          ("ds11-v1", 2))
    )


_ApRadioType_Type.__name__ = "Integer32"
_ApRadioType_Object = MibScalar
apRadioType = _ApRadioType_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 4, 36),
    _ApRadioType_Type()
)
apRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioType.setStatus("mandatory")
_ApSerialPortConfig_ObjectIdentity = ObjectIdentity
apSerialPortConfig = _ApSerialPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 5)
)


class _ApPPPState_Type(Integer32):
    """Custom type apPPPState based on Integer32"""
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


_ApPPPState_Type.__name__ = "Integer32"
_ApPPPState_Object = MibScalar
apPPPState = _ApPPPState_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 5, 1),
    _ApPPPState_Type()
)
apPPPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apPPPState.setStatus("mandatory")


class _ApSerialPortUse_Type(Integer32):
    """Custom type apSerialPortUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ppp", 1),
          ("ui", 2))
    )


_ApSerialPortUse_Type.__name__ = "Integer32"
_ApSerialPortUse_Object = MibScalar
apSerialPortUse = _ApSerialPortUse_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 5, 2),
    _ApSerialPortUse_Type()
)
apSerialPortUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSerialPortUse.setStatus("mandatory")


class _ApModemConnected_Type(Integer32):
    """Custom type apModemConnected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_ApModemConnected_Type.__name__ = "Integer32"
_ApModemConnected_Object = MibScalar
apModemConnected = _ApModemConnected_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 5, 3),
    _ApModemConnected_Type()
)
apModemConnected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apModemConnected.setStatus("mandatory")


class _ApConnectMode_Type(Integer32):
    """Custom type apConnectMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("answer", 2),
          ("originate", 1))
    )


_ApConnectMode_Type.__name__ = "Integer32"
_ApConnectMode_Object = MibScalar
apConnectMode = _ApConnectMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 5, 4),
    _ApConnectMode_Type()
)
apConnectMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apConnectMode.setStatus("mandatory")


class _ApDialOutNumber_Type(DisplayString):
    """Custom type apDialOutNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ApDialOutNumber_Type.__name__ = "DisplayString"
_ApDialOutNumber_Object = MibScalar
apDialOutNumber = _ApDialOutNumber_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 5, 5),
    _ApDialOutNumber_Type()
)
apDialOutNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apDialOutNumber.setStatus("mandatory")


class _ApDialOutMode_Type(Integer32):
    """Custom type apDialOutMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_ApDialOutMode_Type.__name__ = "Integer32"
_ApDialOutMode_Object = MibScalar
apDialOutMode = _ApDialOutMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 5, 6),
    _ApDialOutMode_Type()
)
apDialOutMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apDialOutMode.setStatus("mandatory")
_ApAnswerWaitTime_Type = Integer32
_ApAnswerWaitTime_Object = MibScalar
apAnswerWaitTime = _ApAnswerWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 5, 7),
    _ApAnswerWaitTime_Type()
)
apAnswerWaitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAnswerWaitTime.setStatus("mandatory")


class _ApModemSpeaker_Type(Integer32):
    """Custom type apModemSpeaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_ApModemSpeaker_Type.__name__ = "Integer32"
_ApModemSpeaker_Object = MibScalar
apModemSpeaker = _ApModemSpeaker_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 5, 8),
    _ApModemSpeaker_Type()
)
apModemSpeaker.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apModemSpeaker.setStatus("mandatory")
_ApInactivityTimeout_Type = Integer32
_ApInactivityTimeout_Object = MibScalar
apInactivityTimeout = _ApInactivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 5, 9),
    _ApInactivityTimeout_Type()
)
apInactivityTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apInactivityTimeout.setStatus("mandatory")
_ApPPPTimeout_Type = Integer32
_ApPPPTimeout_Object = MibScalar
apPPPTimeout = _ApPPPTimeout_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 5, 10),
    _ApPPPTimeout_Type()
)
apPPPTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apPPPTimeout.setStatus("mandatory")
_ApPPPTerminates_Type = Counter32
_ApPPPTerminates_Object = MibScalar
apPPPTerminates = _ApPPPTerminates_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 5, 11),
    _ApPPPTerminates_Type()
)
apPPPTerminates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apPPPTerminates.setStatus("mandatory")
_ApAddrFilterTable_Object = MibTable
apAddrFilterTable = _ApAddrFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 6)
)
if mibBuilder.loadTexts:
    apAddrFilterTable.setStatus("mandatory")
_ApAddrFilterEntry_Object = MibTableRow
apAddrFilterEntry = _ApAddrFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 6, 1)
)
apAddrFilterEntry.setIndexNames(
    (0, "SYMBOL-DSSS-ENTERPRISE-PRIVATE-MIB", "disallowedIndex"),
)
if mibBuilder.loadTexts:
    apAddrFilterEntry.setStatus("mandatory")


class _DisallowedIndex_Type(Integer32):
    """Custom type disallowedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_DisallowedIndex_Type.__name__ = "Integer32"
_DisallowedIndex_Object = MibTableColumn
disallowedIndex = _DisallowedIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 6, 1, 1),
    _DisallowedIndex_Type()
)
disallowedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disallowedIndex.setStatus("mandatory")
_DisallowedMU_Type = PhysAddress
_DisallowedMU_Object = MibTableColumn
disallowedMU = _DisallowedMU_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 6, 1, 2),
    _DisallowedMU_Type()
)
disallowedMU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    disallowedMU.setStatus("mandatory")
_ApTypeFilterTable_Object = MibTable
apTypeFilterTable = _ApTypeFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 7)
)
if mibBuilder.loadTexts:
    apTypeFilterTable.setStatus("mandatory")
_ApTypeFilterEntry_Object = MibTableRow
apTypeFilterEntry = _ApTypeFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 7, 1)
)
apTypeFilterEntry.setIndexNames(
    (0, "SYMBOL-DSSS-ENTERPRISE-PRIVATE-MIB", "typeIndex"),
)
if mibBuilder.loadTexts:
    apTypeFilterEntry.setStatus("mandatory")


class _TypeIndex_Type(Integer32):
    """Custom type typeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_TypeIndex_Type.__name__ = "Integer32"
_TypeIndex_Object = MibTableColumn
typeIndex = _TypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 7, 1, 1),
    _TypeIndex_Type()
)
typeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    typeIndex.setStatus("mandatory")


class _EtherType_Type(OctetString):
    """Custom type etherType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_EtherType_Type.__name__ = "OctetString"
_EtherType_Object = MibTableColumn
etherType = _EtherType_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 7, 1, 2),
    _EtherType_Type()
)
etherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etherType.setStatus("mandatory")
_Ap128bWEPKeyTable_Object = MibTable
ap128bWEPKeyTable = _Ap128bWEPKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 8)
)
if mibBuilder.loadTexts:
    ap128bWEPKeyTable.setStatus("mandatory")
_ApWEPKeyEntry_Object = MibTableRow
apWEPKeyEntry = _ApWEPKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 8, 1)
)
apWEPKeyEntry.setIndexNames(
    (0, "SYMBOL-DSSS-ENTERPRISE-PRIVATE-MIB", "ap128bWepkeyIndex"),
)
if mibBuilder.loadTexts:
    apWEPKeyEntry.setStatus("mandatory")


class _Ap128bWepkeyIndex_Type(Integer32):
    """Custom type ap128bWepkeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Ap128bWepkeyIndex_Type.__name__ = "Integer32"
_Ap128bWepkeyIndex_Object = MibTableColumn
ap128bWepkeyIndex = _Ap128bWepkeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 8, 1, 1),
    _Ap128bWepkeyIndex_Type()
)
ap128bWepkeyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap128bWepkeyIndex.setStatus("mandatory")
_Ap128bWepKeyValue_Type = WEPKeytype128b
_Ap128bWepKeyValue_Object = MibTableColumn
ap128bWepKeyValue = _Ap128bWepKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 1, 8, 1, 2),
    _Ap128bWepKeyValue_Type()
)
ap128bWepKeyValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ap128bWepKeyValue.setStatus("mandatory")
_ApPerformMgmt_ObjectIdentity = ObjectIdentity
apPerformMgmt = _ApPerformMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2)
)
_ApTrafficMatrixTable_Object = MibTable
apTrafficMatrixTable = _ApTrafficMatrixTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    apTrafficMatrixTable.setStatus("mandatory")
_ApTrafficMatrixEntry_Object = MibTableRow
apTrafficMatrixEntry = _ApTrafficMatrixEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 1, 1)
)
apTrafficMatrixEntry.setIndexNames(
    (0, "SYMBOL-DSSS-ENTERPRISE-PRIVATE-MIB", "apTMTableIndex"),
)
if mibBuilder.loadTexts:
    apTrafficMatrixEntry.setStatus("mandatory")


class _ApTMTableIndex_Type(Integer32):
    """Custom type apTMTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_ApTMTableIndex_Type.__name__ = "Integer32"
_ApTMTableIndex_Object = MibTableColumn
apTMTableIndex = _ApTMTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 1, 1, 1),
    _ApTMTableIndex_Type()
)
apTMTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTMTableIndex.setStatus("mandatory")


class _ApProtoItfName_Type(DisplayString):
    """Custom type apProtoItfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_ApProtoItfName_Type.__name__ = "DisplayString"
_ApProtoItfName_Object = MibTableColumn
apProtoItfName = _ApProtoItfName_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 1, 1, 2),
    _ApProtoItfName_Type()
)
apProtoItfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProtoItfName.setStatus("mandatory")
_ApNPktsToEnets_Type = Counter32
_ApNPktsToEnets_Object = MibTableColumn
apNPktsToEnets = _ApNPktsToEnets_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 1, 1, 3),
    _ApNPktsToEnets_Type()
)
apNPktsToEnets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNPktsToEnets.setStatus("mandatory")
_ApNPktsToPpps_Type = Counter32
_ApNPktsToPpps_Object = MibTableColumn
apNPktsToPpps = _ApNPktsToPpps_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 1, 1, 4),
    _ApNPktsToPpps_Type()
)
apNPktsToPpps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNPktsToPpps.setStatus("mandatory")
_ApNPktsToRfs_Type = Counter32
_ApNPktsToRfs_Object = MibTableColumn
apNPktsToRfs = _ApNPktsToRfs_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 1, 1, 5),
    _ApNPktsToRfs_Type()
)
apNPktsToRfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNPktsToRfs.setStatus("mandatory")
_ApNPktsToAPStks_Type = Counter32
_ApNPktsToAPStks_Object = MibTableColumn
apNPktsToAPStks = _ApNPktsToAPStks_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 1, 1, 6),
    _ApNPktsToAPStks_Type()
)
apNPktsToAPStks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNPktsToAPStks.setStatus("mandatory")
_ApItfStatTable_Object = MibTable
apItfStatTable = _ApItfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 2)
)
if mibBuilder.loadTexts:
    apItfStatTable.setStatus("mandatory")
_ApItfStatEntry_Object = MibTableRow
apItfStatEntry = _ApItfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 2, 1)
)
apItfStatEntry.setIndexNames(
    (0, "SYMBOL-DSSS-ENTERPRISE-PRIVATE-MIB", "apItfStatIndex"),
)
if mibBuilder.loadTexts:
    apItfStatEntry.setStatus("mandatory")


class _ApItfStatIndex_Type(Integer32):
    """Custom type apItfStatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ApItfStatIndex_Type.__name__ = "Integer32"
_ApItfStatIndex_Object = MibTableColumn
apItfStatIndex = _ApItfStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 2, 1, 1),
    _ApItfStatIndex_Type()
)
apItfStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apItfStatIndex.setStatus("mandatory")


class _ApInterfaceName_Type(DisplayString):
    """Custom type apInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_ApInterfaceName_Type.__name__ = "DisplayString"
_ApInterfaceName_Object = MibTableColumn
apInterfaceName = _ApInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 2, 1, 2),
    _ApInterfaceName_Type()
)
apInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInterfaceName.setStatus("mandatory")
_ApPacketsIns_Type = Counter32
_ApPacketsIns_Object = MibTableColumn
apPacketsIns = _ApPacketsIns_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 2, 1, 3),
    _ApPacketsIns_Type()
)
apPacketsIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPacketsIns.setStatus("mandatory")
_ApPacketsOuts_Type = Counter32
_ApPacketsOuts_Object = MibTableColumn
apPacketsOuts = _ApPacketsOuts_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 2, 1, 4),
    _ApPacketsOuts_Type()
)
apPacketsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPacketsOuts.setStatus("mandatory")
_ApOctetsIns_Type = Counter32
_ApOctetsIns_Object = MibTableColumn
apOctetsIns = _ApOctetsIns_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 2, 1, 5),
    _ApOctetsIns_Type()
)
apOctetsIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOctetsIns.setStatus("mandatory")
_ApOctetsOuts_Type = Counter32
_ApOctetsOuts_Object = MibTableColumn
apOctetsOuts = _ApOctetsOuts_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 2, 1, 6),
    _ApOctetsOuts_Type()
)
apOctetsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOctetsOuts.setStatus("mandatory")
_ApPktsInPerSec_Type = Gauge32
_ApPktsInPerSec_Object = MibTableColumn
apPktsInPerSec = _ApPktsInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 2, 1, 7),
    _ApPktsInPerSec_Type()
)
apPktsInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPktsInPerSec.setStatus("mandatory")
_ApPktsOutPerSec_Type = Gauge32
_ApPktsOutPerSec_Object = MibTableColumn
apPktsOutPerSec = _ApPktsOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 2, 1, 8),
    _ApPktsOutPerSec_Type()
)
apPktsOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPktsOutPerSec.setStatus("mandatory")
_ApOctInPerSec_Type = Gauge32
_ApOctInPerSec_Object = MibTableColumn
apOctInPerSec = _ApOctInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 2, 1, 9),
    _ApOctInPerSec_Type()
)
apOctInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOctInPerSec.setStatus("mandatory")
_ApOctOutPerSec_Type = Gauge32
_ApOctOutPerSec_Object = MibTableColumn
apOctOutPerSec = _ApOctOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 2, 1, 10),
    _ApOctOutPerSec_Type()
)
apOctOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOctOutPerSec.setStatus("mandatory")
_ApEthernetStatistics_ObjectIdentity = ObjectIdentity
apEthernetStatistics = _ApEthernetStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 3)
)
_ApEPktsSeens_Type = Counter32
_ApEPktsSeens_Object = MibScalar
apEPktsSeens = _ApEPktsSeens_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 3, 1),
    _ApEPktsSeens_Type()
)
apEPktsSeens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEPktsSeens.setStatus("mandatory")
_ApEPktsForwardeds_Type = Counter32
_ApEPktsForwardeds_Object = MibScalar
apEPktsForwardeds = _ApEPktsForwardeds_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 3, 2),
    _ApEPktsForwardeds_Type()
)
apEPktsForwardeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEPktsForwardeds.setStatus("mandatory")
_ApEPktsDiscNoMatchs_Type = Counter32
_ApEPktsDiscNoMatchs_Object = MibScalar
apEPktsDiscNoMatchs = _ApEPktsDiscNoMatchs_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 3, 3),
    _ApEPktsDiscNoMatchs_Type()
)
apEPktsDiscNoMatchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEPktsDiscNoMatchs.setStatus("mandatory")
_ApEPktsDiscForceds_Type = Counter32
_ApEPktsDiscForceds_Object = MibScalar
apEPktsDiscForceds = _ApEPktsDiscForceds_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 3, 4),
    _ApEPktsDiscForceds_Type()
)
apEPktsDiscForceds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEPktsDiscForceds.setStatus("mandatory")
_ApEPktsDiscBuffers_Type = Counter32
_ApEPktsDiscBuffers_Object = MibScalar
apEPktsDiscBuffers = _ApEPktsDiscBuffers_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 3, 5),
    _ApEPktsDiscBuffers_Type()
)
apEPktsDiscBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEPktsDiscBuffers.setStatus("mandatory")
_ApEPktsDiscCRCs_Type = Counter32
_ApEPktsDiscCRCs_Object = MibScalar
apEPktsDiscCRCs = _ApEPktsDiscCRCs_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 3, 6),
    _ApEPktsDiscCRCs_Type()
)
apEPktsDiscCRCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEPktsDiscCRCs.setStatus("mandatory")
_ApEPktsSents_Type = Counter32
_ApEPktsSents_Object = MibScalar
apEPktsSents = _ApEPktsSents_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 3, 7),
    _ApEPktsSents_Type()
)
apEPktsSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEPktsSents.setStatus("mandatory")
_ApEAnyCollisions_Type = Counter32
_ApEAnyCollisions_Object = MibScalar
apEAnyCollisions = _ApEAnyCollisions_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 3, 8),
    _ApEAnyCollisions_Type()
)
apEAnyCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEAnyCollisions.setStatus("mandatory")
_ApE1orMoreColls_Type = Counter32
_ApE1orMoreColls_Object = MibScalar
apE1orMoreColls = _ApE1orMoreColls_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 3, 9),
    _ApE1orMoreColls_Type()
)
apE1orMoreColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apE1orMoreColls.setStatus("mandatory")
_ApEMaxCollisions_Type = Counter32
_ApEMaxCollisions_Object = MibScalar
apEMaxCollisions = _ApEMaxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 3, 10),
    _ApEMaxCollisions_Type()
)
apEMaxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEMaxCollisions.setStatus("mandatory")
_ApELateCollisions_Type = Counter32
_ApELateCollisions_Object = MibScalar
apELateCollisions = _ApELateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 3, 11),
    _ApELateCollisions_Type()
)
apELateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apELateCollisions.setStatus("mandatory")
_ApEPktsDefers_Type = Counter32
_ApEPktsDefers_Object = MibScalar
apEPktsDefers = _ApEPktsDefers_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 3, 12),
    _ApEPktsDefers_Type()
)
apEPktsDefers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEPktsDefers.setStatus("mandatory")
_ApEBcMcPkts_Type = Counter32
_ApEBcMcPkts_Object = MibScalar
apEBcMcPkts = _ApEBcMcPkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 3, 13),
    _ApEBcMcPkts_Type()
)
apEBcMcPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEBcMcPkts.setStatus("mandatory")
_ApEIndividualAddrs_Type = Counter32
_ApEIndividualAddrs_Object = MibScalar
apEIndividualAddrs = _ApEIndividualAddrs_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 3, 14),
    _ApEIndividualAddrs_Type()
)
apEIndividualAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEIndividualAddrs.setStatus("mandatory")
_ApRFStatistics_ObjectIdentity = ObjectIdentity
apRFStatistics = _ApRFStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 4)
)
_RfBcMcPktsSents_Type = Counter32
_RfBcMcPktsSents_Object = MibScalar
rfBcMcPktsSents = _RfBcMcPktsSents_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 4, 1),
    _RfBcMcPktsSents_Type()
)
rfBcMcPktsSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfBcMcPktsSents.setStatus("mandatory")
_RfBcMcPktsRcvds_Type = Counter32
_RfBcMcPktsRcvds_Object = MibScalar
rfBcMcPktsRcvds = _RfBcMcPktsRcvds_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 4, 2),
    _RfBcMcPktsRcvds_Type()
)
rfBcMcPktsRcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfBcMcPktsRcvds.setStatus("mandatory")
_RfBcMcOctSents_Type = Counter32
_RfBcMcOctSents_Object = MibScalar
rfBcMcOctSents = _RfBcMcOctSents_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 4, 3),
    _RfBcMcOctSents_Type()
)
rfBcMcOctSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfBcMcOctSents.setStatus("mandatory")
_RfBcMcOctRcvds_Type = Counter32
_RfBcMcOctRcvds_Object = MibScalar
rfBcMcOctRcvds = _RfBcMcOctRcvds_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 4, 4),
    _RfBcMcOctRcvds_Type()
)
rfBcMcOctRcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfBcMcOctRcvds.setStatus("mandatory")
_RfSysPktsSents_Type = Counter32
_RfSysPktsSents_Object = MibScalar
rfSysPktsSents = _RfSysPktsSents_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 4, 5),
    _RfSysPktsSents_Type()
)
rfSysPktsSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfSysPktsSents.setStatus("mandatory")
_RfSysPktsRcvds_Type = Counter32
_RfSysPktsRcvds_Object = MibScalar
rfSysPktsRcvds = _RfSysPktsRcvds_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 4, 6),
    _RfSysPktsRcvds_Type()
)
rfSysPktsRcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfSysPktsRcvds.setStatus("mandatory")
_RfSBcMcPktsSents_Type = Counter32
_RfSBcMcPktsSents_Object = MibScalar
rfSBcMcPktsSents = _RfSBcMcPktsSents_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 4, 7),
    _RfSBcMcPktsSents_Type()
)
rfSBcMcPktsSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfSBcMcPktsSents.setStatus("mandatory")
_RfSBcMcPktsRcvds_Type = Counter32
_RfSBcMcPktsRcvds_Object = MibScalar
rfSBcMcPktsRcvds = _RfSBcMcPktsRcvds_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 4, 8),
    _RfSBcMcPktsRcvds_Type()
)
rfSBcMcPktsRcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfSBcMcPktsRcvds.setStatus("mandatory")
_RfSuccFragPkts_Type = Counter32
_RfSuccFragPkts_Object = MibScalar
rfSuccFragPkts = _RfSuccFragPkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 4, 9),
    _RfSuccFragPkts_Type()
)
rfSuccFragPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfSuccFragPkts.setStatus("mandatory")
_RfUnsuccFragPkts_Type = Counter32
_RfUnsuccFragPkts_Object = MibScalar
rfUnsuccFragPkts = _RfUnsuccFragPkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 4, 10),
    _RfUnsuccFragPkts_Type()
)
rfUnsuccFragPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfUnsuccFragPkts.setStatus("mandatory")
_RfTotalFragSents_Type = Counter32
_RfTotalFragSents_Object = MibScalar
rfTotalFragSents = _RfTotalFragSents_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 4, 11),
    _RfTotalFragSents_Type()
)
rfTotalFragSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfTotalFragSents.setStatus("mandatory")
_RfTotalFragRcvds_Type = Counter32
_RfTotalFragRcvds_Object = MibScalar
rfTotalFragRcvds = _RfTotalFragRcvds_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 4, 12),
    _RfTotalFragRcvds_Type()
)
rfTotalFragRcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfTotalFragRcvds.setStatus("mandatory")
_RfSuccReassPkts_Type = Counter32
_RfSuccReassPkts_Object = MibScalar
rfSuccReassPkts = _RfSuccReassPkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 4, 13),
    _RfSuccReassPkts_Type()
)
rfSuccReassPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfSuccReassPkts.setStatus("mandatory")
_RfUnsuccReassPkts_Type = Counter32
_RfUnsuccReassPkts_Object = MibScalar
rfUnsuccReassPkts = _RfUnsuccReassPkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 4, 14),
    _RfUnsuccReassPkts_Type()
)
rfUnsuccReassPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfUnsuccReassPkts.setStatus("mandatory")
_RfAssocMUs_Type = Counter32
_RfAssocMUs_Object = MibScalar
rfAssocMUs = _RfAssocMUs_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 4, 15),
    _RfAssocMUs_Type()
)
rfAssocMUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfAssocMUs.setStatus("mandatory")
_RfRcvdCRCErrors_Type = Counter32
_RfRcvdCRCErrors_Object = MibScalar
rfRcvdCRCErrors = _RfRcvdCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 4, 16),
    _RfRcvdCRCErrors_Type()
)
rfRcvdCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfRcvdCRCErrors.setStatus("mandatory")
_RfRcvdDupPkts_Type = Counter32
_RfRcvdDupPkts_Object = MibScalar
rfRcvdDupPkts = _RfRcvdDupPkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 4, 17),
    _RfRcvdDupPkts_Type()
)
rfRcvdDupPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfRcvdDupPkts.setStatus("mandatory")
_RfTotalCollisions_Type = Counter32
_RfTotalCollisions_Object = MibScalar
rfTotalCollisions = _RfTotalCollisions_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 4, 18),
    _RfTotalCollisions_Type()
)
rfTotalCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfTotalCollisions.setStatus("mandatory")
_RfPktsWithoutColls_Type = Counter32
_RfPktsWithoutColls_Object = MibScalar
rfPktsWithoutColls = _RfPktsWithoutColls_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 4, 19),
    _RfPktsWithoutColls_Type()
)
rfPktsWithoutColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfPktsWithoutColls.setStatus("mandatory")
_RfPktsWithMaxColls_Type = Counter32
_RfPktsWithMaxColls_Object = MibScalar
rfPktsWithMaxColls = _RfPktsWithMaxColls_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 4, 20),
    _RfPktsWithMaxColls_Type()
)
rfPktsWithMaxColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfPktsWithMaxColls.setStatus("mandatory")
_RfPktsWithColls_Type = Counter32
_RfPktsWithColls_Object = MibScalar
rfPktsWithColls = _RfPktsWithColls_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 4, 21),
    _RfPktsWithColls_Type()
)
rfPktsWithColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfPktsWithColls.setStatus("mandatory")
_RfDataPktsSents_Type = Counter32
_RfDataPktsSents_Object = MibScalar
rfDataPktsSents = _RfDataPktsSents_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 4, 22),
    _RfDataPktsSents_Type()
)
rfDataPktsSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDataPktsSents.setStatus("mandatory")
_RfDataPktsRcvds_Type = Counter32
_RfDataPktsRcvds_Object = MibScalar
rfDataPktsRcvds = _RfDataPktsRcvds_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 4, 23),
    _RfDataPktsRcvds_Type()
)
rfDataPktsRcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDataPktsRcvds.setStatus("mandatory")
_RfDataOctetsSents_Type = Counter32
_RfDataOctetsSents_Object = MibScalar
rfDataOctetsSents = _RfDataOctetsSents_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 4, 24),
    _RfDataOctetsSents_Type()
)
rfDataOctetsSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDataOctetsSents.setStatus("mandatory")
_RfDataOctetsRcvds_Type = Counter32
_RfDataOctetsRcvds_Object = MibScalar
rfDataOctetsRcvds = _RfDataOctetsRcvds_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 4, 25),
    _RfDataOctetsRcvds_Type()
)
rfDataOctetsRcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDataOctetsRcvds.setStatus("mandatory")
_RfEncrypPktsSents_Type = Counter32
_RfEncrypPktsSents_Object = MibScalar
rfEncrypPktsSents = _RfEncrypPktsSents_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 4, 26),
    _RfEncrypPktsSents_Type()
)
rfEncrypPktsSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfEncrypPktsSents.setStatus("mandatory")
_RfEncrypPktsRcvds_Type = Counter32
_RfEncrypPktsRcvds_Object = MibScalar
rfEncrypPktsRcvds = _RfEncrypPktsRcvds_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 4, 27),
    _RfEncrypPktsRcvds_Type()
)
rfEncrypPktsRcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfEncrypPktsRcvds.setStatus("mandatory")
_ApSerialPortStatistics_ObjectIdentity = ObjectIdentity
apSerialPortStatistics = _ApSerialPortStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 6)
)
_ApNbrOfDialouts_Type = Counter32
_ApNbrOfDialouts_Object = MibScalar
apNbrOfDialouts = _ApNbrOfDialouts_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 6, 1),
    _ApNbrOfDialouts_Type()
)
apNbrOfDialouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNbrOfDialouts.setStatus("mandatory")
_ApDialoutFailures_Type = Counter32
_ApDialoutFailures_Object = MibScalar
apDialoutFailures = _ApDialoutFailures_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 6, 2),
    _ApDialoutFailures_Type()
)
apDialoutFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDialoutFailures.setStatus("mandatory")
_ApNbrOfAnswers_Type = Counter32
_ApNbrOfAnswers_Object = MibScalar
apNbrOfAnswers = _ApNbrOfAnswers_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 6, 3),
    _ApNbrOfAnswers_Type()
)
apNbrOfAnswers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNbrOfAnswers.setStatus("mandatory")
_ApCurrCallTime_Type = TimeTicks
_ApCurrCallTime_Object = MibScalar
apCurrCallTime = _ApCurrCallTime_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 6, 4),
    _ApCurrCallTime_Type()
)
apCurrCallTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCurrCallTime.setStatus("mandatory")
_ApLastCallTime_Type = TimeTicks
_ApLastCallTime_Object = MibScalar
apLastCallTime = _ApLastCallTime_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 6, 5),
    _ApLastCallTime_Type()
)
apLastCallTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLastCallTime.setStatus("mandatory")
_ApWNMPStatistics_ObjectIdentity = ObjectIdentity
apWNMPStatistics = _ApWNMPStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 7)
)
_ApWNMPCfgPkts_Type = Counter32
_ApWNMPCfgPkts_Object = MibScalar
apWNMPCfgPkts = _ApWNMPCfgPkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 7, 1),
    _ApWNMPCfgPkts_Type()
)
apWNMPCfgPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWNMPCfgPkts.setStatus("mandatory")
_WEchoRequests_Type = Counter32
_WEchoRequests_Object = MibScalar
wEchoRequests = _WEchoRequests_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 7, 2),
    _WEchoRequests_Type()
)
wEchoRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEchoRequests.setStatus("mandatory")
_WPingRequests_Type = Counter32
_WPingRequests_Object = MibScalar
wPingRequests = _WPingRequests_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 7, 3),
    _WPingRequests_Type()
)
wPingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wPingRequests.setStatus("mandatory")
_WPktsFromNVs_Type = Counter32
_WPktsFromNVs_Object = MibScalar
wPktsFromNVs = _WPktsFromNVs_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 7, 4),
    _WPktsFromNVs_Type()
)
wPktsFromNVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wPktsFromNVs.setStatus("mandatory")
_WPPktsToNVs_Type = Counter32
_WPPktsToNVs_Object = MibScalar
wPPktsToNVs = _WPPktsToNVs_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 7, 5),
    _WPPktsToNVs_Type()
)
wPPktsToNVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wPPktsToNVs.setStatus("mandatory")
_WPassThruEchoes_Type = Counter32
_WPassThruEchoes_Object = MibScalar
wPassThruEchoes = _WPassThruEchoes_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 7, 6),
    _WPassThruEchoes_Type()
)
wPassThruEchoes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wPassThruEchoes.setStatus("mandatory")
_ApMUInfo_ObjectIdentity = ObjectIdentity
apMUInfo = _ApMUInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 8)
)
_ApCurrentMUs_Type = Counter32
_ApCurrentMUs_Object = MibScalar
apCurrentMUs = _ApCurrentMUs_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 8, 1),
    _ApCurrentMUs_Type()
)
apCurrentMUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCurrentMUs.setStatus("mandatory")
_ApMaxMUs_Type = Counter32
_ApMaxMUs_Object = MibScalar
apMaxMUs = _ApMaxMUs_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 8, 2),
    _ApMaxMUs_Type()
)
apMaxMUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMaxMUs.setStatus("mandatory")
_ApTotalAssocs_Type = Counter32
_ApTotalAssocs_Object = MibScalar
apTotalAssocs = _ApTotalAssocs_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 8, 3),
    _ApTotalAssocs_Type()
)
apTotalAssocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTotalAssocs.setStatus("mandatory")
_ApMUTable_Object = MibTable
apMUTable = _ApMUTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 8, 4)
)
if mibBuilder.loadTexts:
    apMUTable.setStatus("mandatory")
_ApMUEntry_Object = MibTableRow
apMUEntry = _ApMUEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 8, 4, 1)
)
apMUEntry.setIndexNames(
    (0, "SYMBOL-DSSS-ENTERPRISE-PRIVATE-MIB", "muIndex"),
)
if mibBuilder.loadTexts:
    apMUEntry.setStatus("mandatory")


class _MuIndex_Type(Integer32):
    """Custom type muIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_MuIndex_Type.__name__ = "Integer32"
_MuIndex_Object = MibTableColumn
muIndex = _MuIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 8, 4, 1, 1),
    _MuIndex_Type()
)
muIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muIndex.setStatus("mandatory")
_MuMacAddr_Type = PhysAddress
_MuMacAddr_Object = MibTableColumn
muMacAddr = _MuMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 8, 4, 1, 2),
    _MuMacAddr_Type()
)
muMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muMacAddr.setStatus("mandatory")


class _MuInterface_Type(Integer32):
    """Custom type muInterface based on Integer32"""
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
        *(("apstack", 4),
          ("ethernet", 1),
          ("ppp", 2),
          ("rf", 3))
    )


_MuInterface_Type.__name__ = "Integer32"
_MuInterface_Object = MibTableColumn
muInterface = _MuInterface_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 8, 4, 1, 3),
    _MuInterface_Type()
)
muInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muInterface.setStatus("mandatory")


class _MuState_Type(Integer32):
    """Custom type muState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("associated", 3),
          ("not-associated", 4))
    )


_MuState_Type.__name__ = "Integer32"
_MuState_Object = MibTableColumn
muState = _MuState_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 8, 4, 1, 4),
    _MuState_Type()
)
muState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muState.setStatus("mandatory")


class _MuPowerMode_Type(Integer32):
    """Custom type muPowerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cam", 1),
          ("psp", 2))
    )


_MuPowerMode_Type.__name__ = "Integer32"
_MuPowerMode_Object = MibTableColumn
muPowerMode = _MuPowerMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 8, 4, 1, 5),
    _MuPowerMode_Type()
)
muPowerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muPowerMode.setStatus("mandatory")
_MuStationID_Type = Integer32
_MuStationID_Object = MibTableColumn
muStationID = _MuStationID_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 8, 4, 1, 6),
    _MuStationID_Type()
)
muStationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muStationID.setStatus("mandatory")
_MuLastAPAddr_Type = PhysAddress
_MuLastAPAddr_Object = MibTableColumn
muLastAPAddr = _MuLastAPAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 8, 4, 1, 7),
    _MuLastAPAddr_Type()
)
muLastAPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muLastAPAddr.setStatus("mandatory")
_MuTotalAssoc_Type = Integer32
_MuTotalAssoc_Object = MibTableColumn
muTotalAssoc = _MuTotalAssoc_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 8, 4, 1, 8),
    _MuTotalAssoc_Type()
)
muTotalAssoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muTotalAssoc.setStatus("mandatory")
_MuAssocStart_Type = TimeTicks
_MuAssocStart_Object = MibTableColumn
muAssocStart = _MuAssocStart_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 8, 4, 1, 9),
    _MuAssocStart_Type()
)
muAssocStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muAssocStart.setStatus("mandatory")
_MuLstAssStrt_Type = TimeTicks
_MuLstAssStrt_Object = MibTableColumn
muLstAssStrt = _MuLstAssStrt_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 8, 4, 1, 10),
    _MuLstAssStrt_Type()
)
muLstAssStrt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muLstAssStrt.setStatus("mandatory")
_MuLastAssEnd_Type = TimeTicks
_MuLastAssEnd_Object = MibTableColumn
muLastAssEnd = _MuLastAssEnd_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 8, 4, 1, 11),
    _MuLastAssEnd_Type()
)
muLastAssEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muLastAssEnd.setStatus("mandatory")
_MuNPktsSents_Type = Counter32
_MuNPktsSents_Object = MibTableColumn
muNPktsSents = _MuNPktsSents_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 8, 4, 1, 12),
    _MuNPktsSents_Type()
)
muNPktsSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muNPktsSents.setStatus("mandatory")
_MuNPktsRcvds_Type = Counter32
_MuNPktsRcvds_Object = MibTableColumn
muNPktsRcvds = _MuNPktsRcvds_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 8, 4, 1, 13),
    _MuNPktsRcvds_Type()
)
muNPktsRcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muNPktsRcvds.setStatus("mandatory")
_MuNBytesSents_Type = Counter32
_MuNBytesSents_Object = MibTableColumn
muNBytesSents = _MuNBytesSents_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 8, 4, 1, 14),
    _MuNBytesSents_Type()
)
muNBytesSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muNBytesSents.setStatus("mandatory")
_MuNBytesRcvds_Type = Counter32
_MuNBytesRcvds_Object = MibTableColumn
muNBytesRcvds = _MuNBytesRcvds_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 8, 4, 1, 15),
    _MuNBytesRcvds_Type()
)
muNBytesRcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muNBytesRcvds.setStatus("mandatory")
_MuNDiscdPkts_Type = Counter32
_MuNDiscdPkts_Object = MibTableColumn
muNDiscdPkts = _MuNDiscdPkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 8, 4, 1, 16),
    _MuNDiscdPkts_Type()
)
muNDiscdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muNDiscdPkts.setStatus("mandatory")
_MuTmLastData_Type = TimeTicks
_MuTmLastData_Object = MibTableColumn
muTmLastData = _MuTmLastData_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 8, 4, 1, 17),
    _MuTmLastData_Type()
)
muTmLastData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muTmLastData.setStatus("mandatory")


class _MuPriority_Type(Integer32):
    """Custom type muPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 2),
          ("voice", 1))
    )


_MuPriority_Type.__name__ = "Integer32"
_MuPriority_Object = MibTableColumn
muPriority = _MuPriority_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 8, 4, 1, 18),
    _MuPriority_Type()
)
muPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muPriority.setStatus("mandatory")


class _MuSupportedRates_Type(Integer32):
    """Custom type muSupportedRates based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("eleven-Mb", 8),
          ("five-half-Mb", 4),
          ("five-half-and-eleven-Mb", 12),
          ("one-Mb", 1),
          ("one-and-eleven-Mb", 9),
          ("one-and-five-half-Mb", 5),
          ("one-and-five-half-and-eleven-Mb", 13),
          ("one-and-two-Mb", 3),
          ("one-and-two-and-eleven-Mb", 11),
          ("one-and-two-and-five-half-Mb", 7),
          ("one-and-two-and-five-half-and-eleven-Mb", 15),
          ("two-Mb", 2),
          ("two-and-eleven-Mb", 10),
          ("two-and-five-half-Mb", 6),
          ("two-and-five-half-and-eleven-Mb", 14))
    )


_MuSupportedRates_Type.__name__ = "Integer32"
_MuSupportedRates_Object = MibTableColumn
muSupportedRates = _MuSupportedRates_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 8, 4, 1, 19),
    _MuSupportedRates_Type()
)
muSupportedRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muSupportedRates.setStatus("mandatory")


class _MuCurrentXmtRate_Type(Integer32):
    """Custom type muCurrentXmtRate based on Integer32"""
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
        *(("eleven-Megabit", 4),
          ("five-half-Megabit", 3),
          ("one-Megabit", 1),
          ("two-Megabit", 2))
    )


_MuCurrentXmtRate_Type.__name__ = "Integer32"
_MuCurrentXmtRate_Object = MibTableColumn
muCurrentXmtRate = _MuCurrentXmtRate_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 8, 4, 1, 20),
    _MuCurrentXmtRate_Type()
)
muCurrentXmtRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muCurrentXmtRate.setStatus("mandatory")
_MuLastActivity_Type = TimeTicks
_MuLastActivity_Object = MibTableColumn
muLastActivity = _MuLastActivity_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 8, 4, 1, 21),
    _MuLastActivity_Type()
)
muLastActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muLastActivity.setStatus("mandatory")
_ApMUHmAgTable_Object = MibTable
apMUHmAgTable = _ApMUHmAgTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 8, 5)
)
if mibBuilder.loadTexts:
    apMUHmAgTable.setStatus("mandatory")
_ApMUHATEntry_Object = MibTableRow
apMUHATEntry = _ApMUHATEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 8, 5, 1)
)
apMUHATEntry.setIndexNames(
    (0, "SYMBOL-DSSS-ENTERPRISE-PRIVATE-MIB", "muHATMUIpAddr"),
)
if mibBuilder.loadTexts:
    apMUHATEntry.setStatus("mandatory")
_MuHATMUIpAddr_Type = IpAddress
_MuHATMUIpAddr_Object = MibTableColumn
muHATMUIpAddr = _MuHATMUIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 8, 5, 1, 1),
    _MuHATMUIpAddr_Type()
)
muHATMUIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muHATMUIpAddr.setStatus("mandatory")
_MuHATFrAgIpAddr_Type = IpAddress
_MuHATFrAgIpAddr_Object = MibTableColumn
muHATFrAgIpAddr = _MuHATFrAgIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 8, 5, 1, 2),
    _MuHATFrAgIpAddr_Type()
)
muHATFrAgIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muHATFrAgIpAddr.setStatus("mandatory")
_ApMUFrAgTable_Object = MibTable
apMUFrAgTable = _ApMUFrAgTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 8, 6)
)
if mibBuilder.loadTexts:
    apMUFrAgTable.setStatus("mandatory")
_ApMUFATEntry_Object = MibTableRow
apMUFATEntry = _ApMUFATEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 8, 6, 1)
)
apMUFATEntry.setIndexNames(
    (0, "SYMBOL-DSSS-ENTERPRISE-PRIVATE-MIB", "muFATMUIpAddr"),
)
if mibBuilder.loadTexts:
    apMUFATEntry.setStatus("mandatory")
_MuFATMUIpAddr_Type = IpAddress
_MuFATMUIpAddr_Object = MibTableColumn
muFATMUIpAddr = _MuFATMUIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 8, 6, 1, 1),
    _MuFATMUIpAddr_Type()
)
muFATMUIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muFATMUIpAddr.setStatus("mandatory")
_MuFATHmAgIpAddr_Type = IpAddress
_MuFATHmAgIpAddr_Object = MibTableColumn
muFATHmAgIpAddr = _MuFATHmAgIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 8, 6, 1, 2),
    _MuFATHmAgIpAddr_Type()
)
muFATHmAgIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muFATHmAgIpAddr.setStatus("mandatory")
_ApKnownAPsTable_Object = MibTable
apKnownAPsTable = _ApKnownAPsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 9)
)
if mibBuilder.loadTexts:
    apKnownAPsTable.setStatus("mandatory")
_ApKnownAPsEntry_Object = MibTableRow
apKnownAPsEntry = _ApKnownAPsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 9, 1)
)
apKnownAPsEntry.setIndexNames(
    (0, "SYMBOL-DSSS-ENTERPRISE-PRIVATE-MIB", "apAPMacAddr"),
)
if mibBuilder.loadTexts:
    apKnownAPsEntry.setStatus("mandatory")
_ApAPMacAddr_Type = PhysAddress
_ApAPMacAddr_Object = MibTableColumn
apAPMacAddr = _ApAPMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 9, 1, 1),
    _ApAPMacAddr_Type()
)
apAPMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAPMacAddr.setStatus("mandatory")
_ApAPIpAddr_Type = IpAddress
_ApAPIpAddr_Object = MibTableColumn
apAPIpAddr = _ApAPIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 9, 1, 2),
    _ApAPIpAddr_Type()
)
apAPIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAPIpAddr.setStatus("mandatory")
_ApHoppingSet_Type = Integer32
_ApHoppingSet_Object = MibTableColumn
apHoppingSet = _ApHoppingSet_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 9, 1, 3),
    _ApHoppingSet_Type()
)
apHoppingSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apHoppingSet.setStatus("mandatory")
_ApHoppingSeq_Type = Integer32
_ApHoppingSeq_Object = MibTableColumn
apHoppingSeq = _ApHoppingSeq_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 9, 1, 4),
    _ApHoppingSeq_Type()
)
apHoppingSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apHoppingSeq.setStatus("mandatory")
_ApNbrOfMUs_Type = Integer32
_ApNbrOfMUs_Object = MibTableColumn
apNbrOfMUs = _ApNbrOfMUs_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 9, 1, 5),
    _ApNbrOfMUs_Type()
)
apNbrOfMUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNbrOfMUs.setStatus("mandatory")
_ApKBIOS_Type = Integer32
_ApKBIOS_Object = MibTableColumn
apKBIOS = _ApKBIOS_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 9, 1, 6),
    _ApKBIOS_Type()
)
apKBIOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apKBIOS.setStatus("mandatory")


class _ApAway_Type(Integer32):
    """Custom type apAway based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_ApAway_Type.__name__ = "Integer32"
_ApAway_Object = MibTableColumn
apAway = _ApAway_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 9, 1, 7),
    _ApAway_Type()
)
apAway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAway.setStatus("mandatory")


class _Ap802dot11Protocol_Type(Integer32):
    """Custom type ap802dot11Protocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Ap802dot11Protocol_Type.__name__ = "Integer32"
_Ap802dot11Protocol_Object = MibTableColumn
ap802dot11Protocol = _Ap802dot11Protocol_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 9, 1, 8),
    _Ap802dot11Protocol_Type()
)
ap802dot11Protocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap802dot11Protocol.setStatus("mandatory")


class _ApFwVer_Type(DisplayString):
    """Custom type apFwVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_ApFwVer_Type.__name__ = "DisplayString"
_ApFwVer_Object = MibTableColumn
apFwVer = _ApFwVer_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 9, 1, 9),
    _ApFwVer_Type()
)
apFwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFwVer.setStatus("mandatory")
_ApDSchannel_Type = Integer32
_ApDSchannel_Object = MibTableColumn
apDSchannel = _ApDSchannel_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 9, 1, 10),
    _ApDSchannel_Type()
)
apDSchannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDSchannel.setStatus("mandatory")
_ApFilterStatistics_ObjectIdentity = ObjectIdentity
apFilterStatistics = _ApFilterStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 10)
)
_ApAdrViolations_Type = Counter32
_ApAdrViolations_Object = MibScalar
apAdrViolations = _ApAdrViolations_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 10, 1),
    _ApAdrViolations_Type()
)
apAdrViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAdrViolations.setStatus("mandatory")
_ApTypeViolations_Type = Counter32
_ApTypeViolations_Object = MibScalar
apTypeViolations = _ApTypeViolations_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 10, 2),
    _ApTypeViolations_Type()
)
apTypeViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTypeViolations.setStatus("mandatory")
_ApWLAPInfo_ObjectIdentity = ObjectIdentity
apWLAPInfo = _ApWLAPInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 11)
)
_ApNbrOfWLAPItfs_Type = Counter32
_ApNbrOfWLAPItfs_Object = MibScalar
apNbrOfWLAPItfs = _ApNbrOfWLAPItfs_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 11, 1),
    _ApNbrOfWLAPItfs_Type()
)
apNbrOfWLAPItfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNbrOfWLAPItfs.setStatus("mandatory")


class _ApWLAPState_Type(Integer32):
    """Custom type apWLAPState based on Integer32"""
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
              10,
              12,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 14),
          ("functional", 15),
          ("initializing", 1),
          ("receive-root-rsp", 10),
          ("root-ap-lost", 12),
          ("send-assoc-req", 3),
          ("send-assoc-rsp", 7),
          ("send-cfg-bpdu", 4),
          ("send-cfg-rsp", 8),
          ("send-probe", 2),
          ("send-probe-rsp", 6),
          ("wait-for-probe", 5),
          ("wlap-lost-on-ethernet", 16))
    )


_ApWLAPState_Type.__name__ = "Integer32"
_ApWLAPState_Object = MibScalar
apWLAPState = _ApWLAPState_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 11, 2),
    _ApWLAPState_Type()
)
apWLAPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWLAPState.setStatus("mandatory")
_ApWLAPHopSequence_Type = Integer32
_ApWLAPHopSequence_Object = MibScalar
apWLAPHopSequence = _ApWLAPHopSequence_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 11, 3),
    _ApWLAPHopSequence_Type()
)
apWLAPHopSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWLAPHopSequence.setStatus("mandatory")
_ApRootInterface_Type = Integer32
_ApRootInterface_Object = MibScalar
apRootInterface = _ApRootInterface_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 11, 4),
    _ApRootInterface_Type()
)
apRootInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRootInterface.setStatus("mandatory")


class _ApRootWLAPID_Type(OctetString):
    """Custom type apRootWLAPID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_ApRootWLAPID_Type.__name__ = "OctetString"
_ApRootWLAPID_Object = MibScalar
apRootWLAPID = _ApRootWLAPID_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 11, 5),
    _ApRootWLAPID_Type()
)
apRootWLAPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRootWLAPID.setStatus("mandatory")
_ApRootPathCost_Type = Integer32
_ApRootPathCost_Object = MibScalar
apRootPathCost = _ApRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 11, 6),
    _ApRootPathCost_Type()
)
apRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRootPathCost.setStatus("mandatory")


class _ApWLAPID_Type(OctetString):
    """Custom type apWLAPID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_ApWLAPID_Type.__name__ = "OctetString"
_ApWLAPID_Object = MibScalar
apWLAPID = _ApWLAPID_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 11, 7),
    _ApWLAPID_Type()
)
apWLAPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWLAPID.setStatus("mandatory")
_ApWLAPItfTable_Object = MibTable
apWLAPItfTable = _ApWLAPItfTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 11, 8)
)
if mibBuilder.loadTexts:
    apWLAPItfTable.setStatus("mandatory")
_ApWLAPItfEntry_Object = MibTableRow
apWLAPItfEntry = _ApWLAPItfEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 11, 8, 1)
)
apWLAPItfEntry.setIndexNames(
    (0, "SYMBOL-DSSS-ENTERPRISE-PRIVATE-MIB", "apWLAPItfID"),
)
if mibBuilder.loadTexts:
    apWLAPItfEntry.setStatus("mandatory")


class _ApWLAPItfID_Type(OctetString):
    """Custom type apWLAPItfID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_ApWLAPItfID_Type.__name__ = "OctetString"
_ApWLAPItfID_Object = MibTableColumn
apWLAPItfID = _ApWLAPItfID_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 11, 8, 1, 1),
    _ApWLAPItfID_Type()
)
apWLAPItfID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWLAPItfID.setStatus("mandatory")
_ApWLAPItfAddr_Type = PhysAddress
_ApWLAPItfAddr_Object = MibTableColumn
apWLAPItfAddr = _ApWLAPItfAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 11, 8, 1, 2),
    _ApWLAPItfAddr_Type()
)
apWLAPItfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWLAPItfAddr.setStatus("mandatory")


class _ApWLAPItfState_Type(Integer32):
    """Custom type apWLAPItfState based on Integer32"""
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
        *(("blocking", 5),
          ("disabled", 1),
          ("forwarding", 4),
          ("learning", 3),
          ("listening", 2))
    )


_ApWLAPItfState_Type.__name__ = "Integer32"
_ApWLAPItfState_Object = MibTableColumn
apWLAPItfState = _ApWLAPItfState_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 11, 8, 1, 3),
    _ApWLAPItfState_Type()
)
apWLAPItfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWLAPItfState.setStatus("mandatory")
_ApWLAPPathCost_Type = Integer32
_ApWLAPPathCost_Object = MibTableColumn
apWLAPPathCost = _ApWLAPPathCost_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 11, 8, 1, 4),
    _ApWLAPPathCost_Type()
)
apWLAPPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWLAPPathCost.setStatus("mandatory")


class _ApDsgnatedRoot_Type(OctetString):
    """Custom type apDsgnatedRoot based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_ApDsgnatedRoot_Type.__name__ = "OctetString"
_ApDsgnatedRoot_Object = MibTableColumn
apDsgnatedRoot = _ApDsgnatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 11, 8, 1, 5),
    _ApDsgnatedRoot_Type()
)
apDsgnatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDsgnatedRoot.setStatus("mandatory")
_ApDsgnatedCost_Type = Integer32
_ApDsgnatedCost_Object = MibTableColumn
apDsgnatedCost = _ApDsgnatedCost_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 11, 8, 1, 6),
    _ApDsgnatedCost_Type()
)
apDsgnatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDsgnatedCost.setStatus("mandatory")


class _ApDsgnatedWLAP_Type(OctetString):
    """Custom type apDsgnatedWLAP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_ApDsgnatedWLAP_Type.__name__ = "OctetString"
_ApDsgnatedWLAP_Object = MibTableColumn
apDsgnatedWLAP = _ApDsgnatedWLAP_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 11, 8, 1, 7),
    _ApDsgnatedWLAP_Type()
)
apDsgnatedWLAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDsgnatedWLAP.setStatus("mandatory")


class _ApDsgnatedItf_Type(OctetString):
    """Custom type apDsgnatedItf based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_ApDsgnatedItf_Type.__name__ = "OctetString"
_ApDsgnatedItf_Object = MibTableColumn
apDsgnatedItf = _ApDsgnatedItf_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 11, 8, 1, 8),
    _ApDsgnatedItf_Type()
)
apDsgnatedItf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDsgnatedItf.setStatus("mandatory")
_ApRetryHistogramTable_Object = MibTable
apRetryHistogramTable = _ApRetryHistogramTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 12)
)
if mibBuilder.loadTexts:
    apRetryHistogramTable.setStatus("mandatory")
_ApRetryHistogramEntry_Object = MibTableRow
apRetryHistogramEntry = _ApRetryHistogramEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 12, 1)
)
apRetryHistogramEntry.setIndexNames(
    (0, "SYMBOL-DSSS-ENTERPRISE-PRIVATE-MIB", "apRetryHistogramIndex"),
)
if mibBuilder.loadTexts:
    apRetryHistogramEntry.setStatus("mandatory")


class _ApRetryHistogramIndex_Type(Integer32):
    """Custom type apRetryHistogramIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ApRetryHistogramIndex_Type.__name__ = "Integer32"
_ApRetryHistogramIndex_Object = MibTableColumn
apRetryHistogramIndex = _ApRetryHistogramIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 12, 1, 1),
    _ApRetryHistogramIndex_Type()
)
apRetryHistogramIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRetryHistogramIndex.setStatus("mandatory")


class _ApNumberOfRetries_Type(Integer32):
    """Custom type apNumberOfRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ApNumberOfRetries_Type.__name__ = "Integer32"
_ApNumberOfRetries_Object = MibTableColumn
apNumberOfRetries = _ApNumberOfRetries_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 12, 1, 2),
    _ApNumberOfRetries_Type()
)
apNumberOfRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNumberOfRetries.setStatus("mandatory")
_ApPacketsHistogramCounts_Type = Counter32
_ApPacketsHistogramCounts_Object = MibTableColumn
apPacketsHistogramCounts = _ApPacketsHistogramCounts_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 12, 1, 3),
    _ApPacketsHistogramCounts_Type()
)
apPacketsHistogramCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPacketsHistogramCounts.setStatus("mandatory")
_ApDSPerFreqStatTable_Object = MibTable
apDSPerFreqStatTable = _ApDSPerFreqStatTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 13)
)
if mibBuilder.loadTexts:
    apDSPerFreqStatTable.setStatus("mandatory")
_ApDSPerFreqStatEntry_Object = MibTableRow
apDSPerFreqStatEntry = _ApDSPerFreqStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 13, 1)
)
apDSPerFreqStatEntry.setIndexNames(
    (0, "SYMBOL-DSSS-ENTERPRISE-PRIVATE-MIB", "rfDSFrequency"),
)
if mibBuilder.loadTexts:
    apDSPerFreqStatEntry.setStatus("mandatory")
_RfDSFrequency_Type = Integer32
_RfDSFrequency_Object = MibTableColumn
rfDSFrequency = _RfDSFrequency_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 13, 1, 1),
    _RfDSFrequency_Type()
)
rfDSFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDSFrequency.setStatus("mandatory")
_RfDSPerFqPktsSents_Type = Counter32
_RfDSPerFqPktsSents_Object = MibTableColumn
rfDSPerFqPktsSents = _RfDSPerFqPktsSents_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 13, 1, 2),
    _RfDSPerFqPktsSents_Type()
)
rfDSPerFqPktsSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDSPerFqPktsSents.setStatus("mandatory")
_RfDSPerFqPktsRcvds_Type = Counter32
_RfDSPerFqPktsRcvds_Object = MibTableColumn
rfDSPerFqPktsRcvds = _RfDSPerFqPktsRcvds_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 13, 1, 3),
    _RfDSPerFqPktsRcvds_Type()
)
rfDSPerFqPktsRcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDSPerFqPktsRcvds.setStatus("mandatory")
_RfDSPerFqRetries_Type = Counter32
_RfDSPerFqRetries_Object = MibTableColumn
rfDSPerFqRetries = _RfDSPerFqRetries_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 13, 1, 4),
    _RfDSPerFqRetries_Type()
)
rfDSPerFqRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDSPerFqRetries.setStatus("mandatory")
_ApMobileIPStatistics_ObjectIdentity = ObjectIdentity
apMobileIPStatistics = _ApMobileIPStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 14)
)
_ApAgentAdSents_Type = Counter32
_ApAgentAdSents_Object = MibScalar
apAgentAdSents = _ApAgentAdSents_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 14, 1),
    _ApAgentAdSents_Type()
)
apAgentAdSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAgentAdSents.setStatus("mandatory")
_ApRegRequestRcvds_Type = Counter32
_ApRegRequestRcvds_Object = MibScalar
apRegRequestRcvds = _ApRegRequestRcvds_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 14, 2),
    _ApRegRequestRcvds_Type()
)
apRegRequestRcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRegRequestRcvds.setStatus("mandatory")
_ApRegReplySents_Type = Counter32
_ApRegReplySents_Object = MibScalar
apRegReplySents = _ApRegReplySents_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 2, 14, 3),
    _ApRegReplySents_Type()
)
apRegReplySents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRegReplySents.setStatus("mandatory")
_ApFaultMgmt_ObjectIdentity = ObjectIdentity
apFaultMgmt = _ApFaultMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 3)
)


class _ApClrAllStatistics_Type(Integer32):
    """Custom type apClrAllStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_ApClrAllStatistics_Type.__name__ = "Integer32"
_ApClrAllStatistics_Object = MibScalar
apClrAllStatistics = _ApClrAllStatistics_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 3, 1),
    _ApClrAllStatistics_Type()
)
apClrAllStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apClrAllStatistics.setStatus("mandatory")


class _ApClrMUTable_Type(Integer32):
    """Custom type apClrMUTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_ApClrMUTable_Type.__name__ = "Integer32"
_ApClrMUTable_Object = MibScalar
apClrMUTable = _ApClrMUTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 3, 2),
    _ApClrMUTable_Type()
)
apClrMUTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apClrMUTable.setStatus("mandatory")


class _ApClrACL_Type(Integer32):
    """Custom type apClrACL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_ApClrACL_Type.__name__ = "Integer32"
_ApClrACL_Object = MibScalar
apClrACL = _ApClrACL_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 3, 3),
    _ApClrACL_Type()
)
apClrACL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apClrACL.setStatus("mandatory")


class _ApClrACLRangeTable_Type(Integer32):
    """Custom type apClrACLRangeTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_ApClrACLRangeTable_Type.__name__ = "Integer32"
_ApClrACLRangeTable_Object = MibScalar
apClrACLRangeTable = _ApClrACLRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 3, 4),
    _ApClrACLRangeTable_Type()
)
apClrACLRangeTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apClrACLRangeTable.setStatus("mandatory")


class _ApClrAddrFilterTbl_Type(Integer32):
    """Custom type apClrAddrFilterTbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_ApClrAddrFilterTbl_Type.__name__ = "Integer32"
_ApClrAddrFilterTbl_Object = MibScalar
apClrAddrFilterTbl = _ApClrAddrFilterTbl_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 3, 5),
    _ApClrAddrFilterTbl_Type()
)
apClrAddrFilterTbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apClrAddrFilterTbl.setStatus("mandatory")


class _ApLdACLFrMUList_Type(Integer32):
    """Custom type apLdACLFrMUList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_ApLdACLFrMUList_Type.__name__ = "Integer32"
_ApLdACLFrMUList_Object = MibScalar
apLdACLFrMUList = _ApLdACLFrMUList_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 3, 6),
    _ApLdACLFrMUList_Type()
)
apLdACLFrMUList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLdACLFrMUList.setStatus("mandatory")


class _ApModemDialOut_Type(Integer32):
    """Custom type apModemDialOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_ApModemDialOut_Type.__name__ = "Integer32"
_ApModemDialOut_Object = MibScalar
apModemDialOut = _ApModemDialOut_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 3, 7),
    _ApModemDialOut_Type()
)
apModemDialOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apModemDialOut.setStatus("mandatory")


class _ApModemHangUp_Type(Integer32):
    """Custom type apModemHangUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_ApModemHangUp_Type.__name__ = "Integer32"
_ApModemHangUp_Object = MibScalar
apModemHangUp = _ApModemHangUp_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 3, 8),
    _ApModemHangUp_Type()
)
apModemHangUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apModemHangUp.setStatus("mandatory")


class _ApUpdateFirmware_Type(Integer32):
    """Custom type apUpdateFirmware based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_ApUpdateFirmware_Type.__name__ = "Integer32"
_ApUpdateFirmware_Object = MibScalar
apUpdateFirmware = _ApUpdateFirmware_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 3, 9),
    _ApUpdateFirmware_Type()
)
apUpdateFirmware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apUpdateFirmware.setStatus("mandatory")


class _ApDnLdFileName_Type(DisplayString):
    """Custom type apDnLdFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_ApDnLdFileName_Type.__name__ = "DisplayString"
_ApDnLdFileName_Object = MibScalar
apDnLdFileName = _ApDnLdFileName_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 3, 10),
    _ApDnLdFileName_Type()
)
apDnLdFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apDnLdFileName.setStatus("mandatory")
_ApTFTPServer_Type = IpAddress
_ApTFTPServer_Object = MibScalar
apTFTPServer = _ApTFTPServer_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 3, 11),
    _ApTFTPServer_Type()
)
apTFTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apTFTPServer.setStatus("mandatory")


class _ApResetAP_Type(Integer32):
    """Custom type apResetAP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_ApResetAP_Type.__name__ = "Integer32"
_ApResetAP_Object = MibScalar
apResetAP = _ApResetAP_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 3, 12),
    _ApResetAP_Type()
)
apResetAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apResetAP.setStatus("mandatory")


class _ApHTMLFileName_Type(DisplayString):
    """Custom type apHTMLFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_ApHTMLFileName_Type.__name__ = "DisplayString"
_ApHTMLFileName_Object = MibScalar
apHTMLFileName = _ApHTMLFileName_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 3, 13),
    _ApHTMLFileName_Type()
)
apHTMLFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apHTMLFileName.setStatus("mandatory")


class _ApUpdateHTMLFile_Type(Integer32):
    """Custom type apUpdateHTMLFile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_ApUpdateHTMLFile_Type.__name__ = "Integer32"
_ApUpdateHTMLFile_Object = MibScalar
apUpdateHTMLFile = _ApUpdateHTMLFile_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 3, 14),
    _ApUpdateHTMLFile_Type()
)
apUpdateHTMLFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apUpdateHTMLFile.setStatus("mandatory")


class _ApDHCPEnable_Type(Integer32):
    """Custom type apDHCPEnable based on Integer32"""
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


_ApDHCPEnable_Type.__name__ = "Integer32"
_ApDHCPEnable_Object = MibScalar
apDHCPEnable = _ApDHCPEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 3, 15),
    _ApDHCPEnable_Type()
)
apDHCPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apDHCPEnable.setStatus("mandatory")


class _ApUpdAllAPsFirmware_Type(Integer32):
    """Custom type apUpdAllAPsFirmware based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_ApUpdAllAPsFirmware_Type.__name__ = "Integer32"
_ApUpdAllAPsFirmware_Object = MibScalar
apUpdAllAPsFirmware = _ApUpdAllAPsFirmware_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 3, 16),
    _ApUpdAllAPsFirmware_Type()
)
apUpdAllAPsFirmware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apUpdAllAPsFirmware.setStatus("mandatory")


class _ApUpdAllAPsHTMLFile_Type(Integer32):
    """Custom type apUpdAllAPsHTMLFile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_ApUpdAllAPsHTMLFile_Type.__name__ = "Integer32"
_ApUpdAllAPsHTMLFile_Object = MibScalar
apUpdAllAPsHTMLFile = _ApUpdAllAPsHTMLFile_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 3, 17),
    _ApUpdAllAPsHTMLFile_Type()
)
apUpdAllAPsHTMLFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apUpdAllAPsHTMLFile.setStatus("mandatory")


class _ApTFTPUpdBothFiles_Type(Integer32):
    """Custom type apTFTPUpdBothFiles based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_ApTFTPUpdBothFiles_Type.__name__ = "Integer32"
_ApTFTPUpdBothFiles_Object = MibScalar
apTFTPUpdBothFiles = _ApTFTPUpdBothFiles_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 3, 18),
    _ApTFTPUpdBothFiles_Type()
)
apTFTPUpdBothFiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apTFTPUpdBothFiles.setStatus("mandatory")


class _ApHelpURL_Type(DisplayString):
    """Custom type apHelpURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_ApHelpURL_Type.__name__ = "DisplayString"
_ApHelpURL_Object = MibScalar
apHelpURL = _ApHelpURL_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 3, 19),
    _ApHelpURL_Type()
)
apHelpURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apHelpURL.setStatus("mandatory")


class _ApFileUpdateStatus_Type(Integer32):
    """Custom type apFileUpdateStatus based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("bad-permissions-for-firmware-file", 10),
          ("corrupted-firmware-file", 15),
          ("download-successful", 1),
          ("error-during-TFTP-download", 13),
          ("firmware-file-not-found", 8),
          ("general-download-failure", 16),
          ("html-file-not-found", 9),
          ("no-ARP-response-from-server", 6),
          ("no-TFTP-service-on-server", 7),
          ("tftp-server-unreachable", 5),
          ("too-many-TFTP-retries", 14),
          ("too-many-XMODEM-errors", 2),
          ("unable-to-open-HTML-file", 12),
          ("unable-to-open-firmware-file", 11),
          ("xmodem-packets-out-of-order", 4),
          ("xmodem-transfer-cancelled", 3))
    )


_ApFileUpdateStatus_Type.__name__ = "Integer32"
_ApFileUpdateStatus_Object = MibScalar
apFileUpdateStatus = _ApFileUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 3, 20),
    _ApFileUpdateStatus_Type()
)
apFileUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFileUpdateStatus.setStatus("mandatory")


class _ApFlashLEDs_Type(Integer32):
    """Custom type apFlashLEDs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_ApFlashLEDs_Type.__name__ = "Integer32"
_ApFlashLEDs_Object = MibScalar
apFlashLEDs = _ApFlashLEDs_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 3, 21),
    _ApFlashLEDs_Type()
)
apFlashLEDs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apFlashLEDs.setStatus("mandatory")
_ApSecurityMgmt_ObjectIdentity = ObjectIdentity
apSecurityMgmt = _ApSecurityMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 4)
)
_ApACLViolations_Type = Counter32
_ApACLViolations_Object = MibScalar
apACLViolations = _ApACLViolations_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 4, 1),
    _ApACLViolations_Type()
)
apACLViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apACLViolations.setStatus("mandatory")


class _ApSaveConfig_Type(Integer32):
    """Custom type apSaveConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_ApSaveConfig_Type.__name__ = "Integer32"
_ApSaveConfig_Object = MibScalar
apSaveConfig = _ApSaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 4, 2),
    _ApSaveConfig_Type()
)
apSaveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSaveConfig.setStatus("mandatory")
_ApAccCtrlTable_Object = MibTable
apAccCtrlTable = _ApAccCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 4, 3)
)
if mibBuilder.loadTexts:
    apAccCtrlTable.setStatus("mandatory")
_ApAccCtrlEntry_Object = MibTableRow
apAccCtrlEntry = _ApAccCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 4, 3, 1)
)
apAccCtrlEntry.setIndexNames(
    (0, "SYMBOL-DSSS-ENTERPRISE-PRIVATE-MIB", "allowedIndex"),
)
if mibBuilder.loadTexts:
    apAccCtrlEntry.setStatus("mandatory")


class _AllowedIndex_Type(Integer32):
    """Custom type allowedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_AllowedIndex_Type.__name__ = "Integer32"
_AllowedIndex_Object = MibTableColumn
allowedIndex = _AllowedIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 4, 3, 1, 1),
    _AllowedIndex_Type()
)
allowedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    allowedIndex.setStatus("mandatory")
_AllowedMU_Type = PhysAddress
_AllowedMU_Object = MibTableColumn
allowedMU = _AllowedMU_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 4, 3, 1, 2),
    _AllowedMU_Type()
)
allowedMU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    allowedMU.setStatus("mandatory")
_ApACLRangeTable_Object = MibTable
apACLRangeTable = _ApACLRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 4, 4)
)
if mibBuilder.loadTexts:
    apACLRangeTable.setStatus("mandatory")
_ApACLRangeEntry_Object = MibTableRow
apACLRangeEntry = _ApACLRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 4, 4, 1)
)
apACLRangeEntry.setIndexNames(
    (0, "SYMBOL-DSSS-ENTERPRISE-PRIVATE-MIB", "apACLRangeIndex"),
)
if mibBuilder.loadTexts:
    apACLRangeEntry.setStatus("mandatory")


class _ApACLRangeIndex_Type(Integer32):
    """Custom type apACLRangeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ApACLRangeIndex_Type.__name__ = "Integer32"
_ApACLRangeIndex_Object = MibTableColumn
apACLRangeIndex = _ApACLRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 4, 4, 1, 1),
    _ApACLRangeIndex_Type()
)
apACLRangeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apACLRangeIndex.setStatus("mandatory")
_LowMacAddr_Type = PhysAddress
_LowMacAddr_Object = MibTableColumn
lowMacAddr = _LowMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 4, 4, 1, 2),
    _LowMacAddr_Type()
)
lowMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowMacAddr.setStatus("mandatory")
_HighMacAddr_Type = PhysAddress
_HighMacAddr_Object = MibTableColumn
highMacAddr = _HighMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 4, 4, 1, 3),
    _HighMacAddr_Type()
)
highMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highMacAddr.setStatus("mandatory")


class _ApSaveConfigAllAPs_Type(Integer32):
    """Custom type apSaveConfigAllAPs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_ApSaveConfigAllAPs_Type.__name__ = "Integer32"
_ApSaveConfigAllAPs_Object = MibScalar
apSaveConfigAllAPs = _ApSaveConfigAllAPs_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 4, 5),
    _ApSaveConfigAllAPs_Type()
)
apSaveConfigAllAPs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSaveConfigAllAPs.setStatus("mandatory")


class _ApWEPLicenseKey_Type(DisplayString):
    """Custom type apWEPLicenseKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ApWEPLicenseKey_Type.__name__ = "DisplayString"
_ApWEPLicenseKey_Object = MibScalar
apWEPLicenseKey = _ApWEPLicenseKey_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 4, 6),
    _ApWEPLicenseKey_Type()
)
apWEPLicenseKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWEPLicenseKey.setStatus("mandatory")


class _Ap128bWEPFlag_Type(Integer32):
    """Custom type ap128bWEPFlag based on Integer32"""
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


_Ap128bWEPFlag_Type.__name__ = "Integer32"
_Ap128bWEPFlag_Object = MibScalar
ap128bWEPFlag = _Ap128bWEPFlag_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 4, 7),
    _Ap128bWEPFlag_Type()
)
ap128bWEPFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap128bWEPFlag.setStatus("mandatory")

# Managed Objects groups


# Notification objects

coldStart = NotificationType(
    (1, 3, 6, 1, 2, 1, 11, 0, 0)
)
coldStart.setObjects(
    ("SYMBOL-DSSS-ENTERPRISE-PRIVATE-MIB", "apMyMacAddr")
)
if mibBuilder.loadTexts:
    coldStart.setStatus(
        ""
    )

authenticationFailure = NotificationType(
    (1, 3, 6, 1, 2, 1, 11, 0, 4)
)
authenticationFailure.setObjects(
      *(("SYMBOL-DSSS-ENTERPRISE-PRIVATE-MIB", "apMyMacAddr"),
        ("SYMBOL-DSSS-ENTERPRISE-PRIVATE-MIB", "apAPMacAddr"))
)
if mibBuilder.loadTexts:
    authenticationFailure.setStatus(
        ""
    )

apDSAPRFStartUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 0, 101)
)
apDSAPRFStartUpTrap.setObjects(
    ("SYMBOL-DSSS-ENTERPRISE-PRIVATE-MIB", "apMyMacAddr")
)
if mibBuilder.loadTexts:
    apDSAPRFStartUpTrap.setStatus(
        ""
    )

apDSAPACLViolationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 0, 102)
)
apDSAPACLViolationTrap.setObjects(
      *(("SYMBOL-DSSS-ENTERPRISE-PRIVATE-MIB", "apMyMacAddr"),
        ("SYMBOL-DSSS-ENTERPRISE-PRIVATE-MIB", "muMacAddr"))
)
if mibBuilder.loadTexts:
    apDSAPACLViolationTrap.setStatus(
        ""
    )

apDSAPMUAssocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 0, 111)
)
apDSAPMUAssocTrap.setObjects(
      *(("SYMBOL-DSSS-ENTERPRISE-PRIVATE-MIB", "apMyMacAddr"),
        ("SYMBOL-DSSS-ENTERPRISE-PRIVATE-MIB", "muMacAddr"),
        ("SYMBOL-DSSS-ENTERPRISE-PRIVATE-MIB", "apCurrentMUs"))
)
if mibBuilder.loadTexts:
    apDSAPMUAssocTrap.setStatus(
        ""
    )

apDSAPMUUnAssocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 0, 112)
)
apDSAPMUUnAssocTrap.setObjects(
      *(("SYMBOL-DSSS-ENTERPRISE-PRIVATE-MIB", "apMyMacAddr"),
        ("SYMBOL-DSSS-ENTERPRISE-PRIVATE-MIB", "muMacAddr"),
        ("SYMBOL-DSSS-ENTERPRISE-PRIVATE-MIB", "apCurrentMUs"))
)
if mibBuilder.loadTexts:
    apDSAPMUUnAssocTrap.setStatus(
        ""
    )

apDSAPMUMaxAssocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 0, 116)
)
apDSAPMUMaxAssocTrap.setObjects(
      *(("SYMBOL-DSSS-ENTERPRISE-PRIVATE-MIB", "apMyMacAddr"),
        ("SYMBOL-DSSS-ENTERPRISE-PRIVATE-MIB", "apCurrentMUs"))
)
if mibBuilder.loadTexts:
    apDSAPMUMaxAssocTrap.setStatus(
        ""
    )

apDSRootWLAPUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 0, 121)
)
apDSRootWLAPUpTrap.setObjects(
      *(("SYMBOL-DSSS-ENTERPRISE-PRIVATE-MIB", "apMyMacAddr"),
        ("SYMBOL-DSSS-ENTERPRISE-PRIVATE-MIB", "apAPMacAddr"),
        ("SYMBOL-DSSS-ENTERPRISE-PRIVATE-MIB", "apNbrOfWLAPItfs"))
)
if mibBuilder.loadTexts:
    apDSRootWLAPUpTrap.setStatus(
        ""
    )

apDSRootWLAPLostTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 0, 122)
)
apDSRootWLAPLostTrap.setObjects(
      *(("SYMBOL-DSSS-ENTERPRISE-PRIVATE-MIB", "apMyMacAddr"),
        ("SYMBOL-DSSS-ENTERPRISE-PRIVATE-MIB", "apAPMacAddr"),
        ("SYMBOL-DSSS-ENTERPRISE-PRIVATE-MIB", "apNbrOfWLAPItfs"))
)
if mibBuilder.loadTexts:
    apDSRootWLAPLostTrap.setStatus(
        ""
    )

apDSDsgntedWLAPUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 0, 123)
)
apDSDsgntedWLAPUpTrap.setObjects(
      *(("SYMBOL-DSSS-ENTERPRISE-PRIVATE-MIB", "apMyMacAddr"),
        ("SYMBOL-DSSS-ENTERPRISE-PRIVATE-MIB", "apAPMacAddr"),
        ("SYMBOL-DSSS-ENTERPRISE-PRIVATE-MIB", "apNbrOfWLAPItfs"))
)
if mibBuilder.loadTexts:
    apDSDsgntedWLAPUpTrap.setStatus(
        ""
    )

apDSDsgnatedWLAPLostTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 0, 124)
)
apDSDsgnatedWLAPLostTrap.setObjects(
      *(("SYMBOL-DSSS-ENTERPRISE-PRIVATE-MIB", "apMyMacAddr"),
        ("SYMBOL-DSSS-ENTERPRISE-PRIVATE-MIB", "apAPMacAddr"),
        ("SYMBOL-DSSS-ENTERPRISE-PRIVATE-MIB", "apNbrOfWLAPItfs"))
)
if mibBuilder.loadTexts:
    apDSDsgnatedWLAPLostTrap.setStatus(
        ""
    )

apDSAPDHCPConfigChgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 0, 130)
)
apDSAPDHCPConfigChgTrap.setObjects(
    ("SYMBOL-DSSS-ENTERPRISE-PRIVATE-MIB", "apMyMacAddr")
)
if mibBuilder.loadTexts:
    apDSAPDHCPConfigChgTrap.setStatus(
        ""
    )

apDSAPDHCPLeaseUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 1, 5, 0, 131)
)
apDSAPDHCPLeaseUpTrap.setObjects(
    ("SYMBOL-DSSS-ENTERPRISE-PRIVATE-MIB", "apMyMacAddr")
)
if mibBuilder.loadTexts:
    apDSAPDHCPLeaseUpTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYMBOL-DSSS-ENTERPRISE-PRIVATE-MIB",
    **{"WEPKeytype128b": WEPKeytype128b,
       "coldStart": coldStart,
       "authenticationFailure": authenticationFailure,
       "symbol": symbol,
       "spectrum24": spectrum24,
       "dsap": dsap,
       "apDSAPRFStartUpTrap": apDSAPRFStartUpTrap,
       "apDSAPACLViolationTrap": apDSAPACLViolationTrap,
       "apDSAPMUAssocTrap": apDSAPMUAssocTrap,
       "apDSAPMUUnAssocTrap": apDSAPMUUnAssocTrap,
       "apDSAPMUMaxAssocTrap": apDSAPMUMaxAssocTrap,
       "apDSRootWLAPUpTrap": apDSRootWLAPUpTrap,
       "apDSRootWLAPLostTrap": apDSRootWLAPLostTrap,
       "apDSDsgntedWLAPUpTrap": apDSDsgntedWLAPUpTrap,
       "apDSDsgnatedWLAPLostTrap": apDSDsgnatedWLAPLostTrap,
       "apDSAPDHCPConfigChgTrap": apDSAPDHCPConfigChgTrap,
       "apDSAPDHCPLeaseUpTrap": apDSAPDHCPLeaseUpTrap,
       "apConfigMgmt": apConfigMgmt,
       "apManufactureInfo": apManufactureInfo,
       "apModelnumber": apModelnumber,
       "apSerialnumber": apSerialnumber,
       "apHardwareRev": apHardwareRev,
       "apMyMacAddr": apMyMacAddr,
       "apAPFirmwareRev": apAPFirmwareRev,
       "apRFFirmwareRev": apRFFirmwareRev,
       "apMfgDate": apMfgDate,
       "apHTMLFileRev": apHTMLFileRev,
       "apVendorID": apVendorID,
       "apSystemConfig": apSystemConfig,
       "apUnitName": apUnitName,
       "apMyIPAddr": apMyIPAddr,
       "apSubnetMask": apSubnetMask,
       "apGatewayIPAddr": apGatewayIPAddr,
       "apDefaultInterface": apDefaultInterface,
       "apEnetPortState": apEnetPortState,
       "apEthernetTimeOut": apEthernetTimeOut,
       "apTelnetEnable": apTelnetEnable,
       "apAccCtrlEnable": apAccCtrlEnable,
       "apTypeFilterEnable": apTypeFilterEnable,
       "apWNMPEnable": apWNMPEnable,
       "apAPStateXchgEnable": apAPStateXchgEnable,
       "apS24MobileIPEnable": apS24MobileIPEnable,
       "apAgentAdInterval": apAgentAdInterval,
       "apWebServerEnable": apWebServerEnable,
       "apMobileHomeMD5Key": apMobileHomeMD5Key,
       "apAdditionalGatewaysTable": apAdditionalGatewaysTable,
       "apAdditionalGatewaysEntry": apAdditionalGatewaysEntry,
       "additionalGatewaysIndex": additionalGatewaysIndex,
       "apAdditionalGatewaysIPAddr": apAdditionalGatewaysIPAddr,
       "apMUMUDisallowed": apMUMUDisallowed,
       "apEncryptAdmin": apEncryptAdmin,
       "apSNMPInfo": apSNMPInfo,
       "apSNMPMode": apSNMPMode,
       "apROCommunityName": apROCommunityName,
       "apRWCommunityName": apRWCommunityName,
       "apTrapHost1IpAdr": apTrapHost1IpAdr,
       "apAllTrapsEnable": apAllTrapsEnable,
       "apColdBootTrapEnable": apColdBootTrapEnable,
       "apAuthenFailureTrapEnable": apAuthenFailureTrapEnable,
       "apRFTrapEnable": apRFTrapEnable,
       "apACLTrapEnable": apACLTrapEnable,
       "apMUStateChngTrapEnable": apMUStateChngTrapEnable,
       "apWLAPConnChngTrapEnable": apWLAPConnChngTrapEnable,
       "apDHCPChangeEnable": apDHCPChangeEnable,
       "apSNMPRequests": apSNMPRequests,
       "apSNMPTraps": apSNMPTraps,
       "apTrapHost2IpAdr": apTrapHost2IpAdr,
       "apRFConfig": apRFConfig,
       "apRFPortState": apRFPortState,
       "apNetID": apNetID,
       "apCountryName": apCountryName,
       "apAntennaSelect": apAntennaSelect,
       "apBCMCQMax": apBCMCQMax,
       "apReassemblyTimeOut": apReassemblyTimeOut,
       "apMaxRetries": apMaxRetries,
       "apMulticastMask": apMulticastMask,
       "apAcceptBCESSID": apAcceptBCESSID,
       "apMUInactivityTimeOut": apMUInactivityTimeOut,
       "apWLAPMode": apWLAPMode,
       "apWLAPPriority": apWLAPPriority,
       "apWLAPManualBSSID": apWLAPManualBSSID,
       "apWLAPHelloTime": apWLAPHelloTime,
       "apWLAPMaxAge": apWLAPMaxAge,
       "apWLAPFwdDelay": apWLAPFwdDelay,
       "apMaxMUTrigger": apMaxMUTrigger,
       "apMaxRetriesVoice": apMaxRetriesVoice,
       "apMcastMaskVoice": apMcastMaskVoice,
       "apWEPAlgorithm": apWEPAlgorithm,
       "apRFRate11Mb": apRFRate11Mb,
       "apRFRate5-5Mb": apRFRate5_5Mb,
       "apRFRate2Mb": apRFRate2Mb,
       "apRFRate1Mb": apRFRate1Mb,
       "apRFPreamble": apRFPreamble,
       "apRadioType": apRadioType,
       "apSerialPortConfig": apSerialPortConfig,
       "apPPPState": apPPPState,
       "apSerialPortUse": apSerialPortUse,
       "apModemConnected": apModemConnected,
       "apConnectMode": apConnectMode,
       "apDialOutNumber": apDialOutNumber,
       "apDialOutMode": apDialOutMode,
       "apAnswerWaitTime": apAnswerWaitTime,
       "apModemSpeaker": apModemSpeaker,
       "apInactivityTimeout": apInactivityTimeout,
       "apPPPTimeout": apPPPTimeout,
       "apPPPTerminates": apPPPTerminates,
       "apAddrFilterTable": apAddrFilterTable,
       "apAddrFilterEntry": apAddrFilterEntry,
       "disallowedIndex": disallowedIndex,
       "disallowedMU": disallowedMU,
       "apTypeFilterTable": apTypeFilterTable,
       "apTypeFilterEntry": apTypeFilterEntry,
       "typeIndex": typeIndex,
       "etherType": etherType,
       "ap128bWEPKeyTable": ap128bWEPKeyTable,
       "apWEPKeyEntry": apWEPKeyEntry,
       "ap128bWepkeyIndex": ap128bWepkeyIndex,
       "ap128bWepKeyValue": ap128bWepKeyValue,
       "apPerformMgmt": apPerformMgmt,
       "apTrafficMatrixTable": apTrafficMatrixTable,
       "apTrafficMatrixEntry": apTrafficMatrixEntry,
       "apTMTableIndex": apTMTableIndex,
       "apProtoItfName": apProtoItfName,
       "apNPktsToEnets": apNPktsToEnets,
       "apNPktsToPpps": apNPktsToPpps,
       "apNPktsToRfs": apNPktsToRfs,
       "apNPktsToAPStks": apNPktsToAPStks,
       "apItfStatTable": apItfStatTable,
       "apItfStatEntry": apItfStatEntry,
       "apItfStatIndex": apItfStatIndex,
       "apInterfaceName": apInterfaceName,
       "apPacketsIns": apPacketsIns,
       "apPacketsOuts": apPacketsOuts,
       "apOctetsIns": apOctetsIns,
       "apOctetsOuts": apOctetsOuts,
       "apPktsInPerSec": apPktsInPerSec,
       "apPktsOutPerSec": apPktsOutPerSec,
       "apOctInPerSec": apOctInPerSec,
       "apOctOutPerSec": apOctOutPerSec,
       "apEthernetStatistics": apEthernetStatistics,
       "apEPktsSeens": apEPktsSeens,
       "apEPktsForwardeds": apEPktsForwardeds,
       "apEPktsDiscNoMatchs": apEPktsDiscNoMatchs,
       "apEPktsDiscForceds": apEPktsDiscForceds,
       "apEPktsDiscBuffers": apEPktsDiscBuffers,
       "apEPktsDiscCRCs": apEPktsDiscCRCs,
       "apEPktsSents": apEPktsSents,
       "apEAnyCollisions": apEAnyCollisions,
       "apE1orMoreColls": apE1orMoreColls,
       "apEMaxCollisions": apEMaxCollisions,
       "apELateCollisions": apELateCollisions,
       "apEPktsDefers": apEPktsDefers,
       "apEBcMcPkts": apEBcMcPkts,
       "apEIndividualAddrs": apEIndividualAddrs,
       "apRFStatistics": apRFStatistics,
       "rfBcMcPktsSents": rfBcMcPktsSents,
       "rfBcMcPktsRcvds": rfBcMcPktsRcvds,
       "rfBcMcOctSents": rfBcMcOctSents,
       "rfBcMcOctRcvds": rfBcMcOctRcvds,
       "rfSysPktsSents": rfSysPktsSents,
       "rfSysPktsRcvds": rfSysPktsRcvds,
       "rfSBcMcPktsSents": rfSBcMcPktsSents,
       "rfSBcMcPktsRcvds": rfSBcMcPktsRcvds,
       "rfSuccFragPkts": rfSuccFragPkts,
       "rfUnsuccFragPkts": rfUnsuccFragPkts,
       "rfTotalFragSents": rfTotalFragSents,
       "rfTotalFragRcvds": rfTotalFragRcvds,
       "rfSuccReassPkts": rfSuccReassPkts,
       "rfUnsuccReassPkts": rfUnsuccReassPkts,
       "rfAssocMUs": rfAssocMUs,
       "rfRcvdCRCErrors": rfRcvdCRCErrors,
       "rfRcvdDupPkts": rfRcvdDupPkts,
       "rfTotalCollisions": rfTotalCollisions,
       "rfPktsWithoutColls": rfPktsWithoutColls,
       "rfPktsWithMaxColls": rfPktsWithMaxColls,
       "rfPktsWithColls": rfPktsWithColls,
       "rfDataPktsSents": rfDataPktsSents,
       "rfDataPktsRcvds": rfDataPktsRcvds,
       "rfDataOctetsSents": rfDataOctetsSents,
       "rfDataOctetsRcvds": rfDataOctetsRcvds,
       "rfEncrypPktsSents": rfEncrypPktsSents,
       "rfEncrypPktsRcvds": rfEncrypPktsRcvds,
       "apSerialPortStatistics": apSerialPortStatistics,
       "apNbrOfDialouts": apNbrOfDialouts,
       "apDialoutFailures": apDialoutFailures,
       "apNbrOfAnswers": apNbrOfAnswers,
       "apCurrCallTime": apCurrCallTime,
       "apLastCallTime": apLastCallTime,
       "apWNMPStatistics": apWNMPStatistics,
       "apWNMPCfgPkts": apWNMPCfgPkts,
       "wEchoRequests": wEchoRequests,
       "wPingRequests": wPingRequests,
       "wPktsFromNVs": wPktsFromNVs,
       "wPPktsToNVs": wPPktsToNVs,
       "wPassThruEchoes": wPassThruEchoes,
       "apMUInfo": apMUInfo,
       "apCurrentMUs": apCurrentMUs,
       "apMaxMUs": apMaxMUs,
       "apTotalAssocs": apTotalAssocs,
       "apMUTable": apMUTable,
       "apMUEntry": apMUEntry,
       "muIndex": muIndex,
       "muMacAddr": muMacAddr,
       "muInterface": muInterface,
       "muState": muState,
       "muPowerMode": muPowerMode,
       "muStationID": muStationID,
       "muLastAPAddr": muLastAPAddr,
       "muTotalAssoc": muTotalAssoc,
       "muAssocStart": muAssocStart,
       "muLstAssStrt": muLstAssStrt,
       "muLastAssEnd": muLastAssEnd,
       "muNPktsSents": muNPktsSents,
       "muNPktsRcvds": muNPktsRcvds,
       "muNBytesSents": muNBytesSents,
       "muNBytesRcvds": muNBytesRcvds,
       "muNDiscdPkts": muNDiscdPkts,
       "muTmLastData": muTmLastData,
       "muPriority": muPriority,
       "muSupportedRates": muSupportedRates,
       "muCurrentXmtRate": muCurrentXmtRate,
       "muLastActivity": muLastActivity,
       "apMUHmAgTable": apMUHmAgTable,
       "apMUHATEntry": apMUHATEntry,
       "muHATMUIpAddr": muHATMUIpAddr,
       "muHATFrAgIpAddr": muHATFrAgIpAddr,
       "apMUFrAgTable": apMUFrAgTable,
       "apMUFATEntry": apMUFATEntry,
       "muFATMUIpAddr": muFATMUIpAddr,
       "muFATHmAgIpAddr": muFATHmAgIpAddr,
       "apKnownAPsTable": apKnownAPsTable,
       "apKnownAPsEntry": apKnownAPsEntry,
       "apAPMacAddr": apAPMacAddr,
       "apAPIpAddr": apAPIpAddr,
       "apHoppingSet": apHoppingSet,
       "apHoppingSeq": apHoppingSeq,
       "apNbrOfMUs": apNbrOfMUs,
       "apKBIOS": apKBIOS,
       "apAway": apAway,
       "ap802dot11Protocol": ap802dot11Protocol,
       "apFwVer": apFwVer,
       "apDSchannel": apDSchannel,
       "apFilterStatistics": apFilterStatistics,
       "apAdrViolations": apAdrViolations,
       "apTypeViolations": apTypeViolations,
       "apWLAPInfo": apWLAPInfo,
       "apNbrOfWLAPItfs": apNbrOfWLAPItfs,
       "apWLAPState": apWLAPState,
       "apWLAPHopSequence": apWLAPHopSequence,
       "apRootInterface": apRootInterface,
       "apRootWLAPID": apRootWLAPID,
       "apRootPathCost": apRootPathCost,
       "apWLAPID": apWLAPID,
       "apWLAPItfTable": apWLAPItfTable,
       "apWLAPItfEntry": apWLAPItfEntry,
       "apWLAPItfID": apWLAPItfID,
       "apWLAPItfAddr": apWLAPItfAddr,
       "apWLAPItfState": apWLAPItfState,
       "apWLAPPathCost": apWLAPPathCost,
       "apDsgnatedRoot": apDsgnatedRoot,
       "apDsgnatedCost": apDsgnatedCost,
       "apDsgnatedWLAP": apDsgnatedWLAP,
       "apDsgnatedItf": apDsgnatedItf,
       "apRetryHistogramTable": apRetryHistogramTable,
       "apRetryHistogramEntry": apRetryHistogramEntry,
       "apRetryHistogramIndex": apRetryHistogramIndex,
       "apNumberOfRetries": apNumberOfRetries,
       "apPacketsHistogramCounts": apPacketsHistogramCounts,
       "apDSPerFreqStatTable": apDSPerFreqStatTable,
       "apDSPerFreqStatEntry": apDSPerFreqStatEntry,
       "rfDSFrequency": rfDSFrequency,
       "rfDSPerFqPktsSents": rfDSPerFqPktsSents,
       "rfDSPerFqPktsRcvds": rfDSPerFqPktsRcvds,
       "rfDSPerFqRetries": rfDSPerFqRetries,
       "apMobileIPStatistics": apMobileIPStatistics,
       "apAgentAdSents": apAgentAdSents,
       "apRegRequestRcvds": apRegRequestRcvds,
       "apRegReplySents": apRegReplySents,
       "apFaultMgmt": apFaultMgmt,
       "apClrAllStatistics": apClrAllStatistics,
       "apClrMUTable": apClrMUTable,
       "apClrACL": apClrACL,
       "apClrACLRangeTable": apClrACLRangeTable,
       "apClrAddrFilterTbl": apClrAddrFilterTbl,
       "apLdACLFrMUList": apLdACLFrMUList,
       "apModemDialOut": apModemDialOut,
       "apModemHangUp": apModemHangUp,
       "apUpdateFirmware": apUpdateFirmware,
       "apDnLdFileName": apDnLdFileName,
       "apTFTPServer": apTFTPServer,
       "apResetAP": apResetAP,
       "apHTMLFileName": apHTMLFileName,
       "apUpdateHTMLFile": apUpdateHTMLFile,
       "apDHCPEnable": apDHCPEnable,
       "apUpdAllAPsFirmware": apUpdAllAPsFirmware,
       "apUpdAllAPsHTMLFile": apUpdAllAPsHTMLFile,
       "apTFTPUpdBothFiles": apTFTPUpdBothFiles,
       "apHelpURL": apHelpURL,
       "apFileUpdateStatus": apFileUpdateStatus,
       "apFlashLEDs": apFlashLEDs,
       "apSecurityMgmt": apSecurityMgmt,
       "apACLViolations": apACLViolations,
       "apSaveConfig": apSaveConfig,
       "apAccCtrlTable": apAccCtrlTable,
       "apAccCtrlEntry": apAccCtrlEntry,
       "allowedIndex": allowedIndex,
       "allowedMU": allowedMU,
       "apACLRangeTable": apACLRangeTable,
       "apACLRangeEntry": apACLRangeEntry,
       "apACLRangeIndex": apACLRangeIndex,
       "lowMacAddr": lowMacAddr,
       "highMacAddr": highMacAddr,
       "apSaveConfigAllAPs": apSaveConfigAllAPs,
       "apWEPLicenseKey": apWEPLicenseKey,
       "ap128bWEPFlag": ap128bWEPFlag}
)
