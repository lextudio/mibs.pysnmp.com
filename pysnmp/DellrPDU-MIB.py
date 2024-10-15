# SNMP MIB module (DellrPDU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DellrPDU-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:35:45 2024
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



class RpduEnableDisableType(Integer32):
    """Custom type RpduEnableDisableType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )





class RpduNormalAlarmType(Integer32):
    """Custom type RpduNormalAlarmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 2),
          ("normal", 1))
    )





class RpduCommNoneOKLostType(Integer32):
    """Custom type RpduCommNoneOKLostType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("commsLost", 3),
          ("commsOK", 2),
          ("notInstalled", 1))
    )





class RpduLowNormalNearOverloadType(Integer32):
    """Custom type RpduLowNormalNearOverloadType based on Integer32"""
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
        *(("lowLoad", 1),
          ("nearOverload", 3),
          ("normal", 2),
          ("overload", 4))
    )





class RpduNotPBMinLowNrmlOHiMaxType(Integer32):
    """Custom type RpduNotPBMinLowNrmlOHiMaxType based on Integer32"""
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
        *(("belowLow", 3),
          ("belowMin", 2),
          ("normal", 4),
          ("notPresent", 1),
          ("overHigh", 5),
          ("overMax", 6))
    )





class RpduOtherToNonrecoverableType(Integer32):
    """Custom type RpduOtherToNonrecoverableType based on Integer32"""
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
        *(("critical", 5),
          ("non-critical", 4),
          ("non-recoverable", 6),
          ("ok", 3),
          ("other", 1),
          ("unknown", 2))
    )





class RpduOutletPhaseLayoutType(Integer32):
    """Custom type RpduOutletPhaseLayoutType based on Integer32"""
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
        *(("seqPhase1ToNeutral", 1),
          ("seqPhase1ToPhase2", 4),
          ("seqPhase2ToNeutral", 2),
          ("seqPhase2ToPhase3", 5),
          ("seqPhase3ToNeutral", 3),
          ("seqPhase3ToPhase1", 6))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dell_ObjectIdentity = ObjectIdentity
dell = _Dell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674)
)
_Pdu_ObjectIdentity = ObjectIdentity
pdu = _Pdu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10903)
)
_Pdusub_ObjectIdentity = ObjectIdentity
pdusub = _Pdusub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200)
)
_Software_ObjectIdentity = ObjectIdentity
software = _Software_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 1)
)
_Hardware_ObjectIdentity = ObjectIdentity
hardware = _Hardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2)
)
_ProductID_ObjectIdentity = ObjectIdentity
productID = _ProductID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 100)
)
_ProductIDDisplayName_Type = DisplayString
_ProductIDDisplayName_Object = MibScalar
productIDDisplayName = _ProductIDDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 100, 1),
    _ProductIDDisplayName_Type()
)
productIDDisplayName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    productIDDisplayName.setStatus("mandatory")
_ProductIDDescription_Type = DisplayString
_ProductIDDescription_Object = MibScalar
productIDDescription = _ProductIDDescription_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 100, 2),
    _ProductIDDescription_Type()
)
productIDDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    productIDDescription.setStatus("mandatory")
_ProductIDVendor_Type = DisplayString
_ProductIDVendor_Object = MibScalar
productIDVendor = _ProductIDVendor_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 100, 3),
    _ProductIDVendor_Type()
)
productIDVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productIDVendor.setStatus("mandatory")
_ProductIDVersion_Type = DisplayString
_ProductIDVersion_Object = MibScalar
productIDVersion = _ProductIDVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 100, 4),
    _ProductIDVersion_Type()
)
productIDVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productIDVersion.setStatus("mandatory")
_ProductIDBuildNumber_Type = DisplayString
_ProductIDBuildNumber_Object = MibScalar
productIDBuildNumber = _ProductIDBuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 100, 5),
    _ProductIDBuildNumber_Type()
)
productIDBuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productIDBuildNumber.setStatus("mandatory")
_ProductIDURL_Type = DisplayString
_ProductIDURL_Object = MibScalar
productIDURL = _ProductIDURL_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 100, 6),
    _ProductIDURL_Type()
)
productIDURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productIDURL.setStatus("mandatory")
_ProductIDDeviceNetworkName_Type = DisplayString
_ProductIDDeviceNetworkName_Object = MibScalar
productIDDeviceNetworkName = _ProductIDDeviceNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 100, 7),
    _ProductIDDeviceNetworkName_Type()
)
productIDDeviceNetworkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    productIDDeviceNetworkName.setStatus("mandatory")
_ProductStatus_ObjectIdentity = ObjectIdentity
productStatus = _ProductStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 110)
)
_ProductStatusGlobalStatus_Type = RpduOtherToNonrecoverableType
_ProductStatusGlobalStatus_Object = MibScalar
productStatusGlobalStatus = _ProductStatusGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 110, 1),
    _ProductStatusGlobalStatus_Type()
)
productStatusGlobalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productStatusGlobalStatus.setStatus("mandatory")
_ProductStatusLastGlobalStatus_Type = RpduOtherToNonrecoverableType
_ProductStatusLastGlobalStatus_Object = MibScalar
productStatusLastGlobalStatus = _ProductStatusLastGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 110, 2),
    _ProductStatusLastGlobalStatus_Type()
)
productStatusLastGlobalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productStatusLastGlobalStatus.setStatus("mandatory")
_ProductStatusTimeStamp_Type = Integer32
_ProductStatusTimeStamp_Object = MibScalar
productStatusTimeStamp = _ProductStatusTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 110, 3),
    _ProductStatusTimeStamp_Type()
)
productStatusTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productStatusTimeStamp.setStatus("mandatory")
_ProductStatusRESERVED1_Type = DisplayString
_ProductStatusRESERVED1_Object = MibScalar
productStatusRESERVED1 = _ProductStatusRESERVED1_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 110, 4),
    _ProductStatusRESERVED1_Type()
)
productStatusRESERVED1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productStatusRESERVED1.setStatus("mandatory")
_ProductStatusRESERVED2_Type = DisplayString
_ProductStatusRESERVED2_Object = MibScalar
productStatusRESERVED2 = _ProductStatusRESERVED2_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 110, 5),
    _ProductStatusRESERVED2_Type()
)
productStatusRESERVED2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productStatusRESERVED2.setStatus("mandatory")
_ProductStatusRESERVED3_Type = DisplayString
_ProductStatusRESERVED3_Object = MibScalar
productStatusRESERVED3 = _ProductStatusRESERVED3_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 110, 6),
    _ProductStatusRESERVED3_Type()
)
productStatusRESERVED3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productStatusRESERVED3.setStatus("mandatory")
_RPDU_ObjectIdentity = ObjectIdentity
rPDU = _RPDU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200)
)
_RPDUIdentD_ObjectIdentity = ObjectIdentity
rPDUIdentD = _RPDUIdentD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 100)
)
_RPDUIdentTableSize_Type = Integer32
_RPDUIdentTableSize_Object = MibScalar
rPDUIdentTableSize = _RPDUIdentTableSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 100, 1),
    _RPDUIdentTableSize_Type()
)
rPDUIdentTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUIdentTableSize.setStatus("mandatory")
_RPDUIdentTable_Object = MibTable
rPDUIdentTable = _RPDUIdentTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 100, 2)
)
if mibBuilder.loadTexts:
    rPDUIdentTable.setStatus("mandatory")
_RPDUIdentEntry_Object = MibTableRow
rPDUIdentEntry = _RPDUIdentEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 100, 2, 1)
)
rPDUIdentEntry.setIndexNames(
    (0, "DellrPDU-MIB", "rPDUIdentIndex"),
)
if mibBuilder.loadTexts:
    rPDUIdentEntry.setStatus("mandatory")
_RPDUIdentIndex_Type = Integer32
_RPDUIdentIndex_Object = MibTableColumn
rPDUIdentIndex = _RPDUIdentIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 100, 2, 1, 1),
    _RPDUIdentIndex_Type()
)
rPDUIdentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUIdentIndex.setStatus("mandatory")
_RPDUIdentNameD_Type = DisplayString
_RPDUIdentNameD_Object = MibTableColumn
rPDUIdentNameD = _RPDUIdentNameD_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 100, 2, 1, 2),
    _RPDUIdentNameD_Type()
)
rPDUIdentNameD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDUIdentNameD.setStatus("mandatory")
_RPDUIdentLocation_Type = DisplayString
_RPDUIdentLocation_Object = MibTableColumn
rPDUIdentLocation = _RPDUIdentLocation_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 100, 2, 1, 3),
    _RPDUIdentLocation_Type()
)
rPDUIdentLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDUIdentLocation.setStatus("mandatory")
_RPDUIdentHardwareRevD_Type = DisplayString
_RPDUIdentHardwareRevD_Object = MibTableColumn
rPDUIdentHardwareRevD = _RPDUIdentHardwareRevD_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 100, 2, 1, 4),
    _RPDUIdentHardwareRevD_Type()
)
rPDUIdentHardwareRevD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUIdentHardwareRevD.setStatus("mandatory")
_RPDUIdentFirmwareRevD_Type = DisplayString
_RPDUIdentFirmwareRevD_Object = MibTableColumn
rPDUIdentFirmwareRevD = _RPDUIdentFirmwareRevD_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 100, 2, 1, 5),
    _RPDUIdentFirmwareRevD_Type()
)
rPDUIdentFirmwareRevD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUIdentFirmwareRevD.setStatus("mandatory")
_RPDUIdentDateOfManufactureD_Type = DisplayString
_RPDUIdentDateOfManufactureD_Object = MibTableColumn
rPDUIdentDateOfManufactureD = _RPDUIdentDateOfManufactureD_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 100, 2, 1, 6),
    _RPDUIdentDateOfManufactureD_Type()
)
rPDUIdentDateOfManufactureD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUIdentDateOfManufactureD.setStatus("mandatory")
_RPDUIdentModelNumberD_Type = DisplayString
_RPDUIdentModelNumberD_Object = MibTableColumn
rPDUIdentModelNumberD = _RPDUIdentModelNumberD_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 100, 2, 1, 7),
    _RPDUIdentModelNumberD_Type()
)
rPDUIdentModelNumberD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUIdentModelNumberD.setStatus("mandatory")
_RPDUIdentSerialNumberD_Type = DisplayString
_RPDUIdentSerialNumberD_Object = MibTableColumn
rPDUIdentSerialNumberD = _RPDUIdentSerialNumberD_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 100, 2, 1, 8),
    _RPDUIdentSerialNumberD_Type()
)
rPDUIdentSerialNumberD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUIdentSerialNumberD.setStatus("mandatory")
_RPDUDevice_ObjectIdentity = ObjectIdentity
rPDUDevice = _RPDUDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 110)
)
_RPDUDeviceTableSize_Type = Integer32
_RPDUDeviceTableSize_Object = MibScalar
rPDUDeviceTableSize = _RPDUDeviceTableSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 110, 1),
    _RPDUDeviceTableSize_Type()
)
rPDUDeviceTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUDeviceTableSize.setStatus("mandatory")
_RPDUDeviceStatusTable_Object = MibTable
rPDUDeviceStatusTable = _RPDUDeviceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 110, 2)
)
if mibBuilder.loadTexts:
    rPDUDeviceStatusTable.setStatus("mandatory")
_RPDUDeviceStatusEntry_Object = MibTableRow
rPDUDeviceStatusEntry = _RPDUDeviceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 110, 2, 1)
)
rPDUDeviceStatusEntry.setIndexNames(
    (0, "DellrPDU-MIB", "rPDUDeviceStatusIndex"),
)
if mibBuilder.loadTexts:
    rPDUDeviceStatusEntry.setStatus("mandatory")
_RPDUDeviceStatusIndex_Type = Integer32
_RPDUDeviceStatusIndex_Object = MibTableColumn
rPDUDeviceStatusIndex = _RPDUDeviceStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 110, 2, 1, 1),
    _RPDUDeviceStatusIndex_Type()
)
rPDUDeviceStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUDeviceStatusIndex.setStatus("mandatory")
_RPDUDeviceStatusName_Type = DisplayString
_RPDUDeviceStatusName_Object = MibTableColumn
rPDUDeviceStatusName = _RPDUDeviceStatusName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 110, 2, 1, 2),
    _RPDUDeviceStatusName_Type()
)
rPDUDeviceStatusName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDUDeviceStatusName.setStatus("mandatory")
_RPDUDeviceStatusPower_Type = Integer32
_RPDUDeviceStatusPower_Object = MibTableColumn
rPDUDeviceStatusPower = _RPDUDeviceStatusPower_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 110, 2, 1, 3),
    _RPDUDeviceStatusPower_Type()
)
rPDUDeviceStatusPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUDeviceStatusPower.setStatus("mandatory")
_RPDUDeviceStatusEnergy_Type = Integer32
_RPDUDeviceStatusEnergy_Object = MibTableColumn
rPDUDeviceStatusEnergy = _RPDUDeviceStatusEnergy_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 110, 2, 1, 4),
    _RPDUDeviceStatusEnergy_Type()
)
rPDUDeviceStatusEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUDeviceStatusEnergy.setStatus("mandatory")


class _RPDUDeviceStatusCommandPending_Type(Integer32):
    """Custom type rPDUDeviceStatusCommandPending based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("commandPending", 1),
          ("commandPendingUnknown", 3),
          ("noCommandPending", 2))
    )


_RPDUDeviceStatusCommandPending_Type.__name__ = "Integer32"
_RPDUDeviceStatusCommandPending_Object = MibTableColumn
rPDUDeviceStatusCommandPending = _RPDUDeviceStatusCommandPending_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 110, 2, 1, 5),
    _RPDUDeviceStatusCommandPending_Type()
)
rPDUDeviceStatusCommandPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUDeviceStatusCommandPending.setStatus("mandatory")
_RPDUDeviceStatusLoadState_Type = RpduLowNormalNearOverloadType
_RPDUDeviceStatusLoadState_Object = MibTableColumn
rPDUDeviceStatusLoadState = _RPDUDeviceStatusLoadState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 110, 2, 1, 6),
    _RPDUDeviceStatusLoadState_Type()
)
rPDUDeviceStatusLoadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUDeviceStatusLoadState.setStatus("mandatory")
_RPDUDeviceConfigTable_Object = MibTable
rPDUDeviceConfigTable = _RPDUDeviceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 110, 3)
)
if mibBuilder.loadTexts:
    rPDUDeviceConfigTable.setStatus("mandatory")
_RPDUDeviceConfigEntry_Object = MibTableRow
rPDUDeviceConfigEntry = _RPDUDeviceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 110, 3, 1)
)
rPDUDeviceConfigEntry.setIndexNames(
    (0, "DellrPDU-MIB", "rPDUDeviceConfigIndex"),
)
if mibBuilder.loadTexts:
    rPDUDeviceConfigEntry.setStatus("mandatory")
_RPDUDeviceConfigIndex_Type = Integer32
_RPDUDeviceConfigIndex_Object = MibTableColumn
rPDUDeviceConfigIndex = _RPDUDeviceConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 110, 3, 1, 1),
    _RPDUDeviceConfigIndex_Type()
)
rPDUDeviceConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUDeviceConfigIndex.setStatus("mandatory")
_RPDUDeviceConfigName_Type = DisplayString
_RPDUDeviceConfigName_Object = MibTableColumn
rPDUDeviceConfigName = _RPDUDeviceConfigName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 110, 3, 1, 2),
    _RPDUDeviceConfigName_Type()
)
rPDUDeviceConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDUDeviceConfigName.setStatus("mandatory")
_RPDUDeviceConfigLocation_Type = DisplayString
_RPDUDeviceConfigLocation_Object = MibTableColumn
rPDUDeviceConfigLocation = _RPDUDeviceConfigLocation_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 110, 3, 1, 3),
    _RPDUDeviceConfigLocation_Type()
)
rPDUDeviceConfigLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDUDeviceConfigLocation.setStatus("mandatory")
_RPDUDeviceConfigColdstartDelay_Type = Integer32
_RPDUDeviceConfigColdstartDelay_Object = MibTableColumn
rPDUDeviceConfigColdstartDelay = _RPDUDeviceConfigColdstartDelay_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 110, 3, 1, 4),
    _RPDUDeviceConfigColdstartDelay_Type()
)
rPDUDeviceConfigColdstartDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDUDeviceConfigColdstartDelay.setStatus("mandatory")
_RPDUDeviceCfgLowLoadPwrThresh_Type = Integer32
_RPDUDeviceCfgLowLoadPwrThresh_Object = MibTableColumn
rPDUDeviceCfgLowLoadPwrThresh = _RPDUDeviceCfgLowLoadPwrThresh_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 110, 3, 1, 5),
    _RPDUDeviceCfgLowLoadPwrThresh_Type()
)
rPDUDeviceCfgLowLoadPwrThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDUDeviceCfgLowLoadPwrThresh.setStatus("mandatory")
_RPDUDeviceCfgNerOvloadPwrThresh_Type = Integer32
_RPDUDeviceCfgNerOvloadPwrThresh_Object = MibTableColumn
rPDUDeviceCfgNerOvloadPwrThresh = _RPDUDeviceCfgNerOvloadPwrThresh_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 110, 3, 1, 6),
    _RPDUDeviceCfgNerOvloadPwrThresh_Type()
)
rPDUDeviceCfgNerOvloadPwrThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDUDeviceCfgNerOvloadPwrThresh.setStatus("mandatory")
_RPDUDeviceCfgOverloadPwrThresh_Type = Integer32
_RPDUDeviceCfgOverloadPwrThresh_Object = MibTableColumn
rPDUDeviceCfgOverloadPwrThresh = _RPDUDeviceCfgOverloadPwrThresh_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 110, 3, 1, 7),
    _RPDUDeviceCfgOverloadPwrThresh_Type()
)
rPDUDeviceCfgOverloadPwrThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDUDeviceCfgOverloadPwrThresh.setStatus("mandatory")
_RPDUDeviceConfigPowerHeadroom_Type = Integer32
_RPDUDeviceConfigPowerHeadroom_Object = MibTableColumn
rPDUDeviceConfigPowerHeadroom = _RPDUDeviceConfigPowerHeadroom_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 110, 3, 1, 8),
    _RPDUDeviceConfigPowerHeadroom_Type()
)
rPDUDeviceConfigPowerHeadroom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUDeviceConfigPowerHeadroom.setStatus("mandatory")
_RPDUDeviceConfigPeakPower_Type = Integer32
_RPDUDeviceConfigPeakPower_Object = MibTableColumn
rPDUDeviceConfigPeakPower = _RPDUDeviceConfigPeakPower_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 110, 3, 1, 9),
    _RPDUDeviceConfigPeakPower_Type()
)
rPDUDeviceConfigPeakPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUDeviceConfigPeakPower.setStatus("mandatory")
_RPDUDeviceCfgPeakPwrStartTime_Type = DisplayString
_RPDUDeviceCfgPeakPwrStartTime_Object = MibTableColumn
rPDUDeviceCfgPeakPwrStartTime = _RPDUDeviceCfgPeakPwrStartTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 110, 3, 1, 10),
    _RPDUDeviceCfgPeakPwrStartTime_Type()
)
rPDUDeviceCfgPeakPwrStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUDeviceCfgPeakPwrStartTime.setStatus("mandatory")
_RPDUDeviceConfigPeakPwrCapTime_Type = DisplayString
_RPDUDeviceConfigPeakPwrCapTime_Object = MibTableColumn
rPDUDeviceConfigPeakPwrCapTime = _RPDUDeviceConfigPeakPwrCapTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 110, 3, 1, 11),
    _RPDUDeviceConfigPeakPwrCapTime_Type()
)
rPDUDeviceConfigPeakPwrCapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUDeviceConfigPeakPwrCapTime.setStatus("mandatory")
_RPDUDeviceCfgPeakPowerHeadroom_Type = Integer32
_RPDUDeviceCfgPeakPowerHeadroom_Object = MibTableColumn
rPDUDeviceCfgPeakPowerHeadroom = _RPDUDeviceCfgPeakPowerHeadroom_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 110, 3, 1, 12),
    _RPDUDeviceCfgPeakPowerHeadroom_Type()
)
rPDUDeviceCfgPeakPowerHeadroom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUDeviceCfgPeakPowerHeadroom.setStatus("mandatory")
_RPDUDeviceCfgEnergyStartTime_Type = DisplayString
_RPDUDeviceCfgEnergyStartTime_Object = MibTableColumn
rPDUDeviceCfgEnergyStartTime = _RPDUDeviceCfgEnergyStartTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 110, 3, 1, 13),
    _RPDUDeviceCfgEnergyStartTime_Type()
)
rPDUDeviceCfgEnergyStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUDeviceCfgEnergyStartTime.setStatus("mandatory")
_RPDUDevicePropertiesTable_Object = MibTable
rPDUDevicePropertiesTable = _RPDUDevicePropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 110, 4)
)
if mibBuilder.loadTexts:
    rPDUDevicePropertiesTable.setStatus("mandatory")
_RPDUDevicePropertiesEntry_Object = MibTableRow
rPDUDevicePropertiesEntry = _RPDUDevicePropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 110, 4, 1)
)
rPDUDevicePropertiesEntry.setIndexNames(
    (0, "DellrPDU-MIB", "rPDUDevicePropertiesIndex"),
)
if mibBuilder.loadTexts:
    rPDUDevicePropertiesEntry.setStatus("mandatory")
_RPDUDevicePropertiesIndex_Type = Integer32
_RPDUDevicePropertiesIndex_Object = MibTableColumn
rPDUDevicePropertiesIndex = _RPDUDevicePropertiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 110, 4, 1, 1),
    _RPDUDevicePropertiesIndex_Type()
)
rPDUDevicePropertiesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUDevicePropertiesIndex.setStatus("mandatory")
_RPDUDevicePropertiesName_Type = DisplayString
_RPDUDevicePropertiesName_Object = MibTableColumn
rPDUDevicePropertiesName = _RPDUDevicePropertiesName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 110, 4, 1, 2),
    _RPDUDevicePropertiesName_Type()
)
rPDUDevicePropertiesName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDUDevicePropertiesName.setStatus("mandatory")
_RPDUDevicePropertiesNumOutlets_Type = Integer32
_RPDUDevicePropertiesNumOutlets_Object = MibTableColumn
rPDUDevicePropertiesNumOutlets = _RPDUDevicePropertiesNumOutlets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 110, 4, 1, 3),
    _RPDUDevicePropertiesNumOutlets_Type()
)
rPDUDevicePropertiesNumOutlets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUDevicePropertiesNumOutlets.setStatus("mandatory")
_RPDUDevicePropertiesNumSwdOuts_Type = Integer32
_RPDUDevicePropertiesNumSwdOuts_Object = MibTableColumn
rPDUDevicePropertiesNumSwdOuts = _RPDUDevicePropertiesNumSwdOuts_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 110, 4, 1, 4),
    _RPDUDevicePropertiesNumSwdOuts_Type()
)
rPDUDevicePropertiesNumSwdOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUDevicePropertiesNumSwdOuts.setStatus("mandatory")
_RPDUDevicePropertiesNumMtrdOuts_Type = Integer32
_RPDUDevicePropertiesNumMtrdOuts_Object = MibTableColumn
rPDUDevicePropertiesNumMtrdOuts = _RPDUDevicePropertiesNumMtrdOuts_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 110, 4, 1, 5),
    _RPDUDevicePropertiesNumMtrdOuts_Type()
)
rPDUDevicePropertiesNumMtrdOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUDevicePropertiesNumMtrdOuts.setStatus("mandatory")
_RPDUDevicePropertiesNumPhases_Type = Integer32
_RPDUDevicePropertiesNumPhases_Object = MibTableColumn
rPDUDevicePropertiesNumPhases = _RPDUDevicePropertiesNumPhases_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 110, 4, 1, 6),
    _RPDUDevicePropertiesNumPhases_Type()
)
rPDUDevicePropertiesNumPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUDevicePropertiesNumPhases.setStatus("mandatory")
_RPDUDevicePropertiesNumBreakers_Type = Integer32
_RPDUDevicePropertiesNumBreakers_Object = MibTableColumn
rPDUDevicePropertiesNumBreakers = _RPDUDevicePropertiesNumBreakers_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 110, 4, 1, 7),
    _RPDUDevicePropertiesNumBreakers_Type()
)
rPDUDevicePropertiesNumBreakers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUDevicePropertiesNumBreakers.setStatus("mandatory")
_RPDUDevicePropertiesMaxCurntRtg_Type = Integer32
_RPDUDevicePropertiesMaxCurntRtg_Object = MibTableColumn
rPDUDevicePropertiesMaxCurntRtg = _RPDUDevicePropertiesMaxCurntRtg_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 110, 4, 1, 8),
    _RPDUDevicePropertiesMaxCurntRtg_Type()
)
rPDUDevicePropertiesMaxCurntRtg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUDevicePropertiesMaxCurntRtg.setStatus("mandatory")


class _RPDUDevicePropertiesOutlayout_Type(Integer32):
    """Custom type rPDUDevicePropertiesOutlayout based on Integer32"""
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
        *(("phaseToNeutral", 1),
          ("phaseToNeutralGrouped", 3),
          ("phaseToPhase", 2),
          ("phaseToPhaseGrouped", 4))
    )


_RPDUDevicePropertiesOutlayout_Type.__name__ = "Integer32"
_RPDUDevicePropertiesOutlayout_Object = MibTableColumn
rPDUDevicePropertiesOutlayout = _RPDUDevicePropertiesOutlayout_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 110, 4, 1, 9),
    _RPDUDevicePropertiesOutlayout_Type()
)
rPDUDevicePropertiesOutlayout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUDevicePropertiesOutlayout.setStatus("mandatory")
_RPDUDeviceControlTable_Object = MibTable
rPDUDeviceControlTable = _RPDUDeviceControlTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 110, 5)
)
if mibBuilder.loadTexts:
    rPDUDeviceControlTable.setStatus("mandatory")
_RPDUDeviceControlEntry_Object = MibTableRow
rPDUDeviceControlEntry = _RPDUDeviceControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 110, 5, 1)
)
rPDUDeviceControlEntry.setIndexNames(
    (0, "DellrPDU-MIB", "rPDUDeviceControlIndex"),
)
if mibBuilder.loadTexts:
    rPDUDeviceControlEntry.setStatus("mandatory")
_RPDUDeviceControlIndex_Type = Integer32
_RPDUDeviceControlIndex_Object = MibTableColumn
rPDUDeviceControlIndex = _RPDUDeviceControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 110, 5, 1, 1),
    _RPDUDeviceControlIndex_Type()
)
rPDUDeviceControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUDeviceControlIndex.setStatus("mandatory")
_RPDUDeviceControlName_Type = DisplayString
_RPDUDeviceControlName_Object = MibTableColumn
rPDUDeviceControlName = _RPDUDeviceControlName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 110, 5, 1, 2),
    _RPDUDeviceControlName_Type()
)
rPDUDeviceControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDUDeviceControlName.setStatus("mandatory")


class _RPDUDeviceControlCommand_Type(Integer32):
    """Custom type rPDUDeviceControlCommand based on Integer32"""
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
        *(("noCommand", 6),
          ("rebootAllNow", 4),
          ("rebootAllSequence", 5),
          ("turnAllOffNow", 3),
          ("turnAllOffSequence", 7),
          ("turnAllOnNow", 1),
          ("turnAllOnSequence", 2))
    )


_RPDUDeviceControlCommand_Type.__name__ = "Integer32"
_RPDUDeviceControlCommand_Object = MibTableColumn
rPDUDeviceControlCommand = _RPDUDeviceControlCommand_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 110, 5, 1, 3),
    _RPDUDeviceControlCommand_Type()
)
rPDUDeviceControlCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDUDeviceControlCommand.setStatus("mandatory")
_RPDUPhase_ObjectIdentity = ObjectIdentity
rPDUPhase = _RPDUPhase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 120)
)
_RPDUPhaseTableSize_Type = Integer32
_RPDUPhaseTableSize_Object = MibScalar
rPDUPhaseTableSize = _RPDUPhaseTableSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 120, 1),
    _RPDUPhaseTableSize_Type()
)
rPDUPhaseTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUPhaseTableSize.setStatus("mandatory")
_RPDUPhaseStatusTable_Object = MibTable
rPDUPhaseStatusTable = _RPDUPhaseStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 120, 2)
)
if mibBuilder.loadTexts:
    rPDUPhaseStatusTable.setStatus("mandatory")
_RPDUPhaseStatusEntry_Object = MibTableRow
rPDUPhaseStatusEntry = _RPDUPhaseStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 120, 2, 1)
)
rPDUPhaseStatusEntry.setIndexNames(
    (0, "DellrPDU-MIB", "rPDUPhaseStatusIndex"),
)
if mibBuilder.loadTexts:
    rPDUPhaseStatusEntry.setStatus("mandatory")
_RPDUPhaseStatusIndex_Type = Integer32
_RPDUPhaseStatusIndex_Object = MibTableColumn
rPDUPhaseStatusIndex = _RPDUPhaseStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 120, 2, 1, 1),
    _RPDUPhaseStatusIndex_Type()
)
rPDUPhaseStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUPhaseStatusIndex.setStatus("mandatory")
_RPDUPhaseStatusNumber_Type = Integer32
_RPDUPhaseStatusNumber_Object = MibTableColumn
rPDUPhaseStatusNumber = _RPDUPhaseStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 120, 2, 1, 2),
    _RPDUPhaseStatusNumber_Type()
)
rPDUPhaseStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUPhaseStatusNumber.setStatus("mandatory")
_RPDUPhaseStatusLoadState_Type = RpduLowNormalNearOverloadType
_RPDUPhaseStatusLoadState_Object = MibTableColumn
rPDUPhaseStatusLoadState = _RPDUPhaseStatusLoadState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 120, 2, 1, 3),
    _RPDUPhaseStatusLoadState_Type()
)
rPDUPhaseStatusLoadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUPhaseStatusLoadState.setStatus("mandatory")
_RPDUPhaseStatusCurrent_Type = Integer32
_RPDUPhaseStatusCurrent_Object = MibTableColumn
rPDUPhaseStatusCurrent = _RPDUPhaseStatusCurrent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 120, 2, 1, 4),
    _RPDUPhaseStatusCurrent_Type()
)
rPDUPhaseStatusCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUPhaseStatusCurrent.setStatus("mandatory")
_RPDUPhaseStatusVoltage_Type = Integer32
_RPDUPhaseStatusVoltage_Object = MibTableColumn
rPDUPhaseStatusVoltage = _RPDUPhaseStatusVoltage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 120, 2, 1, 5),
    _RPDUPhaseStatusVoltage_Type()
)
rPDUPhaseStatusVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUPhaseStatusVoltage.setStatus("mandatory")
_RPDUPhaseStatusPower_Type = Integer32
_RPDUPhaseStatusPower_Object = MibTableColumn
rPDUPhaseStatusPower = _RPDUPhaseStatusPower_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 120, 2, 1, 6),
    _RPDUPhaseStatusPower_Type()
)
rPDUPhaseStatusPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUPhaseStatusPower.setStatus("mandatory")
_RPDUPhaseConfigTable_Object = MibTable
rPDUPhaseConfigTable = _RPDUPhaseConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 120, 3)
)
if mibBuilder.loadTexts:
    rPDUPhaseConfigTable.setStatus("mandatory")
_RPDUPhaseConfigEntry_Object = MibTableRow
rPDUPhaseConfigEntry = _RPDUPhaseConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 120, 3, 1)
)
rPDUPhaseConfigEntry.setIndexNames(
    (0, "DellrPDU-MIB", "rPDUPhaseConfigIndex"),
)
if mibBuilder.loadTexts:
    rPDUPhaseConfigEntry.setStatus("mandatory")
_RPDUPhaseConfigIndex_Type = Integer32
_RPDUPhaseConfigIndex_Object = MibTableColumn
rPDUPhaseConfigIndex = _RPDUPhaseConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 120, 3, 1, 1),
    _RPDUPhaseConfigIndex_Type()
)
rPDUPhaseConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUPhaseConfigIndex.setStatus("mandatory")
_RPDUPhaseConfigNumber_Type = Integer32
_RPDUPhaseConfigNumber_Object = MibTableColumn
rPDUPhaseConfigNumber = _RPDUPhaseConfigNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 120, 3, 1, 2),
    _RPDUPhaseConfigNumber_Type()
)
rPDUPhaseConfigNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUPhaseConfigNumber.setStatus("mandatory")


class _RPDUPhaseCfgOverloadRestriction_Type(Integer32):
    """Custom type rPDUPhaseCfgOverloadRestriction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alwaysAllowTurnON", 1),
          ("restrictOnNearOverload", 2),
          ("restrictOnOverload", 3))
    )


_RPDUPhaseCfgOverloadRestriction_Type.__name__ = "Integer32"
_RPDUPhaseCfgOverloadRestriction_Object = MibTableColumn
rPDUPhaseCfgOverloadRestriction = _RPDUPhaseCfgOverloadRestriction_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 120, 3, 1, 3),
    _RPDUPhaseCfgOverloadRestriction_Type()
)
rPDUPhaseCfgOverloadRestriction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDUPhaseCfgOverloadRestriction.setStatus("mandatory")
_RPDUPhCfgLowLoadCurntThreshold_Type = Integer32
_RPDUPhCfgLowLoadCurntThreshold_Object = MibTableColumn
rPDUPhCfgLowLoadCurntThreshold = _RPDUPhCfgLowLoadCurntThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 120, 3, 1, 4),
    _RPDUPhCfgLowLoadCurntThreshold_Type()
)
rPDUPhCfgLowLoadCurntThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDUPhCfgLowLoadCurntThreshold.setStatus("mandatory")
_RPDUPhCfgNerOverloadCurntThresh_Type = Integer32
_RPDUPhCfgNerOverloadCurntThresh_Object = MibTableColumn
rPDUPhCfgNerOverloadCurntThresh = _RPDUPhCfgNerOverloadCurntThresh_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 120, 3, 1, 5),
    _RPDUPhCfgNerOverloadCurntThresh_Type()
)
rPDUPhCfgNerOverloadCurntThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDUPhCfgNerOverloadCurntThresh.setStatus("mandatory")
_RPDUPhCfgOverloadCurntThreshold_Type = Integer32
_RPDUPhCfgOverloadCurntThreshold_Object = MibTableColumn
rPDUPhCfgOverloadCurntThreshold = _RPDUPhCfgOverloadCurntThreshold_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 120, 3, 1, 6),
    _RPDUPhCfgOverloadCurntThreshold_Type()
)
rPDUPhCfgOverloadCurntThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDUPhCfgOverloadCurntThreshold.setStatus("mandatory")
_RPDUOutlet_ObjectIdentity = ObjectIdentity
rPDUOutlet = _RPDUOutlet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130)
)
_RPDUOutletSwitched_ObjectIdentity = ObjectIdentity
rPDUOutletSwitched = _RPDUOutletSwitched_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 1)
)
_RPDUOutletSwitchedTableSize_Type = Integer32
_RPDUOutletSwitchedTableSize_Object = MibScalar
rPDUOutletSwitchedTableSize = _RPDUOutletSwitchedTableSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 1, 1),
    _RPDUOutletSwitchedTableSize_Type()
)
rPDUOutletSwitchedTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUOutletSwitchedTableSize.setStatus("mandatory")
_RPDUOutletSwitchedStatusTable_Object = MibTable
rPDUOutletSwitchedStatusTable = _RPDUOutletSwitchedStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 1, 2)
)
if mibBuilder.loadTexts:
    rPDUOutletSwitchedStatusTable.setStatus("mandatory")
_RPDUOutletSwitchedStatusEntry_Object = MibTableRow
rPDUOutletSwitchedStatusEntry = _RPDUOutletSwitchedStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 1, 2, 1)
)
rPDUOutletSwitchedStatusEntry.setIndexNames(
    (0, "DellrPDU-MIB", "rPDUOutletSwitchedStatusIndex"),
)
if mibBuilder.loadTexts:
    rPDUOutletSwitchedStatusEntry.setStatus("mandatory")
_RPDUOutletSwitchedStatusIndex_Type = Integer32
_RPDUOutletSwitchedStatusIndex_Object = MibTableColumn
rPDUOutletSwitchedStatusIndex = _RPDUOutletSwitchedStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 1, 2, 1, 1),
    _RPDUOutletSwitchedStatusIndex_Type()
)
rPDUOutletSwitchedStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUOutletSwitchedStatusIndex.setStatus("mandatory")
_RPDUOutletSwitchedStatusNumber_Type = Integer32
_RPDUOutletSwitchedStatusNumber_Object = MibTableColumn
rPDUOutletSwitchedStatusNumber = _RPDUOutletSwitchedStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 1, 2, 1, 2),
    _RPDUOutletSwitchedStatusNumber_Type()
)
rPDUOutletSwitchedStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUOutletSwitchedStatusNumber.setStatus("mandatory")
_RPDUOutletSwitchedStatusName_Type = DisplayString
_RPDUOutletSwitchedStatusName_Object = MibTableColumn
rPDUOutletSwitchedStatusName = _RPDUOutletSwitchedStatusName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 1, 2, 1, 3),
    _RPDUOutletSwitchedStatusName_Type()
)
rPDUOutletSwitchedStatusName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDUOutletSwitchedStatusName.setStatus("mandatory")


class _RPDUOutletSwitchedStatusState_Type(Integer32):
    """Custom type rPDUOutletSwitchedStatusState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1),
          ("unknown", 3))
    )


_RPDUOutletSwitchedStatusState_Type.__name__ = "Integer32"
_RPDUOutletSwitchedStatusState_Object = MibTableColumn
rPDUOutletSwitchedStatusState = _RPDUOutletSwitchedStatusState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 1, 2, 1, 4),
    _RPDUOutletSwitchedStatusState_Type()
)
rPDUOutletSwitchedStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUOutletSwitchedStatusState.setStatus("mandatory")


class _RPDUOutletSwitchedStatCmdPnding_Type(Integer32):
    """Custom type rPDUOutletSwitchedStatCmdPnding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("commandPending", 1),
          ("commandPendingUnknown", 3),
          ("noCommandPending", 2))
    )


_RPDUOutletSwitchedStatCmdPnding_Type.__name__ = "Integer32"
_RPDUOutletSwitchedStatCmdPnding_Object = MibTableColumn
rPDUOutletSwitchedStatCmdPnding = _RPDUOutletSwitchedStatCmdPnding_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 1, 2, 1, 5),
    _RPDUOutletSwitchedStatCmdPnding_Type()
)
rPDUOutletSwitchedStatCmdPnding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUOutletSwitchedStatCmdPnding.setStatus("mandatory")
_RPDUOutletSwitchedStatPhLayout_Type = RpduOutletPhaseLayoutType
_RPDUOutletSwitchedStatPhLayout_Object = MibTableColumn
rPDUOutletSwitchedStatPhLayout = _RPDUOutletSwitchedStatPhLayout_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 1, 2, 1, 6),
    _RPDUOutletSwitchedStatPhLayout_Type()
)
rPDUOutletSwitchedStatPhLayout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUOutletSwitchedStatPhLayout.setStatus("mandatory")
_RPDUOutletSwitchedConfigTable_Object = MibTable
rPDUOutletSwitchedConfigTable = _RPDUOutletSwitchedConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 1, 3)
)
if mibBuilder.loadTexts:
    rPDUOutletSwitchedConfigTable.setStatus("mandatory")
_RPDUOutletSwitchedConfigEntry_Object = MibTableRow
rPDUOutletSwitchedConfigEntry = _RPDUOutletSwitchedConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 1, 3, 1)
)
rPDUOutletSwitchedConfigEntry.setIndexNames(
    (0, "DellrPDU-MIB", "rPDUOutletSwitchedConfigIndex"),
)
if mibBuilder.loadTexts:
    rPDUOutletSwitchedConfigEntry.setStatus("mandatory")
_RPDUOutletSwitchedConfigIndex_Type = Integer32
_RPDUOutletSwitchedConfigIndex_Object = MibTableColumn
rPDUOutletSwitchedConfigIndex = _RPDUOutletSwitchedConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 1, 3, 1, 1),
    _RPDUOutletSwitchedConfigIndex_Type()
)
rPDUOutletSwitchedConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUOutletSwitchedConfigIndex.setStatus("mandatory")
_RPDUOutletSwitchedConfigNumber_Type = Integer32
_RPDUOutletSwitchedConfigNumber_Object = MibTableColumn
rPDUOutletSwitchedConfigNumber = _RPDUOutletSwitchedConfigNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 1, 3, 1, 2),
    _RPDUOutletSwitchedConfigNumber_Type()
)
rPDUOutletSwitchedConfigNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUOutletSwitchedConfigNumber.setStatus("mandatory")
_RPDUOutletSwitchedConfigName_Type = DisplayString
_RPDUOutletSwitchedConfigName_Object = MibTableColumn
rPDUOutletSwitchedConfigName = _RPDUOutletSwitchedConfigName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 1, 3, 1, 3),
    _RPDUOutletSwitchedConfigName_Type()
)
rPDUOutletSwitchedConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDUOutletSwitchedConfigName.setStatus("mandatory")
_RPDUOutSwitchedCfgPowerOnTime_Type = Integer32
_RPDUOutSwitchedCfgPowerOnTime_Object = MibTableColumn
rPDUOutSwitchedCfgPowerOnTime = _RPDUOutSwitchedCfgPowerOnTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 1, 3, 1, 4),
    _RPDUOutSwitchedCfgPowerOnTime_Type()
)
rPDUOutSwitchedCfgPowerOnTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDUOutSwitchedCfgPowerOnTime.setStatus("mandatory")
_RPDUOutSwitchedCfgPowerOffTime_Type = Integer32
_RPDUOutSwitchedCfgPowerOffTime_Object = MibTableColumn
rPDUOutSwitchedCfgPowerOffTime = _RPDUOutSwitchedCfgPowerOffTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 1, 3, 1, 5),
    _RPDUOutSwitchedCfgPowerOffTime_Type()
)
rPDUOutSwitchedCfgPowerOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDUOutSwitchedCfgPowerOffTime.setStatus("mandatory")
_RPDUOutSwtchedCfgRebootDuration_Type = Integer32
_RPDUOutSwtchedCfgRebootDuration_Object = MibTableColumn
rPDUOutSwtchedCfgRebootDuration = _RPDUOutSwtchedCfgRebootDuration_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 1, 3, 1, 6),
    _RPDUOutSwtchedCfgRebootDuration_Type()
)
rPDUOutSwtchedCfgRebootDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDUOutSwtchedCfgRebootDuration.setStatus("mandatory")
_RPDUOutletSwitchedControlTable_Object = MibTable
rPDUOutletSwitchedControlTable = _RPDUOutletSwitchedControlTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 1, 4)
)
if mibBuilder.loadTexts:
    rPDUOutletSwitchedControlTable.setStatus("mandatory")
_RPDUOutletSwitchedControlEntry_Object = MibTableRow
rPDUOutletSwitchedControlEntry = _RPDUOutletSwitchedControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 1, 4, 1)
)
rPDUOutletSwitchedControlEntry.setIndexNames(
    (0, "DellrPDU-MIB", "rPDUOutletSwitchedControlIndex"),
)
if mibBuilder.loadTexts:
    rPDUOutletSwitchedControlEntry.setStatus("mandatory")
_RPDUOutletSwitchedControlIndex_Type = Integer32
_RPDUOutletSwitchedControlIndex_Object = MibTableColumn
rPDUOutletSwitchedControlIndex = _RPDUOutletSwitchedControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 1, 4, 1, 1),
    _RPDUOutletSwitchedControlIndex_Type()
)
rPDUOutletSwitchedControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUOutletSwitchedControlIndex.setStatus("mandatory")
_RPDUOutletSwitchedControlNumber_Type = Integer32
_RPDUOutletSwitchedControlNumber_Object = MibTableColumn
rPDUOutletSwitchedControlNumber = _RPDUOutletSwitchedControlNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 1, 4, 1, 2),
    _RPDUOutletSwitchedControlNumber_Type()
)
rPDUOutletSwitchedControlNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUOutletSwitchedControlNumber.setStatus("mandatory")
_RPDUOutletSwitchedControlName_Type = DisplayString
_RPDUOutletSwitchedControlName_Object = MibTableColumn
rPDUOutletSwitchedControlName = _RPDUOutletSwitchedControlName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 1, 4, 1, 3),
    _RPDUOutletSwitchedControlName_Type()
)
rPDUOutletSwitchedControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDUOutletSwitchedControlName.setStatus("mandatory")


class _RPDUOutletSwitchedControlCmd_Type(Integer32):
    """Custom type rPDUOutletSwitchedControlCmd based on Integer32"""
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
        *(("outletOff", 2),
          ("outletOffWithDelay", 6),
          ("outletOn", 1),
          ("outletOnWithDelay", 5),
          ("outletReboot", 3),
          ("outletRebootWithDelay", 7),
          ("outletUnknown", 4))
    )


_RPDUOutletSwitchedControlCmd_Type.__name__ = "Integer32"
_RPDUOutletSwitchedControlCmd_Object = MibTableColumn
rPDUOutletSwitchedControlCmd = _RPDUOutletSwitchedControlCmd_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 1, 4, 1, 4),
    _RPDUOutletSwitchedControlCmd_Type()
)
rPDUOutletSwitchedControlCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDUOutletSwitchedControlCmd.setStatus("mandatory")
_RPDUOutletMetered_ObjectIdentity = ObjectIdentity
rPDUOutletMetered = _RPDUOutletMetered_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 2)
)
_RPDUOutletMeteredTableSize_Type = Integer32
_RPDUOutletMeteredTableSize_Object = MibScalar
rPDUOutletMeteredTableSize = _RPDUOutletMeteredTableSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 2, 1),
    _RPDUOutletMeteredTableSize_Type()
)
rPDUOutletMeteredTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUOutletMeteredTableSize.setStatus("mandatory")
_RPDUOutletMeteredStatusTable_Object = MibTable
rPDUOutletMeteredStatusTable = _RPDUOutletMeteredStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 2, 2)
)
if mibBuilder.loadTexts:
    rPDUOutletMeteredStatusTable.setStatus("mandatory")
_RPDUOutletMeteredStatusEntry_Object = MibTableRow
rPDUOutletMeteredStatusEntry = _RPDUOutletMeteredStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 2, 2, 1)
)
rPDUOutletMeteredStatusEntry.setIndexNames(
    (0, "DellrPDU-MIB", "rPDUOutletMeteredStatusIndex"),
)
if mibBuilder.loadTexts:
    rPDUOutletMeteredStatusEntry.setStatus("mandatory")
_RPDUOutletMeteredStatusIndex_Type = Integer32
_RPDUOutletMeteredStatusIndex_Object = MibTableColumn
rPDUOutletMeteredStatusIndex = _RPDUOutletMeteredStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 2, 2, 1, 1),
    _RPDUOutletMeteredStatusIndex_Type()
)
rPDUOutletMeteredStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUOutletMeteredStatusIndex.setStatus("mandatory")
_RPDUOutletMeteredStatusNumber_Type = Integer32
_RPDUOutletMeteredStatusNumber_Object = MibTableColumn
rPDUOutletMeteredStatusNumber = _RPDUOutletMeteredStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 2, 2, 1, 2),
    _RPDUOutletMeteredStatusNumber_Type()
)
rPDUOutletMeteredStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUOutletMeteredStatusNumber.setStatus("mandatory")
_RPDUOutletMeteredStatusName_Type = DisplayString
_RPDUOutletMeteredStatusName_Object = MibTableColumn
rPDUOutletMeteredStatusName = _RPDUOutletMeteredStatusName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 2, 2, 1, 3),
    _RPDUOutletMeteredStatusName_Type()
)
rPDUOutletMeteredStatusName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDUOutletMeteredStatusName.setStatus("mandatory")
_RPDUOutletMeteredStatusLayout_Type = RpduOutletPhaseLayoutType
_RPDUOutletMeteredStatusLayout_Object = MibTableColumn
rPDUOutletMeteredStatusLayout = _RPDUOutletMeteredStatusLayout_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 2, 2, 1, 4),
    _RPDUOutletMeteredStatusLayout_Type()
)
rPDUOutletMeteredStatusLayout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUOutletMeteredStatusLayout.setStatus("mandatory")
_RPDUOutMeteredStatPowerRating_Type = Integer32
_RPDUOutMeteredStatPowerRating_Object = MibTableColumn
rPDUOutMeteredStatPowerRating = _RPDUOutMeteredStatPowerRating_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 2, 2, 1, 5),
    _RPDUOutMeteredStatPowerRating_Type()
)
rPDUOutMeteredStatPowerRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUOutMeteredStatPowerRating.setStatus("mandatory")
_RPDUOutletMeteredStatusCurrent_Type = Integer32
_RPDUOutletMeteredStatusCurrent_Object = MibTableColumn
rPDUOutletMeteredStatusCurrent = _RPDUOutletMeteredStatusCurrent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 2, 2, 1, 6),
    _RPDUOutletMeteredStatusCurrent_Type()
)
rPDUOutletMeteredStatusCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUOutletMeteredStatusCurrent.setStatus("mandatory")
_RPDUOutletMeteredStatusEnergy_Type = Integer32
_RPDUOutletMeteredStatusEnergy_Object = MibTableColumn
rPDUOutletMeteredStatusEnergy = _RPDUOutletMeteredStatusEnergy_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 2, 2, 1, 7),
    _RPDUOutletMeteredStatusEnergy_Type()
)
rPDUOutletMeteredStatusEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUOutletMeteredStatusEnergy.setStatus("mandatory")
_RPDUOutletMeteredStatusPower_Type = Integer32
_RPDUOutletMeteredStatusPower_Object = MibTableColumn
rPDUOutletMeteredStatusPower = _RPDUOutletMeteredStatusPower_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 2, 2, 1, 8),
    _RPDUOutletMeteredStatusPower_Type()
)
rPDUOutletMeteredStatusPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUOutletMeteredStatusPower.setStatus("mandatory")
_RPDUOutletMeteredStatPeakPower_Type = Integer32
_RPDUOutletMeteredStatPeakPower_Object = MibTableColumn
rPDUOutletMeteredStatPeakPower = _RPDUOutletMeteredStatPeakPower_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 2, 2, 1, 9),
    _RPDUOutletMeteredStatPeakPower_Type()
)
rPDUOutletMeteredStatPeakPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUOutletMeteredStatPeakPower.setStatus("mandatory")
_RPDUOutMeteredStatPeakPwrTime_Type = DisplayString
_RPDUOutMeteredStatPeakPwrTime_Object = MibTableColumn
rPDUOutMeteredStatPeakPwrTime = _RPDUOutMeteredStatPeakPwrTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 2, 2, 1, 10),
    _RPDUOutMeteredStatPeakPwrTime_Type()
)
rPDUOutMeteredStatPeakPwrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUOutMeteredStatPeakPwrTime.setStatus("mandatory")
_RPDUOutMeteredStatusLoadState_Type = RpduLowNormalNearOverloadType
_RPDUOutMeteredStatusLoadState_Object = MibTableColumn
rPDUOutMeteredStatusLoadState = _RPDUOutMeteredStatusLoadState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 2, 2, 1, 11),
    _RPDUOutMeteredStatusLoadState_Type()
)
rPDUOutMeteredStatusLoadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUOutMeteredStatusLoadState.setStatus("mandatory")
_RPDUOutletMeteredConfigTable_Object = MibTable
rPDUOutletMeteredConfigTable = _RPDUOutletMeteredConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 2, 4)
)
if mibBuilder.loadTexts:
    rPDUOutletMeteredConfigTable.setStatus("mandatory")
_RPDUOutletMeteredConfigEntry_Object = MibTableRow
rPDUOutletMeteredConfigEntry = _RPDUOutletMeteredConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 2, 4, 1)
)
rPDUOutletMeteredConfigEntry.setIndexNames(
    (0, "DellrPDU-MIB", "rPDUOutletMeteredConfigIndex"),
)
if mibBuilder.loadTexts:
    rPDUOutletMeteredConfigEntry.setStatus("mandatory")
_RPDUOutletMeteredConfigIndex_Type = Integer32
_RPDUOutletMeteredConfigIndex_Object = MibTableColumn
rPDUOutletMeteredConfigIndex = _RPDUOutletMeteredConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 2, 4, 1, 1),
    _RPDUOutletMeteredConfigIndex_Type()
)
rPDUOutletMeteredConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUOutletMeteredConfigIndex.setStatus("mandatory")
_RPDUOutletMeteredConfigNumber_Type = Integer32
_RPDUOutletMeteredConfigNumber_Object = MibTableColumn
rPDUOutletMeteredConfigNumber = _RPDUOutletMeteredConfigNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 2, 4, 1, 2),
    _RPDUOutletMeteredConfigNumber_Type()
)
rPDUOutletMeteredConfigNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUOutletMeteredConfigNumber.setStatus("mandatory")
_RPDUOutletMeteredConfigName_Type = DisplayString
_RPDUOutletMeteredConfigName_Object = MibTableColumn
rPDUOutletMeteredConfigName = _RPDUOutletMeteredConfigName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 2, 4, 1, 3),
    _RPDUOutletMeteredConfigName_Type()
)
rPDUOutletMeteredConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDUOutletMeteredConfigName.setStatus("mandatory")
_RPDUOutMtredCfgLowLdCurntThresh_Type = Integer32
_RPDUOutMtredCfgLowLdCurntThresh_Object = MibTableColumn
rPDUOutMtredCfgLowLdCurntThresh = _RPDUOutMtredCfgLowLdCurntThresh_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 2, 4, 1, 4),
    _RPDUOutMtredCfgLowLdCurntThresh_Type()
)
rPDUOutMtredCfgLowLdCurntThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDUOutMtredCfgLowLdCurntThresh.setStatus("mandatory")
_RPDUOutMtrdCfgNrOvdCurntThresh_Type = Integer32
_RPDUOutMtrdCfgNrOvdCurntThresh_Object = MibTableColumn
rPDUOutMtrdCfgNrOvdCurntThresh = _RPDUOutMtrdCfgNrOvdCurntThresh_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 2, 4, 1, 5),
    _RPDUOutMtrdCfgNrOvdCurntThresh_Type()
)
rPDUOutMtrdCfgNrOvdCurntThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDUOutMtrdCfgNrOvdCurntThresh.setStatus("mandatory")
_RPDUOutMtredCfgOvrldCurntThresh_Type = Integer32
_RPDUOutMtredCfgOvrldCurntThresh_Object = MibTableColumn
rPDUOutMtredCfgOvrldCurntThresh = _RPDUOutMtredCfgOvrldCurntThresh_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 2, 4, 1, 6),
    _RPDUOutMtredCfgOvrldCurntThresh_Type()
)
rPDUOutMtredCfgOvrldCurntThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDUOutMtredCfgOvrldCurntThresh.setStatus("mandatory")
_RPDUOutMeteredEnergyStartTime_Type = DisplayString
_RPDUOutMeteredEnergyStartTime_Object = MibScalar
rPDUOutMeteredEnergyStartTime = _RPDUOutMeteredEnergyStartTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 2, 5),
    _RPDUOutMeteredEnergyStartTime_Type()
)
rPDUOutMeteredEnergyStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUOutMeteredEnergyStartTime.setStatus("mandatory")
_RPDUOutMeteredPeakPwrStartTime_Type = DisplayString
_RPDUOutMeteredPeakPwrStartTime_Object = MibScalar
rPDUOutMeteredPeakPwrStartTime = _RPDUOutMeteredPeakPwrStartTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 130, 2, 6),
    _RPDUOutMeteredPeakPwrStartTime_Type()
)
rPDUOutMeteredPeakPwrStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUOutMeteredPeakPwrStartTime.setStatus("mandatory")
_RPDUPowerSupply_ObjectIdentity = ObjectIdentity
rPDUPowerSupply = _RPDUPowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 140)
)


class _RPDUPowerSupplyAlarmD_Type(Integer32):
    """Custom type rPDUPowerSupplyAlarmD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allAvailablePowerSuppliesOK", 1),
          ("powerSupplyFailed", 2))
    )


_RPDUPowerSupplyAlarmD_Type.__name__ = "Integer32"
_RPDUPowerSupplyAlarmD_Object = MibScalar
rPDUPowerSupplyAlarmD = _RPDUPowerSupplyAlarmD_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 140, 1),
    _RPDUPowerSupplyAlarmD_Type()
)
rPDUPowerSupplyAlarmD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUPowerSupplyAlarmD.setStatus("mandatory")
_RPDUPowerSupplyVoltage_Type = Integer32
_RPDUPowerSupplyVoltage_Object = MibScalar
rPDUPowerSupplyVoltage = _RPDUPowerSupplyVoltage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 140, 2),
    _RPDUPowerSupplyVoltage_Type()
)
rPDUPowerSupplyVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUPowerSupplyVoltage.setStatus("mandatory")
_RPDUSensor_ObjectIdentity = ObjectIdentity
rPDUSensor = _RPDUSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150)
)
_RPDUSensorStatus_ObjectIdentity = ObjectIdentity
rPDUSensorStatus = _RPDUSensorStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 1)
)
_RPDUSensorStatusTableSize_Type = Integer32
_RPDUSensorStatusTableSize_Object = MibScalar
rPDUSensorStatusTableSize = _RPDUSensorStatusTableSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 1, 1),
    _RPDUSensorStatusTableSize_Type()
)
rPDUSensorStatusTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUSensorStatusTableSize.setStatus("mandatory")
_RPDUSensorStatusTable_Object = MibTable
rPDUSensorStatusTable = _RPDUSensorStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 1, 2)
)
if mibBuilder.loadTexts:
    rPDUSensorStatusTable.setStatus("mandatory")
_RPDUSensorStatusEntry_Object = MibTableRow
rPDUSensorStatusEntry = _RPDUSensorStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 1, 2, 1)
)
rPDUSensorStatusEntry.setIndexNames(
    (0, "DellrPDU-MIB", "rPDUSensorStatusIndex"),
)
if mibBuilder.loadTexts:
    rPDUSensorStatusEntry.setStatus("mandatory")
_RPDUSensorStatusIndex_Type = Integer32
_RPDUSensorStatusIndex_Object = MibTableColumn
rPDUSensorStatusIndex = _RPDUSensorStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 1, 2, 1, 1),
    _RPDUSensorStatusIndex_Type()
)
rPDUSensorStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUSensorStatusIndex.setStatus("mandatory")
_RPDUSensorStatusName_Type = DisplayString
_RPDUSensorStatusName_Object = MibTableColumn
rPDUSensorStatusName = _RPDUSensorStatusName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 1, 2, 1, 2),
    _RPDUSensorStatusName_Type()
)
rPDUSensorStatusName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDUSensorStatusName.setStatus("mandatory")


class _RPDUSensorStatusType_Type(Integer32):
    """Custom type rPDUSensorStatusType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("temperature", 2),
          ("temperatureHumidity", 3))
    )


_RPDUSensorStatusType_Type.__name__ = "Integer32"
_RPDUSensorStatusType_Object = MibTableColumn
rPDUSensorStatusType = _RPDUSensorStatusType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 1, 2, 1, 3),
    _RPDUSensorStatusType_Type()
)
rPDUSensorStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUSensorStatusType.setStatus("mandatory")
_RPDUSensorTemp_ObjectIdentity = ObjectIdentity
rPDUSensorTemp = _RPDUSensorTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 2)
)
_RPDUSensorTempTableSize_Type = Integer32
_RPDUSensorTempTableSize_Object = MibScalar
rPDUSensorTempTableSize = _RPDUSensorTempTableSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 2, 1),
    _RPDUSensorTempTableSize_Type()
)
rPDUSensorTempTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUSensorTempTableSize.setStatus("mandatory")
_RPDUSensorTempStatusTable_Object = MibTable
rPDUSensorTempStatusTable = _RPDUSensorTempStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 2, 2)
)
if mibBuilder.loadTexts:
    rPDUSensorTempStatusTable.setStatus("mandatory")
_RPDUSensorTempStatusEntry_Object = MibTableRow
rPDUSensorTempStatusEntry = _RPDUSensorTempStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 2, 2, 1)
)
rPDUSensorTempStatusEntry.setIndexNames(
    (0, "DellrPDU-MIB", "rPDUSensorTempStatusIndex"),
)
if mibBuilder.loadTexts:
    rPDUSensorTempStatusEntry.setStatus("mandatory")
_RPDUSensorTempStatusIndex_Type = Integer32
_RPDUSensorTempStatusIndex_Object = MibTableColumn
rPDUSensorTempStatusIndex = _RPDUSensorTempStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 2, 2, 1, 1),
    _RPDUSensorTempStatusIndex_Type()
)
rPDUSensorTempStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUSensorTempStatusIndex.setStatus("mandatory")
_RPDUSensorTempStatusName_Type = DisplayString
_RPDUSensorTempStatusName_Object = MibTableColumn
rPDUSensorTempStatusName = _RPDUSensorTempStatusName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 2, 2, 1, 2),
    _RPDUSensorTempStatusName_Type()
)
rPDUSensorTempStatusName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDUSensorTempStatusName.setStatus("mandatory")
_RPDUSensorTempStatusCommStatus_Type = RpduCommNoneOKLostType
_RPDUSensorTempStatusCommStatus_Object = MibTableColumn
rPDUSensorTempStatusCommStatus = _RPDUSensorTempStatusCommStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 2, 2, 1, 3),
    _RPDUSensorTempStatusCommStatus_Type()
)
rPDUSensorTempStatusCommStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUSensorTempStatusCommStatus.setStatus("mandatory")
_RPDUSensorTempStatusTempF_Type = Integer32
_RPDUSensorTempStatusTempF_Object = MibTableColumn
rPDUSensorTempStatusTempF = _RPDUSensorTempStatusTempF_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 2, 2, 1, 4),
    _RPDUSensorTempStatusTempF_Type()
)
rPDUSensorTempStatusTempF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUSensorTempStatusTempF.setStatus("mandatory")
_RPDUSensorTempStatusTempC_Type = Integer32
_RPDUSensorTempStatusTempC_Object = MibTableColumn
rPDUSensorTempStatusTempC = _RPDUSensorTempStatusTempC_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 2, 2, 1, 5),
    _RPDUSensorTempStatusTempC_Type()
)
rPDUSensorTempStatusTempC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUSensorTempStatusTempC.setStatus("mandatory")
_RPDUSensorTempStatusAlarmStatus_Type = RpduNotPBMinLowNrmlOHiMaxType
_RPDUSensorTempStatusAlarmStatus_Object = MibTableColumn
rPDUSensorTempStatusAlarmStatus = _RPDUSensorTempStatusAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 2, 2, 1, 6),
    _RPDUSensorTempStatusAlarmStatus_Type()
)
rPDUSensorTempStatusAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUSensorTempStatusAlarmStatus.setStatus("mandatory")
_RPDUSensorTempConfigTable_Object = MibTable
rPDUSensorTempConfigTable = _RPDUSensorTempConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 2, 3)
)
if mibBuilder.loadTexts:
    rPDUSensorTempConfigTable.setStatus("mandatory")
_RPDUSensorTempConfigEntry_Object = MibTableRow
rPDUSensorTempConfigEntry = _RPDUSensorTempConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 2, 3, 1)
)
rPDUSensorTempConfigEntry.setIndexNames(
    (0, "DellrPDU-MIB", "rPDUSensorTempConfigIndex"),
)
if mibBuilder.loadTexts:
    rPDUSensorTempConfigEntry.setStatus("mandatory")
_RPDUSensorTempConfigIndex_Type = Integer32
_RPDUSensorTempConfigIndex_Object = MibTableColumn
rPDUSensorTempConfigIndex = _RPDUSensorTempConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 2, 3, 1, 1),
    _RPDUSensorTempConfigIndex_Type()
)
rPDUSensorTempConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUSensorTempConfigIndex.setStatus("mandatory")
_RPDUSensorTempConfigName_Type = DisplayString
_RPDUSensorTempConfigName_Object = MibTableColumn
rPDUSensorTempConfigName = _RPDUSensorTempConfigName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 2, 3, 1, 2),
    _RPDUSensorTempConfigName_Type()
)
rPDUSensorTempConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDUSensorTempConfigName.setStatus("mandatory")
_RPDUSensorTempCfgTempMaxThreshF_Type = Integer32
_RPDUSensorTempCfgTempMaxThreshF_Object = MibTableColumn
rPDUSensorTempCfgTempMaxThreshF = _RPDUSensorTempCfgTempMaxThreshF_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 2, 3, 1, 3),
    _RPDUSensorTempCfgTempMaxThreshF_Type()
)
rPDUSensorTempCfgTempMaxThreshF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDUSensorTempCfgTempMaxThreshF.setStatus("mandatory")
_RPDUSnsorTempCfgTempHighThreshF_Type = Integer32
_RPDUSnsorTempCfgTempHighThreshF_Object = MibTableColumn
rPDUSnsorTempCfgTempHighThreshF = _RPDUSnsorTempCfgTempHighThreshF_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 2, 3, 1, 4),
    _RPDUSnsorTempCfgTempHighThreshF_Type()
)
rPDUSnsorTempCfgTempHighThreshF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDUSnsorTempCfgTempHighThreshF.setStatus("mandatory")
_RPDUSnsorTempCfgTempHysteresisF_Type = Integer32
_RPDUSnsorTempCfgTempHysteresisF_Object = MibTableColumn
rPDUSnsorTempCfgTempHysteresisF = _RPDUSnsorTempCfgTempHysteresisF_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 2, 3, 1, 5),
    _RPDUSnsorTempCfgTempHysteresisF_Type()
)
rPDUSnsorTempCfgTempHysteresisF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDUSnsorTempCfgTempHysteresisF.setStatus("mandatory")
_RPDUSensorTempCfgTempMaxThreshC_Type = Integer32
_RPDUSensorTempCfgTempMaxThreshC_Object = MibTableColumn
rPDUSensorTempCfgTempMaxThreshC = _RPDUSensorTempCfgTempMaxThreshC_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 2, 3, 1, 6),
    _RPDUSensorTempCfgTempMaxThreshC_Type()
)
rPDUSensorTempCfgTempMaxThreshC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDUSensorTempCfgTempMaxThreshC.setStatus("mandatory")
_RPDUSnsorTempCfgTempHighThreshC_Type = Integer32
_RPDUSnsorTempCfgTempHighThreshC_Object = MibTableColumn
rPDUSnsorTempCfgTempHighThreshC = _RPDUSnsorTempCfgTempHighThreshC_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 2, 3, 1, 7),
    _RPDUSnsorTempCfgTempHighThreshC_Type()
)
rPDUSnsorTempCfgTempHighThreshC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDUSnsorTempCfgTempHighThreshC.setStatus("mandatory")
_RPDUSnsorTempCfgTempHysteresisC_Type = Integer32
_RPDUSnsorTempCfgTempHysteresisC_Object = MibTableColumn
rPDUSnsorTempCfgTempHysteresisC = _RPDUSnsorTempCfgTempHysteresisC_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 2, 3, 1, 8),
    _RPDUSnsorTempCfgTempHysteresisC_Type()
)
rPDUSnsorTempCfgTempHysteresisC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDUSnsorTempCfgTempHysteresisC.setStatus("mandatory")
_RPDUSnsorTempCfgAlarmGeneration_Type = RpduEnableDisableType
_RPDUSnsorTempCfgAlarmGeneration_Object = MibTableColumn
rPDUSnsorTempCfgAlarmGeneration = _RPDUSnsorTempCfgAlarmGeneration_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 2, 3, 1, 9),
    _RPDUSnsorTempCfgAlarmGeneration_Type()
)
rPDUSnsorTempCfgAlarmGeneration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDUSnsorTempCfgAlarmGeneration.setStatus("mandatory")
_RPDUSensorHumidity_ObjectIdentity = ObjectIdentity
rPDUSensorHumidity = _RPDUSensorHumidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 3)
)
_RPDUSensorHumidityTableSize_Type = Integer32
_RPDUSensorHumidityTableSize_Object = MibScalar
rPDUSensorHumidityTableSize = _RPDUSensorHumidityTableSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 3, 1),
    _RPDUSensorHumidityTableSize_Type()
)
rPDUSensorHumidityTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUSensorHumidityTableSize.setStatus("mandatory")
_RPDUSensorHumidityStatusTable_Object = MibTable
rPDUSensorHumidityStatusTable = _RPDUSensorHumidityStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 3, 2)
)
if mibBuilder.loadTexts:
    rPDUSensorHumidityStatusTable.setStatus("mandatory")
_RPDUSensorHumidityStatusEntry_Object = MibTableRow
rPDUSensorHumidityStatusEntry = _RPDUSensorHumidityStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 3, 2, 1)
)
rPDUSensorHumidityStatusEntry.setIndexNames(
    (0, "DellrPDU-MIB", "rPDUSensorHumidityStatusIndex"),
)
if mibBuilder.loadTexts:
    rPDUSensorHumidityStatusEntry.setStatus("mandatory")
_RPDUSensorHumidityStatusIndex_Type = Integer32
_RPDUSensorHumidityStatusIndex_Object = MibTableColumn
rPDUSensorHumidityStatusIndex = _RPDUSensorHumidityStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 3, 2, 1, 1),
    _RPDUSensorHumidityStatusIndex_Type()
)
rPDUSensorHumidityStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUSensorHumidityStatusIndex.setStatus("mandatory")
_RPDUSensorHumidityStatusName_Type = DisplayString
_RPDUSensorHumidityStatusName_Object = MibTableColumn
rPDUSensorHumidityStatusName = _RPDUSensorHumidityStatusName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 3, 2, 1, 2),
    _RPDUSensorHumidityStatusName_Type()
)
rPDUSensorHumidityStatusName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDUSensorHumidityStatusName.setStatus("mandatory")
_RPDUSnsorHumidityStatCommStatus_Type = RpduCommNoneOKLostType
_RPDUSnsorHumidityStatCommStatus_Object = MibTableColumn
rPDUSnsorHumidityStatCommStatus = _RPDUSnsorHumidityStatCommStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 3, 2, 1, 3),
    _RPDUSnsorHumidityStatCommStatus_Type()
)
rPDUSnsorHumidityStatCommStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUSnsorHumidityStatCommStatus.setStatus("mandatory")
_RPDUSnsorHumStatRelativeHumdity_Type = Integer32
_RPDUSnsorHumStatRelativeHumdity_Object = MibTableColumn
rPDUSnsorHumStatRelativeHumdity = _RPDUSnsorHumStatRelativeHumdity_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 3, 2, 1, 4),
    _RPDUSnsorHumStatRelativeHumdity_Type()
)
rPDUSnsorHumStatRelativeHumdity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUSnsorHumStatRelativeHumdity.setStatus("mandatory")
_RPDUSnsorHumStatusAlarmStatus_Type = RpduNotPBMinLowNrmlOHiMaxType
_RPDUSnsorHumStatusAlarmStatus_Object = MibTableColumn
rPDUSnsorHumStatusAlarmStatus = _RPDUSnsorHumStatusAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 3, 2, 1, 5),
    _RPDUSnsorHumStatusAlarmStatus_Type()
)
rPDUSnsorHumStatusAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUSnsorHumStatusAlarmStatus.setStatus("mandatory")
_RPDUSensorHumidityConfigTable_Object = MibTable
rPDUSensorHumidityConfigTable = _RPDUSensorHumidityConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 3, 3)
)
if mibBuilder.loadTexts:
    rPDUSensorHumidityConfigTable.setStatus("mandatory")
_RPDUSensorHumidityConfigEntry_Object = MibTableRow
rPDUSensorHumidityConfigEntry = _RPDUSensorHumidityConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 3, 3, 1)
)
rPDUSensorHumidityConfigEntry.setIndexNames(
    (0, "DellrPDU-MIB", "rPDUSensorHumidityConfigIndex"),
)
if mibBuilder.loadTexts:
    rPDUSensorHumidityConfigEntry.setStatus("mandatory")
_RPDUSensorHumidityConfigIndex_Type = Integer32
_RPDUSensorHumidityConfigIndex_Object = MibTableColumn
rPDUSensorHumidityConfigIndex = _RPDUSensorHumidityConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 3, 3, 1, 1),
    _RPDUSensorHumidityConfigIndex_Type()
)
rPDUSensorHumidityConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUSensorHumidityConfigIndex.setStatus("mandatory")
_RPDUSensorHumidityConfigName_Type = DisplayString
_RPDUSensorHumidityConfigName_Object = MibTableColumn
rPDUSensorHumidityConfigName = _RPDUSensorHumidityConfigName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 3, 3, 1, 2),
    _RPDUSensorHumidityConfigName_Type()
)
rPDUSensorHumidityConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDUSensorHumidityConfigName.setStatus("mandatory")
_RPDUSnsorHumCfgHumdityLowThresh_Type = Integer32
_RPDUSnsorHumCfgHumdityLowThresh_Object = MibTableColumn
rPDUSnsorHumCfgHumdityLowThresh = _RPDUSnsorHumCfgHumdityLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 3, 3, 1, 3),
    _RPDUSnsorHumCfgHumdityLowThresh_Type()
)
rPDUSnsorHumCfgHumdityLowThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDUSnsorHumCfgHumdityLowThresh.setStatus("mandatory")
_RPDUSnsorHumCfgHumdityMinThresh_Type = Integer32
_RPDUSnsorHumCfgHumdityMinThresh_Object = MibTableColumn
rPDUSnsorHumCfgHumdityMinThresh = _RPDUSnsorHumCfgHumdityMinThresh_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 3, 3, 1, 4),
    _RPDUSnsorHumCfgHumdityMinThresh_Type()
)
rPDUSnsorHumCfgHumdityMinThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDUSnsorHumCfgHumdityMinThresh.setStatus("mandatory")
_RPDUSnsorHumCfgHumdtyHysteresis_Type = Integer32
_RPDUSnsorHumCfgHumdtyHysteresis_Object = MibTableColumn
rPDUSnsorHumCfgHumdtyHysteresis = _RPDUSnsorHumCfgHumdtyHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 3, 3, 1, 5),
    _RPDUSnsorHumCfgHumdtyHysteresis_Type()
)
rPDUSnsorHumCfgHumdtyHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDUSnsorHumCfgHumdtyHysteresis.setStatus("mandatory")
_RPDUSnsorHumCfgAlarmGeneration_Type = RpduEnableDisableType
_RPDUSnsorHumCfgAlarmGeneration_Object = MibTableColumn
rPDUSnsorHumCfgAlarmGeneration = _RPDUSnsorHumCfgAlarmGeneration_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 3, 3, 1, 6),
    _RPDUSnsorHumCfgAlarmGeneration_Type()
)
rPDUSnsorHumCfgAlarmGeneration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDUSnsorHumCfgAlarmGeneration.setStatus("mandatory")
_RPDUSensorDiscrete_ObjectIdentity = ObjectIdentity
rPDUSensorDiscrete = _RPDUSensorDiscrete_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 4)
)
_RPDUSensorDiscreteTableSize_Type = Integer32
_RPDUSensorDiscreteTableSize_Object = MibScalar
rPDUSensorDiscreteTableSize = _RPDUSensorDiscreteTableSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 4, 1),
    _RPDUSensorDiscreteTableSize_Type()
)
rPDUSensorDiscreteTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUSensorDiscreteTableSize.setStatus("mandatory")
_RPDUSensorDiscreteStatusTable_Object = MibTable
rPDUSensorDiscreteStatusTable = _RPDUSensorDiscreteStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 4, 2)
)
if mibBuilder.loadTexts:
    rPDUSensorDiscreteStatusTable.setStatus("mandatory")
_RPDUSensorDiscreteStatusEntry_Object = MibTableRow
rPDUSensorDiscreteStatusEntry = _RPDUSensorDiscreteStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 4, 2, 1)
)
rPDUSensorDiscreteStatusEntry.setIndexNames(
    (0, "DellrPDU-MIB", "rPDUSensorDiscreteStatusIndex"),
)
if mibBuilder.loadTexts:
    rPDUSensorDiscreteStatusEntry.setStatus("mandatory")
_RPDUSensorDiscreteStatusIndex_Type = Integer32
_RPDUSensorDiscreteStatusIndex_Object = MibTableColumn
rPDUSensorDiscreteStatusIndex = _RPDUSensorDiscreteStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 4, 2, 1, 1),
    _RPDUSensorDiscreteStatusIndex_Type()
)
rPDUSensorDiscreteStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUSensorDiscreteStatusIndex.setStatus("mandatory")
_RPDUSensorDiscreteStatusName_Type = DisplayString
_RPDUSensorDiscreteStatusName_Object = MibTableColumn
rPDUSensorDiscreteStatusName = _RPDUSensorDiscreteStatusName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 4, 2, 1, 2),
    _RPDUSensorDiscreteStatusName_Type()
)
rPDUSensorDiscreteStatusName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDUSensorDiscreteStatusName.setStatus("mandatory")


class _RPDUSnsorDiscreteStatCurntState_Type(Integer32):
    """Custom type rPDUSnsorDiscreteStatCurntState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("open", 1),
          ("unknown", 3))
    )


_RPDUSnsorDiscreteStatCurntState_Type.__name__ = "Integer32"
_RPDUSnsorDiscreteStatCurntState_Object = MibTableColumn
rPDUSnsorDiscreteStatCurntState = _RPDUSnsorDiscreteStatCurntState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 4, 2, 1, 3),
    _RPDUSnsorDiscreteStatCurntState_Type()
)
rPDUSnsorDiscreteStatCurntState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUSnsorDiscreteStatCurntState.setStatus("mandatory")
_RPDUSnsorDiscreteStatAlarmState_Type = RpduNormalAlarmType
_RPDUSnsorDiscreteStatAlarmState_Object = MibTableColumn
rPDUSnsorDiscreteStatAlarmState = _RPDUSnsorDiscreteStatAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 4, 2, 1, 4),
    _RPDUSnsorDiscreteStatAlarmState_Type()
)
rPDUSnsorDiscreteStatAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUSnsorDiscreteStatAlarmState.setStatus("mandatory")
_RPDUSensorDiscreteConfigTable_Object = MibTable
rPDUSensorDiscreteConfigTable = _RPDUSensorDiscreteConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 4, 3)
)
if mibBuilder.loadTexts:
    rPDUSensorDiscreteConfigTable.setStatus("mandatory")
_RPDUSensorDiscreteConfigEntry_Object = MibTableRow
rPDUSensorDiscreteConfigEntry = _RPDUSensorDiscreteConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 4, 3, 1)
)
rPDUSensorDiscreteConfigEntry.setIndexNames(
    (0, "DellrPDU-MIB", "rPDUSensorDiscreteConfigIndex"),
)
if mibBuilder.loadTexts:
    rPDUSensorDiscreteConfigEntry.setStatus("mandatory")
_RPDUSensorDiscreteConfigIndex_Type = Integer32
_RPDUSensorDiscreteConfigIndex_Object = MibTableColumn
rPDUSensorDiscreteConfigIndex = _RPDUSensorDiscreteConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 4, 3, 1, 1),
    _RPDUSensorDiscreteConfigIndex_Type()
)
rPDUSensorDiscreteConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPDUSensorDiscreteConfigIndex.setStatus("mandatory")
_RPDUSensorDiscreteConfigName_Type = DisplayString
_RPDUSensorDiscreteConfigName_Object = MibTableColumn
rPDUSensorDiscreteConfigName = _RPDUSensorDiscreteConfigName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 4, 3, 1, 2),
    _RPDUSensorDiscreteConfigName_Type()
)
rPDUSensorDiscreteConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDUSensorDiscreteConfigName.setStatus("mandatory")


class _RPDUSnsorDiscreteCfgNormalState_Type(Integer32):
    """Custom type rPDUSnsorDiscreteCfgNormalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("open", 1))
    )


_RPDUSnsorDiscreteCfgNormalState_Type.__name__ = "Integer32"
_RPDUSnsorDiscreteCfgNormalState_Object = MibTableColumn
rPDUSnsorDiscreteCfgNormalState = _RPDUSnsorDiscreteCfgNormalState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 4, 3, 1, 3),
    _RPDUSnsorDiscreteCfgNormalState_Type()
)
rPDUSnsorDiscreteCfgNormalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDUSnsorDiscreteCfgNormalState.setStatus("mandatory")
_RPDUSnsorDiscrteAlarmGeneration_Type = RpduEnableDisableType
_RPDUSnsorDiscrteAlarmGeneration_Object = MibTableColumn
rPDUSnsorDiscrteAlarmGeneration = _RPDUSnsorDiscrteAlarmGeneration_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 150, 4, 3, 1, 4),
    _RPDUSnsorDiscrteAlarmGeneration_Type()
)
rPDUSnsorDiscrteAlarmGeneration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDUSnsorDiscrteAlarmGeneration.setStatus("mandatory")
_MtrapargsD_ObjectIdentity = ObjectIdentity
mtrapargsD = _MtrapargsD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 160)
)
_ContactNumber_Type = Integer32
_ContactNumber_Object = MibScalar
contactNumber = _ContactNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 160, 1),
    _ContactNumber_Type()
)
contactNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contactNumber.setStatus("mandatory")
_OutletNumber_Type = Integer32
_OutletNumber_Object = MibScalar
outletNumber = _OutletNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 160, 2),
    _OutletNumber_Type()
)
outletNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletNumber.setStatus("mandatory")
_MtrapargsString_Type = DisplayString
_MtrapargsString_Object = MibScalar
mtrapargsString = _MtrapargsString_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 160, 3),
    _MtrapargsString_Type()
)
mtrapargsString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtrapargsString.setStatus("mandatory")
_PhaseNumber_Type = Integer32
_PhaseNumber_Object = MibScalar
phaseNumber = _PhaseNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 160, 4),
    _PhaseNumber_Type()
)
phaseNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phaseNumber.setStatus("mandatory")
_SensorNumber_Type = Integer32
_SensorNumber_Object = MibScalar
sensorNumber = _SensorNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 160, 5),
    _SensorNumber_Type()
)
sensorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorNumber.setStatus("mandatory")
_DeviceNameD_Type = DisplayString
_DeviceNameD_Object = MibScalar
deviceNameD = _DeviceNameD_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 160, 6),
    _DeviceNameD_Type()
)
deviceNameD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceNameD.setStatus("mandatory")
_SerialNumber_Type = DisplayString
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 160, 7),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("mandatory")
_TestTrapargsInteger_Type = Integer32
_TestTrapargsInteger_Object = MibScalar
testTrapargsInteger = _TestTrapargsInteger_Object(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 160, 8),
    _TestTrapargsInteger_Type()
)
testTrapargsInteger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testTrapargsInteger.setStatus("mandatory")
_Events_ObjectIdentity = ObjectIdentity
events = _Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 3)
)
_SysRPDUV1_ObjectIdentity = ObjectIdentity
sysRPDUV1 = _SysRPDUV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 3, 1)
)

# Managed Objects groups


# Notification objects

deviceCommunicationLostCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 1)
)
deviceCommunicationLostCleared.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    deviceCommunicationLostCleared.setStatus(
        ""
    )

deviceCommunicationLostSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 2)
)
deviceCommunicationLostSet.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    deviceCommunicationLostSet.setStatus(
        ""
    )

componentCommLostCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 3)
)
componentCommLostCleared.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    componentCommLostCleared.setStatus(
        ""
    )

componentCommLostSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 4)
)
componentCommLostSet.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    componentCommLostSet.setStatus(
        ""
    )

cANBusOffCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 5)
)
cANBusOffCleared.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    cANBusOffCleared.setStatus(
        ""
    )

canBusOffSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 6)
)
canBusOffSet.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    canBusOffSet.setStatus(
        ""
    )

powerSupplyFailureCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 7)
)
powerSupplyFailureCleared.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    powerSupplyFailureCleared.setStatus(
        ""
    )

powerSupplyFailureSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 8)
)
powerSupplyFailureSet.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    powerSupplyFailureSet.setStatus(
        ""
    )

keypadButtonStuckCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 9)
)
keypadButtonStuckCleared.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    keypadButtonStuckCleared.setStatus(
        ""
    )

keypadButtonStuckSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 10)
)
keypadButtonStuckSet.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    keypadButtonStuckSet.setStatus(
        ""
    )

dryContactAbnormalCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 11)
)
dryContactAbnormalCleared.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "contactNumber"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    dryContactAbnormalCleared.setStatus(
        ""
    )

dryContactAbnormalSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 12)
)
dryContactAbnormalSet.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "contactNumber"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    dryContactAbnormalSet.setStatus(
        ""
    )

deviceLowLoadCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 13)
)
deviceLowLoadCleared.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    deviceLowLoadCleared.setStatus(
        ""
    )

deviceLowLoadSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 14)
)
deviceLowLoadSet.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    deviceLowLoadSet.setStatus(
        ""
    )

deviceNearOverLoadCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 15)
)
deviceNearOverLoadCleared.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    deviceNearOverLoadCleared.setStatus(
        ""
    )

deviceNearOverLoadSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 16)
)
deviceNearOverLoadSet.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    deviceNearOverLoadSet.setStatus(
        ""
    )

deviceOverLoadCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 17)
)
deviceOverLoadCleared.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    deviceOverLoadCleared.setStatus(
        ""
    )

deviceOverLoadSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 18)
)
deviceOverLoadSet.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    deviceOverLoadSet.setStatus(
        ""
    )

phaseLowLoadCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 19)
)
phaseLowLoadCleared.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "phaseNumber"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    phaseLowLoadCleared.setStatus(
        ""
    )

phaseLowLoadSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 20)
)
phaseLowLoadSet.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "phaseNumber"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    phaseLowLoadSet.setStatus(
        ""
    )

phaseNearOverLoadCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 21)
)
phaseNearOverLoadCleared.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "phaseNumber"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    phaseNearOverLoadCleared.setStatus(
        ""
    )

phaseNearOverLoadSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 22)
)
phaseNearOverLoadSet.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "phaseNumber"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    phaseNearOverLoadSet.setStatus(
        ""
    )

phaseOverLoadCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 23)
)
phaseOverLoadCleared.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "phaseNumber"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    phaseOverLoadCleared.setStatus(
        ""
    )

phaseOverLoadSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 24)
)
phaseOverLoadSet.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "phaseNumber"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    phaseOverLoadSet.setStatus(
        ""
    )

outletLowLoadCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 25)
)
outletLowLoadCleared.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "outletNumber"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    outletLowLoadCleared.setStatus(
        ""
    )

outletLowLoadSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 26)
)
outletLowLoadSet.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "outletNumber"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    outletLowLoadSet.setStatus(
        ""
    )

outletNearOverLoadCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 27)
)
outletNearOverLoadCleared.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "outletNumber"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    outletNearOverLoadCleared.setStatus(
        ""
    )

outletNearOverLoadSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 28)
)
outletNearOverLoadSet.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "outletNumber"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    outletNearOverLoadSet.setStatus(
        ""
    )

outletOverLoadCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 29)
)
outletOverLoadCleared.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "outletNumber"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    outletOverLoadCleared.setStatus(
        ""
    )

outletOverLoadSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 30)
)
outletOverLoadSet.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "outletNumber"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    outletOverLoadSet.setStatus(
        ""
    )

sensorDisconnectedCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 31)
)
sensorDisconnectedCleared.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "sensorNumber"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    sensorDisconnectedCleared.setStatus(
        ""
    )

sensorDisconnectedSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 32)
)
sensorDisconnectedSet.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "sensorNumber"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    sensorDisconnectedSet.setStatus(
        ""
    )

sensorTypeIndeterminateCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 33)
)
sensorTypeIndeterminateCleared.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "sensorNumber"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    sensorTypeIndeterminateCleared.setStatus(
        ""
    )

sensorTypeIndeterminateSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 34)
)
sensorTypeIndeterminateSet.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "sensorNumber"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    sensorTypeIndeterminateSet.setStatus(
        ""
    )

sensorTypeUnsupportedCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 35)
)
sensorTypeUnsupportedCleared.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "sensorNumber"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    sensorTypeUnsupportedCleared.setStatus(
        ""
    )

sensorTypeUnsupportedSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 36)
)
sensorTypeUnsupportedSet.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "sensorNumber"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    sensorTypeUnsupportedSet.setStatus(
        ""
    )

maxTemperatureExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 37)
)
maxTemperatureExceededCleared.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "sensorNumber"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    maxTemperatureExceededCleared.setStatus(
        ""
    )

maxTemperatureExceededSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 38)
)
maxTemperatureExceededSet.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "sensorNumber"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    maxTemperatureExceededSet.setStatus(
        ""
    )

highTemperatureExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 39)
)
highTemperatureExceededCleared.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "sensorNumber"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    highTemperatureExceededCleared.setStatus(
        ""
    )

highTemperatureExceededSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 40)
)
highTemperatureExceededSet.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "sensorNumber"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    highTemperatureExceededSet.setStatus(
        ""
    )

lowHumidityExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 41)
)
lowHumidityExceededCleared.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "sensorNumber"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    lowHumidityExceededCleared.setStatus(
        ""
    )

lowHumidityExceededSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 42)
)
lowHumidityExceededSet.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "sensorNumber"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    lowHumidityExceededSet.setStatus(
        ""
    )

minHumidityExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 43)
)
minHumidityExceededCleared.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "sensorNumber"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    minHumidityExceededCleared.setStatus(
        ""
    )

minHumidityExceededSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 44)
)
minHumidityExceededSet.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "sensorNumber"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    minHumidityExceededSet.setStatus(
        ""
    )

outletTurnOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 45)
)
outletTurnOn.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "outletNumber"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    outletTurnOn.setStatus(
        ""
    )

outletTurnOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 46)
)
outletTurnOff.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "outletNumber"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    outletTurnOff.setStatus(
        ""
    )

actionCancelled = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 47)
)
actionCancelled.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "outletNumber"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    actionCancelled.setStatus(
        ""
    )

deviceConfigurationChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 48)
)
deviceConfigurationChange.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    deviceConfigurationChange.setStatus(
        ""
    )

sensorConfigurationChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 49)
)
sensorConfigurationChange.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "sensorNumber"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    sensorConfigurationChange.setStatus(
        ""
    )

outletConfigurationChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 50)
)
outletConfigurationChange.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "outletNumber"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    outletConfigurationChange.setStatus(
        ""
    )

phaseConfigurationChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 51)
)
phaseConfigurationChange.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "phaseNumber"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    phaseConfigurationChange.setStatus(
        ""
    )

dryContactConfigurationChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 52)
)
dryContactConfigurationChange.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "contactNumber"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    dryContactConfigurationChange.setStatus(
        ""
    )

actionInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 53)
)
actionInit.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "outletNumber"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    actionInit.setStatus(
        ""
    )

actionFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 54)
)
actionFailed.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "outletNumber"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    actionFailed.setStatus(
        ""
    )

actionDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 55)
)
actionDeleted.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "outletNumber"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    actionDeleted.setStatus(
        ""
    )

syncCommandFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 56)
)
syncCommandFailed.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "outletNumber"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    syncCommandFailed.setStatus(
        ""
    )

mPOPicFwDownloadStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 57)
)
mPOPicFwDownloadStarted.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    mPOPicFwDownloadStarted.setStatus(
        ""
    )

mPOPicFwDownloadComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 58)
)
mPOPicFwDownloadComplete.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    mPOPicFwDownloadComplete.setStatus(
        ""
    )

mPOPicFwDownloadAborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 59)
)
mPOPicFwDownloadAborted.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    mPOPicFwDownloadAborted.setStatus(
        ""
    )

sensorCommEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 60)
)
sensorCommEstablished.setObjects(
      *(("DellrPDU-MIB", "serialNumber"),
        ("DellrPDU-MIB", "deviceNameD"),
        ("DellrPDU-MIB", "sensorNumber"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    sensorCommEstablished.setStatus(
        ""
    )

configChangeSNMP = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 1000)
)
configChangeSNMP.setObjects(
    ("DellrPDU-MIB", "mtrapargsString")
)
if mibBuilder.loadTexts:
    configChangeSNMP.setStatus(
        ""
    )

accessViolationConsole = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 1001)
)
accessViolationConsole.setObjects(
    ("DellrPDU-MIB", "mtrapargsString")
)
if mibBuilder.loadTexts:
    accessViolationConsole.setStatus(
        ""
    )

accessViolationHTTP = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 1002)
)
accessViolationHTTP.setObjects(
    ("DellrPDU-MIB", "mtrapargsString")
)
if mibBuilder.loadTexts:
    accessViolationHTTP.setStatus(
        ""
    )

dellTestTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10903, 200, 2, 200, 500, 0, 1003)
)
dellTestTrap.setObjects(
      *(("DellrPDU-MIB", "testTrapargsInteger"),
        ("DellrPDU-MIB", "mtrapargsString"))
)
if mibBuilder.loadTexts:
    dellTestTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DellrPDU-MIB",
    **{"RpduEnableDisableType": RpduEnableDisableType,
       "RpduNormalAlarmType": RpduNormalAlarmType,
       "RpduCommNoneOKLostType": RpduCommNoneOKLostType,
       "RpduLowNormalNearOverloadType": RpduLowNormalNearOverloadType,
       "RpduNotPBMinLowNrmlOHiMaxType": RpduNotPBMinLowNrmlOHiMaxType,
       "RpduOtherToNonrecoverableType": RpduOtherToNonrecoverableType,
       "RpduOutletPhaseLayoutType": RpduOutletPhaseLayoutType,
       "dell": dell,
       "pdu": pdu,
       "pdusub": pdusub,
       "software": software,
       "hardware": hardware,
       "productID": productID,
       "productIDDisplayName": productIDDisplayName,
       "productIDDescription": productIDDescription,
       "productIDVendor": productIDVendor,
       "productIDVersion": productIDVersion,
       "productIDBuildNumber": productIDBuildNumber,
       "productIDURL": productIDURL,
       "productIDDeviceNetworkName": productIDDeviceNetworkName,
       "productStatus": productStatus,
       "productStatusGlobalStatus": productStatusGlobalStatus,
       "productStatusLastGlobalStatus": productStatusLastGlobalStatus,
       "productStatusTimeStamp": productStatusTimeStamp,
       "productStatusRESERVED1": productStatusRESERVED1,
       "productStatusRESERVED2": productStatusRESERVED2,
       "productStatusRESERVED3": productStatusRESERVED3,
       "rPDU": rPDU,
       "rPDUIdentD": rPDUIdentD,
       "rPDUIdentTableSize": rPDUIdentTableSize,
       "rPDUIdentTable": rPDUIdentTable,
       "rPDUIdentEntry": rPDUIdentEntry,
       "rPDUIdentIndex": rPDUIdentIndex,
       "rPDUIdentNameD": rPDUIdentNameD,
       "rPDUIdentLocation": rPDUIdentLocation,
       "rPDUIdentHardwareRevD": rPDUIdentHardwareRevD,
       "rPDUIdentFirmwareRevD": rPDUIdentFirmwareRevD,
       "rPDUIdentDateOfManufactureD": rPDUIdentDateOfManufactureD,
       "rPDUIdentModelNumberD": rPDUIdentModelNumberD,
       "rPDUIdentSerialNumberD": rPDUIdentSerialNumberD,
       "rPDUDevice": rPDUDevice,
       "rPDUDeviceTableSize": rPDUDeviceTableSize,
       "rPDUDeviceStatusTable": rPDUDeviceStatusTable,
       "rPDUDeviceStatusEntry": rPDUDeviceStatusEntry,
       "rPDUDeviceStatusIndex": rPDUDeviceStatusIndex,
       "rPDUDeviceStatusName": rPDUDeviceStatusName,
       "rPDUDeviceStatusPower": rPDUDeviceStatusPower,
       "rPDUDeviceStatusEnergy": rPDUDeviceStatusEnergy,
       "rPDUDeviceStatusCommandPending": rPDUDeviceStatusCommandPending,
       "rPDUDeviceStatusLoadState": rPDUDeviceStatusLoadState,
       "rPDUDeviceConfigTable": rPDUDeviceConfigTable,
       "rPDUDeviceConfigEntry": rPDUDeviceConfigEntry,
       "rPDUDeviceConfigIndex": rPDUDeviceConfigIndex,
       "rPDUDeviceConfigName": rPDUDeviceConfigName,
       "rPDUDeviceConfigLocation": rPDUDeviceConfigLocation,
       "rPDUDeviceConfigColdstartDelay": rPDUDeviceConfigColdstartDelay,
       "rPDUDeviceCfgLowLoadPwrThresh": rPDUDeviceCfgLowLoadPwrThresh,
       "rPDUDeviceCfgNerOvloadPwrThresh": rPDUDeviceCfgNerOvloadPwrThresh,
       "rPDUDeviceCfgOverloadPwrThresh": rPDUDeviceCfgOverloadPwrThresh,
       "rPDUDeviceConfigPowerHeadroom": rPDUDeviceConfigPowerHeadroom,
       "rPDUDeviceConfigPeakPower": rPDUDeviceConfigPeakPower,
       "rPDUDeviceCfgPeakPwrStartTime": rPDUDeviceCfgPeakPwrStartTime,
       "rPDUDeviceConfigPeakPwrCapTime": rPDUDeviceConfigPeakPwrCapTime,
       "rPDUDeviceCfgPeakPowerHeadroom": rPDUDeviceCfgPeakPowerHeadroom,
       "rPDUDeviceCfgEnergyStartTime": rPDUDeviceCfgEnergyStartTime,
       "rPDUDevicePropertiesTable": rPDUDevicePropertiesTable,
       "rPDUDevicePropertiesEntry": rPDUDevicePropertiesEntry,
       "rPDUDevicePropertiesIndex": rPDUDevicePropertiesIndex,
       "rPDUDevicePropertiesName": rPDUDevicePropertiesName,
       "rPDUDevicePropertiesNumOutlets": rPDUDevicePropertiesNumOutlets,
       "rPDUDevicePropertiesNumSwdOuts": rPDUDevicePropertiesNumSwdOuts,
       "rPDUDevicePropertiesNumMtrdOuts": rPDUDevicePropertiesNumMtrdOuts,
       "rPDUDevicePropertiesNumPhases": rPDUDevicePropertiesNumPhases,
       "rPDUDevicePropertiesNumBreakers": rPDUDevicePropertiesNumBreakers,
       "rPDUDevicePropertiesMaxCurntRtg": rPDUDevicePropertiesMaxCurntRtg,
       "rPDUDevicePropertiesOutlayout": rPDUDevicePropertiesOutlayout,
       "rPDUDeviceControlTable": rPDUDeviceControlTable,
       "rPDUDeviceControlEntry": rPDUDeviceControlEntry,
       "rPDUDeviceControlIndex": rPDUDeviceControlIndex,
       "rPDUDeviceControlName": rPDUDeviceControlName,
       "rPDUDeviceControlCommand": rPDUDeviceControlCommand,
       "rPDUPhase": rPDUPhase,
       "rPDUPhaseTableSize": rPDUPhaseTableSize,
       "rPDUPhaseStatusTable": rPDUPhaseStatusTable,
       "rPDUPhaseStatusEntry": rPDUPhaseStatusEntry,
       "rPDUPhaseStatusIndex": rPDUPhaseStatusIndex,
       "rPDUPhaseStatusNumber": rPDUPhaseStatusNumber,
       "rPDUPhaseStatusLoadState": rPDUPhaseStatusLoadState,
       "rPDUPhaseStatusCurrent": rPDUPhaseStatusCurrent,
       "rPDUPhaseStatusVoltage": rPDUPhaseStatusVoltage,
       "rPDUPhaseStatusPower": rPDUPhaseStatusPower,
       "rPDUPhaseConfigTable": rPDUPhaseConfigTable,
       "rPDUPhaseConfigEntry": rPDUPhaseConfigEntry,
       "rPDUPhaseConfigIndex": rPDUPhaseConfigIndex,
       "rPDUPhaseConfigNumber": rPDUPhaseConfigNumber,
       "rPDUPhaseCfgOverloadRestriction": rPDUPhaseCfgOverloadRestriction,
       "rPDUPhCfgLowLoadCurntThreshold": rPDUPhCfgLowLoadCurntThreshold,
       "rPDUPhCfgNerOverloadCurntThresh": rPDUPhCfgNerOverloadCurntThresh,
       "rPDUPhCfgOverloadCurntThreshold": rPDUPhCfgOverloadCurntThreshold,
       "rPDUOutlet": rPDUOutlet,
       "rPDUOutletSwitched": rPDUOutletSwitched,
       "rPDUOutletSwitchedTableSize": rPDUOutletSwitchedTableSize,
       "rPDUOutletSwitchedStatusTable": rPDUOutletSwitchedStatusTable,
       "rPDUOutletSwitchedStatusEntry": rPDUOutletSwitchedStatusEntry,
       "rPDUOutletSwitchedStatusIndex": rPDUOutletSwitchedStatusIndex,
       "rPDUOutletSwitchedStatusNumber": rPDUOutletSwitchedStatusNumber,
       "rPDUOutletSwitchedStatusName": rPDUOutletSwitchedStatusName,
       "rPDUOutletSwitchedStatusState": rPDUOutletSwitchedStatusState,
       "rPDUOutletSwitchedStatCmdPnding": rPDUOutletSwitchedStatCmdPnding,
       "rPDUOutletSwitchedStatPhLayout": rPDUOutletSwitchedStatPhLayout,
       "rPDUOutletSwitchedConfigTable": rPDUOutletSwitchedConfigTable,
       "rPDUOutletSwitchedConfigEntry": rPDUOutletSwitchedConfigEntry,
       "rPDUOutletSwitchedConfigIndex": rPDUOutletSwitchedConfigIndex,
       "rPDUOutletSwitchedConfigNumber": rPDUOutletSwitchedConfigNumber,
       "rPDUOutletSwitchedConfigName": rPDUOutletSwitchedConfigName,
       "rPDUOutSwitchedCfgPowerOnTime": rPDUOutSwitchedCfgPowerOnTime,
       "rPDUOutSwitchedCfgPowerOffTime": rPDUOutSwitchedCfgPowerOffTime,
       "rPDUOutSwtchedCfgRebootDuration": rPDUOutSwtchedCfgRebootDuration,
       "rPDUOutletSwitchedControlTable": rPDUOutletSwitchedControlTable,
       "rPDUOutletSwitchedControlEntry": rPDUOutletSwitchedControlEntry,
       "rPDUOutletSwitchedControlIndex": rPDUOutletSwitchedControlIndex,
       "rPDUOutletSwitchedControlNumber": rPDUOutletSwitchedControlNumber,
       "rPDUOutletSwitchedControlName": rPDUOutletSwitchedControlName,
       "rPDUOutletSwitchedControlCmd": rPDUOutletSwitchedControlCmd,
       "rPDUOutletMetered": rPDUOutletMetered,
       "rPDUOutletMeteredTableSize": rPDUOutletMeteredTableSize,
       "rPDUOutletMeteredStatusTable": rPDUOutletMeteredStatusTable,
       "rPDUOutletMeteredStatusEntry": rPDUOutletMeteredStatusEntry,
       "rPDUOutletMeteredStatusIndex": rPDUOutletMeteredStatusIndex,
       "rPDUOutletMeteredStatusNumber": rPDUOutletMeteredStatusNumber,
       "rPDUOutletMeteredStatusName": rPDUOutletMeteredStatusName,
       "rPDUOutletMeteredStatusLayout": rPDUOutletMeteredStatusLayout,
       "rPDUOutMeteredStatPowerRating": rPDUOutMeteredStatPowerRating,
       "rPDUOutletMeteredStatusCurrent": rPDUOutletMeteredStatusCurrent,
       "rPDUOutletMeteredStatusEnergy": rPDUOutletMeteredStatusEnergy,
       "rPDUOutletMeteredStatusPower": rPDUOutletMeteredStatusPower,
       "rPDUOutletMeteredStatPeakPower": rPDUOutletMeteredStatPeakPower,
       "rPDUOutMeteredStatPeakPwrTime": rPDUOutMeteredStatPeakPwrTime,
       "rPDUOutMeteredStatusLoadState": rPDUOutMeteredStatusLoadState,
       "rPDUOutletMeteredConfigTable": rPDUOutletMeteredConfigTable,
       "rPDUOutletMeteredConfigEntry": rPDUOutletMeteredConfigEntry,
       "rPDUOutletMeteredConfigIndex": rPDUOutletMeteredConfigIndex,
       "rPDUOutletMeteredConfigNumber": rPDUOutletMeteredConfigNumber,
       "rPDUOutletMeteredConfigName": rPDUOutletMeteredConfigName,
       "rPDUOutMtredCfgLowLdCurntThresh": rPDUOutMtredCfgLowLdCurntThresh,
       "rPDUOutMtrdCfgNrOvdCurntThresh": rPDUOutMtrdCfgNrOvdCurntThresh,
       "rPDUOutMtredCfgOvrldCurntThresh": rPDUOutMtredCfgOvrldCurntThresh,
       "rPDUOutMeteredEnergyStartTime": rPDUOutMeteredEnergyStartTime,
       "rPDUOutMeteredPeakPwrStartTime": rPDUOutMeteredPeakPwrStartTime,
       "rPDUPowerSupply": rPDUPowerSupply,
       "rPDUPowerSupplyAlarmD": rPDUPowerSupplyAlarmD,
       "rPDUPowerSupplyVoltage": rPDUPowerSupplyVoltage,
       "rPDUSensor": rPDUSensor,
       "rPDUSensorStatus": rPDUSensorStatus,
       "rPDUSensorStatusTableSize": rPDUSensorStatusTableSize,
       "rPDUSensorStatusTable": rPDUSensorStatusTable,
       "rPDUSensorStatusEntry": rPDUSensorStatusEntry,
       "rPDUSensorStatusIndex": rPDUSensorStatusIndex,
       "rPDUSensorStatusName": rPDUSensorStatusName,
       "rPDUSensorStatusType": rPDUSensorStatusType,
       "rPDUSensorTemp": rPDUSensorTemp,
       "rPDUSensorTempTableSize": rPDUSensorTempTableSize,
       "rPDUSensorTempStatusTable": rPDUSensorTempStatusTable,
       "rPDUSensorTempStatusEntry": rPDUSensorTempStatusEntry,
       "rPDUSensorTempStatusIndex": rPDUSensorTempStatusIndex,
       "rPDUSensorTempStatusName": rPDUSensorTempStatusName,
       "rPDUSensorTempStatusCommStatus": rPDUSensorTempStatusCommStatus,
       "rPDUSensorTempStatusTempF": rPDUSensorTempStatusTempF,
       "rPDUSensorTempStatusTempC": rPDUSensorTempStatusTempC,
       "rPDUSensorTempStatusAlarmStatus": rPDUSensorTempStatusAlarmStatus,
       "rPDUSensorTempConfigTable": rPDUSensorTempConfigTable,
       "rPDUSensorTempConfigEntry": rPDUSensorTempConfigEntry,
       "rPDUSensorTempConfigIndex": rPDUSensorTempConfigIndex,
       "rPDUSensorTempConfigName": rPDUSensorTempConfigName,
       "rPDUSensorTempCfgTempMaxThreshF": rPDUSensorTempCfgTempMaxThreshF,
       "rPDUSnsorTempCfgTempHighThreshF": rPDUSnsorTempCfgTempHighThreshF,
       "rPDUSnsorTempCfgTempHysteresisF": rPDUSnsorTempCfgTempHysteresisF,
       "rPDUSensorTempCfgTempMaxThreshC": rPDUSensorTempCfgTempMaxThreshC,
       "rPDUSnsorTempCfgTempHighThreshC": rPDUSnsorTempCfgTempHighThreshC,
       "rPDUSnsorTempCfgTempHysteresisC": rPDUSnsorTempCfgTempHysteresisC,
       "rPDUSnsorTempCfgAlarmGeneration": rPDUSnsorTempCfgAlarmGeneration,
       "rPDUSensorHumidity": rPDUSensorHumidity,
       "rPDUSensorHumidityTableSize": rPDUSensorHumidityTableSize,
       "rPDUSensorHumidityStatusTable": rPDUSensorHumidityStatusTable,
       "rPDUSensorHumidityStatusEntry": rPDUSensorHumidityStatusEntry,
       "rPDUSensorHumidityStatusIndex": rPDUSensorHumidityStatusIndex,
       "rPDUSensorHumidityStatusName": rPDUSensorHumidityStatusName,
       "rPDUSnsorHumidityStatCommStatus": rPDUSnsorHumidityStatCommStatus,
       "rPDUSnsorHumStatRelativeHumdity": rPDUSnsorHumStatRelativeHumdity,
       "rPDUSnsorHumStatusAlarmStatus": rPDUSnsorHumStatusAlarmStatus,
       "rPDUSensorHumidityConfigTable": rPDUSensorHumidityConfigTable,
       "rPDUSensorHumidityConfigEntry": rPDUSensorHumidityConfigEntry,
       "rPDUSensorHumidityConfigIndex": rPDUSensorHumidityConfigIndex,
       "rPDUSensorHumidityConfigName": rPDUSensorHumidityConfigName,
       "rPDUSnsorHumCfgHumdityLowThresh": rPDUSnsorHumCfgHumdityLowThresh,
       "rPDUSnsorHumCfgHumdityMinThresh": rPDUSnsorHumCfgHumdityMinThresh,
       "rPDUSnsorHumCfgHumdtyHysteresis": rPDUSnsorHumCfgHumdtyHysteresis,
       "rPDUSnsorHumCfgAlarmGeneration": rPDUSnsorHumCfgAlarmGeneration,
       "rPDUSensorDiscrete": rPDUSensorDiscrete,
       "rPDUSensorDiscreteTableSize": rPDUSensorDiscreteTableSize,
       "rPDUSensorDiscreteStatusTable": rPDUSensorDiscreteStatusTable,
       "rPDUSensorDiscreteStatusEntry": rPDUSensorDiscreteStatusEntry,
       "rPDUSensorDiscreteStatusIndex": rPDUSensorDiscreteStatusIndex,
       "rPDUSensorDiscreteStatusName": rPDUSensorDiscreteStatusName,
       "rPDUSnsorDiscreteStatCurntState": rPDUSnsorDiscreteStatCurntState,
       "rPDUSnsorDiscreteStatAlarmState": rPDUSnsorDiscreteStatAlarmState,
       "rPDUSensorDiscreteConfigTable": rPDUSensorDiscreteConfigTable,
       "rPDUSensorDiscreteConfigEntry": rPDUSensorDiscreteConfigEntry,
       "rPDUSensorDiscreteConfigIndex": rPDUSensorDiscreteConfigIndex,
       "rPDUSensorDiscreteConfigName": rPDUSensorDiscreteConfigName,
       "rPDUSnsorDiscreteCfgNormalState": rPDUSnsorDiscreteCfgNormalState,
       "rPDUSnsorDiscrteAlarmGeneration": rPDUSnsorDiscrteAlarmGeneration,
       "mtrapargsD": mtrapargsD,
       "contactNumber": contactNumber,
       "outletNumber": outletNumber,
       "mtrapargsString": mtrapargsString,
       "phaseNumber": phaseNumber,
       "sensorNumber": sensorNumber,
       "deviceNameD": deviceNameD,
       "serialNumber": serialNumber,
       "testTrapargsInteger": testTrapargsInteger,
       "events": events,
       "deviceCommunicationLostCleared": deviceCommunicationLostCleared,
       "deviceCommunicationLostSet": deviceCommunicationLostSet,
       "componentCommLostCleared": componentCommLostCleared,
       "componentCommLostSet": componentCommLostSet,
       "cANBusOffCleared": cANBusOffCleared,
       "canBusOffSet": canBusOffSet,
       "powerSupplyFailureCleared": powerSupplyFailureCleared,
       "powerSupplyFailureSet": powerSupplyFailureSet,
       "keypadButtonStuckCleared": keypadButtonStuckCleared,
       "keypadButtonStuckSet": keypadButtonStuckSet,
       "dryContactAbnormalCleared": dryContactAbnormalCleared,
       "dryContactAbnormalSet": dryContactAbnormalSet,
       "deviceLowLoadCleared": deviceLowLoadCleared,
       "deviceLowLoadSet": deviceLowLoadSet,
       "deviceNearOverLoadCleared": deviceNearOverLoadCleared,
       "deviceNearOverLoadSet": deviceNearOverLoadSet,
       "deviceOverLoadCleared": deviceOverLoadCleared,
       "deviceOverLoadSet": deviceOverLoadSet,
       "phaseLowLoadCleared": phaseLowLoadCleared,
       "phaseLowLoadSet": phaseLowLoadSet,
       "phaseNearOverLoadCleared": phaseNearOverLoadCleared,
       "phaseNearOverLoadSet": phaseNearOverLoadSet,
       "phaseOverLoadCleared": phaseOverLoadCleared,
       "phaseOverLoadSet": phaseOverLoadSet,
       "outletLowLoadCleared": outletLowLoadCleared,
       "outletLowLoadSet": outletLowLoadSet,
       "outletNearOverLoadCleared": outletNearOverLoadCleared,
       "outletNearOverLoadSet": outletNearOverLoadSet,
       "outletOverLoadCleared": outletOverLoadCleared,
       "outletOverLoadSet": outletOverLoadSet,
       "sensorDisconnectedCleared": sensorDisconnectedCleared,
       "sensorDisconnectedSet": sensorDisconnectedSet,
       "sensorTypeIndeterminateCleared": sensorTypeIndeterminateCleared,
       "sensorTypeIndeterminateSet": sensorTypeIndeterminateSet,
       "sensorTypeUnsupportedCleared": sensorTypeUnsupportedCleared,
       "sensorTypeUnsupportedSet": sensorTypeUnsupportedSet,
       "maxTemperatureExceededCleared": maxTemperatureExceededCleared,
       "maxTemperatureExceededSet": maxTemperatureExceededSet,
       "highTemperatureExceededCleared": highTemperatureExceededCleared,
       "highTemperatureExceededSet": highTemperatureExceededSet,
       "lowHumidityExceededCleared": lowHumidityExceededCleared,
       "lowHumidityExceededSet": lowHumidityExceededSet,
       "minHumidityExceededCleared": minHumidityExceededCleared,
       "minHumidityExceededSet": minHumidityExceededSet,
       "outletTurnOn": outletTurnOn,
       "outletTurnOff": outletTurnOff,
       "actionCancelled": actionCancelled,
       "deviceConfigurationChange": deviceConfigurationChange,
       "sensorConfigurationChange": sensorConfigurationChange,
       "outletConfigurationChange": outletConfigurationChange,
       "phaseConfigurationChange": phaseConfigurationChange,
       "dryContactConfigurationChange": dryContactConfigurationChange,
       "actionInit": actionInit,
       "actionFailed": actionFailed,
       "actionDeleted": actionDeleted,
       "syncCommandFailed": syncCommandFailed,
       "mPOPicFwDownloadStarted": mPOPicFwDownloadStarted,
       "mPOPicFwDownloadComplete": mPOPicFwDownloadComplete,
       "mPOPicFwDownloadAborted": mPOPicFwDownloadAborted,
       "sensorCommEstablished": sensorCommEstablished,
       "configChangeSNMP": configChangeSNMP,
       "accessViolationConsole": accessViolationConsole,
       "accessViolationHTTP": accessViolationHTTP,
       "dellTestTrap": dellTestTrap,
       "system": system,
       "sysRPDUV1": sysRPDUV1}
)
