# SNMP MIB module (CISCO-ITP-GRT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ITP-GRT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:21 2024
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

(cgspCLLICode,
 cgspEventSequenceNumber,
 cgspInstDisplayName,
 cgspInstNetwork) = mibBuilder.importSymbols(
    "CISCO-ITP-GSP-MIB",
    "cgspCLLICode",
    "cgspEventSequenceNumber",
    "cgspInstDisplayName",
    "cgspInstNetwork")

(CItpTcDisplayPC,
 CItpTcLinksetId,
 CItpTcPointCode,
 CItpTcQos,
 CItpTcRouteTableName,
 CItpTcServiceIndicator,
 CItpTcTableLoadStatus,
 CItpTcURL) = mibBuilder.importSymbols(
    "CISCO-ITP-TC-MIB",
    "CItpTcDisplayPC",
    "CItpTcLinksetId",
    "CItpTcPointCode",
    "CItpTcQos",
    "CItpTcRouteTableName",
    "CItpTcServiceIndicator",
    "CItpTcTableLoadStatus",
    "CItpTcURL")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoGrtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 334)
)
ciscoGrtMIB.setRevisions(
        ("2008-05-01 00:00",
         "2003-03-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CgrtDisplayPCSI(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoGrtNotifications_ObjectIdentity = ObjectIdentity
ciscoGrtNotifications = _CiscoGrtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 0)
)
_CiscoGrtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoGrtMIBObjects = _CiscoGrtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1)
)
_CgrtScalars_ObjectIdentity = ObjectIdentity
cgrtScalars = _CgrtScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 1)
)


class _CgrtRouteMaxDynamic_Type(Integer32):
    """Custom type cgrtRouteMaxDynamic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_CgrtRouteMaxDynamic_Type.__name__ = "Integer32"
_CgrtRouteMaxDynamic_Object = MibScalar
cgrtRouteMaxDynamic = _CgrtRouteMaxDynamic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 1, 7),
    _CgrtRouteMaxDynamic_Type()
)
cgrtRouteMaxDynamic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgrtRouteMaxDynamic.setStatus("current")


class _CgrtDestNotifDelayTime_Type(Unsigned32):
    """Custom type cgrtDestNotifDelayTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_CgrtDestNotifDelayTime_Type.__name__ = "Unsigned32"
_CgrtDestNotifDelayTime_Object = MibScalar
cgrtDestNotifDelayTime = _CgrtDestNotifDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 1, 11),
    _CgrtDestNotifDelayTime_Type()
)
cgrtDestNotifDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgrtDestNotifDelayTime.setStatus("deprecated")
if mibBuilder.loadTexts:
    cgrtDestNotifDelayTime.setUnits("seconds")


class _CgrtDestNotifWindowTime_Type(Integer32):
    """Custom type cgrtDestNotifWindowTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 900),
    )


_CgrtDestNotifWindowTime_Type.__name__ = "Integer32"
_CgrtDestNotifWindowTime_Object = MibScalar
cgrtDestNotifWindowTime = _CgrtDestNotifWindowTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 1, 12),
    _CgrtDestNotifWindowTime_Type()
)
cgrtDestNotifWindowTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgrtDestNotifWindowTime.setStatus("deprecated")
if mibBuilder.loadTexts:
    cgrtDestNotifWindowTime.setUnits("seconds")


class _CgrtDestNotifMaxPerWindow_Type(Integer32):
    """Custom type cgrtDestNotifMaxPerWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 9000),
    )


_CgrtDestNotifMaxPerWindow_Type.__name__ = "Integer32"
_CgrtDestNotifMaxPerWindow_Object = MibScalar
cgrtDestNotifMaxPerWindow = _CgrtDestNotifMaxPerWindow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 1, 13),
    _CgrtDestNotifMaxPerWindow_Type()
)
cgrtDestNotifMaxPerWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgrtDestNotifMaxPerWindow.setStatus("deprecated")


class _CgrtDestNotifEnabled_Type(TruthValue):
    """Custom type cgrtDestNotifEnabled based on TruthValue"""


_CgrtDestNotifEnabled_Object = MibScalar
cgrtDestNotifEnabled = _CgrtDestNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 1, 14),
    _CgrtDestNotifEnabled_Type()
)
cgrtDestNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgrtDestNotifEnabled.setStatus("deprecated")


class _CgrtMgmtNotifDelayTime_Type(Unsigned32):
    """Custom type cgrtMgmtNotifDelayTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_CgrtMgmtNotifDelayTime_Type.__name__ = "Unsigned32"
_CgrtMgmtNotifDelayTime_Object = MibScalar
cgrtMgmtNotifDelayTime = _CgrtMgmtNotifDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 1, 16),
    _CgrtMgmtNotifDelayTime_Type()
)
cgrtMgmtNotifDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgrtMgmtNotifDelayTime.setStatus("deprecated")
if mibBuilder.loadTexts:
    cgrtMgmtNotifDelayTime.setUnits("seconds")


class _CgrtMgmtNotifWindowTime_Type(Integer32):
    """Custom type cgrtMgmtNotifWindowTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 900),
    )


_CgrtMgmtNotifWindowTime_Type.__name__ = "Integer32"
_CgrtMgmtNotifWindowTime_Object = MibScalar
cgrtMgmtNotifWindowTime = _CgrtMgmtNotifWindowTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 1, 17),
    _CgrtMgmtNotifWindowTime_Type()
)
cgrtMgmtNotifWindowTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgrtMgmtNotifWindowTime.setStatus("deprecated")
if mibBuilder.loadTexts:
    cgrtMgmtNotifWindowTime.setUnits("seconds")


class _CgrtMgmtNotifMaxPerWindow_Type(Integer32):
    """Custom type cgrtMgmtNotifMaxPerWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 9000),
    )


_CgrtMgmtNotifMaxPerWindow_Type.__name__ = "Integer32"
_CgrtMgmtNotifMaxPerWindow_Object = MibScalar
cgrtMgmtNotifMaxPerWindow = _CgrtMgmtNotifMaxPerWindow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 1, 18),
    _CgrtMgmtNotifMaxPerWindow_Type()
)
cgrtMgmtNotifMaxPerWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgrtMgmtNotifMaxPerWindow.setStatus("deprecated")


class _CgrtMgmtNotifEnabled_Type(TruthValue):
    """Custom type cgrtMgmtNotifEnabled based on TruthValue"""


_CgrtMgmtNotifEnabled_Object = MibScalar
cgrtMgmtNotifEnabled = _CgrtMgmtNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 1, 19),
    _CgrtMgmtNotifEnabled_Type()
)
cgrtMgmtNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgrtMgmtNotifEnabled.setStatus("deprecated")


class _CgrtRouteTableLoadNotifEnabled_Type(TruthValue):
    """Custom type cgrtRouteTableLoadNotifEnabled based on TruthValue"""


_CgrtRouteTableLoadNotifEnabled_Object = MibScalar
cgrtRouteTableLoadNotifEnabled = _CgrtRouteTableLoadNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 1, 20),
    _CgrtRouteTableLoadNotifEnabled_Type()
)
cgrtRouteTableLoadNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgrtRouteTableLoadNotifEnabled.setStatus("current")
_CgrtDynamicRoutes_Type = Gauge32
_CgrtDynamicRoutes_Object = MibScalar
cgrtDynamicRoutes = _CgrtDynamicRoutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 1, 21),
    _CgrtDynamicRoutes_Type()
)
cgrtDynamicRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgrtDynamicRoutes.setStatus("current")
_CgrtDynamicRoutesDropped_Type = Counter32
_CgrtDynamicRoutesDropped_Object = MibScalar
cgrtDynamicRoutesDropped = _CgrtDynamicRoutesDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 1, 22),
    _CgrtDynamicRoutesDropped_Type()
)
cgrtDynamicRoutesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgrtDynamicRoutesDropped.setStatus("current")


class _CgrtDestNotifWindowTimeRev1_Type(Integer32):
    """Custom type cgrtDestNotifWindowTimeRev1 based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 86400),
    )


_CgrtDestNotifWindowTimeRev1_Type.__name__ = "Integer32"
_CgrtDestNotifWindowTimeRev1_Object = MibScalar
cgrtDestNotifWindowTimeRev1 = _CgrtDestNotifWindowTimeRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 1, 23),
    _CgrtDestNotifWindowTimeRev1_Type()
)
cgrtDestNotifWindowTimeRev1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgrtDestNotifWindowTimeRev1.setStatus("current")
if mibBuilder.loadTexts:
    cgrtDestNotifWindowTimeRev1.setUnits("seconds")


class _CgrtDestNotifMaxPerWindowRev1_Type(Integer32):
    """Custom type cgrtDestNotifMaxPerWindowRev1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 9000),
    )


_CgrtDestNotifMaxPerWindowRev1_Type.__name__ = "Integer32"
_CgrtDestNotifMaxPerWindowRev1_Object = MibScalar
cgrtDestNotifMaxPerWindowRev1 = _CgrtDestNotifMaxPerWindowRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 1, 24),
    _CgrtDestNotifMaxPerWindowRev1_Type()
)
cgrtDestNotifMaxPerWindowRev1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgrtDestNotifMaxPerWindowRev1.setStatus("current")


class _CgrtDestNotifEnabledRev1_Type(TruthValue):
    """Custom type cgrtDestNotifEnabledRev1 based on TruthValue"""


_CgrtDestNotifEnabledRev1_Object = MibScalar
cgrtDestNotifEnabledRev1 = _CgrtDestNotifEnabledRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 1, 25),
    _CgrtDestNotifEnabledRev1_Type()
)
cgrtDestNotifEnabledRev1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgrtDestNotifEnabledRev1.setStatus("current")


class _CgrtMgmtNotifWindowTimeRev1_Type(Integer32):
    """Custom type cgrtMgmtNotifWindowTimeRev1 based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 86400),
    )


_CgrtMgmtNotifWindowTimeRev1_Type.__name__ = "Integer32"
_CgrtMgmtNotifWindowTimeRev1_Object = MibScalar
cgrtMgmtNotifWindowTimeRev1 = _CgrtMgmtNotifWindowTimeRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 1, 26),
    _CgrtMgmtNotifWindowTimeRev1_Type()
)
cgrtMgmtNotifWindowTimeRev1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgrtMgmtNotifWindowTimeRev1.setStatus("current")
if mibBuilder.loadTexts:
    cgrtMgmtNotifWindowTimeRev1.setUnits("seconds")


class _CgrtMgmtNotifMaxPerWindowRev1_Type(Integer32):
    """Custom type cgrtMgmtNotifMaxPerWindowRev1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 9000),
    )


_CgrtMgmtNotifMaxPerWindowRev1_Type.__name__ = "Integer32"
_CgrtMgmtNotifMaxPerWindowRev1_Object = MibScalar
cgrtMgmtNotifMaxPerWindowRev1 = _CgrtMgmtNotifMaxPerWindowRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 1, 27),
    _CgrtMgmtNotifMaxPerWindowRev1_Type()
)
cgrtMgmtNotifMaxPerWindowRev1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgrtMgmtNotifMaxPerWindowRev1.setStatus("current")


class _CgrtMgmtNotifEnabledRev1_Type(TruthValue):
    """Custom type cgrtMgmtNotifEnabledRev1 based on TruthValue"""


_CgrtMgmtNotifEnabledRev1_Object = MibScalar
cgrtMgmtNotifEnabledRev1 = _CgrtMgmtNotifEnabledRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 1, 28),
    _CgrtMgmtNotifEnabledRev1_Type()
)
cgrtMgmtNotifEnabledRev1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgrtMgmtNotifEnabledRev1.setStatus("current")


class _CgrtOrigTableEnabled_Type(TruthValue):
    """Custom type cgrtOrigTableEnabled based on TruthValue"""


_CgrtOrigTableEnabled_Object = MibScalar
cgrtOrigTableEnabled = _CgrtOrigTableEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 1, 29),
    _CgrtOrigTableEnabled_Type()
)
cgrtOrigTableEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgrtOrigTableEnabled.setStatus("current")


class _CgrtPCStatsInterval_Type(Unsigned32):
    """Custom type cgrtPCStatsInterval based on Unsigned32"""
    defaultValue = 900

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(900, 3600),
    )


_CgrtPCStatsInterval_Type.__name__ = "Unsigned32"
_CgrtPCStatsInterval_Object = MibScalar
cgrtPCStatsInterval = _CgrtPCStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 1, 30),
    _CgrtPCStatsInterval_Type()
)
cgrtPCStatsInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgrtPCStatsInterval.setStatus("current")
if mibBuilder.loadTexts:
    cgrtPCStatsInterval.setUnits("seconds")


class _CgrtNoRouteMSUsNotifEnabled_Type(TruthValue):
    """Custom type cgrtNoRouteMSUsNotifEnabled based on TruthValue"""


_CgrtNoRouteMSUsNotifEnabled_Object = MibScalar
cgrtNoRouteMSUsNotifEnabled = _CgrtNoRouteMSUsNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 1, 31),
    _CgrtNoRouteMSUsNotifEnabled_Type()
)
cgrtNoRouteMSUsNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgrtNoRouteMSUsNotifEnabled.setStatus("current")


class _CgrtNoRouteMSUsNotifWindowTime_Type(Integer32):
    """Custom type cgrtNoRouteMSUsNotifWindowTime based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_CgrtNoRouteMSUsNotifWindowTime_Type.__name__ = "Integer32"
_CgrtNoRouteMSUsNotifWindowTime_Object = MibScalar
cgrtNoRouteMSUsNotifWindowTime = _CgrtNoRouteMSUsNotifWindowTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 1, 32),
    _CgrtNoRouteMSUsNotifWindowTime_Type()
)
cgrtNoRouteMSUsNotifWindowTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgrtNoRouteMSUsNotifWindowTime.setStatus("current")
if mibBuilder.loadTexts:
    cgrtNoRouteMSUsNotifWindowTime.setUnits("seconds")
_CgrtObjects_ObjectIdentity = ObjectIdentity
cgrtObjects = _CgrtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2)
)
_CgrtInstTable_Object = MibTable
cgrtInstTable = _CgrtInstTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cgrtInstTable.setStatus("current")
_CgrtInstEntry_Object = MibTableRow
cgrtInstEntry = _CgrtInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 1, 1)
)
cgrtInstEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
)
if mibBuilder.loadTexts:
    cgrtInstEntry.setStatus("current")
_CgrtInstLastChanged_Type = TimeStamp
_CgrtInstLastChanged_Object = MibTableColumn
cgrtInstLastChanged = _CgrtInstLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 1, 1, 1),
    _CgrtInstLastChanged_Type()
)
cgrtInstLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgrtInstLastChanged.setStatus("current")
_CgrtInstLastLoadTime_Type = TimeStamp
_CgrtInstLastLoadTime_Object = MibTableColumn
cgrtInstLastLoadTime = _CgrtInstLastLoadTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 1, 1, 2),
    _CgrtInstLastLoadTime_Type()
)
cgrtInstLastLoadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgrtInstLastLoadTime.setStatus("current")
_CgrtInstLoadStatus_Type = CItpTcTableLoadStatus
_CgrtInstLoadStatus_Object = MibTableColumn
cgrtInstLoadStatus = _CgrtInstLoadStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 1, 1, 3),
    _CgrtInstLoadStatus_Type()
)
cgrtInstLoadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgrtInstLoadStatus.setStatus("current")
_CgrtInstTableName_Type = CItpTcRouteTableName
_CgrtInstTableName_Object = MibTableColumn
cgrtInstTableName = _CgrtInstTableName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 1, 1, 4),
    _CgrtInstTableName_Type()
)
cgrtInstTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgrtInstTableName.setStatus("current")
_CgrtInstLastURL_Type = CItpTcURL
_CgrtInstLastURL_Object = MibTableColumn
cgrtInstLastURL = _CgrtInstLastURL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 1, 1, 5),
    _CgrtInstLastURL_Type()
)
cgrtInstLastURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgrtInstLastURL.setStatus("current")
_CgrtInstNumberDestinations_Type = Gauge32
_CgrtInstNumberDestinations_Object = MibTableColumn
cgrtInstNumberDestinations = _CgrtInstNumberDestinations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 1, 1, 6),
    _CgrtInstNumberDestinations_Type()
)
cgrtInstNumberDestinations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgrtInstNumberDestinations.setStatus("current")
if mibBuilder.loadTexts:
    cgrtInstNumberDestinations.setUnits("entries")
_CgrtInstNumberRoutes_Type = Gauge32
_CgrtInstNumberRoutes_Object = MibTableColumn
cgrtInstNumberRoutes = _CgrtInstNumberRoutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 1, 1, 7),
    _CgrtInstNumberRoutes_Type()
)
cgrtInstNumberRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgrtInstNumberRoutes.setStatus("current")
if mibBuilder.loadTexts:
    cgrtInstNumberRoutes.setUnits("entries")
_CgrtInstUnknownOrigPCs_Type = Counter32
_CgrtInstUnknownOrigPCs_Object = MibTableColumn
cgrtInstUnknownOrigPCs = _CgrtInstUnknownOrigPCs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 1, 1, 8),
    _CgrtInstUnknownOrigPCs_Type()
)
cgrtInstUnknownOrigPCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgrtInstUnknownOrigPCs.setStatus("current")
if mibBuilder.loadTexts:
    cgrtInstUnknownOrigPCs.setUnits("MSUs")
_CgrtInstNoRouteDrops_Type = Counter32
_CgrtInstNoRouteDrops_Object = MibTableColumn
cgrtInstNoRouteDrops = _CgrtInstNoRouteDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 1, 1, 9),
    _CgrtInstNoRouteDrops_Type()
)
cgrtInstNoRouteDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgrtInstNoRouteDrops.setStatus("current")
if mibBuilder.loadTexts:
    cgrtInstNoRouteDrops.setUnits("MSUs")
_CgrtDestTable_Object = MibTable
cgrtDestTable = _CgrtDestTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cgrtDestTable.setStatus("current")
_CgrtDestEntry_Object = MibTableRow
cgrtDestEntry = _CgrtDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 2, 1)
)
cgrtDestEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-GRT-MIB", "cgrtRouteDpc"),
    (0, "CISCO-ITP-GRT-MIB", "cgrtRouteMask"),
)
if mibBuilder.loadTexts:
    cgrtDestEntry.setStatus("current")


class _CgrtDestStatus_Type(Integer32):
    """Custom type cgrtDestStatus based on Integer32"""
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
        *(("accessible", 2),
          ("inaccessible", 3),
          ("restricted", 4),
          ("unknown", 1))
    )


_CgrtDestStatus_Type.__name__ = "Integer32"
_CgrtDestStatus_Object = MibTableColumn
cgrtDestStatus = _CgrtDestStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 2, 1, 1),
    _CgrtDestStatus_Type()
)
cgrtDestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgrtDestStatus.setStatus("current")


class _CgrtDestCongestion_Type(Unsigned32):
    """Custom type cgrtDestCongestion based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_CgrtDestCongestion_Type.__name__ = "Unsigned32"
_CgrtDestCongestion_Object = MibTableColumn
cgrtDestCongestion = _CgrtDestCongestion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 2, 1, 2),
    _CgrtDestCongestion_Type()
)
cgrtDestCongestion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgrtDestCongestion.setStatus("current")
_CgrtDestAccessibleSeconds_Type = Counter32
_CgrtDestAccessibleSeconds_Object = MibTableColumn
cgrtDestAccessibleSeconds = _CgrtDestAccessibleSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 2, 1, 3),
    _CgrtDestAccessibleSeconds_Type()
)
cgrtDestAccessibleSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgrtDestAccessibleSeconds.setStatus("current")
if mibBuilder.loadTexts:
    cgrtDestAccessibleSeconds.setUnits("seconds")
_CgrtDestInaccessibleSeconds_Type = Counter32
_CgrtDestInaccessibleSeconds_Object = MibTableColumn
cgrtDestInaccessibleSeconds = _CgrtDestInaccessibleSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 2, 1, 4),
    _CgrtDestInaccessibleSeconds_Type()
)
cgrtDestInaccessibleSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgrtDestInaccessibleSeconds.setStatus("current")
if mibBuilder.loadTexts:
    cgrtDestInaccessibleSeconds.setUnits("seconds")
_CgrtDestRestrictedSeconds_Type = Counter32
_CgrtDestRestrictedSeconds_Object = MibTableColumn
cgrtDestRestrictedSeconds = _CgrtDestRestrictedSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 2, 1, 5),
    _CgrtDestRestrictedSeconds_Type()
)
cgrtDestRestrictedSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgrtDestRestrictedSeconds.setStatus("current")
if mibBuilder.loadTexts:
    cgrtDestRestrictedSeconds.setUnits("seconds")
_CgrtDestMSUsOut_Type = Counter32
_CgrtDestMSUsOut_Object = MibTableColumn
cgrtDestMSUsOut = _CgrtDestMSUsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 2, 1, 6),
    _CgrtDestMSUsOut_Type()
)
cgrtDestMSUsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgrtDestMSUsOut.setStatus("current")
if mibBuilder.loadTexts:
    cgrtDestMSUsOut.setUnits("MSUs")
_CgrtDestOctetsOut_Type = Counter64
_CgrtDestOctetsOut_Object = MibTableColumn
cgrtDestOctetsOut = _CgrtDestOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 2, 1, 7),
    _CgrtDestOctetsOut_Type()
)
cgrtDestOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgrtDestOctetsOut.setStatus("current")
if mibBuilder.loadTexts:
    cgrtDestOctetsOut.setUnits("octets")
_CgrtDestMSUsIn_Type = Counter32
_CgrtDestMSUsIn_Object = MibTableColumn
cgrtDestMSUsIn = _CgrtDestMSUsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 2, 1, 8),
    _CgrtDestMSUsIn_Type()
)
cgrtDestMSUsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgrtDestMSUsIn.setStatus("current")
if mibBuilder.loadTexts:
    cgrtDestMSUsIn.setUnits("MSUs")
_CgrtDestOctetsIn_Type = Counter64
_CgrtDestOctetsIn_Object = MibTableColumn
cgrtDestOctetsIn = _CgrtDestOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 2, 1, 9),
    _CgrtDestOctetsIn_Type()
)
cgrtDestOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgrtDestOctetsIn.setStatus("current")
if mibBuilder.loadTexts:
    cgrtDestOctetsIn.setUnits("octets")
_CgrtDestInaccessibleDrops_Type = Counter32
_CgrtDestInaccessibleDrops_Object = MibTableColumn
cgrtDestInaccessibleDrops = _CgrtDestInaccessibleDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 2, 1, 10),
    _CgrtDestInaccessibleDrops_Type()
)
cgrtDestInaccessibleDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgrtDestInaccessibleDrops.setStatus("current")
if mibBuilder.loadTexts:
    cgrtDestInaccessibleDrops.setUnits("MSUs")
_CgrtDestRestrictedMSUs_Type = Counter32
_CgrtDestRestrictedMSUs_Object = MibTableColumn
cgrtDestRestrictedMSUs = _CgrtDestRestrictedMSUs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 2, 1, 11),
    _CgrtDestRestrictedMSUs_Type()
)
cgrtDestRestrictedMSUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgrtDestRestrictedMSUs.setStatus("current")
if mibBuilder.loadTexts:
    cgrtDestRestrictedMSUs.setUnits("MSUs")
_CgrtDestCongestionDrops_Type = Counter32
_CgrtDestCongestionDrops_Object = MibTableColumn
cgrtDestCongestionDrops = _CgrtDestCongestionDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 2, 1, 12),
    _CgrtDestCongestionDrops_Type()
)
cgrtDestCongestionDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgrtDestCongestionDrops.setStatus("current")
if mibBuilder.loadTexts:
    cgrtDestCongestionDrops.setUnits("MSUs")
_CgrtDestDisplay_Type = CItpTcDisplayPC
_CgrtDestDisplay_Object = MibTableColumn
cgrtDestDisplay = _CgrtDestDisplay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 2, 1, 13),
    _CgrtDestDisplay_Type()
)
cgrtDestDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgrtDestDisplay.setStatus("current")
_CgrtRouteTable_Object = MibTable
cgrtRouteTable = _CgrtRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cgrtRouteTable.setStatus("current")
_CgrtRouteEntry_Object = MibTableRow
cgrtRouteEntry = _CgrtRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 3, 1)
)
cgrtRouteEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-GRT-MIB", "cgrtRouteDpc"),
    (0, "CISCO-ITP-GRT-MIB", "cgrtRouteMask"),
    (0, "CISCO-ITP-GRT-MIB", "cgrtRouteDestLsCost"),
    (0, "CISCO-ITP-GRT-MIB", "cgrtRouteDestLinkset"),
)
if mibBuilder.loadTexts:
    cgrtRouteEntry.setStatus("current")
_CgrtRouteDpc_Type = CItpTcPointCode
_CgrtRouteDpc_Object = MibTableColumn
cgrtRouteDpc = _CgrtRouteDpc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 3, 1, 1),
    _CgrtRouteDpc_Type()
)
cgrtRouteDpc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgrtRouteDpc.setStatus("current")


class _CgrtRouteMask_Type(Unsigned32):
    """Custom type cgrtRouteMask based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_CgrtRouteMask_Type.__name__ = "Unsigned32"
_CgrtRouteMask_Object = MibTableColumn
cgrtRouteMask = _CgrtRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 3, 1, 2),
    _CgrtRouteMask_Type()
)
cgrtRouteMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgrtRouteMask.setStatus("current")


class _CgrtRouteDestLsCost_Type(Unsigned32):
    """Custom type cgrtRouteDestLsCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_CgrtRouteDestLsCost_Type.__name__ = "Unsigned32"
_CgrtRouteDestLsCost_Object = MibTableColumn
cgrtRouteDestLsCost = _CgrtRouteDestLsCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 3, 1, 3),
    _CgrtRouteDestLsCost_Type()
)
cgrtRouteDestLsCost.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgrtRouteDestLsCost.setStatus("current")
_CgrtRouteDestLinkset_Type = CItpTcLinksetId
_CgrtRouteDestLinkset_Object = MibTableColumn
cgrtRouteDestLinkset = _CgrtRouteDestLinkset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 3, 1, 4),
    _CgrtRouteDestLinkset_Type()
)
cgrtRouteDestLinkset.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgrtRouteDestLinkset.setStatus("current")
_CgrtRouteQos_Type = CItpTcQos
_CgrtRouteQos_Object = MibTableColumn
cgrtRouteQos = _CgrtRouteQos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 3, 1, 5),
    _CgrtRouteQos_Type()
)
cgrtRouteQos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgrtRouteQos.setStatus("current")


class _CgrtRouteStatus_Type(Integer32):
    """Custom type cgrtRouteStatus based on Integer32"""
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
        *(("available", 2),
          ("deleted", 5),
          ("restricted", 3),
          ("unavailable", 4),
          ("unknown", 1))
    )


_CgrtRouteStatus_Type.__name__ = "Integer32"
_CgrtRouteStatus_Object = MibTableColumn
cgrtRouteStatus = _CgrtRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 3, 1, 6),
    _CgrtRouteStatus_Type()
)
cgrtRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgrtRouteStatus.setStatus("current")


class _CgrtRouteMgmtStatus_Type(Integer32):
    """Custom type cgrtRouteMgmtStatus based on Integer32"""
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
        *(("allowed", 2),
          ("deleted", 5),
          ("prohibited", 4),
          ("restricted", 3),
          ("unknown", 1))
    )


_CgrtRouteMgmtStatus_Type.__name__ = "Integer32"
_CgrtRouteMgmtStatus_Object = MibTableColumn
cgrtRouteMgmtStatus = _CgrtRouteMgmtStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 3, 1, 7),
    _CgrtRouteMgmtStatus_Type()
)
cgrtRouteMgmtStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgrtRouteMgmtStatus.setStatus("current")
_CgrtRouteDynamic_Type = TruthValue
_CgrtRouteDynamic_Object = MibTableColumn
cgrtRouteDynamic = _CgrtRouteDynamic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 3, 1, 8),
    _CgrtRouteDynamic_Type()
)
cgrtRouteDynamic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgrtRouteDynamic.setStatus("current")


class _CgrtRouteType_Type(Integer32):
    """Custom type cgrtRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("alias", 7),
          ("cluster", 2),
          ("management", 6),
          ("shadow", 5),
          ("static", 1),
          ("summary", 3),
          ("unknown", 0),
          ("xlist", 4))
    )


_CgrtRouteType_Type.__name__ = "Integer32"
_CgrtRouteType_Object = MibTableColumn
cgrtRouteType = _CgrtRouteType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 3, 1, 9),
    _CgrtRouteType_Type()
)
cgrtRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgrtRouteType.setStatus("current")


class _CgrtRouteAdminStatus_Type(Integer32):
    """Custom type cgrtRouteAdminStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("available", 2),
          ("deleted", 5),
          ("none", 0),
          ("restricted", 3),
          ("unavailable", 4),
          ("unknown", 1))
    )


_CgrtRouteAdminStatus_Type.__name__ = "Integer32"
_CgrtRouteAdminStatus_Object = MibTableColumn
cgrtRouteAdminStatus = _CgrtRouteAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 3, 1, 10),
    _CgrtRouteAdminStatus_Type()
)
cgrtRouteAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgrtRouteAdminStatus.setStatus("current")
_CgrtRouteRowStatus_Type = RowStatus
_CgrtRouteRowStatus_Object = MibTableColumn
cgrtRouteRowStatus = _CgrtRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 3, 1, 11),
    _CgrtRouteRowStatus_Type()
)
cgrtRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgrtRouteRowStatus.setStatus("current")
_CgrtRouteAllowedSeconds_Type = Counter32
_CgrtRouteAllowedSeconds_Object = MibTableColumn
cgrtRouteAllowedSeconds = _CgrtRouteAllowedSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 3, 1, 12),
    _CgrtRouteAllowedSeconds_Type()
)
cgrtRouteAllowedSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgrtRouteAllowedSeconds.setStatus("current")
if mibBuilder.loadTexts:
    cgrtRouteAllowedSeconds.setUnits("seconds")
_CgrtRouteRestrictedSeconds_Type = Counter32
_CgrtRouteRestrictedSeconds_Object = MibTableColumn
cgrtRouteRestrictedSeconds = _CgrtRouteRestrictedSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 3, 1, 13),
    _CgrtRouteRestrictedSeconds_Type()
)
cgrtRouteRestrictedSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgrtRouteRestrictedSeconds.setStatus("current")
if mibBuilder.loadTexts:
    cgrtRouteRestrictedSeconds.setUnits("seconds")
_CgrtRouteProhibitedSeconds_Type = Counter32
_CgrtRouteProhibitedSeconds_Object = MibTableColumn
cgrtRouteProhibitedSeconds = _CgrtRouteProhibitedSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 3, 1, 14),
    _CgrtRouteProhibitedSeconds_Type()
)
cgrtRouteProhibitedSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgrtRouteProhibitedSeconds.setStatus("current")
if mibBuilder.loadTexts:
    cgrtRouteProhibitedSeconds.setUnits("seconds")
_CgrtRouteDisplay_Type = CItpTcDisplayPC
_CgrtRouteDisplay_Object = MibTableColumn
cgrtRouteDisplay = _CgrtRouteDisplay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 3, 1, 15),
    _CgrtRouteDisplay_Type()
)
cgrtRouteDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgrtRouteDisplay.setStatus("current")
_CgrtNotificationsInfo_ObjectIdentity = ObjectIdentity
cgrtNotificationsInfo = _CgrtNotificationsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 4)
)
_CgrtDestNotifSupFlag_Type = TruthValue
_CgrtDestNotifSupFlag_Object = MibScalar
cgrtDestNotifSupFlag = _CgrtDestNotifSupFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 4, 1),
    _CgrtDestNotifSupFlag_Type()
)
cgrtDestNotifSupFlag.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgrtDestNotifSupFlag.setStatus("deprecated")


class _CgrtDestNotifChanges_Type(OctetString):
    """Custom type cgrtDestNotifChanges based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CgrtDestNotifChanges_Type.__name__ = "OctetString"
_CgrtDestNotifChanges_Object = MibScalar
cgrtDestNotifChanges = _CgrtDestNotifChanges_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 4, 2),
    _CgrtDestNotifChanges_Type()
)
cgrtDestNotifChanges.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgrtDestNotifChanges.setStatus("deprecated")
_CgrtMgmtNotifSupFlag_Type = TruthValue
_CgrtMgmtNotifSupFlag_Object = MibScalar
cgrtMgmtNotifSupFlag = _CgrtMgmtNotifSupFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 4, 3),
    _CgrtMgmtNotifSupFlag_Type()
)
cgrtMgmtNotifSupFlag.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgrtMgmtNotifSupFlag.setStatus("deprecated")


class _CgrtMgmtNotifChanges_Type(OctetString):
    """Custom type cgrtMgmtNotifChanges based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CgrtMgmtNotifChanges_Type.__name__ = "OctetString"
_CgrtMgmtNotifChanges_Object = MibScalar
cgrtMgmtNotifChanges = _CgrtMgmtNotifChanges_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 4, 4),
    _CgrtMgmtNotifChanges_Type()
)
cgrtMgmtNotifChanges.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgrtMgmtNotifChanges.setStatus("deprecated")
_CgrtDestNotifSuppressed_Type = Counter32
_CgrtDestNotifSuppressed_Object = MibScalar
cgrtDestNotifSuppressed = _CgrtDestNotifSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 4, 5),
    _CgrtDestNotifSuppressed_Type()
)
cgrtDestNotifSuppressed.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgrtDestNotifSuppressed.setStatus("current")
if mibBuilder.loadTexts:
    cgrtDestNotifSuppressed.setUnits("occurrences")
_CgrtRouteNotifSuppressed_Type = Counter32
_CgrtRouteNotifSuppressed_Object = MibScalar
cgrtRouteNotifSuppressed = _CgrtRouteNotifSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 4, 6),
    _CgrtRouteNotifSuppressed_Type()
)
cgrtRouteNotifSuppressed.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgrtRouteNotifSuppressed.setStatus("current")
if mibBuilder.loadTexts:
    cgrtRouteNotifSuppressed.setUnits("occurrences")
_CgrtNoRouteMSUsInterval_Type = Unsigned32
_CgrtNoRouteMSUsInterval_Object = MibScalar
cgrtNoRouteMSUsInterval = _CgrtNoRouteMSUsInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 4, 7),
    _CgrtNoRouteMSUsInterval_Type()
)
cgrtNoRouteMSUsInterval.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgrtNoRouteMSUsInterval.setStatus("current")
if mibBuilder.loadTexts:
    cgrtNoRouteMSUsInterval.setUnits("seconds")
_CgrtIntervalNoRouteMSUs_Type = Unsigned32
_CgrtIntervalNoRouteMSUs_Object = MibScalar
cgrtIntervalNoRouteMSUs = _CgrtIntervalNoRouteMSUs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 4, 8),
    _CgrtIntervalNoRouteMSUs_Type()
)
cgrtIntervalNoRouteMSUs.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgrtIntervalNoRouteMSUs.setStatus("current")
if mibBuilder.loadTexts:
    cgrtIntervalNoRouteMSUs.setUnits("MSUs")
_CgrtOrigTable_Object = MibTable
cgrtOrigTable = _CgrtOrigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 5)
)
if mibBuilder.loadTexts:
    cgrtOrigTable.setStatus("current")
_CgrtOrigEntry_Object = MibTableRow
cgrtOrigEntry = _CgrtOrigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 5, 1)
)
cgrtOrigEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-GRT-MIB", "cgrtOrigPC"),
    (0, "CISCO-ITP-GRT-MIB", "cgrtRouteMask"),
)
if mibBuilder.loadTexts:
    cgrtOrigEntry.setStatus("current")
_CgrtOrigPC_Type = CItpTcPointCode
_CgrtOrigPC_Object = MibTableColumn
cgrtOrigPC = _CgrtOrigPC_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 5, 1, 1),
    _CgrtOrigPC_Type()
)
cgrtOrigPC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgrtOrigPC.setStatus("current")
_CgrtOrigMSUs_Type = Counter32
_CgrtOrigMSUs_Object = MibTableColumn
cgrtOrigMSUs = _CgrtOrigMSUs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 5, 1, 2),
    _CgrtOrigMSUs_Type()
)
cgrtOrigMSUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgrtOrigMSUs.setStatus("current")
if mibBuilder.loadTexts:
    cgrtOrigMSUs.setUnits("MSUs")
_CgrtOrigOctets_Type = Counter64
_CgrtOrigOctets_Object = MibTableColumn
cgrtOrigOctets = _CgrtOrigOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 5, 1, 3),
    _CgrtOrigOctets_Type()
)
cgrtOrigOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgrtOrigOctets.setStatus("current")
if mibBuilder.loadTexts:
    cgrtOrigOctets.setUnits("octets")
_CgrtOrigDisplay_Type = CItpTcDisplayPC
_CgrtOrigDisplay_Object = MibTableColumn
cgrtOrigDisplay = _CgrtOrigDisplay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 5, 1, 4),
    _CgrtOrigDisplay_Type()
)
cgrtOrigDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgrtOrigDisplay.setStatus("current")
_CgrtDestSITable_Object = MibTable
cgrtDestSITable = _CgrtDestSITable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 6)
)
if mibBuilder.loadTexts:
    cgrtDestSITable.setStatus("current")
_CgrtDestSIEntry_Object = MibTableRow
cgrtDestSIEntry = _CgrtDestSIEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 6, 1)
)
cgrtDestSIEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-GRT-MIB", "cgrtRouteDpc"),
    (0, "CISCO-ITP-GRT-MIB", "cgrtRouteMask"),
    (0, "CISCO-ITP-GRT-MIB", "cgrtMtp3SI"),
)
if mibBuilder.loadTexts:
    cgrtDestSIEntry.setStatus("current")
_CgrtMtp3SI_Type = CItpTcServiceIndicator
_CgrtMtp3SI_Object = MibTableColumn
cgrtMtp3SI = _CgrtMtp3SI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 6, 1, 1),
    _CgrtMtp3SI_Type()
)
cgrtMtp3SI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgrtMtp3SI.setStatus("current")
_CgrtDestSIMSUsOut_Type = Counter32
_CgrtDestSIMSUsOut_Object = MibTableColumn
cgrtDestSIMSUsOut = _CgrtDestSIMSUsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 6, 1, 2),
    _CgrtDestSIMSUsOut_Type()
)
cgrtDestSIMSUsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgrtDestSIMSUsOut.setStatus("current")
if mibBuilder.loadTexts:
    cgrtDestSIMSUsOut.setUnits("MSUs")
_CgrtDestSIOctetsOut_Type = Counter64
_CgrtDestSIOctetsOut_Object = MibTableColumn
cgrtDestSIOctetsOut = _CgrtDestSIOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 6, 1, 3),
    _CgrtDestSIOctetsOut_Type()
)
cgrtDestSIOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgrtDestSIOctetsOut.setStatus("current")
if mibBuilder.loadTexts:
    cgrtDestSIOctetsOut.setUnits("octets")
_CgrtDestSIMSUsIn_Type = Counter32
_CgrtDestSIMSUsIn_Object = MibTableColumn
cgrtDestSIMSUsIn = _CgrtDestSIMSUsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 6, 1, 4),
    _CgrtDestSIMSUsIn_Type()
)
cgrtDestSIMSUsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgrtDestSIMSUsIn.setStatus("current")
if mibBuilder.loadTexts:
    cgrtDestSIMSUsIn.setUnits("MSUs")
_CgrtDestSIOctetsIn_Type = Counter64
_CgrtDestSIOctetsIn_Object = MibTableColumn
cgrtDestSIOctetsIn = _CgrtDestSIOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 6, 1, 5),
    _CgrtDestSIOctetsIn_Type()
)
cgrtDestSIOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgrtDestSIOctetsIn.setStatus("current")
if mibBuilder.loadTexts:
    cgrtDestSIOctetsIn.setUnits("octets")
_CgrtDestSIDisplay_Type = CgrtDisplayPCSI
_CgrtDestSIDisplay_Object = MibTableColumn
cgrtDestSIDisplay = _CgrtDestSIDisplay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 6, 1, 6),
    _CgrtDestSIDisplay_Type()
)
cgrtDestSIDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgrtDestSIDisplay.setStatus("current")
_CgrtOrigSITable_Object = MibTable
cgrtOrigSITable = _CgrtOrigSITable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 7)
)
if mibBuilder.loadTexts:
    cgrtOrigSITable.setStatus("current")
_CgrtOrigSIEntry_Object = MibTableRow
cgrtOrigSIEntry = _CgrtOrigSIEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 7, 1)
)
cgrtOrigSIEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-GRT-MIB", "cgrtOrigPC"),
    (0, "CISCO-ITP-GRT-MIB", "cgrtRouteMask"),
    (0, "CISCO-ITP-GRT-MIB", "cgrtMtp3SI"),
)
if mibBuilder.loadTexts:
    cgrtOrigSIEntry.setStatus("current")
_CgrtOrigSIMSUs_Type = Counter32
_CgrtOrigSIMSUs_Object = MibTableColumn
cgrtOrigSIMSUs = _CgrtOrigSIMSUs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 7, 1, 1),
    _CgrtOrigSIMSUs_Type()
)
cgrtOrigSIMSUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgrtOrigSIMSUs.setStatus("current")
if mibBuilder.loadTexts:
    cgrtOrigSIMSUs.setUnits("MSUs")
_CgrtOrigSIOctets_Type = Counter64
_CgrtOrigSIOctets_Object = MibTableColumn
cgrtOrigSIOctets = _CgrtOrigSIOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 7, 1, 2),
    _CgrtOrigSIOctets_Type()
)
cgrtOrigSIOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgrtOrigSIOctets.setStatus("current")
if mibBuilder.loadTexts:
    cgrtOrigSIOctets.setUnits("octets")
_CgrtOrigSIDisplay_Type = CgrtDisplayPCSI
_CgrtOrigSIDisplay_Object = MibTableColumn
cgrtOrigSIDisplay = _CgrtOrigSIDisplay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 1, 2, 7, 1, 3),
    _CgrtOrigSIDisplay_Type()
)
cgrtOrigSIDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgrtOrigSIDisplay.setStatus("current")
_CiscoGrtMIBConform_ObjectIdentity = ObjectIdentity
ciscoGrtMIBConform = _CiscoGrtMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 2)
)
_CiscoGrtMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoGrtMIBCompliances = _CiscoGrtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 2, 1)
)
_CiscoGrtMIBGroups_ObjectIdentity = ObjectIdentity
ciscoGrtMIBGroups = _CiscoGrtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 2, 2)
)

# Managed Objects groups

ciscoGrtInstGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 2, 2, 1)
)
ciscoGrtInstGroup.setObjects(
      *(("CISCO-ITP-GRT-MIB", "cgrtInstLastChanged"),
        ("CISCO-ITP-GRT-MIB", "cgrtInstLastLoadTime"),
        ("CISCO-ITP-GRT-MIB", "cgrtInstLoadStatus"),
        ("CISCO-ITP-GRT-MIB", "cgrtInstTableName"),
        ("CISCO-ITP-GRT-MIB", "cgrtInstLastURL"),
        ("CISCO-ITP-GRT-MIB", "cgrtInstNumberDestinations"),
        ("CISCO-ITP-GRT-MIB", "cgrtInstNumberRoutes"),
        ("CISCO-ITP-GRT-MIB", "cgrtRouteTableLoadNotifEnabled"))
)
if mibBuilder.loadTexts:
    ciscoGrtInstGroup.setStatus("current")

ciscoGrtDestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 2, 2, 2)
)
ciscoGrtDestGroup.setObjects(
      *(("CISCO-ITP-GRT-MIB", "cgrtDestNotifDelayTime"),
        ("CISCO-ITP-GRT-MIB", "cgrtDestNotifWindowTime"),
        ("CISCO-ITP-GRT-MIB", "cgrtDestNotifMaxPerWindow"),
        ("CISCO-ITP-GRT-MIB", "cgrtDestNotifEnabled"),
        ("CISCO-ITP-GRT-MIB", "cgrtDestNotifSupFlag"),
        ("CISCO-ITP-GRT-MIB", "cgrtDestNotifChanges"),
        ("CISCO-ITP-GRT-MIB", "cgrtDestStatus"),
        ("CISCO-ITP-GRT-MIB", "cgrtDestCongestion"))
)
if mibBuilder.loadTexts:
    ciscoGrtDestGroup.setStatus("deprecated")

ciscoGrtRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 2, 2, 3)
)
ciscoGrtRouteGroup.setObjects(
      *(("CISCO-ITP-GRT-MIB", "cgrtRouteMaxDynamic"),
        ("CISCO-ITP-GRT-MIB", "cgrtMgmtNotifDelayTime"),
        ("CISCO-ITP-GRT-MIB", "cgrtMgmtNotifWindowTime"),
        ("CISCO-ITP-GRT-MIB", "cgrtMgmtNotifMaxPerWindow"),
        ("CISCO-ITP-GRT-MIB", "cgrtMgmtNotifEnabled"),
        ("CISCO-ITP-GRT-MIB", "cgrtMgmtNotifSupFlag"),
        ("CISCO-ITP-GRT-MIB", "cgrtMgmtNotifChanges"),
        ("CISCO-ITP-GRT-MIB", "cgrtDynamicRoutes"),
        ("CISCO-ITP-GRT-MIB", "cgrtDynamicRoutesDropped"),
        ("CISCO-ITP-GRT-MIB", "cgrtRouteQos"),
        ("CISCO-ITP-GRT-MIB", "cgrtRouteStatus"),
        ("CISCO-ITP-GRT-MIB", "cgrtRouteMgmtStatus"),
        ("CISCO-ITP-GRT-MIB", "cgrtRouteDynamic"),
        ("CISCO-ITP-GRT-MIB", "cgrtRouteType"),
        ("CISCO-ITP-GRT-MIB", "cgrtRouteAdminStatus"),
        ("CISCO-ITP-GRT-MIB", "cgrtRouteRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoGrtRouteGroup.setStatus("deprecated")

ciscoGrtScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 2, 2, 5)
)
ciscoGrtScalarsGroup.setObjects(
    ("CISCO-ITP-GRT-MIB", "cgrtPCStatsInterval")
)
if mibBuilder.loadTexts:
    ciscoGrtScalarsGroup.setStatus("current")

ciscoGrtDestGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 2, 2, 6)
)
ciscoGrtDestGroupRev1.setObjects(
      *(("CISCO-ITP-GRT-MIB", "cgrtDestNotifWindowTimeRev1"),
        ("CISCO-ITP-GRT-MIB", "cgrtDestNotifMaxPerWindowRev1"),
        ("CISCO-ITP-GRT-MIB", "cgrtDestNotifEnabledRev1"),
        ("CISCO-ITP-GRT-MIB", "cgrtDestNotifSuppressed"),
        ("CISCO-ITP-GRT-MIB", "cgrtDestStatus"),
        ("CISCO-ITP-GRT-MIB", "cgrtDestCongestion"),
        ("CISCO-ITP-GRT-MIB", "cgrtDestAccessibleSeconds"),
        ("CISCO-ITP-GRT-MIB", "cgrtDestInaccessibleSeconds"),
        ("CISCO-ITP-GRT-MIB", "cgrtDestRestrictedSeconds"),
        ("CISCO-ITP-GRT-MIB", "cgrtDestMSUsOut"),
        ("CISCO-ITP-GRT-MIB", "cgrtDestOctetsOut"),
        ("CISCO-ITP-GRT-MIB", "cgrtDestMSUsIn"),
        ("CISCO-ITP-GRT-MIB", "cgrtDestOctetsIn"),
        ("CISCO-ITP-GRT-MIB", "cgrtDestRestrictedMSUs"),
        ("CISCO-ITP-GRT-MIB", "cgrtDestInaccessibleDrops"),
        ("CISCO-ITP-GRT-MIB", "cgrtDestCongestionDrops"),
        ("CISCO-ITP-GRT-MIB", "cgrtDestDisplay"))
)
if mibBuilder.loadTexts:
    ciscoGrtDestGroupRev1.setStatus("current")

ciscoGrtRouteGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 2, 2, 7)
)
ciscoGrtRouteGroupRev1.setObjects(
      *(("CISCO-ITP-GRT-MIB", "cgrtRouteMaxDynamic"),
        ("CISCO-ITP-GRT-MIB", "cgrtMgmtNotifWindowTimeRev1"),
        ("CISCO-ITP-GRT-MIB", "cgrtMgmtNotifMaxPerWindowRev1"),
        ("CISCO-ITP-GRT-MIB", "cgrtMgmtNotifEnabledRev1"),
        ("CISCO-ITP-GRT-MIB", "cgrtRouteNotifSuppressed"),
        ("CISCO-ITP-GRT-MIB", "cgrtDynamicRoutes"),
        ("CISCO-ITP-GRT-MIB", "cgrtDynamicRoutesDropped"),
        ("CISCO-ITP-GRT-MIB", "cgrtRouteQos"),
        ("CISCO-ITP-GRT-MIB", "cgrtRouteStatus"),
        ("CISCO-ITP-GRT-MIB", "cgrtRouteMgmtStatus"),
        ("CISCO-ITP-GRT-MIB", "cgrtRouteDynamic"),
        ("CISCO-ITP-GRT-MIB", "cgrtRouteType"),
        ("CISCO-ITP-GRT-MIB", "cgrtRouteAdminStatus"),
        ("CISCO-ITP-GRT-MIB", "cgrtRouteRowStatus"),
        ("CISCO-ITP-GRT-MIB", "cgrtRouteAllowedSeconds"),
        ("CISCO-ITP-GRT-MIB", "cgrtRouteRestrictedSeconds"),
        ("CISCO-ITP-GRT-MIB", "cgrtRouteProhibitedSeconds"),
        ("CISCO-ITP-GRT-MIB", "cgrtRouteDisplay"))
)
if mibBuilder.loadTexts:
    ciscoGrtRouteGroupRev1.setStatus("current")

ciscoGrtOrigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 2, 2, 8)
)
ciscoGrtOrigGroup.setObjects(
      *(("CISCO-ITP-GRT-MIB", "cgrtOrigTableEnabled"),
        ("CISCO-ITP-GRT-MIB", "cgrtOrigMSUs"),
        ("CISCO-ITP-GRT-MIB", "cgrtOrigOctets"),
        ("CISCO-ITP-GRT-MIB", "cgrtOrigDisplay"))
)
if mibBuilder.loadTexts:
    ciscoGrtOrigGroup.setStatus("current")

ciscoGrtDestSIGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 2, 2, 9)
)
ciscoGrtDestSIGroup.setObjects(
      *(("CISCO-ITP-GRT-MIB", "cgrtDestSIMSUsOut"),
        ("CISCO-ITP-GRT-MIB", "cgrtDestSIOctetsOut"),
        ("CISCO-ITP-GRT-MIB", "cgrtDestSIMSUsIn"),
        ("CISCO-ITP-GRT-MIB", "cgrtDestSIOctetsIn"),
        ("CISCO-ITP-GRT-MIB", "cgrtDestSIDisplay"))
)
if mibBuilder.loadTexts:
    ciscoGrtDestSIGroup.setStatus("current")

ciscoGrtOrigSIGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 2, 2, 10)
)
ciscoGrtOrigSIGroup.setObjects(
      *(("CISCO-ITP-GRT-MIB", "cgrtOrigSIMSUs"),
        ("CISCO-ITP-GRT-MIB", "cgrtOrigSIOctets"),
        ("CISCO-ITP-GRT-MIB", "cgrtOrigSIDisplay"))
)
if mibBuilder.loadTexts:
    ciscoGrtOrigSIGroup.setStatus("current")

ciscoGrtInstGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 2, 2, 12)
)
ciscoGrtInstGroupSup1.setObjects(
      *(("CISCO-ITP-GRT-MIB", "cgrtNoRouteMSUsNotifEnabled"),
        ("CISCO-ITP-GRT-MIB", "cgrtNoRouteMSUsNotifWindowTime"),
        ("CISCO-ITP-GRT-MIB", "cgrtInstUnknownOrigPCs"),
        ("CISCO-ITP-GRT-MIB", "cgrtInstNoRouteDrops"),
        ("CISCO-ITP-GRT-MIB", "cgrtNoRouteMSUsInterval"),
        ("CISCO-ITP-GRT-MIB", "cgrtIntervalNoRouteMSUs"))
)
if mibBuilder.loadTexts:
    ciscoGrtInstGroupSup1.setStatus("current")


# Notification objects

ciscoGrtDestStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 0, 1)
)
ciscoGrtDestStateChange.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspEventSequenceNumber"),
        ("CISCO-ITP-GSP-MIB", "cgspCLLICode"),
        ("CISCO-ITP-GRT-MIB", "cgrtDestNotifSupFlag"),
        ("CISCO-ITP-GRT-MIB", "cgrtDestNotifChanges"))
)
if mibBuilder.loadTexts:
    ciscoGrtDestStateChange.setStatus(
        "deprecated"
    )

ciscoGrtMgmtStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 0, 2)
)
ciscoGrtMgmtStateChange.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspEventSequenceNumber"),
        ("CISCO-ITP-GSP-MIB", "cgspCLLICode"),
        ("CISCO-ITP-GRT-MIB", "cgrtMgmtNotifSupFlag"),
        ("CISCO-ITP-GRT-MIB", "cgrtMgmtNotifChanges"))
)
if mibBuilder.loadTexts:
    ciscoGrtMgmtStateChange.setStatus(
        "deprecated"
    )

ciscoGrtRouteTableLoad = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 0, 3)
)
ciscoGrtRouteTableLoad.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspEventSequenceNumber"),
        ("CISCO-ITP-GSP-MIB", "cgspCLLICode"),
        ("CISCO-ITP-GRT-MIB", "cgrtInstLoadStatus"),
        ("CISCO-ITP-GRT-MIB", "cgrtInstTableName"),
        ("CISCO-ITP-GRT-MIB", "cgrtInstLastURL"))
)
if mibBuilder.loadTexts:
    ciscoGrtRouteTableLoad.setStatus(
        "current"
    )

ciscoGrtDestStateChangeRev1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 0, 4)
)
ciscoGrtDestStateChangeRev1.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspEventSequenceNumber"),
        ("CISCO-ITP-GSP-MIB", "cgspCLLICode"),
        ("CISCO-ITP-GRT-MIB", "cgrtDestNotifSuppressed"),
        ("CISCO-ITP-GRT-MIB", "cgrtDestDisplay"),
        ("CISCO-ITP-GRT-MIB", "cgrtDestStatus"),
        ("CISCO-ITP-GRT-MIB", "cgrtDestCongestion"))
)
if mibBuilder.loadTexts:
    ciscoGrtDestStateChangeRev1.setStatus(
        "current"
    )

ciscoGrtMgmtStateChangeRev1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 0, 5)
)
ciscoGrtMgmtStateChangeRev1.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspEventSequenceNumber"),
        ("CISCO-ITP-GSP-MIB", "cgspCLLICode"),
        ("CISCO-ITP-GRT-MIB", "cgrtRouteStatus"),
        ("CISCO-ITP-GRT-MIB", "cgrtRouteMgmtStatus"),
        ("CISCO-ITP-GRT-MIB", "cgrtRouteDynamic"),
        ("CISCO-ITP-GRT-MIB", "cgrtRouteAdminStatus"),
        ("CISCO-ITP-GRT-MIB", "cgrtRouteNotifSuppressed"),
        ("CISCO-ITP-GRT-MIB", "cgrtRouteDisplay"))
)
if mibBuilder.loadTexts:
    ciscoGrtMgmtStateChangeRev1.setStatus(
        "current"
    )

ciscoGrtNoRouteMSUDiscards = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 0, 6)
)
ciscoGrtNoRouteMSUDiscards.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspEventSequenceNumber"),
        ("CISCO-ITP-GSP-MIB", "cgspCLLICode"),
        ("CISCO-ITP-GSP-MIB", "cgspInstDisplayName"),
        ("CISCO-ITP-GRT-MIB", "cgrtNoRouteMSUsInterval"),
        ("CISCO-ITP-GRT-MIB", "cgrtIntervalNoRouteMSUs"))
)
if mibBuilder.loadTexts:
    ciscoGrtNoRouteMSUDiscards.setStatus(
        "current"
    )


# Notifications groups

ciscoGrtNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 2, 2, 4)
)
ciscoGrtNotificationsGroup.setObjects(
      *(("CISCO-ITP-GRT-MIB", "ciscoGrtDestStateChange"),
        ("CISCO-ITP-GRT-MIB", "ciscoGrtMgmtStateChange"),
        ("CISCO-ITP-GRT-MIB", "ciscoGrtRouteTableLoad"))
)
if mibBuilder.loadTexts:
    ciscoGrtNotificationsGroup.setStatus(
        "deprecated"
    )

ciscoGrtNotificationsGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 2, 2, 11)
)
ciscoGrtNotificationsGroupRev1.setObjects(
      *(("CISCO-ITP-GRT-MIB", "ciscoGrtRouteTableLoad"),
        ("CISCO-ITP-GRT-MIB", "ciscoGrtDestStateChangeRev1"),
        ("CISCO-ITP-GRT-MIB", "ciscoGrtMgmtStateChangeRev1"),
        ("CISCO-ITP-GRT-MIB", "ciscoGrtNoRouteMSUDiscards"))
)
if mibBuilder.loadTexts:
    ciscoGrtNotificationsGroupRev1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoGrtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoGrtMIBCompliance.setStatus(
        "deprecated"
    )

ciscoGrtMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 334, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoGrtMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ITP-GRT-MIB",
    **{"CgrtDisplayPCSI": CgrtDisplayPCSI,
       "ciscoGrtMIB": ciscoGrtMIB,
       "ciscoGrtNotifications": ciscoGrtNotifications,
       "ciscoGrtDestStateChange": ciscoGrtDestStateChange,
       "ciscoGrtMgmtStateChange": ciscoGrtMgmtStateChange,
       "ciscoGrtRouteTableLoad": ciscoGrtRouteTableLoad,
       "ciscoGrtDestStateChangeRev1": ciscoGrtDestStateChangeRev1,
       "ciscoGrtMgmtStateChangeRev1": ciscoGrtMgmtStateChangeRev1,
       "ciscoGrtNoRouteMSUDiscards": ciscoGrtNoRouteMSUDiscards,
       "ciscoGrtMIBObjects": ciscoGrtMIBObjects,
       "cgrtScalars": cgrtScalars,
       "cgrtRouteMaxDynamic": cgrtRouteMaxDynamic,
       "cgrtDestNotifDelayTime": cgrtDestNotifDelayTime,
       "cgrtDestNotifWindowTime": cgrtDestNotifWindowTime,
       "cgrtDestNotifMaxPerWindow": cgrtDestNotifMaxPerWindow,
       "cgrtDestNotifEnabled": cgrtDestNotifEnabled,
       "cgrtMgmtNotifDelayTime": cgrtMgmtNotifDelayTime,
       "cgrtMgmtNotifWindowTime": cgrtMgmtNotifWindowTime,
       "cgrtMgmtNotifMaxPerWindow": cgrtMgmtNotifMaxPerWindow,
       "cgrtMgmtNotifEnabled": cgrtMgmtNotifEnabled,
       "cgrtRouteTableLoadNotifEnabled": cgrtRouteTableLoadNotifEnabled,
       "cgrtDynamicRoutes": cgrtDynamicRoutes,
       "cgrtDynamicRoutesDropped": cgrtDynamicRoutesDropped,
       "cgrtDestNotifWindowTimeRev1": cgrtDestNotifWindowTimeRev1,
       "cgrtDestNotifMaxPerWindowRev1": cgrtDestNotifMaxPerWindowRev1,
       "cgrtDestNotifEnabledRev1": cgrtDestNotifEnabledRev1,
       "cgrtMgmtNotifWindowTimeRev1": cgrtMgmtNotifWindowTimeRev1,
       "cgrtMgmtNotifMaxPerWindowRev1": cgrtMgmtNotifMaxPerWindowRev1,
       "cgrtMgmtNotifEnabledRev1": cgrtMgmtNotifEnabledRev1,
       "cgrtOrigTableEnabled": cgrtOrigTableEnabled,
       "cgrtPCStatsInterval": cgrtPCStatsInterval,
       "cgrtNoRouteMSUsNotifEnabled": cgrtNoRouteMSUsNotifEnabled,
       "cgrtNoRouteMSUsNotifWindowTime": cgrtNoRouteMSUsNotifWindowTime,
       "cgrtObjects": cgrtObjects,
       "cgrtInstTable": cgrtInstTable,
       "cgrtInstEntry": cgrtInstEntry,
       "cgrtInstLastChanged": cgrtInstLastChanged,
       "cgrtInstLastLoadTime": cgrtInstLastLoadTime,
       "cgrtInstLoadStatus": cgrtInstLoadStatus,
       "cgrtInstTableName": cgrtInstTableName,
       "cgrtInstLastURL": cgrtInstLastURL,
       "cgrtInstNumberDestinations": cgrtInstNumberDestinations,
       "cgrtInstNumberRoutes": cgrtInstNumberRoutes,
       "cgrtInstUnknownOrigPCs": cgrtInstUnknownOrigPCs,
       "cgrtInstNoRouteDrops": cgrtInstNoRouteDrops,
       "cgrtDestTable": cgrtDestTable,
       "cgrtDestEntry": cgrtDestEntry,
       "cgrtDestStatus": cgrtDestStatus,
       "cgrtDestCongestion": cgrtDestCongestion,
       "cgrtDestAccessibleSeconds": cgrtDestAccessibleSeconds,
       "cgrtDestInaccessibleSeconds": cgrtDestInaccessibleSeconds,
       "cgrtDestRestrictedSeconds": cgrtDestRestrictedSeconds,
       "cgrtDestMSUsOut": cgrtDestMSUsOut,
       "cgrtDestOctetsOut": cgrtDestOctetsOut,
       "cgrtDestMSUsIn": cgrtDestMSUsIn,
       "cgrtDestOctetsIn": cgrtDestOctetsIn,
       "cgrtDestInaccessibleDrops": cgrtDestInaccessibleDrops,
       "cgrtDestRestrictedMSUs": cgrtDestRestrictedMSUs,
       "cgrtDestCongestionDrops": cgrtDestCongestionDrops,
       "cgrtDestDisplay": cgrtDestDisplay,
       "cgrtRouteTable": cgrtRouteTable,
       "cgrtRouteEntry": cgrtRouteEntry,
       "cgrtRouteDpc": cgrtRouteDpc,
       "cgrtRouteMask": cgrtRouteMask,
       "cgrtRouteDestLsCost": cgrtRouteDestLsCost,
       "cgrtRouteDestLinkset": cgrtRouteDestLinkset,
       "cgrtRouteQos": cgrtRouteQos,
       "cgrtRouteStatus": cgrtRouteStatus,
       "cgrtRouteMgmtStatus": cgrtRouteMgmtStatus,
       "cgrtRouteDynamic": cgrtRouteDynamic,
       "cgrtRouteType": cgrtRouteType,
       "cgrtRouteAdminStatus": cgrtRouteAdminStatus,
       "cgrtRouteRowStatus": cgrtRouteRowStatus,
       "cgrtRouteAllowedSeconds": cgrtRouteAllowedSeconds,
       "cgrtRouteRestrictedSeconds": cgrtRouteRestrictedSeconds,
       "cgrtRouteProhibitedSeconds": cgrtRouteProhibitedSeconds,
       "cgrtRouteDisplay": cgrtRouteDisplay,
       "cgrtNotificationsInfo": cgrtNotificationsInfo,
       "cgrtDestNotifSupFlag": cgrtDestNotifSupFlag,
       "cgrtDestNotifChanges": cgrtDestNotifChanges,
       "cgrtMgmtNotifSupFlag": cgrtMgmtNotifSupFlag,
       "cgrtMgmtNotifChanges": cgrtMgmtNotifChanges,
       "cgrtDestNotifSuppressed": cgrtDestNotifSuppressed,
       "cgrtRouteNotifSuppressed": cgrtRouteNotifSuppressed,
       "cgrtNoRouteMSUsInterval": cgrtNoRouteMSUsInterval,
       "cgrtIntervalNoRouteMSUs": cgrtIntervalNoRouteMSUs,
       "cgrtOrigTable": cgrtOrigTable,
       "cgrtOrigEntry": cgrtOrigEntry,
       "cgrtOrigPC": cgrtOrigPC,
       "cgrtOrigMSUs": cgrtOrigMSUs,
       "cgrtOrigOctets": cgrtOrigOctets,
       "cgrtOrigDisplay": cgrtOrigDisplay,
       "cgrtDestSITable": cgrtDestSITable,
       "cgrtDestSIEntry": cgrtDestSIEntry,
       "cgrtMtp3SI": cgrtMtp3SI,
       "cgrtDestSIMSUsOut": cgrtDestSIMSUsOut,
       "cgrtDestSIOctetsOut": cgrtDestSIOctetsOut,
       "cgrtDestSIMSUsIn": cgrtDestSIMSUsIn,
       "cgrtDestSIOctetsIn": cgrtDestSIOctetsIn,
       "cgrtDestSIDisplay": cgrtDestSIDisplay,
       "cgrtOrigSITable": cgrtOrigSITable,
       "cgrtOrigSIEntry": cgrtOrigSIEntry,
       "cgrtOrigSIMSUs": cgrtOrigSIMSUs,
       "cgrtOrigSIOctets": cgrtOrigSIOctets,
       "cgrtOrigSIDisplay": cgrtOrigSIDisplay,
       "ciscoGrtMIBConform": ciscoGrtMIBConform,
       "ciscoGrtMIBCompliances": ciscoGrtMIBCompliances,
       "ciscoGrtMIBCompliance": ciscoGrtMIBCompliance,
       "ciscoGrtMIBComplianceRev1": ciscoGrtMIBComplianceRev1,
       "ciscoGrtMIBGroups": ciscoGrtMIBGroups,
       "ciscoGrtInstGroup": ciscoGrtInstGroup,
       "ciscoGrtDestGroup": ciscoGrtDestGroup,
       "ciscoGrtRouteGroup": ciscoGrtRouteGroup,
       "ciscoGrtNotificationsGroup": ciscoGrtNotificationsGroup,
       "ciscoGrtScalarsGroup": ciscoGrtScalarsGroup,
       "ciscoGrtDestGroupRev1": ciscoGrtDestGroupRev1,
       "ciscoGrtRouteGroupRev1": ciscoGrtRouteGroupRev1,
       "ciscoGrtOrigGroup": ciscoGrtOrigGroup,
       "ciscoGrtDestSIGroup": ciscoGrtDestSIGroup,
       "ciscoGrtOrigSIGroup": ciscoGrtOrigSIGroup,
       "ciscoGrtNotificationsGroupRev1": ciscoGrtNotificationsGroupRev1,
       "ciscoGrtInstGroupSup1": ciscoGrtInstGroupSup1}
)
