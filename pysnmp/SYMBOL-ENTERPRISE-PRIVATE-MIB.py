# SNMP MIB module (SYMBOL-ENTERPRISE-PRIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SYMBOL-ENTERPRISE-PRIVATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:59:39 2024
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
_ApProduct_ObjectIdentity = ObjectIdentity
apProduct = _ApProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 1, 1)
)
_ApConfigMgmt_ObjectIdentity = ObjectIdentity
apConfigMgmt = _ApConfigMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1)
)
_ApManufactureInfo_ObjectIdentity = ObjectIdentity
apManufactureInfo = _ApManufactureInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 1)
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 1, 3),
    _ApHardwareRev_Type()
)
apHardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apHardwareRev.setStatus("mandatory")
_ApMyMacAddr_Type = PhysAddress
_ApMyMacAddr_Object = MibScalar
apMyMacAddr = _ApMyMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 1, 5),
    _ApAPFirmwareRev_Type()
)
apAPFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAPFirmwareRev.setStatus("mandatory")


class _ApRFFirmwareRev_Type(DisplayString):
    """Custom type apRFFirmwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_ApRFFirmwareRev_Type.__name__ = "DisplayString"
_ApRFFirmwareRev_Object = MibScalar
apRFFirmwareRev = _ApRFFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 1, 6),
    _ApRFFirmwareRev_Type()
)
apRFFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRFFirmwareRev.setStatus("mandatory")
_ApSystemConfig_ObjectIdentity = ObjectIdentity
apSystemConfig = _ApSystemConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 2)
)


class _ApSystemName_Type(DisplayString):
    """Custom type apSystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ApSystemName_Type.__name__ = "DisplayString"
_ApSystemName_Object = MibScalar
apSystemName = _ApSystemName_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 2, 1),
    _ApSystemName_Type()
)
apSystemName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSystemName.setStatus("mandatory")
_ApMyIPAddr_Type = IpAddress
_ApMyIPAddr_Object = MibScalar
apMyIPAddr = _ApMyIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 2, 2),
    _ApMyIPAddr_Type()
)
apMyIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apMyIPAddr.setStatus("mandatory")
_ApSubnetMask_Type = IpAddress
_ApSubnetMask_Object = MibScalar
apSubnetMask = _ApSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 2, 3),
    _ApSubnetMask_Type()
)
apSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSubnetMask.setStatus("mandatory")
_ApGatewayIPAddr_Type = IpAddress
_ApGatewayIPAddr_Object = MibScalar
apGatewayIPAddr = _ApGatewayIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 2, 4),
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
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 2),
          ("ppp", 1))
    )


_ApDefaultInterface_Type.__name__ = "Integer32"
_ApDefaultInterface_Object = MibScalar
apDefaultInterface = _ApDefaultInterface_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 2, 5),
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 2, 6),
    _ApEnetPortState_Type()
)
apEnetPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apEnetPortState.setStatus("mandatory")
_ApEthernetTimeOut_Type = Integer32
_ApEthernetTimeOut_Object = MibScalar
apEthernetTimeOut = _ApEthernetTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 2, 7),
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 2, 8),
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 2, 9),
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 2, 10),
    _ApTypeFilterEnable_Type()
)
apTypeFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apTypeFilterEnable.setStatus("mandatory")


class _ApMUAutoCfgEnable_Type(Integer32):
    """Custom type apMUAutoCfgEnable based on Integer32"""
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


_ApMUAutoCfgEnable_Type.__name__ = "Integer32"
_ApMUAutoCfgEnable_Object = MibScalar
apMUAutoCfgEnable = _ApMUAutoCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 2, 11),
    _ApMUAutoCfgEnable_Type()
)
apMUAutoCfgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apMUAutoCfgEnable.setStatus("mandatory")


class _ApAutoCfgEnable_Type(Integer32):
    """Custom type apAutoCfgEnable based on Integer32"""
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


_ApAutoCfgEnable_Type.__name__ = "Integer32"
_ApAutoCfgEnable_Object = MibScalar
apAutoCfgEnable = _ApAutoCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 2, 12),
    _ApAutoCfgEnable_Type()
)
apAutoCfgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAutoCfgEnable.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 2, 13),
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 2, 14),
    _ApAPStateXchgEnable_Type()
)
apAPStateXchgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAPStateXchgEnable.setStatus("mandatory")
_ApSNMPInfo_ObjectIdentity = ObjectIdentity
apSNMPInfo = _ApSNMPInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 3)
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 3, 1),
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 3, 2),
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 3, 3),
    _ApRWCommunityName_Type()
)
apRWCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRWCommunityName.setStatus("mandatory")
_ApTrapRcvrIpAdr_Type = IpAddress
_ApTrapRcvrIpAdr_Object = MibScalar
apTrapRcvrIpAdr = _ApTrapRcvrIpAdr_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 3, 4),
    _ApTrapRcvrIpAdr_Type()
)
apTrapRcvrIpAdr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apTrapRcvrIpAdr.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 3, 5),
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
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_ApColdBootTrapEnable_Type.__name__ = "Integer32"
_ApColdBootTrapEnable_Object = MibScalar
apColdBootTrapEnable = _ApColdBootTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 3, 6),
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
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_ApAuthenFailureTrapEnable_Type.__name__ = "Integer32"
_ApAuthenFailureTrapEnable_Object = MibScalar
apAuthenFailureTrapEnable = _ApAuthenFailureTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 3, 7),
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
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_ApRFTrapEnable_Type.__name__ = "Integer32"
_ApRFTrapEnable_Object = MibScalar
apRFTrapEnable = _ApRFTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 3, 8),
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
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_ApACLTrapEnable_Type.__name__ = "Integer32"
_ApACLTrapEnable_Object = MibScalar
apACLTrapEnable = _ApACLTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 3, 9),
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
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_ApMUStateChngTrapEnable_Type.__name__ = "Integer32"
_ApMUStateChngTrapEnable_Object = MibScalar
apMUStateChngTrapEnable = _ApMUStateChngTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 3, 10),
    _ApMUStateChngTrapEnable_Type()
)
apMUStateChngTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apMUStateChngTrapEnable.setStatus("mandatory")


class _ApAPIdConflictTrapEnable_Type(Integer32):
    """Custom type apAPIdConflictTrapEnable based on Integer32"""
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


_ApAPIdConflictTrapEnable_Type.__name__ = "Integer32"
_ApAPIdConflictTrapEnable_Object = MibScalar
apAPIdConflictTrapEnable = _ApAPIdConflictTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 3, 11),
    _ApAPIdConflictTrapEnable_Type()
)
apAPIdConflictTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAPIdConflictTrapEnable.setStatus("mandatory")


class _ApWLAPConnChngTrapEnable_Type(Integer32):
    """Custom type apWLAPConnChngTrapEnable based on Integer32"""
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


_ApWLAPConnChngTrapEnable_Type.__name__ = "Integer32"
_ApWLAPConnChngTrapEnable_Object = MibScalar
apWLAPConnChngTrapEnable = _ApWLAPConnChngTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 3, 12),
    _ApWLAPConnChngTrapEnable_Type()
)
apWLAPConnChngTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWLAPConnChngTrapEnable.setStatus("mandatory")
_ApRFConfig_ObjectIdentity = ObjectIdentity
apRFConfig = _ApRFConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 4)
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 4, 1),
    _ApRFPortState_Type()
)
apRFPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRFPortState.setStatus("mandatory")


class _ApNetId_Type(OctetString):
    """Custom type apNetId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_ApNetId_Type.__name__ = "OctetString"
_ApNetId_Object = MibScalar
apNetId = _ApNetId_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 4, 2),
    _ApNetId_Type()
)
apNetId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apNetId.setStatus("mandatory")


class _ApApId_Type(OctetString):
    """Custom type apApId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_ApApId_Type.__name__ = "OctetString"
_ApApId_Object = MibScalar
apApId = _ApApId_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 4, 3),
    _ApApId_Type()
)
apApId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apApId.setStatus("mandatory")
_ApHopSequence_Type = Integer32
_ApHopSequence_Object = MibScalar
apHopSequence = _ApHopSequence_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 4, 4),
    _ApHopSequence_Type()
)
apHopSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apHopSequence.setStatus("mandatory")


class _ApCountryName_Type(DisplayString):
    """Custom type apCountryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 36),
    )


_ApCountryName_Type.__name__ = "DisplayString"
_ApCountryName_Object = MibScalar
apCountryName = _ApCountryName_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 4, 5),
    _ApCountryName_Type()
)
apCountryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCountryName.setStatus("mandatory")
_ApHopSet_Type = Integer32
_ApHopSet_Object = MibScalar
apHopSet = _ApHopSet_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 4, 6),
    _ApHopSet_Type()
)
apHopSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apHopSet.setStatus("mandatory")


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
        *(("primary-and-secondary", 1),
          ("primary-only", 2))
    )


_ApAntennaSelect_Type.__name__ = "Integer32"
_ApAntennaSelect_Object = MibScalar
apAntennaSelect = _ApAntennaSelect_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 4, 7),
    _ApAntennaSelect_Type()
)
apAntennaSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAntennaSelect.setStatus("mandatory")
_ApDTIMInterval_Type = Integer32
_ApDTIMInterval_Object = MibScalar
apDTIMInterval = _ApDTIMInterval_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 4, 8),
    _ApDTIMInterval_Type()
)
apDTIMInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apDTIMInterval.setStatus("mandatory")
_ApBCMCQMax_Type = Integer32
_ApBCMCQMax_Object = MibScalar
apBCMCQMax = _ApBCMCQMax_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 4, 9),
    _ApBCMCQMax_Type()
)
apBCMCQMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBCMCQMax.setStatus("mandatory")
_ApReassemblyTimeOut_Type = Integer32
_ApReassemblyTimeOut_Object = MibScalar
apReassemblyTimeOut = _ApReassemblyTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 4, 10),
    _ApReassemblyTimeOut_Type()
)
apReassemblyTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apReassemblyTimeOut.setStatus("mandatory")
_ApMaxRetries_Type = Integer32
_ApMaxRetries_Object = MibScalar
apMaxRetries = _ApMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 4, 11),
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 4, 12),
    _ApMulticastMask_Type()
)
apMulticastMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apMulticastMask.setStatus("mandatory")


class _ApEncryptCoeff_Type(OctetString):
    """Custom type apEncryptCoeff based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_ApEncryptCoeff_Type.__name__ = "OctetString"
_ApEncryptCoeff_Object = MibScalar
apEncryptCoeff = _ApEncryptCoeff_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 4, 13),
    _ApEncryptCoeff_Type()
)
apEncryptCoeff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apEncryptCoeff.setStatus("mandatory")


class _ApEncryptPhase_Type(OctetString):
    """Custom type apEncryptPhase based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_ApEncryptPhase_Type.__name__ = "OctetString"
_ApEncryptPhase_Object = MibScalar
apEncryptPhase = _ApEncryptPhase_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 4, 14),
    _ApEncryptPhase_Type()
)
apEncryptPhase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apEncryptPhase.setStatus("mandatory")


class _ApWLAPMode_Type(Integer32):
    """Custom type apWLAPMode based on Integer32"""
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


_ApWLAPMode_Type.__name__ = "Integer32"
_ApWLAPMode_Object = MibScalar
apWLAPMode = _ApWLAPMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 4, 15),
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 4, 16),
    _ApWLAPPriority_Type()
)
apWLAPPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWLAPPriority.setStatus("mandatory")


class _ApWLAPManualAPID_Type(OctetString):
    """Custom type apWLAPManualAPID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_ApWLAPManualAPID_Type.__name__ = "OctetString"
_ApWLAPManualAPID_Object = MibScalar
apWLAPManualAPID = _ApWLAPManualAPID_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 4, 17),
    _ApWLAPManualAPID_Type()
)
apWLAPManualAPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWLAPManualAPID.setStatus("mandatory")


class _ApWLAPEncryption_Type(Integer32):
    """Custom type apWLAPEncryption based on Integer32"""
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


_ApWLAPEncryption_Type.__name__ = "Integer32"
_ApWLAPEncryption_Object = MibScalar
apWLAPEncryption = _ApWLAPEncryption_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 4, 18),
    _ApWLAPEncryption_Type()
)
apWLAPEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWLAPEncryption.setStatus("mandatory")
_ApWLAPHelloTime_Type = Integer32
_ApWLAPHelloTime_Object = MibScalar
apWLAPHelloTime = _ApWLAPHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 4, 19),
    _ApWLAPHelloTime_Type()
)
apWLAPHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWLAPHelloTime.setStatus("mandatory")
_ApWLAPMaxAge_Type = Integer32
_ApWLAPMaxAge_Object = MibScalar
apWLAPMaxAge = _ApWLAPMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 4, 20),
    _ApWLAPMaxAge_Type()
)
apWLAPMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWLAPMaxAge.setStatus("mandatory")
_ApWLAPFwdDelay_Type = Integer32
_ApWLAPFwdDelay_Object = MibScalar
apWLAPFwdDelay = _ApWLAPFwdDelay_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 4, 21),
    _ApWLAPFwdDelay_Type()
)
apWLAPFwdDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWLAPFwdDelay.setStatus("mandatory")
_ApSerialPortConfig_ObjectIdentity = ObjectIdentity
apSerialPortConfig = _ApSerialPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 5)
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 5, 1),
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 5, 2),
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 5, 3),
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 5, 4),
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 5, 5),
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 5, 6),
    _ApDialOutMode_Type()
)
apDialOutMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apDialOutMode.setStatus("mandatory")
_ApAnswerWaitTime_Type = Integer32
_ApAnswerWaitTime_Object = MibScalar
apAnswerWaitTime = _ApAnswerWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 5, 7),
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 5, 8),
    _ApModemSpeaker_Type()
)
apModemSpeaker.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apModemSpeaker.setStatus("mandatory")
_ApInactivityTimeout_Type = Integer32
_ApInactivityTimeout_Object = MibScalar
apInactivityTimeout = _ApInactivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 5, 9),
    _ApInactivityTimeout_Type()
)
apInactivityTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apInactivityTimeout.setStatus("mandatory")
_ApPPPTimeout_Type = Integer32
_ApPPPTimeout_Object = MibScalar
apPPPTimeout = _ApPPPTimeout_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 5, 10),
    _ApPPPTimeout_Type()
)
apPPPTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apPPPTimeout.setStatus("mandatory")
_ApPPPTerminates_Type = Counter32
_ApPPPTerminates_Object = MibScalar
apPPPTerminates = _ApPPPTerminates_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 5, 11),
    _ApPPPTerminates_Type()
)
apPPPTerminates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apPPPTerminates.setStatus("mandatory")
_ApAddrFilterTable_Object = MibTable
apAddrFilterTable = _ApAddrFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    apAddrFilterTable.setStatus("mandatory")
_ApAddrFilterEntry_Object = MibTableRow
apAddrFilterEntry = _ApAddrFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 6, 1)
)
apAddrFilterEntry.setIndexNames(
    (0, "SYMBOL-ENTERPRISE-PRIVATE-MIB", "disallowedIndex"),
)
if mibBuilder.loadTexts:
    apAddrFilterEntry.setStatus("mandatory")


class _DisallowedIndex_Type(Integer32):
    """Custom type disallowedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_DisallowedIndex_Type.__name__ = "Integer32"
_DisallowedIndex_Object = MibTableColumn
disallowedIndex = _DisallowedIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 6, 1, 1),
    _DisallowedIndex_Type()
)
disallowedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disallowedIndex.setStatus("mandatory")
_DisallowedMU_Type = PhysAddress
_DisallowedMU_Object = MibTableColumn
disallowedMU = _DisallowedMU_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 6, 1, 2),
    _DisallowedMU_Type()
)
disallowedMU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    disallowedMU.setStatus("mandatory")
_ApTypeFilterTable_Object = MibTable
apTypeFilterTable = _ApTypeFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 7)
)
if mibBuilder.loadTexts:
    apTypeFilterTable.setStatus("mandatory")
_ApTypeFilterEntry_Object = MibTableRow
apTypeFilterEntry = _ApTypeFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 7, 1)
)
apTypeFilterEntry.setIndexNames(
    (0, "SYMBOL-ENTERPRISE-PRIVATE-MIB", "typeIndex"),
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 7, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 1, 7, 1, 2),
    _EtherType_Type()
)
etherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etherType.setStatus("mandatory")
_ApPerformMgmt_ObjectIdentity = ObjectIdentity
apPerformMgmt = _ApPerformMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2)
)
_ApTrafficMatrixTable_Object = MibTable
apTrafficMatrixTable = _ApTrafficMatrixTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    apTrafficMatrixTable.setStatus("mandatory")
_ApTrafficMatrixEntry_Object = MibTableRow
apTrafficMatrixEntry = _ApTrafficMatrixEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 1, 1)
)
apTrafficMatrixEntry.setIndexNames(
    (0, "SYMBOL-ENTERPRISE-PRIVATE-MIB", "apTMTableIndex"),
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 1, 1, 2),
    _ApProtoItfName_Type()
)
apProtoItfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProtoItfName.setStatus("mandatory")
_ApNPktsToEnets_Type = Counter32
_ApNPktsToEnets_Object = MibTableColumn
apNPktsToEnets = _ApNPktsToEnets_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 1, 1, 3),
    _ApNPktsToEnets_Type()
)
apNPktsToEnets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNPktsToEnets.setStatus("mandatory")
_ApNPktsToPpps_Type = Counter32
_ApNPktsToPpps_Object = MibTableColumn
apNPktsToPpps = _ApNPktsToPpps_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 1, 1, 4),
    _ApNPktsToPpps_Type()
)
apNPktsToPpps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNPktsToPpps.setStatus("mandatory")
_ApNPktsToRfs_Type = Counter32
_ApNPktsToRfs_Object = MibTableColumn
apNPktsToRfs = _ApNPktsToRfs_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 1, 1, 5),
    _ApNPktsToRfs_Type()
)
apNPktsToRfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNPktsToRfs.setStatus("mandatory")
_ApNPktsToAPStks_Type = Counter32
_ApNPktsToAPStks_Object = MibTableColumn
apNPktsToAPStks = _ApNPktsToAPStks_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 1, 1, 6),
    _ApNPktsToAPStks_Type()
)
apNPktsToAPStks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNPktsToAPStks.setStatus("mandatory")
_ApItfStatTable_Object = MibTable
apItfStatTable = _ApItfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    apItfStatTable.setStatus("mandatory")
_ApItfStatEntry_Object = MibTableRow
apItfStatEntry = _ApItfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 2, 1)
)
apItfStatEntry.setIndexNames(
    (0, "SYMBOL-ENTERPRISE-PRIVATE-MIB", "apItfStatIndex"),
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 2, 1, 2),
    _ApInterfaceName_Type()
)
apInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInterfaceName.setStatus("mandatory")
_ApPacketsIns_Type = Counter32
_ApPacketsIns_Object = MibTableColumn
apPacketsIns = _ApPacketsIns_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 2, 1, 3),
    _ApPacketsIns_Type()
)
apPacketsIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPacketsIns.setStatus("mandatory")
_ApPacketsOuts_Type = Counter32
_ApPacketsOuts_Object = MibTableColumn
apPacketsOuts = _ApPacketsOuts_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 2, 1, 4),
    _ApPacketsOuts_Type()
)
apPacketsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPacketsOuts.setStatus("mandatory")
_ApOctetsIns_Type = Counter32
_ApOctetsIns_Object = MibTableColumn
apOctetsIns = _ApOctetsIns_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 2, 1, 5),
    _ApOctetsIns_Type()
)
apOctetsIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOctetsIns.setStatus("mandatory")
_ApOctetsOuts_Type = Counter32
_ApOctetsOuts_Object = MibTableColumn
apOctetsOuts = _ApOctetsOuts_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 2, 1, 6),
    _ApOctetsOuts_Type()
)
apOctetsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOctetsOuts.setStatus("mandatory")
_ApPktsInPerSec_Type = Gauge32
_ApPktsInPerSec_Object = MibTableColumn
apPktsInPerSec = _ApPktsInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 2, 1, 7),
    _ApPktsInPerSec_Type()
)
apPktsInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPktsInPerSec.setStatus("mandatory")
_ApPktsOutPerSec_Type = Gauge32
_ApPktsOutPerSec_Object = MibTableColumn
apPktsOutPerSec = _ApPktsOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 2, 1, 8),
    _ApPktsOutPerSec_Type()
)
apPktsOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPktsOutPerSec.setStatus("mandatory")
_ApOctInPerSec_Type = Gauge32
_ApOctInPerSec_Object = MibTableColumn
apOctInPerSec = _ApOctInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 2, 1, 9),
    _ApOctInPerSec_Type()
)
apOctInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOctInPerSec.setStatus("mandatory")
_ApOctOutPerSec_Type = Gauge32
_ApOctOutPerSec_Object = MibTableColumn
apOctOutPerSec = _ApOctOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 2, 1, 10),
    _ApOctOutPerSec_Type()
)
apOctOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOctOutPerSec.setStatus("mandatory")
_ApEthernetStatistics_ObjectIdentity = ObjectIdentity
apEthernetStatistics = _ApEthernetStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 3)
)
_ApEPktsSeens_Type = Counter32
_ApEPktsSeens_Object = MibScalar
apEPktsSeens = _ApEPktsSeens_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 3, 1),
    _ApEPktsSeens_Type()
)
apEPktsSeens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEPktsSeens.setStatus("mandatory")
_ApEPktsForwardeds_Type = Counter32
_ApEPktsForwardeds_Object = MibScalar
apEPktsForwardeds = _ApEPktsForwardeds_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 3, 2),
    _ApEPktsForwardeds_Type()
)
apEPktsForwardeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEPktsForwardeds.setStatus("mandatory")
_ApEPktsDiscNoMatchs_Type = Counter32
_ApEPktsDiscNoMatchs_Object = MibScalar
apEPktsDiscNoMatchs = _ApEPktsDiscNoMatchs_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 3, 3),
    _ApEPktsDiscNoMatchs_Type()
)
apEPktsDiscNoMatchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEPktsDiscNoMatchs.setStatus("mandatory")
_ApEPktsDiscForceds_Type = Counter32
_ApEPktsDiscForceds_Object = MibScalar
apEPktsDiscForceds = _ApEPktsDiscForceds_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 3, 4),
    _ApEPktsDiscForceds_Type()
)
apEPktsDiscForceds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEPktsDiscForceds.setStatus("mandatory")
_ApEPktsDiscBuffers_Type = Counter32
_ApEPktsDiscBuffers_Object = MibScalar
apEPktsDiscBuffers = _ApEPktsDiscBuffers_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 3, 5),
    _ApEPktsDiscBuffers_Type()
)
apEPktsDiscBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEPktsDiscBuffers.setStatus("mandatory")
_ApEPktsDiscCRCs_Type = Counter32
_ApEPktsDiscCRCs_Object = MibScalar
apEPktsDiscCRCs = _ApEPktsDiscCRCs_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 3, 6),
    _ApEPktsDiscCRCs_Type()
)
apEPktsDiscCRCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEPktsDiscCRCs.setStatus("mandatory")
_ApEPktsSents_Type = Counter32
_ApEPktsSents_Object = MibScalar
apEPktsSents = _ApEPktsSents_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 3, 7),
    _ApEPktsSents_Type()
)
apEPktsSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEPktsSents.setStatus("mandatory")
_ApEAnyCollisions_Type = Counter32
_ApEAnyCollisions_Object = MibScalar
apEAnyCollisions = _ApEAnyCollisions_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 3, 8),
    _ApEAnyCollisions_Type()
)
apEAnyCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEAnyCollisions.setStatus("mandatory")
_ApE1orMoreColls_Type = Counter32
_ApE1orMoreColls_Object = MibScalar
apE1orMoreColls = _ApE1orMoreColls_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 3, 9),
    _ApE1orMoreColls_Type()
)
apE1orMoreColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apE1orMoreColls.setStatus("mandatory")
_ApEMaxCollisions_Type = Counter32
_ApEMaxCollisions_Object = MibScalar
apEMaxCollisions = _ApEMaxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 3, 10),
    _ApEMaxCollisions_Type()
)
apEMaxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEMaxCollisions.setStatus("mandatory")
_ApELateCollisions_Type = Counter32
_ApELateCollisions_Object = MibScalar
apELateCollisions = _ApELateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 3, 11),
    _ApELateCollisions_Type()
)
apELateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apELateCollisions.setStatus("mandatory")
_ApEPktsDefers_Type = Counter32
_ApEPktsDefers_Object = MibScalar
apEPktsDefers = _ApEPktsDefers_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 3, 12),
    _ApEPktsDefers_Type()
)
apEPktsDefers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEPktsDefers.setStatus("mandatory")
_ApRFStatistics_ObjectIdentity = ObjectIdentity
apRFStatistics = _ApRFStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 4)
)
_RfBcMcPktsSents_Type = Counter32
_RfBcMcPktsSents_Object = MibScalar
rfBcMcPktsSents = _RfBcMcPktsSents_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 4, 1),
    _RfBcMcPktsSents_Type()
)
rfBcMcPktsSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfBcMcPktsSents.setStatus("mandatory")
_RfBcMcPktsRcvds_Type = Counter32
_RfBcMcPktsRcvds_Object = MibScalar
rfBcMcPktsRcvds = _RfBcMcPktsRcvds_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 4, 2),
    _RfBcMcPktsRcvds_Type()
)
rfBcMcPktsRcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfBcMcPktsRcvds.setStatus("mandatory")
_RfBcMcOctSents_Type = Counter32
_RfBcMcOctSents_Object = MibScalar
rfBcMcOctSents = _RfBcMcOctSents_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 4, 3),
    _RfBcMcOctSents_Type()
)
rfBcMcOctSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfBcMcOctSents.setStatus("mandatory")
_RfBcMcOctRcvds_Type = Counter32
_RfBcMcOctRcvds_Object = MibScalar
rfBcMcOctRcvds = _RfBcMcOctRcvds_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 4, 4),
    _RfBcMcOctRcvds_Type()
)
rfBcMcOctRcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfBcMcOctRcvds.setStatus("mandatory")
_RfSysPktsSents_Type = Counter32
_RfSysPktsSents_Object = MibScalar
rfSysPktsSents = _RfSysPktsSents_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 4, 5),
    _RfSysPktsSents_Type()
)
rfSysPktsSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfSysPktsSents.setStatus("mandatory")
_RfSysPktsRcvds_Type = Counter32
_RfSysPktsRcvds_Object = MibScalar
rfSysPktsRcvds = _RfSysPktsRcvds_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 4, 6),
    _RfSysPktsRcvds_Type()
)
rfSysPktsRcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfSysPktsRcvds.setStatus("mandatory")
_RfSBcMcPktsSents_Type = Counter32
_RfSBcMcPktsSents_Object = MibScalar
rfSBcMcPktsSents = _RfSBcMcPktsSents_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 4, 7),
    _RfSBcMcPktsSents_Type()
)
rfSBcMcPktsSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfSBcMcPktsSents.setStatus("mandatory")
_RfSBcMcPktsRcvds_Type = Counter32
_RfSBcMcPktsRcvds_Object = MibScalar
rfSBcMcPktsRcvds = _RfSBcMcPktsRcvds_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 4, 8),
    _RfSBcMcPktsRcvds_Type()
)
rfSBcMcPktsRcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfSBcMcPktsRcvds.setStatus("mandatory")
_RfSuccFragPkts_Type = Counter32
_RfSuccFragPkts_Object = MibScalar
rfSuccFragPkts = _RfSuccFragPkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 4, 9),
    _RfSuccFragPkts_Type()
)
rfSuccFragPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfSuccFragPkts.setStatus("mandatory")
_RfUnsuccFragPkts_Type = Counter32
_RfUnsuccFragPkts_Object = MibScalar
rfUnsuccFragPkts = _RfUnsuccFragPkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 4, 10),
    _RfUnsuccFragPkts_Type()
)
rfUnsuccFragPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfUnsuccFragPkts.setStatus("mandatory")
_RfTotalFragSents_Type = Counter32
_RfTotalFragSents_Object = MibScalar
rfTotalFragSents = _RfTotalFragSents_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 4, 11),
    _RfTotalFragSents_Type()
)
rfTotalFragSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfTotalFragSents.setStatus("mandatory")
_RfTotalFragRcvds_Type = Counter32
_RfTotalFragRcvds_Object = MibScalar
rfTotalFragRcvds = _RfTotalFragRcvds_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 4, 12),
    _RfTotalFragRcvds_Type()
)
rfTotalFragRcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfTotalFragRcvds.setStatus("mandatory")
_RfSuccReassPkts_Type = Counter32
_RfSuccReassPkts_Object = MibScalar
rfSuccReassPkts = _RfSuccReassPkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 4, 13),
    _RfSuccReassPkts_Type()
)
rfSuccReassPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfSuccReassPkts.setStatus("mandatory")
_RfUnsuccReassPkts_Type = Counter32
_RfUnsuccReassPkts_Object = MibScalar
rfUnsuccReassPkts = _RfUnsuccReassPkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 4, 14),
    _RfUnsuccReassPkts_Type()
)
rfUnsuccReassPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfUnsuccReassPkts.setStatus("mandatory")
_RfAssocMUs_Type = Counter32
_RfAssocMUs_Object = MibScalar
rfAssocMUs = _RfAssocMUs_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 4, 15),
    _RfAssocMUs_Type()
)
rfAssocMUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfAssocMUs.setStatus("mandatory")
_RfRcvdCRCErrors_Type = Counter32
_RfRcvdCRCErrors_Object = MibScalar
rfRcvdCRCErrors = _RfRcvdCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 4, 16),
    _RfRcvdCRCErrors_Type()
)
rfRcvdCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfRcvdCRCErrors.setStatus("mandatory")
_RfRcvdDupPkts_Type = Counter32
_RfRcvdDupPkts_Object = MibScalar
rfRcvdDupPkts = _RfRcvdDupPkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 4, 17),
    _RfRcvdDupPkts_Type()
)
rfRcvdDupPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfRcvdDupPkts.setStatus("mandatory")
_RfTotalCollisions_Type = Counter32
_RfTotalCollisions_Object = MibScalar
rfTotalCollisions = _RfTotalCollisions_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 4, 18),
    _RfTotalCollisions_Type()
)
rfTotalCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfTotalCollisions.setStatus("mandatory")
_RfPktsWithoutColls_Type = Counter32
_RfPktsWithoutColls_Object = MibScalar
rfPktsWithoutColls = _RfPktsWithoutColls_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 4, 19),
    _RfPktsWithoutColls_Type()
)
rfPktsWithoutColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfPktsWithoutColls.setStatus("mandatory")
_RfPktsWithMaxColls_Type = Counter32
_RfPktsWithMaxColls_Object = MibScalar
rfPktsWithMaxColls = _RfPktsWithMaxColls_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 4, 20),
    _RfPktsWithMaxColls_Type()
)
rfPktsWithMaxColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfPktsWithMaxColls.setStatus("mandatory")
_RfPktsWithColls_Type = Counter32
_RfPktsWithColls_Object = MibScalar
rfPktsWithColls = _RfPktsWithColls_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 4, 21),
    _RfPktsWithColls_Type()
)
rfPktsWithColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfPktsWithColls.setStatus("mandatory")
_ApPerFreqStatTable_Object = MibTable
apPerFreqStatTable = _ApPerFreqStatTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    apPerFreqStatTable.setStatus("mandatory")
_ApPerFreqStatEntry_Object = MibTableRow
apPerFreqStatEntry = _ApPerFreqStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 5, 1)
)
apPerFreqStatEntry.setIndexNames(
    (0, "SYMBOL-ENTERPRISE-PRIVATE-MIB", "rfPerFqChannel"),
)
if mibBuilder.loadTexts:
    apPerFreqStatEntry.setStatus("mandatory")


class _RfPerFqChannel_Type(Integer32):
    """Custom type rfPerFqChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 79),
    )


_RfPerFqChannel_Type.__name__ = "Integer32"
_RfPerFqChannel_Object = MibTableColumn
rfPerFqChannel = _RfPerFqChannel_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 5, 1, 1),
    _RfPerFqChannel_Type()
)
rfPerFqChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfPerFqChannel.setStatus("mandatory")
_RfPerFqPktsSents_Type = Counter32
_RfPerFqPktsSents_Object = MibTableColumn
rfPerFqPktsSents = _RfPerFqPktsSents_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 5, 1, 2),
    _RfPerFqPktsSents_Type()
)
rfPerFqPktsSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfPerFqPktsSents.setStatus("mandatory")
_RfPerFqPktsRcvds_Type = Counter32
_RfPerFqPktsRcvds_Object = MibTableColumn
rfPerFqPktsRcvds = _RfPerFqPktsRcvds_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 5, 1, 3),
    _RfPerFqPktsRcvds_Type()
)
rfPerFqPktsRcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfPerFqPktsRcvds.setStatus("mandatory")
_RfPerFqRetries_Type = Counter32
_RfPerFqRetries_Object = MibTableColumn
rfPerFqRetries = _RfPerFqRetries_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 5, 1, 4),
    _RfPerFqRetries_Type()
)
rfPerFqRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfPerFqRetries.setStatus("mandatory")
_ApSerialPortStatistics_ObjectIdentity = ObjectIdentity
apSerialPortStatistics = _ApSerialPortStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 6)
)
_ApNbrOfDialouts_Type = Counter32
_ApNbrOfDialouts_Object = MibScalar
apNbrOfDialouts = _ApNbrOfDialouts_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 6, 1),
    _ApNbrOfDialouts_Type()
)
apNbrOfDialouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNbrOfDialouts.setStatus("mandatory")
_ApDialoutFailures_Type = Counter32
_ApDialoutFailures_Object = MibScalar
apDialoutFailures = _ApDialoutFailures_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 6, 2),
    _ApDialoutFailures_Type()
)
apDialoutFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDialoutFailures.setStatus("mandatory")
_ApNbrOfAnswers_Type = Counter32
_ApNbrOfAnswers_Object = MibScalar
apNbrOfAnswers = _ApNbrOfAnswers_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 6, 3),
    _ApNbrOfAnswers_Type()
)
apNbrOfAnswers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNbrOfAnswers.setStatus("mandatory")
_ApCurrCallTime_Type = TimeTicks
_ApCurrCallTime_Object = MibScalar
apCurrCallTime = _ApCurrCallTime_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 6, 4),
    _ApCurrCallTime_Type()
)
apCurrCallTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCurrCallTime.setStatus("mandatory")
_ApLastCallTime_Type = TimeTicks
_ApLastCallTime_Object = MibScalar
apLastCallTime = _ApLastCallTime_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 6, 5),
    _ApLastCallTime_Type()
)
apLastCallTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLastCallTime.setStatus("mandatory")
_ApWNMPStatistics_ObjectIdentity = ObjectIdentity
apWNMPStatistics = _ApWNMPStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 7)
)
_ApWNMPCfgPkts_Type = Counter32
_ApWNMPCfgPkts_Object = MibScalar
apWNMPCfgPkts = _ApWNMPCfgPkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 7, 1),
    _ApWNMPCfgPkts_Type()
)
apWNMPCfgPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWNMPCfgPkts.setStatus("mandatory")
_WEchoRequests_Type = Counter32
_WEchoRequests_Object = MibScalar
wEchoRequests = _WEchoRequests_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 7, 2),
    _WEchoRequests_Type()
)
wEchoRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEchoRequests.setStatus("mandatory")
_WPingRequests_Type = Counter32
_WPingRequests_Object = MibScalar
wPingRequests = _WPingRequests_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 7, 3),
    _WPingRequests_Type()
)
wPingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wPingRequests.setStatus("mandatory")
_WPktsFromNVs_Type = Counter32
_WPktsFromNVs_Object = MibScalar
wPktsFromNVs = _WPktsFromNVs_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 7, 4),
    _WPktsFromNVs_Type()
)
wPktsFromNVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wPktsFromNVs.setStatus("mandatory")
_WPPktsToNVs_Type = Counter32
_WPPktsToNVs_Object = MibScalar
wPPktsToNVs = _WPPktsToNVs_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 7, 5),
    _WPPktsToNVs_Type()
)
wPPktsToNVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wPPktsToNVs.setStatus("mandatory")
_WPassThruEchoes_Type = Counter32
_WPassThruEchoes_Object = MibScalar
wPassThruEchoes = _WPassThruEchoes_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 7, 6),
    _WPassThruEchoes_Type()
)
wPassThruEchoes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wPassThruEchoes.setStatus("mandatory")
_ApMUInfo_ObjectIdentity = ObjectIdentity
apMUInfo = _ApMUInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 8)
)
_ApCurrentMUs_Type = Counter32
_ApCurrentMUs_Object = MibScalar
apCurrentMUs = _ApCurrentMUs_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 8, 1),
    _ApCurrentMUs_Type()
)
apCurrentMUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCurrentMUs.setStatus("mandatory")
_ApMaxMUs_Type = Counter32
_ApMaxMUs_Object = MibScalar
apMaxMUs = _ApMaxMUs_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 8, 2),
    _ApMaxMUs_Type()
)
apMaxMUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMaxMUs.setStatus("mandatory")
_ApTotalAssocs_Type = Counter32
_ApTotalAssocs_Object = MibScalar
apTotalAssocs = _ApTotalAssocs_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 8, 3),
    _ApTotalAssocs_Type()
)
apTotalAssocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTotalAssocs.setStatus("mandatory")
_ApMUTable_Object = MibTable
apMUTable = _ApMUTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 8, 4)
)
if mibBuilder.loadTexts:
    apMUTable.setStatus("mandatory")
_ApMUEntry_Object = MibTableRow
apMUEntry = _ApMUEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 8, 4, 1)
)
apMUEntry.setIndexNames(
    (0, "SYMBOL-ENTERPRISE-PRIVATE-MIB", "muIndex"),
)
if mibBuilder.loadTexts:
    apMUEntry.setStatus("mandatory")


class _MuIndex_Type(Integer32):
    """Custom type muIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_MuIndex_Type.__name__ = "Integer32"
_MuIndex_Object = MibTableColumn
muIndex = _MuIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 8, 4, 1, 1),
    _MuIndex_Type()
)
muIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muIndex.setStatus("mandatory")
_MuMacAddr_Type = PhysAddress
_MuMacAddr_Object = MibTableColumn
muMacAddr = _MuMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 8, 4, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 8, 4, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 8, 4, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 8, 4, 1, 5),
    _MuPowerMode_Type()
)
muPowerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muPowerMode.setStatus("mandatory")
_MuStationID_Type = Integer32
_MuStationID_Object = MibTableColumn
muStationID = _MuStationID_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 8, 4, 1, 6),
    _MuStationID_Type()
)
muStationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muStationID.setStatus("mandatory")
_MuLastAPAddr_Type = PhysAddress
_MuLastAPAddr_Object = MibTableColumn
muLastAPAddr = _MuLastAPAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 8, 4, 1, 7),
    _MuLastAPAddr_Type()
)
muLastAPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muLastAPAddr.setStatus("mandatory")
_MuTotalAssoc_Type = Integer32
_MuTotalAssoc_Object = MibTableColumn
muTotalAssoc = _MuTotalAssoc_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 8, 4, 1, 8),
    _MuTotalAssoc_Type()
)
muTotalAssoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muTotalAssoc.setStatus("mandatory")
_MuAssocStart_Type = TimeTicks
_MuAssocStart_Object = MibTableColumn
muAssocStart = _MuAssocStart_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 8, 4, 1, 9),
    _MuAssocStart_Type()
)
muAssocStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muAssocStart.setStatus("mandatory")
_MuLstAssStrt_Type = TimeTicks
_MuLstAssStrt_Object = MibTableColumn
muLstAssStrt = _MuLstAssStrt_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 8, 4, 1, 10),
    _MuLstAssStrt_Type()
)
muLstAssStrt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muLstAssStrt.setStatus("mandatory")
_MuLastAssEnd_Type = TimeTicks
_MuLastAssEnd_Object = MibTableColumn
muLastAssEnd = _MuLastAssEnd_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 8, 4, 1, 11),
    _MuLastAssEnd_Type()
)
muLastAssEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muLastAssEnd.setStatus("mandatory")
_MuNPktsSents_Type = Counter32
_MuNPktsSents_Object = MibTableColumn
muNPktsSents = _MuNPktsSents_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 8, 4, 1, 12),
    _MuNPktsSents_Type()
)
muNPktsSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muNPktsSents.setStatus("mandatory")
_MuNPktsRcvds_Type = Counter32
_MuNPktsRcvds_Object = MibTableColumn
muNPktsRcvds = _MuNPktsRcvds_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 8, 4, 1, 13),
    _MuNPktsRcvds_Type()
)
muNPktsRcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muNPktsRcvds.setStatus("mandatory")
_MuNBytesSents_Type = Counter32
_MuNBytesSents_Object = MibTableColumn
muNBytesSents = _MuNBytesSents_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 8, 4, 1, 14),
    _MuNBytesSents_Type()
)
muNBytesSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muNBytesSents.setStatus("mandatory")
_MuNBytesRcvds_Type = Counter32
_MuNBytesRcvds_Object = MibTableColumn
muNBytesRcvds = _MuNBytesRcvds_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 8, 4, 1, 15),
    _MuNBytesRcvds_Type()
)
muNBytesRcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muNBytesRcvds.setStatus("mandatory")
_MuNDiscdPkts_Type = Counter32
_MuNDiscdPkts_Object = MibTableColumn
muNDiscdPkts = _MuNDiscdPkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 8, 4, 1, 16),
    _MuNDiscdPkts_Type()
)
muNDiscdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muNDiscdPkts.setStatus("mandatory")
_MuTmLastData_Type = TimeTicks
_MuTmLastData_Object = MibTableColumn
muTmLastData = _MuTmLastData_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 8, 4, 1, 17),
    _MuTmLastData_Type()
)
muTmLastData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muTmLastData.setStatus("mandatory")
_ApKnownAPsTable_Object = MibTable
apKnownAPsTable = _ApKnownAPsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 9)
)
if mibBuilder.loadTexts:
    apKnownAPsTable.setStatus("mandatory")
_ApKnownAPsEntry_Object = MibTableRow
apKnownAPsEntry = _ApKnownAPsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 9, 1)
)
apKnownAPsEntry.setIndexNames(
    (0, "SYMBOL-ENTERPRISE-PRIVATE-MIB", "apAPMacAddr"),
)
if mibBuilder.loadTexts:
    apKnownAPsEntry.setStatus("mandatory")
_ApAPMacAddr_Type = PhysAddress
_ApAPMacAddr_Object = MibTableColumn
apAPMacAddr = _ApAPMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 9, 1, 1),
    _ApAPMacAddr_Type()
)
apAPMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAPMacAddr.setStatus("mandatory")
_ApAPIpAddr_Type = IpAddress
_ApAPIpAddr_Object = MibTableColumn
apAPIpAddr = _ApAPIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 9, 1, 2),
    _ApAPIpAddr_Type()
)
apAPIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAPIpAddr.setStatus("mandatory")


class _ApNetID_Type(OctetString):
    """Custom type apNetID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_ApNetID_Type.__name__ = "OctetString"
_ApNetID_Object = MibTableColumn
apNetID = _ApNetID_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 9, 1, 3),
    _ApNetID_Type()
)
apNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNetID.setStatus("mandatory")


class _ApAPID_Type(OctetString):
    """Custom type apAPID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_ApAPID_Type.__name__ = "OctetString"
_ApAPID_Object = MibTableColumn
apAPID = _ApAPID_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 9, 1, 4),
    _ApAPID_Type()
)
apAPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAPID.setStatus("mandatory")
_ApHoppingSeq_Type = Integer32
_ApHoppingSeq_Object = MibTableColumn
apHoppingSeq = _ApHoppingSeq_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 9, 1, 5),
    _ApHoppingSeq_Type()
)
apHoppingSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apHoppingSeq.setStatus("mandatory")
_ApMUs_Type = Integer32
_ApMUs_Object = MibTableColumn
apMUs = _ApMUs_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 9, 1, 6),
    _ApMUs_Type()
)
apMUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMUs.setStatus("mandatory")
_ApKBOS_Type = Integer32
_ApKBOS_Object = MibTableColumn
apKBOS = _ApKBOS_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 9, 1, 7),
    _ApKBOS_Type()
)
apKBOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apKBOS.setStatus("mandatory")
_ApKBIS_Type = Integer32
_ApKBIS_Object = MibTableColumn
apKBIS = _ApKBIS_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 9, 1, 8),
    _ApKBIS_Type()
)
apKBIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apKBIS.setStatus("mandatory")
_ApLastRcvd_Type = TimeTicks
_ApLastRcvd_Object = MibTableColumn
apLastRcvd = _ApLastRcvd_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 9, 1, 9),
    _ApLastRcvd_Type()
)
apLastRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLastRcvd.setStatus("mandatory")
_ApFilterStatistics_ObjectIdentity = ObjectIdentity
apFilterStatistics = _ApFilterStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 10)
)
_ApAdrViolations_Type = Counter32
_ApAdrViolations_Object = MibScalar
apAdrViolations = _ApAdrViolations_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 10, 1),
    _ApAdrViolations_Type()
)
apAdrViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAdrViolations.setStatus("mandatory")
_ApTypeViolations_Type = Counter32
_ApTypeViolations_Object = MibScalar
apTypeViolations = _ApTypeViolations_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 10, 2),
    _ApTypeViolations_Type()
)
apTypeViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTypeViolations.setStatus("mandatory")
_ApWLAPInfo_ObjectIdentity = ObjectIdentity
apWLAPInfo = _ApWLAPInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 11)
)
_ApNbrOfWLAPItfs_Type = Counter32
_ApNbrOfWLAPItfs_Object = MibScalar
apNbrOfWLAPItfs = _ApNbrOfWLAPItfs_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 11, 1),
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 14),
          ("functional", 15),
          ("initializing", 1),
          ("received-root-rsp", 10),
          ("root-wlap-lost", 12),
          ("send-Probe-rsp", 6),
          ("send-assoc-req", 3),
          ("send-assoc-rsp", 7),
          ("send-cfg-bpdu", 4),
          ("send-cfg-rsp", 8),
          ("sending-probe", 2),
          ("wait-for-probe", 5))
    )


_ApWLAPState_Type.__name__ = "Integer32"
_ApWLAPState_Object = MibScalar
apWLAPState = _ApWLAPState_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 11, 2),
    _ApWLAPState_Type()
)
apWLAPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWLAPState.setStatus("mandatory")
_ApWLAPHopSequence_Type = Integer32
_ApWLAPHopSequence_Object = MibScalar
apWLAPHopSequence = _ApWLAPHopSequence_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 11, 3),
    _ApWLAPHopSequence_Type()
)
apWLAPHopSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWLAPHopSequence.setStatus("mandatory")
_ApRootInterface_Type = Integer32
_ApRootInterface_Object = MibScalar
apRootInterface = _ApRootInterface_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 11, 4),
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 11, 5),
    _ApRootWLAPID_Type()
)
apRootWLAPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRootWLAPID.setStatus("mandatory")
_ApRootPathCost_Type = Integer32
_ApRootPathCost_Object = MibScalar
apRootPathCost = _ApRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 11, 6),
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 11, 7),
    _ApWLAPID_Type()
)
apWLAPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWLAPID.setStatus("mandatory")
_ApWLAPItfTable_Object = MibTable
apWLAPItfTable = _ApWLAPItfTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 11, 8)
)
if mibBuilder.loadTexts:
    apWLAPItfTable.setStatus("mandatory")
_ApWLAPItfEntry_Object = MibTableRow
apWLAPItfEntry = _ApWLAPItfEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 11, 8, 1)
)
apWLAPItfEntry.setIndexNames(
    (0, "SYMBOL-ENTERPRISE-PRIVATE-MIB", "apWLAPItfID"),
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 11, 8, 1, 1),
    _ApWLAPItfID_Type()
)
apWLAPItfID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWLAPItfID.setStatus("mandatory")
_ApWLAPItfAddr_Type = PhysAddress
_ApWLAPItfAddr_Object = MibTableColumn
apWLAPItfAddr = _ApWLAPItfAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 11, 8, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 11, 8, 1, 3),
    _ApWLAPItfState_Type()
)
apWLAPItfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWLAPItfState.setStatus("mandatory")
_ApWLAPPathCost_Type = Integer32
_ApWLAPPathCost_Object = MibTableColumn
apWLAPPathCost = _ApWLAPPathCost_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 11, 8, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 11, 8, 1, 5),
    _ApDsgnatedRoot_Type()
)
apDsgnatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDsgnatedRoot.setStatus("mandatory")
_ApDsgnatedCost_Type = Integer32
_ApDsgnatedCost_Object = MibTableColumn
apDsgnatedCost = _ApDsgnatedCost_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 11, 8, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 11, 8, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 2, 11, 8, 1, 8),
    _ApDsgnatedItf_Type()
)
apDsgnatedItf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDsgnatedItf.setStatus("mandatory")
_ApFaultMgmt_ObjectIdentity = ObjectIdentity
apFaultMgmt = _ApFaultMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 3)
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 3, 1),
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 3, 2),
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 3, 3),
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 3, 4),
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 3, 5),
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 3, 6),
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 3, 7),
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 3, 8),
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 3, 9),
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 3, 10),
    _ApDnLdFileName_Type()
)
apDnLdFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apDnLdFileName.setStatus("mandatory")
_ApTFTPServer_Type = IpAddress
_ApTFTPServer_Object = MibScalar
apTFTPServer = _ApTFTPServer_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 3, 11),
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 3, 12),
    _ApResetAP_Type()
)
apResetAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apResetAP.setStatus("mandatory")
_ApSecurityMgmt_ObjectIdentity = ObjectIdentity
apSecurityMgmt = _ApSecurityMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 4)
)
_ApACLViolations_Type = Counter32
_ApACLViolations_Object = MibScalar
apACLViolations = _ApACLViolations_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 4, 1),
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 4, 2),
    _ApSaveConfig_Type()
)
apSaveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSaveConfig.setStatus("mandatory")
_ApAccCtrlTable_Object = MibTable
apAccCtrlTable = _ApAccCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 4, 3)
)
if mibBuilder.loadTexts:
    apAccCtrlTable.setStatus("mandatory")
_ApAccCtrlEntry_Object = MibTableRow
apAccCtrlEntry = _ApAccCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 4, 3, 1)
)
apAccCtrlEntry.setIndexNames(
    (0, "SYMBOL-ENTERPRISE-PRIVATE-MIB", "allowedIndex"),
)
if mibBuilder.loadTexts:
    apAccCtrlEntry.setStatus("mandatory")


class _AllowedIndex_Type(Integer32):
    """Custom type allowedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_AllowedIndex_Type.__name__ = "Integer32"
_AllowedIndex_Object = MibTableColumn
allowedIndex = _AllowedIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 4, 3, 1, 1),
    _AllowedIndex_Type()
)
allowedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    allowedIndex.setStatus("mandatory")
_AllowedMU_Type = PhysAddress
_AllowedMU_Object = MibTableColumn
allowedMU = _AllowedMU_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 4, 3, 1, 2),
    _AllowedMU_Type()
)
allowedMU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    allowedMU.setStatus("mandatory")
_ApACLRangeTable_Object = MibTable
apACLRangeTable = _ApACLRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 4, 4)
)
if mibBuilder.loadTexts:
    apACLRangeTable.setStatus("mandatory")
_ApACLRangeEntry_Object = MibTableRow
apACLRangeEntry = _ApACLRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 4, 4, 1)
)
apACLRangeEntry.setIndexNames(
    (0, "SYMBOL-ENTERPRISE-PRIVATE-MIB", "apACLRangeIndex"),
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
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 4, 4, 1, 1),
    _ApACLRangeIndex_Type()
)
apACLRangeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apACLRangeIndex.setStatus("mandatory")
_LowMacAddr_Type = PhysAddress
_LowMacAddr_Object = MibTableColumn
lowMacAddr = _LowMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 4, 4, 1, 2),
    _LowMacAddr_Type()
)
lowMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowMacAddr.setStatus("mandatory")
_HighMacAddr_Type = PhysAddress
_HighMacAddr_Object = MibTableColumn
highMacAddr = _HighMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 4, 4, 1, 3),
    _HighMacAddr_Type()
)
highMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highMacAddr.setStatus("mandatory")

# Managed Objects groups


# Notification objects

coldStart = NotificationType(
    (1, 3, 6, 1, 2, 1, 11, 0, 0)
)
coldStart.setObjects(
    ("SYMBOL-ENTERPRISE-PRIVATE-MIB", "apMyMacAddr")
)
if mibBuilder.loadTexts:
    coldStart.setStatus(
        ""
    )

authenticationFailure = NotificationType(
    (1, 3, 6, 1, 2, 1, 11, 0, 4)
)
authenticationFailure.setObjects(
      *(("SYMBOL-ENTERPRISE-PRIVATE-MIB", "apMyMacAddr"),
        ("SYMBOL-ENTERPRISE-PRIVATE-MIB", "apAPMacAddr"))
)
if mibBuilder.loadTexts:
    authenticationFailure.setStatus(
        ""
    )

apRFStartUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 0, 101)
)
apRFStartUpTrap.setObjects(
    ("SYMBOL-ENTERPRISE-PRIVATE-MIB", "apMyMacAddr")
)
if mibBuilder.loadTexts:
    apRFStartUpTrap.setStatus(
        ""
    )

apACLViolationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 0, 102)
)
apACLViolationTrap.setObjects(
      *(("SYMBOL-ENTERPRISE-PRIVATE-MIB", "apMyMacAddr"),
        ("SYMBOL-ENTERPRISE-PRIVATE-MIB", "muMacAddr"))
)
if mibBuilder.loadTexts:
    apACLViolationTrap.setStatus(
        ""
    )

apAPIdConflictTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 0, 103)
)
apAPIdConflictTrap.setObjects(
    ("SYMBOL-ENTERPRISE-PRIVATE-MIB", "apMyMacAddr")
)
if mibBuilder.loadTexts:
    apAPIdConflictTrap.setStatus(
        ""
    )

apMUAssocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 0, 111)
)
apMUAssocTrap.setObjects(
      *(("SYMBOL-ENTERPRISE-PRIVATE-MIB", "apMyMacAddr"),
        ("SYMBOL-ENTERPRISE-PRIVATE-MIB", "muMacAddr"),
        ("SYMBOL-ENTERPRISE-PRIVATE-MIB", "apCurrentMUs"))
)
if mibBuilder.loadTexts:
    apMUAssocTrap.setStatus(
        ""
    )

apMUUnAssocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 0, 112)
)
apMUUnAssocTrap.setObjects(
      *(("SYMBOL-ENTERPRISE-PRIVATE-MIB", "apMyMacAddr"),
        ("SYMBOL-ENTERPRISE-PRIVATE-MIB", "muMacAddr"),
        ("SYMBOL-ENTERPRISE-PRIVATE-MIB", "apCurrentMUs"))
)
if mibBuilder.loadTexts:
    apMUUnAssocTrap.setStatus(
        ""
    )

apMUToCAMTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 0, 113)
)
apMUToCAMTrap.setObjects(
      *(("SYMBOL-ENTERPRISE-PRIVATE-MIB", "apMyMacAddr"),
        ("SYMBOL-ENTERPRISE-PRIVATE-MIB", "muMacAddr"),
        ("SYMBOL-ENTERPRISE-PRIVATE-MIB", "apCurrentMUs"))
)
if mibBuilder.loadTexts:
    apMUToCAMTrap.setStatus(
        ""
    )

apMUToPSPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 0, 114)
)
apMUToPSPTrap.setObjects(
      *(("SYMBOL-ENTERPRISE-PRIVATE-MIB", "apMyMacAddr"),
        ("SYMBOL-ENTERPRISE-PRIVATE-MIB", "muMacAddr"),
        ("SYMBOL-ENTERPRISE-PRIVATE-MIB", "apCurrentMUs"))
)
if mibBuilder.loadTexts:
    apMUToPSPTrap.setStatus(
        ""
    )

apRootWLAPUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 0, 121)
)
apRootWLAPUpTrap.setObjects(
      *(("SYMBOL-ENTERPRISE-PRIVATE-MIB", "apMyMacAddr"),
        ("SYMBOL-ENTERPRISE-PRIVATE-MIB", "apAPMacAddr"),
        ("SYMBOL-ENTERPRISE-PRIVATE-MIB", "apNbrOfWLAPItfs"))
)
if mibBuilder.loadTexts:
    apRootWLAPUpTrap.setStatus(
        ""
    )

apRootWLAPLostTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 0, 122)
)
apRootWLAPLostTrap.setObjects(
      *(("SYMBOL-ENTERPRISE-PRIVATE-MIB", "apMyMacAddr"),
        ("SYMBOL-ENTERPRISE-PRIVATE-MIB", "apAPMacAddr"),
        ("SYMBOL-ENTERPRISE-PRIVATE-MIB", "apNbrOfWLAPItfs"))
)
if mibBuilder.loadTexts:
    apRootWLAPLostTrap.setStatus(
        ""
    )

apDsgntedWLAPUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 0, 123)
)
apDsgntedWLAPUpTrap.setObjects(
      *(("SYMBOL-ENTERPRISE-PRIVATE-MIB", "apMyMacAddr"),
        ("SYMBOL-ENTERPRISE-PRIVATE-MIB", "apAPMacAddr"),
        ("SYMBOL-ENTERPRISE-PRIVATE-MIB", "apNbrOfWLAPItfs"))
)
if mibBuilder.loadTexts:
    apDsgntedWLAPUpTrap.setStatus(
        ""
    )

apDsgnatedWLAPLostTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 1, 1, 0, 124)
)
apDsgnatedWLAPLostTrap.setObjects(
      *(("SYMBOL-ENTERPRISE-PRIVATE-MIB", "apMyMacAddr"),
        ("SYMBOL-ENTERPRISE-PRIVATE-MIB", "apAPMacAddr"),
        ("SYMBOL-ENTERPRISE-PRIVATE-MIB", "apNbrOfWLAPItfs"))
)
if mibBuilder.loadTexts:
    apDsgnatedWLAPLostTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYMBOL-ENTERPRISE-PRIVATE-MIB",
    **{"coldStart": coldStart,
       "authenticationFailure": authenticationFailure,
       "symbol": symbol,
       "spectrum24": spectrum24,
       "apProduct": apProduct,
       "apRFStartUpTrap": apRFStartUpTrap,
       "apACLViolationTrap": apACLViolationTrap,
       "apAPIdConflictTrap": apAPIdConflictTrap,
       "apMUAssocTrap": apMUAssocTrap,
       "apMUUnAssocTrap": apMUUnAssocTrap,
       "apMUToCAMTrap": apMUToCAMTrap,
       "apMUToPSPTrap": apMUToPSPTrap,
       "apRootWLAPUpTrap": apRootWLAPUpTrap,
       "apRootWLAPLostTrap": apRootWLAPLostTrap,
       "apDsgntedWLAPUpTrap": apDsgntedWLAPUpTrap,
       "apDsgnatedWLAPLostTrap": apDsgnatedWLAPLostTrap,
       "apConfigMgmt": apConfigMgmt,
       "apManufactureInfo": apManufactureInfo,
       "apModelnumber": apModelnumber,
       "apSerialnumber": apSerialnumber,
       "apHardwareRev": apHardwareRev,
       "apMyMacAddr": apMyMacAddr,
       "apAPFirmwareRev": apAPFirmwareRev,
       "apRFFirmwareRev": apRFFirmwareRev,
       "apSystemConfig": apSystemConfig,
       "apSystemName": apSystemName,
       "apMyIPAddr": apMyIPAddr,
       "apSubnetMask": apSubnetMask,
       "apGatewayIPAddr": apGatewayIPAddr,
       "apDefaultInterface": apDefaultInterface,
       "apEnetPortState": apEnetPortState,
       "apEthernetTimeOut": apEthernetTimeOut,
       "apTelnetEnable": apTelnetEnable,
       "apAccCtrlEnable": apAccCtrlEnable,
       "apTypeFilterEnable": apTypeFilterEnable,
       "apMUAutoCfgEnable": apMUAutoCfgEnable,
       "apAutoCfgEnable": apAutoCfgEnable,
       "apWNMPEnable": apWNMPEnable,
       "apAPStateXchgEnable": apAPStateXchgEnable,
       "apSNMPInfo": apSNMPInfo,
       "apSNMPMode": apSNMPMode,
       "apROCommunityName": apROCommunityName,
       "apRWCommunityName": apRWCommunityName,
       "apTrapRcvrIpAdr": apTrapRcvrIpAdr,
       "apAllTrapsEnable": apAllTrapsEnable,
       "apColdBootTrapEnable": apColdBootTrapEnable,
       "apAuthenFailureTrapEnable": apAuthenFailureTrapEnable,
       "apRFTrapEnable": apRFTrapEnable,
       "apACLTrapEnable": apACLTrapEnable,
       "apMUStateChngTrapEnable": apMUStateChngTrapEnable,
       "apAPIdConflictTrapEnable": apAPIdConflictTrapEnable,
       "apWLAPConnChngTrapEnable": apWLAPConnChngTrapEnable,
       "apRFConfig": apRFConfig,
       "apRFPortState": apRFPortState,
       "apNetId": apNetId,
       "apApId": apApId,
       "apHopSequence": apHopSequence,
       "apCountryName": apCountryName,
       "apHopSet": apHopSet,
       "apAntennaSelect": apAntennaSelect,
       "apDTIMInterval": apDTIMInterval,
       "apBCMCQMax": apBCMCQMax,
       "apReassemblyTimeOut": apReassemblyTimeOut,
       "apMaxRetries": apMaxRetries,
       "apMulticastMask": apMulticastMask,
       "apEncryptCoeff": apEncryptCoeff,
       "apEncryptPhase": apEncryptPhase,
       "apWLAPMode": apWLAPMode,
       "apWLAPPriority": apWLAPPriority,
       "apWLAPManualAPID": apWLAPManualAPID,
       "apWLAPEncryption": apWLAPEncryption,
       "apWLAPHelloTime": apWLAPHelloTime,
       "apWLAPMaxAge": apWLAPMaxAge,
       "apWLAPFwdDelay": apWLAPFwdDelay,
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
       "apPerFreqStatTable": apPerFreqStatTable,
       "apPerFreqStatEntry": apPerFreqStatEntry,
       "rfPerFqChannel": rfPerFqChannel,
       "rfPerFqPktsSents": rfPerFqPktsSents,
       "rfPerFqPktsRcvds": rfPerFqPktsRcvds,
       "rfPerFqRetries": rfPerFqRetries,
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
       "apKnownAPsTable": apKnownAPsTable,
       "apKnownAPsEntry": apKnownAPsEntry,
       "apAPMacAddr": apAPMacAddr,
       "apAPIpAddr": apAPIpAddr,
       "apNetID": apNetID,
       "apAPID": apAPID,
       "apHoppingSeq": apHoppingSeq,
       "apMUs": apMUs,
       "apKBOS": apKBOS,
       "apKBIS": apKBIS,
       "apLastRcvd": apLastRcvd,
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
       "highMacAddr": highMacAddr}
)
