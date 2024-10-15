# SNMP MIB module (DSLAM-BACKUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DSLAM-BACKUP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:33:38 2024
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

(AtmVcIdentifier,
 AtmVorXOperStatus,
 AtmVpIdentifier) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmVcIdentifier",
    "AtmVorXOperStatus",
    "AtmVpIdentifier")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(pgainDSLAM,) = mibBuilder.importSymbols(
    "PAIRGAIN-COMMON-HD-MIB",
    "pgainDSLAM")

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

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

pgBackupMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 19)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PgBackupObjects_ObjectIdentity = ObjectIdentity
pgBackupObjects = _PgBackupObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 19, 1)
)
_PgBackupPortTable_Object = MibTable
pgBackupPortTable = _PgBackupPortTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 19, 1, 1)
)
if mibBuilder.loadTexts:
    pgBackupPortTable.setStatus("current")
_PgBackupPortEntry_Object = MibTableRow
pgBackupPortEntry = _PgBackupPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 19, 1, 1, 1)
)
pgBackupPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pgBackupPortEntry.setStatus("current")


class _PgBackupPortAdminStatus_Type(Integer32):
    """Custom type pgBackupPortAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_PgBackupPortAdminStatus_Type.__name__ = "Integer32"
_PgBackupPortAdminStatus_Object = MibTableColumn
pgBackupPortAdminStatus = _PgBackupPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 19, 1, 1, 1, 1),
    _PgBackupPortAdminStatus_Type()
)
pgBackupPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgBackupPortAdminStatus.setStatus("current")
_PgBackupVpTable_Object = MibTable
pgBackupVpTable = _PgBackupVpTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 19, 1, 2)
)
if mibBuilder.loadTexts:
    pgBackupVpTable.setStatus("current")
_PgBackupVpEntry_Object = MibTableRow
pgBackupVpEntry = _PgBackupVpEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 19, 1, 2, 1)
)
pgBackupVpEntry.setIndexNames(
    (0, "DSLAM-BACKUP-MIB", "pgBackupVpPrimaryIfIndex"),
    (0, "DSLAM-BACKUP-MIB", "pgBackupVpPrimaryVpi"),
    (0, "DSLAM-BACKUP-MIB", "pgBackupVpSecondaryIfIndex"),
    (0, "DSLAM-BACKUP-MIB", "pgBackupVpSecondaryVpi"),
)
if mibBuilder.loadTexts:
    pgBackupVpEntry.setStatus("current")
_PgBackupVpPrimaryIfIndex_Type = InterfaceIndex
_PgBackupVpPrimaryIfIndex_Object = MibTableColumn
pgBackupVpPrimaryIfIndex = _PgBackupVpPrimaryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 19, 1, 2, 1, 1),
    _PgBackupVpPrimaryIfIndex_Type()
)
pgBackupVpPrimaryIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pgBackupVpPrimaryIfIndex.setStatus("current")
_PgBackupVpPrimaryVpi_Type = AtmVpIdentifier
_PgBackupVpPrimaryVpi_Object = MibTableColumn
pgBackupVpPrimaryVpi = _PgBackupVpPrimaryVpi_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 19, 1, 2, 1, 2),
    _PgBackupVpPrimaryVpi_Type()
)
pgBackupVpPrimaryVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pgBackupVpPrimaryVpi.setStatus("current")
_PgBackupVpSecondaryIfIndex_Type = InterfaceIndex
_PgBackupVpSecondaryIfIndex_Object = MibTableColumn
pgBackupVpSecondaryIfIndex = _PgBackupVpSecondaryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 19, 1, 2, 1, 3),
    _PgBackupVpSecondaryIfIndex_Type()
)
pgBackupVpSecondaryIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pgBackupVpSecondaryIfIndex.setStatus("current")
_PgBackupVpSecondaryVpi_Type = AtmVpIdentifier
_PgBackupVpSecondaryVpi_Object = MibTableColumn
pgBackupVpSecondaryVpi = _PgBackupVpSecondaryVpi_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 19, 1, 2, 1, 4),
    _PgBackupVpSecondaryVpi_Type()
)
pgBackupVpSecondaryVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pgBackupVpSecondaryVpi.setStatus("current")


class _PgBackupVpRowStatus_Type(RowStatus):
    """Custom type pgBackupVpRowStatus based on RowStatus"""


_PgBackupVpRowStatus_Object = MibTableColumn
pgBackupVpRowStatus = _PgBackupVpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 19, 1, 2, 1, 5),
    _PgBackupVpRowStatus_Type()
)
pgBackupVpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pgBackupVpRowStatus.setStatus("current")


class _PgBackupVpPrimaryAdminStatus_Type(Integer32):
    """Custom type pgBackupVpPrimaryAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_PgBackupVpPrimaryAdminStatus_Type.__name__ = "Integer32"
_PgBackupVpPrimaryAdminStatus_Object = MibTableColumn
pgBackupVpPrimaryAdminStatus = _PgBackupVpPrimaryAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 19, 1, 2, 1, 6),
    _PgBackupVpPrimaryAdminStatus_Type()
)
pgBackupVpPrimaryAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgBackupVpPrimaryAdminStatus.setStatus("current")
_PgBackupVpPrimaryOperStatus_Type = AtmVorXOperStatus
_PgBackupVpPrimaryOperStatus_Object = MibTableColumn
pgBackupVpPrimaryOperStatus = _PgBackupVpPrimaryOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 19, 1, 2, 1, 7),
    _PgBackupVpPrimaryOperStatus_Type()
)
pgBackupVpPrimaryOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgBackupVpPrimaryOperStatus.setStatus("current")
_PgBackupVpSecondaryOperStatus_Type = AtmVorXOperStatus
_PgBackupVpSecondaryOperStatus_Object = MibTableColumn
pgBackupVpSecondaryOperStatus = _PgBackupVpSecondaryOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 19, 1, 2, 1, 8),
    _PgBackupVpSecondaryOperStatus_Type()
)
pgBackupVpSecondaryOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgBackupVpSecondaryOperStatus.setStatus("current")


class _PgBackupVpSwitchTimes_Type(Integer32):
    """Custom type pgBackupVpSwitchTimes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PgBackupVpSwitchTimes_Type.__name__ = "Integer32"
_PgBackupVpSwitchTimes_Object = MibTableColumn
pgBackupVpSwitchTimes = _PgBackupVpSwitchTimes_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 19, 1, 2, 1, 9),
    _PgBackupVpSwitchTimes_Type()
)
pgBackupVpSwitchTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgBackupVpSwitchTimes.setStatus("current")
_PgBackupVcTable_Object = MibTable
pgBackupVcTable = _PgBackupVcTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 19, 1, 3)
)
if mibBuilder.loadTexts:
    pgBackupVcTable.setStatus("current")
_PgBackupVcEntry_Object = MibTableRow
pgBackupVcEntry = _PgBackupVcEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 19, 1, 3, 1)
)
pgBackupVcEntry.setIndexNames(
    (0, "DSLAM-BACKUP-MIB", "pgBackupVcPrimaryIfIndex"),
    (0, "DSLAM-BACKUP-MIB", "pgBackupVcPrimaryVpi"),
    (0, "DSLAM-BACKUP-MIB", "pgBackupVcPrimaryVci"),
    (0, "DSLAM-BACKUP-MIB", "pgBackupVcSecondaryIfIndex"),
    (0, "DSLAM-BACKUP-MIB", "pgBackupVcSecondaryVpi"),
    (0, "DSLAM-BACKUP-MIB", "pgBackupVcSecondaryVci"),
)
if mibBuilder.loadTexts:
    pgBackupVcEntry.setStatus("current")
_PgBackupVcPrimaryIfIndex_Type = InterfaceIndex
_PgBackupVcPrimaryIfIndex_Object = MibTableColumn
pgBackupVcPrimaryIfIndex = _PgBackupVcPrimaryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 19, 1, 3, 1, 1),
    _PgBackupVcPrimaryIfIndex_Type()
)
pgBackupVcPrimaryIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pgBackupVcPrimaryIfIndex.setStatus("current")
_PgBackupVcPrimaryVpi_Type = AtmVpIdentifier
_PgBackupVcPrimaryVpi_Object = MibTableColumn
pgBackupVcPrimaryVpi = _PgBackupVcPrimaryVpi_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 19, 1, 3, 1, 2),
    _PgBackupVcPrimaryVpi_Type()
)
pgBackupVcPrimaryVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pgBackupVcPrimaryVpi.setStatus("current")
_PgBackupVcPrimaryVci_Type = AtmVcIdentifier
_PgBackupVcPrimaryVci_Object = MibTableColumn
pgBackupVcPrimaryVci = _PgBackupVcPrimaryVci_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 19, 1, 3, 1, 3),
    _PgBackupVcPrimaryVci_Type()
)
pgBackupVcPrimaryVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pgBackupVcPrimaryVci.setStatus("current")
_PgBackupVcSecondaryIfIndex_Type = InterfaceIndex
_PgBackupVcSecondaryIfIndex_Object = MibTableColumn
pgBackupVcSecondaryIfIndex = _PgBackupVcSecondaryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 19, 1, 3, 1, 4),
    _PgBackupVcSecondaryIfIndex_Type()
)
pgBackupVcSecondaryIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pgBackupVcSecondaryIfIndex.setStatus("current")
_PgBackupVcSecondaryVpi_Type = AtmVpIdentifier
_PgBackupVcSecondaryVpi_Object = MibTableColumn
pgBackupVcSecondaryVpi = _PgBackupVcSecondaryVpi_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 19, 1, 3, 1, 5),
    _PgBackupVcSecondaryVpi_Type()
)
pgBackupVcSecondaryVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pgBackupVcSecondaryVpi.setStatus("current")
_PgBackupVcSecondaryVci_Type = AtmVcIdentifier
_PgBackupVcSecondaryVci_Object = MibTableColumn
pgBackupVcSecondaryVci = _PgBackupVcSecondaryVci_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 19, 1, 3, 1, 6),
    _PgBackupVcSecondaryVci_Type()
)
pgBackupVcSecondaryVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pgBackupVcSecondaryVci.setStatus("current")


class _PgBackupVcRowStatus_Type(RowStatus):
    """Custom type pgBackupVcRowStatus based on RowStatus"""


_PgBackupVcRowStatus_Object = MibTableColumn
pgBackupVcRowStatus = _PgBackupVcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 19, 1, 3, 1, 7),
    _PgBackupVcRowStatus_Type()
)
pgBackupVcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pgBackupVcRowStatus.setStatus("current")


class _PgBackupVcPrimaryAdminStatus_Type(Integer32):
    """Custom type pgBackupVcPrimaryAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_PgBackupVcPrimaryAdminStatus_Type.__name__ = "Integer32"
_PgBackupVcPrimaryAdminStatus_Object = MibTableColumn
pgBackupVcPrimaryAdminStatus = _PgBackupVcPrimaryAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 19, 1, 3, 1, 8),
    _PgBackupVcPrimaryAdminStatus_Type()
)
pgBackupVcPrimaryAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgBackupVcPrimaryAdminStatus.setStatus("current")
_PgBackupVcPrimaryOperStatus_Type = AtmVorXOperStatus
_PgBackupVcPrimaryOperStatus_Object = MibTableColumn
pgBackupVcPrimaryOperStatus = _PgBackupVcPrimaryOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 19, 1, 3, 1, 9),
    _PgBackupVcPrimaryOperStatus_Type()
)
pgBackupVcPrimaryOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgBackupVcPrimaryOperStatus.setStatus("current")
_PgBackupVcSecondaryOperStatus_Type = AtmVorXOperStatus
_PgBackupVcSecondaryOperStatus_Object = MibTableColumn
pgBackupVcSecondaryOperStatus = _PgBackupVcSecondaryOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 19, 1, 3, 1, 10),
    _PgBackupVcSecondaryOperStatus_Type()
)
pgBackupVcSecondaryOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgBackupVcSecondaryOperStatus.setStatus("current")


class _PgBackupVcSwitchTimes_Type(Integer32):
    """Custom type pgBackupVcSwitchTimes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PgBackupVcSwitchTimes_Type.__name__ = "Integer32"
_PgBackupVcSwitchTimes_Object = MibTableColumn
pgBackupVcSwitchTimes = _PgBackupVcSwitchTimes_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 19, 1, 3, 1, 11),
    _PgBackupVcSwitchTimes_Type()
)
pgBackupVcSwitchTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgBackupVcSwitchTimes.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DSLAM-BACKUP-MIB",
    **{"pgBackupMIB": pgBackupMIB,
       "pgBackupObjects": pgBackupObjects,
       "pgBackupPortTable": pgBackupPortTable,
       "pgBackupPortEntry": pgBackupPortEntry,
       "pgBackupPortAdminStatus": pgBackupPortAdminStatus,
       "pgBackupVpTable": pgBackupVpTable,
       "pgBackupVpEntry": pgBackupVpEntry,
       "pgBackupVpPrimaryIfIndex": pgBackupVpPrimaryIfIndex,
       "pgBackupVpPrimaryVpi": pgBackupVpPrimaryVpi,
       "pgBackupVpSecondaryIfIndex": pgBackupVpSecondaryIfIndex,
       "pgBackupVpSecondaryVpi": pgBackupVpSecondaryVpi,
       "pgBackupVpRowStatus": pgBackupVpRowStatus,
       "pgBackupVpPrimaryAdminStatus": pgBackupVpPrimaryAdminStatus,
       "pgBackupVpPrimaryOperStatus": pgBackupVpPrimaryOperStatus,
       "pgBackupVpSecondaryOperStatus": pgBackupVpSecondaryOperStatus,
       "pgBackupVpSwitchTimes": pgBackupVpSwitchTimes,
       "pgBackupVcTable": pgBackupVcTable,
       "pgBackupVcEntry": pgBackupVcEntry,
       "pgBackupVcPrimaryIfIndex": pgBackupVcPrimaryIfIndex,
       "pgBackupVcPrimaryVpi": pgBackupVcPrimaryVpi,
       "pgBackupVcPrimaryVci": pgBackupVcPrimaryVci,
       "pgBackupVcSecondaryIfIndex": pgBackupVcSecondaryIfIndex,
       "pgBackupVcSecondaryVpi": pgBackupVcSecondaryVpi,
       "pgBackupVcSecondaryVci": pgBackupVcSecondaryVci,
       "pgBackupVcRowStatus": pgBackupVcRowStatus,
       "pgBackupVcPrimaryAdminStatus": pgBackupVcPrimaryAdminStatus,
       "pgBackupVcPrimaryOperStatus": pgBackupVcPrimaryOperStatus,
       "pgBackupVcSecondaryOperStatus": pgBackupVcSecondaryOperStatus,
       "pgBackupVcSwitchTimes": pgBackupVcSwitchTimes}
)
