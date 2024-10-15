# SNMP MIB module (TED-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TED-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:06 2024
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

(Float32TC,) = mibBuilder.importSymbols(
    "FLOAT-TC-MIB",
    "Float32TC")

(IANAGmplsLSPEncodingTypeTC,
 IANAGmplsSwitchingTypeTC) = mibBuilder.importSymbols(
    "IANA-GMPLS-TC-MIB",
    "IANAGmplsLSPEncodingTypeTC",
    "IANAGmplsSwitchingTypeTC")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "transmission")

(DisplayString,
 RowPointer,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowPointer",
    "TextualConvention")


# MODULE-IDENTITY

tedMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 273)
)
tedMIB.setRevisions(
        ("2012-12-21 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TedAreaIdTC(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )



class TedRouterIdTC(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )



class TedLinkIndexTC(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )



# MIB Managed Objects in the order of their OIDs

_TedNotifications_ObjectIdentity = ObjectIdentity
tedNotifications = _TedNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 273, 0)
)
_TedObjects_ObjectIdentity = ObjectIdentity
tedObjects = _TedObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 273, 1)
)
_TedTable_Object = MibTable
tedTable = _TedTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 1)
)
if mibBuilder.loadTexts:
    tedTable.setStatus("current")
_TedEntry_Object = MibTableRow
tedEntry = _TedEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 1, 1)
)
tedEntry.setIndexNames(
    (0, "TED-MIB", "tedLocalRouterId"),
    (0, "TED-MIB", "tedRemoteRouterId"),
    (0, "TED-MIB", "tedLinkInformationSource"),
    (0, "TED-MIB", "tedLinkIndex"),
)
if mibBuilder.loadTexts:
    tedEntry.setStatus("current")


class _TedLinkInformationSource_Type(Integer32):
    """Custom type tedLinkInformationSource based on Integer32"""
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
        *(("isis", 4),
          ("locallyConfigured", 1),
          ("ospfv2", 2),
          ("ospfv3", 3),
          ("other", 5),
          ("unknown", 0))
    )


_TedLinkInformationSource_Type.__name__ = "Integer32"
_TedLinkInformationSource_Object = MibTableColumn
tedLinkInformationSource = _TedLinkInformationSource_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 1, 1, 1),
    _TedLinkInformationSource_Type()
)
tedLinkInformationSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tedLinkInformationSource.setStatus("current")
_TedLocalRouterId_Type = TedRouterIdTC
_TedLocalRouterId_Object = MibTableColumn
tedLocalRouterId = _TedLocalRouterId_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 1, 1, 2),
    _TedLocalRouterId_Type()
)
tedLocalRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tedLocalRouterId.setStatus("current")
_TedRemoteRouterId_Type = TedRouterIdTC
_TedRemoteRouterId_Object = MibTableColumn
tedRemoteRouterId = _TedRemoteRouterId_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 1, 1, 3),
    _TedRemoteRouterId_Type()
)
tedRemoteRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tedRemoteRouterId.setStatus("current")
_TedLinkIndex_Type = TedLinkIndexTC
_TedLinkIndex_Object = MibTableColumn
tedLinkIndex = _TedLinkIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 1, 1, 4),
    _TedLinkIndex_Type()
)
tedLinkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tedLinkIndex.setStatus("current")
_TedLinkInformationData_Type = RowPointer
_TedLinkInformationData_Object = MibTableColumn
tedLinkInformationData = _TedLinkInformationData_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 1, 1, 5),
    _TedLinkInformationData_Type()
)
tedLinkInformationData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tedLinkInformationData.setStatus("current")


class _TedLinkState_Type(Integer32):
    """Custom type tedLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("unknown", 0),
          ("up", 1))
    )


_TedLinkState_Type.__name__ = "Integer32"
_TedLinkState_Object = MibTableColumn
tedLinkState = _TedLinkState_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 1, 1, 6),
    _TedLinkState_Type()
)
tedLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tedLinkState.setStatus("current")
_TedAreaId_Type = TedAreaIdTC
_TedAreaId_Object = MibTableColumn
tedAreaId = _TedAreaId_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 1, 1, 7),
    _TedAreaId_Type()
)
tedAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tedAreaId.setStatus("current")


class _TedLinkType_Type(Integer32):
    """Custom type tedLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multiAccess", 2),
          ("pointToPoint", 1))
    )


_TedLinkType_Type.__name__ = "Integer32"
_TedLinkType_Object = MibTableColumn
tedLinkType = _TedLinkType_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 1, 1, 8),
    _TedLinkType_Type()
)
tedLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tedLinkType.setStatus("current")
_TedTeRouterIdAddrType_Type = InetAddressType
_TedTeRouterIdAddrType_Object = MibTableColumn
tedTeRouterIdAddrType = _TedTeRouterIdAddrType_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 1, 1, 9),
    _TedTeRouterIdAddrType_Type()
)
tedTeRouterIdAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tedTeRouterIdAddrType.setStatus("current")
_TedTeRouterIdAddr_Type = InetAddress
_TedTeRouterIdAddr_Object = MibTableColumn
tedTeRouterIdAddr = _TedTeRouterIdAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 1, 1, 10),
    _TedTeRouterIdAddr_Type()
)
tedTeRouterIdAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tedTeRouterIdAddr.setStatus("current")
_TedLinkIdAddrType_Type = InetAddressType
_TedLinkIdAddrType_Object = MibTableColumn
tedLinkIdAddrType = _TedLinkIdAddrType_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 1, 1, 11),
    _TedLinkIdAddrType_Type()
)
tedLinkIdAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tedLinkIdAddrType.setStatus("current")
_TedLinkIdAddr_Type = InetAddress
_TedLinkIdAddr_Object = MibTableColumn
tedLinkIdAddr = _TedLinkIdAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 1, 1, 12),
    _TedLinkIdAddr_Type()
)
tedLinkIdAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tedLinkIdAddr.setStatus("current")
_TedMetric_Type = Integer32
_TedMetric_Object = MibTableColumn
tedMetric = _TedMetric_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 1, 1, 13),
    _TedMetric_Type()
)
tedMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tedMetric.setStatus("current")
_TedMaxBandwidth_Type = Float32TC
_TedMaxBandwidth_Object = MibTableColumn
tedMaxBandwidth = _TedMaxBandwidth_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 1, 1, 14),
    _TedMaxBandwidth_Type()
)
tedMaxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tedMaxBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    tedMaxBandwidth.setUnits("Byte per second")
_TedMaxReservableBandwidth_Type = Float32TC
_TedMaxReservableBandwidth_Object = MibTableColumn
tedMaxReservableBandwidth = _TedMaxReservableBandwidth_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 1, 1, 15),
    _TedMaxReservableBandwidth_Type()
)
tedMaxReservableBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tedMaxReservableBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    tedMaxReservableBandwidth.setUnits("Byte per second")
_TedUnreservedBandwidthPri0_Type = Float32TC
_TedUnreservedBandwidthPri0_Object = MibTableColumn
tedUnreservedBandwidthPri0 = _TedUnreservedBandwidthPri0_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 1, 1, 16),
    _TedUnreservedBandwidthPri0_Type()
)
tedUnreservedBandwidthPri0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tedUnreservedBandwidthPri0.setStatus("current")
if mibBuilder.loadTexts:
    tedUnreservedBandwidthPri0.setUnits("Byte per second")
_TedUnreservedBandwidthPri1_Type = Float32TC
_TedUnreservedBandwidthPri1_Object = MibTableColumn
tedUnreservedBandwidthPri1 = _TedUnreservedBandwidthPri1_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 1, 1, 17),
    _TedUnreservedBandwidthPri1_Type()
)
tedUnreservedBandwidthPri1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tedUnreservedBandwidthPri1.setStatus("current")
if mibBuilder.loadTexts:
    tedUnreservedBandwidthPri1.setUnits("Byte per second")
_TedUnreservedBandwidthPri2_Type = Float32TC
_TedUnreservedBandwidthPri2_Object = MibTableColumn
tedUnreservedBandwidthPri2 = _TedUnreservedBandwidthPri2_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 1, 1, 18),
    _TedUnreservedBandwidthPri2_Type()
)
tedUnreservedBandwidthPri2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tedUnreservedBandwidthPri2.setStatus("current")
if mibBuilder.loadTexts:
    tedUnreservedBandwidthPri2.setUnits("Byte per second")
_TedUnreservedBandwidthPri3_Type = Float32TC
_TedUnreservedBandwidthPri3_Object = MibTableColumn
tedUnreservedBandwidthPri3 = _TedUnreservedBandwidthPri3_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 1, 1, 19),
    _TedUnreservedBandwidthPri3_Type()
)
tedUnreservedBandwidthPri3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tedUnreservedBandwidthPri3.setStatus("current")
if mibBuilder.loadTexts:
    tedUnreservedBandwidthPri3.setUnits("Byte per second")
_TedUnreservedBandwidthPri4_Type = Float32TC
_TedUnreservedBandwidthPri4_Object = MibTableColumn
tedUnreservedBandwidthPri4 = _TedUnreservedBandwidthPri4_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 1, 1, 20),
    _TedUnreservedBandwidthPri4_Type()
)
tedUnreservedBandwidthPri4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tedUnreservedBandwidthPri4.setStatus("current")
if mibBuilder.loadTexts:
    tedUnreservedBandwidthPri4.setUnits("Byte per second")
_TedUnreservedBandwidthPri5_Type = Float32TC
_TedUnreservedBandwidthPri5_Object = MibTableColumn
tedUnreservedBandwidthPri5 = _TedUnreservedBandwidthPri5_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 1, 1, 21),
    _TedUnreservedBandwidthPri5_Type()
)
tedUnreservedBandwidthPri5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tedUnreservedBandwidthPri5.setStatus("current")
if mibBuilder.loadTexts:
    tedUnreservedBandwidthPri5.setUnits("Byte per second")
_TedUnreservedBandwidthPri6_Type = Float32TC
_TedUnreservedBandwidthPri6_Object = MibTableColumn
tedUnreservedBandwidthPri6 = _TedUnreservedBandwidthPri6_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 1, 1, 22),
    _TedUnreservedBandwidthPri6_Type()
)
tedUnreservedBandwidthPri6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tedUnreservedBandwidthPri6.setStatus("current")
if mibBuilder.loadTexts:
    tedUnreservedBandwidthPri6.setUnits("Byte per second")
_TedUnreservedBandwidthPri7_Type = Float32TC
_TedUnreservedBandwidthPri7_Object = MibTableColumn
tedUnreservedBandwidthPri7 = _TedUnreservedBandwidthPri7_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 1, 1, 23),
    _TedUnreservedBandwidthPri7_Type()
)
tedUnreservedBandwidthPri7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tedUnreservedBandwidthPri7.setStatus("current")
if mibBuilder.loadTexts:
    tedUnreservedBandwidthPri7.setUnits("Byte per second")
_TedAdministrativeGroup_Type = Integer32
_TedAdministrativeGroup_Object = MibTableColumn
tedAdministrativeGroup = _TedAdministrativeGroup_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 1, 1, 24),
    _TedAdministrativeGroup_Type()
)
tedAdministrativeGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tedAdministrativeGroup.setStatus("current")
_TedLocalId_Type = Integer32
_TedLocalId_Object = MibTableColumn
tedLocalId = _TedLocalId_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 1, 1, 25),
    _TedLocalId_Type()
)
tedLocalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tedLocalId.setStatus("current")
_TedRemoteId_Type = Integer32
_TedRemoteId_Object = MibTableColumn
tedRemoteId = _TedRemoteId_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 1, 1, 26),
    _TedRemoteId_Type()
)
tedRemoteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tedRemoteId.setStatus("current")


class _TedLinkProtectionType_Type(Bits):
    """Custom type tedLinkProtectionType based on Bits"""
    namedValues = NamedValues(
        *(("dedicatedOnePlusOne", 4),
          ("dedicatedOneToOne", 3),
          ("enhanced", 5),
          ("extraTraffic", 0),
          ("shared", 2),
          ("unprotected", 1))
    )

_TedLinkProtectionType_Type.__name__ = "Bits"
_TedLinkProtectionType_Object = MibTableColumn
tedLinkProtectionType = _TedLinkProtectionType_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 1, 1, 27),
    _TedLinkProtectionType_Type()
)
tedLinkProtectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tedLinkProtectionType.setStatus("current")
_TedLocalIfAddrTable_Object = MibTable
tedLocalIfAddrTable = _TedLocalIfAddrTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 2)
)
if mibBuilder.loadTexts:
    tedLocalIfAddrTable.setStatus("current")
_TedLocalIfAddrEntry_Object = MibTableRow
tedLocalIfAddrEntry = _TedLocalIfAddrEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 2, 1)
)
tedLocalIfAddrEntry.setIndexNames(
    (0, "TED-MIB", "tedLinkIndex"),
    (0, "TED-MIB", "tedLocalIfAddr"),
)
if mibBuilder.loadTexts:
    tedLocalIfAddrEntry.setStatus("current")
_TedLocalIfAddrType_Type = InetAddressType
_TedLocalIfAddrType_Object = MibTableColumn
tedLocalIfAddrType = _TedLocalIfAddrType_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 2, 1, 1),
    _TedLocalIfAddrType_Type()
)
tedLocalIfAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tedLocalIfAddrType.setStatus("current")


class _TedLocalIfAddr_Type(InetAddress):
    """Custom type tedLocalIfAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_TedLocalIfAddr_Type.__name__ = "InetAddress"
_TedLocalIfAddr_Object = MibTableColumn
tedLocalIfAddr = _TedLocalIfAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 2, 1, 2),
    _TedLocalIfAddr_Type()
)
tedLocalIfAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tedLocalIfAddr.setStatus("current")
_TedRemoteIfAddrTable_Object = MibTable
tedRemoteIfAddrTable = _TedRemoteIfAddrTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 3)
)
if mibBuilder.loadTexts:
    tedRemoteIfAddrTable.setStatus("current")
_TedRemoteIfAddrEntry_Object = MibTableRow
tedRemoteIfAddrEntry = _TedRemoteIfAddrEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 3, 1)
)
tedRemoteIfAddrEntry.setIndexNames(
    (0, "TED-MIB", "tedLinkIndex"),
    (0, "TED-MIB", "tedRemoteIfAddr"),
)
if mibBuilder.loadTexts:
    tedRemoteIfAddrEntry.setStatus("current")
_TedRemoteIfAddrType_Type = InetAddressType
_TedRemoteIfAddrType_Object = MibTableColumn
tedRemoteIfAddrType = _TedRemoteIfAddrType_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 3, 1, 1),
    _TedRemoteIfAddrType_Type()
)
tedRemoteIfAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tedRemoteIfAddrType.setStatus("current")


class _TedRemoteIfAddr_Type(InetAddress):
    """Custom type tedRemoteIfAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_TedRemoteIfAddr_Type.__name__ = "InetAddress"
_TedRemoteIfAddr_Object = MibTableColumn
tedRemoteIfAddr = _TedRemoteIfAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 3, 1, 2),
    _TedRemoteIfAddr_Type()
)
tedRemoteIfAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tedRemoteIfAddr.setStatus("current")
_TedSwCapTable_Object = MibTable
tedSwCapTable = _TedSwCapTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 4)
)
if mibBuilder.loadTexts:
    tedSwCapTable.setStatus("current")
_TedSwCapEntry_Object = MibTableRow
tedSwCapEntry = _TedSwCapEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 4, 1)
)
tedSwCapEntry.setIndexNames(
    (0, "TED-MIB", "tedLinkIndex"),
    (0, "TED-MIB", "tedSwCapIndex"),
)
if mibBuilder.loadTexts:
    tedSwCapEntry.setStatus("current")


class _TedSwCapIndex_Type(Unsigned32):
    """Custom type tedSwCapIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TedSwCapIndex_Type.__name__ = "Unsigned32"
_TedSwCapIndex_Object = MibTableColumn
tedSwCapIndex = _TedSwCapIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 4, 1, 1),
    _TedSwCapIndex_Type()
)
tedSwCapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tedSwCapIndex.setStatus("current")
_TedSwCapType_Type = IANAGmplsSwitchingTypeTC
_TedSwCapType_Object = MibTableColumn
tedSwCapType = _TedSwCapType_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 4, 1, 2),
    _TedSwCapType_Type()
)
tedSwCapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tedSwCapType.setStatus("current")
_TedSwCapEncoding_Type = IANAGmplsLSPEncodingTypeTC
_TedSwCapEncoding_Object = MibTableColumn
tedSwCapEncoding = _TedSwCapEncoding_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 4, 1, 3),
    _TedSwCapEncoding_Type()
)
tedSwCapEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tedSwCapEncoding.setStatus("current")
_TedSwCapMaxLspBandwidthPri0_Type = Float32TC
_TedSwCapMaxLspBandwidthPri0_Object = MibTableColumn
tedSwCapMaxLspBandwidthPri0 = _TedSwCapMaxLspBandwidthPri0_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 4, 1, 4),
    _TedSwCapMaxLspBandwidthPri0_Type()
)
tedSwCapMaxLspBandwidthPri0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tedSwCapMaxLspBandwidthPri0.setStatus("current")
if mibBuilder.loadTexts:
    tedSwCapMaxLspBandwidthPri0.setUnits("Byte per second")
_TedSwCapMaxLspBandwidthPri1_Type = Float32TC
_TedSwCapMaxLspBandwidthPri1_Object = MibTableColumn
tedSwCapMaxLspBandwidthPri1 = _TedSwCapMaxLspBandwidthPri1_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 4, 1, 5),
    _TedSwCapMaxLspBandwidthPri1_Type()
)
tedSwCapMaxLspBandwidthPri1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tedSwCapMaxLspBandwidthPri1.setStatus("current")
if mibBuilder.loadTexts:
    tedSwCapMaxLspBandwidthPri1.setUnits("Byte per second")
_TedSwCapMaxLspBandwidthPri2_Type = Float32TC
_TedSwCapMaxLspBandwidthPri2_Object = MibTableColumn
tedSwCapMaxLspBandwidthPri2 = _TedSwCapMaxLspBandwidthPri2_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 4, 1, 6),
    _TedSwCapMaxLspBandwidthPri2_Type()
)
tedSwCapMaxLspBandwidthPri2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tedSwCapMaxLspBandwidthPri2.setStatus("current")
if mibBuilder.loadTexts:
    tedSwCapMaxLspBandwidthPri2.setUnits("Byte per second")
_TedSwCapMaxLspBandwidthPri3_Type = Float32TC
_TedSwCapMaxLspBandwidthPri3_Object = MibTableColumn
tedSwCapMaxLspBandwidthPri3 = _TedSwCapMaxLspBandwidthPri3_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 4, 1, 7),
    _TedSwCapMaxLspBandwidthPri3_Type()
)
tedSwCapMaxLspBandwidthPri3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tedSwCapMaxLspBandwidthPri3.setStatus("current")
if mibBuilder.loadTexts:
    tedSwCapMaxLspBandwidthPri3.setUnits("Byte per second")
_TedSwCapMaxLspBandwidthPri4_Type = Float32TC
_TedSwCapMaxLspBandwidthPri4_Object = MibTableColumn
tedSwCapMaxLspBandwidthPri4 = _TedSwCapMaxLspBandwidthPri4_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 4, 1, 8),
    _TedSwCapMaxLspBandwidthPri4_Type()
)
tedSwCapMaxLspBandwidthPri4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tedSwCapMaxLspBandwidthPri4.setStatus("current")
if mibBuilder.loadTexts:
    tedSwCapMaxLspBandwidthPri4.setUnits("Byte per second")
_TedSwCapMaxLspBandwidthPri5_Type = Float32TC
_TedSwCapMaxLspBandwidthPri5_Object = MibTableColumn
tedSwCapMaxLspBandwidthPri5 = _TedSwCapMaxLspBandwidthPri5_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 4, 1, 9),
    _TedSwCapMaxLspBandwidthPri5_Type()
)
tedSwCapMaxLspBandwidthPri5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tedSwCapMaxLspBandwidthPri5.setStatus("current")
if mibBuilder.loadTexts:
    tedSwCapMaxLspBandwidthPri5.setUnits("Byte per second")
_TedSwCapMaxLspBandwidthPri6_Type = Float32TC
_TedSwCapMaxLspBandwidthPri6_Object = MibTableColumn
tedSwCapMaxLspBandwidthPri6 = _TedSwCapMaxLspBandwidthPri6_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 4, 1, 10),
    _TedSwCapMaxLspBandwidthPri6_Type()
)
tedSwCapMaxLspBandwidthPri6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tedSwCapMaxLspBandwidthPri6.setStatus("current")
if mibBuilder.loadTexts:
    tedSwCapMaxLspBandwidthPri6.setUnits("Byte per second")
_TedSwCapMaxLspBandwidthPri7_Type = Float32TC
_TedSwCapMaxLspBandwidthPri7_Object = MibTableColumn
tedSwCapMaxLspBandwidthPri7 = _TedSwCapMaxLspBandwidthPri7_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 4, 1, 11),
    _TedSwCapMaxLspBandwidthPri7_Type()
)
tedSwCapMaxLspBandwidthPri7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tedSwCapMaxLspBandwidthPri7.setStatus("current")
if mibBuilder.loadTexts:
    tedSwCapMaxLspBandwidthPri7.setUnits("Byte per second")
_TedSwCapMinLspBandwidth_Type = Float32TC
_TedSwCapMinLspBandwidth_Object = MibTableColumn
tedSwCapMinLspBandwidth = _TedSwCapMinLspBandwidth_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 4, 1, 12),
    _TedSwCapMinLspBandwidth_Type()
)
tedSwCapMinLspBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tedSwCapMinLspBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    tedSwCapMinLspBandwidth.setUnits("Byte per second")
_TedSwCapIfMtu_Type = Integer32
_TedSwCapIfMtu_Object = MibTableColumn
tedSwCapIfMtu = _TedSwCapIfMtu_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 4, 1, 13),
    _TedSwCapIfMtu_Type()
)
tedSwCapIfMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tedSwCapIfMtu.setStatus("current")


class _TedSwCapIndication_Type(Integer32):
    """Custom type tedSwCapIndication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("arbitrary", 1),
          ("standard", 0))
    )


_TedSwCapIndication_Type.__name__ = "Integer32"
_TedSwCapIndication_Object = MibTableColumn
tedSwCapIndication = _TedSwCapIndication_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 4, 1, 14),
    _TedSwCapIndication_Type()
)
tedSwCapIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tedSwCapIndication.setStatus("current")
_TedSrlgTable_Object = MibTable
tedSrlgTable = _TedSrlgTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 5)
)
if mibBuilder.loadTexts:
    tedSrlgTable.setStatus("current")
_TedSrlgEntry_Object = MibTableRow
tedSrlgEntry = _TedSrlgEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 5, 1)
)
tedSrlgEntry.setIndexNames(
    (0, "TED-MIB", "tedLinkIndex"),
    (0, "TED-MIB", "tedSrlgIndex"),
)
if mibBuilder.loadTexts:
    tedSrlgEntry.setStatus("current")


class _TedSrlgIndex_Type(Unsigned32):
    """Custom type tedSrlgIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TedSrlgIndex_Type.__name__ = "Unsigned32"
_TedSrlgIndex_Object = MibTableColumn
tedSrlgIndex = _TedSrlgIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 5, 1, 1),
    _TedSrlgIndex_Type()
)
tedSrlgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tedSrlgIndex.setStatus("current")
_TedSrlg_Type = Integer32
_TedSrlg_Object = MibTableColumn
tedSrlg = _TedSrlg_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 5, 1, 2),
    _TedSrlg_Type()
)
tedSrlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tedSrlg.setStatus("current")


class _TedStatusChangeNotificationMaxRate_Type(Unsigned32):
    """Custom type tedStatusChangeNotificationMaxRate based on Unsigned32"""
    defaultValue = 1


_TedStatusChangeNotificationMaxRate_Object = MibScalar
tedStatusChangeNotificationMaxRate = _TedStatusChangeNotificationMaxRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 6),
    _TedStatusChangeNotificationMaxRate_Type()
)
tedStatusChangeNotificationMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tedStatusChangeNotificationMaxRate.setStatus("current")


class _TedCreatedDeletedNotificationMaxRate_Type(Unsigned32):
    """Custom type tedCreatedDeletedNotificationMaxRate based on Unsigned32"""
    defaultValue = 1


_TedCreatedDeletedNotificationMaxRate_Object = MibScalar
tedCreatedDeletedNotificationMaxRate = _TedCreatedDeletedNotificationMaxRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 273, 1, 7),
    _TedCreatedDeletedNotificationMaxRate_Type()
)
tedCreatedDeletedNotificationMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tedCreatedDeletedNotificationMaxRate.setStatus("current")
_TedConformance_ObjectIdentity = ObjectIdentity
tedConformance = _TedConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 273, 2)
)
_TedCompliances_ObjectIdentity = ObjectIdentity
tedCompliances = _TedCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 273, 2, 1)
)
_TedGroups_ObjectIdentity = ObjectIdentity
tedGroups = _TedGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 273, 2, 2)
)

# Managed Objects groups

tedMainGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 273, 2, 2, 1)
)
tedMainGroup.setObjects(
      *(("TED-MIB", "tedLinkState"),
        ("TED-MIB", "tedAreaId"),
        ("TED-MIB", "tedLinkType"),
        ("TED-MIB", "tedTeRouterIdAddrType"),
        ("TED-MIB", "tedTeRouterIdAddr"),
        ("TED-MIB", "tedLinkIdAddrType"),
        ("TED-MIB", "tedLinkIdAddr"),
        ("TED-MIB", "tedMetric"),
        ("TED-MIB", "tedMaxBandwidth"),
        ("TED-MIB", "tedMaxReservableBandwidth"),
        ("TED-MIB", "tedUnreservedBandwidthPri0"),
        ("TED-MIB", "tedUnreservedBandwidthPri1"),
        ("TED-MIB", "tedUnreservedBandwidthPri2"),
        ("TED-MIB", "tedUnreservedBandwidthPri3"),
        ("TED-MIB", "tedUnreservedBandwidthPri4"),
        ("TED-MIB", "tedUnreservedBandwidthPri5"),
        ("TED-MIB", "tedUnreservedBandwidthPri6"),
        ("TED-MIB", "tedUnreservedBandwidthPri7"),
        ("TED-MIB", "tedAdministrativeGroup"),
        ("TED-MIB", "tedLinkProtectionType"),
        ("TED-MIB", "tedLinkInformationData"))
)
if mibBuilder.loadTexts:
    tedMainGroup.setStatus("current")

tedObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 273, 2, 2, 2)
)
tedObjectsGroup.setObjects(
      *(("TED-MIB", "tedStatusChangeNotificationMaxRate"),
        ("TED-MIB", "tedCreatedDeletedNotificationMaxRate"))
)
if mibBuilder.loadTexts:
    tedObjectsGroup.setStatus("current")

tedUnnumberedLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 273, 2, 2, 4)
)
tedUnnumberedLinkGroup.setObjects(
      *(("TED-MIB", "tedLocalId"),
        ("TED-MIB", "tedRemoteId"))
)
if mibBuilder.loadTexts:
    tedUnnumberedLinkGroup.setStatus("current")

tedNumberedLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 273, 2, 2, 5)
)
tedNumberedLinkGroup.setObjects(
      *(("TED-MIB", "tedLocalIfAddrType"),
        ("TED-MIB", "tedRemoteIfAddrType"))
)
if mibBuilder.loadTexts:
    tedNumberedLinkGroup.setStatus("current")

tedSwCapGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 273, 2, 2, 6)
)
tedSwCapGroup.setObjects(
      *(("TED-MIB", "tedSwCapType"),
        ("TED-MIB", "tedSwCapEncoding"),
        ("TED-MIB", "tedSwCapMaxLspBandwidthPri0"),
        ("TED-MIB", "tedSwCapMaxLspBandwidthPri1"),
        ("TED-MIB", "tedSwCapMaxLspBandwidthPri2"),
        ("TED-MIB", "tedSwCapMaxLspBandwidthPri3"),
        ("TED-MIB", "tedSwCapMaxLspBandwidthPri4"),
        ("TED-MIB", "tedSwCapMaxLspBandwidthPri5"),
        ("TED-MIB", "tedSwCapMaxLspBandwidthPri6"),
        ("TED-MIB", "tedSwCapMaxLspBandwidthPri7"))
)
if mibBuilder.loadTexts:
    tedSwCapGroup.setStatus("current")

tedSwCapMinLspBandwidthGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 273, 2, 2, 7)
)
tedSwCapMinLspBandwidthGroup.setObjects(
    ("TED-MIB", "tedSwCapMinLspBandwidth")
)
if mibBuilder.loadTexts:
    tedSwCapMinLspBandwidthGroup.setStatus("current")

tedSwCapIfMtuGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 273, 2, 2, 8)
)
tedSwCapIfMtuGroup.setObjects(
    ("TED-MIB", "tedSwCapIfMtu")
)
if mibBuilder.loadTexts:
    tedSwCapIfMtuGroup.setStatus("current")

tedSwCapIndicationGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 273, 2, 2, 9)
)
tedSwCapIndicationGroup.setObjects(
    ("TED-MIB", "tedSwCapIndication")
)
if mibBuilder.loadTexts:
    tedSwCapIndicationGroup.setStatus("current")

tedSrlgGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 273, 2, 2, 10)
)
tedSrlgGroup.setObjects(
    ("TED-MIB", "tedSrlg")
)
if mibBuilder.loadTexts:
    tedSrlgGroup.setStatus("current")


# Notification objects

tedStatusChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 273, 0, 1)
)
tedStatusChange.setObjects(
    ("TED-MIB", "tedLinkState")
)
if mibBuilder.loadTexts:
    tedStatusChange.setStatus(
        "current"
    )

tedEntryCreated = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 273, 0, 2)
)
tedEntryCreated.setObjects(
    ("TED-MIB", "tedLinkState")
)
if mibBuilder.loadTexts:
    tedEntryCreated.setStatus(
        "current"
    )

tedEntryDeleted = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 273, 0, 3)
)
tedEntryDeleted.setObjects(
    ("TED-MIB", "tedLinkState")
)
if mibBuilder.loadTexts:
    tedEntryDeleted.setStatus(
        "current"
    )


# Notifications groups

tedNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 10, 273, 2, 2, 3)
)
tedNotificationGroup.setObjects(
      *(("TED-MIB", "tedStatusChange"),
        ("TED-MIB", "tedEntryCreated"),
        ("TED-MIB", "tedEntryDeleted"))
)
if mibBuilder.loadTexts:
    tedNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tedModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 273, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tedModuleFullCompliance.setStatus(
        "current"
    )

tedModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 273, 2, 1, 2)
)
if mibBuilder.loadTexts:
    tedModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TED-MIB",
    **{"TedAreaIdTC": TedAreaIdTC,
       "TedRouterIdTC": TedRouterIdTC,
       "TedLinkIndexTC": TedLinkIndexTC,
       "tedMIB": tedMIB,
       "tedNotifications": tedNotifications,
       "tedStatusChange": tedStatusChange,
       "tedEntryCreated": tedEntryCreated,
       "tedEntryDeleted": tedEntryDeleted,
       "tedObjects": tedObjects,
       "tedTable": tedTable,
       "tedEntry": tedEntry,
       "tedLinkInformationSource": tedLinkInformationSource,
       "tedLocalRouterId": tedLocalRouterId,
       "tedRemoteRouterId": tedRemoteRouterId,
       "tedLinkIndex": tedLinkIndex,
       "tedLinkInformationData": tedLinkInformationData,
       "tedLinkState": tedLinkState,
       "tedAreaId": tedAreaId,
       "tedLinkType": tedLinkType,
       "tedTeRouterIdAddrType": tedTeRouterIdAddrType,
       "tedTeRouterIdAddr": tedTeRouterIdAddr,
       "tedLinkIdAddrType": tedLinkIdAddrType,
       "tedLinkIdAddr": tedLinkIdAddr,
       "tedMetric": tedMetric,
       "tedMaxBandwidth": tedMaxBandwidth,
       "tedMaxReservableBandwidth": tedMaxReservableBandwidth,
       "tedUnreservedBandwidthPri0": tedUnreservedBandwidthPri0,
       "tedUnreservedBandwidthPri1": tedUnreservedBandwidthPri1,
       "tedUnreservedBandwidthPri2": tedUnreservedBandwidthPri2,
       "tedUnreservedBandwidthPri3": tedUnreservedBandwidthPri3,
       "tedUnreservedBandwidthPri4": tedUnreservedBandwidthPri4,
       "tedUnreservedBandwidthPri5": tedUnreservedBandwidthPri5,
       "tedUnreservedBandwidthPri6": tedUnreservedBandwidthPri6,
       "tedUnreservedBandwidthPri7": tedUnreservedBandwidthPri7,
       "tedAdministrativeGroup": tedAdministrativeGroup,
       "tedLocalId": tedLocalId,
       "tedRemoteId": tedRemoteId,
       "tedLinkProtectionType": tedLinkProtectionType,
       "tedLocalIfAddrTable": tedLocalIfAddrTable,
       "tedLocalIfAddrEntry": tedLocalIfAddrEntry,
       "tedLocalIfAddrType": tedLocalIfAddrType,
       "tedLocalIfAddr": tedLocalIfAddr,
       "tedRemoteIfAddrTable": tedRemoteIfAddrTable,
       "tedRemoteIfAddrEntry": tedRemoteIfAddrEntry,
       "tedRemoteIfAddrType": tedRemoteIfAddrType,
       "tedRemoteIfAddr": tedRemoteIfAddr,
       "tedSwCapTable": tedSwCapTable,
       "tedSwCapEntry": tedSwCapEntry,
       "tedSwCapIndex": tedSwCapIndex,
       "tedSwCapType": tedSwCapType,
       "tedSwCapEncoding": tedSwCapEncoding,
       "tedSwCapMaxLspBandwidthPri0": tedSwCapMaxLspBandwidthPri0,
       "tedSwCapMaxLspBandwidthPri1": tedSwCapMaxLspBandwidthPri1,
       "tedSwCapMaxLspBandwidthPri2": tedSwCapMaxLspBandwidthPri2,
       "tedSwCapMaxLspBandwidthPri3": tedSwCapMaxLspBandwidthPri3,
       "tedSwCapMaxLspBandwidthPri4": tedSwCapMaxLspBandwidthPri4,
       "tedSwCapMaxLspBandwidthPri5": tedSwCapMaxLspBandwidthPri5,
       "tedSwCapMaxLspBandwidthPri6": tedSwCapMaxLspBandwidthPri6,
       "tedSwCapMaxLspBandwidthPri7": tedSwCapMaxLspBandwidthPri7,
       "tedSwCapMinLspBandwidth": tedSwCapMinLspBandwidth,
       "tedSwCapIfMtu": tedSwCapIfMtu,
       "tedSwCapIndication": tedSwCapIndication,
       "tedSrlgTable": tedSrlgTable,
       "tedSrlgEntry": tedSrlgEntry,
       "tedSrlgIndex": tedSrlgIndex,
       "tedSrlg": tedSrlg,
       "tedStatusChangeNotificationMaxRate": tedStatusChangeNotificationMaxRate,
       "tedCreatedDeletedNotificationMaxRate": tedCreatedDeletedNotificationMaxRate,
       "tedConformance": tedConformance,
       "tedCompliances": tedCompliances,
       "tedModuleFullCompliance": tedModuleFullCompliance,
       "tedModuleReadOnlyCompliance": tedModuleReadOnlyCompliance,
       "tedGroups": tedGroups,
       "tedMainGroup": tedMainGroup,
       "tedObjectsGroup": tedObjectsGroup,
       "tedNotificationGroup": tedNotificationGroup,
       "tedUnnumberedLinkGroup": tedUnnumberedLinkGroup,
       "tedNumberedLinkGroup": tedNumberedLinkGroup,
       "tedSwCapGroup": tedSwCapGroup,
       "tedSwCapMinLspBandwidthGroup": tedSwCapMinLspBandwidthGroup,
       "tedSwCapIfMtuGroup": tedSwCapIfMtuGroup,
       "tedSwCapIndicationGroup": tedSwCapIndicationGroup,
       "tedSrlgGroup": tedSrlgGroup}
)
