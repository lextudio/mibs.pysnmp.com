# SNMP MIB module (HPN-ICF-DOT11S-MESH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-DOT11S-MESH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:57 2024
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

(HpnicfDot11RadioElementIndex,
 hpnicfDot11,
 hpnicfDot11APElementIndex) = mibBuilder.importSymbols(
    "HPN-ICF-DOT11-REF-MIB",
    "HpnicfDot11RadioElementIndex",
    "hpnicfDot11",
    "hpnicfDot11APElementIndex")

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

hpnicfDot11sMesh = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11)
)
hpnicfDot11sMesh.setRevisions(
        ("2009-08-01 10:00",
         "2008-11-07 10:00",
         "2008-07-08 18:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfDot11sConfigGroup_ObjectIdentity = ObjectIdentity
hpnicfDot11sConfigGroup = _HpnicfDot11sConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 1)
)
_HpnicfDot11sMeshGlobalPara_ObjectIdentity = ObjectIdentity
hpnicfDot11sMeshGlobalPara = _HpnicfDot11sMeshGlobalPara_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 1, 1)
)
_HpnicfDot11sMeshMkdID_Type = MacAddress
_HpnicfDot11sMeshMkdID_Object = MibScalar
hpnicfDot11sMeshMkdID = _HpnicfDot11sMeshMkdID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 1, 1, 1),
    _HpnicfDot11sMeshMkdID_Type()
)
hpnicfDot11sMeshMkdID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11sMeshMkdID.setStatus("current")
_HpnicfDot11sMeshPflTable_Object = MibTable
hpnicfDot11sMeshPflTable = _HpnicfDot11sMeshPflTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfDot11sMeshPflTable.setStatus("current")
_HpnicfDot11sMeshPflEntry_Object = MibTableRow
hpnicfDot11sMeshPflEntry = _HpnicfDot11sMeshPflEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 1, 2, 1)
)
hpnicfDot11sMeshPflEntry.setIndexNames(
    (0, "HPN-ICF-DOT11S-MESH-MIB", "hpnicfDot11sMeshPflIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDot11sMeshPflEntry.setStatus("current")
_HpnicfDot11sMeshPflIndex_Type = Integer32
_HpnicfDot11sMeshPflIndex_Object = MibTableColumn
hpnicfDot11sMeshPflIndex = _HpnicfDot11sMeshPflIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 1, 2, 1, 1),
    _HpnicfDot11sMeshPflIndex_Type()
)
hpnicfDot11sMeshPflIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11sMeshPflIndex.setStatus("current")


class _HpnicfDot11sMeshPflMeshID_Type(OctetString):
    """Custom type hpnicfDot11sMeshPflMeshID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfDot11sMeshPflMeshID_Type.__name__ = "OctetString"
_HpnicfDot11sMeshPflMeshID_Object = MibTableColumn
hpnicfDot11sMeshPflMeshID = _HpnicfDot11sMeshPflMeshID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 1, 2, 1, 2),
    _HpnicfDot11sMeshPflMeshID_Type()
)
hpnicfDot11sMeshPflMeshID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11sMeshPflMeshID.setStatus("current")


class _HpnicfDot11sMeshPflBindIntNum_Type(Integer32):
    """Custom type hpnicfDot11sMeshPflBindIntNum based on Integer32"""
    defaultValue = -1


_HpnicfDot11sMeshPflBindIntNum_Object = MibTableColumn
hpnicfDot11sMeshPflBindIntNum = _HpnicfDot11sMeshPflBindIntNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 1, 2, 1, 3),
    _HpnicfDot11sMeshPflBindIntNum_Type()
)
hpnicfDot11sMeshPflBindIntNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11sMeshPflBindIntNum.setStatus("current")


class _HpnicfDot11sMeshPflKeepAlive_Type(Integer32):
    """Custom type hpnicfDot11sMeshPflKeepAlive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )


_HpnicfDot11sMeshPflKeepAlive_Type.__name__ = "Integer32"
_HpnicfDot11sMeshPflKeepAlive_Object = MibTableColumn
hpnicfDot11sMeshPflKeepAlive = _HpnicfDot11sMeshPflKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 1, 2, 1, 4),
    _HpnicfDot11sMeshPflKeepAlive_Type()
)
hpnicfDot11sMeshPflKeepAlive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11sMeshPflKeepAlive.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11sMeshPflKeepAlive.setUnits("second")
_HpnicfDot11sMeshPflBackhaulRate_Type = Integer32
_HpnicfDot11sMeshPflBackhaulRate_Object = MibTableColumn
hpnicfDot11sMeshPflBackhaulRate = _HpnicfDot11sMeshPflBackhaulRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 1, 2, 1, 5),
    _HpnicfDot11sMeshPflBackhaulRate_Type()
)
hpnicfDot11sMeshPflBackhaulRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11sMeshPflBackhaulRate.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11sMeshPflBackhaulRate.setUnits("Kbps")


class _HpnicfDot11sMeshMkdServEnable_Type(TruthValue):
    """Custom type hpnicfDot11sMeshMkdServEnable based on TruthValue"""


_HpnicfDot11sMeshMkdServEnable_Object = MibTableColumn
hpnicfDot11sMeshMkdServEnable = _HpnicfDot11sMeshMkdServEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 1, 2, 1, 6),
    _HpnicfDot11sMeshMkdServEnable_Type()
)
hpnicfDot11sMeshMkdServEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11sMeshMkdServEnable.setStatus("current")


class _HpnicfDot11sMeshPflEnable_Type(TruthValue):
    """Custom type hpnicfDot11sMeshPflEnable based on TruthValue"""


_HpnicfDot11sMeshPflEnable_Object = MibTableColumn
hpnicfDot11sMeshPflEnable = _HpnicfDot11sMeshPflEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 1, 2, 1, 7),
    _HpnicfDot11sMeshPflEnable_Type()
)
hpnicfDot11sMeshPflEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11sMeshPflEnable.setStatus("current")
_HpnicfDot11sMeshPflRowStatus_Type = RowStatus
_HpnicfDot11sMeshPflRowStatus_Object = MibTableColumn
hpnicfDot11sMeshPflRowStatus = _HpnicfDot11sMeshPflRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 1, 2, 1, 8),
    _HpnicfDot11sMeshPflRowStatus_Type()
)
hpnicfDot11sMeshPflRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11sMeshPflRowStatus.setStatus("current")
_HpnicfDot11sMpPlcyTable_Object = MibTable
hpnicfDot11sMpPlcyTable = _HpnicfDot11sMpPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfDot11sMpPlcyTable.setStatus("current")
_HpnicfDot11sMpPlcyEntry_Object = MibTableRow
hpnicfDot11sMpPlcyEntry = _HpnicfDot11sMpPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 1, 3, 1)
)
hpnicfDot11sMpPlcyEntry.setIndexNames(
    (0, "HPN-ICF-DOT11S-MESH-MIB", "hpnicfDot11sMpPlcyIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDot11sMpPlcyEntry.setStatus("current")
_HpnicfDot11sMpPlcyIndex_Type = Integer32
_HpnicfDot11sMpPlcyIndex_Object = MibTableColumn
hpnicfDot11sMpPlcyIndex = _HpnicfDot11sMpPlcyIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 1, 3, 1, 1),
    _HpnicfDot11sMpPlcyIndex_Type()
)
hpnicfDot11sMpPlcyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11sMpPlcyIndex.setStatus("current")


class _HpnicfDot11sMpPlcyName_Type(OctetString):
    """Custom type hpnicfDot11sMpPlcyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_HpnicfDot11sMpPlcyName_Type.__name__ = "OctetString"
_HpnicfDot11sMpPlcyName_Object = MibTableColumn
hpnicfDot11sMpPlcyName = _HpnicfDot11sMpPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 1, 3, 1, 2),
    _HpnicfDot11sMpPlcyName_Type()
)
hpnicfDot11sMpPlcyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11sMpPlcyName.setStatus("current")


class _HpnicfDot11sMpPlcyInitEnable_Type(TruthValue):
    """Custom type hpnicfDot11sMpPlcyInitEnable based on TruthValue"""


_HpnicfDot11sMpPlcyInitEnable_Object = MibTableColumn
hpnicfDot11sMpPlcyInitEnable = _HpnicfDot11sMpPlcyInitEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 1, 3, 1, 3),
    _HpnicfDot11sMpPlcyInitEnable_Type()
)
hpnicfDot11sMpPlcyInitEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11sMpPlcyInitEnable.setStatus("current")


class _HpnicfDot11sMlspEnable_Type(TruthValue):
    """Custom type hpnicfDot11sMlspEnable based on TruthValue"""


_HpnicfDot11sMlspEnable_Object = MibTableColumn
hpnicfDot11sMlspEnable = _HpnicfDot11sMlspEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 1, 3, 1, 4),
    _HpnicfDot11sMlspEnable_Type()
)
hpnicfDot11sMlspEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11sMlspEnable.setStatus("current")
_HpnicfDot11sProbReqInterval_Type = Integer32
_HpnicfDot11sProbReqInterval_Object = MibTableColumn
hpnicfDot11sProbReqInterval = _HpnicfDot11sProbReqInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 1, 3, 1, 5),
    _HpnicfDot11sProbReqInterval_Type()
)
hpnicfDot11sProbReqInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11sProbReqInterval.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11sProbReqInterval.setUnits("millisecond")


class _HpnicfDot11sRoleAuthEnable_Type(TruthValue):
    """Custom type hpnicfDot11sRoleAuthEnable based on TruthValue"""


_HpnicfDot11sRoleAuthEnable_Object = MibTableColumn
hpnicfDot11sRoleAuthEnable = _HpnicfDot11sRoleAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 1, 3, 1, 6),
    _HpnicfDot11sRoleAuthEnable_Type()
)
hpnicfDot11sRoleAuthEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11sRoleAuthEnable.setStatus("current")


class _HpnicfDot11sLinkHoldRSSI_Type(Integer32):
    """Custom type hpnicfDot11sLinkHoldRSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 100),
    )


_HpnicfDot11sLinkHoldRSSI_Type.__name__ = "Integer32"
_HpnicfDot11sLinkHoldRSSI_Object = MibTableColumn
hpnicfDot11sLinkHoldRSSI = _HpnicfDot11sLinkHoldRSSI_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 1, 3, 1, 7),
    _HpnicfDot11sLinkHoldRSSI_Type()
)
hpnicfDot11sLinkHoldRSSI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11sLinkHoldRSSI.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11sLinkHoldRSSI.setUnits("dBm")


class _HpnicfDot11sLinkHoldTime_Type(Integer32):
    """Custom type hpnicfDot11sLinkHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 20000),
    )


_HpnicfDot11sLinkHoldTime_Type.__name__ = "Integer32"
_HpnicfDot11sLinkHoldTime_Object = MibTableColumn
hpnicfDot11sLinkHoldTime = _HpnicfDot11sLinkHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 1, 3, 1, 8),
    _HpnicfDot11sLinkHoldTime_Type()
)
hpnicfDot11sLinkHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11sLinkHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11sLinkHoldTime.setUnits("millisecond")


class _HpnicfDot11sSwitchMargin_Type(Integer32):
    """Custom type hpnicfDot11sSwitchMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HpnicfDot11sSwitchMargin_Type.__name__ = "Integer32"
_HpnicfDot11sSwitchMargin_Object = MibTableColumn
hpnicfDot11sSwitchMargin = _HpnicfDot11sSwitchMargin_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 1, 3, 1, 9),
    _HpnicfDot11sSwitchMargin_Type()
)
hpnicfDot11sSwitchMargin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11sSwitchMargin.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11sSwitchMargin.setUnits("dBm")


class _HpnicfDot11sLinkSaturationRSSI_Type(Integer32):
    """Custom type hpnicfDot11sLinkSaturationRSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 150),
    )


_HpnicfDot11sLinkSaturationRSSI_Type.__name__ = "Integer32"
_HpnicfDot11sLinkSaturationRSSI_Object = MibTableColumn
hpnicfDot11sLinkSaturationRSSI = _HpnicfDot11sLinkSaturationRSSI_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 1, 3, 1, 10),
    _HpnicfDot11sLinkSaturationRSSI_Type()
)
hpnicfDot11sLinkSaturationRSSI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11sLinkSaturationRSSI.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11sLinkSaturationRSSI.setUnits("dBm")


class _HpnicfDot11sLinkRateMode_Type(Integer32):
    """Custom type hpnicfDot11sLinkRateMode based on Integer32"""
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


_HpnicfDot11sLinkRateMode_Type.__name__ = "Integer32"
_HpnicfDot11sLinkRateMode_Object = MibTableColumn
hpnicfDot11sLinkRateMode = _HpnicfDot11sLinkRateMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 1, 3, 1, 11),
    _HpnicfDot11sLinkRateMode_Type()
)
hpnicfDot11sLinkRateMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11sLinkRateMode.setStatus("current")
_HpnicfDot11sMaxLinkNum_Type = Integer32
_HpnicfDot11sMaxLinkNum_Object = MibTableColumn
hpnicfDot11sMaxLinkNum = _HpnicfDot11sMaxLinkNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 1, 3, 1, 12),
    _HpnicfDot11sMaxLinkNum_Type()
)
hpnicfDot11sMaxLinkNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11sMaxLinkNum.setStatus("current")
_HpnicfDot11sMpPlcyRowStatus_Type = RowStatus
_HpnicfDot11sMpPlcyRowStatus_Object = MibTableColumn
hpnicfDot11sMpPlcyRowStatus = _HpnicfDot11sMpPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 1, 3, 1, 13),
    _HpnicfDot11sMpPlcyRowStatus_Type()
)
hpnicfDot11sMpPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11sMpPlcyRowStatus.setStatus("current")
_HpnicfDot11sMlspCfgTable_Object = MibTable
hpnicfDot11sMlspCfgTable = _HpnicfDot11sMlspCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 1, 4)
)
if mibBuilder.loadTexts:
    hpnicfDot11sMlspCfgTable.setStatus("current")
_HpnicfDot11sMlspCfgEntry_Object = MibTableRow
hpnicfDot11sMlspCfgEntry = _HpnicfDot11sMlspCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 1, 4, 1)
)
hpnicfDot11sMlspCfgEntry.setIndexNames(
    (0, "HPN-ICF-DOT11S-MESH-MIB", "hpnicfDot11sMpPlcyIndex"),
    (0, "HPN-ICF-DOT11S-MESH-MIB", "hpnicfDot11sMlspProxyIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDot11sMlspCfgEntry.setStatus("current")
_HpnicfDot11sMlspProxyIndex_Type = Integer32
_HpnicfDot11sMlspProxyIndex_Object = MibTableColumn
hpnicfDot11sMlspProxyIndex = _HpnicfDot11sMlspProxyIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 1, 4, 1, 1),
    _HpnicfDot11sMlspProxyIndex_Type()
)
hpnicfDot11sMlspProxyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11sMlspProxyIndex.setStatus("current")
_HpnicfDot11sMlspProxyMac_Type = MacAddress
_HpnicfDot11sMlspProxyMac_Object = MibTableColumn
hpnicfDot11sMlspProxyMac = _HpnicfDot11sMlspProxyMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 1, 4, 1, 2),
    _HpnicfDot11sMlspProxyMac_Type()
)
hpnicfDot11sMlspProxyMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11sMlspProxyMac.setStatus("current")
_HpnicfDot11sMlspRowStatus_Type = RowStatus
_HpnicfDot11sMlspRowStatus_Object = MibTableColumn
hpnicfDot11sMlspRowStatus = _HpnicfDot11sMlspRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 1, 4, 1, 3),
    _HpnicfDot11sMlspRowStatus_Type()
)
hpnicfDot11sMlspRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11sMlspRowStatus.setStatus("current")
_HpnicfDot11sRadioCfgTable_Object = MibTable
hpnicfDot11sRadioCfgTable = _HpnicfDot11sRadioCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 1, 5)
)
if mibBuilder.loadTexts:
    hpnicfDot11sRadioCfgTable.setStatus("current")
_HpnicfDot11sRadioCfgEntry_Object = MibTableRow
hpnicfDot11sRadioCfgEntry = _HpnicfDot11sRadioCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 1, 5, 1)
)
hpnicfDot11sRadioCfgEntry.setIndexNames(
    (0, "HPN-ICF-DOT11S-MESH-MIB", "hpnicfDot11sCfgRadioIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDot11sRadioCfgEntry.setStatus("current")
_HpnicfDot11sCfgRadioIndex_Type = HpnicfDot11RadioElementIndex
_HpnicfDot11sCfgRadioIndex_Object = MibTableColumn
hpnicfDot11sCfgRadioIndex = _HpnicfDot11sCfgRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 1, 5, 1, 1),
    _HpnicfDot11sCfgRadioIndex_Type()
)
hpnicfDot11sCfgRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11sCfgRadioIndex.setStatus("current")


class _HpnicfDot11sMeshPflMap_Type(Integer32):
    """Custom type hpnicfDot11sMeshPflMap based on Integer32"""
    defaultValue = 0


_HpnicfDot11sMeshPflMap_Object = MibTableColumn
hpnicfDot11sMeshPflMap = _HpnicfDot11sMeshPflMap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 1, 5, 1, 2),
    _HpnicfDot11sMeshPflMap_Type()
)
hpnicfDot11sMeshPflMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11sMeshPflMap.setStatus("current")


class _HpnicfDot11sMpPlcyMap_Type(Integer32):
    """Custom type hpnicfDot11sMpPlcyMap based on Integer32"""
    defaultValue = 1


_HpnicfDot11sMpPlcyMap_Object = MibTableColumn
hpnicfDot11sMpPlcyMap = _HpnicfDot11sMpPlcyMap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 1, 5, 1, 3),
    _HpnicfDot11sMpPlcyMap_Type()
)
hpnicfDot11sMpPlcyMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11sMpPlcyMap.setStatus("current")
_HpnicfDot11sAPCfgTable_Object = MibTable
hpnicfDot11sAPCfgTable = _HpnicfDot11sAPCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 1, 6)
)
if mibBuilder.loadTexts:
    hpnicfDot11sAPCfgTable.setStatus("current")
_HpnicfDot11sAPCfgEntry_Object = MibTableRow
hpnicfDot11sAPCfgEntry = _HpnicfDot11sAPCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 1, 6, 1)
)
hpnicfDot11sAPCfgEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-REF-MIB", "hpnicfDot11APElementIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDot11sAPCfgEntry.setStatus("current")


class _HpnicfDot11sPortalEnable_Type(TruthValue):
    """Custom type hpnicfDot11sPortalEnable based on TruthValue"""


_HpnicfDot11sPortalEnable_Object = MibTableColumn
hpnicfDot11sPortalEnable = _HpnicfDot11sPortalEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 1, 6, 1, 1),
    _HpnicfDot11sPortalEnable_Type()
)
hpnicfDot11sPortalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11sPortalEnable.setStatus("current")
_HpnicfDot11sWDSConfigGroup_ObjectIdentity = ObjectIdentity
hpnicfDot11sWDSConfigGroup = _HpnicfDot11sWDSConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 2)
)
_HpnicfDot11sWDSPeerMacTable_Object = MibTable
hpnicfDot11sWDSPeerMacTable = _HpnicfDot11sWDSPeerMacTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfDot11sWDSPeerMacTable.setStatus("current")
_HpnicfDot11sWDSPeerMacEntry_Object = MibTableRow
hpnicfDot11sWDSPeerMacEntry = _HpnicfDot11sWDSPeerMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 2, 1, 1)
)
hpnicfDot11sWDSPeerMacEntry.setIndexNames(
    (0, "HPN-ICF-DOT11S-MESH-MIB", "hpnicfDot11sCfgRadioIndex"),
    (0, "HPN-ICF-DOT11S-MESH-MIB", "hpnicfDot11sWDSPeerMacIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDot11sWDSPeerMacEntry.setStatus("current")
_HpnicfDot11sWDSPeerMacIndex_Type = Integer32
_HpnicfDot11sWDSPeerMacIndex_Object = MibTableColumn
hpnicfDot11sWDSPeerMacIndex = _HpnicfDot11sWDSPeerMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 2, 1, 1, 1),
    _HpnicfDot11sWDSPeerMacIndex_Type()
)
hpnicfDot11sWDSPeerMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11sWDSPeerMacIndex.setStatus("current")
_HpnicfDot11sWDSPeerMacAddrss_Type = MacAddress
_HpnicfDot11sWDSPeerMacAddrss_Object = MibTableColumn
hpnicfDot11sWDSPeerMacAddrss = _HpnicfDot11sWDSPeerMacAddrss_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 2, 1, 1, 2),
    _HpnicfDot11sWDSPeerMacAddrss_Type()
)
hpnicfDot11sWDSPeerMacAddrss.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11sWDSPeerMacAddrss.setStatus("current")
_HpnicfDot11sWDSPeerMacRowStatus_Type = RowStatus
_HpnicfDot11sWDSPeerMacRowStatus_Object = MibTableColumn
hpnicfDot11sWDSPeerMacRowStatus = _HpnicfDot11sWDSPeerMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 2, 1, 1, 3),
    _HpnicfDot11sWDSPeerMacRowStatus_Type()
)
hpnicfDot11sWDSPeerMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11sWDSPeerMacRowStatus.setStatus("current")
_HpnicfDot11sMeshStatusGroup_ObjectIdentity = ObjectIdentity
hpnicfDot11sMeshStatusGroup = _HpnicfDot11sMeshStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 3)
)
_HpnicfDot11sMeshLinkStatusTable_Object = MibTable
hpnicfDot11sMeshLinkStatusTable = _HpnicfDot11sMeshLinkStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 3, 1)
)
if mibBuilder.loadTexts:
    hpnicfDot11sMeshLinkStatusTable.setStatus("current")
_HpnicfDot11sMeshLinkStatusEntry_Object = MibTableRow
hpnicfDot11sMeshLinkStatusEntry = _HpnicfDot11sMeshLinkStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 3, 1, 1)
)
hpnicfDot11sMeshLinkStatusEntry.setIndexNames(
    (0, "HPN-ICF-DOT11S-MESH-MIB", "hpnicfDot11sMeshLinkIfIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDot11sMeshLinkStatusEntry.setStatus("current")
_HpnicfDot11sMeshLinkIfIndex_Type = Unsigned32
_HpnicfDot11sMeshLinkIfIndex_Object = MibTableColumn
hpnicfDot11sMeshLinkIfIndex = _HpnicfDot11sMeshLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 3, 1, 1, 1),
    _HpnicfDot11sMeshLinkIfIndex_Type()
)
hpnicfDot11sMeshLinkIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11sMeshLinkIfIndex.setStatus("current")
_HpnicfDot11sMeshLinkName_Type = OctetString
_HpnicfDot11sMeshLinkName_Object = MibTableColumn
hpnicfDot11sMeshLinkName = _HpnicfDot11sMeshLinkName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 3, 1, 1, 2),
    _HpnicfDot11sMeshLinkName_Type()
)
hpnicfDot11sMeshLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11sMeshLinkName.setStatus("current")
_HpnicfDot11sMeshLinkBSSID_Type = MacAddress
_HpnicfDot11sMeshLinkBSSID_Object = MibTableColumn
hpnicfDot11sMeshLinkBSSID = _HpnicfDot11sMeshLinkBSSID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 3, 1, 1, 3),
    _HpnicfDot11sMeshLinkBSSID_Type()
)
hpnicfDot11sMeshLinkBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11sMeshLinkBSSID.setStatus("current")
_HpnicfDot11sMeshLinkPeerMac_Type = MacAddress
_HpnicfDot11sMeshLinkPeerMac_Object = MibTableColumn
hpnicfDot11sMeshLinkPeerMac = _HpnicfDot11sMeshLinkPeerMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 3, 1, 1, 4),
    _HpnicfDot11sMeshLinkPeerMac_Type()
)
hpnicfDot11sMeshLinkPeerMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11sMeshLinkPeerMac.setStatus("current")
_HpnicfDot11sMeshLinkExistDuration_Type = Integer32
_HpnicfDot11sMeshLinkExistDuration_Object = MibTableColumn
hpnicfDot11sMeshLinkExistDuration = _HpnicfDot11sMeshLinkExistDuration_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 3, 1, 1, 5),
    _HpnicfDot11sMeshLinkExistDuration_Type()
)
hpnicfDot11sMeshLinkExistDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11sMeshLinkExistDuration.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11sMeshLinkExistDuration.setUnits("second")


class _HpnicfDot11sMeshLinkType_Type(Integer32):
    """Custom type hpnicfDot11sMeshLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("dormant", 2))
    )


_HpnicfDot11sMeshLinkType_Type.__name__ = "Integer32"
_HpnicfDot11sMeshLinkType_Object = MibTableColumn
hpnicfDot11sMeshLinkType = _HpnicfDot11sMeshLinkType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 3, 1, 1, 6),
    _HpnicfDot11sMeshLinkType_Type()
)
hpnicfDot11sMeshLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11sMeshLinkType.setStatus("current")
_HpnicfDot11sMeshLinkStatisTable_Object = MibTable
hpnicfDot11sMeshLinkStatisTable = _HpnicfDot11sMeshLinkStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 3, 2)
)
if mibBuilder.loadTexts:
    hpnicfDot11sMeshLinkStatisTable.setStatus("current")
_HpnicfDot11sMeshLinkStatisEntry_Object = MibTableRow
hpnicfDot11sMeshLinkStatisEntry = _HpnicfDot11sMeshLinkStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 3, 2, 1)
)
hpnicfDot11sMeshLinkStatisEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-REF-MIB", "hpnicfDot11APElementIndex"),
    (0, "HPN-ICF-DOT11S-MESH-MIB", "hpnicfDot11sMeshLinkStatIfIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDot11sMeshLinkStatisEntry.setStatus("current")
_HpnicfDot11sMeshLinkStatIfIndex_Type = Unsigned32
_HpnicfDot11sMeshLinkStatIfIndex_Object = MibTableColumn
hpnicfDot11sMeshLinkStatIfIndex = _HpnicfDot11sMeshLinkStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 3, 2, 1, 1),
    _HpnicfDot11sMeshLinkStatIfIndex_Type()
)
hpnicfDot11sMeshLinkStatIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11sMeshLinkStatIfIndex.setStatus("current")
_HpnicfDot11sMeshLinkNbrIndex_Type = Unsigned32
_HpnicfDot11sMeshLinkNbrIndex_Object = MibTableColumn
hpnicfDot11sMeshLinkNbrIndex = _HpnicfDot11sMeshLinkNbrIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 3, 2, 1, 2),
    _HpnicfDot11sMeshLinkNbrIndex_Type()
)
hpnicfDot11sMeshLinkNbrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11sMeshLinkNbrIndex.setStatus("current")
_HpnicfDot11sMeshLinkRxTotByte_Type = Counter32
_HpnicfDot11sMeshLinkRxTotByte_Object = MibTableColumn
hpnicfDot11sMeshLinkRxTotByte = _HpnicfDot11sMeshLinkRxTotByte_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 3, 2, 1, 3),
    _HpnicfDot11sMeshLinkRxTotByte_Type()
)
hpnicfDot11sMeshLinkRxTotByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11sMeshLinkRxTotByte.setStatus("current")
_HpnicfDot11sMeshLinkRxTotPkt_Type = Counter32
_HpnicfDot11sMeshLinkRxTotPkt_Object = MibTableColumn
hpnicfDot11sMeshLinkRxTotPkt = _HpnicfDot11sMeshLinkRxTotPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 3, 2, 1, 4),
    _HpnicfDot11sMeshLinkRxTotPkt_Type()
)
hpnicfDot11sMeshLinkRxTotPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11sMeshLinkRxTotPkt.setStatus("current")
_HpnicfDot11sMeshLinkRxUniPkt_Type = Counter32
_HpnicfDot11sMeshLinkRxUniPkt_Object = MibTableColumn
hpnicfDot11sMeshLinkRxUniPkt = _HpnicfDot11sMeshLinkRxUniPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 3, 2, 1, 5),
    _HpnicfDot11sMeshLinkRxUniPkt_Type()
)
hpnicfDot11sMeshLinkRxUniPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11sMeshLinkRxUniPkt.setStatus("current")
_HpnicfDot11sMeshLinkRxBrocPkt_Type = Counter32
_HpnicfDot11sMeshLinkRxBrocPkt_Object = MibTableColumn
hpnicfDot11sMeshLinkRxBrocPkt = _HpnicfDot11sMeshLinkRxBrocPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 3, 2, 1, 6),
    _HpnicfDot11sMeshLinkRxBrocPkt_Type()
)
hpnicfDot11sMeshLinkRxBrocPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11sMeshLinkRxBrocPkt.setStatus("current")
_HpnicfDot11sMeshLinkRxMuticPkt_Type = Counter32
_HpnicfDot11sMeshLinkRxMuticPkt_Object = MibTableColumn
hpnicfDot11sMeshLinkRxMuticPkt = _HpnicfDot11sMeshLinkRxMuticPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 3, 2, 1, 7),
    _HpnicfDot11sMeshLinkRxMuticPkt_Type()
)
hpnicfDot11sMeshLinkRxMuticPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11sMeshLinkRxMuticPkt.setStatus("current")
_HpnicfDot11sMeshLinkRxDiscPkt_Type = Counter32
_HpnicfDot11sMeshLinkRxDiscPkt_Object = MibTableColumn
hpnicfDot11sMeshLinkRxDiscPkt = _HpnicfDot11sMeshLinkRxDiscPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 3, 2, 1, 8),
    _HpnicfDot11sMeshLinkRxDiscPkt_Type()
)
hpnicfDot11sMeshLinkRxDiscPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11sMeshLinkRxDiscPkt.setStatus("current")
_HpnicfDot11sMeshLinkTxTotByte_Type = Counter32
_HpnicfDot11sMeshLinkTxTotByte_Object = MibTableColumn
hpnicfDot11sMeshLinkTxTotByte = _HpnicfDot11sMeshLinkTxTotByte_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 3, 2, 1, 9),
    _HpnicfDot11sMeshLinkTxTotByte_Type()
)
hpnicfDot11sMeshLinkTxTotByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11sMeshLinkTxTotByte.setStatus("current")
_HpnicfDot11sMeshLinkTxTotPkt_Type = Counter32
_HpnicfDot11sMeshLinkTxTotPkt_Object = MibTableColumn
hpnicfDot11sMeshLinkTxTotPkt = _HpnicfDot11sMeshLinkTxTotPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 3, 2, 1, 10),
    _HpnicfDot11sMeshLinkTxTotPkt_Type()
)
hpnicfDot11sMeshLinkTxTotPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11sMeshLinkTxTotPkt.setStatus("current")
_HpnicfDot11sMeshLinkTxUniPkt_Type = Counter32
_HpnicfDot11sMeshLinkTxUniPkt_Object = MibTableColumn
hpnicfDot11sMeshLinkTxUniPkt = _HpnicfDot11sMeshLinkTxUniPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 3, 2, 1, 11),
    _HpnicfDot11sMeshLinkTxUniPkt_Type()
)
hpnicfDot11sMeshLinkTxUniPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11sMeshLinkTxUniPkt.setStatus("current")
_HpnicfDot11sMeshLinkTxBrocPkt_Type = Counter32
_HpnicfDot11sMeshLinkTxBrocPkt_Object = MibTableColumn
hpnicfDot11sMeshLinkTxBrocPkt = _HpnicfDot11sMeshLinkTxBrocPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 3, 2, 1, 12),
    _HpnicfDot11sMeshLinkTxBrocPkt_Type()
)
hpnicfDot11sMeshLinkTxBrocPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11sMeshLinkTxBrocPkt.setStatus("current")
_HpnicfDot11sMeshLinkTxMuticPkt_Type = Counter32
_HpnicfDot11sMeshLinkTxMuticPkt_Object = MibTableColumn
hpnicfDot11sMeshLinkTxMuticPkt = _HpnicfDot11sMeshLinkTxMuticPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 3, 2, 1, 13),
    _HpnicfDot11sMeshLinkTxMuticPkt_Type()
)
hpnicfDot11sMeshLinkTxMuticPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11sMeshLinkTxMuticPkt.setStatus("current")
_HpnicfDot11sMeshLinkTxDiscPkt_Type = Counter32
_HpnicfDot11sMeshLinkTxDiscPkt_Object = MibTableColumn
hpnicfDot11sMeshLinkTxDiscPkt = _HpnicfDot11sMeshLinkTxDiscPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 3, 2, 1, 14),
    _HpnicfDot11sMeshLinkTxDiscPkt_Type()
)
hpnicfDot11sMeshLinkTxDiscPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11sMeshLinkTxDiscPkt.setStatus("current")
_HpnicfDot11sMeshLinkIFName_Type = OctetString
_HpnicfDot11sMeshLinkIFName_Object = MibTableColumn
hpnicfDot11sMeshLinkIFName = _HpnicfDot11sMeshLinkIFName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 3, 2, 1, 15),
    _HpnicfDot11sMeshLinkIFName_Type()
)
hpnicfDot11sMeshLinkIFName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11sMeshLinkIFName.setStatus("current")
_HpnicfDot11sMeshNbrStatusTable_Object = MibTable
hpnicfDot11sMeshNbrStatusTable = _HpnicfDot11sMeshNbrStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 3, 3)
)
if mibBuilder.loadTexts:
    hpnicfDot11sMeshNbrStatusTable.setStatus("current")
_HpnicfDot11sMeshNbrStatusEntry_Object = MibTableRow
hpnicfDot11sMeshNbrStatusEntry = _HpnicfDot11sMeshNbrStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 3, 3, 1)
)
hpnicfDot11sMeshNbrStatusEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-REF-MIB", "hpnicfDot11APElementIndex"),
    (0, "HPN-ICF-DOT11S-MESH-MIB", "hpnicfDot11sMeshNbrIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDot11sMeshNbrStatusEntry.setStatus("current")
_HpnicfDot11sMeshNbrIndex_Type = Unsigned32
_HpnicfDot11sMeshNbrIndex_Object = MibTableColumn
hpnicfDot11sMeshNbrIndex = _HpnicfDot11sMeshNbrIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 3, 3, 1, 1),
    _HpnicfDot11sMeshNbrIndex_Type()
)
hpnicfDot11sMeshNbrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11sMeshNbrIndex.setStatus("current")
_HpnicfDot11sMeshNbrRadioID_Type = Unsigned32
_HpnicfDot11sMeshNbrRadioID_Object = MibTableColumn
hpnicfDot11sMeshNbrRadioID = _HpnicfDot11sMeshNbrRadioID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 3, 3, 1, 2),
    _HpnicfDot11sMeshNbrRadioID_Type()
)
hpnicfDot11sMeshNbrRadioID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11sMeshNbrRadioID.setStatus("current")


class _HpnicfDot11sMeshLocalMeshID_Type(OctetString):
    """Custom type hpnicfDot11sMeshLocalMeshID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfDot11sMeshLocalMeshID_Type.__name__ = "OctetString"
_HpnicfDot11sMeshLocalMeshID_Object = MibTableColumn
hpnicfDot11sMeshLocalMeshID = _HpnicfDot11sMeshLocalMeshID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 3, 3, 1, 3),
    _HpnicfDot11sMeshLocalMeshID_Type()
)
hpnicfDot11sMeshLocalMeshID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11sMeshLocalMeshID.setStatus("current")


class _HpnicfDot11sMeshNbrMeshID_Type(OctetString):
    """Custom type hpnicfDot11sMeshNbrMeshID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfDot11sMeshNbrMeshID_Type.__name__ = "OctetString"
_HpnicfDot11sMeshNbrMeshID_Object = MibTableColumn
hpnicfDot11sMeshNbrMeshID = _HpnicfDot11sMeshNbrMeshID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 3, 3, 1, 4),
    _HpnicfDot11sMeshNbrMeshID_Type()
)
hpnicfDot11sMeshNbrMeshID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11sMeshNbrMeshID.setStatus("current")
_HpnicfDot11sMeshNbrBSSID_Type = MacAddress
_HpnicfDot11sMeshNbrBSSID_Object = MibTableColumn
hpnicfDot11sMeshNbrBSSID = _HpnicfDot11sMeshNbrBSSID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 3, 3, 1, 5),
    _HpnicfDot11sMeshNbrBSSID_Type()
)
hpnicfDot11sMeshNbrBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11sMeshNbrBSSID.setStatus("current")
_HpnicfDot11sMeshNbrPeerMac_Type = MacAddress
_HpnicfDot11sMeshNbrPeerMac_Object = MibTableColumn
hpnicfDot11sMeshNbrPeerMac = _HpnicfDot11sMeshNbrPeerMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 3, 3, 1, 6),
    _HpnicfDot11sMeshNbrPeerMac_Type()
)
hpnicfDot11sMeshNbrPeerMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11sMeshNbrPeerMac.setStatus("current")
_HpnicfDot11sMeshLinkInMp_Type = Unsigned32
_HpnicfDot11sMeshLinkInMp_Object = MibTableColumn
hpnicfDot11sMeshLinkInMp = _HpnicfDot11sMeshLinkInMp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 3, 3, 1, 7),
    _HpnicfDot11sMeshLinkInMp_Type()
)
hpnicfDot11sMeshLinkInMp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11sMeshLinkInMp.setStatus("current")


class _HpnicfDot11sMeshMPLinkStatus_Type(Integer32):
    """Custom type hpnicfDot11sMeshMPLinkStatus based on Integer32"""
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


_HpnicfDot11sMeshMPLinkStatus_Type.__name__ = "Integer32"
_HpnicfDot11sMeshMPLinkStatus_Object = MibTableColumn
hpnicfDot11sMeshMPLinkStatus = _HpnicfDot11sMeshMPLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 3, 3, 1, 8),
    _HpnicfDot11sMeshMPLinkStatus_Type()
)
hpnicfDot11sMeshMPLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11sMeshMPLinkStatus.setStatus("current")
_HpnicfDot11sMeshNbrChannel_Type = Unsigned32
_HpnicfDot11sMeshNbrChannel_Object = MibTableColumn
hpnicfDot11sMeshNbrChannel = _HpnicfDot11sMeshNbrChannel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 3, 3, 1, 9),
    _HpnicfDot11sMeshNbrChannel_Type()
)
hpnicfDot11sMeshNbrChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11sMeshNbrChannel.setStatus("current")
_HpnicfDot11sMeshNbrLinkDuration_Type = Integer32
_HpnicfDot11sMeshNbrLinkDuration_Object = MibTableColumn
hpnicfDot11sMeshNbrLinkDuration = _HpnicfDot11sMeshNbrLinkDuration_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 3, 3, 1, 10),
    _HpnicfDot11sMeshNbrLinkDuration_Type()
)
hpnicfDot11sMeshNbrLinkDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11sMeshNbrLinkDuration.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11sMeshNbrLinkDuration.setUnits("second")
_HpnicfDot11sMeshNbrRSSI_Type = Integer32
_HpnicfDot11sMeshNbrRSSI_Object = MibTableColumn
hpnicfDot11sMeshNbrRSSI = _HpnicfDot11sMeshNbrRSSI_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 3, 3, 1, 11),
    _HpnicfDot11sMeshNbrRSSI_Type()
)
hpnicfDot11sMeshNbrRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11sMeshNbrRSSI.setStatus("current")
_HpnicfDot11sMeshNbrSNR_Type = Integer32
_HpnicfDot11sMeshNbrSNR_Object = MibTableColumn
hpnicfDot11sMeshNbrSNR = _HpnicfDot11sMeshNbrSNR_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 11, 3, 3, 1, 12),
    _HpnicfDot11sMeshNbrSNR_Type()
)
hpnicfDot11sMeshNbrSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11sMeshNbrSNR.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11sMeshNbrSNR.setUnits("percent")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-DOT11S-MESH-MIB",
    **{"hpnicfDot11sMesh": hpnicfDot11sMesh,
       "hpnicfDot11sConfigGroup": hpnicfDot11sConfigGroup,
       "hpnicfDot11sMeshGlobalPara": hpnicfDot11sMeshGlobalPara,
       "hpnicfDot11sMeshMkdID": hpnicfDot11sMeshMkdID,
       "hpnicfDot11sMeshPflTable": hpnicfDot11sMeshPflTable,
       "hpnicfDot11sMeshPflEntry": hpnicfDot11sMeshPflEntry,
       "hpnicfDot11sMeshPflIndex": hpnicfDot11sMeshPflIndex,
       "hpnicfDot11sMeshPflMeshID": hpnicfDot11sMeshPflMeshID,
       "hpnicfDot11sMeshPflBindIntNum": hpnicfDot11sMeshPflBindIntNum,
       "hpnicfDot11sMeshPflKeepAlive": hpnicfDot11sMeshPflKeepAlive,
       "hpnicfDot11sMeshPflBackhaulRate": hpnicfDot11sMeshPflBackhaulRate,
       "hpnicfDot11sMeshMkdServEnable": hpnicfDot11sMeshMkdServEnable,
       "hpnicfDot11sMeshPflEnable": hpnicfDot11sMeshPflEnable,
       "hpnicfDot11sMeshPflRowStatus": hpnicfDot11sMeshPflRowStatus,
       "hpnicfDot11sMpPlcyTable": hpnicfDot11sMpPlcyTable,
       "hpnicfDot11sMpPlcyEntry": hpnicfDot11sMpPlcyEntry,
       "hpnicfDot11sMpPlcyIndex": hpnicfDot11sMpPlcyIndex,
       "hpnicfDot11sMpPlcyName": hpnicfDot11sMpPlcyName,
       "hpnicfDot11sMpPlcyInitEnable": hpnicfDot11sMpPlcyInitEnable,
       "hpnicfDot11sMlspEnable": hpnicfDot11sMlspEnable,
       "hpnicfDot11sProbReqInterval": hpnicfDot11sProbReqInterval,
       "hpnicfDot11sRoleAuthEnable": hpnicfDot11sRoleAuthEnable,
       "hpnicfDot11sLinkHoldRSSI": hpnicfDot11sLinkHoldRSSI,
       "hpnicfDot11sLinkHoldTime": hpnicfDot11sLinkHoldTime,
       "hpnicfDot11sSwitchMargin": hpnicfDot11sSwitchMargin,
       "hpnicfDot11sLinkSaturationRSSI": hpnicfDot11sLinkSaturationRSSI,
       "hpnicfDot11sLinkRateMode": hpnicfDot11sLinkRateMode,
       "hpnicfDot11sMaxLinkNum": hpnicfDot11sMaxLinkNum,
       "hpnicfDot11sMpPlcyRowStatus": hpnicfDot11sMpPlcyRowStatus,
       "hpnicfDot11sMlspCfgTable": hpnicfDot11sMlspCfgTable,
       "hpnicfDot11sMlspCfgEntry": hpnicfDot11sMlspCfgEntry,
       "hpnicfDot11sMlspProxyIndex": hpnicfDot11sMlspProxyIndex,
       "hpnicfDot11sMlspProxyMac": hpnicfDot11sMlspProxyMac,
       "hpnicfDot11sMlspRowStatus": hpnicfDot11sMlspRowStatus,
       "hpnicfDot11sRadioCfgTable": hpnicfDot11sRadioCfgTable,
       "hpnicfDot11sRadioCfgEntry": hpnicfDot11sRadioCfgEntry,
       "hpnicfDot11sCfgRadioIndex": hpnicfDot11sCfgRadioIndex,
       "hpnicfDot11sMeshPflMap": hpnicfDot11sMeshPflMap,
       "hpnicfDot11sMpPlcyMap": hpnicfDot11sMpPlcyMap,
       "hpnicfDot11sAPCfgTable": hpnicfDot11sAPCfgTable,
       "hpnicfDot11sAPCfgEntry": hpnicfDot11sAPCfgEntry,
       "hpnicfDot11sPortalEnable": hpnicfDot11sPortalEnable,
       "hpnicfDot11sWDSConfigGroup": hpnicfDot11sWDSConfigGroup,
       "hpnicfDot11sWDSPeerMacTable": hpnicfDot11sWDSPeerMacTable,
       "hpnicfDot11sWDSPeerMacEntry": hpnicfDot11sWDSPeerMacEntry,
       "hpnicfDot11sWDSPeerMacIndex": hpnicfDot11sWDSPeerMacIndex,
       "hpnicfDot11sWDSPeerMacAddrss": hpnicfDot11sWDSPeerMacAddrss,
       "hpnicfDot11sWDSPeerMacRowStatus": hpnicfDot11sWDSPeerMacRowStatus,
       "hpnicfDot11sMeshStatusGroup": hpnicfDot11sMeshStatusGroup,
       "hpnicfDot11sMeshLinkStatusTable": hpnicfDot11sMeshLinkStatusTable,
       "hpnicfDot11sMeshLinkStatusEntry": hpnicfDot11sMeshLinkStatusEntry,
       "hpnicfDot11sMeshLinkIfIndex": hpnicfDot11sMeshLinkIfIndex,
       "hpnicfDot11sMeshLinkName": hpnicfDot11sMeshLinkName,
       "hpnicfDot11sMeshLinkBSSID": hpnicfDot11sMeshLinkBSSID,
       "hpnicfDot11sMeshLinkPeerMac": hpnicfDot11sMeshLinkPeerMac,
       "hpnicfDot11sMeshLinkExistDuration": hpnicfDot11sMeshLinkExistDuration,
       "hpnicfDot11sMeshLinkType": hpnicfDot11sMeshLinkType,
       "hpnicfDot11sMeshLinkStatisTable": hpnicfDot11sMeshLinkStatisTable,
       "hpnicfDot11sMeshLinkStatisEntry": hpnicfDot11sMeshLinkStatisEntry,
       "hpnicfDot11sMeshLinkStatIfIndex": hpnicfDot11sMeshLinkStatIfIndex,
       "hpnicfDot11sMeshLinkNbrIndex": hpnicfDot11sMeshLinkNbrIndex,
       "hpnicfDot11sMeshLinkRxTotByte": hpnicfDot11sMeshLinkRxTotByte,
       "hpnicfDot11sMeshLinkRxTotPkt": hpnicfDot11sMeshLinkRxTotPkt,
       "hpnicfDot11sMeshLinkRxUniPkt": hpnicfDot11sMeshLinkRxUniPkt,
       "hpnicfDot11sMeshLinkRxBrocPkt": hpnicfDot11sMeshLinkRxBrocPkt,
       "hpnicfDot11sMeshLinkRxMuticPkt": hpnicfDot11sMeshLinkRxMuticPkt,
       "hpnicfDot11sMeshLinkRxDiscPkt": hpnicfDot11sMeshLinkRxDiscPkt,
       "hpnicfDot11sMeshLinkTxTotByte": hpnicfDot11sMeshLinkTxTotByte,
       "hpnicfDot11sMeshLinkTxTotPkt": hpnicfDot11sMeshLinkTxTotPkt,
       "hpnicfDot11sMeshLinkTxUniPkt": hpnicfDot11sMeshLinkTxUniPkt,
       "hpnicfDot11sMeshLinkTxBrocPkt": hpnicfDot11sMeshLinkTxBrocPkt,
       "hpnicfDot11sMeshLinkTxMuticPkt": hpnicfDot11sMeshLinkTxMuticPkt,
       "hpnicfDot11sMeshLinkTxDiscPkt": hpnicfDot11sMeshLinkTxDiscPkt,
       "hpnicfDot11sMeshLinkIFName": hpnicfDot11sMeshLinkIFName,
       "hpnicfDot11sMeshNbrStatusTable": hpnicfDot11sMeshNbrStatusTable,
       "hpnicfDot11sMeshNbrStatusEntry": hpnicfDot11sMeshNbrStatusEntry,
       "hpnicfDot11sMeshNbrIndex": hpnicfDot11sMeshNbrIndex,
       "hpnicfDot11sMeshNbrRadioID": hpnicfDot11sMeshNbrRadioID,
       "hpnicfDot11sMeshLocalMeshID": hpnicfDot11sMeshLocalMeshID,
       "hpnicfDot11sMeshNbrMeshID": hpnicfDot11sMeshNbrMeshID,
       "hpnicfDot11sMeshNbrBSSID": hpnicfDot11sMeshNbrBSSID,
       "hpnicfDot11sMeshNbrPeerMac": hpnicfDot11sMeshNbrPeerMac,
       "hpnicfDot11sMeshLinkInMp": hpnicfDot11sMeshLinkInMp,
       "hpnicfDot11sMeshMPLinkStatus": hpnicfDot11sMeshMPLinkStatus,
       "hpnicfDot11sMeshNbrChannel": hpnicfDot11sMeshNbrChannel,
       "hpnicfDot11sMeshNbrLinkDuration": hpnicfDot11sMeshNbrLinkDuration,
       "hpnicfDot11sMeshNbrRSSI": hpnicfDot11sMeshNbrRSSI,
       "hpnicfDot11sMeshNbrSNR": hpnicfDot11sMeshNbrSNR}
)
