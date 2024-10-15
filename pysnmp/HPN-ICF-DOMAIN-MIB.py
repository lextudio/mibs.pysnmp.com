# SNMP MIB module (HPN-ICF-DOMAIN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-DOMAIN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:47 2024
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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpnicfDomain = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 46)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpnicfModeOfDomainScheme(Integer32, TextualConvention):
    status = "current"
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
        *(("ldap", 5),
          ("local", 2),
          ("none", 1),
          ("radius", 3),
          ("tacacs", 4))
    )



class HpnicfAAATypeDomainScheme(Integer32, TextualConvention):
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



class HpnicfAccessModeofDomainScheme(Integer32, TextualConvention):
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
          ("reserved", 12),
          ("superauthen", 10),
          ("voice", 9))
    )



# MIB Managed Objects in the order of their OIDs

_HpnicfDomainControl_ObjectIdentity = ObjectIdentity
hpnicfDomainControl = _HpnicfDomainControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 46, 1)
)


class _HpnicfDomainDefault_Type(OctetString):
    """Custom type hpnicfDomainDefault based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HpnicfDomainDefault_Type.__name__ = "OctetString"
_HpnicfDomainDefault_Object = MibScalar
hpnicfDomainDefault = _HpnicfDomainDefault_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 46, 1, 1),
    _HpnicfDomainDefault_Type()
)
hpnicfDomainDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDomainDefault.setStatus("current")
_HpnicfDomainTables_ObjectIdentity = ObjectIdentity
hpnicfDomainTables = _HpnicfDomainTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 46, 2)
)
_HpnicfDomainInfoTable_Object = MibTable
hpnicfDomainInfoTable = _HpnicfDomainInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 46, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfDomainInfoTable.setStatus("current")
_HpnicfDomainInfoEntry_Object = MibTableRow
hpnicfDomainInfoEntry = _HpnicfDomainInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 46, 2, 1, 1)
)
hpnicfDomainInfoEntry.setIndexNames(
    (0, "HPN-ICF-DOMAIN-MIB", "hpnicfDomainName"),
)
if mibBuilder.loadTexts:
    hpnicfDomainInfoEntry.setStatus("current")


class _HpnicfDomainName_Type(OctetString):
    """Custom type hpnicfDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HpnicfDomainName_Type.__name__ = "OctetString"
_HpnicfDomainName_Object = MibTableColumn
hpnicfDomainName = _HpnicfDomainName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 46, 2, 1, 1, 1),
    _HpnicfDomainName_Type()
)
hpnicfDomainName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDomainName.setStatus("current")


class _HpnicfDomainState_Type(Integer32):
    """Custom type hpnicfDomainState based on Integer32"""
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


_HpnicfDomainState_Type.__name__ = "Integer32"
_HpnicfDomainState_Object = MibTableColumn
hpnicfDomainState = _HpnicfDomainState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 46, 2, 1, 1, 2),
    _HpnicfDomainState_Type()
)
hpnicfDomainState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDomainState.setStatus("current")
_HpnicfDomainMaxAccessNum_Type = Integer32
_HpnicfDomainMaxAccessNum_Object = MibTableColumn
hpnicfDomainMaxAccessNum = _HpnicfDomainMaxAccessNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 46, 2, 1, 1, 3),
    _HpnicfDomainMaxAccessNum_Type()
)
hpnicfDomainMaxAccessNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDomainMaxAccessNum.setStatus("current")


class _HpnicfDomainVlanAssignMode_Type(Integer32):
    """Custom type hpnicfDomainVlanAssignMode based on Integer32"""
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


_HpnicfDomainVlanAssignMode_Type.__name__ = "Integer32"
_HpnicfDomainVlanAssignMode_Object = MibTableColumn
hpnicfDomainVlanAssignMode = _HpnicfDomainVlanAssignMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 46, 2, 1, 1, 4),
    _HpnicfDomainVlanAssignMode_Type()
)
hpnicfDomainVlanAssignMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDomainVlanAssignMode.setStatus("current")
_HpnicfDomainIdleCutEnable_Type = TruthValue
_HpnicfDomainIdleCutEnable_Object = MibTableColumn
hpnicfDomainIdleCutEnable = _HpnicfDomainIdleCutEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 46, 2, 1, 1, 5),
    _HpnicfDomainIdleCutEnable_Type()
)
hpnicfDomainIdleCutEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDomainIdleCutEnable.setStatus("current")
_HpnicfDomainIdleCutMaxTime_Type = Integer32
_HpnicfDomainIdleCutMaxTime_Object = MibTableColumn
hpnicfDomainIdleCutMaxTime = _HpnicfDomainIdleCutMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 46, 2, 1, 1, 6),
    _HpnicfDomainIdleCutMaxTime_Type()
)
hpnicfDomainIdleCutMaxTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDomainIdleCutMaxTime.setStatus("current")


class _HpnicfDomainIdleCutMinFlow_Type(Integer32):
    """Custom type hpnicfDomainIdleCutMinFlow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10240000),
    )


_HpnicfDomainIdleCutMinFlow_Type.__name__ = "Integer32"
_HpnicfDomainIdleCutMinFlow_Object = MibTableColumn
hpnicfDomainIdleCutMinFlow = _HpnicfDomainIdleCutMinFlow_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 46, 2, 1, 1, 7),
    _HpnicfDomainIdleCutMinFlow_Type()
)
hpnicfDomainIdleCutMinFlow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDomainIdleCutMinFlow.setStatus("current")
_HpnicfDomainMessengerEnable_Type = TruthValue
_HpnicfDomainMessengerEnable_Object = MibTableColumn
hpnicfDomainMessengerEnable = _HpnicfDomainMessengerEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 46, 2, 1, 1, 8),
    _HpnicfDomainMessengerEnable_Type()
)
hpnicfDomainMessengerEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDomainMessengerEnable.setStatus("current")


class _HpnicfDomainMessengerLimitTime_Type(Integer32):
    """Custom type hpnicfDomainMessengerLimitTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_HpnicfDomainMessengerLimitTime_Type.__name__ = "Integer32"
_HpnicfDomainMessengerLimitTime_Object = MibTableColumn
hpnicfDomainMessengerLimitTime = _HpnicfDomainMessengerLimitTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 46, 2, 1, 1, 9),
    _HpnicfDomainMessengerLimitTime_Type()
)
hpnicfDomainMessengerLimitTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDomainMessengerLimitTime.setStatus("current")


class _HpnicfDomainMessengerSpanTime_Type(Integer32):
    """Custom type hpnicfDomainMessengerSpanTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_HpnicfDomainMessengerSpanTime_Type.__name__ = "Integer32"
_HpnicfDomainMessengerSpanTime_Object = MibTableColumn
hpnicfDomainMessengerSpanTime = _HpnicfDomainMessengerSpanTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 46, 2, 1, 1, 10),
    _HpnicfDomainMessengerSpanTime_Type()
)
hpnicfDomainMessengerSpanTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDomainMessengerSpanTime.setStatus("current")
_HpnicfDomainSelfServiceEnable_Type = TruthValue
_HpnicfDomainSelfServiceEnable_Object = MibTableColumn
hpnicfDomainSelfServiceEnable = _HpnicfDomainSelfServiceEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 46, 2, 1, 1, 11),
    _HpnicfDomainSelfServiceEnable_Type()
)
hpnicfDomainSelfServiceEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDomainSelfServiceEnable.setStatus("current")


class _HpnicfDomainSelfServiceURL_Type(OctetString):
    """Custom type hpnicfDomainSelfServiceURL based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HpnicfDomainSelfServiceURL_Type.__name__ = "OctetString"
_HpnicfDomainSelfServiceURL_Object = MibTableColumn
hpnicfDomainSelfServiceURL = _HpnicfDomainSelfServiceURL_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 46, 2, 1, 1, 12),
    _HpnicfDomainSelfServiceURL_Type()
)
hpnicfDomainSelfServiceURL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDomainSelfServiceURL.setStatus("current")


class _HpnicfDomainAccFailureAction_Type(Integer32):
    """Custom type hpnicfDomainAccFailureAction based on Integer32"""
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


_HpnicfDomainAccFailureAction_Type.__name__ = "Integer32"
_HpnicfDomainAccFailureAction_Object = MibTableColumn
hpnicfDomainAccFailureAction = _HpnicfDomainAccFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 46, 2, 1, 1, 13),
    _HpnicfDomainAccFailureAction_Type()
)
hpnicfDomainAccFailureAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDomainAccFailureAction.setStatus("current")
_HpnicfDomainRowStatus_Type = RowStatus
_HpnicfDomainRowStatus_Object = MibTableColumn
hpnicfDomainRowStatus = _HpnicfDomainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 46, 2, 1, 1, 14),
    _HpnicfDomainRowStatus_Type()
)
hpnicfDomainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDomainRowStatus.setStatus("current")
_HpnicfDomainCurrentAccessNum_Type = Integer32
_HpnicfDomainCurrentAccessNum_Object = MibTableColumn
hpnicfDomainCurrentAccessNum = _HpnicfDomainCurrentAccessNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 46, 2, 1, 1, 15),
    _HpnicfDomainCurrentAccessNum_Type()
)
hpnicfDomainCurrentAccessNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDomainCurrentAccessNum.setStatus("current")
_HpnicfDomainIdleCutTime_Type = TimeTicks
_HpnicfDomainIdleCutTime_Object = MibTableColumn
hpnicfDomainIdleCutTime = _HpnicfDomainIdleCutTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 46, 2, 1, 1, 16),
    _HpnicfDomainIdleCutTime_Type()
)
hpnicfDomainIdleCutTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDomainIdleCutTime.setStatus("current")
_HpnicfDomainSchemeTable_Object = MibTable
hpnicfDomainSchemeTable = _HpnicfDomainSchemeTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 46, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfDomainSchemeTable.setStatus("current")
_HpnicfDomainSchemeEntry_Object = MibTableRow
hpnicfDomainSchemeEntry = _HpnicfDomainSchemeEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 46, 2, 2, 1)
)
hpnicfDomainSchemeEntry.setIndexNames(
    (0, "HPN-ICF-DOMAIN-MIB", "hpnicfDomainName"),
    (0, "HPN-ICF-DOMAIN-MIB", "hpnicfDomainSchemeIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDomainSchemeEntry.setStatus("current")
_HpnicfDomainSchemeIndex_Type = Integer32
_HpnicfDomainSchemeIndex_Object = MibTableColumn
hpnicfDomainSchemeIndex = _HpnicfDomainSchemeIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 46, 2, 2, 1, 1),
    _HpnicfDomainSchemeIndex_Type()
)
hpnicfDomainSchemeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDomainSchemeIndex.setStatus("current")
_HpnicfDomainSchemeMode_Type = HpnicfModeOfDomainScheme
_HpnicfDomainSchemeMode_Object = MibTableColumn
hpnicfDomainSchemeMode = _HpnicfDomainSchemeMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 46, 2, 2, 1, 2),
    _HpnicfDomainSchemeMode_Type()
)
hpnicfDomainSchemeMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDomainSchemeMode.setStatus("current")


class _HpnicfDomainAuthSchemeName_Type(OctetString):
    """Custom type hpnicfDomainAuthSchemeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfDomainAuthSchemeName_Type.__name__ = "OctetString"
_HpnicfDomainAuthSchemeName_Object = MibTableColumn
hpnicfDomainAuthSchemeName = _HpnicfDomainAuthSchemeName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 46, 2, 2, 1, 3),
    _HpnicfDomainAuthSchemeName_Type()
)
hpnicfDomainAuthSchemeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDomainAuthSchemeName.setStatus("current")


class _HpnicfDomainAcctSchemeName_Type(OctetString):
    """Custom type hpnicfDomainAcctSchemeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfDomainAcctSchemeName_Type.__name__ = "OctetString"
_HpnicfDomainAcctSchemeName_Object = MibTableColumn
hpnicfDomainAcctSchemeName = _HpnicfDomainAcctSchemeName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 46, 2, 2, 1, 4),
    _HpnicfDomainAcctSchemeName_Type()
)
hpnicfDomainAcctSchemeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDomainAcctSchemeName.setStatus("current")
_HpnicfDomainSchemeRowStatus_Type = RowStatus
_HpnicfDomainSchemeRowStatus_Object = MibTableColumn
hpnicfDomainSchemeRowStatus = _HpnicfDomainSchemeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 46, 2, 2, 1, 5),
    _HpnicfDomainSchemeRowStatus_Type()
)
hpnicfDomainSchemeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDomainSchemeRowStatus.setStatus("current")
_HpnicfDomainSchemeAAAType_Type = HpnicfAAATypeDomainScheme
_HpnicfDomainSchemeAAAType_Object = MibTableColumn
hpnicfDomainSchemeAAAType = _HpnicfDomainSchemeAAAType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 46, 2, 2, 1, 6),
    _HpnicfDomainSchemeAAAType_Type()
)
hpnicfDomainSchemeAAAType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDomainSchemeAAAType.setStatus("current")


class _HpnicfDomainSchemeAAAName_Type(OctetString):
    """Custom type hpnicfDomainSchemeAAAName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfDomainSchemeAAAName_Type.__name__ = "OctetString"
_HpnicfDomainSchemeAAAName_Object = MibTableColumn
hpnicfDomainSchemeAAAName = _HpnicfDomainSchemeAAAName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 46, 2, 2, 1, 7),
    _HpnicfDomainSchemeAAAName_Type()
)
hpnicfDomainSchemeAAAName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDomainSchemeAAAName.setStatus("current")
_HpnicfDomainSchemeAccessMode_Type = HpnicfAccessModeofDomainScheme
_HpnicfDomainSchemeAccessMode_Object = MibTableColumn
hpnicfDomainSchemeAccessMode = _HpnicfDomainSchemeAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 46, 2, 2, 1, 8),
    _HpnicfDomainSchemeAccessMode_Type()
)
hpnicfDomainSchemeAccessMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDomainSchemeAccessMode.setStatus("current")
_HpnicfDomainIpPoolTable_Object = MibTable
hpnicfDomainIpPoolTable = _HpnicfDomainIpPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 46, 2, 3)
)
if mibBuilder.loadTexts:
    hpnicfDomainIpPoolTable.setStatus("current")
_HpnicfDomainIpPoolEntry_Object = MibTableRow
hpnicfDomainIpPoolEntry = _HpnicfDomainIpPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 46, 2, 3, 1)
)
hpnicfDomainIpPoolEntry.setIndexNames(
    (0, "HPN-ICF-DOMAIN-MIB", "hpnicfDomainName"),
    (0, "HPN-ICF-DOMAIN-MIB", "hpnicfDomainIpPoolNum"),
)
if mibBuilder.loadTexts:
    hpnicfDomainIpPoolEntry.setStatus("current")


class _HpnicfDomainIpPoolNum_Type(Integer32):
    """Custom type hpnicfDomainIpPoolNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_HpnicfDomainIpPoolNum_Type.__name__ = "Integer32"
_HpnicfDomainIpPoolNum_Object = MibTableColumn
hpnicfDomainIpPoolNum = _HpnicfDomainIpPoolNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 46, 2, 3, 1, 1),
    _HpnicfDomainIpPoolNum_Type()
)
hpnicfDomainIpPoolNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDomainIpPoolNum.setStatus("current")
_HpnicfDomainIpPoolLowIpAddrType_Type = InetAddressType
_HpnicfDomainIpPoolLowIpAddrType_Object = MibTableColumn
hpnicfDomainIpPoolLowIpAddrType = _HpnicfDomainIpPoolLowIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 46, 2, 3, 1, 2),
    _HpnicfDomainIpPoolLowIpAddrType_Type()
)
hpnicfDomainIpPoolLowIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDomainIpPoolLowIpAddrType.setStatus("current")
_HpnicfDomainIpPoolLowIpAddr_Type = InetAddress
_HpnicfDomainIpPoolLowIpAddr_Object = MibTableColumn
hpnicfDomainIpPoolLowIpAddr = _HpnicfDomainIpPoolLowIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 46, 2, 3, 1, 3),
    _HpnicfDomainIpPoolLowIpAddr_Type()
)
hpnicfDomainIpPoolLowIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDomainIpPoolLowIpAddr.setStatus("current")
_HpnicfDomainIpPoolLen_Type = Integer32
_HpnicfDomainIpPoolLen_Object = MibTableColumn
hpnicfDomainIpPoolLen = _HpnicfDomainIpPoolLen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 46, 2, 3, 1, 4),
    _HpnicfDomainIpPoolLen_Type()
)
hpnicfDomainIpPoolLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDomainIpPoolLen.setStatus("current")
_HpnicfDomainIpPoolRowStatus_Type = RowStatus
_HpnicfDomainIpPoolRowStatus_Object = MibTableColumn
hpnicfDomainIpPoolRowStatus = _HpnicfDomainIpPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 46, 2, 3, 1, 5),
    _HpnicfDomainIpPoolRowStatus_Type()
)
hpnicfDomainIpPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDomainIpPoolRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-DOMAIN-MIB",
    **{"HpnicfModeOfDomainScheme": HpnicfModeOfDomainScheme,
       "HpnicfAAATypeDomainScheme": HpnicfAAATypeDomainScheme,
       "HpnicfAccessModeofDomainScheme": HpnicfAccessModeofDomainScheme,
       "hpnicfDomain": hpnicfDomain,
       "hpnicfDomainControl": hpnicfDomainControl,
       "hpnicfDomainDefault": hpnicfDomainDefault,
       "hpnicfDomainTables": hpnicfDomainTables,
       "hpnicfDomainInfoTable": hpnicfDomainInfoTable,
       "hpnicfDomainInfoEntry": hpnicfDomainInfoEntry,
       "hpnicfDomainName": hpnicfDomainName,
       "hpnicfDomainState": hpnicfDomainState,
       "hpnicfDomainMaxAccessNum": hpnicfDomainMaxAccessNum,
       "hpnicfDomainVlanAssignMode": hpnicfDomainVlanAssignMode,
       "hpnicfDomainIdleCutEnable": hpnicfDomainIdleCutEnable,
       "hpnicfDomainIdleCutMaxTime": hpnicfDomainIdleCutMaxTime,
       "hpnicfDomainIdleCutMinFlow": hpnicfDomainIdleCutMinFlow,
       "hpnicfDomainMessengerEnable": hpnicfDomainMessengerEnable,
       "hpnicfDomainMessengerLimitTime": hpnicfDomainMessengerLimitTime,
       "hpnicfDomainMessengerSpanTime": hpnicfDomainMessengerSpanTime,
       "hpnicfDomainSelfServiceEnable": hpnicfDomainSelfServiceEnable,
       "hpnicfDomainSelfServiceURL": hpnicfDomainSelfServiceURL,
       "hpnicfDomainAccFailureAction": hpnicfDomainAccFailureAction,
       "hpnicfDomainRowStatus": hpnicfDomainRowStatus,
       "hpnicfDomainCurrentAccessNum": hpnicfDomainCurrentAccessNum,
       "hpnicfDomainIdleCutTime": hpnicfDomainIdleCutTime,
       "hpnicfDomainSchemeTable": hpnicfDomainSchemeTable,
       "hpnicfDomainSchemeEntry": hpnicfDomainSchemeEntry,
       "hpnicfDomainSchemeIndex": hpnicfDomainSchemeIndex,
       "hpnicfDomainSchemeMode": hpnicfDomainSchemeMode,
       "hpnicfDomainAuthSchemeName": hpnicfDomainAuthSchemeName,
       "hpnicfDomainAcctSchemeName": hpnicfDomainAcctSchemeName,
       "hpnicfDomainSchemeRowStatus": hpnicfDomainSchemeRowStatus,
       "hpnicfDomainSchemeAAAType": hpnicfDomainSchemeAAAType,
       "hpnicfDomainSchemeAAAName": hpnicfDomainSchemeAAAName,
       "hpnicfDomainSchemeAccessMode": hpnicfDomainSchemeAccessMode,
       "hpnicfDomainIpPoolTable": hpnicfDomainIpPoolTable,
       "hpnicfDomainIpPoolEntry": hpnicfDomainIpPoolEntry,
       "hpnicfDomainIpPoolNum": hpnicfDomainIpPoolNum,
       "hpnicfDomainIpPoolLowIpAddrType": hpnicfDomainIpPoolLowIpAddrType,
       "hpnicfDomainIpPoolLowIpAddr": hpnicfDomainIpPoolLowIpAddr,
       "hpnicfDomainIpPoolLen": hpnicfDomainIpPoolLen,
       "hpnicfDomainIpPoolRowStatus": hpnicfDomainIpPoolRowStatus}
)
