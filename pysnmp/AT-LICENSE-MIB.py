# SNMP MIB module (AT-LICENSE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AT-LICENSE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:22 2024
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

(sysinfo,) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "sysinfo")

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

license = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 22)
)
license.setRevisions(
        ("2010-09-07 00:00",
         "2010-08-30 00:00",
         "2010-06-14 05:09",
         "2008-11-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BaseLicenseTable_Object = MibTable
baseLicenseTable = _BaseLicenseTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 22, 1)
)
if mibBuilder.loadTexts:
    baseLicenseTable.setStatus("current")
_BaseLicenseEntry_Object = MibTableRow
baseLicenseEntry = _BaseLicenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 22, 1, 1)
)
baseLicenseEntry.setIndexNames(
    (0, "AT-LICENSE-MIB", "baseLicenseStackId"),
)
if mibBuilder.loadTexts:
    baseLicenseEntry.setStatus("current")


class _BaseLicenseStackId_Type(Integer32):
    """Custom type baseLicenseStackId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BaseLicenseStackId_Type.__name__ = "Integer32"
_BaseLicenseStackId_Object = MibTableColumn
baseLicenseStackId = _BaseLicenseStackId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 22, 1, 1, 1),
    _BaseLicenseStackId_Type()
)
baseLicenseStackId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    baseLicenseStackId.setStatus("current")
_BaseLicenseName_Type = DisplayString
_BaseLicenseName_Object = MibTableColumn
baseLicenseName = _BaseLicenseName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 22, 1, 1, 2),
    _BaseLicenseName_Type()
)
baseLicenseName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseLicenseName.setStatus("current")
_BaseLicenseQuantity_Type = Integer32
_BaseLicenseQuantity_Object = MibTableColumn
baseLicenseQuantity = _BaseLicenseQuantity_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 22, 1, 1, 3),
    _BaseLicenseQuantity_Type()
)
baseLicenseQuantity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseLicenseQuantity.setStatus("current")
_BaseLicenseType_Type = DisplayString
_BaseLicenseType_Object = MibTableColumn
baseLicenseType = _BaseLicenseType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 22, 1, 1, 4),
    _BaseLicenseType_Type()
)
baseLicenseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseLicenseType.setStatus("current")
_BaseLicenseIssueDate_Type = DisplayString
_BaseLicenseIssueDate_Object = MibTableColumn
baseLicenseIssueDate = _BaseLicenseIssueDate_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 22, 1, 1, 5),
    _BaseLicenseIssueDate_Type()
)
baseLicenseIssueDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseLicenseIssueDate.setStatus("current")
_BaseLicenseExpiryDate_Type = DisplayString
_BaseLicenseExpiryDate_Object = MibTableColumn
baseLicenseExpiryDate = _BaseLicenseExpiryDate_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 22, 1, 1, 6),
    _BaseLicenseExpiryDate_Type()
)
baseLicenseExpiryDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseLicenseExpiryDate.setStatus("current")
_BaseLicenseFeatures_Type = OctetString
_BaseLicenseFeatures_Object = MibTableColumn
baseLicenseFeatures = _BaseLicenseFeatures_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 22, 1, 1, 7),
    _BaseLicenseFeatures_Type()
)
baseLicenseFeatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseLicenseFeatures.setStatus("current")
_LicenseTable_Object = MibTable
licenseTable = _LicenseTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 22, 2)
)
if mibBuilder.loadTexts:
    licenseTable.setStatus("current")
_LicenseEntry_Object = MibTableRow
licenseEntry = _LicenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 22, 2, 1)
)
licenseEntry.setIndexNames(
    (0, "AT-LICENSE-MIB", "licenseStackId"),
    (0, "AT-LICENSE-MIB", "licenseIndex"),
)
if mibBuilder.loadTexts:
    licenseEntry.setStatus("current")


class _LicenseStackId_Type(Integer32):
    """Custom type licenseStackId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LicenseStackId_Type.__name__ = "Integer32"
_LicenseStackId_Object = MibTableColumn
licenseStackId = _LicenseStackId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 22, 2, 1, 1),
    _LicenseStackId_Type()
)
licenseStackId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    licenseStackId.setStatus("current")


class _LicenseIndex_Type(Integer32):
    """Custom type licenseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LicenseIndex_Type.__name__ = "Integer32"
_LicenseIndex_Object = MibTableColumn
licenseIndex = _LicenseIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 22, 2, 1, 2),
    _LicenseIndex_Type()
)
licenseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    licenseIndex.setStatus("current")
_LicenseName_Type = DisplayString
_LicenseName_Object = MibTableColumn
licenseName = _LicenseName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 22, 2, 1, 3),
    _LicenseName_Type()
)
licenseName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseName.setStatus("current")
_LicenseCustomer_Type = DisplayString
_LicenseCustomer_Object = MibTableColumn
licenseCustomer = _LicenseCustomer_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 22, 2, 1, 4),
    _LicenseCustomer_Type()
)
licenseCustomer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseCustomer.setStatus("current")
_LicenseQuantity_Type = Integer32
_LicenseQuantity_Object = MibTableColumn
licenseQuantity = _LicenseQuantity_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 22, 2, 1, 5),
    _LicenseQuantity_Type()
)
licenseQuantity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseQuantity.setStatus("current")
_LicenseType_Type = DisplayString
_LicenseType_Object = MibTableColumn
licenseType = _LicenseType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 22, 2, 1, 6),
    _LicenseType_Type()
)
licenseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseType.setStatus("current")
_LicenseIssueDate_Type = DisplayString
_LicenseIssueDate_Object = MibTableColumn
licenseIssueDate = _LicenseIssueDate_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 22, 2, 1, 7),
    _LicenseIssueDate_Type()
)
licenseIssueDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseIssueDate.setStatus("current")
_LicenseExpiryDate_Type = DisplayString
_LicenseExpiryDate_Object = MibTableColumn
licenseExpiryDate = _LicenseExpiryDate_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 22, 2, 1, 8),
    _LicenseExpiryDate_Type()
)
licenseExpiryDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseExpiryDate.setStatus("current")
_LicenseFeatures_Type = OctetString
_LicenseFeatures_Object = MibTableColumn
licenseFeatures = _LicenseFeatures_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 22, 2, 1, 9),
    _LicenseFeatures_Type()
)
licenseFeatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseFeatures.setStatus("current")
_LicenseRowStatus_Type = RowStatus
_LicenseRowStatus_Object = MibTableColumn
licenseRowStatus = _LicenseRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 22, 2, 1, 10),
    _LicenseRowStatus_Type()
)
licenseRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    licenseRowStatus.setStatus("current")
_LicenseFeatureTable_Object = MibTable
licenseFeatureTable = _LicenseFeatureTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 22, 3)
)
if mibBuilder.loadTexts:
    licenseFeatureTable.setStatus("current")
_LicenseFeatureEntry_Object = MibTableRow
licenseFeatureEntry = _LicenseFeatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 22, 3, 1)
)
licenseFeatureEntry.setIndexNames(
    (0, "AT-LICENSE-MIB", "licenseFeatureIndex"),
)
if mibBuilder.loadTexts:
    licenseFeatureEntry.setStatus("current")


class _LicenseFeatureIndex_Type(Integer32):
    """Custom type licenseFeatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LicenseFeatureIndex_Type.__name__ = "Integer32"
_LicenseFeatureIndex_Object = MibTableColumn
licenseFeatureIndex = _LicenseFeatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 22, 3, 1, 1),
    _LicenseFeatureIndex_Type()
)
licenseFeatureIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    licenseFeatureIndex.setStatus("current")
_LicenseFeatureName_Type = DisplayString
_LicenseFeatureName_Object = MibTableColumn
licenseFeatureName = _LicenseFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 22, 3, 1, 2),
    _LicenseFeatureName_Type()
)
licenseFeatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseFeatureName.setStatus("current")
_LicenseFeatureStkMembers_Type = OctetString
_LicenseFeatureStkMembers_Object = MibTableColumn
licenseFeatureStkMembers = _LicenseFeatureStkMembers_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 22, 3, 1, 3),
    _LicenseFeatureStkMembers_Type()
)
licenseFeatureStkMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseFeatureStkMembers.setStatus("current")
_LicenseNew_ObjectIdentity = ObjectIdentity
licenseNew = _LicenseNew_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 22, 4)
)


class _LicenseNewStackId_Type(Integer32):
    """Custom type licenseNewStackId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LicenseNewStackId_Type.__name__ = "Integer32"
_LicenseNewStackId_Object = MibScalar
licenseNewStackId = _LicenseNewStackId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 22, 4, 1),
    _LicenseNewStackId_Type()
)
licenseNewStackId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    licenseNewStackId.setStatus("current")
_LicenseNewName_Type = DisplayString
_LicenseNewName_Object = MibScalar
licenseNewName = _LicenseNewName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 22, 4, 2),
    _LicenseNewName_Type()
)
licenseNewName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    licenseNewName.setStatus("current")
_LicenseNewKey_Type = DisplayString
_LicenseNewKey_Object = MibScalar
licenseNewKey = _LicenseNewKey_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 22, 4, 3),
    _LicenseNewKey_Type()
)
licenseNewKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    licenseNewKey.setStatus("current")
_LicenseNewInstall_Type = TruthValue
_LicenseNewInstall_Object = MibScalar
licenseNewInstall = _LicenseNewInstall_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 22, 4, 4),
    _LicenseNewInstall_Type()
)
licenseNewInstall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    licenseNewInstall.setStatus("current")


class _LicenseNewInstallStatus_Type(Integer32):
    """Custom type licenseNewInstallStatus based on Integer32"""
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
          ("idle", 1),
          ("processing", 2),
          ("success", 3))
    )


_LicenseNewInstallStatus_Type.__name__ = "Integer32"
_LicenseNewInstallStatus_Object = MibScalar
licenseNewInstallStatus = _LicenseNewInstallStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 22, 4, 5),
    _LicenseNewInstallStatus_Type()
)
licenseNewInstallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseNewInstallStatus.setStatus("current")
_LicenseStackRemove_ObjectIdentity = ObjectIdentity
licenseStackRemove = _LicenseStackRemove_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 22, 5)
)
_LicenseStackRemoveName_Type = DisplayString
_LicenseStackRemoveName_Object = MibScalar
licenseStackRemoveName = _LicenseStackRemoveName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 22, 5, 1),
    _LicenseStackRemoveName_Type()
)
licenseStackRemoveName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    licenseStackRemoveName.setStatus("current")
_LicenseStackRemoveExecute_Type = TruthValue
_LicenseStackRemoveExecute_Object = MibScalar
licenseStackRemoveExecute = _LicenseStackRemoveExecute_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 22, 5, 2),
    _LicenseStackRemoveExecute_Type()
)
licenseStackRemoveExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    licenseStackRemoveExecute.setStatus("current")


class _LicenseStackRemoveStatus_Type(Integer32):
    """Custom type licenseStackRemoveStatus based on Integer32"""
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
          ("idle", 1),
          ("processing", 2),
          ("success", 3))
    )


_LicenseStackRemoveStatus_Type.__name__ = "Integer32"
_LicenseStackRemoveStatus_Object = MibScalar
licenseStackRemoveStatus = _LicenseStackRemoveStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 22, 5, 3),
    _LicenseStackRemoveStatus_Type()
)
licenseStackRemoveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseStackRemoveStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-LICENSE-MIB",
    **{"license": license,
       "baseLicenseTable": baseLicenseTable,
       "baseLicenseEntry": baseLicenseEntry,
       "baseLicenseStackId": baseLicenseStackId,
       "baseLicenseName": baseLicenseName,
       "baseLicenseQuantity": baseLicenseQuantity,
       "baseLicenseType": baseLicenseType,
       "baseLicenseIssueDate": baseLicenseIssueDate,
       "baseLicenseExpiryDate": baseLicenseExpiryDate,
       "baseLicenseFeatures": baseLicenseFeatures,
       "licenseTable": licenseTable,
       "licenseEntry": licenseEntry,
       "licenseStackId": licenseStackId,
       "licenseIndex": licenseIndex,
       "licenseName": licenseName,
       "licenseCustomer": licenseCustomer,
       "licenseQuantity": licenseQuantity,
       "licenseType": licenseType,
       "licenseIssueDate": licenseIssueDate,
       "licenseExpiryDate": licenseExpiryDate,
       "licenseFeatures": licenseFeatures,
       "licenseRowStatus": licenseRowStatus,
       "licenseFeatureTable": licenseFeatureTable,
       "licenseFeatureEntry": licenseFeatureEntry,
       "licenseFeatureIndex": licenseFeatureIndex,
       "licenseFeatureName": licenseFeatureName,
       "licenseFeatureStkMembers": licenseFeatureStkMembers,
       "licenseNew": licenseNew,
       "licenseNewStackId": licenseNewStackId,
       "licenseNewName": licenseNewName,
       "licenseNewKey": licenseNewKey,
       "licenseNewInstall": licenseNewInstall,
       "licenseNewInstallStatus": licenseNewInstallStatus,
       "licenseStackRemove": licenseStackRemove,
       "licenseStackRemoveName": licenseStackRemoveName,
       "licenseStackRemoveExecute": licenseStackRemoveExecute,
       "licenseStackRemoveStatus": licenseStackRemoveStatus}
)
