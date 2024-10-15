# SNMP MIB module (ANS-ADMIN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ANS-ADMIN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:55 2024
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

(RowPointer,
 RowStatus,
 mlpmpR115) = mibBuilder.importSymbols(
    "ANS-COMMON-MIB",
    "RowPointer",
    "RowStatus",
    "mlpmpR115")

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

_AdminServices_ObjectIdentity = ObjectIdentity
adminServices = _AdminServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 6)
)
_AnsLicense_ObjectIdentity = ObjectIdentity
ansLicense = _AnsLicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 6, 1)
)
_AnsLicenseTable_Object = MibTable
ansLicenseTable = _AnsLicenseTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 6, 1, 1)
)
if mibBuilder.loadTexts:
    ansLicenseTable.setStatus("mandatory")
_AnsLicenseEntry_Object = MibTableRow
ansLicenseEntry = _AnsLicenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 6, 1, 1, 1)
)
ansLicenseEntry.setIndexNames(
    (0, "ANS-ADMIN-MIB", "ansLicenseId"),
)
if mibBuilder.loadTexts:
    ansLicenseEntry.setStatus("mandatory")
_AnsLicenseId_Type = Integer32
_AnsLicenseId_Object = MibTableColumn
ansLicenseId = _AnsLicenseId_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 6, 1, 1, 1, 1),
    _AnsLicenseId_Type()
)
ansLicenseId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansLicenseId.setStatus("mandatory")
_AnsLicenseName_Type = DisplayString
_AnsLicenseName_Object = MibTableColumn
ansLicenseName = _AnsLicenseName_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 6, 1, 1, 1, 2),
    _AnsLicenseName_Type()
)
ansLicenseName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansLicenseName.setStatus("mandatory")
_AnsLicenseCapacity_Type = Integer32
_AnsLicenseCapacity_Object = MibTableColumn
ansLicenseCapacity = _AnsLicenseCapacity_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 6, 1, 1, 1, 3),
    _AnsLicenseCapacity_Type()
)
ansLicenseCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansLicenseCapacity.setStatus("mandatory")
_AnsLicenseCurrentCapacity_Type = Integer32
_AnsLicenseCurrentCapacity_Object = MibTableColumn
ansLicenseCurrentCapacity = _AnsLicenseCurrentCapacity_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 6, 1, 1, 1, 4),
    _AnsLicenseCurrentCapacity_Type()
)
ansLicenseCurrentCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansLicenseCurrentCapacity.setStatus("mandatory")
_AnsLicenseExpirationDate_Type = DisplayString
_AnsLicenseExpirationDate_Object = MibTableColumn
ansLicenseExpirationDate = _AnsLicenseExpirationDate_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 6, 1, 1, 1, 5),
    _AnsLicenseExpirationDate_Type()
)
ansLicenseExpirationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansLicenseExpirationDate.setStatus("mandatory")
_AnsLicenseInstall_Type = DisplayString
_AnsLicenseInstall_Object = MibTableColumn
ansLicenseInstall = _AnsLicenseInstall_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 6, 1, 1, 1, 6),
    _AnsLicenseInstall_Type()
)
ansLicenseInstall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansLicenseInstall.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ANS-ADMIN-MIB",
    **{"adminServices": adminServices,
       "ansLicense": ansLicense,
       "ansLicenseTable": ansLicenseTable,
       "ansLicenseEntry": ansLicenseEntry,
       "ansLicenseId": ansLicenseId,
       "ansLicenseName": ansLicenseName,
       "ansLicenseCapacity": ansLicenseCapacity,
       "ansLicenseCurrentCapacity": ansLicenseCurrentCapacity,
       "ansLicenseExpirationDate": ansLicenseExpirationDate,
       "ansLicenseInstall": ansLicenseInstall}
)
