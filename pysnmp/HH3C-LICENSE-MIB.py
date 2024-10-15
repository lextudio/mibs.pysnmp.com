# SNMP MIB module (HH3C-LICENSE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-LICENSE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:48 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cLicense = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145)
)
hh3cLicense.setRevisions(
        ("2013-09-18 10:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cLicenseScalarObjects_ObjectIdentity = ObjectIdentity
hh3cLicenseScalarObjects = _Hh3cLicenseScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 1)
)


class _Hh3cLicenseNotifyEnable_Type(TruthValue):
    """Custom type hh3cLicenseNotifyEnable based on TruthValue"""


_Hh3cLicenseNotifyEnable_Object = MibScalar
hh3cLicenseNotifyEnable = _Hh3cLicenseNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 1, 1),
    _Hh3cLicenseNotifyEnable_Type()
)
hh3cLicenseNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLicenseNotifyEnable.setStatus("current")


class _Hh3cLicenseOpEntryMaxNum_Type(Unsigned32):
    """Custom type hh3cLicenseOpEntryMaxNum based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_Hh3cLicenseOpEntryMaxNum_Type.__name__ = "Unsigned32"
_Hh3cLicenseOpEntryMaxNum_Object = MibScalar
hh3cLicenseOpEntryMaxNum = _Hh3cLicenseOpEntryMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 1, 2),
    _Hh3cLicenseOpEntryMaxNum_Type()
)
hh3cLicenseOpEntryMaxNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLicenseOpEntryMaxNum.setStatus("current")
_Hh3cLicenseNextFreeOpIndex_Type = Unsigned32
_Hh3cLicenseNextFreeOpIndex_Object = MibScalar
hh3cLicenseNextFreeOpIndex = _Hh3cLicenseNextFreeOpIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 1, 3),
    _Hh3cLicenseNextFreeOpIndex_Type()
)
hh3cLicenseNextFreeOpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLicenseNextFreeOpIndex.setStatus("current")
_Hh3cLicenseTables_ObjectIdentity = ObjectIdentity
hh3cLicenseTables = _Hh3cLicenseTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 2)
)
_Hh3cLicenseDevInfoTable_Object = MibTable
hh3cLicenseDevInfoTable = _Hh3cLicenseDevInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cLicenseDevInfoTable.setStatus("current")
_Hh3cLicenseDevInfoEntry_Object = MibTableRow
hh3cLicenseDevInfoEntry = _Hh3cLicenseDevInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 1, 1)
)
hh3cLicenseDevInfoEntry.setIndexNames(
    (0, "HH3C-LICENSE-MIB", "hh3cLicensePhysicalIndex"),
)
if mibBuilder.loadTexts:
    hh3cLicenseDevInfoEntry.setStatus("current")
_Hh3cLicensePhysicalIndex_Type = PhysicalIndex
_Hh3cLicensePhysicalIndex_Object = MibTableColumn
hh3cLicensePhysicalIndex = _Hh3cLicensePhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 1, 1, 1),
    _Hh3cLicensePhysicalIndex_Type()
)
hh3cLicensePhysicalIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cLicensePhysicalIndex.setStatus("current")


class _Hh3cLicenseSN_Type(SnmpAdminString):
    """Custom type hh3cLicenseSN based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cLicenseSN_Type.__name__ = "SnmpAdminString"
_Hh3cLicenseSN_Object = MibTableColumn
hh3cLicenseSN = _Hh3cLicenseSN_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 1, 1, 2),
    _Hh3cLicenseSN_Type()
)
hh3cLicenseSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLicenseSN.setStatus("current")


class _Hh3cLicenseDeviceIDType_Type(Integer32):
    """Custom type hh3cLicenseDeviceIDType based on Integer32"""
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


_Hh3cLicenseDeviceIDType_Type.__name__ = "Integer32"
_Hh3cLicenseDeviceIDType_Object = MibTableColumn
hh3cLicenseDeviceIDType = _Hh3cLicenseDeviceIDType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 1, 1, 3),
    _Hh3cLicenseDeviceIDType_Type()
)
hh3cLicenseDeviceIDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLicenseDeviceIDType.setStatus("current")


class _Hh3cLicenseDeviceID_Type(SnmpAdminString):
    """Custom type hh3cLicenseDeviceID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cLicenseDeviceID_Type.__name__ = "SnmpAdminString"
_Hh3cLicenseDeviceID_Object = MibTableColumn
hh3cLicenseDeviceID = _Hh3cLicenseDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 1, 1, 4),
    _Hh3cLicenseDeviceID_Type()
)
hh3cLicenseDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLicenseDeviceID.setStatus("current")


class _Hh3cLicenseHardwareInfo_Type(SnmpAdminString):
    """Custom type hh3cLicenseHardwareInfo based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cLicenseHardwareInfo_Type.__name__ = "SnmpAdminString"
_Hh3cLicenseHardwareInfo_Object = MibTableColumn
hh3cLicenseHardwareInfo = _Hh3cLicenseHardwareInfo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 1, 1, 5),
    _Hh3cLicenseHardwareInfo_Type()
)
hh3cLicenseHardwareInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLicenseHardwareInfo.setStatus("current")
_Hh3cLicenseMaxNum_Type = Unsigned32
_Hh3cLicenseMaxNum_Object = MibTableColumn
hh3cLicenseMaxNum = _Hh3cLicenseMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 1, 1, 6),
    _Hh3cLicenseMaxNum_Type()
)
hh3cLicenseMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLicenseMaxNum.setStatus("current")
_Hh3cLicenseUsedNum_Type = Unsigned32
_Hh3cLicenseUsedNum_Object = MibTableColumn
hh3cLicenseUsedNum = _Hh3cLicenseUsedNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 1, 1, 7),
    _Hh3cLicenseUsedNum_Type()
)
hh3cLicenseUsedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLicenseUsedNum.setStatus("current")
_Hh3cLicenseRecyclableNum_Type = Unsigned32
_Hh3cLicenseRecyclableNum_Object = MibTableColumn
hh3cLicenseRecyclableNum = _Hh3cLicenseRecyclableNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 1, 1, 8),
    _Hh3cLicenseRecyclableNum_Type()
)
hh3cLicenseRecyclableNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLicenseRecyclableNum.setStatus("current")


class _Hh3cLicenseInstallType_Type(Integer32):
    """Custom type hh3cLicenseInstallType based on Integer32"""
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


_Hh3cLicenseInstallType_Type.__name__ = "Integer32"
_Hh3cLicenseInstallType_Object = MibTableColumn
hh3cLicenseInstallType = _Hh3cLicenseInstallType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 1, 1, 9),
    _Hh3cLicenseInstallType_Type()
)
hh3cLicenseInstallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLicenseInstallType.setStatus("current")


class _Hh3cLicenseFileStoragePath_Type(SnmpAdminString):
    """Custom type hh3cLicenseFileStoragePath based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cLicenseFileStoragePath_Type.__name__ = "SnmpAdminString"
_Hh3cLicenseFileStoragePath_Object = MibTableColumn
hh3cLicenseFileStoragePath = _Hh3cLicenseFileStoragePath_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 1, 1, 10),
    _Hh3cLicenseFileStoragePath_Type()
)
hh3cLicenseFileStoragePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLicenseFileStoragePath.setStatus("current")
_Hh3cLicenseGeneralTable_Object = MibTable
hh3cLicenseGeneralTable = _Hh3cLicenseGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cLicenseGeneralTable.setStatus("current")
_Hh3cLicenseGeneralEntry_Object = MibTableRow
hh3cLicenseGeneralEntry = _Hh3cLicenseGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 2, 1)
)
hh3cLicenseGeneralEntry.setIndexNames(
    (0, "HH3C-LICENSE-MIB", "hh3cLicensePhysicalIndex"),
    (0, "HH3C-LICENSE-MIB", "hh3cLicenseIndex"),
)
if mibBuilder.loadTexts:
    hh3cLicenseGeneralEntry.setStatus("current")
_Hh3cLicenseIndex_Type = Unsigned32
_Hh3cLicenseIndex_Object = MibTableColumn
hh3cLicenseIndex = _Hh3cLicenseIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 2, 1, 1),
    _Hh3cLicenseIndex_Type()
)
hh3cLicenseIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cLicenseIndex.setStatus("current")


class _Hh3cLicenseFeature_Type(SnmpAdminString):
    """Custom type hh3cLicenseFeature based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_Hh3cLicenseFeature_Type.__name__ = "SnmpAdminString"
_Hh3cLicenseFeature_Object = MibTableColumn
hh3cLicenseFeature = _Hh3cLicenseFeature_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 2, 1, 2),
    _Hh3cLicenseFeature_Type()
)
hh3cLicenseFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLicenseFeature.setStatus("current")


class _Hh3cLicenseProductDescr_Type(OctetString):
    """Custom type hh3cLicenseProductDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_Hh3cLicenseProductDescr_Type.__name__ = "OctetString"
_Hh3cLicenseProductDescr_Object = MibTableColumn
hh3cLicenseProductDescr = _Hh3cLicenseProductDescr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 2, 1, 3),
    _Hh3cLicenseProductDescr_Type()
)
hh3cLicenseProductDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLicenseProductDescr.setStatus("current")


class _Hh3cLicenseFileDescr_Type(SnmpAdminString):
    """Custom type hh3cLicenseFileDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_Hh3cLicenseFileDescr_Type.__name__ = "SnmpAdminString"
_Hh3cLicenseFileDescr_Object = MibTableColumn
hh3cLicenseFileDescr = _Hh3cLicenseFileDescr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 2, 1, 4),
    _Hh3cLicenseFileDescr_Type()
)
hh3cLicenseFileDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLicenseFileDescr.setStatus("current")


class _Hh3cLicenseState_Type(Integer32):
    """Custom type hh3cLicenseState based on Integer32"""
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


_Hh3cLicenseState_Type.__name__ = "Integer32"
_Hh3cLicenseState_Object = MibTableColumn
hh3cLicenseState = _Hh3cLicenseState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 2, 1, 5),
    _Hh3cLicenseState_Type()
)
hh3cLicenseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLicenseState.setStatus("current")


class _Hh3cLicenseActivationFile_Type(SnmpAdminString):
    """Custom type hh3cLicenseActivationFile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cLicenseActivationFile_Type.__name__ = "SnmpAdminString"
_Hh3cLicenseActivationFile_Object = MibTableColumn
hh3cLicenseActivationFile = _Hh3cLicenseActivationFile_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 2, 1, 6),
    _Hh3cLicenseActivationFile_Type()
)
hh3cLicenseActivationFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLicenseActivationFile.setStatus("current")


class _Hh3cLicenseActivationKey_Type(SnmpAdminString):
    """Custom type hh3cLicenseActivationKey based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cLicenseActivationKey_Type.__name__ = "SnmpAdminString"
_Hh3cLicenseActivationKey_Object = MibTableColumn
hh3cLicenseActivationKey = _Hh3cLicenseActivationKey_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 2, 1, 7),
    _Hh3cLicenseActivationKey_Type()
)
hh3cLicenseActivationKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLicenseActivationKey.setStatus("current")


class _Hh3cLicenseLicenseKey_Type(SnmpAdminString):
    """Custom type hh3cLicenseLicenseKey based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cLicenseLicenseKey_Type.__name__ = "SnmpAdminString"
_Hh3cLicenseLicenseKey_Object = MibTableColumn
hh3cLicenseLicenseKey = _Hh3cLicenseLicenseKey_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 2, 1, 8),
    _Hh3cLicenseLicenseKey_Type()
)
hh3cLicenseLicenseKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLicenseLicenseKey.setStatus("current")


class _Hh3cLicenseUninstActivationFile_Type(SnmpAdminString):
    """Custom type hh3cLicenseUninstActivationFile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cLicenseUninstActivationFile_Type.__name__ = "SnmpAdminString"
_Hh3cLicenseUninstActivationFile_Object = MibTableColumn
hh3cLicenseUninstActivationFile = _Hh3cLicenseUninstActivationFile_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 2, 1, 9),
    _Hh3cLicenseUninstActivationFile_Type()
)
hh3cLicenseUninstActivationFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLicenseUninstActivationFile.setStatus("current")


class _Hh3cLicenseUninstActivationKey_Type(SnmpAdminString):
    """Custom type hh3cLicenseUninstActivationKey based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cLicenseUninstActivationKey_Type.__name__ = "SnmpAdminString"
_Hh3cLicenseUninstActivationKey_Object = MibTableColumn
hh3cLicenseUninstActivationKey = _Hh3cLicenseUninstActivationKey_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 2, 1, 10),
    _Hh3cLicenseUninstActivationKey_Type()
)
hh3cLicenseUninstActivationKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLicenseUninstActivationKey.setStatus("current")


class _Hh3cLicenseType_Type(Integer32):
    """Custom type hh3cLicenseType based on Integer32"""
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


_Hh3cLicenseType_Type.__name__ = "Integer32"
_Hh3cLicenseType_Object = MibTableColumn
hh3cLicenseType = _Hh3cLicenseType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 2, 1, 11),
    _Hh3cLicenseType_Type()
)
hh3cLicenseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLicenseType.setStatus("current")
_Hh3cLicenseInstalledTime_Type = DateAndTime
_Hh3cLicenseInstalledTime_Object = MibTableColumn
hh3cLicenseInstalledTime = _Hh3cLicenseInstalledTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 2, 1, 12),
    _Hh3cLicenseInstalledTime_Type()
)
hh3cLicenseInstalledTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLicenseInstalledTime.setStatus("current")
_Hh3cLicenseUninstalledTime_Type = DateAndTime
_Hh3cLicenseUninstalledTime_Object = MibTableColumn
hh3cLicenseUninstalledTime = _Hh3cLicenseUninstalledTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 2, 1, 13),
    _Hh3cLicenseUninstalledTime_Type()
)
hh3cLicenseUninstalledTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLicenseUninstalledTime.setStatus("current")
_Hh3cLicenseDaysLeft_Type = Unsigned32
_Hh3cLicenseDaysLeft_Object = MibTableColumn
hh3cLicenseDaysLeft = _Hh3cLicenseDaysLeft_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 2, 1, 14),
    _Hh3cLicenseDaysLeft_Type()
)
hh3cLicenseDaysLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLicenseDaysLeft.setStatus("current")
_Hh3cLicenseValidityStart_Type = DateAndTime
_Hh3cLicenseValidityStart_Object = MibTableColumn
hh3cLicenseValidityStart = _Hh3cLicenseValidityStart_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 2, 1, 15),
    _Hh3cLicenseValidityStart_Type()
)
hh3cLicenseValidityStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLicenseValidityStart.setStatus("current")
_Hh3cLicenseValidityEnd_Type = DateAndTime
_Hh3cLicenseValidityEnd_Object = MibTableColumn
hh3cLicenseValidityEnd = _Hh3cLicenseValidityEnd_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 2, 1, 16),
    _Hh3cLicenseValidityEnd_Type()
)
hh3cLicenseValidityEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLicenseValidityEnd.setStatus("current")
_Hh3cLicenseExpiredDays_Type = Unsigned32
_Hh3cLicenseExpiredDays_Object = MibTableColumn
hh3cLicenseExpiredDays = _Hh3cLicenseExpiredDays_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 2, 1, 17),
    _Hh3cLicenseExpiredDays_Type()
)
hh3cLicenseExpiredDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLicenseExpiredDays.setStatus("current")
_Hh3cLicenseCount_Type = Unsigned32
_Hh3cLicenseCount_Object = MibTableColumn
hh3cLicenseCount = _Hh3cLicenseCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 2, 1, 18),
    _Hh3cLicenseCount_Type()
)
hh3cLicenseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLicenseCount.setStatus("current")
_Hh3cLicenseFeatureTable_Object = MibTable
hh3cLicenseFeatureTable = _Hh3cLicenseFeatureTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cLicenseFeatureTable.setStatus("current")
_Hh3cLicenseFeatureEntry_Object = MibTableRow
hh3cLicenseFeatureEntry = _Hh3cLicenseFeatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 3, 1)
)
hh3cLicenseFeatureEntry.setIndexNames(
    (0, "HH3C-LICENSE-MIB", "hh3cLicensePhysicalIndex"),
    (1, "HH3C-LICENSE-MIB", "hh3cLicenseFeatureName"),
)
if mibBuilder.loadTexts:
    hh3cLicenseFeatureEntry.setStatus("current")


class _Hh3cLicenseFeatureName_Type(SnmpAdminString):
    """Custom type hh3cLicenseFeatureName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hh3cLicenseFeatureName_Type.__name__ = "SnmpAdminString"
_Hh3cLicenseFeatureName_Object = MibTableColumn
hh3cLicenseFeatureName = _Hh3cLicenseFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 3, 1, 1),
    _Hh3cLicenseFeatureName_Type()
)
hh3cLicenseFeatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLicenseFeatureName.setStatus("current")


class _Hh3cLicenseFeatureState_Type(Integer32):
    """Custom type hh3cLicenseFeatureState based on Integer32"""
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


_Hh3cLicenseFeatureState_Type.__name__ = "Integer32"
_Hh3cLicenseFeatureState_Object = MibTableColumn
hh3cLicenseFeatureState = _Hh3cLicenseFeatureState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 3, 1, 2),
    _Hh3cLicenseFeatureState_Type()
)
hh3cLicenseFeatureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLicenseFeatureState.setStatus("current")
_Hh3cLicenseOpTable_Object = MibTable
hh3cLicenseOpTable = _Hh3cLicenseOpTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 4)
)
if mibBuilder.loadTexts:
    hh3cLicenseOpTable.setStatus("current")
_Hh3cLicenseOpEntry_Object = MibTableRow
hh3cLicenseOpEntry = _Hh3cLicenseOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 4, 1)
)
hh3cLicenseOpEntry.setIndexNames(
    (0, "HH3C-LICENSE-MIB", "hh3cLicenseOpIndex"),
)
if mibBuilder.loadTexts:
    hh3cLicenseOpEntry.setStatus("current")
_Hh3cLicenseOpIndex_Type = Unsigned32
_Hh3cLicenseOpIndex_Object = MibTableColumn
hh3cLicenseOpIndex = _Hh3cLicenseOpIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 4, 1, 1),
    _Hh3cLicenseOpIndex_Type()
)
hh3cLicenseOpIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cLicenseOpIndex.setStatus("current")
_Hh3cLicenseOpPhysicalIndex_Type = PhysicalIndexOrZero
_Hh3cLicenseOpPhysicalIndex_Object = MibTableColumn
hh3cLicenseOpPhysicalIndex = _Hh3cLicenseOpPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 4, 1, 2),
    _Hh3cLicenseOpPhysicalIndex_Type()
)
hh3cLicenseOpPhysicalIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cLicenseOpPhysicalIndex.setStatus("current")


class _Hh3cLicenseOpType_Type(Integer32):
    """Custom type hh3cLicenseOpType based on Integer32"""
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


_Hh3cLicenseOpType_Type.__name__ = "Integer32"
_Hh3cLicenseOpType_Object = MibTableColumn
hh3cLicenseOpType = _Hh3cLicenseOpType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 4, 1, 3),
    _Hh3cLicenseOpType_Type()
)
hh3cLicenseOpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cLicenseOpType.setStatus("current")


class _Hh3cLicenseOpString_Type(SnmpAdminString):
    """Custom type hh3cLicenseOpString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cLicenseOpString_Type.__name__ = "SnmpAdminString"
_Hh3cLicenseOpString_Object = MibTableColumn
hh3cLicenseOpString = _Hh3cLicenseOpString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 4, 1, 4),
    _Hh3cLicenseOpString_Type()
)
hh3cLicenseOpString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cLicenseOpString.setStatus("current")


class _Hh3cLicenseOpNotifyEnable_Type(TruthValue):
    """Custom type hh3cLicenseOpNotifyEnable based on TruthValue"""


_Hh3cLicenseOpNotifyEnable_Object = MibTableColumn
hh3cLicenseOpNotifyEnable = _Hh3cLicenseOpNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 4, 1, 5),
    _Hh3cLicenseOpNotifyEnable_Type()
)
hh3cLicenseOpNotifyEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cLicenseOpNotifyEnable.setStatus("current")
_Hh3cLicenseOpRowStatus_Type = RowStatus
_Hh3cLicenseOpRowStatus_Object = MibTableColumn
hh3cLicenseOpRowStatus = _Hh3cLicenseOpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 4, 1, 6),
    _Hh3cLicenseOpRowStatus_Type()
)
hh3cLicenseOpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cLicenseOpRowStatus.setStatus("current")


class _Hh3cLicenseOpState_Type(Integer32):
    """Custom type hh3cLicenseOpState based on Integer32"""
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


_Hh3cLicenseOpState_Type.__name__ = "Integer32"
_Hh3cLicenseOpState_Object = MibTableColumn
hh3cLicenseOpState = _Hh3cLicenseOpState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 4, 1, 7),
    _Hh3cLicenseOpState_Type()
)
hh3cLicenseOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLicenseOpState.setStatus("current")


class _Hh3cLicenseOpFailedReason_Type(SnmpAdminString):
    """Custom type hh3cLicenseOpFailedReason based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cLicenseOpFailedReason_Type.__name__ = "SnmpAdminString"
_Hh3cLicenseOpFailedReason_Object = MibTableColumn
hh3cLicenseOpFailedReason = _Hh3cLicenseOpFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 4, 1, 8),
    _Hh3cLicenseOpFailedReason_Type()
)
hh3cLicenseOpFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLicenseOpFailedReason.setStatus("current")
_Hh3cLicenseOpEndTime_Type = TimeTicks
_Hh3cLicenseOpEndTime_Object = MibTableColumn
hh3cLicenseOpEndTime = _Hh3cLicenseOpEndTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 4, 1, 9),
    _Hh3cLicenseOpEndTime_Type()
)
hh3cLicenseOpEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLicenseOpEndTime.setStatus("current")
_Hh3cLicenseNotifications_ObjectIdentity = ObjectIdentity
hh3cLicenseNotifications = _Hh3cLicenseNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 3)
)
_Hh3cLicenseNotificationPrefix_ObjectIdentity = ObjectIdentity
hh3cLicenseNotificationPrefix = _Hh3cLicenseNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 3, 0)
)
_Hh3cLicenseNotificationBindings_ObjectIdentity = ObjectIdentity
hh3cLicenseNotificationBindings = _Hh3cLicenseNotificationBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 3, 1)
)
_Hh3cLicenseBindValidityPeriodRemaining_Type = Unsigned32
_Hh3cLicenseBindValidityPeriodRemaining_Object = MibScalar
hh3cLicenseBindValidityPeriodRemaining = _Hh3cLicenseBindValidityPeriodRemaining_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 3, 1, 1),
    _Hh3cLicenseBindValidityPeriodRemaining_Type()
)
hh3cLicenseBindValidityPeriodRemaining.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cLicenseBindValidityPeriodRemaining.setStatus("current")
if mibBuilder.loadTexts:
    hh3cLicenseBindValidityPeriodRemaining.setUnits("days")

# Managed Objects groups


# Notification objects

hh3cLicenseOpCompletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 3, 0, 1)
)
hh3cLicenseOpCompletion.setObjects(
      *(("HH3C-LICENSE-MIB", "hh3cLicenseOpIndex"),
        ("HH3C-LICENSE-MIB", "hh3cLicenseOpPhysicalIndex"),
        ("HH3C-LICENSE-MIB", "hh3cLicenseOpType"),
        ("HH3C-LICENSE-MIB", "hh3cLicenseOpString"),
        ("HH3C-LICENSE-MIB", "hh3cLicenseOpState"),
        ("HH3C-LICENSE-MIB", "hh3cLicenseOpFailedReason"))
)
if mibBuilder.loadTexts:
    hh3cLicenseOpCompletion.setStatus(
        "current"
    )

hh3cLicenseActivationFileLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 3, 0, 2)
)
hh3cLicenseActivationFileLost.setObjects(
      *(("HH3C-LICENSE-MIB", "hh3cLicensePhysicalIndex"),
        ("HH3C-LICENSE-MIB", "hh3cLicenseActivationFile"))
)
if mibBuilder.loadTexts:
    hh3cLicenseActivationFileLost.setStatus(
        "current"
    )

hh3cLicenseActivationFileRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 3, 0, 3)
)
hh3cLicenseActivationFileRestored.setObjects(
      *(("HH3C-LICENSE-MIB", "hh3cLicensePhysicalIndex"),
        ("HH3C-LICENSE-MIB", "hh3cLicenseActivationFile"))
)
if mibBuilder.loadTexts:
    hh3cLicenseActivationFileRestored.setStatus(
        "current"
    )

hh3cLicenseExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 3, 0, 4)
)
hh3cLicenseExpired.setObjects(
      *(("HH3C-LICENSE-MIB", "hh3cLicenseFeatureName"),
        ("HH3C-LICENSE-MIB", "hh3cLicenseFeatureState"))
)
if mibBuilder.loadTexts:
    hh3cLicenseExpired.setStatus(
        "current"
    )

hh3cLicenseExpireWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145, 3, 0, 5)
)
hh3cLicenseExpireWarning.setObjects(
      *(("HH3C-LICENSE-MIB", "hh3cLicenseFeatureName"),
        ("HH3C-LICENSE-MIB", "hh3cLicenseFeatureState"),
        ("HH3C-LICENSE-MIB", "hh3cLicenseBindValidityPeriodRemaining"))
)
if mibBuilder.loadTexts:
    hh3cLicenseExpireWarning.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-LICENSE-MIB",
    **{"hh3cLicense": hh3cLicense,
       "hh3cLicenseScalarObjects": hh3cLicenseScalarObjects,
       "hh3cLicenseNotifyEnable": hh3cLicenseNotifyEnable,
       "hh3cLicenseOpEntryMaxNum": hh3cLicenseOpEntryMaxNum,
       "hh3cLicenseNextFreeOpIndex": hh3cLicenseNextFreeOpIndex,
       "hh3cLicenseTables": hh3cLicenseTables,
       "hh3cLicenseDevInfoTable": hh3cLicenseDevInfoTable,
       "hh3cLicenseDevInfoEntry": hh3cLicenseDevInfoEntry,
       "hh3cLicensePhysicalIndex": hh3cLicensePhysicalIndex,
       "hh3cLicenseSN": hh3cLicenseSN,
       "hh3cLicenseDeviceIDType": hh3cLicenseDeviceIDType,
       "hh3cLicenseDeviceID": hh3cLicenseDeviceID,
       "hh3cLicenseHardwareInfo": hh3cLicenseHardwareInfo,
       "hh3cLicenseMaxNum": hh3cLicenseMaxNum,
       "hh3cLicenseUsedNum": hh3cLicenseUsedNum,
       "hh3cLicenseRecyclableNum": hh3cLicenseRecyclableNum,
       "hh3cLicenseInstallType": hh3cLicenseInstallType,
       "hh3cLicenseFileStoragePath": hh3cLicenseFileStoragePath,
       "hh3cLicenseGeneralTable": hh3cLicenseGeneralTable,
       "hh3cLicenseGeneralEntry": hh3cLicenseGeneralEntry,
       "hh3cLicenseIndex": hh3cLicenseIndex,
       "hh3cLicenseFeature": hh3cLicenseFeature,
       "hh3cLicenseProductDescr": hh3cLicenseProductDescr,
       "hh3cLicenseFileDescr": hh3cLicenseFileDescr,
       "hh3cLicenseState": hh3cLicenseState,
       "hh3cLicenseActivationFile": hh3cLicenseActivationFile,
       "hh3cLicenseActivationKey": hh3cLicenseActivationKey,
       "hh3cLicenseLicenseKey": hh3cLicenseLicenseKey,
       "hh3cLicenseUninstActivationFile": hh3cLicenseUninstActivationFile,
       "hh3cLicenseUninstActivationKey": hh3cLicenseUninstActivationKey,
       "hh3cLicenseType": hh3cLicenseType,
       "hh3cLicenseInstalledTime": hh3cLicenseInstalledTime,
       "hh3cLicenseUninstalledTime": hh3cLicenseUninstalledTime,
       "hh3cLicenseDaysLeft": hh3cLicenseDaysLeft,
       "hh3cLicenseValidityStart": hh3cLicenseValidityStart,
       "hh3cLicenseValidityEnd": hh3cLicenseValidityEnd,
       "hh3cLicenseExpiredDays": hh3cLicenseExpiredDays,
       "hh3cLicenseCount": hh3cLicenseCount,
       "hh3cLicenseFeatureTable": hh3cLicenseFeatureTable,
       "hh3cLicenseFeatureEntry": hh3cLicenseFeatureEntry,
       "hh3cLicenseFeatureName": hh3cLicenseFeatureName,
       "hh3cLicenseFeatureState": hh3cLicenseFeatureState,
       "hh3cLicenseOpTable": hh3cLicenseOpTable,
       "hh3cLicenseOpEntry": hh3cLicenseOpEntry,
       "hh3cLicenseOpIndex": hh3cLicenseOpIndex,
       "hh3cLicenseOpPhysicalIndex": hh3cLicenseOpPhysicalIndex,
       "hh3cLicenseOpType": hh3cLicenseOpType,
       "hh3cLicenseOpString": hh3cLicenseOpString,
       "hh3cLicenseOpNotifyEnable": hh3cLicenseOpNotifyEnable,
       "hh3cLicenseOpRowStatus": hh3cLicenseOpRowStatus,
       "hh3cLicenseOpState": hh3cLicenseOpState,
       "hh3cLicenseOpFailedReason": hh3cLicenseOpFailedReason,
       "hh3cLicenseOpEndTime": hh3cLicenseOpEndTime,
       "hh3cLicenseNotifications": hh3cLicenseNotifications,
       "hh3cLicenseNotificationPrefix": hh3cLicenseNotificationPrefix,
       "hh3cLicenseOpCompletion": hh3cLicenseOpCompletion,
       "hh3cLicenseActivationFileLost": hh3cLicenseActivationFileLost,
       "hh3cLicenseActivationFileRestored": hh3cLicenseActivationFileRestored,
       "hh3cLicenseExpired": hh3cLicenseExpired,
       "hh3cLicenseExpireWarning": hh3cLicenseExpireWarning,
       "hh3cLicenseNotificationBindings": hh3cLicenseNotificationBindings,
       "hh3cLicenseBindValidityPeriodRemaining": hh3cLicenseBindValidityPeriodRemaining}
)
