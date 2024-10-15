# SNMP MIB module (A3COM-HUAWEI-RCR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-RCR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:28:59 2024
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
    "A3COM-HUAWEI-OID-MIB",
    "h3cCommon")

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

h3cRcr = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48)
)
h3cRcr.setRevisions(
        ("2005-06-28 19:36",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cRcrMR_ObjectIdentity = ObjectIdentity
h3cRcrMR = _H3cRcrMR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 1)
)
_H3cRcrMRGroup_ObjectIdentity = ObjectIdentity
h3cRcrMRGroup = _H3cRcrMRGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 1, 1)
)


class _H3cRcrMRAllMaxUsedBandRate_Type(Integer32):
    """Custom type h3cRcrMRAllMaxUsedBandRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_H3cRcrMRAllMaxUsedBandRate_Type.__name__ = "Integer32"
_H3cRcrMRAllMaxUsedBandRate_Object = MibScalar
h3cRcrMRAllMaxUsedBandRate = _H3cRcrMRAllMaxUsedBandRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 1, 1, 1),
    _H3cRcrMRAllMaxUsedBandRate_Type()
)
h3cRcrMRAllMaxUsedBandRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cRcrMRAllMaxUsedBandRate.setStatus("current")
if mibBuilder.loadTexts:
    h3cRcrMRAllMaxUsedBandRate.setUnits("%")


class _H3cRcrMRAllMinUsedBandRate_Type(Integer32):
    """Custom type h3cRcrMRAllMinUsedBandRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cRcrMRAllMinUsedBandRate_Type.__name__ = "Integer32"
_H3cRcrMRAllMinUsedBandRate_Object = MibScalar
h3cRcrMRAllMinUsedBandRate = _H3cRcrMRAllMinUsedBandRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 1, 1, 2),
    _H3cRcrMRAllMinUsedBandRate_Type()
)
h3cRcrMRAllMinUsedBandRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cRcrMRAllMinUsedBandRate.setStatus("current")
if mibBuilder.loadTexts:
    h3cRcrMRAllMinUsedBandRate.setUnits("%")


class _H3cRcrMRListenTime_Type(Integer32):
    """Custom type h3cRcrMRListenTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_H3cRcrMRListenTime_Type.__name__ = "Integer32"
_H3cRcrMRListenTime_Object = MibScalar
h3cRcrMRListenTime = _H3cRcrMRListenTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 1, 1, 3),
    _H3cRcrMRListenTime_Type()
)
h3cRcrMRListenTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cRcrMRListenTime.setStatus("current")
if mibBuilder.loadTexts:
    h3cRcrMRListenTime.setUnits("minute")
_H3cRcrMRStateTable_Object = MibTable
h3cRcrMRStateTable = _H3cRcrMRStateTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 1, 2)
)
if mibBuilder.loadTexts:
    h3cRcrMRStateTable.setStatus("current")
_H3cRcrMRStateEntry_Object = MibTableRow
h3cRcrMRStateEntry = _H3cRcrMRStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 1, 2, 1)
)
h3cRcrMRStateEntry.setIndexNames(
    (0, "A3COM-HUAWEI-RCR-MIB", "h3cRcrMRName"),
)
if mibBuilder.loadTexts:
    h3cRcrMRStateEntry.setStatus("current")


class _H3cRcrMRName_Type(OctetString):
    """Custom type h3cRcrMRName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_H3cRcrMRName_Type.__name__ = "OctetString"
_H3cRcrMRName_Object = MibTableColumn
h3cRcrMRName = _H3cRcrMRName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 1, 2, 1, 1),
    _H3cRcrMRName_Type()
)
h3cRcrMRName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRcrMRName.setStatus("current")


class _H3cRcrMRState_Type(Integer32):
    """Custom type h3cRcrMRState based on Integer32"""
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


_H3cRcrMRState_Type.__name__ = "Integer32"
_H3cRcrMRState_Object = MibTableColumn
h3cRcrMRState = _H3cRcrMRState_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 1, 2, 1, 2),
    _H3cRcrMRState_Type()
)
h3cRcrMRState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRcrMRState.setStatus("current")


class _H3cRcrMRAuthType_Type(Integer32):
    """Custom type h3cRcrMRAuthType based on Integer32"""
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


_H3cRcrMRAuthType_Type.__name__ = "Integer32"
_H3cRcrMRAuthType_Object = MibTableColumn
h3cRcrMRAuthType = _H3cRcrMRAuthType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 1, 2, 1, 3),
    _H3cRcrMRAuthType_Type()
)
h3cRcrMRAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cRcrMRAuthType.setStatus("current")
_H3cRcrMRAuthPwd_Type = OctetString
_H3cRcrMRAuthPwd_Object = MibTableColumn
h3cRcrMRAuthPwd = _H3cRcrMRAuthPwd_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 1, 2, 1, 4),
    _H3cRcrMRAuthPwd_Type()
)
h3cRcrMRAuthPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cRcrMRAuthPwd.setStatus("current")
_H3cRcrMROutIfStateTable_Object = MibTable
h3cRcrMROutIfStateTable = _H3cRcrMROutIfStateTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 1, 3)
)
if mibBuilder.loadTexts:
    h3cRcrMROutIfStateTable.setStatus("current")
_H3cRcrMROutIfStateEntry_Object = MibTableRow
h3cRcrMROutIfStateEntry = _H3cRcrMROutIfStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 1, 3, 1)
)
h3cRcrMROutIfStateEntry.setIndexNames(
    (0, "A3COM-HUAWEI-RCR-MIB", "h3cRcrMRName"),
    (0, "A3COM-HUAWEI-RCR-MIB", "h3cRcrMROutIfName"),
)
if mibBuilder.loadTexts:
    h3cRcrMROutIfStateEntry.setStatus("current")


class _H3cRcrMROutIfName_Type(OctetString):
    """Custom type h3cRcrMROutIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_H3cRcrMROutIfName_Type.__name__ = "OctetString"
_H3cRcrMROutIfName_Object = MibTableColumn
h3cRcrMROutIfName = _H3cRcrMROutIfName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 1, 3, 1, 1),
    _H3cRcrMROutIfName_Type()
)
h3cRcrMROutIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRcrMROutIfName.setStatus("current")


class _H3cRcrMROutIfState_Type(Integer32):
    """Custom type h3cRcrMROutIfState based on Integer32"""
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


_H3cRcrMROutIfState_Type.__name__ = "Integer32"
_H3cRcrMROutIfState_Object = MibTableColumn
h3cRcrMROutIfState = _H3cRcrMROutIfState_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 1, 3, 1, 2),
    _H3cRcrMROutIfState_Type()
)
h3cRcrMROutIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRcrMROutIfState.setStatus("current")


class _H3cRcrMROutIfMaxUsedBandRate_Type(Integer32):
    """Custom type h3cRcrMROutIfMaxUsedBandRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_H3cRcrMROutIfMaxUsedBandRate_Type.__name__ = "Integer32"
_H3cRcrMROutIfMaxUsedBandRate_Object = MibTableColumn
h3cRcrMROutIfMaxUsedBandRate = _H3cRcrMROutIfMaxUsedBandRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 1, 3, 1, 3),
    _H3cRcrMROutIfMaxUsedBandRate_Type()
)
h3cRcrMROutIfMaxUsedBandRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cRcrMROutIfMaxUsedBandRate.setStatus("current")
if mibBuilder.loadTexts:
    h3cRcrMROutIfMaxUsedBandRate.setUnits("%")


class _H3cRcrMROutIfMinUsedBandRate_Type(Integer32):
    """Custom type h3cRcrMROutIfMinUsedBandRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cRcrMROutIfMinUsedBandRate_Type.__name__ = "Integer32"
_H3cRcrMROutIfMinUsedBandRate_Object = MibTableColumn
h3cRcrMROutIfMinUsedBandRate = _H3cRcrMROutIfMinUsedBandRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 1, 3, 1, 4),
    _H3cRcrMROutIfMinUsedBandRate_Type()
)
h3cRcrMROutIfMinUsedBandRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cRcrMROutIfMinUsedBandRate.setStatus("current")
if mibBuilder.loadTexts:
    h3cRcrMROutIfMinUsedBandRate.setUnits("%")


class _H3cRcrMROutIfUsedBandRate_Type(Integer32):
    """Custom type h3cRcrMROutIfUsedBandRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cRcrMROutIfUsedBandRate_Type.__name__ = "Integer32"
_H3cRcrMROutIfUsedBandRate_Object = MibTableColumn
h3cRcrMROutIfUsedBandRate = _H3cRcrMROutIfUsedBandRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 1, 3, 1, 5),
    _H3cRcrMROutIfUsedBandRate_Type()
)
h3cRcrMROutIfUsedBandRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRcrMROutIfUsedBandRate.setStatus("current")
if mibBuilder.loadTexts:
    h3cRcrMROutIfUsedBandRate.setUnits("%")
_H3cRcrCR_ObjectIdentity = ObjectIdentity
h3cRcrCR = _H3cRcrCR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 2)
)
_H3cRcrCRGroup_ObjectIdentity = ObjectIdentity
h3cRcrCRGroup = _H3cRcrCRGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 2, 1)
)


class _H3cRcrCRState_Type(Integer32):
    """Custom type h3cRcrCRState based on Integer32"""
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


_H3cRcrCRState_Type.__name__ = "Integer32"
_H3cRcrCRState_Object = MibScalar
h3cRcrCRState = _H3cRcrCRState_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 2, 1, 1),
    _H3cRcrCRState_Type()
)
h3cRcrCRState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRcrCRState.setStatus("current")
_H3cRcrCRPortNum_Type = Integer32
_H3cRcrCRPortNum_Object = MibScalar
h3cRcrCRPortNum = _H3cRcrCRPortNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 2, 1, 2),
    _H3cRcrCRPortNum_Type()
)
h3cRcrCRPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cRcrCRPortNum.setStatus("current")


class _H3cRcrCRCtrlMode_Type(Integer32):
    """Custom type h3cRcrCRCtrlMode based on Integer32"""
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


_H3cRcrCRCtrlMode_Type.__name__ = "Integer32"
_H3cRcrCRCtrlMode_Object = MibScalar
h3cRcrCRCtrlMode = _H3cRcrCRCtrlMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 2, 1, 3),
    _H3cRcrCRCtrlMode_Type()
)
h3cRcrCRCtrlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cRcrCRCtrlMode.setStatus("current")


class _H3cRcrCRChooseMode_Type(Integer32):
    """Custom type h3cRcrCRChooseMode based on Integer32"""
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


_H3cRcrCRChooseMode_Type.__name__ = "Integer32"
_H3cRcrCRChooseMode_Object = MibScalar
h3cRcrCRChooseMode = _H3cRcrCRChooseMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 2, 1, 4),
    _H3cRcrCRChooseMode_Type()
)
h3cRcrCRChooseMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cRcrCRChooseMode.setStatus("current")


class _H3cRcrCRKeepaliveTime_Type(Integer32):
    """Custom type h3cRcrCRKeepaliveTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_H3cRcrCRKeepaliveTime_Type.__name__ = "Integer32"
_H3cRcrCRKeepaliveTime_Object = MibScalar
h3cRcrCRKeepaliveTime = _H3cRcrCRKeepaliveTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 2, 1, 5),
    _H3cRcrCRKeepaliveTime_Type()
)
h3cRcrCRKeepaliveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cRcrCRKeepaliveTime.setStatus("current")
if mibBuilder.loadTexts:
    h3cRcrCRKeepaliveTime.setUnits("second")


class _H3cRcrCRPolicyMode_Type(Integer32):
    """Custom type h3cRcrCRPolicyMode based on Integer32"""
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


_H3cRcrCRPolicyMode_Type.__name__ = "Integer32"
_H3cRcrCRPolicyMode_Object = MibScalar
h3cRcrCRPolicyMode = _H3cRcrCRPolicyMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 2, 1, 6),
    _H3cRcrCRPolicyMode_Type()
)
h3cRcrCRPolicyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cRcrCRPolicyMode.setStatus("current")


class _H3cRcrCRStudyMode_Type(Integer32):
    """Custom type h3cRcrCRStudyMode based on Integer32"""
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


_H3cRcrCRStudyMode_Type.__name__ = "Integer32"
_H3cRcrCRStudyMode_Object = MibScalar
h3cRcrCRStudyMode = _H3cRcrCRStudyMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 2, 1, 7),
    _H3cRcrCRStudyMode_Type()
)
h3cRcrCRStudyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cRcrCRStudyMode.setStatus("current")


class _H3cRcrCRStudyIpPrefixNum_Type(Integer32):
    """Custom type h3cRcrCRStudyIpPrefixNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2500),
    )


_H3cRcrCRStudyIpPrefixNum_Type.__name__ = "Integer32"
_H3cRcrCRStudyIpPrefixNum_Object = MibScalar
h3cRcrCRStudyIpPrefixNum = _H3cRcrCRStudyIpPrefixNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 2, 1, 8),
    _H3cRcrCRStudyIpPrefixNum_Type()
)
h3cRcrCRStudyIpPrefixNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cRcrCRStudyIpPrefixNum.setStatus("current")


class _H3cRcrCRIpPrefixLen_Type(Integer32):
    """Custom type h3cRcrCRIpPrefixLen based on Integer32"""
    defaultValue = 24

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_H3cRcrCRIpPrefixLen_Type.__name__ = "Integer32"
_H3cRcrCRIpPrefixLen_Object = MibScalar
h3cRcrCRIpPrefixLen = _H3cRcrCRIpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 2, 1, 9),
    _H3cRcrCRIpPrefixLen_Type()
)
h3cRcrCRIpPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cRcrCRIpPrefixLen.setStatus("current")
_H3cRcrCRRcrPolicyTable_Object = MibTable
h3cRcrCRRcrPolicyTable = _H3cRcrCRRcrPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 2, 2)
)
if mibBuilder.loadTexts:
    h3cRcrCRRcrPolicyTable.setStatus("current")
_H3cRcrCRRcrPolicyEntry_Object = MibTableRow
h3cRcrCRRcrPolicyEntry = _H3cRcrCRRcrPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 2, 2, 1)
)
h3cRcrCRRcrPolicyEntry.setIndexNames(
    (0, "A3COM-HUAWEI-RCR-MIB", "h3cRcrCRRcrPlyID"),
)
if mibBuilder.loadTexts:
    h3cRcrCRRcrPolicyEntry.setStatus("current")
_H3cRcrCRRcrPlyID_Type = Integer32
_H3cRcrCRRcrPlyID_Object = MibTableColumn
h3cRcrCRRcrPlyID = _H3cRcrCRRcrPlyID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 2, 2, 1, 1),
    _H3cRcrCRRcrPlyID_Type()
)
h3cRcrCRRcrPlyID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRcrCRRcrPlyID.setStatus("current")


class _H3cRcrCRRcrPlyMatchIPListName_Type(OctetString):
    """Custom type h3cRcrCRRcrPlyMatchIPListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_H3cRcrCRRcrPlyMatchIPListName_Type.__name__ = "OctetString"
_H3cRcrCRRcrPlyMatchIPListName_Object = MibTableColumn
h3cRcrCRRcrPlyMatchIPListName = _H3cRcrCRRcrPlyMatchIPListName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 2, 2, 1, 2),
    _H3cRcrCRRcrPlyMatchIPListName_Type()
)
h3cRcrCRRcrPlyMatchIPListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cRcrCRRcrPlyMatchIPListName.setStatus("current")


class _H3cRcrCRRcrPlyMatchStudyEnable_Type(Integer32):
    """Custom type h3cRcrCRRcrPlyMatchStudyEnable based on Integer32"""
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


_H3cRcrCRRcrPlyMatchStudyEnable_Type.__name__ = "Integer32"
_H3cRcrCRRcrPlyMatchStudyEnable_Object = MibTableColumn
h3cRcrCRRcrPlyMatchStudyEnable = _H3cRcrCRRcrPlyMatchStudyEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 2, 2, 1, 3),
    _H3cRcrCRRcrPlyMatchStudyEnable_Type()
)
h3cRcrCRRcrPlyMatchStudyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cRcrCRRcrPlyMatchStudyEnable.setStatus("current")


class _H3cRcrCRRcrPlyMatchOperPlyName_Type(OctetString):
    """Custom type h3cRcrCRRcrPlyMatchOperPlyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_H3cRcrCRRcrPlyMatchOperPlyName_Type.__name__ = "OctetString"
_H3cRcrCRRcrPlyMatchOperPlyName_Object = MibTableColumn
h3cRcrCRRcrPlyMatchOperPlyName = _H3cRcrCRRcrPlyMatchOperPlyName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 2, 2, 1, 4),
    _H3cRcrCRRcrPlyMatchOperPlyName_Type()
)
h3cRcrCRRcrPlyMatchOperPlyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cRcrCRRcrPlyMatchOperPlyName.setStatus("current")


class _H3cRcrCRRcrAclNumber_Type(Integer32):
    """Custom type h3cRcrCRRcrAclNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3000, 3999),
    )


_H3cRcrCRRcrAclNumber_Type.__name__ = "Integer32"
_H3cRcrCRRcrAclNumber_Object = MibTableColumn
h3cRcrCRRcrAclNumber = _H3cRcrCRRcrAclNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 2, 2, 1, 5),
    _H3cRcrCRRcrAclNumber_Type()
)
h3cRcrCRRcrAclNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cRcrCRRcrAclNumber.setStatus("current")


class _H3cRcrCRRcrPlyDelayTime_Type(Integer32):
    """Custom type h3cRcrCRRcrPlyDelayTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_H3cRcrCRRcrPlyDelayTime_Type.__name__ = "Integer32"
_H3cRcrCRRcrPlyDelayTime_Object = MibTableColumn
h3cRcrCRRcrPlyDelayTime = _H3cRcrCRRcrPlyDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 2, 2, 1, 6),
    _H3cRcrCRRcrPlyDelayTime_Type()
)
h3cRcrCRRcrPlyDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cRcrCRRcrPlyDelayTime.setStatus("current")
if mibBuilder.loadTexts:
    h3cRcrCRRcrPlyDelayTime.setUnits("millisecond")


class _H3cRcrCRRcrPlyLossRate_Type(Integer32):
    """Custom type h3cRcrCRRcrPlyLossRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_H3cRcrCRRcrPlyLossRate_Type.__name__ = "Integer32"
_H3cRcrCRRcrPlyLossRate_Object = MibTableColumn
h3cRcrCRRcrPlyLossRate = _H3cRcrCRRcrPlyLossRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 2, 2, 1, 7),
    _H3cRcrCRRcrPlyLossRate_Type()
)
h3cRcrCRRcrPlyLossRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cRcrCRRcrPlyLossRate.setStatus("current")
if mibBuilder.loadTexts:
    h3cRcrCRRcrPlyLossRate.setUnits("%")
_H3cRcrCRMatPrefixPerfTable_Object = MibTable
h3cRcrCRMatPrefixPerfTable = _H3cRcrCRMatPrefixPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 2, 3)
)
if mibBuilder.loadTexts:
    h3cRcrCRMatPrefixPerfTable.setStatus("current")
_H3cRcrCRMatPrefixPerfEntry_Object = MibTableRow
h3cRcrCRMatPrefixPerfEntry = _H3cRcrCRMatPrefixPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 2, 3, 1)
)
h3cRcrCRMatPrefixPerfEntry.setIndexNames(
    (0, "A3COM-HUAWEI-RCR-MIB", "h3cRcrCRMatPrefPerfAddrType"),
    (0, "A3COM-HUAWEI-RCR-MIB", "h3cRcrCRMatPrefPerfDestIPAddr"),
    (0, "A3COM-HUAWEI-RCR-MIB", "h3cRcrCRMatPrefPerfDestMaskLen"),
)
if mibBuilder.loadTexts:
    h3cRcrCRMatPrefixPerfEntry.setStatus("current")
_H3cRcrCRMatPrefPerfAddrType_Type = InetAddressType
_H3cRcrCRMatPrefPerfAddrType_Object = MibTableColumn
h3cRcrCRMatPrefPerfAddrType = _H3cRcrCRMatPrefPerfAddrType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 2, 3, 1, 1),
    _H3cRcrCRMatPrefPerfAddrType_Type()
)
h3cRcrCRMatPrefPerfAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRcrCRMatPrefPerfAddrType.setStatus("current")
_H3cRcrCRMatPrefPerfDestIPAddr_Type = InetAddress
_H3cRcrCRMatPrefPerfDestIPAddr_Object = MibTableColumn
h3cRcrCRMatPrefPerfDestIPAddr = _H3cRcrCRMatPrefPerfDestIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 2, 3, 1, 2),
    _H3cRcrCRMatPrefPerfDestIPAddr_Type()
)
h3cRcrCRMatPrefPerfDestIPAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRcrCRMatPrefPerfDestIPAddr.setStatus("current")


class _H3cRcrCRMatPrefPerfDestMaskLen_Type(Integer32):
    """Custom type h3cRcrCRMatPrefPerfDestMaskLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_H3cRcrCRMatPrefPerfDestMaskLen_Type.__name__ = "Integer32"
_H3cRcrCRMatPrefPerfDestMaskLen_Object = MibTableColumn
h3cRcrCRMatPrefPerfDestMaskLen = _H3cRcrCRMatPrefPerfDestMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 2, 3, 1, 3),
    _H3cRcrCRMatPrefPerfDestMaskLen_Type()
)
h3cRcrCRMatPrefPerfDestMaskLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRcrCRMatPrefPerfDestMaskLen.setStatus("current")


class _H3cRcrCRMatPrefPerfDelayTime_Type(Integer32):
    """Custom type h3cRcrCRMatPrefPerfDelayTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_H3cRcrCRMatPrefPerfDelayTime_Type.__name__ = "Integer32"
_H3cRcrCRMatPrefPerfDelayTime_Object = MibTableColumn
h3cRcrCRMatPrefPerfDelayTime = _H3cRcrCRMatPrefPerfDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 2, 3, 1, 4),
    _H3cRcrCRMatPrefPerfDelayTime_Type()
)
h3cRcrCRMatPrefPerfDelayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRcrCRMatPrefPerfDelayTime.setStatus("current")
if mibBuilder.loadTexts:
    h3cRcrCRMatPrefPerfDelayTime.setUnits("second")


class _H3cRcrCRMatPrefPerfLossRate_Type(Integer32):
    """Custom type h3cRcrCRMatPrefPerfLossRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_H3cRcrCRMatPrefPerfLossRate_Type.__name__ = "Integer32"
_H3cRcrCRMatPrefPerfLossRate_Object = MibTableColumn
h3cRcrCRMatPrefPerfLossRate = _H3cRcrCRMatPrefPerfLossRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 2, 3, 1, 5),
    _H3cRcrCRMatPrefPerfLossRate_Type()
)
h3cRcrCRMatPrefPerfLossRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRcrCRMatPrefPerfLossRate.setStatus("current")
if mibBuilder.loadTexts:
    h3cRcrCRMatPrefPerfLossRate.setUnits("%")
_H3cRcrCRMatPrefPerfThroughput_Type = Integer32
_H3cRcrCRMatPrefPerfThroughput_Object = MibTableColumn
h3cRcrCRMatPrefPerfThroughput = _H3cRcrCRMatPrefPerfThroughput_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 2, 3, 1, 6),
    _H3cRcrCRMatPrefPerfThroughput_Type()
)
h3cRcrCRMatPrefPerfThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRcrCRMatPrefPerfThroughput.setStatus("current")
if mibBuilder.loadTexts:
    h3cRcrCRMatPrefPerfThroughput.setUnits("kb")
_H3cRcrCRAdjustPrefixTable_Object = MibTable
h3cRcrCRAdjustPrefixTable = _H3cRcrCRAdjustPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 2, 4)
)
if mibBuilder.loadTexts:
    h3cRcrCRAdjustPrefixTable.setStatus("current")
_H3cRcrCRAdjustPrefixEntry_Object = MibTableRow
h3cRcrCRAdjustPrefixEntry = _H3cRcrCRAdjustPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 2, 4, 1)
)
h3cRcrCRAdjustPrefixEntry.setIndexNames(
    (0, "A3COM-HUAWEI-RCR-MIB", "h3cRcrCRAdjuPrefDestAddrType"),
    (0, "A3COM-HUAWEI-RCR-MIB", "h3cRcrCRAdjuPrefDestAddr"),
    (0, "A3COM-HUAWEI-RCR-MIB", "h3cRcrCRAdjuPrefMaskLen"),
    (0, "A3COM-HUAWEI-RCR-MIB", "h3cRcrCRAdjuPrefPreMRName"),
    (0, "A3COM-HUAWEI-RCR-MIB", "h3cRcrCRAdjuPrefPreOutIfName"),
)
if mibBuilder.loadTexts:
    h3cRcrCRAdjustPrefixEntry.setStatus("current")
_H3cRcrCRAdjuPrefDestAddrType_Type = InetAddressType
_H3cRcrCRAdjuPrefDestAddrType_Object = MibTableColumn
h3cRcrCRAdjuPrefDestAddrType = _H3cRcrCRAdjuPrefDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 2, 4, 1, 1),
    _H3cRcrCRAdjuPrefDestAddrType_Type()
)
h3cRcrCRAdjuPrefDestAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRcrCRAdjuPrefDestAddrType.setStatus("current")
_H3cRcrCRAdjuPrefDestAddr_Type = InetAddress
_H3cRcrCRAdjuPrefDestAddr_Object = MibTableColumn
h3cRcrCRAdjuPrefDestAddr = _H3cRcrCRAdjuPrefDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 2, 4, 1, 2),
    _H3cRcrCRAdjuPrefDestAddr_Type()
)
h3cRcrCRAdjuPrefDestAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRcrCRAdjuPrefDestAddr.setStatus("current")


class _H3cRcrCRAdjuPrefMaskLen_Type(Integer32):
    """Custom type h3cRcrCRAdjuPrefMaskLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_H3cRcrCRAdjuPrefMaskLen_Type.__name__ = "Integer32"
_H3cRcrCRAdjuPrefMaskLen_Object = MibTableColumn
h3cRcrCRAdjuPrefMaskLen = _H3cRcrCRAdjuPrefMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 2, 4, 1, 3),
    _H3cRcrCRAdjuPrefMaskLen_Type()
)
h3cRcrCRAdjuPrefMaskLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRcrCRAdjuPrefMaskLen.setStatus("current")


class _H3cRcrCRAdjuPrefPreMRName_Type(OctetString):
    """Custom type h3cRcrCRAdjuPrefPreMRName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_H3cRcrCRAdjuPrefPreMRName_Type.__name__ = "OctetString"
_H3cRcrCRAdjuPrefPreMRName_Object = MibTableColumn
h3cRcrCRAdjuPrefPreMRName = _H3cRcrCRAdjuPrefPreMRName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 2, 4, 1, 4),
    _H3cRcrCRAdjuPrefPreMRName_Type()
)
h3cRcrCRAdjuPrefPreMRName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRcrCRAdjuPrefPreMRName.setStatus("current")


class _H3cRcrCRAdjuPrefPreOutIfName_Type(OctetString):
    """Custom type h3cRcrCRAdjuPrefPreOutIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_H3cRcrCRAdjuPrefPreOutIfName_Type.__name__ = "OctetString"
_H3cRcrCRAdjuPrefPreOutIfName_Object = MibTableColumn
h3cRcrCRAdjuPrefPreOutIfName = _H3cRcrCRAdjuPrefPreOutIfName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 2, 4, 1, 5),
    _H3cRcrCRAdjuPrefPreOutIfName_Type()
)
h3cRcrCRAdjuPrefPreOutIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRcrCRAdjuPrefPreOutIfName.setStatus("current")


class _H3cRcrCRAdjuPrefCurMRName_Type(OctetString):
    """Custom type h3cRcrCRAdjuPrefCurMRName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_H3cRcrCRAdjuPrefCurMRName_Type.__name__ = "OctetString"
_H3cRcrCRAdjuPrefCurMRName_Object = MibTableColumn
h3cRcrCRAdjuPrefCurMRName = _H3cRcrCRAdjuPrefCurMRName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 2, 4, 1, 6),
    _H3cRcrCRAdjuPrefCurMRName_Type()
)
h3cRcrCRAdjuPrefCurMRName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRcrCRAdjuPrefCurMRName.setStatus("current")
_H3cRcrCRAdjuPrefCurOutIfName_Type = OctetString
_H3cRcrCRAdjuPrefCurOutIfName_Object = MibTableColumn
h3cRcrCRAdjuPrefCurOutIfName = _H3cRcrCRAdjuPrefCurOutIfName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 2, 4, 1, 7),
    _H3cRcrCRAdjuPrefCurOutIfName_Type()
)
h3cRcrCRAdjuPrefCurOutIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRcrCRAdjuPrefCurOutIfName.setStatus("current")
_H3cRcrCRAdjuPrefPersistTime_Type = Integer32
_H3cRcrCRAdjuPrefPersistTime_Object = MibTableColumn
h3cRcrCRAdjuPrefPersistTime = _H3cRcrCRAdjuPrefPersistTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 2, 4, 1, 8),
    _H3cRcrCRAdjuPrefPersistTime_Type()
)
h3cRcrCRAdjuPrefPersistTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRcrCRAdjuPrefPersistTime.setStatus("current")
if mibBuilder.loadTexts:
    h3cRcrCRAdjuPrefPersistTime.setUnits("second")
_H3cRcrCRAdjuPrefAgeTime_Type = Integer32
_H3cRcrCRAdjuPrefAgeTime_Object = MibTableColumn
h3cRcrCRAdjuPrefAgeTime = _H3cRcrCRAdjuPrefAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 48, 2, 4, 1, 9),
    _H3cRcrCRAdjuPrefAgeTime_Type()
)
h3cRcrCRAdjuPrefAgeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRcrCRAdjuPrefAgeTime.setStatus("current")
if mibBuilder.loadTexts:
    h3cRcrCRAdjuPrefAgeTime.setUnits("second")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-RCR-MIB",
    **{"h3cRcr": h3cRcr,
       "h3cRcrMR": h3cRcrMR,
       "h3cRcrMRGroup": h3cRcrMRGroup,
       "h3cRcrMRAllMaxUsedBandRate": h3cRcrMRAllMaxUsedBandRate,
       "h3cRcrMRAllMinUsedBandRate": h3cRcrMRAllMinUsedBandRate,
       "h3cRcrMRListenTime": h3cRcrMRListenTime,
       "h3cRcrMRStateTable": h3cRcrMRStateTable,
       "h3cRcrMRStateEntry": h3cRcrMRStateEntry,
       "h3cRcrMRName": h3cRcrMRName,
       "h3cRcrMRState": h3cRcrMRState,
       "h3cRcrMRAuthType": h3cRcrMRAuthType,
       "h3cRcrMRAuthPwd": h3cRcrMRAuthPwd,
       "h3cRcrMROutIfStateTable": h3cRcrMROutIfStateTable,
       "h3cRcrMROutIfStateEntry": h3cRcrMROutIfStateEntry,
       "h3cRcrMROutIfName": h3cRcrMROutIfName,
       "h3cRcrMROutIfState": h3cRcrMROutIfState,
       "h3cRcrMROutIfMaxUsedBandRate": h3cRcrMROutIfMaxUsedBandRate,
       "h3cRcrMROutIfMinUsedBandRate": h3cRcrMROutIfMinUsedBandRate,
       "h3cRcrMROutIfUsedBandRate": h3cRcrMROutIfUsedBandRate,
       "h3cRcrCR": h3cRcrCR,
       "h3cRcrCRGroup": h3cRcrCRGroup,
       "h3cRcrCRState": h3cRcrCRState,
       "h3cRcrCRPortNum": h3cRcrCRPortNum,
       "h3cRcrCRCtrlMode": h3cRcrCRCtrlMode,
       "h3cRcrCRChooseMode": h3cRcrCRChooseMode,
       "h3cRcrCRKeepaliveTime": h3cRcrCRKeepaliveTime,
       "h3cRcrCRPolicyMode": h3cRcrCRPolicyMode,
       "h3cRcrCRStudyMode": h3cRcrCRStudyMode,
       "h3cRcrCRStudyIpPrefixNum": h3cRcrCRStudyIpPrefixNum,
       "h3cRcrCRIpPrefixLen": h3cRcrCRIpPrefixLen,
       "h3cRcrCRRcrPolicyTable": h3cRcrCRRcrPolicyTable,
       "h3cRcrCRRcrPolicyEntry": h3cRcrCRRcrPolicyEntry,
       "h3cRcrCRRcrPlyID": h3cRcrCRRcrPlyID,
       "h3cRcrCRRcrPlyMatchIPListName": h3cRcrCRRcrPlyMatchIPListName,
       "h3cRcrCRRcrPlyMatchStudyEnable": h3cRcrCRRcrPlyMatchStudyEnable,
       "h3cRcrCRRcrPlyMatchOperPlyName": h3cRcrCRRcrPlyMatchOperPlyName,
       "h3cRcrCRRcrAclNumber": h3cRcrCRRcrAclNumber,
       "h3cRcrCRRcrPlyDelayTime": h3cRcrCRRcrPlyDelayTime,
       "h3cRcrCRRcrPlyLossRate": h3cRcrCRRcrPlyLossRate,
       "h3cRcrCRMatPrefixPerfTable": h3cRcrCRMatPrefixPerfTable,
       "h3cRcrCRMatPrefixPerfEntry": h3cRcrCRMatPrefixPerfEntry,
       "h3cRcrCRMatPrefPerfAddrType": h3cRcrCRMatPrefPerfAddrType,
       "h3cRcrCRMatPrefPerfDestIPAddr": h3cRcrCRMatPrefPerfDestIPAddr,
       "h3cRcrCRMatPrefPerfDestMaskLen": h3cRcrCRMatPrefPerfDestMaskLen,
       "h3cRcrCRMatPrefPerfDelayTime": h3cRcrCRMatPrefPerfDelayTime,
       "h3cRcrCRMatPrefPerfLossRate": h3cRcrCRMatPrefPerfLossRate,
       "h3cRcrCRMatPrefPerfThroughput": h3cRcrCRMatPrefPerfThroughput,
       "h3cRcrCRAdjustPrefixTable": h3cRcrCRAdjustPrefixTable,
       "h3cRcrCRAdjustPrefixEntry": h3cRcrCRAdjustPrefixEntry,
       "h3cRcrCRAdjuPrefDestAddrType": h3cRcrCRAdjuPrefDestAddrType,
       "h3cRcrCRAdjuPrefDestAddr": h3cRcrCRAdjuPrefDestAddr,
       "h3cRcrCRAdjuPrefMaskLen": h3cRcrCRAdjuPrefMaskLen,
       "h3cRcrCRAdjuPrefPreMRName": h3cRcrCRAdjuPrefPreMRName,
       "h3cRcrCRAdjuPrefPreOutIfName": h3cRcrCRAdjuPrefPreOutIfName,
       "h3cRcrCRAdjuPrefCurMRName": h3cRcrCRAdjuPrefCurMRName,
       "h3cRcrCRAdjuPrefCurOutIfName": h3cRcrCRAdjuPrefCurOutIfName,
       "h3cRcrCRAdjuPrefPersistTime": h3cRcrCRAdjuPrefPersistTime,
       "h3cRcrCRAdjuPrefAgeTime": h3cRcrCRAdjuPrefAgeTime}
)
