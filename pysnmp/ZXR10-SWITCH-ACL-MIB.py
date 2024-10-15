# SNMP MIB module (ZXR10-SWITCH-ACL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZXR10-SWITCH-ACL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:21:07 2024
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
 enterprises,
 experimental,
 iso,
 mgmt) = mibBuilder.importSymbols(
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
    "enterprises",
    "experimental",
    "iso",
    "mgmt")

(DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zte_ObjectIdentity = ObjectIdentity
zte = _Zte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902)
)
_Zxr10_ObjectIdentity = ObjectIdentity
zxr10 = _Zxr10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3)
)
_Zxr10switch_ObjectIdentity = ObjectIdentity
zxr10switch = _Zxr10switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102)
)
_Zxr10ACL_ObjectIdentity = ObjectIdentity
zxr10ACL = _Zxr10ACL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2)
)
_Zxr10StandardACLTable_Object = MibTable
zxr10StandardACLTable = _Zxr10StandardACLTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 1)
)
if mibBuilder.loadTexts:
    zxr10StandardACLTable.setStatus("current")
_Zxr10StandardACLEntry_Object = MibTableRow
zxr10StandardACLEntry = _Zxr10StandardACLEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 1, 1)
)
zxr10StandardACLEntry.setIndexNames(
    (0, "ZXR10-SWITCH-ACL-MIB", "zxr10StandardACLNo"),
    (0, "ZXR10-SWITCH-ACL-MIB", "zxr10StandardACLRuleID"),
)
if mibBuilder.loadTexts:
    zxr10StandardACLEntry.setStatus("current")
_Zxr10StandardACLNo_Type = Integer32
_Zxr10StandardACLNo_Object = MibTableColumn
zxr10StandardACLNo = _Zxr10StandardACLNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 1, 1, 1),
    _Zxr10StandardACLNo_Type()
)
zxr10StandardACLNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10StandardACLNo.setStatus("current")
_Zxr10StandardACLName_Type = DisplayString
_Zxr10StandardACLName_Object = MibTableColumn
zxr10StandardACLName = _Zxr10StandardACLName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 1, 1, 2),
    _Zxr10StandardACLName_Type()
)
zxr10StandardACLName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10StandardACLName.setStatus("current")
_Zxr10StandardACLAlias_Type = DisplayString
_Zxr10StandardACLAlias_Object = MibTableColumn
zxr10StandardACLAlias = _Zxr10StandardACLAlias_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 1, 1, 3),
    _Zxr10StandardACLAlias_Type()
)
zxr10StandardACLAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10StandardACLAlias.setStatus("current")


class _Zxr10StandardACLMatchorder_Type(Integer32):
    """Custom type zxr10StandardACLMatchorder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("config", 0))
    )


_Zxr10StandardACLMatchorder_Type.__name__ = "Integer32"
_Zxr10StandardACLMatchorder_Object = MibTableColumn
zxr10StandardACLMatchorder = _Zxr10StandardACLMatchorder_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 1, 1, 4),
    _Zxr10StandardACLMatchorder_Type()
)
zxr10StandardACLMatchorder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10StandardACLMatchorder.setStatus("current")


class _Zxr10StandardACLRuleID_Type(Integer32):
    """Custom type zxr10StandardACLRuleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4000),
    )


_Zxr10StandardACLRuleID_Type.__name__ = "Integer32"
_Zxr10StandardACLRuleID_Object = MibTableColumn
zxr10StandardACLRuleID = _Zxr10StandardACLRuleID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 1, 1, 6),
    _Zxr10StandardACLRuleID_Type()
)
zxr10StandardACLRuleID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10StandardACLRuleID.setStatus("current")


class _Zxr10StandardACLPermitDeny_Type(Integer32):
    """Custom type zxr10StandardACLPermitDeny based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 0))
    )


_Zxr10StandardACLPermitDeny_Type.__name__ = "Integer32"
_Zxr10StandardACLPermitDeny_Object = MibTableColumn
zxr10StandardACLPermitDeny = _Zxr10StandardACLPermitDeny_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 1, 1, 7),
    _Zxr10StandardACLPermitDeny_Type()
)
zxr10StandardACLPermitDeny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10StandardACLPermitDeny.setStatus("current")
_Zxr10StandardACLSrcAddr_Type = IpAddress
_Zxr10StandardACLSrcAddr_Object = MibTableColumn
zxr10StandardACLSrcAddr = _Zxr10StandardACLSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 1, 1, 8),
    _Zxr10StandardACLSrcAddr_Type()
)
zxr10StandardACLSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10StandardACLSrcAddr.setStatus("current")
_Zxr10StandardACLSrcAddrSrcWildcard_Type = IpAddress
_Zxr10StandardACLSrcAddrSrcWildcard_Object = MibTableColumn
zxr10StandardACLSrcAddrSrcWildcard = _Zxr10StandardACLSrcAddrSrcWildcard_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 1, 1, 9),
    _Zxr10StandardACLSrcAddrSrcWildcard_Type()
)
zxr10StandardACLSrcAddrSrcWildcard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10StandardACLSrcAddrSrcWildcard.setStatus("current")


class _Zxr10StandardACLSrcAny_Type(Integer32):
    """Custom type zxr10StandardACLSrcAny based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("valid", 1))
    )


_Zxr10StandardACLSrcAny_Type.__name__ = "Integer32"
_Zxr10StandardACLSrcAny_Object = MibTableColumn
zxr10StandardACLSrcAny = _Zxr10StandardACLSrcAny_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 1, 1, 10),
    _Zxr10StandardACLSrcAny_Type()
)
zxr10StandardACLSrcAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10StandardACLSrcAny.setStatus("current")


class _Zxr10StandardACLFlag_Type(Integer32):
    """Custom type zxr10StandardACLFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 0))
    )


_Zxr10StandardACLFlag_Type.__name__ = "Integer32"
_Zxr10StandardACLFlag_Object = MibTableColumn
zxr10StandardACLFlag = _Zxr10StandardACLFlag_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 1, 1, 11),
    _Zxr10StandardACLFlag_Type()
)
zxr10StandardACLFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10StandardACLFlag.setStatus("current")
_Zxr10StandardACLTimeRangeName_Type = DisplayString
_Zxr10StandardACLTimeRangeName_Object = MibTableColumn
zxr10StandardACLTimeRangeName = _Zxr10StandardACLTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 1, 1, 12),
    _Zxr10StandardACLTimeRangeName_Type()
)
zxr10StandardACLTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10StandardACLTimeRangeName.setStatus("current")
_Zxr10StandardACLRuleDescription_Type = DisplayString
_Zxr10StandardACLRuleDescription_Object = MibTableColumn
zxr10StandardACLRuleDescription = _Zxr10StandardACLRuleDescription_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 1, 1, 13),
    _Zxr10StandardACLRuleDescription_Type()
)
zxr10StandardACLRuleDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10StandardACLRuleDescription.setStatus("current")
_Zxr10StandardACLRowStatus_Type = RowStatus
_Zxr10StandardACLRowStatus_Object = MibTableColumn
zxr10StandardACLRowStatus = _Zxr10StandardACLRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 1, 1, 14),
    _Zxr10StandardACLRowStatus_Type()
)
zxr10StandardACLRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10StandardACLRowStatus.setStatus("current")
_Zxr10ExtendedACLTable_Object = MibTable
zxr10ExtendedACLTable = _Zxr10ExtendedACLTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 2)
)
if mibBuilder.loadTexts:
    zxr10ExtendedACLTable.setStatus("current")
_Zxr10ExtendedACLEntry_Object = MibTableRow
zxr10ExtendedACLEntry = _Zxr10ExtendedACLEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 2, 1)
)
zxr10ExtendedACLEntry.setIndexNames(
    (0, "ZXR10-SWITCH-ACL-MIB", "zxr10ExtendedACLNo"),
    (0, "ZXR10-SWITCH-ACL-MIB", "zxr10ExtendedACLRuleID"),
)
if mibBuilder.loadTexts:
    zxr10ExtendedACLEntry.setStatus("current")
_Zxr10ExtendedACLNo_Type = Integer32
_Zxr10ExtendedACLNo_Object = MibTableColumn
zxr10ExtendedACLNo = _Zxr10ExtendedACLNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 2, 1, 1),
    _Zxr10ExtendedACLNo_Type()
)
zxr10ExtendedACLNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10ExtendedACLNo.setStatus("current")
_Zxr10ExtendedACLName_Type = DisplayString
_Zxr10ExtendedACLName_Object = MibTableColumn
zxr10ExtendedACLName = _Zxr10ExtendedACLName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 2, 1, 2),
    _Zxr10ExtendedACLName_Type()
)
zxr10ExtendedACLName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10ExtendedACLName.setStatus("current")
_Zxr10ExtendedACLAlias_Type = DisplayString
_Zxr10ExtendedACLAlias_Object = MibTableColumn
zxr10ExtendedACLAlias = _Zxr10ExtendedACLAlias_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 2, 1, 3),
    _Zxr10ExtendedACLAlias_Type()
)
zxr10ExtendedACLAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10ExtendedACLAlias.setStatus("current")


class _Zxr10ExtendedACLMatchorder_Type(Integer32):
    """Custom type zxr10ExtendedACLMatchorder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("config", 0))
    )


_Zxr10ExtendedACLMatchorder_Type.__name__ = "Integer32"
_Zxr10ExtendedACLMatchorder_Object = MibTableColumn
zxr10ExtendedACLMatchorder = _Zxr10ExtendedACLMatchorder_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 2, 1, 4),
    _Zxr10ExtendedACLMatchorder_Type()
)
zxr10ExtendedACLMatchorder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10ExtendedACLMatchorder.setStatus("current")


class _Zxr10ExtendedACLRuleID_Type(Integer32):
    """Custom type zxr10ExtendedACLRuleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4000),
    )


_Zxr10ExtendedACLRuleID_Type.__name__ = "Integer32"
_Zxr10ExtendedACLRuleID_Object = MibTableColumn
zxr10ExtendedACLRuleID = _Zxr10ExtendedACLRuleID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 2, 1, 6),
    _Zxr10ExtendedACLRuleID_Type()
)
zxr10ExtendedACLRuleID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10ExtendedACLRuleID.setStatus("current")


class _Zxr10ExtendedACLPermitDeny_Type(Integer32):
    """Custom type zxr10ExtendedACLPermitDeny based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 0))
    )


_Zxr10ExtendedACLPermitDeny_Type.__name__ = "Integer32"
_Zxr10ExtendedACLPermitDeny_Object = MibTableColumn
zxr10ExtendedACLPermitDeny = _Zxr10ExtendedACLPermitDeny_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 2, 1, 7),
    _Zxr10ExtendedACLPermitDeny_Type()
)
zxr10ExtendedACLPermitDeny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10ExtendedACLPermitDeny.setStatus("current")
_Zxr10ExtendedACLSrcAddr_Type = IpAddress
_Zxr10ExtendedACLSrcAddr_Object = MibTableColumn
zxr10ExtendedACLSrcAddr = _Zxr10ExtendedACLSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 2, 1, 8),
    _Zxr10ExtendedACLSrcAddr_Type()
)
zxr10ExtendedACLSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10ExtendedACLSrcAddr.setStatus("current")
_Zxr10ExtendedACLSrcWildcard_Type = IpAddress
_Zxr10ExtendedACLSrcWildcard_Object = MibTableColumn
zxr10ExtendedACLSrcWildcard = _Zxr10ExtendedACLSrcWildcard_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 2, 1, 9),
    _Zxr10ExtendedACLSrcWildcard_Type()
)
zxr10ExtendedACLSrcWildcard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10ExtendedACLSrcWildcard.setStatus("current")


class _Zxr10ExtendedACLSrcAny_Type(Integer32):
    """Custom type zxr10ExtendedACLSrcAny based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("valid", 1))
    )


_Zxr10ExtendedACLSrcAny_Type.__name__ = "Integer32"
_Zxr10ExtendedACLSrcAny_Object = MibTableColumn
zxr10ExtendedACLSrcAny = _Zxr10ExtendedACLSrcAny_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 2, 1, 10),
    _Zxr10ExtendedACLSrcAny_Type()
)
zxr10ExtendedACLSrcAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10ExtendedACLSrcAny.setStatus("current")
_Zxr10ExtendedACLDestAddr_Type = IpAddress
_Zxr10ExtendedACLDestAddr_Object = MibTableColumn
zxr10ExtendedACLDestAddr = _Zxr10ExtendedACLDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 2, 1, 11),
    _Zxr10ExtendedACLDestAddr_Type()
)
zxr10ExtendedACLDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10ExtendedACLDestAddr.setStatus("current")
_Zxr10ExtendedACLDestWildcard_Type = IpAddress
_Zxr10ExtendedACLDestWildcard_Object = MibTableColumn
zxr10ExtendedACLDestWildcard = _Zxr10ExtendedACLDestWildcard_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 2, 1, 12),
    _Zxr10ExtendedACLDestWildcard_Type()
)
zxr10ExtendedACLDestWildcard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10ExtendedACLDestWildcard.setStatus("current")


class _Zxr10ExtendedACLDestAny_Type(Integer32):
    """Custom type zxr10ExtendedACLDestAny based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("valid", 1))
    )


_Zxr10ExtendedACLDestAny_Type.__name__ = "Integer32"
_Zxr10ExtendedACLDestAny_Object = MibTableColumn
zxr10ExtendedACLDestAny = _Zxr10ExtendedACLDestAny_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 2, 1, 13),
    _Zxr10ExtendedACLDestAny_Type()
)
zxr10ExtendedACLDestAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10ExtendedACLDestAny.setStatus("current")


class _Zxr10ExtendedACLProtocol_Type(Integer32):
    """Custom type zxr10ExtendedACLProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Zxr10ExtendedACLProtocol_Type.__name__ = "Integer32"
_Zxr10ExtendedACLProtocol_Object = MibTableColumn
zxr10ExtendedACLProtocol = _Zxr10ExtendedACLProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 2, 1, 14),
    _Zxr10ExtendedACLProtocol_Type()
)
zxr10ExtendedACLProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10ExtendedACLProtocol.setStatus("current")


class _Zxr10ExtendedACLSrcOpr_Type(Integer32):
    """Custom type zxr10ExtendedACLSrcOpr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              7)
        )
    )
    namedValues = NamedValues(
        *(("eq", 1),
          ("ge", 2),
          ("invalid", 0),
          ("le", 3),
          ("range", 7))
    )


_Zxr10ExtendedACLSrcOpr_Type.__name__ = "Integer32"
_Zxr10ExtendedACLSrcOpr_Object = MibTableColumn
zxr10ExtendedACLSrcOpr = _Zxr10ExtendedACLSrcOpr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 2, 1, 15),
    _Zxr10ExtendedACLSrcOpr_Type()
)
zxr10ExtendedACLSrcOpr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10ExtendedACLSrcOpr.setStatus("current")


class _Zxr10ExtendedACLSrcPort_Type(Integer32):
    """Custom type zxr10ExtendedACLSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Zxr10ExtendedACLSrcPort_Type.__name__ = "Integer32"
_Zxr10ExtendedACLSrcPort_Object = MibTableColumn
zxr10ExtendedACLSrcPort = _Zxr10ExtendedACLSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 2, 1, 16),
    _Zxr10ExtendedACLSrcPort_Type()
)
zxr10ExtendedACLSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10ExtendedACLSrcPort.setStatus("current")


class _Zxr10ExtendedACLSrcPort2_Type(Integer32):
    """Custom type zxr10ExtendedACLSrcPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Zxr10ExtendedACLSrcPort2_Type.__name__ = "Integer32"
_Zxr10ExtendedACLSrcPort2_Object = MibTableColumn
zxr10ExtendedACLSrcPort2 = _Zxr10ExtendedACLSrcPort2_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 2, 1, 17),
    _Zxr10ExtendedACLSrcPort2_Type()
)
zxr10ExtendedACLSrcPort2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10ExtendedACLSrcPort2.setStatus("current")


class _Zxr10ExtendedACLDestOpr_Type(Integer32):
    """Custom type zxr10ExtendedACLDestOpr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              7)
        )
    )
    namedValues = NamedValues(
        *(("eq", 1),
          ("ge", 2),
          ("invalid", 0),
          ("le", 3),
          ("range", 7))
    )


_Zxr10ExtendedACLDestOpr_Type.__name__ = "Integer32"
_Zxr10ExtendedACLDestOpr_Object = MibTableColumn
zxr10ExtendedACLDestOpr = _Zxr10ExtendedACLDestOpr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 2, 1, 18),
    _Zxr10ExtendedACLDestOpr_Type()
)
zxr10ExtendedACLDestOpr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10ExtendedACLDestOpr.setStatus("current")


class _Zxr10ExtendedACLDestPort_Type(Integer32):
    """Custom type zxr10ExtendedACLDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Zxr10ExtendedACLDestPort_Type.__name__ = "Integer32"
_Zxr10ExtendedACLDestPort_Object = MibTableColumn
zxr10ExtendedACLDestPort = _Zxr10ExtendedACLDestPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 2, 1, 19),
    _Zxr10ExtendedACLDestPort_Type()
)
zxr10ExtendedACLDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10ExtendedACLDestPort.setStatus("current")


class _Zxr10ExtendedACLDestPort2_Type(Integer32):
    """Custom type zxr10ExtendedACLDestPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Zxr10ExtendedACLDestPort2_Type.__name__ = "Integer32"
_Zxr10ExtendedACLDestPort2_Object = MibTableColumn
zxr10ExtendedACLDestPort2 = _Zxr10ExtendedACLDestPort2_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 2, 1, 20),
    _Zxr10ExtendedACLDestPort2_Type()
)
zxr10ExtendedACLDestPort2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10ExtendedACLDestPort2.setStatus("current")


class _Zxr10ExtendedACLTCPEstablish_Type(Integer32):
    """Custom type zxr10ExtendedACLTCPEstablish based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Zxr10ExtendedACLTCPEstablish_Type.__name__ = "Integer32"
_Zxr10ExtendedACLTCPEstablish_Object = MibTableColumn
zxr10ExtendedACLTCPEstablish = _Zxr10ExtendedACLTCPEstablish_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 2, 1, 21),
    _Zxr10ExtendedACLTCPEstablish_Type()
)
zxr10ExtendedACLTCPEstablish.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10ExtendedACLTCPEstablish.setStatus("current")


class _Zxr10ExtendedACLTCPControl_Type(Integer32):
    """Custom type zxr10ExtendedACLTCPControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Zxr10ExtendedACLTCPControl_Type.__name__ = "Integer32"
_Zxr10ExtendedACLTCPControl_Object = MibTableColumn
zxr10ExtendedACLTCPControl = _Zxr10ExtendedACLTCPControl_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 2, 1, 22),
    _Zxr10ExtendedACLTCPControl_Type()
)
zxr10ExtendedACLTCPControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10ExtendedACLTCPControl.setStatus("current")


class _Zxr10ExtendedACLICMPType_Type(Integer32):
    """Custom type zxr10ExtendedACLICMPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_Zxr10ExtendedACLICMPType_Type.__name__ = "Integer32"
_Zxr10ExtendedACLICMPType_Object = MibTableColumn
zxr10ExtendedACLICMPType = _Zxr10ExtendedACLICMPType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 2, 1, 23),
    _Zxr10ExtendedACLICMPType_Type()
)
zxr10ExtendedACLICMPType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10ExtendedACLICMPType.setStatus("current")


class _Zxr10ExtendedACLICMPCode_Type(Integer32):
    """Custom type zxr10ExtendedACLICMPCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_Zxr10ExtendedACLICMPCode_Type.__name__ = "Integer32"
_Zxr10ExtendedACLICMPCode_Object = MibTableColumn
zxr10ExtendedACLICMPCode = _Zxr10ExtendedACLICMPCode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 2, 1, 24),
    _Zxr10ExtendedACLICMPCode_Type()
)
zxr10ExtendedACLICMPCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10ExtendedACLICMPCode.setStatus("current")


class _Zxr10ExtendedACLPrecedence_Type(Integer32):
    """Custom type zxr10ExtendedACLPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Zxr10ExtendedACLPrecedence_Type.__name__ = "Integer32"
_Zxr10ExtendedACLPrecedence_Object = MibTableColumn
zxr10ExtendedACLPrecedence = _Zxr10ExtendedACLPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 2, 1, 25),
    _Zxr10ExtendedACLPrecedence_Type()
)
zxr10ExtendedACLPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10ExtendedACLPrecedence.setStatus("current")


class _Zxr10ExtendedACLTOS_Type(Integer32):
    """Custom type zxr10ExtendedACLTOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Zxr10ExtendedACLTOS_Type.__name__ = "Integer32"
_Zxr10ExtendedACLTOS_Object = MibTableColumn
zxr10ExtendedACLTOS = _Zxr10ExtendedACLTOS_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 2, 1, 26),
    _Zxr10ExtendedACLTOS_Type()
)
zxr10ExtendedACLTOS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10ExtendedACLTOS.setStatus("current")


class _Zxr10ExtendedACLDSCP_Type(Integer32):
    """Custom type zxr10ExtendedACLDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Zxr10ExtendedACLDSCP_Type.__name__ = "Integer32"
_Zxr10ExtendedACLDSCP_Object = MibTableColumn
zxr10ExtendedACLDSCP = _Zxr10ExtendedACLDSCP_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 2, 1, 27),
    _Zxr10ExtendedACLDSCP_Type()
)
zxr10ExtendedACLDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10ExtendedACLDSCP.setStatus("current")


class _Zxr10ExtendedACLFlag_Type(Integer32):
    """Custom type zxr10ExtendedACLFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 0))
    )


_Zxr10ExtendedACLFlag_Type.__name__ = "Integer32"
_Zxr10ExtendedACLFlag_Object = MibTableColumn
zxr10ExtendedACLFlag = _Zxr10ExtendedACLFlag_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 2, 1, 28),
    _Zxr10ExtendedACLFlag_Type()
)
zxr10ExtendedACLFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10ExtendedACLFlag.setStatus("current")
_Zxr10ExtendedACLTimeRangeName_Type = DisplayString
_Zxr10ExtendedACLTimeRangeName_Object = MibTableColumn
zxr10ExtendedACLTimeRangeName = _Zxr10ExtendedACLTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 2, 1, 29),
    _Zxr10ExtendedACLTimeRangeName_Type()
)
zxr10ExtendedACLTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10ExtendedACLTimeRangeName.setStatus("current")
_Zxr10ExtendedACLRuleDescription_Type = DisplayString
_Zxr10ExtendedACLRuleDescription_Object = MibTableColumn
zxr10ExtendedACLRuleDescription = _Zxr10ExtendedACLRuleDescription_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 2, 1, 30),
    _Zxr10ExtendedACLRuleDescription_Type()
)
zxr10ExtendedACLRuleDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10ExtendedACLRuleDescription.setStatus("current")
_Zxr10ExtendedACLRowStatus_Type = RowStatus
_Zxr10ExtendedACLRowStatus_Object = MibTableColumn
zxr10ExtendedACLRowStatus = _Zxr10ExtendedACLRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 2, 1, 31),
    _Zxr10ExtendedACLRowStatus_Type()
)
zxr10ExtendedACLRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10ExtendedACLRowStatus.setStatus("current")
_Zxr10LinkACLTable_Object = MibTable
zxr10LinkACLTable = _Zxr10LinkACLTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 3)
)
if mibBuilder.loadTexts:
    zxr10LinkACLTable.setStatus("current")
_Zxr10LinkACLEntry_Object = MibTableRow
zxr10LinkACLEntry = _Zxr10LinkACLEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 3, 1)
)
zxr10LinkACLEntry.setIndexNames(
    (0, "ZXR10-SWITCH-ACL-MIB", "zxr10LinkACLNo"),
    (0, "ZXR10-SWITCH-ACL-MIB", "zxr10LinkACLRuleID"),
)
if mibBuilder.loadTexts:
    zxr10LinkACLEntry.setStatus("current")


class _Zxr10LinkACLNo_Type(Integer32):
    """Custom type zxr10LinkACLNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 299),
    )


_Zxr10LinkACLNo_Type.__name__ = "Integer32"
_Zxr10LinkACLNo_Object = MibTableColumn
zxr10LinkACLNo = _Zxr10LinkACLNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 3, 1, 1),
    _Zxr10LinkACLNo_Type()
)
zxr10LinkACLNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10LinkACLNo.setStatus("current")
_Zxr10LinkACLName_Type = DisplayString
_Zxr10LinkACLName_Object = MibTableColumn
zxr10LinkACLName = _Zxr10LinkACLName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 3, 1, 2),
    _Zxr10LinkACLName_Type()
)
zxr10LinkACLName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10LinkACLName.setStatus("current")
_Zxr10LinkACLAlias_Type = DisplayString
_Zxr10LinkACLAlias_Object = MibTableColumn
zxr10LinkACLAlias = _Zxr10LinkACLAlias_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 3, 1, 3),
    _Zxr10LinkACLAlias_Type()
)
zxr10LinkACLAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10LinkACLAlias.setStatus("current")


class _Zxr10LinkACLMatchorder_Type(Integer32):
    """Custom type zxr10LinkACLMatchorder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("config", 0))
    )


_Zxr10LinkACLMatchorder_Type.__name__ = "Integer32"
_Zxr10LinkACLMatchorder_Object = MibTableColumn
zxr10LinkACLMatchorder = _Zxr10LinkACLMatchorder_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 3, 1, 4),
    _Zxr10LinkACLMatchorder_Type()
)
zxr10LinkACLMatchorder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10LinkACLMatchorder.setStatus("current")


class _Zxr10LinkACLRuleID_Type(Integer32):
    """Custom type zxr10LinkACLRuleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_Zxr10LinkACLRuleID_Type.__name__ = "Integer32"
_Zxr10LinkACLRuleID_Object = MibTableColumn
zxr10LinkACLRuleID = _Zxr10LinkACLRuleID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 3, 1, 6),
    _Zxr10LinkACLRuleID_Type()
)
zxr10LinkACLRuleID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10LinkACLRuleID.setStatus("current")


class _Zxr10LinkACLPermitDeny_Type(Integer32):
    """Custom type zxr10LinkACLPermitDeny based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 0))
    )


_Zxr10LinkACLPermitDeny_Type.__name__ = "Integer32"
_Zxr10LinkACLPermitDeny_Object = MibTableColumn
zxr10LinkACLPermitDeny = _Zxr10LinkACLPermitDeny_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 3, 1, 7),
    _Zxr10LinkACLPermitDeny_Type()
)
zxr10LinkACLPermitDeny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10LinkACLPermitDeny.setStatus("current")


class _Zxr10LinkACLProtocol_Type(Integer32):
    """Custom type zxr10LinkACLProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_Zxr10LinkACLProtocol_Type.__name__ = "Integer32"
_Zxr10LinkACLProtocol_Object = MibTableColumn
zxr10LinkACLProtocol = _Zxr10LinkACLProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 3, 1, 8),
    _Zxr10LinkACLProtocol_Type()
)
zxr10LinkACLProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10LinkACLProtocol.setStatus("current")


class _Zxr10LinkACLCos_Type(Integer32):
    """Custom type zxr10LinkACLCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Zxr10LinkACLCos_Type.__name__ = "Integer32"
_Zxr10LinkACLCos_Object = MibTableColumn
zxr10LinkACLCos = _Zxr10LinkACLCos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 3, 1, 9),
    _Zxr10LinkACLCos_Type()
)
zxr10LinkACLCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10LinkACLCos.setStatus("current")


class _Zxr10LinkACLIncos_Type(Integer32):
    """Custom type zxr10LinkACLIncos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Zxr10LinkACLIncos_Type.__name__ = "Integer32"
_Zxr10LinkACLIncos_Object = MibTableColumn
zxr10LinkACLIncos = _Zxr10LinkACLIncos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 3, 1, 10),
    _Zxr10LinkACLIncos_Type()
)
zxr10LinkACLIncos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10LinkACLIncos.setStatus("current")


class _Zxr10LinkACLDinVlanID_Type(Integer32):
    """Custom type zxr10LinkACLDinVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Zxr10LinkACLDinVlanID_Type.__name__ = "Integer32"
_Zxr10LinkACLDinVlanID_Object = MibTableColumn
zxr10LinkACLDinVlanID = _Zxr10LinkACLDinVlanID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 3, 1, 11),
    _Zxr10LinkACLDinVlanID_Type()
)
zxr10LinkACLDinVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10LinkACLDinVlanID.setStatus("current")


class _Zxr10LinkACLDinVlanIDRight_Type(Integer32):
    """Custom type zxr10LinkACLDinVlanIDRight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Zxr10LinkACLDinVlanIDRight_Type.__name__ = "Integer32"
_Zxr10LinkACLDinVlanIDRight_Object = MibTableColumn
zxr10LinkACLDinVlanIDRight = _Zxr10LinkACLDinVlanIDRight_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 3, 1, 12),
    _Zxr10LinkACLDinVlanIDRight_Type()
)
zxr10LinkACLDinVlanIDRight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10LinkACLDinVlanIDRight.setStatus("current")


class _Zxr10LinkACLDoutVlanID_Type(Integer32):
    """Custom type zxr10LinkACLDoutVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Zxr10LinkACLDoutVlanID_Type.__name__ = "Integer32"
_Zxr10LinkACLDoutVlanID_Object = MibTableColumn
zxr10LinkACLDoutVlanID = _Zxr10LinkACLDoutVlanID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 3, 1, 13),
    _Zxr10LinkACLDoutVlanID_Type()
)
zxr10LinkACLDoutVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10LinkACLDoutVlanID.setStatus("current")


class _Zxr10LinkACLDoutVlanIDRight_Type(Integer32):
    """Custom type zxr10LinkACLDoutVlanIDRight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Zxr10LinkACLDoutVlanIDRight_Type.__name__ = "Integer32"
_Zxr10LinkACLDoutVlanIDRight_Object = MibTableColumn
zxr10LinkACLDoutVlanIDRight = _Zxr10LinkACLDoutVlanIDRight_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 3, 1, 14),
    _Zxr10LinkACLDoutVlanIDRight_Type()
)
zxr10LinkACLDoutVlanIDRight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10LinkACLDoutVlanIDRight.setStatus("current")
_Zxr10LinkACLInMAC_Type = MacAddress
_Zxr10LinkACLInMAC_Object = MibTableColumn
zxr10LinkACLInMAC = _Zxr10LinkACLInMAC_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 3, 1, 15),
    _Zxr10LinkACLInMAC_Type()
)
zxr10LinkACLInMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10LinkACLInMAC.setStatus("current")
_Zxr10LinkACLInMACWildcard_Type = MacAddress
_Zxr10LinkACLInMACWildcard_Object = MibTableColumn
zxr10LinkACLInMACWildcard = _Zxr10LinkACLInMACWildcard_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 3, 1, 16),
    _Zxr10LinkACLInMACWildcard_Type()
)
zxr10LinkACLInMACWildcard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10LinkACLInMACWildcard.setStatus("current")


class _Zxr10LinkACLInMACAny_Type(Integer32):
    """Custom type zxr10LinkACLInMACAny based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 0))
    )


_Zxr10LinkACLInMACAny_Type.__name__ = "Integer32"
_Zxr10LinkACLInMACAny_Object = MibTableColumn
zxr10LinkACLInMACAny = _Zxr10LinkACLInMACAny_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 3, 1, 17),
    _Zxr10LinkACLInMACAny_Type()
)
zxr10LinkACLInMACAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10LinkACLInMACAny.setStatus("current")
_Zxr10LinkACLOutMAC_Type = MacAddress
_Zxr10LinkACLOutMAC_Object = MibTableColumn
zxr10LinkACLOutMAC = _Zxr10LinkACLOutMAC_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 3, 1, 18),
    _Zxr10LinkACLOutMAC_Type()
)
zxr10LinkACLOutMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10LinkACLOutMAC.setStatus("current")
_Zxr10LinkACLOutMACWildCard_Type = MacAddress
_Zxr10LinkACLOutMACWildCard_Object = MibTableColumn
zxr10LinkACLOutMACWildCard = _Zxr10LinkACLOutMACWildCard_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 3, 1, 19),
    _Zxr10LinkACLOutMACWildCard_Type()
)
zxr10LinkACLOutMACWildCard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10LinkACLOutMACWildCard.setStatus("current")


class _Zxr10LinkACLOutMACAny_Type(Integer32):
    """Custom type zxr10LinkACLOutMACAny based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 0))
    )


_Zxr10LinkACLOutMACAny_Type.__name__ = "Integer32"
_Zxr10LinkACLOutMACAny_Object = MibTableColumn
zxr10LinkACLOutMACAny = _Zxr10LinkACLOutMACAny_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 3, 1, 20),
    _Zxr10LinkACLOutMACAny_Type()
)
zxr10LinkACLOutMACAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10LinkACLOutMACAny.setStatus("current")


class _Zxr10LinkACLFlag_Type(Integer32):
    """Custom type zxr10LinkACLFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 0))
    )


_Zxr10LinkACLFlag_Type.__name__ = "Integer32"
_Zxr10LinkACLFlag_Object = MibTableColumn
zxr10LinkACLFlag = _Zxr10LinkACLFlag_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 3, 1, 21),
    _Zxr10LinkACLFlag_Type()
)
zxr10LinkACLFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10LinkACLFlag.setStatus("current")
_Zxr10LinkACLTimeRangeName_Type = DisplayString
_Zxr10LinkACLTimeRangeName_Object = MibTableColumn
zxr10LinkACLTimeRangeName = _Zxr10LinkACLTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 3, 1, 22),
    _Zxr10LinkACLTimeRangeName_Type()
)
zxr10LinkACLTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10LinkACLTimeRangeName.setStatus("current")
_Zxr10LinkACLRuleDescription_Type = DisplayString
_Zxr10LinkACLRuleDescription_Object = MibTableColumn
zxr10LinkACLRuleDescription = _Zxr10LinkACLRuleDescription_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 3, 1, 23),
    _Zxr10LinkACLRuleDescription_Type()
)
zxr10LinkACLRuleDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10LinkACLRuleDescription.setStatus("current")
_Zxr10LinkACLRowStatus_Type = RowStatus
_Zxr10LinkACLRowStatus_Object = MibTableColumn
zxr10LinkACLRowStatus = _Zxr10LinkACLRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 3, 1, 24),
    _Zxr10LinkACLRowStatus_Type()
)
zxr10LinkACLRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10LinkACLRowStatus.setStatus("current")
_Zxr10HybridACLTable_Object = MibTable
zxr10HybridACLTable = _Zxr10HybridACLTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 4)
)
if mibBuilder.loadTexts:
    zxr10HybridACLTable.setStatus("current")
_Zxr10HybridACLEntry_Object = MibTableRow
zxr10HybridACLEntry = _Zxr10HybridACLEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 4, 1)
)
zxr10HybridACLEntry.setIndexNames(
    (0, "ZXR10-SWITCH-ACL-MIB", "zxr10HybridACLNo"),
    (0, "ZXR10-SWITCH-ACL-MIB", "zxr10HybridACLRuleID"),
)
if mibBuilder.loadTexts:
    zxr10HybridACLEntry.setStatus("current")


class _Zxr10HybridACLNo_Type(Integer32):
    """Custom type zxr10HybridACLNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 349),
    )


_Zxr10HybridACLNo_Type.__name__ = "Integer32"
_Zxr10HybridACLNo_Object = MibTableColumn
zxr10HybridACLNo = _Zxr10HybridACLNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 4, 1, 1),
    _Zxr10HybridACLNo_Type()
)
zxr10HybridACLNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10HybridACLNo.setStatus("current")
_Zxr10HybridACLName_Type = DisplayString
_Zxr10HybridACLName_Object = MibTableColumn
zxr10HybridACLName = _Zxr10HybridACLName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 4, 1, 2),
    _Zxr10HybridACLName_Type()
)
zxr10HybridACLName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10HybridACLName.setStatus("current")
_Zxr10HybridACLAlias_Type = DisplayString
_Zxr10HybridACLAlias_Object = MibTableColumn
zxr10HybridACLAlias = _Zxr10HybridACLAlias_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 4, 1, 3),
    _Zxr10HybridACLAlias_Type()
)
zxr10HybridACLAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10HybridACLAlias.setStatus("current")


class _Zxr10HybridACLMatchorder_Type(Integer32):
    """Custom type zxr10HybridACLMatchorder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("config", 0))
    )


_Zxr10HybridACLMatchorder_Type.__name__ = "Integer32"
_Zxr10HybridACLMatchorder_Object = MibTableColumn
zxr10HybridACLMatchorder = _Zxr10HybridACLMatchorder_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 4, 1, 4),
    _Zxr10HybridACLMatchorder_Type()
)
zxr10HybridACLMatchorder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10HybridACLMatchorder.setStatus("current")


class _Zxr10HybridACLRuleID_Type(Integer32):
    """Custom type zxr10HybridACLRuleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_Zxr10HybridACLRuleID_Type.__name__ = "Integer32"
_Zxr10HybridACLRuleID_Object = MibTableColumn
zxr10HybridACLRuleID = _Zxr10HybridACLRuleID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 4, 1, 6),
    _Zxr10HybridACLRuleID_Type()
)
zxr10HybridACLRuleID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10HybridACLRuleID.setStatus("current")


class _Zxr10HybridACLPermitDeny_Type(Integer32):
    """Custom type zxr10HybridACLPermitDeny based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 0))
    )


_Zxr10HybridACLPermitDeny_Type.__name__ = "Integer32"
_Zxr10HybridACLPermitDeny_Object = MibTableColumn
zxr10HybridACLPermitDeny = _Zxr10HybridACLPermitDeny_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 4, 1, 7),
    _Zxr10HybridACLPermitDeny_Type()
)
zxr10HybridACLPermitDeny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10HybridACLPermitDeny.setStatus("current")


class _Zxr10HybridACLProtocol_Type(Integer32):
    """Custom type zxr10HybridACLProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Zxr10HybridACLProtocol_Type.__name__ = "Integer32"
_Zxr10HybridACLProtocol_Object = MibTableColumn
zxr10HybridACLProtocol = _Zxr10HybridACLProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 4, 1, 8),
    _Zxr10HybridACLProtocol_Type()
)
zxr10HybridACLProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10HybridACLProtocol.setStatus("current")
_Zxr10HybridACLSrcAddr_Type = IpAddress
_Zxr10HybridACLSrcAddr_Object = MibTableColumn
zxr10HybridACLSrcAddr = _Zxr10HybridACLSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 4, 1, 9),
    _Zxr10HybridACLSrcAddr_Type()
)
zxr10HybridACLSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10HybridACLSrcAddr.setStatus("current")
_Zxr10HybridACLSrcAddrWildcard_Type = IpAddress
_Zxr10HybridACLSrcAddrWildcard_Object = MibTableColumn
zxr10HybridACLSrcAddrWildcard = _Zxr10HybridACLSrcAddrWildcard_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 4, 1, 10),
    _Zxr10HybridACLSrcAddrWildcard_Type()
)
zxr10HybridACLSrcAddrWildcard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10HybridACLSrcAddrWildcard.setStatus("current")


class _Zxr10HybridACLSrcAny_Type(Integer32):
    """Custom type zxr10HybridACLSrcAny based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("valid", 1))
    )


_Zxr10HybridACLSrcAny_Type.__name__ = "Integer32"
_Zxr10HybridACLSrcAny_Object = MibTableColumn
zxr10HybridACLSrcAny = _Zxr10HybridACLSrcAny_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 4, 1, 11),
    _Zxr10HybridACLSrcAny_Type()
)
zxr10HybridACLSrcAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10HybridACLSrcAny.setStatus("current")
_Zxr10HybridACLDestAddr_Type = IpAddress
_Zxr10HybridACLDestAddr_Object = MibTableColumn
zxr10HybridACLDestAddr = _Zxr10HybridACLDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 4, 1, 12),
    _Zxr10HybridACLDestAddr_Type()
)
zxr10HybridACLDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10HybridACLDestAddr.setStatus("current")
_Zxr10HybridACLDestAddrWildcard_Type = IpAddress
_Zxr10HybridACLDestAddrWildcard_Object = MibTableColumn
zxr10HybridACLDestAddrWildcard = _Zxr10HybridACLDestAddrWildcard_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 4, 1, 13),
    _Zxr10HybridACLDestAddrWildcard_Type()
)
zxr10HybridACLDestAddrWildcard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10HybridACLDestAddrWildcard.setStatus("current")


class _Zxr10HybridACLDestAny_Type(Integer32):
    """Custom type zxr10HybridACLDestAny based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("valid", 1))
    )


_Zxr10HybridACLDestAny_Type.__name__ = "Integer32"
_Zxr10HybridACLDestAny_Object = MibTableColumn
zxr10HybridACLDestAny = _Zxr10HybridACLDestAny_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 4, 1, 14),
    _Zxr10HybridACLDestAny_Type()
)
zxr10HybridACLDestAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10HybridACLDestAny.setStatus("current")


class _Zxr10HybridACLSrcOpr_Type(Integer32):
    """Custom type zxr10HybridACLSrcOpr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eq", 1),
          ("invalid", 0))
    )


_Zxr10HybridACLSrcOpr_Type.__name__ = "Integer32"
_Zxr10HybridACLSrcOpr_Object = MibTableColumn
zxr10HybridACLSrcOpr = _Zxr10HybridACLSrcOpr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 4, 1, 15),
    _Zxr10HybridACLSrcOpr_Type()
)
zxr10HybridACLSrcOpr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10HybridACLSrcOpr.setStatus("current")


class _Zxr10HybridACLSrcPort_Type(Integer32):
    """Custom type zxr10HybridACLSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Zxr10HybridACLSrcPort_Type.__name__ = "Integer32"
_Zxr10HybridACLSrcPort_Object = MibTableColumn
zxr10HybridACLSrcPort = _Zxr10HybridACLSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 4, 1, 16),
    _Zxr10HybridACLSrcPort_Type()
)
zxr10HybridACLSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10HybridACLSrcPort.setStatus("current")


class _Zxr10HybridACLDestOpr_Type(Integer32):
    """Custom type zxr10HybridACLDestOpr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eq", 1),
          ("invalid", 0))
    )


_Zxr10HybridACLDestOpr_Type.__name__ = "Integer32"
_Zxr10HybridACLDestOpr_Object = MibTableColumn
zxr10HybridACLDestOpr = _Zxr10HybridACLDestOpr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 4, 1, 17),
    _Zxr10HybridACLDestOpr_Type()
)
zxr10HybridACLDestOpr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10HybridACLDestOpr.setStatus("current")


class _Zxr10HybridACLDestPort_Type(Integer32):
    """Custom type zxr10HybridACLDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Zxr10HybridACLDestPort_Type.__name__ = "Integer32"
_Zxr10HybridACLDestPort_Object = MibTableColumn
zxr10HybridACLDestPort = _Zxr10HybridACLDestPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 4, 1, 18),
    _Zxr10HybridACLDestPort_Type()
)
zxr10HybridACLDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10HybridACLDestPort.setStatus("current")


class _Zxr10HybridACLTCPControl_Type(Integer32):
    """Custom type zxr10HybridACLTCPControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Zxr10HybridACLTCPControl_Type.__name__ = "Integer32"
_Zxr10HybridACLTCPControl_Object = MibTableColumn
zxr10HybridACLTCPControl = _Zxr10HybridACLTCPControl_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 4, 1, 19),
    _Zxr10HybridACLTCPControl_Type()
)
zxr10HybridACLTCPControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10HybridACLTCPControl.setStatus("current")


class _Zxr10HybridACLTOS_Type(Integer32):
    """Custom type zxr10HybridACLTOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Zxr10HybridACLTOS_Type.__name__ = "Integer32"
_Zxr10HybridACLTOS_Object = MibTableColumn
zxr10HybridACLTOS = _Zxr10HybridACLTOS_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 4, 1, 20),
    _Zxr10HybridACLTOS_Type()
)
zxr10HybridACLTOS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10HybridACLTOS.setStatus("current")


class _Zxr10HybridACLPrecedence_Type(Integer32):
    """Custom type zxr10HybridACLPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Zxr10HybridACLPrecedence_Type.__name__ = "Integer32"
_Zxr10HybridACLPrecedence_Object = MibTableColumn
zxr10HybridACLPrecedence = _Zxr10HybridACLPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 4, 1, 21),
    _Zxr10HybridACLPrecedence_Type()
)
zxr10HybridACLPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10HybridACLPrecedence.setStatus("current")


class _Zxr10HybridACLDSCP_Type(Integer32):
    """Custom type zxr10HybridACLDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Zxr10HybridACLDSCP_Type.__name__ = "Integer32"
_Zxr10HybridACLDSCP_Object = MibTableColumn
zxr10HybridACLDSCP = _Zxr10HybridACLDSCP_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 4, 1, 22),
    _Zxr10HybridACLDSCP_Type()
)
zxr10HybridACLDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10HybridACLDSCP.setStatus("current")


class _Zxr10HybridACLIPNumber_Type(Integer32):
    """Custom type zxr10HybridACLIPNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Zxr10HybridACLIPNumber_Type.__name__ = "Integer32"
_Zxr10HybridACLIPNumber_Object = MibTableColumn
zxr10HybridACLIPNumber = _Zxr10HybridACLIPNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 4, 1, 23),
    _Zxr10HybridACLIPNumber_Type()
)
zxr10HybridACLIPNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10HybridACLIPNumber.setStatus("current")


class _Zxr10HybridACLCos_Type(Integer32):
    """Custom type zxr10HybridACLCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Zxr10HybridACLCos_Type.__name__ = "Integer32"
_Zxr10HybridACLCos_Object = MibTableColumn
zxr10HybridACLCos = _Zxr10HybridACLCos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 4, 1, 24),
    _Zxr10HybridACLCos_Type()
)
zxr10HybridACLCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10HybridACLCos.setStatus("current")


class _Zxr10HybridACLIncos_Type(Integer32):
    """Custom type zxr10HybridACLIncos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Zxr10HybridACLIncos_Type.__name__ = "Integer32"
_Zxr10HybridACLIncos_Object = MibTableColumn
zxr10HybridACLIncos = _Zxr10HybridACLIncos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 4, 1, 25),
    _Zxr10HybridACLIncos_Type()
)
zxr10HybridACLIncos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10HybridACLIncos.setStatus("current")


class _Zxr10HybridACLDinVlanID_Type(Integer32):
    """Custom type zxr10HybridACLDinVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Zxr10HybridACLDinVlanID_Type.__name__ = "Integer32"
_Zxr10HybridACLDinVlanID_Object = MibTableColumn
zxr10HybridACLDinVlanID = _Zxr10HybridACLDinVlanID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 4, 1, 26),
    _Zxr10HybridACLDinVlanID_Type()
)
zxr10HybridACLDinVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10HybridACLDinVlanID.setStatus("current")


class _Zxr10HybridACLDoutVlanID_Type(Integer32):
    """Custom type zxr10HybridACLDoutVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Zxr10HybridACLDoutVlanID_Type.__name__ = "Integer32"
_Zxr10HybridACLDoutVlanID_Object = MibTableColumn
zxr10HybridACLDoutVlanID = _Zxr10HybridACLDoutVlanID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 4, 1, 27),
    _Zxr10HybridACLDoutVlanID_Type()
)
zxr10HybridACLDoutVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10HybridACLDoutVlanID.setStatus("current")
_Zxr10HybridACLInMAC_Type = MacAddress
_Zxr10HybridACLInMAC_Object = MibTableColumn
zxr10HybridACLInMAC = _Zxr10HybridACLInMAC_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 4, 1, 28),
    _Zxr10HybridACLInMAC_Type()
)
zxr10HybridACLInMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10HybridACLInMAC.setStatus("current")
_Zxr10HybridACLInMACWildcard_Type = MacAddress
_Zxr10HybridACLInMACWildcard_Object = MibTableColumn
zxr10HybridACLInMACWildcard = _Zxr10HybridACLInMACWildcard_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 4, 1, 29),
    _Zxr10HybridACLInMACWildcard_Type()
)
zxr10HybridACLInMACWildcard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10HybridACLInMACWildcard.setStatus("current")


class _Zxr10HybridACLInMACAny_Type(Integer32):
    """Custom type zxr10HybridACLInMACAny based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 0))
    )


_Zxr10HybridACLInMACAny_Type.__name__ = "Integer32"
_Zxr10HybridACLInMACAny_Object = MibTableColumn
zxr10HybridACLInMACAny = _Zxr10HybridACLInMACAny_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 4, 1, 30),
    _Zxr10HybridACLInMACAny_Type()
)
zxr10HybridACLInMACAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10HybridACLInMACAny.setStatus("current")
_Zxr10HybridACLOutMAC_Type = MacAddress
_Zxr10HybridACLOutMAC_Object = MibTableColumn
zxr10HybridACLOutMAC = _Zxr10HybridACLOutMAC_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 4, 1, 31),
    _Zxr10HybridACLOutMAC_Type()
)
zxr10HybridACLOutMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10HybridACLOutMAC.setStatus("current")
_Zxr10HybridACLOutMACWildcard_Type = MacAddress
_Zxr10HybridACLOutMACWildcard_Object = MibTableColumn
zxr10HybridACLOutMACWildcard = _Zxr10HybridACLOutMACWildcard_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 4, 1, 32),
    _Zxr10HybridACLOutMACWildcard_Type()
)
zxr10HybridACLOutMACWildcard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10HybridACLOutMACWildcard.setStatus("current")


class _Zxr10HybridACLOutMACAny_Type(Integer32):
    """Custom type zxr10HybridACLOutMACAny based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 0))
    )


_Zxr10HybridACLOutMACAny_Type.__name__ = "Integer32"
_Zxr10HybridACLOutMACAny_Object = MibTableColumn
zxr10HybridACLOutMACAny = _Zxr10HybridACLOutMACAny_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 4, 1, 33),
    _Zxr10HybridACLOutMACAny_Type()
)
zxr10HybridACLOutMACAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10HybridACLOutMACAny.setStatus("current")


class _Zxr10HybridACLFlag_Type(Integer32):
    """Custom type zxr10HybridACLFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 0))
    )


_Zxr10HybridACLFlag_Type.__name__ = "Integer32"
_Zxr10HybridACLFlag_Object = MibTableColumn
zxr10HybridACLFlag = _Zxr10HybridACLFlag_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 4, 1, 34),
    _Zxr10HybridACLFlag_Type()
)
zxr10HybridACLFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10HybridACLFlag.setStatus("current")
_Zxr10HybridACLTimeRangeName_Type = DisplayString
_Zxr10HybridACLTimeRangeName_Object = MibTableColumn
zxr10HybridACLTimeRangeName = _Zxr10HybridACLTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 4, 1, 35),
    _Zxr10HybridACLTimeRangeName_Type()
)
zxr10HybridACLTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10HybridACLTimeRangeName.setStatus("current")
_Zxr10HybridACLRuleDescription_Type = DisplayString
_Zxr10HybridACLRuleDescription_Object = MibTableColumn
zxr10HybridACLRuleDescription = _Zxr10HybridACLRuleDescription_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 4, 1, 36),
    _Zxr10HybridACLRuleDescription_Type()
)
zxr10HybridACLRuleDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10HybridACLRuleDescription.setStatus("current")
_Zxr10HybridACLRowStatus_Type = RowStatus
_Zxr10HybridACLRowStatus_Object = MibTableColumn
zxr10HybridACLRowStatus = _Zxr10HybridACLRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 4, 1, 37),
    _Zxr10HybridACLRowStatus_Type()
)
zxr10HybridACLRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10HybridACLRowStatus.setStatus("current")
_Zxr10ACLBoundIfTable_Object = MibTable
zxr10ACLBoundIfTable = _Zxr10ACLBoundIfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 5)
)
if mibBuilder.loadTexts:
    zxr10ACLBoundIfTable.setStatus("current")
_Zxr10ACLBoundIfEntry_Object = MibTableRow
zxr10ACLBoundIfEntry = _Zxr10ACLBoundIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 5, 1)
)
zxr10ACLBoundIfEntry.setIndexNames(
    (0, "ZXR10-SWITCH-ACL-MIB", "zxr10ACLBoundIf"),
)
if mibBuilder.loadTexts:
    zxr10ACLBoundIfEntry.setStatus("current")
_Zxr10ACLBoundIf_Type = Integer32
_Zxr10ACLBoundIf_Object = MibTableColumn
zxr10ACLBoundIf = _Zxr10ACLBoundIf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 5, 1, 1),
    _Zxr10ACLBoundIf_Type()
)
zxr10ACLBoundIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10ACLBoundIf.setStatus("current")
_Zxr10ACLNo_Type = Integer32
_Zxr10ACLNo_Object = MibTableColumn
zxr10ACLNo = _Zxr10ACLNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 5, 1, 2),
    _Zxr10ACLNo_Type()
)
zxr10ACLNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10ACLNo.setStatus("current")
_Zxr10ACLName_Type = DisplayString
_Zxr10ACLName_Object = MibTableColumn
zxr10ACLName = _Zxr10ACLName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 5, 1, 3),
    _Zxr10ACLName_Type()
)
zxr10ACLName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10ACLName.setStatus("current")


class _Zxr10ACLBoundIfDirection_Type(Integer32):
    """Custom type zxr10ACLBoundIfDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("in", 0),
          ("out", 1))
    )


_Zxr10ACLBoundIfDirection_Type.__name__ = "Integer32"
_Zxr10ACLBoundIfDirection_Object = MibTableColumn
zxr10ACLBoundIfDirection = _Zxr10ACLBoundIfDirection_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 5, 1, 4),
    _Zxr10ACLBoundIfDirection_Type()
)
zxr10ACLBoundIfDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10ACLBoundIfDirection.setStatus("current")
_Zxr10ACLRowStatus_Type = RowStatus
_Zxr10ACLRowStatus_Object = MibTableColumn
zxr10ACLRowStatus = _Zxr10ACLRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 2, 5, 1, 5),
    _Zxr10ACLRowStatus_Type()
)
zxr10ACLRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10ACLRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZXR10-SWITCH-ACL-MIB",
    **{"DisplayString": DisplayString,
       "zte": zte,
       "zxr10": zxr10,
       "zxr10switch": zxr10switch,
       "zxr10ACL": zxr10ACL,
       "zxr10StandardACLTable": zxr10StandardACLTable,
       "zxr10StandardACLEntry": zxr10StandardACLEntry,
       "zxr10StandardACLNo": zxr10StandardACLNo,
       "zxr10StandardACLName": zxr10StandardACLName,
       "zxr10StandardACLAlias": zxr10StandardACLAlias,
       "zxr10StandardACLMatchorder": zxr10StandardACLMatchorder,
       "zxr10StandardACLRuleID": zxr10StandardACLRuleID,
       "zxr10StandardACLPermitDeny": zxr10StandardACLPermitDeny,
       "zxr10StandardACLSrcAddr": zxr10StandardACLSrcAddr,
       "zxr10StandardACLSrcAddrSrcWildcard": zxr10StandardACLSrcAddrSrcWildcard,
       "zxr10StandardACLSrcAny": zxr10StandardACLSrcAny,
       "zxr10StandardACLFlag": zxr10StandardACLFlag,
       "zxr10StandardACLTimeRangeName": zxr10StandardACLTimeRangeName,
       "zxr10StandardACLRuleDescription": zxr10StandardACLRuleDescription,
       "zxr10StandardACLRowStatus": zxr10StandardACLRowStatus,
       "zxr10ExtendedACLTable": zxr10ExtendedACLTable,
       "zxr10ExtendedACLEntry": zxr10ExtendedACLEntry,
       "zxr10ExtendedACLNo": zxr10ExtendedACLNo,
       "zxr10ExtendedACLName": zxr10ExtendedACLName,
       "zxr10ExtendedACLAlias": zxr10ExtendedACLAlias,
       "zxr10ExtendedACLMatchorder": zxr10ExtendedACLMatchorder,
       "zxr10ExtendedACLRuleID": zxr10ExtendedACLRuleID,
       "zxr10ExtendedACLPermitDeny": zxr10ExtendedACLPermitDeny,
       "zxr10ExtendedACLSrcAddr": zxr10ExtendedACLSrcAddr,
       "zxr10ExtendedACLSrcWildcard": zxr10ExtendedACLSrcWildcard,
       "zxr10ExtendedACLSrcAny": zxr10ExtendedACLSrcAny,
       "zxr10ExtendedACLDestAddr": zxr10ExtendedACLDestAddr,
       "zxr10ExtendedACLDestWildcard": zxr10ExtendedACLDestWildcard,
       "zxr10ExtendedACLDestAny": zxr10ExtendedACLDestAny,
       "zxr10ExtendedACLProtocol": zxr10ExtendedACLProtocol,
       "zxr10ExtendedACLSrcOpr": zxr10ExtendedACLSrcOpr,
       "zxr10ExtendedACLSrcPort": zxr10ExtendedACLSrcPort,
       "zxr10ExtendedACLSrcPort2": zxr10ExtendedACLSrcPort2,
       "zxr10ExtendedACLDestOpr": zxr10ExtendedACLDestOpr,
       "zxr10ExtendedACLDestPort": zxr10ExtendedACLDestPort,
       "zxr10ExtendedACLDestPort2": zxr10ExtendedACLDestPort2,
       "zxr10ExtendedACLTCPEstablish": zxr10ExtendedACLTCPEstablish,
       "zxr10ExtendedACLTCPControl": zxr10ExtendedACLTCPControl,
       "zxr10ExtendedACLICMPType": zxr10ExtendedACLICMPType,
       "zxr10ExtendedACLICMPCode": zxr10ExtendedACLICMPCode,
       "zxr10ExtendedACLPrecedence": zxr10ExtendedACLPrecedence,
       "zxr10ExtendedACLTOS": zxr10ExtendedACLTOS,
       "zxr10ExtendedACLDSCP": zxr10ExtendedACLDSCP,
       "zxr10ExtendedACLFlag": zxr10ExtendedACLFlag,
       "zxr10ExtendedACLTimeRangeName": zxr10ExtendedACLTimeRangeName,
       "zxr10ExtendedACLRuleDescription": zxr10ExtendedACLRuleDescription,
       "zxr10ExtendedACLRowStatus": zxr10ExtendedACLRowStatus,
       "zxr10LinkACLTable": zxr10LinkACLTable,
       "zxr10LinkACLEntry": zxr10LinkACLEntry,
       "zxr10LinkACLNo": zxr10LinkACLNo,
       "zxr10LinkACLName": zxr10LinkACLName,
       "zxr10LinkACLAlias": zxr10LinkACLAlias,
       "zxr10LinkACLMatchorder": zxr10LinkACLMatchorder,
       "zxr10LinkACLRuleID": zxr10LinkACLRuleID,
       "zxr10LinkACLPermitDeny": zxr10LinkACLPermitDeny,
       "zxr10LinkACLProtocol": zxr10LinkACLProtocol,
       "zxr10LinkACLCos": zxr10LinkACLCos,
       "zxr10LinkACLIncos": zxr10LinkACLIncos,
       "zxr10LinkACLDinVlanID": zxr10LinkACLDinVlanID,
       "zxr10LinkACLDinVlanIDRight": zxr10LinkACLDinVlanIDRight,
       "zxr10LinkACLDoutVlanID": zxr10LinkACLDoutVlanID,
       "zxr10LinkACLDoutVlanIDRight": zxr10LinkACLDoutVlanIDRight,
       "zxr10LinkACLInMAC": zxr10LinkACLInMAC,
       "zxr10LinkACLInMACWildcard": zxr10LinkACLInMACWildcard,
       "zxr10LinkACLInMACAny": zxr10LinkACLInMACAny,
       "zxr10LinkACLOutMAC": zxr10LinkACLOutMAC,
       "zxr10LinkACLOutMACWildCard": zxr10LinkACLOutMACWildCard,
       "zxr10LinkACLOutMACAny": zxr10LinkACLOutMACAny,
       "zxr10LinkACLFlag": zxr10LinkACLFlag,
       "zxr10LinkACLTimeRangeName": zxr10LinkACLTimeRangeName,
       "zxr10LinkACLRuleDescription": zxr10LinkACLRuleDescription,
       "zxr10LinkACLRowStatus": zxr10LinkACLRowStatus,
       "zxr10HybridACLTable": zxr10HybridACLTable,
       "zxr10HybridACLEntry": zxr10HybridACLEntry,
       "zxr10HybridACLNo": zxr10HybridACLNo,
       "zxr10HybridACLName": zxr10HybridACLName,
       "zxr10HybridACLAlias": zxr10HybridACLAlias,
       "zxr10HybridACLMatchorder": zxr10HybridACLMatchorder,
       "zxr10HybridACLRuleID": zxr10HybridACLRuleID,
       "zxr10HybridACLPermitDeny": zxr10HybridACLPermitDeny,
       "zxr10HybridACLProtocol": zxr10HybridACLProtocol,
       "zxr10HybridACLSrcAddr": zxr10HybridACLSrcAddr,
       "zxr10HybridACLSrcAddrWildcard": zxr10HybridACLSrcAddrWildcard,
       "zxr10HybridACLSrcAny": zxr10HybridACLSrcAny,
       "zxr10HybridACLDestAddr": zxr10HybridACLDestAddr,
       "zxr10HybridACLDestAddrWildcard": zxr10HybridACLDestAddrWildcard,
       "zxr10HybridACLDestAny": zxr10HybridACLDestAny,
       "zxr10HybridACLSrcOpr": zxr10HybridACLSrcOpr,
       "zxr10HybridACLSrcPort": zxr10HybridACLSrcPort,
       "zxr10HybridACLDestOpr": zxr10HybridACLDestOpr,
       "zxr10HybridACLDestPort": zxr10HybridACLDestPort,
       "zxr10HybridACLTCPControl": zxr10HybridACLTCPControl,
       "zxr10HybridACLTOS": zxr10HybridACLTOS,
       "zxr10HybridACLPrecedence": zxr10HybridACLPrecedence,
       "zxr10HybridACLDSCP": zxr10HybridACLDSCP,
       "zxr10HybridACLIPNumber": zxr10HybridACLIPNumber,
       "zxr10HybridACLCos": zxr10HybridACLCos,
       "zxr10HybridACLIncos": zxr10HybridACLIncos,
       "zxr10HybridACLDinVlanID": zxr10HybridACLDinVlanID,
       "zxr10HybridACLDoutVlanID": zxr10HybridACLDoutVlanID,
       "zxr10HybridACLInMAC": zxr10HybridACLInMAC,
       "zxr10HybridACLInMACWildcard": zxr10HybridACLInMACWildcard,
       "zxr10HybridACLInMACAny": zxr10HybridACLInMACAny,
       "zxr10HybridACLOutMAC": zxr10HybridACLOutMAC,
       "zxr10HybridACLOutMACWildcard": zxr10HybridACLOutMACWildcard,
       "zxr10HybridACLOutMACAny": zxr10HybridACLOutMACAny,
       "zxr10HybridACLFlag": zxr10HybridACLFlag,
       "zxr10HybridACLTimeRangeName": zxr10HybridACLTimeRangeName,
       "zxr10HybridACLRuleDescription": zxr10HybridACLRuleDescription,
       "zxr10HybridACLRowStatus": zxr10HybridACLRowStatus,
       "zxr10ACLBoundIfTable": zxr10ACLBoundIfTable,
       "zxr10ACLBoundIfEntry": zxr10ACLBoundIfEntry,
       "zxr10ACLBoundIf": zxr10ACLBoundIf,
       "zxr10ACLNo": zxr10ACLNo,
       "zxr10ACLName": zxr10ACLName,
       "zxr10ACLBoundIfDirection": zxr10ACLBoundIfDirection,
       "zxr10ACLRowStatus": zxr10ACLRowStatus}
)
