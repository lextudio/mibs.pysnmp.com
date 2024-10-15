# SNMP MIB module (PG-BRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PG-BRIDGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:38:35 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(pgainDSLAM,) = mibBuilder.importSymbols(
    "PAIRGAIN-COMMON-HD-MIB",
    "pgainDSLAM")

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
 NotificationType,
 TimeTicks,
 Unsigned32,
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso",
    "mib-2")

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

pgsessionMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8)
)


# Types definitions



class BridgeId(OctetString):
    """Custom type BridgeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )





class Timeout(Integer32):
    """Custom type Timeout based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PgSessionPort_ObjectIdentity = ObjectIdentity
pgSessionPort = _PgSessionPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 1)
)
_PgSessionPortTable_Object = MibTable
pgSessionPortTable = _PgSessionPortTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 1, 1)
)
if mibBuilder.loadTexts:
    pgSessionPortTable.setStatus("mandatory")
_PgSessionPortEntry_Object = MibTableRow
pgSessionPortEntry = _PgSessionPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 1, 1, 1)
)
pgSessionPortEntry.setIndexNames(
    (0, "PG-BRIDGE-MIB", "pgSessionInstance"),
    (0, "PG-BRIDGE-MIB", "pgSessionPortVpi"),
    (0, "PG-BRIDGE-MIB", "pgSessionPortVci"),
)
if mibBuilder.loadTexts:
    pgSessionPortEntry.setStatus("mandatory")
_PgSessionInstance_Type = Integer32
_PgSessionInstance_Object = MibTableColumn
pgSessionInstance = _PgSessionInstance_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 1, 1, 1, 1),
    _PgSessionInstance_Type()
)
pgSessionInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSessionInstance.setStatus("mandatory")
_PgSessionPortVpi_Type = Integer32
_PgSessionPortVpi_Object = MibTableColumn
pgSessionPortVpi = _PgSessionPortVpi_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 1, 1, 1, 2),
    _PgSessionPortVpi_Type()
)
pgSessionPortVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSessionPortVpi.setStatus("mandatory")
_PgSessionPortVci_Type = Integer32
_PgSessionPortVci_Object = MibTableColumn
pgSessionPortVci = _PgSessionPortVci_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 1, 1, 1, 3),
    _PgSessionPortVci_Type()
)
pgSessionPortVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSessionPortVci.setStatus("mandatory")
_PgSessionPortSlotNum_Type = Integer32
_PgSessionPortSlotNum_Object = MibTableColumn
pgSessionPortSlotNum = _PgSessionPortSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 1, 1, 1, 4),
    _PgSessionPortSlotNum_Type()
)
pgSessionPortSlotNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgSessionPortSlotNum.setStatus("mandatory")
_PgSessionPortNum_Type = Integer32
_PgSessionPortNum_Object = MibTableColumn
pgSessionPortNum = _PgSessionPortNum_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 1, 1, 1, 5),
    _PgSessionPortNum_Type()
)
pgSessionPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgSessionPortNum.setStatus("mandatory")
_PgSessionPortIfIndex_Type = Integer32
_PgSessionPortIfIndex_Object = MibTableColumn
pgSessionPortIfIndex = _PgSessionPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 1, 1, 1, 6),
    _PgSessionPortIfIndex_Type()
)
pgSessionPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSessionPortIfIndex.setStatus("mandatory")
_PgSessionPortBridgePort_Type = Integer32
_PgSessionPortBridgePort_Object = MibTableColumn
pgSessionPortBridgePort = _PgSessionPortBridgePort_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 1, 1, 1, 7),
    _PgSessionPortBridgePort_Type()
)
pgSessionPortBridgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSessionPortBridgePort.setStatus("mandatory")


class _PgSessionPortRouterGroupInterface_Type(Integer32):
    """Custom type pgSessionPortRouterGroupInterface based on Integer32"""
    defaultValue = 0


_PgSessionPortRouterGroupInterface_Object = MibTableColumn
pgSessionPortRouterGroupInterface = _PgSessionPortRouterGroupInterface_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 1, 1, 1, 8),
    _PgSessionPortRouterGroupInterface_Type()
)
pgSessionPortRouterGroupInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgSessionPortRouterGroupInterface.setStatus("mandatory")


class _PgSessionPortVlanIdentifier_Type(Integer32):
    """Custom type pgSessionPortVlanIdentifier based on Integer32"""
    defaultValue = 1


_PgSessionPortVlanIdentifier_Object = MibTableColumn
pgSessionPortVlanIdentifier = _PgSessionPortVlanIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 1, 1, 1, 9),
    _PgSessionPortVlanIdentifier_Type()
)
pgSessionPortVlanIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgSessionPortVlanIdentifier.setStatus("mandatory")
_PgSessionPortServiceType_Type = Integer32
_PgSessionPortServiceType_Object = MibTableColumn
pgSessionPortServiceType = _PgSessionPortServiceType_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 1, 1, 1, 10),
    _PgSessionPortServiceType_Type()
)
pgSessionPortServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgSessionPortServiceType.setStatus("mandatory")


class _PgSessionPortSubscriberName_Type(DisplayString):
    """Custom type pgSessionPortSubscriberName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PgSessionPortSubscriberName_Type.__name__ = "DisplayString"
_PgSessionPortSubscriberName_Object = MibTableColumn
pgSessionPortSubscriberName = _PgSessionPortSubscriberName_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 1, 1, 1, 11),
    _PgSessionPortSubscriberName_Type()
)
pgSessionPortSubscriberName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgSessionPortSubscriberName.setStatus("mandatory")
_PgSessionPortRowStatus_Type = RowStatus
_PgSessionPortRowStatus_Object = MibTableColumn
pgSessionPortRowStatus = _PgSessionPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 1, 1, 1, 12),
    _PgSessionPortRowStatus_Type()
)
pgSessionPortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgSessionPortRowStatus.setStatus("mandatory")
_PgDot1dBase_ObjectIdentity = ObjectIdentity
pgDot1dBase = _PgDot1dBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 2)
)
_PgDot1dBaseTable_Object = MibTable
pgDot1dBaseTable = _PgDot1dBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 2, 1)
)
if mibBuilder.loadTexts:
    pgDot1dBaseTable.setStatus("mandatory")
_PgDot1dBaseEntry_Object = MibTableRow
pgDot1dBaseEntry = _PgDot1dBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 2, 1, 1)
)
pgDot1dBaseEntry.setIndexNames(
    (0, "PG-BRIDGE-MIB", "pgSessionInstance"),
)
if mibBuilder.loadTexts:
    pgDot1dBaseEntry.setStatus("mandatory")


class _PgDot1dBaseBrEnable_Type(Integer32):
    """Custom type pgDot1dBaseBrEnable based on Integer32"""
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


_PgDot1dBaseBrEnable_Type.__name__ = "Integer32"
_PgDot1dBaseBrEnable_Object = MibTableColumn
pgDot1dBaseBrEnable = _PgDot1dBaseBrEnable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 2, 1, 1, 1),
    _PgDot1dBaseBrEnable_Type()
)
pgDot1dBaseBrEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgDot1dBaseBrEnable.setStatus("mandatory")


class _PgDot1dBaseBrStpEnable_Type(Integer32):
    """Custom type pgDot1dBaseBrStpEnable based on Integer32"""
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


_PgDot1dBaseBrStpEnable_Type.__name__ = "Integer32"
_PgDot1dBaseBrStpEnable_Object = MibTableColumn
pgDot1dBaseBrStpEnable = _PgDot1dBaseBrStpEnable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 2, 1, 1, 2),
    _PgDot1dBaseBrStpEnable_Type()
)
pgDot1dBaseBrStpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgDot1dBaseBrStpEnable.setStatus("mandatory")
_PgDot1dBaseBridgeAddress_Type = MacAddress
_PgDot1dBaseBridgeAddress_Object = MibTableColumn
pgDot1dBaseBridgeAddress = _PgDot1dBaseBridgeAddress_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 2, 1, 1, 3),
    _PgDot1dBaseBridgeAddress_Type()
)
pgDot1dBaseBridgeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDot1dBaseBridgeAddress.setStatus("mandatory")
_PgDot1dBaseNumPorts_Type = Integer32
_PgDot1dBaseNumPorts_Object = MibTableColumn
pgDot1dBaseNumPorts = _PgDot1dBaseNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 2, 1, 1, 4),
    _PgDot1dBaseNumPorts_Type()
)
pgDot1dBaseNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDot1dBaseNumPorts.setStatus("mandatory")


class _PgDot1dBaseType_Type(Integer32):
    """Custom type pgDot1dBaseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("sourceroute-only", 3),
          ("srt", 4),
          ("transparent-only", 2),
          ("unknown", 1))
    )


_PgDot1dBaseType_Type.__name__ = "Integer32"
_PgDot1dBaseType_Object = MibTableColumn
pgDot1dBaseType = _PgDot1dBaseType_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 2, 1, 1, 5),
    _PgDot1dBaseType_Type()
)
pgDot1dBaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDot1dBaseType.setStatus("mandatory")
_PgDot1dTpLearnedEntryDiscards_Type = Counter32
_PgDot1dTpLearnedEntryDiscards_Object = MibTableColumn
pgDot1dTpLearnedEntryDiscards = _PgDot1dTpLearnedEntryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 2, 1, 1, 6),
    _PgDot1dTpLearnedEntryDiscards_Type()
)
pgDot1dTpLearnedEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDot1dTpLearnedEntryDiscards.setStatus("mandatory")


class _PgDot1dTpAgingTime_Type(Integer32):
    """Custom type pgDot1dTpAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_PgDot1dTpAgingTime_Type.__name__ = "Integer32"
_PgDot1dTpAgingTime_Object = MibTableColumn
pgDot1dTpAgingTime = _PgDot1dTpAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 2, 1, 1, 7),
    _PgDot1dTpAgingTime_Type()
)
pgDot1dTpAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgDot1dTpAgingTime.setStatus("mandatory")
_PgDot1dBasePort_ObjectIdentity = ObjectIdentity
pgDot1dBasePort = _PgDot1dBasePort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 3)
)
_Pgdot1dBasePortTable_Object = MibTable
pgdot1dBasePortTable = _Pgdot1dBasePortTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 3, 1)
)
if mibBuilder.loadTexts:
    pgdot1dBasePortTable.setStatus("mandatory")
_Pgdot1dBasePortEntry_Object = MibTableRow
pgdot1dBasePortEntry = _Pgdot1dBasePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 3, 1, 1)
)
pgdot1dBasePortEntry.setIndexNames(
    (0, "PG-BRIDGE-MIB", "pgSessionInstance"),
    (0, "PG-BRIDGE-MIB", "pgSessionPortBridgePort"),
)
if mibBuilder.loadTexts:
    pgdot1dBasePortEntry.setStatus("mandatory")


class _Pgdot1dBasePort_Type(Integer32):
    """Custom type pgdot1dBasePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Pgdot1dBasePort_Type.__name__ = "Integer32"
_Pgdot1dBasePort_Object = MibTableColumn
pgdot1dBasePort = _Pgdot1dBasePort_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 3, 1, 1, 1),
    _Pgdot1dBasePort_Type()
)
pgdot1dBasePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgdot1dBasePort.setStatus("mandatory")
_Pgdot1dBasePortIfIndex_Type = Integer32
_Pgdot1dBasePortIfIndex_Object = MibTableColumn
pgdot1dBasePortIfIndex = _Pgdot1dBasePortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 3, 1, 1, 2),
    _Pgdot1dBasePortIfIndex_Type()
)
pgdot1dBasePortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgdot1dBasePortIfIndex.setStatus("mandatory")
_Pgdot1dBasePortCircuit_Type = ObjectIdentifier
_Pgdot1dBasePortCircuit_Object = MibTableColumn
pgdot1dBasePortCircuit = _Pgdot1dBasePortCircuit_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 3, 1, 1, 3),
    _Pgdot1dBasePortCircuit_Type()
)
pgdot1dBasePortCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgdot1dBasePortCircuit.setStatus("mandatory")
_Pgdot1dBasePortDelayExceededDiscards_Type = Counter32
_Pgdot1dBasePortDelayExceededDiscards_Object = MibTableColumn
pgdot1dBasePortDelayExceededDiscards = _Pgdot1dBasePortDelayExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 3, 1, 1, 4),
    _Pgdot1dBasePortDelayExceededDiscards_Type()
)
pgdot1dBasePortDelayExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgdot1dBasePortDelayExceededDiscards.setStatus("mandatory")
_Pgdot1dBasePortMtuExceededDiscards_Type = Counter32
_Pgdot1dBasePortMtuExceededDiscards_Object = MibTableColumn
pgdot1dBasePortMtuExceededDiscards = _Pgdot1dBasePortMtuExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 3, 1, 1, 5),
    _Pgdot1dBasePortMtuExceededDiscards_Type()
)
pgdot1dBasePortMtuExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgdot1dBasePortMtuExceededDiscards.setStatus("mandatory")
_PgDot1dStpPort_ObjectIdentity = ObjectIdentity
pgDot1dStpPort = _PgDot1dStpPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 4)
)
_Pgdot1dStpPortTable_Object = MibTable
pgdot1dStpPortTable = _Pgdot1dStpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 4, 1)
)
if mibBuilder.loadTexts:
    pgdot1dStpPortTable.setStatus("mandatory")
_Pgdot1dStpPortEntry_Object = MibTableRow
pgdot1dStpPortEntry = _Pgdot1dStpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 4, 1, 1)
)
pgdot1dStpPortEntry.setIndexNames(
    (0, "PG-BRIDGE-MIB", "pgSessionInstance"),
    (0, "PG-BRIDGE-MIB", "pgSessionPortBridgePort"),
)
if mibBuilder.loadTexts:
    pgdot1dStpPortEntry.setStatus("mandatory")


class _Pgdot1dStpPort_Type(Integer32):
    """Custom type pgdot1dStpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Pgdot1dStpPort_Type.__name__ = "Integer32"
_Pgdot1dStpPort_Object = MibTableColumn
pgdot1dStpPort = _Pgdot1dStpPort_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 4, 1, 1, 1),
    _Pgdot1dStpPort_Type()
)
pgdot1dStpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgdot1dStpPort.setStatus("mandatory")


class _Pgdot1dStpPortPriority_Type(Integer32):
    """Custom type pgdot1dStpPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Pgdot1dStpPortPriority_Type.__name__ = "Integer32"
_Pgdot1dStpPortPriority_Object = MibTableColumn
pgdot1dStpPortPriority = _Pgdot1dStpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 4, 1, 1, 2),
    _Pgdot1dStpPortPriority_Type()
)
pgdot1dStpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgdot1dStpPortPriority.setStatus("mandatory")


class _Pgdot1dStpPortState_Type(Integer32):
    """Custom type pgdot1dStpPortState based on Integer32"""
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
        *(("blocking", 2),
          ("broken", 6),
          ("disabled", 1),
          ("forwarding", 5),
          ("learning", 4),
          ("listening", 3))
    )


_Pgdot1dStpPortState_Type.__name__ = "Integer32"
_Pgdot1dStpPortState_Object = MibTableColumn
pgdot1dStpPortState = _Pgdot1dStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 4, 1, 1, 3),
    _Pgdot1dStpPortState_Type()
)
pgdot1dStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgdot1dStpPortState.setStatus("mandatory")


class _Pgdot1dStpPortEnable_Type(Integer32):
    """Custom type pgdot1dStpPortEnable based on Integer32"""
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


_Pgdot1dStpPortEnable_Type.__name__ = "Integer32"
_Pgdot1dStpPortEnable_Object = MibTableColumn
pgdot1dStpPortEnable = _Pgdot1dStpPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 4, 1, 1, 4),
    _Pgdot1dStpPortEnable_Type()
)
pgdot1dStpPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgdot1dStpPortEnable.setStatus("mandatory")


class _Pgdot1dStpPortPathCost_Type(Integer32):
    """Custom type pgdot1dStpPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Pgdot1dStpPortPathCost_Type.__name__ = "Integer32"
_Pgdot1dStpPortPathCost_Object = MibTableColumn
pgdot1dStpPortPathCost = _Pgdot1dStpPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 4, 1, 1, 5),
    _Pgdot1dStpPortPathCost_Type()
)
pgdot1dStpPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgdot1dStpPortPathCost.setStatus("mandatory")
_Pgdot1dStpPortDesignatedRoot_Type = BridgeId
_Pgdot1dStpPortDesignatedRoot_Object = MibTableColumn
pgdot1dStpPortDesignatedRoot = _Pgdot1dStpPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 4, 1, 1, 6),
    _Pgdot1dStpPortDesignatedRoot_Type()
)
pgdot1dStpPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgdot1dStpPortDesignatedRoot.setStatus("mandatory")
_Pgdot1dStpPortDesignatedCost_Type = Integer32
_Pgdot1dStpPortDesignatedCost_Object = MibTableColumn
pgdot1dStpPortDesignatedCost = _Pgdot1dStpPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 4, 1, 1, 7),
    _Pgdot1dStpPortDesignatedCost_Type()
)
pgdot1dStpPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgdot1dStpPortDesignatedCost.setStatus("mandatory")
_Pgdot1dStpPortDesignatedBridge_Type = BridgeId
_Pgdot1dStpPortDesignatedBridge_Object = MibTableColumn
pgdot1dStpPortDesignatedBridge = _Pgdot1dStpPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 4, 1, 1, 8),
    _Pgdot1dStpPortDesignatedBridge_Type()
)
pgdot1dStpPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgdot1dStpPortDesignatedBridge.setStatus("mandatory")


class _Pgdot1dStpPortDesignatedPort_Type(OctetString):
    """Custom type pgdot1dStpPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Pgdot1dStpPortDesignatedPort_Type.__name__ = "OctetString"
_Pgdot1dStpPortDesignatedPort_Object = MibTableColumn
pgdot1dStpPortDesignatedPort = _Pgdot1dStpPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 4, 1, 1, 9),
    _Pgdot1dStpPortDesignatedPort_Type()
)
pgdot1dStpPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgdot1dStpPortDesignatedPort.setStatus("mandatory")
_Pgdot1dStpPortForwardTransitions_Type = Counter32
_Pgdot1dStpPortForwardTransitions_Object = MibTableColumn
pgdot1dStpPortForwardTransitions = _Pgdot1dStpPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 4, 1, 1, 10),
    _Pgdot1dStpPortForwardTransitions_Type()
)
pgdot1dStpPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgdot1dStpPortForwardTransitions.setStatus("mandatory")
_Pgdot1dStpPortRowStatus_Type = RowStatus
_Pgdot1dStpPortRowStatus_Object = MibTableColumn
pgdot1dStpPortRowStatus = _Pgdot1dStpPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 4, 1, 1, 11),
    _Pgdot1dStpPortRowStatus_Type()
)
pgdot1dStpPortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgdot1dStpPortRowStatus.setStatus("mandatory")
_PgDot1dTp_ObjectIdentity = ObjectIdentity
pgDot1dTp = _PgDot1dTp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 5)
)
_PgDot1dTpFdbTable_Object = MibTable
pgDot1dTpFdbTable = _PgDot1dTpFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 5, 1)
)
if mibBuilder.loadTexts:
    pgDot1dTpFdbTable.setStatus("mandatory")
_PgDot1dTpFdbEntry_Object = MibTableRow
pgDot1dTpFdbEntry = _PgDot1dTpFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 5, 1, 1)
)
pgDot1dTpFdbEntry.setIndexNames(
    (0, "PG-BRIDGE-MIB", "pgSessionInstance"),
    (0, "PG-BRIDGE-MIB", "pgDot1dTpFdbAddress"),
)
if mibBuilder.loadTexts:
    pgDot1dTpFdbEntry.setStatus("mandatory")
_PgDot1dTpFdbAddress_Type = MacAddress
_PgDot1dTpFdbAddress_Object = MibTableColumn
pgDot1dTpFdbAddress = _PgDot1dTpFdbAddress_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 5, 1, 1, 1),
    _PgDot1dTpFdbAddress_Type()
)
pgDot1dTpFdbAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDot1dTpFdbAddress.setStatus("mandatory")
_PgDot1dTpFdbPort_Type = Integer32
_PgDot1dTpFdbPort_Object = MibTableColumn
pgDot1dTpFdbPort = _PgDot1dTpFdbPort_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 5, 1, 1, 2),
    _PgDot1dTpFdbPort_Type()
)
pgDot1dTpFdbPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDot1dTpFdbPort.setStatus("mandatory")


class _PgDot1dTpFdbStatus_Type(Integer32):
    """Custom type pgDot1dTpFdbStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("learned", 3),
          ("mgmt", 5),
          ("other", 1),
          ("self", 4))
    )


_PgDot1dTpFdbStatus_Type.__name__ = "Integer32"
_PgDot1dTpFdbStatus_Object = MibTableColumn
pgDot1dTpFdbStatus = _PgDot1dTpFdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 5, 1, 1, 3),
    _PgDot1dTpFdbStatus_Type()
)
pgDot1dTpFdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDot1dTpFdbStatus.setStatus("mandatory")
_PgDot1dTpPortTable_Object = MibTable
pgDot1dTpPortTable = _PgDot1dTpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 5, 2)
)
if mibBuilder.loadTexts:
    pgDot1dTpPortTable.setStatus("mandatory")
_PgDot1dTpPortEntry_Object = MibTableRow
pgDot1dTpPortEntry = _PgDot1dTpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 5, 2, 1)
)
pgDot1dTpPortEntry.setIndexNames(
    (0, "PG-BRIDGE-MIB", "pgSessionInstance"),
    (0, "PG-BRIDGE-MIB", "pgDot1dTpPort"),
)
if mibBuilder.loadTexts:
    pgDot1dTpPortEntry.setStatus("mandatory")


class _PgDot1dTpPort_Type(Integer32):
    """Custom type pgDot1dTpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PgDot1dTpPort_Type.__name__ = "Integer32"
_PgDot1dTpPort_Object = MibTableColumn
pgDot1dTpPort = _PgDot1dTpPort_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 5, 2, 1, 1),
    _PgDot1dTpPort_Type()
)
pgDot1dTpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDot1dTpPort.setStatus("mandatory")
_PgDot1dTpPortMaxInfo_Type = Integer32
_PgDot1dTpPortMaxInfo_Object = MibTableColumn
pgDot1dTpPortMaxInfo = _PgDot1dTpPortMaxInfo_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 5, 2, 1, 2),
    _PgDot1dTpPortMaxInfo_Type()
)
pgDot1dTpPortMaxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDot1dTpPortMaxInfo.setStatus("mandatory")
_PgDot1dTpPortInFrames_Type = Counter32
_PgDot1dTpPortInFrames_Object = MibTableColumn
pgDot1dTpPortInFrames = _PgDot1dTpPortInFrames_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 5, 2, 1, 3),
    _PgDot1dTpPortInFrames_Type()
)
pgDot1dTpPortInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDot1dTpPortInFrames.setStatus("mandatory")
_PgDot1dTpPortOutFrames_Type = Counter32
_PgDot1dTpPortOutFrames_Object = MibTableColumn
pgDot1dTpPortOutFrames = _PgDot1dTpPortOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 5, 2, 1, 4),
    _PgDot1dTpPortOutFrames_Type()
)
pgDot1dTpPortOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDot1dTpPortOutFrames.setStatus("mandatory")
_PgDot1dTpPortInDiscards_Type = Counter32
_PgDot1dTpPortInDiscards_Object = MibTableColumn
pgDot1dTpPortInDiscards = _PgDot1dTpPortInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 5, 2, 1, 5),
    _PgDot1dTpPortInDiscards_Type()
)
pgDot1dTpPortInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDot1dTpPortInDiscards.setStatus("mandatory")
_PgDot1dStatic_ObjectIdentity = ObjectIdentity
pgDot1dStatic = _PgDot1dStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 6)
)
_PgDot1dStaticTable_Object = MibTable
pgDot1dStaticTable = _PgDot1dStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 6, 1)
)
if mibBuilder.loadTexts:
    pgDot1dStaticTable.setStatus("mandatory")
_PgDot1dStaticEntry_Object = MibTableRow
pgDot1dStaticEntry = _PgDot1dStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 6, 1, 1)
)
pgDot1dStaticEntry.setIndexNames(
    (0, "PG-BRIDGE-MIB", "pgSessionInstance"),
    (0, "PG-BRIDGE-MIB", "pgDot1dStaticAddress"),
    (0, "PG-BRIDGE-MIB", "pgDot1dStaticReceivePort"),
)
if mibBuilder.loadTexts:
    pgDot1dStaticEntry.setStatus("mandatory")
_PgDot1dStaticAddress_Type = MacAddress
_PgDot1dStaticAddress_Object = MibTableColumn
pgDot1dStaticAddress = _PgDot1dStaticAddress_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 6, 1, 1, 1),
    _PgDot1dStaticAddress_Type()
)
pgDot1dStaticAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgDot1dStaticAddress.setStatus("mandatory")
_PgDot1dStaticReceivePort_Type = Integer32
_PgDot1dStaticReceivePort_Object = MibTableColumn
pgDot1dStaticReceivePort = _PgDot1dStaticReceivePort_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 6, 1, 1, 2),
    _PgDot1dStaticReceivePort_Type()
)
pgDot1dStaticReceivePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgDot1dStaticReceivePort.setStatus("mandatory")
_PgDot1dStaticAllowedToGoTo_Type = OctetString
_PgDot1dStaticAllowedToGoTo_Object = MibTableColumn
pgDot1dStaticAllowedToGoTo = _PgDot1dStaticAllowedToGoTo_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 6, 1, 1, 3),
    _PgDot1dStaticAllowedToGoTo_Type()
)
pgDot1dStaticAllowedToGoTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgDot1dStaticAllowedToGoTo.setStatus("mandatory")


class _PgDot1dStaticStatus_Type(Integer32):
    """Custom type pgDot1dStaticStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("deleteOnReset", 4),
          ("deleteOnTimeout", 5),
          ("invalid", 2),
          ("other", 1),
          ("permanent", 3))
    )


_PgDot1dStaticStatus_Type.__name__ = "Integer32"
_PgDot1dStaticStatus_Object = MibTableColumn
pgDot1dStaticStatus = _PgDot1dStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 6, 1, 1, 4),
    _PgDot1dStaticStatus_Type()
)
pgDot1dStaticStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgDot1dStaticStatus.setStatus("mandatory")
_PgVlanGroup_ObjectIdentity = ObjectIdentity
pgVlanGroup = _PgVlanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 7)
)
_PgVlanGroupTable_Object = MibTable
pgVlanGroupTable = _PgVlanGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 7, 1)
)
if mibBuilder.loadTexts:
    pgVlanGroupTable.setStatus("mandatory")
_PgVlanGroupEntry_Object = MibTableRow
pgVlanGroupEntry = _PgVlanGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 7, 1, 1)
)
pgVlanGroupEntry.setIndexNames(
    (0, "PG-BRIDGE-MIB", "pgSessionInstance"),
    (0, "PG-BRIDGE-MIB", "pgBrVlanGroupIdentifier"),
)
if mibBuilder.loadTexts:
    pgVlanGroupEntry.setStatus("mandatory")
_PgBrVlanGroupIdentifier_Type = Integer32
_PgBrVlanGroupIdentifier_Object = MibTableColumn
pgBrVlanGroupIdentifier = _PgBrVlanGroupIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 7, 1, 1, 1),
    _PgBrVlanGroupIdentifier_Type()
)
pgBrVlanGroupIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgBrVlanGroupIdentifier.setStatus("mandatory")


class _PgBrVlanGroupWanBcEnable_Type(Integer32):
    """Custom type pgBrVlanGroupWanBcEnable based on Integer32"""
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


_PgBrVlanGroupWanBcEnable_Type.__name__ = "Integer32"
_PgBrVlanGroupWanBcEnable_Object = MibTableColumn
pgBrVlanGroupWanBcEnable = _PgBrVlanGroupWanBcEnable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 7, 1, 1, 2),
    _PgBrVlanGroupWanBcEnable_Type()
)
pgBrVlanGroupWanBcEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgBrVlanGroupWanBcEnable.setStatus("mandatory")


class _PgBrVlanGroupName_Type(OctetString):
    """Custom type pgBrVlanGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_PgBrVlanGroupName_Type.__name__ = "OctetString"
_PgBrVlanGroupName_Object = MibTableColumn
pgBrVlanGroupName = _PgBrVlanGroupName_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 7, 1, 1, 3),
    _PgBrVlanGroupName_Type()
)
pgBrVlanGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgBrVlanGroupName.setStatus("mandatory")


class _PgBrVlanGroupMode_Type(Integer32):
    """Custom type pgBrVlanGroupMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("close", 2),
          ("open", 1))
    )


_PgBrVlanGroupMode_Type.__name__ = "Integer32"
_PgBrVlanGroupMode_Object = MibTableColumn
pgBrVlanGroupMode = _PgBrVlanGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 7, 1, 1, 4),
    _PgBrVlanGroupMode_Type()
)
pgBrVlanGroupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgBrVlanGroupMode.setStatus("mandatory")


class _PgBrVlanGroupTag_Type(Integer32):
    """Custom type pgBrVlanGroupTag based on Integer32"""
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


_PgBrVlanGroupTag_Type.__name__ = "Integer32"
_PgBrVlanGroupTag_Object = MibTableColumn
pgBrVlanGroupTag = _PgBrVlanGroupTag_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 7, 1, 1, 5),
    _PgBrVlanGroupTag_Type()
)
pgBrVlanGroupTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgBrVlanGroupTag.setStatus("mandatory")


class _PgBrVlanGroupStpEnable_Type(Integer32):
    """Custom type pgBrVlanGroupStpEnable based on Integer32"""
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


_PgBrVlanGroupStpEnable_Type.__name__ = "Integer32"
_PgBrVlanGroupStpEnable_Object = MibTableColumn
pgBrVlanGroupStpEnable = _PgBrVlanGroupStpEnable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 7, 1, 1, 6),
    _PgBrVlanGroupStpEnable_Type()
)
pgBrVlanGroupStpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgBrVlanGroupStpEnable.setStatus("mandatory")


class _PgBrVlanGroupStpProtocolSpecification_Type(Integer32):
    """Custom type pgBrVlanGroupStpProtocolSpecification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("decLb100", 2),
          ("ieee8021d", 3),
          ("unknown", 1))
    )


_PgBrVlanGroupStpProtocolSpecification_Type.__name__ = "Integer32"
_PgBrVlanGroupStpProtocolSpecification_Object = MibTableColumn
pgBrVlanGroupStpProtocolSpecification = _PgBrVlanGroupStpProtocolSpecification_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 7, 1, 1, 7),
    _PgBrVlanGroupStpProtocolSpecification_Type()
)
pgBrVlanGroupStpProtocolSpecification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgBrVlanGroupStpProtocolSpecification.setStatus("mandatory")


class _PgBrVlanGroupStpPriority_Type(Integer32):
    """Custom type pgBrVlanGroupStpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PgBrVlanGroupStpPriority_Type.__name__ = "Integer32"
_PgBrVlanGroupStpPriority_Object = MibTableColumn
pgBrVlanGroupStpPriority = _PgBrVlanGroupStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 7, 1, 1, 8),
    _PgBrVlanGroupStpPriority_Type()
)
pgBrVlanGroupStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgBrVlanGroupStpPriority.setStatus("mandatory")
_PgBrVlanGroupStpTimeSinceTopologyChange_Type = TimeTicks
_PgBrVlanGroupStpTimeSinceTopologyChange_Object = MibTableColumn
pgBrVlanGroupStpTimeSinceTopologyChange = _PgBrVlanGroupStpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 7, 1, 1, 9),
    _PgBrVlanGroupStpTimeSinceTopologyChange_Type()
)
pgBrVlanGroupStpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgBrVlanGroupStpTimeSinceTopologyChange.setStatus("mandatory")
_PgBrVlanGroupStpTopChanges_Type = Counter32
_PgBrVlanGroupStpTopChanges_Object = MibTableColumn
pgBrVlanGroupStpTopChanges = _PgBrVlanGroupStpTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 7, 1, 1, 10),
    _PgBrVlanGroupStpTopChanges_Type()
)
pgBrVlanGroupStpTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgBrVlanGroupStpTopChanges.setStatus("mandatory")
_PgBrVlanGroupStpDesignatedRoot_Type = BridgeId
_PgBrVlanGroupStpDesignatedRoot_Object = MibTableColumn
pgBrVlanGroupStpDesignatedRoot = _PgBrVlanGroupStpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 7, 1, 1, 11),
    _PgBrVlanGroupStpDesignatedRoot_Type()
)
pgBrVlanGroupStpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgBrVlanGroupStpDesignatedRoot.setStatus("mandatory")
_PgBrVlanGroupStpRootCost_Type = Integer32
_PgBrVlanGroupStpRootCost_Object = MibTableColumn
pgBrVlanGroupStpRootCost = _PgBrVlanGroupStpRootCost_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 7, 1, 1, 12),
    _PgBrVlanGroupStpRootCost_Type()
)
pgBrVlanGroupStpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgBrVlanGroupStpRootCost.setStatus("mandatory")
_PgBrVlanGroupStpRootPort_Type = Integer32
_PgBrVlanGroupStpRootPort_Object = MibTableColumn
pgBrVlanGroupStpRootPort = _PgBrVlanGroupStpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 7, 1, 1, 13),
    _PgBrVlanGroupStpRootPort_Type()
)
pgBrVlanGroupStpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgBrVlanGroupStpRootPort.setStatus("mandatory")
_PgBrVlanGroupStpMaxAge_Type = Timeout
_PgBrVlanGroupStpMaxAge_Object = MibTableColumn
pgBrVlanGroupStpMaxAge = _PgBrVlanGroupStpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 7, 1, 1, 14),
    _PgBrVlanGroupStpMaxAge_Type()
)
pgBrVlanGroupStpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgBrVlanGroupStpMaxAge.setStatus("mandatory")
_PgBrVlanGroupStpHelloTime_Type = Timeout
_PgBrVlanGroupStpHelloTime_Object = MibTableColumn
pgBrVlanGroupStpHelloTime = _PgBrVlanGroupStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 7, 1, 1, 15),
    _PgBrVlanGroupStpHelloTime_Type()
)
pgBrVlanGroupStpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgBrVlanGroupStpHelloTime.setStatus("mandatory")
_PgBrVlanGroupStpHoldTime_Type = Integer32
_PgBrVlanGroupStpHoldTime_Object = MibTableColumn
pgBrVlanGroupStpHoldTime = _PgBrVlanGroupStpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 7, 1, 1, 16),
    _PgBrVlanGroupStpHoldTime_Type()
)
pgBrVlanGroupStpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgBrVlanGroupStpHoldTime.setStatus("mandatory")
_PgBrVlanGroupStpForwardDelay_Type = Timeout
_PgBrVlanGroupStpForwardDelay_Object = MibTableColumn
pgBrVlanGroupStpForwardDelay = _PgBrVlanGroupStpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 7, 1, 1, 17),
    _PgBrVlanGroupStpForwardDelay_Type()
)
pgBrVlanGroupStpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgBrVlanGroupStpForwardDelay.setStatus("mandatory")


class _PgBrVlanGroupStpBridgeMaxAge_Type(Timeout):
    """Custom type pgBrVlanGroupStpBridgeMaxAge based on Timeout"""
    defaultValue = 2000

    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_PgBrVlanGroupStpBridgeMaxAge_Type.__name__ = "Timeout"
_PgBrVlanGroupStpBridgeMaxAge_Object = MibTableColumn
pgBrVlanGroupStpBridgeMaxAge = _PgBrVlanGroupStpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 7, 1, 1, 18),
    _PgBrVlanGroupStpBridgeMaxAge_Type()
)
pgBrVlanGroupStpBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgBrVlanGroupStpBridgeMaxAge.setStatus("mandatory")


class _PgBrVlanGroupStpBridgeHelloTime_Type(Timeout):
    """Custom type pgBrVlanGroupStpBridgeHelloTime based on Timeout"""
    defaultValue = 200

    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_PgBrVlanGroupStpBridgeHelloTime_Type.__name__ = "Timeout"
_PgBrVlanGroupStpBridgeHelloTime_Object = MibTableColumn
pgBrVlanGroupStpBridgeHelloTime = _PgBrVlanGroupStpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 7, 1, 1, 19),
    _PgBrVlanGroupStpBridgeHelloTime_Type()
)
pgBrVlanGroupStpBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgBrVlanGroupStpBridgeHelloTime.setStatus("mandatory")


class _PgBrVlanGroupStpBridgeForwardDelay_Type(Timeout):
    """Custom type pgBrVlanGroupStpBridgeForwardDelay based on Timeout"""
    defaultValue = 1500

    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_PgBrVlanGroupStpBridgeForwardDelay_Type.__name__ = "Timeout"
_PgBrVlanGroupStpBridgeForwardDelay_Object = MibTableColumn
pgBrVlanGroupStpBridgeForwardDelay = _PgBrVlanGroupStpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 7, 1, 1, 20),
    _PgBrVlanGroupStpBridgeForwardDelay_Type()
)
pgBrVlanGroupStpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgBrVlanGroupStpBridgeForwardDelay.setStatus("mandatory")
_PgBrVlanGroupRowStatus_Type = RowStatus
_PgBrVlanGroupRowStatus_Object = MibTableColumn
pgBrVlanGroupRowStatus = _PgBrVlanGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 7, 1, 1, 21),
    _PgBrVlanGroupRowStatus_Type()
)
pgBrVlanGroupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgBrVlanGroupRowStatus.setStatus("mandatory")
_PgSessionRouterGroup_ObjectIdentity = ObjectIdentity
pgSessionRouterGroup = _PgSessionRouterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 8)
)
_PgSessionRouterGroupTable_Object = MibTable
pgSessionRouterGroupTable = _PgSessionRouterGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 8, 1)
)
if mibBuilder.loadTexts:
    pgSessionRouterGroupTable.setStatus("mandatory")
_PgSessionRouterGroupEntry_Object = MibTableRow
pgSessionRouterGroupEntry = _PgSessionRouterGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 8, 1, 1)
)
pgSessionRouterGroupEntry.setIndexNames(
    (0, "PG-BRIDGE-MIB", "pgSessionInstance"),
    (0, "PG-BRIDGE-MIB", "pgSessionPortRouterGroupInterface"),
)
if mibBuilder.loadTexts:
    pgSessionRouterGroupEntry.setStatus("mandatory")
_PgSessionGroupIpAddress_Type = IpAddress
_PgSessionGroupIpAddress_Object = MibTableColumn
pgSessionGroupIpAddress = _PgSessionGroupIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 8, 1, 1, 1),
    _PgSessionGroupIpAddress_Type()
)
pgSessionGroupIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgSessionGroupIpAddress.setStatus("mandatory")
_PgSessionGroupSubnetMask_Type = IpAddress
_PgSessionGroupSubnetMask_Object = MibTableColumn
pgSessionGroupSubnetMask = _PgSessionGroupSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 8, 1, 1, 2),
    _PgSessionGroupSubnetMask_Type()
)
pgSessionGroupSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgSessionGroupSubnetMask.setStatus("mandatory")
_PgSessionGroupRowStatus_Type = RowStatus
_PgSessionGroupRowStatus_Object = MibTableColumn
pgSessionGroupRowStatus = _PgSessionGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 8, 1, 1, 3),
    _PgSessionGroupRowStatus_Type()
)
pgSessionGroupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgSessionGroupRowStatus.setStatus("mandatory")
_PgIfindexToSlotPortMap_ObjectIdentity = ObjectIdentity
pgIfindexToSlotPortMap = _PgIfindexToSlotPortMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 9)
)
_PgIfindexToSlotPortMapTable_Object = MibTable
pgIfindexToSlotPortMapTable = _PgIfindexToSlotPortMapTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 9, 1)
)
if mibBuilder.loadTexts:
    pgIfindexToSlotPortMapTable.setStatus("mandatory")
_PgIfindexToSlotPortMapEntry_Object = MibTableRow
pgIfindexToSlotPortMapEntry = _PgIfindexToSlotPortMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 9, 1, 1)
)
pgIfindexToSlotPortMapEntry.setIndexNames(
    (0, "PG-BRIDGE-MIB", "pgSessionInstance"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pgIfindexToSlotPortMapEntry.setStatus("mandatory")
_PgIfindexToSlotPortMapSlot_Type = Integer32
_PgIfindexToSlotPortMapSlot_Object = MibTableColumn
pgIfindexToSlotPortMapSlot = _PgIfindexToSlotPortMapSlot_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 9, 1, 1, 1),
    _PgIfindexToSlotPortMapSlot_Type()
)
pgIfindexToSlotPortMapSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgIfindexToSlotPortMapSlot.setStatus("mandatory")
_PgIfindexToSlotPortMapPort_Type = Integer32
_PgIfindexToSlotPortMapPort_Object = MibTableColumn
pgIfindexToSlotPortMapPort = _PgIfindexToSlotPortMapPort_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 9, 1, 1, 2),
    _PgIfindexToSlotPortMapPort_Type()
)
pgIfindexToSlotPortMapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgIfindexToSlotPortMapPort.setStatus("mandatory")
_PgIfindexToSlotPortMapIntVpi_Type = Integer32
_PgIfindexToSlotPortMapIntVpi_Object = MibTableColumn
pgIfindexToSlotPortMapIntVpi = _PgIfindexToSlotPortMapIntVpi_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 9, 1, 1, 3),
    _PgIfindexToSlotPortMapIntVpi_Type()
)
pgIfindexToSlotPortMapIntVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgIfindexToSlotPortMapIntVpi.setStatus("mandatory")
_PgIfindexToSlotPortMapIntVci_Type = Integer32
_PgIfindexToSlotPortMapIntVci_Object = MibTableColumn
pgIfindexToSlotPortMapIntVci = _PgIfindexToSlotPortMapIntVci_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 9, 1, 1, 4),
    _PgIfindexToSlotPortMapIntVci_Type()
)
pgIfindexToSlotPortMapIntVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgIfindexToSlotPortMapIntVci.setStatus("mandatory")
_PgIfindexToSlotPortMapExtVpi_Type = Integer32
_PgIfindexToSlotPortMapExtVpi_Object = MibTableColumn
pgIfindexToSlotPortMapExtVpi = _PgIfindexToSlotPortMapExtVpi_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 9, 1, 1, 5),
    _PgIfindexToSlotPortMapExtVpi_Type()
)
pgIfindexToSlotPortMapExtVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgIfindexToSlotPortMapExtVpi.setStatus("mandatory")
_PgIfindexToSlotPortMapExtVci_Type = Integer32
_PgIfindexToSlotPortMapExtVci_Object = MibTableColumn
pgIfindexToSlotPortMapExtVci = _PgIfindexToSlotPortMapExtVci_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 9, 1, 1, 6),
    _PgIfindexToSlotPortMapExtVci_Type()
)
pgIfindexToSlotPortMapExtVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgIfindexToSlotPortMapExtVci.setStatus("mandatory")
_PgBridgePortToSlotPortMap_ObjectIdentity = ObjectIdentity
pgBridgePortToSlotPortMap = _PgBridgePortToSlotPortMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 10)
)
_PgBridgePortToSlotPortMapTable_Object = MibTable
pgBridgePortToSlotPortMapTable = _PgBridgePortToSlotPortMapTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 10, 1)
)
if mibBuilder.loadTexts:
    pgBridgePortToSlotPortMapTable.setStatus("mandatory")
_PgBridgePortToSlotPortMapEntry_Object = MibTableRow
pgBridgePortToSlotPortMapEntry = _PgBridgePortToSlotPortMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 10, 1, 1)
)
pgBridgePortToSlotPortMapEntry.setIndexNames(
    (0, "PG-BRIDGE-MIB", "pgSessionInstance"),
    (0, "PG-BRIDGE-MIB", "pgSessionPortBridgePort"),
)
if mibBuilder.loadTexts:
    pgBridgePortToSlotPortMapEntry.setStatus("mandatory")
_PgBridgePortToSlotPortMapSlot_Type = Integer32
_PgBridgePortToSlotPortMapSlot_Object = MibTableColumn
pgBridgePortToSlotPortMapSlot = _PgBridgePortToSlotPortMapSlot_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 10, 1, 1, 1),
    _PgBridgePortToSlotPortMapSlot_Type()
)
pgBridgePortToSlotPortMapSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgBridgePortToSlotPortMapSlot.setStatus("mandatory")
_PgBridgePortToSlotPortMapPort_Type = Integer32
_PgBridgePortToSlotPortMapPort_Object = MibTableColumn
pgBridgePortToSlotPortMapPort = _PgBridgePortToSlotPortMapPort_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 10, 1, 1, 2),
    _PgBridgePortToSlotPortMapPort_Type()
)
pgBridgePortToSlotPortMapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgBridgePortToSlotPortMapPort.setStatus("mandatory")
_PgBridgePortToSlotPortMapIntVpi_Type = Integer32
_PgBridgePortToSlotPortMapIntVpi_Object = MibTableColumn
pgBridgePortToSlotPortMapIntVpi = _PgBridgePortToSlotPortMapIntVpi_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 10, 1, 1, 3),
    _PgBridgePortToSlotPortMapIntVpi_Type()
)
pgBridgePortToSlotPortMapIntVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgBridgePortToSlotPortMapIntVpi.setStatus("mandatory")
_PgBridgePortToSlotPortMapIntVci_Type = Integer32
_PgBridgePortToSlotPortMapIntVci_Object = MibTableColumn
pgBridgePortToSlotPortMapIntVci = _PgBridgePortToSlotPortMapIntVci_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 10, 1, 1, 4),
    _PgBridgePortToSlotPortMapIntVci_Type()
)
pgBridgePortToSlotPortMapIntVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgBridgePortToSlotPortMapIntVci.setStatus("mandatory")
_PgBridgePortToSlotPortMapExtVpi_Type = Integer32
_PgBridgePortToSlotPortMapExtVpi_Object = MibTableColumn
pgBridgePortToSlotPortMapExtVpi = _PgBridgePortToSlotPortMapExtVpi_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 10, 1, 1, 5),
    _PgBridgePortToSlotPortMapExtVpi_Type()
)
pgBridgePortToSlotPortMapExtVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgBridgePortToSlotPortMapExtVpi.setStatus("mandatory")
_PgBridgePortToSlotPortMapExtVci_Type = Integer32
_PgBridgePortToSlotPortMapExtVci_Object = MibTableColumn
pgBridgePortToSlotPortMapExtVci = _PgBridgePortToSlotPortMapExtVci_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 8, 10, 1, 1, 6),
    _PgBridgePortToSlotPortMapExtVci_Type()
)
pgBridgePortToSlotPortMapExtVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgBridgePortToSlotPortMapExtVci.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PG-BRIDGE-MIB",
    **{"BridgeId": BridgeId,
       "Timeout": Timeout,
       "pgsessionMIB": pgsessionMIB,
       "pgSessionPort": pgSessionPort,
       "pgSessionPortTable": pgSessionPortTable,
       "pgSessionPortEntry": pgSessionPortEntry,
       "pgSessionInstance": pgSessionInstance,
       "pgSessionPortVpi": pgSessionPortVpi,
       "pgSessionPortVci": pgSessionPortVci,
       "pgSessionPortSlotNum": pgSessionPortSlotNum,
       "pgSessionPortNum": pgSessionPortNum,
       "pgSessionPortIfIndex": pgSessionPortIfIndex,
       "pgSessionPortBridgePort": pgSessionPortBridgePort,
       "pgSessionPortRouterGroupInterface": pgSessionPortRouterGroupInterface,
       "pgSessionPortVlanIdentifier": pgSessionPortVlanIdentifier,
       "pgSessionPortServiceType": pgSessionPortServiceType,
       "pgSessionPortSubscriberName": pgSessionPortSubscriberName,
       "pgSessionPortRowStatus": pgSessionPortRowStatus,
       "pgDot1dBase": pgDot1dBase,
       "pgDot1dBaseTable": pgDot1dBaseTable,
       "pgDot1dBaseEntry": pgDot1dBaseEntry,
       "pgDot1dBaseBrEnable": pgDot1dBaseBrEnable,
       "pgDot1dBaseBrStpEnable": pgDot1dBaseBrStpEnable,
       "pgDot1dBaseBridgeAddress": pgDot1dBaseBridgeAddress,
       "pgDot1dBaseNumPorts": pgDot1dBaseNumPorts,
       "pgDot1dBaseType": pgDot1dBaseType,
       "pgDot1dTpLearnedEntryDiscards": pgDot1dTpLearnedEntryDiscards,
       "pgDot1dTpAgingTime": pgDot1dTpAgingTime,
       "pgDot1dBasePort": pgDot1dBasePort,
       "pgdot1dBasePortTable": pgdot1dBasePortTable,
       "pgdot1dBasePortEntry": pgdot1dBasePortEntry,
       "pgdot1dBasePort": pgdot1dBasePort,
       "pgdot1dBasePortIfIndex": pgdot1dBasePortIfIndex,
       "pgdot1dBasePortCircuit": pgdot1dBasePortCircuit,
       "pgdot1dBasePortDelayExceededDiscards": pgdot1dBasePortDelayExceededDiscards,
       "pgdot1dBasePortMtuExceededDiscards": pgdot1dBasePortMtuExceededDiscards,
       "pgDot1dStpPort": pgDot1dStpPort,
       "pgdot1dStpPortTable": pgdot1dStpPortTable,
       "pgdot1dStpPortEntry": pgdot1dStpPortEntry,
       "pgdot1dStpPort": pgdot1dStpPort,
       "pgdot1dStpPortPriority": pgdot1dStpPortPriority,
       "pgdot1dStpPortState": pgdot1dStpPortState,
       "pgdot1dStpPortEnable": pgdot1dStpPortEnable,
       "pgdot1dStpPortPathCost": pgdot1dStpPortPathCost,
       "pgdot1dStpPortDesignatedRoot": pgdot1dStpPortDesignatedRoot,
       "pgdot1dStpPortDesignatedCost": pgdot1dStpPortDesignatedCost,
       "pgdot1dStpPortDesignatedBridge": pgdot1dStpPortDesignatedBridge,
       "pgdot1dStpPortDesignatedPort": pgdot1dStpPortDesignatedPort,
       "pgdot1dStpPortForwardTransitions": pgdot1dStpPortForwardTransitions,
       "pgdot1dStpPortRowStatus": pgdot1dStpPortRowStatus,
       "pgDot1dTp": pgDot1dTp,
       "pgDot1dTpFdbTable": pgDot1dTpFdbTable,
       "pgDot1dTpFdbEntry": pgDot1dTpFdbEntry,
       "pgDot1dTpFdbAddress": pgDot1dTpFdbAddress,
       "pgDot1dTpFdbPort": pgDot1dTpFdbPort,
       "pgDot1dTpFdbStatus": pgDot1dTpFdbStatus,
       "pgDot1dTpPortTable": pgDot1dTpPortTable,
       "pgDot1dTpPortEntry": pgDot1dTpPortEntry,
       "pgDot1dTpPort": pgDot1dTpPort,
       "pgDot1dTpPortMaxInfo": pgDot1dTpPortMaxInfo,
       "pgDot1dTpPortInFrames": pgDot1dTpPortInFrames,
       "pgDot1dTpPortOutFrames": pgDot1dTpPortOutFrames,
       "pgDot1dTpPortInDiscards": pgDot1dTpPortInDiscards,
       "pgDot1dStatic": pgDot1dStatic,
       "pgDot1dStaticTable": pgDot1dStaticTable,
       "pgDot1dStaticEntry": pgDot1dStaticEntry,
       "pgDot1dStaticAddress": pgDot1dStaticAddress,
       "pgDot1dStaticReceivePort": pgDot1dStaticReceivePort,
       "pgDot1dStaticAllowedToGoTo": pgDot1dStaticAllowedToGoTo,
       "pgDot1dStaticStatus": pgDot1dStaticStatus,
       "pgVlanGroup": pgVlanGroup,
       "pgVlanGroupTable": pgVlanGroupTable,
       "pgVlanGroupEntry": pgVlanGroupEntry,
       "pgBrVlanGroupIdentifier": pgBrVlanGroupIdentifier,
       "pgBrVlanGroupWanBcEnable": pgBrVlanGroupWanBcEnable,
       "pgBrVlanGroupName": pgBrVlanGroupName,
       "pgBrVlanGroupMode": pgBrVlanGroupMode,
       "pgBrVlanGroupTag": pgBrVlanGroupTag,
       "pgBrVlanGroupStpEnable": pgBrVlanGroupStpEnable,
       "pgBrVlanGroupStpProtocolSpecification": pgBrVlanGroupStpProtocolSpecification,
       "pgBrVlanGroupStpPriority": pgBrVlanGroupStpPriority,
       "pgBrVlanGroupStpTimeSinceTopologyChange": pgBrVlanGroupStpTimeSinceTopologyChange,
       "pgBrVlanGroupStpTopChanges": pgBrVlanGroupStpTopChanges,
       "pgBrVlanGroupStpDesignatedRoot": pgBrVlanGroupStpDesignatedRoot,
       "pgBrVlanGroupStpRootCost": pgBrVlanGroupStpRootCost,
       "pgBrVlanGroupStpRootPort": pgBrVlanGroupStpRootPort,
       "pgBrVlanGroupStpMaxAge": pgBrVlanGroupStpMaxAge,
       "pgBrVlanGroupStpHelloTime": pgBrVlanGroupStpHelloTime,
       "pgBrVlanGroupStpHoldTime": pgBrVlanGroupStpHoldTime,
       "pgBrVlanGroupStpForwardDelay": pgBrVlanGroupStpForwardDelay,
       "pgBrVlanGroupStpBridgeMaxAge": pgBrVlanGroupStpBridgeMaxAge,
       "pgBrVlanGroupStpBridgeHelloTime": pgBrVlanGroupStpBridgeHelloTime,
       "pgBrVlanGroupStpBridgeForwardDelay": pgBrVlanGroupStpBridgeForwardDelay,
       "pgBrVlanGroupRowStatus": pgBrVlanGroupRowStatus,
       "pgSessionRouterGroup": pgSessionRouterGroup,
       "pgSessionRouterGroupTable": pgSessionRouterGroupTable,
       "pgSessionRouterGroupEntry": pgSessionRouterGroupEntry,
       "pgSessionGroupIpAddress": pgSessionGroupIpAddress,
       "pgSessionGroupSubnetMask": pgSessionGroupSubnetMask,
       "pgSessionGroupRowStatus": pgSessionGroupRowStatus,
       "pgIfindexToSlotPortMap": pgIfindexToSlotPortMap,
       "pgIfindexToSlotPortMapTable": pgIfindexToSlotPortMapTable,
       "pgIfindexToSlotPortMapEntry": pgIfindexToSlotPortMapEntry,
       "pgIfindexToSlotPortMapSlot": pgIfindexToSlotPortMapSlot,
       "pgIfindexToSlotPortMapPort": pgIfindexToSlotPortMapPort,
       "pgIfindexToSlotPortMapIntVpi": pgIfindexToSlotPortMapIntVpi,
       "pgIfindexToSlotPortMapIntVci": pgIfindexToSlotPortMapIntVci,
       "pgIfindexToSlotPortMapExtVpi": pgIfindexToSlotPortMapExtVpi,
       "pgIfindexToSlotPortMapExtVci": pgIfindexToSlotPortMapExtVci,
       "pgBridgePortToSlotPortMap": pgBridgePortToSlotPortMap,
       "pgBridgePortToSlotPortMapTable": pgBridgePortToSlotPortMapTable,
       "pgBridgePortToSlotPortMapEntry": pgBridgePortToSlotPortMapEntry,
       "pgBridgePortToSlotPortMapSlot": pgBridgePortToSlotPortMapSlot,
       "pgBridgePortToSlotPortMapPort": pgBridgePortToSlotPortMapPort,
       "pgBridgePortToSlotPortMapIntVpi": pgBridgePortToSlotPortMapIntVpi,
       "pgBridgePortToSlotPortMapIntVci": pgBridgePortToSlotPortMapIntVci,
       "pgBridgePortToSlotPortMapExtVpi": pgBridgePortToSlotPortMapExtVpi,
       "pgBridgePortToSlotPortMapExtVci": pgBridgePortToSlotPortMapExtVci}
)
