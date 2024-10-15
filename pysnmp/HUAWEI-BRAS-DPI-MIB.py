# SNMP MIB module (HUAWEI-BRAS-DPI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-BRAS-DPI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:58 2024
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

(hwBRASMib,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwBRASMib")

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

hwBRASDpi = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 16)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwDpiPolicyObject_ObjectIdentity = ObjectIdentity
hwDpiPolicyObject = _HwDpiPolicyObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 16, 1)
)
_HwDpiPolicyTable_Object = MibTable
hwDpiPolicyTable = _HwDpiPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 16, 1, 1)
)
if mibBuilder.loadTexts:
    hwDpiPolicyTable.setStatus("current")
_HwDpiPolicyEntry_Object = MibTableRow
hwDpiPolicyEntry = _HwDpiPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 16, 1, 1, 1)
)
hwDpiPolicyEntry.setIndexNames(
    (0, "HUAWEI-BRAS-DPI-MIB", "hwDpiPolicyName"),
)
if mibBuilder.loadTexts:
    hwDpiPolicyEntry.setStatus("current")


class _HwDpiServiceType_Type(Integer32):
    """Custom type hwDpiServiceType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("p2p", 0))
    )


_HwDpiServiceType_Type.__name__ = "Integer32"
_HwDpiServiceType_Object = MibTableColumn
hwDpiServiceType = _HwDpiServiceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 16, 1, 1, 1, 1),
    _HwDpiServiceType_Type()
)
hwDpiServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDpiServiceType.setStatus("current")


class _HwDpiPolicyName_Type(OctetString):
    """Custom type hwDpiPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwDpiPolicyName_Type.__name__ = "OctetString"
_HwDpiPolicyName_Object = MibTableColumn
hwDpiPolicyName = _HwDpiPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 16, 1, 1, 1, 2),
    _HwDpiPolicyName_Type()
)
hwDpiPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDpiPolicyName.setStatus("current")


class _HwDpiUpBehaviorName_Type(OctetString):
    """Custom type hwDpiUpBehaviorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwDpiUpBehaviorName_Type.__name__ = "OctetString"
_HwDpiUpBehaviorName_Object = MibTableColumn
hwDpiUpBehaviorName = _HwDpiUpBehaviorName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 16, 1, 1, 1, 3),
    _HwDpiUpBehaviorName_Type()
)
hwDpiUpBehaviorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDpiUpBehaviorName.setStatus("current")


class _HwDpiDownBehaviorName_Type(OctetString):
    """Custom type hwDpiDownBehaviorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwDpiDownBehaviorName_Type.__name__ = "OctetString"
_HwDpiDownBehaviorName_Object = MibTableColumn
hwDpiDownBehaviorName = _HwDpiDownBehaviorName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 16, 1, 1, 1, 4),
    _HwDpiDownBehaviorName_Type()
)
hwDpiDownBehaviorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDpiDownBehaviorName.setStatus("current")
_HwDpiPolicyRowStatus_Type = RowStatus
_HwDpiPolicyRowStatus_Object = MibTableColumn
hwDpiPolicyRowStatus = _HwDpiPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 16, 1, 1, 1, 5),
    _HwDpiPolicyRowStatus_Type()
)
hwDpiPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDpiPolicyRowStatus.setStatus("current")
_HwDpiBehaviorTable_Object = MibTable
hwDpiBehaviorTable = _HwDpiBehaviorTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 16, 1, 2)
)
if mibBuilder.loadTexts:
    hwDpiBehaviorTable.setStatus("current")
_HwDpiBehaviorEntry_Object = MibTableRow
hwDpiBehaviorEntry = _HwDpiBehaviorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 16, 1, 2, 1)
)
hwDpiBehaviorEntry.setIndexNames(
    (0, "HUAWEI-BRAS-DPI-MIB", "hwDpiBehaviorName"),
)
if mibBuilder.loadTexts:
    hwDpiBehaviorEntry.setStatus("current")


class _HwDpiBehaviorName_Type(OctetString):
    """Custom type hwDpiBehaviorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwDpiBehaviorName_Type.__name__ = "OctetString"
_HwDpiBehaviorName_Object = MibTableColumn
hwDpiBehaviorName = _HwDpiBehaviorName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 16, 1, 2, 1, 1),
    _HwDpiBehaviorName_Type()
)
hwDpiBehaviorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDpiBehaviorName.setStatus("current")


class _HwDpiBehaviorCarCir_Type(Integer32):
    """Custom type hwDpiBehaviorCarCir based on Integer32"""
    defaultValue = 100000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 3000000),
    )


_HwDpiBehaviorCarCir_Type.__name__ = "Integer32"
_HwDpiBehaviorCarCir_Object = MibTableColumn
hwDpiBehaviorCarCir = _HwDpiBehaviorCarCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 16, 1, 2, 1, 2),
    _HwDpiBehaviorCarCir_Type()
)
hwDpiBehaviorCarCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDpiBehaviorCarCir.setStatus("current")
_HwDpiBehaviorRowStatus_Type = RowStatus
_HwDpiBehaviorRowStatus_Object = MibTableColumn
hwDpiBehaviorRowStatus = _HwDpiBehaviorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 16, 1, 2, 1, 3),
    _HwDpiBehaviorRowStatus_Type()
)
hwDpiBehaviorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDpiBehaviorRowStatus.setStatus("current")
_HwDpiConformance_ObjectIdentity = ObjectIdentity
hwDpiConformance = _HwDpiConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 16, 2)
)
_HwDpiCompliances_ObjectIdentity = ObjectIdentity
hwDpiCompliances = _HwDpiCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 16, 2, 1)
)
_HwDpiGroups_ObjectIdentity = ObjectIdentity
hwDpiGroups = _HwDpiGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 16, 2, 2)
)

# Managed Objects groups

hwDpiPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 16, 2, 2, 1)
)
hwDpiPolicyGroup.setObjects(
      *(("HUAWEI-BRAS-DPI-MIB", "hwDpiServiceType"),
        ("HUAWEI-BRAS-DPI-MIB", "hwDpiPolicyName"),
        ("HUAWEI-BRAS-DPI-MIB", "hwDpiUpBehaviorName"),
        ("HUAWEI-BRAS-DPI-MIB", "hwDpiDownBehaviorName"),
        ("HUAWEI-BRAS-DPI-MIB", "hwDpiPolicyRowStatus"))
)
if mibBuilder.loadTexts:
    hwDpiPolicyGroup.setStatus("current")

hwDpiBehaviorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 16, 2, 2, 2)
)
hwDpiBehaviorGroup.setObjects(
      *(("HUAWEI-BRAS-DPI-MIB", "hwDpiBehaviorName"),
        ("HUAWEI-BRAS-DPI-MIB", "hwDpiBehaviorCarCir"),
        ("HUAWEI-BRAS-DPI-MIB", "hwDpiBehaviorRowStatus"))
)
if mibBuilder.loadTexts:
    hwDpiBehaviorGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwDpiCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 16, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwDpiCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-BRAS-DPI-MIB",
    **{"hwBRASDpi": hwBRASDpi,
       "hwDpiPolicyObject": hwDpiPolicyObject,
       "hwDpiPolicyTable": hwDpiPolicyTable,
       "hwDpiPolicyEntry": hwDpiPolicyEntry,
       "hwDpiServiceType": hwDpiServiceType,
       "hwDpiPolicyName": hwDpiPolicyName,
       "hwDpiUpBehaviorName": hwDpiUpBehaviorName,
       "hwDpiDownBehaviorName": hwDpiDownBehaviorName,
       "hwDpiPolicyRowStatus": hwDpiPolicyRowStatus,
       "hwDpiBehaviorTable": hwDpiBehaviorTable,
       "hwDpiBehaviorEntry": hwDpiBehaviorEntry,
       "hwDpiBehaviorName": hwDpiBehaviorName,
       "hwDpiBehaviorCarCir": hwDpiBehaviorCarCir,
       "hwDpiBehaviorRowStatus": hwDpiBehaviorRowStatus,
       "hwDpiConformance": hwDpiConformance,
       "hwDpiCompliances": hwDpiCompliances,
       "hwDpiCompliance": hwDpiCompliance,
       "hwDpiGroups": hwDpiGroups,
       "hwDpiPolicyGroup": hwDpiPolicyGroup,
       "hwDpiBehaviorGroup": hwDpiBehaviorGroup}
)
