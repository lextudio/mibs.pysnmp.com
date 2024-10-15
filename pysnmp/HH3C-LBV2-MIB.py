# SNMP MIB module (HH3C-LBV2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-LBV2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:46 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cLBv2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148)
)
hh3cLBv2.setRevisions(
        ("2013-11-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cLBv2GlobalObjects_ObjectIdentity = ObjectIdentity
hh3cLBv2GlobalObjects = _Hh3cLBv2GlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 1)
)


class _Hh3cLBv2TrapEnable_Type(Integer32):
    """Custom type hh3cLBv2TrapEnable based on Integer32"""
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


_Hh3cLBv2TrapEnable_Type.__name__ = "Integer32"
_Hh3cLBv2TrapEnable_Object = MibScalar
hh3cLBv2TrapEnable = _Hh3cLBv2TrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 1, 1),
    _Hh3cLBv2TrapEnable_Type()
)
hh3cLBv2TrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLBv2TrapEnable.setStatus("current")
_Hh3cLBv2ActionTables_ObjectIdentity = ObjectIdentity
hh3cLBv2ActionTables = _Hh3cLBv2ActionTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 2)
)
_Hh3cLBv2ActionTable_Object = MibTable
hh3cLBv2ActionTable = _Hh3cLBv2ActionTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cLBv2ActionTable.setStatus("current")
_Hh3cLBv2ActionEntry_Object = MibTableRow
hh3cLBv2ActionEntry = _Hh3cLBv2ActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 2, 1, 1)
)
hh3cLBv2ActionEntry.setIndexNames(
    (0, "HH3C-LBV2-MIB", "hh3cLBv2ActionName"),
)
if mibBuilder.loadTexts:
    hh3cLBv2ActionEntry.setStatus("current")


class _Hh3cLBv2ActionName_Type(DisplayString):
    """Custom type hh3cLBv2ActionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cLBv2ActionName_Type.__name__ = "DisplayString"
_Hh3cLBv2ActionName_Object = MibTableColumn
hh3cLBv2ActionName = _Hh3cLBv2ActionName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 2, 1, 1, 1),
    _Hh3cLBv2ActionName_Type()
)
hh3cLBv2ActionName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cLBv2ActionName.setStatus("current")


class _Hh3cLBv2ActionDefaultSF_Type(DisplayString):
    """Custom type hh3cLBv2ActionDefaultSF based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Hh3cLBv2ActionDefaultSF_Type.__name__ = "DisplayString"
_Hh3cLBv2ActionDefaultSF_Object = MibTableColumn
hh3cLBv2ActionDefaultSF = _Hh3cLBv2ActionDefaultSF_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 2, 1, 1, 2),
    _Hh3cLBv2ActionDefaultSF_Type()
)
hh3cLBv2ActionDefaultSF.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cLBv2ActionDefaultSF.setStatus("current")


class _Hh3cLBv2ActionBackupSF_Type(DisplayString):
    """Custom type hh3cLBv2ActionBackupSF based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Hh3cLBv2ActionBackupSF_Type.__name__ = "DisplayString"
_Hh3cLBv2ActionBackupSF_Object = MibTableColumn
hh3cLBv2ActionBackupSF = _Hh3cLBv2ActionBackupSF_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 2, 1, 1, 3),
    _Hh3cLBv2ActionBackupSF_Type()
)
hh3cLBv2ActionBackupSF.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cLBv2ActionBackupSF.setStatus("current")


class _Hh3cLBv2ActionInUseSF_Type(DisplayString):
    """Custom type hh3cLBv2ActionInUseSF based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Hh3cLBv2ActionInUseSF_Type.__name__ = "DisplayString"
_Hh3cLBv2ActionInUseSF_Object = MibTableColumn
hh3cLBv2ActionInUseSF = _Hh3cLBv2ActionInUseSF_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 2, 1, 1, 4),
    _Hh3cLBv2ActionInUseSF_Type()
)
hh3cLBv2ActionInUseSF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLBv2ActionInUseSF.setStatus("current")
_Hh3cLBv2ActionRowStatus_Type = RowStatus
_Hh3cLBv2ActionRowStatus_Object = MibTableColumn
hh3cLBv2ActionRowStatus = _Hh3cLBv2ActionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 2, 1, 1, 5),
    _Hh3cLBv2ActionRowStatus_Type()
)
hh3cLBv2ActionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cLBv2ActionRowStatus.setStatus("current")
_Hh3cLBv2VSTables_ObjectIdentity = ObjectIdentity
hh3cLBv2VSTables = _Hh3cLBv2VSTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 3)
)
_Hh3cLBv2VSTable_Object = MibTable
hh3cLBv2VSTable = _Hh3cLBv2VSTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 3, 1)
)
if mibBuilder.loadTexts:
    hh3cLBv2VSTable.setStatus("current")
_Hh3cLBv2VSEntry_Object = MibTableRow
hh3cLBv2VSEntry = _Hh3cLBv2VSEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 3, 1, 1)
)
hh3cLBv2VSEntry.setIndexNames(
    (0, "HH3C-LBV2-MIB", "hh3cLBv2VSName"),
)
if mibBuilder.loadTexts:
    hh3cLBv2VSEntry.setStatus("current")


class _Hh3cLBv2VSName_Type(DisplayString):
    """Custom type hh3cLBv2VSName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cLBv2VSName_Type.__name__ = "DisplayString"
_Hh3cLBv2VSName_Object = MibTableColumn
hh3cLBv2VSName = _Hh3cLBv2VSName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 3, 1, 1, 1),
    _Hh3cLBv2VSName_Type()
)
hh3cLBv2VSName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cLBv2VSName.setStatus("current")


class _Hh3cLBv2VSConnectionsLimit_Type(Unsigned32):
    """Custom type hh3cLBv2VSConnectionsLimit based on Unsigned32"""
    defaultValue = 0


_Hh3cLBv2VSConnectionsLimit_Object = MibTableColumn
hh3cLBv2VSConnectionsLimit = _Hh3cLBv2VSConnectionsLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 3, 1, 1, 2),
    _Hh3cLBv2VSConnectionsLimit_Type()
)
hh3cLBv2VSConnectionsLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cLBv2VSConnectionsLimit.setStatus("current")


class _Hh3cLBv2VSConnectionsRateLimit_Type(Unsigned32):
    """Custom type hh3cLBv2VSConnectionsRateLimit based on Unsigned32"""
    defaultValue = 0


_Hh3cLBv2VSConnectionsRateLimit_Object = MibTableColumn
hh3cLBv2VSConnectionsRateLimit = _Hh3cLBv2VSConnectionsRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 3, 1, 1, 3),
    _Hh3cLBv2VSConnectionsRateLimit_Type()
)
hh3cLBv2VSConnectionsRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cLBv2VSConnectionsRateLimit.setStatus("current")


class _Hh3cLBv2VSDefaultSF_Type(DisplayString):
    """Custom type hh3cLBv2VSDefaultSF based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Hh3cLBv2VSDefaultSF_Type.__name__ = "DisplayString"
_Hh3cLBv2VSDefaultSF_Object = MibTableColumn
hh3cLBv2VSDefaultSF = _Hh3cLBv2VSDefaultSF_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 3, 1, 1, 4),
    _Hh3cLBv2VSDefaultSF_Type()
)
hh3cLBv2VSDefaultSF.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cLBv2VSDefaultSF.setStatus("current")


class _Hh3cLBv2VSBackupSF_Type(DisplayString):
    """Custom type hh3cLBv2VSBackupSF based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Hh3cLBv2VSBackupSF_Type.__name__ = "DisplayString"
_Hh3cLBv2VSBackupSF_Object = MibTableColumn
hh3cLBv2VSBackupSF = _Hh3cLBv2VSBackupSF_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 3, 1, 1, 5),
    _Hh3cLBv2VSBackupSF_Type()
)
hh3cLBv2VSBackupSF.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cLBv2VSBackupSF.setStatus("current")


class _Hh3cLBv2VSInUseSF_Type(DisplayString):
    """Custom type hh3cLBv2VSInUseSF based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Hh3cLBv2VSInUseSF_Type.__name__ = "DisplayString"
_Hh3cLBv2VSInUseSF_Object = MibTableColumn
hh3cLBv2VSInUseSF = _Hh3cLBv2VSInUseSF_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 3, 1, 1, 6),
    _Hh3cLBv2VSInUseSF_Type()
)
hh3cLBv2VSInUseSF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLBv2VSInUseSF.setStatus("current")
_Hh3cLBv2VSRowStatus_Type = RowStatus
_Hh3cLBv2VSRowStatus_Object = MibTableColumn
hh3cLBv2VSRowStatus = _Hh3cLBv2VSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 3, 1, 1, 7),
    _Hh3cLBv2VSRowStatus_Type()
)
hh3cLBv2VSRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cLBv2VSRowStatus.setStatus("current")
_Hh3cLBv2VSStatsTable_Object = MibTable
hh3cLBv2VSStatsTable = _Hh3cLBv2VSStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 3, 2)
)
if mibBuilder.loadTexts:
    hh3cLBv2VSStatsTable.setStatus("current")
_Hh3cLBv2VSStatsEntry_Object = MibTableRow
hh3cLBv2VSStatsEntry = _Hh3cLBv2VSStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 3, 2, 1)
)
hh3cLBv2VSStatsEntry.setIndexNames(
    (0, "HH3C-LBV2-MIB", "hh3cLBv2VSName"),
    (0, "HH3C-LBV2-MIB", "hh3cLBv2VSStatChassis"),
    (0, "HH3C-LBV2-MIB", "hh3cLBv2VSStatSlot"),
    (0, "HH3C-LBV2-MIB", "hh3cLBv2VSStatCpuid"),
)
if mibBuilder.loadTexts:
    hh3cLBv2VSStatsEntry.setStatus("current")


class _Hh3cLBv2VSStatChassis_Type(Unsigned32):
    """Custom type hh3cLBv2VSStatChassis based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cLBv2VSStatChassis_Type.__name__ = "Unsigned32"
_Hh3cLBv2VSStatChassis_Object = MibTableColumn
hh3cLBv2VSStatChassis = _Hh3cLBv2VSStatChassis_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 3, 2, 1, 1),
    _Hh3cLBv2VSStatChassis_Type()
)
hh3cLBv2VSStatChassis.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cLBv2VSStatChassis.setStatus("current")


class _Hh3cLBv2VSStatSlot_Type(Unsigned32):
    """Custom type hh3cLBv2VSStatSlot based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cLBv2VSStatSlot_Type.__name__ = "Unsigned32"
_Hh3cLBv2VSStatSlot_Object = MibTableColumn
hh3cLBv2VSStatSlot = _Hh3cLBv2VSStatSlot_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 3, 2, 1, 2),
    _Hh3cLBv2VSStatSlot_Type()
)
hh3cLBv2VSStatSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cLBv2VSStatSlot.setStatus("current")


class _Hh3cLBv2VSStatCpuid_Type(Unsigned32):
    """Custom type hh3cLBv2VSStatCpuid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cLBv2VSStatCpuid_Type.__name__ = "Unsigned32"
_Hh3cLBv2VSStatCpuid_Object = MibTableColumn
hh3cLBv2VSStatCpuid = _Hh3cLBv2VSStatCpuid_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 3, 2, 1, 3),
    _Hh3cLBv2VSStatCpuid_Type()
)
hh3cLBv2VSStatCpuid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cLBv2VSStatCpuid.setStatus("current")
_Hh3cLBv2VSStatTotalConnections_Type = Counter64
_Hh3cLBv2VSStatTotalConnections_Object = MibTableColumn
hh3cLBv2VSStatTotalConnections = _Hh3cLBv2VSStatTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 3, 2, 1, 4),
    _Hh3cLBv2VSStatTotalConnections_Type()
)
hh3cLBv2VSStatTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLBv2VSStatTotalConnections.setStatus("current")
_Hh3cLBv2VSStatActiveConnections_Type = Unsigned32
_Hh3cLBv2VSStatActiveConnections_Object = MibTableColumn
hh3cLBv2VSStatActiveConnections = _Hh3cLBv2VSStatActiveConnections_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 3, 2, 1, 5),
    _Hh3cLBv2VSStatActiveConnections_Type()
)
hh3cLBv2VSStatActiveConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLBv2VSStatActiveConnections.setStatus("current")
_Hh3cLBv2VSStatClientSidePKTsIn_Type = Counter64
_Hh3cLBv2VSStatClientSidePKTsIn_Object = MibTableColumn
hh3cLBv2VSStatClientSidePKTsIn = _Hh3cLBv2VSStatClientSidePKTsIn_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 3, 2, 1, 6),
    _Hh3cLBv2VSStatClientSidePKTsIn_Type()
)
hh3cLBv2VSStatClientSidePKTsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLBv2VSStatClientSidePKTsIn.setStatus("current")
_Hh3cLBv2VSStatClientSidePKTsOut_Type = Counter64
_Hh3cLBv2VSStatClientSidePKTsOut_Object = MibTableColumn
hh3cLBv2VSStatClientSidePKTsOut = _Hh3cLBv2VSStatClientSidePKTsOut_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 3, 2, 1, 7),
    _Hh3cLBv2VSStatClientSidePKTsOut_Type()
)
hh3cLBv2VSStatClientSidePKTsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLBv2VSStatClientSidePKTsOut.setStatus("current")
_Hh3cLBv2VSStatDroppedPackets_Type = Counter64
_Hh3cLBv2VSStatDroppedPackets_Object = MibTableColumn
hh3cLBv2VSStatDroppedPackets = _Hh3cLBv2VSStatDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 3, 2, 1, 8),
    _Hh3cLBv2VSStatDroppedPackets_Type()
)
hh3cLBv2VSStatDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLBv2VSStatDroppedPackets.setStatus("current")
_Hh3cLBv2VSStatClientSideBytesIn_Type = Counter64
_Hh3cLBv2VSStatClientSideBytesIn_Object = MibTableColumn
hh3cLBv2VSStatClientSideBytesIn = _Hh3cLBv2VSStatClientSideBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 3, 2, 1, 9),
    _Hh3cLBv2VSStatClientSideBytesIn_Type()
)
hh3cLBv2VSStatClientSideBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLBv2VSStatClientSideBytesIn.setStatus("current")
if mibBuilder.loadTexts:
    hh3cLBv2VSStatClientSideBytesIn.setUnits("byte")
_Hh3cLBv2VSStatClientSideBytesOut_Type = Counter64
_Hh3cLBv2VSStatClientSideBytesOut_Object = MibTableColumn
hh3cLBv2VSStatClientSideBytesOut = _Hh3cLBv2VSStatClientSideBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 3, 2, 1, 10),
    _Hh3cLBv2VSStatClientSideBytesOut_Type()
)
hh3cLBv2VSStatClientSideBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLBv2VSStatClientSideBytesOut.setStatus("current")
if mibBuilder.loadTexts:
    hh3cLBv2VSStatClientSideBytesOut.setUnits("byte")
_Hh3cLBv2VSStatReceivedRequests_Type = Counter64
_Hh3cLBv2VSStatReceivedRequests_Object = MibTableColumn
hh3cLBv2VSStatReceivedRequests = _Hh3cLBv2VSStatReceivedRequests_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 3, 2, 1, 11),
    _Hh3cLBv2VSStatReceivedRequests_Type()
)
hh3cLBv2VSStatReceivedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLBv2VSStatReceivedRequests.setStatus("current")
_Hh3cLBv2VSStatSentResponses_Type = Counter64
_Hh3cLBv2VSStatSentResponses_Object = MibTableColumn
hh3cLBv2VSStatSentResponses = _Hh3cLBv2VSStatSentResponses_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 3, 2, 1, 12),
    _Hh3cLBv2VSStatSentResponses_Type()
)
hh3cLBv2VSStatSentResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLBv2VSStatSentResponses.setStatus("current")
_Hh3cLBv2VSStatConnectionsRate_Type = Unsigned32
_Hh3cLBv2VSStatConnectionsRate_Object = MibTableColumn
hh3cLBv2VSStatConnectionsRate = _Hh3cLBv2VSStatConnectionsRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 3, 2, 1, 13),
    _Hh3cLBv2VSStatConnectionsRate_Type()
)
hh3cLBv2VSStatConnectionsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLBv2VSStatConnectionsRate.setStatus("current")
if mibBuilder.loadTexts:
    hh3cLBv2VSStatConnectionsRate.setUnits("cps")
_Hh3cLBv2RSTables_ObjectIdentity = ObjectIdentity
hh3cLBv2RSTables = _Hh3cLBv2RSTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 4)
)
_Hh3cLBv2RSTable_Object = MibTable
hh3cLBv2RSTable = _Hh3cLBv2RSTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 4, 1)
)
if mibBuilder.loadTexts:
    hh3cLBv2RSTable.setStatus("current")
_Hh3cLBv2RSEntry_Object = MibTableRow
hh3cLBv2RSEntry = _Hh3cLBv2RSEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 4, 1, 1)
)
hh3cLBv2RSEntry.setIndexNames(
    (0, "HH3C-LBV2-MIB", "hh3cLBv2RSName"),
)
if mibBuilder.loadTexts:
    hh3cLBv2RSEntry.setStatus("current")


class _Hh3cLBv2RSName_Type(DisplayString):
    """Custom type hh3cLBv2RSName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cLBv2RSName_Type.__name__ = "DisplayString"
_Hh3cLBv2RSName_Object = MibTableColumn
hh3cLBv2RSName = _Hh3cLBv2RSName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 4, 1, 1, 1),
    _Hh3cLBv2RSName_Type()
)
hh3cLBv2RSName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cLBv2RSName.setStatus("current")
_Hh3cLBv2RSRowStatus_Type = RowStatus
_Hh3cLBv2RSRowStatus_Object = MibTableColumn
hh3cLBv2RSRowStatus = _Hh3cLBv2RSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 4, 1, 1, 2),
    _Hh3cLBv2RSRowStatus_Type()
)
hh3cLBv2RSRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cLBv2RSRowStatus.setStatus("current")


class _Hh3cLBv2RSConnectionsLimit_Type(Unsigned32):
    """Custom type hh3cLBv2RSConnectionsLimit based on Unsigned32"""
    defaultValue = 0


_Hh3cLBv2RSConnectionsLimit_Object = MibTableColumn
hh3cLBv2RSConnectionsLimit = _Hh3cLBv2RSConnectionsLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 4, 1, 1, 3),
    _Hh3cLBv2RSConnectionsLimit_Type()
)
hh3cLBv2RSConnectionsLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cLBv2RSConnectionsLimit.setStatus("current")


class _Hh3cLBv2RSConnectionsRateLimit_Type(Unsigned32):
    """Custom type hh3cLBv2RSConnectionsRateLimit based on Unsigned32"""
    defaultValue = 0


_Hh3cLBv2RSConnectionsRateLimit_Object = MibTableColumn
hh3cLBv2RSConnectionsRateLimit = _Hh3cLBv2RSConnectionsRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 4, 1, 1, 4),
    _Hh3cLBv2RSConnectionsRateLimit_Type()
)
hh3cLBv2RSConnectionsRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cLBv2RSConnectionsRateLimit.setStatus("current")
_Hh3cLBv2RSStatsTable_Object = MibTable
hh3cLBv2RSStatsTable = _Hh3cLBv2RSStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 4, 2)
)
if mibBuilder.loadTexts:
    hh3cLBv2RSStatsTable.setStatus("current")
_Hh3cLBv2RSStatsEntry_Object = MibTableRow
hh3cLBv2RSStatsEntry = _Hh3cLBv2RSStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 4, 2, 1)
)
hh3cLBv2RSStatsEntry.setIndexNames(
    (0, "HH3C-LBV2-MIB", "hh3cLBv2RSName"),
    (0, "HH3C-LBV2-MIB", "hh3cLBv2RSStatChassis"),
    (0, "HH3C-LBV2-MIB", "hh3cLBv2RSStatSlot"),
    (0, "HH3C-LBV2-MIB", "hh3cLBv2RSStatCpuid"),
)
if mibBuilder.loadTexts:
    hh3cLBv2RSStatsEntry.setStatus("current")


class _Hh3cLBv2RSStatChassis_Type(Unsigned32):
    """Custom type hh3cLBv2RSStatChassis based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cLBv2RSStatChassis_Type.__name__ = "Unsigned32"
_Hh3cLBv2RSStatChassis_Object = MibTableColumn
hh3cLBv2RSStatChassis = _Hh3cLBv2RSStatChassis_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 4, 2, 1, 1),
    _Hh3cLBv2RSStatChassis_Type()
)
hh3cLBv2RSStatChassis.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cLBv2RSStatChassis.setStatus("current")


class _Hh3cLBv2RSStatSlot_Type(Unsigned32):
    """Custom type hh3cLBv2RSStatSlot based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cLBv2RSStatSlot_Type.__name__ = "Unsigned32"
_Hh3cLBv2RSStatSlot_Object = MibTableColumn
hh3cLBv2RSStatSlot = _Hh3cLBv2RSStatSlot_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 4, 2, 1, 2),
    _Hh3cLBv2RSStatSlot_Type()
)
hh3cLBv2RSStatSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cLBv2RSStatSlot.setStatus("current")


class _Hh3cLBv2RSStatCpuid_Type(Unsigned32):
    """Custom type hh3cLBv2RSStatCpuid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cLBv2RSStatCpuid_Type.__name__ = "Unsigned32"
_Hh3cLBv2RSStatCpuid_Object = MibTableColumn
hh3cLBv2RSStatCpuid = _Hh3cLBv2RSStatCpuid_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 4, 2, 1, 3),
    _Hh3cLBv2RSStatCpuid_Type()
)
hh3cLBv2RSStatCpuid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cLBv2RSStatCpuid.setStatus("current")
_Hh3cLBv2RSStatTotalConnections_Type = Counter64
_Hh3cLBv2RSStatTotalConnections_Object = MibTableColumn
hh3cLBv2RSStatTotalConnections = _Hh3cLBv2RSStatTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 4, 2, 1, 4),
    _Hh3cLBv2RSStatTotalConnections_Type()
)
hh3cLBv2RSStatTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLBv2RSStatTotalConnections.setStatus("current")
_Hh3cLBv2RSStatActiveConnections_Type = Unsigned32
_Hh3cLBv2RSStatActiveConnections_Object = MibTableColumn
hh3cLBv2RSStatActiveConnections = _Hh3cLBv2RSStatActiveConnections_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 4, 2, 1, 5),
    _Hh3cLBv2RSStatActiveConnections_Type()
)
hh3cLBv2RSStatActiveConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLBv2RSStatActiveConnections.setStatus("current")
_Hh3cLBv2RSStatServerSidePKTsIn_Type = Counter64
_Hh3cLBv2RSStatServerSidePKTsIn_Object = MibTableColumn
hh3cLBv2RSStatServerSidePKTsIn = _Hh3cLBv2RSStatServerSidePKTsIn_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 4, 2, 1, 6),
    _Hh3cLBv2RSStatServerSidePKTsIn_Type()
)
hh3cLBv2RSStatServerSidePKTsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLBv2RSStatServerSidePKTsIn.setStatus("current")
_Hh3cLBv2RSStatServerSidePKTsOut_Type = Counter64
_Hh3cLBv2RSStatServerSidePKTsOut_Object = MibTableColumn
hh3cLBv2RSStatServerSidePKTsOut = _Hh3cLBv2RSStatServerSidePKTsOut_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 4, 2, 1, 7),
    _Hh3cLBv2RSStatServerSidePKTsOut_Type()
)
hh3cLBv2RSStatServerSidePKTsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLBv2RSStatServerSidePKTsOut.setStatus("current")
_Hh3cLBv2RSStatDroppedPackets_Type = Counter64
_Hh3cLBv2RSStatDroppedPackets_Object = MibTableColumn
hh3cLBv2RSStatDroppedPackets = _Hh3cLBv2RSStatDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 4, 2, 1, 8),
    _Hh3cLBv2RSStatDroppedPackets_Type()
)
hh3cLBv2RSStatDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLBv2RSStatDroppedPackets.setStatus("current")
_Hh3cLBv2RSStatServerSideBytesIn_Type = Counter64
_Hh3cLBv2RSStatServerSideBytesIn_Object = MibTableColumn
hh3cLBv2RSStatServerSideBytesIn = _Hh3cLBv2RSStatServerSideBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 4, 2, 1, 9),
    _Hh3cLBv2RSStatServerSideBytesIn_Type()
)
hh3cLBv2RSStatServerSideBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLBv2RSStatServerSideBytesIn.setStatus("current")
if mibBuilder.loadTexts:
    hh3cLBv2RSStatServerSideBytesIn.setUnits("byte")
_Hh3cLBv2RSStatServerSideBytesOut_Type = Counter64
_Hh3cLBv2RSStatServerSideBytesOut_Object = MibTableColumn
hh3cLBv2RSStatServerSideBytesOut = _Hh3cLBv2RSStatServerSideBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 4, 2, 1, 10),
    _Hh3cLBv2RSStatServerSideBytesOut_Type()
)
hh3cLBv2RSStatServerSideBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLBv2RSStatServerSideBytesOut.setStatus("current")
if mibBuilder.loadTexts:
    hh3cLBv2RSStatServerSideBytesOut.setUnits("byte")
_Hh3cLBv2RSStatReceivedRequests_Type = Counter64
_Hh3cLBv2RSStatReceivedRequests_Object = MibTableColumn
hh3cLBv2RSStatReceivedRequests = _Hh3cLBv2RSStatReceivedRequests_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 4, 2, 1, 11),
    _Hh3cLBv2RSStatReceivedRequests_Type()
)
hh3cLBv2RSStatReceivedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLBv2RSStatReceivedRequests.setStatus("current")
_Hh3cLBv2RSStatSentResponses_Type = Counter64
_Hh3cLBv2RSStatSentResponses_Object = MibTableColumn
hh3cLBv2RSStatSentResponses = _Hh3cLBv2RSStatSentResponses_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 4, 2, 1, 12),
    _Hh3cLBv2RSStatSentResponses_Type()
)
hh3cLBv2RSStatSentResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLBv2RSStatSentResponses.setStatus("current")
_Hh3cLBv2RSStatConnectionsRate_Type = Unsigned32
_Hh3cLBv2RSStatConnectionsRate_Object = MibTableColumn
hh3cLBv2RSStatConnectionsRate = _Hh3cLBv2RSStatConnectionsRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 4, 2, 1, 13),
    _Hh3cLBv2RSStatConnectionsRate_Type()
)
hh3cLBv2RSStatConnectionsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLBv2RSStatConnectionsRate.setStatus("current")
if mibBuilder.loadTexts:
    hh3cLBv2RSStatConnectionsRate.setUnits("cps")
_Hh3cLBv2SFTables_ObjectIdentity = ObjectIdentity
hh3cLBv2SFTables = _Hh3cLBv2SFTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 5)
)
_Hh3cLBv2SFTable_Object = MibTable
hh3cLBv2SFTable = _Hh3cLBv2SFTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 5, 1)
)
if mibBuilder.loadTexts:
    hh3cLBv2SFTable.setStatus("current")
_Hh3cLBv2SFEntry_Object = MibTableRow
hh3cLBv2SFEntry = _Hh3cLBv2SFEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 5, 1, 1)
)
hh3cLBv2SFEntry.setIndexNames(
    (0, "HH3C-LBV2-MIB", "hh3cLBv2SFName"),
)
if mibBuilder.loadTexts:
    hh3cLBv2SFEntry.setStatus("current")


class _Hh3cLBv2SFName_Type(DisplayString):
    """Custom type hh3cLBv2SFName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cLBv2SFName_Type.__name__ = "DisplayString"
_Hh3cLBv2SFName_Object = MibTableColumn
hh3cLBv2SFName = _Hh3cLBv2SFName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 5, 1, 1, 1),
    _Hh3cLBv2SFName_Type()
)
hh3cLBv2SFName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cLBv2SFName.setStatus("current")
_Hh3cLBv2SFRowStatus_Type = RowStatus
_Hh3cLBv2SFRowStatus_Object = MibTableColumn
hh3cLBv2SFRowStatus = _Hh3cLBv2SFRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 5, 1, 1, 2),
    _Hh3cLBv2SFRowStatus_Type()
)
hh3cLBv2SFRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cLBv2SFRowStatus.setStatus("current")
_Hh3cLBv2SFStatsTable_Object = MibTable
hh3cLBv2SFStatsTable = _Hh3cLBv2SFStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 5, 2)
)
if mibBuilder.loadTexts:
    hh3cLBv2SFStatsTable.setStatus("current")
_Hh3cLBv2SFStatsEntry_Object = MibTableRow
hh3cLBv2SFStatsEntry = _Hh3cLBv2SFStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 5, 2, 1)
)
hh3cLBv2SFStatsEntry.setIndexNames(
    (0, "HH3C-LBV2-MIB", "hh3cLBv2SFName"),
    (0, "HH3C-LBV2-MIB", "hh3cLBv2SFStatChassis"),
    (0, "HH3C-LBV2-MIB", "hh3cLBv2SFStatSlot"),
    (0, "HH3C-LBV2-MIB", "hh3cLBv2SFStatCpuid"),
)
if mibBuilder.loadTexts:
    hh3cLBv2SFStatsEntry.setStatus("current")


class _Hh3cLBv2SFStatChassis_Type(Unsigned32):
    """Custom type hh3cLBv2SFStatChassis based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cLBv2SFStatChassis_Type.__name__ = "Unsigned32"
_Hh3cLBv2SFStatChassis_Object = MibTableColumn
hh3cLBv2SFStatChassis = _Hh3cLBv2SFStatChassis_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 5, 2, 1, 1),
    _Hh3cLBv2SFStatChassis_Type()
)
hh3cLBv2SFStatChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cLBv2SFStatChassis.setStatus("current")


class _Hh3cLBv2SFStatSlot_Type(Unsigned32):
    """Custom type hh3cLBv2SFStatSlot based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cLBv2SFStatSlot_Type.__name__ = "Unsigned32"
_Hh3cLBv2SFStatSlot_Object = MibTableColumn
hh3cLBv2SFStatSlot = _Hh3cLBv2SFStatSlot_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 5, 2, 1, 2),
    _Hh3cLBv2SFStatSlot_Type()
)
hh3cLBv2SFStatSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cLBv2SFStatSlot.setStatus("current")


class _Hh3cLBv2SFStatCpuid_Type(Unsigned32):
    """Custom type hh3cLBv2SFStatCpuid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cLBv2SFStatCpuid_Type.__name__ = "Unsigned32"
_Hh3cLBv2SFStatCpuid_Object = MibTableColumn
hh3cLBv2SFStatCpuid = _Hh3cLBv2SFStatCpuid_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 5, 2, 1, 3),
    _Hh3cLBv2SFStatCpuid_Type()
)
hh3cLBv2SFStatCpuid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cLBv2SFStatCpuid.setStatus("current")
_Hh3cLBv2SFStatTotalConnections_Type = Counter64
_Hh3cLBv2SFStatTotalConnections_Object = MibTableColumn
hh3cLBv2SFStatTotalConnections = _Hh3cLBv2SFStatTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 5, 2, 1, 4),
    _Hh3cLBv2SFStatTotalConnections_Type()
)
hh3cLBv2SFStatTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLBv2SFStatTotalConnections.setStatus("current")
_Hh3cLBv2SFStatActiveConnections_Type = Unsigned32
_Hh3cLBv2SFStatActiveConnections_Object = MibTableColumn
hh3cLBv2SFStatActiveConnections = _Hh3cLBv2SFStatActiveConnections_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 5, 2, 1, 5),
    _Hh3cLBv2SFStatActiveConnections_Type()
)
hh3cLBv2SFStatActiveConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLBv2SFStatActiveConnections.setStatus("current")
_Hh3cLBv2SFStatServerSidePKTsIn_Type = Counter64
_Hh3cLBv2SFStatServerSidePKTsIn_Object = MibTableColumn
hh3cLBv2SFStatServerSidePKTsIn = _Hh3cLBv2SFStatServerSidePKTsIn_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 5, 2, 1, 6),
    _Hh3cLBv2SFStatServerSidePKTsIn_Type()
)
hh3cLBv2SFStatServerSidePKTsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLBv2SFStatServerSidePKTsIn.setStatus("current")
_Hh3cLBv2SFStatServerSidePKTsOut_Type = Counter64
_Hh3cLBv2SFStatServerSidePKTsOut_Object = MibTableColumn
hh3cLBv2SFStatServerSidePKTsOut = _Hh3cLBv2SFStatServerSidePKTsOut_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 5, 2, 1, 7),
    _Hh3cLBv2SFStatServerSidePKTsOut_Type()
)
hh3cLBv2SFStatServerSidePKTsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLBv2SFStatServerSidePKTsOut.setStatus("current")
_Hh3cLBv2SFStatDroppedPackets_Type = Counter64
_Hh3cLBv2SFStatDroppedPackets_Object = MibTableColumn
hh3cLBv2SFStatDroppedPackets = _Hh3cLBv2SFStatDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 5, 2, 1, 8),
    _Hh3cLBv2SFStatDroppedPackets_Type()
)
hh3cLBv2SFStatDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLBv2SFStatDroppedPackets.setStatus("current")
_Hh3cLBv2SFStatServerSideBytesIn_Type = Counter64
_Hh3cLBv2SFStatServerSideBytesIn_Object = MibTableColumn
hh3cLBv2SFStatServerSideBytesIn = _Hh3cLBv2SFStatServerSideBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 5, 2, 1, 9),
    _Hh3cLBv2SFStatServerSideBytesIn_Type()
)
hh3cLBv2SFStatServerSideBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLBv2SFStatServerSideBytesIn.setStatus("current")
if mibBuilder.loadTexts:
    hh3cLBv2SFStatServerSideBytesIn.setUnits("byte")
_Hh3cLBv2SFStatServerSideBytesOut_Type = Counter64
_Hh3cLBv2SFStatServerSideBytesOut_Object = MibTableColumn
hh3cLBv2SFStatServerSideBytesOut = _Hh3cLBv2SFStatServerSideBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 5, 2, 1, 10),
    _Hh3cLBv2SFStatServerSideBytesOut_Type()
)
hh3cLBv2SFStatServerSideBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLBv2SFStatServerSideBytesOut.setStatus("current")
if mibBuilder.loadTexts:
    hh3cLBv2SFStatServerSideBytesOut.setUnits("byte")
_Hh3cLBv2SFStatReceivedRequests_Type = Counter64
_Hh3cLBv2SFStatReceivedRequests_Object = MibTableColumn
hh3cLBv2SFStatReceivedRequests = _Hh3cLBv2SFStatReceivedRequests_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 5, 2, 1, 11),
    _Hh3cLBv2SFStatReceivedRequests_Type()
)
hh3cLBv2SFStatReceivedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLBv2SFStatReceivedRequests.setStatus("current")
_Hh3cLBv2SFStatSentResponses_Type = Counter64
_Hh3cLBv2SFStatSentResponses_Object = MibTableColumn
hh3cLBv2SFStatSentResponses = _Hh3cLBv2SFStatSentResponses_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 5, 2, 1, 12),
    _Hh3cLBv2SFStatSentResponses_Type()
)
hh3cLBv2SFStatSentResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLBv2SFStatSentResponses.setStatus("current")
_Hh3cLBv2Trap_ObjectIdentity = ObjectIdentity
hh3cLBv2Trap = _Hh3cLBv2Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 6)
)
_Hh3cLBv2TrapPrefix_ObjectIdentity = ObjectIdentity
hh3cLBv2TrapPrefix = _Hh3cLBv2TrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 6, 0)
)

# Managed Objects groups


# Notification objects

hh3cLBv2VSConnOverloadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 6, 0, 1)
)
hh3cLBv2VSConnOverloadTrap.setObjects(
      *(("HH3C-LBV2-MIB", "hh3cLBv2VSName"),
        ("HH3C-LBV2-MIB", "hh3cLBv2VSConnectionsLimit"),
        ("HH3C-LBV2-MIB", "hh3cLBv2VSStatChassis"),
        ("HH3C-LBV2-MIB", "hh3cLBv2VSStatSlot"),
        ("HH3C-LBV2-MIB", "hh3cLBv2VSStatCpuid"),
        ("HH3C-LBV2-MIB", "hh3cLBv2VSStatActiveConnections"))
)
if mibBuilder.loadTexts:
    hh3cLBv2VSConnOverloadTrap.setStatus(
        "current"
    )

hh3cLBv2VSConnRecoveryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 6, 0, 2)
)
hh3cLBv2VSConnRecoveryTrap.setObjects(
      *(("HH3C-LBV2-MIB", "hh3cLBv2VSName"),
        ("HH3C-LBV2-MIB", "hh3cLBv2VSConnectionsLimit"),
        ("HH3C-LBV2-MIB", "hh3cLBv2VSStatChassis"),
        ("HH3C-LBV2-MIB", "hh3cLBv2VSStatSlot"),
        ("HH3C-LBV2-MIB", "hh3cLBv2VSStatCpuid"),
        ("HH3C-LBV2-MIB", "hh3cLBv2VSStatActiveConnections"))
)
if mibBuilder.loadTexts:
    hh3cLBv2VSConnRecoveryTrap.setStatus(
        "current"
    )

hh3cLBv2VSConnsRateOverloadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 6, 0, 3)
)
hh3cLBv2VSConnsRateOverloadTrap.setObjects(
      *(("HH3C-LBV2-MIB", "hh3cLBv2VSName"),
        ("HH3C-LBV2-MIB", "hh3cLBv2VSConnectionsRateLimit"),
        ("HH3C-LBV2-MIB", "hh3cLBv2VSStatChassis"),
        ("HH3C-LBV2-MIB", "hh3cLBv2VSStatSlot"),
        ("HH3C-LBV2-MIB", "hh3cLBv2VSStatCpuid"),
        ("HH3C-LBV2-MIB", "hh3cLBv2VSStatConnectionsRate"))
)
if mibBuilder.loadTexts:
    hh3cLBv2VSConnsRateOverloadTrap.setStatus(
        "current"
    )

hh3cLBv2VSConnsRateRecoveryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 6, 0, 4)
)
hh3cLBv2VSConnsRateRecoveryTrap.setObjects(
      *(("HH3C-LBV2-MIB", "hh3cLBv2VSName"),
        ("HH3C-LBV2-MIB", "hh3cLBv2VSConnectionsRateLimit"),
        ("HH3C-LBV2-MIB", "hh3cLBv2VSStatChassis"),
        ("HH3C-LBV2-MIB", "hh3cLBv2VSStatSlot"),
        ("HH3C-LBV2-MIB", "hh3cLBv2VSStatCpuid"),
        ("HH3C-LBV2-MIB", "hh3cLBv2VSStatConnectionsRate"))
)
if mibBuilder.loadTexts:
    hh3cLBv2VSConnsRateRecoveryTrap.setStatus(
        "current"
    )

hh3cLBv2VSActiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 6, 0, 5)
)
hh3cLBv2VSActiveTrap.setObjects(
    ("HH3C-LBV2-MIB", "hh3cLBv2VSName")
)
if mibBuilder.loadTexts:
    hh3cLBv2VSActiveTrap.setStatus(
        "current"
    )

hh3cLBv2VSInactiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 6, 0, 6)
)
hh3cLBv2VSInactiveTrap.setObjects(
    ("HH3C-LBV2-MIB", "hh3cLBv2VSName")
)
if mibBuilder.loadTexts:
    hh3cLBv2VSInactiveTrap.setStatus(
        "current"
    )

hh3cLBv2RSAvailableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 6, 0, 7)
)
hh3cLBv2RSAvailableTrap.setObjects(
    ("HH3C-LBV2-MIB", "hh3cLBv2RSName")
)
if mibBuilder.loadTexts:
    hh3cLBv2RSAvailableTrap.setStatus(
        "current"
    )

hh3cLBv2RSUnavailableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 6, 0, 8)
)
hh3cLBv2RSUnavailableTrap.setObjects(
    ("HH3C-LBV2-MIB", "hh3cLBv2RSName")
)
if mibBuilder.loadTexts:
    hh3cLBv2RSUnavailableTrap.setStatus(
        "current"
    )

hh3cLBv2SFActiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 6, 0, 9)
)
hh3cLBv2SFActiveTrap.setObjects(
    ("HH3C-LBV2-MIB", "hh3cLBv2SFName")
)
if mibBuilder.loadTexts:
    hh3cLBv2SFActiveTrap.setStatus(
        "current"
    )

hh3cLBv2SFInactiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 6, 0, 10)
)
hh3cLBv2SFInactiveTrap.setObjects(
    ("HH3C-LBV2-MIB", "hh3cLBv2SFName")
)
if mibBuilder.loadTexts:
    hh3cLBv2SFInactiveTrap.setStatus(
        "current"
    )

hh3cLBv2ActionInUseSFChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 6, 0, 11)
)
hh3cLBv2ActionInUseSFChangeTrap.setObjects(
      *(("HH3C-LBV2-MIB", "hh3cLBv2ActionName"),
        ("HH3C-LBV2-MIB", "hh3cLBv2ActionDefaultSF"),
        ("HH3C-LBV2-MIB", "hh3cLBv2ActionBackupSF"),
        ("HH3C-LBV2-MIB", "hh3cLBv2ActionInUseSF"))
)
if mibBuilder.loadTexts:
    hh3cLBv2ActionInUseSFChangeTrap.setStatus(
        "current"
    )

hh3cLBv2VSInUseSFChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 6, 0, 12)
)
hh3cLBv2VSInUseSFChangeTrap.setObjects(
      *(("HH3C-LBV2-MIB", "hh3cLBv2VSName"),
        ("HH3C-LBV2-MIB", "hh3cLBv2VSDefaultSF"),
        ("HH3C-LBV2-MIB", "hh3cLBv2VSBackupSF"),
        ("HH3C-LBV2-MIB", "hh3cLBv2VSInUseSF"))
)
if mibBuilder.loadTexts:
    hh3cLBv2VSInUseSFChangeTrap.setStatus(
        "current"
    )

hh3cLBv2RSConnOverloadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 6, 0, 13)
)
hh3cLBv2RSConnOverloadTrap.setObjects(
      *(("HH3C-LBV2-MIB", "hh3cLBv2RSName"),
        ("HH3C-LBV2-MIB", "hh3cLBv2RSConnectionsLimit"),
        ("HH3C-LBV2-MIB", "hh3cLBv2RSStatChassis"),
        ("HH3C-LBV2-MIB", "hh3cLBv2RSStatSlot"),
        ("HH3C-LBV2-MIB", "hh3cLBv2RSStatCpuid"),
        ("HH3C-LBV2-MIB", "hh3cLBv2RSStatActiveConnections"))
)
if mibBuilder.loadTexts:
    hh3cLBv2RSConnOverloadTrap.setStatus(
        "current"
    )

hh3cLBv2RSConnRecoveryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 6, 0, 14)
)
hh3cLBv2RSConnRecoveryTrap.setObjects(
      *(("HH3C-LBV2-MIB", "hh3cLBv2RSName"),
        ("HH3C-LBV2-MIB", "hh3cLBv2RSConnectionsLimit"),
        ("HH3C-LBV2-MIB", "hh3cLBv2RSStatChassis"),
        ("HH3C-LBV2-MIB", "hh3cLBv2RSStatSlot"),
        ("HH3C-LBV2-MIB", "hh3cLBv2RSStatCpuid"),
        ("HH3C-LBV2-MIB", "hh3cLBv2RSStatActiveConnections"))
)
if mibBuilder.loadTexts:
    hh3cLBv2RSConnRecoveryTrap.setStatus(
        "current"
    )

hh3cLBv2RSConnsRateOverloadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 6, 0, 15)
)
hh3cLBv2RSConnsRateOverloadTrap.setObjects(
      *(("HH3C-LBV2-MIB", "hh3cLBv2RSName"),
        ("HH3C-LBV2-MIB", "hh3cLBv2RSConnectionsRateLimit"),
        ("HH3C-LBV2-MIB", "hh3cLBv2RSStatChassis"),
        ("HH3C-LBV2-MIB", "hh3cLBv2RSStatSlot"),
        ("HH3C-LBV2-MIB", "hh3cLBv2RSStatCpuid"),
        ("HH3C-LBV2-MIB", "hh3cLBv2RSStatConnectionsRate"))
)
if mibBuilder.loadTexts:
    hh3cLBv2RSConnsRateOverloadTrap.setStatus(
        "current"
    )

hh3cLBv2RSConnsRateRecoveryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148, 6, 0, 16)
)
hh3cLBv2RSConnsRateRecoveryTrap.setObjects(
      *(("HH3C-LBV2-MIB", "hh3cLBv2RSName"),
        ("HH3C-LBV2-MIB", "hh3cLBv2RSConnectionsRateLimit"),
        ("HH3C-LBV2-MIB", "hh3cLBv2RSStatChassis"),
        ("HH3C-LBV2-MIB", "hh3cLBv2RSStatSlot"),
        ("HH3C-LBV2-MIB", "hh3cLBv2RSStatCpuid"),
        ("HH3C-LBV2-MIB", "hh3cLBv2RSStatConnectionsRate"))
)
if mibBuilder.loadTexts:
    hh3cLBv2RSConnsRateRecoveryTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-LBV2-MIB",
    **{"hh3cLBv2": hh3cLBv2,
       "hh3cLBv2GlobalObjects": hh3cLBv2GlobalObjects,
       "hh3cLBv2TrapEnable": hh3cLBv2TrapEnable,
       "hh3cLBv2ActionTables": hh3cLBv2ActionTables,
       "hh3cLBv2ActionTable": hh3cLBv2ActionTable,
       "hh3cLBv2ActionEntry": hh3cLBv2ActionEntry,
       "hh3cLBv2ActionName": hh3cLBv2ActionName,
       "hh3cLBv2ActionDefaultSF": hh3cLBv2ActionDefaultSF,
       "hh3cLBv2ActionBackupSF": hh3cLBv2ActionBackupSF,
       "hh3cLBv2ActionInUseSF": hh3cLBv2ActionInUseSF,
       "hh3cLBv2ActionRowStatus": hh3cLBv2ActionRowStatus,
       "hh3cLBv2VSTables": hh3cLBv2VSTables,
       "hh3cLBv2VSTable": hh3cLBv2VSTable,
       "hh3cLBv2VSEntry": hh3cLBv2VSEntry,
       "hh3cLBv2VSName": hh3cLBv2VSName,
       "hh3cLBv2VSConnectionsLimit": hh3cLBv2VSConnectionsLimit,
       "hh3cLBv2VSConnectionsRateLimit": hh3cLBv2VSConnectionsRateLimit,
       "hh3cLBv2VSDefaultSF": hh3cLBv2VSDefaultSF,
       "hh3cLBv2VSBackupSF": hh3cLBv2VSBackupSF,
       "hh3cLBv2VSInUseSF": hh3cLBv2VSInUseSF,
       "hh3cLBv2VSRowStatus": hh3cLBv2VSRowStatus,
       "hh3cLBv2VSStatsTable": hh3cLBv2VSStatsTable,
       "hh3cLBv2VSStatsEntry": hh3cLBv2VSStatsEntry,
       "hh3cLBv2VSStatChassis": hh3cLBv2VSStatChassis,
       "hh3cLBv2VSStatSlot": hh3cLBv2VSStatSlot,
       "hh3cLBv2VSStatCpuid": hh3cLBv2VSStatCpuid,
       "hh3cLBv2VSStatTotalConnections": hh3cLBv2VSStatTotalConnections,
       "hh3cLBv2VSStatActiveConnections": hh3cLBv2VSStatActiveConnections,
       "hh3cLBv2VSStatClientSidePKTsIn": hh3cLBv2VSStatClientSidePKTsIn,
       "hh3cLBv2VSStatClientSidePKTsOut": hh3cLBv2VSStatClientSidePKTsOut,
       "hh3cLBv2VSStatDroppedPackets": hh3cLBv2VSStatDroppedPackets,
       "hh3cLBv2VSStatClientSideBytesIn": hh3cLBv2VSStatClientSideBytesIn,
       "hh3cLBv2VSStatClientSideBytesOut": hh3cLBv2VSStatClientSideBytesOut,
       "hh3cLBv2VSStatReceivedRequests": hh3cLBv2VSStatReceivedRequests,
       "hh3cLBv2VSStatSentResponses": hh3cLBv2VSStatSentResponses,
       "hh3cLBv2VSStatConnectionsRate": hh3cLBv2VSStatConnectionsRate,
       "hh3cLBv2RSTables": hh3cLBv2RSTables,
       "hh3cLBv2RSTable": hh3cLBv2RSTable,
       "hh3cLBv2RSEntry": hh3cLBv2RSEntry,
       "hh3cLBv2RSName": hh3cLBv2RSName,
       "hh3cLBv2RSRowStatus": hh3cLBv2RSRowStatus,
       "hh3cLBv2RSConnectionsLimit": hh3cLBv2RSConnectionsLimit,
       "hh3cLBv2RSConnectionsRateLimit": hh3cLBv2RSConnectionsRateLimit,
       "hh3cLBv2RSStatsTable": hh3cLBv2RSStatsTable,
       "hh3cLBv2RSStatsEntry": hh3cLBv2RSStatsEntry,
       "hh3cLBv2RSStatChassis": hh3cLBv2RSStatChassis,
       "hh3cLBv2RSStatSlot": hh3cLBv2RSStatSlot,
       "hh3cLBv2RSStatCpuid": hh3cLBv2RSStatCpuid,
       "hh3cLBv2RSStatTotalConnections": hh3cLBv2RSStatTotalConnections,
       "hh3cLBv2RSStatActiveConnections": hh3cLBv2RSStatActiveConnections,
       "hh3cLBv2RSStatServerSidePKTsIn": hh3cLBv2RSStatServerSidePKTsIn,
       "hh3cLBv2RSStatServerSidePKTsOut": hh3cLBv2RSStatServerSidePKTsOut,
       "hh3cLBv2RSStatDroppedPackets": hh3cLBv2RSStatDroppedPackets,
       "hh3cLBv2RSStatServerSideBytesIn": hh3cLBv2RSStatServerSideBytesIn,
       "hh3cLBv2RSStatServerSideBytesOut": hh3cLBv2RSStatServerSideBytesOut,
       "hh3cLBv2RSStatReceivedRequests": hh3cLBv2RSStatReceivedRequests,
       "hh3cLBv2RSStatSentResponses": hh3cLBv2RSStatSentResponses,
       "hh3cLBv2RSStatConnectionsRate": hh3cLBv2RSStatConnectionsRate,
       "hh3cLBv2SFTables": hh3cLBv2SFTables,
       "hh3cLBv2SFTable": hh3cLBv2SFTable,
       "hh3cLBv2SFEntry": hh3cLBv2SFEntry,
       "hh3cLBv2SFName": hh3cLBv2SFName,
       "hh3cLBv2SFRowStatus": hh3cLBv2SFRowStatus,
       "hh3cLBv2SFStatsTable": hh3cLBv2SFStatsTable,
       "hh3cLBv2SFStatsEntry": hh3cLBv2SFStatsEntry,
       "hh3cLBv2SFStatChassis": hh3cLBv2SFStatChassis,
       "hh3cLBv2SFStatSlot": hh3cLBv2SFStatSlot,
       "hh3cLBv2SFStatCpuid": hh3cLBv2SFStatCpuid,
       "hh3cLBv2SFStatTotalConnections": hh3cLBv2SFStatTotalConnections,
       "hh3cLBv2SFStatActiveConnections": hh3cLBv2SFStatActiveConnections,
       "hh3cLBv2SFStatServerSidePKTsIn": hh3cLBv2SFStatServerSidePKTsIn,
       "hh3cLBv2SFStatServerSidePKTsOut": hh3cLBv2SFStatServerSidePKTsOut,
       "hh3cLBv2SFStatDroppedPackets": hh3cLBv2SFStatDroppedPackets,
       "hh3cLBv2SFStatServerSideBytesIn": hh3cLBv2SFStatServerSideBytesIn,
       "hh3cLBv2SFStatServerSideBytesOut": hh3cLBv2SFStatServerSideBytesOut,
       "hh3cLBv2SFStatReceivedRequests": hh3cLBv2SFStatReceivedRequests,
       "hh3cLBv2SFStatSentResponses": hh3cLBv2SFStatSentResponses,
       "hh3cLBv2Trap": hh3cLBv2Trap,
       "hh3cLBv2TrapPrefix": hh3cLBv2TrapPrefix,
       "hh3cLBv2VSConnOverloadTrap": hh3cLBv2VSConnOverloadTrap,
       "hh3cLBv2VSConnRecoveryTrap": hh3cLBv2VSConnRecoveryTrap,
       "hh3cLBv2VSConnsRateOverloadTrap": hh3cLBv2VSConnsRateOverloadTrap,
       "hh3cLBv2VSConnsRateRecoveryTrap": hh3cLBv2VSConnsRateRecoveryTrap,
       "hh3cLBv2VSActiveTrap": hh3cLBv2VSActiveTrap,
       "hh3cLBv2VSInactiveTrap": hh3cLBv2VSInactiveTrap,
       "hh3cLBv2RSAvailableTrap": hh3cLBv2RSAvailableTrap,
       "hh3cLBv2RSUnavailableTrap": hh3cLBv2RSUnavailableTrap,
       "hh3cLBv2SFActiveTrap": hh3cLBv2SFActiveTrap,
       "hh3cLBv2SFInactiveTrap": hh3cLBv2SFInactiveTrap,
       "hh3cLBv2ActionInUseSFChangeTrap": hh3cLBv2ActionInUseSFChangeTrap,
       "hh3cLBv2VSInUseSFChangeTrap": hh3cLBv2VSInUseSFChangeTrap,
       "hh3cLBv2RSConnOverloadTrap": hh3cLBv2RSConnOverloadTrap,
       "hh3cLBv2RSConnRecoveryTrap": hh3cLBv2RSConnRecoveryTrap,
       "hh3cLBv2RSConnsRateOverloadTrap": hh3cLBv2RSConnsRateOverloadTrap,
       "hh3cLBv2RSConnsRateRecoveryTrap": hh3cLBv2RSConnsRateRecoveryTrap}
)
