# SNMP MIB module (CT-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CT-CHASSIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:00 2024
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

(chassis,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "chassis")

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

_ChType_Type = ObjectIdentifier
_ChType_Object = MibScalar
chType = _ChType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 1),
    _ChType_Type()
)
chType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chType.setStatus("mandatory")
_ChBackplaneTable_Object = MibTable
chBackplaneTable = _ChBackplaneTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    chBackplaneTable.setStatus("mandatory")
_ChBackplaneEntry_Object = MibTableRow
chBackplaneEntry = _ChBackplaneEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 2, 1)
)
chBackplaneEntry.setIndexNames(
    (0, "CT-CHASSIS-MIB", "chBackplaneID"),
)
if mibBuilder.loadTexts:
    chBackplaneEntry.setStatus("mandatory")
_ChBackplaneID_Type = Integer32
_ChBackplaneID_Object = MibTableColumn
chBackplaneID = _ChBackplaneID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 2, 1, 1),
    _ChBackplaneID_Type()
)
chBackplaneID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chBackplaneID.setStatus("mandatory")
_ChBackplaneType_Type = ObjectIdentifier
_ChBackplaneType_Object = MibTableColumn
chBackplaneType = _ChBackplaneType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 2, 1, 2),
    _ChBackplaneType_Type()
)
chBackplaneType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chBackplaneType.setStatus("mandatory")


class _ChNumSlots_Type(Integer32):
    """Custom type chNumSlots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_ChNumSlots_Type.__name__ = "Integer32"
_ChNumSlots_Object = MibScalar
chNumSlots = _ChNumSlots_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 3),
    _ChNumSlots_Type()
)
chNumSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chNumSlots.setStatus("mandatory")
_ChCompTable_Object = MibTable
chCompTable = _ChCompTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    chCompTable.setStatus("mandatory")
_ChCompEntry_Object = MibTableRow
chCompEntry = _ChCompEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 4, 1)
)
chCompEntry.setIndexNames(
    (0, "CT-CHASSIS-MIB", "chCompID"),
)
if mibBuilder.loadTexts:
    chCompEntry.setStatus("mandatory")
_ChCompID_Type = Integer32
_ChCompID_Object = MibTableColumn
chCompID = _ChCompID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 4, 1, 1),
    _ChCompID_Type()
)
chCompID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chCompID.setStatus("mandatory")


class _ChCompAdminStatus_Type(Integer32):
    """Custom type chCompAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("delete", 8),
          ("disabled", 7),
          ("enabled", 3),
          ("error", 6),
          ("invalid", 2),
          ("operational", 5),
          ("testing", 4),
          ("unknown", 1))
    )


_ChCompAdminStatus_Type.__name__ = "Integer32"
_ChCompAdminStatus_Object = MibTableColumn
chCompAdminStatus = _ChCompAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 4, 1, 2),
    _ChCompAdminStatus_Type()
)
chCompAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chCompAdminStatus.setStatus("mandatory")


class _ChCompArg_Type(OctetString):
    """Custom type chCompArg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_ChCompArg_Type.__name__ = "OctetString"
_ChCompArg_Object = MibTableColumn
chCompArg = _ChCompArg_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 4, 1, 3),
    _ChCompArg_Type()
)
chCompArg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chCompArg.setStatus("mandatory")
_ChCompType_Type = ObjectIdentifier
_ChCompType_Object = MibTableColumn
chCompType = _ChCompType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 4, 1, 4),
    _ChCompType_Type()
)
chCompType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chCompType.setStatus("mandatory")


class _ChCompName_Type(DisplayString):
    """Custom type chCompName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ChCompName_Type.__name__ = "DisplayString"
_ChCompName_Object = MibTableColumn
chCompName = _ChCompName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 4, 1, 5),
    _ChCompName_Type()
)
chCompName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chCompName.setStatus("mandatory")


class _ChCompVersion_Type(DisplayString):
    """Custom type chCompVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ChCompVersion_Type.__name__ = "DisplayString"
_ChCompVersion_Object = MibTableColumn
chCompVersion = _ChCompVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 4, 1, 6),
    _ChCompVersion_Type()
)
chCompVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chCompVersion.setStatus("mandatory")
_ChCompTimeStamp_Type = TimeTicks
_ChCompTimeStamp_Object = MibTableColumn
chCompTimeStamp = _ChCompTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 4, 1, 7),
    _ChCompTimeStamp_Type()
)
chCompTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chCompTimeStamp.setStatus("mandatory")


class _ChCompAccessPolicy_Type(Integer32):
    """Custom type chCompAccessPolicy based on Integer32"""
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
          ("other", 5),
          ("otherCommStr", 4),
          ("same", 3),
          ("unknown", 1))
    )


_ChCompAccessPolicy_Type.__name__ = "Integer32"
_ChCompAccessPolicy_Object = MibTableColumn
chCompAccessPolicy = _ChCompAccessPolicy_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 4, 1, 8),
    _ChCompAccessPolicy_Type()
)
chCompAccessPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chCompAccessPolicy.setStatus("mandatory")
_ChCompBasicCommStr_Type = OctetString
_ChCompBasicCommStr_Object = MibTableColumn
chCompBasicCommStr = _ChCompBasicCommStr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 4, 1, 9),
    _ChCompBasicCommStr_Type()
)
chCompBasicCommStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chCompBasicCommStr.setStatus("mandatory")
_ChCompROCommStr_Type = OctetString
_ChCompROCommStr_Object = MibTableColumn
chCompROCommStr = _ChCompROCommStr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 4, 1, 10),
    _ChCompROCommStr_Type()
)
chCompROCommStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chCompROCommStr.setStatus("mandatory")
_ChCompRWCommStr_Type = OctetString
_ChCompRWCommStr_Object = MibTableColumn
chCompRWCommStr = _ChCompRWCommStr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 4, 1, 11),
    _ChCompRWCommStr_Type()
)
chCompRWCommStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chCompRWCommStr.setStatus("mandatory")
_ChCompSUCommStr_Type = OctetString
_ChCompSUCommStr_Object = MibTableColumn
chCompSUCommStr = _ChCompSUCommStr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 4, 1, 12),
    _ChCompSUCommStr_Type()
)
chCompSUCommStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chCompSUCommStr.setStatus("mandatory")
_ChCompNetAdr_Type = IpAddress
_ChCompNetAdr_Object = MibTableColumn
chCompNetAdr = _ChCompNetAdr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 4, 1, 13),
    _ChCompNetAdr_Type()
)
chCompNetAdr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chCompNetAdr.setStatus("mandatory")
_ChSlotTable_Object = MibTable
chSlotTable = _ChSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    chSlotTable.setStatus("mandatory")
_ChSlotEntry_Object = MibTableRow
chSlotEntry = _ChSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 5, 1)
)
chSlotEntry.setIndexNames(
    (0, "CT-CHASSIS-MIB", "chSlotID"),
    (0, "CT-CHASSIS-MIB", "chSlotCompID"),
)
if mibBuilder.loadTexts:
    chSlotEntry.setStatus("mandatory")
_ChSlotID_Type = Integer32
_ChSlotID_Object = MibTableColumn
chSlotID = _ChSlotID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 5, 1, 1),
    _ChSlotID_Type()
)
chSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSlotID.setStatus("mandatory")
_ChSlotCompID_Type = Integer32
_ChSlotCompID_Object = MibTableColumn
chSlotCompID = _ChSlotCompID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 5, 1, 2),
    _ChSlotCompID_Type()
)
chSlotCompID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSlotCompID.setStatus("mandatory")
_ChSlotClass_Type = ObjectIdentifier
_ChSlotClass_Object = MibTableColumn
chSlotClass = _ChSlotClass_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 5, 1, 3),
    _ChSlotClass_Type()
)
chSlotClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSlotClass.setStatus("mandatory")
_ChSlotModuleType_Type = ObjectIdentifier
_ChSlotModuleType_Object = MibTableColumn
chSlotModuleType = _ChSlotModuleType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 5, 1, 4),
    _ChSlotModuleType_Type()
)
chSlotModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSlotModuleType.setStatus("mandatory")


class _ChSlotModuleName_Type(DisplayString):
    """Custom type chSlotModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ChSlotModuleName_Type.__name__ = "DisplayString"
_ChSlotModuleName_Object = MibTableColumn
chSlotModuleName = _ChSlotModuleName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 5, 1, 5),
    _ChSlotModuleName_Type()
)
chSlotModuleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chSlotModuleName.setStatus("mandatory")


class _ChSlotModuleVersion_Type(DisplayString):
    """Custom type chSlotModuleVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ChSlotModuleVersion_Type.__name__ = "DisplayString"
_ChSlotModuleVersion_Object = MibTableColumn
chSlotModuleVersion = _ChSlotModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 5, 1, 6),
    _ChSlotModuleVersion_Type()
)
chSlotModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSlotModuleVersion.setStatus("mandatory")
_ChSlotModuleTimeStamp_Type = TimeTicks
_ChSlotModuleTimeStamp_Object = MibTableColumn
chSlotModuleTimeStamp = _ChSlotModuleTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 5, 1, 7),
    _ChSlotModuleTimeStamp_Type()
)
chSlotModuleTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSlotModuleTimeStamp.setStatus("mandatory")
_ChCompMIBTable_Object = MibTable
chCompMIBTable = _ChCompMIBTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 6)
)
if mibBuilder.loadTexts:
    chCompMIBTable.setStatus("deprecated")
_ChCompMIBEntry_Object = MibTableRow
chCompMIBEntry = _ChCompMIBEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 6, 1)
)
chCompMIBEntry.setIndexNames(
    (0, "CT-CHASSIS-MIB", "chCompMIBID"),
    (0, "CT-CHASSIS-MIB", "chCompMIBSlotID"),
    (0, "CT-CHASSIS-MIB", "chCompMIBCompID"),
)
if mibBuilder.loadTexts:
    chCompMIBEntry.setStatus("deprecated")
_ChCompMIBID_Type = Integer32
_ChCompMIBID_Object = MibTableColumn
chCompMIBID = _ChCompMIBID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 6, 1, 1),
    _ChCompMIBID_Type()
)
chCompMIBID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chCompMIBID.setStatus("deprecated")
_ChCompMIBSlotID_Type = Integer32
_ChCompMIBSlotID_Object = MibTableColumn
chCompMIBSlotID = _ChCompMIBSlotID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 6, 1, 2),
    _ChCompMIBSlotID_Type()
)
chCompMIBSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chCompMIBSlotID.setStatus("deprecated")
_ChCompMIBCompID_Type = Integer32
_ChCompMIBCompID_Object = MibTableColumn
chCompMIBCompID = _ChCompMIBCompID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 6, 1, 3),
    _ChCompMIBCompID_Type()
)
chCompMIBCompID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chCompMIBCompID.setStatus("deprecated")
_ChCompMIBGrpOID_Type = ObjectIdentifier
_ChCompMIBGrpOID_Object = MibTableColumn
chCompMIBGrpOID = _ChCompMIBGrpOID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 6, 1, 4),
    _ChCompMIBGrpOID_Type()
)
chCompMIBGrpOID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chCompMIBGrpOID.setStatus("deprecated")
_ChCompMIBVectorObjectBase_Type = ObjectIdentifier
_ChCompMIBVectorObjectBase_Object = MibTableColumn
chCompMIBVectorObjectBase = _ChCompMIBVectorObjectBase_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 6, 1, 5),
    _ChCompMIBVectorObjectBase_Type()
)
chCompMIBVectorObjectBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chCompMIBVectorObjectBase.setStatus("deprecated")
_ChCompMIBVectorNum_Type = Integer32
_ChCompMIBVectorNum_Object = MibTableColumn
chCompMIBVectorNum = _ChCompMIBVectorNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 6, 1, 6),
    _ChCompMIBVectorNum_Type()
)
chCompMIBVectorNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chCompMIBVectorNum.setStatus("deprecated")


class _ChCompMIBType_Type(Integer32):
    """Custom type chCompMIBType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("instanced", 2),
          ("not-instanced", 1))
    )


_ChCompMIBType_Type.__name__ = "Integer32"
_ChCompMIBType_Object = MibTableColumn
chCompMIBType = _ChCompMIBType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 6, 1, 7),
    _ChCompMIBType_Type()
)
chCompMIBType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chCompMIBType.setStatus("deprecated")


class _ChCompMIBStatus_Type(Integer32):
    """Custom type chCompMIBStatus based on Integer32"""
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
        *(("agent", 3),
          ("invalid", 2),
          ("management", 4),
          ("unknown", 1))
    )


_ChCompMIBStatus_Type.__name__ = "Integer32"
_ChCompMIBStatus_Object = MibTableColumn
chCompMIBStatus = _ChCompMIBStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 6, 1, 8),
    _ChCompMIBStatus_Type()
)
chCompMIBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chCompMIBStatus.setStatus("deprecated")
_ChPhysicalChanges_Type = Counter32
_ChPhysicalChanges_Object = MibScalar
chPhysicalChanges = _ChPhysicalChanges_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 7),
    _ChPhysicalChanges_Type()
)
chPhysicalChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chPhysicalChanges.setStatus("deprecated")
_ChLogicalChanges_Type = Counter32
_ChLogicalChanges_Object = MibScalar
chLogicalChanges = _ChLogicalChanges_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 8),
    _ChLogicalChanges_Type()
)
chLogicalChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chLogicalChanges.setStatus("deprecated")


class _ChCompGlobalBasicCommStr_Type(OctetString):
    """Custom type chCompGlobalBasicCommStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 27),
    )


_ChCompGlobalBasicCommStr_Type.__name__ = "OctetString"
_ChCompGlobalBasicCommStr_Object = MibScalar
chCompGlobalBasicCommStr = _ChCompGlobalBasicCommStr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 9),
    _ChCompGlobalBasicCommStr_Type()
)
chCompGlobalBasicCommStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chCompGlobalBasicCommStr.setStatus("mandatory")


class _ChCompGlobalROCommStr_Type(OctetString):
    """Custom type chCompGlobalROCommStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 27),
    )


_ChCompGlobalROCommStr_Type.__name__ = "OctetString"
_ChCompGlobalROCommStr_Object = MibScalar
chCompGlobalROCommStr = _ChCompGlobalROCommStr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 10),
    _ChCompGlobalROCommStr_Type()
)
chCompGlobalROCommStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chCompGlobalROCommStr.setStatus("mandatory")


class _ChCompGlobalRWCommStr_Type(OctetString):
    """Custom type chCompGlobalRWCommStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 27),
    )


_ChCompGlobalRWCommStr_Type.__name__ = "OctetString"
_ChCompGlobalRWCommStr_Object = MibScalar
chCompGlobalRWCommStr = _ChCompGlobalRWCommStr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 11),
    _ChCompGlobalRWCommStr_Type()
)
chCompGlobalRWCommStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chCompGlobalRWCommStr.setStatus("mandatory")


class _ChCompGlobalSUCommStr_Type(OctetString):
    """Custom type chCompGlobalSUCommStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 27),
    )


_ChCompGlobalSUCommStr_Type.__name__ = "OctetString"
_ChCompGlobalSUCommStr_Object = MibScalar
chCompGlobalSUCommStr = _ChCompGlobalSUCommStr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2, 12),
    _ChCompGlobalSUCommStr_Type()
)
chCompGlobalSUCommStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chCompGlobalSUCommStr.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CT-CHASSIS-MIB",
    **{"chType": chType,
       "chBackplaneTable": chBackplaneTable,
       "chBackplaneEntry": chBackplaneEntry,
       "chBackplaneID": chBackplaneID,
       "chBackplaneType": chBackplaneType,
       "chNumSlots": chNumSlots,
       "chCompTable": chCompTable,
       "chCompEntry": chCompEntry,
       "chCompID": chCompID,
       "chCompAdminStatus": chCompAdminStatus,
       "chCompArg": chCompArg,
       "chCompType": chCompType,
       "chCompName": chCompName,
       "chCompVersion": chCompVersion,
       "chCompTimeStamp": chCompTimeStamp,
       "chCompAccessPolicy": chCompAccessPolicy,
       "chCompBasicCommStr": chCompBasicCommStr,
       "chCompROCommStr": chCompROCommStr,
       "chCompRWCommStr": chCompRWCommStr,
       "chCompSUCommStr": chCompSUCommStr,
       "chCompNetAdr": chCompNetAdr,
       "chSlotTable": chSlotTable,
       "chSlotEntry": chSlotEntry,
       "chSlotID": chSlotID,
       "chSlotCompID": chSlotCompID,
       "chSlotClass": chSlotClass,
       "chSlotModuleType": chSlotModuleType,
       "chSlotModuleName": chSlotModuleName,
       "chSlotModuleVersion": chSlotModuleVersion,
       "chSlotModuleTimeStamp": chSlotModuleTimeStamp,
       "chCompMIBTable": chCompMIBTable,
       "chCompMIBEntry": chCompMIBEntry,
       "chCompMIBID": chCompMIBID,
       "chCompMIBSlotID": chCompMIBSlotID,
       "chCompMIBCompID": chCompMIBCompID,
       "chCompMIBGrpOID": chCompMIBGrpOID,
       "chCompMIBVectorObjectBase": chCompMIBVectorObjectBase,
       "chCompMIBVectorNum": chCompMIBVectorNum,
       "chCompMIBType": chCompMIBType,
       "chCompMIBStatus": chCompMIBStatus,
       "chPhysicalChanges": chPhysicalChanges,
       "chLogicalChanges": chLogicalChanges,
       "chCompGlobalBasicCommStr": chCompGlobalBasicCommStr,
       "chCompGlobalROCommStr": chCompGlobalROCommStr,
       "chCompGlobalRWCommStr": chCompGlobalRWCommStr,
       "chCompGlobalSUCommStr": chCompGlobalSUCommStr}
)
