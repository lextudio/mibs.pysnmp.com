# SNMP MIB module (APPIAN-BUFFERS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APPIAN-BUFFERS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:31 2024
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

(AcAdminStatus,
 AcNodeId,
 acOsap) = mibBuilder.importSymbols(
    "APPIAN-SMI-MIB",
    "AcAdminStatus",
    "AcNodeId",
    "acOsap")

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

acBuffers = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 10)
)
acBuffers.setRevisions(
        ("1900-10-16 11:30",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcSwitchBuffStatsTable_Object = MibTable
acSwitchBuffStatsTable = _AcSwitchBuffStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 10, 1)
)
if mibBuilder.loadTexts:
    acSwitchBuffStatsTable.setStatus("current")
_AcSwitchBuffStatsEntry_Object = MibTableRow
acSwitchBuffStatsEntry = _AcSwitchBuffStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 10, 1, 1)
)
acSwitchBuffStatsEntry.setIndexNames(
    (0, "APPIAN-BUFFERS-MIB", "acSwitchBuffStatsNodeId"),
)
if mibBuilder.loadTexts:
    acSwitchBuffStatsEntry.setStatus("current")
_AcSwitchBuffStatsNodeId_Type = AcNodeId
_AcSwitchBuffStatsNodeId_Object = MibTableColumn
acSwitchBuffStatsNodeId = _AcSwitchBuffStatsNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 10, 1, 1, 1),
    _AcSwitchBuffStatsNodeId_Type()
)
acSwitchBuffStatsNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSwitchBuffStatsNodeId.setStatus("current")
_AcSwitchBuffStatsBuffSize_Type = Unsigned32
_AcSwitchBuffStatsBuffSize_Object = MibTableColumn
acSwitchBuffStatsBuffSize = _AcSwitchBuffStatsBuffSize_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 10, 1, 1, 2),
    _AcSwitchBuffStatsBuffSize_Type()
)
acSwitchBuffStatsBuffSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSwitchBuffStatsBuffSize.setStatus("current")
_AcSwitchBuffStatsTotalBuffs_Type = Unsigned32
_AcSwitchBuffStatsTotalBuffs_Object = MibTableColumn
acSwitchBuffStatsTotalBuffs = _AcSwitchBuffStatsTotalBuffs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 10, 1, 1, 3),
    _AcSwitchBuffStatsTotalBuffs_Type()
)
acSwitchBuffStatsTotalBuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSwitchBuffStatsTotalBuffs.setStatus("current")
_AcSwitchBuffStatsTotalBuffCredits_Type = Unsigned32
_AcSwitchBuffStatsTotalBuffCredits_Object = MibTableColumn
acSwitchBuffStatsTotalBuffCredits = _AcSwitchBuffStatsTotalBuffCredits_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 10, 1, 1, 4),
    _AcSwitchBuffStatsTotalBuffCredits_Type()
)
acSwitchBuffStatsTotalBuffCredits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSwitchBuffStatsTotalBuffCredits.setStatus("current")
_AcSwitchBuffStatsTotalLocalServices_Type = Unsigned32
_AcSwitchBuffStatsTotalLocalServices_Object = MibTableColumn
acSwitchBuffStatsTotalLocalServices = _AcSwitchBuffStatsTotalLocalServices_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 10, 1, 1, 5),
    _AcSwitchBuffStatsTotalLocalServices_Type()
)
acSwitchBuffStatsTotalLocalServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSwitchBuffStatsTotalLocalServices.setStatus("current")
_AcSwitchBuffStatsTotalRemoteServices_Type = Unsigned32
_AcSwitchBuffStatsTotalRemoteServices_Object = MibTableColumn
acSwitchBuffStatsTotalRemoteServices = _AcSwitchBuffStatsTotalRemoteServices_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 10, 1, 1, 6),
    _AcSwitchBuffStatsTotalRemoteServices_Type()
)
acSwitchBuffStatsTotalRemoteServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSwitchBuffStatsTotalRemoteServices.setStatus("current")
_AcSwitchBuffStatsTotalRemPoolMisses_Type = Unsigned32
_AcSwitchBuffStatsTotalRemPoolMisses_Object = MibTableColumn
acSwitchBuffStatsTotalRemPoolMisses = _AcSwitchBuffStatsTotalRemPoolMisses_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 10, 1, 1, 7),
    _AcSwitchBuffStatsTotalRemPoolMisses_Type()
)
acSwitchBuffStatsTotalRemPoolMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSwitchBuffStatsTotalRemPoolMisses.setStatus("current")
_AcSwitchBuffCfgTable_Object = MibTable
acSwitchBuffCfgTable = _AcSwitchBuffCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 10, 2)
)
if mibBuilder.loadTexts:
    acSwitchBuffCfgTable.setStatus("current")
_AcSwitchBuffCfgEntry_Object = MibTableRow
acSwitchBuffCfgEntry = _AcSwitchBuffCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 10, 2, 1)
)
acSwitchBuffCfgEntry.setIndexNames(
    (0, "APPIAN-BUFFERS-MIB", "acSwitchBuffCfgNodeId"),
)
if mibBuilder.loadTexts:
    acSwitchBuffCfgEntry.setStatus("current")
_AcSwitchBuffCfgNodeId_Type = AcNodeId
_AcSwitchBuffCfgNodeId_Object = MibTableColumn
acSwitchBuffCfgNodeId = _AcSwitchBuffCfgNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 10, 2, 1, 1),
    _AcSwitchBuffCfgNodeId_Type()
)
acSwitchBuffCfgNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSwitchBuffCfgNodeId.setStatus("current")


class _AcSwitchBuffCfgOversubRate_Type(Unsigned32):
    """Custom type acSwitchBuffCfgOversubRate based on Unsigned32"""
    defaultValue = 0


_AcSwitchBuffCfgOversubRate_Object = MibTableColumn
acSwitchBuffCfgOversubRate = _AcSwitchBuffCfgOversubRate_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 10, 2, 1, 2),
    _AcSwitchBuffCfgOversubRate_Type()
)
acSwitchBuffCfgOversubRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSwitchBuffCfgOversubRate.setStatus("current")


class _AcSwitchBuffCfgMinDefaultBPSize_Type(Unsigned32):
    """Custom type acSwitchBuffCfgMinDefaultBPSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AcSwitchBuffCfgMinDefaultBPSize_Type.__name__ = "Unsigned32"
_AcSwitchBuffCfgMinDefaultBPSize_Object = MibTableColumn
acSwitchBuffCfgMinDefaultBPSize = _AcSwitchBuffCfgMinDefaultBPSize_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 10, 2, 1, 3),
    _AcSwitchBuffCfgMinDefaultBPSize_Type()
)
acSwitchBuffCfgMinDefaultBPSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSwitchBuffCfgMinDefaultBPSize.setStatus("current")


class _AcSwitchBuffCfgRemoteServicesBP_Type(Unsigned32):
    """Custom type acSwitchBuffCfgRemoteServicesBP based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 131072),
    )


_AcSwitchBuffCfgRemoteServicesBP_Type.__name__ = "Unsigned32"
_AcSwitchBuffCfgRemoteServicesBP_Object = MibTableColumn
acSwitchBuffCfgRemoteServicesBP = _AcSwitchBuffCfgRemoteServicesBP_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 10, 2, 1, 4),
    _AcSwitchBuffCfgRemoteServicesBP_Type()
)
acSwitchBuffCfgRemoteServicesBP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSwitchBuffCfgRemoteServicesBP.setStatus("current")


class _AcSwitchBuffCfgUpBuffCapWeight_Type(Unsigned32):
    """Custom type acSwitchBuffCfgUpBuffCapWeight based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AcSwitchBuffCfgUpBuffCapWeight_Type.__name__ = "Unsigned32"
_AcSwitchBuffCfgUpBuffCapWeight_Object = MibTableColumn
acSwitchBuffCfgUpBuffCapWeight = _AcSwitchBuffCfgUpBuffCapWeight_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 10, 2, 1, 5),
    _AcSwitchBuffCfgUpBuffCapWeight_Type()
)
acSwitchBuffCfgUpBuffCapWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSwitchBuffCfgUpBuffCapWeight.setStatus("current")


class _AcSwitchBuffCfgDownBuffCapWeight_Type(Unsigned32):
    """Custom type acSwitchBuffCfgDownBuffCapWeight based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AcSwitchBuffCfgDownBuffCapWeight_Type.__name__ = "Unsigned32"
_AcSwitchBuffCfgDownBuffCapWeight_Object = MibTableColumn
acSwitchBuffCfgDownBuffCapWeight = _AcSwitchBuffCfgDownBuffCapWeight_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 10, 2, 1, 6),
    _AcSwitchBuffCfgDownBuffCapWeight_Type()
)
acSwitchBuffCfgDownBuffCapWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSwitchBuffCfgDownBuffCapWeight.setStatus("current")


class _AcSwitchBuffCfgLocalBuffCapWeight_Type(Unsigned32):
    """Custom type acSwitchBuffCfgLocalBuffCapWeight based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AcSwitchBuffCfgLocalBuffCapWeight_Type.__name__ = "Unsigned32"
_AcSwitchBuffCfgLocalBuffCapWeight_Object = MibTableColumn
acSwitchBuffCfgLocalBuffCapWeight = _AcSwitchBuffCfgLocalBuffCapWeight_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 10, 2, 1, 7),
    _AcSwitchBuffCfgLocalBuffCapWeight_Type()
)
acSwitchBuffCfgLocalBuffCapWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSwitchBuffCfgLocalBuffCapWeight.setStatus("current")


class _AcSwitchBuffCfgRemoteBuffCapWeight_Type(Unsigned32):
    """Custom type acSwitchBuffCfgRemoteBuffCapWeight based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AcSwitchBuffCfgRemoteBuffCapWeight_Type.__name__ = "Unsigned32"
_AcSwitchBuffCfgRemoteBuffCapWeight_Object = MibTableColumn
acSwitchBuffCfgRemoteBuffCapWeight = _AcSwitchBuffCfgRemoteBuffCapWeight_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 10, 2, 1, 8),
    _AcSwitchBuffCfgRemoteBuffCapWeight_Type()
)
acSwitchBuffCfgRemoteBuffCapWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSwitchBuffCfgRemoteBuffCapWeight.setStatus("current")
_AcSwitchBuffPoolTable_Object = MibTable
acSwitchBuffPoolTable = _AcSwitchBuffPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 10, 3)
)
if mibBuilder.loadTexts:
    acSwitchBuffPoolTable.setStatus("current")
_AcSwitchBuffPoolEntry_Object = MibTableRow
acSwitchBuffPoolEntry = _AcSwitchBuffPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 10, 3, 1)
)
acSwitchBuffPoolEntry.setIndexNames(
    (0, "APPIAN-BUFFERS-MIB", "acSwitchBuffPoolNodeId"),
    (0, "APPIAN-BUFFERS-MIB", "acSwitchBuffPoolID"),
)
if mibBuilder.loadTexts:
    acSwitchBuffPoolEntry.setStatus("current")
_AcSwitchBuffPoolNodeId_Type = AcNodeId
_AcSwitchBuffPoolNodeId_Object = MibTableColumn
acSwitchBuffPoolNodeId = _AcSwitchBuffPoolNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 10, 3, 1, 1),
    _AcSwitchBuffPoolNodeId_Type()
)
acSwitchBuffPoolNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSwitchBuffPoolNodeId.setStatus("current")


class _AcSwitchBuffPoolID_Type(Unsigned32):
    """Custom type acSwitchBuffPoolID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 131072),
    )


_AcSwitchBuffPoolID_Type.__name__ = "Unsigned32"
_AcSwitchBuffPoolID_Object = MibTableColumn
acSwitchBuffPoolID = _AcSwitchBuffPoolID_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 10, 3, 1, 2),
    _AcSwitchBuffPoolID_Type()
)
acSwitchBuffPoolID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSwitchBuffPoolID.setStatus("current")


class _AcSwitchBuffPoolAdminStatus_Type(AcAdminStatus):
    """Custom type acSwitchBuffPoolAdminStatus based on AcAdminStatus"""


_AcSwitchBuffPoolAdminStatus_Object = MibTableColumn
acSwitchBuffPoolAdminStatus = _AcSwitchBuffPoolAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 10, 3, 1, 3),
    _AcSwitchBuffPoolAdminStatus_Type()
)
acSwitchBuffPoolAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSwitchBuffPoolAdminStatus.setStatus("current")


class _AcSwitchBuffPoolName_Type(DisplayString):
    """Custom type acSwitchBuffPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AcSwitchBuffPoolName_Type.__name__ = "DisplayString"
_AcSwitchBuffPoolName_Object = MibTableColumn
acSwitchBuffPoolName = _AcSwitchBuffPoolName_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 10, 3, 1, 4),
    _AcSwitchBuffPoolName_Type()
)
acSwitchBuffPoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSwitchBuffPoolName.setStatus("current")


class _AcSwitchBuffPoolCfgBuffCredits_Type(Unsigned32):
    """Custom type acSwitchBuffPoolCfgBuffCredits based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AcSwitchBuffPoolCfgBuffCredits_Type.__name__ = "Unsigned32"
_AcSwitchBuffPoolCfgBuffCredits_Object = MibTableColumn
acSwitchBuffPoolCfgBuffCredits = _AcSwitchBuffPoolCfgBuffCredits_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 10, 3, 1, 5),
    _AcSwitchBuffPoolCfgBuffCredits_Type()
)
acSwitchBuffPoolCfgBuffCredits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSwitchBuffPoolCfgBuffCredits.setStatus("current")


class _AcSwitchBuffPoolActualBuffCredits_Type(Unsigned32):
    """Custom type acSwitchBuffPoolActualBuffCredits based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AcSwitchBuffPoolActualBuffCredits_Type.__name__ = "Unsigned32"
_AcSwitchBuffPoolActualBuffCredits_Object = MibTableColumn
acSwitchBuffPoolActualBuffCredits = _AcSwitchBuffPoolActualBuffCredits_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 10, 3, 1, 6),
    _AcSwitchBuffPoolActualBuffCredits_Type()
)
acSwitchBuffPoolActualBuffCredits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSwitchBuffPoolActualBuffCredits.setStatus("current")
_AcSwitchBuffPoolTotalLocalServices_Type = Unsigned32
_AcSwitchBuffPoolTotalLocalServices_Object = MibTableColumn
acSwitchBuffPoolTotalLocalServices = _AcSwitchBuffPoolTotalLocalServices_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 10, 3, 1, 7),
    _AcSwitchBuffPoolTotalLocalServices_Type()
)
acSwitchBuffPoolTotalLocalServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSwitchBuffPoolTotalLocalServices.setStatus("current")
_AcSwitchBuffPoolTotalRemoteServices_Type = Unsigned32
_AcSwitchBuffPoolTotalRemoteServices_Object = MibTableColumn
acSwitchBuffPoolTotalRemoteServices = _AcSwitchBuffPoolTotalRemoteServices_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 10, 3, 1, 8),
    _AcSwitchBuffPoolTotalRemoteServices_Type()
)
acSwitchBuffPoolTotalRemoteServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSwitchBuffPoolTotalRemoteServices.setStatus("current")
_AcSwitchBuffPoolResellerId_Type = Integer32
_AcSwitchBuffPoolResellerId_Object = MibTableColumn
acSwitchBuffPoolResellerId = _AcSwitchBuffPoolResellerId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 10, 3, 1, 9),
    _AcSwitchBuffPoolResellerId_Type()
)
acSwitchBuffPoolResellerId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSwitchBuffPoolResellerId.setStatus("current")


class _AcSwitchBuffPoolResellerName_Type(DisplayString):
    """Custom type acSwitchBuffPoolResellerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AcSwitchBuffPoolResellerName_Type.__name__ = "DisplayString"
_AcSwitchBuffPoolResellerName_Object = MibTableColumn
acSwitchBuffPoolResellerName = _AcSwitchBuffPoolResellerName_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 10, 3, 1, 10),
    _AcSwitchBuffPoolResellerName_Type()
)
acSwitchBuffPoolResellerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSwitchBuffPoolResellerName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APPIAN-BUFFERS-MIB",
    **{"acBuffers": acBuffers,
       "acSwitchBuffStatsTable": acSwitchBuffStatsTable,
       "acSwitchBuffStatsEntry": acSwitchBuffStatsEntry,
       "acSwitchBuffStatsNodeId": acSwitchBuffStatsNodeId,
       "acSwitchBuffStatsBuffSize": acSwitchBuffStatsBuffSize,
       "acSwitchBuffStatsTotalBuffs": acSwitchBuffStatsTotalBuffs,
       "acSwitchBuffStatsTotalBuffCredits": acSwitchBuffStatsTotalBuffCredits,
       "acSwitchBuffStatsTotalLocalServices": acSwitchBuffStatsTotalLocalServices,
       "acSwitchBuffStatsTotalRemoteServices": acSwitchBuffStatsTotalRemoteServices,
       "acSwitchBuffStatsTotalRemPoolMisses": acSwitchBuffStatsTotalRemPoolMisses,
       "acSwitchBuffCfgTable": acSwitchBuffCfgTable,
       "acSwitchBuffCfgEntry": acSwitchBuffCfgEntry,
       "acSwitchBuffCfgNodeId": acSwitchBuffCfgNodeId,
       "acSwitchBuffCfgOversubRate": acSwitchBuffCfgOversubRate,
       "acSwitchBuffCfgMinDefaultBPSize": acSwitchBuffCfgMinDefaultBPSize,
       "acSwitchBuffCfgRemoteServicesBP": acSwitchBuffCfgRemoteServicesBP,
       "acSwitchBuffCfgUpBuffCapWeight": acSwitchBuffCfgUpBuffCapWeight,
       "acSwitchBuffCfgDownBuffCapWeight": acSwitchBuffCfgDownBuffCapWeight,
       "acSwitchBuffCfgLocalBuffCapWeight": acSwitchBuffCfgLocalBuffCapWeight,
       "acSwitchBuffCfgRemoteBuffCapWeight": acSwitchBuffCfgRemoteBuffCapWeight,
       "acSwitchBuffPoolTable": acSwitchBuffPoolTable,
       "acSwitchBuffPoolEntry": acSwitchBuffPoolEntry,
       "acSwitchBuffPoolNodeId": acSwitchBuffPoolNodeId,
       "acSwitchBuffPoolID": acSwitchBuffPoolID,
       "acSwitchBuffPoolAdminStatus": acSwitchBuffPoolAdminStatus,
       "acSwitchBuffPoolName": acSwitchBuffPoolName,
       "acSwitchBuffPoolCfgBuffCredits": acSwitchBuffPoolCfgBuffCredits,
       "acSwitchBuffPoolActualBuffCredits": acSwitchBuffPoolActualBuffCredits,
       "acSwitchBuffPoolTotalLocalServices": acSwitchBuffPoolTotalLocalServices,
       "acSwitchBuffPoolTotalRemoteServices": acSwitchBuffPoolTotalRemoteServices,
       "acSwitchBuffPoolResellerId": acSwitchBuffPoolResellerId,
       "acSwitchBuffPoolResellerName": acSwitchBuffPoolResellerName}
)
