# SNMP MIB module (ALCATEL-STATIC-FRR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-STATIC-FRR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:37:41 2024
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

(softentIND1MplsFrr,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1MplsFrr")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddressIPv4,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressType")

(MplsLabel,
 MplsObjectOwner) = mibBuilder.importSymbols(
    "MPLS-LSR-MIB",
    "MplsLabel",
    "MplsObjectOwner")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(TmnxOperState,) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TmnxOperState")


# MODULE-IDENTITY

alcatelStaticFrrMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 53, 1)
)
alcatelStaticFrrMIBModule.setRevisions(
        ("1909-02-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelStaticFrrMIBModuleObjs_ObjectIdentity = ObjectIdentity
alcatelStaticFrrMIBModuleObjs = _AlcatelStaticFrrMIBModuleObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 53, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelStaticFrrMIBModuleObjs.setStatus("current")
_VRtrStaticFrrMplsInSegmentTable_Object = MibTable
vRtrStaticFrrMplsInSegmentTable = _VRtrStaticFrrMplsInSegmentTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 53, 1, 1, 1)
)
if mibBuilder.loadTexts:
    vRtrStaticFrrMplsInSegmentTable.setStatus("current")
_VRtrStaticFrrMplsInSegmentEntry_Object = MibTableRow
vRtrStaticFrrMplsInSegmentEntry = _VRtrStaticFrrMplsInSegmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 53, 1, 1, 1, 1)
)
vRtrStaticFrrMplsInSegmentEntry.setIndexNames(
    (0, "ALCATEL-STATIC-FRR-MIB", "vRtrStaticFrrMplsInSegmentIfIndex"),
    (0, "ALCATEL-STATIC-FRR-MIB", "vRtrStaticFrrMplsInSegmentLabel"),
)
if mibBuilder.loadTexts:
    vRtrStaticFrrMplsInSegmentEntry.setStatus("current")
_VRtrStaticFrrMplsInSegmentIfIndex_Type = InterfaceIndexOrZero
_VRtrStaticFrrMplsInSegmentIfIndex_Object = MibTableColumn
vRtrStaticFrrMplsInSegmentIfIndex = _VRtrStaticFrrMplsInSegmentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 53, 1, 1, 1, 1, 1),
    _VRtrStaticFrrMplsInSegmentIfIndex_Type()
)
vRtrStaticFrrMplsInSegmentIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrStaticFrrMplsInSegmentIfIndex.setStatus("current")
_VRtrStaticFrrMplsInSegmentLabel_Type = MplsLabel
_VRtrStaticFrrMplsInSegmentLabel_Object = MibTableColumn
vRtrStaticFrrMplsInSegmentLabel = _VRtrStaticFrrMplsInSegmentLabel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 53, 1, 1, 1, 1, 2),
    _VRtrStaticFrrMplsInSegmentLabel_Type()
)
vRtrStaticFrrMplsInSegmentLabel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrStaticFrrMplsInSegmentLabel.setStatus("current")


class _VRtrStaticFrrMplsInSegmentNPop_Type(Integer32):
    """Custom type vRtrStaticFrrMplsInSegmentNPop based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VRtrStaticFrrMplsInSegmentNPop_Type.__name__ = "Integer32"
_VRtrStaticFrrMplsInSegmentNPop_Object = MibTableColumn
vRtrStaticFrrMplsInSegmentNPop = _VRtrStaticFrrMplsInSegmentNPop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 53, 1, 1, 1, 1, 3),
    _VRtrStaticFrrMplsInSegmentNPop_Type()
)
vRtrStaticFrrMplsInSegmentNPop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrStaticFrrMplsInSegmentNPop.setStatus("current")


class _VRtrStaticFrrMplsInSegmentXCIndex_Type(Integer32):
    """Custom type vRtrStaticFrrMplsInSegmentXCIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VRtrStaticFrrMplsInSegmentXCIndex_Type.__name__ = "Integer32"
_VRtrStaticFrrMplsInSegmentXCIndex_Object = MibTableColumn
vRtrStaticFrrMplsInSegmentXCIndex = _VRtrStaticFrrMplsInSegmentXCIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 53, 1, 1, 1, 1, 4),
    _VRtrStaticFrrMplsInSegmentXCIndex_Type()
)
vRtrStaticFrrMplsInSegmentXCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStaticFrrMplsInSegmentXCIndex.setStatus("current")


class _VRtrStaticFrrMplsInSegmentOwner_Type(MplsObjectOwner):
    """Custom type vRtrStaticFrrMplsInSegmentOwner based on MplsObjectOwner"""


_VRtrStaticFrrMplsInSegmentOwner_Object = MibTableColumn
vRtrStaticFrrMplsInSegmentOwner = _VRtrStaticFrrMplsInSegmentOwner_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 53, 1, 1, 1, 1, 5),
    _VRtrStaticFrrMplsInSegmentOwner_Type()
)
vRtrStaticFrrMplsInSegmentOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrStaticFrrMplsInSegmentOwner.setStatus("current")
_VRtrStaticFrrMplsInSegmentRowStatus_Type = RowStatus
_VRtrStaticFrrMplsInSegmentRowStatus_Object = MibTableColumn
vRtrStaticFrrMplsInSegmentRowStatus = _VRtrStaticFrrMplsInSegmentRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 53, 1, 1, 1, 1, 6),
    _VRtrStaticFrrMplsInSegmentRowStatus_Type()
)
vRtrStaticFrrMplsInSegmentRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrStaticFrrMplsInSegmentRowStatus.setStatus("current")


class _VRtrStaticFrrMplsOutSegmentIndexNext_Type(Integer32):
    """Custom type vRtrStaticFrrMplsOutSegmentIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VRtrStaticFrrMplsOutSegmentIndexNext_Type.__name__ = "Integer32"
_VRtrStaticFrrMplsOutSegmentIndexNext_Object = MibScalar
vRtrStaticFrrMplsOutSegmentIndexNext = _VRtrStaticFrrMplsOutSegmentIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 53, 1, 1, 2),
    _VRtrStaticFrrMplsOutSegmentIndexNext_Type()
)
vRtrStaticFrrMplsOutSegmentIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStaticFrrMplsOutSegmentIndexNext.setStatus("current")
_VRtrStaticFrrMplsOutSegmentTable_Object = MibTable
vRtrStaticFrrMplsOutSegmentTable = _VRtrStaticFrrMplsOutSegmentTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 53, 1, 1, 3)
)
if mibBuilder.loadTexts:
    vRtrStaticFrrMplsOutSegmentTable.setStatus("current")
_VRtrStaticFrrMplsOutSegmentEntry_Object = MibTableRow
vRtrStaticFrrMplsOutSegmentEntry = _VRtrStaticFrrMplsOutSegmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 53, 1, 1, 3, 1)
)
vRtrStaticFrrMplsOutSegmentEntry.setIndexNames(
    (0, "ALCATEL-STATIC-FRR-MIB", "vRtrStaticFrrMplsOutSegmentIndex"),
)
if mibBuilder.loadTexts:
    vRtrStaticFrrMplsOutSegmentEntry.setStatus("current")


class _VRtrStaticFrrMplsOutSegmentIndex_Type(Integer32):
    """Custom type vRtrStaticFrrMplsOutSegmentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VRtrStaticFrrMplsOutSegmentIndex_Type.__name__ = "Integer32"
_VRtrStaticFrrMplsOutSegmentIndex_Object = MibTableColumn
vRtrStaticFrrMplsOutSegmentIndex = _VRtrStaticFrrMplsOutSegmentIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 53, 1, 1, 3, 1, 1),
    _VRtrStaticFrrMplsOutSegmentIndex_Type()
)
vRtrStaticFrrMplsOutSegmentIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrStaticFrrMplsOutSegmentIndex.setStatus("current")
_VRtrStaticFrrMplsOutSegmentIfIndex_Type = InterfaceIndexOrZero
_VRtrStaticFrrMplsOutSegmentIfIndex_Object = MibTableColumn
vRtrStaticFrrMplsOutSegmentIfIndex = _VRtrStaticFrrMplsOutSegmentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 53, 1, 1, 3, 1, 2),
    _VRtrStaticFrrMplsOutSegmentIfIndex_Type()
)
vRtrStaticFrrMplsOutSegmentIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrStaticFrrMplsOutSegmentIfIndex.setStatus("current")
_VRtrStaticFrrMplsOutSegmentPushTopLabel_Type = TruthValue
_VRtrStaticFrrMplsOutSegmentPushTopLabel_Object = MibTableColumn
vRtrStaticFrrMplsOutSegmentPushTopLabel = _VRtrStaticFrrMplsOutSegmentPushTopLabel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 53, 1, 1, 3, 1, 3),
    _VRtrStaticFrrMplsOutSegmentPushTopLabel_Type()
)
vRtrStaticFrrMplsOutSegmentPushTopLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrStaticFrrMplsOutSegmentPushTopLabel.setStatus("current")
_VRtrStaticFrrMplsOutSegmentTopLabel_Type = MplsLabel
_VRtrStaticFrrMplsOutSegmentTopLabel_Object = MibTableColumn
vRtrStaticFrrMplsOutSegmentTopLabel = _VRtrStaticFrrMplsOutSegmentTopLabel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 53, 1, 1, 3, 1, 4),
    _VRtrStaticFrrMplsOutSegmentTopLabel_Type()
)
vRtrStaticFrrMplsOutSegmentTopLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrStaticFrrMplsOutSegmentTopLabel.setStatus("current")


class _VRtrStaticFrrMplsOutSegmentNextHopIpAddrType_Type(InetAddressType):
    """Custom type vRtrStaticFrrMplsOutSegmentNextHopIpAddrType based on InetAddressType"""


_VRtrStaticFrrMplsOutSegmentNextHopIpAddrType_Object = MibTableColumn
vRtrStaticFrrMplsOutSegmentNextHopIpAddrType = _VRtrStaticFrrMplsOutSegmentNextHopIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 53, 1, 1, 3, 1, 5),
    _VRtrStaticFrrMplsOutSegmentNextHopIpAddrType_Type()
)
vRtrStaticFrrMplsOutSegmentNextHopIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrStaticFrrMplsOutSegmentNextHopIpAddrType.setStatus("current")
_VRtrStaticFrrMplsOutSegmentNextHopIpv4Addr_Type = IpAddress
_VRtrStaticFrrMplsOutSegmentNextHopIpv4Addr_Object = MibTableColumn
vRtrStaticFrrMplsOutSegmentNextHopIpv4Addr = _VRtrStaticFrrMplsOutSegmentNextHopIpv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 53, 1, 1, 3, 1, 6),
    _VRtrStaticFrrMplsOutSegmentNextHopIpv4Addr_Type()
)
vRtrStaticFrrMplsOutSegmentNextHopIpv4Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrStaticFrrMplsOutSegmentNextHopIpv4Addr.setStatus("current")


class _VRtrStaticFrrMplsOutSegmentXCIndex_Type(Integer32):
    """Custom type vRtrStaticFrrMplsOutSegmentXCIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VRtrStaticFrrMplsOutSegmentXCIndex_Type.__name__ = "Integer32"
_VRtrStaticFrrMplsOutSegmentXCIndex_Object = MibTableColumn
vRtrStaticFrrMplsOutSegmentXCIndex = _VRtrStaticFrrMplsOutSegmentXCIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 53, 1, 1, 3, 1, 7),
    _VRtrStaticFrrMplsOutSegmentXCIndex_Type()
)
vRtrStaticFrrMplsOutSegmentXCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStaticFrrMplsOutSegmentXCIndex.setStatus("current")


class _VRtrStaticFrrMplsOutSegmentOwner_Type(MplsObjectOwner):
    """Custom type vRtrStaticFrrMplsOutSegmentOwner based on MplsObjectOwner"""


_VRtrStaticFrrMplsOutSegmentOwner_Object = MibTableColumn
vRtrStaticFrrMplsOutSegmentOwner = _VRtrStaticFrrMplsOutSegmentOwner_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 53, 1, 1, 3, 1, 8),
    _VRtrStaticFrrMplsOutSegmentOwner_Type()
)
vRtrStaticFrrMplsOutSegmentOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrStaticFrrMplsOutSegmentOwner.setStatus("current")
_VRtrStaticFrrMplsOutSegmentRowStatus_Type = RowStatus
_VRtrStaticFrrMplsOutSegmentRowStatus_Object = MibTableColumn
vRtrStaticFrrMplsOutSegmentRowStatus = _VRtrStaticFrrMplsOutSegmentRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 53, 1, 1, 3, 1, 9),
    _VRtrStaticFrrMplsOutSegmentRowStatus_Type()
)
vRtrStaticFrrMplsOutSegmentRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrStaticFrrMplsOutSegmentRowStatus.setStatus("current")


class _VRtrStaticFrrMplsXCIndexNext_Type(Integer32):
    """Custom type vRtrStaticFrrMplsXCIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VRtrStaticFrrMplsXCIndexNext_Type.__name__ = "Integer32"
_VRtrStaticFrrMplsXCIndexNext_Object = MibScalar
vRtrStaticFrrMplsXCIndexNext = _VRtrStaticFrrMplsXCIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 53, 1, 1, 4),
    _VRtrStaticFrrMplsXCIndexNext_Type()
)
vRtrStaticFrrMplsXCIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStaticFrrMplsXCIndexNext.setStatus("current")
_VRtrStaticFrrMplsXCTable_Object = MibTable
vRtrStaticFrrMplsXCTable = _VRtrStaticFrrMplsXCTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 53, 1, 1, 5)
)
if mibBuilder.loadTexts:
    vRtrStaticFrrMplsXCTable.setStatus("current")
_VRtrStaticFrrMplsXCEntry_Object = MibTableRow
vRtrStaticFrrMplsXCEntry = _VRtrStaticFrrMplsXCEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 53, 1, 1, 5, 1)
)
vRtrStaticFrrMplsXCEntry.setIndexNames(
    (0, "ALCATEL-STATIC-FRR-MIB", "vRtrStaticFrrMplsXCIndex"),
    (0, "ALCATEL-STATIC-FRR-MIB", "vRtrStaticFrrMplsInSegmentIfIndex"),
    (0, "ALCATEL-STATIC-FRR-MIB", "vRtrStaticFrrMplsInSegmentLabel"),
    (0, "ALCATEL-STATIC-FRR-MIB", "vRtrStaticFrrMplsOutSegmentIndex"),
)
if mibBuilder.loadTexts:
    vRtrStaticFrrMplsXCEntry.setStatus("current")


class _VRtrStaticFrrMplsXCIndex_Type(Integer32):
    """Custom type vRtrStaticFrrMplsXCIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VRtrStaticFrrMplsXCIndex_Type.__name__ = "Integer32"
_VRtrStaticFrrMplsXCIndex_Object = MibTableColumn
vRtrStaticFrrMplsXCIndex = _VRtrStaticFrrMplsXCIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 53, 1, 1, 5, 1, 1),
    _VRtrStaticFrrMplsXCIndex_Type()
)
vRtrStaticFrrMplsXCIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrStaticFrrMplsXCIndex.setStatus("current")
_VRtrStaticFrrMplsXCOwner_Type = MplsObjectOwner
_VRtrStaticFrrMplsXCOwner_Object = MibTableColumn
vRtrStaticFrrMplsXCOwner = _VRtrStaticFrrMplsXCOwner_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 53, 1, 1, 5, 1, 2),
    _VRtrStaticFrrMplsXCOwner_Type()
)
vRtrStaticFrrMplsXCOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrStaticFrrMplsXCOwner.setStatus("current")
_VRtrStaticFrrMplsXCRowStatus_Type = RowStatus
_VRtrStaticFrrMplsXCRowStatus_Object = MibTableColumn
vRtrStaticFrrMplsXCRowStatus = _VRtrStaticFrrMplsXCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 53, 1, 1, 5, 1, 3),
    _VRtrStaticFrrMplsXCRowStatus_Type()
)
vRtrStaticFrrMplsXCRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrStaticFrrMplsXCRowStatus.setStatus("current")


class _VRtrStaticFrrMplsXCAdminStatus_Type(Integer32):
    """Custom type vRtrStaticFrrMplsXCAdminStatus based on Integer32"""
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


_VRtrStaticFrrMplsXCAdminStatus_Type.__name__ = "Integer32"
_VRtrStaticFrrMplsXCAdminStatus_Object = MibTableColumn
vRtrStaticFrrMplsXCAdminStatus = _VRtrStaticFrrMplsXCAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 53, 1, 1, 5, 1, 4),
    _VRtrStaticFrrMplsXCAdminStatus_Type()
)
vRtrStaticFrrMplsXCAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrStaticFrrMplsXCAdminStatus.setStatus("current")


class _VRtrStaticFrrMplsXCOperStatus_Type(Integer32):
    """Custom type vRtrStaticFrrMplsXCOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("unknown", 4),
          ("up", 1))
    )


_VRtrStaticFrrMplsXCOperStatus_Type.__name__ = "Integer32"
_VRtrStaticFrrMplsXCOperStatus_Object = MibTableColumn
vRtrStaticFrrMplsXCOperStatus = _VRtrStaticFrrMplsXCOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 53, 1, 1, 5, 1, 5),
    _VRtrStaticFrrMplsXCOperStatus_Type()
)
vRtrStaticFrrMplsXCOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStaticFrrMplsXCOperStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-STATIC-FRR-MIB",
    **{"alcatelStaticFrrMIBModule": alcatelStaticFrrMIBModule,
       "alcatelStaticFrrMIBModuleObjs": alcatelStaticFrrMIBModuleObjs,
       "vRtrStaticFrrMplsInSegmentTable": vRtrStaticFrrMplsInSegmentTable,
       "vRtrStaticFrrMplsInSegmentEntry": vRtrStaticFrrMplsInSegmentEntry,
       "vRtrStaticFrrMplsInSegmentIfIndex": vRtrStaticFrrMplsInSegmentIfIndex,
       "vRtrStaticFrrMplsInSegmentLabel": vRtrStaticFrrMplsInSegmentLabel,
       "vRtrStaticFrrMplsInSegmentNPop": vRtrStaticFrrMplsInSegmentNPop,
       "vRtrStaticFrrMplsInSegmentXCIndex": vRtrStaticFrrMplsInSegmentXCIndex,
       "vRtrStaticFrrMplsInSegmentOwner": vRtrStaticFrrMplsInSegmentOwner,
       "vRtrStaticFrrMplsInSegmentRowStatus": vRtrStaticFrrMplsInSegmentRowStatus,
       "vRtrStaticFrrMplsOutSegmentIndexNext": vRtrStaticFrrMplsOutSegmentIndexNext,
       "vRtrStaticFrrMplsOutSegmentTable": vRtrStaticFrrMplsOutSegmentTable,
       "vRtrStaticFrrMplsOutSegmentEntry": vRtrStaticFrrMplsOutSegmentEntry,
       "vRtrStaticFrrMplsOutSegmentIndex": vRtrStaticFrrMplsOutSegmentIndex,
       "vRtrStaticFrrMplsOutSegmentIfIndex": vRtrStaticFrrMplsOutSegmentIfIndex,
       "vRtrStaticFrrMplsOutSegmentPushTopLabel": vRtrStaticFrrMplsOutSegmentPushTopLabel,
       "vRtrStaticFrrMplsOutSegmentTopLabel": vRtrStaticFrrMplsOutSegmentTopLabel,
       "vRtrStaticFrrMplsOutSegmentNextHopIpAddrType": vRtrStaticFrrMplsOutSegmentNextHopIpAddrType,
       "vRtrStaticFrrMplsOutSegmentNextHopIpv4Addr": vRtrStaticFrrMplsOutSegmentNextHopIpv4Addr,
       "vRtrStaticFrrMplsOutSegmentXCIndex": vRtrStaticFrrMplsOutSegmentXCIndex,
       "vRtrStaticFrrMplsOutSegmentOwner": vRtrStaticFrrMplsOutSegmentOwner,
       "vRtrStaticFrrMplsOutSegmentRowStatus": vRtrStaticFrrMplsOutSegmentRowStatus,
       "vRtrStaticFrrMplsXCIndexNext": vRtrStaticFrrMplsXCIndexNext,
       "vRtrStaticFrrMplsXCTable": vRtrStaticFrrMplsXCTable,
       "vRtrStaticFrrMplsXCEntry": vRtrStaticFrrMplsXCEntry,
       "vRtrStaticFrrMplsXCIndex": vRtrStaticFrrMplsXCIndex,
       "vRtrStaticFrrMplsXCOwner": vRtrStaticFrrMplsXCOwner,
       "vRtrStaticFrrMplsXCRowStatus": vRtrStaticFrrMplsXCRowStatus,
       "vRtrStaticFrrMplsXCAdminStatus": vRtrStaticFrrMplsXCAdminStatus,
       "vRtrStaticFrrMplsXCOperStatus": vRtrStaticFrrMplsXCOperStatus}
)
