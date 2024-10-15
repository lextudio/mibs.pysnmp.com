# SNMP MIB module (HH3C-NAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-NAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:18 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

hh3cNat = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18)
)
hh3cNat.setRevisions(
        ("2005-01-20 15:18",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cNATGlobalVars_ObjectIdentity = ObjectIdentity
hh3cNATGlobalVars = _Hh3cNATGlobalVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 1)
)
_Hh3cNATClearSession_ObjectIdentity = ObjectIdentity
hh3cNATClearSession = _Hh3cNATClearSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 1, 1)
)


class _Hh3cNATClearSessionSlotNo_Type(Integer32):
    """Custom type hh3cNATClearSessionSlotNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
        ValueRangeConstraint(255, 255),
    )


_Hh3cNATClearSessionSlotNo_Type.__name__ = "Integer32"
_Hh3cNATClearSessionSlotNo_Object = MibScalar
hh3cNATClearSessionSlotNo = _Hh3cNATClearSessionSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 1, 1, 1),
    _Hh3cNATClearSessionSlotNo_Type()
)
hh3cNATClearSessionSlotNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNATClearSessionSlotNo.setStatus("current")
_Hh3cNATBLConnectLimitPara_ObjectIdentity = ObjectIdentity
hh3cNATBLConnectLimitPara = _Hh3cNATBLConnectLimitPara_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 1, 2)
)


class _Hh3cNATBLConnectHighValue_Type(Integer32):
    """Custom type hh3cNATBLConnectHighValue based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 20000),
    )


_Hh3cNATBLConnectHighValue_Type.__name__ = "Integer32"
_Hh3cNATBLConnectHighValue_Object = MibScalar
hh3cNATBLConnectHighValue = _Hh3cNATBLConnectHighValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 1, 2, 1),
    _Hh3cNATBLConnectHighValue_Type()
)
hh3cNATBLConnectHighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNATBLConnectHighValue.setStatus("current")


class _Hh3cNATBLConnectLowValue_Type(Integer32):
    """Custom type hh3cNATBLConnectLowValue based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 20000),
    )


_Hh3cNATBLConnectLowValue_Type.__name__ = "Integer32"
_Hh3cNATBLConnectLowValue_Object = MibScalar
hh3cNATBLConnectLowValue = _Hh3cNATBLConnectLowValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 1, 2, 2),
    _Hh3cNATBLConnectLowValue_Type()
)
hh3cNATBLConnectLowValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNATBLConnectLowValue.setStatus("current")


class _Hh3cNATBLConnectHighRate_Type(Integer32):
    """Custom type hh3cNATBLConnectHighRate based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 21474836),
    )


_Hh3cNATBLConnectHighRate_Type.__name__ = "Integer32"
_Hh3cNATBLConnectHighRate_Object = MibScalar
hh3cNATBLConnectHighRate = _Hh3cNATBLConnectHighRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 1, 2, 3),
    _Hh3cNATBLConnectHighRate_Type()
)
hh3cNATBLConnectHighRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNATBLConnectHighRate.setStatus("current")


class _Hh3cNATBLConnectLowRate_Type(Integer32):
    """Custom type hh3cNATBLConnectLowRate based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 21474836),
    )


_Hh3cNATBLConnectLowRate_Type.__name__ = "Integer32"
_Hh3cNATBLConnectLowRate_Object = MibScalar
hh3cNATBLConnectLowRate = _Hh3cNATBLConnectLowRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 1, 2, 4),
    _Hh3cNATBLConnectLowRate_Type()
)
hh3cNATBLConnectLowRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNATBLConnectLowRate.setStatus("current")


class _Hh3cNATBLSpecialConnectHighRate_Type(Integer32):
    """Custom type hh3cNATBLSpecialConnectHighRate based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 21474836),
    )


_Hh3cNATBLSpecialConnectHighRate_Type.__name__ = "Integer32"
_Hh3cNATBLSpecialConnectHighRate_Object = MibScalar
hh3cNATBLSpecialConnectHighRate = _Hh3cNATBLSpecialConnectHighRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 1, 2, 5),
    _Hh3cNATBLSpecialConnectHighRate_Type()
)
hh3cNATBLSpecialConnectHighRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNATBLSpecialConnectHighRate.setStatus("current")


class _Hh3cNATBLSpecialConnectLowRate_Type(Integer32):
    """Custom type hh3cNATBLSpecialConnectLowRate based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 21474836),
    )


_Hh3cNATBLSpecialConnectLowRate_Type.__name__ = "Integer32"
_Hh3cNATBLSpecialConnectLowRate_Object = MibScalar
hh3cNATBLSpecialConnectLowRate = _Hh3cNATBLSpecialConnectLowRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 1, 2, 6),
    _Hh3cNATBLSpecialConnectLowRate_Type()
)
hh3cNATBLSpecialConnectLowRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNATBLSpecialConnectLowRate.setStatus("current")
_Hh3cNATBLCtrlEnable_ObjectIdentity = ObjectIdentity
hh3cNATBLCtrlEnable = _Hh3cNATBLCtrlEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 1, 3)
)


class _Hh3cNATBLConnectSumEnable_Type(Integer32):
    """Custom type hh3cNATBLConnectSumEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_Hh3cNATBLConnectSumEnable_Type.__name__ = "Integer32"
_Hh3cNATBLConnectSumEnable_Object = MibScalar
hh3cNATBLConnectSumEnable = _Hh3cNATBLConnectSumEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 1, 3, 1),
    _Hh3cNATBLConnectSumEnable_Type()
)
hh3cNATBLConnectSumEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNATBLConnectSumEnable.setStatus("current")


class _Hh3cNATBLConnectRateEnable_Type(Integer32):
    """Custom type hh3cNATBLConnectRateEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_Hh3cNATBLConnectRateEnable_Type.__name__ = "Integer32"
_Hh3cNATBLConnectRateEnable_Object = MibScalar
hh3cNATBLConnectRateEnable = _Hh3cNATBLConnectRateEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 1, 3, 2),
    _Hh3cNATBLConnectRateEnable_Type()
)
hh3cNATBLConnectRateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNATBLConnectRateEnable.setStatus("current")
_Hh3cNATNPTimer_ObjectIdentity = ObjectIdentity
hh3cNATNPTimer = _Hh3cNATNPTimer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 1, 4)
)


class _Hh3cNATNPAgingTime_Type(Integer32):
    """Custom type hh3cNATNPAgingTime based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fast", 1),
          ("slow", 2))
    )


_Hh3cNATNPAgingTime_Type.__name__ = "Integer32"
_Hh3cNATNPAgingTime_Object = MibScalar
hh3cNATNPAgingTime = _Hh3cNATNPAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 1, 4, 1),
    _Hh3cNATNPAgingTime_Type()
)
hh3cNATNPAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNATNPAgingTime.setStatus("current")
_Hh3cNATMibObjects_ObjectIdentity = ObjectIdentity
hh3cNATMibObjects = _Hh3cNATMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2)
)
_Hh3cNATPoolInfoTable_Object = MibTable
hh3cNATPoolInfoTable = _Hh3cNATPoolInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cNATPoolInfoTable.setStatus("current")
_Hh3cNATPoolInfoEntry_Object = MibTableRow
hh3cNATPoolInfoEntry = _Hh3cNATPoolInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 1, 1)
)
hh3cNATPoolInfoEntry.setIndexNames(
    (0, "HH3C-NAT-MIB", "hh3cNATPoolIdx"),
)
if mibBuilder.loadTexts:
    hh3cNATPoolInfoEntry.setStatus("current")


class _Hh3cNATPoolIdx_Type(Integer32):
    """Custom type hh3cNATPoolIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 320),
    )


_Hh3cNATPoolIdx_Type.__name__ = "Integer32"
_Hh3cNATPoolIdx_Object = MibTableColumn
hh3cNATPoolIdx = _Hh3cNATPoolIdx_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 1, 1, 1),
    _Hh3cNATPoolIdx_Type()
)
hh3cNATPoolIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATPoolIdx.setStatus("current")
_Hh3cNATPoolStartIpAddr_Type = IpAddress
_Hh3cNATPoolStartIpAddr_Object = MibTableColumn
hh3cNATPoolStartIpAddr = _Hh3cNATPoolStartIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 1, 1, 2),
    _Hh3cNATPoolStartIpAddr_Type()
)
hh3cNATPoolStartIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATPoolStartIpAddr.setStatus("current")
_Hh3cNATPoolEndIpAddr_Type = IpAddress
_Hh3cNATPoolEndIpAddr_Object = MibTableColumn
hh3cNATPoolEndIpAddr = _Hh3cNATPoolEndIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 1, 1, 3),
    _Hh3cNATPoolEndIpAddr_Type()
)
hh3cNATPoolEndIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATPoolEndIpAddr.setStatus("current")


class _Hh3cNATPoolSlotNo_Type(Integer32):
    """Custom type hh3cNATPoolSlotNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
        ValueRangeConstraint(255, 255),
    )


_Hh3cNATPoolSlotNo_Type.__name__ = "Integer32"
_Hh3cNATPoolSlotNo_Object = MibTableColumn
hh3cNATPoolSlotNo = _Hh3cNATPoolSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 1, 1, 4),
    _Hh3cNATPoolSlotNo_Type()
)
hh3cNATPoolSlotNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATPoolSlotNo.setStatus("current")
_Hh3cNATPoolRefCounter_Type = Integer32
_Hh3cNATPoolRefCounter_Object = MibTableColumn
hh3cNATPoolRefCounter = _Hh3cNATPoolRefCounter_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 1, 1, 5),
    _Hh3cNATPoolRefCounter_Type()
)
hh3cNATPoolRefCounter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATPoolRefCounter.setStatus("current")
_Hh3cNATPoolRowStatus_Type = RowStatus
_Hh3cNATPoolRowStatus_Object = MibTableColumn
hh3cNATPoolRowStatus = _Hh3cNATPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 1, 1, 6),
    _Hh3cNATPoolRowStatus_Type()
)
hh3cNATPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATPoolRowStatus.setStatus("current")
_Hh3cNATOutboundTable_Object = MibTable
hh3cNATOutboundTable = _Hh3cNATOutboundTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cNATOutboundTable.setStatus("current")
_Hh3cNATOutboundEntry_Object = MibTableRow
hh3cNATOutboundEntry = _Hh3cNATOutboundEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 2, 1)
)
hh3cNATOutboundEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-NAT-MIB", "hh3cNATOutboundAclNo"),
)
if mibBuilder.loadTexts:
    hh3cNATOutboundEntry.setStatus("current")


class _Hh3cNATOutboundAclNo_Type(Integer32):
    """Custom type hh3cNATOutboundAclNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 3999),
    )


_Hh3cNATOutboundAclNo_Type.__name__ = "Integer32"
_Hh3cNATOutboundAclNo_Object = MibTableColumn
hh3cNATOutboundAclNo = _Hh3cNATOutboundAclNo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 2, 1, 1),
    _Hh3cNATOutboundAclNo_Type()
)
hh3cNATOutboundAclNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATOutboundAclNo.setStatus("current")


class _Hh3cNATOutboundPoolIdx_Type(Integer32):
    """Custom type hh3cNATOutboundPoolIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 320),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Hh3cNATOutboundPoolIdx_Type.__name__ = "Integer32"
_Hh3cNATOutboundPoolIdx_Object = MibTableColumn
hh3cNATOutboundPoolIdx = _Hh3cNATOutboundPoolIdx_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 2, 1, 2),
    _Hh3cNATOutboundPoolIdx_Type()
)
hh3cNATOutboundPoolIdx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATOutboundPoolIdx.setStatus("current")


class _Hh3cNATOutboundIsNoPat_Type(Integer32):
    """Custom type hh3cNATOutboundIsNoPat based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_Hh3cNATOutboundIsNoPat_Type.__name__ = "Integer32"
_Hh3cNATOutboundIsNoPat_Object = MibTableColumn
hh3cNATOutboundIsNoPat = _Hh3cNATOutboundIsNoPat_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 2, 1, 3),
    _Hh3cNATOutboundIsNoPat_Type()
)
hh3cNATOutboundIsNoPat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATOutboundIsNoPat.setStatus("current")


class _Hh3cNATOutboundSlotNo_Type(Integer32):
    """Custom type hh3cNATOutboundSlotNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
        ValueRangeConstraint(255, 255),
    )


_Hh3cNATOutboundSlotNo_Type.__name__ = "Integer32"
_Hh3cNATOutboundSlotNo_Object = MibTableColumn
hh3cNATOutboundSlotNo = _Hh3cNATOutboundSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 2, 1, 4),
    _Hh3cNATOutboundSlotNo_Type()
)
hh3cNATOutboundSlotNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATOutboundSlotNo.setStatus("current")
_Hh3cNATOutboundRowStatus_Type = RowStatus
_Hh3cNATOutboundRowStatus_Object = MibTableColumn
hh3cNATOutboundRowStatus = _Hh3cNATOutboundRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 2, 1, 5),
    _Hh3cNATOutboundRowStatus_Type()
)
hh3cNATOutboundRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATOutboundRowStatus.setStatus("current")
_Hh3cNATServerTable_Object = MibTable
hh3cNATServerTable = _Hh3cNATServerTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cNATServerTable.setStatus("current")
_Hh3cNATServerEntry_Object = MibTableRow
hh3cNATServerEntry = _Hh3cNATServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 3, 1)
)
hh3cNATServerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-NAT-MIB", "hh3cNATServerProType"),
    (0, "HH3C-NAT-MIB", "hh3cNATServerGlobalIP"),
    (0, "HH3C-NAT-MIB", "hh3cNATServerStartGlobalPort"),
    (0, "HH3C-NAT-MIB", "hh3cNATServerVpnIndex"),
)
if mibBuilder.loadTexts:
    hh3cNATServerEntry.setStatus("current")


class _Hh3cNATServerProType_Type(Integer32):
    """Custom type hh3cNATServerProType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Hh3cNATServerProType_Type.__name__ = "Integer32"
_Hh3cNATServerProType_Object = MibTableColumn
hh3cNATServerProType = _Hh3cNATServerProType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 3, 1, 1),
    _Hh3cNATServerProType_Type()
)
hh3cNATServerProType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATServerProType.setStatus("current")
_Hh3cNATServerGlobalIP_Type = IpAddress
_Hh3cNATServerGlobalIP_Object = MibTableColumn
hh3cNATServerGlobalIP = _Hh3cNATServerGlobalIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 3, 1, 2),
    _Hh3cNATServerGlobalIP_Type()
)
hh3cNATServerGlobalIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATServerGlobalIP.setStatus("current")


class _Hh3cNATServerStartGlobalPort_Type(Integer32):
    """Custom type hh3cNATServerStartGlobalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cNATServerStartGlobalPort_Type.__name__ = "Integer32"
_Hh3cNATServerStartGlobalPort_Object = MibTableColumn
hh3cNATServerStartGlobalPort = _Hh3cNATServerStartGlobalPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 3, 1, 3),
    _Hh3cNATServerStartGlobalPort_Type()
)
hh3cNATServerStartGlobalPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATServerStartGlobalPort.setStatus("current")


class _Hh3cNATServerEndGlobalPort_Type(Integer32):
    """Custom type hh3cNATServerEndGlobalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cNATServerEndGlobalPort_Type.__name__ = "Integer32"
_Hh3cNATServerEndGlobalPort_Object = MibTableColumn
hh3cNATServerEndGlobalPort = _Hh3cNATServerEndGlobalPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 3, 1, 4),
    _Hh3cNATServerEndGlobalPort_Type()
)
hh3cNATServerEndGlobalPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATServerEndGlobalPort.setStatus("current")
_Hh3cNATServerStartInsideIP_Type = IpAddress
_Hh3cNATServerStartInsideIP_Object = MibTableColumn
hh3cNATServerStartInsideIP = _Hh3cNATServerStartInsideIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 3, 1, 5),
    _Hh3cNATServerStartInsideIP_Type()
)
hh3cNATServerStartInsideIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATServerStartInsideIP.setStatus("current")
_Hh3cNATServerEndInsideIP_Type = IpAddress
_Hh3cNATServerEndInsideIP_Object = MibTableColumn
hh3cNATServerEndInsideIP = _Hh3cNATServerEndInsideIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 3, 1, 6),
    _Hh3cNATServerEndInsideIP_Type()
)
hh3cNATServerEndInsideIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATServerEndInsideIP.setStatus("current")


class _Hh3cNATServerInsidePort_Type(Integer32):
    """Custom type hh3cNATServerInsidePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cNATServerInsidePort_Type.__name__ = "Integer32"
_Hh3cNATServerInsidePort_Object = MibTableColumn
hh3cNATServerInsidePort = _Hh3cNATServerInsidePort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 3, 1, 7),
    _Hh3cNATServerInsidePort_Type()
)
hh3cNATServerInsidePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATServerInsidePort.setStatus("current")


class _Hh3cNATServerSlotNo_Type(Integer32):
    """Custom type hh3cNATServerSlotNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
        ValueRangeConstraint(255, 255),
    )


_Hh3cNATServerSlotNo_Type.__name__ = "Integer32"
_Hh3cNATServerSlotNo_Object = MibTableColumn
hh3cNATServerSlotNo = _Hh3cNATServerSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 3, 1, 8),
    _Hh3cNATServerSlotNo_Type()
)
hh3cNATServerSlotNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATServerSlotNo.setStatus("current")


class _Hh3cNATServerVpnIndex_Type(Integer32):
    """Custom type hh3cNATServerVpnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cNATServerVpnIndex_Type.__name__ = "Integer32"
_Hh3cNATServerVpnIndex_Object = MibTableColumn
hh3cNATServerVpnIndex = _Hh3cNATServerVpnIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 3, 1, 10),
    _Hh3cNATServerVpnIndex_Type()
)
hh3cNATServerVpnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATServerVpnIndex.setStatus("current")


class _Hh3cNATServerAclNumber_Type(Integer32):
    """Custom type hh3cNATServerAclNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_Hh3cNATServerAclNumber_Type.__name__ = "Integer32"
_Hh3cNATServerAclNumber_Object = MibTableColumn
hh3cNATServerAclNumber = _Hh3cNATServerAclNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 3, 1, 11),
    _Hh3cNATServerAclNumber_Type()
)
hh3cNATServerAclNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATServerAclNumber.setStatus("current")
_Hh3cNATServerRowStatus_Type = RowStatus
_Hh3cNATServerRowStatus_Object = MibTableColumn
hh3cNATServerRowStatus = _Hh3cNATServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 3, 1, 12),
    _Hh3cNATServerRowStatus_Type()
)
hh3cNATServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATServerRowStatus.setStatus("current")
_Hh3cNATTimeOutTable_Object = MibTable
hh3cNATTimeOutTable = _Hh3cNATTimeOutTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 4)
)
if mibBuilder.loadTexts:
    hh3cNATTimeOutTable.setStatus("current")
_Hh3cNATTimeOutEntry_Object = MibTableRow
hh3cNATTimeOutEntry = _Hh3cNATTimeOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 4, 1)
)
hh3cNATTimeOutEntry.setIndexNames(
    (0, "HH3C-NAT-MIB", "hh3cNATTimeOutProtocol"),
)
if mibBuilder.loadTexts:
    hh3cNATTimeOutEntry.setStatus("current")


class _Hh3cNATTimeOutProtocol_Type(Integer32):
    """Custom type hh3cNATTimeOutProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("dns", 5),
          ("ftpCtrl", 8),
          ("ftpData", 9),
          ("icmp", 3),
          ("pptp", 4),
          ("tcp", 1),
          ("tcpFin", 6),
          ("tcpSyn", 7),
          ("udp", 2))
    )


_Hh3cNATTimeOutProtocol_Type.__name__ = "Integer32"
_Hh3cNATTimeOutProtocol_Object = MibTableColumn
hh3cNATTimeOutProtocol = _Hh3cNATTimeOutProtocol_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 4, 1, 1),
    _Hh3cNATTimeOutProtocol_Type()
)
hh3cNATTimeOutProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATTimeOutProtocol.setStatus("current")


class _Hh3cNATTimeOutTimeValue_Type(Integer32):
    """Custom type hh3cNATTimeOutTimeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 86400),
    )


_Hh3cNATTimeOutTimeValue_Type.__name__ = "Integer32"
_Hh3cNATTimeOutTimeValue_Object = MibTableColumn
hh3cNATTimeOutTimeValue = _Hh3cNATTimeOutTimeValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 4, 1, 2),
    _Hh3cNATTimeOutTimeValue_Type()
)
hh3cNATTimeOutTimeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNATTimeOutTimeValue.setStatus("current")
_Hh3cNATBLEnableTable_Object = MibTable
hh3cNATBLEnableTable = _Hh3cNATBLEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 5)
)
if mibBuilder.loadTexts:
    hh3cNATBLEnableTable.setStatus("current")
_Hh3cNATBLEnableEntry_Object = MibTableRow
hh3cNATBLEnableEntry = _Hh3cNATBLEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 5, 1)
)
hh3cNATBLEnableEntry.setIndexNames(
    (0, "HH3C-NAT-MIB", "hh3cNATBLEnableSlotNo"),
)
if mibBuilder.loadTexts:
    hh3cNATBLEnableEntry.setStatus("current")


class _Hh3cNATBLEnableSlotNo_Type(Integer32):
    """Custom type hh3cNATBLEnableSlotNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
        ValueRangeConstraint(255, 255),
    )


_Hh3cNATBLEnableSlotNo_Type.__name__ = "Integer32"
_Hh3cNATBLEnableSlotNo_Object = MibTableColumn
hh3cNATBLEnableSlotNo = _Hh3cNATBLEnableSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 5, 1, 1),
    _Hh3cNATBLEnableSlotNo_Type()
)
hh3cNATBLEnableSlotNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATBLEnableSlotNo.setStatus("current")


class _Hh3cNATBLEnable_Type(Integer32):
    """Custom type hh3cNATBLEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_Hh3cNATBLEnable_Type.__name__ = "Integer32"
_Hh3cNATBLEnable_Object = MibTableColumn
hh3cNATBLEnable = _Hh3cNATBLEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 5, 1, 2),
    _Hh3cNATBLEnable_Type()
)
hh3cNATBLEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNATBLEnable.setStatus("current")
_Hh3cNATBLIPConnectLimitParaTable_Object = MibTable
hh3cNATBLIPConnectLimitParaTable = _Hh3cNATBLIPConnectLimitParaTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 6)
)
if mibBuilder.loadTexts:
    hh3cNATBLIPConnectLimitParaTable.setStatus("current")
_Hh3cNATBLIPConnectLimitParaEntry_Object = MibTableRow
hh3cNATBLIPConnectLimitParaEntry = _Hh3cNATBLIPConnectLimitParaEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 6, 1)
)
hh3cNATBLIPConnectLimitParaEntry.setIndexNames(
    (0, "HH3C-NAT-MIB", "hh3cNATBLIPConnectLimitParaIP"),
)
if mibBuilder.loadTexts:
    hh3cNATBLIPConnectLimitParaEntry.setStatus("current")
_Hh3cNATBLIPConnectLimitParaIP_Type = IpAddress
_Hh3cNATBLIPConnectLimitParaIP_Object = MibTableColumn
hh3cNATBLIPConnectLimitParaIP = _Hh3cNATBLIPConnectLimitParaIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 6, 1, 1),
    _Hh3cNATBLIPConnectLimitParaIP_Type()
)
hh3cNATBLIPConnectLimitParaIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATBLIPConnectLimitParaIP.setStatus("current")


class _Hh3cNATBLIPConnectHighValue_Type(Integer32):
    """Custom type hh3cNATBLIPConnectHighValue based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 20000),
    )


_Hh3cNATBLIPConnectHighValue_Type.__name__ = "Integer32"
_Hh3cNATBLIPConnectHighValue_Object = MibTableColumn
hh3cNATBLIPConnectHighValue = _Hh3cNATBLIPConnectHighValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 6, 1, 2),
    _Hh3cNATBLIPConnectHighValue_Type()
)
hh3cNATBLIPConnectHighValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATBLIPConnectHighValue.setStatus("current")


class _Hh3cNATBLIPConnectLowValue_Type(Integer32):
    """Custom type hh3cNATBLIPConnectLowValue based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 20000),
    )


_Hh3cNATBLIPConnectLowValue_Type.__name__ = "Integer32"
_Hh3cNATBLIPConnectLowValue_Object = MibTableColumn
hh3cNATBLIPConnectLowValue = _Hh3cNATBLIPConnectLowValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 6, 1, 3),
    _Hh3cNATBLIPConnectLowValue_Type()
)
hh3cNATBLIPConnectLowValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATBLIPConnectLowValue.setStatus("current")


class _Hh3cNATBLIPUseSpecialConnectRate_Type(Integer32):
    """Custom type hh3cNATBLIPUseSpecialConnectRate based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_Hh3cNATBLIPUseSpecialConnectRate_Type.__name__ = "Integer32"
_Hh3cNATBLIPUseSpecialConnectRate_Object = MibTableColumn
hh3cNATBLIPUseSpecialConnectRate = _Hh3cNATBLIPUseSpecialConnectRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 6, 1, 4),
    _Hh3cNATBLIPUseSpecialConnectRate_Type()
)
hh3cNATBLIPUseSpecialConnectRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATBLIPUseSpecialConnectRate.setStatus("current")
_Hh3cNATBLIPConnectLimitRowStatus_Type = RowStatus
_Hh3cNATBLIPConnectLimitRowStatus_Object = MibTableColumn
hh3cNATBLIPConnectLimitRowStatus = _Hh3cNATBLIPConnectLimitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 6, 1, 5),
    _Hh3cNATBLIPConnectLimitRowStatus_Type()
)
hh3cNATBLIPConnectLimitRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATBLIPConnectLimitRowStatus.setStatus("current")
_Hh3cNATBLManagerTable_Object = MibTable
hh3cNATBLManagerTable = _Hh3cNATBLManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 7)
)
if mibBuilder.loadTexts:
    hh3cNATBLManagerTable.setStatus("current")
_Hh3cNATBLManagerEntry_Object = MibTableRow
hh3cNATBLManagerEntry = _Hh3cNATBLManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 7, 1)
)
hh3cNATBLManagerEntry.setIndexNames(
    (0, "HH3C-NAT-MIB", "hh3cNATBLIpAdress"),
    (0, "HH3C-NAT-MIB", "hh3cNATBLSlotNo"),
)
if mibBuilder.loadTexts:
    hh3cNATBLManagerEntry.setStatus("current")
_Hh3cNATBLIpAdress_Type = IpAddress
_Hh3cNATBLIpAdress_Object = MibTableColumn
hh3cNATBLIpAdress = _Hh3cNATBLIpAdress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 7, 1, 1),
    _Hh3cNATBLIpAdress_Type()
)
hh3cNATBLIpAdress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATBLIpAdress.setStatus("current")


class _Hh3cNATBLSlotNo_Type(Integer32):
    """Custom type hh3cNATBLSlotNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_Hh3cNATBLSlotNo_Type.__name__ = "Integer32"
_Hh3cNATBLSlotNo_Object = MibTableColumn
hh3cNATBLSlotNo = _Hh3cNATBLSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 7, 1, 2),
    _Hh3cNATBLSlotNo_Type()
)
hh3cNATBLSlotNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATBLSlotNo.setStatus("current")
_Hh3cNATBLConSum_Type = Integer32
_Hh3cNATBLConSum_Object = MibTableColumn
hh3cNATBLConSum = _Hh3cNATBLConSum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 7, 1, 3),
    _Hh3cNATBLConSum_Type()
)
hh3cNATBLConSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATBLConSum.setStatus("current")


class _Hh3cNATBLConSpd_Type(Integer32):
    """Custom type hh3cNATBLConSpd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("green", 3),
          ("red", 1),
          ("yellow", 2))
    )


_Hh3cNATBLConSpd_Type.__name__ = "Integer32"
_Hh3cNATBLConSpd_Object = MibTableColumn
hh3cNATBLConSpd = _Hh3cNATBLConSpd_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 7, 1, 4),
    _Hh3cNATBLConSpd_Type()
)
hh3cNATBLConSpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATBLConSpd.setStatus("current")
_Hh3cNATStatTable_Object = MibTable
hh3cNATStatTable = _Hh3cNATStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 8)
)
if mibBuilder.loadTexts:
    hh3cNATStatTable.setStatus("current")
_Hh3cNATStatEntry_Object = MibTableRow
hh3cNATStatEntry = _Hh3cNATStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 8, 1)
)
hh3cNATStatEntry.setIndexNames(
    (0, "HH3C-NAT-MIB", "hh3cNATStatNATBoardNo"),
)
if mibBuilder.loadTexts:
    hh3cNATStatEntry.setStatus("current")


class _Hh3cNATStatNATBoardNo_Type(Integer32):
    """Custom type hh3cNATStatNATBoardNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
        ValueRangeConstraint(255, 255),
    )


_Hh3cNATStatNATBoardNo_Type.__name__ = "Integer32"
_Hh3cNATStatNATBoardNo_Object = MibTableColumn
hh3cNATStatNATBoardNo = _Hh3cNATStatNATBoardNo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 8, 1, 1),
    _Hh3cNATStatNATBoardNo_Type()
)
hh3cNATStatNATBoardNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATStatNATBoardNo.setStatus("current")
_Hh3cNATStatActiveTblCount_Type = Counter32
_Hh3cNATStatActiveTblCount_Object = MibTableColumn
hh3cNATStatActiveTblCount = _Hh3cNATStatActiveTblCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 8, 1, 2),
    _Hh3cNATStatActiveTblCount_Type()
)
hh3cNATStatActiveTblCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATStatActiveTblCount.setStatus("current")
_Hh3cNATStatActiveTblCountInNP_Type = Counter32
_Hh3cNATStatActiveTblCountInNP_Object = MibTableColumn
hh3cNATStatActiveTblCountInNP = _Hh3cNATStatActiveTblCountInNP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 8, 1, 3),
    _Hh3cNATStatActiveTblCountInNP_Type()
)
hh3cNATStatActiveTblCountInNP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATStatActiveTblCountInNP.setStatus("current")
_Hh3cNATStatActiveNatTblCount_Type = Counter32
_Hh3cNATStatActiveNatTblCount_Object = MibTableColumn
hh3cNATStatActiveNatTblCount = _Hh3cNATStatActiveNatTblCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 8, 1, 4),
    _Hh3cNATStatActiveNatTblCount_Type()
)
hh3cNATStatActiveNatTblCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATStatActiveNatTblCount.setStatus("current")
_Hh3cNATStatActiveSvrTblCount_Type = Counter32
_Hh3cNATStatActiveSvrTblCount_Object = MibTableColumn
hh3cNATStatActiveSvrTblCount = _Hh3cNATStatActiveSvrTblCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 8, 1, 5),
    _Hh3cNATStatActiveSvrTblCount_Type()
)
hh3cNATStatActiveSvrTblCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATStatActiveSvrTblCount.setStatus("current")
_Hh3cNATStatActivePoolTblCount_Type = Counter32
_Hh3cNATStatActivePoolTblCount_Object = MibTableColumn
hh3cNATStatActivePoolTblCount = _Hh3cNATStatActivePoolTblCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 8, 1, 6),
    _Hh3cNATStatActivePoolTblCount_Type()
)
hh3cNATStatActivePoolTblCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATStatActivePoolTblCount.setStatus("current")
_Hh3cNATStatNumOfUsedPort_Type = Counter32
_Hh3cNATStatNumOfUsedPort_Object = MibTableColumn
hh3cNATStatNumOfUsedPort = _Hh3cNATStatNumOfUsedPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 8, 1, 7),
    _Hh3cNATStatNumOfUsedPort_Type()
)
hh3cNATStatNumOfUsedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATStatNumOfUsedPort.setStatus("current")
_Hh3cNATStatNumOfGoodPkt_Type = Counter32
_Hh3cNATStatNumOfGoodPkt_Object = MibTableColumn
hh3cNATStatNumOfGoodPkt = _Hh3cNATStatNumOfGoodPkt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 8, 1, 8),
    _Hh3cNATStatNumOfGoodPkt_Type()
)
hh3cNATStatNumOfGoodPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATStatNumOfGoodPkt.setStatus("current")
_Hh3cNATStatNumOfBadPkt_Type = Counter32
_Hh3cNATStatNumOfBadPkt_Object = MibTableColumn
hh3cNATStatNumOfBadPkt = _Hh3cNATStatNumOfBadPkt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 8, 1, 9),
    _Hh3cNATStatNumOfBadPkt_Type()
)
hh3cNATStatNumOfBadPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATStatNumOfBadPkt.setStatus("current")
_Hh3cNATStaticSessionCount_Type = Integer32
_Hh3cNATStaticSessionCount_Object = MibTableColumn
hh3cNATStaticSessionCount = _Hh3cNATStaticSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 8, 1, 10),
    _Hh3cNATStaticSessionCount_Type()
)
hh3cNATStaticSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATStaticSessionCount.setStatus("current")
_Hh3cNATFragmentSessionCount_Type = Integer32
_Hh3cNATFragmentSessionCount_Object = MibTableColumn
hh3cNATFragmentSessionCount = _Hh3cNATFragmentSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 8, 1, 11),
    _Hh3cNATFragmentSessionCount_Type()
)
hh3cNATFragmentSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATFragmentSessionCount.setStatus("current")
_Hh3cNATSequenceSessionCount_Type = Integer32
_Hh3cNATSequenceSessionCount_Object = MibTableColumn
hh3cNATSequenceSessionCount = _Hh3cNATSequenceSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 8, 1, 12),
    _Hh3cNATSequenceSessionCount_Type()
)
hh3cNATSequenceSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATSequenceSessionCount.setStatus("current")
_Hh3cNATLogCount_Type = Integer32
_Hh3cNATLogCount_Object = MibTableColumn
hh3cNATLogCount = _Hh3cNATLogCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 8, 1, 13),
    _Hh3cNATLogCount_Type()
)
hh3cNATLogCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATLogCount.setStatus("current")
_Hh3cNATSessionTable_Object = MibTable
hh3cNATSessionTable = _Hh3cNATSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 9)
)
if mibBuilder.loadTexts:
    hh3cNATSessionTable.setStatus("current")
_Hh3cNATSessionEntry_Object = MibTableRow
hh3cNATSessionEntry = _Hh3cNATSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 9, 1)
)
hh3cNATSessionEntry.setIndexNames(
    (0, "HH3C-NAT-MIB", "hh3cNATSessionHashNumber"),
    (0, "HH3C-NAT-MIB", "hh3cNATSessionProtocol"),
    (0, "HH3C-NAT-MIB", "hh3cNATSessionInsideIP"),
    (0, "HH3C-NAT-MIB", "hh3cNATSessionInsidePort"),
    (0, "HH3C-NAT-MIB", "hh3cNATSessionPeerIP"),
    (0, "HH3C-NAT-MIB", "hh3cNATSessionPeerPort"),
    (0, "HH3C-NAT-MIB", "hh3cNATSessionVpnIndex"),
)
if mibBuilder.loadTexts:
    hh3cNATSessionEntry.setStatus("current")


class _Hh3cNATSessionHashNumber_Type(Integer32):
    """Custom type hh3cNATSessionHashNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300000),
    )


_Hh3cNATSessionHashNumber_Type.__name__ = "Integer32"
_Hh3cNATSessionHashNumber_Object = MibTableColumn
hh3cNATSessionHashNumber = _Hh3cNATSessionHashNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 9, 1, 1),
    _Hh3cNATSessionHashNumber_Type()
)
hh3cNATSessionHashNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATSessionHashNumber.setStatus("current")


class _Hh3cNATSessionProtocol_Type(Integer32):
    """Custom type hh3cNATSessionProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Hh3cNATSessionProtocol_Type.__name__ = "Integer32"
_Hh3cNATSessionProtocol_Object = MibTableColumn
hh3cNATSessionProtocol = _Hh3cNATSessionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 9, 1, 2),
    _Hh3cNATSessionProtocol_Type()
)
hh3cNATSessionProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATSessionProtocol.setStatus("current")
_Hh3cNATSessionGlobalIP_Type = IpAddress
_Hh3cNATSessionGlobalIP_Object = MibTableColumn
hh3cNATSessionGlobalIP = _Hh3cNATSessionGlobalIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 9, 1, 3),
    _Hh3cNATSessionGlobalIP_Type()
)
hh3cNATSessionGlobalIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATSessionGlobalIP.setStatus("current")


class _Hh3cNATSessionGlobalPort_Type(Integer32):
    """Custom type hh3cNATSessionGlobalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cNATSessionGlobalPort_Type.__name__ = "Integer32"
_Hh3cNATSessionGlobalPort_Object = MibTableColumn
hh3cNATSessionGlobalPort = _Hh3cNATSessionGlobalPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 9, 1, 4),
    _Hh3cNATSessionGlobalPort_Type()
)
hh3cNATSessionGlobalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATSessionGlobalPort.setStatus("current")
_Hh3cNATSessionInsideIP_Type = IpAddress
_Hh3cNATSessionInsideIP_Object = MibTableColumn
hh3cNATSessionInsideIP = _Hh3cNATSessionInsideIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 9, 1, 5),
    _Hh3cNATSessionInsideIP_Type()
)
hh3cNATSessionInsideIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATSessionInsideIP.setStatus("current")


class _Hh3cNATSessionInsidePort_Type(Integer32):
    """Custom type hh3cNATSessionInsidePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cNATSessionInsidePort_Type.__name__ = "Integer32"
_Hh3cNATSessionInsidePort_Object = MibTableColumn
hh3cNATSessionInsidePort = _Hh3cNATSessionInsidePort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 9, 1, 6),
    _Hh3cNATSessionInsidePort_Type()
)
hh3cNATSessionInsidePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATSessionInsidePort.setStatus("current")
_Hh3cNATSessionPeerIP_Type = IpAddress
_Hh3cNATSessionPeerIP_Object = MibTableColumn
hh3cNATSessionPeerIP = _Hh3cNATSessionPeerIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 9, 1, 7),
    _Hh3cNATSessionPeerIP_Type()
)
hh3cNATSessionPeerIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATSessionPeerIP.setStatus("current")


class _Hh3cNATSessionPeerPort_Type(Integer32):
    """Custom type hh3cNATSessionPeerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cNATSessionPeerPort_Type.__name__ = "Integer32"
_Hh3cNATSessionPeerPort_Object = MibTableColumn
hh3cNATSessionPeerPort = _Hh3cNATSessionPeerPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 9, 1, 8),
    _Hh3cNATSessionPeerPort_Type()
)
hh3cNATSessionPeerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATSessionPeerPort.setStatus("current")


class _Hh3cNATSessionVpnIndex_Type(Integer32):
    """Custom type hh3cNATSessionVpnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cNATSessionVpnIndex_Type.__name__ = "Integer32"
_Hh3cNATSessionVpnIndex_Object = MibTableColumn
hh3cNATSessionVpnIndex = _Hh3cNATSessionVpnIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 9, 1, 9),
    _Hh3cNATSessionVpnIndex_Type()
)
hh3cNATSessionVpnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATSessionVpnIndex.setStatus("current")
_Hh3cNATSessionTTL_Type = Integer32
_Hh3cNATSessionTTL_Object = MibTableColumn
hh3cNATSessionTTL = _Hh3cNATSessionTTL_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 9, 1, 10),
    _Hh3cNATSessionTTL_Type()
)
hh3cNATSessionTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATSessionTTL.setStatus("current")
_Hh3cNATSessionStatus_Type = Integer32
_Hh3cNATSessionStatus_Object = MibTableColumn
hh3cNATSessionStatus = _Hh3cNATSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 9, 1, 11),
    _Hh3cNATSessionStatus_Type()
)
hh3cNATSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATSessionStatus.setStatus("current")
_Hh3cNATSessionLeftTime_Type = TimeTicks
_Hh3cNATSessionLeftTime_Object = MibTableColumn
hh3cNATSessionLeftTime = _Hh3cNATSessionLeftTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 9, 1, 12),
    _Hh3cNATSessionLeftTime_Type()
)
hh3cNATSessionLeftTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATSessionLeftTime.setStatus("current")
_Hh3cNATStaticConfTable_Object = MibTable
hh3cNATStaticConfTable = _Hh3cNATStaticConfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 10)
)
if mibBuilder.loadTexts:
    hh3cNATStaticConfTable.setStatus("current")
_Hh3cNATStaticConfEntry_Object = MibTableRow
hh3cNATStaticConfEntry = _Hh3cNATStaticConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 10, 1)
)
hh3cNATStaticConfEntry.setIndexNames(
    (0, "HH3C-NAT-MIB", "hh3cNATStaticInsideIp"),
)
if mibBuilder.loadTexts:
    hh3cNATStaticConfEntry.setStatus("current")
_Hh3cNATStaticInsideIp_Type = IpAddress
_Hh3cNATStaticInsideIp_Object = MibTableColumn
hh3cNATStaticInsideIp = _Hh3cNATStaticInsideIp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 10, 1, 1),
    _Hh3cNATStaticInsideIp_Type()
)
hh3cNATStaticInsideIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATStaticInsideIp.setStatus("current")
_Hh3cNATStaticGlobalIp_Type = IpAddress
_Hh3cNATStaticGlobalIp_Object = MibTableColumn
hh3cNATStaticGlobalIp = _Hh3cNATStaticGlobalIp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 10, 1, 2),
    _Hh3cNATStaticGlobalIp_Type()
)
hh3cNATStaticGlobalIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATStaticGlobalIp.setStatus("current")
_Hh3cNATStaticRowStatus_Type = RowStatus
_Hh3cNATStaticRowStatus_Object = MibTableColumn
hh3cNATStaticRowStatus = _Hh3cNATStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 10, 1, 3),
    _Hh3cNATStaticRowStatus_Type()
)
hh3cNATStaticRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATStaticRowStatus.setStatus("current")
_Hh3cNATStaticEnableTable_Object = MibTable
hh3cNATStaticEnableTable = _Hh3cNATStaticEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 11)
)
if mibBuilder.loadTexts:
    hh3cNATStaticEnableTable.setStatus("current")
_Hh3cNATStaticEnableEntry_Object = MibTableRow
hh3cNATStaticEnableEntry = _Hh3cNATStaticEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 11, 1)
)
hh3cNATStaticEnableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cNATStaticEnableEntry.setStatus("current")


class _Hh3cNATStaticEnable_Type(Integer32):
    """Custom type hh3cNATStaticEnable based on Integer32"""
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


_Hh3cNATStaticEnable_Type.__name__ = "Integer32"
_Hh3cNATStaticEnable_Object = MibTableColumn
hh3cNATStaticEnable = _Hh3cNATStaticEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 11, 1, 2),
    _Hh3cNATStaticEnable_Type()
)
hh3cNATStaticEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNATStaticEnable.setStatus("current")
_Hh3cNATDnsMapTable_Object = MibTable
hh3cNATDnsMapTable = _Hh3cNATDnsMapTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 12)
)
if mibBuilder.loadTexts:
    hh3cNATDnsMapTable.setStatus("current")
_Hh3cNATDnsMapEntry_Object = MibTableRow
hh3cNATDnsMapEntry = _Hh3cNATDnsMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 12, 1)
)
hh3cNATDnsMapEntry.setIndexNames(
    (0, "HH3C-NAT-MIB", "hh3cNATDnsMapDomainName"),
)
if mibBuilder.loadTexts:
    hh3cNATDnsMapEntry.setStatus("current")
_Hh3cNATDnsMapDomainName_Type = DisplayString
_Hh3cNATDnsMapDomainName_Object = MibTableColumn
hh3cNATDnsMapDomainName = _Hh3cNATDnsMapDomainName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 12, 1, 1),
    _Hh3cNATDnsMapDomainName_Type()
)
hh3cNATDnsMapDomainName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATDnsMapDomainName.setStatus("current")
_Hh3cNATDnsMapGlobalIp_Type = IpAddress
_Hh3cNATDnsMapGlobalIp_Object = MibTableColumn
hh3cNATDnsMapGlobalIp = _Hh3cNATDnsMapGlobalIp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 12, 1, 2),
    _Hh3cNATDnsMapGlobalIp_Type()
)
hh3cNATDnsMapGlobalIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATDnsMapGlobalIp.setStatus("current")


class _Hh3cNATDnsMapGlobalPort_Type(Integer32):
    """Custom type hh3cNATDnsMapGlobalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cNATDnsMapGlobalPort_Type.__name__ = "Integer32"
_Hh3cNATDnsMapGlobalPort_Object = MibTableColumn
hh3cNATDnsMapGlobalPort = _Hh3cNATDnsMapGlobalPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 12, 1, 3),
    _Hh3cNATDnsMapGlobalPort_Type()
)
hh3cNATDnsMapGlobalPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATDnsMapGlobalPort.setStatus("current")


class _Hh3cNATDnsMapProtocolType_Type(Integer32):
    """Custom type hh3cNATDnsMapProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("typeTCP", 1),
          ("typeUDP", 2))
    )


_Hh3cNATDnsMapProtocolType_Type.__name__ = "Integer32"
_Hh3cNATDnsMapProtocolType_Object = MibTableColumn
hh3cNATDnsMapProtocolType = _Hh3cNATDnsMapProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 12, 1, 4),
    _Hh3cNATDnsMapProtocolType_Type()
)
hh3cNATDnsMapProtocolType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATDnsMapProtocolType.setStatus("current")
_Hh3cNATDnsMapLastUseTime_Type = TimeTicks
_Hh3cNATDnsMapLastUseTime_Object = MibTableColumn
hh3cNATDnsMapLastUseTime = _Hh3cNATDnsMapLastUseTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 12, 1, 5),
    _Hh3cNATDnsMapLastUseTime_Type()
)
hh3cNATDnsMapLastUseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATDnsMapLastUseTime.setStatus("current")
_Hh3cNATDnsMapRowStatus_Type = RowStatus
_Hh3cNATDnsMapRowStatus_Object = MibTableColumn
hh3cNATDnsMapRowStatus = _Hh3cNATDnsMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 12, 1, 6),
    _Hh3cNATDnsMapRowStatus_Type()
)
hh3cNATDnsMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATDnsMapRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-NAT-MIB",
    **{"hh3cNat": hh3cNat,
       "hh3cNATGlobalVars": hh3cNATGlobalVars,
       "hh3cNATClearSession": hh3cNATClearSession,
       "hh3cNATClearSessionSlotNo": hh3cNATClearSessionSlotNo,
       "hh3cNATBLConnectLimitPara": hh3cNATBLConnectLimitPara,
       "hh3cNATBLConnectHighValue": hh3cNATBLConnectHighValue,
       "hh3cNATBLConnectLowValue": hh3cNATBLConnectLowValue,
       "hh3cNATBLConnectHighRate": hh3cNATBLConnectHighRate,
       "hh3cNATBLConnectLowRate": hh3cNATBLConnectLowRate,
       "hh3cNATBLSpecialConnectHighRate": hh3cNATBLSpecialConnectHighRate,
       "hh3cNATBLSpecialConnectLowRate": hh3cNATBLSpecialConnectLowRate,
       "hh3cNATBLCtrlEnable": hh3cNATBLCtrlEnable,
       "hh3cNATBLConnectSumEnable": hh3cNATBLConnectSumEnable,
       "hh3cNATBLConnectRateEnable": hh3cNATBLConnectRateEnable,
       "hh3cNATNPTimer": hh3cNATNPTimer,
       "hh3cNATNPAgingTime": hh3cNATNPAgingTime,
       "hh3cNATMibObjects": hh3cNATMibObjects,
       "hh3cNATPoolInfoTable": hh3cNATPoolInfoTable,
       "hh3cNATPoolInfoEntry": hh3cNATPoolInfoEntry,
       "hh3cNATPoolIdx": hh3cNATPoolIdx,
       "hh3cNATPoolStartIpAddr": hh3cNATPoolStartIpAddr,
       "hh3cNATPoolEndIpAddr": hh3cNATPoolEndIpAddr,
       "hh3cNATPoolSlotNo": hh3cNATPoolSlotNo,
       "hh3cNATPoolRefCounter": hh3cNATPoolRefCounter,
       "hh3cNATPoolRowStatus": hh3cNATPoolRowStatus,
       "hh3cNATOutboundTable": hh3cNATOutboundTable,
       "hh3cNATOutboundEntry": hh3cNATOutboundEntry,
       "hh3cNATOutboundAclNo": hh3cNATOutboundAclNo,
       "hh3cNATOutboundPoolIdx": hh3cNATOutboundPoolIdx,
       "hh3cNATOutboundIsNoPat": hh3cNATOutboundIsNoPat,
       "hh3cNATOutboundSlotNo": hh3cNATOutboundSlotNo,
       "hh3cNATOutboundRowStatus": hh3cNATOutboundRowStatus,
       "hh3cNATServerTable": hh3cNATServerTable,
       "hh3cNATServerEntry": hh3cNATServerEntry,
       "hh3cNATServerProType": hh3cNATServerProType,
       "hh3cNATServerGlobalIP": hh3cNATServerGlobalIP,
       "hh3cNATServerStartGlobalPort": hh3cNATServerStartGlobalPort,
       "hh3cNATServerEndGlobalPort": hh3cNATServerEndGlobalPort,
       "hh3cNATServerStartInsideIP": hh3cNATServerStartInsideIP,
       "hh3cNATServerEndInsideIP": hh3cNATServerEndInsideIP,
       "hh3cNATServerInsidePort": hh3cNATServerInsidePort,
       "hh3cNATServerSlotNo": hh3cNATServerSlotNo,
       "hh3cNATServerVpnIndex": hh3cNATServerVpnIndex,
       "hh3cNATServerAclNumber": hh3cNATServerAclNumber,
       "hh3cNATServerRowStatus": hh3cNATServerRowStatus,
       "hh3cNATTimeOutTable": hh3cNATTimeOutTable,
       "hh3cNATTimeOutEntry": hh3cNATTimeOutEntry,
       "hh3cNATTimeOutProtocol": hh3cNATTimeOutProtocol,
       "hh3cNATTimeOutTimeValue": hh3cNATTimeOutTimeValue,
       "hh3cNATBLEnableTable": hh3cNATBLEnableTable,
       "hh3cNATBLEnableEntry": hh3cNATBLEnableEntry,
       "hh3cNATBLEnableSlotNo": hh3cNATBLEnableSlotNo,
       "hh3cNATBLEnable": hh3cNATBLEnable,
       "hh3cNATBLIPConnectLimitParaTable": hh3cNATBLIPConnectLimitParaTable,
       "hh3cNATBLIPConnectLimitParaEntry": hh3cNATBLIPConnectLimitParaEntry,
       "hh3cNATBLIPConnectLimitParaIP": hh3cNATBLIPConnectLimitParaIP,
       "hh3cNATBLIPConnectHighValue": hh3cNATBLIPConnectHighValue,
       "hh3cNATBLIPConnectLowValue": hh3cNATBLIPConnectLowValue,
       "hh3cNATBLIPUseSpecialConnectRate": hh3cNATBLIPUseSpecialConnectRate,
       "hh3cNATBLIPConnectLimitRowStatus": hh3cNATBLIPConnectLimitRowStatus,
       "hh3cNATBLManagerTable": hh3cNATBLManagerTable,
       "hh3cNATBLManagerEntry": hh3cNATBLManagerEntry,
       "hh3cNATBLIpAdress": hh3cNATBLIpAdress,
       "hh3cNATBLSlotNo": hh3cNATBLSlotNo,
       "hh3cNATBLConSum": hh3cNATBLConSum,
       "hh3cNATBLConSpd": hh3cNATBLConSpd,
       "hh3cNATStatTable": hh3cNATStatTable,
       "hh3cNATStatEntry": hh3cNATStatEntry,
       "hh3cNATStatNATBoardNo": hh3cNATStatNATBoardNo,
       "hh3cNATStatActiveTblCount": hh3cNATStatActiveTblCount,
       "hh3cNATStatActiveTblCountInNP": hh3cNATStatActiveTblCountInNP,
       "hh3cNATStatActiveNatTblCount": hh3cNATStatActiveNatTblCount,
       "hh3cNATStatActiveSvrTblCount": hh3cNATStatActiveSvrTblCount,
       "hh3cNATStatActivePoolTblCount": hh3cNATStatActivePoolTblCount,
       "hh3cNATStatNumOfUsedPort": hh3cNATStatNumOfUsedPort,
       "hh3cNATStatNumOfGoodPkt": hh3cNATStatNumOfGoodPkt,
       "hh3cNATStatNumOfBadPkt": hh3cNATStatNumOfBadPkt,
       "hh3cNATStaticSessionCount": hh3cNATStaticSessionCount,
       "hh3cNATFragmentSessionCount": hh3cNATFragmentSessionCount,
       "hh3cNATSequenceSessionCount": hh3cNATSequenceSessionCount,
       "hh3cNATLogCount": hh3cNATLogCount,
       "hh3cNATSessionTable": hh3cNATSessionTable,
       "hh3cNATSessionEntry": hh3cNATSessionEntry,
       "hh3cNATSessionHashNumber": hh3cNATSessionHashNumber,
       "hh3cNATSessionProtocol": hh3cNATSessionProtocol,
       "hh3cNATSessionGlobalIP": hh3cNATSessionGlobalIP,
       "hh3cNATSessionGlobalPort": hh3cNATSessionGlobalPort,
       "hh3cNATSessionInsideIP": hh3cNATSessionInsideIP,
       "hh3cNATSessionInsidePort": hh3cNATSessionInsidePort,
       "hh3cNATSessionPeerIP": hh3cNATSessionPeerIP,
       "hh3cNATSessionPeerPort": hh3cNATSessionPeerPort,
       "hh3cNATSessionVpnIndex": hh3cNATSessionVpnIndex,
       "hh3cNATSessionTTL": hh3cNATSessionTTL,
       "hh3cNATSessionStatus": hh3cNATSessionStatus,
       "hh3cNATSessionLeftTime": hh3cNATSessionLeftTime,
       "hh3cNATStaticConfTable": hh3cNATStaticConfTable,
       "hh3cNATStaticConfEntry": hh3cNATStaticConfEntry,
       "hh3cNATStaticInsideIp": hh3cNATStaticInsideIp,
       "hh3cNATStaticGlobalIp": hh3cNATStaticGlobalIp,
       "hh3cNATStaticRowStatus": hh3cNATStaticRowStatus,
       "hh3cNATStaticEnableTable": hh3cNATStaticEnableTable,
       "hh3cNATStaticEnableEntry": hh3cNATStaticEnableEntry,
       "hh3cNATStaticEnable": hh3cNATStaticEnable,
       "hh3cNATDnsMapTable": hh3cNATDnsMapTable,
       "hh3cNATDnsMapEntry": hh3cNATDnsMapEntry,
       "hh3cNATDnsMapDomainName": hh3cNATDnsMapDomainName,
       "hh3cNATDnsMapGlobalIp": hh3cNATDnsMapGlobalIp,
       "hh3cNATDnsMapGlobalPort": hh3cNATDnsMapGlobalPort,
       "hh3cNATDnsMapProtocolType": hh3cNATDnsMapProtocolType,
       "hh3cNATDnsMapLastUseTime": hh3cNATDnsMapLastUseTime,
       "hh3cNATDnsMapRowStatus": hh3cNATDnsMapRowStatus}
)
