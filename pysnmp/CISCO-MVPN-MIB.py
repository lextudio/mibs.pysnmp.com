# SNMP MIB module (CISCO-MVPN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-MVPN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:05:59 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(MplsVpnRouteDistinguisher,
 mplsVpnVrfName) = mibBuilder.importSymbols(
    "MPLS-VPN-MIB",
    "MplsVpnRouteDistinguisher",
    "mplsVpnVrfName")

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
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoMvpnMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 113)
)
ciscoMvpnMIB.setRevisions(
        ("2004-02-23 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoMvpnNotifications_ObjectIdentity = ObjectIdentity
ciscoMvpnNotifications = _CiscoMvpnNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 0)
)
_CiscoMvpnObjects_ObjectIdentity = ObjectIdentity
ciscoMvpnObjects = _CiscoMvpnObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1)
)
_CiscoMvpnScalars_ObjectIdentity = ObjectIdentity
ciscoMvpnScalars = _CiscoMvpnScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 1)
)
_CiscoMvpnMvrfNumber_Type = Unsigned32
_CiscoMvpnMvrfNumber_Object = MibScalar
ciscoMvpnMvrfNumber = _CiscoMvpnMvrfNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 1, 1),
    _CiscoMvpnMvrfNumber_Type()
)
ciscoMvpnMvrfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoMvpnMvrfNumber.setStatus("current")


class _CiscoMvpnNotificationEnable_Type(TruthValue):
    """Custom type ciscoMvpnNotificationEnable based on TruthValue"""


_CiscoMvpnNotificationEnable_Object = MibScalar
ciscoMvpnNotificationEnable = _CiscoMvpnNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 1, 2),
    _CiscoMvpnNotificationEnable_Type()
)
ciscoMvpnNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoMvpnNotificationEnable.setStatus("current")
_CiscoMvpnGeneric_ObjectIdentity = ObjectIdentity
ciscoMvpnGeneric = _CiscoMvpnGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 2)
)
_CiscoMvpnGenericTable_Object = MibTable
ciscoMvpnGenericTable = _CiscoMvpnGenericTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ciscoMvpnGenericTable.setStatus("current")
_CiscoMvpnGenericEntry_Object = MibTableRow
ciscoMvpnGenericEntry = _CiscoMvpnGenericEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 2, 1, 1)
)
ciscoMvpnGenericEntry.setIndexNames(
    (0, "MPLS-VPN-MIB", "mplsVpnVrfName"),
)
if mibBuilder.loadTexts:
    ciscoMvpnGenericEntry.setStatus("current")


class _CiscoMvpnGenOperStatusChange_Type(Integer32):
    """Custom type ciscoMvpnGenOperStatusChange based on Integer32"""
    defaultValue = 1

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
        *(("createdMvrf", 1),
          ("deletedMvrf", 2),
          ("modifiedMvrfDataMdtConfig", 4),
          ("modifiedMvrfDefMdtConfig", 3))
    )


_CiscoMvpnGenOperStatusChange_Type.__name__ = "Integer32"
_CiscoMvpnGenOperStatusChange_Object = MibTableColumn
ciscoMvpnGenOperStatusChange = _CiscoMvpnGenOperStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 2, 1, 1, 1),
    _CiscoMvpnGenOperStatusChange_Type()
)
ciscoMvpnGenOperStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoMvpnGenOperStatusChange.setStatus("current")
_CiscoMvpnGenOperChangeTime_Type = TimeStamp
_CiscoMvpnGenOperChangeTime_Object = MibTableColumn
ciscoMvpnGenOperChangeTime = _CiscoMvpnGenOperChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 2, 1, 1, 2),
    _CiscoMvpnGenOperChangeTime_Type()
)
ciscoMvpnGenOperChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoMvpnGenOperChangeTime.setStatus("current")
_CiscoMvpnGenAssociatedInterfaces_Type = Unsigned32
_CiscoMvpnGenAssociatedInterfaces_Object = MibTableColumn
ciscoMvpnGenAssociatedInterfaces = _CiscoMvpnGenAssociatedInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 2, 1, 1, 3),
    _CiscoMvpnGenAssociatedInterfaces_Type()
)
ciscoMvpnGenAssociatedInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoMvpnGenAssociatedInterfaces.setStatus("current")
_CiscoMvpnGenRowStatus_Type = RowStatus
_CiscoMvpnGenRowStatus_Object = MibTableColumn
ciscoMvpnGenRowStatus = _CiscoMvpnGenRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 2, 1, 1, 4),
    _CiscoMvpnGenRowStatus_Type()
)
ciscoMvpnGenRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoMvpnGenRowStatus.setStatus("current")
_CiscoMvpnConfig_ObjectIdentity = ObjectIdentity
ciscoMvpnConfig = _CiscoMvpnConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 3)
)
_CiscoMvpnMdtDefaultTable_Object = MibTable
ciscoMvpnMdtDefaultTable = _CiscoMvpnMdtDefaultTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ciscoMvpnMdtDefaultTable.setStatus("current")
_CiscoMvpnMdtDefaultEntry_Object = MibTableRow
ciscoMvpnMdtDefaultEntry = _CiscoMvpnMdtDefaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 3, 1, 1)
)
ciscoMvpnMdtDefaultEntry.setIndexNames(
    (0, "MPLS-VPN-MIB", "mplsVpnVrfName"),
)
if mibBuilder.loadTexts:
    ciscoMvpnMdtDefaultEntry.setStatus("current")
_CiscoMvpnMdtDefaultAddrType_Type = InetAddressType
_CiscoMvpnMdtDefaultAddrType_Object = MibTableColumn
ciscoMvpnMdtDefaultAddrType = _CiscoMvpnMdtDefaultAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 3, 1, 1, 1),
    _CiscoMvpnMdtDefaultAddrType_Type()
)
ciscoMvpnMdtDefaultAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoMvpnMdtDefaultAddrType.setStatus("current")
_CiscoMvpnMdtDefaultAddress_Type = InetAddress
_CiscoMvpnMdtDefaultAddress_Object = MibTableColumn
ciscoMvpnMdtDefaultAddress = _CiscoMvpnMdtDefaultAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 3, 1, 1, 2),
    _CiscoMvpnMdtDefaultAddress_Type()
)
ciscoMvpnMdtDefaultAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoMvpnMdtDefaultAddress.setStatus("current")


class _CiscoMvpnMdtEncapsType_Type(Integer32):
    """Custom type ciscoMvpnMdtEncapsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("greIp", 1),
          ("ipIp", 2),
          ("mpls", 3))
    )


_CiscoMvpnMdtEncapsType_Type.__name__ = "Integer32"
_CiscoMvpnMdtEncapsType_Object = MibTableColumn
ciscoMvpnMdtEncapsType = _CiscoMvpnMdtEncapsType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 3, 1, 1, 3),
    _CiscoMvpnMdtEncapsType_Type()
)
ciscoMvpnMdtEncapsType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoMvpnMdtEncapsType.setStatus("current")
_CiscoMvpnMdtDefaultRowStatus_Type = RowStatus
_CiscoMvpnMdtDefaultRowStatus_Object = MibTableColumn
ciscoMvpnMdtDefaultRowStatus = _CiscoMvpnMdtDefaultRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 3, 1, 1, 4),
    _CiscoMvpnMdtDefaultRowStatus_Type()
)
ciscoMvpnMdtDefaultRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoMvpnMdtDefaultRowStatus.setStatus("current")
_CiscoMvpnMdtDataTable_Object = MibTable
ciscoMvpnMdtDataTable = _CiscoMvpnMdtDataTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ciscoMvpnMdtDataTable.setStatus("current")
_CiscoMvpnMdtDataEntry_Object = MibTableRow
ciscoMvpnMdtDataEntry = _CiscoMvpnMdtDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 3, 2, 1)
)
ciscoMvpnMdtDataEntry.setIndexNames(
    (0, "MPLS-VPN-MIB", "mplsVpnVrfName"),
)
if mibBuilder.loadTexts:
    ciscoMvpnMdtDataEntry.setStatus("current")
_CiscoMvpnMdtDataRangeAddrType_Type = InetAddressType
_CiscoMvpnMdtDataRangeAddrType_Object = MibTableColumn
ciscoMvpnMdtDataRangeAddrType = _CiscoMvpnMdtDataRangeAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 3, 2, 1, 1),
    _CiscoMvpnMdtDataRangeAddrType_Type()
)
ciscoMvpnMdtDataRangeAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoMvpnMdtDataRangeAddrType.setStatus("current")
_CiscoMvpnMdtDataRangeAddress_Type = InetAddress
_CiscoMvpnMdtDataRangeAddress_Object = MibTableColumn
ciscoMvpnMdtDataRangeAddress = _CiscoMvpnMdtDataRangeAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 3, 2, 1, 2),
    _CiscoMvpnMdtDataRangeAddress_Type()
)
ciscoMvpnMdtDataRangeAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoMvpnMdtDataRangeAddress.setStatus("current")
_CiscoMvpnMdtDataWildcardType_Type = InetAddressType
_CiscoMvpnMdtDataWildcardType_Object = MibTableColumn
ciscoMvpnMdtDataWildcardType = _CiscoMvpnMdtDataWildcardType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 3, 2, 1, 3),
    _CiscoMvpnMdtDataWildcardType_Type()
)
ciscoMvpnMdtDataWildcardType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoMvpnMdtDataWildcardType.setStatus("current")
_CiscoMvpnMdtDataWildcardBits_Type = InetAddress
_CiscoMvpnMdtDataWildcardBits_Object = MibTableColumn
ciscoMvpnMdtDataWildcardBits = _CiscoMvpnMdtDataWildcardBits_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 3, 2, 1, 4),
    _CiscoMvpnMdtDataWildcardBits_Type()
)
ciscoMvpnMdtDataWildcardBits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoMvpnMdtDataWildcardBits.setStatus("current")


class _CiscoMvpnMdtDataThreshold_Type(Unsigned32):
    """Custom type ciscoMvpnMdtDataThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CiscoMvpnMdtDataThreshold_Type.__name__ = "Unsigned32"
_CiscoMvpnMdtDataThreshold_Object = MibTableColumn
ciscoMvpnMdtDataThreshold = _CiscoMvpnMdtDataThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 3, 2, 1, 5),
    _CiscoMvpnMdtDataThreshold_Type()
)
ciscoMvpnMdtDataThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoMvpnMdtDataThreshold.setStatus("current")
if mibBuilder.loadTexts:
    ciscoMvpnMdtDataThreshold.setUnits("kilobits per second")
_CiscoMvpnMdtDataRowStatus_Type = RowStatus
_CiscoMvpnMdtDataRowStatus_Object = MibTableColumn
ciscoMvpnMdtDataRowStatus = _CiscoMvpnMdtDataRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 3, 2, 1, 6),
    _CiscoMvpnMdtDataRowStatus_Type()
)
ciscoMvpnMdtDataRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoMvpnMdtDataRowStatus.setStatus("current")
_CiscoMvpnProtocol_ObjectIdentity = ObjectIdentity
ciscoMvpnProtocol = _CiscoMvpnProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 4)
)
_CiscoMvpnMrouteMdtTable_Object = MibTable
ciscoMvpnMrouteMdtTable = _CiscoMvpnMrouteMdtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ciscoMvpnMrouteMdtTable.setStatus("current")
_CiscoMvpnMrouteMdtEntry_Object = MibTableRow
ciscoMvpnMrouteMdtEntry = _CiscoMvpnMrouteMdtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 4, 1, 1)
)
ciscoMvpnMrouteMdtEntry.setIndexNames(
    (0, "MPLS-VPN-MIB", "mplsVpnVrfName"),
    (0, "CISCO-MVPN-MIB", "ciscoMvpnMrouteMvrfGrpAddrType"),
    (0, "CISCO-MVPN-MIB", "ciscoMvpnMrouteMvrfGroup"),
    (0, "CISCO-MVPN-MIB", "ciscoMvpnMrouteMvrfSrcAddrType"),
    (0, "CISCO-MVPN-MIB", "ciscoMvpnMrouteMvrfSource"),
    (0, "CISCO-MVPN-MIB", "ciscoMvpnMrouteUpDownStreamInfo"),
)
if mibBuilder.loadTexts:
    ciscoMvpnMrouteMdtEntry.setStatus("current")
_CiscoMvpnMrouteMvrfGrpAddrType_Type = InetAddressType
_CiscoMvpnMrouteMvrfGrpAddrType_Object = MibTableColumn
ciscoMvpnMrouteMvrfGrpAddrType = _CiscoMvpnMrouteMvrfGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 4, 1, 1, 1),
    _CiscoMvpnMrouteMvrfGrpAddrType_Type()
)
ciscoMvpnMrouteMvrfGrpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoMvpnMrouteMvrfGrpAddrType.setStatus("current")


class _CiscoMvpnMrouteMvrfGroup_Type(InetAddress):
    """Custom type ciscoMvpnMrouteMvrfGroup based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_CiscoMvpnMrouteMvrfGroup_Type.__name__ = "InetAddress"
_CiscoMvpnMrouteMvrfGroup_Object = MibTableColumn
ciscoMvpnMrouteMvrfGroup = _CiscoMvpnMrouteMvrfGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 4, 1, 1, 2),
    _CiscoMvpnMrouteMvrfGroup_Type()
)
ciscoMvpnMrouteMvrfGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoMvpnMrouteMvrfGroup.setStatus("current")
_CiscoMvpnMrouteMvrfSrcAddrType_Type = InetAddressType
_CiscoMvpnMrouteMvrfSrcAddrType_Object = MibTableColumn
ciscoMvpnMrouteMvrfSrcAddrType = _CiscoMvpnMrouteMvrfSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 4, 1, 1, 3),
    _CiscoMvpnMrouteMvrfSrcAddrType_Type()
)
ciscoMvpnMrouteMvrfSrcAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoMvpnMrouteMvrfSrcAddrType.setStatus("current")


class _CiscoMvpnMrouteMvrfSource_Type(InetAddress):
    """Custom type ciscoMvpnMrouteMvrfSource based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_CiscoMvpnMrouteMvrfSource_Type.__name__ = "InetAddress"
_CiscoMvpnMrouteMvrfSource_Object = MibTableColumn
ciscoMvpnMrouteMvrfSource = _CiscoMvpnMrouteMvrfSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 4, 1, 1, 4),
    _CiscoMvpnMrouteMvrfSource_Type()
)
ciscoMvpnMrouteMvrfSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoMvpnMrouteMvrfSource.setStatus("current")


class _CiscoMvpnMrouteUpDownStreamInfo_Type(Integer32):
    """Custom type ciscoMvpnMrouteUpDownStreamInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downstream", 2),
          ("upstream", 1))
    )


_CiscoMvpnMrouteUpDownStreamInfo_Type.__name__ = "Integer32"
_CiscoMvpnMrouteUpDownStreamInfo_Object = MibTableColumn
ciscoMvpnMrouteUpDownStreamInfo = _CiscoMvpnMrouteUpDownStreamInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 4, 1, 1, 5),
    _CiscoMvpnMrouteUpDownStreamInfo_Type()
)
ciscoMvpnMrouteUpDownStreamInfo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoMvpnMrouteUpDownStreamInfo.setStatus("current")
_CiscoMvpnMrouteMdtGrpAddrType_Type = InetAddressType
_CiscoMvpnMrouteMdtGrpAddrType_Object = MibTableColumn
ciscoMvpnMrouteMdtGrpAddrType = _CiscoMvpnMrouteMdtGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 4, 1, 1, 6),
    _CiscoMvpnMrouteMdtGrpAddrType_Type()
)
ciscoMvpnMrouteMdtGrpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoMvpnMrouteMdtGrpAddrType.setStatus("current")
_CiscoMvpnMrouteMdtGroup_Type = InetAddress
_CiscoMvpnMrouteMdtGroup_Object = MibTableColumn
ciscoMvpnMrouteMdtGroup = _CiscoMvpnMrouteMdtGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 4, 1, 1, 7),
    _CiscoMvpnMrouteMdtGroup_Type()
)
ciscoMvpnMrouteMdtGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoMvpnMrouteMdtGroup.setStatus("current")


class _CiscoMvpnMrouteMdtType_Type(Integer32):
    """Custom type ciscoMvpnMrouteMdtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mdtData", 2),
          ("mdtDefault", 1))
    )


_CiscoMvpnMrouteMdtType_Type.__name__ = "Integer32"
_CiscoMvpnMrouteMdtType_Object = MibTableColumn
ciscoMvpnMrouteMdtType = _CiscoMvpnMrouteMdtType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 4, 1, 1, 8),
    _CiscoMvpnMrouteMdtType_Type()
)
ciscoMvpnMrouteMdtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoMvpnMrouteMdtType.setStatus("current")
_CiscoMvpnBgpMdtUpdateTable_Object = MibTable
ciscoMvpnBgpMdtUpdateTable = _CiscoMvpnBgpMdtUpdateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 4, 2)
)
if mibBuilder.loadTexts:
    ciscoMvpnBgpMdtUpdateTable.setStatus("current")
_CiscoMvpnBgpMdtUpdateEntry_Object = MibTableRow
ciscoMvpnBgpMdtUpdateEntry = _CiscoMvpnBgpMdtUpdateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 4, 2, 1)
)
ciscoMvpnBgpMdtUpdateEntry.setIndexNames(
    (0, "CISCO-MVPN-MIB", "ciscoMvpnBgpMdtUpdGrpAddrType"),
    (0, "CISCO-MVPN-MIB", "ciscoMvpnBgpMdtUpdateGroup"),
    (0, "CISCO-MVPN-MIB", "ciscoMvpnBgpMdtUpdSrcAddrType"),
    (0, "CISCO-MVPN-MIB", "ciscoMvpnBgpMdtUpdateSource"),
)
if mibBuilder.loadTexts:
    ciscoMvpnBgpMdtUpdateEntry.setStatus("current")
_CiscoMvpnBgpMdtUpdGrpAddrType_Type = InetAddressType
_CiscoMvpnBgpMdtUpdGrpAddrType_Object = MibTableColumn
ciscoMvpnBgpMdtUpdGrpAddrType = _CiscoMvpnBgpMdtUpdGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 4, 2, 1, 1),
    _CiscoMvpnBgpMdtUpdGrpAddrType_Type()
)
ciscoMvpnBgpMdtUpdGrpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoMvpnBgpMdtUpdGrpAddrType.setStatus("current")


class _CiscoMvpnBgpMdtUpdateGroup_Type(InetAddress):
    """Custom type ciscoMvpnBgpMdtUpdateGroup based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_CiscoMvpnBgpMdtUpdateGroup_Type.__name__ = "InetAddress"
_CiscoMvpnBgpMdtUpdateGroup_Object = MibTableColumn
ciscoMvpnBgpMdtUpdateGroup = _CiscoMvpnBgpMdtUpdateGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 4, 2, 1, 2),
    _CiscoMvpnBgpMdtUpdateGroup_Type()
)
ciscoMvpnBgpMdtUpdateGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoMvpnBgpMdtUpdateGroup.setStatus("current")
_CiscoMvpnBgpMdtUpdateRd_Type = MplsVpnRouteDistinguisher
_CiscoMvpnBgpMdtUpdateRd_Object = MibTableColumn
ciscoMvpnBgpMdtUpdateRd = _CiscoMvpnBgpMdtUpdateRd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 4, 2, 1, 3),
    _CiscoMvpnBgpMdtUpdateRd_Type()
)
ciscoMvpnBgpMdtUpdateRd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoMvpnBgpMdtUpdateRd.setStatus("current")
_CiscoMvpnBgpMdtUpdSrcAddrType_Type = InetAddressType
_CiscoMvpnBgpMdtUpdSrcAddrType_Object = MibTableColumn
ciscoMvpnBgpMdtUpdSrcAddrType = _CiscoMvpnBgpMdtUpdSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 4, 2, 1, 4),
    _CiscoMvpnBgpMdtUpdSrcAddrType_Type()
)
ciscoMvpnBgpMdtUpdSrcAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoMvpnBgpMdtUpdSrcAddrType.setStatus("current")


class _CiscoMvpnBgpMdtUpdateSource_Type(InetAddress):
    """Custom type ciscoMvpnBgpMdtUpdateSource based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_CiscoMvpnBgpMdtUpdateSource_Type.__name__ = "InetAddress"
_CiscoMvpnBgpMdtUpdateSource_Object = MibTableColumn
ciscoMvpnBgpMdtUpdateSource = _CiscoMvpnBgpMdtUpdateSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 4, 2, 1, 5),
    _CiscoMvpnBgpMdtUpdateSource_Type()
)
ciscoMvpnBgpMdtUpdateSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoMvpnBgpMdtUpdateSource.setStatus("current")
_CiscoMvpnBgpMdtUpdOrigAddrType_Type = InetAddressType
_CiscoMvpnBgpMdtUpdOrigAddrType_Object = MibTableColumn
ciscoMvpnBgpMdtUpdOrigAddrType = _CiscoMvpnBgpMdtUpdOrigAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 4, 2, 1, 6),
    _CiscoMvpnBgpMdtUpdOrigAddrType_Type()
)
ciscoMvpnBgpMdtUpdOrigAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoMvpnBgpMdtUpdOrigAddrType.setStatus("current")
_CiscoMvpnBgpMdtUpdateOriginator_Type = InetAddress
_CiscoMvpnBgpMdtUpdateOriginator_Object = MibTableColumn
ciscoMvpnBgpMdtUpdateOriginator = _CiscoMvpnBgpMdtUpdateOriginator_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 4, 2, 1, 7),
    _CiscoMvpnBgpMdtUpdateOriginator_Type()
)
ciscoMvpnBgpMdtUpdateOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoMvpnBgpMdtUpdateOriginator.setStatus("current")
_CiscoMvpnBgpMdtUpdNhAddrType_Type = InetAddressType
_CiscoMvpnBgpMdtUpdNhAddrType_Object = MibTableColumn
ciscoMvpnBgpMdtUpdNhAddrType = _CiscoMvpnBgpMdtUpdNhAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 4, 2, 1, 8),
    _CiscoMvpnBgpMdtUpdNhAddrType_Type()
)
ciscoMvpnBgpMdtUpdNhAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoMvpnBgpMdtUpdNhAddrType.setStatus("current")
_CiscoMvpnBgpMdtUpdateNexthop_Type = InetAddress
_CiscoMvpnBgpMdtUpdateNexthop_Object = MibTableColumn
ciscoMvpnBgpMdtUpdateNexthop = _CiscoMvpnBgpMdtUpdateNexthop_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 4, 2, 1, 9),
    _CiscoMvpnBgpMdtUpdateNexthop_Type()
)
ciscoMvpnBgpMdtUpdateNexthop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoMvpnBgpMdtUpdateNexthop.setStatus("current")
_CiscoMvpnMdtJnRcvTable_Object = MibTable
ciscoMvpnMdtJnRcvTable = _CiscoMvpnMdtJnRcvTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 4, 3)
)
if mibBuilder.loadTexts:
    ciscoMvpnMdtJnRcvTable.setStatus("current")
_CiscoMvpnMdtJnRcvEntry_Object = MibTableRow
ciscoMvpnMdtJnRcvEntry = _CiscoMvpnMdtJnRcvEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 4, 3, 1)
)
ciscoMvpnMdtJnRcvEntry.setIndexNames(
    (0, "MPLS-VPN-MIB", "mplsVpnVrfName"),
    (0, "CISCO-MVPN-MIB", "ciscoMvpnMdtJnRcvGrpAddrType"),
    (0, "CISCO-MVPN-MIB", "ciscoMvpnMdtJnRcvGroup"),
    (0, "CISCO-MVPN-MIB", "ciscoMvpnMdtJnRcvSrcAddrType"),
    (0, "CISCO-MVPN-MIB", "ciscoMvpnMdtJnRcvSource"),
)
if mibBuilder.loadTexts:
    ciscoMvpnMdtJnRcvEntry.setStatus("current")
_CiscoMvpnMdtJnRcvGrpAddrType_Type = InetAddressType
_CiscoMvpnMdtJnRcvGrpAddrType_Object = MibTableColumn
ciscoMvpnMdtJnRcvGrpAddrType = _CiscoMvpnMdtJnRcvGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 4, 3, 1, 1),
    _CiscoMvpnMdtJnRcvGrpAddrType_Type()
)
ciscoMvpnMdtJnRcvGrpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoMvpnMdtJnRcvGrpAddrType.setStatus("current")


class _CiscoMvpnMdtJnRcvGroup_Type(InetAddress):
    """Custom type ciscoMvpnMdtJnRcvGroup based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_CiscoMvpnMdtJnRcvGroup_Type.__name__ = "InetAddress"
_CiscoMvpnMdtJnRcvGroup_Object = MibTableColumn
ciscoMvpnMdtJnRcvGroup = _CiscoMvpnMdtJnRcvGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 4, 3, 1, 2),
    _CiscoMvpnMdtJnRcvGroup_Type()
)
ciscoMvpnMdtJnRcvGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoMvpnMdtJnRcvGroup.setStatus("current")
_CiscoMvpnMdtJnRcvSrcAddrType_Type = InetAddressType
_CiscoMvpnMdtJnRcvSrcAddrType_Object = MibTableColumn
ciscoMvpnMdtJnRcvSrcAddrType = _CiscoMvpnMdtJnRcvSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 4, 3, 1, 3),
    _CiscoMvpnMdtJnRcvSrcAddrType_Type()
)
ciscoMvpnMdtJnRcvSrcAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoMvpnMdtJnRcvSrcAddrType.setStatus("current")


class _CiscoMvpnMdtJnRcvSource_Type(InetAddress):
    """Custom type ciscoMvpnMdtJnRcvSource based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_CiscoMvpnMdtJnRcvSource_Type.__name__ = "InetAddress"
_CiscoMvpnMdtJnRcvSource_Object = MibTableColumn
ciscoMvpnMdtJnRcvSource = _CiscoMvpnMdtJnRcvSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 4, 3, 1, 4),
    _CiscoMvpnMdtJnRcvSource_Type()
)
ciscoMvpnMdtJnRcvSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoMvpnMdtJnRcvSource.setStatus("current")
_CiscoMvpnMdtJnRcvUpTime_Type = TimeInterval
_CiscoMvpnMdtJnRcvUpTime_Object = MibTableColumn
ciscoMvpnMdtJnRcvUpTime = _CiscoMvpnMdtJnRcvUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 4, 3, 1, 5),
    _CiscoMvpnMdtJnRcvUpTime_Type()
)
ciscoMvpnMdtJnRcvUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoMvpnMdtJnRcvUpTime.setStatus("current")
_CiscoMvpnMdtJnRcvExpTime_Type = TimeInterval
_CiscoMvpnMdtJnRcvExpTime_Object = MibTableColumn
ciscoMvpnMdtJnRcvExpTime = _CiscoMvpnMdtJnRcvExpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 4, 3, 1, 6),
    _CiscoMvpnMdtJnRcvExpTime_Type()
)
ciscoMvpnMdtJnRcvExpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoMvpnMdtJnRcvExpTime.setStatus("current")
_CiscoMvpnMdtJnSendTable_Object = MibTable
ciscoMvpnMdtJnSendTable = _CiscoMvpnMdtJnSendTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 4, 4)
)
if mibBuilder.loadTexts:
    ciscoMvpnMdtJnSendTable.setStatus("current")
_CiscoMvpnMdtJnSendEntry_Object = MibTableRow
ciscoMvpnMdtJnSendEntry = _CiscoMvpnMdtJnSendEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 4, 4, 1)
)
ciscoMvpnMdtJnSendEntry.setIndexNames(
    (0, "MPLS-VPN-MIB", "mplsVpnVrfName"),
    (0, "CISCO-MVPN-MIB", "ciscoMvpnMdtJnSendGrpAddrType"),
    (0, "CISCO-MVPN-MIB", "ciscoMvpnMdtJnSendGroup"),
    (0, "CISCO-MVPN-MIB", "ciscoMvpnMdtJnSendSrcAddrType"),
    (0, "CISCO-MVPN-MIB", "ciscoMvpnMdtJnSendSource"),
)
if mibBuilder.loadTexts:
    ciscoMvpnMdtJnSendEntry.setStatus("current")
_CiscoMvpnMdtJnSendGrpAddrType_Type = InetAddressType
_CiscoMvpnMdtJnSendGrpAddrType_Object = MibTableColumn
ciscoMvpnMdtJnSendGrpAddrType = _CiscoMvpnMdtJnSendGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 4, 4, 1, 1),
    _CiscoMvpnMdtJnSendGrpAddrType_Type()
)
ciscoMvpnMdtJnSendGrpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoMvpnMdtJnSendGrpAddrType.setStatus("current")


class _CiscoMvpnMdtJnSendGroup_Type(InetAddress):
    """Custom type ciscoMvpnMdtJnSendGroup based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_CiscoMvpnMdtJnSendGroup_Type.__name__ = "InetAddress"
_CiscoMvpnMdtJnSendGroup_Object = MibTableColumn
ciscoMvpnMdtJnSendGroup = _CiscoMvpnMdtJnSendGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 4, 4, 1, 2),
    _CiscoMvpnMdtJnSendGroup_Type()
)
ciscoMvpnMdtJnSendGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoMvpnMdtJnSendGroup.setStatus("current")
_CiscoMvpnMdtJnSendSrcAddrType_Type = InetAddressType
_CiscoMvpnMdtJnSendSrcAddrType_Object = MibTableColumn
ciscoMvpnMdtJnSendSrcAddrType = _CiscoMvpnMdtJnSendSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 4, 4, 1, 3),
    _CiscoMvpnMdtJnSendSrcAddrType_Type()
)
ciscoMvpnMdtJnSendSrcAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoMvpnMdtJnSendSrcAddrType.setStatus("current")


class _CiscoMvpnMdtJnSendSource_Type(InetAddress):
    """Custom type ciscoMvpnMdtJnSendSource based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_CiscoMvpnMdtJnSendSource_Type.__name__ = "InetAddress"
_CiscoMvpnMdtJnSendSource_Object = MibTableColumn
ciscoMvpnMdtJnSendSource = _CiscoMvpnMdtJnSendSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 4, 4, 1, 4),
    _CiscoMvpnMdtJnSendSource_Type()
)
ciscoMvpnMdtJnSendSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoMvpnMdtJnSendSource.setStatus("current")
_CiscoMvpnMdtJnSendMdtGrpAddrType_Type = InetAddressType
_CiscoMvpnMdtJnSendMdtGrpAddrType_Object = MibTableColumn
ciscoMvpnMdtJnSendMdtGrpAddrType = _CiscoMvpnMdtJnSendMdtGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 4, 4, 1, 5),
    _CiscoMvpnMdtJnSendMdtGrpAddrType_Type()
)
ciscoMvpnMdtJnSendMdtGrpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoMvpnMdtJnSendMdtGrpAddrType.setStatus("current")
_CiscoMvpnMdtJnSendMdtGroup_Type = InetAddress
_CiscoMvpnMdtJnSendMdtGroup_Object = MibTableColumn
ciscoMvpnMdtJnSendMdtGroup = _CiscoMvpnMdtJnSendMdtGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 4, 4, 1, 6),
    _CiscoMvpnMdtJnSendMdtGroup_Type()
)
ciscoMvpnMdtJnSendMdtGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoMvpnMdtJnSendMdtGroup.setStatus("current")


class _CiscoMvpnMdtJnSendMdtRefCt_Type(Unsigned32):
    """Custom type ciscoMvpnMdtJnSendMdtRefCt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CiscoMvpnMdtJnSendMdtRefCt_Type.__name__ = "Unsigned32"
_CiscoMvpnMdtJnSendMdtRefCt_Object = MibTableColumn
ciscoMvpnMdtJnSendMdtRefCt = _CiscoMvpnMdtJnSendMdtRefCt_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 4, 4, 1, 7),
    _CiscoMvpnMdtJnSendMdtRefCt_Type()
)
ciscoMvpnMdtJnSendMdtRefCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoMvpnMdtJnSendMdtRefCt.setStatus("current")
_CiscoMvpnTunnelTable_Object = MibTable
ciscoMvpnTunnelTable = _CiscoMvpnTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 4, 5)
)
if mibBuilder.loadTexts:
    ciscoMvpnTunnelTable.setStatus("current")
_CiscoMvpnTunnelEntry_Object = MibTableRow
ciscoMvpnTunnelEntry = _CiscoMvpnTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 4, 5, 1)
)
ciscoMvpnTunnelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ciscoMvpnTunnelEntry.setStatus("current")
_CiscoMvpnTunnelName_Type = DisplayString
_CiscoMvpnTunnelName_Object = MibTableColumn
ciscoMvpnTunnelName = _CiscoMvpnTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 4, 5, 1, 1),
    _CiscoMvpnTunnelName_Type()
)
ciscoMvpnTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoMvpnTunnelName.setStatus("current")
_CiscoMvpnTunnelMvrf_Type = SnmpAdminString
_CiscoMvpnTunnelMvrf_Object = MibTableColumn
ciscoMvpnTunnelMvrf = _CiscoMvpnTunnelMvrf_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 1, 4, 5, 1, 2),
    _CiscoMvpnTunnelMvrf_Type()
)
ciscoMvpnTunnelMvrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoMvpnTunnelMvrf.setStatus("current")
_CiscoMvpnConformance_ObjectIdentity = ObjectIdentity
ciscoMvpnConformance = _CiscoMvpnConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 2)
)
_CiscoMvpnGroups_ObjectIdentity = ObjectIdentity
ciscoMvpnGroups = _CiscoMvpnGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 2, 1)
)
_CiscoMvpnCompliances_ObjectIdentity = ObjectIdentity
ciscoMvpnCompliances = _CiscoMvpnCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 2, 2)
)

# Managed Objects groups

ciscoMvpnScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 2, 1, 1)
)
ciscoMvpnScalarGroup.setObjects(
      *(("CISCO-MVPN-MIB", "ciscoMvpnMvrfNumber"),
        ("CISCO-MVPN-MIB", "ciscoMvpnNotificationEnable"))
)
if mibBuilder.loadTexts:
    ciscoMvpnScalarGroup.setStatus("current")

ciscoMvpnMIBGenericGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 2, 1, 2)
)
ciscoMvpnMIBGenericGroup.setObjects(
      *(("CISCO-MVPN-MIB", "ciscoMvpnGenOperStatusChange"),
        ("CISCO-MVPN-MIB", "ciscoMvpnGenOperChangeTime"),
        ("CISCO-MVPN-MIB", "ciscoMvpnGenAssociatedInterfaces"),
        ("CISCO-MVPN-MIB", "ciscoMvpnGenRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoMvpnMIBGenericGroup.setStatus("current")

ciscoMvpnMIBMdtDefaultGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 2, 1, 3)
)
ciscoMvpnMIBMdtDefaultGroup.setObjects(
      *(("CISCO-MVPN-MIB", "ciscoMvpnMdtDefaultAddrType"),
        ("CISCO-MVPN-MIB", "ciscoMvpnMdtDefaultAddress"),
        ("CISCO-MVPN-MIB", "ciscoMvpnMdtEncapsType"),
        ("CISCO-MVPN-MIB", "ciscoMvpnMdtDefaultRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoMvpnMIBMdtDefaultGroup.setStatus("current")

ciscoMvpnMIBMdtDataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 2, 1, 4)
)
ciscoMvpnMIBMdtDataGroup.setObjects(
      *(("CISCO-MVPN-MIB", "ciscoMvpnMdtDataRangeAddrType"),
        ("CISCO-MVPN-MIB", "ciscoMvpnMdtDataRangeAddress"),
        ("CISCO-MVPN-MIB", "ciscoMvpnMdtDataWildcardType"),
        ("CISCO-MVPN-MIB", "ciscoMvpnMdtDataWildcardBits"),
        ("CISCO-MVPN-MIB", "ciscoMvpnMdtDataThreshold"),
        ("CISCO-MVPN-MIB", "ciscoMvpnMdtDataRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoMvpnMIBMdtDataGroup.setStatus("current")

ciscoMvpnMIBMrouteMdtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 2, 1, 5)
)
ciscoMvpnMIBMrouteMdtGroup.setObjects(
      *(("CISCO-MVPN-MIB", "ciscoMvpnMrouteMdtGrpAddrType"),
        ("CISCO-MVPN-MIB", "ciscoMvpnMrouteMdtGroup"),
        ("CISCO-MVPN-MIB", "ciscoMvpnMrouteMdtType"))
)
if mibBuilder.loadTexts:
    ciscoMvpnMIBMrouteMdtGroup.setStatus("current")

ciscoMvpnMIBBgpMdtUpdateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 2, 1, 6)
)
ciscoMvpnMIBBgpMdtUpdateGroup.setObjects(
      *(("CISCO-MVPN-MIB", "ciscoMvpnBgpMdtUpdateRd"),
        ("CISCO-MVPN-MIB", "ciscoMvpnBgpMdtUpdOrigAddrType"),
        ("CISCO-MVPN-MIB", "ciscoMvpnBgpMdtUpdateOriginator"),
        ("CISCO-MVPN-MIB", "ciscoMvpnBgpMdtUpdNhAddrType"),
        ("CISCO-MVPN-MIB", "ciscoMvpnBgpMdtUpdateNexthop"))
)
if mibBuilder.loadTexts:
    ciscoMvpnMIBBgpMdtUpdateGroup.setStatus("current")

ciscoMvpnMIBMdtJnRcvGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 2, 1, 7)
)
ciscoMvpnMIBMdtJnRcvGroup.setObjects(
      *(("CISCO-MVPN-MIB", "ciscoMvpnMdtJnRcvUpTime"),
        ("CISCO-MVPN-MIB", "ciscoMvpnMdtJnRcvExpTime"))
)
if mibBuilder.loadTexts:
    ciscoMvpnMIBMdtJnRcvGroup.setStatus("current")

ciscoMvpnMIBMdtJnSendGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 2, 1, 8)
)
ciscoMvpnMIBMdtJnSendGroup.setObjects(
      *(("CISCO-MVPN-MIB", "ciscoMvpnMdtJnSendMdtGrpAddrType"),
        ("CISCO-MVPN-MIB", "ciscoMvpnMdtJnSendMdtGroup"),
        ("CISCO-MVPN-MIB", "ciscoMvpnMdtJnSendMdtRefCt"))
)
if mibBuilder.loadTexts:
    ciscoMvpnMIBMdtJnSendGroup.setStatus("current")

ciscoMvpnTunnelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 2, 1, 9)
)
ciscoMvpnTunnelGroup.setObjects(
      *(("CISCO-MVPN-MIB", "ciscoMvpnTunnelName"),
        ("CISCO-MVPN-MIB", "ciscoMvpnTunnelMvrf"))
)
if mibBuilder.loadTexts:
    ciscoMvpnTunnelGroup.setStatus("current")


# Notification objects

ciscoMvpnMvrfChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 0, 2)
)
ciscoMvpnMvrfChange.setObjects(
    ("CISCO-MVPN-MIB", "ciscoMvpnGenOperStatusChange")
)
if mibBuilder.loadTexts:
    ciscoMvpnMvrfChange.setStatus(
        "current"
    )


# Notifications groups

ciscoMvpnNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 2, 1, 10)
)
ciscoMvpnNotificationGroup.setObjects(
    ("CISCO-MVPN-MIB", "ciscoMvpnMvrfChange")
)
if mibBuilder.loadTexts:
    ciscoMvpnNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoMvpnModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ciscoMvpnModuleFullCompliance.setStatus(
        "current"
    )

ciscoMvpnModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 113, 2, 2, 2)
)
if mibBuilder.loadTexts:
    ciscoMvpnModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-MVPN-MIB",
    **{"ciscoMvpnMIB": ciscoMvpnMIB,
       "ciscoMvpnNotifications": ciscoMvpnNotifications,
       "ciscoMvpnMvrfChange": ciscoMvpnMvrfChange,
       "ciscoMvpnObjects": ciscoMvpnObjects,
       "ciscoMvpnScalars": ciscoMvpnScalars,
       "ciscoMvpnMvrfNumber": ciscoMvpnMvrfNumber,
       "ciscoMvpnNotificationEnable": ciscoMvpnNotificationEnable,
       "ciscoMvpnGeneric": ciscoMvpnGeneric,
       "ciscoMvpnGenericTable": ciscoMvpnGenericTable,
       "ciscoMvpnGenericEntry": ciscoMvpnGenericEntry,
       "ciscoMvpnGenOperStatusChange": ciscoMvpnGenOperStatusChange,
       "ciscoMvpnGenOperChangeTime": ciscoMvpnGenOperChangeTime,
       "ciscoMvpnGenAssociatedInterfaces": ciscoMvpnGenAssociatedInterfaces,
       "ciscoMvpnGenRowStatus": ciscoMvpnGenRowStatus,
       "ciscoMvpnConfig": ciscoMvpnConfig,
       "ciscoMvpnMdtDefaultTable": ciscoMvpnMdtDefaultTable,
       "ciscoMvpnMdtDefaultEntry": ciscoMvpnMdtDefaultEntry,
       "ciscoMvpnMdtDefaultAddrType": ciscoMvpnMdtDefaultAddrType,
       "ciscoMvpnMdtDefaultAddress": ciscoMvpnMdtDefaultAddress,
       "ciscoMvpnMdtEncapsType": ciscoMvpnMdtEncapsType,
       "ciscoMvpnMdtDefaultRowStatus": ciscoMvpnMdtDefaultRowStatus,
       "ciscoMvpnMdtDataTable": ciscoMvpnMdtDataTable,
       "ciscoMvpnMdtDataEntry": ciscoMvpnMdtDataEntry,
       "ciscoMvpnMdtDataRangeAddrType": ciscoMvpnMdtDataRangeAddrType,
       "ciscoMvpnMdtDataRangeAddress": ciscoMvpnMdtDataRangeAddress,
       "ciscoMvpnMdtDataWildcardType": ciscoMvpnMdtDataWildcardType,
       "ciscoMvpnMdtDataWildcardBits": ciscoMvpnMdtDataWildcardBits,
       "ciscoMvpnMdtDataThreshold": ciscoMvpnMdtDataThreshold,
       "ciscoMvpnMdtDataRowStatus": ciscoMvpnMdtDataRowStatus,
       "ciscoMvpnProtocol": ciscoMvpnProtocol,
       "ciscoMvpnMrouteMdtTable": ciscoMvpnMrouteMdtTable,
       "ciscoMvpnMrouteMdtEntry": ciscoMvpnMrouteMdtEntry,
       "ciscoMvpnMrouteMvrfGrpAddrType": ciscoMvpnMrouteMvrfGrpAddrType,
       "ciscoMvpnMrouteMvrfGroup": ciscoMvpnMrouteMvrfGroup,
       "ciscoMvpnMrouteMvrfSrcAddrType": ciscoMvpnMrouteMvrfSrcAddrType,
       "ciscoMvpnMrouteMvrfSource": ciscoMvpnMrouteMvrfSource,
       "ciscoMvpnMrouteUpDownStreamInfo": ciscoMvpnMrouteUpDownStreamInfo,
       "ciscoMvpnMrouteMdtGrpAddrType": ciscoMvpnMrouteMdtGrpAddrType,
       "ciscoMvpnMrouteMdtGroup": ciscoMvpnMrouteMdtGroup,
       "ciscoMvpnMrouteMdtType": ciscoMvpnMrouteMdtType,
       "ciscoMvpnBgpMdtUpdateTable": ciscoMvpnBgpMdtUpdateTable,
       "ciscoMvpnBgpMdtUpdateEntry": ciscoMvpnBgpMdtUpdateEntry,
       "ciscoMvpnBgpMdtUpdGrpAddrType": ciscoMvpnBgpMdtUpdGrpAddrType,
       "ciscoMvpnBgpMdtUpdateGroup": ciscoMvpnBgpMdtUpdateGroup,
       "ciscoMvpnBgpMdtUpdateRd": ciscoMvpnBgpMdtUpdateRd,
       "ciscoMvpnBgpMdtUpdSrcAddrType": ciscoMvpnBgpMdtUpdSrcAddrType,
       "ciscoMvpnBgpMdtUpdateSource": ciscoMvpnBgpMdtUpdateSource,
       "ciscoMvpnBgpMdtUpdOrigAddrType": ciscoMvpnBgpMdtUpdOrigAddrType,
       "ciscoMvpnBgpMdtUpdateOriginator": ciscoMvpnBgpMdtUpdateOriginator,
       "ciscoMvpnBgpMdtUpdNhAddrType": ciscoMvpnBgpMdtUpdNhAddrType,
       "ciscoMvpnBgpMdtUpdateNexthop": ciscoMvpnBgpMdtUpdateNexthop,
       "ciscoMvpnMdtJnRcvTable": ciscoMvpnMdtJnRcvTable,
       "ciscoMvpnMdtJnRcvEntry": ciscoMvpnMdtJnRcvEntry,
       "ciscoMvpnMdtJnRcvGrpAddrType": ciscoMvpnMdtJnRcvGrpAddrType,
       "ciscoMvpnMdtJnRcvGroup": ciscoMvpnMdtJnRcvGroup,
       "ciscoMvpnMdtJnRcvSrcAddrType": ciscoMvpnMdtJnRcvSrcAddrType,
       "ciscoMvpnMdtJnRcvSource": ciscoMvpnMdtJnRcvSource,
       "ciscoMvpnMdtJnRcvUpTime": ciscoMvpnMdtJnRcvUpTime,
       "ciscoMvpnMdtJnRcvExpTime": ciscoMvpnMdtJnRcvExpTime,
       "ciscoMvpnMdtJnSendTable": ciscoMvpnMdtJnSendTable,
       "ciscoMvpnMdtJnSendEntry": ciscoMvpnMdtJnSendEntry,
       "ciscoMvpnMdtJnSendGrpAddrType": ciscoMvpnMdtJnSendGrpAddrType,
       "ciscoMvpnMdtJnSendGroup": ciscoMvpnMdtJnSendGroup,
       "ciscoMvpnMdtJnSendSrcAddrType": ciscoMvpnMdtJnSendSrcAddrType,
       "ciscoMvpnMdtJnSendSource": ciscoMvpnMdtJnSendSource,
       "ciscoMvpnMdtJnSendMdtGrpAddrType": ciscoMvpnMdtJnSendMdtGrpAddrType,
       "ciscoMvpnMdtJnSendMdtGroup": ciscoMvpnMdtJnSendMdtGroup,
       "ciscoMvpnMdtJnSendMdtRefCt": ciscoMvpnMdtJnSendMdtRefCt,
       "ciscoMvpnTunnelTable": ciscoMvpnTunnelTable,
       "ciscoMvpnTunnelEntry": ciscoMvpnTunnelEntry,
       "ciscoMvpnTunnelName": ciscoMvpnTunnelName,
       "ciscoMvpnTunnelMvrf": ciscoMvpnTunnelMvrf,
       "ciscoMvpnConformance": ciscoMvpnConformance,
       "ciscoMvpnGroups": ciscoMvpnGroups,
       "ciscoMvpnScalarGroup": ciscoMvpnScalarGroup,
       "ciscoMvpnMIBGenericGroup": ciscoMvpnMIBGenericGroup,
       "ciscoMvpnMIBMdtDefaultGroup": ciscoMvpnMIBMdtDefaultGroup,
       "ciscoMvpnMIBMdtDataGroup": ciscoMvpnMIBMdtDataGroup,
       "ciscoMvpnMIBMrouteMdtGroup": ciscoMvpnMIBMrouteMdtGroup,
       "ciscoMvpnMIBBgpMdtUpdateGroup": ciscoMvpnMIBBgpMdtUpdateGroup,
       "ciscoMvpnMIBMdtJnRcvGroup": ciscoMvpnMIBMdtJnRcvGroup,
       "ciscoMvpnMIBMdtJnSendGroup": ciscoMvpnMIBMdtJnSendGroup,
       "ciscoMvpnTunnelGroup": ciscoMvpnTunnelGroup,
       "ciscoMvpnNotificationGroup": ciscoMvpnNotificationGroup,
       "ciscoMvpnCompliances": ciscoMvpnCompliances,
       "ciscoMvpnModuleFullCompliance": ciscoMvpnModuleFullCompliance,
       "ciscoMvpnModuleReadOnlyCompliance": ciscoMvpnModuleReadOnlyCompliance}
)
