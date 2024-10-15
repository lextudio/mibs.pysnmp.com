# SNMP MIB module (HP-ICF-CHAIN) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-CHAIN
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:10 2024
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

(hpicfCommon,
 hpicfCommonTrapsPrefix,
 hpicfObjectModules) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpicfCommon",
    "hpicfCommonTrapsPrefix",
    "hpicfObjectModules")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

hpicfChainMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 2)
)
hpicfChainMib.setRevisions(
        ("2000-11-03 22:16",
         "1997-03-06 03:33",
         "1996-09-10 02:08",
         "1994-02-25 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfChainConformance_ObjectIdentity = ObjectIdentity
hpicfChainConformance = _HpicfChainConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 2, 1)
)
_HpicfChainCompliances_ObjectIdentity = ObjectIdentity
hpicfChainCompliances = _HpicfChainCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 2, 1, 1)
)
_HpicfChainGroups_ObjectIdentity = ObjectIdentity
hpicfChainGroups = _HpicfChainGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 2, 1, 2)
)
_HpicfChain_ObjectIdentity = ObjectIdentity
hpicfChain = _HpicfChain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 1)
)


class _HpicfChainMaxMembers_Type(Integer32):
    """Custom type hpicfChainMaxMembers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HpicfChainMaxMembers_Type.__name__ = "Integer32"
_HpicfChainMaxMembers_Object = MibScalar
hpicfChainMaxMembers = _HpicfChainMaxMembers_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 1, 1),
    _HpicfChainMaxMembers_Type()
)
hpicfChainMaxMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfChainMaxMembers.setStatus("current")


class _HpicfChainCurMembers_Type(Integer32):
    """Custom type hpicfChainCurMembers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HpicfChainCurMembers_Type.__name__ = "Integer32"
_HpicfChainCurMembers_Object = MibScalar
hpicfChainCurMembers = _HpicfChainCurMembers_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 1, 2),
    _HpicfChainCurMembers_Type()
)
hpicfChainCurMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfChainCurMembers.setStatus("current")
_HpicfChainLastChange_Type = TimeStamp
_HpicfChainLastChange_Object = MibScalar
hpicfChainLastChange = _HpicfChainLastChange_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 1, 3),
    _HpicfChainLastChange_Type()
)
hpicfChainLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfChainLastChange.setStatus("current")
_HpicfChainChanges_Type = Counter32
_HpicfChainChanges_Object = MibScalar
hpicfChainChanges = _HpicfChainChanges_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 1, 4),
    _HpicfChainChanges_Type()
)
hpicfChainChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfChainChanges.setStatus("current")
_HpicfChainTable_Object = MibTable
hpicfChainTable = _HpicfChainTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 1, 5)
)
if mibBuilder.loadTexts:
    hpicfChainTable.setStatus("current")
_HpicfChainEntry_Object = MibTableRow
hpicfChainEntry = _HpicfChainEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 1, 5, 1)
)
hpicfChainEntry.setIndexNames(
    (0, "HP-ICF-CHAIN", "hpicfChainId"),
)
if mibBuilder.loadTexts:
    hpicfChainEntry.setStatus("current")


class _HpicfChainId_Type(OctetString):
    """Custom type hpicfChainId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_HpicfChainId_Type.__name__ = "OctetString"
_HpicfChainId_Object = MibTableColumn
hpicfChainId = _HpicfChainId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 1, 5, 1, 1),
    _HpicfChainId_Type()
)
hpicfChainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfChainId.setStatus("current")
_HpicfChainObjectId_Type = ObjectIdentifier
_HpicfChainObjectId_Object = MibTableColumn
hpicfChainObjectId = _HpicfChainObjectId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 1, 5, 1, 2),
    _HpicfChainObjectId_Type()
)
hpicfChainObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfChainObjectId.setStatus("current")
_HpicfChainTimestamp_Type = TimeStamp
_HpicfChainTimestamp_Object = MibTableColumn
hpicfChainTimestamp = _HpicfChainTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 1, 5, 1, 3),
    _HpicfChainTimestamp_Type()
)
hpicfChainTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfChainTimestamp.setStatus("current")
_HpicfChainHasAgent_Type = TruthValue
_HpicfChainHasAgent_Object = MibTableColumn
hpicfChainHasAgent = _HpicfChainHasAgent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 1, 5, 1, 4),
    _HpicfChainHasAgent_Type()
)
hpicfChainHasAgent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfChainHasAgent.setStatus("current")
_HpicfChainThisBox_Type = TruthValue
_HpicfChainThisBox_Object = MibTableColumn
hpicfChainThisBox = _HpicfChainThisBox_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 1, 5, 1, 5),
    _HpicfChainThisBox_Type()
)
hpicfChainThisBox.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfChainThisBox.setStatus("current")


class _HpicfChainLocation_Type(Integer32):
    """Custom type hpicfChainLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpicfChainLocation_Type.__name__ = "Integer32"
_HpicfChainLocation_Object = MibTableColumn
hpicfChainLocation = _HpicfChainLocation_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 1, 5, 1, 6),
    _HpicfChainLocation_Type()
)
hpicfChainLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfChainLocation.setStatus("current")
_HpicfChainViewTable_Object = MibTable
hpicfChainViewTable = _HpicfChainViewTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 1, 6)
)
if mibBuilder.loadTexts:
    hpicfChainViewTable.setStatus("current")
_HpicfChainViewEntry_Object = MibTableRow
hpicfChainViewEntry = _HpicfChainViewEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 1, 6, 1)
)
hpicfChainViewEntry.setIndexNames(
    (0, "HP-ICF-CHAIN", "hpicfChainViewId"),
)
if mibBuilder.loadTexts:
    hpicfChainViewEntry.setStatus("current")


class _HpicfChainViewId_Type(OctetString):
    """Custom type hpicfChainViewId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_HpicfChainViewId_Type.__name__ = "OctetString"
_HpicfChainViewId_Object = MibTableColumn
hpicfChainViewId = _HpicfChainViewId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 1, 6, 1, 1),
    _HpicfChainViewId_Type()
)
hpicfChainViewId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfChainViewId.setStatus("current")


class _HpicfChainViewName_Type(DisplayString):
    """Custom type hpicfChainViewName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_HpicfChainViewName_Type.__name__ = "DisplayString"
_HpicfChainViewName_Object = MibTableColumn
hpicfChainViewName = _HpicfChainViewName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 1, 6, 1, 2),
    _HpicfChainViewName_Type()
)
hpicfChainViewName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfChainViewName.setStatus("current")

# Managed Objects groups

hpicfChainingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 2, 1, 2, 1)
)
hpicfChainingGroup.setObjects(
      *(("HP-ICF-CHAIN", "hpicfChainMaxMembers"),
        ("HP-ICF-CHAIN", "hpicfChainCurMembers"),
        ("HP-ICF-CHAIN", "hpicfChainLastChange"),
        ("HP-ICF-CHAIN", "hpicfChainChanges"),
        ("HP-ICF-CHAIN", "hpicfChainId"),
        ("HP-ICF-CHAIN", "hpicfChainObjectId"),
        ("HP-ICF-CHAIN", "hpicfChainTimestamp"),
        ("HP-ICF-CHAIN", "hpicfChainHasAgent"),
        ("HP-ICF-CHAIN", "hpicfChainThisBox"),
        ("HP-ICF-CHAIN", "hpicfChainLocation"),
        ("HP-ICF-CHAIN", "hpicfChainViewId"),
        ("HP-ICF-CHAIN", "hpicfChainViewName"))
)
if mibBuilder.loadTexts:
    hpicfChainingGroup.setStatus("current")


# Notification objects

hpicfChainAddition = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 12, 1, 0, 1)
)
hpicfChainAddition.setObjects(
    ("HP-ICF-CHAIN", "hpicfChainId")
)
if mibBuilder.loadTexts:
    hpicfChainAddition.setStatus(
        "deprecated"
    )

hpicfChainRemoval = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 12, 1, 0, 2)
)
hpicfChainRemoval.setObjects(
    ("HP-ICF-CHAIN", "hpicfChainId")
)
if mibBuilder.loadTexts:
    hpicfChainRemoval.setStatus(
        "current"
    )


# Notifications groups

hpicfChainTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 2, 1, 2, 2)
)
hpicfChainTrapGroup.setObjects(
      *(("HP-ICF-CHAIN", "hpicfChainAddition"),
        ("HP-ICF-CHAIN", "hpicfChainRemoval"))
)
if mibBuilder.loadTexts:
    hpicfChainTrapGroup.setStatus(
        "obsolete"
    )

hpicfChainNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 2, 1, 2, 3)
)
hpicfChainNotifyGroup.setObjects(
    ("HP-ICF-CHAIN", "hpicfChainRemoval")
)
if mibBuilder.loadTexts:
    hpicfChainNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpicfChainingCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfChainingCompliance.setStatus(
        "obsolete"
    )

hpicfChainingCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfChainingCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-CHAIN",
    **{"hpicfChainMib": hpicfChainMib,
       "hpicfChainConformance": hpicfChainConformance,
       "hpicfChainCompliances": hpicfChainCompliances,
       "hpicfChainingCompliance": hpicfChainingCompliance,
       "hpicfChainingCompliance2": hpicfChainingCompliance2,
       "hpicfChainGroups": hpicfChainGroups,
       "hpicfChainingGroup": hpicfChainingGroup,
       "hpicfChainTrapGroup": hpicfChainTrapGroup,
       "hpicfChainNotifyGroup": hpicfChainNotifyGroup,
       "hpicfChain": hpicfChain,
       "hpicfChainMaxMembers": hpicfChainMaxMembers,
       "hpicfChainCurMembers": hpicfChainCurMembers,
       "hpicfChainLastChange": hpicfChainLastChange,
       "hpicfChainChanges": hpicfChainChanges,
       "hpicfChainTable": hpicfChainTable,
       "hpicfChainEntry": hpicfChainEntry,
       "hpicfChainId": hpicfChainId,
       "hpicfChainObjectId": hpicfChainObjectId,
       "hpicfChainTimestamp": hpicfChainTimestamp,
       "hpicfChainHasAgent": hpicfChainHasAgent,
       "hpicfChainThisBox": hpicfChainThisBox,
       "hpicfChainLocation": hpicfChainLocation,
       "hpicfChainViewTable": hpicfChainViewTable,
       "hpicfChainViewEntry": hpicfChainViewEntry,
       "hpicfChainViewId": hpicfChainViewId,
       "hpicfChainViewName": hpicfChainViewName,
       "hpicfChainAddition": hpicfChainAddition,
       "hpicfChainRemoval": hpicfChainRemoval}
)
