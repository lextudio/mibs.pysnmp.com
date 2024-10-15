# SNMP MIB module (H3C-NAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-NAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:51:01 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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

h3cNat = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18)
)
h3cNat.setRevisions(
        ("2005-01-20 15:18",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cNATGlobalVars_ObjectIdentity = ObjectIdentity
h3cNATGlobalVars = _H3cNATGlobalVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 1)
)
_H3cNATClearSession_ObjectIdentity = ObjectIdentity
h3cNATClearSession = _H3cNATClearSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 1, 1)
)


class _H3cNATClearSessionSlotNo_Type(Integer32):
    """Custom type h3cNATClearSessionSlotNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
        ValueRangeConstraint(255, 255),
    )


_H3cNATClearSessionSlotNo_Type.__name__ = "Integer32"
_H3cNATClearSessionSlotNo_Object = MibScalar
h3cNATClearSessionSlotNo = _H3cNATClearSessionSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 1, 1, 1),
    _H3cNATClearSessionSlotNo_Type()
)
h3cNATClearSessionSlotNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cNATClearSessionSlotNo.setStatus("current")
_H3cNATBLConnectLimitPara_ObjectIdentity = ObjectIdentity
h3cNATBLConnectLimitPara = _H3cNATBLConnectLimitPara_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 1, 2)
)


class _H3cNATBLConnectHighValue_Type(Integer32):
    """Custom type h3cNATBLConnectHighValue based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 20000),
    )


_H3cNATBLConnectHighValue_Type.__name__ = "Integer32"
_H3cNATBLConnectHighValue_Object = MibScalar
h3cNATBLConnectHighValue = _H3cNATBLConnectHighValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 1, 2, 1),
    _H3cNATBLConnectHighValue_Type()
)
h3cNATBLConnectHighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cNATBLConnectHighValue.setStatus("current")


class _H3cNATBLConnectLowValue_Type(Integer32):
    """Custom type h3cNATBLConnectLowValue based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 20000),
    )


_H3cNATBLConnectLowValue_Type.__name__ = "Integer32"
_H3cNATBLConnectLowValue_Object = MibScalar
h3cNATBLConnectLowValue = _H3cNATBLConnectLowValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 1, 2, 2),
    _H3cNATBLConnectLowValue_Type()
)
h3cNATBLConnectLowValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cNATBLConnectLowValue.setStatus("current")


class _H3cNATBLConnectHighRate_Type(Integer32):
    """Custom type h3cNATBLConnectHighRate based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 21474836),
    )


_H3cNATBLConnectHighRate_Type.__name__ = "Integer32"
_H3cNATBLConnectHighRate_Object = MibScalar
h3cNATBLConnectHighRate = _H3cNATBLConnectHighRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 1, 2, 3),
    _H3cNATBLConnectHighRate_Type()
)
h3cNATBLConnectHighRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cNATBLConnectHighRate.setStatus("current")


class _H3cNATBLConnectLowRate_Type(Integer32):
    """Custom type h3cNATBLConnectLowRate based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 21474836),
    )


_H3cNATBLConnectLowRate_Type.__name__ = "Integer32"
_H3cNATBLConnectLowRate_Object = MibScalar
h3cNATBLConnectLowRate = _H3cNATBLConnectLowRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 1, 2, 4),
    _H3cNATBLConnectLowRate_Type()
)
h3cNATBLConnectLowRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cNATBLConnectLowRate.setStatus("current")


class _H3cNATBLSpecialConnectHighRate_Type(Integer32):
    """Custom type h3cNATBLSpecialConnectHighRate based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 21474836),
    )


_H3cNATBLSpecialConnectHighRate_Type.__name__ = "Integer32"
_H3cNATBLSpecialConnectHighRate_Object = MibScalar
h3cNATBLSpecialConnectHighRate = _H3cNATBLSpecialConnectHighRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 1, 2, 5),
    _H3cNATBLSpecialConnectHighRate_Type()
)
h3cNATBLSpecialConnectHighRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cNATBLSpecialConnectHighRate.setStatus("current")


class _H3cNATBLSpecialConnectLowRate_Type(Integer32):
    """Custom type h3cNATBLSpecialConnectLowRate based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 21474836),
    )


_H3cNATBLSpecialConnectLowRate_Type.__name__ = "Integer32"
_H3cNATBLSpecialConnectLowRate_Object = MibScalar
h3cNATBLSpecialConnectLowRate = _H3cNATBLSpecialConnectLowRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 1, 2, 6),
    _H3cNATBLSpecialConnectLowRate_Type()
)
h3cNATBLSpecialConnectLowRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cNATBLSpecialConnectLowRate.setStatus("current")
_H3cNATBLCtrlEnable_ObjectIdentity = ObjectIdentity
h3cNATBLCtrlEnable = _H3cNATBLCtrlEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 1, 3)
)


class _H3cNATBLConnectSumEnable_Type(Integer32):
    """Custom type h3cNATBLConnectSumEnable based on Integer32"""
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


_H3cNATBLConnectSumEnable_Type.__name__ = "Integer32"
_H3cNATBLConnectSumEnable_Object = MibScalar
h3cNATBLConnectSumEnable = _H3cNATBLConnectSumEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 1, 3, 1),
    _H3cNATBLConnectSumEnable_Type()
)
h3cNATBLConnectSumEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cNATBLConnectSumEnable.setStatus("current")


class _H3cNATBLConnectRateEnable_Type(Integer32):
    """Custom type h3cNATBLConnectRateEnable based on Integer32"""
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


_H3cNATBLConnectRateEnable_Type.__name__ = "Integer32"
_H3cNATBLConnectRateEnable_Object = MibScalar
h3cNATBLConnectRateEnable = _H3cNATBLConnectRateEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 1, 3, 2),
    _H3cNATBLConnectRateEnable_Type()
)
h3cNATBLConnectRateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cNATBLConnectRateEnable.setStatus("current")
_H3cNATNPTimer_ObjectIdentity = ObjectIdentity
h3cNATNPTimer = _H3cNATNPTimer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 1, 4)
)


class _H3cNATNPAgingTime_Type(Integer32):
    """Custom type h3cNATNPAgingTime based on Integer32"""
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


_H3cNATNPAgingTime_Type.__name__ = "Integer32"
_H3cNATNPAgingTime_Object = MibScalar
h3cNATNPAgingTime = _H3cNATNPAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 1, 4, 1),
    _H3cNATNPAgingTime_Type()
)
h3cNATNPAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cNATNPAgingTime.setStatus("current")
_H3cNATMibObjects_ObjectIdentity = ObjectIdentity
h3cNATMibObjects = _H3cNATMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2)
)
_H3cNATPoolInfoTable_Object = MibTable
h3cNATPoolInfoTable = _H3cNATPoolInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 1)
)
if mibBuilder.loadTexts:
    h3cNATPoolInfoTable.setStatus("current")
_H3cNATPoolInfoEntry_Object = MibTableRow
h3cNATPoolInfoEntry = _H3cNATPoolInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 1, 1)
)
h3cNATPoolInfoEntry.setIndexNames(
    (0, "H3C-NAT-MIB", "h3cNATPoolIdx"),
)
if mibBuilder.loadTexts:
    h3cNATPoolInfoEntry.setStatus("current")


class _H3cNATPoolIdx_Type(Integer32):
    """Custom type h3cNATPoolIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 320),
    )


_H3cNATPoolIdx_Type.__name__ = "Integer32"
_H3cNATPoolIdx_Object = MibTableColumn
h3cNATPoolIdx = _H3cNATPoolIdx_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 1, 1, 1),
    _H3cNATPoolIdx_Type()
)
h3cNATPoolIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cNATPoolIdx.setStatus("current")
_H3cNATPoolStartIpAddr_Type = IpAddress
_H3cNATPoolStartIpAddr_Object = MibTableColumn
h3cNATPoolStartIpAddr = _H3cNATPoolStartIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 1, 1, 2),
    _H3cNATPoolStartIpAddr_Type()
)
h3cNATPoolStartIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cNATPoolStartIpAddr.setStatus("current")
_H3cNATPoolEndIpAddr_Type = IpAddress
_H3cNATPoolEndIpAddr_Object = MibTableColumn
h3cNATPoolEndIpAddr = _H3cNATPoolEndIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 1, 1, 3),
    _H3cNATPoolEndIpAddr_Type()
)
h3cNATPoolEndIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cNATPoolEndIpAddr.setStatus("current")


class _H3cNATPoolSlotNo_Type(Integer32):
    """Custom type h3cNATPoolSlotNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
        ValueRangeConstraint(255, 255),
    )


_H3cNATPoolSlotNo_Type.__name__ = "Integer32"
_H3cNATPoolSlotNo_Object = MibTableColumn
h3cNATPoolSlotNo = _H3cNATPoolSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 1, 1, 4),
    _H3cNATPoolSlotNo_Type()
)
h3cNATPoolSlotNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cNATPoolSlotNo.setStatus("current")
_H3cNATPoolRefCounter_Type = Integer32
_H3cNATPoolRefCounter_Object = MibTableColumn
h3cNATPoolRefCounter = _H3cNATPoolRefCounter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 1, 1, 5),
    _H3cNATPoolRefCounter_Type()
)
h3cNATPoolRefCounter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cNATPoolRefCounter.setStatus("current")
_H3cNATPoolRowStatus_Type = RowStatus
_H3cNATPoolRowStatus_Object = MibTableColumn
h3cNATPoolRowStatus = _H3cNATPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 1, 1, 6),
    _H3cNATPoolRowStatus_Type()
)
h3cNATPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cNATPoolRowStatus.setStatus("current")
_H3cNATOutboundTable_Object = MibTable
h3cNATOutboundTable = _H3cNATOutboundTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 2)
)
if mibBuilder.loadTexts:
    h3cNATOutboundTable.setStatus("current")
_H3cNATOutboundEntry_Object = MibTableRow
h3cNATOutboundEntry = _H3cNATOutboundEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 2, 1)
)
h3cNATOutboundEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "H3C-NAT-MIB", "h3cNATOutboundAclNo"),
)
if mibBuilder.loadTexts:
    h3cNATOutboundEntry.setStatus("current")


class _H3cNATOutboundAclNo_Type(Integer32):
    """Custom type h3cNATOutboundAclNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 3999),
    )


_H3cNATOutboundAclNo_Type.__name__ = "Integer32"
_H3cNATOutboundAclNo_Object = MibTableColumn
h3cNATOutboundAclNo = _H3cNATOutboundAclNo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 2, 1, 1),
    _H3cNATOutboundAclNo_Type()
)
h3cNATOutboundAclNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cNATOutboundAclNo.setStatus("current")


class _H3cNATOutboundPoolIdx_Type(Integer32):
    """Custom type h3cNATOutboundPoolIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 320),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_H3cNATOutboundPoolIdx_Type.__name__ = "Integer32"
_H3cNATOutboundPoolIdx_Object = MibTableColumn
h3cNATOutboundPoolIdx = _H3cNATOutboundPoolIdx_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 2, 1, 2),
    _H3cNATOutboundPoolIdx_Type()
)
h3cNATOutboundPoolIdx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cNATOutboundPoolIdx.setStatus("current")


class _H3cNATOutboundIsNoPat_Type(Integer32):
    """Custom type h3cNATOutboundIsNoPat based on Integer32"""
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


_H3cNATOutboundIsNoPat_Type.__name__ = "Integer32"
_H3cNATOutboundIsNoPat_Object = MibTableColumn
h3cNATOutboundIsNoPat = _H3cNATOutboundIsNoPat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 2, 1, 3),
    _H3cNATOutboundIsNoPat_Type()
)
h3cNATOutboundIsNoPat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cNATOutboundIsNoPat.setStatus("current")


class _H3cNATOutboundSlotNo_Type(Integer32):
    """Custom type h3cNATOutboundSlotNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
        ValueRangeConstraint(255, 255),
    )


_H3cNATOutboundSlotNo_Type.__name__ = "Integer32"
_H3cNATOutboundSlotNo_Object = MibTableColumn
h3cNATOutboundSlotNo = _H3cNATOutboundSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 2, 1, 4),
    _H3cNATOutboundSlotNo_Type()
)
h3cNATOutboundSlotNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cNATOutboundSlotNo.setStatus("current")
_H3cNATOutboundRowStatus_Type = RowStatus
_H3cNATOutboundRowStatus_Object = MibTableColumn
h3cNATOutboundRowStatus = _H3cNATOutboundRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 2, 1, 5),
    _H3cNATOutboundRowStatus_Type()
)
h3cNATOutboundRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cNATOutboundRowStatus.setStatus("current")
_H3cNATServerTable_Object = MibTable
h3cNATServerTable = _H3cNATServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 3)
)
if mibBuilder.loadTexts:
    h3cNATServerTable.setStatus("current")
_H3cNATServerEntry_Object = MibTableRow
h3cNATServerEntry = _H3cNATServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 3, 1)
)
h3cNATServerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "H3C-NAT-MIB", "h3cNATServerProType"),
    (0, "H3C-NAT-MIB", "h3cNATServerGlobalIP"),
    (0, "H3C-NAT-MIB", "h3cNATServerStartGlobalPort"),
    (0, "H3C-NAT-MIB", "h3cNATServerVpnIndex"),
)
if mibBuilder.loadTexts:
    h3cNATServerEntry.setStatus("current")


class _H3cNATServerProType_Type(Integer32):
    """Custom type h3cNATServerProType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_H3cNATServerProType_Type.__name__ = "Integer32"
_H3cNATServerProType_Object = MibTableColumn
h3cNATServerProType = _H3cNATServerProType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 3, 1, 1),
    _H3cNATServerProType_Type()
)
h3cNATServerProType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cNATServerProType.setStatus("current")
_H3cNATServerGlobalIP_Type = IpAddress
_H3cNATServerGlobalIP_Object = MibTableColumn
h3cNATServerGlobalIP = _H3cNATServerGlobalIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 3, 1, 2),
    _H3cNATServerGlobalIP_Type()
)
h3cNATServerGlobalIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cNATServerGlobalIP.setStatus("current")


class _H3cNATServerStartGlobalPort_Type(Integer32):
    """Custom type h3cNATServerStartGlobalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cNATServerStartGlobalPort_Type.__name__ = "Integer32"
_H3cNATServerStartGlobalPort_Object = MibTableColumn
h3cNATServerStartGlobalPort = _H3cNATServerStartGlobalPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 3, 1, 3),
    _H3cNATServerStartGlobalPort_Type()
)
h3cNATServerStartGlobalPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cNATServerStartGlobalPort.setStatus("current")


class _H3cNATServerEndGlobalPort_Type(Integer32):
    """Custom type h3cNATServerEndGlobalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cNATServerEndGlobalPort_Type.__name__ = "Integer32"
_H3cNATServerEndGlobalPort_Object = MibTableColumn
h3cNATServerEndGlobalPort = _H3cNATServerEndGlobalPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 3, 1, 4),
    _H3cNATServerEndGlobalPort_Type()
)
h3cNATServerEndGlobalPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cNATServerEndGlobalPort.setStatus("current")
_H3cNATServerStartInsideIP_Type = IpAddress
_H3cNATServerStartInsideIP_Object = MibTableColumn
h3cNATServerStartInsideIP = _H3cNATServerStartInsideIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 3, 1, 5),
    _H3cNATServerStartInsideIP_Type()
)
h3cNATServerStartInsideIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cNATServerStartInsideIP.setStatus("current")
_H3cNATServerEndInsideIP_Type = IpAddress
_H3cNATServerEndInsideIP_Object = MibTableColumn
h3cNATServerEndInsideIP = _H3cNATServerEndInsideIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 3, 1, 6),
    _H3cNATServerEndInsideIP_Type()
)
h3cNATServerEndInsideIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cNATServerEndInsideIP.setStatus("current")


class _H3cNATServerInsidePort_Type(Integer32):
    """Custom type h3cNATServerInsidePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cNATServerInsidePort_Type.__name__ = "Integer32"
_H3cNATServerInsidePort_Object = MibTableColumn
h3cNATServerInsidePort = _H3cNATServerInsidePort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 3, 1, 7),
    _H3cNATServerInsidePort_Type()
)
h3cNATServerInsidePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cNATServerInsidePort.setStatus("current")


class _H3cNATServerSlotNo_Type(Integer32):
    """Custom type h3cNATServerSlotNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
        ValueRangeConstraint(255, 255),
    )


_H3cNATServerSlotNo_Type.__name__ = "Integer32"
_H3cNATServerSlotNo_Object = MibTableColumn
h3cNATServerSlotNo = _H3cNATServerSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 3, 1, 8),
    _H3cNATServerSlotNo_Type()
)
h3cNATServerSlotNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cNATServerSlotNo.setStatus("current")


class _H3cNATServerVpnIndex_Type(Integer32):
    """Custom type h3cNATServerVpnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cNATServerVpnIndex_Type.__name__ = "Integer32"
_H3cNATServerVpnIndex_Object = MibTableColumn
h3cNATServerVpnIndex = _H3cNATServerVpnIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 3, 1, 10),
    _H3cNATServerVpnIndex_Type()
)
h3cNATServerVpnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cNATServerVpnIndex.setStatus("current")


class _H3cNATServerAclNumber_Type(Integer32):
    """Custom type h3cNATServerAclNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_H3cNATServerAclNumber_Type.__name__ = "Integer32"
_H3cNATServerAclNumber_Object = MibTableColumn
h3cNATServerAclNumber = _H3cNATServerAclNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 3, 1, 11),
    _H3cNATServerAclNumber_Type()
)
h3cNATServerAclNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cNATServerAclNumber.setStatus("current")
_H3cNATServerRowStatus_Type = RowStatus
_H3cNATServerRowStatus_Object = MibTableColumn
h3cNATServerRowStatus = _H3cNATServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 3, 1, 12),
    _H3cNATServerRowStatus_Type()
)
h3cNATServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cNATServerRowStatus.setStatus("current")
_H3cNATTimeOutTable_Object = MibTable
h3cNATTimeOutTable = _H3cNATTimeOutTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 4)
)
if mibBuilder.loadTexts:
    h3cNATTimeOutTable.setStatus("current")
_H3cNATTimeOutEntry_Object = MibTableRow
h3cNATTimeOutEntry = _H3cNATTimeOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 4, 1)
)
h3cNATTimeOutEntry.setIndexNames(
    (0, "H3C-NAT-MIB", "h3cNATTimeOutProtocol"),
)
if mibBuilder.loadTexts:
    h3cNATTimeOutEntry.setStatus("current")


class _H3cNATTimeOutProtocol_Type(Integer32):
    """Custom type h3cNATTimeOutProtocol based on Integer32"""
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


_H3cNATTimeOutProtocol_Type.__name__ = "Integer32"
_H3cNATTimeOutProtocol_Object = MibTableColumn
h3cNATTimeOutProtocol = _H3cNATTimeOutProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 4, 1, 1),
    _H3cNATTimeOutProtocol_Type()
)
h3cNATTimeOutProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cNATTimeOutProtocol.setStatus("current")


class _H3cNATTimeOutTimeValue_Type(Integer32):
    """Custom type h3cNATTimeOutTimeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 86400),
    )


_H3cNATTimeOutTimeValue_Type.__name__ = "Integer32"
_H3cNATTimeOutTimeValue_Object = MibTableColumn
h3cNATTimeOutTimeValue = _H3cNATTimeOutTimeValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 4, 1, 2),
    _H3cNATTimeOutTimeValue_Type()
)
h3cNATTimeOutTimeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cNATTimeOutTimeValue.setStatus("current")
_H3cNATBLEnableTable_Object = MibTable
h3cNATBLEnableTable = _H3cNATBLEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 5)
)
if mibBuilder.loadTexts:
    h3cNATBLEnableTable.setStatus("current")
_H3cNATBLEnableEntry_Object = MibTableRow
h3cNATBLEnableEntry = _H3cNATBLEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 5, 1)
)
h3cNATBLEnableEntry.setIndexNames(
    (0, "H3C-NAT-MIB", "h3cNATBLEnableSlotNo"),
)
if mibBuilder.loadTexts:
    h3cNATBLEnableEntry.setStatus("current")


class _H3cNATBLEnableSlotNo_Type(Integer32):
    """Custom type h3cNATBLEnableSlotNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
        ValueRangeConstraint(255, 255),
    )


_H3cNATBLEnableSlotNo_Type.__name__ = "Integer32"
_H3cNATBLEnableSlotNo_Object = MibTableColumn
h3cNATBLEnableSlotNo = _H3cNATBLEnableSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 5, 1, 1),
    _H3cNATBLEnableSlotNo_Type()
)
h3cNATBLEnableSlotNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cNATBLEnableSlotNo.setStatus("current")


class _H3cNATBLEnable_Type(Integer32):
    """Custom type h3cNATBLEnable based on Integer32"""
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


_H3cNATBLEnable_Type.__name__ = "Integer32"
_H3cNATBLEnable_Object = MibTableColumn
h3cNATBLEnable = _H3cNATBLEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 5, 1, 2),
    _H3cNATBLEnable_Type()
)
h3cNATBLEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cNATBLEnable.setStatus("current")
_H3cNATBLIPConnectLimitParaTable_Object = MibTable
h3cNATBLIPConnectLimitParaTable = _H3cNATBLIPConnectLimitParaTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 6)
)
if mibBuilder.loadTexts:
    h3cNATBLIPConnectLimitParaTable.setStatus("current")
_H3cNATBLIPConnectLimitParaEntry_Object = MibTableRow
h3cNATBLIPConnectLimitParaEntry = _H3cNATBLIPConnectLimitParaEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 6, 1)
)
h3cNATBLIPConnectLimitParaEntry.setIndexNames(
    (0, "H3C-NAT-MIB", "h3cNATBLIPConnectLimitParaIP"),
)
if mibBuilder.loadTexts:
    h3cNATBLIPConnectLimitParaEntry.setStatus("current")
_H3cNATBLIPConnectLimitParaIP_Type = IpAddress
_H3cNATBLIPConnectLimitParaIP_Object = MibTableColumn
h3cNATBLIPConnectLimitParaIP = _H3cNATBLIPConnectLimitParaIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 6, 1, 1),
    _H3cNATBLIPConnectLimitParaIP_Type()
)
h3cNATBLIPConnectLimitParaIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cNATBLIPConnectLimitParaIP.setStatus("current")


class _H3cNATBLIPConnectHighValue_Type(Integer32):
    """Custom type h3cNATBLIPConnectHighValue based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 20000),
    )


_H3cNATBLIPConnectHighValue_Type.__name__ = "Integer32"
_H3cNATBLIPConnectHighValue_Object = MibTableColumn
h3cNATBLIPConnectHighValue = _H3cNATBLIPConnectHighValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 6, 1, 2),
    _H3cNATBLIPConnectHighValue_Type()
)
h3cNATBLIPConnectHighValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cNATBLIPConnectHighValue.setStatus("current")


class _H3cNATBLIPConnectLowValue_Type(Integer32):
    """Custom type h3cNATBLIPConnectLowValue based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 20000),
    )


_H3cNATBLIPConnectLowValue_Type.__name__ = "Integer32"
_H3cNATBLIPConnectLowValue_Object = MibTableColumn
h3cNATBLIPConnectLowValue = _H3cNATBLIPConnectLowValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 6, 1, 3),
    _H3cNATBLIPConnectLowValue_Type()
)
h3cNATBLIPConnectLowValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cNATBLIPConnectLowValue.setStatus("current")


class _H3cNATBLIPUseSpecialConnectRate_Type(Integer32):
    """Custom type h3cNATBLIPUseSpecialConnectRate based on Integer32"""
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


_H3cNATBLIPUseSpecialConnectRate_Type.__name__ = "Integer32"
_H3cNATBLIPUseSpecialConnectRate_Object = MibTableColumn
h3cNATBLIPUseSpecialConnectRate = _H3cNATBLIPUseSpecialConnectRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 6, 1, 4),
    _H3cNATBLIPUseSpecialConnectRate_Type()
)
h3cNATBLIPUseSpecialConnectRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cNATBLIPUseSpecialConnectRate.setStatus("current")
_H3cNATBLIPConnectLimitRowStatus_Type = RowStatus
_H3cNATBLIPConnectLimitRowStatus_Object = MibTableColumn
h3cNATBLIPConnectLimitRowStatus = _H3cNATBLIPConnectLimitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 6, 1, 5),
    _H3cNATBLIPConnectLimitRowStatus_Type()
)
h3cNATBLIPConnectLimitRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cNATBLIPConnectLimitRowStatus.setStatus("current")
_H3cNATBLManagerTable_Object = MibTable
h3cNATBLManagerTable = _H3cNATBLManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 7)
)
if mibBuilder.loadTexts:
    h3cNATBLManagerTable.setStatus("current")
_H3cNATBLManagerEntry_Object = MibTableRow
h3cNATBLManagerEntry = _H3cNATBLManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 7, 1)
)
h3cNATBLManagerEntry.setIndexNames(
    (0, "H3C-NAT-MIB", "h3cNATBLIpAdress"),
    (0, "H3C-NAT-MIB", "h3cNATBLSlotNo"),
)
if mibBuilder.loadTexts:
    h3cNATBLManagerEntry.setStatus("current")
_H3cNATBLIpAdress_Type = IpAddress
_H3cNATBLIpAdress_Object = MibTableColumn
h3cNATBLIpAdress = _H3cNATBLIpAdress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 7, 1, 1),
    _H3cNATBLIpAdress_Type()
)
h3cNATBLIpAdress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cNATBLIpAdress.setStatus("current")


class _H3cNATBLSlotNo_Type(Integer32):
    """Custom type h3cNATBLSlotNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_H3cNATBLSlotNo_Type.__name__ = "Integer32"
_H3cNATBLSlotNo_Object = MibTableColumn
h3cNATBLSlotNo = _H3cNATBLSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 7, 1, 2),
    _H3cNATBLSlotNo_Type()
)
h3cNATBLSlotNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cNATBLSlotNo.setStatus("current")
_H3cNATBLConSum_Type = Integer32
_H3cNATBLConSum_Object = MibTableColumn
h3cNATBLConSum = _H3cNATBLConSum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 7, 1, 3),
    _H3cNATBLConSum_Type()
)
h3cNATBLConSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cNATBLConSum.setStatus("current")


class _H3cNATBLConSpd_Type(Integer32):
    """Custom type h3cNATBLConSpd based on Integer32"""
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


_H3cNATBLConSpd_Type.__name__ = "Integer32"
_H3cNATBLConSpd_Object = MibTableColumn
h3cNATBLConSpd = _H3cNATBLConSpd_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 7, 1, 4),
    _H3cNATBLConSpd_Type()
)
h3cNATBLConSpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cNATBLConSpd.setStatus("current")
_H3cNATStatTable_Object = MibTable
h3cNATStatTable = _H3cNATStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 8)
)
if mibBuilder.loadTexts:
    h3cNATStatTable.setStatus("current")
_H3cNATStatEntry_Object = MibTableRow
h3cNATStatEntry = _H3cNATStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 8, 1)
)
h3cNATStatEntry.setIndexNames(
    (0, "H3C-NAT-MIB", "h3cNATStatNATBoardNo"),
)
if mibBuilder.loadTexts:
    h3cNATStatEntry.setStatus("current")


class _H3cNATStatNATBoardNo_Type(Integer32):
    """Custom type h3cNATStatNATBoardNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
        ValueRangeConstraint(255, 255),
    )


_H3cNATStatNATBoardNo_Type.__name__ = "Integer32"
_H3cNATStatNATBoardNo_Object = MibTableColumn
h3cNATStatNATBoardNo = _H3cNATStatNATBoardNo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 8, 1, 1),
    _H3cNATStatNATBoardNo_Type()
)
h3cNATStatNATBoardNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cNATStatNATBoardNo.setStatus("current")
_H3cNATStatActiveTblCount_Type = Counter32
_H3cNATStatActiveTblCount_Object = MibTableColumn
h3cNATStatActiveTblCount = _H3cNATStatActiveTblCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 8, 1, 2),
    _H3cNATStatActiveTblCount_Type()
)
h3cNATStatActiveTblCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cNATStatActiveTblCount.setStatus("current")
_H3cNATStatActiveTblCountInNP_Type = Counter32
_H3cNATStatActiveTblCountInNP_Object = MibTableColumn
h3cNATStatActiveTblCountInNP = _H3cNATStatActiveTblCountInNP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 8, 1, 3),
    _H3cNATStatActiveTblCountInNP_Type()
)
h3cNATStatActiveTblCountInNP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cNATStatActiveTblCountInNP.setStatus("current")
_H3cNATStatActiveNatTblCount_Type = Counter32
_H3cNATStatActiveNatTblCount_Object = MibTableColumn
h3cNATStatActiveNatTblCount = _H3cNATStatActiveNatTblCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 8, 1, 4),
    _H3cNATStatActiveNatTblCount_Type()
)
h3cNATStatActiveNatTblCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cNATStatActiveNatTblCount.setStatus("current")
_H3cNATStatActiveSvrTblCount_Type = Counter32
_H3cNATStatActiveSvrTblCount_Object = MibTableColumn
h3cNATStatActiveSvrTblCount = _H3cNATStatActiveSvrTblCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 8, 1, 5),
    _H3cNATStatActiveSvrTblCount_Type()
)
h3cNATStatActiveSvrTblCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cNATStatActiveSvrTblCount.setStatus("current")
_H3cNATStatActivePoolTblCount_Type = Counter32
_H3cNATStatActivePoolTblCount_Object = MibTableColumn
h3cNATStatActivePoolTblCount = _H3cNATStatActivePoolTblCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 8, 1, 6),
    _H3cNATStatActivePoolTblCount_Type()
)
h3cNATStatActivePoolTblCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cNATStatActivePoolTblCount.setStatus("current")
_H3cNATStatNumOfUsedPort_Type = Counter32
_H3cNATStatNumOfUsedPort_Object = MibTableColumn
h3cNATStatNumOfUsedPort = _H3cNATStatNumOfUsedPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 8, 1, 7),
    _H3cNATStatNumOfUsedPort_Type()
)
h3cNATStatNumOfUsedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cNATStatNumOfUsedPort.setStatus("current")
_H3cNATStatNumOfGoodPkt_Type = Counter32
_H3cNATStatNumOfGoodPkt_Object = MibTableColumn
h3cNATStatNumOfGoodPkt = _H3cNATStatNumOfGoodPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 8, 1, 8),
    _H3cNATStatNumOfGoodPkt_Type()
)
h3cNATStatNumOfGoodPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cNATStatNumOfGoodPkt.setStatus("current")
_H3cNATStatNumOfBadPkt_Type = Counter32
_H3cNATStatNumOfBadPkt_Object = MibTableColumn
h3cNATStatNumOfBadPkt = _H3cNATStatNumOfBadPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 8, 1, 9),
    _H3cNATStatNumOfBadPkt_Type()
)
h3cNATStatNumOfBadPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cNATStatNumOfBadPkt.setStatus("current")
_H3cNATStaticSessionCount_Type = Integer32
_H3cNATStaticSessionCount_Object = MibTableColumn
h3cNATStaticSessionCount = _H3cNATStaticSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 8, 1, 10),
    _H3cNATStaticSessionCount_Type()
)
h3cNATStaticSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cNATStaticSessionCount.setStatus("current")
_H3cNATFragmentSessionCount_Type = Integer32
_H3cNATFragmentSessionCount_Object = MibTableColumn
h3cNATFragmentSessionCount = _H3cNATFragmentSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 8, 1, 11),
    _H3cNATFragmentSessionCount_Type()
)
h3cNATFragmentSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cNATFragmentSessionCount.setStatus("current")
_H3cNATSequenceSessionCount_Type = Integer32
_H3cNATSequenceSessionCount_Object = MibTableColumn
h3cNATSequenceSessionCount = _H3cNATSequenceSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 8, 1, 12),
    _H3cNATSequenceSessionCount_Type()
)
h3cNATSequenceSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cNATSequenceSessionCount.setStatus("current")
_H3cNATLogCount_Type = Integer32
_H3cNATLogCount_Object = MibTableColumn
h3cNATLogCount = _H3cNATLogCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 8, 1, 13),
    _H3cNATLogCount_Type()
)
h3cNATLogCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cNATLogCount.setStatus("current")
_H3cNATSessionTable_Object = MibTable
h3cNATSessionTable = _H3cNATSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 9)
)
if mibBuilder.loadTexts:
    h3cNATSessionTable.setStatus("current")
_H3cNATSessionEntry_Object = MibTableRow
h3cNATSessionEntry = _H3cNATSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 9, 1)
)
h3cNATSessionEntry.setIndexNames(
    (0, "H3C-NAT-MIB", "h3cNATSessionHashNumber"),
    (0, "H3C-NAT-MIB", "h3cNATSessionProtocol"),
    (0, "H3C-NAT-MIB", "h3cNATSessionInsideIP"),
    (0, "H3C-NAT-MIB", "h3cNATSessionInsidePort"),
    (0, "H3C-NAT-MIB", "h3cNATSessionPeerIP"),
    (0, "H3C-NAT-MIB", "h3cNATSessionPeerPort"),
    (0, "H3C-NAT-MIB", "h3cNATSessionVpnIndex"),
)
if mibBuilder.loadTexts:
    h3cNATSessionEntry.setStatus("current")


class _H3cNATSessionHashNumber_Type(Integer32):
    """Custom type h3cNATSessionHashNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300000),
    )


_H3cNATSessionHashNumber_Type.__name__ = "Integer32"
_H3cNATSessionHashNumber_Object = MibTableColumn
h3cNATSessionHashNumber = _H3cNATSessionHashNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 9, 1, 1),
    _H3cNATSessionHashNumber_Type()
)
h3cNATSessionHashNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cNATSessionHashNumber.setStatus("current")


class _H3cNATSessionProtocol_Type(Integer32):
    """Custom type h3cNATSessionProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_H3cNATSessionProtocol_Type.__name__ = "Integer32"
_H3cNATSessionProtocol_Object = MibTableColumn
h3cNATSessionProtocol = _H3cNATSessionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 9, 1, 2),
    _H3cNATSessionProtocol_Type()
)
h3cNATSessionProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cNATSessionProtocol.setStatus("current")
_H3cNATSessionGlobalIP_Type = IpAddress
_H3cNATSessionGlobalIP_Object = MibTableColumn
h3cNATSessionGlobalIP = _H3cNATSessionGlobalIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 9, 1, 3),
    _H3cNATSessionGlobalIP_Type()
)
h3cNATSessionGlobalIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cNATSessionGlobalIP.setStatus("current")


class _H3cNATSessionGlobalPort_Type(Integer32):
    """Custom type h3cNATSessionGlobalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cNATSessionGlobalPort_Type.__name__ = "Integer32"
_H3cNATSessionGlobalPort_Object = MibTableColumn
h3cNATSessionGlobalPort = _H3cNATSessionGlobalPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 9, 1, 4),
    _H3cNATSessionGlobalPort_Type()
)
h3cNATSessionGlobalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cNATSessionGlobalPort.setStatus("current")
_H3cNATSessionInsideIP_Type = IpAddress
_H3cNATSessionInsideIP_Object = MibTableColumn
h3cNATSessionInsideIP = _H3cNATSessionInsideIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 9, 1, 5),
    _H3cNATSessionInsideIP_Type()
)
h3cNATSessionInsideIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cNATSessionInsideIP.setStatus("current")


class _H3cNATSessionInsidePort_Type(Integer32):
    """Custom type h3cNATSessionInsidePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cNATSessionInsidePort_Type.__name__ = "Integer32"
_H3cNATSessionInsidePort_Object = MibTableColumn
h3cNATSessionInsidePort = _H3cNATSessionInsidePort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 9, 1, 6),
    _H3cNATSessionInsidePort_Type()
)
h3cNATSessionInsidePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cNATSessionInsidePort.setStatus("current")
_H3cNATSessionPeerIP_Type = IpAddress
_H3cNATSessionPeerIP_Object = MibTableColumn
h3cNATSessionPeerIP = _H3cNATSessionPeerIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 9, 1, 7),
    _H3cNATSessionPeerIP_Type()
)
h3cNATSessionPeerIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cNATSessionPeerIP.setStatus("current")


class _H3cNATSessionPeerPort_Type(Integer32):
    """Custom type h3cNATSessionPeerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cNATSessionPeerPort_Type.__name__ = "Integer32"
_H3cNATSessionPeerPort_Object = MibTableColumn
h3cNATSessionPeerPort = _H3cNATSessionPeerPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 9, 1, 8),
    _H3cNATSessionPeerPort_Type()
)
h3cNATSessionPeerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cNATSessionPeerPort.setStatus("current")


class _H3cNATSessionVpnIndex_Type(Integer32):
    """Custom type h3cNATSessionVpnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H3cNATSessionVpnIndex_Type.__name__ = "Integer32"
_H3cNATSessionVpnIndex_Object = MibTableColumn
h3cNATSessionVpnIndex = _H3cNATSessionVpnIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 9, 1, 9),
    _H3cNATSessionVpnIndex_Type()
)
h3cNATSessionVpnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cNATSessionVpnIndex.setStatus("current")
_H3cNATSessionTTL_Type = Integer32
_H3cNATSessionTTL_Object = MibTableColumn
h3cNATSessionTTL = _H3cNATSessionTTL_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 9, 1, 10),
    _H3cNATSessionTTL_Type()
)
h3cNATSessionTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cNATSessionTTL.setStatus("current")
_H3cNATSessionStatus_Type = Integer32
_H3cNATSessionStatus_Object = MibTableColumn
h3cNATSessionStatus = _H3cNATSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 9, 1, 11),
    _H3cNATSessionStatus_Type()
)
h3cNATSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cNATSessionStatus.setStatus("current")
_H3cNATSessionLeftTime_Type = TimeTicks
_H3cNATSessionLeftTime_Object = MibTableColumn
h3cNATSessionLeftTime = _H3cNATSessionLeftTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 9, 1, 12),
    _H3cNATSessionLeftTime_Type()
)
h3cNATSessionLeftTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cNATSessionLeftTime.setStatus("current")
_H3cNATStaticConfTable_Object = MibTable
h3cNATStaticConfTable = _H3cNATStaticConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 10)
)
if mibBuilder.loadTexts:
    h3cNATStaticConfTable.setStatus("current")
_H3cNATStaticConfEntry_Object = MibTableRow
h3cNATStaticConfEntry = _H3cNATStaticConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 10, 1)
)
h3cNATStaticConfEntry.setIndexNames(
    (0, "H3C-NAT-MIB", "h3cNATStaticInsideIp"),
)
if mibBuilder.loadTexts:
    h3cNATStaticConfEntry.setStatus("current")
_H3cNATStaticInsideIp_Type = IpAddress
_H3cNATStaticInsideIp_Object = MibTableColumn
h3cNATStaticInsideIp = _H3cNATStaticInsideIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 10, 1, 1),
    _H3cNATStaticInsideIp_Type()
)
h3cNATStaticInsideIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cNATStaticInsideIp.setStatus("current")
_H3cNATStaticGlobalIp_Type = IpAddress
_H3cNATStaticGlobalIp_Object = MibTableColumn
h3cNATStaticGlobalIp = _H3cNATStaticGlobalIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 10, 1, 2),
    _H3cNATStaticGlobalIp_Type()
)
h3cNATStaticGlobalIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cNATStaticGlobalIp.setStatus("current")
_H3cNATStaticRowStatus_Type = RowStatus
_H3cNATStaticRowStatus_Object = MibTableColumn
h3cNATStaticRowStatus = _H3cNATStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 10, 1, 3),
    _H3cNATStaticRowStatus_Type()
)
h3cNATStaticRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cNATStaticRowStatus.setStatus("current")
_H3cNATStaticEnableTable_Object = MibTable
h3cNATStaticEnableTable = _H3cNATStaticEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 11)
)
if mibBuilder.loadTexts:
    h3cNATStaticEnableTable.setStatus("current")
_H3cNATStaticEnableEntry_Object = MibTableRow
h3cNATStaticEnableEntry = _H3cNATStaticEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 11, 1)
)
h3cNATStaticEnableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cNATStaticEnableEntry.setStatus("current")


class _H3cNATStaticEnable_Type(Integer32):
    """Custom type h3cNATStaticEnable based on Integer32"""
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


_H3cNATStaticEnable_Type.__name__ = "Integer32"
_H3cNATStaticEnable_Object = MibTableColumn
h3cNATStaticEnable = _H3cNATStaticEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 11, 1, 2),
    _H3cNATStaticEnable_Type()
)
h3cNATStaticEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cNATStaticEnable.setStatus("current")
_H3cNATDnsMapTable_Object = MibTable
h3cNATDnsMapTable = _H3cNATDnsMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 12)
)
if mibBuilder.loadTexts:
    h3cNATDnsMapTable.setStatus("current")
_H3cNATDnsMapEntry_Object = MibTableRow
h3cNATDnsMapEntry = _H3cNATDnsMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 12, 1)
)
h3cNATDnsMapEntry.setIndexNames(
    (0, "H3C-NAT-MIB", "h3cNATDnsMapDomainName"),
)
if mibBuilder.loadTexts:
    h3cNATDnsMapEntry.setStatus("current")
_H3cNATDnsMapDomainName_Type = DisplayString
_H3cNATDnsMapDomainName_Object = MibTableColumn
h3cNATDnsMapDomainName = _H3cNATDnsMapDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 12, 1, 1),
    _H3cNATDnsMapDomainName_Type()
)
h3cNATDnsMapDomainName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cNATDnsMapDomainName.setStatus("current")
_H3cNATDnsMapGlobalIp_Type = IpAddress
_H3cNATDnsMapGlobalIp_Object = MibTableColumn
h3cNATDnsMapGlobalIp = _H3cNATDnsMapGlobalIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 12, 1, 2),
    _H3cNATDnsMapGlobalIp_Type()
)
h3cNATDnsMapGlobalIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cNATDnsMapGlobalIp.setStatus("current")


class _H3cNATDnsMapGlobalPort_Type(Integer32):
    """Custom type h3cNATDnsMapGlobalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cNATDnsMapGlobalPort_Type.__name__ = "Integer32"
_H3cNATDnsMapGlobalPort_Object = MibTableColumn
h3cNATDnsMapGlobalPort = _H3cNATDnsMapGlobalPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 12, 1, 3),
    _H3cNATDnsMapGlobalPort_Type()
)
h3cNATDnsMapGlobalPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cNATDnsMapGlobalPort.setStatus("current")


class _H3cNATDnsMapProtocolType_Type(Integer32):
    """Custom type h3cNATDnsMapProtocolType based on Integer32"""
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


_H3cNATDnsMapProtocolType_Type.__name__ = "Integer32"
_H3cNATDnsMapProtocolType_Object = MibTableColumn
h3cNATDnsMapProtocolType = _H3cNATDnsMapProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 12, 1, 4),
    _H3cNATDnsMapProtocolType_Type()
)
h3cNATDnsMapProtocolType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cNATDnsMapProtocolType.setStatus("current")
_H3cNATDnsMapLastUseTime_Type = TimeTicks
_H3cNATDnsMapLastUseTime_Object = MibTableColumn
h3cNATDnsMapLastUseTime = _H3cNATDnsMapLastUseTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 12, 1, 5),
    _H3cNATDnsMapLastUseTime_Type()
)
h3cNATDnsMapLastUseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cNATDnsMapLastUseTime.setStatus("current")
_H3cNATDnsMapRowStatus_Type = RowStatus
_H3cNATDnsMapRowStatus_Object = MibTableColumn
h3cNATDnsMapRowStatus = _H3cNATDnsMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 18, 2, 12, 1, 6),
    _H3cNATDnsMapRowStatus_Type()
)
h3cNATDnsMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cNATDnsMapRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-NAT-MIB",
    **{"h3cNat": h3cNat,
       "h3cNATGlobalVars": h3cNATGlobalVars,
       "h3cNATClearSession": h3cNATClearSession,
       "h3cNATClearSessionSlotNo": h3cNATClearSessionSlotNo,
       "h3cNATBLConnectLimitPara": h3cNATBLConnectLimitPara,
       "h3cNATBLConnectHighValue": h3cNATBLConnectHighValue,
       "h3cNATBLConnectLowValue": h3cNATBLConnectLowValue,
       "h3cNATBLConnectHighRate": h3cNATBLConnectHighRate,
       "h3cNATBLConnectLowRate": h3cNATBLConnectLowRate,
       "h3cNATBLSpecialConnectHighRate": h3cNATBLSpecialConnectHighRate,
       "h3cNATBLSpecialConnectLowRate": h3cNATBLSpecialConnectLowRate,
       "h3cNATBLCtrlEnable": h3cNATBLCtrlEnable,
       "h3cNATBLConnectSumEnable": h3cNATBLConnectSumEnable,
       "h3cNATBLConnectRateEnable": h3cNATBLConnectRateEnable,
       "h3cNATNPTimer": h3cNATNPTimer,
       "h3cNATNPAgingTime": h3cNATNPAgingTime,
       "h3cNATMibObjects": h3cNATMibObjects,
       "h3cNATPoolInfoTable": h3cNATPoolInfoTable,
       "h3cNATPoolInfoEntry": h3cNATPoolInfoEntry,
       "h3cNATPoolIdx": h3cNATPoolIdx,
       "h3cNATPoolStartIpAddr": h3cNATPoolStartIpAddr,
       "h3cNATPoolEndIpAddr": h3cNATPoolEndIpAddr,
       "h3cNATPoolSlotNo": h3cNATPoolSlotNo,
       "h3cNATPoolRefCounter": h3cNATPoolRefCounter,
       "h3cNATPoolRowStatus": h3cNATPoolRowStatus,
       "h3cNATOutboundTable": h3cNATOutboundTable,
       "h3cNATOutboundEntry": h3cNATOutboundEntry,
       "h3cNATOutboundAclNo": h3cNATOutboundAclNo,
       "h3cNATOutboundPoolIdx": h3cNATOutboundPoolIdx,
       "h3cNATOutboundIsNoPat": h3cNATOutboundIsNoPat,
       "h3cNATOutboundSlotNo": h3cNATOutboundSlotNo,
       "h3cNATOutboundRowStatus": h3cNATOutboundRowStatus,
       "h3cNATServerTable": h3cNATServerTable,
       "h3cNATServerEntry": h3cNATServerEntry,
       "h3cNATServerProType": h3cNATServerProType,
       "h3cNATServerGlobalIP": h3cNATServerGlobalIP,
       "h3cNATServerStartGlobalPort": h3cNATServerStartGlobalPort,
       "h3cNATServerEndGlobalPort": h3cNATServerEndGlobalPort,
       "h3cNATServerStartInsideIP": h3cNATServerStartInsideIP,
       "h3cNATServerEndInsideIP": h3cNATServerEndInsideIP,
       "h3cNATServerInsidePort": h3cNATServerInsidePort,
       "h3cNATServerSlotNo": h3cNATServerSlotNo,
       "h3cNATServerVpnIndex": h3cNATServerVpnIndex,
       "h3cNATServerAclNumber": h3cNATServerAclNumber,
       "h3cNATServerRowStatus": h3cNATServerRowStatus,
       "h3cNATTimeOutTable": h3cNATTimeOutTable,
       "h3cNATTimeOutEntry": h3cNATTimeOutEntry,
       "h3cNATTimeOutProtocol": h3cNATTimeOutProtocol,
       "h3cNATTimeOutTimeValue": h3cNATTimeOutTimeValue,
       "h3cNATBLEnableTable": h3cNATBLEnableTable,
       "h3cNATBLEnableEntry": h3cNATBLEnableEntry,
       "h3cNATBLEnableSlotNo": h3cNATBLEnableSlotNo,
       "h3cNATBLEnable": h3cNATBLEnable,
       "h3cNATBLIPConnectLimitParaTable": h3cNATBLIPConnectLimitParaTable,
       "h3cNATBLIPConnectLimitParaEntry": h3cNATBLIPConnectLimitParaEntry,
       "h3cNATBLIPConnectLimitParaIP": h3cNATBLIPConnectLimitParaIP,
       "h3cNATBLIPConnectHighValue": h3cNATBLIPConnectHighValue,
       "h3cNATBLIPConnectLowValue": h3cNATBLIPConnectLowValue,
       "h3cNATBLIPUseSpecialConnectRate": h3cNATBLIPUseSpecialConnectRate,
       "h3cNATBLIPConnectLimitRowStatus": h3cNATBLIPConnectLimitRowStatus,
       "h3cNATBLManagerTable": h3cNATBLManagerTable,
       "h3cNATBLManagerEntry": h3cNATBLManagerEntry,
       "h3cNATBLIpAdress": h3cNATBLIpAdress,
       "h3cNATBLSlotNo": h3cNATBLSlotNo,
       "h3cNATBLConSum": h3cNATBLConSum,
       "h3cNATBLConSpd": h3cNATBLConSpd,
       "h3cNATStatTable": h3cNATStatTable,
       "h3cNATStatEntry": h3cNATStatEntry,
       "h3cNATStatNATBoardNo": h3cNATStatNATBoardNo,
       "h3cNATStatActiveTblCount": h3cNATStatActiveTblCount,
       "h3cNATStatActiveTblCountInNP": h3cNATStatActiveTblCountInNP,
       "h3cNATStatActiveNatTblCount": h3cNATStatActiveNatTblCount,
       "h3cNATStatActiveSvrTblCount": h3cNATStatActiveSvrTblCount,
       "h3cNATStatActivePoolTblCount": h3cNATStatActivePoolTblCount,
       "h3cNATStatNumOfUsedPort": h3cNATStatNumOfUsedPort,
       "h3cNATStatNumOfGoodPkt": h3cNATStatNumOfGoodPkt,
       "h3cNATStatNumOfBadPkt": h3cNATStatNumOfBadPkt,
       "h3cNATStaticSessionCount": h3cNATStaticSessionCount,
       "h3cNATFragmentSessionCount": h3cNATFragmentSessionCount,
       "h3cNATSequenceSessionCount": h3cNATSequenceSessionCount,
       "h3cNATLogCount": h3cNATLogCount,
       "h3cNATSessionTable": h3cNATSessionTable,
       "h3cNATSessionEntry": h3cNATSessionEntry,
       "h3cNATSessionHashNumber": h3cNATSessionHashNumber,
       "h3cNATSessionProtocol": h3cNATSessionProtocol,
       "h3cNATSessionGlobalIP": h3cNATSessionGlobalIP,
       "h3cNATSessionGlobalPort": h3cNATSessionGlobalPort,
       "h3cNATSessionInsideIP": h3cNATSessionInsideIP,
       "h3cNATSessionInsidePort": h3cNATSessionInsidePort,
       "h3cNATSessionPeerIP": h3cNATSessionPeerIP,
       "h3cNATSessionPeerPort": h3cNATSessionPeerPort,
       "h3cNATSessionVpnIndex": h3cNATSessionVpnIndex,
       "h3cNATSessionTTL": h3cNATSessionTTL,
       "h3cNATSessionStatus": h3cNATSessionStatus,
       "h3cNATSessionLeftTime": h3cNATSessionLeftTime,
       "h3cNATStaticConfTable": h3cNATStaticConfTable,
       "h3cNATStaticConfEntry": h3cNATStaticConfEntry,
       "h3cNATStaticInsideIp": h3cNATStaticInsideIp,
       "h3cNATStaticGlobalIp": h3cNATStaticGlobalIp,
       "h3cNATStaticRowStatus": h3cNATStaticRowStatus,
       "h3cNATStaticEnableTable": h3cNATStaticEnableTable,
       "h3cNATStaticEnableEntry": h3cNATStaticEnableEntry,
       "h3cNATStaticEnable": h3cNATStaticEnable,
       "h3cNATDnsMapTable": h3cNATDnsMapTable,
       "h3cNATDnsMapEntry": h3cNATDnsMapEntry,
       "h3cNATDnsMapDomainName": h3cNATDnsMapDomainName,
       "h3cNATDnsMapGlobalIp": h3cNATDnsMapGlobalIp,
       "h3cNATDnsMapGlobalPort": h3cNATDnsMapGlobalPort,
       "h3cNATDnsMapProtocolType": h3cNATDnsMapProtocolType,
       "h3cNATDnsMapLastUseTime": h3cNATDnsMapLastUseTime,
       "h3cNATDnsMapRowStatus": h3cNATDnsMapRowStatus}
)
