# SNMP MIB module (CISCO-FABRIC-HFR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-FABRIC-HFR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:05 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(PhysicalIndex,
 entPhysicalIndex) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex",
    "entPhysicalIndex")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoFabricHfrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 257)
)
ciscoFabricHfrMIB.setRevisions(
        ("2009-04-14 00:00",
         "2006-01-01 00:00",
         "2003-06-09 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CfhPlane(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class CfhBundle(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class CfhAdminState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )



class CfhScaledPercentage(Gauge32, TextualConvention):
    status = "current"
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )



# MIB Managed Objects in the order of their OIDs

_CfhMIBNotifications_ObjectIdentity = ObjectIdentity
cfhMIBNotifications = _CfhMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 0)
)
_CiscoFabricHfrMIBObjects_ObjectIdentity = ObjectIdentity
ciscoFabricHfrMIBObjects = _CiscoFabricHfrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1)
)
_CfhGeneral_ObjectIdentity = ObjectIdentity
cfhGeneral = _CfhGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 1)
)


class _CfhGenPlaneStateTrapEnable_Type(TruthValue):
    """Custom type cfhGenPlaneStateTrapEnable based on TruthValue"""


_CfhGenPlaneStateTrapEnable_Object = MibScalar
cfhGenPlaneStateTrapEnable = _CfhGenPlaneStateTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 1, 1),
    _CfhGenPlaneStateTrapEnable_Type()
)
cfhGenPlaneStateTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfhGenPlaneStateTrapEnable.setStatus("current")


class _CfhGenBundleStateTrapEnable_Type(TruthValue):
    """Custom type cfhGenBundleStateTrapEnable based on TruthValue"""


_CfhGenBundleStateTrapEnable_Object = MibScalar
cfhGenBundleStateTrapEnable = _CfhGenBundleStateTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 1, 2),
    _CfhGenBundleStateTrapEnable_Type()
)
cfhGenBundleStateTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfhGenBundleStateTrapEnable.setStatus("current")


class _CfhGenBundleDownedLinkTrapEnable_Type(TruthValue):
    """Custom type cfhGenBundleDownedLinkTrapEnable based on TruthValue"""


_CfhGenBundleDownedLinkTrapEnable_Object = MibScalar
cfhGenBundleDownedLinkTrapEnable = _CfhGenBundleDownedLinkTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 1, 3),
    _CfhGenBundleDownedLinkTrapEnable_Type()
)
cfhGenBundleDownedLinkTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfhGenBundleDownedLinkTrapEnable.setStatus("current")
_CfhPlane_ObjectIdentity = ObjectIdentity
cfhPlane = _CfhPlane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 2)
)
_CfhPlaneTable_Object = MibTable
cfhPlaneTable = _CfhPlaneTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cfhPlaneTable.setStatus("current")
_CfhPlaneEntry_Object = MibTableRow
cfhPlaneEntry = _CfhPlaneEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 2, 1, 1)
)
cfhPlaneEntry.setIndexNames(
    (0, "CISCO-FABRIC-HFR-MIB", "cfhPlaneId"),
)
if mibBuilder.loadTexts:
    cfhPlaneEntry.setStatus("current")
_CfhPlaneId_Type = CfhPlane
_CfhPlaneId_Object = MibTableColumn
cfhPlaneId = _CfhPlaneId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 2, 1, 1, 1),
    _CfhPlaneId_Type()
)
cfhPlaneId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfhPlaneId.setStatus("current")
_CfhPlaneAdminStatus_Type = CfhAdminState
_CfhPlaneAdminStatus_Object = MibTableColumn
cfhPlaneAdminStatus = _CfhPlaneAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 2, 1, 1, 2),
    _CfhPlaneAdminStatus_Type()
)
cfhPlaneAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfhPlaneAdminStatus.setStatus("current")


class _CfhPlaneOperStatus_Type(Integer32):
    """Custom type cfhPlaneOperStatus based on Integer32"""
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
        *(("down", 2),
          ("mcastDown", 3),
          ("oos", 4),
          ("up", 1))
    )


_CfhPlaneOperStatus_Type.__name__ = "Integer32"
_CfhPlaneOperStatus_Object = MibTableColumn
cfhPlaneOperStatus = _CfhPlaneOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 2, 1, 1, 3),
    _CfhPlaneOperStatus_Type()
)
cfhPlaneOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfhPlaneOperStatus.setStatus("current")
_CfhPlaneTotalBundles_Type = Unsigned32
_CfhPlaneTotalBundles_Object = MibTableColumn
cfhPlaneTotalBundles = _CfhPlaneTotalBundles_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 2, 1, 1, 4),
    _CfhPlaneTotalBundles_Type()
)
cfhPlaneTotalBundles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfhPlaneTotalBundles.setStatus("current")
_CfhPlaneDownedBundles_Type = Gauge32
_CfhPlaneDownedBundles_Object = MibTableColumn
cfhPlaneDownedBundles = _CfhPlaneDownedBundles_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 2, 1, 1, 5),
    _CfhPlaneDownedBundles_Type()
)
cfhPlaneDownedBundles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfhPlaneDownedBundles.setStatus("current")
_CfhPlaneStatsTable_Object = MibTable
cfhPlaneStatsTable = _CfhPlaneStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cfhPlaneStatsTable.setStatus("current")
_CfhPlaneStatsEntry_Object = MibTableRow
cfhPlaneStatsEntry = _CfhPlaneStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cfhPlaneStatsEntry.setStatus("current")
_CfhPlaneStatsRxDataCells_Type = Counter64
_CfhPlaneStatsRxDataCells_Object = MibTableColumn
cfhPlaneStatsRxDataCells = _CfhPlaneStatsRxDataCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 2, 2, 1, 1),
    _CfhPlaneStatsRxDataCells_Type()
)
cfhPlaneStatsRxDataCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfhPlaneStatsRxDataCells.setStatus("current")
_CfhPlaneStatsTxDataCells_Type = Counter64
_CfhPlaneStatsTxDataCells_Object = MibTableColumn
cfhPlaneStatsTxDataCells = _CfhPlaneStatsTxDataCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 2, 2, 1, 2),
    _CfhPlaneStatsTxDataCells_Type()
)
cfhPlaneStatsTxDataCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfhPlaneStatsTxDataCells.setStatus("current")
_CfhPlaneStatsRxCECells_Type = Counter32
_CfhPlaneStatsRxCECells_Object = MibTableColumn
cfhPlaneStatsRxCECells = _CfhPlaneStatsRxCECells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 2, 2, 1, 3),
    _CfhPlaneStatsRxCECells_Type()
)
cfhPlaneStatsRxCECells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfhPlaneStatsRxCECells.setStatus("current")
_CfhPlaneStatsRxUCECells_Type = Counter32
_CfhPlaneStatsRxUCECells_Object = MibTableColumn
cfhPlaneStatsRxUCECells = _CfhPlaneStatsRxUCECells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 2, 2, 1, 4),
    _CfhPlaneStatsRxUCECells_Type()
)
cfhPlaneStatsRxUCECells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfhPlaneStatsRxUCECells.setStatus("current")
_CfhPlaneStatsRxPECells_Type = Counter32
_CfhPlaneStatsRxPECells_Object = MibTableColumn
cfhPlaneStatsRxPECells = _CfhPlaneStatsRxPECells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 2, 2, 1, 5),
    _CfhPlaneStatsRxPECells_Type()
)
cfhPlaneStatsRxPECells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfhPlaneStatsRxPECells.setStatus("current")
_CfhPlaneStatsUnicastLostCells_Type = Counter32
_CfhPlaneStatsUnicastLostCells_Object = MibTableColumn
cfhPlaneStatsUnicastLostCells = _CfhPlaneStatsUnicastLostCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 2, 2, 1, 6),
    _CfhPlaneStatsUnicastLostCells_Type()
)
cfhPlaneStatsUnicastLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfhPlaneStatsUnicastLostCells.setStatus("current")
_CfhPlaneStatsMulticastLostCells_Type = Counter32
_CfhPlaneStatsMulticastLostCells_Object = MibTableColumn
cfhPlaneStatsMulticastLostCells = _CfhPlaneStatsMulticastLostCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 2, 2, 1, 7),
    _CfhPlaneStatsMulticastLostCells_Type()
)
cfhPlaneStatsMulticastLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfhPlaneStatsMulticastLostCells.setStatus("current")
_CfhPlaneStatsCounterDiscTime_Type = TimeStamp
_CfhPlaneStatsCounterDiscTime_Object = MibTableColumn
cfhPlaneStatsCounterDiscTime = _CfhPlaneStatsCounterDiscTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 2, 2, 1, 8),
    _CfhPlaneStatsCounterDiscTime_Type()
)
cfhPlaneStatsCounterDiscTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfhPlaneStatsCounterDiscTime.setStatus("current")
_CfhPlaneCapacityThreshold_Type = Unsigned32
_CfhPlaneCapacityThreshold_Object = MibScalar
cfhPlaneCapacityThreshold = _CfhPlaneCapacityThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 2, 3),
    _CfhPlaneCapacityThreshold_Type()
)
cfhPlaneCapacityThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfhPlaneCapacityThreshold.setStatus("current")
_CfhBundle_ObjectIdentity = ObjectIdentity
cfhBundle = _CfhBundle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 3)
)
_CfhBundleTotal_Type = Unsigned32
_CfhBundleTotal_Object = MibScalar
cfhBundleTotal = _CfhBundleTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 3, 1),
    _CfhBundleTotal_Type()
)
cfhBundleTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfhBundleTotal.setStatus("current")
_CfhBundleDowned_Type = Gauge32
_CfhBundleDowned_Object = MibScalar
cfhBundleDowned = _CfhBundleDowned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 3, 2),
    _CfhBundleDowned_Type()
)
cfhBundleDowned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfhBundleDowned.setStatus("current")
_CfhBundleTable_Object = MibTable
cfhBundleTable = _CfhBundleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cfhBundleTable.setStatus("current")
_CfhBundleEntry_Object = MibTableRow
cfhBundleEntry = _CfhBundleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 3, 3, 1)
)
cfhBundleEntry.setIndexNames(
    (0, "CISCO-FABRIC-HFR-MIB", "cfhBundleId"),
)
if mibBuilder.loadTexts:
    cfhBundleEntry.setStatus("current")
_CfhBundleId_Type = CfhBundle
_CfhBundleId_Object = MibTableColumn
cfhBundleId = _CfhBundleId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 3, 3, 1, 1),
    _CfhBundleId_Type()
)
cfhBundleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfhBundleId.setStatus("current")
_CfhBundleName_Type = SnmpAdminString
_CfhBundleName_Object = MibTableColumn
cfhBundleName = _CfhBundleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 3, 3, 1, 2),
    _CfhBundleName_Type()
)
cfhBundleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfhBundleName.setStatus("current")
_CfhBundlePlane_Type = CfhPlane
_CfhBundlePlane_Object = MibTableColumn
cfhBundlePlane = _CfhBundlePlane_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 3, 3, 1, 3),
    _CfhBundlePlane_Type()
)
cfhBundlePlane.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfhBundlePlane.setStatus("current")


class _CfhBundleOperStatus_Type(Integer32):
    """Custom type cfhBundleOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CfhBundleOperStatus_Type.__name__ = "Integer32"
_CfhBundleOperStatus_Object = MibTableColumn
cfhBundleOperStatus = _CfhBundleOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 3, 3, 1, 4),
    _CfhBundleOperStatus_Type()
)
cfhBundleOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfhBundleOperStatus.setStatus("current")
_CfhBundleTotalLinks_Type = Unsigned32
_CfhBundleTotalLinks_Object = MibTableColumn
cfhBundleTotalLinks = _CfhBundleTotalLinks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 3, 3, 1, 5),
    _CfhBundleTotalLinks_Type()
)
cfhBundleTotalLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfhBundleTotalLinks.setStatus("current")
_CfhBundleDownedLinks_Type = Gauge32
_CfhBundleDownedLinks_Object = MibTableColumn
cfhBundleDownedLinks = _CfhBundleDownedLinks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 3, 3, 1, 6),
    _CfhBundleDownedLinks_Type()
)
cfhBundleDownedLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfhBundleDownedLinks.setStatus("current")
_CfhBundlePortLCRCardIndex_Type = PhysicalIndex
_CfhBundlePortLCRCardIndex_Object = MibTableColumn
cfhBundlePortLCRCardIndex = _CfhBundlePortLCRCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 3, 3, 1, 7),
    _CfhBundlePortLCRCardIndex_Type()
)
cfhBundlePortLCRCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfhBundlePortLCRCardIndex.setStatus("current")
_CfhBundlePortLCRId_Type = Unsigned32
_CfhBundlePortLCRId_Object = MibTableColumn
cfhBundlePortLCRId = _CfhBundlePortLCRId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 3, 3, 1, 8),
    _CfhBundlePortLCRId_Type()
)
cfhBundlePortLCRId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfhBundlePortLCRId.setStatus("current")
_CfhBundlePortSecondCardIndex_Type = PhysicalIndex
_CfhBundlePortSecondCardIndex_Object = MibTableColumn
cfhBundlePortSecondCardIndex = _CfhBundlePortSecondCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 3, 3, 1, 9),
    _CfhBundlePortSecondCardIndex_Type()
)
cfhBundlePortSecondCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfhBundlePortSecondCardIndex.setStatus("current")
_CfhBundlePortSecondId_Type = Unsigned32
_CfhBundlePortSecondId_Object = MibTableColumn
cfhBundlePortSecondId = _CfhBundlePortSecondId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 3, 3, 1, 10),
    _CfhBundlePortSecondId_Type()
)
cfhBundlePortSecondId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfhBundlePortSecondId.setStatus("current")
_CfhBundlePort_ObjectIdentity = ObjectIdentity
cfhBundlePort = _CfhBundlePort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 4)
)
_CfhBundlePortTotalNumber_Type = Unsigned32
_CfhBundlePortTotalNumber_Object = MibScalar
cfhBundlePortTotalNumber = _CfhBundlePortTotalNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 4, 1),
    _CfhBundlePortTotalNumber_Type()
)
cfhBundlePortTotalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfhBundlePortTotalNumber.setStatus("current")
_CfhBundlePortTable_Object = MibTable
cfhBundlePortTable = _CfhBundlePortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cfhBundlePortTable.setStatus("current")
_CfhBundlePortEntry_Object = MibTableRow
cfhBundlePortEntry = _CfhBundlePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 4, 2, 1)
)
cfhBundlePortEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-FABRIC-HFR-MIB", "cfhBundlePortId"),
)
if mibBuilder.loadTexts:
    cfhBundlePortEntry.setStatus("current")


class _CfhBundlePortId_Type(Unsigned32):
    """Custom type cfhBundlePortId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CfhBundlePortId_Type.__name__ = "Unsigned32"
_CfhBundlePortId_Object = MibTableColumn
cfhBundlePortId = _CfhBundlePortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 4, 2, 1, 1),
    _CfhBundlePortId_Type()
)
cfhBundlePortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfhBundlePortId.setStatus("current")
_CfhBundlePortAdminState_Type = CfhAdminState
_CfhBundlePortAdminState_Object = MibTableColumn
cfhBundlePortAdminState = _CfhBundlePortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 4, 2, 1, 3),
    _CfhBundlePortAdminState_Type()
)
cfhBundlePortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfhBundlePortAdminState.setStatus("current")


class _CfhBundlePortOperState_Type(Integer32):
    """Custom type cfhBundlePortOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("unknown", 1),
          ("up", 2))
    )


_CfhBundlePortOperState_Type.__name__ = "Integer32"
_CfhBundlePortOperState_Object = MibTableColumn
cfhBundlePortOperState = _CfhBundlePortOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 4, 2, 1, 4),
    _CfhBundlePortOperState_Type()
)
cfhBundlePortOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfhBundlePortOperState.setStatus("current")
_CfhBundlePortGrpId_Type = CfhBundle
_CfhBundlePortGrpId_Object = MibTableColumn
cfhBundlePortGrpId = _CfhBundlePortGrpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 4, 2, 1, 5),
    _CfhBundlePortGrpId_Type()
)
cfhBundlePortGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfhBundlePortGrpId.setStatus("current")
_CfhBundlePortStatsTable_Object = MibTable
cfhBundlePortStatsTable = _CfhBundlePortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 4, 3)
)
if mibBuilder.loadTexts:
    cfhBundlePortStatsTable.setStatus("current")
_CfhBundlePortStatsEntry_Object = MibTableRow
cfhBundlePortStatsEntry = _CfhBundlePortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    cfhBundlePortStatsEntry.setStatus("current")
_CfhBundlePortStatsRxDataCells_Type = Counter64
_CfhBundlePortStatsRxDataCells_Object = MibTableColumn
cfhBundlePortStatsRxDataCells = _CfhBundlePortStatsRxDataCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 4, 3, 1, 1),
    _CfhBundlePortStatsRxDataCells_Type()
)
cfhBundlePortStatsRxDataCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfhBundlePortStatsRxDataCells.setStatus("current")
_CfhBundlePortStatsTxDataCells_Type = Counter64
_CfhBundlePortStatsTxDataCells_Object = MibTableColumn
cfhBundlePortStatsTxDataCells = _CfhBundlePortStatsTxDataCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 4, 3, 1, 2),
    _CfhBundlePortStatsTxDataCells_Type()
)
cfhBundlePortStatsTxDataCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfhBundlePortStatsTxDataCells.setStatus("current")
_CfhBundlePortStatsRxCECells_Type = Counter32
_CfhBundlePortStatsRxCECells_Object = MibTableColumn
cfhBundlePortStatsRxCECells = _CfhBundlePortStatsRxCECells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 4, 3, 1, 3),
    _CfhBundlePortStatsRxCECells_Type()
)
cfhBundlePortStatsRxCECells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfhBundlePortStatsRxCECells.setStatus("current")
_CfhBundlePortStatsRxUCECells_Type = Counter32
_CfhBundlePortStatsRxUCECells_Object = MibTableColumn
cfhBundlePortStatsRxUCECells = _CfhBundlePortStatsRxUCECells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 4, 3, 1, 4),
    _CfhBundlePortStatsRxUCECells_Type()
)
cfhBundlePortStatsRxUCECells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfhBundlePortStatsRxUCECells.setStatus("current")
_CfhBundlePortStatsRxPECells_Type = Counter32
_CfhBundlePortStatsRxPECells_Object = MibTableColumn
cfhBundlePortStatsRxPECells = _CfhBundlePortStatsRxPECells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 4, 3, 1, 5),
    _CfhBundlePortStatsRxPECells_Type()
)
cfhBundlePortStatsRxPECells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfhBundlePortStatsRxPECells.setStatus("current")
_CfhBundlePortStatsHighRxCECells_Type = Gauge32
_CfhBundlePortStatsHighRxCECells_Object = MibTableColumn
cfhBundlePortStatsHighRxCECells = _CfhBundlePortStatsHighRxCECells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 4, 3, 1, 6),
    _CfhBundlePortStatsHighRxCECells_Type()
)
cfhBundlePortStatsHighRxCECells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfhBundlePortStatsHighRxCECells.setStatus("current")
_CfhBundlePortStatsHighRxUCECells_Type = Gauge32
_CfhBundlePortStatsHighRxUCECells_Object = MibTableColumn
cfhBundlePortStatsHighRxUCECells = _CfhBundlePortStatsHighRxUCECells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 4, 3, 1, 7),
    _CfhBundlePortStatsHighRxUCECells_Type()
)
cfhBundlePortStatsHighRxUCECells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfhBundlePortStatsHighRxUCECells.setStatus("current")
_CfhBundlePortStatsHighRxPECells_Type = Gauge32
_CfhBundlePortStatsHighRxPECells_Object = MibTableColumn
cfhBundlePortStatsHighRxPECells = _CfhBundlePortStatsHighRxPECells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 4, 3, 1, 8),
    _CfhBundlePortStatsHighRxPECells_Type()
)
cfhBundlePortStatsHighRxPECells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfhBundlePortStatsHighRxPECells.setStatus("current")
_CfhCard_ObjectIdentity = ObjectIdentity
cfhCard = _CfhCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 5)
)
_CfhCardTable_Object = MibTable
cfhCardTable = _CfhCardTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cfhCardTable.setStatus("current")
_CfhCardEntry_Object = MibTableRow
cfhCardEntry = _CfhCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 5, 1, 1)
)
cfhCardEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cfhCardEntry.setStatus("current")
_CfhCardFabInUse_Type = TruthValue
_CfhCardFabInUse_Object = MibTableColumn
cfhCardFabInUse = _CfhCardFabInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 5, 1, 1, 1),
    _CfhCardFabInUse_Type()
)
cfhCardFabInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfhCardFabInUse.setStatus("current")
_CfhCardFabUsage_Type = CfhScaledPercentage
_CfhCardFabUsage_Object = MibTableColumn
cfhCardFabUsage = _CfhCardFabUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 5, 1, 1, 2),
    _CfhCardFabUsage_Type()
)
cfhCardFabUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfhCardFabUsage.setStatus("current")
if mibBuilder.loadTexts:
    cfhCardFabUsage.setUnits("thousandths of a percent")
_CfhCardFabInUseDiscTime_Type = TimeStamp
_CfhCardFabInUseDiscTime_Object = MibTableColumn
cfhCardFabInUseDiscTime = _CfhCardFabInUseDiscTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 5, 1, 1, 3),
    _CfhCardFabInUseDiscTime_Type()
)
cfhCardFabInUseDiscTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfhCardFabInUseDiscTime.setStatus("current")
_CfhCardPlaneTable_Object = MibTable
cfhCardPlaneTable = _CfhCardPlaneTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 5, 2)
)
if mibBuilder.loadTexts:
    cfhCardPlaneTable.setStatus("current")
_CfhCardPlaneEntry_Object = MibTableRow
cfhCardPlaneEntry = _CfhCardPlaneEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 5, 2, 1)
)
cfhCardPlaneEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-FABRIC-HFR-MIB", "cfhPlaneId"),
)
if mibBuilder.loadTexts:
    cfhCardPlaneEntry.setStatus("current")
_CfhCardPlaneTxConnectivity_Type = TruthValue
_CfhCardPlaneTxConnectivity_Object = MibTableColumn
cfhCardPlaneTxConnectivity = _CfhCardPlaneTxConnectivity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 5, 2, 1, 1),
    _CfhCardPlaneTxConnectivity_Type()
)
cfhCardPlaneTxConnectivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfhCardPlaneTxConnectivity.setStatus("current")
_CfhCardPlaneRxConnectivity_Type = TruthValue
_CfhCardPlaneRxConnectivity_Object = MibTableColumn
cfhCardPlaneRxConnectivity = _CfhCardPlaneRxConnectivity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 1, 5, 2, 1, 2),
    _CfhCardPlaneRxConnectivity_Type()
)
cfhCardPlaneRxConnectivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfhCardPlaneRxConnectivity.setStatus("current")
_CfhMIBConformance_ObjectIdentity = ObjectIdentity
cfhMIBConformance = _CfhMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 3)
)
_CfhMIBCompliances_ObjectIdentity = ObjectIdentity
cfhMIBCompliances = _CfhMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 3, 1)
)
_CfhMIBGroups_ObjectIdentity = ObjectIdentity
cfhMIBGroups = _CfhMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 3, 2)
)
cfhPlaneEntry.registerAugmentions(
    ("CISCO-FABRIC-HFR-MIB",
     "cfhPlaneStatsEntry")
)
cfhPlaneStatsEntry.setIndexNames(*cfhPlaneEntry.getIndexNames())
cfhBundlePortEntry.registerAugmentions(
    ("CISCO-FABRIC-HFR-MIB",
     "cfhBundlePortStatsEntry")
)
cfhBundlePortStatsEntry.setIndexNames(*cfhBundlePortEntry.getIndexNames())

# Managed Objects groups

cfhGenInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 3, 2, 1)
)
cfhGenInfoGroup.setObjects(
      *(("CISCO-FABRIC-HFR-MIB", "cfhGenPlaneStateTrapEnable"),
        ("CISCO-FABRIC-HFR-MIB", "cfhGenBundleStateTrapEnable"),
        ("CISCO-FABRIC-HFR-MIB", "cfhGenBundleDownedLinkTrapEnable"))
)
if mibBuilder.loadTexts:
    cfhGenInfoGroup.setStatus("current")

cfhPlaneGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 3, 2, 2)
)
cfhPlaneGroup.setObjects(
      *(("CISCO-FABRIC-HFR-MIB", "cfhPlaneAdminStatus"),
        ("CISCO-FABRIC-HFR-MIB", "cfhPlaneOperStatus"),
        ("CISCO-FABRIC-HFR-MIB", "cfhPlaneTotalBundles"),
        ("CISCO-FABRIC-HFR-MIB", "cfhPlaneDownedBundles"),
        ("CISCO-FABRIC-HFR-MIB", "cfhPlaneStatsRxDataCells"),
        ("CISCO-FABRIC-HFR-MIB", "cfhPlaneStatsTxDataCells"),
        ("CISCO-FABRIC-HFR-MIB", "cfhPlaneStatsRxCECells"),
        ("CISCO-FABRIC-HFR-MIB", "cfhPlaneStatsRxUCECells"),
        ("CISCO-FABRIC-HFR-MIB", "cfhPlaneStatsRxPECells"),
        ("CISCO-FABRIC-HFR-MIB", "cfhPlaneStatsUnicastLostCells"),
        ("CISCO-FABRIC-HFR-MIB", "cfhPlaneStatsMulticastLostCells"),
        ("CISCO-FABRIC-HFR-MIB", "cfhPlaneStatsCounterDiscTime"))
)
if mibBuilder.loadTexts:
    cfhPlaneGroup.setStatus("current")

cfhBundleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 3, 2, 3)
)
cfhBundleGroup.setObjects(
      *(("CISCO-FABRIC-HFR-MIB", "cfhBundleTotal"),
        ("CISCO-FABRIC-HFR-MIB", "cfhBundleDowned"),
        ("CISCO-FABRIC-HFR-MIB", "cfhBundleName"),
        ("CISCO-FABRIC-HFR-MIB", "cfhBundlePlane"),
        ("CISCO-FABRIC-HFR-MIB", "cfhBundleOperStatus"),
        ("CISCO-FABRIC-HFR-MIB", "cfhBundleTotalLinks"),
        ("CISCO-FABRIC-HFR-MIB", "cfhBundleDownedLinks"),
        ("CISCO-FABRIC-HFR-MIB", "cfhBundlePortLCRCardIndex"),
        ("CISCO-FABRIC-HFR-MIB", "cfhBundlePortLCRId"),
        ("CISCO-FABRIC-HFR-MIB", "cfhBundlePortSecondCardIndex"),
        ("CISCO-FABRIC-HFR-MIB", "cfhBundlePortSecondId"))
)
if mibBuilder.loadTexts:
    cfhBundleGroup.setStatus("current")

cfhBundlePortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 3, 2, 4)
)
cfhBundlePortGroup.setObjects(
      *(("CISCO-FABRIC-HFR-MIB", "cfhBundlePortTotalNumber"),
        ("CISCO-FABRIC-HFR-MIB", "cfhBundlePortAdminState"),
        ("CISCO-FABRIC-HFR-MIB", "cfhBundlePortOperState"),
        ("CISCO-FABRIC-HFR-MIB", "cfhBundlePortGrpId"),
        ("CISCO-FABRIC-HFR-MIB", "cfhBundlePortStatsRxDataCells"),
        ("CISCO-FABRIC-HFR-MIB", "cfhBundlePortStatsTxDataCells"),
        ("CISCO-FABRIC-HFR-MIB", "cfhBundlePortStatsRxCECells"),
        ("CISCO-FABRIC-HFR-MIB", "cfhBundlePortStatsRxUCECells"),
        ("CISCO-FABRIC-HFR-MIB", "cfhBundlePortStatsRxPECells"),
        ("CISCO-FABRIC-HFR-MIB", "cfhBundlePortStatsHighRxCECells"),
        ("CISCO-FABRIC-HFR-MIB", "cfhBundlePortStatsHighRxUCECells"),
        ("CISCO-FABRIC-HFR-MIB", "cfhBundlePortStatsHighRxPECells"))
)
if mibBuilder.loadTexts:
    cfhBundlePortGroup.setStatus("current")

cfhCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 3, 2, 5)
)
cfhCardGroup.setObjects(
      *(("CISCO-FABRIC-HFR-MIB", "cfhCardFabInUse"),
        ("CISCO-FABRIC-HFR-MIB", "cfhCardFabUsage"),
        ("CISCO-FABRIC-HFR-MIB", "cfhCardFabInUseDiscTime"),
        ("CISCO-FABRIC-HFR-MIB", "cfhCardPlaneTxConnectivity"),
        ("CISCO-FABRIC-HFR-MIB", "cfhCardPlaneRxConnectivity"))
)
if mibBuilder.loadTexts:
    cfhCardGroup.setStatus("current")

cfhFabricCapacityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 3, 2, 7)
)
cfhFabricCapacityGroup.setObjects(
    ("CISCO-FABRIC-HFR-MIB", "cfhPlaneCapacityThreshold")
)
if mibBuilder.loadTexts:
    cfhFabricCapacityGroup.setStatus("current")


# Notification objects

cfhPlaneStateNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 0, 1)
)
cfhPlaneStateNotification.setObjects(
    ("CISCO-FABRIC-HFR-MIB", "cfhPlaneOperStatus")
)
if mibBuilder.loadTexts:
    cfhPlaneStateNotification.setStatus(
        "current"
    )

cfhBundleStateNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 0, 2)
)
cfhBundleStateNotification.setObjects(
      *(("CISCO-FABRIC-HFR-MIB", "cfhBundleOperStatus"),
        ("CISCO-FABRIC-HFR-MIB", "cfhBundlePlane"),
        ("CISCO-FABRIC-HFR-MIB", "cfhBundleName"))
)
if mibBuilder.loadTexts:
    cfhBundleStateNotification.setStatus(
        "current"
    )

cfhBundleDownedLinkNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 0, 3)
)
cfhBundleDownedLinkNotification.setObjects(
      *(("CISCO-FABRIC-HFR-MIB", "cfhBundleOperStatus"),
        ("CISCO-FABRIC-HFR-MIB", "cfhBundlePlane"),
        ("CISCO-FABRIC-HFR-MIB", "cfhBundleDownedLinks"),
        ("CISCO-FABRIC-HFR-MIB", "cfhBundleName"))
)
if mibBuilder.loadTexts:
    cfhBundleDownedLinkNotification.setStatus(
        "current"
    )


# Notifications groups

cfhNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 3, 2, 6)
)
cfhNotificationsGroup.setObjects(
      *(("CISCO-FABRIC-HFR-MIB", "cfhPlaneStateNotification"),
        ("CISCO-FABRIC-HFR-MIB", "cfhBundleStateNotification"),
        ("CISCO-FABRIC-HFR-MIB", "cfhBundleDownedLinkNotification"))
)
if mibBuilder.loadTexts:
    cfhNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cfhMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cfhMIBCompliance.setStatus(
        "deprecated"
    )

cfhMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 257, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cfhMIBCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FABRIC-HFR-MIB",
    **{"CfhPlane": CfhPlane,
       "CfhBundle": CfhBundle,
       "CfhAdminState": CfhAdminState,
       "CfhScaledPercentage": CfhScaledPercentage,
       "ciscoFabricHfrMIB": ciscoFabricHfrMIB,
       "cfhMIBNotifications": cfhMIBNotifications,
       "cfhPlaneStateNotification": cfhPlaneStateNotification,
       "cfhBundleStateNotification": cfhBundleStateNotification,
       "cfhBundleDownedLinkNotification": cfhBundleDownedLinkNotification,
       "ciscoFabricHfrMIBObjects": ciscoFabricHfrMIBObjects,
       "cfhGeneral": cfhGeneral,
       "cfhGenPlaneStateTrapEnable": cfhGenPlaneStateTrapEnable,
       "cfhGenBundleStateTrapEnable": cfhGenBundleStateTrapEnable,
       "cfhGenBundleDownedLinkTrapEnable": cfhGenBundleDownedLinkTrapEnable,
       "cfhPlane": cfhPlane,
       "cfhPlaneTable": cfhPlaneTable,
       "cfhPlaneEntry": cfhPlaneEntry,
       "cfhPlaneId": cfhPlaneId,
       "cfhPlaneAdminStatus": cfhPlaneAdminStatus,
       "cfhPlaneOperStatus": cfhPlaneOperStatus,
       "cfhPlaneTotalBundles": cfhPlaneTotalBundles,
       "cfhPlaneDownedBundles": cfhPlaneDownedBundles,
       "cfhPlaneStatsTable": cfhPlaneStatsTable,
       "cfhPlaneStatsEntry": cfhPlaneStatsEntry,
       "cfhPlaneStatsRxDataCells": cfhPlaneStatsRxDataCells,
       "cfhPlaneStatsTxDataCells": cfhPlaneStatsTxDataCells,
       "cfhPlaneStatsRxCECells": cfhPlaneStatsRxCECells,
       "cfhPlaneStatsRxUCECells": cfhPlaneStatsRxUCECells,
       "cfhPlaneStatsRxPECells": cfhPlaneStatsRxPECells,
       "cfhPlaneStatsUnicastLostCells": cfhPlaneStatsUnicastLostCells,
       "cfhPlaneStatsMulticastLostCells": cfhPlaneStatsMulticastLostCells,
       "cfhPlaneStatsCounterDiscTime": cfhPlaneStatsCounterDiscTime,
       "cfhPlaneCapacityThreshold": cfhPlaneCapacityThreshold,
       "cfhBundle": cfhBundle,
       "cfhBundleTotal": cfhBundleTotal,
       "cfhBundleDowned": cfhBundleDowned,
       "cfhBundleTable": cfhBundleTable,
       "cfhBundleEntry": cfhBundleEntry,
       "cfhBundleId": cfhBundleId,
       "cfhBundleName": cfhBundleName,
       "cfhBundlePlane": cfhBundlePlane,
       "cfhBundleOperStatus": cfhBundleOperStatus,
       "cfhBundleTotalLinks": cfhBundleTotalLinks,
       "cfhBundleDownedLinks": cfhBundleDownedLinks,
       "cfhBundlePortLCRCardIndex": cfhBundlePortLCRCardIndex,
       "cfhBundlePortLCRId": cfhBundlePortLCRId,
       "cfhBundlePortSecondCardIndex": cfhBundlePortSecondCardIndex,
       "cfhBundlePortSecondId": cfhBundlePortSecondId,
       "cfhBundlePort": cfhBundlePort,
       "cfhBundlePortTotalNumber": cfhBundlePortTotalNumber,
       "cfhBundlePortTable": cfhBundlePortTable,
       "cfhBundlePortEntry": cfhBundlePortEntry,
       "cfhBundlePortId": cfhBundlePortId,
       "cfhBundlePortAdminState": cfhBundlePortAdminState,
       "cfhBundlePortOperState": cfhBundlePortOperState,
       "cfhBundlePortGrpId": cfhBundlePortGrpId,
       "cfhBundlePortStatsTable": cfhBundlePortStatsTable,
       "cfhBundlePortStatsEntry": cfhBundlePortStatsEntry,
       "cfhBundlePortStatsRxDataCells": cfhBundlePortStatsRxDataCells,
       "cfhBundlePortStatsTxDataCells": cfhBundlePortStatsTxDataCells,
       "cfhBundlePortStatsRxCECells": cfhBundlePortStatsRxCECells,
       "cfhBundlePortStatsRxUCECells": cfhBundlePortStatsRxUCECells,
       "cfhBundlePortStatsRxPECells": cfhBundlePortStatsRxPECells,
       "cfhBundlePortStatsHighRxCECells": cfhBundlePortStatsHighRxCECells,
       "cfhBundlePortStatsHighRxUCECells": cfhBundlePortStatsHighRxUCECells,
       "cfhBundlePortStatsHighRxPECells": cfhBundlePortStatsHighRxPECells,
       "cfhCard": cfhCard,
       "cfhCardTable": cfhCardTable,
       "cfhCardEntry": cfhCardEntry,
       "cfhCardFabInUse": cfhCardFabInUse,
       "cfhCardFabUsage": cfhCardFabUsage,
       "cfhCardFabInUseDiscTime": cfhCardFabInUseDiscTime,
       "cfhCardPlaneTable": cfhCardPlaneTable,
       "cfhCardPlaneEntry": cfhCardPlaneEntry,
       "cfhCardPlaneTxConnectivity": cfhCardPlaneTxConnectivity,
       "cfhCardPlaneRxConnectivity": cfhCardPlaneRxConnectivity,
       "cfhMIBConformance": cfhMIBConformance,
       "cfhMIBCompliances": cfhMIBCompliances,
       "cfhMIBCompliance": cfhMIBCompliance,
       "cfhMIBCompliance1": cfhMIBCompliance1,
       "cfhMIBGroups": cfhMIBGroups,
       "cfhGenInfoGroup": cfhGenInfoGroup,
       "cfhPlaneGroup": cfhPlaneGroup,
       "cfhBundleGroup": cfhBundleGroup,
       "cfhBundlePortGroup": cfhBundlePortGroup,
       "cfhCardGroup": cfhCardGroup,
       "cfhNotificationsGroup": cfhNotificationsGroup,
       "cfhFabricCapacityGroup": cfhFabricCapacityGroup}
)
