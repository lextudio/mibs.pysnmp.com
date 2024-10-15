# SNMP MIB module (HUAWEI-BRAS-GRE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-BRAS-GRE-MIB
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwGRE = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 13)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwhwGREMibObjects_ObjectIdentity = ObjectIdentity
hwhwGREMibObjects = _HwhwGREMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 13, 1)
)
_HwQueryGreGroupTable_Object = MibTable
hwQueryGreGroupTable = _HwQueryGreGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 13, 1, 1)
)
if mibBuilder.loadTexts:
    hwQueryGreGroupTable.setStatus("current")
_HwQueryGreGroupEntry_Object = MibTableRow
hwQueryGreGroupEntry = _HwQueryGreGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 13, 1, 1, 1)
)
hwQueryGreGroupEntry.setIndexNames(
    (0, "HUAWEI-BRAS-GRE-MIB", "hwQueryGreGroupName"),
)
if mibBuilder.loadTexts:
    hwQueryGreGroupEntry.setStatus("current")


class _HwQueryGreGroupName_Type(OctetString):
    """Custom type hwQueryGreGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwQueryGreGroupName_Type.__name__ = "OctetString"
_HwQueryGreGroupName_Object = MibTableColumn
hwQueryGreGroupName = _HwQueryGreGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 13, 1, 1, 1, 1),
    _HwQueryGreGroupName_Type()
)
hwQueryGreGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQueryGreGroupName.setStatus("current")


class _HwQueryGreGroupCounter_Type(Integer32):
    """Custom type hwQueryGreGroupCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_HwQueryGreGroupCounter_Type.__name__ = "Integer32"
_HwQueryGreGroupCounter_Object = MibTableColumn
hwQueryGreGroupCounter = _HwQueryGreGroupCounter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 13, 1, 1, 1, 2),
    _HwQueryGreGroupCounter_Type()
)
hwQueryGreGroupCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQueryGreGroupCounter.setStatus("current")


class _HwQueryGreGroupActiveTunnel_Type(OctetString):
    """Custom type hwQueryGreGroupActiveTunnel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwQueryGreGroupActiveTunnel_Type.__name__ = "OctetString"
_HwQueryGreGroupActiveTunnel_Object = MibTableColumn
hwQueryGreGroupActiveTunnel = _HwQueryGreGroupActiveTunnel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 13, 1, 1, 1, 3),
    _HwQueryGreGroupActiveTunnel_Type()
)
hwQueryGreGroupActiveTunnel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQueryGreGroupActiveTunnel.setStatus("current")


class _HwQueryGreGroupTunnel1Name_Type(OctetString):
    """Custom type hwQueryGreGroupTunnel1Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwQueryGreGroupTunnel1Name_Type.__name__ = "OctetString"
_HwQueryGreGroupTunnel1Name_Object = MibTableColumn
hwQueryGreGroupTunnel1Name = _HwQueryGreGroupTunnel1Name_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 13, 1, 1, 1, 4),
    _HwQueryGreGroupTunnel1Name_Type()
)
hwQueryGreGroupTunnel1Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQueryGreGroupTunnel1Name.setStatus("current")


class _HwQueryGreGroupTunnel2Name_Type(OctetString):
    """Custom type hwQueryGreGroupTunnel2Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwQueryGreGroupTunnel2Name_Type.__name__ = "OctetString"
_HwQueryGreGroupTunnel2Name_Object = MibTableColumn
hwQueryGreGroupTunnel2Name = _HwQueryGreGroupTunnel2Name_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 13, 1, 1, 1, 5),
    _HwQueryGreGroupTunnel2Name_Type()
)
hwQueryGreGroupTunnel2Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQueryGreGroupTunnel2Name.setStatus("current")


class _HwQueryGreGroupTunnel3Name_Type(OctetString):
    """Custom type hwQueryGreGroupTunnel3Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwQueryGreGroupTunnel3Name_Type.__name__ = "OctetString"
_HwQueryGreGroupTunnel3Name_Object = MibTableColumn
hwQueryGreGroupTunnel3Name = _HwQueryGreGroupTunnel3Name_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 13, 1, 1, 1, 6),
    _HwQueryGreGroupTunnel3Name_Type()
)
hwQueryGreGroupTunnel3Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQueryGreGroupTunnel3Name.setStatus("current")


class _HwQueryGreGroupTunnel4Name_Type(OctetString):
    """Custom type hwQueryGreGroupTunnel4Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwQueryGreGroupTunnel4Name_Type.__name__ = "OctetString"
_HwQueryGreGroupTunnel4Name_Object = MibTableColumn
hwQueryGreGroupTunnel4Name = _HwQueryGreGroupTunnel4Name_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 13, 1, 1, 1, 7),
    _HwQueryGreGroupTunnel4Name_Type()
)
hwQueryGreGroupTunnel4Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQueryGreGroupTunnel4Name.setStatus("current")


class _HwQueryGreGroupTunnel1Preference_Type(Integer32):
    """Custom type hwQueryGreGroupTunnel1Preference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwQueryGreGroupTunnel1Preference_Type.__name__ = "Integer32"
_HwQueryGreGroupTunnel1Preference_Object = MibTableColumn
hwQueryGreGroupTunnel1Preference = _HwQueryGreGroupTunnel1Preference_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 13, 1, 1, 1, 8),
    _HwQueryGreGroupTunnel1Preference_Type()
)
hwQueryGreGroupTunnel1Preference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQueryGreGroupTunnel1Preference.setStatus("current")


class _HwQueryGreGroupTunnel2Preference_Type(Integer32):
    """Custom type hwQueryGreGroupTunnel2Preference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwQueryGreGroupTunnel2Preference_Type.__name__ = "Integer32"
_HwQueryGreGroupTunnel2Preference_Object = MibTableColumn
hwQueryGreGroupTunnel2Preference = _HwQueryGreGroupTunnel2Preference_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 13, 1, 1, 1, 9),
    _HwQueryGreGroupTunnel2Preference_Type()
)
hwQueryGreGroupTunnel2Preference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQueryGreGroupTunnel2Preference.setStatus("current")


class _HwQueryGreGroupTunnel3Preference_Type(Integer32):
    """Custom type hwQueryGreGroupTunnel3Preference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwQueryGreGroupTunnel3Preference_Type.__name__ = "Integer32"
_HwQueryGreGroupTunnel3Preference_Object = MibTableColumn
hwQueryGreGroupTunnel3Preference = _HwQueryGreGroupTunnel3Preference_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 13, 1, 1, 1, 10),
    _HwQueryGreGroupTunnel3Preference_Type()
)
hwQueryGreGroupTunnel3Preference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQueryGreGroupTunnel3Preference.setStatus("current")


class _HwQueryGreGroupTunnel4Preference_Type(Integer32):
    """Custom type hwQueryGreGroupTunnel4Preference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwQueryGreGroupTunnel4Preference_Type.__name__ = "Integer32"
_HwQueryGreGroupTunnel4Preference_Object = MibTableColumn
hwQueryGreGroupTunnel4Preference = _HwQueryGreGroupTunnel4Preference_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 13, 1, 1, 1, 11),
    _HwQueryGreGroupTunnel4Preference_Type()
)
hwQueryGreGroupTunnel4Preference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQueryGreGroupTunnel4Preference.setStatus("current")
_HwQueryGreConformance_ObjectIdentity = ObjectIdentity
hwQueryGreConformance = _HwQueryGreConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 13, 2)
)
_HwQueryGreCompliances_ObjectIdentity = ObjectIdentity
hwQueryGreCompliances = _HwQueryGreCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 13, 2, 1)
)
_HwQueryGreGroups_ObjectIdentity = ObjectIdentity
hwQueryGreGroups = _HwQueryGreGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 13, 2, 2)
)

# Managed Objects groups

hwQueryGrePolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 13, 2, 2, 1)
)
hwQueryGrePolicyGroup.setObjects(
      *(("HUAWEI-BRAS-GRE-MIB", "hwQueryGreGroupName"),
        ("HUAWEI-BRAS-GRE-MIB", "hwQueryGreGroupCounter"),
        ("HUAWEI-BRAS-GRE-MIB", "hwQueryGreGroupActiveTunnel"),
        ("HUAWEI-BRAS-GRE-MIB", "hwQueryGreGroupTunnel1Name"),
        ("HUAWEI-BRAS-GRE-MIB", "hwQueryGreGroupTunnel2Name"),
        ("HUAWEI-BRAS-GRE-MIB", "hwQueryGreGroupTunnel3Name"),
        ("HUAWEI-BRAS-GRE-MIB", "hwQueryGreGroupTunnel4Name"),
        ("HUAWEI-BRAS-GRE-MIB", "hwQueryGreGroupTunnel1Preference"),
        ("HUAWEI-BRAS-GRE-MIB", "hwQueryGreGroupTunnel2Preference"),
        ("HUAWEI-BRAS-GRE-MIB", "hwQueryGreGroupTunnel3Preference"),
        ("HUAWEI-BRAS-GRE-MIB", "hwQueryGreGroupTunnel4Preference"))
)
if mibBuilder.loadTexts:
    hwQueryGrePolicyGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwQueryGreCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 13, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwQueryGreCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-BRAS-GRE-MIB",
    **{"hwGRE": hwGRE,
       "hwhwGREMibObjects": hwhwGREMibObjects,
       "hwQueryGreGroupTable": hwQueryGreGroupTable,
       "hwQueryGreGroupEntry": hwQueryGreGroupEntry,
       "hwQueryGreGroupName": hwQueryGreGroupName,
       "hwQueryGreGroupCounter": hwQueryGreGroupCounter,
       "hwQueryGreGroupActiveTunnel": hwQueryGreGroupActiveTunnel,
       "hwQueryGreGroupTunnel1Name": hwQueryGreGroupTunnel1Name,
       "hwQueryGreGroupTunnel2Name": hwQueryGreGroupTunnel2Name,
       "hwQueryGreGroupTunnel3Name": hwQueryGreGroupTunnel3Name,
       "hwQueryGreGroupTunnel4Name": hwQueryGreGroupTunnel4Name,
       "hwQueryGreGroupTunnel1Preference": hwQueryGreGroupTunnel1Preference,
       "hwQueryGreGroupTunnel2Preference": hwQueryGreGroupTunnel2Preference,
       "hwQueryGreGroupTunnel3Preference": hwQueryGreGroupTunnel3Preference,
       "hwQueryGreGroupTunnel4Preference": hwQueryGreGroupTunnel4Preference,
       "hwQueryGreConformance": hwQueryGreConformance,
       "hwQueryGreCompliances": hwQueryGreCompliances,
       "hwQueryGreCompliance": hwQueryGreCompliance,
       "hwQueryGreGroups": hwQueryGreGroups,
       "hwQueryGrePolicyGroup": hwQueryGrePolicyGroup}
)
