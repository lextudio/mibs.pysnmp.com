# SNMP MIB module (NMS-EPON-LLID) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NMS-EPON-LLID
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:40 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NmsEponLlid_ObjectIdentity = ObjectIdentity
nmsEponLlid = _NmsEponLlid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 9)
)
_NmseponllidTable_Object = MibTable
nmseponllidTable = _NmseponllidTable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1)
)
if mibBuilder.loadTexts:
    nmseponllidTable.setStatus("mandatory")
_NmsEponLlidEntry_Object = MibTableRow
nmsEponLlidEntry = _NmsEponLlidEntry_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1)
)
nmsEponLlidEntry.setIndexNames(
    (0, "NMS-EPON-LLID", "llidIfIndex"),
)
if mibBuilder.loadTexts:
    nmsEponLlidEntry.setStatus("mandatory")
_LlidIfIndex_Type = Integer32
_LlidIfIndex_Object = MibTableColumn
llidIfIndex = _LlidIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 1),
    _LlidIfIndex_Type()
)
llidIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llidIfIndex.setStatus("mandatory")
_LlidToEponPortDiid_Type = Integer32
_LlidToEponPortDiid_Object = MibTableColumn
llidToEponPortDiid = _LlidToEponPortDiid_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 2),
    _LlidToEponPortDiid_Type()
)
llidToEponPortDiid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llidToEponPortDiid.setStatus("mandatory")
_LlidsequenceNo_Type = Integer32
_LlidsequenceNo_Object = MibTableColumn
llidsequenceNo = _LlidsequenceNo_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 3),
    _LlidsequenceNo_Type()
)
llidsequenceNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llidsequenceNo.setStatus("mandatory")
_LlidEncrypStatus_Type = TruthValue
_LlidEncrypStatus_Object = MibTableColumn
llidEncrypStatus = _LlidEncrypStatus_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 4),
    _LlidEncrypStatus_Type()
)
llidEncrypStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llidEncrypStatus.setStatus("mandatory")
_LlidCtcOamExtStatus_Type = OctetString
_LlidCtcOamExtStatus_Object = MibTableColumn
llidCtcOamExtStatus = _LlidCtcOamExtStatus_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 5),
    _LlidCtcOamExtStatus_Type()
)
llidCtcOamExtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llidCtcOamExtStatus.setStatus("mandatory")
_LlidCtcOamExtOui_Type = OctetString
_LlidCtcOamExtOui_Object = MibTableColumn
llidCtcOamExtOui = _LlidCtcOamExtOui_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 6),
    _LlidCtcOamExtOui_Type()
)
llidCtcOamExtOui.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llidCtcOamExtOui.setStatus("mandatory")
_LlidCtcOamExtVersion_Type = Integer32
_LlidCtcOamExtVersion_Object = MibTableColumn
llidCtcOamExtVersion = _LlidCtcOamExtVersion_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 7),
    _LlidCtcOamExtVersion_Type()
)
llidCtcOamExtVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llidCtcOamExtVersion.setStatus("mandatory")


class _LlidIfPIR_Type(Integer32):
    """Custom type llidIfPIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_LlidIfPIR_Type.__name__ = "Integer32"
_LlidIfPIR_Object = MibTableColumn
llidIfPIR = _LlidIfPIR_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 8),
    _LlidIfPIR_Type()
)
llidIfPIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llidIfPIR.setStatus("mandatory")


class _LlidIfCIR_Type(Integer32):
    """Custom type llidIfCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 955000),
    )


_LlidIfCIR_Type.__name__ = "Integer32"
_LlidIfCIR_Object = MibTableColumn
llidIfCIR = _LlidIfCIR_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 9),
    _LlidIfCIR_Type()
)
llidIfCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llidIfCIR.setStatus("mandatory")


class _LlidIfFIR_Type(Integer32):
    """Custom type llidIfFIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 955000),
    )


_LlidIfFIR_Type.__name__ = "Integer32"
_LlidIfFIR_Object = MibTableColumn
llidIfFIR = _LlidIfFIR_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 10),
    _LlidIfFIR_Type()
)
llidIfFIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llidIfFIR.setStatus("mandatory")
_LlidIfConfigRowStatus_Type = RowStatus
_LlidIfConfigRowStatus_Object = MibTableColumn
llidIfConfigRowStatus = _LlidIfConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 11),
    _LlidIfConfigRowStatus_Type()
)
llidIfConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    llidIfConfigRowStatus.setStatus("mandatory")


class _LlidIfDynamicMacLearningStatus_Type(Integer32):
    """Custom type llidIfDynamicMacLearningStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_LlidIfDynamicMacLearningStatus_Type.__name__ = "Integer32"
_LlidIfDynamicMacLearningStatus_Object = MibTableColumn
llidIfDynamicMacLearningStatus = _LlidIfDynamicMacLearningStatus_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 12),
    _LlidIfDynamicMacLearningStatus_Type()
)
llidIfDynamicMacLearningStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llidIfDynamicMacLearningStatus.setStatus("mandatory")
_LlidIfDynamicMacLearningLimit_Type = TruthValue
_LlidIfDynamicMacLearningLimit_Object = MibTableColumn
llidIfDynamicMacLearningLimit = _LlidIfDynamicMacLearningLimit_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 13),
    _LlidIfDynamicMacLearningLimit_Type()
)
llidIfDynamicMacLearningLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llidIfDynamicMacLearningLimit.setStatus("mandatory")


class _LlidIfDynamicMacLearningNumberLimit_Type(Integer32):
    """Custom type llidIfDynamicMacLearningNumberLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_LlidIfDynamicMacLearningNumberLimit_Type.__name__ = "Integer32"
_LlidIfDynamicMacLearningNumberLimit_Object = MibTableColumn
llidIfDynamicMacLearningNumberLimit = _LlidIfDynamicMacLearningNumberLimit_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 14),
    _LlidIfDynamicMacLearningNumberLimit_Type()
)
llidIfDynamicMacLearningNumberLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llidIfDynamicMacLearningNumberLimit.setStatus("mandatory")
_LlidIfQosPolicy_Type = OctetString
_LlidIfQosPolicy_Object = MibTableColumn
llidIfQosPolicy = _LlidIfQosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 15),
    _LlidIfQosPolicy_Type()
)
llidIfQosPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llidIfQosPolicy.setStatus("mandatory")
_LlidIfACL_Type = OctetString
_LlidIfACL_Object = MibTableColumn
llidIfACL = _LlidIfACL_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 16),
    _LlidIfACL_Type()
)
llidIfACL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llidIfACL.setStatus("mandatory")


class _LlidDownStreamPir_Type(Integer32):
    """Custom type llidDownStreamPir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_LlidDownStreamPir_Type.__name__ = "Integer32"
_LlidDownStreamPir_Object = MibTableColumn
llidDownStreamPir = _LlidDownStreamPir_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 17),
    _LlidDownStreamPir_Type()
)
llidDownStreamPir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llidDownStreamPir.setStatus("mandatory")


class _LlidDownStreamCir_Type(Integer32):
    """Custom type llidDownStreamCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 955000),
    )


_LlidDownStreamCir_Type.__name__ = "Integer32"
_LlidDownStreamCir_Object = MibTableColumn
llidDownStreamCir = _LlidDownStreamCir_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 18),
    _LlidDownStreamCir_Type()
)
llidDownStreamCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llidDownStreamCir.setStatus("mandatory")


class _LlidDownStreamFir_Type(Integer32):
    """Custom type llidDownStreamFir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 955000),
    )


_LlidDownStreamFir_Type.__name__ = "Integer32"
_LlidDownStreamFir_Object = MibTableColumn
llidDownStreamFir = _LlidDownStreamFir_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 19),
    _LlidDownStreamFir_Type()
)
llidDownStreamFir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llidDownStreamFir.setStatus("mandatory")
_LlidDownStreamIfRowstatus_Type = RowStatus
_LlidDownStreamIfRowstatus_Object = MibTableColumn
llidDownStreamIfRowstatus = _LlidDownStreamIfRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 20),
    _LlidDownStreamIfRowstatus_Type()
)
llidDownStreamIfRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    llidDownStreamIfRowstatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NMS-EPON-LLID",
    **{"nmsEponLlid": nmsEponLlid,
       "nmseponllidTable": nmseponllidTable,
       "nmsEponLlidEntry": nmsEponLlidEntry,
       "llidIfIndex": llidIfIndex,
       "llidToEponPortDiid": llidToEponPortDiid,
       "llidsequenceNo": llidsequenceNo,
       "llidEncrypStatus": llidEncrypStatus,
       "llidCtcOamExtStatus": llidCtcOamExtStatus,
       "llidCtcOamExtOui": llidCtcOamExtOui,
       "llidCtcOamExtVersion": llidCtcOamExtVersion,
       "llidIfPIR": llidIfPIR,
       "llidIfCIR": llidIfCIR,
       "llidIfFIR": llidIfFIR,
       "llidIfConfigRowStatus": llidIfConfigRowStatus,
       "llidIfDynamicMacLearningStatus": llidIfDynamicMacLearningStatus,
       "llidIfDynamicMacLearningLimit": llidIfDynamicMacLearningLimit,
       "llidIfDynamicMacLearningNumberLimit": llidIfDynamicMacLearningNumberLimit,
       "llidIfQosPolicy": llidIfQosPolicy,
       "llidIfACL": llidIfACL,
       "llidDownStreamPir": llidDownStreamPir,
       "llidDownStreamCir": llidDownStreamCir,
       "llidDownStreamFir": llidDownStreamFir,
       "llidDownStreamIfRowstatus": llidDownStreamIfRowstatus}
)
