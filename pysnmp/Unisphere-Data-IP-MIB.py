# SNMP MIB module (Unisphere-Data-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-IP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:10:53 2024
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(ipCidrRouteEntry,) = mibBuilder.importSymbols(
    "IP-FORWARD-MIB",
    "ipCidrRouteEntry")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")

(UsdEnable,
 UsdIpAddrLessIf,
 UsdNextIfIndex) = mibBuilder.importSymbols(
    "Unisphere-Data-TC",
    "UsdEnable",
    "UsdIpAddrLessIf",
    "UsdNextIfIndex")


# MODULE-IDENTITY

usdIpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12)
)
usdIpMIB.setRevisions(
        ("2002-04-03 14:04",
         "2001-07-05 14:00",
         "2001-06-18 19:11",
         "2000-07-31 00:00",
         "1999-11-09 00:00",
         "1999-09-16 00:00",
         "1998-11-19 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UsdIpObjects_ObjectIdentity = ObjectIdentity
usdIpObjects = _UsdIpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1)
)
_UsdIpInterface_ObjectIdentity = ObjectIdentity
usdIpInterface = _UsdIpInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1)
)
_UsdIpNextIfIndex_Type = UsdNextIfIndex
_UsdIpNextIfIndex_Object = MibScalar
usdIpNextIfIndex = _UsdIpNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 1),
    _UsdIpNextIfIndex_Type()
)
usdIpNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpNextIfIndex.setStatus("current")
_UsdIpIfTable_Object = MibTable
usdIpIfTable = _UsdIpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2)
)
if mibBuilder.loadTexts:
    usdIpIfTable.setStatus("current")
_UsdIpIfEntry_Object = MibTableRow
usdIpIfEntry = _UsdIpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1)
)
usdIpIfEntry.setIndexNames(
    (0, "Unisphere-Data-IP-MIB", "usdIpIfIndex"),
)
if mibBuilder.loadTexts:
    usdIpIfEntry.setStatus("current")
_UsdIpIfIndex_Type = InterfaceIndex
_UsdIpIfIndex_Object = MibTableColumn
usdIpIfIndex = _UsdIpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 1),
    _UsdIpIfIndex_Type()
)
usdIpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIpIfIndex.setStatus("current")
_UsdIpIfRowStatus_Type = RowStatus
_UsdIpIfRowStatus_Object = MibTableColumn
usdIpIfRowStatus = _UsdIpIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 2),
    _UsdIpIfRowStatus_Type()
)
usdIpIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpIfRowStatus.setStatus("current")
_UsdIpIfLowerIfIndex_Type = InterfaceIndexOrZero
_UsdIpIfLowerIfIndex_Object = MibTableColumn
usdIpIfLowerIfIndex = _UsdIpIfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 3),
    _UsdIpIfLowerIfIndex_Type()
)
usdIpIfLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpIfLowerIfIndex.setStatus("current")


class _UsdIpIfType_Type(Integer32):
    """Custom type usdIpIfType based on Integer32"""
    defaultValue = 2

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
        *(("broadcast", 1),
          ("loopback", 4),
          ("nbma", 3),
          ("null", 5),
          ("other", 0),
          ("pointToPoint", 2))
    )


_UsdIpIfType_Type.__name__ = "Integer32"
_UsdIpIfType_Object = MibTableColumn
usdIpIfType = _UsdIpIfType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 4),
    _UsdIpIfType_Type()
)
usdIpIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpIfType.setStatus("current")


class _UsdIpIfTypeId_Type(Unsigned32):
    """Custom type usdIpIfTypeId based on Unsigned32"""
    defaultValue = 0


_UsdIpIfTypeId_Object = MibTableColumn
usdIpIfTypeId = _UsdIpIfTypeId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 5),
    _UsdIpIfTypeId_Type()
)
usdIpIfTypeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpIfTypeId.setStatus("current")


class _UsdIpIfSAValidationEnable_Type(UsdEnable):
    """Custom type usdIpIfSAValidationEnable based on UsdEnable"""


_UsdIpIfSAValidationEnable_Object = MibTableColumn
usdIpIfSAValidationEnable = _UsdIpIfSAValidationEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 6),
    _UsdIpIfSAValidationEnable_Type()
)
usdIpIfSAValidationEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpIfSAValidationEnable.setStatus("current")


class _UsdIpIfCreationType_Type(Integer32):
    """Custom type usdIpIfCreationType based on Integer32"""
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


_UsdIpIfCreationType_Type.__name__ = "Integer32"
_UsdIpIfCreationType_Object = MibTableColumn
usdIpIfCreationType = _UsdIpIfCreationType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 7),
    _UsdIpIfCreationType_Type()
)
usdIpIfCreationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpIfCreationType.setStatus("current")


class _UsdIpIfProfileId_Type(Unsigned32):
    """Custom type usdIpIfProfileId based on Unsigned32"""
    defaultValue = 0


_UsdIpIfProfileId_Object = MibTableColumn
usdIpIfProfileId = _UsdIpIfProfileId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 8),
    _UsdIpIfProfileId_Type()
)
usdIpIfProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpIfProfileId.setStatus("current")


class _UsdIpIfAlwaysUp_Type(UsdEnable):
    """Custom type usdIpIfAlwaysUp based on UsdEnable"""


_UsdIpIfAlwaysUp_Object = MibTableColumn
usdIpIfAlwaysUp = _UsdIpIfAlwaysUp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 9),
    _UsdIpIfAlwaysUp_Type()
)
usdIpIfAlwaysUp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpIfAlwaysUp.setStatus("current")


class _UsdIpIfLoopback_Type(UsdEnable):
    """Custom type usdIpIfLoopback based on UsdEnable"""


_UsdIpIfLoopback_Object = MibTableColumn
usdIpIfLoopback = _UsdIpIfLoopback_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 10),
    _UsdIpIfLoopback_Type()
)
usdIpIfLoopback.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpIfLoopback.setStatus("current")


class _UsdIpIfLoopbackUid_Type(InterfaceIndexOrZero):
    """Custom type usdIpIfLoopbackUid based on InterfaceIndexOrZero"""
    defaultValue = 0


_UsdIpIfLoopbackUid_Object = MibTableColumn
usdIpIfLoopbackUid = _UsdIpIfLoopbackUid_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 11),
    _UsdIpIfLoopbackUid_Type()
)
usdIpIfLoopbackUid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpIfLoopbackUid.setStatus("current")


class _UsdIpIfDebounceTime_Type(Integer32):
    """Custom type usdIpIfDebounceTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_UsdIpIfDebounceTime_Type.__name__ = "Integer32"
_UsdIpIfDebounceTime_Object = MibTableColumn
usdIpIfDebounceTime = _UsdIpIfDebounceTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 12),
    _UsdIpIfDebounceTime_Type()
)
usdIpIfDebounceTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpIfDebounceTime.setStatus("current")
if mibBuilder.loadTexts:
    usdIpIfDebounceTime.setUnits("milliseconds")


class _UsdIpIfForwarding_Type(UsdEnable):
    """Custom type usdIpIfForwarding based on UsdEnable"""


_UsdIpIfForwarding_Object = MibTableColumn
usdIpIfForwarding = _UsdIpIfForwarding_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 13),
    _UsdIpIfForwarding_Type()
)
usdIpIfForwarding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpIfForwarding.setStatus("current")


class _UsdIpIfForceFragmentation_Type(UsdEnable):
    """Custom type usdIpIfForceFragmentation based on UsdEnable"""


_UsdIpIfForceFragmentation_Object = MibTableColumn
usdIpIfForceFragmentation = _UsdIpIfForceFragmentation_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 14),
    _UsdIpIfForceFragmentation_Type()
)
usdIpIfForceFragmentation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpIfForceFragmentation.setStatus("current")
_UsdIpIfSharesLowerUid_Type = UsdEnable
_UsdIpIfSharesLowerUid_Object = MibTableColumn
usdIpIfSharesLowerUid = _UsdIpIfSharesLowerUid_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 15),
    _UsdIpIfSharesLowerUid_Type()
)
usdIpIfSharesLowerUid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpIfSharesLowerUid.setStatus("current")


class _UsdIpIfFilterOptions_Type(Unsigned32):
    """Custom type usdIpIfFilterOptions based on Unsigned32"""
    defaultValue = 0


_UsdIpIfFilterOptions_Object = MibTableColumn
usdIpIfFilterOptions = _UsdIpIfFilterOptions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 16),
    _UsdIpIfFilterOptions_Type()
)
usdIpIfFilterOptions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpIfFilterOptions.setStatus("current")


class _UsdIpIfName_Type(OctetString):
    """Custom type usdIpIfName based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UsdIpIfName_Type.__name__ = "OctetString"
_UsdIpIfName_Object = MibTableColumn
usdIpIfName = _UsdIpIfName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 17),
    _UsdIpIfName_Type()
)
usdIpIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpIfName.setStatus("current")


class _UsdIpIfArpTimeout_Type(Unsigned32):
    """Custom type usdIpIfArpTimeout based on Unsigned32"""
    defaultValue = 21600


_UsdIpIfArpTimeout_Object = MibTableColumn
usdIpIfArpTimeout = _UsdIpIfArpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 18),
    _UsdIpIfArpTimeout_Type()
)
usdIpIfArpTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpIfArpTimeout.setStatus("current")


class _UsdIpIfAdminSpeed_Type(Unsigned32):
    """Custom type usdIpIfAdminSpeed based on Unsigned32"""
    defaultValue = 0


_UsdIpIfAdminSpeed_Object = MibTableColumn
usdIpIfAdminSpeed = _UsdIpIfAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 19),
    _UsdIpIfAdminSpeed_Type()
)
usdIpIfAdminSpeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpIfAdminSpeed.setStatus("current")


class _UsdIpIfMultipathMode_Type(Integer32):
    """Custom type usdIpIfMultipathMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hashed", 1),
          ("roundRobin", 2))
    )


_UsdIpIfMultipathMode_Type.__name__ = "Integer32"
_UsdIpIfMultipathMode_Object = MibTableColumn
usdIpIfMultipathMode = _UsdIpIfMultipathMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 20),
    _UsdIpIfMultipathMode_Type()
)
usdIpIfMultipathMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpIfMultipathMode.setStatus("current")


class _UsdIpIfSharedNhAddr_Type(IpAddress):
    """Custom type usdIpIfSharedNhAddr based on IpAddress"""
    defaultValue = 0


_UsdIpIfSharedNhAddr_Object = MibTableColumn
usdIpIfSharedNhAddr = _UsdIpIfSharedNhAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 21),
    _UsdIpIfSharedNhAddr_Type()
)
usdIpIfSharedNhAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpIfSharedNhAddr.setStatus("current")


class _UsdIpIfSharedNhRouterId_Type(Unsigned32):
    """Custom type usdIpIfSharedNhRouterId based on Unsigned32"""
    defaultValue = 0


_UsdIpIfSharedNhRouterId_Object = MibTableColumn
usdIpIfSharedNhRouterId = _UsdIpIfSharedNhRouterId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 22),
    _UsdIpIfSharedNhRouterId_Type()
)
usdIpIfSharedNhRouterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpIfSharedNhRouterId.setStatus("current")
_UsdIpIfPrimaryIpAddress_Type = IpAddress
_UsdIpIfPrimaryIpAddress_Object = MibTableColumn
usdIpIfPrimaryIpAddress = _UsdIpIfPrimaryIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 23),
    _UsdIpIfPrimaryIpAddress_Type()
)
usdIpIfPrimaryIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpIfPrimaryIpAddress.setStatus("current")
_UsdIpIfPrimaryIpMask_Type = IpAddress
_UsdIpIfPrimaryIpMask_Object = MibTableColumn
usdIpIfPrimaryIpMask = _UsdIpIfPrimaryIpMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 24),
    _UsdIpIfPrimaryIpMask_Type()
)
usdIpIfPrimaryIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpIfPrimaryIpMask.setStatus("current")


class _UsdIpIfOperDebounceTime_Type(Integer32):
    """Custom type usdIpIfOperDebounceTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_UsdIpIfOperDebounceTime_Type.__name__ = "Integer32"
_UsdIpIfOperDebounceTime_Object = MibTableColumn
usdIpIfOperDebounceTime = _UsdIpIfOperDebounceTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 25),
    _UsdIpIfOperDebounceTime_Type()
)
usdIpIfOperDebounceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpIfOperDebounceTime.setStatus("current")
if mibBuilder.loadTexts:
    usdIpIfOperDebounceTime.setUnits("milliseconds")
_UsdIpIfStatsTable_Object = MibTable
usdIpIfStatsTable = _UsdIpIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3)
)
if mibBuilder.loadTexts:
    usdIpIfStatsTable.setStatus("current")
_UsdIpIfStatsEntry_Object = MibTableRow
usdIpIfStatsEntry = _UsdIpIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3, 1)
)
usdIpIfStatsEntry.setIndexNames(
    (0, "Unisphere-Data-IP-MIB", "usdIpIfStatsIndex"),
)
if mibBuilder.loadTexts:
    usdIpIfStatsEntry.setStatus("current")
_UsdIpIfStatsIndex_Type = InterfaceIndex
_UsdIpIfStatsIndex_Object = MibTableColumn
usdIpIfStatsIndex = _UsdIpIfStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3, 1, 1),
    _UsdIpIfStatsIndex_Type()
)
usdIpIfStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIpIfStatsIndex.setStatus("current")
_UsdIpIfStatsInPackets_Type = Counter64
_UsdIpIfStatsInPackets_Object = MibTableColumn
usdIpIfStatsInPackets = _UsdIpIfStatsInPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3, 1, 2),
    _UsdIpIfStatsInPackets_Type()
)
usdIpIfStatsInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpIfStatsInPackets.setStatus("current")
_UsdIpIfStatsInOctets_Type = Counter64
_UsdIpIfStatsInOctets_Object = MibTableColumn
usdIpIfStatsInOctets = _UsdIpIfStatsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3, 1, 3),
    _UsdIpIfStatsInOctets_Type()
)
usdIpIfStatsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpIfStatsInOctets.setStatus("current")
_UsdIpIfStatsInPoliciedPackets_Type = Counter64
_UsdIpIfStatsInPoliciedPackets_Object = MibTableColumn
usdIpIfStatsInPoliciedPackets = _UsdIpIfStatsInPoliciedPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3, 1, 4),
    _UsdIpIfStatsInPoliciedPackets_Type()
)
usdIpIfStatsInPoliciedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpIfStatsInPoliciedPackets.setStatus("current")
_UsdIpIfStatsInPoliciedOctets_Type = Counter64
_UsdIpIfStatsInPoliciedOctets_Object = MibTableColumn
usdIpIfStatsInPoliciedOctets = _UsdIpIfStatsInPoliciedOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3, 1, 5),
    _UsdIpIfStatsInPoliciedOctets_Type()
)
usdIpIfStatsInPoliciedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpIfStatsInPoliciedOctets.setStatus("current")
_UsdIpIfStatsInErrorPackets_Type = Counter64
_UsdIpIfStatsInErrorPackets_Object = MibTableColumn
usdIpIfStatsInErrorPackets = _UsdIpIfStatsInErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3, 1, 6),
    _UsdIpIfStatsInErrorPackets_Type()
)
usdIpIfStatsInErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpIfStatsInErrorPackets.setStatus("current")
_UsdIpIfStatsInSpoofedPackets_Type = Counter64
_UsdIpIfStatsInSpoofedPackets_Object = MibTableColumn
usdIpIfStatsInSpoofedPackets = _UsdIpIfStatsInSpoofedPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3, 1, 7),
    _UsdIpIfStatsInSpoofedPackets_Type()
)
usdIpIfStatsInSpoofedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpIfStatsInSpoofedPackets.setStatus("current")
_UsdIpIfStatsInForwardedPackets_Type = Counter64
_UsdIpIfStatsInForwardedPackets_Object = MibTableColumn
usdIpIfStatsInForwardedPackets = _UsdIpIfStatsInForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3, 1, 8),
    _UsdIpIfStatsInForwardedPackets_Type()
)
usdIpIfStatsInForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpIfStatsInForwardedPackets.setStatus("obsolete")
_UsdIpIfStatsInForwardedOctets_Type = Counter64
_UsdIpIfStatsInForwardedOctets_Object = MibTableColumn
usdIpIfStatsInForwardedOctets = _UsdIpIfStatsInForwardedOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3, 1, 9),
    _UsdIpIfStatsInForwardedOctets_Type()
)
usdIpIfStatsInForwardedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpIfStatsInForwardedOctets.setStatus("obsolete")
_UsdIpIfStatsOutForwardedPackets_Type = Counter64
_UsdIpIfStatsOutForwardedPackets_Object = MibTableColumn
usdIpIfStatsOutForwardedPackets = _UsdIpIfStatsOutForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3, 1, 10),
    _UsdIpIfStatsOutForwardedPackets_Type()
)
usdIpIfStatsOutForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpIfStatsOutForwardedPackets.setStatus("current")
_UsdIpIfStatsOutForwardedOctets_Type = Counter64
_UsdIpIfStatsOutForwardedOctets_Object = MibTableColumn
usdIpIfStatsOutForwardedOctets = _UsdIpIfStatsOutForwardedOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3, 1, 11),
    _UsdIpIfStatsOutForwardedOctets_Type()
)
usdIpIfStatsOutForwardedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpIfStatsOutForwardedOctets.setStatus("current")
_UsdIpIfStatsOutSchedDropPackets_Type = Counter64
_UsdIpIfStatsOutSchedDropPackets_Object = MibTableColumn
usdIpIfStatsOutSchedDropPackets = _UsdIpIfStatsOutSchedDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3, 1, 12),
    _UsdIpIfStatsOutSchedDropPackets_Type()
)
usdIpIfStatsOutSchedDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpIfStatsOutSchedDropPackets.setStatus("current")
_UsdIpIfStatsOutSchedDropOctets_Type = Counter64
_UsdIpIfStatsOutSchedDropOctets_Object = MibTableColumn
usdIpIfStatsOutSchedDropOctets = _UsdIpIfStatsOutSchedDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3, 1, 13),
    _UsdIpIfStatsOutSchedDropOctets_Type()
)
usdIpIfStatsOutSchedDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpIfStatsOutSchedDropOctets.setStatus("current")
_UsdIpIfStatsOutRequestedPackets_Type = Counter64
_UsdIpIfStatsOutRequestedPackets_Object = MibTableColumn
usdIpIfStatsOutRequestedPackets = _UsdIpIfStatsOutRequestedPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3, 1, 14),
    _UsdIpIfStatsOutRequestedPackets_Type()
)
usdIpIfStatsOutRequestedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpIfStatsOutRequestedPackets.setStatus("obsolete")
_UsdIpIfStatsOutRequestedOctets_Type = Counter64
_UsdIpIfStatsOutRequestedOctets_Object = MibTableColumn
usdIpIfStatsOutRequestedOctets = _UsdIpIfStatsOutRequestedOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3, 1, 15),
    _UsdIpIfStatsOutRequestedOctets_Type()
)
usdIpIfStatsOutRequestedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpIfStatsOutRequestedOctets.setStatus("obsolete")
_UsdIpIfStatsOutPoliciedPackets_Type = Counter64
_UsdIpIfStatsOutPoliciedPackets_Object = MibTableColumn
usdIpIfStatsOutPoliciedPackets = _UsdIpIfStatsOutPoliciedPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3, 1, 16),
    _UsdIpIfStatsOutPoliciedPackets_Type()
)
usdIpIfStatsOutPoliciedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpIfStatsOutPoliciedPackets.setStatus("current")
_UsdIpIfStatsOutPoliciedOctets_Type = Counter64
_UsdIpIfStatsOutPoliciedOctets_Object = MibTableColumn
usdIpIfStatsOutPoliciedOctets = _UsdIpIfStatsOutPoliciedOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3, 1, 17),
    _UsdIpIfStatsOutPoliciedOctets_Type()
)
usdIpIfStatsOutPoliciedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpIfStatsOutPoliciedOctets.setStatus("current")
_UsdIpIfStatsGreenOutSchedDropPackets_Type = Counter64
_UsdIpIfStatsGreenOutSchedDropPackets_Object = MibTableColumn
usdIpIfStatsGreenOutSchedDropPackets = _UsdIpIfStatsGreenOutSchedDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3, 1, 18),
    _UsdIpIfStatsGreenOutSchedDropPackets_Type()
)
usdIpIfStatsGreenOutSchedDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpIfStatsGreenOutSchedDropPackets.setStatus("deprecated")
_UsdIpIfStatsYellowOutSchedDropPackets_Type = Counter64
_UsdIpIfStatsYellowOutSchedDropPackets_Object = MibTableColumn
usdIpIfStatsYellowOutSchedDropPackets = _UsdIpIfStatsYellowOutSchedDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3, 1, 19),
    _UsdIpIfStatsYellowOutSchedDropPackets_Type()
)
usdIpIfStatsYellowOutSchedDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpIfStatsYellowOutSchedDropPackets.setStatus("deprecated")
_UsdIpIfStatsRedOutSchedDropPackets_Type = Counter64
_UsdIpIfStatsRedOutSchedDropPackets_Object = MibTableColumn
usdIpIfStatsRedOutSchedDropPackets = _UsdIpIfStatsRedOutSchedDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3, 1, 20),
    _UsdIpIfStatsRedOutSchedDropPackets_Type()
)
usdIpIfStatsRedOutSchedDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpIfStatsRedOutSchedDropPackets.setStatus("deprecated")
_UsdIpIfStatsGreenOutSchedDropOctets_Type = Counter64
_UsdIpIfStatsGreenOutSchedDropOctets_Object = MibTableColumn
usdIpIfStatsGreenOutSchedDropOctets = _UsdIpIfStatsGreenOutSchedDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3, 1, 21),
    _UsdIpIfStatsGreenOutSchedDropOctets_Type()
)
usdIpIfStatsGreenOutSchedDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpIfStatsGreenOutSchedDropOctets.setStatus("deprecated")
_UsdIpIfStatsYellowOutSchedDropOctets_Type = Counter64
_UsdIpIfStatsYellowOutSchedDropOctets_Object = MibTableColumn
usdIpIfStatsYellowOutSchedDropOctets = _UsdIpIfStatsYellowOutSchedDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3, 1, 22),
    _UsdIpIfStatsYellowOutSchedDropOctets_Type()
)
usdIpIfStatsYellowOutSchedDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpIfStatsYellowOutSchedDropOctets.setStatus("deprecated")
_UsdIpIfStatsRedOutSchedDropOctets_Type = Counter64
_UsdIpIfStatsRedOutSchedDropOctets_Object = MibTableColumn
usdIpIfStatsRedOutSchedDropOctets = _UsdIpIfStatsRedOutSchedDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3, 1, 23),
    _UsdIpIfStatsRedOutSchedDropOctets_Type()
)
usdIpIfStatsRedOutSchedDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpIfStatsRedOutSchedDropOctets.setStatus("deprecated")
_UsdIpIfAssocTable_Object = MibTable
usdIpIfAssocTable = _UsdIpIfAssocTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 4)
)
if mibBuilder.loadTexts:
    usdIpIfAssocTable.setStatus("current")
_UsdIpIfAssocEntry_Object = MibTableRow
usdIpIfAssocEntry = _UsdIpIfAssocEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 4, 1)
)
usdIpIfAssocEntry.setIndexNames(
    (0, "Unisphere-Data-IP-MIB", "usdIpIfAssocLowerIfIndex"),
)
if mibBuilder.loadTexts:
    usdIpIfAssocEntry.setStatus("current")
_UsdIpIfAssocLowerIfIndex_Type = InterfaceIndex
_UsdIpIfAssocLowerIfIndex_Object = MibTableColumn
usdIpIfAssocLowerIfIndex = _UsdIpIfAssocLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 4, 1, 1),
    _UsdIpIfAssocLowerIfIndex_Type()
)
usdIpIfAssocLowerIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIpIfAssocLowerIfIndex.setStatus("current")
_UsdIpIfAssocIpIfIndex_Type = InterfaceIndexOrZero
_UsdIpIfAssocIpIfIndex_Object = MibTableColumn
usdIpIfAssocIpIfIndex = _UsdIpIfAssocIpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 4, 1, 2),
    _UsdIpIfAssocIpIfIndex_Type()
)
usdIpIfAssocIpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpIfAssocIpIfIndex.setStatus("current")
_UsdIpAddress_ObjectIdentity = ObjectIdentity
usdIpAddress = _UsdIpAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2)
)
_UsdIpAddrGlobals_ObjectIdentity = ObjectIdentity
usdIpAddrGlobals = _UsdIpAddrGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 1)
)


class _UsdIpArpTimeout_Type(Integer32):
    """Custom type usdIpArpTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_UsdIpArpTimeout_Type.__name__ = "Integer32"
_UsdIpArpTimeout_Object = MibScalar
usdIpArpTimeout = _UsdIpArpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 1, 1),
    _UsdIpArpTimeout_Type()
)
usdIpArpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIpArpTimeout.setStatus("current")
if mibBuilder.loadTexts:
    usdIpArpTimeout.setUnits("seconds")
_UsdIpAddrTable_Object = MibTable
usdIpAddrTable = _UsdIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 2)
)
if mibBuilder.loadTexts:
    usdIpAddrTable.setStatus("current")
_UsdIpAddrEntry_Object = MibTableRow
usdIpAddrEntry = _UsdIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 2, 1)
)
usdIpAddrEntry.setIndexNames(
    (0, "Unisphere-Data-IP-MIB", "usdIpAdEntAddr"),
)
if mibBuilder.loadTexts:
    usdIpAddrEntry.setStatus("current")
_UsdIpAdEntAddr_Type = UsdIpAddrLessIf
_UsdIpAdEntAddr_Object = MibTableColumn
usdIpAdEntAddr = _UsdIpAdEntAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 2, 1, 1),
    _UsdIpAdEntAddr_Type()
)
usdIpAdEntAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIpAdEntAddr.setStatus("current")
_UsdIpAdEntIfIndex_Type = InterfaceIndex
_UsdIpAdEntIfIndex_Object = MibTableColumn
usdIpAdEntIfIndex = _UsdIpAdEntIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 2, 1, 2),
    _UsdIpAdEntIfIndex_Type()
)
usdIpAdEntIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpAdEntIfIndex.setStatus("current")


class _UsdIpAdEntNetMask_Type(IpAddress):
    """Custom type usdIpAdEntNetMask based on IpAddress"""
    defaultHexValue = "ffffffff"


_UsdIpAdEntNetMask_Object = MibTableColumn
usdIpAdEntNetMask = _UsdIpAdEntNetMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 2, 1, 3),
    _UsdIpAdEntNetMask_Type()
)
usdIpAdEntNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpAdEntNetMask.setStatus("current")


class _UsdIpAdEntBcastAddr_Type(Integer32):
    """Custom type usdIpAdEntBcastAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_UsdIpAdEntBcastAddr_Type.__name__ = "Integer32"
_UsdIpAdEntBcastAddr_Object = MibTableColumn
usdIpAdEntBcastAddr = _UsdIpAdEntBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 2, 1, 4),
    _UsdIpAdEntBcastAddr_Type()
)
usdIpAdEntBcastAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpAdEntBcastAddr.setStatus("current")


class _UsdIpAdEntReasmMaxSize_Type(Integer32):
    """Custom type usdIpAdEntReasmMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdIpAdEntReasmMaxSize_Type.__name__ = "Integer32"
_UsdIpAdEntReasmMaxSize_Object = MibTableColumn
usdIpAdEntReasmMaxSize = _UsdIpAdEntReasmMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 2, 1, 5),
    _UsdIpAdEntReasmMaxSize_Type()
)
usdIpAdEntReasmMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpAdEntReasmMaxSize.setStatus("current")
_UsdIpAdEntRowStatus_Type = RowStatus
_UsdIpAdEntRowStatus_Object = MibTableColumn
usdIpAdEntRowStatus = _UsdIpAdEntRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 2, 1, 6),
    _UsdIpAdEntRowStatus_Type()
)
usdIpAdEntRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpAdEntRowStatus.setStatus("current")


class _UsdIpAdEntAdminStatus_Type(UsdEnable):
    """Custom type usdIpAdEntAdminStatus based on UsdEnable"""


_UsdIpAdEntAdminStatus_Object = MibTableColumn
usdIpAdEntAdminStatus = _UsdIpAdEntAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 2, 1, 7),
    _UsdIpAdEntAdminStatus_Type()
)
usdIpAdEntAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpAdEntAdminStatus.setStatus("current")


class _UsdIpAdEntArpRspEnable_Type(UsdEnable):
    """Custom type usdIpAdEntArpRspEnable based on UsdEnable"""


_UsdIpAdEntArpRspEnable_Object = MibTableColumn
usdIpAdEntArpRspEnable = _UsdIpAdEntArpRspEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 2, 1, 8),
    _UsdIpAdEntArpRspEnable_Type()
)
usdIpAdEntArpRspEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpAdEntArpRspEnable.setStatus("current")


class _UsdIpAdEntProxyArpRspEnable_Type(UsdEnable):
    """Custom type usdIpAdEntProxyArpRspEnable based on UsdEnable"""


_UsdIpAdEntProxyArpRspEnable_Object = MibTableColumn
usdIpAdEntProxyArpRspEnable = _UsdIpAdEntProxyArpRspEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 2, 1, 9),
    _UsdIpAdEntProxyArpRspEnable_Type()
)
usdIpAdEntProxyArpRspEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpAdEntProxyArpRspEnable.setStatus("current")


class _UsdIpAdEntIgmpEnable_Type(UsdEnable):
    """Custom type usdIpAdEntIgmpEnable based on UsdEnable"""


_UsdIpAdEntIgmpEnable_Object = MibTableColumn
usdIpAdEntIgmpEnable = _UsdIpAdEntIgmpEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 2, 1, 10),
    _UsdIpAdEntIgmpEnable_Type()
)
usdIpAdEntIgmpEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpAdEntIgmpEnable.setStatus("deprecated")


class _UsdIpAdEntDirectedBcastEnable_Type(UsdEnable):
    """Custom type usdIpAdEntDirectedBcastEnable based on UsdEnable"""


_UsdIpAdEntDirectedBcastEnable_Object = MibTableColumn
usdIpAdEntDirectedBcastEnable = _UsdIpAdEntDirectedBcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 2, 1, 11),
    _UsdIpAdEntDirectedBcastEnable_Type()
)
usdIpAdEntDirectedBcastEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpAdEntDirectedBcastEnable.setStatus("current")


class _UsdIpAdEntIcmpRedirectEnable_Type(UsdEnable):
    """Custom type usdIpAdEntIcmpRedirectEnable based on UsdEnable"""


_UsdIpAdEntIcmpRedirectEnable_Object = MibTableColumn
usdIpAdEntIcmpRedirectEnable = _UsdIpAdEntIcmpRedirectEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 2, 1, 12),
    _UsdIpAdEntIcmpRedirectEnable_Type()
)
usdIpAdEntIcmpRedirectEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpAdEntIcmpRedirectEnable.setStatus("current")


class _UsdIpAdEntIcmpMaskReplyEnable_Type(UsdEnable):
    """Custom type usdIpAdEntIcmpMaskReplyEnable based on UsdEnable"""


_UsdIpAdEntIcmpMaskReplyEnable_Object = MibTableColumn
usdIpAdEntIcmpMaskReplyEnable = _UsdIpAdEntIcmpMaskReplyEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 2, 1, 13),
    _UsdIpAdEntIcmpMaskReplyEnable_Type()
)
usdIpAdEntIcmpMaskReplyEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpAdEntIcmpMaskReplyEnable.setStatus("current")


class _UsdIpAdEntIcmpUnreachEnable_Type(UsdEnable):
    """Custom type usdIpAdEntIcmpUnreachEnable based on UsdEnable"""


_UsdIpAdEntIcmpUnreachEnable_Object = MibTableColumn
usdIpAdEntIcmpUnreachEnable = _UsdIpAdEntIcmpUnreachEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 2, 1, 14),
    _UsdIpAdEntIcmpUnreachEnable_Type()
)
usdIpAdEntIcmpUnreachEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpAdEntIcmpUnreachEnable.setStatus("current")


class _UsdIpAdEntMtu_Type(Integer32):
    """Custom type usdIpAdEntMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdIpAdEntMtu_Type.__name__ = "Integer32"
_UsdIpAdEntMtu_Object = MibTableColumn
usdIpAdEntMtu = _UsdIpAdEntMtu_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 2, 1, 15),
    _UsdIpAdEntMtu_Type()
)
usdIpAdEntMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpAdEntMtu.setStatus("current")


class _UsdIpAdEntUnnumLoopbackIfIndex_Type(InterfaceIndexOrZero):
    """Custom type usdIpAdEntUnnumLoopbackIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_UsdIpAdEntUnnumLoopbackIfIndex_Object = MibTableColumn
usdIpAdEntUnnumLoopbackIfIndex = _UsdIpAdEntUnnumLoopbackIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 2, 1, 16),
    _UsdIpAdEntUnnumLoopbackIfIndex_Type()
)
usdIpAdEntUnnumLoopbackIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpAdEntUnnumLoopbackIfIndex.setStatus("current")


class _UsdIpAdEntIrdpEnable_Type(UsdEnable):
    """Custom type usdIpAdEntIrdpEnable based on UsdEnable"""


_UsdIpAdEntIrdpEnable_Object = MibTableColumn
usdIpAdEntIrdpEnable = _UsdIpAdEntIrdpEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 2, 1, 17),
    _UsdIpAdEntIrdpEnable_Type()
)
usdIpAdEntIrdpEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpAdEntIrdpEnable.setStatus("current")


class _UsdIpAdEntAccessRouteEnable_Type(UsdEnable):
    """Custom type usdIpAdEntAccessRouteEnable based on UsdEnable"""


_UsdIpAdEntAccessRouteEnable_Object = MibTableColumn
usdIpAdEntAccessRouteEnable = _UsdIpAdEntAccessRouteEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 2, 1, 18),
    _UsdIpAdEntAccessRouteEnable_Type()
)
usdIpAdEntAccessRouteEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpAdEntAccessRouteEnable.setStatus("current")
_UsdIpAdEntAccessRouteHost_Type = IpAddress
_UsdIpAdEntAccessRouteHost_Object = MibTableColumn
usdIpAdEntAccessRouteHost = _UsdIpAdEntAccessRouteHost_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 2, 1, 19),
    _UsdIpAdEntAccessRouteHost_Type()
)
usdIpAdEntAccessRouteHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpAdEntAccessRouteHost.setStatus("current")


class _UsdIpAdEntIsSecondary_Type(UsdEnable):
    """Custom type usdIpAdEntIsSecondary based on UsdEnable"""


_UsdIpAdEntIsSecondary_Object = MibTableColumn
usdIpAdEntIsSecondary = _UsdIpAdEntIsSecondary_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 2, 1, 20),
    _UsdIpAdEntIsSecondary_Type()
)
usdIpAdEntIsSecondary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpAdEntIsSecondary.setStatus("current")
_UsdIpRoute_ObjectIdentity = ObjectIdentity
usdIpRoute = _UsdIpRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3)
)
_UsdIpRouteGlobals_ObjectIdentity = ObjectIdentity
usdIpRouteGlobals = _UsdIpRouteGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3, 1)
)
_UsdIpRouteLimit_Type = Integer32
_UsdIpRouteLimit_Object = MibScalar
usdIpRouteLimit = _UsdIpRouteLimit_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3, 1, 1),
    _UsdIpRouteLimit_Type()
)
usdIpRouteLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIpRouteLimit.setStatus("current")
_UsdIpRouteStaticTable_Object = MibTable
usdIpRouteStaticTable = _UsdIpRouteStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3, 2)
)
if mibBuilder.loadTexts:
    usdIpRouteStaticTable.setStatus("current")
_UsdIpRouteStaticEntry_Object = MibTableRow
usdIpRouteStaticEntry = _UsdIpRouteStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3, 2, 1)
)
usdIpRouteStaticEntry.setIndexNames(
    (0, "Unisphere-Data-IP-MIB", "usdIpRouteStaticDest"),
    (0, "Unisphere-Data-IP-MIB", "usdIpRouteStaticMask"),
    (0, "Unisphere-Data-IP-MIB", "usdIpRouteStaticPref"),
    (0, "Unisphere-Data-IP-MIB", "usdIpRouteStaticNextHop"),
)
if mibBuilder.loadTexts:
    usdIpRouteStaticEntry.setStatus("current")
_UsdIpRouteStaticDest_Type = IpAddress
_UsdIpRouteStaticDest_Object = MibTableColumn
usdIpRouteStaticDest = _UsdIpRouteStaticDest_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3, 2, 1, 1),
    _UsdIpRouteStaticDest_Type()
)
usdIpRouteStaticDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpRouteStaticDest.setStatus("current")
_UsdIpRouteStaticMask_Type = IpAddress
_UsdIpRouteStaticMask_Object = MibTableColumn
usdIpRouteStaticMask = _UsdIpRouteStaticMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3, 2, 1, 2),
    _UsdIpRouteStaticMask_Type()
)
usdIpRouteStaticMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpRouteStaticMask.setStatus("current")


class _UsdIpRouteStaticPref_Type(Integer32):
    """Custom type usdIpRouteStaticPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UsdIpRouteStaticPref_Type.__name__ = "Integer32"
_UsdIpRouteStaticPref_Object = MibTableColumn
usdIpRouteStaticPref = _UsdIpRouteStaticPref_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3, 2, 1, 3),
    _UsdIpRouteStaticPref_Type()
)
usdIpRouteStaticPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpRouteStaticPref.setStatus("current")
_UsdIpRouteStaticNextHop_Type = UsdIpAddrLessIf
_UsdIpRouteStaticNextHop_Object = MibTableColumn
usdIpRouteStaticNextHop = _UsdIpRouteStaticNextHop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3, 2, 1, 4),
    _UsdIpRouteStaticNextHop_Type()
)
usdIpRouteStaticNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpRouteStaticNextHop.setStatus("current")
_UsdIpRouteStaticRowStatus_Type = RowStatus
_UsdIpRouteStaticRowStatus_Object = MibTableColumn
usdIpRouteStaticRowStatus = _UsdIpRouteStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3, 2, 1, 5),
    _UsdIpRouteStaticRowStatus_Type()
)
usdIpRouteStaticRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpRouteStaticRowStatus.setStatus("current")


class _UsdIpRouteStaticIfIndex_Type(Integer32):
    """Custom type usdIpRouteStaticIfIndex based on Integer32"""
    defaultValue = 0


_UsdIpRouteStaticIfIndex_Object = MibTableColumn
usdIpRouteStaticIfIndex = _UsdIpRouteStaticIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3, 2, 1, 6),
    _UsdIpRouteStaticIfIndex_Type()
)
usdIpRouteStaticIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpRouteStaticIfIndex.setStatus("current")


class _UsdIpRouteStaticStatus_Type(Integer32):
    """Custom type usdIpRouteStaticStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("inactive", 1),
          ("incomplete", 2))
    )


_UsdIpRouteStaticStatus_Type.__name__ = "Integer32"
_UsdIpRouteStaticStatus_Object = MibTableColumn
usdIpRouteStaticStatus = _UsdIpRouteStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3, 2, 1, 7),
    _UsdIpRouteStaticStatus_Type()
)
usdIpRouteStaticStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpRouteStaticStatus.setStatus("current")


class _UsdIpRouteStaticNextHopAS_Type(Integer32):
    """Custom type usdIpRouteStaticNextHopAS based on Integer32"""
    defaultValue = 0


_UsdIpRouteStaticNextHopAS_Object = MibTableColumn
usdIpRouteStaticNextHopAS = _UsdIpRouteStaticNextHopAS_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3, 2, 1, 8),
    _UsdIpRouteStaticNextHopAS_Type()
)
usdIpRouteStaticNextHopAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpRouteStaticNextHopAS.setStatus("current")


class _UsdIpRouteStaticMetric_Type(Integer32):
    """Custom type usdIpRouteStaticMetric based on Integer32"""
    defaultValue = -1


_UsdIpRouteStaticMetric_Object = MibTableColumn
usdIpRouteStaticMetric = _UsdIpRouteStaticMetric_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3, 2, 1, 9),
    _UsdIpRouteStaticMetric_Type()
)
usdIpRouteStaticMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpRouteStaticMetric.setStatus("current")


class _UsdIpRouteStaticTag_Type(Unsigned32):
    """Custom type usdIpRouteStaticTag based on Unsigned32"""
    defaultValue = 0


_UsdIpRouteStaticTag_Object = MibTableColumn
usdIpRouteStaticTag = _UsdIpRouteStaticTag_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3, 2, 1, 10),
    _UsdIpRouteStaticTag_Type()
)
usdIpRouteStaticTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpRouteStaticTag.setStatus("current")
_UsdIpCidrRouteTable_Object = MibTable
usdIpCidrRouteTable = _UsdIpCidrRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3, 3)
)
if mibBuilder.loadTexts:
    usdIpCidrRouteTable.setStatus("current")
_UsdIpCidrRouteEntry_Object = MibTableRow
usdIpCidrRouteEntry = _UsdIpCidrRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    usdIpCidrRouteEntry.setStatus("current")


class _UsdIpCidrRoutePref_Type(Integer32):
    """Custom type usdIpCidrRoutePref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UsdIpCidrRoutePref_Type.__name__ = "Integer32"
_UsdIpCidrRoutePref_Object = MibTableColumn
usdIpCidrRoutePref = _UsdIpCidrRoutePref_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3, 3, 1, 1),
    _UsdIpCidrRoutePref_Type()
)
usdIpCidrRoutePref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpCidrRoutePref.setStatus("current")
_UsdIpCidrRouteArea_Type = IpAddress
_UsdIpCidrRouteArea_Object = MibTableColumn
usdIpCidrRouteArea = _UsdIpCidrRouteArea_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3, 3, 1, 2),
    _UsdIpCidrRouteArea_Type()
)
usdIpCidrRouteArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpCidrRouteArea.setStatus("current")
_UsdIpCidrRouteTag_Type = Unsigned32
_UsdIpCidrRouteTag_Object = MibTableColumn
usdIpCidrRouteTag = _UsdIpCidrRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3, 3, 1, 3),
    _UsdIpCidrRouteTag_Type()
)
usdIpCidrRouteTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpCidrRouteTag.setStatus("current")
_UsdIpGlobals_ObjectIdentity = ObjectIdentity
usdIpGlobals = _UsdIpGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 4)
)


class _UsdIpDebounceTime_Type(Integer32):
    """Custom type usdIpDebounceTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_UsdIpDebounceTime_Type.__name__ = "Integer32"
_UsdIpDebounceTime_Object = MibScalar
usdIpDebounceTime = _UsdIpDebounceTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 4, 1),
    _UsdIpDebounceTime_Type()
)
usdIpDebounceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIpDebounceTime.setStatus("current")
if mibBuilder.loadTexts:
    usdIpDebounceTime.setUnits("milliseconds")
_UsdIpRouterId_Type = IpAddress
_UsdIpRouterId_Object = MibScalar
usdIpRouterId = _UsdIpRouterId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 4, 2),
    _UsdIpRouterId_Type()
)
usdIpRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIpRouterId.setStatus("current")
_UsdIpSourceRoutingAdminStatus_Type = UsdEnable
_UsdIpSourceRoutingAdminStatus_Object = MibScalar
usdIpSourceRoutingAdminStatus = _UsdIpSourceRoutingAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 4, 3),
    _UsdIpSourceRoutingAdminStatus_Type()
)
usdIpSourceRoutingAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIpSourceRoutingAdminStatus.setStatus("current")


class _UsdIpVpnIdOui_Type(Integer32):
    """Custom type usdIpVpnIdOui based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_UsdIpVpnIdOui_Type.__name__ = "Integer32"
_UsdIpVpnIdOui_Object = MibScalar
usdIpVpnIdOui = _UsdIpVpnIdOui_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 4, 4),
    _UsdIpVpnIdOui_Type()
)
usdIpVpnIdOui.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIpVpnIdOui.setStatus("current")
_UsdIpVpnIdIndex_Type = IpAddress
_UsdIpVpnIdIndex_Object = MibScalar
usdIpVpnIdIndex = _UsdIpVpnIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 4, 5),
    _UsdIpVpnIdIndex_Type()
)
usdIpVpnIdIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdIpVpnIdIndex.setStatus("current")
_UsdIpConformance_ObjectIdentity = ObjectIdentity
usdIpConformance = _UsdIpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4)
)
_UsdIpCompliances_ObjectIdentity = ObjectIdentity
usdIpCompliances = _UsdIpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 1)
)
_UsdIpGroups_ObjectIdentity = ObjectIdentity
usdIpGroups = _UsdIpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 2)
)
ipCidrRouteEntry.registerAugmentions(
    ("Unisphere-Data-IP-MIB",
     "usdIpCidrRouteEntry")
)
usdIpCidrRouteEntry.setIndexNames(*ipCidrRouteEntry.getIndexNames())

# Managed Objects groups

usdIpInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 2, 1)
)
usdIpInterfaceGroup.setObjects(
      *(("Unisphere-Data-IP-MIB", "usdIpNextIfIndex"),
        ("Unisphere-Data-IP-MIB", "usdIpIfRowStatus"),
        ("Unisphere-Data-IP-MIB", "usdIpIfLowerIfIndex"),
        ("Unisphere-Data-IP-MIB", "usdIpIfType"),
        ("Unisphere-Data-IP-MIB", "usdIpIfTypeId"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsInPackets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsInOctets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsInPoliciedPackets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsInPoliciedOctets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsInErrorPackets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsInSpoofedPackets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsInForwardedPackets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsInForwardedOctets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsOutForwardedPackets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsOutForwardedOctets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsOutSchedDropPackets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsOutSchedDropOctets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsOutRequestedPackets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsOutRequestedOctets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsOutPoliciedPackets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsOutPoliciedOctets"))
)
if mibBuilder.loadTexts:
    usdIpInterfaceGroup.setStatus("obsolete")

usdIpAddressGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 2, 2)
)
usdIpAddressGroup.setObjects(
      *(("Unisphere-Data-IP-MIB", "usdIpArpTimeout"),
        ("Unisphere-Data-IP-MIB", "usdIpAdEntRowStatus"),
        ("Unisphere-Data-IP-MIB", "usdIpAdEntIfIndex"),
        ("Unisphere-Data-IP-MIB", "usdIpAdEntNetMask"),
        ("Unisphere-Data-IP-MIB", "usdIpAdEntAdminStatus"),
        ("Unisphere-Data-IP-MIB", "usdIpAdEntArpRspEnable"),
        ("Unisphere-Data-IP-MIB", "usdIpAdEntProxyArpRspEnable"),
        ("Unisphere-Data-IP-MIB", "usdIpAdEntIgmpEnable"),
        ("Unisphere-Data-IP-MIB", "usdIpAdEntDirectedBcastEnable"),
        ("Unisphere-Data-IP-MIB", "usdIpAdEntIcmpRedirectEnable"),
        ("Unisphere-Data-IP-MIB", "usdIpAdEntIcmpMaskReplyEnable"),
        ("Unisphere-Data-IP-MIB", "usdIpAdEntIcmpUnreachEnable"),
        ("Unisphere-Data-IP-MIB", "usdIpAdEntMtu"),
        ("Unisphere-Data-IP-MIB", "usdIpAdEntUnnumLoopbackIfIndex"),
        ("Unisphere-Data-IP-MIB", "usdIpAdEntIrdpEnable"),
        ("Unisphere-Data-IP-MIB", "usdIpAdEntAccessRouteEnable"),
        ("Unisphere-Data-IP-MIB", "usdIpAdEntAccessRouteHost"))
)
if mibBuilder.loadTexts:
    usdIpAddressGroup.setStatus("obsolete")

usdIpRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 2, 3)
)
usdIpRouteGroup.setObjects(
      *(("Unisphere-Data-IP-MIB", "usdIpRouteLimit"),
        ("Unisphere-Data-IP-MIB", "usdIpRouteStaticDest"),
        ("Unisphere-Data-IP-MIB", "usdIpRouteStaticMask"),
        ("Unisphere-Data-IP-MIB", "usdIpRouteStaticPref"),
        ("Unisphere-Data-IP-MIB", "usdIpRouteStaticNextHop"),
        ("Unisphere-Data-IP-MIB", "usdIpRouteStaticRowStatus"),
        ("Unisphere-Data-IP-MIB", "usdIpRouteStaticIfIndex"),
        ("Unisphere-Data-IP-MIB", "usdIpRouteStaticStatus"),
        ("Unisphere-Data-IP-MIB", "usdIpRouteStaticNextHopAS"),
        ("Unisphere-Data-IP-MIB", "usdIpRouteStaticMetric"),
        ("Unisphere-Data-IP-MIB", "usdIpRouteStaticTag"),
        ("Unisphere-Data-IP-MIB", "usdIpCidrRoutePref"),
        ("Unisphere-Data-IP-MIB", "usdIpCidrRouteArea"),
        ("Unisphere-Data-IP-MIB", "usdIpCidrRouteTag"))
)
if mibBuilder.loadTexts:
    usdIpRouteGroup.setStatus("current")

usdIpGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 2, 4)
)
usdIpGlobalGroup.setObjects(
      *(("Unisphere-Data-IP-MIB", "usdIpDebounceTime"),
        ("Unisphere-Data-IP-MIB", "usdIpRouterId"),
        ("Unisphere-Data-IP-MIB", "usdIpSourceRoutingAdminStatus"),
        ("Unisphere-Data-IP-MIB", "usdIpVpnIdOui"),
        ("Unisphere-Data-IP-MIB", "usdIpVpnIdIndex"))
)
if mibBuilder.loadTexts:
    usdIpGlobalGroup.setStatus("current")

usdIpInterfaceGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 2, 5)
)
usdIpInterfaceGroup2.setObjects(
      *(("Unisphere-Data-IP-MIB", "usdIpNextIfIndex"),
        ("Unisphere-Data-IP-MIB", "usdIpIfRowStatus"),
        ("Unisphere-Data-IP-MIB", "usdIpIfLowerIfIndex"),
        ("Unisphere-Data-IP-MIB", "usdIpIfType"),
        ("Unisphere-Data-IP-MIB", "usdIpIfTypeId"),
        ("Unisphere-Data-IP-MIB", "usdIpIfSAValidationEnable"),
        ("Unisphere-Data-IP-MIB", "usdIpIfCreationType"),
        ("Unisphere-Data-IP-MIB", "usdIpIfProfileId"),
        ("Unisphere-Data-IP-MIB", "usdIpIfAlwaysUp"),
        ("Unisphere-Data-IP-MIB", "usdIpIfLoopback"),
        ("Unisphere-Data-IP-MIB", "usdIpIfLoopbackUid"),
        ("Unisphere-Data-IP-MIB", "usdIpIfDebounceTime"),
        ("Unisphere-Data-IP-MIB", "usdIpIfForwarding"),
        ("Unisphere-Data-IP-MIB", "usdIpIfForceFragmentation"),
        ("Unisphere-Data-IP-MIB", "usdIpIfSharesLowerUid"),
        ("Unisphere-Data-IP-MIB", "usdIpIfFilterOptions"),
        ("Unisphere-Data-IP-MIB", "usdIpIfName"),
        ("Unisphere-Data-IP-MIB", "usdIpIfArpTimeout"),
        ("Unisphere-Data-IP-MIB", "usdIpIfAdminSpeed"),
        ("Unisphere-Data-IP-MIB", "usdIpIfMultipathMode"),
        ("Unisphere-Data-IP-MIB", "usdIpIfSharedNhAddr"),
        ("Unisphere-Data-IP-MIB", "usdIpIfSharedNhRouterId"),
        ("Unisphere-Data-IP-MIB", "usdIpIfPrimaryIpAddress"),
        ("Unisphere-Data-IP-MIB", "usdIpIfPrimaryIpMask"),
        ("Unisphere-Data-IP-MIB", "usdIpIfOperDebounceTime"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsInPackets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsInOctets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsInPoliciedPackets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsInPoliciedOctets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsInErrorPackets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsInSpoofedPackets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsInForwardedPackets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsInForwardedOctets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsOutForwardedPackets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsOutForwardedOctets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsOutSchedDropPackets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsOutSchedDropOctets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsOutRequestedPackets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsOutRequestedOctets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsOutPoliciedPackets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsOutPoliciedOctets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsGreenOutSchedDropPackets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsYellowOutSchedDropPackets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsRedOutSchedDropPackets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsGreenOutSchedDropOctets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsYellowOutSchedDropOctets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsRedOutSchedDropOctets"))
)
if mibBuilder.loadTexts:
    usdIpInterfaceGroup2.setStatus("obsolete")

usdIpAddressGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 2, 6)
)
usdIpAddressGroup2.setObjects(
      *(("Unisphere-Data-IP-MIB", "usdIpArpTimeout"),
        ("Unisphere-Data-IP-MIB", "usdIpAdEntRowStatus"),
        ("Unisphere-Data-IP-MIB", "usdIpAdEntIfIndex"),
        ("Unisphere-Data-IP-MIB", "usdIpAdEntNetMask"),
        ("Unisphere-Data-IP-MIB", "usdIpAdEntBcastAddr"),
        ("Unisphere-Data-IP-MIB", "usdIpAdEntReasmMaxSize"),
        ("Unisphere-Data-IP-MIB", "usdIpAdEntAdminStatus"),
        ("Unisphere-Data-IP-MIB", "usdIpAdEntArpRspEnable"),
        ("Unisphere-Data-IP-MIB", "usdIpAdEntProxyArpRspEnable"),
        ("Unisphere-Data-IP-MIB", "usdIpAdEntDirectedBcastEnable"),
        ("Unisphere-Data-IP-MIB", "usdIpAdEntIcmpRedirectEnable"),
        ("Unisphere-Data-IP-MIB", "usdIpAdEntIcmpMaskReplyEnable"),
        ("Unisphere-Data-IP-MIB", "usdIpAdEntIcmpUnreachEnable"),
        ("Unisphere-Data-IP-MIB", "usdIpAdEntMtu"),
        ("Unisphere-Data-IP-MIB", "usdIpAdEntUnnumLoopbackIfIndex"),
        ("Unisphere-Data-IP-MIB", "usdIpAdEntIrdpEnable"),
        ("Unisphere-Data-IP-MIB", "usdIpAdEntAccessRouteEnable"),
        ("Unisphere-Data-IP-MIB", "usdIpAdEntAccessRouteHost"),
        ("Unisphere-Data-IP-MIB", "usdIpAdEntIsSecondary"))
)
if mibBuilder.loadTexts:
    usdIpAddressGroup2.setStatus("current")

usdIpInterfaceGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 2, 7)
)
usdIpInterfaceGroup3.setObjects(
      *(("Unisphere-Data-IP-MIB", "usdIpNextIfIndex"),
        ("Unisphere-Data-IP-MIB", "usdIpIfRowStatus"),
        ("Unisphere-Data-IP-MIB", "usdIpIfLowerIfIndex"),
        ("Unisphere-Data-IP-MIB", "usdIpIfType"),
        ("Unisphere-Data-IP-MIB", "usdIpIfTypeId"),
        ("Unisphere-Data-IP-MIB", "usdIpIfSAValidationEnable"),
        ("Unisphere-Data-IP-MIB", "usdIpIfCreationType"),
        ("Unisphere-Data-IP-MIB", "usdIpIfProfileId"),
        ("Unisphere-Data-IP-MIB", "usdIpIfAlwaysUp"),
        ("Unisphere-Data-IP-MIB", "usdIpIfLoopback"),
        ("Unisphere-Data-IP-MIB", "usdIpIfLoopbackUid"),
        ("Unisphere-Data-IP-MIB", "usdIpIfDebounceTime"),
        ("Unisphere-Data-IP-MIB", "usdIpIfForwarding"),
        ("Unisphere-Data-IP-MIB", "usdIpIfForceFragmentation"),
        ("Unisphere-Data-IP-MIB", "usdIpIfSharesLowerUid"),
        ("Unisphere-Data-IP-MIB", "usdIpIfFilterOptions"),
        ("Unisphere-Data-IP-MIB", "usdIpIfName"),
        ("Unisphere-Data-IP-MIB", "usdIpIfArpTimeout"),
        ("Unisphere-Data-IP-MIB", "usdIpIfAdminSpeed"),
        ("Unisphere-Data-IP-MIB", "usdIpIfMultipathMode"),
        ("Unisphere-Data-IP-MIB", "usdIpIfSharedNhAddr"),
        ("Unisphere-Data-IP-MIB", "usdIpIfSharedNhRouterId"),
        ("Unisphere-Data-IP-MIB", "usdIpIfPrimaryIpAddress"),
        ("Unisphere-Data-IP-MIB", "usdIpIfPrimaryIpMask"),
        ("Unisphere-Data-IP-MIB", "usdIpIfOperDebounceTime"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsInPackets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsInOctets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsInPoliciedPackets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsInPoliciedOctets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsInErrorPackets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsInSpoofedPackets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsInForwardedPackets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsInForwardedOctets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsOutForwardedPackets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsOutForwardedOctets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsOutSchedDropPackets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsOutSchedDropOctets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsOutRequestedPackets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsOutRequestedOctets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsOutPoliciedPackets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsOutPoliciedOctets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsGreenOutSchedDropPackets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsYellowOutSchedDropPackets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsRedOutSchedDropPackets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsGreenOutSchedDropOctets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsYellowOutSchedDropOctets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsRedOutSchedDropOctets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfAssocIpIfIndex"))
)
if mibBuilder.loadTexts:
    usdIpInterfaceGroup3.setStatus("obsolete")

usdIpInterfaceGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 2, 8)
)
usdIpInterfaceGroup4.setObjects(
      *(("Unisphere-Data-IP-MIB", "usdIpNextIfIndex"),
        ("Unisphere-Data-IP-MIB", "usdIpIfRowStatus"),
        ("Unisphere-Data-IP-MIB", "usdIpIfLowerIfIndex"),
        ("Unisphere-Data-IP-MIB", "usdIpIfType"),
        ("Unisphere-Data-IP-MIB", "usdIpIfTypeId"),
        ("Unisphere-Data-IP-MIB", "usdIpIfSAValidationEnable"),
        ("Unisphere-Data-IP-MIB", "usdIpIfCreationType"),
        ("Unisphere-Data-IP-MIB", "usdIpIfProfileId"),
        ("Unisphere-Data-IP-MIB", "usdIpIfAlwaysUp"),
        ("Unisphere-Data-IP-MIB", "usdIpIfLoopback"),
        ("Unisphere-Data-IP-MIB", "usdIpIfLoopbackUid"),
        ("Unisphere-Data-IP-MIB", "usdIpIfDebounceTime"),
        ("Unisphere-Data-IP-MIB", "usdIpIfForwarding"),
        ("Unisphere-Data-IP-MIB", "usdIpIfForceFragmentation"),
        ("Unisphere-Data-IP-MIB", "usdIpIfSharesLowerUid"),
        ("Unisphere-Data-IP-MIB", "usdIpIfFilterOptions"),
        ("Unisphere-Data-IP-MIB", "usdIpIfName"),
        ("Unisphere-Data-IP-MIB", "usdIpIfArpTimeout"),
        ("Unisphere-Data-IP-MIB", "usdIpIfAdminSpeed"),
        ("Unisphere-Data-IP-MIB", "usdIpIfMultipathMode"),
        ("Unisphere-Data-IP-MIB", "usdIpIfSharedNhAddr"),
        ("Unisphere-Data-IP-MIB", "usdIpIfSharedNhRouterId"),
        ("Unisphere-Data-IP-MIB", "usdIpIfPrimaryIpAddress"),
        ("Unisphere-Data-IP-MIB", "usdIpIfPrimaryIpMask"),
        ("Unisphere-Data-IP-MIB", "usdIpIfOperDebounceTime"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsInPackets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsInOctets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsInPoliciedPackets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsInPoliciedOctets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsInErrorPackets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsInSpoofedPackets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsOutForwardedPackets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsOutForwardedOctets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsOutSchedDropPackets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsOutSchedDropOctets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsOutPoliciedPackets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfStatsOutPoliciedOctets"),
        ("Unisphere-Data-IP-MIB", "usdIpIfAssocIpIfIndex"))
)
if mibBuilder.loadTexts:
    usdIpInterfaceGroup4.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

usdIpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 1, 1)
)
if mibBuilder.loadTexts:
    usdIpCompliance.setStatus(
        "obsolete"
    )

usdIpCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 1, 2)
)
if mibBuilder.loadTexts:
    usdIpCompliance2.setStatus(
        "obsolete"
    )

usdIpCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 1, 3)
)
if mibBuilder.loadTexts:
    usdIpCompliance3.setStatus(
        "obsolete"
    )

usdIpCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 1, 4)
)
if mibBuilder.loadTexts:
    usdIpCompliance4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-IP-MIB",
    **{"usdIpMIB": usdIpMIB,
       "usdIpObjects": usdIpObjects,
       "usdIpInterface": usdIpInterface,
       "usdIpNextIfIndex": usdIpNextIfIndex,
       "usdIpIfTable": usdIpIfTable,
       "usdIpIfEntry": usdIpIfEntry,
       "usdIpIfIndex": usdIpIfIndex,
       "usdIpIfRowStatus": usdIpIfRowStatus,
       "usdIpIfLowerIfIndex": usdIpIfLowerIfIndex,
       "usdIpIfType": usdIpIfType,
       "usdIpIfTypeId": usdIpIfTypeId,
       "usdIpIfSAValidationEnable": usdIpIfSAValidationEnable,
       "usdIpIfCreationType": usdIpIfCreationType,
       "usdIpIfProfileId": usdIpIfProfileId,
       "usdIpIfAlwaysUp": usdIpIfAlwaysUp,
       "usdIpIfLoopback": usdIpIfLoopback,
       "usdIpIfLoopbackUid": usdIpIfLoopbackUid,
       "usdIpIfDebounceTime": usdIpIfDebounceTime,
       "usdIpIfForwarding": usdIpIfForwarding,
       "usdIpIfForceFragmentation": usdIpIfForceFragmentation,
       "usdIpIfSharesLowerUid": usdIpIfSharesLowerUid,
       "usdIpIfFilterOptions": usdIpIfFilterOptions,
       "usdIpIfName": usdIpIfName,
       "usdIpIfArpTimeout": usdIpIfArpTimeout,
       "usdIpIfAdminSpeed": usdIpIfAdminSpeed,
       "usdIpIfMultipathMode": usdIpIfMultipathMode,
       "usdIpIfSharedNhAddr": usdIpIfSharedNhAddr,
       "usdIpIfSharedNhRouterId": usdIpIfSharedNhRouterId,
       "usdIpIfPrimaryIpAddress": usdIpIfPrimaryIpAddress,
       "usdIpIfPrimaryIpMask": usdIpIfPrimaryIpMask,
       "usdIpIfOperDebounceTime": usdIpIfOperDebounceTime,
       "usdIpIfStatsTable": usdIpIfStatsTable,
       "usdIpIfStatsEntry": usdIpIfStatsEntry,
       "usdIpIfStatsIndex": usdIpIfStatsIndex,
       "usdIpIfStatsInPackets": usdIpIfStatsInPackets,
       "usdIpIfStatsInOctets": usdIpIfStatsInOctets,
       "usdIpIfStatsInPoliciedPackets": usdIpIfStatsInPoliciedPackets,
       "usdIpIfStatsInPoliciedOctets": usdIpIfStatsInPoliciedOctets,
       "usdIpIfStatsInErrorPackets": usdIpIfStatsInErrorPackets,
       "usdIpIfStatsInSpoofedPackets": usdIpIfStatsInSpoofedPackets,
       "usdIpIfStatsInForwardedPackets": usdIpIfStatsInForwardedPackets,
       "usdIpIfStatsInForwardedOctets": usdIpIfStatsInForwardedOctets,
       "usdIpIfStatsOutForwardedPackets": usdIpIfStatsOutForwardedPackets,
       "usdIpIfStatsOutForwardedOctets": usdIpIfStatsOutForwardedOctets,
       "usdIpIfStatsOutSchedDropPackets": usdIpIfStatsOutSchedDropPackets,
       "usdIpIfStatsOutSchedDropOctets": usdIpIfStatsOutSchedDropOctets,
       "usdIpIfStatsOutRequestedPackets": usdIpIfStatsOutRequestedPackets,
       "usdIpIfStatsOutRequestedOctets": usdIpIfStatsOutRequestedOctets,
       "usdIpIfStatsOutPoliciedPackets": usdIpIfStatsOutPoliciedPackets,
       "usdIpIfStatsOutPoliciedOctets": usdIpIfStatsOutPoliciedOctets,
       "usdIpIfStatsGreenOutSchedDropPackets": usdIpIfStatsGreenOutSchedDropPackets,
       "usdIpIfStatsYellowOutSchedDropPackets": usdIpIfStatsYellowOutSchedDropPackets,
       "usdIpIfStatsRedOutSchedDropPackets": usdIpIfStatsRedOutSchedDropPackets,
       "usdIpIfStatsGreenOutSchedDropOctets": usdIpIfStatsGreenOutSchedDropOctets,
       "usdIpIfStatsYellowOutSchedDropOctets": usdIpIfStatsYellowOutSchedDropOctets,
       "usdIpIfStatsRedOutSchedDropOctets": usdIpIfStatsRedOutSchedDropOctets,
       "usdIpIfAssocTable": usdIpIfAssocTable,
       "usdIpIfAssocEntry": usdIpIfAssocEntry,
       "usdIpIfAssocLowerIfIndex": usdIpIfAssocLowerIfIndex,
       "usdIpIfAssocIpIfIndex": usdIpIfAssocIpIfIndex,
       "usdIpAddress": usdIpAddress,
       "usdIpAddrGlobals": usdIpAddrGlobals,
       "usdIpArpTimeout": usdIpArpTimeout,
       "usdIpAddrTable": usdIpAddrTable,
       "usdIpAddrEntry": usdIpAddrEntry,
       "usdIpAdEntAddr": usdIpAdEntAddr,
       "usdIpAdEntIfIndex": usdIpAdEntIfIndex,
       "usdIpAdEntNetMask": usdIpAdEntNetMask,
       "usdIpAdEntBcastAddr": usdIpAdEntBcastAddr,
       "usdIpAdEntReasmMaxSize": usdIpAdEntReasmMaxSize,
       "usdIpAdEntRowStatus": usdIpAdEntRowStatus,
       "usdIpAdEntAdminStatus": usdIpAdEntAdminStatus,
       "usdIpAdEntArpRspEnable": usdIpAdEntArpRspEnable,
       "usdIpAdEntProxyArpRspEnable": usdIpAdEntProxyArpRspEnable,
       "usdIpAdEntIgmpEnable": usdIpAdEntIgmpEnable,
       "usdIpAdEntDirectedBcastEnable": usdIpAdEntDirectedBcastEnable,
       "usdIpAdEntIcmpRedirectEnable": usdIpAdEntIcmpRedirectEnable,
       "usdIpAdEntIcmpMaskReplyEnable": usdIpAdEntIcmpMaskReplyEnable,
       "usdIpAdEntIcmpUnreachEnable": usdIpAdEntIcmpUnreachEnable,
       "usdIpAdEntMtu": usdIpAdEntMtu,
       "usdIpAdEntUnnumLoopbackIfIndex": usdIpAdEntUnnumLoopbackIfIndex,
       "usdIpAdEntIrdpEnable": usdIpAdEntIrdpEnable,
       "usdIpAdEntAccessRouteEnable": usdIpAdEntAccessRouteEnable,
       "usdIpAdEntAccessRouteHost": usdIpAdEntAccessRouteHost,
       "usdIpAdEntIsSecondary": usdIpAdEntIsSecondary,
       "usdIpRoute": usdIpRoute,
       "usdIpRouteGlobals": usdIpRouteGlobals,
       "usdIpRouteLimit": usdIpRouteLimit,
       "usdIpRouteStaticTable": usdIpRouteStaticTable,
       "usdIpRouteStaticEntry": usdIpRouteStaticEntry,
       "usdIpRouteStaticDest": usdIpRouteStaticDest,
       "usdIpRouteStaticMask": usdIpRouteStaticMask,
       "usdIpRouteStaticPref": usdIpRouteStaticPref,
       "usdIpRouteStaticNextHop": usdIpRouteStaticNextHop,
       "usdIpRouteStaticRowStatus": usdIpRouteStaticRowStatus,
       "usdIpRouteStaticIfIndex": usdIpRouteStaticIfIndex,
       "usdIpRouteStaticStatus": usdIpRouteStaticStatus,
       "usdIpRouteStaticNextHopAS": usdIpRouteStaticNextHopAS,
       "usdIpRouteStaticMetric": usdIpRouteStaticMetric,
       "usdIpRouteStaticTag": usdIpRouteStaticTag,
       "usdIpCidrRouteTable": usdIpCidrRouteTable,
       "usdIpCidrRouteEntry": usdIpCidrRouteEntry,
       "usdIpCidrRoutePref": usdIpCidrRoutePref,
       "usdIpCidrRouteArea": usdIpCidrRouteArea,
       "usdIpCidrRouteTag": usdIpCidrRouteTag,
       "usdIpGlobals": usdIpGlobals,
       "usdIpDebounceTime": usdIpDebounceTime,
       "usdIpRouterId": usdIpRouterId,
       "usdIpSourceRoutingAdminStatus": usdIpSourceRoutingAdminStatus,
       "usdIpVpnIdOui": usdIpVpnIdOui,
       "usdIpVpnIdIndex": usdIpVpnIdIndex,
       "usdIpConformance": usdIpConformance,
       "usdIpCompliances": usdIpCompliances,
       "usdIpCompliance": usdIpCompliance,
       "usdIpCompliance2": usdIpCompliance2,
       "usdIpCompliance3": usdIpCompliance3,
       "usdIpCompliance4": usdIpCompliance4,
       "usdIpGroups": usdIpGroups,
       "usdIpInterfaceGroup": usdIpInterfaceGroup,
       "usdIpAddressGroup": usdIpAddressGroup,
       "usdIpRouteGroup": usdIpRouteGroup,
       "usdIpGlobalGroup": usdIpGlobalGroup,
       "usdIpInterfaceGroup2": usdIpInterfaceGroup2,
       "usdIpAddressGroup2": usdIpAddressGroup2,
       "usdIpInterfaceGroup3": usdIpInterfaceGroup3,
       "usdIpInterfaceGroup4": usdIpInterfaceGroup4}
)
