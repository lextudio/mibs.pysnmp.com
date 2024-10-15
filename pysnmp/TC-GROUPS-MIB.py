# SNMP MIB module (TC-GROUPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TC-GROUPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:00:56 2024
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

nbTcGroups = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10)
)
nbTcGroups.setRevisions(
        ("2006-01-12 00:00",
         "2005-07-07 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SupportValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("supported", 2))
    )



class EntryValidator(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )



# MIB Managed Objects in the order of their OIDs

_Nbase_ObjectIdentity = ObjectIdentity
nbase = _Nbase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629)
)
_NbSwitchG1_ObjectIdentity = ObjectIdentity
nbSwitchG1 = _NbSwitchG1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1)
)
_NbSwitchG1Il_ObjectIdentity = ObjectIdentity
nbSwitchG1Il = _NbSwitchG1Il_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50)
)
_NbRouterConfig_ObjectIdentity = ObjectIdentity
nbRouterConfig = _NbRouterConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12)
)
_NbRtActionLists_ObjectIdentity = ObjectIdentity
nbRtActionLists = _NbRtActionLists_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9)
)
_NbTcGrpCntrTable_Object = MibTable
nbTcGrpCntrTable = _NbTcGrpCntrTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 1)
)
if mibBuilder.loadTexts:
    nbTcGrpCntrTable.setStatus("current")
_NbTcGrpCntrEntry_Object = MibTableRow
nbTcGrpCntrEntry = _NbTcGrpCntrEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 1, 1)
)
nbTcGrpCntrEntry.setIndexNames(
    (0, "TC-GROUPS-MIB", "nbTcGroupCntrGrpName"),
    (0, "TC-GROUPS-MIB", "nbTcGroupCntrActionName"),
)
if mibBuilder.loadTexts:
    nbTcGrpCntrEntry.setStatus("current")


class _NbTcGroupCntrGrpName_Type(SnmpAdminString):
    """Custom type nbTcGroupCntrGrpName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NbTcGroupCntrGrpName_Type.__name__ = "SnmpAdminString"
_NbTcGroupCntrGrpName_Object = MibTableColumn
nbTcGroupCntrGrpName = _NbTcGroupCntrGrpName_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 1, 1, 1),
    _NbTcGroupCntrGrpName_Type()
)
nbTcGroupCntrGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbTcGroupCntrGrpName.setStatus("current")


class _NbTcGroupCntrActionName_Type(SnmpAdminString):
    """Custom type nbTcGroupCntrActionName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NbTcGroupCntrActionName_Type.__name__ = "SnmpAdminString"
_NbTcGroupCntrActionName_Object = MibTableColumn
nbTcGroupCntrActionName = _NbTcGroupCntrActionName_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 1, 1, 2),
    _NbTcGroupCntrActionName_Type()
)
nbTcGroupCntrActionName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbTcGroupCntrActionName.setStatus("current")
_NbTcGroupCntrStatus_Type = EntryValidator
_NbTcGroupCntrStatus_Object = MibTableColumn
nbTcGroupCntrStatus = _NbTcGroupCntrStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 1, 1, 3),
    _NbTcGroupCntrStatus_Type()
)
nbTcGroupCntrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbTcGroupCntrStatus.setStatus("current")
_NbTcGrpDscrTable_Object = MibTable
nbTcGrpDscrTable = _NbTcGrpDscrTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 2)
)
if mibBuilder.loadTexts:
    nbTcGrpDscrTable.setStatus("current")
_NbTcGrpDscrEntry_Object = MibTableRow
nbTcGrpDscrEntry = _NbTcGrpDscrEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 2, 1)
)
nbTcGrpDscrEntry.setIndexNames(
    (0, "TC-GROUPS-MIB", "nbTcGroupDscrGrpName"),
)
if mibBuilder.loadTexts:
    nbTcGrpDscrEntry.setStatus("current")


class _NbTcGroupDscrGrpName_Type(SnmpAdminString):
    """Custom type nbTcGroupDscrGrpName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NbTcGroupDscrGrpName_Type.__name__ = "SnmpAdminString"
_NbTcGroupDscrGrpName_Object = MibTableColumn
nbTcGroupDscrGrpName = _NbTcGroupDscrGrpName_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 2, 1, 1),
    _NbTcGroupDscrGrpName_Type()
)
nbTcGroupDscrGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbTcGroupDscrGrpName.setStatus("current")


class _NbTcGroupDscrText_Type(DisplayString):
    """Custom type nbTcGroupDscrText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_NbTcGroupDscrText_Type.__name__ = "DisplayString"
_NbTcGroupDscrText_Object = MibTableColumn
nbTcGroupDscrText = _NbTcGroupDscrText_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 2, 1, 3),
    _NbTcGroupDscrText_Type()
)
nbTcGroupDscrText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbTcGroupDscrText.setStatus("current")
_NbTcGrpReslTable_Object = MibTable
nbTcGrpReslTable = _NbTcGrpReslTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 3)
)
if mibBuilder.loadTexts:
    nbTcGrpReslTable.setStatus("current")
_NbTcGrpReslEntry_Object = MibTableRow
nbTcGrpReslEntry = _NbTcGrpReslEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 3, 1)
)
if mibBuilder.loadTexts:
    nbTcGrpReslEntry.setStatus("current")
_NbTcGroupReslStatus_Type = OctetString
_NbTcGroupReslStatus_Object = MibTableColumn
nbTcGroupReslStatus = _NbTcGroupReslStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 3, 1, 3),
    _NbTcGroupReslStatus_Type()
)
nbTcGroupReslStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbTcGroupReslStatus.setStatus("current")
_NbTcGroupReslCnfrmncCntrSet_Type = Integer32
_NbTcGroupReslCnfrmncCntrSet_Object = MibTableColumn
nbTcGroupReslCnfrmncCntrSet = _NbTcGroupReslCnfrmncCntrSet_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 3, 1, 4),
    _NbTcGroupReslCnfrmncCntrSet_Type()
)
nbTcGroupReslCnfrmncCntrSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbTcGroupReslCnfrmncCntrSet.setStatus("current")
_NbTcGroupReslMeteringGreens_Type = Counter64
_NbTcGroupReslMeteringGreens_Object = MibTableColumn
nbTcGroupReslMeteringGreens = _NbTcGroupReslMeteringGreens_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 3, 1, 5),
    _NbTcGroupReslMeteringGreens_Type()
)
nbTcGroupReslMeteringGreens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbTcGroupReslMeteringGreens.setStatus("current")
_NbTcGroupReslMeteringYellows_Type = Counter64
_NbTcGroupReslMeteringYellows_Object = MibTableColumn
nbTcGroupReslMeteringYellows = _NbTcGroupReslMeteringYellows_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 3, 1, 6),
    _NbTcGroupReslMeteringYellows_Type()
)
nbTcGroupReslMeteringYellows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbTcGroupReslMeteringYellows.setStatus("current")
_NbTcGroupReslMeteringReds_Type = Counter64
_NbTcGroupReslMeteringReds_Object = MibTableColumn
nbTcGroupReslMeteringReds = _NbTcGroupReslMeteringReds_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 3, 1, 7),
    _NbTcGroupReslMeteringReds_Type()
)
nbTcGroupReslMeteringReds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbTcGroupReslMeteringReds.setStatus("current")
_NbTcGroupReslAggrOctets_Type = Counter64
_NbTcGroupReslAggrOctets_Object = MibTableColumn
nbTcGroupReslAggrOctets = _NbTcGroupReslAggrOctets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 3, 1, 9),
    _NbTcGroupReslAggrOctets_Type()
)
nbTcGroupReslAggrOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbTcGroupReslAggrOctets.setStatus("current")
_NbTcGroupReslAggrPackets_Type = Counter64
_NbTcGroupReslAggrPackets_Object = MibTableColumn
nbTcGroupReslAggrPackets = _NbTcGroupReslAggrPackets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 3, 1, 10),
    _NbTcGroupReslAggrPackets_Type()
)
nbTcGroupReslAggrPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbTcGroupReslAggrPackets.setStatus("current")
_NbTcGroupReslConfGreenOctets_Type = Counter64
_NbTcGroupReslConfGreenOctets_Object = MibTableColumn
nbTcGroupReslConfGreenOctets = _NbTcGroupReslConfGreenOctets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 3, 1, 12),
    _NbTcGroupReslConfGreenOctets_Type()
)
nbTcGroupReslConfGreenOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbTcGroupReslConfGreenOctets.setStatus("current")
_NbTcGroupReslConfGreenPackets_Type = Counter64
_NbTcGroupReslConfGreenPackets_Object = MibTableColumn
nbTcGroupReslConfGreenPackets = _NbTcGroupReslConfGreenPackets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 3, 1, 13),
    _NbTcGroupReslConfGreenPackets_Type()
)
nbTcGroupReslConfGreenPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbTcGroupReslConfGreenPackets.setStatus("current")
_NbTcGroupReslConfYellowOctets_Type = Counter64
_NbTcGroupReslConfYellowOctets_Object = MibTableColumn
nbTcGroupReslConfYellowOctets = _NbTcGroupReslConfYellowOctets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 3, 1, 14),
    _NbTcGroupReslConfYellowOctets_Type()
)
nbTcGroupReslConfYellowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbTcGroupReslConfYellowOctets.setStatus("current")
_NbTcGroupReslConfYellowPackets_Type = Counter64
_NbTcGroupReslConfYellowPackets_Object = MibTableColumn
nbTcGroupReslConfYellowPackets = _NbTcGroupReslConfYellowPackets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 3, 1, 15),
    _NbTcGroupReslConfYellowPackets_Type()
)
nbTcGroupReslConfYellowPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbTcGroupReslConfYellowPackets.setStatus("current")
_NbTcGroupReslConfRedOctets_Type = Counter64
_NbTcGroupReslConfRedOctets_Object = MibTableColumn
nbTcGroupReslConfRedOctets = _NbTcGroupReslConfRedOctets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 3, 1, 16),
    _NbTcGroupReslConfRedOctets_Type()
)
nbTcGroupReslConfRedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbTcGroupReslConfRedOctets.setStatus("current")
_NbTcGroupReslConfRedPackets_Type = Counter64
_NbTcGroupReslConfRedPackets_Object = MibTableColumn
nbTcGroupReslConfRedPackets = _NbTcGroupReslConfRedPackets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 3, 1, 17),
    _NbTcGroupReslConfRedPackets_Type()
)
nbTcGroupReslConfRedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbTcGroupReslConfRedPackets.setStatus("current")
_NbTcActCtrlTable_Object = MibTable
nbTcActCtrlTable = _NbTcActCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 9)
)
if mibBuilder.loadTexts:
    nbTcActCtrlTable.setStatus("current")
_NbTcActCtrlEntry_Object = MibTableRow
nbTcActCtrlEntry = _NbTcActCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 9, 1)
)
nbTcActCtrlEntry.setIndexNames(
    (0, "TC-GROUPS-MIB", "nbTcActName"),
)
if mibBuilder.loadTexts:
    nbTcActCtrlEntry.setStatus("current")


class _NbTcActName_Type(SnmpAdminString):
    """Custom type nbTcActName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NbTcActName_Type.__name__ = "SnmpAdminString"
_NbTcActName_Object = MibTableColumn
nbTcActName = _NbTcActName_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 9, 1, 1),
    _NbTcActName_Type()
)
nbTcActName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbTcActName.setStatus("current")
_NbTcActStatus_Type = EntryValidator
_NbTcActStatus_Object = MibTableColumn
nbTcActStatus = _NbTcActStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 9, 1, 64),
    _NbTcActStatus_Type()
)
nbTcActStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbTcActStatus.setStatus("current")
_NbTcActReslTable_Object = MibTable
nbTcActReslTable = _NbTcActReslTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 10)
)
if mibBuilder.loadTexts:
    nbTcActReslTable.setStatus("current")
_NbTcActReslEntry_Object = MibTableRow
nbTcActReslEntry = _NbTcActReslEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 10, 1)
)
if mibBuilder.loadTexts:
    nbTcActReslEntry.setStatus("current")
_NbTcActReslStatus_Type = OctetString
_NbTcActReslStatus_Object = MibTableColumn
nbTcActReslStatus = _NbTcActReslStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 10, 1, 3),
    _NbTcActReslStatus_Type()
)
nbTcActReslStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbTcActReslStatus.setStatus("current")
_NbTcGrpSupport_ObjectIdentity = ObjectIdentity
nbTcGrpSupport = _NbTcGrpSupport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 100)
)
_NbTcGrpSupportGroups_Type = SupportValue
_NbTcGrpSupportGroups_Object = MibScalar
nbTcGrpSupportGroups = _NbTcGrpSupportGroups_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 100, 2),
    _NbTcGrpSupportGroups_Type()
)
nbTcGrpSupportGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbTcGrpSupportGroups.setStatus("current")
_NbTcGrpSupportLists_Type = SupportValue
_NbTcGrpSupportLists_Object = MibScalar
nbTcGrpSupportLists = _NbTcGrpSupportLists_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 100, 9),
    _NbTcGrpSupportLists_Type()
)
nbTcGrpSupportLists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbTcGrpSupportLists.setStatus("current")
_NbTcGrpConformance_ObjectIdentity = ObjectIdentity
nbTcGrpConformance = _NbTcGrpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 101)
)
_NbTcGrpMIBCompliances_ObjectIdentity = ObjectIdentity
nbTcGrpMIBCompliances = _NbTcGrpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 101, 1)
)
_NbTcGrpMIBGroups_ObjectIdentity = ObjectIdentity
nbTcGrpMIBGroups = _NbTcGrpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 101, 2)
)
nbTcGrpCntrEntry.registerAugmentions(
    ("TC-GROUPS-MIB",
     "nbTcGrpReslEntry")
)
nbTcGrpReslEntry.setIndexNames(*nbTcGrpCntrEntry.getIndexNames())
nbTcActCtrlEntry.registerAugmentions(
    ("TC-GROUPS-MIB",
     "nbTcActReslEntry")
)
nbTcActReslEntry.setIndexNames(*nbTcActCtrlEntry.getIndexNames())

# Managed Objects groups

nbTcGrpSupportReflectors = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 101, 2, 1)
)
nbTcGrpSupportReflectors.setObjects(
      *(("TC-GROUPS-MIB", "nbTcGrpSupportGroups"),
        ("TC-GROUPS-MIB", "nbTcGrpSupportLists"))
)
if mibBuilder.loadTexts:
    nbTcGrpSupportReflectors.setStatus("current")

nbTcGrpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 101, 2, 2)
)
nbTcGrpGroup.setObjects(
      *(("TC-GROUPS-MIB", "nbTcGroupCntrStatus"),
        ("TC-GROUPS-MIB", "nbTcGroupDscrText"),
        ("TC-GROUPS-MIB", "nbTcGroupReslStatus"),
        ("TC-GROUPS-MIB", "nbTcGroupReslCnfrmncCntrSet"),
        ("TC-GROUPS-MIB", "nbTcGroupReslMeteringGreens"),
        ("TC-GROUPS-MIB", "nbTcGroupReslMeteringYellows"),
        ("TC-GROUPS-MIB", "nbTcGroupReslMeteringReds"),
        ("TC-GROUPS-MIB", "nbTcGroupReslAggrOctets"),
        ("TC-GROUPS-MIB", "nbTcGroupReslAggrPackets"),
        ("TC-GROUPS-MIB", "nbTcGroupReslConfGreenOctets"),
        ("TC-GROUPS-MIB", "nbTcGroupReslConfGreenPackets"),
        ("TC-GROUPS-MIB", "nbTcGroupReslConfYellowOctets"),
        ("TC-GROUPS-MIB", "nbTcGroupReslConfYellowPackets"),
        ("TC-GROUPS-MIB", "nbTcGroupReslConfRedOctets"),
        ("TC-GROUPS-MIB", "nbTcGroupReslConfRedPackets"))
)
if mibBuilder.loadTexts:
    nbTcGrpGroup.setStatus("current")

nbTcActGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 101, 2, 3)
)
nbTcActGroup.setObjects(
      *(("TC-GROUPS-MIB", "nbTcActStatus"),
        ("TC-GROUPS-MIB", "nbTcActReslStatus"))
)
if mibBuilder.loadTexts:
    nbTcActGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

nbTcGrpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 101, 1, 1)
)
if mibBuilder.loadTexts:
    nbTcGrpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TC-GROUPS-MIB",
    **{"SupportValue": SupportValue,
       "EntryValidator": EntryValidator,
       "nbase": nbase,
       "nbSwitchG1": nbSwitchG1,
       "nbSwitchG1Il": nbSwitchG1Il,
       "nbRouterConfig": nbRouterConfig,
       "nbRtActionLists": nbRtActionLists,
       "nbTcGroups": nbTcGroups,
       "nbTcGrpCntrTable": nbTcGrpCntrTable,
       "nbTcGrpCntrEntry": nbTcGrpCntrEntry,
       "nbTcGroupCntrGrpName": nbTcGroupCntrGrpName,
       "nbTcGroupCntrActionName": nbTcGroupCntrActionName,
       "nbTcGroupCntrStatus": nbTcGroupCntrStatus,
       "nbTcGrpDscrTable": nbTcGrpDscrTable,
       "nbTcGrpDscrEntry": nbTcGrpDscrEntry,
       "nbTcGroupDscrGrpName": nbTcGroupDscrGrpName,
       "nbTcGroupDscrText": nbTcGroupDscrText,
       "nbTcGrpReslTable": nbTcGrpReslTable,
       "nbTcGrpReslEntry": nbTcGrpReslEntry,
       "nbTcGroupReslStatus": nbTcGroupReslStatus,
       "nbTcGroupReslCnfrmncCntrSet": nbTcGroupReslCnfrmncCntrSet,
       "nbTcGroupReslMeteringGreens": nbTcGroupReslMeteringGreens,
       "nbTcGroupReslMeteringYellows": nbTcGroupReslMeteringYellows,
       "nbTcGroupReslMeteringReds": nbTcGroupReslMeteringReds,
       "nbTcGroupReslAggrOctets": nbTcGroupReslAggrOctets,
       "nbTcGroupReslAggrPackets": nbTcGroupReslAggrPackets,
       "nbTcGroupReslConfGreenOctets": nbTcGroupReslConfGreenOctets,
       "nbTcGroupReslConfGreenPackets": nbTcGroupReslConfGreenPackets,
       "nbTcGroupReslConfYellowOctets": nbTcGroupReslConfYellowOctets,
       "nbTcGroupReslConfYellowPackets": nbTcGroupReslConfYellowPackets,
       "nbTcGroupReslConfRedOctets": nbTcGroupReslConfRedOctets,
       "nbTcGroupReslConfRedPackets": nbTcGroupReslConfRedPackets,
       "nbTcActCtrlTable": nbTcActCtrlTable,
       "nbTcActCtrlEntry": nbTcActCtrlEntry,
       "nbTcActName": nbTcActName,
       "nbTcActStatus": nbTcActStatus,
       "nbTcActReslTable": nbTcActReslTable,
       "nbTcActReslEntry": nbTcActReslEntry,
       "nbTcActReslStatus": nbTcActReslStatus,
       "nbTcGrpSupport": nbTcGrpSupport,
       "nbTcGrpSupportGroups": nbTcGrpSupportGroups,
       "nbTcGrpSupportLists": nbTcGrpSupportLists,
       "nbTcGrpConformance": nbTcGrpConformance,
       "nbTcGrpMIBCompliances": nbTcGrpMIBCompliances,
       "nbTcGrpMIBCompliance": nbTcGrpMIBCompliance,
       "nbTcGrpMIBGroups": nbTcGrpMIBGroups,
       "nbTcGrpSupportReflectors": nbTcGrpSupportReflectors,
       "nbTcGrpGroup": nbTcGrpGroup,
       "nbTcActGroup": nbTcActGroup}
)
