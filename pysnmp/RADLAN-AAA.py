# SNMP MIB module (RADLAN-AAA) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-AAA
# Produced by pysmi-1.5.4 at Mon Oct 14 22:41:34 2024
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

(InetAddress,
 InetAddressIPv6,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv6",
    "InetAddressType")

(rlAAAEap,
 rlRadius,
 rnd) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rlAAAEap",
    "rlRadius",
    "rnd")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

rlAAA = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 79)
)
rlAAA.setRevisions(
        ("2010-06-21 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RlAAAMethodtype(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("rlAAAMethodDeny", 0),
          ("rlAAAMethodLinePassword", 1),
          ("rlAAAMethodLocalUserTable", 3),
          ("rlAAAMethodRadius", 4),
          ("rlAAAMethodSucceed", 6),
          ("rlAAAMethodSystemPassword", 2),
          ("rlAAAMethodTacacs", 5))
    )



class RlAAAServiceType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("rlAAAServiceTypeDontCare", 0),
          ("rlAAAServiceTypeHttp", 2),
          ("rlAAAServiceTypeHttps", 4),
          ("rlAAAServiceTypeSnmp", 5),
          ("rlAAAServiceTypeSsh", 3),
          ("rlAAAServiceTypeSshPubkey", 6),
          ("rlAAAServiceTypeTelnet", 1))
    )



class RlAAALinePortType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rlAAAPortConsole", 2),
          ("rlAAAPortDontCare", 0),
          ("rlAAAPortNetwork", 1))
    )



class RlAAAEapMethodtype(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rlAAAEapMethodDeny", 0),
          ("rlAAAEapMethodRadius", 1),
          ("rlAAAEapMethodSucceed", 2))
    )



class RlTacacsConnectionType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rlTacacsPerSessionConnection", 1),
          ("rlTacacsSingleConnection", 0))
    )



class RlTacacsConnectionStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rlTacacsConnected", 0),
          ("rlTacacsNotConnected", 1))
    )



class RlAAAAccountingMethod(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("radius", 2),
          ("tacacs", 3))
    )



# MIB Managed Objects in the order of their OIDs

_RlAAAMibVersion_Type = Integer32
_RlAAAMibVersion_Object = MibScalar
rlAAAMibVersion = _RlAAAMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 1),
    _RlAAAMibVersion_Type()
)
rlAAAMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAAMibVersion.setStatus("current")


class _RlAAARetries_Type(Integer32):
    """Custom type rlAAARetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_RlAAARetries_Type.__name__ = "Integer32"
_RlAAARetries_Object = MibScalar
rlAAARetries = _RlAAARetries_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 2),
    _RlAAARetries_Type()
)
rlAAARetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAARetries.setStatus("current")
_RlAAARadiusEnabled_Type = TruthValue
_RlAAARadiusEnabled_Object = MibScalar
rlAAARadiusEnabled = _RlAAARadiusEnabled_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 3),
    _RlAAARadiusEnabled_Type()
)
rlAAARadiusEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAARadiusEnabled.setStatus("current")
_RlAAATacacsEnabled_Type = TruthValue
_RlAAATacacsEnabled_Object = MibScalar
rlAAATacacsEnabled = _RlAAATacacsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 4),
    _RlAAATacacsEnabled_Type()
)
rlAAATacacsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAATacacsEnabled.setStatus("current")
_RlAAALocalUserEnabled_Type = TruthValue
_RlAAALocalUserEnabled_Object = MibScalar
rlAAALocalUserEnabled = _RlAAALocalUserEnabled_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 5),
    _RlAAALocalUserEnabled_Type()
)
rlAAALocalUserEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAALocalUserEnabled.setStatus("current")
_RlAAASystemPasswordEnabled_Type = TruthValue
_RlAAASystemPasswordEnabled_Object = MibScalar
rlAAASystemPasswordEnabled = _RlAAASystemPasswordEnabled_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 6),
    _RlAAASystemPasswordEnabled_Type()
)
rlAAASystemPasswordEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAASystemPasswordEnabled.setStatus("current")
_RlAAALinePasswordEnabled_Type = TruthValue
_RlAAALinePasswordEnabled_Object = MibScalar
rlAAALinePasswordEnabled = _RlAAALinePasswordEnabled_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 7),
    _RlAAALinePasswordEnabled_Type()
)
rlAAALinePasswordEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAALinePasswordEnabled.setStatus("current")
_RlAAAAlwaysSuccessEnabled_Type = TruthValue
_RlAAAAlwaysSuccessEnabled_Object = MibScalar
rlAAAAlwaysSuccessEnabled = _RlAAAAlwaysSuccessEnabled_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 8),
    _RlAAAAlwaysSuccessEnabled_Type()
)
rlAAAAlwaysSuccessEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAAAlwaysSuccessEnabled.setStatus("current")
_RlAAARadiusSupported_Type = TruthValue
_RlAAARadiusSupported_Object = MibScalar
rlAAARadiusSupported = _RlAAARadiusSupported_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 9),
    _RlAAARadiusSupported_Type()
)
rlAAARadiusSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAARadiusSupported.setStatus("current")
_RlAAATacacsSupported_Type = TruthValue
_RlAAATacacsSupported_Object = MibScalar
rlAAATacacsSupported = _RlAAATacacsSupported_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 10),
    _RlAAATacacsSupported_Type()
)
rlAAATacacsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAATacacsSupported.setStatus("current")
_RlAAALocalUserSupported_Type = TruthValue
_RlAAALocalUserSupported_Object = MibScalar
rlAAALocalUserSupported = _RlAAALocalUserSupported_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 11),
    _RlAAALocalUserSupported_Type()
)
rlAAALocalUserSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAALocalUserSupported.setStatus("current")
_RlAAASystemPasswordSupported_Type = TruthValue
_RlAAASystemPasswordSupported_Object = MibScalar
rlAAASystemPasswordSupported = _RlAAASystemPasswordSupported_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 12),
    _RlAAASystemPasswordSupported_Type()
)
rlAAASystemPasswordSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAASystemPasswordSupported.setStatus("current")
_RlAAALinePasswordSupported_Type = TruthValue
_RlAAALinePasswordSupported_Object = MibScalar
rlAAALinePasswordSupported = _RlAAALinePasswordSupported_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 13),
    _RlAAALinePasswordSupported_Type()
)
rlAAALinePasswordSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAALinePasswordSupported.setStatus("current")
_RlAAALineAlwaysSuccessSupported_Type = TruthValue
_RlAAALineAlwaysSuccessSupported_Object = MibScalar
rlAAALineAlwaysSuccessSupported = _RlAAALineAlwaysSuccessSupported_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 14),
    _RlAAALineAlwaysSuccessSupported_Type()
)
rlAAALineAlwaysSuccessSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAALineAlwaysSuccessSupported.setStatus("current")
_RlAAAMethodListTable_Object = MibTable
rlAAAMethodListTable = _RlAAAMethodListTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 15)
)
if mibBuilder.loadTexts:
    rlAAAMethodListTable.setStatus("current")
_RlAAAMethodListEntry_Object = MibTableRow
rlAAAMethodListEntry = _RlAAAMethodListEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 15, 1)
)
rlAAAMethodListEntry.setIndexNames(
    (0, "RADLAN-AAA", "rlAAAMethodListName"),
)
if mibBuilder.loadTexts:
    rlAAAMethodListEntry.setStatus("current")


class _RlAAAMethodListName_Type(DisplayString):
    """Custom type rlAAAMethodListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 20),
    )


_RlAAAMethodListName_Type.__name__ = "DisplayString"
_RlAAAMethodListName_Object = MibTableColumn
rlAAAMethodListName = _RlAAAMethodListName_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 15, 1, 1),
    _RlAAAMethodListName_Type()
)
rlAAAMethodListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAAMethodListName.setStatus("current")
_RlAAAMethodType1_Type = RlAAAMethodtype
_RlAAAMethodType1_Object = MibTableColumn
rlAAAMethodType1 = _RlAAAMethodType1_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 15, 1, 2),
    _RlAAAMethodType1_Type()
)
rlAAAMethodType1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAAMethodType1.setStatus("current")
_RlAAAMethodType2_Type = RlAAAMethodtype
_RlAAAMethodType2_Object = MibTableColumn
rlAAAMethodType2 = _RlAAAMethodType2_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 15, 1, 3),
    _RlAAAMethodType2_Type()
)
rlAAAMethodType2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAAMethodType2.setStatus("current")
_RlAAAMethodType3_Type = RlAAAMethodtype
_RlAAAMethodType3_Object = MibTableColumn
rlAAAMethodType3 = _RlAAAMethodType3_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 15, 1, 4),
    _RlAAAMethodType3_Type()
)
rlAAAMethodType3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAAMethodType3.setStatus("current")
_RlAAAMethodType4_Type = RlAAAMethodtype
_RlAAAMethodType4_Object = MibTableColumn
rlAAAMethodType4 = _RlAAAMethodType4_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 15, 1, 5),
    _RlAAAMethodType4_Type()
)
rlAAAMethodType4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAAMethodType4.setStatus("current")
_RlAAAMethodType5_Type = RlAAAMethodtype
_RlAAAMethodType5_Object = MibTableColumn
rlAAAMethodType5 = _RlAAAMethodType5_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 15, 1, 6),
    _RlAAAMethodType5_Type()
)
rlAAAMethodType5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAAMethodType5.setStatus("current")
_RlAAAMethodType6_Type = RlAAAMethodtype
_RlAAAMethodType6_Object = MibTableColumn
rlAAAMethodType6 = _RlAAAMethodType6_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 15, 1, 7),
    _RlAAAMethodType6_Type()
)
rlAAAMethodType6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAAMethodType6.setStatus("current")
_RlAAAMethodType7_Type = RlAAAMethodtype
_RlAAAMethodType7_Object = MibTableColumn
rlAAAMethodType7 = _RlAAAMethodType7_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 15, 1, 8),
    _RlAAAMethodType7_Type()
)
rlAAAMethodType7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAAMethodType7.setStatus("current")
_RlAAAMethodListStatus_Type = RowStatus
_RlAAAMethodListStatus_Object = MibTableColumn
rlAAAMethodListStatus = _RlAAAMethodListStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 15, 1, 9),
    _RlAAAMethodListStatus_Type()
)
rlAAAMethodListStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAAMethodListStatus.setStatus("current")
_RlAAAAuthorizeEnable_Type = Integer32
_RlAAAAuthorizeEnable_Object = MibTableColumn
rlAAAAuthorizeEnable = _RlAAAAuthorizeEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 15, 1, 10),
    _RlAAAAuthorizeEnable_Type()
)
rlAAAAuthorizeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAAAuthorizeEnable.setStatus("current")
_RlAAALineTable_Object = MibTable
rlAAALineTable = _RlAAALineTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 16)
)
if mibBuilder.loadTexts:
    rlAAALineTable.setStatus("current")
_RlAAALineEntry_Object = MibTableRow
rlAAALineEntry = _RlAAALineEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 16, 1)
)
rlAAALineEntry.setIndexNames(
    (0, "RADLAN-AAA", "rlAAALinePortType"),
    (0, "RADLAN-AAA", "rlAAAIfIndex"),
    (0, "RADLAN-AAA", "rlAAAServiceType"),
)
if mibBuilder.loadTexts:
    rlAAALineEntry.setStatus("current")
_RlAAALinePortType_Type = RlAAALinePortType
_RlAAALinePortType_Object = MibTableColumn
rlAAALinePortType = _RlAAALinePortType_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 16, 1, 1),
    _RlAAALinePortType_Type()
)
rlAAALinePortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAALinePortType.setStatus("current")
_RlAAAIfIndex_Type = Unsigned32
_RlAAAIfIndex_Object = MibTableColumn
rlAAAIfIndex = _RlAAAIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 16, 1, 2),
    _RlAAAIfIndex_Type()
)
rlAAAIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAAIfIndex.setStatus("current")
_RlAAAServiceType_Type = RlAAAServiceType
_RlAAAServiceType_Object = MibTableColumn
rlAAAServiceType = _RlAAAServiceType_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 16, 1, 3),
    _RlAAAServiceType_Type()
)
rlAAAServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAAServiceType.setStatus("current")


class _RlAAALineMethodListNameLevel1_Type(DisplayString):
    """Custom type rlAAALineMethodListNameLevel1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RlAAALineMethodListNameLevel1_Type.__name__ = "DisplayString"
_RlAAALineMethodListNameLevel1_Object = MibTableColumn
rlAAALineMethodListNameLevel1 = _RlAAALineMethodListNameLevel1_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 16, 1, 4),
    _RlAAALineMethodListNameLevel1_Type()
)
rlAAALineMethodListNameLevel1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAALineMethodListNameLevel1.setStatus("current")


class _RlAAALineMethodListNameLevel2_Type(DisplayString):
    """Custom type rlAAALineMethodListNameLevel2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RlAAALineMethodListNameLevel2_Type.__name__ = "DisplayString"
_RlAAALineMethodListNameLevel2_Object = MibTableColumn
rlAAALineMethodListNameLevel2 = _RlAAALineMethodListNameLevel2_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 16, 1, 5),
    _RlAAALineMethodListNameLevel2_Type()
)
rlAAALineMethodListNameLevel2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAALineMethodListNameLevel2.setStatus("current")


class _RlAAALineMethodListNameLevel3_Type(DisplayString):
    """Custom type rlAAALineMethodListNameLevel3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RlAAALineMethodListNameLevel3_Type.__name__ = "DisplayString"
_RlAAALineMethodListNameLevel3_Object = MibTableColumn
rlAAALineMethodListNameLevel3 = _RlAAALineMethodListNameLevel3_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 16, 1, 6),
    _RlAAALineMethodListNameLevel3_Type()
)
rlAAALineMethodListNameLevel3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAALineMethodListNameLevel3.setStatus("current")


class _RlAAALineMethodListNameLevel4_Type(DisplayString):
    """Custom type rlAAALineMethodListNameLevel4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RlAAALineMethodListNameLevel4_Type.__name__ = "DisplayString"
_RlAAALineMethodListNameLevel4_Object = MibTableColumn
rlAAALineMethodListNameLevel4 = _RlAAALineMethodListNameLevel4_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 16, 1, 7),
    _RlAAALineMethodListNameLevel4_Type()
)
rlAAALineMethodListNameLevel4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAALineMethodListNameLevel4.setStatus("current")


class _RlAAALineMethodListNameLevel5_Type(DisplayString):
    """Custom type rlAAALineMethodListNameLevel5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RlAAALineMethodListNameLevel5_Type.__name__ = "DisplayString"
_RlAAALineMethodListNameLevel5_Object = MibTableColumn
rlAAALineMethodListNameLevel5 = _RlAAALineMethodListNameLevel5_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 16, 1, 8),
    _RlAAALineMethodListNameLevel5_Type()
)
rlAAALineMethodListNameLevel5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAALineMethodListNameLevel5.setStatus("current")


class _RlAAALineMethodListNameLevel6_Type(DisplayString):
    """Custom type rlAAALineMethodListNameLevel6 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RlAAALineMethodListNameLevel6_Type.__name__ = "DisplayString"
_RlAAALineMethodListNameLevel6_Object = MibTableColumn
rlAAALineMethodListNameLevel6 = _RlAAALineMethodListNameLevel6_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 16, 1, 9),
    _RlAAALineMethodListNameLevel6_Type()
)
rlAAALineMethodListNameLevel6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAALineMethodListNameLevel6.setStatus("current")


class _RlAAALineMethodListNameLevel7_Type(DisplayString):
    """Custom type rlAAALineMethodListNameLevel7 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RlAAALineMethodListNameLevel7_Type.__name__ = "DisplayString"
_RlAAALineMethodListNameLevel7_Object = MibTableColumn
rlAAALineMethodListNameLevel7 = _RlAAALineMethodListNameLevel7_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 16, 1, 10),
    _RlAAALineMethodListNameLevel7_Type()
)
rlAAALineMethodListNameLevel7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAALineMethodListNameLevel7.setStatus("current")


class _RlAAALineMethodListNameLevel8_Type(DisplayString):
    """Custom type rlAAALineMethodListNameLevel8 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RlAAALineMethodListNameLevel8_Type.__name__ = "DisplayString"
_RlAAALineMethodListNameLevel8_Object = MibTableColumn
rlAAALineMethodListNameLevel8 = _RlAAALineMethodListNameLevel8_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 16, 1, 11),
    _RlAAALineMethodListNameLevel8_Type()
)
rlAAALineMethodListNameLevel8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAALineMethodListNameLevel8.setStatus("current")


class _RlAAALineMethodListNameLevel9_Type(DisplayString):
    """Custom type rlAAALineMethodListNameLevel9 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RlAAALineMethodListNameLevel9_Type.__name__ = "DisplayString"
_RlAAALineMethodListNameLevel9_Object = MibTableColumn
rlAAALineMethodListNameLevel9 = _RlAAALineMethodListNameLevel9_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 16, 1, 12),
    _RlAAALineMethodListNameLevel9_Type()
)
rlAAALineMethodListNameLevel9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAALineMethodListNameLevel9.setStatus("current")


class _RlAAALineMethodListNameLevel10_Type(DisplayString):
    """Custom type rlAAALineMethodListNameLevel10 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RlAAALineMethodListNameLevel10_Type.__name__ = "DisplayString"
_RlAAALineMethodListNameLevel10_Object = MibTableColumn
rlAAALineMethodListNameLevel10 = _RlAAALineMethodListNameLevel10_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 16, 1, 13),
    _RlAAALineMethodListNameLevel10_Type()
)
rlAAALineMethodListNameLevel10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAALineMethodListNameLevel10.setStatus("current")


class _RlAAALineMethodListNameLevel11_Type(DisplayString):
    """Custom type rlAAALineMethodListNameLevel11 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RlAAALineMethodListNameLevel11_Type.__name__ = "DisplayString"
_RlAAALineMethodListNameLevel11_Object = MibTableColumn
rlAAALineMethodListNameLevel11 = _RlAAALineMethodListNameLevel11_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 16, 1, 14),
    _RlAAALineMethodListNameLevel11_Type()
)
rlAAALineMethodListNameLevel11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAALineMethodListNameLevel11.setStatus("current")


class _RlAAALineMethodListNameLevel12_Type(DisplayString):
    """Custom type rlAAALineMethodListNameLevel12 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RlAAALineMethodListNameLevel12_Type.__name__ = "DisplayString"
_RlAAALineMethodListNameLevel12_Object = MibTableColumn
rlAAALineMethodListNameLevel12 = _RlAAALineMethodListNameLevel12_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 16, 1, 15),
    _RlAAALineMethodListNameLevel12_Type()
)
rlAAALineMethodListNameLevel12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAALineMethodListNameLevel12.setStatus("current")


class _RlAAALineMethodListNameLevel13_Type(DisplayString):
    """Custom type rlAAALineMethodListNameLevel13 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RlAAALineMethodListNameLevel13_Type.__name__ = "DisplayString"
_RlAAALineMethodListNameLevel13_Object = MibTableColumn
rlAAALineMethodListNameLevel13 = _RlAAALineMethodListNameLevel13_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 16, 1, 16),
    _RlAAALineMethodListNameLevel13_Type()
)
rlAAALineMethodListNameLevel13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAALineMethodListNameLevel13.setStatus("current")


class _RlAAALineMethodListNameLevel14_Type(DisplayString):
    """Custom type rlAAALineMethodListNameLevel14 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RlAAALineMethodListNameLevel14_Type.__name__ = "DisplayString"
_RlAAALineMethodListNameLevel14_Object = MibTableColumn
rlAAALineMethodListNameLevel14 = _RlAAALineMethodListNameLevel14_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 16, 1, 17),
    _RlAAALineMethodListNameLevel14_Type()
)
rlAAALineMethodListNameLevel14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAALineMethodListNameLevel14.setStatus("current")


class _RlAAALineMethodListNameLevel15_Type(DisplayString):
    """Custom type rlAAALineMethodListNameLevel15 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RlAAALineMethodListNameLevel15_Type.__name__ = "DisplayString"
_RlAAALineMethodListNameLevel15_Object = MibTableColumn
rlAAALineMethodListNameLevel15 = _RlAAALineMethodListNameLevel15_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 16, 1, 18),
    _RlAAALineMethodListNameLevel15_Type()
)
rlAAALineMethodListNameLevel15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAALineMethodListNameLevel15.setStatus("current")


class _RlAAALinePassword_Type(DisplayString):
    """Custom type rlAAALinePassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_RlAAALinePassword_Type.__name__ = "DisplayString"
_RlAAALinePassword_Object = MibTableColumn
rlAAALinePassword = _RlAAALinePassword_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 16, 1, 19),
    _RlAAALinePassword_Type()
)
rlAAALinePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAALinePassword.setStatus("current")
_RlAAALineStatus_Type = RowStatus
_RlAAALineStatus_Object = MibTableColumn
rlAAALineStatus = _RlAAALineStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 16, 1, 20),
    _RlAAALineStatus_Type()
)
rlAAALineStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAALineStatus.setStatus("current")


class _RlAAALineLockedState_Type(Integer32):
    """Custom type rlAAALineLockedState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("usable", 1))
    )


_RlAAALineLockedState_Type.__name__ = "Integer32"
_RlAAALineLockedState_Object = MibTableColumn
rlAAALineLockedState = _RlAAALineLockedState_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 16, 1, 21),
    _RlAAALineLockedState_Type()
)
rlAAALineLockedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAALineLockedState.setStatus("current")
_RlAAALineConsFailedLogins_Type = Counter32
_RlAAALineConsFailedLogins_Object = MibTableColumn
rlAAALineConsFailedLogins = _RlAAALineConsFailedLogins_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 16, 1, 22),
    _RlAAALineConsFailedLogins_Type()
)
rlAAALineConsFailedLogins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAALineConsFailedLogins.setStatus("current")


class _RlAAALinePasswordValidTime_Type(Unsigned32):
    """Custom type rlAAALinePasswordValidTime based on Unsigned32"""
    defaultValue = 0


_RlAAALinePasswordValidTime_Object = MibTableColumn
rlAAALinePasswordValidTime = _RlAAALinePasswordValidTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 16, 1, 23),
    _RlAAALinePasswordValidTime_Type()
)
rlAAALinePasswordValidTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAALinePasswordValidTime.setStatus("current")
_RlAAALinePasswordExpieryDate_Type = DisplayString
_RlAAALinePasswordExpieryDate_Object = MibTableColumn
rlAAALinePasswordExpieryDate = _RlAAALinePasswordExpieryDate_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 16, 1, 24),
    _RlAAALinePasswordExpieryDate_Type()
)
rlAAALinePasswordExpieryDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAALinePasswordExpieryDate.setStatus("current")
_RlAAALocalUserTable_Object = MibTable
rlAAALocalUserTable = _RlAAALocalUserTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 17)
)
if mibBuilder.loadTexts:
    rlAAALocalUserTable.setStatus("current")
_RlAAALocalUserEntry_Object = MibTableRow
rlAAALocalUserEntry = _RlAAALocalUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 17, 1)
)
rlAAALocalUserEntry.setIndexNames(
    (0, "RADLAN-AAA", "rlAAALocalUserName"),
)
if mibBuilder.loadTexts:
    rlAAALocalUserEntry.setStatus("current")


class _RlAAALocalUserName_Type(DisplayString):
    """Custom type rlAAALocalUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_RlAAALocalUserName_Type.__name__ = "DisplayString"
_RlAAALocalUserName_Object = MibTableColumn
rlAAALocalUserName = _RlAAALocalUserName_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 17, 1, 1),
    _RlAAALocalUserName_Type()
)
rlAAALocalUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAALocalUserName.setStatus("current")


class _RlAAALocalUserPassword_Type(DisplayString):
    """Custom type rlAAALocalUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_RlAAALocalUserPassword_Type.__name__ = "DisplayString"
_RlAAALocalUserPassword_Object = MibTableColumn
rlAAALocalUserPassword = _RlAAALocalUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 17, 1, 2),
    _RlAAALocalUserPassword_Type()
)
rlAAALocalUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAALocalUserPassword.setStatus("current")


class _RlAAALocalUserPrivilage_Type(Integer32):
    """Custom type rlAAALocalUserPrivilage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RlAAALocalUserPrivilage_Type.__name__ = "Integer32"
_RlAAALocalUserPrivilage_Object = MibTableColumn
rlAAALocalUserPrivilage = _RlAAALocalUserPrivilage_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 17, 1, 3),
    _RlAAALocalUserPrivilage_Type()
)
rlAAALocalUserPrivilage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAALocalUserPrivilage.setStatus("current")
_RlAAALocalHostStatus_Type = RowStatus
_RlAAALocalHostStatus_Object = MibTableColumn
rlAAALocalHostStatus = _RlAAALocalHostStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 17, 1, 4),
    _RlAAALocalHostStatus_Type()
)
rlAAALocalHostStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAALocalHostStatus.setStatus("current")


class _RlAAALocalLockedState_Type(Integer32):
    """Custom type rlAAALocalLockedState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("usable", 1))
    )


_RlAAALocalLockedState_Type.__name__ = "Integer32"
_RlAAALocalLockedState_Object = MibTableColumn
rlAAALocalLockedState = _RlAAALocalLockedState_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 17, 1, 5),
    _RlAAALocalLockedState_Type()
)
rlAAALocalLockedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAALocalLockedState.setStatus("current")
_RlAAALocalConsFailedLogins_Type = Counter32
_RlAAALocalConsFailedLogins_Object = MibTableColumn
rlAAALocalConsFailedLogins = _RlAAALocalConsFailedLogins_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 17, 1, 6),
    _RlAAALocalConsFailedLogins_Type()
)
rlAAALocalConsFailedLogins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAALocalConsFailedLogins.setStatus("current")


class _RlAAALocalPasswordValidTime_Type(Unsigned32):
    """Custom type rlAAALocalPasswordValidTime based on Unsigned32"""
    defaultValue = 0


_RlAAALocalPasswordValidTime_Object = MibTableColumn
rlAAALocalPasswordValidTime = _RlAAALocalPasswordValidTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 17, 1, 7),
    _RlAAALocalPasswordValidTime_Type()
)
rlAAALocalPasswordValidTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAALocalPasswordValidTime.setStatus("current")
_RlAAALocalPasswordExpieryDate_Type = DisplayString
_RlAAALocalPasswordExpieryDate_Object = MibTableColumn
rlAAALocalPasswordExpieryDate = _RlAAALocalPasswordExpieryDate_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 17, 1, 8),
    _RlAAALocalPasswordExpieryDate_Type()
)
rlAAALocalPasswordExpieryDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAALocalPasswordExpieryDate.setStatus("current")
_RlAAALocalPasswordCreationDate_Type = DisplayString
_RlAAALocalPasswordCreationDate_Object = MibTableColumn
rlAAALocalPasswordCreationDate = _RlAAALocalPasswordCreationDate_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 17, 1, 9),
    _RlAAALocalPasswordCreationDate_Type()
)
rlAAALocalPasswordCreationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAALocalPasswordCreationDate.setStatus("current")


class _RlAAASystemPasswordlevel1_Type(DisplayString):
    """Custom type rlAAASystemPasswordlevel1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_RlAAASystemPasswordlevel1_Type.__name__ = "DisplayString"
_RlAAASystemPasswordlevel1_Object = MibScalar
rlAAASystemPasswordlevel1 = _RlAAASystemPasswordlevel1_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 18),
    _RlAAASystemPasswordlevel1_Type()
)
rlAAASystemPasswordlevel1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAASystemPasswordlevel1.setStatus("current")


class _RlAAASystemPasswordlevel2_Type(DisplayString):
    """Custom type rlAAASystemPasswordlevel2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_RlAAASystemPasswordlevel2_Type.__name__ = "DisplayString"
_RlAAASystemPasswordlevel2_Object = MibScalar
rlAAASystemPasswordlevel2 = _RlAAASystemPasswordlevel2_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 19),
    _RlAAASystemPasswordlevel2_Type()
)
rlAAASystemPasswordlevel2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAASystemPasswordlevel2.setStatus("current")


class _RlAAASystemPasswordlevel3_Type(DisplayString):
    """Custom type rlAAASystemPasswordlevel3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_RlAAASystemPasswordlevel3_Type.__name__ = "DisplayString"
_RlAAASystemPasswordlevel3_Object = MibScalar
rlAAASystemPasswordlevel3 = _RlAAASystemPasswordlevel3_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 20),
    _RlAAASystemPasswordlevel3_Type()
)
rlAAASystemPasswordlevel3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAASystemPasswordlevel3.setStatus("current")


class _RlAAASystemPasswordlevel4_Type(DisplayString):
    """Custom type rlAAASystemPasswordlevel4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_RlAAASystemPasswordlevel4_Type.__name__ = "DisplayString"
_RlAAASystemPasswordlevel4_Object = MibScalar
rlAAASystemPasswordlevel4 = _RlAAASystemPasswordlevel4_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 21),
    _RlAAASystemPasswordlevel4_Type()
)
rlAAASystemPasswordlevel4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAASystemPasswordlevel4.setStatus("current")


class _RlAAASystemPasswordlevel5_Type(DisplayString):
    """Custom type rlAAASystemPasswordlevel5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_RlAAASystemPasswordlevel5_Type.__name__ = "DisplayString"
_RlAAASystemPasswordlevel5_Object = MibScalar
rlAAASystemPasswordlevel5 = _RlAAASystemPasswordlevel5_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 22),
    _RlAAASystemPasswordlevel5_Type()
)
rlAAASystemPasswordlevel5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAASystemPasswordlevel5.setStatus("current")


class _RlAAASystemPasswordlevel6_Type(DisplayString):
    """Custom type rlAAASystemPasswordlevel6 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_RlAAASystemPasswordlevel6_Type.__name__ = "DisplayString"
_RlAAASystemPasswordlevel6_Object = MibScalar
rlAAASystemPasswordlevel6 = _RlAAASystemPasswordlevel6_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 23),
    _RlAAASystemPasswordlevel6_Type()
)
rlAAASystemPasswordlevel6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAASystemPasswordlevel6.setStatus("current")


class _RlAAASystemPasswordlevel7_Type(DisplayString):
    """Custom type rlAAASystemPasswordlevel7 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_RlAAASystemPasswordlevel7_Type.__name__ = "DisplayString"
_RlAAASystemPasswordlevel7_Object = MibScalar
rlAAASystemPasswordlevel7 = _RlAAASystemPasswordlevel7_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 24),
    _RlAAASystemPasswordlevel7_Type()
)
rlAAASystemPasswordlevel7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAASystemPasswordlevel7.setStatus("current")


class _RlAAASystemPasswordlevel8_Type(DisplayString):
    """Custom type rlAAASystemPasswordlevel8 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_RlAAASystemPasswordlevel8_Type.__name__ = "DisplayString"
_RlAAASystemPasswordlevel8_Object = MibScalar
rlAAASystemPasswordlevel8 = _RlAAASystemPasswordlevel8_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 25),
    _RlAAASystemPasswordlevel8_Type()
)
rlAAASystemPasswordlevel8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAASystemPasswordlevel8.setStatus("current")


class _RlAAASystemPasswordlevel9_Type(DisplayString):
    """Custom type rlAAASystemPasswordlevel9 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_RlAAASystemPasswordlevel9_Type.__name__ = "DisplayString"
_RlAAASystemPasswordlevel9_Object = MibScalar
rlAAASystemPasswordlevel9 = _RlAAASystemPasswordlevel9_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 26),
    _RlAAASystemPasswordlevel9_Type()
)
rlAAASystemPasswordlevel9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAASystemPasswordlevel9.setStatus("current")


class _RlAAASystemPasswordlevel10_Type(DisplayString):
    """Custom type rlAAASystemPasswordlevel10 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_RlAAASystemPasswordlevel10_Type.__name__ = "DisplayString"
_RlAAASystemPasswordlevel10_Object = MibScalar
rlAAASystemPasswordlevel10 = _RlAAASystemPasswordlevel10_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 27),
    _RlAAASystemPasswordlevel10_Type()
)
rlAAASystemPasswordlevel10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAASystemPasswordlevel10.setStatus("current")


class _RlAAASystemPasswordlevel11_Type(DisplayString):
    """Custom type rlAAASystemPasswordlevel11 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_RlAAASystemPasswordlevel11_Type.__name__ = "DisplayString"
_RlAAASystemPasswordlevel11_Object = MibScalar
rlAAASystemPasswordlevel11 = _RlAAASystemPasswordlevel11_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 28),
    _RlAAASystemPasswordlevel11_Type()
)
rlAAASystemPasswordlevel11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAASystemPasswordlevel11.setStatus("current")


class _RlAAASystemPasswordlevel12_Type(DisplayString):
    """Custom type rlAAASystemPasswordlevel12 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_RlAAASystemPasswordlevel12_Type.__name__ = "DisplayString"
_RlAAASystemPasswordlevel12_Object = MibScalar
rlAAASystemPasswordlevel12 = _RlAAASystemPasswordlevel12_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 29),
    _RlAAASystemPasswordlevel12_Type()
)
rlAAASystemPasswordlevel12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAASystemPasswordlevel12.setStatus("current")


class _RlAAASystemPasswordlevel13_Type(DisplayString):
    """Custom type rlAAASystemPasswordlevel13 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_RlAAASystemPasswordlevel13_Type.__name__ = "DisplayString"
_RlAAASystemPasswordlevel13_Object = MibScalar
rlAAASystemPasswordlevel13 = _RlAAASystemPasswordlevel13_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 30),
    _RlAAASystemPasswordlevel13_Type()
)
rlAAASystemPasswordlevel13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAASystemPasswordlevel13.setStatus("current")


class _RlAAASystemPasswordlevel14_Type(DisplayString):
    """Custom type rlAAASystemPasswordlevel14 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_RlAAASystemPasswordlevel14_Type.__name__ = "DisplayString"
_RlAAASystemPasswordlevel14_Object = MibScalar
rlAAASystemPasswordlevel14 = _RlAAASystemPasswordlevel14_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 31),
    _RlAAASystemPasswordlevel14_Type()
)
rlAAASystemPasswordlevel14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAASystemPasswordlevel14.setStatus("current")


class _RlAAASystemPasswordlevel15_Type(DisplayString):
    """Custom type rlAAASystemPasswordlevel15 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_RlAAASystemPasswordlevel15_Type.__name__ = "DisplayString"
_RlAAASystemPasswordlevel15_Object = MibScalar
rlAAASystemPasswordlevel15 = _RlAAASystemPasswordlevel15_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 32),
    _RlAAASystemPasswordlevel15_Type()
)
rlAAASystemPasswordlevel15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAASystemPasswordlevel15.setStatus("current")
_RlAAAUserTable_Object = MibTable
rlAAAUserTable = _RlAAAUserTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 33)
)
if mibBuilder.loadTexts:
    rlAAAUserTable.setStatus("current")
_RlAAAUserEntry_Object = MibTableRow
rlAAAUserEntry = _RlAAAUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 33, 1)
)
rlAAAUserEntry.setIndexNames(
    (0, "RADLAN-AAA", "rlAAAUserIndex"),
)
if mibBuilder.loadTexts:
    rlAAAUserEntry.setStatus("current")
_RlAAAUserIndex_Type = Unsigned32
_RlAAAUserIndex_Object = MibTableColumn
rlAAAUserIndex = _RlAAAUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 33, 1, 1),
    _RlAAAUserIndex_Type()
)
rlAAAUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlAAAUserIndex.setStatus("current")
_RlAAAUserServiceType_Type = RlAAAServiceType
_RlAAAUserServiceType_Object = MibTableColumn
rlAAAUserServiceType = _RlAAAUserServiceType_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 33, 1, 2),
    _RlAAAUserServiceType_Type()
)
rlAAAUserServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAAUserServiceType.setStatus("current")
_RlAAAUserRemoteIpAddress_Type = IpAddress
_RlAAAUserRemoteIpAddress_Object = MibTableColumn
rlAAAUserRemoteIpAddress = _RlAAAUserRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 33, 1, 3),
    _RlAAAUserRemoteIpAddress_Type()
)
rlAAAUserRemoteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAAUserRemoteIpAddress.setStatus("current")
_RlAAAUserName_Type = DisplayString
_RlAAAUserName_Object = MibTableColumn
rlAAAUserName = _RlAAAUserName_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 33, 1, 4),
    _RlAAAUserName_Type()
)
rlAAAUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAAUserName.setStatus("current")


class _RlAAAUserLevel_Type(Unsigned32):
    """Custom type rlAAAUserLevel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RlAAAUserLevel_Type.__name__ = "Unsigned32"
_RlAAAUserLevel_Object = MibTableColumn
rlAAAUserLevel = _RlAAAUserLevel_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 33, 1, 5),
    _RlAAAUserLevel_Type()
)
rlAAAUserLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAAUserLevel.setStatus("current")
_RlAAAUserIfIndex_Type = Unsigned32
_RlAAAUserIfIndex_Object = MibTableColumn
rlAAAUserIfIndex = _RlAAAUserIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 33, 1, 6),
    _RlAAAUserIfIndex_Type()
)
rlAAAUserIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAAUserIfIndex.setStatus("current")
_RlAAAUserLoginDate_Type = DateAndTime
_RlAAAUserLoginDate_Object = MibTableColumn
rlAAAUserLoginDate = _RlAAAUserLoginDate_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 33, 1, 7),
    _RlAAAUserLoginDate_Type()
)
rlAAAUserLoginDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAAUserLoginDate.setStatus("current")
_RlAAAUserLoginDurationMS_Type = Unsigned32
_RlAAAUserLoginDurationMS_Object = MibTableColumn
rlAAAUserLoginDurationMS = _RlAAAUserLoginDurationMS_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 33, 1, 8),
    _RlAAAUserLoginDurationMS_Type()
)
rlAAAUserLoginDurationMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAAUserLoginDurationMS.setStatus("current")
_RlAAATest_ObjectIdentity = ObjectIdentity
rlAAATest = _RlAAATest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 79, 34)
)
_RlAAATestPassword_Type = Integer32
_RlAAATestPassword_Object = MibScalar
rlAAATestPassword = _RlAAATestPassword_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 34, 1),
    _RlAAATestPassword_Type()
)
rlAAATestPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAATestPassword.setStatus("current")
_RlAAATestUserTable_Object = MibTable
rlAAATestUserTable = _RlAAATestUserTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 34, 2)
)
if mibBuilder.loadTexts:
    rlAAATestUserTable.setStatus("current")
_RlAAATestUserEntry_Object = MibTableRow
rlAAATestUserEntry = _RlAAATestUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 34, 2, 1)
)
rlAAATestUserEntry.setIndexNames(
    (0, "RADLAN-AAA", "rlAAATestUserIndex"),
)
if mibBuilder.loadTexts:
    rlAAATestUserEntry.setStatus("current")
_RlAAATestUserIndex_Type = Unsigned32
_RlAAATestUserIndex_Object = MibTableColumn
rlAAATestUserIndex = _RlAAATestUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 34, 2, 1, 1),
    _RlAAATestUserIndex_Type()
)
rlAAATestUserIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAATestUserIndex.setStatus("current")
_RlAAATestPortType_Type = RlAAALinePortType
_RlAAATestPortType_Object = MibTableColumn
rlAAATestPortType = _RlAAATestPortType_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 34, 2, 1, 2),
    _RlAAATestPortType_Type()
)
rlAAATestPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAATestPortType.setStatus("current")
_RlAAATestIfIndex_Type = Integer32
_RlAAATestIfIndex_Object = MibTableColumn
rlAAATestIfIndex = _RlAAATestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 34, 2, 1, 3),
    _RlAAATestIfIndex_Type()
)
rlAAATestIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAATestIfIndex.setStatus("current")
_RlAAATestServiceType_Type = RlAAAServiceType
_RlAAATestServiceType_Object = MibTableColumn
rlAAATestServiceType = _RlAAATestServiceType_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 34, 2, 1, 4),
    _RlAAATestServiceType_Type()
)
rlAAATestServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAATestServiceType.setStatus("current")


class _RlAAATestUserAuthenticationStatus_Type(Integer32):
    """Custom type rlAAATestUserAuthenticationStatus based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 5),
          ("deleted", 6),
          ("failure", 4),
          ("needPassword", 1),
          ("needUsername", 2),
          ("success", 3),
          ("usedNewMethod", 8),
          ("waiting", 7))
    )


_RlAAATestUserAuthenticationStatus_Type.__name__ = "Integer32"
_RlAAATestUserAuthenticationStatus_Object = MibTableColumn
rlAAATestUserAuthenticationStatus = _RlAAATestUserAuthenticationStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 34, 2, 1, 5),
    _RlAAATestUserAuthenticationStatus_Type()
)
rlAAATestUserAuthenticationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAATestUserAuthenticationStatus.setStatus("current")


class _RlAAATestUserAuthenticationAction_Type(Integer32):
    """Custom type rlAAATestUserAuthenticationAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("abort", 4),
          ("begin", 1),
          ("continue", 6),
          ("delete", 5),
          ("receivePassword", 2),
          ("receiveUsername", 3))
    )


_RlAAATestUserAuthenticationAction_Type.__name__ = "Integer32"
_RlAAATestUserAuthenticationAction_Object = MibTableColumn
rlAAATestUserAuthenticationAction = _RlAAATestUserAuthenticationAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 34, 2, 1, 6),
    _RlAAATestUserAuthenticationAction_Type()
)
rlAAATestUserAuthenticationAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAATestUserAuthenticationAction.setStatus("current")


class _RlAAATestUserInput_Type(DisplayString):
    """Custom type rlAAATestUserInput based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_RlAAATestUserInput_Type.__name__ = "DisplayString"
_RlAAATestUserInput_Object = MibTableColumn
rlAAATestUserInput = _RlAAATestUserInput_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 34, 2, 1, 7),
    _RlAAATestUserInput_Type()
)
rlAAATestUserInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAATestUserInput.setStatus("current")
_RlAAATestUserStatus_Type = RowStatus
_RlAAATestUserStatus_Object = MibTableColumn
rlAAATestUserStatus = _RlAAATestUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 34, 2, 1, 8),
    _RlAAATestUserStatus_Type()
)
rlAAATestUserStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAATestUserStatus.setStatus("current")
_RlTacacs_ObjectIdentity = ObjectIdentity
rlTacacs = _RlTacacs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 79, 40)
)
_RlTacacsMibVersion_Type = Integer32
_RlTacacsMibVersion_Object = MibScalar
rlTacacsMibVersion = _RlTacacsMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 40, 1),
    _RlTacacsMibVersion_Type()
)
rlTacacsMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlTacacsMibVersion.setStatus("current")


class _RlTacacsGlobalDefaultTimeout_Type(Integer32):
    """Custom type rlTacacsGlobalDefaultTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_RlTacacsGlobalDefaultTimeout_Type.__name__ = "Integer32"
_RlTacacsGlobalDefaultTimeout_Object = MibScalar
rlTacacsGlobalDefaultTimeout = _RlTacacsGlobalDefaultTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 40, 2),
    _RlTacacsGlobalDefaultTimeout_Type()
)
rlTacacsGlobalDefaultTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTacacsGlobalDefaultTimeout.setStatus("current")


class _RlTacacsGlobalDefaultKey_Type(DisplayString):
    """Custom type rlTacacsGlobalDefaultKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlTacacsGlobalDefaultKey_Type.__name__ = "DisplayString"
_RlTacacsGlobalDefaultKey_Object = MibScalar
rlTacacsGlobalDefaultKey = _RlTacacsGlobalDefaultKey_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 40, 3),
    _RlTacacsGlobalDefaultKey_Type()
)
rlTacacsGlobalDefaultKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTacacsGlobalDefaultKey.setStatus("current")


class _RlTacacsGlobalDefaultSourceIpInterface_Type(IpAddress):
    """Custom type rlTacacsGlobalDefaultSourceIpInterface based on IpAddress"""
    defaultHexValue = "00000000"


_RlTacacsGlobalDefaultSourceIpInterface_Object = MibScalar
rlTacacsGlobalDefaultSourceIpInterface = _RlTacacsGlobalDefaultSourceIpInterface_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 40, 6),
    _RlTacacsGlobalDefaultSourceIpInterface_Type()
)
rlTacacsGlobalDefaultSourceIpInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTacacsGlobalDefaultSourceIpInterface.setStatus("current")
_RlTacacsServerTable_Object = MibTable
rlTacacsServerTable = _RlTacacsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 40, 7)
)
if mibBuilder.loadTexts:
    rlTacacsServerTable.setStatus("current")
_RlTacacsServerEntry_Object = MibTableRow
rlTacacsServerEntry = _RlTacacsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 40, 7, 1)
)
rlTacacsServerEntry.setIndexNames(
    (0, "RADLAN-AAA", "rlTacacsServerAddress"),
)
if mibBuilder.loadTexts:
    rlTacacsServerEntry.setStatus("current")
_RlTacacsServerAddress_Type = IpAddress
_RlTacacsServerAddress_Object = MibTableColumn
rlTacacsServerAddress = _RlTacacsServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 40, 7, 1, 1),
    _RlTacacsServerAddress_Type()
)
rlTacacsServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTacacsServerAddress.setStatus("current")


class _RlTacacsServerPortNumber_Type(Integer32):
    """Custom type rlTacacsServerPortNumber based on Integer32"""
    defaultValue = 49

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlTacacsServerPortNumber_Type.__name__ = "Integer32"
_RlTacacsServerPortNumber_Object = MibTableColumn
rlTacacsServerPortNumber = _RlTacacsServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 40, 7, 1, 2),
    _RlTacacsServerPortNumber_Type()
)
rlTacacsServerPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTacacsServerPortNumber.setStatus("current")


class _RlTacacsServerConnectionType_Type(RlTacacsConnectionType):
    """Custom type rlTacacsServerConnectionType based on RlTacacsConnectionType"""


_RlTacacsServerConnectionType_Object = MibTableColumn
rlTacacsServerConnectionType = _RlTacacsServerConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 40, 7, 1, 3),
    _RlTacacsServerConnectionType_Type()
)
rlTacacsServerConnectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTacacsServerConnectionType.setStatus("current")


class _RlTacacsServerConnectionStatus_Type(RlTacacsConnectionStatus):
    """Custom type rlTacacsServerConnectionStatus based on RlTacacsConnectionStatus"""


_RlTacacsServerConnectionStatus_Object = MibTableColumn
rlTacacsServerConnectionStatus = _RlTacacsServerConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 40, 7, 1, 4),
    _RlTacacsServerConnectionStatus_Type()
)
rlTacacsServerConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlTacacsServerConnectionStatus.setStatus("current")


class _RlTacacsServerTimeout_Type(Integer32):
    """Custom type rlTacacsServerTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_RlTacacsServerTimeout_Type.__name__ = "Integer32"
_RlTacacsServerTimeout_Object = MibTableColumn
rlTacacsServerTimeout = _RlTacacsServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 40, 7, 1, 5),
    _RlTacacsServerTimeout_Type()
)
rlTacacsServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTacacsServerTimeout.setStatus("current")


class _RlTacacsServerUseGlobalDefaultKey_Type(TruthValue):
    """Custom type rlTacacsServerUseGlobalDefaultKey based on TruthValue"""


_RlTacacsServerUseGlobalDefaultKey_Object = MibTableColumn
rlTacacsServerUseGlobalDefaultKey = _RlTacacsServerUseGlobalDefaultKey_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 40, 7, 1, 6),
    _RlTacacsServerUseGlobalDefaultKey_Type()
)
rlTacacsServerUseGlobalDefaultKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTacacsServerUseGlobalDefaultKey.setStatus("current")


class _RlTacacsServerKey_Type(DisplayString):
    """Custom type rlTacacsServerKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlTacacsServerKey_Type.__name__ = "DisplayString"
_RlTacacsServerKey_Object = MibTableColumn
rlTacacsServerKey = _RlTacacsServerKey_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 40, 7, 1, 7),
    _RlTacacsServerKey_Type()
)
rlTacacsServerKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTacacsServerKey.setStatus("current")


class _RlTacacsServerSourceIpInterface_Type(IpAddress):
    """Custom type rlTacacsServerSourceIpInterface based on IpAddress"""
    defaultHexValue = "00000000"


_RlTacacsServerSourceIpInterface_Object = MibTableColumn
rlTacacsServerSourceIpInterface = _RlTacacsServerSourceIpInterface_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 40, 7, 1, 8),
    _RlTacacsServerSourceIpInterface_Type()
)
rlTacacsServerSourceIpInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTacacsServerSourceIpInterface.setStatus("current")


class _RlTacacsServerPriority_Type(Integer32):
    """Custom type rlTacacsServerPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlTacacsServerPriority_Type.__name__ = "Integer32"
_RlTacacsServerPriority_Object = MibTableColumn
rlTacacsServerPriority = _RlTacacsServerPriority_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 40, 7, 1, 9),
    _RlTacacsServerPriority_Type()
)
rlTacacsServerPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTacacsServerPriority.setStatus("current")
_RlTacacsServerRowStatus_Type = RowStatus
_RlTacacsServerRowStatus_Object = MibTableColumn
rlTacacsServerRowStatus = _RlTacacsServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 40, 7, 1, 10),
    _RlTacacsServerRowStatus_Type()
)
rlTacacsServerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTacacsServerRowStatus.setStatus("current")


class _RlTacacsGlobalDefaultSourceIPv6Interface_Type(InetAddressIPv6):
    """Custom type rlTacacsGlobalDefaultSourceIPv6Interface based on InetAddressIPv6"""
    defaultHexValue = "0000000000000000"


_RlTacacsGlobalDefaultSourceIPv6Interface_Object = MibScalar
rlTacacsGlobalDefaultSourceIPv6Interface = _RlTacacsGlobalDefaultSourceIPv6Interface_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 40, 8),
    _RlTacacsGlobalDefaultSourceIPv6Interface_Type()
)
rlTacacsGlobalDefaultSourceIPv6Interface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTacacsGlobalDefaultSourceIPv6Interface.setStatus("current")
_RlTacacsServerInetTable_Object = MibTable
rlTacacsServerInetTable = _RlTacacsServerInetTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 40, 9)
)
if mibBuilder.loadTexts:
    rlTacacsServerInetTable.setStatus("current")
_RlTacacsServerInetEntry_Object = MibTableRow
rlTacacsServerInetEntry = _RlTacacsServerInetEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 40, 9, 1)
)
rlTacacsServerInetEntry.setIndexNames(
    (0, "RADLAN-AAA", "rlTacacsServerInetAddressType"),
    (0, "RADLAN-AAA", "rlTacacsServerInetAddress"),
)
if mibBuilder.loadTexts:
    rlTacacsServerInetEntry.setStatus("current")
_RlTacacsServerInetAddressType_Type = InetAddressType
_RlTacacsServerInetAddressType_Object = MibTableColumn
rlTacacsServerInetAddressType = _RlTacacsServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 40, 9, 1, 1),
    _RlTacacsServerInetAddressType_Type()
)
rlTacacsServerInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTacacsServerInetAddressType.setStatus("current")
_RlTacacsServerInetAddress_Type = InetAddress
_RlTacacsServerInetAddress_Object = MibTableColumn
rlTacacsServerInetAddress = _RlTacacsServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 40, 9, 1, 2),
    _RlTacacsServerInetAddress_Type()
)
rlTacacsServerInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTacacsServerInetAddress.setStatus("current")


class _RlTacacsServerInetPortNumber_Type(Integer32):
    """Custom type rlTacacsServerInetPortNumber based on Integer32"""
    defaultValue = 49

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlTacacsServerInetPortNumber_Type.__name__ = "Integer32"
_RlTacacsServerInetPortNumber_Object = MibTableColumn
rlTacacsServerInetPortNumber = _RlTacacsServerInetPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 40, 9, 1, 3),
    _RlTacacsServerInetPortNumber_Type()
)
rlTacacsServerInetPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTacacsServerInetPortNumber.setStatus("current")


class _RlTacacsServerInetConnectionType_Type(RlTacacsConnectionType):
    """Custom type rlTacacsServerInetConnectionType based on RlTacacsConnectionType"""


_RlTacacsServerInetConnectionType_Object = MibTableColumn
rlTacacsServerInetConnectionType = _RlTacacsServerInetConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 40, 9, 1, 4),
    _RlTacacsServerInetConnectionType_Type()
)
rlTacacsServerInetConnectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTacacsServerInetConnectionType.setStatus("current")


class _RlTacacsServerInetConnectionStatus_Type(RlTacacsConnectionStatus):
    """Custom type rlTacacsServerInetConnectionStatus based on RlTacacsConnectionStatus"""


_RlTacacsServerInetConnectionStatus_Object = MibTableColumn
rlTacacsServerInetConnectionStatus = _RlTacacsServerInetConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 40, 9, 1, 5),
    _RlTacacsServerInetConnectionStatus_Type()
)
rlTacacsServerInetConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlTacacsServerInetConnectionStatus.setStatus("current")


class _RlTacacsServerInetTimeout_Type(Integer32):
    """Custom type rlTacacsServerInetTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_RlTacacsServerInetTimeout_Type.__name__ = "Integer32"
_RlTacacsServerInetTimeout_Object = MibTableColumn
rlTacacsServerInetTimeout = _RlTacacsServerInetTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 40, 9, 1, 6),
    _RlTacacsServerInetTimeout_Type()
)
rlTacacsServerInetTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTacacsServerInetTimeout.setStatus("current")


class _RlTacacsServerInetUseGlobalDefaultKey_Type(TruthValue):
    """Custom type rlTacacsServerInetUseGlobalDefaultKey based on TruthValue"""


_RlTacacsServerInetUseGlobalDefaultKey_Object = MibTableColumn
rlTacacsServerInetUseGlobalDefaultKey = _RlTacacsServerInetUseGlobalDefaultKey_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 40, 9, 1, 7),
    _RlTacacsServerInetUseGlobalDefaultKey_Type()
)
rlTacacsServerInetUseGlobalDefaultKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTacacsServerInetUseGlobalDefaultKey.setStatus("current")


class _RlTacacsServerInetKey_Type(DisplayString):
    """Custom type rlTacacsServerInetKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlTacacsServerInetKey_Type.__name__ = "DisplayString"
_RlTacacsServerInetKey_Object = MibTableColumn
rlTacacsServerInetKey = _RlTacacsServerInetKey_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 40, 9, 1, 8),
    _RlTacacsServerInetKey_Type()
)
rlTacacsServerInetKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTacacsServerInetKey.setStatus("current")
_RlTacacsServerInetSourceInterfaceType_Type = InetAddressType
_RlTacacsServerInetSourceInterfaceType_Object = MibTableColumn
rlTacacsServerInetSourceInterfaceType = _RlTacacsServerInetSourceInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 40, 9, 1, 9),
    _RlTacacsServerInetSourceInterfaceType_Type()
)
rlTacacsServerInetSourceInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTacacsServerInetSourceInterfaceType.setStatus("current")
_RlTacacsServerInetSourceInterface_Type = InetAddress
_RlTacacsServerInetSourceInterface_Object = MibTableColumn
rlTacacsServerInetSourceInterface = _RlTacacsServerInetSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 40, 9, 1, 10),
    _RlTacacsServerInetSourceInterface_Type()
)
rlTacacsServerInetSourceInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTacacsServerInetSourceInterface.setStatus("current")


class _RlTacacsServerInetPriority_Type(Integer32):
    """Custom type rlTacacsServerInetPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlTacacsServerInetPriority_Type.__name__ = "Integer32"
_RlTacacsServerInetPriority_Object = MibTableColumn
rlTacacsServerInetPriority = _RlTacacsServerInetPriority_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 40, 9, 1, 11),
    _RlTacacsServerInetPriority_Type()
)
rlTacacsServerInetPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTacacsServerInetPriority.setStatus("current")
_RlTacacsServerInetRowStatus_Type = RowStatus
_RlTacacsServerInetRowStatus_Object = MibTableColumn
rlTacacsServerInetRowStatus = _RlTacacsServerInetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 40, 9, 1, 12),
    _RlTacacsServerInetRowStatus_Type()
)
rlTacacsServerInetRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTacacsServerInetRowStatus.setStatus("current")


class _RlAAAAuditingEnable_Type(TruthValue):
    """Custom type rlAAAAuditingEnable based on TruthValue"""


_RlAAAAuditingEnable_Object = MibScalar
rlAAAAuditingEnable = _RlAAAAuditingEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 41),
    _RlAAAAuditingEnable_Type()
)
rlAAAAuditingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAAAuditingEnable.setStatus("current")


class _RlAAAMinPasswordLength_Type(Integer32):
    """Custom type rlAAAMinPasswordLength based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_RlAAAMinPasswordLength_Type.__name__ = "Integer32"
_RlAAAMinPasswordLength_Object = MibScalar
rlAAAMinPasswordLength = _RlAAAMinPasswordLength_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 42),
    _RlAAAMinPasswordLength_Type()
)
rlAAAMinPasswordLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAAMinPasswordLength.setStatus("current")


class _RlAAAPasswordHistSize_Type(Unsigned32):
    """Custom type rlAAAPasswordHistSize based on Unsigned32"""
    defaultValue = 0


_RlAAAPasswordHistSize_Object = MibScalar
rlAAAPasswordHistSize = _RlAAAPasswordHistSize_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 43),
    _RlAAAPasswordHistSize_Type()
)
rlAAAPasswordHistSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAAPasswordHistSize.setStatus("current")


class _RlAAAPasswordHistHoldTime_Type(Unsigned32):
    """Custom type rlAAAPasswordHistHoldTime based on Unsigned32"""
    defaultValue = 0


_RlAAAPasswordHistHoldTime_Object = MibScalar
rlAAAPasswordHistHoldTime = _RlAAAPasswordHistHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 44),
    _RlAAAPasswordHistHoldTime_Type()
)
rlAAAPasswordHistHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAAPasswordHistHoldTime.setStatus("current")


class _RlAAASuccLoginWriteToFile_Type(TruthValue):
    """Custom type rlAAASuccLoginWriteToFile based on TruthValue"""


_RlAAASuccLoginWriteToFile_Object = MibScalar
rlAAASuccLoginWriteToFile = _RlAAASuccLoginWriteToFile_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 45),
    _RlAAASuccLoginWriteToFile_Type()
)
rlAAASuccLoginWriteToFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAASuccLoginWriteToFile.setStatus("current")
_RlAAALocalLoginHistTable_Object = MibTable
rlAAALocalLoginHistTable = _RlAAALocalLoginHistTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 46)
)
if mibBuilder.loadTexts:
    rlAAALocalLoginHistTable.setStatus("current")
_RlAAALocalLoginHistEntry_Object = MibTableRow
rlAAALocalLoginHistEntry = _RlAAALocalLoginHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 46, 1)
)
rlAAALocalLoginHistEntry.setIndexNames(
    (0, "RADLAN-AAA", "rlAAALocalLoginHistName"),
    (0, "RADLAN-AAA", "rlAAALocalLoginHistIndex"),
)
if mibBuilder.loadTexts:
    rlAAALocalLoginHistEntry.setStatus("current")
_RlAAALocalLoginHistName_Type = DisplayString
_RlAAALocalLoginHistName_Object = MibTableColumn
rlAAALocalLoginHistName = _RlAAALocalLoginHistName_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 46, 1, 1),
    _RlAAALocalLoginHistName_Type()
)
rlAAALocalLoginHistName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAALocalLoginHistName.setStatus("current")


class _RlAAALocalLoginHistIndex_Type(Unsigned32):
    """Custom type rlAAALocalLoginHistIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RlAAALocalLoginHistIndex_Type.__name__ = "Unsigned32"
_RlAAALocalLoginHistIndex_Object = MibTableColumn
rlAAALocalLoginHistIndex = _RlAAALocalLoginHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 46, 1, 2),
    _RlAAALocalLoginHistIndex_Type()
)
rlAAALocalLoginHistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlAAALocalLoginHistIndex.setStatus("current")
_RlAAALocalLoginHistServiceType_Type = RlAAAServiceType
_RlAAALocalLoginHistServiceType_Object = MibTableColumn
rlAAALocalLoginHistServiceType = _RlAAALocalLoginHistServiceType_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 46, 1, 3),
    _RlAAALocalLoginHistServiceType_Type()
)
rlAAALocalLoginHistServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAALocalLoginHistServiceType.setStatus("current")
_RlAAALocalLoginHistRemoteIpAddress_Type = IpAddress
_RlAAALocalLoginHistRemoteIpAddress_Object = MibTableColumn
rlAAALocalLoginHistRemoteIpAddress = _RlAAALocalLoginHistRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 46, 1, 4),
    _RlAAALocalLoginHistRemoteIpAddress_Type()
)
rlAAALocalLoginHistRemoteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAALocalLoginHistRemoteIpAddress.setStatus("current")
_RlAAALocalLoginHistLocalIpAddress_Type = IpAddress
_RlAAALocalLoginHistLocalIpAddress_Object = MibTableColumn
rlAAALocalLoginHistLocalIpAddress = _RlAAALocalLoginHistLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 46, 1, 5),
    _RlAAALocalLoginHistLocalIpAddress_Type()
)
rlAAALocalLoginHistLocalIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAALocalLoginHistLocalIpAddress.setStatus("current")
_RlAAALocalLoginDateTime_Type = DisplayString
_RlAAALocalLoginDateTime_Object = MibTableColumn
rlAAALocalLoginDateTime = _RlAAALocalLoginDateTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 46, 1, 6),
    _RlAAALocalLoginDateTime_Type()
)
rlAAALocalLoginDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAALocalLoginDateTime.setStatus("current")
_RlAAALocalLoginMrid_Type = Unsigned32
_RlAAALocalLoginMrid_Object = MibTableColumn
rlAAALocalLoginMrid = _RlAAALocalLoginMrid_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 46, 1, 7),
    _RlAAALocalLoginMrid_Type()
)
rlAAALocalLoginMrid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAALocalLoginMrid.setStatus("current")
_RlAAALinePassLoginHistTable_Object = MibTable
rlAAALinePassLoginHistTable = _RlAAALinePassLoginHistTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 47)
)
if mibBuilder.loadTexts:
    rlAAALinePassLoginHistTable.setStatus("current")
_RlAAALinePassLoginHistEntry_Object = MibTableRow
rlAAALinePassLoginHistEntry = _RlAAALinePassLoginHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 47, 1)
)
rlAAALinePassLoginHistEntry.setIndexNames(
    (0, "RADLAN-AAA", "rlAAALinePassLoginHistPortType"),
    (0, "RADLAN-AAA", "rlAAALinePassLoginHistIfIndex"),
    (0, "RADLAN-AAA", "rlAAALinePassLoginHistServiceType"),
    (0, "RADLAN-AAA", "rlAAALinePassLoginHistIndex"),
)
if mibBuilder.loadTexts:
    rlAAALinePassLoginHistEntry.setStatus("current")
_RlAAALinePassLoginHistPortType_Type = RlAAALinePortType
_RlAAALinePassLoginHistPortType_Object = MibTableColumn
rlAAALinePassLoginHistPortType = _RlAAALinePassLoginHistPortType_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 47, 1, 1),
    _RlAAALinePassLoginHistPortType_Type()
)
rlAAALinePassLoginHistPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAALinePassLoginHistPortType.setStatus("current")
_RlAAALinePassLoginHistIfIndex_Type = Unsigned32
_RlAAALinePassLoginHistIfIndex_Object = MibTableColumn
rlAAALinePassLoginHistIfIndex = _RlAAALinePassLoginHistIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 47, 1, 2),
    _RlAAALinePassLoginHistIfIndex_Type()
)
rlAAALinePassLoginHistIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAALinePassLoginHistIfIndex.setStatus("current")
_RlAAALinePassLoginHistServiceType_Type = RlAAAServiceType
_RlAAALinePassLoginHistServiceType_Object = MibTableColumn
rlAAALinePassLoginHistServiceType = _RlAAALinePassLoginHistServiceType_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 47, 1, 3),
    _RlAAALinePassLoginHistServiceType_Type()
)
rlAAALinePassLoginHistServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAALinePassLoginHistServiceType.setStatus("current")


class _RlAAALinePassLoginHistIndex_Type(Unsigned32):
    """Custom type rlAAALinePassLoginHistIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RlAAALinePassLoginHistIndex_Type.__name__ = "Unsigned32"
_RlAAALinePassLoginHistIndex_Object = MibTableColumn
rlAAALinePassLoginHistIndex = _RlAAALinePassLoginHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 47, 1, 4),
    _RlAAALinePassLoginHistIndex_Type()
)
rlAAALinePassLoginHistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlAAALinePassLoginHistIndex.setStatus("current")
_RlAAALinePassLoginHistActServiceType_Type = RlAAAServiceType
_RlAAALinePassLoginHistActServiceType_Object = MibTableColumn
rlAAALinePassLoginHistActServiceType = _RlAAALinePassLoginHistActServiceType_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 47, 1, 5),
    _RlAAALinePassLoginHistActServiceType_Type()
)
rlAAALinePassLoginHistActServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAALinePassLoginHistActServiceType.setStatus("current")
_RlAAALinePassLoginHistRemoteIpAddress_Type = IpAddress
_RlAAALinePassLoginHistRemoteIpAddress_Object = MibTableColumn
rlAAALinePassLoginHistRemoteIpAddress = _RlAAALinePassLoginHistRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 47, 1, 6),
    _RlAAALinePassLoginHistRemoteIpAddress_Type()
)
rlAAALinePassLoginHistRemoteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAALinePassLoginHistRemoteIpAddress.setStatus("current")
_RlAAALinePassLoginHistLocalIpAddress_Type = IpAddress
_RlAAALinePassLoginHistLocalIpAddress_Object = MibTableColumn
rlAAALinePassLoginHistLocalIpAddress = _RlAAALinePassLoginHistLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 47, 1, 7),
    _RlAAALinePassLoginHistLocalIpAddress_Type()
)
rlAAALinePassLoginHistLocalIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAALinePassLoginHistLocalIpAddress.setStatus("current")
_RlAAALinePassLoginDateTime_Type = DisplayString
_RlAAALinePassLoginDateTime_Object = MibTableColumn
rlAAALinePassLoginDateTime = _RlAAALinePassLoginDateTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 47, 1, 8),
    _RlAAALinePassLoginDateTime_Type()
)
rlAAALinePassLoginDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAALinePassLoginDateTime.setStatus("current")
_RlAAALinePassLoginMrid_Type = Unsigned32
_RlAAALinePassLoginMrid_Object = MibTableColumn
rlAAALinePassLoginMrid = _RlAAALinePassLoginMrid_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 47, 1, 9),
    _RlAAALinePassLoginMrid_Type()
)
rlAAALinePassLoginMrid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAALinePassLoginMrid.setStatus("current")
_RlAAASystemLoginHistTable_Object = MibTable
rlAAASystemLoginHistTable = _RlAAASystemLoginHistTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 48)
)
if mibBuilder.loadTexts:
    rlAAASystemLoginHistTable.setStatus("current")
_RlAAASystemLoginHistEntry_Object = MibTableRow
rlAAASystemLoginHistEntry = _RlAAASystemLoginHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 48, 1)
)
rlAAASystemLoginHistEntry.setIndexNames(
    (0, "RADLAN-AAA", "rlAAASystemLoginHistLevel"),
    (0, "RADLAN-AAA", "rlAAASystemLoginHistIndex"),
)
if mibBuilder.loadTexts:
    rlAAASystemLoginHistEntry.setStatus("current")


class _RlAAASystemLoginHistLevel_Type(Integer32):
    """Custom type rlAAASystemLoginHistLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RlAAASystemLoginHistLevel_Type.__name__ = "Integer32"
_RlAAASystemLoginHistLevel_Object = MibTableColumn
rlAAASystemLoginHistLevel = _RlAAASystemLoginHistLevel_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 48, 1, 1),
    _RlAAASystemLoginHistLevel_Type()
)
rlAAASystemLoginHistLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAASystemLoginHistLevel.setStatus("current")


class _RlAAASystemLoginHistIndex_Type(Unsigned32):
    """Custom type rlAAASystemLoginHistIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RlAAASystemLoginHistIndex_Type.__name__ = "Unsigned32"
_RlAAASystemLoginHistIndex_Object = MibTableColumn
rlAAASystemLoginHistIndex = _RlAAASystemLoginHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 48, 1, 2),
    _RlAAASystemLoginHistIndex_Type()
)
rlAAASystemLoginHistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlAAASystemLoginHistIndex.setStatus("current")
_RlAAASystemLoginHistServiceType_Type = RlAAAServiceType
_RlAAASystemLoginHistServiceType_Object = MibTableColumn
rlAAASystemLoginHistServiceType = _RlAAASystemLoginHistServiceType_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 48, 1, 3),
    _RlAAASystemLoginHistServiceType_Type()
)
rlAAASystemLoginHistServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAASystemLoginHistServiceType.setStatus("current")
_RlAAASystemLoginHistRemoteIpAddress_Type = IpAddress
_RlAAASystemLoginHistRemoteIpAddress_Object = MibTableColumn
rlAAASystemLoginHistRemoteIpAddress = _RlAAASystemLoginHistRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 48, 1, 4),
    _RlAAASystemLoginHistRemoteIpAddress_Type()
)
rlAAASystemLoginHistRemoteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAASystemLoginHistRemoteIpAddress.setStatus("current")
_RlAAASystemLoginHistLocalIpAddress_Type = IpAddress
_RlAAASystemLoginHistLocalIpAddress_Object = MibTableColumn
rlAAASystemLoginHistLocalIpAddress = _RlAAASystemLoginHistLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 48, 1, 5),
    _RlAAASystemLoginHistLocalIpAddress_Type()
)
rlAAASystemLoginHistLocalIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAASystemLoginHistLocalIpAddress.setStatus("current")
_RlAAASystemLoginDateTime_Type = DisplayString
_RlAAASystemLoginDateTime_Object = MibTableColumn
rlAAASystemLoginDateTime = _RlAAASystemLoginDateTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 48, 1, 6),
    _RlAAASystemLoginDateTime_Type()
)
rlAAASystemLoginDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAASystemLoginDateTime.setStatus("current")
_RlAAASystemLoginMrid_Type = Unsigned32
_RlAAASystemLoginMrid_Object = MibTableColumn
rlAAASystemLoginMrid = _RlAAASystemLoginMrid_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 48, 1, 7),
    _RlAAASystemLoginMrid_Type()
)
rlAAASystemLoginMrid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAASystemLoginMrid.setStatus("current")
_RlAAASysPassStatTable_Object = MibTable
rlAAASysPassStatTable = _RlAAASysPassStatTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 49)
)
if mibBuilder.loadTexts:
    rlAAASysPassStatTable.setStatus("current")
_RlAAASysPassStatEntry_Object = MibTableRow
rlAAASysPassStatEntry = _RlAAASysPassStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 49, 1)
)
rlAAASysPassStatEntry.setIndexNames(
    (0, "RADLAN-AAA", "rlAAASysPassStatLevel"),
)
if mibBuilder.loadTexts:
    rlAAASysPassStatEntry.setStatus("current")


class _RlAAASysPassStatLevel_Type(Integer32):
    """Custom type rlAAASysPassStatLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RlAAASysPassStatLevel_Type.__name__ = "Integer32"
_RlAAASysPassStatLevel_Object = MibTableColumn
rlAAASysPassStatLevel = _RlAAASysPassStatLevel_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 49, 1, 1),
    _RlAAASysPassStatLevel_Type()
)
rlAAASysPassStatLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAASysPassStatLevel.setStatus("current")


class _RlAAASysPassStatLockedState_Type(Integer32):
    """Custom type rlAAASysPassStatLockedState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("usable", 1))
    )


_RlAAASysPassStatLockedState_Type.__name__ = "Integer32"
_RlAAASysPassStatLockedState_Object = MibTableColumn
rlAAASysPassStatLockedState = _RlAAASysPassStatLockedState_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 49, 1, 2),
    _RlAAASysPassStatLockedState_Type()
)
rlAAASysPassStatLockedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAASysPassStatLockedState.setStatus("current")
_RlAAASysPassStatConsFailedLogins_Type = Counter32
_RlAAASysPassStatConsFailedLogins_Object = MibTableColumn
rlAAASysPassStatConsFailedLogins = _RlAAASysPassStatConsFailedLogins_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 49, 1, 3),
    _RlAAASysPassStatConsFailedLogins_Type()
)
rlAAASysPassStatConsFailedLogins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAASysPassStatConsFailedLogins.setStatus("current")


class _RlAAASysPassStatPasswordValidTime_Type(Unsigned32):
    """Custom type rlAAASysPassStatPasswordValidTime based on Unsigned32"""
    defaultValue = 0


_RlAAASysPassStatPasswordValidTime_Object = MibTableColumn
rlAAASysPassStatPasswordValidTime = _RlAAASysPassStatPasswordValidTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 49, 1, 4),
    _RlAAASysPassStatPasswordValidTime_Type()
)
rlAAASysPassStatPasswordValidTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAASysPassStatPasswordValidTime.setStatus("current")
_RlAAASysPassStatPasswordExpieryDate_Type = DisplayString
_RlAAASysPassStatPasswordExpieryDate_Object = MibTableColumn
rlAAASysPassStatPasswordExpieryDate = _RlAAASysPassStatPasswordExpieryDate_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 49, 1, 5),
    _RlAAASysPassStatPasswordExpieryDate_Type()
)
rlAAASysPassStatPasswordExpieryDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAASysPassStatPasswordExpieryDate.setStatus("current")


class _RlAAAMaxNumLogAttmpts_Type(Integer32):
    """Custom type rlAAAMaxNumLogAttmpts based on Integer32"""
    defaultValue = 0


_RlAAAMaxNumLogAttmpts_Object = MibScalar
rlAAAMaxNumLogAttmpts = _RlAAAMaxNumLogAttmpts_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 50),
    _RlAAAMaxNumLogAttmpts_Type()
)
rlAAAMaxNumLogAttmpts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAAMaxNumLogAttmpts.setStatus("current")


class _RlAAAUnlockUserName_Type(DisplayString):
    """Custom type rlAAAUnlockUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RlAAAUnlockUserName_Type.__name__ = "DisplayString"
_RlAAAUnlockUserName_Object = MibScalar
rlAAAUnlockUserName = _RlAAAUnlockUserName_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 51),
    _RlAAAUnlockUserName_Type()
)
rlAAAUnlockUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAAUnlockUserName.setStatus("current")


class _RlAAAUnlockSystemPassword_Type(Integer32):
    """Custom type rlAAAUnlockSystemPassword based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RlAAAUnlockSystemPassword_Type.__name__ = "Integer32"
_RlAAAUnlockSystemPassword_Object = MibScalar
rlAAAUnlockSystemPassword = _RlAAAUnlockSystemPassword_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 52),
    _RlAAAUnlockSystemPassword_Type()
)
rlAAAUnlockSystemPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAAUnlockSystemPassword.setStatus("current")
_RlAAALockedLineTable_Object = MibTable
rlAAALockedLineTable = _RlAAALockedLineTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 53)
)
if mibBuilder.loadTexts:
    rlAAALockedLineTable.setStatus("current")
_RlAAALockedLineEntry_Object = MibTableRow
rlAAALockedLineEntry = _RlAAALockedLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 53, 1)
)
rlAAALockedLineEntry.setIndexNames(
    (0, "RADLAN-AAA", "rlAAALockedLinePortType"),
    (0, "RADLAN-AAA", "rlAAALockedLineIfIndex"),
    (0, "RADLAN-AAA", "rlAAALockedLineServiceType"),
)
if mibBuilder.loadTexts:
    rlAAALockedLineEntry.setStatus("current")
_RlAAALockedLinePortType_Type = RlAAALinePortType
_RlAAALockedLinePortType_Object = MibTableColumn
rlAAALockedLinePortType = _RlAAALockedLinePortType_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 53, 1, 1),
    _RlAAALockedLinePortType_Type()
)
rlAAALockedLinePortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAALockedLinePortType.setStatus("current")
_RlAAALockedLineIfIndex_Type = Unsigned32
_RlAAALockedLineIfIndex_Object = MibTableColumn
rlAAALockedLineIfIndex = _RlAAALockedLineIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 53, 1, 2),
    _RlAAALockedLineIfIndex_Type()
)
rlAAALockedLineIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAALockedLineIfIndex.setStatus("current")
_RlAAALockedLineServiceType_Type = RlAAAServiceType
_RlAAALockedLineServiceType_Object = MibTableColumn
rlAAALockedLineServiceType = _RlAAALockedLineServiceType_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 53, 1, 3),
    _RlAAALockedLineServiceType_Type()
)
rlAAALockedLineServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAALockedLineServiceType.setStatus("current")


class _RlAAALockedLineStatus_Type(Integer32):
    """Custom type rlAAALockedLineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("usable", 1))
    )


_RlAAALockedLineStatus_Type.__name__ = "Integer32"
_RlAAALockedLineStatus_Object = MibTableColumn
rlAAALockedLineStatus = _RlAAALockedLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 53, 1, 4),
    _RlAAALockedLineStatus_Type()
)
rlAAALockedLineStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAALockedLineStatus.setStatus("current")
_RlAAASystemPasswordVerificationAndSettingTable_Object = MibTable
rlAAASystemPasswordVerificationAndSettingTable = _RlAAASystemPasswordVerificationAndSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 54)
)
if mibBuilder.loadTexts:
    rlAAASystemPasswordVerificationAndSettingTable.setStatus("current")
_RlAAASystemPasswordVerificationAndSettingEntry_Object = MibTableRow
rlAAASystemPasswordVerificationAndSettingEntry = _RlAAASystemPasswordVerificationAndSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 54, 1)
)
rlAAASystemPasswordVerificationAndSettingEntry.setIndexNames(
    (0, "RADLAN-AAA", "rlAAASystemPasswordSettingPrivilegeLevel"),
)
if mibBuilder.loadTexts:
    rlAAASystemPasswordVerificationAndSettingEntry.setStatus("current")


class _RlAAASystemPasswordSettingPrivilegeLevel_Type(Integer32):
    """Custom type rlAAASystemPasswordSettingPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RlAAASystemPasswordSettingPrivilegeLevel_Type.__name__ = "Integer32"
_RlAAASystemPasswordSettingPrivilegeLevel_Object = MibTableColumn
rlAAASystemPasswordSettingPrivilegeLevel = _RlAAASystemPasswordSettingPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 54, 1, 1),
    _RlAAASystemPasswordSettingPrivilegeLevel_Type()
)
rlAAASystemPasswordSettingPrivilegeLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlAAASystemPasswordSettingPrivilegeLevel.setStatus("current")
_RlAAASystemPasswordVerificationOldPassword_Type = DisplayString
_RlAAASystemPasswordVerificationOldPassword_Object = MibTableColumn
rlAAASystemPasswordVerificationOldPassword = _RlAAASystemPasswordVerificationOldPassword_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 54, 1, 2),
    _RlAAASystemPasswordVerificationOldPassword_Type()
)
rlAAASystemPasswordVerificationOldPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAASystemPasswordVerificationOldPassword.setStatus("current")
_RlAAASystemPasswordSettingNewPassword_Type = DisplayString
_RlAAASystemPasswordSettingNewPassword_Object = MibTableColumn
rlAAASystemPasswordSettingNewPassword = _RlAAASystemPasswordSettingNewPassword_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 54, 1, 3),
    _RlAAASystemPasswordSettingNewPassword_Type()
)
rlAAASystemPasswordSettingNewPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAASystemPasswordSettingNewPassword.setStatus("current")
_RlAAASystemPasswordConfirmNewPassword_Type = DisplayString
_RlAAASystemPasswordConfirmNewPassword_Object = MibTableColumn
rlAAASystemPasswordConfirmNewPassword = _RlAAASystemPasswordConfirmNewPassword_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 54, 1, 4),
    _RlAAASystemPasswordConfirmNewPassword_Type()
)
rlAAASystemPasswordConfirmNewPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAASystemPasswordConfirmNewPassword.setStatus("current")
_RlAAAAccountingMngMethod_Type = RlAAAAccountingMethod
_RlAAAAccountingMngMethod_Object = MibScalar
rlAAAAccountingMngMethod = _RlAAAAccountingMngMethod_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 55),
    _RlAAAAccountingMngMethod_Type()
)
rlAAAAccountingMngMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAAAccountingMngMethod.setStatus("current")
_RlAAAAccountingDot1xMethod_Type = RlAAAAccountingMethod
_RlAAAAccountingDot1xMethod_Object = MibScalar
rlAAAAccountingDot1xMethod = _RlAAAAccountingDot1xMethod_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 56),
    _RlAAAAccountingDot1xMethod_Type()
)
rlAAAAccountingDot1xMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAAAccountingDot1xMethod.setStatus("current")
_RlAAAUserInetTable_Object = MibTable
rlAAAUserInetTable = _RlAAAUserInetTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 57)
)
if mibBuilder.loadTexts:
    rlAAAUserInetTable.setStatus("current")
_RlAAAUserInetEntry_Object = MibTableRow
rlAAAUserInetEntry = _RlAAAUserInetEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 57, 1)
)
rlAAAUserInetEntry.setIndexNames(
    (0, "RADLAN-AAA", "rlAAAUserInetIndex"),
)
if mibBuilder.loadTexts:
    rlAAAUserInetEntry.setStatus("current")
_RlAAAUserInetIndex_Type = Unsigned32
_RlAAAUserInetIndex_Object = MibTableColumn
rlAAAUserInetIndex = _RlAAAUserInetIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 57, 1, 1),
    _RlAAAUserInetIndex_Type()
)
rlAAAUserInetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlAAAUserInetIndex.setStatus("current")
_RlAAAUserInetServiceType_Type = RlAAAServiceType
_RlAAAUserInetServiceType_Object = MibTableColumn
rlAAAUserInetServiceType = _RlAAAUserInetServiceType_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 57, 1, 2),
    _RlAAAUserInetServiceType_Type()
)
rlAAAUserInetServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAAUserInetServiceType.setStatus("current")
_RlAAAUserInetRemoteIpAddressType_Type = InetAddressType
_RlAAAUserInetRemoteIpAddressType_Object = MibTableColumn
rlAAAUserInetRemoteIpAddressType = _RlAAAUserInetRemoteIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 57, 1, 3),
    _RlAAAUserInetRemoteIpAddressType_Type()
)
rlAAAUserInetRemoteIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAAUserInetRemoteIpAddressType.setStatus("current")
_RlAAAUserInetRemoteIpAddress_Type = InetAddress
_RlAAAUserInetRemoteIpAddress_Object = MibTableColumn
rlAAAUserInetRemoteIpAddress = _RlAAAUserInetRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 57, 1, 4),
    _RlAAAUserInetRemoteIpAddress_Type()
)
rlAAAUserInetRemoteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAAUserInetRemoteIpAddress.setStatus("current")
_RlAAAUserInetName_Type = DisplayString
_RlAAAUserInetName_Object = MibTableColumn
rlAAAUserInetName = _RlAAAUserInetName_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 57, 1, 5),
    _RlAAAUserInetName_Type()
)
rlAAAUserInetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAAUserInetName.setStatus("current")


class _RlAAAUserInetLevel_Type(Unsigned32):
    """Custom type rlAAAUserInetLevel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RlAAAUserInetLevel_Type.__name__ = "Unsigned32"
_RlAAAUserInetLevel_Object = MibTableColumn
rlAAAUserInetLevel = _RlAAAUserInetLevel_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 57, 1, 6),
    _RlAAAUserInetLevel_Type()
)
rlAAAUserInetLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAAUserInetLevel.setStatus("current")
_RlAAAUserInetIfIndex_Type = Unsigned32
_RlAAAUserInetIfIndex_Object = MibTableColumn
rlAAAUserInetIfIndex = _RlAAAUserInetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 57, 1, 7),
    _RlAAAUserInetIfIndex_Type()
)
rlAAAUserInetIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAAUserInetIfIndex.setStatus("current")
_RlAAAUserInetLoginDate_Type = DateAndTime
_RlAAAUserInetLoginDate_Object = MibTableColumn
rlAAAUserInetLoginDate = _RlAAAUserInetLoginDate_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 57, 1, 8),
    _RlAAAUserInetLoginDate_Type()
)
rlAAAUserInetLoginDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAAUserInetLoginDate.setStatus("current")
_RlAAAUserInetLoginDurationMS_Type = Unsigned32
_RlAAAUserInetLoginDurationMS_Object = MibTableColumn
rlAAAUserInetLoginDurationMS = _RlAAAUserInetLoginDurationMS_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 57, 1, 9),
    _RlAAAUserInetLoginDurationMS_Type()
)
rlAAAUserInetLoginDurationMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAAUserInetLoginDurationMS.setStatus("current")
_RlAAALocalLoginHistInetTable_Object = MibTable
rlAAALocalLoginHistInetTable = _RlAAALocalLoginHistInetTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 58)
)
if mibBuilder.loadTexts:
    rlAAALocalLoginHistInetTable.setStatus("current")
_RlAAALocalLoginHistInetEntry_Object = MibTableRow
rlAAALocalLoginHistInetEntry = _RlAAALocalLoginHistInetEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 58, 1)
)
rlAAALocalLoginHistInetEntry.setIndexNames(
    (0, "RADLAN-AAA", "rlAAALocalLoginHistInetName"),
    (0, "RADLAN-AAA", "rlAAALocalLoginHistInetIndex"),
)
if mibBuilder.loadTexts:
    rlAAALocalLoginHistInetEntry.setStatus("current")
_RlAAALocalLoginHistInetName_Type = DisplayString
_RlAAALocalLoginHistInetName_Object = MibTableColumn
rlAAALocalLoginHistInetName = _RlAAALocalLoginHistInetName_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 58, 1, 1),
    _RlAAALocalLoginHistInetName_Type()
)
rlAAALocalLoginHistInetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAALocalLoginHistInetName.setStatus("current")


class _RlAAALocalLoginHistInetIndex_Type(Unsigned32):
    """Custom type rlAAALocalLoginHistInetIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RlAAALocalLoginHistInetIndex_Type.__name__ = "Unsigned32"
_RlAAALocalLoginHistInetIndex_Object = MibTableColumn
rlAAALocalLoginHistInetIndex = _RlAAALocalLoginHistInetIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 58, 1, 2),
    _RlAAALocalLoginHistInetIndex_Type()
)
rlAAALocalLoginHistInetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlAAALocalLoginHistInetIndex.setStatus("current")
_RlAAALocalLoginHistInetServiceType_Type = RlAAAServiceType
_RlAAALocalLoginHistInetServiceType_Object = MibTableColumn
rlAAALocalLoginHistInetServiceType = _RlAAALocalLoginHistInetServiceType_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 58, 1, 3),
    _RlAAALocalLoginHistInetServiceType_Type()
)
rlAAALocalLoginHistInetServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAALocalLoginHistInetServiceType.setStatus("current")
_RlAAALocalLoginHistInetRemoteIpAddressType_Type = InetAddressType
_RlAAALocalLoginHistInetRemoteIpAddressType_Object = MibTableColumn
rlAAALocalLoginHistInetRemoteIpAddressType = _RlAAALocalLoginHistInetRemoteIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 58, 1, 4),
    _RlAAALocalLoginHistInetRemoteIpAddressType_Type()
)
rlAAALocalLoginHistInetRemoteIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAALocalLoginHistInetRemoteIpAddressType.setStatus("current")
_RlAAALocalLoginHistInetRemoteIpAddress_Type = InetAddress
_RlAAALocalLoginHistInetRemoteIpAddress_Object = MibTableColumn
rlAAALocalLoginHistInetRemoteIpAddress = _RlAAALocalLoginHistInetRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 58, 1, 5),
    _RlAAALocalLoginHistInetRemoteIpAddress_Type()
)
rlAAALocalLoginHistInetRemoteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAALocalLoginHistInetRemoteIpAddress.setStatus("current")
_RlAAALocalLoginHistInetLocalIpAddressType_Type = InetAddressType
_RlAAALocalLoginHistInetLocalIpAddressType_Object = MibTableColumn
rlAAALocalLoginHistInetLocalIpAddressType = _RlAAALocalLoginHistInetLocalIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 58, 1, 6),
    _RlAAALocalLoginHistInetLocalIpAddressType_Type()
)
rlAAALocalLoginHistInetLocalIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAALocalLoginHistInetLocalIpAddressType.setStatus("current")
_RlAAALocalLoginHistInetLocalIpAddress_Type = InetAddress
_RlAAALocalLoginHistInetLocalIpAddress_Object = MibTableColumn
rlAAALocalLoginHistInetLocalIpAddress = _RlAAALocalLoginHistInetLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 58, 1, 7),
    _RlAAALocalLoginHistInetLocalIpAddress_Type()
)
rlAAALocalLoginHistInetLocalIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAALocalLoginHistInetLocalIpAddress.setStatus("current")
_RlAAALocalLoginHistInetDateTime_Type = DisplayString
_RlAAALocalLoginHistInetDateTime_Object = MibTableColumn
rlAAALocalLoginHistInetDateTime = _RlAAALocalLoginHistInetDateTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 58, 1, 8),
    _RlAAALocalLoginHistInetDateTime_Type()
)
rlAAALocalLoginHistInetDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAALocalLoginHistInetDateTime.setStatus("current")
_RlAAALocalLoginHistInetMrid_Type = Unsigned32
_RlAAALocalLoginHistInetMrid_Object = MibTableColumn
rlAAALocalLoginHistInetMrid = _RlAAALocalLoginHistInetMrid_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 58, 1, 9),
    _RlAAALocalLoginHistInetMrid_Type()
)
rlAAALocalLoginHistInetMrid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAALocalLoginHistInetMrid.setStatus("current")
_RlAAALinePassLoginHistInetTable_Object = MibTable
rlAAALinePassLoginHistInetTable = _RlAAALinePassLoginHistInetTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 59)
)
if mibBuilder.loadTexts:
    rlAAALinePassLoginHistInetTable.setStatus("current")
_RlAAALinePassLoginHistInetEntry_Object = MibTableRow
rlAAALinePassLoginHistInetEntry = _RlAAALinePassLoginHistInetEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 59, 1)
)
rlAAALinePassLoginHistInetEntry.setIndexNames(
    (0, "RADLAN-AAA", "rlAAALinePassLoginHistInetPortType"),
    (0, "RADLAN-AAA", "rlAAALinePassLoginHistInetIfIndex"),
    (0, "RADLAN-AAA", "rlAAALinePassLoginHistInetServiceType"),
    (0, "RADLAN-AAA", "rlAAALinePassLoginHistInetIndex"),
)
if mibBuilder.loadTexts:
    rlAAALinePassLoginHistInetEntry.setStatus("current")
_RlAAALinePassLoginHistInetPortType_Type = RlAAALinePortType
_RlAAALinePassLoginHistInetPortType_Object = MibTableColumn
rlAAALinePassLoginHistInetPortType = _RlAAALinePassLoginHistInetPortType_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 59, 1, 1),
    _RlAAALinePassLoginHistInetPortType_Type()
)
rlAAALinePassLoginHistInetPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAALinePassLoginHistInetPortType.setStatus("current")
_RlAAALinePassLoginHistInetIfIndex_Type = Unsigned32
_RlAAALinePassLoginHistInetIfIndex_Object = MibTableColumn
rlAAALinePassLoginHistInetIfIndex = _RlAAALinePassLoginHistInetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 59, 1, 2),
    _RlAAALinePassLoginHistInetIfIndex_Type()
)
rlAAALinePassLoginHistInetIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAALinePassLoginHistInetIfIndex.setStatus("current")
_RlAAALinePassLoginHistInetServiceType_Type = RlAAAServiceType
_RlAAALinePassLoginHistInetServiceType_Object = MibTableColumn
rlAAALinePassLoginHistInetServiceType = _RlAAALinePassLoginHistInetServiceType_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 59, 1, 3),
    _RlAAALinePassLoginHistInetServiceType_Type()
)
rlAAALinePassLoginHistInetServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAALinePassLoginHistInetServiceType.setStatus("current")


class _RlAAALinePassLoginHistInetIndex_Type(Unsigned32):
    """Custom type rlAAALinePassLoginHistInetIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RlAAALinePassLoginHistInetIndex_Type.__name__ = "Unsigned32"
_RlAAALinePassLoginHistInetIndex_Object = MibTableColumn
rlAAALinePassLoginHistInetIndex = _RlAAALinePassLoginHistInetIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 59, 1, 4),
    _RlAAALinePassLoginHistInetIndex_Type()
)
rlAAALinePassLoginHistInetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlAAALinePassLoginHistInetIndex.setStatus("current")
_RlAAALinePassLoginHistInetActServiceType_Type = RlAAAServiceType
_RlAAALinePassLoginHistInetActServiceType_Object = MibTableColumn
rlAAALinePassLoginHistInetActServiceType = _RlAAALinePassLoginHistInetActServiceType_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 59, 1, 5),
    _RlAAALinePassLoginHistInetActServiceType_Type()
)
rlAAALinePassLoginHistInetActServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAALinePassLoginHistInetActServiceType.setStatus("current")
_RlAAALinePassLoginHistInetRemoteInetAddressType_Type = InetAddressType
_RlAAALinePassLoginHistInetRemoteInetAddressType_Object = MibTableColumn
rlAAALinePassLoginHistInetRemoteInetAddressType = _RlAAALinePassLoginHistInetRemoteInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 59, 1, 6),
    _RlAAALinePassLoginHistInetRemoteInetAddressType_Type()
)
rlAAALinePassLoginHistInetRemoteInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAALinePassLoginHistInetRemoteInetAddressType.setStatus("current")
_RlAAALinePassLoginHistInetRemoteInetAddress_Type = InetAddress
_RlAAALinePassLoginHistInetRemoteInetAddress_Object = MibTableColumn
rlAAALinePassLoginHistInetRemoteInetAddress = _RlAAALinePassLoginHistInetRemoteInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 59, 1, 7),
    _RlAAALinePassLoginHistInetRemoteInetAddress_Type()
)
rlAAALinePassLoginHistInetRemoteInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAALinePassLoginHistInetRemoteInetAddress.setStatus("current")
_RlAAALinePassLoginHistInetLocalInetAddressType_Type = InetAddressType
_RlAAALinePassLoginHistInetLocalInetAddressType_Object = MibTableColumn
rlAAALinePassLoginHistInetLocalInetAddressType = _RlAAALinePassLoginHistInetLocalInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 59, 1, 8),
    _RlAAALinePassLoginHistInetLocalInetAddressType_Type()
)
rlAAALinePassLoginHistInetLocalInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAALinePassLoginHistInetLocalInetAddressType.setStatus("current")
_RlAAALinePassLoginHistInetLocalInetAddress_Type = InetAddress
_RlAAALinePassLoginHistInetLocalInetAddress_Object = MibTableColumn
rlAAALinePassLoginHistInetLocalInetAddress = _RlAAALinePassLoginHistInetLocalInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 59, 1, 9),
    _RlAAALinePassLoginHistInetLocalInetAddress_Type()
)
rlAAALinePassLoginHistInetLocalInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAALinePassLoginHistInetLocalInetAddress.setStatus("current")
_RlAAALinePassLoginHistInetDateTime_Type = DisplayString
_RlAAALinePassLoginHistInetDateTime_Object = MibTableColumn
rlAAALinePassLoginHistInetDateTime = _RlAAALinePassLoginHistInetDateTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 59, 1, 10),
    _RlAAALinePassLoginHistInetDateTime_Type()
)
rlAAALinePassLoginHistInetDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAALinePassLoginHistInetDateTime.setStatus("current")
_RlAAALinePassLoginHistInetMrid_Type = Unsigned32
_RlAAALinePassLoginHistInetMrid_Object = MibTableColumn
rlAAALinePassLoginHistInetMrid = _RlAAALinePassLoginHistInetMrid_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 59, 1, 11),
    _RlAAALinePassLoginHistInetMrid_Type()
)
rlAAALinePassLoginHistInetMrid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAALinePassLoginHistInetMrid.setStatus("current")
_RlAAASystemLoginHistInetTable_Object = MibTable
rlAAASystemLoginHistInetTable = _RlAAASystemLoginHistInetTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 60)
)
if mibBuilder.loadTexts:
    rlAAASystemLoginHistInetTable.setStatus("current")
_RlAAASystemLoginHistInetEntry_Object = MibTableRow
rlAAASystemLoginHistInetEntry = _RlAAASystemLoginHistInetEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 60, 1)
)
rlAAASystemLoginHistInetEntry.setIndexNames(
    (0, "RADLAN-AAA", "rlAAASystemLoginHistInetLevel"),
    (0, "RADLAN-AAA", "rlAAASystemLoginHistInetIndex"),
)
if mibBuilder.loadTexts:
    rlAAASystemLoginHistInetEntry.setStatus("current")


class _RlAAASystemLoginHistInetLevel_Type(Integer32):
    """Custom type rlAAASystemLoginHistInetLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RlAAASystemLoginHistInetLevel_Type.__name__ = "Integer32"
_RlAAASystemLoginHistInetLevel_Object = MibTableColumn
rlAAASystemLoginHistInetLevel = _RlAAASystemLoginHistInetLevel_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 60, 1, 1),
    _RlAAASystemLoginHistInetLevel_Type()
)
rlAAASystemLoginHistInetLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAASystemLoginHistInetLevel.setStatus("current")


class _RlAAASystemLoginHistInetIndex_Type(Unsigned32):
    """Custom type rlAAASystemLoginHistInetIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RlAAASystemLoginHistInetIndex_Type.__name__ = "Unsigned32"
_RlAAASystemLoginHistInetIndex_Object = MibTableColumn
rlAAASystemLoginHistInetIndex = _RlAAASystemLoginHistInetIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 60, 1, 2),
    _RlAAASystemLoginHistInetIndex_Type()
)
rlAAASystemLoginHistInetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlAAASystemLoginHistInetIndex.setStatus("current")
_RlAAASystemLoginHistInetServiceType_Type = RlAAAServiceType
_RlAAASystemLoginHistInetServiceType_Object = MibTableColumn
rlAAASystemLoginHistInetServiceType = _RlAAASystemLoginHistInetServiceType_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 60, 1, 3),
    _RlAAASystemLoginHistInetServiceType_Type()
)
rlAAASystemLoginHistInetServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAASystemLoginHistInetServiceType.setStatus("current")
_RlAAASystemLoginHistInetRemoteInetAddressType_Type = InetAddressType
_RlAAASystemLoginHistInetRemoteInetAddressType_Object = MibTableColumn
rlAAASystemLoginHistInetRemoteInetAddressType = _RlAAASystemLoginHistInetRemoteInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 60, 1, 4),
    _RlAAASystemLoginHistInetRemoteInetAddressType_Type()
)
rlAAASystemLoginHistInetRemoteInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAASystemLoginHistInetRemoteInetAddressType.setStatus("current")
_RlAAASystemLoginHistInetRemoteInetAddress_Type = InetAddress
_RlAAASystemLoginHistInetRemoteInetAddress_Object = MibTableColumn
rlAAASystemLoginHistInetRemoteInetAddress = _RlAAASystemLoginHistInetRemoteInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 60, 1, 5),
    _RlAAASystemLoginHistInetRemoteInetAddress_Type()
)
rlAAASystemLoginHistInetRemoteInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAASystemLoginHistInetRemoteInetAddress.setStatus("current")
_RlAAASystemLoginHistInetLocalInetAddressType_Type = InetAddressType
_RlAAASystemLoginHistInetLocalInetAddressType_Object = MibTableColumn
rlAAASystemLoginHistInetLocalInetAddressType = _RlAAASystemLoginHistInetLocalInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 60, 1, 6),
    _RlAAASystemLoginHistInetLocalInetAddressType_Type()
)
rlAAASystemLoginHistInetLocalInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAASystemLoginHistInetLocalInetAddressType.setStatus("current")
_RlAAASystemLoginHistInetLocalInetAddress_Type = InetAddress
_RlAAASystemLoginHistInetLocalInetAddress_Object = MibTableColumn
rlAAASystemLoginHistInetLocalInetAddress = _RlAAASystemLoginHistInetLocalInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 60, 1, 7),
    _RlAAASystemLoginHistInetLocalInetAddress_Type()
)
rlAAASystemLoginHistInetLocalInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAASystemLoginHistInetLocalInetAddress.setStatus("current")
_RlAAASystemLoginHistInetDateTime_Type = DisplayString
_RlAAASystemLoginHistInetDateTime_Object = MibTableColumn
rlAAASystemLoginHistInetDateTime = _RlAAASystemLoginHistInetDateTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 60, 1, 8),
    _RlAAASystemLoginHistInetDateTime_Type()
)
rlAAASystemLoginHistInetDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAASystemLoginHistInetDateTime.setStatus("current")
_RlAAASystemLoginHistInetMrid_Type = Unsigned32
_RlAAASystemLoginHistInetMrid_Object = MibTableColumn
rlAAASystemLoginHistInetMrid = _RlAAASystemLoginHistInetMrid_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 60, 1, 9),
    _RlAAASystemLoginHistInetMrid_Type()
)
rlAAASystemLoginHistInetMrid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAASystemLoginHistInetMrid.setStatus("current")
_RlAAAPasswordComplexityEnabled_Type = TruthValue
_RlAAAPasswordComplexityEnabled_Object = MibScalar
rlAAAPasswordComplexityEnabled = _RlAAAPasswordComplexityEnabled_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 61),
    _RlAAAPasswordComplexityEnabled_Type()
)
rlAAAPasswordComplexityEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAAPasswordComplexityEnabled.setStatus("current")


class _RlAAAPasswordComplexityMinCharClasses_Type(Integer32):
    """Custom type rlAAAPasswordComplexityMinCharClasses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_RlAAAPasswordComplexityMinCharClasses_Type.__name__ = "Integer32"
_RlAAAPasswordComplexityMinCharClasses_Object = MibScalar
rlAAAPasswordComplexityMinCharClasses = _RlAAAPasswordComplexityMinCharClasses_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 62),
    _RlAAAPasswordComplexityMinCharClasses_Type()
)
rlAAAPasswordComplexityMinCharClasses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAAPasswordComplexityMinCharClasses.setStatus("current")
_RlAAAPasswordComplexityNotOldPasswordEnabled_Type = TruthValue
_RlAAAPasswordComplexityNotOldPasswordEnabled_Object = MibScalar
rlAAAPasswordComplexityNotOldPasswordEnabled = _RlAAAPasswordComplexityNotOldPasswordEnabled_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 63),
    _RlAAAPasswordComplexityNotOldPasswordEnabled_Type()
)
rlAAAPasswordComplexityNotOldPasswordEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAAPasswordComplexityNotOldPasswordEnabled.setStatus("current")
_RlAAAPasswordComplexityCharRepeat_Type = Integer32
_RlAAAPasswordComplexityCharRepeat_Object = MibScalar
rlAAAPasswordComplexityCharRepeat = _RlAAAPasswordComplexityCharRepeat_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 64),
    _RlAAAPasswordComplexityCharRepeat_Type()
)
rlAAAPasswordComplexityCharRepeat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAAPasswordComplexityCharRepeat.setStatus("current")
_RlAAAPasswordComplexityNotUserNameEnabled_Type = TruthValue
_RlAAAPasswordComplexityNotUserNameEnabled_Object = MibScalar
rlAAAPasswordComplexityNotUserNameEnabled = _RlAAAPasswordComplexityNotUserNameEnabled_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 65),
    _RlAAAPasswordComplexityNotUserNameEnabled_Type()
)
rlAAAPasswordComplexityNotUserNameEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAAPasswordComplexityNotUserNameEnabled.setStatus("current")
_RlAAAPasswordComplexityNotManufacturerEnabled_Type = TruthValue
_RlAAAPasswordComplexityNotManufacturerEnabled_Object = MibScalar
rlAAAPasswordComplexityNotManufacturerEnabled = _RlAAAPasswordComplexityNotManufacturerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 66),
    _RlAAAPasswordComplexityNotManufacturerEnabled_Type()
)
rlAAAPasswordComplexityNotManufacturerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAAPasswordComplexityNotManufacturerEnabled.setStatus("current")


class _RlAAAPasswordGlobalAgingTime_Type(Integer32):
    """Custom type rlAAAPasswordGlobalAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 365),
    )


_RlAAAPasswordGlobalAgingTime_Type.__name__ = "Integer32"
_RlAAAPasswordGlobalAgingTime_Object = MibScalar
rlAAAPasswordGlobalAgingTime = _RlAAAPasswordGlobalAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 67),
    _RlAAAPasswordGlobalAgingTime_Type()
)
rlAAAPasswordGlobalAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAAPasswordGlobalAgingTime.setStatus("current")
_RlAAALocalUserPasswordVerificationAndSettingTable_Object = MibTable
rlAAALocalUserPasswordVerificationAndSettingTable = _RlAAALocalUserPasswordVerificationAndSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 68)
)
if mibBuilder.loadTexts:
    rlAAALocalUserPasswordVerificationAndSettingTable.setStatus("current")
_RlAAALocalUserPasswordVerificationAndSettingEntry_Object = MibTableRow
rlAAALocalUserPasswordVerificationAndSettingEntry = _RlAAALocalUserPasswordVerificationAndSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 68, 1)
)
rlAAALocalUserPasswordVerificationAndSettingEntry.setIndexNames(
    (0, "RADLAN-AAA", "rlAAALocalUserNameString"),
)
if mibBuilder.loadTexts:
    rlAAALocalUserPasswordVerificationAndSettingEntry.setStatus("current")


class _RlAAALocalUserNameString_Type(DisplayString):
    """Custom type rlAAALocalUserNameString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_RlAAALocalUserNameString_Type.__name__ = "DisplayString"
_RlAAALocalUserNameString_Object = MibTableColumn
rlAAALocalUserNameString = _RlAAALocalUserNameString_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 68, 1, 1),
    _RlAAALocalUserNameString_Type()
)
rlAAALocalUserNameString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAALocalUserNameString.setStatus("current")
_RlAAALocalUserVerificationOldPassword_Type = DisplayString
_RlAAALocalUserVerificationOldPassword_Object = MibTableColumn
rlAAALocalUserVerificationOldPassword = _RlAAALocalUserVerificationOldPassword_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 68, 1, 2),
    _RlAAALocalUserVerificationOldPassword_Type()
)
rlAAALocalUserVerificationOldPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAALocalUserVerificationOldPassword.setStatus("current")
_RlAAALocalUserSettingNewPassword_Type = DisplayString
_RlAAALocalUserSettingNewPassword_Object = MibTableColumn
rlAAALocalUserSettingNewPassword = _RlAAALocalUserSettingNewPassword_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 68, 1, 3),
    _RlAAALocalUserSettingNewPassword_Type()
)
rlAAALocalUserSettingNewPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAALocalUserSettingNewPassword.setStatus("current")
_RlAAALocalUserConfirmNewPassword_Type = DisplayString
_RlAAALocalUserConfirmNewPassword_Object = MibTableColumn
rlAAALocalUserConfirmNewPassword = _RlAAALocalUserConfirmNewPassword_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 68, 1, 4),
    _RlAAALocalUserConfirmNewPassword_Type()
)
rlAAALocalUserConfirmNewPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAALocalUserConfirmNewPassword.setStatus("current")
_RlAAACreationDateSystemPasswordLevel15_Type = DisplayString
_RlAAACreationDateSystemPasswordLevel15_Object = MibScalar
rlAAACreationDateSystemPasswordLevel15 = _RlAAACreationDateSystemPasswordLevel15_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 69),
    _RlAAACreationDateSystemPasswordLevel15_Type()
)
rlAAACreationDateSystemPasswordLevel15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAAACreationDateSystemPasswordLevel15.setStatus("current")


class _RlAAAPasswordRecoveryDisable_Type(TruthValue):
    """Custom type rlAAAPasswordRecoveryDisable based on TruthValue"""


_RlAAAPasswordRecoveryDisable_Object = MibScalar
rlAAAPasswordRecoveryDisable = _RlAAAPasswordRecoveryDisable_Object(
    (1, 3, 6, 1, 4, 1, 89, 79, 70),
    _RlAAAPasswordRecoveryDisable_Type()
)
rlAAAPasswordRecoveryDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAAPasswordRecoveryDisable.setStatus("current")
_RlRadiusMibVersion_Type = Integer32
_RlRadiusMibVersion_Object = MibScalar
rlRadiusMibVersion = _RlRadiusMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 80, 1),
    _RlRadiusMibVersion_Type()
)
rlRadiusMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRadiusMibVersion.setStatus("current")


class _RlRadiusGlobalDefaultTimeout_Type(Integer32):
    """Custom type rlRadiusGlobalDefaultTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_RlRadiusGlobalDefaultTimeout_Type.__name__ = "Integer32"
_RlRadiusGlobalDefaultTimeout_Object = MibScalar
rlRadiusGlobalDefaultTimeout = _RlRadiusGlobalDefaultTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 80, 2),
    _RlRadiusGlobalDefaultTimeout_Type()
)
rlRadiusGlobalDefaultTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusGlobalDefaultTimeout.setStatus("current")


class _RlRadiusGlobalDefaultRetries_Type(Integer32):
    """Custom type rlRadiusGlobalDefaultRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RlRadiusGlobalDefaultRetries_Type.__name__ = "Integer32"
_RlRadiusGlobalDefaultRetries_Object = MibScalar
rlRadiusGlobalDefaultRetries = _RlRadiusGlobalDefaultRetries_Object(
    (1, 3, 6, 1, 4, 1, 89, 80, 3),
    _RlRadiusGlobalDefaultRetries_Type()
)
rlRadiusGlobalDefaultRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusGlobalDefaultRetries.setStatus("current")


class _RlRadiusGlobalDefaultDeadtime_Type(Integer32):
    """Custom type rlRadiusGlobalDefaultDeadtime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_RlRadiusGlobalDefaultDeadtime_Type.__name__ = "Integer32"
_RlRadiusGlobalDefaultDeadtime_Object = MibScalar
rlRadiusGlobalDefaultDeadtime = _RlRadiusGlobalDefaultDeadtime_Object(
    (1, 3, 6, 1, 4, 1, 89, 80, 4),
    _RlRadiusGlobalDefaultDeadtime_Type()
)
rlRadiusGlobalDefaultDeadtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusGlobalDefaultDeadtime.setStatus("current")


class _RlRadiusGlobalDefaultKey_Type(DisplayString):
    """Custom type rlRadiusGlobalDefaultKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlRadiusGlobalDefaultKey_Type.__name__ = "DisplayString"
_RlRadiusGlobalDefaultKey_Object = MibScalar
rlRadiusGlobalDefaultKey = _RlRadiusGlobalDefaultKey_Object(
    (1, 3, 6, 1, 4, 1, 89, 80, 5),
    _RlRadiusGlobalDefaultKey_Type()
)
rlRadiusGlobalDefaultKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusGlobalDefaultKey.setStatus("current")
_RlRadiusGlobalDefaultSource_Type = IpAddress
_RlRadiusGlobalDefaultSource_Object = MibScalar
rlRadiusGlobalDefaultSource = _RlRadiusGlobalDefaultSource_Object(
    (1, 3, 6, 1, 4, 1, 89, 80, 6),
    _RlRadiusGlobalDefaultSource_Type()
)
rlRadiusGlobalDefaultSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusGlobalDefaultSource.setStatus("current")
_RlRadiusServerTable_Object = MibTable
rlRadiusServerTable = _RlRadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 80, 7)
)
if mibBuilder.loadTexts:
    rlRadiusServerTable.setStatus("current")
_RlRadiusServerEntry_Object = MibTableRow
rlRadiusServerEntry = _RlRadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 80, 7, 1)
)
rlRadiusServerEntry.setIndexNames(
    (0, "RADLAN-AAA", "rlRadiusServerAddress"),
    (0, "RADLAN-AAA", "rlRadiusServerAuthPortNumber"),
    (0, "RADLAN-AAA", "rlRadiusServerAcctPortNumber"),
)
if mibBuilder.loadTexts:
    rlRadiusServerEntry.setStatus("current")
_RlRadiusServerAddress_Type = IpAddress
_RlRadiusServerAddress_Object = MibTableColumn
rlRadiusServerAddress = _RlRadiusServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 80, 7, 1, 1),
    _RlRadiusServerAddress_Type()
)
rlRadiusServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServerAddress.setStatus("current")


class _RlRadiusServerAuthPortNumber_Type(Integer32):
    """Custom type rlRadiusServerAuthPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlRadiusServerAuthPortNumber_Type.__name__ = "Integer32"
_RlRadiusServerAuthPortNumber_Object = MibTableColumn
rlRadiusServerAuthPortNumber = _RlRadiusServerAuthPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 80, 7, 1, 2),
    _RlRadiusServerAuthPortNumber_Type()
)
rlRadiusServerAuthPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServerAuthPortNumber.setStatus("current")


class _RlRadiusServerAcctPortNumber_Type(Integer32):
    """Custom type rlRadiusServerAcctPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlRadiusServerAcctPortNumber_Type.__name__ = "Integer32"
_RlRadiusServerAcctPortNumber_Object = MibTableColumn
rlRadiusServerAcctPortNumber = _RlRadiusServerAcctPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 80, 7, 1, 3),
    _RlRadiusServerAcctPortNumber_Type()
)
rlRadiusServerAcctPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServerAcctPortNumber.setStatus("current")


class _RlRadiusServerTimeout_Type(Integer32):
    """Custom type rlRadiusServerTimeout based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_RlRadiusServerTimeout_Type.__name__ = "Integer32"
_RlRadiusServerTimeout_Object = MibTableColumn
rlRadiusServerTimeout = _RlRadiusServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 80, 7, 1, 4),
    _RlRadiusServerTimeout_Type()
)
rlRadiusServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServerTimeout.setStatus("current")


class _RlRadiusServerRetries_Type(Integer32):
    """Custom type rlRadiusServerRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RlRadiusServerRetries_Type.__name__ = "Integer32"
_RlRadiusServerRetries_Object = MibTableColumn
rlRadiusServerRetries = _RlRadiusServerRetries_Object(
    (1, 3, 6, 1, 4, 1, 89, 80, 7, 1, 5),
    _RlRadiusServerRetries_Type()
)
rlRadiusServerRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServerRetries.setStatus("current")


class _RlRadiusServerDeadtime_Type(Integer32):
    """Custom type rlRadiusServerDeadtime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2001),
    )


_RlRadiusServerDeadtime_Type.__name__ = "Integer32"
_RlRadiusServerDeadtime_Object = MibTableColumn
rlRadiusServerDeadtime = _RlRadiusServerDeadtime_Object(
    (1, 3, 6, 1, 4, 1, 89, 80, 7, 1, 6),
    _RlRadiusServerDeadtime_Type()
)
rlRadiusServerDeadtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServerDeadtime.setStatus("current")


class _RlRadiusServerUseGlobalDefaultKey_Type(TruthValue):
    """Custom type rlRadiusServerUseGlobalDefaultKey based on TruthValue"""


_RlRadiusServerUseGlobalDefaultKey_Object = MibTableColumn
rlRadiusServerUseGlobalDefaultKey = _RlRadiusServerUseGlobalDefaultKey_Object(
    (1, 3, 6, 1, 4, 1, 89, 80, 7, 1, 7),
    _RlRadiusServerUseGlobalDefaultKey_Type()
)
rlRadiusServerUseGlobalDefaultKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServerUseGlobalDefaultKey.setStatus("current")


class _RlRadiusServerKey_Type(DisplayString):
    """Custom type rlRadiusServerKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlRadiusServerKey_Type.__name__ = "DisplayString"
_RlRadiusServerKey_Object = MibTableColumn
rlRadiusServerKey = _RlRadiusServerKey_Object(
    (1, 3, 6, 1, 4, 1, 89, 80, 7, 1, 8),
    _RlRadiusServerKey_Type()
)
rlRadiusServerKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServerKey.setStatus("current")
_RlRadiusServerSource_Type = IpAddress
_RlRadiusServerSource_Object = MibTableColumn
rlRadiusServerSource = _RlRadiusServerSource_Object(
    (1, 3, 6, 1, 4, 1, 89, 80, 7, 1, 9),
    _RlRadiusServerSource_Type()
)
rlRadiusServerSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServerSource.setStatus("current")


class _RlRadiusServerPriority_Type(Integer32):
    """Custom type rlRadiusServerPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlRadiusServerPriority_Type.__name__ = "Integer32"
_RlRadiusServerPriority_Object = MibTableColumn
rlRadiusServerPriority = _RlRadiusServerPriority_Object(
    (1, 3, 6, 1, 4, 1, 89, 80, 7, 1, 10),
    _RlRadiusServerPriority_Type()
)
rlRadiusServerPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServerPriority.setStatus("current")
_RlRadiusServerStatus_Type = RowStatus
_RlRadiusServerStatus_Object = MibTableColumn
rlRadiusServerStatus = _RlRadiusServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 80, 7, 1, 11),
    _RlRadiusServerStatus_Type()
)
rlRadiusServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServerStatus.setStatus("current")


class _RlRadiusServerUsage_Type(Integer32):
    """Custom type rlRadiusServerUsage based on Integer32"""
    defaultValue = 3

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
        *(("all", 3),
          ("portAuthentication", 2),
          ("userAuthentication", 1),
          ("wirelessAuthentication", 4))
    )


_RlRadiusServerUsage_Type.__name__ = "Integer32"
_RlRadiusServerUsage_Object = MibTableColumn
rlRadiusServerUsage = _RlRadiusServerUsage_Object(
    (1, 3, 6, 1, 4, 1, 89, 80, 7, 1, 12),
    _RlRadiusServerUsage_Type()
)
rlRadiusServerUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServerUsage.setStatus("current")
_RlRadiusServerInetTable_Object = MibTable
rlRadiusServerInetTable = _RlRadiusServerInetTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 80, 8)
)
if mibBuilder.loadTexts:
    rlRadiusServerInetTable.setStatus("current")
_RlRadiusServerInetEntry_Object = MibTableRow
rlRadiusServerInetEntry = _RlRadiusServerInetEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 80, 8, 1)
)
rlRadiusServerInetEntry.setIndexNames(
    (0, "RADLAN-AAA", "rlRadiusServerInetAddressType"),
    (0, "RADLAN-AAA", "rlRadiusServerInetAddress"),
    (0, "RADLAN-AAA", "rlRadiusServerInetAuthPortNumber"),
    (0, "RADLAN-AAA", "rlRadiusServerInetAcctPortNumber"),
)
if mibBuilder.loadTexts:
    rlRadiusServerInetEntry.setStatus("current")
_RlRadiusServerInetAddressType_Type = InetAddressType
_RlRadiusServerInetAddressType_Object = MibTableColumn
rlRadiusServerInetAddressType = _RlRadiusServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 89, 80, 8, 1, 1),
    _RlRadiusServerInetAddressType_Type()
)
rlRadiusServerInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServerInetAddressType.setStatus("current")
_RlRadiusServerInetAddress_Type = InetAddress
_RlRadiusServerInetAddress_Object = MibTableColumn
rlRadiusServerInetAddress = _RlRadiusServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 80, 8, 1, 2),
    _RlRadiusServerInetAddress_Type()
)
rlRadiusServerInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServerInetAddress.setStatus("current")


class _RlRadiusServerInetAuthPortNumber_Type(Integer32):
    """Custom type rlRadiusServerInetAuthPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlRadiusServerInetAuthPortNumber_Type.__name__ = "Integer32"
_RlRadiusServerInetAuthPortNumber_Object = MibTableColumn
rlRadiusServerInetAuthPortNumber = _RlRadiusServerInetAuthPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 80, 8, 1, 3),
    _RlRadiusServerInetAuthPortNumber_Type()
)
rlRadiusServerInetAuthPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServerInetAuthPortNumber.setStatus("current")


class _RlRadiusServerInetAcctPortNumber_Type(Integer32):
    """Custom type rlRadiusServerInetAcctPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlRadiusServerInetAcctPortNumber_Type.__name__ = "Integer32"
_RlRadiusServerInetAcctPortNumber_Object = MibTableColumn
rlRadiusServerInetAcctPortNumber = _RlRadiusServerInetAcctPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 80, 8, 1, 4),
    _RlRadiusServerInetAcctPortNumber_Type()
)
rlRadiusServerInetAcctPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServerInetAcctPortNumber.setStatus("current")


class _RlRadiusServerInetTimeout_Type(Integer32):
    """Custom type rlRadiusServerInetTimeout based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_RlRadiusServerInetTimeout_Type.__name__ = "Integer32"
_RlRadiusServerInetTimeout_Object = MibTableColumn
rlRadiusServerInetTimeout = _RlRadiusServerInetTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 80, 8, 1, 5),
    _RlRadiusServerInetTimeout_Type()
)
rlRadiusServerInetTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServerInetTimeout.setStatus("current")


class _RlRadiusServerInetRetries_Type(Integer32):
    """Custom type rlRadiusServerInetRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RlRadiusServerInetRetries_Type.__name__ = "Integer32"
_RlRadiusServerInetRetries_Object = MibTableColumn
rlRadiusServerInetRetries = _RlRadiusServerInetRetries_Object(
    (1, 3, 6, 1, 4, 1, 89, 80, 8, 1, 6),
    _RlRadiusServerInetRetries_Type()
)
rlRadiusServerInetRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServerInetRetries.setStatus("current")


class _RlRadiusServerInetDeadtime_Type(Integer32):
    """Custom type rlRadiusServerInetDeadtime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2001),
    )


_RlRadiusServerInetDeadtime_Type.__name__ = "Integer32"
_RlRadiusServerInetDeadtime_Object = MibTableColumn
rlRadiusServerInetDeadtime = _RlRadiusServerInetDeadtime_Object(
    (1, 3, 6, 1, 4, 1, 89, 80, 8, 1, 7),
    _RlRadiusServerInetDeadtime_Type()
)
rlRadiusServerInetDeadtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServerInetDeadtime.setStatus("current")


class _RlRadiusServerInetUseGlobalDefaultKey_Type(TruthValue):
    """Custom type rlRadiusServerInetUseGlobalDefaultKey based on TruthValue"""


_RlRadiusServerInetUseGlobalDefaultKey_Object = MibTableColumn
rlRadiusServerInetUseGlobalDefaultKey = _RlRadiusServerInetUseGlobalDefaultKey_Object(
    (1, 3, 6, 1, 4, 1, 89, 80, 8, 1, 8),
    _RlRadiusServerInetUseGlobalDefaultKey_Type()
)
rlRadiusServerInetUseGlobalDefaultKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServerInetUseGlobalDefaultKey.setStatus("current")


class _RlRadiusServerInetKey_Type(DisplayString):
    """Custom type rlRadiusServerInetKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlRadiusServerInetKey_Type.__name__ = "DisplayString"
_RlRadiusServerInetKey_Object = MibTableColumn
rlRadiusServerInetKey = _RlRadiusServerInetKey_Object(
    (1, 3, 6, 1, 4, 1, 89, 80, 8, 1, 9),
    _RlRadiusServerInetKey_Type()
)
rlRadiusServerInetKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServerInetKey.setStatus("current")
_RlRadiusServerInetSourceType_Type = InetAddressType
_RlRadiusServerInetSourceType_Object = MibTableColumn
rlRadiusServerInetSourceType = _RlRadiusServerInetSourceType_Object(
    (1, 3, 6, 1, 4, 1, 89, 80, 8, 1, 10),
    _RlRadiusServerInetSourceType_Type()
)
rlRadiusServerInetSourceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServerInetSourceType.setStatus("current")
_RlRadiusServerInetSource_Type = InetAddress
_RlRadiusServerInetSource_Object = MibTableColumn
rlRadiusServerInetSource = _RlRadiusServerInetSource_Object(
    (1, 3, 6, 1, 4, 1, 89, 80, 8, 1, 11),
    _RlRadiusServerInetSource_Type()
)
rlRadiusServerInetSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServerInetSource.setStatus("current")


class _RlRadiusServerInetPriority_Type(Integer32):
    """Custom type rlRadiusServerInetPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlRadiusServerInetPriority_Type.__name__ = "Integer32"
_RlRadiusServerInetPriority_Object = MibTableColumn
rlRadiusServerInetPriority = _RlRadiusServerInetPriority_Object(
    (1, 3, 6, 1, 4, 1, 89, 80, 8, 1, 12),
    _RlRadiusServerInetPriority_Type()
)
rlRadiusServerInetPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServerInetPriority.setStatus("current")
_RlRadiusServerInetStatus_Type = RowStatus
_RlRadiusServerInetStatus_Object = MibTableColumn
rlRadiusServerInetStatus = _RlRadiusServerInetStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 80, 8, 1, 13),
    _RlRadiusServerInetStatus_Type()
)
rlRadiusServerInetStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServerInetStatus.setStatus("current")


class _RlRadiusServerInetUsage_Type(Integer32):
    """Custom type rlRadiusServerInetUsage based on Integer32"""
    defaultValue = 3

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
        *(("all", 3),
          ("portAuthentication", 2),
          ("userAuthentication", 1),
          ("wirelessAuthentication", 4))
    )


_RlRadiusServerInetUsage_Type.__name__ = "Integer32"
_RlRadiusServerInetUsage_Object = MibTableColumn
rlRadiusServerInetUsage = _RlRadiusServerInetUsage_Object(
    (1, 3, 6, 1, 4, 1, 89, 80, 8, 1, 14),
    _RlRadiusServerInetUsage_Type()
)
rlRadiusServerInetUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusServerInetUsage.setStatus("current")
_RlRadiusServerInetLastResponseTime_Type = TimeStamp
_RlRadiusServerInetLastResponseTime_Object = MibTableColumn
rlRadiusServerInetLastResponseTime = _RlRadiusServerInetLastResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 80, 8, 1, 15),
    _RlRadiusServerInetLastResponseTime_Type()
)
rlRadiusServerInetLastResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRadiusServerInetLastResponseTime.setStatus("current")
_RlRadiusGlobalIPv6DefaultSource_Type = InetAddressIPv6
_RlRadiusGlobalIPv6DefaultSource_Object = MibScalar
rlRadiusGlobalIPv6DefaultSource = _RlRadiusGlobalIPv6DefaultSource_Object(
    (1, 3, 6, 1, 4, 1, 89, 80, 9),
    _RlRadiusGlobalIPv6DefaultSource_Type()
)
rlRadiusGlobalIPv6DefaultSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRadiusGlobalIPv6DefaultSource.setStatus("current")
_RlAAAEapMethodListTable_Object = MibTable
rlAAAEapMethodListTable = _RlAAAEapMethodListTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 97, 1)
)
if mibBuilder.loadTexts:
    rlAAAEapMethodListTable.setStatus("current")
_RlAAAEapMethodListEntry_Object = MibTableRow
rlAAAEapMethodListEntry = _RlAAAEapMethodListEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 97, 1, 1)
)
rlAAAEapMethodListEntry.setIndexNames(
    (0, "RADLAN-AAA", "rlAAAEapMethodListName"),
)
if mibBuilder.loadTexts:
    rlAAAEapMethodListEntry.setStatus("current")


class _RlAAAEapMethodListName_Type(DisplayString):
    """Custom type rlAAAEapMethodListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 20),
    )


_RlAAAEapMethodListName_Type.__name__ = "DisplayString"
_RlAAAEapMethodListName_Object = MibTableColumn
rlAAAEapMethodListName = _RlAAAEapMethodListName_Object(
    (1, 3, 6, 1, 4, 1, 89, 97, 1, 1, 1),
    _RlAAAEapMethodListName_Type()
)
rlAAAEapMethodListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAAEapMethodListName.setStatus("current")
_RlAAAEapMethodType1_Type = RlAAAEapMethodtype
_RlAAAEapMethodType1_Object = MibTableColumn
rlAAAEapMethodType1 = _RlAAAEapMethodType1_Object(
    (1, 3, 6, 1, 4, 1, 89, 97, 1, 1, 2),
    _RlAAAEapMethodType1_Type()
)
rlAAAEapMethodType1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAAEapMethodType1.setStatus("current")
_RlAAAEapMethodType2_Type = RlAAAEapMethodtype
_RlAAAEapMethodType2_Object = MibTableColumn
rlAAAEapMethodType2 = _RlAAAEapMethodType2_Object(
    (1, 3, 6, 1, 4, 1, 89, 97, 1, 1, 3),
    _RlAAAEapMethodType2_Type()
)
rlAAAEapMethodType2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAAEapMethodType2.setStatus("current")
_RlAAAEapMethodType3_Type = RlAAAEapMethodtype
_RlAAAEapMethodType3_Object = MibTableColumn
rlAAAEapMethodType3 = _RlAAAEapMethodType3_Object(
    (1, 3, 6, 1, 4, 1, 89, 97, 1, 1, 4),
    _RlAAAEapMethodType3_Type()
)
rlAAAEapMethodType3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAAEapMethodType3.setStatus("current")
_RlAAAEapMethodType4_Type = RlAAAEapMethodtype
_RlAAAEapMethodType4_Object = MibTableColumn
rlAAAEapMethodType4 = _RlAAAEapMethodType4_Object(
    (1, 3, 6, 1, 4, 1, 89, 97, 1, 1, 5),
    _RlAAAEapMethodType4_Type()
)
rlAAAEapMethodType4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAAEapMethodType4.setStatus("current")
_RlAAAEapMethodType5_Type = RlAAAEapMethodtype
_RlAAAEapMethodType5_Object = MibTableColumn
rlAAAEapMethodType5 = _RlAAAEapMethodType5_Object(
    (1, 3, 6, 1, 4, 1, 89, 97, 1, 1, 6),
    _RlAAAEapMethodType5_Type()
)
rlAAAEapMethodType5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAAEapMethodType5.setStatus("current")
_RlAAAEapMethodListStatus_Type = RowStatus
_RlAAAEapMethodListStatus_Object = MibTableColumn
rlAAAEapMethodListStatus = _RlAAAEapMethodListStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 97, 1, 1, 7),
    _RlAAAEapMethodListStatus_Type()
)
rlAAAEapMethodListStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAAEapMethodListStatus.setStatus("current")


class _RlAAAEapCurrentMethodList_Type(DisplayString):
    """Custom type rlAAAEapCurrentMethodList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 20),
    )


_RlAAAEapCurrentMethodList_Type.__name__ = "DisplayString"
_RlAAAEapCurrentMethodList_Object = MibScalar
rlAAAEapCurrentMethodList = _RlAAAEapCurrentMethodList_Object(
    (1, 3, 6, 1, 4, 1, 89, 97, 2),
    _RlAAAEapCurrentMethodList_Type()
)
rlAAAEapCurrentMethodList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAAAEapCurrentMethodList.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-AAA",
    **{"RlAAAMethodtype": RlAAAMethodtype,
       "RlAAAServiceType": RlAAAServiceType,
       "RlAAALinePortType": RlAAALinePortType,
       "RlAAAEapMethodtype": RlAAAEapMethodtype,
       "RlTacacsConnectionType": RlTacacsConnectionType,
       "RlTacacsConnectionStatus": RlTacacsConnectionStatus,
       "RlAAAAccountingMethod": RlAAAAccountingMethod,
       "rlAAA": rlAAA,
       "rlAAAMibVersion": rlAAAMibVersion,
       "rlAAARetries": rlAAARetries,
       "rlAAARadiusEnabled": rlAAARadiusEnabled,
       "rlAAATacacsEnabled": rlAAATacacsEnabled,
       "rlAAALocalUserEnabled": rlAAALocalUserEnabled,
       "rlAAASystemPasswordEnabled": rlAAASystemPasswordEnabled,
       "rlAAALinePasswordEnabled": rlAAALinePasswordEnabled,
       "rlAAAAlwaysSuccessEnabled": rlAAAAlwaysSuccessEnabled,
       "rlAAARadiusSupported": rlAAARadiusSupported,
       "rlAAATacacsSupported": rlAAATacacsSupported,
       "rlAAALocalUserSupported": rlAAALocalUserSupported,
       "rlAAASystemPasswordSupported": rlAAASystemPasswordSupported,
       "rlAAALinePasswordSupported": rlAAALinePasswordSupported,
       "rlAAALineAlwaysSuccessSupported": rlAAALineAlwaysSuccessSupported,
       "rlAAAMethodListTable": rlAAAMethodListTable,
       "rlAAAMethodListEntry": rlAAAMethodListEntry,
       "rlAAAMethodListName": rlAAAMethodListName,
       "rlAAAMethodType1": rlAAAMethodType1,
       "rlAAAMethodType2": rlAAAMethodType2,
       "rlAAAMethodType3": rlAAAMethodType3,
       "rlAAAMethodType4": rlAAAMethodType4,
       "rlAAAMethodType5": rlAAAMethodType5,
       "rlAAAMethodType6": rlAAAMethodType6,
       "rlAAAMethodType7": rlAAAMethodType7,
       "rlAAAMethodListStatus": rlAAAMethodListStatus,
       "rlAAAAuthorizeEnable": rlAAAAuthorizeEnable,
       "rlAAALineTable": rlAAALineTable,
       "rlAAALineEntry": rlAAALineEntry,
       "rlAAALinePortType": rlAAALinePortType,
       "rlAAAIfIndex": rlAAAIfIndex,
       "rlAAAServiceType": rlAAAServiceType,
       "rlAAALineMethodListNameLevel1": rlAAALineMethodListNameLevel1,
       "rlAAALineMethodListNameLevel2": rlAAALineMethodListNameLevel2,
       "rlAAALineMethodListNameLevel3": rlAAALineMethodListNameLevel3,
       "rlAAALineMethodListNameLevel4": rlAAALineMethodListNameLevel4,
       "rlAAALineMethodListNameLevel5": rlAAALineMethodListNameLevel5,
       "rlAAALineMethodListNameLevel6": rlAAALineMethodListNameLevel6,
       "rlAAALineMethodListNameLevel7": rlAAALineMethodListNameLevel7,
       "rlAAALineMethodListNameLevel8": rlAAALineMethodListNameLevel8,
       "rlAAALineMethodListNameLevel9": rlAAALineMethodListNameLevel9,
       "rlAAALineMethodListNameLevel10": rlAAALineMethodListNameLevel10,
       "rlAAALineMethodListNameLevel11": rlAAALineMethodListNameLevel11,
       "rlAAALineMethodListNameLevel12": rlAAALineMethodListNameLevel12,
       "rlAAALineMethodListNameLevel13": rlAAALineMethodListNameLevel13,
       "rlAAALineMethodListNameLevel14": rlAAALineMethodListNameLevel14,
       "rlAAALineMethodListNameLevel15": rlAAALineMethodListNameLevel15,
       "rlAAALinePassword": rlAAALinePassword,
       "rlAAALineStatus": rlAAALineStatus,
       "rlAAALineLockedState": rlAAALineLockedState,
       "rlAAALineConsFailedLogins": rlAAALineConsFailedLogins,
       "rlAAALinePasswordValidTime": rlAAALinePasswordValidTime,
       "rlAAALinePasswordExpieryDate": rlAAALinePasswordExpieryDate,
       "rlAAALocalUserTable": rlAAALocalUserTable,
       "rlAAALocalUserEntry": rlAAALocalUserEntry,
       "rlAAALocalUserName": rlAAALocalUserName,
       "rlAAALocalUserPassword": rlAAALocalUserPassword,
       "rlAAALocalUserPrivilage": rlAAALocalUserPrivilage,
       "rlAAALocalHostStatus": rlAAALocalHostStatus,
       "rlAAALocalLockedState": rlAAALocalLockedState,
       "rlAAALocalConsFailedLogins": rlAAALocalConsFailedLogins,
       "rlAAALocalPasswordValidTime": rlAAALocalPasswordValidTime,
       "rlAAALocalPasswordExpieryDate": rlAAALocalPasswordExpieryDate,
       "rlAAALocalPasswordCreationDate": rlAAALocalPasswordCreationDate,
       "rlAAASystemPasswordlevel1": rlAAASystemPasswordlevel1,
       "rlAAASystemPasswordlevel2": rlAAASystemPasswordlevel2,
       "rlAAASystemPasswordlevel3": rlAAASystemPasswordlevel3,
       "rlAAASystemPasswordlevel4": rlAAASystemPasswordlevel4,
       "rlAAASystemPasswordlevel5": rlAAASystemPasswordlevel5,
       "rlAAASystemPasswordlevel6": rlAAASystemPasswordlevel6,
       "rlAAASystemPasswordlevel7": rlAAASystemPasswordlevel7,
       "rlAAASystemPasswordlevel8": rlAAASystemPasswordlevel8,
       "rlAAASystemPasswordlevel9": rlAAASystemPasswordlevel9,
       "rlAAASystemPasswordlevel10": rlAAASystemPasswordlevel10,
       "rlAAASystemPasswordlevel11": rlAAASystemPasswordlevel11,
       "rlAAASystemPasswordlevel12": rlAAASystemPasswordlevel12,
       "rlAAASystemPasswordlevel13": rlAAASystemPasswordlevel13,
       "rlAAASystemPasswordlevel14": rlAAASystemPasswordlevel14,
       "rlAAASystemPasswordlevel15": rlAAASystemPasswordlevel15,
       "rlAAAUserTable": rlAAAUserTable,
       "rlAAAUserEntry": rlAAAUserEntry,
       "rlAAAUserIndex": rlAAAUserIndex,
       "rlAAAUserServiceType": rlAAAUserServiceType,
       "rlAAAUserRemoteIpAddress": rlAAAUserRemoteIpAddress,
       "rlAAAUserName": rlAAAUserName,
       "rlAAAUserLevel": rlAAAUserLevel,
       "rlAAAUserIfIndex": rlAAAUserIfIndex,
       "rlAAAUserLoginDate": rlAAAUserLoginDate,
       "rlAAAUserLoginDurationMS": rlAAAUserLoginDurationMS,
       "rlAAATest": rlAAATest,
       "rlAAATestPassword": rlAAATestPassword,
       "rlAAATestUserTable": rlAAATestUserTable,
       "rlAAATestUserEntry": rlAAATestUserEntry,
       "rlAAATestUserIndex": rlAAATestUserIndex,
       "rlAAATestPortType": rlAAATestPortType,
       "rlAAATestIfIndex": rlAAATestIfIndex,
       "rlAAATestServiceType": rlAAATestServiceType,
       "rlAAATestUserAuthenticationStatus": rlAAATestUserAuthenticationStatus,
       "rlAAATestUserAuthenticationAction": rlAAATestUserAuthenticationAction,
       "rlAAATestUserInput": rlAAATestUserInput,
       "rlAAATestUserStatus": rlAAATestUserStatus,
       "rlTacacs": rlTacacs,
       "rlTacacsMibVersion": rlTacacsMibVersion,
       "rlTacacsGlobalDefaultTimeout": rlTacacsGlobalDefaultTimeout,
       "rlTacacsGlobalDefaultKey": rlTacacsGlobalDefaultKey,
       "rlTacacsGlobalDefaultSourceIpInterface": rlTacacsGlobalDefaultSourceIpInterface,
       "rlTacacsServerTable": rlTacacsServerTable,
       "rlTacacsServerEntry": rlTacacsServerEntry,
       "rlTacacsServerAddress": rlTacacsServerAddress,
       "rlTacacsServerPortNumber": rlTacacsServerPortNumber,
       "rlTacacsServerConnectionType": rlTacacsServerConnectionType,
       "rlTacacsServerConnectionStatus": rlTacacsServerConnectionStatus,
       "rlTacacsServerTimeout": rlTacacsServerTimeout,
       "rlTacacsServerUseGlobalDefaultKey": rlTacacsServerUseGlobalDefaultKey,
       "rlTacacsServerKey": rlTacacsServerKey,
       "rlTacacsServerSourceIpInterface": rlTacacsServerSourceIpInterface,
       "rlTacacsServerPriority": rlTacacsServerPriority,
       "rlTacacsServerRowStatus": rlTacacsServerRowStatus,
       "rlTacacsGlobalDefaultSourceIPv6Interface": rlTacacsGlobalDefaultSourceIPv6Interface,
       "rlTacacsServerInetTable": rlTacacsServerInetTable,
       "rlTacacsServerInetEntry": rlTacacsServerInetEntry,
       "rlTacacsServerInetAddressType": rlTacacsServerInetAddressType,
       "rlTacacsServerInetAddress": rlTacacsServerInetAddress,
       "rlTacacsServerInetPortNumber": rlTacacsServerInetPortNumber,
       "rlTacacsServerInetConnectionType": rlTacacsServerInetConnectionType,
       "rlTacacsServerInetConnectionStatus": rlTacacsServerInetConnectionStatus,
       "rlTacacsServerInetTimeout": rlTacacsServerInetTimeout,
       "rlTacacsServerInetUseGlobalDefaultKey": rlTacacsServerInetUseGlobalDefaultKey,
       "rlTacacsServerInetKey": rlTacacsServerInetKey,
       "rlTacacsServerInetSourceInterfaceType": rlTacacsServerInetSourceInterfaceType,
       "rlTacacsServerInetSourceInterface": rlTacacsServerInetSourceInterface,
       "rlTacacsServerInetPriority": rlTacacsServerInetPriority,
       "rlTacacsServerInetRowStatus": rlTacacsServerInetRowStatus,
       "rlAAAAuditingEnable": rlAAAAuditingEnable,
       "rlAAAMinPasswordLength": rlAAAMinPasswordLength,
       "rlAAAPasswordHistSize": rlAAAPasswordHistSize,
       "rlAAAPasswordHistHoldTime": rlAAAPasswordHistHoldTime,
       "rlAAASuccLoginWriteToFile": rlAAASuccLoginWriteToFile,
       "rlAAALocalLoginHistTable": rlAAALocalLoginHistTable,
       "rlAAALocalLoginHistEntry": rlAAALocalLoginHistEntry,
       "rlAAALocalLoginHistName": rlAAALocalLoginHistName,
       "rlAAALocalLoginHistIndex": rlAAALocalLoginHistIndex,
       "rlAAALocalLoginHistServiceType": rlAAALocalLoginHistServiceType,
       "rlAAALocalLoginHistRemoteIpAddress": rlAAALocalLoginHistRemoteIpAddress,
       "rlAAALocalLoginHistLocalIpAddress": rlAAALocalLoginHistLocalIpAddress,
       "rlAAALocalLoginDateTime": rlAAALocalLoginDateTime,
       "rlAAALocalLoginMrid": rlAAALocalLoginMrid,
       "rlAAALinePassLoginHistTable": rlAAALinePassLoginHistTable,
       "rlAAALinePassLoginHistEntry": rlAAALinePassLoginHistEntry,
       "rlAAALinePassLoginHistPortType": rlAAALinePassLoginHistPortType,
       "rlAAALinePassLoginHistIfIndex": rlAAALinePassLoginHistIfIndex,
       "rlAAALinePassLoginHistServiceType": rlAAALinePassLoginHistServiceType,
       "rlAAALinePassLoginHistIndex": rlAAALinePassLoginHistIndex,
       "rlAAALinePassLoginHistActServiceType": rlAAALinePassLoginHistActServiceType,
       "rlAAALinePassLoginHistRemoteIpAddress": rlAAALinePassLoginHistRemoteIpAddress,
       "rlAAALinePassLoginHistLocalIpAddress": rlAAALinePassLoginHistLocalIpAddress,
       "rlAAALinePassLoginDateTime": rlAAALinePassLoginDateTime,
       "rlAAALinePassLoginMrid": rlAAALinePassLoginMrid,
       "rlAAASystemLoginHistTable": rlAAASystemLoginHistTable,
       "rlAAASystemLoginHistEntry": rlAAASystemLoginHistEntry,
       "rlAAASystemLoginHistLevel": rlAAASystemLoginHistLevel,
       "rlAAASystemLoginHistIndex": rlAAASystemLoginHistIndex,
       "rlAAASystemLoginHistServiceType": rlAAASystemLoginHistServiceType,
       "rlAAASystemLoginHistRemoteIpAddress": rlAAASystemLoginHistRemoteIpAddress,
       "rlAAASystemLoginHistLocalIpAddress": rlAAASystemLoginHistLocalIpAddress,
       "rlAAASystemLoginDateTime": rlAAASystemLoginDateTime,
       "rlAAASystemLoginMrid": rlAAASystemLoginMrid,
       "rlAAASysPassStatTable": rlAAASysPassStatTable,
       "rlAAASysPassStatEntry": rlAAASysPassStatEntry,
       "rlAAASysPassStatLevel": rlAAASysPassStatLevel,
       "rlAAASysPassStatLockedState": rlAAASysPassStatLockedState,
       "rlAAASysPassStatConsFailedLogins": rlAAASysPassStatConsFailedLogins,
       "rlAAASysPassStatPasswordValidTime": rlAAASysPassStatPasswordValidTime,
       "rlAAASysPassStatPasswordExpieryDate": rlAAASysPassStatPasswordExpieryDate,
       "rlAAAMaxNumLogAttmpts": rlAAAMaxNumLogAttmpts,
       "rlAAAUnlockUserName": rlAAAUnlockUserName,
       "rlAAAUnlockSystemPassword": rlAAAUnlockSystemPassword,
       "rlAAALockedLineTable": rlAAALockedLineTable,
       "rlAAALockedLineEntry": rlAAALockedLineEntry,
       "rlAAALockedLinePortType": rlAAALockedLinePortType,
       "rlAAALockedLineIfIndex": rlAAALockedLineIfIndex,
       "rlAAALockedLineServiceType": rlAAALockedLineServiceType,
       "rlAAALockedLineStatus": rlAAALockedLineStatus,
       "rlAAASystemPasswordVerificationAndSettingTable": rlAAASystemPasswordVerificationAndSettingTable,
       "rlAAASystemPasswordVerificationAndSettingEntry": rlAAASystemPasswordVerificationAndSettingEntry,
       "rlAAASystemPasswordSettingPrivilegeLevel": rlAAASystemPasswordSettingPrivilegeLevel,
       "rlAAASystemPasswordVerificationOldPassword": rlAAASystemPasswordVerificationOldPassword,
       "rlAAASystemPasswordSettingNewPassword": rlAAASystemPasswordSettingNewPassword,
       "rlAAASystemPasswordConfirmNewPassword": rlAAASystemPasswordConfirmNewPassword,
       "rlAAAAccountingMngMethod": rlAAAAccountingMngMethod,
       "rlAAAAccountingDot1xMethod": rlAAAAccountingDot1xMethod,
       "rlAAAUserInetTable": rlAAAUserInetTable,
       "rlAAAUserInetEntry": rlAAAUserInetEntry,
       "rlAAAUserInetIndex": rlAAAUserInetIndex,
       "rlAAAUserInetServiceType": rlAAAUserInetServiceType,
       "rlAAAUserInetRemoteIpAddressType": rlAAAUserInetRemoteIpAddressType,
       "rlAAAUserInetRemoteIpAddress": rlAAAUserInetRemoteIpAddress,
       "rlAAAUserInetName": rlAAAUserInetName,
       "rlAAAUserInetLevel": rlAAAUserInetLevel,
       "rlAAAUserInetIfIndex": rlAAAUserInetIfIndex,
       "rlAAAUserInetLoginDate": rlAAAUserInetLoginDate,
       "rlAAAUserInetLoginDurationMS": rlAAAUserInetLoginDurationMS,
       "rlAAALocalLoginHistInetTable": rlAAALocalLoginHistInetTable,
       "rlAAALocalLoginHistInetEntry": rlAAALocalLoginHistInetEntry,
       "rlAAALocalLoginHistInetName": rlAAALocalLoginHistInetName,
       "rlAAALocalLoginHistInetIndex": rlAAALocalLoginHistInetIndex,
       "rlAAALocalLoginHistInetServiceType": rlAAALocalLoginHistInetServiceType,
       "rlAAALocalLoginHistInetRemoteIpAddressType": rlAAALocalLoginHistInetRemoteIpAddressType,
       "rlAAALocalLoginHistInetRemoteIpAddress": rlAAALocalLoginHistInetRemoteIpAddress,
       "rlAAALocalLoginHistInetLocalIpAddressType": rlAAALocalLoginHistInetLocalIpAddressType,
       "rlAAALocalLoginHistInetLocalIpAddress": rlAAALocalLoginHistInetLocalIpAddress,
       "rlAAALocalLoginHistInetDateTime": rlAAALocalLoginHistInetDateTime,
       "rlAAALocalLoginHistInetMrid": rlAAALocalLoginHistInetMrid,
       "rlAAALinePassLoginHistInetTable": rlAAALinePassLoginHistInetTable,
       "rlAAALinePassLoginHistInetEntry": rlAAALinePassLoginHistInetEntry,
       "rlAAALinePassLoginHistInetPortType": rlAAALinePassLoginHistInetPortType,
       "rlAAALinePassLoginHistInetIfIndex": rlAAALinePassLoginHistInetIfIndex,
       "rlAAALinePassLoginHistInetServiceType": rlAAALinePassLoginHistInetServiceType,
       "rlAAALinePassLoginHistInetIndex": rlAAALinePassLoginHistInetIndex,
       "rlAAALinePassLoginHistInetActServiceType": rlAAALinePassLoginHistInetActServiceType,
       "rlAAALinePassLoginHistInetRemoteInetAddressType": rlAAALinePassLoginHistInetRemoteInetAddressType,
       "rlAAALinePassLoginHistInetRemoteInetAddress": rlAAALinePassLoginHistInetRemoteInetAddress,
       "rlAAALinePassLoginHistInetLocalInetAddressType": rlAAALinePassLoginHistInetLocalInetAddressType,
       "rlAAALinePassLoginHistInetLocalInetAddress": rlAAALinePassLoginHistInetLocalInetAddress,
       "rlAAALinePassLoginHistInetDateTime": rlAAALinePassLoginHistInetDateTime,
       "rlAAALinePassLoginHistInetMrid": rlAAALinePassLoginHistInetMrid,
       "rlAAASystemLoginHistInetTable": rlAAASystemLoginHistInetTable,
       "rlAAASystemLoginHistInetEntry": rlAAASystemLoginHistInetEntry,
       "rlAAASystemLoginHistInetLevel": rlAAASystemLoginHistInetLevel,
       "rlAAASystemLoginHistInetIndex": rlAAASystemLoginHistInetIndex,
       "rlAAASystemLoginHistInetServiceType": rlAAASystemLoginHistInetServiceType,
       "rlAAASystemLoginHistInetRemoteInetAddressType": rlAAASystemLoginHistInetRemoteInetAddressType,
       "rlAAASystemLoginHistInetRemoteInetAddress": rlAAASystemLoginHistInetRemoteInetAddress,
       "rlAAASystemLoginHistInetLocalInetAddressType": rlAAASystemLoginHistInetLocalInetAddressType,
       "rlAAASystemLoginHistInetLocalInetAddress": rlAAASystemLoginHistInetLocalInetAddress,
       "rlAAASystemLoginHistInetDateTime": rlAAASystemLoginHistInetDateTime,
       "rlAAASystemLoginHistInetMrid": rlAAASystemLoginHistInetMrid,
       "rlAAAPasswordComplexityEnabled": rlAAAPasswordComplexityEnabled,
       "rlAAAPasswordComplexityMinCharClasses": rlAAAPasswordComplexityMinCharClasses,
       "rlAAAPasswordComplexityNotOldPasswordEnabled": rlAAAPasswordComplexityNotOldPasswordEnabled,
       "rlAAAPasswordComplexityCharRepeat": rlAAAPasswordComplexityCharRepeat,
       "rlAAAPasswordComplexityNotUserNameEnabled": rlAAAPasswordComplexityNotUserNameEnabled,
       "rlAAAPasswordComplexityNotManufacturerEnabled": rlAAAPasswordComplexityNotManufacturerEnabled,
       "rlAAAPasswordGlobalAgingTime": rlAAAPasswordGlobalAgingTime,
       "rlAAALocalUserPasswordVerificationAndSettingTable": rlAAALocalUserPasswordVerificationAndSettingTable,
       "rlAAALocalUserPasswordVerificationAndSettingEntry": rlAAALocalUserPasswordVerificationAndSettingEntry,
       "rlAAALocalUserNameString": rlAAALocalUserNameString,
       "rlAAALocalUserVerificationOldPassword": rlAAALocalUserVerificationOldPassword,
       "rlAAALocalUserSettingNewPassword": rlAAALocalUserSettingNewPassword,
       "rlAAALocalUserConfirmNewPassword": rlAAALocalUserConfirmNewPassword,
       "rlAAACreationDateSystemPasswordLevel15": rlAAACreationDateSystemPasswordLevel15,
       "rlAAAPasswordRecoveryDisable": rlAAAPasswordRecoveryDisable,
       "rlRadiusMibVersion": rlRadiusMibVersion,
       "rlRadiusGlobalDefaultTimeout": rlRadiusGlobalDefaultTimeout,
       "rlRadiusGlobalDefaultRetries": rlRadiusGlobalDefaultRetries,
       "rlRadiusGlobalDefaultDeadtime": rlRadiusGlobalDefaultDeadtime,
       "rlRadiusGlobalDefaultKey": rlRadiusGlobalDefaultKey,
       "rlRadiusGlobalDefaultSource": rlRadiusGlobalDefaultSource,
       "rlRadiusServerTable": rlRadiusServerTable,
       "rlRadiusServerEntry": rlRadiusServerEntry,
       "rlRadiusServerAddress": rlRadiusServerAddress,
       "rlRadiusServerAuthPortNumber": rlRadiusServerAuthPortNumber,
       "rlRadiusServerAcctPortNumber": rlRadiusServerAcctPortNumber,
       "rlRadiusServerTimeout": rlRadiusServerTimeout,
       "rlRadiusServerRetries": rlRadiusServerRetries,
       "rlRadiusServerDeadtime": rlRadiusServerDeadtime,
       "rlRadiusServerUseGlobalDefaultKey": rlRadiusServerUseGlobalDefaultKey,
       "rlRadiusServerKey": rlRadiusServerKey,
       "rlRadiusServerSource": rlRadiusServerSource,
       "rlRadiusServerPriority": rlRadiusServerPriority,
       "rlRadiusServerStatus": rlRadiusServerStatus,
       "rlRadiusServerUsage": rlRadiusServerUsage,
       "rlRadiusServerInetTable": rlRadiusServerInetTable,
       "rlRadiusServerInetEntry": rlRadiusServerInetEntry,
       "rlRadiusServerInetAddressType": rlRadiusServerInetAddressType,
       "rlRadiusServerInetAddress": rlRadiusServerInetAddress,
       "rlRadiusServerInetAuthPortNumber": rlRadiusServerInetAuthPortNumber,
       "rlRadiusServerInetAcctPortNumber": rlRadiusServerInetAcctPortNumber,
       "rlRadiusServerInetTimeout": rlRadiusServerInetTimeout,
       "rlRadiusServerInetRetries": rlRadiusServerInetRetries,
       "rlRadiusServerInetDeadtime": rlRadiusServerInetDeadtime,
       "rlRadiusServerInetUseGlobalDefaultKey": rlRadiusServerInetUseGlobalDefaultKey,
       "rlRadiusServerInetKey": rlRadiusServerInetKey,
       "rlRadiusServerInetSourceType": rlRadiusServerInetSourceType,
       "rlRadiusServerInetSource": rlRadiusServerInetSource,
       "rlRadiusServerInetPriority": rlRadiusServerInetPriority,
       "rlRadiusServerInetStatus": rlRadiusServerInetStatus,
       "rlRadiusServerInetUsage": rlRadiusServerInetUsage,
       "rlRadiusServerInetLastResponseTime": rlRadiusServerInetLastResponseTime,
       "rlRadiusGlobalIPv6DefaultSource": rlRadiusGlobalIPv6DefaultSource,
       "rlAAAEapMethodListTable": rlAAAEapMethodListTable,
       "rlAAAEapMethodListEntry": rlAAAEapMethodListEntry,
       "rlAAAEapMethodListName": rlAAAEapMethodListName,
       "rlAAAEapMethodType1": rlAAAEapMethodType1,
       "rlAAAEapMethodType2": rlAAAEapMethodType2,
       "rlAAAEapMethodType3": rlAAAEapMethodType3,
       "rlAAAEapMethodType4": rlAAAEapMethodType4,
       "rlAAAEapMethodType5": rlAAAEapMethodType5,
       "rlAAAEapMethodListStatus": rlAAAEapMethodListStatus,
       "rlAAAEapCurrentMethodList": rlAAAEapCurrentMethodList}
)
