# SNMP MIB module (TPLINK-MLDSNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-MLDSNOOPING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:23 2024
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

tplinkMldSnoopingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43)
)
tplinkMldSnoopingMIB.setRevisions(
        ("2012-12-14 14:32",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkMldSnoopingMIBObjects_ObjectIdentity = ObjectIdentity
tplinkMldSnoopingMIBObjects = _TplinkMldSnoopingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1)
)
_TpMldSnooping_ObjectIdentity = ObjectIdentity
tpMldSnooping = _TpMldSnooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1)
)
_TpMldSnoopingGlobalConfig_ObjectIdentity = ObjectIdentity
tpMldSnoopingGlobalConfig = _TpMldSnoopingGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 1)
)


class _TpMldSnoopingEnable_Type(Integer32):
    """Custom type tpMldSnoopingEnable based on Integer32"""
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


_TpMldSnoopingEnable_Type.__name__ = "Integer32"
_TpMldSnoopingEnable_Object = MibScalar
tpMldSnoopingEnable = _TpMldSnoopingEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 1, 1),
    _TpMldSnoopingEnable_Type()
)
tpMldSnoopingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpMldSnoopingEnable.setStatus("current")


class _TpMldUnknownMulticastPacket_Type(Integer32):
    """Custom type tpMldUnknownMulticastPacket based on Integer32"""
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


_TpMldUnknownMulticastPacket_Type.__name__ = "Integer32"
_TpMldUnknownMulticastPacket_Object = MibScalar
tpMldUnknownMulticastPacket = _TpMldUnknownMulticastPacket_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 1, 2),
    _TpMldUnknownMulticastPacket_Type()
)
tpMldUnknownMulticastPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpMldUnknownMulticastPacket.setStatus("current")


class _TpMldUnknownReportSuppression_Type(Integer32):
    """Custom type tpMldUnknownReportSuppression based on Integer32"""
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


_TpMldUnknownReportSuppression_Type.__name__ = "Integer32"
_TpMldUnknownReportSuppression_Object = MibScalar
tpMldUnknownReportSuppression = _TpMldUnknownReportSuppression_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 1, 3),
    _TpMldUnknownReportSuppression_Type()
)
tpMldUnknownReportSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpMldUnknownReportSuppression.setStatus("current")


class _TpMldGlobalRouterTime_Type(Integer32):
    """Custom type tpMldGlobalRouterTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_TpMldGlobalRouterTime_Type.__name__ = "Integer32"
_TpMldGlobalRouterTime_Object = MibScalar
tpMldGlobalRouterTime = _TpMldGlobalRouterTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 1, 4),
    _TpMldGlobalRouterTime_Type()
)
tpMldGlobalRouterTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMldGlobalRouterTime.setStatus("current")


class _TpMldGlobalMemberTime_Type(Integer32):
    """Custom type tpMldGlobalMemberTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_TpMldGlobalMemberTime_Type.__name__ = "Integer32"
_TpMldGlobalMemberTime_Object = MibScalar
tpMldGlobalMemberTime = _TpMldGlobalMemberTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 1, 5),
    _TpMldGlobalMemberTime_Type()
)
tpMldGlobalMemberTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMldGlobalMemberTime.setStatus("current")


class _TpMldlastListenerQueryInterval_Type(Integer32):
    """Custom type tpMldlastListenerQueryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_TpMldlastListenerQueryInterval_Type.__name__ = "Integer32"
_TpMldlastListenerQueryInterval_Object = MibScalar
tpMldlastListenerQueryInterval = _TpMldlastListenerQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 1, 6),
    _TpMldlastListenerQueryInterval_Type()
)
tpMldlastListenerQueryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMldlastListenerQueryInterval.setStatus("current")


class _TpMldlastListenerQueryCount_Type(Integer32):
    """Custom type tpMldlastListenerQueryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_TpMldlastListenerQueryCount_Type.__name__ = "Integer32"
_TpMldlastListenerQueryCount_Object = MibScalar
tpMldlastListenerQueryCount = _TpMldlastListenerQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 1, 7),
    _TpMldlastListenerQueryCount_Type()
)
tpMldlastListenerQueryCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMldlastListenerQueryCount.setStatus("current")
_TpMldPortConfig_ObjectIdentity = ObjectIdentity
tpMldPortConfig = _TpMldPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 2)
)
_TpMldPortTable_Object = MibTable
tpMldPortTable = _TpMldPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tpMldPortTable.setStatus("current")
_TpMldPortEntry_Object = MibTableRow
tpMldPortEntry = _TpMldPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 2, 1, 1)
)
tpMldPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tpMldPortEntry.setStatus("current")


class _TpMldSnoopingPortEnable_Type(Integer32):
    """Custom type tpMldSnoopingPortEnable based on Integer32"""
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


_TpMldSnoopingPortEnable_Type.__name__ = "Integer32"
_TpMldSnoopingPortEnable_Object = MibTableColumn
tpMldSnoopingPortEnable = _TpMldSnoopingPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 2, 1, 1, 2),
    _TpMldSnoopingPortEnable_Type()
)
tpMldSnoopingPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpMldSnoopingPortEnable.setStatus("current")


class _TpMldFastLeavePortEnable_Type(Integer32):
    """Custom type tpMldFastLeavePortEnable based on Integer32"""
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


_TpMldFastLeavePortEnable_Type.__name__ = "Integer32"
_TpMldFastLeavePortEnable_Object = MibTableColumn
tpMldFastLeavePortEnable = _TpMldFastLeavePortEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 2, 1, 1, 3),
    _TpMldFastLeavePortEnable_Type()
)
tpMldFastLeavePortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpMldFastLeavePortEnable.setStatus("current")


class _TpMldPortLag_Type(OctetString):
    """Custom type tpMldPortLag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpMldPortLag_Type.__name__ = "OctetString"
_TpMldPortLag_Object = MibTableColumn
tpMldPortLag = _TpMldPortLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 2, 1, 1, 4),
    _TpMldPortLag_Type()
)
tpMldPortLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpMldPortLag.setStatus("current")
_TpMldVlanConfig_ObjectIdentity = ObjectIdentity
tpMldVlanConfig = _TpMldVlanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 3)
)
_TpMldVlanTable_Object = MibTable
tpMldVlanTable = _TpMldVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tpMldVlanTable.setStatus("current")
_TpMldVlanEntry_Object = MibTableRow
tpMldVlanEntry = _TpMldVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 3, 1, 1)
)
tpMldVlanEntry.setIndexNames(
    (0, "TPLINK-MLDSNOOPING-MIB", "tpMldVlanId"),
)
if mibBuilder.loadTexts:
    tpMldVlanEntry.setStatus("current")


class _TpMldVlanId_Type(Integer32):
    """Custom type tpMldVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_TpMldVlanId_Type.__name__ = "Integer32"
_TpMldVlanId_Object = MibTableColumn
tpMldVlanId = _TpMldVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 3, 1, 1, 1),
    _TpMldVlanId_Type()
)
tpMldVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpMldVlanId.setStatus("current")


class _TpMldRouterTime_Type(Integer32):
    """Custom type tpMldRouterTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_TpMldRouterTime_Type.__name__ = "Integer32"
_TpMldRouterTime_Object = MibTableColumn
tpMldRouterTime = _TpMldRouterTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 3, 1, 1, 2),
    _TpMldRouterTime_Type()
)
tpMldRouterTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMldRouterTime.setStatus("current")


class _TpMldMemberTime_Type(Integer32):
    """Custom type tpMldMemberTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_TpMldMemberTime_Type.__name__ = "Integer32"
_TpMldMemberTime_Object = MibTableColumn
tpMldMemberTime = _TpMldMemberTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 3, 1, 1, 3),
    _TpMldMemberTime_Type()
)
tpMldMemberTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMldMemberTime.setStatus("current")


class _TpMldRouterPort_Type(OctetString):
    """Custom type tpMldRouterPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpMldRouterPort_Type.__name__ = "OctetString"
_TpMldRouterPort_Object = MibTableColumn
tpMldRouterPort = _TpMldRouterPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 3, 1, 1, 4),
    _TpMldRouterPort_Type()
)
tpMldRouterPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMldRouterPort.setStatus("current")


class _TpMldForbiddenRouterPort_Type(OctetString):
    """Custom type tpMldForbiddenRouterPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpMldForbiddenRouterPort_Type.__name__ = "OctetString"
_TpMldForbiddenRouterPort_Object = MibTableColumn
tpMldForbiddenRouterPort = _TpMldForbiddenRouterPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 3, 1, 1, 5),
    _TpMldForbiddenRouterPort_Type()
)
tpMldForbiddenRouterPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMldForbiddenRouterPort.setStatus("current")
_TpMldVlanStatus_Type = TPRowStatus
_TpMldVlanStatus_Object = MibTableColumn
tpMldVlanStatus = _TpMldVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 3, 1, 1, 6),
    _TpMldVlanStatus_Type()
)
tpMldVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMldVlanStatus.setStatus("current")
_TpMldMultiVlanConfig_ObjectIdentity = ObjectIdentity
tpMldMultiVlanConfig = _TpMldMultiVlanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 4)
)


class _TpMldMultiVlanId_Type(Integer32):
    """Custom type tpMldMultiVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
    )


_TpMldMultiVlanId_Type.__name__ = "Integer32"
_TpMldMultiVlanId_Object = MibScalar
tpMldMultiVlanId = _TpMldMultiVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 4, 1),
    _TpMldMultiVlanId_Type()
)
tpMldMultiVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpMldMultiVlanId.setStatus("current")


class _TpMldMultitRouterTime_Type(Integer32):
    """Custom type tpMldMultitRouterTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_TpMldMultitRouterTime_Type.__name__ = "Integer32"
_TpMldMultitRouterTime_Object = MibScalar
tpMldMultitRouterTime = _TpMldMultitRouterTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 4, 2),
    _TpMldMultitRouterTime_Type()
)
tpMldMultitRouterTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpMldMultitRouterTime.setStatus("current")


class _TpMldMultiMemberTime_Type(Integer32):
    """Custom type tpMldMultiMemberTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_TpMldMultiMemberTime_Type.__name__ = "Integer32"
_TpMldMultiMemberTime_Object = MibScalar
tpMldMultiMemberTime = _TpMldMultiMemberTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 4, 3),
    _TpMldMultiMemberTime_Type()
)
tpMldMultiMemberTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpMldMultiMemberTime.setStatus("current")


class _TpMldMultiRouterPort_Type(OctetString):
    """Custom type tpMldMultiRouterPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpMldMultiRouterPort_Type.__name__ = "OctetString"
_TpMldMultiRouterPort_Object = MibScalar
tpMldMultiRouterPort = _TpMldMultiRouterPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 4, 4),
    _TpMldMultiRouterPort_Type()
)
tpMldMultiRouterPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpMldMultiRouterPort.setStatus("current")


class _TpMldMultiForbiddenRouterPort_Type(OctetString):
    """Custom type tpMldMultiForbiddenRouterPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpMldMultiForbiddenRouterPort_Type.__name__ = "OctetString"
_TpMldMultiForbiddenRouterPort_Object = MibScalar
tpMldMultiForbiddenRouterPort = _TpMldMultiForbiddenRouterPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 4, 5),
    _TpMldMultiForbiddenRouterPort_Type()
)
tpMldMultiForbiddenRouterPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpMldMultiForbiddenRouterPort.setStatus("current")
_TpMldMultiReplaceSrcIp_Type = OctetString
_TpMldMultiReplaceSrcIp_Object = MibScalar
tpMldMultiReplaceSrcIp = _TpMldMultiReplaceSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 4, 6),
    _TpMldMultiReplaceSrcIp_Type()
)
tpMldMultiReplaceSrcIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMldMultiReplaceSrcIp.setStatus("current")
_TpMldQuerierConfig_ObjectIdentity = ObjectIdentity
tpMldQuerierConfig = _TpMldQuerierConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 5)
)
_MldQuerierTable_Object = MibTable
mldQuerierTable = _MldQuerierTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    mldQuerierTable.setStatus("current")
_MldQuerierEntry_Object = MibTableRow
mldQuerierEntry = _MldQuerierEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 5, 1, 1)
)
mldQuerierEntry.setIndexNames(
    (0, "TPLINK-MLDSNOOPING-MIB", "mldQuerierVlanId"),
)
if mibBuilder.loadTexts:
    mldQuerierEntry.setStatus("current")


class _MldQuerierVlanId_Type(Integer32):
    """Custom type mldQuerierVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MldQuerierVlanId_Type.__name__ = "Integer32"
_MldQuerierVlanId_Object = MibTableColumn
mldQuerierVlanId = _MldQuerierVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 5, 1, 1, 1),
    _MldQuerierVlanId_Type()
)
mldQuerierVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldQuerierVlanId.setStatus("current")


class _MldQueryInterval_Type(Integer32):
    """Custom type mldQueryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_MldQueryInterval_Type.__name__ = "Integer32"
_MldQueryInterval_Object = MibTableColumn
mldQueryInterval = _MldQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 5, 1, 1, 2),
    _MldQueryInterval_Type()
)
mldQueryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mldQueryInterval.setStatus("current")


class _MldMaxResponseTime_Type(Integer32):
    """Custom type mldMaxResponseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_MldMaxResponseTime_Type.__name__ = "Integer32"
_MldMaxResponseTime_Object = MibTableColumn
mldMaxResponseTime = _MldMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 5, 1, 1, 3),
    _MldMaxResponseTime_Type()
)
mldMaxResponseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mldMaxResponseTime.setStatus("current")
_MldGeneralQuerySrcIp_Type = OctetString
_MldGeneralQuerySrcIp_Object = MibTableColumn
mldGeneralQuerySrcIp = _MldGeneralQuerySrcIp_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 5, 1, 1, 4),
    _MldGeneralQuerySrcIp_Type()
)
mldGeneralQuerySrcIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mldGeneralQuerySrcIp.setStatus("current")
_MldQuerierStatus_Type = TPRowStatus
_MldQuerierStatus_Object = MibTableColumn
mldQuerierStatus = _MldQuerierStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 1, 5, 1, 1, 5),
    _MldQuerierStatus_Type()
)
mldQuerierStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mldQuerierStatus.setStatus("current")
_TpMldFilter_ObjectIdentity = ObjectIdentity
tpMldFilter = _TpMldFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 2)
)
_TpMldPortFilterConfig_ObjectIdentity = ObjectIdentity
tpMldPortFilterConfig = _TpMldPortFilterConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 2, 1)
)
_TpMldFilterPortTable_Object = MibTable
tpMldFilterPortTable = _TpMldFilterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tpMldFilterPortTable.setStatus("current")
_TpMldFilterPortEntry_Object = MibTableRow
tpMldFilterPortEntry = _TpMldFilterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 2, 1, 1, 1)
)
tpMldFilterPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tpMldFilterPortEntry.setStatus("current")


class _TpMldFilterMaxGroup_Type(Integer32):
    """Custom type tpMldFilterMaxGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_TpMldFilterMaxGroup_Type.__name__ = "Integer32"
_TpMldFilterMaxGroup_Object = MibTableColumn
tpMldFilterMaxGroup = _TpMldFilterMaxGroup_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 2, 1, 1, 1, 2),
    _TpMldFilterMaxGroup_Type()
)
tpMldFilterMaxGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpMldFilterMaxGroup.setStatus("current")


class _TpMldFilterMaxGroupAction_Type(Integer32):
    """Custom type tpMldFilterMaxGroupAction based on Integer32"""
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


_TpMldFilterMaxGroupAction_Type.__name__ = "Integer32"
_TpMldFilterMaxGroupAction_Object = MibTableColumn
tpMldFilterMaxGroupAction = _TpMldFilterMaxGroupAction_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 2, 1, 1, 1, 3),
    _TpMldFilterMaxGroupAction_Type()
)
tpMldFilterMaxGroupAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpMldFilterMaxGroupAction.setStatus("current")


class _TpMldFilterBindAddrId_Type(OctetString):
    """Custom type tpMldFilterBindAddrId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_TpMldFilterBindAddrId_Type.__name__ = "OctetString"
_TpMldFilterBindAddrId_Object = MibTableColumn
tpMldFilterBindAddrId = _TpMldFilterBindAddrId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 2, 1, 1, 1, 4),
    _TpMldFilterBindAddrId_Type()
)
tpMldFilterBindAddrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpMldFilterBindAddrId.setStatus("current")


class _TpMldFilterPortLag_Type(OctetString):
    """Custom type tpMldFilterPortLag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpMldFilterPortLag_Type.__name__ = "OctetString"
_TpMldFilterPortLag_Object = MibTableColumn
tpMldFilterPortLag = _TpMldFilterPortLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 2, 1, 1, 1, 5),
    _TpMldFilterPortLag_Type()
)
tpMldFilterPortLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpMldFilterPortLag.setStatus("current")
_TpMldPacketStatistic_ObjectIdentity = ObjectIdentity
tpMldPacketStatistic = _TpMldPacketStatistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 3)
)
_TpMldPktStat_ObjectIdentity = ObjectIdentity
tpMldPktStat = _TpMldPktStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 3, 1)
)
_TpMldPktStatTable_Object = MibTable
tpMldPktStatTable = _TpMldPktStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    tpMldPktStatTable.setStatus("current")
_TpMldPktStatEntry_Object = MibTableRow
tpMldPktStatEntry = _TpMldPktStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 3, 1, 1, 1)
)
tpMldPktStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tpMldPktStatEntry.setStatus("current")
_TpMldQueryPktStat_Type = Integer32
_TpMldQueryPktStat_Object = MibTableColumn
tpMldQueryPktStat = _TpMldQueryPktStat_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 3, 1, 1, 1, 2),
    _TpMldQueryPktStat_Type()
)
tpMldQueryPktStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpMldQueryPktStat.setStatus("current")
_TpMldReportV1PktStat_Type = Integer32
_TpMldReportV1PktStat_Object = MibTableColumn
tpMldReportV1PktStat = _TpMldReportV1PktStat_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 3, 1, 1, 1, 3),
    _TpMldReportV1PktStat_Type()
)
tpMldReportV1PktStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpMldReportV1PktStat.setStatus("current")
_TpMldReportV2PktStat_Type = Integer32
_TpMldReportV2PktStat_Object = MibTableColumn
tpMldReportV2PktStat = _TpMldReportV2PktStat_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 3, 1, 1, 1, 4),
    _TpMldReportV2PktStat_Type()
)
tpMldReportV2PktStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpMldReportV2PktStat.setStatus("current")
_TpMldDonePktStat_Type = Integer32
_TpMldDonePktStat_Object = MibTableColumn
tpMldDonePktStat = _TpMldDonePktStat_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 3, 1, 1, 1, 6),
    _TpMldDonePktStat_Type()
)
tpMldDonePktStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpMldDonePktStat.setStatus("current")
_TpMldErrorPktStat_Type = Integer32
_TpMldErrorPktStat_Object = MibTableColumn
tpMldErrorPktStat = _TpMldErrorPktStat_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 3, 1, 1, 1, 7),
    _TpMldErrorPktStat_Type()
)
tpMldErrorPktStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpMldErrorPktStat.setStatus("current")


class _TpIpMldPktStatClear_Type(Integer32):
    """Custom type tpIpMldPktStatClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("commit", 1)
    )


_TpIpMldPktStatClear_Type.__name__ = "Integer32"
_TpIpMldPktStatClear_Object = MibScalar
tpIpMldPktStatClear = _TpIpMldPktStatClear_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 3, 1, 2),
    _TpIpMldPktStatClear_Type()
)
tpIpMldPktStatClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpIpMldPktStatClear.setStatus("current")
_TpMldMultigroup_ObjectIdentity = ObjectIdentity
tpMldMultigroup = _TpMldMultigroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 4)
)
_TpMldMulticastGroups_ObjectIdentity = ObjectIdentity
tpMldMulticastGroups = _TpMldMulticastGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 4, 1)
)
_TpMldMulticastGroupTable_Object = MibTable
tpMldMulticastGroupTable = _TpMldMulticastGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    tpMldMulticastGroupTable.setStatus("current")
_TpMldMulticastGroupEntry_Object = MibTableRow
tpMldMulticastGroupEntry = _TpMldMulticastGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 4, 1, 1, 1)
)
tpMldMulticastGroupEntry.setIndexNames(
    (0, "TPLINK-MLDSNOOPING-MIB", "tpMldMulticastIP"),
    (0, "TPLINK-MLDSNOOPING-MIB", "tpMldVlanID"),
)
if mibBuilder.loadTexts:
    tpMldMulticastGroupEntry.setStatus("current")
_TpMldMulticastIP_Type = OctetString
_TpMldMulticastIP_Object = MibTableColumn
tpMldMulticastIP = _TpMldMulticastIP_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 4, 1, 1, 1, 1),
    _TpMldMulticastIP_Type()
)
tpMldMulticastIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpMldMulticastIP.setStatus("current")
_TpMldVlanID_Type = Integer32
_TpMldVlanID_Object = MibTableColumn
tpMldVlanID = _TpMldVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 4, 1, 1, 1, 2),
    _TpMldVlanID_Type()
)
tpMldVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpMldVlanID.setStatus("current")


class _TpMldForwardPorts_Type(OctetString):
    """Custom type tpMldForwardPorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_TpMldForwardPorts_Type.__name__ = "OctetString"
_TpMldForwardPorts_Object = MibTableColumn
tpMldForwardPorts = _TpMldForwardPorts_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 4, 1, 1, 1, 3),
    _TpMldForwardPorts_Type()
)
tpMldForwardPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpMldForwardPorts.setStatus("current")


class _TpMldGrouptype_Type(Integer32):
    """Custom type tpMldGrouptype based on Integer32"""
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


_TpMldGrouptype_Type.__name__ = "Integer32"
_TpMldGrouptype_Object = MibTableColumn
tpMldGrouptype = _TpMldGrouptype_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 4, 1, 1, 1, 4),
    _TpMldGrouptype_Type()
)
tpMldGrouptype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpMldGrouptype.setStatus("current")
_TpMldStaticMultigroup_ObjectIdentity = ObjectIdentity
tpMldStaticMultigroup = _TpMldStaticMultigroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 5)
)
_TpMldMulticastStaticGroups_ObjectIdentity = ObjectIdentity
tpMldMulticastStaticGroups = _TpMldMulticastStaticGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 5, 1)
)
_TpMldMulticastStaticGroupTable_Object = MibTable
tpMldMulticastStaticGroupTable = _TpMldMulticastStaticGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    tpMldMulticastStaticGroupTable.setStatus("current")
_TpMldMulticastStaticGroupEntry_Object = MibTableRow
tpMldMulticastStaticGroupEntry = _TpMldMulticastStaticGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 5, 1, 1, 1)
)
tpMldMulticastStaticGroupEntry.setIndexNames(
    (0, "TPLINK-MLDSNOOPING-MIB", "tpMldStaticMulticastIP"),
    (0, "TPLINK-MLDSNOOPING-MIB", "tpMldStaticVlanID"),
)
if mibBuilder.loadTexts:
    tpMldMulticastStaticGroupEntry.setStatus("current")
_TpMldStaticMulticastIP_Type = OctetString
_TpMldStaticMulticastIP_Object = MibTableColumn
tpMldStaticMulticastIP = _TpMldStaticMulticastIP_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 5, 1, 1, 1, 1),
    _TpMldStaticMulticastIP_Type()
)
tpMldStaticMulticastIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMldStaticMulticastIP.setStatus("current")
_TpMldStaticVlanID_Type = Integer32
_TpMldStaticVlanID_Object = MibTableColumn
tpMldStaticVlanID = _TpMldStaticVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 5, 1, 1, 1, 2),
    _TpMldStaticVlanID_Type()
)
tpMldStaticVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMldStaticVlanID.setStatus("current")


class _TpMldStaticForwardPorts_Type(OctetString):
    """Custom type tpMldStaticForwardPorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_TpMldStaticForwardPorts_Type.__name__ = "OctetString"
_TpMldStaticForwardPorts_Object = MibTableColumn
tpMldStaticForwardPorts = _TpMldStaticForwardPorts_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 5, 1, 1, 1, 3),
    _TpMldStaticForwardPorts_Type()
)
tpMldStaticForwardPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMldStaticForwardPorts.setStatus("current")
_TpMldStaticGroupStatus_Type = TPRowStatus
_TpMldStaticGroupStatus_Object = MibTableColumn
tpMldStaticGroupStatus = _TpMldStaticGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 1, 5, 1, 1, 1, 4),
    _TpMldStaticGroupStatus_Type()
)
tpMldStaticGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMldStaticGroupStatus.setStatus("current")
_TplinkMldSnoopingNotifications_ObjectIdentity = ObjectIdentity
tplinkMldSnoopingNotifications = _TplinkMldSnoopingNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 43, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-MLDSNOOPING-MIB",
    **{"tplinkMldSnoopingMIB": tplinkMldSnoopingMIB,
       "tplinkMldSnoopingMIBObjects": tplinkMldSnoopingMIBObjects,
       "tpMldSnooping": tpMldSnooping,
       "tpMldSnoopingGlobalConfig": tpMldSnoopingGlobalConfig,
       "tpMldSnoopingEnable": tpMldSnoopingEnable,
       "tpMldUnknownMulticastPacket": tpMldUnknownMulticastPacket,
       "tpMldUnknownReportSuppression": tpMldUnknownReportSuppression,
       "tpMldGlobalRouterTime": tpMldGlobalRouterTime,
       "tpMldGlobalMemberTime": tpMldGlobalMemberTime,
       "tpMldlastListenerQueryInterval": tpMldlastListenerQueryInterval,
       "tpMldlastListenerQueryCount": tpMldlastListenerQueryCount,
       "tpMldPortConfig": tpMldPortConfig,
       "tpMldPortTable": tpMldPortTable,
       "tpMldPortEntry": tpMldPortEntry,
       "tpMldSnoopingPortEnable": tpMldSnoopingPortEnable,
       "tpMldFastLeavePortEnable": tpMldFastLeavePortEnable,
       "tpMldPortLag": tpMldPortLag,
       "tpMldVlanConfig": tpMldVlanConfig,
       "tpMldVlanTable": tpMldVlanTable,
       "tpMldVlanEntry": tpMldVlanEntry,
       "tpMldVlanId": tpMldVlanId,
       "tpMldRouterTime": tpMldRouterTime,
       "tpMldMemberTime": tpMldMemberTime,
       "tpMldRouterPort": tpMldRouterPort,
       "tpMldForbiddenRouterPort": tpMldForbiddenRouterPort,
       "tpMldVlanStatus": tpMldVlanStatus,
       "tpMldMultiVlanConfig": tpMldMultiVlanConfig,
       "tpMldMultiVlanId": tpMldMultiVlanId,
       "tpMldMultitRouterTime": tpMldMultitRouterTime,
       "tpMldMultiMemberTime": tpMldMultiMemberTime,
       "tpMldMultiRouterPort": tpMldMultiRouterPort,
       "tpMldMultiForbiddenRouterPort": tpMldMultiForbiddenRouterPort,
       "tpMldMultiReplaceSrcIp": tpMldMultiReplaceSrcIp,
       "tpMldQuerierConfig": tpMldQuerierConfig,
       "mldQuerierTable": mldQuerierTable,
       "mldQuerierEntry": mldQuerierEntry,
       "mldQuerierVlanId": mldQuerierVlanId,
       "mldQueryInterval": mldQueryInterval,
       "mldMaxResponseTime": mldMaxResponseTime,
       "mldGeneralQuerySrcIp": mldGeneralQuerySrcIp,
       "mldQuerierStatus": mldQuerierStatus,
       "tpMldFilter": tpMldFilter,
       "tpMldPortFilterConfig": tpMldPortFilterConfig,
       "tpMldFilterPortTable": tpMldFilterPortTable,
       "tpMldFilterPortEntry": tpMldFilterPortEntry,
       "tpMldFilterMaxGroup": tpMldFilterMaxGroup,
       "tpMldFilterMaxGroupAction": tpMldFilterMaxGroupAction,
       "tpMldFilterBindAddrId": tpMldFilterBindAddrId,
       "tpMldFilterPortLag": tpMldFilterPortLag,
       "tpMldPacketStatistic": tpMldPacketStatistic,
       "tpMldPktStat": tpMldPktStat,
       "tpMldPktStatTable": tpMldPktStatTable,
       "tpMldPktStatEntry": tpMldPktStatEntry,
       "tpMldQueryPktStat": tpMldQueryPktStat,
       "tpMldReportV1PktStat": tpMldReportV1PktStat,
       "tpMldReportV2PktStat": tpMldReportV2PktStat,
       "tpMldDonePktStat": tpMldDonePktStat,
       "tpMldErrorPktStat": tpMldErrorPktStat,
       "tpIpMldPktStatClear": tpIpMldPktStatClear,
       "tpMldMultigroup": tpMldMultigroup,
       "tpMldMulticastGroups": tpMldMulticastGroups,
       "tpMldMulticastGroupTable": tpMldMulticastGroupTable,
       "tpMldMulticastGroupEntry": tpMldMulticastGroupEntry,
       "tpMldMulticastIP": tpMldMulticastIP,
       "tpMldVlanID": tpMldVlanID,
       "tpMldForwardPorts": tpMldForwardPorts,
       "tpMldGrouptype": tpMldGrouptype,
       "tpMldStaticMultigroup": tpMldStaticMultigroup,
       "tpMldMulticastStaticGroups": tpMldMulticastStaticGroups,
       "tpMldMulticastStaticGroupTable": tpMldMulticastStaticGroupTable,
       "tpMldMulticastStaticGroupEntry": tpMldMulticastStaticGroupEntry,
       "tpMldStaticMulticastIP": tpMldStaticMulticastIP,
       "tpMldStaticVlanID": tpMldStaticVlanID,
       "tpMldStaticForwardPorts": tpMldStaticForwardPorts,
       "tpMldStaticGroupStatus": tpMldStaticGroupStatus,
       "tplinkMldSnoopingNotifications": tplinkMldSnoopingNotifications}
)
