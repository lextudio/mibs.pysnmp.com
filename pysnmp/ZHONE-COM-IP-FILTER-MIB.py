# SNMP MIB module (ZHONE-COM-IP-FILTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHONE-COM-IP-FILTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:13 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(zhoneIp,
 zhoneModules) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneIp",
    "zhoneModules")

(ZhoneAdminString,
 ZhoneRowStatus) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneAdminString",
    "ZhoneRowStatus")


# MODULE-IDENTITY

comIpFilter = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 58)
)
comIpFilter.setRevisions(
        ("2005-01-10 10:16",
         "2005-01-03 09:24",
         "2004-12-21 09:25",
         "2004-08-30 11:00",
         "2004-04-06 00:17",
         "2001-01-17 08:48",
         "2000-09-11 16:22")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Filter_ObjectIdentity = ObjectIdentity
filter = _Filter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8)
)
if mibBuilder.loadTexts:
    filter.setStatus("current")
_FilterGlobal_ObjectIdentity = ObjectIdentity
filterGlobal = _FilterGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 1)
)
if mibBuilder.loadTexts:
    filterGlobal.setStatus("current")


class _FltGlobalIndexNext_Type(Integer32):
    """Custom type fltGlobalIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FltGlobalIndexNext_Type.__name__ = "Integer32"
_FltGlobalIndexNext_Object = MibScalar
fltGlobalIndexNext = _FltGlobalIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 1, 1),
    _FltGlobalIndexNext_Type()
)
fltGlobalIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltGlobalIndexNext.setStatus("current")


class _FltGlobalTimeout_Type(Integer32):
    """Custom type fltGlobalTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FltGlobalTimeout_Type.__name__ = "Integer32"
_FltGlobalTimeout_Object = MibScalar
fltGlobalTimeout = _FltGlobalTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 1, 2),
    _FltGlobalTimeout_Type()
)
fltGlobalTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltGlobalTimeout.setStatus("current")
if mibBuilder.loadTexts:
    fltGlobalTimeout.setUnits("seconds")
_FilterSpecTable_Object = MibTable
filterSpecTable = _FilterSpecTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 2)
)
if mibBuilder.loadTexts:
    filterSpecTable.setStatus("current")
_FilterSpecEntry_Object = MibTableRow
filterSpecEntry = _FilterSpecEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 2, 1)
)
filterSpecEntry.setIndexNames(
    (0, "ZHONE-COM-IP-FILTER-MIB", "fltSpecIndex"),
)
if mibBuilder.loadTexts:
    filterSpecEntry.setStatus("current")


class _FltSpecIndex_Type(Integer32):
    """Custom type fltSpecIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FltSpecIndex_Type.__name__ = "Integer32"
_FltSpecIndex_Object = MibTableColumn
fltSpecIndex = _FltSpecIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 2, 1, 1),
    _FltSpecIndex_Type()
)
fltSpecIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fltSpecIndex.setStatus("current")
_FltSpecName_Type = ZhoneAdminString
_FltSpecName_Object = MibTableColumn
fltSpecName = _FltSpecName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 2, 1, 2),
    _FltSpecName_Type()
)
fltSpecName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltSpecName.setStatus("current")
_FltSpecDesc_Type = SnmpAdminString
_FltSpecDesc_Object = MibTableColumn
fltSpecDesc = _FltSpecDesc_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 2, 1, 3),
    _FltSpecDesc_Type()
)
fltSpecDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltSpecDesc.setStatus("current")


class _FltSpecVersion1_Type(Unsigned32):
    """Custom type fltSpecVersion1 based on Unsigned32"""
    defaultValue = 0


_FltSpecVersion1_Object = MibTableColumn
fltSpecVersion1 = _FltSpecVersion1_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 2, 1, 4),
    _FltSpecVersion1_Type()
)
fltSpecVersion1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltSpecVersion1.setStatus("current")


class _FltSpecVersion2_Type(Unsigned32):
    """Custom type fltSpecVersion2 based on Unsigned32"""
    defaultValue = 0


_FltSpecVersion2_Object = MibTableColumn
fltSpecVersion2 = _FltSpecVersion2_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 2, 1, 5),
    _FltSpecVersion2_Type()
)
fltSpecVersion2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltSpecVersion2.setStatus("current")


class _FltSpecLanguageVersion_Type(Unsigned32):
    """Custom type fltSpecLanguageVersion based on Unsigned32"""
    defaultValue = 0


_FltSpecLanguageVersion_Object = MibTableColumn
fltSpecLanguageVersion = _FltSpecLanguageVersion_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 2, 1, 6),
    _FltSpecLanguageVersion_Type()
)
fltSpecLanguageVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltSpecLanguageVersion.setStatus("current")
_FltSpecRowStatus_Type = ZhoneRowStatus
_FltSpecRowStatus_Object = MibTableColumn
fltSpecRowStatus = _FltSpecRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 2, 1, 7),
    _FltSpecRowStatus_Type()
)
fltSpecRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltSpecRowStatus.setStatus("current")
_FilterStatementTable_Object = MibTable
filterStatementTable = _FilterStatementTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 3)
)
if mibBuilder.loadTexts:
    filterStatementTable.setStatus("current")
_FilterStatementEntry_Object = MibTableRow
filterStatementEntry = _FilterStatementEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 3, 1)
)
filterStatementEntry.setIndexNames(
    (0, "ZHONE-COM-IP-FILTER-MIB", "fltSpecIndex"),
    (0, "ZHONE-COM-IP-FILTER-MIB", "fltStmtIndex"),
)
if mibBuilder.loadTexts:
    filterStatementEntry.setStatus("current")


class _FltStmtIndex_Type(Integer32):
    """Custom type fltStmtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FltStmtIndex_Type.__name__ = "Integer32"
_FltStmtIndex_Object = MibTableColumn
fltStmtIndex = _FltStmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 3, 1, 1),
    _FltStmtIndex_Type()
)
fltStmtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fltStmtIndex.setStatus("current")


class _FltStmtIpSrcAddrLow_Type(IpAddress):
    """Custom type fltStmtIpSrcAddrLow based on IpAddress"""
    defaultHexValue = "00000000"


_FltStmtIpSrcAddrLow_Object = MibTableColumn
fltStmtIpSrcAddrLow = _FltStmtIpSrcAddrLow_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 3, 1, 2),
    _FltStmtIpSrcAddrLow_Type()
)
fltStmtIpSrcAddrLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltStmtIpSrcAddrLow.setStatus("current")


class _FltStmtIpSrcAddrHigh_Type(IpAddress):
    """Custom type fltStmtIpSrcAddrHigh based on IpAddress"""
    defaultHexValue = "00000000"


_FltStmtIpSrcAddrHigh_Object = MibTableColumn
fltStmtIpSrcAddrHigh = _FltStmtIpSrcAddrHigh_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 3, 1, 3),
    _FltStmtIpSrcAddrHigh_Type()
)
fltStmtIpSrcAddrHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltStmtIpSrcAddrHigh.setStatus("current")


class _FltStmtSrcPortLow_Type(Integer32):
    """Custom type fltStmtSrcPortLow based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FltStmtSrcPortLow_Type.__name__ = "Integer32"
_FltStmtSrcPortLow_Object = MibTableColumn
fltStmtSrcPortLow = _FltStmtSrcPortLow_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 3, 1, 4),
    _FltStmtSrcPortLow_Type()
)
fltStmtSrcPortLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltStmtSrcPortLow.setStatus("current")


class _FltStmtSrcPortHigh_Type(Integer32):
    """Custom type fltStmtSrcPortHigh based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FltStmtSrcPortHigh_Type.__name__ = "Integer32"
_FltStmtSrcPortHigh_Object = MibTableColumn
fltStmtSrcPortHigh = _FltStmtSrcPortHigh_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 3, 1, 5),
    _FltStmtSrcPortHigh_Type()
)
fltStmtSrcPortHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltStmtSrcPortHigh.setStatus("current")


class _FltStmtIpDstAddrLow_Type(IpAddress):
    """Custom type fltStmtIpDstAddrLow based on IpAddress"""
    defaultHexValue = "00000000"


_FltStmtIpDstAddrLow_Object = MibTableColumn
fltStmtIpDstAddrLow = _FltStmtIpDstAddrLow_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 3, 1, 6),
    _FltStmtIpDstAddrLow_Type()
)
fltStmtIpDstAddrLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltStmtIpDstAddrLow.setStatus("current")


class _FltStmtIpDstAddrHigh_Type(IpAddress):
    """Custom type fltStmtIpDstAddrHigh based on IpAddress"""
    defaultHexValue = "00000000"


_FltStmtIpDstAddrHigh_Object = MibTableColumn
fltStmtIpDstAddrHigh = _FltStmtIpDstAddrHigh_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 3, 1, 7),
    _FltStmtIpDstAddrHigh_Type()
)
fltStmtIpDstAddrHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltStmtIpDstAddrHigh.setStatus("current")


class _FltStmtDstPortLow_Type(Integer32):
    """Custom type fltStmtDstPortLow based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FltStmtDstPortLow_Type.__name__ = "Integer32"
_FltStmtDstPortLow_Object = MibTableColumn
fltStmtDstPortLow = _FltStmtDstPortLow_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 3, 1, 8),
    _FltStmtDstPortLow_Type()
)
fltStmtDstPortLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltStmtDstPortLow.setStatus("current")


class _FltStmtDstPortHigh_Type(Integer32):
    """Custom type fltStmtDstPortHigh based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FltStmtDstPortHigh_Type.__name__ = "Integer32"
_FltStmtDstPortHigh_Object = MibTableColumn
fltStmtDstPortHigh = _FltStmtDstPortHigh_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 3, 1, 9),
    _FltStmtDstPortHigh_Type()
)
fltStmtDstPortHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltStmtDstPortHigh.setStatus("current")


class _FltStmtIpProtocol_Type(Integer32):
    """Custom type fltStmtIpProtocol based on Integer32"""
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
        *(("any", 1),
          ("icmp", 5),
          ("ip", 2),
          ("tcp", 3),
          ("udp", 4))
    )


_FltStmtIpProtocol_Type.__name__ = "Integer32"
_FltStmtIpProtocol_Object = MibTableColumn
fltStmtIpProtocol = _FltStmtIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 3, 1, 10),
    _FltStmtIpProtocol_Type()
)
fltStmtIpProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltStmtIpProtocol.setStatus("current")


class _FltStmtArbValueBase_Type(Integer32):
    """Custom type fltStmtArbValueBase based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("icmp", 5),
          ("ip", 2),
          ("ipOptions", 6),
          ("none", 1),
          ("tcp", 4),
          ("tcpOptions", 7),
          ("udp", 3))
    )


_FltStmtArbValueBase_Type.__name__ = "Integer32"
_FltStmtArbValueBase_Object = MibTableColumn
fltStmtArbValueBase = _FltStmtArbValueBase_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 3, 1, 11),
    _FltStmtArbValueBase_Type()
)
fltStmtArbValueBase.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltStmtArbValueBase.setStatus("current")


class _FltStmtArbOffset_Type(Integer32):
    """Custom type fltStmtArbOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_FltStmtArbOffset_Type.__name__ = "Integer32"
_FltStmtArbOffset_Object = MibTableColumn
fltStmtArbOffset = _FltStmtArbOffset_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 3, 1, 12),
    _FltStmtArbOffset_Type()
)
fltStmtArbOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltStmtArbOffset.setStatus("current")


class _FltStmtArbMask_Type(Unsigned32):
    """Custom type fltStmtArbMask based on Unsigned32"""
    defaultValue = 0


_FltStmtArbMask_Object = MibTableColumn
fltStmtArbMask = _FltStmtArbMask_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 3, 1, 13),
    _FltStmtArbMask_Type()
)
fltStmtArbMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltStmtArbMask.setStatus("current")


class _FltStmtArbValueLow_Type(Unsigned32):
    """Custom type fltStmtArbValueLow based on Unsigned32"""
    defaultValue = 0


_FltStmtArbValueLow_Object = MibTableColumn
fltStmtArbValueLow = _FltStmtArbValueLow_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 3, 1, 14),
    _FltStmtArbValueLow_Type()
)
fltStmtArbValueLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltStmtArbValueLow.setStatus("current")


class _FltStmtArbValueHigh_Type(Unsigned32):
    """Custom type fltStmtArbValueHigh based on Unsigned32"""
    defaultValue = 0


_FltStmtArbValueHigh_Object = MibTableColumn
fltStmtArbValueHigh = _FltStmtArbValueHigh_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 3, 1, 15),
    _FltStmtArbValueHigh_Type()
)
fltStmtArbValueHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltStmtArbValueHigh.setStatus("current")


class _FltStmtModifier_Type(Bits):
    """Custom type fltStmtModifier based on Bits"""
    namedValues = NamedValues(
        *(("notArbitrary", 5),
          ("notDstIp", 2),
          ("notIpSrc", 0),
          ("notPortDst", 3),
          ("notProtocol", 4),
          ("notSrcPort", 1),
          ("notStatement", 6))
    )

_FltStmtModifier_Type.__name__ = "Bits"
_FltStmtModifier_Object = MibTableColumn
fltStmtModifier = _FltStmtModifier_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 3, 1, 16),
    _FltStmtModifier_Type()
)
fltStmtModifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltStmtModifier.setStatus("current")


class _FltStmtAction_Type(Bits):
    """Custom type fltStmtAction based on Bits"""
    defaultBinValue = "001"

    namedValues = NamedValues(
        *(("deny", 2),
          ("forward", 3),
          ("log", 5),
          ("permit", 1),
          ("reject", 4),
          ("reset", 0))
    )

_FltStmtAction_Type.__name__ = "Bits"
_FltStmtAction_Object = MibTableColumn
fltStmtAction = _FltStmtAction_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 3, 1, 17),
    _FltStmtAction_Type()
)
fltStmtAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltStmtAction.setStatus("current")


class _FltStmtActionArg_Type(Integer32):
    """Custom type fltStmtActionArg based on Integer32"""
    defaultValue = 0


_FltStmtActionArg_Object = MibTableColumn
fltStmtActionArg = _FltStmtActionArg_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 3, 1, 18),
    _FltStmtActionArg_Type()
)
fltStmtActionArg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltStmtActionArg.setStatus("current")
_FltStmtRowStatus_Type = ZhoneRowStatus
_FltStmtRowStatus_Object = MibTableColumn
fltStmtRowStatus = _FltStmtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 3, 1, 19),
    _FltStmtRowStatus_Type()
)
fltStmtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltStmtRowStatus.setStatus("current")
_FilterStmtRenumTable_Object = MibTable
filterStmtRenumTable = _FilterStmtRenumTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 4)
)
if mibBuilder.loadTexts:
    filterStmtRenumTable.setStatus("current")
_FilterStmtRenumEntry_Object = MibTableRow
filterStmtRenumEntry = _FilterStmtRenumEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 4, 1)
)
if mibBuilder.loadTexts:
    filterStmtRenumEntry.setStatus("current")


class _FltStmtIndexNew_Type(Integer32):
    """Custom type fltStmtIndexNew based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FltStmtIndexNew_Type.__name__ = "Integer32"
_FltStmtIndexNew_Object = MibTableColumn
fltStmtIndexNew = _FltStmtIndexNew_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 4, 1, 1),
    _FltStmtIndexNew_Type()
)
fltStmtIndexNew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltStmtIndexNew.setStatus("current")
_FilterStatsTable_Object = MibTable
filterStatsTable = _FilterStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 5)
)
if mibBuilder.loadTexts:
    filterStatsTable.setStatus("current")
_FilterStatsEntry_Object = MibTableRow
filterStatsEntry = _FilterStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 5, 1)
)
filterStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZHONE-COM-IP-FILTER-MIB", "fltStatDirection"),
)
if mibBuilder.loadTexts:
    filterStatsEntry.setStatus("current")


class _FltStatDirection_Type(Integer32):
    """Custom type fltStatDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("egress", 2),
          ("ingress", 1))
    )


_FltStatDirection_Type.__name__ = "Integer32"
_FltStatDirection_Object = MibTableColumn
fltStatDirection = _FltStatDirection_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 5, 1, 1),
    _FltStatDirection_Type()
)
fltStatDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fltStatDirection.setStatus("current")
_FltStatResetPkts_Type = Counter32
_FltStatResetPkts_Object = MibTableColumn
fltStatResetPkts = _FltStatResetPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 5, 1, 2),
    _FltStatResetPkts_Type()
)
fltStatResetPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltStatResetPkts.setStatus("current")
if mibBuilder.loadTexts:
    fltStatResetPkts.setUnits("packets")
_FltStatPermitPkts_Type = Counter32
_FltStatPermitPkts_Object = MibTableColumn
fltStatPermitPkts = _FltStatPermitPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 5, 1, 3),
    _FltStatPermitPkts_Type()
)
fltStatPermitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltStatPermitPkts.setStatus("current")
if mibBuilder.loadTexts:
    fltStatPermitPkts.setUnits("packets")
_FltStatDenyPkts_Type = Counter32
_FltStatDenyPkts_Object = MibTableColumn
fltStatDenyPkts = _FltStatDenyPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 5, 1, 4),
    _FltStatDenyPkts_Type()
)
fltStatDenyPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltStatDenyPkts.setStatus("current")
if mibBuilder.loadTexts:
    fltStatDenyPkts.setUnits("packets")
_FltStatForwardPkts_Type = Counter32
_FltStatForwardPkts_Object = MibTableColumn
fltStatForwardPkts = _FltStatForwardPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 5, 1, 5),
    _FltStatForwardPkts_Type()
)
fltStatForwardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltStatForwardPkts.setStatus("current")
if mibBuilder.loadTexts:
    fltStatForwardPkts.setUnits("packets")
_FltStatRejectPkts_Type = Counter32
_FltStatRejectPkts_Object = MibTableColumn
fltStatRejectPkts = _FltStatRejectPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 5, 1, 6),
    _FltStatRejectPkts_Type()
)
fltStatRejectPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltStatRejectPkts.setStatus("current")
if mibBuilder.loadTexts:
    fltStatRejectPkts.setUnits("packets")
_FltStatLogPkts_Type = Counter32
_FltStatLogPkts_Object = MibTableColumn
fltStatLogPkts = _FltStatLogPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 5, 1, 7),
    _FltStatLogPkts_Type()
)
fltStatLogPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltStatLogPkts.setStatus("current")
if mibBuilder.loadTexts:
    fltStatLogPkts.setUnits("packets")
_FltStatDefaultPkts_Type = Counter32
_FltStatDefaultPkts_Object = MibTableColumn
fltStatDefaultPkts = _FltStatDefaultPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 5, 1, 8),
    _FltStatDefaultPkts_Type()
)
fltStatDefaultPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltStatDefaultPkts.setStatus("current")
_FltStatSpecVersion_Type = Unsigned32
_FltStatSpecVersion_Object = MibTableColumn
fltStatSpecVersion = _FltStatSpecVersion_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 5, 1, 9),
    _FltStatSpecVersion_Type()
)
fltStatSpecVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltStatSpecVersion.setStatus("current")


class _FltStatSpecIndex_Type(Integer32):
    """Custom type fltStatSpecIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FltStatSpecIndex_Type.__name__ = "Integer32"
_FltStatSpecIndex_Object = MibTableColumn
fltStatSpecIndex = _FltStatSpecIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 5, 1, 10),
    _FltStatSpecIndex_Type()
)
fltStatSpecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltStatSpecIndex.setStatus("current")
_McastControl_ObjectIdentity = ObjectIdentity
mcastControl = _McastControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 6)
)
if mibBuilder.loadTexts:
    mcastControl.setStatus("current")
_McastControlListTable_Object = MibTable
mcastControlListTable = _McastControlListTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 6, 1)
)
if mibBuilder.loadTexts:
    mcastControlListTable.setStatus("current")
_McastControlListEntry_Object = MibTableRow
mcastControlListEntry = _McastControlListEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 6, 1, 1)
)
mcastControlListEntry.setIndexNames(
    (0, "ZHONE-COM-IP-FILTER-MIB", "mcastControlListControlId"),
    (0, "ZHONE-COM-IP-FILTER-MIB", "mcastControlListControlPrecedence"),
)
if mibBuilder.loadTexts:
    mcastControlListEntry.setStatus("current")


class _McastControlListControlId_Type(Integer32):
    """Custom type mcastControlListControlId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_McastControlListControlId_Type.__name__ = "Integer32"
_McastControlListControlId_Object = MibTableColumn
mcastControlListControlId = _McastControlListControlId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 6, 1, 1, 1),
    _McastControlListControlId_Type()
)
mcastControlListControlId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mcastControlListControlId.setStatus("current")


class _McastControlListControlPrecedence_Type(Integer32):
    """Custom type mcastControlListControlPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_McastControlListControlPrecedence_Type.__name__ = "Integer32"
_McastControlListControlPrecedence_Object = MibTableColumn
mcastControlListControlPrecedence = _McastControlListControlPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 6, 1, 1, 2),
    _McastControlListControlPrecedence_Type()
)
mcastControlListControlPrecedence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mcastControlListControlPrecedence.setStatus("current")
_McastControlListRowStatus_Type = ZhoneRowStatus
_McastControlListRowStatus_Object = MibTableColumn
mcastControlListRowStatus = _McastControlListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 6, 1, 1, 3),
    _McastControlListRowStatus_Type()
)
mcastControlListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mcastControlListRowStatus.setStatus("current")
_McastControlListIpAddress_Type = IpAddress
_McastControlListIpAddress_Object = MibTableColumn
mcastControlListIpAddress = _McastControlListIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 6, 1, 1, 4),
    _McastControlListIpAddress_Type()
)
mcastControlListIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mcastControlListIpAddress.setStatus("current")


class _McastControlListType_Type(Integer32):
    """Custom type mcastControlListType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("always-on", 2),
          ("normal", 1),
          ("periodic", 3))
    )


_McastControlListType_Type.__name__ = "Integer32"
_McastControlListType_Object = MibTableColumn
mcastControlListType = _McastControlListType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 6, 1, 1, 5),
    _McastControlListType_Type()
)
mcastControlListType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mcastControlListType.setStatus("current")
_PortAccessControl_ObjectIdentity = ObjectIdentity
portAccessControl = _PortAccessControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 7)
)
if mibBuilder.loadTexts:
    portAccessControl.setStatus("current")
_PortAccessNextIndex_Type = Integer32
_PortAccessNextIndex_Object = MibScalar
portAccessNextIndex = _PortAccessNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 7, 1),
    _PortAccessNextIndex_Type()
)
portAccessNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portAccessNextIndex.setStatus("current")
_PortAccessTable_Object = MibTable
portAccessTable = _PortAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 7, 2)
)
if mibBuilder.loadTexts:
    portAccessTable.setStatus("current")
_PortAccessEntry_Object = MibTableRow
portAccessEntry = _PortAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 7, 2, 1)
)
portAccessEntry.setIndexNames(
    (0, "ZHONE-COM-IP-FILTER-MIB", "portAccessIndex"),
)
if mibBuilder.loadTexts:
    portAccessEntry.setStatus("current")


class _PortAccessIndex_Type(Integer32):
    """Custom type portAccessIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_PortAccessIndex_Type.__name__ = "Integer32"
_PortAccessIndex_Object = MibTableColumn
portAccessIndex = _PortAccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 7, 2, 1, 1),
    _PortAccessIndex_Type()
)
portAccessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portAccessIndex.setStatus("current")
_PortAccessRowStatus_Type = ZhoneRowStatus
_PortAccessRowStatus_Object = MibTableColumn
portAccessRowStatus = _PortAccessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 7, 2, 1, 2),
    _PortAccessRowStatus_Type()
)
portAccessRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portAccessRowStatus.setStatus("current")


class _PortAccessNumber_Type(Integer32):
    """Custom type portAccessNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_PortAccessNumber_Type.__name__ = "Integer32"
_PortAccessNumber_Object = MibTableColumn
portAccessNumber = _PortAccessNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 7, 2, 1, 3),
    _PortAccessNumber_Type()
)
portAccessNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portAccessNumber.setStatus("current")
_PortAccessSrcAddr_Type = IpAddress
_PortAccessSrcAddr_Object = MibTableColumn
portAccessSrcAddr = _PortAccessSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 7, 2, 1, 4),
    _PortAccessSrcAddr_Type()
)
portAccessSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portAccessSrcAddr.setStatus("current")
_PortAccessNetMask_Type = IpAddress
_PortAccessNetMask_Object = MibTableColumn
portAccessNetMask = _PortAccessNetMask_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 8, 7, 2, 1, 5),
    _PortAccessNetMask_Type()
)
portAccessNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portAccessNetMask.setStatus("current")
filterStatementEntry.registerAugmentions(
    ("ZHONE-COM-IP-FILTER-MIB",
     "filterStmtRenumEntry")
)
filterStmtRenumEntry.setIndexNames(*filterStatementEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-COM-IP-FILTER-MIB",
    **{"filter": filter,
       "filterGlobal": filterGlobal,
       "fltGlobalIndexNext": fltGlobalIndexNext,
       "fltGlobalTimeout": fltGlobalTimeout,
       "filterSpecTable": filterSpecTable,
       "filterSpecEntry": filterSpecEntry,
       "fltSpecIndex": fltSpecIndex,
       "fltSpecName": fltSpecName,
       "fltSpecDesc": fltSpecDesc,
       "fltSpecVersion1": fltSpecVersion1,
       "fltSpecVersion2": fltSpecVersion2,
       "fltSpecLanguageVersion": fltSpecLanguageVersion,
       "fltSpecRowStatus": fltSpecRowStatus,
       "filterStatementTable": filterStatementTable,
       "filterStatementEntry": filterStatementEntry,
       "fltStmtIndex": fltStmtIndex,
       "fltStmtIpSrcAddrLow": fltStmtIpSrcAddrLow,
       "fltStmtIpSrcAddrHigh": fltStmtIpSrcAddrHigh,
       "fltStmtSrcPortLow": fltStmtSrcPortLow,
       "fltStmtSrcPortHigh": fltStmtSrcPortHigh,
       "fltStmtIpDstAddrLow": fltStmtIpDstAddrLow,
       "fltStmtIpDstAddrHigh": fltStmtIpDstAddrHigh,
       "fltStmtDstPortLow": fltStmtDstPortLow,
       "fltStmtDstPortHigh": fltStmtDstPortHigh,
       "fltStmtIpProtocol": fltStmtIpProtocol,
       "fltStmtArbValueBase": fltStmtArbValueBase,
       "fltStmtArbOffset": fltStmtArbOffset,
       "fltStmtArbMask": fltStmtArbMask,
       "fltStmtArbValueLow": fltStmtArbValueLow,
       "fltStmtArbValueHigh": fltStmtArbValueHigh,
       "fltStmtModifier": fltStmtModifier,
       "fltStmtAction": fltStmtAction,
       "fltStmtActionArg": fltStmtActionArg,
       "fltStmtRowStatus": fltStmtRowStatus,
       "filterStmtRenumTable": filterStmtRenumTable,
       "filterStmtRenumEntry": filterStmtRenumEntry,
       "fltStmtIndexNew": fltStmtIndexNew,
       "filterStatsTable": filterStatsTable,
       "filterStatsEntry": filterStatsEntry,
       "fltStatDirection": fltStatDirection,
       "fltStatResetPkts": fltStatResetPkts,
       "fltStatPermitPkts": fltStatPermitPkts,
       "fltStatDenyPkts": fltStatDenyPkts,
       "fltStatForwardPkts": fltStatForwardPkts,
       "fltStatRejectPkts": fltStatRejectPkts,
       "fltStatLogPkts": fltStatLogPkts,
       "fltStatDefaultPkts": fltStatDefaultPkts,
       "fltStatSpecVersion": fltStatSpecVersion,
       "fltStatSpecIndex": fltStatSpecIndex,
       "mcastControl": mcastControl,
       "mcastControlListTable": mcastControlListTable,
       "mcastControlListEntry": mcastControlListEntry,
       "mcastControlListControlId": mcastControlListControlId,
       "mcastControlListControlPrecedence": mcastControlListControlPrecedence,
       "mcastControlListRowStatus": mcastControlListRowStatus,
       "mcastControlListIpAddress": mcastControlListIpAddress,
       "mcastControlListType": mcastControlListType,
       "portAccessControl": portAccessControl,
       "portAccessNextIndex": portAccessNextIndex,
       "portAccessTable": portAccessTable,
       "portAccessEntry": portAccessEntry,
       "portAccessIndex": portAccessIndex,
       "portAccessRowStatus": portAccessRowStatus,
       "portAccessNumber": portAccessNumber,
       "portAccessSrcAddr": portAccessSrcAddr,
       "portAccessNetMask": portAccessNetMask,
       "comIpFilter": comIpFilter}
)
