# SNMP MIB module (NMS-EPON-ONU-BATCH-CONFIG) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NMS-EPON-ONU-BATCH-CONFIG
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:47 2024
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

(nmsEPONGroup,) = mibBuilder.importSymbols(
    "NMS-SMI",
    "nmsEPONGroup")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NmsEponOnuBatchConfig_ObjectIdentity = ObjectIdentity
nmsEponOnuBatchConfig = _NmsEponOnuBatchConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 22)
)
_NmsEponOnuConfigIndex_Type = Integer32
_NmsEponOnuConfigIndex_Object = MibScalar
nmsEponOnuConfigIndex = _NmsEponOnuConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 22, 1),
    _NmsEponOnuConfigIndex_Type()
)
nmsEponOnuConfigIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsEponOnuConfigIndex.setStatus("mandatory")
_NmsEponOnuConfigTable_Object = MibTable
nmsEponOnuConfigTable = _NmsEponOnuConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 22, 2)
)
if mibBuilder.loadTexts:
    nmsEponOnuConfigTable.setStatus("mandatory")
_NmsEponOnuConfigEntry_Object = MibTableRow
nmsEponOnuConfigEntry = _NmsEponOnuConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 22, 2, 1)
)
nmsEponOnuConfigEntry.setIndexNames(
    (0, "NMS-EPON-ONU-BATCH-CONFIG", "onuConfigSequenceNo"),
)
if mibBuilder.loadTexts:
    nmsEponOnuConfigEntry.setStatus("mandatory")
_OnuConfigSequenceNo_Type = Integer32
_OnuConfigSequenceNo_Object = MibTableColumn
onuConfigSequenceNo = _OnuConfigSequenceNo_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 22, 2, 1, 1),
    _OnuConfigSequenceNo_Type()
)
onuConfigSequenceNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuConfigSequenceNo.setStatus("mandatory")
_OnuConfigCommand_Type = OctetString
_OnuConfigCommand_Object = MibTableColumn
onuConfigCommand = _OnuConfigCommand_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 22, 2, 1, 2),
    _OnuConfigCommand_Type()
)
onuConfigCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuConfigCommand.setStatus("mandatory")
_OnuConfigurationAdd_Type = OctetString
_OnuConfigurationAdd_Object = MibScalar
onuConfigurationAdd = _OnuConfigurationAdd_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 22, 3),
    _OnuConfigurationAdd_Type()
)
onuConfigurationAdd.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    onuConfigurationAdd.setStatus("mandatory")
_OnuCfgApplyLLIDs_Type = PortList
_OnuCfgApplyLLIDs_Object = MibScalar
onuCfgApplyLLIDs = _OnuCfgApplyLLIDs_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 22, 4),
    _OnuCfgApplyLLIDs_Type()
)
onuCfgApplyLLIDs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuCfgApplyLLIDs.setStatus("mandatory")


class _OnuCfgApplyAction_Type(Integer32):
    """Custom type onuCfgApplyAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("apply", 1),
          ("no_action", 0))
    )


_OnuCfgApplyAction_Type.__name__ = "Integer32"
_OnuCfgApplyAction_Object = MibScalar
onuCfgApplyAction = _OnuCfgApplyAction_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 22, 5),
    _OnuCfgApplyAction_Type()
)
onuCfgApplyAction.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    onuCfgApplyAction.setStatus("mandatory")


class _OunCfgApplyResult_Type(Integer32):
    """Custom type ounCfgApplyResult based on Integer32"""
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
        *(("other", 2),
          ("processing", 1),
          ("reserved", 3),
          ("success", 0))
    )


_OunCfgApplyResult_Type.__name__ = "Integer32"
_OunCfgApplyResult_Object = MibScalar
ounCfgApplyResult = _OunCfgApplyResult_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 22, 6),
    _OunCfgApplyResult_Type()
)
ounCfgApplyResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ounCfgApplyResult.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NMS-EPON-ONU-BATCH-CONFIG",
    **{"nmsEponOnuBatchConfig": nmsEponOnuBatchConfig,
       "nmsEponOnuConfigIndex": nmsEponOnuConfigIndex,
       "nmsEponOnuConfigTable": nmsEponOnuConfigTable,
       "nmsEponOnuConfigEntry": nmsEponOnuConfigEntry,
       "onuConfigSequenceNo": onuConfigSequenceNo,
       "onuConfigCommand": onuConfigCommand,
       "onuConfigurationAdd": onuConfigurationAdd,
       "onuCfgApplyLLIDs": onuCfgApplyLLIDs,
       "onuCfgApplyAction": onuCfgApplyAction,
       "ounCfgApplyResult": ounCfgApplyResult}
)
