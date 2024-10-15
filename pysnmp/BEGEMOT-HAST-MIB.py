# SNMP MIB module (BEGEMOT-HAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BEGEMOT-HAST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:42 2024
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

(begemot,) = mibBuilder.importSymbols(
    "BEGEMOT-MIB",
    "begemot")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

begemotHast = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 220)
)
begemotHast.setRevisions(
        ("2013-04-13 00:00",
         "2013-07-01 00:00",
         "2013-12-29 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BegemotHastObjects_ObjectIdentity = ObjectIdentity
begemotHastObjects = _BegemotHastObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 220, 1)
)
_HastConfig_ObjectIdentity = ObjectIdentity
hastConfig = _HastConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 1)
)
_HastConfigFile_Type = OctetString
_HastConfigFile_Object = MibScalar
hastConfigFile = _HastConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 1, 1),
    _HastConfigFile_Type()
)
hastConfigFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hastConfigFile.setStatus("current")
_HastResourceTable_Object = MibTable
hastResourceTable = _HastResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2)
)
if mibBuilder.loadTexts:
    hastResourceTable.setStatus("current")
_HastResourceEntry_Object = MibTableRow
hastResourceEntry = _HastResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1)
)
hastResourceEntry.setIndexNames(
    (0, "BEGEMOT-HAST-MIB", "hastResourceIndex"),
)
if mibBuilder.loadTexts:
    hastResourceEntry.setStatus("current")
_HastResourceIndex_Type = Integer32
_HastResourceIndex_Object = MibTableColumn
hastResourceIndex = _HastResourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 1),
    _HastResourceIndex_Type()
)
hastResourceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hastResourceIndex.setStatus("current")
_HastResourceName_Type = OctetString
_HastResourceName_Object = MibTableColumn
hastResourceName = _HastResourceName_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 2),
    _HastResourceName_Type()
)
hastResourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hastResourceName.setStatus("current")


class _HastResourceRole_Type(Integer32):
    """Custom type hastResourceRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("init", 1),
          ("primary", 2),
          ("secondary", 3),
          ("undef", 0))
    )


_HastResourceRole_Type.__name__ = "Integer32"
_HastResourceRole_Object = MibTableColumn
hastResourceRole = _HastResourceRole_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 3),
    _HastResourceRole_Type()
)
hastResourceRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hastResourceRole.setStatus("current")
_HastResourceProvName_Type = OctetString
_HastResourceProvName_Object = MibTableColumn
hastResourceProvName = _HastResourceProvName_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 4),
    _HastResourceProvName_Type()
)
hastResourceProvName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hastResourceProvName.setStatus("current")
_HastResourceLocalPath_Type = OctetString
_HastResourceLocalPath_Object = MibTableColumn
hastResourceLocalPath = _HastResourceLocalPath_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 5),
    _HastResourceLocalPath_Type()
)
hastResourceLocalPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hastResourceLocalPath.setStatus("current")
_HastResourceExtentSize_Type = Integer32
_HastResourceExtentSize_Object = MibTableColumn
hastResourceExtentSize = _HastResourceExtentSize_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 6),
    _HastResourceExtentSize_Type()
)
hastResourceExtentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hastResourceExtentSize.setStatus("current")
_HastResourceKeepDirty_Type = Integer32
_HastResourceKeepDirty_Object = MibTableColumn
hastResourceKeepDirty = _HastResourceKeepDirty_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 7),
    _HastResourceKeepDirty_Type()
)
hastResourceKeepDirty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hastResourceKeepDirty.setStatus("current")
_HastResourceRemoteAddr_Type = OctetString
_HastResourceRemoteAddr_Object = MibTableColumn
hastResourceRemoteAddr = _HastResourceRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 8),
    _HastResourceRemoteAddr_Type()
)
hastResourceRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hastResourceRemoteAddr.setStatus("current")
_HastResourceSourceAddr_Type = OctetString
_HastResourceSourceAddr_Object = MibTableColumn
hastResourceSourceAddr = _HastResourceSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 9),
    _HastResourceSourceAddr_Type()
)
hastResourceSourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hastResourceSourceAddr.setStatus("current")


class _HastResourceReplication_Type(Integer32):
    """Custom type hastResourceReplication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("async", 2),
          ("fullsync", 0),
          ("memsync", 1))
    )


_HastResourceReplication_Type.__name__ = "Integer32"
_HastResourceReplication_Object = MibTableColumn
hastResourceReplication = _HastResourceReplication_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 10),
    _HastResourceReplication_Type()
)
hastResourceReplication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hastResourceReplication.setStatus("current")


class _HastResourceStatus_Type(Integer32):
    """Custom type hastResourceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("complete", 0),
          ("degraded", 1))
    )


_HastResourceStatus_Type.__name__ = "Integer32"
_HastResourceStatus_Object = MibTableColumn
hastResourceStatus = _HastResourceStatus_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 11),
    _HastResourceStatus_Type()
)
hastResourceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hastResourceStatus.setStatus("current")
_HastResourceDirty_Type = Counter64
_HastResourceDirty_Object = MibTableColumn
hastResourceDirty = _HastResourceDirty_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 12),
    _HastResourceDirty_Type()
)
hastResourceDirty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hastResourceDirty.setStatus("current")
_HastResourceReads_Type = Counter64
_HastResourceReads_Object = MibTableColumn
hastResourceReads = _HastResourceReads_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 13),
    _HastResourceReads_Type()
)
hastResourceReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hastResourceReads.setStatus("current")
_HastResourceWrites_Type = Counter64
_HastResourceWrites_Object = MibTableColumn
hastResourceWrites = _HastResourceWrites_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 14),
    _HastResourceWrites_Type()
)
hastResourceWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hastResourceWrites.setStatus("current")
_HastResourceDeletes_Type = Counter64
_HastResourceDeletes_Object = MibTableColumn
hastResourceDeletes = _HastResourceDeletes_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 15),
    _HastResourceDeletes_Type()
)
hastResourceDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hastResourceDeletes.setStatus("current")
_HastResourceFlushes_Type = Counter64
_HastResourceFlushes_Object = MibTableColumn
hastResourceFlushes = _HastResourceFlushes_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 16),
    _HastResourceFlushes_Type()
)
hastResourceFlushes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hastResourceFlushes.setStatus("current")
_HastResourceActivemapUpdates_Type = Counter64
_HastResourceActivemapUpdates_Object = MibTableColumn
hastResourceActivemapUpdates = _HastResourceActivemapUpdates_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 17),
    _HastResourceActivemapUpdates_Type()
)
hastResourceActivemapUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hastResourceActivemapUpdates.setStatus("current")
_HastResourceReadErrors_Type = Counter64
_HastResourceReadErrors_Object = MibTableColumn
hastResourceReadErrors = _HastResourceReadErrors_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 18),
    _HastResourceReadErrors_Type()
)
hastResourceReadErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hastResourceReadErrors.setStatus("current")
_HastResourceWriteErrors_Type = Counter64
_HastResourceWriteErrors_Object = MibTableColumn
hastResourceWriteErrors = _HastResourceWriteErrors_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 19),
    _HastResourceWriteErrors_Type()
)
hastResourceWriteErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hastResourceWriteErrors.setStatus("current")
_HastResourceDeleteErrors_Type = Counter64
_HastResourceDeleteErrors_Object = MibTableColumn
hastResourceDeleteErrors = _HastResourceDeleteErrors_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 20),
    _HastResourceDeleteErrors_Type()
)
hastResourceDeleteErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hastResourceDeleteErrors.setStatus("current")
_HastResourceFlushErrors_Type = Counter64
_HastResourceFlushErrors_Object = MibTableColumn
hastResourceFlushErrors = _HastResourceFlushErrors_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 21),
    _HastResourceFlushErrors_Type()
)
hastResourceFlushErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hastResourceFlushErrors.setStatus("current")
_HastResourceWorkerPid_Type = Integer32
_HastResourceWorkerPid_Object = MibTableColumn
hastResourceWorkerPid = _HastResourceWorkerPid_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 22),
    _HastResourceWorkerPid_Type()
)
hastResourceWorkerPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hastResourceWorkerPid.setStatus("current")
_HastResourceLocalQueue_Type = Unsigned32
_HastResourceLocalQueue_Object = MibTableColumn
hastResourceLocalQueue = _HastResourceLocalQueue_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 23),
    _HastResourceLocalQueue_Type()
)
hastResourceLocalQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hastResourceLocalQueue.setStatus("current")
_HastResourceSendQueue_Type = Unsigned32
_HastResourceSendQueue_Object = MibTableColumn
hastResourceSendQueue = _HastResourceSendQueue_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 24),
    _HastResourceSendQueue_Type()
)
hastResourceSendQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hastResourceSendQueue.setStatus("current")
_HastResourceRecvQueue_Type = Unsigned32
_HastResourceRecvQueue_Object = MibTableColumn
hastResourceRecvQueue = _HastResourceRecvQueue_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 25),
    _HastResourceRecvQueue_Type()
)
hastResourceRecvQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hastResourceRecvQueue.setStatus("current")
_HastResourceDoneQueue_Type = Unsigned32
_HastResourceDoneQueue_Object = MibTableColumn
hastResourceDoneQueue = _HastResourceDoneQueue_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 26),
    _HastResourceDoneQueue_Type()
)
hastResourceDoneQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hastResourceDoneQueue.setStatus("current")
_HastResourceIdleQueue_Type = Unsigned32
_HastResourceIdleQueue_Object = MibTableColumn
hastResourceIdleQueue = _HastResourceIdleQueue_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 220, 1, 2, 1, 27),
    _HastResourceIdleQueue_Type()
)
hastResourceIdleQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hastResourceIdleQueue.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BEGEMOT-HAST-MIB",
    **{"begemotHast": begemotHast,
       "begemotHastObjects": begemotHastObjects,
       "hastConfig": hastConfig,
       "hastConfigFile": hastConfigFile,
       "hastResourceTable": hastResourceTable,
       "hastResourceEntry": hastResourceEntry,
       "hastResourceIndex": hastResourceIndex,
       "hastResourceName": hastResourceName,
       "hastResourceRole": hastResourceRole,
       "hastResourceProvName": hastResourceProvName,
       "hastResourceLocalPath": hastResourceLocalPath,
       "hastResourceExtentSize": hastResourceExtentSize,
       "hastResourceKeepDirty": hastResourceKeepDirty,
       "hastResourceRemoteAddr": hastResourceRemoteAddr,
       "hastResourceSourceAddr": hastResourceSourceAddr,
       "hastResourceReplication": hastResourceReplication,
       "hastResourceStatus": hastResourceStatus,
       "hastResourceDirty": hastResourceDirty,
       "hastResourceReads": hastResourceReads,
       "hastResourceWrites": hastResourceWrites,
       "hastResourceDeletes": hastResourceDeletes,
       "hastResourceFlushes": hastResourceFlushes,
       "hastResourceActivemapUpdates": hastResourceActivemapUpdates,
       "hastResourceReadErrors": hastResourceReadErrors,
       "hastResourceWriteErrors": hastResourceWriteErrors,
       "hastResourceDeleteErrors": hastResourceDeleteErrors,
       "hastResourceFlushErrors": hastResourceFlushErrors,
       "hastResourceWorkerPid": hastResourceWorkerPid,
       "hastResourceLocalQueue": hastResourceLocalQueue,
       "hastResourceSendQueue": hastResourceSendQueue,
       "hastResourceRecvQueue": hastResourceRecvQueue,
       "hastResourceDoneQueue": hastResourceDoneQueue,
       "hastResourceIdleQueue": hastResourceIdleQueue}
)
