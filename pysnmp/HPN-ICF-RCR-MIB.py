# SNMP MIB module (HPN-ICF-RCR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-RCR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:40 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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


# MODULE-IDENTITY

hpnicfRcr = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48)
)
hpnicfRcr.setRevisions(
        ("2005-06-28 19:36",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfRcrMR_ObjectIdentity = ObjectIdentity
hpnicfRcrMR = _HpnicfRcrMR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 1)
)
_HpnicfRcrMRGroup_ObjectIdentity = ObjectIdentity
hpnicfRcrMRGroup = _HpnicfRcrMRGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 1, 1)
)


class _HpnicfRcrMRAllMaxUsedBandRate_Type(Integer32):
    """Custom type hpnicfRcrMRAllMaxUsedBandRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HpnicfRcrMRAllMaxUsedBandRate_Type.__name__ = "Integer32"
_HpnicfRcrMRAllMaxUsedBandRate_Object = MibScalar
hpnicfRcrMRAllMaxUsedBandRate = _HpnicfRcrMRAllMaxUsedBandRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 1, 1, 1),
    _HpnicfRcrMRAllMaxUsedBandRate_Type()
)
hpnicfRcrMRAllMaxUsedBandRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfRcrMRAllMaxUsedBandRate.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfRcrMRAllMaxUsedBandRate.setUnits("%")


class _HpnicfRcrMRAllMinUsedBandRate_Type(Integer32):
    """Custom type hpnicfRcrMRAllMinUsedBandRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfRcrMRAllMinUsedBandRate_Type.__name__ = "Integer32"
_HpnicfRcrMRAllMinUsedBandRate_Object = MibScalar
hpnicfRcrMRAllMinUsedBandRate = _HpnicfRcrMRAllMinUsedBandRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 1, 1, 2),
    _HpnicfRcrMRAllMinUsedBandRate_Type()
)
hpnicfRcrMRAllMinUsedBandRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfRcrMRAllMinUsedBandRate.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfRcrMRAllMinUsedBandRate.setUnits("%")


class _HpnicfRcrMRListenTime_Type(Integer32):
    """Custom type hpnicfRcrMRListenTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_HpnicfRcrMRListenTime_Type.__name__ = "Integer32"
_HpnicfRcrMRListenTime_Object = MibScalar
hpnicfRcrMRListenTime = _HpnicfRcrMRListenTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 1, 1, 3),
    _HpnicfRcrMRListenTime_Type()
)
hpnicfRcrMRListenTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfRcrMRListenTime.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfRcrMRListenTime.setUnits("minute")
_HpnicfRcrMRStateTable_Object = MibTable
hpnicfRcrMRStateTable = _HpnicfRcrMRStateTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfRcrMRStateTable.setStatus("current")
_HpnicfRcrMRStateEntry_Object = MibTableRow
hpnicfRcrMRStateEntry = _HpnicfRcrMRStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 1, 2, 1)
)
hpnicfRcrMRStateEntry.setIndexNames(
    (0, "HPN-ICF-RCR-MIB", "hpnicfRcrMRName"),
)
if mibBuilder.loadTexts:
    hpnicfRcrMRStateEntry.setStatus("current")


class _HpnicfRcrMRName_Type(OctetString):
    """Custom type hpnicfRcrMRName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpnicfRcrMRName_Type.__name__ = "OctetString"
_HpnicfRcrMRName_Object = MibTableColumn
hpnicfRcrMRName = _HpnicfRcrMRName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 1, 2, 1, 1),
    _HpnicfRcrMRName_Type()
)
hpnicfRcrMRName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfRcrMRName.setStatus("current")


class _HpnicfRcrMRState_Type(Integer32):
    """Custom type hpnicfRcrMRState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("controlled", 3),
          ("down", 1),
          ("up", 2))
    )


_HpnicfRcrMRState_Type.__name__ = "Integer32"
_HpnicfRcrMRState_Object = MibTableColumn
hpnicfRcrMRState = _HpnicfRcrMRState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 1, 2, 1, 2),
    _HpnicfRcrMRState_Type()
)
hpnicfRcrMRState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRcrMRState.setStatus("current")


class _HpnicfRcrMRAuthType_Type(Integer32):
    """Custom type hpnicfRcrMRAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("md5", 2),
          ("simple", 1))
    )


_HpnicfRcrMRAuthType_Type.__name__ = "Integer32"
_HpnicfRcrMRAuthType_Object = MibTableColumn
hpnicfRcrMRAuthType = _HpnicfRcrMRAuthType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 1, 2, 1, 3),
    _HpnicfRcrMRAuthType_Type()
)
hpnicfRcrMRAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfRcrMRAuthType.setStatus("current")
_HpnicfRcrMRAuthPwd_Type = OctetString
_HpnicfRcrMRAuthPwd_Object = MibTableColumn
hpnicfRcrMRAuthPwd = _HpnicfRcrMRAuthPwd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 1, 2, 1, 4),
    _HpnicfRcrMRAuthPwd_Type()
)
hpnicfRcrMRAuthPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfRcrMRAuthPwd.setStatus("current")
_HpnicfRcrMROutIfStateTable_Object = MibTable
hpnicfRcrMROutIfStateTable = _HpnicfRcrMROutIfStateTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfRcrMROutIfStateTable.setStatus("current")
_HpnicfRcrMROutIfStateEntry_Object = MibTableRow
hpnicfRcrMROutIfStateEntry = _HpnicfRcrMROutIfStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 1, 3, 1)
)
hpnicfRcrMROutIfStateEntry.setIndexNames(
    (0, "HPN-ICF-RCR-MIB", "hpnicfRcrMRName"),
    (0, "HPN-ICF-RCR-MIB", "hpnicfRcrMROutIfName"),
)
if mibBuilder.loadTexts:
    hpnicfRcrMROutIfStateEntry.setStatus("current")


class _HpnicfRcrMROutIfName_Type(OctetString):
    """Custom type hpnicfRcrMROutIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_HpnicfRcrMROutIfName_Type.__name__ = "OctetString"
_HpnicfRcrMROutIfName_Object = MibTableColumn
hpnicfRcrMROutIfName = _HpnicfRcrMROutIfName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 1, 3, 1, 1),
    _HpnicfRcrMROutIfName_Type()
)
hpnicfRcrMROutIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfRcrMROutIfName.setStatus("current")


class _HpnicfRcrMROutIfState_Type(Integer32):
    """Custom type hpnicfRcrMROutIfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("notExist", 3),
          ("up", 2))
    )


_HpnicfRcrMROutIfState_Type.__name__ = "Integer32"
_HpnicfRcrMROutIfState_Object = MibTableColumn
hpnicfRcrMROutIfState = _HpnicfRcrMROutIfState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 1, 3, 1, 2),
    _HpnicfRcrMROutIfState_Type()
)
hpnicfRcrMROutIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRcrMROutIfState.setStatus("current")


class _HpnicfRcrMROutIfMaxUsedBandRate_Type(Integer32):
    """Custom type hpnicfRcrMROutIfMaxUsedBandRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HpnicfRcrMROutIfMaxUsedBandRate_Type.__name__ = "Integer32"
_HpnicfRcrMROutIfMaxUsedBandRate_Object = MibTableColumn
hpnicfRcrMROutIfMaxUsedBandRate = _HpnicfRcrMROutIfMaxUsedBandRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 1, 3, 1, 3),
    _HpnicfRcrMROutIfMaxUsedBandRate_Type()
)
hpnicfRcrMROutIfMaxUsedBandRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfRcrMROutIfMaxUsedBandRate.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfRcrMROutIfMaxUsedBandRate.setUnits("%")


class _HpnicfRcrMROutIfMinUsedBandRate_Type(Integer32):
    """Custom type hpnicfRcrMROutIfMinUsedBandRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfRcrMROutIfMinUsedBandRate_Type.__name__ = "Integer32"
_HpnicfRcrMROutIfMinUsedBandRate_Object = MibTableColumn
hpnicfRcrMROutIfMinUsedBandRate = _HpnicfRcrMROutIfMinUsedBandRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 1, 3, 1, 4),
    _HpnicfRcrMROutIfMinUsedBandRate_Type()
)
hpnicfRcrMROutIfMinUsedBandRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfRcrMROutIfMinUsedBandRate.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfRcrMROutIfMinUsedBandRate.setUnits("%")


class _HpnicfRcrMROutIfUsedBandRate_Type(Integer32):
    """Custom type hpnicfRcrMROutIfUsedBandRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfRcrMROutIfUsedBandRate_Type.__name__ = "Integer32"
_HpnicfRcrMROutIfUsedBandRate_Object = MibTableColumn
hpnicfRcrMROutIfUsedBandRate = _HpnicfRcrMROutIfUsedBandRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 1, 3, 1, 5),
    _HpnicfRcrMROutIfUsedBandRate_Type()
)
hpnicfRcrMROutIfUsedBandRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRcrMROutIfUsedBandRate.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfRcrMROutIfUsedBandRate.setUnits("%")
_HpnicfRcrCR_ObjectIdentity = ObjectIdentity
hpnicfRcrCR = _HpnicfRcrCR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2)
)
_HpnicfRcrCRGroup_ObjectIdentity = ObjectIdentity
hpnicfRcrCRGroup = _HpnicfRcrCRGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 1)
)


class _HpnicfRcrCRState_Type(Integer32):
    """Custom type hpnicfRcrCRState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("down", 1),
          ("init", 2))
    )


_HpnicfRcrCRState_Type.__name__ = "Integer32"
_HpnicfRcrCRState_Object = MibScalar
hpnicfRcrCRState = _HpnicfRcrCRState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 1, 1),
    _HpnicfRcrCRState_Type()
)
hpnicfRcrCRState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRcrCRState.setStatus("current")
_HpnicfRcrCRPortNum_Type = Integer32
_HpnicfRcrCRPortNum_Object = MibScalar
hpnicfRcrCRPortNum = _HpnicfRcrCRPortNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 1, 2),
    _HpnicfRcrCRPortNum_Type()
)
hpnicfRcrCRPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfRcrCRPortNum.setStatus("current")


class _HpnicfRcrCRCtrlMode_Type(Integer32):
    """Custom type hpnicfRcrCRCtrlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("control", 1),
          ("observe", 2))
    )


_HpnicfRcrCRCtrlMode_Type.__name__ = "Integer32"
_HpnicfRcrCRCtrlMode_Object = MibScalar
hpnicfRcrCRCtrlMode = _HpnicfRcrCRCtrlMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 1, 3),
    _HpnicfRcrCRCtrlMode_Type()
)
hpnicfRcrCRCtrlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfRcrCRCtrlMode.setStatus("current")


class _HpnicfRcrCRChooseMode_Type(Integer32):
    """Custom type hpnicfRcrCRChooseMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("best", 2),
          ("good", 1))
    )


_HpnicfRcrCRChooseMode_Type.__name__ = "Integer32"
_HpnicfRcrCRChooseMode_Object = MibScalar
hpnicfRcrCRChooseMode = _HpnicfRcrCRChooseMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 1, 4),
    _HpnicfRcrCRChooseMode_Type()
)
hpnicfRcrCRChooseMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfRcrCRChooseMode.setStatus("current")


class _HpnicfRcrCRKeepaliveTime_Type(Integer32):
    """Custom type hpnicfRcrCRKeepaliveTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_HpnicfRcrCRKeepaliveTime_Type.__name__ = "Integer32"
_HpnicfRcrCRKeepaliveTime_Object = MibScalar
hpnicfRcrCRKeepaliveTime = _HpnicfRcrCRKeepaliveTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 1, 5),
    _HpnicfRcrCRKeepaliveTime_Type()
)
hpnicfRcrCRKeepaliveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfRcrCRKeepaliveTime.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfRcrCRKeepaliveTime.setUnits("second")


class _HpnicfRcrCRPolicyMode_Type(Integer32):
    """Custom type hpnicfRcrCRPolicyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("operation", 2),
          ("prefix", 1),
          ("study", 3))
    )


_HpnicfRcrCRPolicyMode_Type.__name__ = "Integer32"
_HpnicfRcrCRPolicyMode_Object = MibScalar
hpnicfRcrCRPolicyMode = _HpnicfRcrCRPolicyMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 1, 6),
    _HpnicfRcrCRPolicyMode_Type()
)
hpnicfRcrCRPolicyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfRcrCRPolicyMode.setStatus("current")


class _HpnicfRcrCRStudyMode_Type(Integer32):
    """Custom type hpnicfRcrCRStudyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("maxDelay", 2),
          ("maxThoughout", 1))
    )


_HpnicfRcrCRStudyMode_Type.__name__ = "Integer32"
_HpnicfRcrCRStudyMode_Object = MibScalar
hpnicfRcrCRStudyMode = _HpnicfRcrCRStudyMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 1, 7),
    _HpnicfRcrCRStudyMode_Type()
)
hpnicfRcrCRStudyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfRcrCRStudyMode.setStatus("current")


class _HpnicfRcrCRStudyIpPrefixNum_Type(Integer32):
    """Custom type hpnicfRcrCRStudyIpPrefixNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2500),
    )


_HpnicfRcrCRStudyIpPrefixNum_Type.__name__ = "Integer32"
_HpnicfRcrCRStudyIpPrefixNum_Object = MibScalar
hpnicfRcrCRStudyIpPrefixNum = _HpnicfRcrCRStudyIpPrefixNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 1, 8),
    _HpnicfRcrCRStudyIpPrefixNum_Type()
)
hpnicfRcrCRStudyIpPrefixNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfRcrCRStudyIpPrefixNum.setStatus("current")


class _HpnicfRcrCRIpPrefixLen_Type(Integer32):
    """Custom type hpnicfRcrCRIpPrefixLen based on Integer32"""
    defaultValue = 24

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_HpnicfRcrCRIpPrefixLen_Type.__name__ = "Integer32"
_HpnicfRcrCRIpPrefixLen_Object = MibScalar
hpnicfRcrCRIpPrefixLen = _HpnicfRcrCRIpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 1, 9),
    _HpnicfRcrCRIpPrefixLen_Type()
)
hpnicfRcrCRIpPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfRcrCRIpPrefixLen.setStatus("current")
_HpnicfRcrCRRcrPolicyTable_Object = MibTable
hpnicfRcrCRRcrPolicyTable = _HpnicfRcrCRRcrPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfRcrCRRcrPolicyTable.setStatus("current")
_HpnicfRcrCRRcrPolicyEntry_Object = MibTableRow
hpnicfRcrCRRcrPolicyEntry = _HpnicfRcrCRRcrPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 2, 1)
)
hpnicfRcrCRRcrPolicyEntry.setIndexNames(
    (0, "HPN-ICF-RCR-MIB", "hpnicfRcrCRRcrPlyID"),
)
if mibBuilder.loadTexts:
    hpnicfRcrCRRcrPolicyEntry.setStatus("current")
_HpnicfRcrCRRcrPlyID_Type = Integer32
_HpnicfRcrCRRcrPlyID_Object = MibTableColumn
hpnicfRcrCRRcrPlyID = _HpnicfRcrCRRcrPlyID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 2, 1, 1),
    _HpnicfRcrCRRcrPlyID_Type()
)
hpnicfRcrCRRcrPlyID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfRcrCRRcrPlyID.setStatus("current")


class _HpnicfRcrCRRcrPlyMatchIPListName_Type(OctetString):
    """Custom type hpnicfRcrCRRcrPlyMatchIPListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_HpnicfRcrCRRcrPlyMatchIPListName_Type.__name__ = "OctetString"
_HpnicfRcrCRRcrPlyMatchIPListName_Object = MibTableColumn
hpnicfRcrCRRcrPlyMatchIPListName = _HpnicfRcrCRRcrPlyMatchIPListName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 2, 1, 2),
    _HpnicfRcrCRRcrPlyMatchIPListName_Type()
)
hpnicfRcrCRRcrPlyMatchIPListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfRcrCRRcrPlyMatchIPListName.setStatus("current")


class _HpnicfRcrCRRcrPlyMatchStudyEnable_Type(Integer32):
    """Custom type hpnicfRcrCRRcrPlyMatchStudyEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HpnicfRcrCRRcrPlyMatchStudyEnable_Type.__name__ = "Integer32"
_HpnicfRcrCRRcrPlyMatchStudyEnable_Object = MibTableColumn
hpnicfRcrCRRcrPlyMatchStudyEnable = _HpnicfRcrCRRcrPlyMatchStudyEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 2, 1, 3),
    _HpnicfRcrCRRcrPlyMatchStudyEnable_Type()
)
hpnicfRcrCRRcrPlyMatchStudyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfRcrCRRcrPlyMatchStudyEnable.setStatus("current")


class _HpnicfRcrCRRcrPlyMatchOperPlyName_Type(OctetString):
    """Custom type hpnicfRcrCRRcrPlyMatchOperPlyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_HpnicfRcrCRRcrPlyMatchOperPlyName_Type.__name__ = "OctetString"
_HpnicfRcrCRRcrPlyMatchOperPlyName_Object = MibTableColumn
hpnicfRcrCRRcrPlyMatchOperPlyName = _HpnicfRcrCRRcrPlyMatchOperPlyName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 2, 1, 4),
    _HpnicfRcrCRRcrPlyMatchOperPlyName_Type()
)
hpnicfRcrCRRcrPlyMatchOperPlyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfRcrCRRcrPlyMatchOperPlyName.setStatus("current")


class _HpnicfRcrCRRcrAclNumber_Type(Integer32):
    """Custom type hpnicfRcrCRRcrAclNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3000, 3999),
    )


_HpnicfRcrCRRcrAclNumber_Type.__name__ = "Integer32"
_HpnicfRcrCRRcrAclNumber_Object = MibTableColumn
hpnicfRcrCRRcrAclNumber = _HpnicfRcrCRRcrAclNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 2, 1, 5),
    _HpnicfRcrCRRcrAclNumber_Type()
)
hpnicfRcrCRRcrAclNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfRcrCRRcrAclNumber.setStatus("current")


class _HpnicfRcrCRRcrPlyDelayTime_Type(Integer32):
    """Custom type hpnicfRcrCRRcrPlyDelayTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_HpnicfRcrCRRcrPlyDelayTime_Type.__name__ = "Integer32"
_HpnicfRcrCRRcrPlyDelayTime_Object = MibTableColumn
hpnicfRcrCRRcrPlyDelayTime = _HpnicfRcrCRRcrPlyDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 2, 1, 6),
    _HpnicfRcrCRRcrPlyDelayTime_Type()
)
hpnicfRcrCRRcrPlyDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfRcrCRRcrPlyDelayTime.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfRcrCRRcrPlyDelayTime.setUnits("millisecond")


class _HpnicfRcrCRRcrPlyLossRate_Type(Integer32):
    """Custom type hpnicfRcrCRRcrPlyLossRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HpnicfRcrCRRcrPlyLossRate_Type.__name__ = "Integer32"
_HpnicfRcrCRRcrPlyLossRate_Object = MibTableColumn
hpnicfRcrCRRcrPlyLossRate = _HpnicfRcrCRRcrPlyLossRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 2, 1, 7),
    _HpnicfRcrCRRcrPlyLossRate_Type()
)
hpnicfRcrCRRcrPlyLossRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfRcrCRRcrPlyLossRate.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfRcrCRRcrPlyLossRate.setUnits("%")
_HpnicfRcrCRMatPrefixPerfTable_Object = MibTable
hpnicfRcrCRMatPrefixPerfTable = _HpnicfRcrCRMatPrefixPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 3)
)
if mibBuilder.loadTexts:
    hpnicfRcrCRMatPrefixPerfTable.setStatus("current")
_HpnicfRcrCRMatPrefixPerfEntry_Object = MibTableRow
hpnicfRcrCRMatPrefixPerfEntry = _HpnicfRcrCRMatPrefixPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 3, 1)
)
hpnicfRcrCRMatPrefixPerfEntry.setIndexNames(
    (0, "HPN-ICF-RCR-MIB", "hpnicfRcrCRMatPrefPerfAddrType"),
    (0, "HPN-ICF-RCR-MIB", "hpnicfRcrCRMatPrefPerfDestIPAddr"),
    (0, "HPN-ICF-RCR-MIB", "hpnicfRcrCRMatPrefPerfDestMaskLen"),
)
if mibBuilder.loadTexts:
    hpnicfRcrCRMatPrefixPerfEntry.setStatus("current")
_HpnicfRcrCRMatPrefPerfAddrType_Type = InetAddressType
_HpnicfRcrCRMatPrefPerfAddrType_Object = MibTableColumn
hpnicfRcrCRMatPrefPerfAddrType = _HpnicfRcrCRMatPrefPerfAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 3, 1, 1),
    _HpnicfRcrCRMatPrefPerfAddrType_Type()
)
hpnicfRcrCRMatPrefPerfAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfRcrCRMatPrefPerfAddrType.setStatus("current")
_HpnicfRcrCRMatPrefPerfDestIPAddr_Type = InetAddress
_HpnicfRcrCRMatPrefPerfDestIPAddr_Object = MibTableColumn
hpnicfRcrCRMatPrefPerfDestIPAddr = _HpnicfRcrCRMatPrefPerfDestIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 3, 1, 2),
    _HpnicfRcrCRMatPrefPerfDestIPAddr_Type()
)
hpnicfRcrCRMatPrefPerfDestIPAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfRcrCRMatPrefPerfDestIPAddr.setStatus("current")


class _HpnicfRcrCRMatPrefPerfDestMaskLen_Type(Integer32):
    """Custom type hpnicfRcrCRMatPrefPerfDestMaskLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_HpnicfRcrCRMatPrefPerfDestMaskLen_Type.__name__ = "Integer32"
_HpnicfRcrCRMatPrefPerfDestMaskLen_Object = MibTableColumn
hpnicfRcrCRMatPrefPerfDestMaskLen = _HpnicfRcrCRMatPrefPerfDestMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 3, 1, 3),
    _HpnicfRcrCRMatPrefPerfDestMaskLen_Type()
)
hpnicfRcrCRMatPrefPerfDestMaskLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfRcrCRMatPrefPerfDestMaskLen.setStatus("current")


class _HpnicfRcrCRMatPrefPerfDelayTime_Type(Integer32):
    """Custom type hpnicfRcrCRMatPrefPerfDelayTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_HpnicfRcrCRMatPrefPerfDelayTime_Type.__name__ = "Integer32"
_HpnicfRcrCRMatPrefPerfDelayTime_Object = MibTableColumn
hpnicfRcrCRMatPrefPerfDelayTime = _HpnicfRcrCRMatPrefPerfDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 3, 1, 4),
    _HpnicfRcrCRMatPrefPerfDelayTime_Type()
)
hpnicfRcrCRMatPrefPerfDelayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRcrCRMatPrefPerfDelayTime.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfRcrCRMatPrefPerfDelayTime.setUnits("second")


class _HpnicfRcrCRMatPrefPerfLossRate_Type(Integer32):
    """Custom type hpnicfRcrCRMatPrefPerfLossRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HpnicfRcrCRMatPrefPerfLossRate_Type.__name__ = "Integer32"
_HpnicfRcrCRMatPrefPerfLossRate_Object = MibTableColumn
hpnicfRcrCRMatPrefPerfLossRate = _HpnicfRcrCRMatPrefPerfLossRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 3, 1, 5),
    _HpnicfRcrCRMatPrefPerfLossRate_Type()
)
hpnicfRcrCRMatPrefPerfLossRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRcrCRMatPrefPerfLossRate.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfRcrCRMatPrefPerfLossRate.setUnits("%")
_HpnicfRcrCRMatPrefPerfThroughput_Type = Integer32
_HpnicfRcrCRMatPrefPerfThroughput_Object = MibTableColumn
hpnicfRcrCRMatPrefPerfThroughput = _HpnicfRcrCRMatPrefPerfThroughput_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 3, 1, 6),
    _HpnicfRcrCRMatPrefPerfThroughput_Type()
)
hpnicfRcrCRMatPrefPerfThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRcrCRMatPrefPerfThroughput.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfRcrCRMatPrefPerfThroughput.setUnits("kb")
_HpnicfRcrCRAdjustPrefixTable_Object = MibTable
hpnicfRcrCRAdjustPrefixTable = _HpnicfRcrCRAdjustPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 4)
)
if mibBuilder.loadTexts:
    hpnicfRcrCRAdjustPrefixTable.setStatus("current")
_HpnicfRcrCRAdjustPrefixEntry_Object = MibTableRow
hpnicfRcrCRAdjustPrefixEntry = _HpnicfRcrCRAdjustPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 4, 1)
)
hpnicfRcrCRAdjustPrefixEntry.setIndexNames(
    (0, "HPN-ICF-RCR-MIB", "hpnicfRcrCRAdjuPrefDestAddrType"),
    (0, "HPN-ICF-RCR-MIB", "hpnicfRcrCRAdjuPrefDestAddr"),
    (0, "HPN-ICF-RCR-MIB", "hpnicfRcrCRAdjuPrefMaskLen"),
    (0, "HPN-ICF-RCR-MIB", "hpnicfRcrCRAdjuPrefPreMRName"),
    (0, "HPN-ICF-RCR-MIB", "hpnicfRcrCRAdjuPrefPreOutIfName"),
)
if mibBuilder.loadTexts:
    hpnicfRcrCRAdjustPrefixEntry.setStatus("current")
_HpnicfRcrCRAdjuPrefDestAddrType_Type = InetAddressType
_HpnicfRcrCRAdjuPrefDestAddrType_Object = MibTableColumn
hpnicfRcrCRAdjuPrefDestAddrType = _HpnicfRcrCRAdjuPrefDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 4, 1, 1),
    _HpnicfRcrCRAdjuPrefDestAddrType_Type()
)
hpnicfRcrCRAdjuPrefDestAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfRcrCRAdjuPrefDestAddrType.setStatus("current")
_HpnicfRcrCRAdjuPrefDestAddr_Type = InetAddress
_HpnicfRcrCRAdjuPrefDestAddr_Object = MibTableColumn
hpnicfRcrCRAdjuPrefDestAddr = _HpnicfRcrCRAdjuPrefDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 4, 1, 2),
    _HpnicfRcrCRAdjuPrefDestAddr_Type()
)
hpnicfRcrCRAdjuPrefDestAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfRcrCRAdjuPrefDestAddr.setStatus("current")


class _HpnicfRcrCRAdjuPrefMaskLen_Type(Integer32):
    """Custom type hpnicfRcrCRAdjuPrefMaskLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_HpnicfRcrCRAdjuPrefMaskLen_Type.__name__ = "Integer32"
_HpnicfRcrCRAdjuPrefMaskLen_Object = MibTableColumn
hpnicfRcrCRAdjuPrefMaskLen = _HpnicfRcrCRAdjuPrefMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 4, 1, 3),
    _HpnicfRcrCRAdjuPrefMaskLen_Type()
)
hpnicfRcrCRAdjuPrefMaskLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfRcrCRAdjuPrefMaskLen.setStatus("current")


class _HpnicfRcrCRAdjuPrefPreMRName_Type(OctetString):
    """Custom type hpnicfRcrCRAdjuPrefPreMRName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpnicfRcrCRAdjuPrefPreMRName_Type.__name__ = "OctetString"
_HpnicfRcrCRAdjuPrefPreMRName_Object = MibTableColumn
hpnicfRcrCRAdjuPrefPreMRName = _HpnicfRcrCRAdjuPrefPreMRName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 4, 1, 4),
    _HpnicfRcrCRAdjuPrefPreMRName_Type()
)
hpnicfRcrCRAdjuPrefPreMRName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfRcrCRAdjuPrefPreMRName.setStatus("current")


class _HpnicfRcrCRAdjuPrefPreOutIfName_Type(OctetString):
    """Custom type hpnicfRcrCRAdjuPrefPreOutIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_HpnicfRcrCRAdjuPrefPreOutIfName_Type.__name__ = "OctetString"
_HpnicfRcrCRAdjuPrefPreOutIfName_Object = MibTableColumn
hpnicfRcrCRAdjuPrefPreOutIfName = _HpnicfRcrCRAdjuPrefPreOutIfName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 4, 1, 5),
    _HpnicfRcrCRAdjuPrefPreOutIfName_Type()
)
hpnicfRcrCRAdjuPrefPreOutIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfRcrCRAdjuPrefPreOutIfName.setStatus("current")


class _HpnicfRcrCRAdjuPrefCurMRName_Type(OctetString):
    """Custom type hpnicfRcrCRAdjuPrefCurMRName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpnicfRcrCRAdjuPrefCurMRName_Type.__name__ = "OctetString"
_HpnicfRcrCRAdjuPrefCurMRName_Object = MibTableColumn
hpnicfRcrCRAdjuPrefCurMRName = _HpnicfRcrCRAdjuPrefCurMRName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 4, 1, 6),
    _HpnicfRcrCRAdjuPrefCurMRName_Type()
)
hpnicfRcrCRAdjuPrefCurMRName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRcrCRAdjuPrefCurMRName.setStatus("current")
_HpnicfRcrCRAdjuPrefCurOutIfName_Type = OctetString
_HpnicfRcrCRAdjuPrefCurOutIfName_Object = MibTableColumn
hpnicfRcrCRAdjuPrefCurOutIfName = _HpnicfRcrCRAdjuPrefCurOutIfName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 4, 1, 7),
    _HpnicfRcrCRAdjuPrefCurOutIfName_Type()
)
hpnicfRcrCRAdjuPrefCurOutIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRcrCRAdjuPrefCurOutIfName.setStatus("current")
_HpnicfRcrCRAdjuPrefPersistTime_Type = Integer32
_HpnicfRcrCRAdjuPrefPersistTime_Object = MibTableColumn
hpnicfRcrCRAdjuPrefPersistTime = _HpnicfRcrCRAdjuPrefPersistTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 4, 1, 8),
    _HpnicfRcrCRAdjuPrefPersistTime_Type()
)
hpnicfRcrCRAdjuPrefPersistTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRcrCRAdjuPrefPersistTime.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfRcrCRAdjuPrefPersistTime.setUnits("second")
_HpnicfRcrCRAdjuPrefAgeTime_Type = Integer32
_HpnicfRcrCRAdjuPrefAgeTime_Object = MibTableColumn
hpnicfRcrCRAdjuPrefAgeTime = _HpnicfRcrCRAdjuPrefAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48, 2, 4, 1, 9),
    _HpnicfRcrCRAdjuPrefAgeTime_Type()
)
hpnicfRcrCRAdjuPrefAgeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRcrCRAdjuPrefAgeTime.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfRcrCRAdjuPrefAgeTime.setUnits("second")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-RCR-MIB",
    **{"hpnicfRcr": hpnicfRcr,
       "hpnicfRcrMR": hpnicfRcrMR,
       "hpnicfRcrMRGroup": hpnicfRcrMRGroup,
       "hpnicfRcrMRAllMaxUsedBandRate": hpnicfRcrMRAllMaxUsedBandRate,
       "hpnicfRcrMRAllMinUsedBandRate": hpnicfRcrMRAllMinUsedBandRate,
       "hpnicfRcrMRListenTime": hpnicfRcrMRListenTime,
       "hpnicfRcrMRStateTable": hpnicfRcrMRStateTable,
       "hpnicfRcrMRStateEntry": hpnicfRcrMRStateEntry,
       "hpnicfRcrMRName": hpnicfRcrMRName,
       "hpnicfRcrMRState": hpnicfRcrMRState,
       "hpnicfRcrMRAuthType": hpnicfRcrMRAuthType,
       "hpnicfRcrMRAuthPwd": hpnicfRcrMRAuthPwd,
       "hpnicfRcrMROutIfStateTable": hpnicfRcrMROutIfStateTable,
       "hpnicfRcrMROutIfStateEntry": hpnicfRcrMROutIfStateEntry,
       "hpnicfRcrMROutIfName": hpnicfRcrMROutIfName,
       "hpnicfRcrMROutIfState": hpnicfRcrMROutIfState,
       "hpnicfRcrMROutIfMaxUsedBandRate": hpnicfRcrMROutIfMaxUsedBandRate,
       "hpnicfRcrMROutIfMinUsedBandRate": hpnicfRcrMROutIfMinUsedBandRate,
       "hpnicfRcrMROutIfUsedBandRate": hpnicfRcrMROutIfUsedBandRate,
       "hpnicfRcrCR": hpnicfRcrCR,
       "hpnicfRcrCRGroup": hpnicfRcrCRGroup,
       "hpnicfRcrCRState": hpnicfRcrCRState,
       "hpnicfRcrCRPortNum": hpnicfRcrCRPortNum,
       "hpnicfRcrCRCtrlMode": hpnicfRcrCRCtrlMode,
       "hpnicfRcrCRChooseMode": hpnicfRcrCRChooseMode,
       "hpnicfRcrCRKeepaliveTime": hpnicfRcrCRKeepaliveTime,
       "hpnicfRcrCRPolicyMode": hpnicfRcrCRPolicyMode,
       "hpnicfRcrCRStudyMode": hpnicfRcrCRStudyMode,
       "hpnicfRcrCRStudyIpPrefixNum": hpnicfRcrCRStudyIpPrefixNum,
       "hpnicfRcrCRIpPrefixLen": hpnicfRcrCRIpPrefixLen,
       "hpnicfRcrCRRcrPolicyTable": hpnicfRcrCRRcrPolicyTable,
       "hpnicfRcrCRRcrPolicyEntry": hpnicfRcrCRRcrPolicyEntry,
       "hpnicfRcrCRRcrPlyID": hpnicfRcrCRRcrPlyID,
       "hpnicfRcrCRRcrPlyMatchIPListName": hpnicfRcrCRRcrPlyMatchIPListName,
       "hpnicfRcrCRRcrPlyMatchStudyEnable": hpnicfRcrCRRcrPlyMatchStudyEnable,
       "hpnicfRcrCRRcrPlyMatchOperPlyName": hpnicfRcrCRRcrPlyMatchOperPlyName,
       "hpnicfRcrCRRcrAclNumber": hpnicfRcrCRRcrAclNumber,
       "hpnicfRcrCRRcrPlyDelayTime": hpnicfRcrCRRcrPlyDelayTime,
       "hpnicfRcrCRRcrPlyLossRate": hpnicfRcrCRRcrPlyLossRate,
       "hpnicfRcrCRMatPrefixPerfTable": hpnicfRcrCRMatPrefixPerfTable,
       "hpnicfRcrCRMatPrefixPerfEntry": hpnicfRcrCRMatPrefixPerfEntry,
       "hpnicfRcrCRMatPrefPerfAddrType": hpnicfRcrCRMatPrefPerfAddrType,
       "hpnicfRcrCRMatPrefPerfDestIPAddr": hpnicfRcrCRMatPrefPerfDestIPAddr,
       "hpnicfRcrCRMatPrefPerfDestMaskLen": hpnicfRcrCRMatPrefPerfDestMaskLen,
       "hpnicfRcrCRMatPrefPerfDelayTime": hpnicfRcrCRMatPrefPerfDelayTime,
       "hpnicfRcrCRMatPrefPerfLossRate": hpnicfRcrCRMatPrefPerfLossRate,
       "hpnicfRcrCRMatPrefPerfThroughput": hpnicfRcrCRMatPrefPerfThroughput,
       "hpnicfRcrCRAdjustPrefixTable": hpnicfRcrCRAdjustPrefixTable,
       "hpnicfRcrCRAdjustPrefixEntry": hpnicfRcrCRAdjustPrefixEntry,
       "hpnicfRcrCRAdjuPrefDestAddrType": hpnicfRcrCRAdjuPrefDestAddrType,
       "hpnicfRcrCRAdjuPrefDestAddr": hpnicfRcrCRAdjuPrefDestAddr,
       "hpnicfRcrCRAdjuPrefMaskLen": hpnicfRcrCRAdjuPrefMaskLen,
       "hpnicfRcrCRAdjuPrefPreMRName": hpnicfRcrCRAdjuPrefPreMRName,
       "hpnicfRcrCRAdjuPrefPreOutIfName": hpnicfRcrCRAdjuPrefPreOutIfName,
       "hpnicfRcrCRAdjuPrefCurMRName": hpnicfRcrCRAdjuPrefCurMRName,
       "hpnicfRcrCRAdjuPrefCurOutIfName": hpnicfRcrCRAdjuPrefCurOutIfName,
       "hpnicfRcrCRAdjuPrefPersistTime": hpnicfRcrCRAdjuPrefPersistTime,
       "hpnicfRcrCRAdjuPrefAgeTime": hpnicfRcrCRAdjuPrefAgeTime}
)
