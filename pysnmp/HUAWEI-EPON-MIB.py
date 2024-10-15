# SNMP MIB module (HUAWEI-EPON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-EPON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:42 2024
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

(huaweiUtility,
 hwDatacomm) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "huaweiUtility",
    "hwDatacomm")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwEponMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179)
)


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



class PortList(OctetString, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_HwEponObjects_ObjectIdentity = ObjectIdentity
hwEponObjects = _HwEponObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1)
)
_HwEponGlobalObjects_ObjectIdentity = ObjectIdentity
hwEponGlobalObjects = _HwEponGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 1)
)


class _HwEponAutoFindOnuAge_Type(Integer32):
    """Custom type hwEponAutoFindOnuAge based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 300),
    )


_HwEponAutoFindOnuAge_Type.__name__ = "Integer32"
_HwEponAutoFindOnuAge_Object = MibScalar
hwEponAutoFindOnuAge = _HwEponAutoFindOnuAge_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 1, 1),
    _HwEponAutoFindOnuAge_Type()
)
hwEponAutoFindOnuAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEponAutoFindOnuAge.setStatus("current")


class _HwEponCtcOuiId_Type(Integer32):
    """Custom type hwEponCtcOuiId based on Integer32"""
    defaultValue = 111111

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwEponCtcOuiId_Type.__name__ = "Integer32"
_HwEponCtcOuiId_Object = MibScalar
hwEponCtcOuiId = _HwEponCtcOuiId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 1, 2),
    _HwEponCtcOuiId_Type()
)
hwEponCtcOuiId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEponCtcOuiId.setStatus("current")


class _HwEponChangePasswordAge_Type(Integer32):
    """Custom type hwEponChangePasswordAge based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_HwEponChangePasswordAge_Type.__name__ = "Integer32"
_HwEponChangePasswordAge_Object = MibScalar
hwEponChangePasswordAge = _HwEponChangePasswordAge_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 1, 3),
    _HwEponChangePasswordAge_Type()
)
hwEponChangePasswordAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEponChangePasswordAge.setStatus("current")
_HwEponControlObjects_ObjectIdentity = ObjectIdentity
hwEponControlObjects = _HwEponControlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2)
)
_HwEponOltControlTable_Object = MibTable
hwEponOltControlTable = _HwEponOltControlTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hwEponOltControlTable.setStatus("current")
_HwEponOltControlEntry_Object = MibTableRow
hwEponOltControlEntry = _HwEponOltControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 1, 1)
)
hwEponOltControlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hwEponOltControlEntry.setStatus("current")


class _HwEponOltControlfarthest_Type(Integer32):
    """Custom type hwEponOltControlfarthest based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_HwEponOltControlfarthest_Type.__name__ = "Integer32"
_HwEponOltControlfarthest_Object = MibTableColumn
hwEponOltControlfarthest = _HwEponOltControlfarthest_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 1, 1, 1),
    _HwEponOltControlfarthest_Type()
)
hwEponOltControlfarthest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEponOltControlfarthest.setStatus("current")
_HwEponOltControlAutofindOnuEnable_Type = EnabledStatus
_HwEponOltControlAutofindOnuEnable_Object = MibTableColumn
hwEponOltControlAutofindOnuEnable = _HwEponOltControlAutofindOnuEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 1, 1, 2),
    _HwEponOltControlAutofindOnuEnable_Type()
)
hwEponOltControlAutofindOnuEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEponOltControlAutofindOnuEnable.setStatus("current")


class _HwEponOltControlStatus_Type(Integer32):
    """Custom type hwEponOltControlStatus based on Integer32"""
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


_HwEponOltControlStatus_Type.__name__ = "Integer32"
_HwEponOltControlStatus_Object = MibTableColumn
hwEponOltControlStatus = _HwEponOltControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 1, 1, 3),
    _HwEponOltControlStatus_Type()
)
hwEponOltControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOltControlStatus.setStatus("current")
_HwEponOltControlUpStreamBandWidth_Type = Counter64
_HwEponOltControlUpStreamBandWidth_Object = MibTableColumn
hwEponOltControlUpStreamBandWidth = _HwEponOltControlUpStreamBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 1, 1, 4),
    _HwEponOltControlUpStreamBandWidth_Type()
)
hwEponOltControlUpStreamBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOltControlUpStreamBandWidth.setStatus("current")
_HwEponOltControlDownStreamBandWidth_Type = Counter64
_HwEponOltControlDownStreamBandWidth_Object = MibTableColumn
hwEponOltControlDownStreamBandWidth = _HwEponOltControlDownStreamBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 1, 1, 5),
    _HwEponOltControlDownStreamBandWidth_Type()
)
hwEponOltControlDownStreamBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOltControlDownStreamBandWidth.setStatus("current")
_HwEponOnuConfigTable_Object = MibTable
hwEponOnuConfigTable = _HwEponOnuConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hwEponOnuConfigTable.setStatus("current")
_HwEponOnuConfigEntry_Object = MibTableRow
hwEponOnuConfigEntry = _HwEponOnuConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 2, 1)
)
hwEponOnuConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HUAWEI-EPON-MIB", "hwEponOnuIndex"),
)
if mibBuilder.loadTexts:
    hwEponOnuConfigEntry.setStatus("current")


class _HwEponOnuIndex_Type(Integer32):
    """Custom type hwEponOnuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HwEponOnuIndex_Type.__name__ = "Integer32"
_HwEponOnuIndex_Object = MibTableColumn
hwEponOnuIndex = _HwEponOnuIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 2, 1, 1),
    _HwEponOnuIndex_Type()
)
hwEponOnuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEponOnuIndex.setStatus("current")


class _HwEponOnuId_Type(Integer32):
    """Custom type hwEponOnuId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HwEponOnuId_Type.__name__ = "Integer32"
_HwEponOnuId_Object = MibTableColumn
hwEponOnuId = _HwEponOnuId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 2, 1, 2),
    _HwEponOnuId_Type()
)
hwEponOnuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuId.setStatus("current")


class _HwEponOnuAuthMode_Type(Integer32):
    """Custom type hwEponOnuAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("alwaysOn", 3),
          ("onceOn", 4),
          ("sn", 1))
    )


_HwEponOnuAuthMode_Type.__name__ = "Integer32"
_HwEponOnuAuthMode_Object = MibTableColumn
hwEponOnuAuthMode = _HwEponOnuAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 2, 1, 3),
    _HwEponOnuAuthMode_Type()
)
hwEponOnuAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEponOnuAuthMode.setStatus("current")
_HwEponOnuMacAddress_Type = MacAddress
_HwEponOnuMacAddress_Object = MibTableColumn
hwEponOnuMacAddress = _HwEponOnuMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 2, 1, 4),
    _HwEponOnuMacAddress_Type()
)
hwEponOnuMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEponOnuMacAddress.setStatus("current")


class _HwEponOnuPassword_Type(DisplayString):
    """Custom type hwEponOnuPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_HwEponOnuPassword_Type.__name__ = "DisplayString"
_HwEponOnuPassword_Object = MibTableColumn
hwEponOnuPassword = _HwEponOnuPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 2, 1, 5),
    _HwEponOnuPassword_Type()
)
hwEponOnuPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEponOnuPassword.setStatus("current")


class _HwEponOnuTimeout_Type(Integer32):
    """Custom type hwEponOnuTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 168),
    )


_HwEponOnuTimeout_Type.__name__ = "Integer32"
_HwEponOnuTimeout_Object = MibTableColumn
hwEponOnuTimeout = _HwEponOnuTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 2, 1, 6),
    _HwEponOnuTimeout_Type()
)
hwEponOnuTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEponOnuTimeout.setStatus("current")


class _HwEponOnuManagementMode_Type(Integer32):
    """Custom type hwEponOnuManagementMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oam", 1),
          ("snmp", 2))
    )


_HwEponOnuManagementMode_Type.__name__ = "Integer32"
_HwEponOnuManagementMode_Object = MibTableColumn
hwEponOnuManagementMode = _HwEponOnuManagementMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 2, 1, 7),
    _HwEponOnuManagementMode_Type()
)
hwEponOnuManagementMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEponOnuManagementMode.setStatus("current")


class _HwEponOnuLineProfName_Type(DisplayString):
    """Custom type hwEponOnuLineProfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwEponOnuLineProfName_Type.__name__ = "DisplayString"
_HwEponOnuLineProfName_Object = MibTableColumn
hwEponOnuLineProfName = _HwEponOnuLineProfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 2, 1, 8),
    _HwEponOnuLineProfName_Type()
)
hwEponOnuLineProfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEponOnuLineProfName.setStatus("current")


class _HwEponOnuServiceProfName_Type(DisplayString):
    """Custom type hwEponOnuServiceProfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwEponOnuServiceProfName_Type.__name__ = "DisplayString"
_HwEponOnuServiceProfName_Object = MibTableColumn
hwEponOnuServiceProfName = _HwEponOnuServiceProfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 2, 1, 9),
    _HwEponOnuServiceProfName_Type()
)
hwEponOnuServiceProfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEponOnuServiceProfName.setStatus("current")


class _HwEponOnuSnmpProfName_Type(DisplayString):
    """Custom type hwEponOnuSnmpProfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwEponOnuSnmpProfName_Type.__name__ = "DisplayString"
_HwEponOnuSnmpProfName_Object = MibTableColumn
hwEponOnuSnmpProfName = _HwEponOnuSnmpProfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 2, 1, 10),
    _HwEponOnuSnmpProfName_Type()
)
hwEponOnuSnmpProfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEponOnuSnmpProfName.setStatus("current")


class _HwEponOnuDescription_Type(DisplayString):
    """Custom type hwEponOnuDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwEponOnuDescription_Type.__name__ = "DisplayString"
_HwEponOnuDescription_Object = MibTableColumn
hwEponOnuDescription = _HwEponOnuDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 2, 1, 11),
    _HwEponOnuDescription_Type()
)
hwEponOnuDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEponOnuDescription.setStatus("current")


class _HwEponOnuActiveStatus_Type(Integer32):
    """Custom type hwEponOnuActiveStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("deactive", 2))
    )


_HwEponOnuActiveStatus_Type.__name__ = "Integer32"
_HwEponOnuActiveStatus_Object = MibTableColumn
hwEponOnuActiveStatus = _HwEponOnuActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 2, 1, 12),
    _HwEponOnuActiveStatus_Type()
)
hwEponOnuActiveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEponOnuActiveStatus.setStatus("current")
_HwEponOnuRowStatus_Type = RowStatus
_HwEponOnuRowStatus_Object = MibTableColumn
hwEponOnuRowStatus = _HwEponOnuRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 2, 1, 51),
    _HwEponOnuRowStatus_Type()
)
hwEponOnuRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOnuRowStatus.setStatus("current")
_HwEponOnuVersionTable_Object = MibTable
hwEponOnuVersionTable = _HwEponOnuVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hwEponOnuVersionTable.setStatus("current")
_HwEponOnuVersionEntry_Object = MibTableRow
hwEponOnuVersionEntry = _HwEponOnuVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 3, 1)
)
hwEponOnuVersionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HUAWEI-EPON-MIB", "hwEponOnuIndex"),
)
if mibBuilder.loadTexts:
    hwEponOnuVersionEntry.setStatus("current")
_HwEponOnuVendorId_Type = DisplayString
_HwEponOnuVendorId_Object = MibTableColumn
hwEponOnuVendorId = _HwEponOnuVendorId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 3, 1, 1),
    _HwEponOnuVendorId_Type()
)
hwEponOnuVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuVendorId.setStatus("current")
_HwEponOnuModel_Type = Integer32
_HwEponOnuModel_Object = MibTableColumn
hwEponOnuModel = _HwEponOnuModel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 3, 1, 2),
    _HwEponOnuModel_Type()
)
hwEponOnuModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuModel.setStatus("current")
_HwEponOnuOnuIdentifier_Type = DisplayString
_HwEponOnuOnuIdentifier_Object = MibTableColumn
hwEponOnuOnuIdentifier = _HwEponOnuOnuIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 3, 1, 3),
    _HwEponOnuOnuIdentifier_Type()
)
hwEponOnuOnuIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuOnuIdentifier.setStatus("current")
_HwEponOnuHardwareVersion_Type = DisplayString
_HwEponOnuHardwareVersion_Object = MibTableColumn
hwEponOnuHardwareVersion = _HwEponOnuHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 3, 1, 4),
    _HwEponOnuHardwareVersion_Type()
)
hwEponOnuHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuHardwareVersion.setStatus("current")
_HwEponOnuSoftwareVersion_Type = DisplayString
_HwEponOnuSoftwareVersion_Object = MibTableColumn
hwEponOnuSoftwareVersion = _HwEponOnuSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 3, 1, 5),
    _HwEponOnuSoftwareVersion_Type()
)
hwEponOnuSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuSoftwareVersion.setStatus("current")
_HwEponOnuChipVenderId_Type = DisplayString
_HwEponOnuChipVenderId_Object = MibTableColumn
hwEponOnuChipVenderId = _HwEponOnuChipVenderId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 3, 1, 6),
    _HwEponOnuChipVenderId_Type()
)
hwEponOnuChipVenderId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuChipVenderId.setStatus("current")
_HwEponOnuChipModel_Type = Integer32
_HwEponOnuChipModel_Object = MibTableColumn
hwEponOnuChipModel = _HwEponOnuChipModel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 3, 1, 7),
    _HwEponOnuChipModel_Type()
)
hwEponOnuChipModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuChipModel.setStatus("current")
_HwEponOnuChipVersion_Type = Integer32
_HwEponOnuChipVersion_Object = MibTableColumn
hwEponOnuChipVersion = _HwEponOnuChipVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 3, 1, 8),
    _HwEponOnuChipVersion_Type()
)
hwEponOnuChipVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuChipVersion.setStatus("current")
_HwEponOnuChipDesignDate_Type = DisplayString
_HwEponOnuChipDesignDate_Object = MibTableColumn
hwEponOnuChipDesignDate = _HwEponOnuChipDesignDate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 3, 1, 9),
    _HwEponOnuChipDesignDate_Type()
)
hwEponOnuChipDesignDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuChipDesignDate.setStatus("current")
_HwEponOnuFirmwareVersion_Type = Integer32
_HwEponOnuFirmwareVersion_Object = MibTableColumn
hwEponOnuFirmwareVersion = _HwEponOnuFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 3, 1, 10),
    _HwEponOnuFirmwareVersion_Type()
)
hwEponOnuFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuFirmwareVersion.setStatus("current")
_HwEponOnuControlTable_Object = MibTable
hwEponOnuControlTable = _HwEponOnuControlTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 4)
)
if mibBuilder.loadTexts:
    hwEponOnuControlTable.setStatus("current")
_HwEponOnuControlEntry_Object = MibTableRow
hwEponOnuControlEntry = _HwEponOnuControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 4, 1)
)
hwEponOnuControlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HUAWEI-EPON-MIB", "hwEponOnuIndex"),
)
if mibBuilder.loadTexts:
    hwEponOnuControlEntry.setStatus("current")


class _HwEponOnuReset_Type(Integer32):
    """Custom type hwEponOnuReset based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_HwEponOnuReset_Type.__name__ = "Integer32"
_HwEponOnuReset_Object = MibTableColumn
hwEponOnuReset = _HwEponOnuReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 4, 1, 1),
    _HwEponOnuReset_Type()
)
hwEponOnuReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEponOnuReset.setStatus("current")


class _HwEponOnuReRegister_Type(Integer32):
    """Custom type hwEponOnuReRegister based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_HwEponOnuReRegister_Type.__name__ = "Integer32"
_HwEponOnuReRegister_Object = MibTableColumn
hwEponOnuReRegister = _HwEponOnuReRegister_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 4, 1, 2),
    _HwEponOnuReRegister_Type()
)
hwEponOnuReRegister.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEponOnuReRegister.setStatus("current")


class _HwEponOnuReDiscovery_Type(Integer32):
    """Custom type hwEponOnuReDiscovery based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_HwEponOnuReDiscovery_Type.__name__ = "Integer32"
_HwEponOnuReDiscovery_Object = MibTableColumn
hwEponOnuReDiscovery = _HwEponOnuReDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 4, 1, 3),
    _HwEponOnuReDiscovery_Type()
)
hwEponOnuReDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEponOnuReDiscovery.setStatus("current")


class _HwEponOnuRunStatus_Type(Integer32):
    """Custom type hwEponOnuRunStatus based on Integer32"""
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


_HwEponOnuRunStatus_Type.__name__ = "Integer32"
_HwEponOnuRunStatus_Object = MibTableColumn
hwEponOnuRunStatus = _HwEponOnuRunStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 4, 1, 4),
    _HwEponOnuRunStatus_Type()
)
hwEponOnuRunStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuRunStatus.setStatus("current")
_HwEponOnuDistance_Type = Integer32
_HwEponOnuDistance_Object = MibTableColumn
hwEponOnuDistance = _HwEponOnuDistance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 4, 1, 5),
    _HwEponOnuDistance_Type()
)
hwEponOnuDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuDistance.setStatus("current")
_HwEponOnuRtt_Type = Integer32
_HwEponOnuRtt_Object = MibTableColumn
hwEponOnuRtt = _HwEponOnuRtt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 4, 1, 6),
    _HwEponOnuRtt_Type()
)
hwEponOnuRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuRtt.setStatus("current")
_HwEponOnuLastUpTime_Type = DisplayString
_HwEponOnuLastUpTime_Object = MibTableColumn
hwEponOnuLastUpTime = _HwEponOnuLastUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 4, 1, 7),
    _HwEponOnuLastUpTime_Type()
)
hwEponOnuLastUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuLastUpTime.setStatus("current")
_HwEponOnuLastDownTime_Type = DisplayString
_HwEponOnuLastDownTime_Object = MibTableColumn
hwEponOnuLastDownTime = _HwEponOnuLastDownTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 4, 1, 8),
    _HwEponOnuLastDownTime_Type()
)
hwEponOnuLastDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuLastDownTime.setStatus("current")


class _HwEponOnuLastDownCause_Type(Integer32):
    """Custom type hwEponOnuLastDownCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(7, 10),
        ValueRangeConstraint(13, 13),
    )


_HwEponOnuLastDownCause_Type.__name__ = "Integer32"
_HwEponOnuLastDownCause_Object = MibTableColumn
hwEponOnuLastDownCause = _HwEponOnuLastDownCause_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 4, 1, 9),
    _HwEponOnuLastDownCause_Type()
)
hwEponOnuLastDownCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuLastDownCause.setStatus("current")
_HwEponAutoFindOnuInfoTable_Object = MibTable
hwEponAutoFindOnuInfoTable = _HwEponAutoFindOnuInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 5)
)
if mibBuilder.loadTexts:
    hwEponAutoFindOnuInfoTable.setStatus("current")
_HwEponAutoFindOnuInfoEntry_Object = MibTableRow
hwEponAutoFindOnuInfoEntry = _HwEponAutoFindOnuInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 5, 1)
)
hwEponAutoFindOnuInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HUAWEI-EPON-MIB", "hwEponAutoFindOnuOrder"),
)
if mibBuilder.loadTexts:
    hwEponAutoFindOnuInfoEntry.setStatus("current")


class _HwEponAutoFindOnuOrder_Type(Integer32):
    """Custom type hwEponAutoFindOnuOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HwEponAutoFindOnuOrder_Type.__name__ = "Integer32"
_HwEponAutoFindOnuOrder_Object = MibTableColumn
hwEponAutoFindOnuOrder = _HwEponAutoFindOnuOrder_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 5, 1, 1),
    _HwEponAutoFindOnuOrder_Type()
)
hwEponAutoFindOnuOrder.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEponAutoFindOnuOrder.setStatus("current")
_HwEponAutoFindOnuInfoMacAddress_Type = MacAddress
_HwEponAutoFindOnuInfoMacAddress_Object = MibTableColumn
hwEponAutoFindOnuInfoMacAddress = _HwEponAutoFindOnuInfoMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 5, 1, 2),
    _HwEponAutoFindOnuInfoMacAddress_Type()
)
hwEponAutoFindOnuInfoMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponAutoFindOnuInfoMacAddress.setStatus("current")
_HwEponAutoFindOnuInfoPasswordValue_Type = DisplayString
_HwEponAutoFindOnuInfoPasswordValue_Object = MibTableColumn
hwEponAutoFindOnuInfoPasswordValue = _HwEponAutoFindOnuInfoPasswordValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 5, 1, 3),
    _HwEponAutoFindOnuInfoPasswordValue_Type()
)
hwEponAutoFindOnuInfoPasswordValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponAutoFindOnuInfoPasswordValue.setStatus("current")
_HwEponOnuCapabilityInfoTable_Object = MibTable
hwEponOnuCapabilityInfoTable = _HwEponOnuCapabilityInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 6)
)
if mibBuilder.loadTexts:
    hwEponOnuCapabilityInfoTable.setStatus("current")
_HwEponOnuCapabilityInfoEntry_Object = MibTableRow
hwEponOnuCapabilityInfoEntry = _HwEponOnuCapabilityInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 6, 1)
)
hwEponOnuCapabilityInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HUAWEI-EPON-MIB", "hwEponOnuIndex"),
)
if mibBuilder.loadTexts:
    hwEponOnuCapabilityInfoEntry.setStatus("current")
_HwEponOnuPotsPortNum_Type = Integer32
_HwEponOnuPotsPortNum_Object = MibTableColumn
hwEponOnuPotsPortNum = _HwEponOnuPotsPortNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 6, 1, 1),
    _HwEponOnuPotsPortNum_Type()
)
hwEponOnuPotsPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuPotsPortNum.setStatus("current")
_HwEponOnuFePortsNum_Type = Integer32
_HwEponOnuFePortsNum_Object = MibTableColumn
hwEponOnuFePortsNum = _HwEponOnuFePortsNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 6, 1, 2),
    _HwEponOnuFePortsNum_Type()
)
hwEponOnuFePortsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuFePortsNum.setStatus("current")
_HwEponOnuGePortsNum_Type = Integer32
_HwEponOnuGePortsNum_Object = MibTableColumn
hwEponOnuGePortsNum = _HwEponOnuGePortsNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 6, 1, 3),
    _HwEponOnuGePortsNum_Type()
)
hwEponOnuGePortsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuGePortsNum.setStatus("current")
_HwEponOnuTdmPortsNum_Type = Integer32
_HwEponOnuTdmPortsNum_Object = MibTableColumn
hwEponOnuTdmPortsNum = _HwEponOnuTdmPortsNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 6, 1, 4),
    _HwEponOnuTdmPortsNum_Type()
)
hwEponOnuTdmPortsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuTdmPortsNum.setStatus("current")
_HwEponOnuFecSupport_Type = Integer32
_HwEponOnuFecSupport_Object = MibTableColumn
hwEponOnuFecSupport = _HwEponOnuFecSupport_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 6, 1, 5),
    _HwEponOnuFecSupport_Type()
)
hwEponOnuFecSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuFecSupport.setStatus("current")
_HwEponOnuSupportBackupBattery_Type = Integer32
_HwEponOnuSupportBackupBattery_Object = MibTableColumn
hwEponOnuSupportBackupBattery = _HwEponOnuSupportBackupBattery_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 6, 1, 6),
    _HwEponOnuSupportBackupBattery_Type()
)
hwEponOnuSupportBackupBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuSupportBackupBattery.setStatus("current")
_HwEponOnuUpQueueNum_Type = Integer32
_HwEponOnuUpQueueNum_Object = MibTableColumn
hwEponOnuUpQueueNum = _HwEponOnuUpQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 6, 1, 7),
    _HwEponOnuUpQueueNum_Type()
)
hwEponOnuUpQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuUpQueueNum.setStatus("current")
_HwEponOnuUpQueueNumPerPort_Type = Integer32
_HwEponOnuUpQueueNumPerPort_Object = MibTableColumn
hwEponOnuUpQueueNumPerPort = _HwEponOnuUpQueueNumPerPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 6, 1, 8),
    _HwEponOnuUpQueueNumPerPort_Type()
)
hwEponOnuUpQueueNumPerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuUpQueueNumPerPort.setStatus("current")
_HwEponOnuDownQueueNum_Type = Integer32
_HwEponOnuDownQueueNum_Object = MibTableColumn
hwEponOnuDownQueueNum = _HwEponOnuDownQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 6, 1, 9),
    _HwEponOnuDownQueueNum_Type()
)
hwEponOnuDownQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuDownQueueNum.setStatus("current")
_HwEponOnuDownQueueNumPerPort_Type = Integer32
_HwEponOnuDownQueueNumPerPort_Object = MibTableColumn
hwEponOnuDownQueueNumPerPort = _HwEponOnuDownQueueNumPerPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 6, 1, 10),
    _HwEponOnuDownQueueNumPerPort_Type()
)
hwEponOnuDownQueueNumPerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuDownQueueNumPerPort.setStatus("current")
_HwEponOnuFePortList_Type = PortList
_HwEponOnuFePortList_Object = MibTableColumn
hwEponOnuFePortList = _HwEponOnuFePortList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 6, 1, 11),
    _HwEponOnuFePortList_Type()
)
hwEponOnuFePortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuFePortList.setStatus("current")
_HwEponOnuGePortList_Type = PortList
_HwEponOnuGePortList_Object = MibTableColumn
hwEponOnuGePortList = _HwEponOnuGePortList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 6, 1, 12),
    _HwEponOnuGePortList_Type()
)
hwEponOnuGePortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuGePortList.setStatus("current")
_HwEponOnuSupportMulticastQuickLeave_Type = Integer32
_HwEponOnuSupportMulticastQuickLeave_Object = MibTableColumn
hwEponOnuSupportMulticastQuickLeave = _HwEponOnuSupportMulticastQuickLeave_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 6, 1, 13),
    _HwEponOnuSupportMulticastQuickLeave_Type()
)
hwEponOnuSupportMulticastQuickLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuSupportMulticastQuickLeave.setStatus("current")
_HwEponOnuIpConfigTable_Object = MibTable
hwEponOnuIpConfigTable = _HwEponOnuIpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 7)
)
if mibBuilder.loadTexts:
    hwEponOnuIpConfigTable.setStatus("current")
_HwEponOnuIpConfigEntry_Object = MibTableRow
hwEponOnuIpConfigEntry = _HwEponOnuIpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 7, 1)
)
hwEponOnuIpConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HUAWEI-EPON-MIB", "hwEponOnuIndex"),
)
if mibBuilder.loadTexts:
    hwEponOnuIpConfigEntry.setStatus("current")
_HwEponOnuIpAddress_Type = IpAddress
_HwEponOnuIpAddress_Object = MibTableColumn
hwEponOnuIpAddress = _HwEponOnuIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 7, 1, 1),
    _HwEponOnuIpAddress_Type()
)
hwEponOnuIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOnuIpAddress.setStatus("current")
_HwEponOnuNetMask_Type = IpAddress
_HwEponOnuNetMask_Object = MibTableColumn
hwEponOnuNetMask = _HwEponOnuNetMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 7, 1, 2),
    _HwEponOnuNetMask_Type()
)
hwEponOnuNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOnuNetMask.setStatus("current")
_HwEponOnuNetGateway_Type = IpAddress
_HwEponOnuNetGateway_Object = MibTableColumn
hwEponOnuNetGateway = _HwEponOnuNetGateway_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 7, 1, 3),
    _HwEponOnuNetGateway_Type()
)
hwEponOnuNetGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOnuNetGateway.setStatus("current")


class _HwEponOnuIpManageVlan_Type(Integer32):
    """Custom type hwEponOnuIpManageVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HwEponOnuIpManageVlan_Type.__name__ = "Integer32"
_HwEponOnuIpManageVlan_Object = MibTableColumn
hwEponOnuIpManageVlan = _HwEponOnuIpManageVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 7, 1, 4),
    _HwEponOnuIpManageVlan_Type()
)
hwEponOnuIpManageVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOnuIpManageVlan.setStatus("current")
_HwEponOnuIpRowStates_Type = RowStatus
_HwEponOnuIpRowStates_Object = MibTableColumn
hwEponOnuIpRowStates = _HwEponOnuIpRowStates_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 7, 1, 51),
    _HwEponOnuIpRowStates_Type()
)
hwEponOnuIpRowStates.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOnuIpRowStates.setStatus("current")
_HwEponOnuEthObjectCfgTable_Object = MibTable
hwEponOnuEthObjectCfgTable = _HwEponOnuEthObjectCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 8)
)
if mibBuilder.loadTexts:
    hwEponOnuEthObjectCfgTable.setStatus("current")
_HwEponOnuEthObjectCfgEntry_Object = MibTableRow
hwEponOnuEthObjectCfgEntry = _HwEponOnuEthObjectCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 8, 1)
)
hwEponOnuEthObjectCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HUAWEI-EPON-MIB", "hwEponOnuIndex"),
    (0, "HUAWEI-EPON-MIB", "hwEponOnuEthPortId"),
)
if mibBuilder.loadTexts:
    hwEponOnuEthObjectCfgEntry.setStatus("current")


class _HwEponOnuEthPortId_Type(Integer32):
    """Custom type hwEponOnuEthPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HwEponOnuEthPortId_Type.__name__ = "Integer32"
_HwEponOnuEthPortId_Object = MibTableColumn
hwEponOnuEthPortId = _HwEponOnuEthPortId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 8, 1, 1),
    _HwEponOnuEthPortId_Type()
)
hwEponOnuEthPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEponOnuEthPortId.setStatus("current")


class _HwEponOnuEthOperateStatus_Type(Integer32):
    """Custom type hwEponOnuEthOperateStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("shutdown", 2),
          ("undoshutdown", 1))
    )


_HwEponOnuEthOperateStatus_Type.__name__ = "Integer32"
_HwEponOnuEthOperateStatus_Object = MibTableColumn
hwEponOnuEthOperateStatus = _HwEponOnuEthOperateStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 8, 1, 2),
    _HwEponOnuEthOperateStatus_Type()
)
hwEponOnuEthOperateStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEponOnuEthOperateStatus.setStatus("current")


class _HwEponOnuEthFlowcontrolSwitch_Type(Integer32):
    """Custom type hwEponOnuEthFlowcontrolSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("close", 2),
          ("open", 1))
    )


_HwEponOnuEthFlowcontrolSwitch_Type.__name__ = "Integer32"
_HwEponOnuEthFlowcontrolSwitch_Object = MibTableColumn
hwEponOnuEthFlowcontrolSwitch = _HwEponOnuEthFlowcontrolSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 8, 1, 3),
    _HwEponOnuEthFlowcontrolSwitch_Type()
)
hwEponOnuEthFlowcontrolSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEponOnuEthFlowcontrolSwitch.setStatus("current")
_HwEponOnuTdmPortCfgTable_Object = MibTable
hwEponOnuTdmPortCfgTable = _HwEponOnuTdmPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 9)
)
if mibBuilder.loadTexts:
    hwEponOnuTdmPortCfgTable.setStatus("current")
_HwEponOnuTdmPortCfgEntry_Object = MibTableRow
hwEponOnuTdmPortCfgEntry = _HwEponOnuTdmPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 9, 1)
)
hwEponOnuTdmPortCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HUAWEI-EPON-MIB", "hwEponOnuIndex"),
    (0, "HUAWEI-EPON-MIB", "hwEponOnuTdmPortId"),
)
if mibBuilder.loadTexts:
    hwEponOnuTdmPortCfgEntry.setStatus("current")


class _HwEponOnuTdmPortId_Type(Integer32):
    """Custom type hwEponOnuTdmPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwEponOnuTdmPortId_Type.__name__ = "Integer32"
_HwEponOnuTdmPortId_Object = MibTableColumn
hwEponOnuTdmPortId = _HwEponOnuTdmPortId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 9, 1, 1),
    _HwEponOnuTdmPortId_Type()
)
hwEponOnuTdmPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEponOnuTdmPortId.setStatus("current")


class _HwEponOnuTdmPortOperateStatus_Type(Integer32):
    """Custom type hwEponOnuTdmPortOperateStatus based on Integer32"""
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


_HwEponOnuTdmPortOperateStatus_Type.__name__ = "Integer32"
_HwEponOnuTdmPortOperateStatus_Object = MibTableColumn
hwEponOnuTdmPortOperateStatus = _HwEponOnuTdmPortOperateStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 9, 1, 2),
    _HwEponOnuTdmPortOperateStatus_Type()
)
hwEponOnuTdmPortOperateStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEponOnuTdmPortOperateStatus.setStatus("current")
_HwEponOnuPotsPortCfgTable_Object = MibTable
hwEponOnuPotsPortCfgTable = _HwEponOnuPotsPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 10)
)
if mibBuilder.loadTexts:
    hwEponOnuPotsPortCfgTable.setStatus("current")
_HwEponOnuPotsPortCfgEntry_Object = MibTableRow
hwEponOnuPotsPortCfgEntry = _HwEponOnuPotsPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 10, 1)
)
hwEponOnuPotsPortCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HUAWEI-EPON-MIB", "hwEponOnuIndex"),
    (0, "HUAWEI-EPON-MIB", "hwEponOnuPotsPortId"),
)
if mibBuilder.loadTexts:
    hwEponOnuPotsPortCfgEntry.setStatus("current")


class _HwEponOnuPotsPortId_Type(Integer32):
    """Custom type hwEponOnuPotsPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HwEponOnuPotsPortId_Type.__name__ = "Integer32"
_HwEponOnuPotsPortId_Object = MibTableColumn
hwEponOnuPotsPortId = _HwEponOnuPotsPortId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 10, 1, 1),
    _HwEponOnuPotsPortId_Type()
)
hwEponOnuPotsPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEponOnuPotsPortId.setStatus("current")


class _HwEponOnuPotsPortOperateStatus_Type(Integer32):
    """Custom type hwEponOnuPotsPortOperateStatus based on Integer32"""
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


_HwEponOnuPotsPortOperateStatus_Type.__name__ = "Integer32"
_HwEponOnuPotsPortOperateStatus_Object = MibTableColumn
hwEponOnuPotsPortOperateStatus = _HwEponOnuPotsPortOperateStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 10, 1, 2),
    _HwEponOnuPotsPortOperateStatus_Type()
)
hwEponOnuPotsPortOperateStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEponOnuPotsPortOperateStatus.setStatus("current")
_HwEponOnuCfgCarTable_Object = MibTable
hwEponOnuCfgCarTable = _HwEponOnuCfgCarTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 11)
)
if mibBuilder.loadTexts:
    hwEponOnuCfgCarTable.setStatus("current")
_HwEponOnuCfgCarEntry_Object = MibTableRow
hwEponOnuCfgCarEntry = _HwEponOnuCfgCarEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 11, 1)
)
hwEponOnuCfgCarEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HUAWEI-EPON-MIB", "hwEponOnuIndex"),
    (0, "HUAWEI-EPON-MIB", "hwEponOnuCfgCarDirection"),
)
if mibBuilder.loadTexts:
    hwEponOnuCfgCarEntry.setStatus("current")


class _HwEponOnuCfgCarDirection_Type(Integer32):
    """Custom type hwEponOnuCfgCarDirection based on Integer32"""
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


_HwEponOnuCfgCarDirection_Type.__name__ = "Integer32"
_HwEponOnuCfgCarDirection_Object = MibTableColumn
hwEponOnuCfgCarDirection = _HwEponOnuCfgCarDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 11, 1, 1),
    _HwEponOnuCfgCarDirection_Type()
)
hwEponOnuCfgCarDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEponOnuCfgCarDirection.setStatus("current")
_HwEponOnuCarProfileNameIndex_Type = DisplayString
_HwEponOnuCarProfileNameIndex_Object = MibTableColumn
hwEponOnuCarProfileNameIndex = _HwEponOnuCarProfileNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 11, 1, 2),
    _HwEponOnuCarProfileNameIndex_Type()
)
hwEponOnuCarProfileNameIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOnuCarProfileNameIndex.setStatus("current")
_HwEponOnuTrafficPolicyNameIndex_Type = DisplayString
_HwEponOnuTrafficPolicyNameIndex_Object = MibTableColumn
hwEponOnuTrafficPolicyNameIndex = _HwEponOnuTrafficPolicyNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 11, 1, 3),
    _HwEponOnuTrafficPolicyNameIndex_Type()
)
hwEponOnuTrafficPolicyNameIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOnuTrafficPolicyNameIndex.setStatus("current")
_HwEponOnuCfgCarRowStatus_Type = RowStatus
_HwEponOnuCfgCarRowStatus_Object = MibTableColumn
hwEponOnuCfgCarRowStatus = _HwEponOnuCfgCarRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 11, 1, 51),
    _HwEponOnuCfgCarRowStatus_Type()
)
hwEponOnuCfgCarRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOnuCfgCarRowStatus.setStatus("current")
_HwEponOltPortDefaultVlanTable_Object = MibTable
hwEponOltPortDefaultVlanTable = _HwEponOltPortDefaultVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 12)
)
if mibBuilder.loadTexts:
    hwEponOltPortDefaultVlanTable.setStatus("current")
_HwEponOltPortDefaultVlanEntry_Object = MibTableRow
hwEponOltPortDefaultVlanEntry = _HwEponOltPortDefaultVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 12, 1)
)
hwEponOltPortDefaultVlanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HUAWEI-EPON-MIB", "hwEponOnuIndex"),
)
if mibBuilder.loadTexts:
    hwEponOltPortDefaultVlanEntry.setStatus("current")


class _HwEponOltPortDefaultVlanId_Type(Integer32):
    """Custom type hwEponOltPortDefaultVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HwEponOltPortDefaultVlanId_Type.__name__ = "Integer32"
_HwEponOltPortDefaultVlanId_Object = MibTableColumn
hwEponOltPortDefaultVlanId = _HwEponOltPortDefaultVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 12, 1, 1),
    _HwEponOltPortDefaultVlanId_Type()
)
hwEponOltPortDefaultVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOltPortDefaultVlanId.setStatus("current")


class _HwEponOltPortDefaultVlanBatch_Type(Integer32):
    """Custom type hwEponOltPortDefaultVlanBatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("batch", 1),
          ("notBatch", 2))
    )


_HwEponOltPortDefaultVlanBatch_Type.__name__ = "Integer32"
_HwEponOltPortDefaultVlanBatch_Object = MibTableColumn
hwEponOltPortDefaultVlanBatch = _HwEponOltPortDefaultVlanBatch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 12, 1, 2),
    _HwEponOltPortDefaultVlanBatch_Type()
)
hwEponOltPortDefaultVlanBatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOltPortDefaultVlanBatch.setStatus("current")


class _HwEponOltPortDefaultVlanOnuStartId_Type(Integer32):
    """Custom type hwEponOltPortDefaultVlanOnuStartId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HwEponOltPortDefaultVlanOnuStartId_Type.__name__ = "Integer32"
_HwEponOltPortDefaultVlanOnuStartId_Object = MibTableColumn
hwEponOltPortDefaultVlanOnuStartId = _HwEponOltPortDefaultVlanOnuStartId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 12, 1, 3),
    _HwEponOltPortDefaultVlanOnuStartId_Type()
)
hwEponOltPortDefaultVlanOnuStartId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOltPortDefaultVlanOnuStartId.setStatus("current")


class _HwEponOltPortDefaultVlanOnuEndId_Type(Integer32):
    """Custom type hwEponOltPortDefaultVlanOnuEndId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HwEponOltPortDefaultVlanOnuEndId_Type.__name__ = "Integer32"
_HwEponOltPortDefaultVlanOnuEndId_Object = MibTableColumn
hwEponOltPortDefaultVlanOnuEndId = _HwEponOltPortDefaultVlanOnuEndId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 12, 1, 4),
    _HwEponOltPortDefaultVlanOnuEndId_Type()
)
hwEponOltPortDefaultVlanOnuEndId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOltPortDefaultVlanOnuEndId.setStatus("current")
_HwEponOltPortDefaultVlanRowStatus_Type = RowStatus
_HwEponOltPortDefaultVlanRowStatus_Object = MibTableColumn
hwEponOltPortDefaultVlanRowStatus = _HwEponOltPortDefaultVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 12, 1, 51),
    _HwEponOltPortDefaultVlanRowStatus_Type()
)
hwEponOltPortDefaultVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOltPortDefaultVlanRowStatus.setStatus("current")
_HwEponVlanStackingAndMappingTable_Object = MibTable
hwEponVlanStackingAndMappingTable = _HwEponVlanStackingAndMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 13)
)
if mibBuilder.loadTexts:
    hwEponVlanStackingAndMappingTable.setStatus("current")
_HwEponVlanStackingAndMappingEntry_Object = MibTableRow
hwEponVlanStackingAndMappingEntry = _HwEponVlanStackingAndMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 13, 1)
)
hwEponVlanStackingAndMappingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HUAWEI-EPON-MIB", "hwEponOnuIndex"),
    (0, "HUAWEI-EPON-MIB", "hwEponOnuExtSVlanId"),
    (0, "HUAWEI-EPON-MIB", "hwEponOnuIntSStartVlanId"),
    (0, "HUAWEI-EPON-MIB", "hwEponOnuIntSEndVlanId"),
)
if mibBuilder.loadTexts:
    hwEponVlanStackingAndMappingEntry.setStatus("current")


class _HwEponOnuExtSVlanId_Type(Integer32):
    """Custom type hwEponOnuExtSVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwEponOnuExtSVlanId_Type.__name__ = "Integer32"
_HwEponOnuExtSVlanId_Object = MibTableColumn
hwEponOnuExtSVlanId = _HwEponOnuExtSVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 13, 1, 1),
    _HwEponOnuExtSVlanId_Type()
)
hwEponOnuExtSVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEponOnuExtSVlanId.setStatus("current")


class _HwEponOnuIntSStartVlanId_Type(Integer32):
    """Custom type hwEponOnuIntSStartVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwEponOnuIntSStartVlanId_Type.__name__ = "Integer32"
_HwEponOnuIntSStartVlanId_Object = MibTableColumn
hwEponOnuIntSStartVlanId = _HwEponOnuIntSStartVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 13, 1, 2),
    _HwEponOnuIntSStartVlanId_Type()
)
hwEponOnuIntSStartVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEponOnuIntSStartVlanId.setStatus("current")


class _HwEponOnuIntSEndVlanId_Type(Integer32):
    """Custom type hwEponOnuIntSEndVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwEponOnuIntSEndVlanId_Type.__name__ = "Integer32"
_HwEponOnuIntSEndVlanId_Object = MibTableColumn
hwEponOnuIntSEndVlanId = _HwEponOnuIntSEndVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 13, 1, 3),
    _HwEponOnuIntSEndVlanId_Type()
)
hwEponOnuIntSEndVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEponOnuIntSEndVlanId.setStatus("current")


class _HwEponVlanStackingOrMapping_Type(Integer32):
    """Custom type hwEponVlanStackingOrMapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("doubleMapping", 2),
          ("singleMapping", 1),
          ("stacking", 3))
    )


_HwEponVlanStackingOrMapping_Type.__name__ = "Integer32"
_HwEponVlanStackingOrMapping_Object = MibTableColumn
hwEponVlanStackingOrMapping = _HwEponVlanStackingOrMapping_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 13, 1, 4),
    _HwEponVlanStackingOrMapping_Type()
)
hwEponVlanStackingOrMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEponVlanStackingOrMapping.setStatus("current")


class _HwEponOnuDextVlanId_Type(Integer32):
    """Custom type hwEponOnuDextVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwEponOnuDextVlanId_Type.__name__ = "Integer32"
_HwEponOnuDextVlanId_Object = MibTableColumn
hwEponOnuDextVlanId = _HwEponOnuDextVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 13, 1, 5),
    _HwEponOnuDextVlanId_Type()
)
hwEponOnuDextVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOnuDextVlanId.setStatus("current")


class _HwEponOnuDintVlanId_Type(Integer32):
    """Custom type hwEponOnuDintVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwEponOnuDintVlanId_Type.__name__ = "Integer32"
_HwEponOnuDintVlanId_Object = MibTableColumn
hwEponOnuDintVlanId = _HwEponOnuDintVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 13, 1, 6),
    _HwEponOnuDintVlanId_Type()
)
hwEponOnuDintVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOnuDintVlanId.setStatus("current")


class _HwEponOnuPopExtVlanId_Type(Integer32):
    """Custom type hwEponOnuPopExtVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notPop", 2),
          ("pop", 1))
    )


_HwEponOnuPopExtVlanId_Type.__name__ = "Integer32"
_HwEponOnuPopExtVlanId_Object = MibTableColumn
hwEponOnuPopExtVlanId = _HwEponOnuPopExtVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 13, 1, 7),
    _HwEponOnuPopExtVlanId_Type()
)
hwEponOnuPopExtVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOnuPopExtVlanId.setStatus("current")


class _HwEponOnuVlanCopyPri_Type(Integer32):
    """Custom type hwEponOnuVlanCopyPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copy", 1),
          ("notCopy", 2))
    )


_HwEponOnuVlanCopyPri_Type.__name__ = "Integer32"
_HwEponOnuVlanCopyPri_Object = MibTableColumn
hwEponOnuVlanCopyPri = _HwEponOnuVlanCopyPri_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 13, 1, 8),
    _HwEponOnuVlanCopyPri_Type()
)
hwEponOnuVlanCopyPri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOnuVlanCopyPri.setStatus("current")


class _HwEponOnuIntVlanRemarkPri_Type(Integer32):
    """Custom type hwEponOnuIntVlanRemarkPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notRemark", 2),
          ("remark", 1))
    )


_HwEponOnuIntVlanRemarkPri_Type.__name__ = "Integer32"
_HwEponOnuIntVlanRemarkPri_Object = MibTableColumn
hwEponOnuIntVlanRemarkPri = _HwEponOnuIntVlanRemarkPri_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 13, 1, 9),
    _HwEponOnuIntVlanRemarkPri_Type()
)
hwEponOnuIntVlanRemarkPri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOnuIntVlanRemarkPri.setStatus("current")


class _HwEponOnuExtVlanRemarkPri_Type(Integer32):
    """Custom type hwEponOnuExtVlanRemarkPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notRemark", 2),
          ("remark", 1))
    )


_HwEponOnuExtVlanRemarkPri_Type.__name__ = "Integer32"
_HwEponOnuExtVlanRemarkPri_Object = MibTableColumn
hwEponOnuExtVlanRemarkPri = _HwEponOnuExtVlanRemarkPri_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 13, 1, 10),
    _HwEponOnuExtVlanRemarkPri_Type()
)
hwEponOnuExtVlanRemarkPri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOnuExtVlanRemarkPri.setStatus("current")


class _HwEponOnuIntVlanPri_Type(Integer32):
    """Custom type hwEponOnuIntVlanPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_HwEponOnuIntVlanPri_Type.__name__ = "Integer32"
_HwEponOnuIntVlanPri_Object = MibTableColumn
hwEponOnuIntVlanPri = _HwEponOnuIntVlanPri_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 13, 1, 11),
    _HwEponOnuIntVlanPri_Type()
)
hwEponOnuIntVlanPri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOnuIntVlanPri.setStatus("current")


class _HwEponOnuExtVlanPri_Type(Integer32):
    """Custom type hwEponOnuExtVlanPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_HwEponOnuExtVlanPri_Type.__name__ = "Integer32"
_HwEponOnuExtVlanPri_Object = MibTableColumn
hwEponOnuExtVlanPri = _HwEponOnuExtVlanPri_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 13, 1, 12),
    _HwEponOnuExtVlanPri_Type()
)
hwEponOnuExtVlanPri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOnuExtVlanPri.setStatus("current")


class _HwEponVlanMappingBatch_Type(Integer32):
    """Custom type hwEponVlanMappingBatch based on Integer32"""
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


_HwEponVlanMappingBatch_Type.__name__ = "Integer32"
_HwEponVlanMappingBatch_Object = MibTableColumn
hwEponVlanMappingBatch = _HwEponVlanMappingBatch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 13, 1, 13),
    _HwEponVlanMappingBatch_Type()
)
hwEponVlanMappingBatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponVlanMappingBatch.setStatus("current")


class _HwEponVlanMappingOnuStartId_Type(Integer32):
    """Custom type hwEponVlanMappingOnuStartId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HwEponVlanMappingOnuStartId_Type.__name__ = "Integer32"
_HwEponVlanMappingOnuStartId_Object = MibTableColumn
hwEponVlanMappingOnuStartId = _HwEponVlanMappingOnuStartId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 13, 1, 14),
    _HwEponVlanMappingOnuStartId_Type()
)
hwEponVlanMappingOnuStartId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponVlanMappingOnuStartId.setStatus("current")


class _HwEponVlanMappingOnuEndId_Type(Integer32):
    """Custom type hwEponVlanMappingOnuEndId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HwEponVlanMappingOnuEndId_Type.__name__ = "Integer32"
_HwEponVlanMappingOnuEndId_Object = MibTableColumn
hwEponVlanMappingOnuEndId = _HwEponVlanMappingOnuEndId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 13, 1, 15),
    _HwEponVlanMappingOnuEndId_Type()
)
hwEponVlanMappingOnuEndId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponVlanMappingOnuEndId.setStatus("current")
_HwEponVlanMappingRowStatus_Type = RowStatus
_HwEponVlanMappingRowStatus_Object = MibTableColumn
hwEponVlanMappingRowStatus = _HwEponVlanMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 13, 1, 51),
    _HwEponVlanMappingRowStatus_Type()
)
hwEponVlanMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponVlanMappingRowStatus.setStatus("current")
_HwEponOltPortStaticMacTable_Object = MibTable
hwEponOltPortStaticMacTable = _HwEponOltPortStaticMacTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 14)
)
if mibBuilder.loadTexts:
    hwEponOltPortStaticMacTable.setStatus("current")
_HwEponOltPortStaticMacEntry_Object = MibTableRow
hwEponOltPortStaticMacEntry = _HwEponOltPortStaticMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 14, 1)
)
hwEponOltPortStaticMacEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HUAWEI-EPON-MIB", "hwEponOnuIndex"),
    (0, "HUAWEI-EPON-MIB", "hwEponOnuUserMacAddressOrder"),
)
if mibBuilder.loadTexts:
    hwEponOltPortStaticMacEntry.setStatus("current")


class _HwEponOnuUserMacAddressOrder_Type(Integer32):
    """Custom type hwEponOnuUserMacAddressOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HwEponOnuUserMacAddressOrder_Type.__name__ = "Integer32"
_HwEponOnuUserMacAddressOrder_Object = MibTableColumn
hwEponOnuUserMacAddressOrder = _HwEponOnuUserMacAddressOrder_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 14, 1, 1),
    _HwEponOnuUserMacAddressOrder_Type()
)
hwEponOnuUserMacAddressOrder.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEponOnuUserMacAddressOrder.setStatus("current")
_HwEponOnuUserMacAddress_Type = MacAddress
_HwEponOnuUserMacAddress_Object = MibTableColumn
hwEponOnuUserMacAddress = _HwEponOnuUserMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 14, 1, 2),
    _HwEponOnuUserMacAddress_Type()
)
hwEponOnuUserMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOnuUserMacAddress.setStatus("current")
_HwEponOltPortStaticMacRowStatus_Type = RowStatus
_HwEponOltPortStaticMacRowStatus_Object = MibTableColumn
hwEponOltPortStaticMacRowStatus = _HwEponOltPortStaticMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 14, 1, 51),
    _HwEponOltPortStaticMacRowStatus_Type()
)
hwEponOltPortStaticMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOltPortStaticMacRowStatus.setStatus("current")
_HwEponOltPortMacLimitTable_Object = MibTable
hwEponOltPortMacLimitTable = _HwEponOltPortMacLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 15)
)
if mibBuilder.loadTexts:
    hwEponOltPortMacLimitTable.setStatus("current")
_HwEponOltPortMacLimitEntry_Object = MibTableRow
hwEponOltPortMacLimitEntry = _HwEponOltPortMacLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 15, 1)
)
hwEponOltPortMacLimitEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HUAWEI-EPON-MIB", "hwEponOnuIndex"),
)
if mibBuilder.loadTexts:
    hwEponOltPortMacLimitEntry.setStatus("current")


class _HwEponOnuUserMacAddressNumber_Type(Integer32):
    """Custom type hwEponOnuUserMacAddressNumber based on Integer32"""
    defaultValue = 4094

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HwEponOnuUserMacAddressNumber_Type.__name__ = "Integer32"
_HwEponOnuUserMacAddressNumber_Object = MibTableColumn
hwEponOnuUserMacAddressNumber = _HwEponOnuUserMacAddressNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 15, 1, 1),
    _HwEponOnuUserMacAddressNumber_Type()
)
hwEponOnuUserMacAddressNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOnuUserMacAddressNumber.setStatus("current")


class _HwEponOnuForwardAction_Type(Integer32):
    """Custom type hwEponOnuForwardAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("forward", 1))
    )


_HwEponOnuForwardAction_Type.__name__ = "Integer32"
_HwEponOnuForwardAction_Object = MibTableColumn
hwEponOnuForwardAction = _HwEponOnuForwardAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 15, 1, 2),
    _HwEponOnuForwardAction_Type()
)
hwEponOnuForwardAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOnuForwardAction.setStatus("current")


class _HwEponOnuAlarmAction_Type(Integer32):
    """Custom type hwEponOnuAlarmAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notWarning", 2),
          ("warning", 1))
    )


_HwEponOnuAlarmAction_Type.__name__ = "Integer32"
_HwEponOnuAlarmAction_Object = MibTableColumn
hwEponOnuAlarmAction = _HwEponOnuAlarmAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 15, 1, 3),
    _HwEponOnuAlarmAction_Type()
)
hwEponOnuAlarmAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOnuAlarmAction.setStatus("current")
_HwEponOnuMacLimitRowStatus_Type = RowStatus
_HwEponOnuMacLimitRowStatus_Object = MibTableColumn
hwEponOnuMacLimitRowStatus = _HwEponOnuMacLimitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 2, 15, 1, 51),
    _HwEponOnuMacLimitRowStatus_Type()
)
hwEponOnuMacLimitRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOnuMacLimitRowStatus.setStatus("current")
_HwEponProfileObjects_ObjectIdentity = ObjectIdentity
hwEponProfileObjects = _HwEponProfileObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3)
)
_HwEponLineProfileInfoTable_Object = MibTable
hwEponLineProfileInfoTable = _HwEponLineProfileInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hwEponLineProfileInfoTable.setStatus("current")
_HwEponLineProfileInfoEntry_Object = MibTableRow
hwEponLineProfileInfoEntry = _HwEponLineProfileInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 1, 1)
)
hwEponLineProfileInfoEntry.setIndexNames(
    (0, "HUAWEI-EPON-MIB", "hwEponLineProfileNameIndex"),
)
if mibBuilder.loadTexts:
    hwEponLineProfileInfoEntry.setStatus("current")


class _HwEponLineProfileNameIndex_Type(DisplayString):
    """Custom type hwEponLineProfileNameIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwEponLineProfileNameIndex_Type.__name__ = "DisplayString"
_HwEponLineProfileNameIndex_Object = MibTableColumn
hwEponLineProfileNameIndex = _HwEponLineProfileNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 1, 1, 1),
    _HwEponLineProfileNameIndex_Type()
)
hwEponLineProfileNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEponLineProfileNameIndex.setStatus("current")
_HwEponLineProfileBindNum_Type = Integer32
_HwEponLineProfileBindNum_Object = MibTableColumn
hwEponLineProfileBindNum = _HwEponLineProfileBindNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 1, 1, 2),
    _HwEponLineProfileBindNum_Type()
)
hwEponLineProfileBindNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponLineProfileBindNum.setStatus("current")


class _HwEponLineProfileDbaProfileName_Type(DisplayString):
    """Custom type hwEponLineProfileDbaProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwEponLineProfileDbaProfileName_Type.__name__ = "DisplayString"
_HwEponLineProfileDbaProfileName_Object = MibTableColumn
hwEponLineProfileDbaProfileName = _HwEponLineProfileDbaProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 1, 1, 3),
    _HwEponLineProfileDbaProfileName_Type()
)
hwEponLineProfileDbaProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponLineProfileDbaProfileName.setStatus("current")


class _HwEponLineProfileEncryptMode_Type(Integer32):
    """Custom type hwEponLineProfileEncryptMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aes", 1),
          ("off", 3),
          ("tripleChurining", 2))
    )


_HwEponLineProfileEncryptMode_Type.__name__ = "Integer32"
_HwEponLineProfileEncryptMode_Object = MibTableColumn
hwEponLineProfileEncryptMode = _HwEponLineProfileEncryptMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 1, 1, 4),
    _HwEponLineProfileEncryptMode_Type()
)
hwEponLineProfileEncryptMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponLineProfileEncryptMode.setStatus("current")


class _HwEponLineProfileQueueSetIndex1Threshold_Type(DisplayString):
    """Custom type hwEponLineProfileQueueSetIndex1Threshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 500),
    )


_HwEponLineProfileQueueSetIndex1Threshold_Type.__name__ = "DisplayString"
_HwEponLineProfileQueueSetIndex1Threshold_Object = MibTableColumn
hwEponLineProfileQueueSetIndex1Threshold = _HwEponLineProfileQueueSetIndex1Threshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 1, 1, 5),
    _HwEponLineProfileQueueSetIndex1Threshold_Type()
)
hwEponLineProfileQueueSetIndex1Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEponLineProfileQueueSetIndex1Threshold.setStatus("current")


class _HwEponLineProfileQueueSetIndex2Threshold_Type(DisplayString):
    """Custom type hwEponLineProfileQueueSetIndex2Threshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 500),
    )


_HwEponLineProfileQueueSetIndex2Threshold_Type.__name__ = "DisplayString"
_HwEponLineProfileQueueSetIndex2Threshold_Object = MibTableColumn
hwEponLineProfileQueueSetIndex2Threshold = _HwEponLineProfileQueueSetIndex2Threshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 1, 1, 6),
    _HwEponLineProfileQueueSetIndex2Threshold_Type()
)
hwEponLineProfileQueueSetIndex2Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEponLineProfileQueueSetIndex2Threshold.setStatus("current")


class _HwEponLineProfileQueueSetIndex3Threshold_Type(DisplayString):
    """Custom type hwEponLineProfileQueueSetIndex3Threshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 500),
    )


_HwEponLineProfileQueueSetIndex3Threshold_Type.__name__ = "DisplayString"
_HwEponLineProfileQueueSetIndex3Threshold_Object = MibTableColumn
hwEponLineProfileQueueSetIndex3Threshold = _HwEponLineProfileQueueSetIndex3Threshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 1, 1, 7),
    _HwEponLineProfileQueueSetIndex3Threshold_Type()
)
hwEponLineProfileQueueSetIndex3Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEponLineProfileQueueSetIndex3Threshold.setStatus("current")
_HwEponLineProfileRowStatus_Type = RowStatus
_HwEponLineProfileRowStatus_Object = MibTableColumn
hwEponLineProfileRowStatus = _HwEponLineProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 1, 1, 51),
    _HwEponLineProfileRowStatus_Type()
)
hwEponLineProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponLineProfileRowStatus.setStatus("current")
_HwEponOnuSrvProfileInfoTable_Object = MibTable
hwEponOnuSrvProfileInfoTable = _HwEponOnuSrvProfileInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hwEponOnuSrvProfileInfoTable.setStatus("current")
_HwEponOnuSrvProfileInfoEntry_Object = MibTableRow
hwEponOnuSrvProfileInfoEntry = _HwEponOnuSrvProfileInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 2, 1)
)
hwEponOnuSrvProfileInfoEntry.setIndexNames(
    (0, "HUAWEI-EPON-MIB", "hwEponOnuSrvProfNameIndex"),
)
if mibBuilder.loadTexts:
    hwEponOnuSrvProfileInfoEntry.setStatus("current")


class _HwEponOnuSrvProfNameIndex_Type(DisplayString):
    """Custom type hwEponOnuSrvProfNameIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwEponOnuSrvProfNameIndex_Type.__name__ = "DisplayString"
_HwEponOnuSrvProfNameIndex_Object = MibTableColumn
hwEponOnuSrvProfNameIndex = _HwEponOnuSrvProfNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 2, 1, 1),
    _HwEponOnuSrvProfNameIndex_Type()
)
hwEponOnuSrvProfNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEponOnuSrvProfNameIndex.setStatus("current")
_HwEponOnuSrvProfileBindNum_Type = Integer32
_HwEponOnuSrvProfileBindNum_Object = MibTableColumn
hwEponOnuSrvProfileBindNum = _HwEponOnuSrvProfileBindNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 2, 1, 2),
    _HwEponOnuSrvProfileBindNum_Type()
)
hwEponOnuSrvProfileBindNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOnuSrvProfileBindNum.setStatus("current")
_HwEponOnuSrvProfileRowStatus_Type = RowStatus
_HwEponOnuSrvProfileRowStatus_Object = MibTableColumn
hwEponOnuSrvProfileRowStatus = _HwEponOnuSrvProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 2, 1, 51),
    _HwEponOnuSrvProfileRowStatus_Type()
)
hwEponOnuSrvProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOnuSrvProfileRowStatus.setStatus("current")
_HwEponSrvProfileOnuCfgTable_Object = MibTable
hwEponSrvProfileOnuCfgTable = _HwEponSrvProfileOnuCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 3)
)
if mibBuilder.loadTexts:
    hwEponSrvProfileOnuCfgTable.setStatus("current")
_HwEponSrvProfileOnuCfgEntry_Object = MibTableRow
hwEponSrvProfileOnuCfgEntry = _HwEponSrvProfileOnuCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 3, 1)
)
hwEponSrvProfileOnuCfgEntry.setIndexNames(
    (0, "HUAWEI-EPON-MIB", "hwEponOnuSrvProfNameIndex"),
)
if mibBuilder.loadTexts:
    hwEponSrvProfileOnuCfgEntry.setStatus("current")
_HwEponSrvProfileFecMode_Type = EnabledStatus
_HwEponSrvProfileFecMode_Object = MibTableColumn
hwEponSrvProfileFecMode = _HwEponSrvProfileFecMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 3, 1, 4),
    _HwEponSrvProfileFecMode_Type()
)
hwEponSrvProfileFecMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEponSrvProfileFecMode.setStatus("current")


class _HwEponSrvProfileMulticastMode_Type(Integer32):
    """Custom type hwEponSrvProfileMulticastMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ctc", 1),
          ("igmpsnooping", 2))
    )


_HwEponSrvProfileMulticastMode_Type.__name__ = "Integer32"
_HwEponSrvProfileMulticastMode_Object = MibTableColumn
hwEponSrvProfileMulticastMode = _HwEponSrvProfileMulticastMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 3, 1, 5),
    _HwEponSrvProfileMulticastMode_Type()
)
hwEponSrvProfileMulticastMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEponSrvProfileMulticastMode.setStatus("current")
_HwEponSrvProfileMulticastQuickLeaveSwitch_Type = EnabledStatus
_HwEponSrvProfileMulticastQuickLeaveSwitch_Object = MibTableColumn
hwEponSrvProfileMulticastQuickLeaveSwitch = _HwEponSrvProfileMulticastQuickLeaveSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 3, 1, 6),
    _HwEponSrvProfileMulticastQuickLeaveSwitch_Type()
)
hwEponSrvProfileMulticastQuickLeaveSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEponSrvProfileMulticastQuickLeaveSwitch.setStatus("current")
_HwEponSrvProfOnuPortCfgTable_Object = MibTable
hwEponSrvProfOnuPortCfgTable = _HwEponSrvProfOnuPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 4)
)
if mibBuilder.loadTexts:
    hwEponSrvProfOnuPortCfgTable.setStatus("current")
_HwEponSrvProfOnuPortCfgEntry_Object = MibTableRow
hwEponSrvProfOnuPortCfgEntry = _HwEponSrvProfOnuPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 4, 1)
)
hwEponSrvProfOnuPortCfgEntry.setIndexNames(
    (0, "HUAWEI-EPON-MIB", "hwEponOnuSrvProfNameIndex"),
    (0, "HUAWEI-EPON-MIB", "hwEponOnuPortTypeIndex"),
    (0, "HUAWEI-EPON-MIB", "hwEponOnuPortIdIndex"),
)
if mibBuilder.loadTexts:
    hwEponSrvProfOnuPortCfgEntry.setStatus("current")


class _HwEponOnuPortTypeIndex_Type(Integer32):
    """Custom type hwEponOnuPortTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              48)
        )
    )
    namedValues = NamedValues(
        *(("eth1", 1),
          ("eth2", 2),
          ("eth3", 3),
          ("eth4", 48))
    )


_HwEponOnuPortTypeIndex_Type.__name__ = "Integer32"
_HwEponOnuPortTypeIndex_Object = MibTableColumn
hwEponOnuPortTypeIndex = _HwEponOnuPortTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 4, 1, 1),
    _HwEponOnuPortTypeIndex_Type()
)
hwEponOnuPortTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEponOnuPortTypeIndex.setStatus("current")


class _HwEponOnuPortIdIndex_Type(Integer32):
    """Custom type hwEponOnuPortIdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HwEponOnuPortIdIndex_Type.__name__ = "Integer32"
_HwEponOnuPortIdIndex_Object = MibTableColumn
hwEponOnuPortIdIndex = _HwEponOnuPortIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 4, 1, 2),
    _HwEponOnuPortIdIndex_Type()
)
hwEponOnuPortIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEponOnuPortIdIndex.setStatus("current")


class _HwEponSrvProfOnuPortCfgMaxMacAddressNum_Type(Integer32):
    """Custom type hwEponSrvProfOnuPortCfgMaxMacAddressNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_HwEponSrvProfOnuPortCfgMaxMacAddressNum_Type.__name__ = "Integer32"
_HwEponSrvProfOnuPortCfgMaxMacAddressNum_Object = MibTableColumn
hwEponSrvProfOnuPortCfgMaxMacAddressNum = _HwEponSrvProfOnuPortCfgMaxMacAddressNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 4, 1, 3),
    _HwEponSrvProfOnuPortCfgMaxMacAddressNum_Type()
)
hwEponSrvProfOnuPortCfgMaxMacAddressNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEponSrvProfOnuPortCfgMaxMacAddressNum.setStatus("current")


class _HwEponSrvProfOnuPortCfgMulticastStripSwitch_Type(Integer32):
    """Custom type hwEponSrvProfOnuPortCfgMulticastStripSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notStrip", 2),
          ("strip", 1))
    )


_HwEponSrvProfOnuPortCfgMulticastStripSwitch_Type.__name__ = "Integer32"
_HwEponSrvProfOnuPortCfgMulticastStripSwitch_Object = MibTableColumn
hwEponSrvProfOnuPortCfgMulticastStripSwitch = _HwEponSrvProfOnuPortCfgMulticastStripSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 4, 1, 4),
    _HwEponSrvProfOnuPortCfgMulticastStripSwitch_Type()
)
hwEponSrvProfOnuPortCfgMulticastStripSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEponSrvProfOnuPortCfgMulticastStripSwitch.setStatus("current")
_HwEponSrvProfMulticastVlanCfgTable_Object = MibTable
hwEponSrvProfMulticastVlanCfgTable = _HwEponSrvProfMulticastVlanCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 5)
)
if mibBuilder.loadTexts:
    hwEponSrvProfMulticastVlanCfgTable.setStatus("current")
_HwEponSrvProfMulticastVlanCfgEntry_Object = MibTableRow
hwEponSrvProfMulticastVlanCfgEntry = _HwEponSrvProfMulticastVlanCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 5, 1)
)
hwEponSrvProfMulticastVlanCfgEntry.setIndexNames(
    (0, "HUAWEI-EPON-MIB", "hwEponOnuSrvProfNameIndex"),
    (0, "HUAWEI-EPON-MIB", "hwEponOnuPortTypeIndex"),
    (0, "HUAWEI-EPON-MIB", "hwEponOnuPortIdIndex"),
    (0, "HUAWEI-EPON-MIB", "hwEponSrvProfMulticastVlanCfgMulticastVlan"),
)
if mibBuilder.loadTexts:
    hwEponSrvProfMulticastVlanCfgEntry.setStatus("current")


class _HwEponSrvProfMulticastVlanCfgMulticastVlan_Type(Integer32):
    """Custom type hwEponSrvProfMulticastVlanCfgMulticastVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HwEponSrvProfMulticastVlanCfgMulticastVlan_Type.__name__ = "Integer32"
_HwEponSrvProfMulticastVlanCfgMulticastVlan_Object = MibTableColumn
hwEponSrvProfMulticastVlanCfgMulticastVlan = _HwEponSrvProfMulticastVlanCfgMulticastVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 5, 1, 1),
    _HwEponSrvProfMulticastVlanCfgMulticastVlan_Type()
)
hwEponSrvProfMulticastVlanCfgMulticastVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEponSrvProfMulticastVlanCfgMulticastVlan.setStatus("current")
_HwEponSrvProfMulticastVlanCfgRowStatus_Type = RowStatus
_HwEponSrvProfMulticastVlanCfgRowStatus_Object = MibTableColumn
hwEponSrvProfMulticastVlanCfgRowStatus = _HwEponSrvProfMulticastVlanCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 5, 1, 51),
    _HwEponSrvProfMulticastVlanCfgRowStatus_Type()
)
hwEponSrvProfMulticastVlanCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponSrvProfMulticastVlanCfgRowStatus.setStatus("current")
_HwEponSrvProfOnuPortVlanCfgTable_Object = MibTable
hwEponSrvProfOnuPortVlanCfgTable = _HwEponSrvProfOnuPortVlanCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 6)
)
if mibBuilder.loadTexts:
    hwEponSrvProfOnuPortVlanCfgTable.setStatus("current")
_HwEponSrvProfOnuPortVlanCfgEntry_Object = MibTableRow
hwEponSrvProfOnuPortVlanCfgEntry = _HwEponSrvProfOnuPortVlanCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 6, 1)
)
hwEponSrvProfOnuPortVlanCfgEntry.setIndexNames(
    (0, "HUAWEI-EPON-MIB", "hwEponOnuSrvProfNameIndex"),
    (0, "HUAWEI-EPON-MIB", "hwEponOnuPortType"),
    (0, "HUAWEI-EPON-MIB", "hwEponOnuPortId"),
)
if mibBuilder.loadTexts:
    hwEponSrvProfOnuPortVlanCfgEntry.setStatus("current")


class _HwEponOnuPortType_Type(Integer32):
    """Custom type hwEponOnuPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("eth", 1)
    )


_HwEponOnuPortType_Type.__name__ = "Integer32"
_HwEponOnuPortType_Object = MibTableColumn
hwEponOnuPortType = _HwEponOnuPortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 6, 1, 1),
    _HwEponOnuPortType_Type()
)
hwEponOnuPortType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEponOnuPortType.setStatus("current")


class _HwEponOnuPortId_Type(Integer32):
    """Custom type hwEponOnuPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HwEponOnuPortId_Type.__name__ = "Integer32"
_HwEponOnuPortId_Object = MibTableColumn
hwEponOnuPortId = _HwEponOnuPortId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 6, 1, 2),
    _HwEponOnuPortId_Type()
)
hwEponOnuPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEponOnuPortId.setStatus("current")


class _HwEponSrvProfOnuPortVlanMode_Type(Integer32):
    """Custom type hwEponSrvProfOnuPortVlanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("translation", 2),
          ("transmit", 3),
          ("transparent", 1))
    )


_HwEponSrvProfOnuPortVlanMode_Type.__name__ = "Integer32"
_HwEponSrvProfOnuPortVlanMode_Object = MibTableColumn
hwEponSrvProfOnuPortVlanMode = _HwEponSrvProfOnuPortVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 6, 1, 3),
    _HwEponSrvProfOnuPortVlanMode_Type()
)
hwEponSrvProfOnuPortVlanMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponSrvProfOnuPortVlanMode.setStatus("current")
_HwEponSrvProfOnuPortAddToVlanId_Type = Integer32
_HwEponSrvProfOnuPortAddToVlanId_Object = MibTableColumn
hwEponSrvProfOnuPortAddToVlanId = _HwEponSrvProfOnuPortAddToVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 6, 1, 4),
    _HwEponSrvProfOnuPortAddToVlanId_Type()
)
hwEponSrvProfOnuPortAddToVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponSrvProfOnuPortAddToVlanId.setStatus("current")
_HwEponSrvProfOnuPortDefaultVlanId_Type = Integer32
_HwEponSrvProfOnuPortDefaultVlanId_Object = MibTableColumn
hwEponSrvProfOnuPortDefaultVlanId = _HwEponSrvProfOnuPortDefaultVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 6, 1, 5),
    _HwEponSrvProfOnuPortDefaultVlanId_Type()
)
hwEponSrvProfOnuPortDefaultVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponSrvProfOnuPortDefaultVlanId.setStatus("current")
_HwEponSrvProfOnuPortVlanRowStatus_Type = RowStatus
_HwEponSrvProfOnuPortVlanRowStatus_Object = MibTableColumn
hwEponSrvProfOnuPortVlanRowStatus = _HwEponSrvProfOnuPortVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 6, 1, 51),
    _HwEponSrvProfOnuPortVlanRowStatus_Type()
)
hwEponSrvProfOnuPortVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponSrvProfOnuPortVlanRowStatus.setStatus("current")
_HwEponSrvProfOnuPortVlanTranslationTable_Object = MibTable
hwEponSrvProfOnuPortVlanTranslationTable = _HwEponSrvProfOnuPortVlanTranslationTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 7)
)
if mibBuilder.loadTexts:
    hwEponSrvProfOnuPortVlanTranslationTable.setStatus("current")
_HwEponSrvProfOnuPortVlanTranslationEntry_Object = MibTableRow
hwEponSrvProfOnuPortVlanTranslationEntry = _HwEponSrvProfOnuPortVlanTranslationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 7, 1)
)
hwEponSrvProfOnuPortVlanTranslationEntry.setIndexNames(
    (0, "HUAWEI-EPON-MIB", "hwEponOnuSrvProfNameIndex"),
    (0, "HUAWEI-EPON-MIB", "hwEponOnuPortType"),
    (0, "HUAWEI-EPON-MIB", "hwEponOnuPortId"),
    (0, "HUAWEI-EPON-MIB", "hwEponSrvProfOnuPortVlanTranslationCvlanId"),
)
if mibBuilder.loadTexts:
    hwEponSrvProfOnuPortVlanTranslationEntry.setStatus("current")


class _HwEponSrvProfOnuPortVlanTranslationCvlanId_Type(Integer32):
    """Custom type hwEponSrvProfOnuPortVlanTranslationCvlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HwEponSrvProfOnuPortVlanTranslationCvlanId_Type.__name__ = "Integer32"
_HwEponSrvProfOnuPortVlanTranslationCvlanId_Object = MibTableColumn
hwEponSrvProfOnuPortVlanTranslationCvlanId = _HwEponSrvProfOnuPortVlanTranslationCvlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 7, 1, 1),
    _HwEponSrvProfOnuPortVlanTranslationCvlanId_Type()
)
hwEponSrvProfOnuPortVlanTranslationCvlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEponSrvProfOnuPortVlanTranslationCvlanId.setStatus("current")


class _HwEponSrvProfOnuPortVlanTranslationSVlanId_Type(Integer32):
    """Custom type hwEponSrvProfOnuPortVlanTranslationSVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HwEponSrvProfOnuPortVlanTranslationSVlanId_Type.__name__ = "Integer32"
_HwEponSrvProfOnuPortVlanTranslationSVlanId_Object = MibTableColumn
hwEponSrvProfOnuPortVlanTranslationSVlanId = _HwEponSrvProfOnuPortVlanTranslationSVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 7, 1, 2),
    _HwEponSrvProfOnuPortVlanTranslationSVlanId_Type()
)
hwEponSrvProfOnuPortVlanTranslationSVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponSrvProfOnuPortVlanTranslationSVlanId.setStatus("current")
_HwEponSrvProfOnuPortVlanTranslationRowStatus_Type = RowStatus
_HwEponSrvProfOnuPortVlanTranslationRowStatus_Object = MibTableColumn
hwEponSrvProfOnuPortVlanTranslationRowStatus = _HwEponSrvProfOnuPortVlanTranslationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 7, 1, 51),
    _HwEponSrvProfOnuPortVlanTranslationRowStatus_Type()
)
hwEponSrvProfOnuPortVlanTranslationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponSrvProfOnuPortVlanTranslationRowStatus.setStatus("current")
_HwEponDbaProfileInfoTable_Object = MibTable
hwEponDbaProfileInfoTable = _HwEponDbaProfileInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 8)
)
if mibBuilder.loadTexts:
    hwEponDbaProfileInfoTable.setStatus("current")
_HwEponDbaProfileInfoEntry_Object = MibTableRow
hwEponDbaProfileInfoEntry = _HwEponDbaProfileInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 8, 1)
)
hwEponDbaProfileInfoEntry.setIndexNames(
    (0, "HUAWEI-EPON-MIB", "hwEponDbaProfileInfoNameIndex"),
)
if mibBuilder.loadTexts:
    hwEponDbaProfileInfoEntry.setStatus("current")


class _HwEponDbaProfileInfoNameIndex_Type(DisplayString):
    """Custom type hwEponDbaProfileInfoNameIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwEponDbaProfileInfoNameIndex_Type.__name__ = "DisplayString"
_HwEponDbaProfileInfoNameIndex_Object = MibTableColumn
hwEponDbaProfileInfoNameIndex = _HwEponDbaProfileInfoNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 8, 1, 1),
    _HwEponDbaProfileInfoNameIndex_Type()
)
hwEponDbaProfileInfoNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEponDbaProfileInfoNameIndex.setStatus("current")


class _HwEponDbaTypeIndex_Type(Integer32):
    """Custom type hwEponDbaTypeIndex based on Integer32"""
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
        *(("assure", 2),
          ("assureAndmax", 3),
          ("fix", 1),
          ("fixAndassureAndMax", 5),
          ("max", 4))
    )


_HwEponDbaTypeIndex_Type.__name__ = "Integer32"
_HwEponDbaTypeIndex_Object = MibTableColumn
hwEponDbaTypeIndex = _HwEponDbaTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 8, 1, 2),
    _HwEponDbaTypeIndex_Type()
)
hwEponDbaTypeIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponDbaTypeIndex.setStatus("current")


class _HwEponDbaProfileFixedRate_Type(Integer32):
    """Custom type hwEponDbaProfileFixedRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_HwEponDbaProfileFixedRate_Type.__name__ = "Integer32"
_HwEponDbaProfileFixedRate_Object = MibTableColumn
hwEponDbaProfileFixedRate = _HwEponDbaProfileFixedRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 8, 1, 3),
    _HwEponDbaProfileFixedRate_Type()
)
hwEponDbaProfileFixedRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponDbaProfileFixedRate.setStatus("current")


class _HwEponDbaProfileAssuredRate_Type(Integer32):
    """Custom type hwEponDbaProfileAssuredRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_HwEponDbaProfileAssuredRate_Type.__name__ = "Integer32"
_HwEponDbaProfileAssuredRate_Object = MibTableColumn
hwEponDbaProfileAssuredRate = _HwEponDbaProfileAssuredRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 8, 1, 4),
    _HwEponDbaProfileAssuredRate_Type()
)
hwEponDbaProfileAssuredRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponDbaProfileAssuredRate.setStatus("current")


class _HwEponDbaProfileMaxRate_Type(Integer32):
    """Custom type hwEponDbaProfileMaxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_HwEponDbaProfileMaxRate_Type.__name__ = "Integer32"
_HwEponDbaProfileMaxRate_Object = MibTableColumn
hwEponDbaProfileMaxRate = _HwEponDbaProfileMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 8, 1, 5),
    _HwEponDbaProfileMaxRate_Type()
)
hwEponDbaProfileMaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponDbaProfileMaxRate.setStatus("current")
_HwEponDbaProfileReferenceNum_Type = Integer32
_HwEponDbaProfileReferenceNum_Object = MibTableColumn
hwEponDbaProfileReferenceNum = _HwEponDbaProfileReferenceNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 8, 1, 6),
    _HwEponDbaProfileReferenceNum_Type()
)
hwEponDbaProfileReferenceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponDbaProfileReferenceNum.setStatus("current")
_HwEponDbaProfileEntryStatus_Type = RowStatus
_HwEponDbaProfileEntryStatus_Object = MibTableColumn
hwEponDbaProfileEntryStatus = _HwEponDbaProfileEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 8, 1, 51),
    _HwEponDbaProfileEntryStatus_Type()
)
hwEponDbaProfileEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponDbaProfileEntryStatus.setStatus("current")
_HwEponOnuSnmpProfileInfoTable_Object = MibTable
hwEponOnuSnmpProfileInfoTable = _HwEponOnuSnmpProfileInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 9)
)
if mibBuilder.loadTexts:
    hwEponOnuSnmpProfileInfoTable.setStatus("current")
_HwEponOnuSnmpProfileInfoEntry_Object = MibTableRow
hwEponOnuSnmpProfileInfoEntry = _HwEponOnuSnmpProfileInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 9, 1)
)
hwEponOnuSnmpProfileInfoEntry.setIndexNames(
    (0, "HUAWEI-EPON-MIB", "hwEponOnuSnmpProfileInfoNameIndex"),
)
if mibBuilder.loadTexts:
    hwEponOnuSnmpProfileInfoEntry.setStatus("current")


class _HwEponOnuSnmpProfileInfoNameIndex_Type(DisplayString):
    """Custom type hwEponOnuSnmpProfileInfoNameIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwEponOnuSnmpProfileInfoNameIndex_Type.__name__ = "DisplayString"
_HwEponOnuSnmpProfileInfoNameIndex_Object = MibTableColumn
hwEponOnuSnmpProfileInfoNameIndex = _HwEponOnuSnmpProfileInfoNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 9, 1, 1),
    _HwEponOnuSnmpProfileInfoNameIndex_Type()
)
hwEponOnuSnmpProfileInfoNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEponOnuSnmpProfileInfoNameIndex.setStatus("current")


class _HwEponOnuSnmpProfileVersion_Type(Integer32):
    """Custom type hwEponOnuSnmpProfileVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2", 2))
    )


_HwEponOnuSnmpProfileVersion_Type.__name__ = "Integer32"
_HwEponOnuSnmpProfileVersion_Object = MibTableColumn
hwEponOnuSnmpProfileVersion = _HwEponOnuSnmpProfileVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 9, 1, 2),
    _HwEponOnuSnmpProfileVersion_Type()
)
hwEponOnuSnmpProfileVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOnuSnmpProfileVersion.setStatus("current")


class _HwEponOnuSnmpProfileReadCommunityName_Type(DisplayString):
    """Custom type hwEponOnuSnmpProfileReadCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwEponOnuSnmpProfileReadCommunityName_Type.__name__ = "DisplayString"
_HwEponOnuSnmpProfileReadCommunityName_Object = MibTableColumn
hwEponOnuSnmpProfileReadCommunityName = _HwEponOnuSnmpProfileReadCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 9, 1, 3),
    _HwEponOnuSnmpProfileReadCommunityName_Type()
)
hwEponOnuSnmpProfileReadCommunityName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOnuSnmpProfileReadCommunityName.setStatus("current")


class _HwEponOnuSnmpProfileWriteCommunityName_Type(DisplayString):
    """Custom type hwEponOnuSnmpProfileWriteCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwEponOnuSnmpProfileWriteCommunityName_Type.__name__ = "DisplayString"
_HwEponOnuSnmpProfileWriteCommunityName_Object = MibTableColumn
hwEponOnuSnmpProfileWriteCommunityName = _HwEponOnuSnmpProfileWriteCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 9, 1, 4),
    _HwEponOnuSnmpProfileWriteCommunityName_Type()
)
hwEponOnuSnmpProfileWriteCommunityName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOnuSnmpProfileWriteCommunityName.setStatus("current")
_HwEponOnuSnmpProfileTrapHostIp_Type = IpAddress
_HwEponOnuSnmpProfileTrapHostIp_Object = MibTableColumn
hwEponOnuSnmpProfileTrapHostIp = _HwEponOnuSnmpProfileTrapHostIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 9, 1, 5),
    _HwEponOnuSnmpProfileTrapHostIp_Type()
)
hwEponOnuSnmpProfileTrapHostIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOnuSnmpProfileTrapHostIp.setStatus("current")


class _HwEponOnuSnmpProfileTrapHostSrcUdpPort_Type(Integer32):
    """Custom type hwEponOnuSnmpProfileTrapHostSrcUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwEponOnuSnmpProfileTrapHostSrcUdpPort_Type.__name__ = "Integer32"
_HwEponOnuSnmpProfileTrapHostSrcUdpPort_Object = MibTableColumn
hwEponOnuSnmpProfileTrapHostSrcUdpPort = _HwEponOnuSnmpProfileTrapHostSrcUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 9, 1, 6),
    _HwEponOnuSnmpProfileTrapHostSrcUdpPort_Type()
)
hwEponOnuSnmpProfileTrapHostSrcUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOnuSnmpProfileTrapHostSrcUdpPort.setStatus("current")


class _HwEponOnuSnmpProfileSecurityName_Type(DisplayString):
    """Custom type hwEponOnuSnmpProfileSecurityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwEponOnuSnmpProfileSecurityName_Type.__name__ = "DisplayString"
_HwEponOnuSnmpProfileSecurityName_Object = MibTableColumn
hwEponOnuSnmpProfileSecurityName = _HwEponOnuSnmpProfileSecurityName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 9, 1, 7),
    _HwEponOnuSnmpProfileSecurityName_Type()
)
hwEponOnuSnmpProfileSecurityName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOnuSnmpProfileSecurityName.setStatus("current")
_HwEponOnuSnmpProfileRowStatus_Type = RowStatus
_HwEponOnuSnmpProfileRowStatus_Object = MibTableColumn
hwEponOnuSnmpProfileRowStatus = _HwEponOnuSnmpProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 9, 1, 51),
    _HwEponOnuSnmpProfileRowStatus_Type()
)
hwEponOnuSnmpProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOnuSnmpProfileRowStatus.setStatus("current")
_HwEponSrvProfOnuPortClassTable_Object = MibTable
hwEponSrvProfOnuPortClassTable = _HwEponSrvProfOnuPortClassTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 10)
)
if mibBuilder.loadTexts:
    hwEponSrvProfOnuPortClassTable.setStatus("current")
_HwEponSrvProfOnuPortClassEntry_Object = MibTableRow
hwEponSrvProfOnuPortClassEntry = _HwEponSrvProfOnuPortClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 10, 1)
)
hwEponSrvProfOnuPortClassEntry.setIndexNames(
    (0, "HUAWEI-EPON-MIB", "hwEponOnuSrvProfNameIndex"),
    (0, "HUAWEI-EPON-MIB", "hwEponOnuClassifEthPortIndex"),
    (0, "HUAWEI-EPON-MIB", "hwEponOnuPortClassRuleIndexId"),
)
if mibBuilder.loadTexts:
    hwEponSrvProfOnuPortClassEntry.setStatus("current")


class _HwEponOnuClassifEthPortIndex_Type(Integer32):
    """Custom type hwEponOnuClassifEthPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HwEponOnuClassifEthPortIndex_Type.__name__ = "Integer32"
_HwEponOnuClassifEthPortIndex_Object = MibTableColumn
hwEponOnuClassifEthPortIndex = _HwEponOnuClassifEthPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 10, 1, 1),
    _HwEponOnuClassifEthPortIndex_Type()
)
hwEponOnuClassifEthPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEponOnuClassifEthPortIndex.setStatus("current")


class _HwEponOnuPortClassRuleIndexId_Type(Integer32):
    """Custom type hwEponOnuPortClassRuleIndexId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HwEponOnuPortClassRuleIndexId_Type.__name__ = "Integer32"
_HwEponOnuPortClassRuleIndexId_Object = MibTableColumn
hwEponOnuPortClassRuleIndexId = _HwEponOnuPortClassRuleIndexId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 10, 1, 2),
    _HwEponOnuPortClassRuleIndexId_Type()
)
hwEponOnuPortClassRuleIndexId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEponOnuPortClassRuleIndexId.setStatus("current")


class _HwEponOnuPortClassConditionNum_Type(Integer32):
    """Custom type hwEponOnuPortClassConditionNum based on Integer32"""
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
        *(("four", 4),
          ("one", 1),
          ("three", 3),
          ("two", 2))
    )


_HwEponOnuPortClassConditionNum_Type.__name__ = "Integer32"
_HwEponOnuPortClassConditionNum_Object = MibTableColumn
hwEponOnuPortClassConditionNum = _HwEponOnuPortClassConditionNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 10, 1, 3),
    _HwEponOnuPortClassConditionNum_Type()
)
hwEponOnuPortClassConditionNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOnuPortClassConditionNum.setStatus("current")
_HwEponOnuPortClassQueueIndexId_Type = Integer32
_HwEponOnuPortClassQueueIndexId_Object = MibTableColumn
hwEponOnuPortClassQueueIndexId = _HwEponOnuPortClassQueueIndexId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 10, 1, 4),
    _HwEponOnuPortClassQueueIndexId_Type()
)
hwEponOnuPortClassQueueIndexId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOnuPortClassQueueIndexId.setStatus("current")
_HwEponOnuPortClassPriMark_Type = Integer32
_HwEponOnuPortClassPriMark_Object = MibTableColumn
hwEponOnuPortClassPriMark = _HwEponOnuPortClassPriMark_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 10, 1, 5),
    _HwEponOnuPortClassPriMark_Type()
)
hwEponOnuPortClassPriMark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOnuPortClassPriMark.setStatus("current")


class _HwEponOnuPortClassFieldSelect1_Type(Integer32):
    """Custom type hwEponOnuPortClassFieldSelect1 based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("dstIp", 6),
          ("dstMac", 1),
          ("dstPort", 12),
          ("ethPri", 3),
          ("ethType", 5),
          ("ipPrecedence", 10),
          ("ipTosDscp", 9),
          ("ipType", 8),
          ("srcIp", 7),
          ("srcMac", 2),
          ("srcPort", 11),
          ("vlanId", 4))
    )


_HwEponOnuPortClassFieldSelect1_Type.__name__ = "Integer32"
_HwEponOnuPortClassFieldSelect1_Object = MibTableColumn
hwEponOnuPortClassFieldSelect1 = _HwEponOnuPortClassFieldSelect1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 10, 1, 6),
    _HwEponOnuPortClassFieldSelect1_Type()
)
hwEponOnuPortClassFieldSelect1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOnuPortClassFieldSelect1.setStatus("current")


class _HwEponOnuPortClassOperator1_Type(Integer32):
    """Custom type hwEponOnuPortClassOperator1 based on Integer32"""
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
        *(("alwaysMatch", 8),
          ("equal", 2),
          ("exists", 6),
          ("greaterOrEqual", 5),
          ("lessOrEqual", 4),
          ("neverMatch", 1),
          ("notEqual", 3),
          ("notExists", 7))
    )


_HwEponOnuPortClassOperator1_Type.__name__ = "Integer32"
_HwEponOnuPortClassOperator1_Object = MibTableColumn
hwEponOnuPortClassOperator1 = _HwEponOnuPortClassOperator1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 10, 1, 7),
    _HwEponOnuPortClassOperator1_Type()
)
hwEponOnuPortClassOperator1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOnuPortClassOperator1.setStatus("current")
_HwEponOnuPortClassMatchValue1_Type = DisplayString
_HwEponOnuPortClassMatchValue1_Object = MibTableColumn
hwEponOnuPortClassMatchValue1 = _HwEponOnuPortClassMatchValue1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 10, 1, 8),
    _HwEponOnuPortClassMatchValue1_Type()
)
hwEponOnuPortClassMatchValue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOnuPortClassMatchValue1.setStatus("current")


class _HwEponOnuPortClassFieldSelect2_Type(Integer32):
    """Custom type hwEponOnuPortClassFieldSelect2 based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("dstIp", 6),
          ("dstMac", 1),
          ("dstPort", 12),
          ("ethPri", 3),
          ("ethType", 5),
          ("ipPrecedence", 10),
          ("ipTosDscp", 9),
          ("ipType", 8),
          ("srcIp", 7),
          ("srcMac", 2),
          ("srcPort", 11),
          ("vlanId", 4))
    )


_HwEponOnuPortClassFieldSelect2_Type.__name__ = "Integer32"
_HwEponOnuPortClassFieldSelect2_Object = MibTableColumn
hwEponOnuPortClassFieldSelect2 = _HwEponOnuPortClassFieldSelect2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 10, 1, 9),
    _HwEponOnuPortClassFieldSelect2_Type()
)
hwEponOnuPortClassFieldSelect2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOnuPortClassFieldSelect2.setStatus("current")


class _HwEponOnuPortClassOperator2_Type(Integer32):
    """Custom type hwEponOnuPortClassOperator2 based on Integer32"""
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
        *(("alwaysMatch", 8),
          ("equal", 2),
          ("exists", 6),
          ("greaterOrEqual", 5),
          ("lessOrEqual", 4),
          ("neverMatch", 1),
          ("notEqual", 3),
          ("notExists", 7))
    )


_HwEponOnuPortClassOperator2_Type.__name__ = "Integer32"
_HwEponOnuPortClassOperator2_Object = MibTableColumn
hwEponOnuPortClassOperator2 = _HwEponOnuPortClassOperator2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 10, 1, 10),
    _HwEponOnuPortClassOperator2_Type()
)
hwEponOnuPortClassOperator2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOnuPortClassOperator2.setStatus("current")
_HwEponOnuPortClassMatchValue2_Type = DisplayString
_HwEponOnuPortClassMatchValue2_Object = MibTableColumn
hwEponOnuPortClassMatchValue2 = _HwEponOnuPortClassMatchValue2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 10, 1, 11),
    _HwEponOnuPortClassMatchValue2_Type()
)
hwEponOnuPortClassMatchValue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOnuPortClassMatchValue2.setStatus("current")


class _HwEponOnuPortClassFieldSelect3_Type(Integer32):
    """Custom type hwEponOnuPortClassFieldSelect3 based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("dstIp", 6),
          ("dstMac", 1),
          ("dstPort", 12),
          ("ethPri", 3),
          ("ethType", 5),
          ("ipPrecedence", 10),
          ("ipTosDscp", 9),
          ("ipType", 8),
          ("srcIp", 7),
          ("srcMac", 2),
          ("srcPort", 11),
          ("vlanId", 4))
    )


_HwEponOnuPortClassFieldSelect3_Type.__name__ = "Integer32"
_HwEponOnuPortClassFieldSelect3_Object = MibTableColumn
hwEponOnuPortClassFieldSelect3 = _HwEponOnuPortClassFieldSelect3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 10, 1, 12),
    _HwEponOnuPortClassFieldSelect3_Type()
)
hwEponOnuPortClassFieldSelect3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOnuPortClassFieldSelect3.setStatus("current")


class _HwEponOnuPortClassOperator3_Type(Integer32):
    """Custom type hwEponOnuPortClassOperator3 based on Integer32"""
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
        *(("alwaysMatch", 8),
          ("equal", 2),
          ("exists", 6),
          ("greaterOrEqual", 5),
          ("lessOrEqual", 4),
          ("neverMatch", 1),
          ("notEqual", 3),
          ("notExists", 7))
    )


_HwEponOnuPortClassOperator3_Type.__name__ = "Integer32"
_HwEponOnuPortClassOperator3_Object = MibTableColumn
hwEponOnuPortClassOperator3 = _HwEponOnuPortClassOperator3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 10, 1, 13),
    _HwEponOnuPortClassOperator3_Type()
)
hwEponOnuPortClassOperator3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOnuPortClassOperator3.setStatus("current")
_HwEponOnuPortClassMatchValue3_Type = DisplayString
_HwEponOnuPortClassMatchValue3_Object = MibTableColumn
hwEponOnuPortClassMatchValue3 = _HwEponOnuPortClassMatchValue3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 10, 1, 14),
    _HwEponOnuPortClassMatchValue3_Type()
)
hwEponOnuPortClassMatchValue3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOnuPortClassMatchValue3.setStatus("current")


class _HwEponOnuPortClassFieldSelect4_Type(Integer32):
    """Custom type hwEponOnuPortClassFieldSelect4 based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("dstIp", 6),
          ("dstMac", 1),
          ("dstPort", 12),
          ("ethPri", 3),
          ("ethType", 5),
          ("ipPrecedence", 10),
          ("ipTosDscp", 9),
          ("ipType", 8),
          ("srcIp", 7),
          ("srcMac", 2),
          ("srcPort", 11),
          ("vlanId", 4))
    )


_HwEponOnuPortClassFieldSelect4_Type.__name__ = "Integer32"
_HwEponOnuPortClassFieldSelect4_Object = MibTableColumn
hwEponOnuPortClassFieldSelect4 = _HwEponOnuPortClassFieldSelect4_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 10, 1, 15),
    _HwEponOnuPortClassFieldSelect4_Type()
)
hwEponOnuPortClassFieldSelect4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOnuPortClassFieldSelect4.setStatus("current")


class _HwEponOnuPortClassOperator4_Type(Integer32):
    """Custom type hwEponOnuPortClassOperator4 based on Integer32"""
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
        *(("alwaysMatch", 8),
          ("equal", 2),
          ("exists", 6),
          ("greaterOrEqual", 5),
          ("lessOrEqual", 4),
          ("neverMatch", 1),
          ("notEqual", 3),
          ("notExists", 7))
    )


_HwEponOnuPortClassOperator4_Type.__name__ = "Integer32"
_HwEponOnuPortClassOperator4_Object = MibTableColumn
hwEponOnuPortClassOperator4 = _HwEponOnuPortClassOperator4_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 10, 1, 16),
    _HwEponOnuPortClassOperator4_Type()
)
hwEponOnuPortClassOperator4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOnuPortClassOperator4.setStatus("current")
_HwEponOnuPortClassMatchValue4_Type = DisplayString
_HwEponOnuPortClassMatchValue4_Object = MibTableColumn
hwEponOnuPortClassMatchValue4 = _HwEponOnuPortClassMatchValue4_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 10, 1, 17),
    _HwEponOnuPortClassMatchValue4_Type()
)
hwEponOnuPortClassMatchValue4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOnuPortClassMatchValue4.setStatus("current")
_HwEponOnuPortClassProfileRowStatus_Type = RowStatus
_HwEponOnuPortClassProfileRowStatus_Object = MibTableColumn
hwEponOnuPortClassProfileRowStatus = _HwEponOnuPortClassProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 10, 1, 51),
    _HwEponOnuPortClassProfileRowStatus_Type()
)
hwEponOnuPortClassProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponOnuPortClassProfileRowStatus.setStatus("current")
_HwEponSrvProfOnuPortCfgCarTable_Object = MibTable
hwEponSrvProfOnuPortCfgCarTable = _HwEponSrvProfOnuPortCfgCarTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 11)
)
if mibBuilder.loadTexts:
    hwEponSrvProfOnuPortCfgCarTable.setStatus("current")
_HwEponSrvProfOnuPortCfgCarEntry_Object = MibTableRow
hwEponSrvProfOnuPortCfgCarEntry = _HwEponSrvProfOnuPortCfgCarEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 11, 1)
)
hwEponSrvProfOnuPortCfgCarEntry.setIndexNames(
    (0, "HUAWEI-EPON-MIB", "hwEponOnuSrvProfNameIndex"),
    (0, "HUAWEI-EPON-MIB", "hwEponOnuPortTypeIndex"),
    (0, "HUAWEI-EPON-MIB", "hwEponOnuPortIdIndex"),
    (0, "HUAWEI-EPON-MIB", "hwEponSrvProfOnuPortCarCfgDirection"),
)
if mibBuilder.loadTexts:
    hwEponSrvProfOnuPortCfgCarEntry.setStatus("current")


class _HwEponSrvProfOnuPortCarCfgDirection_Type(Integer32):
    """Custom type hwEponSrvProfOnuPortCarCfgDirection based on Integer32"""
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


_HwEponSrvProfOnuPortCarCfgDirection_Type.__name__ = "Integer32"
_HwEponSrvProfOnuPortCarCfgDirection_Object = MibTableColumn
hwEponSrvProfOnuPortCarCfgDirection = _HwEponSrvProfOnuPortCarCfgDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 11, 1, 1),
    _HwEponSrvProfOnuPortCarCfgDirection_Type()
)
hwEponSrvProfOnuPortCarCfgDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEponSrvProfOnuPortCarCfgDirection.setStatus("current")


class _HwEponSrvProfOnuPortCarCfgCir_Type(Integer32):
    """Custom type hwEponSrvProfOnuPortCarCfgCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(640, 1000000),
    )


_HwEponSrvProfOnuPortCarCfgCir_Type.__name__ = "Integer32"
_HwEponSrvProfOnuPortCarCfgCir_Object = MibTableColumn
hwEponSrvProfOnuPortCarCfgCir = _HwEponSrvProfOnuPortCarCfgCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 11, 1, 2),
    _HwEponSrvProfOnuPortCarCfgCir_Type()
)
hwEponSrvProfOnuPortCarCfgCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponSrvProfOnuPortCarCfgCir.setStatus("current")


class _HwEponSrvProfOnuPortCarCfgPir_Type(Integer32):
    """Custom type hwEponSrvProfOnuPortCarCfgPir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_HwEponSrvProfOnuPortCarCfgPir_Type.__name__ = "Integer32"
_HwEponSrvProfOnuPortCarCfgPir_Object = MibTableColumn
hwEponSrvProfOnuPortCarCfgPir = _HwEponSrvProfOnuPortCarCfgPir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 11, 1, 3),
    _HwEponSrvProfOnuPortCarCfgPir_Type()
)
hwEponSrvProfOnuPortCarCfgPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponSrvProfOnuPortCarCfgPir.setStatus("current")


class _HwEponSrvProfOnuPortCarCfgCbs_Type(Integer32):
    """Custom type hwEponSrvProfOnuPortCarCfgCbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1568, 1000000),
    )


_HwEponSrvProfOnuPortCarCfgCbs_Type.__name__ = "Integer32"
_HwEponSrvProfOnuPortCarCfgCbs_Object = MibTableColumn
hwEponSrvProfOnuPortCarCfgCbs = _HwEponSrvProfOnuPortCarCfgCbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 11, 1, 4),
    _HwEponSrvProfOnuPortCarCfgCbs_Type()
)
hwEponSrvProfOnuPortCarCfgCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponSrvProfOnuPortCarCfgCbs.setStatus("current")


class _HwEponSrvProfOnuPortCarCfgEbs_Type(Integer32):
    """Custom type hwEponSrvProfOnuPortCarCfgEbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_HwEponSrvProfOnuPortCarCfgEbs_Type.__name__ = "Integer32"
_HwEponSrvProfOnuPortCarCfgEbs_Object = MibTableColumn
hwEponSrvProfOnuPortCarCfgEbs = _HwEponSrvProfOnuPortCarCfgEbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 11, 1, 5),
    _HwEponSrvProfOnuPortCarCfgEbs_Type()
)
hwEponSrvProfOnuPortCarCfgEbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponSrvProfOnuPortCarCfgEbs.setStatus("current")
_HwEponSrvProfOnuPortCarCfgRowStatus_Type = RowStatus
_HwEponSrvProfOnuPortCarCfgRowStatus_Object = MibTableColumn
hwEponSrvProfOnuPortCarCfgRowStatus = _HwEponSrvProfOnuPortCarCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 3, 11, 1, 51),
    _HwEponSrvProfOnuPortCarCfgRowStatus_Type()
)
hwEponSrvProfOnuPortCarCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEponSrvProfOnuPortCarCfgRowStatus.setStatus("current")
_HwEponStatisticObjects_ObjectIdentity = ObjectIdentity
hwEponStatisticObjects = _HwEponStatisticObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4)
)
_HwEponOltStatisticTable_Object = MibTable
hwEponOltStatisticTable = _HwEponOltStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hwEponOltStatisticTable.setStatus("current")
_HwEponOltStatisticEntry_Object = MibTableRow
hwEponOltStatisticEntry = _HwEponOltStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 1, 1)
)
hwEponOltStatisticEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HUAWEI-EPON-MIB", "hwEponOnuIndex"),
)
if mibBuilder.loadTexts:
    hwEponOltStatisticEntry.setStatus("current")
_HwEponOltStatisticRecvDataFrames_Type = Counter64
_HwEponOltStatisticRecvDataFrames_Object = MibTableColumn
hwEponOltStatisticRecvDataFrames = _HwEponOltStatisticRecvDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 1, 1, 1),
    _HwEponOltStatisticRecvDataFrames_Type()
)
hwEponOltStatisticRecvDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOltStatisticRecvDataFrames.setStatus("current")
_HwEponOltStatisticRecvDataBytes_Type = Counter64
_HwEponOltStatisticRecvDataBytes_Object = MibTableColumn
hwEponOltStatisticRecvDataBytes = _HwEponOltStatisticRecvDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 1, 1, 2),
    _HwEponOltStatisticRecvDataBytes_Type()
)
hwEponOltStatisticRecvDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOltStatisticRecvDataBytes.setStatus("current")
_HwEponOltStatisticRecvMulticastFrames_Type = Counter64
_HwEponOltStatisticRecvMulticastFrames_Object = MibTableColumn
hwEponOltStatisticRecvMulticastFrames = _HwEponOltStatisticRecvMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 1, 1, 3),
    _HwEponOltStatisticRecvMulticastFrames_Type()
)
hwEponOltStatisticRecvMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOltStatisticRecvMulticastFrames.setStatus("current")
_HwEponOltStatisticRecvBoardcastFrames_Type = Counter64
_HwEponOltStatisticRecvBoardcastFrames_Object = MibTableColumn
hwEponOltStatisticRecvBoardcastFrames = _HwEponOltStatisticRecvBoardcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 1, 1, 4),
    _HwEponOltStatisticRecvBoardcastFrames_Type()
)
hwEponOltStatisticRecvBoardcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOltStatisticRecvBoardcastFrames.setStatus("current")
_HwEponOltStatisticRecvErrorFrames_Type = Counter64
_HwEponOltStatisticRecvErrorFrames_Object = MibTableColumn
hwEponOltStatisticRecvErrorFrames = _HwEponOltStatisticRecvErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 1, 1, 5),
    _HwEponOltStatisticRecvErrorFrames_Type()
)
hwEponOltStatisticRecvErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOltStatisticRecvErrorFrames.setStatus("current")
_HwEponOltStatisticRecvErrorBytes_Type = Counter64
_HwEponOltStatisticRecvErrorBytes_Object = MibTableColumn
hwEponOltStatisticRecvErrorBytes = _HwEponOltStatisticRecvErrorBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 1, 1, 6),
    _HwEponOltStatisticRecvErrorBytes_Type()
)
hwEponOltStatisticRecvErrorBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOltStatisticRecvErrorBytes.setStatus("current")
_HwEponOltStatisticRecv64ByteFrames_Type = Counter64
_HwEponOltStatisticRecv64ByteFrames_Object = MibTableColumn
hwEponOltStatisticRecv64ByteFrames = _HwEponOltStatisticRecv64ByteFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 1, 1, 7),
    _HwEponOltStatisticRecv64ByteFrames_Type()
)
hwEponOltStatisticRecv64ByteFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOltStatisticRecv64ByteFrames.setStatus("current")
_HwEponOltStatisticRecv65To127ByteFrames_Type = Counter64
_HwEponOltStatisticRecv65To127ByteFrames_Object = MibTableColumn
hwEponOltStatisticRecv65To127ByteFrames = _HwEponOltStatisticRecv65To127ByteFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 1, 1, 8),
    _HwEponOltStatisticRecv65To127ByteFrames_Type()
)
hwEponOltStatisticRecv65To127ByteFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOltStatisticRecv65To127ByteFrames.setStatus("current")
_HwEponOltStatisticRecv128To255ByteFrames_Type = Counter64
_HwEponOltStatisticRecv128To255ByteFrames_Object = MibTableColumn
hwEponOltStatisticRecv128To255ByteFrames = _HwEponOltStatisticRecv128To255ByteFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 1, 1, 9),
    _HwEponOltStatisticRecv128To255ByteFrames_Type()
)
hwEponOltStatisticRecv128To255ByteFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOltStatisticRecv128To255ByteFrames.setStatus("current")
_HwEponOltStatisticRecv256To511ByteFrames_Type = Counter64
_HwEponOltStatisticRecv256To511ByteFrames_Object = MibTableColumn
hwEponOltStatisticRecv256To511ByteFrames = _HwEponOltStatisticRecv256To511ByteFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 1, 1, 10),
    _HwEponOltStatisticRecv256To511ByteFrames_Type()
)
hwEponOltStatisticRecv256To511ByteFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOltStatisticRecv256To511ByteFrames.setStatus("current")
_HwEponOltStatisticRecv512To1023ByteFrames_Type = Counter64
_HwEponOltStatisticRecv512To1023ByteFrames_Object = MibTableColumn
hwEponOltStatisticRecv512To1023ByteFrames = _HwEponOltStatisticRecv512To1023ByteFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 1, 1, 11),
    _HwEponOltStatisticRecv512To1023ByteFrames_Type()
)
hwEponOltStatisticRecv512To1023ByteFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOltStatisticRecv512To1023ByteFrames.setStatus("current")
_HwEponOltStatisticRecv1024To1518ByteFrames_Type = Counter64
_HwEponOltStatisticRecv1024To1518ByteFrames_Object = MibTableColumn
hwEponOltStatisticRecv1024To1518ByteFrames = _HwEponOltStatisticRecv1024To1518ByteFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 1, 1, 12),
    _HwEponOltStatisticRecv1024To1518ByteFrames_Type()
)
hwEponOltStatisticRecv1024To1518ByteFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOltStatisticRecv1024To1518ByteFrames.setStatus("current")
_HwEponOltStatisticRecvOver1518ByteFrames_Type = Counter64
_HwEponOltStatisticRecvOver1518ByteFrames_Object = MibTableColumn
hwEponOltStatisticRecvOver1518ByteFrames = _HwEponOltStatisticRecvOver1518ByteFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 1, 1, 13),
    _HwEponOltStatisticRecvOver1518ByteFrames_Type()
)
hwEponOltStatisticRecvOver1518ByteFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOltStatisticRecvOver1518ByteFrames.setStatus("current")
_HwEponOltStatisticRecvUndersizeFrames_Type = Counter64
_HwEponOltStatisticRecvUndersizeFrames_Object = MibTableColumn
hwEponOltStatisticRecvUndersizeFrames = _HwEponOltStatisticRecvUndersizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 1, 1, 14),
    _HwEponOltStatisticRecvUndersizeFrames_Type()
)
hwEponOltStatisticRecvUndersizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOltStatisticRecvUndersizeFrames.setStatus("current")
_HwEponOltStatisticRecvOversizeFrames_Type = Counter64
_HwEponOltStatisticRecvOversizeFrames_Object = MibTableColumn
hwEponOltStatisticRecvOversizeFrames = _HwEponOltStatisticRecvOversizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 1, 1, 15),
    _HwEponOltStatisticRecvOversizeFrames_Type()
)
hwEponOltStatisticRecvOversizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOltStatisticRecvOversizeFrames.setStatus("current")
_HwEponOltStatisticRecvFcsErrorFrames_Type = Counter64
_HwEponOltStatisticRecvFcsErrorFrames_Object = MibTableColumn
hwEponOltStatisticRecvFcsErrorFrames = _HwEponOltStatisticRecvFcsErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 1, 1, 16),
    _HwEponOltStatisticRecvFcsErrorFrames_Type()
)
hwEponOltStatisticRecvFcsErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOltStatisticRecvFcsErrorFrames.setStatus("current")
_HwEponOltStatisticUniCastFrames_Type = Counter64
_HwEponOltStatisticUniCastFrames_Object = MibTableColumn
hwEponOltStatisticUniCastFrames = _HwEponOltStatisticUniCastFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 1, 1, 17),
    _HwEponOltStatisticUniCastFrames_Type()
)
hwEponOltStatisticUniCastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOltStatisticUniCastFrames.setStatus("current")
_HwEponOltStatisticRecvOkFrameCnt_Type = Counter64
_HwEponOltStatisticRecvOkFrameCnt_Object = MibTableColumn
hwEponOltStatisticRecvOkFrameCnt = _HwEponOltStatisticRecvOkFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 1, 1, 18),
    _HwEponOltStatisticRecvOkFrameCnt_Type()
)
hwEponOltStatisticRecvOkFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOltStatisticRecvOkFrameCnt.setStatus("current")
_HwEponOltStatisticRecvOkByteCnt_Type = Counter64
_HwEponOltStatisticRecvOkByteCnt_Object = MibTableColumn
hwEponOltStatisticRecvOkByteCnt = _HwEponOltStatisticRecvOkByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 1, 1, 19),
    _HwEponOltStatisticRecvOkByteCnt_Type()
)
hwEponOltStatisticRecvOkByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOltStatisticRecvOkByteCnt.setStatus("current")
_HwEponOltStatisticTransDataFrames_Type = Counter64
_HwEponOltStatisticTransDataFrames_Object = MibTableColumn
hwEponOltStatisticTransDataFrames = _HwEponOltStatisticTransDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 1, 1, 20),
    _HwEponOltStatisticTransDataFrames_Type()
)
hwEponOltStatisticTransDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOltStatisticTransDataFrames.setStatus("current")
_HwEponOltStatisticTransDataBytes_Type = Counter64
_HwEponOltStatisticTransDataBytes_Object = MibTableColumn
hwEponOltStatisticTransDataBytes = _HwEponOltStatisticTransDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 1, 1, 21),
    _HwEponOltStatisticTransDataBytes_Type()
)
hwEponOltStatisticTransDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOltStatisticTransDataBytes.setStatus("current")
_HwEponOltStatisticTransUnicastFrames_Type = Counter64
_HwEponOltStatisticTransUnicastFrames_Object = MibTableColumn
hwEponOltStatisticTransUnicastFrames = _HwEponOltStatisticTransUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 1, 1, 22),
    _HwEponOltStatisticTransUnicastFrames_Type()
)
hwEponOltStatisticTransUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOltStatisticTransUnicastFrames.setStatus("current")
_HwEponOltStatisticTransMulticastFrames_Type = Counter64
_HwEponOltStatisticTransMulticastFrames_Object = MibTableColumn
hwEponOltStatisticTransMulticastFrames = _HwEponOltStatisticTransMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 1, 1, 23),
    _HwEponOltStatisticTransMulticastFrames_Type()
)
hwEponOltStatisticTransMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOltStatisticTransMulticastFrames.setStatus("current")
_HwEponOltStatisticTransBoardcastFrames_Type = Counter64
_HwEponOltStatisticTransBoardcastFrames_Object = MibTableColumn
hwEponOltStatisticTransBoardcastFrames = _HwEponOltStatisticTransBoardcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 1, 1, 24),
    _HwEponOltStatisticTransBoardcastFrames_Type()
)
hwEponOltStatisticTransBoardcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOltStatisticTransBoardcastFrames.setStatus("current")
_HwEponOltStatisticTrans64ByteFrames_Type = Counter64
_HwEponOltStatisticTrans64ByteFrames_Object = MibTableColumn
hwEponOltStatisticTrans64ByteFrames = _HwEponOltStatisticTrans64ByteFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 1, 1, 25),
    _HwEponOltStatisticTrans64ByteFrames_Type()
)
hwEponOltStatisticTrans64ByteFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOltStatisticTrans64ByteFrames.setStatus("current")
_HwEponOltStatisticTrans65To127ByteFrames_Type = Counter64
_HwEponOltStatisticTrans65To127ByteFrames_Object = MibTableColumn
hwEponOltStatisticTrans65To127ByteFrames = _HwEponOltStatisticTrans65To127ByteFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 1, 1, 26),
    _HwEponOltStatisticTrans65To127ByteFrames_Type()
)
hwEponOltStatisticTrans65To127ByteFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOltStatisticTrans65To127ByteFrames.setStatus("current")
_HwEponOltStatisticTrans128To255ByteFrames_Type = Counter64
_HwEponOltStatisticTrans128To255ByteFrames_Object = MibTableColumn
hwEponOltStatisticTrans128To255ByteFrames = _HwEponOltStatisticTrans128To255ByteFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 1, 1, 27),
    _HwEponOltStatisticTrans128To255ByteFrames_Type()
)
hwEponOltStatisticTrans128To255ByteFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOltStatisticTrans128To255ByteFrames.setStatus("current")
_HwEponOltStatisticTrans256To511ByteFrames_Type = Counter64
_HwEponOltStatisticTrans256To511ByteFrames_Object = MibTableColumn
hwEponOltStatisticTrans256To511ByteFrames = _HwEponOltStatisticTrans256To511ByteFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 1, 1, 28),
    _HwEponOltStatisticTrans256To511ByteFrames_Type()
)
hwEponOltStatisticTrans256To511ByteFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOltStatisticTrans256To511ByteFrames.setStatus("current")
_HwEponOltStatisticTrans512To1023ByteFrames_Type = Counter64
_HwEponOltStatisticTrans512To1023ByteFrames_Object = MibTableColumn
hwEponOltStatisticTrans512To1023ByteFrames = _HwEponOltStatisticTrans512To1023ByteFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 1, 1, 29),
    _HwEponOltStatisticTrans512To1023ByteFrames_Type()
)
hwEponOltStatisticTrans512To1023ByteFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOltStatisticTrans512To1023ByteFrames.setStatus("current")
_HwEponOltStatisticTrans1024To1518ByteFrames_Type = Counter64
_HwEponOltStatisticTrans1024To1518ByteFrames_Object = MibTableColumn
hwEponOltStatisticTrans1024To1518ByteFrames = _HwEponOltStatisticTrans1024To1518ByteFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 1, 1, 30),
    _HwEponOltStatisticTrans1024To1518ByteFrames_Type()
)
hwEponOltStatisticTrans1024To1518ByteFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOltStatisticTrans1024To1518ByteFrames.setStatus("current")
_HwEponOltStatisticTransOver1518ByteFrames_Type = Counter64
_HwEponOltStatisticTransOver1518ByteFrames_Object = MibTableColumn
hwEponOltStatisticTransOver1518ByteFrames = _HwEponOltStatisticTransOver1518ByteFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 1, 1, 31),
    _HwEponOltStatisticTransOver1518ByteFrames_Type()
)
hwEponOltStatisticTransOver1518ByteFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOltStatisticTransOver1518ByteFrames.setStatus("current")
_HwEponOltStatisticTransFcsErrorFrames_Type = Counter64
_HwEponOltStatisticTransFcsErrorFrames_Object = MibTableColumn
hwEponOltStatisticTransFcsErrorFrames = _HwEponOltStatisticTransFcsErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 1, 1, 32),
    _HwEponOltStatisticTransFcsErrorFrames_Type()
)
hwEponOltStatisticTransFcsErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOltStatisticTransFcsErrorFrames.setStatus("current")


class _HwEponOltStatisticClear_Type(Integer32):
    """Custom type hwEponOltStatisticClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_HwEponOltStatisticClear_Type.__name__ = "Integer32"
_HwEponOltStatisticClear_Object = MibTableColumn
hwEponOltStatisticClear = _HwEponOltStatisticClear_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 1, 1, 33),
    _HwEponOltStatisticClear_Type()
)
hwEponOltStatisticClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEponOltStatisticClear.setStatus("current")
_HwEponOnuPonStatisticTable_Object = MibTable
hwEponOnuPonStatisticTable = _HwEponOnuPonStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 2)
)
if mibBuilder.loadTexts:
    hwEponOnuPonStatisticTable.setStatus("current")
_HwEponOnuPonStatisticEntry_Object = MibTableRow
hwEponOnuPonStatisticEntry = _HwEponOnuPonStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 2, 1)
)
hwEponOnuPonStatisticEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HUAWEI-EPON-MIB", "hwEponOnuIndex"),
)
if mibBuilder.loadTexts:
    hwEponOnuPonStatisticEntry.setStatus("current")
_HwEponOnuPonStatisticRcv1024To1518byteFrm_Type = Counter64
_HwEponOnuPonStatisticRcv1024To1518byteFrm_Object = MibTableColumn
hwEponOnuPonStatisticRcv1024To1518byteFrm = _HwEponOnuPonStatisticRcv1024To1518byteFrm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 2, 1, 1),
    _HwEponOnuPonStatisticRcv1024To1518byteFrm_Type()
)
hwEponOnuPonStatisticRcv1024To1518byteFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuPonStatisticRcv1024To1518byteFrm.setStatus("current")
_HwEponOnuPonStatisticRcv128To255byteFrm_Type = Counter64
_HwEponOnuPonStatisticRcv128To255byteFrm_Object = MibTableColumn
hwEponOnuPonStatisticRcv128To255byteFrm = _HwEponOnuPonStatisticRcv128To255byteFrm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 2, 1, 2),
    _HwEponOnuPonStatisticRcv128To255byteFrm_Type()
)
hwEponOnuPonStatisticRcv128To255byteFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuPonStatisticRcv128To255byteFrm.setStatus("current")
_HwEponOnuPonStatisticRcv256To511byteFrm_Type = Counter64
_HwEponOnuPonStatisticRcv256To511byteFrm_Object = MibTableColumn
hwEponOnuPonStatisticRcv256To511byteFrm = _HwEponOnuPonStatisticRcv256To511byteFrm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 2, 1, 3),
    _HwEponOnuPonStatisticRcv256To511byteFrm_Type()
)
hwEponOnuPonStatisticRcv256To511byteFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuPonStatisticRcv256To511byteFrm.setStatus("current")
_HwEponOnuPonStatisticRcv512To1023byteFrm_Type = Counter64
_HwEponOnuPonStatisticRcv512To1023byteFrm_Object = MibTableColumn
hwEponOnuPonStatisticRcv512To1023byteFrm = _HwEponOnuPonStatisticRcv512To1023byteFrm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 2, 1, 4),
    _HwEponOnuPonStatisticRcv512To1023byteFrm_Type()
)
hwEponOnuPonStatisticRcv512To1023byteFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuPonStatisticRcv512To1023byteFrm.setStatus("current")
_HwEponOnuPonStatisticRcv64byteFrm_Type = Counter64
_HwEponOnuPonStatisticRcv64byteFrm_Object = MibTableColumn
hwEponOnuPonStatisticRcv64byteFrm = _HwEponOnuPonStatisticRcv64byteFrm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 2, 1, 5),
    _HwEponOnuPonStatisticRcv64byteFrm_Type()
)
hwEponOnuPonStatisticRcv64byteFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuPonStatisticRcv64byteFrm.setStatus("current")
_HwEponOnuPonStatisticRcv65To127byteFrm_Type = Counter64
_HwEponOnuPonStatisticRcv65To127byteFrm_Object = MibTableColumn
hwEponOnuPonStatisticRcv65To127byteFrm = _HwEponOnuPonStatisticRcv65To127byteFrm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 2, 1, 6),
    _HwEponOnuPonStatisticRcv65To127byteFrm_Type()
)
hwEponOnuPonStatisticRcv65To127byteFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuPonStatisticRcv65To127byteFrm.setStatus("current")
_HwEponOnuPonStatisticRcvBcFrame_Type = Counter64
_HwEponOnuPonStatisticRcvBcFrame_Object = MibTableColumn
hwEponOnuPonStatisticRcvBcFrame = _HwEponOnuPonStatisticRcvBcFrame_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 2, 1, 7),
    _HwEponOnuPonStatisticRcvBcFrame_Type()
)
hwEponOnuPonStatisticRcvBcFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuPonStatisticRcvBcFrame.setStatus("current")
_HwEponOnuPonStatisticRcvByte_Type = Counter64
_HwEponOnuPonStatisticRcvByte_Object = MibTableColumn
hwEponOnuPonStatisticRcvByte = _HwEponOnuPonStatisticRcvByte_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 2, 1, 8),
    _HwEponOnuPonStatisticRcvByte_Type()
)
hwEponOnuPonStatisticRcvByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuPonStatisticRcvByte.setStatus("current")
_HwEponOnuPonStatisticRcvCrc8Err_Type = Counter64
_HwEponOnuPonStatisticRcvCrc8Err_Object = MibTableColumn
hwEponOnuPonStatisticRcvCrc8Err = _HwEponOnuPonStatisticRcvCrc8Err_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 2, 1, 9),
    _HwEponOnuPonStatisticRcvCrc8Err_Type()
)
hwEponOnuPonStatisticRcvCrc8Err.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuPonStatisticRcvCrc8Err.setStatus("current")
_HwEponOnuPonStatisticRcvDelayByte_Type = Counter64
_HwEponOnuPonStatisticRcvDelayByte_Object = MibTableColumn
hwEponOnuPonStatisticRcvDelayByte = _HwEponOnuPonStatisticRcvDelayByte_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 2, 1, 10),
    _HwEponOnuPonStatisticRcvDelayByte_Type()
)
hwEponOnuPonStatisticRcvDelayByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuPonStatisticRcvDelayByte.setStatus("current")
_HwEponOnuPonStatisticRcvDelayMax_Type = Counter64
_HwEponOnuPonStatisticRcvDelayMax_Object = MibTableColumn
hwEponOnuPonStatisticRcvDelayMax = _HwEponOnuPonStatisticRcvDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 2, 1, 11),
    _HwEponOnuPonStatisticRcvDelayMax_Type()
)
hwEponOnuPonStatisticRcvDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuPonStatisticRcvDelayMax.setStatus("current")
_HwEponOnuPonStatisticRcvDelayThreshold_Type = Counter64
_HwEponOnuPonStatisticRcvDelayThreshold_Object = MibTableColumn
hwEponOnuPonStatisticRcvDelayThreshold = _HwEponOnuPonStatisticRcvDelayThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 2, 1, 12),
    _HwEponOnuPonStatisticRcvDelayThreshold_Type()
)
hwEponOnuPonStatisticRcvDelayThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuPonStatisticRcvDelayThreshold.setStatus("current")
_HwEponOnuPonStatisticRcvDropByte_Type = Counter64
_HwEponOnuPonStatisticRcvDropByte_Object = MibTableColumn
hwEponOnuPonStatisticRcvDropByte = _HwEponOnuPonStatisticRcvDropByte_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 2, 1, 13),
    _HwEponOnuPonStatisticRcvDropByte_Type()
)
hwEponOnuPonStatisticRcvDropByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuPonStatisticRcvDropByte.setStatus("current")
_HwEponOnuPonStatisticRcvDropFrm_Type = Counter64
_HwEponOnuPonStatisticRcvDropFrm_Object = MibTableColumn
hwEponOnuPonStatisticRcvDropFrm = _HwEponOnuPonStatisticRcvDropFrm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 2, 1, 14),
    _HwEponOnuPonStatisticRcvDropFrm_Type()
)
hwEponOnuPonStatisticRcvDropFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuPonStatisticRcvDropFrm.setStatus("current")
_HwEponOnuPonStatisticRcvErrFrm_Type = Counter64
_HwEponOnuPonStatisticRcvErrFrm_Object = MibTableColumn
hwEponOnuPonStatisticRcvErrFrm = _HwEponOnuPonStatisticRcvErrFrm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 2, 1, 15),
    _HwEponOnuPonStatisticRcvErrFrm_Type()
)
hwEponOnuPonStatisticRcvErrFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuPonStatisticRcvErrFrm.setStatus("current")
_HwEponOnuPonStatisticRcvErrOntDestinedByte_Type = Counter64
_HwEponOnuPonStatisticRcvErrOntDestinedByte_Object = MibTableColumn
hwEponOnuPonStatisticRcvErrOntDestinedByte = _HwEponOnuPonStatisticRcvErrOntDestinedByte_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 2, 1, 16),
    _HwEponOnuPonStatisticRcvErrOntDestinedByte_Type()
)
hwEponOnuPonStatisticRcvErrOntDestinedByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuPonStatisticRcvErrOntDestinedByte.setStatus("current")
_HwEponOnuPonStatisticRcvFcsErr_Type = Counter64
_HwEponOnuPonStatisticRcvFcsErr_Object = MibTableColumn
hwEponOnuPonStatisticRcvFcsErr = _HwEponOnuPonStatisticRcvFcsErr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 2, 1, 17),
    _HwEponOnuPonStatisticRcvFcsErr_Type()
)
hwEponOnuPonStatisticRcvFcsErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuPonStatisticRcvFcsErr.setStatus("current")
_HwEponOnuPonStatisticRcvFrame_Type = Counter64
_HwEponOnuPonStatisticRcvFrame_Object = MibTableColumn
hwEponOnuPonStatisticRcvFrame = _HwEponOnuPonStatisticRcvFrame_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 2, 1, 18),
    _HwEponOnuPonStatisticRcvFrame_Type()
)
hwEponOnuPonStatisticRcvFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuPonStatisticRcvFrame.setStatus("current")
_HwEponOnuPonStatisticRcvGreatThan1518byteFrm_Type = Counter64
_HwEponOnuPonStatisticRcvGreatThan1518byteFrm_Object = MibTableColumn
hwEponOnuPonStatisticRcvGreatThan1518byteFrm = _HwEponOnuPonStatisticRcvGreatThan1518byteFrm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 2, 1, 19),
    _HwEponOnuPonStatisticRcvGreatThan1518byteFrm_Type()
)
hwEponOnuPonStatisticRcvGreatThan1518byteFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuPonStatisticRcvGreatThan1518byteFrm.setStatus("current")
_HwEponOnuPonStatisticRcvInvalidSldFrm_Type = Counter64
_HwEponOnuPonStatisticRcvInvalidSldFrm_Object = MibTableColumn
hwEponOnuPonStatisticRcvInvalidSldFrm = _HwEponOnuPonStatisticRcvInvalidSldFrm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 2, 1, 20),
    _HwEponOnuPonStatisticRcvInvalidSldFrm_Type()
)
hwEponOnuPonStatisticRcvInvalidSldFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuPonStatisticRcvInvalidSldFrm.setStatus("current")
_HwEponOnuPonStatisticRcvLaserPower_Type = Counter64
_HwEponOnuPonStatisticRcvLaserPower_Object = MibTableColumn
hwEponOnuPonStatisticRcvLaserPower = _HwEponOnuPonStatisticRcvLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 2, 1, 21),
    _HwEponOnuPonStatisticRcvLaserPower_Type()
)
hwEponOnuPonStatisticRcvLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuPonStatisticRcvLaserPower.setStatus("current")
_HwEponOnuPonStatisticRcvLineCodeErr_Type = Counter64
_HwEponOnuPonStatisticRcvLineCodeErr_Object = MibTableColumn
hwEponOnuPonStatisticRcvLineCodeErr = _HwEponOnuPonStatisticRcvLineCodeErr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 2, 1, 22),
    _HwEponOnuPonStatisticRcvLineCodeErr_Type()
)
hwEponOnuPonStatisticRcvLineCodeErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuPonStatisticRcvLineCodeErr.setStatus("current")
_HwEponOnuPonStatisticRcvMcFrame_Type = Counter64
_HwEponOnuPonStatisticRcvMcFrame_Object = MibTableColumn
hwEponOnuPonStatisticRcvMcFrame = _HwEponOnuPonStatisticRcvMcFrame_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 2, 1, 23),
    _HwEponOnuPonStatisticRcvMcFrame_Type()
)
hwEponOnuPonStatisticRcvMcFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuPonStatisticRcvMcFrame.setStatus("current")
_HwEponOnuPonStatisticRcvOntDestinedByte_Type = Counter64
_HwEponOnuPonStatisticRcvOntDestinedByte_Object = MibTableColumn
hwEponOnuPonStatisticRcvOntDestinedByte = _HwEponOnuPonStatisticRcvOntDestinedByte_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 2, 1, 24),
    _HwEponOnuPonStatisticRcvOntDestinedByte_Type()
)
hwEponOnuPonStatisticRcvOntDestinedByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuPonStatisticRcvOntDestinedByte.setStatus("current")
_HwEponOnuPonStatisticRcvUcFrame_Type = Counter64
_HwEponOnuPonStatisticRcvUcFrame_Object = MibTableColumn
hwEponOnuPonStatisticRcvUcFrame = _HwEponOnuPonStatisticRcvUcFrame_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 2, 1, 25),
    _HwEponOnuPonStatisticRcvUcFrame_Type()
)
hwEponOnuPonStatisticRcvUcFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuPonStatisticRcvUcFrame.setStatus("current")
_HwEponOnuPonStatisticRcvUndersizeFrm_Type = Counter64
_HwEponOnuPonStatisticRcvUndersizeFrm_Object = MibTableColumn
hwEponOnuPonStatisticRcvUndersizeFrm = _HwEponOnuPonStatisticRcvUndersizeFrm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 2, 1, 26),
    _HwEponOnuPonStatisticRcvUndersizeFrm_Type()
)
hwEponOnuPonStatisticRcvUndersizeFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuPonStatisticRcvUndersizeFrm.setStatus("current")
_HwEponOnuPonStatisticSend1024To1518byteFrm_Type = Counter64
_HwEponOnuPonStatisticSend1024To1518byteFrm_Object = MibTableColumn
hwEponOnuPonStatisticSend1024To1518byteFrm = _HwEponOnuPonStatisticSend1024To1518byteFrm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 2, 1, 27),
    _HwEponOnuPonStatisticSend1024To1518byteFrm_Type()
)
hwEponOnuPonStatisticSend1024To1518byteFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuPonStatisticSend1024To1518byteFrm.setStatus("current")
_HwEponOnuPonStatisticSend128To255byteFrm_Type = Counter64
_HwEponOnuPonStatisticSend128To255byteFrm_Object = MibTableColumn
hwEponOnuPonStatisticSend128To255byteFrm = _HwEponOnuPonStatisticSend128To255byteFrm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 2, 1, 28),
    _HwEponOnuPonStatisticSend128To255byteFrm_Type()
)
hwEponOnuPonStatisticSend128To255byteFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuPonStatisticSend128To255byteFrm.setStatus("current")
_HwEponOnuPonStatisticSend256To511byteFrm_Type = Counter64
_HwEponOnuPonStatisticSend256To511byteFrm_Object = MibTableColumn
hwEponOnuPonStatisticSend256To511byteFrm = _HwEponOnuPonStatisticSend256To511byteFrm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 2, 1, 29),
    _HwEponOnuPonStatisticSend256To511byteFrm_Type()
)
hwEponOnuPonStatisticSend256To511byteFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuPonStatisticSend256To511byteFrm.setStatus("current")
_HwEponOnuPonStatisticSend512To1023byteFrm_Type = Counter64
_HwEponOnuPonStatisticSend512To1023byteFrm_Object = MibTableColumn
hwEponOnuPonStatisticSend512To1023byteFrm = _HwEponOnuPonStatisticSend512To1023byteFrm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 2, 1, 30),
    _HwEponOnuPonStatisticSend512To1023byteFrm_Type()
)
hwEponOnuPonStatisticSend512To1023byteFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuPonStatisticSend512To1023byteFrm.setStatus("current")
_HwEponOnuPonStatisticSend64byteFrm_Type = Counter64
_HwEponOnuPonStatisticSend64byteFrm_Object = MibTableColumn
hwEponOnuPonStatisticSend64byteFrm = _HwEponOnuPonStatisticSend64byteFrm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 2, 1, 31),
    _HwEponOnuPonStatisticSend64byteFrm_Type()
)
hwEponOnuPonStatisticSend64byteFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuPonStatisticSend64byteFrm.setStatus("current")
_HwEponOnuPonStatisticSend65To127byteFrm_Type = Counter64
_HwEponOnuPonStatisticSend65To127byteFrm_Object = MibTableColumn
hwEponOnuPonStatisticSend65To127byteFrm = _HwEponOnuPonStatisticSend65To127byteFrm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 2, 1, 32),
    _HwEponOnuPonStatisticSend65To127byteFrm_Type()
)
hwEponOnuPonStatisticSend65To127byteFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuPonStatisticSend65To127byteFrm.setStatus("current")
_HwEponOnuPonStatisticSendBcFrame_Type = Counter64
_HwEponOnuPonStatisticSendBcFrame_Object = MibTableColumn
hwEponOnuPonStatisticSendBcFrame = _HwEponOnuPonStatisticSendBcFrame_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 2, 1, 33),
    _HwEponOnuPonStatisticSendBcFrame_Type()
)
hwEponOnuPonStatisticSendBcFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuPonStatisticSendBcFrame.setStatus("current")
_HwEponOnuPonStatisticSendByte_Type = Counter64
_HwEponOnuPonStatisticSendByte_Object = MibTableColumn
hwEponOnuPonStatisticSendByte = _HwEponOnuPonStatisticSendByte_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 2, 1, 34),
    _HwEponOnuPonStatisticSendByte_Type()
)
hwEponOnuPonStatisticSendByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuPonStatisticSendByte.setStatus("current")
_HwEponOnuPonStatisticSendDelayByte_Type = Counter64
_HwEponOnuPonStatisticSendDelayByte_Object = MibTableColumn
hwEponOnuPonStatisticSendDelayByte = _HwEponOnuPonStatisticSendDelayByte_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 2, 1, 35),
    _HwEponOnuPonStatisticSendDelayByte_Type()
)
hwEponOnuPonStatisticSendDelayByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuPonStatisticSendDelayByte.setStatus("current")
_HwEponOnuPonStatisticSendDelayMax_Type = Counter64
_HwEponOnuPonStatisticSendDelayMax_Object = MibTableColumn
hwEponOnuPonStatisticSendDelayMax = _HwEponOnuPonStatisticSendDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 2, 1, 36),
    _HwEponOnuPonStatisticSendDelayMax_Type()
)
hwEponOnuPonStatisticSendDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuPonStatisticSendDelayMax.setStatus("current")
_HwEponOnuPonStatisticSendDelayThreshold_Type = Counter64
_HwEponOnuPonStatisticSendDelayThreshold_Object = MibTableColumn
hwEponOnuPonStatisticSendDelayThreshold = _HwEponOnuPonStatisticSendDelayThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 2, 1, 37),
    _HwEponOnuPonStatisticSendDelayThreshold_Type()
)
hwEponOnuPonStatisticSendDelayThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuPonStatisticSendDelayThreshold.setStatus("current")
_HwEponOnuPonStatisticSendDropByte_Type = Counter64
_HwEponOnuPonStatisticSendDropByte_Object = MibTableColumn
hwEponOnuPonStatisticSendDropByte = _HwEponOnuPonStatisticSendDropByte_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 2, 1, 38),
    _HwEponOnuPonStatisticSendDropByte_Type()
)
hwEponOnuPonStatisticSendDropByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuPonStatisticSendDropByte.setStatus("current")
_HwEponOnuPonStatisticSendDropFrm_Type = Counter64
_HwEponOnuPonStatisticSendDropFrm_Object = MibTableColumn
hwEponOnuPonStatisticSendDropFrm = _HwEponOnuPonStatisticSendDropFrm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 2, 1, 39),
    _HwEponOnuPonStatisticSendDropFrm_Type()
)
hwEponOnuPonStatisticSendDropFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuPonStatisticSendDropFrm.setStatus("current")
_HwEponOnuPonStatisticSendFrame_Type = Counter64
_HwEponOnuPonStatisticSendFrame_Object = MibTableColumn
hwEponOnuPonStatisticSendFrame = _HwEponOnuPonStatisticSendFrame_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 2, 1, 40),
    _HwEponOnuPonStatisticSendFrame_Type()
)
hwEponOnuPonStatisticSendFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuPonStatisticSendFrame.setStatus("current")
_HwEponOnuPonStatisticSendGreatThan1518byteFrm_Type = Counter64
_HwEponOnuPonStatisticSendGreatThan1518byteFrm_Object = MibTableColumn
hwEponOnuPonStatisticSendGreatThan1518byteFrm = _HwEponOnuPonStatisticSendGreatThan1518byteFrm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 2, 1, 41),
    _HwEponOnuPonStatisticSendGreatThan1518byteFrm_Type()
)
hwEponOnuPonStatisticSendGreatThan1518byteFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuPonStatisticSendGreatThan1518byteFrm.setStatus("current")
_HwEponOnuPonStatisticSendMcFrame_Type = Counter64
_HwEponOnuPonStatisticSendMcFrame_Object = MibTableColumn
hwEponOnuPonStatisticSendMcFrame = _HwEponOnuPonStatisticSendMcFrame_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 2, 1, 42),
    _HwEponOnuPonStatisticSendMcFrame_Type()
)
hwEponOnuPonStatisticSendMcFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuPonStatisticSendMcFrame.setStatus("current")
_HwEponOnuPonStatisticSendUcFrame_Type = Counter64
_HwEponOnuPonStatisticSendUcFrame_Object = MibTableColumn
hwEponOnuPonStatisticSendUcFrame = _HwEponOnuPonStatisticSendUcFrame_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 2, 1, 43),
    _HwEponOnuPonStatisticSendUcFrame_Type()
)
hwEponOnuPonStatisticSendUcFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuPonStatisticSendUcFrame.setStatus("current")
_HwEponOnuPonStatisticSendUnusedByte_Type = Counter64
_HwEponOnuPonStatisticSendUnusedByte_Object = MibTableColumn
hwEponOnuPonStatisticSendUnusedByte = _HwEponOnuPonStatisticSendUnusedByte_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 2, 1, 44),
    _HwEponOnuPonStatisticSendUnusedByte_Type()
)
hwEponOnuPonStatisticSendUnusedByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuPonStatisticSendUnusedByte.setStatus("current")


class _HwEponOnuPonStatisticClear_Type(Integer32):
    """Custom type hwEponOnuPonStatisticClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_HwEponOnuPonStatisticClear_Type.__name__ = "Integer32"
_HwEponOnuPonStatisticClear_Object = MibTableColumn
hwEponOnuPonStatisticClear = _HwEponOnuPonStatisticClear_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 2, 1, 45),
    _HwEponOnuPonStatisticClear_Type()
)
hwEponOnuPonStatisticClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEponOnuPonStatisticClear.setStatus("current")
_HwEponOnuUniStatisticTable_Object = MibTable
hwEponOnuUniStatisticTable = _HwEponOnuUniStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 3)
)
if mibBuilder.loadTexts:
    hwEponOnuUniStatisticTable.setStatus("current")
_HwEponOnuUniStatisticEntry_Object = MibTableRow
hwEponOnuUniStatisticEntry = _HwEponOnuUniStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 3, 1)
)
hwEponOnuUniStatisticEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HUAWEI-EPON-MIB", "hwEponOnuIndex"),
    (0, "HUAWEI-EPON-MIB", "hwEponOnuEthPortId"),
)
if mibBuilder.loadTexts:
    hwEponOnuUniStatisticEntry.setStatus("current")
_HwEponOnuUniStatisticRecvFrames_Type = Counter64
_HwEponOnuUniStatisticRecvFrames_Object = MibTableColumn
hwEponOnuUniStatisticRecvFrames = _HwEponOnuUniStatisticRecvFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 3, 1, 1),
    _HwEponOnuUniStatisticRecvFrames_Type()
)
hwEponOnuUniStatisticRecvFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuUniStatisticRecvFrames.setStatus("current")
_HwEponOnuUniStatisticRecvMulticastFrames_Type = Counter64
_HwEponOnuUniStatisticRecvMulticastFrames_Object = MibTableColumn
hwEponOnuUniStatisticRecvMulticastFrames = _HwEponOnuUniStatisticRecvMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 3, 1, 2),
    _HwEponOnuUniStatisticRecvMulticastFrames_Type()
)
hwEponOnuUniStatisticRecvMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuUniStatisticRecvMulticastFrames.setStatus("current")
_HwEponOnuUniStatisticRecvBroadcastFrames_Type = Counter64
_HwEponOnuUniStatisticRecvBroadcastFrames_Object = MibTableColumn
hwEponOnuUniStatisticRecvBroadcastFrames = _HwEponOnuUniStatisticRecvBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 3, 1, 3),
    _HwEponOnuUniStatisticRecvBroadcastFrames_Type()
)
hwEponOnuUniStatisticRecvBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuUniStatisticRecvBroadcastFrames.setStatus("current")
_HwEponOnuUniStatisticRecv64OctetFrames_Type = Counter64
_HwEponOnuUniStatisticRecv64OctetFrames_Object = MibTableColumn
hwEponOnuUniStatisticRecv64OctetFrames = _HwEponOnuUniStatisticRecv64OctetFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 3, 1, 4),
    _HwEponOnuUniStatisticRecv64OctetFrames_Type()
)
hwEponOnuUniStatisticRecv64OctetFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuUniStatisticRecv64OctetFrames.setStatus("current")
_HwEponOnuUniStatisticRecv65To127OctetFrames_Type = Counter64
_HwEponOnuUniStatisticRecv65To127OctetFrames_Object = MibTableColumn
hwEponOnuUniStatisticRecv65To127OctetFrames = _HwEponOnuUniStatisticRecv65To127OctetFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 3, 1, 5),
    _HwEponOnuUniStatisticRecv65To127OctetFrames_Type()
)
hwEponOnuUniStatisticRecv65To127OctetFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuUniStatisticRecv65To127OctetFrames.setStatus("current")
_HwEponOnuUniStatisticRecv128To255OctetFrames_Type = Counter64
_HwEponOnuUniStatisticRecv128To255OctetFrames_Object = MibTableColumn
hwEponOnuUniStatisticRecv128To255OctetFrames = _HwEponOnuUniStatisticRecv128To255OctetFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 3, 1, 6),
    _HwEponOnuUniStatisticRecv128To255OctetFrames_Type()
)
hwEponOnuUniStatisticRecv128To255OctetFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuUniStatisticRecv128To255OctetFrames.setStatus("current")
_HwEponOnuUniStatisticRecv256To511OctetFrames_Type = Counter64
_HwEponOnuUniStatisticRecv256To511OctetFrames_Object = MibTableColumn
hwEponOnuUniStatisticRecv256To511OctetFrames = _HwEponOnuUniStatisticRecv256To511OctetFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 3, 1, 7),
    _HwEponOnuUniStatisticRecv256To511OctetFrames_Type()
)
hwEponOnuUniStatisticRecv256To511OctetFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuUniStatisticRecv256To511OctetFrames.setStatus("current")
_HwEponOnuUniStatisticRecv512To1023OctetFrames_Type = Counter64
_HwEponOnuUniStatisticRecv512To1023OctetFrames_Object = MibTableColumn
hwEponOnuUniStatisticRecv512To1023OctetFrames = _HwEponOnuUniStatisticRecv512To1023OctetFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 3, 1, 8),
    _HwEponOnuUniStatisticRecv512To1023OctetFrames_Type()
)
hwEponOnuUniStatisticRecv512To1023OctetFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuUniStatisticRecv512To1023OctetFrames.setStatus("current")
_HwEponOnuUniStatisticRecv1024To1518OctetFrames_Type = Counter64
_HwEponOnuUniStatisticRecv1024To1518OctetFrames_Object = MibTableColumn
hwEponOnuUniStatisticRecv1024To1518OctetFrames = _HwEponOnuUniStatisticRecv1024To1518OctetFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 3, 1, 9),
    _HwEponOnuUniStatisticRecv1024To1518OctetFrames_Type()
)
hwEponOnuUniStatisticRecv1024To1518OctetFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuUniStatisticRecv1024To1518OctetFrames.setStatus("current")
_HwEponOnuUniStatisticRecvUndersizeFrames_Type = Counter64
_HwEponOnuUniStatisticRecvUndersizeFrames_Object = MibTableColumn
hwEponOnuUniStatisticRecvUndersizeFrames = _HwEponOnuUniStatisticRecvUndersizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 3, 1, 10),
    _HwEponOnuUniStatisticRecvUndersizeFrames_Type()
)
hwEponOnuUniStatisticRecvUndersizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuUniStatisticRecvUndersizeFrames.setStatus("current")
_HwEponOnuUniStatisticRecvTooLongFrames_Type = Counter64
_HwEponOnuUniStatisticRecvTooLongFrames_Object = MibTableColumn
hwEponOnuUniStatisticRecvTooLongFrames = _HwEponOnuUniStatisticRecvTooLongFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 3, 1, 11),
    _HwEponOnuUniStatisticRecvTooLongFrames_Type()
)
hwEponOnuUniStatisticRecvTooLongFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuUniStatisticRecvTooLongFrames.setStatus("current")
_HwEponOnuUniStatisticTransDropFrames_Type = Counter64
_HwEponOnuUniStatisticTransDropFrames_Object = MibTableColumn
hwEponOnuUniStatisticTransDropFrames = _HwEponOnuUniStatisticTransDropFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 3, 1, 12),
    _HwEponOnuUniStatisticTransDropFrames_Type()
)
hwEponOnuUniStatisticTransDropFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuUniStatisticTransDropFrames.setStatus("current")
_HwEponOnuUniStatisticTransFrames_Type = Counter64
_HwEponOnuUniStatisticTransFrames_Object = MibTableColumn
hwEponOnuUniStatisticTransFrames = _HwEponOnuUniStatisticTransFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 3, 1, 13),
    _HwEponOnuUniStatisticTransFrames_Type()
)
hwEponOnuUniStatisticTransFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuUniStatisticTransFrames.setStatus("current")
_HwEponOnuUniStatisticTransMtuExceededDiscardFrames_Type = Counter64
_HwEponOnuUniStatisticTransMtuExceededDiscardFrames_Object = MibTableColumn
hwEponOnuUniStatisticTransMtuExceededDiscardFrames = _HwEponOnuUniStatisticTransMtuExceededDiscardFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 3, 1, 14),
    _HwEponOnuUniStatisticTransMtuExceededDiscardFrames_Type()
)
hwEponOnuUniStatisticTransMtuExceededDiscardFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuUniStatisticTransMtuExceededDiscardFrames.setStatus("current")


class _HwEponOnuUniStatisticClear_Type(Integer32):
    """Custom type hwEponOnuUniStatisticClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_HwEponOnuUniStatisticClear_Type.__name__ = "Integer32"
_HwEponOnuUniStatisticClear_Object = MibTableColumn
hwEponOnuUniStatisticClear = _HwEponOnuUniStatisticClear_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 4, 3, 1, 15),
    _HwEponOnuUniStatisticClear_Type()
)
hwEponOnuUniStatisticClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEponOnuUniStatisticClear.setStatus("current")
_HwEponDisplayAlarmObjects_ObjectIdentity = ObjectIdentity
hwEponDisplayAlarmObjects = _HwEponDisplayAlarmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 5)
)
_HwEponOnuAlarmStateTable_Object = MibTable
hwEponOnuAlarmStateTable = _HwEponOnuAlarmStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hwEponOnuAlarmStateTable.setStatus("current")
_HwEponOnuAlarmStateEntry_Object = MibTableRow
hwEponOnuAlarmStateEntry = _HwEponOnuAlarmStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 5, 1, 1)
)
hwEponOnuAlarmStateEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HUAWEI-EPON-MIB", "hwEponOnuIndex"),
)
if mibBuilder.loadTexts:
    hwEponOnuAlarmStateEntry.setStatus("current")


class _HwEponOnuAlarmStateKeyExchangeFail_Type(Integer32):
    """Custom type hwEponOnuAlarmStateKeyExchangeFail based on Integer32"""
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


_HwEponOnuAlarmStateKeyExchangeFail_Type.__name__ = "Integer32"
_HwEponOnuAlarmStateKeyExchangeFail_Object = MibTableColumn
hwEponOnuAlarmStateKeyExchangeFail = _HwEponOnuAlarmStateKeyExchangeFail_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 5, 1, 1, 1),
    _HwEponOnuAlarmStateKeyExchangeFail_Type()
)
hwEponOnuAlarmStateKeyExchangeFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuAlarmStateKeyExchangeFail.setStatus("current")


class _HwEponOnuAlarmStateDyingGasp_Type(Integer32):
    """Custom type hwEponOnuAlarmStateDyingGasp based on Integer32"""
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


_HwEponOnuAlarmStateDyingGasp_Type.__name__ = "Integer32"
_HwEponOnuAlarmStateDyingGasp_Object = MibTableColumn
hwEponOnuAlarmStateDyingGasp = _HwEponOnuAlarmStateDyingGasp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 5, 1, 1, 2),
    _HwEponOnuAlarmStateDyingGasp_Type()
)
hwEponOnuAlarmStateDyingGasp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuAlarmStateDyingGasp.setStatus("current")


class _HwEponOnuAlarmStateLinkFault_Type(Integer32):
    """Custom type hwEponOnuAlarmStateLinkFault based on Integer32"""
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


_HwEponOnuAlarmStateLinkFault_Type.__name__ = "Integer32"
_HwEponOnuAlarmStateLinkFault_Object = MibTableColumn
hwEponOnuAlarmStateLinkFault = _HwEponOnuAlarmStateLinkFault_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 5, 1, 1, 3),
    _HwEponOnuAlarmStateLinkFault_Type()
)
hwEponOnuAlarmStateLinkFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuAlarmStateLinkFault.setStatus("current")


class _HwEponOnuFirmWareLoadStateSucc_Type(Integer32):
    """Custom type hwEponOnuFirmWareLoadStateSucc based on Integer32"""
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


_HwEponOnuFirmWareLoadStateSucc_Type.__name__ = "Integer32"
_HwEponOnuFirmWareLoadStateSucc_Object = MibTableColumn
hwEponOnuFirmWareLoadStateSucc = _HwEponOnuFirmWareLoadStateSucc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 5, 1, 1, 4),
    _HwEponOnuFirmWareLoadStateSucc_Type()
)
hwEponOnuFirmWareLoadStateSucc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEponOnuFirmWareLoadStateSucc.setStatus("current")


class _HwEponOnuFirmWareLoadStateFault_Type(Integer32):
    """Custom type hwEponOnuFirmWareLoadStateFault based on Integer32"""
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


_HwEponOnuFirmWareLoadStateFault_Type.__name__ = "Integer32"
_HwEponOnuFirmWareLoadStateFault_Object = MibTableColumn
hwEponOnuFirmWareLoadStateFault = _HwEponOnuFirmWareLoadStateFault_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 5, 1, 1, 5),
    _HwEponOnuFirmWareLoadStateFault_Type()
)
hwEponOnuFirmWareLoadStateFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuFirmWareLoadStateFault.setStatus("current")
_HwEponOnuUniAlarmStateTable_Object = MibTable
hwEponOnuUniAlarmStateTable = _HwEponOnuUniAlarmStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 5, 2)
)
if mibBuilder.loadTexts:
    hwEponOnuUniAlarmStateTable.setStatus("current")
_HwEponOnuUniAlarmStateEntry_Object = MibTableRow
hwEponOnuUniAlarmStateEntry = _HwEponOnuUniAlarmStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 5, 2, 1)
)
hwEponOnuUniAlarmStateEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HUAWEI-EPON-MIB", "hwEponOnuIndex"),
    (0, "HUAWEI-EPON-MIB", "hwEponOnuPortId"),
)
if mibBuilder.loadTexts:
    hwEponOnuUniAlarmStateEntry.setStatus("current")


class _HwEponOnuUniAlarmStateTransmitFail_Type(Integer32):
    """Custom type hwEponOnuUniAlarmStateTransmitFail based on Integer32"""
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


_HwEponOnuUniAlarmStateTransmitFail_Type.__name__ = "Integer32"
_HwEponOnuUniAlarmStateTransmitFail_Object = MibTableColumn
hwEponOnuUniAlarmStateTransmitFail = _HwEponOnuUniAlarmStateTransmitFail_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 5, 2, 1, 2),
    _HwEponOnuUniAlarmStateTransmitFail_Type()
)
hwEponOnuUniAlarmStateTransmitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuUniAlarmStateTransmitFail.setStatus("current")


class _HwEponOnuUniAlarmStateLos_Type(Integer32):
    """Custom type hwEponOnuUniAlarmStateLos based on Integer32"""
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


_HwEponOnuUniAlarmStateLos_Type.__name__ = "Integer32"
_HwEponOnuUniAlarmStateLos_Object = MibTableColumn
hwEponOnuUniAlarmStateLos = _HwEponOnuUniAlarmStateLos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 5, 2, 1, 3),
    _HwEponOnuUniAlarmStateLos_Type()
)
hwEponOnuUniAlarmStateLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOnuUniAlarmStateLos.setStatus("current")
_HwEponOltAlarmStateTable_Object = MibTable
hwEponOltAlarmStateTable = _HwEponOltAlarmStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 5, 3)
)
if mibBuilder.loadTexts:
    hwEponOltAlarmStateTable.setStatus("current")
_HwEponOltAlarmStateEntry_Object = MibTableRow
hwEponOltAlarmStateEntry = _HwEponOltAlarmStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 5, 3, 1)
)
hwEponOltAlarmStateEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hwEponOltAlarmStateEntry.setStatus("current")


class _HwEponOltAlarmStateDegrade_Type(Integer32):
    """Custom type hwEponOltAlarmStateDegrade based on Integer32"""
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


_HwEponOltAlarmStateDegrade_Type.__name__ = "Integer32"
_HwEponOltAlarmStateDegrade_Object = MibTableColumn
hwEponOltAlarmStateDegrade = _HwEponOltAlarmStateDegrade_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 5, 3, 1, 1),
    _HwEponOltAlarmStateDegrade_Type()
)
hwEponOltAlarmStateDegrade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEponOltAlarmStateDegrade.setStatus("current")
_HwEponTrapObjects_ObjectIdentity = ObjectIdentity
hwEponTrapObjects = _HwEponTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 6)
)
_HwEponSlotIndex_Type = Integer32
_HwEponSlotIndex_Object = MibScalar
hwEponSlotIndex = _HwEponSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 6, 1),
    _HwEponSlotIndex_Type()
)
hwEponSlotIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwEponSlotIndex.setStatus("current")
_HwEponCardIndex_Type = Integer32
_HwEponCardIndex_Object = MibScalar
hwEponCardIndex = _HwEponCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 6, 2),
    _HwEponCardIndex_Type()
)
hwEponCardIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwEponCardIndex.setStatus("current")
_HwEponPortIndex_Type = Integer32
_HwEponPortIndex_Object = MibScalar
hwEponPortIndex = _HwEponPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 6, 3),
    _HwEponPortIndex_Type()
)
hwEponPortIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwEponPortIndex.setStatus("current")
_HwEponTrapOnuId_Type = Integer32
_HwEponTrapOnuId_Object = MibScalar
hwEponTrapOnuId = _HwEponTrapOnuId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 6, 4),
    _HwEponTrapOnuId_Type()
)
hwEponTrapOnuId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwEponTrapOnuId.setStatus("current")
_HwEponTrapMac_Type = DisplayString
_HwEponTrapMac_Object = MibScalar
hwEponTrapMac = _HwEponTrapMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 6, 5),
    _HwEponTrapMac_Type()
)
hwEponTrapMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwEponTrapMac.setStatus("current")
_HwEponTrapPwd_Type = DisplayString
_HwEponTrapPwd_Object = MibScalar
hwEponTrapPwd = _HwEponTrapPwd_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 6, 6),
    _HwEponTrapPwd_Type()
)
hwEponTrapPwd.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwEponTrapPwd.setStatus("current")
_HwEponTrap_ObjectIdentity = ObjectIdentity
hwEponTrap = _HwEponTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 7)
)
_HwEponConformance_ObjectIdentity = ObjectIdentity
hwEponConformance = _HwEponConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 8)
)
_HwEponCompliances_ObjectIdentity = ObjectIdentity
hwEponCompliances = _HwEponCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 8, 1)
)
_HwEponGroups_ObjectIdentity = ObjectIdentity
hwEponGroups = _HwEponGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 8, 2)
)

# Managed Objects groups

hwEponGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 8, 2, 1)
)
hwEponGlobalGroup.setObjects(
      *(("HUAWEI-EPON-MIB", "hwEponAutoFindOnuAge"),
        ("HUAWEI-EPON-MIB", "hwEponCtcOuiId"),
        ("HUAWEI-EPON-MIB", "hwEponChangePasswordAge"))
)
if mibBuilder.loadTexts:
    hwEponGlobalGroup.setStatus("current")

hwEponControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 8, 2, 2)
)
hwEponControlGroup.setObjects(
      *(("HUAWEI-EPON-MIB", "hwEponOltControlfarthest"),
        ("HUAWEI-EPON-MIB", "hwEponOltControlAutofindOnuEnable"),
        ("HUAWEI-EPON-MIB", "hwEponOltControlStatus"),
        ("HUAWEI-EPON-MIB", "hwEponOltControlUpStreamBandWidth"),
        ("HUAWEI-EPON-MIB", "hwEponOltControlDownStreamBandWidth"),
        ("HUAWEI-EPON-MIB", "hwEponOnuId"),
        ("HUAWEI-EPON-MIB", "hwEponOnuAuthMode"),
        ("HUAWEI-EPON-MIB", "hwEponOnuMacAddress"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPassword"),
        ("HUAWEI-EPON-MIB", "hwEponOnuTimeout"),
        ("HUAWEI-EPON-MIB", "hwEponOnuManagementMode"),
        ("HUAWEI-EPON-MIB", "hwEponOnuLineProfName"),
        ("HUAWEI-EPON-MIB", "hwEponOnuServiceProfName"),
        ("HUAWEI-EPON-MIB", "hwEponOnuActiveStatus"),
        ("HUAWEI-EPON-MIB", "hwEponOnuDescription"),
        ("HUAWEI-EPON-MIB", "hwEponOnuVendorId"),
        ("HUAWEI-EPON-MIB", "hwEponOnuModel"),
        ("HUAWEI-EPON-MIB", "hwEponOnuOnuIdentifier"),
        ("HUAWEI-EPON-MIB", "hwEponOnuHardwareVersion"),
        ("HUAWEI-EPON-MIB", "hwEponOnuSoftwareVersion"),
        ("HUAWEI-EPON-MIB", "hwEponOnuChipVenderId"),
        ("HUAWEI-EPON-MIB", "hwEponOnuChipModel"),
        ("HUAWEI-EPON-MIB", "hwEponOnuChipVersion"),
        ("HUAWEI-EPON-MIB", "hwEponOnuChipDesignDate"),
        ("HUAWEI-EPON-MIB", "hwEponOnuFirmwareVersion"),
        ("HUAWEI-EPON-MIB", "hwEponOnuReset"),
        ("HUAWEI-EPON-MIB", "hwEponOnuReRegister"),
        ("HUAWEI-EPON-MIB", "hwEponOnuReDiscovery"),
        ("HUAWEI-EPON-MIB", "hwEponOnuRunStatus"),
        ("HUAWEI-EPON-MIB", "hwEponOnuDistance"),
        ("HUAWEI-EPON-MIB", "hwEponOnuRtt"),
        ("HUAWEI-EPON-MIB", "hwEponOnuLastUpTime"),
        ("HUAWEI-EPON-MIB", "hwEponOnuLastDownTime"),
        ("HUAWEI-EPON-MIB", "hwEponOnuLastDownCause"),
        ("HUAWEI-EPON-MIB", "hwEponAutoFindOnuInfoMacAddress"),
        ("HUAWEI-EPON-MIB", "hwEponAutoFindOnuInfoPasswordValue"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPotsPortNum"),
        ("HUAWEI-EPON-MIB", "hwEponOnuFePortsNum"),
        ("HUAWEI-EPON-MIB", "hwEponOnuGePortsNum"),
        ("HUAWEI-EPON-MIB", "hwEponOnuTdmPortsNum"),
        ("HUAWEI-EPON-MIB", "hwEponOnuFecSupport"),
        ("HUAWEI-EPON-MIB", "hwEponOnuSupportBackupBattery"),
        ("HUAWEI-EPON-MIB", "hwEponOnuUpQueueNum"),
        ("HUAWEI-EPON-MIB", "hwEponOnuUpQueueNumPerPort"),
        ("HUAWEI-EPON-MIB", "hwEponOnuDownQueueNum"),
        ("HUAWEI-EPON-MIB", "hwEponOnuDownQueueNumPerPort"),
        ("HUAWEI-EPON-MIB", "hwEponOnuFePortList"),
        ("HUAWEI-EPON-MIB", "hwEponOnuGePortList"),
        ("HUAWEI-EPON-MIB", "hwEponOnuSupportMulticastQuickLeave"),
        ("HUAWEI-EPON-MIB", "hwEponOnuIpAddress"),
        ("HUAWEI-EPON-MIB", "hwEponOnuNetMask"),
        ("HUAWEI-EPON-MIB", "hwEponOnuNetGateway"),
        ("HUAWEI-EPON-MIB", "hwEponOnuEthOperateStatus"),
        ("HUAWEI-EPON-MIB", "hwEponOnuEthFlowcontrolSwitch"),
        ("HUAWEI-EPON-MIB", "hwEponOnuTdmPortOperateStatus"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPotsPortOperateStatus"),
        ("HUAWEI-EPON-MIB", "hwEponOltPortDefaultVlanId"),
        ("HUAWEI-EPON-MIB", "hwEponOltPortDefaultVlanBatch"),
        ("HUAWEI-EPON-MIB", "hwEponOltPortDefaultVlanOnuStartId"),
        ("HUAWEI-EPON-MIB", "hwEponOltPortDefaultVlanOnuEndId"),
        ("HUAWEI-EPON-MIB", "hwEponOnuCarProfileNameIndex"),
        ("HUAWEI-EPON-MIB", "hwEponOnuTrafficPolicyNameIndex"),
        ("HUAWEI-EPON-MIB", "hwEponVlanStackingOrMapping"),
        ("HUAWEI-EPON-MIB", "hwEponOnuDextVlanId"),
        ("HUAWEI-EPON-MIB", "hwEponOnuDintVlanId"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPopExtVlanId"),
        ("HUAWEI-EPON-MIB", "hwEponOnuVlanCopyPri"),
        ("HUAWEI-EPON-MIB", "hwEponOnuIntVlanRemarkPri"),
        ("HUAWEI-EPON-MIB", "hwEponOnuExtVlanRemarkPri"),
        ("HUAWEI-EPON-MIB", "hwEponOnuIntVlanPri"),
        ("HUAWEI-EPON-MIB", "hwEponOnuExtVlanPri"),
        ("HUAWEI-EPON-MIB", "hwEponVlanMappingBatch"),
        ("HUAWEI-EPON-MIB", "hwEponVlanMappingOnuStartId"),
        ("HUAWEI-EPON-MIB", "hwEponVlanMappingOnuEndId"),
        ("HUAWEI-EPON-MIB", "hwEponOnuUserMacAddress"),
        ("HUAWEI-EPON-MIB", "hwEponOnuUserMacAddressNumber"),
        ("HUAWEI-EPON-MIB", "hwEponOnuForwardAction"),
        ("HUAWEI-EPON-MIB", "hwEponOnuAlarmAction"),
        ("HUAWEI-EPON-MIB", "hwEponOnuRowStatus"),
        ("HUAWEI-EPON-MIB", "hwEponOnuCfgCarRowStatus"),
        ("HUAWEI-EPON-MIB", "hwEponOltPortDefaultVlanRowStatus"),
        ("HUAWEI-EPON-MIB", "hwEponVlanMappingRowStatus"),
        ("HUAWEI-EPON-MIB", "hwEponOnuIpRowStates"),
        ("HUAWEI-EPON-MIB", "hwEponOltPortStaticMacRowStatus"),
        ("HUAWEI-EPON-MIB", "hwEponOnuMacLimitRowStatus"),
        ("HUAWEI-EPON-MIB", "hwEponOnuIpManageVlan"))
)
if mibBuilder.loadTexts:
    hwEponControlGroup.setStatus("current")

hwEponProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 8, 2, 3)
)
hwEponProfileGroup.setObjects(
      *(("HUAWEI-EPON-MIB", "hwEponLineProfileBindNum"),
        ("HUAWEI-EPON-MIB", "hwEponLineProfileDbaProfileName"),
        ("HUAWEI-EPON-MIB", "hwEponLineProfileEncryptMode"),
        ("HUAWEI-EPON-MIB", "hwEponLineProfileQueueSetIndex1Threshold"),
        ("HUAWEI-EPON-MIB", "hwEponLineProfileQueueSetIndex2Threshold"),
        ("HUAWEI-EPON-MIB", "hwEponLineProfileQueueSetIndex3Threshold"),
        ("HUAWEI-EPON-MIB", "hwEponOnuSrvProfileBindNum"),
        ("HUAWEI-EPON-MIB", "hwEponSrvProfileMulticastMode"),
        ("HUAWEI-EPON-MIB", "hwEponSrvProfileFecMode"),
        ("HUAWEI-EPON-MIB", "hwEponSrvProfileMulticastQuickLeaveSwitch"),
        ("HUAWEI-EPON-MIB", "hwEponSrvProfOnuPortCfgMaxMacAddressNum"),
        ("HUAWEI-EPON-MIB", "hwEponSrvProfOnuPortCfgMulticastStripSwitch"),
        ("HUAWEI-EPON-MIB", "hwEponDbaProfileFixedRate"),
        ("HUAWEI-EPON-MIB", "hwEponDbaProfileAssuredRate"),
        ("HUAWEI-EPON-MIB", "hwEponDbaProfileMaxRate"),
        ("HUAWEI-EPON-MIB", "hwEponDbaProfileReferenceNum"),
        ("HUAWEI-EPON-MIB", "hwEponDbaProfileEntryStatus"),
        ("HUAWEI-EPON-MIB", "hwEponOnuSnmpProfileVersion"),
        ("HUAWEI-EPON-MIB", "hwEponOnuSnmpProfileReadCommunityName"),
        ("HUAWEI-EPON-MIB", "hwEponOnuSnmpProfileWriteCommunityName"),
        ("HUAWEI-EPON-MIB", "hwEponOnuSnmpProfileTrapHostIp"),
        ("HUAWEI-EPON-MIB", "hwEponOnuSnmpProfileTrapHostSrcUdpPort"),
        ("HUAWEI-EPON-MIB", "hwEponOnuSnmpProfileSecurityName"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPortClassPriMark"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPortClassConditionNum"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPortClassFieldSelect1"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPortClassOperator1"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPortClassMatchValue1"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPortClassFieldSelect2"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPortClassOperator2"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPortClassMatchValue2"),
        ("HUAWEI-EPON-MIB", "hwEponSrvProfOnuPortCarCfgCir"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPortClassFieldSelect3"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPortClassOperator3"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPortClassMatchValue3"),
        ("HUAWEI-EPON-MIB", "hwEponSrvProfOnuPortCarCfgPir"),
        ("HUAWEI-EPON-MIB", "hwEponSrvProfOnuPortCarCfgCbs"),
        ("HUAWEI-EPON-MIB", "hwEponSrvProfOnuPortCarCfgEbs"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPortClassQueueIndexId"),
        ("HUAWEI-EPON-MIB", "hwEponLineProfileRowStatus"),
        ("HUAWEI-EPON-MIB", "hwEponOnuSrvProfileRowStatus"),
        ("HUAWEI-EPON-MIB", "hwEponOnuSnmpProfileRowStatus"),
        ("HUAWEI-EPON-MIB", "hwEponSrvProfOnuPortCarCfgRowStatus"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPortClassProfileRowStatus"),
        ("HUAWEI-EPON-MIB", "hwEponSrvProfMulticastVlanCfgRowStatus"),
        ("HUAWEI-EPON-MIB", "hwEponOnuSnmpProfName"),
        ("HUAWEI-EPON-MIB", "hwEponDbaTypeIndex"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPortClassFieldSelect4"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPortClassOperator4"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPortClassMatchValue4"),
        ("HUAWEI-EPON-MIB", "hwEponSrvProfOnuPortVlanMode"),
        ("HUAWEI-EPON-MIB", "hwEponSrvProfOnuPortVlanTranslationRowStatus"),
        ("HUAWEI-EPON-MIB", "hwEponSrvProfOnuPortDefaultVlanId"),
        ("HUAWEI-EPON-MIB", "hwEponSrvProfOnuPortVlanRowStatus"),
        ("HUAWEI-EPON-MIB", "hwEponSrvProfOnuPortVlanTranslationSVlanId"),
        ("HUAWEI-EPON-MIB", "hwEponSrvProfOnuPortAddToVlanId"))
)
if mibBuilder.loadTexts:
    hwEponProfileGroup.setStatus("current")

hwEponStatisticGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 8, 2, 4)
)
hwEponStatisticGroup.setObjects(
      *(("HUAWEI-EPON-MIB", "hwEponOltStatisticRecvDataFrames"),
        ("HUAWEI-EPON-MIB", "hwEponOltStatisticRecvDataBytes"),
        ("HUAWEI-EPON-MIB", "hwEponOltStatisticRecvMulticastFrames"),
        ("HUAWEI-EPON-MIB", "hwEponOltStatisticRecvBoardcastFrames"),
        ("HUAWEI-EPON-MIB", "hwEponOltStatisticRecvErrorFrames"),
        ("HUAWEI-EPON-MIB", "hwEponOltStatisticRecvErrorBytes"),
        ("HUAWEI-EPON-MIB", "hwEponOltStatisticRecv64ByteFrames"),
        ("HUAWEI-EPON-MIB", "hwEponOltStatisticRecv65To127ByteFrames"),
        ("HUAWEI-EPON-MIB", "hwEponOltStatisticRecv128To255ByteFrames"),
        ("HUAWEI-EPON-MIB", "hwEponOltStatisticRecv256To511ByteFrames"),
        ("HUAWEI-EPON-MIB", "hwEponOltStatisticRecv512To1023ByteFrames"),
        ("HUAWEI-EPON-MIB", "hwEponOltStatisticRecv1024To1518ByteFrames"),
        ("HUAWEI-EPON-MIB", "hwEponOltStatisticRecvOver1518ByteFrames"),
        ("HUAWEI-EPON-MIB", "hwEponOltStatisticRecvUndersizeFrames"),
        ("HUAWEI-EPON-MIB", "hwEponOltStatisticRecvOversizeFrames"),
        ("HUAWEI-EPON-MIB", "hwEponOltStatisticRecvFcsErrorFrames"),
        ("HUAWEI-EPON-MIB", "hwEponOltStatisticUniCastFrames"),
        ("HUAWEI-EPON-MIB", "hwEponOltStatisticRecvOkFrameCnt"),
        ("HUAWEI-EPON-MIB", "hwEponOltStatisticRecvOkByteCnt"),
        ("HUAWEI-EPON-MIB", "hwEponOltStatisticTransDataFrames"),
        ("HUAWEI-EPON-MIB", "hwEponOltStatisticTransDataBytes"),
        ("HUAWEI-EPON-MIB", "hwEponOltStatisticTransUnicastFrames"),
        ("HUAWEI-EPON-MIB", "hwEponOltStatisticTransMulticastFrames"),
        ("HUAWEI-EPON-MIB", "hwEponOltStatisticTransBoardcastFrames"),
        ("HUAWEI-EPON-MIB", "hwEponOltStatisticTrans64ByteFrames"),
        ("HUAWEI-EPON-MIB", "hwEponOltStatisticTrans65To127ByteFrames"),
        ("HUAWEI-EPON-MIB", "hwEponOltStatisticTrans128To255ByteFrames"),
        ("HUAWEI-EPON-MIB", "hwEponOltStatisticTrans256To511ByteFrames"),
        ("HUAWEI-EPON-MIB", "hwEponOltStatisticTrans512To1023ByteFrames"),
        ("HUAWEI-EPON-MIB", "hwEponOltStatisticTrans1024To1518ByteFrames"),
        ("HUAWEI-EPON-MIB", "hwEponOltStatisticTransOver1518ByteFrames"),
        ("HUAWEI-EPON-MIB", "hwEponOltStatisticTransFcsErrorFrames"),
        ("HUAWEI-EPON-MIB", "hwEponOltStatisticClear"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPonStatisticRcv1024To1518byteFrm"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPonStatisticRcv128To255byteFrm"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPonStatisticRcv256To511byteFrm"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPonStatisticRcv512To1023byteFrm"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPonStatisticRcv64byteFrm"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPonStatisticRcv65To127byteFrm"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPonStatisticRcvBcFrame"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPonStatisticRcvByte"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPonStatisticRcvCrc8Err"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPonStatisticRcvDelayByte"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPonStatisticRcvDelayMax"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPonStatisticRcvDelayThreshold"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPonStatisticRcvDropByte"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPonStatisticRcvDropFrm"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPonStatisticRcvErrFrm"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPonStatisticRcvErrOntDestinedByte"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPonStatisticRcvFcsErr"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPonStatisticRcvFrame"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPonStatisticRcvGreatThan1518byteFrm"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPonStatisticRcvInvalidSldFrm"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPonStatisticRcvLaserPower"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPonStatisticRcvLineCodeErr"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPonStatisticRcvMcFrame"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPonStatisticRcvOntDestinedByte"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPonStatisticRcvUcFrame"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPonStatisticRcvUndersizeFrm"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPonStatisticSend1024To1518byteFrm"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPonStatisticSend128To255byteFrm"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPonStatisticSend256To511byteFrm"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPonStatisticSend512To1023byteFrm"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPonStatisticSend64byteFrm"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPonStatisticSend65To127byteFrm"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPonStatisticSendBcFrame"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPonStatisticSendByte"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPonStatisticSendDelayByte"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPonStatisticSendDelayMax"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPonStatisticSendDelayThreshold"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPonStatisticSendDropByte"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPonStatisticSendDropFrm"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPonStatisticSendFrame"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPonStatisticSendGreatThan1518byteFrm"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPonStatisticSendMcFrame"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPonStatisticSendUcFrame"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPonStatisticSendUnusedByte"),
        ("HUAWEI-EPON-MIB", "hwEponOnuPonStatisticClear"),
        ("HUAWEI-EPON-MIB", "hwEponOnuUniStatisticRecvFrames"),
        ("HUAWEI-EPON-MIB", "hwEponOnuUniStatisticRecvMulticastFrames"),
        ("HUAWEI-EPON-MIB", "hwEponOnuUniStatisticRecvBroadcastFrames"),
        ("HUAWEI-EPON-MIB", "hwEponOnuUniStatisticRecv64OctetFrames"),
        ("HUAWEI-EPON-MIB", "hwEponOnuUniStatisticRecv65To127OctetFrames"),
        ("HUAWEI-EPON-MIB", "hwEponOnuUniStatisticRecv128To255OctetFrames"),
        ("HUAWEI-EPON-MIB", "hwEponOnuUniStatisticRecv256To511OctetFrames"),
        ("HUAWEI-EPON-MIB", "hwEponOnuUniStatisticRecv512To1023OctetFrames"),
        ("HUAWEI-EPON-MIB", "hwEponOnuUniStatisticRecv1024To1518OctetFrames"),
        ("HUAWEI-EPON-MIB", "hwEponOnuUniStatisticRecvUndersizeFrames"),
        ("HUAWEI-EPON-MIB", "hwEponOnuUniStatisticRecvTooLongFrames"),
        ("HUAWEI-EPON-MIB", "hwEponOnuUniStatisticTransDropFrames"),
        ("HUAWEI-EPON-MIB", "hwEponOnuUniStatisticTransFrames"),
        ("HUAWEI-EPON-MIB", "hwEponOnuUniStatisticTransMtuExceededDiscardFrames"),
        ("HUAWEI-EPON-MIB", "hwEponOnuUniStatisticClear"))
)
if mibBuilder.loadTexts:
    hwEponStatisticGroup.setStatus("current")

hwEponDisplayAlarmObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 8, 2, 5)
)
hwEponDisplayAlarmObjectsGroup.setObjects(
      *(("HUAWEI-EPON-MIB", "hwEponOnuAlarmStateKeyExchangeFail"),
        ("HUAWEI-EPON-MIB", "hwEponOnuAlarmStateDyingGasp"),
        ("HUAWEI-EPON-MIB", "hwEponOnuAlarmStateLinkFault"),
        ("HUAWEI-EPON-MIB", "hwEponOnuFirmWareLoadStateSucc"),
        ("HUAWEI-EPON-MIB", "hwEponOnuFirmWareLoadStateFault"),
        ("HUAWEI-EPON-MIB", "hwEponOltAlarmStateDegrade"),
        ("HUAWEI-EPON-MIB", "hwEponOnuUniAlarmStateTransmitFail"),
        ("HUAWEI-EPON-MIB", "hwEponOnuUniAlarmStateLos"))
)
if mibBuilder.loadTexts:
    hwEponDisplayAlarmObjectsGroup.setStatus("current")

hwEponTrapObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 8, 2, 6)
)
hwEponTrapObjectsGroup.setObjects(
      *(("HUAWEI-EPON-MIB", "hwEponSlotIndex"),
        ("HUAWEI-EPON-MIB", "hwEponCardIndex"),
        ("HUAWEI-EPON-MIB", "hwEponPortIndex"),
        ("HUAWEI-EPON-MIB", "hwEponTrapOnuId"),
        ("HUAWEI-EPON-MIB", "hwEponTrapMac"),
        ("HUAWEI-EPON-MIB", "hwEponTrapPwd"))
)
if mibBuilder.loadTexts:
    hwEponTrapObjectsGroup.setStatus("current")


# Notification objects

hwEponOltAlarmLosTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 7, 1)
)
hwEponOltAlarmLosTrap.setObjects(
      *(("HUAWEI-EPON-MIB", "hwEponSlotIndex"),
        ("HUAWEI-EPON-MIB", "hwEponCardIndex"),
        ("HUAWEI-EPON-MIB", "hwEponPortIndex"))
)
if mibBuilder.loadTexts:
    hwEponOltAlarmLosTrap.setStatus(
        "current"
    )

hwEponOltAlarmLosResumeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 7, 2)
)
hwEponOltAlarmLosResumeTrap.setObjects(
      *(("HUAWEI-EPON-MIB", "hwEponSlotIndex"),
        ("HUAWEI-EPON-MIB", "hwEponCardIndex"),
        ("HUAWEI-EPON-MIB", "hwEponPortIndex"))
)
if mibBuilder.loadTexts:
    hwEponOltAlarmLosResumeTrap.setStatus(
        "current"
    )

hwEponOltAutoFindTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 7, 3)
)
hwEponOltAutoFindTrap.setObjects(
      *(("HUAWEI-EPON-MIB", "hwEponSlotIndex"),
        ("HUAWEI-EPON-MIB", "hwEponCardIndex"),
        ("HUAWEI-EPON-MIB", "hwEponPortIndex"),
        ("HUAWEI-EPON-MIB", "hwEponTrapMac"),
        ("HUAWEI-EPON-MIB", "hwEponTrapPwd"))
)
if mibBuilder.loadTexts:
    hwEponOltAutoFindTrap.setStatus(
        "current"
    )

hwEponOltAlarmTransmitFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 7, 4)
)
hwEponOltAlarmTransmitFaultTrap.setObjects(
      *(("HUAWEI-EPON-MIB", "hwEponSlotIndex"),
        ("HUAWEI-EPON-MIB", "hwEponCardIndex"),
        ("HUAWEI-EPON-MIB", "hwEponPortIndex"))
)
if mibBuilder.loadTexts:
    hwEponOltAlarmTransmitFaultTrap.setStatus(
        "current"
    )

hwEponOnuAlarmPwdConlictTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 7, 5)
)
hwEponOnuAlarmPwdConlictTrap.setObjects(
      *(("HUAWEI-EPON-MIB", "hwEponSlotIndex"),
        ("HUAWEI-EPON-MIB", "hwEponCardIndex"),
        ("HUAWEI-EPON-MIB", "hwEponPortIndex"),
        ("HUAWEI-EPON-MIB", "hwEponTrapOnuId"))
)
if mibBuilder.loadTexts:
    hwEponOnuAlarmPwdConlictTrap.setStatus(
        "current"
    )

hwEponOnuOnlineTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 7, 6)
)
hwEponOnuOnlineTrap.setObjects(
      *(("HUAWEI-EPON-MIB", "hwEponSlotIndex"),
        ("HUAWEI-EPON-MIB", "hwEponCardIndex"),
        ("HUAWEI-EPON-MIB", "hwEponPortIndex"),
        ("HUAWEI-EPON-MIB", "hwEponTrapOnuId"),
        ("HUAWEI-EPON-MIB", "hwEponTrapMac"),
        ("HUAWEI-EPON-MIB", "hwEponTrapPwd"))
)
if mibBuilder.loadTexts:
    hwEponOnuOnlineTrap.setStatus(
        "current"
    )

hwEponOnuOfflineTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 7, 7)
)
hwEponOnuOfflineTrap.setObjects(
      *(("HUAWEI-EPON-MIB", "hwEponSlotIndex"),
        ("HUAWEI-EPON-MIB", "hwEponCardIndex"),
        ("HUAWEI-EPON-MIB", "hwEponPortIndex"),
        ("HUAWEI-EPON-MIB", "hwEponTrapOnuId"),
        ("HUAWEI-EPON-MIB", "hwEponTrapMac"),
        ("HUAWEI-EPON-MIB", "hwEponTrapPwd"))
)
if mibBuilder.loadTexts:
    hwEponOnuOfflineTrap.setStatus(
        "current"
    )


# Notifications groups

hwEponTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 8, 2, 7)
)
hwEponTrapGroup.setObjects(
      *(("HUAWEI-EPON-MIB", "hwEponOltAlarmLosTrap"),
        ("HUAWEI-EPON-MIB", "hwEponOltAlarmLosResumeTrap"),
        ("HUAWEI-EPON-MIB", "hwEponOltAutoFindTrap"),
        ("HUAWEI-EPON-MIB", "hwEponOltAlarmTransmitFaultTrap"),
        ("HUAWEI-EPON-MIB", "hwEponOnuAlarmPwdConlictTrap"),
        ("HUAWEI-EPON-MIB", "hwEponOnuOnlineTrap"),
        ("HUAWEI-EPON-MIB", "hwEponOnuOfflineTrap"))
)
if mibBuilder.loadTexts:
    hwEponTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwEponCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 179, 1, 8, 1, 1)
)
if mibBuilder.loadTexts:
    hwEponCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-EPON-MIB",
    **{"DisplayString": DisplayString,
       "PortList": PortList,
       "hwEponMIB": hwEponMIB,
       "hwEponObjects": hwEponObjects,
       "hwEponGlobalObjects": hwEponGlobalObjects,
       "hwEponAutoFindOnuAge": hwEponAutoFindOnuAge,
       "hwEponCtcOuiId": hwEponCtcOuiId,
       "hwEponChangePasswordAge": hwEponChangePasswordAge,
       "hwEponControlObjects": hwEponControlObjects,
       "hwEponOltControlTable": hwEponOltControlTable,
       "hwEponOltControlEntry": hwEponOltControlEntry,
       "hwEponOltControlfarthest": hwEponOltControlfarthest,
       "hwEponOltControlAutofindOnuEnable": hwEponOltControlAutofindOnuEnable,
       "hwEponOltControlStatus": hwEponOltControlStatus,
       "hwEponOltControlUpStreamBandWidth": hwEponOltControlUpStreamBandWidth,
       "hwEponOltControlDownStreamBandWidth": hwEponOltControlDownStreamBandWidth,
       "hwEponOnuConfigTable": hwEponOnuConfigTable,
       "hwEponOnuConfigEntry": hwEponOnuConfigEntry,
       "hwEponOnuIndex": hwEponOnuIndex,
       "hwEponOnuId": hwEponOnuId,
       "hwEponOnuAuthMode": hwEponOnuAuthMode,
       "hwEponOnuMacAddress": hwEponOnuMacAddress,
       "hwEponOnuPassword": hwEponOnuPassword,
       "hwEponOnuTimeout": hwEponOnuTimeout,
       "hwEponOnuManagementMode": hwEponOnuManagementMode,
       "hwEponOnuLineProfName": hwEponOnuLineProfName,
       "hwEponOnuServiceProfName": hwEponOnuServiceProfName,
       "hwEponOnuSnmpProfName": hwEponOnuSnmpProfName,
       "hwEponOnuDescription": hwEponOnuDescription,
       "hwEponOnuActiveStatus": hwEponOnuActiveStatus,
       "hwEponOnuRowStatus": hwEponOnuRowStatus,
       "hwEponOnuVersionTable": hwEponOnuVersionTable,
       "hwEponOnuVersionEntry": hwEponOnuVersionEntry,
       "hwEponOnuVendorId": hwEponOnuVendorId,
       "hwEponOnuModel": hwEponOnuModel,
       "hwEponOnuOnuIdentifier": hwEponOnuOnuIdentifier,
       "hwEponOnuHardwareVersion": hwEponOnuHardwareVersion,
       "hwEponOnuSoftwareVersion": hwEponOnuSoftwareVersion,
       "hwEponOnuChipVenderId": hwEponOnuChipVenderId,
       "hwEponOnuChipModel": hwEponOnuChipModel,
       "hwEponOnuChipVersion": hwEponOnuChipVersion,
       "hwEponOnuChipDesignDate": hwEponOnuChipDesignDate,
       "hwEponOnuFirmwareVersion": hwEponOnuFirmwareVersion,
       "hwEponOnuControlTable": hwEponOnuControlTable,
       "hwEponOnuControlEntry": hwEponOnuControlEntry,
       "hwEponOnuReset": hwEponOnuReset,
       "hwEponOnuReRegister": hwEponOnuReRegister,
       "hwEponOnuReDiscovery": hwEponOnuReDiscovery,
       "hwEponOnuRunStatus": hwEponOnuRunStatus,
       "hwEponOnuDistance": hwEponOnuDistance,
       "hwEponOnuRtt": hwEponOnuRtt,
       "hwEponOnuLastUpTime": hwEponOnuLastUpTime,
       "hwEponOnuLastDownTime": hwEponOnuLastDownTime,
       "hwEponOnuLastDownCause": hwEponOnuLastDownCause,
       "hwEponAutoFindOnuInfoTable": hwEponAutoFindOnuInfoTable,
       "hwEponAutoFindOnuInfoEntry": hwEponAutoFindOnuInfoEntry,
       "hwEponAutoFindOnuOrder": hwEponAutoFindOnuOrder,
       "hwEponAutoFindOnuInfoMacAddress": hwEponAutoFindOnuInfoMacAddress,
       "hwEponAutoFindOnuInfoPasswordValue": hwEponAutoFindOnuInfoPasswordValue,
       "hwEponOnuCapabilityInfoTable": hwEponOnuCapabilityInfoTable,
       "hwEponOnuCapabilityInfoEntry": hwEponOnuCapabilityInfoEntry,
       "hwEponOnuPotsPortNum": hwEponOnuPotsPortNum,
       "hwEponOnuFePortsNum": hwEponOnuFePortsNum,
       "hwEponOnuGePortsNum": hwEponOnuGePortsNum,
       "hwEponOnuTdmPortsNum": hwEponOnuTdmPortsNum,
       "hwEponOnuFecSupport": hwEponOnuFecSupport,
       "hwEponOnuSupportBackupBattery": hwEponOnuSupportBackupBattery,
       "hwEponOnuUpQueueNum": hwEponOnuUpQueueNum,
       "hwEponOnuUpQueueNumPerPort": hwEponOnuUpQueueNumPerPort,
       "hwEponOnuDownQueueNum": hwEponOnuDownQueueNum,
       "hwEponOnuDownQueueNumPerPort": hwEponOnuDownQueueNumPerPort,
       "hwEponOnuFePortList": hwEponOnuFePortList,
       "hwEponOnuGePortList": hwEponOnuGePortList,
       "hwEponOnuSupportMulticastQuickLeave": hwEponOnuSupportMulticastQuickLeave,
       "hwEponOnuIpConfigTable": hwEponOnuIpConfigTable,
       "hwEponOnuIpConfigEntry": hwEponOnuIpConfigEntry,
       "hwEponOnuIpAddress": hwEponOnuIpAddress,
       "hwEponOnuNetMask": hwEponOnuNetMask,
       "hwEponOnuNetGateway": hwEponOnuNetGateway,
       "hwEponOnuIpManageVlan": hwEponOnuIpManageVlan,
       "hwEponOnuIpRowStates": hwEponOnuIpRowStates,
       "hwEponOnuEthObjectCfgTable": hwEponOnuEthObjectCfgTable,
       "hwEponOnuEthObjectCfgEntry": hwEponOnuEthObjectCfgEntry,
       "hwEponOnuEthPortId": hwEponOnuEthPortId,
       "hwEponOnuEthOperateStatus": hwEponOnuEthOperateStatus,
       "hwEponOnuEthFlowcontrolSwitch": hwEponOnuEthFlowcontrolSwitch,
       "hwEponOnuTdmPortCfgTable": hwEponOnuTdmPortCfgTable,
       "hwEponOnuTdmPortCfgEntry": hwEponOnuTdmPortCfgEntry,
       "hwEponOnuTdmPortId": hwEponOnuTdmPortId,
       "hwEponOnuTdmPortOperateStatus": hwEponOnuTdmPortOperateStatus,
       "hwEponOnuPotsPortCfgTable": hwEponOnuPotsPortCfgTable,
       "hwEponOnuPotsPortCfgEntry": hwEponOnuPotsPortCfgEntry,
       "hwEponOnuPotsPortId": hwEponOnuPotsPortId,
       "hwEponOnuPotsPortOperateStatus": hwEponOnuPotsPortOperateStatus,
       "hwEponOnuCfgCarTable": hwEponOnuCfgCarTable,
       "hwEponOnuCfgCarEntry": hwEponOnuCfgCarEntry,
       "hwEponOnuCfgCarDirection": hwEponOnuCfgCarDirection,
       "hwEponOnuCarProfileNameIndex": hwEponOnuCarProfileNameIndex,
       "hwEponOnuTrafficPolicyNameIndex": hwEponOnuTrafficPolicyNameIndex,
       "hwEponOnuCfgCarRowStatus": hwEponOnuCfgCarRowStatus,
       "hwEponOltPortDefaultVlanTable": hwEponOltPortDefaultVlanTable,
       "hwEponOltPortDefaultVlanEntry": hwEponOltPortDefaultVlanEntry,
       "hwEponOltPortDefaultVlanId": hwEponOltPortDefaultVlanId,
       "hwEponOltPortDefaultVlanBatch": hwEponOltPortDefaultVlanBatch,
       "hwEponOltPortDefaultVlanOnuStartId": hwEponOltPortDefaultVlanOnuStartId,
       "hwEponOltPortDefaultVlanOnuEndId": hwEponOltPortDefaultVlanOnuEndId,
       "hwEponOltPortDefaultVlanRowStatus": hwEponOltPortDefaultVlanRowStatus,
       "hwEponVlanStackingAndMappingTable": hwEponVlanStackingAndMappingTable,
       "hwEponVlanStackingAndMappingEntry": hwEponVlanStackingAndMappingEntry,
       "hwEponOnuExtSVlanId": hwEponOnuExtSVlanId,
       "hwEponOnuIntSStartVlanId": hwEponOnuIntSStartVlanId,
       "hwEponOnuIntSEndVlanId": hwEponOnuIntSEndVlanId,
       "hwEponVlanStackingOrMapping": hwEponVlanStackingOrMapping,
       "hwEponOnuDextVlanId": hwEponOnuDextVlanId,
       "hwEponOnuDintVlanId": hwEponOnuDintVlanId,
       "hwEponOnuPopExtVlanId": hwEponOnuPopExtVlanId,
       "hwEponOnuVlanCopyPri": hwEponOnuVlanCopyPri,
       "hwEponOnuIntVlanRemarkPri": hwEponOnuIntVlanRemarkPri,
       "hwEponOnuExtVlanRemarkPri": hwEponOnuExtVlanRemarkPri,
       "hwEponOnuIntVlanPri": hwEponOnuIntVlanPri,
       "hwEponOnuExtVlanPri": hwEponOnuExtVlanPri,
       "hwEponVlanMappingBatch": hwEponVlanMappingBatch,
       "hwEponVlanMappingOnuStartId": hwEponVlanMappingOnuStartId,
       "hwEponVlanMappingOnuEndId": hwEponVlanMappingOnuEndId,
       "hwEponVlanMappingRowStatus": hwEponVlanMappingRowStatus,
       "hwEponOltPortStaticMacTable": hwEponOltPortStaticMacTable,
       "hwEponOltPortStaticMacEntry": hwEponOltPortStaticMacEntry,
       "hwEponOnuUserMacAddressOrder": hwEponOnuUserMacAddressOrder,
       "hwEponOnuUserMacAddress": hwEponOnuUserMacAddress,
       "hwEponOltPortStaticMacRowStatus": hwEponOltPortStaticMacRowStatus,
       "hwEponOltPortMacLimitTable": hwEponOltPortMacLimitTable,
       "hwEponOltPortMacLimitEntry": hwEponOltPortMacLimitEntry,
       "hwEponOnuUserMacAddressNumber": hwEponOnuUserMacAddressNumber,
       "hwEponOnuForwardAction": hwEponOnuForwardAction,
       "hwEponOnuAlarmAction": hwEponOnuAlarmAction,
       "hwEponOnuMacLimitRowStatus": hwEponOnuMacLimitRowStatus,
       "hwEponProfileObjects": hwEponProfileObjects,
       "hwEponLineProfileInfoTable": hwEponLineProfileInfoTable,
       "hwEponLineProfileInfoEntry": hwEponLineProfileInfoEntry,
       "hwEponLineProfileNameIndex": hwEponLineProfileNameIndex,
       "hwEponLineProfileBindNum": hwEponLineProfileBindNum,
       "hwEponLineProfileDbaProfileName": hwEponLineProfileDbaProfileName,
       "hwEponLineProfileEncryptMode": hwEponLineProfileEncryptMode,
       "hwEponLineProfileQueueSetIndex1Threshold": hwEponLineProfileQueueSetIndex1Threshold,
       "hwEponLineProfileQueueSetIndex2Threshold": hwEponLineProfileQueueSetIndex2Threshold,
       "hwEponLineProfileQueueSetIndex3Threshold": hwEponLineProfileQueueSetIndex3Threshold,
       "hwEponLineProfileRowStatus": hwEponLineProfileRowStatus,
       "hwEponOnuSrvProfileInfoTable": hwEponOnuSrvProfileInfoTable,
       "hwEponOnuSrvProfileInfoEntry": hwEponOnuSrvProfileInfoEntry,
       "hwEponOnuSrvProfNameIndex": hwEponOnuSrvProfNameIndex,
       "hwEponOnuSrvProfileBindNum": hwEponOnuSrvProfileBindNum,
       "hwEponOnuSrvProfileRowStatus": hwEponOnuSrvProfileRowStatus,
       "hwEponSrvProfileOnuCfgTable": hwEponSrvProfileOnuCfgTable,
       "hwEponSrvProfileOnuCfgEntry": hwEponSrvProfileOnuCfgEntry,
       "hwEponSrvProfileFecMode": hwEponSrvProfileFecMode,
       "hwEponSrvProfileMulticastMode": hwEponSrvProfileMulticastMode,
       "hwEponSrvProfileMulticastQuickLeaveSwitch": hwEponSrvProfileMulticastQuickLeaveSwitch,
       "hwEponSrvProfOnuPortCfgTable": hwEponSrvProfOnuPortCfgTable,
       "hwEponSrvProfOnuPortCfgEntry": hwEponSrvProfOnuPortCfgEntry,
       "hwEponOnuPortTypeIndex": hwEponOnuPortTypeIndex,
       "hwEponOnuPortIdIndex": hwEponOnuPortIdIndex,
       "hwEponSrvProfOnuPortCfgMaxMacAddressNum": hwEponSrvProfOnuPortCfgMaxMacAddressNum,
       "hwEponSrvProfOnuPortCfgMulticastStripSwitch": hwEponSrvProfOnuPortCfgMulticastStripSwitch,
       "hwEponSrvProfMulticastVlanCfgTable": hwEponSrvProfMulticastVlanCfgTable,
       "hwEponSrvProfMulticastVlanCfgEntry": hwEponSrvProfMulticastVlanCfgEntry,
       "hwEponSrvProfMulticastVlanCfgMulticastVlan": hwEponSrvProfMulticastVlanCfgMulticastVlan,
       "hwEponSrvProfMulticastVlanCfgRowStatus": hwEponSrvProfMulticastVlanCfgRowStatus,
       "hwEponSrvProfOnuPortVlanCfgTable": hwEponSrvProfOnuPortVlanCfgTable,
       "hwEponSrvProfOnuPortVlanCfgEntry": hwEponSrvProfOnuPortVlanCfgEntry,
       "hwEponOnuPortType": hwEponOnuPortType,
       "hwEponOnuPortId": hwEponOnuPortId,
       "hwEponSrvProfOnuPortVlanMode": hwEponSrvProfOnuPortVlanMode,
       "hwEponSrvProfOnuPortAddToVlanId": hwEponSrvProfOnuPortAddToVlanId,
       "hwEponSrvProfOnuPortDefaultVlanId": hwEponSrvProfOnuPortDefaultVlanId,
       "hwEponSrvProfOnuPortVlanRowStatus": hwEponSrvProfOnuPortVlanRowStatus,
       "hwEponSrvProfOnuPortVlanTranslationTable": hwEponSrvProfOnuPortVlanTranslationTable,
       "hwEponSrvProfOnuPortVlanTranslationEntry": hwEponSrvProfOnuPortVlanTranslationEntry,
       "hwEponSrvProfOnuPortVlanTranslationCvlanId": hwEponSrvProfOnuPortVlanTranslationCvlanId,
       "hwEponSrvProfOnuPortVlanTranslationSVlanId": hwEponSrvProfOnuPortVlanTranslationSVlanId,
       "hwEponSrvProfOnuPortVlanTranslationRowStatus": hwEponSrvProfOnuPortVlanTranslationRowStatus,
       "hwEponDbaProfileInfoTable": hwEponDbaProfileInfoTable,
       "hwEponDbaProfileInfoEntry": hwEponDbaProfileInfoEntry,
       "hwEponDbaProfileInfoNameIndex": hwEponDbaProfileInfoNameIndex,
       "hwEponDbaTypeIndex": hwEponDbaTypeIndex,
       "hwEponDbaProfileFixedRate": hwEponDbaProfileFixedRate,
       "hwEponDbaProfileAssuredRate": hwEponDbaProfileAssuredRate,
       "hwEponDbaProfileMaxRate": hwEponDbaProfileMaxRate,
       "hwEponDbaProfileReferenceNum": hwEponDbaProfileReferenceNum,
       "hwEponDbaProfileEntryStatus": hwEponDbaProfileEntryStatus,
       "hwEponOnuSnmpProfileInfoTable": hwEponOnuSnmpProfileInfoTable,
       "hwEponOnuSnmpProfileInfoEntry": hwEponOnuSnmpProfileInfoEntry,
       "hwEponOnuSnmpProfileInfoNameIndex": hwEponOnuSnmpProfileInfoNameIndex,
       "hwEponOnuSnmpProfileVersion": hwEponOnuSnmpProfileVersion,
       "hwEponOnuSnmpProfileReadCommunityName": hwEponOnuSnmpProfileReadCommunityName,
       "hwEponOnuSnmpProfileWriteCommunityName": hwEponOnuSnmpProfileWriteCommunityName,
       "hwEponOnuSnmpProfileTrapHostIp": hwEponOnuSnmpProfileTrapHostIp,
       "hwEponOnuSnmpProfileTrapHostSrcUdpPort": hwEponOnuSnmpProfileTrapHostSrcUdpPort,
       "hwEponOnuSnmpProfileSecurityName": hwEponOnuSnmpProfileSecurityName,
       "hwEponOnuSnmpProfileRowStatus": hwEponOnuSnmpProfileRowStatus,
       "hwEponSrvProfOnuPortClassTable": hwEponSrvProfOnuPortClassTable,
       "hwEponSrvProfOnuPortClassEntry": hwEponSrvProfOnuPortClassEntry,
       "hwEponOnuClassifEthPortIndex": hwEponOnuClassifEthPortIndex,
       "hwEponOnuPortClassRuleIndexId": hwEponOnuPortClassRuleIndexId,
       "hwEponOnuPortClassConditionNum": hwEponOnuPortClassConditionNum,
       "hwEponOnuPortClassQueueIndexId": hwEponOnuPortClassQueueIndexId,
       "hwEponOnuPortClassPriMark": hwEponOnuPortClassPriMark,
       "hwEponOnuPortClassFieldSelect1": hwEponOnuPortClassFieldSelect1,
       "hwEponOnuPortClassOperator1": hwEponOnuPortClassOperator1,
       "hwEponOnuPortClassMatchValue1": hwEponOnuPortClassMatchValue1,
       "hwEponOnuPortClassFieldSelect2": hwEponOnuPortClassFieldSelect2,
       "hwEponOnuPortClassOperator2": hwEponOnuPortClassOperator2,
       "hwEponOnuPortClassMatchValue2": hwEponOnuPortClassMatchValue2,
       "hwEponOnuPortClassFieldSelect3": hwEponOnuPortClassFieldSelect3,
       "hwEponOnuPortClassOperator3": hwEponOnuPortClassOperator3,
       "hwEponOnuPortClassMatchValue3": hwEponOnuPortClassMatchValue3,
       "hwEponOnuPortClassFieldSelect4": hwEponOnuPortClassFieldSelect4,
       "hwEponOnuPortClassOperator4": hwEponOnuPortClassOperator4,
       "hwEponOnuPortClassMatchValue4": hwEponOnuPortClassMatchValue4,
       "hwEponOnuPortClassProfileRowStatus": hwEponOnuPortClassProfileRowStatus,
       "hwEponSrvProfOnuPortCfgCarTable": hwEponSrvProfOnuPortCfgCarTable,
       "hwEponSrvProfOnuPortCfgCarEntry": hwEponSrvProfOnuPortCfgCarEntry,
       "hwEponSrvProfOnuPortCarCfgDirection": hwEponSrvProfOnuPortCarCfgDirection,
       "hwEponSrvProfOnuPortCarCfgCir": hwEponSrvProfOnuPortCarCfgCir,
       "hwEponSrvProfOnuPortCarCfgPir": hwEponSrvProfOnuPortCarCfgPir,
       "hwEponSrvProfOnuPortCarCfgCbs": hwEponSrvProfOnuPortCarCfgCbs,
       "hwEponSrvProfOnuPortCarCfgEbs": hwEponSrvProfOnuPortCarCfgEbs,
       "hwEponSrvProfOnuPortCarCfgRowStatus": hwEponSrvProfOnuPortCarCfgRowStatus,
       "hwEponStatisticObjects": hwEponStatisticObjects,
       "hwEponOltStatisticTable": hwEponOltStatisticTable,
       "hwEponOltStatisticEntry": hwEponOltStatisticEntry,
       "hwEponOltStatisticRecvDataFrames": hwEponOltStatisticRecvDataFrames,
       "hwEponOltStatisticRecvDataBytes": hwEponOltStatisticRecvDataBytes,
       "hwEponOltStatisticRecvMulticastFrames": hwEponOltStatisticRecvMulticastFrames,
       "hwEponOltStatisticRecvBoardcastFrames": hwEponOltStatisticRecvBoardcastFrames,
       "hwEponOltStatisticRecvErrorFrames": hwEponOltStatisticRecvErrorFrames,
       "hwEponOltStatisticRecvErrorBytes": hwEponOltStatisticRecvErrorBytes,
       "hwEponOltStatisticRecv64ByteFrames": hwEponOltStatisticRecv64ByteFrames,
       "hwEponOltStatisticRecv65To127ByteFrames": hwEponOltStatisticRecv65To127ByteFrames,
       "hwEponOltStatisticRecv128To255ByteFrames": hwEponOltStatisticRecv128To255ByteFrames,
       "hwEponOltStatisticRecv256To511ByteFrames": hwEponOltStatisticRecv256To511ByteFrames,
       "hwEponOltStatisticRecv512To1023ByteFrames": hwEponOltStatisticRecv512To1023ByteFrames,
       "hwEponOltStatisticRecv1024To1518ByteFrames": hwEponOltStatisticRecv1024To1518ByteFrames,
       "hwEponOltStatisticRecvOver1518ByteFrames": hwEponOltStatisticRecvOver1518ByteFrames,
       "hwEponOltStatisticRecvUndersizeFrames": hwEponOltStatisticRecvUndersizeFrames,
       "hwEponOltStatisticRecvOversizeFrames": hwEponOltStatisticRecvOversizeFrames,
       "hwEponOltStatisticRecvFcsErrorFrames": hwEponOltStatisticRecvFcsErrorFrames,
       "hwEponOltStatisticUniCastFrames": hwEponOltStatisticUniCastFrames,
       "hwEponOltStatisticRecvOkFrameCnt": hwEponOltStatisticRecvOkFrameCnt,
       "hwEponOltStatisticRecvOkByteCnt": hwEponOltStatisticRecvOkByteCnt,
       "hwEponOltStatisticTransDataFrames": hwEponOltStatisticTransDataFrames,
       "hwEponOltStatisticTransDataBytes": hwEponOltStatisticTransDataBytes,
       "hwEponOltStatisticTransUnicastFrames": hwEponOltStatisticTransUnicastFrames,
       "hwEponOltStatisticTransMulticastFrames": hwEponOltStatisticTransMulticastFrames,
       "hwEponOltStatisticTransBoardcastFrames": hwEponOltStatisticTransBoardcastFrames,
       "hwEponOltStatisticTrans64ByteFrames": hwEponOltStatisticTrans64ByteFrames,
       "hwEponOltStatisticTrans65To127ByteFrames": hwEponOltStatisticTrans65To127ByteFrames,
       "hwEponOltStatisticTrans128To255ByteFrames": hwEponOltStatisticTrans128To255ByteFrames,
       "hwEponOltStatisticTrans256To511ByteFrames": hwEponOltStatisticTrans256To511ByteFrames,
       "hwEponOltStatisticTrans512To1023ByteFrames": hwEponOltStatisticTrans512To1023ByteFrames,
       "hwEponOltStatisticTrans1024To1518ByteFrames": hwEponOltStatisticTrans1024To1518ByteFrames,
       "hwEponOltStatisticTransOver1518ByteFrames": hwEponOltStatisticTransOver1518ByteFrames,
       "hwEponOltStatisticTransFcsErrorFrames": hwEponOltStatisticTransFcsErrorFrames,
       "hwEponOltStatisticClear": hwEponOltStatisticClear,
       "hwEponOnuPonStatisticTable": hwEponOnuPonStatisticTable,
       "hwEponOnuPonStatisticEntry": hwEponOnuPonStatisticEntry,
       "hwEponOnuPonStatisticRcv1024To1518byteFrm": hwEponOnuPonStatisticRcv1024To1518byteFrm,
       "hwEponOnuPonStatisticRcv128To255byteFrm": hwEponOnuPonStatisticRcv128To255byteFrm,
       "hwEponOnuPonStatisticRcv256To511byteFrm": hwEponOnuPonStatisticRcv256To511byteFrm,
       "hwEponOnuPonStatisticRcv512To1023byteFrm": hwEponOnuPonStatisticRcv512To1023byteFrm,
       "hwEponOnuPonStatisticRcv64byteFrm": hwEponOnuPonStatisticRcv64byteFrm,
       "hwEponOnuPonStatisticRcv65To127byteFrm": hwEponOnuPonStatisticRcv65To127byteFrm,
       "hwEponOnuPonStatisticRcvBcFrame": hwEponOnuPonStatisticRcvBcFrame,
       "hwEponOnuPonStatisticRcvByte": hwEponOnuPonStatisticRcvByte,
       "hwEponOnuPonStatisticRcvCrc8Err": hwEponOnuPonStatisticRcvCrc8Err,
       "hwEponOnuPonStatisticRcvDelayByte": hwEponOnuPonStatisticRcvDelayByte,
       "hwEponOnuPonStatisticRcvDelayMax": hwEponOnuPonStatisticRcvDelayMax,
       "hwEponOnuPonStatisticRcvDelayThreshold": hwEponOnuPonStatisticRcvDelayThreshold,
       "hwEponOnuPonStatisticRcvDropByte": hwEponOnuPonStatisticRcvDropByte,
       "hwEponOnuPonStatisticRcvDropFrm": hwEponOnuPonStatisticRcvDropFrm,
       "hwEponOnuPonStatisticRcvErrFrm": hwEponOnuPonStatisticRcvErrFrm,
       "hwEponOnuPonStatisticRcvErrOntDestinedByte": hwEponOnuPonStatisticRcvErrOntDestinedByte,
       "hwEponOnuPonStatisticRcvFcsErr": hwEponOnuPonStatisticRcvFcsErr,
       "hwEponOnuPonStatisticRcvFrame": hwEponOnuPonStatisticRcvFrame,
       "hwEponOnuPonStatisticRcvGreatThan1518byteFrm": hwEponOnuPonStatisticRcvGreatThan1518byteFrm,
       "hwEponOnuPonStatisticRcvInvalidSldFrm": hwEponOnuPonStatisticRcvInvalidSldFrm,
       "hwEponOnuPonStatisticRcvLaserPower": hwEponOnuPonStatisticRcvLaserPower,
       "hwEponOnuPonStatisticRcvLineCodeErr": hwEponOnuPonStatisticRcvLineCodeErr,
       "hwEponOnuPonStatisticRcvMcFrame": hwEponOnuPonStatisticRcvMcFrame,
       "hwEponOnuPonStatisticRcvOntDestinedByte": hwEponOnuPonStatisticRcvOntDestinedByte,
       "hwEponOnuPonStatisticRcvUcFrame": hwEponOnuPonStatisticRcvUcFrame,
       "hwEponOnuPonStatisticRcvUndersizeFrm": hwEponOnuPonStatisticRcvUndersizeFrm,
       "hwEponOnuPonStatisticSend1024To1518byteFrm": hwEponOnuPonStatisticSend1024To1518byteFrm,
       "hwEponOnuPonStatisticSend128To255byteFrm": hwEponOnuPonStatisticSend128To255byteFrm,
       "hwEponOnuPonStatisticSend256To511byteFrm": hwEponOnuPonStatisticSend256To511byteFrm,
       "hwEponOnuPonStatisticSend512To1023byteFrm": hwEponOnuPonStatisticSend512To1023byteFrm,
       "hwEponOnuPonStatisticSend64byteFrm": hwEponOnuPonStatisticSend64byteFrm,
       "hwEponOnuPonStatisticSend65To127byteFrm": hwEponOnuPonStatisticSend65To127byteFrm,
       "hwEponOnuPonStatisticSendBcFrame": hwEponOnuPonStatisticSendBcFrame,
       "hwEponOnuPonStatisticSendByte": hwEponOnuPonStatisticSendByte,
       "hwEponOnuPonStatisticSendDelayByte": hwEponOnuPonStatisticSendDelayByte,
       "hwEponOnuPonStatisticSendDelayMax": hwEponOnuPonStatisticSendDelayMax,
       "hwEponOnuPonStatisticSendDelayThreshold": hwEponOnuPonStatisticSendDelayThreshold,
       "hwEponOnuPonStatisticSendDropByte": hwEponOnuPonStatisticSendDropByte,
       "hwEponOnuPonStatisticSendDropFrm": hwEponOnuPonStatisticSendDropFrm,
       "hwEponOnuPonStatisticSendFrame": hwEponOnuPonStatisticSendFrame,
       "hwEponOnuPonStatisticSendGreatThan1518byteFrm": hwEponOnuPonStatisticSendGreatThan1518byteFrm,
       "hwEponOnuPonStatisticSendMcFrame": hwEponOnuPonStatisticSendMcFrame,
       "hwEponOnuPonStatisticSendUcFrame": hwEponOnuPonStatisticSendUcFrame,
       "hwEponOnuPonStatisticSendUnusedByte": hwEponOnuPonStatisticSendUnusedByte,
       "hwEponOnuPonStatisticClear": hwEponOnuPonStatisticClear,
       "hwEponOnuUniStatisticTable": hwEponOnuUniStatisticTable,
       "hwEponOnuUniStatisticEntry": hwEponOnuUniStatisticEntry,
       "hwEponOnuUniStatisticRecvFrames": hwEponOnuUniStatisticRecvFrames,
       "hwEponOnuUniStatisticRecvMulticastFrames": hwEponOnuUniStatisticRecvMulticastFrames,
       "hwEponOnuUniStatisticRecvBroadcastFrames": hwEponOnuUniStatisticRecvBroadcastFrames,
       "hwEponOnuUniStatisticRecv64OctetFrames": hwEponOnuUniStatisticRecv64OctetFrames,
       "hwEponOnuUniStatisticRecv65To127OctetFrames": hwEponOnuUniStatisticRecv65To127OctetFrames,
       "hwEponOnuUniStatisticRecv128To255OctetFrames": hwEponOnuUniStatisticRecv128To255OctetFrames,
       "hwEponOnuUniStatisticRecv256To511OctetFrames": hwEponOnuUniStatisticRecv256To511OctetFrames,
       "hwEponOnuUniStatisticRecv512To1023OctetFrames": hwEponOnuUniStatisticRecv512To1023OctetFrames,
       "hwEponOnuUniStatisticRecv1024To1518OctetFrames": hwEponOnuUniStatisticRecv1024To1518OctetFrames,
       "hwEponOnuUniStatisticRecvUndersizeFrames": hwEponOnuUniStatisticRecvUndersizeFrames,
       "hwEponOnuUniStatisticRecvTooLongFrames": hwEponOnuUniStatisticRecvTooLongFrames,
       "hwEponOnuUniStatisticTransDropFrames": hwEponOnuUniStatisticTransDropFrames,
       "hwEponOnuUniStatisticTransFrames": hwEponOnuUniStatisticTransFrames,
       "hwEponOnuUniStatisticTransMtuExceededDiscardFrames": hwEponOnuUniStatisticTransMtuExceededDiscardFrames,
       "hwEponOnuUniStatisticClear": hwEponOnuUniStatisticClear,
       "hwEponDisplayAlarmObjects": hwEponDisplayAlarmObjects,
       "hwEponOnuAlarmStateTable": hwEponOnuAlarmStateTable,
       "hwEponOnuAlarmStateEntry": hwEponOnuAlarmStateEntry,
       "hwEponOnuAlarmStateKeyExchangeFail": hwEponOnuAlarmStateKeyExchangeFail,
       "hwEponOnuAlarmStateDyingGasp": hwEponOnuAlarmStateDyingGasp,
       "hwEponOnuAlarmStateLinkFault": hwEponOnuAlarmStateLinkFault,
       "hwEponOnuFirmWareLoadStateSucc": hwEponOnuFirmWareLoadStateSucc,
       "hwEponOnuFirmWareLoadStateFault": hwEponOnuFirmWareLoadStateFault,
       "hwEponOnuUniAlarmStateTable": hwEponOnuUniAlarmStateTable,
       "hwEponOnuUniAlarmStateEntry": hwEponOnuUniAlarmStateEntry,
       "hwEponOnuUniAlarmStateTransmitFail": hwEponOnuUniAlarmStateTransmitFail,
       "hwEponOnuUniAlarmStateLos": hwEponOnuUniAlarmStateLos,
       "hwEponOltAlarmStateTable": hwEponOltAlarmStateTable,
       "hwEponOltAlarmStateEntry": hwEponOltAlarmStateEntry,
       "hwEponOltAlarmStateDegrade": hwEponOltAlarmStateDegrade,
       "hwEponTrapObjects": hwEponTrapObjects,
       "hwEponSlotIndex": hwEponSlotIndex,
       "hwEponCardIndex": hwEponCardIndex,
       "hwEponPortIndex": hwEponPortIndex,
       "hwEponTrapOnuId": hwEponTrapOnuId,
       "hwEponTrapMac": hwEponTrapMac,
       "hwEponTrapPwd": hwEponTrapPwd,
       "hwEponTrap": hwEponTrap,
       "hwEponOltAlarmLosTrap": hwEponOltAlarmLosTrap,
       "hwEponOltAlarmLosResumeTrap": hwEponOltAlarmLosResumeTrap,
       "hwEponOltAutoFindTrap": hwEponOltAutoFindTrap,
       "hwEponOltAlarmTransmitFaultTrap": hwEponOltAlarmTransmitFaultTrap,
       "hwEponOnuAlarmPwdConlictTrap": hwEponOnuAlarmPwdConlictTrap,
       "hwEponOnuOnlineTrap": hwEponOnuOnlineTrap,
       "hwEponOnuOfflineTrap": hwEponOnuOfflineTrap,
       "hwEponConformance": hwEponConformance,
       "hwEponCompliances": hwEponCompliances,
       "hwEponCompliance": hwEponCompliance,
       "hwEponGroups": hwEponGroups,
       "hwEponGlobalGroup": hwEponGlobalGroup,
       "hwEponControlGroup": hwEponControlGroup,
       "hwEponProfileGroup": hwEponProfileGroup,
       "hwEponStatisticGroup": hwEponStatisticGroup,
       "hwEponDisplayAlarmObjectsGroup": hwEponDisplayAlarmObjectsGroup,
       "hwEponTrapObjectsGroup": hwEponTrapObjectsGroup,
       "hwEponTrapGroup": hwEponTrapGroup}
)
