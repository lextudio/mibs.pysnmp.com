# SNMP MIB module (SRM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SRM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:39 2024
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

(cardSpecific,) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "cardSpecific")

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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Srm3T3CnfGrp_ObjectIdentity = ObjectIdentity
srm3T3CnfGrp = _Srm3T3CnfGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 10)
)
_Srm3T3CnfGrpTable_Object = MibTable
srm3T3CnfGrpTable = _Srm3T3CnfGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 10, 1)
)
if mibBuilder.loadTexts:
    srm3T3CnfGrpTable.setStatus("mandatory")
_Srm3T3CnfGrpEntry_Object = MibTableRow
srm3T3CnfGrpEntry = _Srm3T3CnfGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 10, 1, 1)
)
srm3T3CnfGrpEntry.setIndexNames(
    (0, "SRM-MIB", "srmT3LineNum"),
    (0, "SRM-MIB", "srmStartT1LineNum"),
)
if mibBuilder.loadTexts:
    srm3T3CnfGrpEntry.setStatus("mandatory")


class _SrmT3LineNum_Type(Integer32):
    """Custom type srmT3LineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SrmT3LineNum_Type.__name__ = "Integer32"
_SrmT3LineNum_Object = MibTableColumn
srmT3LineNum = _SrmT3LineNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 10, 1, 1, 1),
    _SrmT3LineNum_Type()
)
srmT3LineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srmT3LineNum.setStatus("mandatory")


class _SrmStartT1LineNum_Type(Integer32):
    """Custom type srmStartT1LineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 28),
    )


_SrmStartT1LineNum_Type.__name__ = "Integer32"
_SrmStartT1LineNum_Object = MibTableColumn
srmStartT1LineNum = _SrmStartT1LineNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 10, 1, 1, 2),
    _SrmStartT1LineNum_Type()
)
srmStartT1LineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srmStartT1LineNum.setStatus("mandatory")


class _SrmT1RowStatus_Type(Integer32):
    """Custom type srmT1RowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("delete", 2),
          ("modify", 3))
    )


_SrmT1RowStatus_Type.__name__ = "Integer32"
_SrmT1RowStatus_Object = MibTableColumn
srmT1RowStatus = _SrmT1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 10, 1, 1, 3),
    _SrmT1RowStatus_Type()
)
srmT1RowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srmT1RowStatus.setStatus("mandatory")


class _SrmTargetSlotNum_Type(Integer32):
    """Custom type srmTargetSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SrmTargetSlotNum_Type.__name__ = "Integer32"
_SrmTargetSlotNum_Object = MibTableColumn
srmTargetSlotNum = _SrmTargetSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 10, 1, 1, 4),
    _SrmTargetSlotNum_Type()
)
srmTargetSlotNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srmTargetSlotNum.setStatus("mandatory")


class _SrmTargetSlotLineNum_Type(Integer32):
    """Custom type srmTargetSlotLineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_SrmTargetSlotLineNum_Type.__name__ = "Integer32"
_SrmTargetSlotLineNum_Object = MibTableColumn
srmTargetSlotLineNum = _SrmTargetSlotLineNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 10, 1, 1, 5),
    _SrmTargetSlotLineNum_Type()
)
srmTargetSlotLineNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srmTargetSlotLineNum.setStatus("mandatory")
_SrmeCnfGrp_ObjectIdentity = ObjectIdentity
srmeCnfGrp = _SrmeCnfGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 22)
)
_SrmeCnfGrpTable_Object = MibTable
srmeCnfGrpTable = _SrmeCnfGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 22, 1)
)
if mibBuilder.loadTexts:
    srmeCnfGrpTable.setStatus("mandatory")
_SrmeCnfGrpEntry_Object = MibTableRow
srmeCnfGrpEntry = _SrmeCnfGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 22, 1, 1)
)
srmeCnfGrpEntry.setIndexNames(
    (0, "SRM-MIB", "srmeLineNum"),
    (0, "SRM-MIB", "srmeStartVtNum"),
)
if mibBuilder.loadTexts:
    srmeCnfGrpEntry.setStatus("mandatory")


class _SrmeLineNum_Type(Integer32):
    """Custom type srmeLineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SrmeLineNum_Type.__name__ = "Integer32"
_SrmeLineNum_Object = MibTableColumn
srmeLineNum = _SrmeLineNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 22, 1, 1, 1),
    _SrmeLineNum_Type()
)
srmeLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srmeLineNum.setStatus("mandatory")


class _SrmeStartVtNum_Type(Integer32):
    """Custom type srmeStartVtNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 84),
    )


_SrmeStartVtNum_Type.__name__ = "Integer32"
_SrmeStartVtNum_Object = MibTableColumn
srmeStartVtNum = _SrmeStartVtNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 22, 1, 1, 2),
    _SrmeStartVtNum_Type()
)
srmeStartVtNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srmeStartVtNum.setStatus("mandatory")


class _SrmeRowStatus_Type(Integer32):
    """Custom type srmeRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("delete", 2),
          ("modify", 3))
    )


_SrmeRowStatus_Type.__name__ = "Integer32"
_SrmeRowStatus_Object = MibTableColumn
srmeRowStatus = _SrmeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 22, 1, 1, 3),
    _SrmeRowStatus_Type()
)
srmeRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srmeRowStatus.setStatus("mandatory")


class _SrmeTargetSlotNum_Type(Integer32):
    """Custom type srmeTargetSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SrmeTargetSlotNum_Type.__name__ = "Integer32"
_SrmeTargetSlotNum_Object = MibTableColumn
srmeTargetSlotNum = _SrmeTargetSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 22, 1, 1, 4),
    _SrmeTargetSlotNum_Type()
)
srmeTargetSlotNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srmeTargetSlotNum.setStatus("mandatory")


class _SrmeTargetSlotLineNum_Type(Integer32):
    """Custom type srmeTargetSlotLineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_SrmeTargetSlotLineNum_Type.__name__ = "Integer32"
_SrmeTargetSlotLineNum_Object = MibTableColumn
srmeTargetSlotLineNum = _SrmeTargetSlotLineNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 22, 1, 1, 5),
    _SrmeTargetSlotLineNum_Type()
)
srmeTargetSlotLineNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srmeTargetSlotLineNum.setStatus("mandatory")


class _SrmeVtFramingType_Type(Integer32):
    """Custom type srmeVtFramingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("esf", 3),
          ("notApplicable", 1),
          ("sf", 2))
    )


_SrmeVtFramingType_Type.__name__ = "Integer32"
_SrmeVtFramingType_Object = MibTableColumn
srmeVtFramingType = _SrmeVtFramingType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 22, 1, 1, 6),
    _SrmeVtFramingType_Type()
)
srmeVtFramingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srmeVtFramingType.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SRM-MIB",
    **{"srm3T3CnfGrp": srm3T3CnfGrp,
       "srm3T3CnfGrpTable": srm3T3CnfGrpTable,
       "srm3T3CnfGrpEntry": srm3T3CnfGrpEntry,
       "srmT3LineNum": srmT3LineNum,
       "srmStartT1LineNum": srmStartT1LineNum,
       "srmT1RowStatus": srmT1RowStatus,
       "srmTargetSlotNum": srmTargetSlotNum,
       "srmTargetSlotLineNum": srmTargetSlotLineNum,
       "srmeCnfGrp": srmeCnfGrp,
       "srmeCnfGrpTable": srmeCnfGrpTable,
       "srmeCnfGrpEntry": srmeCnfGrpEntry,
       "srmeLineNum": srmeLineNum,
       "srmeStartVtNum": srmeStartVtNum,
       "srmeRowStatus": srmeRowStatus,
       "srmeTargetSlotNum": srmeTargetSlotNum,
       "srmeTargetSlotLineNum": srmeTargetSlotLineNum,
       "srmeVtFramingType": srmeVtFramingType}
)
