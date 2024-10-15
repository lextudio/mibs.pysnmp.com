# SNMP MIB module (HPN-ICF-LBV2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-LBV2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:46 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfLBv2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148)
)
hpnicfLBv2.setRevisions(
        ("2013-11-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfLBv2GlobalObjects_ObjectIdentity = ObjectIdentity
hpnicfLBv2GlobalObjects = _HpnicfLBv2GlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 1)
)


class _HpnicfLBv2TrapEnable_Type(Integer32):
    """Custom type hpnicfLBv2TrapEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HpnicfLBv2TrapEnable_Type.__name__ = "Integer32"
_HpnicfLBv2TrapEnable_Object = MibScalar
hpnicfLBv2TrapEnable = _HpnicfLBv2TrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 1, 1),
    _HpnicfLBv2TrapEnable_Type()
)
hpnicfLBv2TrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfLBv2TrapEnable.setStatus("current")
_HpnicfLBv2ActionTables_ObjectIdentity = ObjectIdentity
hpnicfLBv2ActionTables = _HpnicfLBv2ActionTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 2)
)
_HpnicfLBv2ActionTable_Object = MibTable
hpnicfLBv2ActionTable = _HpnicfLBv2ActionTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfLBv2ActionTable.setStatus("current")
_HpnicfLBv2ActionEntry_Object = MibTableRow
hpnicfLBv2ActionEntry = _HpnicfLBv2ActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 2, 1, 1)
)
hpnicfLBv2ActionEntry.setIndexNames(
    (0, "HPN-ICF-LBV2-MIB", "hpnicfLBv2ActionName"),
)
if mibBuilder.loadTexts:
    hpnicfLBv2ActionEntry.setStatus("current")


class _HpnicfLBv2ActionName_Type(DisplayString):
    """Custom type hpnicfLBv2ActionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_HpnicfLBv2ActionName_Type.__name__ = "DisplayString"
_HpnicfLBv2ActionName_Object = MibTableColumn
hpnicfLBv2ActionName = _HpnicfLBv2ActionName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 2, 1, 1, 1),
    _HpnicfLBv2ActionName_Type()
)
hpnicfLBv2ActionName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfLBv2ActionName.setStatus("current")


class _HpnicfLBv2ActionDefaultSF_Type(DisplayString):
    """Custom type hpnicfLBv2ActionDefaultSF based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HpnicfLBv2ActionDefaultSF_Type.__name__ = "DisplayString"
_HpnicfLBv2ActionDefaultSF_Object = MibTableColumn
hpnicfLBv2ActionDefaultSF = _HpnicfLBv2ActionDefaultSF_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 2, 1, 1, 2),
    _HpnicfLBv2ActionDefaultSF_Type()
)
hpnicfLBv2ActionDefaultSF.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfLBv2ActionDefaultSF.setStatus("current")


class _HpnicfLBv2ActionBackupSF_Type(DisplayString):
    """Custom type hpnicfLBv2ActionBackupSF based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HpnicfLBv2ActionBackupSF_Type.__name__ = "DisplayString"
_HpnicfLBv2ActionBackupSF_Object = MibTableColumn
hpnicfLBv2ActionBackupSF = _HpnicfLBv2ActionBackupSF_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 2, 1, 1, 3),
    _HpnicfLBv2ActionBackupSF_Type()
)
hpnicfLBv2ActionBackupSF.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfLBv2ActionBackupSF.setStatus("current")


class _HpnicfLBv2ActionInUseSF_Type(DisplayString):
    """Custom type hpnicfLBv2ActionInUseSF based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HpnicfLBv2ActionInUseSF_Type.__name__ = "DisplayString"
_HpnicfLBv2ActionInUseSF_Object = MibTableColumn
hpnicfLBv2ActionInUseSF = _HpnicfLBv2ActionInUseSF_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 2, 1, 1, 4),
    _HpnicfLBv2ActionInUseSF_Type()
)
hpnicfLBv2ActionInUseSF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLBv2ActionInUseSF.setStatus("current")
_HpnicfLBv2ActionRowStatus_Type = RowStatus
_HpnicfLBv2ActionRowStatus_Object = MibTableColumn
hpnicfLBv2ActionRowStatus = _HpnicfLBv2ActionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 2, 1, 1, 5),
    _HpnicfLBv2ActionRowStatus_Type()
)
hpnicfLBv2ActionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfLBv2ActionRowStatus.setStatus("current")
_HpnicfLBv2VSTables_ObjectIdentity = ObjectIdentity
hpnicfLBv2VSTables = _HpnicfLBv2VSTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3)
)
_HpnicfLBv2VSTable_Object = MibTable
hpnicfLBv2VSTable = _HpnicfLBv2VSTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3, 1)
)
if mibBuilder.loadTexts:
    hpnicfLBv2VSTable.setStatus("current")
_HpnicfLBv2VSEntry_Object = MibTableRow
hpnicfLBv2VSEntry = _HpnicfLBv2VSEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3, 1, 1)
)
hpnicfLBv2VSEntry.setIndexNames(
    (0, "HPN-ICF-LBV2-MIB", "hpnicfLBv2VSName"),
)
if mibBuilder.loadTexts:
    hpnicfLBv2VSEntry.setStatus("current")


class _HpnicfLBv2VSName_Type(DisplayString):
    """Custom type hpnicfLBv2VSName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_HpnicfLBv2VSName_Type.__name__ = "DisplayString"
_HpnicfLBv2VSName_Object = MibTableColumn
hpnicfLBv2VSName = _HpnicfLBv2VSName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3, 1, 1, 1),
    _HpnicfLBv2VSName_Type()
)
hpnicfLBv2VSName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfLBv2VSName.setStatus("current")


class _HpnicfLBv2VSConnectionsLimit_Type(Unsigned32):
    """Custom type hpnicfLBv2VSConnectionsLimit based on Unsigned32"""
    defaultValue = 0


_HpnicfLBv2VSConnectionsLimit_Object = MibTableColumn
hpnicfLBv2VSConnectionsLimit = _HpnicfLBv2VSConnectionsLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3, 1, 1, 2),
    _HpnicfLBv2VSConnectionsLimit_Type()
)
hpnicfLBv2VSConnectionsLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfLBv2VSConnectionsLimit.setStatus("current")


class _HpnicfLBv2VSConnectionsRateLimit_Type(Unsigned32):
    """Custom type hpnicfLBv2VSConnectionsRateLimit based on Unsigned32"""
    defaultValue = 0


_HpnicfLBv2VSConnectionsRateLimit_Object = MibTableColumn
hpnicfLBv2VSConnectionsRateLimit = _HpnicfLBv2VSConnectionsRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3, 1, 1, 3),
    _HpnicfLBv2VSConnectionsRateLimit_Type()
)
hpnicfLBv2VSConnectionsRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfLBv2VSConnectionsRateLimit.setStatus("current")


class _HpnicfLBv2VSDefaultSF_Type(DisplayString):
    """Custom type hpnicfLBv2VSDefaultSF based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HpnicfLBv2VSDefaultSF_Type.__name__ = "DisplayString"
_HpnicfLBv2VSDefaultSF_Object = MibTableColumn
hpnicfLBv2VSDefaultSF = _HpnicfLBv2VSDefaultSF_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3, 1, 1, 4),
    _HpnicfLBv2VSDefaultSF_Type()
)
hpnicfLBv2VSDefaultSF.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfLBv2VSDefaultSF.setStatus("current")


class _HpnicfLBv2VSBackupSF_Type(DisplayString):
    """Custom type hpnicfLBv2VSBackupSF based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HpnicfLBv2VSBackupSF_Type.__name__ = "DisplayString"
_HpnicfLBv2VSBackupSF_Object = MibTableColumn
hpnicfLBv2VSBackupSF = _HpnicfLBv2VSBackupSF_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3, 1, 1, 5),
    _HpnicfLBv2VSBackupSF_Type()
)
hpnicfLBv2VSBackupSF.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfLBv2VSBackupSF.setStatus("current")


class _HpnicfLBv2VSInUseSF_Type(DisplayString):
    """Custom type hpnicfLBv2VSInUseSF based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HpnicfLBv2VSInUseSF_Type.__name__ = "DisplayString"
_HpnicfLBv2VSInUseSF_Object = MibTableColumn
hpnicfLBv2VSInUseSF = _HpnicfLBv2VSInUseSF_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3, 1, 1, 6),
    _HpnicfLBv2VSInUseSF_Type()
)
hpnicfLBv2VSInUseSF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLBv2VSInUseSF.setStatus("current")
_HpnicfLBv2VSRowStatus_Type = RowStatus
_HpnicfLBv2VSRowStatus_Object = MibTableColumn
hpnicfLBv2VSRowStatus = _HpnicfLBv2VSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3, 1, 1, 7),
    _HpnicfLBv2VSRowStatus_Type()
)
hpnicfLBv2VSRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfLBv2VSRowStatus.setStatus("current")
_HpnicfLBv2VSStatsTable_Object = MibTable
hpnicfLBv2VSStatsTable = _HpnicfLBv2VSStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3, 2)
)
if mibBuilder.loadTexts:
    hpnicfLBv2VSStatsTable.setStatus("current")
_HpnicfLBv2VSStatsEntry_Object = MibTableRow
hpnicfLBv2VSStatsEntry = _HpnicfLBv2VSStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3, 2, 1)
)
hpnicfLBv2VSStatsEntry.setIndexNames(
    (0, "HPN-ICF-LBV2-MIB", "hpnicfLBv2VSName"),
    (0, "HPN-ICF-LBV2-MIB", "hpnicfLBv2VSStatChassis"),
    (0, "HPN-ICF-LBV2-MIB", "hpnicfLBv2VSStatSlot"),
    (0, "HPN-ICF-LBV2-MIB", "hpnicfLBv2VSStatCpuid"),
)
if mibBuilder.loadTexts:
    hpnicfLBv2VSStatsEntry.setStatus("current")


class _HpnicfLBv2VSStatChassis_Type(Unsigned32):
    """Custom type hpnicfLBv2VSStatChassis based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfLBv2VSStatChassis_Type.__name__ = "Unsigned32"
_HpnicfLBv2VSStatChassis_Object = MibTableColumn
hpnicfLBv2VSStatChassis = _HpnicfLBv2VSStatChassis_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3, 2, 1, 1),
    _HpnicfLBv2VSStatChassis_Type()
)
hpnicfLBv2VSStatChassis.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfLBv2VSStatChassis.setStatus("current")


class _HpnicfLBv2VSStatSlot_Type(Unsigned32):
    """Custom type hpnicfLBv2VSStatSlot based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfLBv2VSStatSlot_Type.__name__ = "Unsigned32"
_HpnicfLBv2VSStatSlot_Object = MibTableColumn
hpnicfLBv2VSStatSlot = _HpnicfLBv2VSStatSlot_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3, 2, 1, 2),
    _HpnicfLBv2VSStatSlot_Type()
)
hpnicfLBv2VSStatSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfLBv2VSStatSlot.setStatus("current")


class _HpnicfLBv2VSStatCpuid_Type(Unsigned32):
    """Custom type hpnicfLBv2VSStatCpuid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfLBv2VSStatCpuid_Type.__name__ = "Unsigned32"
_HpnicfLBv2VSStatCpuid_Object = MibTableColumn
hpnicfLBv2VSStatCpuid = _HpnicfLBv2VSStatCpuid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3, 2, 1, 3),
    _HpnicfLBv2VSStatCpuid_Type()
)
hpnicfLBv2VSStatCpuid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfLBv2VSStatCpuid.setStatus("current")
_HpnicfLBv2VSStatTotalConnections_Type = Counter64
_HpnicfLBv2VSStatTotalConnections_Object = MibTableColumn
hpnicfLBv2VSStatTotalConnections = _HpnicfLBv2VSStatTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3, 2, 1, 4),
    _HpnicfLBv2VSStatTotalConnections_Type()
)
hpnicfLBv2VSStatTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLBv2VSStatTotalConnections.setStatus("current")
_HpnicfLBv2VSStatActiveConnections_Type = Unsigned32
_HpnicfLBv2VSStatActiveConnections_Object = MibTableColumn
hpnicfLBv2VSStatActiveConnections = _HpnicfLBv2VSStatActiveConnections_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3, 2, 1, 5),
    _HpnicfLBv2VSStatActiveConnections_Type()
)
hpnicfLBv2VSStatActiveConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLBv2VSStatActiveConnections.setStatus("current")
_HpnicfLBv2VSStatClientSidePKTsIn_Type = Counter64
_HpnicfLBv2VSStatClientSidePKTsIn_Object = MibTableColumn
hpnicfLBv2VSStatClientSidePKTsIn = _HpnicfLBv2VSStatClientSidePKTsIn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3, 2, 1, 6),
    _HpnicfLBv2VSStatClientSidePKTsIn_Type()
)
hpnicfLBv2VSStatClientSidePKTsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLBv2VSStatClientSidePKTsIn.setStatus("current")
_HpnicfLBv2VSStatClientSidePKTsOut_Type = Counter64
_HpnicfLBv2VSStatClientSidePKTsOut_Object = MibTableColumn
hpnicfLBv2VSStatClientSidePKTsOut = _HpnicfLBv2VSStatClientSidePKTsOut_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3, 2, 1, 7),
    _HpnicfLBv2VSStatClientSidePKTsOut_Type()
)
hpnicfLBv2VSStatClientSidePKTsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLBv2VSStatClientSidePKTsOut.setStatus("current")
_HpnicfLBv2VSStatDroppedPackets_Type = Counter64
_HpnicfLBv2VSStatDroppedPackets_Object = MibTableColumn
hpnicfLBv2VSStatDroppedPackets = _HpnicfLBv2VSStatDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3, 2, 1, 8),
    _HpnicfLBv2VSStatDroppedPackets_Type()
)
hpnicfLBv2VSStatDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLBv2VSStatDroppedPackets.setStatus("current")
_HpnicfLBv2VSStatClientSideBytesIn_Type = Counter64
_HpnicfLBv2VSStatClientSideBytesIn_Object = MibTableColumn
hpnicfLBv2VSStatClientSideBytesIn = _HpnicfLBv2VSStatClientSideBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3, 2, 1, 9),
    _HpnicfLBv2VSStatClientSideBytesIn_Type()
)
hpnicfLBv2VSStatClientSideBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLBv2VSStatClientSideBytesIn.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfLBv2VSStatClientSideBytesIn.setUnits("byte")
_HpnicfLBv2VSStatClientSideBytesOut_Type = Counter64
_HpnicfLBv2VSStatClientSideBytesOut_Object = MibTableColumn
hpnicfLBv2VSStatClientSideBytesOut = _HpnicfLBv2VSStatClientSideBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3, 2, 1, 10),
    _HpnicfLBv2VSStatClientSideBytesOut_Type()
)
hpnicfLBv2VSStatClientSideBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLBv2VSStatClientSideBytesOut.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfLBv2VSStatClientSideBytesOut.setUnits("byte")
_HpnicfLBv2VSStatReceivedRequests_Type = Counter64
_HpnicfLBv2VSStatReceivedRequests_Object = MibTableColumn
hpnicfLBv2VSStatReceivedRequests = _HpnicfLBv2VSStatReceivedRequests_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3, 2, 1, 11),
    _HpnicfLBv2VSStatReceivedRequests_Type()
)
hpnicfLBv2VSStatReceivedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLBv2VSStatReceivedRequests.setStatus("current")
_HpnicfLBv2VSStatSentResponses_Type = Counter64
_HpnicfLBv2VSStatSentResponses_Object = MibTableColumn
hpnicfLBv2VSStatSentResponses = _HpnicfLBv2VSStatSentResponses_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3, 2, 1, 12),
    _HpnicfLBv2VSStatSentResponses_Type()
)
hpnicfLBv2VSStatSentResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLBv2VSStatSentResponses.setStatus("current")
_HpnicfLBv2VSStatConnectionsRate_Type = Unsigned32
_HpnicfLBv2VSStatConnectionsRate_Object = MibTableColumn
hpnicfLBv2VSStatConnectionsRate = _HpnicfLBv2VSStatConnectionsRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3, 2, 1, 13),
    _HpnicfLBv2VSStatConnectionsRate_Type()
)
hpnicfLBv2VSStatConnectionsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLBv2VSStatConnectionsRate.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfLBv2VSStatConnectionsRate.setUnits("cps")
_HpnicfLBv2RSTables_ObjectIdentity = ObjectIdentity
hpnicfLBv2RSTables = _HpnicfLBv2RSTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 4)
)
_HpnicfLBv2RSTable_Object = MibTable
hpnicfLBv2RSTable = _HpnicfLBv2RSTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 4, 1)
)
if mibBuilder.loadTexts:
    hpnicfLBv2RSTable.setStatus("current")
_HpnicfLBv2RSEntry_Object = MibTableRow
hpnicfLBv2RSEntry = _HpnicfLBv2RSEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 4, 1, 1)
)
hpnicfLBv2RSEntry.setIndexNames(
    (0, "HPN-ICF-LBV2-MIB", "hpnicfLBv2RSName"),
)
if mibBuilder.loadTexts:
    hpnicfLBv2RSEntry.setStatus("current")


class _HpnicfLBv2RSName_Type(DisplayString):
    """Custom type hpnicfLBv2RSName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_HpnicfLBv2RSName_Type.__name__ = "DisplayString"
_HpnicfLBv2RSName_Object = MibTableColumn
hpnicfLBv2RSName = _HpnicfLBv2RSName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 4, 1, 1, 1),
    _HpnicfLBv2RSName_Type()
)
hpnicfLBv2RSName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfLBv2RSName.setStatus("current")
_HpnicfLBv2RSRowStatus_Type = RowStatus
_HpnicfLBv2RSRowStatus_Object = MibTableColumn
hpnicfLBv2RSRowStatus = _HpnicfLBv2RSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 4, 1, 1, 2),
    _HpnicfLBv2RSRowStatus_Type()
)
hpnicfLBv2RSRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfLBv2RSRowStatus.setStatus("current")
_HpnicfLBv2RSStatsTable_Object = MibTable
hpnicfLBv2RSStatsTable = _HpnicfLBv2RSStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 4, 2)
)
if mibBuilder.loadTexts:
    hpnicfLBv2RSStatsTable.setStatus("current")
_HpnicfLBv2RSStatsEntry_Object = MibTableRow
hpnicfLBv2RSStatsEntry = _HpnicfLBv2RSStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 4, 2, 1)
)
hpnicfLBv2RSStatsEntry.setIndexNames(
    (0, "HPN-ICF-LBV2-MIB", "hpnicfLBv2RSName"),
    (0, "HPN-ICF-LBV2-MIB", "hpnicfLBv2RSStatChassis"),
    (0, "HPN-ICF-LBV2-MIB", "hpnicfLBv2RSStatSlot"),
    (0, "HPN-ICF-LBV2-MIB", "hpnicfLBv2RSStatCpuid"),
)
if mibBuilder.loadTexts:
    hpnicfLBv2RSStatsEntry.setStatus("current")


class _HpnicfLBv2RSStatChassis_Type(Unsigned32):
    """Custom type hpnicfLBv2RSStatChassis based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfLBv2RSStatChassis_Type.__name__ = "Unsigned32"
_HpnicfLBv2RSStatChassis_Object = MibTableColumn
hpnicfLBv2RSStatChassis = _HpnicfLBv2RSStatChassis_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 4, 2, 1, 1),
    _HpnicfLBv2RSStatChassis_Type()
)
hpnicfLBv2RSStatChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfLBv2RSStatChassis.setStatus("current")


class _HpnicfLBv2RSStatSlot_Type(Unsigned32):
    """Custom type hpnicfLBv2RSStatSlot based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfLBv2RSStatSlot_Type.__name__ = "Unsigned32"
_HpnicfLBv2RSStatSlot_Object = MibTableColumn
hpnicfLBv2RSStatSlot = _HpnicfLBv2RSStatSlot_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 4, 2, 1, 2),
    _HpnicfLBv2RSStatSlot_Type()
)
hpnicfLBv2RSStatSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfLBv2RSStatSlot.setStatus("current")


class _HpnicfLBv2RSStatCpuid_Type(Unsigned32):
    """Custom type hpnicfLBv2RSStatCpuid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfLBv2RSStatCpuid_Type.__name__ = "Unsigned32"
_HpnicfLBv2RSStatCpuid_Object = MibTableColumn
hpnicfLBv2RSStatCpuid = _HpnicfLBv2RSStatCpuid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 4, 2, 1, 3),
    _HpnicfLBv2RSStatCpuid_Type()
)
hpnicfLBv2RSStatCpuid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfLBv2RSStatCpuid.setStatus("current")
_HpnicfLBv2RSStatTotalConnections_Type = Counter64
_HpnicfLBv2RSStatTotalConnections_Object = MibTableColumn
hpnicfLBv2RSStatTotalConnections = _HpnicfLBv2RSStatTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 4, 2, 1, 4),
    _HpnicfLBv2RSStatTotalConnections_Type()
)
hpnicfLBv2RSStatTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLBv2RSStatTotalConnections.setStatus("current")
_HpnicfLBv2RSStatActiveConnections_Type = Unsigned32
_HpnicfLBv2RSStatActiveConnections_Object = MibTableColumn
hpnicfLBv2RSStatActiveConnections = _HpnicfLBv2RSStatActiveConnections_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 4, 2, 1, 5),
    _HpnicfLBv2RSStatActiveConnections_Type()
)
hpnicfLBv2RSStatActiveConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLBv2RSStatActiveConnections.setStatus("current")
_HpnicfLBv2RSStatServerSidePKTsIn_Type = Counter64
_HpnicfLBv2RSStatServerSidePKTsIn_Object = MibTableColumn
hpnicfLBv2RSStatServerSidePKTsIn = _HpnicfLBv2RSStatServerSidePKTsIn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 4, 2, 1, 6),
    _HpnicfLBv2RSStatServerSidePKTsIn_Type()
)
hpnicfLBv2RSStatServerSidePKTsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLBv2RSStatServerSidePKTsIn.setStatus("current")
_HpnicfLBv2RSStatServerSidePKTsOut_Type = Counter64
_HpnicfLBv2RSStatServerSidePKTsOut_Object = MibTableColumn
hpnicfLBv2RSStatServerSidePKTsOut = _HpnicfLBv2RSStatServerSidePKTsOut_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 4, 2, 1, 7),
    _HpnicfLBv2RSStatServerSidePKTsOut_Type()
)
hpnicfLBv2RSStatServerSidePKTsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLBv2RSStatServerSidePKTsOut.setStatus("current")
_HpnicfLBv2RSStatDroppedPackets_Type = Counter64
_HpnicfLBv2RSStatDroppedPackets_Object = MibTableColumn
hpnicfLBv2RSStatDroppedPackets = _HpnicfLBv2RSStatDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 4, 2, 1, 8),
    _HpnicfLBv2RSStatDroppedPackets_Type()
)
hpnicfLBv2RSStatDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLBv2RSStatDroppedPackets.setStatus("current")
_HpnicfLBv2RSStatServerSideBytesIn_Type = Counter64
_HpnicfLBv2RSStatServerSideBytesIn_Object = MibTableColumn
hpnicfLBv2RSStatServerSideBytesIn = _HpnicfLBv2RSStatServerSideBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 4, 2, 1, 9),
    _HpnicfLBv2RSStatServerSideBytesIn_Type()
)
hpnicfLBv2RSStatServerSideBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLBv2RSStatServerSideBytesIn.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfLBv2RSStatServerSideBytesIn.setUnits("byte")
_HpnicfLBv2RSStatServerSideBytesOut_Type = Counter64
_HpnicfLBv2RSStatServerSideBytesOut_Object = MibTableColumn
hpnicfLBv2RSStatServerSideBytesOut = _HpnicfLBv2RSStatServerSideBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 4, 2, 1, 10),
    _HpnicfLBv2RSStatServerSideBytesOut_Type()
)
hpnicfLBv2RSStatServerSideBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLBv2RSStatServerSideBytesOut.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfLBv2RSStatServerSideBytesOut.setUnits("byte")
_HpnicfLBv2RSStatReceivedRequests_Type = Counter64
_HpnicfLBv2RSStatReceivedRequests_Object = MibTableColumn
hpnicfLBv2RSStatReceivedRequests = _HpnicfLBv2RSStatReceivedRequests_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 4, 2, 1, 11),
    _HpnicfLBv2RSStatReceivedRequests_Type()
)
hpnicfLBv2RSStatReceivedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLBv2RSStatReceivedRequests.setStatus("current")
_HpnicfLBv2RSStatSentResponses_Type = Counter64
_HpnicfLBv2RSStatSentResponses_Object = MibTableColumn
hpnicfLBv2RSStatSentResponses = _HpnicfLBv2RSStatSentResponses_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 4, 2, 1, 12),
    _HpnicfLBv2RSStatSentResponses_Type()
)
hpnicfLBv2RSStatSentResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLBv2RSStatSentResponses.setStatus("current")
_HpnicfLBv2SFTables_ObjectIdentity = ObjectIdentity
hpnicfLBv2SFTables = _HpnicfLBv2SFTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 5)
)
_HpnicfLBv2SFTable_Object = MibTable
hpnicfLBv2SFTable = _HpnicfLBv2SFTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 5, 1)
)
if mibBuilder.loadTexts:
    hpnicfLBv2SFTable.setStatus("current")
_HpnicfLBv2SFEntry_Object = MibTableRow
hpnicfLBv2SFEntry = _HpnicfLBv2SFEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 5, 1, 1)
)
hpnicfLBv2SFEntry.setIndexNames(
    (0, "HPN-ICF-LBV2-MIB", "hpnicfLBv2SFName"),
)
if mibBuilder.loadTexts:
    hpnicfLBv2SFEntry.setStatus("current")


class _HpnicfLBv2SFName_Type(DisplayString):
    """Custom type hpnicfLBv2SFName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_HpnicfLBv2SFName_Type.__name__ = "DisplayString"
_HpnicfLBv2SFName_Object = MibTableColumn
hpnicfLBv2SFName = _HpnicfLBv2SFName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 5, 1, 1, 1),
    _HpnicfLBv2SFName_Type()
)
hpnicfLBv2SFName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfLBv2SFName.setStatus("current")
_HpnicfLBv2SFRowStatus_Type = RowStatus
_HpnicfLBv2SFRowStatus_Object = MibTableColumn
hpnicfLBv2SFRowStatus = _HpnicfLBv2SFRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 5, 1, 1, 2),
    _HpnicfLBv2SFRowStatus_Type()
)
hpnicfLBv2SFRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfLBv2SFRowStatus.setStatus("current")
_HpnicfLBv2SFStatsTable_Object = MibTable
hpnicfLBv2SFStatsTable = _HpnicfLBv2SFStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 5, 2)
)
if mibBuilder.loadTexts:
    hpnicfLBv2SFStatsTable.setStatus("current")
_HpnicfLBv2SFStatsEntry_Object = MibTableRow
hpnicfLBv2SFStatsEntry = _HpnicfLBv2SFStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 5, 2, 1)
)
hpnicfLBv2SFStatsEntry.setIndexNames(
    (0, "HPN-ICF-LBV2-MIB", "hpnicfLBv2SFName"),
    (0, "HPN-ICF-LBV2-MIB", "hpnicfLBv2SFStatChassis"),
    (0, "HPN-ICF-LBV2-MIB", "hpnicfLBv2SFStatSlot"),
    (0, "HPN-ICF-LBV2-MIB", "hpnicfLBv2SFStatCpuid"),
)
if mibBuilder.loadTexts:
    hpnicfLBv2SFStatsEntry.setStatus("current")


class _HpnicfLBv2SFStatChassis_Type(Unsigned32):
    """Custom type hpnicfLBv2SFStatChassis based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfLBv2SFStatChassis_Type.__name__ = "Unsigned32"
_HpnicfLBv2SFStatChassis_Object = MibTableColumn
hpnicfLBv2SFStatChassis = _HpnicfLBv2SFStatChassis_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 5, 2, 1, 1),
    _HpnicfLBv2SFStatChassis_Type()
)
hpnicfLBv2SFStatChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfLBv2SFStatChassis.setStatus("current")


class _HpnicfLBv2SFStatSlot_Type(Unsigned32):
    """Custom type hpnicfLBv2SFStatSlot based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfLBv2SFStatSlot_Type.__name__ = "Unsigned32"
_HpnicfLBv2SFStatSlot_Object = MibTableColumn
hpnicfLBv2SFStatSlot = _HpnicfLBv2SFStatSlot_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 5, 2, 1, 2),
    _HpnicfLBv2SFStatSlot_Type()
)
hpnicfLBv2SFStatSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfLBv2SFStatSlot.setStatus("current")


class _HpnicfLBv2SFStatCpuid_Type(Unsigned32):
    """Custom type hpnicfLBv2SFStatCpuid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfLBv2SFStatCpuid_Type.__name__ = "Unsigned32"
_HpnicfLBv2SFStatCpuid_Object = MibTableColumn
hpnicfLBv2SFStatCpuid = _HpnicfLBv2SFStatCpuid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 5, 2, 1, 3),
    _HpnicfLBv2SFStatCpuid_Type()
)
hpnicfLBv2SFStatCpuid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfLBv2SFStatCpuid.setStatus("current")
_HpnicfLBv2SFStatTotalConnections_Type = Counter64
_HpnicfLBv2SFStatTotalConnections_Object = MibTableColumn
hpnicfLBv2SFStatTotalConnections = _HpnicfLBv2SFStatTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 5, 2, 1, 4),
    _HpnicfLBv2SFStatTotalConnections_Type()
)
hpnicfLBv2SFStatTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLBv2SFStatTotalConnections.setStatus("current")
_HpnicfLBv2SFStatActiveConnections_Type = Unsigned32
_HpnicfLBv2SFStatActiveConnections_Object = MibTableColumn
hpnicfLBv2SFStatActiveConnections = _HpnicfLBv2SFStatActiveConnections_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 5, 2, 1, 5),
    _HpnicfLBv2SFStatActiveConnections_Type()
)
hpnicfLBv2SFStatActiveConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLBv2SFStatActiveConnections.setStatus("current")
_HpnicfLBv2SFStatServerSidePKTsIn_Type = Counter64
_HpnicfLBv2SFStatServerSidePKTsIn_Object = MibTableColumn
hpnicfLBv2SFStatServerSidePKTsIn = _HpnicfLBv2SFStatServerSidePKTsIn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 5, 2, 1, 6),
    _HpnicfLBv2SFStatServerSidePKTsIn_Type()
)
hpnicfLBv2SFStatServerSidePKTsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLBv2SFStatServerSidePKTsIn.setStatus("current")
_HpnicfLBv2SFStatServerSidePKTsOut_Type = Counter64
_HpnicfLBv2SFStatServerSidePKTsOut_Object = MibTableColumn
hpnicfLBv2SFStatServerSidePKTsOut = _HpnicfLBv2SFStatServerSidePKTsOut_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 5, 2, 1, 7),
    _HpnicfLBv2SFStatServerSidePKTsOut_Type()
)
hpnicfLBv2SFStatServerSidePKTsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLBv2SFStatServerSidePKTsOut.setStatus("current")
_HpnicfLBv2SFStatDroppedPackets_Type = Counter64
_HpnicfLBv2SFStatDroppedPackets_Object = MibTableColumn
hpnicfLBv2SFStatDroppedPackets = _HpnicfLBv2SFStatDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 5, 2, 1, 8),
    _HpnicfLBv2SFStatDroppedPackets_Type()
)
hpnicfLBv2SFStatDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLBv2SFStatDroppedPackets.setStatus("current")
_HpnicfLBv2SFStatServerSideBytesIn_Type = Counter64
_HpnicfLBv2SFStatServerSideBytesIn_Object = MibTableColumn
hpnicfLBv2SFStatServerSideBytesIn = _HpnicfLBv2SFStatServerSideBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 5, 2, 1, 9),
    _HpnicfLBv2SFStatServerSideBytesIn_Type()
)
hpnicfLBv2SFStatServerSideBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLBv2SFStatServerSideBytesIn.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfLBv2SFStatServerSideBytesIn.setUnits("byte")
_HpnicfLBv2SFStatServerSideBytesOut_Type = Counter64
_HpnicfLBv2SFStatServerSideBytesOut_Object = MibTableColumn
hpnicfLBv2SFStatServerSideBytesOut = _HpnicfLBv2SFStatServerSideBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 5, 2, 1, 10),
    _HpnicfLBv2SFStatServerSideBytesOut_Type()
)
hpnicfLBv2SFStatServerSideBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLBv2SFStatServerSideBytesOut.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfLBv2SFStatServerSideBytesOut.setUnits("byte")
_HpnicfLBv2SFStatReceivedRequests_Type = Counter64
_HpnicfLBv2SFStatReceivedRequests_Object = MibTableColumn
hpnicfLBv2SFStatReceivedRequests = _HpnicfLBv2SFStatReceivedRequests_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 5, 2, 1, 11),
    _HpnicfLBv2SFStatReceivedRequests_Type()
)
hpnicfLBv2SFStatReceivedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLBv2SFStatReceivedRequests.setStatus("current")
_HpnicfLBv2SFStatSentResponses_Type = Counter64
_HpnicfLBv2SFStatSentResponses_Object = MibTableColumn
hpnicfLBv2SFStatSentResponses = _HpnicfLBv2SFStatSentResponses_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 5, 2, 1, 12),
    _HpnicfLBv2SFStatSentResponses_Type()
)
hpnicfLBv2SFStatSentResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLBv2SFStatSentResponses.setStatus("current")
_HpnicfLBv2Trap_ObjectIdentity = ObjectIdentity
hpnicfLBv2Trap = _HpnicfLBv2Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 6)
)
_HpnicfLBv2TrapPrefix_ObjectIdentity = ObjectIdentity
hpnicfLBv2TrapPrefix = _HpnicfLBv2TrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 6, 0)
)

# Managed Objects groups


# Notification objects

hpnicfLBv2VSConnOverloadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 6, 0, 1)
)
hpnicfLBv2VSConnOverloadTrap.setObjects(
      *(("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSName"),
        ("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSConnectionsLimit"),
        ("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSStatChassis"),
        ("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSStatSlot"),
        ("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSStatCpuid"),
        ("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSStatActiveConnections"))
)
if mibBuilder.loadTexts:
    hpnicfLBv2VSConnOverloadTrap.setStatus(
        "current"
    )

hpnicfLBv2VSConnRecoveryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 6, 0, 2)
)
hpnicfLBv2VSConnRecoveryTrap.setObjects(
      *(("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSName"),
        ("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSConnectionsLimit"),
        ("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSStatChassis"),
        ("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSStatSlot"),
        ("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSStatCpuid"),
        ("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSStatActiveConnections"))
)
if mibBuilder.loadTexts:
    hpnicfLBv2VSConnRecoveryTrap.setStatus(
        "current"
    )

hpnicfLBv2VSConnsRateOverloadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 6, 0, 3)
)
hpnicfLBv2VSConnsRateOverloadTrap.setObjects(
      *(("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSName"),
        ("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSConnectionsRateLimit"),
        ("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSStatChassis"),
        ("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSStatSlot"),
        ("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSStatCpuid"),
        ("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSStatConnectionsRate"))
)
if mibBuilder.loadTexts:
    hpnicfLBv2VSConnsRateOverloadTrap.setStatus(
        "current"
    )

hpnicfLBv2VSConnsRateRecoveryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 6, 0, 4)
)
hpnicfLBv2VSConnsRateRecoveryTrap.setObjects(
      *(("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSName"),
        ("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSConnectionsRateLimit"),
        ("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSStatChassis"),
        ("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSStatSlot"),
        ("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSStatCpuid"),
        ("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSStatConnectionsRate"))
)
if mibBuilder.loadTexts:
    hpnicfLBv2VSConnsRateRecoveryTrap.setStatus(
        "current"
    )

hpnicfLBv2VSActiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 6, 0, 5)
)
hpnicfLBv2VSActiveTrap.setObjects(
    ("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSName")
)
if mibBuilder.loadTexts:
    hpnicfLBv2VSActiveTrap.setStatus(
        "current"
    )

hpnicfLBv2VSInactiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 6, 0, 6)
)
hpnicfLBv2VSInactiveTrap.setObjects(
    ("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSName")
)
if mibBuilder.loadTexts:
    hpnicfLBv2VSInactiveTrap.setStatus(
        "current"
    )

hpnicfLBv2RSAvailableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 6, 0, 7)
)
hpnicfLBv2RSAvailableTrap.setObjects(
    ("HPN-ICF-LBV2-MIB", "hpnicfLBv2RSName")
)
if mibBuilder.loadTexts:
    hpnicfLBv2RSAvailableTrap.setStatus(
        "current"
    )

hpnicfLBv2RSUnavailableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 6, 0, 8)
)
hpnicfLBv2RSUnavailableTrap.setObjects(
    ("HPN-ICF-LBV2-MIB", "hpnicfLBv2RSName")
)
if mibBuilder.loadTexts:
    hpnicfLBv2RSUnavailableTrap.setStatus(
        "current"
    )

hpnicfLBv2SFActiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 6, 0, 9)
)
hpnicfLBv2SFActiveTrap.setObjects(
    ("HPN-ICF-LBV2-MIB", "hpnicfLBv2SFName")
)
if mibBuilder.loadTexts:
    hpnicfLBv2SFActiveTrap.setStatus(
        "current"
    )

hpnicfLBv2SFInactiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 6, 0, 10)
)
hpnicfLBv2SFInactiveTrap.setObjects(
    ("HPN-ICF-LBV2-MIB", "hpnicfLBv2SFName")
)
if mibBuilder.loadTexts:
    hpnicfLBv2SFInactiveTrap.setStatus(
        "current"
    )

hpnicfLBv2ActionInUseSFChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 6, 0, 11)
)
hpnicfLBv2ActionInUseSFChangeTrap.setObjects(
      *(("HPN-ICF-LBV2-MIB", "hpnicfLBv2ActionName"),
        ("HPN-ICF-LBV2-MIB", "hpnicfLBv2ActionDefaultSF"),
        ("HPN-ICF-LBV2-MIB", "hpnicfLBv2ActionBackupSF"),
        ("HPN-ICF-LBV2-MIB", "hpnicfLBv2ActionInUseSF"))
)
if mibBuilder.loadTexts:
    hpnicfLBv2ActionInUseSFChangeTrap.setStatus(
        "current"
    )

hpnicfLBv2VSInUseSFChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 6, 0, 12)
)
hpnicfLBv2VSInUseSFChangeTrap.setObjects(
      *(("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSName"),
        ("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSDefaultSF"),
        ("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSBackupSF"),
        ("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSInUseSF"))
)
if mibBuilder.loadTexts:
    hpnicfLBv2VSInUseSFChangeTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-LBV2-MIB",
    **{"hpnicfLBv2": hpnicfLBv2,
       "hpnicfLBv2GlobalObjects": hpnicfLBv2GlobalObjects,
       "hpnicfLBv2TrapEnable": hpnicfLBv2TrapEnable,
       "hpnicfLBv2ActionTables": hpnicfLBv2ActionTables,
       "hpnicfLBv2ActionTable": hpnicfLBv2ActionTable,
       "hpnicfLBv2ActionEntry": hpnicfLBv2ActionEntry,
       "hpnicfLBv2ActionName": hpnicfLBv2ActionName,
       "hpnicfLBv2ActionDefaultSF": hpnicfLBv2ActionDefaultSF,
       "hpnicfLBv2ActionBackupSF": hpnicfLBv2ActionBackupSF,
       "hpnicfLBv2ActionInUseSF": hpnicfLBv2ActionInUseSF,
       "hpnicfLBv2ActionRowStatus": hpnicfLBv2ActionRowStatus,
       "hpnicfLBv2VSTables": hpnicfLBv2VSTables,
       "hpnicfLBv2VSTable": hpnicfLBv2VSTable,
       "hpnicfLBv2VSEntry": hpnicfLBv2VSEntry,
       "hpnicfLBv2VSName": hpnicfLBv2VSName,
       "hpnicfLBv2VSConnectionsLimit": hpnicfLBv2VSConnectionsLimit,
       "hpnicfLBv2VSConnectionsRateLimit": hpnicfLBv2VSConnectionsRateLimit,
       "hpnicfLBv2VSDefaultSF": hpnicfLBv2VSDefaultSF,
       "hpnicfLBv2VSBackupSF": hpnicfLBv2VSBackupSF,
       "hpnicfLBv2VSInUseSF": hpnicfLBv2VSInUseSF,
       "hpnicfLBv2VSRowStatus": hpnicfLBv2VSRowStatus,
       "hpnicfLBv2VSStatsTable": hpnicfLBv2VSStatsTable,
       "hpnicfLBv2VSStatsEntry": hpnicfLBv2VSStatsEntry,
       "hpnicfLBv2VSStatChassis": hpnicfLBv2VSStatChassis,
       "hpnicfLBv2VSStatSlot": hpnicfLBv2VSStatSlot,
       "hpnicfLBv2VSStatCpuid": hpnicfLBv2VSStatCpuid,
       "hpnicfLBv2VSStatTotalConnections": hpnicfLBv2VSStatTotalConnections,
       "hpnicfLBv2VSStatActiveConnections": hpnicfLBv2VSStatActiveConnections,
       "hpnicfLBv2VSStatClientSidePKTsIn": hpnicfLBv2VSStatClientSidePKTsIn,
       "hpnicfLBv2VSStatClientSidePKTsOut": hpnicfLBv2VSStatClientSidePKTsOut,
       "hpnicfLBv2VSStatDroppedPackets": hpnicfLBv2VSStatDroppedPackets,
       "hpnicfLBv2VSStatClientSideBytesIn": hpnicfLBv2VSStatClientSideBytesIn,
       "hpnicfLBv2VSStatClientSideBytesOut": hpnicfLBv2VSStatClientSideBytesOut,
       "hpnicfLBv2VSStatReceivedRequests": hpnicfLBv2VSStatReceivedRequests,
       "hpnicfLBv2VSStatSentResponses": hpnicfLBv2VSStatSentResponses,
       "hpnicfLBv2VSStatConnectionsRate": hpnicfLBv2VSStatConnectionsRate,
       "hpnicfLBv2RSTables": hpnicfLBv2RSTables,
       "hpnicfLBv2RSTable": hpnicfLBv2RSTable,
       "hpnicfLBv2RSEntry": hpnicfLBv2RSEntry,
       "hpnicfLBv2RSName": hpnicfLBv2RSName,
       "hpnicfLBv2RSRowStatus": hpnicfLBv2RSRowStatus,
       "hpnicfLBv2RSStatsTable": hpnicfLBv2RSStatsTable,
       "hpnicfLBv2RSStatsEntry": hpnicfLBv2RSStatsEntry,
       "hpnicfLBv2RSStatChassis": hpnicfLBv2RSStatChassis,
       "hpnicfLBv2RSStatSlot": hpnicfLBv2RSStatSlot,
       "hpnicfLBv2RSStatCpuid": hpnicfLBv2RSStatCpuid,
       "hpnicfLBv2RSStatTotalConnections": hpnicfLBv2RSStatTotalConnections,
       "hpnicfLBv2RSStatActiveConnections": hpnicfLBv2RSStatActiveConnections,
       "hpnicfLBv2RSStatServerSidePKTsIn": hpnicfLBv2RSStatServerSidePKTsIn,
       "hpnicfLBv2RSStatServerSidePKTsOut": hpnicfLBv2RSStatServerSidePKTsOut,
       "hpnicfLBv2RSStatDroppedPackets": hpnicfLBv2RSStatDroppedPackets,
       "hpnicfLBv2RSStatServerSideBytesIn": hpnicfLBv2RSStatServerSideBytesIn,
       "hpnicfLBv2RSStatServerSideBytesOut": hpnicfLBv2RSStatServerSideBytesOut,
       "hpnicfLBv2RSStatReceivedRequests": hpnicfLBv2RSStatReceivedRequests,
       "hpnicfLBv2RSStatSentResponses": hpnicfLBv2RSStatSentResponses,
       "hpnicfLBv2SFTables": hpnicfLBv2SFTables,
       "hpnicfLBv2SFTable": hpnicfLBv2SFTable,
       "hpnicfLBv2SFEntry": hpnicfLBv2SFEntry,
       "hpnicfLBv2SFName": hpnicfLBv2SFName,
       "hpnicfLBv2SFRowStatus": hpnicfLBv2SFRowStatus,
       "hpnicfLBv2SFStatsTable": hpnicfLBv2SFStatsTable,
       "hpnicfLBv2SFStatsEntry": hpnicfLBv2SFStatsEntry,
       "hpnicfLBv2SFStatChassis": hpnicfLBv2SFStatChassis,
       "hpnicfLBv2SFStatSlot": hpnicfLBv2SFStatSlot,
       "hpnicfLBv2SFStatCpuid": hpnicfLBv2SFStatCpuid,
       "hpnicfLBv2SFStatTotalConnections": hpnicfLBv2SFStatTotalConnections,
       "hpnicfLBv2SFStatActiveConnections": hpnicfLBv2SFStatActiveConnections,
       "hpnicfLBv2SFStatServerSidePKTsIn": hpnicfLBv2SFStatServerSidePKTsIn,
       "hpnicfLBv2SFStatServerSidePKTsOut": hpnicfLBv2SFStatServerSidePKTsOut,
       "hpnicfLBv2SFStatDroppedPackets": hpnicfLBv2SFStatDroppedPackets,
       "hpnicfLBv2SFStatServerSideBytesIn": hpnicfLBv2SFStatServerSideBytesIn,
       "hpnicfLBv2SFStatServerSideBytesOut": hpnicfLBv2SFStatServerSideBytesOut,
       "hpnicfLBv2SFStatReceivedRequests": hpnicfLBv2SFStatReceivedRequests,
       "hpnicfLBv2SFStatSentResponses": hpnicfLBv2SFStatSentResponses,
       "hpnicfLBv2Trap": hpnicfLBv2Trap,
       "hpnicfLBv2TrapPrefix": hpnicfLBv2TrapPrefix,
       "hpnicfLBv2VSConnOverloadTrap": hpnicfLBv2VSConnOverloadTrap,
       "hpnicfLBv2VSConnRecoveryTrap": hpnicfLBv2VSConnRecoveryTrap,
       "hpnicfLBv2VSConnsRateOverloadTrap": hpnicfLBv2VSConnsRateOverloadTrap,
       "hpnicfLBv2VSConnsRateRecoveryTrap": hpnicfLBv2VSConnsRateRecoveryTrap,
       "hpnicfLBv2VSActiveTrap": hpnicfLBv2VSActiveTrap,
       "hpnicfLBv2VSInactiveTrap": hpnicfLBv2VSInactiveTrap,
       "hpnicfLBv2RSAvailableTrap": hpnicfLBv2RSAvailableTrap,
       "hpnicfLBv2RSUnavailableTrap": hpnicfLBv2RSUnavailableTrap,
       "hpnicfLBv2SFActiveTrap": hpnicfLBv2SFActiveTrap,
       "hpnicfLBv2SFInactiveTrap": hpnicfLBv2SFInactiveTrap,
       "hpnicfLBv2ActionInUseSFChangeTrap": hpnicfLBv2ActionInUseSFChangeTrap,
       "hpnicfLBv2VSInUseSFChangeTrap": hpnicfLBv2VSInUseSFChangeTrap}
)
