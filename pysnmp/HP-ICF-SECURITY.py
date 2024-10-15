# SNMP MIB module (HP-ICF-SECURITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-SECURITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:07 2024
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

(hpicfObjectModules,
 icfSecurity) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpicfObjectModules",
    "icfSecurity")

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


# MODULE-IDENTITY

icfSecurityMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 1)
)
icfSecurityMib.setRevisions(
        ("2008-03-05 09:00",
         "2007-10-01 09:03",
         "2003-01-09 01:12",
         "2000-11-03 07:56",
         "1996-09-10 02:00",
         "1996-01-25 03:56",
         "1993-07-09 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _IcfSecurPassword_Type(DisplayString):
    """Custom type icfSecurPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_IcfSecurPassword_Type.__name__ = "DisplayString"
_IcfSecurPassword_Object = MibScalar
icfSecurPassword = _IcfSecurPassword_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 1),
    _IcfSecurPassword_Type()
)
icfSecurPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icfSecurPassword.setStatus("deprecated")


class _IcfSecurAuthAnyMgr_Type(Integer32):
    """Custom type icfSecurAuthAnyMgr based on Integer32"""
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


_IcfSecurAuthAnyMgr_Type.__name__ = "Integer32"
_IcfSecurAuthAnyMgr_Object = MibScalar
icfSecurAuthAnyMgr = _IcfSecurAuthAnyMgr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 2),
    _IcfSecurAuthAnyMgr_Type()
)
icfSecurAuthAnyMgr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icfSecurAuthAnyMgr.setStatus("deprecated")
_IcfSecurAuthMgrTable_Object = MibTable
icfSecurAuthMgrTable = _IcfSecurAuthMgrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 3)
)
if mibBuilder.loadTexts:
    icfSecurAuthMgrTable.setStatus("deprecated")
_IcfSecurAuthMgrEntry_Object = MibTableRow
icfSecurAuthMgrEntry = _IcfSecurAuthMgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 3, 1)
)
icfSecurAuthMgrEntry.setIndexNames(
    (0, "HP-ICF-SECURITY", "icfAuthMgrIndex"),
)
if mibBuilder.loadTexts:
    icfSecurAuthMgrEntry.setStatus("deprecated")


class _IcfAuthMgrIndex_Type(Integer32):
    """Custom type icfAuthMgrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_IcfAuthMgrIndex_Type.__name__ = "Integer32"
_IcfAuthMgrIndex_Object = MibTableColumn
icfAuthMgrIndex = _IcfAuthMgrIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 3, 1, 1),
    _IcfAuthMgrIndex_Type()
)
icfAuthMgrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfAuthMgrIndex.setStatus("deprecated")
_IcfAuthMgrIpAddress_Type = IpAddress
_IcfAuthMgrIpAddress_Object = MibTableColumn
icfAuthMgrIpAddress = _IcfAuthMgrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 3, 1, 2),
    _IcfAuthMgrIpAddress_Type()
)
icfAuthMgrIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icfAuthMgrIpAddress.setStatus("deprecated")


class _IcfAuthMgrIpxAddress_Type(OctetString):
    """Custom type icfAuthMgrIpxAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_IcfAuthMgrIpxAddress_Type.__name__ = "OctetString"
_IcfAuthMgrIpxAddress_Object = MibTableColumn
icfAuthMgrIpxAddress = _IcfAuthMgrIpxAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 3, 1, 3),
    _IcfAuthMgrIpxAddress_Type()
)
icfAuthMgrIpxAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icfAuthMgrIpxAddress.setStatus("deprecated")


class _IcfAuthMgrRcvTraps_Type(Integer32):
    """Custom type icfAuthMgrRcvTraps based on Integer32"""
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


_IcfAuthMgrRcvTraps_Type.__name__ = "Integer32"
_IcfAuthMgrRcvTraps_Object = MibTableColumn
icfAuthMgrRcvTraps = _IcfAuthMgrRcvTraps_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 3, 1, 4),
    _IcfAuthMgrRcvTraps_Type()
)
icfAuthMgrRcvTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icfAuthMgrRcvTraps.setStatus("deprecated")
_IcfSecurIntruder_ObjectIdentity = ObjectIdentity
icfSecurIntruder = _IcfSecurIntruder_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 4)
)


class _IcfSecurIntruderFlag_Type(Integer32):
    """Custom type icfSecurIntruderFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_IcfSecurIntruderFlag_Type.__name__ = "Integer32"
_IcfSecurIntruderFlag_Object = MibScalar
icfSecurIntruderFlag = _IcfSecurIntruderFlag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 4, 1),
    _IcfSecurIntruderFlag_Type()
)
icfSecurIntruderFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icfSecurIntruderFlag.setStatus("current")
_IcfSecurIntruderIpAddress_Type = IpAddress
_IcfSecurIntruderIpAddress_Object = MibScalar
icfSecurIntruderIpAddress = _IcfSecurIntruderIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 4, 2),
    _IcfSecurIntruderIpAddress_Type()
)
icfSecurIntruderIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfSecurIntruderIpAddress.setStatus("current")


class _IcfSecurIntruderIpxAddress_Type(OctetString):
    """Custom type icfSecurIntruderIpxAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_IcfSecurIntruderIpxAddress_Type.__name__ = "OctetString"
_IcfSecurIntruderIpxAddress_Object = MibScalar
icfSecurIntruderIpxAddress = _IcfSecurIntruderIpxAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 4, 3),
    _IcfSecurIntruderIpxAddress_Type()
)
icfSecurIntruderIpxAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfSecurIntruderIpxAddress.setStatus("current")
_IcfSecurIntruderTime_Type = TimeTicks
_IcfSecurIntruderTime_Object = MibScalar
icfSecurIntruderTime = _IcfSecurIntruderTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 4, 4),
    _IcfSecurIntruderTime_Type()
)
icfSecurIntruderTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfSecurIntruderTime.setStatus("current")
_IcfCommunityTable_Object = MibTable
icfCommunityTable = _IcfCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 5)
)
if mibBuilder.loadTexts:
    icfCommunityTable.setStatus("deprecated")
_IcfCommunityEntry_Object = MibTableRow
icfCommunityEntry = _IcfCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 5, 1)
)
icfCommunityEntry.setIndexNames(
    (0, "HP-ICF-SECURITY", "icfCommunityIndex"),
)
if mibBuilder.loadTexts:
    icfCommunityEntry.setStatus("deprecated")


class _IcfCommunityIndex_Type(Integer32):
    """Custom type icfCommunityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IcfCommunityIndex_Type.__name__ = "Integer32"
_IcfCommunityIndex_Object = MibTableColumn
icfCommunityIndex = _IcfCommunityIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 5, 1, 1),
    _IcfCommunityIndex_Type()
)
icfCommunityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icfCommunityIndex.setStatus("deprecated")


class _IcfCommunityName_Type(OctetString):
    """Custom type icfCommunityName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IcfCommunityName_Type.__name__ = "OctetString"
_IcfCommunityName_Object = MibTableColumn
icfCommunityName = _IcfCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 5, 1, 2),
    _IcfCommunityName_Type()
)
icfCommunityName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    icfCommunityName.setStatus("deprecated")


class _IcfCommunityReadView_Type(Integer32):
    """Custom type icfCommunityReadView based on Integer32"""
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
        *(("discovery", 2),
          ("none", 1),
          ("restricted", 3),
          ("root", 5),
          ("user", 4))
    )


_IcfCommunityReadView_Type.__name__ = "Integer32"
_IcfCommunityReadView_Object = MibTableColumn
icfCommunityReadView = _IcfCommunityReadView_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 5, 1, 3),
    _IcfCommunityReadView_Type()
)
icfCommunityReadView.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    icfCommunityReadView.setStatus("deprecated")


class _IcfCommunityWriteView_Type(Integer32):
    """Custom type icfCommunityWriteView based on Integer32"""
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
        *(("discovery", 2),
          ("none", 1),
          ("restricted", 3),
          ("root", 5),
          ("user", 4))
    )


_IcfCommunityWriteView_Type.__name__ = "Integer32"
_IcfCommunityWriteView_Object = MibTableColumn
icfCommunityWriteView = _IcfCommunityWriteView_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 5, 1, 4),
    _IcfCommunityWriteView_Type()
)
icfCommunityWriteView.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    icfCommunityWriteView.setStatus("deprecated")
_IcfCommunityStatus_Type = RowStatus
_IcfCommunityStatus_Object = MibTableColumn
icfCommunityStatus = _IcfCommunityStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 5, 1, 5),
    _IcfCommunityStatus_Type()
)
icfCommunityStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    icfCommunityStatus.setStatus("deprecated")
_IcfAuthMgrTable_Object = MibTable
icfAuthMgrTable = _IcfAuthMgrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 6)
)
if mibBuilder.loadTexts:
    icfAuthMgrTable.setStatus("deprecated")
_IcfAuthMgrEntry_Object = MibTableRow
icfAuthMgrEntry = _IcfAuthMgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 6, 1)
)
icfAuthMgrEntry.setIndexNames(
    (0, "HP-ICF-SECURITY", "icfCommunityIndex"),
    (0, "HP-ICF-SECURITY", "icfAuthMgrSubIndex"),
)
if mibBuilder.loadTexts:
    icfAuthMgrEntry.setStatus("deprecated")


class _IcfAuthMgrSubIndex_Type(Integer32):
    """Custom type icfAuthMgrSubIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IcfAuthMgrSubIndex_Type.__name__ = "Integer32"
_IcfAuthMgrSubIndex_Object = MibTableColumn
icfAuthMgrSubIndex = _IcfAuthMgrSubIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 6, 1, 1),
    _IcfAuthMgrSubIndex_Type()
)
icfAuthMgrSubIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icfAuthMgrSubIndex.setStatus("deprecated")


class _IcfAuthMgrAddrType_Type(Integer32):
    """Custom type icfAuthMgrAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("ipx", 2))
    )


_IcfAuthMgrAddrType_Type.__name__ = "Integer32"
_IcfAuthMgrAddrType_Object = MibTableColumn
icfAuthMgrAddrType = _IcfAuthMgrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 6, 1, 2),
    _IcfAuthMgrAddrType_Type()
)
icfAuthMgrAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    icfAuthMgrAddrType.setStatus("deprecated")


class _IcfAuthMgrAddress_Type(OctetString):
    """Custom type icfAuthMgrAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(10, 10),
    )


_IcfAuthMgrAddress_Type.__name__ = "OctetString"
_IcfAuthMgrAddress_Object = MibTableColumn
icfAuthMgrAddress = _IcfAuthMgrAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 6, 1, 3),
    _IcfAuthMgrAddress_Type()
)
icfAuthMgrAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    icfAuthMgrAddress.setStatus("deprecated")


class _IcfAuthMgrMask_Type(OctetString):
    """Custom type icfAuthMgrMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(10, 10),
    )


_IcfAuthMgrMask_Type.__name__ = "OctetString"
_IcfAuthMgrMask_Object = MibTableColumn
icfAuthMgrMask = _IcfAuthMgrMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 6, 1, 4),
    _IcfAuthMgrMask_Type()
)
icfAuthMgrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    icfAuthMgrMask.setStatus("deprecated")
_IcfAuthMgrStatus_Type = RowStatus
_IcfAuthMgrStatus_Object = MibTableColumn
icfAuthMgrStatus = _IcfAuthMgrStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 6, 1, 5),
    _IcfAuthMgrStatus_Type()
)
icfAuthMgrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    icfAuthMgrStatus.setStatus("deprecated")
_IcfAuthIPMgrTable_Object = MibTable
icfAuthIPMgrTable = _IcfAuthIPMgrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 7)
)
if mibBuilder.loadTexts:
    icfAuthIPMgrTable.setStatus("current")
_IcfAuthIPMgrEntry_Object = MibTableRow
icfAuthIPMgrEntry = _IcfAuthIPMgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 7, 1)
)
icfAuthIPMgrEntry.setIndexNames(
    (0, "HP-ICF-SECURITY", "icfAuthIPMgrIndex"),
)
if mibBuilder.loadTexts:
    icfAuthIPMgrEntry.setStatus("current")


class _IcfAuthIPMgrIndex_Type(Integer32):
    """Custom type icfAuthIPMgrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IcfAuthIPMgrIndex_Type.__name__ = "Integer32"
_IcfAuthIPMgrIndex_Object = MibTableColumn
icfAuthIPMgrIndex = _IcfAuthIPMgrIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 7, 1, 1),
    _IcfAuthIPMgrIndex_Type()
)
icfAuthIPMgrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icfAuthIPMgrIndex.setStatus("current")
_IcfAuthIPMgrAddress_Type = IpAddress
_IcfAuthIPMgrAddress_Object = MibTableColumn
icfAuthIPMgrAddress = _IcfAuthIPMgrAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 7, 1, 2),
    _IcfAuthIPMgrAddress_Type()
)
icfAuthIPMgrAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    icfAuthIPMgrAddress.setStatus("deprecated")
_IcfAuthIPMgrMask_Type = IpAddress
_IcfAuthIPMgrMask_Object = MibTableColumn
icfAuthIPMgrMask = _IcfAuthIPMgrMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 7, 1, 3),
    _IcfAuthIPMgrMask_Type()
)
icfAuthIPMgrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    icfAuthIPMgrMask.setStatus("deprecated")


class _IcfAuthIPMgrAccess_Type(Integer32):
    """Custom type icfAuthIPMgrAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manager", 2),
          ("operator", 1))
    )


_IcfAuthIPMgrAccess_Type.__name__ = "Integer32"
_IcfAuthIPMgrAccess_Object = MibTableColumn
icfAuthIPMgrAccess = _IcfAuthIPMgrAccess_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 7, 1, 4),
    _IcfAuthIPMgrAccess_Type()
)
icfAuthIPMgrAccess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    icfAuthIPMgrAccess.setStatus("current")
_IcfAuthIPMgrStatus_Type = RowStatus
_IcfAuthIPMgrStatus_Object = MibTableColumn
icfAuthIPMgrStatus = _IcfAuthIPMgrStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 7, 1, 5),
    _IcfAuthIPMgrStatus_Type()
)
icfAuthIPMgrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    icfAuthIPMgrStatus.setStatus("current")
_IcfAuthIPMgrInetAddrType_Type = InetAddressType
_IcfAuthIPMgrInetAddrType_Object = MibTableColumn
icfAuthIPMgrInetAddrType = _IcfAuthIPMgrInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 7, 1, 6),
    _IcfAuthIPMgrInetAddrType_Type()
)
icfAuthIPMgrInetAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    icfAuthIPMgrInetAddrType.setStatus("current")
_IcfAuthIPMgrInetAddress_Type = InetAddress
_IcfAuthIPMgrInetAddress_Object = MibTableColumn
icfAuthIPMgrInetAddress = _IcfAuthIPMgrInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 7, 1, 7),
    _IcfAuthIPMgrInetAddress_Type()
)
icfAuthIPMgrInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    icfAuthIPMgrInetAddress.setStatus("current")
_IcfAuthIPMgrInetAddrMaskType_Type = InetAddressType
_IcfAuthIPMgrInetAddrMaskType_Object = MibTableColumn
icfAuthIPMgrInetAddrMaskType = _IcfAuthIPMgrInetAddrMaskType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 7, 1, 8),
    _IcfAuthIPMgrInetAddrMaskType_Type()
)
icfAuthIPMgrInetAddrMaskType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    icfAuthIPMgrInetAddrMaskType.setStatus("current")
_IcfAuthIPMgrInetAddrMask_Type = InetAddress
_IcfAuthIPMgrInetAddrMask_Object = MibTableColumn
icfAuthIPMgrInetAddrMask = _IcfAuthIPMgrInetAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 7, 1, 9),
    _IcfAuthIPMgrInetAddrMask_Type()
)
icfAuthIPMgrInetAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    icfAuthIPMgrInetAddrMask.setStatus("current")


class _IcfAuthIPMgrAccessMethod_Type(Integer32):
    """Custom type icfAuthIPMgrAccessMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("snmp", 5),
          ("ssh", 2),
          ("telnet", 3),
          ("tftp", 6),
          ("web", 4))
    )


_IcfAuthIPMgrAccessMethod_Type.__name__ = "Integer32"
_IcfAuthIPMgrAccessMethod_Object = MibTableColumn
icfAuthIPMgrAccessMethod = _IcfAuthIPMgrAccessMethod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 7, 1, 10),
    _IcfAuthIPMgrAccessMethod_Type()
)
icfAuthIPMgrAccessMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    icfAuthIPMgrAccessMethod.setStatus("current")
_IcfSecurityConformance_ObjectIdentity = ObjectIdentity
icfSecurityConformance = _IcfSecurityConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 1, 1)
)
_IcfSecurityCompliances_ObjectIdentity = ObjectIdentity
icfSecurityCompliances = _IcfSecurityCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 1, 1, 1)
)
_IcfSecurityGroups_ObjectIdentity = ObjectIdentity
icfSecurityGroups = _IcfSecurityGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 1, 1, 2)
)

# Managed Objects groups

icfSnmpSecurityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 1, 1, 2, 1)
)
icfSnmpSecurityGroup.setObjects(
      *(("HP-ICF-SECURITY", "icfSecurPassword"),
        ("HP-ICF-SECURITY", "icfSecurAuthAnyMgr"),
        ("HP-ICF-SECURITY", "icfAuthMgrIndex"),
        ("HP-ICF-SECURITY", "icfAuthMgrIpAddress"),
        ("HP-ICF-SECURITY", "icfAuthMgrIpxAddress"),
        ("HP-ICF-SECURITY", "icfAuthMgrRcvTraps"))
)
if mibBuilder.loadTexts:
    icfSnmpSecurityGroup.setStatus("obsolete")

icfSecIntruderGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 1, 1, 2, 2)
)
icfSecIntruderGroup.setObjects(
      *(("HP-ICF-SECURITY", "icfSecurIntruderFlag"),
        ("HP-ICF-SECURITY", "icfSecurIntruderIpAddress"),
        ("HP-ICF-SECURITY", "icfSecurIntruderIpxAddress"),
        ("HP-ICF-SECURITY", "icfSecurIntruderTime"))
)
if mibBuilder.loadTexts:
    icfSecIntruderGroup.setStatus("current")

icfV1CommunityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 1, 1, 2, 13)
)
icfV1CommunityGroup.setObjects(
      *(("HP-ICF-SECURITY", "icfCommunityName"),
        ("HP-ICF-SECURITY", "icfCommunityReadView"),
        ("HP-ICF-SECURITY", "icfCommunityWriteView"),
        ("HP-ICF-SECURITY", "icfCommunityStatus"),
        ("HP-ICF-SECURITY", "icfAuthMgrAddrType"),
        ("HP-ICF-SECURITY", "icfAuthMgrAddress"),
        ("HP-ICF-SECURITY", "icfAuthMgrMask"),
        ("HP-ICF-SECURITY", "icfAuthMgrStatus"))
)
if mibBuilder.loadTexts:
    icfV1CommunityGroup.setStatus("deprecated")

icfAuthIPMgrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 1, 1, 2, 14)
)
icfAuthIPMgrGroup.setObjects(
      *(("HP-ICF-SECURITY", "icfAuthIPMgrAddress"),
        ("HP-ICF-SECURITY", "icfAuthIPMgrMask"),
        ("HP-ICF-SECURITY", "icfAuthIPMgrAccess"),
        ("HP-ICF-SECURITY", "icfAuthIPMgrStatus"))
)
if mibBuilder.loadTexts:
    icfAuthIPMgrGroup.setStatus("deprecated")

icfAuthIPMgrInetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 1, 1, 2, 15)
)
icfAuthIPMgrInetGroup.setObjects(
      *(("HP-ICF-SECURITY", "icfAuthIPMgrInetAddrType"),
        ("HP-ICF-SECURITY", "icfAuthIPMgrInetAddress"),
        ("HP-ICF-SECURITY", "icfAuthIPMgrInetAddrMaskType"),
        ("HP-ICF-SECURITY", "icfAuthIPMgrInetAddrMask"),
        ("HP-ICF-SECURITY", "icfAuthIPMgrAccessMethod"))
)
if mibBuilder.loadTexts:
    icfAuthIPMgrInetGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

icfSecurCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    icfSecurCompliance.setStatus(
        "obsolete"
    )

icfV1CommunityCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    icfV1CommunityCompliance.setStatus(
        "deprecated"
    )

icfAuthIPMgrCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    icfAuthIPMgrCompliance.setStatus(
        "deprecated"
    )

icfAuthIPMgrCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    icfAuthIPMgrCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-SECURITY",
    **{"icfSecurPassword": icfSecurPassword,
       "icfSecurAuthAnyMgr": icfSecurAuthAnyMgr,
       "icfSecurAuthMgrTable": icfSecurAuthMgrTable,
       "icfSecurAuthMgrEntry": icfSecurAuthMgrEntry,
       "icfAuthMgrIndex": icfAuthMgrIndex,
       "icfAuthMgrIpAddress": icfAuthMgrIpAddress,
       "icfAuthMgrIpxAddress": icfAuthMgrIpxAddress,
       "icfAuthMgrRcvTraps": icfAuthMgrRcvTraps,
       "icfSecurIntruder": icfSecurIntruder,
       "icfSecurIntruderFlag": icfSecurIntruderFlag,
       "icfSecurIntruderIpAddress": icfSecurIntruderIpAddress,
       "icfSecurIntruderIpxAddress": icfSecurIntruderIpxAddress,
       "icfSecurIntruderTime": icfSecurIntruderTime,
       "icfCommunityTable": icfCommunityTable,
       "icfCommunityEntry": icfCommunityEntry,
       "icfCommunityIndex": icfCommunityIndex,
       "icfCommunityName": icfCommunityName,
       "icfCommunityReadView": icfCommunityReadView,
       "icfCommunityWriteView": icfCommunityWriteView,
       "icfCommunityStatus": icfCommunityStatus,
       "icfAuthMgrTable": icfAuthMgrTable,
       "icfAuthMgrEntry": icfAuthMgrEntry,
       "icfAuthMgrSubIndex": icfAuthMgrSubIndex,
       "icfAuthMgrAddrType": icfAuthMgrAddrType,
       "icfAuthMgrAddress": icfAuthMgrAddress,
       "icfAuthMgrMask": icfAuthMgrMask,
       "icfAuthMgrStatus": icfAuthMgrStatus,
       "icfAuthIPMgrTable": icfAuthIPMgrTable,
       "icfAuthIPMgrEntry": icfAuthIPMgrEntry,
       "icfAuthIPMgrIndex": icfAuthIPMgrIndex,
       "icfAuthIPMgrAddress": icfAuthIPMgrAddress,
       "icfAuthIPMgrMask": icfAuthIPMgrMask,
       "icfAuthIPMgrAccess": icfAuthIPMgrAccess,
       "icfAuthIPMgrStatus": icfAuthIPMgrStatus,
       "icfAuthIPMgrInetAddrType": icfAuthIPMgrInetAddrType,
       "icfAuthIPMgrInetAddress": icfAuthIPMgrInetAddress,
       "icfAuthIPMgrInetAddrMaskType": icfAuthIPMgrInetAddrMaskType,
       "icfAuthIPMgrInetAddrMask": icfAuthIPMgrInetAddrMask,
       "icfAuthIPMgrAccessMethod": icfAuthIPMgrAccessMethod,
       "icfSecurityMib": icfSecurityMib,
       "icfSecurityConformance": icfSecurityConformance,
       "icfSecurityCompliances": icfSecurityCompliances,
       "icfSecurCompliance": icfSecurCompliance,
       "icfV1CommunityCompliance": icfV1CommunityCompliance,
       "icfAuthIPMgrCompliance": icfAuthIPMgrCompliance,
       "icfAuthIPMgrCompliance1": icfAuthIPMgrCompliance1,
       "icfSecurityGroups": icfSecurityGroups,
       "icfSnmpSecurityGroup": icfSnmpSecurityGroup,
       "icfSecIntruderGroup": icfSecIntruderGroup,
       "icfV1CommunityGroup": icfV1CommunityGroup,
       "icfAuthIPMgrGroup": icfAuthIPMgrGroup,
       "icfAuthIPMgrInetGroup": icfAuthIPMgrInetGroup}
)
