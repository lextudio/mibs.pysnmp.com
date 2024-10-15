# SNMP MIB module (Juniper-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-IP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:15:29 2024
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
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(ipCidrRouteEntry,
 ipCidrRouteNumber) = mibBuilder.importSymbols(
    "IP-FORWARD-MIB",
    "ipCidrRouteEntry",
    "ipCidrRouteNumber")

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(JuniEnable,
 JuniIpAddrLessIf,
 JuniNextIfIndex) = mibBuilder.importSymbols(
    "Juniper-TC",
    "JuniEnable",
    "JuniIpAddrLessIf",
    "JuniNextIfIndex")

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


# MODULE-IDENTITY

juniIpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12)
)
juniIpMIB.setRevisions(
        ("2007-01-17 23:02",
         "2005-03-30 13:49",
         "2005-04-29 20:37",
         "2004-09-20 13:49",
         "2004-09-10 15:26",
         "2003-11-03 15:26",
         "2003-06-25 19:48",
         "2003-02-11 19:05",
         "2002-10-23 18:53",
         "2002-04-03 22:06",
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

_JuniIpObjects_ObjectIdentity = ObjectIdentity
juniIpObjects = _JuniIpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1)
)
_JuniIpInterface_ObjectIdentity = ObjectIdentity
juniIpInterface = _JuniIpInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1)
)
_JuniIpNextIfIndex_Type = JuniNextIfIndex
_JuniIpNextIfIndex_Object = MibScalar
juniIpNextIfIndex = _JuniIpNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 1),
    _JuniIpNextIfIndex_Type()
)
juniIpNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpNextIfIndex.setStatus("current")
_JuniIpIfTable_Object = MibTable
juniIpIfTable = _JuniIpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2)
)
if mibBuilder.loadTexts:
    juniIpIfTable.setStatus("current")
_JuniIpIfEntry_Object = MibTableRow
juniIpIfEntry = _JuniIpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1)
)
juniIpIfEntry.setIndexNames(
    (0, "Juniper-IP-MIB", "juniIpIfIndex"),
)
if mibBuilder.loadTexts:
    juniIpIfEntry.setStatus("current")
_JuniIpIfIndex_Type = InterfaceIndex
_JuniIpIfIndex_Object = MibTableColumn
juniIpIfIndex = _JuniIpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 1),
    _JuniIpIfIndex_Type()
)
juniIpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIpIfIndex.setStatus("current")
_JuniIpIfRowStatus_Type = RowStatus
_JuniIpIfRowStatus_Object = MibTableColumn
juniIpIfRowStatus = _JuniIpIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 2),
    _JuniIpIfRowStatus_Type()
)
juniIpIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpIfRowStatus.setStatus("current")
_JuniIpIfLowerIfIndex_Type = InterfaceIndexOrZero
_JuniIpIfLowerIfIndex_Object = MibTableColumn
juniIpIfLowerIfIndex = _JuniIpIfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 3),
    _JuniIpIfLowerIfIndex_Type()
)
juniIpIfLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpIfLowerIfIndex.setStatus("current")


class _JuniIpIfType_Type(Integer32):
    """Custom type juniIpIfType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("bgpMplsVpn", 6),
          ("broadcast", 1),
          ("dialout", 8),
          ("loopback", 4),
          ("nbma", 3),
          ("null", 5),
          ("other", 0),
          ("pointToPoint", 2),
          ("vrfInternal", 7))
    )


_JuniIpIfType_Type.__name__ = "Integer32"
_JuniIpIfType_Object = MibTableColumn
juniIpIfType = _JuniIpIfType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 4),
    _JuniIpIfType_Type()
)
juniIpIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpIfType.setStatus("current")


class _JuniIpIfTypeId_Type(Unsigned32):
    """Custom type juniIpIfTypeId based on Unsigned32"""
    defaultValue = 0


_JuniIpIfTypeId_Object = MibTableColumn
juniIpIfTypeId = _JuniIpIfTypeId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 5),
    _JuniIpIfTypeId_Type()
)
juniIpIfTypeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpIfTypeId.setStatus("current")


class _JuniIpIfSAValidationEnable_Type(JuniEnable):
    """Custom type juniIpIfSAValidationEnable based on JuniEnable"""


_JuniIpIfSAValidationEnable_Object = MibTableColumn
juniIpIfSAValidationEnable = _JuniIpIfSAValidationEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 6),
    _JuniIpIfSAValidationEnable_Type()
)
juniIpIfSAValidationEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpIfSAValidationEnable.setStatus("current")


class _JuniIpIfCreationType_Type(Integer32):
    """Custom type juniIpIfCreationType based on Integer32"""
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


_JuniIpIfCreationType_Type.__name__ = "Integer32"
_JuniIpIfCreationType_Object = MibTableColumn
juniIpIfCreationType = _JuniIpIfCreationType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 7),
    _JuniIpIfCreationType_Type()
)
juniIpIfCreationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpIfCreationType.setStatus("current")


class _JuniIpIfProfileId_Type(Unsigned32):
    """Custom type juniIpIfProfileId based on Unsigned32"""
    defaultValue = 0


_JuniIpIfProfileId_Object = MibTableColumn
juniIpIfProfileId = _JuniIpIfProfileId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 8),
    _JuniIpIfProfileId_Type()
)
juniIpIfProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpIfProfileId.setStatus("current")


class _JuniIpIfAlwaysUp_Type(JuniEnable):
    """Custom type juniIpIfAlwaysUp based on JuniEnable"""


_JuniIpIfAlwaysUp_Object = MibTableColumn
juniIpIfAlwaysUp = _JuniIpIfAlwaysUp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 9),
    _JuniIpIfAlwaysUp_Type()
)
juniIpIfAlwaysUp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpIfAlwaysUp.setStatus("current")


class _JuniIpIfLoopback_Type(JuniEnable):
    """Custom type juniIpIfLoopback based on JuniEnable"""


_JuniIpIfLoopback_Object = MibTableColumn
juniIpIfLoopback = _JuniIpIfLoopback_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 10),
    _JuniIpIfLoopback_Type()
)
juniIpIfLoopback.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpIfLoopback.setStatus("deprecated")


class _JuniIpIfLoopbackUid_Type(InterfaceIndexOrZero):
    """Custom type juniIpIfLoopbackUid based on InterfaceIndexOrZero"""
    defaultValue = 0


_JuniIpIfLoopbackUid_Object = MibTableColumn
juniIpIfLoopbackUid = _JuniIpIfLoopbackUid_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 11),
    _JuniIpIfLoopbackUid_Type()
)
juniIpIfLoopbackUid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpIfLoopbackUid.setStatus("deprecated")


class _JuniIpIfDebounceTime_Type(Integer32):
    """Custom type juniIpIfDebounceTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_JuniIpIfDebounceTime_Type.__name__ = "Integer32"
_JuniIpIfDebounceTime_Object = MibTableColumn
juniIpIfDebounceTime = _JuniIpIfDebounceTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 12),
    _JuniIpIfDebounceTime_Type()
)
juniIpIfDebounceTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpIfDebounceTime.setStatus("current")
if mibBuilder.loadTexts:
    juniIpIfDebounceTime.setUnits("milliseconds")


class _JuniIpIfForwarding_Type(JuniEnable):
    """Custom type juniIpIfForwarding based on JuniEnable"""


_JuniIpIfForwarding_Object = MibTableColumn
juniIpIfForwarding = _JuniIpIfForwarding_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 13),
    _JuniIpIfForwarding_Type()
)
juniIpIfForwarding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpIfForwarding.setStatus("current")


class _JuniIpIfForceFragmentation_Type(JuniEnable):
    """Custom type juniIpIfForceFragmentation based on JuniEnable"""


_JuniIpIfForceFragmentation_Object = MibTableColumn
juniIpIfForceFragmentation = _JuniIpIfForceFragmentation_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 14),
    _JuniIpIfForceFragmentation_Type()
)
juniIpIfForceFragmentation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpIfForceFragmentation.setStatus("current")
_JuniIpIfSharesLowerUid_Type = JuniEnable
_JuniIpIfSharesLowerUid_Object = MibTableColumn
juniIpIfSharesLowerUid = _JuniIpIfSharesLowerUid_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 15),
    _JuniIpIfSharesLowerUid_Type()
)
juniIpIfSharesLowerUid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpIfSharesLowerUid.setStatus("current")


class _JuniIpIfFilterOptions_Type(Unsigned32):
    """Custom type juniIpIfFilterOptions based on Unsigned32"""
    defaultValue = 0


_JuniIpIfFilterOptions_Object = MibTableColumn
juniIpIfFilterOptions = _JuniIpIfFilterOptions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 16),
    _JuniIpIfFilterOptions_Type()
)
juniIpIfFilterOptions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpIfFilterOptions.setStatus("current")


class _JuniIpIfName_Type(OctetString):
    """Custom type juniIpIfName based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JuniIpIfName_Type.__name__ = "OctetString"
_JuniIpIfName_Object = MibTableColumn
juniIpIfName = _JuniIpIfName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 17),
    _JuniIpIfName_Type()
)
juniIpIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpIfName.setStatus("current")


class _JuniIpIfArpTimeout_Type(Unsigned32):
    """Custom type juniIpIfArpTimeout based on Unsigned32"""
    defaultValue = 21600


_JuniIpIfArpTimeout_Object = MibTableColumn
juniIpIfArpTimeout = _JuniIpIfArpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 18),
    _JuniIpIfArpTimeout_Type()
)
juniIpIfArpTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpIfArpTimeout.setStatus("current")


class _JuniIpIfAdminSpeed_Type(Unsigned32):
    """Custom type juniIpIfAdminSpeed based on Unsigned32"""
    defaultValue = 0


_JuniIpIfAdminSpeed_Object = MibTableColumn
juniIpIfAdminSpeed = _JuniIpIfAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 19),
    _JuniIpIfAdminSpeed_Type()
)
juniIpIfAdminSpeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpIfAdminSpeed.setStatus("current")


class _JuniIpIfMultipathMode_Type(Integer32):
    """Custom type juniIpIfMultipathMode based on Integer32"""
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


_JuniIpIfMultipathMode_Type.__name__ = "Integer32"
_JuniIpIfMultipathMode_Object = MibTableColumn
juniIpIfMultipathMode = _JuniIpIfMultipathMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 20),
    _JuniIpIfMultipathMode_Type()
)
juniIpIfMultipathMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpIfMultipathMode.setStatus("current")


class _JuniIpIfSharedNhAddr_Type(IpAddress):
    """Custom type juniIpIfSharedNhAddr based on IpAddress"""
    defaultValue = 0


_JuniIpIfSharedNhAddr_Object = MibTableColumn
juniIpIfSharedNhAddr = _JuniIpIfSharedNhAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 21),
    _JuniIpIfSharedNhAddr_Type()
)
juniIpIfSharedNhAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpIfSharedNhAddr.setStatus("current")


class _JuniIpIfSharedNhRouterId_Type(Unsigned32):
    """Custom type juniIpIfSharedNhRouterId based on Unsigned32"""
    defaultValue = 0


_JuniIpIfSharedNhRouterId_Object = MibTableColumn
juniIpIfSharedNhRouterId = _JuniIpIfSharedNhRouterId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 22),
    _JuniIpIfSharedNhRouterId_Type()
)
juniIpIfSharedNhRouterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpIfSharedNhRouterId.setStatus("current")
_JuniIpIfPrimaryIpAddress_Type = IpAddress
_JuniIpIfPrimaryIpAddress_Object = MibTableColumn
juniIpIfPrimaryIpAddress = _JuniIpIfPrimaryIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 23),
    _JuniIpIfPrimaryIpAddress_Type()
)
juniIpIfPrimaryIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpIfPrimaryIpAddress.setStatus("current")
_JuniIpIfPrimaryIpMask_Type = IpAddress
_JuniIpIfPrimaryIpMask_Object = MibTableColumn
juniIpIfPrimaryIpMask = _JuniIpIfPrimaryIpMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 24),
    _JuniIpIfPrimaryIpMask_Type()
)
juniIpIfPrimaryIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpIfPrimaryIpMask.setStatus("current")


class _JuniIpIfOperDebounceTime_Type(Integer32):
    """Custom type juniIpIfOperDebounceTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_JuniIpIfOperDebounceTime_Type.__name__ = "Integer32"
_JuniIpIfOperDebounceTime_Object = MibTableColumn
juniIpIfOperDebounceTime = _JuniIpIfOperDebounceTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 25),
    _JuniIpIfOperDebounceTime_Type()
)
juniIpIfOperDebounceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpIfOperDebounceTime.setStatus("current")
if mibBuilder.loadTexts:
    juniIpIfOperDebounceTime.setUnits("milliseconds")
_JuniIpIfRouterIndex_Type = Unsigned32
_JuniIpIfRouterIndex_Object = MibTableColumn
juniIpIfRouterIndex = _JuniIpIfRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 26),
    _JuniIpIfRouterIndex_Type()
)
juniIpIfRouterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpIfRouterIndex.setStatus("current")
_JuniIpIfInheritNum_Type = JuniEnable
_JuniIpIfInheritNum_Object = MibTableColumn
juniIpIfInheritNum = _JuniIpIfInheritNum_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 27),
    _JuniIpIfInheritNum_Type()
)
juniIpIfInheritNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpIfInheritNum.setStatus("current")


class _JuniIpIfInheritNumUid_Type(InterfaceIndexOrZero):
    """Custom type juniIpIfInheritNumUid based on InterfaceIndexOrZero"""
    defaultValue = 0


_JuniIpIfInheritNumUid_Object = MibTableColumn
juniIpIfInheritNumUid = _JuniIpIfInheritNumUid_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 28),
    _JuniIpIfInheritNumUid_Type()
)
juniIpIfInheritNumUid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpIfInheritNumUid.setStatus("current")


class _JuniIpIfAnalyzerMode_Type(Integer32):
    """Custom type juniIpIfAnalyzerMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 2),
          ("disable", 0),
          ("enable", 1))
    )


_JuniIpIfAnalyzerMode_Type.__name__ = "Integer32"
_JuniIpIfAnalyzerMode_Object = MibTableColumn
juniIpIfAnalyzerMode = _JuniIpIfAnalyzerMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 29),
    _JuniIpIfAnalyzerMode_Type()
)
juniIpIfAnalyzerMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpIfAnalyzerMode.setStatus("current")


class _JuniIpIfAutoConfigure_Type(JuniEnable):
    """Custom type juniIpIfAutoConfigure based on JuniEnable"""


_JuniIpIfAutoConfigure_Object = MibTableColumn
juniIpIfAutoConfigure = _JuniIpIfAutoConfigure_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 30),
    _JuniIpIfAutoConfigure_Type()
)
juniIpIfAutoConfigure.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpIfAutoConfigure.setStatus("current")


class _JuniIpIfTcpMss_Type(Integer32):
    """Custom type juniIpIfTcpMss based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(160, 10240),
    )


_JuniIpIfTcpMss_Type.__name__ = "Integer32"
_JuniIpIfTcpMss_Object = MibTableColumn
juniIpIfTcpMss = _JuniIpIfTcpMss_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 31),
    _JuniIpIfTcpMss_Type()
)
juniIpIfTcpMss.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpIfTcpMss.setStatus("current")
_JuniIpIfInitSeqPrefOper_Type = Unsigned32
_JuniIpIfInitSeqPrefOper_Object = MibTableColumn
juniIpIfInitSeqPrefOper = _JuniIpIfInitSeqPrefOper_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 32),
    _JuniIpIfInitSeqPrefOper_Type()
)
juniIpIfInitSeqPrefOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpIfInitSeqPrefOper.setStatus("current")


class _JuniIpIfInitSeqPrefAdmin_Type(Unsigned32):
    """Custom type juniIpIfInitSeqPrefAdmin based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_JuniIpIfInitSeqPrefAdmin_Type.__name__ = "Unsigned32"
_JuniIpIfInitSeqPrefAdmin_Object = MibTableColumn
juniIpIfInitSeqPrefAdmin = _JuniIpIfInitSeqPrefAdmin_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 33),
    _JuniIpIfInitSeqPrefAdmin_Type()
)
juniIpIfInitSeqPrefAdmin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpIfInitSeqPrefAdmin.setStatus("current")


class _JuniIpIfArpSpoofCheck_Type(JuniEnable):
    """Custom type juniIpIfArpSpoofCheck based on JuniEnable"""


_JuniIpIfArpSpoofCheck_Object = MibTableColumn
juniIpIfArpSpoofCheck = _JuniIpIfArpSpoofCheck_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 2, 1, 34),
    _JuniIpIfArpSpoofCheck_Type()
)
juniIpIfArpSpoofCheck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpIfArpSpoofCheck.setStatus("current")
_JuniIpIfStatsTable_Object = MibTable
juniIpIfStatsTable = _JuniIpIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3)
)
if mibBuilder.loadTexts:
    juniIpIfStatsTable.setStatus("current")
_JuniIpIfStatsEntry_Object = MibTableRow
juniIpIfStatsEntry = _JuniIpIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3, 1)
)
juniIpIfStatsEntry.setIndexNames(
    (0, "Juniper-IP-MIB", "juniIpIfStatsIndex"),
)
if mibBuilder.loadTexts:
    juniIpIfStatsEntry.setStatus("current")
_JuniIpIfStatsIndex_Type = InterfaceIndex
_JuniIpIfStatsIndex_Object = MibTableColumn
juniIpIfStatsIndex = _JuniIpIfStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3, 1, 1),
    _JuniIpIfStatsIndex_Type()
)
juniIpIfStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIpIfStatsIndex.setStatus("current")
_JuniIpIfStatsInPackets_Type = Counter64
_JuniIpIfStatsInPackets_Object = MibTableColumn
juniIpIfStatsInPackets = _JuniIpIfStatsInPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3, 1, 2),
    _JuniIpIfStatsInPackets_Type()
)
juniIpIfStatsInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpIfStatsInPackets.setStatus("current")
_JuniIpIfStatsInOctets_Type = Counter64
_JuniIpIfStatsInOctets_Object = MibTableColumn
juniIpIfStatsInOctets = _JuniIpIfStatsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3, 1, 3),
    _JuniIpIfStatsInOctets_Type()
)
juniIpIfStatsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpIfStatsInOctets.setStatus("current")
_JuniIpIfStatsInPoliciedPackets_Type = Counter64
_JuniIpIfStatsInPoliciedPackets_Object = MibTableColumn
juniIpIfStatsInPoliciedPackets = _JuniIpIfStatsInPoliciedPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3, 1, 4),
    _JuniIpIfStatsInPoliciedPackets_Type()
)
juniIpIfStatsInPoliciedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpIfStatsInPoliciedPackets.setStatus("current")
_JuniIpIfStatsInPoliciedOctets_Type = Counter64
_JuniIpIfStatsInPoliciedOctets_Object = MibTableColumn
juniIpIfStatsInPoliciedOctets = _JuniIpIfStatsInPoliciedOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3, 1, 5),
    _JuniIpIfStatsInPoliciedOctets_Type()
)
juniIpIfStatsInPoliciedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpIfStatsInPoliciedOctets.setStatus("current")
_JuniIpIfStatsInErrorPackets_Type = Counter64
_JuniIpIfStatsInErrorPackets_Object = MibTableColumn
juniIpIfStatsInErrorPackets = _JuniIpIfStatsInErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3, 1, 6),
    _JuniIpIfStatsInErrorPackets_Type()
)
juniIpIfStatsInErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpIfStatsInErrorPackets.setStatus("current")
_JuniIpIfStatsInSpoofedPackets_Type = Counter64
_JuniIpIfStatsInSpoofedPackets_Object = MibTableColumn
juniIpIfStatsInSpoofedPackets = _JuniIpIfStatsInSpoofedPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3, 1, 7),
    _JuniIpIfStatsInSpoofedPackets_Type()
)
juniIpIfStatsInSpoofedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpIfStatsInSpoofedPackets.setStatus("current")
_JuniIpIfStatsInForwardedPackets_Type = Counter64
_JuniIpIfStatsInForwardedPackets_Object = MibTableColumn
juniIpIfStatsInForwardedPackets = _JuniIpIfStatsInForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3, 1, 8),
    _JuniIpIfStatsInForwardedPackets_Type()
)
juniIpIfStatsInForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpIfStatsInForwardedPackets.setStatus("obsolete")
_JuniIpIfStatsInForwardedOctets_Type = Counter64
_JuniIpIfStatsInForwardedOctets_Object = MibTableColumn
juniIpIfStatsInForwardedOctets = _JuniIpIfStatsInForwardedOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3, 1, 9),
    _JuniIpIfStatsInForwardedOctets_Type()
)
juniIpIfStatsInForwardedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpIfStatsInForwardedOctets.setStatus("obsolete")
_JuniIpIfStatsOutForwardedPackets_Type = Counter64
_JuniIpIfStatsOutForwardedPackets_Object = MibTableColumn
juniIpIfStatsOutForwardedPackets = _JuniIpIfStatsOutForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3, 1, 10),
    _JuniIpIfStatsOutForwardedPackets_Type()
)
juniIpIfStatsOutForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpIfStatsOutForwardedPackets.setStatus("current")
_JuniIpIfStatsOutForwardedOctets_Type = Counter64
_JuniIpIfStatsOutForwardedOctets_Object = MibTableColumn
juniIpIfStatsOutForwardedOctets = _JuniIpIfStatsOutForwardedOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3, 1, 11),
    _JuniIpIfStatsOutForwardedOctets_Type()
)
juniIpIfStatsOutForwardedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpIfStatsOutForwardedOctets.setStatus("current")
_JuniIpIfStatsOutSchedDropPackets_Type = Counter64
_JuniIpIfStatsOutSchedDropPackets_Object = MibTableColumn
juniIpIfStatsOutSchedDropPackets = _JuniIpIfStatsOutSchedDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3, 1, 12),
    _JuniIpIfStatsOutSchedDropPackets_Type()
)
juniIpIfStatsOutSchedDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpIfStatsOutSchedDropPackets.setStatus("current")
_JuniIpIfStatsOutSchedDropOctets_Type = Counter64
_JuniIpIfStatsOutSchedDropOctets_Object = MibTableColumn
juniIpIfStatsOutSchedDropOctets = _JuniIpIfStatsOutSchedDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3, 1, 13),
    _JuniIpIfStatsOutSchedDropOctets_Type()
)
juniIpIfStatsOutSchedDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpIfStatsOutSchedDropOctets.setStatus("current")
_JuniIpIfStatsOutRequestedPackets_Type = Counter64
_JuniIpIfStatsOutRequestedPackets_Object = MibTableColumn
juniIpIfStatsOutRequestedPackets = _JuniIpIfStatsOutRequestedPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3, 1, 14),
    _JuniIpIfStatsOutRequestedPackets_Type()
)
juniIpIfStatsOutRequestedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpIfStatsOutRequestedPackets.setStatus("obsolete")
_JuniIpIfStatsOutRequestedOctets_Type = Counter64
_JuniIpIfStatsOutRequestedOctets_Object = MibTableColumn
juniIpIfStatsOutRequestedOctets = _JuniIpIfStatsOutRequestedOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3, 1, 15),
    _JuniIpIfStatsOutRequestedOctets_Type()
)
juniIpIfStatsOutRequestedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpIfStatsOutRequestedOctets.setStatus("obsolete")
_JuniIpIfStatsOutPoliciedPackets_Type = Counter64
_JuniIpIfStatsOutPoliciedPackets_Object = MibTableColumn
juniIpIfStatsOutPoliciedPackets = _JuniIpIfStatsOutPoliciedPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3, 1, 16),
    _JuniIpIfStatsOutPoliciedPackets_Type()
)
juniIpIfStatsOutPoliciedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpIfStatsOutPoliciedPackets.setStatus("current")
_JuniIpIfStatsOutPoliciedOctets_Type = Counter64
_JuniIpIfStatsOutPoliciedOctets_Object = MibTableColumn
juniIpIfStatsOutPoliciedOctets = _JuniIpIfStatsOutPoliciedOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3, 1, 17),
    _JuniIpIfStatsOutPoliciedOctets_Type()
)
juniIpIfStatsOutPoliciedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpIfStatsOutPoliciedOctets.setStatus("current")
_JuniIpIfStatsGreenOutSchedDropPackets_Type = Counter64
_JuniIpIfStatsGreenOutSchedDropPackets_Object = MibTableColumn
juniIpIfStatsGreenOutSchedDropPackets = _JuniIpIfStatsGreenOutSchedDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3, 1, 18),
    _JuniIpIfStatsGreenOutSchedDropPackets_Type()
)
juniIpIfStatsGreenOutSchedDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpIfStatsGreenOutSchedDropPackets.setStatus("obsolete")
_JuniIpIfStatsYellowOutSchedDropPackets_Type = Counter64
_JuniIpIfStatsYellowOutSchedDropPackets_Object = MibTableColumn
juniIpIfStatsYellowOutSchedDropPackets = _JuniIpIfStatsYellowOutSchedDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3, 1, 19),
    _JuniIpIfStatsYellowOutSchedDropPackets_Type()
)
juniIpIfStatsYellowOutSchedDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpIfStatsYellowOutSchedDropPackets.setStatus("obsolete")
_JuniIpIfStatsRedOutSchedDropPackets_Type = Counter64
_JuniIpIfStatsRedOutSchedDropPackets_Object = MibTableColumn
juniIpIfStatsRedOutSchedDropPackets = _JuniIpIfStatsRedOutSchedDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3, 1, 20),
    _JuniIpIfStatsRedOutSchedDropPackets_Type()
)
juniIpIfStatsRedOutSchedDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpIfStatsRedOutSchedDropPackets.setStatus("obsolete")
_JuniIpIfStatsGreenOutSchedDropOctets_Type = Counter64
_JuniIpIfStatsGreenOutSchedDropOctets_Object = MibTableColumn
juniIpIfStatsGreenOutSchedDropOctets = _JuniIpIfStatsGreenOutSchedDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3, 1, 21),
    _JuniIpIfStatsGreenOutSchedDropOctets_Type()
)
juniIpIfStatsGreenOutSchedDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpIfStatsGreenOutSchedDropOctets.setStatus("obsolete")
_JuniIpIfStatsYellowOutSchedDropOctets_Type = Counter64
_JuniIpIfStatsYellowOutSchedDropOctets_Object = MibTableColumn
juniIpIfStatsYellowOutSchedDropOctets = _JuniIpIfStatsYellowOutSchedDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3, 1, 22),
    _JuniIpIfStatsYellowOutSchedDropOctets_Type()
)
juniIpIfStatsYellowOutSchedDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpIfStatsYellowOutSchedDropOctets.setStatus("obsolete")
_JuniIpIfStatsRedOutSchedDropOctets_Type = Counter64
_JuniIpIfStatsRedOutSchedDropOctets_Object = MibTableColumn
juniIpIfStatsRedOutSchedDropOctets = _JuniIpIfStatsRedOutSchedDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 3, 1, 23),
    _JuniIpIfStatsRedOutSchedDropOctets_Type()
)
juniIpIfStatsRedOutSchedDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpIfStatsRedOutSchedDropOctets.setStatus("obsolete")
_JuniIpIfAssocTable_Object = MibTable
juniIpIfAssocTable = _JuniIpIfAssocTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 4)
)
if mibBuilder.loadTexts:
    juniIpIfAssocTable.setStatus("current")
_JuniIpIfAssocEntry_Object = MibTableRow
juniIpIfAssocEntry = _JuniIpIfAssocEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 4, 1)
)
juniIpIfAssocEntry.setIndexNames(
    (0, "Juniper-IP-MIB", "juniIpIfAssocLowerIfIndex"),
)
if mibBuilder.loadTexts:
    juniIpIfAssocEntry.setStatus("current")
_JuniIpIfAssocLowerIfIndex_Type = InterfaceIndex
_JuniIpIfAssocLowerIfIndex_Object = MibTableColumn
juniIpIfAssocLowerIfIndex = _JuniIpIfAssocLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 4, 1, 1),
    _JuniIpIfAssocLowerIfIndex_Type()
)
juniIpIfAssocLowerIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIpIfAssocLowerIfIndex.setStatus("current")
_JuniIpIfAssocIpIfIndex_Type = InterfaceIndexOrZero
_JuniIpIfAssocIpIfIndex_Object = MibTableColumn
juniIpIfAssocIpIfIndex = _JuniIpIfAssocIpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 1, 4, 1, 2),
    _JuniIpIfAssocIpIfIndex_Type()
)
juniIpIfAssocIpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpIfAssocIpIfIndex.setStatus("current")
_JuniIpAddress_ObjectIdentity = ObjectIdentity
juniIpAddress = _JuniIpAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2)
)
_JuniIpAddrGlobals_ObjectIdentity = ObjectIdentity
juniIpAddrGlobals = _JuniIpAddrGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 1)
)


class _JuniIpArpTimeout_Type(Integer32):
    """Custom type juniIpArpTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_JuniIpArpTimeout_Type.__name__ = "Integer32"
_JuniIpArpTimeout_Object = MibScalar
juniIpArpTimeout = _JuniIpArpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 1, 1),
    _JuniIpArpTimeout_Type()
)
juniIpArpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIpArpTimeout.setStatus("obsolete")
if mibBuilder.loadTexts:
    juniIpArpTimeout.setUnits("seconds")
_JuniIpAddrTable_Object = MibTable
juniIpAddrTable = _JuniIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 2)
)
if mibBuilder.loadTexts:
    juniIpAddrTable.setStatus("current")
_JuniIpAddrEntry_Object = MibTableRow
juniIpAddrEntry = _JuniIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 2, 1)
)
juniIpAddrEntry.setIndexNames(
    (0, "Juniper-IP-MIB", "juniIpAdEntAddr"),
)
if mibBuilder.loadTexts:
    juniIpAddrEntry.setStatus("current")
_JuniIpAdEntAddr_Type = JuniIpAddrLessIf
_JuniIpAdEntAddr_Object = MibTableColumn
juniIpAdEntAddr = _JuniIpAdEntAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 2, 1, 1),
    _JuniIpAdEntAddr_Type()
)
juniIpAdEntAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIpAdEntAddr.setStatus("current")
_JuniIpAdEntIfIndex_Type = InterfaceIndex
_JuniIpAdEntIfIndex_Object = MibTableColumn
juniIpAdEntIfIndex = _JuniIpAdEntIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 2, 1, 2),
    _JuniIpAdEntIfIndex_Type()
)
juniIpAdEntIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpAdEntIfIndex.setStatus("current")


class _JuniIpAdEntNetMask_Type(IpAddress):
    """Custom type juniIpAdEntNetMask based on IpAddress"""
    defaultHexValue = "ffffffff"


_JuniIpAdEntNetMask_Object = MibTableColumn
juniIpAdEntNetMask = _JuniIpAdEntNetMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 2, 1, 3),
    _JuniIpAdEntNetMask_Type()
)
juniIpAdEntNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpAdEntNetMask.setStatus("current")


class _JuniIpAdEntBcastAddr_Type(Integer32):
    """Custom type juniIpAdEntBcastAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_JuniIpAdEntBcastAddr_Type.__name__ = "Integer32"
_JuniIpAdEntBcastAddr_Object = MibTableColumn
juniIpAdEntBcastAddr = _JuniIpAdEntBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 2, 1, 4),
    _JuniIpAdEntBcastAddr_Type()
)
juniIpAdEntBcastAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpAdEntBcastAddr.setStatus("current")


class _JuniIpAdEntReasmMaxSize_Type(Integer32):
    """Custom type juniIpAdEntReasmMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniIpAdEntReasmMaxSize_Type.__name__ = "Integer32"
_JuniIpAdEntReasmMaxSize_Object = MibTableColumn
juniIpAdEntReasmMaxSize = _JuniIpAdEntReasmMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 2, 1, 5),
    _JuniIpAdEntReasmMaxSize_Type()
)
juniIpAdEntReasmMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpAdEntReasmMaxSize.setStatus("current")
_JuniIpAdEntRowStatus_Type = RowStatus
_JuniIpAdEntRowStatus_Object = MibTableColumn
juniIpAdEntRowStatus = _JuniIpAdEntRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 2, 1, 6),
    _JuniIpAdEntRowStatus_Type()
)
juniIpAdEntRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpAdEntRowStatus.setStatus("current")


class _JuniIpAdEntAdminStatus_Type(JuniEnable):
    """Custom type juniIpAdEntAdminStatus based on JuniEnable"""


_JuniIpAdEntAdminStatus_Object = MibTableColumn
juniIpAdEntAdminStatus = _JuniIpAdEntAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 2, 1, 7),
    _JuniIpAdEntAdminStatus_Type()
)
juniIpAdEntAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpAdEntAdminStatus.setStatus("current")


class _JuniIpAdEntArpRspEnable_Type(JuniEnable):
    """Custom type juniIpAdEntArpRspEnable based on JuniEnable"""


_JuniIpAdEntArpRspEnable_Object = MibTableColumn
juniIpAdEntArpRspEnable = _JuniIpAdEntArpRspEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 2, 1, 8),
    _JuniIpAdEntArpRspEnable_Type()
)
juniIpAdEntArpRspEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpAdEntArpRspEnable.setStatus("current")


class _JuniIpAdEntProxyArpRspEnable_Type(JuniEnable):
    """Custom type juniIpAdEntProxyArpRspEnable based on JuniEnable"""


_JuniIpAdEntProxyArpRspEnable_Object = MibTableColumn
juniIpAdEntProxyArpRspEnable = _JuniIpAdEntProxyArpRspEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 2, 1, 9),
    _JuniIpAdEntProxyArpRspEnable_Type()
)
juniIpAdEntProxyArpRspEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpAdEntProxyArpRspEnable.setStatus("current")


class _JuniIpAdEntIgmpEnable_Type(JuniEnable):
    """Custom type juniIpAdEntIgmpEnable based on JuniEnable"""


_JuniIpAdEntIgmpEnable_Object = MibTableColumn
juniIpAdEntIgmpEnable = _JuniIpAdEntIgmpEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 2, 1, 10),
    _JuniIpAdEntIgmpEnable_Type()
)
juniIpAdEntIgmpEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpAdEntIgmpEnable.setStatus("deprecated")


class _JuniIpAdEntDirectedBcastEnable_Type(JuniEnable):
    """Custom type juniIpAdEntDirectedBcastEnable based on JuniEnable"""


_JuniIpAdEntDirectedBcastEnable_Object = MibTableColumn
juniIpAdEntDirectedBcastEnable = _JuniIpAdEntDirectedBcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 2, 1, 11),
    _JuniIpAdEntDirectedBcastEnable_Type()
)
juniIpAdEntDirectedBcastEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpAdEntDirectedBcastEnable.setStatus("current")


class _JuniIpAdEntIcmpRedirectEnable_Type(JuniEnable):
    """Custom type juniIpAdEntIcmpRedirectEnable based on JuniEnable"""


_JuniIpAdEntIcmpRedirectEnable_Object = MibTableColumn
juniIpAdEntIcmpRedirectEnable = _JuniIpAdEntIcmpRedirectEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 2, 1, 12),
    _JuniIpAdEntIcmpRedirectEnable_Type()
)
juniIpAdEntIcmpRedirectEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpAdEntIcmpRedirectEnable.setStatus("current")


class _JuniIpAdEntIcmpMaskReplyEnable_Type(JuniEnable):
    """Custom type juniIpAdEntIcmpMaskReplyEnable based on JuniEnable"""


_JuniIpAdEntIcmpMaskReplyEnable_Object = MibTableColumn
juniIpAdEntIcmpMaskReplyEnable = _JuniIpAdEntIcmpMaskReplyEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 2, 1, 13),
    _JuniIpAdEntIcmpMaskReplyEnable_Type()
)
juniIpAdEntIcmpMaskReplyEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpAdEntIcmpMaskReplyEnable.setStatus("current")


class _JuniIpAdEntIcmpUnreachEnable_Type(JuniEnable):
    """Custom type juniIpAdEntIcmpUnreachEnable based on JuniEnable"""


_JuniIpAdEntIcmpUnreachEnable_Object = MibTableColumn
juniIpAdEntIcmpUnreachEnable = _JuniIpAdEntIcmpUnreachEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 2, 1, 14),
    _JuniIpAdEntIcmpUnreachEnable_Type()
)
juniIpAdEntIcmpUnreachEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpAdEntIcmpUnreachEnable.setStatus("current")


class _JuniIpAdEntMtu_Type(Integer32):
    """Custom type juniIpAdEntMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniIpAdEntMtu_Type.__name__ = "Integer32"
_JuniIpAdEntMtu_Object = MibTableColumn
juniIpAdEntMtu = _JuniIpAdEntMtu_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 2, 1, 15),
    _JuniIpAdEntMtu_Type()
)
juniIpAdEntMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpAdEntMtu.setStatus("current")


class _JuniIpAdEntUnnumLoopbackIfIndex_Type(InterfaceIndexOrZero):
    """Custom type juniIpAdEntUnnumLoopbackIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_JuniIpAdEntUnnumLoopbackIfIndex_Object = MibTableColumn
juniIpAdEntUnnumLoopbackIfIndex = _JuniIpAdEntUnnumLoopbackIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 2, 1, 16),
    _JuniIpAdEntUnnumLoopbackIfIndex_Type()
)
juniIpAdEntUnnumLoopbackIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpAdEntUnnumLoopbackIfIndex.setStatus("deprecated")


class _JuniIpAdEntIrdpEnable_Type(JuniEnable):
    """Custom type juniIpAdEntIrdpEnable based on JuniEnable"""


_JuniIpAdEntIrdpEnable_Object = MibTableColumn
juniIpAdEntIrdpEnable = _JuniIpAdEntIrdpEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 2, 1, 17),
    _JuniIpAdEntIrdpEnable_Type()
)
juniIpAdEntIrdpEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpAdEntIrdpEnable.setStatus("current")


class _JuniIpAdEntAccessRouteEnable_Type(JuniEnable):
    """Custom type juniIpAdEntAccessRouteEnable based on JuniEnable"""


_JuniIpAdEntAccessRouteEnable_Object = MibTableColumn
juniIpAdEntAccessRouteEnable = _JuniIpAdEntAccessRouteEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 2, 1, 18),
    _JuniIpAdEntAccessRouteEnable_Type()
)
juniIpAdEntAccessRouteEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpAdEntAccessRouteEnable.setStatus("current")
_JuniIpAdEntAccessRouteHost_Type = IpAddress
_JuniIpAdEntAccessRouteHost_Object = MibTableColumn
juniIpAdEntAccessRouteHost = _JuniIpAdEntAccessRouteHost_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 2, 1, 19),
    _JuniIpAdEntAccessRouteHost_Type()
)
juniIpAdEntAccessRouteHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpAdEntAccessRouteHost.setStatus("current")


class _JuniIpAdEntIsSecondary_Type(JuniEnable):
    """Custom type juniIpAdEntIsSecondary based on JuniEnable"""


_JuniIpAdEntIsSecondary_Object = MibTableColumn
juniIpAdEntIsSecondary = _JuniIpAdEntIsSecondary_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 2, 1, 20),
    _JuniIpAdEntIsSecondary_Type()
)
juniIpAdEntIsSecondary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpAdEntIsSecondary.setStatus("current")


class _JuniIpAdEntUnnumInheritNumIfIndex_Type(InterfaceIndexOrZero):
    """Custom type juniIpAdEntUnnumInheritNumIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_JuniIpAdEntUnnumInheritNumIfIndex_Object = MibTableColumn
juniIpAdEntUnnumInheritNumIfIndex = _JuniIpAdEntUnnumInheritNumIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 2, 2, 1, 21),
    _JuniIpAdEntUnnumInheritNumIfIndex_Type()
)
juniIpAdEntUnnumInheritNumIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpAdEntUnnumInheritNumIfIndex.setStatus("current")
_JuniIpRoute_ObjectIdentity = ObjectIdentity
juniIpRoute = _JuniIpRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3)
)
_JuniIpRouteGlobals_ObjectIdentity = ObjectIdentity
juniIpRouteGlobals = _JuniIpRouteGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3, 1)
)
_JuniIpRouteLimit_Type = Integer32
_JuniIpRouteLimit_Object = MibScalar
juniIpRouteLimit = _JuniIpRouteLimit_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3, 1, 1),
    _JuniIpRouteLimit_Type()
)
juniIpRouteLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIpRouteLimit.setStatus("obsolete")


class _JuniIpRouteTableLimit_Type(Unsigned32):
    """Custom type juniIpRouteTableLimit based on Unsigned32"""
    defaultValue = 0


_JuniIpRouteTableLimit_Object = MibScalar
juniIpRouteTableLimit = _JuniIpRouteTableLimit_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3, 1, 2),
    _JuniIpRouteTableLimit_Type()
)
juniIpRouteTableLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIpRouteTableLimit.setStatus("current")


class _JuniIpRouteTableWarnPercent_Type(Unsigned32):
    """Custom type juniIpRouteTableWarnPercent based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_JuniIpRouteTableWarnPercent_Type.__name__ = "Unsigned32"
_JuniIpRouteTableWarnPercent_Object = MibScalar
juniIpRouteTableWarnPercent = _JuniIpRouteTableWarnPercent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3, 1, 3),
    _JuniIpRouteTableWarnPercent_Type()
)
juniIpRouteTableWarnPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIpRouteTableWarnPercent.setStatus("current")


class _JuniIpRouteTableWarnOnly_Type(TruthValue):
    """Custom type juniIpRouteTableWarnOnly based on TruthValue"""


_JuniIpRouteTableWarnOnly_Object = MibScalar
juniIpRouteTableWarnOnly = _JuniIpRouteTableWarnOnly_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3, 1, 4),
    _JuniIpRouteTableWarnOnly_Type()
)
juniIpRouteTableWarnOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIpRouteTableWarnOnly.setStatus("current")
_JuniIpRouteTableWarnThreshold_Type = Unsigned32
_JuniIpRouteTableWarnThreshold_Object = MibScalar
juniIpRouteTableWarnThreshold = _JuniIpRouteTableWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3, 1, 5),
    _JuniIpRouteTableWarnThreshold_Type()
)
juniIpRouteTableWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteTableWarnThreshold.setStatus("current")
_JuniIpRouteStaticTable_Object = MibTable
juniIpRouteStaticTable = _JuniIpRouteStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3, 2)
)
if mibBuilder.loadTexts:
    juniIpRouteStaticTable.setStatus("current")
_JuniIpRouteStaticEntry_Object = MibTableRow
juniIpRouteStaticEntry = _JuniIpRouteStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3, 2, 1)
)
juniIpRouteStaticEntry.setIndexNames(
    (0, "Juniper-IP-MIB", "juniIpRouteStaticDest"),
    (0, "Juniper-IP-MIB", "juniIpRouteStaticMask"),
    (0, "Juniper-IP-MIB", "juniIpRouteStaticPref"),
    (0, "Juniper-IP-MIB", "juniIpRouteStaticNextHop"),
)
if mibBuilder.loadTexts:
    juniIpRouteStaticEntry.setStatus("current")
_JuniIpRouteStaticDest_Type = IpAddress
_JuniIpRouteStaticDest_Object = MibTableColumn
juniIpRouteStaticDest = _JuniIpRouteStaticDest_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3, 2, 1, 1),
    _JuniIpRouteStaticDest_Type()
)
juniIpRouteStaticDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteStaticDest.setStatus("current")
_JuniIpRouteStaticMask_Type = IpAddress
_JuniIpRouteStaticMask_Object = MibTableColumn
juniIpRouteStaticMask = _JuniIpRouteStaticMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3, 2, 1, 2),
    _JuniIpRouteStaticMask_Type()
)
juniIpRouteStaticMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteStaticMask.setStatus("current")


class _JuniIpRouteStaticPref_Type(Integer32):
    """Custom type juniIpRouteStaticPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniIpRouteStaticPref_Type.__name__ = "Integer32"
_JuniIpRouteStaticPref_Object = MibTableColumn
juniIpRouteStaticPref = _JuniIpRouteStaticPref_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3, 2, 1, 3),
    _JuniIpRouteStaticPref_Type()
)
juniIpRouteStaticPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteStaticPref.setStatus("current")
_JuniIpRouteStaticNextHop_Type = JuniIpAddrLessIf
_JuniIpRouteStaticNextHop_Object = MibTableColumn
juniIpRouteStaticNextHop = _JuniIpRouteStaticNextHop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3, 2, 1, 4),
    _JuniIpRouteStaticNextHop_Type()
)
juniIpRouteStaticNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteStaticNextHop.setStatus("current")
_JuniIpRouteStaticRowStatus_Type = RowStatus
_JuniIpRouteStaticRowStatus_Object = MibTableColumn
juniIpRouteStaticRowStatus = _JuniIpRouteStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3, 2, 1, 5),
    _JuniIpRouteStaticRowStatus_Type()
)
juniIpRouteStaticRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpRouteStaticRowStatus.setStatus("current")


class _JuniIpRouteStaticIfIndex_Type(Integer32):
    """Custom type juniIpRouteStaticIfIndex based on Integer32"""
    defaultValue = 0


_JuniIpRouteStaticIfIndex_Object = MibTableColumn
juniIpRouteStaticIfIndex = _JuniIpRouteStaticIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3, 2, 1, 6),
    _JuniIpRouteStaticIfIndex_Type()
)
juniIpRouteStaticIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpRouteStaticIfIndex.setStatus("current")


class _JuniIpRouteStaticStatus_Type(Integer32):
    """Custom type juniIpRouteStaticStatus based on Integer32"""
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


_JuniIpRouteStaticStatus_Type.__name__ = "Integer32"
_JuniIpRouteStaticStatus_Object = MibTableColumn
juniIpRouteStaticStatus = _JuniIpRouteStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3, 2, 1, 7),
    _JuniIpRouteStaticStatus_Type()
)
juniIpRouteStaticStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteStaticStatus.setStatus("current")


class _JuniIpRouteStaticNextHopAS_Type(Integer32):
    """Custom type juniIpRouteStaticNextHopAS based on Integer32"""
    defaultValue = 0


_JuniIpRouteStaticNextHopAS_Object = MibTableColumn
juniIpRouteStaticNextHopAS = _JuniIpRouteStaticNextHopAS_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3, 2, 1, 8),
    _JuniIpRouteStaticNextHopAS_Type()
)
juniIpRouteStaticNextHopAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpRouteStaticNextHopAS.setStatus("current")


class _JuniIpRouteStaticMetric_Type(Integer32):
    """Custom type juniIpRouteStaticMetric based on Integer32"""
    defaultValue = -1


_JuniIpRouteStaticMetric_Object = MibTableColumn
juniIpRouteStaticMetric = _JuniIpRouteStaticMetric_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3, 2, 1, 9),
    _JuniIpRouteStaticMetric_Type()
)
juniIpRouteStaticMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpRouteStaticMetric.setStatus("current")


class _JuniIpRouteStaticTag_Type(Unsigned32):
    """Custom type juniIpRouteStaticTag based on Unsigned32"""
    defaultValue = 0


_JuniIpRouteStaticTag_Object = MibTableColumn
juniIpRouteStaticTag = _JuniIpRouteStaticTag_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3, 2, 1, 10),
    _JuniIpRouteStaticTag_Type()
)
juniIpRouteStaticTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpRouteStaticTag.setStatus("current")
_JuniIpCidrRouteTable_Object = MibTable
juniIpCidrRouteTable = _JuniIpCidrRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3, 3)
)
if mibBuilder.loadTexts:
    juniIpCidrRouteTable.setStatus("current")
_JuniIpCidrRouteEntry_Object = MibTableRow
juniIpCidrRouteEntry = _JuniIpCidrRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    juniIpCidrRouteEntry.setStatus("current")


class _JuniIpCidrRoutePref_Type(Integer32):
    """Custom type juniIpCidrRoutePref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniIpCidrRoutePref_Type.__name__ = "Integer32"
_JuniIpCidrRoutePref_Object = MibTableColumn
juniIpCidrRoutePref = _JuniIpCidrRoutePref_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3, 3, 1, 1),
    _JuniIpCidrRoutePref_Type()
)
juniIpCidrRoutePref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpCidrRoutePref.setStatus("current")
_JuniIpCidrRouteArea_Type = IpAddress
_JuniIpCidrRouteArea_Object = MibTableColumn
juniIpCidrRouteArea = _JuniIpCidrRouteArea_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3, 3, 1, 2),
    _JuniIpCidrRouteArea_Type()
)
juniIpCidrRouteArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpCidrRouteArea.setStatus("current")
_JuniIpCidrRouteTag_Type = Unsigned32
_JuniIpCidrRouteTag_Object = MibTableColumn
juniIpCidrRouteTag = _JuniIpCidrRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3, 3, 1, 3),
    _JuniIpCidrRouteTag_Type()
)
juniIpCidrRouteTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpCidrRouteTag.setStatus("current")
_JuniIpRouteStaticBFDTable_Object = MibTable
juniIpRouteStaticBFDTable = _JuniIpRouteStaticBFDTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3, 4)
)
if mibBuilder.loadTexts:
    juniIpRouteStaticBFDTable.setStatus("current")
_JuniIpRouteStaticBFDEntry_Object = MibTableRow
juniIpRouteStaticBFDEntry = _JuniIpRouteStaticBFDEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    juniIpRouteStaticBFDEntry.setStatus("current")


class _JuniIpRouteStaticBfdEnable_Type(TruthValue):
    """Custom type juniIpRouteStaticBfdEnable based on TruthValue"""


_JuniIpRouteStaticBfdEnable_Object = MibTableColumn
juniIpRouteStaticBfdEnable = _JuniIpRouteStaticBfdEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3, 4, 1, 1),
    _JuniIpRouteStaticBfdEnable_Type()
)
juniIpRouteStaticBfdEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpRouteStaticBfdEnable.setStatus("current")


class _JuniIpRouteStaticBfdMinRxInterval_Type(Integer32):
    """Custom type juniIpRouteStaticBfdMinRxInterval based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 65535),
    )


_JuniIpRouteStaticBfdMinRxInterval_Type.__name__ = "Integer32"
_JuniIpRouteStaticBfdMinRxInterval_Object = MibTableColumn
juniIpRouteStaticBfdMinRxInterval = _JuniIpRouteStaticBfdMinRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3, 4, 1, 2),
    _JuniIpRouteStaticBfdMinRxInterval_Type()
)
juniIpRouteStaticBfdMinRxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpRouteStaticBfdMinRxInterval.setStatus("current")


class _JuniIpRouteStaticBfdMinTxInterval_Type(Integer32):
    """Custom type juniIpRouteStaticBfdMinTxInterval based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 65535),
    )


_JuniIpRouteStaticBfdMinTxInterval_Type.__name__ = "Integer32"
_JuniIpRouteStaticBfdMinTxInterval_Object = MibTableColumn
juniIpRouteStaticBfdMinTxInterval = _JuniIpRouteStaticBfdMinTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3, 4, 1, 3),
    _JuniIpRouteStaticBfdMinTxInterval_Type()
)
juniIpRouteStaticBfdMinTxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpRouteStaticBfdMinTxInterval.setStatus("current")


class _JuniIpRouteStaticBfdMultiplier_Type(Integer32):
    """Custom type juniIpRouteStaticBfdMultiplier based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_JuniIpRouteStaticBfdMultiplier_Type.__name__ = "Integer32"
_JuniIpRouteStaticBfdMultiplier_Object = MibTableColumn
juniIpRouteStaticBfdMultiplier = _JuniIpRouteStaticBfdMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 3, 4, 1, 4),
    _JuniIpRouteStaticBfdMultiplier_Type()
)
juniIpRouteStaticBfdMultiplier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpRouteStaticBfdMultiplier.setStatus("current")
_JuniIpGlobals_ObjectIdentity = ObjectIdentity
juniIpGlobals = _JuniIpGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 4)
)


class _JuniIpDebounceTime_Type(Integer32):
    """Custom type juniIpDebounceTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_JuniIpDebounceTime_Type.__name__ = "Integer32"
_JuniIpDebounceTime_Object = MibScalar
juniIpDebounceTime = _JuniIpDebounceTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 4, 1),
    _JuniIpDebounceTime_Type()
)
juniIpDebounceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIpDebounceTime.setStatus("current")
if mibBuilder.loadTexts:
    juniIpDebounceTime.setUnits("milliseconds")
_JuniIpRouterId_Type = IpAddress
_JuniIpRouterId_Object = MibScalar
juniIpRouterId = _JuniIpRouterId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 4, 2),
    _JuniIpRouterId_Type()
)
juniIpRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIpRouterId.setStatus("current")
_JuniIpSourceRoutingAdminStatus_Type = JuniEnable
_JuniIpSourceRoutingAdminStatus_Object = MibScalar
juniIpSourceRoutingAdminStatus = _JuniIpSourceRoutingAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 4, 3),
    _JuniIpSourceRoutingAdminStatus_Type()
)
juniIpSourceRoutingAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIpSourceRoutingAdminStatus.setStatus("current")


class _JuniIpVpnIdOui_Type(Integer32):
    """Custom type juniIpVpnIdOui based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_JuniIpVpnIdOui_Type.__name__ = "Integer32"
_JuniIpVpnIdOui_Object = MibScalar
juniIpVpnIdOui = _JuniIpVpnIdOui_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 4, 4),
    _JuniIpVpnIdOui_Type()
)
juniIpVpnIdOui.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIpVpnIdOui.setStatus("obsolete")
_JuniIpVpnIdIndex_Type = IpAddress
_JuniIpVpnIdIndex_Object = MibScalar
juniIpVpnIdIndex = _JuniIpVpnIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 4, 5),
    _JuniIpVpnIdIndex_Type()
)
juniIpVpnIdIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIpVpnIdIndex.setStatus("obsolete")


class _JuniIpBgpCommunityNewFormat_Type(TruthValue):
    """Custom type juniIpBgpCommunityNewFormat based on TruthValue"""


_JuniIpBgpCommunityNewFormat_Object = MibScalar
juniIpBgpCommunityNewFormat = _JuniIpBgpCommunityNewFormat_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 4, 6),
    _JuniIpBgpCommunityNewFormat_Type()
)
juniIpBgpCommunityNewFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIpBgpCommunityNewFormat.setStatus("current")


class _JuniIpBgpAsConfedSetNewFormat_Type(TruthValue):
    """Custom type juniIpBgpAsConfedSetNewFormat based on TruthValue"""


_JuniIpBgpAsConfedSetNewFormat_Object = MibScalar
juniIpBgpAsConfedSetNewFormat = _JuniIpBgpAsConfedSetNewFormat_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 4, 7),
    _JuniIpBgpAsConfedSetNewFormat_Type()
)
juniIpBgpAsConfedSetNewFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIpBgpAsConfedSetNewFormat.setStatus("current")
_JuniIpIfSummary_ObjectIdentity = ObjectIdentity
juniIpIfSummary = _JuniIpIfSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 5)
)
_JuniIpIfSummaryTotalIntf_Type = Gauge32
_JuniIpIfSummaryTotalIntf_Object = MibScalar
juniIpIfSummaryTotalIntf = _JuniIpIfSummaryTotalIntf_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 5, 1),
    _JuniIpIfSummaryTotalIntf_Type()
)
juniIpIfSummaryTotalIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpIfSummaryTotalIntf.setStatus("current")
_JuniIpIfSummaryTotalIntfUp_Type = Gauge32
_JuniIpIfSummaryTotalIntfUp_Object = MibScalar
juniIpIfSummaryTotalIntfUp = _JuniIpIfSummaryTotalIntfUp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 5, 2),
    _JuniIpIfSummaryTotalIntfUp_Type()
)
juniIpIfSummaryTotalIntfUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpIfSummaryTotalIntfUp.setStatus("current")
_JuniIpIfSummaryTotalIntfDown_Type = Gauge32
_JuniIpIfSummaryTotalIntfDown_Object = MibScalar
juniIpIfSummaryTotalIntfDown = _JuniIpIfSummaryTotalIntfDown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 5, 3),
    _JuniIpIfSummaryTotalIntfDown_Type()
)
juniIpIfSummaryTotalIntfDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpIfSummaryTotalIntfDown.setStatus("current")
_JuniIpIfSummaryTotalIntfProtUp_Type = Gauge32
_JuniIpIfSummaryTotalIntfProtUp_Object = MibScalar
juniIpIfSummaryTotalIntfProtUp = _JuniIpIfSummaryTotalIntfProtUp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 5, 4),
    _JuniIpIfSummaryTotalIntfProtUp_Type()
)
juniIpIfSummaryTotalIntfProtUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpIfSummaryTotalIntfProtUp.setStatus("current")
_JuniIpIfSummaryTotalIntfProtDown_Type = Gauge32
_JuniIpIfSummaryTotalIntfProtDown_Object = MibScalar
juniIpIfSummaryTotalIntfProtDown = _JuniIpIfSummaryTotalIntfProtDown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 5, 5),
    _JuniIpIfSummaryTotalIntfProtDown_Type()
)
juniIpIfSummaryTotalIntfProtDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpIfSummaryTotalIntfProtDown.setStatus("current")
_JuniIpIfSummaryTotalIntfProtNotPresent_Type = Gauge32
_JuniIpIfSummaryTotalIntfProtNotPresent_Object = MibScalar
juniIpIfSummaryTotalIntfProtNotPresent = _JuniIpIfSummaryTotalIntfProtNotPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 5, 6),
    _JuniIpIfSummaryTotalIntfProtNotPresent_Type()
)
juniIpIfSummaryTotalIntfProtNotPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpIfSummaryTotalIntfProtNotPresent.setStatus("current")
_JuniIpRouteSummary_ObjectIdentity = ObjectIdentity
juniIpRouteSummary = _JuniIpRouteSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 6)
)
_JuniIpRouteUnicastSummary_ObjectIdentity = ObjectIdentity
juniIpRouteUnicastSummary = _JuniIpRouteUnicastSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 6, 1)
)
_JuniIpRouteSummaryUnicastTotalRoutes_Type = Gauge32
_JuniIpRouteSummaryUnicastTotalRoutes_Object = MibScalar
juniIpRouteSummaryUnicastTotalRoutes = _JuniIpRouteSummaryUnicastTotalRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 6, 1, 1),
    _JuniIpRouteSummaryUnicastTotalRoutes_Type()
)
juniIpRouteSummaryUnicastTotalRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteSummaryUnicastTotalRoutes.setStatus("current")
_JuniIpRouteSummaryUnicastTotalBytes_Type = Gauge32
_JuniIpRouteSummaryUnicastTotalBytes_Object = MibScalar
juniIpRouteSummaryUnicastTotalBytes = _JuniIpRouteSummaryUnicastTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 6, 1, 2),
    _JuniIpRouteSummaryUnicastTotalBytes_Type()
)
juniIpRouteSummaryUnicastTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteSummaryUnicastTotalBytes.setStatus("current")
_JuniIpRouteSummaryUnicastIsisRoutes_Type = Gauge32
_JuniIpRouteSummaryUnicastIsisRoutes_Object = MibScalar
juniIpRouteSummaryUnicastIsisRoutes = _JuniIpRouteSummaryUnicastIsisRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 6, 1, 3),
    _JuniIpRouteSummaryUnicastIsisRoutes_Type()
)
juniIpRouteSummaryUnicastIsisRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteSummaryUnicastIsisRoutes.setStatus("current")
_JuniIpRouteSummaryUnicastIsisLevel1Routes_Type = Gauge32
_JuniIpRouteSummaryUnicastIsisLevel1Routes_Object = MibScalar
juniIpRouteSummaryUnicastIsisLevel1Routes = _JuniIpRouteSummaryUnicastIsisLevel1Routes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 6, 1, 4),
    _JuniIpRouteSummaryUnicastIsisLevel1Routes_Type()
)
juniIpRouteSummaryUnicastIsisLevel1Routes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteSummaryUnicastIsisLevel1Routes.setStatus("current")
_JuniIpRouteSummaryUnicastIsisLevel2Routes_Type = Gauge32
_JuniIpRouteSummaryUnicastIsisLevel2Routes_Object = MibScalar
juniIpRouteSummaryUnicastIsisLevel2Routes = _JuniIpRouteSummaryUnicastIsisLevel2Routes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 6, 1, 5),
    _JuniIpRouteSummaryUnicastIsisLevel2Routes_Type()
)
juniIpRouteSummaryUnicastIsisLevel2Routes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteSummaryUnicastIsisLevel2Routes.setStatus("current")
_JuniIpRouteSummaryUnicastRipRoutes_Type = Gauge32
_JuniIpRouteSummaryUnicastRipRoutes_Object = MibScalar
juniIpRouteSummaryUnicastRipRoutes = _JuniIpRouteSummaryUnicastRipRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 6, 1, 6),
    _JuniIpRouteSummaryUnicastRipRoutes_Type()
)
juniIpRouteSummaryUnicastRipRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteSummaryUnicastRipRoutes.setStatus("current")
_JuniIpRouteSummaryUnicastStaticRoutes_Type = Gauge32
_JuniIpRouteSummaryUnicastStaticRoutes_Object = MibScalar
juniIpRouteSummaryUnicastStaticRoutes = _JuniIpRouteSummaryUnicastStaticRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 6, 1, 7),
    _JuniIpRouteSummaryUnicastStaticRoutes_Type()
)
juniIpRouteSummaryUnicastStaticRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteSummaryUnicastStaticRoutes.setStatus("current")
_JuniIpRouteSummaryUnicastConnectedRoutes_Type = Gauge32
_JuniIpRouteSummaryUnicastConnectedRoutes_Object = MibScalar
juniIpRouteSummaryUnicastConnectedRoutes = _JuniIpRouteSummaryUnicastConnectedRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 6, 1, 8),
    _JuniIpRouteSummaryUnicastConnectedRoutes_Type()
)
juniIpRouteSummaryUnicastConnectedRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteSummaryUnicastConnectedRoutes.setStatus("current")
_JuniIpRouteSummaryUnicastBgpRoutes_Type = Gauge32
_JuniIpRouteSummaryUnicastBgpRoutes_Object = MibScalar
juniIpRouteSummaryUnicastBgpRoutes = _JuniIpRouteSummaryUnicastBgpRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 6, 1, 9),
    _JuniIpRouteSummaryUnicastBgpRoutes_Type()
)
juniIpRouteSummaryUnicastBgpRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteSummaryUnicastBgpRoutes.setStatus("current")
_JuniIpRouteSummaryUnicastOspfRoutes_Type = Gauge32
_JuniIpRouteSummaryUnicastOspfRoutes_Object = MibScalar
juniIpRouteSummaryUnicastOspfRoutes = _JuniIpRouteSummaryUnicastOspfRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 6, 1, 10),
    _JuniIpRouteSummaryUnicastOspfRoutes_Type()
)
juniIpRouteSummaryUnicastOspfRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteSummaryUnicastOspfRoutes.setStatus("current")
_JuniIpRouteSummaryUnicastIntraAreaOspfRoutes_Type = Gauge32
_JuniIpRouteSummaryUnicastIntraAreaOspfRoutes_Object = MibScalar
juniIpRouteSummaryUnicastIntraAreaOspfRoutes = _JuniIpRouteSummaryUnicastIntraAreaOspfRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 6, 1, 11),
    _JuniIpRouteSummaryUnicastIntraAreaOspfRoutes_Type()
)
juniIpRouteSummaryUnicastIntraAreaOspfRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteSummaryUnicastIntraAreaOspfRoutes.setStatus("current")
_JuniIpRouteSummaryUnicastInterAreaOspfRoutes_Type = Gauge32
_JuniIpRouteSummaryUnicastInterAreaOspfRoutes_Object = MibScalar
juniIpRouteSummaryUnicastInterAreaOspfRoutes = _JuniIpRouteSummaryUnicastInterAreaOspfRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 6, 1, 12),
    _JuniIpRouteSummaryUnicastInterAreaOspfRoutes_Type()
)
juniIpRouteSummaryUnicastInterAreaOspfRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteSummaryUnicastInterAreaOspfRoutes.setStatus("current")
_JuniIpRouteSummaryUnicastExternalOspfRoutes_Type = Gauge32
_JuniIpRouteSummaryUnicastExternalOspfRoutes_Object = MibScalar
juniIpRouteSummaryUnicastExternalOspfRoutes = _JuniIpRouteSummaryUnicastExternalOspfRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 6, 1, 13),
    _JuniIpRouteSummaryUnicastExternalOspfRoutes_Type()
)
juniIpRouteSummaryUnicastExternalOspfRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteSummaryUnicastExternalOspfRoutes.setStatus("current")
_JuniIpRouteSummaryUnicastOtherInternalRoutes_Type = Gauge32
_JuniIpRouteSummaryUnicastOtherInternalRoutes_Object = MibScalar
juniIpRouteSummaryUnicastOtherInternalRoutes = _JuniIpRouteSummaryUnicastOtherInternalRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 6, 1, 14),
    _JuniIpRouteSummaryUnicastOtherInternalRoutes_Type()
)
juniIpRouteSummaryUnicastOtherInternalRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteSummaryUnicastOtherInternalRoutes.setStatus("current")
_JuniIpRouteSummaryUnicastAccessRoutes_Type = Gauge32
_JuniIpRouteSummaryUnicastAccessRoutes_Object = MibScalar
juniIpRouteSummaryUnicastAccessRoutes = _JuniIpRouteSummaryUnicastAccessRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 6, 1, 15),
    _JuniIpRouteSummaryUnicastAccessRoutes_Type()
)
juniIpRouteSummaryUnicastAccessRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteSummaryUnicastAccessRoutes.setStatus("current")
_JuniIpRouteSummaryUnicastIntCreatedAccessHostRoutes_Type = Gauge32
_JuniIpRouteSummaryUnicastIntCreatedAccessHostRoutes_Object = MibScalar
juniIpRouteSummaryUnicastIntCreatedAccessHostRoutes = _JuniIpRouteSummaryUnicastIntCreatedAccessHostRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 6, 1, 16),
    _JuniIpRouteSummaryUnicastIntCreatedAccessHostRoutes_Type()
)
juniIpRouteSummaryUnicastIntCreatedAccessHostRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteSummaryUnicastIntCreatedAccessHostRoutes.setStatus("current")
_JuniIpRouteSummaryUnicastIntDialoutRoutes_Type = Gauge32
_JuniIpRouteSummaryUnicastIntDialoutRoutes_Object = MibScalar
juniIpRouteSummaryUnicastIntDialoutRoutes = _JuniIpRouteSummaryUnicastIntDialoutRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 6, 1, 17),
    _JuniIpRouteSummaryUnicastIntDialoutRoutes_Type()
)
juniIpRouteSummaryUnicastIntDialoutRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteSummaryUnicastIntDialoutRoutes.setStatus("current")
_JuniIpRouteSummaryUnicastRouteMemoryActive_Type = Gauge32
_JuniIpRouteSummaryUnicastRouteMemoryActive_Object = MibScalar
juniIpRouteSummaryUnicastRouteMemoryActive = _JuniIpRouteSummaryUnicastRouteMemoryActive_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 6, 1, 18),
    _JuniIpRouteSummaryUnicastRouteMemoryActive_Type()
)
juniIpRouteSummaryUnicastRouteMemoryActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteSummaryUnicastRouteMemoryActive.setStatus("current")
_JuniIpRouteSummaryUnicastLastRouteAddedOrDeletedIP_Type = IpAddress
_JuniIpRouteSummaryUnicastLastRouteAddedOrDeletedIP_Object = MibScalar
juniIpRouteSummaryUnicastLastRouteAddedOrDeletedIP = _JuniIpRouteSummaryUnicastLastRouteAddedOrDeletedIP_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 6, 1, 19),
    _JuniIpRouteSummaryUnicastLastRouteAddedOrDeletedIP_Type()
)
juniIpRouteSummaryUnicastLastRouteAddedOrDeletedIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteSummaryUnicastLastRouteAddedOrDeletedIP.setStatus("current")
_JuniIpRouteSummaryUnicastLastRouteAddedOrDeletedMask_Type = IpAddress
_JuniIpRouteSummaryUnicastLastRouteAddedOrDeletedMask_Object = MibScalar
juniIpRouteSummaryUnicastLastRouteAddedOrDeletedMask = _JuniIpRouteSummaryUnicastLastRouteAddedOrDeletedMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 6, 1, 20),
    _JuniIpRouteSummaryUnicastLastRouteAddedOrDeletedMask_Type()
)
juniIpRouteSummaryUnicastLastRouteAddedOrDeletedMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteSummaryUnicastLastRouteAddedOrDeletedMask.setStatus("current")


class _JuniIpRouteSummaryUnicastLastRouteAddedOrDeletedClient_Type(Integer32):
    """Custom type juniIpRouteSummaryUnicastLastRouteAddedOrDeletedClient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("access", 14),
          ("accessInternal", 15),
          ("bgp", 6),
          ("default", 17),
          ("dialOut", 16),
          ("dvmrp", 11),
          ("dvmrpAggregate", 12),
          ("hidden", 13),
          ("inValid", 0),
          ("isis", 1),
          ("local", 5),
          ("mbgp", 7),
          ("ospf", 3),
          ("ospfExternal", 10),
          ("ospfInternal", 9),
          ("rip", 2),
          ("static", 4),
          ("staticLow", 8))
    )


_JuniIpRouteSummaryUnicastLastRouteAddedOrDeletedClient_Type.__name__ = "Integer32"
_JuniIpRouteSummaryUnicastLastRouteAddedOrDeletedClient_Object = MibScalar
juniIpRouteSummaryUnicastLastRouteAddedOrDeletedClient = _JuniIpRouteSummaryUnicastLastRouteAddedOrDeletedClient_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 6, 1, 21),
    _JuniIpRouteSummaryUnicastLastRouteAddedOrDeletedClient_Type()
)
juniIpRouteSummaryUnicastLastRouteAddedOrDeletedClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteSummaryUnicastLastRouteAddedOrDeletedClient.setStatus("current")


class _JuniIpRouteSummaryUnicastLastRouteAddedOrDeletedDate_Type(OctetString):
    """Custom type juniIpRouteSummaryUnicastLastRouteAddedOrDeletedDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_JuniIpRouteSummaryUnicastLastRouteAddedOrDeletedDate_Type.__name__ = "OctetString"
_JuniIpRouteSummaryUnicastLastRouteAddedOrDeletedDate_Object = MibScalar
juniIpRouteSummaryUnicastLastRouteAddedOrDeletedDate = _JuniIpRouteSummaryUnicastLastRouteAddedOrDeletedDate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 6, 1, 22),
    _JuniIpRouteSummaryUnicastLastRouteAddedOrDeletedDate_Type()
)
juniIpRouteSummaryUnicastLastRouteAddedOrDeletedDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteSummaryUnicastLastRouteAddedOrDeletedDate.setStatus("current")
_JuniIpRouteMulticastSummary_ObjectIdentity = ObjectIdentity
juniIpRouteMulticastSummary = _JuniIpRouteMulticastSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 6, 2)
)
_JuniIpRouteSummaryMulticastTotalRoutes_Type = Gauge32
_JuniIpRouteSummaryMulticastTotalRoutes_Object = MibScalar
juniIpRouteSummaryMulticastTotalRoutes = _JuniIpRouteSummaryMulticastTotalRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 6, 2, 1),
    _JuniIpRouteSummaryMulticastTotalRoutes_Type()
)
juniIpRouteSummaryMulticastTotalRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteSummaryMulticastTotalRoutes.setStatus("current")
_JuniIpRouteSummaryMulticastTotalBytes_Type = Gauge32
_JuniIpRouteSummaryMulticastTotalBytes_Object = MibScalar
juniIpRouteSummaryMulticastTotalBytes = _JuniIpRouteSummaryMulticastTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 6, 2, 2),
    _JuniIpRouteSummaryMulticastTotalBytes_Type()
)
juniIpRouteSummaryMulticastTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteSummaryMulticastTotalBytes.setStatus("current")
_JuniIpRouteSummaryMulticastIsisRoutes_Type = Gauge32
_JuniIpRouteSummaryMulticastIsisRoutes_Object = MibScalar
juniIpRouteSummaryMulticastIsisRoutes = _JuniIpRouteSummaryMulticastIsisRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 6, 2, 3),
    _JuniIpRouteSummaryMulticastIsisRoutes_Type()
)
juniIpRouteSummaryMulticastIsisRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteSummaryMulticastIsisRoutes.setStatus("current")
_JuniIpRouteSummaryMulticastLevel1IsisRoutes_Type = Gauge32
_JuniIpRouteSummaryMulticastLevel1IsisRoutes_Object = MibScalar
juniIpRouteSummaryMulticastLevel1IsisRoutes = _JuniIpRouteSummaryMulticastLevel1IsisRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 6, 2, 4),
    _JuniIpRouteSummaryMulticastLevel1IsisRoutes_Type()
)
juniIpRouteSummaryMulticastLevel1IsisRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteSummaryMulticastLevel1IsisRoutes.setStatus("current")
_JuniIpRouteSummaryMulticastLevel2IsisRoutes_Type = Gauge32
_JuniIpRouteSummaryMulticastLevel2IsisRoutes_Object = MibScalar
juniIpRouteSummaryMulticastLevel2IsisRoutes = _JuniIpRouteSummaryMulticastLevel2IsisRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 6, 2, 5),
    _JuniIpRouteSummaryMulticastLevel2IsisRoutes_Type()
)
juniIpRouteSummaryMulticastLevel2IsisRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteSummaryMulticastLevel2IsisRoutes.setStatus("current")
_JuniIpRouteSummaryMulticastRipRoutes_Type = Gauge32
_JuniIpRouteSummaryMulticastRipRoutes_Object = MibScalar
juniIpRouteSummaryMulticastRipRoutes = _JuniIpRouteSummaryMulticastRipRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 6, 2, 6),
    _JuniIpRouteSummaryMulticastRipRoutes_Type()
)
juniIpRouteSummaryMulticastRipRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteSummaryMulticastRipRoutes.setStatus("current")
_JuniIpRouteSummaryMulticastStaticRoutes_Type = Gauge32
_JuniIpRouteSummaryMulticastStaticRoutes_Object = MibScalar
juniIpRouteSummaryMulticastStaticRoutes = _JuniIpRouteSummaryMulticastStaticRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 6, 2, 7),
    _JuniIpRouteSummaryMulticastStaticRoutes_Type()
)
juniIpRouteSummaryMulticastStaticRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteSummaryMulticastStaticRoutes.setStatus("current")
_JuniIpRouteSummaryMulticastConnectedRoutes_Type = Gauge32
_JuniIpRouteSummaryMulticastConnectedRoutes_Object = MibScalar
juniIpRouteSummaryMulticastConnectedRoutes = _JuniIpRouteSummaryMulticastConnectedRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 6, 2, 8),
    _JuniIpRouteSummaryMulticastConnectedRoutes_Type()
)
juniIpRouteSummaryMulticastConnectedRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteSummaryMulticastConnectedRoutes.setStatus("current")
_JuniIpRouteSummaryMulticastBgpRoutes_Type = Gauge32
_JuniIpRouteSummaryMulticastBgpRoutes_Object = MibScalar
juniIpRouteSummaryMulticastBgpRoutes = _JuniIpRouteSummaryMulticastBgpRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 6, 2, 9),
    _JuniIpRouteSummaryMulticastBgpRoutes_Type()
)
juniIpRouteSummaryMulticastBgpRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteSummaryMulticastBgpRoutes.setStatus("current")
_JuniIpRouteSummaryMulticastOspfRoutes_Type = Gauge32
_JuniIpRouteSummaryMulticastOspfRoutes_Object = MibScalar
juniIpRouteSummaryMulticastOspfRoutes = _JuniIpRouteSummaryMulticastOspfRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 6, 2, 10),
    _JuniIpRouteSummaryMulticastOspfRoutes_Type()
)
juniIpRouteSummaryMulticastOspfRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteSummaryMulticastOspfRoutes.setStatus("current")
_JuniIpRouteSummaryMulticastIntraAreaOspfRoutes_Type = Gauge32
_JuniIpRouteSummaryMulticastIntraAreaOspfRoutes_Object = MibScalar
juniIpRouteSummaryMulticastIntraAreaOspfRoutes = _JuniIpRouteSummaryMulticastIntraAreaOspfRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 6, 2, 11),
    _JuniIpRouteSummaryMulticastIntraAreaOspfRoutes_Type()
)
juniIpRouteSummaryMulticastIntraAreaOspfRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteSummaryMulticastIntraAreaOspfRoutes.setStatus("current")
_JuniIpRouteSummaryMulticastInterAreaOspfRoutes_Type = Gauge32
_JuniIpRouteSummaryMulticastInterAreaOspfRoutes_Object = MibScalar
juniIpRouteSummaryMulticastInterAreaOspfRoutes = _JuniIpRouteSummaryMulticastInterAreaOspfRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 6, 2, 12),
    _JuniIpRouteSummaryMulticastInterAreaOspfRoutes_Type()
)
juniIpRouteSummaryMulticastInterAreaOspfRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteSummaryMulticastInterAreaOspfRoutes.setStatus("current")
_JuniIpRouteSummaryMulticastExternalOspfRoutes_Type = Gauge32
_JuniIpRouteSummaryMulticastExternalOspfRoutes_Object = MibScalar
juniIpRouteSummaryMulticastExternalOspfRoutes = _JuniIpRouteSummaryMulticastExternalOspfRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 6, 2, 13),
    _JuniIpRouteSummaryMulticastExternalOspfRoutes_Type()
)
juniIpRouteSummaryMulticastExternalOspfRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteSummaryMulticastExternalOspfRoutes.setStatus("current")
_JuniIpRouteSummaryMulticastOtherInternalRoutes_Type = Gauge32
_JuniIpRouteSummaryMulticastOtherInternalRoutes_Object = MibScalar
juniIpRouteSummaryMulticastOtherInternalRoutes = _JuniIpRouteSummaryMulticastOtherInternalRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 6, 2, 14),
    _JuniIpRouteSummaryMulticastOtherInternalRoutes_Type()
)
juniIpRouteSummaryMulticastOtherInternalRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteSummaryMulticastOtherInternalRoutes.setStatus("current")
_JuniIpRouteSummaryMulticastAccessRoutes_Type = Gauge32
_JuniIpRouteSummaryMulticastAccessRoutes_Object = MibScalar
juniIpRouteSummaryMulticastAccessRoutes = _JuniIpRouteSummaryMulticastAccessRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 6, 2, 15),
    _JuniIpRouteSummaryMulticastAccessRoutes_Type()
)
juniIpRouteSummaryMulticastAccessRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteSummaryMulticastAccessRoutes.setStatus("current")
_JuniIpRouteSummaryMulticastIntCreatedAccessHostRoutes_Type = Gauge32
_JuniIpRouteSummaryMulticastIntCreatedAccessHostRoutes_Object = MibScalar
juniIpRouteSummaryMulticastIntCreatedAccessHostRoutes = _JuniIpRouteSummaryMulticastIntCreatedAccessHostRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 6, 2, 16),
    _JuniIpRouteSummaryMulticastIntCreatedAccessHostRoutes_Type()
)
juniIpRouteSummaryMulticastIntCreatedAccessHostRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteSummaryMulticastIntCreatedAccessHostRoutes.setStatus("current")
_JuniIpRouteSummaryMultiastIntDialoutRoutes_Type = Gauge32
_JuniIpRouteSummaryMultiastIntDialoutRoutes_Object = MibScalar
juniIpRouteSummaryMultiastIntDialoutRoutes = _JuniIpRouteSummaryMultiastIntDialoutRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 6, 2, 17),
    _JuniIpRouteSummaryMultiastIntDialoutRoutes_Type()
)
juniIpRouteSummaryMultiastIntDialoutRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteSummaryMultiastIntDialoutRoutes.setStatus("current")
_JuniIpRouteSummaryMulticastRouteMemoryActive_Type = Gauge32
_JuniIpRouteSummaryMulticastRouteMemoryActive_Object = MibScalar
juniIpRouteSummaryMulticastRouteMemoryActive = _JuniIpRouteSummaryMulticastRouteMemoryActive_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 6, 2, 18),
    _JuniIpRouteSummaryMulticastRouteMemoryActive_Type()
)
juniIpRouteSummaryMulticastRouteMemoryActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteSummaryMulticastRouteMemoryActive.setStatus("current")
_JuniIpRouteSummaryMulticastLastRouteAddedOrDeletedIP_Type = IpAddress
_JuniIpRouteSummaryMulticastLastRouteAddedOrDeletedIP_Object = MibScalar
juniIpRouteSummaryMulticastLastRouteAddedOrDeletedIP = _JuniIpRouteSummaryMulticastLastRouteAddedOrDeletedIP_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 6, 2, 19),
    _JuniIpRouteSummaryMulticastLastRouteAddedOrDeletedIP_Type()
)
juniIpRouteSummaryMulticastLastRouteAddedOrDeletedIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteSummaryMulticastLastRouteAddedOrDeletedIP.setStatus("current")
_JuniIpRouteSummaryMulticastLastRouteAddedOrDeletedMask_Type = IpAddress
_JuniIpRouteSummaryMulticastLastRouteAddedOrDeletedMask_Object = MibScalar
juniIpRouteSummaryMulticastLastRouteAddedOrDeletedMask = _JuniIpRouteSummaryMulticastLastRouteAddedOrDeletedMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 6, 2, 20),
    _JuniIpRouteSummaryMulticastLastRouteAddedOrDeletedMask_Type()
)
juniIpRouteSummaryMulticastLastRouteAddedOrDeletedMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteSummaryMulticastLastRouteAddedOrDeletedMask.setStatus("current")


class _JuniIpRouteSummaryMulticastLastRouteAddedOrDeletedClient_Type(Integer32):
    """Custom type juniIpRouteSummaryMulticastLastRouteAddedOrDeletedClient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("access", 14),
          ("accessInternal", 15),
          ("bgp", 6),
          ("default", 17),
          ("dialOut", 16),
          ("dvmrp", 11),
          ("dvmrpAggregate", 12),
          ("hidden", 13),
          ("inValid", 0),
          ("isis", 1),
          ("local", 5),
          ("mbgp", 7),
          ("ospf", 3),
          ("ospfExternal", 10),
          ("ospfInternal", 9),
          ("rip", 2),
          ("static", 4),
          ("staticLow", 8))
    )


_JuniIpRouteSummaryMulticastLastRouteAddedOrDeletedClient_Type.__name__ = "Integer32"
_JuniIpRouteSummaryMulticastLastRouteAddedOrDeletedClient_Object = MibScalar
juniIpRouteSummaryMulticastLastRouteAddedOrDeletedClient = _JuniIpRouteSummaryMulticastLastRouteAddedOrDeletedClient_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 6, 2, 21),
    _JuniIpRouteSummaryMulticastLastRouteAddedOrDeletedClient_Type()
)
juniIpRouteSummaryMulticastLastRouteAddedOrDeletedClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteSummaryMulticastLastRouteAddedOrDeletedClient.setStatus("current")


class _JuniIpRouteSummaryMulticastLastRouteAddedOrDeletedDate_Type(OctetString):
    """Custom type juniIpRouteSummaryMulticastLastRouteAddedOrDeletedDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_JuniIpRouteSummaryMulticastLastRouteAddedOrDeletedDate_Type.__name__ = "OctetString"
_JuniIpRouteSummaryMulticastLastRouteAddedOrDeletedDate_Object = MibScalar
juniIpRouteSummaryMulticastLastRouteAddedOrDeletedDate = _JuniIpRouteSummaryMulticastLastRouteAddedOrDeletedDate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 1, 6, 2, 22),
    _JuniIpRouteSummaryMulticastLastRouteAddedOrDeletedDate_Type()
)
juniIpRouteSummaryMulticastLastRouteAddedOrDeletedDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteSummaryMulticastLastRouteAddedOrDeletedDate.setStatus("current")
_JuniIpTrapEnables_ObjectIdentity = ObjectIdentity
juniIpTrapEnables = _JuniIpTrapEnables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 2)
)


class _JuniIpSaValidateTrapEnable_Type(TruthValue):
    """Custom type juniIpSaValidateTrapEnable based on TruthValue"""


_JuniIpSaValidateTrapEnable_Object = MibScalar
juniIpSaValidateTrapEnable = _JuniIpSaValidateTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 2, 1),
    _JuniIpSaValidateTrapEnable_Type()
)
juniIpSaValidateTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIpSaValidateTrapEnable.setStatus("current")
_JuniIpTraps_ObjectIdentity = ObjectIdentity
juniIpTraps = _JuniIpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 3)
)
_JuniIpTrapPrefix_ObjectIdentity = ObjectIdentity
juniIpTrapPrefix = _JuniIpTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 3, 0)
)
_JuniIpMIBNotificationObjects_ObjectIdentity = ObjectIdentity
juniIpMIBNotificationObjects = _JuniIpMIBNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 3, 1)
)
_JuniIpIfSaValFailSrcIpAddr_Type = IpAddress
_JuniIpIfSaValFailSrcIpAddr_Object = MibScalar
juniIpIfSaValFailSrcIpAddr = _JuniIpIfSaValFailSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 3, 1, 1),
    _JuniIpIfSaValFailSrcIpAddr_Type()
)
juniIpIfSaValFailSrcIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniIpIfSaValFailSrcIpAddr.setStatus("current")
_JuniIpIfSaValFailDestIpAddr_Type = IpAddress
_JuniIpIfSaValFailDestIpAddr_Object = MibScalar
juniIpIfSaValFailDestIpAddr = _JuniIpIfSaValFailDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 3, 1, 2),
    _JuniIpIfSaValFailDestIpAddr_Type()
)
juniIpIfSaValFailDestIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniIpIfSaValFailDestIpAddr.setStatus("current")
_JuniIpConformance_ObjectIdentity = ObjectIdentity
juniIpConformance = _JuniIpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4)
)
_JuniIpCompliances_ObjectIdentity = ObjectIdentity
juniIpCompliances = _JuniIpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 1)
)
_JuniIpGroups_ObjectIdentity = ObjectIdentity
juniIpGroups = _JuniIpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 2)
)
ipCidrRouteEntry.registerAugmentions(
    ("Juniper-IP-MIB",
     "juniIpCidrRouteEntry")
)
juniIpCidrRouteEntry.setIndexNames(*ipCidrRouteEntry.getIndexNames())
juniIpRouteStaticEntry.registerAugmentions(
    ("Juniper-IP-MIB",
     "juniIpRouteStaticBFDEntry")
)
juniIpRouteStaticBFDEntry.setIndexNames(*juniIpRouteStaticEntry.getIndexNames())

# Managed Objects groups

juniIpInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 2, 1)
)
juniIpInterfaceGroup.setObjects(
      *(("Juniper-IP-MIB", "juniIpNextIfIndex"),
        ("Juniper-IP-MIB", "juniIpIfRowStatus"),
        ("Juniper-IP-MIB", "juniIpIfLowerIfIndex"),
        ("Juniper-IP-MIB", "juniIpIfType"),
        ("Juniper-IP-MIB", "juniIpIfTypeId"),
        ("Juniper-IP-MIB", "juniIpIfStatsInPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInOctets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInPoliciedPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInPoliciedOctets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInErrorPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInSpoofedPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInForwardedPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInForwardedOctets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutForwardedPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutForwardedOctets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutSchedDropPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutSchedDropOctets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutRequestedPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutRequestedOctets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutPoliciedPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutPoliciedOctets"))
)
if mibBuilder.loadTexts:
    juniIpInterfaceGroup.setStatus("obsolete")

juniIpAddressGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 2, 2)
)
juniIpAddressGroup.setObjects(
      *(("Juniper-IP-MIB", "juniIpArpTimeout"),
        ("Juniper-IP-MIB", "juniIpAdEntRowStatus"),
        ("Juniper-IP-MIB", "juniIpAdEntIfIndex"),
        ("Juniper-IP-MIB", "juniIpAdEntNetMask"),
        ("Juniper-IP-MIB", "juniIpAdEntAdminStatus"),
        ("Juniper-IP-MIB", "juniIpAdEntArpRspEnable"),
        ("Juniper-IP-MIB", "juniIpAdEntProxyArpRspEnable"),
        ("Juniper-IP-MIB", "juniIpAdEntIgmpEnable"),
        ("Juniper-IP-MIB", "juniIpAdEntDirectedBcastEnable"),
        ("Juniper-IP-MIB", "juniIpAdEntIcmpRedirectEnable"),
        ("Juniper-IP-MIB", "juniIpAdEntIcmpMaskReplyEnable"),
        ("Juniper-IP-MIB", "juniIpAdEntIcmpUnreachEnable"),
        ("Juniper-IP-MIB", "juniIpAdEntMtu"),
        ("Juniper-IP-MIB", "juniIpAdEntUnnumLoopbackIfIndex"),
        ("Juniper-IP-MIB", "juniIpAdEntIrdpEnable"),
        ("Juniper-IP-MIB", "juniIpAdEntAccessRouteEnable"),
        ("Juniper-IP-MIB", "juniIpAdEntAccessRouteHost"))
)
if mibBuilder.loadTexts:
    juniIpAddressGroup.setStatus("obsolete")

juniIpRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 2, 3)
)
juniIpRouteGroup.setObjects(
      *(("Juniper-IP-MIB", "juniIpRouteLimit"),
        ("Juniper-IP-MIB", "juniIpRouteStaticDest"),
        ("Juniper-IP-MIB", "juniIpRouteStaticMask"),
        ("Juniper-IP-MIB", "juniIpRouteStaticPref"),
        ("Juniper-IP-MIB", "juniIpRouteStaticNextHop"),
        ("Juniper-IP-MIB", "juniIpRouteStaticRowStatus"),
        ("Juniper-IP-MIB", "juniIpRouteStaticIfIndex"),
        ("Juniper-IP-MIB", "juniIpRouteStaticStatus"),
        ("Juniper-IP-MIB", "juniIpRouteStaticNextHopAS"),
        ("Juniper-IP-MIB", "juniIpRouteStaticMetric"),
        ("Juniper-IP-MIB", "juniIpRouteStaticTag"),
        ("Juniper-IP-MIB", "juniIpCidrRoutePref"),
        ("Juniper-IP-MIB", "juniIpCidrRouteArea"),
        ("Juniper-IP-MIB", "juniIpCidrRouteTag"))
)
if mibBuilder.loadTexts:
    juniIpRouteGroup.setStatus("obsolete")

juniIpGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 2, 4)
)
juniIpGlobalGroup.setObjects(
      *(("Juniper-IP-MIB", "juniIpDebounceTime"),
        ("Juniper-IP-MIB", "juniIpRouterId"),
        ("Juniper-IP-MIB", "juniIpSourceRoutingAdminStatus"),
        ("Juniper-IP-MIB", "juniIpVpnIdOui"),
        ("Juniper-IP-MIB", "juniIpVpnIdIndex"))
)
if mibBuilder.loadTexts:
    juniIpGlobalGroup.setStatus("obsolete")

juniIpInterfaceGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 2, 5)
)
juniIpInterfaceGroup2.setObjects(
      *(("Juniper-IP-MIB", "juniIpNextIfIndex"),
        ("Juniper-IP-MIB", "juniIpIfRowStatus"),
        ("Juniper-IP-MIB", "juniIpIfLowerIfIndex"),
        ("Juniper-IP-MIB", "juniIpIfType"),
        ("Juniper-IP-MIB", "juniIpIfTypeId"),
        ("Juniper-IP-MIB", "juniIpIfSAValidationEnable"),
        ("Juniper-IP-MIB", "juniIpIfCreationType"),
        ("Juniper-IP-MIB", "juniIpIfProfileId"),
        ("Juniper-IP-MIB", "juniIpIfAlwaysUp"),
        ("Juniper-IP-MIB", "juniIpIfLoopback"),
        ("Juniper-IP-MIB", "juniIpIfLoopbackUid"),
        ("Juniper-IP-MIB", "juniIpIfDebounceTime"),
        ("Juniper-IP-MIB", "juniIpIfForwarding"),
        ("Juniper-IP-MIB", "juniIpIfForceFragmentation"),
        ("Juniper-IP-MIB", "juniIpIfSharesLowerUid"),
        ("Juniper-IP-MIB", "juniIpIfFilterOptions"),
        ("Juniper-IP-MIB", "juniIpIfName"),
        ("Juniper-IP-MIB", "juniIpIfArpTimeout"),
        ("Juniper-IP-MIB", "juniIpIfAdminSpeed"),
        ("Juniper-IP-MIB", "juniIpIfMultipathMode"),
        ("Juniper-IP-MIB", "juniIpIfSharedNhAddr"),
        ("Juniper-IP-MIB", "juniIpIfSharedNhRouterId"),
        ("Juniper-IP-MIB", "juniIpIfPrimaryIpAddress"),
        ("Juniper-IP-MIB", "juniIpIfPrimaryIpMask"),
        ("Juniper-IP-MIB", "juniIpIfOperDebounceTime"),
        ("Juniper-IP-MIB", "juniIpIfStatsInPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInOctets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInPoliciedPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInPoliciedOctets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInErrorPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInSpoofedPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInForwardedPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInForwardedOctets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutForwardedPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutForwardedOctets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutSchedDropPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutSchedDropOctets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutRequestedPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutRequestedOctets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutPoliciedPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutPoliciedOctets"),
        ("Juniper-IP-MIB", "juniIpIfStatsGreenOutSchedDropPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsYellowOutSchedDropPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsRedOutSchedDropPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsGreenOutSchedDropOctets"),
        ("Juniper-IP-MIB", "juniIpIfStatsYellowOutSchedDropOctets"),
        ("Juniper-IP-MIB", "juniIpIfStatsRedOutSchedDropOctets"))
)
if mibBuilder.loadTexts:
    juniIpInterfaceGroup2.setStatus("obsolete")

juniIpAddressGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 2, 6)
)
juniIpAddressGroup2.setObjects(
      *(("Juniper-IP-MIB", "juniIpArpTimeout"),
        ("Juniper-IP-MIB", "juniIpAdEntRowStatus"),
        ("Juniper-IP-MIB", "juniIpAdEntIfIndex"),
        ("Juniper-IP-MIB", "juniIpAdEntNetMask"),
        ("Juniper-IP-MIB", "juniIpAdEntBcastAddr"),
        ("Juniper-IP-MIB", "juniIpAdEntReasmMaxSize"),
        ("Juniper-IP-MIB", "juniIpAdEntAdminStatus"),
        ("Juniper-IP-MIB", "juniIpAdEntArpRspEnable"),
        ("Juniper-IP-MIB", "juniIpAdEntProxyArpRspEnable"),
        ("Juniper-IP-MIB", "juniIpAdEntDirectedBcastEnable"),
        ("Juniper-IP-MIB", "juniIpAdEntIcmpRedirectEnable"),
        ("Juniper-IP-MIB", "juniIpAdEntIcmpMaskReplyEnable"),
        ("Juniper-IP-MIB", "juniIpAdEntIcmpUnreachEnable"),
        ("Juniper-IP-MIB", "juniIpAdEntMtu"),
        ("Juniper-IP-MIB", "juniIpAdEntUnnumLoopbackIfIndex"),
        ("Juniper-IP-MIB", "juniIpAdEntIrdpEnable"),
        ("Juniper-IP-MIB", "juniIpAdEntAccessRouteEnable"),
        ("Juniper-IP-MIB", "juniIpAdEntAccessRouteHost"),
        ("Juniper-IP-MIB", "juniIpAdEntIsSecondary"))
)
if mibBuilder.loadTexts:
    juniIpAddressGroup2.setStatus("obsolete")

juniIpInterfaceGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 2, 7)
)
juniIpInterfaceGroup3.setObjects(
      *(("Juniper-IP-MIB", "juniIpNextIfIndex"),
        ("Juniper-IP-MIB", "juniIpIfRowStatus"),
        ("Juniper-IP-MIB", "juniIpIfLowerIfIndex"),
        ("Juniper-IP-MIB", "juniIpIfType"),
        ("Juniper-IP-MIB", "juniIpIfTypeId"),
        ("Juniper-IP-MIB", "juniIpIfSAValidationEnable"),
        ("Juniper-IP-MIB", "juniIpIfCreationType"),
        ("Juniper-IP-MIB", "juniIpIfProfileId"),
        ("Juniper-IP-MIB", "juniIpIfAlwaysUp"),
        ("Juniper-IP-MIB", "juniIpIfLoopback"),
        ("Juniper-IP-MIB", "juniIpIfLoopbackUid"),
        ("Juniper-IP-MIB", "juniIpIfDebounceTime"),
        ("Juniper-IP-MIB", "juniIpIfForwarding"),
        ("Juniper-IP-MIB", "juniIpIfForceFragmentation"),
        ("Juniper-IP-MIB", "juniIpIfSharesLowerUid"),
        ("Juniper-IP-MIB", "juniIpIfFilterOptions"),
        ("Juniper-IP-MIB", "juniIpIfName"),
        ("Juniper-IP-MIB", "juniIpIfArpTimeout"),
        ("Juniper-IP-MIB", "juniIpIfAdminSpeed"),
        ("Juniper-IP-MIB", "juniIpIfMultipathMode"),
        ("Juniper-IP-MIB", "juniIpIfSharedNhAddr"),
        ("Juniper-IP-MIB", "juniIpIfSharedNhRouterId"),
        ("Juniper-IP-MIB", "juniIpIfPrimaryIpAddress"),
        ("Juniper-IP-MIB", "juniIpIfPrimaryIpMask"),
        ("Juniper-IP-MIB", "juniIpIfOperDebounceTime"),
        ("Juniper-IP-MIB", "juniIpIfStatsInPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInOctets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInPoliciedPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInPoliciedOctets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInErrorPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInSpoofedPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInForwardedPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInForwardedOctets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutForwardedPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutForwardedOctets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutSchedDropPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutSchedDropOctets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutRequestedPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutRequestedOctets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutPoliciedPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutPoliciedOctets"),
        ("Juniper-IP-MIB", "juniIpIfStatsGreenOutSchedDropPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsYellowOutSchedDropPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsRedOutSchedDropPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsGreenOutSchedDropOctets"),
        ("Juniper-IP-MIB", "juniIpIfStatsYellowOutSchedDropOctets"),
        ("Juniper-IP-MIB", "juniIpIfStatsRedOutSchedDropOctets"),
        ("Juniper-IP-MIB", "juniIpIfAssocIpIfIndex"))
)
if mibBuilder.loadTexts:
    juniIpInterfaceGroup3.setStatus("obsolete")

juniIpInterfaceGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 2, 8)
)
juniIpInterfaceGroup4.setObjects(
      *(("Juniper-IP-MIB", "juniIpNextIfIndex"),
        ("Juniper-IP-MIB", "juniIpIfRowStatus"),
        ("Juniper-IP-MIB", "juniIpIfLowerIfIndex"),
        ("Juniper-IP-MIB", "juniIpIfType"),
        ("Juniper-IP-MIB", "juniIpIfTypeId"),
        ("Juniper-IP-MIB", "juniIpIfSAValidationEnable"),
        ("Juniper-IP-MIB", "juniIpIfCreationType"),
        ("Juniper-IP-MIB", "juniIpIfProfileId"),
        ("Juniper-IP-MIB", "juniIpIfAlwaysUp"),
        ("Juniper-IP-MIB", "juniIpIfLoopback"),
        ("Juniper-IP-MIB", "juniIpIfLoopbackUid"),
        ("Juniper-IP-MIB", "juniIpIfDebounceTime"),
        ("Juniper-IP-MIB", "juniIpIfForwarding"),
        ("Juniper-IP-MIB", "juniIpIfForceFragmentation"),
        ("Juniper-IP-MIB", "juniIpIfSharesLowerUid"),
        ("Juniper-IP-MIB", "juniIpIfFilterOptions"),
        ("Juniper-IP-MIB", "juniIpIfName"),
        ("Juniper-IP-MIB", "juniIpIfArpTimeout"),
        ("Juniper-IP-MIB", "juniIpIfAdminSpeed"),
        ("Juniper-IP-MIB", "juniIpIfMultipathMode"),
        ("Juniper-IP-MIB", "juniIpIfSharedNhAddr"),
        ("Juniper-IP-MIB", "juniIpIfSharedNhRouterId"),
        ("Juniper-IP-MIB", "juniIpIfPrimaryIpAddress"),
        ("Juniper-IP-MIB", "juniIpIfPrimaryIpMask"),
        ("Juniper-IP-MIB", "juniIpIfOperDebounceTime"),
        ("Juniper-IP-MIB", "juniIpIfStatsInPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInOctets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInPoliciedPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInPoliciedOctets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInErrorPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInSpoofedPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutForwardedPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutForwardedOctets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutSchedDropPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutSchedDropOctets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutPoliciedPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutPoliciedOctets"),
        ("Juniper-IP-MIB", "juniIpIfAssocIpIfIndex"))
)
if mibBuilder.loadTexts:
    juniIpInterfaceGroup4.setStatus("obsolete")

juniIpAddressGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 2, 9)
)
juniIpAddressGroup3.setObjects(
      *(("Juniper-IP-MIB", "juniIpAdEntRowStatus"),
        ("Juniper-IP-MIB", "juniIpAdEntIfIndex"),
        ("Juniper-IP-MIB", "juniIpAdEntNetMask"),
        ("Juniper-IP-MIB", "juniIpAdEntBcastAddr"),
        ("Juniper-IP-MIB", "juniIpAdEntReasmMaxSize"),
        ("Juniper-IP-MIB", "juniIpAdEntAdminStatus"),
        ("Juniper-IP-MIB", "juniIpAdEntArpRspEnable"),
        ("Juniper-IP-MIB", "juniIpAdEntProxyArpRspEnable"),
        ("Juniper-IP-MIB", "juniIpAdEntDirectedBcastEnable"),
        ("Juniper-IP-MIB", "juniIpAdEntIcmpRedirectEnable"),
        ("Juniper-IP-MIB", "juniIpAdEntIcmpMaskReplyEnable"),
        ("Juniper-IP-MIB", "juniIpAdEntIcmpUnreachEnable"),
        ("Juniper-IP-MIB", "juniIpAdEntMtu"),
        ("Juniper-IP-MIB", "juniIpAdEntUnnumLoopbackIfIndex"),
        ("Juniper-IP-MIB", "juniIpAdEntIrdpEnable"),
        ("Juniper-IP-MIB", "juniIpAdEntAccessRouteEnable"),
        ("Juniper-IP-MIB", "juniIpAdEntAccessRouteHost"),
        ("Juniper-IP-MIB", "juniIpAdEntIsSecondary"))
)
if mibBuilder.loadTexts:
    juniIpAddressGroup3.setStatus("obsolete")

juniIpRouteGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 2, 10)
)
juniIpRouteGroup2.setObjects(
      *(("Juniper-IP-MIB", "juniIpRouteStaticDest"),
        ("Juniper-IP-MIB", "juniIpRouteStaticMask"),
        ("Juniper-IP-MIB", "juniIpRouteStaticPref"),
        ("Juniper-IP-MIB", "juniIpRouteStaticNextHop"),
        ("Juniper-IP-MIB", "juniIpRouteStaticRowStatus"),
        ("Juniper-IP-MIB", "juniIpRouteStaticIfIndex"),
        ("Juniper-IP-MIB", "juniIpRouteStaticStatus"),
        ("Juniper-IP-MIB", "juniIpRouteStaticNextHopAS"),
        ("Juniper-IP-MIB", "juniIpRouteStaticMetric"),
        ("Juniper-IP-MIB", "juniIpRouteStaticTag"),
        ("Juniper-IP-MIB", "juniIpCidrRoutePref"),
        ("Juniper-IP-MIB", "juniIpCidrRouteArea"),
        ("Juniper-IP-MIB", "juniIpCidrRouteTag"))
)
if mibBuilder.loadTexts:
    juniIpRouteGroup2.setStatus("obsolete")

juniIpGlobalGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 2, 11)
)
juniIpGlobalGroup2.setObjects(
      *(("Juniper-IP-MIB", "juniIpDebounceTime"),
        ("Juniper-IP-MIB", "juniIpRouterId"),
        ("Juniper-IP-MIB", "juniIpSourceRoutingAdminStatus"),
        ("Juniper-IP-MIB", "juniIpVpnIdOui"),
        ("Juniper-IP-MIB", "juniIpVpnIdIndex"),
        ("Juniper-IP-MIB", "juniIpBgpCommunityNewFormat"),
        ("Juniper-IP-MIB", "juniIpBgpAsConfedSetNewFormat"))
)
if mibBuilder.loadTexts:
    juniIpGlobalGroup2.setStatus("obsolete")

juniIpInterfaceGroup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 2, 12)
)
juniIpInterfaceGroup5.setObjects(
      *(("Juniper-IP-MIB", "juniIpNextIfIndex"),
        ("Juniper-IP-MIB", "juniIpIfRowStatus"),
        ("Juniper-IP-MIB", "juniIpIfLowerIfIndex"),
        ("Juniper-IP-MIB", "juniIpIfType"),
        ("Juniper-IP-MIB", "juniIpIfTypeId"),
        ("Juniper-IP-MIB", "juniIpIfSAValidationEnable"),
        ("Juniper-IP-MIB", "juniIpIfCreationType"),
        ("Juniper-IP-MIB", "juniIpIfProfileId"),
        ("Juniper-IP-MIB", "juniIpIfAlwaysUp"),
        ("Juniper-IP-MIB", "juniIpIfDebounceTime"),
        ("Juniper-IP-MIB", "juniIpIfForwarding"),
        ("Juniper-IP-MIB", "juniIpIfForceFragmentation"),
        ("Juniper-IP-MIB", "juniIpIfSharesLowerUid"),
        ("Juniper-IP-MIB", "juniIpIfFilterOptions"),
        ("Juniper-IP-MIB", "juniIpIfName"),
        ("Juniper-IP-MIB", "juniIpIfArpTimeout"),
        ("Juniper-IP-MIB", "juniIpIfAdminSpeed"),
        ("Juniper-IP-MIB", "juniIpIfMultipathMode"),
        ("Juniper-IP-MIB", "juniIpIfSharedNhAddr"),
        ("Juniper-IP-MIB", "juniIpIfSharedNhRouterId"),
        ("Juniper-IP-MIB", "juniIpIfPrimaryIpAddress"),
        ("Juniper-IP-MIB", "juniIpIfPrimaryIpMask"),
        ("Juniper-IP-MIB", "juniIpIfOperDebounceTime"),
        ("Juniper-IP-MIB", "juniIpIfRouterIndex"),
        ("Juniper-IP-MIB", "juniIpIfInheritNum"),
        ("Juniper-IP-MIB", "juniIpIfInheritNumUid"),
        ("Juniper-IP-MIB", "juniIpIfStatsInPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInOctets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInPoliciedPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInPoliciedOctets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInErrorPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInSpoofedPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutForwardedPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutForwardedOctets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutSchedDropPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutSchedDropOctets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutPoliciedPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutPoliciedOctets"),
        ("Juniper-IP-MIB", "juniIpIfAssocIpIfIndex"))
)
if mibBuilder.loadTexts:
    juniIpInterfaceGroup5.setStatus("obsolete")

juniIpAddressGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 2, 13)
)
juniIpAddressGroup4.setObjects(
      *(("Juniper-IP-MIB", "juniIpAdEntRowStatus"),
        ("Juniper-IP-MIB", "juniIpAdEntIfIndex"),
        ("Juniper-IP-MIB", "juniIpAdEntNetMask"),
        ("Juniper-IP-MIB", "juniIpAdEntBcastAddr"),
        ("Juniper-IP-MIB", "juniIpAdEntReasmMaxSize"),
        ("Juniper-IP-MIB", "juniIpAdEntAdminStatus"),
        ("Juniper-IP-MIB", "juniIpAdEntArpRspEnable"),
        ("Juniper-IP-MIB", "juniIpAdEntProxyArpRspEnable"),
        ("Juniper-IP-MIB", "juniIpAdEntDirectedBcastEnable"),
        ("Juniper-IP-MIB", "juniIpAdEntIcmpRedirectEnable"),
        ("Juniper-IP-MIB", "juniIpAdEntIcmpMaskReplyEnable"),
        ("Juniper-IP-MIB", "juniIpAdEntIcmpUnreachEnable"),
        ("Juniper-IP-MIB", "juniIpAdEntMtu"),
        ("Juniper-IP-MIB", "juniIpAdEntIrdpEnable"),
        ("Juniper-IP-MIB", "juniIpAdEntAccessRouteEnable"),
        ("Juniper-IP-MIB", "juniIpAdEntAccessRouteHost"),
        ("Juniper-IP-MIB", "juniIpAdEntIsSecondary"),
        ("Juniper-IP-MIB", "juniIpAdEntUnnumInheritNumIfIndex"))
)
if mibBuilder.loadTexts:
    juniIpAddressGroup4.setStatus("current")

juniIpInterfaceDeprecatedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 2, 14)
)
juniIpInterfaceDeprecatedGroup.setObjects(
      *(("Juniper-IP-MIB", "juniIpIfLoopback"),
        ("Juniper-IP-MIB", "juniIpIfLoopbackUid"))
)
if mibBuilder.loadTexts:
    juniIpInterfaceDeprecatedGroup.setStatus("deprecated")

juniIpAddressDeprecatedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 2, 15)
)
juniIpAddressDeprecatedGroup.setObjects(
      *(("Juniper-IP-MIB", "juniIpAdEntIgmpEnable"),
        ("Juniper-IP-MIB", "juniIpAdEntUnnumLoopbackIfIndex"))
)
if mibBuilder.loadTexts:
    juniIpAddressDeprecatedGroup.setStatus("deprecated")

juniIpInterfaceGroup6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 2, 16)
)
juniIpInterfaceGroup6.setObjects(
      *(("Juniper-IP-MIB", "juniIpNextIfIndex"),
        ("Juniper-IP-MIB", "juniIpIfRowStatus"),
        ("Juniper-IP-MIB", "juniIpIfLowerIfIndex"),
        ("Juniper-IP-MIB", "juniIpIfType"),
        ("Juniper-IP-MIB", "juniIpIfTypeId"),
        ("Juniper-IP-MIB", "juniIpIfSAValidationEnable"),
        ("Juniper-IP-MIB", "juniIpIfCreationType"),
        ("Juniper-IP-MIB", "juniIpIfProfileId"),
        ("Juniper-IP-MIB", "juniIpIfAlwaysUp"),
        ("Juniper-IP-MIB", "juniIpIfDebounceTime"),
        ("Juniper-IP-MIB", "juniIpIfForwarding"),
        ("Juniper-IP-MIB", "juniIpIfForceFragmentation"),
        ("Juniper-IP-MIB", "juniIpIfSharesLowerUid"),
        ("Juniper-IP-MIB", "juniIpIfFilterOptions"),
        ("Juniper-IP-MIB", "juniIpIfName"),
        ("Juniper-IP-MIB", "juniIpIfArpTimeout"),
        ("Juniper-IP-MIB", "juniIpIfAdminSpeed"),
        ("Juniper-IP-MIB", "juniIpIfMultipathMode"),
        ("Juniper-IP-MIB", "juniIpIfSharedNhAddr"),
        ("Juniper-IP-MIB", "juniIpIfSharedNhRouterId"),
        ("Juniper-IP-MIB", "juniIpIfPrimaryIpAddress"),
        ("Juniper-IP-MIB", "juniIpIfPrimaryIpMask"),
        ("Juniper-IP-MIB", "juniIpIfOperDebounceTime"),
        ("Juniper-IP-MIB", "juniIpIfRouterIndex"),
        ("Juniper-IP-MIB", "juniIpIfInheritNum"),
        ("Juniper-IP-MIB", "juniIpIfInheritNumUid"),
        ("Juniper-IP-MIB", "juniIpIfAnalyzerMode"),
        ("Juniper-IP-MIB", "juniIpIfAutoConfigure"),
        ("Juniper-IP-MIB", "juniIpIfStatsInPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInOctets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInPoliciedPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInPoliciedOctets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInErrorPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInSpoofedPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutForwardedPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutForwardedOctets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutSchedDropPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutSchedDropOctets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutPoliciedPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutPoliciedOctets"),
        ("Juniper-IP-MIB", "juniIpIfAssocIpIfIndex"))
)
if mibBuilder.loadTexts:
    juniIpInterfaceGroup6.setStatus("obsolete")

juniIpIfSummaryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 2, 17)
)
juniIpIfSummaryGroup.setObjects(
      *(("Juniper-IP-MIB", "juniIpIfSummaryTotalIntf"),
        ("Juniper-IP-MIB", "juniIpIfSummaryTotalIntfUp"),
        ("Juniper-IP-MIB", "juniIpIfSummaryTotalIntfDown"),
        ("Juniper-IP-MIB", "juniIpIfSummaryTotalIntfProtUp"),
        ("Juniper-IP-MIB", "juniIpIfSummaryTotalIntfProtDown"),
        ("Juniper-IP-MIB", "juniIpIfSummaryTotalIntfProtNotPresent"))
)
if mibBuilder.loadTexts:
    juniIpIfSummaryGroup.setStatus("current")

juniIpInterfaceGroup7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 2, 18)
)
juniIpInterfaceGroup7.setObjects(
      *(("Juniper-IP-MIB", "juniIpNextIfIndex"),
        ("Juniper-IP-MIB", "juniIpIfRowStatus"),
        ("Juniper-IP-MIB", "juniIpIfLowerIfIndex"),
        ("Juniper-IP-MIB", "juniIpIfType"),
        ("Juniper-IP-MIB", "juniIpIfTypeId"),
        ("Juniper-IP-MIB", "juniIpIfSAValidationEnable"),
        ("Juniper-IP-MIB", "juniIpIfCreationType"),
        ("Juniper-IP-MIB", "juniIpIfProfileId"),
        ("Juniper-IP-MIB", "juniIpIfAlwaysUp"),
        ("Juniper-IP-MIB", "juniIpIfDebounceTime"),
        ("Juniper-IP-MIB", "juniIpIfForwarding"),
        ("Juniper-IP-MIB", "juniIpIfForceFragmentation"),
        ("Juniper-IP-MIB", "juniIpIfSharesLowerUid"),
        ("Juniper-IP-MIB", "juniIpIfFilterOptions"),
        ("Juniper-IP-MIB", "juniIpIfName"),
        ("Juniper-IP-MIB", "juniIpIfArpTimeout"),
        ("Juniper-IP-MIB", "juniIpIfAdminSpeed"),
        ("Juniper-IP-MIB", "juniIpIfMultipathMode"),
        ("Juniper-IP-MIB", "juniIpIfSharedNhAddr"),
        ("Juniper-IP-MIB", "juniIpIfSharedNhRouterId"),
        ("Juniper-IP-MIB", "juniIpIfPrimaryIpAddress"),
        ("Juniper-IP-MIB", "juniIpIfPrimaryIpMask"),
        ("Juniper-IP-MIB", "juniIpIfOperDebounceTime"),
        ("Juniper-IP-MIB", "juniIpIfRouterIndex"),
        ("Juniper-IP-MIB", "juniIpIfInheritNum"),
        ("Juniper-IP-MIB", "juniIpIfInheritNumUid"),
        ("Juniper-IP-MIB", "juniIpIfAnalyzerMode"),
        ("Juniper-IP-MIB", "juniIpIfAutoConfigure"),
        ("Juniper-IP-MIB", "juniIpIfTcpMss"),
        ("Juniper-IP-MIB", "juniIpIfStatsInPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInOctets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInPoliciedPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInPoliciedOctets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInErrorPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInSpoofedPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutForwardedPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutForwardedOctets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutSchedDropPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutSchedDropOctets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutPoliciedPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutPoliciedOctets"),
        ("Juniper-IP-MIB", "juniIpIfAssocIpIfIndex"))
)
if mibBuilder.loadTexts:
    juniIpInterfaceGroup7.setStatus("obsolete")

juniIpGlobalGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 2, 19)
)
juniIpGlobalGroup3.setObjects(
      *(("Juniper-IP-MIB", "juniIpDebounceTime"),
        ("Juniper-IP-MIB", "juniIpRouterId"),
        ("Juniper-IP-MIB", "juniIpSourceRoutingAdminStatus"),
        ("Juniper-IP-MIB", "juniIpBgpCommunityNewFormat"),
        ("Juniper-IP-MIB", "juniIpBgpAsConfedSetNewFormat"))
)
if mibBuilder.loadTexts:
    juniIpGlobalGroup3.setStatus("current")

juniIpRouteGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 2, 20)
)
juniIpRouteGroup3.setObjects(
      *(("Juniper-IP-MIB", "juniIpRouteTableLimit"),
        ("Juniper-IP-MIB", "juniIpRouteTableWarnPercent"),
        ("Juniper-IP-MIB", "juniIpRouteTableWarnOnly"),
        ("Juniper-IP-MIB", "juniIpRouteTableWarnThreshold"),
        ("Juniper-IP-MIB", "juniIpRouteStaticDest"),
        ("Juniper-IP-MIB", "juniIpRouteStaticMask"),
        ("Juniper-IP-MIB", "juniIpRouteStaticPref"),
        ("Juniper-IP-MIB", "juniIpRouteStaticNextHop"),
        ("Juniper-IP-MIB", "juniIpRouteStaticRowStatus"),
        ("Juniper-IP-MIB", "juniIpRouteStaticIfIndex"),
        ("Juniper-IP-MIB", "juniIpRouteStaticStatus"),
        ("Juniper-IP-MIB", "juniIpRouteStaticNextHopAS"),
        ("Juniper-IP-MIB", "juniIpRouteStaticMetric"),
        ("Juniper-IP-MIB", "juniIpRouteStaticTag"),
        ("Juniper-IP-MIB", "juniIpCidrRoutePref"),
        ("Juniper-IP-MIB", "juniIpCidrRouteArea"),
        ("Juniper-IP-MIB", "juniIpCidrRouteTag"))
)
if mibBuilder.loadTexts:
    juniIpRouteGroup3.setStatus("current")

juniIpMIBNotificationObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 2, 23)
)
juniIpMIBNotificationObjectsGroup.setObjects(
      *(("Juniper-IP-MIB", "juniIpIfSaValFailSrcIpAddr"),
        ("Juniper-IP-MIB", "juniIpIfSaValFailDestIpAddr"))
)
if mibBuilder.loadTexts:
    juniIpMIBNotificationObjectsGroup.setStatus("current")

juniIpRouteSummaryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 2, 24)
)
juniIpRouteSummaryGroup.setObjects(
      *(("Juniper-IP-MIB", "juniIpRouteSummaryUnicastTotalRoutes"),
        ("Juniper-IP-MIB", "juniIpRouteSummaryUnicastTotalBytes"),
        ("Juniper-IP-MIB", "juniIpRouteSummaryUnicastIsisRoutes"),
        ("Juniper-IP-MIB", "juniIpRouteSummaryUnicastIsisLevel1Routes"),
        ("Juniper-IP-MIB", "juniIpRouteSummaryUnicastIsisLevel2Routes"),
        ("Juniper-IP-MIB", "juniIpRouteSummaryUnicastRipRoutes"),
        ("Juniper-IP-MIB", "juniIpRouteSummaryUnicastStaticRoutes"),
        ("Juniper-IP-MIB", "juniIpRouteSummaryUnicastConnectedRoutes"),
        ("Juniper-IP-MIB", "juniIpRouteSummaryUnicastBgpRoutes"),
        ("Juniper-IP-MIB", "juniIpRouteSummaryUnicastOspfRoutes"),
        ("Juniper-IP-MIB", "juniIpRouteSummaryUnicastIntraAreaOspfRoutes"),
        ("Juniper-IP-MIB", "juniIpRouteSummaryUnicastOtherInternalRoutes"),
        ("Juniper-IP-MIB", "juniIpRouteSummaryUnicastExternalOspfRoutes"),
        ("Juniper-IP-MIB", "juniIpRouteSummaryUnicastInterAreaOspfRoutes"),
        ("Juniper-IP-MIB", "juniIpRouteSummaryUnicastAccessRoutes"),
        ("Juniper-IP-MIB", "juniIpRouteSummaryUnicastIntCreatedAccessHostRoutes"),
        ("Juniper-IP-MIB", "juniIpRouteSummaryUnicastIntDialoutRoutes"),
        ("Juniper-IP-MIB", "juniIpRouteSummaryUnicastRouteMemoryActive"),
        ("Juniper-IP-MIB", "juniIpRouteSummaryUnicastLastRouteAddedOrDeletedIP"),
        ("Juniper-IP-MIB", "juniIpRouteSummaryUnicastLastRouteAddedOrDeletedMask"),
        ("Juniper-IP-MIB", "juniIpRouteSummaryUnicastLastRouteAddedOrDeletedClient"),
        ("Juniper-IP-MIB", "juniIpRouteSummaryUnicastLastRouteAddedOrDeletedDate"),
        ("Juniper-IP-MIB", "juniIpRouteSummaryMulticastTotalRoutes"),
        ("Juniper-IP-MIB", "juniIpRouteSummaryMulticastTotalBytes"),
        ("Juniper-IP-MIB", "juniIpRouteSummaryMulticastIsisRoutes"),
        ("Juniper-IP-MIB", "juniIpRouteSummaryMulticastLevel1IsisRoutes"),
        ("Juniper-IP-MIB", "juniIpRouteSummaryMulticastLevel2IsisRoutes"),
        ("Juniper-IP-MIB", "juniIpRouteSummaryMulticastRipRoutes"),
        ("Juniper-IP-MIB", "juniIpRouteSummaryMulticastStaticRoutes"),
        ("Juniper-IP-MIB", "juniIpRouteSummaryMulticastConnectedRoutes"),
        ("Juniper-IP-MIB", "juniIpRouteSummaryMulticastBgpRoutes"),
        ("Juniper-IP-MIB", "juniIpRouteSummaryMulticastOspfRoutes"),
        ("Juniper-IP-MIB", "juniIpRouteSummaryMulticastIntraAreaOspfRoutes"),
        ("Juniper-IP-MIB", "juniIpRouteSummaryMulticastInterAreaOspfRoutes"),
        ("Juniper-IP-MIB", "juniIpRouteSummaryMulticastExternalOspfRoutes"),
        ("Juniper-IP-MIB", "juniIpRouteSummaryMulticastOtherInternalRoutes"),
        ("Juniper-IP-MIB", "juniIpRouteSummaryMulticastAccessRoutes"),
        ("Juniper-IP-MIB", "juniIpRouteSummaryMulticastIntCreatedAccessHostRoutes"),
        ("Juniper-IP-MIB", "juniIpRouteSummaryMultiastIntDialoutRoutes"),
        ("Juniper-IP-MIB", "juniIpRouteSummaryMulticastRouteMemoryActive"),
        ("Juniper-IP-MIB", "juniIpRouteSummaryMulticastLastRouteAddedOrDeletedIP"),
        ("Juniper-IP-MIB", "juniIpRouteSummaryMulticastLastRouteAddedOrDeletedMask"),
        ("Juniper-IP-MIB", "juniIpRouteSummaryMulticastLastRouteAddedOrDeletedClient"),
        ("Juniper-IP-MIB", "juniIpRouteSummaryMulticastLastRouteAddedOrDeletedDate"))
)
if mibBuilder.loadTexts:
    juniIpRouteSummaryGroup.setStatus("current")

juniIpRouteStaticBFDGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 2, 25)
)
juniIpRouteStaticBFDGroup.setObjects(
      *(("Juniper-IP-MIB", "juniIpRouteStaticBfdEnable"),
        ("Juniper-IP-MIB", "juniIpRouteStaticBfdMinRxInterval"),
        ("Juniper-IP-MIB", "juniIpRouteStaticBfdMinTxInterval"),
        ("Juniper-IP-MIB", "juniIpRouteStaticBfdMultiplier"))
)
if mibBuilder.loadTexts:
    juniIpRouteStaticBFDGroup.setStatus("current")

juniIpInterfaceGroup8 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 2, 26)
)
juniIpInterfaceGroup8.setObjects(
      *(("Juniper-IP-MIB", "juniIpNextIfIndex"),
        ("Juniper-IP-MIB", "juniIpIfRowStatus"),
        ("Juniper-IP-MIB", "juniIpIfLowerIfIndex"),
        ("Juniper-IP-MIB", "juniIpIfType"),
        ("Juniper-IP-MIB", "juniIpIfTypeId"),
        ("Juniper-IP-MIB", "juniIpIfSAValidationEnable"),
        ("Juniper-IP-MIB", "juniIpIfCreationType"),
        ("Juniper-IP-MIB", "juniIpIfProfileId"),
        ("Juniper-IP-MIB", "juniIpIfAlwaysUp"),
        ("Juniper-IP-MIB", "juniIpIfDebounceTime"),
        ("Juniper-IP-MIB", "juniIpIfForwarding"),
        ("Juniper-IP-MIB", "juniIpIfForceFragmentation"),
        ("Juniper-IP-MIB", "juniIpIfSharesLowerUid"),
        ("Juniper-IP-MIB", "juniIpIfFilterOptions"),
        ("Juniper-IP-MIB", "juniIpIfName"),
        ("Juniper-IP-MIB", "juniIpIfArpTimeout"),
        ("Juniper-IP-MIB", "juniIpIfAdminSpeed"),
        ("Juniper-IP-MIB", "juniIpIfMultipathMode"),
        ("Juniper-IP-MIB", "juniIpIfSharedNhAddr"),
        ("Juniper-IP-MIB", "juniIpIfSharedNhRouterId"),
        ("Juniper-IP-MIB", "juniIpIfPrimaryIpAddress"),
        ("Juniper-IP-MIB", "juniIpIfPrimaryIpMask"),
        ("Juniper-IP-MIB", "juniIpIfOperDebounceTime"),
        ("Juniper-IP-MIB", "juniIpIfRouterIndex"),
        ("Juniper-IP-MIB", "juniIpIfInheritNum"),
        ("Juniper-IP-MIB", "juniIpIfInheritNumUid"),
        ("Juniper-IP-MIB", "juniIpIfAnalyzerMode"),
        ("Juniper-IP-MIB", "juniIpIfAutoConfigure"),
        ("Juniper-IP-MIB", "juniIpIfTcpMss"),
        ("Juniper-IP-MIB", "juniIpIfInitSeqPrefOper"),
        ("Juniper-IP-MIB", "juniIpIfInitSeqPrefAdmin"),
        ("Juniper-IP-MIB", "juniIpIfStatsInPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInOctets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInPoliciedPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInPoliciedOctets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInErrorPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInSpoofedPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutForwardedPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutForwardedOctets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutSchedDropPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutSchedDropOctets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutPoliciedPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutPoliciedOctets"),
        ("Juniper-IP-MIB", "juniIpIfAssocIpIfIndex"))
)
if mibBuilder.loadTexts:
    juniIpInterfaceGroup8.setStatus("obsolete")

juniIpInterfaceGroup9 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 2, 27)
)
juniIpInterfaceGroup9.setObjects(
      *(("Juniper-IP-MIB", "juniIpNextIfIndex"),
        ("Juniper-IP-MIB", "juniIpIfRowStatus"),
        ("Juniper-IP-MIB", "juniIpIfLowerIfIndex"),
        ("Juniper-IP-MIB", "juniIpIfType"),
        ("Juniper-IP-MIB", "juniIpIfTypeId"),
        ("Juniper-IP-MIB", "juniIpIfSAValidationEnable"),
        ("Juniper-IP-MIB", "juniIpIfCreationType"),
        ("Juniper-IP-MIB", "juniIpIfProfileId"),
        ("Juniper-IP-MIB", "juniIpIfAlwaysUp"),
        ("Juniper-IP-MIB", "juniIpIfDebounceTime"),
        ("Juniper-IP-MIB", "juniIpIfForwarding"),
        ("Juniper-IP-MIB", "juniIpIfForceFragmentation"),
        ("Juniper-IP-MIB", "juniIpIfSharesLowerUid"),
        ("Juniper-IP-MIB", "juniIpIfFilterOptions"),
        ("Juniper-IP-MIB", "juniIpIfName"),
        ("Juniper-IP-MIB", "juniIpIfArpTimeout"),
        ("Juniper-IP-MIB", "juniIpIfAdminSpeed"),
        ("Juniper-IP-MIB", "juniIpIfMultipathMode"),
        ("Juniper-IP-MIB", "juniIpIfSharedNhAddr"),
        ("Juniper-IP-MIB", "juniIpIfSharedNhRouterId"),
        ("Juniper-IP-MIB", "juniIpIfPrimaryIpAddress"),
        ("Juniper-IP-MIB", "juniIpIfPrimaryIpMask"),
        ("Juniper-IP-MIB", "juniIpIfOperDebounceTime"),
        ("Juniper-IP-MIB", "juniIpIfRouterIndex"),
        ("Juniper-IP-MIB", "juniIpIfInheritNum"),
        ("Juniper-IP-MIB", "juniIpIfInheritNumUid"),
        ("Juniper-IP-MIB", "juniIpIfAnalyzerMode"),
        ("Juniper-IP-MIB", "juniIpIfAutoConfigure"),
        ("Juniper-IP-MIB", "juniIpIfTcpMss"),
        ("Juniper-IP-MIB", "juniIpIfInitSeqPrefOper"),
        ("Juniper-IP-MIB", "juniIpIfInitSeqPrefAdmin"),
        ("Juniper-IP-MIB", "juniIpIfArpSpoofCheck"),
        ("Juniper-IP-MIB", "juniIpIfStatsInPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInOctets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInPoliciedPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInPoliciedOctets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInErrorPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsInSpoofedPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutForwardedPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutForwardedOctets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutSchedDropPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutSchedDropOctets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutPoliciedPackets"),
        ("Juniper-IP-MIB", "juniIpIfStatsOutPoliciedOctets"),
        ("Juniper-IP-MIB", "juniIpIfAssocIpIfIndex"))
)
if mibBuilder.loadTexts:
    juniIpInterfaceGroup9.setStatus("current")


# Notification objects

juniIpRouteTableTrapRouteLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 3, 0, 1)
)
juniIpRouteTableTrapRouteLimitExceeded.setObjects(
      *(("Juniper-IP-MIB", "juniIpRouteTableLimit"),
        ("IP-FORWARD-MIB", "ipCidrRouteNumber"))
)
if mibBuilder.loadTexts:
    juniIpRouteTableTrapRouteLimitExceeded.setStatus(
        "current"
    )

juniIpRouteTableTrapRouteLimitRemove = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 3, 0, 2)
)
juniIpRouteTableTrapRouteLimitRemove.setObjects(
      *(("Juniper-IP-MIB", "juniIpRouteTableLimit"),
        ("IP-FORWARD-MIB", "ipCidrRouteNumber"))
)
if mibBuilder.loadTexts:
    juniIpRouteTableTrapRouteLimitRemove.setStatus(
        "current"
    )

juniIpRouteTableTrapWarnThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 3, 0, 3)
)
juniIpRouteTableTrapWarnThresholdExceeded.setObjects(
      *(("Juniper-IP-MIB", "juniIpRouteTableLimit"),
        ("Juniper-IP-MIB", "juniIpRouteTableWarnThreshold"),
        ("IP-FORWARD-MIB", "ipCidrRouteNumber"))
)
if mibBuilder.loadTexts:
    juniIpRouteTableTrapWarnThresholdExceeded.setStatus(
        "current"
    )

juniIpTrapSaValidationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 3, 0, 4)
)
juniIpTrapSaValidationFailure.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("Juniper-IP-MIB", "juniIpIfSaValFailSrcIpAddr"),
        ("Juniper-IP-MIB", "juniIpIfSaValFailDestIpAddr"))
)
if mibBuilder.loadTexts:
    juniIpTrapSaValidationFailure.setStatus(
        "current"
    )


# Notifications groups

juniIpNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 2, 21)
)
juniIpNotificationGroup.setObjects(
      *(("Juniper-IP-MIB", "juniIpRouteTableTrapRouteLimitExceeded"),
        ("Juniper-IP-MIB", "juniIpRouteTableTrapRouteLimitRemove"),
        ("Juniper-IP-MIB", "juniIpRouteTableTrapWarnThresholdExceeded"))
)
if mibBuilder.loadTexts:
    juniIpNotificationGroup.setStatus(
        "obsolete"
    )

juniIpNotificationGroup1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 2, 22)
)
juniIpNotificationGroup1.setObjects(
      *(("Juniper-IP-MIB", "juniIpRouteTableTrapRouteLimitExceeded"),
        ("Juniper-IP-MIB", "juniIpRouteTableTrapRouteLimitRemove"),
        ("Juniper-IP-MIB", "juniIpRouteTableTrapWarnThresholdExceeded"),
        ("Juniper-IP-MIB", "juniIpTrapSaValidationFailure"))
)
if mibBuilder.loadTexts:
    juniIpNotificationGroup1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

juniIpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 1, 1)
)
if mibBuilder.loadTexts:
    juniIpCompliance.setStatus(
        "obsolete"
    )

juniIpCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 1, 2)
)
if mibBuilder.loadTexts:
    juniIpCompliance2.setStatus(
        "obsolete"
    )

juniIpCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 1, 3)
)
if mibBuilder.loadTexts:
    juniIpCompliance3.setStatus(
        "obsolete"
    )

juniIpCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 1, 4)
)
if mibBuilder.loadTexts:
    juniIpCompliance4.setStatus(
        "obsolete"
    )

juniIpCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 1, 5)
)
if mibBuilder.loadTexts:
    juniIpCompliance5.setStatus(
        "obsolete"
    )

juniIpCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 1, 6)
)
if mibBuilder.loadTexts:
    juniIpCompliance6.setStatus(
        "obsolete"
    )

juniIpCompliance7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 1, 7)
)
if mibBuilder.loadTexts:
    juniIpCompliance7.setStatus(
        "obsolete"
    )

juniIpCompliance8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 1, 8)
)
if mibBuilder.loadTexts:
    juniIpCompliance8.setStatus(
        "obsolete"
    )

juniIpCompliance9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 1, 9)
)
if mibBuilder.loadTexts:
    juniIpCompliance9.setStatus(
        "obsolete"
    )

juniIpCompliance10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 1, 10)
)
if mibBuilder.loadTexts:
    juniIpCompliance10.setStatus(
        "obsolete"
    )

juniIpCompliance11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 1, 11)
)
if mibBuilder.loadTexts:
    juniIpCompliance11.setStatus(
        "obsolete"
    )

juniIpCompliance12 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 1, 12)
)
if mibBuilder.loadTexts:
    juniIpCompliance12.setStatus(
        "obsolete"
    )

juniIpCompliance13 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 1, 13)
)
if mibBuilder.loadTexts:
    juniIpCompliance13.setStatus(
        "obsolete"
    )

juniIpCompliance14 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12, 4, 1, 14)
)
if mibBuilder.loadTexts:
    juniIpCompliance14.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-IP-MIB",
    **{"juniIpMIB": juniIpMIB,
       "juniIpObjects": juniIpObjects,
       "juniIpInterface": juniIpInterface,
       "juniIpNextIfIndex": juniIpNextIfIndex,
       "juniIpIfTable": juniIpIfTable,
       "juniIpIfEntry": juniIpIfEntry,
       "juniIpIfIndex": juniIpIfIndex,
       "juniIpIfRowStatus": juniIpIfRowStatus,
       "juniIpIfLowerIfIndex": juniIpIfLowerIfIndex,
       "juniIpIfType": juniIpIfType,
       "juniIpIfTypeId": juniIpIfTypeId,
       "juniIpIfSAValidationEnable": juniIpIfSAValidationEnable,
       "juniIpIfCreationType": juniIpIfCreationType,
       "juniIpIfProfileId": juniIpIfProfileId,
       "juniIpIfAlwaysUp": juniIpIfAlwaysUp,
       "juniIpIfLoopback": juniIpIfLoopback,
       "juniIpIfLoopbackUid": juniIpIfLoopbackUid,
       "juniIpIfDebounceTime": juniIpIfDebounceTime,
       "juniIpIfForwarding": juniIpIfForwarding,
       "juniIpIfForceFragmentation": juniIpIfForceFragmentation,
       "juniIpIfSharesLowerUid": juniIpIfSharesLowerUid,
       "juniIpIfFilterOptions": juniIpIfFilterOptions,
       "juniIpIfName": juniIpIfName,
       "juniIpIfArpTimeout": juniIpIfArpTimeout,
       "juniIpIfAdminSpeed": juniIpIfAdminSpeed,
       "juniIpIfMultipathMode": juniIpIfMultipathMode,
       "juniIpIfSharedNhAddr": juniIpIfSharedNhAddr,
       "juniIpIfSharedNhRouterId": juniIpIfSharedNhRouterId,
       "juniIpIfPrimaryIpAddress": juniIpIfPrimaryIpAddress,
       "juniIpIfPrimaryIpMask": juniIpIfPrimaryIpMask,
       "juniIpIfOperDebounceTime": juniIpIfOperDebounceTime,
       "juniIpIfRouterIndex": juniIpIfRouterIndex,
       "juniIpIfInheritNum": juniIpIfInheritNum,
       "juniIpIfInheritNumUid": juniIpIfInheritNumUid,
       "juniIpIfAnalyzerMode": juniIpIfAnalyzerMode,
       "juniIpIfAutoConfigure": juniIpIfAutoConfigure,
       "juniIpIfTcpMss": juniIpIfTcpMss,
       "juniIpIfInitSeqPrefOper": juniIpIfInitSeqPrefOper,
       "juniIpIfInitSeqPrefAdmin": juniIpIfInitSeqPrefAdmin,
       "juniIpIfArpSpoofCheck": juniIpIfArpSpoofCheck,
       "juniIpIfStatsTable": juniIpIfStatsTable,
       "juniIpIfStatsEntry": juniIpIfStatsEntry,
       "juniIpIfStatsIndex": juniIpIfStatsIndex,
       "juniIpIfStatsInPackets": juniIpIfStatsInPackets,
       "juniIpIfStatsInOctets": juniIpIfStatsInOctets,
       "juniIpIfStatsInPoliciedPackets": juniIpIfStatsInPoliciedPackets,
       "juniIpIfStatsInPoliciedOctets": juniIpIfStatsInPoliciedOctets,
       "juniIpIfStatsInErrorPackets": juniIpIfStatsInErrorPackets,
       "juniIpIfStatsInSpoofedPackets": juniIpIfStatsInSpoofedPackets,
       "juniIpIfStatsInForwardedPackets": juniIpIfStatsInForwardedPackets,
       "juniIpIfStatsInForwardedOctets": juniIpIfStatsInForwardedOctets,
       "juniIpIfStatsOutForwardedPackets": juniIpIfStatsOutForwardedPackets,
       "juniIpIfStatsOutForwardedOctets": juniIpIfStatsOutForwardedOctets,
       "juniIpIfStatsOutSchedDropPackets": juniIpIfStatsOutSchedDropPackets,
       "juniIpIfStatsOutSchedDropOctets": juniIpIfStatsOutSchedDropOctets,
       "juniIpIfStatsOutRequestedPackets": juniIpIfStatsOutRequestedPackets,
       "juniIpIfStatsOutRequestedOctets": juniIpIfStatsOutRequestedOctets,
       "juniIpIfStatsOutPoliciedPackets": juniIpIfStatsOutPoliciedPackets,
       "juniIpIfStatsOutPoliciedOctets": juniIpIfStatsOutPoliciedOctets,
       "juniIpIfStatsGreenOutSchedDropPackets": juniIpIfStatsGreenOutSchedDropPackets,
       "juniIpIfStatsYellowOutSchedDropPackets": juniIpIfStatsYellowOutSchedDropPackets,
       "juniIpIfStatsRedOutSchedDropPackets": juniIpIfStatsRedOutSchedDropPackets,
       "juniIpIfStatsGreenOutSchedDropOctets": juniIpIfStatsGreenOutSchedDropOctets,
       "juniIpIfStatsYellowOutSchedDropOctets": juniIpIfStatsYellowOutSchedDropOctets,
       "juniIpIfStatsRedOutSchedDropOctets": juniIpIfStatsRedOutSchedDropOctets,
       "juniIpIfAssocTable": juniIpIfAssocTable,
       "juniIpIfAssocEntry": juniIpIfAssocEntry,
       "juniIpIfAssocLowerIfIndex": juniIpIfAssocLowerIfIndex,
       "juniIpIfAssocIpIfIndex": juniIpIfAssocIpIfIndex,
       "juniIpAddress": juniIpAddress,
       "juniIpAddrGlobals": juniIpAddrGlobals,
       "juniIpArpTimeout": juniIpArpTimeout,
       "juniIpAddrTable": juniIpAddrTable,
       "juniIpAddrEntry": juniIpAddrEntry,
       "juniIpAdEntAddr": juniIpAdEntAddr,
       "juniIpAdEntIfIndex": juniIpAdEntIfIndex,
       "juniIpAdEntNetMask": juniIpAdEntNetMask,
       "juniIpAdEntBcastAddr": juniIpAdEntBcastAddr,
       "juniIpAdEntReasmMaxSize": juniIpAdEntReasmMaxSize,
       "juniIpAdEntRowStatus": juniIpAdEntRowStatus,
       "juniIpAdEntAdminStatus": juniIpAdEntAdminStatus,
       "juniIpAdEntArpRspEnable": juniIpAdEntArpRspEnable,
       "juniIpAdEntProxyArpRspEnable": juniIpAdEntProxyArpRspEnable,
       "juniIpAdEntIgmpEnable": juniIpAdEntIgmpEnable,
       "juniIpAdEntDirectedBcastEnable": juniIpAdEntDirectedBcastEnable,
       "juniIpAdEntIcmpRedirectEnable": juniIpAdEntIcmpRedirectEnable,
       "juniIpAdEntIcmpMaskReplyEnable": juniIpAdEntIcmpMaskReplyEnable,
       "juniIpAdEntIcmpUnreachEnable": juniIpAdEntIcmpUnreachEnable,
       "juniIpAdEntMtu": juniIpAdEntMtu,
       "juniIpAdEntUnnumLoopbackIfIndex": juniIpAdEntUnnumLoopbackIfIndex,
       "juniIpAdEntIrdpEnable": juniIpAdEntIrdpEnable,
       "juniIpAdEntAccessRouteEnable": juniIpAdEntAccessRouteEnable,
       "juniIpAdEntAccessRouteHost": juniIpAdEntAccessRouteHost,
       "juniIpAdEntIsSecondary": juniIpAdEntIsSecondary,
       "juniIpAdEntUnnumInheritNumIfIndex": juniIpAdEntUnnumInheritNumIfIndex,
       "juniIpRoute": juniIpRoute,
       "juniIpRouteGlobals": juniIpRouteGlobals,
       "juniIpRouteLimit": juniIpRouteLimit,
       "juniIpRouteTableLimit": juniIpRouteTableLimit,
       "juniIpRouteTableWarnPercent": juniIpRouteTableWarnPercent,
       "juniIpRouteTableWarnOnly": juniIpRouteTableWarnOnly,
       "juniIpRouteTableWarnThreshold": juniIpRouteTableWarnThreshold,
       "juniIpRouteStaticTable": juniIpRouteStaticTable,
       "juniIpRouteStaticEntry": juniIpRouteStaticEntry,
       "juniIpRouteStaticDest": juniIpRouteStaticDest,
       "juniIpRouteStaticMask": juniIpRouteStaticMask,
       "juniIpRouteStaticPref": juniIpRouteStaticPref,
       "juniIpRouteStaticNextHop": juniIpRouteStaticNextHop,
       "juniIpRouteStaticRowStatus": juniIpRouteStaticRowStatus,
       "juniIpRouteStaticIfIndex": juniIpRouteStaticIfIndex,
       "juniIpRouteStaticStatus": juniIpRouteStaticStatus,
       "juniIpRouteStaticNextHopAS": juniIpRouteStaticNextHopAS,
       "juniIpRouteStaticMetric": juniIpRouteStaticMetric,
       "juniIpRouteStaticTag": juniIpRouteStaticTag,
       "juniIpCidrRouteTable": juniIpCidrRouteTable,
       "juniIpCidrRouteEntry": juniIpCidrRouteEntry,
       "juniIpCidrRoutePref": juniIpCidrRoutePref,
       "juniIpCidrRouteArea": juniIpCidrRouteArea,
       "juniIpCidrRouteTag": juniIpCidrRouteTag,
       "juniIpRouteStaticBFDTable": juniIpRouteStaticBFDTable,
       "juniIpRouteStaticBFDEntry": juniIpRouteStaticBFDEntry,
       "juniIpRouteStaticBfdEnable": juniIpRouteStaticBfdEnable,
       "juniIpRouteStaticBfdMinRxInterval": juniIpRouteStaticBfdMinRxInterval,
       "juniIpRouteStaticBfdMinTxInterval": juniIpRouteStaticBfdMinTxInterval,
       "juniIpRouteStaticBfdMultiplier": juniIpRouteStaticBfdMultiplier,
       "juniIpGlobals": juniIpGlobals,
       "juniIpDebounceTime": juniIpDebounceTime,
       "juniIpRouterId": juniIpRouterId,
       "juniIpSourceRoutingAdminStatus": juniIpSourceRoutingAdminStatus,
       "juniIpVpnIdOui": juniIpVpnIdOui,
       "juniIpVpnIdIndex": juniIpVpnIdIndex,
       "juniIpBgpCommunityNewFormat": juniIpBgpCommunityNewFormat,
       "juniIpBgpAsConfedSetNewFormat": juniIpBgpAsConfedSetNewFormat,
       "juniIpIfSummary": juniIpIfSummary,
       "juniIpIfSummaryTotalIntf": juniIpIfSummaryTotalIntf,
       "juniIpIfSummaryTotalIntfUp": juniIpIfSummaryTotalIntfUp,
       "juniIpIfSummaryTotalIntfDown": juniIpIfSummaryTotalIntfDown,
       "juniIpIfSummaryTotalIntfProtUp": juniIpIfSummaryTotalIntfProtUp,
       "juniIpIfSummaryTotalIntfProtDown": juniIpIfSummaryTotalIntfProtDown,
       "juniIpIfSummaryTotalIntfProtNotPresent": juniIpIfSummaryTotalIntfProtNotPresent,
       "juniIpRouteSummary": juniIpRouteSummary,
       "juniIpRouteUnicastSummary": juniIpRouteUnicastSummary,
       "juniIpRouteSummaryUnicastTotalRoutes": juniIpRouteSummaryUnicastTotalRoutes,
       "juniIpRouteSummaryUnicastTotalBytes": juniIpRouteSummaryUnicastTotalBytes,
       "juniIpRouteSummaryUnicastIsisRoutes": juniIpRouteSummaryUnicastIsisRoutes,
       "juniIpRouteSummaryUnicastIsisLevel1Routes": juniIpRouteSummaryUnicastIsisLevel1Routes,
       "juniIpRouteSummaryUnicastIsisLevel2Routes": juniIpRouteSummaryUnicastIsisLevel2Routes,
       "juniIpRouteSummaryUnicastRipRoutes": juniIpRouteSummaryUnicastRipRoutes,
       "juniIpRouteSummaryUnicastStaticRoutes": juniIpRouteSummaryUnicastStaticRoutes,
       "juniIpRouteSummaryUnicastConnectedRoutes": juniIpRouteSummaryUnicastConnectedRoutes,
       "juniIpRouteSummaryUnicastBgpRoutes": juniIpRouteSummaryUnicastBgpRoutes,
       "juniIpRouteSummaryUnicastOspfRoutes": juniIpRouteSummaryUnicastOspfRoutes,
       "juniIpRouteSummaryUnicastIntraAreaOspfRoutes": juniIpRouteSummaryUnicastIntraAreaOspfRoutes,
       "juniIpRouteSummaryUnicastInterAreaOspfRoutes": juniIpRouteSummaryUnicastInterAreaOspfRoutes,
       "juniIpRouteSummaryUnicastExternalOspfRoutes": juniIpRouteSummaryUnicastExternalOspfRoutes,
       "juniIpRouteSummaryUnicastOtherInternalRoutes": juniIpRouteSummaryUnicastOtherInternalRoutes,
       "juniIpRouteSummaryUnicastAccessRoutes": juniIpRouteSummaryUnicastAccessRoutes,
       "juniIpRouteSummaryUnicastIntCreatedAccessHostRoutes": juniIpRouteSummaryUnicastIntCreatedAccessHostRoutes,
       "juniIpRouteSummaryUnicastIntDialoutRoutes": juniIpRouteSummaryUnicastIntDialoutRoutes,
       "juniIpRouteSummaryUnicastRouteMemoryActive": juniIpRouteSummaryUnicastRouteMemoryActive,
       "juniIpRouteSummaryUnicastLastRouteAddedOrDeletedIP": juniIpRouteSummaryUnicastLastRouteAddedOrDeletedIP,
       "juniIpRouteSummaryUnicastLastRouteAddedOrDeletedMask": juniIpRouteSummaryUnicastLastRouteAddedOrDeletedMask,
       "juniIpRouteSummaryUnicastLastRouteAddedOrDeletedClient": juniIpRouteSummaryUnicastLastRouteAddedOrDeletedClient,
       "juniIpRouteSummaryUnicastLastRouteAddedOrDeletedDate": juniIpRouteSummaryUnicastLastRouteAddedOrDeletedDate,
       "juniIpRouteMulticastSummary": juniIpRouteMulticastSummary,
       "juniIpRouteSummaryMulticastTotalRoutes": juniIpRouteSummaryMulticastTotalRoutes,
       "juniIpRouteSummaryMulticastTotalBytes": juniIpRouteSummaryMulticastTotalBytes,
       "juniIpRouteSummaryMulticastIsisRoutes": juniIpRouteSummaryMulticastIsisRoutes,
       "juniIpRouteSummaryMulticastLevel1IsisRoutes": juniIpRouteSummaryMulticastLevel1IsisRoutes,
       "juniIpRouteSummaryMulticastLevel2IsisRoutes": juniIpRouteSummaryMulticastLevel2IsisRoutes,
       "juniIpRouteSummaryMulticastRipRoutes": juniIpRouteSummaryMulticastRipRoutes,
       "juniIpRouteSummaryMulticastStaticRoutes": juniIpRouteSummaryMulticastStaticRoutes,
       "juniIpRouteSummaryMulticastConnectedRoutes": juniIpRouteSummaryMulticastConnectedRoutes,
       "juniIpRouteSummaryMulticastBgpRoutes": juniIpRouteSummaryMulticastBgpRoutes,
       "juniIpRouteSummaryMulticastOspfRoutes": juniIpRouteSummaryMulticastOspfRoutes,
       "juniIpRouteSummaryMulticastIntraAreaOspfRoutes": juniIpRouteSummaryMulticastIntraAreaOspfRoutes,
       "juniIpRouteSummaryMulticastInterAreaOspfRoutes": juniIpRouteSummaryMulticastInterAreaOspfRoutes,
       "juniIpRouteSummaryMulticastExternalOspfRoutes": juniIpRouteSummaryMulticastExternalOspfRoutes,
       "juniIpRouteSummaryMulticastOtherInternalRoutes": juniIpRouteSummaryMulticastOtherInternalRoutes,
       "juniIpRouteSummaryMulticastAccessRoutes": juniIpRouteSummaryMulticastAccessRoutes,
       "juniIpRouteSummaryMulticastIntCreatedAccessHostRoutes": juniIpRouteSummaryMulticastIntCreatedAccessHostRoutes,
       "juniIpRouteSummaryMultiastIntDialoutRoutes": juniIpRouteSummaryMultiastIntDialoutRoutes,
       "juniIpRouteSummaryMulticastRouteMemoryActive": juniIpRouteSummaryMulticastRouteMemoryActive,
       "juniIpRouteSummaryMulticastLastRouteAddedOrDeletedIP": juniIpRouteSummaryMulticastLastRouteAddedOrDeletedIP,
       "juniIpRouteSummaryMulticastLastRouteAddedOrDeletedMask": juniIpRouteSummaryMulticastLastRouteAddedOrDeletedMask,
       "juniIpRouteSummaryMulticastLastRouteAddedOrDeletedClient": juniIpRouteSummaryMulticastLastRouteAddedOrDeletedClient,
       "juniIpRouteSummaryMulticastLastRouteAddedOrDeletedDate": juniIpRouteSummaryMulticastLastRouteAddedOrDeletedDate,
       "juniIpTrapEnables": juniIpTrapEnables,
       "juniIpSaValidateTrapEnable": juniIpSaValidateTrapEnable,
       "juniIpTraps": juniIpTraps,
       "juniIpTrapPrefix": juniIpTrapPrefix,
       "juniIpRouteTableTrapRouteLimitExceeded": juniIpRouteTableTrapRouteLimitExceeded,
       "juniIpRouteTableTrapRouteLimitRemove": juniIpRouteTableTrapRouteLimitRemove,
       "juniIpRouteTableTrapWarnThresholdExceeded": juniIpRouteTableTrapWarnThresholdExceeded,
       "juniIpTrapSaValidationFailure": juniIpTrapSaValidationFailure,
       "juniIpMIBNotificationObjects": juniIpMIBNotificationObjects,
       "juniIpIfSaValFailSrcIpAddr": juniIpIfSaValFailSrcIpAddr,
       "juniIpIfSaValFailDestIpAddr": juniIpIfSaValFailDestIpAddr,
       "juniIpConformance": juniIpConformance,
       "juniIpCompliances": juniIpCompliances,
       "juniIpCompliance": juniIpCompliance,
       "juniIpCompliance2": juniIpCompliance2,
       "juniIpCompliance3": juniIpCompliance3,
       "juniIpCompliance4": juniIpCompliance4,
       "juniIpCompliance5": juniIpCompliance5,
       "juniIpCompliance6": juniIpCompliance6,
       "juniIpCompliance7": juniIpCompliance7,
       "juniIpCompliance8": juniIpCompliance8,
       "juniIpCompliance9": juniIpCompliance9,
       "juniIpCompliance10": juniIpCompliance10,
       "juniIpCompliance11": juniIpCompliance11,
       "juniIpCompliance12": juniIpCompliance12,
       "juniIpCompliance13": juniIpCompliance13,
       "juniIpCompliance14": juniIpCompliance14,
       "juniIpGroups": juniIpGroups,
       "juniIpInterfaceGroup": juniIpInterfaceGroup,
       "juniIpAddressGroup": juniIpAddressGroup,
       "juniIpRouteGroup": juniIpRouteGroup,
       "juniIpGlobalGroup": juniIpGlobalGroup,
       "juniIpInterfaceGroup2": juniIpInterfaceGroup2,
       "juniIpAddressGroup2": juniIpAddressGroup2,
       "juniIpInterfaceGroup3": juniIpInterfaceGroup3,
       "juniIpInterfaceGroup4": juniIpInterfaceGroup4,
       "juniIpAddressGroup3": juniIpAddressGroup3,
       "juniIpRouteGroup2": juniIpRouteGroup2,
       "juniIpGlobalGroup2": juniIpGlobalGroup2,
       "juniIpInterfaceGroup5": juniIpInterfaceGroup5,
       "juniIpAddressGroup4": juniIpAddressGroup4,
       "juniIpInterfaceDeprecatedGroup": juniIpInterfaceDeprecatedGroup,
       "juniIpAddressDeprecatedGroup": juniIpAddressDeprecatedGroup,
       "juniIpInterfaceGroup6": juniIpInterfaceGroup6,
       "juniIpIfSummaryGroup": juniIpIfSummaryGroup,
       "juniIpInterfaceGroup7": juniIpInterfaceGroup7,
       "juniIpGlobalGroup3": juniIpGlobalGroup3,
       "juniIpRouteGroup3": juniIpRouteGroup3,
       "juniIpNotificationGroup": juniIpNotificationGroup,
       "juniIpNotificationGroup1": juniIpNotificationGroup1,
       "juniIpMIBNotificationObjectsGroup": juniIpMIBNotificationObjectsGroup,
       "juniIpRouteSummaryGroup": juniIpRouteSummaryGroup,
       "juniIpRouteStaticBFDGroup": juniIpRouteStaticBFDGroup,
       "juniIpInterfaceGroup8": juniIpInterfaceGroup8,
       "juniIpInterfaceGroup9": juniIpInterfaceGroup9}
)
