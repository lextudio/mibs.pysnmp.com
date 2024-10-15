# SNMP MIB module (HW-IMAPV1NORTHBOUND-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HW-IMAPV1NORTHBOUND-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:48 2024
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

_Huawei_ObjectIdentity = ObjectIdentity
huawei = _Huawei_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2)
)
_HwNetManagement_ObjectIdentity = ObjectIdentity
hwNetManagement = _HwNetManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15)
)
_HwNmAgent_ObjectIdentity = ObjectIdentity
hwNmAgent = _HwNmAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1)
)
_HwNmFault_ObjectIdentity = ObjectIdentity
hwNmFault = _HwNmFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 3)
)


class _ThirdNMSFaultFilter_Type(OctetString):
    """Custom type thirdNMSFaultFilter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 32),
    )


_ThirdNMSFaultFilter_Type.__name__ = "OctetString"
_ThirdNMSFaultFilter_Object = MibScalar
thirdNMSFaultFilter = _ThirdNMSFaultFilter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 3, 5),
    _ThirdNMSFaultFilter_Type()
)
thirdNMSFaultFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thirdNMSFaultFilter.setStatus("mandatory")
_HwNmNorthboundEvent_ObjectIdentity = ObjectIdentity
hwNmNorthboundEvent = _HwNmNorthboundEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7)
)
_HwNmNorthboundEventInfo_ObjectIdentity = ObjectIdentity
hwNmNorthboundEventInfo = _HwNmNorthboundEventInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1)
)


class _HwNmNorthboundNEName_Type(OctetString):
    """Custom type hwNmNorthboundNEName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwNmNorthboundNEName_Type.__name__ = "OctetString"
_HwNmNorthboundNEName_Object = MibScalar
hwNmNorthboundNEName = _HwNmNorthboundNEName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 1),
    _HwNmNorthboundNEName_Type()
)
hwNmNorthboundNEName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNmNorthboundNEName.setStatus("mandatory")


class _HwNmNorthboundNEType_Type(OctetString):
    """Custom type hwNmNorthboundNEType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwNmNorthboundNEType_Type.__name__ = "OctetString"
_HwNmNorthboundNEType_Object = MibScalar
hwNmNorthboundNEType = _HwNmNorthboundNEType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 2),
    _HwNmNorthboundNEType_Type()
)
hwNmNorthboundNEType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNmNorthboundNEType.setStatus("mandatory")


class _HwNmNorthboundObjectInstance_Type(OctetString):
    """Custom type hwNmNorthboundObjectInstance based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwNmNorthboundObjectInstance_Type.__name__ = "OctetString"
_HwNmNorthboundObjectInstance_Object = MibScalar
hwNmNorthboundObjectInstance = _HwNmNorthboundObjectInstance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 3),
    _HwNmNorthboundObjectInstance_Type()
)
hwNmNorthboundObjectInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNmNorthboundObjectInstance.setStatus("mandatory")


class _HwNmNorthboundEventType_Type(OctetString):
    """Custom type hwNmNorthboundEventType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwNmNorthboundEventType_Type.__name__ = "OctetString"
_HwNmNorthboundEventType_Object = MibScalar
hwNmNorthboundEventType = _HwNmNorthboundEventType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 4),
    _HwNmNorthboundEventType_Type()
)
hwNmNorthboundEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNmNorthboundEventType.setStatus("mandatory")


class _HwNmNorthboundEventTime_Type(OctetString):
    """Custom type hwNmNorthboundEventTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwNmNorthboundEventTime_Type.__name__ = "OctetString"
_HwNmNorthboundEventTime_Object = MibScalar
hwNmNorthboundEventTime = _HwNmNorthboundEventTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 5),
    _HwNmNorthboundEventTime_Type()
)
hwNmNorthboundEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNmNorthboundEventTime.setStatus("mandatory")


class _HwNmNorthboundProbableCause_Type(OctetString):
    """Custom type hwNmNorthboundProbableCause based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwNmNorthboundProbableCause_Type.__name__ = "OctetString"
_HwNmNorthboundProbableCause_Object = MibScalar
hwNmNorthboundProbableCause = _HwNmNorthboundProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 6),
    _HwNmNorthboundProbableCause_Type()
)
hwNmNorthboundProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNmNorthboundProbableCause.setStatus("mandatory")


class _HwNmNorthboundSeverity_Type(OctetString):
    """Custom type hwNmNorthboundSeverity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwNmNorthboundSeverity_Type.__name__ = "OctetString"
_HwNmNorthboundSeverity_Object = MibScalar
hwNmNorthboundSeverity = _HwNmNorthboundSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 7),
    _HwNmNorthboundSeverity_Type()
)
hwNmNorthboundSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNmNorthboundSeverity.setStatus("mandatory")


class _HwNmNorthboundEventDetail_Type(OctetString):
    """Custom type hwNmNorthboundEventDetail based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwNmNorthboundEventDetail_Type.__name__ = "OctetString"
_HwNmNorthboundEventDetail_Object = MibScalar
hwNmNorthboundEventDetail = _HwNmNorthboundEventDetail_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 8),
    _HwNmNorthboundEventDetail_Type()
)
hwNmNorthboundEventDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNmNorthboundEventDetail.setStatus("mandatory")


class _HwNmNorthboundAdditionalInfo_Type(OctetString):
    """Custom type hwNmNorthboundAdditionalInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwNmNorthboundAdditionalInfo_Type.__name__ = "OctetString"
_HwNmNorthboundAdditionalInfo_Object = MibScalar
hwNmNorthboundAdditionalInfo = _HwNmNorthboundAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 9),
    _HwNmNorthboundAdditionalInfo_Type()
)
hwNmNorthboundAdditionalInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNmNorthboundAdditionalInfo.setStatus("mandatory")


class _HwNmNorthboundFaultFlag_Type(OctetString):
    """Custom type hwNmNorthboundFaultFlag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwNmNorthboundFaultFlag_Type.__name__ = "OctetString"
_HwNmNorthboundFaultFlag_Object = MibScalar
hwNmNorthboundFaultFlag = _HwNmNorthboundFaultFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 10),
    _HwNmNorthboundFaultFlag_Type()
)
hwNmNorthboundFaultFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNmNorthboundFaultFlag.setStatus("mandatory")


class _HwNmNorthboundFaultFunction_Type(OctetString):
    """Custom type hwNmNorthboundFaultFunction based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwNmNorthboundFaultFunction_Type.__name__ = "OctetString"
_HwNmNorthboundFaultFunction_Object = MibScalar
hwNmNorthboundFaultFunction = _HwNmNorthboundFaultFunction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 11),
    _HwNmNorthboundFaultFunction_Type()
)
hwNmNorthboundFaultFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNmNorthboundFaultFunction.setStatus("mandatory")
_HwNmNorthboundDeviceIP_Type = IpAddress
_HwNmNorthboundDeviceIP_Object = MibScalar
hwNmNorthboundDeviceIP = _HwNmNorthboundDeviceIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 12),
    _HwNmNorthboundDeviceIP_Type()
)
hwNmNorthboundDeviceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNmNorthboundDeviceIP.setStatus("mandatory")
_HwNmNorthboundSerialNo_Type = Integer32
_HwNmNorthboundSerialNo_Object = MibScalar
hwNmNorthboundSerialNo = _HwNmNorthboundSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 13),
    _HwNmNorthboundSerialNo_Type()
)
hwNmNorthboundSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNmNorthboundSerialNo.setStatus("mandatory")


class _HwNmNorthboundProbableRepair_Type(OctetString):
    """Custom type hwNmNorthboundProbableRepair based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwNmNorthboundProbableRepair_Type.__name__ = "OctetString"
_HwNmNorthboundProbableRepair_Object = MibScalar
hwNmNorthboundProbableRepair = _HwNmNorthboundProbableRepair_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 14),
    _HwNmNorthboundProbableRepair_Type()
)
hwNmNorthboundProbableRepair.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNmNorthboundProbableRepair.setStatus("mandatory")


class _HwNmNorthboundResourceIDs_Type(OctetString):
    """Custom type hwNmNorthboundResourceIDs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwNmNorthboundResourceIDs_Type.__name__ = "OctetString"
_HwNmNorthboundResourceIDs_Object = MibScalar
hwNmNorthboundResourceIDs = _HwNmNorthboundResourceIDs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 15),
    _HwNmNorthboundResourceIDs_Type()
)
hwNmNorthboundResourceIDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNmNorthboundResourceIDs.setStatus("mandatory")


class _HwNmNorthboundsAdditionalVB1_Type(OctetString):
    """Custom type hwNmNorthboundsAdditionalVB1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwNmNorthboundsAdditionalVB1_Type.__name__ = "OctetString"
_HwNmNorthboundsAdditionalVB1_Object = MibScalar
hwNmNorthboundsAdditionalVB1 = _HwNmNorthboundsAdditionalVB1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 16),
    _HwNmNorthboundsAdditionalVB1_Type()
)
hwNmNorthboundsAdditionalVB1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNmNorthboundsAdditionalVB1.setStatus("mandatory")


class _HwNmNorthboundsAdditionalVB2_Type(OctetString):
    """Custom type hwNmNorthboundsAdditionalVB2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwNmNorthboundsAdditionalVB2_Type.__name__ = "OctetString"
_HwNmNorthboundsAdditionalVB2_Object = MibScalar
hwNmNorthboundsAdditionalVB2 = _HwNmNorthboundsAdditionalVB2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 17),
    _HwNmNorthboundsAdditionalVB2_Type()
)
hwNmNorthboundsAdditionalVB2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNmNorthboundsAdditionalVB2.setStatus("mandatory")


class _HwNmNorthboundsAdditionalVB3_Type(OctetString):
    """Custom type hwNmNorthboundsAdditionalVB3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwNmNorthboundsAdditionalVB3_Type.__name__ = "OctetString"
_HwNmNorthboundsAdditionalVB3_Object = MibScalar
hwNmNorthboundsAdditionalVB3 = _HwNmNorthboundsAdditionalVB3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 18),
    _HwNmNorthboundsAdditionalVB3_Type()
)
hwNmNorthboundsAdditionalVB3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNmNorthboundsAdditionalVB3.setStatus("mandatory")


class _HwNmNorthboundsAdditionalVB4_Type(OctetString):
    """Custom type hwNmNorthboundsAdditionalVB4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwNmNorthboundsAdditionalVB4_Type.__name__ = "OctetString"
_HwNmNorthboundsAdditionalVB4_Object = MibScalar
hwNmNorthboundsAdditionalVB4 = _HwNmNorthboundsAdditionalVB4_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 19),
    _HwNmNorthboundsAdditionalVB4_Type()
)
hwNmNorthboundsAdditionalVB4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNmNorthboundsAdditionalVB4.setStatus("mandatory")


class _HwNmNorthboundsAdditionalVB5_Type(OctetString):
    """Custom type hwNmNorthboundsAdditionalVB5 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwNmNorthboundsAdditionalVB5_Type.__name__ = "OctetString"
_HwNmNorthboundsAdditionalVB5_Object = MibScalar
hwNmNorthboundsAdditionalVB5 = _HwNmNorthboundsAdditionalVB5_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 20),
    _HwNmNorthboundsAdditionalVB5_Type()
)
hwNmNorthboundsAdditionalVB5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNmNorthboundsAdditionalVB5.setStatus("mandatory")


class _HwNmNorthboundsAdditionalVB6_Type(OctetString):
    """Custom type hwNmNorthboundsAdditionalVB6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwNmNorthboundsAdditionalVB6_Type.__name__ = "OctetString"
_HwNmNorthboundsAdditionalVB6_Object = MibScalar
hwNmNorthboundsAdditionalVB6 = _HwNmNorthboundsAdditionalVB6_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 21),
    _HwNmNorthboundsAdditionalVB6_Type()
)
hwNmNorthboundsAdditionalVB6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNmNorthboundsAdditionalVB6.setStatus("mandatory")


class _HwNmNorthboundsAdditionalVB7_Type(OctetString):
    """Custom type hwNmNorthboundsAdditionalVB7 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwNmNorthboundsAdditionalVB7_Type.__name__ = "OctetString"
_HwNmNorthboundsAdditionalVB7_Object = MibScalar
hwNmNorthboundsAdditionalVB7 = _HwNmNorthboundsAdditionalVB7_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 22),
    _HwNmNorthboundsAdditionalVB7_Type()
)
hwNmNorthboundsAdditionalVB7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNmNorthboundsAdditionalVB7.setStatus("mandatory")


class _HwNmNorthboundsAdditionalVB8_Type(OctetString):
    """Custom type hwNmNorthboundsAdditionalVB8 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwNmNorthboundsAdditionalVB8_Type.__name__ = "OctetString"
_HwNmNorthboundsAdditionalVB8_Object = MibScalar
hwNmNorthboundsAdditionalVB8 = _HwNmNorthboundsAdditionalVB8_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 23),
    _HwNmNorthboundsAdditionalVB8_Type()
)
hwNmNorthboundsAdditionalVB8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNmNorthboundsAdditionalVB8.setStatus("mandatory")


class _HwNmNorthboundEventName_Type(OctetString):
    """Custom type hwNmNorthboundEventName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwNmNorthboundEventName_Type.__name__ = "OctetString"
_HwNmNorthboundEventName_Object = MibScalar
hwNmNorthboundEventName = _HwNmNorthboundEventName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 24),
    _HwNmNorthboundEventName_Type()
)
hwNmNorthboundEventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNmNorthboundEventName.setStatus("mandatory")
_HwNmNorthboundEventKeepAliveInfo_ObjectIdentity = ObjectIdentity
hwNmNorthboundEventKeepAliveInfo = _HwNmNorthboundEventKeepAliveInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 2)
)
_HwNmNorthboundEventSynchronization_ObjectIdentity = ObjectIdentity
hwNmNorthboundEventSynchronization = _HwNmNorthboundEventSynchronization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 7)
)
_HwNmNorthboundEventSynchronizationStart_ObjectIdentity = ObjectIdentity
hwNmNorthboundEventSynchronizationStart = _HwNmNorthboundEventSynchronizationStart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 7, 1)
)
_HwNmNorthboundEventSynchronizationQueryResult_ObjectIdentity = ObjectIdentity
hwNmNorthboundEventSynchronizationQueryResult = _HwNmNorthboundEventSynchronizationQueryResult_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 7, 2)
)
_HwNmNorthboundEventSynchronizationEnd_ObjectIdentity = ObjectIdentity
hwNmNorthboundEventSynchronizationEnd = _HwNmNorthboundEventSynchronizationEnd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 7, 3)
)


class _HwNmNorthboundEventSynchronizationEndStatus_Type(Integer32):
    """Custom type hwNmNorthboundEventSynchronizationEndStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 3),
          ("normalEnd", 1),
          ("stopped", 2))
    )


_HwNmNorthboundEventSynchronizationEndStatus_Type.__name__ = "Integer32"
_HwNmNorthboundEventSynchronizationEndStatus_Object = MibScalar
hwNmNorthboundEventSynchronizationEndStatus = _HwNmNorthboundEventSynchronizationEndStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 7, 3, 1),
    _HwNmNorthboundEventSynchronizationEndStatus_Type()
)
hwNmNorthboundEventSynchronizationEndStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNmNorthboundEventSynchronizationEndStatus.setStatus("mandatory")
_HwNmNorthboundEventSynchronizationEndStatusDetail_Type = OctetString
_HwNmNorthboundEventSynchronizationEndStatusDetail_Object = MibScalar
hwNmNorthboundEventSynchronizationEndStatusDetail = _HwNmNorthboundEventSynchronizationEndStatusDetail_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 7, 3, 2),
    _HwNmNorthboundEventSynchronizationEndStatusDetail_Type()
)
hwNmNorthboundEventSynchronizationEndStatusDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNmNorthboundEventSynchronizationEndStatusDetail.setStatus("mandatory")
_HwNmNorthboundEventSynchronizationCommandStart_Type = OctetString
_HwNmNorthboundEventSynchronizationCommandStart_Object = MibScalar
hwNmNorthboundEventSynchronizationCommandStart = _HwNmNorthboundEventSynchronizationCommandStart_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 7, 4),
    _HwNmNorthboundEventSynchronizationCommandStart_Type()
)
hwNmNorthboundEventSynchronizationCommandStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwNmNorthboundEventSynchronizationCommandStart.setStatus("mandatory")
_HwNmNorthboundEventSynchronizationCommandStop_Type = OctetString
_HwNmNorthboundEventSynchronizationCommandStop_Object = MibScalar
hwNmNorthboundEventSynchronizationCommandStop = _HwNmNorthboundEventSynchronizationCommandStop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 7, 5),
    _HwNmNorthboundEventSynchronizationCommandStop_Type()
)
hwNmNorthboundEventSynchronizationCommandStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwNmNorthboundEventSynchronizationCommandStop.setStatus("mandatory")

# Managed Objects groups


# Notification objects

hwNmNorthboundEventNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 0, 1)
)
hwNmNorthboundEventNotify.setObjects(
      *(("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundNEName"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundNEType"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundObjectInstance"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventType"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventTime"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundProbableCause"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundSeverity"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventDetail"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundAdditionalInfo"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundFaultFlag"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundFaultFunction"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundDeviceIP"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundSerialNo"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundProbableRepair"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundResourceIDs"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB1"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB2"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB3"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB4"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB5"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB6"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB7"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB8"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventName"))
)
if mibBuilder.loadTexts:
    hwNmNorthboundEventNotify.setStatus(
        ""
    )

hwNmNorthboundEventNotifyCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 0, 3)
)
hwNmNorthboundEventNotifyCritical.setObjects(
      *(("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundNEName"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundNEType"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundObjectInstance"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventType"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventTime"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundProbableCause"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundSeverity"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventDetail"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundAdditionalInfo"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundFaultFlag"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundFaultFunction"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundDeviceIP"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundSerialNo"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundProbableRepair"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundResourceIDs"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB1"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB2"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB3"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB4"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB5"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB6"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB7"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB8"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventName"))
)
if mibBuilder.loadTexts:
    hwNmNorthboundEventNotifyCritical.setStatus(
        ""
    )

hwNmNorthboundEventNotifyMajor = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 0, 4)
)
hwNmNorthboundEventNotifyMajor.setObjects(
      *(("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundNEName"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundNEType"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundObjectInstance"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventType"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventTime"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundProbableCause"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundSeverity"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventDetail"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundAdditionalInfo"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundFaultFlag"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundFaultFunction"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundDeviceIP"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundSerialNo"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundProbableRepair"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundResourceIDs"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB1"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB2"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB3"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB4"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB5"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB6"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB7"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB8"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventName"))
)
if mibBuilder.loadTexts:
    hwNmNorthboundEventNotifyMajor.setStatus(
        ""
    )

hwNmNorthboundEventNotifyMinor = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 0, 5)
)
hwNmNorthboundEventNotifyMinor.setObjects(
      *(("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundNEName"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundNEType"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundObjectInstance"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventType"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventTime"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundProbableCause"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundSeverity"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventDetail"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundAdditionalInfo"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundFaultFlag"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundFaultFunction"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundDeviceIP"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundSerialNo"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundProbableRepair"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundResourceIDs"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB1"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB2"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB3"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB4"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB5"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB6"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB7"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB8"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventName"))
)
if mibBuilder.loadTexts:
    hwNmNorthboundEventNotifyMinor.setStatus(
        ""
    )

hwNmNorthboundEventNotifyWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 0, 6)
)
hwNmNorthboundEventNotifyWarning.setObjects(
      *(("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundNEName"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundNEType"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundObjectInstance"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventType"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventTime"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundProbableCause"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundSeverity"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventDetail"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundAdditionalInfo"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundFaultFlag"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundFaultFunction"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundDeviceIP"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundSerialNo"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundProbableRepair"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundResourceIDs"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB1"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB2"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB3"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB4"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB5"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB6"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB7"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB8"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventName"))
)
if mibBuilder.loadTexts:
    hwNmNorthboundEventNotifyWarning.setStatus(
        ""
    )

hwNmNorthboundEventNotifyIndefinitely = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 0, 7)
)
hwNmNorthboundEventNotifyIndefinitely.setObjects(
      *(("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundNEName"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundNEType"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundObjectInstance"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventType"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventTime"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundProbableCause"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundSeverity"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventDetail"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundAdditionalInfo"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundFaultFlag"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundFaultFunction"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundDeviceIP"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundSerialNo"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundProbableRepair"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundResourceIDs"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB1"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB2"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB3"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB4"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB5"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB6"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB7"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB8"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventName"))
)
if mibBuilder.loadTexts:
    hwNmNorthboundEventNotifyIndefinitely.setStatus(
        ""
    )

hwNmNorthboundEventNotifyUnknownSeverity = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 0, 8)
)
hwNmNorthboundEventNotifyUnknownSeverity.setObjects(
      *(("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundNEName"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundNEType"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundObjectInstance"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventType"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventTime"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundProbableCause"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundSeverity"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventDetail"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundAdditionalInfo"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundFaultFlag"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundFaultFunction"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundDeviceIP"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundSerialNo"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundProbableRepair"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundResourceIDs"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB1"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB2"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB3"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB4"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB5"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB6"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB7"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB8"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventName"))
)
if mibBuilder.loadTexts:
    hwNmNorthboundEventNotifyUnknownSeverity.setStatus(
        ""
    )

hwNmNorthboundEventKeepAlive = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 2, 0, 2)
)
if mibBuilder.loadTexts:
    hwNmNorthboundEventKeepAlive.setStatus(
        ""
    )

hwNmNorthboundEventSynchronizationStartNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 7, 1, 0, 9)
)
if mibBuilder.loadTexts:
    hwNmNorthboundEventSynchronizationStartNotify.setStatus(
        ""
    )

hwNmNorthboundEventSynchronizationQueryResultNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 7, 2, 0, 10)
)
hwNmNorthboundEventSynchronizationQueryResultNotify.setObjects(
      *(("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundNEName"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundNEType"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundObjectInstance"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventType"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventTime"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundProbableCause"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundSeverity"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventDetail"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundAdditionalInfo"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundFaultFlag"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundFaultFunction"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundDeviceIP"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundSerialNo"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundProbableRepair"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundResourceIDs"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB1"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB2"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB3"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB4"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB5"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB6"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB7"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB8"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventName"))
)
if mibBuilder.loadTexts:
    hwNmNorthboundEventSynchronizationQueryResultNotify.setStatus(
        ""
    )

hwNmNorthboundEventSynchronizationEndNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 7, 3, 0, 11)
)
hwNmNorthboundEventSynchronizationEndNotify.setObjects(
      *(("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventSynchronizationEndStatus"),
        ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventSynchronizationEndStatusDetail"))
)
if mibBuilder.loadTexts:
    hwNmNorthboundEventSynchronizationEndNotify.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HW-IMAPV1NORTHBOUND-TRAP-MIB",
    **{"huawei": huawei,
       "products": products,
       "hwNetManagement": hwNetManagement,
       "hwNmAgent": hwNmAgent,
       "hwNmFault": hwNmFault,
       "thirdNMSFaultFilter": thirdNMSFaultFilter,
       "hwNmNorthboundEvent": hwNmNorthboundEvent,
       "hwNmNorthboundEventInfo": hwNmNorthboundEventInfo,
       "hwNmNorthboundEventNotify": hwNmNorthboundEventNotify,
       "hwNmNorthboundEventNotifyCritical": hwNmNorthboundEventNotifyCritical,
       "hwNmNorthboundEventNotifyMajor": hwNmNorthboundEventNotifyMajor,
       "hwNmNorthboundEventNotifyMinor": hwNmNorthboundEventNotifyMinor,
       "hwNmNorthboundEventNotifyWarning": hwNmNorthboundEventNotifyWarning,
       "hwNmNorthboundEventNotifyIndefinitely": hwNmNorthboundEventNotifyIndefinitely,
       "hwNmNorthboundEventNotifyUnknownSeverity": hwNmNorthboundEventNotifyUnknownSeverity,
       "hwNmNorthboundNEName": hwNmNorthboundNEName,
       "hwNmNorthboundNEType": hwNmNorthboundNEType,
       "hwNmNorthboundObjectInstance": hwNmNorthboundObjectInstance,
       "hwNmNorthboundEventType": hwNmNorthboundEventType,
       "hwNmNorthboundEventTime": hwNmNorthboundEventTime,
       "hwNmNorthboundProbableCause": hwNmNorthboundProbableCause,
       "hwNmNorthboundSeverity": hwNmNorthboundSeverity,
       "hwNmNorthboundEventDetail": hwNmNorthboundEventDetail,
       "hwNmNorthboundAdditionalInfo": hwNmNorthboundAdditionalInfo,
       "hwNmNorthboundFaultFlag": hwNmNorthboundFaultFlag,
       "hwNmNorthboundFaultFunction": hwNmNorthboundFaultFunction,
       "hwNmNorthboundDeviceIP": hwNmNorthboundDeviceIP,
       "hwNmNorthboundSerialNo": hwNmNorthboundSerialNo,
       "hwNmNorthboundProbableRepair": hwNmNorthboundProbableRepair,
       "hwNmNorthboundResourceIDs": hwNmNorthboundResourceIDs,
       "hwNmNorthboundsAdditionalVB1": hwNmNorthboundsAdditionalVB1,
       "hwNmNorthboundsAdditionalVB2": hwNmNorthboundsAdditionalVB2,
       "hwNmNorthboundsAdditionalVB3": hwNmNorthboundsAdditionalVB3,
       "hwNmNorthboundsAdditionalVB4": hwNmNorthboundsAdditionalVB4,
       "hwNmNorthboundsAdditionalVB5": hwNmNorthboundsAdditionalVB5,
       "hwNmNorthboundsAdditionalVB6": hwNmNorthboundsAdditionalVB6,
       "hwNmNorthboundsAdditionalVB7": hwNmNorthboundsAdditionalVB7,
       "hwNmNorthboundsAdditionalVB8": hwNmNorthboundsAdditionalVB8,
       "hwNmNorthboundEventName": hwNmNorthboundEventName,
       "hwNmNorthboundEventKeepAliveInfo": hwNmNorthboundEventKeepAliveInfo,
       "hwNmNorthboundEventKeepAlive": hwNmNorthboundEventKeepAlive,
       "hwNmNorthboundEventSynchronization": hwNmNorthboundEventSynchronization,
       "hwNmNorthboundEventSynchronizationStart": hwNmNorthboundEventSynchronizationStart,
       "hwNmNorthboundEventSynchronizationStartNotify": hwNmNorthboundEventSynchronizationStartNotify,
       "hwNmNorthboundEventSynchronizationQueryResult": hwNmNorthboundEventSynchronizationQueryResult,
       "hwNmNorthboundEventSynchronizationQueryResultNotify": hwNmNorthboundEventSynchronizationQueryResultNotify,
       "hwNmNorthboundEventSynchronizationEnd": hwNmNorthboundEventSynchronizationEnd,
       "hwNmNorthboundEventSynchronizationEndNotify": hwNmNorthboundEventSynchronizationEndNotify,
       "hwNmNorthboundEventSynchronizationEndStatus": hwNmNorthboundEventSynchronizationEndStatus,
       "hwNmNorthboundEventSynchronizationEndStatusDetail": hwNmNorthboundEventSynchronizationEndStatusDetail,
       "hwNmNorthboundEventSynchronizationCommandStart": hwNmNorthboundEventSynchronizationCommandStart,
       "hwNmNorthboundEventSynchronizationCommandStop": hwNmNorthboundEventSynchronizationCommandStop}
)
