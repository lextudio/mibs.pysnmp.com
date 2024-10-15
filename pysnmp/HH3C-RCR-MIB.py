# SNMP MIB module (HH3C-RCR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-RCR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:43 2024
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

hh3cRcr = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48)
)
hh3cRcr.setRevisions(
        ("2005-06-28 19:36",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cRcrMR_ObjectIdentity = ObjectIdentity
hh3cRcrMR = _Hh3cRcrMR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 1)
)
_Hh3cRcrMRGroup_ObjectIdentity = ObjectIdentity
hh3cRcrMRGroup = _Hh3cRcrMRGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 1, 1)
)


class _Hh3cRcrMRAllMaxUsedBandRate_Type(Integer32):
    """Custom type hh3cRcrMRAllMaxUsedBandRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Hh3cRcrMRAllMaxUsedBandRate_Type.__name__ = "Integer32"
_Hh3cRcrMRAllMaxUsedBandRate_Object = MibScalar
hh3cRcrMRAllMaxUsedBandRate = _Hh3cRcrMRAllMaxUsedBandRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 1, 1, 1),
    _Hh3cRcrMRAllMaxUsedBandRate_Type()
)
hh3cRcrMRAllMaxUsedBandRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRcrMRAllMaxUsedBandRate.setStatus("current")
if mibBuilder.loadTexts:
    hh3cRcrMRAllMaxUsedBandRate.setUnits("%")


class _Hh3cRcrMRAllMinUsedBandRate_Type(Integer32):
    """Custom type hh3cRcrMRAllMinUsedBandRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cRcrMRAllMinUsedBandRate_Type.__name__ = "Integer32"
_Hh3cRcrMRAllMinUsedBandRate_Object = MibScalar
hh3cRcrMRAllMinUsedBandRate = _Hh3cRcrMRAllMinUsedBandRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 1, 1, 2),
    _Hh3cRcrMRAllMinUsedBandRate_Type()
)
hh3cRcrMRAllMinUsedBandRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRcrMRAllMinUsedBandRate.setStatus("current")
if mibBuilder.loadTexts:
    hh3cRcrMRAllMinUsedBandRate.setUnits("%")


class _Hh3cRcrMRListenTime_Type(Integer32):
    """Custom type hh3cRcrMRListenTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_Hh3cRcrMRListenTime_Type.__name__ = "Integer32"
_Hh3cRcrMRListenTime_Object = MibScalar
hh3cRcrMRListenTime = _Hh3cRcrMRListenTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 1, 1, 3),
    _Hh3cRcrMRListenTime_Type()
)
hh3cRcrMRListenTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRcrMRListenTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cRcrMRListenTime.setUnits("minute")
_Hh3cRcrMRStateTable_Object = MibTable
hh3cRcrMRStateTable = _Hh3cRcrMRStateTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cRcrMRStateTable.setStatus("current")
_Hh3cRcrMRStateEntry_Object = MibTableRow
hh3cRcrMRStateEntry = _Hh3cRcrMRStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 1, 2, 1)
)
hh3cRcrMRStateEntry.setIndexNames(
    (0, "HH3C-RCR-MIB", "hh3cRcrMRName"),
)
if mibBuilder.loadTexts:
    hh3cRcrMRStateEntry.setStatus("current")


class _Hh3cRcrMRName_Type(OctetString):
    """Custom type hh3cRcrMRName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cRcrMRName_Type.__name__ = "OctetString"
_Hh3cRcrMRName_Object = MibTableColumn
hh3cRcrMRName = _Hh3cRcrMRName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 1, 2, 1, 1),
    _Hh3cRcrMRName_Type()
)
hh3cRcrMRName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRcrMRName.setStatus("current")


class _Hh3cRcrMRState_Type(Integer32):
    """Custom type hh3cRcrMRState based on Integer32"""
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


_Hh3cRcrMRState_Type.__name__ = "Integer32"
_Hh3cRcrMRState_Object = MibTableColumn
hh3cRcrMRState = _Hh3cRcrMRState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 1, 2, 1, 2),
    _Hh3cRcrMRState_Type()
)
hh3cRcrMRState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRcrMRState.setStatus("current")


class _Hh3cRcrMRAuthType_Type(Integer32):
    """Custom type hh3cRcrMRAuthType based on Integer32"""
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


_Hh3cRcrMRAuthType_Type.__name__ = "Integer32"
_Hh3cRcrMRAuthType_Object = MibTableColumn
hh3cRcrMRAuthType = _Hh3cRcrMRAuthType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 1, 2, 1, 3),
    _Hh3cRcrMRAuthType_Type()
)
hh3cRcrMRAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRcrMRAuthType.setStatus("current")
_Hh3cRcrMRAuthPwd_Type = OctetString
_Hh3cRcrMRAuthPwd_Object = MibTableColumn
hh3cRcrMRAuthPwd = _Hh3cRcrMRAuthPwd_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 1, 2, 1, 4),
    _Hh3cRcrMRAuthPwd_Type()
)
hh3cRcrMRAuthPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRcrMRAuthPwd.setStatus("current")
_Hh3cRcrMROutIfStateTable_Object = MibTable
hh3cRcrMROutIfStateTable = _Hh3cRcrMROutIfStateTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cRcrMROutIfStateTable.setStatus("current")
_Hh3cRcrMROutIfStateEntry_Object = MibTableRow
hh3cRcrMROutIfStateEntry = _Hh3cRcrMROutIfStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 1, 3, 1)
)
hh3cRcrMROutIfStateEntry.setIndexNames(
    (0, "HH3C-RCR-MIB", "hh3cRcrMRName"),
    (0, "HH3C-RCR-MIB", "hh3cRcrMROutIfName"),
)
if mibBuilder.loadTexts:
    hh3cRcrMROutIfStateEntry.setStatus("current")


class _Hh3cRcrMROutIfName_Type(OctetString):
    """Custom type hh3cRcrMROutIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_Hh3cRcrMROutIfName_Type.__name__ = "OctetString"
_Hh3cRcrMROutIfName_Object = MibTableColumn
hh3cRcrMROutIfName = _Hh3cRcrMROutIfName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 1, 3, 1, 1),
    _Hh3cRcrMROutIfName_Type()
)
hh3cRcrMROutIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRcrMROutIfName.setStatus("current")


class _Hh3cRcrMROutIfState_Type(Integer32):
    """Custom type hh3cRcrMROutIfState based on Integer32"""
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


_Hh3cRcrMROutIfState_Type.__name__ = "Integer32"
_Hh3cRcrMROutIfState_Object = MibTableColumn
hh3cRcrMROutIfState = _Hh3cRcrMROutIfState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 1, 3, 1, 2),
    _Hh3cRcrMROutIfState_Type()
)
hh3cRcrMROutIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRcrMROutIfState.setStatus("current")


class _Hh3cRcrMROutIfMaxUsedBandRate_Type(Integer32):
    """Custom type hh3cRcrMROutIfMaxUsedBandRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Hh3cRcrMROutIfMaxUsedBandRate_Type.__name__ = "Integer32"
_Hh3cRcrMROutIfMaxUsedBandRate_Object = MibTableColumn
hh3cRcrMROutIfMaxUsedBandRate = _Hh3cRcrMROutIfMaxUsedBandRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 1, 3, 1, 3),
    _Hh3cRcrMROutIfMaxUsedBandRate_Type()
)
hh3cRcrMROutIfMaxUsedBandRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRcrMROutIfMaxUsedBandRate.setStatus("current")
if mibBuilder.loadTexts:
    hh3cRcrMROutIfMaxUsedBandRate.setUnits("%")


class _Hh3cRcrMROutIfMinUsedBandRate_Type(Integer32):
    """Custom type hh3cRcrMROutIfMinUsedBandRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cRcrMROutIfMinUsedBandRate_Type.__name__ = "Integer32"
_Hh3cRcrMROutIfMinUsedBandRate_Object = MibTableColumn
hh3cRcrMROutIfMinUsedBandRate = _Hh3cRcrMROutIfMinUsedBandRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 1, 3, 1, 4),
    _Hh3cRcrMROutIfMinUsedBandRate_Type()
)
hh3cRcrMROutIfMinUsedBandRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRcrMROutIfMinUsedBandRate.setStatus("current")
if mibBuilder.loadTexts:
    hh3cRcrMROutIfMinUsedBandRate.setUnits("%")


class _Hh3cRcrMROutIfUsedBandRate_Type(Integer32):
    """Custom type hh3cRcrMROutIfUsedBandRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cRcrMROutIfUsedBandRate_Type.__name__ = "Integer32"
_Hh3cRcrMROutIfUsedBandRate_Object = MibTableColumn
hh3cRcrMROutIfUsedBandRate = _Hh3cRcrMROutIfUsedBandRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 1, 3, 1, 5),
    _Hh3cRcrMROutIfUsedBandRate_Type()
)
hh3cRcrMROutIfUsedBandRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRcrMROutIfUsedBandRate.setStatus("current")
if mibBuilder.loadTexts:
    hh3cRcrMROutIfUsedBandRate.setUnits("%")
_Hh3cRcrCR_ObjectIdentity = ObjectIdentity
hh3cRcrCR = _Hh3cRcrCR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 2)
)
_Hh3cRcrCRGroup_ObjectIdentity = ObjectIdentity
hh3cRcrCRGroup = _Hh3cRcrCRGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 1)
)


class _Hh3cRcrCRState_Type(Integer32):
    """Custom type hh3cRcrCRState based on Integer32"""
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


_Hh3cRcrCRState_Type.__name__ = "Integer32"
_Hh3cRcrCRState_Object = MibScalar
hh3cRcrCRState = _Hh3cRcrCRState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 1, 1),
    _Hh3cRcrCRState_Type()
)
hh3cRcrCRState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRcrCRState.setStatus("current")
_Hh3cRcrCRPortNum_Type = Integer32
_Hh3cRcrCRPortNum_Object = MibScalar
hh3cRcrCRPortNum = _Hh3cRcrCRPortNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 1, 2),
    _Hh3cRcrCRPortNum_Type()
)
hh3cRcrCRPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRcrCRPortNum.setStatus("current")


class _Hh3cRcrCRCtrlMode_Type(Integer32):
    """Custom type hh3cRcrCRCtrlMode based on Integer32"""
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


_Hh3cRcrCRCtrlMode_Type.__name__ = "Integer32"
_Hh3cRcrCRCtrlMode_Object = MibScalar
hh3cRcrCRCtrlMode = _Hh3cRcrCRCtrlMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 1, 3),
    _Hh3cRcrCRCtrlMode_Type()
)
hh3cRcrCRCtrlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRcrCRCtrlMode.setStatus("current")


class _Hh3cRcrCRChooseMode_Type(Integer32):
    """Custom type hh3cRcrCRChooseMode based on Integer32"""
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


_Hh3cRcrCRChooseMode_Type.__name__ = "Integer32"
_Hh3cRcrCRChooseMode_Object = MibScalar
hh3cRcrCRChooseMode = _Hh3cRcrCRChooseMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 1, 4),
    _Hh3cRcrCRChooseMode_Type()
)
hh3cRcrCRChooseMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRcrCRChooseMode.setStatus("current")


class _Hh3cRcrCRKeepaliveTime_Type(Integer32):
    """Custom type hh3cRcrCRKeepaliveTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_Hh3cRcrCRKeepaliveTime_Type.__name__ = "Integer32"
_Hh3cRcrCRKeepaliveTime_Object = MibScalar
hh3cRcrCRKeepaliveTime = _Hh3cRcrCRKeepaliveTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 1, 5),
    _Hh3cRcrCRKeepaliveTime_Type()
)
hh3cRcrCRKeepaliveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRcrCRKeepaliveTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cRcrCRKeepaliveTime.setUnits("second")


class _Hh3cRcrCRPolicyMode_Type(Integer32):
    """Custom type hh3cRcrCRPolicyMode based on Integer32"""
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


_Hh3cRcrCRPolicyMode_Type.__name__ = "Integer32"
_Hh3cRcrCRPolicyMode_Object = MibScalar
hh3cRcrCRPolicyMode = _Hh3cRcrCRPolicyMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 1, 6),
    _Hh3cRcrCRPolicyMode_Type()
)
hh3cRcrCRPolicyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRcrCRPolicyMode.setStatus("current")


class _Hh3cRcrCRStudyMode_Type(Integer32):
    """Custom type hh3cRcrCRStudyMode based on Integer32"""
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


_Hh3cRcrCRStudyMode_Type.__name__ = "Integer32"
_Hh3cRcrCRStudyMode_Object = MibScalar
hh3cRcrCRStudyMode = _Hh3cRcrCRStudyMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 1, 7),
    _Hh3cRcrCRStudyMode_Type()
)
hh3cRcrCRStudyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRcrCRStudyMode.setStatus("current")


class _Hh3cRcrCRStudyIpPrefixNum_Type(Integer32):
    """Custom type hh3cRcrCRStudyIpPrefixNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2500),
    )


_Hh3cRcrCRStudyIpPrefixNum_Type.__name__ = "Integer32"
_Hh3cRcrCRStudyIpPrefixNum_Object = MibScalar
hh3cRcrCRStudyIpPrefixNum = _Hh3cRcrCRStudyIpPrefixNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 1, 8),
    _Hh3cRcrCRStudyIpPrefixNum_Type()
)
hh3cRcrCRStudyIpPrefixNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRcrCRStudyIpPrefixNum.setStatus("current")


class _Hh3cRcrCRIpPrefixLen_Type(Integer32):
    """Custom type hh3cRcrCRIpPrefixLen based on Integer32"""
    defaultValue = 24

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Hh3cRcrCRIpPrefixLen_Type.__name__ = "Integer32"
_Hh3cRcrCRIpPrefixLen_Object = MibScalar
hh3cRcrCRIpPrefixLen = _Hh3cRcrCRIpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 1, 9),
    _Hh3cRcrCRIpPrefixLen_Type()
)
hh3cRcrCRIpPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRcrCRIpPrefixLen.setStatus("current")
_Hh3cRcrCRRcrPolicyTable_Object = MibTable
hh3cRcrCRRcrPolicyTable = _Hh3cRcrCRRcrPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cRcrCRRcrPolicyTable.setStatus("current")
_Hh3cRcrCRRcrPolicyEntry_Object = MibTableRow
hh3cRcrCRRcrPolicyEntry = _Hh3cRcrCRRcrPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 2, 1)
)
hh3cRcrCRRcrPolicyEntry.setIndexNames(
    (0, "HH3C-RCR-MIB", "hh3cRcrCRRcrPlyID"),
)
if mibBuilder.loadTexts:
    hh3cRcrCRRcrPolicyEntry.setStatus("current")
_Hh3cRcrCRRcrPlyID_Type = Integer32
_Hh3cRcrCRRcrPlyID_Object = MibTableColumn
hh3cRcrCRRcrPlyID = _Hh3cRcrCRRcrPlyID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 2, 1, 1),
    _Hh3cRcrCRRcrPlyID_Type()
)
hh3cRcrCRRcrPlyID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRcrCRRcrPlyID.setStatus("current")


class _Hh3cRcrCRRcrPlyMatchIPListName_Type(OctetString):
    """Custom type hh3cRcrCRRcrPlyMatchIPListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_Hh3cRcrCRRcrPlyMatchIPListName_Type.__name__ = "OctetString"
_Hh3cRcrCRRcrPlyMatchIPListName_Object = MibTableColumn
hh3cRcrCRRcrPlyMatchIPListName = _Hh3cRcrCRRcrPlyMatchIPListName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 2, 1, 2),
    _Hh3cRcrCRRcrPlyMatchIPListName_Type()
)
hh3cRcrCRRcrPlyMatchIPListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRcrCRRcrPlyMatchIPListName.setStatus("current")


class _Hh3cRcrCRRcrPlyMatchStudyEnable_Type(Integer32):
    """Custom type hh3cRcrCRRcrPlyMatchStudyEnable based on Integer32"""
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


_Hh3cRcrCRRcrPlyMatchStudyEnable_Type.__name__ = "Integer32"
_Hh3cRcrCRRcrPlyMatchStudyEnable_Object = MibTableColumn
hh3cRcrCRRcrPlyMatchStudyEnable = _Hh3cRcrCRRcrPlyMatchStudyEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 2, 1, 3),
    _Hh3cRcrCRRcrPlyMatchStudyEnable_Type()
)
hh3cRcrCRRcrPlyMatchStudyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRcrCRRcrPlyMatchStudyEnable.setStatus("current")


class _Hh3cRcrCRRcrPlyMatchOperPlyName_Type(OctetString):
    """Custom type hh3cRcrCRRcrPlyMatchOperPlyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_Hh3cRcrCRRcrPlyMatchOperPlyName_Type.__name__ = "OctetString"
_Hh3cRcrCRRcrPlyMatchOperPlyName_Object = MibTableColumn
hh3cRcrCRRcrPlyMatchOperPlyName = _Hh3cRcrCRRcrPlyMatchOperPlyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 2, 1, 4),
    _Hh3cRcrCRRcrPlyMatchOperPlyName_Type()
)
hh3cRcrCRRcrPlyMatchOperPlyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRcrCRRcrPlyMatchOperPlyName.setStatus("current")


class _Hh3cRcrCRRcrAclNumber_Type(Integer32):
    """Custom type hh3cRcrCRRcrAclNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3000, 3999),
    )


_Hh3cRcrCRRcrAclNumber_Type.__name__ = "Integer32"
_Hh3cRcrCRRcrAclNumber_Object = MibTableColumn
hh3cRcrCRRcrAclNumber = _Hh3cRcrCRRcrAclNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 2, 1, 5),
    _Hh3cRcrCRRcrAclNumber_Type()
)
hh3cRcrCRRcrAclNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRcrCRRcrAclNumber.setStatus("current")


class _Hh3cRcrCRRcrPlyDelayTime_Type(Integer32):
    """Custom type hh3cRcrCRRcrPlyDelayTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_Hh3cRcrCRRcrPlyDelayTime_Type.__name__ = "Integer32"
_Hh3cRcrCRRcrPlyDelayTime_Object = MibTableColumn
hh3cRcrCRRcrPlyDelayTime = _Hh3cRcrCRRcrPlyDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 2, 1, 6),
    _Hh3cRcrCRRcrPlyDelayTime_Type()
)
hh3cRcrCRRcrPlyDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRcrCRRcrPlyDelayTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cRcrCRRcrPlyDelayTime.setUnits("millisecond")


class _Hh3cRcrCRRcrPlyLossRate_Type(Integer32):
    """Custom type hh3cRcrCRRcrPlyLossRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Hh3cRcrCRRcrPlyLossRate_Type.__name__ = "Integer32"
_Hh3cRcrCRRcrPlyLossRate_Object = MibTableColumn
hh3cRcrCRRcrPlyLossRate = _Hh3cRcrCRRcrPlyLossRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 2, 1, 7),
    _Hh3cRcrCRRcrPlyLossRate_Type()
)
hh3cRcrCRRcrPlyLossRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRcrCRRcrPlyLossRate.setStatus("current")
if mibBuilder.loadTexts:
    hh3cRcrCRRcrPlyLossRate.setUnits("%")
_Hh3cRcrCRMatPrefixPerfTable_Object = MibTable
hh3cRcrCRMatPrefixPerfTable = _Hh3cRcrCRMatPrefixPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cRcrCRMatPrefixPerfTable.setStatus("current")
_Hh3cRcrCRMatPrefixPerfEntry_Object = MibTableRow
hh3cRcrCRMatPrefixPerfEntry = _Hh3cRcrCRMatPrefixPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 3, 1)
)
hh3cRcrCRMatPrefixPerfEntry.setIndexNames(
    (0, "HH3C-RCR-MIB", "hh3cRcrCRMatPrefPerfAddrType"),
    (0, "HH3C-RCR-MIB", "hh3cRcrCRMatPrefPerfDestIPAddr"),
    (0, "HH3C-RCR-MIB", "hh3cRcrCRMatPrefPerfDestMaskLen"),
)
if mibBuilder.loadTexts:
    hh3cRcrCRMatPrefixPerfEntry.setStatus("current")
_Hh3cRcrCRMatPrefPerfAddrType_Type = InetAddressType
_Hh3cRcrCRMatPrefPerfAddrType_Object = MibTableColumn
hh3cRcrCRMatPrefPerfAddrType = _Hh3cRcrCRMatPrefPerfAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 3, 1, 1),
    _Hh3cRcrCRMatPrefPerfAddrType_Type()
)
hh3cRcrCRMatPrefPerfAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRcrCRMatPrefPerfAddrType.setStatus("current")
_Hh3cRcrCRMatPrefPerfDestIPAddr_Type = InetAddress
_Hh3cRcrCRMatPrefPerfDestIPAddr_Object = MibTableColumn
hh3cRcrCRMatPrefPerfDestIPAddr = _Hh3cRcrCRMatPrefPerfDestIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 3, 1, 2),
    _Hh3cRcrCRMatPrefPerfDestIPAddr_Type()
)
hh3cRcrCRMatPrefPerfDestIPAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRcrCRMatPrefPerfDestIPAddr.setStatus("current")


class _Hh3cRcrCRMatPrefPerfDestMaskLen_Type(Integer32):
    """Custom type hh3cRcrCRMatPrefPerfDestMaskLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Hh3cRcrCRMatPrefPerfDestMaskLen_Type.__name__ = "Integer32"
_Hh3cRcrCRMatPrefPerfDestMaskLen_Object = MibTableColumn
hh3cRcrCRMatPrefPerfDestMaskLen = _Hh3cRcrCRMatPrefPerfDestMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 3, 1, 3),
    _Hh3cRcrCRMatPrefPerfDestMaskLen_Type()
)
hh3cRcrCRMatPrefPerfDestMaskLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRcrCRMatPrefPerfDestMaskLen.setStatus("current")


class _Hh3cRcrCRMatPrefPerfDelayTime_Type(Integer32):
    """Custom type hh3cRcrCRMatPrefPerfDelayTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_Hh3cRcrCRMatPrefPerfDelayTime_Type.__name__ = "Integer32"
_Hh3cRcrCRMatPrefPerfDelayTime_Object = MibTableColumn
hh3cRcrCRMatPrefPerfDelayTime = _Hh3cRcrCRMatPrefPerfDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 3, 1, 4),
    _Hh3cRcrCRMatPrefPerfDelayTime_Type()
)
hh3cRcrCRMatPrefPerfDelayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRcrCRMatPrefPerfDelayTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cRcrCRMatPrefPerfDelayTime.setUnits("second")


class _Hh3cRcrCRMatPrefPerfLossRate_Type(Integer32):
    """Custom type hh3cRcrCRMatPrefPerfLossRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Hh3cRcrCRMatPrefPerfLossRate_Type.__name__ = "Integer32"
_Hh3cRcrCRMatPrefPerfLossRate_Object = MibTableColumn
hh3cRcrCRMatPrefPerfLossRate = _Hh3cRcrCRMatPrefPerfLossRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 3, 1, 5),
    _Hh3cRcrCRMatPrefPerfLossRate_Type()
)
hh3cRcrCRMatPrefPerfLossRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRcrCRMatPrefPerfLossRate.setStatus("current")
if mibBuilder.loadTexts:
    hh3cRcrCRMatPrefPerfLossRate.setUnits("%")
_Hh3cRcrCRMatPrefPerfThroughput_Type = Integer32
_Hh3cRcrCRMatPrefPerfThroughput_Object = MibTableColumn
hh3cRcrCRMatPrefPerfThroughput = _Hh3cRcrCRMatPrefPerfThroughput_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 3, 1, 6),
    _Hh3cRcrCRMatPrefPerfThroughput_Type()
)
hh3cRcrCRMatPrefPerfThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRcrCRMatPrefPerfThroughput.setStatus("current")
if mibBuilder.loadTexts:
    hh3cRcrCRMatPrefPerfThroughput.setUnits("kb")
_Hh3cRcrCRAdjustPrefixTable_Object = MibTable
hh3cRcrCRAdjustPrefixTable = _Hh3cRcrCRAdjustPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 4)
)
if mibBuilder.loadTexts:
    hh3cRcrCRAdjustPrefixTable.setStatus("current")
_Hh3cRcrCRAdjustPrefixEntry_Object = MibTableRow
hh3cRcrCRAdjustPrefixEntry = _Hh3cRcrCRAdjustPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 4, 1)
)
hh3cRcrCRAdjustPrefixEntry.setIndexNames(
    (0, "HH3C-RCR-MIB", "hh3cRcrCRAdjuPrefDestAddrType"),
    (0, "HH3C-RCR-MIB", "hh3cRcrCRAdjuPrefDestAddr"),
    (0, "HH3C-RCR-MIB", "hh3cRcrCRAdjuPrefMaskLen"),
    (0, "HH3C-RCR-MIB", "hh3cRcrCRAdjuPrefPreMRName"),
    (0, "HH3C-RCR-MIB", "hh3cRcrCRAdjuPrefPreOutIfName"),
)
if mibBuilder.loadTexts:
    hh3cRcrCRAdjustPrefixEntry.setStatus("current")
_Hh3cRcrCRAdjuPrefDestAddrType_Type = InetAddressType
_Hh3cRcrCRAdjuPrefDestAddrType_Object = MibTableColumn
hh3cRcrCRAdjuPrefDestAddrType = _Hh3cRcrCRAdjuPrefDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 4, 1, 1),
    _Hh3cRcrCRAdjuPrefDestAddrType_Type()
)
hh3cRcrCRAdjuPrefDestAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRcrCRAdjuPrefDestAddrType.setStatus("current")
_Hh3cRcrCRAdjuPrefDestAddr_Type = InetAddress
_Hh3cRcrCRAdjuPrefDestAddr_Object = MibTableColumn
hh3cRcrCRAdjuPrefDestAddr = _Hh3cRcrCRAdjuPrefDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 4, 1, 2),
    _Hh3cRcrCRAdjuPrefDestAddr_Type()
)
hh3cRcrCRAdjuPrefDestAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRcrCRAdjuPrefDestAddr.setStatus("current")


class _Hh3cRcrCRAdjuPrefMaskLen_Type(Integer32):
    """Custom type hh3cRcrCRAdjuPrefMaskLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Hh3cRcrCRAdjuPrefMaskLen_Type.__name__ = "Integer32"
_Hh3cRcrCRAdjuPrefMaskLen_Object = MibTableColumn
hh3cRcrCRAdjuPrefMaskLen = _Hh3cRcrCRAdjuPrefMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 4, 1, 3),
    _Hh3cRcrCRAdjuPrefMaskLen_Type()
)
hh3cRcrCRAdjuPrefMaskLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRcrCRAdjuPrefMaskLen.setStatus("current")


class _Hh3cRcrCRAdjuPrefPreMRName_Type(OctetString):
    """Custom type hh3cRcrCRAdjuPrefPreMRName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cRcrCRAdjuPrefPreMRName_Type.__name__ = "OctetString"
_Hh3cRcrCRAdjuPrefPreMRName_Object = MibTableColumn
hh3cRcrCRAdjuPrefPreMRName = _Hh3cRcrCRAdjuPrefPreMRName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 4, 1, 4),
    _Hh3cRcrCRAdjuPrefPreMRName_Type()
)
hh3cRcrCRAdjuPrefPreMRName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRcrCRAdjuPrefPreMRName.setStatus("current")


class _Hh3cRcrCRAdjuPrefPreOutIfName_Type(OctetString):
    """Custom type hh3cRcrCRAdjuPrefPreOutIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_Hh3cRcrCRAdjuPrefPreOutIfName_Type.__name__ = "OctetString"
_Hh3cRcrCRAdjuPrefPreOutIfName_Object = MibTableColumn
hh3cRcrCRAdjuPrefPreOutIfName = _Hh3cRcrCRAdjuPrefPreOutIfName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 4, 1, 5),
    _Hh3cRcrCRAdjuPrefPreOutIfName_Type()
)
hh3cRcrCRAdjuPrefPreOutIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRcrCRAdjuPrefPreOutIfName.setStatus("current")


class _Hh3cRcrCRAdjuPrefCurMRName_Type(OctetString):
    """Custom type hh3cRcrCRAdjuPrefCurMRName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cRcrCRAdjuPrefCurMRName_Type.__name__ = "OctetString"
_Hh3cRcrCRAdjuPrefCurMRName_Object = MibTableColumn
hh3cRcrCRAdjuPrefCurMRName = _Hh3cRcrCRAdjuPrefCurMRName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 4, 1, 6),
    _Hh3cRcrCRAdjuPrefCurMRName_Type()
)
hh3cRcrCRAdjuPrefCurMRName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRcrCRAdjuPrefCurMRName.setStatus("current")
_Hh3cRcrCRAdjuPrefCurOutIfName_Type = OctetString
_Hh3cRcrCRAdjuPrefCurOutIfName_Object = MibTableColumn
hh3cRcrCRAdjuPrefCurOutIfName = _Hh3cRcrCRAdjuPrefCurOutIfName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 4, 1, 7),
    _Hh3cRcrCRAdjuPrefCurOutIfName_Type()
)
hh3cRcrCRAdjuPrefCurOutIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRcrCRAdjuPrefCurOutIfName.setStatus("current")
_Hh3cRcrCRAdjuPrefPersistTime_Type = Integer32
_Hh3cRcrCRAdjuPrefPersistTime_Object = MibTableColumn
hh3cRcrCRAdjuPrefPersistTime = _Hh3cRcrCRAdjuPrefPersistTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 4, 1, 8),
    _Hh3cRcrCRAdjuPrefPersistTime_Type()
)
hh3cRcrCRAdjuPrefPersistTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRcrCRAdjuPrefPersistTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cRcrCRAdjuPrefPersistTime.setUnits("second")
_Hh3cRcrCRAdjuPrefAgeTime_Type = Integer32
_Hh3cRcrCRAdjuPrefAgeTime_Object = MibTableColumn
hh3cRcrCRAdjuPrefAgeTime = _Hh3cRcrCRAdjuPrefAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 4, 1, 9),
    _Hh3cRcrCRAdjuPrefAgeTime_Type()
)
hh3cRcrCRAdjuPrefAgeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRcrCRAdjuPrefAgeTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cRcrCRAdjuPrefAgeTime.setUnits("second")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-RCR-MIB",
    **{"hh3cRcr": hh3cRcr,
       "hh3cRcrMR": hh3cRcrMR,
       "hh3cRcrMRGroup": hh3cRcrMRGroup,
       "hh3cRcrMRAllMaxUsedBandRate": hh3cRcrMRAllMaxUsedBandRate,
       "hh3cRcrMRAllMinUsedBandRate": hh3cRcrMRAllMinUsedBandRate,
       "hh3cRcrMRListenTime": hh3cRcrMRListenTime,
       "hh3cRcrMRStateTable": hh3cRcrMRStateTable,
       "hh3cRcrMRStateEntry": hh3cRcrMRStateEntry,
       "hh3cRcrMRName": hh3cRcrMRName,
       "hh3cRcrMRState": hh3cRcrMRState,
       "hh3cRcrMRAuthType": hh3cRcrMRAuthType,
       "hh3cRcrMRAuthPwd": hh3cRcrMRAuthPwd,
       "hh3cRcrMROutIfStateTable": hh3cRcrMROutIfStateTable,
       "hh3cRcrMROutIfStateEntry": hh3cRcrMROutIfStateEntry,
       "hh3cRcrMROutIfName": hh3cRcrMROutIfName,
       "hh3cRcrMROutIfState": hh3cRcrMROutIfState,
       "hh3cRcrMROutIfMaxUsedBandRate": hh3cRcrMROutIfMaxUsedBandRate,
       "hh3cRcrMROutIfMinUsedBandRate": hh3cRcrMROutIfMinUsedBandRate,
       "hh3cRcrMROutIfUsedBandRate": hh3cRcrMROutIfUsedBandRate,
       "hh3cRcrCR": hh3cRcrCR,
       "hh3cRcrCRGroup": hh3cRcrCRGroup,
       "hh3cRcrCRState": hh3cRcrCRState,
       "hh3cRcrCRPortNum": hh3cRcrCRPortNum,
       "hh3cRcrCRCtrlMode": hh3cRcrCRCtrlMode,
       "hh3cRcrCRChooseMode": hh3cRcrCRChooseMode,
       "hh3cRcrCRKeepaliveTime": hh3cRcrCRKeepaliveTime,
       "hh3cRcrCRPolicyMode": hh3cRcrCRPolicyMode,
       "hh3cRcrCRStudyMode": hh3cRcrCRStudyMode,
       "hh3cRcrCRStudyIpPrefixNum": hh3cRcrCRStudyIpPrefixNum,
       "hh3cRcrCRIpPrefixLen": hh3cRcrCRIpPrefixLen,
       "hh3cRcrCRRcrPolicyTable": hh3cRcrCRRcrPolicyTable,
       "hh3cRcrCRRcrPolicyEntry": hh3cRcrCRRcrPolicyEntry,
       "hh3cRcrCRRcrPlyID": hh3cRcrCRRcrPlyID,
       "hh3cRcrCRRcrPlyMatchIPListName": hh3cRcrCRRcrPlyMatchIPListName,
       "hh3cRcrCRRcrPlyMatchStudyEnable": hh3cRcrCRRcrPlyMatchStudyEnable,
       "hh3cRcrCRRcrPlyMatchOperPlyName": hh3cRcrCRRcrPlyMatchOperPlyName,
       "hh3cRcrCRRcrAclNumber": hh3cRcrCRRcrAclNumber,
       "hh3cRcrCRRcrPlyDelayTime": hh3cRcrCRRcrPlyDelayTime,
       "hh3cRcrCRRcrPlyLossRate": hh3cRcrCRRcrPlyLossRate,
       "hh3cRcrCRMatPrefixPerfTable": hh3cRcrCRMatPrefixPerfTable,
       "hh3cRcrCRMatPrefixPerfEntry": hh3cRcrCRMatPrefixPerfEntry,
       "hh3cRcrCRMatPrefPerfAddrType": hh3cRcrCRMatPrefPerfAddrType,
       "hh3cRcrCRMatPrefPerfDestIPAddr": hh3cRcrCRMatPrefPerfDestIPAddr,
       "hh3cRcrCRMatPrefPerfDestMaskLen": hh3cRcrCRMatPrefPerfDestMaskLen,
       "hh3cRcrCRMatPrefPerfDelayTime": hh3cRcrCRMatPrefPerfDelayTime,
       "hh3cRcrCRMatPrefPerfLossRate": hh3cRcrCRMatPrefPerfLossRate,
       "hh3cRcrCRMatPrefPerfThroughput": hh3cRcrCRMatPrefPerfThroughput,
       "hh3cRcrCRAdjustPrefixTable": hh3cRcrCRAdjustPrefixTable,
       "hh3cRcrCRAdjustPrefixEntry": hh3cRcrCRAdjustPrefixEntry,
       "hh3cRcrCRAdjuPrefDestAddrType": hh3cRcrCRAdjuPrefDestAddrType,
       "hh3cRcrCRAdjuPrefDestAddr": hh3cRcrCRAdjuPrefDestAddr,
       "hh3cRcrCRAdjuPrefMaskLen": hh3cRcrCRAdjuPrefMaskLen,
       "hh3cRcrCRAdjuPrefPreMRName": hh3cRcrCRAdjuPrefPreMRName,
       "hh3cRcrCRAdjuPrefPreOutIfName": hh3cRcrCRAdjuPrefPreOutIfName,
       "hh3cRcrCRAdjuPrefCurMRName": hh3cRcrCRAdjuPrefCurMRName,
       "hh3cRcrCRAdjuPrefCurOutIfName": hh3cRcrCRAdjuPrefCurOutIfName,
       "hh3cRcrCRAdjuPrefPersistTime": hh3cRcrCRAdjuPrefPersistTime,
       "hh3cRcrCRAdjuPrefAgeTime": hh3cRcrCRAdjuPrefAgeTime}
)
