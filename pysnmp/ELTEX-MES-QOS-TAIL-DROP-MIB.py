# SNMP MIB module (ELTEX-MES-QOS-TAIL-DROP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-MES-QOS-TAIL-DROP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:37:58 2024
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

(eltMes,
 eltMesQosTailDropMib) = mibBuilder.importSymbols(
    "ELTEX-MES",
    "eltMes",
    "eltMesQosTailDropMib")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltMesQosTailDropMibMIBObjects_ObjectIdentity = ObjectIdentity
eltMesQosTailDropMibMIBObjects = _EltMesQosTailDropMibMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1)
)
_EltMesQosTailDropConfig_ObjectIdentity = ObjectIdentity
eltMesQosTailDropConfig = _EltMesQosTailDropConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 1)
)
_EltQosTailDropProfileQueueTable_Object = MibTable
eltQosTailDropProfileQueueTable = _EltQosTailDropProfileQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 1, 1)
)
if mibBuilder.loadTexts:
    eltQosTailDropProfileQueueTable.setStatus("current")
_EltQosTailDropProfileQueueEntry_Object = MibTableRow
eltQosTailDropProfileQueueEntry = _EltQosTailDropProfileQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 1, 1, 1)
)
eltQosTailDropProfileQueueEntry.setIndexNames(
    (0, "ELTEX-MES-QOS-TAIL-DROP-MIB", "eltQosTailDropProfileIndex"),
    (0, "ELTEX-MES-QOS-TAIL-DROP-MIB", "eltQosTailDropProfileQueueIndex"),
)
if mibBuilder.loadTexts:
    eltQosTailDropProfileQueueEntry.setStatus("current")
_EltQosTailDropProfileIndex_Type = Integer32
_EltQosTailDropProfileIndex_Object = MibTableColumn
eltQosTailDropProfileIndex = _EltQosTailDropProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 1, 1, 1, 1),
    _EltQosTailDropProfileIndex_Type()
)
eltQosTailDropProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltQosTailDropProfileIndex.setStatus("current")
_EltQosTailDropProfileQueueIndex_Type = Integer32
_EltQosTailDropProfileQueueIndex_Object = MibTableColumn
eltQosTailDropProfileQueueIndex = _EltQosTailDropProfileQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 1, 1, 1, 2),
    _EltQosTailDropProfileQueueIndex_Type()
)
eltQosTailDropProfileQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltQosTailDropProfileQueueIndex.setStatus("current")


class _EltQosTailDropProfileQueueSharedPoolUsage_Type(TruthValue):
    """Custom type eltQosTailDropProfileQueueSharedPoolUsage based on TruthValue"""


_EltQosTailDropProfileQueueSharedPoolUsage_Object = MibTableColumn
eltQosTailDropProfileQueueSharedPoolUsage = _EltQosTailDropProfileQueueSharedPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 1, 1, 1, 3),
    _EltQosTailDropProfileQueueSharedPoolUsage_Type()
)
eltQosTailDropProfileQueueSharedPoolUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltQosTailDropProfileQueueSharedPoolUsage.setStatus("current")
_EltQosTailDropProfileQueueLimit_Type = Integer32
_EltQosTailDropProfileQueueLimit_Object = MibTableColumn
eltQosTailDropProfileQueueLimit = _EltQosTailDropProfileQueueLimit_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 1, 1, 1, 4),
    _EltQosTailDropProfileQueueLimit_Type()
)
eltQosTailDropProfileQueueLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltQosTailDropProfileQueueLimit.setStatus("current")
_EltQosTailDropIfConfigTable_Object = MibTable
eltQosTailDropIfConfigTable = _EltQosTailDropIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 1, 2)
)
if mibBuilder.loadTexts:
    eltQosTailDropIfConfigTable.setStatus("current")
_EltQosTailDropIfConfigEntry_Object = MibTableRow
eltQosTailDropIfConfigEntry = _EltQosTailDropIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 1, 2, 1)
)
eltQosTailDropIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    eltQosTailDropIfConfigEntry.setStatus("current")


class _EltQosTailDropIfProfileIndex_Type(Integer32):
    """Custom type eltQosTailDropIfProfileIndex based on Integer32"""
    defaultValue = 0


_EltQosTailDropIfProfileIndex_Object = MibTableColumn
eltQosTailDropIfProfileIndex = _EltQosTailDropIfProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 1, 2, 1, 1),
    _EltQosTailDropIfProfileIndex_Type()
)
eltQosTailDropIfProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltQosTailDropIfProfileIndex.setStatus("current")
_EltQosTailDropConfigTable_Object = MibTable
eltQosTailDropConfigTable = _EltQosTailDropConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 1, 3)
)
if mibBuilder.loadTexts:
    eltQosTailDropConfigTable.setStatus("current")
_EltQosTailDropConfigEntry_Object = MibTableRow
eltQosTailDropConfigEntry = _EltQosTailDropConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 1, 3, 1)
)
eltQosTailDropConfigEntry.setIndexNames(
    (0, "ELTEX-MES-QOS-TAIL-DROP-MIB", "eltQosTailDropConfigUnitId"),
)
if mibBuilder.loadTexts:
    eltQosTailDropConfigEntry.setStatus("current")
_EltQosTailDropConfigUnitId_Type = Integer32
_EltQosTailDropConfigUnitId_Object = MibTableColumn
eltQosTailDropConfigUnitId = _EltQosTailDropConfigUnitId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 1, 3, 1, 1),
    _EltQosTailDropConfigUnitId_Type()
)
eltQosTailDropConfigUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosTailDropConfigUnitId.setStatus("current")
_EltQosTailDropConfigPhysicalBuffersLimit_Type = Integer32
_EltQosTailDropConfigPhysicalBuffersLimit_Object = MibTableColumn
eltQosTailDropConfigPhysicalBuffersLimit = _EltQosTailDropConfigPhysicalBuffersLimit_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 1, 3, 1, 2),
    _EltQosTailDropConfigPhysicalBuffersLimit_Type()
)
eltQosTailDropConfigPhysicalBuffersLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosTailDropConfigPhysicalBuffersLimit.setStatus("current")
_EltQosTailDropConfigTotalDescriptorsLimit_Type = Integer32
_EltQosTailDropConfigTotalDescriptorsLimit_Object = MibTableColumn
eltQosTailDropConfigTotalDescriptorsLimit = _EltQosTailDropConfigTotalDescriptorsLimit_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 1, 3, 1, 3),
    _EltQosTailDropConfigTotalDescriptorsLimit_Type()
)
eltQosTailDropConfigTotalDescriptorsLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosTailDropConfigTotalDescriptorsLimit.setStatus("current")
_EltQosTailDropConfigTotalBuffersLimit_Type = Integer32
_EltQosTailDropConfigTotalBuffersLimit_Object = MibTableColumn
eltQosTailDropConfigTotalBuffersLimit = _EltQosTailDropConfigTotalBuffersLimit_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 1, 3, 1, 4),
    _EltQosTailDropConfigTotalBuffersLimit_Type()
)
eltQosTailDropConfigTotalBuffersLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosTailDropConfigTotalBuffersLimit.setStatus("current")
_EltQosTailDropConfigMCDescriptorsLimit_Type = Integer32
_EltQosTailDropConfigMCDescriptorsLimit_Object = MibTableColumn
eltQosTailDropConfigMCDescriptorsLimit = _EltQosTailDropConfigMCDescriptorsLimit_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 1, 3, 1, 5),
    _EltQosTailDropConfigMCDescriptorsLimit_Type()
)
eltQosTailDropConfigMCDescriptorsLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosTailDropConfigMCDescriptorsLimit.setStatus("current")
_EltQosTailDropConfigMCBuffersLimit_Type = Integer32
_EltQosTailDropConfigMCBuffersLimit_Object = MibTableColumn
eltQosTailDropConfigMCBuffersLimit = _EltQosTailDropConfigMCBuffersLimit_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 1, 3, 1, 6),
    _EltQosTailDropConfigMCBuffersLimit_Type()
)
eltQosTailDropConfigMCBuffersLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosTailDropConfigMCBuffersLimit.setStatus("current")
_EltQosTailDropConfigSharedDescriptorsLimit_Type = Integer32
_EltQosTailDropConfigSharedDescriptorsLimit_Object = MibTableColumn
eltQosTailDropConfigSharedDescriptorsLimit = _EltQosTailDropConfigSharedDescriptorsLimit_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 1, 3, 1, 7),
    _EltQosTailDropConfigSharedDescriptorsLimit_Type()
)
eltQosTailDropConfigSharedDescriptorsLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosTailDropConfigSharedDescriptorsLimit.setStatus("current")
_EltQosTailDropConfigSharedBuffersLimit_Type = Integer32
_EltQosTailDropConfigSharedBuffersLimit_Object = MibTableColumn
eltQosTailDropConfigSharedBuffersLimit = _EltQosTailDropConfigSharedBuffersLimit_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 1, 3, 1, 8),
    _EltQosTailDropConfigSharedBuffersLimit_Type()
)
eltQosTailDropConfigSharedBuffersLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosTailDropConfigSharedBuffersLimit.setStatus("current")
_EltQosTailDropProfileTable_Object = MibTable
eltQosTailDropProfileTable = _EltQosTailDropProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 1, 4)
)
if mibBuilder.loadTexts:
    eltQosTailDropProfileTable.setStatus("current")
_EltQosTailDropProfileEntry_Object = MibTableRow
eltQosTailDropProfileEntry = _EltQosTailDropProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 1, 4, 1)
)
eltQosTailDropProfileEntry.setIndexNames(
    (0, "ELTEX-MES-QOS-TAIL-DROP-MIB", "eltQosTailDropProfile"),
)
if mibBuilder.loadTexts:
    eltQosTailDropProfileEntry.setStatus("current")
_EltQosTailDropProfile_Type = Integer32
_EltQosTailDropProfile_Object = MibTableColumn
eltQosTailDropProfile = _EltQosTailDropProfile_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 1, 4, 1, 1),
    _EltQosTailDropProfile_Type()
)
eltQosTailDropProfile.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltQosTailDropProfile.setStatus("current")
_EltQosTailDropProfilePortLimit_Type = Integer32
_EltQosTailDropProfilePortLimit_Object = MibTableColumn
eltQosTailDropProfilePortLimit = _EltQosTailDropProfilePortLimit_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 1, 4, 1, 2),
    _EltQosTailDropProfilePortLimit_Type()
)
eltQosTailDropProfilePortLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltQosTailDropProfilePortLimit.setStatus("current")
_EltMesQosTailDropStatus_ObjectIdentity = ObjectIdentity
eltMesQosTailDropStatus = _EltMesQosTailDropStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 2)
)
_EltQosTailDropStatusTable_Object = MibTable
eltQosTailDropStatusTable = _EltQosTailDropStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 2, 1)
)
if mibBuilder.loadTexts:
    eltQosTailDropStatusTable.setStatus("current")
_EltQosTailDropStatusEntry_Object = MibTableRow
eltQosTailDropStatusEntry = _EltQosTailDropStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 2, 1, 1)
)
eltQosTailDropStatusEntry.setIndexNames(
    (0, "ELTEX-MES-QOS-TAIL-DROP-MIB", "eltQosTailDropStatusUnitId"),
)
if mibBuilder.loadTexts:
    eltQosTailDropStatusEntry.setStatus("current")
_EltQosTailDropStatusUnitId_Type = Integer32
_EltQosTailDropStatusUnitId_Object = MibTableColumn
eltQosTailDropStatusUnitId = _EltQosTailDropStatusUnitId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 2, 1, 1, 1),
    _EltQosTailDropStatusUnitId_Type()
)
eltQosTailDropStatusUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosTailDropStatusUnitId.setStatus("current")
_EltQosTailDropStatusPhysicalBuffersEnqueuedCounter_Type = Integer32
_EltQosTailDropStatusPhysicalBuffersEnqueuedCounter_Object = MibTableColumn
eltQosTailDropStatusPhysicalBuffersEnqueuedCounter = _EltQosTailDropStatusPhysicalBuffersEnqueuedCounter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 2, 1, 1, 2),
    _EltQosTailDropStatusPhysicalBuffersEnqueuedCounter_Type()
)
eltQosTailDropStatusPhysicalBuffersEnqueuedCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosTailDropStatusPhysicalBuffersEnqueuedCounter.setStatus("current")
_EltQosTailDropStatusTotalDescriptorsEnqueuedCounter_Type = Integer32
_EltQosTailDropStatusTotalDescriptorsEnqueuedCounter_Object = MibTableColumn
eltQosTailDropStatusTotalDescriptorsEnqueuedCounter = _EltQosTailDropStatusTotalDescriptorsEnqueuedCounter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 2, 1, 1, 3),
    _EltQosTailDropStatusTotalDescriptorsEnqueuedCounter_Type()
)
eltQosTailDropStatusTotalDescriptorsEnqueuedCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosTailDropStatusTotalDescriptorsEnqueuedCounter.setStatus("current")
_EltQosTailDropStatusTotalBuffersEnqueuedCounter_Type = Integer32
_EltQosTailDropStatusTotalBuffersEnqueuedCounter_Object = MibTableColumn
eltQosTailDropStatusTotalBuffersEnqueuedCounter = _EltQosTailDropStatusTotalBuffersEnqueuedCounter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 2, 1, 1, 4),
    _EltQosTailDropStatusTotalBuffersEnqueuedCounter_Type()
)
eltQosTailDropStatusTotalBuffersEnqueuedCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosTailDropStatusTotalBuffersEnqueuedCounter.setStatus("current")
_EltQosTailDropStatusTotalMCDescriptorsEnqueuedCounter_Type = Integer32
_EltQosTailDropStatusTotalMCDescriptorsEnqueuedCounter_Object = MibTableColumn
eltQosTailDropStatusTotalMCDescriptorsEnqueuedCounter = _EltQosTailDropStatusTotalMCDescriptorsEnqueuedCounter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 2, 1, 1, 5),
    _EltQosTailDropStatusTotalMCDescriptorsEnqueuedCounter_Type()
)
eltQosTailDropStatusTotalMCDescriptorsEnqueuedCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosTailDropStatusTotalMCDescriptorsEnqueuedCounter.setStatus("current")
_EltQosTailDropStatusTotalMCBuffersEnqueuedCounter_Type = Integer32
_EltQosTailDropStatusTotalMCBuffersEnqueuedCounter_Object = MibTableColumn
eltQosTailDropStatusTotalMCBuffersEnqueuedCounter = _EltQosTailDropStatusTotalMCBuffersEnqueuedCounter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 2, 1, 1, 6),
    _EltQosTailDropStatusTotalMCBuffersEnqueuedCounter_Type()
)
eltQosTailDropStatusTotalMCBuffersEnqueuedCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosTailDropStatusTotalMCBuffersEnqueuedCounter.setStatus("current")
_EltQosTailDropStatusSharedDescriptorsEnqueuedCounter_Type = Integer32
_EltQosTailDropStatusSharedDescriptorsEnqueuedCounter_Object = MibTableColumn
eltQosTailDropStatusSharedDescriptorsEnqueuedCounter = _EltQosTailDropStatusSharedDescriptorsEnqueuedCounter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 2, 1, 1, 7),
    _EltQosTailDropStatusSharedDescriptorsEnqueuedCounter_Type()
)
eltQosTailDropStatusSharedDescriptorsEnqueuedCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosTailDropStatusSharedDescriptorsEnqueuedCounter.setStatus("current")
_EltQosTailDropStatusSharedBuffersEnqueuedCounter_Type = Integer32
_EltQosTailDropStatusSharedBuffersEnqueuedCounter_Object = MibTableColumn
eltQosTailDropStatusSharedBuffersEnqueuedCounter = _EltQosTailDropStatusSharedBuffersEnqueuedCounter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 2, 1, 1, 8),
    _EltQosTailDropStatusSharedBuffersEnqueuedCounter_Type()
)
eltQosTailDropStatusSharedBuffersEnqueuedCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosTailDropStatusSharedBuffersEnqueuedCounter.setStatus("current")
_EltQosTailDropIfStatusTable_Object = MibTable
eltQosTailDropIfStatusTable = _EltQosTailDropIfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 2, 2)
)
if mibBuilder.loadTexts:
    eltQosTailDropIfStatusTable.setStatus("current")
_EltQosTailDropIfStatusEntry_Object = MibTableRow
eltQosTailDropIfStatusEntry = _EltQosTailDropIfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 2, 2, 1)
)
eltQosTailDropIfStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    eltQosTailDropIfStatusEntry.setStatus("current")
_EltQosTailDropIfStatusEnqueuedDescriptorsCounter_Type = Integer32
_EltQosTailDropIfStatusEnqueuedDescriptorsCounter_Object = MibTableColumn
eltQosTailDropIfStatusEnqueuedDescriptorsCounter = _EltQosTailDropIfStatusEnqueuedDescriptorsCounter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 2, 2, 1, 1),
    _EltQosTailDropIfStatusEnqueuedDescriptorsCounter_Type()
)
eltQosTailDropIfStatusEnqueuedDescriptorsCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosTailDropIfStatusEnqueuedDescriptorsCounter.setStatus("current")
_EltQosTailDropIfStatusEnqueuedBuffersCounter_Type = Integer32
_EltQosTailDropIfStatusEnqueuedBuffersCounter_Object = MibTableColumn
eltQosTailDropIfStatusEnqueuedBuffersCounter = _EltQosTailDropIfStatusEnqueuedBuffersCounter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 2, 2, 1, 2),
    _EltQosTailDropIfStatusEnqueuedBuffersCounter_Type()
)
eltQosTailDropIfStatusEnqueuedBuffersCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosTailDropIfStatusEnqueuedBuffersCounter.setStatus("current")
_EltQosTailDropIfStatusDescriptorsLimit_Type = Integer32
_EltQosTailDropIfStatusDescriptorsLimit_Object = MibTableColumn
eltQosTailDropIfStatusDescriptorsLimit = _EltQosTailDropIfStatusDescriptorsLimit_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 2, 2, 1, 3),
    _EltQosTailDropIfStatusDescriptorsLimit_Type()
)
eltQosTailDropIfStatusDescriptorsLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosTailDropIfStatusDescriptorsLimit.setStatus("current")
_EltQosTailDropIfStatusBuffersLimit_Type = Integer32
_EltQosTailDropIfStatusBuffersLimit_Object = MibTableColumn
eltQosTailDropIfStatusBuffersLimit = _EltQosTailDropIfStatusBuffersLimit_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 2, 2, 1, 4),
    _EltQosTailDropIfStatusBuffersLimit_Type()
)
eltQosTailDropIfStatusBuffersLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosTailDropIfStatusBuffersLimit.setStatus("current")
_EltQosTailDropIfQueueStatusTable_Object = MibTable
eltQosTailDropIfQueueStatusTable = _EltQosTailDropIfQueueStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 2, 3)
)
if mibBuilder.loadTexts:
    eltQosTailDropIfQueueStatusTable.setStatus("current")
_EltQosTailDropIfQueueStatusEntry_Object = MibTableRow
eltQosTailDropIfQueueStatusEntry = _EltQosTailDropIfQueueStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 2, 3, 1)
)
eltQosTailDropIfQueueStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ELTEX-MES-QOS-TAIL-DROP-MIB", "eltQosTailDropIfQueueStatusQueueIndex"),
)
if mibBuilder.loadTexts:
    eltQosTailDropIfQueueStatusEntry.setStatus("current")
_EltQosTailDropIfQueueStatusQueueIndex_Type = Integer32
_EltQosTailDropIfQueueStatusQueueIndex_Object = MibTableColumn
eltQosTailDropIfQueueStatusQueueIndex = _EltQosTailDropIfQueueStatusQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 2, 3, 1, 1),
    _EltQosTailDropIfQueueStatusQueueIndex_Type()
)
eltQosTailDropIfQueueStatusQueueIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltQosTailDropIfQueueStatusQueueIndex.setStatus("current")
_EltQosTailDropIfQueueStatusTotalDescriptorsEnqueuedCounter_Type = Integer32
_EltQosTailDropIfQueueStatusTotalDescriptorsEnqueuedCounter_Object = MibTableColumn
eltQosTailDropIfQueueStatusTotalDescriptorsEnqueuedCounter = _EltQosTailDropIfQueueStatusTotalDescriptorsEnqueuedCounter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 2, 3, 1, 2),
    _EltQosTailDropIfQueueStatusTotalDescriptorsEnqueuedCounter_Type()
)
eltQosTailDropIfQueueStatusTotalDescriptorsEnqueuedCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosTailDropIfQueueStatusTotalDescriptorsEnqueuedCounter.setStatus("current")
_EltQosTailDropIfQueueStatusTotalBuffersEnqueuedCounter_Type = Integer32
_EltQosTailDropIfQueueStatusTotalBuffersEnqueuedCounter_Object = MibTableColumn
eltQosTailDropIfQueueStatusTotalBuffersEnqueuedCounter = _EltQosTailDropIfQueueStatusTotalBuffersEnqueuedCounter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 2, 3, 1, 3),
    _EltQosTailDropIfQueueStatusTotalBuffersEnqueuedCounter_Type()
)
eltQosTailDropIfQueueStatusTotalBuffersEnqueuedCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosTailDropIfQueueStatusTotalBuffersEnqueuedCounter.setStatus("current")
_EltQosTailDropIfQueueStatusDP0BuffersLimit_Type = Integer32
_EltQosTailDropIfQueueStatusDP0BuffersLimit_Object = MibTableColumn
eltQosTailDropIfQueueStatusDP0BuffersLimit = _EltQosTailDropIfQueueStatusDP0BuffersLimit_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 2, 3, 1, 4),
    _EltQosTailDropIfQueueStatusDP0BuffersLimit_Type()
)
eltQosTailDropIfQueueStatusDP0BuffersLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosTailDropIfQueueStatusDP0BuffersLimit.setStatus("current")
_EltQosTailDropIfQueueStatusDP1BuffersLimit_Type = Integer32
_EltQosTailDropIfQueueStatusDP1BuffersLimit_Object = MibTableColumn
eltQosTailDropIfQueueStatusDP1BuffersLimit = _EltQosTailDropIfQueueStatusDP1BuffersLimit_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 2, 3, 1, 5),
    _EltQosTailDropIfQueueStatusDP1BuffersLimit_Type()
)
eltQosTailDropIfQueueStatusDP1BuffersLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosTailDropIfQueueStatusDP1BuffersLimit.setStatus("current")
_EltQosTailDropIfQueueStatusDP2BuffersLimit_Type = Integer32
_EltQosTailDropIfQueueStatusDP2BuffersLimit_Object = MibTableColumn
eltQosTailDropIfQueueStatusDP2BuffersLimit = _EltQosTailDropIfQueueStatusDP2BuffersLimit_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 2, 3, 1, 6),
    _EltQosTailDropIfQueueStatusDP2BuffersLimit_Type()
)
eltQosTailDropIfQueueStatusDP2BuffersLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosTailDropIfQueueStatusDP2BuffersLimit.setStatus("current")
_EltQosTailDropIfQueueStatusDP0DescriptorsLimit_Type = Integer32
_EltQosTailDropIfQueueStatusDP0DescriptorsLimit_Object = MibTableColumn
eltQosTailDropIfQueueStatusDP0DescriptorsLimit = _EltQosTailDropIfQueueStatusDP0DescriptorsLimit_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 2, 3, 1, 7),
    _EltQosTailDropIfQueueStatusDP0DescriptorsLimit_Type()
)
eltQosTailDropIfQueueStatusDP0DescriptorsLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosTailDropIfQueueStatusDP0DescriptorsLimit.setStatus("current")
_EltQosTailDropIfQueueStatusDP1DescriptorsLimit_Type = Integer32
_EltQosTailDropIfQueueStatusDP1DescriptorsLimit_Object = MibTableColumn
eltQosTailDropIfQueueStatusDP1DescriptorsLimit = _EltQosTailDropIfQueueStatusDP1DescriptorsLimit_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 2, 3, 1, 8),
    _EltQosTailDropIfQueueStatusDP1DescriptorsLimit_Type()
)
eltQosTailDropIfQueueStatusDP1DescriptorsLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosTailDropIfQueueStatusDP1DescriptorsLimit.setStatus("current")
_EltQosTailDropIfQueueStatusDP2DescriptorsLimit_Type = Integer32
_EltQosTailDropIfQueueStatusDP2DescriptorsLimit_Object = MibTableColumn
eltQosTailDropIfQueueStatusDP2DescriptorsLimit = _EltQosTailDropIfQueueStatusDP2DescriptorsLimit_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12, 1, 2, 3, 1, 9),
    _EltQosTailDropIfQueueStatusDP2DescriptorsLimit_Type()
)
eltQosTailDropIfQueueStatusDP2DescriptorsLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosTailDropIfQueueStatusDP2DescriptorsLimit.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-QOS-TAIL-DROP-MIB",
    **{"eltMesQosTailDropMibMIBObjects": eltMesQosTailDropMibMIBObjects,
       "eltMesQosTailDropConfig": eltMesQosTailDropConfig,
       "eltQosTailDropProfileQueueTable": eltQosTailDropProfileQueueTable,
       "eltQosTailDropProfileQueueEntry": eltQosTailDropProfileQueueEntry,
       "eltQosTailDropProfileIndex": eltQosTailDropProfileIndex,
       "eltQosTailDropProfileQueueIndex": eltQosTailDropProfileQueueIndex,
       "eltQosTailDropProfileQueueSharedPoolUsage": eltQosTailDropProfileQueueSharedPoolUsage,
       "eltQosTailDropProfileQueueLimit": eltQosTailDropProfileQueueLimit,
       "eltQosTailDropIfConfigTable": eltQosTailDropIfConfigTable,
       "eltQosTailDropIfConfigEntry": eltQosTailDropIfConfigEntry,
       "eltQosTailDropIfProfileIndex": eltQosTailDropIfProfileIndex,
       "eltQosTailDropConfigTable": eltQosTailDropConfigTable,
       "eltQosTailDropConfigEntry": eltQosTailDropConfigEntry,
       "eltQosTailDropConfigUnitId": eltQosTailDropConfigUnitId,
       "eltQosTailDropConfigPhysicalBuffersLimit": eltQosTailDropConfigPhysicalBuffersLimit,
       "eltQosTailDropConfigTotalDescriptorsLimit": eltQosTailDropConfigTotalDescriptorsLimit,
       "eltQosTailDropConfigTotalBuffersLimit": eltQosTailDropConfigTotalBuffersLimit,
       "eltQosTailDropConfigMCDescriptorsLimit": eltQosTailDropConfigMCDescriptorsLimit,
       "eltQosTailDropConfigMCBuffersLimit": eltQosTailDropConfigMCBuffersLimit,
       "eltQosTailDropConfigSharedDescriptorsLimit": eltQosTailDropConfigSharedDescriptorsLimit,
       "eltQosTailDropConfigSharedBuffersLimit": eltQosTailDropConfigSharedBuffersLimit,
       "eltQosTailDropProfileTable": eltQosTailDropProfileTable,
       "eltQosTailDropProfileEntry": eltQosTailDropProfileEntry,
       "eltQosTailDropProfile": eltQosTailDropProfile,
       "eltQosTailDropProfilePortLimit": eltQosTailDropProfilePortLimit,
       "eltMesQosTailDropStatus": eltMesQosTailDropStatus,
       "eltQosTailDropStatusTable": eltQosTailDropStatusTable,
       "eltQosTailDropStatusEntry": eltQosTailDropStatusEntry,
       "eltQosTailDropStatusUnitId": eltQosTailDropStatusUnitId,
       "eltQosTailDropStatusPhysicalBuffersEnqueuedCounter": eltQosTailDropStatusPhysicalBuffersEnqueuedCounter,
       "eltQosTailDropStatusTotalDescriptorsEnqueuedCounter": eltQosTailDropStatusTotalDescriptorsEnqueuedCounter,
       "eltQosTailDropStatusTotalBuffersEnqueuedCounter": eltQosTailDropStatusTotalBuffersEnqueuedCounter,
       "eltQosTailDropStatusTotalMCDescriptorsEnqueuedCounter": eltQosTailDropStatusTotalMCDescriptorsEnqueuedCounter,
       "eltQosTailDropStatusTotalMCBuffersEnqueuedCounter": eltQosTailDropStatusTotalMCBuffersEnqueuedCounter,
       "eltQosTailDropStatusSharedDescriptorsEnqueuedCounter": eltQosTailDropStatusSharedDescriptorsEnqueuedCounter,
       "eltQosTailDropStatusSharedBuffersEnqueuedCounter": eltQosTailDropStatusSharedBuffersEnqueuedCounter,
       "eltQosTailDropIfStatusTable": eltQosTailDropIfStatusTable,
       "eltQosTailDropIfStatusEntry": eltQosTailDropIfStatusEntry,
       "eltQosTailDropIfStatusEnqueuedDescriptorsCounter": eltQosTailDropIfStatusEnqueuedDescriptorsCounter,
       "eltQosTailDropIfStatusEnqueuedBuffersCounter": eltQosTailDropIfStatusEnqueuedBuffersCounter,
       "eltQosTailDropIfStatusDescriptorsLimit": eltQosTailDropIfStatusDescriptorsLimit,
       "eltQosTailDropIfStatusBuffersLimit": eltQosTailDropIfStatusBuffersLimit,
       "eltQosTailDropIfQueueStatusTable": eltQosTailDropIfQueueStatusTable,
       "eltQosTailDropIfQueueStatusEntry": eltQosTailDropIfQueueStatusEntry,
       "eltQosTailDropIfQueueStatusQueueIndex": eltQosTailDropIfQueueStatusQueueIndex,
       "eltQosTailDropIfQueueStatusTotalDescriptorsEnqueuedCounter": eltQosTailDropIfQueueStatusTotalDescriptorsEnqueuedCounter,
       "eltQosTailDropIfQueueStatusTotalBuffersEnqueuedCounter": eltQosTailDropIfQueueStatusTotalBuffersEnqueuedCounter,
       "eltQosTailDropIfQueueStatusDP0BuffersLimit": eltQosTailDropIfQueueStatusDP0BuffersLimit,
       "eltQosTailDropIfQueueStatusDP1BuffersLimit": eltQosTailDropIfQueueStatusDP1BuffersLimit,
       "eltQosTailDropIfQueueStatusDP2BuffersLimit": eltQosTailDropIfQueueStatusDP2BuffersLimit,
       "eltQosTailDropIfQueueStatusDP0DescriptorsLimit": eltQosTailDropIfQueueStatusDP0DescriptorsLimit,
       "eltQosTailDropIfQueueStatusDP1DescriptorsLimit": eltQosTailDropIfQueueStatusDP1DescriptorsLimit,
       "eltQosTailDropIfQueueStatusDP2DescriptorsLimit": eltQosTailDropIfQueueStatusDP2DescriptorsLimit}
)
