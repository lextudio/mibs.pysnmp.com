# SNMP MIB module (NMS-IPAcl) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NMS-IPAcl
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:58 2024
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

(nmslocal,) = mibBuilder.importSymbols(
    "NMS-SMI",
    "nmslocal")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

nmsIPAclMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NmsAclTotal_Type = Integer32
_NmsAclTotal_Object = MibScalar
nmsAclTotal = _NmsAclTotal_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 1),
    _NmsAclTotal_Type()
)
nmsAclTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsAclTotal.setStatus("mandatory")
_NmsIPAclTable_Object = MibTable
nmsIPAclTable = _NmsIPAclTable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 2)
)
if mibBuilder.loadTexts:
    nmsIPAclTable.setStatus("mandatory")
_NmsIPAclEntry_Object = MibTableRow
nmsIPAclEntry = _NmsIPAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 2, 1)
)
nmsIPAclEntry.setIndexNames(
    (0, "NMS-IPAcl", "nmsIPAclname"),
)
if mibBuilder.loadTexts:
    nmsIPAclEntry.setStatus("mandatory")
_NmsIPAclname_Type = DisplayString
_NmsIPAclname_Object = MibTableColumn
nmsIPAclname = _NmsIPAclname_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 2, 1, 1),
    _NmsIPAclname_Type()
)
nmsIPAclname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsIPAclname.setStatus("mandatory")
_NmsIPAclEntrytotal_Type = Integer32
_NmsIPAclEntrytotal_Object = MibTableColumn
nmsIPAclEntrytotal = _NmsIPAclEntrytotal_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 2, 1, 2),
    _NmsIPAclEntrytotal_Type()
)
nmsIPAclEntrytotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsIPAclEntrytotal.setStatus("mandatory")


class _NmsIPAclType_Type(Integer32):
    """Custom type nmsIPAclType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("extended", 0),
          ("standard", 1))
    )


_NmsIPAclType_Type.__name__ = "Integer32"
_NmsIPAclType_Object = MibTableColumn
nmsIPAclType = _NmsIPAclType_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 2, 1, 3),
    _NmsIPAclType_Type()
)
nmsIPAclType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAclType.setStatus("mandatory")


class _NmsIPAclMergeEnable_Type(Integer32):
    """Custom type nmsIPAclMergeEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_NmsIPAclMergeEnable_Type.__name__ = "Integer32"
_NmsIPAclMergeEnable_Object = MibTableColumn
nmsIPAclMergeEnable = _NmsIPAclMergeEnable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 2, 1, 4),
    _NmsIPAclMergeEnable_Type()
)
nmsIPAclMergeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAclMergeEnable.setStatus("mandatory")
_NmsIPAclRowStatus_Type = RowStatus
_NmsIPAclRowStatus_Object = MibTableColumn
nmsIPAclRowStatus = _NmsIPAclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 2, 1, 5),
    _NmsIPAclRowStatus_Type()
)
nmsIPAclRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAclRowStatus.setStatus("mandatory")
_NmsIPAclsRuleTable_Object = MibTable
nmsIPAclsRuleTable = _NmsIPAclsRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 3)
)
if mibBuilder.loadTexts:
    nmsIPAclsRuleTable.setStatus("mandatory")
_NmsIPAclsRuleEntry_Object = MibTableRow
nmsIPAclsRuleEntry = _NmsIPAclsRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 3, 1)
)
nmsIPAclsRuleEntry.setIndexNames(
    (0, "NMS-IPAcl", "nmsIPAclsname"),
    (0, "NMS-IPAcl", "nmsIPAclsentryId"),
)
if mibBuilder.loadTexts:
    nmsIPAclsRuleEntry.setStatus("mandatory")
_NmsIPAclsname_Type = DisplayString
_NmsIPAclsname_Object = MibTableColumn
nmsIPAclsname = _NmsIPAclsname_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 3, 1, 1),
    _NmsIPAclsname_Type()
)
nmsIPAclsname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsIPAclsname.setStatus("current")
_NmsIPAclsentryId_Type = Integer32
_NmsIPAclsentryId_Object = MibTableColumn
nmsIPAclsentryId = _NmsIPAclsentryId_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 3, 1, 2),
    _NmsIPAclsentryId_Type()
)
nmsIPAclsentryId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAclsentryId.setStatus("current")


class _NmsIPAclsrule_Type(Integer32):
    """Custom type nmsIPAclsrule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 0),
          ("permit", 1))
    )


_NmsIPAclsrule_Type.__name__ = "Integer32"
_NmsIPAclsrule_Object = MibTableColumn
nmsIPAclsrule = _NmsIPAclsrule_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 3, 1, 3),
    _NmsIPAclsrule_Type()
)
nmsIPAclsrule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAclsrule.setStatus("mandatory")
_NmsIPAclssrcip_Type = IpAddress
_NmsIPAclssrcip_Object = MibTableColumn
nmsIPAclssrcip = _NmsIPAclssrcip_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 3, 1, 4),
    _NmsIPAclssrcip_Type()
)
nmsIPAclssrcip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAclssrcip.setStatus("current")
_NmsIPAclssrcmask_Type = IpAddress
_NmsIPAclssrcmask_Object = MibTableColumn
nmsIPAclssrcmask = _NmsIPAclssrcmask_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 3, 1, 5),
    _NmsIPAclssrcmask_Type()
)
nmsIPAclssrcmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAclssrcmask.setStatus("current")
_NmsIPAclssrcbeginip_Type = IpAddress
_NmsIPAclssrcbeginip_Object = MibTableColumn
nmsIPAclssrcbeginip = _NmsIPAclssrcbeginip_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 3, 1, 6),
    _NmsIPAclssrcbeginip_Type()
)
nmsIPAclssrcbeginip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAclssrcbeginip.setStatus("current")
_NmsIPAclssrcendip_Type = IpAddress
_NmsIPAclssrcendip_Object = MibTableColumn
nmsIPAclssrcendip = _NmsIPAclssrcendip_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 3, 1, 7),
    _NmsIPAclssrcendip_Type()
)
nmsIPAclssrcendip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAclssrcendip.setStatus("current")


class _NmsIPAclscompare_Type(Integer32):
    """Custom type nmsIPAclscompare based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("usemask", 1),
          ("userange", 2))
    )


_NmsIPAclscompare_Type.__name__ = "Integer32"
_NmsIPAclscompare_Object = MibTableColumn
nmsIPAclscompare = _NmsIPAclscompare_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 3, 1, 8),
    _NmsIPAclscompare_Type()
)
nmsIPAclscompare.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAclscompare.setStatus("current")


class _NmsIPAclsany_Type(Integer32):
    """Custom type nmsIPAclsany based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("useany", 0),
          ("usezero", 1))
    )


_NmsIPAclsany_Type.__name__ = "Integer32"
_NmsIPAclsany_Object = MibTableColumn
nmsIPAclsany = _NmsIPAclsany_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 3, 1, 9),
    _NmsIPAclsany_Type()
)
nmsIPAclsany.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAclsany.setStatus("current")


class _NmsIPAclslog_Type(Integer32):
    """Custom type nmsIPAclslog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_NmsIPAclslog_Type.__name__ = "Integer32"
_NmsIPAclslog_Object = MibTableColumn
nmsIPAclslog = _NmsIPAclslog_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 3, 1, 10),
    _NmsIPAclslog_Type()
)
nmsIPAclslog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAclslog.setStatus("current")
_NmsIPAclsrowstatus_Type = RowStatus
_NmsIPAclsrowstatus_Object = MibTableColumn
nmsIPAclsrowstatus = _NmsIPAclsrowstatus_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 3, 1, 11),
    _NmsIPAclsrowstatus_Type()
)
nmsIPAclsrowstatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAclsrowstatus.setStatus("current")
_NmsIPAcleRuleTable_Object = MibTable
nmsIPAcleRuleTable = _NmsIPAcleRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4)
)
if mibBuilder.loadTexts:
    nmsIPAcleRuleTable.setStatus("mandatory")
_NmsIPAcleRuleEntry_Object = MibTableRow
nmsIPAcleRuleEntry = _NmsIPAcleRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1)
)
nmsIPAcleRuleEntry.setIndexNames(
    (0, "NMS-IPAcl", "nmsIPAclename"),
    (0, "NMS-IPAcl", "nmsIPAcleentryId"),
)
if mibBuilder.loadTexts:
    nmsIPAcleRuleEntry.setStatus("mandatory")
_NmsIPAclename_Type = DisplayString
_NmsIPAclename_Object = MibTableColumn
nmsIPAclename = _NmsIPAclename_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 1),
    _NmsIPAclename_Type()
)
nmsIPAclename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsIPAclename.setStatus("current")
_NmsIPAcleentryId_Type = Integer32
_NmsIPAcleentryId_Object = MibTableColumn
nmsIPAcleentryId = _NmsIPAcleentryId_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 2),
    _NmsIPAcleentryId_Type()
)
nmsIPAcleentryId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAcleentryId.setStatus("current")


class _NmsIPAclerule_Type(Integer32):
    """Custom type nmsIPAclerule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 0),
          ("permit", 1))
    )


_NmsIPAclerule_Type.__name__ = "Integer32"
_NmsIPAclerule_Object = MibTableColumn
nmsIPAclerule = _NmsIPAclerule_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 3),
    _NmsIPAclerule_Type()
)
nmsIPAclerule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAclerule.setStatus("mandatory")
_NmsIPAcleprotocol_Type = Integer32
_NmsIPAcleprotocol_Object = MibTableColumn
nmsIPAcleprotocol = _NmsIPAcleprotocol_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 4),
    _NmsIPAcleprotocol_Type()
)
nmsIPAcleprotocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAcleprotocol.setStatus("current")
_NmsIPAclesrceid_Type = Integer32
_NmsIPAclesrceid_Object = MibTableColumn
nmsIPAclesrceid = _NmsIPAclesrceid_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 5),
    _NmsIPAclesrceid_Type()
)
nmsIPAclesrceid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAclesrceid.setStatus("current")
_NmsIPAclesrcip_Type = IpAddress
_NmsIPAclesrcip_Object = MibTableColumn
nmsIPAclesrcip = _NmsIPAclesrcip_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 6),
    _NmsIPAclesrcip_Type()
)
nmsIPAclesrcip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAclesrcip.setStatus("current")
_NmsIPAclesrcmask_Type = IpAddress
_NmsIPAclesrcmask_Object = MibTableColumn
nmsIPAclesrcmask = _NmsIPAclesrcmask_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 7),
    _NmsIPAclesrcmask_Type()
)
nmsIPAclesrcmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAclesrcmask.setStatus("current")
_NmsIPAclesrcport_Type = Integer32
_NmsIPAclesrcport_Object = MibTableColumn
nmsIPAclesrcport = _NmsIPAclesrcport_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 8),
    _NmsIPAclesrcport_Type()
)
nmsIPAclesrcport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAclesrcport.setStatus("current")


class _NmsIPAclesrcpflag_Type(Integer32):
    """Custom type nmsIPAclesrcpflag based on Integer32"""
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
        *(("eq", 3),
          ("gt", 1),
          ("lt", 2),
          ("neq", 4),
          ("none", 0),
          ("range", 5))
    )


_NmsIPAclesrcpflag_Type.__name__ = "Integer32"
_NmsIPAclesrcpflag_Object = MibTableColumn
nmsIPAclesrcpflag = _NmsIPAclesrcpflag_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 9),
    _NmsIPAclesrcpflag_Type()
)
nmsIPAclesrcpflag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAclesrcpflag.setStatus("current")
_NmsIPAclesrcbeginip_Type = IpAddress
_NmsIPAclesrcbeginip_Object = MibTableColumn
nmsIPAclesrcbeginip = _NmsIPAclesrcbeginip_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 10),
    _NmsIPAclesrcbeginip_Type()
)
nmsIPAclesrcbeginip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAclesrcbeginip.setStatus("current")
_NmsIPAclesrcendip_Type = IpAddress
_NmsIPAclesrcendip_Object = MibTableColumn
nmsIPAclesrcendip = _NmsIPAclesrcendip_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 11),
    _NmsIPAclesrcendip_Type()
)
nmsIPAclesrcendip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAclesrcendip.setStatus("current")
_NmsIPAclesrcbeginport_Type = Integer32
_NmsIPAclesrcbeginport_Object = MibTableColumn
nmsIPAclesrcbeginport = _NmsIPAclesrcbeginport_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 12),
    _NmsIPAclesrcbeginport_Type()
)
nmsIPAclesrcbeginport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAclesrcbeginport.setStatus("current")
_NmsIPAclesrcendport_Type = Integer32
_NmsIPAclesrcendport_Object = MibTableColumn
nmsIPAclesrcendport = _NmsIPAclesrcendport_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 13),
    _NmsIPAclesrcendport_Type()
)
nmsIPAclesrcendport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAclesrcendport.setStatus("current")


class _NmsIPAclesrccompare_Type(Integer32):
    """Custom type nmsIPAclesrccompare based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("usemask", 1),
          ("userange", 2))
    )


_NmsIPAclesrccompare_Type.__name__ = "Integer32"
_NmsIPAclesrccompare_Object = MibTableColumn
nmsIPAclesrccompare = _NmsIPAclesrccompare_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 14),
    _NmsIPAclesrccompare_Type()
)
nmsIPAclesrccompare.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAclesrccompare.setStatus("current")


class _NmsIPAclesrcany_Type(Integer32):
    """Custom type nmsIPAclesrcany based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("useany", 0),
          ("usezero", 1))
    )


_NmsIPAclesrcany_Type.__name__ = "Integer32"
_NmsIPAclesrcany_Object = MibTableColumn
nmsIPAclesrcany = _NmsIPAclesrcany_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 15),
    _NmsIPAclesrcany_Type()
)
nmsIPAclesrcany.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAclesrcany.setStatus("current")
_NmsIPAcledeseid_Type = Integer32
_NmsIPAcledeseid_Object = MibTableColumn
nmsIPAcledeseid = _NmsIPAcledeseid_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 16),
    _NmsIPAcledeseid_Type()
)
nmsIPAcledeseid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAcledeseid.setStatus("current")
_NmsIPAcledesip_Type = IpAddress
_NmsIPAcledesip_Object = MibTableColumn
nmsIPAcledesip = _NmsIPAcledesip_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 17),
    _NmsIPAcledesip_Type()
)
nmsIPAcledesip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAcledesip.setStatus("current")
_NmsIPAcledesmask_Type = IpAddress
_NmsIPAcledesmask_Object = MibTableColumn
nmsIPAcledesmask = _NmsIPAcledesmask_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 18),
    _NmsIPAcledesmask_Type()
)
nmsIPAcledesmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAcledesmask.setStatus("current")
_NmsIPAcledesport_Type = Integer32
_NmsIPAcledesport_Object = MibTableColumn
nmsIPAcledesport = _NmsIPAcledesport_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 19),
    _NmsIPAcledesport_Type()
)
nmsIPAcledesport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAcledesport.setStatus("current")


class _NmsIPAcledespflag_Type(Integer32):
    """Custom type nmsIPAcledespflag based on Integer32"""
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
        *(("eq", 3),
          ("gt", 1),
          ("lt", 2),
          ("neq", 4),
          ("none", 0),
          ("range", 5))
    )


_NmsIPAcledespflag_Type.__name__ = "Integer32"
_NmsIPAcledespflag_Object = MibTableColumn
nmsIPAcledespflag = _NmsIPAcledespflag_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 20),
    _NmsIPAcledespflag_Type()
)
nmsIPAcledespflag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAcledespflag.setStatus("current")
_NmsIPAcledesbeginip_Type = IpAddress
_NmsIPAcledesbeginip_Object = MibTableColumn
nmsIPAcledesbeginip = _NmsIPAcledesbeginip_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 21),
    _NmsIPAcledesbeginip_Type()
)
nmsIPAcledesbeginip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAcledesbeginip.setStatus("current")
_NmsIPAcledesendip_Type = IpAddress
_NmsIPAcledesendip_Object = MibTableColumn
nmsIPAcledesendip = _NmsIPAcledesendip_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 22),
    _NmsIPAcledesendip_Type()
)
nmsIPAcledesendip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAcledesendip.setStatus("current")
_NmsIPAcledesbeginport_Type = Integer32
_NmsIPAcledesbeginport_Object = MibTableColumn
nmsIPAcledesbeginport = _NmsIPAcledesbeginport_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 23),
    _NmsIPAcledesbeginport_Type()
)
nmsIPAcledesbeginport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAcledesbeginport.setStatus("current")
_NmsIPAcledesendport_Type = Integer32
_NmsIPAcledesendport_Object = MibTableColumn
nmsIPAcledesendport = _NmsIPAcledesendport_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 24),
    _NmsIPAcledesendport_Type()
)
nmsIPAcledesendport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAcledesendport.setStatus("current")


class _NmsIPAcledescompare_Type(Integer32):
    """Custom type nmsIPAcledescompare based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("usemask", 1),
          ("userange", 2))
    )


_NmsIPAcledescompare_Type.__name__ = "Integer32"
_NmsIPAcledescompare_Object = MibTableColumn
nmsIPAcledescompare = _NmsIPAcledescompare_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 25),
    _NmsIPAcledescompare_Type()
)
nmsIPAcledescompare.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAcledescompare.setStatus("current")


class _NmsIPAcledesany_Type(Integer32):
    """Custom type nmsIPAcledesany based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("useany", 0),
          ("usezero", 1))
    )


_NmsIPAcledesany_Type.__name__ = "Integer32"
_NmsIPAcledesany_Object = MibTableColumn
nmsIPAcledesany = _NmsIPAcledesany_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 26),
    _NmsIPAcledesany_Type()
)
nmsIPAcledesany.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAcledesany.setStatus("current")
_NmsIPAcleicmptype_Type = Integer32
_NmsIPAcleicmptype_Object = MibTableColumn
nmsIPAcleicmptype = _NmsIPAcleicmptype_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 27),
    _NmsIPAcleicmptype_Type()
)
nmsIPAcleicmptype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAcleicmptype.setStatus("mandatory")
_NmsIPAcleigmptype_Type = Integer32
_NmsIPAcleigmptype_Object = MibTableColumn
nmsIPAcleigmptype = _NmsIPAcleigmptype_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 28),
    _NmsIPAcleigmptype_Type()
)
nmsIPAcleigmptype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAcleigmptype.setStatus("current")
_NmsIPAcletimerange_Type = DisplayString
_NmsIPAcletimerange_Object = MibTableColumn
nmsIPAcletimerange = _NmsIPAcletimerange_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 29),
    _NmsIPAcletimerange_Type()
)
nmsIPAcletimerange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAcletimerange.setStatus("current")
_NmsIPAcletos_Type = Integer32
_NmsIPAcletos_Object = MibTableColumn
nmsIPAcletos = _NmsIPAcletos_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 30),
    _NmsIPAcletos_Type()
)
nmsIPAcletos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAcletos.setStatus("current")
_NmsIPAcleprecedence_Type = Integer32
_NmsIPAcleprecedence_Object = MibTableColumn
nmsIPAcleprecedence = _NmsIPAcleprecedence_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 31),
    _NmsIPAcleprecedence_Type()
)
nmsIPAcleprecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAcleprecedence.setStatus("current")


class _NmsIPAcleestablished_Type(Integer32):
    """Custom type nmsIPAcleestablished based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_NmsIPAcleestablished_Type.__name__ = "Integer32"
_NmsIPAcleestablished_Object = MibTableColumn
nmsIPAcleestablished = _NmsIPAcleestablished_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 32),
    _NmsIPAcleestablished_Type()
)
nmsIPAcleestablished.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAcleestablished.setStatus("current")


class _NmsIPAclelog_Type(Integer32):
    """Custom type nmsIPAclelog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_NmsIPAclelog_Type.__name__ = "Integer32"
_NmsIPAclelog_Object = MibTableColumn
nmsIPAclelog = _NmsIPAclelog_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 33),
    _NmsIPAclelog_Type()
)
nmsIPAclelog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAclelog.setStatus("current")


class _NmsIPAcledonotfragment_Type(Integer32):
    """Custom type nmsIPAcledonotfragment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("donotcheck", 0),
          ("notset", 2),
          ("set", 1))
    )


_NmsIPAcledonotfragment_Type.__name__ = "Integer32"
_NmsIPAcledonotfragment_Object = MibTableColumn
nmsIPAcledonotfragment = _NmsIPAcledonotfragment_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 34),
    _NmsIPAcledonotfragment_Type()
)
nmsIPAcledonotfragment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAcledonotfragment.setStatus("current")


class _NmsIPAcleisfragment_Type(Integer32):
    """Custom type nmsIPAcleisfragment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("donotcheck", 0),
          ("notset", 2),
          ("set", 1))
    )


_NmsIPAcleisfragment_Type.__name__ = "Integer32"
_NmsIPAcleisfragment_Object = MibTableColumn
nmsIPAcleisfragment = _NmsIPAcleisfragment_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 35),
    _NmsIPAcleisfragment_Type()
)
nmsIPAcleisfragment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAcleisfragment.setStatus("current")


class _NmsIPAcletotallen_Type(Integer32):
    """Custom type nmsIPAcletotallen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NmsIPAcletotallen_Type.__name__ = "Integer32"
_NmsIPAcletotallen_Object = MibTableColumn
nmsIPAcletotallen = _NmsIPAcletotallen_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 36),
    _NmsIPAcletotallen_Type()
)
nmsIPAcletotallen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAcletotallen.setStatus("current")


class _NmsIPAcletotallenflag_Type(Integer32):
    """Custom type nmsIPAcletotallenflag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("donotcheck", 0),
          ("eq", 3),
          ("gt", 1),
          ("lt", 2))
    )


_NmsIPAcletotallenflag_Type.__name__ = "Integer32"
_NmsIPAcletotallenflag_Object = MibTableColumn
nmsIPAcletotallenflag = _NmsIPAcletotallenflag_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 37),
    _NmsIPAcletotallenflag_Type()
)
nmsIPAcletotallenflag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAcletotallenflag.setStatus("current")


class _NmsIPAclettl_Type(Integer32):
    """Custom type nmsIPAclettl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NmsIPAclettl_Type.__name__ = "Integer32"
_NmsIPAclettl_Object = MibTableColumn
nmsIPAclettl = _NmsIPAclettl_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 38),
    _NmsIPAclettl_Type()
)
nmsIPAclettl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAclettl.setStatus("current")


class _NmsIPAclettlflag_Type(Integer32):
    """Custom type nmsIPAclettlflag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("donotcheck", 0),
          ("eq", 3),
          ("gt", 1),
          ("lt", 2))
    )


_NmsIPAclettlflag_Type.__name__ = "Integer32"
_NmsIPAclettlflag_Object = MibTableColumn
nmsIPAclettlflag = _NmsIPAclettlflag_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 39),
    _NmsIPAclettlflag_Type()
)
nmsIPAclettlflag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAclettlflag.setStatus("current")
_NmsIPAclerowstatus_Type = RowStatus
_NmsIPAclerowstatus_Object = MibTableColumn
nmsIPAclerowstatus = _NmsIPAclerowstatus_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 5, 4, 1, 40),
    _NmsIPAclerowstatus_Type()
)
nmsIPAclerowstatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIPAclerowstatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NMS-IPAcl",
    **{"nmsIPAclMIB": nmsIPAclMIB,
       "nmsAclTotal": nmsAclTotal,
       "nmsIPAclTable": nmsIPAclTable,
       "nmsIPAclEntry": nmsIPAclEntry,
       "nmsIPAclname": nmsIPAclname,
       "nmsIPAclEntrytotal": nmsIPAclEntrytotal,
       "nmsIPAclType": nmsIPAclType,
       "nmsIPAclMergeEnable": nmsIPAclMergeEnable,
       "nmsIPAclRowStatus": nmsIPAclRowStatus,
       "nmsIPAclsRuleTable": nmsIPAclsRuleTable,
       "nmsIPAclsRuleEntry": nmsIPAclsRuleEntry,
       "nmsIPAclsname": nmsIPAclsname,
       "nmsIPAclsentryId": nmsIPAclsentryId,
       "nmsIPAclsrule": nmsIPAclsrule,
       "nmsIPAclssrcip": nmsIPAclssrcip,
       "nmsIPAclssrcmask": nmsIPAclssrcmask,
       "nmsIPAclssrcbeginip": nmsIPAclssrcbeginip,
       "nmsIPAclssrcendip": nmsIPAclssrcendip,
       "nmsIPAclscompare": nmsIPAclscompare,
       "nmsIPAclsany": nmsIPAclsany,
       "nmsIPAclslog": nmsIPAclslog,
       "nmsIPAclsrowstatus": nmsIPAclsrowstatus,
       "nmsIPAcleRuleTable": nmsIPAcleRuleTable,
       "nmsIPAcleRuleEntry": nmsIPAcleRuleEntry,
       "nmsIPAclename": nmsIPAclename,
       "nmsIPAcleentryId": nmsIPAcleentryId,
       "nmsIPAclerule": nmsIPAclerule,
       "nmsIPAcleprotocol": nmsIPAcleprotocol,
       "nmsIPAclesrceid": nmsIPAclesrceid,
       "nmsIPAclesrcip": nmsIPAclesrcip,
       "nmsIPAclesrcmask": nmsIPAclesrcmask,
       "nmsIPAclesrcport": nmsIPAclesrcport,
       "nmsIPAclesrcpflag": nmsIPAclesrcpflag,
       "nmsIPAclesrcbeginip": nmsIPAclesrcbeginip,
       "nmsIPAclesrcendip": nmsIPAclesrcendip,
       "nmsIPAclesrcbeginport": nmsIPAclesrcbeginport,
       "nmsIPAclesrcendport": nmsIPAclesrcendport,
       "nmsIPAclesrccompare": nmsIPAclesrccompare,
       "nmsIPAclesrcany": nmsIPAclesrcany,
       "nmsIPAcledeseid": nmsIPAcledeseid,
       "nmsIPAcledesip": nmsIPAcledesip,
       "nmsIPAcledesmask": nmsIPAcledesmask,
       "nmsIPAcledesport": nmsIPAcledesport,
       "nmsIPAcledespflag": nmsIPAcledespflag,
       "nmsIPAcledesbeginip": nmsIPAcledesbeginip,
       "nmsIPAcledesendip": nmsIPAcledesendip,
       "nmsIPAcledesbeginport": nmsIPAcledesbeginport,
       "nmsIPAcledesendport": nmsIPAcledesendport,
       "nmsIPAcledescompare": nmsIPAcledescompare,
       "nmsIPAcledesany": nmsIPAcledesany,
       "nmsIPAcleicmptype": nmsIPAcleicmptype,
       "nmsIPAcleigmptype": nmsIPAcleigmptype,
       "nmsIPAcletimerange": nmsIPAcletimerange,
       "nmsIPAcletos": nmsIPAcletos,
       "nmsIPAcleprecedence": nmsIPAcleprecedence,
       "nmsIPAcleestablished": nmsIPAcleestablished,
       "nmsIPAclelog": nmsIPAclelog,
       "nmsIPAcledonotfragment": nmsIPAcledonotfragment,
       "nmsIPAcleisfragment": nmsIPAcleisfragment,
       "nmsIPAcletotallen": nmsIPAcletotallen,
       "nmsIPAcletotallenflag": nmsIPAcletotallenflag,
       "nmsIPAclettl": nmsIPAclettl,
       "nmsIPAclettlflag": nmsIPAclettlflag,
       "nmsIPAclerowstatus": nmsIPAclerowstatus}
)
