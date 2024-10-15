# SNMP MIB module (HPN-ICF-ISSU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-ISSU-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:41 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpnicfIssuUpgrade = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133)
)
hpnicfIssuUpgrade.setRevisions(
        ("2013-01-15 15:36",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfIssuUpgradeMibObjects_ObjectIdentity = ObjectIdentity
hpnicfIssuUpgradeMibObjects = _HpnicfIssuUpgradeMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1)
)
_HpnicfIssuUpgradeGroup_ObjectIdentity = ObjectIdentity
hpnicfIssuUpgradeGroup = _HpnicfIssuUpgradeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 1)
)
_HpnicfIssuUpgradeImageTable_Object = MibTable
hpnicfIssuUpgradeImageTable = _HpnicfIssuUpgradeImageTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfIssuUpgradeImageTable.setStatus("current")
_HpnicfIssuUpgradeImageEntry_Object = MibTableRow
hpnicfIssuUpgradeImageEntry = _HpnicfIssuUpgradeImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 1, 1, 1)
)
hpnicfIssuUpgradeImageEntry.setIndexNames(
    (0, "HPN-ICF-ISSU-MIB", "hpnicfIssuUpgradeImageIndex"),
)
if mibBuilder.loadTexts:
    hpnicfIssuUpgradeImageEntry.setStatus("current")


class _HpnicfIssuUpgradeImageIndex_Type(Integer32):
    """Custom type hpnicfIssuUpgradeImageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfIssuUpgradeImageIndex_Type.__name__ = "Integer32"
_HpnicfIssuUpgradeImageIndex_Object = MibTableColumn
hpnicfIssuUpgradeImageIndex = _HpnicfIssuUpgradeImageIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 1, 1, 1, 1),
    _HpnicfIssuUpgradeImageIndex_Type()
)
hpnicfIssuUpgradeImageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIssuUpgradeImageIndex.setStatus("current")


class _HpnicfIssuUpgradeImageType_Type(Integer32):
    """Custom type hpnicfIssuUpgradeImageType based on Integer32"""
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
        *(("boot", 1),
          ("feature", 3),
          ("ipe", 4),
          ("system", 2))
    )


_HpnicfIssuUpgradeImageType_Type.__name__ = "Integer32"
_HpnicfIssuUpgradeImageType_Object = MibTableColumn
hpnicfIssuUpgradeImageType = _HpnicfIssuUpgradeImageType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 1, 1, 1, 2),
    _HpnicfIssuUpgradeImageType_Type()
)
hpnicfIssuUpgradeImageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIssuUpgradeImageType.setStatus("current")


class _HpnicfIssuUpgradeImageURL_Type(DisplayString):
    """Custom type hpnicfIssuUpgradeImageURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_HpnicfIssuUpgradeImageURL_Type.__name__ = "DisplayString"
_HpnicfIssuUpgradeImageURL_Object = MibTableColumn
hpnicfIssuUpgradeImageURL = _HpnicfIssuUpgradeImageURL_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 1, 1, 1, 3),
    _HpnicfIssuUpgradeImageURL_Type()
)
hpnicfIssuUpgradeImageURL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIssuUpgradeImageURL.setStatus("current")
_HpnicfIssuUpgradeImageRowStatus_Type = RowStatus
_HpnicfIssuUpgradeImageRowStatus_Object = MibTableColumn
hpnicfIssuUpgradeImageRowStatus = _HpnicfIssuUpgradeImageRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 1, 1, 1, 4),
    _HpnicfIssuUpgradeImageRowStatus_Type()
)
hpnicfIssuUpgradeImageRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIssuUpgradeImageRowStatus.setStatus("current")
_HpnicfIssuOp_ObjectIdentity = ObjectIdentity
hpnicfIssuOp = _HpnicfIssuOp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 1, 2)
)


class _HpnicfIssuOpType_Type(Integer32):
    """Custom type hpnicfIssuOpType based on Integer32"""
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
        *(("done", 2),
          ("install", 4),
          ("none", 1),
          ("rollback", 5),
          ("test", 3))
    )


_HpnicfIssuOpType_Type.__name__ = "Integer32"
_HpnicfIssuOpType_Object = MibScalar
hpnicfIssuOpType = _HpnicfIssuOpType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 1, 2, 1),
    _HpnicfIssuOpType_Type()
)
hpnicfIssuOpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIssuOpType.setStatus("current")


class _HpnicfIssuImageFileOverwrite_Type(TruthValue):
    """Custom type hpnicfIssuImageFileOverwrite based on TruthValue"""


_HpnicfIssuImageFileOverwrite_Object = MibScalar
hpnicfIssuImageFileOverwrite = _HpnicfIssuImageFileOverwrite_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 1, 2, 2),
    _HpnicfIssuImageFileOverwrite_Type()
)
hpnicfIssuImageFileOverwrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIssuImageFileOverwrite.setStatus("current")


class _HpnicfIssuOpTrapEnable_Type(TruthValue):
    """Custom type hpnicfIssuOpTrapEnable based on TruthValue"""


_HpnicfIssuOpTrapEnable_Object = MibScalar
hpnicfIssuOpTrapEnable = _HpnicfIssuOpTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 1, 2, 3),
    _HpnicfIssuOpTrapEnable_Type()
)
hpnicfIssuOpTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIssuOpTrapEnable.setStatus("current")


class _HpnicfIssuOpStatus_Type(Integer32):
    """Custom type hpnicfIssuOpStatus based on Integer32"""
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
        *(("failure", 2),
          ("inProgress", 3),
          ("none", 1),
          ("rollbackInProgress", 5),
          ("rollbackSuccess", 6),
          ("success", 4))
    )


_HpnicfIssuOpStatus_Type.__name__ = "Integer32"
_HpnicfIssuOpStatus_Object = MibScalar
hpnicfIssuOpStatus = _HpnicfIssuOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 1, 2, 4),
    _HpnicfIssuOpStatus_Type()
)
hpnicfIssuOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIssuOpStatus.setStatus("current")


class _HpnicfIssuFailedReason_Type(DisplayString):
    """Custom type hpnicfIssuFailedReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfIssuFailedReason_Type.__name__ = "DisplayString"
_HpnicfIssuFailedReason_Object = MibScalar
hpnicfIssuFailedReason = _HpnicfIssuFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 1, 2, 5),
    _HpnicfIssuFailedReason_Type()
)
hpnicfIssuFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIssuFailedReason.setStatus("current")


class _HpnicfIssuOpTimeCompleted_Type(DisplayString):
    """Custom type hpnicfIssuOpTimeCompleted based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfIssuOpTimeCompleted_Type.__name__ = "DisplayString"
_HpnicfIssuOpTimeCompleted_Object = MibScalar
hpnicfIssuOpTimeCompleted = _HpnicfIssuOpTimeCompleted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 1, 2, 6),
    _HpnicfIssuOpTimeCompleted_Type()
)
hpnicfIssuOpTimeCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIssuOpTimeCompleted.setStatus("current")


class _HpnicfIssuLastOpType_Type(Integer32):
    """Custom type hpnicfIssuLastOpType based on Integer32"""
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
        *(("done", 2),
          ("install", 4),
          ("none", 1),
          ("rollback", 5),
          ("test", 3))
    )


_HpnicfIssuLastOpType_Type.__name__ = "Integer32"
_HpnicfIssuLastOpType_Object = MibScalar
hpnicfIssuLastOpType = _HpnicfIssuLastOpType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 1, 2, 7),
    _HpnicfIssuLastOpType_Type()
)
hpnicfIssuLastOpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIssuLastOpType.setStatus("current")


class _HpnicfIssuLastOpStatus_Type(Integer32):
    """Custom type hpnicfIssuLastOpStatus based on Integer32"""
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
        *(("failure", 2),
          ("inProgress", 3),
          ("none", 1),
          ("rollbackInProgress", 5),
          ("rollbackSuccess", 6),
          ("success", 4))
    )


_HpnicfIssuLastOpStatus_Type.__name__ = "Integer32"
_HpnicfIssuLastOpStatus_Object = MibScalar
hpnicfIssuLastOpStatus = _HpnicfIssuLastOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 1, 2, 8),
    _HpnicfIssuLastOpStatus_Type()
)
hpnicfIssuLastOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIssuLastOpStatus.setStatus("current")


class _HpnicfIssuLastOpFailedReason_Type(DisplayString):
    """Custom type hpnicfIssuLastOpFailedReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfIssuLastOpFailedReason_Type.__name__ = "DisplayString"
_HpnicfIssuLastOpFailedReason_Object = MibScalar
hpnicfIssuLastOpFailedReason = _HpnicfIssuLastOpFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 1, 2, 9),
    _HpnicfIssuLastOpFailedReason_Type()
)
hpnicfIssuLastOpFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIssuLastOpFailedReason.setStatus("current")


class _HpnicfIssuLastOpTimeCompleted_Type(DisplayString):
    """Custom type hpnicfIssuLastOpTimeCompleted based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfIssuLastOpTimeCompleted_Type.__name__ = "DisplayString"
_HpnicfIssuLastOpTimeCompleted_Object = MibScalar
hpnicfIssuLastOpTimeCompleted = _HpnicfIssuLastOpTimeCompleted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 1, 2, 10),
    _HpnicfIssuLastOpTimeCompleted_Type()
)
hpnicfIssuLastOpTimeCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIssuLastOpTimeCompleted.setStatus("current")
_HpnicfIssuUpgradeResultGroup_ObjectIdentity = ObjectIdentity
hpnicfIssuUpgradeResultGroup = _HpnicfIssuUpgradeResultGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 2)
)
_HpnicfIssuCompatibleResult_ObjectIdentity = ObjectIdentity
hpnicfIssuCompatibleResult = _HpnicfIssuCompatibleResult_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 2, 1)
)


class _HpnicfIssuCompatibleResultStatus_Type(Integer32):
    """Custom type hpnicfIssuCompatibleResultStatus based on Integer32"""
    defaultValue = 1

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
        *(("compatible", 3),
          ("failure", 4),
          ("inCompatible", 2),
          ("none", 1))
    )


_HpnicfIssuCompatibleResultStatus_Type.__name__ = "Integer32"
_HpnicfIssuCompatibleResultStatus_Object = MibScalar
hpnicfIssuCompatibleResultStatus = _HpnicfIssuCompatibleResultStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 2, 1, 1),
    _HpnicfIssuCompatibleResultStatus_Type()
)
hpnicfIssuCompatibleResultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIssuCompatibleResultStatus.setStatus("current")


class _HpnicfIssuCompatibleResultFailedReason_Type(DisplayString):
    """Custom type hpnicfIssuCompatibleResultFailedReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfIssuCompatibleResultFailedReason_Type.__name__ = "DisplayString"
_HpnicfIssuCompatibleResultFailedReason_Object = MibScalar
hpnicfIssuCompatibleResultFailedReason = _HpnicfIssuCompatibleResultFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 2, 1, 2),
    _HpnicfIssuCompatibleResultFailedReason_Type()
)
hpnicfIssuCompatibleResultFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIssuCompatibleResultFailedReason.setStatus("current")
_HpnicfIssuTestResultTable_Object = MibTable
hpnicfIssuTestResultTable = _HpnicfIssuTestResultTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfIssuTestResultTable.setStatus("current")
_HpnicfIssuTestResultEntry_Object = MibTableRow
hpnicfIssuTestResultEntry = _HpnicfIssuTestResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 2, 2, 1)
)
hpnicfIssuTestResultEntry.setIndexNames(
    (0, "HPN-ICF-ISSU-MIB", "hpnicfIssuTestResultIndex"),
)
if mibBuilder.loadTexts:
    hpnicfIssuTestResultEntry.setStatus("current")


class _HpnicfIssuTestResultIndex_Type(Integer32):
    """Custom type hpnicfIssuTestResultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfIssuTestResultIndex_Type.__name__ = "Integer32"
_HpnicfIssuTestResultIndex_Object = MibTableColumn
hpnicfIssuTestResultIndex = _HpnicfIssuTestResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 2, 2, 1, 1),
    _HpnicfIssuTestResultIndex_Type()
)
hpnicfIssuTestResultIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIssuTestResultIndex.setStatus("current")


class _HpnicfIssuTestDeviceChassisID_Type(Integer32):
    """Custom type hpnicfIssuTestDeviceChassisID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfIssuTestDeviceChassisID_Type.__name__ = "Integer32"
_HpnicfIssuTestDeviceChassisID_Object = MibTableColumn
hpnicfIssuTestDeviceChassisID = _HpnicfIssuTestDeviceChassisID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 2, 2, 1, 2),
    _HpnicfIssuTestDeviceChassisID_Type()
)
hpnicfIssuTestDeviceChassisID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIssuTestDeviceChassisID.setStatus("current")


class _HpnicfIssuTestDeviceSlotID_Type(Integer32):
    """Custom type hpnicfIssuTestDeviceSlotID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfIssuTestDeviceSlotID_Type.__name__ = "Integer32"
_HpnicfIssuTestDeviceSlotID_Object = MibTableColumn
hpnicfIssuTestDeviceSlotID = _HpnicfIssuTestDeviceSlotID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 2, 2, 1, 3),
    _HpnicfIssuTestDeviceSlotID_Type()
)
hpnicfIssuTestDeviceSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIssuTestDeviceSlotID.setStatus("current")


class _HpnicfIssuTestDeviceCpuID_Type(Integer32):
    """Custom type hpnicfIssuTestDeviceCpuID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HpnicfIssuTestDeviceCpuID_Type.__name__ = "Integer32"
_HpnicfIssuTestDeviceCpuID_Object = MibTableColumn
hpnicfIssuTestDeviceCpuID = _HpnicfIssuTestDeviceCpuID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 2, 2, 1, 4),
    _HpnicfIssuTestDeviceCpuID_Type()
)
hpnicfIssuTestDeviceCpuID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIssuTestDeviceCpuID.setStatus("current")


class _HpnicfIssuTestDeviceUpgradeWay_Type(Integer32):
    """Custom type hpnicfIssuTestDeviceUpgradeWay based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("fileUpgrade", 6),
          ("incompatibleUpgrade", 7),
          ("issuReboot", 4),
          ("none", 1),
          ("reboot", 2),
          ("sequenceReboot", 3),
          ("serviceUpgrade", 5))
    )


_HpnicfIssuTestDeviceUpgradeWay_Type.__name__ = "Integer32"
_HpnicfIssuTestDeviceUpgradeWay_Object = MibTableColumn
hpnicfIssuTestDeviceUpgradeWay = _HpnicfIssuTestDeviceUpgradeWay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 2, 2, 1, 5),
    _HpnicfIssuTestDeviceUpgradeWay_Type()
)
hpnicfIssuTestDeviceUpgradeWay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIssuTestDeviceUpgradeWay.setStatus("current")
_HpnicfIssuUpgradeResultTable_Object = MibTable
hpnicfIssuUpgradeResultTable = _HpnicfIssuUpgradeResultTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hpnicfIssuUpgradeResultTable.setStatus("current")
_HpnicfIssuUpgradeResultEntry_Object = MibTableRow
hpnicfIssuUpgradeResultEntry = _HpnicfIssuUpgradeResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 2, 3, 1)
)
hpnicfIssuUpgradeResultEntry.setIndexNames(
    (0, "HPN-ICF-ISSU-MIB", "hpnicfIssuUpgradeResultIndex"),
)
if mibBuilder.loadTexts:
    hpnicfIssuUpgradeResultEntry.setStatus("current")


class _HpnicfIssuUpgradeResultIndex_Type(Integer32):
    """Custom type hpnicfIssuUpgradeResultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfIssuUpgradeResultIndex_Type.__name__ = "Integer32"
_HpnicfIssuUpgradeResultIndex_Object = MibTableColumn
hpnicfIssuUpgradeResultIndex = _HpnicfIssuUpgradeResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 2, 3, 1, 1),
    _HpnicfIssuUpgradeResultIndex_Type()
)
hpnicfIssuUpgradeResultIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIssuUpgradeResultIndex.setStatus("current")


class _HpnicfIssuUpgradeDeviceChassisID_Type(Integer32):
    """Custom type hpnicfIssuUpgradeDeviceChassisID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfIssuUpgradeDeviceChassisID_Type.__name__ = "Integer32"
_HpnicfIssuUpgradeDeviceChassisID_Object = MibTableColumn
hpnicfIssuUpgradeDeviceChassisID = _HpnicfIssuUpgradeDeviceChassisID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 2, 3, 1, 2),
    _HpnicfIssuUpgradeDeviceChassisID_Type()
)
hpnicfIssuUpgradeDeviceChassisID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIssuUpgradeDeviceChassisID.setStatus("current")


class _HpnicfIssuUpgradeDeviceSlotID_Type(Integer32):
    """Custom type hpnicfIssuUpgradeDeviceSlotID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfIssuUpgradeDeviceSlotID_Type.__name__ = "Integer32"
_HpnicfIssuUpgradeDeviceSlotID_Object = MibTableColumn
hpnicfIssuUpgradeDeviceSlotID = _HpnicfIssuUpgradeDeviceSlotID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 2, 3, 1, 3),
    _HpnicfIssuUpgradeDeviceSlotID_Type()
)
hpnicfIssuUpgradeDeviceSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIssuUpgradeDeviceSlotID.setStatus("current")


class _HpnicfIssuUpgradeDeviceCpuID_Type(Integer32):
    """Custom type hpnicfIssuUpgradeDeviceCpuID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HpnicfIssuUpgradeDeviceCpuID_Type.__name__ = "Integer32"
_HpnicfIssuUpgradeDeviceCpuID_Object = MibTableColumn
hpnicfIssuUpgradeDeviceCpuID = _HpnicfIssuUpgradeDeviceCpuID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 2, 3, 1, 4),
    _HpnicfIssuUpgradeDeviceCpuID_Type()
)
hpnicfIssuUpgradeDeviceCpuID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIssuUpgradeDeviceCpuID.setStatus("current")


class _HpnicfIssuUpgradeState_Type(Integer32):
    """Custom type hpnicfIssuUpgradeState based on Integer32"""
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
        *(("committed", 7),
          ("committing", 6),
          ("init", 1),
          ("loaded", 3),
          ("loading", 2),
          ("rollbacked", 9),
          ("rollbacking", 8),
          ("switching", 4),
          ("switchover", 5))
    )


_HpnicfIssuUpgradeState_Type.__name__ = "Integer32"
_HpnicfIssuUpgradeState_Object = MibTableColumn
hpnicfIssuUpgradeState = _HpnicfIssuUpgradeState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 2, 3, 1, 5),
    _HpnicfIssuUpgradeState_Type()
)
hpnicfIssuUpgradeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIssuUpgradeState.setStatus("current")


class _HpnicfIssuDeviceUpgradeWay_Type(Integer32):
    """Custom type hpnicfIssuDeviceUpgradeWay based on Integer32"""
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
        *(("fileUpgrade", 6),
          ("incompatibleUpgrade", 7),
          ("issuReboot", 4),
          ("none", 1),
          ("reboot", 2),
          ("sequenceReboot", 3),
          ("serviceUpgrade", 5))
    )


_HpnicfIssuDeviceUpgradeWay_Type.__name__ = "Integer32"
_HpnicfIssuDeviceUpgradeWay_Object = MibTableColumn
hpnicfIssuDeviceUpgradeWay = _HpnicfIssuDeviceUpgradeWay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 2, 3, 1, 6),
    _HpnicfIssuDeviceUpgradeWay_Type()
)
hpnicfIssuDeviceUpgradeWay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIssuDeviceUpgradeWay.setStatus("current")


class _HpnicfIssuUpgradeDeviceStatus_Type(Integer32):
    """Custom type hpnicfIssuUpgradeDeviceStatus based on Integer32"""
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
        *(("failure", 4),
          ("inProcess", 2),
          ("success", 3),
          ("waitingUpgrade", 1))
    )


_HpnicfIssuUpgradeDeviceStatus_Type.__name__ = "Integer32"
_HpnicfIssuUpgradeDeviceStatus_Object = MibTableColumn
hpnicfIssuUpgradeDeviceStatus = _HpnicfIssuUpgradeDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 2, 3, 1, 7),
    _HpnicfIssuUpgradeDeviceStatus_Type()
)
hpnicfIssuUpgradeDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIssuUpgradeDeviceStatus.setStatus("current")


class _HpnicfIssuUpgradeFailedReason_Type(DisplayString):
    """Custom type hpnicfIssuUpgradeFailedReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfIssuUpgradeFailedReason_Type.__name__ = "DisplayString"
_HpnicfIssuUpgradeFailedReason_Object = MibTableColumn
hpnicfIssuUpgradeFailedReason = _HpnicfIssuUpgradeFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 1, 2, 3, 1, 8),
    _HpnicfIssuUpgradeFailedReason_Type()
)
hpnicfIssuUpgradeFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIssuUpgradeFailedReason.setStatus("current")
_HpnicfIssuUpgradeNotify_ObjectIdentity = ObjectIdentity
hpnicfIssuUpgradeNotify = _HpnicfIssuUpgradeNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 2)
)
_HpnicfIssuUpgradeTrapPrefix_ObjectIdentity = ObjectIdentity
hpnicfIssuUpgradeTrapPrefix = _HpnicfIssuUpgradeTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 2, 0)
)

# Managed Objects groups


# Notification objects

hpnicfIssuUpgradeOpCompletionNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133, 2, 0, 1)
)
hpnicfIssuUpgradeOpCompletionNotify.setObjects(
      *(("HPN-ICF-ISSU-MIB", "hpnicfIssuOpType"),
        ("HPN-ICF-ISSU-MIB", "hpnicfIssuOpStatus"),
        ("HPN-ICF-ISSU-MIB", "hpnicfIssuFailedReason"),
        ("HPN-ICF-ISSU-MIB", "hpnicfIssuOpTimeCompleted"))
)
if mibBuilder.loadTexts:
    hpnicfIssuUpgradeOpCompletionNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-ISSU-MIB",
    **{"hpnicfIssuUpgrade": hpnicfIssuUpgrade,
       "hpnicfIssuUpgradeMibObjects": hpnicfIssuUpgradeMibObjects,
       "hpnicfIssuUpgradeGroup": hpnicfIssuUpgradeGroup,
       "hpnicfIssuUpgradeImageTable": hpnicfIssuUpgradeImageTable,
       "hpnicfIssuUpgradeImageEntry": hpnicfIssuUpgradeImageEntry,
       "hpnicfIssuUpgradeImageIndex": hpnicfIssuUpgradeImageIndex,
       "hpnicfIssuUpgradeImageType": hpnicfIssuUpgradeImageType,
       "hpnicfIssuUpgradeImageURL": hpnicfIssuUpgradeImageURL,
       "hpnicfIssuUpgradeImageRowStatus": hpnicfIssuUpgradeImageRowStatus,
       "hpnicfIssuOp": hpnicfIssuOp,
       "hpnicfIssuOpType": hpnicfIssuOpType,
       "hpnicfIssuImageFileOverwrite": hpnicfIssuImageFileOverwrite,
       "hpnicfIssuOpTrapEnable": hpnicfIssuOpTrapEnable,
       "hpnicfIssuOpStatus": hpnicfIssuOpStatus,
       "hpnicfIssuFailedReason": hpnicfIssuFailedReason,
       "hpnicfIssuOpTimeCompleted": hpnicfIssuOpTimeCompleted,
       "hpnicfIssuLastOpType": hpnicfIssuLastOpType,
       "hpnicfIssuLastOpStatus": hpnicfIssuLastOpStatus,
       "hpnicfIssuLastOpFailedReason": hpnicfIssuLastOpFailedReason,
       "hpnicfIssuLastOpTimeCompleted": hpnicfIssuLastOpTimeCompleted,
       "hpnicfIssuUpgradeResultGroup": hpnicfIssuUpgradeResultGroup,
       "hpnicfIssuCompatibleResult": hpnicfIssuCompatibleResult,
       "hpnicfIssuCompatibleResultStatus": hpnicfIssuCompatibleResultStatus,
       "hpnicfIssuCompatibleResultFailedReason": hpnicfIssuCompatibleResultFailedReason,
       "hpnicfIssuTestResultTable": hpnicfIssuTestResultTable,
       "hpnicfIssuTestResultEntry": hpnicfIssuTestResultEntry,
       "hpnicfIssuTestResultIndex": hpnicfIssuTestResultIndex,
       "hpnicfIssuTestDeviceChassisID": hpnicfIssuTestDeviceChassisID,
       "hpnicfIssuTestDeviceSlotID": hpnicfIssuTestDeviceSlotID,
       "hpnicfIssuTestDeviceCpuID": hpnicfIssuTestDeviceCpuID,
       "hpnicfIssuTestDeviceUpgradeWay": hpnicfIssuTestDeviceUpgradeWay,
       "hpnicfIssuUpgradeResultTable": hpnicfIssuUpgradeResultTable,
       "hpnicfIssuUpgradeResultEntry": hpnicfIssuUpgradeResultEntry,
       "hpnicfIssuUpgradeResultIndex": hpnicfIssuUpgradeResultIndex,
       "hpnicfIssuUpgradeDeviceChassisID": hpnicfIssuUpgradeDeviceChassisID,
       "hpnicfIssuUpgradeDeviceSlotID": hpnicfIssuUpgradeDeviceSlotID,
       "hpnicfIssuUpgradeDeviceCpuID": hpnicfIssuUpgradeDeviceCpuID,
       "hpnicfIssuUpgradeState": hpnicfIssuUpgradeState,
       "hpnicfIssuDeviceUpgradeWay": hpnicfIssuDeviceUpgradeWay,
       "hpnicfIssuUpgradeDeviceStatus": hpnicfIssuUpgradeDeviceStatus,
       "hpnicfIssuUpgradeFailedReason": hpnicfIssuUpgradeFailedReason,
       "hpnicfIssuUpgradeNotify": hpnicfIssuUpgradeNotify,
       "hpnicfIssuUpgradeTrapPrefix": hpnicfIssuUpgradeTrapPrefix,
       "hpnicfIssuUpgradeOpCompletionNotify": hpnicfIssuUpgradeOpCompletionNotify}
)
