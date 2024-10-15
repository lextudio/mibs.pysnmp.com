# SNMP MIB module (ACC-TUNNEL) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-TUNNEL
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:07 2024
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

(DisplayString,
 IfIndex,
 RowStatus,
 SmdsAddress,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "IfIndex",
    "RowStatus",
    "SmdsAddress",
    "accBRG")

(accTrapLogSeqNum,) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accTrapLogSeqNum")

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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AccTunnel_ObjectIdentity = ObjectIdentity
accTunnel = _AccTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 72)
)
_AccTunnelScalars_ObjectIdentity = ObjectIdentity
accTunnelScalars = _AccTunnelScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 72, 1)
)


class _AccTunnelPortCount_Type(Integer32):
    """Custom type accTunnelPortCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccTunnelPortCount_Type.__name__ = "Integer32"
_AccTunnelPortCount_Object = MibScalar
accTunnelPortCount = _AccTunnelPortCount_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 72, 1, 1),
    _AccTunnelPortCount_Type()
)
accTunnelPortCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accTunnelPortCount.setStatus("mandatory")
_AccTunnelPortTable_Object = MibTable
accTunnelPortTable = _AccTunnelPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 72, 2)
)
if mibBuilder.loadTexts:
    accTunnelPortTable.setStatus("mandatory")
_AccTunnelPortEntry_Object = MibTableRow
accTunnelPortEntry = _AccTunnelPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 72, 2, 1)
)
accTunnelPortEntry.setIndexNames(
    (0, "ACC-TUNNEL", "accTunnelPortTunnelIfIndex"),
)
if mibBuilder.loadTexts:
    accTunnelPortEntry.setStatus("mandatory")


class _AccTunnelPortTunnelIfIndex_Type(Integer32):
    """Custom type accTunnelPortTunnelIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AccTunnelPortTunnelIfIndex_Type.__name__ = "Integer32"
_AccTunnelPortTunnelIfIndex_Object = MibTableColumn
accTunnelPortTunnelIfIndex = _AccTunnelPortTunnelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 72, 2, 1, 1),
    _AccTunnelPortTunnelIfIndex_Type()
)
accTunnelPortTunnelIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accTunnelPortTunnelIfIndex.setStatus("mandatory")


class _AccTunnelPortTunnelManager_Type(Integer32):
    """Custom type accTunnelPortTunnelManager based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("l2tp", 1)
    )


_AccTunnelPortTunnelManager_Type.__name__ = "Integer32"
_AccTunnelPortTunnelManager_Object = MibTableColumn
accTunnelPortTunnelManager = _AccTunnelPortTunnelManager_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 72, 2, 1, 2),
    _AccTunnelPortTunnelManager_Type()
)
accTunnelPortTunnelManager.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accTunnelPortTunnelManager.setStatus("mandatory")


class _AccTunnelPortAdminState_Type(Integer32):
    """Custom type accTunnelPortAdminState based on Integer32"""
    defaultValue = 2

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


_AccTunnelPortAdminState_Type.__name__ = "Integer32"
_AccTunnelPortAdminState_Object = MibTableColumn
accTunnelPortAdminState = _AccTunnelPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 72, 2, 1, 3),
    _AccTunnelPortAdminState_Type()
)
accTunnelPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accTunnelPortAdminState.setStatus("mandatory")


class _AccTunnelPortOperStatus_Type(Integer32):
    """Custom type accTunnelPortOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_AccTunnelPortOperStatus_Type.__name__ = "Integer32"
_AccTunnelPortOperStatus_Object = MibTableColumn
accTunnelPortOperStatus = _AccTunnelPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 72, 2, 1, 4),
    _AccTunnelPortOperStatus_Type()
)
accTunnelPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accTunnelPortOperStatus.setStatus("mandatory")
_AccTunnelPortAccessPartition_Type = DisplayString
_AccTunnelPortAccessPartition_Object = MibTableColumn
accTunnelPortAccessPartition = _AccTunnelPortAccessPartition_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 72, 2, 1, 5),
    _AccTunnelPortAccessPartition_Type()
)
accTunnelPortAccessPartition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accTunnelPortAccessPartition.setStatus("mandatory")
_AccTunnelPortCreate_Type = Integer32
_AccTunnelPortCreate_Object = MibTableColumn
accTunnelPortCreate = _AccTunnelPortCreate_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 72, 2, 1, 6),
    _AccTunnelPortCreate_Type()
)
accTunnelPortCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accTunnelPortCreate.setStatus("mandatory")
_AccTunnelPortStatus_Type = RowStatus
_AccTunnelPortStatus_Object = MibTableColumn
accTunnelPortStatus = _AccTunnelPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 72, 2, 1, 7),
    _AccTunnelPortStatus_Type()
)
accTunnelPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accTunnelPortStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-TUNNEL",
    **{"accTunnel": accTunnel,
       "accTunnelScalars": accTunnelScalars,
       "accTunnelPortCount": accTunnelPortCount,
       "accTunnelPortTable": accTunnelPortTable,
       "accTunnelPortEntry": accTunnelPortEntry,
       "accTunnelPortTunnelIfIndex": accTunnelPortTunnelIfIndex,
       "accTunnelPortTunnelManager": accTunnelPortTunnelManager,
       "accTunnelPortAdminState": accTunnelPortAdminState,
       "accTunnelPortOperStatus": accTunnelPortOperStatus,
       "accTunnelPortAccessPartition": accTunnelPortAccessPartition,
       "accTunnelPortCreate": accTunnelPortCreate,
       "accTunnelPortStatus": accTunnelPortStatus}
)
