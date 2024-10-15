# SNMP MIB module (Wellfleet-IPACCT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-IPACCT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:27 2024
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

(wfAccountingGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfAccountingGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfIpAcctGroup_ObjectIdentity = ObjectIdentity
wfIpAcctGroup = _WfIpAcctGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1)
)
_WfIpAcctBase_ObjectIdentity = ObjectIdentity
wfIpAcctBase = _WfIpAcctBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 1)
)


class _WfIpAcctBaseCreate_Type(Integer32):
    """Custom type wfIpAcctBaseCreate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfIpAcctBaseCreate_Type.__name__ = "Integer32"
_WfIpAcctBaseCreate_Object = MibScalar
wfIpAcctBaseCreate = _WfIpAcctBaseCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 1, 1),
    _WfIpAcctBaseCreate_Type()
)
wfIpAcctBaseCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpAcctBaseCreate.setStatus("mandatory")


class _WfIpAcctBaseEnable_Type(Integer32):
    """Custom type wfIpAcctBaseEnable based on Integer32"""
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


_WfIpAcctBaseEnable_Type.__name__ = "Integer32"
_WfIpAcctBaseEnable_Object = MibScalar
wfIpAcctBaseEnable = _WfIpAcctBaseEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 1, 2),
    _WfIpAcctBaseEnable_Type()
)
wfIpAcctBaseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpAcctBaseEnable.setStatus("mandatory")


class _WfIpAcctBaseThreshold_Type(Integer32):
    """Custom type wfIpAcctBaseThreshold based on Integer32"""
    defaultValue = 512

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10240),
    )


_WfIpAcctBaseThreshold_Type.__name__ = "Integer32"
_WfIpAcctBaseThreshold_Object = MibScalar
wfIpAcctBaseThreshold = _WfIpAcctBaseThreshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 1, 3),
    _WfIpAcctBaseThreshold_Type()
)
wfIpAcctBaseThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpAcctBaseThreshold.setStatus("mandatory")


class _WfIpAcctBaseTransitCount_Type(Integer32):
    """Custom type wfIpAcctBaseTransitCount based on Integer32"""
    defaultValue = 512

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10240),
    )


_WfIpAcctBaseTransitCount_Type.__name__ = "Integer32"
_WfIpAcctBaseTransitCount_Object = MibScalar
wfIpAcctBaseTransitCount = _WfIpAcctBaseTransitCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 1, 4),
    _WfIpAcctBaseTransitCount_Type()
)
wfIpAcctBaseTransitCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpAcctBaseTransitCount.setStatus("mandatory")


class _WfIpAcctBaseTrapPercent_Type(Integer32):
    """Custom type wfIpAcctBaseTrapPercent based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WfIpAcctBaseTrapPercent_Type.__name__ = "Integer32"
_WfIpAcctBaseTrapPercent_Object = MibScalar
wfIpAcctBaseTrapPercent = _WfIpAcctBaseTrapPercent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 1, 5),
    _WfIpAcctBaseTrapPercent_Type()
)
wfIpAcctBaseTrapPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpAcctBaseTrapPercent.setStatus("mandatory")
_WfIpAcctAge_Type = TimeTicks
_WfIpAcctAge_Object = MibScalar
wfIpAcctAge = _WfIpAcctAge_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 1, 6),
    _WfIpAcctAge_Type()
)
wfIpAcctAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpAcctAge.setStatus("mandatory")
_WfIpCkAcctFlag_Type = Integer32
_WfIpCkAcctFlag_Object = MibScalar
wfIpCkAcctFlag = _WfIpCkAcctFlag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 1, 7),
    _WfIpCkAcctFlag_Type()
)
wfIpCkAcctFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpCkAcctFlag.setStatus("mandatory")
_WfIpCkAcctAge_Type = TimeTicks
_WfIpCkAcctAge_Object = MibScalar
wfIpCkAcctAge = _WfIpCkAcctAge_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 1, 8),
    _WfIpCkAcctAge_Type()
)
wfIpCkAcctAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpCkAcctAge.setStatus("mandatory")
_WfIpAcctTable_Object = MibTable
wfIpAcctTable = _WfIpAcctTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 2)
)
if mibBuilder.loadTexts:
    wfIpAcctTable.setStatus("mandatory")
_WfIpAcctTableEntry_Object = MibTableRow
wfIpAcctTableEntry = _WfIpAcctTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 2, 1)
)
wfIpAcctTableEntry.setIndexNames(
    (0, "Wellfleet-IPACCT-MIB", "wfIpAcctTableSrcAddr"),
    (0, "Wellfleet-IPACCT-MIB", "wfIpAcctTableDestAddr"),
)
if mibBuilder.loadTexts:
    wfIpAcctTableEntry.setStatus("mandatory")
_WfIpAcctTableSrcAddr_Type = IpAddress
_WfIpAcctTableSrcAddr_Object = MibTableColumn
wfIpAcctTableSrcAddr = _WfIpAcctTableSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 2, 1, 1),
    _WfIpAcctTableSrcAddr_Type()
)
wfIpAcctTableSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpAcctTableSrcAddr.setStatus("mandatory")
_WfIpAcctTableDestAddr_Type = IpAddress
_WfIpAcctTableDestAddr_Object = MibTableColumn
wfIpAcctTableDestAddr = _WfIpAcctTableDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 2, 1, 2),
    _WfIpAcctTableDestAddr_Type()
)
wfIpAcctTableDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpAcctTableDestAddr.setStatus("mandatory")
_WfIpAcctTablePkts_Type = Counter32
_WfIpAcctTablePkts_Object = MibTableColumn
wfIpAcctTablePkts = _WfIpAcctTablePkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 2, 1, 3),
    _WfIpAcctTablePkts_Type()
)
wfIpAcctTablePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpAcctTablePkts.setStatus("mandatory")
_WfIpAcctTableBytes_Type = Counter32
_WfIpAcctTableBytes_Object = MibTableColumn
wfIpAcctTableBytes = _WfIpAcctTableBytes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 2, 1, 4),
    _WfIpAcctTableBytes_Type()
)
wfIpAcctTableBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpAcctTableBytes.setStatus("mandatory")
_WfIpAcctCctTable_Object = MibTable
wfIpAcctCctTable = _WfIpAcctCctTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 3)
)
if mibBuilder.loadTexts:
    wfIpAcctCctTable.setStatus("mandatory")
_WfIpAcctCctTableEntry_Object = MibTableRow
wfIpAcctCctTableEntry = _WfIpAcctCctTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 3, 1)
)
wfIpAcctCctTableEntry.setIndexNames(
    (0, "Wellfleet-IPACCT-MIB", "wfIpAcctCctNum"),
)
if mibBuilder.loadTexts:
    wfIpAcctCctTableEntry.setStatus("mandatory")


class _WfIpAcctCctDelete_Type(Integer32):
    """Custom type wfIpAcctCctDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfIpAcctCctDelete_Type.__name__ = "Integer32"
_WfIpAcctCctDelete_Object = MibTableColumn
wfIpAcctCctDelete = _WfIpAcctCctDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 3, 1, 1),
    _WfIpAcctCctDelete_Type()
)
wfIpAcctCctDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpAcctCctDelete.setStatus("mandatory")


class _WfIpAcctCctDisable_Type(Integer32):
    """Custom type wfIpAcctCctDisable based on Integer32"""
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


_WfIpAcctCctDisable_Type.__name__ = "Integer32"
_WfIpAcctCctDisable_Object = MibTableColumn
wfIpAcctCctDisable = _WfIpAcctCctDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 3, 1, 2),
    _WfIpAcctCctDisable_Type()
)
wfIpAcctCctDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpAcctCctDisable.setStatus("mandatory")
_WfIpAcctCctNum_Type = Integer32
_WfIpAcctCctNum_Object = MibTableColumn
wfIpAcctCctNum = _WfIpAcctCctNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 3, 1, 3),
    _WfIpAcctCctNum_Type()
)
wfIpAcctCctNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpAcctCctNum.setStatus("mandatory")
_WfIpCkAcctTable_Object = MibTable
wfIpCkAcctTable = _WfIpCkAcctTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 4)
)
if mibBuilder.loadTexts:
    wfIpCkAcctTable.setStatus("mandatory")
_WfIpCkAcctTableEntry_Object = MibTableRow
wfIpCkAcctTableEntry = _WfIpCkAcctTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 4, 1)
)
wfIpCkAcctTableEntry.setIndexNames(
    (0, "Wellfleet-IPACCT-MIB", "wfIpCkAcctTableSrcAddr"),
    (0, "Wellfleet-IPACCT-MIB", "wfIpCkAcctTableDestAddr"),
)
if mibBuilder.loadTexts:
    wfIpCkAcctTableEntry.setStatus("mandatory")
_WfIpCkAcctTableSrcAddr_Type = IpAddress
_WfIpCkAcctTableSrcAddr_Object = MibTableColumn
wfIpCkAcctTableSrcAddr = _WfIpCkAcctTableSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 4, 1, 1),
    _WfIpCkAcctTableSrcAddr_Type()
)
wfIpCkAcctTableSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpCkAcctTableSrcAddr.setStatus("mandatory")
_WfIpCkAcctTableDestAddr_Type = IpAddress
_WfIpCkAcctTableDestAddr_Object = MibTableColumn
wfIpCkAcctTableDestAddr = _WfIpCkAcctTableDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 4, 1, 2),
    _WfIpCkAcctTableDestAddr_Type()
)
wfIpCkAcctTableDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpCkAcctTableDestAddr.setStatus("mandatory")
_WfIpCkAcctTablePkts_Type = Counter32
_WfIpCkAcctTablePkts_Object = MibTableColumn
wfIpCkAcctTablePkts = _WfIpCkAcctTablePkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 4, 1, 3),
    _WfIpCkAcctTablePkts_Type()
)
wfIpCkAcctTablePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpCkAcctTablePkts.setStatus("mandatory")
_WfIpCkAcctTableBytes_Type = Counter32
_WfIpCkAcctTableBytes_Object = MibTableColumn
wfIpCkAcctTableBytes = _WfIpCkAcctTableBytes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 4, 1, 4),
    _WfIpCkAcctTableBytes_Type()
)
wfIpCkAcctTableBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpCkAcctTableBytes.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-IPACCT-MIB",
    **{"wfIpAcctGroup": wfIpAcctGroup,
       "wfIpAcctBase": wfIpAcctBase,
       "wfIpAcctBaseCreate": wfIpAcctBaseCreate,
       "wfIpAcctBaseEnable": wfIpAcctBaseEnable,
       "wfIpAcctBaseThreshold": wfIpAcctBaseThreshold,
       "wfIpAcctBaseTransitCount": wfIpAcctBaseTransitCount,
       "wfIpAcctBaseTrapPercent": wfIpAcctBaseTrapPercent,
       "wfIpAcctAge": wfIpAcctAge,
       "wfIpCkAcctFlag": wfIpCkAcctFlag,
       "wfIpCkAcctAge": wfIpCkAcctAge,
       "wfIpAcctTable": wfIpAcctTable,
       "wfIpAcctTableEntry": wfIpAcctTableEntry,
       "wfIpAcctTableSrcAddr": wfIpAcctTableSrcAddr,
       "wfIpAcctTableDestAddr": wfIpAcctTableDestAddr,
       "wfIpAcctTablePkts": wfIpAcctTablePkts,
       "wfIpAcctTableBytes": wfIpAcctTableBytes,
       "wfIpAcctCctTable": wfIpAcctCctTable,
       "wfIpAcctCctTableEntry": wfIpAcctCctTableEntry,
       "wfIpAcctCctDelete": wfIpAcctCctDelete,
       "wfIpAcctCctDisable": wfIpAcctCctDisable,
       "wfIpAcctCctNum": wfIpAcctCctNum,
       "wfIpCkAcctTable": wfIpCkAcctTable,
       "wfIpCkAcctTableEntry": wfIpCkAcctTableEntry,
       "wfIpCkAcctTableSrcAddr": wfIpCkAcctTableSrcAddr,
       "wfIpCkAcctTableDestAddr": wfIpCkAcctTableDestAddr,
       "wfIpCkAcctTablePkts": wfIpCkAcctTablePkts,
       "wfIpCkAcctTableBytes": wfIpCkAcctTableBytes}
)
