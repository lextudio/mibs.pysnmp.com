# SNMP MIB module (ZHONE-GEN-LINE-REDUNDANCY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHONE-GEN-LINE-REDUNDANCY
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:32 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(zhoneInterfaceGroup,
 zhoneModules) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneInterfaceGroup",
    "zhoneModules")

(ZhoneAdminString,
 ZhoneRowStatus,
 ZhoneShelfValue,
 ZhoneSlotValue) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneAdminString",
    "ZhoneRowStatus",
    "ZhoneShelfValue",
    "ZhoneSlotValue")


# MODULE-IDENTITY

zhoneRedundantLine = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 9)
)
zhoneRedundantLine.setRevisions(
        ("2000-09-12 18:01",
         "2000-10-25 16:46",
         "2000-11-03 19:43",
         "2000-11-06 18:53")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class InterfaceIndexOrZero(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs



class _NextLineGroupId_Type(Integer32):
    """Custom type nextLineGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NextLineGroupId_Type.__name__ = "Integer32"
_NextLineGroupId_Object = MibScalar
nextLineGroupId = _NextLineGroupId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 6, 1),
    _NextLineGroupId_Type()
)
nextLineGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nextLineGroupId.setStatus("current")
_LineProfileTable_Object = MibTable
lineProfileTable = _LineProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 6, 2)
)
if mibBuilder.loadTexts:
    lineProfileTable.setStatus("current")
_LineProfileEntry_Object = MibTableRow
lineProfileEntry = _LineProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 6, 2, 1)
)
lineProfileEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    lineProfileEntry.setStatus("current")
_LpDescription_Type = ZhoneAdminString
_LpDescription_Object = MibTableColumn
lpDescription = _LpDescription_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 6, 2, 1, 1),
    _LpDescription_Type()
)
lpDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDescription.setStatus("current")
_LpPhysicalShelf_Type = ZhoneShelfValue
_LpPhysicalShelf_Object = MibTableColumn
lpPhysicalShelf = _LpPhysicalShelf_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 6, 2, 1, 2),
    _LpPhysicalShelf_Type()
)
lpPhysicalShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpPhysicalShelf.setStatus("current")
_LpPhysicalSlot_Type = ZhoneSlotValue
_LpPhysicalSlot_Object = MibTableColumn
lpPhysicalSlot = _LpPhysicalSlot_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 6, 2, 1, 3),
    _LpPhysicalSlot_Type()
)
lpPhysicalSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpPhysicalSlot.setStatus("current")


class _LpPhysicalPort_Type(Integer32):
    """Custom type lpPhysicalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 262143),
    )


_LpPhysicalPort_Type.__name__ = "Integer32"
_LpPhysicalPort_Object = MibTableColumn
lpPhysicalPort = _LpPhysicalPort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 6, 2, 1, 4),
    _LpPhysicalPort_Type()
)
lpPhysicalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpPhysicalPort.setStatus("current")
_LpPhysicalSubPort_Type = Integer32
_LpPhysicalSubPort_Object = MibTableColumn
lpPhysicalSubPort = _LpPhysicalSubPort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 6, 2, 1, 5),
    _LpPhysicalSubPort_Type()
)
lpPhysicalSubPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpPhysicalSubPort.setStatus("current")
_LpRedundancyGroupId_Type = Integer32
_LpRedundancyGroupId_Object = MibTableColumn
lpRedundancyGroupId = _LpRedundancyGroupId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 6, 2, 1, 6),
    _LpRedundancyGroupId_Type()
)
lpRedundancyGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpRedundancyGroupId.setStatus("current")
_LineGroupTable_Object = MibTable
lineGroupTable = _LineGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 6, 3)
)
if mibBuilder.loadTexts:
    lineGroupTable.setStatus("current")
_LineGroupEntry_Object = MibTableRow
lineGroupEntry = _LineGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 6, 3, 1)
)
lineGroupEntry.setIndexNames(
    (0, "ZHONE-GEN-LINE-REDUNDANCY", "lgId"),
)
if mibBuilder.loadTexts:
    lineGroupEntry.setStatus("current")


class _LgId_Type(Integer32):
    """Custom type lgId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LgId_Type.__name__ = "Integer32"
_LgId_Object = MibTableColumn
lgId = _LgId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 6, 3, 1, 1),
    _LgId_Type()
)
lgId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgId.setStatus("current")
_LgName_Type = ZhoneAdminString
_LgName_Object = MibTableColumn
lgName = _LgName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 6, 3, 1, 2),
    _LgName_Type()
)
lgName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lgName.setStatus("current")


class _LgPrimaryLineId_Type(InterfaceIndexOrZero):
    """Custom type lgPrimaryLineId based on InterfaceIndexOrZero"""
    defaultValue = 0


_LgPrimaryLineId_Object = MibTableColumn
lgPrimaryLineId = _LgPrimaryLineId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 6, 3, 1, 3),
    _LgPrimaryLineId_Type()
)
lgPrimaryLineId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lgPrimaryLineId.setStatus("current")


class _LgPrimaryWeight_Type(Integer32):
    """Custom type lgPrimaryWeight based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_LgPrimaryWeight_Type.__name__ = "Integer32"
_LgPrimaryWeight_Object = MibTableColumn
lgPrimaryWeight = _LgPrimaryWeight_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 6, 3, 1, 4),
    _LgPrimaryWeight_Type()
)
lgPrimaryWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lgPrimaryWeight.setStatus("current")


class _LgSecondaryLineId_Type(InterfaceIndexOrZero):
    """Custom type lgSecondaryLineId based on InterfaceIndexOrZero"""
    defaultValue = 0


_LgSecondaryLineId_Object = MibTableColumn
lgSecondaryLineId = _LgSecondaryLineId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 6, 3, 1, 5),
    _LgSecondaryLineId_Type()
)
lgSecondaryLineId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lgSecondaryLineId.setStatus("current")


class _LgSecondaryWeight_Type(Integer32):
    """Custom type lgSecondaryWeight based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_LgSecondaryWeight_Type.__name__ = "Integer32"
_LgSecondaryWeight_Object = MibTableColumn
lgSecondaryWeight = _LgSecondaryWeight_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 6, 3, 1, 6),
    _LgSecondaryWeight_Type()
)
lgSecondaryWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lgSecondaryWeight.setStatus("current")


class _LgGroupAdminState_Type(Integer32):
    """Custom type lgGroupAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("lockActive", 3),
          ("up", 2))
    )


_LgGroupAdminState_Type.__name__ = "Integer32"
_LgGroupAdminState_Object = MibTableColumn
lgGroupAdminState = _LgGroupAdminState_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 6, 3, 1, 7),
    _LgGroupAdminState_Type()
)
lgGroupAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lgGroupAdminState.setStatus("current")


class _LgGroupOperState_Type(Integer32):
    """Custom type lgGroupOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_LgGroupOperState_Type.__name__ = "Integer32"
_LgGroupOperState_Object = MibTableColumn
lgGroupOperState = _LgGroupOperState_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 6, 3, 1, 8),
    _LgGroupOperState_Type()
)
lgGroupOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgGroupOperState.setStatus("current")
_LgActiveLineId_Type = InterfaceIndex
_LgActiveLineId_Object = MibTableColumn
lgActiveLineId = _LgActiveLineId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 6, 3, 1, 9),
    _LgActiveLineId_Type()
)
lgActiveLineId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgActiveLineId.setStatus("current")
_LgRowStatus_Type = ZhoneRowStatus
_LgRowStatus_Object = MibTableColumn
lgRowStatus = _LgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 6, 3, 1, 10),
    _LgRowStatus_Type()
)
lgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lgRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-GEN-LINE-REDUNDANCY",
    **{"InterfaceIndexOrZero": InterfaceIndexOrZero,
       "nextLineGroupId": nextLineGroupId,
       "lineProfileTable": lineProfileTable,
       "lineProfileEntry": lineProfileEntry,
       "lpDescription": lpDescription,
       "lpPhysicalShelf": lpPhysicalShelf,
       "lpPhysicalSlot": lpPhysicalSlot,
       "lpPhysicalPort": lpPhysicalPort,
       "lpPhysicalSubPort": lpPhysicalSubPort,
       "lpRedundancyGroupId": lpRedundancyGroupId,
       "lineGroupTable": lineGroupTable,
       "lineGroupEntry": lineGroupEntry,
       "lgId": lgId,
       "lgName": lgName,
       "lgPrimaryLineId": lgPrimaryLineId,
       "lgPrimaryWeight": lgPrimaryWeight,
       "lgSecondaryLineId": lgSecondaryLineId,
       "lgSecondaryWeight": lgSecondaryWeight,
       "lgGroupAdminState": lgGroupAdminState,
       "lgGroupOperState": lgGroupOperState,
       "lgActiveLineId": lgActiveLineId,
       "lgRowStatus": lgRowStatus,
       "zhoneRedundantLine": zhoneRedundantLine}
)
