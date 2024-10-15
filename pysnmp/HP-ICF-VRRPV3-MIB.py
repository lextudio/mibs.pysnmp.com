# SNMP MIB module (HP-ICF-VRRPV3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-VRRPV3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:29 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(vrrpv3AssociatedIpAddrEntry,
 vrrpv3OperationsEntry,
 vrrpv3OperationsInetAddrType,
 vrrpv3OperationsVrId) = mibBuilder.importSymbols(
    "VRRPV3-MIB",
    "vrrpv3AssociatedIpAddrEntry",
    "vrrpv3OperationsEntry",
    "vrrpv3OperationsInetAddrType",
    "vrrpv3OperationsVrId")


# MODULE-IDENTITY

hpicfVrrpv3MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 90)
)
hpicfVrrpv3MIB.setRevisions(
        ("2015-09-16 00:00",
         "2012-11-21 00:00",
         "2012-10-25 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfVrrpv3Operations_ObjectIdentity = ObjectIdentity
hpicfVrrpv3Operations = _HpicfVrrpv3Operations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 90, 1)
)


class _HpicfVrrpv3IPv4AdminStatus_Type(TruthValue):
    """Custom type hpicfVrrpv3IPv4AdminStatus based on TruthValue"""


_HpicfVrrpv3IPv4AdminStatus_Object = MibScalar
hpicfVrrpv3IPv4AdminStatus = _HpicfVrrpv3IPv4AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 90, 1, 1),
    _HpicfVrrpv3IPv4AdminStatus_Type()
)
hpicfVrrpv3IPv4AdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfVrrpv3IPv4AdminStatus.setStatus("current")


class _HpicfVrrpv3IPv6AdminStatus_Type(TruthValue):
    """Custom type hpicfVrrpv3IPv6AdminStatus based on TruthValue"""


_HpicfVrrpv3IPv6AdminStatus_Object = MibScalar
hpicfVrrpv3IPv6AdminStatus = _HpicfVrrpv3IPv6AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 90, 1, 2),
    _HpicfVrrpv3IPv6AdminStatus_Type()
)
hpicfVrrpv3IPv6AdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfVrrpv3IPv6AdminStatus.setStatus("current")
_HpicfVrrpv3OperationsTable_Object = MibTable
hpicfVrrpv3OperationsTable = _HpicfVrrpv3OperationsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 90, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfVrrpv3OperationsTable.setStatus("current")
_HpicfVrrpv3OperationsEntry_Object = MibTableRow
hpicfVrrpv3OperationsEntry = _HpicfVrrpv3OperationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 90, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hpicfVrrpv3OperationsEntry.setStatus("current")


class _HpicfVrrpv3VrMode_Type(Integer32):
    """Custom type hpicfVrrpv3VrMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("owner", 1),
          ("uninitialized", 3))
    )


_HpicfVrrpv3VrMode_Type.__name__ = "Integer32"
_HpicfVrrpv3VrMode_Object = MibTableColumn
hpicfVrrpv3VrMode = _HpicfVrrpv3VrMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 90, 1, 3, 1, 1),
    _HpicfVrrpv3VrMode_Type()
)
hpicfVrrpv3VrMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfVrrpv3VrMode.setStatus("current")


class _HpicfVrrpv3VrPreemptDelayTime_Type(Integer32):
    """Custom type hpicfVrrpv3VrPreemptDelayTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_HpicfVrrpv3VrPreemptDelayTime_Type.__name__ = "Integer32"
_HpicfVrrpv3VrPreemptDelayTime_Object = MibTableColumn
hpicfVrrpv3VrPreemptDelayTime = _HpicfVrrpv3VrPreemptDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 90, 1, 3, 1, 2),
    _HpicfVrrpv3VrPreemptDelayTime_Type()
)
hpicfVrrpv3VrPreemptDelayTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfVrrpv3VrPreemptDelayTime.setStatus("current")


class _HpicfVrrpv3VrControl_Type(Integer32):
    """Custom type hpicfVrrpv3VrControl based on Integer32"""
    defaultValue = 4

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
        *(("failback", 1),
          ("failover", 2),
          ("failoverWithMonitoring", 3),
          ("invalid", 4))
    )


_HpicfVrrpv3VrControl_Type.__name__ = "Integer32"
_HpicfVrrpv3VrControl_Object = MibTableColumn
hpicfVrrpv3VrControl = _HpicfVrrpv3VrControl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 90, 1, 3, 1, 3),
    _HpicfVrrpv3VrControl_Type()
)
hpicfVrrpv3VrControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfVrrpv3VrControl.setStatus("current")


class _HpicfVrrpv3VrRespondToPing_Type(TruthValue):
    """Custom type hpicfVrrpv3VrRespondToPing based on TruthValue"""


_HpicfVrrpv3VrRespondToPing_Object = MibTableColumn
hpicfVrrpv3VrRespondToPing = _HpicfVrrpv3VrRespondToPing_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 90, 1, 3, 1, 4),
    _HpicfVrrpv3VrRespondToPing_Type()
)
hpicfVrrpv3VrRespondToPing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfVrrpv3VrRespondToPing.setStatus("current")


class _HpicfVrrpv3Version_Type(Integer32):
    """Custom type hpicfVrrpv3Version based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v2", 2),
          ("v3", 3))
    )


_HpicfVrrpv3Version_Type.__name__ = "Integer32"
_HpicfVrrpv3Version_Object = MibTableColumn
hpicfVrrpv3Version = _HpicfVrrpv3Version_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 90, 1, 3, 1, 5),
    _HpicfVrrpv3Version_Type()
)
hpicfVrrpv3Version.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfVrrpv3Version.setStatus("current")


class _HpicfVrrpv3VrNullAuthCompatibility_Type(TruthValue):
    """Custom type hpicfVrrpv3VrNullAuthCompatibility based on TruthValue"""


_HpicfVrrpv3VrNullAuthCompatibility_Object = MibTableColumn
hpicfVrrpv3VrNullAuthCompatibility = _HpicfVrrpv3VrNullAuthCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 90, 1, 3, 1, 6),
    _HpicfVrrpv3VrNullAuthCompatibility_Type()
)
hpicfVrrpv3VrNullAuthCompatibility.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfVrrpv3VrNullAuthCompatibility.setStatus("current")
_HpicfVrrpv3VrBfdIPAddr_Type = InetAddress
_HpicfVrrpv3VrBfdIPAddr_Object = MibTableColumn
hpicfVrrpv3VrBfdIPAddr = _HpicfVrrpv3VrBfdIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 90, 1, 3, 1, 13),
    _HpicfVrrpv3VrBfdIPAddr_Type()
)
hpicfVrrpv3VrBfdIPAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfVrrpv3VrBfdIPAddr.setStatus("current")
_HpicfVrrpv3TrackTable_Object = MibTable
hpicfVrrpv3TrackTable = _HpicfVrrpv3TrackTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 90, 1, 4)
)
if mibBuilder.loadTexts:
    hpicfVrrpv3TrackTable.setStatus("current")
_HpicfVrrpv3TrackEntry_Object = MibTableRow
hpicfVrrpv3TrackEntry = _HpicfVrrpv3TrackEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 90, 1, 4, 1)
)
hpicfVrrpv3TrackEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VRRPV3-MIB", "vrrpv3OperationsVrId"),
    (0, "VRRPV3-MIB", "vrrpv3OperationsInetAddrType"),
    (0, "HP-ICF-VRRPV3-MIB", "hpicfVrrpv3VrTrackType"),
    (0, "HP-ICF-VRRPV3-MIB", "hpicfVrrpv3VrTrackEntity"),
)
if mibBuilder.loadTexts:
    hpicfVrrpv3TrackEntry.setStatus("current")


class _HpicfVrrpv3VrTrackType_Type(Integer32):
    """Custom type hpicfVrrpv3VrTrackType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("port", 1),
          ("trunk", 2),
          ("vlan", 3))
    )


_HpicfVrrpv3VrTrackType_Type.__name__ = "Integer32"
_HpicfVrrpv3VrTrackType_Object = MibTableColumn
hpicfVrrpv3VrTrackType = _HpicfVrrpv3VrTrackType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 90, 1, 4, 1, 1),
    _HpicfVrrpv3VrTrackType_Type()
)
hpicfVrrpv3VrTrackType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfVrrpv3VrTrackType.setStatus("current")


class _HpicfVrrpv3VrTrackEntity_Type(SnmpAdminString):
    """Custom type hpicfVrrpv3VrTrackEntity based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HpicfVrrpv3VrTrackEntity_Type.__name__ = "SnmpAdminString"
_HpicfVrrpv3VrTrackEntity_Object = MibTableColumn
hpicfVrrpv3VrTrackEntity = _HpicfVrrpv3VrTrackEntity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 90, 1, 4, 1, 2),
    _HpicfVrrpv3VrTrackEntity_Type()
)
hpicfVrrpv3VrTrackEntity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfVrrpv3VrTrackEntity.setStatus("current")
_HpicfVrrpv3TrackRowStatus_Type = RowStatus
_HpicfVrrpv3TrackRowStatus_Object = MibTableColumn
hpicfVrrpv3TrackRowStatus = _HpicfVrrpv3TrackRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 90, 1, 4, 1, 3),
    _HpicfVrrpv3TrackRowStatus_Type()
)
hpicfVrrpv3TrackRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfVrrpv3TrackRowStatus.setStatus("current")
_HpicfVrrpv3StatsTable_Object = MibTable
hpicfVrrpv3StatsTable = _HpicfVrrpv3StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 90, 1, 5)
)
if mibBuilder.loadTexts:
    hpicfVrrpv3StatsTable.setStatus("current")
_HpicfVrrpv3StatsEntry_Object = MibTableRow
hpicfVrrpv3StatsEntry = _HpicfVrrpv3StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 90, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hpicfVrrpv3StatsEntry.setStatus("current")


class _HpicfVrrpv3StatsNearFailovers_Type(Counter32):
    """Custom type hpicfVrrpv3StatsNearFailovers based on Counter32"""
    defaultValue = 0


_HpicfVrrpv3StatsNearFailovers_Object = MibTableColumn
hpicfVrrpv3StatsNearFailovers = _HpicfVrrpv3StatsNearFailovers_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 90, 1, 5, 1, 1),
    _HpicfVrrpv3StatsNearFailovers_Type()
)
hpicfVrrpv3StatsNearFailovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVrrpv3StatsNearFailovers.setStatus("current")


class _HpicfVrrpv3RespondToPing_Type(TruthValue):
    """Custom type hpicfVrrpv3RespondToPing based on TruthValue"""


_HpicfVrrpv3RespondToPing_Object = MibScalar
hpicfVrrpv3RespondToPing = _HpicfVrrpv3RespondToPing_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 90, 1, 6),
    _HpicfVrrpv3RespondToPing_Type()
)
hpicfVrrpv3RespondToPing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfVrrpv3RespondToPing.setStatus("current")


class _HpicfVrrpv3RemoveConfig_Type(TruthValue):
    """Custom type hpicfVrrpv3RemoveConfig based on TruthValue"""


_HpicfVrrpv3RemoveConfig_Object = MibScalar
hpicfVrrpv3RemoveConfig = _HpicfVrrpv3RemoveConfig_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 90, 1, 7),
    _HpicfVrrpv3RemoveConfig_Type()
)
hpicfVrrpv3RemoveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfVrrpv3RemoveConfig.setStatus("current")


class _HpicfVrrpv3Nonstop_Type(TruthValue):
    """Custom type hpicfVrrpv3Nonstop based on TruthValue"""


_HpicfVrrpv3Nonstop_Object = MibScalar
hpicfVrrpv3Nonstop = _HpicfVrrpv3Nonstop_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 90, 1, 8),
    _HpicfVrrpv3Nonstop_Type()
)
hpicfVrrpv3Nonstop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfVrrpv3Nonstop.setStatus("current")


class _HpicfVrrpv3NotificationCntl_Type(Integer32):
    """Custom type hpicfVrrpv3NotificationCntl based on Integer32"""
    defaultValue = 1

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


_HpicfVrrpv3NotificationCntl_Type.__name__ = "Integer32"
_HpicfVrrpv3NotificationCntl_Object = MibScalar
hpicfVrrpv3NotificationCntl = _HpicfVrrpv3NotificationCntl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 90, 1, 9),
    _HpicfVrrpv3NotificationCntl_Type()
)
hpicfVrrpv3NotificationCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfVrrpv3NotificationCntl.setStatus("current")
_HpicfVrrpv3ErrorObjects_ObjectIdentity = ObjectIdentity
hpicfVrrpv3ErrorObjects = _HpicfVrrpv3ErrorObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 90, 1, 10)
)


class _HpicfVrrpv3IPv4RouterChecksumErrors_Type(Counter64):
    """Custom type hpicfVrrpv3IPv4RouterChecksumErrors based on Counter64"""
    defaultValue = 0


_HpicfVrrpv3IPv4RouterChecksumErrors_Object = MibScalar
hpicfVrrpv3IPv4RouterChecksumErrors = _HpicfVrrpv3IPv4RouterChecksumErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 90, 1, 10, 1),
    _HpicfVrrpv3IPv4RouterChecksumErrors_Type()
)
hpicfVrrpv3IPv4RouterChecksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVrrpv3IPv4RouterChecksumErrors.setStatus("current")


class _HpicfVrrpv3IPv6RouterChecksumErrors_Type(Counter64):
    """Custom type hpicfVrrpv3IPv6RouterChecksumErrors based on Counter64"""
    defaultValue = 0


_HpicfVrrpv3IPv6RouterChecksumErrors_Object = MibScalar
hpicfVrrpv3IPv6RouterChecksumErrors = _HpicfVrrpv3IPv6RouterChecksumErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 90, 1, 10, 2),
    _HpicfVrrpv3IPv6RouterChecksumErrors_Type()
)
hpicfVrrpv3IPv6RouterChecksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVrrpv3IPv6RouterChecksumErrors.setStatus("current")


class _HpicfVrrpv3IPv4RouterVersionErrors_Type(Counter64):
    """Custom type hpicfVrrpv3IPv4RouterVersionErrors based on Counter64"""
    defaultValue = 0


_HpicfVrrpv3IPv4RouterVersionErrors_Object = MibScalar
hpicfVrrpv3IPv4RouterVersionErrors = _HpicfVrrpv3IPv4RouterVersionErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 90, 1, 10, 3),
    _HpicfVrrpv3IPv4RouterVersionErrors_Type()
)
hpicfVrrpv3IPv4RouterVersionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVrrpv3IPv4RouterVersionErrors.setStatus("current")


class _HpicfVrrpv3IPv6RouterVersionErrors_Type(Counter64):
    """Custom type hpicfVrrpv3IPv6RouterVersionErrors based on Counter64"""
    defaultValue = 0


_HpicfVrrpv3IPv6RouterVersionErrors_Object = MibScalar
hpicfVrrpv3IPv6RouterVersionErrors = _HpicfVrrpv3IPv6RouterVersionErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 90, 1, 10, 4),
    _HpicfVrrpv3IPv6RouterVersionErrors_Type()
)
hpicfVrrpv3IPv6RouterVersionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVrrpv3IPv6RouterVersionErrors.setStatus("current")


class _HpicfVrrpv3IPv4RouterVrIdErrors_Type(Counter64):
    """Custom type hpicfVrrpv3IPv4RouterVrIdErrors based on Counter64"""
    defaultValue = 0


_HpicfVrrpv3IPv4RouterVrIdErrors_Object = MibScalar
hpicfVrrpv3IPv4RouterVrIdErrors = _HpicfVrrpv3IPv4RouterVrIdErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 90, 1, 10, 5),
    _HpicfVrrpv3IPv4RouterVrIdErrors_Type()
)
hpicfVrrpv3IPv4RouterVrIdErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVrrpv3IPv4RouterVrIdErrors.setStatus("current")


class _HpicfVrrpv3IPv6RouterVrIdErrors_Type(Counter64):
    """Custom type hpicfVrrpv3IPv6RouterVrIdErrors based on Counter64"""
    defaultValue = 0


_HpicfVrrpv3IPv6RouterVrIdErrors_Object = MibScalar
hpicfVrrpv3IPv6RouterVrIdErrors = _HpicfVrrpv3IPv6RouterVrIdErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 90, 1, 10, 6),
    _HpicfVrrpv3IPv6RouterVrIdErrors_Type()
)
hpicfVrrpv3IPv6RouterVrIdErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVrrpv3IPv6RouterVrIdErrors.setStatus("current")
_HpicfVrrpv3Conformance_ObjectIdentity = ObjectIdentity
hpicfVrrpv3Conformance = _HpicfVrrpv3Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 90, 2)
)
_HpicfVrrpv3MIBCompliances_ObjectIdentity = ObjectIdentity
hpicfVrrpv3MIBCompliances = _HpicfVrrpv3MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 90, 2, 1)
)
_HpicfVrrpv3MIBGroups_ObjectIdentity = ObjectIdentity
hpicfVrrpv3MIBGroups = _HpicfVrrpv3MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 90, 2, 2)
)
vrrpv3OperationsEntry.registerAugmentions(
    ("HP-ICF-VRRPV3-MIB",
     "hpicfVrrpv3OperationsEntry")
)
hpicfVrrpv3OperationsEntry.setIndexNames(*vrrpv3OperationsEntry.getIndexNames())
vrrpv3OperationsEntry.registerAugmentions(
    ("HP-ICF-VRRPV3-MIB",
     "hpicfVrrpv3StatsEntry")
)
hpicfVrrpv3StatsEntry.setIndexNames(*vrrpv3OperationsEntry.getIndexNames())

# Managed Objects groups

hpicfVrrpv3OperGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 90, 2, 2, 1)
)
hpicfVrrpv3OperGroup.setObjects(
      *(("HP-ICF-VRRPV3-MIB", "hpicfVrrpv3IPv4AdminStatus"),
        ("HP-ICF-VRRPV3-MIB", "hpicfVrrpv3IPv6AdminStatus"),
        ("HP-ICF-VRRPV3-MIB", "hpicfVrrpv3Version"),
        ("HP-ICF-VRRPV3-MIB", "hpicfVrrpv3VrMode"),
        ("HP-ICF-VRRPV3-MIB", "hpicfVrrpv3VrRespondToPing"),
        ("HP-ICF-VRRPV3-MIB", "hpicfVrrpv3VrPreemptDelayTime"),
        ("HP-ICF-VRRPV3-MIB", "hpicfVrrpv3VrControl"),
        ("HP-ICF-VRRPV3-MIB", "hpicfVrrpv3StatsNearFailovers"),
        ("HP-ICF-VRRPV3-MIB", "hpicfVrrpv3VrNullAuthCompatibility"),
        ("HP-ICF-VRRPV3-MIB", "hpicfVrrpv3RespondToPing"),
        ("HP-ICF-VRRPV3-MIB", "hpicfVrrpv3RemoveConfig"),
        ("HP-ICF-VRRPV3-MIB", "hpicfVrrpv3Nonstop"),
        ("HP-ICF-VRRPV3-MIB", "hpicfVrrpv3NotificationCntl"),
        ("HP-ICF-VRRPV3-MIB", "hpicfVrrpv3IPv4RouterChecksumErrors"),
        ("HP-ICF-VRRPV3-MIB", "hpicfVrrpv3IPv6RouterChecksumErrors"),
        ("HP-ICF-VRRPV3-MIB", "hpicfVrrpv3IPv4RouterVersionErrors"),
        ("HP-ICF-VRRPV3-MIB", "hpicfVrrpv3IPv6RouterVersionErrors"),
        ("HP-ICF-VRRPV3-MIB", "hpicfVrrpv3IPv4RouterVrIdErrors"),
        ("HP-ICF-VRRPV3-MIB", "hpicfVrrpv3IPv6RouterVrIdErrors"))
)
if mibBuilder.loadTexts:
    hpicfVrrpv3OperGroup.setStatus("current")

hpicfVrrpv3TrackGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 90, 2, 2, 2)
)
hpicfVrrpv3TrackGroup.setObjects(
    ("HP-ICF-VRRPV3-MIB", "hpicfVrrpv3TrackRowStatus")
)
if mibBuilder.loadTexts:
    hpicfVrrpv3TrackGroup.setStatus("current")

hpicfVrrpv3BfdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 90, 2, 2, 5)
)
hpicfVrrpv3BfdGroup.setObjects(
    ("HP-ICF-VRRPV3-MIB", "hpicfVrrpv3VrBfdIPAddr")
)
if mibBuilder.loadTexts:
    hpicfVrrpv3BfdGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfVrrpv3MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 90, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfVrrpv3MIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-VRRPV3-MIB",
    **{"hpicfVrrpv3MIB": hpicfVrrpv3MIB,
       "hpicfVrrpv3Operations": hpicfVrrpv3Operations,
       "hpicfVrrpv3IPv4AdminStatus": hpicfVrrpv3IPv4AdminStatus,
       "hpicfVrrpv3IPv6AdminStatus": hpicfVrrpv3IPv6AdminStatus,
       "hpicfVrrpv3OperationsTable": hpicfVrrpv3OperationsTable,
       "hpicfVrrpv3OperationsEntry": hpicfVrrpv3OperationsEntry,
       "hpicfVrrpv3VrMode": hpicfVrrpv3VrMode,
       "hpicfVrrpv3VrPreemptDelayTime": hpicfVrrpv3VrPreemptDelayTime,
       "hpicfVrrpv3VrControl": hpicfVrrpv3VrControl,
       "hpicfVrrpv3VrRespondToPing": hpicfVrrpv3VrRespondToPing,
       "hpicfVrrpv3Version": hpicfVrrpv3Version,
       "hpicfVrrpv3VrNullAuthCompatibility": hpicfVrrpv3VrNullAuthCompatibility,
       "hpicfVrrpv3VrBfdIPAddr": hpicfVrrpv3VrBfdIPAddr,
       "hpicfVrrpv3TrackTable": hpicfVrrpv3TrackTable,
       "hpicfVrrpv3TrackEntry": hpicfVrrpv3TrackEntry,
       "hpicfVrrpv3VrTrackType": hpicfVrrpv3VrTrackType,
       "hpicfVrrpv3VrTrackEntity": hpicfVrrpv3VrTrackEntity,
       "hpicfVrrpv3TrackRowStatus": hpicfVrrpv3TrackRowStatus,
       "hpicfVrrpv3StatsTable": hpicfVrrpv3StatsTable,
       "hpicfVrrpv3StatsEntry": hpicfVrrpv3StatsEntry,
       "hpicfVrrpv3StatsNearFailovers": hpicfVrrpv3StatsNearFailovers,
       "hpicfVrrpv3RespondToPing": hpicfVrrpv3RespondToPing,
       "hpicfVrrpv3RemoveConfig": hpicfVrrpv3RemoveConfig,
       "hpicfVrrpv3Nonstop": hpicfVrrpv3Nonstop,
       "hpicfVrrpv3NotificationCntl": hpicfVrrpv3NotificationCntl,
       "hpicfVrrpv3ErrorObjects": hpicfVrrpv3ErrorObjects,
       "hpicfVrrpv3IPv4RouterChecksumErrors": hpicfVrrpv3IPv4RouterChecksumErrors,
       "hpicfVrrpv3IPv6RouterChecksumErrors": hpicfVrrpv3IPv6RouterChecksumErrors,
       "hpicfVrrpv3IPv4RouterVersionErrors": hpicfVrrpv3IPv4RouterVersionErrors,
       "hpicfVrrpv3IPv6RouterVersionErrors": hpicfVrrpv3IPv6RouterVersionErrors,
       "hpicfVrrpv3IPv4RouterVrIdErrors": hpicfVrrpv3IPv4RouterVrIdErrors,
       "hpicfVrrpv3IPv6RouterVrIdErrors": hpicfVrrpv3IPv6RouterVrIdErrors,
       "hpicfVrrpv3Conformance": hpicfVrrpv3Conformance,
       "hpicfVrrpv3MIBCompliances": hpicfVrrpv3MIBCompliances,
       "hpicfVrrpv3MIBCompliance": hpicfVrrpv3MIBCompliance,
       "hpicfVrrpv3MIBGroups": hpicfVrrpv3MIBGroups,
       "hpicfVrrpv3OperGroup": hpicfVrrpv3OperGroup,
       "hpicfVrrpv3TrackGroup": hpicfVrrpv3TrackGroup,
       "hpicfVrrpv3BfdGroup": hpicfVrrpv3BfdGroup}
)
