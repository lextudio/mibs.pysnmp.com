# SNMP MIB module (PAIRGAIN-ATMTEST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PAIRGAIN-ATMTEST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:17 2024
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

(OwnerString,) = mibBuilder.importSymbols(
    "IF-MIB",
    "OwnerString")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

pgATMTestMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 9)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PgATMTestMIBObjects_ObjectIdentity = ObjectIdentity
pgATMTestMIBObjects = _PgATMTestMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 1)
)


class _PgoamLoopbackAddress_Type(OctetString):
    """Custom type pgoamLoopbackAddress based on OctetString"""
    defaultHexValue = "ffffffffffffffff"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_PgoamLoopbackAddress_Type.__name__ = "OctetString"
_PgoamLoopbackAddress_Object = MibScalar
pgoamLoopbackAddress = _PgoamLoopbackAddress_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 1, 1),
    _PgoamLoopbackAddress_Type()
)
pgoamLoopbackAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgoamLoopbackAddress.setStatus("current")
_PgoamLoopbackTable_Object = MibTable
pgoamLoopbackTable = _PgoamLoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 1, 2)
)
if mibBuilder.loadTexts:
    pgoamLoopbackTable.setStatus("current")
_PgoamLoopbackEntry_Object = MibTableRow
pgoamLoopbackEntry = _PgoamLoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 1, 2, 1)
)
pgoamLoopbackEntry.setIndexNames(
    (0, "PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackIfIndex"),
    (0, "PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackVpi"),
    (0, "PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackVci"),
)
if mibBuilder.loadTexts:
    pgoamLoopbackEntry.setStatus("current")
_PgoamLoopbackIfIndex_Type = Integer32
_PgoamLoopbackIfIndex_Object = MibTableColumn
pgoamLoopbackIfIndex = _PgoamLoopbackIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 1, 2, 1, 1),
    _PgoamLoopbackIfIndex_Type()
)
pgoamLoopbackIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgoamLoopbackIfIndex.setStatus("current")


class _PgoamLoopbackVpi_Type(Integer32):
    """Custom type pgoamLoopbackVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_PgoamLoopbackVpi_Type.__name__ = "Integer32"
_PgoamLoopbackVpi_Object = MibTableColumn
pgoamLoopbackVpi = _PgoamLoopbackVpi_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 1, 2, 1, 2),
    _PgoamLoopbackVpi_Type()
)
pgoamLoopbackVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgoamLoopbackVpi.setStatus("current")


class _PgoamLoopbackVci_Type(Integer32):
    """Custom type pgoamLoopbackVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PgoamLoopbackVci_Type.__name__ = "Integer32"
_PgoamLoopbackVci_Object = MibTableColumn
pgoamLoopbackVci = _PgoamLoopbackVci_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 1, 2, 1, 3),
    _PgoamLoopbackVci_Type()
)
pgoamLoopbackVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgoamLoopbackVci.setStatus("current")


class _PgoamLoopbackType_Type(Integer32):
    """Custom type pgoamLoopbackType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("end2end", 2),
          ("segment", 1))
    )


_PgoamLoopbackType_Type.__name__ = "Integer32"
_PgoamLoopbackType_Object = MibTableColumn
pgoamLoopbackType = _PgoamLoopbackType_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 1, 2, 1, 5),
    _PgoamLoopbackType_Type()
)
pgoamLoopbackType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pgoamLoopbackType.setStatus("current")


class _PgoamLoopbackLocation_Type(OctetString):
    """Custom type pgoamLoopbackLocation based on OctetString"""
    defaultHexValue = "ffffffffffffffff"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_PgoamLoopbackLocation_Type.__name__ = "OctetString"
_PgoamLoopbackLocation_Object = MibTableColumn
pgoamLoopbackLocation = _PgoamLoopbackLocation_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 1, 2, 1, 6),
    _PgoamLoopbackLocation_Type()
)
pgoamLoopbackLocation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pgoamLoopbackLocation.setStatus("current")


class _PgoamLoopbackCount_Type(Integer32):
    """Custom type pgoamLoopbackCount based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_PgoamLoopbackCount_Type.__name__ = "Integer32"
_PgoamLoopbackCount_Object = MibTableColumn
pgoamLoopbackCount = _PgoamLoopbackCount_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 1, 2, 1, 7),
    _PgoamLoopbackCount_Type()
)
pgoamLoopbackCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pgoamLoopbackCount.setStatus("current")


class _PgoamLoopbackTimeout_Type(Integer32):
    """Custom type pgoamLoopbackTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 15),
    )


_PgoamLoopbackTimeout_Type.__name__ = "Integer32"
_PgoamLoopbackTimeout_Object = MibTableColumn
pgoamLoopbackTimeout = _PgoamLoopbackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 1, 2, 1, 8),
    _PgoamLoopbackTimeout_Type()
)
pgoamLoopbackTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pgoamLoopbackTimeout.setStatus("current")
if mibBuilder.loadTexts:
    pgoamLoopbackTimeout.setUnits("seconds")


class _PgoamLoopbackDelay_Type(Integer32):
    """Custom type pgoamLoopbackDelay based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 15),
    )


_PgoamLoopbackDelay_Type.__name__ = "Integer32"
_PgoamLoopbackDelay_Object = MibTableColumn
pgoamLoopbackDelay = _PgoamLoopbackDelay_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 1, 2, 1, 9),
    _PgoamLoopbackDelay_Type()
)
pgoamLoopbackDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pgoamLoopbackDelay.setStatus("current")
if mibBuilder.loadTexts:
    pgoamLoopbackDelay.setUnits("seconds")


class _PgoamLoopbackTrapOnCompletion_Type(TruthValue):
    """Custom type pgoamLoopbackTrapOnCompletion based on TruthValue"""


_PgoamLoopbackTrapOnCompletion_Object = MibTableColumn
pgoamLoopbackTrapOnCompletion = _PgoamLoopbackTrapOnCompletion_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 1, 2, 1, 10),
    _PgoamLoopbackTrapOnCompletion_Type()
)
pgoamLoopbackTrapOnCompletion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pgoamLoopbackTrapOnCompletion.setStatus("current")
_PgoamLoopbackSentCells_Type = Counter32
_PgoamLoopbackSentCells_Object = MibTableColumn
pgoamLoopbackSentCells = _PgoamLoopbackSentCells_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 1, 2, 1, 11),
    _PgoamLoopbackSentCells_Type()
)
pgoamLoopbackSentCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgoamLoopbackSentCells.setStatus("current")
_PgoamLoopbackReceivedCells_Type = Counter32
_PgoamLoopbackReceivedCells_Object = MibTableColumn
pgoamLoopbackReceivedCells = _PgoamLoopbackReceivedCells_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 1, 2, 1, 12),
    _PgoamLoopbackReceivedCells_Type()
)
pgoamLoopbackReceivedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgoamLoopbackReceivedCells.setStatus("current")
_PgoamLoopbackErroredCells_Type = Counter32
_PgoamLoopbackErroredCells_Object = MibTableColumn
pgoamLoopbackErroredCells = _PgoamLoopbackErroredCells_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 1, 2, 1, 13),
    _PgoamLoopbackErroredCells_Type()
)
pgoamLoopbackErroredCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgoamLoopbackErroredCells.setStatus("current")


class _PgoamLoopbackStatus_Type(Integer32):
    """Custom type pgoamLoopbackStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 4),
          ("completed", 3),
          ("expired", 6),
          ("failed", 5),
          ("inProgress", 2),
          ("null", 1))
    )


_PgoamLoopbackStatus_Type.__name__ = "Integer32"
_PgoamLoopbackStatus_Object = MibTableColumn
pgoamLoopbackStatus = _PgoamLoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 1, 2, 1, 14),
    _PgoamLoopbackStatus_Type()
)
pgoamLoopbackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgoamLoopbackStatus.setStatus("current")
_PgoamLoopbackEntryOwner_Type = OwnerString
_PgoamLoopbackEntryOwner_Object = MibTableColumn
pgoamLoopbackEntryOwner = _PgoamLoopbackEntryOwner_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 1, 2, 1, 15),
    _PgoamLoopbackEntryOwner_Type()
)
pgoamLoopbackEntryOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pgoamLoopbackEntryOwner.setStatus("current")
_PgoamLoopbackEntryStatus_Type = RowStatus
_PgoamLoopbackEntryStatus_Object = MibTableColumn
pgoamLoopbackEntryStatus = _PgoamLoopbackEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 1, 2, 1, 16),
    _PgoamLoopbackEntryStatus_Type()
)
pgoamLoopbackEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pgoamLoopbackEntryStatus.setStatus("current")


class _PgoamLoopbackFlowType_Type(Integer32):
    """Custom type pgoamLoopbackFlowType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oamF4", 1),
          ("oamF5", 2))
    )


_PgoamLoopbackFlowType_Type.__name__ = "Integer32"
_PgoamLoopbackFlowType_Object = MibTableColumn
pgoamLoopbackFlowType = _PgoamLoopbackFlowType_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 1, 2, 1, 17),
    _PgoamLoopbackFlowType_Type()
)
pgoamLoopbackFlowType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgoamLoopbackFlowType.setStatus("current")
_PgATMTestMIBTrapPrefix_ObjectIdentity = ObjectIdentity
pgATMTestMIBTrapPrefix = _PgATMTestMIBTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 2)
)
_PgoamLoopbackMIBTraps_ObjectIdentity = ObjectIdentity
pgoamLoopbackMIBTraps = _PgoamLoopbackMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 2, 0)
)
_PgATMTestMIBConformance_ObjectIdentity = ObjectIdentity
pgATMTestMIBConformance = _PgATMTestMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 3)
)
_PgATMTestMIBCompliances_ObjectIdentity = ObjectIdentity
pgATMTestMIBCompliances = _PgATMTestMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 3, 1)
)
_PgATMTestMIBGroups_ObjectIdentity = ObjectIdentity
pgATMTestMIBGroups = _PgATMTestMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 3, 2)
)

# Managed Objects groups

pgATMTestMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 3, 2, 1)
)
pgATMTestMIBGroup.setObjects(
      *(("PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackIfIndex"),
        ("PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackVpi"),
        ("PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackVci"),
        ("PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackCount"),
        ("PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackType"),
        ("PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackLocation"),
        ("PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackTimeout"),
        ("PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackDelay"),
        ("PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackTrapOnCompletion"),
        ("PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackSentCells"),
        ("PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackReceivedCells"),
        ("PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackErroredCells"),
        ("PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackStatus"),
        ("PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackEntryOwner"),
        ("PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackEntryStatus"))
)
if mibBuilder.loadTexts:
    pgATMTestMIBGroup.setStatus("current")


# Notification objects

pgoamLoopbackCompletionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 2, 0, 1)
)
pgoamLoopbackCompletionTrap.setObjects(
      *(("PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackIfIndex"),
        ("PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackVpi"),
        ("PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackVci"),
        ("PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackStatus"),
        ("PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackSentCells"),
        ("PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackReceivedCells"),
        ("PAIRGAIN-ATMTEST-MIB", "pgoamLoopbackErroredCells"))
)
if mibBuilder.loadTexts:
    pgoamLoopbackCompletionTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

pgATMTestMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 9, 3, 1, 1)
)
if mibBuilder.loadTexts:
    pgATMTestMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PAIRGAIN-ATMTEST-MIB",
    **{"pgATMTestMIB": pgATMTestMIB,
       "pgATMTestMIBObjects": pgATMTestMIBObjects,
       "pgoamLoopbackAddress": pgoamLoopbackAddress,
       "pgoamLoopbackTable": pgoamLoopbackTable,
       "pgoamLoopbackEntry": pgoamLoopbackEntry,
       "pgoamLoopbackIfIndex": pgoamLoopbackIfIndex,
       "pgoamLoopbackVpi": pgoamLoopbackVpi,
       "pgoamLoopbackVci": pgoamLoopbackVci,
       "pgoamLoopbackType": pgoamLoopbackType,
       "pgoamLoopbackLocation": pgoamLoopbackLocation,
       "pgoamLoopbackCount": pgoamLoopbackCount,
       "pgoamLoopbackTimeout": pgoamLoopbackTimeout,
       "pgoamLoopbackDelay": pgoamLoopbackDelay,
       "pgoamLoopbackTrapOnCompletion": pgoamLoopbackTrapOnCompletion,
       "pgoamLoopbackSentCells": pgoamLoopbackSentCells,
       "pgoamLoopbackReceivedCells": pgoamLoopbackReceivedCells,
       "pgoamLoopbackErroredCells": pgoamLoopbackErroredCells,
       "pgoamLoopbackStatus": pgoamLoopbackStatus,
       "pgoamLoopbackEntryOwner": pgoamLoopbackEntryOwner,
       "pgoamLoopbackEntryStatus": pgoamLoopbackEntryStatus,
       "pgoamLoopbackFlowType": pgoamLoopbackFlowType,
       "pgATMTestMIBTrapPrefix": pgATMTestMIBTrapPrefix,
       "pgoamLoopbackMIBTraps": pgoamLoopbackMIBTraps,
       "pgoamLoopbackCompletionTrap": pgoamLoopbackCompletionTrap,
       "pgATMTestMIBConformance": pgATMTestMIBConformance,
       "pgATMTestMIBCompliances": pgATMTestMIBCompliances,
       "pgATMTestMIBCompliance": pgATMTestMIBCompliance,
       "pgATMTestMIBGroups": pgATMTestMIBGroups,
       "pgATMTestMIBGroup": pgATMTestMIBGroup}
)
