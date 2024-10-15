# SNMP MIB module (HP-ICF-VRRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-VRRP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:29 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

(vrrpAssoIpAddrEntry,
 vrrpOperEntry,
 vrrpOperVrId) = mibBuilder.importSymbols(
    "VRRP-MIB",
    "vrrpAssoIpAddrEntry",
    "vrrpOperEntry",
    "vrrpOperVrId")


# MODULE-IDENTITY

hpicfVrrpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31)
)
hpicfVrrpMIB.setRevisions(
        ("2012-11-15 00:00",
         "2013-06-12 00:00",
         "2012-02-22 00:00",
         "2010-10-20 00:00",
         "2010-07-28 00:00",
         "2009-05-19 00:00",
         "2008-02-20 00:00",
         "2007-12-12 00:00",
         "2007-08-22 00:00",
         "2005-07-14 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfVrrpOperations_ObjectIdentity = ObjectIdentity
hpicfVrrpOperations = _HpicfVrrpOperations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1)
)


class _HpicfVrrpAdminStatus_Type(TruthValue):
    """Custom type hpicfVrrpAdminStatus based on TruthValue"""


_HpicfVrrpAdminStatus_Object = MibScalar
hpicfVrrpAdminStatus = _HpicfVrrpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 1),
    _HpicfVrrpAdminStatus_Type()
)
hpicfVrrpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfVrrpAdminStatus.setStatus("deprecated")
_HpicfVrrpOperTable_Object = MibTable
hpicfVrrpOperTable = _HpicfVrrpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfVrrpOperTable.setStatus("current")
_HpicfVrrpOperEntry_Object = MibTableRow
hpicfVrrpOperEntry = _HpicfVrrpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfVrrpOperEntry.setStatus("current")


class _HpicfVrrpVrMode_Type(Integer32):
    """Custom type hpicfVrrpVrMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("owner", 1),
          ("uninitialized", 3))
    )


_HpicfVrrpVrMode_Type.__name__ = "Integer32"
_HpicfVrrpVrMode_Object = MibTableColumn
hpicfVrrpVrMode = _HpicfVrrpVrMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 2, 1, 1),
    _HpicfVrrpVrMode_Type()
)
hpicfVrrpVrMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfVrrpVrMode.setStatus("current")


class _HpicfVrrpVrMasterPreempt_Type(TruthValue):
    """Custom type hpicfVrrpVrMasterPreempt based on TruthValue"""


_HpicfVrrpVrMasterPreempt_Object = MibTableColumn
hpicfVrrpVrMasterPreempt = _HpicfVrrpVrMasterPreempt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 2, 1, 2),
    _HpicfVrrpVrMasterPreempt_Type()
)
hpicfVrrpVrMasterPreempt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfVrrpVrMasterPreempt.setStatus("current")


class _HpicfVrrpVrTransferControl_Type(TruthValue):
    """Custom type hpicfVrrpVrTransferControl based on TruthValue"""


_HpicfVrrpVrTransferControl_Object = MibTableColumn
hpicfVrrpVrTransferControl = _HpicfVrrpVrTransferControl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 2, 1, 3),
    _HpicfVrrpVrTransferControl_Type()
)
hpicfVrrpVrTransferControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfVrrpVrTransferControl.setStatus("current")


class _HpicfVrrpVrPreemptDelayTime_Type(Integer32):
    """Custom type hpicfVrrpVrPreemptDelayTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_HpicfVrrpVrPreemptDelayTime_Type.__name__ = "Integer32"
_HpicfVrrpVrPreemptDelayTime_Object = MibTableColumn
hpicfVrrpVrPreemptDelayTime = _HpicfVrrpVrPreemptDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 2, 1, 4),
    _HpicfVrrpVrPreemptDelayTime_Type()
)
hpicfVrrpVrPreemptDelayTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfVrrpVrPreemptDelayTime.setStatus("current")


class _HpicfVrrpVrControl_Type(Integer32):
    """Custom type hpicfVrrpVrControl based on Integer32"""
    defaultValue = 4

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
        *(("failback", 1),
          ("failover", 2),
          ("failoverWithMonitoring", 3),
          ("invalid", 4))
    )


_HpicfVrrpVrControl_Type.__name__ = "Integer32"
_HpicfVrrpVrControl_Object = MibTableColumn
hpicfVrrpVrControl = _HpicfVrrpVrControl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 2, 1, 5),
    _HpicfVrrpVrControl_Type()
)
hpicfVrrpVrControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfVrrpVrControl.setStatus("current")


class _HpicfVrrpVrRespondToPing_Type(TruthValue):
    """Custom type hpicfVrrpVrRespondToPing based on TruthValue"""


_HpicfVrrpVrRespondToPing_Object = MibTableColumn
hpicfVrrpVrRespondToPing = _HpicfVrrpVrRespondToPing_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 2, 1, 6),
    _HpicfVrrpVrRespondToPing_Type()
)
hpicfVrrpVrRespondToPing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfVrrpVrRespondToPing.setStatus("current")
_HpicfVrrpAssoIpAddrTable_Object = MibTable
hpicfVrrpAssoIpAddrTable = _HpicfVrrpAssoIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfVrrpAssoIpAddrTable.setStatus("current")
_HpicfVrrpAssoIpAddrEntry_Object = MibTableRow
hpicfVrrpAssoIpAddrEntry = _HpicfVrrpAssoIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hpicfVrrpAssoIpAddrEntry.setStatus("current")


class _HpicfVrrpAssoIpMask_Type(IpAddress):
    """Custom type hpicfVrrpAssoIpMask based on IpAddress"""
    defaultHexValue = "00000000"


_HpicfVrrpAssoIpMask_Object = MibTableColumn
hpicfVrrpAssoIpMask = _HpicfVrrpAssoIpMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 3, 1, 1),
    _HpicfVrrpAssoIpMask_Type()
)
hpicfVrrpAssoIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfVrrpAssoIpMask.setStatus("current")
_HpicfVrrpTrackTable_Object = MibTable
hpicfVrrpTrackTable = _HpicfVrrpTrackTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 5)
)
if mibBuilder.loadTexts:
    hpicfVrrpTrackTable.setStatus("current")
_HpicfVrrpTrackEntry_Object = MibTableRow
hpicfVrrpTrackEntry = _HpicfVrrpTrackEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 5, 1)
)
hpicfVrrpTrackEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VRRP-MIB", "vrrpOperVrId"),
    (0, "HP-ICF-VRRP-MIB", "hpicfVrrpVrTrackType"),
    (0, "HP-ICF-VRRP-MIB", "hpicfVrrpVrTrackEntity"),
)
if mibBuilder.loadTexts:
    hpicfVrrpTrackEntry.setStatus("current")


class _HpicfVrrpVrTrackType_Type(Integer32):
    """Custom type hpicfVrrpVrTrackType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("port", 1),
          ("trunk", 2),
          ("vlan", 3))
    )


_HpicfVrrpVrTrackType_Type.__name__ = "Integer32"
_HpicfVrrpVrTrackType_Object = MibTableColumn
hpicfVrrpVrTrackType = _HpicfVrrpVrTrackType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 5, 1, 1),
    _HpicfVrrpVrTrackType_Type()
)
hpicfVrrpVrTrackType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfVrrpVrTrackType.setStatus("current")


class _HpicfVrrpVrTrackEntity_Type(SnmpAdminString):
    """Custom type hpicfVrrpVrTrackEntity based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HpicfVrrpVrTrackEntity_Type.__name__ = "SnmpAdminString"
_HpicfVrrpVrTrackEntity_Object = MibTableColumn
hpicfVrrpVrTrackEntity = _HpicfVrrpVrTrackEntity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 5, 1, 2),
    _HpicfVrrpVrTrackEntity_Type()
)
hpicfVrrpVrTrackEntity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfVrrpVrTrackEntity.setStatus("current")
_HpicfVrrpTrackRowStatus_Type = RowStatus
_HpicfVrrpTrackRowStatus_Object = MibTableColumn
hpicfVrrpTrackRowStatus = _HpicfVrrpTrackRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 5, 1, 3),
    _HpicfVrrpTrackRowStatus_Type()
)
hpicfVrrpTrackRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfVrrpTrackRowStatus.setStatus("current")


class _HpicfVrrpTrackState_Type(Integer32):
    """Custom type hpicfVrrpTrackState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_HpicfVrrpTrackState_Type.__name__ = "Integer32"
_HpicfVrrpTrackState_Object = MibTableColumn
hpicfVrrpTrackState = _HpicfVrrpTrackState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 5, 1, 4),
    _HpicfVrrpTrackState_Type()
)
hpicfVrrpTrackState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVrrpTrackState.setStatus("current")
_HpicfVrrpStatsTable_Object = MibTable
hpicfVrrpStatsTable = _HpicfVrrpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 6)
)
if mibBuilder.loadTexts:
    hpicfVrrpStatsTable.setStatus("current")
_HpicfVrrpStatsEntry_Object = MibTableRow
hpicfVrrpStatsEntry = _HpicfVrrpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 6, 1)
)
if mibBuilder.loadTexts:
    hpicfVrrpStatsEntry.setStatus("current")


class _HpicfVrrpStatsNearFailovers_Type(Counter32):
    """Custom type hpicfVrrpStatsNearFailovers based on Counter32"""
    defaultValue = 0


_HpicfVrrpStatsNearFailovers_Object = MibTableColumn
hpicfVrrpStatsNearFailovers = _HpicfVrrpStatsNearFailovers_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 6, 1, 1),
    _HpicfVrrpStatsNearFailovers_Type()
)
hpicfVrrpStatsNearFailovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVrrpStatsNearFailovers.setStatus("current")


class _HpicfVrrpRespondToPing_Type(TruthValue):
    """Custom type hpicfVrrpRespondToPing based on TruthValue"""


_HpicfVrrpRespondToPing_Object = MibScalar
hpicfVrrpRespondToPing = _HpicfVrrpRespondToPing_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 7),
    _HpicfVrrpRespondToPing_Type()
)
hpicfVrrpRespondToPing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfVrrpRespondToPing.setStatus("deprecated")


class _HpicfVrrpRemoveConfig_Type(TruthValue):
    """Custom type hpicfVrrpRemoveConfig based on TruthValue"""


_HpicfVrrpRemoveConfig_Object = MibScalar
hpicfVrrpRemoveConfig = _HpicfVrrpRemoveConfig_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 8),
    _HpicfVrrpRemoveConfig_Type()
)
hpicfVrrpRemoveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfVrrpRemoveConfig.setStatus("deprecated")


class _HpicfVrrpNonstop_Type(TruthValue):
    """Custom type hpicfVrrpNonstop based on TruthValue"""


_HpicfVrrpNonstop_Object = MibScalar
hpicfVrrpNonstop = _HpicfVrrpNonstop_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 9),
    _HpicfVrrpNonstop_Type()
)
hpicfVrrpNonstop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfVrrpNonstop.setStatus("deprecated")
_HpicfVrrpConformance_ObjectIdentity = ObjectIdentity
hpicfVrrpConformance = _HpicfVrrpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2)
)
_HpicfVrrpMIBCompliances_ObjectIdentity = ObjectIdentity
hpicfVrrpMIBCompliances = _HpicfVrrpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 1)
)
_HpicfVrrpMIBGroups_ObjectIdentity = ObjectIdentity
hpicfVrrpMIBGroups = _HpicfVrrpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 2)
)
vrrpOperEntry.registerAugmentions(
    ("HP-ICF-VRRP-MIB",
     "hpicfVrrpOperEntry")
)
hpicfVrrpOperEntry.setIndexNames(*vrrpOperEntry.getIndexNames())
vrrpAssoIpAddrEntry.registerAugmentions(
    ("HP-ICF-VRRP-MIB",
     "hpicfVrrpAssoIpAddrEntry")
)
hpicfVrrpAssoIpAddrEntry.setIndexNames(*vrrpAssoIpAddrEntry.getIndexNames())
vrrpOperEntry.registerAugmentions(
    ("HP-ICF-VRRP-MIB",
     "hpicfVrrpStatsEntry")
)
hpicfVrrpStatsEntry.setIndexNames(*vrrpOperEntry.getIndexNames())

# Managed Objects groups

hpicfVrrpOperGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 2, 1)
)
hpicfVrrpOperGroup.setObjects(
      *(("HP-ICF-VRRP-MIB", "hpicfVrrpAdminStatus"),
        ("HP-ICF-VRRP-MIB", "hpicfVrrpVrMode"),
        ("HP-ICF-VRRP-MIB", "hpicfVrrpVrMasterPreempt"),
        ("HP-ICF-VRRP-MIB", "hpicfVrrpVrTransferControl"),
        ("HP-ICF-VRRP-MIB", "hpicfVrrpVrPreemptDelayTime"),
        ("HP-ICF-VRRP-MIB", "hpicfVrrpAssoIpMask"))
)
if mibBuilder.loadTexts:
    hpicfVrrpOperGroup.setStatus("deprecated")

hpicfVrrpTrackGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 2, 2)
)
hpicfVrrpTrackGroup.setObjects(
      *(("HP-ICF-VRRP-MIB", "hpicfVrrpTrackRowStatus"),
        ("HP-ICF-VRRP-MIB", "hpicfVrrpVrControl"))
)
if mibBuilder.loadTexts:
    hpicfVrrpTrackGroup.setStatus("deprecated")

hpicfVrrpVrPingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 2, 3)
)
hpicfVrrpVrPingGroup.setObjects(
    ("HP-ICF-VRRP-MIB", "hpicfVrrpVrRespondToPing")
)
if mibBuilder.loadTexts:
    hpicfVrrpVrPingGroup.setStatus("current")

hpicfVrrpNonstopGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 2, 4)
)
hpicfVrrpNonstopGroup.setObjects(
    ("HP-ICF-VRRP-MIB", "hpicfVrrpNonstop")
)
if mibBuilder.loadTexts:
    hpicfVrrpNonstopGroup.setStatus("deprecated")

hpicfVrrpOperationsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 2, 5)
)
hpicfVrrpOperationsGroup.setObjects(
      *(("HP-ICF-VRRP-MIB", "hpicfVrrpRespondToPing"),
        ("HP-ICF-VRRP-MIB", "hpicfVrrpRemoveConfig"),
        ("HP-ICF-VRRP-MIB", "hpicfVrrpStatsNearFailovers"))
)
if mibBuilder.loadTexts:
    hpicfVrrpOperationsGroup.setStatus("deprecated")

hpicfVrrpTrackGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 2, 6)
)
hpicfVrrpTrackGroup1.setObjects(
      *(("HP-ICF-VRRP-MIB", "hpicfVrrpTrackRowStatus"),
        ("HP-ICF-VRRP-MIB", "hpicfVrrpVrControl"),
        ("HP-ICF-VRRP-MIB", "hpicfVrrpTrackState"))
)
if mibBuilder.loadTexts:
    hpicfVrrpTrackGroup1.setStatus("current")

hpicfVrrpOperGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 2, 7)
)
hpicfVrrpOperGroup1.setObjects(
      *(("HP-ICF-VRRP-MIB", "hpicfVrrpVrMode"),
        ("HP-ICF-VRRP-MIB", "hpicfVrrpVrMasterPreempt"),
        ("HP-ICF-VRRP-MIB", "hpicfVrrpVrTransferControl"),
        ("HP-ICF-VRRP-MIB", "hpicfVrrpVrPreemptDelayTime"),
        ("HP-ICF-VRRP-MIB", "hpicfVrrpAssoIpMask"))
)
if mibBuilder.loadTexts:
    hpicfVrrpOperGroup1.setStatus("current")

hpicfVrrpOperationsGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 2, 8)
)
hpicfVrrpOperationsGroup1.setObjects(
    ("HP-ICF-VRRP-MIB", "hpicfVrrpStatsNearFailovers")
)
if mibBuilder.loadTexts:
    hpicfVrrpOperationsGroup1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfVrrpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfVrrpMIBCompliance.setStatus(
        "deprecated"
    )

hpicfVrrpMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfVrrpMIBCompliance1.setStatus(
        "deprecated"
    )

hpicfVrrpMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfVrrpMIBCompliance2.setStatus(
        "current"
    )

hpicfVrrpMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 1, 4)
)
if mibBuilder.loadTexts:
    hpicfVrrpMIBCompliance3.setStatus(
        "deprecated"
    )

hpicfVrrpMIBCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 1, 5)
)
if mibBuilder.loadTexts:
    hpicfVrrpMIBCompliance4.setStatus(
        "deprecated"
    )

hpicfVrrpMIBCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 1, 6)
)
if mibBuilder.loadTexts:
    hpicfVrrpMIBCompliance5.setStatus(
        "deprecated"
    )

hpicfVrrpMIBCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 1, 7)
)
if mibBuilder.loadTexts:
    hpicfVrrpMIBCompliance6.setStatus(
        "current"
    )

hpicfVrrpMIBCompliance7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 1, 8)
)
if mibBuilder.loadTexts:
    hpicfVrrpMIBCompliance7.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-VRRP-MIB",
    **{"hpicfVrrpMIB": hpicfVrrpMIB,
       "hpicfVrrpOperations": hpicfVrrpOperations,
       "hpicfVrrpAdminStatus": hpicfVrrpAdminStatus,
       "hpicfVrrpOperTable": hpicfVrrpOperTable,
       "hpicfVrrpOperEntry": hpicfVrrpOperEntry,
       "hpicfVrrpVrMode": hpicfVrrpVrMode,
       "hpicfVrrpVrMasterPreempt": hpicfVrrpVrMasterPreempt,
       "hpicfVrrpVrTransferControl": hpicfVrrpVrTransferControl,
       "hpicfVrrpVrPreemptDelayTime": hpicfVrrpVrPreemptDelayTime,
       "hpicfVrrpVrControl": hpicfVrrpVrControl,
       "hpicfVrrpVrRespondToPing": hpicfVrrpVrRespondToPing,
       "hpicfVrrpAssoIpAddrTable": hpicfVrrpAssoIpAddrTable,
       "hpicfVrrpAssoIpAddrEntry": hpicfVrrpAssoIpAddrEntry,
       "hpicfVrrpAssoIpMask": hpicfVrrpAssoIpMask,
       "hpicfVrrpTrackTable": hpicfVrrpTrackTable,
       "hpicfVrrpTrackEntry": hpicfVrrpTrackEntry,
       "hpicfVrrpVrTrackType": hpicfVrrpVrTrackType,
       "hpicfVrrpVrTrackEntity": hpicfVrrpVrTrackEntity,
       "hpicfVrrpTrackRowStatus": hpicfVrrpTrackRowStatus,
       "hpicfVrrpTrackState": hpicfVrrpTrackState,
       "hpicfVrrpStatsTable": hpicfVrrpStatsTable,
       "hpicfVrrpStatsEntry": hpicfVrrpStatsEntry,
       "hpicfVrrpStatsNearFailovers": hpicfVrrpStatsNearFailovers,
       "hpicfVrrpRespondToPing": hpicfVrrpRespondToPing,
       "hpicfVrrpRemoveConfig": hpicfVrrpRemoveConfig,
       "hpicfVrrpNonstop": hpicfVrrpNonstop,
       "hpicfVrrpConformance": hpicfVrrpConformance,
       "hpicfVrrpMIBCompliances": hpicfVrrpMIBCompliances,
       "hpicfVrrpMIBCompliance": hpicfVrrpMIBCompliance,
       "hpicfVrrpMIBCompliance1": hpicfVrrpMIBCompliance1,
       "hpicfVrrpMIBCompliance2": hpicfVrrpMIBCompliance2,
       "hpicfVrrpMIBCompliance3": hpicfVrrpMIBCompliance3,
       "hpicfVrrpMIBCompliance4": hpicfVrrpMIBCompliance4,
       "hpicfVrrpMIBCompliance5": hpicfVrrpMIBCompliance5,
       "hpicfVrrpMIBCompliance6": hpicfVrrpMIBCompliance6,
       "hpicfVrrpMIBCompliance7": hpicfVrrpMIBCompliance7,
       "hpicfVrrpMIBGroups": hpicfVrrpMIBGroups,
       "hpicfVrrpOperGroup": hpicfVrrpOperGroup,
       "hpicfVrrpTrackGroup": hpicfVrrpTrackGroup,
       "hpicfVrrpVrPingGroup": hpicfVrrpVrPingGroup,
       "hpicfVrrpNonstopGroup": hpicfVrrpNonstopGroup,
       "hpicfVrrpOperationsGroup": hpicfVrrpOperationsGroup,
       "hpicfVrrpTrackGroup1": hpicfVrrpTrackGroup1,
       "hpicfVrrpOperGroup1": hpicfVrrpOperGroup1,
       "hpicfVrrpOperationsGroup1": hpicfVrrpOperationsGroup1}
)
