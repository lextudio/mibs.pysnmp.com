# SNMP MIB module (CISCO-LICENSE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LICENSE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:01 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(EntPhysicalIndexOrZero,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "EntPhysicalIndexOrZero")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(AutonomousType,
 DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoLicenseMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 359)
)
ciscoLicenseMIB.setRevisions(
        ("2004-01-31 00:00",
         "2003-06-06 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class LicenseType(Integer32, TextualConvention):
    status = "current"
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("channelization", 6),
          ("ima", 7),
          ("mfr", 8),
          ("multiService", 5),
          ("multilink", 10),
          ("none", 2),
          ("ppp", 11),
          ("rateControl", 9),
          ("reserved", 3),
          ("singleService", 4),
          ("unknown", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CelMIBNotifications_ObjectIdentity = ObjectIdentity
celMIBNotifications = _CelMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 0)
)
_CelMIBObjects_ObjectIdentity = ObjectIdentity
celMIBObjects = _CelMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 1)
)
_CelGeneral_ObjectIdentity = ObjectIdentity
celGeneral = _CelGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 1, 1)
)
_CelLicenseConfigHistoryTable_Object = MibTable
celLicenseConfigHistoryTable = _CelLicenseConfigHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 1, 1, 1)
)
if mibBuilder.loadTexts:
    celLicenseConfigHistoryTable.setStatus("current")
_CelLicenseConfigHistoryEntry_Object = MibTableRow
celLicenseConfigHistoryEntry = _CelLicenseConfigHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 1, 1, 1, 1)
)
celLicenseConfigHistoryEntry.setIndexNames(
    (0, "CISCO-LICENSE-MIB", "celLicenseConfigIndex"),
)
if mibBuilder.loadTexts:
    celLicenseConfigHistoryEntry.setStatus("current")


class _CelLicenseConfigIndex_Type(Unsigned32):
    """Custom type celLicenseConfigIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CelLicenseConfigIndex_Type.__name__ = "Unsigned32"
_CelLicenseConfigIndex_Object = MibTableColumn
celLicenseConfigIndex = _CelLicenseConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 1, 1, 1, 1, 1),
    _CelLicenseConfigIndex_Type()
)
celLicenseConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    celLicenseConfigIndex.setStatus("current")
_CelLicenseEntityVendorType_Type = AutonomousType
_CelLicenseEntityVendorType_Object = MibTableColumn
celLicenseEntityVendorType = _CelLicenseEntityVendorType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 1, 1, 1, 1, 2),
    _CelLicenseEntityVendorType_Type()
)
celLicenseEntityVendorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    celLicenseEntityVendorType.setStatus("current")


class _CelLicenseSerialNumber_Type(SnmpAdminString):
    """Custom type celLicenseSerialNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CelLicenseSerialNumber_Type.__name__ = "SnmpAdminString"
_CelLicenseSerialNumber_Object = MibTableColumn
celLicenseSerialNumber = _CelLicenseSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 1, 1, 1, 1, 3),
    _CelLicenseSerialNumber_Type()
)
celLicenseSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    celLicenseSerialNumber.setStatus("current")


class _CelLicenseInstallEntitySerNum_Type(SnmpAdminString):
    """Custom type celLicenseInstallEntitySerNum based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CelLicenseInstallEntitySerNum_Type.__name__ = "SnmpAdminString"
_CelLicenseInstallEntitySerNum_Object = MibTableColumn
celLicenseInstallEntitySerNum = _CelLicenseInstallEntitySerNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 1, 1, 1, 1, 4),
    _CelLicenseInstallEntitySerNum_Type()
)
celLicenseInstallEntitySerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    celLicenseInstallEntitySerNum.setStatus("current")
_CelLicenseUpdateTimeStamp_Type = DateAndTime
_CelLicenseUpdateTimeStamp_Object = MibTableColumn
celLicenseUpdateTimeStamp = _CelLicenseUpdateTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 1, 1, 1, 1, 5),
    _CelLicenseUpdateTimeStamp_Type()
)
celLicenseUpdateTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    celLicenseUpdateTimeStamp.setStatus("current")
_CelLicenseConfigHistoryIndex_Type = Counter32
_CelLicenseConfigHistoryIndex_Object = MibTableColumn
celLicenseConfigHistoryIndex = _CelLicenseConfigHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 1, 1, 1, 1, 6),
    _CelLicenseConfigHistoryIndex_Type()
)
celLicenseConfigHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    celLicenseConfigHistoryIndex.setStatus("current")
_CelLicenseUpdateSequenceNum_Type = Counter32
_CelLicenseUpdateSequenceNum_Object = MibTableColumn
celLicenseUpdateSequenceNum = _CelLicenseUpdateSequenceNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 1, 1, 1, 1, 7),
    _CelLicenseUpdateSequenceNum_Type()
)
celLicenseUpdateSequenceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    celLicenseUpdateSequenceNum.setStatus("current")


class _CelLicenseUpdateMethod_Type(SnmpAdminString):
    """Custom type celLicenseUpdateMethod based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CelLicenseUpdateMethod_Type.__name__ = "SnmpAdminString"
_CelLicenseUpdateMethod_Object = MibTableColumn
celLicenseUpdateMethod = _CelLicenseUpdateMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 1, 1, 1, 1, 8),
    _CelLicenseUpdateMethod_Type()
)
celLicenseUpdateMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    celLicenseUpdateMethod.setStatus("current")
_CelLicenseConfigDetailTable_Object = MibTable
celLicenseConfigDetailTable = _CelLicenseConfigDetailTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 1, 1, 2)
)
if mibBuilder.loadTexts:
    celLicenseConfigDetailTable.setStatus("current")
_CelLicenseConfigDetailEntry_Object = MibTableRow
celLicenseConfigDetailEntry = _CelLicenseConfigDetailEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 1, 1, 2, 1)
)
celLicenseConfigDetailEntry.setIndexNames(
    (0, "CISCO-LICENSE-MIB", "celLicenseConfigIndex"),
    (0, "CISCO-LICENSE-MIB", "celLicenseConfigType"),
)
if mibBuilder.loadTexts:
    celLicenseConfigDetailEntry.setStatus("current")
_CelLicenseConfigType_Type = LicenseType
_CelLicenseConfigType_Object = MibTableColumn
celLicenseConfigType = _CelLicenseConfigType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 1, 1, 2, 1, 1),
    _CelLicenseConfigType_Type()
)
celLicenseConfigType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    celLicenseConfigType.setStatus("current")


class _CelLicenseTypeDescr_Type(SnmpAdminString):
    """Custom type celLicenseTypeDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CelLicenseTypeDescr_Type.__name__ = "SnmpAdminString"
_CelLicenseTypeDescr_Object = MibTableColumn
celLicenseTypeDescr = _CelLicenseTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 1, 1, 2, 1, 2),
    _CelLicenseTypeDescr_Type()
)
celLicenseTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    celLicenseTypeDescr.setStatus("current")


class _CelLicenseConfigCount_Type(Unsigned32):
    """Custom type celLicenseConfigCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CelLicenseConfigCount_Type.__name__ = "Unsigned32"
_CelLicenseConfigCount_Object = MibTableColumn
celLicenseConfigCount = _CelLicenseConfigCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 1, 1, 2, 1, 3),
    _CelLicenseConfigCount_Type()
)
celLicenseConfigCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    celLicenseConfigCount.setStatus("current")
_CelPoolLicenseTable_Object = MibTable
celPoolLicenseTable = _CelPoolLicenseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 1, 1, 3)
)
if mibBuilder.loadTexts:
    celPoolLicenseTable.setStatus("current")
_CelPoolLicenseEntry_Object = MibTableRow
celPoolLicenseEntry = _CelPoolLicenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 1, 1, 3, 1)
)
celPoolLicenseEntry.setIndexNames(
    (0, "CISCO-LICENSE-MIB", "celPoolLicenseIndex"),
)
if mibBuilder.loadTexts:
    celPoolLicenseEntry.setStatus("current")


class _CelPoolLicenseIndex_Type(Unsigned32):
    """Custom type celPoolLicenseIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CelPoolLicenseIndex_Type.__name__ = "Unsigned32"
_CelPoolLicenseIndex_Object = MibTableColumn
celPoolLicenseIndex = _CelPoolLicenseIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 1, 1, 3, 1, 1),
    _CelPoolLicenseIndex_Type()
)
celPoolLicenseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    celPoolLicenseIndex.setStatus("current")
_CelPoolLicenseEntityVendorType_Type = AutonomousType
_CelPoolLicenseEntityVendorType_Object = MibTableColumn
celPoolLicenseEntityVendorType = _CelPoolLicenseEntityVendorType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 1, 1, 3, 1, 2),
    _CelPoolLicenseEntityVendorType_Type()
)
celPoolLicenseEntityVendorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    celPoolLicenseEntityVendorType.setStatus("current")
_CelPoolLicenseType_Type = LicenseType
_CelPoolLicenseType_Object = MibTableColumn
celPoolLicenseType = _CelPoolLicenseType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 1, 1, 3, 1, 3),
    _CelPoolLicenseType_Type()
)
celPoolLicenseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    celPoolLicenseType.setStatus("current")
_CelPoolLicensesInstalled_Type = Gauge32
_CelPoolLicensesInstalled_Object = MibTableColumn
celPoolLicensesInstalled = _CelPoolLicensesInstalled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 1, 1, 3, 1, 4),
    _CelPoolLicensesInstalled_Type()
)
celPoolLicensesInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    celPoolLicensesInstalled.setStatus("current")
_CelPoolLicensesInUse_Type = Gauge32
_CelPoolLicensesInUse_Object = MibTableColumn
celPoolLicensesInUse = _CelPoolLicensesInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 1, 1, 3, 1, 5),
    _CelPoolLicensesInUse_Type()
)
celPoolLicensesInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    celPoolLicensesInUse.setStatus("current")
_CelPoolLicenseMaxUsage_Type = Gauge32
_CelPoolLicenseMaxUsage_Object = MibTableColumn
celPoolLicenseMaxUsage = _CelPoolLicenseMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 1, 1, 3, 1, 6),
    _CelPoolLicenseMaxUsage_Type()
)
celPoolLicenseMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    celPoolLicenseMaxUsage.setStatus("current")
_CelInUseLicenseTable_Object = MibTable
celInUseLicenseTable = _CelInUseLicenseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 1, 1, 4)
)
if mibBuilder.loadTexts:
    celInUseLicenseTable.setStatus("current")
_CelInUseLicenseEntry_Object = MibTableRow
celInUseLicenseEntry = _CelInUseLicenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 1, 1, 4, 1)
)
celInUseLicenseEntry.setIndexNames(
    (0, "CISCO-LICENSE-MIB", "celInUseSlotIndex"),
    (0, "CISCO-LICENSE-MIB", "celInUseLicenseType"),
)
if mibBuilder.loadTexts:
    celInUseLicenseEntry.setStatus("current")


class _CelInUseSlotIndex_Type(Integer32):
    """Custom type celInUseSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CelInUseSlotIndex_Type.__name__ = "Integer32"
_CelInUseSlotIndex_Object = MibTableColumn
celInUseSlotIndex = _CelInUseSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 1, 1, 4, 1, 1),
    _CelInUseSlotIndex_Type()
)
celInUseSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    celInUseSlotIndex.setStatus("current")
_CelInUseLicenseType_Type = LicenseType
_CelInUseLicenseType_Object = MibTableColumn
celInUseLicenseType = _CelInUseLicenseType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 1, 1, 4, 1, 2),
    _CelInUseLicenseType_Type()
)
celInUseLicenseType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    celInUseLicenseType.setStatus("current")
_CelEntPhysicalIndex_Type = EntPhysicalIndexOrZero
_CelEntPhysicalIndex_Object = MibTableColumn
celEntPhysicalIndex = _CelEntPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 1, 1, 4, 1, 3),
    _CelEntPhysicalIndex_Type()
)
celEntPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    celEntPhysicalIndex.setStatus("current")


class _CelInUseLicenseDescr_Type(SnmpAdminString):
    """Custom type celInUseLicenseDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CelInUseLicenseDescr_Type.__name__ = "SnmpAdminString"
_CelInUseLicenseDescr_Object = MibTableColumn
celInUseLicenseDescr = _CelInUseLicenseDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 1, 1, 4, 1, 4),
    _CelInUseLicenseDescr_Type()
)
celInUseLicenseDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    celInUseLicenseDescr.setStatus("current")


class _CelInUseLicenses_Type(Gauge32):
    """Custom type celInUseLicenses based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CelInUseLicenses_Type.__name__ = "Gauge32"
_CelInUseLicenses_Object = MibTableColumn
celInUseLicenses = _CelInUseLicenses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 1, 1, 4, 1, 5),
    _CelInUseLicenses_Type()
)
celInUseLicenses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    celInUseLicenses.setStatus("current")


class _CelNeededLicenses_Type(Gauge32):
    """Custom type celNeededLicenses based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CelNeededLicenses_Type.__name__ = "Gauge32"
_CelNeededLicenses_Object = MibTableColumn
celNeededLicenses = _CelNeededLicenses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 1, 1, 4, 1, 6),
    _CelNeededLicenses_Type()
)
celNeededLicenses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    celNeededLicenses.setStatus("current")
_CelOperationExpiryTmStamp_Type = DateAndTime
_CelOperationExpiryTmStamp_Object = MibTableColumn
celOperationExpiryTmStamp = _CelOperationExpiryTmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 1, 1, 4, 1, 7),
    _CelOperationExpiryTmStamp_Type()
)
celOperationExpiryTmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    celOperationExpiryTmStamp.setStatus("current")
_CelPhysicallyProgLicenseTable_Object = MibTable
celPhysicallyProgLicenseTable = _CelPhysicallyProgLicenseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 1, 1, 5)
)
if mibBuilder.loadTexts:
    celPhysicallyProgLicenseTable.setStatus("current")
_CelPhysicallyProgLicenseEntry_Object = MibTableRow
celPhysicallyProgLicenseEntry = _CelPhysicallyProgLicenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 1, 1, 5, 1)
)
celPhysicallyProgLicenseEntry.setIndexNames(
    (0, "CISCO-LICENSE-MIB", "celPhysicallyProgSlotNumber"),
    (0, "CISCO-LICENSE-MIB", "celPhysicallyProgLicenseType"),
)
if mibBuilder.loadTexts:
    celPhysicallyProgLicenseEntry.setStatus("current")


class _CelPhysicallyProgSlotNumber_Type(Integer32):
    """Custom type celPhysicallyProgSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CelPhysicallyProgSlotNumber_Type.__name__ = "Integer32"
_CelPhysicallyProgSlotNumber_Object = MibTableColumn
celPhysicallyProgSlotNumber = _CelPhysicallyProgSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 1, 1, 5, 1, 1),
    _CelPhysicallyProgSlotNumber_Type()
)
celPhysicallyProgSlotNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    celPhysicallyProgSlotNumber.setStatus("current")
_CelPhysicallyProgLicenseType_Type = LicenseType
_CelPhysicallyProgLicenseType_Object = MibTableColumn
celPhysicallyProgLicenseType = _CelPhysicallyProgLicenseType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 1, 1, 5, 1, 2),
    _CelPhysicallyProgLicenseType_Type()
)
celPhysicallyProgLicenseType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    celPhysicallyProgLicenseType.setStatus("current")
_CelPhysicallyProgEntIndex_Type = EntPhysicalIndexOrZero
_CelPhysicallyProgEntIndex_Object = MibTableColumn
celPhysicallyProgEntIndex = _CelPhysicallyProgEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 1, 1, 5, 1, 3),
    _CelPhysicallyProgEntIndex_Type()
)
celPhysicallyProgEntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    celPhysicallyProgEntIndex.setStatus("current")


class _CelPhysicallyProgLicTypeDescr_Type(SnmpAdminString):
    """Custom type celPhysicallyProgLicTypeDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CelPhysicallyProgLicTypeDescr_Type.__name__ = "SnmpAdminString"
_CelPhysicallyProgLicTypeDescr_Object = MibTableColumn
celPhysicallyProgLicTypeDescr = _CelPhysicallyProgLicTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 1, 1, 5, 1, 4),
    _CelPhysicallyProgLicTypeDescr_Type()
)
celPhysicallyProgLicTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    celPhysicallyProgLicTypeDescr.setStatus("current")


class _CelPhysicallyProgLicenses_Type(Unsigned32):
    """Custom type celPhysicallyProgLicenses based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CelPhysicallyProgLicenses_Type.__name__ = "Unsigned32"
_CelPhysicallyProgLicenses_Object = MibTableColumn
celPhysicallyProgLicenses = _CelPhysicallyProgLicenses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 1, 1, 5, 1, 5),
    _CelPhysicallyProgLicenses_Type()
)
celPhysicallyProgLicenses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    celPhysicallyProgLicenses.setStatus("current")


class _CelPhysicallyProgLicenseStatus_Type(Integer32):
    """Custom type celPhysicallyProgLicenseStatus based on Integer32"""
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
        *(("alreadyInstalled", 4),
          ("hasInstallableLic", 3),
          ("noInstallableLic", 2),
          ("unknown", 1))
    )


_CelPhysicallyProgLicenseStatus_Type.__name__ = "Integer32"
_CelPhysicallyProgLicenseStatus_Object = MibTableColumn
celPhysicallyProgLicenseStatus = _CelPhysicallyProgLicenseStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 1, 1, 5, 1, 6),
    _CelPhysicallyProgLicenseStatus_Type()
)
celPhysicallyProgLicenseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    celPhysicallyProgLicenseStatus.setStatus("current")


class _CelPhysicallyProgLicInstSysName_Type(DisplayString):
    """Custom type celPhysicallyProgLicInstSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CelPhysicallyProgLicInstSysName_Type.__name__ = "DisplayString"
_CelPhysicallyProgLicInstSysName_Object = MibTableColumn
celPhysicallyProgLicInstSysName = _CelPhysicallyProgLicInstSysName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 1, 1, 5, 1, 7),
    _CelPhysicallyProgLicInstSysName_Type()
)
celPhysicallyProgLicInstSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    celPhysicallyProgLicInstSysName.setStatus("current")


class _CelPhysicallyProgLicInstSerNum_Type(SnmpAdminString):
    """Custom type celPhysicallyProgLicInstSerNum based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CelPhysicallyProgLicInstSerNum_Type.__name__ = "SnmpAdminString"
_CelPhysicallyProgLicInstSerNum_Object = MibTableColumn
celPhysicallyProgLicInstSerNum = _CelPhysicallyProgLicInstSerNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 1, 1, 5, 1, 8),
    _CelPhysicallyProgLicInstSerNum_Type()
)
celPhysicallyProgLicInstSerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    celPhysicallyProgLicInstSerNum.setStatus("current")


class _CelPhysicallyProgLicSerialNum_Type(SnmpAdminString):
    """Custom type celPhysicallyProgLicSerialNum based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CelPhysicallyProgLicSerialNum_Type.__name__ = "SnmpAdminString"
_CelPhysicallyProgLicSerialNum_Object = MibTableColumn
celPhysicallyProgLicSerialNum = _CelPhysicallyProgLicSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 1, 1, 5, 1, 9),
    _CelPhysicallyProgLicSerialNum_Type()
)
celPhysicallyProgLicSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    celPhysicallyProgLicSerialNum.setStatus("current")
_CelPhysicallyProgLicUseTmStamp_Type = DateAndTime
_CelPhysicallyProgLicUseTmStamp_Object = MibTableColumn
celPhysicallyProgLicUseTmStamp = _CelPhysicallyProgLicUseTmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 1, 1, 5, 1, 10),
    _CelPhysicallyProgLicUseTmStamp_Type()
)
celPhysicallyProgLicUseTmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    celPhysicallyProgLicUseTmStamp.setStatus("current")
_CelMIBConformance_ObjectIdentity = ObjectIdentity
celMIBConformance = _CelMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 2)
)
_CelMIBCompliances_ObjectIdentity = ObjectIdentity
celMIBCompliances = _CelMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 2, 1)
)
_CelMIBGroups_ObjectIdentity = ObjectIdentity
celMIBGroups = _CelMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 2, 2)
)

# Managed Objects groups

celMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 2, 2, 1)
)
celMIBGroup.setObjects(
      *(("CISCO-LICENSE-MIB", "celLicenseEntityVendorType"),
        ("CISCO-LICENSE-MIB", "celLicenseSerialNumber"),
        ("CISCO-LICENSE-MIB", "celLicenseInstallEntitySerNum"),
        ("CISCO-LICENSE-MIB", "celLicenseUpdateTimeStamp"),
        ("CISCO-LICENSE-MIB", "celLicenseConfigHistoryIndex"),
        ("CISCO-LICENSE-MIB", "celLicenseUpdateSequenceNum"),
        ("CISCO-LICENSE-MIB", "celLicenseUpdateMethod"),
        ("CISCO-LICENSE-MIB", "celLicenseConfigCount"),
        ("CISCO-LICENSE-MIB", "celLicenseTypeDescr"),
        ("CISCO-LICENSE-MIB", "celPoolLicenseEntityVendorType"),
        ("CISCO-LICENSE-MIB", "celPoolLicenseType"),
        ("CISCO-LICENSE-MIB", "celPoolLicensesInstalled"),
        ("CISCO-LICENSE-MIB", "celPoolLicensesInUse"),
        ("CISCO-LICENSE-MIB", "celPoolLicenseMaxUsage"),
        ("CISCO-LICENSE-MIB", "celInUseLicenseDescr"),
        ("CISCO-LICENSE-MIB", "celInUseLicenses"),
        ("CISCO-LICENSE-MIB", "celEntPhysicalIndex"),
        ("CISCO-LICENSE-MIB", "celNeededLicenses"),
        ("CISCO-LICENSE-MIB", "celOperationExpiryTmStamp"),
        ("CISCO-LICENSE-MIB", "celPhysicallyProgLicenses"),
        ("CISCO-LICENSE-MIB", "celPhysicallyProgEntIndex"),
        ("CISCO-LICENSE-MIB", "celPhysicallyProgLicTypeDescr"),
        ("CISCO-LICENSE-MIB", "celPhysicallyProgLicenseStatus"),
        ("CISCO-LICENSE-MIB", "celPhysicallyProgLicInstSysName"),
        ("CISCO-LICENSE-MIB", "celPhysicallyProgLicInstSerNum"),
        ("CISCO-LICENSE-MIB", "celPhysicallyProgLicSerialNum"),
        ("CISCO-LICENSE-MIB", "celPhysicallyProgLicUseTmStamp"))
)
if mibBuilder.loadTexts:
    celMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

celMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 359, 2, 1, 1)
)
if mibBuilder.loadTexts:
    celMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LICENSE-MIB",
    **{"LicenseType": LicenseType,
       "ciscoLicenseMIB": ciscoLicenseMIB,
       "celMIBNotifications": celMIBNotifications,
       "celMIBObjects": celMIBObjects,
       "celGeneral": celGeneral,
       "celLicenseConfigHistoryTable": celLicenseConfigHistoryTable,
       "celLicenseConfigHistoryEntry": celLicenseConfigHistoryEntry,
       "celLicenseConfigIndex": celLicenseConfigIndex,
       "celLicenseEntityVendorType": celLicenseEntityVendorType,
       "celLicenseSerialNumber": celLicenseSerialNumber,
       "celLicenseInstallEntitySerNum": celLicenseInstallEntitySerNum,
       "celLicenseUpdateTimeStamp": celLicenseUpdateTimeStamp,
       "celLicenseConfigHistoryIndex": celLicenseConfigHistoryIndex,
       "celLicenseUpdateSequenceNum": celLicenseUpdateSequenceNum,
       "celLicenseUpdateMethod": celLicenseUpdateMethod,
       "celLicenseConfigDetailTable": celLicenseConfigDetailTable,
       "celLicenseConfigDetailEntry": celLicenseConfigDetailEntry,
       "celLicenseConfigType": celLicenseConfigType,
       "celLicenseTypeDescr": celLicenseTypeDescr,
       "celLicenseConfigCount": celLicenseConfigCount,
       "celPoolLicenseTable": celPoolLicenseTable,
       "celPoolLicenseEntry": celPoolLicenseEntry,
       "celPoolLicenseIndex": celPoolLicenseIndex,
       "celPoolLicenseEntityVendorType": celPoolLicenseEntityVendorType,
       "celPoolLicenseType": celPoolLicenseType,
       "celPoolLicensesInstalled": celPoolLicensesInstalled,
       "celPoolLicensesInUse": celPoolLicensesInUse,
       "celPoolLicenseMaxUsage": celPoolLicenseMaxUsage,
       "celInUseLicenseTable": celInUseLicenseTable,
       "celInUseLicenseEntry": celInUseLicenseEntry,
       "celInUseSlotIndex": celInUseSlotIndex,
       "celInUseLicenseType": celInUseLicenseType,
       "celEntPhysicalIndex": celEntPhysicalIndex,
       "celInUseLicenseDescr": celInUseLicenseDescr,
       "celInUseLicenses": celInUseLicenses,
       "celNeededLicenses": celNeededLicenses,
       "celOperationExpiryTmStamp": celOperationExpiryTmStamp,
       "celPhysicallyProgLicenseTable": celPhysicallyProgLicenseTable,
       "celPhysicallyProgLicenseEntry": celPhysicallyProgLicenseEntry,
       "celPhysicallyProgSlotNumber": celPhysicallyProgSlotNumber,
       "celPhysicallyProgLicenseType": celPhysicallyProgLicenseType,
       "celPhysicallyProgEntIndex": celPhysicallyProgEntIndex,
       "celPhysicallyProgLicTypeDescr": celPhysicallyProgLicTypeDescr,
       "celPhysicallyProgLicenses": celPhysicallyProgLicenses,
       "celPhysicallyProgLicenseStatus": celPhysicallyProgLicenseStatus,
       "celPhysicallyProgLicInstSysName": celPhysicallyProgLicInstSysName,
       "celPhysicallyProgLicInstSerNum": celPhysicallyProgLicInstSerNum,
       "celPhysicallyProgLicSerialNum": celPhysicallyProgLicSerialNum,
       "celPhysicallyProgLicUseTmStamp": celPhysicallyProgLicUseTmStamp,
       "celMIBConformance": celMIBConformance,
       "celMIBCompliances": celMIBCompliances,
       "celMIBCompliance": celMIBCompliance,
       "celMIBGroups": celMIBGroups,
       "celMIBGroup": celMIBGroup}
)
