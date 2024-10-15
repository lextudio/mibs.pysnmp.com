# SNMP MIB module (CISCO-SWITCH-ENGINE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SWITCH-ENGINE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:04 2024
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

(CiscoNetworkProtocol,
 CiscoPort) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoNetworkProtocol",
    "CiscoPort")

(VlanIndex,) = mibBuilder.importSymbols(
    "CISCO-VTP-MIB",
    "VlanIndex")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(InterfaceIndexOrZero,
 OwnerString,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "OwnerString",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(MplsVpnId,) = mibBuilder.importSymbols(
    "MPLS-VPN-MIB",
    "MplsVpnId")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoSwitchEngineMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 97)
)
ciscoSwitchEngineMIB.setRevisions(
        ("2013-02-13 00:00",
         "2012-03-12 00:00",
         "2010-12-17 00:00",
         "2008-11-11 00:00",
         "2008-01-29 00:00",
         "2005-09-16 00:00",
         "2005-04-12 00:00",
         "2004-11-15 00:00",
         "2004-06-09 00:00",
         "2003-11-07 00:00",
         "2003-08-20 00:00",
         "2003-06-10 00:00",
         "2003-05-06 00:00",
         "2003-02-21 00:00",
         "2002-08-05 00:00",
         "2002-02-07 00:00",
         "2001-10-26 00:00",
         "2001-09-13 00:00",
         "2001-05-16 00:00",
         "2001-03-09 00:00",
         "2000-06-23 00:00",
         "2000-01-31 11:30",
         "1999-12-09 11:30",
         "1998-06-24 11:30",
         "1998-05-28 11:30")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoGauge64(Counter64, TextualConvention):
    status = "current"


class ControlStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )



class McastGroupIp(IpAddress, TextualConvention):
    status = "current"
    displayHint = "1d.1d.1d.1d"


class FlowAddressComponent(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
        ValueSizeConstraint(10, 10),
    )



# MIB Managed Objects in the order of their OIDs

_CseMIBObjects_ObjectIdentity = ObjectIdentity
cseMIBObjects = _CseMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1)
)
_CseL2Objects_ObjectIdentity = ObjectIdentity
cseL2Objects = _CseL2Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 1)
)
_CseL2StatsTable_Object = MibTable
cseL2StatsTable = _CseL2StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cseL2StatsTable.setStatus("current")
_CseL2StatsEntry_Object = MibTableRow
cseL2StatsEntry = _CseL2StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 1, 1, 1)
)
cseL2StatsEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cseL2StatsEntry.setStatus("current")
_CseL2ForwardedLocalPkts_Type = Counter32
_CseL2ForwardedLocalPkts_Object = MibTableColumn
cseL2ForwardedLocalPkts = _CseL2ForwardedLocalPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 1, 1, 1, 1),
    _CseL2ForwardedLocalPkts_Type()
)
cseL2ForwardedLocalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseL2ForwardedLocalPkts.setStatus("current")
_CseL2ForwardedLocalOctets_Type = Counter64
_CseL2ForwardedLocalOctets_Object = MibTableColumn
cseL2ForwardedLocalOctets = _CseL2ForwardedLocalOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 1, 1, 1, 2),
    _CseL2ForwardedLocalOctets_Type()
)
cseL2ForwardedLocalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseL2ForwardedLocalOctets.setStatus("current")
_CseL2ForwardedTotalPkts_Type = Counter32
_CseL2ForwardedTotalPkts_Object = MibTableColumn
cseL2ForwardedTotalPkts = _CseL2ForwardedTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 1, 1, 1, 3),
    _CseL2ForwardedTotalPkts_Type()
)
cseL2ForwardedTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseL2ForwardedTotalPkts.setStatus("current")
_CseL2NewAddressLearns_Type = Counter32
_CseL2NewAddressLearns_Object = MibTableColumn
cseL2NewAddressLearns = _CseL2NewAddressLearns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 1, 1, 1, 4),
    _CseL2NewAddressLearns_Type()
)
cseL2NewAddressLearns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseL2NewAddressLearns.setStatus("current")
_CseL2AddrLearnFailures_Type = Counter32
_CseL2AddrLearnFailures_Object = MibTableColumn
cseL2AddrLearnFailures = _CseL2AddrLearnFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 1, 1, 1, 5),
    _CseL2AddrLearnFailures_Type()
)
cseL2AddrLearnFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseL2AddrLearnFailures.setStatus("current")
_CseL2DstAddrLookupMisses_Type = Counter32
_CseL2DstAddrLookupMisses_Object = MibTableColumn
cseL2DstAddrLookupMisses = _CseL2DstAddrLookupMisses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 1, 1, 1, 6),
    _CseL2DstAddrLookupMisses_Type()
)
cseL2DstAddrLookupMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseL2DstAddrLookupMisses.setStatus("current")
_CseL2IpPkts_Type = Counter32
_CseL2IpPkts_Object = MibTableColumn
cseL2IpPkts = _CseL2IpPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 1, 1, 1, 7),
    _CseL2IpPkts_Type()
)
cseL2IpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseL2IpPkts.setStatus("current")
_CseL2IpxPkts_Type = Counter32
_CseL2IpxPkts_Object = MibTableColumn
cseL2IpxPkts = _CseL2IpxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 1, 1, 1, 8),
    _CseL2IpxPkts_Type()
)
cseL2IpxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseL2IpxPkts.setStatus("current")
_CseL2AssignedProtoPkts_Type = Counter32
_CseL2AssignedProtoPkts_Object = MibTableColumn
cseL2AssignedProtoPkts = _CseL2AssignedProtoPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 1, 1, 1, 9),
    _CseL2AssignedProtoPkts_Type()
)
cseL2AssignedProtoPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseL2AssignedProtoPkts.setStatus("current")
_CseL2OtherProtoPkts_Type = Counter32
_CseL2OtherProtoPkts_Object = MibTableColumn
cseL2OtherProtoPkts = _CseL2OtherProtoPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 1, 1, 1, 10),
    _CseL2OtherProtoPkts_Type()
)
cseL2OtherProtoPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseL2OtherProtoPkts.setStatus("current")
_CseL2StatsHCTable_Object = MibTable
cseL2StatsHCTable = _CseL2StatsHCTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cseL2StatsHCTable.setStatus("current")
_CseL2StatsHCEntry_Object = MibTableRow
cseL2StatsHCEntry = _CseL2StatsHCEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 1, 2, 1)
)
cseL2StatsHCEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cseL2StatsHCEntry.setStatus("current")
_CseL2HCOverflowForwardedLocalPkts_Type = Counter32
_CseL2HCOverflowForwardedLocalPkts_Object = MibTableColumn
cseL2HCOverflowForwardedLocalPkts = _CseL2HCOverflowForwardedLocalPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 1, 2, 1, 1),
    _CseL2HCOverflowForwardedLocalPkts_Type()
)
cseL2HCOverflowForwardedLocalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseL2HCOverflowForwardedLocalPkts.setStatus("current")
_CseL2HCForwardedLocalPkts_Type = Counter64
_CseL2HCForwardedLocalPkts_Object = MibTableColumn
cseL2HCForwardedLocalPkts = _CseL2HCForwardedLocalPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 1, 2, 1, 2),
    _CseL2HCForwardedLocalPkts_Type()
)
cseL2HCForwardedLocalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseL2HCForwardedLocalPkts.setStatus("current")
_CseL2HCOverflowForwardedTotalPkts_Type = Counter32
_CseL2HCOverflowForwardedTotalPkts_Object = MibTableColumn
cseL2HCOverflowForwardedTotalPkts = _CseL2HCOverflowForwardedTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 1, 2, 1, 3),
    _CseL2HCOverflowForwardedTotalPkts_Type()
)
cseL2HCOverflowForwardedTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseL2HCOverflowForwardedTotalPkts.setStatus("current")
_CseL2HCForwardedTotalPkts_Type = Counter64
_CseL2HCForwardedTotalPkts_Object = MibTableColumn
cseL2HCForwardedTotalPkts = _CseL2HCForwardedTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 1, 2, 1, 4),
    _CseL2HCForwardedTotalPkts_Type()
)
cseL2HCForwardedTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseL2HCForwardedTotalPkts.setStatus("current")
_CseL2HCOverflowIpPkts_Type = Counter32
_CseL2HCOverflowIpPkts_Object = MibTableColumn
cseL2HCOverflowIpPkts = _CseL2HCOverflowIpPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 1, 2, 1, 5),
    _CseL2HCOverflowIpPkts_Type()
)
cseL2HCOverflowIpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseL2HCOverflowIpPkts.setStatus("current")
_CseL2HCIpPkts_Type = Counter64
_CseL2HCIpPkts_Object = MibTableColumn
cseL2HCIpPkts = _CseL2HCIpPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 1, 2, 1, 6),
    _CseL2HCIpPkts_Type()
)
cseL2HCIpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseL2HCIpPkts.setStatus("current")
_CseL2HCOverflowIpxPkts_Type = Counter32
_CseL2HCOverflowIpxPkts_Object = MibTableColumn
cseL2HCOverflowIpxPkts = _CseL2HCOverflowIpxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 1, 2, 1, 7),
    _CseL2HCOverflowIpxPkts_Type()
)
cseL2HCOverflowIpxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseL2HCOverflowIpxPkts.setStatus("current")
_CseL2HCIpxPkts_Type = Counter64
_CseL2HCIpxPkts_Object = MibTableColumn
cseL2HCIpxPkts = _CseL2HCIpxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 1, 2, 1, 8),
    _CseL2HCIpxPkts_Type()
)
cseL2HCIpxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseL2HCIpxPkts.setStatus("current")
_CseL2HCOverflowAssignedProtoPkts_Type = Counter32
_CseL2HCOverflowAssignedProtoPkts_Object = MibTableColumn
cseL2HCOverflowAssignedProtoPkts = _CseL2HCOverflowAssignedProtoPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 1, 2, 1, 9),
    _CseL2HCOverflowAssignedProtoPkts_Type()
)
cseL2HCOverflowAssignedProtoPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseL2HCOverflowAssignedProtoPkts.setStatus("current")
_CseL2HCAssignedProtoPkts_Type = Counter64
_CseL2HCAssignedProtoPkts_Object = MibTableColumn
cseL2HCAssignedProtoPkts = _CseL2HCAssignedProtoPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 1, 2, 1, 10),
    _CseL2HCAssignedProtoPkts_Type()
)
cseL2HCAssignedProtoPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseL2HCAssignedProtoPkts.setStatus("current")
_CseL2HCOverflowOtherProtoPkts_Type = Counter32
_CseL2HCOverflowOtherProtoPkts_Object = MibTableColumn
cseL2HCOverflowOtherProtoPkts = _CseL2HCOverflowOtherProtoPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 1, 2, 1, 11),
    _CseL2HCOverflowOtherProtoPkts_Type()
)
cseL2HCOverflowOtherProtoPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseL2HCOverflowOtherProtoPkts.setStatus("current")
_CseL2HCOtherProtoPkts_Type = Counter64
_CseL2HCOtherProtoPkts_Object = MibTableColumn
cseL2HCOtherProtoPkts = _CseL2HCOtherProtoPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 1, 2, 1, 12),
    _CseL2HCOtherProtoPkts_Type()
)
cseL2HCOtherProtoPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseL2HCOtherProtoPkts.setStatus("current")
_CseFlow_ObjectIdentity = ObjectIdentity
cseFlow = _CseFlow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2)
)


class _CseFlowEstablishedAgingTime_Type(Integer32):
    """Custom type cseFlowEstablishedAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CseFlowEstablishedAgingTime_Type.__name__ = "Integer32"
_CseFlowEstablishedAgingTime_Object = MibScalar
cseFlowEstablishedAgingTime = _CseFlowEstablishedAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 1),
    _CseFlowEstablishedAgingTime_Type()
)
cseFlowEstablishedAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cseFlowEstablishedAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    cseFlowEstablishedAgingTime.setUnits("seconds")
_CseFlowFastAgingTime_Type = Unsigned32
_CseFlowFastAgingTime_Object = MibScalar
cseFlowFastAgingTime = _CseFlowFastAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 2),
    _CseFlowFastAgingTime_Type()
)
cseFlowFastAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cseFlowFastAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    cseFlowFastAgingTime.setUnits("seconds")
_CseFlowFastAgePktThreshold_Type = Unsigned32
_CseFlowFastAgePktThreshold_Object = MibScalar
cseFlowFastAgePktThreshold = _CseFlowFastAgePktThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 3),
    _CseFlowFastAgePktThreshold_Type()
)
cseFlowFastAgePktThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cseFlowFastAgePktThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cseFlowFastAgePktThreshold.setUnits("packets")
_CseRouterTable_Object = MibTable
cseRouterTable = _CseRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cseRouterTable.setStatus("current")
_CseRouterEntry_Object = MibTableRow
cseRouterEntry = _CseRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 4, 1)
)
cseRouterEntry.setIndexNames(
    (0, "CISCO-SWITCH-ENGINE-MIB", "cseRouterIndex"),
)
if mibBuilder.loadTexts:
    cseRouterEntry.setStatus("current")
_CseRouterIndex_Type = IpAddress
_CseRouterIndex_Object = MibTableColumn
cseRouterIndex = _CseRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 4, 1, 1),
    _CseRouterIndex_Type()
)
cseRouterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cseRouterIndex.setStatus("current")


class _CseRouterFlowMask_Type(Integer32):
    """Custom type cseRouterFlowMask based on Integer32"""
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
        *(("dstOnly", 1),
          ("fullFlow", 3),
          ("notApplicable", 4),
          ("srcDst", 2),
          ("srcDstVlan", 5))
    )


_CseRouterFlowMask_Type.__name__ = "Integer32"
_CseRouterFlowMask_Object = MibTableColumn
cseRouterFlowMask = _CseRouterFlowMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 4, 1, 2),
    _CseRouterFlowMask_Type()
)
cseRouterFlowMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseRouterFlowMask.setStatus("current")
_CseRouterName_Type = DisplayString
_CseRouterName_Object = MibTableColumn
cseRouterName = _CseRouterName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 4, 1, 3),
    _CseRouterName_Type()
)
cseRouterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseRouterName.setStatus("current")
_CseRouterStatic_Type = TruthValue
_CseRouterStatic_Object = MibTableColumn
cseRouterStatic = _CseRouterStatic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 4, 1, 4),
    _CseRouterStatic_Type()
)
cseRouterStatic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseRouterStatic.setStatus("current")


class _CseRouterIpxFlowMask_Type(Integer32):
    """Custom type cseRouterIpxFlowMask based on Integer32"""
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
        *(("dstOnly", 1),
          ("fullFlow", 3),
          ("notApplicable", 4),
          ("srcDst", 2))
    )


_CseRouterIpxFlowMask_Type.__name__ = "Integer32"
_CseRouterIpxFlowMask_Object = MibTableColumn
cseRouterIpxFlowMask = _CseRouterIpxFlowMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 4, 1, 5),
    _CseRouterIpxFlowMask_Type()
)
cseRouterIpxFlowMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseRouterIpxFlowMask.setStatus("current")
_CseStaticExtRouterTable_Object = MibTable
cseStaticExtRouterTable = _CseStaticExtRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 5)
)
if mibBuilder.loadTexts:
    cseStaticExtRouterTable.setStatus("current")
_CseStaticExtRouterEntry_Object = MibTableRow
cseStaticExtRouterEntry = _CseStaticExtRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 5, 1)
)
cseStaticExtRouterEntry.setIndexNames(
    (0, "CISCO-SWITCH-ENGINE-MIB", "cseRouterIndex"),
)
if mibBuilder.loadTexts:
    cseStaticExtRouterEntry.setStatus("current")
_CseStaticRouterName_Type = DisplayString
_CseStaticRouterName_Object = MibTableColumn
cseStaticRouterName = _CseStaticRouterName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 5, 1, 1),
    _CseStaticRouterName_Type()
)
cseStaticRouterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseStaticRouterName.setStatus("current")
_CseStaticRouterOwner_Type = OwnerString
_CseStaticRouterOwner_Object = MibTableColumn
cseStaticRouterOwner = _CseStaticRouterOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 5, 1, 2),
    _CseStaticRouterOwner_Type()
)
cseStaticRouterOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseStaticRouterOwner.setStatus("current")
_CseStaticRouterStatus_Type = RowStatus
_CseStaticRouterStatus_Object = MibTableColumn
cseStaticRouterStatus = _CseStaticRouterStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 5, 1, 3),
    _CseStaticRouterStatus_Type()
)
cseStaticRouterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseStaticRouterStatus.setStatus("current")


class _CseStaticRouterType_Type(Bits):
    """Custom type cseStaticRouterType based on Bits"""
    defaultBinValue = "1"

    namedValues = NamedValues(
        *(("multicast", 1),
          ("unicast", 0))
    )

_CseStaticRouterType_Type.__name__ = "Bits"
_CseStaticRouterType_Object = MibTableColumn
cseStaticRouterType = _CseStaticRouterType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 5, 1, 4),
    _CseStaticRouterType_Type()
)
cseStaticRouterType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseStaticRouterType.setStatus("current")
_CseRouterVlanTable_Object = MibTable
cseRouterVlanTable = _CseRouterVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 6)
)
if mibBuilder.loadTexts:
    cseRouterVlanTable.setStatus("current")
_CseRouterVlanEntry_Object = MibTableRow
cseRouterVlanEntry = _CseRouterVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 6, 1)
)
cseRouterVlanEntry.setIndexNames(
    (0, "CISCO-SWITCH-ENGINE-MIB", "cseRouterIndex"),
    (0, "CISCO-SWITCH-ENGINE-MIB", "cseRouterMac"),
    (0, "CISCO-SWITCH-ENGINE-MIB", "cseRouterVlan"),
)
if mibBuilder.loadTexts:
    cseRouterVlanEntry.setStatus("current")
_CseRouterMac_Type = MacAddress
_CseRouterMac_Object = MibTableColumn
cseRouterMac = _CseRouterMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 6, 1, 1),
    _CseRouterMac_Type()
)
cseRouterMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseRouterMac.setStatus("current")
_CseRouterVlan_Type = VlanIndex
_CseRouterVlan_Object = MibTableColumn
cseRouterVlan = _CseRouterVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 6, 1, 2),
    _CseRouterVlan_Type()
)
cseRouterVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cseRouterVlan.setStatus("current")


class _CseRouterProtocol_Type(Bits):
    """Custom type cseRouterProtocol based on Bits"""
    namedValues = NamedValues(
        *(("ip", 0),
          ("ipx", 1))
    )

_CseRouterProtocol_Type.__name__ = "Bits"
_CseRouterProtocol_Object = MibTableColumn
cseRouterProtocol = _CseRouterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 6, 1, 3),
    _CseRouterProtocol_Type()
)
cseRouterProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseRouterProtocol.setStatus("current")
_CseFlowMaxQueries_Type = Unsigned32
_CseFlowMaxQueries_Object = MibScalar
cseFlowMaxQueries = _CseFlowMaxQueries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 7),
    _CseFlowMaxQueries_Type()
)
cseFlowMaxQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowMaxQueries.setStatus("current")
_CseFlowQueryTable_Object = MibTable
cseFlowQueryTable = _CseFlowQueryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 8)
)
if mibBuilder.loadTexts:
    cseFlowQueryTable.setStatus("current")
_CseFlowQueryEntry_Object = MibTableRow
cseFlowQueryEntry = _CseFlowQueryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 8, 1)
)
cseFlowQueryEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-SWITCH-ENGINE-MIB", "cseFlowQueryIndex"),
)
if mibBuilder.loadTexts:
    cseFlowQueryEntry.setStatus("current")
_CseFlowQueryIndex_Type = Unsigned32
_CseFlowQueryIndex_Object = MibTableColumn
cseFlowQueryIndex = _CseFlowQueryIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 8, 1, 1),
    _CseFlowQueryIndex_Type()
)
cseFlowQueryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cseFlowQueryIndex.setStatus("current")


class _CseFlowQueryMask_Type(Integer32):
    """Custom type cseFlowQueryMask based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("any", 7),
          ("dstOnly", 1),
          ("fullFlow", 4),
          ("ipxDstOnly", 5),
          ("ipxSrcAndDst", 6),
          ("srcAndDst", 3),
          ("srcOrDst", 2))
    )


_CseFlowQueryMask_Type.__name__ = "Integer32"
_CseFlowQueryMask_Object = MibTableColumn
cseFlowQueryMask = _CseFlowQueryMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 8, 1, 2),
    _CseFlowQueryMask_Type()
)
cseFlowQueryMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseFlowQueryMask.setStatus("current")


class _CseFlowQueryTransport_Type(Bits):
    """Custom type cseFlowQueryTransport based on Bits"""
    defaultBinValue = "11"

    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 0))
    )

_CseFlowQueryTransport_Type.__name__ = "Bits"
_CseFlowQueryTransport_Object = MibTableColumn
cseFlowQueryTransport = _CseFlowQueryTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 8, 1, 3),
    _CseFlowQueryTransport_Type()
)
cseFlowQueryTransport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseFlowQueryTransport.setStatus("current")


class _CseFlowQuerySource_Type(FlowAddressComponent):
    """Custom type cseFlowQuerySource based on FlowAddressComponent"""
    defaultHexValue = "000000000000"


_CseFlowQuerySource_Object = MibTableColumn
cseFlowQuerySource = _CseFlowQuerySource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 8, 1, 4),
    _CseFlowQuerySource_Type()
)
cseFlowQuerySource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseFlowQuerySource.setStatus("current")


class _CseFlowQuerySourceMask_Type(FlowAddressComponent):
    """Custom type cseFlowQuerySourceMask based on FlowAddressComponent"""
    defaultHexValue = "FFFFFFFFFFFF"


_CseFlowQuerySourceMask_Object = MibTableColumn
cseFlowQuerySourceMask = _CseFlowQuerySourceMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 8, 1, 5),
    _CseFlowQuerySourceMask_Type()
)
cseFlowQuerySourceMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseFlowQuerySourceMask.setStatus("current")


class _CseFlowQueryDestination_Type(FlowAddressComponent):
    """Custom type cseFlowQueryDestination based on FlowAddressComponent"""
    defaultHexValue = "000000000000"


_CseFlowQueryDestination_Object = MibTableColumn
cseFlowQueryDestination = _CseFlowQueryDestination_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 8, 1, 6),
    _CseFlowQueryDestination_Type()
)
cseFlowQueryDestination.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseFlowQueryDestination.setStatus("current")


class _CseFlowQueryDestinationMask_Type(FlowAddressComponent):
    """Custom type cseFlowQueryDestinationMask based on FlowAddressComponent"""
    defaultHexValue = "FFFFFFFFFFFF"


_CseFlowQueryDestinationMask_Object = MibTableColumn
cseFlowQueryDestinationMask = _CseFlowQueryDestinationMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 8, 1, 7),
    _CseFlowQueryDestinationMask_Type()
)
cseFlowQueryDestinationMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseFlowQueryDestinationMask.setStatus("current")
_CseFlowQueryRouterIndex_Type = IpAddress
_CseFlowQueryRouterIndex_Object = MibTableColumn
cseFlowQueryRouterIndex = _CseFlowQueryRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 8, 1, 8),
    _CseFlowQueryRouterIndex_Type()
)
cseFlowQueryRouterIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseFlowQueryRouterIndex.setStatus("current")
_CseFlowQueryOwner_Type = OwnerString
_CseFlowQueryOwner_Object = MibTableColumn
cseFlowQueryOwner = _CseFlowQueryOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 8, 1, 9),
    _CseFlowQueryOwner_Type()
)
cseFlowQueryOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseFlowQueryOwner.setStatus("current")


class _CseFlowQueryResultingRows_Type(Integer32):
    """Custom type cseFlowQueryResultingRows based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_CseFlowQueryResultingRows_Type.__name__ = "Integer32"
_CseFlowQueryResultingRows_Object = MibTableColumn
cseFlowQueryResultingRows = _CseFlowQueryResultingRows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 8, 1, 10),
    _CseFlowQueryResultingRows_Type()
)
cseFlowQueryResultingRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowQueryResultingRows.setStatus("current")
_CseFlowQueryResultTotalPkts_Type = CiscoGauge64
_CseFlowQueryResultTotalPkts_Object = MibTableColumn
cseFlowQueryResultTotalPkts = _CseFlowQueryResultTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 8, 1, 11),
    _CseFlowQueryResultTotalPkts_Type()
)
cseFlowQueryResultTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowQueryResultTotalPkts.setStatus("current")
_CseFlowQueryResultTotalOctets_Type = CiscoGauge64
_CseFlowQueryResultTotalOctets_Object = MibTableColumn
cseFlowQueryResultTotalOctets = _CseFlowQueryResultTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 8, 1, 12),
    _CseFlowQueryResultTotalOctets_Type()
)
cseFlowQueryResultTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowQueryResultTotalOctets.setStatus("current")
_CseFlowQueryResultAvgDuration_Type = TimeInterval
_CseFlowQueryResultAvgDuration_Object = MibTableColumn
cseFlowQueryResultAvgDuration = _CseFlowQueryResultAvgDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 8, 1, 13),
    _CseFlowQueryResultAvgDuration_Type()
)
cseFlowQueryResultAvgDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowQueryResultAvgDuration.setStatus("current")
_CseFlowQueryResultAvgIdle_Type = TimeInterval
_CseFlowQueryResultAvgIdle_Object = MibTableColumn
cseFlowQueryResultAvgIdle = _CseFlowQueryResultAvgIdle_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 8, 1, 14),
    _CseFlowQueryResultAvgIdle_Type()
)
cseFlowQueryResultAvgIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowQueryResultAvgIdle.setStatus("current")
_CseFlowQueryStatus_Type = RowStatus
_CseFlowQueryStatus_Object = MibTableColumn
cseFlowQueryStatus = _CseFlowQueryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 8, 1, 15),
    _CseFlowQueryStatus_Type()
)
cseFlowQueryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseFlowQueryStatus.setStatus("current")
_CseFlowQueryCreateTime_Type = TimeStamp
_CseFlowQueryCreateTime_Object = MibTableColumn
cseFlowQueryCreateTime = _CseFlowQueryCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 8, 1, 16),
    _CseFlowQueryCreateTime_Type()
)
cseFlowQueryCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowQueryCreateTime.setStatus("current")
_CseFlowQueryTotalFlows_Type = Unsigned32
_CseFlowQueryTotalFlows_Object = MibTableColumn
cseFlowQueryTotalFlows = _CseFlowQueryTotalFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 8, 1, 17),
    _CseFlowQueryTotalFlows_Type()
)
cseFlowQueryTotalFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowQueryTotalFlows.setStatus("current")


class _CseFlowQuerySkipNFlows_Type(Integer32):
    """Custom type cseFlowQuerySkipNFlows based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CseFlowQuerySkipNFlows_Type.__name__ = "Integer32"
_CseFlowQuerySkipNFlows_Object = MibTableColumn
cseFlowQuerySkipNFlows = _CseFlowQuerySkipNFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 8, 1, 18),
    _CseFlowQuerySkipNFlows_Type()
)
cseFlowQuerySkipNFlows.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseFlowQuerySkipNFlows.setStatus("current")
_CseFlowDataTable_Object = MibTable
cseFlowDataTable = _CseFlowDataTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 9)
)
if mibBuilder.loadTexts:
    cseFlowDataTable.setStatus("current")
_CseFlowDataEntry_Object = MibTableRow
cseFlowDataEntry = _CseFlowDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 9, 1)
)
cseFlowDataEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-SWITCH-ENGINE-MIB", "cseFlowQueryIndex"),
    (0, "CISCO-SWITCH-ENGINE-MIB", "cseFlowDataIndex"),
)
if mibBuilder.loadTexts:
    cseFlowDataEntry.setStatus("current")
_CseFlowDataIndex_Type = Unsigned32
_CseFlowDataIndex_Object = MibTableColumn
cseFlowDataIndex = _CseFlowDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 9, 1, 1),
    _CseFlowDataIndex_Type()
)
cseFlowDataIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cseFlowDataIndex.setStatus("current")
_CseFlowDataSrcMac_Type = MacAddress
_CseFlowDataSrcMac_Object = MibTableColumn
cseFlowDataSrcMac = _CseFlowDataSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 9, 1, 2),
    _CseFlowDataSrcMac_Type()
)
cseFlowDataSrcMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowDataSrcMac.setStatus("current")
_CseFlowDataDstMac_Type = MacAddress
_CseFlowDataDstMac_Object = MibTableColumn
cseFlowDataDstMac = _CseFlowDataDstMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 9, 1, 3),
    _CseFlowDataDstMac_Type()
)
cseFlowDataDstMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowDataDstMac.setStatus("current")
_CseFlowDataStaticFlow_Type = TruthValue
_CseFlowDataStaticFlow_Object = MibTableColumn
cseFlowDataStaticFlow = _CseFlowDataStaticFlow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 9, 1, 4),
    _CseFlowDataStaticFlow_Type()
)
cseFlowDataStaticFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowDataStaticFlow.setStatus("current")


class _CseFlowDataEncapType_Type(Integer32):
    """Custom type cseFlowDataEncapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ipArpa", 1),
          ("ipx802raw", 3),
          ("ipx802sap", 4),
          ("ipx802snap", 5),
          ("ipxEthernet", 2),
          ("other", 6))
    )


_CseFlowDataEncapType_Type.__name__ = "Integer32"
_CseFlowDataEncapType_Object = MibTableColumn
cseFlowDataEncapType = _CseFlowDataEncapType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 9, 1, 5),
    _CseFlowDataEncapType_Type()
)
cseFlowDataEncapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowDataEncapType.setStatus("current")
_CseFlowDataSource_Type = FlowAddressComponent
_CseFlowDataSource_Object = MibTableColumn
cseFlowDataSource = _CseFlowDataSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 9, 1, 6),
    _CseFlowDataSource_Type()
)
cseFlowDataSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowDataSource.setStatus("current")
_CseFlowDataDestination_Type = FlowAddressComponent
_CseFlowDataDestination_Object = MibTableColumn
cseFlowDataDestination = _CseFlowDataDestination_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 9, 1, 7),
    _CseFlowDataDestination_Type()
)
cseFlowDataDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowDataDestination.setStatus("current")
_CseFlowDataDestVlan_Type = VlanIndex
_CseFlowDataDestVlan_Object = MibTableColumn
cseFlowDataDestVlan = _CseFlowDataDestVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 9, 1, 8),
    _CseFlowDataDestVlan_Type()
)
cseFlowDataDestVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowDataDestVlan.setStatus("current")


class _CseFlowDataIpQOS_Type(Integer32):
    """Custom type cseFlowDataIpQOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CseFlowDataIpQOS_Type.__name__ = "Integer32"
_CseFlowDataIpQOS_Object = MibTableColumn
cseFlowDataIpQOS = _CseFlowDataIpQOS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 9, 1, 9),
    _CseFlowDataIpQOS_Type()
)
cseFlowDataIpQOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowDataIpQOS.setStatus("current")


class _CseFlowDataIpQOSPolicy_Type(Integer32):
    """Custom type cseFlowDataIpQOSPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CseFlowDataIpQOSPolicy_Type.__name__ = "Integer32"
_CseFlowDataIpQOSPolicy_Object = MibTableColumn
cseFlowDataIpQOSPolicy = _CseFlowDataIpQOSPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 9, 1, 10),
    _CseFlowDataIpQOSPolicy_Type()
)
cseFlowDataIpQOSPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowDataIpQOSPolicy.setStatus("current")
_CseFlowDataWhenCreated_Type = TimeStamp
_CseFlowDataWhenCreated_Object = MibTableColumn
cseFlowDataWhenCreated = _CseFlowDataWhenCreated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 9, 1, 11),
    _CseFlowDataWhenCreated_Type()
)
cseFlowDataWhenCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowDataWhenCreated.setStatus("current")
_CseFlowDataLastUsed_Type = TimeStamp
_CseFlowDataLastUsed_Object = MibTableColumn
cseFlowDataLastUsed = _CseFlowDataLastUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 9, 1, 12),
    _CseFlowDataLastUsed_Type()
)
cseFlowDataLastUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowDataLastUsed.setStatus("current")
_CseFlowDataPkts_Type = Gauge32
_CseFlowDataPkts_Object = MibTableColumn
cseFlowDataPkts = _CseFlowDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 9, 1, 13),
    _CseFlowDataPkts_Type()
)
cseFlowDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowDataPkts.setStatus("current")
_CseFlowDataOctets_Type = CiscoGauge64
_CseFlowDataOctets_Object = MibTableColumn
cseFlowDataOctets = _CseFlowDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 9, 1, 14),
    _CseFlowDataOctets_Type()
)
cseFlowDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowDataOctets.setStatus("current")
_CseFlowSwitchControlTable_Object = MibTable
cseFlowSwitchControlTable = _CseFlowSwitchControlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 10)
)
if mibBuilder.loadTexts:
    cseFlowSwitchControlTable.setStatus("current")
_CseFlowSwitchControlEntry_Object = MibTableRow
cseFlowSwitchControlEntry = _CseFlowSwitchControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 10, 1)
)
cseFlowSwitchControlEntry.setIndexNames(
    (0, "CISCO-SWITCH-ENGINE-MIB", "cseFlowSwitchProtocol"),
)
if mibBuilder.loadTexts:
    cseFlowSwitchControlEntry.setStatus("current")
_CseFlowSwitchProtocol_Type = CiscoNetworkProtocol
_CseFlowSwitchProtocol_Object = MibTableColumn
cseFlowSwitchProtocol = _CseFlowSwitchProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 10, 1, 1),
    _CseFlowSwitchProtocol_Type()
)
cseFlowSwitchProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cseFlowSwitchProtocol.setStatus("current")
_CseFlowSwitchStatus_Type = ControlStatus
_CseFlowSwitchStatus_Object = MibTableColumn
cseFlowSwitchStatus = _CseFlowSwitchStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 10, 1, 2),
    _CseFlowSwitchStatus_Type()
)
cseFlowSwitchStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cseFlowSwitchStatus.setStatus("current")
_CseFlowMcastMaxQueries_Type = Unsigned32
_CseFlowMcastMaxQueries_Object = MibScalar
cseFlowMcastMaxQueries = _CseFlowMcastMaxQueries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 11),
    _CseFlowMcastMaxQueries_Type()
)
cseFlowMcastMaxQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowMcastMaxQueries.setStatus("current")
_CseFlowMcastQueryTable_Object = MibTable
cseFlowMcastQueryTable = _CseFlowMcastQueryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 12)
)
if mibBuilder.loadTexts:
    cseFlowMcastQueryTable.setStatus("current")
_CseFlowMcastQueryEntry_Object = MibTableRow
cseFlowMcastQueryEntry = _CseFlowMcastQueryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 12, 1)
)
cseFlowMcastQueryEntry.setIndexNames(
    (0, "CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastQueryIndex"),
)
if mibBuilder.loadTexts:
    cseFlowMcastQueryEntry.setStatus("current")
_CseFlowMcastQueryIndex_Type = Unsigned32
_CseFlowMcastQueryIndex_Object = MibTableColumn
cseFlowMcastQueryIndex = _CseFlowMcastQueryIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 12, 1, 1),
    _CseFlowMcastQueryIndex_Type()
)
cseFlowMcastQueryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cseFlowMcastQueryIndex.setStatus("current")


class _CseFlowMcastQueryMask_Type(Bits):
    """Custom type cseFlowMcastQueryMask based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("group", 1),
          ("groupip", 6),
          ("mvrf", 4),
          ("router", 3),
          ("source", 0),
          ("sourceip", 5),
          ("vlan", 2))
    )

_CseFlowMcastQueryMask_Type.__name__ = "Bits"
_CseFlowMcastQueryMask_Object = MibTableColumn
cseFlowMcastQueryMask = _CseFlowMcastQueryMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 12, 1, 2),
    _CseFlowMcastQueryMask_Type()
)
cseFlowMcastQueryMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseFlowMcastQueryMask.setStatus("current")
_CseFlowMcastQuerySrc_Type = IpAddress
_CseFlowMcastQuerySrc_Object = MibTableColumn
cseFlowMcastQuerySrc = _CseFlowMcastQuerySrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 12, 1, 3),
    _CseFlowMcastQuerySrc_Type()
)
cseFlowMcastQuerySrc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseFlowMcastQuerySrc.setStatus("deprecated")
_CseFlowMcastQueryGrp_Type = McastGroupIp
_CseFlowMcastQueryGrp_Object = MibTableColumn
cseFlowMcastQueryGrp = _CseFlowMcastQueryGrp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 12, 1, 4),
    _CseFlowMcastQueryGrp_Type()
)
cseFlowMcastQueryGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseFlowMcastQueryGrp.setStatus("deprecated")
_CseFlowMcastQuerySrcVlan_Type = VlanIndex
_CseFlowMcastQuerySrcVlan_Object = MibTableColumn
cseFlowMcastQuerySrcVlan = _CseFlowMcastQuerySrcVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 12, 1, 5),
    _CseFlowMcastQuerySrcVlan_Type()
)
cseFlowMcastQuerySrcVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseFlowMcastQuerySrcVlan.setStatus("current")
_CseFlowMcastQueryRtrIndex_Type = IpAddress
_CseFlowMcastQueryRtrIndex_Object = MibTableColumn
cseFlowMcastQueryRtrIndex = _CseFlowMcastQueryRtrIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 12, 1, 6),
    _CseFlowMcastQueryRtrIndex_Type()
)
cseFlowMcastQueryRtrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseFlowMcastQueryRtrIndex.setStatus("current")


class _CseFlowMcastQuerySkipNFlows_Type(Integer32):
    """Custom type cseFlowMcastQuerySkipNFlows based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CseFlowMcastQuerySkipNFlows_Type.__name__ = "Integer32"
_CseFlowMcastQuerySkipNFlows_Object = MibTableColumn
cseFlowMcastQuerySkipNFlows = _CseFlowMcastQuerySkipNFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 12, 1, 7),
    _CseFlowMcastQuerySkipNFlows_Type()
)
cseFlowMcastQuerySkipNFlows.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseFlowMcastQuerySkipNFlows.setStatus("current")
_CseFlowMcastQueryOwner_Type = OwnerString
_CseFlowMcastQueryOwner_Object = MibTableColumn
cseFlowMcastQueryOwner = _CseFlowMcastQueryOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 12, 1, 8),
    _CseFlowMcastQueryOwner_Type()
)
cseFlowMcastQueryOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseFlowMcastQueryOwner.setStatus("current")


class _CseFlowMcastQueryTotalFlows_Type(Integer32):
    """Custom type cseFlowMcastQueryTotalFlows based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CseFlowMcastQueryTotalFlows_Type.__name__ = "Integer32"
_CseFlowMcastQueryTotalFlows_Object = MibTableColumn
cseFlowMcastQueryTotalFlows = _CseFlowMcastQueryTotalFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 12, 1, 9),
    _CseFlowMcastQueryTotalFlows_Type()
)
cseFlowMcastQueryTotalFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowMcastQueryTotalFlows.setStatus("current")


class _CseFlowMcastQueryRows_Type(Integer32):
    """Custom type cseFlowMcastQueryRows based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_CseFlowMcastQueryRows_Type.__name__ = "Integer32"
_CseFlowMcastQueryRows_Object = MibTableColumn
cseFlowMcastQueryRows = _CseFlowMcastQueryRows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 12, 1, 10),
    _CseFlowMcastQueryRows_Type()
)
cseFlowMcastQueryRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowMcastQueryRows.setStatus("current")
_CseFlowMcastQueryStatus_Type = RowStatus
_CseFlowMcastQueryStatus_Object = MibTableColumn
cseFlowMcastQueryStatus = _CseFlowMcastQueryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 12, 1, 11),
    _CseFlowMcastQueryStatus_Type()
)
cseFlowMcastQueryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseFlowMcastQueryStatus.setStatus("current")
_CseFlowMcastQueryCreateTime_Type = TimeStamp
_CseFlowMcastQueryCreateTime_Object = MibTableColumn
cseFlowMcastQueryCreateTime = _CseFlowMcastQueryCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 12, 1, 12),
    _CseFlowMcastQueryCreateTime_Type()
)
cseFlowMcastQueryCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowMcastQueryCreateTime.setStatus("current")
_CseFlowMcastQueryMvrf_Type = MplsVpnId
_CseFlowMcastQueryMvrf_Object = MibTableColumn
cseFlowMcastQueryMvrf = _CseFlowMcastQueryMvrf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 12, 1, 13),
    _CseFlowMcastQueryMvrf_Type()
)
cseFlowMcastQueryMvrf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseFlowMcastQueryMvrf.setStatus("current")


class _CseFlowMcastQueryAddrType_Type(InetAddressType):
    """Custom type cseFlowMcastQueryAddrType based on InetAddressType"""


_CseFlowMcastQueryAddrType_Object = MibTableColumn
cseFlowMcastQueryAddrType = _CseFlowMcastQueryAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 12, 1, 14),
    _CseFlowMcastQueryAddrType_Type()
)
cseFlowMcastQueryAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseFlowMcastQueryAddrType.setStatus("current")


class _CseFlowMcastQuerySource_Type(InetAddress):
    """Custom type cseFlowMcastQuerySource based on InetAddress"""
    defaultHexValue = "00000000"


_CseFlowMcastQuerySource_Object = MibTableColumn
cseFlowMcastQuerySource = _CseFlowMcastQuerySource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 12, 1, 15),
    _CseFlowMcastQuerySource_Type()
)
cseFlowMcastQuerySource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseFlowMcastQuerySource.setStatus("current")


class _CseFlowMcastQueryGroup_Type(InetAddress):
    """Custom type cseFlowMcastQueryGroup based on InetAddress"""
    defaultHexValue = "00000000"


_CseFlowMcastQueryGroup_Object = MibTableColumn
cseFlowMcastQueryGroup = _CseFlowMcastQueryGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 12, 1, 16),
    _CseFlowMcastQueryGroup_Type()
)
cseFlowMcastQueryGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseFlowMcastQueryGroup.setStatus("current")
_CseFlowMcastResultTable_Object = MibTable
cseFlowMcastResultTable = _CseFlowMcastResultTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 13)
)
if mibBuilder.loadTexts:
    cseFlowMcastResultTable.setStatus("current")
_CseFlowMcastResultEntry_Object = MibTableRow
cseFlowMcastResultEntry = _CseFlowMcastResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 13, 1)
)
cseFlowMcastResultEntry.setIndexNames(
    (0, "CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastQueryIndex"),
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastResultIndex"),
)
if mibBuilder.loadTexts:
    cseFlowMcastResultEntry.setStatus("current")


class _CseFlowMcastResultIndex_Type(Integer32):
    """Custom type cseFlowMcastResultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CseFlowMcastResultIndex_Type.__name__ = "Integer32"
_CseFlowMcastResultIndex_Object = MibTableColumn
cseFlowMcastResultIndex = _CseFlowMcastResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 13, 1, 1),
    _CseFlowMcastResultIndex_Type()
)
cseFlowMcastResultIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cseFlowMcastResultIndex.setStatus("current")
_CseFlowMcastResultGrp_Type = McastGroupIp
_CseFlowMcastResultGrp_Object = MibTableColumn
cseFlowMcastResultGrp = _CseFlowMcastResultGrp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 13, 1, 2),
    _CseFlowMcastResultGrp_Type()
)
cseFlowMcastResultGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowMcastResultGrp.setStatus("deprecated")
_CseFlowMcastResultSrc_Type = IpAddress
_CseFlowMcastResultSrc_Object = MibTableColumn
cseFlowMcastResultSrc = _CseFlowMcastResultSrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 13, 1, 3),
    _CseFlowMcastResultSrc_Type()
)
cseFlowMcastResultSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowMcastResultSrc.setStatus("deprecated")
_CseFlowMcastResultSrcVlan_Type = VlanIndex
_CseFlowMcastResultSrcVlan_Object = MibTableColumn
cseFlowMcastResultSrcVlan = _CseFlowMcastResultSrcVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 13, 1, 4),
    _CseFlowMcastResultSrcVlan_Type()
)
cseFlowMcastResultSrcVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowMcastResultSrcVlan.setStatus("current")
_CseFlowMcastResultRtrIp_Type = IpAddress
_CseFlowMcastResultRtrIp_Object = MibTableColumn
cseFlowMcastResultRtrIp = _CseFlowMcastResultRtrIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 13, 1, 5),
    _CseFlowMcastResultRtrIp_Type()
)
cseFlowMcastResultRtrIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowMcastResultRtrIp.setStatus("current")
_CseFlowMcastResultRtrMac_Type = MacAddress
_CseFlowMcastResultRtrMac_Object = MibTableColumn
cseFlowMcastResultRtrMac = _CseFlowMcastResultRtrMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 13, 1, 6),
    _CseFlowMcastResultRtrMac_Type()
)
cseFlowMcastResultRtrMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowMcastResultRtrMac.setStatus("current")
_CseFlowMcastResultCreatedTS_Type = TimeStamp
_CseFlowMcastResultCreatedTS_Object = MibTableColumn
cseFlowMcastResultCreatedTS = _CseFlowMcastResultCreatedTS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 13, 1, 7),
    _CseFlowMcastResultCreatedTS_Type()
)
cseFlowMcastResultCreatedTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowMcastResultCreatedTS.setStatus("current")
_CseFlowMcastResultLastUsedTS_Type = TimeStamp
_CseFlowMcastResultLastUsedTS_Object = MibTableColumn
cseFlowMcastResultLastUsedTS = _CseFlowMcastResultLastUsedTS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 13, 1, 8),
    _CseFlowMcastResultLastUsedTS_Type()
)
cseFlowMcastResultLastUsedTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowMcastResultLastUsedTS.setStatus("current")
_CseFlowMcastResultPkts_Type = Counter64
_CseFlowMcastResultPkts_Object = MibTableColumn
cseFlowMcastResultPkts = _CseFlowMcastResultPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 13, 1, 9),
    _CseFlowMcastResultPkts_Type()
)
cseFlowMcastResultPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowMcastResultPkts.setStatus("current")
_CseFlowMcastResultOctets_Type = Counter64
_CseFlowMcastResultOctets_Object = MibTableColumn
cseFlowMcastResultOctets = _CseFlowMcastResultOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 13, 1, 10),
    _CseFlowMcastResultOctets_Type()
)
cseFlowMcastResultOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowMcastResultOctets.setStatus("current")


class _CseFlowMcastResultDstVlans_Type(OctetString):
    """Custom type cseFlowMcastResultDstVlans based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CseFlowMcastResultDstVlans_Type.__name__ = "OctetString"
_CseFlowMcastResultDstVlans_Object = MibTableColumn
cseFlowMcastResultDstVlans = _CseFlowMcastResultDstVlans_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 13, 1, 11),
    _CseFlowMcastResultDstVlans_Type()
)
cseFlowMcastResultDstVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowMcastResultDstVlans.setStatus("current")


class _CseFlowMcastResultDstVlans2k_Type(OctetString):
    """Custom type cseFlowMcastResultDstVlans2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CseFlowMcastResultDstVlans2k_Type.__name__ = "OctetString"
_CseFlowMcastResultDstVlans2k_Object = MibTableColumn
cseFlowMcastResultDstVlans2k = _CseFlowMcastResultDstVlans2k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 13, 1, 12),
    _CseFlowMcastResultDstVlans2k_Type()
)
cseFlowMcastResultDstVlans2k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowMcastResultDstVlans2k.setStatus("current")


class _CseFlowMcastResultDstVlans3k_Type(OctetString):
    """Custom type cseFlowMcastResultDstVlans3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CseFlowMcastResultDstVlans3k_Type.__name__ = "OctetString"
_CseFlowMcastResultDstVlans3k_Object = MibTableColumn
cseFlowMcastResultDstVlans3k = _CseFlowMcastResultDstVlans3k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 13, 1, 13),
    _CseFlowMcastResultDstVlans3k_Type()
)
cseFlowMcastResultDstVlans3k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowMcastResultDstVlans3k.setStatus("current")


class _CseFlowMcastResultDstVlans4k_Type(OctetString):
    """Custom type cseFlowMcastResultDstVlans4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CseFlowMcastResultDstVlans4k_Type.__name__ = "OctetString"
_CseFlowMcastResultDstVlans4k_Object = MibTableColumn
cseFlowMcastResultDstVlans4k = _CseFlowMcastResultDstVlans4k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 13, 1, 14),
    _CseFlowMcastResultDstVlans4k_Type()
)
cseFlowMcastResultDstVlans4k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowMcastResultDstVlans4k.setStatus("current")
_CseFlowMcastResultMvrf_Type = MplsVpnId
_CseFlowMcastResultMvrf_Object = MibTableColumn
cseFlowMcastResultMvrf = _CseFlowMcastResultMvrf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 13, 1, 15),
    _CseFlowMcastResultMvrf_Type()
)
cseFlowMcastResultMvrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowMcastResultMvrf.setStatus("current")
_CseFlowMcastResultAddrType_Type = InetAddressType
_CseFlowMcastResultAddrType_Object = MibTableColumn
cseFlowMcastResultAddrType = _CseFlowMcastResultAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 13, 1, 16),
    _CseFlowMcastResultAddrType_Type()
)
cseFlowMcastResultAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowMcastResultAddrType.setStatus("current")
_CseFlowMcastResultGroup_Type = InetAddress
_CseFlowMcastResultGroup_Object = MibTableColumn
cseFlowMcastResultGroup = _CseFlowMcastResultGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 13, 1, 17),
    _CseFlowMcastResultGroup_Type()
)
cseFlowMcastResultGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowMcastResultGroup.setStatus("current")
_CseFlowMcastResultSource_Type = InetAddress
_CseFlowMcastResultSource_Object = MibTableColumn
cseFlowMcastResultSource = _CseFlowMcastResultSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 13, 1, 18),
    _CseFlowMcastResultSource_Type()
)
cseFlowMcastResultSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowMcastResultSource.setStatus("current")


class _CseFlowMcastResultFlowType_Type(Integer32):
    """Custom type cseFlowMcastResultFlowType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("partialSC", 3),
          ("rpfMfd", 2))
    )


_CseFlowMcastResultFlowType_Type.__name__ = "Integer32"
_CseFlowMcastResultFlowType_Object = MibTableColumn
cseFlowMcastResultFlowType = _CseFlowMcastResultFlowType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 13, 1, 19),
    _CseFlowMcastResultFlowType_Type()
)
cseFlowMcastResultFlowType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowMcastResultFlowType.setStatus("current")


class _CseFlowMcastResultHFlag1k2k_Type(OctetString):
    """Custom type cseFlowMcastResultHFlag1k2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CseFlowMcastResultHFlag1k2k_Type.__name__ = "OctetString"
_CseFlowMcastResultHFlag1k2k_Object = MibTableColumn
cseFlowMcastResultHFlag1k2k = _CseFlowMcastResultHFlag1k2k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 13, 1, 20),
    _CseFlowMcastResultHFlag1k2k_Type()
)
cseFlowMcastResultHFlag1k2k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowMcastResultHFlag1k2k.setStatus("current")


class _CseFlowMcastResultHFlag3k4k_Type(OctetString):
    """Custom type cseFlowMcastResultHFlag3k4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CseFlowMcastResultHFlag3k4k_Type.__name__ = "OctetString"
_CseFlowMcastResultHFlag3k4k_Object = MibTableColumn
cseFlowMcastResultHFlag3k4k = _CseFlowMcastResultHFlag3k4k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 13, 1, 21),
    _CseFlowMcastResultHFlag3k4k_Type()
)
cseFlowMcastResultHFlag3k4k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowMcastResultHFlag3k4k.setStatus("current")
_CseFlowMcastSwitchStatus_Type = ControlStatus
_CseFlowMcastSwitchStatus_Object = MibScalar
cseFlowMcastSwitchStatus = _CseFlowMcastSwitchStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 14),
    _CseFlowMcastSwitchStatus_Type()
)
cseFlowMcastSwitchStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cseFlowMcastSwitchStatus.setStatus("current")


class _CseFlowIPXEstablishedAgingTime_Type(Integer32):
    """Custom type cseFlowIPXEstablishedAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CseFlowIPXEstablishedAgingTime_Type.__name__ = "Integer32"
_CseFlowIPXEstablishedAgingTime_Object = MibScalar
cseFlowIPXEstablishedAgingTime = _CseFlowIPXEstablishedAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 15),
    _CseFlowIPXEstablishedAgingTime_Type()
)
cseFlowIPXEstablishedAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cseFlowIPXEstablishedAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    cseFlowIPXEstablishedAgingTime.setUnits("seconds")
_CseStaticIpxExtRouterTable_Object = MibTable
cseStaticIpxExtRouterTable = _CseStaticIpxExtRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 16)
)
if mibBuilder.loadTexts:
    cseStaticIpxExtRouterTable.setStatus("current")
_CseStaticIpxExtRouterEntry_Object = MibTableRow
cseStaticIpxExtRouterEntry = _CseStaticIpxExtRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 16, 1)
)
cseStaticIpxExtRouterEntry.setIndexNames(
    (0, "CISCO-SWITCH-ENGINE-MIB", "cseRouterIndex"),
)
if mibBuilder.loadTexts:
    cseStaticIpxExtRouterEntry.setStatus("current")
_CseStaticIpxRouterName_Type = DisplayString
_CseStaticIpxRouterName_Object = MibTableColumn
cseStaticIpxRouterName = _CseStaticIpxRouterName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 16, 1, 1),
    _CseStaticIpxRouterName_Type()
)
cseStaticIpxRouterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseStaticIpxRouterName.setStatus("current")
_CseStaticIpxRouterOwner_Type = OwnerString
_CseStaticIpxRouterOwner_Object = MibTableColumn
cseStaticIpxRouterOwner = _CseStaticIpxRouterOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 16, 1, 2),
    _CseStaticIpxRouterOwner_Type()
)
cseStaticIpxRouterOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseStaticIpxRouterOwner.setStatus("current")
_CseStaticIpxRouterStatus_Type = RowStatus
_CseStaticIpxRouterStatus_Object = MibTableColumn
cseStaticIpxRouterStatus = _CseStaticIpxRouterStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 16, 1, 3),
    _CseStaticIpxRouterStatus_Type()
)
cseStaticIpxRouterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseStaticIpxRouterStatus.setStatus("current")


class _CseFlowOperEstablishedAgingTime_Type(Integer32):
    """Custom type cseFlowOperEstablishedAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CseFlowOperEstablishedAgingTime_Type.__name__ = "Integer32"
_CseFlowOperEstablishedAgingTime_Object = MibScalar
cseFlowOperEstablishedAgingTime = _CseFlowOperEstablishedAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 17),
    _CseFlowOperEstablishedAgingTime_Type()
)
cseFlowOperEstablishedAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowOperEstablishedAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    cseFlowOperEstablishedAgingTime.setUnits("seconds")
_CseFlowOperFastAgingTime_Type = Unsigned32
_CseFlowOperFastAgingTime_Object = MibScalar
cseFlowOperFastAgingTime = _CseFlowOperFastAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 18),
    _CseFlowOperFastAgingTime_Type()
)
cseFlowOperFastAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowOperFastAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    cseFlowOperFastAgingTime.setUnits("seconds")
_CseFlowOperFastAgePktThreshold_Type = Unsigned32
_CseFlowOperFastAgePktThreshold_Object = MibScalar
cseFlowOperFastAgePktThreshold = _CseFlowOperFastAgePktThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 19),
    _CseFlowOperFastAgePktThreshold_Type()
)
cseFlowOperFastAgePktThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowOperFastAgePktThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cseFlowOperFastAgePktThreshold.setUnits("packets")


class _CseFlowOperIPXAgingTime_Type(Integer32):
    """Custom type cseFlowOperIPXAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CseFlowOperIPXAgingTime_Type.__name__ = "Integer32"
_CseFlowOperIPXAgingTime_Object = MibScalar
cseFlowOperIPXAgingTime = _CseFlowOperIPXAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 20),
    _CseFlowOperIPXAgingTime_Type()
)
cseFlowOperIPXAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowOperIPXAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    cseFlowOperIPXAgingTime.setUnits("seconds")
_CseBridgedFlowStatsCtrlTable_Object = MibTable
cseBridgedFlowStatsCtrlTable = _CseBridgedFlowStatsCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 21)
)
if mibBuilder.loadTexts:
    cseBridgedFlowStatsCtrlTable.setStatus("current")
_CseBridgedFlowStatsCtrlEntry_Object = MibTableRow
cseBridgedFlowStatsCtrlEntry = _CseBridgedFlowStatsCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 21, 1)
)
cseBridgedFlowStatsCtrlEntry.setIndexNames(
    (0, "CISCO-SWITCH-ENGINE-MIB", "cseBridgedFlowVlan"),
)
if mibBuilder.loadTexts:
    cseBridgedFlowStatsCtrlEntry.setStatus("current")
_CseBridgedFlowVlan_Type = VlanIndex
_CseBridgedFlowVlan_Object = MibTableColumn
cseBridgedFlowVlan = _CseBridgedFlowVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 21, 1, 1),
    _CseBridgedFlowVlan_Type()
)
cseBridgedFlowVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cseBridgedFlowVlan.setStatus("current")


class _CseFlowBridgedFlowStatsEnable_Type(TruthValue):
    """Custom type cseFlowBridgedFlowStatsEnable based on TruthValue"""


_CseFlowBridgedFlowStatsEnable_Object = MibTableColumn
cseFlowBridgedFlowStatsEnable = _CseFlowBridgedFlowStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 21, 1, 2),
    _CseFlowBridgedFlowStatsEnable_Type()
)
cseFlowBridgedFlowStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cseFlowBridgedFlowStatsEnable.setStatus("current")


class _CseFlowIPFlowMask_Type(Integer32):
    """Custom type cseFlowIPFlowMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("dstOnly", 1),
          ("fullFlow", 3),
          ("intDstOnly", 8),
          ("intDstSrc", 5),
          ("intFull", 6),
          ("intSrcOnly", 9),
          ("null", 7),
          ("srcDst", 2),
          ("srcOnly", 4))
    )


_CseFlowIPFlowMask_Type.__name__ = "Integer32"
_CseFlowIPFlowMask_Object = MibScalar
cseFlowIPFlowMask = _CseFlowIPFlowMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 22),
    _CseFlowIPFlowMask_Type()
)
cseFlowIPFlowMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cseFlowIPFlowMask.setStatus("current")


class _CseFlowIPXFlowMask_Type(Integer32):
    """Custom type cseFlowIPXFlowMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dstOnly", 1),
          ("srcDst", 2))
    )


_CseFlowIPXFlowMask_Type.__name__ = "Integer32"
_CseFlowIPXFlowMask_Object = MibScalar
cseFlowIPXFlowMask = _CseFlowIPXFlowMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 23),
    _CseFlowIPXFlowMask_Type()
)
cseFlowIPXFlowMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowIPXFlowMask.setStatus("current")
_CseFlowLongAgingTime_Type = Unsigned32
_CseFlowLongAgingTime_Object = MibScalar
cseFlowLongAgingTime = _CseFlowLongAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 24),
    _CseFlowLongAgingTime_Type()
)
cseFlowLongAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cseFlowLongAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    cseFlowLongAgingTime.setUnits("seconds")
_CseFlowExcludeTable_Object = MibTable
cseFlowExcludeTable = _CseFlowExcludeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 25)
)
if mibBuilder.loadTexts:
    cseFlowExcludeTable.setStatus("current")
_CseFlowExcludeEntry_Object = MibTableRow
cseFlowExcludeEntry = _CseFlowExcludeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 25, 1)
)
cseFlowExcludeEntry.setIndexNames(
    (0, "CISCO-SWITCH-ENGINE-MIB", "cseFlowExcludePort"),
)
if mibBuilder.loadTexts:
    cseFlowExcludeEntry.setStatus("current")
_CseFlowExcludePort_Type = CiscoPort
_CseFlowExcludePort_Object = MibTableColumn
cseFlowExcludePort = _CseFlowExcludePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 25, 1, 1),
    _CseFlowExcludePort_Type()
)
cseFlowExcludePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cseFlowExcludePort.setStatus("current")


class _CseFlowExcludeProtocol_Type(Integer32):
    """Custom type cseFlowExcludeProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("tcp", 2),
          ("udp", 1))
    )


_CseFlowExcludeProtocol_Type.__name__ = "Integer32"
_CseFlowExcludeProtocol_Object = MibTableColumn
cseFlowExcludeProtocol = _CseFlowExcludeProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 25, 1, 2),
    _CseFlowExcludeProtocol_Type()
)
cseFlowExcludeProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseFlowExcludeProtocol.setStatus("current")
_CseFlowExcludeStatus_Type = RowStatus
_CseFlowExcludeStatus_Object = MibTableColumn
cseFlowExcludeStatus = _CseFlowExcludeStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 25, 1, 3),
    _CseFlowExcludeStatus_Type()
)
cseFlowExcludeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseFlowExcludeStatus.setStatus("current")
_CseFlowStatsTable_Object = MibTable
cseFlowStatsTable = _CseFlowStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 26)
)
if mibBuilder.loadTexts:
    cseFlowStatsTable.setStatus("current")
_CseFlowStatsEntry_Object = MibTableRow
cseFlowStatsEntry = _CseFlowStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 26, 1)
)
cseFlowStatsEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cseFlowStatsEntry.setStatus("current")
_CseFlowTotalFlows_Type = Gauge32
_CseFlowTotalFlows_Object = MibTableColumn
cseFlowTotalFlows = _CseFlowTotalFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 26, 1, 1),
    _CseFlowTotalFlows_Type()
)
cseFlowTotalFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowTotalFlows.setStatus("current")
_CseFlowTotalIpv4Flows_Type = Gauge32
_CseFlowTotalIpv4Flows_Object = MibTableColumn
cseFlowTotalIpv4Flows = _CseFlowTotalIpv4Flows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 26, 1, 2),
    _CseFlowTotalIpv4Flows_Type()
)
cseFlowTotalIpv4Flows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseFlowTotalIpv4Flows.setStatus("current")
_CseNetflowLS_ObjectIdentity = ObjectIdentity
cseNetflowLS = _CseNetflowLS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 3)
)
_CseNetflowLSExportStatus_Type = ControlStatus
_CseNetflowLSExportStatus_Object = MibScalar
cseNetflowLSExportStatus = _CseNetflowLSExportStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 3, 1),
    _CseNetflowLSExportStatus_Type()
)
cseNetflowLSExportStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cseNetflowLSExportStatus.setStatus("current")
_CseNetflowLSExportHost_Type = DisplayString
_CseNetflowLSExportHost_Object = MibScalar
cseNetflowLSExportHost = _CseNetflowLSExportHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 3, 2),
    _CseNetflowLSExportHost_Type()
)
cseNetflowLSExportHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cseNetflowLSExportHost.setStatus("deprecated")
_CseNetflowLSExportTransportNumber_Type = Unsigned32
_CseNetflowLSExportTransportNumber_Object = MibScalar
cseNetflowLSExportTransportNumber = _CseNetflowLSExportTransportNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 3, 3),
    _CseNetflowLSExportTransportNumber_Type()
)
cseNetflowLSExportTransportNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cseNetflowLSExportTransportNumber.setStatus("deprecated")
_CseNetflowLSExportDataSource_Type = FlowAddressComponent
_CseNetflowLSExportDataSource_Object = MibScalar
cseNetflowLSExportDataSource = _CseNetflowLSExportDataSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 3, 4),
    _CseNetflowLSExportDataSource_Type()
)
cseNetflowLSExportDataSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cseNetflowLSExportDataSource.setStatus("current")
_CseNetflowLSExportDataSourceMask_Type = FlowAddressComponent
_CseNetflowLSExportDataSourceMask_Object = MibScalar
cseNetflowLSExportDataSourceMask = _CseNetflowLSExportDataSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 3, 5),
    _CseNetflowLSExportDataSourceMask_Type()
)
cseNetflowLSExportDataSourceMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cseNetflowLSExportDataSourceMask.setStatus("current")
_CseNetflowLSExportDataDest_Type = FlowAddressComponent
_CseNetflowLSExportDataDest_Object = MibScalar
cseNetflowLSExportDataDest = _CseNetflowLSExportDataDest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 3, 6),
    _CseNetflowLSExportDataDest_Type()
)
cseNetflowLSExportDataDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cseNetflowLSExportDataDest.setStatus("current")
_CseNetflowLSExportDataDestMask_Type = FlowAddressComponent
_CseNetflowLSExportDataDestMask_Object = MibScalar
cseNetflowLSExportDataDestMask = _CseNetflowLSExportDataDestMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 3, 7),
    _CseNetflowLSExportDataDestMask_Type()
)
cseNetflowLSExportDataDestMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cseNetflowLSExportDataDestMask.setStatus("current")


class _CseNetflowLSExportDataProtocol_Type(Integer32):
    """Custom type cseNetflowLSExportDataProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CseNetflowLSExportDataProtocol_Type.__name__ = "Integer32"
_CseNetflowLSExportDataProtocol_Object = MibScalar
cseNetflowLSExportDataProtocol = _CseNetflowLSExportDataProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 3, 8),
    _CseNetflowLSExportDataProtocol_Type()
)
cseNetflowLSExportDataProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cseNetflowLSExportDataProtocol.setStatus("current")


class _CseNetflowLSExportDataFilterSelection_Type(Integer32):
    """Custom type cseNetflowLSExportDataFilterSelection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("excluded", 2),
          ("included", 1))
    )


_CseNetflowLSExportDataFilterSelection_Type.__name__ = "Integer32"
_CseNetflowLSExportDataFilterSelection_Object = MibScalar
cseNetflowLSExportDataFilterSelection = _CseNetflowLSExportDataFilterSelection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 3, 9),
    _CseNetflowLSExportDataFilterSelection_Type()
)
cseNetflowLSExportDataFilterSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cseNetflowLSExportDataFilterSelection.setStatus("current")


class _CseNetflowLSExportNDEVersionNumber_Type(Integer32):
    """Custom type cseNetflowLSExportNDEVersionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CseNetflowLSExportNDEVersionNumber_Type.__name__ = "Integer32"
_CseNetflowLSExportNDEVersionNumber_Object = MibScalar
cseNetflowLSExportNDEVersionNumber = _CseNetflowLSExportNDEVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 3, 10),
    _CseNetflowLSExportNDEVersionNumber_Type()
)
cseNetflowLSExportNDEVersionNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cseNetflowLSExportNDEVersionNumber.setStatus("current")


class _CseNetflowLSFilterSupport_Type(Integer32):
    """Custom type cseNetflowLSFilterSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multiple", 2),
          ("single", 1))
    )


_CseNetflowLSFilterSupport_Type.__name__ = "Integer32"
_CseNetflowLSFilterSupport_Object = MibScalar
cseNetflowLSFilterSupport = _CseNetflowLSFilterSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 3, 11),
    _CseNetflowLSFilterSupport_Type()
)
cseNetflowLSFilterSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseNetflowLSFilterSupport.setStatus("current")
_CseNetflowLSFilterTable_Object = MibTable
cseNetflowLSFilterTable = _CseNetflowLSFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 3, 12)
)
if mibBuilder.loadTexts:
    cseNetflowLSFilterTable.setStatus("current")
_CseNetflowLSFilterEntry_Object = MibTableRow
cseNetflowLSFilterEntry = _CseNetflowLSFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 3, 12, 1)
)
cseNetflowLSFilterEntry.setIndexNames(
    (0, "CISCO-SWITCH-ENGINE-MIB", "cseNetflowLSFilterIndex"),
)
if mibBuilder.loadTexts:
    cseNetflowLSFilterEntry.setStatus("current")
_CseNetflowLSFilterIndex_Type = Unsigned32
_CseNetflowLSFilterIndex_Object = MibTableColumn
cseNetflowLSFilterIndex = _CseNetflowLSFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 3, 12, 1, 1),
    _CseNetflowLSFilterIndex_Type()
)
cseNetflowLSFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cseNetflowLSFilterIndex.setStatus("current")


class _CseNetflowLSFilterDataSource_Type(FlowAddressComponent):
    """Custom type cseNetflowLSFilterDataSource based on FlowAddressComponent"""
    defaultHexValue = "000000000000"


_CseNetflowLSFilterDataSource_Object = MibTableColumn
cseNetflowLSFilterDataSource = _CseNetflowLSFilterDataSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 3, 12, 1, 2),
    _CseNetflowLSFilterDataSource_Type()
)
cseNetflowLSFilterDataSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseNetflowLSFilterDataSource.setStatus("current")


class _CseNetflowLSFilterDataSourceMask_Type(FlowAddressComponent):
    """Custom type cseNetflowLSFilterDataSourceMask based on FlowAddressComponent"""
    defaultHexValue = "000000000000"


_CseNetflowLSFilterDataSourceMask_Object = MibTableColumn
cseNetflowLSFilterDataSourceMask = _CseNetflowLSFilterDataSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 3, 12, 1, 3),
    _CseNetflowLSFilterDataSourceMask_Type()
)
cseNetflowLSFilterDataSourceMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseNetflowLSFilterDataSourceMask.setStatus("current")


class _CseNetflowLSFilterDataDest_Type(FlowAddressComponent):
    """Custom type cseNetflowLSFilterDataDest based on FlowAddressComponent"""
    defaultHexValue = "000000000000"


_CseNetflowLSFilterDataDest_Object = MibTableColumn
cseNetflowLSFilterDataDest = _CseNetflowLSFilterDataDest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 3, 12, 1, 4),
    _CseNetflowLSFilterDataDest_Type()
)
cseNetflowLSFilterDataDest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseNetflowLSFilterDataDest.setStatus("current")


class _CseNetflowLSFilterDataDestMask_Type(FlowAddressComponent):
    """Custom type cseNetflowLSFilterDataDestMask based on FlowAddressComponent"""
    defaultHexValue = "000000000000"


_CseNetflowLSFilterDataDestMask_Object = MibTableColumn
cseNetflowLSFilterDataDestMask = _CseNetflowLSFilterDataDestMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 3, 12, 1, 5),
    _CseNetflowLSFilterDataDestMask_Type()
)
cseNetflowLSFilterDataDestMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseNetflowLSFilterDataDestMask.setStatus("current")


class _CseNetflowLSFilterDataProtocol_Type(Integer32):
    """Custom type cseNetflowLSFilterDataProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CseNetflowLSFilterDataProtocol_Type.__name__ = "Integer32"
_CseNetflowLSFilterDataProtocol_Object = MibTableColumn
cseNetflowLSFilterDataProtocol = _CseNetflowLSFilterDataProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 3, 12, 1, 6),
    _CseNetflowLSFilterDataProtocol_Type()
)
cseNetflowLSFilterDataProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseNetflowLSFilterDataProtocol.setStatus("current")


class _CseNetflowLSFilterSelection_Type(Integer32):
    """Custom type cseNetflowLSFilterSelection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("excluded", 2),
          ("included", 1))
    )


_CseNetflowLSFilterSelection_Type.__name__ = "Integer32"
_CseNetflowLSFilterSelection_Object = MibTableColumn
cseNetflowLSFilterSelection = _CseNetflowLSFilterSelection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 3, 12, 1, 7),
    _CseNetflowLSFilterSelection_Type()
)
cseNetflowLSFilterSelection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseNetflowLSFilterSelection.setStatus("current")
_CseNetflowLSFilterStatus_Type = RowStatus
_CseNetflowLSFilterStatus_Object = MibTableColumn
cseNetflowLSFilterStatus = _CseNetflowLSFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 3, 12, 1, 8),
    _CseNetflowLSFilterStatus_Type()
)
cseNetflowLSFilterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseNetflowLSFilterStatus.setStatus("current")


class _CseNetFlowIfIndexEnable_Type(Bits):
    """Custom type cseNetFlowIfIndexEnable based on Bits"""
    namedValues = NamedValues(
        *(("destIfIndex", 0),
          ("srcIfIndex", 1))
    )

_CseNetFlowIfIndexEnable_Type.__name__ = "Bits"
_CseNetFlowIfIndexEnable_Object = MibScalar
cseNetFlowIfIndexEnable = _CseNetFlowIfIndexEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 3, 13),
    _CseNetFlowIfIndexEnable_Type()
)
cseNetFlowIfIndexEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cseNetFlowIfIndexEnable.setStatus("current")


class _CseNetflowASInfoExportCtrl_Type(Integer32):
    """Custom type cseNetflowASInfoExportCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("originate", 2),
          ("peer", 3))
    )


_CseNetflowASInfoExportCtrl_Type.__name__ = "Integer32"
_CseNetflowASInfoExportCtrl_Object = MibScalar
cseNetflowASInfoExportCtrl = _CseNetflowASInfoExportCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 3, 14),
    _CseNetflowASInfoExportCtrl_Type()
)
cseNetflowASInfoExportCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cseNetflowASInfoExportCtrl.setStatus("current")
_CseNetflowPerVlanIfGlobalEnable_Type = TruthValue
_CseNetflowPerVlanIfGlobalEnable_Object = MibScalar
cseNetflowPerVlanIfGlobalEnable = _CseNetflowPerVlanIfGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 3, 15),
    _CseNetflowPerVlanIfGlobalEnable_Type()
)
cseNetflowPerVlanIfGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cseNetflowPerVlanIfGlobalEnable.setStatus("current")
_CseNetflowPerVlanIfCtrlTable_Object = MibTable
cseNetflowPerVlanIfCtrlTable = _CseNetflowPerVlanIfCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 3, 16)
)
if mibBuilder.loadTexts:
    cseNetflowPerVlanIfCtrlTable.setStatus("current")
_CseNetflowPerVlanIfCtrlEntry_Object = MibTableRow
cseNetflowPerVlanIfCtrlEntry = _CseNetflowPerVlanIfCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 3, 16, 1)
)
cseNetflowPerVlanIfCtrlEntry.setIndexNames(
    (0, "CISCO-SWITCH-ENGINE-MIB", "cseNetflowPerVlanIfCtrlVlan"),
)
if mibBuilder.loadTexts:
    cseNetflowPerVlanIfCtrlEntry.setStatus("current")
_CseNetflowPerVlanIfCtrlVlan_Type = VlanIndex
_CseNetflowPerVlanIfCtrlVlan_Object = MibTableColumn
cseNetflowPerVlanIfCtrlVlan = _CseNetflowPerVlanIfCtrlVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 3, 16, 1, 1),
    _CseNetflowPerVlanIfCtrlVlan_Type()
)
cseNetflowPerVlanIfCtrlVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cseNetflowPerVlanIfCtrlVlan.setStatus("current")
_CseNetflowPerVlanIfEnable_Type = TruthValue
_CseNetflowPerVlanIfEnable_Object = MibTableColumn
cseNetflowPerVlanIfEnable = _CseNetflowPerVlanIfEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 3, 16, 1, 2),
    _CseNetflowPerVlanIfEnable_Type()
)
cseNetflowPerVlanIfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cseNetflowPerVlanIfEnable.setStatus("current")
_CseL3Objects_ObjectIdentity = ObjectIdentity
cseL3Objects = _CseL3Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4)
)
_CseL3StatsTable_Object = MibTable
cseL3StatsTable = _CseL3StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cseL3StatsTable.setStatus("current")
_CseL3StatsEntry_Object = MibTableRow
cseL3StatsEntry = _CseL3StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 1, 1)
)
cseL3StatsEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cseL3StatsEntry.setStatus("current")
_CseL3SwitchedTotalPkts_Type = Counter32
_CseL3SwitchedTotalPkts_Object = MibTableColumn
cseL3SwitchedTotalPkts = _CseL3SwitchedTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 1, 1, 1),
    _CseL3SwitchedTotalPkts_Type()
)
cseL3SwitchedTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseL3SwitchedTotalPkts.setStatus("current")
_CseL3SwitchedTotalOctets_Type = Counter64
_CseL3SwitchedTotalOctets_Object = MibTableColumn
cseL3SwitchedTotalOctets = _CseL3SwitchedTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 1, 1, 2),
    _CseL3SwitchedTotalOctets_Type()
)
cseL3SwitchedTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseL3SwitchedTotalOctets.setStatus("current")
_CseL3CandidateFlowHits_Type = Counter32
_CseL3CandidateFlowHits_Object = MibTableColumn
cseL3CandidateFlowHits = _CseL3CandidateFlowHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 1, 1, 3),
    _CseL3CandidateFlowHits_Type()
)
cseL3CandidateFlowHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseL3CandidateFlowHits.setStatus("current")
_CseL3EstablishedFlowHits_Type = Counter32
_CseL3EstablishedFlowHits_Object = MibTableColumn
cseL3EstablishedFlowHits = _CseL3EstablishedFlowHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 1, 1, 4),
    _CseL3EstablishedFlowHits_Type()
)
cseL3EstablishedFlowHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseL3EstablishedFlowHits.setStatus("current")
_CseL3ActiveFlows_Type = Gauge32
_CseL3ActiveFlows_Object = MibTableColumn
cseL3ActiveFlows = _CseL3ActiveFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 1, 1, 5),
    _CseL3ActiveFlows_Type()
)
cseL3ActiveFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseL3ActiveFlows.setStatus("current")
_CseL3FlowLearnFailures_Type = Counter32
_CseL3FlowLearnFailures_Object = MibTableColumn
cseL3FlowLearnFailures = _CseL3FlowLearnFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 1, 1, 6),
    _CseL3FlowLearnFailures_Type()
)
cseL3FlowLearnFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseL3FlowLearnFailures.setStatus("current")
_CseL3IntFlowInvalids_Type = Counter32
_CseL3IntFlowInvalids_Object = MibTableColumn
cseL3IntFlowInvalids = _CseL3IntFlowInvalids_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 1, 1, 7),
    _CseL3IntFlowInvalids_Type()
)
cseL3IntFlowInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseL3IntFlowInvalids.setStatus("current")
_CseL3ExtFlowInvalids_Type = Counter32
_CseL3ExtFlowInvalids_Object = MibTableColumn
cseL3ExtFlowInvalids = _CseL3ExtFlowInvalids_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 1, 1, 8),
    _CseL3ExtFlowInvalids_Type()
)
cseL3ExtFlowInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseL3ExtFlowInvalids.setStatus("current")
_CseL3SwitchedPktsPerSec_Type = Counter32
_CseL3SwitchedPktsPerSec_Object = MibTableColumn
cseL3SwitchedPktsPerSec = _CseL3SwitchedPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 1, 1, 9),
    _CseL3SwitchedPktsPerSec_Type()
)
cseL3SwitchedPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseL3SwitchedPktsPerSec.setStatus("current")
_CseL3VlanStatsTable_Object = MibTable
cseL3VlanStatsTable = _CseL3VlanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cseL3VlanStatsTable.setStatus("current")
_CseL3VlanStatsEntry_Object = MibTableRow
cseL3VlanStatsEntry = _CseL3VlanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 2, 1)
)
cseL3VlanStatsEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-SWITCH-ENGINE-MIB", "cseL3VlanIndex"),
)
if mibBuilder.loadTexts:
    cseL3VlanStatsEntry.setStatus("current")
_CseL3VlanIndex_Type = VlanIndex
_CseL3VlanIndex_Object = MibTableColumn
cseL3VlanIndex = _CseL3VlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 2, 1, 1),
    _CseL3VlanIndex_Type()
)
cseL3VlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cseL3VlanIndex.setStatus("current")
_CseL3VlanInPkts_Type = Counter64
_CseL3VlanInPkts_Object = MibTableColumn
cseL3VlanInPkts = _CseL3VlanInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 2, 1, 2),
    _CseL3VlanInPkts_Type()
)
cseL3VlanInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseL3VlanInPkts.setStatus("current")
_CseL3VlanInOctets_Type = Counter64
_CseL3VlanInOctets_Object = MibTableColumn
cseL3VlanInOctets = _CseL3VlanInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 2, 1, 3),
    _CseL3VlanInOctets_Type()
)
cseL3VlanInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseL3VlanInOctets.setStatus("current")
_CseL3VlanOutPkts_Type = Counter64
_CseL3VlanOutPkts_Object = MibTableColumn
cseL3VlanOutPkts = _CseL3VlanOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 2, 1, 4),
    _CseL3VlanOutPkts_Type()
)
cseL3VlanOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseL3VlanOutPkts.setStatus("current")
_CseL3VlanOutOctets_Type = Counter64
_CseL3VlanOutOctets_Object = MibTableColumn
cseL3VlanOutOctets = _CseL3VlanOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 2, 1, 5),
    _CseL3VlanOutOctets_Type()
)
cseL3VlanOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseL3VlanOutOctets.setStatus("current")
_CseL3VlanInUnicastPkts_Type = Counter64
_CseL3VlanInUnicastPkts_Object = MibTableColumn
cseL3VlanInUnicastPkts = _CseL3VlanInUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 2, 1, 6),
    _CseL3VlanInUnicastPkts_Type()
)
cseL3VlanInUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseL3VlanInUnicastPkts.setStatus("current")
_CseL3VlanInUnicastOctets_Type = Counter64
_CseL3VlanInUnicastOctets_Object = MibTableColumn
cseL3VlanInUnicastOctets = _CseL3VlanInUnicastOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 2, 1, 7),
    _CseL3VlanInUnicastOctets_Type()
)
cseL3VlanInUnicastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseL3VlanInUnicastOctets.setStatus("current")
_CseL3VlanOutUnicastPkts_Type = Counter64
_CseL3VlanOutUnicastPkts_Object = MibTableColumn
cseL3VlanOutUnicastPkts = _CseL3VlanOutUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 2, 1, 8),
    _CseL3VlanOutUnicastPkts_Type()
)
cseL3VlanOutUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseL3VlanOutUnicastPkts.setStatus("current")
_CseL3VlanOutUnicastOctets_Type = Counter64
_CseL3VlanOutUnicastOctets_Object = MibTableColumn
cseL3VlanOutUnicastOctets = _CseL3VlanOutUnicastOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 2, 1, 9),
    _CseL3VlanOutUnicastOctets_Type()
)
cseL3VlanOutUnicastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseL3VlanOutUnicastOctets.setStatus("current")
_CseStatsFlowTable_Object = MibTable
cseStatsFlowTable = _CseStatsFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 3)
)
if mibBuilder.loadTexts:
    cseStatsFlowTable.setStatus("current")
_CseStatsFlowEntry_Object = MibTableRow
cseStatsFlowEntry = _CseStatsFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    cseStatsFlowEntry.setStatus("current")
_CseStatsFlowAged_Type = Counter32
_CseStatsFlowAged_Object = MibTableColumn
cseStatsFlowAged = _CseStatsFlowAged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 3, 1, 1),
    _CseStatsFlowAged_Type()
)
cseStatsFlowAged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseStatsFlowAged.setStatus("current")
_CseStatsFlowPurged_Type = Counter32
_CseStatsFlowPurged_Object = MibTableColumn
cseStatsFlowPurged = _CseStatsFlowPurged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 3, 1, 2),
    _CseStatsFlowPurged_Type()
)
cseStatsFlowPurged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseStatsFlowPurged.setStatus("current")
_CseStatsFlowParityFail_Type = Counter32
_CseStatsFlowParityFail_Object = MibTableColumn
cseStatsFlowParityFail = _CseStatsFlowParityFail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 3, 1, 3),
    _CseStatsFlowParityFail_Type()
)
cseStatsFlowParityFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseStatsFlowParityFail.setStatus("current")
_CseCacheUtilTable_Object = MibTable
cseCacheUtilTable = _CseCacheUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 4)
)
if mibBuilder.loadTexts:
    cseCacheUtilTable.setStatus("current")
_CseCacheUtilEntry_Object = MibTableRow
cseCacheUtilEntry = _CseCacheUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 4, 1)
)
cseCacheUtilEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cseCacheUtilEntry.setStatus("current")


class _CseCacheUtilization_Type(Gauge32):
    """Custom type cseCacheUtilization based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CseCacheUtilization_Type.__name__ = "Gauge32"
_CseCacheUtilization_Object = MibTableColumn
cseCacheUtilization = _CseCacheUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 4, 1, 1),
    _CseCacheUtilization_Type()
)
cseCacheUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseCacheUtilization.setStatus("current")
_CseCacheEntriesCreated_Type = Unsigned32
_CseCacheEntriesCreated_Object = MibTableColumn
cseCacheEntriesCreated = _CseCacheEntriesCreated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 4, 1, 2),
    _CseCacheEntriesCreated_Type()
)
cseCacheEntriesCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseCacheEntriesCreated.setStatus("current")
_CseCacheEntriesFailed_Type = Unsigned32
_CseCacheEntriesFailed_Object = MibTableColumn
cseCacheEntriesFailed = _CseCacheEntriesFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 4, 1, 3),
    _CseCacheEntriesFailed_Type()
)
cseCacheEntriesFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseCacheEntriesFailed.setStatus("current")
_CseErrorStatsTable_Object = MibTable
cseErrorStatsTable = _CseErrorStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 5)
)
if mibBuilder.loadTexts:
    cseErrorStatsTable.setStatus("current")
_CseErrorStatsEntry_Object = MibTableRow
cseErrorStatsEntry = _CseErrorStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 5, 1)
)
cseErrorStatsEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cseErrorStatsEntry.setStatus("current")
_CseIpPlenErrors_Type = Counter64
_CseIpPlenErrors_Object = MibTableColumn
cseIpPlenErrors = _CseIpPlenErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 5, 1, 1),
    _CseIpPlenErrors_Type()
)
cseIpPlenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseIpPlenErrors.setStatus("current")
_CseIpTooShortErrors_Type = Counter64
_CseIpTooShortErrors_Object = MibTableColumn
cseIpTooShortErrors = _CseIpTooShortErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 5, 1, 2),
    _CseIpTooShortErrors_Type()
)
cseIpTooShortErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseIpTooShortErrors.setStatus("current")
_CseIpCheckSumErrors_Type = Counter64
_CseIpCheckSumErrors_Object = MibTableColumn
cseIpCheckSumErrors = _CseIpCheckSumErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 5, 1, 3),
    _CseIpCheckSumErrors_Type()
)
cseIpCheckSumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseIpCheckSumErrors.setStatus("current")
_CseIpxPlenErrors_Type = Counter64
_CseIpxPlenErrors_Object = MibTableColumn
cseIpxPlenErrors = _CseIpxPlenErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 5, 1, 4),
    _CseIpxPlenErrors_Type()
)
cseIpxPlenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseIpxPlenErrors.setStatus("current")
_CseIpxTooShortErrors_Type = Counter64
_CseIpxTooShortErrors_Object = MibTableColumn
cseIpxTooShortErrors = _CseIpxTooShortErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 5, 1, 5),
    _CseIpxTooShortErrors_Type()
)
cseIpxTooShortErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseIpxTooShortErrors.setStatus("current")
_CseErrorStatsLCTable_Object = MibTable
cseErrorStatsLCTable = _CseErrorStatsLCTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 6)
)
if mibBuilder.loadTexts:
    cseErrorStatsLCTable.setStatus("current")
_CseErrorStatsLCEntry_Object = MibTableRow
cseErrorStatsLCEntry = _CseErrorStatsLCEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 6, 1)
)
cseErrorStatsLCEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cseErrorStatsLCEntry.setStatus("current")
_CseLCIpPlenErrors_Type = Counter32
_CseLCIpPlenErrors_Object = MibTableColumn
cseLCIpPlenErrors = _CseLCIpPlenErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 6, 1, 1),
    _CseLCIpPlenErrors_Type()
)
cseLCIpPlenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseLCIpPlenErrors.setStatus("current")
_CseLCIpTooShortErrors_Type = Counter32
_CseLCIpTooShortErrors_Object = MibTableColumn
cseLCIpTooShortErrors = _CseLCIpTooShortErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 6, 1, 2),
    _CseLCIpTooShortErrors_Type()
)
cseLCIpTooShortErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseLCIpTooShortErrors.setStatus("current")
_CseLCIpCheckSumErrors_Type = Counter32
_CseLCIpCheckSumErrors_Object = MibTableColumn
cseLCIpCheckSumErrors = _CseLCIpCheckSumErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 6, 1, 3),
    _CseLCIpCheckSumErrors_Type()
)
cseLCIpCheckSumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseLCIpCheckSumErrors.setStatus("current")
_CseLCIpxPlenErrors_Type = Counter32
_CseLCIpxPlenErrors_Object = MibTableColumn
cseLCIpxPlenErrors = _CseLCIpxPlenErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 6, 1, 4),
    _CseLCIpxPlenErrors_Type()
)
cseLCIpxPlenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseLCIpxPlenErrors.setStatus("current")
_CseLCIpxTooShortErrors_Type = Counter32
_CseLCIpxTooShortErrors_Object = MibTableColumn
cseLCIpxTooShortErrors = _CseLCIpxTooShortErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 6, 1, 5),
    _CseLCIpxTooShortErrors_Type()
)
cseLCIpxTooShortErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseLCIpxTooShortErrors.setStatus("current")
_CseL3SwitchedAggrPktsPerSec_Type = Counter32
_CseL3SwitchedAggrPktsPerSec_Object = MibScalar
cseL3SwitchedAggrPktsPerSec = _CseL3SwitchedAggrPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 7),
    _CseL3SwitchedAggrPktsPerSec_Type()
)
cseL3SwitchedAggrPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseL3SwitchedAggrPktsPerSec.setStatus("current")
_CseProtocolFilter_ObjectIdentity = ObjectIdentity
cseProtocolFilter = _CseProtocolFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 5)
)
_CseProtocolFilterEnable_Type = TruthValue
_CseProtocolFilterEnable_Object = MibScalar
cseProtocolFilterEnable = _CseProtocolFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 5, 1),
    _CseProtocolFilterEnable_Type()
)
cseProtocolFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cseProtocolFilterEnable.setStatus("current")
_CseProtocolFilterPortTable_Object = MibTable
cseProtocolFilterPortTable = _CseProtocolFilterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 5, 2)
)
if mibBuilder.loadTexts:
    cseProtocolFilterPortTable.setStatus("current")
_CseProtocolFilterPortEntry_Object = MibTableRow
cseProtocolFilterPortEntry = _CseProtocolFilterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 5, 2, 1)
)
cseProtocolFilterPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-SWITCH-ENGINE-MIB", "cseProtocolFilterPortProtocol"),
)
if mibBuilder.loadTexts:
    cseProtocolFilterPortEntry.setStatus("current")


class _CseProtocolFilterPortProtocol_Type(Integer32):
    """Custom type cseProtocolFilterPortProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("grpProtocols", 3),
          ("ip", 1),
          ("ipx", 2))
    )


_CseProtocolFilterPortProtocol_Type.__name__ = "Integer32"
_CseProtocolFilterPortProtocol_Object = MibTableColumn
cseProtocolFilterPortProtocol = _CseProtocolFilterPortProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 5, 2, 1, 1),
    _CseProtocolFilterPortProtocol_Type()
)
cseProtocolFilterPortProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cseProtocolFilterPortProtocol.setStatus("current")


class _CseProtocolFilterPortAdminStatus_Type(Integer32):
    """Custom type cseProtocolFilterPortAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("off", 2),
          ("on", 1))
    )


_CseProtocolFilterPortAdminStatus_Type.__name__ = "Integer32"
_CseProtocolFilterPortAdminStatus_Object = MibTableColumn
cseProtocolFilterPortAdminStatus = _CseProtocolFilterPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 5, 2, 1, 2),
    _CseProtocolFilterPortAdminStatus_Type()
)
cseProtocolFilterPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cseProtocolFilterPortAdminStatus.setStatus("current")


class _CseProtocolFilterPortOperStatus_Type(Integer32):
    """Custom type cseProtocolFilterPortOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 3),
          ("off", 2),
          ("on", 1))
    )


_CseProtocolFilterPortOperStatus_Type.__name__ = "Integer32"
_CseProtocolFilterPortOperStatus_Object = MibTableColumn
cseProtocolFilterPortOperStatus = _CseProtocolFilterPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 5, 2, 1, 3),
    _CseProtocolFilterPortOperStatus_Type()
)
cseProtocolFilterPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseProtocolFilterPortOperStatus.setStatus("current")
_CseUcastCache_ObjectIdentity = ObjectIdentity
cseUcastCache = _CseUcastCache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 6)
)
_CseUcastCacheTable_Object = MibTable
cseUcastCacheTable = _CseUcastCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cseUcastCacheTable.setStatus("current")
_CseUcastCacheEntry_Object = MibTableRow
cseUcastCacheEntry = _CseUcastCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 6, 1, 1)
)
cseUcastCacheEntry.setIndexNames(
    (0, "CISCO-SWITCH-ENGINE-MIB", "cseUcastCacheIndex"),
)
if mibBuilder.loadTexts:
    cseUcastCacheEntry.setStatus("current")
_CseUcastCacheIndex_Type = Unsigned32
_CseUcastCacheIndex_Object = MibTableColumn
cseUcastCacheIndex = _CseUcastCacheIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 6, 1, 1, 1),
    _CseUcastCacheIndex_Type()
)
cseUcastCacheIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cseUcastCacheIndex.setStatus("current")


class _CseUcastCacheFlowType_Type(Integer32):
    """Custom type cseUcastCacheFlowType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("dstOnly", 2),
          ("fullFlow", 5),
          ("ipxDstOnly", 6),
          ("ipxSrcAndDst", 7),
          ("srcAndDst", 4),
          ("srcOrDst", 3))
    )


_CseUcastCacheFlowType_Type.__name__ = "Integer32"
_CseUcastCacheFlowType_Object = MibTableColumn
cseUcastCacheFlowType = _CseUcastCacheFlowType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 6, 1, 1, 2),
    _CseUcastCacheFlowType_Type()
)
cseUcastCacheFlowType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseUcastCacheFlowType.setStatus("current")


class _CseUcastCacheTransport_Type(Integer32):
    """Custom type cseUcastCacheTransport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 2),
          ("udp", 1))
    )


_CseUcastCacheTransport_Type.__name__ = "Integer32"
_CseUcastCacheTransport_Object = MibTableColumn
cseUcastCacheTransport = _CseUcastCacheTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 6, 1, 1, 3),
    _CseUcastCacheTransport_Type()
)
cseUcastCacheTransport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseUcastCacheTransport.setStatus("current")
_CseUcastCacheDest_Type = FlowAddressComponent
_CseUcastCacheDest_Object = MibTableColumn
cseUcastCacheDest = _CseUcastCacheDest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 6, 1, 1, 4),
    _CseUcastCacheDest_Type()
)
cseUcastCacheDest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseUcastCacheDest.setStatus("current")
_CseUcastCacheDestMask_Type = FlowAddressComponent
_CseUcastCacheDestMask_Object = MibTableColumn
cseUcastCacheDestMask = _CseUcastCacheDestMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 6, 1, 1, 5),
    _CseUcastCacheDestMask_Type()
)
cseUcastCacheDestMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseUcastCacheDestMask.setStatus("current")
_CseUcastCacheSource_Type = FlowAddressComponent
_CseUcastCacheSource_Object = MibTableColumn
cseUcastCacheSource = _CseUcastCacheSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 6, 1, 1, 6),
    _CseUcastCacheSource_Type()
)
cseUcastCacheSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseUcastCacheSource.setStatus("current")
_CseUcastCacheSrcMask_Type = FlowAddressComponent
_CseUcastCacheSrcMask_Object = MibTableColumn
cseUcastCacheSrcMask = _CseUcastCacheSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 6, 1, 1, 7),
    _CseUcastCacheSrcMask_Type()
)
cseUcastCacheSrcMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseUcastCacheSrcMask.setStatus("current")
_CseUcastCacheRtrIp_Type = IpAddress
_CseUcastCacheRtrIp_Object = MibTableColumn
cseUcastCacheRtrIp = _CseUcastCacheRtrIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 6, 1, 1, 8),
    _CseUcastCacheRtrIp_Type()
)
cseUcastCacheRtrIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseUcastCacheRtrIp.setStatus("current")
_CseUcastCacheOwner_Type = OwnerString
_CseUcastCacheOwner_Object = MibTableColumn
cseUcastCacheOwner = _CseUcastCacheOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 6, 1, 1, 9),
    _CseUcastCacheOwner_Type()
)
cseUcastCacheOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseUcastCacheOwner.setStatus("current")
_CseUcastCacheStatus_Type = RowStatus
_CseUcastCacheStatus_Object = MibTableColumn
cseUcastCacheStatus = _CseUcastCacheStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 6, 1, 1, 10),
    _CseUcastCacheStatus_Type()
)
cseUcastCacheStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseUcastCacheStatus.setStatus("current")


class _CseUcastCacheResult_Type(Integer32):
    """Custom type cseUcastCacheResult based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notPurging", 2),
          ("purging", 1))
    )


_CseUcastCacheResult_Type.__name__ = "Integer32"
_CseUcastCacheResult_Object = MibTableColumn
cseUcastCacheResult = _CseUcastCacheResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 6, 1, 1, 11),
    _CseUcastCacheResult_Type()
)
cseUcastCacheResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseUcastCacheResult.setStatus("current")
_CseMcastCache_ObjectIdentity = ObjectIdentity
cseMcastCache = _CseMcastCache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 7)
)
_CseMcastCacheTable_Object = MibTable
cseMcastCacheTable = _CseMcastCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 7, 1)
)
if mibBuilder.loadTexts:
    cseMcastCacheTable.setStatus("current")
_CseMcastCacheEntry_Object = MibTableRow
cseMcastCacheEntry = _CseMcastCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 7, 1, 1)
)
cseMcastCacheEntry.setIndexNames(
    (0, "CISCO-SWITCH-ENGINE-MIB", "cseMcastCacheIndex"),
)
if mibBuilder.loadTexts:
    cseMcastCacheEntry.setStatus("current")
_CseMcastCacheIndex_Type = Unsigned32
_CseMcastCacheIndex_Object = MibTableColumn
cseMcastCacheIndex = _CseMcastCacheIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 7, 1, 1, 1),
    _CseMcastCacheIndex_Type()
)
cseMcastCacheIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cseMcastCacheIndex.setStatus("current")


class _CseMcastCacheFlowType_Type(Integer32):
    """Custom type cseMcastCacheFlowType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("group", 2),
          ("grpAndSrc", 3))
    )


_CseMcastCacheFlowType_Type.__name__ = "Integer32"
_CseMcastCacheFlowType_Object = MibTableColumn
cseMcastCacheFlowType = _CseMcastCacheFlowType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 7, 1, 1, 2),
    _CseMcastCacheFlowType_Type()
)
cseMcastCacheFlowType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseMcastCacheFlowType.setStatus("current")
_CseMcastCacheGrp_Type = McastGroupIp
_CseMcastCacheGrp_Object = MibTableColumn
cseMcastCacheGrp = _CseMcastCacheGrp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 7, 1, 1, 3),
    _CseMcastCacheGrp_Type()
)
cseMcastCacheGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseMcastCacheGrp.setStatus("current")
_CseMcastCacheSrc_Type = IpAddress
_CseMcastCacheSrc_Object = MibTableColumn
cseMcastCacheSrc = _CseMcastCacheSrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 7, 1, 1, 4),
    _CseMcastCacheSrc_Type()
)
cseMcastCacheSrc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseMcastCacheSrc.setStatus("current")
_CseMcastCacheRtrIp_Type = IpAddress
_CseMcastCacheRtrIp_Object = MibTableColumn
cseMcastCacheRtrIp = _CseMcastCacheRtrIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 7, 1, 1, 5),
    _CseMcastCacheRtrIp_Type()
)
cseMcastCacheRtrIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseMcastCacheRtrIp.setStatus("current")
_CseMcastCacheOwner_Type = OwnerString
_CseMcastCacheOwner_Object = MibTableColumn
cseMcastCacheOwner = _CseMcastCacheOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 7, 1, 1, 6),
    _CseMcastCacheOwner_Type()
)
cseMcastCacheOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseMcastCacheOwner.setStatus("current")


class _CseMcastCacheResult_Type(Integer32):
    """Custom type cseMcastCacheResult based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notPurging", 2),
          ("purging", 1))
    )


_CseMcastCacheResult_Type.__name__ = "Integer32"
_CseMcastCacheResult_Object = MibTableColumn
cseMcastCacheResult = _CseMcastCacheResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 7, 1, 1, 7),
    _CseMcastCacheResult_Type()
)
cseMcastCacheResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseMcastCacheResult.setStatus("current")
_CseMcastCacheStatus_Type = RowStatus
_CseMcastCacheStatus_Object = MibTableColumn
cseMcastCacheStatus = _CseMcastCacheStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 7, 1, 1, 8),
    _CseMcastCacheStatus_Type()
)
cseMcastCacheStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cseMcastCacheStatus.setStatus("current")
_CseCef_ObjectIdentity = ObjectIdentity
cseCef = _CseCef_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 8)
)
_CseCefFibTable_Object = MibTable
cseCefFibTable = _CseCefFibTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 8, 1)
)
if mibBuilder.loadTexts:
    cseCefFibTable.setStatus("current")
_CseCefFibEntry_Object = MibTableRow
cseCefFibEntry = _CseCefFibEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 8, 1, 1)
)
cseCefFibEntry.setIndexNames(
    (0, "CISCO-SWITCH-ENGINE-MIB", "cseCefFibIndex"),
)
if mibBuilder.loadTexts:
    cseCefFibEntry.setStatus("current")
_CseCefFibIndex_Type = Unsigned32
_CseCefFibIndex_Object = MibTableColumn
cseCefFibIndex = _CseCefFibIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 8, 1, 1, 1),
    _CseCefFibIndex_Type()
)
cseCefFibIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cseCefFibIndex.setStatus("current")
_CseCefFibAddrType_Type = InetAddressType
_CseCefFibAddrType_Object = MibTableColumn
cseCefFibAddrType = _CseCefFibAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 8, 1, 1, 2),
    _CseCefFibAddrType_Type()
)
cseCefFibAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseCefFibAddrType.setStatus("current")
_CseCefFibDestIp_Type = InetAddress
_CseCefFibDestIp_Object = MibTableColumn
cseCefFibDestIp = _CseCefFibDestIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 8, 1, 1, 3),
    _CseCefFibDestIp_Type()
)
cseCefFibDestIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseCefFibDestIp.setStatus("current")
_CseCefFibDestIpMask_Type = InetAddress
_CseCefFibDestIpMask_Object = MibTableColumn
cseCefFibDestIpMask = _CseCefFibDestIpMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 8, 1, 1, 4),
    _CseCefFibDestIpMask_Type()
)
cseCefFibDestIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseCefFibDestIpMask.setStatus("current")


class _CseCefFibType_Type(Integer32):
    """Custom type cseCefFibType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("bridge", 3),
          ("connected", 5),
          ("default", 9),
          ("drop", 4),
          ("other", 1),
          ("receive", 6),
          ("resolved", 2),
          ("tunnel", 8),
          ("wildcard", 7))
    )


_CseCefFibType_Type.__name__ = "Integer32"
_CseCefFibType_Object = MibTableColumn
cseCefFibType = _CseCefFibType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 8, 1, 1, 5),
    _CseCefFibType_Type()
)
cseCefFibType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseCefFibType.setStatus("current")
_CseCefAdjacencyTable_Object = MibTable
cseCefAdjacencyTable = _CseCefAdjacencyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 8, 3)
)
if mibBuilder.loadTexts:
    cseCefAdjacencyTable.setStatus("current")
_CseCefAdjacencyEntry_Object = MibTableRow
cseCefAdjacencyEntry = _CseCefAdjacencyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 8, 3, 1)
)
cseCefAdjacencyEntry.setIndexNames(
    (0, "CISCO-SWITCH-ENGINE-MIB", "cseCefFibIndex"),
    (0, "CISCO-SWITCH-ENGINE-MIB", "cseCefAdjacencyIndex"),
)
if mibBuilder.loadTexts:
    cseCefAdjacencyEntry.setStatus("current")
_CseCefAdjacencyIndex_Type = Unsigned32
_CseCefAdjacencyIndex_Object = MibTableColumn
cseCefAdjacencyIndex = _CseCefAdjacencyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 8, 3, 1, 1),
    _CseCefAdjacencyIndex_Type()
)
cseCefAdjacencyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cseCefAdjacencyIndex.setStatus("current")
_CseCefAdjacencyAddrType_Type = InetAddressType
_CseCefAdjacencyAddrType_Object = MibTableColumn
cseCefAdjacencyAddrType = _CseCefAdjacencyAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 8, 3, 1, 2),
    _CseCefAdjacencyAddrType_Type()
)
cseCefAdjacencyAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseCefAdjacencyAddrType.setStatus("current")
_CseCefAdjacencyNextHopIp_Type = InetAddress
_CseCefAdjacencyNextHopIp_Object = MibTableColumn
cseCefAdjacencyNextHopIp = _CseCefAdjacencyNextHopIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 8, 3, 1, 3),
    _CseCefAdjacencyNextHopIp_Type()
)
cseCefAdjacencyNextHopIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseCefAdjacencyNextHopIp.setStatus("current")
_CseCefAdjacencyNextHopMac_Type = MacAddress
_CseCefAdjacencyNextHopMac_Object = MibTableColumn
cseCefAdjacencyNextHopMac = _CseCefAdjacencyNextHopMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 8, 3, 1, 4),
    _CseCefAdjacencyNextHopMac_Type()
)
cseCefAdjacencyNextHopMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseCefAdjacencyNextHopMac.setStatus("current")
_CseCefAdjacencyNextHopIfIndex_Type = InterfaceIndexOrZero
_CseCefAdjacencyNextHopIfIndex_Object = MibTableColumn
cseCefAdjacencyNextHopIfIndex = _CseCefAdjacencyNextHopIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 8, 3, 1, 5),
    _CseCefAdjacencyNextHopIfIndex_Type()
)
cseCefAdjacencyNextHopIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseCefAdjacencyNextHopIfIndex.setStatus("current")


class _CseCefAdjacencyType_Type(Integer32):
    """Custom type cseCefAdjacencyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("connect", 8),
          ("drop", 4),
          ("forceDrop", 7),
          ("glean", 3),
          ("loopback", 10),
          ("noRewrite", 6),
          ("null", 5),
          ("other", 1),
          ("punt", 2),
          ("tunnel", 11),
          ("unresolved", 9))
    )


_CseCefAdjacencyType_Type.__name__ = "Integer32"
_CseCefAdjacencyType_Object = MibTableColumn
cseCefAdjacencyType = _CseCefAdjacencyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 8, 3, 1, 6),
    _CseCefAdjacencyType_Type()
)
cseCefAdjacencyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseCefAdjacencyType.setStatus("current")
_CseCefAdjacencyPkts_Type = Counter64
_CseCefAdjacencyPkts_Object = MibTableColumn
cseCefAdjacencyPkts = _CseCefAdjacencyPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 8, 3, 1, 7),
    _CseCefAdjacencyPkts_Type()
)
cseCefAdjacencyPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseCefAdjacencyPkts.setStatus("current")
_CseCefAdjacencyOctets_Type = Counter64
_CseCefAdjacencyOctets_Object = MibTableColumn
cseCefAdjacencyOctets = _CseCefAdjacencyOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 8, 3, 1, 8),
    _CseCefAdjacencyOctets_Type()
)
cseCefAdjacencyOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseCefAdjacencyOctets.setStatus("current")


class _CseCefAdjacencyEncap_Type(Integer32):
    """Custom type cseCefAdjacencyEncap based on Integer32"""
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
        *(("arpa", 1),
          ("raw", 2),
          ("sap", 3),
          ("snap", 4))
    )


_CseCefAdjacencyEncap_Type.__name__ = "Integer32"
_CseCefAdjacencyEncap_Object = MibTableColumn
cseCefAdjacencyEncap = _CseCefAdjacencyEncap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 8, 3, 1, 9),
    _CseCefAdjacencyEncap_Type()
)
cseCefAdjacencyEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseCefAdjacencyEncap.setStatus("current")
_CseCefAdjacencyMTU_Type = Unsigned32
_CseCefAdjacencyMTU_Object = MibTableColumn
cseCefAdjacencyMTU = _CseCefAdjacencyMTU_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 8, 3, 1, 10),
    _CseCefAdjacencyMTU_Type()
)
cseCefAdjacencyMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseCefAdjacencyMTU.setStatus("current")
_CseTcamUsage_ObjectIdentity = ObjectIdentity
cseTcamUsage = _CseTcamUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 9)
)
_CseTcamUsageTable_Object = MibTable
cseTcamUsageTable = _CseTcamUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 9, 1)
)
if mibBuilder.loadTexts:
    cseTcamUsageTable.setStatus("current")
_CseTcamUsageEntry_Object = MibTableRow
cseTcamUsageEntry = _CseTcamUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 9, 1, 1)
)
cseTcamUsageEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-SWITCH-ENGINE-MIB", "cseTcamResourceType"),
)
if mibBuilder.loadTexts:
    cseTcamUsageEntry.setStatus("current")


class _CseTcamResourceType_Type(Integer32):
    """Custom type cseTcamResourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85)
        )
    )
    namedValues = NamedValues(
        *(("accounting", 27),
          ("aclAdjacency", 17),
          ("aclDynamicStorageMask", 3),
          ("aclDynamicStorageValue", 4),
          ("aclHighStorageMask", 18),
          ("aclHighStorageValue", 19),
          ("aclLowStorageMask", 20),
          ("aclLowStorageValue", 21),
          ("aclStorageMask", 1),
          ("aclStorageValue", 2),
          ("andOr", 15),
          ("anyAnyRegion", 32),
          ("bank0Aggregate", 43),
          ("bank1Aggregate", 44),
          ("bothLouOperands", 46),
          ("destInfo", 30),
          ("destInfoIn", 35),
          ("destInfoOut", 36),
          ("dgtSgtRegion", 31),
          ("egressBothLouOperands", 78),
          ("egressDestInfoTable", 63),
          ("egressInterfaceMapping", 12),
          ("egressIpv6Tcam", 76),
          ("egressLou", 77),
          ("egressLouL2Ttl", 84),
          ("egressLouL3PacketLength", 82),
          ("egressLouL3Ttl", 83),
          ("egressLouL4DstPort", 81),
          ("egressLouL4SourcePort", 80),
          ("egressSingleLouOperands", 79),
          ("egressTcam", 75),
          ("egressTcpFlags", 85),
          ("ethertype", 29),
          ("ingressBothLouOperands", 67),
          ("ingressDestInfoTable", 62),
          ("ingressInterfaceMapping", 11),
          ("ingressIpv6Tcam", 65),
          ("ingressLou", 66),
          ("ingressLouL2Ttl", 73),
          ("ingressLouL3PacketLength", 71),
          ("ingressLouL3Ttl", 72),
          ("ingressLouL4DstPort", 70),
          ("ingressLouL4SourcePort", 69),
          ("ingressSingleLouOperands", 68),
          ("ingressTcam", 64),
          ("ingressTcpFlags", 74),
          ("interfaceMapping", 10),
          ("ipv6Ext", 28),
          ("l4DynamicProtocolCam", 56),
          ("l4OpLabelTcam0", 60),
          ("l4OpLabelTcam1", 61),
          ("l4PortOperator", 9),
          ("lou", 45),
          ("louDestination", 14),
          ("louIpDscp", 52),
          ("louIpPrecedence", 53),
          ("louIpTos", 51),
          ("louIpTtl", 54),
          ("louL3PacketLength", 50),
          ("louL4DstPort", 49),
          ("louL4SourcePort", 48),
          ("louSource", 13),
          ("macEtypeOrProtoCam", 57),
          ("nonL4OpLabelsTcam0", 58),
          ("nonL4OpLabelsTcam1", 59),
          ("orAnd", 16),
          ("qosDynamicStorageMask", 7),
          ("qosDynamicStorageValue", 8),
          ("qosHighStorageMask", 22),
          ("qosHighStorageValue", 23),
          ("qosLowStorageMask", 24),
          ("qosLowStorageValue", 25),
          ("qosStorageMask", 5),
          ("qosStorageValue", 6),
          ("sgacl", 26),
          ("singleLouOperands", 47),
          ("tcam0Aggregate", 41),
          ("tcam0Bank0", 37),
          ("tcam0Bank1", 38),
          ("tcam1Aggregate", 42),
          ("tcam1Bank0", 39),
          ("tcam1Bank1", 40),
          ("tcamALabel", 33),
          ("tcamBLabel", 34),
          ("tcpFlags", 55))
    )


_CseTcamResourceType_Type.__name__ = "Integer32"
_CseTcamResourceType_Object = MibTableColumn
cseTcamResourceType = _CseTcamResourceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 9, 1, 1, 1),
    _CseTcamResourceType_Type()
)
cseTcamResourceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cseTcamResourceType.setStatus("current")
_CseTcamResourceDescr_Type = SnmpAdminString
_CseTcamResourceDescr_Object = MibTableColumn
cseTcamResourceDescr = _CseTcamResourceDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 9, 1, 1, 2),
    _CseTcamResourceDescr_Type()
)
cseTcamResourceDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseTcamResourceDescr.setStatus("current")
_CseTcamResourceUsed_Type = Unsigned32
_CseTcamResourceUsed_Object = MibTableColumn
cseTcamResourceUsed = _CseTcamResourceUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 9, 1, 1, 3),
    _CseTcamResourceUsed_Type()
)
cseTcamResourceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseTcamResourceUsed.setStatus("current")
_CseTcamResourceTotal_Type = Unsigned32
_CseTcamResourceTotal_Object = MibTableColumn
cseTcamResourceTotal = _CseTcamResourceTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 9, 1, 1, 4),
    _CseTcamResourceTotal_Type()
)
cseTcamResourceTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseTcamResourceTotal.setStatus("current")
_CseMet_ObjectIdentity = ObjectIdentity
cseMet = _CseMet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 10)
)
_CseMetUsageTable_Object = MibTable
cseMetUsageTable = _CseMetUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 10, 1)
)
if mibBuilder.loadTexts:
    cseMetUsageTable.setStatus("current")
_CseMetUsageEntry_Object = MibTableRow
cseMetUsageEntry = _CseMetUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 10, 1, 1)
)
cseMetUsageEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-SWITCH-ENGINE-MIB", "cseMetIndex"),
)
if mibBuilder.loadTexts:
    cseMetUsageEntry.setStatus("current")
_CseMetIndex_Type = Unsigned32
_CseMetIndex_Object = MibTableColumn
cseMetIndex = _CseMetIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 10, 1, 1, 1),
    _CseMetIndex_Type()
)
cseMetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cseMetIndex.setStatus("current")
_CseMetTotalEntries_Type = Unsigned32
_CseMetTotalEntries_Object = MibTableColumn
cseMetTotalEntries = _CseMetTotalEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 10, 1, 1, 2),
    _CseMetTotalEntries_Type()
)
cseMetTotalEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseMetTotalEntries.setStatus("current")
_CseMetUnallocatedSpcFreeEntries_Type = Unsigned32
_CseMetUnallocatedSpcFreeEntries_Object = MibTableColumn
cseMetUnallocatedSpcFreeEntries = _CseMetUnallocatedSpcFreeEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 10, 1, 1, 3),
    _CseMetUnallocatedSpcFreeEntries_Type()
)
cseMetUnallocatedSpcFreeEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseMetUnallocatedSpcFreeEntries.setStatus("current")
_CseMetAllocatedSpcFreeEntries_Type = Unsigned32
_CseMetAllocatedSpcFreeEntries_Object = MibTableColumn
cseMetAllocatedSpcFreeEntries = _CseMetAllocatedSpcFreeEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 10, 1, 1, 4),
    _CseMetAllocatedSpcFreeEntries_Type()
)
cseMetAllocatedSpcFreeEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseMetAllocatedSpcFreeEntries.setStatus("current")
_CseMIBNotifications_ObjectIdentity = ObjectIdentity
cseMIBNotifications = _CseMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 2)
)
_CseMIBConformance_ObjectIdentity = ObjectIdentity
cseMIBConformance = _CseMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3)
)
_CseMIBCompliances_ObjectIdentity = ObjectIdentity
cseMIBCompliances = _CseMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 1)
)
_CseMIBGroups_ObjectIdentity = ObjectIdentity
cseMIBGroups = _CseMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 2)
)
cseL3StatsEntry.registerAugmentions(
    ("CISCO-SWITCH-ENGINE-MIB",
     "cseStatsFlowEntry")
)
cseStatsFlowEntry.setIndexNames(*cseL3StatsEntry.getIndexNames())

# Managed Objects groups

cseStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 2, 1)
)
cseStatisticsGroup.setObjects(
      *(("CISCO-SWITCH-ENGINE-MIB", "cseL2ForwardedLocalPkts"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseL2ForwardedLocalOctets"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseL2ForwardedTotalPkts"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseL2NewAddressLearns"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseL2AddrLearnFailures"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseL2DstAddrLookupMisses"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseL3SwitchedTotalPkts"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseL3SwitchedTotalOctets"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseL3CandidateFlowHits"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseL3EstablishedFlowHits"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseL3ActiveFlows"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseL3FlowLearnFailures"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseL3IntFlowInvalids"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseL3ExtFlowInvalids"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseL2HCOverflowForwardedLocalPkts"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseL2HCForwardedLocalPkts"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseL2HCOverflowForwardedTotalPkts"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseL2HCForwardedTotalPkts"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseL2HCOverflowIpPkts"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseL2HCIpPkts"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseL2HCOverflowIpxPkts"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseL2HCIpxPkts"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseL2HCOverflowAssignedProtoPkts"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseL2HCAssignedProtoPkts"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseL2HCOverflowOtherProtoPkts"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseL2HCOtherProtoPkts"))
)
if mibBuilder.loadTexts:
    cseStatisticsGroup.setStatus("current")

cseStatisticsGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 2, 2)
)
cseStatisticsGroup2.setObjects(
      *(("CISCO-SWITCH-ENGINE-MIB", "cseStatsFlowAged"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseStatsFlowPurged"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseStatsFlowParityFail"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseCacheUtilization"))
)
if mibBuilder.loadTexts:
    cseStatisticsGroup2.setStatus("current")

cseVlanStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 2, 3)
)
cseVlanStatisticsGroup.setObjects(
      *(("CISCO-SWITCH-ENGINE-MIB", "cseL3VlanInPkts"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseL3VlanInOctets"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseL3VlanOutPkts"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseL3VlanOutOctets"))
)
if mibBuilder.loadTexts:
    cseVlanStatisticsGroup.setStatus("current")

cseRouterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 2, 4)
)
cseRouterGroup.setObjects(
      *(("CISCO-SWITCH-ENGINE-MIB", "cseRouterFlowMask"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseRouterName"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseRouterStatic"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseStaticRouterOwner"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseStaticRouterName"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseStaticRouterType"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseStaticRouterStatus"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseRouterIpxFlowMask"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseStaticIpxRouterOwner"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseStaticIpxRouterName"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseStaticIpxRouterStatus"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseRouterMac"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseRouterProtocol"))
)
if mibBuilder.loadTexts:
    cseRouterGroup.setStatus("current")

cseFlowMgmtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 2, 5)
)
cseFlowMgmtGroup.setObjects(
      *(("CISCO-SWITCH-ENGINE-MIB", "cseFlowEstablishedAgingTime"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowFastAgingTime"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowFastAgePktThreshold"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowIPXEstablishedAgingTime"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMaxQueries"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowQueryMask"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowQueryTransport"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowQuerySource"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowQuerySourceMask"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowQueryDestination"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowQueryDestinationMask"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowQueryRouterIndex"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowQueryOwner"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowQueryResultingRows"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowQueryResultTotalPkts"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowQueryResultTotalOctets"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowQueryResultAvgDuration"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowQueryResultAvgIdle"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowQueryStatus"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowQueryCreateTime"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowDataSrcMac"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowDataDstMac"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowDataEncapType"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowDataSource"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowDataStaticFlow"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowDataDestination"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowDataDestVlan"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowDataIpQOS"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowDataIpQOSPolicy"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowDataWhenCreated"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowDataLastUsed"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowDataPkts"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowDataOctets"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowSwitchStatus"))
)
if mibBuilder.loadTexts:
    cseFlowMgmtGroup.setStatus("deprecated")

cseNetflowLSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 2, 6)
)
cseNetflowLSGroup.setObjects(
      *(("CISCO-SWITCH-ENGINE-MIB", "cseNetflowLSExportHost"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseNetflowLSExportTransportNumber"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseNetflowLSExportStatus"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseNetflowLSExportDataSource"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseNetflowLSExportDataSourceMask"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseNetflowLSExportDataDest"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseNetflowLSExportDataDestMask"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseNetflowLSExportDataProtocol"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseNetflowLSExportDataFilterSelection"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseNetflowLSExportNDEVersionNumber"))
)
if mibBuilder.loadTexts:
    cseNetflowLSGroup.setStatus("deprecated")

cseProtocolFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 2, 7)
)
cseProtocolFilterGroup.setObjects(
      *(("CISCO-SWITCH-ENGINE-MIB", "cseProtocolFilterPortAdminStatus"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseProtocolFilterPortOperStatus"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseL2IpPkts"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseL2IpxPkts"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseL2AssignedProtoPkts"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseL2OtherProtoPkts"))
)
if mibBuilder.loadTexts:
    cseProtocolFilterGroup.setStatus("current")

cseFlowMcastMgmtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 2, 8)
)
cseFlowMcastMgmtGroup.setObjects(
      *(("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastMaxQueries"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastQueryMask"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastQuerySrc"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastQueryGrp"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastQuerySrcVlan"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastQueryRtrIndex"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastQuerySkipNFlows"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastQueryOwner"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastQueryTotalFlows"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastQueryRows"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastQueryStatus"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastQueryCreateTime"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastResultSrc"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastResultGrp"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastResultSrcVlan"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastResultRtrIp"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastResultRtrMac"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastResultCreatedTS"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastResultLastUsedTS"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastResultPkts"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastResultOctets"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastResultDstVlans"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastSwitchStatus"))
)
if mibBuilder.loadTexts:
    cseFlowMcastMgmtGroup.setStatus("deprecated")

cseUcastCachePurgeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 2, 9)
)
cseUcastCachePurgeGroup.setObjects(
      *(("CISCO-SWITCH-ENGINE-MIB", "cseUcastCacheFlowType"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseUcastCacheTransport"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseUcastCacheDest"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseUcastCacheDestMask"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseUcastCacheSource"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseUcastCacheSrcMask"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseUcastCacheRtrIp"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseUcastCacheOwner"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseUcastCacheStatus"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseUcastCacheResult"))
)
if mibBuilder.loadTexts:
    cseUcastCachePurgeGroup.setStatus("current")

cseMcastCachePurgeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 2, 10)
)
cseMcastCachePurgeGroup.setObjects(
      *(("CISCO-SWITCH-ENGINE-MIB", "cseMcastCacheFlowType"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseMcastCacheGrp"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseMcastCacheSrc"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseMcastCacheRtrIp"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseMcastCacheOwner"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseMcastCacheStatus"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseMcastCacheResult"))
)
if mibBuilder.loadTexts:
    cseMcastCachePurgeGroup.setStatus("current")

cseFlowMgmtOperStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 2, 11)
)
cseFlowMgmtOperStatusGroup.setObjects(
      *(("CISCO-SWITCH-ENGINE-MIB", "cseFlowOperEstablishedAgingTime"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowOperFastAgingTime"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowOperFastAgePktThreshold"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowOperIPXAgingTime"))
)
if mibBuilder.loadTexts:
    cseFlowMgmtOperStatusGroup.setStatus("current")

cse4kVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 2, 12)
)
cse4kVlanGroup.setObjects(
      *(("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastResultDstVlans2k"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastResultDstVlans3k"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastResultDstVlans4k"))
)
if mibBuilder.loadTexts:
    cse4kVlanGroup.setStatus("current")

cseNDEMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 2, 13)
)
cseNDEMandatoryGroup.setObjects(
      *(("CISCO-SWITCH-ENGINE-MIB", "cseNetflowLSFilterSupport"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseNetflowLSExportStatus"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseNetflowLSExportNDEVersionNumber"))
)
if mibBuilder.loadTexts:
    cseNDEMandatoryGroup.setStatus("current")

cseNDESingleFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 2, 14)
)
cseNDESingleFilterGroup.setObjects(
      *(("CISCO-SWITCH-ENGINE-MIB", "cseNetflowLSExportHost"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseNetflowLSExportTransportNumber"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseNetflowLSExportDataSource"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseNetflowLSExportDataSourceMask"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseNetflowLSExportDataDest"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseNetflowLSExportDataDestMask"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseNetflowLSExportDataProtocol"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseNetflowLSExportDataFilterSelection"))
)
if mibBuilder.loadTexts:
    cseNDESingleFilterGroup.setStatus("deprecated")

cseNDEMultipleFiltersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 2, 15)
)
cseNDEMultipleFiltersGroup.setObjects(
      *(("CISCO-SWITCH-ENGINE-MIB", "cseNetflowLSFilterDataSource"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseNetflowLSFilterDataSourceMask"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseNetflowLSFilterDataDest"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseNetflowLSFilterDataDestMask"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseNetflowLSFilterDataProtocol"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseNetflowLSFilterSelection"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseNetflowLSFilterStatus"))
)
if mibBuilder.loadTexts:
    cseNDEMultipleFiltersGroup.setStatus("current")

cseFlowMgmtGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 2, 16)
)
cseFlowMgmtGroupRev1.setObjects(
      *(("CISCO-SWITCH-ENGINE-MIB", "cseFlowEstablishedAgingTime"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowFastAgingTime"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowFastAgePktThreshold"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowIPXEstablishedAgingTime"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMaxQueries"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowQueryMask"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowQueryTransport"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowQuerySource"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowQuerySourceMask"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowQueryDestination"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowQueryDestinationMask"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowQueryRouterIndex"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowQueryOwner"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowQueryResultingRows"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowQueryResultTotalPkts"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowQueryResultTotalOctets"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowQueryResultAvgDuration"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowQueryResultAvgIdle"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowQueryStatus"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowQueryCreateTime"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowQueryTotalFlows"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowDataSrcMac"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowDataDstMac"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowDataEncapType"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowDataSource"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowDataStaticFlow"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowDataDestination"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowDataDestVlan"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowDataIpQOS"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowDataIpQOSPolicy"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowDataWhenCreated"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowDataLastUsed"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowDataPkts"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowDataOctets"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowSwitchStatus"))
)
if mibBuilder.loadTexts:
    cseFlowMgmtGroupRev1.setStatus("current")

cseL3ErrorsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 2, 17)
)
cseL3ErrorsGroup.setObjects(
      *(("CISCO-SWITCH-ENGINE-MIB", "cseIpPlenErrors"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseIpTooShortErrors"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseIpCheckSumErrors"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseIpxPlenErrors"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseIpxTooShortErrors"))
)
if mibBuilder.loadTexts:
    cseL3ErrorsGroup.setStatus("current")

cseBridgedFlowGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 2, 18)
)
cseBridgedFlowGroup.setObjects(
    ("CISCO-SWITCH-ENGINE-MIB", "cseFlowBridgedFlowStatsEnable")
)
if mibBuilder.loadTexts:
    cseBridgedFlowGroup.setStatus("current")

cseVlanStatisticsExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 2, 19)
)
cseVlanStatisticsExtGroup.setObjects(
      *(("CISCO-SWITCH-ENGINE-MIB", "cseL3VlanInUnicastPkts"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseL3VlanInUnicastOctets"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseL3VlanOutUnicastPkts"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseL3VlanOutUnicastOctets"))
)
if mibBuilder.loadTexts:
    cseVlanStatisticsExtGroup.setStatus("current")

cseProtocolFilterExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 2, 20)
)
cseProtocolFilterExtGroup.setObjects(
    ("CISCO-SWITCH-ENGINE-MIB", "cseProtocolFilterEnable")
)
if mibBuilder.loadTexts:
    cseProtocolFilterExtGroup.setStatus("current")

cseFlowMgmtExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 2, 21)
)
cseFlowMgmtExtGroup.setObjects(
      *(("CISCO-SWITCH-ENGINE-MIB", "cseFlowIPFlowMask"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowIPXFlowMask"))
)
if mibBuilder.loadTexts:
    cseFlowMgmtExtGroup.setStatus("current")

cseFlowMgmtExtGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 2, 22)
)
cseFlowMgmtExtGroup1.setObjects(
      *(("CISCO-SWITCH-ENGINE-MIB", "cseFlowLongAgingTime"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowExcludeProtocol"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowExcludeStatus"))
)
if mibBuilder.loadTexts:
    cseFlowMgmtExtGroup1.setStatus("current")

cseNDEReportGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 2, 23)
)
cseNDEReportGroup.setObjects(
    ("CISCO-SWITCH-ENGINE-MIB", "cseNetFlowIfIndexEnable")
)
if mibBuilder.loadTexts:
    cseNDEReportGroup.setStatus("current")

cseStatisticsFlowGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 2, 24)
)
cseStatisticsFlowGroup.setObjects(
    ("CISCO-SWITCH-ENGINE-MIB", "cseFlowTotalFlows")
)
if mibBuilder.loadTexts:
    cseStatisticsFlowGroup.setStatus("current")

cseFlowMgmtExtGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 2, 25)
)
cseFlowMgmtExtGroup2.setObjects(
    ("CISCO-SWITCH-ENGINE-MIB", "cseFlowQuerySkipNFlows")
)
if mibBuilder.loadTexts:
    cseFlowMgmtExtGroup2.setStatus("current")

cseNDESingleFilterGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 2, 26)
)
cseNDESingleFilterGroupRev1.setObjects(
      *(("CISCO-SWITCH-ENGINE-MIB", "cseNetflowLSExportDataSource"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseNetflowLSExportDataSourceMask"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseNetflowLSExportDataDest"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseNetflowLSExportDataDestMask"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseNetflowLSExportDataProtocol"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseNetflowLSExportDataFilterSelection"))
)
if mibBuilder.loadTexts:
    cseNDESingleFilterGroupRev1.setStatus("current")

cseCefFibAdjacencyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 2, 27)
)
cseCefFibAdjacencyGroup.setObjects(
      *(("CISCO-SWITCH-ENGINE-MIB", "cseCefFibAddrType"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseCefFibDestIp"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseCefFibDestIpMask"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseCefFibType"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseCefAdjacencyAddrType"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseCefAdjacencyNextHopIp"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseCefAdjacencyNextHopMac"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseCefAdjacencyNextHopIfIndex"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseCefAdjacencyType"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseCefAdjacencyPkts"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseCefAdjacencyOctets"))
)
if mibBuilder.loadTexts:
    cseCefFibAdjacencyGroup.setStatus("current")

cseCefAdjacencyEncapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 2, 28)
)
cseCefAdjacencyEncapGroup.setObjects(
    ("CISCO-SWITCH-ENGINE-MIB", "cseCefAdjacencyEncap")
)
if mibBuilder.loadTexts:
    cseCefAdjacencyEncapGroup.setStatus("current")

cseCefAdjacencyMTUGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 2, 29)
)
cseCefAdjacencyMTUGroup.setObjects(
    ("CISCO-SWITCH-ENGINE-MIB", "cseCefAdjacencyMTU")
)
if mibBuilder.loadTexts:
    cseCefAdjacencyMTUGroup.setStatus("current")

cseTcamUsageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 2, 30)
)
cseTcamUsageGroup.setObjects(
      *(("CISCO-SWITCH-ENGINE-MIB", "cseTcamResourceDescr"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseTcamResourceUsed"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseTcamResourceTotal"))
)
if mibBuilder.loadTexts:
    cseTcamUsageGroup.setStatus("current")

cseL3ErrorsLCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 2, 31)
)
cseL3ErrorsLCGroup.setObjects(
      *(("CISCO-SWITCH-ENGINE-MIB", "cseLCIpPlenErrors"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseLCIpTooShortErrors"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseLCIpCheckSumErrors"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseLCIpxPlenErrors"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseLCIpxTooShortErrors"))
)
if mibBuilder.loadTexts:
    cseL3ErrorsLCGroup.setStatus("current")

cseNetflowASInfoExportGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 2, 32)
)
cseNetflowASInfoExportGroup.setObjects(
    ("CISCO-SWITCH-ENGINE-MIB", "cseNetflowASInfoExportCtrl")
)
if mibBuilder.loadTexts:
    cseNetflowASInfoExportGroup.setStatus("current")

cseNetflowPerVlanIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 2, 33)
)
cseNetflowPerVlanIfGroup.setObjects(
      *(("CISCO-SWITCH-ENGINE-MIB", "cseNetflowPerVlanIfGlobalEnable"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseNetflowPerVlanIfEnable"))
)
if mibBuilder.loadTexts:
    cseNetflowPerVlanIfGroup.setStatus("current")

cseMetUsageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 2, 34)
)
cseMetUsageGroup.setObjects(
      *(("CISCO-SWITCH-ENGINE-MIB", "cseMetTotalEntries"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseMetUnallocatedSpcFreeEntries"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseMetAllocatedSpcFreeEntries"))
)
if mibBuilder.loadTexts:
    cseMetUsageGroup.setStatus("current")

cseFlowMcastMgmtGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 2, 35)
)
cseFlowMcastMgmtGroup1.setObjects(
      *(("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastMaxQueries"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastQueryMask"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastQuerySrcVlan"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastQuerySkipNFlows"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastQueryOwner"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastQueryTotalFlows"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastQueryRows"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastQueryStatus"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastQueryCreateTime"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastResultSrcVlan"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastResultCreatedTS"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastResultLastUsedTS"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastResultPkts"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastResultOctets"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastResultDstVlans"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastSwitchStatus"))
)
if mibBuilder.loadTexts:
    cseFlowMcastMgmtGroup1.setStatus("current")

cseFlowMcastRtrMgmtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 2, 36)
)
cseFlowMcastRtrMgmtGroup.setObjects(
      *(("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastQueryRtrIndex"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastResultRtrIp"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastResultRtrMac"))
)
if mibBuilder.loadTexts:
    cseFlowMcastRtrMgmtGroup.setStatus("current")

cseFlowMcastMgmtGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 2, 37)
)
cseFlowMcastMgmtGroup2.setObjects(
      *(("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastQueryMvrf"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastQueryAddrType"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastQuerySource"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastQueryGroup"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastResultMvrf"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastResultAddrType"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastResultGroup"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastResultSource"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastResultFlowType"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastResultHFlag1k2k"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseFlowMcastResultHFlag3k4k"))
)
if mibBuilder.loadTexts:
    cseFlowMcastMgmtGroup2.setStatus("current")

cseCacheStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 2, 38)
)
cseCacheStatisticsGroup.setObjects(
      *(("CISCO-SWITCH-ENGINE-MIB", "cseCacheEntriesCreated"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseCacheEntriesFailed"))
)
if mibBuilder.loadTexts:
    cseCacheStatisticsGroup.setStatus("current")

cseL3SwitchedPktsPerSecGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 2, 39)
)
cseL3SwitchedPktsPerSecGroup.setObjects(
      *(("CISCO-SWITCH-ENGINE-MIB", "cseL3SwitchedPktsPerSec"),
        ("CISCO-SWITCH-ENGINE-MIB", "cseL3SwitchedAggrPktsPerSec"))
)
if mibBuilder.loadTexts:
    cseL3SwitchedPktsPerSecGroup.setStatus("current")

cseStatisticsFlowGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 2, 40)
)
cseStatisticsFlowGroup1.setObjects(
    ("CISCO-SWITCH-ENGINE-MIB", "cseFlowTotalIpv4Flows")
)
if mibBuilder.loadTexts:
    cseStatisticsFlowGroup1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cseMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cseMIBCompliance.setStatus(
        "deprecated"
    )

cseMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cseMIBCompliance2.setStatus(
        "deprecated"
    )

cseMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 1, 3)
)
if mibBuilder.loadTexts:
    cseMIBCompliance3.setStatus(
        "deprecated"
    )

cseMIBCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 1, 4)
)
if mibBuilder.loadTexts:
    cseMIBCompliance4.setStatus(
        "deprecated"
    )

cseMIBCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 1, 5)
)
if mibBuilder.loadTexts:
    cseMIBCompliance5.setStatus(
        "deprecated"
    )

cseMIBCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 1, 6)
)
if mibBuilder.loadTexts:
    cseMIBCompliance6.setStatus(
        "deprecated"
    )

cseMIBCompliance7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 1, 7)
)
if mibBuilder.loadTexts:
    cseMIBCompliance7.setStatus(
        "deprecated"
    )

cseMIBCompliance8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 1, 8)
)
if mibBuilder.loadTexts:
    cseMIBCompliance8.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SWITCH-ENGINE-MIB",
    **{"CiscoGauge64": CiscoGauge64,
       "ControlStatus": ControlStatus,
       "McastGroupIp": McastGroupIp,
       "FlowAddressComponent": FlowAddressComponent,
       "ciscoSwitchEngineMIB": ciscoSwitchEngineMIB,
       "cseMIBObjects": cseMIBObjects,
       "cseL2Objects": cseL2Objects,
       "cseL2StatsTable": cseL2StatsTable,
       "cseL2StatsEntry": cseL2StatsEntry,
       "cseL2ForwardedLocalPkts": cseL2ForwardedLocalPkts,
       "cseL2ForwardedLocalOctets": cseL2ForwardedLocalOctets,
       "cseL2ForwardedTotalPkts": cseL2ForwardedTotalPkts,
       "cseL2NewAddressLearns": cseL2NewAddressLearns,
       "cseL2AddrLearnFailures": cseL2AddrLearnFailures,
       "cseL2DstAddrLookupMisses": cseL2DstAddrLookupMisses,
       "cseL2IpPkts": cseL2IpPkts,
       "cseL2IpxPkts": cseL2IpxPkts,
       "cseL2AssignedProtoPkts": cseL2AssignedProtoPkts,
       "cseL2OtherProtoPkts": cseL2OtherProtoPkts,
       "cseL2StatsHCTable": cseL2StatsHCTable,
       "cseL2StatsHCEntry": cseL2StatsHCEntry,
       "cseL2HCOverflowForwardedLocalPkts": cseL2HCOverflowForwardedLocalPkts,
       "cseL2HCForwardedLocalPkts": cseL2HCForwardedLocalPkts,
       "cseL2HCOverflowForwardedTotalPkts": cseL2HCOverflowForwardedTotalPkts,
       "cseL2HCForwardedTotalPkts": cseL2HCForwardedTotalPkts,
       "cseL2HCOverflowIpPkts": cseL2HCOverflowIpPkts,
       "cseL2HCIpPkts": cseL2HCIpPkts,
       "cseL2HCOverflowIpxPkts": cseL2HCOverflowIpxPkts,
       "cseL2HCIpxPkts": cseL2HCIpxPkts,
       "cseL2HCOverflowAssignedProtoPkts": cseL2HCOverflowAssignedProtoPkts,
       "cseL2HCAssignedProtoPkts": cseL2HCAssignedProtoPkts,
       "cseL2HCOverflowOtherProtoPkts": cseL2HCOverflowOtherProtoPkts,
       "cseL2HCOtherProtoPkts": cseL2HCOtherProtoPkts,
       "cseFlow": cseFlow,
       "cseFlowEstablishedAgingTime": cseFlowEstablishedAgingTime,
       "cseFlowFastAgingTime": cseFlowFastAgingTime,
       "cseFlowFastAgePktThreshold": cseFlowFastAgePktThreshold,
       "cseRouterTable": cseRouterTable,
       "cseRouterEntry": cseRouterEntry,
       "cseRouterIndex": cseRouterIndex,
       "cseRouterFlowMask": cseRouterFlowMask,
       "cseRouterName": cseRouterName,
       "cseRouterStatic": cseRouterStatic,
       "cseRouterIpxFlowMask": cseRouterIpxFlowMask,
       "cseStaticExtRouterTable": cseStaticExtRouterTable,
       "cseStaticExtRouterEntry": cseStaticExtRouterEntry,
       "cseStaticRouterName": cseStaticRouterName,
       "cseStaticRouterOwner": cseStaticRouterOwner,
       "cseStaticRouterStatus": cseStaticRouterStatus,
       "cseStaticRouterType": cseStaticRouterType,
       "cseRouterVlanTable": cseRouterVlanTable,
       "cseRouterVlanEntry": cseRouterVlanEntry,
       "cseRouterMac": cseRouterMac,
       "cseRouterVlan": cseRouterVlan,
       "cseRouterProtocol": cseRouterProtocol,
       "cseFlowMaxQueries": cseFlowMaxQueries,
       "cseFlowQueryTable": cseFlowQueryTable,
       "cseFlowQueryEntry": cseFlowQueryEntry,
       "cseFlowQueryIndex": cseFlowQueryIndex,
       "cseFlowQueryMask": cseFlowQueryMask,
       "cseFlowQueryTransport": cseFlowQueryTransport,
       "cseFlowQuerySource": cseFlowQuerySource,
       "cseFlowQuerySourceMask": cseFlowQuerySourceMask,
       "cseFlowQueryDestination": cseFlowQueryDestination,
       "cseFlowQueryDestinationMask": cseFlowQueryDestinationMask,
       "cseFlowQueryRouterIndex": cseFlowQueryRouterIndex,
       "cseFlowQueryOwner": cseFlowQueryOwner,
       "cseFlowQueryResultingRows": cseFlowQueryResultingRows,
       "cseFlowQueryResultTotalPkts": cseFlowQueryResultTotalPkts,
       "cseFlowQueryResultTotalOctets": cseFlowQueryResultTotalOctets,
       "cseFlowQueryResultAvgDuration": cseFlowQueryResultAvgDuration,
       "cseFlowQueryResultAvgIdle": cseFlowQueryResultAvgIdle,
       "cseFlowQueryStatus": cseFlowQueryStatus,
       "cseFlowQueryCreateTime": cseFlowQueryCreateTime,
       "cseFlowQueryTotalFlows": cseFlowQueryTotalFlows,
       "cseFlowQuerySkipNFlows": cseFlowQuerySkipNFlows,
       "cseFlowDataTable": cseFlowDataTable,
       "cseFlowDataEntry": cseFlowDataEntry,
       "cseFlowDataIndex": cseFlowDataIndex,
       "cseFlowDataSrcMac": cseFlowDataSrcMac,
       "cseFlowDataDstMac": cseFlowDataDstMac,
       "cseFlowDataStaticFlow": cseFlowDataStaticFlow,
       "cseFlowDataEncapType": cseFlowDataEncapType,
       "cseFlowDataSource": cseFlowDataSource,
       "cseFlowDataDestination": cseFlowDataDestination,
       "cseFlowDataDestVlan": cseFlowDataDestVlan,
       "cseFlowDataIpQOS": cseFlowDataIpQOS,
       "cseFlowDataIpQOSPolicy": cseFlowDataIpQOSPolicy,
       "cseFlowDataWhenCreated": cseFlowDataWhenCreated,
       "cseFlowDataLastUsed": cseFlowDataLastUsed,
       "cseFlowDataPkts": cseFlowDataPkts,
       "cseFlowDataOctets": cseFlowDataOctets,
       "cseFlowSwitchControlTable": cseFlowSwitchControlTable,
       "cseFlowSwitchControlEntry": cseFlowSwitchControlEntry,
       "cseFlowSwitchProtocol": cseFlowSwitchProtocol,
       "cseFlowSwitchStatus": cseFlowSwitchStatus,
       "cseFlowMcastMaxQueries": cseFlowMcastMaxQueries,
       "cseFlowMcastQueryTable": cseFlowMcastQueryTable,
       "cseFlowMcastQueryEntry": cseFlowMcastQueryEntry,
       "cseFlowMcastQueryIndex": cseFlowMcastQueryIndex,
       "cseFlowMcastQueryMask": cseFlowMcastQueryMask,
       "cseFlowMcastQuerySrc": cseFlowMcastQuerySrc,
       "cseFlowMcastQueryGrp": cseFlowMcastQueryGrp,
       "cseFlowMcastQuerySrcVlan": cseFlowMcastQuerySrcVlan,
       "cseFlowMcastQueryRtrIndex": cseFlowMcastQueryRtrIndex,
       "cseFlowMcastQuerySkipNFlows": cseFlowMcastQuerySkipNFlows,
       "cseFlowMcastQueryOwner": cseFlowMcastQueryOwner,
       "cseFlowMcastQueryTotalFlows": cseFlowMcastQueryTotalFlows,
       "cseFlowMcastQueryRows": cseFlowMcastQueryRows,
       "cseFlowMcastQueryStatus": cseFlowMcastQueryStatus,
       "cseFlowMcastQueryCreateTime": cseFlowMcastQueryCreateTime,
       "cseFlowMcastQueryMvrf": cseFlowMcastQueryMvrf,
       "cseFlowMcastQueryAddrType": cseFlowMcastQueryAddrType,
       "cseFlowMcastQuerySource": cseFlowMcastQuerySource,
       "cseFlowMcastQueryGroup": cseFlowMcastQueryGroup,
       "cseFlowMcastResultTable": cseFlowMcastResultTable,
       "cseFlowMcastResultEntry": cseFlowMcastResultEntry,
       "cseFlowMcastResultIndex": cseFlowMcastResultIndex,
       "cseFlowMcastResultGrp": cseFlowMcastResultGrp,
       "cseFlowMcastResultSrc": cseFlowMcastResultSrc,
       "cseFlowMcastResultSrcVlan": cseFlowMcastResultSrcVlan,
       "cseFlowMcastResultRtrIp": cseFlowMcastResultRtrIp,
       "cseFlowMcastResultRtrMac": cseFlowMcastResultRtrMac,
       "cseFlowMcastResultCreatedTS": cseFlowMcastResultCreatedTS,
       "cseFlowMcastResultLastUsedTS": cseFlowMcastResultLastUsedTS,
       "cseFlowMcastResultPkts": cseFlowMcastResultPkts,
       "cseFlowMcastResultOctets": cseFlowMcastResultOctets,
       "cseFlowMcastResultDstVlans": cseFlowMcastResultDstVlans,
       "cseFlowMcastResultDstVlans2k": cseFlowMcastResultDstVlans2k,
       "cseFlowMcastResultDstVlans3k": cseFlowMcastResultDstVlans3k,
       "cseFlowMcastResultDstVlans4k": cseFlowMcastResultDstVlans4k,
       "cseFlowMcastResultMvrf": cseFlowMcastResultMvrf,
       "cseFlowMcastResultAddrType": cseFlowMcastResultAddrType,
       "cseFlowMcastResultGroup": cseFlowMcastResultGroup,
       "cseFlowMcastResultSource": cseFlowMcastResultSource,
       "cseFlowMcastResultFlowType": cseFlowMcastResultFlowType,
       "cseFlowMcastResultHFlag1k2k": cseFlowMcastResultHFlag1k2k,
       "cseFlowMcastResultHFlag3k4k": cseFlowMcastResultHFlag3k4k,
       "cseFlowMcastSwitchStatus": cseFlowMcastSwitchStatus,
       "cseFlowIPXEstablishedAgingTime": cseFlowIPXEstablishedAgingTime,
       "cseStaticIpxExtRouterTable": cseStaticIpxExtRouterTable,
       "cseStaticIpxExtRouterEntry": cseStaticIpxExtRouterEntry,
       "cseStaticIpxRouterName": cseStaticIpxRouterName,
       "cseStaticIpxRouterOwner": cseStaticIpxRouterOwner,
       "cseStaticIpxRouterStatus": cseStaticIpxRouterStatus,
       "cseFlowOperEstablishedAgingTime": cseFlowOperEstablishedAgingTime,
       "cseFlowOperFastAgingTime": cseFlowOperFastAgingTime,
       "cseFlowOperFastAgePktThreshold": cseFlowOperFastAgePktThreshold,
       "cseFlowOperIPXAgingTime": cseFlowOperIPXAgingTime,
       "cseBridgedFlowStatsCtrlTable": cseBridgedFlowStatsCtrlTable,
       "cseBridgedFlowStatsCtrlEntry": cseBridgedFlowStatsCtrlEntry,
       "cseBridgedFlowVlan": cseBridgedFlowVlan,
       "cseFlowBridgedFlowStatsEnable": cseFlowBridgedFlowStatsEnable,
       "cseFlowIPFlowMask": cseFlowIPFlowMask,
       "cseFlowIPXFlowMask": cseFlowIPXFlowMask,
       "cseFlowLongAgingTime": cseFlowLongAgingTime,
       "cseFlowExcludeTable": cseFlowExcludeTable,
       "cseFlowExcludeEntry": cseFlowExcludeEntry,
       "cseFlowExcludePort": cseFlowExcludePort,
       "cseFlowExcludeProtocol": cseFlowExcludeProtocol,
       "cseFlowExcludeStatus": cseFlowExcludeStatus,
       "cseFlowStatsTable": cseFlowStatsTable,
       "cseFlowStatsEntry": cseFlowStatsEntry,
       "cseFlowTotalFlows": cseFlowTotalFlows,
       "cseFlowTotalIpv4Flows": cseFlowTotalIpv4Flows,
       "cseNetflowLS": cseNetflowLS,
       "cseNetflowLSExportStatus": cseNetflowLSExportStatus,
       "cseNetflowLSExportHost": cseNetflowLSExportHost,
       "cseNetflowLSExportTransportNumber": cseNetflowLSExportTransportNumber,
       "cseNetflowLSExportDataSource": cseNetflowLSExportDataSource,
       "cseNetflowLSExportDataSourceMask": cseNetflowLSExportDataSourceMask,
       "cseNetflowLSExportDataDest": cseNetflowLSExportDataDest,
       "cseNetflowLSExportDataDestMask": cseNetflowLSExportDataDestMask,
       "cseNetflowLSExportDataProtocol": cseNetflowLSExportDataProtocol,
       "cseNetflowLSExportDataFilterSelection": cseNetflowLSExportDataFilterSelection,
       "cseNetflowLSExportNDEVersionNumber": cseNetflowLSExportNDEVersionNumber,
       "cseNetflowLSFilterSupport": cseNetflowLSFilterSupport,
       "cseNetflowLSFilterTable": cseNetflowLSFilterTable,
       "cseNetflowLSFilterEntry": cseNetflowLSFilterEntry,
       "cseNetflowLSFilterIndex": cseNetflowLSFilterIndex,
       "cseNetflowLSFilterDataSource": cseNetflowLSFilterDataSource,
       "cseNetflowLSFilterDataSourceMask": cseNetflowLSFilterDataSourceMask,
       "cseNetflowLSFilterDataDest": cseNetflowLSFilterDataDest,
       "cseNetflowLSFilterDataDestMask": cseNetflowLSFilterDataDestMask,
       "cseNetflowLSFilterDataProtocol": cseNetflowLSFilterDataProtocol,
       "cseNetflowLSFilterSelection": cseNetflowLSFilterSelection,
       "cseNetflowLSFilterStatus": cseNetflowLSFilterStatus,
       "cseNetFlowIfIndexEnable": cseNetFlowIfIndexEnable,
       "cseNetflowASInfoExportCtrl": cseNetflowASInfoExportCtrl,
       "cseNetflowPerVlanIfGlobalEnable": cseNetflowPerVlanIfGlobalEnable,
       "cseNetflowPerVlanIfCtrlTable": cseNetflowPerVlanIfCtrlTable,
       "cseNetflowPerVlanIfCtrlEntry": cseNetflowPerVlanIfCtrlEntry,
       "cseNetflowPerVlanIfCtrlVlan": cseNetflowPerVlanIfCtrlVlan,
       "cseNetflowPerVlanIfEnable": cseNetflowPerVlanIfEnable,
       "cseL3Objects": cseL3Objects,
       "cseL3StatsTable": cseL3StatsTable,
       "cseL3StatsEntry": cseL3StatsEntry,
       "cseL3SwitchedTotalPkts": cseL3SwitchedTotalPkts,
       "cseL3SwitchedTotalOctets": cseL3SwitchedTotalOctets,
       "cseL3CandidateFlowHits": cseL3CandidateFlowHits,
       "cseL3EstablishedFlowHits": cseL3EstablishedFlowHits,
       "cseL3ActiveFlows": cseL3ActiveFlows,
       "cseL3FlowLearnFailures": cseL3FlowLearnFailures,
       "cseL3IntFlowInvalids": cseL3IntFlowInvalids,
       "cseL3ExtFlowInvalids": cseL3ExtFlowInvalids,
       "cseL3SwitchedPktsPerSec": cseL3SwitchedPktsPerSec,
       "cseL3VlanStatsTable": cseL3VlanStatsTable,
       "cseL3VlanStatsEntry": cseL3VlanStatsEntry,
       "cseL3VlanIndex": cseL3VlanIndex,
       "cseL3VlanInPkts": cseL3VlanInPkts,
       "cseL3VlanInOctets": cseL3VlanInOctets,
       "cseL3VlanOutPkts": cseL3VlanOutPkts,
       "cseL3VlanOutOctets": cseL3VlanOutOctets,
       "cseL3VlanInUnicastPkts": cseL3VlanInUnicastPkts,
       "cseL3VlanInUnicastOctets": cseL3VlanInUnicastOctets,
       "cseL3VlanOutUnicastPkts": cseL3VlanOutUnicastPkts,
       "cseL3VlanOutUnicastOctets": cseL3VlanOutUnicastOctets,
       "cseStatsFlowTable": cseStatsFlowTable,
       "cseStatsFlowEntry": cseStatsFlowEntry,
       "cseStatsFlowAged": cseStatsFlowAged,
       "cseStatsFlowPurged": cseStatsFlowPurged,
       "cseStatsFlowParityFail": cseStatsFlowParityFail,
       "cseCacheUtilTable": cseCacheUtilTable,
       "cseCacheUtilEntry": cseCacheUtilEntry,
       "cseCacheUtilization": cseCacheUtilization,
       "cseCacheEntriesCreated": cseCacheEntriesCreated,
       "cseCacheEntriesFailed": cseCacheEntriesFailed,
       "cseErrorStatsTable": cseErrorStatsTable,
       "cseErrorStatsEntry": cseErrorStatsEntry,
       "cseIpPlenErrors": cseIpPlenErrors,
       "cseIpTooShortErrors": cseIpTooShortErrors,
       "cseIpCheckSumErrors": cseIpCheckSumErrors,
       "cseIpxPlenErrors": cseIpxPlenErrors,
       "cseIpxTooShortErrors": cseIpxTooShortErrors,
       "cseErrorStatsLCTable": cseErrorStatsLCTable,
       "cseErrorStatsLCEntry": cseErrorStatsLCEntry,
       "cseLCIpPlenErrors": cseLCIpPlenErrors,
       "cseLCIpTooShortErrors": cseLCIpTooShortErrors,
       "cseLCIpCheckSumErrors": cseLCIpCheckSumErrors,
       "cseLCIpxPlenErrors": cseLCIpxPlenErrors,
       "cseLCIpxTooShortErrors": cseLCIpxTooShortErrors,
       "cseL3SwitchedAggrPktsPerSec": cseL3SwitchedAggrPktsPerSec,
       "cseProtocolFilter": cseProtocolFilter,
       "cseProtocolFilterEnable": cseProtocolFilterEnable,
       "cseProtocolFilterPortTable": cseProtocolFilterPortTable,
       "cseProtocolFilterPortEntry": cseProtocolFilterPortEntry,
       "cseProtocolFilterPortProtocol": cseProtocolFilterPortProtocol,
       "cseProtocolFilterPortAdminStatus": cseProtocolFilterPortAdminStatus,
       "cseProtocolFilterPortOperStatus": cseProtocolFilterPortOperStatus,
       "cseUcastCache": cseUcastCache,
       "cseUcastCacheTable": cseUcastCacheTable,
       "cseUcastCacheEntry": cseUcastCacheEntry,
       "cseUcastCacheIndex": cseUcastCacheIndex,
       "cseUcastCacheFlowType": cseUcastCacheFlowType,
       "cseUcastCacheTransport": cseUcastCacheTransport,
       "cseUcastCacheDest": cseUcastCacheDest,
       "cseUcastCacheDestMask": cseUcastCacheDestMask,
       "cseUcastCacheSource": cseUcastCacheSource,
       "cseUcastCacheSrcMask": cseUcastCacheSrcMask,
       "cseUcastCacheRtrIp": cseUcastCacheRtrIp,
       "cseUcastCacheOwner": cseUcastCacheOwner,
       "cseUcastCacheStatus": cseUcastCacheStatus,
       "cseUcastCacheResult": cseUcastCacheResult,
       "cseMcastCache": cseMcastCache,
       "cseMcastCacheTable": cseMcastCacheTable,
       "cseMcastCacheEntry": cseMcastCacheEntry,
       "cseMcastCacheIndex": cseMcastCacheIndex,
       "cseMcastCacheFlowType": cseMcastCacheFlowType,
       "cseMcastCacheGrp": cseMcastCacheGrp,
       "cseMcastCacheSrc": cseMcastCacheSrc,
       "cseMcastCacheRtrIp": cseMcastCacheRtrIp,
       "cseMcastCacheOwner": cseMcastCacheOwner,
       "cseMcastCacheResult": cseMcastCacheResult,
       "cseMcastCacheStatus": cseMcastCacheStatus,
       "cseCef": cseCef,
       "cseCefFibTable": cseCefFibTable,
       "cseCefFibEntry": cseCefFibEntry,
       "cseCefFibIndex": cseCefFibIndex,
       "cseCefFibAddrType": cseCefFibAddrType,
       "cseCefFibDestIp": cseCefFibDestIp,
       "cseCefFibDestIpMask": cseCefFibDestIpMask,
       "cseCefFibType": cseCefFibType,
       "cseCefAdjacencyTable": cseCefAdjacencyTable,
       "cseCefAdjacencyEntry": cseCefAdjacencyEntry,
       "cseCefAdjacencyIndex": cseCefAdjacencyIndex,
       "cseCefAdjacencyAddrType": cseCefAdjacencyAddrType,
       "cseCefAdjacencyNextHopIp": cseCefAdjacencyNextHopIp,
       "cseCefAdjacencyNextHopMac": cseCefAdjacencyNextHopMac,
       "cseCefAdjacencyNextHopIfIndex": cseCefAdjacencyNextHopIfIndex,
       "cseCefAdjacencyType": cseCefAdjacencyType,
       "cseCefAdjacencyPkts": cseCefAdjacencyPkts,
       "cseCefAdjacencyOctets": cseCefAdjacencyOctets,
       "cseCefAdjacencyEncap": cseCefAdjacencyEncap,
       "cseCefAdjacencyMTU": cseCefAdjacencyMTU,
       "cseTcamUsage": cseTcamUsage,
       "cseTcamUsageTable": cseTcamUsageTable,
       "cseTcamUsageEntry": cseTcamUsageEntry,
       "cseTcamResourceType": cseTcamResourceType,
       "cseTcamResourceDescr": cseTcamResourceDescr,
       "cseTcamResourceUsed": cseTcamResourceUsed,
       "cseTcamResourceTotal": cseTcamResourceTotal,
       "cseMet": cseMet,
       "cseMetUsageTable": cseMetUsageTable,
       "cseMetUsageEntry": cseMetUsageEntry,
       "cseMetIndex": cseMetIndex,
       "cseMetTotalEntries": cseMetTotalEntries,
       "cseMetUnallocatedSpcFreeEntries": cseMetUnallocatedSpcFreeEntries,
       "cseMetAllocatedSpcFreeEntries": cseMetAllocatedSpcFreeEntries,
       "cseMIBNotifications": cseMIBNotifications,
       "cseMIBConformance": cseMIBConformance,
       "cseMIBCompliances": cseMIBCompliances,
       "cseMIBCompliance": cseMIBCompliance,
       "cseMIBCompliance2": cseMIBCompliance2,
       "cseMIBCompliance3": cseMIBCompliance3,
       "cseMIBCompliance4": cseMIBCompliance4,
       "cseMIBCompliance5": cseMIBCompliance5,
       "cseMIBCompliance6": cseMIBCompliance6,
       "cseMIBCompliance7": cseMIBCompliance7,
       "cseMIBCompliance8": cseMIBCompliance8,
       "cseMIBGroups": cseMIBGroups,
       "cseStatisticsGroup": cseStatisticsGroup,
       "cseStatisticsGroup2": cseStatisticsGroup2,
       "cseVlanStatisticsGroup": cseVlanStatisticsGroup,
       "cseRouterGroup": cseRouterGroup,
       "cseFlowMgmtGroup": cseFlowMgmtGroup,
       "cseNetflowLSGroup": cseNetflowLSGroup,
       "cseProtocolFilterGroup": cseProtocolFilterGroup,
       "cseFlowMcastMgmtGroup": cseFlowMcastMgmtGroup,
       "cseUcastCachePurgeGroup": cseUcastCachePurgeGroup,
       "cseMcastCachePurgeGroup": cseMcastCachePurgeGroup,
       "cseFlowMgmtOperStatusGroup": cseFlowMgmtOperStatusGroup,
       "cse4kVlanGroup": cse4kVlanGroup,
       "cseNDEMandatoryGroup": cseNDEMandatoryGroup,
       "cseNDESingleFilterGroup": cseNDESingleFilterGroup,
       "cseNDEMultipleFiltersGroup": cseNDEMultipleFiltersGroup,
       "cseFlowMgmtGroupRev1": cseFlowMgmtGroupRev1,
       "cseL3ErrorsGroup": cseL3ErrorsGroup,
       "cseBridgedFlowGroup": cseBridgedFlowGroup,
       "cseVlanStatisticsExtGroup": cseVlanStatisticsExtGroup,
       "cseProtocolFilterExtGroup": cseProtocolFilterExtGroup,
       "cseFlowMgmtExtGroup": cseFlowMgmtExtGroup,
       "cseFlowMgmtExtGroup1": cseFlowMgmtExtGroup1,
       "cseNDEReportGroup": cseNDEReportGroup,
       "cseStatisticsFlowGroup": cseStatisticsFlowGroup,
       "cseFlowMgmtExtGroup2": cseFlowMgmtExtGroup2,
       "cseNDESingleFilterGroupRev1": cseNDESingleFilterGroupRev1,
       "cseCefFibAdjacencyGroup": cseCefFibAdjacencyGroup,
       "cseCefAdjacencyEncapGroup": cseCefAdjacencyEncapGroup,
       "cseCefAdjacencyMTUGroup": cseCefAdjacencyMTUGroup,
       "cseTcamUsageGroup": cseTcamUsageGroup,
       "cseL3ErrorsLCGroup": cseL3ErrorsLCGroup,
       "cseNetflowASInfoExportGroup": cseNetflowASInfoExportGroup,
       "cseNetflowPerVlanIfGroup": cseNetflowPerVlanIfGroup,
       "cseMetUsageGroup": cseMetUsageGroup,
       "cseFlowMcastMgmtGroup1": cseFlowMcastMgmtGroup1,
       "cseFlowMcastRtrMgmtGroup": cseFlowMcastRtrMgmtGroup,
       "cseFlowMcastMgmtGroup2": cseFlowMcastMgmtGroup2,
       "cseCacheStatisticsGroup": cseCacheStatisticsGroup,
       "cseL3SwitchedPktsPerSecGroup": cseL3SwitchedPktsPerSecGroup,
       "cseStatisticsFlowGroup1": cseStatisticsFlowGroup1}
)
