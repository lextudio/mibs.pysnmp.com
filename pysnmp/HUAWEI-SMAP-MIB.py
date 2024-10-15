# SNMP MIB module (HUAWEI-SMAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-SMAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:56 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

hwSMAP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 14)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwSmapMibObjects_ObjectIdentity = ObjectIdentity
hwSmapMibObjects = _HwSmapMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 14, 1)
)
_HwSmapTable_Object = MibTable
hwSmapTable = _HwSmapTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 14, 1, 1)
)
if mibBuilder.loadTexts:
    hwSmapTable.setStatus("current")
_HwSmapEntry_Object = MibTableRow
hwSmapEntry = _HwSmapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 14, 1, 1, 1)
)
hwSmapEntry.setIndexNames(
    (0, "HUAWEI-SMAP-MIB", "hwSmapUserPort"),
    (0, "HUAWEI-SMAP-MIB", "hwSmapAcl"),
)
if mibBuilder.loadTexts:
    hwSmapEntry.setStatus("current")


class _HwSmapUserPort_Type(Integer32):
    """Custom type hwSmapUserPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwSmapUserPort_Type.__name__ = "Integer32"
_HwSmapUserPort_Object = MibTableColumn
hwSmapUserPort = _HwSmapUserPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 14, 1, 1, 1, 1),
    _HwSmapUserPort_Type()
)
hwSmapUserPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSmapUserPort.setStatus("current")


class _HwSmapAcl_Type(Integer32):
    """Custom type hwSmapAcl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 2999),
    )


_HwSmapAcl_Type.__name__ = "Integer32"
_HwSmapAcl_Object = MibTableColumn
hwSmapAcl = _HwSmapAcl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 14, 1, 1, 1, 2),
    _HwSmapAcl_Type()
)
hwSmapAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSmapAcl.setStatus("current")


class _HwSmapAppSysPort_Type(Integer32):
    """Custom type hwSmapAppSysPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwSmapAppSysPort_Type.__name__ = "Integer32"
_HwSmapAppSysPort_Object = MibTableColumn
hwSmapAppSysPort = _HwSmapAppSysPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 14, 1, 1, 1, 3),
    _HwSmapAppSysPort_Type()
)
hwSmapAppSysPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSmapAppSysPort.setStatus("current")
_HwSmapStatus_Type = RowStatus
_HwSmapStatus_Object = MibTableColumn
hwSmapStatus = _HwSmapStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 14, 1, 1, 1, 4),
    _HwSmapStatus_Type()
)
hwSmapStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSmapStatus.setStatus("current")
_HwSmapMibConformance_ObjectIdentity = ObjectIdentity
hwSmapMibConformance = _HwSmapMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 14, 2)
)
_HwSmapMibGroup_ObjectIdentity = ObjectIdentity
hwSmapMibGroup = _HwSmapMibGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 14, 2, 1)
)

# Managed Objects groups

hwSmapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 14, 2, 1, 1)
)
hwSmapGroup.setObjects(
      *(("HUAWEI-SMAP-MIB", "hwSmapUserPort"),
        ("HUAWEI-SMAP-MIB", "hwSmapAcl"),
        ("HUAWEI-SMAP-MIB", "hwSmapAppSysPort"),
        ("HUAWEI-SMAP-MIB", "hwSmapStatus"))
)
if mibBuilder.loadTexts:
    hwSmapGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-SMAP-MIB",
    **{"hwSMAP": hwSMAP,
       "hwSmapMibObjects": hwSmapMibObjects,
       "hwSmapTable": hwSmapTable,
       "hwSmapEntry": hwSmapEntry,
       "hwSmapUserPort": hwSmapUserPort,
       "hwSmapAcl": hwSmapAcl,
       "hwSmapAppSysPort": hwSmapAppSysPort,
       "hwSmapStatus": hwSmapStatus,
       "hwSmapMibConformance": hwSmapMibConformance,
       "hwSmapMibGroup": hwSmapMibGroup,
       "hwSmapGroup": hwSmapGroup}
)
