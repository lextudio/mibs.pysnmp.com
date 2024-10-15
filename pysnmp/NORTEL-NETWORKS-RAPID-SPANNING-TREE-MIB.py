# SNMP MIB module (NORTEL-NETWORKS-RAPID-SPANNING-TREE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NORTEL-NETWORKS-RAPID-SPANNING-TREE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:51 2024
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

(BridgeId,
 Timeout,
 dot1dBaseBridgeAddress,
 dot1dStpDesignatedRoot,
 dot1dStpPort) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId",
    "Timeout",
    "dot1dBaseBridgeAddress",
    "dot1dStpDesignatedRoot",
    "dot1dStpPort")

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

(bayStackMibs,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "bayStackMibs")


# MODULE-IDENTITY

nnRapidSpanningTreeMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 4)
)
nnRapidSpanningTreeMib.setRevisions(
        ("2004-02-24 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NnRstNotifications_ObjectIdentity = ObjectIdentity
nnRstNotifications = _NnRstNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 0)
)
_NnRstObjects_ObjectIdentity = ObjectIdentity
nnRstObjects = _NnRstObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1)
)
_NnRstDot1d_ObjectIdentity = ObjectIdentity
nnRstDot1d = _NnRstDot1d_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 1)
)
_NnRstDot1dScalars_ObjectIdentity = ObjectIdentity
nnRstDot1dScalars = _NnRstDot1dScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 1, 1)
)


class _NnRstDot1dStpVersion_Type(Integer32):
    """Custom type nnRstDot1dStpVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rstp", 2),
          ("stpCompatible", 0))
    )


_NnRstDot1dStpVersion_Type.__name__ = "Integer32"
_NnRstDot1dStpVersion_Object = MibScalar
nnRstDot1dStpVersion = _NnRstDot1dStpVersion_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 1, 1, 1),
    _NnRstDot1dStpVersion_Type()
)
nnRstDot1dStpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnRstDot1dStpVersion.setStatus("current")


class _NnRstDot1dStpTxHoldCount_Type(Integer32):
    """Custom type nnRstDot1dStpTxHoldCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_NnRstDot1dStpTxHoldCount_Type.__name__ = "Integer32"
_NnRstDot1dStpTxHoldCount_Object = MibScalar
nnRstDot1dStpTxHoldCount = _NnRstDot1dStpTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 1, 1, 2),
    _NnRstDot1dStpTxHoldCount_Type()
)
nnRstDot1dStpTxHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnRstDot1dStpTxHoldCount.setStatus("current")


class _NnRstDot1dStpPathCostDefault_Type(Integer32):
    """Custom type nnRstDot1dStpPathCostDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stp8021d1998", 1),
          ("stp8021t2001", 2))
    )


_NnRstDot1dStpPathCostDefault_Type.__name__ = "Integer32"
_NnRstDot1dStpPathCostDefault_Object = MibScalar
nnRstDot1dStpPathCostDefault = _NnRstDot1dStpPathCostDefault_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 1, 1, 3),
    _NnRstDot1dStpPathCostDefault_Type()
)
nnRstDot1dStpPathCostDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnRstDot1dStpPathCostDefault.setStatus("current")
_NnRstDot1dStpPortTable_Object = MibTable
nnRstDot1dStpPortTable = _NnRstDot1dStpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    nnRstDot1dStpPortTable.setStatus("current")
_NnRstDot1dStpPortEntry_Object = MibTableRow
nnRstDot1dStpPortEntry = _NnRstDot1dStpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 1, 2, 1)
)
nnRstDot1dStpPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dStpPort"),
)
if mibBuilder.loadTexts:
    nnRstDot1dStpPortEntry.setStatus("current")
_NnRstDot1dStpPortProtocolMigration_Type = TruthValue
_NnRstDot1dStpPortProtocolMigration_Object = MibTableColumn
nnRstDot1dStpPortProtocolMigration = _NnRstDot1dStpPortProtocolMigration_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 1, 2, 1, 1),
    _NnRstDot1dStpPortProtocolMigration_Type()
)
nnRstDot1dStpPortProtocolMigration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnRstDot1dStpPortProtocolMigration.setStatus("current")
_NnRstDot1dStpPortAdminEdgePort_Type = TruthValue
_NnRstDot1dStpPortAdminEdgePort_Object = MibTableColumn
nnRstDot1dStpPortAdminEdgePort = _NnRstDot1dStpPortAdminEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 1, 2, 1, 2),
    _NnRstDot1dStpPortAdminEdgePort_Type()
)
nnRstDot1dStpPortAdminEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnRstDot1dStpPortAdminEdgePort.setStatus("current")
_NnRstDot1dStpPortOperEdgePort_Type = TruthValue
_NnRstDot1dStpPortOperEdgePort_Object = MibTableColumn
nnRstDot1dStpPortOperEdgePort = _NnRstDot1dStpPortOperEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 1, 2, 1, 3),
    _NnRstDot1dStpPortOperEdgePort_Type()
)
nnRstDot1dStpPortOperEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRstDot1dStpPortOperEdgePort.setStatus("current")


class _NnRstDot1dStpPortAdminPointToPoint_Type(Integer32):
    """Custom type nnRstDot1dStpPortAdminPointToPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("forceFalse", 1),
          ("forceTrue", 0))
    )


_NnRstDot1dStpPortAdminPointToPoint_Type.__name__ = "Integer32"
_NnRstDot1dStpPortAdminPointToPoint_Object = MibTableColumn
nnRstDot1dStpPortAdminPointToPoint = _NnRstDot1dStpPortAdminPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 1, 2, 1, 4),
    _NnRstDot1dStpPortAdminPointToPoint_Type()
)
nnRstDot1dStpPortAdminPointToPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnRstDot1dStpPortAdminPointToPoint.setStatus("current")
_NnRstDot1dStpPortOperPointToPoint_Type = TruthValue
_NnRstDot1dStpPortOperPointToPoint_Object = MibTableColumn
nnRstDot1dStpPortOperPointToPoint = _NnRstDot1dStpPortOperPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 1, 2, 1, 5),
    _NnRstDot1dStpPortOperPointToPoint_Type()
)
nnRstDot1dStpPortOperPointToPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRstDot1dStpPortOperPointToPoint.setStatus("current")
_NnRstDot1dStpPortParticipating_Type = TruthValue
_NnRstDot1dStpPortParticipating_Object = MibTableColumn
nnRstDot1dStpPortParticipating = _NnRstDot1dStpPortParticipating_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 1, 2, 1, 6),
    _NnRstDot1dStpPortParticipating_Type()
)
nnRstDot1dStpPortParticipating.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnRstDot1dStpPortParticipating.setStatus("current")
_NnRstDot1w_ObjectIdentity = ObjectIdentity
nnRstDot1w = _NnRstDot1w_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 2)
)
_NnRstDot1wScalars_ObjectIdentity = ObjectIdentity
nnRstDot1wScalars = _NnRstDot1wScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 2, 1)
)
_NnRstDot1wRstpUpCount_Type = Counter32
_NnRstDot1wRstpUpCount_Object = MibScalar
nnRstDot1wRstpUpCount = _NnRstDot1wRstpUpCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 2, 1, 1),
    _NnRstDot1wRstpUpCount_Type()
)
nnRstDot1wRstpUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRstDot1wRstpUpCount.setStatus("current")
_NnRstDot1wRstpDownCount_Type = Counter32
_NnRstDot1wRstpDownCount_Object = MibScalar
nnRstDot1wRstpDownCount = _NnRstDot1wRstpDownCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 2, 1, 2),
    _NnRstDot1wRstpDownCount_Type()
)
nnRstDot1wRstpDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRstDot1wRstpDownCount.setStatus("current")
_NnRstDot1wNewRootIdCount_Type = Counter32
_NnRstDot1wNewRootIdCount_Object = MibScalar
nnRstDot1wNewRootIdCount = _NnRstDot1wNewRootIdCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 2, 1, 3),
    _NnRstDot1wNewRootIdCount_Type()
)
nnRstDot1wNewRootIdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRstDot1wNewRootIdCount.setStatus("current")


class _NnRstDot1wPortRoleSelSmState_Type(Integer32):
    """Custom type nnRstDot1wPortRoleSelSmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("initbridge", 0),
          ("roleselection", 1))
    )


_NnRstDot1wPortRoleSelSmState_Type.__name__ = "Integer32"
_NnRstDot1wPortRoleSelSmState_Object = MibScalar
nnRstDot1wPortRoleSelSmState = _NnRstDot1wPortRoleSelSmState_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 2, 1, 4),
    _NnRstDot1wPortRoleSelSmState_Type()
)
nnRstDot1wPortRoleSelSmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRstDot1wPortRoleSelSmState.setStatus("current")
_NnRstDot1wOldDesignatedRoot_Type = BridgeId
_NnRstDot1wOldDesignatedRoot_Object = MibScalar
nnRstDot1wOldDesignatedRoot = _NnRstDot1wOldDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 2, 1, 5),
    _NnRstDot1wOldDesignatedRoot_Type()
)
nnRstDot1wOldDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRstDot1wOldDesignatedRoot.setStatus("current")
_NnRstDot1wPortTable_Object = MibTable
nnRstDot1wPortTable = _NnRstDot1wPortTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 2, 2)
)
if mibBuilder.loadTexts:
    nnRstDot1wPortTable.setStatus("current")
_NnRstDot1wPortEntry_Object = MibTableRow
nnRstDot1wPortEntry = _NnRstDot1wPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 2, 2, 1)
)
nnRstDot1wPortEntry.setIndexNames(
    (0, "NORTEL-NETWORKS-RAPID-SPANNING-TREE-MIB", "nnRstDot1wPort"),
)
if mibBuilder.loadTexts:
    nnRstDot1wPortEntry.setStatus("current")


class _NnRstDot1wPort_Type(Integer32):
    """Custom type nnRstDot1wPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_NnRstDot1wPort_Type.__name__ = "Integer32"
_NnRstDot1wPort_Object = MibTableColumn
nnRstDot1wPort = _NnRstDot1wPort_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 2, 2, 1, 1),
    _NnRstDot1wPort_Type()
)
nnRstDot1wPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nnRstDot1wPort.setStatus("current")


class _NnRstDot1wPortRole_Type(Integer32):
    """Custom type nnRstDot1wPortRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("alternatePort", 1),
          ("backupPort", 2),
          ("designatedPort", 4),
          ("disabledPort", 0),
          ("rootPort", 3))
    )


_NnRstDot1wPortRole_Type.__name__ = "Integer32"
_NnRstDot1wPortRole_Object = MibTableColumn
nnRstDot1wPortRole = _NnRstDot1wPortRole_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 2, 2, 1, 2),
    _NnRstDot1wPortRole_Type()
)
nnRstDot1wPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRstDot1wPortRole.setStatus("current")


class _NnRstDot1wPortOperVersion_Type(Integer32):
    """Custom type nnRstDot1wPortOperVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rstp", 2),
          ("stpCompatible", 0))
    )


_NnRstDot1wPortOperVersion_Type.__name__ = "Integer32"
_NnRstDot1wPortOperVersion_Object = MibTableColumn
nnRstDot1wPortOperVersion = _NnRstDot1wPortOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 2, 2, 1, 3),
    _NnRstDot1wPortOperVersion_Type()
)
nnRstDot1wPortOperVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRstDot1wPortOperVersion.setStatus("current")


class _NnRstDot1wPortInfoSmState_Type(Integer32):
    """Custom type nnRstDot1wPortInfoSmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("aged", 1),
          ("agreement", 5),
          ("disabled", 0),
          ("present", 6),
          ("receive", 7),
          ("repeat", 4),
          ("superior", 3),
          ("update", 2))
    )


_NnRstDot1wPortInfoSmState_Type.__name__ = "Integer32"
_NnRstDot1wPortInfoSmState_Object = MibTableColumn
nnRstDot1wPortInfoSmState = _NnRstDot1wPortInfoSmState_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 2, 2, 1, 4),
    _NnRstDot1wPortInfoSmState_Type()
)
nnRstDot1wPortInfoSmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRstDot1wPortInfoSmState.setStatus("current")


class _NnRstDot1wPortMigSmState_Type(Integer32):
    """Custom type nnRstDot1wPortMigSmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("init", 0),
          ("sendingrstp", 2),
          ("sendingstp", 4),
          ("sendrstp", 1),
          ("sendstp", 3))
    )


_NnRstDot1wPortMigSmState_Type.__name__ = "Integer32"
_NnRstDot1wPortMigSmState_Object = MibTableColumn
nnRstDot1wPortMigSmState = _NnRstDot1wPortMigSmState_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 2, 2, 1, 5),
    _NnRstDot1wPortMigSmState_Type()
)
nnRstDot1wPortMigSmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRstDot1wPortMigSmState.setStatus("current")


class _NnRstDot1wPortRoleTransSmState_Type(Integer32):
    """Custom type nnRstDot1wPortRoleTransSmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("backupport", 5),
          ("blockedport", 2),
          ("blockport", 1),
          ("designatedforward", 15),
          ("designatedlearn", 16),
          ("designatedlisten", 17),
          ("designatedport", 4),
          ("designatedpropose", 12),
          ("designatedretired", 14),
          ("designatedsynced", 13),
          ("init", 0),
          ("reroot", 8),
          ("rerooted", 11),
          ("rootagreed", 7),
          ("rootforward", 9),
          ("rootlearn", 10),
          ("rootport", 3),
          ("rootproposed", 6))
    )


_NnRstDot1wPortRoleTransSmState_Type.__name__ = "Integer32"
_NnRstDot1wPortRoleTransSmState_Object = MibTableColumn
nnRstDot1wPortRoleTransSmState = _NnRstDot1wPortRoleTransSmState_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 2, 2, 1, 6),
    _NnRstDot1wPortRoleTransSmState_Type()
)
nnRstDot1wPortRoleTransSmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRstDot1wPortRoleTransSmState.setStatus("current")


class _NnRstDot1wPortStateTransSmState_Type(Integer32):
    """Custom type nnRstDot1wPortStateTransSmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discarding", 0),
          ("forwarding", 2),
          ("learning", 1))
    )


_NnRstDot1wPortStateTransSmState_Type.__name__ = "Integer32"
_NnRstDot1wPortStateTransSmState_Object = MibTableColumn
nnRstDot1wPortStateTransSmState = _NnRstDot1wPortStateTransSmState_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 2, 2, 1, 7),
    _NnRstDot1wPortStateTransSmState_Type()
)
nnRstDot1wPortStateTransSmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRstDot1wPortStateTransSmState.setStatus("current")


class _NnRstDot1wPortTopoChSmState_Type(Integer32):
    """Custom type nnRstDot1wPortTopoChSmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("acknowledged", 7),
          ("active", 2),
          ("detected", 3),
          ("inactive", 1),
          ("init", 0),
          ("notifiedtc", 5),
          ("notifiedtcn", 4),
          ("propagating", 6))
    )


_NnRstDot1wPortTopoChSmState_Type.__name__ = "Integer32"
_NnRstDot1wPortTopoChSmState_Object = MibTableColumn
nnRstDot1wPortTopoChSmState = _NnRstDot1wPortTopoChSmState_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 2, 2, 1, 8),
    _NnRstDot1wPortTopoChSmState_Type()
)
nnRstDot1wPortTopoChSmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRstDot1wPortTopoChSmState.setStatus("current")


class _NnRstDot1wPortTxSmState_Type(Integer32):
    """Custom type nnRstDot1wPortTxSmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("idle", 5),
          ("transmitconfig", 2),
          ("transmitinit", 0),
          ("transmitperiodic", 1),
          ("transmitrstp", 4),
          ("transmittcn", 3))
    )


_NnRstDot1wPortTxSmState_Type.__name__ = "Integer32"
_NnRstDot1wPortTxSmState_Object = MibTableColumn
nnRstDot1wPortTxSmState = _NnRstDot1wPortTxSmState_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 2, 2, 1, 9),
    _NnRstDot1wPortTxSmState_Type()
)
nnRstDot1wPortTxSmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRstDot1wPortTxSmState.setStatus("current")
_NnRstDot1wPortRxRstBpduCount_Type = Counter32
_NnRstDot1wPortRxRstBpduCount_Object = MibTableColumn
nnRstDot1wPortRxRstBpduCount = _NnRstDot1wPortRxRstBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 2, 2, 1, 10),
    _NnRstDot1wPortRxRstBpduCount_Type()
)
nnRstDot1wPortRxRstBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRstDot1wPortRxRstBpduCount.setStatus("current")
_NnRstDot1wPortRxConfigBpduCount_Type = Counter32
_NnRstDot1wPortRxConfigBpduCount_Object = MibTableColumn
nnRstDot1wPortRxConfigBpduCount = _NnRstDot1wPortRxConfigBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 2, 2, 1, 11),
    _NnRstDot1wPortRxConfigBpduCount_Type()
)
nnRstDot1wPortRxConfigBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRstDot1wPortRxConfigBpduCount.setStatus("current")
_NnRstDot1wPortRxTcnBpduCount_Type = Counter32
_NnRstDot1wPortRxTcnBpduCount_Object = MibTableColumn
nnRstDot1wPortRxTcnBpduCount = _NnRstDot1wPortRxTcnBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 2, 2, 1, 12),
    _NnRstDot1wPortRxTcnBpduCount_Type()
)
nnRstDot1wPortRxTcnBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRstDot1wPortRxTcnBpduCount.setStatus("current")
_NnRstDot1wPortTxRstBpduCount_Type = Counter32
_NnRstDot1wPortTxRstBpduCount_Object = MibTableColumn
nnRstDot1wPortTxRstBpduCount = _NnRstDot1wPortTxRstBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 2, 2, 1, 13),
    _NnRstDot1wPortTxRstBpduCount_Type()
)
nnRstDot1wPortTxRstBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRstDot1wPortTxRstBpduCount.setStatus("current")
_NnRstDot1wPortTxConfigBpduCount_Type = Counter32
_NnRstDot1wPortTxConfigBpduCount_Object = MibTableColumn
nnRstDot1wPortTxConfigBpduCount = _NnRstDot1wPortTxConfigBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 2, 2, 1, 14),
    _NnRstDot1wPortTxConfigBpduCount_Type()
)
nnRstDot1wPortTxConfigBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRstDot1wPortTxConfigBpduCount.setStatus("current")
_NnRstDot1wPortTxTcnBpduCount_Type = Counter32
_NnRstDot1wPortTxTcnBpduCount_Object = MibTableColumn
nnRstDot1wPortTxTcnBpduCount = _NnRstDot1wPortTxTcnBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 2, 2, 1, 15),
    _NnRstDot1wPortTxTcnBpduCount_Type()
)
nnRstDot1wPortTxTcnBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRstDot1wPortTxTcnBpduCount.setStatus("current")
_NnRstDot1wPortInvalidRstBpduRxCount_Type = Counter32
_NnRstDot1wPortInvalidRstBpduRxCount_Object = MibTableColumn
nnRstDot1wPortInvalidRstBpduRxCount = _NnRstDot1wPortInvalidRstBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 2, 2, 1, 16),
    _NnRstDot1wPortInvalidRstBpduRxCount_Type()
)
nnRstDot1wPortInvalidRstBpduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRstDot1wPortInvalidRstBpduRxCount.setStatus("current")
_NnRstDot1wPortInvalidConfigBpduRxCount_Type = Counter32
_NnRstDot1wPortInvalidConfigBpduRxCount_Object = MibTableColumn
nnRstDot1wPortInvalidConfigBpduRxCount = _NnRstDot1wPortInvalidConfigBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 2, 2, 1, 17),
    _NnRstDot1wPortInvalidConfigBpduRxCount_Type()
)
nnRstDot1wPortInvalidConfigBpduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRstDot1wPortInvalidConfigBpduRxCount.setStatus("current")
_NnRstDot1wPortInvalidTcnBpduRxCount_Type = Counter32
_NnRstDot1wPortInvalidTcnBpduRxCount_Object = MibTableColumn
nnRstDot1wPortInvalidTcnBpduRxCount = _NnRstDot1wPortInvalidTcnBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 2, 2, 1, 18),
    _NnRstDot1wPortInvalidTcnBpduRxCount_Type()
)
nnRstDot1wPortInvalidTcnBpduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRstDot1wPortInvalidTcnBpduRxCount.setStatus("current")
_NnRstDot1wPortProtocolMigrationCount_Type = Counter32
_NnRstDot1wPortProtocolMigrationCount_Object = MibTableColumn
nnRstDot1wPortProtocolMigrationCount = _NnRstDot1wPortProtocolMigrationCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 2, 2, 1, 19),
    _NnRstDot1wPortProtocolMigrationCount_Type()
)
nnRstDot1wPortProtocolMigrationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRstDot1wPortProtocolMigrationCount.setStatus("current")
_NnRstDot1wPortEffectivePortState_Type = TruthValue
_NnRstDot1wPortEffectivePortState_Object = MibTableColumn
nnRstDot1wPortEffectivePortState = _NnRstDot1wPortEffectivePortState_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 2, 2, 1, 20),
    _NnRstDot1wPortEffectivePortState_Type()
)
nnRstDot1wPortEffectivePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRstDot1wPortEffectivePortState.setStatus("current")
_NnRstNotificationControl_ObjectIdentity = ObjectIdentity
nnRstNotificationControl = _NnRstNotificationControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 3)
)
_NnRstNotificationControlScalars_ObjectIdentity = ObjectIdentity
nnRstNotificationControlScalars = _NnRstNotificationControlScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 3, 1)
)


class _NnRstSetNotifications_Type(Integer32):
    """Custom type nnRstSetNotifications based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NnRstSetNotifications_Type.__name__ = "Integer32"
_NnRstSetNotifications_Object = MibScalar
nnRstSetNotifications = _NnRstSetNotifications_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 3, 1, 1),
    _NnRstSetNotifications_Type()
)
nnRstSetNotifications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnRstSetNotifications.setStatus("current")


class _NnRstGenNotificationType_Type(Integer32):
    """Custom type nnRstGenNotificationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("none", 0),
          ("up", 1))
    )


_NnRstGenNotificationType_Type.__name__ = "Integer32"
_NnRstGenNotificationType_Object = MibScalar
nnRstGenNotificationType = _NnRstGenNotificationType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 3, 1, 2),
    _NnRstGenNotificationType_Type()
)
nnRstGenNotificationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRstGenNotificationType.setStatus("current")


class _NnRstErrNotificationType_Type(Integer32):
    """Custom type nnRstErrNotificationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bufffail", 2),
          ("memfail", 1),
          ("none", 0))
    )


_NnRstErrNotificationType_Type.__name__ = "Integer32"
_NnRstErrNotificationType_Object = MibScalar
nnRstErrNotificationType = _NnRstErrNotificationType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 3, 1, 3),
    _NnRstErrNotificationType_Type()
)
nnRstErrNotificationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRstErrNotificationType.setStatus("current")
_NnRstPortNotificationTable_Object = MibTable
nnRstPortNotificationTable = _NnRstPortNotificationTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 3, 2)
)
if mibBuilder.loadTexts:
    nnRstPortNotificationTable.setStatus("current")
_NnRstPortNotificationEntry_Object = MibTableRow
nnRstPortNotificationEntry = _NnRstPortNotificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 3, 2, 1)
)
nnRstPortNotificationEntry.setIndexNames(
    (0, "NORTEL-NETWORKS-RAPID-SPANNING-TREE-MIB", "nnRstPortNotificationIndex"),
)
if mibBuilder.loadTexts:
    nnRstPortNotificationEntry.setStatus("current")


class _NnRstPortNotificationIndex_Type(Integer32):
    """Custom type nnRstPortNotificationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_NnRstPortNotificationIndex_Type.__name__ = "Integer32"
_NnRstPortNotificationIndex_Object = MibTableColumn
nnRstPortNotificationIndex = _NnRstPortNotificationIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 3, 2, 1, 1),
    _NnRstPortNotificationIndex_Type()
)
nnRstPortNotificationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nnRstPortNotificationIndex.setStatus("current")


class _NnRstPortNotificationMigrationType_Type(Integer32):
    """Custom type nnRstPortNotificationMigrationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("sendrstp", 1),
          ("sendstp", 0))
    )


_NnRstPortNotificationMigrationType_Type.__name__ = "Integer32"
_NnRstPortNotificationMigrationType_Object = MibTableColumn
nnRstPortNotificationMigrationType = _NnRstPortNotificationMigrationType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 3, 2, 1, 2),
    _NnRstPortNotificationMigrationType_Type()
)
nnRstPortNotificationMigrationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRstPortNotificationMigrationType.setStatus("current")


class _NnRstPortNotificationPktErrType_Type(Integer32):
    """Custom type nnRstPortNotificationPktErrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("configLengthErr", 2),
          ("fwdDelayErr", 6),
          ("helloTimeErr", 7),
          ("invalidBpdu", 1),
          ("maxAgeErr", 5),
          ("protocolIdErr", 0),
          ("rstpLengthErr", 4),
          ("tcnLengthErr", 3))
    )


_NnRstPortNotificationPktErrType_Type.__name__ = "Integer32"
_NnRstPortNotificationPktErrType_Object = MibTableColumn
nnRstPortNotificationPktErrType = _NnRstPortNotificationPktErrType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 3, 2, 1, 3),
    _NnRstPortNotificationPktErrType_Type()
)
nnRstPortNotificationPktErrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRstPortNotificationPktErrType.setStatus("current")
_NnRstPortNotificationPktErrVal_Type = Integer32
_NnRstPortNotificationPktErrVal_Object = MibTableColumn
nnRstPortNotificationPktErrVal = _NnRstPortNotificationPktErrVal_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 1, 3, 2, 1, 4),
    _NnRstPortNotificationPktErrVal_Type()
)
nnRstPortNotificationPktErrVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnRstPortNotificationPktErrVal.setStatus("current")

# Managed Objects groups


# Notification objects

nnRstGeneralEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 0, 1)
)
nnRstGeneralEvent.setObjects(
      *(("BRIDGE-MIB", "dot1dBaseBridgeAddress"),
        ("NORTEL-NETWORKS-RAPID-SPANNING-TREE-MIB", "nnRstGenNotificationType"))
)
if mibBuilder.loadTexts:
    nnRstGeneralEvent.setStatus(
        "current"
    )

nnRstErrorEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 0, 2)
)
nnRstErrorEvent.setObjects(
      *(("BRIDGE-MIB", "dot1dBaseBridgeAddress"),
        ("NORTEL-NETWORKS-RAPID-SPANNING-TREE-MIB", "nnRstErrNotificationType"))
)
if mibBuilder.loadTexts:
    nnRstErrorEvent.setStatus(
        "current"
    )

nnRstNewRoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 0, 3)
)
nnRstNewRoot.setObjects(
      *(("BRIDGE-MIB", "dot1dBaseBridgeAddress"),
        ("NORTEL-NETWORKS-RAPID-SPANNING-TREE-MIB", "nnRstDot1wOldDesignatedRoot"),
        ("BRIDGE-MIB", "dot1dStpDesignatedRoot"))
)
if mibBuilder.loadTexts:
    nnRstNewRoot.setStatus(
        "current"
    )

nnRstTopologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 0, 4)
)
nnRstTopologyChange.setObjects(
    ("BRIDGE-MIB", "dot1dBaseBridgeAddress")
)
if mibBuilder.loadTexts:
    nnRstTopologyChange.setStatus(
        "current"
    )

nnRstProtocolMigration = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 4, 0, 5)
)
nnRstProtocolMigration.setObjects(
      *(("BRIDGE-MIB", "dot1dBaseBridgeAddress"),
        ("NORTEL-NETWORKS-RAPID-SPANNING-TREE-MIB", "nnRstDot1dStpVersion"),
        ("NORTEL-NETWORKS-RAPID-SPANNING-TREE-MIB", "nnRstPortNotificationMigrationType"))
)
if mibBuilder.loadTexts:
    nnRstProtocolMigration.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NORTEL-NETWORKS-RAPID-SPANNING-TREE-MIB",
    **{"nnRapidSpanningTreeMib": nnRapidSpanningTreeMib,
       "nnRstNotifications": nnRstNotifications,
       "nnRstGeneralEvent": nnRstGeneralEvent,
       "nnRstErrorEvent": nnRstErrorEvent,
       "nnRstNewRoot": nnRstNewRoot,
       "nnRstTopologyChange": nnRstTopologyChange,
       "nnRstProtocolMigration": nnRstProtocolMigration,
       "nnRstObjects": nnRstObjects,
       "nnRstDot1d": nnRstDot1d,
       "nnRstDot1dScalars": nnRstDot1dScalars,
       "nnRstDot1dStpVersion": nnRstDot1dStpVersion,
       "nnRstDot1dStpTxHoldCount": nnRstDot1dStpTxHoldCount,
       "nnRstDot1dStpPathCostDefault": nnRstDot1dStpPathCostDefault,
       "nnRstDot1dStpPortTable": nnRstDot1dStpPortTable,
       "nnRstDot1dStpPortEntry": nnRstDot1dStpPortEntry,
       "nnRstDot1dStpPortProtocolMigration": nnRstDot1dStpPortProtocolMigration,
       "nnRstDot1dStpPortAdminEdgePort": nnRstDot1dStpPortAdminEdgePort,
       "nnRstDot1dStpPortOperEdgePort": nnRstDot1dStpPortOperEdgePort,
       "nnRstDot1dStpPortAdminPointToPoint": nnRstDot1dStpPortAdminPointToPoint,
       "nnRstDot1dStpPortOperPointToPoint": nnRstDot1dStpPortOperPointToPoint,
       "nnRstDot1dStpPortParticipating": nnRstDot1dStpPortParticipating,
       "nnRstDot1w": nnRstDot1w,
       "nnRstDot1wScalars": nnRstDot1wScalars,
       "nnRstDot1wRstpUpCount": nnRstDot1wRstpUpCount,
       "nnRstDot1wRstpDownCount": nnRstDot1wRstpDownCount,
       "nnRstDot1wNewRootIdCount": nnRstDot1wNewRootIdCount,
       "nnRstDot1wPortRoleSelSmState": nnRstDot1wPortRoleSelSmState,
       "nnRstDot1wOldDesignatedRoot": nnRstDot1wOldDesignatedRoot,
       "nnRstDot1wPortTable": nnRstDot1wPortTable,
       "nnRstDot1wPortEntry": nnRstDot1wPortEntry,
       "nnRstDot1wPort": nnRstDot1wPort,
       "nnRstDot1wPortRole": nnRstDot1wPortRole,
       "nnRstDot1wPortOperVersion": nnRstDot1wPortOperVersion,
       "nnRstDot1wPortInfoSmState": nnRstDot1wPortInfoSmState,
       "nnRstDot1wPortMigSmState": nnRstDot1wPortMigSmState,
       "nnRstDot1wPortRoleTransSmState": nnRstDot1wPortRoleTransSmState,
       "nnRstDot1wPortStateTransSmState": nnRstDot1wPortStateTransSmState,
       "nnRstDot1wPortTopoChSmState": nnRstDot1wPortTopoChSmState,
       "nnRstDot1wPortTxSmState": nnRstDot1wPortTxSmState,
       "nnRstDot1wPortRxRstBpduCount": nnRstDot1wPortRxRstBpduCount,
       "nnRstDot1wPortRxConfigBpduCount": nnRstDot1wPortRxConfigBpduCount,
       "nnRstDot1wPortRxTcnBpduCount": nnRstDot1wPortRxTcnBpduCount,
       "nnRstDot1wPortTxRstBpduCount": nnRstDot1wPortTxRstBpduCount,
       "nnRstDot1wPortTxConfigBpduCount": nnRstDot1wPortTxConfigBpduCount,
       "nnRstDot1wPortTxTcnBpduCount": nnRstDot1wPortTxTcnBpduCount,
       "nnRstDot1wPortInvalidRstBpduRxCount": nnRstDot1wPortInvalidRstBpduRxCount,
       "nnRstDot1wPortInvalidConfigBpduRxCount": nnRstDot1wPortInvalidConfigBpduRxCount,
       "nnRstDot1wPortInvalidTcnBpduRxCount": nnRstDot1wPortInvalidTcnBpduRxCount,
       "nnRstDot1wPortProtocolMigrationCount": nnRstDot1wPortProtocolMigrationCount,
       "nnRstDot1wPortEffectivePortState": nnRstDot1wPortEffectivePortState,
       "nnRstNotificationControl": nnRstNotificationControl,
       "nnRstNotificationControlScalars": nnRstNotificationControlScalars,
       "nnRstSetNotifications": nnRstSetNotifications,
       "nnRstGenNotificationType": nnRstGenNotificationType,
       "nnRstErrNotificationType": nnRstErrNotificationType,
       "nnRstPortNotificationTable": nnRstPortNotificationTable,
       "nnRstPortNotificationEntry": nnRstPortNotificationEntry,
       "nnRstPortNotificationIndex": nnRstPortNotificationIndex,
       "nnRstPortNotificationMigrationType": nnRstPortNotificationMigrationType,
       "nnRstPortNotificationPktErrType": nnRstPortNotificationPktErrType,
       "nnRstPortNotificationPktErrVal": nnRstPortNotificationPktErrVal}
)
