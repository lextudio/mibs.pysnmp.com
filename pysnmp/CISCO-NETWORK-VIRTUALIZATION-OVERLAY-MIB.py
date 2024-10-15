# SNMP MIB module (CISCO-NETWORK-VIRTUALIZATION-OVERLAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-NETWORK-VIRTUALIZATION-OVERLAY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:06:13 2024
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

(VlanIndexOrZero,) = mibBuilder.importSymbols(
    "CISCO-PRIVATE-VLAN-MIB",
    "VlanIndexOrZero")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

ciscoNetworkVirtualizationOverlayMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 820)
)
ciscoNetworkVirtualizationOverlayMIB.setRevisions(
        ("2015-01-26 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CnvoMIBNotifs_ObjectIdentity = ObjectIdentity
cnvoMIBNotifs = _CnvoMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 0)
)
_CnvoMIBObjects_ObjectIdentity = ObjectIdentity
cnvoMIBObjects = _CnvoMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 1)
)
_CnvoNvoObjects_ObjectIdentity = ObjectIdentity
cnvoNvoObjects = _CnvoNvoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 1, 1)
)
_CnvoNvoTable_Object = MibTable
cnvoNvoTable = _CnvoNvoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cnvoNvoTable.setStatus("current")
_CnvoNvoEntry_Object = MibTableRow
cnvoNvoEntry = _CnvoNvoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 1, 1, 1, 1)
)
cnvoNvoEntry.setIndexNames(
    (0, "CISCO-NETWORK-VIRTUALIZATION-OVERLAY-MIB", "cnvoNvoInstanceId"),
)
if mibBuilder.loadTexts:
    cnvoNvoEntry.setStatus("current")
_CnvoNvoInstanceId_Type = Unsigned32
_CnvoNvoInstanceId_Object = MibTableColumn
cnvoNvoInstanceId = _CnvoNvoInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 1, 1, 1, 1, 1),
    _CnvoNvoInstanceId_Type()
)
cnvoNvoInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnvoNvoInstanceId.setStatus("current")


class _CnvoNvoEncapType_Type(Integer32):
    """Custom type cnvoNvoEncapType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nvgre", 3),
          ("unknown", 1),
          ("vxlan", 2))
    )


_CnvoNvoEncapType_Type.__name__ = "Integer32"
_CnvoNvoEncapType_Object = MibTableColumn
cnvoNvoEncapType = _CnvoNvoEncapType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 1, 1, 1, 1, 2),
    _CnvoNvoEncapType_Type()
)
cnvoNvoEncapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnvoNvoEncapType.setStatus("current")


class _CnvoNvoSourceInterface_Type(InterfaceIndexOrZero):
    """Custom type cnvoNvoSourceInterface based on InterfaceIndexOrZero"""
    defaultValue = 0


_CnvoNvoSourceInterface_Object = MibTableColumn
cnvoNvoSourceInterface = _CnvoNvoSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 1, 1, 1, 1, 3),
    _CnvoNvoSourceInterface_Type()
)
cnvoNvoSourceInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnvoNvoSourceInterface.setStatus("current")
_CnvoNvoConfiguredVni_Type = SnmpAdminString
_CnvoNvoConfiguredVni_Object = MibTableColumn
cnvoNvoConfiguredVni = _CnvoNvoConfiguredVni_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 1, 1, 1, 1, 4),
    _CnvoNvoConfiguredVni_Type()
)
cnvoNvoConfiguredVni.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnvoNvoConfiguredVni.setStatus("current")


class _CnvoNvoStorageType_Type(StorageType):
    """Custom type cnvoNvoStorageType based on StorageType"""


_CnvoNvoStorageType_Object = MibTableColumn
cnvoNvoStorageType = _CnvoNvoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 1, 1, 1, 1, 5),
    _CnvoNvoStorageType_Type()
)
cnvoNvoStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnvoNvoStorageType.setStatus("current")
_CnvoNvoRowStatus_Type = RowStatus
_CnvoNvoRowStatus_Object = MibTableColumn
cnvoNvoRowStatus = _CnvoNvoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 1, 1, 1, 1, 6),
    _CnvoNvoRowStatus_Type()
)
cnvoNvoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnvoNvoRowStatus.setStatus("current")
_CnvoVNetTable_Object = MibTable
cnvoVNetTable = _CnvoVNetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cnvoVNetTable.setStatus("current")
_CnvoVNetEntry_Object = MibTableRow
cnvoVNetEntry = _CnvoVNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 1, 1, 2, 1)
)
cnvoVNetEntry.setIndexNames(
    (0, "CISCO-NETWORK-VIRTUALIZATION-OVERLAY-MIB", "cnvoNvoInstanceId"),
    (0, "CISCO-NETWORK-VIRTUALIZATION-OVERLAY-MIB", "cnvoVNetLocalVNetId"),
)
if mibBuilder.loadTexts:
    cnvoVNetEntry.setStatus("current")
_CnvoVNetLocalVNetId_Type = Unsigned32
_CnvoVNetLocalVNetId_Object = MibTableColumn
cnvoVNetLocalVNetId = _CnvoVNetLocalVNetId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 1, 1, 2, 1, 1),
    _CnvoVNetLocalVNetId_Type()
)
cnvoVNetLocalVNetId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnvoVNetLocalVNetId.setStatus("current")
_CnvoVNetIpMcastAddrType_Type = InetAddressType
_CnvoVNetIpMcastAddrType_Object = MibTableColumn
cnvoVNetIpMcastAddrType = _CnvoVNetIpMcastAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 1, 1, 2, 1, 2),
    _CnvoVNetIpMcastAddrType_Type()
)
cnvoVNetIpMcastAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnvoVNetIpMcastAddrType.setStatus("current")
_CnvoVNetIpMcastAddr_Type = InetAddress
_CnvoVNetIpMcastAddr_Object = MibTableColumn
cnvoVNetIpMcastAddr = _CnvoVNetIpMcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 1, 1, 2, 1, 3),
    _CnvoVNetIpMcastAddr_Type()
)
cnvoVNetIpMcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnvoVNetIpMcastAddr.setStatus("current")
_CnvoVNetVlan_Type = VlanIndexOrZero
_CnvoVNetVlan_Object = MibTableColumn
cnvoVNetVlan = _CnvoVNetVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 1, 1, 2, 1, 4),
    _CnvoVNetVlan_Type()
)
cnvoVNetVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnvoVNetVlan.setStatus("current")


class _CnvoVNetArpSuppression_Type(Integer32):
    """Custom type cnvoVNetArpSuppression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("arpSupOFF", 2),
          ("arpSupON", 1))
    )


_CnvoVNetArpSuppression_Type.__name__ = "Integer32"
_CnvoVNetArpSuppression_Object = MibTableColumn
cnvoVNetArpSuppression = _CnvoVNetArpSuppression_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 1, 1, 2, 1, 5),
    _CnvoVNetArpSuppression_Type()
)
cnvoVNetArpSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnvoVNetArpSuppression.setStatus("current")


class _CnvoVNetReplication_Type(Integer32):
    """Custom type cnvoVNetReplication based on Integer32"""
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
        *(("mcast", 1),
          ("ucastBgp", 3),
          ("ucastStatic", 4),
          ("unconf", 2))
    )


_CnvoVNetReplication_Type.__name__ = "Integer32"
_CnvoVNetReplication_Object = MibTableColumn
cnvoVNetReplication = _CnvoVNetReplication_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 1, 1, 2, 1, 6),
    _CnvoVNetReplication_Type()
)
cnvoVNetReplication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnvoVNetReplication.setStatus("current")


class _CnvoVNetHostReachability_Type(Integer32):
    """Custom type cnvoVNetHostReachability based on Integer32"""
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
        *(("controlPlaneL3", 4),
          ("dataPlaneL2", 3),
          ("hostReachabilityUnconf", 2),
          ("unknown", 1))
    )


_CnvoVNetHostReachability_Type.__name__ = "Integer32"
_CnvoVNetHostReachability_Object = MibTableColumn
cnvoVNetHostReachability = _CnvoVNetHostReachability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 1, 1, 2, 1, 7),
    _CnvoVNetHostReachability_Type()
)
cnvoVNetHostReachability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnvoVNetHostReachability.setStatus("current")


class _CnvoVNetVniType_Type(Integer32):
    """Custom type cnvoVNetVniType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("l2", 2),
          ("l3", 3),
          ("unknown", 1))
    )


_CnvoVNetVniType_Type.__name__ = "Integer32"
_CnvoVNetVniType_Object = MibTableColumn
cnvoVNetVniType = _CnvoVNetVniType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 1, 1, 2, 1, 8),
    _CnvoVNetVniType_Type()
)
cnvoVNetVniType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnvoVNetVniType.setStatus("current")
_CnvoVNetIpVrfOrBridgeDomainName_Type = SnmpAdminString
_CnvoVNetIpVrfOrBridgeDomainName_Object = MibTableColumn
cnvoVNetIpVrfOrBridgeDomainName = _CnvoVNetIpVrfOrBridgeDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 1, 1, 2, 1, 9),
    _CnvoVNetIpVrfOrBridgeDomainName_Type()
)
cnvoVNetIpVrfOrBridgeDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnvoVNetIpVrfOrBridgeDomainName.setStatus("current")
_CnvoVNetRouterMacAddr_Type = InetAddress
_CnvoVNetRouterMacAddr_Object = MibTableColumn
cnvoVNetRouterMacAddr = _CnvoVNetRouterMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 1, 1, 2, 1, 10),
    _CnvoVNetRouterMacAddr_Type()
)
cnvoVNetRouterMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnvoVNetRouterMacAddr.setStatus("current")
_CnvoPeerTable_Object = MibTable
cnvoPeerTable = _CnvoPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cnvoPeerTable.setStatus("current")
_CnvoPeerEntry_Object = MibTableRow
cnvoPeerEntry = _CnvoPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 1, 1, 3, 1)
)
cnvoPeerEntry.setIndexNames(
    (0, "CISCO-NETWORK-VIRTUALIZATION-OVERLAY-MIB", "cnvoNvoInstanceId"),
    (0, "CISCO-NETWORK-VIRTUALIZATION-OVERLAY-MIB", "cnvoPeerIpAddrType"),
    (0, "CISCO-NETWORK-VIRTUALIZATION-OVERLAY-MIB", "cnvoPeerIpAddr"),
)
if mibBuilder.loadTexts:
    cnvoPeerEntry.setStatus("current")
_CnvoPeerIpAddrType_Type = InetAddressType
_CnvoPeerIpAddrType_Object = MibTableColumn
cnvoPeerIpAddrType = _CnvoPeerIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 1, 1, 3, 1, 1),
    _CnvoPeerIpAddrType_Type()
)
cnvoPeerIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnvoPeerIpAddrType.setStatus("current")


class _CnvoPeerIpAddr_Type(InetAddress):
    """Custom type cnvoPeerIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CnvoPeerIpAddr_Type.__name__ = "InetAddress"
_CnvoPeerIpAddr_Object = MibTableColumn
cnvoPeerIpAddr = _CnvoPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 1, 1, 3, 1, 2),
    _CnvoPeerIpAddr_Type()
)
cnvoPeerIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnvoPeerIpAddr.setStatus("current")
_CnvoPeerUpTime_Type = DateAndTime
_CnvoPeerUpTime_Object = MibTableColumn
cnvoPeerUpTime = _CnvoPeerUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 1, 1, 3, 1, 3),
    _CnvoPeerUpTime_Type()
)
cnvoPeerUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnvoPeerUpTime.setStatus("current")


class _CnvoPeerLearningSourceType_Type(Integer32):
    """Custom type cnvoPeerLearningSourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("controlPlane", 3),
          ("dataPlane", 2),
          ("unknown", 1))
    )


_CnvoPeerLearningSourceType_Type.__name__ = "Integer32"
_CnvoPeerLearningSourceType_Object = MibTableColumn
cnvoPeerLearningSourceType = _CnvoPeerLearningSourceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 1, 1, 3, 1, 4),
    _CnvoPeerLearningSourceType_Type()
)
cnvoPeerLearningSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnvoPeerLearningSourceType.setStatus("current")
_CnvoVNetStatsTable_Object = MibTable
cnvoVNetStatsTable = _CnvoVNetStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cnvoVNetStatsTable.setStatus("current")
_CnvoVNetStatsEntry_Object = MibTableRow
cnvoVNetStatsEntry = _CnvoVNetStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 1, 1, 4, 1)
)
cnvoVNetStatsEntry.setIndexNames(
    (0, "CISCO-NETWORK-VIRTUALIZATION-OVERLAY-MIB", "cnvoNvoInstanceId"),
    (0, "CISCO-NETWORK-VIRTUALIZATION-OVERLAY-MIB", "cnvoVNetLocalVNetId"),
)
if mibBuilder.loadTexts:
    cnvoVNetStatsEntry.setStatus("current")
_CnvoVNetOutUnicastPackets_Type = Counter64
_CnvoVNetOutUnicastPackets_Object = MibTableColumn
cnvoVNetOutUnicastPackets = _CnvoVNetOutUnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 1, 1, 4, 1, 1),
    _CnvoVNetOutUnicastPackets_Type()
)
cnvoVNetOutUnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnvoVNetOutUnicastPackets.setStatus("current")
_CnvoVNetOutUnicastBytes_Type = Counter64
_CnvoVNetOutUnicastBytes_Object = MibTableColumn
cnvoVNetOutUnicastBytes = _CnvoVNetOutUnicastBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 1, 1, 4, 1, 2),
    _CnvoVNetOutUnicastBytes_Type()
)
cnvoVNetOutUnicastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnvoVNetOutUnicastBytes.setStatus("current")
_CnvoVNetOutMulticastPackets_Type = Counter64
_CnvoVNetOutMulticastPackets_Object = MibTableColumn
cnvoVNetOutMulticastPackets = _CnvoVNetOutMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 1, 1, 4, 1, 3),
    _CnvoVNetOutMulticastPackets_Type()
)
cnvoVNetOutMulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnvoVNetOutMulticastPackets.setStatus("current")
_CnvoVNetOutMulticastBytes_Type = Counter64
_CnvoVNetOutMulticastBytes_Object = MibTableColumn
cnvoVNetOutMulticastBytes = _CnvoVNetOutMulticastBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 1, 1, 4, 1, 4),
    _CnvoVNetOutMulticastBytes_Type()
)
cnvoVNetOutMulticastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnvoVNetOutMulticastBytes.setStatus("current")
_CnvoVNetInUnicastPackets_Type = Counter64
_CnvoVNetInUnicastPackets_Object = MibTableColumn
cnvoVNetInUnicastPackets = _CnvoVNetInUnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 1, 1, 4, 1, 5),
    _CnvoVNetInUnicastPackets_Type()
)
cnvoVNetInUnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnvoVNetInUnicastPackets.setStatus("current")
_CnvoVNetInUnicastBytes_Type = Counter64
_CnvoVNetInUnicastBytes_Object = MibTableColumn
cnvoVNetInUnicastBytes = _CnvoVNetInUnicastBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 1, 1, 4, 1, 6),
    _CnvoVNetInUnicastBytes_Type()
)
cnvoVNetInUnicastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnvoVNetInUnicastBytes.setStatus("current")
_CnvoVNetInMulticastPackets_Type = Counter64
_CnvoVNetInMulticastPackets_Object = MibTableColumn
cnvoVNetInMulticastPackets = _CnvoVNetInMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 1, 1, 4, 1, 7),
    _CnvoVNetInMulticastPackets_Type()
)
cnvoVNetInMulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnvoVNetInMulticastPackets.setStatus("current")
_CnvoVNetInMulticastBytes_Type = Counter64
_CnvoVNetInMulticastBytes_Object = MibTableColumn
cnvoVNetInMulticastBytes = _CnvoVNetInMulticastBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 1, 1, 4, 1, 8),
    _CnvoVNetInMulticastBytes_Type()
)
cnvoVNetInMulticastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnvoVNetInMulticastBytes.setStatus("current")
_CnvoNvoPeerStatsTable_Object = MibTable
cnvoNvoPeerStatsTable = _CnvoNvoPeerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cnvoNvoPeerStatsTable.setStatus("current")
_CnvoNvoPeerStatsEntry_Object = MibTableRow
cnvoNvoPeerStatsEntry = _CnvoNvoPeerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 1, 1, 5, 1)
)
cnvoNvoPeerStatsEntry.setIndexNames(
    (0, "CISCO-NETWORK-VIRTUALIZATION-OVERLAY-MIB", "cnvoNvoInstanceId"),
    (0, "CISCO-NETWORK-VIRTUALIZATION-OVERLAY-MIB", "cnvoPeerIpAddrType"),
    (0, "CISCO-NETWORK-VIRTUALIZATION-OVERLAY-MIB", "cnvoPeerIpAddr"),
)
if mibBuilder.loadTexts:
    cnvoNvoPeerStatsEntry.setStatus("current")
_CnvoNvoPeerOutUnicastPackets_Type = Counter64
_CnvoNvoPeerOutUnicastPackets_Object = MibTableColumn
cnvoNvoPeerOutUnicastPackets = _CnvoNvoPeerOutUnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 1, 1, 5, 1, 1),
    _CnvoNvoPeerOutUnicastPackets_Type()
)
cnvoNvoPeerOutUnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnvoNvoPeerOutUnicastPackets.setStatus("current")
_CnvoNvoPeerOutUnicastBytes_Type = Counter64
_CnvoNvoPeerOutUnicastBytes_Object = MibTableColumn
cnvoNvoPeerOutUnicastBytes = _CnvoNvoPeerOutUnicastBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 1, 1, 5, 1, 2),
    _CnvoNvoPeerOutUnicastBytes_Type()
)
cnvoNvoPeerOutUnicastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnvoNvoPeerOutUnicastBytes.setStatus("current")
_CnvoNvoPeerOutMulticastPackets_Type = Counter64
_CnvoNvoPeerOutMulticastPackets_Object = MibTableColumn
cnvoNvoPeerOutMulticastPackets = _CnvoNvoPeerOutMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 1, 1, 5, 1, 3),
    _CnvoNvoPeerOutMulticastPackets_Type()
)
cnvoNvoPeerOutMulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnvoNvoPeerOutMulticastPackets.setStatus("current")
_CnvoNvoPeerOutMulticastBytes_Type = Counter64
_CnvoNvoPeerOutMulticastBytes_Object = MibTableColumn
cnvoNvoPeerOutMulticastBytes = _CnvoNvoPeerOutMulticastBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 1, 1, 5, 1, 4),
    _CnvoNvoPeerOutMulticastBytes_Type()
)
cnvoNvoPeerOutMulticastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnvoNvoPeerOutMulticastBytes.setStatus("current")
_CnvoNvoPeerInUnicastPackets_Type = Counter64
_CnvoNvoPeerInUnicastPackets_Object = MibTableColumn
cnvoNvoPeerInUnicastPackets = _CnvoNvoPeerInUnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 1, 1, 5, 1, 5),
    _CnvoNvoPeerInUnicastPackets_Type()
)
cnvoNvoPeerInUnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnvoNvoPeerInUnicastPackets.setStatus("current")
_CnvoNvoPeerInUnicastBytes_Type = Counter64
_CnvoNvoPeerInUnicastBytes_Object = MibTableColumn
cnvoNvoPeerInUnicastBytes = _CnvoNvoPeerInUnicastBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 1, 1, 5, 1, 6),
    _CnvoNvoPeerInUnicastBytes_Type()
)
cnvoNvoPeerInUnicastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnvoNvoPeerInUnicastBytes.setStatus("current")
_CnvoNvoPeerInMulticastPackets_Type = Counter64
_CnvoNvoPeerInMulticastPackets_Object = MibTableColumn
cnvoNvoPeerInMulticastPackets = _CnvoNvoPeerInMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 1, 1, 5, 1, 7),
    _CnvoNvoPeerInMulticastPackets_Type()
)
cnvoNvoPeerInMulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnvoNvoPeerInMulticastPackets.setStatus("current")
_CnvoNvoPeerInMulticastBytes_Type = Counter64
_CnvoNvoPeerInMulticastBytes_Object = MibTableColumn
cnvoNvoPeerInMulticastBytes = _CnvoNvoPeerInMulticastBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 1, 1, 5, 1, 8),
    _CnvoNvoPeerInMulticastBytes_Type()
)
cnvoNvoPeerInMulticastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnvoNvoPeerInMulticastBytes.setStatus("current")
_CnvoMIBConform_ObjectIdentity = ObjectIdentity
cnvoMIBConform = _CnvoMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 2)
)
_CnvoMIBCompliances_ObjectIdentity = ObjectIdentity
cnvoMIBCompliances = _CnvoMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 2, 1)
)
_CnvoMIBGroups_ObjectIdentity = ObjectIdentity
cnvoMIBGroups = _CnvoMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 2, 2)
)

# Managed Objects groups

cnvoNvoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 2, 2, 1)
)
cnvoNvoGroup.setObjects(
      *(("CISCO-NETWORK-VIRTUALIZATION-OVERLAY-MIB", "cnvoNvoEncapType"),
        ("CISCO-NETWORK-VIRTUALIZATION-OVERLAY-MIB", "cnvoNvoSourceInterface"),
        ("CISCO-NETWORK-VIRTUALIZATION-OVERLAY-MIB", "cnvoNvoConfiguredVni"),
        ("CISCO-NETWORK-VIRTUALIZATION-OVERLAY-MIB", "cnvoNvoStorageType"),
        ("CISCO-NETWORK-VIRTUALIZATION-OVERLAY-MIB", "cnvoNvoRowStatus"))
)
if mibBuilder.loadTexts:
    cnvoNvoGroup.setStatus("current")

cnvoVirtualNetworkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 2, 2, 2)
)
cnvoVirtualNetworkGroup.setObjects(
      *(("CISCO-NETWORK-VIRTUALIZATION-OVERLAY-MIB", "cnvoVNetIpMcastAddrType"),
        ("CISCO-NETWORK-VIRTUALIZATION-OVERLAY-MIB", "cnvoVNetIpMcastAddr"),
        ("CISCO-NETWORK-VIRTUALIZATION-OVERLAY-MIB", "cnvoVNetVlan"),
        ("CISCO-NETWORK-VIRTUALIZATION-OVERLAY-MIB", "cnvoVNetArpSuppression"),
        ("CISCO-NETWORK-VIRTUALIZATION-OVERLAY-MIB", "cnvoVNetReplication"),
        ("CISCO-NETWORK-VIRTUALIZATION-OVERLAY-MIB", "cnvoVNetHostReachability"),
        ("CISCO-NETWORK-VIRTUALIZATION-OVERLAY-MIB", "cnvoVNetVniType"),
        ("CISCO-NETWORK-VIRTUALIZATION-OVERLAY-MIB", "cnvoVNetIpVrfOrBridgeDomainName"),
        ("CISCO-NETWORK-VIRTUALIZATION-OVERLAY-MIB", "cnvoVNetRouterMacAddr"))
)
if mibBuilder.loadTexts:
    cnvoVirtualNetworkGroup.setStatus("current")

cnvoPeerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 2, 2, 3)
)
cnvoPeerGroup.setObjects(
      *(("CISCO-NETWORK-VIRTUALIZATION-OVERLAY-MIB", "cnvoPeerUpTime"),
        ("CISCO-NETWORK-VIRTUALIZATION-OVERLAY-MIB", "cnvoPeerLearningSourceType"))
)
if mibBuilder.loadTexts:
    cnvoPeerGroup.setStatus("current")

cnvoVirtualNetworkStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 2, 2, 4)
)
cnvoVirtualNetworkStatsGroup.setObjects(
      *(("CISCO-NETWORK-VIRTUALIZATION-OVERLAY-MIB", "cnvoVNetOutUnicastPackets"),
        ("CISCO-NETWORK-VIRTUALIZATION-OVERLAY-MIB", "cnvoVNetOutUnicastBytes"),
        ("CISCO-NETWORK-VIRTUALIZATION-OVERLAY-MIB", "cnvoVNetOutMulticastPackets"),
        ("CISCO-NETWORK-VIRTUALIZATION-OVERLAY-MIB", "cnvoVNetOutMulticastBytes"),
        ("CISCO-NETWORK-VIRTUALIZATION-OVERLAY-MIB", "cnvoVNetInUnicastPackets"),
        ("CISCO-NETWORK-VIRTUALIZATION-OVERLAY-MIB", "cnvoVNetInUnicastBytes"),
        ("CISCO-NETWORK-VIRTUALIZATION-OVERLAY-MIB", "cnvoVNetInMulticastPackets"),
        ("CISCO-NETWORK-VIRTUALIZATION-OVERLAY-MIB", "cnvoVNetInMulticastBytes"))
)
if mibBuilder.loadTexts:
    cnvoVirtualNetworkStatsGroup.setStatus("current")

cnvoNvoPerPeerOutUnicastStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 2, 2, 5)
)
cnvoNvoPerPeerOutUnicastStatsGroup.setObjects(
      *(("CISCO-NETWORK-VIRTUALIZATION-OVERLAY-MIB", "cnvoNvoPeerOutUnicastPackets"),
        ("CISCO-NETWORK-VIRTUALIZATION-OVERLAY-MIB", "cnvoNvoPeerOutUnicastBytes"))
)
if mibBuilder.loadTexts:
    cnvoNvoPerPeerOutUnicastStatsGroup.setStatus("current")

cnvoNvoPerPeerInUnicastStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 2, 2, 6)
)
cnvoNvoPerPeerInUnicastStatsGroup.setObjects(
      *(("CISCO-NETWORK-VIRTUALIZATION-OVERLAY-MIB", "cnvoNvoPeerInUnicastPackets"),
        ("CISCO-NETWORK-VIRTUALIZATION-OVERLAY-MIB", "cnvoNvoPeerInUnicastBytes"))
)
if mibBuilder.loadTexts:
    cnvoNvoPerPeerInUnicastStatsGroup.setStatus("current")

cnvoNvoPerPeerInMulticastStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 2, 2, 7)
)
cnvoNvoPerPeerInMulticastStatsGroup.setObjects(
      *(("CISCO-NETWORK-VIRTUALIZATION-OVERLAY-MIB", "cnvoNvoPeerInMulticastPackets"),
        ("CISCO-NETWORK-VIRTUALIZATION-OVERLAY-MIB", "cnvoNvoPeerInMulticastBytes"))
)
if mibBuilder.loadTexts:
    cnvoNvoPerPeerInMulticastStatsGroup.setStatus("current")

cnvoNvoPerPeerOutMulticastStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 2, 2, 8)
)
cnvoNvoPerPeerOutMulticastStatsGroup.setObjects(
      *(("CISCO-NETWORK-VIRTUALIZATION-OVERLAY-MIB", "cnvoNvoPeerOutMulticastPackets"),
        ("CISCO-NETWORK-VIRTUALIZATION-OVERLAY-MIB", "cnvoNvoPeerOutMulticastBytes"))
)
if mibBuilder.loadTexts:
    cnvoNvoPerPeerOutMulticastStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cnvoMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 820, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cnvoMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-NETWORK-VIRTUALIZATION-OVERLAY-MIB",
    **{"ciscoNetworkVirtualizationOverlayMIB": ciscoNetworkVirtualizationOverlayMIB,
       "cnvoMIBNotifs": cnvoMIBNotifs,
       "cnvoMIBObjects": cnvoMIBObjects,
       "cnvoNvoObjects": cnvoNvoObjects,
       "cnvoNvoTable": cnvoNvoTable,
       "cnvoNvoEntry": cnvoNvoEntry,
       "cnvoNvoInstanceId": cnvoNvoInstanceId,
       "cnvoNvoEncapType": cnvoNvoEncapType,
       "cnvoNvoSourceInterface": cnvoNvoSourceInterface,
       "cnvoNvoConfiguredVni": cnvoNvoConfiguredVni,
       "cnvoNvoStorageType": cnvoNvoStorageType,
       "cnvoNvoRowStatus": cnvoNvoRowStatus,
       "cnvoVNetTable": cnvoVNetTable,
       "cnvoVNetEntry": cnvoVNetEntry,
       "cnvoVNetLocalVNetId": cnvoVNetLocalVNetId,
       "cnvoVNetIpMcastAddrType": cnvoVNetIpMcastAddrType,
       "cnvoVNetIpMcastAddr": cnvoVNetIpMcastAddr,
       "cnvoVNetVlan": cnvoVNetVlan,
       "cnvoVNetArpSuppression": cnvoVNetArpSuppression,
       "cnvoVNetReplication": cnvoVNetReplication,
       "cnvoVNetHostReachability": cnvoVNetHostReachability,
       "cnvoVNetVniType": cnvoVNetVniType,
       "cnvoVNetIpVrfOrBridgeDomainName": cnvoVNetIpVrfOrBridgeDomainName,
       "cnvoVNetRouterMacAddr": cnvoVNetRouterMacAddr,
       "cnvoPeerTable": cnvoPeerTable,
       "cnvoPeerEntry": cnvoPeerEntry,
       "cnvoPeerIpAddrType": cnvoPeerIpAddrType,
       "cnvoPeerIpAddr": cnvoPeerIpAddr,
       "cnvoPeerUpTime": cnvoPeerUpTime,
       "cnvoPeerLearningSourceType": cnvoPeerLearningSourceType,
       "cnvoVNetStatsTable": cnvoVNetStatsTable,
       "cnvoVNetStatsEntry": cnvoVNetStatsEntry,
       "cnvoVNetOutUnicastPackets": cnvoVNetOutUnicastPackets,
       "cnvoVNetOutUnicastBytes": cnvoVNetOutUnicastBytes,
       "cnvoVNetOutMulticastPackets": cnvoVNetOutMulticastPackets,
       "cnvoVNetOutMulticastBytes": cnvoVNetOutMulticastBytes,
       "cnvoVNetInUnicastPackets": cnvoVNetInUnicastPackets,
       "cnvoVNetInUnicastBytes": cnvoVNetInUnicastBytes,
       "cnvoVNetInMulticastPackets": cnvoVNetInMulticastPackets,
       "cnvoVNetInMulticastBytes": cnvoVNetInMulticastBytes,
       "cnvoNvoPeerStatsTable": cnvoNvoPeerStatsTable,
       "cnvoNvoPeerStatsEntry": cnvoNvoPeerStatsEntry,
       "cnvoNvoPeerOutUnicastPackets": cnvoNvoPeerOutUnicastPackets,
       "cnvoNvoPeerOutUnicastBytes": cnvoNvoPeerOutUnicastBytes,
       "cnvoNvoPeerOutMulticastPackets": cnvoNvoPeerOutMulticastPackets,
       "cnvoNvoPeerOutMulticastBytes": cnvoNvoPeerOutMulticastBytes,
       "cnvoNvoPeerInUnicastPackets": cnvoNvoPeerInUnicastPackets,
       "cnvoNvoPeerInUnicastBytes": cnvoNvoPeerInUnicastBytes,
       "cnvoNvoPeerInMulticastPackets": cnvoNvoPeerInMulticastPackets,
       "cnvoNvoPeerInMulticastBytes": cnvoNvoPeerInMulticastBytes,
       "cnvoMIBConform": cnvoMIBConform,
       "cnvoMIBCompliances": cnvoMIBCompliances,
       "cnvoMIBCompliance": cnvoMIBCompliance,
       "cnvoMIBGroups": cnvoMIBGroups,
       "cnvoNvoGroup": cnvoNvoGroup,
       "cnvoVirtualNetworkGroup": cnvoVirtualNetworkGroup,
       "cnvoPeerGroup": cnvoPeerGroup,
       "cnvoVirtualNetworkStatsGroup": cnvoVirtualNetworkStatsGroup,
       "cnvoNvoPerPeerOutUnicastStatsGroup": cnvoNvoPerPeerOutUnicastStatsGroup,
       "cnvoNvoPerPeerInUnicastStatsGroup": cnvoNvoPerPeerInUnicastStatsGroup,
       "cnvoNvoPerPeerInMulticastStatsGroup": cnvoNvoPerPeerInMulticastStatsGroup,
       "cnvoNvoPerPeerOutMulticastStatsGroup": cnvoNvoPerPeerOutMulticastStatsGroup}
)
