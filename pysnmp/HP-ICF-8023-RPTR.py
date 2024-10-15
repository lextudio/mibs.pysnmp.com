# SNMP MIB module (HP-ICF-8023-RPTR) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-8023-RPTR
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:02 2024
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

(hp,
 hpicf8023RptrTrapsPrefix,
 hpicfObjectModules,
 hpicfRepeater) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hp",
    "hpicf8023RptrTrapsPrefix",
    "hpicfObjectModules",
    "hpicfRepeater")

(rpMauGroupIndex,
 rpMauIndex,
 rpMauMediaAvailable,
 rpMauPortIndex) = mibBuilder.importSymbols(
    "MAU-MIB",
    "rpMauGroupIndex",
    "rpMauIndex",
    "rpMauMediaAvailable",
    "rpMauPortIndex")

(rptrPortAutoPartitionState,) = mibBuilder.importSymbols(
    "SNMP-REPEATER-MIB",
    "rptrPortAutoPartitionState")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpicf8023RptrMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 9)
)
hpicf8023RptrMib.setRevisions(
        ("2000-11-03 22:10",
         "1998-07-16 20:27",
         "1996-09-10 02:19",
         "1994-02-25 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hpicf8023RptrConformance_ObjectIdentity = ObjectIdentity
hpicf8023RptrConformance = _Hpicf8023RptrConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 9, 1)
)
_Hpicf8023RptrCompliances_ObjectIdentity = ObjectIdentity
hpicf8023RptrCompliances = _Hpicf8023RptrCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 9, 1, 1)
)
_Hpicf8023RptrGroups_ObjectIdentity = ObjectIdentity
hpicf8023RptrGroups = _Hpicf8023RptrGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 9, 1, 2)
)
_HpRptrBasic_ObjectIdentity = ObjectIdentity
hpRptrBasic = _HpRptrBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1)
)
_HpRptrBasicGlobal_ObjectIdentity = ObjectIdentity
hpRptrBasicGlobal = _HpRptrBasicGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 1)
)


class _HpRptrEntityName_Type(DisplayString):
    """Custom type hpRptrEntityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_HpRptrEntityName_Type.__name__ = "DisplayString"
_HpRptrEntityName_Object = MibScalar
hpRptrEntityName = _HpRptrEntityName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 1, 1),
    _HpRptrEntityName_Type()
)
hpRptrEntityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrEntityName.setStatus("deprecated")
_HpRptrThinlanFault_Type = TruthValue
_HpRptrThinlanFault_Object = MibScalar
hpRptrThinlanFault = _HpRptrThinlanFault_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 1, 2),
    _HpRptrThinlanFault_Type()
)
hpRptrThinlanFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpRptrThinlanFault.setStatus("deprecated")
_HpRptrSqeEnabled_Type = TruthValue
_HpRptrSqeEnabled_Object = MibScalar
hpRptrSqeEnabled = _HpRptrSqeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 1, 3),
    _HpRptrSqeEnabled_Type()
)
hpRptrSqeEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrSqeEnabled.setStatus("deprecated")
_HpRptrRobustHealing_Type = TruthValue
_HpRptrRobustHealing_Object = MibScalar
hpRptrRobustHealing = _HpRptrRobustHealing_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 1, 4),
    _HpRptrRobustHealing_Type()
)
hpRptrRobustHealing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpRptrRobustHealing.setStatus("deprecated")
_HpRptrBasicGroup_ObjectIdentity = ObjectIdentity
hpRptrBasicGroup = _HpRptrBasicGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 2)
)
_HpRptrBasicGroupTable_Object = MibTable
hpRptrBasicGroupTable = _HpRptrBasicGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpRptrBasicGroupTable.setStatus("deprecated")
_HpRptrBasicGroupEntry_Object = MibTableRow
hpRptrBasicGroupEntry = _HpRptrBasicGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 2, 1, 1)
)
hpRptrBasicGroupEntry.setIndexNames(
    (0, "HP-ICF-8023-RPTR", "hpRptrGrpGroupIndex"),
)
if mibBuilder.loadTexts:
    hpRptrBasicGroupEntry.setStatus("deprecated")


class _HpRptrGrpGroupIndex_Type(Integer32):
    """Custom type hpRptrGrpGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpRptrGrpGroupIndex_Type.__name__ = "Integer32"
_HpRptrGrpGroupIndex_Object = MibTableColumn
hpRptrGrpGroupIndex = _HpRptrGrpGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 2, 1, 1, 1),
    _HpRptrGrpGroupIndex_Type()
)
hpRptrGrpGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrGrpGroupIndex.setStatus("deprecated")


class _HpRptrGrpPortsAdminStatus_Type(OctetString):
    """Custom type hpRptrGrpPortsAdminStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HpRptrGrpPortsAdminStatus_Type.__name__ = "OctetString"
_HpRptrGrpPortsAdminStatus_Object = MibTableColumn
hpRptrGrpPortsAdminStatus = _HpRptrGrpPortsAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 2, 1, 1, 2),
    _HpRptrGrpPortsAdminStatus_Type()
)
hpRptrGrpPortsAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrGrpPortsAdminStatus.setStatus("deprecated")


class _HpRptrGrpPortsSegStatus_Type(OctetString):
    """Custom type hpRptrGrpPortsSegStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HpRptrGrpPortsSegStatus_Type.__name__ = "OctetString"
_HpRptrGrpPortsSegStatus_Object = MibTableColumn
hpRptrGrpPortsSegStatus = _HpRptrGrpPortsSegStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 2, 1, 1, 3),
    _HpRptrGrpPortsSegStatus_Type()
)
hpRptrGrpPortsSegStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrGrpPortsSegStatus.setStatus("deprecated")


class _HpRptrGrpPortsMediaAvailable_Type(OctetString):
    """Custom type hpRptrGrpPortsMediaAvailable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HpRptrGrpPortsMediaAvailable_Type.__name__ = "OctetString"
_HpRptrGrpPortsMediaAvailable_Object = MibTableColumn
hpRptrGrpPortsMediaAvailable = _HpRptrGrpPortsMediaAvailable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 2, 1, 1, 4),
    _HpRptrGrpPortsMediaAvailable_Type()
)
hpRptrGrpPortsMediaAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrGrpPortsMediaAvailable.setStatus("deprecated")


class _HpRptrGrpPortsLinkbeatEnabled_Type(OctetString):
    """Custom type hpRptrGrpPortsLinkbeatEnabled based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HpRptrGrpPortsLinkbeatEnabled_Type.__name__ = "OctetString"
_HpRptrGrpPortsLinkbeatEnabled_Object = MibTableColumn
hpRptrGrpPortsLinkbeatEnabled = _HpRptrGrpPortsLinkbeatEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 2, 1, 1, 5),
    _HpRptrGrpPortsLinkbeatEnabled_Type()
)
hpRptrGrpPortsLinkbeatEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrGrpPortsLinkbeatEnabled.setStatus("deprecated")


class _HpRptrGrpPortsOperStatus_Type(OctetString):
    """Custom type hpRptrGrpPortsOperStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HpRptrGrpPortsOperStatus_Type.__name__ = "OctetString"
_HpRptrGrpPortsOperStatus_Object = MibTableColumn
hpRptrGrpPortsOperStatus = _HpRptrGrpPortsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 2, 1, 1, 6),
    _HpRptrGrpPortsOperStatus_Type()
)
hpRptrGrpPortsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrGrpPortsOperStatus.setStatus("deprecated")
_HpRptrBasicPort_ObjectIdentity = ObjectIdentity
hpRptrBasicPort = _HpRptrBasicPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 3)
)
_HpRptrBasicPtTable_Object = MibTable
hpRptrBasicPtTable = _HpRptrBasicPtTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hpRptrBasicPtTable.setStatus("current")
_HpRptrBasicPtEntry_Object = MibTableRow
hpRptrBasicPtEntry = _HpRptrBasicPtEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 3, 1, 1)
)
hpRptrBasicPtEntry.setIndexNames(
    (0, "HP-ICF-8023-RPTR", "hpRptrPtGroupIndex"),
    (0, "HP-ICF-8023-RPTR", "hpRptrPtPortIndex"),
)
if mibBuilder.loadTexts:
    hpRptrBasicPtEntry.setStatus("current")


class _HpRptrPtGroupIndex_Type(Integer32):
    """Custom type hpRptrPtGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpRptrPtGroupIndex_Type.__name__ = "Integer32"
_HpRptrPtGroupIndex_Object = MibTableColumn
hpRptrPtGroupIndex = _HpRptrPtGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 3, 1, 1, 1),
    _HpRptrPtGroupIndex_Type()
)
hpRptrPtGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrPtGroupIndex.setStatus("current")


class _HpRptrPtPortIndex_Type(Integer32):
    """Custom type hpRptrPtPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpRptrPtPortIndex_Type.__name__ = "Integer32"
_HpRptrPtPortIndex_Object = MibTableColumn
hpRptrPtPortIndex = _HpRptrPtPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 3, 1, 1, 2),
    _HpRptrPtPortIndex_Type()
)
hpRptrPtPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrPtPortIndex.setStatus("current")
_HpRptrPtLinkbeatEnable_Type = TruthValue
_HpRptrPtLinkbeatEnable_Object = MibTableColumn
hpRptrPtLinkbeatEnable = _HpRptrPtLinkbeatEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 3, 1, 1, 3),
    _HpRptrPtLinkbeatEnable_Type()
)
hpRptrPtLinkbeatEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpRptrPtLinkbeatEnable.setStatus("current")
_HpRptrPtPolarityReversed_Type = TruthValue
_HpRptrPtPolarityReversed_Object = MibTableColumn
hpRptrPtPolarityReversed = _HpRptrPtPolarityReversed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 3, 1, 1, 4),
    _HpRptrPtPolarityReversed_Type()
)
hpRptrPtPolarityReversed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrPtPolarityReversed.setStatus("current")
_HpRptrPtSqeEnabled_Type = TruthValue
_HpRptrPtSqeEnabled_Object = MibTableColumn
hpRptrPtSqeEnabled = _HpRptrPtSqeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 3, 1, 1, 5),
    _HpRptrPtSqeEnabled_Type()
)
hpRptrPtSqeEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrPtSqeEnabled.setStatus("current")
_HpRptrPtMediaAvailTrapEnable_Type = TruthValue
_HpRptrPtMediaAvailTrapEnable_Object = MibTableColumn
hpRptrPtMediaAvailTrapEnable = _HpRptrPtMediaAvailTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 3, 1, 1, 6),
    _HpRptrPtMediaAvailTrapEnable_Type()
)
hpRptrPtMediaAvailTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpRptrPtMediaAvailTrapEnable.setStatus("current")
_HpRptrPtLongCableEnable_Type = TruthValue
_HpRptrPtLongCableEnable_Object = MibTableColumn
hpRptrPtLongCableEnable = _HpRptrPtLongCableEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 3, 1, 1, 7),
    _HpRptrPtLongCableEnable_Type()
)
hpRptrPtLongCableEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpRptrPtLongCableEnable.setStatus("current")
_HpRptrMonitor_ObjectIdentity = ObjectIdentity
hpRptrMonitor = _HpRptrMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2)
)
_HpRptrMonitorGlobal_ObjectIdentity = ObjectIdentity
hpRptrMonitorGlobal = _HpRptrMonitorGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1)
)
_HpRptrMonCounters_ObjectIdentity = ObjectIdentity
hpRptrMonCounters = _HpRptrMonCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1)
)
_HpRptrMonGlobalFrames_Type = Counter32
_HpRptrMonGlobalFrames_Object = MibScalar
hpRptrMonGlobalFrames = _HpRptrMonGlobalFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1, 1),
    _HpRptrMonGlobalFrames_Type()
)
hpRptrMonGlobalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrMonGlobalFrames.setStatus("deprecated")
_HpRptrMonGlobalOctets_Type = Counter32
_HpRptrMonGlobalOctets_Object = MibScalar
hpRptrMonGlobalOctets = _HpRptrMonGlobalOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1, 2),
    _HpRptrMonGlobalOctets_Type()
)
hpRptrMonGlobalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrMonGlobalOctets.setStatus("deprecated")
_HpRptrMonGlobalFCSErrors_Type = Counter32
_HpRptrMonGlobalFCSErrors_Object = MibScalar
hpRptrMonGlobalFCSErrors = _HpRptrMonGlobalFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1, 3),
    _HpRptrMonGlobalFCSErrors_Type()
)
hpRptrMonGlobalFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrMonGlobalFCSErrors.setStatus("deprecated")
_HpRptrMonGlobalAlignmentErrors_Type = Counter32
_HpRptrMonGlobalAlignmentErrors_Object = MibScalar
hpRptrMonGlobalAlignmentErrors = _HpRptrMonGlobalAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1, 4),
    _HpRptrMonGlobalAlignmentErrors_Type()
)
hpRptrMonGlobalAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrMonGlobalAlignmentErrors.setStatus("deprecated")
_HpRptrMonGlobalFrameTooLongs_Type = Counter32
_HpRptrMonGlobalFrameTooLongs_Object = MibScalar
hpRptrMonGlobalFrameTooLongs = _HpRptrMonGlobalFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1, 5),
    _HpRptrMonGlobalFrameTooLongs_Type()
)
hpRptrMonGlobalFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrMonGlobalFrameTooLongs.setStatus("deprecated")
_HpRptrMonGlobalShortEvents_Type = Counter32
_HpRptrMonGlobalShortEvents_Object = MibScalar
hpRptrMonGlobalShortEvents = _HpRptrMonGlobalShortEvents_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1, 6),
    _HpRptrMonGlobalShortEvents_Type()
)
hpRptrMonGlobalShortEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrMonGlobalShortEvents.setStatus("deprecated")
_HpRptrMonGlobalRunts_Type = Counter32
_HpRptrMonGlobalRunts_Object = MibScalar
hpRptrMonGlobalRunts = _HpRptrMonGlobalRunts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1, 7),
    _HpRptrMonGlobalRunts_Type()
)
hpRptrMonGlobalRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrMonGlobalRunts.setStatus("deprecated")
_HpRptrMonGlobalCollisions_Type = Counter32
_HpRptrMonGlobalCollisions_Object = MibScalar
hpRptrMonGlobalCollisions = _HpRptrMonGlobalCollisions_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1, 8),
    _HpRptrMonGlobalCollisions_Type()
)
hpRptrMonGlobalCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrMonGlobalCollisions.setStatus("deprecated")
_HpRptrMonGlobalLateEvents_Type = Counter32
_HpRptrMonGlobalLateEvents_Object = MibScalar
hpRptrMonGlobalLateEvents = _HpRptrMonGlobalLateEvents_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1, 9),
    _HpRptrMonGlobalLateEvents_Type()
)
hpRptrMonGlobalLateEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrMonGlobalLateEvents.setStatus("deprecated")
_HpRptrMonGlobalVeryLongEvents_Type = Counter32
_HpRptrMonGlobalVeryLongEvents_Object = MibScalar
hpRptrMonGlobalVeryLongEvents = _HpRptrMonGlobalVeryLongEvents_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1, 10),
    _HpRptrMonGlobalVeryLongEvents_Type()
)
hpRptrMonGlobalVeryLongEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrMonGlobalVeryLongEvents.setStatus("deprecated")
_HpRptrMonGlobalDataRateMismatches_Type = Counter32
_HpRptrMonGlobalDataRateMismatches_Object = MibScalar
hpRptrMonGlobalDataRateMismatches = _HpRptrMonGlobalDataRateMismatches_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1, 11),
    _HpRptrMonGlobalDataRateMismatches_Type()
)
hpRptrMonGlobalDataRateMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrMonGlobalDataRateMismatches.setStatus("deprecated")
_HpRptrMonGlobalAutoPartitions_Type = Counter32
_HpRptrMonGlobalAutoPartitions_Object = MibScalar
hpRptrMonGlobalAutoPartitions = _HpRptrMonGlobalAutoPartitions_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1, 12),
    _HpRptrMonGlobalAutoPartitions_Type()
)
hpRptrMonGlobalAutoPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrMonGlobalAutoPartitions.setStatus("deprecated")
_HpRptrMonGlobalErrors_Type = Counter32
_HpRptrMonGlobalErrors_Object = MibScalar
hpRptrMonGlobalErrors = _HpRptrMonGlobalErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1, 13),
    _HpRptrMonGlobalErrors_Type()
)
hpRptrMonGlobalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrMonGlobalErrors.setStatus("deprecated")
_HpRptrMonGlobalUcastPackets_Type = Counter32
_HpRptrMonGlobalUcastPackets_Object = MibScalar
hpRptrMonGlobalUcastPackets = _HpRptrMonGlobalUcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1, 14),
    _HpRptrMonGlobalUcastPackets_Type()
)
hpRptrMonGlobalUcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrMonGlobalUcastPackets.setStatus("deprecated")
_HpRptrMonGlobalBcastPackets_Type = Counter32
_HpRptrMonGlobalBcastPackets_Object = MibScalar
hpRptrMonGlobalBcastPackets = _HpRptrMonGlobalBcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1, 15),
    _HpRptrMonGlobalBcastPackets_Type()
)
hpRptrMonGlobalBcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrMonGlobalBcastPackets.setStatus("deprecated")
_HpRptrMonGlobalMcastPackets_Type = Counter32
_HpRptrMonGlobalMcastPackets_Object = MibScalar
hpRptrMonGlobalMcastPackets = _HpRptrMonGlobalMcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1, 16),
    _HpRptrMonGlobalMcastPackets_Type()
)
hpRptrMonGlobalMcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrMonGlobalMcastPackets.setStatus("deprecated")
_HpRptrMonitorGroup_ObjectIdentity = ObjectIdentity
hpRptrMonitorGroup = _HpRptrMonitorGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 2)
)
_HpRptrMonitorPort_ObjectIdentity = ObjectIdentity
hpRptrMonitorPort = _HpRptrMonitorPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 3)
)
_HpRptrMonPtTable_Object = MibTable
hpRptrMonPtTable = _HpRptrMonPtTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    hpRptrMonPtTable.setStatus("current")
_HpRptrMonPtEntry_Object = MibTableRow
hpRptrMonPtEntry = _HpRptrMonPtEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 3, 1, 1)
)
hpRptrMonPtEntry.setIndexNames(
    (0, "HP-ICF-8023-RPTR", "hpRptrMonPtGroupIndex"),
    (0, "HP-ICF-8023-RPTR", "hpRptrMonPtPortIndex"),
)
if mibBuilder.loadTexts:
    hpRptrMonPtEntry.setStatus("current")


class _HpRptrMonPtGroupIndex_Type(Integer32):
    """Custom type hpRptrMonPtGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpRptrMonPtGroupIndex_Type.__name__ = "Integer32"
_HpRptrMonPtGroupIndex_Object = MibTableColumn
hpRptrMonPtGroupIndex = _HpRptrMonPtGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 3, 1, 1, 1),
    _HpRptrMonPtGroupIndex_Type()
)
hpRptrMonPtGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrMonPtGroupIndex.setStatus("current")


class _HpRptrMonPtPortIndex_Type(Integer32):
    """Custom type hpRptrMonPtPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpRptrMonPtPortIndex_Type.__name__ = "Integer32"
_HpRptrMonPtPortIndex_Object = MibTableColumn
hpRptrMonPtPortIndex = _HpRptrMonPtPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 3, 1, 1, 2),
    _HpRptrMonPtPortIndex_Type()
)
hpRptrMonPtPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrMonPtPortIndex.setStatus("current")
_HpRptrMonPtUcastPackets_Type = Counter32
_HpRptrMonPtUcastPackets_Object = MibTableColumn
hpRptrMonPtUcastPackets = _HpRptrMonPtUcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 3, 1, 1, 3),
    _HpRptrMonPtUcastPackets_Type()
)
hpRptrMonPtUcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrMonPtUcastPackets.setStatus("current")
_HpRptrMonPtBcastPackets_Type = Counter32
_HpRptrMonPtBcastPackets_Object = MibTableColumn
hpRptrMonPtBcastPackets = _HpRptrMonPtBcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 3, 1, 1, 4),
    _HpRptrMonPtBcastPackets_Type()
)
hpRptrMonPtBcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrMonPtBcastPackets.setStatus("current")
_HpRptrMonPtMcastPackets_Type = Counter32
_HpRptrMonPtMcastPackets_Object = MibTableColumn
hpRptrMonPtMcastPackets = _HpRptrMonPtMcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 3, 1, 1, 5),
    _HpRptrMonPtMcastPackets_Type()
)
hpRptrMonPtMcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrMonPtMcastPackets.setStatus("current")
_HpRpMauGroup_ObjectIdentity = ObjectIdentity
hpRpMauGroup = _HpRpMauGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 4)
)
_HpRpMauTable_Object = MibTable
hpRpMauTable = _HpRpMauTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 4, 1)
)
if mibBuilder.loadTexts:
    hpRpMauTable.setStatus("current")
_HpRpMauEntry_Object = MibTableRow
hpRpMauEntry = _HpRpMauEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 4, 1, 1)
)
hpRpMauEntry.setIndexNames(
    (0, "MAU-MIB", "rpMauGroupIndex"),
    (0, "MAU-MIB", "rpMauPortIndex"),
    (0, "MAU-MIB", "rpMauIndex"),
)
if mibBuilder.loadTexts:
    hpRpMauEntry.setStatus("current")


class _HpRpMauTypeList_Type(Bits):
    """Custom type hpRpMauTypeList based on Bits"""
    namedValues = NamedValues(
        *(("b100baseFXFD", 18),
          ("b100baseFXHD", 17),
          ("b100baseT2FD", 20),
          ("b100baseT2HD", 19),
          ("b100baseT4", 14),
          ("b100baseTXFD", 16),
          ("b100baseTXHD", 15),
          ("b10base2", 4),
          ("b10base5", 2),
          ("b10baseFB", 7),
          ("b10baseFL", 8),
          ("b10baseFLFD", 13),
          ("b10baseFLHD", 12),
          ("b10baseFP", 6),
          ("b10baseT", 5),
          ("b10baseTFD", 11),
          ("b10baseTHD", 10),
          ("b10broad36", 9),
          ("bAUI", 1),
          ("bFoirl", 3),
          ("bOther", 0))
    )

_HpRpMauTypeList_Type.__name__ = "Bits"
_HpRpMauTypeList_Object = MibTableColumn
hpRpMauTypeList = _HpRpMauTypeList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 4, 1, 1, 1),
    _HpRpMauTypeList_Type()
)
hpRpMauTypeList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRpMauTypeList.setStatus("current")
_HpRpMauAutoNegSupported_Type = TruthValue
_HpRpMauAutoNegSupported_Object = MibTableColumn
hpRpMauAutoNegSupported = _HpRpMauAutoNegSupported_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 4, 1, 1, 2),
    _HpRpMauAutoNegSupported_Type()
)
hpRpMauAutoNegSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRpMauAutoNegSupported.setStatus("current")


class _HpRpMauAutoNegAdminStatus_Type(Integer32):
    """Custom type hpRpMauAutoNegAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoNegotiate", 1),
          ("forceTo100TXHD", 2),
          ("forceTo10THD", 3))
    )


_HpRpMauAutoNegAdminStatus_Type.__name__ = "Integer32"
_HpRpMauAutoNegAdminStatus_Object = MibTableColumn
hpRpMauAutoNegAdminStatus = _HpRpMauAutoNegAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 4, 1, 1, 3),
    _HpRpMauAutoNegAdminStatus_Type()
)
hpRpMauAutoNegAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpRpMauAutoNegAdminStatus.setStatus("current")


class _HpRpMauAutoNegRemoteSignaling_Type(Integer32):
    """Custom type hpRpMauAutoNegRemoteSignaling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("detected", 1),
          ("notdetected", 2))
    )


_HpRpMauAutoNegRemoteSignaling_Type.__name__ = "Integer32"
_HpRpMauAutoNegRemoteSignaling_Object = MibTableColumn
hpRpMauAutoNegRemoteSignaling = _HpRpMauAutoNegRemoteSignaling_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 4, 1, 1, 4),
    _HpRpMauAutoNegRemoteSignaling_Type()
)
hpRpMauAutoNegRemoteSignaling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRpMauAutoNegRemoteSignaling.setStatus("current")


class _HpRpMauAutoNegConfig_Type(Integer32):
    """Custom type hpRpMauAutoNegConfig based on Integer32"""
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
        *(("complete", 3),
          ("configuring", 2),
          ("disabled", 4),
          ("other", 1),
          ("parallelDetectFail", 5))
    )


_HpRpMauAutoNegConfig_Type.__name__ = "Integer32"
_HpRpMauAutoNegConfig_Object = MibTableColumn
hpRpMauAutoNegConfig = _HpRpMauAutoNegConfig_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 4, 1, 1, 5),
    _HpRpMauAutoNegConfig_Type()
)
hpRpMauAutoNegConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRpMauAutoNegConfig.setStatus("current")


class _HpRpMauAutoNegCapReceived_Type(Bits):
    """Custom type hpRpMauAutoNegCapReceived based on Bits"""
    namedValues = NamedValues(
        *(("b100baseT2", 6),
          ("b100baseT2FD", 7),
          ("b100baseT4", 3),
          ("b100baseTX", 4),
          ("b100baseTXFD", 5),
          ("b10baseT", 1),
          ("b10baseTFD", 2),
          ("bOther", 0))
    )

_HpRpMauAutoNegCapReceived_Type.__name__ = "Bits"
_HpRpMauAutoNegCapReceived_Object = MibTableColumn
hpRpMauAutoNegCapReceived = _HpRpMauAutoNegCapReceived_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 4, 1, 1, 6),
    _HpRpMauAutoNegCapReceived_Type()
)
hpRpMauAutoNegCapReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRpMauAutoNegCapReceived.setStatus("current")


class _HpRpMauAutoNegRestart_Type(Integer32):
    """Custom type hpRpMauAutoNegRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("norestart", 2),
          ("restart", 1))
    )


_HpRpMauAutoNegRestart_Type.__name__ = "Integer32"
_HpRpMauAutoNegRestart_Object = MibTableColumn
hpRpMauAutoNegRestart = _HpRpMauAutoNegRestart_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 4, 1, 1, 7),
    _HpRpMauAutoNegRestart_Type()
)
hpRpMauAutoNegRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpRpMauAutoNegRestart.setStatus("current")

# Managed Objects groups

hpicf8023RptrBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 9, 1, 2, 1)
)
hpicf8023RptrBasicGroup.setObjects(
      *(("HP-ICF-8023-RPTR", "hpRptrEntityName"),
        ("HP-ICF-8023-RPTR", "hpRptrThinlanFault"),
        ("HP-ICF-8023-RPTR", "hpRptrSqeEnabled"),
        ("HP-ICF-8023-RPTR", "hpRptrRobustHealing"),
        ("HP-ICF-8023-RPTR", "hpRptrGrpGroupIndex"),
        ("HP-ICF-8023-RPTR", "hpRptrGrpPortsAdminStatus"),
        ("HP-ICF-8023-RPTR", "hpRptrGrpPortsSegStatus"),
        ("HP-ICF-8023-RPTR", "hpRptrGrpPortsMediaAvailable"),
        ("HP-ICF-8023-RPTR", "hpRptrGrpPortsLinkbeatEnabled"),
        ("HP-ICF-8023-RPTR", "hpRptrGrpPortsOperStatus"),
        ("HP-ICF-8023-RPTR", "hpRptrPtGroupIndex"),
        ("HP-ICF-8023-RPTR", "hpRptrPtPortIndex"),
        ("HP-ICF-8023-RPTR", "hpRptrPtLinkbeatEnable"),
        ("HP-ICF-8023-RPTR", "hpRptrPtPolarityReversed"))
)
if mibBuilder.loadTexts:
    hpicf8023RptrBasicGroup.setStatus("deprecated")

hpicf8023RptrBasicSlaveGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 9, 1, 2, 2)
)
hpicf8023RptrBasicSlaveGroup.setObjects(
      *(("HP-ICF-8023-RPTR", "hpRptrEntityName"),
        ("HP-ICF-8023-RPTR", "hpRptrThinlanFault"),
        ("HP-ICF-8023-RPTR", "hpRptrSqeEnabled"),
        ("HP-ICF-8023-RPTR", "hpRptrGrpGroupIndex"),
        ("HP-ICF-8023-RPTR", "hpRptrGrpPortsAdminStatus"),
        ("HP-ICF-8023-RPTR", "hpRptrGrpPortsSegStatus"),
        ("HP-ICF-8023-RPTR", "hpRptrGrpPortsMediaAvailable"),
        ("HP-ICF-8023-RPTR", "hpRptrGrpPortsLinkbeatEnabled"),
        ("HP-ICF-8023-RPTR", "hpRptrGrpPortsOperStatus"),
        ("HP-ICF-8023-RPTR", "hpRptrPtGroupIndex"),
        ("HP-ICF-8023-RPTR", "hpRptrPtPortIndex"),
        ("HP-ICF-8023-RPTR", "hpRptrPtLinkbeatEnable"),
        ("HP-ICF-8023-RPTR", "hpRptrPtPolarityReversed"))
)
if mibBuilder.loadTexts:
    hpicf8023RptrBasicSlaveGroup.setStatus("deprecated")

hpicf8023RptrMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 9, 1, 2, 3)
)
hpicf8023RptrMonitorGroup.setObjects(
      *(("HP-ICF-8023-RPTR", "hpRptrMonGlobalFrames"),
        ("HP-ICF-8023-RPTR", "hpRptrMonGlobalOctets"),
        ("HP-ICF-8023-RPTR", "hpRptrMonGlobalFCSErrors"),
        ("HP-ICF-8023-RPTR", "hpRptrMonGlobalAlignmentErrors"),
        ("HP-ICF-8023-RPTR", "hpRptrMonGlobalFrameTooLongs"),
        ("HP-ICF-8023-RPTR", "hpRptrMonGlobalShortEvents"),
        ("HP-ICF-8023-RPTR", "hpRptrMonGlobalRunts"),
        ("HP-ICF-8023-RPTR", "hpRptrMonGlobalCollisions"),
        ("HP-ICF-8023-RPTR", "hpRptrMonGlobalLateEvents"),
        ("HP-ICF-8023-RPTR", "hpRptrMonGlobalVeryLongEvents"),
        ("HP-ICF-8023-RPTR", "hpRptrMonGlobalDataRateMismatches"),
        ("HP-ICF-8023-RPTR", "hpRptrMonGlobalAutoPartitions"),
        ("HP-ICF-8023-RPTR", "hpRptrMonGlobalErrors"),
        ("HP-ICF-8023-RPTR", "hpRptrMonGlobalUcastPackets"),
        ("HP-ICF-8023-RPTR", "hpRptrMonGlobalBcastPackets"),
        ("HP-ICF-8023-RPTR", "hpRptrMonGlobalMcastPackets"),
        ("HP-ICF-8023-RPTR", "hpRptrMonPtGroupIndex"),
        ("HP-ICF-8023-RPTR", "hpRptrMonPtPortIndex"),
        ("HP-ICF-8023-RPTR", "hpRptrMonPtUcastPackets"),
        ("HP-ICF-8023-RPTR", "hpRptrMonPtBcastPackets"),
        ("HP-ICF-8023-RPTR", "hpRptrMonPtMcastPackets"))
)
if mibBuilder.loadTexts:
    hpicf8023RptrMonitorGroup.setStatus("deprecated")

hpicf8023RptrMonitorSlaveGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 9, 1, 2, 4)
)
hpicf8023RptrMonitorSlaveGroup.setObjects(
      *(("HP-ICF-8023-RPTR", "hpRptrMonGlobalFrames"),
        ("HP-ICF-8023-RPTR", "hpRptrMonGlobalOctets"),
        ("HP-ICF-8023-RPTR", "hpRptrMonGlobalFCSErrors"),
        ("HP-ICF-8023-RPTR", "hpRptrMonGlobalAlignmentErrors"),
        ("HP-ICF-8023-RPTR", "hpRptrMonGlobalFrameTooLongs"),
        ("HP-ICF-8023-RPTR", "hpRptrMonGlobalShortEvents"),
        ("HP-ICF-8023-RPTR", "hpRptrMonGlobalRunts"),
        ("HP-ICF-8023-RPTR", "hpRptrMonGlobalCollisions"),
        ("HP-ICF-8023-RPTR", "hpRptrMonGlobalLateEvents"),
        ("HP-ICF-8023-RPTR", "hpRptrMonGlobalVeryLongEvents"),
        ("HP-ICF-8023-RPTR", "hpRptrMonGlobalDataRateMismatches"),
        ("HP-ICF-8023-RPTR", "hpRptrMonGlobalAutoPartitions"),
        ("HP-ICF-8023-RPTR", "hpRptrMonGlobalErrors"))
)
if mibBuilder.loadTexts:
    hpicf8023RptrMonitorSlaveGroup.setStatus("deprecated")

hpicf8023MultiRptrBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 9, 1, 2, 5)
)
hpicf8023MultiRptrBasicGroup.setObjects(
      *(("HP-ICF-8023-RPTR", "hpRptrPtGroupIndex"),
        ("HP-ICF-8023-RPTR", "hpRptrPtPortIndex"),
        ("HP-ICF-8023-RPTR", "hpRptrPtLinkbeatEnable"),
        ("HP-ICF-8023-RPTR", "hpRptrPtPolarityReversed"),
        ("HP-ICF-8023-RPTR", "hpRptrPtSqeEnabled"),
        ("HP-ICF-8023-RPTR", "hpRptrPtMediaAvailTrapEnable"),
        ("HP-ICF-8023-RPTR", "hpRptrPtLongCableEnable"))
)
if mibBuilder.loadTexts:
    hpicf8023MultiRptrBasicGroup.setStatus("current")

hpicf8023MultiRptrMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 9, 1, 2, 6)
)
hpicf8023MultiRptrMonitorGroup.setObjects(
      *(("HP-ICF-8023-RPTR", "hpRptrMonPtGroupIndex"),
        ("HP-ICF-8023-RPTR", "hpRptrMonPtPortIndex"),
        ("HP-ICF-8023-RPTR", "hpRptrMonPtUcastPackets"),
        ("HP-ICF-8023-RPTR", "hpRptrMonPtBcastPackets"),
        ("HP-ICF-8023-RPTR", "hpRptrMonPtMcastPackets"))
)
if mibBuilder.loadTexts:
    hpicf8023MultiRptrMonitorGroup.setStatus("current")

hpicf8023RpMauAutoNegGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 9, 1, 2, 9)
)
hpicf8023RpMauAutoNegGroup.setObjects(
      *(("HP-ICF-8023-RPTR", "hpRpMauTypeList"),
        ("HP-ICF-8023-RPTR", "hpRpMauAutoNegSupported"),
        ("HP-ICF-8023-RPTR", "hpRpMauAutoNegAdminStatus"),
        ("HP-ICF-8023-RPTR", "hpRpMauAutoNegRemoteSignaling"),
        ("HP-ICF-8023-RPTR", "hpRpMauAutoNegConfig"),
        ("HP-ICF-8023-RPTR", "hpRpMauAutoNegCapReceived"),
        ("HP-ICF-8023-RPTR", "hpRpMauAutoNegRestart"))
)
if mibBuilder.loadTexts:
    hpicf8023RpMauAutoNegGroup.setStatus("current")

hpicf8023Rptr100BasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 9, 1, 2, 10)
)
hpicf8023Rptr100BasicGroup.setObjects(
      *(("HP-ICF-8023-RPTR", "hpRptrPtGroupIndex"),
        ("HP-ICF-8023-RPTR", "hpRptrPtPortIndex"),
        ("HP-ICF-8023-RPTR", "hpRptrPtPolarityReversed"),
        ("HP-ICF-8023-RPTR", "hpRptrPtMediaAvailTrapEnable"))
)
if mibBuilder.loadTexts:
    hpicf8023Rptr100BasicGroup.setStatus("current")


# Notification objects

hpicfLinkBeatTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 12, 2, 0, 1)
)
hpicfLinkBeatTrap.setObjects(
    ("MAU-MIB", "rpMauMediaAvailable")
)
if mibBuilder.loadTexts:
    hpicfLinkBeatTrap.setStatus(
        "deprecated"
    )

hpicfPartitionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 12, 2, 0, 2)
)
hpicfPartitionTrap.setObjects(
    ("SNMP-REPEATER-MIB", "rptrPortAutoPartitionState")
)
if mibBuilder.loadTexts:
    hpicfPartitionTrap.setStatus(
        "deprecated"
    )

hpicfMediaAvailDetectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 12, 2, 0, 3)
)
hpicfMediaAvailDetectTrap.setObjects(
    ("MAU-MIB", "rpMauMediaAvailable")
)
if mibBuilder.loadTexts:
    hpicfMediaAvailDetectTrap.setStatus(
        "current"
    )

hpicfMediaAvailLostTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 12, 2, 0, 4)
)
hpicfMediaAvailLostTrap.setObjects(
    ("MAU-MIB", "rpMauMediaAvailable")
)
if mibBuilder.loadTexts:
    hpicfMediaAvailLostTrap.setStatus(
        "current"
    )

hpicfPortPartitionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 12, 2, 0, 5)
)
hpicfPortPartitionTrap.setObjects(
    ("SNMP-REPEATER-MIB", "rptrPortAutoPartitionState")
)
if mibBuilder.loadTexts:
    hpicfPortPartitionTrap.setStatus(
        "current"
    )

hpicfPortHealTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 12, 2, 0, 6)
)
hpicfPortHealTrap.setObjects(
    ("SNMP-REPEATER-MIB", "rptrPortAutoPartitionState")
)
if mibBuilder.loadTexts:
    hpicfPortHealTrap.setStatus(
        "current"
    )


# Notifications groups

hpicf8023RptrNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 9, 1, 2, 7)
)
hpicf8023RptrNotifyGroup.setObjects(
      *(("HP-ICF-8023-RPTR", "hpicfLinkBeatTrap"),
        ("HP-ICF-8023-RPTR", "hpicfPartitionTrap"))
)
if mibBuilder.loadTexts:
    hpicf8023RptrNotifyGroup.setStatus(
        "deprecated"
    )

hpicf8023MultiRptrNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 9, 1, 2, 8)
)
hpicf8023MultiRptrNotifyGroup.setObjects(
      *(("HP-ICF-8023-RPTR", "hpicfMediaAvailDetectTrap"),
        ("HP-ICF-8023-RPTR", "hpicfMediaAvailLostTrap"),
        ("HP-ICF-8023-RPTR", "hpicfPortPartitionTrap"),
        ("HP-ICF-8023-RPTR", "hpicfPortHealTrap"))
)
if mibBuilder.loadTexts:
    hpicf8023MultiRptrNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpicf8023RptrCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 9, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpicf8023RptrCompliance.setStatus(
        "deprecated"
    )

hpicf8023RptrSlaveCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 9, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpicf8023RptrSlaveCompliance.setStatus(
        "deprecated"
    )

hpicf8023MultiRptrCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 9, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hpicf8023MultiRptrCompliance.setStatus(
        "current"
    )

hpicf8023RptrAutoNegCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 9, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hpicf8023RptrAutoNegCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-8023-RPTR",
    **{"hpicf8023RptrMib": hpicf8023RptrMib,
       "hpicf8023RptrConformance": hpicf8023RptrConformance,
       "hpicf8023RptrCompliances": hpicf8023RptrCompliances,
       "hpicf8023RptrCompliance": hpicf8023RptrCompliance,
       "hpicf8023RptrSlaveCompliance": hpicf8023RptrSlaveCompliance,
       "hpicf8023MultiRptrCompliance": hpicf8023MultiRptrCompliance,
       "hpicf8023RptrAutoNegCompliance": hpicf8023RptrAutoNegCompliance,
       "hpicf8023RptrGroups": hpicf8023RptrGroups,
       "hpicf8023RptrBasicGroup": hpicf8023RptrBasicGroup,
       "hpicf8023RptrBasicSlaveGroup": hpicf8023RptrBasicSlaveGroup,
       "hpicf8023RptrMonitorGroup": hpicf8023RptrMonitorGroup,
       "hpicf8023RptrMonitorSlaveGroup": hpicf8023RptrMonitorSlaveGroup,
       "hpicf8023MultiRptrBasicGroup": hpicf8023MultiRptrBasicGroup,
       "hpicf8023MultiRptrMonitorGroup": hpicf8023MultiRptrMonitorGroup,
       "hpicf8023RptrNotifyGroup": hpicf8023RptrNotifyGroup,
       "hpicf8023MultiRptrNotifyGroup": hpicf8023MultiRptrNotifyGroup,
       "hpicf8023RpMauAutoNegGroup": hpicf8023RpMauAutoNegGroup,
       "hpicf8023Rptr100BasicGroup": hpicf8023Rptr100BasicGroup,
       "hpRptrBasic": hpRptrBasic,
       "hpRptrBasicGlobal": hpRptrBasicGlobal,
       "hpRptrEntityName": hpRptrEntityName,
       "hpRptrThinlanFault": hpRptrThinlanFault,
       "hpRptrSqeEnabled": hpRptrSqeEnabled,
       "hpRptrRobustHealing": hpRptrRobustHealing,
       "hpRptrBasicGroup": hpRptrBasicGroup,
       "hpRptrBasicGroupTable": hpRptrBasicGroupTable,
       "hpRptrBasicGroupEntry": hpRptrBasicGroupEntry,
       "hpRptrGrpGroupIndex": hpRptrGrpGroupIndex,
       "hpRptrGrpPortsAdminStatus": hpRptrGrpPortsAdminStatus,
       "hpRptrGrpPortsSegStatus": hpRptrGrpPortsSegStatus,
       "hpRptrGrpPortsMediaAvailable": hpRptrGrpPortsMediaAvailable,
       "hpRptrGrpPortsLinkbeatEnabled": hpRptrGrpPortsLinkbeatEnabled,
       "hpRptrGrpPortsOperStatus": hpRptrGrpPortsOperStatus,
       "hpRptrBasicPort": hpRptrBasicPort,
       "hpRptrBasicPtTable": hpRptrBasicPtTable,
       "hpRptrBasicPtEntry": hpRptrBasicPtEntry,
       "hpRptrPtGroupIndex": hpRptrPtGroupIndex,
       "hpRptrPtPortIndex": hpRptrPtPortIndex,
       "hpRptrPtLinkbeatEnable": hpRptrPtLinkbeatEnable,
       "hpRptrPtPolarityReversed": hpRptrPtPolarityReversed,
       "hpRptrPtSqeEnabled": hpRptrPtSqeEnabled,
       "hpRptrPtMediaAvailTrapEnable": hpRptrPtMediaAvailTrapEnable,
       "hpRptrPtLongCableEnable": hpRptrPtLongCableEnable,
       "hpRptrMonitor": hpRptrMonitor,
       "hpRptrMonitorGlobal": hpRptrMonitorGlobal,
       "hpRptrMonCounters": hpRptrMonCounters,
       "hpRptrMonGlobalFrames": hpRptrMonGlobalFrames,
       "hpRptrMonGlobalOctets": hpRptrMonGlobalOctets,
       "hpRptrMonGlobalFCSErrors": hpRptrMonGlobalFCSErrors,
       "hpRptrMonGlobalAlignmentErrors": hpRptrMonGlobalAlignmentErrors,
       "hpRptrMonGlobalFrameTooLongs": hpRptrMonGlobalFrameTooLongs,
       "hpRptrMonGlobalShortEvents": hpRptrMonGlobalShortEvents,
       "hpRptrMonGlobalRunts": hpRptrMonGlobalRunts,
       "hpRptrMonGlobalCollisions": hpRptrMonGlobalCollisions,
       "hpRptrMonGlobalLateEvents": hpRptrMonGlobalLateEvents,
       "hpRptrMonGlobalVeryLongEvents": hpRptrMonGlobalVeryLongEvents,
       "hpRptrMonGlobalDataRateMismatches": hpRptrMonGlobalDataRateMismatches,
       "hpRptrMonGlobalAutoPartitions": hpRptrMonGlobalAutoPartitions,
       "hpRptrMonGlobalErrors": hpRptrMonGlobalErrors,
       "hpRptrMonGlobalUcastPackets": hpRptrMonGlobalUcastPackets,
       "hpRptrMonGlobalBcastPackets": hpRptrMonGlobalBcastPackets,
       "hpRptrMonGlobalMcastPackets": hpRptrMonGlobalMcastPackets,
       "hpRptrMonitorGroup": hpRptrMonitorGroup,
       "hpRptrMonitorPort": hpRptrMonitorPort,
       "hpRptrMonPtTable": hpRptrMonPtTable,
       "hpRptrMonPtEntry": hpRptrMonPtEntry,
       "hpRptrMonPtGroupIndex": hpRptrMonPtGroupIndex,
       "hpRptrMonPtPortIndex": hpRptrMonPtPortIndex,
       "hpRptrMonPtUcastPackets": hpRptrMonPtUcastPackets,
       "hpRptrMonPtBcastPackets": hpRptrMonPtBcastPackets,
       "hpRptrMonPtMcastPackets": hpRptrMonPtMcastPackets,
       "hpRpMauGroup": hpRpMauGroup,
       "hpRpMauTable": hpRpMauTable,
       "hpRpMauEntry": hpRpMauEntry,
       "hpRpMauTypeList": hpRpMauTypeList,
       "hpRpMauAutoNegSupported": hpRpMauAutoNegSupported,
       "hpRpMauAutoNegAdminStatus": hpRpMauAutoNegAdminStatus,
       "hpRpMauAutoNegRemoteSignaling": hpRpMauAutoNegRemoteSignaling,
       "hpRpMauAutoNegConfig": hpRpMauAutoNegConfig,
       "hpRpMauAutoNegCapReceived": hpRpMauAutoNegCapReceived,
       "hpRpMauAutoNegRestart": hpRpMauAutoNegRestart,
       "hpicfLinkBeatTrap": hpicfLinkBeatTrap,
       "hpicfPartitionTrap": hpicfPartitionTrap,
       "hpicfMediaAvailDetectTrap": hpicfMediaAvailDetectTrap,
       "hpicfMediaAvailLostTrap": hpicfMediaAvailLostTrap,
       "hpicfPortPartitionTrap": hpicfPortPartitionTrap,
       "hpicfPortHealTrap": hpicfPortHealTrap}
)
