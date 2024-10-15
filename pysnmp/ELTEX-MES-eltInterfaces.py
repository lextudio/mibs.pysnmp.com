# SNMP MIB module (ELTEX-MES-eltInterfaces) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-MES-eltInterfaces
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:11 2024
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

(eltMesSwInterfaces,) = mibBuilder.importSymbols(
    "ELTEX-MES",
    "eltMesSwInterfaces")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltSwIfTable_Object = MibTable
eltSwIfTable = _EltSwIfTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 43, 1)
)
if mibBuilder.loadTexts:
    eltSwIfTable.setStatus("current")
_EltSwIfEntry_Object = MibTableRow
eltSwIfEntry = _EltSwIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 43, 1, 1)
)
eltSwIfEntry.setIndexNames(
    (0, "ELTEX-MES-eltInterfaces", "eltSwIfIndex"),
)
if mibBuilder.loadTexts:
    eltSwIfEntry.setStatus("current")
_EltSwIfIndex_Type = Integer32
_EltSwIfIndex_Object = MibTableColumn
eltSwIfIndex = _EltSwIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 43, 1, 1, 1),
    _EltSwIfIndex_Type()
)
eltSwIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltSwIfIndex.setStatus("current")


class _EltSwIfSfpOperationMode_Type(Integer32):
    """Custom type eltSwIfSfpOperationMode based on Integer32"""
    defaultValue = 3

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
        *(("copperSfp", 2),
          ("directAttach", 1),
          ("fiber", 0),
          ("unknown", 3))
    )


_EltSwIfSfpOperationMode_Type.__name__ = "Integer32"
_EltSwIfSfpOperationMode_Object = MibTableColumn
eltSwIfSfpOperationMode = _EltSwIfSfpOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 43, 1, 1, 2),
    _EltSwIfSfpOperationMode_Type()
)
eltSwIfSfpOperationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltSwIfSfpOperationMode.setStatus("current")
_EltSwIfUtilizationTable_Object = MibTable
eltSwIfUtilizationTable = _EltSwIfUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 43, 2)
)
if mibBuilder.loadTexts:
    eltSwIfUtilizationTable.setStatus("current")
_EltSwIfUtilizationEntry_Object = MibTableRow
eltSwIfUtilizationEntry = _EltSwIfUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 43, 2, 1)
)
eltSwIfUtilizationEntry.setIndexNames(
    (0, "ELTEX-MES-eltInterfaces", "eltSwIfUtilizationIfIndex"),
)
if mibBuilder.loadTexts:
    eltSwIfUtilizationEntry.setStatus("current")
_EltSwIfUtilizationIfIndex_Type = Integer32
_EltSwIfUtilizationIfIndex_Object = MibTableColumn
eltSwIfUtilizationIfIndex = _EltSwIfUtilizationIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 43, 2, 1, 1),
    _EltSwIfUtilizationIfIndex_Type()
)
eltSwIfUtilizationIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltSwIfUtilizationIfIndex.setStatus("current")
_EltSwIfUtilizationAverageTime_Type = Integer32
_EltSwIfUtilizationAverageTime_Object = MibTableColumn
eltSwIfUtilizationAverageTime = _EltSwIfUtilizationAverageTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 43, 2, 1, 2),
    _EltSwIfUtilizationAverageTime_Type()
)
eltSwIfUtilizationAverageTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltSwIfUtilizationAverageTime.setStatus("current")
_EltSwIfUtilizationCurrentInPkts_Type = Counter32
_EltSwIfUtilizationCurrentInPkts_Object = MibTableColumn
eltSwIfUtilizationCurrentInPkts = _EltSwIfUtilizationCurrentInPkts_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 43, 2, 1, 3),
    _EltSwIfUtilizationCurrentInPkts_Type()
)
eltSwIfUtilizationCurrentInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltSwIfUtilizationCurrentInPkts.setStatus("current")
_EltSwIfUtilizationCurrentInRate_Type = Counter32
_EltSwIfUtilizationCurrentInRate_Object = MibTableColumn
eltSwIfUtilizationCurrentInRate = _EltSwIfUtilizationCurrentInRate_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 43, 2, 1, 4),
    _EltSwIfUtilizationCurrentInRate_Type()
)
eltSwIfUtilizationCurrentInRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltSwIfUtilizationCurrentInRate.setStatus("current")
_EltSwIfUtilizationCurrentOutPkts_Type = Counter32
_EltSwIfUtilizationCurrentOutPkts_Object = MibTableColumn
eltSwIfUtilizationCurrentOutPkts = _EltSwIfUtilizationCurrentOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 43, 2, 1, 5),
    _EltSwIfUtilizationCurrentOutPkts_Type()
)
eltSwIfUtilizationCurrentOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltSwIfUtilizationCurrentOutPkts.setStatus("current")
_EltSwIfUtilizationCurrentOutRate_Type = Counter32
_EltSwIfUtilizationCurrentOutRate_Object = MibTableColumn
eltSwIfUtilizationCurrentOutRate = _EltSwIfUtilizationCurrentOutRate_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 43, 2, 1, 6),
    _EltSwIfUtilizationCurrentOutRate_Type()
)
eltSwIfUtilizationCurrentOutRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltSwIfUtilizationCurrentOutRate.setStatus("current")
_EltSwIfUtilizationAverageInPkts_Type = Counter32
_EltSwIfUtilizationAverageInPkts_Object = MibTableColumn
eltSwIfUtilizationAverageInPkts = _EltSwIfUtilizationAverageInPkts_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 43, 2, 1, 7),
    _EltSwIfUtilizationAverageInPkts_Type()
)
eltSwIfUtilizationAverageInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltSwIfUtilizationAverageInPkts.setStatus("current")
_EltSwIfUtilizationAverageInRate_Type = Counter32
_EltSwIfUtilizationAverageInRate_Object = MibTableColumn
eltSwIfUtilizationAverageInRate = _EltSwIfUtilizationAverageInRate_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 43, 2, 1, 8),
    _EltSwIfUtilizationAverageInRate_Type()
)
eltSwIfUtilizationAverageInRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltSwIfUtilizationAverageInRate.setStatus("current")
_EltSwIfUtilizationAverageOutPkts_Type = Counter32
_EltSwIfUtilizationAverageOutPkts_Object = MibTableColumn
eltSwIfUtilizationAverageOutPkts = _EltSwIfUtilizationAverageOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 43, 2, 1, 9),
    _EltSwIfUtilizationAverageOutPkts_Type()
)
eltSwIfUtilizationAverageOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltSwIfUtilizationAverageOutPkts.setStatus("current")
_EltSwIfUtilizationAverageOutRate_Type = Counter32
_EltSwIfUtilizationAverageOutRate_Object = MibTableColumn
eltSwIfUtilizationAverageOutRate = _EltSwIfUtilizationAverageOutRate_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 43, 2, 1, 10),
    _EltSwIfUtilizationAverageOutRate_Type()
)
eltSwIfUtilizationAverageOutRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltSwIfUtilizationAverageOutRate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-eltInterfaces",
    **{"eltSwIfTable": eltSwIfTable,
       "eltSwIfEntry": eltSwIfEntry,
       "eltSwIfIndex": eltSwIfIndex,
       "eltSwIfSfpOperationMode": eltSwIfSfpOperationMode,
       "eltSwIfUtilizationTable": eltSwIfUtilizationTable,
       "eltSwIfUtilizationEntry": eltSwIfUtilizationEntry,
       "eltSwIfUtilizationIfIndex": eltSwIfUtilizationIfIndex,
       "eltSwIfUtilizationAverageTime": eltSwIfUtilizationAverageTime,
       "eltSwIfUtilizationCurrentInPkts": eltSwIfUtilizationCurrentInPkts,
       "eltSwIfUtilizationCurrentInRate": eltSwIfUtilizationCurrentInRate,
       "eltSwIfUtilizationCurrentOutPkts": eltSwIfUtilizationCurrentOutPkts,
       "eltSwIfUtilizationCurrentOutRate": eltSwIfUtilizationCurrentOutRate,
       "eltSwIfUtilizationAverageInPkts": eltSwIfUtilizationAverageInPkts,
       "eltSwIfUtilizationAverageInRate": eltSwIfUtilizationAverageInRate,
       "eltSwIfUtilizationAverageOutPkts": eltSwIfUtilizationAverageOutPkts,
       "eltSwIfUtilizationAverageOutRate": eltSwIfUtilizationAverageOutRate}
)
