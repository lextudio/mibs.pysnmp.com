# SNMP MIB module (NAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:06:02 2024
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

(ifCounterDiscontinuityGroup,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifCounterDiscontinuityGroup",
    "ifIndex")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "mib-2")

(DisplayString,
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

natMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 123)
)
natMIB.setRevisions(
        ("2015-10-02 00:00",
         "2005-03-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NatProtocolType(Integer32, TextualConvention):
    status = "deprecated"
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
        *(("icmp", 3),
          ("none", 1),
          ("other", 2),
          ("tcp", 5),
          ("udp", 4))
    )



class NatProtocolMap(Bits, TextualConvention):
    status = "deprecated"


class NatAddrMapId(Unsigned32, TextualConvention):
    status = "deprecated"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class NatBindIdOrZero(Unsigned32, TextualConvention):
    status = "deprecated"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class NatBindId(Unsigned32, TextualConvention):
    status = "deprecated"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class NatSessionId(Unsigned32, TextualConvention):
    status = "deprecated"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class NatBindMode(Integer32, TextualConvention):
    status = "deprecated"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("addressBind", 1),
          ("addressPortBind", 2))
    )



class NatAssociationType(Integer32, TextualConvention):
    status = "deprecated"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )



class NatTranslationEntity(Bits, TextualConvention):
    status = "deprecated"


# MIB Managed Objects in the order of their OIDs

_NatMIBNotifications_ObjectIdentity = ObjectIdentity
natMIBNotifications = _NatMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 123, 0)
)
_NatMIBObjects_ObjectIdentity = ObjectIdentity
natMIBObjects = _NatMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 123, 1)
)
_NatDefTimeouts_ObjectIdentity = ObjectIdentity
natDefTimeouts = _NatDefTimeouts_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 123, 1, 1)
)


class _NatBindDefIdleTimeout_Type(Unsigned32):
    """Custom type natBindDefIdleTimeout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NatBindDefIdleTimeout_Type.__name__ = "Unsigned32"
_NatBindDefIdleTimeout_Object = MibScalar
natBindDefIdleTimeout = _NatBindDefIdleTimeout_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 1, 1),
    _NatBindDefIdleTimeout_Type()
)
natBindDefIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natBindDefIdleTimeout.setStatus("deprecated")
if mibBuilder.loadTexts:
    natBindDefIdleTimeout.setUnits("seconds")


class _NatUdpDefIdleTimeout_Type(Unsigned32):
    """Custom type natUdpDefIdleTimeout based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_NatUdpDefIdleTimeout_Type.__name__ = "Unsigned32"
_NatUdpDefIdleTimeout_Object = MibScalar
natUdpDefIdleTimeout = _NatUdpDefIdleTimeout_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 1, 2),
    _NatUdpDefIdleTimeout_Type()
)
natUdpDefIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natUdpDefIdleTimeout.setStatus("deprecated")
if mibBuilder.loadTexts:
    natUdpDefIdleTimeout.setUnits("seconds")


class _NatIcmpDefIdleTimeout_Type(Unsigned32):
    """Custom type natIcmpDefIdleTimeout based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_NatIcmpDefIdleTimeout_Type.__name__ = "Unsigned32"
_NatIcmpDefIdleTimeout_Object = MibScalar
natIcmpDefIdleTimeout = _NatIcmpDefIdleTimeout_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 1, 3),
    _NatIcmpDefIdleTimeout_Type()
)
natIcmpDefIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natIcmpDefIdleTimeout.setStatus("deprecated")
if mibBuilder.loadTexts:
    natIcmpDefIdleTimeout.setUnits("seconds")


class _NatOtherDefIdleTimeout_Type(Unsigned32):
    """Custom type natOtherDefIdleTimeout based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_NatOtherDefIdleTimeout_Type.__name__ = "Unsigned32"
_NatOtherDefIdleTimeout_Object = MibScalar
natOtherDefIdleTimeout = _NatOtherDefIdleTimeout_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 1, 4),
    _NatOtherDefIdleTimeout_Type()
)
natOtherDefIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natOtherDefIdleTimeout.setStatus("deprecated")
if mibBuilder.loadTexts:
    natOtherDefIdleTimeout.setUnits("seconds")


class _NatTcpDefIdleTimeout_Type(Unsigned32):
    """Custom type natTcpDefIdleTimeout based on Unsigned32"""
    defaultValue = 86400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_NatTcpDefIdleTimeout_Type.__name__ = "Unsigned32"
_NatTcpDefIdleTimeout_Object = MibScalar
natTcpDefIdleTimeout = _NatTcpDefIdleTimeout_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 1, 5),
    _NatTcpDefIdleTimeout_Type()
)
natTcpDefIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natTcpDefIdleTimeout.setStatus("deprecated")
if mibBuilder.loadTexts:
    natTcpDefIdleTimeout.setUnits("seconds")


class _NatTcpDefNegTimeout_Type(Unsigned32):
    """Custom type natTcpDefNegTimeout based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_NatTcpDefNegTimeout_Type.__name__ = "Unsigned32"
_NatTcpDefNegTimeout_Object = MibScalar
natTcpDefNegTimeout = _NatTcpDefNegTimeout_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 1, 6),
    _NatTcpDefNegTimeout_Type()
)
natTcpDefNegTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natTcpDefNegTimeout.setStatus("deprecated")
if mibBuilder.loadTexts:
    natTcpDefNegTimeout.setUnits("seconds")
_NatNotifCtrl_ObjectIdentity = ObjectIdentity
natNotifCtrl = _NatNotifCtrl_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 123, 1, 2)
)


class _NatNotifThrottlingInterval_Type(Integer32):
    """Custom type natNotifThrottlingInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 3600),
    )


_NatNotifThrottlingInterval_Type.__name__ = "Integer32"
_NatNotifThrottlingInterval_Object = MibScalar
natNotifThrottlingInterval = _NatNotifThrottlingInterval_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 2, 1),
    _NatNotifThrottlingInterval_Type()
)
natNotifThrottlingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natNotifThrottlingInterval.setStatus("deprecated")
if mibBuilder.loadTexts:
    natNotifThrottlingInterval.setUnits("seconds")
_NatInterfaceTable_Object = MibTable
natInterfaceTable = _NatInterfaceTable_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 3)
)
if mibBuilder.loadTexts:
    natInterfaceTable.setStatus("deprecated")
_NatInterfaceEntry_Object = MibTableRow
natInterfaceEntry = _NatInterfaceEntry_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 3, 1)
)
natInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    natInterfaceEntry.setStatus("deprecated")


class _NatInterfaceRealm_Type(Integer32):
    """Custom type natInterfaceRealm based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("private", 1),
          ("public", 2))
    )


_NatInterfaceRealm_Type.__name__ = "Integer32"
_NatInterfaceRealm_Object = MibTableColumn
natInterfaceRealm = _NatInterfaceRealm_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 3, 1, 1),
    _NatInterfaceRealm_Type()
)
natInterfaceRealm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    natInterfaceRealm.setStatus("deprecated")


class _NatInterfaceServiceType_Type(Bits):
    """Custom type natInterfaceServiceType based on Bits"""
    namedValues = NamedValues(
        *(("basicNat", 0),
          ("bidirectionalNat", 2),
          ("napt", 1),
          ("twiceNat", 3))
    )

_NatInterfaceServiceType_Type.__name__ = "Bits"
_NatInterfaceServiceType_Object = MibTableColumn
natInterfaceServiceType = _NatInterfaceServiceType_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 3, 1, 2),
    _NatInterfaceServiceType_Type()
)
natInterfaceServiceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    natInterfaceServiceType.setStatus("deprecated")
_NatInterfaceInTranslates_Type = Counter64
_NatInterfaceInTranslates_Object = MibTableColumn
natInterfaceInTranslates = _NatInterfaceInTranslates_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 3, 1, 3),
    _NatInterfaceInTranslates_Type()
)
natInterfaceInTranslates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natInterfaceInTranslates.setStatus("deprecated")
_NatInterfaceOutTranslates_Type = Counter64
_NatInterfaceOutTranslates_Object = MibTableColumn
natInterfaceOutTranslates = _NatInterfaceOutTranslates_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 3, 1, 4),
    _NatInterfaceOutTranslates_Type()
)
natInterfaceOutTranslates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natInterfaceOutTranslates.setStatus("deprecated")
_NatInterfaceDiscards_Type = Counter64
_NatInterfaceDiscards_Object = MibTableColumn
natInterfaceDiscards = _NatInterfaceDiscards_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 3, 1, 5),
    _NatInterfaceDiscards_Type()
)
natInterfaceDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natInterfaceDiscards.setStatus("deprecated")


class _NatInterfaceStorageType_Type(StorageType):
    """Custom type natInterfaceStorageType based on StorageType"""


_NatInterfaceStorageType_Object = MibTableColumn
natInterfaceStorageType = _NatInterfaceStorageType_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 3, 1, 6),
    _NatInterfaceStorageType_Type()
)
natInterfaceStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    natInterfaceStorageType.setStatus("deprecated")
_NatInterfaceRowStatus_Type = RowStatus
_NatInterfaceRowStatus_Object = MibTableColumn
natInterfaceRowStatus = _NatInterfaceRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 3, 1, 7),
    _NatInterfaceRowStatus_Type()
)
natInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    natInterfaceRowStatus.setStatus("deprecated")
_NatAddrMapTable_Object = MibTable
natAddrMapTable = _NatAddrMapTable_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 4)
)
if mibBuilder.loadTexts:
    natAddrMapTable.setStatus("deprecated")
_NatAddrMapEntry_Object = MibTableRow
natAddrMapEntry = _NatAddrMapEntry_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 4, 1)
)
natAddrMapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "NAT-MIB", "natAddrMapIndex"),
)
if mibBuilder.loadTexts:
    natAddrMapEntry.setStatus("deprecated")
_NatAddrMapIndex_Type = NatAddrMapId
_NatAddrMapIndex_Object = MibTableColumn
natAddrMapIndex = _NatAddrMapIndex_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 1),
    _NatAddrMapIndex_Type()
)
natAddrMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natAddrMapIndex.setStatus("deprecated")


class _NatAddrMapName_Type(SnmpAdminString):
    """Custom type natAddrMapName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NatAddrMapName_Type.__name__ = "SnmpAdminString"
_NatAddrMapName_Object = MibTableColumn
natAddrMapName = _NatAddrMapName_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 2),
    _NatAddrMapName_Type()
)
natAddrMapName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    natAddrMapName.setStatus("deprecated")
_NatAddrMapEntryType_Type = NatAssociationType
_NatAddrMapEntryType_Object = MibTableColumn
natAddrMapEntryType = _NatAddrMapEntryType_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 3),
    _NatAddrMapEntryType_Type()
)
natAddrMapEntryType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    natAddrMapEntryType.setStatus("deprecated")
_NatAddrMapTranslationEntity_Type = NatTranslationEntity
_NatAddrMapTranslationEntity_Object = MibTableColumn
natAddrMapTranslationEntity = _NatAddrMapTranslationEntity_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 4),
    _NatAddrMapTranslationEntity_Type()
)
natAddrMapTranslationEntity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    natAddrMapTranslationEntity.setStatus("deprecated")
_NatAddrMapLocalAddrType_Type = InetAddressType
_NatAddrMapLocalAddrType_Object = MibTableColumn
natAddrMapLocalAddrType = _NatAddrMapLocalAddrType_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 5),
    _NatAddrMapLocalAddrType_Type()
)
natAddrMapLocalAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    natAddrMapLocalAddrType.setStatus("deprecated")
_NatAddrMapLocalAddrFrom_Type = InetAddress
_NatAddrMapLocalAddrFrom_Object = MibTableColumn
natAddrMapLocalAddrFrom = _NatAddrMapLocalAddrFrom_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 6),
    _NatAddrMapLocalAddrFrom_Type()
)
natAddrMapLocalAddrFrom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    natAddrMapLocalAddrFrom.setStatus("deprecated")
_NatAddrMapLocalAddrTo_Type = InetAddress
_NatAddrMapLocalAddrTo_Object = MibTableColumn
natAddrMapLocalAddrTo = _NatAddrMapLocalAddrTo_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 7),
    _NatAddrMapLocalAddrTo_Type()
)
natAddrMapLocalAddrTo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    natAddrMapLocalAddrTo.setStatus("deprecated")


class _NatAddrMapLocalPortFrom_Type(InetPortNumber):
    """Custom type natAddrMapLocalPortFrom based on InetPortNumber"""
    defaultValue = 0


_NatAddrMapLocalPortFrom_Object = MibTableColumn
natAddrMapLocalPortFrom = _NatAddrMapLocalPortFrom_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 8),
    _NatAddrMapLocalPortFrom_Type()
)
natAddrMapLocalPortFrom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    natAddrMapLocalPortFrom.setStatus("deprecated")


class _NatAddrMapLocalPortTo_Type(InetPortNumber):
    """Custom type natAddrMapLocalPortTo based on InetPortNumber"""
    defaultValue = 0


_NatAddrMapLocalPortTo_Object = MibTableColumn
natAddrMapLocalPortTo = _NatAddrMapLocalPortTo_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 9),
    _NatAddrMapLocalPortTo_Type()
)
natAddrMapLocalPortTo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    natAddrMapLocalPortTo.setStatus("deprecated")
_NatAddrMapGlobalAddrType_Type = InetAddressType
_NatAddrMapGlobalAddrType_Object = MibTableColumn
natAddrMapGlobalAddrType = _NatAddrMapGlobalAddrType_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 10),
    _NatAddrMapGlobalAddrType_Type()
)
natAddrMapGlobalAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    natAddrMapGlobalAddrType.setStatus("deprecated")
_NatAddrMapGlobalAddrFrom_Type = InetAddress
_NatAddrMapGlobalAddrFrom_Object = MibTableColumn
natAddrMapGlobalAddrFrom = _NatAddrMapGlobalAddrFrom_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 11),
    _NatAddrMapGlobalAddrFrom_Type()
)
natAddrMapGlobalAddrFrom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    natAddrMapGlobalAddrFrom.setStatus("deprecated")
_NatAddrMapGlobalAddrTo_Type = InetAddress
_NatAddrMapGlobalAddrTo_Object = MibTableColumn
natAddrMapGlobalAddrTo = _NatAddrMapGlobalAddrTo_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 12),
    _NatAddrMapGlobalAddrTo_Type()
)
natAddrMapGlobalAddrTo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    natAddrMapGlobalAddrTo.setStatus("deprecated")


class _NatAddrMapGlobalPortFrom_Type(InetPortNumber):
    """Custom type natAddrMapGlobalPortFrom based on InetPortNumber"""
    defaultValue = 0


_NatAddrMapGlobalPortFrom_Object = MibTableColumn
natAddrMapGlobalPortFrom = _NatAddrMapGlobalPortFrom_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 13),
    _NatAddrMapGlobalPortFrom_Type()
)
natAddrMapGlobalPortFrom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    natAddrMapGlobalPortFrom.setStatus("deprecated")


class _NatAddrMapGlobalPortTo_Type(InetPortNumber):
    """Custom type natAddrMapGlobalPortTo based on InetPortNumber"""
    defaultValue = 0


_NatAddrMapGlobalPortTo_Object = MibTableColumn
natAddrMapGlobalPortTo = _NatAddrMapGlobalPortTo_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 14),
    _NatAddrMapGlobalPortTo_Type()
)
natAddrMapGlobalPortTo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    natAddrMapGlobalPortTo.setStatus("deprecated")
_NatAddrMapProtocol_Type = NatProtocolMap
_NatAddrMapProtocol_Object = MibTableColumn
natAddrMapProtocol = _NatAddrMapProtocol_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 15),
    _NatAddrMapProtocol_Type()
)
natAddrMapProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    natAddrMapProtocol.setStatus("deprecated")
_NatAddrMapInTranslates_Type = Counter64
_NatAddrMapInTranslates_Object = MibTableColumn
natAddrMapInTranslates = _NatAddrMapInTranslates_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 16),
    _NatAddrMapInTranslates_Type()
)
natAddrMapInTranslates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natAddrMapInTranslates.setStatus("deprecated")
_NatAddrMapOutTranslates_Type = Counter64
_NatAddrMapOutTranslates_Object = MibTableColumn
natAddrMapOutTranslates = _NatAddrMapOutTranslates_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 17),
    _NatAddrMapOutTranslates_Type()
)
natAddrMapOutTranslates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natAddrMapOutTranslates.setStatus("deprecated")
_NatAddrMapDiscards_Type = Counter64
_NatAddrMapDiscards_Object = MibTableColumn
natAddrMapDiscards = _NatAddrMapDiscards_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 18),
    _NatAddrMapDiscards_Type()
)
natAddrMapDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natAddrMapDiscards.setStatus("deprecated")
_NatAddrMapAddrUsed_Type = Gauge32
_NatAddrMapAddrUsed_Object = MibTableColumn
natAddrMapAddrUsed = _NatAddrMapAddrUsed_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 19),
    _NatAddrMapAddrUsed_Type()
)
natAddrMapAddrUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natAddrMapAddrUsed.setStatus("deprecated")


class _NatAddrMapStorageType_Type(StorageType):
    """Custom type natAddrMapStorageType based on StorageType"""


_NatAddrMapStorageType_Object = MibTableColumn
natAddrMapStorageType = _NatAddrMapStorageType_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 20),
    _NatAddrMapStorageType_Type()
)
natAddrMapStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    natAddrMapStorageType.setStatus("deprecated")
_NatAddrMapRowStatus_Type = RowStatus
_NatAddrMapRowStatus_Object = MibTableColumn
natAddrMapRowStatus = _NatAddrMapRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 4, 1, 21),
    _NatAddrMapRowStatus_Type()
)
natAddrMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    natAddrMapRowStatus.setStatus("deprecated")
_NatAddrBindNumberOfEntries_Type = Gauge32
_NatAddrBindNumberOfEntries_Object = MibScalar
natAddrBindNumberOfEntries = _NatAddrBindNumberOfEntries_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 5),
    _NatAddrBindNumberOfEntries_Type()
)
natAddrBindNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natAddrBindNumberOfEntries.setStatus("deprecated")
_NatAddrBindTable_Object = MibTable
natAddrBindTable = _NatAddrBindTable_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 6)
)
if mibBuilder.loadTexts:
    natAddrBindTable.setStatus("deprecated")
_NatAddrBindEntry_Object = MibTableRow
natAddrBindEntry = _NatAddrBindEntry_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 6, 1)
)
natAddrBindEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "NAT-MIB", "natAddrBindLocalAddrType"),
    (0, "NAT-MIB", "natAddrBindLocalAddr"),
)
if mibBuilder.loadTexts:
    natAddrBindEntry.setStatus("deprecated")
_NatAddrBindLocalAddrType_Type = InetAddressType
_NatAddrBindLocalAddrType_Object = MibTableColumn
natAddrBindLocalAddrType = _NatAddrBindLocalAddrType_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 6, 1, 1),
    _NatAddrBindLocalAddrType_Type()
)
natAddrBindLocalAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natAddrBindLocalAddrType.setStatus("deprecated")


class _NatAddrBindLocalAddr_Type(InetAddress):
    """Custom type natAddrBindLocalAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_NatAddrBindLocalAddr_Type.__name__ = "InetAddress"
_NatAddrBindLocalAddr_Object = MibTableColumn
natAddrBindLocalAddr = _NatAddrBindLocalAddr_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 6, 1, 2),
    _NatAddrBindLocalAddr_Type()
)
natAddrBindLocalAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natAddrBindLocalAddr.setStatus("deprecated")
_NatAddrBindGlobalAddrType_Type = InetAddressType
_NatAddrBindGlobalAddrType_Object = MibTableColumn
natAddrBindGlobalAddrType = _NatAddrBindGlobalAddrType_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 6, 1, 3),
    _NatAddrBindGlobalAddrType_Type()
)
natAddrBindGlobalAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natAddrBindGlobalAddrType.setStatus("deprecated")
_NatAddrBindGlobalAddr_Type = InetAddress
_NatAddrBindGlobalAddr_Object = MibTableColumn
natAddrBindGlobalAddr = _NatAddrBindGlobalAddr_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 6, 1, 4),
    _NatAddrBindGlobalAddr_Type()
)
natAddrBindGlobalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natAddrBindGlobalAddr.setStatus("deprecated")
_NatAddrBindId_Type = NatBindId
_NatAddrBindId_Object = MibTableColumn
natAddrBindId = _NatAddrBindId_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 6, 1, 5),
    _NatAddrBindId_Type()
)
natAddrBindId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natAddrBindId.setStatus("deprecated")
_NatAddrBindTranslationEntity_Type = NatTranslationEntity
_NatAddrBindTranslationEntity_Object = MibTableColumn
natAddrBindTranslationEntity = _NatAddrBindTranslationEntity_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 6, 1, 6),
    _NatAddrBindTranslationEntity_Type()
)
natAddrBindTranslationEntity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natAddrBindTranslationEntity.setStatus("deprecated")
_NatAddrBindType_Type = NatAssociationType
_NatAddrBindType_Object = MibTableColumn
natAddrBindType = _NatAddrBindType_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 6, 1, 7),
    _NatAddrBindType_Type()
)
natAddrBindType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natAddrBindType.setStatus("deprecated")
_NatAddrBindMapIndex_Type = NatAddrMapId
_NatAddrBindMapIndex_Object = MibTableColumn
natAddrBindMapIndex = _NatAddrBindMapIndex_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 6, 1, 8),
    _NatAddrBindMapIndex_Type()
)
natAddrBindMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natAddrBindMapIndex.setStatus("deprecated")
_NatAddrBindSessions_Type = Gauge32
_NatAddrBindSessions_Object = MibTableColumn
natAddrBindSessions = _NatAddrBindSessions_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 6, 1, 9),
    _NatAddrBindSessions_Type()
)
natAddrBindSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natAddrBindSessions.setStatus("deprecated")
_NatAddrBindMaxIdleTime_Type = TimeTicks
_NatAddrBindMaxIdleTime_Object = MibTableColumn
natAddrBindMaxIdleTime = _NatAddrBindMaxIdleTime_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 6, 1, 10),
    _NatAddrBindMaxIdleTime_Type()
)
natAddrBindMaxIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natAddrBindMaxIdleTime.setStatus("deprecated")
_NatAddrBindCurrentIdleTime_Type = TimeTicks
_NatAddrBindCurrentIdleTime_Object = MibTableColumn
natAddrBindCurrentIdleTime = _NatAddrBindCurrentIdleTime_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 6, 1, 11),
    _NatAddrBindCurrentIdleTime_Type()
)
natAddrBindCurrentIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natAddrBindCurrentIdleTime.setStatus("deprecated")
_NatAddrBindInTranslates_Type = Counter64
_NatAddrBindInTranslates_Object = MibTableColumn
natAddrBindInTranslates = _NatAddrBindInTranslates_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 6, 1, 12),
    _NatAddrBindInTranslates_Type()
)
natAddrBindInTranslates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natAddrBindInTranslates.setStatus("deprecated")
_NatAddrBindOutTranslates_Type = Counter64
_NatAddrBindOutTranslates_Object = MibTableColumn
natAddrBindOutTranslates = _NatAddrBindOutTranslates_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 6, 1, 13),
    _NatAddrBindOutTranslates_Type()
)
natAddrBindOutTranslates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natAddrBindOutTranslates.setStatus("deprecated")
_NatAddrPortBindNumberOfEntries_Type = Gauge32
_NatAddrPortBindNumberOfEntries_Object = MibScalar
natAddrPortBindNumberOfEntries = _NatAddrPortBindNumberOfEntries_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 7),
    _NatAddrPortBindNumberOfEntries_Type()
)
natAddrPortBindNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natAddrPortBindNumberOfEntries.setStatus("deprecated")
_NatAddrPortBindTable_Object = MibTable
natAddrPortBindTable = _NatAddrPortBindTable_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 8)
)
if mibBuilder.loadTexts:
    natAddrPortBindTable.setStatus("deprecated")
_NatAddrPortBindEntry_Object = MibTableRow
natAddrPortBindEntry = _NatAddrPortBindEntry_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 8, 1)
)
natAddrPortBindEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "NAT-MIB", "natAddrPortBindLocalAddrType"),
    (0, "NAT-MIB", "natAddrPortBindLocalAddr"),
    (0, "NAT-MIB", "natAddrPortBindLocalPort"),
    (0, "NAT-MIB", "natAddrPortBindProtocol"),
)
if mibBuilder.loadTexts:
    natAddrPortBindEntry.setStatus("deprecated")
_NatAddrPortBindLocalAddrType_Type = InetAddressType
_NatAddrPortBindLocalAddrType_Object = MibTableColumn
natAddrPortBindLocalAddrType = _NatAddrPortBindLocalAddrType_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 8, 1, 1),
    _NatAddrPortBindLocalAddrType_Type()
)
natAddrPortBindLocalAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natAddrPortBindLocalAddrType.setStatus("deprecated")


class _NatAddrPortBindLocalAddr_Type(InetAddress):
    """Custom type natAddrPortBindLocalAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_NatAddrPortBindLocalAddr_Type.__name__ = "InetAddress"
_NatAddrPortBindLocalAddr_Object = MibTableColumn
natAddrPortBindLocalAddr = _NatAddrPortBindLocalAddr_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 8, 1, 2),
    _NatAddrPortBindLocalAddr_Type()
)
natAddrPortBindLocalAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natAddrPortBindLocalAddr.setStatus("deprecated")
_NatAddrPortBindLocalPort_Type = InetPortNumber
_NatAddrPortBindLocalPort_Object = MibTableColumn
natAddrPortBindLocalPort = _NatAddrPortBindLocalPort_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 8, 1, 3),
    _NatAddrPortBindLocalPort_Type()
)
natAddrPortBindLocalPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natAddrPortBindLocalPort.setStatus("deprecated")
_NatAddrPortBindProtocol_Type = NatProtocolType
_NatAddrPortBindProtocol_Object = MibTableColumn
natAddrPortBindProtocol = _NatAddrPortBindProtocol_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 8, 1, 4),
    _NatAddrPortBindProtocol_Type()
)
natAddrPortBindProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natAddrPortBindProtocol.setStatus("deprecated")
_NatAddrPortBindGlobalAddrType_Type = InetAddressType
_NatAddrPortBindGlobalAddrType_Object = MibTableColumn
natAddrPortBindGlobalAddrType = _NatAddrPortBindGlobalAddrType_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 8, 1, 5),
    _NatAddrPortBindGlobalAddrType_Type()
)
natAddrPortBindGlobalAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natAddrPortBindGlobalAddrType.setStatus("deprecated")
_NatAddrPortBindGlobalAddr_Type = InetAddress
_NatAddrPortBindGlobalAddr_Object = MibTableColumn
natAddrPortBindGlobalAddr = _NatAddrPortBindGlobalAddr_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 8, 1, 6),
    _NatAddrPortBindGlobalAddr_Type()
)
natAddrPortBindGlobalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natAddrPortBindGlobalAddr.setStatus("deprecated")
_NatAddrPortBindGlobalPort_Type = InetPortNumber
_NatAddrPortBindGlobalPort_Object = MibTableColumn
natAddrPortBindGlobalPort = _NatAddrPortBindGlobalPort_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 8, 1, 7),
    _NatAddrPortBindGlobalPort_Type()
)
natAddrPortBindGlobalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natAddrPortBindGlobalPort.setStatus("deprecated")
_NatAddrPortBindId_Type = NatBindId
_NatAddrPortBindId_Object = MibTableColumn
natAddrPortBindId = _NatAddrPortBindId_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 8, 1, 8),
    _NatAddrPortBindId_Type()
)
natAddrPortBindId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natAddrPortBindId.setStatus("deprecated")
_NatAddrPortBindTranslationEntity_Type = NatTranslationEntity
_NatAddrPortBindTranslationEntity_Object = MibTableColumn
natAddrPortBindTranslationEntity = _NatAddrPortBindTranslationEntity_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 8, 1, 9),
    _NatAddrPortBindTranslationEntity_Type()
)
natAddrPortBindTranslationEntity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natAddrPortBindTranslationEntity.setStatus("deprecated")
_NatAddrPortBindType_Type = NatAssociationType
_NatAddrPortBindType_Object = MibTableColumn
natAddrPortBindType = _NatAddrPortBindType_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 8, 1, 10),
    _NatAddrPortBindType_Type()
)
natAddrPortBindType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natAddrPortBindType.setStatus("deprecated")
_NatAddrPortBindMapIndex_Type = NatAddrMapId
_NatAddrPortBindMapIndex_Object = MibTableColumn
natAddrPortBindMapIndex = _NatAddrPortBindMapIndex_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 8, 1, 11),
    _NatAddrPortBindMapIndex_Type()
)
natAddrPortBindMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natAddrPortBindMapIndex.setStatus("deprecated")
_NatAddrPortBindSessions_Type = Gauge32
_NatAddrPortBindSessions_Object = MibTableColumn
natAddrPortBindSessions = _NatAddrPortBindSessions_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 8, 1, 12),
    _NatAddrPortBindSessions_Type()
)
natAddrPortBindSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natAddrPortBindSessions.setStatus("deprecated")
_NatAddrPortBindMaxIdleTime_Type = TimeTicks
_NatAddrPortBindMaxIdleTime_Object = MibTableColumn
natAddrPortBindMaxIdleTime = _NatAddrPortBindMaxIdleTime_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 8, 1, 13),
    _NatAddrPortBindMaxIdleTime_Type()
)
natAddrPortBindMaxIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natAddrPortBindMaxIdleTime.setStatus("deprecated")
_NatAddrPortBindCurrentIdleTime_Type = TimeTicks
_NatAddrPortBindCurrentIdleTime_Object = MibTableColumn
natAddrPortBindCurrentIdleTime = _NatAddrPortBindCurrentIdleTime_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 8, 1, 14),
    _NatAddrPortBindCurrentIdleTime_Type()
)
natAddrPortBindCurrentIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natAddrPortBindCurrentIdleTime.setStatus("deprecated")
_NatAddrPortBindInTranslates_Type = Counter64
_NatAddrPortBindInTranslates_Object = MibTableColumn
natAddrPortBindInTranslates = _NatAddrPortBindInTranslates_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 8, 1, 15),
    _NatAddrPortBindInTranslates_Type()
)
natAddrPortBindInTranslates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natAddrPortBindInTranslates.setStatus("deprecated")
_NatAddrPortBindOutTranslates_Type = Counter64
_NatAddrPortBindOutTranslates_Object = MibTableColumn
natAddrPortBindOutTranslates = _NatAddrPortBindOutTranslates_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 8, 1, 16),
    _NatAddrPortBindOutTranslates_Type()
)
natAddrPortBindOutTranslates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natAddrPortBindOutTranslates.setStatus("deprecated")
_NatSessionTable_Object = MibTable
natSessionTable = _NatSessionTable_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 9)
)
if mibBuilder.loadTexts:
    natSessionTable.setStatus("deprecated")
_NatSessionEntry_Object = MibTableRow
natSessionEntry = _NatSessionEntry_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 9, 1)
)
natSessionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "NAT-MIB", "natSessionIndex"),
)
if mibBuilder.loadTexts:
    natSessionEntry.setStatus("deprecated")
_NatSessionIndex_Type = NatSessionId
_NatSessionIndex_Object = MibTableColumn
natSessionIndex = _NatSessionIndex_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 1),
    _NatSessionIndex_Type()
)
natSessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natSessionIndex.setStatus("deprecated")
_NatSessionPrivateSrcEPBindId_Type = NatBindIdOrZero
_NatSessionPrivateSrcEPBindId_Object = MibTableColumn
natSessionPrivateSrcEPBindId = _NatSessionPrivateSrcEPBindId_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 2),
    _NatSessionPrivateSrcEPBindId_Type()
)
natSessionPrivateSrcEPBindId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natSessionPrivateSrcEPBindId.setStatus("deprecated")
_NatSessionPrivateSrcEPBindMode_Type = NatBindMode
_NatSessionPrivateSrcEPBindMode_Object = MibTableColumn
natSessionPrivateSrcEPBindMode = _NatSessionPrivateSrcEPBindMode_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 3),
    _NatSessionPrivateSrcEPBindMode_Type()
)
natSessionPrivateSrcEPBindMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natSessionPrivateSrcEPBindMode.setStatus("deprecated")
_NatSessionPrivateDstEPBindId_Type = NatBindIdOrZero
_NatSessionPrivateDstEPBindId_Object = MibTableColumn
natSessionPrivateDstEPBindId = _NatSessionPrivateDstEPBindId_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 4),
    _NatSessionPrivateDstEPBindId_Type()
)
natSessionPrivateDstEPBindId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natSessionPrivateDstEPBindId.setStatus("deprecated")
_NatSessionPrivateDstEPBindMode_Type = NatBindMode
_NatSessionPrivateDstEPBindMode_Object = MibTableColumn
natSessionPrivateDstEPBindMode = _NatSessionPrivateDstEPBindMode_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 5),
    _NatSessionPrivateDstEPBindMode_Type()
)
natSessionPrivateDstEPBindMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natSessionPrivateDstEPBindMode.setStatus("deprecated")


class _NatSessionDirection_Type(Integer32):
    """Custom type natSessionDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_NatSessionDirection_Type.__name__ = "Integer32"
_NatSessionDirection_Object = MibTableColumn
natSessionDirection = _NatSessionDirection_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 6),
    _NatSessionDirection_Type()
)
natSessionDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natSessionDirection.setStatus("deprecated")
_NatSessionUpTime_Type = TimeTicks
_NatSessionUpTime_Object = MibTableColumn
natSessionUpTime = _NatSessionUpTime_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 7),
    _NatSessionUpTime_Type()
)
natSessionUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natSessionUpTime.setStatus("deprecated")
_NatSessionAddrMapIndex_Type = NatAddrMapId
_NatSessionAddrMapIndex_Object = MibTableColumn
natSessionAddrMapIndex = _NatSessionAddrMapIndex_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 8),
    _NatSessionAddrMapIndex_Type()
)
natSessionAddrMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natSessionAddrMapIndex.setStatus("deprecated")
_NatSessionProtocolType_Type = NatProtocolType
_NatSessionProtocolType_Object = MibTableColumn
natSessionProtocolType = _NatSessionProtocolType_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 9),
    _NatSessionProtocolType_Type()
)
natSessionProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natSessionProtocolType.setStatus("deprecated")
_NatSessionPrivateAddrType_Type = InetAddressType
_NatSessionPrivateAddrType_Object = MibTableColumn
natSessionPrivateAddrType = _NatSessionPrivateAddrType_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 10),
    _NatSessionPrivateAddrType_Type()
)
natSessionPrivateAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natSessionPrivateAddrType.setStatus("deprecated")
_NatSessionPrivateSrcAddr_Type = InetAddress
_NatSessionPrivateSrcAddr_Object = MibTableColumn
natSessionPrivateSrcAddr = _NatSessionPrivateSrcAddr_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 11),
    _NatSessionPrivateSrcAddr_Type()
)
natSessionPrivateSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natSessionPrivateSrcAddr.setStatus("deprecated")
_NatSessionPrivateSrcPort_Type = InetPortNumber
_NatSessionPrivateSrcPort_Object = MibTableColumn
natSessionPrivateSrcPort = _NatSessionPrivateSrcPort_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 12),
    _NatSessionPrivateSrcPort_Type()
)
natSessionPrivateSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natSessionPrivateSrcPort.setStatus("deprecated")
_NatSessionPrivateDstAddr_Type = InetAddress
_NatSessionPrivateDstAddr_Object = MibTableColumn
natSessionPrivateDstAddr = _NatSessionPrivateDstAddr_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 13),
    _NatSessionPrivateDstAddr_Type()
)
natSessionPrivateDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natSessionPrivateDstAddr.setStatus("deprecated")
_NatSessionPrivateDstPort_Type = InetPortNumber
_NatSessionPrivateDstPort_Object = MibTableColumn
natSessionPrivateDstPort = _NatSessionPrivateDstPort_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 14),
    _NatSessionPrivateDstPort_Type()
)
natSessionPrivateDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natSessionPrivateDstPort.setStatus("deprecated")
_NatSessionPublicAddrType_Type = InetAddressType
_NatSessionPublicAddrType_Object = MibTableColumn
natSessionPublicAddrType = _NatSessionPublicAddrType_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 15),
    _NatSessionPublicAddrType_Type()
)
natSessionPublicAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natSessionPublicAddrType.setStatus("deprecated")
_NatSessionPublicSrcAddr_Type = InetAddress
_NatSessionPublicSrcAddr_Object = MibTableColumn
natSessionPublicSrcAddr = _NatSessionPublicSrcAddr_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 16),
    _NatSessionPublicSrcAddr_Type()
)
natSessionPublicSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natSessionPublicSrcAddr.setStatus("deprecated")
_NatSessionPublicSrcPort_Type = InetPortNumber
_NatSessionPublicSrcPort_Object = MibTableColumn
natSessionPublicSrcPort = _NatSessionPublicSrcPort_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 17),
    _NatSessionPublicSrcPort_Type()
)
natSessionPublicSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natSessionPublicSrcPort.setStatus("deprecated")
_NatSessionPublicDstAddr_Type = InetAddress
_NatSessionPublicDstAddr_Object = MibTableColumn
natSessionPublicDstAddr = _NatSessionPublicDstAddr_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 18),
    _NatSessionPublicDstAddr_Type()
)
natSessionPublicDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natSessionPublicDstAddr.setStatus("deprecated")
_NatSessionPublicDstPort_Type = InetPortNumber
_NatSessionPublicDstPort_Object = MibTableColumn
natSessionPublicDstPort = _NatSessionPublicDstPort_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 19),
    _NatSessionPublicDstPort_Type()
)
natSessionPublicDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natSessionPublicDstPort.setStatus("deprecated")
_NatSessionMaxIdleTime_Type = TimeTicks
_NatSessionMaxIdleTime_Object = MibTableColumn
natSessionMaxIdleTime = _NatSessionMaxIdleTime_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 20),
    _NatSessionMaxIdleTime_Type()
)
natSessionMaxIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natSessionMaxIdleTime.setStatus("deprecated")
_NatSessionCurrentIdleTime_Type = TimeTicks
_NatSessionCurrentIdleTime_Object = MibTableColumn
natSessionCurrentIdleTime = _NatSessionCurrentIdleTime_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 21),
    _NatSessionCurrentIdleTime_Type()
)
natSessionCurrentIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natSessionCurrentIdleTime.setStatus("deprecated")
_NatSessionInTranslates_Type = Counter64
_NatSessionInTranslates_Object = MibTableColumn
natSessionInTranslates = _NatSessionInTranslates_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 22),
    _NatSessionInTranslates_Type()
)
natSessionInTranslates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natSessionInTranslates.setStatus("deprecated")
_NatSessionOutTranslates_Type = Counter64
_NatSessionOutTranslates_Object = MibTableColumn
natSessionOutTranslates = _NatSessionOutTranslates_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 9, 1, 23),
    _NatSessionOutTranslates_Type()
)
natSessionOutTranslates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natSessionOutTranslates.setStatus("deprecated")
_NatProtocolTable_Object = MibTable
natProtocolTable = _NatProtocolTable_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 10)
)
if mibBuilder.loadTexts:
    natProtocolTable.setStatus("deprecated")
_NatProtocolEntry_Object = MibTableRow
natProtocolEntry = _NatProtocolEntry_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 10, 1)
)
natProtocolEntry.setIndexNames(
    (0, "NAT-MIB", "natProtocol"),
)
if mibBuilder.loadTexts:
    natProtocolEntry.setStatus("deprecated")
_NatProtocol_Type = NatProtocolType
_NatProtocol_Object = MibTableColumn
natProtocol = _NatProtocol_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 10, 1, 1),
    _NatProtocol_Type()
)
natProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natProtocol.setStatus("deprecated")
_NatProtocolInTranslates_Type = Counter64
_NatProtocolInTranslates_Object = MibTableColumn
natProtocolInTranslates = _NatProtocolInTranslates_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 10, 1, 2),
    _NatProtocolInTranslates_Type()
)
natProtocolInTranslates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natProtocolInTranslates.setStatus("deprecated")
_NatProtocolOutTranslates_Type = Counter64
_NatProtocolOutTranslates_Object = MibTableColumn
natProtocolOutTranslates = _NatProtocolOutTranslates_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 10, 1, 3),
    _NatProtocolOutTranslates_Type()
)
natProtocolOutTranslates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natProtocolOutTranslates.setStatus("deprecated")
_NatProtocolDiscards_Type = Counter64
_NatProtocolDiscards_Object = MibTableColumn
natProtocolDiscards = _NatProtocolDiscards_Object(
    (1, 3, 6, 1, 2, 1, 123, 1, 10, 1, 4),
    _NatProtocolDiscards_Type()
)
natProtocolDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natProtocolDiscards.setStatus("deprecated")
_NatMIBConformance_ObjectIdentity = ObjectIdentity
natMIBConformance = _NatMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 123, 2)
)
_NatMIBGroups_ObjectIdentity = ObjectIdentity
natMIBGroups = _NatMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 123, 2, 1)
)
_NatMIBCompliances_ObjectIdentity = ObjectIdentity
natMIBCompliances = _NatMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 123, 2, 2)
)

# Managed Objects groups

natConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 123, 2, 1, 1)
)
natConfigGroup.setObjects(
      *(("NAT-MIB", "natInterfaceRealm"),
        ("NAT-MIB", "natInterfaceServiceType"),
        ("NAT-MIB", "natInterfaceStorageType"),
        ("NAT-MIB", "natInterfaceRowStatus"),
        ("NAT-MIB", "natAddrMapName"),
        ("NAT-MIB", "natAddrMapEntryType"),
        ("NAT-MIB", "natAddrMapTranslationEntity"),
        ("NAT-MIB", "natAddrMapLocalAddrType"),
        ("NAT-MIB", "natAddrMapLocalAddrFrom"),
        ("NAT-MIB", "natAddrMapLocalAddrTo"),
        ("NAT-MIB", "natAddrMapLocalPortFrom"),
        ("NAT-MIB", "natAddrMapLocalPortTo"),
        ("NAT-MIB", "natAddrMapGlobalAddrType"),
        ("NAT-MIB", "natAddrMapGlobalAddrFrom"),
        ("NAT-MIB", "natAddrMapGlobalAddrTo"),
        ("NAT-MIB", "natAddrMapGlobalPortFrom"),
        ("NAT-MIB", "natAddrMapGlobalPortTo"),
        ("NAT-MIB", "natAddrMapProtocol"),
        ("NAT-MIB", "natAddrMapStorageType"),
        ("NAT-MIB", "natAddrMapRowStatus"),
        ("NAT-MIB", "natBindDefIdleTimeout"),
        ("NAT-MIB", "natUdpDefIdleTimeout"),
        ("NAT-MIB", "natIcmpDefIdleTimeout"),
        ("NAT-MIB", "natOtherDefIdleTimeout"),
        ("NAT-MIB", "natTcpDefIdleTimeout"),
        ("NAT-MIB", "natTcpDefNegTimeout"),
        ("NAT-MIB", "natNotifThrottlingInterval"))
)
if mibBuilder.loadTexts:
    natConfigGroup.setStatus("deprecated")

natTranslationGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 123, 2, 1, 2)
)
natTranslationGroup.setObjects(
      *(("NAT-MIB", "natAddrBindNumberOfEntries"),
        ("NAT-MIB", "natAddrBindGlobalAddrType"),
        ("NAT-MIB", "natAddrBindGlobalAddr"),
        ("NAT-MIB", "natAddrBindId"),
        ("NAT-MIB", "natAddrBindTranslationEntity"),
        ("NAT-MIB", "natAddrBindType"),
        ("NAT-MIB", "natAddrBindMapIndex"),
        ("NAT-MIB", "natAddrBindSessions"),
        ("NAT-MIB", "natAddrBindMaxIdleTime"),
        ("NAT-MIB", "natAddrBindCurrentIdleTime"),
        ("NAT-MIB", "natAddrBindInTranslates"),
        ("NAT-MIB", "natAddrBindOutTranslates"),
        ("NAT-MIB", "natAddrPortBindNumberOfEntries"),
        ("NAT-MIB", "natAddrPortBindGlobalAddrType"),
        ("NAT-MIB", "natAddrPortBindGlobalAddr"),
        ("NAT-MIB", "natAddrPortBindGlobalPort"),
        ("NAT-MIB", "natAddrPortBindId"),
        ("NAT-MIB", "natAddrPortBindTranslationEntity"),
        ("NAT-MIB", "natAddrPortBindType"),
        ("NAT-MIB", "natAddrPortBindMapIndex"),
        ("NAT-MIB", "natAddrPortBindSessions"),
        ("NAT-MIB", "natAddrPortBindMaxIdleTime"),
        ("NAT-MIB", "natAddrPortBindCurrentIdleTime"),
        ("NAT-MIB", "natAddrPortBindInTranslates"),
        ("NAT-MIB", "natAddrPortBindOutTranslates"),
        ("NAT-MIB", "natSessionPrivateSrcEPBindId"),
        ("NAT-MIB", "natSessionPrivateSrcEPBindMode"),
        ("NAT-MIB", "natSessionPrivateDstEPBindId"),
        ("NAT-MIB", "natSessionPrivateDstEPBindMode"),
        ("NAT-MIB", "natSessionDirection"),
        ("NAT-MIB", "natSessionUpTime"),
        ("NAT-MIB", "natSessionAddrMapIndex"),
        ("NAT-MIB", "natSessionProtocolType"),
        ("NAT-MIB", "natSessionPrivateAddrType"),
        ("NAT-MIB", "natSessionPrivateSrcAddr"),
        ("NAT-MIB", "natSessionPrivateSrcPort"),
        ("NAT-MIB", "natSessionPrivateDstAddr"),
        ("NAT-MIB", "natSessionPrivateDstPort"),
        ("NAT-MIB", "natSessionPublicAddrType"),
        ("NAT-MIB", "natSessionPublicSrcAddr"),
        ("NAT-MIB", "natSessionPublicSrcPort"),
        ("NAT-MIB", "natSessionPublicDstAddr"),
        ("NAT-MIB", "natSessionPublicDstPort"),
        ("NAT-MIB", "natSessionMaxIdleTime"),
        ("NAT-MIB", "natSessionCurrentIdleTime"),
        ("NAT-MIB", "natSessionInTranslates"),
        ("NAT-MIB", "natSessionOutTranslates"))
)
if mibBuilder.loadTexts:
    natTranslationGroup.setStatus("deprecated")

natStatsInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 123, 2, 1, 3)
)
natStatsInterfaceGroup.setObjects(
      *(("NAT-MIB", "natInterfaceInTranslates"),
        ("NAT-MIB", "natInterfaceOutTranslates"),
        ("NAT-MIB", "natInterfaceDiscards"))
)
if mibBuilder.loadTexts:
    natStatsInterfaceGroup.setStatus("deprecated")

natStatsProtocolGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 123, 2, 1, 4)
)
natStatsProtocolGroup.setObjects(
      *(("NAT-MIB", "natProtocolInTranslates"),
        ("NAT-MIB", "natProtocolOutTranslates"),
        ("NAT-MIB", "natProtocolDiscards"))
)
if mibBuilder.loadTexts:
    natStatsProtocolGroup.setStatus("deprecated")

natStatsAddrMapGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 123, 2, 1, 5)
)
natStatsAddrMapGroup.setObjects(
      *(("NAT-MIB", "natAddrMapInTranslates"),
        ("NAT-MIB", "natAddrMapOutTranslates"),
        ("NAT-MIB", "natAddrMapDiscards"),
        ("NAT-MIB", "natAddrMapAddrUsed"))
)
if mibBuilder.loadTexts:
    natStatsAddrMapGroup.setStatus("deprecated")


# Notification objects

natPacketDiscard = NotificationType(
    (1, 3, 6, 1, 2, 1, 123, 0, 1)
)
natPacketDiscard.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    natPacketDiscard.setStatus(
        "deprecated"
    )


# Notifications groups

natMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 123, 2, 1, 6)
)
natMIBNotificationGroup.setObjects(
    ("NAT-MIB", "natPacketDiscard")
)
if mibBuilder.loadTexts:
    natMIBNotificationGroup.setStatus(
        "deprecated"
    )


# Agent capabilities


# Module compliance

natMIBFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 123, 2, 2, 1)
)
if mibBuilder.loadTexts:
    natMIBFullCompliance.setStatus(
        "deprecated"
    )

natMIBReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 123, 2, 2, 2)
)
if mibBuilder.loadTexts:
    natMIBReadOnlyCompliance.setStatus(
        "deprecated"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NAT-MIB",
    **{"NatProtocolType": NatProtocolType,
       "NatProtocolMap": NatProtocolMap,
       "NatAddrMapId": NatAddrMapId,
       "NatBindIdOrZero": NatBindIdOrZero,
       "NatBindId": NatBindId,
       "NatSessionId": NatSessionId,
       "NatBindMode": NatBindMode,
       "NatAssociationType": NatAssociationType,
       "NatTranslationEntity": NatTranslationEntity,
       "natMIB": natMIB,
       "natMIBNotifications": natMIBNotifications,
       "natPacketDiscard": natPacketDiscard,
       "natMIBObjects": natMIBObjects,
       "natDefTimeouts": natDefTimeouts,
       "natBindDefIdleTimeout": natBindDefIdleTimeout,
       "natUdpDefIdleTimeout": natUdpDefIdleTimeout,
       "natIcmpDefIdleTimeout": natIcmpDefIdleTimeout,
       "natOtherDefIdleTimeout": natOtherDefIdleTimeout,
       "natTcpDefIdleTimeout": natTcpDefIdleTimeout,
       "natTcpDefNegTimeout": natTcpDefNegTimeout,
       "natNotifCtrl": natNotifCtrl,
       "natNotifThrottlingInterval": natNotifThrottlingInterval,
       "natInterfaceTable": natInterfaceTable,
       "natInterfaceEntry": natInterfaceEntry,
       "natInterfaceRealm": natInterfaceRealm,
       "natInterfaceServiceType": natInterfaceServiceType,
       "natInterfaceInTranslates": natInterfaceInTranslates,
       "natInterfaceOutTranslates": natInterfaceOutTranslates,
       "natInterfaceDiscards": natInterfaceDiscards,
       "natInterfaceStorageType": natInterfaceStorageType,
       "natInterfaceRowStatus": natInterfaceRowStatus,
       "natAddrMapTable": natAddrMapTable,
       "natAddrMapEntry": natAddrMapEntry,
       "natAddrMapIndex": natAddrMapIndex,
       "natAddrMapName": natAddrMapName,
       "natAddrMapEntryType": natAddrMapEntryType,
       "natAddrMapTranslationEntity": natAddrMapTranslationEntity,
       "natAddrMapLocalAddrType": natAddrMapLocalAddrType,
       "natAddrMapLocalAddrFrom": natAddrMapLocalAddrFrom,
       "natAddrMapLocalAddrTo": natAddrMapLocalAddrTo,
       "natAddrMapLocalPortFrom": natAddrMapLocalPortFrom,
       "natAddrMapLocalPortTo": natAddrMapLocalPortTo,
       "natAddrMapGlobalAddrType": natAddrMapGlobalAddrType,
       "natAddrMapGlobalAddrFrom": natAddrMapGlobalAddrFrom,
       "natAddrMapGlobalAddrTo": natAddrMapGlobalAddrTo,
       "natAddrMapGlobalPortFrom": natAddrMapGlobalPortFrom,
       "natAddrMapGlobalPortTo": natAddrMapGlobalPortTo,
       "natAddrMapProtocol": natAddrMapProtocol,
       "natAddrMapInTranslates": natAddrMapInTranslates,
       "natAddrMapOutTranslates": natAddrMapOutTranslates,
       "natAddrMapDiscards": natAddrMapDiscards,
       "natAddrMapAddrUsed": natAddrMapAddrUsed,
       "natAddrMapStorageType": natAddrMapStorageType,
       "natAddrMapRowStatus": natAddrMapRowStatus,
       "natAddrBindNumberOfEntries": natAddrBindNumberOfEntries,
       "natAddrBindTable": natAddrBindTable,
       "natAddrBindEntry": natAddrBindEntry,
       "natAddrBindLocalAddrType": natAddrBindLocalAddrType,
       "natAddrBindLocalAddr": natAddrBindLocalAddr,
       "natAddrBindGlobalAddrType": natAddrBindGlobalAddrType,
       "natAddrBindGlobalAddr": natAddrBindGlobalAddr,
       "natAddrBindId": natAddrBindId,
       "natAddrBindTranslationEntity": natAddrBindTranslationEntity,
       "natAddrBindType": natAddrBindType,
       "natAddrBindMapIndex": natAddrBindMapIndex,
       "natAddrBindSessions": natAddrBindSessions,
       "natAddrBindMaxIdleTime": natAddrBindMaxIdleTime,
       "natAddrBindCurrentIdleTime": natAddrBindCurrentIdleTime,
       "natAddrBindInTranslates": natAddrBindInTranslates,
       "natAddrBindOutTranslates": natAddrBindOutTranslates,
       "natAddrPortBindNumberOfEntries": natAddrPortBindNumberOfEntries,
       "natAddrPortBindTable": natAddrPortBindTable,
       "natAddrPortBindEntry": natAddrPortBindEntry,
       "natAddrPortBindLocalAddrType": natAddrPortBindLocalAddrType,
       "natAddrPortBindLocalAddr": natAddrPortBindLocalAddr,
       "natAddrPortBindLocalPort": natAddrPortBindLocalPort,
       "natAddrPortBindProtocol": natAddrPortBindProtocol,
       "natAddrPortBindGlobalAddrType": natAddrPortBindGlobalAddrType,
       "natAddrPortBindGlobalAddr": natAddrPortBindGlobalAddr,
       "natAddrPortBindGlobalPort": natAddrPortBindGlobalPort,
       "natAddrPortBindId": natAddrPortBindId,
       "natAddrPortBindTranslationEntity": natAddrPortBindTranslationEntity,
       "natAddrPortBindType": natAddrPortBindType,
       "natAddrPortBindMapIndex": natAddrPortBindMapIndex,
       "natAddrPortBindSessions": natAddrPortBindSessions,
       "natAddrPortBindMaxIdleTime": natAddrPortBindMaxIdleTime,
       "natAddrPortBindCurrentIdleTime": natAddrPortBindCurrentIdleTime,
       "natAddrPortBindInTranslates": natAddrPortBindInTranslates,
       "natAddrPortBindOutTranslates": natAddrPortBindOutTranslates,
       "natSessionTable": natSessionTable,
       "natSessionEntry": natSessionEntry,
       "natSessionIndex": natSessionIndex,
       "natSessionPrivateSrcEPBindId": natSessionPrivateSrcEPBindId,
       "natSessionPrivateSrcEPBindMode": natSessionPrivateSrcEPBindMode,
       "natSessionPrivateDstEPBindId": natSessionPrivateDstEPBindId,
       "natSessionPrivateDstEPBindMode": natSessionPrivateDstEPBindMode,
       "natSessionDirection": natSessionDirection,
       "natSessionUpTime": natSessionUpTime,
       "natSessionAddrMapIndex": natSessionAddrMapIndex,
       "natSessionProtocolType": natSessionProtocolType,
       "natSessionPrivateAddrType": natSessionPrivateAddrType,
       "natSessionPrivateSrcAddr": natSessionPrivateSrcAddr,
       "natSessionPrivateSrcPort": natSessionPrivateSrcPort,
       "natSessionPrivateDstAddr": natSessionPrivateDstAddr,
       "natSessionPrivateDstPort": natSessionPrivateDstPort,
       "natSessionPublicAddrType": natSessionPublicAddrType,
       "natSessionPublicSrcAddr": natSessionPublicSrcAddr,
       "natSessionPublicSrcPort": natSessionPublicSrcPort,
       "natSessionPublicDstAddr": natSessionPublicDstAddr,
       "natSessionPublicDstPort": natSessionPublicDstPort,
       "natSessionMaxIdleTime": natSessionMaxIdleTime,
       "natSessionCurrentIdleTime": natSessionCurrentIdleTime,
       "natSessionInTranslates": natSessionInTranslates,
       "natSessionOutTranslates": natSessionOutTranslates,
       "natProtocolTable": natProtocolTable,
       "natProtocolEntry": natProtocolEntry,
       "natProtocol": natProtocol,
       "natProtocolInTranslates": natProtocolInTranslates,
       "natProtocolOutTranslates": natProtocolOutTranslates,
       "natProtocolDiscards": natProtocolDiscards,
       "natMIBConformance": natMIBConformance,
       "natMIBGroups": natMIBGroups,
       "natConfigGroup": natConfigGroup,
       "natTranslationGroup": natTranslationGroup,
       "natStatsInterfaceGroup": natStatsInterfaceGroup,
       "natStatsProtocolGroup": natStatsProtocolGroup,
       "natStatsAddrMapGroup": natStatsAddrMapGroup,
       "natMIBNotificationGroup": natMIBNotificationGroup,
       "natMIBCompliances": natMIBCompliances,
       "natMIBFullCompliance": natMIBFullCompliance,
       "natMIBReadOnlyCompliance": natMIBReadOnlyCompliance}
)
