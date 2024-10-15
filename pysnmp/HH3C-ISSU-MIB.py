# SNMP MIB module (HH3C-ISSU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-ISSU-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:41 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cIssuUpgrade = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 133)
)
hh3cIssuUpgrade.setRevisions(
        ("2013-01-15 15:36",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cIssuUpgradeMibObjects_ObjectIdentity = ObjectIdentity
hh3cIssuUpgradeMibObjects = _Hh3cIssuUpgradeMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 133, 1)
)
_Hh3cIssuUpgradeGroup_ObjectIdentity = ObjectIdentity
hh3cIssuUpgradeGroup = _Hh3cIssuUpgradeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 1)
)
_Hh3cIssuUpgradeImageTable_Object = MibTable
hh3cIssuUpgradeImageTable = _Hh3cIssuUpgradeImageTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cIssuUpgradeImageTable.setStatus("current")
_Hh3cIssuUpgradeImageEntry_Object = MibTableRow
hh3cIssuUpgradeImageEntry = _Hh3cIssuUpgradeImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 1, 1, 1)
)
hh3cIssuUpgradeImageEntry.setIndexNames(
    (0, "HH3C-ISSU-MIB", "hh3cIssuUpgradeImageIndex"),
)
if mibBuilder.loadTexts:
    hh3cIssuUpgradeImageEntry.setStatus("current")


class _Hh3cIssuUpgradeImageIndex_Type(Integer32):
    """Custom type hh3cIssuUpgradeImageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cIssuUpgradeImageIndex_Type.__name__ = "Integer32"
_Hh3cIssuUpgradeImageIndex_Object = MibTableColumn
hh3cIssuUpgradeImageIndex = _Hh3cIssuUpgradeImageIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 1, 1, 1, 1),
    _Hh3cIssuUpgradeImageIndex_Type()
)
hh3cIssuUpgradeImageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIssuUpgradeImageIndex.setStatus("current")


class _Hh3cIssuUpgradeImageType_Type(Integer32):
    """Custom type hh3cIssuUpgradeImageType based on Integer32"""
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


_Hh3cIssuUpgradeImageType_Type.__name__ = "Integer32"
_Hh3cIssuUpgradeImageType_Object = MibTableColumn
hh3cIssuUpgradeImageType = _Hh3cIssuUpgradeImageType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 1, 1, 1, 2),
    _Hh3cIssuUpgradeImageType_Type()
)
hh3cIssuUpgradeImageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIssuUpgradeImageType.setStatus("current")


class _Hh3cIssuUpgradeImageURL_Type(DisplayString):
    """Custom type hh3cIssuUpgradeImageURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_Hh3cIssuUpgradeImageURL_Type.__name__ = "DisplayString"
_Hh3cIssuUpgradeImageURL_Object = MibTableColumn
hh3cIssuUpgradeImageURL = _Hh3cIssuUpgradeImageURL_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 1, 1, 1, 3),
    _Hh3cIssuUpgradeImageURL_Type()
)
hh3cIssuUpgradeImageURL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIssuUpgradeImageURL.setStatus("current")
_Hh3cIssuUpgradeImageRowStatus_Type = RowStatus
_Hh3cIssuUpgradeImageRowStatus_Object = MibTableColumn
hh3cIssuUpgradeImageRowStatus = _Hh3cIssuUpgradeImageRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 1, 1, 1, 4),
    _Hh3cIssuUpgradeImageRowStatus_Type()
)
hh3cIssuUpgradeImageRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIssuUpgradeImageRowStatus.setStatus("current")
_Hh3cIssuOp_ObjectIdentity = ObjectIdentity
hh3cIssuOp = _Hh3cIssuOp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 1, 2)
)


class _Hh3cIssuOpType_Type(Integer32):
    """Custom type hh3cIssuOpType based on Integer32"""
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


_Hh3cIssuOpType_Type.__name__ = "Integer32"
_Hh3cIssuOpType_Object = MibScalar
hh3cIssuOpType = _Hh3cIssuOpType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 1, 2, 1),
    _Hh3cIssuOpType_Type()
)
hh3cIssuOpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIssuOpType.setStatus("current")


class _Hh3cIssuImageFileOverwrite_Type(TruthValue):
    """Custom type hh3cIssuImageFileOverwrite based on TruthValue"""


_Hh3cIssuImageFileOverwrite_Object = MibScalar
hh3cIssuImageFileOverwrite = _Hh3cIssuImageFileOverwrite_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 1, 2, 2),
    _Hh3cIssuImageFileOverwrite_Type()
)
hh3cIssuImageFileOverwrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIssuImageFileOverwrite.setStatus("current")


class _Hh3cIssuOpTrapEnable_Type(TruthValue):
    """Custom type hh3cIssuOpTrapEnable based on TruthValue"""


_Hh3cIssuOpTrapEnable_Object = MibScalar
hh3cIssuOpTrapEnable = _Hh3cIssuOpTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 1, 2, 3),
    _Hh3cIssuOpTrapEnable_Type()
)
hh3cIssuOpTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIssuOpTrapEnable.setStatus("current")


class _Hh3cIssuOpStatus_Type(Integer32):
    """Custom type hh3cIssuOpStatus based on Integer32"""
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


_Hh3cIssuOpStatus_Type.__name__ = "Integer32"
_Hh3cIssuOpStatus_Object = MibScalar
hh3cIssuOpStatus = _Hh3cIssuOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 1, 2, 4),
    _Hh3cIssuOpStatus_Type()
)
hh3cIssuOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIssuOpStatus.setStatus("current")


class _Hh3cIssuFailedReason_Type(DisplayString):
    """Custom type hh3cIssuFailedReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cIssuFailedReason_Type.__name__ = "DisplayString"
_Hh3cIssuFailedReason_Object = MibScalar
hh3cIssuFailedReason = _Hh3cIssuFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 1, 2, 5),
    _Hh3cIssuFailedReason_Type()
)
hh3cIssuFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIssuFailedReason.setStatus("current")


class _Hh3cIssuOpTimeCompleted_Type(DisplayString):
    """Custom type hh3cIssuOpTimeCompleted based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cIssuOpTimeCompleted_Type.__name__ = "DisplayString"
_Hh3cIssuOpTimeCompleted_Object = MibScalar
hh3cIssuOpTimeCompleted = _Hh3cIssuOpTimeCompleted_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 1, 2, 6),
    _Hh3cIssuOpTimeCompleted_Type()
)
hh3cIssuOpTimeCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIssuOpTimeCompleted.setStatus("current")


class _Hh3cIssuLastOpType_Type(Integer32):
    """Custom type hh3cIssuLastOpType based on Integer32"""
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


_Hh3cIssuLastOpType_Type.__name__ = "Integer32"
_Hh3cIssuLastOpType_Object = MibScalar
hh3cIssuLastOpType = _Hh3cIssuLastOpType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 1, 2, 7),
    _Hh3cIssuLastOpType_Type()
)
hh3cIssuLastOpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIssuLastOpType.setStatus("current")


class _Hh3cIssuLastOpStatus_Type(Integer32):
    """Custom type hh3cIssuLastOpStatus based on Integer32"""
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


_Hh3cIssuLastOpStatus_Type.__name__ = "Integer32"
_Hh3cIssuLastOpStatus_Object = MibScalar
hh3cIssuLastOpStatus = _Hh3cIssuLastOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 1, 2, 8),
    _Hh3cIssuLastOpStatus_Type()
)
hh3cIssuLastOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIssuLastOpStatus.setStatus("current")


class _Hh3cIssuLastOpFailedReason_Type(DisplayString):
    """Custom type hh3cIssuLastOpFailedReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cIssuLastOpFailedReason_Type.__name__ = "DisplayString"
_Hh3cIssuLastOpFailedReason_Object = MibScalar
hh3cIssuLastOpFailedReason = _Hh3cIssuLastOpFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 1, 2, 9),
    _Hh3cIssuLastOpFailedReason_Type()
)
hh3cIssuLastOpFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIssuLastOpFailedReason.setStatus("current")


class _Hh3cIssuLastOpTimeCompleted_Type(DisplayString):
    """Custom type hh3cIssuLastOpTimeCompleted based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cIssuLastOpTimeCompleted_Type.__name__ = "DisplayString"
_Hh3cIssuLastOpTimeCompleted_Object = MibScalar
hh3cIssuLastOpTimeCompleted = _Hh3cIssuLastOpTimeCompleted_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 1, 2, 10),
    _Hh3cIssuLastOpTimeCompleted_Type()
)
hh3cIssuLastOpTimeCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIssuLastOpTimeCompleted.setStatus("current")
_Hh3cIssuUpgradeResultGroup_ObjectIdentity = ObjectIdentity
hh3cIssuUpgradeResultGroup = _Hh3cIssuUpgradeResultGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 2)
)
_Hh3cIssuCompatibleResult_ObjectIdentity = ObjectIdentity
hh3cIssuCompatibleResult = _Hh3cIssuCompatibleResult_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 2, 1)
)


class _Hh3cIssuCompatibleResultStatus_Type(Integer32):
    """Custom type hh3cIssuCompatibleResultStatus based on Integer32"""
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


_Hh3cIssuCompatibleResultStatus_Type.__name__ = "Integer32"
_Hh3cIssuCompatibleResultStatus_Object = MibScalar
hh3cIssuCompatibleResultStatus = _Hh3cIssuCompatibleResultStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 2, 1, 1),
    _Hh3cIssuCompatibleResultStatus_Type()
)
hh3cIssuCompatibleResultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIssuCompatibleResultStatus.setStatus("current")


class _Hh3cIssuCompatibleResultFailedReason_Type(DisplayString):
    """Custom type hh3cIssuCompatibleResultFailedReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cIssuCompatibleResultFailedReason_Type.__name__ = "DisplayString"
_Hh3cIssuCompatibleResultFailedReason_Object = MibScalar
hh3cIssuCompatibleResultFailedReason = _Hh3cIssuCompatibleResultFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 2, 1, 2),
    _Hh3cIssuCompatibleResultFailedReason_Type()
)
hh3cIssuCompatibleResultFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIssuCompatibleResultFailedReason.setStatus("current")
_Hh3cIssuTestResultTable_Object = MibTable
hh3cIssuTestResultTable = _Hh3cIssuTestResultTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cIssuTestResultTable.setStatus("current")
_Hh3cIssuTestResultEntry_Object = MibTableRow
hh3cIssuTestResultEntry = _Hh3cIssuTestResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 2, 2, 1)
)
hh3cIssuTestResultEntry.setIndexNames(
    (0, "HH3C-ISSU-MIB", "hh3cIssuTestResultIndex"),
)
if mibBuilder.loadTexts:
    hh3cIssuTestResultEntry.setStatus("current")


class _Hh3cIssuTestResultIndex_Type(Integer32):
    """Custom type hh3cIssuTestResultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cIssuTestResultIndex_Type.__name__ = "Integer32"
_Hh3cIssuTestResultIndex_Object = MibTableColumn
hh3cIssuTestResultIndex = _Hh3cIssuTestResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 2, 2, 1, 1),
    _Hh3cIssuTestResultIndex_Type()
)
hh3cIssuTestResultIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIssuTestResultIndex.setStatus("current")


class _Hh3cIssuTestDeviceChassisID_Type(Integer32):
    """Custom type hh3cIssuTestDeviceChassisID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cIssuTestDeviceChassisID_Type.__name__ = "Integer32"
_Hh3cIssuTestDeviceChassisID_Object = MibTableColumn
hh3cIssuTestDeviceChassisID = _Hh3cIssuTestDeviceChassisID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 2, 2, 1, 2),
    _Hh3cIssuTestDeviceChassisID_Type()
)
hh3cIssuTestDeviceChassisID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIssuTestDeviceChassisID.setStatus("current")


class _Hh3cIssuTestDeviceSlotID_Type(Integer32):
    """Custom type hh3cIssuTestDeviceSlotID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cIssuTestDeviceSlotID_Type.__name__ = "Integer32"
_Hh3cIssuTestDeviceSlotID_Object = MibTableColumn
hh3cIssuTestDeviceSlotID = _Hh3cIssuTestDeviceSlotID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 2, 2, 1, 3),
    _Hh3cIssuTestDeviceSlotID_Type()
)
hh3cIssuTestDeviceSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIssuTestDeviceSlotID.setStatus("current")


class _Hh3cIssuTestDeviceCpuID_Type(Integer32):
    """Custom type hh3cIssuTestDeviceCpuID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hh3cIssuTestDeviceCpuID_Type.__name__ = "Integer32"
_Hh3cIssuTestDeviceCpuID_Object = MibTableColumn
hh3cIssuTestDeviceCpuID = _Hh3cIssuTestDeviceCpuID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 2, 2, 1, 4),
    _Hh3cIssuTestDeviceCpuID_Type()
)
hh3cIssuTestDeviceCpuID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIssuTestDeviceCpuID.setStatus("current")


class _Hh3cIssuTestDeviceUpgradeWay_Type(Integer32):
    """Custom type hh3cIssuTestDeviceUpgradeWay based on Integer32"""
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


_Hh3cIssuTestDeviceUpgradeWay_Type.__name__ = "Integer32"
_Hh3cIssuTestDeviceUpgradeWay_Object = MibTableColumn
hh3cIssuTestDeviceUpgradeWay = _Hh3cIssuTestDeviceUpgradeWay_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 2, 2, 1, 5),
    _Hh3cIssuTestDeviceUpgradeWay_Type()
)
hh3cIssuTestDeviceUpgradeWay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIssuTestDeviceUpgradeWay.setStatus("current")
_Hh3cIssuUpgradeResultTable_Object = MibTable
hh3cIssuUpgradeResultTable = _Hh3cIssuUpgradeResultTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cIssuUpgradeResultTable.setStatus("current")
_Hh3cIssuUpgradeResultEntry_Object = MibTableRow
hh3cIssuUpgradeResultEntry = _Hh3cIssuUpgradeResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 2, 3, 1)
)
hh3cIssuUpgradeResultEntry.setIndexNames(
    (0, "HH3C-ISSU-MIB", "hh3cIssuUpgradeResultIndex"),
)
if mibBuilder.loadTexts:
    hh3cIssuUpgradeResultEntry.setStatus("current")


class _Hh3cIssuUpgradeResultIndex_Type(Integer32):
    """Custom type hh3cIssuUpgradeResultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cIssuUpgradeResultIndex_Type.__name__ = "Integer32"
_Hh3cIssuUpgradeResultIndex_Object = MibTableColumn
hh3cIssuUpgradeResultIndex = _Hh3cIssuUpgradeResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 2, 3, 1, 1),
    _Hh3cIssuUpgradeResultIndex_Type()
)
hh3cIssuUpgradeResultIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIssuUpgradeResultIndex.setStatus("current")


class _Hh3cIssuUpgradeDeviceChassisID_Type(Integer32):
    """Custom type hh3cIssuUpgradeDeviceChassisID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cIssuUpgradeDeviceChassisID_Type.__name__ = "Integer32"
_Hh3cIssuUpgradeDeviceChassisID_Object = MibTableColumn
hh3cIssuUpgradeDeviceChassisID = _Hh3cIssuUpgradeDeviceChassisID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 2, 3, 1, 2),
    _Hh3cIssuUpgradeDeviceChassisID_Type()
)
hh3cIssuUpgradeDeviceChassisID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIssuUpgradeDeviceChassisID.setStatus("current")


class _Hh3cIssuUpgradeDeviceSlotID_Type(Integer32):
    """Custom type hh3cIssuUpgradeDeviceSlotID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cIssuUpgradeDeviceSlotID_Type.__name__ = "Integer32"
_Hh3cIssuUpgradeDeviceSlotID_Object = MibTableColumn
hh3cIssuUpgradeDeviceSlotID = _Hh3cIssuUpgradeDeviceSlotID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 2, 3, 1, 3),
    _Hh3cIssuUpgradeDeviceSlotID_Type()
)
hh3cIssuUpgradeDeviceSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIssuUpgradeDeviceSlotID.setStatus("current")


class _Hh3cIssuUpgradeDeviceCpuID_Type(Integer32):
    """Custom type hh3cIssuUpgradeDeviceCpuID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hh3cIssuUpgradeDeviceCpuID_Type.__name__ = "Integer32"
_Hh3cIssuUpgradeDeviceCpuID_Object = MibTableColumn
hh3cIssuUpgradeDeviceCpuID = _Hh3cIssuUpgradeDeviceCpuID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 2, 3, 1, 4),
    _Hh3cIssuUpgradeDeviceCpuID_Type()
)
hh3cIssuUpgradeDeviceCpuID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIssuUpgradeDeviceCpuID.setStatus("current")


class _Hh3cIssuUpgradeState_Type(Integer32):
    """Custom type hh3cIssuUpgradeState based on Integer32"""
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


_Hh3cIssuUpgradeState_Type.__name__ = "Integer32"
_Hh3cIssuUpgradeState_Object = MibTableColumn
hh3cIssuUpgradeState = _Hh3cIssuUpgradeState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 2, 3, 1, 5),
    _Hh3cIssuUpgradeState_Type()
)
hh3cIssuUpgradeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIssuUpgradeState.setStatus("current")


class _Hh3cIssuDeviceUpgradeWay_Type(Integer32):
    """Custom type hh3cIssuDeviceUpgradeWay based on Integer32"""
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


_Hh3cIssuDeviceUpgradeWay_Type.__name__ = "Integer32"
_Hh3cIssuDeviceUpgradeWay_Object = MibTableColumn
hh3cIssuDeviceUpgradeWay = _Hh3cIssuDeviceUpgradeWay_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 2, 3, 1, 6),
    _Hh3cIssuDeviceUpgradeWay_Type()
)
hh3cIssuDeviceUpgradeWay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIssuDeviceUpgradeWay.setStatus("current")


class _Hh3cIssuUpgradeDeviceStatus_Type(Integer32):
    """Custom type hh3cIssuUpgradeDeviceStatus based on Integer32"""
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


_Hh3cIssuUpgradeDeviceStatus_Type.__name__ = "Integer32"
_Hh3cIssuUpgradeDeviceStatus_Object = MibTableColumn
hh3cIssuUpgradeDeviceStatus = _Hh3cIssuUpgradeDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 2, 3, 1, 7),
    _Hh3cIssuUpgradeDeviceStatus_Type()
)
hh3cIssuUpgradeDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIssuUpgradeDeviceStatus.setStatus("current")


class _Hh3cIssuUpgradeFailedReason_Type(DisplayString):
    """Custom type hh3cIssuUpgradeFailedReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cIssuUpgradeFailedReason_Type.__name__ = "DisplayString"
_Hh3cIssuUpgradeFailedReason_Object = MibTableColumn
hh3cIssuUpgradeFailedReason = _Hh3cIssuUpgradeFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 133, 1, 2, 3, 1, 8),
    _Hh3cIssuUpgradeFailedReason_Type()
)
hh3cIssuUpgradeFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIssuUpgradeFailedReason.setStatus("current")
_Hh3cIssuUpgradeNotify_ObjectIdentity = ObjectIdentity
hh3cIssuUpgradeNotify = _Hh3cIssuUpgradeNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 133, 2)
)
_Hh3cIssuUpgradeTrapPrefix_ObjectIdentity = ObjectIdentity
hh3cIssuUpgradeTrapPrefix = _Hh3cIssuUpgradeTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 133, 2, 0)
)

# Managed Objects groups


# Notification objects

hh3cIssuUpgradeOpCompletionNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 133, 2, 0, 1)
)
hh3cIssuUpgradeOpCompletionNotify.setObjects(
      *(("HH3C-ISSU-MIB", "hh3cIssuOpType"),
        ("HH3C-ISSU-MIB", "hh3cIssuOpStatus"),
        ("HH3C-ISSU-MIB", "hh3cIssuFailedReason"),
        ("HH3C-ISSU-MIB", "hh3cIssuOpTimeCompleted"))
)
if mibBuilder.loadTexts:
    hh3cIssuUpgradeOpCompletionNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-ISSU-MIB",
    **{"hh3cIssuUpgrade": hh3cIssuUpgrade,
       "hh3cIssuUpgradeMibObjects": hh3cIssuUpgradeMibObjects,
       "hh3cIssuUpgradeGroup": hh3cIssuUpgradeGroup,
       "hh3cIssuUpgradeImageTable": hh3cIssuUpgradeImageTable,
       "hh3cIssuUpgradeImageEntry": hh3cIssuUpgradeImageEntry,
       "hh3cIssuUpgradeImageIndex": hh3cIssuUpgradeImageIndex,
       "hh3cIssuUpgradeImageType": hh3cIssuUpgradeImageType,
       "hh3cIssuUpgradeImageURL": hh3cIssuUpgradeImageURL,
       "hh3cIssuUpgradeImageRowStatus": hh3cIssuUpgradeImageRowStatus,
       "hh3cIssuOp": hh3cIssuOp,
       "hh3cIssuOpType": hh3cIssuOpType,
       "hh3cIssuImageFileOverwrite": hh3cIssuImageFileOverwrite,
       "hh3cIssuOpTrapEnable": hh3cIssuOpTrapEnable,
       "hh3cIssuOpStatus": hh3cIssuOpStatus,
       "hh3cIssuFailedReason": hh3cIssuFailedReason,
       "hh3cIssuOpTimeCompleted": hh3cIssuOpTimeCompleted,
       "hh3cIssuLastOpType": hh3cIssuLastOpType,
       "hh3cIssuLastOpStatus": hh3cIssuLastOpStatus,
       "hh3cIssuLastOpFailedReason": hh3cIssuLastOpFailedReason,
       "hh3cIssuLastOpTimeCompleted": hh3cIssuLastOpTimeCompleted,
       "hh3cIssuUpgradeResultGroup": hh3cIssuUpgradeResultGroup,
       "hh3cIssuCompatibleResult": hh3cIssuCompatibleResult,
       "hh3cIssuCompatibleResultStatus": hh3cIssuCompatibleResultStatus,
       "hh3cIssuCompatibleResultFailedReason": hh3cIssuCompatibleResultFailedReason,
       "hh3cIssuTestResultTable": hh3cIssuTestResultTable,
       "hh3cIssuTestResultEntry": hh3cIssuTestResultEntry,
       "hh3cIssuTestResultIndex": hh3cIssuTestResultIndex,
       "hh3cIssuTestDeviceChassisID": hh3cIssuTestDeviceChassisID,
       "hh3cIssuTestDeviceSlotID": hh3cIssuTestDeviceSlotID,
       "hh3cIssuTestDeviceCpuID": hh3cIssuTestDeviceCpuID,
       "hh3cIssuTestDeviceUpgradeWay": hh3cIssuTestDeviceUpgradeWay,
       "hh3cIssuUpgradeResultTable": hh3cIssuUpgradeResultTable,
       "hh3cIssuUpgradeResultEntry": hh3cIssuUpgradeResultEntry,
       "hh3cIssuUpgradeResultIndex": hh3cIssuUpgradeResultIndex,
       "hh3cIssuUpgradeDeviceChassisID": hh3cIssuUpgradeDeviceChassisID,
       "hh3cIssuUpgradeDeviceSlotID": hh3cIssuUpgradeDeviceSlotID,
       "hh3cIssuUpgradeDeviceCpuID": hh3cIssuUpgradeDeviceCpuID,
       "hh3cIssuUpgradeState": hh3cIssuUpgradeState,
       "hh3cIssuDeviceUpgradeWay": hh3cIssuDeviceUpgradeWay,
       "hh3cIssuUpgradeDeviceStatus": hh3cIssuUpgradeDeviceStatus,
       "hh3cIssuUpgradeFailedReason": hh3cIssuUpgradeFailedReason,
       "hh3cIssuUpgradeNotify": hh3cIssuUpgradeNotify,
       "hh3cIssuUpgradeTrapPrefix": hh3cIssuUpgradeTrapPrefix,
       "hh3cIssuUpgradeOpCompletionNotify": hh3cIssuUpgradeOpCompletionNotify}
)
