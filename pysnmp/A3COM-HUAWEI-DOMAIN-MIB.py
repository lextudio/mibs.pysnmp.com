# SNMP MIB module (A3COM-HUAWEI-DOMAIN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-DOMAIN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:27:35 2024
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

h3cDomain = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 46)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class H3cModeOfDomainScheme(Integer32, TextualConvention):
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



class H3cAAATypeDomainScheme(Integer32, TextualConvention):
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



class H3cAccessModeofDomainScheme(Integer32, TextualConvention):
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

_H3cDomainControl_ObjectIdentity = ObjectIdentity
h3cDomainControl = _H3cDomainControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 46, 1)
)


class _H3cDomainDefault_Type(OctetString):
    """Custom type h3cDomainDefault based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_H3cDomainDefault_Type.__name__ = "OctetString"
_H3cDomainDefault_Object = MibScalar
h3cDomainDefault = _H3cDomainDefault_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 46, 1, 1),
    _H3cDomainDefault_Type()
)
h3cDomainDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDomainDefault.setStatus("current")
_H3cDomainTables_ObjectIdentity = ObjectIdentity
h3cDomainTables = _H3cDomainTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 46, 2)
)
_H3cDomainInfoTable_Object = MibTable
h3cDomainInfoTable = _H3cDomainInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 46, 2, 1)
)
if mibBuilder.loadTexts:
    h3cDomainInfoTable.setStatus("current")
_H3cDomainInfoEntry_Object = MibTableRow
h3cDomainInfoEntry = _H3cDomainInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 46, 2, 1, 1)
)
h3cDomainInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOMAIN-MIB", "h3cDomainName"),
)
if mibBuilder.loadTexts:
    h3cDomainInfoEntry.setStatus("current")


class _H3cDomainName_Type(OctetString):
    """Custom type h3cDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_H3cDomainName_Type.__name__ = "OctetString"
_H3cDomainName_Object = MibTableColumn
h3cDomainName = _H3cDomainName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 46, 2, 1, 1, 1),
    _H3cDomainName_Type()
)
h3cDomainName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDomainName.setStatus("current")


class _H3cDomainState_Type(Integer32):
    """Custom type h3cDomainState based on Integer32"""
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


_H3cDomainState_Type.__name__ = "Integer32"
_H3cDomainState_Object = MibTableColumn
h3cDomainState = _H3cDomainState_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 46, 2, 1, 1, 2),
    _H3cDomainState_Type()
)
h3cDomainState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainState.setStatus("current")
_H3cDomainMaxAccessNum_Type = Integer32
_H3cDomainMaxAccessNum_Object = MibTableColumn
h3cDomainMaxAccessNum = _H3cDomainMaxAccessNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 46, 2, 1, 1, 3),
    _H3cDomainMaxAccessNum_Type()
)
h3cDomainMaxAccessNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainMaxAccessNum.setStatus("current")


class _H3cDomainVlanAssignMode_Type(Integer32):
    """Custom type h3cDomainVlanAssignMode based on Integer32"""
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


_H3cDomainVlanAssignMode_Type.__name__ = "Integer32"
_H3cDomainVlanAssignMode_Object = MibTableColumn
h3cDomainVlanAssignMode = _H3cDomainVlanAssignMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 46, 2, 1, 1, 4),
    _H3cDomainVlanAssignMode_Type()
)
h3cDomainVlanAssignMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainVlanAssignMode.setStatus("current")
_H3cDomainIdleCutEnable_Type = TruthValue
_H3cDomainIdleCutEnable_Object = MibTableColumn
h3cDomainIdleCutEnable = _H3cDomainIdleCutEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 46, 2, 1, 1, 5),
    _H3cDomainIdleCutEnable_Type()
)
h3cDomainIdleCutEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainIdleCutEnable.setStatus("current")


class _H3cDomainIdleCutMaxTime_Type(Integer32):
    """Custom type h3cDomainIdleCutMaxTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_H3cDomainIdleCutMaxTime_Type.__name__ = "Integer32"
_H3cDomainIdleCutMaxTime_Object = MibTableColumn
h3cDomainIdleCutMaxTime = _H3cDomainIdleCutMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 46, 2, 1, 1, 6),
    _H3cDomainIdleCutMaxTime_Type()
)
h3cDomainIdleCutMaxTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainIdleCutMaxTime.setStatus("current")


class _H3cDomainIdleCutMinFlow_Type(Integer32):
    """Custom type h3cDomainIdleCutMinFlow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10240000),
    )


_H3cDomainIdleCutMinFlow_Type.__name__ = "Integer32"
_H3cDomainIdleCutMinFlow_Object = MibTableColumn
h3cDomainIdleCutMinFlow = _H3cDomainIdleCutMinFlow_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 46, 2, 1, 1, 7),
    _H3cDomainIdleCutMinFlow_Type()
)
h3cDomainIdleCutMinFlow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainIdleCutMinFlow.setStatus("current")
_H3cDomainMessengerEnable_Type = TruthValue
_H3cDomainMessengerEnable_Object = MibTableColumn
h3cDomainMessengerEnable = _H3cDomainMessengerEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 46, 2, 1, 1, 8),
    _H3cDomainMessengerEnable_Type()
)
h3cDomainMessengerEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainMessengerEnable.setStatus("current")


class _H3cDomainMessengerLimitTime_Type(Integer32):
    """Custom type h3cDomainMessengerLimitTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_H3cDomainMessengerLimitTime_Type.__name__ = "Integer32"
_H3cDomainMessengerLimitTime_Object = MibTableColumn
h3cDomainMessengerLimitTime = _H3cDomainMessengerLimitTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 46, 2, 1, 1, 9),
    _H3cDomainMessengerLimitTime_Type()
)
h3cDomainMessengerLimitTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainMessengerLimitTime.setStatus("current")


class _H3cDomainMessengerSpanTime_Type(Integer32):
    """Custom type h3cDomainMessengerSpanTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_H3cDomainMessengerSpanTime_Type.__name__ = "Integer32"
_H3cDomainMessengerSpanTime_Object = MibTableColumn
h3cDomainMessengerSpanTime = _H3cDomainMessengerSpanTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 46, 2, 1, 1, 10),
    _H3cDomainMessengerSpanTime_Type()
)
h3cDomainMessengerSpanTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainMessengerSpanTime.setStatus("current")
_H3cDomainSelfServiceEnable_Type = TruthValue
_H3cDomainSelfServiceEnable_Object = MibTableColumn
h3cDomainSelfServiceEnable = _H3cDomainSelfServiceEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 46, 2, 1, 1, 11),
    _H3cDomainSelfServiceEnable_Type()
)
h3cDomainSelfServiceEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainSelfServiceEnable.setStatus("current")


class _H3cDomainSelfServiceURL_Type(OctetString):
    """Custom type h3cDomainSelfServiceURL based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_H3cDomainSelfServiceURL_Type.__name__ = "OctetString"
_H3cDomainSelfServiceURL_Object = MibTableColumn
h3cDomainSelfServiceURL = _H3cDomainSelfServiceURL_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 46, 2, 1, 1, 12),
    _H3cDomainSelfServiceURL_Type()
)
h3cDomainSelfServiceURL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainSelfServiceURL.setStatus("current")


class _H3cDomainAccFailureAction_Type(Integer32):
    """Custom type h3cDomainAccFailureAction based on Integer32"""
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


_H3cDomainAccFailureAction_Type.__name__ = "Integer32"
_H3cDomainAccFailureAction_Object = MibTableColumn
h3cDomainAccFailureAction = _H3cDomainAccFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 46, 2, 1, 1, 13),
    _H3cDomainAccFailureAction_Type()
)
h3cDomainAccFailureAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainAccFailureAction.setStatus("current")
_H3cDomainRowStatus_Type = RowStatus
_H3cDomainRowStatus_Object = MibTableColumn
h3cDomainRowStatus = _H3cDomainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 46, 2, 1, 1, 14),
    _H3cDomainRowStatus_Type()
)
h3cDomainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainRowStatus.setStatus("current")
_H3cDomainCurrentAccessNum_Type = Integer32
_H3cDomainCurrentAccessNum_Object = MibTableColumn
h3cDomainCurrentAccessNum = _H3cDomainCurrentAccessNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 46, 2, 1, 1, 15),
    _H3cDomainCurrentAccessNum_Type()
)
h3cDomainCurrentAccessNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDomainCurrentAccessNum.setStatus("current")
_H3cDomainSchemeTable_Object = MibTable
h3cDomainSchemeTable = _H3cDomainSchemeTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 46, 2, 2)
)
if mibBuilder.loadTexts:
    h3cDomainSchemeTable.setStatus("current")
_H3cDomainSchemeEntry_Object = MibTableRow
h3cDomainSchemeEntry = _H3cDomainSchemeEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 46, 2, 2, 1)
)
h3cDomainSchemeEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOMAIN-MIB", "h3cDomainName"),
    (0, "A3COM-HUAWEI-DOMAIN-MIB", "h3cDomainSchemeIndex"),
)
if mibBuilder.loadTexts:
    h3cDomainSchemeEntry.setStatus("current")
_H3cDomainSchemeIndex_Type = Integer32
_H3cDomainSchemeIndex_Object = MibTableColumn
h3cDomainSchemeIndex = _H3cDomainSchemeIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 46, 2, 2, 1, 1),
    _H3cDomainSchemeIndex_Type()
)
h3cDomainSchemeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDomainSchemeIndex.setStatus("current")
_H3cDomainSchemeMode_Type = H3cModeOfDomainScheme
_H3cDomainSchemeMode_Object = MibTableColumn
h3cDomainSchemeMode = _H3cDomainSchemeMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 46, 2, 2, 1, 2),
    _H3cDomainSchemeMode_Type()
)
h3cDomainSchemeMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainSchemeMode.setStatus("current")


class _H3cDomainAuthSchemeName_Type(OctetString):
    """Custom type h3cDomainAuthSchemeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cDomainAuthSchemeName_Type.__name__ = "OctetString"
_H3cDomainAuthSchemeName_Object = MibTableColumn
h3cDomainAuthSchemeName = _H3cDomainAuthSchemeName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 46, 2, 2, 1, 3),
    _H3cDomainAuthSchemeName_Type()
)
h3cDomainAuthSchemeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainAuthSchemeName.setStatus("current")


class _H3cDomainAcctSchemeName_Type(OctetString):
    """Custom type h3cDomainAcctSchemeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cDomainAcctSchemeName_Type.__name__ = "OctetString"
_H3cDomainAcctSchemeName_Object = MibTableColumn
h3cDomainAcctSchemeName = _H3cDomainAcctSchemeName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 46, 2, 2, 1, 4),
    _H3cDomainAcctSchemeName_Type()
)
h3cDomainAcctSchemeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainAcctSchemeName.setStatus("current")
_H3cDomainSchemeRowStatus_Type = RowStatus
_H3cDomainSchemeRowStatus_Object = MibTableColumn
h3cDomainSchemeRowStatus = _H3cDomainSchemeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 46, 2, 2, 1, 5),
    _H3cDomainSchemeRowStatus_Type()
)
h3cDomainSchemeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainSchemeRowStatus.setStatus("current")
_H3cDomainSchemeAAAType_Type = H3cAAATypeDomainScheme
_H3cDomainSchemeAAAType_Object = MibTableColumn
h3cDomainSchemeAAAType = _H3cDomainSchemeAAAType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 46, 2, 2, 1, 6),
    _H3cDomainSchemeAAAType_Type()
)
h3cDomainSchemeAAAType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainSchemeAAAType.setStatus("current")


class _H3cDomainSchemeAAAName_Type(OctetString):
    """Custom type h3cDomainSchemeAAAName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cDomainSchemeAAAName_Type.__name__ = "OctetString"
_H3cDomainSchemeAAAName_Object = MibTableColumn
h3cDomainSchemeAAAName = _H3cDomainSchemeAAAName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 46, 2, 2, 1, 7),
    _H3cDomainSchemeAAAName_Type()
)
h3cDomainSchemeAAAName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainSchemeAAAName.setStatus("current")
_H3cDomainSchemeAccessMode_Type = H3cAccessModeofDomainScheme
_H3cDomainSchemeAccessMode_Object = MibTableColumn
h3cDomainSchemeAccessMode = _H3cDomainSchemeAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 46, 2, 2, 1, 8),
    _H3cDomainSchemeAccessMode_Type()
)
h3cDomainSchemeAccessMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainSchemeAccessMode.setStatus("current")
_H3cDomainIpPoolTable_Object = MibTable
h3cDomainIpPoolTable = _H3cDomainIpPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 46, 2, 3)
)
if mibBuilder.loadTexts:
    h3cDomainIpPoolTable.setStatus("current")
_H3cDomainIpPoolEntry_Object = MibTableRow
h3cDomainIpPoolEntry = _H3cDomainIpPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 46, 2, 3, 1)
)
h3cDomainIpPoolEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOMAIN-MIB", "h3cDomainName"),
    (0, "A3COM-HUAWEI-DOMAIN-MIB", "h3cDomainIpPoolNum"),
)
if mibBuilder.loadTexts:
    h3cDomainIpPoolEntry.setStatus("current")


class _H3cDomainIpPoolNum_Type(Integer32):
    """Custom type h3cDomainIpPoolNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_H3cDomainIpPoolNum_Type.__name__ = "Integer32"
_H3cDomainIpPoolNum_Object = MibTableColumn
h3cDomainIpPoolNum = _H3cDomainIpPoolNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 46, 2, 3, 1, 1),
    _H3cDomainIpPoolNum_Type()
)
h3cDomainIpPoolNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDomainIpPoolNum.setStatus("current")
_H3cDomainIpPoolLowIpAddrType_Type = InetAddressType
_H3cDomainIpPoolLowIpAddrType_Object = MibTableColumn
h3cDomainIpPoolLowIpAddrType = _H3cDomainIpPoolLowIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 46, 2, 3, 1, 2),
    _H3cDomainIpPoolLowIpAddrType_Type()
)
h3cDomainIpPoolLowIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainIpPoolLowIpAddrType.setStatus("current")
_H3cDomainIpPoolLowIpAddr_Type = InetAddress
_H3cDomainIpPoolLowIpAddr_Object = MibTableColumn
h3cDomainIpPoolLowIpAddr = _H3cDomainIpPoolLowIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 46, 2, 3, 1, 3),
    _H3cDomainIpPoolLowIpAddr_Type()
)
h3cDomainIpPoolLowIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainIpPoolLowIpAddr.setStatus("current")
_H3cDomainIpPoolLen_Type = Integer32
_H3cDomainIpPoolLen_Object = MibTableColumn
h3cDomainIpPoolLen = _H3cDomainIpPoolLen_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 46, 2, 3, 1, 4),
    _H3cDomainIpPoolLen_Type()
)
h3cDomainIpPoolLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainIpPoolLen.setStatus("current")
_H3cDomainIpPoolRowStatus_Type = RowStatus
_H3cDomainIpPoolRowStatus_Object = MibTableColumn
h3cDomainIpPoolRowStatus = _H3cDomainIpPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 46, 2, 3, 1, 5),
    _H3cDomainIpPoolRowStatus_Type()
)
h3cDomainIpPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainIpPoolRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-DOMAIN-MIB",
    **{"H3cModeOfDomainScheme": H3cModeOfDomainScheme,
       "H3cAAATypeDomainScheme": H3cAAATypeDomainScheme,
       "H3cAccessModeofDomainScheme": H3cAccessModeofDomainScheme,
       "h3cDomain": h3cDomain,
       "h3cDomainControl": h3cDomainControl,
       "h3cDomainDefault": h3cDomainDefault,
       "h3cDomainTables": h3cDomainTables,
       "h3cDomainInfoTable": h3cDomainInfoTable,
       "h3cDomainInfoEntry": h3cDomainInfoEntry,
       "h3cDomainName": h3cDomainName,
       "h3cDomainState": h3cDomainState,
       "h3cDomainMaxAccessNum": h3cDomainMaxAccessNum,
       "h3cDomainVlanAssignMode": h3cDomainVlanAssignMode,
       "h3cDomainIdleCutEnable": h3cDomainIdleCutEnable,
       "h3cDomainIdleCutMaxTime": h3cDomainIdleCutMaxTime,
       "h3cDomainIdleCutMinFlow": h3cDomainIdleCutMinFlow,
       "h3cDomainMessengerEnable": h3cDomainMessengerEnable,
       "h3cDomainMessengerLimitTime": h3cDomainMessengerLimitTime,
       "h3cDomainMessengerSpanTime": h3cDomainMessengerSpanTime,
       "h3cDomainSelfServiceEnable": h3cDomainSelfServiceEnable,
       "h3cDomainSelfServiceURL": h3cDomainSelfServiceURL,
       "h3cDomainAccFailureAction": h3cDomainAccFailureAction,
       "h3cDomainRowStatus": h3cDomainRowStatus,
       "h3cDomainCurrentAccessNum": h3cDomainCurrentAccessNum,
       "h3cDomainSchemeTable": h3cDomainSchemeTable,
       "h3cDomainSchemeEntry": h3cDomainSchemeEntry,
       "h3cDomainSchemeIndex": h3cDomainSchemeIndex,
       "h3cDomainSchemeMode": h3cDomainSchemeMode,
       "h3cDomainAuthSchemeName": h3cDomainAuthSchemeName,
       "h3cDomainAcctSchemeName": h3cDomainAcctSchemeName,
       "h3cDomainSchemeRowStatus": h3cDomainSchemeRowStatus,
       "h3cDomainSchemeAAAType": h3cDomainSchemeAAAType,
       "h3cDomainSchemeAAAName": h3cDomainSchemeAAAName,
       "h3cDomainSchemeAccessMode": h3cDomainSchemeAccessMode,
       "h3cDomainIpPoolTable": h3cDomainIpPoolTable,
       "h3cDomainIpPoolEntry": h3cDomainIpPoolEntry,
       "h3cDomainIpPoolNum": h3cDomainIpPoolNum,
       "h3cDomainIpPoolLowIpAddrType": h3cDomainIpPoolLowIpAddrType,
       "h3cDomainIpPoolLowIpAddr": h3cDomainIpPoolLowIpAddr,
       "h3cDomainIpPoolLen": h3cDomainIpPoolLen,
       "h3cDomainIpPoolRowStatus": h3cDomainIpPoolRowStatus}
)
