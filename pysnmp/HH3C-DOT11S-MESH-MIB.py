# SNMP MIB module (HH3C-DOT11S-MESH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-DOT11S-MESH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:58 2024
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

(Hh3cDot11RadioElementIndex,
 hh3cDot11,
 hh3cDot11APElementIndex) = mibBuilder.importSymbols(
    "HH3C-DOT11-REF-MIB",
    "Hh3cDot11RadioElementIndex",
    "hh3cDot11",
    "hh3cDot11APElementIndex")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3cDot11sMesh = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11)
)
hh3cDot11sMesh.setRevisions(
        ("2009-08-01 10:00",
         "2008-11-07 10:00",
         "2008-07-08 18:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cDot11sConfigGroup_ObjectIdentity = ObjectIdentity
hh3cDot11sConfigGroup = _Hh3cDot11sConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 1)
)
_Hh3cDot11sMeshGlobalPara_ObjectIdentity = ObjectIdentity
hh3cDot11sMeshGlobalPara = _Hh3cDot11sMeshGlobalPara_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 1, 1)
)
_Hh3cDot11sMeshMkdID_Type = MacAddress
_Hh3cDot11sMeshMkdID_Object = MibScalar
hh3cDot11sMeshMkdID = _Hh3cDot11sMeshMkdID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 1, 1, 1),
    _Hh3cDot11sMeshMkdID_Type()
)
hh3cDot11sMeshMkdID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11sMeshMkdID.setStatus("current")
_Hh3cDot11sMeshPflTable_Object = MibTable
hh3cDot11sMeshPflTable = _Hh3cDot11sMeshPflTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cDot11sMeshPflTable.setStatus("current")
_Hh3cDot11sMeshPflEntry_Object = MibTableRow
hh3cDot11sMeshPflEntry = _Hh3cDot11sMeshPflEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 1, 2, 1)
)
hh3cDot11sMeshPflEntry.setIndexNames(
    (0, "HH3C-DOT11S-MESH-MIB", "hh3cDot11sMeshPflIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot11sMeshPflEntry.setStatus("current")
_Hh3cDot11sMeshPflIndex_Type = Integer32
_Hh3cDot11sMeshPflIndex_Object = MibTableColumn
hh3cDot11sMeshPflIndex = _Hh3cDot11sMeshPflIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 1, 2, 1, 1),
    _Hh3cDot11sMeshPflIndex_Type()
)
hh3cDot11sMeshPflIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11sMeshPflIndex.setStatus("current")


class _Hh3cDot11sMeshPflMeshID_Type(OctetString):
    """Custom type hh3cDot11sMeshPflMeshID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cDot11sMeshPflMeshID_Type.__name__ = "OctetString"
_Hh3cDot11sMeshPflMeshID_Object = MibTableColumn
hh3cDot11sMeshPflMeshID = _Hh3cDot11sMeshPflMeshID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 1, 2, 1, 2),
    _Hh3cDot11sMeshPflMeshID_Type()
)
hh3cDot11sMeshPflMeshID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11sMeshPflMeshID.setStatus("current")


class _Hh3cDot11sMeshPflBindIntNum_Type(Integer32):
    """Custom type hh3cDot11sMeshPflBindIntNum based on Integer32"""
    defaultValue = -1


_Hh3cDot11sMeshPflBindIntNum_Object = MibTableColumn
hh3cDot11sMeshPflBindIntNum = _Hh3cDot11sMeshPflBindIntNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 1, 2, 1, 3),
    _Hh3cDot11sMeshPflBindIntNum_Type()
)
hh3cDot11sMeshPflBindIntNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11sMeshPflBindIntNum.setStatus("current")


class _Hh3cDot11sMeshPflKeepAlive_Type(Integer32):
    """Custom type hh3cDot11sMeshPflKeepAlive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )


_Hh3cDot11sMeshPflKeepAlive_Type.__name__ = "Integer32"
_Hh3cDot11sMeshPflKeepAlive_Object = MibTableColumn
hh3cDot11sMeshPflKeepAlive = _Hh3cDot11sMeshPflKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 1, 2, 1, 4),
    _Hh3cDot11sMeshPflKeepAlive_Type()
)
hh3cDot11sMeshPflKeepAlive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11sMeshPflKeepAlive.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11sMeshPflKeepAlive.setUnits("second")
_Hh3cDot11sMeshPflBackhaulRate_Type = Integer32
_Hh3cDot11sMeshPflBackhaulRate_Object = MibTableColumn
hh3cDot11sMeshPflBackhaulRate = _Hh3cDot11sMeshPflBackhaulRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 1, 2, 1, 5),
    _Hh3cDot11sMeshPflBackhaulRate_Type()
)
hh3cDot11sMeshPflBackhaulRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11sMeshPflBackhaulRate.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11sMeshPflBackhaulRate.setUnits("Kbps")


class _Hh3cDot11sMeshMkdServEnable_Type(TruthValue):
    """Custom type hh3cDot11sMeshMkdServEnable based on TruthValue"""


_Hh3cDot11sMeshMkdServEnable_Object = MibTableColumn
hh3cDot11sMeshMkdServEnable = _Hh3cDot11sMeshMkdServEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 1, 2, 1, 6),
    _Hh3cDot11sMeshMkdServEnable_Type()
)
hh3cDot11sMeshMkdServEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11sMeshMkdServEnable.setStatus("current")


class _Hh3cDot11sMeshPflEnable_Type(TruthValue):
    """Custom type hh3cDot11sMeshPflEnable based on TruthValue"""


_Hh3cDot11sMeshPflEnable_Object = MibTableColumn
hh3cDot11sMeshPflEnable = _Hh3cDot11sMeshPflEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 1, 2, 1, 7),
    _Hh3cDot11sMeshPflEnable_Type()
)
hh3cDot11sMeshPflEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11sMeshPflEnable.setStatus("current")
_Hh3cDot11sMeshPflRowStatus_Type = RowStatus
_Hh3cDot11sMeshPflRowStatus_Object = MibTableColumn
hh3cDot11sMeshPflRowStatus = _Hh3cDot11sMeshPflRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 1, 2, 1, 8),
    _Hh3cDot11sMeshPflRowStatus_Type()
)
hh3cDot11sMeshPflRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11sMeshPflRowStatus.setStatus("current")
_Hh3cDot11sMpPlcyTable_Object = MibTable
hh3cDot11sMpPlcyTable = _Hh3cDot11sMpPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cDot11sMpPlcyTable.setStatus("current")
_Hh3cDot11sMpPlcyEntry_Object = MibTableRow
hh3cDot11sMpPlcyEntry = _Hh3cDot11sMpPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 1, 3, 1)
)
hh3cDot11sMpPlcyEntry.setIndexNames(
    (0, "HH3C-DOT11S-MESH-MIB", "hh3cDot11sMpPlcyIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot11sMpPlcyEntry.setStatus("current")
_Hh3cDot11sMpPlcyIndex_Type = Integer32
_Hh3cDot11sMpPlcyIndex_Object = MibTableColumn
hh3cDot11sMpPlcyIndex = _Hh3cDot11sMpPlcyIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 1, 3, 1, 1),
    _Hh3cDot11sMpPlcyIndex_Type()
)
hh3cDot11sMpPlcyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11sMpPlcyIndex.setStatus("current")


class _Hh3cDot11sMpPlcyName_Type(OctetString):
    """Custom type hh3cDot11sMpPlcyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_Hh3cDot11sMpPlcyName_Type.__name__ = "OctetString"
_Hh3cDot11sMpPlcyName_Object = MibTableColumn
hh3cDot11sMpPlcyName = _Hh3cDot11sMpPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 1, 3, 1, 2),
    _Hh3cDot11sMpPlcyName_Type()
)
hh3cDot11sMpPlcyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11sMpPlcyName.setStatus("current")


class _Hh3cDot11sMpPlcyInitEnable_Type(TruthValue):
    """Custom type hh3cDot11sMpPlcyInitEnable based on TruthValue"""


_Hh3cDot11sMpPlcyInitEnable_Object = MibTableColumn
hh3cDot11sMpPlcyInitEnable = _Hh3cDot11sMpPlcyInitEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 1, 3, 1, 3),
    _Hh3cDot11sMpPlcyInitEnable_Type()
)
hh3cDot11sMpPlcyInitEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11sMpPlcyInitEnable.setStatus("current")


class _Hh3cDot11sMlspEnable_Type(TruthValue):
    """Custom type hh3cDot11sMlspEnable based on TruthValue"""


_Hh3cDot11sMlspEnable_Object = MibTableColumn
hh3cDot11sMlspEnable = _Hh3cDot11sMlspEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 1, 3, 1, 4),
    _Hh3cDot11sMlspEnable_Type()
)
hh3cDot11sMlspEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11sMlspEnable.setStatus("current")
_Hh3cDot11sProbReqInterval_Type = Integer32
_Hh3cDot11sProbReqInterval_Object = MibTableColumn
hh3cDot11sProbReqInterval = _Hh3cDot11sProbReqInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 1, 3, 1, 5),
    _Hh3cDot11sProbReqInterval_Type()
)
hh3cDot11sProbReqInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11sProbReqInterval.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11sProbReqInterval.setUnits("millisecond")


class _Hh3cDot11sRoleAuthEnable_Type(TruthValue):
    """Custom type hh3cDot11sRoleAuthEnable based on TruthValue"""


_Hh3cDot11sRoleAuthEnable_Object = MibTableColumn
hh3cDot11sRoleAuthEnable = _Hh3cDot11sRoleAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 1, 3, 1, 6),
    _Hh3cDot11sRoleAuthEnable_Type()
)
hh3cDot11sRoleAuthEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11sRoleAuthEnable.setStatus("current")


class _Hh3cDot11sLinkHoldRSSI_Type(Integer32):
    """Custom type hh3cDot11sLinkHoldRSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 100),
    )


_Hh3cDot11sLinkHoldRSSI_Type.__name__ = "Integer32"
_Hh3cDot11sLinkHoldRSSI_Object = MibTableColumn
hh3cDot11sLinkHoldRSSI = _Hh3cDot11sLinkHoldRSSI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 1, 3, 1, 7),
    _Hh3cDot11sLinkHoldRSSI_Type()
)
hh3cDot11sLinkHoldRSSI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11sLinkHoldRSSI.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11sLinkHoldRSSI.setUnits("dBm")


class _Hh3cDot11sLinkHoldTime_Type(Integer32):
    """Custom type hh3cDot11sLinkHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 20000),
    )


_Hh3cDot11sLinkHoldTime_Type.__name__ = "Integer32"
_Hh3cDot11sLinkHoldTime_Object = MibTableColumn
hh3cDot11sLinkHoldTime = _Hh3cDot11sLinkHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 1, 3, 1, 8),
    _Hh3cDot11sLinkHoldTime_Type()
)
hh3cDot11sLinkHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11sLinkHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11sLinkHoldTime.setUnits("millisecond")


class _Hh3cDot11sSwitchMargin_Type(Integer32):
    """Custom type hh3cDot11sSwitchMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Hh3cDot11sSwitchMargin_Type.__name__ = "Integer32"
_Hh3cDot11sSwitchMargin_Object = MibTableColumn
hh3cDot11sSwitchMargin = _Hh3cDot11sSwitchMargin_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 1, 3, 1, 9),
    _Hh3cDot11sSwitchMargin_Type()
)
hh3cDot11sSwitchMargin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11sSwitchMargin.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11sSwitchMargin.setUnits("dBm")


class _Hh3cDot11sLinkSaturationRSSI_Type(Integer32):
    """Custom type hh3cDot11sLinkSaturationRSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 150),
    )


_Hh3cDot11sLinkSaturationRSSI_Type.__name__ = "Integer32"
_Hh3cDot11sLinkSaturationRSSI_Object = MibTableColumn
hh3cDot11sLinkSaturationRSSI = _Hh3cDot11sLinkSaturationRSSI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 1, 3, 1, 10),
    _Hh3cDot11sLinkSaturationRSSI_Type()
)
hh3cDot11sLinkSaturationRSSI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11sLinkSaturationRSSI.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11sLinkSaturationRSSI.setUnits("dBm")


class _Hh3cDot11sLinkRateMode_Type(Integer32):
    """Custom type hh3cDot11sLinkRateMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("realtime", 2))
    )


_Hh3cDot11sLinkRateMode_Type.__name__ = "Integer32"
_Hh3cDot11sLinkRateMode_Object = MibTableColumn
hh3cDot11sLinkRateMode = _Hh3cDot11sLinkRateMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 1, 3, 1, 11),
    _Hh3cDot11sLinkRateMode_Type()
)
hh3cDot11sLinkRateMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11sLinkRateMode.setStatus("current")
_Hh3cDot11sMaxLinkNum_Type = Integer32
_Hh3cDot11sMaxLinkNum_Object = MibTableColumn
hh3cDot11sMaxLinkNum = _Hh3cDot11sMaxLinkNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 1, 3, 1, 12),
    _Hh3cDot11sMaxLinkNum_Type()
)
hh3cDot11sMaxLinkNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11sMaxLinkNum.setStatus("current")
_Hh3cDot11sMpPlcyRowStatus_Type = RowStatus
_Hh3cDot11sMpPlcyRowStatus_Object = MibTableColumn
hh3cDot11sMpPlcyRowStatus = _Hh3cDot11sMpPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 1, 3, 1, 13),
    _Hh3cDot11sMpPlcyRowStatus_Type()
)
hh3cDot11sMpPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11sMpPlcyRowStatus.setStatus("current")
_Hh3cDot11sMlspCfgTable_Object = MibTable
hh3cDot11sMlspCfgTable = _Hh3cDot11sMlspCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cDot11sMlspCfgTable.setStatus("current")
_Hh3cDot11sMlspCfgEntry_Object = MibTableRow
hh3cDot11sMlspCfgEntry = _Hh3cDot11sMlspCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 1, 4, 1)
)
hh3cDot11sMlspCfgEntry.setIndexNames(
    (0, "HH3C-DOT11S-MESH-MIB", "hh3cDot11sMpPlcyIndex"),
    (0, "HH3C-DOT11S-MESH-MIB", "hh3cDot11sMlspProxyIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot11sMlspCfgEntry.setStatus("current")
_Hh3cDot11sMlspProxyIndex_Type = Integer32
_Hh3cDot11sMlspProxyIndex_Object = MibTableColumn
hh3cDot11sMlspProxyIndex = _Hh3cDot11sMlspProxyIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 1, 4, 1, 1),
    _Hh3cDot11sMlspProxyIndex_Type()
)
hh3cDot11sMlspProxyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11sMlspProxyIndex.setStatus("current")
_Hh3cDot11sMlspProxyMac_Type = MacAddress
_Hh3cDot11sMlspProxyMac_Object = MibTableColumn
hh3cDot11sMlspProxyMac = _Hh3cDot11sMlspProxyMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 1, 4, 1, 2),
    _Hh3cDot11sMlspProxyMac_Type()
)
hh3cDot11sMlspProxyMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11sMlspProxyMac.setStatus("current")
_Hh3cDot11sMlspRowStatus_Type = RowStatus
_Hh3cDot11sMlspRowStatus_Object = MibTableColumn
hh3cDot11sMlspRowStatus = _Hh3cDot11sMlspRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 1, 4, 1, 3),
    _Hh3cDot11sMlspRowStatus_Type()
)
hh3cDot11sMlspRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11sMlspRowStatus.setStatus("current")
_Hh3cDot11sRadioCfgTable_Object = MibTable
hh3cDot11sRadioCfgTable = _Hh3cDot11sRadioCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 1, 5)
)
if mibBuilder.loadTexts:
    hh3cDot11sRadioCfgTable.setStatus("current")
_Hh3cDot11sRadioCfgEntry_Object = MibTableRow
hh3cDot11sRadioCfgEntry = _Hh3cDot11sRadioCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 1, 5, 1)
)
hh3cDot11sRadioCfgEntry.setIndexNames(
    (0, "HH3C-DOT11S-MESH-MIB", "hh3cDot11sCfgRadioIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot11sRadioCfgEntry.setStatus("current")
_Hh3cDot11sCfgRadioIndex_Type = Hh3cDot11RadioElementIndex
_Hh3cDot11sCfgRadioIndex_Object = MibTableColumn
hh3cDot11sCfgRadioIndex = _Hh3cDot11sCfgRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 1, 5, 1, 1),
    _Hh3cDot11sCfgRadioIndex_Type()
)
hh3cDot11sCfgRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11sCfgRadioIndex.setStatus("current")


class _Hh3cDot11sMeshPflMap_Type(Integer32):
    """Custom type hh3cDot11sMeshPflMap based on Integer32"""
    defaultValue = 0


_Hh3cDot11sMeshPflMap_Object = MibTableColumn
hh3cDot11sMeshPflMap = _Hh3cDot11sMeshPflMap_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 1, 5, 1, 2),
    _Hh3cDot11sMeshPflMap_Type()
)
hh3cDot11sMeshPflMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11sMeshPflMap.setStatus("current")


class _Hh3cDot11sMpPlcyMap_Type(Integer32):
    """Custom type hh3cDot11sMpPlcyMap based on Integer32"""
    defaultValue = 1


_Hh3cDot11sMpPlcyMap_Object = MibTableColumn
hh3cDot11sMpPlcyMap = _Hh3cDot11sMpPlcyMap_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 1, 5, 1, 3),
    _Hh3cDot11sMpPlcyMap_Type()
)
hh3cDot11sMpPlcyMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11sMpPlcyMap.setStatus("current")
_Hh3cDot11sAPCfgTable_Object = MibTable
hh3cDot11sAPCfgTable = _Hh3cDot11sAPCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 1, 6)
)
if mibBuilder.loadTexts:
    hh3cDot11sAPCfgTable.setStatus("current")
_Hh3cDot11sAPCfgEntry_Object = MibTableRow
hh3cDot11sAPCfgEntry = _Hh3cDot11sAPCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 1, 6, 1)
)
hh3cDot11sAPCfgEntry.setIndexNames(
    (0, "HH3C-DOT11-REF-MIB", "hh3cDot11APElementIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot11sAPCfgEntry.setStatus("current")


class _Hh3cDot11sPortalEnable_Type(TruthValue):
    """Custom type hh3cDot11sPortalEnable based on TruthValue"""


_Hh3cDot11sPortalEnable_Object = MibTableColumn
hh3cDot11sPortalEnable = _Hh3cDot11sPortalEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 1, 6, 1, 1),
    _Hh3cDot11sPortalEnable_Type()
)
hh3cDot11sPortalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11sPortalEnable.setStatus("current")
_Hh3cDot11sWDSConfigGroup_ObjectIdentity = ObjectIdentity
hh3cDot11sWDSConfigGroup = _Hh3cDot11sWDSConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 2)
)
_Hh3cDot11sWDSPeerMacTable_Object = MibTable
hh3cDot11sWDSPeerMacTable = _Hh3cDot11sWDSPeerMacTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cDot11sWDSPeerMacTable.setStatus("current")
_Hh3cDot11sWDSPeerMacEntry_Object = MibTableRow
hh3cDot11sWDSPeerMacEntry = _Hh3cDot11sWDSPeerMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 2, 1, 1)
)
hh3cDot11sWDSPeerMacEntry.setIndexNames(
    (0, "HH3C-DOT11S-MESH-MIB", "hh3cDot11sCfgRadioIndex"),
    (0, "HH3C-DOT11S-MESH-MIB", "hh3cDot11sWDSPeerMacIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot11sWDSPeerMacEntry.setStatus("current")
_Hh3cDot11sWDSPeerMacIndex_Type = Integer32
_Hh3cDot11sWDSPeerMacIndex_Object = MibTableColumn
hh3cDot11sWDSPeerMacIndex = _Hh3cDot11sWDSPeerMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 2, 1, 1, 1),
    _Hh3cDot11sWDSPeerMacIndex_Type()
)
hh3cDot11sWDSPeerMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11sWDSPeerMacIndex.setStatus("current")
_Hh3cDot11sWDSPeerMacAddrss_Type = MacAddress
_Hh3cDot11sWDSPeerMacAddrss_Object = MibTableColumn
hh3cDot11sWDSPeerMacAddrss = _Hh3cDot11sWDSPeerMacAddrss_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 2, 1, 1, 2),
    _Hh3cDot11sWDSPeerMacAddrss_Type()
)
hh3cDot11sWDSPeerMacAddrss.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11sWDSPeerMacAddrss.setStatus("current")
_Hh3cDot11sWDSPeerMacRowStatus_Type = RowStatus
_Hh3cDot11sWDSPeerMacRowStatus_Object = MibTableColumn
hh3cDot11sWDSPeerMacRowStatus = _Hh3cDot11sWDSPeerMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 2, 1, 1, 3),
    _Hh3cDot11sWDSPeerMacRowStatus_Type()
)
hh3cDot11sWDSPeerMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11sWDSPeerMacRowStatus.setStatus("current")
_Hh3cDot11sMeshStatusGroup_ObjectIdentity = ObjectIdentity
hh3cDot11sMeshStatusGroup = _Hh3cDot11sMeshStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 3)
)
_Hh3cDot11sMeshLinkStatusTable_Object = MibTable
hh3cDot11sMeshLinkStatusTable = _Hh3cDot11sMeshLinkStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 3, 1)
)
if mibBuilder.loadTexts:
    hh3cDot11sMeshLinkStatusTable.setStatus("current")
_Hh3cDot11sMeshLinkStatusEntry_Object = MibTableRow
hh3cDot11sMeshLinkStatusEntry = _Hh3cDot11sMeshLinkStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 3, 1, 1)
)
hh3cDot11sMeshLinkStatusEntry.setIndexNames(
    (0, "HH3C-DOT11S-MESH-MIB", "hh3cDot11sMeshLinkIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot11sMeshLinkStatusEntry.setStatus("current")
_Hh3cDot11sMeshLinkIfIndex_Type = Unsigned32
_Hh3cDot11sMeshLinkIfIndex_Object = MibTableColumn
hh3cDot11sMeshLinkIfIndex = _Hh3cDot11sMeshLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 3, 1, 1, 1),
    _Hh3cDot11sMeshLinkIfIndex_Type()
)
hh3cDot11sMeshLinkIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11sMeshLinkIfIndex.setStatus("current")
_Hh3cDot11sMeshLinkName_Type = OctetString
_Hh3cDot11sMeshLinkName_Object = MibTableColumn
hh3cDot11sMeshLinkName = _Hh3cDot11sMeshLinkName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 3, 1, 1, 2),
    _Hh3cDot11sMeshLinkName_Type()
)
hh3cDot11sMeshLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11sMeshLinkName.setStatus("current")
_Hh3cDot11sMeshLinkBSSID_Type = MacAddress
_Hh3cDot11sMeshLinkBSSID_Object = MibTableColumn
hh3cDot11sMeshLinkBSSID = _Hh3cDot11sMeshLinkBSSID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 3, 1, 1, 3),
    _Hh3cDot11sMeshLinkBSSID_Type()
)
hh3cDot11sMeshLinkBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11sMeshLinkBSSID.setStatus("current")
_Hh3cDot11sMeshLinkPeerMac_Type = MacAddress
_Hh3cDot11sMeshLinkPeerMac_Object = MibTableColumn
hh3cDot11sMeshLinkPeerMac = _Hh3cDot11sMeshLinkPeerMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 3, 1, 1, 4),
    _Hh3cDot11sMeshLinkPeerMac_Type()
)
hh3cDot11sMeshLinkPeerMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11sMeshLinkPeerMac.setStatus("current")
_Hh3cDot11sMeshLinkExistDuration_Type = Integer32
_Hh3cDot11sMeshLinkExistDuration_Object = MibTableColumn
hh3cDot11sMeshLinkExistDuration = _Hh3cDot11sMeshLinkExistDuration_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 3, 1, 1, 5),
    _Hh3cDot11sMeshLinkExistDuration_Type()
)
hh3cDot11sMeshLinkExistDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11sMeshLinkExistDuration.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11sMeshLinkExistDuration.setUnits("second")
_Hh3cDot11sMeshLinkStatisTable_Object = MibTable
hh3cDot11sMeshLinkStatisTable = _Hh3cDot11sMeshLinkStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 3, 2)
)
if mibBuilder.loadTexts:
    hh3cDot11sMeshLinkStatisTable.setStatus("current")
_Hh3cDot11sMeshLinkStatisEntry_Object = MibTableRow
hh3cDot11sMeshLinkStatisEntry = _Hh3cDot11sMeshLinkStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 3, 2, 1)
)
hh3cDot11sMeshLinkStatisEntry.setIndexNames(
    (0, "HH3C-DOT11-REF-MIB", "hh3cDot11APElementIndex"),
    (0, "HH3C-DOT11S-MESH-MIB", "hh3cDot11sMeshLinkStatIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot11sMeshLinkStatisEntry.setStatus("current")
_Hh3cDot11sMeshLinkStatIfIndex_Type = Unsigned32
_Hh3cDot11sMeshLinkStatIfIndex_Object = MibTableColumn
hh3cDot11sMeshLinkStatIfIndex = _Hh3cDot11sMeshLinkStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 3, 2, 1, 1),
    _Hh3cDot11sMeshLinkStatIfIndex_Type()
)
hh3cDot11sMeshLinkStatIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11sMeshLinkStatIfIndex.setStatus("current")
_Hh3cDot11sMeshLinkNbrIndex_Type = Unsigned32
_Hh3cDot11sMeshLinkNbrIndex_Object = MibTableColumn
hh3cDot11sMeshLinkNbrIndex = _Hh3cDot11sMeshLinkNbrIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 3, 2, 1, 2),
    _Hh3cDot11sMeshLinkNbrIndex_Type()
)
hh3cDot11sMeshLinkNbrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11sMeshLinkNbrIndex.setStatus("current")
_Hh3cDot11sMeshLinkRxTotByte_Type = Counter32
_Hh3cDot11sMeshLinkRxTotByte_Object = MibTableColumn
hh3cDot11sMeshLinkRxTotByte = _Hh3cDot11sMeshLinkRxTotByte_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 3, 2, 1, 3),
    _Hh3cDot11sMeshLinkRxTotByte_Type()
)
hh3cDot11sMeshLinkRxTotByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11sMeshLinkRxTotByte.setStatus("current")
_Hh3cDot11sMeshLinkRxTotPkt_Type = Counter32
_Hh3cDot11sMeshLinkRxTotPkt_Object = MibTableColumn
hh3cDot11sMeshLinkRxTotPkt = _Hh3cDot11sMeshLinkRxTotPkt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 3, 2, 1, 4),
    _Hh3cDot11sMeshLinkRxTotPkt_Type()
)
hh3cDot11sMeshLinkRxTotPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11sMeshLinkRxTotPkt.setStatus("current")
_Hh3cDot11sMeshLinkRxUniPkt_Type = Counter32
_Hh3cDot11sMeshLinkRxUniPkt_Object = MibTableColumn
hh3cDot11sMeshLinkRxUniPkt = _Hh3cDot11sMeshLinkRxUniPkt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 3, 2, 1, 5),
    _Hh3cDot11sMeshLinkRxUniPkt_Type()
)
hh3cDot11sMeshLinkRxUniPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11sMeshLinkRxUniPkt.setStatus("current")
_Hh3cDot11sMeshLinkRxBrocPkt_Type = Counter32
_Hh3cDot11sMeshLinkRxBrocPkt_Object = MibTableColumn
hh3cDot11sMeshLinkRxBrocPkt = _Hh3cDot11sMeshLinkRxBrocPkt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 3, 2, 1, 6),
    _Hh3cDot11sMeshLinkRxBrocPkt_Type()
)
hh3cDot11sMeshLinkRxBrocPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11sMeshLinkRxBrocPkt.setStatus("current")
_Hh3cDot11sMeshLinkRxMuticPkt_Type = Counter32
_Hh3cDot11sMeshLinkRxMuticPkt_Object = MibTableColumn
hh3cDot11sMeshLinkRxMuticPkt = _Hh3cDot11sMeshLinkRxMuticPkt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 3, 2, 1, 7),
    _Hh3cDot11sMeshLinkRxMuticPkt_Type()
)
hh3cDot11sMeshLinkRxMuticPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11sMeshLinkRxMuticPkt.setStatus("current")
_Hh3cDot11sMeshLinkRxDiscPkt_Type = Counter32
_Hh3cDot11sMeshLinkRxDiscPkt_Object = MibTableColumn
hh3cDot11sMeshLinkRxDiscPkt = _Hh3cDot11sMeshLinkRxDiscPkt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 3, 2, 1, 8),
    _Hh3cDot11sMeshLinkRxDiscPkt_Type()
)
hh3cDot11sMeshLinkRxDiscPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11sMeshLinkRxDiscPkt.setStatus("current")
_Hh3cDot11sMeshLinkTxTotByte_Type = Counter32
_Hh3cDot11sMeshLinkTxTotByte_Object = MibTableColumn
hh3cDot11sMeshLinkTxTotByte = _Hh3cDot11sMeshLinkTxTotByte_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 3, 2, 1, 9),
    _Hh3cDot11sMeshLinkTxTotByte_Type()
)
hh3cDot11sMeshLinkTxTotByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11sMeshLinkTxTotByte.setStatus("current")
_Hh3cDot11sMeshLinkTxTotPkt_Type = Counter32
_Hh3cDot11sMeshLinkTxTotPkt_Object = MibTableColumn
hh3cDot11sMeshLinkTxTotPkt = _Hh3cDot11sMeshLinkTxTotPkt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 3, 2, 1, 10),
    _Hh3cDot11sMeshLinkTxTotPkt_Type()
)
hh3cDot11sMeshLinkTxTotPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11sMeshLinkTxTotPkt.setStatus("current")
_Hh3cDot11sMeshLinkTxUniPkt_Type = Counter32
_Hh3cDot11sMeshLinkTxUniPkt_Object = MibTableColumn
hh3cDot11sMeshLinkTxUniPkt = _Hh3cDot11sMeshLinkTxUniPkt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 3, 2, 1, 11),
    _Hh3cDot11sMeshLinkTxUniPkt_Type()
)
hh3cDot11sMeshLinkTxUniPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11sMeshLinkTxUniPkt.setStatus("current")
_Hh3cDot11sMeshLinkTxBrocPkt_Type = Counter32
_Hh3cDot11sMeshLinkTxBrocPkt_Object = MibTableColumn
hh3cDot11sMeshLinkTxBrocPkt = _Hh3cDot11sMeshLinkTxBrocPkt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 3, 2, 1, 12),
    _Hh3cDot11sMeshLinkTxBrocPkt_Type()
)
hh3cDot11sMeshLinkTxBrocPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11sMeshLinkTxBrocPkt.setStatus("current")
_Hh3cDot11sMeshLinkTxMuticPkt_Type = Counter32
_Hh3cDot11sMeshLinkTxMuticPkt_Object = MibTableColumn
hh3cDot11sMeshLinkTxMuticPkt = _Hh3cDot11sMeshLinkTxMuticPkt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 3, 2, 1, 13),
    _Hh3cDot11sMeshLinkTxMuticPkt_Type()
)
hh3cDot11sMeshLinkTxMuticPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11sMeshLinkTxMuticPkt.setStatus("current")
_Hh3cDot11sMeshLinkTxDiscPkt_Type = Counter32
_Hh3cDot11sMeshLinkTxDiscPkt_Object = MibTableColumn
hh3cDot11sMeshLinkTxDiscPkt = _Hh3cDot11sMeshLinkTxDiscPkt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 3, 2, 1, 14),
    _Hh3cDot11sMeshLinkTxDiscPkt_Type()
)
hh3cDot11sMeshLinkTxDiscPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11sMeshLinkTxDiscPkt.setStatus("current")
_Hh3cDot11sMeshLinkIFName_Type = OctetString
_Hh3cDot11sMeshLinkIFName_Object = MibTableColumn
hh3cDot11sMeshLinkIFName = _Hh3cDot11sMeshLinkIFName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 3, 2, 1, 15),
    _Hh3cDot11sMeshLinkIFName_Type()
)
hh3cDot11sMeshLinkIFName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11sMeshLinkIFName.setStatus("current")
_Hh3cDot11sMeshNbrStatusTable_Object = MibTable
hh3cDot11sMeshNbrStatusTable = _Hh3cDot11sMeshNbrStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 3, 3)
)
if mibBuilder.loadTexts:
    hh3cDot11sMeshNbrStatusTable.setStatus("current")
_Hh3cDot11sMeshNbrStatusEntry_Object = MibTableRow
hh3cDot11sMeshNbrStatusEntry = _Hh3cDot11sMeshNbrStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 3, 3, 1)
)
hh3cDot11sMeshNbrStatusEntry.setIndexNames(
    (0, "HH3C-DOT11-REF-MIB", "hh3cDot11APElementIndex"),
    (0, "HH3C-DOT11S-MESH-MIB", "hh3cDot11sMeshNbrIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot11sMeshNbrStatusEntry.setStatus("current")
_Hh3cDot11sMeshNbrIndex_Type = Unsigned32
_Hh3cDot11sMeshNbrIndex_Object = MibTableColumn
hh3cDot11sMeshNbrIndex = _Hh3cDot11sMeshNbrIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 3, 3, 1, 1),
    _Hh3cDot11sMeshNbrIndex_Type()
)
hh3cDot11sMeshNbrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11sMeshNbrIndex.setStatus("current")
_Hh3cDot11sMeshNbrRadioID_Type = Unsigned32
_Hh3cDot11sMeshNbrRadioID_Object = MibTableColumn
hh3cDot11sMeshNbrRadioID = _Hh3cDot11sMeshNbrRadioID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 3, 3, 1, 2),
    _Hh3cDot11sMeshNbrRadioID_Type()
)
hh3cDot11sMeshNbrRadioID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11sMeshNbrRadioID.setStatus("current")


class _Hh3cDot11sMeshLocalMeshID_Type(OctetString):
    """Custom type hh3cDot11sMeshLocalMeshID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cDot11sMeshLocalMeshID_Type.__name__ = "OctetString"
_Hh3cDot11sMeshLocalMeshID_Object = MibTableColumn
hh3cDot11sMeshLocalMeshID = _Hh3cDot11sMeshLocalMeshID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 3, 3, 1, 3),
    _Hh3cDot11sMeshLocalMeshID_Type()
)
hh3cDot11sMeshLocalMeshID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11sMeshLocalMeshID.setStatus("current")


class _Hh3cDot11sMeshNbrMeshID_Type(OctetString):
    """Custom type hh3cDot11sMeshNbrMeshID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cDot11sMeshNbrMeshID_Type.__name__ = "OctetString"
_Hh3cDot11sMeshNbrMeshID_Object = MibTableColumn
hh3cDot11sMeshNbrMeshID = _Hh3cDot11sMeshNbrMeshID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 3, 3, 1, 4),
    _Hh3cDot11sMeshNbrMeshID_Type()
)
hh3cDot11sMeshNbrMeshID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11sMeshNbrMeshID.setStatus("current")
_Hh3cDot11sMeshNbrBSSID_Type = MacAddress
_Hh3cDot11sMeshNbrBSSID_Object = MibTableColumn
hh3cDot11sMeshNbrBSSID = _Hh3cDot11sMeshNbrBSSID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 3, 3, 1, 5),
    _Hh3cDot11sMeshNbrBSSID_Type()
)
hh3cDot11sMeshNbrBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11sMeshNbrBSSID.setStatus("current")
_Hh3cDot11sMeshNbrPeerMac_Type = MacAddress
_Hh3cDot11sMeshNbrPeerMac_Object = MibTableColumn
hh3cDot11sMeshNbrPeerMac = _Hh3cDot11sMeshNbrPeerMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 3, 3, 1, 6),
    _Hh3cDot11sMeshNbrPeerMac_Type()
)
hh3cDot11sMeshNbrPeerMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11sMeshNbrPeerMac.setStatus("current")
_Hh3cDot11sMeshLinkInMp_Type = Unsigned32
_Hh3cDot11sMeshLinkInMp_Object = MibTableColumn
hh3cDot11sMeshLinkInMp = _Hh3cDot11sMeshLinkInMp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 3, 3, 1, 7),
    _Hh3cDot11sMeshLinkInMp_Type()
)
hh3cDot11sMeshLinkInMp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11sMeshLinkInMp.setStatus("current")


class _Hh3cDot11sMeshMPLinkStatus_Type(Integer32):
    """Custom type hh3cDot11sMeshMPLinkStatus based on Integer32"""
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
          ("processing", 1),
          ("up", 2))
    )


_Hh3cDot11sMeshMPLinkStatus_Type.__name__ = "Integer32"
_Hh3cDot11sMeshMPLinkStatus_Object = MibTableColumn
hh3cDot11sMeshMPLinkStatus = _Hh3cDot11sMeshMPLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 3, 3, 1, 8),
    _Hh3cDot11sMeshMPLinkStatus_Type()
)
hh3cDot11sMeshMPLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11sMeshMPLinkStatus.setStatus("current")
_Hh3cDot11sMeshNbrChannel_Type = Unsigned32
_Hh3cDot11sMeshNbrChannel_Object = MibTableColumn
hh3cDot11sMeshNbrChannel = _Hh3cDot11sMeshNbrChannel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 3, 3, 1, 9),
    _Hh3cDot11sMeshNbrChannel_Type()
)
hh3cDot11sMeshNbrChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11sMeshNbrChannel.setStatus("current")
_Hh3cDot11sMeshNbrLinkDuration_Type = Integer32
_Hh3cDot11sMeshNbrLinkDuration_Object = MibTableColumn
hh3cDot11sMeshNbrLinkDuration = _Hh3cDot11sMeshNbrLinkDuration_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 3, 3, 1, 10),
    _Hh3cDot11sMeshNbrLinkDuration_Type()
)
hh3cDot11sMeshNbrLinkDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11sMeshNbrLinkDuration.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11sMeshNbrLinkDuration.setUnits("second")
_Hh3cDot11sMeshNbrRSSI_Type = Integer32
_Hh3cDot11sMeshNbrRSSI_Object = MibTableColumn
hh3cDot11sMeshNbrRSSI = _Hh3cDot11sMeshNbrRSSI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 3, 3, 1, 11),
    _Hh3cDot11sMeshNbrRSSI_Type()
)
hh3cDot11sMeshNbrRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11sMeshNbrRSSI.setStatus("current")
_Hh3cDot11sMeshNbrSNR_Type = Integer32
_Hh3cDot11sMeshNbrSNR_Object = MibTableColumn
hh3cDot11sMeshNbrSNR = _Hh3cDot11sMeshNbrSNR_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 11, 3, 3, 1, 12),
    _Hh3cDot11sMeshNbrSNR_Type()
)
hh3cDot11sMeshNbrSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11sMeshNbrSNR.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11sMeshNbrSNR.setUnits("percent")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-DOT11S-MESH-MIB",
    **{"hh3cDot11sMesh": hh3cDot11sMesh,
       "hh3cDot11sConfigGroup": hh3cDot11sConfigGroup,
       "hh3cDot11sMeshGlobalPara": hh3cDot11sMeshGlobalPara,
       "hh3cDot11sMeshMkdID": hh3cDot11sMeshMkdID,
       "hh3cDot11sMeshPflTable": hh3cDot11sMeshPflTable,
       "hh3cDot11sMeshPflEntry": hh3cDot11sMeshPflEntry,
       "hh3cDot11sMeshPflIndex": hh3cDot11sMeshPflIndex,
       "hh3cDot11sMeshPflMeshID": hh3cDot11sMeshPflMeshID,
       "hh3cDot11sMeshPflBindIntNum": hh3cDot11sMeshPflBindIntNum,
       "hh3cDot11sMeshPflKeepAlive": hh3cDot11sMeshPflKeepAlive,
       "hh3cDot11sMeshPflBackhaulRate": hh3cDot11sMeshPflBackhaulRate,
       "hh3cDot11sMeshMkdServEnable": hh3cDot11sMeshMkdServEnable,
       "hh3cDot11sMeshPflEnable": hh3cDot11sMeshPflEnable,
       "hh3cDot11sMeshPflRowStatus": hh3cDot11sMeshPflRowStatus,
       "hh3cDot11sMpPlcyTable": hh3cDot11sMpPlcyTable,
       "hh3cDot11sMpPlcyEntry": hh3cDot11sMpPlcyEntry,
       "hh3cDot11sMpPlcyIndex": hh3cDot11sMpPlcyIndex,
       "hh3cDot11sMpPlcyName": hh3cDot11sMpPlcyName,
       "hh3cDot11sMpPlcyInitEnable": hh3cDot11sMpPlcyInitEnable,
       "hh3cDot11sMlspEnable": hh3cDot11sMlspEnable,
       "hh3cDot11sProbReqInterval": hh3cDot11sProbReqInterval,
       "hh3cDot11sRoleAuthEnable": hh3cDot11sRoleAuthEnable,
       "hh3cDot11sLinkHoldRSSI": hh3cDot11sLinkHoldRSSI,
       "hh3cDot11sLinkHoldTime": hh3cDot11sLinkHoldTime,
       "hh3cDot11sSwitchMargin": hh3cDot11sSwitchMargin,
       "hh3cDot11sLinkSaturationRSSI": hh3cDot11sLinkSaturationRSSI,
       "hh3cDot11sLinkRateMode": hh3cDot11sLinkRateMode,
       "hh3cDot11sMaxLinkNum": hh3cDot11sMaxLinkNum,
       "hh3cDot11sMpPlcyRowStatus": hh3cDot11sMpPlcyRowStatus,
       "hh3cDot11sMlspCfgTable": hh3cDot11sMlspCfgTable,
       "hh3cDot11sMlspCfgEntry": hh3cDot11sMlspCfgEntry,
       "hh3cDot11sMlspProxyIndex": hh3cDot11sMlspProxyIndex,
       "hh3cDot11sMlspProxyMac": hh3cDot11sMlspProxyMac,
       "hh3cDot11sMlspRowStatus": hh3cDot11sMlspRowStatus,
       "hh3cDot11sRadioCfgTable": hh3cDot11sRadioCfgTable,
       "hh3cDot11sRadioCfgEntry": hh3cDot11sRadioCfgEntry,
       "hh3cDot11sCfgRadioIndex": hh3cDot11sCfgRadioIndex,
       "hh3cDot11sMeshPflMap": hh3cDot11sMeshPflMap,
       "hh3cDot11sMpPlcyMap": hh3cDot11sMpPlcyMap,
       "hh3cDot11sAPCfgTable": hh3cDot11sAPCfgTable,
       "hh3cDot11sAPCfgEntry": hh3cDot11sAPCfgEntry,
       "hh3cDot11sPortalEnable": hh3cDot11sPortalEnable,
       "hh3cDot11sWDSConfigGroup": hh3cDot11sWDSConfigGroup,
       "hh3cDot11sWDSPeerMacTable": hh3cDot11sWDSPeerMacTable,
       "hh3cDot11sWDSPeerMacEntry": hh3cDot11sWDSPeerMacEntry,
       "hh3cDot11sWDSPeerMacIndex": hh3cDot11sWDSPeerMacIndex,
       "hh3cDot11sWDSPeerMacAddrss": hh3cDot11sWDSPeerMacAddrss,
       "hh3cDot11sWDSPeerMacRowStatus": hh3cDot11sWDSPeerMacRowStatus,
       "hh3cDot11sMeshStatusGroup": hh3cDot11sMeshStatusGroup,
       "hh3cDot11sMeshLinkStatusTable": hh3cDot11sMeshLinkStatusTable,
       "hh3cDot11sMeshLinkStatusEntry": hh3cDot11sMeshLinkStatusEntry,
       "hh3cDot11sMeshLinkIfIndex": hh3cDot11sMeshLinkIfIndex,
       "hh3cDot11sMeshLinkName": hh3cDot11sMeshLinkName,
       "hh3cDot11sMeshLinkBSSID": hh3cDot11sMeshLinkBSSID,
       "hh3cDot11sMeshLinkPeerMac": hh3cDot11sMeshLinkPeerMac,
       "hh3cDot11sMeshLinkExistDuration": hh3cDot11sMeshLinkExistDuration,
       "hh3cDot11sMeshLinkStatisTable": hh3cDot11sMeshLinkStatisTable,
       "hh3cDot11sMeshLinkStatisEntry": hh3cDot11sMeshLinkStatisEntry,
       "hh3cDot11sMeshLinkStatIfIndex": hh3cDot11sMeshLinkStatIfIndex,
       "hh3cDot11sMeshLinkNbrIndex": hh3cDot11sMeshLinkNbrIndex,
       "hh3cDot11sMeshLinkRxTotByte": hh3cDot11sMeshLinkRxTotByte,
       "hh3cDot11sMeshLinkRxTotPkt": hh3cDot11sMeshLinkRxTotPkt,
       "hh3cDot11sMeshLinkRxUniPkt": hh3cDot11sMeshLinkRxUniPkt,
       "hh3cDot11sMeshLinkRxBrocPkt": hh3cDot11sMeshLinkRxBrocPkt,
       "hh3cDot11sMeshLinkRxMuticPkt": hh3cDot11sMeshLinkRxMuticPkt,
       "hh3cDot11sMeshLinkRxDiscPkt": hh3cDot11sMeshLinkRxDiscPkt,
       "hh3cDot11sMeshLinkTxTotByte": hh3cDot11sMeshLinkTxTotByte,
       "hh3cDot11sMeshLinkTxTotPkt": hh3cDot11sMeshLinkTxTotPkt,
       "hh3cDot11sMeshLinkTxUniPkt": hh3cDot11sMeshLinkTxUniPkt,
       "hh3cDot11sMeshLinkTxBrocPkt": hh3cDot11sMeshLinkTxBrocPkt,
       "hh3cDot11sMeshLinkTxMuticPkt": hh3cDot11sMeshLinkTxMuticPkt,
       "hh3cDot11sMeshLinkTxDiscPkt": hh3cDot11sMeshLinkTxDiscPkt,
       "hh3cDot11sMeshLinkIFName": hh3cDot11sMeshLinkIFName,
       "hh3cDot11sMeshNbrStatusTable": hh3cDot11sMeshNbrStatusTable,
       "hh3cDot11sMeshNbrStatusEntry": hh3cDot11sMeshNbrStatusEntry,
       "hh3cDot11sMeshNbrIndex": hh3cDot11sMeshNbrIndex,
       "hh3cDot11sMeshNbrRadioID": hh3cDot11sMeshNbrRadioID,
       "hh3cDot11sMeshLocalMeshID": hh3cDot11sMeshLocalMeshID,
       "hh3cDot11sMeshNbrMeshID": hh3cDot11sMeshNbrMeshID,
       "hh3cDot11sMeshNbrBSSID": hh3cDot11sMeshNbrBSSID,
       "hh3cDot11sMeshNbrPeerMac": hh3cDot11sMeshNbrPeerMac,
       "hh3cDot11sMeshLinkInMp": hh3cDot11sMeshLinkInMp,
       "hh3cDot11sMeshMPLinkStatus": hh3cDot11sMeshMPLinkStatus,
       "hh3cDot11sMeshNbrChannel": hh3cDot11sMeshNbrChannel,
       "hh3cDot11sMeshNbrLinkDuration": hh3cDot11sMeshNbrLinkDuration,
       "hh3cDot11sMeshNbrRSSI": hh3cDot11sMeshNbrRSSI,
       "hh3cDot11sMeshNbrSNR": hh3cDot11sMeshNbrSNR}
)
