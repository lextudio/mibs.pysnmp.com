# SNMP MIB module (INTEL-VAS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTEL-VAS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:01 2024
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

(mib2ext,) = mibBuilder.importSymbols(
    "INTEL-GEN-MIB",
    "mib2ext")

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

_Vas_ObjectIdentity = ObjectIdentity
vas = _Vas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 53)
)
_VasConfig_ObjectIdentity = ObjectIdentity
vasConfig = _VasConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 53, 1)
)
_VasConfigTable_Object = MibTable
vasConfigTable = _VasConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 53, 1, 1)
)
if mibBuilder.loadTexts:
    vasConfigTable.setStatus("mandatory")
_VasConfigEntry_Object = MibTableRow
vasConfigEntry = _VasConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 53, 1, 1, 1)
)
vasConfigEntry.setIndexNames(
    (0, "INTEL-VAS-MIB", "vasConfigIndex"),
)
if mibBuilder.loadTexts:
    vasConfigEntry.setStatus("mandatory")
_VasConfigIndex_Type = Integer32
_VasConfigIndex_Object = MibTableColumn
vasConfigIndex = _VasConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 53, 1, 1, 1, 1),
    _VasConfigIndex_Type()
)
vasConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasConfigIndex.setStatus("mandatory")
_VasConfigStatus_Type = Integer32
_VasConfigStatus_Object = MibTableColumn
vasConfigStatus = _VasConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 53, 1, 1, 1, 2),
    _VasConfigStatus_Type()
)
vasConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasConfigStatus.setStatus("mandatory")


class _VasConfigLicenseKey_Type(DisplayString):
    """Custom type vasConfigLicenseKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_VasConfigLicenseKey_Type.__name__ = "DisplayString"
_VasConfigLicenseKey_Object = MibTableColumn
vasConfigLicenseKey = _VasConfigLicenseKey_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 53, 1, 1, 1, 3),
    _VasConfigLicenseKey_Type()
)
vasConfigLicenseKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vasConfigLicenseKey.setStatus("mandatory")


class _VasConfigNameOfLicense_Type(DisplayString):
    """Custom type vasConfigNameOfLicense based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_VasConfigNameOfLicense_Type.__name__ = "DisplayString"
_VasConfigNameOfLicense_Object = MibTableColumn
vasConfigNameOfLicense = _VasConfigNameOfLicense_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 53, 1, 1, 1, 4),
    _VasConfigNameOfLicense_Type()
)
vasConfigNameOfLicense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasConfigNameOfLicense.setStatus("mandatory")
_VasConfigEraseLicense_Type = Integer32
_VasConfigEraseLicense_Object = MibTableColumn
vasConfigEraseLicense = _VasConfigEraseLicense_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 53, 1, 1, 1, 5),
    _VasConfigEraseLicense_Type()
)
vasConfigEraseLicense.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vasConfigEraseLicense.setStatus("mandatory")
_VasConfigDemoLicenseKey_Type = Integer32
_VasConfigDemoLicenseKey_Object = MibTableColumn
vasConfigDemoLicenseKey = _VasConfigDemoLicenseKey_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 53, 1, 1, 1, 6),
    _VasConfigDemoLicenseKey_Type()
)
vasConfigDemoLicenseKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasConfigDemoLicenseKey.setStatus("mandatory")


class _VasConfigNameOfUser_Type(DisplayString):
    """Custom type vasConfigNameOfUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_VasConfigNameOfUser_Type.__name__ = "DisplayString"
_VasConfigNameOfUser_Object = MibTableColumn
vasConfigNameOfUser = _VasConfigNameOfUser_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 53, 1, 1, 1, 7),
    _VasConfigNameOfUser_Type()
)
vasConfigNameOfUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vasConfigNameOfUser.setStatus("mandatory")


class _VasConfigDateOfIssue_Type(DisplayString):
    """Custom type vasConfigDateOfIssue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_VasConfigDateOfIssue_Type.__name__ = "DisplayString"
_VasConfigDateOfIssue_Object = MibTableColumn
vasConfigDateOfIssue = _VasConfigDateOfIssue_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 53, 1, 1, 1, 8),
    _VasConfigDateOfIssue_Type()
)
vasConfigDateOfIssue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasConfigDateOfIssue.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTEL-VAS-MIB",
    **{"vas": vas,
       "vasConfig": vasConfig,
       "vasConfigTable": vasConfigTable,
       "vasConfigEntry": vasConfigEntry,
       "vasConfigIndex": vasConfigIndex,
       "vasConfigStatus": vasConfigStatus,
       "vasConfigLicenseKey": vasConfigLicenseKey,
       "vasConfigNameOfLicense": vasConfigNameOfLicense,
       "vasConfigEraseLicense": vasConfigEraseLicense,
       "vasConfigDemoLicenseKey": vasConfigDemoLicenseKey,
       "vasConfigNameOfUser": vasConfigNameOfUser,
       "vasConfigDateOfIssue": vasConfigDateOfIssue}
)
