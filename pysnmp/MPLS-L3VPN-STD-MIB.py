# SNMP MIB module (MPLS-L3VPN-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MPLS-L3VPN-STD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:04 2024
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

(IANAipRouteProtocol,) = mibBuilder.importSymbols(
    "IANA-RTPROTO-MIB",
    "IANAipRouteProtocol")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetAutonomousSystemNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetAutonomousSystemNumber")

(MplsIndexType,) = mibBuilder.importSymbols(
    "MPLS-LSR-STD-MIB",
    "MplsIndexType")

(mplsStdMIB,) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "mplsStdMIB")

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
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(VPNIdOrZero,) = mibBuilder.importSymbols(
    "VPN-TC-STD-MIB",
    "VPNIdOrZero")


# MODULE-IDENTITY

mplsL3VpnMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 11)
)
mplsL3VpnMIB.setRevisions(
        ("2006-01-23 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MplsL3VpnName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )



class MplsL3VpnRouteDistinguisher(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class MplsL3VpnRtType(Integer32, TextualConvention):
    status = "current"
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
          ("export", 2),
          ("import", 1))
    )



# MIB Managed Objects in the order of their OIDs

_MplsL3VpnNotifications_ObjectIdentity = ObjectIdentity
mplsL3VpnNotifications = _MplsL3VpnNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 0)
)
_MplsL3VpnObjects_ObjectIdentity = ObjectIdentity
mplsL3VpnObjects = _MplsL3VpnObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1)
)
_MplsL3VpnScalars_ObjectIdentity = ObjectIdentity
mplsL3VpnScalars = _MplsL3VpnScalars_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 1)
)
_MplsL3VpnConfiguredVrfs_Type = Unsigned32
_MplsL3VpnConfiguredVrfs_Object = MibScalar
mplsL3VpnConfiguredVrfs = _MplsL3VpnConfiguredVrfs_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 1, 1),
    _MplsL3VpnConfiguredVrfs_Type()
)
mplsL3VpnConfiguredVrfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsL3VpnConfiguredVrfs.setStatus("current")
_MplsL3VpnActiveVrfs_Type = Gauge32
_MplsL3VpnActiveVrfs_Object = MibScalar
mplsL3VpnActiveVrfs = _MplsL3VpnActiveVrfs_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 1, 2),
    _MplsL3VpnActiveVrfs_Type()
)
mplsL3VpnActiveVrfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsL3VpnActiveVrfs.setStatus("current")
_MplsL3VpnConnectedInterfaces_Type = Gauge32
_MplsL3VpnConnectedInterfaces_Object = MibScalar
mplsL3VpnConnectedInterfaces = _MplsL3VpnConnectedInterfaces_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 1, 3),
    _MplsL3VpnConnectedInterfaces_Type()
)
mplsL3VpnConnectedInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsL3VpnConnectedInterfaces.setStatus("current")


class _MplsL3VpnNotificationEnable_Type(TruthValue):
    """Custom type mplsL3VpnNotificationEnable based on TruthValue"""


_MplsL3VpnNotificationEnable_Object = MibScalar
mplsL3VpnNotificationEnable = _MplsL3VpnNotificationEnable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 1, 4),
    _MplsL3VpnNotificationEnable_Type()
)
mplsL3VpnNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsL3VpnNotificationEnable.setStatus("current")
_MplsL3VpnVrfConfMaxPossRts_Type = Unsigned32
_MplsL3VpnVrfConfMaxPossRts_Object = MibScalar
mplsL3VpnVrfConfMaxPossRts = _MplsL3VpnVrfConfMaxPossRts_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 1, 5),
    _MplsL3VpnVrfConfMaxPossRts_Type()
)
mplsL3VpnVrfConfMaxPossRts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsL3VpnVrfConfMaxPossRts.setStatus("current")


class _MplsL3VpnVrfConfRteMxThrshTime_Type(Unsigned32):
    """Custom type mplsL3VpnVrfConfRteMxThrshTime based on Unsigned32"""
    defaultValue = 0


_MplsL3VpnVrfConfRteMxThrshTime_Object = MibScalar
mplsL3VpnVrfConfRteMxThrshTime = _MplsL3VpnVrfConfRteMxThrshTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 1, 6),
    _MplsL3VpnVrfConfRteMxThrshTime_Type()
)
mplsL3VpnVrfConfRteMxThrshTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsL3VpnVrfConfRteMxThrshTime.setStatus("current")
if mibBuilder.loadTexts:
    mplsL3VpnVrfConfRteMxThrshTime.setUnits("seconds")
_MplsL3VpnIllLblRcvThrsh_Type = Unsigned32
_MplsL3VpnIllLblRcvThrsh_Object = MibScalar
mplsL3VpnIllLblRcvThrsh = _MplsL3VpnIllLblRcvThrsh_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 1, 7),
    _MplsL3VpnIllLblRcvThrsh_Type()
)
mplsL3VpnIllLblRcvThrsh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsL3VpnIllLblRcvThrsh.setStatus("current")
_MplsL3VpnConf_ObjectIdentity = ObjectIdentity
mplsL3VpnConf = _MplsL3VpnConf_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2)
)
_MplsL3VpnIfConfTable_Object = MibTable
mplsL3VpnIfConfTable = _MplsL3VpnIfConfTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mplsL3VpnIfConfTable.setStatus("current")
_MplsL3VpnIfConfEntry_Object = MibTableRow
mplsL3VpnIfConfEntry = _MplsL3VpnIfConfEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 1, 1)
)
mplsL3VpnIfConfEntry.setIndexNames(
    (0, "MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfName"),
    (0, "MPLS-L3VPN-STD-MIB", "mplsL3VpnIfConfIndex"),
)
if mibBuilder.loadTexts:
    mplsL3VpnIfConfEntry.setStatus("current")
_MplsL3VpnIfConfIndex_Type = InterfaceIndex
_MplsL3VpnIfConfIndex_Object = MibTableColumn
mplsL3VpnIfConfIndex = _MplsL3VpnIfConfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 1, 1, 1),
    _MplsL3VpnIfConfIndex_Type()
)
mplsL3VpnIfConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsL3VpnIfConfIndex.setStatus("current")


class _MplsL3VpnIfVpnClassification_Type(Integer32):
    """Custom type mplsL3VpnIfVpnClassification based on Integer32"""
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
        *(("carrierOfCarrier", 1),
          ("enterprise", 2),
          ("interProvider", 3))
    )


_MplsL3VpnIfVpnClassification_Type.__name__ = "Integer32"
_MplsL3VpnIfVpnClassification_Object = MibTableColumn
mplsL3VpnIfVpnClassification = _MplsL3VpnIfVpnClassification_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 1, 1, 2),
    _MplsL3VpnIfVpnClassification_Type()
)
mplsL3VpnIfVpnClassification.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsL3VpnIfVpnClassification.setStatus("current")


class _MplsL3VpnIfVpnRouteDistProtocol_Type(Bits):
    """Custom type mplsL3VpnIfVpnRouteDistProtocol based on Bits"""
    namedValues = NamedValues(
        *(("bgp", 1),
          ("isis", 4),
          ("none", 0),
          ("ospf", 2),
          ("other", 6),
          ("rip", 3),
          ("static", 5))
    )

_MplsL3VpnIfVpnRouteDistProtocol_Type.__name__ = "Bits"
_MplsL3VpnIfVpnRouteDistProtocol_Object = MibTableColumn
mplsL3VpnIfVpnRouteDistProtocol = _MplsL3VpnIfVpnRouteDistProtocol_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 1, 1, 3),
    _MplsL3VpnIfVpnRouteDistProtocol_Type()
)
mplsL3VpnIfVpnRouteDistProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsL3VpnIfVpnRouteDistProtocol.setStatus("current")


class _MplsL3VpnIfConfStorageType_Type(StorageType):
    """Custom type mplsL3VpnIfConfStorageType based on StorageType"""


_MplsL3VpnIfConfStorageType_Object = MibTableColumn
mplsL3VpnIfConfStorageType = _MplsL3VpnIfConfStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 1, 1, 4),
    _MplsL3VpnIfConfStorageType_Type()
)
mplsL3VpnIfConfStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsL3VpnIfConfStorageType.setStatus("current")
_MplsL3VpnIfConfRowStatus_Type = RowStatus
_MplsL3VpnIfConfRowStatus_Object = MibTableColumn
mplsL3VpnIfConfRowStatus = _MplsL3VpnIfConfRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 1, 1, 5),
    _MplsL3VpnIfConfRowStatus_Type()
)
mplsL3VpnIfConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsL3VpnIfConfRowStatus.setStatus("current")
_MplsL3VpnVrfTable_Object = MibTable
mplsL3VpnVrfTable = _MplsL3VpnVrfTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 2)
)
if mibBuilder.loadTexts:
    mplsL3VpnVrfTable.setStatus("current")
_MplsL3VpnVrfEntry_Object = MibTableRow
mplsL3VpnVrfEntry = _MplsL3VpnVrfEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 2, 1)
)
mplsL3VpnVrfEntry.setIndexNames(
    (0, "MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfName"),
)
if mibBuilder.loadTexts:
    mplsL3VpnVrfEntry.setStatus("current")
_MplsL3VpnVrfName_Type = MplsL3VpnName
_MplsL3VpnVrfName_Object = MibTableColumn
mplsL3VpnVrfName = _MplsL3VpnVrfName_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 2, 1, 1),
    _MplsL3VpnVrfName_Type()
)
mplsL3VpnVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsL3VpnVrfName.setStatus("current")
_MplsL3VpnVrfVpnId_Type = VPNIdOrZero
_MplsL3VpnVrfVpnId_Object = MibTableColumn
mplsL3VpnVrfVpnId = _MplsL3VpnVrfVpnId_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 2, 1, 2),
    _MplsL3VpnVrfVpnId_Type()
)
mplsL3VpnVrfVpnId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsL3VpnVrfVpnId.setStatus("current")
_MplsL3VpnVrfDescription_Type = SnmpAdminString
_MplsL3VpnVrfDescription_Object = MibTableColumn
mplsL3VpnVrfDescription = _MplsL3VpnVrfDescription_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 2, 1, 3),
    _MplsL3VpnVrfDescription_Type()
)
mplsL3VpnVrfDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsL3VpnVrfDescription.setStatus("current")
_MplsL3VpnVrfRD_Type = MplsL3VpnRouteDistinguisher
_MplsL3VpnVrfRD_Object = MibTableColumn
mplsL3VpnVrfRD = _MplsL3VpnVrfRD_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 2, 1, 4),
    _MplsL3VpnVrfRD_Type()
)
mplsL3VpnVrfRD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsL3VpnVrfRD.setStatus("current")
_MplsL3VpnVrfCreationTime_Type = TimeStamp
_MplsL3VpnVrfCreationTime_Object = MibTableColumn
mplsL3VpnVrfCreationTime = _MplsL3VpnVrfCreationTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 2, 1, 5),
    _MplsL3VpnVrfCreationTime_Type()
)
mplsL3VpnVrfCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsL3VpnVrfCreationTime.setStatus("current")


class _MplsL3VpnVrfOperStatus_Type(Integer32):
    """Custom type mplsL3VpnVrfOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_MplsL3VpnVrfOperStatus_Type.__name__ = "Integer32"
_MplsL3VpnVrfOperStatus_Object = MibTableColumn
mplsL3VpnVrfOperStatus = _MplsL3VpnVrfOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 2, 1, 6),
    _MplsL3VpnVrfOperStatus_Type()
)
mplsL3VpnVrfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsL3VpnVrfOperStatus.setStatus("current")
_MplsL3VpnVrfActiveInterfaces_Type = Gauge32
_MplsL3VpnVrfActiveInterfaces_Object = MibTableColumn
mplsL3VpnVrfActiveInterfaces = _MplsL3VpnVrfActiveInterfaces_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 2, 1, 7),
    _MplsL3VpnVrfActiveInterfaces_Type()
)
mplsL3VpnVrfActiveInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsL3VpnVrfActiveInterfaces.setStatus("current")
_MplsL3VpnVrfAssociatedInterfaces_Type = Unsigned32
_MplsL3VpnVrfAssociatedInterfaces_Object = MibTableColumn
mplsL3VpnVrfAssociatedInterfaces = _MplsL3VpnVrfAssociatedInterfaces_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 2, 1, 8),
    _MplsL3VpnVrfAssociatedInterfaces_Type()
)
mplsL3VpnVrfAssociatedInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsL3VpnVrfAssociatedInterfaces.setStatus("current")


class _MplsL3VpnVrfConfMidRteThresh_Type(Unsigned32):
    """Custom type mplsL3VpnVrfConfMidRteThresh based on Unsigned32"""
    defaultValue = 0


_MplsL3VpnVrfConfMidRteThresh_Object = MibTableColumn
mplsL3VpnVrfConfMidRteThresh = _MplsL3VpnVrfConfMidRteThresh_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 2, 1, 9),
    _MplsL3VpnVrfConfMidRteThresh_Type()
)
mplsL3VpnVrfConfMidRteThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsL3VpnVrfConfMidRteThresh.setStatus("current")


class _MplsL3VpnVrfConfHighRteThresh_Type(Unsigned32):
    """Custom type mplsL3VpnVrfConfHighRteThresh based on Unsigned32"""
    defaultValue = 0


_MplsL3VpnVrfConfHighRteThresh_Object = MibTableColumn
mplsL3VpnVrfConfHighRteThresh = _MplsL3VpnVrfConfHighRteThresh_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 2, 1, 10),
    _MplsL3VpnVrfConfHighRteThresh_Type()
)
mplsL3VpnVrfConfHighRteThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsL3VpnVrfConfHighRteThresh.setStatus("current")


class _MplsL3VpnVrfConfMaxRoutes_Type(Unsigned32):
    """Custom type mplsL3VpnVrfConfMaxRoutes based on Unsigned32"""
    defaultValue = 0


_MplsL3VpnVrfConfMaxRoutes_Object = MibTableColumn
mplsL3VpnVrfConfMaxRoutes = _MplsL3VpnVrfConfMaxRoutes_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 2, 1, 11),
    _MplsL3VpnVrfConfMaxRoutes_Type()
)
mplsL3VpnVrfConfMaxRoutes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsL3VpnVrfConfMaxRoutes.setStatus("current")
_MplsL3VpnVrfConfLastChanged_Type = TimeStamp
_MplsL3VpnVrfConfLastChanged_Object = MibTableColumn
mplsL3VpnVrfConfLastChanged = _MplsL3VpnVrfConfLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 2, 1, 12),
    _MplsL3VpnVrfConfLastChanged_Type()
)
mplsL3VpnVrfConfLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsL3VpnVrfConfLastChanged.setStatus("current")
_MplsL3VpnVrfConfRowStatus_Type = RowStatus
_MplsL3VpnVrfConfRowStatus_Object = MibTableColumn
mplsL3VpnVrfConfRowStatus = _MplsL3VpnVrfConfRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 2, 1, 13),
    _MplsL3VpnVrfConfRowStatus_Type()
)
mplsL3VpnVrfConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsL3VpnVrfConfRowStatus.setStatus("current")


class _MplsL3VpnVrfConfAdminStatus_Type(Integer32):
    """Custom type mplsL3VpnVrfConfAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_MplsL3VpnVrfConfAdminStatus_Type.__name__ = "Integer32"
_MplsL3VpnVrfConfAdminStatus_Object = MibTableColumn
mplsL3VpnVrfConfAdminStatus = _MplsL3VpnVrfConfAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 2, 1, 14),
    _MplsL3VpnVrfConfAdminStatus_Type()
)
mplsL3VpnVrfConfAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsL3VpnVrfConfAdminStatus.setStatus("current")


class _MplsL3VpnVrfConfStorageType_Type(StorageType):
    """Custom type mplsL3VpnVrfConfStorageType based on StorageType"""


_MplsL3VpnVrfConfStorageType_Object = MibTableColumn
mplsL3VpnVrfConfStorageType = _MplsL3VpnVrfConfStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 2, 1, 15),
    _MplsL3VpnVrfConfStorageType_Type()
)
mplsL3VpnVrfConfStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsL3VpnVrfConfStorageType.setStatus("current")
_MplsL3VpnVrfRTTable_Object = MibTable
mplsL3VpnVrfRTTable = _MplsL3VpnVrfRTTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 3)
)
if mibBuilder.loadTexts:
    mplsL3VpnVrfRTTable.setStatus("current")
_MplsL3VpnVrfRTEntry_Object = MibTableRow
mplsL3VpnVrfRTEntry = _MplsL3VpnVrfRTEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 3, 1)
)
mplsL3VpnVrfRTEntry.setIndexNames(
    (0, "MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfName"),
    (0, "MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfRTIndex"),
    (0, "MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfRTType"),
)
if mibBuilder.loadTexts:
    mplsL3VpnVrfRTEntry.setStatus("current")


class _MplsL3VpnVrfRTIndex_Type(Unsigned32):
    """Custom type mplsL3VpnVrfRTIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MplsL3VpnVrfRTIndex_Type.__name__ = "Unsigned32"
_MplsL3VpnVrfRTIndex_Object = MibTableColumn
mplsL3VpnVrfRTIndex = _MplsL3VpnVrfRTIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 3, 1, 2),
    _MplsL3VpnVrfRTIndex_Type()
)
mplsL3VpnVrfRTIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsL3VpnVrfRTIndex.setStatus("current")
_MplsL3VpnVrfRTType_Type = MplsL3VpnRtType
_MplsL3VpnVrfRTType_Object = MibTableColumn
mplsL3VpnVrfRTType = _MplsL3VpnVrfRTType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 3, 1, 3),
    _MplsL3VpnVrfRTType_Type()
)
mplsL3VpnVrfRTType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsL3VpnVrfRTType.setStatus("current")
_MplsL3VpnVrfRT_Type = MplsL3VpnRouteDistinguisher
_MplsL3VpnVrfRT_Object = MibTableColumn
mplsL3VpnVrfRT = _MplsL3VpnVrfRT_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 3, 1, 4),
    _MplsL3VpnVrfRT_Type()
)
mplsL3VpnVrfRT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsL3VpnVrfRT.setStatus("current")
_MplsL3VpnVrfRTDescr_Type = SnmpAdminString
_MplsL3VpnVrfRTDescr_Object = MibTableColumn
mplsL3VpnVrfRTDescr = _MplsL3VpnVrfRTDescr_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 3, 1, 5),
    _MplsL3VpnVrfRTDescr_Type()
)
mplsL3VpnVrfRTDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsL3VpnVrfRTDescr.setStatus("current")
_MplsL3VpnVrfRTRowStatus_Type = RowStatus
_MplsL3VpnVrfRTRowStatus_Object = MibTableColumn
mplsL3VpnVrfRTRowStatus = _MplsL3VpnVrfRTRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 3, 1, 6),
    _MplsL3VpnVrfRTRowStatus_Type()
)
mplsL3VpnVrfRTRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsL3VpnVrfRTRowStatus.setStatus("current")


class _MplsL3VpnVrfRTStorageType_Type(StorageType):
    """Custom type mplsL3VpnVrfRTStorageType based on StorageType"""


_MplsL3VpnVrfRTStorageType_Object = MibTableColumn
mplsL3VpnVrfRTStorageType = _MplsL3VpnVrfRTStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 3, 1, 7),
    _MplsL3VpnVrfRTStorageType_Type()
)
mplsL3VpnVrfRTStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsL3VpnVrfRTStorageType.setStatus("current")
_MplsL3VpnVrfSecTable_Object = MibTable
mplsL3VpnVrfSecTable = _MplsL3VpnVrfSecTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 6)
)
if mibBuilder.loadTexts:
    mplsL3VpnVrfSecTable.setStatus("current")
_MplsL3VpnVrfSecEntry_Object = MibTableRow
mplsL3VpnVrfSecEntry = _MplsL3VpnVrfSecEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    mplsL3VpnVrfSecEntry.setStatus("current")
_MplsL3VpnVrfSecIllegalLblVltns_Type = Counter32
_MplsL3VpnVrfSecIllegalLblVltns_Object = MibTableColumn
mplsL3VpnVrfSecIllegalLblVltns = _MplsL3VpnVrfSecIllegalLblVltns_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 6, 1, 1),
    _MplsL3VpnVrfSecIllegalLblVltns_Type()
)
mplsL3VpnVrfSecIllegalLblVltns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsL3VpnVrfSecIllegalLblVltns.setStatus("current")
_MplsL3VpnVrfSecDiscontinuityTime_Type = TimeStamp
_MplsL3VpnVrfSecDiscontinuityTime_Object = MibTableColumn
mplsL3VpnVrfSecDiscontinuityTime = _MplsL3VpnVrfSecDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 2, 6, 1, 2),
    _MplsL3VpnVrfSecDiscontinuityTime_Type()
)
mplsL3VpnVrfSecDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsL3VpnVrfSecDiscontinuityTime.setStatus("current")
_MplsL3VpnPerf_ObjectIdentity = ObjectIdentity
mplsL3VpnPerf = _MplsL3VpnPerf_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 3)
)
_MplsL3VpnVrfPerfTable_Object = MibTable
mplsL3VpnVrfPerfTable = _MplsL3VpnVrfPerfTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 3, 1)
)
if mibBuilder.loadTexts:
    mplsL3VpnVrfPerfTable.setStatus("current")
_MplsL3VpnVrfPerfEntry_Object = MibTableRow
mplsL3VpnVrfPerfEntry = _MplsL3VpnVrfPerfEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    mplsL3VpnVrfPerfEntry.setStatus("current")
_MplsL3VpnVrfPerfRoutesAdded_Type = Counter32
_MplsL3VpnVrfPerfRoutesAdded_Object = MibTableColumn
mplsL3VpnVrfPerfRoutesAdded = _MplsL3VpnVrfPerfRoutesAdded_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 3, 1, 1, 1),
    _MplsL3VpnVrfPerfRoutesAdded_Type()
)
mplsL3VpnVrfPerfRoutesAdded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsL3VpnVrfPerfRoutesAdded.setStatus("current")
_MplsL3VpnVrfPerfRoutesDeleted_Type = Counter32
_MplsL3VpnVrfPerfRoutesDeleted_Object = MibTableColumn
mplsL3VpnVrfPerfRoutesDeleted = _MplsL3VpnVrfPerfRoutesDeleted_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 3, 1, 1, 2),
    _MplsL3VpnVrfPerfRoutesDeleted_Type()
)
mplsL3VpnVrfPerfRoutesDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsL3VpnVrfPerfRoutesDeleted.setStatus("current")
_MplsL3VpnVrfPerfCurrNumRoutes_Type = Gauge32
_MplsL3VpnVrfPerfCurrNumRoutes_Object = MibTableColumn
mplsL3VpnVrfPerfCurrNumRoutes = _MplsL3VpnVrfPerfCurrNumRoutes_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 3, 1, 1, 3),
    _MplsL3VpnVrfPerfCurrNumRoutes_Type()
)
mplsL3VpnVrfPerfCurrNumRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsL3VpnVrfPerfCurrNumRoutes.setStatus("current")
_MplsL3VpnVrfPerfRoutesDropped_Type = Counter32
_MplsL3VpnVrfPerfRoutesDropped_Object = MibTableColumn
mplsL3VpnVrfPerfRoutesDropped = _MplsL3VpnVrfPerfRoutesDropped_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 3, 1, 1, 4),
    _MplsL3VpnVrfPerfRoutesDropped_Type()
)
mplsL3VpnVrfPerfRoutesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsL3VpnVrfPerfRoutesDropped.setStatus("current")
_MplsL3VpnVrfPerfDiscTime_Type = TimeStamp
_MplsL3VpnVrfPerfDiscTime_Object = MibTableColumn
mplsL3VpnVrfPerfDiscTime = _MplsL3VpnVrfPerfDiscTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 3, 1, 1, 5),
    _MplsL3VpnVrfPerfDiscTime_Type()
)
mplsL3VpnVrfPerfDiscTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsL3VpnVrfPerfDiscTime.setStatus("current")
_MplsL3VpnRoute_ObjectIdentity = ObjectIdentity
mplsL3VpnRoute = _MplsL3VpnRoute_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 4)
)
_MplsL3VpnVrfRteTable_Object = MibTable
mplsL3VpnVrfRteTable = _MplsL3VpnVrfRteTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 4, 1)
)
if mibBuilder.loadTexts:
    mplsL3VpnVrfRteTable.setStatus("current")
_MplsL3VpnVrfRteEntry_Object = MibTableRow
mplsL3VpnVrfRteEntry = _MplsL3VpnVrfRteEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 4, 1, 1)
)
mplsL3VpnVrfRteEntry.setIndexNames(
    (0, "MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfName"),
    (0, "MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfRteInetCidrDestType"),
    (0, "MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfRteInetCidrDest"),
    (0, "MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfRteInetCidrPfxLen"),
    (0, "MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfRteInetCidrPolicy"),
    (0, "MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfRteInetCidrNHopType"),
    (0, "MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfRteInetCidrNextHop"),
)
if mibBuilder.loadTexts:
    mplsL3VpnVrfRteEntry.setStatus("current")
_MplsL3VpnVrfRteInetCidrDestType_Type = InetAddressType
_MplsL3VpnVrfRteInetCidrDestType_Object = MibTableColumn
mplsL3VpnVrfRteInetCidrDestType = _MplsL3VpnVrfRteInetCidrDestType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 4, 1, 1, 1),
    _MplsL3VpnVrfRteInetCidrDestType_Type()
)
mplsL3VpnVrfRteInetCidrDestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsL3VpnVrfRteInetCidrDestType.setStatus("current")
_MplsL3VpnVrfRteInetCidrDest_Type = InetAddress
_MplsL3VpnVrfRteInetCidrDest_Object = MibTableColumn
mplsL3VpnVrfRteInetCidrDest = _MplsL3VpnVrfRteInetCidrDest_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 4, 1, 1, 2),
    _MplsL3VpnVrfRteInetCidrDest_Type()
)
mplsL3VpnVrfRteInetCidrDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsL3VpnVrfRteInetCidrDest.setStatus("current")


class _MplsL3VpnVrfRteInetCidrPfxLen_Type(InetAddressPrefixLength):
    """Custom type mplsL3VpnVrfRteInetCidrPfxLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MplsL3VpnVrfRteInetCidrPfxLen_Type.__name__ = "InetAddressPrefixLength"
_MplsL3VpnVrfRteInetCidrPfxLen_Object = MibTableColumn
mplsL3VpnVrfRteInetCidrPfxLen = _MplsL3VpnVrfRteInetCidrPfxLen_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 4, 1, 1, 3),
    _MplsL3VpnVrfRteInetCidrPfxLen_Type()
)
mplsL3VpnVrfRteInetCidrPfxLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsL3VpnVrfRteInetCidrPfxLen.setStatus("current")
_MplsL3VpnVrfRteInetCidrPolicy_Type = ObjectIdentifier
_MplsL3VpnVrfRteInetCidrPolicy_Object = MibTableColumn
mplsL3VpnVrfRteInetCidrPolicy = _MplsL3VpnVrfRteInetCidrPolicy_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 4, 1, 1, 4),
    _MplsL3VpnVrfRteInetCidrPolicy_Type()
)
mplsL3VpnVrfRteInetCidrPolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsL3VpnVrfRteInetCidrPolicy.setStatus("current")
_MplsL3VpnVrfRteInetCidrNHopType_Type = InetAddressType
_MplsL3VpnVrfRteInetCidrNHopType_Object = MibTableColumn
mplsL3VpnVrfRteInetCidrNHopType = _MplsL3VpnVrfRteInetCidrNHopType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 4, 1, 1, 5),
    _MplsL3VpnVrfRteInetCidrNHopType_Type()
)
mplsL3VpnVrfRteInetCidrNHopType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsL3VpnVrfRteInetCidrNHopType.setStatus("current")
_MplsL3VpnVrfRteInetCidrNextHop_Type = InetAddress
_MplsL3VpnVrfRteInetCidrNextHop_Object = MibTableColumn
mplsL3VpnVrfRteInetCidrNextHop = _MplsL3VpnVrfRteInetCidrNextHop_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 4, 1, 1, 6),
    _MplsL3VpnVrfRteInetCidrNextHop_Type()
)
mplsL3VpnVrfRteInetCidrNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsL3VpnVrfRteInetCidrNextHop.setStatus("current")


class _MplsL3VpnVrfRteInetCidrIfIndex_Type(InterfaceIndexOrZero):
    """Custom type mplsL3VpnVrfRteInetCidrIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_MplsL3VpnVrfRteInetCidrIfIndex_Object = MibTableColumn
mplsL3VpnVrfRteInetCidrIfIndex = _MplsL3VpnVrfRteInetCidrIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 4, 1, 1, 7),
    _MplsL3VpnVrfRteInetCidrIfIndex_Type()
)
mplsL3VpnVrfRteInetCidrIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsL3VpnVrfRteInetCidrIfIndex.setStatus("current")


class _MplsL3VpnVrfRteInetCidrType_Type(Integer32):
    """Custom type mplsL3VpnVrfRteInetCidrType based on Integer32"""
    defaultValue = 1

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
        *(("blackhole", 5),
          ("local", 3),
          ("other", 1),
          ("reject", 2),
          ("remote", 4))
    )


_MplsL3VpnVrfRteInetCidrType_Type.__name__ = "Integer32"
_MplsL3VpnVrfRteInetCidrType_Object = MibTableColumn
mplsL3VpnVrfRteInetCidrType = _MplsL3VpnVrfRteInetCidrType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 4, 1, 1, 8),
    _MplsL3VpnVrfRteInetCidrType_Type()
)
mplsL3VpnVrfRteInetCidrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsL3VpnVrfRteInetCidrType.setStatus("current")
_MplsL3VpnVrfRteInetCidrProto_Type = IANAipRouteProtocol
_MplsL3VpnVrfRteInetCidrProto_Object = MibTableColumn
mplsL3VpnVrfRteInetCidrProto = _MplsL3VpnVrfRteInetCidrProto_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 4, 1, 1, 9),
    _MplsL3VpnVrfRteInetCidrProto_Type()
)
mplsL3VpnVrfRteInetCidrProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsL3VpnVrfRteInetCidrProto.setStatus("current")
_MplsL3VpnVrfRteInetCidrAge_Type = Gauge32
_MplsL3VpnVrfRteInetCidrAge_Object = MibTableColumn
mplsL3VpnVrfRteInetCidrAge = _MplsL3VpnVrfRteInetCidrAge_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 4, 1, 1, 10),
    _MplsL3VpnVrfRteInetCidrAge_Type()
)
mplsL3VpnVrfRteInetCidrAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsL3VpnVrfRteInetCidrAge.setStatus("current")


class _MplsL3VpnVrfRteInetCidrNextHopAS_Type(InetAutonomousSystemNumber):
    """Custom type mplsL3VpnVrfRteInetCidrNextHopAS based on InetAutonomousSystemNumber"""
    defaultValue = 0


_MplsL3VpnVrfRteInetCidrNextHopAS_Object = MibTableColumn
mplsL3VpnVrfRteInetCidrNextHopAS = _MplsL3VpnVrfRteInetCidrNextHopAS_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 4, 1, 1, 11),
    _MplsL3VpnVrfRteInetCidrNextHopAS_Type()
)
mplsL3VpnVrfRteInetCidrNextHopAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsL3VpnVrfRteInetCidrNextHopAS.setStatus("current")


class _MplsL3VpnVrfRteInetCidrMetric1_Type(Integer32):
    """Custom type mplsL3VpnVrfRteInetCidrMetric1 based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_MplsL3VpnVrfRteInetCidrMetric1_Type.__name__ = "Integer32"
_MplsL3VpnVrfRteInetCidrMetric1_Object = MibTableColumn
mplsL3VpnVrfRteInetCidrMetric1 = _MplsL3VpnVrfRteInetCidrMetric1_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 4, 1, 1, 12),
    _MplsL3VpnVrfRteInetCidrMetric1_Type()
)
mplsL3VpnVrfRteInetCidrMetric1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsL3VpnVrfRteInetCidrMetric1.setStatus("current")


class _MplsL3VpnVrfRteInetCidrMetric2_Type(Integer32):
    """Custom type mplsL3VpnVrfRteInetCidrMetric2 based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_MplsL3VpnVrfRteInetCidrMetric2_Type.__name__ = "Integer32"
_MplsL3VpnVrfRteInetCidrMetric2_Object = MibTableColumn
mplsL3VpnVrfRteInetCidrMetric2 = _MplsL3VpnVrfRteInetCidrMetric2_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 4, 1, 1, 13),
    _MplsL3VpnVrfRteInetCidrMetric2_Type()
)
mplsL3VpnVrfRteInetCidrMetric2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsL3VpnVrfRteInetCidrMetric2.setStatus("current")


class _MplsL3VpnVrfRteInetCidrMetric3_Type(Integer32):
    """Custom type mplsL3VpnVrfRteInetCidrMetric3 based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_MplsL3VpnVrfRteInetCidrMetric3_Type.__name__ = "Integer32"
_MplsL3VpnVrfRteInetCidrMetric3_Object = MibTableColumn
mplsL3VpnVrfRteInetCidrMetric3 = _MplsL3VpnVrfRteInetCidrMetric3_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 4, 1, 1, 14),
    _MplsL3VpnVrfRteInetCidrMetric3_Type()
)
mplsL3VpnVrfRteInetCidrMetric3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsL3VpnVrfRteInetCidrMetric3.setStatus("current")


class _MplsL3VpnVrfRteInetCidrMetric4_Type(Integer32):
    """Custom type mplsL3VpnVrfRteInetCidrMetric4 based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_MplsL3VpnVrfRteInetCidrMetric4_Type.__name__ = "Integer32"
_MplsL3VpnVrfRteInetCidrMetric4_Object = MibTableColumn
mplsL3VpnVrfRteInetCidrMetric4 = _MplsL3VpnVrfRteInetCidrMetric4_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 4, 1, 1, 15),
    _MplsL3VpnVrfRteInetCidrMetric4_Type()
)
mplsL3VpnVrfRteInetCidrMetric4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsL3VpnVrfRteInetCidrMetric4.setStatus("current")


class _MplsL3VpnVrfRteInetCidrMetric5_Type(Integer32):
    """Custom type mplsL3VpnVrfRteInetCidrMetric5 based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_MplsL3VpnVrfRteInetCidrMetric5_Type.__name__ = "Integer32"
_MplsL3VpnVrfRteInetCidrMetric5_Object = MibTableColumn
mplsL3VpnVrfRteInetCidrMetric5 = _MplsL3VpnVrfRteInetCidrMetric5_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 4, 1, 1, 16),
    _MplsL3VpnVrfRteInetCidrMetric5_Type()
)
mplsL3VpnVrfRteInetCidrMetric5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsL3VpnVrfRteInetCidrMetric5.setStatus("current")
_MplsL3VpnVrfRteXCPointer_Type = MplsIndexType
_MplsL3VpnVrfRteXCPointer_Object = MibTableColumn
mplsL3VpnVrfRteXCPointer = _MplsL3VpnVrfRteXCPointer_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 4, 1, 1, 17),
    _MplsL3VpnVrfRteXCPointer_Type()
)
mplsL3VpnVrfRteXCPointer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsL3VpnVrfRteXCPointer.setStatus("current")
_MplsL3VpnVrfRteInetCidrStatus_Type = RowStatus
_MplsL3VpnVrfRteInetCidrStatus_Object = MibTableColumn
mplsL3VpnVrfRteInetCidrStatus = _MplsL3VpnVrfRteInetCidrStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 1, 4, 1, 1, 18),
    _MplsL3VpnVrfRteInetCidrStatus_Type()
)
mplsL3VpnVrfRteInetCidrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsL3VpnVrfRteInetCidrStatus.setStatus("current")
_MplsL3VpnConformance_ObjectIdentity = ObjectIdentity
mplsL3VpnConformance = _MplsL3VpnConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 2)
)
_MplsL3VpnGroups_ObjectIdentity = ObjectIdentity
mplsL3VpnGroups = _MplsL3VpnGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 2, 1)
)
_MplsL3VpnCompliances_ObjectIdentity = ObjectIdentity
mplsL3VpnCompliances = _MplsL3VpnCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 2, 2)
)
mplsL3VpnVrfEntry.registerAugmentions(
    ("MPLS-L3VPN-STD-MIB",
     "mplsL3VpnVrfSecEntry")
)
mplsL3VpnVrfSecEntry.setIndexNames(*mplsL3VpnVrfEntry.getIndexNames())
mplsL3VpnVrfEntry.registerAugmentions(
    ("MPLS-L3VPN-STD-MIB",
     "mplsL3VpnVrfPerfEntry")
)
mplsL3VpnVrfPerfEntry.setIndexNames(*mplsL3VpnVrfEntry.getIndexNames())

# Managed Objects groups

mplsL3VpnScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 2, 1, 1)
)
mplsL3VpnScalarGroup.setObjects(
      *(("MPLS-L3VPN-STD-MIB", "mplsL3VpnConfiguredVrfs"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnActiveVrfs"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnConnectedInterfaces"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnNotificationEnable"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfConfMaxPossRts"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfConfRteMxThrshTime"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnIllLblRcvThrsh"))
)
if mibBuilder.loadTexts:
    mplsL3VpnScalarGroup.setStatus("current")

mplsL3VpnVrfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 2, 1, 2)
)
mplsL3VpnVrfGroup.setObjects(
      *(("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfVpnId"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfDescription"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfRD"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfCreationTime"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfOperStatus"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfActiveInterfaces"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfAssociatedInterfaces"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfConfMidRteThresh"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfConfHighRteThresh"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfConfMaxRoutes"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfConfLastChanged"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfConfRowStatus"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfConfAdminStatus"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfConfStorageType"))
)
if mibBuilder.loadTexts:
    mplsL3VpnVrfGroup.setStatus("current")

mplsL3VpnIfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 2, 1, 3)
)
mplsL3VpnIfGroup.setObjects(
      *(("MPLS-L3VPN-STD-MIB", "mplsL3VpnIfVpnClassification"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnIfVpnRouteDistProtocol"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnIfConfStorageType"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnIfConfRowStatus"))
)
if mibBuilder.loadTexts:
    mplsL3VpnIfGroup.setStatus("current")

mplsL3VpnPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 2, 1, 4)
)
mplsL3VpnPerfGroup.setObjects(
      *(("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfPerfRoutesAdded"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfPerfRoutesDeleted"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfPerfCurrNumRoutes"))
)
if mibBuilder.loadTexts:
    mplsL3VpnPerfGroup.setStatus("current")

mplsL3VpnPerfRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 2, 1, 5)
)
mplsL3VpnPerfRouteGroup.setObjects(
      *(("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfPerfRoutesDropped"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfPerfDiscTime"))
)
if mibBuilder.loadTexts:
    mplsL3VpnPerfRouteGroup.setStatus("current")

mplsL3VpnSecGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 2, 1, 7)
)
mplsL3VpnSecGroup.setObjects(
      *(("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfSecIllegalLblVltns"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfSecDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    mplsL3VpnSecGroup.setStatus("current")

mplsL3VpnVrfRteGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 2, 1, 8)
)
mplsL3VpnVrfRteGroup.setObjects(
      *(("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfRteInetCidrIfIndex"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfRteInetCidrType"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfRteInetCidrProto"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfRteInetCidrAge"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfRteInetCidrNextHopAS"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfRteInetCidrMetric1"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfRteInetCidrMetric2"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfRteInetCidrMetric3"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfRteInetCidrMetric4"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfRteInetCidrMetric5"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfRteXCPointer"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfRteInetCidrStatus"))
)
if mibBuilder.loadTexts:
    mplsL3VpnVrfRteGroup.setStatus("current")

mplsL3VpnVrfRTGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 2, 1, 9)
)
mplsL3VpnVrfRTGroup.setObjects(
      *(("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfRTDescr"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfRT"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfRTRowStatus"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfRTStorageType"))
)
if mibBuilder.loadTexts:
    mplsL3VpnVrfRTGroup.setStatus("current")


# Notification objects

mplsL3VpnVrfUp = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 0, 1)
)
mplsL3VpnVrfUp.setObjects(
      *(("MPLS-L3VPN-STD-MIB", "mplsL3VpnIfConfRowStatus"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfOperStatus"))
)
if mibBuilder.loadTexts:
    mplsL3VpnVrfUp.setStatus(
        "current"
    )

mplsL3VpnVrfDown = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 0, 2)
)
mplsL3VpnVrfDown.setObjects(
      *(("MPLS-L3VPN-STD-MIB", "mplsL3VpnIfConfRowStatus"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfOperStatus"))
)
if mibBuilder.loadTexts:
    mplsL3VpnVrfDown.setStatus(
        "current"
    )

mplsL3VpnVrfRouteMidThreshExceeded = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 0, 3)
)
mplsL3VpnVrfRouteMidThreshExceeded.setObjects(
      *(("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfPerfCurrNumRoutes"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfConfMidRteThresh"))
)
if mibBuilder.loadTexts:
    mplsL3VpnVrfRouteMidThreshExceeded.setStatus(
        "current"
    )

mplsL3VpnVrfNumVrfRouteMaxThreshExceeded = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 0, 4)
)
mplsL3VpnVrfNumVrfRouteMaxThreshExceeded.setObjects(
      *(("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfPerfCurrNumRoutes"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfConfHighRteThresh"))
)
if mibBuilder.loadTexts:
    mplsL3VpnVrfNumVrfRouteMaxThreshExceeded.setStatus(
        "current"
    )

mplsL3VpnNumVrfSecIllglLblThrshExcd = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 0, 5)
)
mplsL3VpnNumVrfSecIllglLblThrshExcd.setObjects(
    ("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfSecIllegalLblVltns")
)
if mibBuilder.loadTexts:
    mplsL3VpnNumVrfSecIllglLblThrshExcd.setStatus(
        "current"
    )

mplsL3VpnNumVrfRouteMaxThreshCleared = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 0, 6)
)
mplsL3VpnNumVrfRouteMaxThreshCleared.setObjects(
      *(("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfPerfCurrNumRoutes"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfConfHighRteThresh"))
)
if mibBuilder.loadTexts:
    mplsL3VpnNumVrfRouteMaxThreshCleared.setStatus(
        "current"
    )


# Notifications groups

mplsL3VpnNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 2, 1, 10)
)
mplsL3VpnNotificationGroup.setObjects(
      *(("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfUp"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfDown"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfRouteMidThreshExceeded"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfNumVrfRouteMaxThreshExceeded"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnNumVrfSecIllglLblThrshExcd"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnNumVrfRouteMaxThreshCleared"))
)
if mibBuilder.loadTexts:
    mplsL3VpnNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

mplsL3VpnModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mplsL3VpnModuleFullCompliance.setStatus(
        "current"
    )

mplsL3VpnModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 166, 11, 2, 2, 2)
)
if mibBuilder.loadTexts:
    mplsL3VpnModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MPLS-L3VPN-STD-MIB",
    **{"MplsL3VpnName": MplsL3VpnName,
       "MplsL3VpnRouteDistinguisher": MplsL3VpnRouteDistinguisher,
       "MplsL3VpnRtType": MplsL3VpnRtType,
       "mplsL3VpnMIB": mplsL3VpnMIB,
       "mplsL3VpnNotifications": mplsL3VpnNotifications,
       "mplsL3VpnVrfUp": mplsL3VpnVrfUp,
       "mplsL3VpnVrfDown": mplsL3VpnVrfDown,
       "mplsL3VpnVrfRouteMidThreshExceeded": mplsL3VpnVrfRouteMidThreshExceeded,
       "mplsL3VpnVrfNumVrfRouteMaxThreshExceeded": mplsL3VpnVrfNumVrfRouteMaxThreshExceeded,
       "mplsL3VpnNumVrfSecIllglLblThrshExcd": mplsL3VpnNumVrfSecIllglLblThrshExcd,
       "mplsL3VpnNumVrfRouteMaxThreshCleared": mplsL3VpnNumVrfRouteMaxThreshCleared,
       "mplsL3VpnObjects": mplsL3VpnObjects,
       "mplsL3VpnScalars": mplsL3VpnScalars,
       "mplsL3VpnConfiguredVrfs": mplsL3VpnConfiguredVrfs,
       "mplsL3VpnActiveVrfs": mplsL3VpnActiveVrfs,
       "mplsL3VpnConnectedInterfaces": mplsL3VpnConnectedInterfaces,
       "mplsL3VpnNotificationEnable": mplsL3VpnNotificationEnable,
       "mplsL3VpnVrfConfMaxPossRts": mplsL3VpnVrfConfMaxPossRts,
       "mplsL3VpnVrfConfRteMxThrshTime": mplsL3VpnVrfConfRteMxThrshTime,
       "mplsL3VpnIllLblRcvThrsh": mplsL3VpnIllLblRcvThrsh,
       "mplsL3VpnConf": mplsL3VpnConf,
       "mplsL3VpnIfConfTable": mplsL3VpnIfConfTable,
       "mplsL3VpnIfConfEntry": mplsL3VpnIfConfEntry,
       "mplsL3VpnIfConfIndex": mplsL3VpnIfConfIndex,
       "mplsL3VpnIfVpnClassification": mplsL3VpnIfVpnClassification,
       "mplsL3VpnIfVpnRouteDistProtocol": mplsL3VpnIfVpnRouteDistProtocol,
       "mplsL3VpnIfConfStorageType": mplsL3VpnIfConfStorageType,
       "mplsL3VpnIfConfRowStatus": mplsL3VpnIfConfRowStatus,
       "mplsL3VpnVrfTable": mplsL3VpnVrfTable,
       "mplsL3VpnVrfEntry": mplsL3VpnVrfEntry,
       "mplsL3VpnVrfName": mplsL3VpnVrfName,
       "mplsL3VpnVrfVpnId": mplsL3VpnVrfVpnId,
       "mplsL3VpnVrfDescription": mplsL3VpnVrfDescription,
       "mplsL3VpnVrfRD": mplsL3VpnVrfRD,
       "mplsL3VpnVrfCreationTime": mplsL3VpnVrfCreationTime,
       "mplsL3VpnVrfOperStatus": mplsL3VpnVrfOperStatus,
       "mplsL3VpnVrfActiveInterfaces": mplsL3VpnVrfActiveInterfaces,
       "mplsL3VpnVrfAssociatedInterfaces": mplsL3VpnVrfAssociatedInterfaces,
       "mplsL3VpnVrfConfMidRteThresh": mplsL3VpnVrfConfMidRteThresh,
       "mplsL3VpnVrfConfHighRteThresh": mplsL3VpnVrfConfHighRteThresh,
       "mplsL3VpnVrfConfMaxRoutes": mplsL3VpnVrfConfMaxRoutes,
       "mplsL3VpnVrfConfLastChanged": mplsL3VpnVrfConfLastChanged,
       "mplsL3VpnVrfConfRowStatus": mplsL3VpnVrfConfRowStatus,
       "mplsL3VpnVrfConfAdminStatus": mplsL3VpnVrfConfAdminStatus,
       "mplsL3VpnVrfConfStorageType": mplsL3VpnVrfConfStorageType,
       "mplsL3VpnVrfRTTable": mplsL3VpnVrfRTTable,
       "mplsL3VpnVrfRTEntry": mplsL3VpnVrfRTEntry,
       "mplsL3VpnVrfRTIndex": mplsL3VpnVrfRTIndex,
       "mplsL3VpnVrfRTType": mplsL3VpnVrfRTType,
       "mplsL3VpnVrfRT": mplsL3VpnVrfRT,
       "mplsL3VpnVrfRTDescr": mplsL3VpnVrfRTDescr,
       "mplsL3VpnVrfRTRowStatus": mplsL3VpnVrfRTRowStatus,
       "mplsL3VpnVrfRTStorageType": mplsL3VpnVrfRTStorageType,
       "mplsL3VpnVrfSecTable": mplsL3VpnVrfSecTable,
       "mplsL3VpnVrfSecEntry": mplsL3VpnVrfSecEntry,
       "mplsL3VpnVrfSecIllegalLblVltns": mplsL3VpnVrfSecIllegalLblVltns,
       "mplsL3VpnVrfSecDiscontinuityTime": mplsL3VpnVrfSecDiscontinuityTime,
       "mplsL3VpnPerf": mplsL3VpnPerf,
       "mplsL3VpnVrfPerfTable": mplsL3VpnVrfPerfTable,
       "mplsL3VpnVrfPerfEntry": mplsL3VpnVrfPerfEntry,
       "mplsL3VpnVrfPerfRoutesAdded": mplsL3VpnVrfPerfRoutesAdded,
       "mplsL3VpnVrfPerfRoutesDeleted": mplsL3VpnVrfPerfRoutesDeleted,
       "mplsL3VpnVrfPerfCurrNumRoutes": mplsL3VpnVrfPerfCurrNumRoutes,
       "mplsL3VpnVrfPerfRoutesDropped": mplsL3VpnVrfPerfRoutesDropped,
       "mplsL3VpnVrfPerfDiscTime": mplsL3VpnVrfPerfDiscTime,
       "mplsL3VpnRoute": mplsL3VpnRoute,
       "mplsL3VpnVrfRteTable": mplsL3VpnVrfRteTable,
       "mplsL3VpnVrfRteEntry": mplsL3VpnVrfRteEntry,
       "mplsL3VpnVrfRteInetCidrDestType": mplsL3VpnVrfRteInetCidrDestType,
       "mplsL3VpnVrfRteInetCidrDest": mplsL3VpnVrfRteInetCidrDest,
       "mplsL3VpnVrfRteInetCidrPfxLen": mplsL3VpnVrfRteInetCidrPfxLen,
       "mplsL3VpnVrfRteInetCidrPolicy": mplsL3VpnVrfRteInetCidrPolicy,
       "mplsL3VpnVrfRteInetCidrNHopType": mplsL3VpnVrfRteInetCidrNHopType,
       "mplsL3VpnVrfRteInetCidrNextHop": mplsL3VpnVrfRteInetCidrNextHop,
       "mplsL3VpnVrfRteInetCidrIfIndex": mplsL3VpnVrfRteInetCidrIfIndex,
       "mplsL3VpnVrfRteInetCidrType": mplsL3VpnVrfRteInetCidrType,
       "mplsL3VpnVrfRteInetCidrProto": mplsL3VpnVrfRteInetCidrProto,
       "mplsL3VpnVrfRteInetCidrAge": mplsL3VpnVrfRteInetCidrAge,
       "mplsL3VpnVrfRteInetCidrNextHopAS": mplsL3VpnVrfRteInetCidrNextHopAS,
       "mplsL3VpnVrfRteInetCidrMetric1": mplsL3VpnVrfRteInetCidrMetric1,
       "mplsL3VpnVrfRteInetCidrMetric2": mplsL3VpnVrfRteInetCidrMetric2,
       "mplsL3VpnVrfRteInetCidrMetric3": mplsL3VpnVrfRteInetCidrMetric3,
       "mplsL3VpnVrfRteInetCidrMetric4": mplsL3VpnVrfRteInetCidrMetric4,
       "mplsL3VpnVrfRteInetCidrMetric5": mplsL3VpnVrfRteInetCidrMetric5,
       "mplsL3VpnVrfRteXCPointer": mplsL3VpnVrfRteXCPointer,
       "mplsL3VpnVrfRteInetCidrStatus": mplsL3VpnVrfRteInetCidrStatus,
       "mplsL3VpnConformance": mplsL3VpnConformance,
       "mplsL3VpnGroups": mplsL3VpnGroups,
       "mplsL3VpnScalarGroup": mplsL3VpnScalarGroup,
       "mplsL3VpnVrfGroup": mplsL3VpnVrfGroup,
       "mplsL3VpnIfGroup": mplsL3VpnIfGroup,
       "mplsL3VpnPerfGroup": mplsL3VpnPerfGroup,
       "mplsL3VpnPerfRouteGroup": mplsL3VpnPerfRouteGroup,
       "mplsL3VpnSecGroup": mplsL3VpnSecGroup,
       "mplsL3VpnVrfRteGroup": mplsL3VpnVrfRteGroup,
       "mplsL3VpnVrfRTGroup": mplsL3VpnVrfRTGroup,
       "mplsL3VpnNotificationGroup": mplsL3VpnNotificationGroup,
       "mplsL3VpnCompliances": mplsL3VpnCompliances,
       "mplsL3VpnModuleFullCompliance": mplsL3VpnModuleFullCompliance,
       "mplsL3VpnModuleReadOnlyCompliance": mplsL3VpnModuleReadOnlyCompliance}
)
