# SNMP MIB module (HH3C-MP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-MP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:08 2024
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

(hh3cRhw,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cRhw")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hh3cMultilinkPPP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 33)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cMpObjects_ObjectIdentity = ObjectIdentity
hh3cMpObjects = _Hh3cMpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 33, 1)
)
_Hh3cMpMultilinkTable_Object = MibTable
hh3cMpMultilinkTable = _Hh3cMpMultilinkTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 33, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cMpMultilinkTable.setStatus("current")
_Hh3cMpMultilinkEntry_Object = MibTableRow
hh3cMpMultilinkEntry = _Hh3cMpMultilinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 33, 1, 1, 1)
)
hh3cMpMultilinkEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cMpMultilinkEntry.setStatus("current")
_Hh3cMpMultilinkDescr_Type = DisplayString
_Hh3cMpMultilinkDescr_Object = MibTableColumn
hh3cMpMultilinkDescr = _Hh3cMpMultilinkDescr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 33, 1, 1, 1, 1),
    _Hh3cMpMultilinkDescr_Type()
)
hh3cMpMultilinkDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMpMultilinkDescr.setStatus("current")
_Hh3cMpBundleName_Type = DisplayString
_Hh3cMpBundleName_Object = MibTableColumn
hh3cMpBundleName = _Hh3cMpBundleName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 33, 1, 1, 1, 2),
    _Hh3cMpBundleName_Type()
)
hh3cMpBundleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMpBundleName.setStatus("current")
_Hh3cMpBundledSlot_Type = Integer32
_Hh3cMpBundledSlot_Object = MibTableColumn
hh3cMpBundledSlot = _Hh3cMpBundledSlot_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 33, 1, 1, 1, 3),
    _Hh3cMpBundledSlot_Type()
)
hh3cMpBundledSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMpBundledSlot.setStatus("current")
_Hh3cMpBundledMemberCnt_Type = Integer32
_Hh3cMpBundledMemberCnt_Object = MibTableColumn
hh3cMpBundledMemberCnt = _Hh3cMpBundledMemberCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 33, 1, 1, 1, 4),
    _Hh3cMpBundledMemberCnt_Type()
)
hh3cMpBundledMemberCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMpBundledMemberCnt.setStatus("current")
_Hh3cMpLostFragments_Type = Counter32
_Hh3cMpLostFragments_Object = MibTableColumn
hh3cMpLostFragments = _Hh3cMpLostFragments_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 33, 1, 1, 1, 5),
    _Hh3cMpLostFragments_Type()
)
hh3cMpLostFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMpLostFragments.setStatus("current")
_Hh3cMpReorderedPkts_Type = Counter32
_Hh3cMpReorderedPkts_Object = MibTableColumn
hh3cMpReorderedPkts = _Hh3cMpReorderedPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 33, 1, 1, 1, 6),
    _Hh3cMpReorderedPkts_Type()
)
hh3cMpReorderedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMpReorderedPkts.setStatus("current")
_Hh3cMpUnassignedPkts_Type = Counter32
_Hh3cMpUnassignedPkts_Object = MibTableColumn
hh3cMpUnassignedPkts = _Hh3cMpUnassignedPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 33, 1, 1, 1, 7),
    _Hh3cMpUnassignedPkts_Type()
)
hh3cMpUnassignedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMpUnassignedPkts.setStatus("current")
_Hh3cMpInterleavedPkts_Type = Counter32
_Hh3cMpInterleavedPkts_Object = MibTableColumn
hh3cMpInterleavedPkts = _Hh3cMpInterleavedPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 33, 1, 1, 1, 8),
    _Hh3cMpInterleavedPkts_Type()
)
hh3cMpInterleavedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMpInterleavedPkts.setStatus("current")
_Hh3cMpRcvdSequence_Type = Integer32
_Hh3cMpRcvdSequence_Object = MibTableColumn
hh3cMpRcvdSequence = _Hh3cMpRcvdSequence_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 33, 1, 1, 1, 9),
    _Hh3cMpRcvdSequence_Type()
)
hh3cMpRcvdSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMpRcvdSequence.setStatus("current")
_Hh3cMpSentSequence_Type = Integer32
_Hh3cMpSentSequence_Object = MibTableColumn
hh3cMpSentSequence = _Hh3cMpSentSequence_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 33, 1, 1, 1, 10),
    _Hh3cMpSentSequence_Type()
)
hh3cMpSentSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMpSentSequence.setStatus("current")
_Hh3cMpMemberlinkTable_Object = MibTable
hh3cMpMemberlinkTable = _Hh3cMpMemberlinkTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 33, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cMpMemberlinkTable.setStatus("current")
_Hh3cMpMemberlinkEntry_Object = MibTableRow
hh3cMpMemberlinkEntry = _Hh3cMpMemberlinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 33, 1, 2, 1)
)
hh3cMpMemberlinkEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-MP-MIB", "hh3cMpMemberlinkSeqNumber"),
)
if mibBuilder.loadTexts:
    hh3cMpMemberlinkEntry.setStatus("current")
_Hh3cMpMemberlinkSeqNumber_Type = Integer32
_Hh3cMpMemberlinkSeqNumber_Object = MibTableColumn
hh3cMpMemberlinkSeqNumber = _Hh3cMpMemberlinkSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 33, 1, 2, 1, 1),
    _Hh3cMpMemberlinkSeqNumber_Type()
)
hh3cMpMemberlinkSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMpMemberlinkSeqNumber.setStatus("current")
_Hh3cMpMemberlinkIfIndex_Type = Integer32
_Hh3cMpMemberlinkIfIndex_Object = MibTableColumn
hh3cMpMemberlinkIfIndex = _Hh3cMpMemberlinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 33, 1, 2, 1, 2),
    _Hh3cMpMemberlinkIfIndex_Type()
)
hh3cMpMemberlinkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMpMemberlinkIfIndex.setStatus("current")
_Hh3cMpMemberlinkDescr_Type = DisplayString
_Hh3cMpMemberlinkDescr_Object = MibTableColumn
hh3cMpMemberlinkDescr = _Hh3cMpMemberlinkDescr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 33, 1, 2, 1, 3),
    _Hh3cMpMemberlinkDescr_Type()
)
hh3cMpMemberlinkDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMpMemberlinkDescr.setStatus("current")
_Hh3cMpMemberlinkMpStatus_Type = Integer32
_Hh3cMpMemberlinkMpStatus_Object = MibTableColumn
hh3cMpMemberlinkMpStatus = _Hh3cMpMemberlinkMpStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 33, 1, 2, 1, 4),
    _Hh3cMpMemberlinkMpStatus_Type()
)
hh3cMpMemberlinkMpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMpMemberlinkMpStatus.setStatus("current")
_Hh3cMpNotifications_ObjectIdentity = ObjectIdentity
hh3cMpNotifications = _Hh3cMpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 33, 2)
)
_Hh3cMpConformance_ObjectIdentity = ObjectIdentity
hh3cMpConformance = _Hh3cMpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 33, 3)
)
_Hh3cMpCompliances_ObjectIdentity = ObjectIdentity
hh3cMpCompliances = _Hh3cMpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 33, 3, 1)
)
_Hh3cMpGroups_ObjectIdentity = ObjectIdentity
hh3cMpGroups = _Hh3cMpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 33, 3, 2)
)

# Managed Objects groups

hh3cMpMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 8, 33, 3, 2, 1)
)
hh3cMpMandatoryGroup.setObjects(
      *(("HH3C-MP-MIB", "hh3cMpBundledMemberCnt"),
        ("HH3C-MP-MIB", "hh3cMpMemberlinkSeqNumber"),
        ("HH3C-MP-MIB", "hh3cMpMemberlinkIfIndex"))
)
if mibBuilder.loadTexts:
    hh3cMpMandatoryGroup.setStatus("current")

hh3cMpInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 8, 33, 3, 2, 2)
)
hh3cMpInfoGroup.setObjects(
      *(("HH3C-MP-MIB", "hh3cMpMultilinkDescr"),
        ("HH3C-MP-MIB", "hh3cMpBundleName"),
        ("HH3C-MP-MIB", "hh3cMpBundledSlot"),
        ("HH3C-MP-MIB", "hh3cMpBundledMemberCnt"),
        ("HH3C-MP-MIB", "hh3cMpLostFragments"),
        ("HH3C-MP-MIB", "hh3cMpReorderedPkts"),
        ("HH3C-MP-MIB", "hh3cMpUnassignedPkts"),
        ("HH3C-MP-MIB", "hh3cMpInterleavedPkts"),
        ("HH3C-MP-MIB", "hh3cMpRcvdSequence"),
        ("HH3C-MP-MIB", "hh3cMpSentSequence"),
        ("HH3C-MP-MIB", "hh3cMpMemberlinkDescr"),
        ("HH3C-MP-MIB", "hh3cMpMemberlinkMpStatus"))
)
if mibBuilder.loadTexts:
    hh3cMpInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hh3cMpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25506, 8, 33, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cMpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-MP-MIB",
    **{"hh3cMultilinkPPP": hh3cMultilinkPPP,
       "hh3cMpObjects": hh3cMpObjects,
       "hh3cMpMultilinkTable": hh3cMpMultilinkTable,
       "hh3cMpMultilinkEntry": hh3cMpMultilinkEntry,
       "hh3cMpMultilinkDescr": hh3cMpMultilinkDescr,
       "hh3cMpBundleName": hh3cMpBundleName,
       "hh3cMpBundledSlot": hh3cMpBundledSlot,
       "hh3cMpBundledMemberCnt": hh3cMpBundledMemberCnt,
       "hh3cMpLostFragments": hh3cMpLostFragments,
       "hh3cMpReorderedPkts": hh3cMpReorderedPkts,
       "hh3cMpUnassignedPkts": hh3cMpUnassignedPkts,
       "hh3cMpInterleavedPkts": hh3cMpInterleavedPkts,
       "hh3cMpRcvdSequence": hh3cMpRcvdSequence,
       "hh3cMpSentSequence": hh3cMpSentSequence,
       "hh3cMpMemberlinkTable": hh3cMpMemberlinkTable,
       "hh3cMpMemberlinkEntry": hh3cMpMemberlinkEntry,
       "hh3cMpMemberlinkSeqNumber": hh3cMpMemberlinkSeqNumber,
       "hh3cMpMemberlinkIfIndex": hh3cMpMemberlinkIfIndex,
       "hh3cMpMemberlinkDescr": hh3cMpMemberlinkDescr,
       "hh3cMpMemberlinkMpStatus": hh3cMpMemberlinkMpStatus,
       "hh3cMpNotifications": hh3cMpNotifications,
       "hh3cMpConformance": hh3cMpConformance,
       "hh3cMpCompliances": hh3cMpCompliances,
       "hh3cMpCompliance": hh3cMpCompliance,
       "hh3cMpGroups": hh3cMpGroups,
       "hh3cMpMandatoryGroup": hh3cMpMandatoryGroup,
       "hh3cMpInfoGroup": hh3cMpInfoGroup}
)
