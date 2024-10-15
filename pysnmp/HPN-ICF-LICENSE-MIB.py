# SNMP MIB module (HPN-ICF-LICENSE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-LICENSE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:47 2024
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

(PhysicalIndex,
 PhysicalIndexOrZero) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex",
    "PhysicalIndexOrZero")

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpnicfLicense = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145)
)
hpnicfLicense.setRevisions(
        ("2013-09-18 10:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfLicenseScalarObjects_ObjectIdentity = ObjectIdentity
hpnicfLicenseScalarObjects = _HpnicfLicenseScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 1)
)


class _HpnicfLicenseNotifyEnable_Type(TruthValue):
    """Custom type hpnicfLicenseNotifyEnable based on TruthValue"""


_HpnicfLicenseNotifyEnable_Object = MibScalar
hpnicfLicenseNotifyEnable = _HpnicfLicenseNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 1, 1),
    _HpnicfLicenseNotifyEnable_Type()
)
hpnicfLicenseNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfLicenseNotifyEnable.setStatus("current")


class _HpnicfLicenseOpEntryMaxNum_Type(Unsigned32):
    """Custom type hpnicfLicenseOpEntryMaxNum based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_HpnicfLicenseOpEntryMaxNum_Type.__name__ = "Unsigned32"
_HpnicfLicenseOpEntryMaxNum_Object = MibScalar
hpnicfLicenseOpEntryMaxNum = _HpnicfLicenseOpEntryMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 1, 2),
    _HpnicfLicenseOpEntryMaxNum_Type()
)
hpnicfLicenseOpEntryMaxNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfLicenseOpEntryMaxNum.setStatus("current")
_HpnicfLicenseNextFreeOpIndex_Type = Unsigned32
_HpnicfLicenseNextFreeOpIndex_Object = MibScalar
hpnicfLicenseNextFreeOpIndex = _HpnicfLicenseNextFreeOpIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 1, 3),
    _HpnicfLicenseNextFreeOpIndex_Type()
)
hpnicfLicenseNextFreeOpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLicenseNextFreeOpIndex.setStatus("current")
_HpnicfLicenseTables_ObjectIdentity = ObjectIdentity
hpnicfLicenseTables = _HpnicfLicenseTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 2)
)
_HpnicfLicenseDevInfoTable_Object = MibTable
hpnicfLicenseDevInfoTable = _HpnicfLicenseDevInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfLicenseDevInfoTable.setStatus("current")
_HpnicfLicenseDevInfoEntry_Object = MibTableRow
hpnicfLicenseDevInfoEntry = _HpnicfLicenseDevInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 2, 1, 1)
)
hpnicfLicenseDevInfoEntry.setIndexNames(
    (0, "HPN-ICF-LICENSE-MIB", "hpnicfLicensePhysicalIndex"),
)
if mibBuilder.loadTexts:
    hpnicfLicenseDevInfoEntry.setStatus("current")
_HpnicfLicensePhysicalIndex_Type = PhysicalIndex
_HpnicfLicensePhysicalIndex_Object = MibTableColumn
hpnicfLicensePhysicalIndex = _HpnicfLicensePhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 2, 1, 1, 1),
    _HpnicfLicensePhysicalIndex_Type()
)
hpnicfLicensePhysicalIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfLicensePhysicalIndex.setStatus("current")


class _HpnicfLicenseSN_Type(SnmpAdminString):
    """Custom type hpnicfLicenseSN based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfLicenseSN_Type.__name__ = "SnmpAdminString"
_HpnicfLicenseSN_Object = MibTableColumn
hpnicfLicenseSN = _HpnicfLicenseSN_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 2, 1, 1, 2),
    _HpnicfLicenseSN_Type()
)
hpnicfLicenseSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLicenseSN.setStatus("current")


class _HpnicfLicenseDeviceIDType_Type(Integer32):
    """Custom type hpnicfLicenseDeviceIDType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("file", 3),
          ("invalid", 1),
          ("keyString", 2))
    )


_HpnicfLicenseDeviceIDType_Type.__name__ = "Integer32"
_HpnicfLicenseDeviceIDType_Object = MibTableColumn
hpnicfLicenseDeviceIDType = _HpnicfLicenseDeviceIDType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 2, 1, 1, 3),
    _HpnicfLicenseDeviceIDType_Type()
)
hpnicfLicenseDeviceIDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLicenseDeviceIDType.setStatus("current")


class _HpnicfLicenseDeviceID_Type(SnmpAdminString):
    """Custom type hpnicfLicenseDeviceID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfLicenseDeviceID_Type.__name__ = "SnmpAdminString"
_HpnicfLicenseDeviceID_Object = MibTableColumn
hpnicfLicenseDeviceID = _HpnicfLicenseDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 2, 1, 1, 4),
    _HpnicfLicenseDeviceID_Type()
)
hpnicfLicenseDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLicenseDeviceID.setStatus("current")


class _HpnicfLicenseHardwareInfo_Type(SnmpAdminString):
    """Custom type hpnicfLicenseHardwareInfo based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfLicenseHardwareInfo_Type.__name__ = "SnmpAdminString"
_HpnicfLicenseHardwareInfo_Object = MibTableColumn
hpnicfLicenseHardwareInfo = _HpnicfLicenseHardwareInfo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 2, 1, 1, 5),
    _HpnicfLicenseHardwareInfo_Type()
)
hpnicfLicenseHardwareInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLicenseHardwareInfo.setStatus("current")
_HpnicfLicenseMaxNum_Type = Unsigned32
_HpnicfLicenseMaxNum_Object = MibTableColumn
hpnicfLicenseMaxNum = _HpnicfLicenseMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 2, 1, 1, 6),
    _HpnicfLicenseMaxNum_Type()
)
hpnicfLicenseMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLicenseMaxNum.setStatus("current")
_HpnicfLicenseUsedNum_Type = Unsigned32
_HpnicfLicenseUsedNum_Object = MibTableColumn
hpnicfLicenseUsedNum = _HpnicfLicenseUsedNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 2, 1, 1, 7),
    _HpnicfLicenseUsedNum_Type()
)
hpnicfLicenseUsedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLicenseUsedNum.setStatus("current")
_HpnicfLicenseRecyclableNum_Type = Unsigned32
_HpnicfLicenseRecyclableNum_Object = MibTableColumn
hpnicfLicenseRecyclableNum = _HpnicfLicenseRecyclableNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 2, 1, 1, 8),
    _HpnicfLicenseRecyclableNum_Type()
)
hpnicfLicenseRecyclableNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLicenseRecyclableNum.setStatus("current")


class _HpnicfLicenseInstallType_Type(Integer32):
    """Custom type hpnicfLicenseInstallType based on Integer32"""
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
        *(("installInCPU", 4),
          ("installInChassis", 2),
          ("installInSlot", 3),
          ("invalid", 1))
    )


_HpnicfLicenseInstallType_Type.__name__ = "Integer32"
_HpnicfLicenseInstallType_Object = MibTableColumn
hpnicfLicenseInstallType = _HpnicfLicenseInstallType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 2, 1, 1, 9),
    _HpnicfLicenseInstallType_Type()
)
hpnicfLicenseInstallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLicenseInstallType.setStatus("current")


class _HpnicfLicenseFileStoragePath_Type(SnmpAdminString):
    """Custom type hpnicfLicenseFileStoragePath based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfLicenseFileStoragePath_Type.__name__ = "SnmpAdminString"
_HpnicfLicenseFileStoragePath_Object = MibTableColumn
hpnicfLicenseFileStoragePath = _HpnicfLicenseFileStoragePath_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 2, 1, 1, 10),
    _HpnicfLicenseFileStoragePath_Type()
)
hpnicfLicenseFileStoragePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLicenseFileStoragePath.setStatus("current")
_HpnicfLicenseGeneralTable_Object = MibTable
hpnicfLicenseGeneralTable = _HpnicfLicenseGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfLicenseGeneralTable.setStatus("current")
_HpnicfLicenseGeneralEntry_Object = MibTableRow
hpnicfLicenseGeneralEntry = _HpnicfLicenseGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 2, 2, 1)
)
hpnicfLicenseGeneralEntry.setIndexNames(
    (0, "HPN-ICF-LICENSE-MIB", "hpnicfLicensePhysicalIndex"),
    (0, "HPN-ICF-LICENSE-MIB", "hpnicfLicenseIndex"),
)
if mibBuilder.loadTexts:
    hpnicfLicenseGeneralEntry.setStatus("current")
_HpnicfLicenseIndex_Type = Unsigned32
_HpnicfLicenseIndex_Object = MibTableColumn
hpnicfLicenseIndex = _HpnicfLicenseIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 2, 2, 1, 1),
    _HpnicfLicenseIndex_Type()
)
hpnicfLicenseIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfLicenseIndex.setStatus("current")


class _HpnicfLicenseFeature_Type(SnmpAdminString):
    """Custom type hpnicfLicenseFeature based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_HpnicfLicenseFeature_Type.__name__ = "SnmpAdminString"
_HpnicfLicenseFeature_Object = MibTableColumn
hpnicfLicenseFeature = _HpnicfLicenseFeature_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 2, 2, 1, 2),
    _HpnicfLicenseFeature_Type()
)
hpnicfLicenseFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLicenseFeature.setStatus("current")


class _HpnicfLicenseProductDescr_Type(OctetString):
    """Custom type hpnicfLicenseProductDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_HpnicfLicenseProductDescr_Type.__name__ = "OctetString"
_HpnicfLicenseProductDescr_Object = MibTableColumn
hpnicfLicenseProductDescr = _HpnicfLicenseProductDescr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 2, 2, 1, 3),
    _HpnicfLicenseProductDescr_Type()
)
hpnicfLicenseProductDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLicenseProductDescr.setStatus("current")


class _HpnicfLicenseFileDescr_Type(SnmpAdminString):
    """Custom type hpnicfLicenseFileDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_HpnicfLicenseFileDescr_Type.__name__ = "SnmpAdminString"
_HpnicfLicenseFileDescr_Object = MibTableColumn
hpnicfLicenseFileDescr = _HpnicfLicenseFileDescr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 2, 2, 1, 4),
    _HpnicfLicenseFileDescr_Type()
)
hpnicfLicenseFileDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLicenseFileDescr.setStatus("current")


class _HpnicfLicenseState_Type(Integer32):
    """Custom type hpnicfLicenseState based on Integer32"""
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
        *(("expired", 4),
          ("inuse", 2),
          ("invalid", 1),
          ("uninstalled", 5),
          ("unusable", 6),
          ("usable", 3))
    )


_HpnicfLicenseState_Type.__name__ = "Integer32"
_HpnicfLicenseState_Object = MibTableColumn
hpnicfLicenseState = _HpnicfLicenseState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 2, 2, 1, 5),
    _HpnicfLicenseState_Type()
)
hpnicfLicenseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLicenseState.setStatus("current")


class _HpnicfLicenseActivationFile_Type(SnmpAdminString):
    """Custom type hpnicfLicenseActivationFile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfLicenseActivationFile_Type.__name__ = "SnmpAdminString"
_HpnicfLicenseActivationFile_Object = MibTableColumn
hpnicfLicenseActivationFile = _HpnicfLicenseActivationFile_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 2, 2, 1, 6),
    _HpnicfLicenseActivationFile_Type()
)
hpnicfLicenseActivationFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLicenseActivationFile.setStatus("current")


class _HpnicfLicenseActivationKey_Type(SnmpAdminString):
    """Custom type hpnicfLicenseActivationKey based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfLicenseActivationKey_Type.__name__ = "SnmpAdminString"
_HpnicfLicenseActivationKey_Object = MibTableColumn
hpnicfLicenseActivationKey = _HpnicfLicenseActivationKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 2, 2, 1, 7),
    _HpnicfLicenseActivationKey_Type()
)
hpnicfLicenseActivationKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLicenseActivationKey.setStatus("current")


class _HpnicfLicenseLicenseKey_Type(SnmpAdminString):
    """Custom type hpnicfLicenseLicenseKey based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfLicenseLicenseKey_Type.__name__ = "SnmpAdminString"
_HpnicfLicenseLicenseKey_Object = MibTableColumn
hpnicfLicenseLicenseKey = _HpnicfLicenseLicenseKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 2, 2, 1, 8),
    _HpnicfLicenseLicenseKey_Type()
)
hpnicfLicenseLicenseKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLicenseLicenseKey.setStatus("current")


class _HpnicfLicenseUninstActivationFile_Type(SnmpAdminString):
    """Custom type hpnicfLicenseUninstActivationFile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfLicenseUninstActivationFile_Type.__name__ = "SnmpAdminString"
_HpnicfLicenseUninstActivationFile_Object = MibTableColumn
hpnicfLicenseUninstActivationFile = _HpnicfLicenseUninstActivationFile_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 2, 2, 1, 9),
    _HpnicfLicenseUninstActivationFile_Type()
)
hpnicfLicenseUninstActivationFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLicenseUninstActivationFile.setStatus("current")


class _HpnicfLicenseUninstActivationKey_Type(SnmpAdminString):
    """Custom type hpnicfLicenseUninstActivationKey based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfLicenseUninstActivationKey_Type.__name__ = "SnmpAdminString"
_HpnicfLicenseUninstActivationKey_Object = MibTableColumn
hpnicfLicenseUninstActivationKey = _HpnicfLicenseUninstActivationKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 2, 2, 1, 10),
    _HpnicfLicenseUninstActivationKey_Type()
)
hpnicfLicenseUninstActivationKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLicenseUninstActivationKey.setStatus("current")


class _HpnicfLicenseType_Type(Integer32):
    """Custom type hpnicfLicenseType based on Integer32"""
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
        *(("countRestricted", 7),
          ("dateRestricted", 5),
          ("daysRestricted", 3),
          ("permanent", 2),
          ("trialCountRestricted", 8),
          ("trialDateRestricted", 6),
          ("trialDaysRestricted", 4),
          ("unknown", 1))
    )


_HpnicfLicenseType_Type.__name__ = "Integer32"
_HpnicfLicenseType_Object = MibTableColumn
hpnicfLicenseType = _HpnicfLicenseType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 2, 2, 1, 11),
    _HpnicfLicenseType_Type()
)
hpnicfLicenseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLicenseType.setStatus("current")
_HpnicfLicenseInstalledTime_Type = DateAndTime
_HpnicfLicenseInstalledTime_Object = MibTableColumn
hpnicfLicenseInstalledTime = _HpnicfLicenseInstalledTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 2, 2, 1, 12),
    _HpnicfLicenseInstalledTime_Type()
)
hpnicfLicenseInstalledTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLicenseInstalledTime.setStatus("current")
_HpnicfLicenseUninstalledTime_Type = DateAndTime
_HpnicfLicenseUninstalledTime_Object = MibTableColumn
hpnicfLicenseUninstalledTime = _HpnicfLicenseUninstalledTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 2, 2, 1, 13),
    _HpnicfLicenseUninstalledTime_Type()
)
hpnicfLicenseUninstalledTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLicenseUninstalledTime.setStatus("current")
_HpnicfLicenseDaysLeft_Type = Unsigned32
_HpnicfLicenseDaysLeft_Object = MibTableColumn
hpnicfLicenseDaysLeft = _HpnicfLicenseDaysLeft_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 2, 2, 1, 14),
    _HpnicfLicenseDaysLeft_Type()
)
hpnicfLicenseDaysLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLicenseDaysLeft.setStatus("current")
_HpnicfLicenseValidityStart_Type = DateAndTime
_HpnicfLicenseValidityStart_Object = MibTableColumn
hpnicfLicenseValidityStart = _HpnicfLicenseValidityStart_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 2, 2, 1, 15),
    _HpnicfLicenseValidityStart_Type()
)
hpnicfLicenseValidityStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLicenseValidityStart.setStatus("current")
_HpnicfLicenseValidityEnd_Type = DateAndTime
_HpnicfLicenseValidityEnd_Object = MibTableColumn
hpnicfLicenseValidityEnd = _HpnicfLicenseValidityEnd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 2, 2, 1, 16),
    _HpnicfLicenseValidityEnd_Type()
)
hpnicfLicenseValidityEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLicenseValidityEnd.setStatus("current")
_HpnicfLicenseExpiredDays_Type = Unsigned32
_HpnicfLicenseExpiredDays_Object = MibTableColumn
hpnicfLicenseExpiredDays = _HpnicfLicenseExpiredDays_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 2, 2, 1, 17),
    _HpnicfLicenseExpiredDays_Type()
)
hpnicfLicenseExpiredDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLicenseExpiredDays.setStatus("current")
_HpnicfLicenseCount_Type = Unsigned32
_HpnicfLicenseCount_Object = MibTableColumn
hpnicfLicenseCount = _HpnicfLicenseCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 2, 2, 1, 18),
    _HpnicfLicenseCount_Type()
)
hpnicfLicenseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLicenseCount.setStatus("current")
_HpnicfLicenseFeatureTable_Object = MibTable
hpnicfLicenseFeatureTable = _HpnicfLicenseFeatureTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 2, 3)
)
if mibBuilder.loadTexts:
    hpnicfLicenseFeatureTable.setStatus("current")
_HpnicfLicenseFeatureEntry_Object = MibTableRow
hpnicfLicenseFeatureEntry = _HpnicfLicenseFeatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 2, 3, 1)
)
hpnicfLicenseFeatureEntry.setIndexNames(
    (0, "HPN-ICF-LICENSE-MIB", "hpnicfLicensePhysicalIndex"),
    (1, "HPN-ICF-LICENSE-MIB", "hpnicfLicenseFeatureName"),
)
if mibBuilder.loadTexts:
    hpnicfLicenseFeatureEntry.setStatus("current")


class _HpnicfLicenseFeatureName_Type(SnmpAdminString):
    """Custom type hpnicfLicenseFeatureName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HpnicfLicenseFeatureName_Type.__name__ = "SnmpAdminString"
_HpnicfLicenseFeatureName_Object = MibTableColumn
hpnicfLicenseFeatureName = _HpnicfLicenseFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 2, 3, 1, 1),
    _HpnicfLicenseFeatureName_Type()
)
hpnicfLicenseFeatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLicenseFeatureName.setStatus("current")


class _HpnicfLicenseFeatureState_Type(Integer32):
    """Custom type hpnicfLicenseFeatureState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("formalLicense", 3),
          ("notLicensed", 1),
          ("trialLicense", 2))
    )


_HpnicfLicenseFeatureState_Type.__name__ = "Integer32"
_HpnicfLicenseFeatureState_Object = MibTableColumn
hpnicfLicenseFeatureState = _HpnicfLicenseFeatureState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 2, 3, 1, 2),
    _HpnicfLicenseFeatureState_Type()
)
hpnicfLicenseFeatureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLicenseFeatureState.setStatus("current")
_HpnicfLicenseOpTable_Object = MibTable
hpnicfLicenseOpTable = _HpnicfLicenseOpTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 2, 4)
)
if mibBuilder.loadTexts:
    hpnicfLicenseOpTable.setStatus("current")
_HpnicfLicenseOpEntry_Object = MibTableRow
hpnicfLicenseOpEntry = _HpnicfLicenseOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 2, 4, 1)
)
hpnicfLicenseOpEntry.setIndexNames(
    (0, "HPN-ICF-LICENSE-MIB", "hpnicfLicenseOpIndex"),
)
if mibBuilder.loadTexts:
    hpnicfLicenseOpEntry.setStatus("current")
_HpnicfLicenseOpIndex_Type = Unsigned32
_HpnicfLicenseOpIndex_Object = MibTableColumn
hpnicfLicenseOpIndex = _HpnicfLicenseOpIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 2, 4, 1, 1),
    _HpnicfLicenseOpIndex_Type()
)
hpnicfLicenseOpIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfLicenseOpIndex.setStatus("current")
_HpnicfLicenseOpPhysicalIndex_Type = PhysicalIndexOrZero
_HpnicfLicenseOpPhysicalIndex_Object = MibTableColumn
hpnicfLicenseOpPhysicalIndex = _HpnicfLicenseOpPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 2, 4, 1, 2),
    _HpnicfLicenseOpPhysicalIndex_Type()
)
hpnicfLicenseOpPhysicalIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfLicenseOpPhysicalIndex.setStatus("current")


class _HpnicfLicenseOpType_Type(Integer32):
    """Custom type hpnicfLicenseOpType based on Integer32"""
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
        *(("compress", 1),
          ("delete", 2),
          ("installActivationFile", 3),
          ("installActivationKey", 4),
          ("installLicenseKey", 5),
          ("uninstallActivationFile", 6),
          ("uninstallActivationKey", 7),
          ("uninstallLicenseKey", 8))
    )


_HpnicfLicenseOpType_Type.__name__ = "Integer32"
_HpnicfLicenseOpType_Object = MibTableColumn
hpnicfLicenseOpType = _HpnicfLicenseOpType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 2, 4, 1, 3),
    _HpnicfLicenseOpType_Type()
)
hpnicfLicenseOpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfLicenseOpType.setStatus("current")


class _HpnicfLicenseOpString_Type(SnmpAdminString):
    """Custom type hpnicfLicenseOpString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfLicenseOpString_Type.__name__ = "SnmpAdminString"
_HpnicfLicenseOpString_Object = MibTableColumn
hpnicfLicenseOpString = _HpnicfLicenseOpString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 2, 4, 1, 4),
    _HpnicfLicenseOpString_Type()
)
hpnicfLicenseOpString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfLicenseOpString.setStatus("current")


class _HpnicfLicenseOpNotifyEnable_Type(TruthValue):
    """Custom type hpnicfLicenseOpNotifyEnable based on TruthValue"""


_HpnicfLicenseOpNotifyEnable_Object = MibTableColumn
hpnicfLicenseOpNotifyEnable = _HpnicfLicenseOpNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 2, 4, 1, 5),
    _HpnicfLicenseOpNotifyEnable_Type()
)
hpnicfLicenseOpNotifyEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfLicenseOpNotifyEnable.setStatus("current")
_HpnicfLicenseOpRowStatus_Type = RowStatus
_HpnicfLicenseOpRowStatus_Object = MibTableColumn
hpnicfLicenseOpRowStatus = _HpnicfLicenseOpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 2, 4, 1, 6),
    _HpnicfLicenseOpRowStatus_Type()
)
hpnicfLicenseOpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfLicenseOpRowStatus.setStatus("current")


class _HpnicfLicenseOpState_Type(Integer32):
    """Custom type hpnicfLicenseOpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("opFailed", 3),
          ("opInProgress", 1),
          ("opSuccessful", 2))
    )


_HpnicfLicenseOpState_Type.__name__ = "Integer32"
_HpnicfLicenseOpState_Object = MibTableColumn
hpnicfLicenseOpState = _HpnicfLicenseOpState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 2, 4, 1, 7),
    _HpnicfLicenseOpState_Type()
)
hpnicfLicenseOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLicenseOpState.setStatus("current")


class _HpnicfLicenseOpFailedReason_Type(SnmpAdminString):
    """Custom type hpnicfLicenseOpFailedReason based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfLicenseOpFailedReason_Type.__name__ = "SnmpAdminString"
_HpnicfLicenseOpFailedReason_Object = MibTableColumn
hpnicfLicenseOpFailedReason = _HpnicfLicenseOpFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 2, 4, 1, 8),
    _HpnicfLicenseOpFailedReason_Type()
)
hpnicfLicenseOpFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLicenseOpFailedReason.setStatus("current")
_HpnicfLicenseOpEndTime_Type = TimeTicks
_HpnicfLicenseOpEndTime_Object = MibTableColumn
hpnicfLicenseOpEndTime = _HpnicfLicenseOpEndTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 2, 4, 1, 9),
    _HpnicfLicenseOpEndTime_Type()
)
hpnicfLicenseOpEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLicenseOpEndTime.setStatus("current")
_HpnicfLicenseNotifications_ObjectIdentity = ObjectIdentity
hpnicfLicenseNotifications = _HpnicfLicenseNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 3)
)
_HpnicfLicenseNotificationPrefix_ObjectIdentity = ObjectIdentity
hpnicfLicenseNotificationPrefix = _HpnicfLicenseNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 3, 0)
)
_HpnicfLicenseNotificationBindings_ObjectIdentity = ObjectIdentity
hpnicfLicenseNotificationBindings = _HpnicfLicenseNotificationBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 3, 1)
)
_HpnicfLicenseBindValidityPeriodRemaining_Type = Unsigned32
_HpnicfLicenseBindValidityPeriodRemaining_Object = MibScalar
hpnicfLicenseBindValidityPeriodRemaining = _HpnicfLicenseBindValidityPeriodRemaining_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 3, 1, 1),
    _HpnicfLicenseBindValidityPeriodRemaining_Type()
)
hpnicfLicenseBindValidityPeriodRemaining.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfLicenseBindValidityPeriodRemaining.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfLicenseBindValidityPeriodRemaining.setUnits("days")

# Managed Objects groups


# Notification objects

hpnicfLicenseOpCompletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 3, 0, 1)
)
hpnicfLicenseOpCompletion.setObjects(
      *(("HPN-ICF-LICENSE-MIB", "hpnicfLicenseOpIndex"),
        ("HPN-ICF-LICENSE-MIB", "hpnicfLicenseOpPhysicalIndex"),
        ("HPN-ICF-LICENSE-MIB", "hpnicfLicenseOpType"),
        ("HPN-ICF-LICENSE-MIB", "hpnicfLicenseOpString"),
        ("HPN-ICF-LICENSE-MIB", "hpnicfLicenseOpState"),
        ("HPN-ICF-LICENSE-MIB", "hpnicfLicenseOpFailedReason"))
)
if mibBuilder.loadTexts:
    hpnicfLicenseOpCompletion.setStatus(
        "current"
    )

hpnicfLicenseActivationFileLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 3, 0, 2)
)
hpnicfLicenseActivationFileLost.setObjects(
      *(("HPN-ICF-LICENSE-MIB", "hpnicfLicensePhysicalIndex"),
        ("HPN-ICF-LICENSE-MIB", "hpnicfLicenseActivationFile"))
)
if mibBuilder.loadTexts:
    hpnicfLicenseActivationFileLost.setStatus(
        "current"
    )

hpnicfLicenseActivationFileRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 3, 0, 3)
)
hpnicfLicenseActivationFileRestored.setObjects(
      *(("HPN-ICF-LICENSE-MIB", "hpnicfLicensePhysicalIndex"),
        ("HPN-ICF-LICENSE-MIB", "hpnicfLicenseActivationFile"))
)
if mibBuilder.loadTexts:
    hpnicfLicenseActivationFileRestored.setStatus(
        "current"
    )

hpnicfLicenseExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 3, 0, 4)
)
hpnicfLicenseExpired.setObjects(
      *(("HPN-ICF-LICENSE-MIB", "hpnicfLicenseFeatureName"),
        ("HPN-ICF-LICENSE-MIB", "hpnicfLicenseFeatureState"))
)
if mibBuilder.loadTexts:
    hpnicfLicenseExpired.setStatus(
        "current"
    )

hpnicfLicenseExpireWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145, 3, 0, 5)
)
hpnicfLicenseExpireWarning.setObjects(
      *(("HPN-ICF-LICENSE-MIB", "hpnicfLicenseFeatureName"),
        ("HPN-ICF-LICENSE-MIB", "hpnicfLicenseFeatureState"),
        ("HPN-ICF-LICENSE-MIB", "hpnicfLicenseBindValidityPeriodRemaining"))
)
if mibBuilder.loadTexts:
    hpnicfLicenseExpireWarning.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-LICENSE-MIB",
    **{"hpnicfLicense": hpnicfLicense,
       "hpnicfLicenseScalarObjects": hpnicfLicenseScalarObjects,
       "hpnicfLicenseNotifyEnable": hpnicfLicenseNotifyEnable,
       "hpnicfLicenseOpEntryMaxNum": hpnicfLicenseOpEntryMaxNum,
       "hpnicfLicenseNextFreeOpIndex": hpnicfLicenseNextFreeOpIndex,
       "hpnicfLicenseTables": hpnicfLicenseTables,
       "hpnicfLicenseDevInfoTable": hpnicfLicenseDevInfoTable,
       "hpnicfLicenseDevInfoEntry": hpnicfLicenseDevInfoEntry,
       "hpnicfLicensePhysicalIndex": hpnicfLicensePhysicalIndex,
       "hpnicfLicenseSN": hpnicfLicenseSN,
       "hpnicfLicenseDeviceIDType": hpnicfLicenseDeviceIDType,
       "hpnicfLicenseDeviceID": hpnicfLicenseDeviceID,
       "hpnicfLicenseHardwareInfo": hpnicfLicenseHardwareInfo,
       "hpnicfLicenseMaxNum": hpnicfLicenseMaxNum,
       "hpnicfLicenseUsedNum": hpnicfLicenseUsedNum,
       "hpnicfLicenseRecyclableNum": hpnicfLicenseRecyclableNum,
       "hpnicfLicenseInstallType": hpnicfLicenseInstallType,
       "hpnicfLicenseFileStoragePath": hpnicfLicenseFileStoragePath,
       "hpnicfLicenseGeneralTable": hpnicfLicenseGeneralTable,
       "hpnicfLicenseGeneralEntry": hpnicfLicenseGeneralEntry,
       "hpnicfLicenseIndex": hpnicfLicenseIndex,
       "hpnicfLicenseFeature": hpnicfLicenseFeature,
       "hpnicfLicenseProductDescr": hpnicfLicenseProductDescr,
       "hpnicfLicenseFileDescr": hpnicfLicenseFileDescr,
       "hpnicfLicenseState": hpnicfLicenseState,
       "hpnicfLicenseActivationFile": hpnicfLicenseActivationFile,
       "hpnicfLicenseActivationKey": hpnicfLicenseActivationKey,
       "hpnicfLicenseLicenseKey": hpnicfLicenseLicenseKey,
       "hpnicfLicenseUninstActivationFile": hpnicfLicenseUninstActivationFile,
       "hpnicfLicenseUninstActivationKey": hpnicfLicenseUninstActivationKey,
       "hpnicfLicenseType": hpnicfLicenseType,
       "hpnicfLicenseInstalledTime": hpnicfLicenseInstalledTime,
       "hpnicfLicenseUninstalledTime": hpnicfLicenseUninstalledTime,
       "hpnicfLicenseDaysLeft": hpnicfLicenseDaysLeft,
       "hpnicfLicenseValidityStart": hpnicfLicenseValidityStart,
       "hpnicfLicenseValidityEnd": hpnicfLicenseValidityEnd,
       "hpnicfLicenseExpiredDays": hpnicfLicenseExpiredDays,
       "hpnicfLicenseCount": hpnicfLicenseCount,
       "hpnicfLicenseFeatureTable": hpnicfLicenseFeatureTable,
       "hpnicfLicenseFeatureEntry": hpnicfLicenseFeatureEntry,
       "hpnicfLicenseFeatureName": hpnicfLicenseFeatureName,
       "hpnicfLicenseFeatureState": hpnicfLicenseFeatureState,
       "hpnicfLicenseOpTable": hpnicfLicenseOpTable,
       "hpnicfLicenseOpEntry": hpnicfLicenseOpEntry,
       "hpnicfLicenseOpIndex": hpnicfLicenseOpIndex,
       "hpnicfLicenseOpPhysicalIndex": hpnicfLicenseOpPhysicalIndex,
       "hpnicfLicenseOpType": hpnicfLicenseOpType,
       "hpnicfLicenseOpString": hpnicfLicenseOpString,
       "hpnicfLicenseOpNotifyEnable": hpnicfLicenseOpNotifyEnable,
       "hpnicfLicenseOpRowStatus": hpnicfLicenseOpRowStatus,
       "hpnicfLicenseOpState": hpnicfLicenseOpState,
       "hpnicfLicenseOpFailedReason": hpnicfLicenseOpFailedReason,
       "hpnicfLicenseOpEndTime": hpnicfLicenseOpEndTime,
       "hpnicfLicenseNotifications": hpnicfLicenseNotifications,
       "hpnicfLicenseNotificationPrefix": hpnicfLicenseNotificationPrefix,
       "hpnicfLicenseOpCompletion": hpnicfLicenseOpCompletion,
       "hpnicfLicenseActivationFileLost": hpnicfLicenseActivationFileLost,
       "hpnicfLicenseActivationFileRestored": hpnicfLicenseActivationFileRestored,
       "hpnicfLicenseExpired": hpnicfLicenseExpired,
       "hpnicfLicenseExpireWarning": hpnicfLicenseExpireWarning,
       "hpnicfLicenseNotificationBindings": hpnicfLicenseNotificationBindings,
       "hpnicfLicenseBindValidityPeriodRemaining": hpnicfLicenseBindValidityPeriodRemaining}
)
