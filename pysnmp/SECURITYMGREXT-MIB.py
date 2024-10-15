# SNMP MIB module (SECURITYMGREXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SECURITYMGREXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:50:16 2024
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

(securityMgrExt,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "securityMgrExt")

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

securityMgrExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 13, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _ApSecurityMgrConsoleAuthType_Type(Integer32):
    """Custom type apSecurityMgrConsoleAuthType based on Integer32"""
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
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("enable-none", 6),
          ("enable-radius", 5),
          ("enable-radius-none", 9),
          ("none", 3),
          ("radius", 2),
          ("radius-enable", 4),
          ("radius-enable-none", 8),
          ("radius-none", 7))
    )


_ApSecurityMgrConsoleAuthType_Type.__name__ = "Integer32"
_ApSecurityMgrConsoleAuthType_Object = MibScalar
apSecurityMgrConsoleAuthType = _ApSecurityMgrConsoleAuthType_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 13, 2),
    _ApSecurityMgrConsoleAuthType_Type()
)
apSecurityMgrConsoleAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSecurityMgrConsoleAuthType.setStatus("current")


class _ApSecurityMgrVirtualAuthType_Type(Integer32):
    """Custom type apSecurityMgrVirtualAuthType based on Integer32"""
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
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("disallowed", 10),
          ("enable", 1),
          ("enable-none", 6),
          ("enable-radius", 5),
          ("enable-radius-none", 9),
          ("none", 3),
          ("radius", 2),
          ("radius-enable", 4),
          ("radius-enable-none", 8),
          ("radius-none", 7))
    )


_ApSecurityMgrVirtualAuthType_Type.__name__ = "Integer32"
_ApSecurityMgrVirtualAuthType_Object = MibScalar
apSecurityMgrVirtualAuthType = _ApSecurityMgrVirtualAuthType_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 13, 3),
    _ApSecurityMgrVirtualAuthType_Type()
)
apSecurityMgrVirtualAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSecurityMgrVirtualAuthType.setStatus("current")
_ApSecurityMgrUsernameTable_Object = MibTable
apSecurityMgrUsernameTable = _ApSecurityMgrUsernameTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 13, 4)
)
if mibBuilder.loadTexts:
    apSecurityMgrUsernameTable.setStatus("current")
_ApSecurityMgrUsernameEntry_Object = MibTableRow
apSecurityMgrUsernameEntry = _ApSecurityMgrUsernameEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 13, 4, 1)
)
apSecurityMgrUsernameEntry.setIndexNames(
    (0, "SECURITYMGREXT-MIB", "apSecurityMgrUsername"),
)
if mibBuilder.loadTexts:
    apSecurityMgrUsernameEntry.setStatus("current")


class _ApSecurityMgrUsername_Type(DisplayString):
    """Custom type apSecurityMgrUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_ApSecurityMgrUsername_Type.__name__ = "DisplayString"
_ApSecurityMgrUsername_Object = MibTableColumn
apSecurityMgrUsername = _ApSecurityMgrUsername_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 13, 4, 1, 1),
    _ApSecurityMgrUsername_Type()
)
apSecurityMgrUsername.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSecurityMgrUsername.setStatus("current")


class _ApSecurityMgrPassword_Type(DisplayString):
    """Custom type apSecurityMgrPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 16),
    )


_ApSecurityMgrPassword_Type.__name__ = "DisplayString"
_ApSecurityMgrPassword_Object = MibTableColumn
apSecurityMgrPassword = _ApSecurityMgrPassword_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 13, 4, 1, 2),
    _ApSecurityMgrPassword_Type()
)
apSecurityMgrPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSecurityMgrPassword.setStatus("current")


class _ApSecurityMgrEncryptedPassword_Type(DisplayString):
    """Custom type apSecurityMgrEncryptedPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 64),
    )


_ApSecurityMgrEncryptedPassword_Type.__name__ = "DisplayString"
_ApSecurityMgrEncryptedPassword_Object = MibTableColumn
apSecurityMgrEncryptedPassword = _ApSecurityMgrEncryptedPassword_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 13, 4, 1, 3),
    _ApSecurityMgrEncryptedPassword_Type()
)
apSecurityMgrEncryptedPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSecurityMgrEncryptedPassword.setStatus("current")


class _ApSecurityMgrUserPriviledgeLevel_Type(Integer32):
    """Custom type apSecurityMgrUserPriviledgeLevel based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("non-priviledge", 1),
          ("priviledge", 2))
    )


_ApSecurityMgrUserPriviledgeLevel_Type.__name__ = "Integer32"
_ApSecurityMgrUserPriviledgeLevel_Object = MibTableColumn
apSecurityMgrUserPriviledgeLevel = _ApSecurityMgrUserPriviledgeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 13, 4, 1, 4),
    _ApSecurityMgrUserPriviledgeLevel_Type()
)
apSecurityMgrUserPriviledgeLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSecurityMgrUserPriviledgeLevel.setStatus("current")
_ApSecurityMgrStatus_Type = RowStatus
_ApSecurityMgrStatus_Object = MibTableColumn
apSecurityMgrStatus = _ApSecurityMgrStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 13, 4, 1, 5),
    _ApSecurityMgrStatus_Type()
)
apSecurityMgrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSecurityMgrStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SECURITYMGREXT-MIB",
    **{"securityMgrExtMib": securityMgrExtMib,
       "apSecurityMgrConsoleAuthType": apSecurityMgrConsoleAuthType,
       "apSecurityMgrVirtualAuthType": apSecurityMgrVirtualAuthType,
       "apSecurityMgrUsernameTable": apSecurityMgrUsernameTable,
       "apSecurityMgrUsernameEntry": apSecurityMgrUsernameEntry,
       "apSecurityMgrUsername": apSecurityMgrUsername,
       "apSecurityMgrPassword": apSecurityMgrPassword,
       "apSecurityMgrEncryptedPassword": apSecurityMgrEncryptedPassword,
       "apSecurityMgrUserPriviledgeLevel": apSecurityMgrUserPriviledgeLevel,
       "apSecurityMgrStatus": apSecurityMgrStatus}
)
