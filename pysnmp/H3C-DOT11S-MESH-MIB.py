# SNMP MIB module (H3C-DOT11S-MESH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-DOT11S-MESH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:50:18 2024
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

(H3cDot11RadioElementIndex,
 h3cDot11,
 h3cDot11APElementIndex) = mibBuilder.importSymbols(
    "H3C-DOT11-REF-MIB",
    "H3cDot11RadioElementIndex",
    "h3cDot11",
    "h3cDot11APElementIndex")

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

h3cDot11sMesh = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11)
)
h3cDot11sMesh.setRevisions(
        ("2009-08-01 10:00",
         "2008-11-07 10:00",
         "2008-07-08 18:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cDot11sConfigGroup_ObjectIdentity = ObjectIdentity
h3cDot11sConfigGroup = _H3cDot11sConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 1)
)
_H3cDot11sMeshGlobalPara_ObjectIdentity = ObjectIdentity
h3cDot11sMeshGlobalPara = _H3cDot11sMeshGlobalPara_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 1, 1)
)
_H3cDot11sMeshMkdID_Type = MacAddress
_H3cDot11sMeshMkdID_Object = MibScalar
h3cDot11sMeshMkdID = _H3cDot11sMeshMkdID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 1, 1, 1),
    _H3cDot11sMeshMkdID_Type()
)
h3cDot11sMeshMkdID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11sMeshMkdID.setStatus("current")
_H3cDot11sMeshPflTable_Object = MibTable
h3cDot11sMeshPflTable = _H3cDot11sMeshPflTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 1, 2)
)
if mibBuilder.loadTexts:
    h3cDot11sMeshPflTable.setStatus("current")
_H3cDot11sMeshPflEntry_Object = MibTableRow
h3cDot11sMeshPflEntry = _H3cDot11sMeshPflEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 1, 2, 1)
)
h3cDot11sMeshPflEntry.setIndexNames(
    (0, "H3C-DOT11S-MESH-MIB", "h3cDot11sMeshPflIndex"),
)
if mibBuilder.loadTexts:
    h3cDot11sMeshPflEntry.setStatus("current")
_H3cDot11sMeshPflIndex_Type = Integer32
_H3cDot11sMeshPflIndex_Object = MibTableColumn
h3cDot11sMeshPflIndex = _H3cDot11sMeshPflIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 1, 2, 1, 1),
    _H3cDot11sMeshPflIndex_Type()
)
h3cDot11sMeshPflIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11sMeshPflIndex.setStatus("current")


class _H3cDot11sMeshPflMeshID_Type(OctetString):
    """Custom type h3cDot11sMeshPflMeshID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cDot11sMeshPflMeshID_Type.__name__ = "OctetString"
_H3cDot11sMeshPflMeshID_Object = MibTableColumn
h3cDot11sMeshPflMeshID = _H3cDot11sMeshPflMeshID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 1, 2, 1, 2),
    _H3cDot11sMeshPflMeshID_Type()
)
h3cDot11sMeshPflMeshID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11sMeshPflMeshID.setStatus("current")


class _H3cDot11sMeshPflBindIntNum_Type(Integer32):
    """Custom type h3cDot11sMeshPflBindIntNum based on Integer32"""
    defaultValue = -1


_H3cDot11sMeshPflBindIntNum_Object = MibTableColumn
h3cDot11sMeshPflBindIntNum = _H3cDot11sMeshPflBindIntNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 1, 2, 1, 3),
    _H3cDot11sMeshPflBindIntNum_Type()
)
h3cDot11sMeshPflBindIntNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11sMeshPflBindIntNum.setStatus("current")


class _H3cDot11sMeshPflKeepAlive_Type(Integer32):
    """Custom type h3cDot11sMeshPflKeepAlive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )


_H3cDot11sMeshPflKeepAlive_Type.__name__ = "Integer32"
_H3cDot11sMeshPflKeepAlive_Object = MibTableColumn
h3cDot11sMeshPflKeepAlive = _H3cDot11sMeshPflKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 1, 2, 1, 4),
    _H3cDot11sMeshPflKeepAlive_Type()
)
h3cDot11sMeshPflKeepAlive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11sMeshPflKeepAlive.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11sMeshPflKeepAlive.setUnits("second")
_H3cDot11sMeshPflBackhaulRate_Type = Integer32
_H3cDot11sMeshPflBackhaulRate_Object = MibTableColumn
h3cDot11sMeshPflBackhaulRate = _H3cDot11sMeshPflBackhaulRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 1, 2, 1, 5),
    _H3cDot11sMeshPflBackhaulRate_Type()
)
h3cDot11sMeshPflBackhaulRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11sMeshPflBackhaulRate.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11sMeshPflBackhaulRate.setUnits("Kbps")


class _H3cDot11sMeshMkdServEnable_Type(TruthValue):
    """Custom type h3cDot11sMeshMkdServEnable based on TruthValue"""


_H3cDot11sMeshMkdServEnable_Object = MibTableColumn
h3cDot11sMeshMkdServEnable = _H3cDot11sMeshMkdServEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 1, 2, 1, 6),
    _H3cDot11sMeshMkdServEnable_Type()
)
h3cDot11sMeshMkdServEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11sMeshMkdServEnable.setStatus("current")


class _H3cDot11sMeshPflEnable_Type(TruthValue):
    """Custom type h3cDot11sMeshPflEnable based on TruthValue"""


_H3cDot11sMeshPflEnable_Object = MibTableColumn
h3cDot11sMeshPflEnable = _H3cDot11sMeshPflEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 1, 2, 1, 7),
    _H3cDot11sMeshPflEnable_Type()
)
h3cDot11sMeshPflEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11sMeshPflEnable.setStatus("current")
_H3cDot11sMeshPflRowStatus_Type = RowStatus
_H3cDot11sMeshPflRowStatus_Object = MibTableColumn
h3cDot11sMeshPflRowStatus = _H3cDot11sMeshPflRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 1, 2, 1, 8),
    _H3cDot11sMeshPflRowStatus_Type()
)
h3cDot11sMeshPflRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11sMeshPflRowStatus.setStatus("current")
_H3cDot11sMpPlcyTable_Object = MibTable
h3cDot11sMpPlcyTable = _H3cDot11sMpPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 1, 3)
)
if mibBuilder.loadTexts:
    h3cDot11sMpPlcyTable.setStatus("current")
_H3cDot11sMpPlcyEntry_Object = MibTableRow
h3cDot11sMpPlcyEntry = _H3cDot11sMpPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 1, 3, 1)
)
h3cDot11sMpPlcyEntry.setIndexNames(
    (0, "H3C-DOT11S-MESH-MIB", "h3cDot11sMpPlcyIndex"),
)
if mibBuilder.loadTexts:
    h3cDot11sMpPlcyEntry.setStatus("current")
_H3cDot11sMpPlcyIndex_Type = Integer32
_H3cDot11sMpPlcyIndex_Object = MibTableColumn
h3cDot11sMpPlcyIndex = _H3cDot11sMpPlcyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 1, 3, 1, 1),
    _H3cDot11sMpPlcyIndex_Type()
)
h3cDot11sMpPlcyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11sMpPlcyIndex.setStatus("current")


class _H3cDot11sMpPlcyName_Type(OctetString):
    """Custom type h3cDot11sMpPlcyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_H3cDot11sMpPlcyName_Type.__name__ = "OctetString"
_H3cDot11sMpPlcyName_Object = MibTableColumn
h3cDot11sMpPlcyName = _H3cDot11sMpPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 1, 3, 1, 2),
    _H3cDot11sMpPlcyName_Type()
)
h3cDot11sMpPlcyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11sMpPlcyName.setStatus("current")


class _H3cDot11sMpPlcyInitEnable_Type(TruthValue):
    """Custom type h3cDot11sMpPlcyInitEnable based on TruthValue"""


_H3cDot11sMpPlcyInitEnable_Object = MibTableColumn
h3cDot11sMpPlcyInitEnable = _H3cDot11sMpPlcyInitEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 1, 3, 1, 3),
    _H3cDot11sMpPlcyInitEnable_Type()
)
h3cDot11sMpPlcyInitEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11sMpPlcyInitEnable.setStatus("current")


class _H3cDot11sMlspEnable_Type(TruthValue):
    """Custom type h3cDot11sMlspEnable based on TruthValue"""


_H3cDot11sMlspEnable_Object = MibTableColumn
h3cDot11sMlspEnable = _H3cDot11sMlspEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 1, 3, 1, 4),
    _H3cDot11sMlspEnable_Type()
)
h3cDot11sMlspEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11sMlspEnable.setStatus("current")
_H3cDot11sProbReqInterval_Type = Integer32
_H3cDot11sProbReqInterval_Object = MibTableColumn
h3cDot11sProbReqInterval = _H3cDot11sProbReqInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 1, 3, 1, 5),
    _H3cDot11sProbReqInterval_Type()
)
h3cDot11sProbReqInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11sProbReqInterval.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11sProbReqInterval.setUnits("millisecond")


class _H3cDot11sRoleAuthEnable_Type(TruthValue):
    """Custom type h3cDot11sRoleAuthEnable based on TruthValue"""


_H3cDot11sRoleAuthEnable_Object = MibTableColumn
h3cDot11sRoleAuthEnable = _H3cDot11sRoleAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 1, 3, 1, 6),
    _H3cDot11sRoleAuthEnable_Type()
)
h3cDot11sRoleAuthEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11sRoleAuthEnable.setStatus("current")


class _H3cDot11sLinkHoldRSSI_Type(Integer32):
    """Custom type h3cDot11sLinkHoldRSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 100),
    )


_H3cDot11sLinkHoldRSSI_Type.__name__ = "Integer32"
_H3cDot11sLinkHoldRSSI_Object = MibTableColumn
h3cDot11sLinkHoldRSSI = _H3cDot11sLinkHoldRSSI_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 1, 3, 1, 7),
    _H3cDot11sLinkHoldRSSI_Type()
)
h3cDot11sLinkHoldRSSI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11sLinkHoldRSSI.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11sLinkHoldRSSI.setUnits("dBm")


class _H3cDot11sLinkHoldTime_Type(Integer32):
    """Custom type h3cDot11sLinkHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 20000),
    )


_H3cDot11sLinkHoldTime_Type.__name__ = "Integer32"
_H3cDot11sLinkHoldTime_Object = MibTableColumn
h3cDot11sLinkHoldTime = _H3cDot11sLinkHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 1, 3, 1, 8),
    _H3cDot11sLinkHoldTime_Type()
)
h3cDot11sLinkHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11sLinkHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11sLinkHoldTime.setUnits("millisecond")


class _H3cDot11sSwitchMargin_Type(Integer32):
    """Custom type h3cDot11sSwitchMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_H3cDot11sSwitchMargin_Type.__name__ = "Integer32"
_H3cDot11sSwitchMargin_Object = MibTableColumn
h3cDot11sSwitchMargin = _H3cDot11sSwitchMargin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 1, 3, 1, 9),
    _H3cDot11sSwitchMargin_Type()
)
h3cDot11sSwitchMargin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11sSwitchMargin.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11sSwitchMargin.setUnits("dBm")


class _H3cDot11sLinkSaturationRSSI_Type(Integer32):
    """Custom type h3cDot11sLinkSaturationRSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 150),
    )


_H3cDot11sLinkSaturationRSSI_Type.__name__ = "Integer32"
_H3cDot11sLinkSaturationRSSI_Object = MibTableColumn
h3cDot11sLinkSaturationRSSI = _H3cDot11sLinkSaturationRSSI_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 1, 3, 1, 10),
    _H3cDot11sLinkSaturationRSSI_Type()
)
h3cDot11sLinkSaturationRSSI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11sLinkSaturationRSSI.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11sLinkSaturationRSSI.setUnits("dBm")


class _H3cDot11sLinkRateMode_Type(Integer32):
    """Custom type h3cDot11sLinkRateMode based on Integer32"""
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


_H3cDot11sLinkRateMode_Type.__name__ = "Integer32"
_H3cDot11sLinkRateMode_Object = MibTableColumn
h3cDot11sLinkRateMode = _H3cDot11sLinkRateMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 1, 3, 1, 11),
    _H3cDot11sLinkRateMode_Type()
)
h3cDot11sLinkRateMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11sLinkRateMode.setStatus("current")
_H3cDot11sMaxLinkNum_Type = Integer32
_H3cDot11sMaxLinkNum_Object = MibTableColumn
h3cDot11sMaxLinkNum = _H3cDot11sMaxLinkNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 1, 3, 1, 12),
    _H3cDot11sMaxLinkNum_Type()
)
h3cDot11sMaxLinkNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11sMaxLinkNum.setStatus("current")
_H3cDot11sMpPlcyRowStatus_Type = RowStatus
_H3cDot11sMpPlcyRowStatus_Object = MibTableColumn
h3cDot11sMpPlcyRowStatus = _H3cDot11sMpPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 1, 3, 1, 13),
    _H3cDot11sMpPlcyRowStatus_Type()
)
h3cDot11sMpPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11sMpPlcyRowStatus.setStatus("current")
_H3cDot11sMlspCfgTable_Object = MibTable
h3cDot11sMlspCfgTable = _H3cDot11sMlspCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 1, 4)
)
if mibBuilder.loadTexts:
    h3cDot11sMlspCfgTable.setStatus("current")
_H3cDot11sMlspCfgEntry_Object = MibTableRow
h3cDot11sMlspCfgEntry = _H3cDot11sMlspCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 1, 4, 1)
)
h3cDot11sMlspCfgEntry.setIndexNames(
    (0, "H3C-DOT11S-MESH-MIB", "h3cDot11sMpPlcyIndex"),
    (0, "H3C-DOT11S-MESH-MIB", "h3cDot11sMlspProxyIndex"),
)
if mibBuilder.loadTexts:
    h3cDot11sMlspCfgEntry.setStatus("current")
_H3cDot11sMlspProxyIndex_Type = Integer32
_H3cDot11sMlspProxyIndex_Object = MibTableColumn
h3cDot11sMlspProxyIndex = _H3cDot11sMlspProxyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 1, 4, 1, 1),
    _H3cDot11sMlspProxyIndex_Type()
)
h3cDot11sMlspProxyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11sMlspProxyIndex.setStatus("current")
_H3cDot11sMlspProxyMac_Type = MacAddress
_H3cDot11sMlspProxyMac_Object = MibTableColumn
h3cDot11sMlspProxyMac = _H3cDot11sMlspProxyMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 1, 4, 1, 2),
    _H3cDot11sMlspProxyMac_Type()
)
h3cDot11sMlspProxyMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11sMlspProxyMac.setStatus("current")
_H3cDot11sMlspRowStatus_Type = RowStatus
_H3cDot11sMlspRowStatus_Object = MibTableColumn
h3cDot11sMlspRowStatus = _H3cDot11sMlspRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 1, 4, 1, 3),
    _H3cDot11sMlspRowStatus_Type()
)
h3cDot11sMlspRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11sMlspRowStatus.setStatus("current")
_H3cDot11sRadioCfgTable_Object = MibTable
h3cDot11sRadioCfgTable = _H3cDot11sRadioCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 1, 5)
)
if mibBuilder.loadTexts:
    h3cDot11sRadioCfgTable.setStatus("current")
_H3cDot11sRadioCfgEntry_Object = MibTableRow
h3cDot11sRadioCfgEntry = _H3cDot11sRadioCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 1, 5, 1)
)
h3cDot11sRadioCfgEntry.setIndexNames(
    (0, "H3C-DOT11S-MESH-MIB", "h3cDot11sCfgRadioIndex"),
)
if mibBuilder.loadTexts:
    h3cDot11sRadioCfgEntry.setStatus("current")
_H3cDot11sCfgRadioIndex_Type = H3cDot11RadioElementIndex
_H3cDot11sCfgRadioIndex_Object = MibTableColumn
h3cDot11sCfgRadioIndex = _H3cDot11sCfgRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 1, 5, 1, 1),
    _H3cDot11sCfgRadioIndex_Type()
)
h3cDot11sCfgRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11sCfgRadioIndex.setStatus("current")


class _H3cDot11sMeshPflMap_Type(Integer32):
    """Custom type h3cDot11sMeshPflMap based on Integer32"""
    defaultValue = 0


_H3cDot11sMeshPflMap_Object = MibTableColumn
h3cDot11sMeshPflMap = _H3cDot11sMeshPflMap_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 1, 5, 1, 2),
    _H3cDot11sMeshPflMap_Type()
)
h3cDot11sMeshPflMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11sMeshPflMap.setStatus("current")


class _H3cDot11sMpPlcyMap_Type(Integer32):
    """Custom type h3cDot11sMpPlcyMap based on Integer32"""
    defaultValue = 1


_H3cDot11sMpPlcyMap_Object = MibTableColumn
h3cDot11sMpPlcyMap = _H3cDot11sMpPlcyMap_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 1, 5, 1, 3),
    _H3cDot11sMpPlcyMap_Type()
)
h3cDot11sMpPlcyMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11sMpPlcyMap.setStatus("current")
_H3cDot11sAPCfgTable_Object = MibTable
h3cDot11sAPCfgTable = _H3cDot11sAPCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 1, 6)
)
if mibBuilder.loadTexts:
    h3cDot11sAPCfgTable.setStatus("current")
_H3cDot11sAPCfgEntry_Object = MibTableRow
h3cDot11sAPCfgEntry = _H3cDot11sAPCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 1, 6, 1)
)
h3cDot11sAPCfgEntry.setIndexNames(
    (0, "H3C-DOT11-REF-MIB", "h3cDot11APElementIndex"),
)
if mibBuilder.loadTexts:
    h3cDot11sAPCfgEntry.setStatus("current")


class _H3cDot11sPortalEnable_Type(TruthValue):
    """Custom type h3cDot11sPortalEnable based on TruthValue"""


_H3cDot11sPortalEnable_Object = MibTableColumn
h3cDot11sPortalEnable = _H3cDot11sPortalEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 1, 6, 1, 1),
    _H3cDot11sPortalEnable_Type()
)
h3cDot11sPortalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11sPortalEnable.setStatus("current")
_H3cDot11sWDSConfigGroup_ObjectIdentity = ObjectIdentity
h3cDot11sWDSConfigGroup = _H3cDot11sWDSConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 2)
)
_H3cDot11sWDSPeerMacTable_Object = MibTable
h3cDot11sWDSPeerMacTable = _H3cDot11sWDSPeerMacTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 2, 1)
)
if mibBuilder.loadTexts:
    h3cDot11sWDSPeerMacTable.setStatus("current")
_H3cDot11sWDSPeerMacEntry_Object = MibTableRow
h3cDot11sWDSPeerMacEntry = _H3cDot11sWDSPeerMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 2, 1, 1)
)
h3cDot11sWDSPeerMacEntry.setIndexNames(
    (0, "H3C-DOT11S-MESH-MIB", "h3cDot11sCfgRadioIndex"),
    (0, "H3C-DOT11S-MESH-MIB", "h3cDot11sWDSPeerMacIndex"),
)
if mibBuilder.loadTexts:
    h3cDot11sWDSPeerMacEntry.setStatus("current")
_H3cDot11sWDSPeerMacIndex_Type = Integer32
_H3cDot11sWDSPeerMacIndex_Object = MibTableColumn
h3cDot11sWDSPeerMacIndex = _H3cDot11sWDSPeerMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 2, 1, 1, 1),
    _H3cDot11sWDSPeerMacIndex_Type()
)
h3cDot11sWDSPeerMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11sWDSPeerMacIndex.setStatus("current")
_H3cDot11sWDSPeerMacAddrss_Type = MacAddress
_H3cDot11sWDSPeerMacAddrss_Object = MibTableColumn
h3cDot11sWDSPeerMacAddrss = _H3cDot11sWDSPeerMacAddrss_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 2, 1, 1, 2),
    _H3cDot11sWDSPeerMacAddrss_Type()
)
h3cDot11sWDSPeerMacAddrss.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11sWDSPeerMacAddrss.setStatus("current")
_H3cDot11sWDSPeerMacRowStatus_Type = RowStatus
_H3cDot11sWDSPeerMacRowStatus_Object = MibTableColumn
h3cDot11sWDSPeerMacRowStatus = _H3cDot11sWDSPeerMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 2, 1, 1, 3),
    _H3cDot11sWDSPeerMacRowStatus_Type()
)
h3cDot11sWDSPeerMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11sWDSPeerMacRowStatus.setStatus("current")
_H3cDot11sMeshStatusGroup_ObjectIdentity = ObjectIdentity
h3cDot11sMeshStatusGroup = _H3cDot11sMeshStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 3)
)
_H3cDot11sMeshLinkStatusTable_Object = MibTable
h3cDot11sMeshLinkStatusTable = _H3cDot11sMeshLinkStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 3, 1)
)
if mibBuilder.loadTexts:
    h3cDot11sMeshLinkStatusTable.setStatus("current")
_H3cDot11sMeshLinkStatusEntry_Object = MibTableRow
h3cDot11sMeshLinkStatusEntry = _H3cDot11sMeshLinkStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 3, 1, 1)
)
h3cDot11sMeshLinkStatusEntry.setIndexNames(
    (0, "H3C-DOT11S-MESH-MIB", "h3cDot11sMeshLinkIfIndex"),
)
if mibBuilder.loadTexts:
    h3cDot11sMeshLinkStatusEntry.setStatus("current")
_H3cDot11sMeshLinkIfIndex_Type = Unsigned32
_H3cDot11sMeshLinkIfIndex_Object = MibTableColumn
h3cDot11sMeshLinkIfIndex = _H3cDot11sMeshLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 3, 1, 1, 1),
    _H3cDot11sMeshLinkIfIndex_Type()
)
h3cDot11sMeshLinkIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11sMeshLinkIfIndex.setStatus("current")
_H3cDot11sMeshLinkName_Type = OctetString
_H3cDot11sMeshLinkName_Object = MibTableColumn
h3cDot11sMeshLinkName = _H3cDot11sMeshLinkName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 3, 1, 1, 2),
    _H3cDot11sMeshLinkName_Type()
)
h3cDot11sMeshLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11sMeshLinkName.setStatus("current")
_H3cDot11sMeshLinkBSSID_Type = MacAddress
_H3cDot11sMeshLinkBSSID_Object = MibTableColumn
h3cDot11sMeshLinkBSSID = _H3cDot11sMeshLinkBSSID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 3, 1, 1, 3),
    _H3cDot11sMeshLinkBSSID_Type()
)
h3cDot11sMeshLinkBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11sMeshLinkBSSID.setStatus("current")
_H3cDot11sMeshLinkPeerMac_Type = MacAddress
_H3cDot11sMeshLinkPeerMac_Object = MibTableColumn
h3cDot11sMeshLinkPeerMac = _H3cDot11sMeshLinkPeerMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 3, 1, 1, 4),
    _H3cDot11sMeshLinkPeerMac_Type()
)
h3cDot11sMeshLinkPeerMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11sMeshLinkPeerMac.setStatus("current")
_H3cDot11sMeshLinkExistDuration_Type = Integer32
_H3cDot11sMeshLinkExistDuration_Object = MibTableColumn
h3cDot11sMeshLinkExistDuration = _H3cDot11sMeshLinkExistDuration_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 3, 1, 1, 5),
    _H3cDot11sMeshLinkExistDuration_Type()
)
h3cDot11sMeshLinkExistDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11sMeshLinkExistDuration.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11sMeshLinkExistDuration.setUnits("second")
_H3cDot11sMeshLinkStatisTable_Object = MibTable
h3cDot11sMeshLinkStatisTable = _H3cDot11sMeshLinkStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 3, 2)
)
if mibBuilder.loadTexts:
    h3cDot11sMeshLinkStatisTable.setStatus("current")
_H3cDot11sMeshLinkStatisEntry_Object = MibTableRow
h3cDot11sMeshLinkStatisEntry = _H3cDot11sMeshLinkStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 3, 2, 1)
)
h3cDot11sMeshLinkStatisEntry.setIndexNames(
    (0, "H3C-DOT11-REF-MIB", "h3cDot11APElementIndex"),
    (0, "H3C-DOT11S-MESH-MIB", "h3cDot11sMeshLinkStatIfIndex"),
)
if mibBuilder.loadTexts:
    h3cDot11sMeshLinkStatisEntry.setStatus("current")
_H3cDot11sMeshLinkStatIfIndex_Type = Unsigned32
_H3cDot11sMeshLinkStatIfIndex_Object = MibTableColumn
h3cDot11sMeshLinkStatIfIndex = _H3cDot11sMeshLinkStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 3, 2, 1, 1),
    _H3cDot11sMeshLinkStatIfIndex_Type()
)
h3cDot11sMeshLinkStatIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11sMeshLinkStatIfIndex.setStatus("current")
_H3cDot11sMeshLinkNbrIndex_Type = Unsigned32
_H3cDot11sMeshLinkNbrIndex_Object = MibTableColumn
h3cDot11sMeshLinkNbrIndex = _H3cDot11sMeshLinkNbrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 3, 2, 1, 2),
    _H3cDot11sMeshLinkNbrIndex_Type()
)
h3cDot11sMeshLinkNbrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11sMeshLinkNbrIndex.setStatus("current")
_H3cDot11sMeshLinkRxTotByte_Type = Counter32
_H3cDot11sMeshLinkRxTotByte_Object = MibTableColumn
h3cDot11sMeshLinkRxTotByte = _H3cDot11sMeshLinkRxTotByte_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 3, 2, 1, 3),
    _H3cDot11sMeshLinkRxTotByte_Type()
)
h3cDot11sMeshLinkRxTotByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11sMeshLinkRxTotByte.setStatus("current")
_H3cDot11sMeshLinkRxTotPkt_Type = Counter32
_H3cDot11sMeshLinkRxTotPkt_Object = MibTableColumn
h3cDot11sMeshLinkRxTotPkt = _H3cDot11sMeshLinkRxTotPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 3, 2, 1, 4),
    _H3cDot11sMeshLinkRxTotPkt_Type()
)
h3cDot11sMeshLinkRxTotPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11sMeshLinkRxTotPkt.setStatus("current")
_H3cDot11sMeshLinkRxUniPkt_Type = Counter32
_H3cDot11sMeshLinkRxUniPkt_Object = MibTableColumn
h3cDot11sMeshLinkRxUniPkt = _H3cDot11sMeshLinkRxUniPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 3, 2, 1, 5),
    _H3cDot11sMeshLinkRxUniPkt_Type()
)
h3cDot11sMeshLinkRxUniPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11sMeshLinkRxUniPkt.setStatus("current")
_H3cDot11sMeshLinkRxBrocPkt_Type = Counter32
_H3cDot11sMeshLinkRxBrocPkt_Object = MibTableColumn
h3cDot11sMeshLinkRxBrocPkt = _H3cDot11sMeshLinkRxBrocPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 3, 2, 1, 6),
    _H3cDot11sMeshLinkRxBrocPkt_Type()
)
h3cDot11sMeshLinkRxBrocPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11sMeshLinkRxBrocPkt.setStatus("current")
_H3cDot11sMeshLinkRxMuticPkt_Type = Counter32
_H3cDot11sMeshLinkRxMuticPkt_Object = MibTableColumn
h3cDot11sMeshLinkRxMuticPkt = _H3cDot11sMeshLinkRxMuticPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 3, 2, 1, 7),
    _H3cDot11sMeshLinkRxMuticPkt_Type()
)
h3cDot11sMeshLinkRxMuticPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11sMeshLinkRxMuticPkt.setStatus("current")
_H3cDot11sMeshLinkRxDiscPkt_Type = Counter32
_H3cDot11sMeshLinkRxDiscPkt_Object = MibTableColumn
h3cDot11sMeshLinkRxDiscPkt = _H3cDot11sMeshLinkRxDiscPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 3, 2, 1, 8),
    _H3cDot11sMeshLinkRxDiscPkt_Type()
)
h3cDot11sMeshLinkRxDiscPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11sMeshLinkRxDiscPkt.setStatus("current")
_H3cDot11sMeshLinkTxTotByte_Type = Counter32
_H3cDot11sMeshLinkTxTotByte_Object = MibTableColumn
h3cDot11sMeshLinkTxTotByte = _H3cDot11sMeshLinkTxTotByte_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 3, 2, 1, 9),
    _H3cDot11sMeshLinkTxTotByte_Type()
)
h3cDot11sMeshLinkTxTotByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11sMeshLinkTxTotByte.setStatus("current")
_H3cDot11sMeshLinkTxTotPkt_Type = Counter32
_H3cDot11sMeshLinkTxTotPkt_Object = MibTableColumn
h3cDot11sMeshLinkTxTotPkt = _H3cDot11sMeshLinkTxTotPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 3, 2, 1, 10),
    _H3cDot11sMeshLinkTxTotPkt_Type()
)
h3cDot11sMeshLinkTxTotPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11sMeshLinkTxTotPkt.setStatus("current")
_H3cDot11sMeshLinkTxUniPkt_Type = Counter32
_H3cDot11sMeshLinkTxUniPkt_Object = MibTableColumn
h3cDot11sMeshLinkTxUniPkt = _H3cDot11sMeshLinkTxUniPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 3, 2, 1, 11),
    _H3cDot11sMeshLinkTxUniPkt_Type()
)
h3cDot11sMeshLinkTxUniPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11sMeshLinkTxUniPkt.setStatus("current")
_H3cDot11sMeshLinkTxBrocPkt_Type = Counter32
_H3cDot11sMeshLinkTxBrocPkt_Object = MibTableColumn
h3cDot11sMeshLinkTxBrocPkt = _H3cDot11sMeshLinkTxBrocPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 3, 2, 1, 12),
    _H3cDot11sMeshLinkTxBrocPkt_Type()
)
h3cDot11sMeshLinkTxBrocPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11sMeshLinkTxBrocPkt.setStatus("current")
_H3cDot11sMeshLinkTxMuticPkt_Type = Counter32
_H3cDot11sMeshLinkTxMuticPkt_Object = MibTableColumn
h3cDot11sMeshLinkTxMuticPkt = _H3cDot11sMeshLinkTxMuticPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 3, 2, 1, 13),
    _H3cDot11sMeshLinkTxMuticPkt_Type()
)
h3cDot11sMeshLinkTxMuticPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11sMeshLinkTxMuticPkt.setStatus("current")
_H3cDot11sMeshLinkTxDiscPkt_Type = Counter32
_H3cDot11sMeshLinkTxDiscPkt_Object = MibTableColumn
h3cDot11sMeshLinkTxDiscPkt = _H3cDot11sMeshLinkTxDiscPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 3, 2, 1, 14),
    _H3cDot11sMeshLinkTxDiscPkt_Type()
)
h3cDot11sMeshLinkTxDiscPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11sMeshLinkTxDiscPkt.setStatus("current")
_H3cDot11sMeshLinkIFName_Type = OctetString
_H3cDot11sMeshLinkIFName_Object = MibTableColumn
h3cDot11sMeshLinkIFName = _H3cDot11sMeshLinkIFName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 3, 2, 1, 15),
    _H3cDot11sMeshLinkIFName_Type()
)
h3cDot11sMeshLinkIFName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11sMeshLinkIFName.setStatus("current")
_H3cDot11sMeshNbrStatusTable_Object = MibTable
h3cDot11sMeshNbrStatusTable = _H3cDot11sMeshNbrStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 3, 3)
)
if mibBuilder.loadTexts:
    h3cDot11sMeshNbrStatusTable.setStatus("current")
_H3cDot11sMeshNbrStatusEntry_Object = MibTableRow
h3cDot11sMeshNbrStatusEntry = _H3cDot11sMeshNbrStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 3, 3, 1)
)
h3cDot11sMeshNbrStatusEntry.setIndexNames(
    (0, "H3C-DOT11-REF-MIB", "h3cDot11APElementIndex"),
    (0, "H3C-DOT11S-MESH-MIB", "h3cDot11sMeshNbrIndex"),
)
if mibBuilder.loadTexts:
    h3cDot11sMeshNbrStatusEntry.setStatus("current")
_H3cDot11sMeshNbrIndex_Type = Unsigned32
_H3cDot11sMeshNbrIndex_Object = MibTableColumn
h3cDot11sMeshNbrIndex = _H3cDot11sMeshNbrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 3, 3, 1, 1),
    _H3cDot11sMeshNbrIndex_Type()
)
h3cDot11sMeshNbrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11sMeshNbrIndex.setStatus("current")
_H3cDot11sMeshNbrRadioID_Type = Unsigned32
_H3cDot11sMeshNbrRadioID_Object = MibTableColumn
h3cDot11sMeshNbrRadioID = _H3cDot11sMeshNbrRadioID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 3, 3, 1, 2),
    _H3cDot11sMeshNbrRadioID_Type()
)
h3cDot11sMeshNbrRadioID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11sMeshNbrRadioID.setStatus("current")


class _H3cDot11sMeshLocalMeshID_Type(OctetString):
    """Custom type h3cDot11sMeshLocalMeshID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cDot11sMeshLocalMeshID_Type.__name__ = "OctetString"
_H3cDot11sMeshLocalMeshID_Object = MibTableColumn
h3cDot11sMeshLocalMeshID = _H3cDot11sMeshLocalMeshID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 3, 3, 1, 3),
    _H3cDot11sMeshLocalMeshID_Type()
)
h3cDot11sMeshLocalMeshID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11sMeshLocalMeshID.setStatus("current")


class _H3cDot11sMeshNbrMeshID_Type(OctetString):
    """Custom type h3cDot11sMeshNbrMeshID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cDot11sMeshNbrMeshID_Type.__name__ = "OctetString"
_H3cDot11sMeshNbrMeshID_Object = MibTableColumn
h3cDot11sMeshNbrMeshID = _H3cDot11sMeshNbrMeshID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 3, 3, 1, 4),
    _H3cDot11sMeshNbrMeshID_Type()
)
h3cDot11sMeshNbrMeshID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11sMeshNbrMeshID.setStatus("current")
_H3cDot11sMeshNbrBSSID_Type = MacAddress
_H3cDot11sMeshNbrBSSID_Object = MibTableColumn
h3cDot11sMeshNbrBSSID = _H3cDot11sMeshNbrBSSID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 3, 3, 1, 5),
    _H3cDot11sMeshNbrBSSID_Type()
)
h3cDot11sMeshNbrBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11sMeshNbrBSSID.setStatus("current")
_H3cDot11sMeshNbrPeerMac_Type = MacAddress
_H3cDot11sMeshNbrPeerMac_Object = MibTableColumn
h3cDot11sMeshNbrPeerMac = _H3cDot11sMeshNbrPeerMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 3, 3, 1, 6),
    _H3cDot11sMeshNbrPeerMac_Type()
)
h3cDot11sMeshNbrPeerMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11sMeshNbrPeerMac.setStatus("current")
_H3cDot11sMeshLinkInMp_Type = Unsigned32
_H3cDot11sMeshLinkInMp_Object = MibTableColumn
h3cDot11sMeshLinkInMp = _H3cDot11sMeshLinkInMp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 3, 3, 1, 7),
    _H3cDot11sMeshLinkInMp_Type()
)
h3cDot11sMeshLinkInMp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11sMeshLinkInMp.setStatus("current")


class _H3cDot11sMeshMPLinkStatus_Type(Integer32):
    """Custom type h3cDot11sMeshMPLinkStatus based on Integer32"""
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


_H3cDot11sMeshMPLinkStatus_Type.__name__ = "Integer32"
_H3cDot11sMeshMPLinkStatus_Object = MibTableColumn
h3cDot11sMeshMPLinkStatus = _H3cDot11sMeshMPLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 3, 3, 1, 8),
    _H3cDot11sMeshMPLinkStatus_Type()
)
h3cDot11sMeshMPLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11sMeshMPLinkStatus.setStatus("current")
_H3cDot11sMeshNbrChannel_Type = Unsigned32
_H3cDot11sMeshNbrChannel_Object = MibTableColumn
h3cDot11sMeshNbrChannel = _H3cDot11sMeshNbrChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 3, 3, 1, 9),
    _H3cDot11sMeshNbrChannel_Type()
)
h3cDot11sMeshNbrChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11sMeshNbrChannel.setStatus("current")
_H3cDot11sMeshNbrLinkDuration_Type = Integer32
_H3cDot11sMeshNbrLinkDuration_Object = MibTableColumn
h3cDot11sMeshNbrLinkDuration = _H3cDot11sMeshNbrLinkDuration_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 3, 3, 1, 10),
    _H3cDot11sMeshNbrLinkDuration_Type()
)
h3cDot11sMeshNbrLinkDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11sMeshNbrLinkDuration.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11sMeshNbrLinkDuration.setUnits("second")
_H3cDot11sMeshNbrRSSI_Type = Integer32
_H3cDot11sMeshNbrRSSI_Object = MibTableColumn
h3cDot11sMeshNbrRSSI = _H3cDot11sMeshNbrRSSI_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 3, 3, 1, 11),
    _H3cDot11sMeshNbrRSSI_Type()
)
h3cDot11sMeshNbrRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11sMeshNbrRSSI.setStatus("current")
_H3cDot11sMeshNbrSNR_Type = Integer32
_H3cDot11sMeshNbrSNR_Object = MibTableColumn
h3cDot11sMeshNbrSNR = _H3cDot11sMeshNbrSNR_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 11, 3, 3, 1, 12),
    _H3cDot11sMeshNbrSNR_Type()
)
h3cDot11sMeshNbrSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11sMeshNbrSNR.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11sMeshNbrSNR.setUnits("percent")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-DOT11S-MESH-MIB",
    **{"h3cDot11sMesh": h3cDot11sMesh,
       "h3cDot11sConfigGroup": h3cDot11sConfigGroup,
       "h3cDot11sMeshGlobalPara": h3cDot11sMeshGlobalPara,
       "h3cDot11sMeshMkdID": h3cDot11sMeshMkdID,
       "h3cDot11sMeshPflTable": h3cDot11sMeshPflTable,
       "h3cDot11sMeshPflEntry": h3cDot11sMeshPflEntry,
       "h3cDot11sMeshPflIndex": h3cDot11sMeshPflIndex,
       "h3cDot11sMeshPflMeshID": h3cDot11sMeshPflMeshID,
       "h3cDot11sMeshPflBindIntNum": h3cDot11sMeshPflBindIntNum,
       "h3cDot11sMeshPflKeepAlive": h3cDot11sMeshPflKeepAlive,
       "h3cDot11sMeshPflBackhaulRate": h3cDot11sMeshPflBackhaulRate,
       "h3cDot11sMeshMkdServEnable": h3cDot11sMeshMkdServEnable,
       "h3cDot11sMeshPflEnable": h3cDot11sMeshPflEnable,
       "h3cDot11sMeshPflRowStatus": h3cDot11sMeshPflRowStatus,
       "h3cDot11sMpPlcyTable": h3cDot11sMpPlcyTable,
       "h3cDot11sMpPlcyEntry": h3cDot11sMpPlcyEntry,
       "h3cDot11sMpPlcyIndex": h3cDot11sMpPlcyIndex,
       "h3cDot11sMpPlcyName": h3cDot11sMpPlcyName,
       "h3cDot11sMpPlcyInitEnable": h3cDot11sMpPlcyInitEnable,
       "h3cDot11sMlspEnable": h3cDot11sMlspEnable,
       "h3cDot11sProbReqInterval": h3cDot11sProbReqInterval,
       "h3cDot11sRoleAuthEnable": h3cDot11sRoleAuthEnable,
       "h3cDot11sLinkHoldRSSI": h3cDot11sLinkHoldRSSI,
       "h3cDot11sLinkHoldTime": h3cDot11sLinkHoldTime,
       "h3cDot11sSwitchMargin": h3cDot11sSwitchMargin,
       "h3cDot11sLinkSaturationRSSI": h3cDot11sLinkSaturationRSSI,
       "h3cDot11sLinkRateMode": h3cDot11sLinkRateMode,
       "h3cDot11sMaxLinkNum": h3cDot11sMaxLinkNum,
       "h3cDot11sMpPlcyRowStatus": h3cDot11sMpPlcyRowStatus,
       "h3cDot11sMlspCfgTable": h3cDot11sMlspCfgTable,
       "h3cDot11sMlspCfgEntry": h3cDot11sMlspCfgEntry,
       "h3cDot11sMlspProxyIndex": h3cDot11sMlspProxyIndex,
       "h3cDot11sMlspProxyMac": h3cDot11sMlspProxyMac,
       "h3cDot11sMlspRowStatus": h3cDot11sMlspRowStatus,
       "h3cDot11sRadioCfgTable": h3cDot11sRadioCfgTable,
       "h3cDot11sRadioCfgEntry": h3cDot11sRadioCfgEntry,
       "h3cDot11sCfgRadioIndex": h3cDot11sCfgRadioIndex,
       "h3cDot11sMeshPflMap": h3cDot11sMeshPflMap,
       "h3cDot11sMpPlcyMap": h3cDot11sMpPlcyMap,
       "h3cDot11sAPCfgTable": h3cDot11sAPCfgTable,
       "h3cDot11sAPCfgEntry": h3cDot11sAPCfgEntry,
       "h3cDot11sPortalEnable": h3cDot11sPortalEnable,
       "h3cDot11sWDSConfigGroup": h3cDot11sWDSConfigGroup,
       "h3cDot11sWDSPeerMacTable": h3cDot11sWDSPeerMacTable,
       "h3cDot11sWDSPeerMacEntry": h3cDot11sWDSPeerMacEntry,
       "h3cDot11sWDSPeerMacIndex": h3cDot11sWDSPeerMacIndex,
       "h3cDot11sWDSPeerMacAddrss": h3cDot11sWDSPeerMacAddrss,
       "h3cDot11sWDSPeerMacRowStatus": h3cDot11sWDSPeerMacRowStatus,
       "h3cDot11sMeshStatusGroup": h3cDot11sMeshStatusGroup,
       "h3cDot11sMeshLinkStatusTable": h3cDot11sMeshLinkStatusTable,
       "h3cDot11sMeshLinkStatusEntry": h3cDot11sMeshLinkStatusEntry,
       "h3cDot11sMeshLinkIfIndex": h3cDot11sMeshLinkIfIndex,
       "h3cDot11sMeshLinkName": h3cDot11sMeshLinkName,
       "h3cDot11sMeshLinkBSSID": h3cDot11sMeshLinkBSSID,
       "h3cDot11sMeshLinkPeerMac": h3cDot11sMeshLinkPeerMac,
       "h3cDot11sMeshLinkExistDuration": h3cDot11sMeshLinkExistDuration,
       "h3cDot11sMeshLinkStatisTable": h3cDot11sMeshLinkStatisTable,
       "h3cDot11sMeshLinkStatisEntry": h3cDot11sMeshLinkStatisEntry,
       "h3cDot11sMeshLinkStatIfIndex": h3cDot11sMeshLinkStatIfIndex,
       "h3cDot11sMeshLinkNbrIndex": h3cDot11sMeshLinkNbrIndex,
       "h3cDot11sMeshLinkRxTotByte": h3cDot11sMeshLinkRxTotByte,
       "h3cDot11sMeshLinkRxTotPkt": h3cDot11sMeshLinkRxTotPkt,
       "h3cDot11sMeshLinkRxUniPkt": h3cDot11sMeshLinkRxUniPkt,
       "h3cDot11sMeshLinkRxBrocPkt": h3cDot11sMeshLinkRxBrocPkt,
       "h3cDot11sMeshLinkRxMuticPkt": h3cDot11sMeshLinkRxMuticPkt,
       "h3cDot11sMeshLinkRxDiscPkt": h3cDot11sMeshLinkRxDiscPkt,
       "h3cDot11sMeshLinkTxTotByte": h3cDot11sMeshLinkTxTotByte,
       "h3cDot11sMeshLinkTxTotPkt": h3cDot11sMeshLinkTxTotPkt,
       "h3cDot11sMeshLinkTxUniPkt": h3cDot11sMeshLinkTxUniPkt,
       "h3cDot11sMeshLinkTxBrocPkt": h3cDot11sMeshLinkTxBrocPkt,
       "h3cDot11sMeshLinkTxMuticPkt": h3cDot11sMeshLinkTxMuticPkt,
       "h3cDot11sMeshLinkTxDiscPkt": h3cDot11sMeshLinkTxDiscPkt,
       "h3cDot11sMeshLinkIFName": h3cDot11sMeshLinkIFName,
       "h3cDot11sMeshNbrStatusTable": h3cDot11sMeshNbrStatusTable,
       "h3cDot11sMeshNbrStatusEntry": h3cDot11sMeshNbrStatusEntry,
       "h3cDot11sMeshNbrIndex": h3cDot11sMeshNbrIndex,
       "h3cDot11sMeshNbrRadioID": h3cDot11sMeshNbrRadioID,
       "h3cDot11sMeshLocalMeshID": h3cDot11sMeshLocalMeshID,
       "h3cDot11sMeshNbrMeshID": h3cDot11sMeshNbrMeshID,
       "h3cDot11sMeshNbrBSSID": h3cDot11sMeshNbrBSSID,
       "h3cDot11sMeshNbrPeerMac": h3cDot11sMeshNbrPeerMac,
       "h3cDot11sMeshLinkInMp": h3cDot11sMeshLinkInMp,
       "h3cDot11sMeshMPLinkStatus": h3cDot11sMeshMPLinkStatus,
       "h3cDot11sMeshNbrChannel": h3cDot11sMeshNbrChannel,
       "h3cDot11sMeshNbrLinkDuration": h3cDot11sMeshNbrLinkDuration,
       "h3cDot11sMeshNbrRSSI": h3cDot11sMeshNbrRSSI,
       "h3cDot11sMeshNbrSNR": h3cDot11sMeshNbrSNR}
)
