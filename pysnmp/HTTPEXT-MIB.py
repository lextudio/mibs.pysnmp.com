# SNMP MIB module (HTTPEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HTTPEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:38 2024
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

(httpExt,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "httpExt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

httpExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 47, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApHttpTable_Object = MibTable
apHttpTable = _ApHttpTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 47, 2)
)
if mibBuilder.loadTexts:
    apHttpTable.setStatus("current")
_ApHttpEntry_Object = MibTableRow
apHttpEntry = _ApHttpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 47, 2, 1)
)
apHttpEntry.setIndexNames(
    (0, "HTTPEXT-MIB", "apHttpRecordName"),
)
if mibBuilder.loadTexts:
    apHttpEntry.setStatus("current")


class _ApHttpRecordName_Type(DisplayString):
    """Custom type apHttpRecordName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ApHttpRecordName_Type.__name__ = "DisplayString"
_ApHttpRecordName_Object = MibTableColumn
apHttpRecordName = _ApHttpRecordName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 47, 2, 1, 1),
    _ApHttpRecordName_Type()
)
apHttpRecordName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apHttpRecordName.setStatus("current")
_ApHttpIpAddress_Type = IpAddress
_ApHttpIpAddress_Object = MibTableColumn
apHttpIpAddress = _ApHttpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 47, 2, 1, 2),
    _ApHttpIpAddress_Type()
)
apHttpIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apHttpIpAddress.setStatus("current")
_ApHttpPort_Type = Integer32
_ApHttpPort_Object = MibTableColumn
apHttpPort = _ApHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 47, 2, 1, 3),
    _ApHttpPort_Type()
)
apHttpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apHttpPort.setStatus("current")


class _ApHttpUserName_Type(DisplayString):
    """Custom type apHttpUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ApHttpUserName_Type.__name__ = "DisplayString"
_ApHttpUserName_Object = MibTableColumn
apHttpUserName = _ApHttpUserName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 47, 2, 1, 4),
    _ApHttpUserName_Type()
)
apHttpUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apHttpUserName.setStatus("current")


class _ApHttpPassword_Type(DisplayString):
    """Custom type apHttpPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ApHttpPassword_Type.__name__ = "DisplayString"
_ApHttpPassword_Object = MibTableColumn
apHttpPassword = _ApHttpPassword_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 47, 2, 1, 5),
    _ApHttpPassword_Type()
)
apHttpPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apHttpPassword.setStatus("current")


class _ApHttpEncryptedPassword_Type(DisplayString):
    """Custom type apHttpEncryptedPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApHttpEncryptedPassword_Type.__name__ = "DisplayString"
_ApHttpEncryptedPassword_Object = MibTableColumn
apHttpEncryptedPassword = _ApHttpEncryptedPassword_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 47, 2, 1, 6),
    _ApHttpEncryptedPassword_Type()
)
apHttpEncryptedPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apHttpEncryptedPassword.setStatus("current")


class _ApHttpBaseDirectory_Type(DisplayString):
    """Custom type apHttpBaseDirectory based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApHttpBaseDirectory_Type.__name__ = "DisplayString"
_ApHttpBaseDirectory_Object = MibTableColumn
apHttpBaseDirectory = _ApHttpBaseDirectory_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 47, 2, 1, 7),
    _ApHttpBaseDirectory_Type()
)
apHttpBaseDirectory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apHttpBaseDirectory.setStatus("current")
_ApHttpStatus_Type = RowStatus
_ApHttpStatus_Object = MibTableColumn
apHttpStatus = _ApHttpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 47, 2, 1, 8),
    _ApHttpStatus_Type()
)
apHttpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apHttpStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HTTPEXT-MIB",
    **{"httpExtMib": httpExtMib,
       "apHttpTable": apHttpTable,
       "apHttpEntry": apHttpEntry,
       "apHttpRecordName": apHttpRecordName,
       "apHttpIpAddress": apHttpIpAddress,
       "apHttpPort": apHttpPort,
       "apHttpUserName": apHttpUserName,
       "apHttpPassword": apHttpPassword,
       "apHttpEncryptedPassword": apHttpEncryptedPassword,
       "apHttpBaseDirectory": apHttpBaseDirectory,
       "apHttpStatus": apHttpStatus}
)
