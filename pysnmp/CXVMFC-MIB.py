# SNMP MIB module (CXVMFC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXVMFC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:59 2024
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

(cxMcVox,) = mibBuilder.importSymbols(
    "CXMCVOX-MIB",
    "cxMcVox")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CxVMFC_ObjectIdentity = ObjectIdentity
cxVMFC = _CxVMFC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 22)
)


class _VmfcOutRegCallerCategory_Type(Integer32):
    """Custom type vmfcOutRegCallerCategory based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("charge-meter", 4),
          ("data-tx", 6),
          ("maintenance-equipment", 3),
          ("operator", 5),
          ("subscriber-with-priority", 2),
          ("subscriber-without-priority", 1))
    )


_VmfcOutRegCallerCategory_Type.__name__ = "Integer32"
_VmfcOutRegCallerCategory_Object = MibScalar
vmfcOutRegCallerCategory = _VmfcOutRegCallerCategory_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 22, 1),
    _VmfcOutRegCallerCategory_Type()
)
vmfcOutRegCallerCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmfcOutRegCallerCategory.setStatus("mandatory")


class _VmfcOutRegCallerCatGrpII3_Type(Integer32):
    """Custom type vmfcOutRegCallerCatGrpII3 based on Integer32"""
    defaultValue = 1

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
        *(("atme-equipment", 2),
          ("maintenance-equipment", 3),
          ("normal-subscriber", 1),
          ("operator-with-intercept-capability", 5),
          ("operator-with-transfer-capability", 4))
    )


_VmfcOutRegCallerCatGrpII3_Type.__name__ = "Integer32"
_VmfcOutRegCallerCatGrpII3_Object = MibScalar
vmfcOutRegCallerCatGrpII3 = _VmfcOutRegCallerCatGrpII3_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 22, 2),
    _VmfcOutRegCallerCatGrpII3_Type()
)
vmfcOutRegCallerCatGrpII3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmfcOutRegCallerCatGrpII3.setStatus("mandatory")


class _VmfcOutRegCallerCatGrpII6_Type(Integer32):
    """Custom type vmfcOutRegCallerCatGrpII6 based on Integer32"""
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
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("atme-equipment", 2),
          ("collect-call", 4),
          ("maintenance-equipment", 3),
          ("normal-subscriber", 1),
          ("operator-without-transfer-capability", 9),
          ("subscriber1-on-shared-line", 6),
          ("subscriber2-on-shared-line", 7),
          ("subscriber3-on-shared-line", 8),
          ("time-and-charges", 5))
    )


_VmfcOutRegCallerCatGrpII6_Type.__name__ = "Integer32"
_VmfcOutRegCallerCatGrpII6_Object = MibScalar
vmfcOutRegCallerCatGrpII6 = _VmfcOutRegCallerCatGrpII6_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 22, 3),
    _VmfcOutRegCallerCatGrpII6_Type()
)
vmfcOutRegCallerCatGrpII6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmfcOutRegCallerCatGrpII6.setStatus("mandatory")


class _VmfcOutRegExchangeType_Type(Integer32):
    """Custom type vmfcOutRegExchangeType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("international-exchange", 2),
          ("national-exchange", 1))
    )


_VmfcOutRegExchangeType_Type.__name__ = "Integer32"
_VmfcOutRegExchangeType_Object = MibScalar
vmfcOutRegExchangeType = _VmfcOutRegExchangeType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 22, 4),
    _VmfcOutRegExchangeType_Type()
)
vmfcOutRegExchangeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmfcOutRegExchangeType.setStatus("mandatory")


class _VmfcOutRegCallingID_Type(DisplayString):
    """Custom type vmfcOutRegCallingID based on DisplayString"""
    defaultValue = OctetString("0")


_VmfcOutRegCallingID_Object = MibScalar
vmfcOutRegCallingID = _VmfcOutRegCallingID_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 22, 5),
    _VmfcOutRegCallingID_Type()
)
vmfcOutRegCallingID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmfcOutRegCallingID.setStatus("mandatory")


class _VmfcInRegNationalAddressSize_Type(Integer32):
    """Custom type vmfcInRegNationalAddressSize based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_VmfcInRegNationalAddressSize_Type.__name__ = "Integer32"
_VmfcInRegNationalAddressSize_Object = MibScalar
vmfcInRegNationalAddressSize = _VmfcInRegNationalAddressSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 22, 6),
    _VmfcInRegNationalAddressSize_Type()
)
vmfcInRegNationalAddressSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmfcInRegNationalAddressSize.setStatus("mandatory")


class _VmfcInRegInfoRequest_Type(Integer32):
    """Custom type vmfcInRegInfoRequest based on Integer32"""
    defaultHexValue = 0


_VmfcInRegInfoRequest_Object = MibScalar
vmfcInRegInfoRequest = _VmfcInRegInfoRequest_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 22, 7),
    _VmfcInRegInfoRequest_Type()
)
vmfcInRegInfoRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmfcInRegInfoRequest.setStatus("mandatory")


class _VmfcInRegPulsePeriod_Type(Integer32):
    """Custom type vmfcInRegPulsePeriod based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VmfcInRegPulsePeriod_Type.__name__ = "Integer32"
_VmfcInRegPulsePeriod_Object = MibScalar
vmfcInRegPulsePeriod = _VmfcInRegPulsePeriod_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 22, 8),
    _VmfcInRegPulsePeriod_Type()
)
vmfcInRegPulsePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmfcInRegPulsePeriod.setStatus("mandatory")


class _VmfcCountry_Type(Integer32):
    """Custom type vmfcCountry based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("argentina", 6),
          ("china", 5),
          ("korea", 4),
          ("mexico", 1),
          ("nicaragua", 3),
          ("philippines", 2))
    )


_VmfcCountry_Type.__name__ = "Integer32"
_VmfcCountry_Object = MibScalar
vmfcCountry = _VmfcCountry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 22, 9),
    _VmfcCountry_Type()
)
vmfcCountry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmfcCountry.setStatus("mandatory")


class _VmfcTimeOutBackwardSignal_Type(Integer32):
    """Custom type vmfcTimeOutBackwardSignal based on Integer32"""
    defaultValue = 15000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VmfcTimeOutBackwardSignal_Type.__name__ = "Integer32"
_VmfcTimeOutBackwardSignal_Object = MibScalar
vmfcTimeOutBackwardSignal = _VmfcTimeOutBackwardSignal_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 22, 10),
    _VmfcTimeOutBackwardSignal_Type()
)
vmfcTimeOutBackwardSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmfcTimeOutBackwardSignal.setStatus("mandatory")


class _VmfcTimeOutForwardSignal_Type(Integer32):
    """Custom type vmfcTimeOutForwardSignal based on Integer32"""
    defaultValue = 24000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VmfcTimeOutForwardSignal_Type.__name__ = "Integer32"
_VmfcTimeOutForwardSignal_Object = MibScalar
vmfcTimeOutForwardSignal = _VmfcTimeOutForwardSignal_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 22, 11),
    _VmfcTimeOutForwardSignal_Type()
)
vmfcTimeOutForwardSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmfcTimeOutForwardSignal.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXVMFC-MIB",
    **{"cxVMFC": cxVMFC,
       "vmfcOutRegCallerCategory": vmfcOutRegCallerCategory,
       "vmfcOutRegCallerCatGrpII3": vmfcOutRegCallerCatGrpII3,
       "vmfcOutRegCallerCatGrpII6": vmfcOutRegCallerCatGrpII6,
       "vmfcOutRegExchangeType": vmfcOutRegExchangeType,
       "vmfcOutRegCallingID": vmfcOutRegCallingID,
       "vmfcInRegNationalAddressSize": vmfcInRegNationalAddressSize,
       "vmfcInRegInfoRequest": vmfcInRegInfoRequest,
       "vmfcInRegPulsePeriod": vmfcInRegPulsePeriod,
       "vmfcCountry": vmfcCountry,
       "vmfcTimeOutBackwardSignal": vmfcTimeOutBackwardSignal,
       "vmfcTimeOutForwardSignal": vmfcTimeOutForwardSignal}
)
