# SNMP MIB module (XYLAN-BACKUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYLAN-BACKUP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:18:56 2024
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

(xylanBackupArch,) = mibBuilder.importSymbols(
    "XYLAN-BASE-MIB",
    "xylanBackupArch")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BackupxConfigGroup_ObjectIdentity = ObjectIdentity
backupxConfigGroup = _BackupxConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 16, 1)
)
_BackupxConfigTable_Object = MibTable
backupxConfigTable = _BackupxConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 16, 1, 1)
)
if mibBuilder.loadTexts:
    backupxConfigTable.setStatus("mandatory")
_BackupxConfigEntry_Object = MibTableRow
backupxConfigEntry = _BackupxConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 16, 1, 1, 1)
)
backupxConfigEntry.setIndexNames(
    (0, "XYLAN-BACKUP-MIB", "backupxConfigID"),
)
if mibBuilder.loadTexts:
    backupxConfigEntry.setStatus("mandatory")
_BackupxConfigID_Type = Integer32
_BackupxConfigID_Object = MibTableColumn
backupxConfigID = _BackupxConfigID_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 16, 1, 1, 1, 1),
    _BackupxConfigID_Type()
)
backupxConfigID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupxConfigID.setStatus("mandatory")


class _BackupxConfigDescription_Type(DisplayString):
    """Custom type backupxConfigDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_BackupxConfigDescription_Type.__name__ = "DisplayString"
_BackupxConfigDescription_Object = MibTableColumn
backupxConfigDescription = _BackupxConfigDescription_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 16, 1, 1, 1, 2),
    _BackupxConfigDescription_Type()
)
backupxConfigDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupxConfigDescription.setStatus("mandatory")


class _BackupxConfigAdminStatus_Type(Integer32):
    """Custom type backupxConfigAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("disabled", 2),
          ("enabled", 1))
    )


_BackupxConfigAdminStatus_Type.__name__ = "Integer32"
_BackupxConfigAdminStatus_Object = MibTableColumn
backupxConfigAdminStatus = _BackupxConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 16, 1, 1, 1, 3),
    _BackupxConfigAdminStatus_Type()
)
backupxConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupxConfigAdminStatus.setStatus("mandatory")


class _BackupxConfigPrimaryType_Type(Integer32):
    """Custom type backupxConfigPrimaryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("frameRelayPvcDlci", 2),
          ("physicalPort", 1))
    )


_BackupxConfigPrimaryType_Type.__name__ = "Integer32"
_BackupxConfigPrimaryType_Object = MibTableColumn
backupxConfigPrimaryType = _BackupxConfigPrimaryType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 16, 1, 1, 1, 4),
    _BackupxConfigPrimaryType_Type()
)
backupxConfigPrimaryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupxConfigPrimaryType.setStatus("mandatory")
_BackupxConfigPrimaryIndex1_Type = Integer32
_BackupxConfigPrimaryIndex1_Object = MibTableColumn
backupxConfigPrimaryIndex1 = _BackupxConfigPrimaryIndex1_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 16, 1, 1, 1, 5),
    _BackupxConfigPrimaryIndex1_Type()
)
backupxConfigPrimaryIndex1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupxConfigPrimaryIndex1.setStatus("mandatory")
_BackupxConfigPrimaryIndex2_Type = Integer32
_BackupxConfigPrimaryIndex2_Object = MibTableColumn
backupxConfigPrimaryIndex2 = _BackupxConfigPrimaryIndex2_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 16, 1, 1, 1, 6),
    _BackupxConfigPrimaryIndex2_Type()
)
backupxConfigPrimaryIndex2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupxConfigPrimaryIndex2.setStatus("mandatory")
_BackupxConfigPrimaryIndex3_Type = Integer32
_BackupxConfigPrimaryIndex3_Object = MibTableColumn
backupxConfigPrimaryIndex3 = _BackupxConfigPrimaryIndex3_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 16, 1, 1, 1, 7),
    _BackupxConfigPrimaryIndex3_Type()
)
backupxConfigPrimaryIndex3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupxConfigPrimaryIndex3.setStatus("mandatory")


class _BackupxConfigBackupType_Type(Integer32):
    """Custom type backupxConfigBackupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("pppPeer", 1)
    )


_BackupxConfigBackupType_Type.__name__ = "Integer32"
_BackupxConfigBackupType_Object = MibTableColumn
backupxConfigBackupType = _BackupxConfigBackupType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 16, 1, 1, 1, 8),
    _BackupxConfigBackupType_Type()
)
backupxConfigBackupType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupxConfigBackupType.setStatus("mandatory")
_BackupxConfigBackupIndex1_Type = Integer32
_BackupxConfigBackupIndex1_Object = MibTableColumn
backupxConfigBackupIndex1 = _BackupxConfigBackupIndex1_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 16, 1, 1, 1, 9),
    _BackupxConfigBackupIndex1_Type()
)
backupxConfigBackupIndex1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupxConfigBackupIndex1.setStatus("mandatory")
_BackupxConfigBackupIndex2_Type = Integer32
_BackupxConfigBackupIndex2_Object = MibTableColumn
backupxConfigBackupIndex2 = _BackupxConfigBackupIndex2_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 16, 1, 1, 1, 10),
    _BackupxConfigBackupIndex2_Type()
)
backupxConfigBackupIndex2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupxConfigBackupIndex2.setStatus("mandatory")
_BackupxConfigBackupIndex3_Type = Integer32
_BackupxConfigBackupIndex3_Object = MibTableColumn
backupxConfigBackupIndex3 = _BackupxConfigBackupIndex3_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 16, 1, 1, 1, 11),
    _BackupxConfigBackupIndex3_Type()
)
backupxConfigBackupIndex3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupxConfigBackupIndex3.setStatus("mandatory")


class _BackupxConfigStartupTimeout_Type(Integer32):
    """Custom type backupxConfigStartupTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BackupxConfigStartupTimeout_Type.__name__ = "Integer32"
_BackupxConfigStartupTimeout_Object = MibTableColumn
backupxConfigStartupTimeout = _BackupxConfigStartupTimeout_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 16, 1, 1, 1, 12),
    _BackupxConfigStartupTimeout_Type()
)
backupxConfigStartupTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupxConfigStartupTimeout.setStatus("mandatory")


class _BackupxConfigActivateTimeout_Type(Integer32):
    """Custom type backupxConfigActivateTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BackupxConfigActivateTimeout_Type.__name__ = "Integer32"
_BackupxConfigActivateTimeout_Object = MibTableColumn
backupxConfigActivateTimeout = _BackupxConfigActivateTimeout_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 16, 1, 1, 1, 13),
    _BackupxConfigActivateTimeout_Type()
)
backupxConfigActivateTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupxConfigActivateTimeout.setStatus("mandatory")


class _BackupxConfigRestoreTimeout_Type(Integer32):
    """Custom type backupxConfigRestoreTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BackupxConfigRestoreTimeout_Type.__name__ = "Integer32"
_BackupxConfigRestoreTimeout_Object = MibTableColumn
backupxConfigRestoreTimeout = _BackupxConfigRestoreTimeout_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 16, 1, 1, 1, 14),
    _BackupxConfigRestoreTimeout_Type()
)
backupxConfigRestoreTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupxConfigRestoreTimeout.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYLAN-BACKUP-MIB",
    **{"backupxConfigGroup": backupxConfigGroup,
       "backupxConfigTable": backupxConfigTable,
       "backupxConfigEntry": backupxConfigEntry,
       "backupxConfigID": backupxConfigID,
       "backupxConfigDescription": backupxConfigDescription,
       "backupxConfigAdminStatus": backupxConfigAdminStatus,
       "backupxConfigPrimaryType": backupxConfigPrimaryType,
       "backupxConfigPrimaryIndex1": backupxConfigPrimaryIndex1,
       "backupxConfigPrimaryIndex2": backupxConfigPrimaryIndex2,
       "backupxConfigPrimaryIndex3": backupxConfigPrimaryIndex3,
       "backupxConfigBackupType": backupxConfigBackupType,
       "backupxConfigBackupIndex1": backupxConfigBackupIndex1,
       "backupxConfigBackupIndex2": backupxConfigBackupIndex2,
       "backupxConfigBackupIndex3": backupxConfigBackupIndex3,
       "backupxConfigStartupTimeout": backupxConfigStartupTimeout,
       "backupxConfigActivateTimeout": backupxConfigActivateTimeout,
       "backupxConfigRestoreTimeout": backupxConfigRestoreTimeout}
)
