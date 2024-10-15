# SNMP MIB module (HPN-ICF-MP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-MP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:07 2024
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

(hpnicfRhw,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfRhw")

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

hpnicfMultilinkPPP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 33)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfMpObjects_ObjectIdentity = ObjectIdentity
hpnicfMpObjects = _HpnicfMpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 33, 1)
)
_HpnicfMpMultilinkTable_Object = MibTable
hpnicfMpMultilinkTable = _HpnicfMpMultilinkTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 33, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfMpMultilinkTable.setStatus("current")
_HpnicfMpMultilinkEntry_Object = MibTableRow
hpnicfMpMultilinkEntry = _HpnicfMpMultilinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 33, 1, 1, 1)
)
hpnicfMpMultilinkEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfMpMultilinkEntry.setStatus("current")
_HpnicfMpMultilinkDescr_Type = DisplayString
_HpnicfMpMultilinkDescr_Object = MibTableColumn
hpnicfMpMultilinkDescr = _HpnicfMpMultilinkDescr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 33, 1, 1, 1, 1),
    _HpnicfMpMultilinkDescr_Type()
)
hpnicfMpMultilinkDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMpMultilinkDescr.setStatus("current")
_HpnicfMpBundleName_Type = DisplayString
_HpnicfMpBundleName_Object = MibTableColumn
hpnicfMpBundleName = _HpnicfMpBundleName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 33, 1, 1, 1, 2),
    _HpnicfMpBundleName_Type()
)
hpnicfMpBundleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMpBundleName.setStatus("current")
_HpnicfMpBundledSlot_Type = Integer32
_HpnicfMpBundledSlot_Object = MibTableColumn
hpnicfMpBundledSlot = _HpnicfMpBundledSlot_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 33, 1, 1, 1, 3),
    _HpnicfMpBundledSlot_Type()
)
hpnicfMpBundledSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMpBundledSlot.setStatus("current")
_HpnicfMpBundledMemberCnt_Type = Integer32
_HpnicfMpBundledMemberCnt_Object = MibTableColumn
hpnicfMpBundledMemberCnt = _HpnicfMpBundledMemberCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 33, 1, 1, 1, 4),
    _HpnicfMpBundledMemberCnt_Type()
)
hpnicfMpBundledMemberCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMpBundledMemberCnt.setStatus("current")
_HpnicfMpLostFragments_Type = Counter32
_HpnicfMpLostFragments_Object = MibTableColumn
hpnicfMpLostFragments = _HpnicfMpLostFragments_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 33, 1, 1, 1, 5),
    _HpnicfMpLostFragments_Type()
)
hpnicfMpLostFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMpLostFragments.setStatus("current")
_HpnicfMpReorderedPkts_Type = Counter32
_HpnicfMpReorderedPkts_Object = MibTableColumn
hpnicfMpReorderedPkts = _HpnicfMpReorderedPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 33, 1, 1, 1, 6),
    _HpnicfMpReorderedPkts_Type()
)
hpnicfMpReorderedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMpReorderedPkts.setStatus("current")
_HpnicfMpUnassignedPkts_Type = Counter32
_HpnicfMpUnassignedPkts_Object = MibTableColumn
hpnicfMpUnassignedPkts = _HpnicfMpUnassignedPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 33, 1, 1, 1, 7),
    _HpnicfMpUnassignedPkts_Type()
)
hpnicfMpUnassignedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMpUnassignedPkts.setStatus("current")
_HpnicfMpInterleavedPkts_Type = Counter32
_HpnicfMpInterleavedPkts_Object = MibTableColumn
hpnicfMpInterleavedPkts = _HpnicfMpInterleavedPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 33, 1, 1, 1, 8),
    _HpnicfMpInterleavedPkts_Type()
)
hpnicfMpInterleavedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMpInterleavedPkts.setStatus("current")
_HpnicfMpRcvdSequence_Type = Integer32
_HpnicfMpRcvdSequence_Object = MibTableColumn
hpnicfMpRcvdSequence = _HpnicfMpRcvdSequence_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 33, 1, 1, 1, 9),
    _HpnicfMpRcvdSequence_Type()
)
hpnicfMpRcvdSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMpRcvdSequence.setStatus("current")
_HpnicfMpSentSequence_Type = Integer32
_HpnicfMpSentSequence_Object = MibTableColumn
hpnicfMpSentSequence = _HpnicfMpSentSequence_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 33, 1, 1, 1, 10),
    _HpnicfMpSentSequence_Type()
)
hpnicfMpSentSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMpSentSequence.setStatus("current")
_HpnicfMpMemberlinkTable_Object = MibTable
hpnicfMpMemberlinkTable = _HpnicfMpMemberlinkTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 33, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfMpMemberlinkTable.setStatus("current")
_HpnicfMpMemberlinkEntry_Object = MibTableRow
hpnicfMpMemberlinkEntry = _HpnicfMpMemberlinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 33, 1, 2, 1)
)
hpnicfMpMemberlinkEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-MP-MIB", "hpnicfMpMemberlinkSeqNumber"),
)
if mibBuilder.loadTexts:
    hpnicfMpMemberlinkEntry.setStatus("current")
_HpnicfMpMemberlinkSeqNumber_Type = Integer32
_HpnicfMpMemberlinkSeqNumber_Object = MibTableColumn
hpnicfMpMemberlinkSeqNumber = _HpnicfMpMemberlinkSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 33, 1, 2, 1, 1),
    _HpnicfMpMemberlinkSeqNumber_Type()
)
hpnicfMpMemberlinkSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMpMemberlinkSeqNumber.setStatus("current")
_HpnicfMpMemberlinkIfIndex_Type = Integer32
_HpnicfMpMemberlinkIfIndex_Object = MibTableColumn
hpnicfMpMemberlinkIfIndex = _HpnicfMpMemberlinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 33, 1, 2, 1, 2),
    _HpnicfMpMemberlinkIfIndex_Type()
)
hpnicfMpMemberlinkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMpMemberlinkIfIndex.setStatus("current")
_HpnicfMpMemberlinkDescr_Type = DisplayString
_HpnicfMpMemberlinkDescr_Object = MibTableColumn
hpnicfMpMemberlinkDescr = _HpnicfMpMemberlinkDescr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 33, 1, 2, 1, 3),
    _HpnicfMpMemberlinkDescr_Type()
)
hpnicfMpMemberlinkDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMpMemberlinkDescr.setStatus("current")
_HpnicfMpMemberlinkMpStatus_Type = Integer32
_HpnicfMpMemberlinkMpStatus_Object = MibTableColumn
hpnicfMpMemberlinkMpStatus = _HpnicfMpMemberlinkMpStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 33, 1, 2, 1, 4),
    _HpnicfMpMemberlinkMpStatus_Type()
)
hpnicfMpMemberlinkMpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMpMemberlinkMpStatus.setStatus("current")
_HpnicfMpNotifications_ObjectIdentity = ObjectIdentity
hpnicfMpNotifications = _HpnicfMpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 33, 2)
)
_HpnicfMpConformance_ObjectIdentity = ObjectIdentity
hpnicfMpConformance = _HpnicfMpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 33, 3)
)
_HpnicfMpCompliances_ObjectIdentity = ObjectIdentity
hpnicfMpCompliances = _HpnicfMpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 33, 3, 1)
)
_HpnicfMpGroups_ObjectIdentity = ObjectIdentity
hpnicfMpGroups = _HpnicfMpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 33, 3, 2)
)

# Managed Objects groups

hpnicfMpMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 33, 3, 2, 1)
)
hpnicfMpMandatoryGroup.setObjects(
      *(("HPN-ICF-MP-MIB", "hpnicfMpBundledMemberCnt"),
        ("HPN-ICF-MP-MIB", "hpnicfMpMemberlinkSeqNumber"),
        ("HPN-ICF-MP-MIB", "hpnicfMpMemberlinkIfIndex"))
)
if mibBuilder.loadTexts:
    hpnicfMpMandatoryGroup.setStatus("current")

hpnicfMpInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 33, 3, 2, 2)
)
hpnicfMpInfoGroup.setObjects(
      *(("HPN-ICF-MP-MIB", "hpnicfMpMultilinkDescr"),
        ("HPN-ICF-MP-MIB", "hpnicfMpBundleName"),
        ("HPN-ICF-MP-MIB", "hpnicfMpBundledSlot"),
        ("HPN-ICF-MP-MIB", "hpnicfMpBundledMemberCnt"),
        ("HPN-ICF-MP-MIB", "hpnicfMpLostFragments"),
        ("HPN-ICF-MP-MIB", "hpnicfMpReorderedPkts"),
        ("HPN-ICF-MP-MIB", "hpnicfMpUnassignedPkts"),
        ("HPN-ICF-MP-MIB", "hpnicfMpInterleavedPkts"),
        ("HPN-ICF-MP-MIB", "hpnicfMpRcvdSequence"),
        ("HPN-ICF-MP-MIB", "hpnicfMpSentSequence"),
        ("HPN-ICF-MP-MIB", "hpnicfMpMemberlinkDescr"),
        ("HPN-ICF-MP-MIB", "hpnicfMpMemberlinkMpStatus"))
)
if mibBuilder.loadTexts:
    hpnicfMpInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpnicfMpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 33, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfMpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-MP-MIB",
    **{"hpnicfMultilinkPPP": hpnicfMultilinkPPP,
       "hpnicfMpObjects": hpnicfMpObjects,
       "hpnicfMpMultilinkTable": hpnicfMpMultilinkTable,
       "hpnicfMpMultilinkEntry": hpnicfMpMultilinkEntry,
       "hpnicfMpMultilinkDescr": hpnicfMpMultilinkDescr,
       "hpnicfMpBundleName": hpnicfMpBundleName,
       "hpnicfMpBundledSlot": hpnicfMpBundledSlot,
       "hpnicfMpBundledMemberCnt": hpnicfMpBundledMemberCnt,
       "hpnicfMpLostFragments": hpnicfMpLostFragments,
       "hpnicfMpReorderedPkts": hpnicfMpReorderedPkts,
       "hpnicfMpUnassignedPkts": hpnicfMpUnassignedPkts,
       "hpnicfMpInterleavedPkts": hpnicfMpInterleavedPkts,
       "hpnicfMpRcvdSequence": hpnicfMpRcvdSequence,
       "hpnicfMpSentSequence": hpnicfMpSentSequence,
       "hpnicfMpMemberlinkTable": hpnicfMpMemberlinkTable,
       "hpnicfMpMemberlinkEntry": hpnicfMpMemberlinkEntry,
       "hpnicfMpMemberlinkSeqNumber": hpnicfMpMemberlinkSeqNumber,
       "hpnicfMpMemberlinkIfIndex": hpnicfMpMemberlinkIfIndex,
       "hpnicfMpMemberlinkDescr": hpnicfMpMemberlinkDescr,
       "hpnicfMpMemberlinkMpStatus": hpnicfMpMemberlinkMpStatus,
       "hpnicfMpNotifications": hpnicfMpNotifications,
       "hpnicfMpConformance": hpnicfMpConformance,
       "hpnicfMpCompliances": hpnicfMpCompliances,
       "hpnicfMpCompliance": hpnicfMpCompliance,
       "hpnicfMpGroups": hpnicfMpGroups,
       "hpnicfMpMandatoryGroup": hpnicfMpMandatoryGroup,
       "hpnicfMpInfoGroup": hpnicfMpInfoGroup}
)
