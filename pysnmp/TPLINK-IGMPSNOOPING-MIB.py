# SNMP MIB module (TPLINK-IGMPSNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-IGMPSNOOPING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:09 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")

(TPRowStatus,) = mibBuilder.importSymbols(
    "TPLINK-TC-MIB",
    "TPRowStatus")


# MODULE-IDENTITY

tplinkIgmpSnoopingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25)
)
tplinkIgmpSnoopingMIB.setRevisions(
        ("2012-12-14 14:32",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkIgmpSnoopingMIBObjects_ObjectIdentity = ObjectIdentity
tplinkIgmpSnoopingMIBObjects = _TplinkIgmpSnoopingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1)
)
_TpIgmpSnooping_ObjectIdentity = ObjectIdentity
tpIgmpSnooping = _TpIgmpSnooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1)
)
_TpIgmpSnoopingGlobalConfig_ObjectIdentity = ObjectIdentity
tpIgmpSnoopingGlobalConfig = _TpIgmpSnoopingGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 1)
)


class _TpIgmpSnoopingEnable_Type(Integer32):
    """Custom type tpIgmpSnoopingEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpIgmpSnoopingEnable_Type.__name__ = "Integer32"
_TpIgmpSnoopingEnable_Object = MibScalar
tpIgmpSnoopingEnable = _TpIgmpSnoopingEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 1, 1),
    _TpIgmpSnoopingEnable_Type()
)
tpIgmpSnoopingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpIgmpSnoopingEnable.setStatus("current")


class _TpUnknownMulticastPacket_Type(Integer32):
    """Custom type tpUnknownMulticastPacket based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("forward", 0))
    )


_TpUnknownMulticastPacket_Type.__name__ = "Integer32"
_TpUnknownMulticastPacket_Object = MibScalar
tpUnknownMulticastPacket = _TpUnknownMulticastPacket_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 1, 2),
    _TpUnknownMulticastPacket_Type()
)
tpUnknownMulticastPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpUnknownMulticastPacket.setStatus("current")


class _TpUnknownReportSuppression_Type(Integer32):
    """Custom type tpUnknownReportSuppression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpUnknownReportSuppression_Type.__name__ = "Integer32"
_TpUnknownReportSuppression_Object = MibScalar
tpUnknownReportSuppression = _TpUnknownReportSuppression_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 1, 3),
    _TpUnknownReportSuppression_Type()
)
tpUnknownReportSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpUnknownReportSuppression.setStatus("current")


class _TpIgmpGlobalRouterTime_Type(Integer32):
    """Custom type tpIgmpGlobalRouterTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_TpIgmpGlobalRouterTime_Type.__name__ = "Integer32"
_TpIgmpGlobalRouterTime_Object = MibScalar
tpIgmpGlobalRouterTime = _TpIgmpGlobalRouterTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 1, 4),
    _TpIgmpGlobalRouterTime_Type()
)
tpIgmpGlobalRouterTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIgmpGlobalRouterTime.setStatus("current")


class _TpIgmpGlobalMemberTime_Type(Integer32):
    """Custom type tpIgmpGlobalMemberTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_TpIgmpGlobalMemberTime_Type.__name__ = "Integer32"
_TpIgmpGlobalMemberTime_Object = MibScalar
tpIgmpGlobalMemberTime = _TpIgmpGlobalMemberTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 1, 5),
    _TpIgmpGlobalMemberTime_Type()
)
tpIgmpGlobalMemberTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIgmpGlobalMemberTime.setStatus("current")


class _TpIgmplastListenerQueryInterval_Type(Integer32):
    """Custom type tpIgmplastListenerQueryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_TpIgmplastListenerQueryInterval_Type.__name__ = "Integer32"
_TpIgmplastListenerQueryInterval_Object = MibScalar
tpIgmplastListenerQueryInterval = _TpIgmplastListenerQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 1, 6),
    _TpIgmplastListenerQueryInterval_Type()
)
tpIgmplastListenerQueryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIgmplastListenerQueryInterval.setStatus("current")


class _TpIgmplastListenerQueryCount_Type(Integer32):
    """Custom type tpIgmplastListenerQueryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_TpIgmplastListenerQueryCount_Type.__name__ = "Integer32"
_TpIgmplastListenerQueryCount_Object = MibScalar
tpIgmplastListenerQueryCount = _TpIgmplastListenerQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 1, 7),
    _TpIgmplastListenerQueryCount_Type()
)
tpIgmplastListenerQueryCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIgmplastListenerQueryCount.setStatus("current")
_TpIgmpPortConfig_ObjectIdentity = ObjectIdentity
tpIgmpPortConfig = _TpIgmpPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 2)
)
_TpIgmpPortTable_Object = MibTable
tpIgmpPortTable = _TpIgmpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tpIgmpPortTable.setStatus("current")
_TpIgmpPortEntry_Object = MibTableRow
tpIgmpPortEntry = _TpIgmpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 2, 1, 1)
)
tpIgmpPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tpIgmpPortEntry.setStatus("current")


class _TpIgmpSnoopingPortEnable_Type(Integer32):
    """Custom type tpIgmpSnoopingPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpIgmpSnoopingPortEnable_Type.__name__ = "Integer32"
_TpIgmpSnoopingPortEnable_Object = MibTableColumn
tpIgmpSnoopingPortEnable = _TpIgmpSnoopingPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 2, 1, 1, 2),
    _TpIgmpSnoopingPortEnable_Type()
)
tpIgmpSnoopingPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpIgmpSnoopingPortEnable.setStatus("current")


class _TpIgmpFastLeavePortEnable_Type(Integer32):
    """Custom type tpIgmpFastLeavePortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpIgmpFastLeavePortEnable_Type.__name__ = "Integer32"
_TpIgmpFastLeavePortEnable_Object = MibTableColumn
tpIgmpFastLeavePortEnable = _TpIgmpFastLeavePortEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 2, 1, 1, 3),
    _TpIgmpFastLeavePortEnable_Type()
)
tpIgmpFastLeavePortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpIgmpFastLeavePortEnable.setStatus("current")


class _TpIgmpPortLag_Type(OctetString):
    """Custom type tpIgmpPortLag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpIgmpPortLag_Type.__name__ = "OctetString"
_TpIgmpPortLag_Object = MibTableColumn
tpIgmpPortLag = _TpIgmpPortLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 2, 1, 1, 4),
    _TpIgmpPortLag_Type()
)
tpIgmpPortLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIgmpPortLag.setStatus("current")
_TpIgmpVlanConfig_ObjectIdentity = ObjectIdentity
tpIgmpVlanConfig = _TpIgmpVlanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 3)
)
_TpIgmpVlanTable_Object = MibTable
tpIgmpVlanTable = _TpIgmpVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tpIgmpVlanTable.setStatus("current")
_TpIgmpVlanEntry_Object = MibTableRow
tpIgmpVlanEntry = _TpIgmpVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 3, 1, 1)
)
tpIgmpVlanEntry.setIndexNames(
    (0, "TPLINK-IGMPSNOOPING-MIB", "tpIgmpVlanId"),
)
if mibBuilder.loadTexts:
    tpIgmpVlanEntry.setStatus("current")


class _TpIgmpVlanId_Type(Integer32):
    """Custom type tpIgmpVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_TpIgmpVlanId_Type.__name__ = "Integer32"
_TpIgmpVlanId_Object = MibTableColumn
tpIgmpVlanId = _TpIgmpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 3, 1, 1, 1),
    _TpIgmpVlanId_Type()
)
tpIgmpVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIgmpVlanId.setStatus("current")


class _TpIgmpRouterTime_Type(Integer32):
    """Custom type tpIgmpRouterTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_TpIgmpRouterTime_Type.__name__ = "Integer32"
_TpIgmpRouterTime_Object = MibTableColumn
tpIgmpRouterTime = _TpIgmpRouterTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 3, 1, 1, 2),
    _TpIgmpRouterTime_Type()
)
tpIgmpRouterTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIgmpRouterTime.setStatus("current")


class _TpIgmpMemberTime_Type(Integer32):
    """Custom type tpIgmpMemberTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_TpIgmpMemberTime_Type.__name__ = "Integer32"
_TpIgmpMemberTime_Object = MibTableColumn
tpIgmpMemberTime = _TpIgmpMemberTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 3, 1, 1, 3),
    _TpIgmpMemberTime_Type()
)
tpIgmpMemberTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIgmpMemberTime.setStatus("current")


class _TpIgmpRouterPort_Type(OctetString):
    """Custom type tpIgmpRouterPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpIgmpRouterPort_Type.__name__ = "OctetString"
_TpIgmpRouterPort_Object = MibTableColumn
tpIgmpRouterPort = _TpIgmpRouterPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 3, 1, 1, 4),
    _TpIgmpRouterPort_Type()
)
tpIgmpRouterPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIgmpRouterPort.setStatus("current")


class _TpIgmpForbiddenRouterPort_Type(OctetString):
    """Custom type tpIgmpForbiddenRouterPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpIgmpForbiddenRouterPort_Type.__name__ = "OctetString"
_TpIgmpForbiddenRouterPort_Object = MibTableColumn
tpIgmpForbiddenRouterPort = _TpIgmpForbiddenRouterPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 3, 1, 1, 5),
    _TpIgmpForbiddenRouterPort_Type()
)
tpIgmpForbiddenRouterPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIgmpForbiddenRouterPort.setStatus("current")
_TpIgmpVlanStatus_Type = TPRowStatus
_TpIgmpVlanStatus_Object = MibTableColumn
tpIgmpVlanStatus = _TpIgmpVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 3, 1, 1, 6),
    _TpIgmpVlanStatus_Type()
)
tpIgmpVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIgmpVlanStatus.setStatus("current")
_TpIgmpMultiVlanConfig_ObjectIdentity = ObjectIdentity
tpIgmpMultiVlanConfig = _TpIgmpMultiVlanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 4)
)


class _TpIgmpMultiVlanId_Type(Integer32):
    """Custom type tpIgmpMultiVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
    )


_TpIgmpMultiVlanId_Type.__name__ = "Integer32"
_TpIgmpMultiVlanId_Object = MibScalar
tpIgmpMultiVlanId = _TpIgmpMultiVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 4, 1),
    _TpIgmpMultiVlanId_Type()
)
tpIgmpMultiVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpIgmpMultiVlanId.setStatus("current")


class _TpIgmpMultitRouterTime_Type(Integer32):
    """Custom type tpIgmpMultitRouterTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_TpIgmpMultitRouterTime_Type.__name__ = "Integer32"
_TpIgmpMultitRouterTime_Object = MibScalar
tpIgmpMultitRouterTime = _TpIgmpMultitRouterTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 4, 2),
    _TpIgmpMultitRouterTime_Type()
)
tpIgmpMultitRouterTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpIgmpMultitRouterTime.setStatus("current")


class _TpIgmpMultiMemberTime_Type(Integer32):
    """Custom type tpIgmpMultiMemberTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_TpIgmpMultiMemberTime_Type.__name__ = "Integer32"
_TpIgmpMultiMemberTime_Object = MibScalar
tpIgmpMultiMemberTime = _TpIgmpMultiMemberTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 4, 3),
    _TpIgmpMultiMemberTime_Type()
)
tpIgmpMultiMemberTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpIgmpMultiMemberTime.setStatus("current")


class _TpIgmpMultiRouterPort_Type(OctetString):
    """Custom type tpIgmpMultiRouterPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpIgmpMultiRouterPort_Type.__name__ = "OctetString"
_TpIgmpMultiRouterPort_Object = MibScalar
tpIgmpMultiRouterPort = _TpIgmpMultiRouterPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 4, 4),
    _TpIgmpMultiRouterPort_Type()
)
tpIgmpMultiRouterPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpIgmpMultiRouterPort.setStatus("current")


class _TpIgmpMultiForbiddenRouterPort_Type(OctetString):
    """Custom type tpIgmpMultiForbiddenRouterPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpIgmpMultiForbiddenRouterPort_Type.__name__ = "OctetString"
_TpIgmpMultiForbiddenRouterPort_Object = MibScalar
tpIgmpMultiForbiddenRouterPort = _TpIgmpMultiForbiddenRouterPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 4, 5),
    _TpIgmpMultiForbiddenRouterPort_Type()
)
tpIgmpMultiForbiddenRouterPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpIgmpMultiForbiddenRouterPort.setStatus("current")
_TpIgmpMultiReplaceSrcIp_Type = IpAddress
_TpIgmpMultiReplaceSrcIp_Object = MibScalar
tpIgmpMultiReplaceSrcIp = _TpIgmpMultiReplaceSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 4, 6),
    _TpIgmpMultiReplaceSrcIp_Type()
)
tpIgmpMultiReplaceSrcIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIgmpMultiReplaceSrcIp.setStatus("current")
_TpIgmpQuerierConfig_ObjectIdentity = ObjectIdentity
tpIgmpQuerierConfig = _TpIgmpQuerierConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 5)
)
_IgmpQuerierTable_Object = MibTable
igmpQuerierTable = _IgmpQuerierTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    igmpQuerierTable.setStatus("current")
_IgmpQuerierEntry_Object = MibTableRow
igmpQuerierEntry = _IgmpQuerierEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 5, 1, 1)
)
igmpQuerierEntry.setIndexNames(
    (0, "TPLINK-IGMPSNOOPING-MIB", "igmpQuerierVlanId"),
)
if mibBuilder.loadTexts:
    igmpQuerierEntry.setStatus("current")


class _IgmpQuerierVlanId_Type(Integer32):
    """Custom type igmpQuerierVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_IgmpQuerierVlanId_Type.__name__ = "Integer32"
_IgmpQuerierVlanId_Object = MibTableColumn
igmpQuerierVlanId = _IgmpQuerierVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 5, 1, 1, 1),
    _IgmpQuerierVlanId_Type()
)
igmpQuerierVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpQuerierVlanId.setStatus("current")


class _QueryInterval_Type(Integer32):
    """Custom type queryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_QueryInterval_Type.__name__ = "Integer32"
_QueryInterval_Object = MibTableColumn
queryInterval = _QueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 5, 1, 1, 2),
    _QueryInterval_Type()
)
queryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    queryInterval.setStatus("current")


class _MaxResponseTime_Type(Integer32):
    """Custom type maxResponseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_MaxResponseTime_Type.__name__ = "Integer32"
_MaxResponseTime_Object = MibTableColumn
maxResponseTime = _MaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 5, 1, 1, 3),
    _MaxResponseTime_Type()
)
maxResponseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    maxResponseTime.setStatus("current")
_GeneralQuerySrcIp_Type = IpAddress
_GeneralQuerySrcIp_Object = MibTableColumn
generalQuerySrcIp = _GeneralQuerySrcIp_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 5, 1, 1, 4),
    _GeneralQuerySrcIp_Type()
)
generalQuerySrcIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    generalQuerySrcIp.setStatus("current")
_IgmpQuerierStatus_Type = TPRowStatus
_IgmpQuerierStatus_Object = MibTableColumn
igmpQuerierStatus = _IgmpQuerierStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 5, 1, 1, 5),
    _IgmpQuerierStatus_Type()
)
igmpQuerierStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpQuerierStatus.setStatus("current")
_TpIgmpFilter_ObjectIdentity = ObjectIdentity
tpIgmpFilter = _TpIgmpFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 2)
)
_TpIgmpPortFilterConfig_ObjectIdentity = ObjectIdentity
tpIgmpPortFilterConfig = _TpIgmpPortFilterConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 2, 1)
)
_TpIgmpFilterPortTable_Object = MibTable
tpIgmpFilterPortTable = _TpIgmpFilterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tpIgmpFilterPortTable.setStatus("current")
_TpIgmpFilterPortEntry_Object = MibTableRow
tpIgmpFilterPortEntry = _TpIgmpFilterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 2, 1, 1, 1)
)
tpIgmpFilterPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tpIgmpFilterPortEntry.setStatus("current")


class _TpIgmpFilterMaxGroup_Type(Integer32):
    """Custom type tpIgmpFilterMaxGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_TpIgmpFilterMaxGroup_Type.__name__ = "Integer32"
_TpIgmpFilterMaxGroup_Object = MibTableColumn
tpIgmpFilterMaxGroup = _TpIgmpFilterMaxGroup_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 2, 1, 1, 1, 2),
    _TpIgmpFilterMaxGroup_Type()
)
tpIgmpFilterMaxGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpIgmpFilterMaxGroup.setStatus("current")


class _TpIgmpFilterMaxGroupAction_Type(Integer32):
    """Custom type tpIgmpFilterMaxGroupAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("drop", 0),
          ("replace", 1))
    )


_TpIgmpFilterMaxGroupAction_Type.__name__ = "Integer32"
_TpIgmpFilterMaxGroupAction_Object = MibTableColumn
tpIgmpFilterMaxGroupAction = _TpIgmpFilterMaxGroupAction_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 2, 1, 1, 1, 3),
    _TpIgmpFilterMaxGroupAction_Type()
)
tpIgmpFilterMaxGroupAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpIgmpFilterMaxGroupAction.setStatus("current")


class _TpIgmpFilterBindAddrId_Type(OctetString):
    """Custom type tpIgmpFilterBindAddrId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_TpIgmpFilterBindAddrId_Type.__name__ = "OctetString"
_TpIgmpFilterBindAddrId_Object = MibTableColumn
tpIgmpFilterBindAddrId = _TpIgmpFilterBindAddrId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 2, 1, 1, 1, 4),
    _TpIgmpFilterBindAddrId_Type()
)
tpIgmpFilterBindAddrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpIgmpFilterBindAddrId.setStatus("current")


class _TpIgmpFilterPortLag_Type(OctetString):
    """Custom type tpIgmpFilterPortLag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpIgmpFilterPortLag_Type.__name__ = "OctetString"
_TpIgmpFilterPortLag_Object = MibTableColumn
tpIgmpFilterPortLag = _TpIgmpFilterPortLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 2, 1, 1, 1, 5),
    _TpIgmpFilterPortLag_Type()
)
tpIgmpFilterPortLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIgmpFilterPortLag.setStatus("current")
_TpIgmpAuth_ObjectIdentity = ObjectIdentity
tpIgmpAuth = _TpIgmpAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 3)
)
_TpIgmpPortAuthConfig_ObjectIdentity = ObjectIdentity
tpIgmpPortAuthConfig = _TpIgmpPortAuthConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 3, 1)
)
_TpIgmpAuthPortTable_Object = MibTable
tpIgmpAuthPortTable = _TpIgmpAuthPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    tpIgmpAuthPortTable.setStatus("current")
_TpIgmpAuthPortEntry_Object = MibTableRow
tpIgmpAuthPortEntry = _TpIgmpAuthPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 3, 1, 1, 1)
)
tpIgmpAuthPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tpIgmpAuthPortEntry.setStatus("current")


class _TpIgmpAuthEnable_Type(Integer32):
    """Custom type tpIgmpAuthEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpIgmpAuthEnable_Type.__name__ = "Integer32"
_TpIgmpAuthEnable_Object = MibTableColumn
tpIgmpAuthEnable = _TpIgmpAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 3, 1, 1, 1, 2),
    _TpIgmpAuthEnable_Type()
)
tpIgmpAuthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpIgmpAuthEnable.setStatus("current")


class _TpIgmpAuthPortLag_Type(OctetString):
    """Custom type tpIgmpAuthPortLag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpIgmpAuthPortLag_Type.__name__ = "OctetString"
_TpIgmpAuthPortLag_Object = MibTableColumn
tpIgmpAuthPortLag = _TpIgmpAuthPortLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 3, 1, 1, 1, 3),
    _TpIgmpAuthPortLag_Type()
)
tpIgmpAuthPortLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIgmpAuthPortLag.setStatus("current")
_TpIgmpGlobalAuthAccountConfig_ObjectIdentity = ObjectIdentity
tpIgmpGlobalAuthAccountConfig = _TpIgmpGlobalAuthAccountConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 3, 2)
)


class _TpIgmpGlobalAuthAccountConfigEable_Type(Integer32):
    """Custom type tpIgmpGlobalAuthAccountConfigEable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpIgmpGlobalAuthAccountConfigEable_Type.__name__ = "Integer32"
_TpIgmpGlobalAuthAccountConfigEable_Object = MibScalar
tpIgmpGlobalAuthAccountConfigEable = _TpIgmpGlobalAuthAccountConfigEable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 3, 2, 1),
    _TpIgmpGlobalAuthAccountConfigEable_Type()
)
tpIgmpGlobalAuthAccountConfigEable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpIgmpGlobalAuthAccountConfigEable.setStatus("current")
_TpIgmpPacketStatistic_ObjectIdentity = ObjectIdentity
tpIgmpPacketStatistic = _TpIgmpPacketStatistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 4)
)
_TpIgmpPktStat_ObjectIdentity = ObjectIdentity
tpIgmpPktStat = _TpIgmpPktStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 4, 1)
)
_TpIgmpPktStatTable_Object = MibTable
tpIgmpPktStatTable = _TpIgmpPktStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    tpIgmpPktStatTable.setStatus("current")
_TpIgmpPktStatEntry_Object = MibTableRow
tpIgmpPktStatEntry = _TpIgmpPktStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 4, 1, 1, 1)
)
tpIgmpPktStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tpIgmpPktStatEntry.setStatus("current")
_TpIgmpQueryPktStat_Type = Integer32
_TpIgmpQueryPktStat_Object = MibTableColumn
tpIgmpQueryPktStat = _TpIgmpQueryPktStat_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 4, 1, 1, 1, 2),
    _TpIgmpQueryPktStat_Type()
)
tpIgmpQueryPktStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIgmpQueryPktStat.setStatus("current")
_TpIgmpReportV1PktStat_Type = Integer32
_TpIgmpReportV1PktStat_Object = MibTableColumn
tpIgmpReportV1PktStat = _TpIgmpReportV1PktStat_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 4, 1, 1, 1, 3),
    _TpIgmpReportV1PktStat_Type()
)
tpIgmpReportV1PktStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIgmpReportV1PktStat.setStatus("current")
_TpIgmpReportV2PktStat_Type = Integer32
_TpIgmpReportV2PktStat_Object = MibTableColumn
tpIgmpReportV2PktStat = _TpIgmpReportV2PktStat_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 4, 1, 1, 1, 4),
    _TpIgmpReportV2PktStat_Type()
)
tpIgmpReportV2PktStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIgmpReportV2PktStat.setStatus("current")
_TpIgmpReportV3PktStat_Type = Integer32
_TpIgmpReportV3PktStat_Object = MibTableColumn
tpIgmpReportV3PktStat = _TpIgmpReportV3PktStat_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 4, 1, 1, 1, 5),
    _TpIgmpReportV3PktStat_Type()
)
tpIgmpReportV3PktStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIgmpReportV3PktStat.setStatus("current")
_TpIgmpLeavePktStat_Type = Integer32
_TpIgmpLeavePktStat_Object = MibTableColumn
tpIgmpLeavePktStat = _TpIgmpLeavePktStat_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 4, 1, 1, 1, 6),
    _TpIgmpLeavePktStat_Type()
)
tpIgmpLeavePktStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIgmpLeavePktStat.setStatus("current")
_TpIgmpErrorPktStat_Type = Integer32
_TpIgmpErrorPktStat_Object = MibTableColumn
tpIgmpErrorPktStat = _TpIgmpErrorPktStat_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 4, 1, 1, 1, 7),
    _TpIgmpErrorPktStat_Type()
)
tpIgmpErrorPktStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIgmpErrorPktStat.setStatus("current")


class _TpIpIgmpPktStatClear_Type(Integer32):
    """Custom type tpIpIgmpPktStatClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("commit", 1)
    )


_TpIpIgmpPktStatClear_Type.__name__ = "Integer32"
_TpIpIgmpPktStatClear_Object = MibScalar
tpIpIgmpPktStatClear = _TpIpIgmpPktStatClear_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 4, 1, 2),
    _TpIpIgmpPktStatClear_Type()
)
tpIpIgmpPktStatClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpIpIgmpPktStatClear.setStatus("current")
_TpIgmpMultigroup_ObjectIdentity = ObjectIdentity
tpIgmpMultigroup = _TpIgmpMultigroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 5)
)
_TpIgmpMulticastGroups_ObjectIdentity = ObjectIdentity
tpIgmpMulticastGroups = _TpIgmpMulticastGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 5, 1)
)
_TpIgmpMulticastGroupTable_Object = MibTable
tpIgmpMulticastGroupTable = _TpIgmpMulticastGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    tpIgmpMulticastGroupTable.setStatus("current")
_TpIgmpMulticastGroupEntry_Object = MibTableRow
tpIgmpMulticastGroupEntry = _TpIgmpMulticastGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 5, 1, 1, 1)
)
tpIgmpMulticastGroupEntry.setIndexNames(
    (0, "TPLINK-IGMPSNOOPING-MIB", "tpIgmpMulticastIP"),
    (0, "TPLINK-IGMPSNOOPING-MIB", "tpIgmpVlanID"),
)
if mibBuilder.loadTexts:
    tpIgmpMulticastGroupEntry.setStatus("current")
_TpIgmpMulticastIP_Type = IpAddress
_TpIgmpMulticastIP_Object = MibTableColumn
tpIgmpMulticastIP = _TpIgmpMulticastIP_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 5, 1, 1, 1, 1),
    _TpIgmpMulticastIP_Type()
)
tpIgmpMulticastIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIgmpMulticastIP.setStatus("current")
_TpIgmpVlanID_Type = Integer32
_TpIgmpVlanID_Object = MibTableColumn
tpIgmpVlanID = _TpIgmpVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 5, 1, 1, 1, 2),
    _TpIgmpVlanID_Type()
)
tpIgmpVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIgmpVlanID.setStatus("current")


class _TpIgmpForwardPorts_Type(OctetString):
    """Custom type tpIgmpForwardPorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_TpIgmpForwardPorts_Type.__name__ = "OctetString"
_TpIgmpForwardPorts_Object = MibTableColumn
tpIgmpForwardPorts = _TpIgmpForwardPorts_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 5, 1, 1, 1, 3),
    _TpIgmpForwardPorts_Type()
)
tpIgmpForwardPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIgmpForwardPorts.setStatus("current")


class _TpIgmpGrouptype_Type(Integer32):
    """Custom type tpIgmpGrouptype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 0))
    )


_TpIgmpGrouptype_Type.__name__ = "Integer32"
_TpIgmpGrouptype_Object = MibTableColumn
tpIgmpGrouptype = _TpIgmpGrouptype_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 5, 1, 1, 1, 4),
    _TpIgmpGrouptype_Type()
)
tpIgmpGrouptype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIgmpGrouptype.setStatus("current")
_TpIgmpStaticMultigroup_ObjectIdentity = ObjectIdentity
tpIgmpStaticMultigroup = _TpIgmpStaticMultigroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 6)
)
_TpIgmpMulticastStaticGroups_ObjectIdentity = ObjectIdentity
tpIgmpMulticastStaticGroups = _TpIgmpMulticastStaticGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 6, 1)
)
_TpIgmpMulticastStaticGroupTable_Object = MibTable
tpIgmpMulticastStaticGroupTable = _TpIgmpMulticastStaticGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    tpIgmpMulticastStaticGroupTable.setStatus("current")
_TpIgmpMulticastStaticGroupEntry_Object = MibTableRow
tpIgmpMulticastStaticGroupEntry = _TpIgmpMulticastStaticGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 6, 1, 1, 1)
)
tpIgmpMulticastStaticGroupEntry.setIndexNames(
    (0, "TPLINK-IGMPSNOOPING-MIB", "tpIgmpStaticMulticastIP"),
    (0, "TPLINK-IGMPSNOOPING-MIB", "tpIgmpStaticVlanID"),
)
if mibBuilder.loadTexts:
    tpIgmpMulticastStaticGroupEntry.setStatus("current")
_TpIgmpStaticMulticastIP_Type = IpAddress
_TpIgmpStaticMulticastIP_Object = MibTableColumn
tpIgmpStaticMulticastIP = _TpIgmpStaticMulticastIP_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 6, 1, 1, 1, 1),
    _TpIgmpStaticMulticastIP_Type()
)
tpIgmpStaticMulticastIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIgmpStaticMulticastIP.setStatus("current")
_TpIgmpStaticVlanID_Type = Integer32
_TpIgmpStaticVlanID_Object = MibTableColumn
tpIgmpStaticVlanID = _TpIgmpStaticVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 6, 1, 1, 1, 2),
    _TpIgmpStaticVlanID_Type()
)
tpIgmpStaticVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIgmpStaticVlanID.setStatus("current")


class _TpIgmpStaticForwardPorts_Type(OctetString):
    """Custom type tpIgmpStaticForwardPorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_TpIgmpStaticForwardPorts_Type.__name__ = "OctetString"
_TpIgmpStaticForwardPorts_Object = MibTableColumn
tpIgmpStaticForwardPorts = _TpIgmpStaticForwardPorts_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 6, 1, 1, 1, 3),
    _TpIgmpStaticForwardPorts_Type()
)
tpIgmpStaticForwardPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIgmpStaticForwardPorts.setStatus("current")
_TpIgmpStaticGroupStatus_Type = TPRowStatus
_TpIgmpStaticGroupStatus_Object = MibTableColumn
tpIgmpStaticGroupStatus = _TpIgmpStaticGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 6, 1, 1, 1, 4),
    _TpIgmpStaticGroupStatus_Type()
)
tpIgmpStaticGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIgmpStaticGroupStatus.setStatus("current")
_TplinkIgmpSnoopingNotifications_ObjectIdentity = ObjectIdentity
tplinkIgmpSnoopingNotifications = _TplinkIgmpSnoopingNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 25, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-IGMPSNOOPING-MIB",
    **{"tplinkIgmpSnoopingMIB": tplinkIgmpSnoopingMIB,
       "tplinkIgmpSnoopingMIBObjects": tplinkIgmpSnoopingMIBObjects,
       "tpIgmpSnooping": tpIgmpSnooping,
       "tpIgmpSnoopingGlobalConfig": tpIgmpSnoopingGlobalConfig,
       "tpIgmpSnoopingEnable": tpIgmpSnoopingEnable,
       "tpUnknownMulticastPacket": tpUnknownMulticastPacket,
       "tpUnknownReportSuppression": tpUnknownReportSuppression,
       "tpIgmpGlobalRouterTime": tpIgmpGlobalRouterTime,
       "tpIgmpGlobalMemberTime": tpIgmpGlobalMemberTime,
       "tpIgmplastListenerQueryInterval": tpIgmplastListenerQueryInterval,
       "tpIgmplastListenerQueryCount": tpIgmplastListenerQueryCount,
       "tpIgmpPortConfig": tpIgmpPortConfig,
       "tpIgmpPortTable": tpIgmpPortTable,
       "tpIgmpPortEntry": tpIgmpPortEntry,
       "tpIgmpSnoopingPortEnable": tpIgmpSnoopingPortEnable,
       "tpIgmpFastLeavePortEnable": tpIgmpFastLeavePortEnable,
       "tpIgmpPortLag": tpIgmpPortLag,
       "tpIgmpVlanConfig": tpIgmpVlanConfig,
       "tpIgmpVlanTable": tpIgmpVlanTable,
       "tpIgmpVlanEntry": tpIgmpVlanEntry,
       "tpIgmpVlanId": tpIgmpVlanId,
       "tpIgmpRouterTime": tpIgmpRouterTime,
       "tpIgmpMemberTime": tpIgmpMemberTime,
       "tpIgmpRouterPort": tpIgmpRouterPort,
       "tpIgmpForbiddenRouterPort": tpIgmpForbiddenRouterPort,
       "tpIgmpVlanStatus": tpIgmpVlanStatus,
       "tpIgmpMultiVlanConfig": tpIgmpMultiVlanConfig,
       "tpIgmpMultiVlanId": tpIgmpMultiVlanId,
       "tpIgmpMultitRouterTime": tpIgmpMultitRouterTime,
       "tpIgmpMultiMemberTime": tpIgmpMultiMemberTime,
       "tpIgmpMultiRouterPort": tpIgmpMultiRouterPort,
       "tpIgmpMultiForbiddenRouterPort": tpIgmpMultiForbiddenRouterPort,
       "tpIgmpMultiReplaceSrcIp": tpIgmpMultiReplaceSrcIp,
       "tpIgmpQuerierConfig": tpIgmpQuerierConfig,
       "igmpQuerierTable": igmpQuerierTable,
       "igmpQuerierEntry": igmpQuerierEntry,
       "igmpQuerierVlanId": igmpQuerierVlanId,
       "queryInterval": queryInterval,
       "maxResponseTime": maxResponseTime,
       "generalQuerySrcIp": generalQuerySrcIp,
       "igmpQuerierStatus": igmpQuerierStatus,
       "tpIgmpFilter": tpIgmpFilter,
       "tpIgmpPortFilterConfig": tpIgmpPortFilterConfig,
       "tpIgmpFilterPortTable": tpIgmpFilterPortTable,
       "tpIgmpFilterPortEntry": tpIgmpFilterPortEntry,
       "tpIgmpFilterMaxGroup": tpIgmpFilterMaxGroup,
       "tpIgmpFilterMaxGroupAction": tpIgmpFilterMaxGroupAction,
       "tpIgmpFilterBindAddrId": tpIgmpFilterBindAddrId,
       "tpIgmpFilterPortLag": tpIgmpFilterPortLag,
       "tpIgmpAuth": tpIgmpAuth,
       "tpIgmpPortAuthConfig": tpIgmpPortAuthConfig,
       "tpIgmpAuthPortTable": tpIgmpAuthPortTable,
       "tpIgmpAuthPortEntry": tpIgmpAuthPortEntry,
       "tpIgmpAuthEnable": tpIgmpAuthEnable,
       "tpIgmpAuthPortLag": tpIgmpAuthPortLag,
       "tpIgmpGlobalAuthAccountConfig": tpIgmpGlobalAuthAccountConfig,
       "tpIgmpGlobalAuthAccountConfigEable": tpIgmpGlobalAuthAccountConfigEable,
       "tpIgmpPacketStatistic": tpIgmpPacketStatistic,
       "tpIgmpPktStat": tpIgmpPktStat,
       "tpIgmpPktStatTable": tpIgmpPktStatTable,
       "tpIgmpPktStatEntry": tpIgmpPktStatEntry,
       "tpIgmpQueryPktStat": tpIgmpQueryPktStat,
       "tpIgmpReportV1PktStat": tpIgmpReportV1PktStat,
       "tpIgmpReportV2PktStat": tpIgmpReportV2PktStat,
       "tpIgmpReportV3PktStat": tpIgmpReportV3PktStat,
       "tpIgmpLeavePktStat": tpIgmpLeavePktStat,
       "tpIgmpErrorPktStat": tpIgmpErrorPktStat,
       "tpIpIgmpPktStatClear": tpIpIgmpPktStatClear,
       "tpIgmpMultigroup": tpIgmpMultigroup,
       "tpIgmpMulticastGroups": tpIgmpMulticastGroups,
       "tpIgmpMulticastGroupTable": tpIgmpMulticastGroupTable,
       "tpIgmpMulticastGroupEntry": tpIgmpMulticastGroupEntry,
       "tpIgmpMulticastIP": tpIgmpMulticastIP,
       "tpIgmpVlanID": tpIgmpVlanID,
       "tpIgmpForwardPorts": tpIgmpForwardPorts,
       "tpIgmpGrouptype": tpIgmpGrouptype,
       "tpIgmpStaticMultigroup": tpIgmpStaticMultigroup,
       "tpIgmpMulticastStaticGroups": tpIgmpMulticastStaticGroups,
       "tpIgmpMulticastStaticGroupTable": tpIgmpMulticastStaticGroupTable,
       "tpIgmpMulticastStaticGroupEntry": tpIgmpMulticastStaticGroupEntry,
       "tpIgmpStaticMulticastIP": tpIgmpStaticMulticastIP,
       "tpIgmpStaticVlanID": tpIgmpStaticVlanID,
       "tpIgmpStaticForwardPorts": tpIgmpStaticForwardPorts,
       "tpIgmpStaticGroupStatus": tpIgmpStaticGroupStatus,
       "tplinkIgmpSnoopingNotifications": tplinkIgmpSnoopingNotifications}
)
