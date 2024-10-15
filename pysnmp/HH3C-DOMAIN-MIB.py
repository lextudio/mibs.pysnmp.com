# SNMP MIB module (HH3C-DOMAIN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-DOMAIN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:48 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3cDomain = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cModeOfDomainScheme(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("none", 1),
          ("radius", 3),
          ("tacacs", 4))
    )



class Hh3cAAATypeDomainScheme(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("accounting", 1),
          ("authentication", 2),
          ("authorization", 3),
          ("none", 4))
    )



class Hh3cAccessModeofDomainScheme(Integer32, TextualConvention):
    status = "current"
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
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("command", 11),
          ("default", 1),
          ("dhcp", 8),
          ("dvpn", 7),
          ("gcm", 6),
          ("lanAccess", 3),
          ("login", 2),
          ("portal", 4),
          ("ppp", 5),
          ("superauthen", 10),
          ("voice", 9),
          ("wapi", 12))
    )



# MIB Managed Objects in the order of their OIDs

_Hh3cDomainControl_ObjectIdentity = ObjectIdentity
hh3cDomainControl = _Hh3cDomainControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 1)
)


class _Hh3cDomainDefault_Type(OctetString):
    """Custom type hh3cDomainDefault based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Hh3cDomainDefault_Type.__name__ = "OctetString"
_Hh3cDomainDefault_Object = MibScalar
hh3cDomainDefault = _Hh3cDomainDefault_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 1, 1),
    _Hh3cDomainDefault_Type()
)
hh3cDomainDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDomainDefault.setStatus("current")
_Hh3cDomainTables_ObjectIdentity = ObjectIdentity
hh3cDomainTables = _Hh3cDomainTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2)
)
_Hh3cDomainInfoTable_Object = MibTable
hh3cDomainInfoTable = _Hh3cDomainInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cDomainInfoTable.setStatus("current")
_Hh3cDomainInfoEntry_Object = MibTableRow
hh3cDomainInfoEntry = _Hh3cDomainInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1)
)
hh3cDomainInfoEntry.setIndexNames(
    (0, "HH3C-DOMAIN-MIB", "hh3cDomainName"),
)
if mibBuilder.loadTexts:
    hh3cDomainInfoEntry.setStatus("current")


class _Hh3cDomainName_Type(OctetString):
    """Custom type hh3cDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Hh3cDomainName_Type.__name__ = "OctetString"
_Hh3cDomainName_Object = MibTableColumn
hh3cDomainName = _Hh3cDomainName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 1),
    _Hh3cDomainName_Type()
)
hh3cDomainName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDomainName.setStatus("current")


class _Hh3cDomainState_Type(Integer32):
    """Custom type hh3cDomainState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("block", 2))
    )


_Hh3cDomainState_Type.__name__ = "Integer32"
_Hh3cDomainState_Object = MibTableColumn
hh3cDomainState = _Hh3cDomainState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 2),
    _Hh3cDomainState_Type()
)
hh3cDomainState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainState.setStatus("current")
_Hh3cDomainMaxAccessNum_Type = Integer32
_Hh3cDomainMaxAccessNum_Object = MibTableColumn
hh3cDomainMaxAccessNum = _Hh3cDomainMaxAccessNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 3),
    _Hh3cDomainMaxAccessNum_Type()
)
hh3cDomainMaxAccessNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainMaxAccessNum.setStatus("current")


class _Hh3cDomainVlanAssignMode_Type(Integer32):
    """Custom type hh3cDomainVlanAssignMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("integer", 1),
          ("string", 2),
          ("vlanlist", 3))
    )


_Hh3cDomainVlanAssignMode_Type.__name__ = "Integer32"
_Hh3cDomainVlanAssignMode_Object = MibTableColumn
hh3cDomainVlanAssignMode = _Hh3cDomainVlanAssignMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 4),
    _Hh3cDomainVlanAssignMode_Type()
)
hh3cDomainVlanAssignMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainVlanAssignMode.setStatus("current")
_Hh3cDomainIdleCutEnable_Type = TruthValue
_Hh3cDomainIdleCutEnable_Object = MibTableColumn
hh3cDomainIdleCutEnable = _Hh3cDomainIdleCutEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 5),
    _Hh3cDomainIdleCutEnable_Type()
)
hh3cDomainIdleCutEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainIdleCutEnable.setStatus("current")


class _Hh3cDomainIdleCutMaxTime_Type(Integer32):
    """Custom type hh3cDomainIdleCutMaxTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_Hh3cDomainIdleCutMaxTime_Type.__name__ = "Integer32"
_Hh3cDomainIdleCutMaxTime_Object = MibTableColumn
hh3cDomainIdleCutMaxTime = _Hh3cDomainIdleCutMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 6),
    _Hh3cDomainIdleCutMaxTime_Type()
)
hh3cDomainIdleCutMaxTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainIdleCutMaxTime.setStatus("current")


class _Hh3cDomainIdleCutMinFlow_Type(Integer32):
    """Custom type hh3cDomainIdleCutMinFlow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10240000),
    )


_Hh3cDomainIdleCutMinFlow_Type.__name__ = "Integer32"
_Hh3cDomainIdleCutMinFlow_Object = MibTableColumn
hh3cDomainIdleCutMinFlow = _Hh3cDomainIdleCutMinFlow_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 7),
    _Hh3cDomainIdleCutMinFlow_Type()
)
hh3cDomainIdleCutMinFlow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainIdleCutMinFlow.setStatus("current")
_Hh3cDomainMessengerEnable_Type = TruthValue
_Hh3cDomainMessengerEnable_Object = MibTableColumn
hh3cDomainMessengerEnable = _Hh3cDomainMessengerEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 8),
    _Hh3cDomainMessengerEnable_Type()
)
hh3cDomainMessengerEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainMessengerEnable.setStatus("current")


class _Hh3cDomainMessengerLimitTime_Type(Integer32):
    """Custom type hh3cDomainMessengerLimitTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_Hh3cDomainMessengerLimitTime_Type.__name__ = "Integer32"
_Hh3cDomainMessengerLimitTime_Object = MibTableColumn
hh3cDomainMessengerLimitTime = _Hh3cDomainMessengerLimitTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 9),
    _Hh3cDomainMessengerLimitTime_Type()
)
hh3cDomainMessengerLimitTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainMessengerLimitTime.setStatus("current")


class _Hh3cDomainMessengerSpanTime_Type(Integer32):
    """Custom type hh3cDomainMessengerSpanTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_Hh3cDomainMessengerSpanTime_Type.__name__ = "Integer32"
_Hh3cDomainMessengerSpanTime_Object = MibTableColumn
hh3cDomainMessengerSpanTime = _Hh3cDomainMessengerSpanTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 10),
    _Hh3cDomainMessengerSpanTime_Type()
)
hh3cDomainMessengerSpanTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainMessengerSpanTime.setStatus("current")
_Hh3cDomainSelfServiceEnable_Type = TruthValue
_Hh3cDomainSelfServiceEnable_Object = MibTableColumn
hh3cDomainSelfServiceEnable = _Hh3cDomainSelfServiceEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 11),
    _Hh3cDomainSelfServiceEnable_Type()
)
hh3cDomainSelfServiceEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainSelfServiceEnable.setStatus("current")


class _Hh3cDomainSelfServiceURL_Type(OctetString):
    """Custom type hh3cDomainSelfServiceURL based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Hh3cDomainSelfServiceURL_Type.__name__ = "OctetString"
_Hh3cDomainSelfServiceURL_Object = MibTableColumn
hh3cDomainSelfServiceURL = _Hh3cDomainSelfServiceURL_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 12),
    _Hh3cDomainSelfServiceURL_Type()
)
hh3cDomainSelfServiceURL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainSelfServiceURL.setStatus("current")


class _Hh3cDomainAccFailureAction_Type(Integer32):
    """Custom type hh3cDomainAccFailureAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("reject", 2))
    )


_Hh3cDomainAccFailureAction_Type.__name__ = "Integer32"
_Hh3cDomainAccFailureAction_Object = MibTableColumn
hh3cDomainAccFailureAction = _Hh3cDomainAccFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 13),
    _Hh3cDomainAccFailureAction_Type()
)
hh3cDomainAccFailureAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainAccFailureAction.setStatus("current")
_Hh3cDomainRowStatus_Type = RowStatus
_Hh3cDomainRowStatus_Object = MibTableColumn
hh3cDomainRowStatus = _Hh3cDomainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 14),
    _Hh3cDomainRowStatus_Type()
)
hh3cDomainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainRowStatus.setStatus("current")
_Hh3cDomainCurrentAccessNum_Type = Integer32
_Hh3cDomainCurrentAccessNum_Object = MibTableColumn
hh3cDomainCurrentAccessNum = _Hh3cDomainCurrentAccessNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 15),
    _Hh3cDomainCurrentAccessNum_Type()
)
hh3cDomainCurrentAccessNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainCurrentAccessNum.setStatus("current")
_Hh3cDomainSchemeTable_Object = MibTable
hh3cDomainSchemeTable = _Hh3cDomainSchemeTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cDomainSchemeTable.setStatus("current")
_Hh3cDomainSchemeEntry_Object = MibTableRow
hh3cDomainSchemeEntry = _Hh3cDomainSchemeEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 2, 1)
)
hh3cDomainSchemeEntry.setIndexNames(
    (0, "HH3C-DOMAIN-MIB", "hh3cDomainName"),
    (0, "HH3C-DOMAIN-MIB", "hh3cDomainSchemeIndex"),
)
if mibBuilder.loadTexts:
    hh3cDomainSchemeEntry.setStatus("current")
_Hh3cDomainSchemeIndex_Type = Integer32
_Hh3cDomainSchemeIndex_Object = MibTableColumn
hh3cDomainSchemeIndex = _Hh3cDomainSchemeIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 2, 1, 1),
    _Hh3cDomainSchemeIndex_Type()
)
hh3cDomainSchemeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDomainSchemeIndex.setStatus("current")
_Hh3cDomainSchemeMode_Type = Hh3cModeOfDomainScheme
_Hh3cDomainSchemeMode_Object = MibTableColumn
hh3cDomainSchemeMode = _Hh3cDomainSchemeMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 2, 1, 2),
    _Hh3cDomainSchemeMode_Type()
)
hh3cDomainSchemeMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainSchemeMode.setStatus("current")


class _Hh3cDomainAuthSchemeName_Type(OctetString):
    """Custom type hh3cDomainAuthSchemeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cDomainAuthSchemeName_Type.__name__ = "OctetString"
_Hh3cDomainAuthSchemeName_Object = MibTableColumn
hh3cDomainAuthSchemeName = _Hh3cDomainAuthSchemeName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 2, 1, 3),
    _Hh3cDomainAuthSchemeName_Type()
)
hh3cDomainAuthSchemeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainAuthSchemeName.setStatus("current")


class _Hh3cDomainAcctSchemeName_Type(OctetString):
    """Custom type hh3cDomainAcctSchemeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cDomainAcctSchemeName_Type.__name__ = "OctetString"
_Hh3cDomainAcctSchemeName_Object = MibTableColumn
hh3cDomainAcctSchemeName = _Hh3cDomainAcctSchemeName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 2, 1, 4),
    _Hh3cDomainAcctSchemeName_Type()
)
hh3cDomainAcctSchemeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainAcctSchemeName.setStatus("current")
_Hh3cDomainSchemeRowStatus_Type = RowStatus
_Hh3cDomainSchemeRowStatus_Object = MibTableColumn
hh3cDomainSchemeRowStatus = _Hh3cDomainSchemeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 2, 1, 5),
    _Hh3cDomainSchemeRowStatus_Type()
)
hh3cDomainSchemeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainSchemeRowStatus.setStatus("current")
_Hh3cDomainSchemeAAAType_Type = Hh3cAAATypeDomainScheme
_Hh3cDomainSchemeAAAType_Object = MibTableColumn
hh3cDomainSchemeAAAType = _Hh3cDomainSchemeAAAType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 2, 1, 6),
    _Hh3cDomainSchemeAAAType_Type()
)
hh3cDomainSchemeAAAType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainSchemeAAAType.setStatus("current")


class _Hh3cDomainSchemeAAAName_Type(OctetString):
    """Custom type hh3cDomainSchemeAAAName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cDomainSchemeAAAName_Type.__name__ = "OctetString"
_Hh3cDomainSchemeAAAName_Object = MibTableColumn
hh3cDomainSchemeAAAName = _Hh3cDomainSchemeAAAName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 2, 1, 7),
    _Hh3cDomainSchemeAAAName_Type()
)
hh3cDomainSchemeAAAName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainSchemeAAAName.setStatus("current")
_Hh3cDomainSchemeAccessMode_Type = Hh3cAccessModeofDomainScheme
_Hh3cDomainSchemeAccessMode_Object = MibTableColumn
hh3cDomainSchemeAccessMode = _Hh3cDomainSchemeAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 2, 1, 8),
    _Hh3cDomainSchemeAccessMode_Type()
)
hh3cDomainSchemeAccessMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainSchemeAccessMode.setStatus("current")
_Hh3cDomainIpPoolTable_Object = MibTable
hh3cDomainIpPoolTable = _Hh3cDomainIpPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cDomainIpPoolTable.setStatus("current")
_Hh3cDomainIpPoolEntry_Object = MibTableRow
hh3cDomainIpPoolEntry = _Hh3cDomainIpPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 3, 1)
)
hh3cDomainIpPoolEntry.setIndexNames(
    (0, "HH3C-DOMAIN-MIB", "hh3cDomainName"),
    (0, "HH3C-DOMAIN-MIB", "hh3cDomainIpPoolNum"),
)
if mibBuilder.loadTexts:
    hh3cDomainIpPoolEntry.setStatus("current")


class _Hh3cDomainIpPoolNum_Type(Integer32):
    """Custom type hh3cDomainIpPoolNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_Hh3cDomainIpPoolNum_Type.__name__ = "Integer32"
_Hh3cDomainIpPoolNum_Object = MibTableColumn
hh3cDomainIpPoolNum = _Hh3cDomainIpPoolNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 3, 1, 1),
    _Hh3cDomainIpPoolNum_Type()
)
hh3cDomainIpPoolNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDomainIpPoolNum.setStatus("current")
_Hh3cDomainIpPoolLowIpAddrType_Type = InetAddressType
_Hh3cDomainIpPoolLowIpAddrType_Object = MibTableColumn
hh3cDomainIpPoolLowIpAddrType = _Hh3cDomainIpPoolLowIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 3, 1, 2),
    _Hh3cDomainIpPoolLowIpAddrType_Type()
)
hh3cDomainIpPoolLowIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainIpPoolLowIpAddrType.setStatus("current")
_Hh3cDomainIpPoolLowIpAddr_Type = InetAddress
_Hh3cDomainIpPoolLowIpAddr_Object = MibTableColumn
hh3cDomainIpPoolLowIpAddr = _Hh3cDomainIpPoolLowIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 3, 1, 3),
    _Hh3cDomainIpPoolLowIpAddr_Type()
)
hh3cDomainIpPoolLowIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainIpPoolLowIpAddr.setStatus("current")
_Hh3cDomainIpPoolLen_Type = Integer32
_Hh3cDomainIpPoolLen_Object = MibTableColumn
hh3cDomainIpPoolLen = _Hh3cDomainIpPoolLen_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 3, 1, 4),
    _Hh3cDomainIpPoolLen_Type()
)
hh3cDomainIpPoolLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainIpPoolLen.setStatus("current")
_Hh3cDomainIpPoolRowStatus_Type = RowStatus
_Hh3cDomainIpPoolRowStatus_Object = MibTableColumn
hh3cDomainIpPoolRowStatus = _Hh3cDomainIpPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 3, 1, 5),
    _Hh3cDomainIpPoolRowStatus_Type()
)
hh3cDomainIpPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainIpPoolRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-DOMAIN-MIB",
    **{"Hh3cModeOfDomainScheme": Hh3cModeOfDomainScheme,
       "Hh3cAAATypeDomainScheme": Hh3cAAATypeDomainScheme,
       "Hh3cAccessModeofDomainScheme": Hh3cAccessModeofDomainScheme,
       "hh3cDomain": hh3cDomain,
       "hh3cDomainControl": hh3cDomainControl,
       "hh3cDomainDefault": hh3cDomainDefault,
       "hh3cDomainTables": hh3cDomainTables,
       "hh3cDomainInfoTable": hh3cDomainInfoTable,
       "hh3cDomainInfoEntry": hh3cDomainInfoEntry,
       "hh3cDomainName": hh3cDomainName,
       "hh3cDomainState": hh3cDomainState,
       "hh3cDomainMaxAccessNum": hh3cDomainMaxAccessNum,
       "hh3cDomainVlanAssignMode": hh3cDomainVlanAssignMode,
       "hh3cDomainIdleCutEnable": hh3cDomainIdleCutEnable,
       "hh3cDomainIdleCutMaxTime": hh3cDomainIdleCutMaxTime,
       "hh3cDomainIdleCutMinFlow": hh3cDomainIdleCutMinFlow,
       "hh3cDomainMessengerEnable": hh3cDomainMessengerEnable,
       "hh3cDomainMessengerLimitTime": hh3cDomainMessengerLimitTime,
       "hh3cDomainMessengerSpanTime": hh3cDomainMessengerSpanTime,
       "hh3cDomainSelfServiceEnable": hh3cDomainSelfServiceEnable,
       "hh3cDomainSelfServiceURL": hh3cDomainSelfServiceURL,
       "hh3cDomainAccFailureAction": hh3cDomainAccFailureAction,
       "hh3cDomainRowStatus": hh3cDomainRowStatus,
       "hh3cDomainCurrentAccessNum": hh3cDomainCurrentAccessNum,
       "hh3cDomainSchemeTable": hh3cDomainSchemeTable,
       "hh3cDomainSchemeEntry": hh3cDomainSchemeEntry,
       "hh3cDomainSchemeIndex": hh3cDomainSchemeIndex,
       "hh3cDomainSchemeMode": hh3cDomainSchemeMode,
       "hh3cDomainAuthSchemeName": hh3cDomainAuthSchemeName,
       "hh3cDomainAcctSchemeName": hh3cDomainAcctSchemeName,
       "hh3cDomainSchemeRowStatus": hh3cDomainSchemeRowStatus,
       "hh3cDomainSchemeAAAType": hh3cDomainSchemeAAAType,
       "hh3cDomainSchemeAAAName": hh3cDomainSchemeAAAName,
       "hh3cDomainSchemeAccessMode": hh3cDomainSchemeAccessMode,
       "hh3cDomainIpPoolTable": hh3cDomainIpPoolTable,
       "hh3cDomainIpPoolEntry": hh3cDomainIpPoolEntry,
       "hh3cDomainIpPoolNum": hh3cDomainIpPoolNum,
       "hh3cDomainIpPoolLowIpAddrType": hh3cDomainIpPoolLowIpAddrType,
       "hh3cDomainIpPoolLowIpAddr": hh3cDomainIpPoolLowIpAddr,
       "hh3cDomainIpPoolLen": hh3cDomainIpPoolLen,
       "hh3cDomainIpPoolRowStatus": hh3cDomainIpPoolRowStatus}
)
