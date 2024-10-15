# SNMP MIB module (HPN-ICF-NAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-NAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:17 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfNat = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18)
)
hpnicfNat.setRevisions(
        ("2005-01-20 15:18",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfNATGlobalVars_ObjectIdentity = ObjectIdentity
hpnicfNATGlobalVars = _HpnicfNATGlobalVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 1)
)
_HpnicfNATClearSession_ObjectIdentity = ObjectIdentity
hpnicfNATClearSession = _HpnicfNATClearSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 1, 1)
)


class _HpnicfNATClearSessionSlotNo_Type(Integer32):
    """Custom type hpnicfNATClearSessionSlotNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
        ValueRangeConstraint(255, 255),
    )


_HpnicfNATClearSessionSlotNo_Type.__name__ = "Integer32"
_HpnicfNATClearSessionSlotNo_Object = MibScalar
hpnicfNATClearSessionSlotNo = _HpnicfNATClearSessionSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 1, 1, 1),
    _HpnicfNATClearSessionSlotNo_Type()
)
hpnicfNATClearSessionSlotNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfNATClearSessionSlotNo.setStatus("current")
_HpnicfNATBLConnectLimitPara_ObjectIdentity = ObjectIdentity
hpnicfNATBLConnectLimitPara = _HpnicfNATBLConnectLimitPara_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 1, 2)
)


class _HpnicfNATBLConnectHighValue_Type(Integer32):
    """Custom type hpnicfNATBLConnectHighValue based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 20000),
    )


_HpnicfNATBLConnectHighValue_Type.__name__ = "Integer32"
_HpnicfNATBLConnectHighValue_Object = MibScalar
hpnicfNATBLConnectHighValue = _HpnicfNATBLConnectHighValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 1, 2, 1),
    _HpnicfNATBLConnectHighValue_Type()
)
hpnicfNATBLConnectHighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfNATBLConnectHighValue.setStatus("current")


class _HpnicfNATBLConnectLowValue_Type(Integer32):
    """Custom type hpnicfNATBLConnectLowValue based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 20000),
    )


_HpnicfNATBLConnectLowValue_Type.__name__ = "Integer32"
_HpnicfNATBLConnectLowValue_Object = MibScalar
hpnicfNATBLConnectLowValue = _HpnicfNATBLConnectLowValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 1, 2, 2),
    _HpnicfNATBLConnectLowValue_Type()
)
hpnicfNATBLConnectLowValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfNATBLConnectLowValue.setStatus("current")


class _HpnicfNATBLConnectHighRate_Type(Integer32):
    """Custom type hpnicfNATBLConnectHighRate based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 21474836),
    )


_HpnicfNATBLConnectHighRate_Type.__name__ = "Integer32"
_HpnicfNATBLConnectHighRate_Object = MibScalar
hpnicfNATBLConnectHighRate = _HpnicfNATBLConnectHighRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 1, 2, 3),
    _HpnicfNATBLConnectHighRate_Type()
)
hpnicfNATBLConnectHighRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfNATBLConnectHighRate.setStatus("current")


class _HpnicfNATBLConnectLowRate_Type(Integer32):
    """Custom type hpnicfNATBLConnectLowRate based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 21474836),
    )


_HpnicfNATBLConnectLowRate_Type.__name__ = "Integer32"
_HpnicfNATBLConnectLowRate_Object = MibScalar
hpnicfNATBLConnectLowRate = _HpnicfNATBLConnectLowRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 1, 2, 4),
    _HpnicfNATBLConnectLowRate_Type()
)
hpnicfNATBLConnectLowRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfNATBLConnectLowRate.setStatus("current")


class _HpnicfNATBLSpecialConnectHighRate_Type(Integer32):
    """Custom type hpnicfNATBLSpecialConnectHighRate based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 21474836),
    )


_HpnicfNATBLSpecialConnectHighRate_Type.__name__ = "Integer32"
_HpnicfNATBLSpecialConnectHighRate_Object = MibScalar
hpnicfNATBLSpecialConnectHighRate = _HpnicfNATBLSpecialConnectHighRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 1, 2, 5),
    _HpnicfNATBLSpecialConnectHighRate_Type()
)
hpnicfNATBLSpecialConnectHighRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfNATBLSpecialConnectHighRate.setStatus("current")


class _HpnicfNATBLSpecialConnectLowRate_Type(Integer32):
    """Custom type hpnicfNATBLSpecialConnectLowRate based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 21474836),
    )


_HpnicfNATBLSpecialConnectLowRate_Type.__name__ = "Integer32"
_HpnicfNATBLSpecialConnectLowRate_Object = MibScalar
hpnicfNATBLSpecialConnectLowRate = _HpnicfNATBLSpecialConnectLowRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 1, 2, 6),
    _HpnicfNATBLSpecialConnectLowRate_Type()
)
hpnicfNATBLSpecialConnectLowRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfNATBLSpecialConnectLowRate.setStatus("current")
_HpnicfNATBLCtrlEnable_ObjectIdentity = ObjectIdentity
hpnicfNATBLCtrlEnable = _HpnicfNATBLCtrlEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 1, 3)
)


class _HpnicfNATBLConnectSumEnable_Type(Integer32):
    """Custom type hpnicfNATBLConnectSumEnable based on Integer32"""
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


_HpnicfNATBLConnectSumEnable_Type.__name__ = "Integer32"
_HpnicfNATBLConnectSumEnable_Object = MibScalar
hpnicfNATBLConnectSumEnable = _HpnicfNATBLConnectSumEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 1, 3, 1),
    _HpnicfNATBLConnectSumEnable_Type()
)
hpnicfNATBLConnectSumEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfNATBLConnectSumEnable.setStatus("current")


class _HpnicfNATBLConnectRateEnable_Type(Integer32):
    """Custom type hpnicfNATBLConnectRateEnable based on Integer32"""
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


_HpnicfNATBLConnectRateEnable_Type.__name__ = "Integer32"
_HpnicfNATBLConnectRateEnable_Object = MibScalar
hpnicfNATBLConnectRateEnable = _HpnicfNATBLConnectRateEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 1, 3, 2),
    _HpnicfNATBLConnectRateEnable_Type()
)
hpnicfNATBLConnectRateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfNATBLConnectRateEnable.setStatus("current")
_HpnicfNATNPTimer_ObjectIdentity = ObjectIdentity
hpnicfNATNPTimer = _HpnicfNATNPTimer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 1, 4)
)


class _HpnicfNATNPAgingTime_Type(Integer32):
    """Custom type hpnicfNATNPAgingTime based on Integer32"""
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


_HpnicfNATNPAgingTime_Type.__name__ = "Integer32"
_HpnicfNATNPAgingTime_Object = MibScalar
hpnicfNATNPAgingTime = _HpnicfNATNPAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 1, 4, 1),
    _HpnicfNATNPAgingTime_Type()
)
hpnicfNATNPAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfNATNPAgingTime.setStatus("current")
_HpnicfNATMibObjects_ObjectIdentity = ObjectIdentity
hpnicfNATMibObjects = _HpnicfNATMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2)
)
_HpnicfNATPoolInfoTable_Object = MibTable
hpnicfNATPoolInfoTable = _HpnicfNATPoolInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfNATPoolInfoTable.setStatus("current")
_HpnicfNATPoolInfoEntry_Object = MibTableRow
hpnicfNATPoolInfoEntry = _HpnicfNATPoolInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 1, 1)
)
hpnicfNATPoolInfoEntry.setIndexNames(
    (0, "HPN-ICF-NAT-MIB", "hpnicfNATPoolIdx"),
)
if mibBuilder.loadTexts:
    hpnicfNATPoolInfoEntry.setStatus("current")


class _HpnicfNATPoolIdx_Type(Integer32):
    """Custom type hpnicfNATPoolIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 320),
    )


_HpnicfNATPoolIdx_Type.__name__ = "Integer32"
_HpnicfNATPoolIdx_Object = MibTableColumn
hpnicfNATPoolIdx = _HpnicfNATPoolIdx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 1, 1, 1),
    _HpnicfNATPoolIdx_Type()
)
hpnicfNATPoolIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfNATPoolIdx.setStatus("current")
_HpnicfNATPoolStartIpAddr_Type = IpAddress
_HpnicfNATPoolStartIpAddr_Object = MibTableColumn
hpnicfNATPoolStartIpAddr = _HpnicfNATPoolStartIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 1, 1, 2),
    _HpnicfNATPoolStartIpAddr_Type()
)
hpnicfNATPoolStartIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNATPoolStartIpAddr.setStatus("current")
_HpnicfNATPoolEndIpAddr_Type = IpAddress
_HpnicfNATPoolEndIpAddr_Object = MibTableColumn
hpnicfNATPoolEndIpAddr = _HpnicfNATPoolEndIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 1, 1, 3),
    _HpnicfNATPoolEndIpAddr_Type()
)
hpnicfNATPoolEndIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNATPoolEndIpAddr.setStatus("current")


class _HpnicfNATPoolSlotNo_Type(Integer32):
    """Custom type hpnicfNATPoolSlotNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
        ValueRangeConstraint(255, 255),
    )


_HpnicfNATPoolSlotNo_Type.__name__ = "Integer32"
_HpnicfNATPoolSlotNo_Object = MibTableColumn
hpnicfNATPoolSlotNo = _HpnicfNATPoolSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 1, 1, 4),
    _HpnicfNATPoolSlotNo_Type()
)
hpnicfNATPoolSlotNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNATPoolSlotNo.setStatus("current")
_HpnicfNATPoolRefCounter_Type = Integer32
_HpnicfNATPoolRefCounter_Object = MibTableColumn
hpnicfNATPoolRefCounter = _HpnicfNATPoolRefCounter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 1, 1, 5),
    _HpnicfNATPoolRefCounter_Type()
)
hpnicfNATPoolRefCounter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNATPoolRefCounter.setStatus("current")
_HpnicfNATPoolRowStatus_Type = RowStatus
_HpnicfNATPoolRowStatus_Object = MibTableColumn
hpnicfNATPoolRowStatus = _HpnicfNATPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 1, 1, 6),
    _HpnicfNATPoolRowStatus_Type()
)
hpnicfNATPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNATPoolRowStatus.setStatus("current")
_HpnicfNATOutboundTable_Object = MibTable
hpnicfNATOutboundTable = _HpnicfNATOutboundTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfNATOutboundTable.setStatus("current")
_HpnicfNATOutboundEntry_Object = MibTableRow
hpnicfNATOutboundEntry = _HpnicfNATOutboundEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 2, 1)
)
hpnicfNATOutboundEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-NAT-MIB", "hpnicfNATOutboundAclNo"),
)
if mibBuilder.loadTexts:
    hpnicfNATOutboundEntry.setStatus("current")


class _HpnicfNATOutboundAclNo_Type(Integer32):
    """Custom type hpnicfNATOutboundAclNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 3999),
    )


_HpnicfNATOutboundAclNo_Type.__name__ = "Integer32"
_HpnicfNATOutboundAclNo_Object = MibTableColumn
hpnicfNATOutboundAclNo = _HpnicfNATOutboundAclNo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 2, 1, 1),
    _HpnicfNATOutboundAclNo_Type()
)
hpnicfNATOutboundAclNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfNATOutboundAclNo.setStatus("current")


class _HpnicfNATOutboundPoolIdx_Type(Integer32):
    """Custom type hpnicfNATOutboundPoolIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 320),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_HpnicfNATOutboundPoolIdx_Type.__name__ = "Integer32"
_HpnicfNATOutboundPoolIdx_Object = MibTableColumn
hpnicfNATOutboundPoolIdx = _HpnicfNATOutboundPoolIdx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 2, 1, 2),
    _HpnicfNATOutboundPoolIdx_Type()
)
hpnicfNATOutboundPoolIdx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNATOutboundPoolIdx.setStatus("current")


class _HpnicfNATOutboundIsNoPat_Type(Integer32):
    """Custom type hpnicfNATOutboundIsNoPat based on Integer32"""
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


_HpnicfNATOutboundIsNoPat_Type.__name__ = "Integer32"
_HpnicfNATOutboundIsNoPat_Object = MibTableColumn
hpnicfNATOutboundIsNoPat = _HpnicfNATOutboundIsNoPat_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 2, 1, 3),
    _HpnicfNATOutboundIsNoPat_Type()
)
hpnicfNATOutboundIsNoPat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNATOutboundIsNoPat.setStatus("current")


class _HpnicfNATOutboundSlotNo_Type(Integer32):
    """Custom type hpnicfNATOutboundSlotNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
        ValueRangeConstraint(255, 255),
    )


_HpnicfNATOutboundSlotNo_Type.__name__ = "Integer32"
_HpnicfNATOutboundSlotNo_Object = MibTableColumn
hpnicfNATOutboundSlotNo = _HpnicfNATOutboundSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 2, 1, 4),
    _HpnicfNATOutboundSlotNo_Type()
)
hpnicfNATOutboundSlotNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNATOutboundSlotNo.setStatus("current")
_HpnicfNATOutboundRowStatus_Type = RowStatus
_HpnicfNATOutboundRowStatus_Object = MibTableColumn
hpnicfNATOutboundRowStatus = _HpnicfNATOutboundRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 2, 1, 5),
    _HpnicfNATOutboundRowStatus_Type()
)
hpnicfNATOutboundRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNATOutboundRowStatus.setStatus("current")
_HpnicfNATServerTable_Object = MibTable
hpnicfNATServerTable = _HpnicfNATServerTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 3)
)
if mibBuilder.loadTexts:
    hpnicfNATServerTable.setStatus("current")
_HpnicfNATServerEntry_Object = MibTableRow
hpnicfNATServerEntry = _HpnicfNATServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 3, 1)
)
hpnicfNATServerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-NAT-MIB", "hpnicfNATServerProType"),
    (0, "HPN-ICF-NAT-MIB", "hpnicfNATServerGlobalIP"),
    (0, "HPN-ICF-NAT-MIB", "hpnicfNATServerStartGlobalPort"),
    (0, "HPN-ICF-NAT-MIB", "hpnicfNATServerVpnIndex"),
)
if mibBuilder.loadTexts:
    hpnicfNATServerEntry.setStatus("current")


class _HpnicfNATServerProType_Type(Integer32):
    """Custom type hpnicfNATServerProType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HpnicfNATServerProType_Type.__name__ = "Integer32"
_HpnicfNATServerProType_Object = MibTableColumn
hpnicfNATServerProType = _HpnicfNATServerProType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 3, 1, 1),
    _HpnicfNATServerProType_Type()
)
hpnicfNATServerProType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfNATServerProType.setStatus("current")
_HpnicfNATServerGlobalIP_Type = IpAddress
_HpnicfNATServerGlobalIP_Object = MibTableColumn
hpnicfNATServerGlobalIP = _HpnicfNATServerGlobalIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 3, 1, 2),
    _HpnicfNATServerGlobalIP_Type()
)
hpnicfNATServerGlobalIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfNATServerGlobalIP.setStatus("current")


class _HpnicfNATServerStartGlobalPort_Type(Integer32):
    """Custom type hpnicfNATServerStartGlobalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfNATServerStartGlobalPort_Type.__name__ = "Integer32"
_HpnicfNATServerStartGlobalPort_Object = MibTableColumn
hpnicfNATServerStartGlobalPort = _HpnicfNATServerStartGlobalPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 3, 1, 3),
    _HpnicfNATServerStartGlobalPort_Type()
)
hpnicfNATServerStartGlobalPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfNATServerStartGlobalPort.setStatus("current")


class _HpnicfNATServerEndGlobalPort_Type(Integer32):
    """Custom type hpnicfNATServerEndGlobalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfNATServerEndGlobalPort_Type.__name__ = "Integer32"
_HpnicfNATServerEndGlobalPort_Object = MibTableColumn
hpnicfNATServerEndGlobalPort = _HpnicfNATServerEndGlobalPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 3, 1, 4),
    _HpnicfNATServerEndGlobalPort_Type()
)
hpnicfNATServerEndGlobalPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNATServerEndGlobalPort.setStatus("current")
_HpnicfNATServerStartInsideIP_Type = IpAddress
_HpnicfNATServerStartInsideIP_Object = MibTableColumn
hpnicfNATServerStartInsideIP = _HpnicfNATServerStartInsideIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 3, 1, 5),
    _HpnicfNATServerStartInsideIP_Type()
)
hpnicfNATServerStartInsideIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNATServerStartInsideIP.setStatus("current")
_HpnicfNATServerEndInsideIP_Type = IpAddress
_HpnicfNATServerEndInsideIP_Object = MibTableColumn
hpnicfNATServerEndInsideIP = _HpnicfNATServerEndInsideIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 3, 1, 6),
    _HpnicfNATServerEndInsideIP_Type()
)
hpnicfNATServerEndInsideIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNATServerEndInsideIP.setStatus("current")


class _HpnicfNATServerInsidePort_Type(Integer32):
    """Custom type hpnicfNATServerInsidePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfNATServerInsidePort_Type.__name__ = "Integer32"
_HpnicfNATServerInsidePort_Object = MibTableColumn
hpnicfNATServerInsidePort = _HpnicfNATServerInsidePort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 3, 1, 7),
    _HpnicfNATServerInsidePort_Type()
)
hpnicfNATServerInsidePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNATServerInsidePort.setStatus("current")


class _HpnicfNATServerSlotNo_Type(Integer32):
    """Custom type hpnicfNATServerSlotNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
        ValueRangeConstraint(255, 255),
    )


_HpnicfNATServerSlotNo_Type.__name__ = "Integer32"
_HpnicfNATServerSlotNo_Object = MibTableColumn
hpnicfNATServerSlotNo = _HpnicfNATServerSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 3, 1, 8),
    _HpnicfNATServerSlotNo_Type()
)
hpnicfNATServerSlotNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNATServerSlotNo.setStatus("current")


class _HpnicfNATServerVpnIndex_Type(Integer32):
    """Custom type hpnicfNATServerVpnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfNATServerVpnIndex_Type.__name__ = "Integer32"
_HpnicfNATServerVpnIndex_Object = MibTableColumn
hpnicfNATServerVpnIndex = _HpnicfNATServerVpnIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 3, 1, 10),
    _HpnicfNATServerVpnIndex_Type()
)
hpnicfNATServerVpnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfNATServerVpnIndex.setStatus("current")


class _HpnicfNATServerAclNumber_Type(Integer32):
    """Custom type hpnicfNATServerAclNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_HpnicfNATServerAclNumber_Type.__name__ = "Integer32"
_HpnicfNATServerAclNumber_Object = MibTableColumn
hpnicfNATServerAclNumber = _HpnicfNATServerAclNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 3, 1, 11),
    _HpnicfNATServerAclNumber_Type()
)
hpnicfNATServerAclNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNATServerAclNumber.setStatus("current")
_HpnicfNATServerRowStatus_Type = RowStatus
_HpnicfNATServerRowStatus_Object = MibTableColumn
hpnicfNATServerRowStatus = _HpnicfNATServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 3, 1, 12),
    _HpnicfNATServerRowStatus_Type()
)
hpnicfNATServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNATServerRowStatus.setStatus("current")
_HpnicfNATTimeOutTable_Object = MibTable
hpnicfNATTimeOutTable = _HpnicfNATTimeOutTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 4)
)
if mibBuilder.loadTexts:
    hpnicfNATTimeOutTable.setStatus("current")
_HpnicfNATTimeOutEntry_Object = MibTableRow
hpnicfNATTimeOutEntry = _HpnicfNATTimeOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 4, 1)
)
hpnicfNATTimeOutEntry.setIndexNames(
    (0, "HPN-ICF-NAT-MIB", "hpnicfNATTimeOutProtocol"),
)
if mibBuilder.loadTexts:
    hpnicfNATTimeOutEntry.setStatus("current")


class _HpnicfNATTimeOutProtocol_Type(Integer32):
    """Custom type hpnicfNATTimeOutProtocol based on Integer32"""
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


_HpnicfNATTimeOutProtocol_Type.__name__ = "Integer32"
_HpnicfNATTimeOutProtocol_Object = MibTableColumn
hpnicfNATTimeOutProtocol = _HpnicfNATTimeOutProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 4, 1, 1),
    _HpnicfNATTimeOutProtocol_Type()
)
hpnicfNATTimeOutProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfNATTimeOutProtocol.setStatus("current")


class _HpnicfNATTimeOutTimeValue_Type(Integer32):
    """Custom type hpnicfNATTimeOutTimeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 86400),
    )


_HpnicfNATTimeOutTimeValue_Type.__name__ = "Integer32"
_HpnicfNATTimeOutTimeValue_Object = MibTableColumn
hpnicfNATTimeOutTimeValue = _HpnicfNATTimeOutTimeValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 4, 1, 2),
    _HpnicfNATTimeOutTimeValue_Type()
)
hpnicfNATTimeOutTimeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfNATTimeOutTimeValue.setStatus("current")
_HpnicfNATBLEnableTable_Object = MibTable
hpnicfNATBLEnableTable = _HpnicfNATBLEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 5)
)
if mibBuilder.loadTexts:
    hpnicfNATBLEnableTable.setStatus("current")
_HpnicfNATBLEnableEntry_Object = MibTableRow
hpnicfNATBLEnableEntry = _HpnicfNATBLEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 5, 1)
)
hpnicfNATBLEnableEntry.setIndexNames(
    (0, "HPN-ICF-NAT-MIB", "hpnicfNATBLEnableSlotNo"),
)
if mibBuilder.loadTexts:
    hpnicfNATBLEnableEntry.setStatus("current")


class _HpnicfNATBLEnableSlotNo_Type(Integer32):
    """Custom type hpnicfNATBLEnableSlotNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
        ValueRangeConstraint(255, 255),
    )


_HpnicfNATBLEnableSlotNo_Type.__name__ = "Integer32"
_HpnicfNATBLEnableSlotNo_Object = MibTableColumn
hpnicfNATBLEnableSlotNo = _HpnicfNATBLEnableSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 5, 1, 1),
    _HpnicfNATBLEnableSlotNo_Type()
)
hpnicfNATBLEnableSlotNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfNATBLEnableSlotNo.setStatus("current")


class _HpnicfNATBLEnable_Type(Integer32):
    """Custom type hpnicfNATBLEnable based on Integer32"""
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


_HpnicfNATBLEnable_Type.__name__ = "Integer32"
_HpnicfNATBLEnable_Object = MibTableColumn
hpnicfNATBLEnable = _HpnicfNATBLEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 5, 1, 2),
    _HpnicfNATBLEnable_Type()
)
hpnicfNATBLEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfNATBLEnable.setStatus("current")
_HpnicfNATBLIPConnectLimitParaTable_Object = MibTable
hpnicfNATBLIPConnectLimitParaTable = _HpnicfNATBLIPConnectLimitParaTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 6)
)
if mibBuilder.loadTexts:
    hpnicfNATBLIPConnectLimitParaTable.setStatus("current")
_HpnicfNATBLIPConnectLimitParaEntry_Object = MibTableRow
hpnicfNATBLIPConnectLimitParaEntry = _HpnicfNATBLIPConnectLimitParaEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 6, 1)
)
hpnicfNATBLIPConnectLimitParaEntry.setIndexNames(
    (0, "HPN-ICF-NAT-MIB", "hpnicfNATBLIPConnectLimitParaIP"),
)
if mibBuilder.loadTexts:
    hpnicfNATBLIPConnectLimitParaEntry.setStatus("current")
_HpnicfNATBLIPConnectLimitParaIP_Type = IpAddress
_HpnicfNATBLIPConnectLimitParaIP_Object = MibTableColumn
hpnicfNATBLIPConnectLimitParaIP = _HpnicfNATBLIPConnectLimitParaIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 6, 1, 1),
    _HpnicfNATBLIPConnectLimitParaIP_Type()
)
hpnicfNATBLIPConnectLimitParaIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfNATBLIPConnectLimitParaIP.setStatus("current")


class _HpnicfNATBLIPConnectHighValue_Type(Integer32):
    """Custom type hpnicfNATBLIPConnectHighValue based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 20000),
    )


_HpnicfNATBLIPConnectHighValue_Type.__name__ = "Integer32"
_HpnicfNATBLIPConnectHighValue_Object = MibTableColumn
hpnicfNATBLIPConnectHighValue = _HpnicfNATBLIPConnectHighValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 6, 1, 2),
    _HpnicfNATBLIPConnectHighValue_Type()
)
hpnicfNATBLIPConnectHighValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNATBLIPConnectHighValue.setStatus("current")


class _HpnicfNATBLIPConnectLowValue_Type(Integer32):
    """Custom type hpnicfNATBLIPConnectLowValue based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 20000),
    )


_HpnicfNATBLIPConnectLowValue_Type.__name__ = "Integer32"
_HpnicfNATBLIPConnectLowValue_Object = MibTableColumn
hpnicfNATBLIPConnectLowValue = _HpnicfNATBLIPConnectLowValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 6, 1, 3),
    _HpnicfNATBLIPConnectLowValue_Type()
)
hpnicfNATBLIPConnectLowValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNATBLIPConnectLowValue.setStatus("current")


class _HpnicfNATBLIPUseSpecialConnectRate_Type(Integer32):
    """Custom type hpnicfNATBLIPUseSpecialConnectRate based on Integer32"""
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


_HpnicfNATBLIPUseSpecialConnectRate_Type.__name__ = "Integer32"
_HpnicfNATBLIPUseSpecialConnectRate_Object = MibTableColumn
hpnicfNATBLIPUseSpecialConnectRate = _HpnicfNATBLIPUseSpecialConnectRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 6, 1, 4),
    _HpnicfNATBLIPUseSpecialConnectRate_Type()
)
hpnicfNATBLIPUseSpecialConnectRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNATBLIPUseSpecialConnectRate.setStatus("current")
_HpnicfNATBLIPConnectLimitRowStatus_Type = RowStatus
_HpnicfNATBLIPConnectLimitRowStatus_Object = MibTableColumn
hpnicfNATBLIPConnectLimitRowStatus = _HpnicfNATBLIPConnectLimitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 6, 1, 5),
    _HpnicfNATBLIPConnectLimitRowStatus_Type()
)
hpnicfNATBLIPConnectLimitRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNATBLIPConnectLimitRowStatus.setStatus("current")
_HpnicfNATBLManagerTable_Object = MibTable
hpnicfNATBLManagerTable = _HpnicfNATBLManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 7)
)
if mibBuilder.loadTexts:
    hpnicfNATBLManagerTable.setStatus("current")
_HpnicfNATBLManagerEntry_Object = MibTableRow
hpnicfNATBLManagerEntry = _HpnicfNATBLManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 7, 1)
)
hpnicfNATBLManagerEntry.setIndexNames(
    (0, "HPN-ICF-NAT-MIB", "hpnicfNATBLIpAdress"),
    (0, "HPN-ICF-NAT-MIB", "hpnicfNATBLSlotNo"),
)
if mibBuilder.loadTexts:
    hpnicfNATBLManagerEntry.setStatus("current")
_HpnicfNATBLIpAdress_Type = IpAddress
_HpnicfNATBLIpAdress_Object = MibTableColumn
hpnicfNATBLIpAdress = _HpnicfNATBLIpAdress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 7, 1, 1),
    _HpnicfNATBLIpAdress_Type()
)
hpnicfNATBLIpAdress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfNATBLIpAdress.setStatus("current")


class _HpnicfNATBLSlotNo_Type(Integer32):
    """Custom type hpnicfNATBLSlotNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_HpnicfNATBLSlotNo_Type.__name__ = "Integer32"
_HpnicfNATBLSlotNo_Object = MibTableColumn
hpnicfNATBLSlotNo = _HpnicfNATBLSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 7, 1, 2),
    _HpnicfNATBLSlotNo_Type()
)
hpnicfNATBLSlotNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfNATBLSlotNo.setStatus("current")
_HpnicfNATBLConSum_Type = Integer32
_HpnicfNATBLConSum_Object = MibTableColumn
hpnicfNATBLConSum = _HpnicfNATBLConSum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 7, 1, 3),
    _HpnicfNATBLConSum_Type()
)
hpnicfNATBLConSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNATBLConSum.setStatus("current")


class _HpnicfNATBLConSpd_Type(Integer32):
    """Custom type hpnicfNATBLConSpd based on Integer32"""
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


_HpnicfNATBLConSpd_Type.__name__ = "Integer32"
_HpnicfNATBLConSpd_Object = MibTableColumn
hpnicfNATBLConSpd = _HpnicfNATBLConSpd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 7, 1, 4),
    _HpnicfNATBLConSpd_Type()
)
hpnicfNATBLConSpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNATBLConSpd.setStatus("current")
_HpnicfNATStatTable_Object = MibTable
hpnicfNATStatTable = _HpnicfNATStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 8)
)
if mibBuilder.loadTexts:
    hpnicfNATStatTable.setStatus("current")
_HpnicfNATStatEntry_Object = MibTableRow
hpnicfNATStatEntry = _HpnicfNATStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 8, 1)
)
hpnicfNATStatEntry.setIndexNames(
    (0, "HPN-ICF-NAT-MIB", "hpnicfNATStatNATBoardNo"),
)
if mibBuilder.loadTexts:
    hpnicfNATStatEntry.setStatus("current")


class _HpnicfNATStatNATBoardNo_Type(Integer32):
    """Custom type hpnicfNATStatNATBoardNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
        ValueRangeConstraint(255, 255),
    )


_HpnicfNATStatNATBoardNo_Type.__name__ = "Integer32"
_HpnicfNATStatNATBoardNo_Object = MibTableColumn
hpnicfNATStatNATBoardNo = _HpnicfNATStatNATBoardNo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 8, 1, 1),
    _HpnicfNATStatNATBoardNo_Type()
)
hpnicfNATStatNATBoardNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfNATStatNATBoardNo.setStatus("current")
_HpnicfNATStatActiveTblCount_Type = Counter32
_HpnicfNATStatActiveTblCount_Object = MibTableColumn
hpnicfNATStatActiveTblCount = _HpnicfNATStatActiveTblCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 8, 1, 2),
    _HpnicfNATStatActiveTblCount_Type()
)
hpnicfNATStatActiveTblCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNATStatActiveTblCount.setStatus("current")
_HpnicfNATStatActiveTblCountInNP_Type = Counter32
_HpnicfNATStatActiveTblCountInNP_Object = MibTableColumn
hpnicfNATStatActiveTblCountInNP = _HpnicfNATStatActiveTblCountInNP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 8, 1, 3),
    _HpnicfNATStatActiveTblCountInNP_Type()
)
hpnicfNATStatActiveTblCountInNP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNATStatActiveTblCountInNP.setStatus("current")
_HpnicfNATStatActiveNatTblCount_Type = Counter32
_HpnicfNATStatActiveNatTblCount_Object = MibTableColumn
hpnicfNATStatActiveNatTblCount = _HpnicfNATStatActiveNatTblCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 8, 1, 4),
    _HpnicfNATStatActiveNatTblCount_Type()
)
hpnicfNATStatActiveNatTblCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNATStatActiveNatTblCount.setStatus("current")
_HpnicfNATStatActiveSvrTblCount_Type = Counter32
_HpnicfNATStatActiveSvrTblCount_Object = MibTableColumn
hpnicfNATStatActiveSvrTblCount = _HpnicfNATStatActiveSvrTblCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 8, 1, 5),
    _HpnicfNATStatActiveSvrTblCount_Type()
)
hpnicfNATStatActiveSvrTblCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNATStatActiveSvrTblCount.setStatus("current")
_HpnicfNATStatActivePoolTblCount_Type = Counter32
_HpnicfNATStatActivePoolTblCount_Object = MibTableColumn
hpnicfNATStatActivePoolTblCount = _HpnicfNATStatActivePoolTblCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 8, 1, 6),
    _HpnicfNATStatActivePoolTblCount_Type()
)
hpnicfNATStatActivePoolTblCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNATStatActivePoolTblCount.setStatus("current")
_HpnicfNATStatNumOfUsedPort_Type = Counter32
_HpnicfNATStatNumOfUsedPort_Object = MibTableColumn
hpnicfNATStatNumOfUsedPort = _HpnicfNATStatNumOfUsedPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 8, 1, 7),
    _HpnicfNATStatNumOfUsedPort_Type()
)
hpnicfNATStatNumOfUsedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNATStatNumOfUsedPort.setStatus("current")
_HpnicfNATStatNumOfGoodPkt_Type = Counter32
_HpnicfNATStatNumOfGoodPkt_Object = MibTableColumn
hpnicfNATStatNumOfGoodPkt = _HpnicfNATStatNumOfGoodPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 8, 1, 8),
    _HpnicfNATStatNumOfGoodPkt_Type()
)
hpnicfNATStatNumOfGoodPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNATStatNumOfGoodPkt.setStatus("current")
_HpnicfNATStatNumOfBadPkt_Type = Counter32
_HpnicfNATStatNumOfBadPkt_Object = MibTableColumn
hpnicfNATStatNumOfBadPkt = _HpnicfNATStatNumOfBadPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 8, 1, 9),
    _HpnicfNATStatNumOfBadPkt_Type()
)
hpnicfNATStatNumOfBadPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNATStatNumOfBadPkt.setStatus("current")
_HpnicfNATStaticSessionCount_Type = Integer32
_HpnicfNATStaticSessionCount_Object = MibTableColumn
hpnicfNATStaticSessionCount = _HpnicfNATStaticSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 8, 1, 10),
    _HpnicfNATStaticSessionCount_Type()
)
hpnicfNATStaticSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNATStaticSessionCount.setStatus("current")
_HpnicfNATFragmentSessionCount_Type = Integer32
_HpnicfNATFragmentSessionCount_Object = MibTableColumn
hpnicfNATFragmentSessionCount = _HpnicfNATFragmentSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 8, 1, 11),
    _HpnicfNATFragmentSessionCount_Type()
)
hpnicfNATFragmentSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNATFragmentSessionCount.setStatus("current")
_HpnicfNATSequenceSessionCount_Type = Integer32
_HpnicfNATSequenceSessionCount_Object = MibTableColumn
hpnicfNATSequenceSessionCount = _HpnicfNATSequenceSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 8, 1, 12),
    _HpnicfNATSequenceSessionCount_Type()
)
hpnicfNATSequenceSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNATSequenceSessionCount.setStatus("current")
_HpnicfNATLogCount_Type = Integer32
_HpnicfNATLogCount_Object = MibTableColumn
hpnicfNATLogCount = _HpnicfNATLogCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 8, 1, 13),
    _HpnicfNATLogCount_Type()
)
hpnicfNATLogCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNATLogCount.setStatus("current")
_HpnicfNATSessionTable_Object = MibTable
hpnicfNATSessionTable = _HpnicfNATSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 9)
)
if mibBuilder.loadTexts:
    hpnicfNATSessionTable.setStatus("current")
_HpnicfNATSessionEntry_Object = MibTableRow
hpnicfNATSessionEntry = _HpnicfNATSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 9, 1)
)
hpnicfNATSessionEntry.setIndexNames(
    (0, "HPN-ICF-NAT-MIB", "hpnicfNATSessionHashNumber"),
    (0, "HPN-ICF-NAT-MIB", "hpnicfNATSessionProtocol"),
    (0, "HPN-ICF-NAT-MIB", "hpnicfNATSessionInsideIP"),
    (0, "HPN-ICF-NAT-MIB", "hpnicfNATSessionInsidePort"),
    (0, "HPN-ICF-NAT-MIB", "hpnicfNATSessionPeerIP"),
    (0, "HPN-ICF-NAT-MIB", "hpnicfNATSessionPeerPort"),
    (0, "HPN-ICF-NAT-MIB", "hpnicfNATSessionVpnIndex"),
)
if mibBuilder.loadTexts:
    hpnicfNATSessionEntry.setStatus("current")


class _HpnicfNATSessionHashNumber_Type(Integer32):
    """Custom type hpnicfNATSessionHashNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300000),
    )


_HpnicfNATSessionHashNumber_Type.__name__ = "Integer32"
_HpnicfNATSessionHashNumber_Object = MibTableColumn
hpnicfNATSessionHashNumber = _HpnicfNATSessionHashNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 9, 1, 1),
    _HpnicfNATSessionHashNumber_Type()
)
hpnicfNATSessionHashNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfNATSessionHashNumber.setStatus("current")


class _HpnicfNATSessionProtocol_Type(Integer32):
    """Custom type hpnicfNATSessionProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HpnicfNATSessionProtocol_Type.__name__ = "Integer32"
_HpnicfNATSessionProtocol_Object = MibTableColumn
hpnicfNATSessionProtocol = _HpnicfNATSessionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 9, 1, 2),
    _HpnicfNATSessionProtocol_Type()
)
hpnicfNATSessionProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfNATSessionProtocol.setStatus("current")
_HpnicfNATSessionGlobalIP_Type = IpAddress
_HpnicfNATSessionGlobalIP_Object = MibTableColumn
hpnicfNATSessionGlobalIP = _HpnicfNATSessionGlobalIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 9, 1, 3),
    _HpnicfNATSessionGlobalIP_Type()
)
hpnicfNATSessionGlobalIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNATSessionGlobalIP.setStatus("current")


class _HpnicfNATSessionGlobalPort_Type(Integer32):
    """Custom type hpnicfNATSessionGlobalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfNATSessionGlobalPort_Type.__name__ = "Integer32"
_HpnicfNATSessionGlobalPort_Object = MibTableColumn
hpnicfNATSessionGlobalPort = _HpnicfNATSessionGlobalPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 9, 1, 4),
    _HpnicfNATSessionGlobalPort_Type()
)
hpnicfNATSessionGlobalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNATSessionGlobalPort.setStatus("current")
_HpnicfNATSessionInsideIP_Type = IpAddress
_HpnicfNATSessionInsideIP_Object = MibTableColumn
hpnicfNATSessionInsideIP = _HpnicfNATSessionInsideIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 9, 1, 5),
    _HpnicfNATSessionInsideIP_Type()
)
hpnicfNATSessionInsideIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfNATSessionInsideIP.setStatus("current")


class _HpnicfNATSessionInsidePort_Type(Integer32):
    """Custom type hpnicfNATSessionInsidePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfNATSessionInsidePort_Type.__name__ = "Integer32"
_HpnicfNATSessionInsidePort_Object = MibTableColumn
hpnicfNATSessionInsidePort = _HpnicfNATSessionInsidePort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 9, 1, 6),
    _HpnicfNATSessionInsidePort_Type()
)
hpnicfNATSessionInsidePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfNATSessionInsidePort.setStatus("current")
_HpnicfNATSessionPeerIP_Type = IpAddress
_HpnicfNATSessionPeerIP_Object = MibTableColumn
hpnicfNATSessionPeerIP = _HpnicfNATSessionPeerIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 9, 1, 7),
    _HpnicfNATSessionPeerIP_Type()
)
hpnicfNATSessionPeerIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfNATSessionPeerIP.setStatus("current")


class _HpnicfNATSessionPeerPort_Type(Integer32):
    """Custom type hpnicfNATSessionPeerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfNATSessionPeerPort_Type.__name__ = "Integer32"
_HpnicfNATSessionPeerPort_Object = MibTableColumn
hpnicfNATSessionPeerPort = _HpnicfNATSessionPeerPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 9, 1, 8),
    _HpnicfNATSessionPeerPort_Type()
)
hpnicfNATSessionPeerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfNATSessionPeerPort.setStatus("current")


class _HpnicfNATSessionVpnIndex_Type(Integer32):
    """Custom type hpnicfNATSessionVpnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfNATSessionVpnIndex_Type.__name__ = "Integer32"
_HpnicfNATSessionVpnIndex_Object = MibTableColumn
hpnicfNATSessionVpnIndex = _HpnicfNATSessionVpnIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 9, 1, 9),
    _HpnicfNATSessionVpnIndex_Type()
)
hpnicfNATSessionVpnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfNATSessionVpnIndex.setStatus("current")
_HpnicfNATSessionTTL_Type = Integer32
_HpnicfNATSessionTTL_Object = MibTableColumn
hpnicfNATSessionTTL = _HpnicfNATSessionTTL_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 9, 1, 10),
    _HpnicfNATSessionTTL_Type()
)
hpnicfNATSessionTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNATSessionTTL.setStatus("current")
_HpnicfNATSessionStatus_Type = Integer32
_HpnicfNATSessionStatus_Object = MibTableColumn
hpnicfNATSessionStatus = _HpnicfNATSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 9, 1, 11),
    _HpnicfNATSessionStatus_Type()
)
hpnicfNATSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNATSessionStatus.setStatus("current")
_HpnicfNATSessionLeftTime_Type = TimeTicks
_HpnicfNATSessionLeftTime_Object = MibTableColumn
hpnicfNATSessionLeftTime = _HpnicfNATSessionLeftTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 9, 1, 12),
    _HpnicfNATSessionLeftTime_Type()
)
hpnicfNATSessionLeftTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNATSessionLeftTime.setStatus("current")
_HpnicfNATStaticConfTable_Object = MibTable
hpnicfNATStaticConfTable = _HpnicfNATStaticConfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 10)
)
if mibBuilder.loadTexts:
    hpnicfNATStaticConfTable.setStatus("current")
_HpnicfNATStaticConfEntry_Object = MibTableRow
hpnicfNATStaticConfEntry = _HpnicfNATStaticConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 10, 1)
)
hpnicfNATStaticConfEntry.setIndexNames(
    (0, "HPN-ICF-NAT-MIB", "hpnicfNATStaticInsideIp"),
)
if mibBuilder.loadTexts:
    hpnicfNATStaticConfEntry.setStatus("current")
_HpnicfNATStaticInsideIp_Type = IpAddress
_HpnicfNATStaticInsideIp_Object = MibTableColumn
hpnicfNATStaticInsideIp = _HpnicfNATStaticInsideIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 10, 1, 1),
    _HpnicfNATStaticInsideIp_Type()
)
hpnicfNATStaticInsideIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfNATStaticInsideIp.setStatus("current")
_HpnicfNATStaticGlobalIp_Type = IpAddress
_HpnicfNATStaticGlobalIp_Object = MibTableColumn
hpnicfNATStaticGlobalIp = _HpnicfNATStaticGlobalIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 10, 1, 2),
    _HpnicfNATStaticGlobalIp_Type()
)
hpnicfNATStaticGlobalIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNATStaticGlobalIp.setStatus("current")
_HpnicfNATStaticRowStatus_Type = RowStatus
_HpnicfNATStaticRowStatus_Object = MibTableColumn
hpnicfNATStaticRowStatus = _HpnicfNATStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 10, 1, 3),
    _HpnicfNATStaticRowStatus_Type()
)
hpnicfNATStaticRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNATStaticRowStatus.setStatus("current")
_HpnicfNATStaticEnableTable_Object = MibTable
hpnicfNATStaticEnableTable = _HpnicfNATStaticEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 11)
)
if mibBuilder.loadTexts:
    hpnicfNATStaticEnableTable.setStatus("current")
_HpnicfNATStaticEnableEntry_Object = MibTableRow
hpnicfNATStaticEnableEntry = _HpnicfNATStaticEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 11, 1)
)
hpnicfNATStaticEnableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfNATStaticEnableEntry.setStatus("current")


class _HpnicfNATStaticEnable_Type(Integer32):
    """Custom type hpnicfNATStaticEnable based on Integer32"""
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


_HpnicfNATStaticEnable_Type.__name__ = "Integer32"
_HpnicfNATStaticEnable_Object = MibTableColumn
hpnicfNATStaticEnable = _HpnicfNATStaticEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 11, 1, 2),
    _HpnicfNATStaticEnable_Type()
)
hpnicfNATStaticEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfNATStaticEnable.setStatus("current")
_HpnicfNATDnsMapTable_Object = MibTable
hpnicfNATDnsMapTable = _HpnicfNATDnsMapTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 12)
)
if mibBuilder.loadTexts:
    hpnicfNATDnsMapTable.setStatus("current")
_HpnicfNATDnsMapEntry_Object = MibTableRow
hpnicfNATDnsMapEntry = _HpnicfNATDnsMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 12, 1)
)
hpnicfNATDnsMapEntry.setIndexNames(
    (0, "HPN-ICF-NAT-MIB", "hpnicfNATDnsMapDomainName"),
)
if mibBuilder.loadTexts:
    hpnicfNATDnsMapEntry.setStatus("current")
_HpnicfNATDnsMapDomainName_Type = DisplayString
_HpnicfNATDnsMapDomainName_Object = MibTableColumn
hpnicfNATDnsMapDomainName = _HpnicfNATDnsMapDomainName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 12, 1, 1),
    _HpnicfNATDnsMapDomainName_Type()
)
hpnicfNATDnsMapDomainName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfNATDnsMapDomainName.setStatus("current")
_HpnicfNATDnsMapGlobalIp_Type = IpAddress
_HpnicfNATDnsMapGlobalIp_Object = MibTableColumn
hpnicfNATDnsMapGlobalIp = _HpnicfNATDnsMapGlobalIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 12, 1, 2),
    _HpnicfNATDnsMapGlobalIp_Type()
)
hpnicfNATDnsMapGlobalIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNATDnsMapGlobalIp.setStatus("current")


class _HpnicfNATDnsMapGlobalPort_Type(Integer32):
    """Custom type hpnicfNATDnsMapGlobalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfNATDnsMapGlobalPort_Type.__name__ = "Integer32"
_HpnicfNATDnsMapGlobalPort_Object = MibTableColumn
hpnicfNATDnsMapGlobalPort = _HpnicfNATDnsMapGlobalPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 12, 1, 3),
    _HpnicfNATDnsMapGlobalPort_Type()
)
hpnicfNATDnsMapGlobalPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNATDnsMapGlobalPort.setStatus("current")


class _HpnicfNATDnsMapProtocolType_Type(Integer32):
    """Custom type hpnicfNATDnsMapProtocolType based on Integer32"""
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


_HpnicfNATDnsMapProtocolType_Type.__name__ = "Integer32"
_HpnicfNATDnsMapProtocolType_Object = MibTableColumn
hpnicfNATDnsMapProtocolType = _HpnicfNATDnsMapProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 12, 1, 4),
    _HpnicfNATDnsMapProtocolType_Type()
)
hpnicfNATDnsMapProtocolType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNATDnsMapProtocolType.setStatus("current")
_HpnicfNATDnsMapLastUseTime_Type = TimeTicks
_HpnicfNATDnsMapLastUseTime_Object = MibTableColumn
hpnicfNATDnsMapLastUseTime = _HpnicfNATDnsMapLastUseTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 12, 1, 5),
    _HpnicfNATDnsMapLastUseTime_Type()
)
hpnicfNATDnsMapLastUseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNATDnsMapLastUseTime.setStatus("current")
_HpnicfNATDnsMapRowStatus_Type = RowStatus
_HpnicfNATDnsMapRowStatus_Object = MibTableColumn
hpnicfNATDnsMapRowStatus = _HpnicfNATDnsMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18, 2, 12, 1, 6),
    _HpnicfNATDnsMapRowStatus_Type()
)
hpnicfNATDnsMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNATDnsMapRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-NAT-MIB",
    **{"hpnicfNat": hpnicfNat,
       "hpnicfNATGlobalVars": hpnicfNATGlobalVars,
       "hpnicfNATClearSession": hpnicfNATClearSession,
       "hpnicfNATClearSessionSlotNo": hpnicfNATClearSessionSlotNo,
       "hpnicfNATBLConnectLimitPara": hpnicfNATBLConnectLimitPara,
       "hpnicfNATBLConnectHighValue": hpnicfNATBLConnectHighValue,
       "hpnicfNATBLConnectLowValue": hpnicfNATBLConnectLowValue,
       "hpnicfNATBLConnectHighRate": hpnicfNATBLConnectHighRate,
       "hpnicfNATBLConnectLowRate": hpnicfNATBLConnectLowRate,
       "hpnicfNATBLSpecialConnectHighRate": hpnicfNATBLSpecialConnectHighRate,
       "hpnicfNATBLSpecialConnectLowRate": hpnicfNATBLSpecialConnectLowRate,
       "hpnicfNATBLCtrlEnable": hpnicfNATBLCtrlEnable,
       "hpnicfNATBLConnectSumEnable": hpnicfNATBLConnectSumEnable,
       "hpnicfNATBLConnectRateEnable": hpnicfNATBLConnectRateEnable,
       "hpnicfNATNPTimer": hpnicfNATNPTimer,
       "hpnicfNATNPAgingTime": hpnicfNATNPAgingTime,
       "hpnicfNATMibObjects": hpnicfNATMibObjects,
       "hpnicfNATPoolInfoTable": hpnicfNATPoolInfoTable,
       "hpnicfNATPoolInfoEntry": hpnicfNATPoolInfoEntry,
       "hpnicfNATPoolIdx": hpnicfNATPoolIdx,
       "hpnicfNATPoolStartIpAddr": hpnicfNATPoolStartIpAddr,
       "hpnicfNATPoolEndIpAddr": hpnicfNATPoolEndIpAddr,
       "hpnicfNATPoolSlotNo": hpnicfNATPoolSlotNo,
       "hpnicfNATPoolRefCounter": hpnicfNATPoolRefCounter,
       "hpnicfNATPoolRowStatus": hpnicfNATPoolRowStatus,
       "hpnicfNATOutboundTable": hpnicfNATOutboundTable,
       "hpnicfNATOutboundEntry": hpnicfNATOutboundEntry,
       "hpnicfNATOutboundAclNo": hpnicfNATOutboundAclNo,
       "hpnicfNATOutboundPoolIdx": hpnicfNATOutboundPoolIdx,
       "hpnicfNATOutboundIsNoPat": hpnicfNATOutboundIsNoPat,
       "hpnicfNATOutboundSlotNo": hpnicfNATOutboundSlotNo,
       "hpnicfNATOutboundRowStatus": hpnicfNATOutboundRowStatus,
       "hpnicfNATServerTable": hpnicfNATServerTable,
       "hpnicfNATServerEntry": hpnicfNATServerEntry,
       "hpnicfNATServerProType": hpnicfNATServerProType,
       "hpnicfNATServerGlobalIP": hpnicfNATServerGlobalIP,
       "hpnicfNATServerStartGlobalPort": hpnicfNATServerStartGlobalPort,
       "hpnicfNATServerEndGlobalPort": hpnicfNATServerEndGlobalPort,
       "hpnicfNATServerStartInsideIP": hpnicfNATServerStartInsideIP,
       "hpnicfNATServerEndInsideIP": hpnicfNATServerEndInsideIP,
       "hpnicfNATServerInsidePort": hpnicfNATServerInsidePort,
       "hpnicfNATServerSlotNo": hpnicfNATServerSlotNo,
       "hpnicfNATServerVpnIndex": hpnicfNATServerVpnIndex,
       "hpnicfNATServerAclNumber": hpnicfNATServerAclNumber,
       "hpnicfNATServerRowStatus": hpnicfNATServerRowStatus,
       "hpnicfNATTimeOutTable": hpnicfNATTimeOutTable,
       "hpnicfNATTimeOutEntry": hpnicfNATTimeOutEntry,
       "hpnicfNATTimeOutProtocol": hpnicfNATTimeOutProtocol,
       "hpnicfNATTimeOutTimeValue": hpnicfNATTimeOutTimeValue,
       "hpnicfNATBLEnableTable": hpnicfNATBLEnableTable,
       "hpnicfNATBLEnableEntry": hpnicfNATBLEnableEntry,
       "hpnicfNATBLEnableSlotNo": hpnicfNATBLEnableSlotNo,
       "hpnicfNATBLEnable": hpnicfNATBLEnable,
       "hpnicfNATBLIPConnectLimitParaTable": hpnicfNATBLIPConnectLimitParaTable,
       "hpnicfNATBLIPConnectLimitParaEntry": hpnicfNATBLIPConnectLimitParaEntry,
       "hpnicfNATBLIPConnectLimitParaIP": hpnicfNATBLIPConnectLimitParaIP,
       "hpnicfNATBLIPConnectHighValue": hpnicfNATBLIPConnectHighValue,
       "hpnicfNATBLIPConnectLowValue": hpnicfNATBLIPConnectLowValue,
       "hpnicfNATBLIPUseSpecialConnectRate": hpnicfNATBLIPUseSpecialConnectRate,
       "hpnicfNATBLIPConnectLimitRowStatus": hpnicfNATBLIPConnectLimitRowStatus,
       "hpnicfNATBLManagerTable": hpnicfNATBLManagerTable,
       "hpnicfNATBLManagerEntry": hpnicfNATBLManagerEntry,
       "hpnicfNATBLIpAdress": hpnicfNATBLIpAdress,
       "hpnicfNATBLSlotNo": hpnicfNATBLSlotNo,
       "hpnicfNATBLConSum": hpnicfNATBLConSum,
       "hpnicfNATBLConSpd": hpnicfNATBLConSpd,
       "hpnicfNATStatTable": hpnicfNATStatTable,
       "hpnicfNATStatEntry": hpnicfNATStatEntry,
       "hpnicfNATStatNATBoardNo": hpnicfNATStatNATBoardNo,
       "hpnicfNATStatActiveTblCount": hpnicfNATStatActiveTblCount,
       "hpnicfNATStatActiveTblCountInNP": hpnicfNATStatActiveTblCountInNP,
       "hpnicfNATStatActiveNatTblCount": hpnicfNATStatActiveNatTblCount,
       "hpnicfNATStatActiveSvrTblCount": hpnicfNATStatActiveSvrTblCount,
       "hpnicfNATStatActivePoolTblCount": hpnicfNATStatActivePoolTblCount,
       "hpnicfNATStatNumOfUsedPort": hpnicfNATStatNumOfUsedPort,
       "hpnicfNATStatNumOfGoodPkt": hpnicfNATStatNumOfGoodPkt,
       "hpnicfNATStatNumOfBadPkt": hpnicfNATStatNumOfBadPkt,
       "hpnicfNATStaticSessionCount": hpnicfNATStaticSessionCount,
       "hpnicfNATFragmentSessionCount": hpnicfNATFragmentSessionCount,
       "hpnicfNATSequenceSessionCount": hpnicfNATSequenceSessionCount,
       "hpnicfNATLogCount": hpnicfNATLogCount,
       "hpnicfNATSessionTable": hpnicfNATSessionTable,
       "hpnicfNATSessionEntry": hpnicfNATSessionEntry,
       "hpnicfNATSessionHashNumber": hpnicfNATSessionHashNumber,
       "hpnicfNATSessionProtocol": hpnicfNATSessionProtocol,
       "hpnicfNATSessionGlobalIP": hpnicfNATSessionGlobalIP,
       "hpnicfNATSessionGlobalPort": hpnicfNATSessionGlobalPort,
       "hpnicfNATSessionInsideIP": hpnicfNATSessionInsideIP,
       "hpnicfNATSessionInsidePort": hpnicfNATSessionInsidePort,
       "hpnicfNATSessionPeerIP": hpnicfNATSessionPeerIP,
       "hpnicfNATSessionPeerPort": hpnicfNATSessionPeerPort,
       "hpnicfNATSessionVpnIndex": hpnicfNATSessionVpnIndex,
       "hpnicfNATSessionTTL": hpnicfNATSessionTTL,
       "hpnicfNATSessionStatus": hpnicfNATSessionStatus,
       "hpnicfNATSessionLeftTime": hpnicfNATSessionLeftTime,
       "hpnicfNATStaticConfTable": hpnicfNATStaticConfTable,
       "hpnicfNATStaticConfEntry": hpnicfNATStaticConfEntry,
       "hpnicfNATStaticInsideIp": hpnicfNATStaticInsideIp,
       "hpnicfNATStaticGlobalIp": hpnicfNATStaticGlobalIp,
       "hpnicfNATStaticRowStatus": hpnicfNATStaticRowStatus,
       "hpnicfNATStaticEnableTable": hpnicfNATStaticEnableTable,
       "hpnicfNATStaticEnableEntry": hpnicfNATStaticEnableEntry,
       "hpnicfNATStaticEnable": hpnicfNATStaticEnable,
       "hpnicfNATDnsMapTable": hpnicfNATDnsMapTable,
       "hpnicfNATDnsMapEntry": hpnicfNATDnsMapEntry,
       "hpnicfNATDnsMapDomainName": hpnicfNATDnsMapDomainName,
       "hpnicfNATDnsMapGlobalIp": hpnicfNATDnsMapGlobalIp,
       "hpnicfNATDnsMapGlobalPort": hpnicfNATDnsMapGlobalPort,
       "hpnicfNATDnsMapProtocolType": hpnicfNATDnsMapProtocolType,
       "hpnicfNATDnsMapLastUseTime": hpnicfNATDnsMapLastUseTime,
       "hpnicfNATDnsMapRowStatus": hpnicfNATDnsMapRowStatus}
)
