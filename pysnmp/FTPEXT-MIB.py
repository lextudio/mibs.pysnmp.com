# SNMP MIB module (FTPEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FTPEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:42 2024
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

(ftpExt,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "ftpExt")

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

ftpExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 30, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApFtpTable_Object = MibTable
apFtpTable = _ApFtpTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 30, 2)
)
if mibBuilder.loadTexts:
    apFtpTable.setStatus("current")
_ApFtpEntry_Object = MibTableRow
apFtpEntry = _ApFtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 30, 2, 1)
)
apFtpEntry.setIndexNames(
    (0, "FTPEXT-MIB", "apFtpRecordName"),
)
if mibBuilder.loadTexts:
    apFtpEntry.setStatus("current")


class _ApFtpRecordName_Type(DisplayString):
    """Custom type apFtpRecordName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ApFtpRecordName_Type.__name__ = "DisplayString"
_ApFtpRecordName_Object = MibTableColumn
apFtpRecordName = _ApFtpRecordName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 30, 2, 1, 1),
    _ApFtpRecordName_Type()
)
apFtpRecordName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apFtpRecordName.setStatus("current")
_ApFtpIpAddress_Type = IpAddress
_ApFtpIpAddress_Object = MibTableColumn
apFtpIpAddress = _ApFtpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 30, 2, 1, 2),
    _ApFtpIpAddress_Type()
)
apFtpIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apFtpIpAddress.setStatus("current")


class _ApFtpUserName_Type(DisplayString):
    """Custom type apFtpUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ApFtpUserName_Type.__name__ = "DisplayString"
_ApFtpUserName_Object = MibTableColumn
apFtpUserName = _ApFtpUserName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 30, 2, 1, 3),
    _ApFtpUserName_Type()
)
apFtpUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apFtpUserName.setStatus("current")


class _ApFtpPassword_Type(DisplayString):
    """Custom type apFtpPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ApFtpPassword_Type.__name__ = "DisplayString"
_ApFtpPassword_Object = MibTableColumn
apFtpPassword = _ApFtpPassword_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 30, 2, 1, 4),
    _ApFtpPassword_Type()
)
apFtpPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apFtpPassword.setStatus("current")


class _ApFtpEncryptedPassword_Type(DisplayString):
    """Custom type apFtpEncryptedPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApFtpEncryptedPassword_Type.__name__ = "DisplayString"
_ApFtpEncryptedPassword_Object = MibTableColumn
apFtpEncryptedPassword = _ApFtpEncryptedPassword_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 30, 2, 1, 5),
    _ApFtpEncryptedPassword_Type()
)
apFtpEncryptedPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apFtpEncryptedPassword.setStatus("current")


class _ApFtpBaseDirectory_Type(DisplayString):
    """Custom type apFtpBaseDirectory based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApFtpBaseDirectory_Type.__name__ = "DisplayString"
_ApFtpBaseDirectory_Object = MibTableColumn
apFtpBaseDirectory = _ApFtpBaseDirectory_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 30, 2, 1, 6),
    _ApFtpBaseDirectory_Type()
)
apFtpBaseDirectory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apFtpBaseDirectory.setStatus("current")
_ApFtpStatus_Type = RowStatus
_ApFtpStatus_Object = MibTableColumn
apFtpStatus = _ApFtpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 30, 2, 1, 7),
    _ApFtpStatus_Type()
)
apFtpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apFtpStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FTPEXT-MIB",
    **{"ftpExtMib": ftpExtMib,
       "apFtpTable": apFtpTable,
       "apFtpEntry": apFtpEntry,
       "apFtpRecordName": apFtpRecordName,
       "apFtpIpAddress": apFtpIpAddress,
       "apFtpUserName": apFtpUserName,
       "apFtpPassword": apFtpPassword,
       "apFtpEncryptedPassword": apFtpEncryptedPassword,
       "apFtpBaseDirectory": apFtpBaseDirectory,
       "apFtpStatus": apFtpStatus}
)
